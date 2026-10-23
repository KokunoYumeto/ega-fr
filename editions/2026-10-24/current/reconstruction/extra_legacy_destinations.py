"""Restore a passage-bound destination removed by equation renumbering.

Only the in-memory navigation model is augmented. Source PDFs and page streams
are untouched. Exact component bytes and a unique printed passage are required.
"""
from pathlib import Path
import hashlib,re
import fitz
from pypdf.generic import Destination,Fit,TextStringObject

def augment(reader,local,component,legacy,path):
    rows=[r for r in legacy.get('additional_destinations',[]) if r['component']==component]
    if not rows:return
    raw=Path(path).read_bytes()
    with fitz.open(path) as doc:
        pages=[re.sub(r'\s+','',p.get_text()) for p in doc]
        for row in rows:
            expected=row['component_pdf']
            assert len(raw)==expected['bytes'] and hashlib.sha256(raw).hexdigest().upper()==expected['sha256']
            name=row['name'];p=row['local_page']
            assert name.startswith('canon-legacy.') and name not in local
            assert 0<=p<len(reader.pages) and row['zoom'] is None
            assert 0<=row['left']<=float(doc[p].rect.width) and 0<=row['top']<=float(doc[p].rect.height)
            assert sum(s.count(row['witness_text']) for s in pages)==1
            assert pages[p].count(row['witness_text'])==1
            local[name]=Destination(TextStringObject(name),reader.pages[p].indirect_reference,
                Fit.xyz(row['left'],row['top'],row['zoom']))
