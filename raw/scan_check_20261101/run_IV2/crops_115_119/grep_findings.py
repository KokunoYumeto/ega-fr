import json, glob, sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
pat = re.compile(sys.argv[1])
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 8
root = sys.argv[3] if len(sys.argv) > 3 else r'user\Documents\ega_scan_check_20261101\run_IV2'
n = 0
for f in sorted(glob.glob(root + r'\findings_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for x in d:
        s = json.dumps(x, ensure_ascii=False)
        if pat.search(s):
            n += 1
            if n <= limit:
                print(f.split('\\')[-1], s[:1000])
                print()
print('total matches', n)
