import json, glob, sys
pat = sys.argv[1]
runs = sys.argv[2] if len(sys.argv) > 2 else 'run_*'
n = 0
for f in sorted(glob.glob(r'user/Documents/ega_scan_check_20261101/' + runs + '/findings_*.json')):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        raw = json.dumps(x.get('fix'), ensure_ascii=False) + ' ' + str(x.get('tex')) + ' ' + str(x.get('note')) + ' ' + str(x.get('scan')) + ' ' + str(x.get('where'))
        if pat in raw or pat in s:
            n += 1
            if n <= int(sys.argv[3] if len(sys.argv) > 3 else 15):
                sys.stdout.buffer.write((f.split('/')[-1] + ' ' + s[:700] + '\n\n').encode('utf-8'))
print('TOTAL', n)
