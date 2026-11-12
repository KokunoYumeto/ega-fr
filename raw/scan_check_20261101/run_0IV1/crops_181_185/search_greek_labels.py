import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
for f in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        o = fx.get('old', '') or ''
        n = fx.get('new', '') or ''
        if '\item[$' in o and 'textup' in n:
            print(f, x['page'], x.get('convention'), '|', o[:60].replace('\n', '/'), '=>', n[:80].replace('\n', '/'))
