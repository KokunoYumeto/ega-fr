import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
root = r'user\Documents\ega_scan_check_20261101'
n = 0
for fn in sorted(glob.glob(root + r'\run_IV*\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        f = x.get('fix') or {}
        if 'leadsto' in (f.get('new') or ''):
            n += 1
            if n <= 6:
                print(fn.split('\\')[-2:], x['page'], x['kind'], x.get('convention'), '|', (f.get('old') or '')[:60], '=>', (f.get('new') or '')[:60], '|', (x.get('note') or '')[:150])
print('total', n)
