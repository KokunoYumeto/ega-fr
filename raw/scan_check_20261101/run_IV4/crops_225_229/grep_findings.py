import json
import glob
import sys

pat = sys.argv[1]
field = sys.argv[2] if len(sys.argv) > 2 else 'old'
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 40
n = 0
for f in sorted(glob.glob('user/Documents/ega_scan_check_20261101/run_IV*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        continue
    for x in d:
        fx = x.get('fix') or {}
        if not isinstance(fx, dict):
            fx = {}
        o = fx.get('old', '') or ''
        nw = fx.get('new', '') or ''
        target = {'old': o, 'new': nw, 'note': x.get('note', '') or '', 'any': o + ' ' + nw + ' ' + (x.get('note', '') or '')}[field]
        if pat in target:
            n += 1
            if n > limit:
                break
            sys.stdout.buffer.write((f.split('\\')[-1].split('/')[-1] + ' p' + str(x.get('page')) + ' ' + str(x.get('kind')) + ' conv=' + str(x.get('convention')) + '\n  OLD: ' + o[:200] + '\n  NEW: ' + nw[:200] + '\n  NOTE: ' + (x.get('note', '') or '')[:300] + '\n').encode('utf-8'))
