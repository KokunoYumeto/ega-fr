"""Bind a finite declared set of remote references inside the cumulative PDF.

Standalone components use named links to the accompanying cumulative reader.
Composition converts only the declared file/destination pairs into local GoTo
actions. All annotation fields other than these exact routing fields survive.
"""
import copy
from collections import Counter
from decimal import Decimal
from pypdf.generic import ArrayObject, DictionaryObject, FloatObject, NameObject, NullObject, NumberObject

def require(ok,message):
    if not ok: raise RuntimeError(message)

def references(spec):
    return {r['destination']:r for r in spec['references']}

def signature_operand(value):
    kind,*rest=value
    if kind=='null': return NullObject()
    number,=rest
    if kind=='name': return NameObject(number)
    require(kind=='number','Unknown destination operand')
    dec=Decimal(number)
    return NumberObject(int(dec)) if dec==dec.to_integral_value() else FloatObject(number)

def rebind(writer,expected_names,spec):
    allowed=references(spec);counts=Counter();rows=[]
    require(len(allowed)==len(spec['references']) and len(allowed)>0,'Unique declared target identities required')
    require(all(isinstance(r['occurrences'],int) and r['occurrences']>0 for r in spec['references']),'Positive exact multiplicities required')
    require(sum(r['occurrences'] for r in spec['references'])==spec['total_source_annotations'],'Declared total differs')
    for n,page in enumerate(writer.pages):
        for annotation in page.get('/Annots',[]):
            annotation=annotation.get_object()
            if '/A' not in annotation: continue
            action=annotation['/A'].get_object()
            if action.get('/S')!='/GoToR' or str(action.get('/F'))!=spec['cumulative_filename']:continue
            target=str(action.get('/D'))
            require(target in allowed and target in expected_names,'Missing or undeclared cross-component target: '+target)
            require(set(action)<= {'/S','/F','/D','/NewWindow'},'Unreviewed remote action attribute')
            sig=expected_names[target]
            destination=ArrayObject([writer.pages[sig['page']].indirect_reference,*[signature_operand(x) for x in sig['fit']]])
            annotation[NameObject('/A')]=DictionaryObject({NameObject('/S'):NameObject('/GoTo'),NameObject('/D'):destination})
            counts[target]+=1;rows.append(dict(source_page=n+1,destination=target,target_page=sig['page']+1))
    wanted={r['destination']:r['occurrences'] for r in spec['references']}
    require(dict(counts)==wanted,'Cross-component annotation multiplicities differ')
    return dict(rebound_count=sum(counts.values()),bindings=rows,source_counts=dict(counts),file=spec['cumulative_filename'])

def expected_annotations(before,expected_names,spec):
    """Independent semantic expectation for exact raw-annotation comparison."""
    result=copy.deepcopy(before);allowed=references(spec)
    for annotation in result:
        action=annotation.get('/A',{})
        if action.get('/S')!={'type':'name','value':'/GoToR'}:continue
        if action.get('/F')!={'type':'string','value':spec['cumulative_filename']}:continue
        destination=action.get('/D',{})
        require(destination.get('type')=='string','Cross-component destination must be named')
        target=destination['value']
        require(target in allowed and target in expected_names,'Unresolved expected cross-component reference')
        require(set(action)<= {'/S','/F','/D','/NewWindow'},'Unexpected raw action attribute')
        sig=expected_names[target];operands=[]
        for kind,*value in sig['fit']:
            operands.append({'type':kind,**({'value':value[0]} if value else {})})
        annotation['/A']={'/S':{'type':'name','value':'/GoTo'},'/D':{'page':sig['page'],'fit_operands':operands}}
    return result
