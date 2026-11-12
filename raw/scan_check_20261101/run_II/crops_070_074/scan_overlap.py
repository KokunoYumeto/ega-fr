import json, glob, sys
# Read-only survey: fixes that combine \textup{(...)} with \textbf{0|I|II} in one edit.
root = r'user\Documents\ega_scan_check_20261101'
out = sys.stdout.buffer
n = 0
for f in sorted(glob.glob(root + r'\run_*\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        if not isinstance(fx, dict):
            continue
        w = fx.get('new', '') or ''
        if '\\textup{(' in w and '\\textbf{' in w:
            n += 1
            if n <= 5:
                out.write((f.split('\\')[-2] + '/' + f.split('\\')[-1] + ' ' + json.dumps({k: x.get(k) for k in ('page', 'kind', 'convention', 'fix', 'note')}, ensure_ascii=False)[:420] + '\n').encode('utf-8'))
out.write(('total ' + str(n) + '\n').encode('utf-8'))
