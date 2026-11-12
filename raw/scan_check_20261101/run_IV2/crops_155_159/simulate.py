import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex").read_text(encoding="utf-8")
L = json.load(open(E / r"run_IV2\findings_155_159.json", encoding="utf-8"))
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
for x in L:
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    assert seg.count(x["fix"]["old"]) == 1, x
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
a = t.index(r"\oldpage[IV-2]{155}")
b = t.index(r"\oldpage[IV-2]{161}")
(E / r"run_IV2\crops_155_159\simulated_155_160.tex").write_text(t[a:b], encoding="utf-8")
print("ok", b - a)
