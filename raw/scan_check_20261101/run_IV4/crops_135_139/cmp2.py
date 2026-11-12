import sys
sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex'
RUN = r'user/Documents/ega_scan_check_20261101/run_IV4/'
src = open(SRC, encoding='utf-8', newline='').read()
for p in range(135, 140):
    a = src.index(r'\oldpage[IV-4]{%d}' % p)
    b = src.index(r'\oldpage[IV-4]{%d}' % (p + 1))
    seg = src[a:b]
    pg = open(RUN + 'page_%03d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    first, body = pg.split('\n', 1)
    print(p, repr(first), len(seg), len(body), seg.rstrip('\n') == body.rstrip('\n'), repr(seg[-5:]), repr(body[-5:]))
    if seg.rstrip('\n') != body.rstrip('\n'):
        sl = seg.split('\n'); bl = body.split('\n')
        for i,(x,y) in enumerate(zip(sl,bl)):
            if x!=y:
                print('  line',i); print('  SRC:',x[:800]); print('  PAG:',y[:800])
