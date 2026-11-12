import json, sys
n = 0
for fn in ['FIXLOG.jsonl', 'FIXLOG_CURRENT.jsonl']:
    for line in open('user/Documents/ega_scan_check_20261101/' + fn, encoding='utf-8'):
        try:
            x = json.loads(line)
        except Exception:
            continue
        old = x.get('old', ''); new = x.get('new', '')
        why = x.get('why', '')
        if ('diagram' in why.lower() and ('period' in why.lower() or 'full stop' in why.lower())):
            print(fn, json.dumps({'old': old, 'new': new, 'why': why}, ensure_ascii=False)[:500]); n += 1
            if n > 12:
                sys.exit()
