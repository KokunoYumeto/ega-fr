import json, glob, collections, os, sys
root = sys.argv[1]
cnt = collections.Counter(); ex = {}
for f in sorted(glob.glob(os.path.join(root, 'run_*', 'findings_*.json'))):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    run = os.path.basename(os.path.dirname(f))
    for d in data:
        if not isinstance(d, dict):
            continue
        if d.get('convention') == 6:
            fx = d.get('fix') or {}
            new = fx.get('new', '') if isinstance(fx, dict) else ''
            isref = ('hyperref' in new) and ('textup' in new)
            cnt[(run, isref)] += 1
            if isref and run not in ex:
                ex[run] = json.dumps(d, ensure_ascii=False)[:450]
for k, v in sorted(cnt.items()):
    print(k, v)
for r, s in list(ex.items())[:5]:
    print(r, s); print()
