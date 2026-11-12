import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
n = 0
nnull = 0
for f in sorted(glob.glob('run_*/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        if not isinstance(x, dict) or x.get('convention') != 7:
            continue
        n += 1
        fx = x.get('fix')
        if fx is None:
            nnull += 1
        if n <= 12 or 'run_0IV1' in f:
            print(f, x.get('page'), '|', x.get('where', '')[:90])
            print('   fix:', json.dumps(fx, ensure_ascii=False)[:200])
            print('   note:', (x.get('note') or '')[:200])
print('total conv7', n, 'null fixes', nnull)
