import json, glob, sys
pat = sys.argv[1]
for f in sorted(glob.glob('findings_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat in s:
            fx = x.get('fix')
            print(f, x.get('page'), x.get('kind'), x.get('convention'), json.dumps(fx, ensure_ascii=False)[:200], '|', (x.get('note') or '')[:160])
