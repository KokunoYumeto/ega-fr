import json,glob
n=0
for f in sorted(glob.glob('run_IV2/findings_*.json')):
    d=json.load(open(f,encoding='utf-8'))
    for x in d:
        s=json.dumps(x,ensure_ascii=False)
        if 'subsection' in s:
            if n<6: print(f, s[:600]); print()
            n+=1
print(n)
