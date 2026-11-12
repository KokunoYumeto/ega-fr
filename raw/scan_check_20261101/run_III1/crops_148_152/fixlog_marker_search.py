import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
root = r'user\Documents\ega_scan_check_20261101'
pat_before = re.compile(r'\n\n\\oldpage')
n = 0
for fn in ['FIXLOG_CURRENT.jsonl']:
    with open(root + '\\' + fn, encoding='utf-8') as f:
        for line in f:
            try:
                x = json.loads(line)
            except Exception:
                continue
            o = x.get('old', ''); nw = x.get('new', '')
            if pat_before.search(o):
                n += 1
                if n <= 10:
                    print(fn, json.dumps({'page': x.get('page'), 'part': x.get('part'), 'file': x['file'][-16:], 'old': o, 'new': nw}, ensure_ascii=False))
                    print()
print('count', n)
# also: fixes for part III with oldpage
m = 0
with open(root + '\\FIXLOG_CURRENT.jsonl', encoding='utf-8') as f:
    for line in f:
        try:
            x = json.loads(line)
        except Exception:
            continue
        if 'ega3-1' in x.get('file', '') and 'oldpage' in x.get('old', ''):
            m += 1
            if m <= 12:
                print('III', json.dumps({'page': x.get('page'), 'old': x['old'], 'new': x['new']}, ensure_ascii=False))
print('III marker fixes', m)
