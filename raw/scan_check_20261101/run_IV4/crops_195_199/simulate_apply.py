"""Simulate apply_fixes.py on an in-memory copy of ega4-18-fr.tex (no file is written) and print the result for pp. 195-199."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


F = json.load(open(RUN / "findings_195_199.json", encoding="utf-8"))
bad = 0
for x in F:
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        bad += 1
        print("FAIL", x["page"], repr(fx["old"]), seg.count(fx["old"]))
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("failures:", bad)
a = t.index("\\oldpage[IV-4]{195}") - 300
b = t.index("\\oldpage[IV-4]{200}") + 60
out = RUN / "crops_195_199" / "simulated_195_199.tex"
out.write_text(t[a:b], encoding="utf-8")
print("markers:", [m.group(0) for m in marker.finditer(t[a:b])])
