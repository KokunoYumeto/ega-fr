import json, glob, re
n = 0
for fn in sorted(glob.glob('run_0IV1/findings_*.json')):
    d = json.load(open(fn, encoding='utf-8'))
    for f in d:
        fx = f.get('fix') or {}
        if not isinstance(fx, dict): continue
        new = fx.get('new', '') or ''
        old = fx.get('old', '') or ''
        if re.match(r'^\textup\{\(\d', new) or re.search(r'\textup\{\(\ref|\textup\{\sref', new):
            print(fn, json.dumps({'old': old, 'new': new, 'note': f.get('note')}, ensure_ascii=False)); n += 1
print(n)
