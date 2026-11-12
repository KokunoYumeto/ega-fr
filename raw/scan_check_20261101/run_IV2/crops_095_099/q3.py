import json,glob
from collections import Counter
c=Counter(); ex={}
for f in sorted(glob.glob('run_IV2/findings_*.json')):
    d=json.load(open(f,encoding='utf-8'))
    for x in d:
        s=json.dumps(x,ensure_ascii=False)
        if 'paragraph' in (x.get('where','')+x.get('scan','')+x.get('note','') if x.get('note') else x.get('where','')+x.get('scan','')).lower():
            c[x['kind']]+=1
            ex.setdefault(x['kind'], (f, s[:500]))
print(c)
for k,v in ex.items(): print(k, v); print()
