import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
cnt = {'emph': 0, 'textup': 0}
ex = {'emph': [], 'textup': []}
for f in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        if not isinstance(x, dict) or x.get('convention') != 6:
            continue
        fx = x.get('fix')
        if not isinstance(fx, dict):
            continue
        o = fx.get('old') or ''
        nw = fx.get('new') or ''
        if '(' in nw and 'textup' in nw:
            continue
        for k in cnt:
            if ('\\' + k + '{') in nw and ('\\' + k + '{') not in o:
                cnt[k] += 1
                if len(ex[k]) < 6:
                    ex[k].append((f, x.get('page'), o[:80], nw[:100], (x.get('note') or '')[:120]))
print(cnt)
for k in ex:
    for e in ex[k]:
        print(k, e)
