import json, glob, sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
os.chdir(r'user\Documents\ega_scan_check_20261101\run_IV4')
pats = sys.argv[1].split('||')
files = sys.argv[2] if len(sys.argv) > 2 else 'findings_*.json'
maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 400
for f in sorted(glob.glob(files)):
    if f.endswith('.orig'):
        continue
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        print('ERR', f, e)
        continue
    for x in d:
        fx = x.get('fix') or {}
        s = json.dumps(x, ensure_ascii=False)
        if any(p in s for p in pats):
            print(f, x.get('page'), x.get('kind'), x.get('convention'))
            print('   OLD:', repr(fx.get('old'))[:maxn])
            print('   NEW:', repr(fx.get('new'))[:maxn])
            print('   NOTE:', (x.get('note') or '')[:maxn])
