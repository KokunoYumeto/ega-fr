import glob
import sys

root = 'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/'
pats = sys.argv[1:]
tot = {p: 0 for p in pats}
for f in sorted(glob.glob(root + '**/*.tex', recursive=True)):
    s = open(f, encoding='utf-8').read()
    row = []
    for p in pats:
        c = s.count(p)
        tot[p] += c
        row.append(c)
    if any(row):
        print(f.replace('\\', '/').split('packages/')[-1], row)
print('TOTAL', tot)
