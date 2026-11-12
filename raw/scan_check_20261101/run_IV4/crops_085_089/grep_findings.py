import json, sys, glob
sys.stdout.reconfigure(encoding='utf-8')
# usage: grep_findings.py KEY VALUE [maxn]   e.g. convention 7
key, val = sys.argv[1], sys.argv[2]
maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 20
n = 0
for fn in sorted(glob.glob(r'user/Documents/ega_scan_check_20261101/run_IV*/findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception as e:
        continue
    for x in d:
        v = x.get(key)
        if (str(v) == val) or (key == 'text' and val in json.dumps(x, ensure_ascii=False)):
            print(fn.split('\\')[-1].split('/')[-1], json.dumps(x, ensure_ascii=False)[:900])
            n += 1
            if n >= maxn:
                sys.exit()
