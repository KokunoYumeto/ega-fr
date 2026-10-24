"""Successor French merger: preserve exact outline presentation after pypdf import.

Only merge() authors a new PDF, and only when invoked by the root build lane.
restore_outline_metadata() fixes an in-memory writer after its caller's import;
it never writes or promotes any file. validate() remains the original exact
destination/title/hierarchy/fit/style/color/open comparator, unchanged.
"""
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import sys
sys.dont_write_bytecode = True

import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DictionaryObject, NameObject, NumberObject, TextStringObject

HERE = Path(__file__).resolve().parent
ORIGINAL = HERE / 'merge_french_namespaced.py'
ORIGINAL_SHA256 = 'E98B99D1E332F2235680028051E98514D3B1743B67991E65CCDF73CE6691EA23'
if hashlib.sha256(ORIGINAL.read_bytes()).hexdigest().upper() != ORIGINAL_SHA256:
    raise RuntimeError('Original reviewed merger recipe changed')
if pypdf.__version__ != '6.12.2':
    raise RuntimeError('Unreviewed pypdf outline API version')
_spec = importlib.util.spec_from_file_location('ega_fr_namespaced_original_r1', ORIGINAL)
_old = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_old)
require = _old.require
_identity = _old._identity
_obj = _old._obj
_outline = _old._outline
_destination = _old._destination
expected_navigation = _old.expected_navigation
default_cover_outline_signatures = _old.default_cover_outline_signatures
validate = _old.validate
COMPONENT_IDS = _old.COMPONENT_IDS
PREFIX = _old.PREFIX


def _outline_nodes(document):
    """Return raw titled nodes in preorder; reject cycles and detached hierarchy."""
    root = _obj(document.root_object.get('/Outlines'))
    if root is None:
        return None, []
    require(isinstance(root, DictionaryObject), 'Malformed /Outlines root')
    result, seen = [], set()

    def walk(value, parent):
        while value is not None:
            node = _obj(value)
            require(isinstance(node, DictionaryObject) and '/Title' in node,
                    'Malformed titled outline node')
            require(id(node) not in seen, 'Outline cycle or repeated child')
            seen.add(id(node))
            require(_obj(node.get('/Parent')) is parent, 'Detached outline parent')
            result.append(node)
            if '/First' in node:
                walk(node['/First'], node)
            value = node.get('/Next')

    if '/First' in root:
        walk(root['/First'], root)
    return root, result


def _metadata(node):
    """Keep absence distinct from explicit default values, including /Count."""
    result = {}
    for key in ('/F', '/C', '/Count'):
        if key in node:
            value = _obj(node[key])
            if key == '/C':
                require(isinstance(value, ArrayObject) and len(value) == 3,
                        'Outline color must have exactly three components')
                result[key] = tuple(_old._scalar(x) for x in value)
            else:
                require(isinstance(value, NumberObject), f'Noninteger outline {key}')
                result[key] = int(value)
    return result


