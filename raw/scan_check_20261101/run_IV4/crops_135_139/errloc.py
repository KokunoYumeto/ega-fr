import sys, re
sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex'
lines = open(SRC, encoding='utf-8').read().split('\n')
m = None
for i, l in enumerate(lines, 1):
    for mm in re.finditer(r'\\oldpage\[IV-4\]\{(\d+)\}', l):
        m = mm.group(1)
    for e in re.finditer(r'Err', l):
        print(i, 'page', m, l[max(0, e.start()-60):e.start()+40])
