"""Compare the page files 148-152 with the live source segments (read-only) and check fix olds there."""
import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user\Documents\ega_scan_check_20261101\run_III1'
SRC = (r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current'
       r'\packages\BASE\native\ega3\ega3-1-fr.tex')
src = open(SRC, encoding='utf-8', newline='').read().replace('\r\n', '\n')
marks = {int(m.group(1)): m.start() for m in re.finditer(r'\\oldpage\[III\]\{(\d+)\}', src)}
F = json.load(open(RUN + r'\findings_148_152.json', encoding='utf-8'))
for p in (148, 149, 150, 151, 152):
    seg = src[marks[p]:marks[p + 1]]
    page = open(rf'{RUN}\page_{p}.tex', encoding='utf-8', newline='').read().replace('\r\n', '\n')
    body = page.split('\n', 1)[1]  # drop the '% from' line
    print(p, 'segment identical to page file:', seg == body, len(seg), len(body))
    for d in F:
        if d['page'] == p and d['fix']:
            n = seg.count(d['fix']['old'])
            if n != 1:
                print('   old not unique in live segment', n, repr(d['fix']['old'])[:80])
