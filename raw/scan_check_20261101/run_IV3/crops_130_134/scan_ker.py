import json, sys, glob
sys.stdout.reconfigure(encoding='utf-8')
n = 0
for fn in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        f = x.get('fix') or {}
        if '\ker' in (f.get('old') or ''):
            print(fn, json.dumps(x, ensure_ascii=False)[:500]); print(); n += 1
            if n > 3:
                sys.exit()
