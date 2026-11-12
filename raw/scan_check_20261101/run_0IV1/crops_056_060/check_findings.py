import json, os

RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
F = json.load(open(os.path.join(RUN, 'findings_056_060.json'), encoding='utf-8'))
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-18-fr.tex'
src = open(SRC, encoding='utf-8', newline='').read()
assert '\r' not in src

orig = {}
cur = {}
ok = True
for i, x in enumerate(F):
    p = x['page']
    if p not in orig:
        t = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read().replace('\r\n', '\n')
        orig[p] = t
        cur[p] = t
    fx = x['fix']
    if fx is None:
        if x['kind'] != 'misprint_in_print':
            print('NULL FIX on non-misprint', i, p, x['where'])
            ok = False
        continue
    old, new = fx['old'], fx['new']
    n_orig = orig[p].count(old)
    n_cur = cur[p].count(old)
    flag = ''
    if n_cur != 1:
        flag = 'FAIL(cur=%d)' % n_cur
        ok = False
    elif n_orig != 1:
        flag = 'after-earlier-fix(orig=%d)' % n_orig
    # source-file check (whole file): how often does old occur in ega0-18-fr.tex
    n_src = src.count(old)
    if flag or n_src != 1:
        print(i, p, x['kind'], flag, 'src=%d' % n_src, '|', repr(old[:60]))
    if n_cur == 1:
        cur[p] = cur[p].replace(old, new, 1)
    if old == new:
        print('NOOP', i)
        ok = False

# counts per page
from collections import Counter
c = Counter()
for x in F:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    c[(x['page'], k)] += 1
for p in sorted(set(x['page'] for x in F)):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('ALL OK' if ok else 'PROBLEMS')
