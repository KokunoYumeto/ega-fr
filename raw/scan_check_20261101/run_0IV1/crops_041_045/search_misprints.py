import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r'user\Documents\ega_scan_check_20261101\MISPRINTS.json', encoding='utf-8'))
pat = re.compile(sys.argv[1])
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
print('entries', len(d))
print('example keys', list(d[0].keys()) if isinstance(d[0], dict) else d[0])
n = 0
for x in d:
    s = json.dumps(x, ensure_ascii=False)
    if pat.search(s):
        n += 1
        if n <= limit:
            print('---', s[:700])
print('matches', n)
