import json, re

SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega2\ega2-1-fr.tex"
FND = r"user\Documents\ega_scan_check_20261101\run_II\findings_030_034.json"

src = open(SRC, encoding="utf-8", newline="").read()
assert "\r" not in src
F = json.load(open(FND, encoding="utf-8"))

def segment(p):
    a = src.index("\\oldpage[II]{%d}" % p)
    b = src.index("\\oldpage[II]{%d}" % (p + 1))
    return a, b

bad = 0
for f in F:
    if f["fix"] is None:
        continue
    a, b = segment(f["page"])
    seg = src[a:b]
    n = seg.count(f["fix"]["old"])
    if n != 1:
        bad += 1
        print("page", f["page"], "count in source segment =", n, repr(f["fix"]["old"]))
print("checked", len(F), "bad", bad)
