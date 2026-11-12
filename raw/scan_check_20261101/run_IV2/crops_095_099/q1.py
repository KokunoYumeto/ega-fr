import json,glob,sys
n=0
for f in sorted(glob.glob('run_IV2/findings_*.json')):
    d=json.load(open(f,encoding='utf-8'))
    for x in d:
        fx=x.get('fix') or {}
        new=fx.get('new') or ''
        if '_{\mathbf{k}' in new or '_{\mathbf k' in new or '\mathbf{k}(' in new:
            if n<8: print(f, json.dumps(x,ensure_ascii=False)[:700]); print()
            n+=1
print(n)
