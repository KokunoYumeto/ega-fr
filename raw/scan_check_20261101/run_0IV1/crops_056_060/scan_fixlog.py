import json, re, glob, sys

BS = chr(92)
AR = BS + 'ar['

# 1. FIXLOG: label-side swaps
n = 0; side = 0
for line in open(r'user\Documents\ega_scan_check_20261101\FIXLOG.jsonl', encoding='utf-8'):
    try:
        d = json.loads(line)
    except Exception:
        continue
    old = d.get('old') or ''; new = d.get('new') or ''
    if AR in old:
        n += 1
        if old.replace('^', '_') == new.replace('^', '_') and old != new:
            side += 1
            if side <= 12:
                print('FIXLOG', d.get('file', '')[-28:], d.get('page'), repr(old[:70]), '=>', repr(new[:70]), '|', (d.get('why') or '')[:140])
print('FIXLOG fixes touching ar:', n, 'pure label-side swaps:', side)

# 2. findings files: vertical label-side swaps
cnt = 0; vert = 0
for fn in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_*\findings_*.json')):
    try:
        dd = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in dd:
        f = x.get('fix') or {}
        old = f.get('old') or ''; new = f.get('new') or ''
        if AR in old and old.replace('^', '_') == new.replace('^', '_') and old != new:
            cnt += 1
            if re.search(re.escape(BS) + r'ar\[[a-z]*[du][a-z]*\]', old):
                vert += 1
print('findings label-side swaps:', cnt, 'of which vertical/diagonal:', vert)
