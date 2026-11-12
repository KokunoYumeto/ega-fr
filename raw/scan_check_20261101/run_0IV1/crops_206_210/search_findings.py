import json, glob, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
pat = re.compile(sys.argv[1])
maxn = int(sys.argv[2]) if len(sys.argv) > 2 else 40
n = 0
for fn in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_0IV1\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception as e:
        print('ERR', fn, e)
        continue
    for f in d:
        s = json.dumps(f, ensure_ascii=False)
        if pat.search(s):
            keep = {k: f.get(k) for k in ('page', 'where', 'kind', 'convention', 'fix', 'note')}
            print(fn.split('\\')[-1], json.dumps(keep, ensure_ascii=False)[:700])
            n += 1
            if n >= maxn:
                sys.exit(0)
