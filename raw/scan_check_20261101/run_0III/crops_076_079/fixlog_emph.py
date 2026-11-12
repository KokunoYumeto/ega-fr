import json
fn = r'user/Documents/ega_scan_check_20261101/FIXLOG.jsonl'
with open(fn, encoding='utf-8') as f:
    for line in f:
        try:
            r = json.loads(line)
        except Exception:
            continue
        fil = str(r.get('file', ''))
        if 'ega3-1' not in fil:
            continue
        old = r.get('old') or ''
        new = r.get('new') or ''
        if ('emph' in old or 'emph' in new or 'textup' in new or 'boldsymbol' in new or 'leadsto' in new
                or 'mathbf{e}' in new or 'oldpage' in old or 'oldpage' in new):
            print(r.get('page'), '|', repr(old)[:300], '=>', repr(new)[:300])
            keys = [k for k in r.keys() if k not in ('old', 'new', 'file')]
            print('    ', {k: str(r[k])[:200] for k in keys})
