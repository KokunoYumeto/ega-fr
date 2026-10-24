# PDF content and navigation signatures.
from decimal import Decimal
import hashlib
import json
sha = lambda b: hashlib.sha256(b).hexdigest().upper()

def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def streams(doc, page):
    return [hashlib.sha256(doc.xref_stream(x)).hexdigest() for x in doc[page].get_contents()]


class RawAnnotationPDF:
    """Exact PDF annotation semantics, independent of viewer API presentation.

    PyMuPDF reports named GoTo coordinates in PDF space but direct GoTo
    coordinates in viewer space. Resolve raw names before comparing; retain
    every annotation/action field, full fit operands and null versus zero.
    This checker never edits PDF objects or writes a PDF.
    """
    def __init__(self, path):
        from pypdf import PdfReader
        from pypdf.generic import (ArrayObject, BooleanObject, ByteStringObject,
            DictionaryObject, FloatObject, IndirectObject, NameObject,
            NullObject, NumberObject, TextStringObject)
        self.types = dict(array=ArrayObject, boolean=BooleanObject, bytes=ByteStringObject,
            dictionary=DictionaryObject, float=FloatObject, indirect=IndirectObject,
            name=NameObject, null=NullObject, number=NumberObject, text=TextStringObject)
        self.reader = PdfReader(path, strict=True)
        self.pages = {self.refkey(p.indirect_reference): n for n, p in enumerate(self.reader.pages)}
        require(len(self.pages) == len(self.reader.pages), 'Ambiguous repeated page object in annotation destination map')
        self.names = {}
        catalog = self.reader.root_object
        def add(name, value):
            require(str(name) not in self.names, 'Duplicate raw named destination')
            self.names[str(name)] = value
        def walk(value):
            node = self.obj(value)
            pairs = self.obj(node.get('/Names', []))
            require(len(pairs) % 2 == 0, 'Odd named destination pair list')
            for i in range(0, len(pairs), 2):
                add(pairs[i], pairs[i + 1])
            for child in self.obj(node.get('/Kids', [])):
                walk(child)
        if '/Names' in catalog and '/Dests' in self.obj(catalog['/Names']):
            walk(self.obj(catalog['/Names'])['/Dests'])
        if '/Dests' in catalog:
            for key, value in self.obj(catalog['/Dests']).items():
                add(key, value)

    def obj(self, value):
        return value.get_object() if isinstance(value, self.types['indirect']) else value

    def refkey(self, value):
        return (value.idnum, value.generation) if isinstance(value, self.types['indirect']) else None

    def destination(self, value, offset=0):
        seen = set()
        while True:
            value = self.obj(value)
            if isinstance(value, self.types['dictionary']):
                require('/D' in value, 'Raw destination dictionary missing /D')
                value = value['/D']
                continue
            if isinstance(value, self.types['array']):
                break
            require(isinstance(value, (self.types['name'], self.types['text'])), 'Unknown named destination type')
            key = str(value)
            if key not in self.names and isinstance(value, self.types['name']) and key.startswith('/'):
                key = key[1:]
            require(key in self.names and key not in seen, 'Unresolved or cyclic raw name: ' + key)
            seen.add(key)
            value = self.names[key]
        require(len(value) >= 2, 'Incomplete local destination array')
        first = value[0]
        if isinstance(first, self.types['indirect']):
            require(self.refkey(first) in self.pages, 'Local destination reference absent from page tree')
            page = self.pages[self.refkey(first)]
        else:
            target = self.obj(first)
            require(hasattr(target, 'indirect_reference') and self.refkey(target.indirect_reference) in self.pages,
                    'Local destination is not a page reference')
            page = self.pages[self.refkey(target.indirect_reference)]
        return {'page': page + offset, 'fit_operands': [self.atom(x, offset) for x in value[1:]]}

    def atom(self, value, offset=0):
        t = self.types
        if isinstance(value, t['indirect']) and self.refkey(value) in self.pages:
            return {'type': 'page', 'value': self.pages[self.refkey(value)] + offset}
        value = self.obj(value)
        if isinstance(value, t['null']) or value is None:
            return {'type': 'null'}
        if isinstance(value, t['boolean']):
            return {'type': 'boolean', 'value': value.value}
        if isinstance(value, (t['number'], t['float'], int, float, Decimal)):
            return {'type': 'number', 'value': str(Decimal(str(value)).normalize())}
        if isinstance(value, t['name']):
            return {'type': 'name', 'value': str(value)}
        if isinstance(value, t['bytes']):
            return {'type': 'bytes', 'hex': bytes(value).hex()}
        if isinstance(value, (t['text'], str)):
            return {'type': 'string', 'value': str(value)}
        if isinstance(value, (t['array'], list)):
            return [self.atom(x, offset) for x in value]
        if isinstance(value, t['dictionary']):
            require(not hasattr(value, 'get_data'), 'Unexpected stream in annotation dictionary')
            return {str(k): self.atom(v, offset) for k, v in sorted(value.items())}
        raise RuntimeError('Unsupported annotation field: ' + type(value).__name__)

    def action(self, value, offset=0):
        value = self.obj(value)
        if isinstance(value, self.types['array']):
            return [self.action(x, offset) for x in value]
        require(isinstance(value, self.types['dictionary']), 'Action must be a dictionary')
        result = {}
        for key, val in sorted(value.items()):
            if key == '/D' and value.get('/S') == '/GoTo':
                result[key] = self.destination(val, offset)
            elif key == '/Next':
                result[key] = self.action(val, offset)
            else:
                result[key] = self.atom(val, offset)
        return result

    def annotation(self, value, offset=0):
        value = self.obj(value)
        result = {}
        for key, val in sorted(value.items()):
            if key == '/Dest':
                result[key] = self.destination(val, offset)
            elif key == '/A':
                result[key] = self.action(val, offset)
            elif key == '/AA':
                result[key] = {str(n): self.action(a, offset) for n, a in sorted(self.obj(val).items())}
            else:
                result[key] = self.atom(val, offset)
        return result

    def annotations(self, page, offset=0):
        return [self.annotation(a, offset)
                for a in self.obj(self.reader.pages[page].get('/Annots', []))]


