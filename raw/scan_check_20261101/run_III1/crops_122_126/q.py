import json
for line in open(r'user/Documents/ega_scan_check_20261101/FIXLOG_CURRENT.jsonl', encoding='utf-8'):
    x = json.loads(line)
    if x['part'] == 'III' and ('oldpage' in x['old'] or x['old'].endswith('\n\n')):
        print(x['page'], repr(x['old'])[:150], '->', repr(x['new'])[:150], x.get('source'))
