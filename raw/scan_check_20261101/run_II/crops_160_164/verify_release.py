import json
import re
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / r"ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega2/ega2-1-fr.tex").read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]
d = json.load(open(E / "run_II/findings_160_164.json", encoding="utf-8"))
cur = dict(seg)
bad = 0
for x in d:
    f = x.get("fix")
    if not f:
        continue
    c = cur[x["page"]].count(f["old"])
    if c != 1:
        bad += 1
        print("FAIL", x["page"], c, repr(f["old"][:70]))
        continue
    cur[x["page"]] = cur[x["page"]].replace(f["old"], f["new"])
print("checked against current release segments; failures:", bad)
