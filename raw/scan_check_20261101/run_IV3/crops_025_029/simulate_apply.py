"""Dry run in memory (no file is written): apply findings_025_029.json to ega4-8-fr.tex with the same page-segment
logic as apply_fixes.py, in file order and in reverse order, and report any fix whose old string is not unique."""
import json
import pathlib
import re

SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV3\native\ega4\ega4-8-fr.tex")
FIND = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3\findings_025_029.json")
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


def run(items):
    t = SRC.read_text(encoding="utf-8")
    fails = 0
    for x in items:
        fx = x.get("fix")
        if not fx:
            continue
        s, e = locate(t, x["page"])
        seg = t[s:e]
        if seg.count(fx["old"]) != 1:
            fails += 1
            print("  FAIL p.", x["page"], seg.count(fx["old"]), repr(fx["old"][:60]))
            continue
        t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    return t, fails


items = json.load(open(FIND, encoding="utf-8"))
t1, f1 = run(items)
print("file order: fails", f1)
t2, f2 = run(list(reversed(items)))
print("reverse order: fails", f2, "| same result:", t1 == t2)
i = t1.find("\\end{theorem}")
print(repr(t1[i:i + 90]))
i = t1.find("l'on a un diagramme\ncommutatif")
print(repr(t1[i:i + 60]))
print("markers 24-30:", [m.group(1) for m in marker.finditer(t1) if 24 <= int(m.group(1)) <= 30])
