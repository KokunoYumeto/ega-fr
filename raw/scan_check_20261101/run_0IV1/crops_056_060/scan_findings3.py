import json, glob, re, sys

pat = re.compile(sys.argv[1], re.I)
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 12
cnt = 0
for fn in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            cnt += 1
            if cnt <= lim:
                f = x.get('fix') or {}
                print(fn.split('\\')[-2] + '/' + fn.split('\\')[-1], x.get('page'), x.get('kind'), x.get('convention'), '|', (x.get('where') or '')[:100], '|', (f.get('old') or '')[:90], '=>', (f.get('new') or '')[:90], '|', (x.get('note') or '')[:260])
                print()
print('count', cnt)
