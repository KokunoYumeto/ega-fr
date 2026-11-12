# Read-only check: does each fix's old occur exactly once in its page's segment of the current source file?
import json, os, re
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(os.path.dirname(RUN), 'ega-fr', 'editions', '2026-10-24-r20', 'diplomatic', 'packages',
                   'IV2', 'native', 'ega4', 'ega4-2-fr.tex')
with open(SRC, encoding='utf-8', newline='') as fh:
    src = fh.read().replace('\r\n', '\n')
d = json.load(open(os.path.join(RUN, 'findings_095_099.json'), encoding='utf-8'))

def segment(n):
    a = src.index('\\oldpage[IV-2]{%d}' % n)
    b = src.index('\\oldpage[IV-2]{%d}' % (n + 1))
    return src[a:b]

bad = 0
for i, x in enumerate(d):
    if not x['fix']:
        continue
    seg = segment(x['page'])
    c = seg.count(x['fix']['old'])
    if c != 1:
        bad += 1
        print(i, x['page'], x['kind'], 'segment count', c, '|', x['where'][:80])
print('checked', sum(1 for x in d if x['fix']), 'edits;', bad, 'not exactly once in the current source segment')
