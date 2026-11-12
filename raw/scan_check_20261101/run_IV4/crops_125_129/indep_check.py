import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
src = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
t = open(src, encoding="utf-8").read()
m = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
F = json.load(open(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_125_129.json", encoding="utf-8"))
bad = 0
for i, x in enumerate(F):
    f = x.get("fix")
    if not f:
        continue
    c = seg[x["page"]].count(f["old"])
    if c != 1:
        bad += 1
        print("original-segment count", c, i, x["page"], f["old"][:60])
print("independent check on original source segments: bad =", bad)
