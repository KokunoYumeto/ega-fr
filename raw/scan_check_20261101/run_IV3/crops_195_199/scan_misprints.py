import json, glob, sys
sys.stdout.reconfigure(encoding='utf-8')
root = r'user\Documents\ega_scan_check_20261101\run_IV3'
n = 0
for fn in sorted(glob.glob(root + r'\findings_1[5-6]*.json')):
    d = json.load(open(fn, encoding='utf-8'))
    for x in d:
        if x['kind'] == 'misprint_in_print':
            n += 1
            f = x.get('fix')
            print(fn.split('\\')[-1], x['page'], '| fix:', None if f is None else (f['old'][:50], f['new'][:50]), '| corrected:', repr(x.get('corrected'))[:90])
            print('   scan:', x['scan'][:120], '| tex:', x['tex'][:100])
print(n)
