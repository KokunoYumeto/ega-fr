import sys
P = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native'
D = r'user/Documents/ega_scan_check_20261101/run_IV4/crops_085_089'
which = sys.argv[1] if len(sys.argv) > 1 else 'fixed'
pre = open(P + '/ega4/EGA_IV4_FR.tex', encoding='utf-8').read()
head = pre.split(r'\begin{document}')[0]
head = head.replace(r'\input{preamble-base}', r'\input{' + P + '/preamble-base}')
parts = []
for n in range(85, 90):
    if which == 'fixed':
        parts.append(open(D + '/fixed_%03d.tex' % n, encoding='utf-8').read())
    else:
        t = open(r'user/Documents/ega_scan_check_20261101/run_IV4/page_%03d.tex' % n, encoding='utf-8').read()
        parts.append(t.replace('\r\n', '\n').split('\n', 1)[1])
body = ''.join(parts)
doc = head + '\\begin{document}\n\\setcounter{section}{17}\\setcounter{subsection}{11}\n' + body + '\n\\end{env}\n\\end{document}\n'
open(D + '/compile_%s.tex' % which, 'w', encoding='utf-8', newline='\n').write(doc)
print(len(doc))
