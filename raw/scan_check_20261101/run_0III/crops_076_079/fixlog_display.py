import json, sys
sys.stdout.reconfigure(encoding='utf-8')
fn = r'user/Documents/ega_scan_check_20261101/FIXLOG.jsonl'
n = 0
with open(fn, encoding='utf-8') as f:
    for line in f:
        try:
            r = json.loads(line)
        except Exception:
            continue
        old = r.get('old') or ''
        new = r.get('new') or ''
        if ('\\[' in old and '\\[' not in new) or ('begin{equation' in old and 'begin{equation' not in new):
            n += 1
            if n <= 6:
                print(r.get('file', '')[-30:], r.get('page'), r.get('kind'), r.get('convention'), r.get('source'))
                print('  OLD:', repr(old)[:400])
                print('  NEW:', repr(new)[:400])
print('total', n)
