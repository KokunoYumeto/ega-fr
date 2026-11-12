import sys
F = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-18-fr.tex'
lines = open(F, encoding='utf-8', newline='').read().split('\n')
for n in (335, 397, 459, 523, 600, 675):
    print('== line', n)
    for i in range(n - 4, n + 2):
        print(i, repr(lines[i - 1])[:110])
