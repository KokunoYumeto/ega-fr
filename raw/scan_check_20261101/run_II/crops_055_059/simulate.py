"""Apply findings_055_059.json in memory, in listed order, to a copy of the current release text (no file is written),
the way apply_fixes.py does (old must occur once inside its page segment), and print the touched segments."""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
F = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex"
t = F.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(text)


bad = 0
for x in json.load(open(E / "run_II" / "findings_055_059.json", encoding="utf-8")):
    fx = x["fix"]
    if not fx or not fx.get("old") or fx["old"] == fx.get("new"):
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        bad += 1
        print("FAIL", x["page"], seg.count(fx["old"]), repr(fx["old"][:60]))
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("failures:", bad)
if len(sys.argv) > 1:
    a, b = int(sys.argv[1]), int(sys.argv[2])
    s, _ = locate(t, a)
    _, e = locate(t, b)
    sys.stdout.write(t[s - 120:e])
