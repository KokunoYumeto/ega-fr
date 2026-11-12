import re
import sys

base = 'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/'
jobs = [
    ('BASE/native/ega3/ega3-1-fr.tex', r'\\hyperref\[0\.[^\]]*\]\{\$\\mathbf\{0\}_\{\\mathrm I\}\$, [0-9.]*\} et ', 3),
    ('BASE/native/ega3/ega3-1-fr.tex', r'\(\$\\mathbf\{0\}_\{\\mathrm I\}\$, [0-9.]* et [0-9.]*\)', 3),
    ('IV4/native/ega4/ega4-16-fr.tex', r'\\mathbf\{0\}_\{\\mathrm I\}', 3),
    ('IV4/native/ega4/ega4-18-fr.tex', r'\\mathbf\{0\}_\{\\mathrm I\}', 3),
    ('IV4/native/ega4/ega4-20-fr.tex', r'textsubscript\{I\}', 10),
]
for path, pat, n in jobs:
    s = open(base + path, encoding='utf-8').read()
    ms = list(re.finditer(pat, s))
    print('==', path, pat, 'count', len(ms))
    for m in ms[:n]:
        a = max(0, m.start() - 70)
        b = min(len(s), m.end() + 70)
        sys.stdout.buffer.write(('>> ' + s[a:b].replace('\n', '\\n') + '\n').encode('utf-8'))
