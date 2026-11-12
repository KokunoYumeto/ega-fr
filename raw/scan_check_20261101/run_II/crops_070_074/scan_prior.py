import json, glob, collections, sys
# Survey of prior checkers' fixes (read-only): how references inside italic statements were handled.
root = r'user\Documents\ega_scan_check_20261101'
cnt = collections.Counter(); ex = {}
for f in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        if not isinstance(fx, dict):
            continue
        n = fx.get('new', '') or ''
        if '\\textup{(\\hyperref' in n or '\\textup{(' in n:
            cnt[f] += 1
            ex.setdefault(f, (x.get('page'), x.get('convention'), fx))
for f, c in cnt.items():
    sys.stdout.buffer.write((f + ' ' + str(c) + ' ' + json.dumps(ex[f], ensure_ascii=False)[:240] + '\n').encode('utf-8'))