def check_segments(segments, target, helper, paint_validator, shift=0, annotation_transform=None):
    """Every stream/resource/text/pagebox/link survives composition exactly."""
    import fitz
    import pikepdf
    count, links = 0, 0
    combined_annotations = RawAnnotationPDF(target)
    with fitz.open(target) as combined, pikepdf.open(target) as combined_objects:
        combined_paint = paint_validator.PaintResources(combined_objects)
        for segment in segments:
            original_annotations = RawAnnotationPDF(segment)
            with fitz.open(segment) as original, pikepdf.open(segment) as original_objects:
                original_paint = paint_validator.PaintResources(original_objects)
                for i in range(len(original)):
                    j = shift + count + i
                    a, b = original[i], combined[j]
                    require(streams(original, i) == streams(combined, j), f'Composition changed streams: {segment}:{i}')
                    require(original_paint.page(i) == combined_paint.page(j), f'Composition changed paint resources: {segment}:{i}')
                    require(a.get_text() == b.get_text(), f'Composition changed text: {segment}:{i}')
                    require(list(a.mediabox) == list(b.mediabox) and list(a.cropbox) == list(b.cropbox) and a.rotation == b.rotation,
                            f'Composition changed geometry: {segment}:{i}')
                    before = original_annotations.annotations(i, shift + count)
                    if annotation_transform is not None: before = annotation_transform(before)
                    after = combined_annotations.annotations(j)
                    require(before == after, f'Composition changed exact annotation semantics: {segment}:{i}')
                    links += len(before)
                count += len(original)
        require(len(combined) == count + shift, 'Composition page count mismatch')
    return {'pages': count, 'links': links, 'decoded_streams_resources_text_geometry_exact': True,
            'annotations_equal_explicit_expected_rebinding': True, 'cross_component_rebinding_applied': annotation_transform is not None,
            'target_page_shift': shift, 'annotation_policy': 'EXACT_RAW_PAGE_FIT_NULL_RECT_AND_COMPLETE_ACTION_ATTRIBUTES'}


class PaintResources:
    """Compare decoded resource semantics independently of object numbers.

    Content bytes alone do not protect fonts, images, forms, colour profiles or
    transparency. Hash their recursive decoded content, memoized per indirect
    object. Compression encoding and Length are not painting semantics.
    """
    def __init__(self, document):
        self.document = document
        self.cache = {}
        self.active = set()

    def value(self, value):
        import pikepdf
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        objgen = getattr(value, "objgen", (0, 0))
        if objgen != (0, 0):
            if objgen in self.cache:
                return {"object_semantic_sha256": self.cache[objgen]}
            require(objgen not in self.active, "cyclic paint resource requires explicit analysis")
            self.active.add(objgen)
        if isinstance(value, pikepdf.Stream):
            row = {"type": "stream", "decoded_bytes": len(value.read_bytes()),
                   "decoded_sha256": sha(value.read_bytes()),
                   "dictionary": {str(k): self.value(v) for k, v in value.items()
                                  if str(k) not in {"/Length", "/Filter", "/DecodeParms"}}}
        elif isinstance(value, pikepdf.Dictionary):
            row = {"type": "dictionary", "entries": {str(k): self.value(v) for k, v in value.items()}}
        elif isinstance(value, pikepdf.Array):
            row = {"type": "array", "items": [self.value(v) for v in value]}
        elif isinstance(value, pikepdf.String):
            row = {"type": "string", "raw_hex": bytes(value).hex()}
        else:
            row = {"type": str(getattr(value, "_type_name", type(value).__name__)), "value": str(value)}
        digest = sha(json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
        if objgen != (0, 0):
            self.active.remove(objgen)
            self.cache[objgen] = digest
        return {"object_semantic_sha256": digest}

    def page(self, index):
        obj = self.document.pages[index].obj
        appearances = [self.value(a.get("/AP")) for a in obj.get("/Annots", [])]
        row = {"resources": self.value(obj.get("/Resources")), "group": self.value(obj.get("/Group")),
               "annotation_appearances": appearances}
        return sha(json.dumps(row, sort_keys=True, separators=(",", ":")).encode("utf-8"))

