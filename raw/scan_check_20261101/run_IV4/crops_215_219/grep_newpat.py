import json, glob, sys, io, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
os.chdir(r'user\Documents\ega_scan_check_20261101')
rx = re.compile(sys.argv[1])
globpat = sys.argv[2] if len(sys.argv) > 2 else 'run_*/findings_*.json'
n = 0
for f in sorted(glob.glob(globpat)):
    if f.endswith('.orig'):
        continue
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        fx = x.get('fix') or {}
        old = fx.get('old') or ''
        new = fx.get('new') or ''
        if rx.search(new) and not rx.search(old):
            n += 1
            if n < 20:
                print(f, x.get('page'), x.get('kind'), x.get('convention'))
                print('   OLD:', repr(old)[:250])
                print('   NEW:', repr(new)[:250])
                print('   NOTE:', (x.get('note') or '')[:250])
print('total', n)
