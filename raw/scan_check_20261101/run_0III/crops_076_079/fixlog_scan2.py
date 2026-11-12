import json, sys, glob, collections
base = r'user/Documents/ega_scan_check_20261101/'
filt = sys.argv[1] if len(sys.argv) > 1 else 'ega3-1'
needle = sys.argv[2] if len(sys.argv) > 2 else None
cnt = collections.Counter()
for fn in sorted(glob.glob(base + 'FIXLOG*.jsonl')):
    with open(fn, encoding='utf-8') as f:
        for line in f:
            try:
                r = json.loads(line)
            except Exception:
                continue
            fil = str(r.get('file', ''))
            cnt[(fn.rsplit('\\', 1)[-1].rsplit('/', 1)[-1], fil)] += 1
            if filt not in fil:
                continue
            s = json.dumps(r, ensure_ascii=False)
            if needle and needle not in s:
                continue
            print(fn.rsplit('/', 1)[-1], fil, r.get('page'), '|', repr(r.get('old'))[:220], '=>', repr(r.get('new'))[:220], '|', str(r.get('source') or r.get('finding') or '')[:80])
for k, v in sorted(cnt.items()):
    print(k, v)
