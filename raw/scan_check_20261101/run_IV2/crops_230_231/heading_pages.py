"""List the page (by \\oldpage markers) on which each \\section / \\subsection heading of ega4-2-fr.tex falls,
and compare with the contents entries (\\EGAIVtwoContentsLine) of the same file."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
F = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex'
lines = open(F, encoding='utf-8').read().split('\n')
page = None
heads = []
sec = 1
sub = 0
toc = []
for i, l in enumerate(lines, 1):
    m = re.search(r'\\oldpage\[IV-2\]\{(\d+)\}', l)
    if m:
        page = int(m.group(1))
    m = re.match(r'\\section\*?\{(.*)', l)
    if m and not l.startswith('\\section*'):
        sec += 1
        sub = 0
        heads.append((f'S{sec}', page, i, m.group(1)[:70]))
    m = re.match(r'\\subsection\{(.*)', l)
    if m:
        sub += 1
        heads.append((f'{sec}.{sub}', page, i, m.group(1)[:70]))
    m = re.match(r'\\EGAIVtwoContentsLine\{(.*?)\}\{(.*)\}\{(\d+)\}\s*$', l)
    if m:
        toc.append((m.group(1), int(m.group(3)), m.group(2)[:60]))
for h in heads:
    print(h)
print('---- contents')
for t in toc:
    print(t)
