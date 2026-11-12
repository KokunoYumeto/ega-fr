import json, glob, sys
needle_sets = [s.split('&&') for s in sys.argv[1:]]
root = r'user\Documents\ega_scan_check_20261101'
seen = 0
for f in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(data, list):
        continue
    for d in data:
        fx = d.get('fix') or {}
        new = fx.get('new') if isinstance(fx, dict) else None
        if not new:
            continue
        for needles in needle_sets:
            if all(n in new for n in needles):
                if seen < 6:
                    print(f)
                    print(json.dumps(d, ensure_ascii=False, indent=1))
                seen += 1
                break
print('matches', seen)
