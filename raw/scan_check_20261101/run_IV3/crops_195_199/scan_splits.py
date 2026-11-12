import json, glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')
root = r'user\Documents\ega_scan_check_20261101'
pat = re.compile(r'[A-Za-zéèàùâêîôûç]-\s*\n\s*\\oldpage')
n = 0
for fn in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        f = x.get('fix') or {}
        o = f.get('old') or ''
        if pat.search(o) or ('oldpage' in o and re.search(r'[a-zé]-\n', o)):
            n += 1
            if n <= 12:
                print(fn.split('\\')[-2:], x['page'], x['kind'], '|', repr(o[:100]), '=>', repr((f.get('new') or '')[:100]), '|', (x.get('note') or '')[:220])
print('total', n)
