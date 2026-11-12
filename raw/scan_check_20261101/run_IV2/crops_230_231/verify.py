import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')
run = r'user\Documents\ega_scan_check_20261101\run_IV2'
d = json.load(open(os.path.join(run, 'findings_230_231.json'), encoding='utf-8'))
pages = {}
for x in d:
    p = x['page']
    if p not in pages:
        pages[p] = open(os.path.join(run, 'page_%03d.tex' % p), encoding='utf-8').read().replace('\r\n', '\n')
ok = True
for x in d:
    fx = x['fix']
    if fx is None:
        print(x['page'], 'fix null')
        continue
    n = pages[x['page']].count(fx['old'])
    print(x['page'], x['kind'], 'count', n, repr(fx['old'][:60]))
    if n != 1:
        ok = False
# apply all fixes per page and show the result
for p, t in pages.items():
    for x in d:
        if x['page'] == p and x['fix']:
            assert t.count(x['fix']['old']) == 1, (p, x['fix']['old'])
            t = t.replace(x['fix']['old'], x['fix']['new'], 1)
    print('=====', p)
    print(t if p != 229 else t[:700])
print('ALL UNIQUE' if ok else 'PROBLEM')
