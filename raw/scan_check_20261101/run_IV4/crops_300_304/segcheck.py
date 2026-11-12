import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SRC = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
def read(p):
    with open(p, encoding='utf-8', newline='') as f:
        return f.read().replace('\r\n', '\n')
b = read(SRC + 'ega4-21b-fr.tex')
c = read(SRC + 'ega4-21c-fr.tex')
def seg(text, n, nxt):
    i = text.index('\oldpage[IV-4]{%d}' % n)
    j = text.find('\oldpage[IV-4]{%d}' % nxt)
    return text[i: (j if j >= 0 else len(text))]
cur = {}
cur[300] = seg(b, 300, 301)
cur[301] = seg(b, 301, 302)
c0 = c.index('\oldpage[IV-4]{303}')
cur[302] = seg(b, 302, 303) + c[:c0]
cur[303] = seg(c, 303, 304)
cur[304] = seg(c, 304, 305)
for p in range(300, 305):
    pg = read(RUN + 'page_%d.tex' % p)
    body = pg.split('\n', 1)[1]
    body = body.replace('\n% (continued in ega4-21c-fr.tex, before its first page marker)\n', '')
    a = body.rstrip('\n'); bb = cur[p].rstrip('\n')
    print(p, 'SAME' if a == bb else 'DIFF', len(a), len(bb))
    if a != bb:
        import difflib
        for l in difflib.unified_diff(a.split('\n'), bb.split('\n'), lineterm='', n=0):
            print('   ', l[:200])
