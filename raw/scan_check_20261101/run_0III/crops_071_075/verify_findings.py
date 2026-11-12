"""Check that every fix's old string occurs exactly once in its page file, that no two
fixes on a page overlap, and that applying all fixes of a page in sequence succeeds."""
import json
import os
import sys
from collections import Counter

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(RUN, 'findings_071_075.json'), encoding='utf-8'))

REL = os.path.join(os.path.dirname(RUN), 'ega-fr', 'editions', '2026-10-24-r20', 'diplomatic', 'packages',
                   'BASE', 'native', 'ega3', 'ega3-1-fr.tex')
rel = open(REL, encoding='utf-8', newline='').read()  # LF file


def segment(p):
    m = '\\oldpage[0\\textsubscript{III}]{%d}' % p
    s = rel.find(m)
    e = rel.find('\\oldpage[', s + len(m))
    return rel[s:e]


pages = {}
bad = 0
for i, d in enumerate(data):
    p = d['page']
    if p not in pages:
        # page files are CRLF on disk; the release files are LF: compare with \n
        pages[p] = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8').read()
    fx = d.get('fix')
    if fx is None:
        continue
    n = pages[p].count(fx['old'])
    ns = segment(p).count(fx['old'])
    if n != 1 or ns != 1:
        bad += 1
        print('NOT UNIQUE/ABSENT', p, 'page file:', n, 'release segment:', ns, repr(fx['old'])[:100])

# overlap check per page
for p, text in pages.items():
    spans = []
    for d in data:
        if d['page'] != p or d.get('fix') is None:
            continue
        o = d['fix']['old']
        s = text.find(o)
        spans.append((s, s + len(o), o))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print('OVERLAP', p, repr(a[2])[:60], '|', repr(b[2])[:60])
    # sequential application
    t = text
    for d in data:
        if d['page'] != p or d.get('fix') is None:
            continue
        o, nw = d['fix']['old'], d['fix']['new']
        if t.count(o) != 1:
            bad += 1
            print('SEQ FAIL', p, repr(o)[:80])
            continue
        t = t.replace(o, nw)
    # brace balance after all fixes
    if t.count('{') - t.count('\\{') != t.count('}') - t.count('\\}'):
        print('BRACE IMBALANCE after fixes on page', p,
              t.count('{') - t.count('}'), 'vs before', text.count('{') - text.count('}'))

c = Counter(d['page'] for d in data)
kinds = Counter((d['page'], 'misprint' if d['kind'] == 'misprint_in_print'
                 else ('convention' if d['kind'] == 'convention' else 'normal')) for d in data)
print('total', len(data), dict(c))
for p in sorted(c):
    print(p, kinds[(p, 'normal')], kinds[(p, 'convention')], kinds[(p, 'misprint')])
print('problems:', bad)
