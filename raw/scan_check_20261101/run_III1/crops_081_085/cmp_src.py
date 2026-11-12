import sys, difflib
sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex'
RUN = r'user\Documents\ega_scan_check_20261101\run_III1'
CRLF = '\r\n'
LF = '\n'
raw = open(SRC, encoding='utf-8', newline='').read()
print('source has CRLF:', CRLF in raw)
src = raw.replace(CRLF, LF)
for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    pg = open(RUN + r'\page_%03d.tex' % n, encoding='utf-8', newline='').read().replace(CRLF, LF)
    body = pg.split(LF, 1)[1]
    a = src.find('\\oldpage[III]{%d}' % n)
    b = src.find('\\oldpage[III]{%d}' % (n + 1))
    seg = src[a:b]
    print('=== page', n, 'same' if seg == body else 'DIFFERENT', len(seg), len(body))
    if seg != body:
        for line in difflib.unified_diff(body.split(LF), seg.split(LF), 'page_file', 'current_source', lineterm='', n=0):
            print(line)
