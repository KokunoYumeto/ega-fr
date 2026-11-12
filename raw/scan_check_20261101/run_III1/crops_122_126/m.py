import re
p = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/current/packages/BASE/native/ega3/ega3-1-fr.tex'
L = open(p, encoding='utf-8').read().split('\n')
for i, l in enumerate(L):
    m = re.match(r'\\oldpage\[III\]\{(\d+)\}', l)
    if m and 81 <= int(m.group(1)) <= 130:
        before = L[i-1] == ''
        after = L[i+1] == ''
        b = L[i-2] if before else L[i-1]
        a = L[i+2] if after else L[i+1]
        print(m.group(1), 'B' if before else '-', 'A' if after else '-', '|', b[-45:], '||', a[:45])
