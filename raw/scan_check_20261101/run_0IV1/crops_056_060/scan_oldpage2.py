import json, glob
BS = chr(92)
cnt = 0
for fn in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        f = x.get('fix') or {}
        old = f.get('old') or ''
        new = f.get('new') or ''
        if (BS + 'oldpage' in old and old.count('\n\n') > new.count('\n\n')) or (old.endswith('\n\n') and not new.endswith('\n\n') and BS + 'oldpage' not in old):
            cnt += 1
            if cnt <= 8:
                print(fn.split('\\')[-2] + '/' + fn.split('\\')[-1], x.get('page'), x.get('kind'), '|', repr(old[:100]), '=>', repr(new[:100]), '|', (x.get('note') or '')[:300])
                print()
print('count', cnt)
