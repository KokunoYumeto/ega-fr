import os
base = r'user\Documents\ega_scan_check_20261101'
native = base + r'\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native'
pre = open(native + r'\ega4\EGA_IV4_FR.tex', encoding='utf-8').read()
pre = pre.split('\\begin{document}')[0]
pre = pre.replace('\\input{preamble-base}', '\\input{' + native.replace('\\', '/') + '/preamble-base}')
body = []
for p in range(215, 220):
    t = open(base + r'\run_IV4\crops_215_219\after_%d.tex' % p, encoding='utf-8').read()
    body.append(t.split('\n', 1)[1])
doc = pre + '\\begin{document}\n\\setcounter{section}{19}\\setcounter{subsection}{7}\n' + ''.join(body) + '\\end{proposition}\n\\end{document}\n'
os.makedirs(base + r'\run_IV4\crops_215_219\compile', exist_ok=True)
open(base + r'\run_IV4\crops_215_219\compile\stub_215_219.tex', 'w', encoding='utf-8').write(doc)
print('written')
