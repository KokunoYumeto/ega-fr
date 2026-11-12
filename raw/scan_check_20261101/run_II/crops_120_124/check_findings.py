import json, sys
base = r'user/Documents/ega_scan_check_20261101/run_II/'
L = json.load(open(base + 'findings_120_124.json', encoding='utf-8'))
pages = {}
bad = 0
for i, d in enumerate(L):
    p = d['page']
    if p not in pages:
        pages[p] = open(base + 'page_%03d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    fx = d['fix']
    if fx is None:
        continue
    n = pages[p].count(fx['old'])
    if n != 1:
        bad += 1
        print('BAD', i, p, n, repr(fx['old']))
# apply all fixes per page sequentially to check non-interference
for p, s in pages.items():
    t = s
    for d in L:
        if d['page'] == p and d['fix']:
            o, nw = d['fix']['old'], d['fix']['new']
            if t.count(o) != 1:
                print('SEQ-BAD', p, repr(o)); bad += 1
            t = t.replace(o, nw, 1)
print('checked', len(L), 'bad', bad)
from collections import Counter
c = Counter()
for d in L:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    c[(d['page'], k)] += 1
for p in sorted(pages):
    print(p, c[(p,'normal')], c[(p,'convention')], c[(p,'misprint')])
