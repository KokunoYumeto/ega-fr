import re
import sys

path = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
t = open(path, encoding="utf-8").read()
pat = re.compile(r"\\item\[\\emph\{[ivx]+\)\}\]")
lines = [t.count("\n", 0, m.start()) + 1 for m in pat.finditer(t)]
print("emph roman labels without opening parenthesis:", len(lines), lines)
pat2 = re.compile(r"\\item\[\\emph\{\([ivx]+\)\}\]")
print("emph roman labels with parentheses:", len(list(pat2.finditer(t))))
pat3 = re.compile(r"\\item\[\\emph\{[a-f]'?\)\}\]")
print("emph letter labels:", len(list(pat3.finditer(t))))
print("Cohen--Macaulay:", t.count("Cohen--Macaulay"), "Cohen-Macaulay:", t.count("Cohen-Macaulay") - t.count("Cohen--Macaulay"))
# markers lines
for m in re.finditer(r"\\oldpage\[IV-2\]\{(19[0-5])\}", t):
    print("marker", m.group(1), "line", t.count("\n", 0, m.start()) + 1)
