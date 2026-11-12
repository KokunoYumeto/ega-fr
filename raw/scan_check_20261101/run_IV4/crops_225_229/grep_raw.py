import glob
import json
import sys

pats = sys.argv[1:]
n = 0
for f in sorted(glob.glob('user/Documents/ega_scan_check_20261101/run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') if isinstance(x.get('fix'), dict) else {}
        blob = ' | '.join(str(v) for v in [x.get('scan'), x.get('tex'), fx.get('old'), fx.get('new'), x.get('note')])
        if any(p in blob for p in pats):
            n += 1
            if n <= 25:
                ff = f.replace('\\', '/').split('/')
                sys.stdout.buffer.write((ff[-2] + '/' + ff[-1] + ' p' + str(x.get('page')) + ' ' + str(x.get('kind')) + ' conv=' + str(x.get('convention')) + '\n  ' + blob[:700] + '\n').encode('utf-8'))
print('total', n)
