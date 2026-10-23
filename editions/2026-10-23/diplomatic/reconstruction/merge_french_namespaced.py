"""Namespaced, outline-preserving French EGA assembly proposal.

Only merge() writes a PDF, exclusively to its supplied fresh output path.
No source PDF is modified. The caller owns the mutexes, memory guard, dates,
visual QA, and promotion. validate() and expected_navigation() are read-only.

Installed pypdf 6.12.2 APIs reviewed: PdfWriter.append/merge,
_merge__process_named_dests, _insert_filtered_annotations,
_get_filtered_outline, _insert_filtered_outline, add_named_destination_array,
PdfReader.named_destinations/_build_outline_item, Destination.dest_array.
"""
from __future__ import annotations

from collections import Counter
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (ArrayObject, BooleanObject, DictionaryObject, FloatObject,
                          IndirectObject, NameObject, NullObject, NumberObject,
                          TextStringObject)

COMPONENT_IDS = ('base', 'iv1', 'iv2', 'iv3', 'iv4')
PREFIX = 'ega-fr:'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def _identity(path):
    path = Path(path)
    raw = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest().upper()}


def _obj(value):
    return value.get_object() if isinstance(value, IndirectObject) else value


def _scalar(value):
    value = _obj(value)
    if isinstance(value, NullObject) or value is None:
        return ['null']
    if isinstance(value, (NumberObject, FloatObject, int, float, Decimal)):
        return ['number', str(Decimal(str(value)).normalize())]
    if isinstance(value, NameObject):
        return ['name', str(value)]
    raise RuntimeError(f'Unsupported destination operand: {type(value).__name__}')


def _destination(reader, destination, offset=0):
    """Exact semantic page/fit signature, including null versus zero operands."""
    page = reader.get_destination_page_number(destination)
    require(page is not None and 0 <= page < len(reader.pages), 'Destination has no local page')
    array = destination.dest_array
    require(len(array) >= 2, 'Incomplete destination array')
    return {'page': page + offset, 'fit': [_scalar(x) for x in array[1:]]}


def _outline(reader, offset=0):
    rows = []
    def visit(items, level):
        for item in items:
            if isinstance(item, list):
                visit(item, level + 1)
                continue
            sig = _destination(reader, item, offset)
            rows.append({'level': level, 'title': str(item.title), **sig,
                         'style': int(item.get('/F', 0)),
                         'color': [_scalar(x) for x in item.get('/C', [])],
                         'open': (item['/%is_open%'].value if isinstance(item.get('/%is_open%'), BooleanObject)
                                  else bool(item.get('/%is_open%', True)))})
    visit(reader.outline, 1)
    return rows


def _models(components, baseline_body):
    paths = [Path(p).resolve(strict=True) for p in components]
    require(len(paths) == len(COMPONENT_IDS) and len(set(paths)) == 5,
            'French assembly requires exactly base, IV-1, IV-2, IV-3, IV-4')
    readers = [PdfReader(path, strict=True) for path in paths]
    offsets, offset = [], 0
    names, expected_names, expected_outline = [], {}, []
    for component_id, reader in zip(COMPONENT_IDS, readers, strict=True):
        offsets.append(offset)
        local = reader.named_destinations
        names.append(local)
        require(local, f'No named destinations in component {component_id}')
        for name, destination in local.items():
            key = PREFIX + component_id + ':' + name
            require(key not in expected_names, 'Duplicate prefixed destination')
            expected_names[key] = _destination(reader, destination, offset)
        expected_outline.extend(_outline(reader, offset))
        offset += len(reader.pages)
    baseline = PdfReader(Path(baseline_body), strict=True)
    require(len(baseline.pages) == offset, 'Baseline body page topology changed')
    aliases = {}
    for name, destination in baseline.named_destinations.items():
        require(not name.startswith(PREFIX), 'Historical alias conflicts with namespace')
        old = _destination(baseline, destination)
        matches = [i for i, (start, reader) in enumerate(zip(offsets, readers))
                   if start <= old['page'] < start + len(reader.pages)]
        require(len(matches) == 1, f'Cannot locate baseline alias component: {name}')
        index = matches[0]
        require(name in names[index], f'Baseline alias is absent in intended component: {name}')
        current = _destination(readers[index], names[index][name], offsets[index])
        # An accepted current source correction can move a named anchor within
        # its page. Preserve key and original component/name identity, but use
        # that anchor's current fit coordinates. This recipe has fixed pages.
        require(current['page'] == old['page'], f'Baseline alias source page moved: {name}')
        require(name not in expected_names, f'Alias collision with prefixed destination: {name}')
        aliases[name] = {'component_index': index, 'component_id': COMPONENT_IDS[index],
                         'original_name': name, 'signature': current,
                         'baseline_signature': old, 'coordinates_updated': current != old}
        expected_names[name] = current
    return paths, readers, names, offsets, baseline, aliases, expected_names, expected_outline


