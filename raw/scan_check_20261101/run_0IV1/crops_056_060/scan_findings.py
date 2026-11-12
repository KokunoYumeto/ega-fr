import json, glob, re, sys
pat_old = re.compile(r'\ar\[[a-z]*d[a-z]*\]\^')
pat_new = re.compile(r'\ar\[[a-z]*d[a-z]*\]_')
n = 0; tot = 0
for fn in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        f = x.get('fix') or {}
        old = f.get('old') or ''; new = f.get('new') or ''
        if '\ar[d' in old or '\ar[u' in old:
            tot += 1
        if pat_old.search(old) and pat_new.search(new):
            n += 1
            if n <= 8:
                print(fn, x['page'], x['kind'], '|', (x.get('where') or '')[:90], '|', old[:90], '=>', new[:90], '|', (x.get('note') or '')[:220])
                print()
print('vertical-side fixes:', n, 'fixes touching vertical arrows:', tot)
