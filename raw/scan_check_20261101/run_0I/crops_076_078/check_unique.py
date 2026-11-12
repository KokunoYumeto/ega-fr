import json, os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = json.load(open(os.path.join(RUN, 'findings_076_078.json'), encoding='utf-8'))
src_path = os.path.join(os.path.dirname(RUN), 'ega-fr', 'source', 'ega1', 'ega0-1-fr.tex')
src = open(src_path, encoding='utf-8', newline='').read()
print('source has CR:', '\r' in src)

def marker(n):
    return r'\oldpage[0\textsubscript{I}]{%d}' % n

m = {n: src.find(marker(n)) for n in (76, 77, 78, 79)}
print('marker positions:', m)
end78 = m[79] if m[79] > 0 else len(src)
seg = {76: src[m[76]:m[77]], 77: src[m[77]:m[78]], 78: src[m[78]:end78]}

ok = True
for d in F:
    if d['fix'] is None:
        continue
    p = d['page']
    tex = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read().replace('\r\n', '\n')
    old = d['fix']['old']
    n_page, n_seg, n_file = tex.count(old), seg[p].count(old), src.count(old)
    bad = not (n_page == 1 and n_seg == 1)
    ok &= not bad
    print(p, n_page, n_seg, n_file, repr(old)[:72], '<-- PROBLEM' if bad else '')

# each fix applied alone and all fixes applied together, on the page text
for p in (76, 77, 78):
    tex = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read().replace('\r\n', '\n')
    t = tex
    for d in F:
        if d['page'] == p and d['fix']:
            if t.count(d['fix']['old']) != 1:
                ok = False
                print('sequential application fails on', p, repr(d['fix']['old']))
            t = t.replace(d['fix']['old'], d['fix']['new'], 1)
    # reverse order too
    t = tex
    for d in reversed(F):
        if d['page'] == p and d['fix']:
            if t.count(d['fix']['old']) != 1:
                ok = False
                print('reverse application fails on', p, repr(d['fix']['old']))
            t = t.replace(d['fix']['old'], d['fix']['new'], 1)
print('ALL OK' if ok else 'FAILED')
