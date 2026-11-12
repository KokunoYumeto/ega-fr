import json, os, collections
run = r'user\Documents\ega_scan_check_20261101\run_IV2'
data = json.load(open(os.path.join(run, 'findings_005_009.json'), encoding='utf-8'))
pages = {}
for p in range(5, 10):
    t = open(os.path.join(run, 'page_%03d.tex' % p), encoding='utf-8').read()
    pages[p] = t.replace('\r\n', '\n')
ok = True
keys_needed = {'page', 'where', 'scan', 'tex', 'kind', 'convention', 'confidence', 'fix', 'note'}
counts = collections.defaultdict(lambda: [0, 0, 0])
for i, f in enumerate(data):
    missing = keys_needed - set(f)
    if missing:
        print('MISSING KEYS', i, missing); ok = False
    if f['kind'] == 'misprint_in_print' and 'corrected' not in f:
        print('NO corrected', i); ok = False
    if f['kind'] == 'convention' and not f.get('convention'):
        print('NO convention number', i); ok = False
    if f['kind'] != 'convention' and f.get('convention'):
        print('convention number on non-convention', i); ok = False
    if f['kind'] == 'misprint_in_print':
        counts[f['page']][2] += 1
    elif f['kind'] == 'convention':
        counts[f['page']][1] += 1
    else:
        counts[f['page']][0] += 1
    fx = f.get('fix')
    if fx is None:
        continue
    n = pages[f['page']].count(fx['old'])
    if n != 1:
        print('NOT UNIQUE/ABSENT in original', i, f['page'], n, repr(fx['old'])); ok = False
# sequential application per page
applied = dict(pages)
for i, f in enumerate(data):
    fx = f.get('fix')
    if fx is None:
        continue
    t = applied[f['page']]
    n = t.count(fx['old'])
    if n != 1:
        print('CONFLICT during sequential apply', i, f['page'], n, repr(fx['old'])); ok = False
        continue
    applied[f['page']] = t.replace(fx['old'], fx['new'], 1)
print('total findings', len(data))
for p in sorted(counts):
    print('page', p, 'normal/convention/misprint', counts[p])
print('OK' if ok else 'PROBLEMS')
out = os.path.join(run, 'crops_005_009', 'applied_preview')
os.makedirs(out, exist_ok=True)
for p, t in applied.items():
    open(os.path.join(out, 'page_%03d_applied.tex' % p), 'w', encoding='utf-8', newline='\n').write(t)
