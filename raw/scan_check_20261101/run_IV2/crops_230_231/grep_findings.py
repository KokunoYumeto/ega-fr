import json, glob, sys, os
sys.stdout.reconfigure(encoding='utf-8')
pat = [p.lower() for p in sys.argv[1:]]
root = r'user\Documents\ega_scan_check_20261101'
for f in sorted(glob.glob(os.path.join(root, 'run_*', 'findings_*.json'))):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        print(f, 'ERR', e)
        continue
    rel = os.path.relpath(f, root)
    for x in d:
        s = json.dumps(x, ensure_ascii=False).lower()
        if all(p in s for p in pat):
            print(rel, x.get('page'), x.get('kind'), '|', (x.get('tex') or '')[:90], '|',
                  (x.get('scan') or '')[:90], '|', (x.get('note') or '')[:300], '|',
                  json.dumps(x.get('fix'), ensure_ascii=False)[:220])
