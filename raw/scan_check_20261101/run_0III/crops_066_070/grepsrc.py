import re, sys
base = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/'
fn = sys.argv[1]
needle = sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 0
lines = open(base + fn, encoding='utf-8').read().split('\n')
n = 0
for i, l in enumerate(lines):
    if needle in l:
        n += 1
        for j in range(max(0, i - ctx), min(len(lines), i + ctx + 1)):
            print(f'{j+1}: {lines[j]}')
        if ctx:
            print('--')
print('count', n)
