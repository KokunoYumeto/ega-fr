import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
SRC = r'user\Documents\ega_scan_check_20261101\ega-fr\source\ega3\ega3-7-fr.tex'
F = json.load(open(r'user\Documents\ega_scan_check_20261101\run_III2\findings_207_211.json', encoding='utf-8'))
src = open(SRC, encoding='utf-8', newline='').read()
assert '\r' not in src, 'source has CR'
seg = {}
for p in range(207, 212):
    a = src.index('\\oldpage[III]{%d}' % p)
    b = src.index('\\oldpage[III]{%d}' % (p + 1))
    seg[p] = src[a:b]


def bal(s):
    s2 = s.replace('\\{', '').replace('\\}', '')
    return (s2.count('{') - s2.count('}'),
            len(re.findall(r'(?<!\\)\$', s)) % 2,
            s.count('\\[') - s.count('\\]'),
            s.count('\\begin{') - s.count('\\end{'))


bad = 0
for f in F:
    if not f['fix']:
        continue
    old, new = f['fix']['old'], f['fix']['new']
    n = seg[f['page']].count(old)
    if n != 1:
        bad += 1
        print('SEG COUNT', n, f['page'], repr(old[:60]))
    bo, bn = bal(old), bal(new)
    # braces must balance the same way; the display-to-inline edits trade \[ \] for $ by design
    if bo[0] != bn[0] or (bo[3] != bn[3] and 'env}[7.9.12]' not in old + new):
        bad += 1
        print('BALANCE', f['page'], bo, bn, repr(old[:50]))
# whole-page simulation: apply all fixes per page and check the overall balance is unchanged
for p in range(207, 212):
    s = seg[p]
    for f in F:
        if f['page'] == p and f['fix']:
            s = s.replace(f['fix']['old'], f['fix']['new'], 1)
    b0, b1 = bal(seg[p]), bal(s)
    print(p, 'before', b0, 'after', b1, 'OK' if b0 == b1 else 'DIFF')
print('bad', bad)
