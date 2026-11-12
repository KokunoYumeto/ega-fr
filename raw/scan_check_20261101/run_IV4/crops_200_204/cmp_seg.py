import sys, io
SRC = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex"
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
src = open(SRC, encoding='utf-8', newline='').read()
assert '\r' not in src
for p in [200, 201, 202, 203, 204]:
    a = src.index('\oldpage[IV-4]{%d}' % p)
    b = src.index('\oldpage[IV-4]{%d}' % (p+1))
    seg = src[a:b]
    pg = open(RUN + '/page_%03d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    body = pg.split('\n', 1)[1]
    if '% (continued in' in body:
        print(p, 'has continuation')
    print(p, 'identical' if body.rstrip('\n') == seg.rstrip('\n') else 'DIFFERENT', len(seg), len(body))
    if body.rstrip('\n') != seg.rstrip('\n'):
        import difflib
        for l in difflib.unified_diff(body.split('\n'), seg.split('\n'), 'page', 'src', lineterm='', n=0):
            print(l[:300])
