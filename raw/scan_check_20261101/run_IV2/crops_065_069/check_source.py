import json, re, sys

sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega4-2-fr.tex'
FND = r'user\Documents\ega_scan_check_20261101\run_IV2\findings_065_069.json'
src = open(SRC, 'rb').read().decode('utf-8')
print('CRLF in source:', '\r\n' in src)
F = json.load(open(FND, encoding='utf-8'))
seg = {}
for p in range(65, 70):
    a = src.index('\\oldpage[IV-2]{%d}' % p)
    b = src.index('\\oldpage[IV-2]{%d}' % (p + 1))
    seg[p] = src[a:b]
bad = 0
for d in F:
    if not d['fix']:
        continue
    n = seg[d['page']].count(d['fix']['old'])
    if n != 1:
        bad += 1
        print('segment count %d p.%d %r' % (n, d['page'], d['fix']['old']))
print(len(F), 'findings;', bad, 'not unique in their source segment')
