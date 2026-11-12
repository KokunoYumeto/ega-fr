import json, glob, sys
BS = chr(92)
n = 0
for f in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        if not isinstance(x, dict):
            continue
        fx = x.get('fix')
        if not isinstance(fx, dict):
            continue
        o = fx.get('old') or ''
        nw = fx.get('new') or ''
        if BS + 'ar' in o and (o.replace('^', '_') == nw.replace('^', '_') or BS + 'wr' in o or BS + 'wr' in nw):
            n += 1
            if n <= 15:
                print(f, x.get('page'), x.get('kind'), '|', repr(o[:140]), '->', repr(nw[:140]))
                print('   note:', (x.get('note') or '')[:250])
print(n)
