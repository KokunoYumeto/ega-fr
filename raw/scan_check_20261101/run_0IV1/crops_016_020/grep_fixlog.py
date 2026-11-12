import json, sys
path = sys.argv[1]
needle_old = sys.argv[2]
needle_new = sys.argv[3] if len(sys.argv) > 3 else None
n = 0
with open(path, encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
        except Exception:
            continue
        old, new = d.get('old', ''), d.get('new', '')
        if needle_old in old and (needle_new is None or needle_new in new):
            n += 1
            if n <= 8:
                print(d.get('part'), d.get('page'), repr(old)[:250], '=>', repr(new)[:250])
print('total', n)
