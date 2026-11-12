"""Check the findings' 'old' strings against the current release file (page segments), read-only."""
import json
import pathlib
import re

E = pathlib.Path(r"user/Documents/ega_scan_check_20261101")
rel = E / r"ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega1/ega0-1-fr.tex"
t = rel.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    seg[n] = t[s:e]
for n in range(65, 71):
    local = (E / f"run_0I/page_{n:03d}.tex").read_text(encoding="utf-8").split("\n", 1)[1]
    print(n, "segment identical to page file:", local == seg[n], len(local), len(seg[n]))
f = json.load(open(E / "run_0I/findings_066_070.json", encoding="utf-8"))
for x in f:
    if not x["fix"]:
        continue
    c = seg[x["page"]].count(x["fix"]["old"])
    if c != 1:
        print("release count", c, x["page"], repr(x["fix"]["old"])[:80])
print("tail of 70:", repr(seg[70][-80:]))
