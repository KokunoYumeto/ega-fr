"""Simulate apply_fixes.py sequentially in memory (no file is written) and report every entry that would go to manual.

usage: python simulate_apply.py PART FINDINGS.json
"""
import json
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
part, fn = sys.argv[1], sys.argv[2]
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
key = part.replace("\\textsubscript{", "_").replace("}", "")
files = inv[key]["files"]
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in files}
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")


def locate(page):
    for f in files:
        t = texts[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                j = i + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return f, s, cuts[j][1] if j < len(cuts) else len(t)
    for f in files:
        t = texts[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
            if a < page < b:
                return f, sa, sb
    return None, None, None


ok = 0
for i, x in enumerate(json.load(open(fn, encoding="utf-8"))):
    fix = x.get("fix")
    if not fix or not fix.get("old") or fix.get("old") == fix.get("new"):
        continue
    page = int(x["page"])
    f, s, e = locate(page)
    if f is None:
        print(i, page, "page not found", repr(fix["old"])[:60]); continue
    seg = texts[f][s:e]
    c = seg.count(fix["old"])
    if c != 1:
        print(i, page, f"old occurs {c} times", repr(fix["old"])[:60], "| segment starts", repr(seg[:40]))
        continue
    texts[f] = texts[f][:s] + seg.replace(fix["old"], fix["new"]) + texts[f][e:]
    ok += 1
print("applied", ok)
# show the result around the moved markers
for f in files:
    t = texts[f]
    for n in (224, 225, 226, 227):
        for m in re.finditer(r"\\oldpage\[IV-1\]\{%d\}" % n, t):
            print("---", n, repr(t[max(0, m.start() - 70):m.end() + 50]))
