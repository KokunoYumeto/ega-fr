import json, re, sys
from collections import Counter

path = sys.argv[1]
c = Counter()
ex = {}
pat = re.compile(r'\\textup\{\((.{0,30})')
for line in open(path, encoding='utf-8'):
    try:
        d = json.loads(line)
    except Exception:
        continue
    o = d.get('old', '')
    nw = d.get('new', '')
    for m in pat.finditer(nw):
        s = m.group(1)
        if s.startswith('\\hyperref'):
            k = 'hyperref'
        elif re.match(r'[0-9]', s):
            k = 'digit'
        elif s.startswith('$'):
            k = 'math'
        else:
            k = 'text'
        c[k] += 1
        ex.setdefault(k, []).append((d.get('part'), d.get('page'), s))
print(c)
for k, v in ex.items():
    print(k, v[:8])
