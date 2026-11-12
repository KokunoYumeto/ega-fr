import json, sys, os

pat = sys.argv[1]
field = sys.argv[2] if len(sys.argv) > 2 else 'new'
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 12
seen = 0
with open(r'user\Documents\ega_scan_check_20261101\FIXLOG.jsonl', encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
        except Exception:
            continue
        o = d.get('old', '') or ''
        n = d.get('new', '') or ''
        target = n if field == 'new' else o
        if pat in target and seen < limit:
            print(repr(o), '=>', repr(n), os.path.basename(d.get('file', '') or ''), d.get('page'))
            seen += 1
