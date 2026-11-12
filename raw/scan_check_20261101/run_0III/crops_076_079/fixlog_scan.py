import json, sys, glob
key = sys.argv[1] if len(sys.argv) > 1 else 'ega3-1'
needle = sys.argv[2] if len(sys.argv) > 2 else None
base = r'user/Documents/ega_scan_check_20261101/'
for fn in sorted(glob.glob(base + 'FIXLOG*.jsonl')):
    n = 0
    with open(fn, encoding='utf-8') as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            if key not in json.dumps(r, ensure_ascii=False):
                continue
            s = json.dumps(r, ensure_ascii=False)
            if needle and needle not in s:
                continue
            n += 1
            print(fn.rsplit('/', 1)[-1], r.get('page'), r.get('kind'), r.get('convention'), '|', repr(r.get('old'))[:200], '=>', repr(r.get('new'))[:200])
    print(fn.rsplit('/', 1)[-1], 'total', n)