def expected_navigation(components, baseline_body):
    """Read-only expected destination/outline definitions for independent replay."""
    paths, readers, names, offsets, baseline, aliases, expected, outlines = _models(components, baseline_body)
    return {'components': [_identity(p) for p in paths],
            'baseline_body': _identity(baseline_body), 'component_ids': list(COMPONENT_IDS),
            'component_offsets': offsets, 'pages': sum(len(r.pages) for r in readers),
            'prefixed_name_count': sum(len(n) for n in names),
            'preserved_legacy_alias_count': len(aliases),
            'legacy_alias_coordinate_updates': [
                {'legacy_key': name, 'component_id': info['component_id'],
                 'current_prefixed_key': PREFIX + info['component_id'] + ':' + info['original_name'],
                 'baseline': info['baseline_signature'], 'current': info['signature']}
                for name, info in sorted(aliases.items()) if info['coordinates_updated']],
            'named_destinations': expected, 'outlines': outlines}


def default_cover_outline_signatures():
    """The parent's two final appended PdfWriter.add_outline_item defaults.

    Installed pypdf 6.12.2 default is PAGE_FIT (/Fit, no numeric operands),
    no style/color, open=True. Pages are final zero-based indices.
    """
    return [{'level': 1, 'title': title, 'page': page,
             'fit': [['name', '/Fit']], 'style': 0, 'color': [], 'open': True}
            for title, page in [('Couverture de l’édition complète', 0),
                                ('Lecteur cumulatif français', 1)]]


def _materialize(reader, names):
    """Resolve local named actions before any destination namespace mutation."""
    stats = Counter()
    seen_actions, seen_nodes = set(), set()

    def resolve(value):
        value = _obj(value)
        if isinstance(value, DictionaryObject) and '/D' in value:
            return resolve(value['/D'])
        if isinstance(value, ArrayObject):
            return value
        require(isinstance(value, (TextStringObject, NameObject, str)),
                f'Unsupported local destination kind: {type(value).__name__}')
        text = str(value)
        keys = [text]
        if isinstance(value, NameObject) and text.startswith('/'):
            keys.append(text[1:])
        hits = [key for key in keys if key in names]
        require(len(hits) == 1, f'Missing or ambiguous original named destination: {text}')
        stats['named_references_materialized'] += 1
        return ArrayObject(names[hits[0]].dest_array)

    def action(value):
        value = _obj(value)
        if isinstance(value, ArrayObject):
            for child in value:
                action(child)
            return
        require(isinstance(value, DictionaryObject), 'Malformed action dictionary')
        marker = id(value)
        if marker in seen_actions:
            return
        seen_actions.add(marker)
        if value.get('/S') == '/GoTo':
            require('/D' in value, 'Local GoTo action has no /D')
            value[NameObject('/D')] = resolve(value['/D'])
        if '/Next' in value:
            action(value['/Next'])

    def node_actions(node):
        if '/Dest' in node:
            node[NameObject('/Dest')] = resolve(node['/Dest'])
        if '/A' in node:
            action(node['/A'])
        if '/AA' in node:
            aa = _obj(node['/AA'])
            require(isinstance(aa, DictionaryObject), 'Malformed additional actions')
            for child in aa.values():
                action(child)

    for page in reader.pages:
        node_actions(page)
        for annotation in page.get('/Annots', []):
            node_actions(_obj(annotation))

    def outline_nodes(value):
        if value is None:
            return
        node = _obj(value)
        require(isinstance(node, DictionaryObject), 'Malformed outline node')
        marker = id(node)
        require(marker not in seen_nodes, 'Outline cycle or multiply-linked node')
        seen_nodes.add(marker)
        node_actions(node)
        if '/First' in node:
            outline_nodes(node['/First'])
        if '/Next' in node:
            outline_nodes(node['/Next'])
    if '/Outlines' in reader.root_object:
        outline_nodes(reader.root_object['/Outlines'])
    if '/OpenAction' in reader.root_object:
        opening = _obj(reader.root_object['/OpenAction'])
        if isinstance(opening, DictionaryObject):
            action(opening)
        else:
            reader.root_object[NameObject('/OpenAction')] = resolve(opening)
    return dict(stats)


