import glob
import re

D = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4"
for f in sorted(glob.glob(D + r"\ega4-*.tex")):
    t = open(f, encoding="utf-8").read()
    a = len(re.findall(r"\\textbf\{[IVX]+\)\}", t))
    b = t.count(r"n$^\circ$")
    if a or b:
        print(f.split("\\")[-1], "bold step labels:", a, " n$^\\circ$:", b)
