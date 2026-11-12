import json, glob, re, sys

root = sys.argv[1]
pat_new = re.compile(r"\\textup\{\d+\}|\\emph\{[^}]*dimension\}\s*\d|\\emph\{de dimension\} \d")
n = 0
for f in sorted(glob.glob(root + '/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix')
        if isinstance(fx, dict):
            new = fx.get('new', '')
            if pat_new.search(new):
                n += 1
                if n <= 20:
                    print(f[len(root):][:32], x.get('page'), x.get('kind'), x.get('convention'), '|',
                          repr(fx.get('old'))[:70], '->', repr(new)[:90])
print(n)
