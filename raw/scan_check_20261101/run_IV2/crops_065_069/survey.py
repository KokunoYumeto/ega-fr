import json, glob, sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')
root = sys.argv[1]
want = sys.argv[2] if len(sys.argv) > 2 else None
c = Counter()
ex = {}
for f in sorted(glob.glob(root + '/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        if x.get('convention') == 6 and x.get('fix'):
            old = x['fix'].get('old', '')
            new = x['fix'].get('new', '')
            if '\\emph{' in new and '\\emph{' not in old:
                k = 'add_emph'
            elif '\\textup{' in new and '\\textup{' not in old:
                k = 'add_textup'
            elif '\\emph{' in old and '\\emph{' not in new:
                k = 'drop_emph'
            else:
                k = 'other'
            c[k] += 1
            ex.setdefault(k, [])
            if len(ex[k]) < 4:
                ex[k].append((f, json.dumps(x, ensure_ascii=False)[:500]))
print(c)
for k, v in ex.items():
    if want and k != want:
        continue
    print('==', k)
    for f, s in v:
        print(f)
        print(s)
        print()
