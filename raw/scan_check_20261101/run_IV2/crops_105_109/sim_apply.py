"""In-memory simulation of apply_fixes.py on the release source (nothing is written)."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
t = (E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex").read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
F = json.load(open(E / r"run_IV2\findings_105_109.json", encoding="utf-8"))
applied = manual = 0
for x in F:
    fix = x.get("fix")
    if not fix or not fix.get("old") or fix.get("old") == fix.get("new"):
        continue
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    i = [k for k, (n, s) in enumerate(cuts) if n == x["page"]][0]
    s, e = cuts[i][1], cuts[i + 1][1]
    seg = t[s:e]
    if seg.count(fix["old"]) != 1:
        manual += 1
        print("MANUAL", x["page"], repr(fix["old"]), seg.count(fix["old"]))
        continue
    t = t[:s] + seg.replace(fix["old"], fix["new"]) + t[e:]
    applied += 1
print("applied", applied, "manual", manual)
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
i = [k for k, (n, s) in enumerate(cuts) if n == 107][0]
print(t[cuts[i + 1][1] - 120:cuts[i + 1][1] + 120])
