import json
import re

REL = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex"
BASE = r"user\Documents\ega_scan_check_20261101\run_II"
rel = open(REL, encoding="utf-8").read()
marks = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[II\]\{(\d+)\}", rel)]
segs = {}
for i, (n, s) in enumerate(marks):
    if 115 <= n <= 119:
        seg = rel[s:marks[i + 1][1]]
        segs[n] = seg
        t = open(BASE + rf"\page_{n}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
        t = t[t.index("\\oldpage"):]
        print(n, "identical" if seg == t else "DIFFERENT", len(seg), len(t))
F = json.load(open(BASE + r"\findings_115_119.json", encoding="utf-8"))
sim = dict(segs)
bad = 0
for i, d in enumerate(F):
    fx = d["fix"]
    if not fx:
        continue
    c = sim[d["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("release count", c, i, repr(fx["old"]))
    else:
        sim[d["page"]] = sim[d["page"]].replace(fx["old"], fx["new"])
print("release simulation:", "ok" if not bad else f"{bad} problems")
