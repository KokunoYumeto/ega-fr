import json, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r'user/Documents/ega_scan_check_20261101/run_IV4/findings_080_084.json', encoding='utf-8'))
pages = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else None
for x in d:
    if pages is None or x['page'] in pages:
        print(json.dumps(x, ensure_ascii=False))
        print()
