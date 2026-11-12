import json
import sys

RUN = 'user/Documents/ega_scan_check_20261101/run_IV4/'
SRC = 'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/'


def rd(p):
    return open(p, encoding='utf-8', newline='').read().replace('\r\n', '\n')


s18 = rd(SRC + 'ega4-18-fr.tex')
s20 = rd(SRC + 'ega4-20-fr.tex')
# page segments in the current source
seg = {}
i = s18.index('\\oldpage[IV-4]{225}')
j = s20.index('\\oldpage[IV-4]{226}')
seg[225] = s18[i:] + '\n' + s20[:j]
marks = [s20.index('\\oldpage[IV-4]{%d}' % n) for n in [226, 227, 228, 229, 230]]
for n, (a, b) in zip([226, 227, 228, 229], zip(marks, marks[1:])):
    seg[n] = s20[a:b]
findings = json.load(open(RUN + 'findings_225_229.json', encoding='utf-8'))
bad = 0
for k, f in enumerate(findings):
    fx = f['fix']
    if not fx:
        continue
    o = fx['old']
    p = f['page']
    in_seg = seg[p].count(o)
    in18 = s18.count(o)
    in20 = s20.count(o)
    flag = '' if in_seg == 1 else '  <-- SEGMENT COUNT'
    if in_seg != 1:
        bad += 1
    if (in18 + in20) > 1 or flag:
        sys.stdout.buffer.write(('#%d p%d seg=%d ega4-18=%d ega4-20=%d old=%r%s\n' % (k, p, in_seg, in18, in20, o[:70], flag)).encode('utf-8'))
print('segment problems:', bad, 'of', sum(1 for f in findings if f['fix']))
