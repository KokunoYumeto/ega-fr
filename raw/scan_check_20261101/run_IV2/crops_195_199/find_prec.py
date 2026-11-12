import json, glob, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
needles = sys.argv[1:]
n = 0
for f in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(d, list):
        continue
    for x in d:
        fx = x.get('fix') or {}
        old = fx.get('old', '') if isinstance(fx, dict) else ''
        if any(nd in old for nd in needles):
            if n < 10:
                print(f, json.dumps(x, ensure_ascii=False)[:700])
                print()
            n += 1
print('total', n)
