import json,glob,sys
needle = sys.argv[1]
for fn in sorted(glob.glob('findings_*.json')):
    d=json.load(open(fn,encoding='utf-8'))
    for x in d:
        s=json.dumps(x,ensure_ascii=False)
        f = x.get('fix') or {}
        if needle in (f.get('new') or '') or needle in (x.get('note') or ''):
            print(fn, s[:700])
            print()
