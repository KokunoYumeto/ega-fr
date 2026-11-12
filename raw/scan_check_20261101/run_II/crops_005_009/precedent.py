"""Print earlier findings matching a predicate (read-only helper)."""
import glob
import json
import sys

D = 'user/Documents/ega_scan_check_20261101'
sys.stdout.reconfigure(encoding='utf-8')
mode = sys.argv[1]
n = 0
for f in sorted(glob.glob(D + '/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        old = fx.get('old', '') if isinstance(fx, dict) else ''
        new = fx.get('new', '') if isinstance(fx, dict) else ''
        hit = False
        if mode == 'dropemph':
            hit = '\\emph{' in old and '\\emph{' not in new
        elif mode == 'bold':
            hit = '\\textbf{I' in new or '\\textbf{0}' in new
        elif mode == 'marker':
            hit = x.get('kind') == 'marker'
        elif mode == 'kw':
            hit = sys.argv[2].lower() in json.dumps(x, ensure_ascii=False).lower()
        if hit and n < int(sys.argv[-1]):
            n += 1
            print(f[len(D) + 1:], '|', x.get('kind'), x.get('convention'), '|', x.get('where', '')[:90])
            print('   old:', old[:120].replace('\n', '\\n'))
            print('   new:', new[:120].replace('\n', '\\n'))
            print('   note:', (x.get('note') or '')[:250])
