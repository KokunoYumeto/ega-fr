import os
here = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'applied_preview')
src = open(r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\EGA_IV2_FR.tex', encoding='utf-8').read()
pre = src.split('\\begin{document}')[0]
body = []
for p in range(5, 10):
    body.append(open(os.path.join(here, 'page_%03d_applied.tex' % p), encoding='utf-8').read())
doc = pre + '\\providecommand{\\EGAReaderTarget}[2]{}\n\\begin{document}\n' + '\n'.join(body) + '\n\\end{enumerate}\\end{proposition}\n\\end{document}\n'
open(os.path.join(here, 'test_applied.tex'), 'w', encoding='utf-8', newline='\n').write(doc)
print('written', len(doc))
