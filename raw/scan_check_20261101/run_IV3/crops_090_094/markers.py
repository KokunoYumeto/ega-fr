import re
import sys

p = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-9-fr.tex"
t = open(p, encoding="utf-8").read()
both = before = after = none = 0
for m in re.finditer(r"\\oldpage\[IV-3\]\{(\d+)\}", t):
    b = t[:m.start()].endswith("\n\n")
    a = t[m.end():].startswith("\n\n")
    if a and b:
        both += 1
    elif b:
        before += 1
    elif a:
        after += 1
    else:
        none += 1
print("both", both, "before", before, "after", after, "none", none)
