"""Assemble five native documents behind a compiled LaTeX cover.

All historical alias names retain their component identity, even after reflow.
No mathematical text is re-expressed. No promotion or publication is performed.
Run under a bounded process guard for full-volume operation.
"""
from pathlib import Path
import argparse
import hashlib
import json
import pypdf
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, NameObject, TextStringObject
import merge_french_namespaced as old
import outline_metadata as navigation
import page_integrity as integrity
import cross_component_links as crosslinks
import extra_legacy_destinations as extra_destinations

IDS = ('base','iv1','iv2','iv3','iv4')
TITLE = 'Éléments de géométrie algébrique — Édition française corrigée'

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def identity(p):
    b=Path(p).read_bytes()
    return dict(path=str(Path(p).resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest().upper())

def model(paths, legacy, shift):
    require(len(paths)==5 and len(set(map(str, paths)))==5, 'Five distinct ordered components required')
    require(legacy['component_ids']==list(IDS), 'Unexpected legacy component order')
    readers=[PdfReader(p, strict=True) for p in paths]
    offsets=[]; names=[]; expected={}; outlines=[]; offset=shift
    for component, reader in zip(IDS, readers, strict=True):
        offsets.append(offset)
        local=reader.named_destinations
        extra_destinations.augment(reader,local,component,legacy,paths[IDS.index(component)])
        require(local, 'Missing destinations: '+component)
        names.append(local)
        for name,destination in local.items():
            expected[old.PREFIX+component+':'+name]=old._destination(reader,destination,offset)
        outlines.extend(old._outline(reader,offset))
        offset+=len(reader.pages)
    alias_keys=set()
    moved=[]
    for row in legacy['aliases']:
        name=row['name']; component=row['component']
        require(name not in alias_keys and name not in expected, 'Duplicate/colliding alias: '+name)
        alias_keys.add(name)
        i=IDS.index(component)
        target_name=row.get('target_name',name)
        require(target_name in names[i], 'Legacy destination disappeared from its component: '+target_name)
        current=old._destination(readers[i],names[i][target_name],offsets[i])
        expected[name]=current
        if current['page'] != row['baseline_page']+shift:
            moved.append(dict(name=name,component=component,old_page=row['baseline_page']+shift,new_page=current['page']))
    return dict(readers=readers,offsets=offsets,names=names,expected=expected,
        outlines=outlines,pages=offset,legacy_page_updates=moved)

def validate(path, expected, cover_outline):
    reader=PdfReader(path,strict=True)
    require(len(reader.pages)==expected['pages'],'Page count changed during assembly')
    actual={n:old._destination(reader,d) for n,d in reader.named_destinations.items()}
    require(actual==expected['expected'],'Named destinations changed')
    require(old._outline(reader)==expected['outlines']+cover_outline,'Outline semantics changed')
    return dict(pages=len(reader.pages),named_destinations=len(actual),
        outlines=len(expected['outlines'])+len(cover_outline),
        legacy_page_updates=expected['legacy_page_updates'])

def assemble(paths, cover, legacy, output, metadata):
    require(pypdf.__version__=='6.12.2','Use pinned pypdf 6.12.2')
    output=Path(output)
    require(not output.exists() and output.parent.is_dir(),'Fresh output in existing directory required')
    paths=[Path(p).resolve(strict=True) for p in paths]
    cover=Path(cover).resolve(strict=True)
    require(output.resolve() not in paths+[cover],'Output aliases an input')
    before=[identity(p) for p in paths+[cover]]
    front=PdfReader(cover,strict=True)
    front_pages=len(front.pages)
    require(front_pages>0,'At least one frontmatter page required')
    require(not front.outline and not front.named_destinations,'Cover must not inject names or outlines')
    expected=model(paths,legacy,front_pages)
    writer=PdfWriter()
    for page in front.pages:
        writer.add_page(page)
    materialized=[]
    for component,reader,local in zip(IDS,expected['readers'],expected['names'],strict=True):
        materialized.append(old._materialize(reader,local))
        old._install_namespace(reader,local,component)
        writer.append(reader,import_outline=True)
    restored=navigation.restore_outline_metadata(writer,expected['readers'],shift=front_pages)
    for row in sorted(legacy['aliases'],key=lambda r:r['name']):
        name=row['name']; i=IDS.index(row['component'])
        destination=expected['names'][i][row.get('target_name',name)].dest_array
        page=expected['expected'][name]['page']
        writer.add_named_destination_array(TextStringObject(name),ArrayObject([writer.pages[page].indirect_reference,*destination[1:]]))
    cross_spec=json.loads(Path(__file__).with_name('CROSS_COMPONENT_LINKS.json').read_bytes())
    cross_result=crosslinks.rebind(writer,expected['expected'],cross_spec)
    writer.add_outline_item('Couverture de l’édition complète',0)
    writer.add_outline_item('Lecteur cumulatif français',front_pages)
    writer.root_object[NameObject('/PageMode')]=NameObject('/UseOutlines')
    require(metadata.get('/Title')==TITLE,'Incorrect French edition title')
    require(metadata.get('/Author')=='Alexandre Grothendieck et Jean Dieudonné','Incorrect author attribution')
    require(bool(metadata.get('/Creator')),'Exact production attribution required')
    writer.add_metadata(metadata)
    with output.open('xb') as f:
        writer.write(f)
    extra=old.default_cover_outline_signatures()
    extra[1]['page']=front_pages
    nav=validate(output,expected,extra)
    body=integrity.check_segments(paths,output,None,integrity,shift=front_pages,annotation_transform=lambda a: crosslinks.expected_annotations(a,expected['expected'],cross_spec))
    # Cover text/paint is preserved separately; its external URI annotations are
    # checked in the same exact raw representation as the body annotations.
    import fitz
    import pikepdf
    a=integrity.RawAnnotationPDF(cover);b=integrity.RawAnnotationPDF(output)
    with fitz.open(cover) as first,fitz.open(output) as final,pikepdf.open(cover) as ap,pikepdf.open(output) as bp:
        for page in range(front_pages):
            require(integrity.streams(first,page)==integrity.streams(final,page),'Cover streams changed')
            require(first[page].get_text()==final[page].get_text(),'Cover text changed')
            require(list(first[page].mediabox)==list(final[page].mediabox) and list(first[page].cropbox)==list(final[page].cropbox) and first[page].rotation==final[page].rotation,'Cover geometry changed')
            require(integrity.PaintResources(ap).page(page)==integrity.PaintResources(bp).page(page),'Cover resources changed')
            require(a.annotations(page)==b.annotations(page),'Cover annotations changed')
    require([identity(p) for p in paths+[cover]]==before,'Input changed during assembly')
    return dict(status='PASS_ASSEMBLY_INTEGRITY__CONTENT_AND_VISUAL_RELEASE_QA_SEPARATE',
        output=identity(output),inputs=before,navigation=nav,body_integrity=body,
        outline_restoration=restored,materialized_references=materialized,cross_component_rebinding=cross_result,
        source_mutation=False,publication=False)

def main():
    p=argparse.ArgumentParser(description='Assembler le lecteur français sans modifier les cinq composantes.')
    p.add_argument('--components',nargs=5,required=True,type=Path)
    p.add_argument('--cover',required=True,type=Path)
    p.add_argument('--legacy',type=Path,default=Path(__file__).with_name('LEGACY_ALIASES.json'))
    p.add_argument('--metadata',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    a=p.parse_args()
    receipt=a.output.with_suffix('.assembly.json')
    require(not receipt.exists(),'Receipt already exists')
    result=assemble(a.components,a.cover,json.loads(a.legacy.read_bytes()),a.output,json.loads(a.metadata.read_bytes()))
    with receipt.open('x',encoding='utf-8',newline='\n') as f:
        json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')

if __name__=='__main__': main()
