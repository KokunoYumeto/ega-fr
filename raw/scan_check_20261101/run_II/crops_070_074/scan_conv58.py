import json, glob, sys
# Read-only survey: sample convention 5 and 8 fixes from run_II, and display->inline layout fixes.
root = r'user\Documents\ega_scan_check_20261101'
out = sys.stdout.buffer
seen = {5: 0, 8: 0, 'inline': 0}
for f in sorted(glob.glob(root + r'\run_II\findings_*.json')) + sorted(glob.glob(root + r'\run_I_*\findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        c = x.get('convention')
        fx = x.get('fix') or {}
        if c in (5, 8) and seen[c] < 4:
            seen[c] += 1
            out.write((f.split('\\')[-2] + '/' + f.split('\\')[-1] + ' ' + json.dumps({k: x.get(k) for k in ('page', 'convention', 'fix', 'note')}, ensure_ascii=False)[:330] + '\n').encode('utf-8'))
        if isinstance(fx, dict) and (fx.get('old') or '').startswith('\\[') and (fx.get('new') or '').startswith('$') and seen['inline'] < 3:
            seen['inline'] += 1
            out.write(('INLINE ' + f.split('\\')[-2] + '/' + f.split('\\')[-1] + ' ' + json.dumps({k: x.get(k) for k in ('page', 'kind', 'confidence', 'fix', 'note')}, ensure_ascii=False)[:420] + '\n').encode('utf-8'))
