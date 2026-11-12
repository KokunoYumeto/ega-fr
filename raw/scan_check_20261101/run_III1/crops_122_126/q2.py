import json, glob, collections, os
c = collections.Counter()
for f in sorted(glob.glob('user/Documents/ega_scan_check_20261101/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    run = os.path.basename(os.path.dirname(f))
    for x in d:
        fx = x.get('fix') or {}
        nw = fx.get('new') or ''
        od = fx.get('old') or ''
        if '\\emph{' in nw and '\\emph{' not in od:
            c[(run, x['kind'], x.get('convention'))] += 1
for k, v in sorted(c.items(), key=lambda t: (t[0][0], str(t[0][1]), str(t[0][2]))):
    print(k, v)
