import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
pat = sys.argv[1]
root = r'user/Documents/ega_scan_check_20261101/'
globs = sys.argv[2] if len(sys.argv) > 2 else 'run_0IV1/findings_*.json'
for fn in sorted(glob.glob(root + globs)):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat in s:
            f = x.get('fix') or {}
            print(fn.split('/')[-1], x.get('page'), x.get('kind'), x.get('convention'), '|', (x.get('where') or '')[:90], '|', json.dumps(f, ensure_ascii=False)[:300], '|', (x.get('note') or '')[:250])
