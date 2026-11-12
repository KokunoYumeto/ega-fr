import json
import pathlib
import collections

RUN = pathlib.Path(r'user\Documents\ega_scan_check_20261101\run_IV3')
d = json.loads((RUN / 'findings_185_189.json').read_text(encoding='utf-8'))
pages = {}
for n in range(185, 190):
    pages[n] = (RUN / f'page_{n}.tex').read_bytes().decode('utf-8').replace('\r\n', '\n')

ok = True
# 1. every old occurs exactly once in its page file
for i, x in enumerate(d):
    fx = x['fix']
    if fx is None:
        continue
    c = pages[x['page']].count(fx['old'])
    if c != 1:
        ok = False
        print('COUNT', c, i, x['page'], repr(fx['old']))
# 2. sequential application in listed order works (each old still found exactly once when applied)
work = dict(pages)
for i, x in enumerate(d):
    fx = x['fix']
    if fx is None:
        continue
    t = work[x['page']]
    c = t.count(fx['old'])
    if c != 1:
        ok = False
        print('SEQ', c, i, x['page'], repr(fx['old']))
        continue
    work[x['page']] = t.replace(fx['old'], fx['new'])
# 3. the fixes do not overlap each other (old spans in the original text are disjoint)
for n in range(185, 190):
    spans = []
    for i, x in enumerate(d):
        if x['page'] != n or x['fix'] is None:
            continue
        a = pages[n].index(x['fix']['old'])
        spans.append((a, a + len(x['fix']['old']), i))
    spans.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(spans, spans[1:]):
        if a2 < b1:
            print('OVERLAP', n, i1, i2)
# counts
cnt = collections.defaultdict(lambda: [0, 0, 0])
for x in d:
    k = 1 if x['kind'] == 'convention' else 2 if x['kind'] == 'misprint_in_print' else 0
    cnt[x['page']][k] += 1
print('ok' if ok else 'PROBLEMS')
for n in sorted(cnt):
    print(n, '%d/%d/%d' % tuple(cnt[n]))
# show the resulting text of a few edited regions for a visual check
for n, key in [(187, 'tels que'), (187, 'pour tout $s'), (189, 'on ait'), (187, 'Malheureuse'), (187, 'constante')]:
    t = work[n]
    j = t.find(key)
    print('----', n, key)
    print(t[max(0, j - 80): j + 260])
