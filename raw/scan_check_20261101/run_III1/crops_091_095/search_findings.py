import json, glob, sys
pat = sys.argv[1].lower()
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 15
n = 0
for f in sorted(glob.glob('user/Documents/ega_scan_check_20261101/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat in s.lower():
            print(f.split('20261101')[1], s[:500]); print(); n += 1
            if n >= lim:
                sys.exit()
