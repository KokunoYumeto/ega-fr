import re
from collections import Counter

p = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
t = open(p, encoding="utf-8").read()
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", t)]
c = Counter()
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    k = len(re.findall(r"\\mathfrak\s*\{?R", t[s:e]))
    if k:
        c[n] = k
print(sorted(c.items()))
print("before first marker:", len(re.findall(r"\\mathfrak\s*\{?R", t[: cuts[0][1]])))
print("markers:", cuts[0][0], "...", cuts[-1][0])
