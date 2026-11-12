import json, glob, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
pat = sys.argv[1]
globs = sys.argv[2:]
n = 0
for g in globs:
    for f in sorted(glob.glob(g)):
        if f.endswith('.orig'):
            continue
        try:
            d = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print('ERR', f, e)
            continue
        for x in d:
            fx = x.get('fix') or {}
            if pat in (fx.get('new') or ''):
                n += 1
                if n < 25:
                    print(os.path.basename(f), x.get('page'), x.get('kind'), repr(fx.get('old'))[:200], '->', repr(fx.get('new'))[:200])
                    print('    NOTE:', (x.get('note') or '')[:300])
print('total', n)