def _restore_nodes(observed, nodes, expected, originals, outline_root):
    """Narrow object-dictionary repair; no destination/link/painting mutation."""
    require(len(observed) == len(nodes) == len(expected) == len(originals),
            'Outline entry count changed before metadata restoration')
    identity_fields = ('level', 'title', 'page', 'fit', 'style')
    for index, (actual, wanted) in enumerate(zip(observed, expected, strict=True)):
        require(all(actual[key] == wanted[key] for key in identity_fields),
                f'Outline semantic identity changed before restoration at row {index}')
    # Validate every original before making any mutation.
    original_metadata = [_metadata(node) for node in originals]
    changed = {'color': 0, 'open': 0, 'raw_metadata': 0}
    for actual, wanted, target, source, metadata in zip(observed, expected, nodes, originals, original_metadata, strict=True):
        changed['color'] += actual['color'] != wanted['color']
        changed['open'] += actual['open'] != wanted['open']
        changed['raw_metadata'] += _metadata(target) != metadata
        for key in ('/F', '/C', '/Count'):
            if key in source:
                value = _obj(source[key])
                target[NameObject(key)] = ArrayObject(value) if key == '/C' else NumberObject(value)
            else:
                target.pop(NameObject(key), None)
        # This pypdf-only cache must not contradict the restored /Count if a
        # caller subsequently appends siblings. It is not a PDF source field.
        target.pop(NameObject('/%is_open%'), None)
        require(_metadata(target) == metadata, 'Exact raw outline metadata restoration failed')
    # A cumulative catalog needs the visible count of the combined forest,
    # rather than the sum of the importer's all-open defaults. Source node
    # /Count values themselves stay byte-value exact, never recomputed.
    visible = 0
    blocked_level = None
    for row in expected:
        level = row['level']
        if blocked_level is not None and level <= blocked_level:
            blocked_level = None
        if blocked_level is None:
            visible += 1
            if not row['open']:
                blocked_level = level
    require(outline_root is not None or not expected, 'Missing output outline root')
    if outline_root is not None:
        outline_root[NameObject('/Count')] = NumberObject(visible)
    return {'entries': len(expected), 'restored': changed, 'visible_outline_entries': visible}


def restore_outline_metadata(writer, sources, shift=0):
    """Restore exact original /C,/F,/Count after importing complete components.

    Call after all original outlines have been imported but before adding any
    new cover outlines. For a cover followed by a full body use sources=[body]
    and shift=1. Source paths or existing PdfReader instances are supported.
    Invariants for titles/order/hierarchy/page/fit/style remain fail-closed.
    """
    require(isinstance(shift, int) and not isinstance(shift, bool) and shift >= 0,
            'Outline page shift must be a nonnegative integer')
    require(sources, 'No original outline sources')
    readers = [source if isinstance(source, PdfReader) else PdfReader(Path(source), strict=True)
               for source in sources]
    expected, originals = [], []
    offset = shift
    for reader in readers:
        _, local_nodes = _outline_nodes(reader)
        rows = _outline(reader, offset)
        require(len(local_nodes) == len(rows), 'Source raw/semantic outline count differs')
        expected.extend(rows)
        originals.extend(local_nodes)
        offset += len(reader.pages)
    root, nodes = _outline_nodes(writer)
    result = _restore_nodes(_outline(writer), nodes, expected, originals, root)
    require(_outline(writer) == expected, 'Full exact outline equality failed after restoration')
    result['result'] = 'PASS_EXACT_ORIGINAL_OUTLINE_METADATA_RESTORED'
    result['page_shift'] = shift
    return result


def merge(output, components, baseline_body):
    """Root-invoked fresh PDF authoring; identical recipe plus exact metadata fix."""
    output = Path(output).resolve()
    require(output.parent.is_dir() and not output.exists(), 'Output must be a fresh file in an existing directory')
    paths, readers, names, offsets, baseline, aliases, expected, outlines = _old._models(components, baseline_body)
    require(output not in paths and output != Path(baseline_body).resolve(), 'Output aliases an input PDF')
    before = [_identity(p) for p in paths] + [_identity(baseline_body)]
    writer = PdfWriter()
    materialized = []
    for component_id, reader, local in zip(COMPONENT_IDS, readers, names, strict=True):
        stats = _old._materialize(reader, local)
        _old._install_namespace(reader, local, component_id)
        writer.append(reader, import_outline=True)
        materialized.append({'component_id': component_id, **stats})
    outline_repair = restore_outline_metadata(writer, readers)
    for name in sorted(aliases):
        info = aliases[name]
        index = info['component_index']
        source_dest = names[index][name].dest_array
        array = ArrayObject([writer.pages[info['signature']['page']].indirect_reference,
                             *source_dest[1:]])
        writer.add_named_destination_array(TextStringObject(name), array)
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
            'outline_metadata_restoration': outline_repair,
            'materialized_references': materialized, 'input_pins': before,
            'source_pdf_mutation': False, 'promotion': False, 'publication': False}
