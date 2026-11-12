import json, glob, sys

sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
needle = sys.argv[2]
field = sys.argv[3] if len(sys.argv) > 3 else 'new'
limit = int(sys.argv[4]) if len(sys.argv) > 4 else 6
n = 0
for f in sorted(glob.glob(root + '/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        s = fx.get(field, '') if field in ('old', 'new') else json.dumps(x, ensure_ascii=False)
        if needle in s:
            print(f)
            print(json.dumps(x, ensure_ascii=False)[:700])
            print()
            n += 1
            if n >= limit:
                sys.exit(0)
