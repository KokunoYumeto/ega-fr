import difflib, os, re
RUN = r'user\Documents\ega_scan_check_20261101\run_0IV1'
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-18-fr.tex'
src = open(SRC, encoding='utf-8', newline='').read()
print('source mtime', os.path.getmtime(SRC))
BS = chr(92)
for p in range(55, 62):
    m1 = BS + 'oldpage[0' + BS + 'textsubscript{IV-1}]{%d}' % p
    m2 = BS + 'oldpage[0' + BS + 'textsubscript{IV-1}]{%d}' % (p + 1)
    a = src.find(m1); b = src.find(m2)
    seg = src[a:b]
    t = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read().replace('\r\n', '\n')
    t = t.split('\n', 1)[1]  # drop '% from' line
    if '% (continued in' in t:
        t = t.split('% (continued in')[0]
    if seg == t:
        print(p, 'identical')
        continue
    d = list(difflib.unified_diff(t.split('\n'), seg.split('\n'), 'page_file', 'source_now', lineterm='', n=0))
    print(p, 'DIFF', len(d))
    for l in d[:40]:
        print('   ', l[:160])
