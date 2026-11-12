import json, sys, glob
sys.stdout.reconfigure(encoding="utf-8")

# usage: python search_fixlog.py <substring-in-old> <substring-in-new>  (either may be '-')
a = sys.argv[1] if len(sys.argv) > 1 else '-'
b = sys.argv[2] if len(sys.argv) > 2 else '-'
root = r'user\Documents\ega_scan_check_20261101'
n = 0
for line in open(root + r'\FIXLOG.jsonl', encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    try:
        d = json.loads(line)
    except Exception:
        continue
    o = d.get('old', '') or ''
    nw = d.get('new', '') or ''
    if (a == '-' or a in o) and (b == '-' or b in nw):
        if a != '-' and b != '-' and b in o:
            continue
        print(d.get('page'), '|', repr(o)[:220], '->', repr(nw)[:220], '|', (d.get('why', '') or '')[:300])
        n += 1
print('matches:', n)
