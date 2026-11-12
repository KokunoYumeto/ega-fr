"""Simulate apply_fixes.py on an in-memory copy of ega4-11-fr.tex (no file is written)."""
import json
import pathlib
import re
import sys

src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex").read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
F = json.load(open(sys.argv[1], encoding="utf-8"))
order = F if len(sys.argv) < 3 else list(reversed(F))
ok = 0
for x in order:
    fx = x.get("fix")
    if not fx:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        print("FAIL", x["page"], repr(fx["old"][:50]), c)
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    ok += 1
print("applied", ok)
print("markers:", [(m.group(1), t.count("\n", 0, m.start()) + 1) for m in marker.finditer(t)
                   if 119 <= int(m.group(1)) <= 126])
for n in (120, 121, 123, 125):
    m = re.search(r"\\oldpage\[IV-3\]\{%d\}" % n, t)
    print(n, repr(t[m.start() - 110:m.end() + 70]))
out = pathlib.Path(__file__).resolve().parent / "simulated_ega4-11_120_125.txt"
lines = t.split("\n")
a = next(i for i, l in enumerate(lines) if "\\oldpage[IV-3]{120}" in l)
b = next(i for i, l in enumerate(lines) if "\\oldpage[IV-3]{126}" in l)
out.write_text("\n".join(lines[a - 3:b]), encoding="utf-8")
print("excerpt ->", out)
