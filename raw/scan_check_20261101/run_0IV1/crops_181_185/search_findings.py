import json, glob, sys, re
sys.stdout.reconfigure(encoding='utf-8')
# usage: python search_findings.py <regex on old> <regex on new> [kind]
pat_old = re.compile(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] else None
pat_new = re.compile(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else None
kind = sys.argv[3] if len(sys.argv) > 3 else None
root = r'user\Documents\ega_scan_check_20261101'
for f in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        o = fx.get('old', '') or ''
        n = fx.get('new', '') or ''
        if pat_old and not pat_old.search(o):
            continue
        if pat_new and not pat_new.search(n):
            continue
        if kind and x.get('kind') != kind:
            continue
        print(f.split('\\')[-2] + '/' + f.split('\\')[-1], x.get('page'), x.get('kind'), x.get('convention'), '|', x.get('where', '')[:70], '|', o[:70].replace('\n', '/'), '=>', n[:90].replace('\n', '/'), '|', (x.get('note') or '')[:160])
