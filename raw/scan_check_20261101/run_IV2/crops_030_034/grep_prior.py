import json, glob, re, sys
pat = re.compile(sys.argv[1])
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 8
n = 0
for f in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        new = fx.get('new', '') if isinstance(fx, dict) else ''
        if pat.search(new):
            print(f, json.dumps(x, ensure_ascii=False)[:420]); n += 1
            if n >= lim: sys.exit()
print(n)
