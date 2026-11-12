import json, collections, sys
c = collections.Counter()
ex = {}
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    try:
        d = json.loads(line)
    except Exception:
        continue
    n = d.get('new') or ''
    o = d.get('old') or ''
    hit = False
    for pref in ('\\textup{(1', '\\textup{(2', '\\textup{(3', '\\textup{(4', '\\textup{(5', '\\textup{(6',
                 '\\textup{(7', '\\textup{(8', '\\textup{(9', '\\textup{(\\hyperref', '\\textup{(\\sref', '\\textup{\\sref'):
        if pref in n and pref not in o:
            hit = True
    if hit:
        f = d.get('file', '').split('/')[-1]
        c[f] += 1
        ex.setdefault(f, []).append((d.get('page'), o[:80], n[:100]))
for k, v in c.most_common(40):
    print(k, v)
    for e in ex[k][:2]:
        print('   ', e)
