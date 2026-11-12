import sys, difflib, re
sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex'
RUN = r'user/Documents/ega_scan_check_20261101/run_IV4/'
src = open(SRC, encoding='utf-8', newline='').read()
print('CRLF in source:', '\r\n' in src)
for p in range(135, 140):
    a = src.index('\\oldpage[IV-4]{%d}' % p)
    b = src.index('\\oldpage[IV-4]{%d}' % (p + 1))
    seg = src[a:b]
    pg = open(RUN + 'page_%03d.tex' % p, encoding='utf-8', newline='').read()
    # drop first line (% from ...)
    pg_body = pg.split('\n', 1)[1]
    if seg == pg_body:
        print(p, 'IDENTICAL')
    else:
        print(p, 'DIFFERENT')
        for l in difflib.unified_diff(pg_body.split('\n'), seg.split('\n'), 'page', 'source', lineterm='', n=0):
            print('   ', l[:300])
