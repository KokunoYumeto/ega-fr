import re, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'user/Documents/ega_scan_check_20261101/run_IV4/'
pats = [r'\\cdot', r'\\cdots', r'\\ldots', r'\\dots', r'qquad', r'\\mathbf', r'\\textbf', r'\\ker\b',
        r'\\kappa', r'\\#', r'\\mathfrak', r'\\mathscr', r'\\gr', r'\\Omega', r'\\simeq', r'\\isoto',
        r'\\mapsto', r'\\longmapsto', r'\\widetilde', r'\$[a-d]\'*\)\$', r'\\item\[', r'\(I+,', r'\\sh\{[IJ]\}',
        r'\(\\sref', r'\\sref\[', r'\\sref\{[^}]*\}, \(', r'\\emph', r'\\textup', r'\\frac', r'-', r'\\setminus',
        r'\\boldsymbol', r'\\hat|\\widehat', r'\\overline']
for p in range(300, 305):
    t = io.open(base + 'page_%d.tex' % p, encoding='utf-8').read().replace('\r\n', '\n')
    for pat in pats:
        for m in re.finditer(pat, t):
            if pat == r'-':
                # only minus signs inside math: crude test, skip text hyphens between letters
                s = t[max(0, m.start() - 1):m.end() + 1]
                if re.match(r'[A-Za-zéèàù]-[A-Za-zéèàù]', s) or s.startswith('--') or s.endswith('--') or t[m.start()-1:m.start()+1] == '--':
                    continue
            s = max(0, m.start() - 30)
            e = min(len(t), m.end() + 40)
            print(p, pat, repr(t[s:e]))
