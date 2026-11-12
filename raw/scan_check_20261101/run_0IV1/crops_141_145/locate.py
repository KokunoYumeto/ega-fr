import os
import re
import sys

D = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                 'ega-fr', 'editions', '2026-10-24-r20', 'diplomatic', 'packages', 'IV1', 'native', 'ega4')
MARK = re.compile(r'\\oldpage\[[^\]]*\]\{(\d+)\}')


def pages(fn, pat):
    t = open(os.path.join(D, fn), encoding='utf-8').read()
    marks = [(m.start(), m.group(1)) for m in MARK.finditer(t)]
    out = []
    for m in re.finditer(pat, t):
        pg = None
        for pos, n in marks:
            if pos <= m.start():
                pg = n
        out.append((pg, t.count('\n', 0, m.start()) + 1))
    return out


print('sref, (i) in ega0-20:', pages('ega0-20-fr.tex', r'\\sref\{[^}]*\}, \((?:i|v)'))
print('mathbf{0_I} in ega0-20:', pages('ega0-20-fr.tex', r'mathbf\{0_I\}'))
print('ar@{=} in ega0-20:', pages('ega0-20-fr.tex', r'ar@\{=\}'))
print('ar@{=} in ega0-22:', pages('ega0-22-fr.tex', r'ar@\{=\}'))
for fn in sorted(os.listdir(D)):
    if fn.endswith('.tex'):
        n = len(pages(fn, r'\\sref\{[^}]*\}, \((?:i|v)'))
        if n:
            print(fn, 'sref-item refs:', n)
