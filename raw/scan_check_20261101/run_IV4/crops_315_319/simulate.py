"""Apply findings_315_319.json in list order to a copy of the source segment (pp. 315-319)
and write the result to the crops folder for review. Does not touch any .tex in the edition.
"""
import json

BASE = r"user\Documents\ega_scan_check_20261101"
SRC = BASE + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21c-fr.tex"
F = json.load(open(BASE + r"\run_IV4\findings_315_319.json", encoding="utf-8"))
src = open(SRC, encoding="utf-8").read().replace("\r\n", "\n")
a = src.index("\\oldpage[IV-4]{315}")
b = src.index("\\oldpage[IV-4]{320}")
seg = src[a:b]
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    n = seg.count(fx["old"])
    assert n == 1, (d["page"], fx["old"][:50], n)
    seg = seg.replace(fx["old"], fx["new"])
open(BASE + r"\run_IV4\crops_315_319\segment_after_fixes.tex", "w", encoding="utf-8", newline="\n").write(seg)
print("applied; length", len(seg))