def _install_namespace(reader, local, component_id):
    root = reader.root_object
    catalog_names = root.get('/Names')
    catalog_names = _obj(catalog_names) if catalog_names is not None else DictionaryObject()
    require(isinstance(catalog_names, DictionaryObject), 'Malformed catalog /Names')
    pairs = ArrayObject()
    for name in sorted(local):
        pairs.extend([TextStringObject(PREFIX + component_id + ':' + name),
                      ArrayObject(local[name].dest_array)])
    catalog_names[NameObject('/Dests')] = DictionaryObject({NameObject('/Names'): pairs})
    root[NameObject('/Names')] = catalog_names
    if '/Dests' in root:
        del root['/Dests']
    # PdfReader 6.12.2 assumes its name tree is static and caches it. We changed
    # only the in-memory reader, so invalidate the reviewed cache explicitly.
    require(hasattr(reader, '_named_destinations_cache'), 'Unreviewed pypdf name-cache API')
    reader._named_destinations_cache = None
    require(set(reader.named_destinations) == {PREFIX + component_id + ':' + n for n in local},
            'Namespace replacement did not yield the exact original definition set')


def validate(output, components, baseline_body, shift=0, extra_outlines=None):
    """Validate all prefixed definitions, legacy aliases, and full outline tree.

    For a final PDF containing a cover pass shift=1 and the exact extra outline
    rows added by the caller (at the end), using the same signature schema.
    """
    model = expected_navigation(components, baseline_body)
    actual = PdfReader(Path(output), strict=True)
    require(len(actual.pages) == model['pages'] + shift, 'Navigation page count mismatch')
    observed_names = {name: _destination(actual, dest) for name, dest in actual.named_destinations.items()}
    expected_names = {name: {**sig, 'page': sig['page'] + shift}
                      for name, sig in model['named_destinations'].items()}
    require(observed_names == expected_names, 'Named destination keys or exact page/fit operands changed')
    wanted_outline = [{**row, 'page': row['page'] + shift} for row in model['outlines']]
    wanted_outline.extend(extra_outlines or [])
    require(_outline(actual) == wanted_outline, 'Outline title/order/hierarchy/page/fit/style changed')
    definitions = json.dumps({'names': expected_names, 'outlines': wanted_outline},
                             ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    return {'result': 'PASS_ALL_PREFIXED_NAMES_LEGACY_ALIASES_AND_OUTLINES',
            'pages': len(actual.pages), 'prefixed_names': model['prefixed_name_count'],
            'legacy_aliases': model['preserved_legacy_alias_count'],
            'total_names': len(observed_names), 'outline_entries': len(wanted_outline),
            'legacy_alias_coordinate_updates': model['legacy_alias_coordinate_updates'],
            'navigation_definition_sha256': hashlib.sha256(definitions).hexdigest().upper(),
            'cover_page_shift': shift}


def merge(output, components, baseline_body):
    """Create one new PDF body; no overwrite, no promotion, no publication."""
    output = Path(output).resolve()
    require(output.parent.is_dir() and not output.exists(), 'Output must be a fresh file in an existing directory')
    paths, readers, names, offsets, baseline, aliases, expected, outlines = _models(components, baseline_body)
    require(output not in paths and output != Path(baseline_body).resolve(), 'Output aliases an input PDF')
    before = [_identity(p) for p in paths] + [_identity(baseline_body)]
    writer = PdfWriter()
    materialized = []
    for component_id, reader, local in zip(COMPONENT_IDS, readers, names, strict=True):
        stats = _materialize(reader, local)
        _install_namespace(reader, local, component_id)
        writer.append(reader, import_outline=True)
        materialized.append({'component_id': component_id, **stats})
    for name in sorted(aliases):
        info = aliases[name]
        index = info['component_index']
        source_dest = names[index][name].dest_array
        array = ArrayObject([writer.pages[info['signature']['page']].indirect_reference,
                             *source_dest[1:]])
        writer.add_named_destination_array(TextStringObject(name), array)
    # Retain the pinned baseline body's human metadata. Caller sets successor
    # dates on the final covered PDF, after its own cover construction.
    writer.add_metadata({str(k): str(v) for k, v in (baseline.metadata or {}).items()
                         if isinstance(v, str)})
    require([_identity(p) for p in paths] + [_identity(baseline_body)] == before,
            'Input PDF changed before writing')
    with output.open('xb') as stream:
        writer.write(stream)
    proof = validate(output, paths, baseline_body)
    require([_identity(p) for p in paths] + [_identity(baseline_body)] == before,
            'Input PDF changed during assembly')
    return {'output': _identity(output), 'navigation': proof,
            'materialized_references': materialized, 'input_pins': before,
            'source_pdf_mutation': False, 'promotion': False, 'publication': False}
