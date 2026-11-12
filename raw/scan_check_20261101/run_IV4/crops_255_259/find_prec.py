import json, glob, re, sys

pat_I = re.compile(r'\\(mathscr|sh|mathcal)\{?I\}?')
pat_J = re.compile(r'\\(mathscr|sh|mathcal)\{?J\}?')
n = 0
for f in sorted(glob.glob(r'user\Documents\ega_scan_check_20261101\run_IV*\findings_*.json')):
    try:
        data = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for d in data:
        fx = d.get('fix') or {}
        new = fx.get('new', '') if fx else ''
        old = fx.get('old', '') if fx else ''
        if (pat_I.search(new) and pat_J.search(old) and not pat_I.search(old)) or (pat_J.search(new) and pat_I.search(old) and not pat_J.search(old)):
            n += 1
            if n < 12:
                print(f.split('\\')[-2], f.split('\\')[-1], d['page'], d['kind'], d.get('convention'), '|', old[:70], '=>', new[:70], '|', d.get('note', '')[:100])
print(n)
