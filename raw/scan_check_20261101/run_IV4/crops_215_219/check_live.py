import json, sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex'
F = json.load(open(r'user\Documents\ega_scan_check_20261101\run_IV4\findings_215_219.json', encoding='utf-8'))
src = open(SRC, encoding='utf-8').read()
assert '\r' not in src
segs = {}
for p in range(215, 220):
    a = src.index('\\oldpage[IV-4]{%d}' % p)
    b = src.index('\\oldpage[IV-4]{%d}' % (p + 1))
    segs[p] = src[a:b]
# compare with page files
for p in segs:
    pf = open(r'user\Documents\ega_scan_check_20261101\run_IV4\page_%d.tex' % p, encoding='utf-8').read().replace('\r\n', '\n')
    body = pf.split('\n', 1)[1]  # drop the '% from' line
    print(p, 'segment == page file:', body == segs[p])
nonuniq_file = 0
for i, e in enumerate(F):
    fx = e['fix']
    if not fx:
        continue
    c = segs[e['page']].count(fx['old'])
    cf = src.count(fx['old'])
    if c != 1:
        print('segment count', c, i, e['page'], e['kind'], repr(fx['old'])[:100])
    if cf != 1:
        nonuniq_file += 1
print('olds not unique in the whole file:', nonuniq_file)
print('json entries', len(F), 'with fix', sum(1 for e in F if e['fix']))
