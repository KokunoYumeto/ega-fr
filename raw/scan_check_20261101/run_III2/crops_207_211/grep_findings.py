import json, glob, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(r'user\Documents\ega_scan_check_20261101')
pat = re.compile(sys.argv[1])
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 30
files = sorted(glob.glob('run_*/findings_*.json')) + sorted(glob.glob('MANUAL_*.json'))
n = 0
for fn in files:
    try:
        d = json.load(open(fn, encoding='utf-8'))
    except Exception:
        continue
    if isinstance(d, dict):
        d = d.get('findings', [])
    for x in d:
        if not isinstance(x, dict):
            continue
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            n += 1
            if n <= limit:
                print(fn, x.get('page'), x.get('kind'), x.get('convention'), '|',
                      (x.get('where') or '')[:70], '|', (x.get('scan') or '')[:70], '|',
                      (x.get('tex') or '')[:50], '| fix:', json.dumps(x.get('fix'), ensure_ascii=False)[:160])
print('total', n)
