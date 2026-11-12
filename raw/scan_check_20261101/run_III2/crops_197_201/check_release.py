# Checks the findings' "old" strings against the release file segments that apply_fixes.py uses.
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
f = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega3/ega3-7-fr.tex"
t = f.read_text(encoding="utf-8")
print("release file line ends:", "CRLF" if "\r\n" in t else "LF")
m = re.compile(r"\\oldpage\[III\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    seg[n] = t[s:e]
d = json.load(open(E / "run_III2/findings_197_201.json", encoding="utf-8"))
bad = 0
work = {n: seg[n] for n in range(197, 202)}
for x in d:
    if not x["fix"]:
        continue
    o = x["fix"]["old"]
    if seg[x["page"]].count(o) != 1 or work[x["page"]].count(o) != 1:
        bad += 1
        print("BAD", x["page"], repr(o[:60]))
    else:
        work[x["page"]] = work[x["page"]].replace(o, x["fix"]["new"])
print("bad", bad)
for n in range(197, 202):
    pt = (E / f"run_III2/page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pt.split("\n", 1)[1]
    print(n, "page file == release segment:", body == seg[n])
