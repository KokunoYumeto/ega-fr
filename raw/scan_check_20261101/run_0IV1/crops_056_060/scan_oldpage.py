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
        if BS + 'oldpage' in old:
            cnt += 1
            if cnt <= 10:
                print(fn.split('\\')[-2] + '/' + fn.split('\\')[-1], x.get('page'), x.get('kind'), '|', repr(old[:120]), '=>', repr((f.get('new') or '')[:120]), '|', (x.get('note') or '')[:300])
                print()
print('count', cnt)
# page_059.tex tail
t = open(r'user\Documents\ega_scan_check_20261101\run_0IV1\page_059.tex', encoding='utf-8', newline='').read()
print(repr(t[-80:]))
t = open(r'user\Documents\ega_scan_check_20261101\run_0IV1\page_060.tex', encoding='utf-8', newline='').read()
print(repr(t[:80]))
print('CR in 60:', '\r' in t)
