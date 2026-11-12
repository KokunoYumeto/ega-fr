"""Compare my page files with the CURRENT source segments and re-check every fix 'old' (in order)."""
import difflib
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-20-fr.tex")
src = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]
for p in range(235, 240):
    page = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = page.split("\n", 1)[1]  # drop the '% from ...' line
    a, b = body.rstrip("\n"), seg[p].rstrip("\n")
    if a == b:
        print(p, "segment identical to page file")
    else:
        print(p, "DIFFERS:")
        for ln in difflib.unified_diff(a.split("\n"), b.split("\n"), "page", "current", n=0, lineterm=""):
            print("   ", ln[:200])
X = json.load(open(RUN / "findings_235_239.json", encoding="utf-8"))
cur = dict(seg)
bad = 0
for x in X:
    fx = x["fix"]
    if not fx:
        continue
    c = cur[x["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("PROBLEM", x["page"], repr(fx["old"]), c)
    cur[x["page"]] = cur[x["page"]].replace(fx["old"], fx["new"])
print("fix problems against current source:", bad)
# context of the p. 234/235 boundary
i = src.index("\\oldpage[IV-4]{235}")
print(repr(src[i - 120:i + 80]))
