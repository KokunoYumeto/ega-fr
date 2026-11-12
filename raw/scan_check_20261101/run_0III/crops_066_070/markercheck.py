import json
fn = r'user/Documents/ega_scan_check_20261101/FIXLOG.jsonl'
n = 0
with open(fn, encoding='utf-8') as f:
    for line in f:
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get('kind') != 'marker':
            continue
        n += 1
        if n <= 40:
            print(r.get('page'), '|', repr(r.get('old'))[:200], '=>', repr(r.get('new'))[:260])
print('total', n)
