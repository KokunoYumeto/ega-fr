import json, glob, sys
# Read-only survey: how prior checkers treated \cdots / \ldots against the print's dots.
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
        o = fx.get('old', '') or ''
        w = fx.get('new', '') or ''
        if ('\\cdots' in o and '\\ldots' in w) or ('\\ldots' in o and '\\cdots' in w) or ('\\dots' in o and '\\cdots' in w) or ('\\cdots' in o and '\\dots' in w):
            n += 1
            if n <= 6:
                out.write((f.split('\\')[-2] + '/' + f.split('\\')[-1] + ' ' + json.dumps({k: x.get(k) for k in ('page', 'kind', 'fix', 'note')}, ensure_ascii=False)[:300] + '\n').encode('utf-8'))
out.write(('total ' + str(n) + '\n').encode('utf-8'))
