import json, glob, sys
n = 0
pats = sys.argv[1:]
for fn in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for f in d:
        fx = f.get('fix') or {}
        if not isinstance(fx, dict):
            continue
        old = fx.get('old', '') or ''
        new = fx.get('new', '') or ''
        if all(p in old + ' ||| ' + new for p in pats):
            if n < 15:
                print(fn, json.dumps({'old': old, 'new': new, 'kind': f.get('kind')}, ensure_ascii=False))
            n += 1
print(n)
