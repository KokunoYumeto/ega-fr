import json, glob, re, sys
pat = re.compile(sys.argv[1])
n = 0
for f in sorted(glob.glob('findings_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        fx = x.get('fix') or {}
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            n += 1
            if n <= int(sys.argv[2]) if len(sys.argv) > 2 else 15:
                print(f, x.get('page'), '|', x.get('kind'), x.get('convention'), '|', x.get('where'), '|', json.dumps(fx, ensure_ascii=False)[:300], '|', (x.get('note') or '')[:200])
                print()
print(n)
