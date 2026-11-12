import difflib
import os
import sys

run, src = sys.argv[1], sys.argv[2]
text = open(src, encoding='utf-8', newline='').read()
for p in range(41, 46):
    m = '\\oldpage[0\\textsubscript{I}]{%d}' % p
    m2 = '\\oldpage[0\\textsubscript{I}]{%d}' % (p + 1)
    a = text.find(m)
    b = text.find(m2)
    seg = text[a:b]
    page = open(os.path.join(run, 'page_%03d.tex' % p), encoding='utf-8', newline='').read()
    page = page.replace('\r\n', '\n')
    body = page.split('\n', 1)[1]  # drop the "% from ..." line
    same = seg.rstrip('\n') == body.rstrip('\n')
    print(p, 'segment chars', len(seg), 'page chars', len(body), 'identical' if same else 'DIFFERENT')
    if not same:
        for line in list(difflib.unified_diff(seg.splitlines(), body.splitlines(), lineterm='', n=0))[:12]:
            print('   ', line)
