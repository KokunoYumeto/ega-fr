import json

BASE = 'user/Documents/ega_scan_check_20261101/'
SRC = BASE + 'ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV1/native/ega4/ega0-23-fr.tex'

with open(SRC, encoding='utf-8', newline='') as fh:
    t = fh.read().replace('\r\n', '\n')


def seg(text, n):
    a = text.find('\\oldpage[0\\textsubscript{IV-1}]{%d}' % n)
    b = text.find('\\oldpage[0\\textsubscript{IV-1}]{%d}' % (n + 1))
    return a, b


d = json.load(open(BASE + 'run_0IV1/findings_216_220.json', encoding='utf-8'))
ok = True
for x in d:
    fx = x['fix']
    if not fx:
        continue
    a, b = seg(t, x['page'])
    s = t[a:b]
    c = s.count(fx['old'])
    if c != 1:
        ok = False
        print('segment count', c, x['page'], repr(fx['old'])[:70])
        continue
    i = t.index(fx['old'], a)
    t = t[:i] + fx['new'] + t[i + len(fx['old']):]
print('all apply once in their r20 segments:', ok)
# paragraph breaks left around the markers after the fixes
for n in range(216, 222):
    a = t.find('\\oldpage[0\\textsubscript{IV-1}]{%d}' % n)
    print(n, repr(t[a - 40:a + 60]))
