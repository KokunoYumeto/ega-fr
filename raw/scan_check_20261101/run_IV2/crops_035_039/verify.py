import json, sys, collections

sys.stdout.reconfigure(encoding='utf-8')
base = r'user\Documents\ega_scan_check_20261101\run_IV2'
data = json.load(open(base + r'\findings_035_039.json', encoding='utf-8'))
pages = {}
ok = True
counts = collections.defaultdict(lambda: collections.Counter())
keys = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
for i, it in enumerate(data):
    p = it['page']
    missing = keys - set(it)
    if missing:
        print('MISSING KEYS', i, missing); ok = False
    if it['kind'] == 'misprint_in_print':
        counts[p]['misprint'] += 1
        if 'corrected' not in it:
            print('NO corrected', i); ok = False
    elif it['kind'] == 'convention':
        counts[p]['convention'] += 1
        if not it.get('convention'):
            print('NO convention number', i); ok = False
    else:
        counts[p]['normal'] += 1
        if it.get('convention') is not None:
            print('convention set on non-convention', i); ok = False
    if p not in pages:
        pages[p] = open(base + r'\page_%03d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    fx = it.get('fix')
    if fx is None:
        continue
    n = pages[p].count(fx['old'])
    if n != 1:
        print('OLD COUNT', n, 'page', p, repr(fx['old'])); ok = False
# sequential application per page
for p in sorted(pages):
    t = pages[p]
    if '\r' in t:
        print('CR found in page', p)
    for it in data:
        if it['page'] != p or not it.get('fix'):
            continue
        old, new = it['fix']['old'], it['fix']['new']
        c = t.count(old)
        if c != 1:
            print('SEQ FAIL page', p, c, repr(old)); ok = False
            continue
        t = t.replace(old, new)
print('OK' if ok else 'PROBLEMS')
for p in sorted(counts):
    c = counts[p]
    print(p, '%d/%d/%d' % (c['normal'], c['convention'], c['misprint']))
print('total', len(data))
