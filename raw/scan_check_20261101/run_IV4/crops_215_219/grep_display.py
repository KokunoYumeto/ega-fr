import json, glob, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
os.chdir(r'user\Documents\ega_scan_check_20261101')
n = 0
for f in sorted(glob.glob('run_IV*/findings_*.json')):
    if f.endswith('.orig'):
        continue
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        continue
    for x in d:
        fx = x.get('fix') or {}
        old = fx.get('old') or ''
        new = fx.get('new') or ''
        if ('\\[' in new and '\\[' not in old) or ('\\begin{equation' in new and 'equation' not in old):
            n += 1
            if n < 15:
                print(f, x.get('page'), x.get('kind'))
                print('   OLD:', repr(old)[:250])
                print('   NEW:', repr(new)[:250])
                print('   NOTE:', (x.get('note') or '')[:250])
print('total', n)
