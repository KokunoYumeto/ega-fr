"""Re-apply findings_220_224.json in memory (page-segment rule of apply_fixes.py) and print the edited page breaks."""
import json
import pathlib
import re

run = pathlib.Path(__file__).resolve().parent.parent
src = (run.parent / "ega-fr" / "source" / "ega4" / "ega4-2-fr.tex").read_text(encoding="utf-8")
F = json.load(open(run / "findings_220_224.json", encoding="utf-8"))
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


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


t = src
for x in F:
    if x["fix"]:
        s, e = locate(t, x["page"])
        seg = t[s:e]
        assert seg.count(x["fix"]["old"]) == 1, x
        t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
k = t.find("\\oldpage[IV-2]{222}")
print(t[k - 60:k + 70])
print("----", t.count("\\oldpage[IV-2]{221}"), "copy of the 221 marker")
k = t.find("Nous supposerons encore")
print(t[k - 60:k + 30])
print("----")
k = t.find("(ce qui sera par")
print(t[k - 10:k + 40])
print("----")
k = t.find("\\textbf{[33]}") if "\\textbf{[33]}" in t else t.find("[33] M.")
print(t[k:k + 200])
print(len(F), "entries,", sum(1 for x in F if x["fix"] is None), "with fix null")
