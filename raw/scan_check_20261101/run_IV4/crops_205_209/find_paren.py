import json, glob, re, sys
pat = sys.argv[1]
n = 0
for f in sorted(glob.glob(sys.argv[2])):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        o = fx.get('old') or ''
        nw = fx.get('new') or ''
        if pat in nw and pat not in o:
            print(f, x['page'], x['kind'], x.get('convention'), '|', o[:80].replace('\n', '|'), '=>', nw[:110].replace('\n', '|'))
            print('    W:', (x.get('where') or '')[:120], '| N:', (x.get('note') or '')[:160])
            n += 1
print(n)
