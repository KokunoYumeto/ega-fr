import json, sys, pathlib
part = sys.argv[1]; lo = int(sys.argv[2]); hi = int(sys.argv[3])
fn = sys.argv[4] if len(sys.argv) > 4 else 'FIXLOG.jsonl'
filt = sys.argv[5] if len(sys.argv) > 5 else ''
for line in open('user/Documents/ega_scan_check_20261101/' + fn, encoding='utf-8'):
    x = json.loads(line)
    if x.get('part') == part and lo <= int(x.get('page', -1)) <= hi and filt in pathlib.Path(x.get('file', '')).name:
        print(x['page'], pathlib.Path(x['file']).name, x.get('kind'), x.get('convention'), repr(x['old'])[:170], '=>', repr(x['new'])[:220])
