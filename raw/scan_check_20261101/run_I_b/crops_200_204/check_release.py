import json
import pathlib
import re

SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega1\ega1-10-fr.tex")
FND = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b\findings_200_204.json")
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
bad = 0
for x in json.load(open(FND, encoding="utf-8")):
    fx = x.get("fix")
    if not fx:
        continue
    s = seg[x["page"]]
    c = s.count(fx["old"])
    if c != 1:
        bad += 1
        print("release segment count", c, x["page"], repr(fx["old"]))
    else:
        seg[x["page"]] = s.replace(fx["old"], fx["new"])
print("release-segment problems:", bad, "(read only, nothing written)")
