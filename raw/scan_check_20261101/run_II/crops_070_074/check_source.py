import json, sys, re
# Check every fix's "old" against the page segments of the source file (read-only).
src = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega2\ega2-1-fr.tex'
fj = r'user\Documents\ega_scan_check_20261101\run_II\findings_070_074.json'
t = open(src, encoding='utf-8', newline='').read()
crlf = '\r\n' in t
t = t.replace('\r\n', '\n')
seg = {}
for p in range(70, 75):
    a = t.index('\\oldpage[II]{%d}' % p)
    b = t.index('\\oldpage[II]{%d}' % (p + 1))
    seg[p] = t[a:b]
d = json.load(open(fj, encoding='utf-8'))
bad = 0
for i, x in enumerate(d):
    c = seg[x['page']].count(x['fix']['old'])
    if c != 1:
        bad += 1
        sys.stdout.buffer.write(('segment count %d for finding %d (p.%d)\n' % (c, i, x['page'])).encode('utf-8'))
sys.stdout.buffer.write(('source CRLF=%s; findings=%d; bad=%d\n' % (crlf, len(d), bad)).encode('utf-8'))
