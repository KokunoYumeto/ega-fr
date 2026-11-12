import json, sys, glob
sys.stdout.reconfigure(encoding="utf-8")

# usage: python search_findings.py <substring> [<substring2>]  -- searches all run_*/findings_*.json
root = r'user\Documents\ega_scan_check_20261101'
subs = sys.argv[1:]
n = 0
for fn in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if all(t in s for t in subs):
            print(fn.split('\\')[-2] + '/' + fn.split('\\')[-1], s[:900])
            print('--')
            n += 1
print('matches:', n)
