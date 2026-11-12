import json
import pathlib
import re

# Dry run (no writes): apply the fixes, in order, to the real source page segments, as apply_fixes.py would.
src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex").read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    if 110 <= n <= 114:
        seg[n] = src[s:cuts[i + 1][1]]
d = json.load(open(r"user\Documents\ega_scan_check_20261101\run_II\findings_110_114.json", encoding="utf-8"))
bad = 0
for x in d:
    f = x["fix"]
    if not f:
        continue
    c = seg[x["page"]].count(f["old"])
    if c != 1:
        bad += 1
        print("source count", c, x["page"], repr(f["old"]))
    else:
        seg[x["page"]] = seg[x["page"]].replace(f["old"], f["new"])
print("bad", bad)
# show the page boundaries after the fixes
for n in (112, 113):
    print(repr(seg[n][-60:]))
for n in (113, 114):
    print(repr(seg[n][:60]))
