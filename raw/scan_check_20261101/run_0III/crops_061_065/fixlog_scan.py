import json, sys, collections
p = sys.argv[1]
needle = sys.argv[2] if len(sys.argv) > 2 else None
rows = []
for line in open(p, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    try:
        rows.append(json.loads(line))
    except Exception:
        pass
e3 = [r for r in rows if 'ega3-1' in r.get('file', '') and 'diplomatic' in r.get('file', '')]
print('ega3-1 diplomatic rows:', len(e3))
print(collections.Counter(r.get('page') for r in e3))
if needle:
    for r in e3:
        if needle in r.get('old', '') or needle in r.get('new', ''):
            s = json.dumps({k: r.get(k) for k in ('page', 'old', 'new')}, ensure_ascii=True)
            print(s[:600])
