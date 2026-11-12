import json, glob, sys, os
pat = sys.argv[1].replace('\\n', '\n')
runs = sys.argv[2] if len(sys.argv) > 2 else 'run_*'
lim = int(sys.argv[3]) if len(sys.argv) > 3 else 10
n = 0
for f in sorted(glob.glob(r'user/Documents/ega_scan_check_20261101/' + runs + '/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        if isinstance(fx, dict) and (pat in (fx.get('new') or '') or pat in (fx.get('old') or '')):
            n += 1
            if n <= lim:
                sys.stdout.buffer.write((os.path.basename(f) + ' ' + os.path.basename(os.path.dirname(f)) + ' ' + json.dumps(x, ensure_ascii=False)[:600] + '\n\n').encode('utf-8'))
print('TOTAL', n)
