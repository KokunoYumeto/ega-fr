import json
import os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(RUN)
src = open(os.path.join(ROOT, "ega-fr", "editions", "2026-10-24-r20", "current", "packages", "IV1", "native", "ega4", "ega0-20-fr.tex"), encoding='utf-8').read()
d = json.load(open(os.path.join(RUN, 'findings_141_145.json'), encoding='utf-8'))


def seg(p):
    a = src.index(r'\oldpage[0\textsubscript{IV-1}]{%d}' % p)
    b = src.index(r'\oldpage[0\textsubscript{IV-1}]{%d}' % (p + 1))
    return src[a:b]


for p in range(141, 146):
    s = seg(p)
    t = open(os.path.join(RUN, 'page_%03d.tex' % p), 'rb').read().decode('utf-8').replace('\r\n', '\n')
    body = t.split('\n', 1)[1]  # drop the '% from ...' line
    print(p, 'page file equals source segment:', body.rstrip('\n') == s.rstrip('\n'))

for x in d:
    if not x['fix']:
        continue
    o = x['fix']['old']
    print(x['page'], 'segment:', seg(x['page']).count(o), 'file:', src.count(o), json.dumps(o, ensure_ascii=False)[:60])
