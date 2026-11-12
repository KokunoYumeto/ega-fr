import json, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')
root = r'user\Documents\ega_scan_check_20261101'
pat = re.compile(sys.argv[1])
field = sys.argv[2] if len(sys.argv) > 2 else 'new'
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 15
n = 0
for f in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        if field == 'new':
            s = fx.get('new', '') if isinstance(fx, dict) else ''
        elif field == 'old':
            s = fx.get('old', '') if isinstance(fx, dict) else ''
        else:
            s = str(x.get(field, ''))
        if pat.search(s):
            n += 1
            if n <= limit:
                print(f.split('\\')[-2] + '/' + f.split('\\')[-1],
                      json.dumps({k: x.get(k) for k in ('page', 'where', 'kind', 'convention', 'fix', 'note')}, ensure_ascii=False)[:700])
print('TOTAL', n)
