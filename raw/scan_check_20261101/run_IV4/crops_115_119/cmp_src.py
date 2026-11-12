import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
src = open(SRC, encoding='utf-8', newline='').read()
for p in range(115, 120):
    m1 = src.index('\\oldpage[IV-4]{%d}' % p)
    m2 = src.index('\\oldpage[IV-4]{%d}' % (p + 1))
    seg = src[m1:m2]
    pg = open(RUN + '\\page_%03d.tex' % p, encoding='utf-8', newline='').read()
    pg = pg.replace('\r\n', '\n')
    first, rest = pg.split('\n', 1)
    same = (rest == seg)
    if not same:
        i = 0
        while i < min(len(rest), len(seg)) and rest[i] == seg[i]:
            i += 1
        print(p, 'DIFF at', i, repr(rest[max(0,i-60):i+60]), '||', repr(seg[max(0,i-60):i+60]), len(rest), len(seg))
    else:
        print(p, 'identical', first)
