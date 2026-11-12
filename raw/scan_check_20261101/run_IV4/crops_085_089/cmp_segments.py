import difflib, re, sys
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-17-fr.tex'
RUN = r'user/Documents/ega_scan_check_20261101/run_IV4'
src = open(SRC, encoding='utf-8', newline='').read()
lines = src.split('\n')
marks = {}
pat = re.compile(r'\\oldpage\[IV-4\]\{(\d+)\}')
for i, l in enumerate(lines):
    m = pat.match(l)
    if m:
        marks[int(m.group(1))] = i
for n in [85, 86, 87, 88, 89]:
    p = open(RUN + '/page_%03d.tex' % n, encoding='utf-8', newline='').read()
    p = p.replace(chr(13) + chr(10), chr(10))
    plines = p.split(chr(10))[1:]
    while plines and plines[-1] == '':
        plines.pop()
    seg = lines[marks[n]:marks[n + 1]]
    while seg and seg[-1] == '':
        seg.pop()
    d = list(difflib.unified_diff(seg, plines, lineterm='', n=0))
    print('page', n, 'source lines', marks[n] + 1, '-', marks[n + 1], 'diff lines:', len(d))
    for x in d[:40]:
        print(repr(x)[:300])
