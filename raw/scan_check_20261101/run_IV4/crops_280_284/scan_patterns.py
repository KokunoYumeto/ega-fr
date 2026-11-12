import re, io
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
pats = [r'\\cdot', r'\\begin\{env\}', r'\\ldots', r'\\dots', r'qquad', r'\\mathbf\{P\}', r'\\textbf', r'\\ker\b',
        r'\\kappa', r'\\#', r'\\mathfrak', r'\\mathscr', r'\\gr', r'\\Omega', r'\\operatorname\{Diff\}', r'\\simeq',
        r'\\isoto', r'\\longmapsto', r'\\widetilde', r'\$[a-d]\'*\)\$', r'\\item\[', r'\(I+,', r'\\sh\{[IJ]\}']
for p in range(280, 286):
    t = io.open(base + 'page_%d.tex' % p, encoding='utf-8').read().replace('\r\n', '\n')
    for pat in pats:
        for m in re.finditer(pat, t):
            s = max(0, m.start() - 30)
            e = min(len(t), m.end() + 40)
            print(p, pat, repr(t[s:e]))
