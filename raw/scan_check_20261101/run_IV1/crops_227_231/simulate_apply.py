"""Read-only simulation of apply_fixes.py on in-memory copies of the release files (nothing is written)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
part = "IV-1"
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
key = part
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


L = json.load(open(E / "run_IV1" / "findings_227_231.json", encoding="utf-8"))
applied = manual = 0
for x in L:
    fix = x.get("fix")
    if not fix:
        continue
    f, s, e = locate(int(x["page"]))
    if f is None:
        print("page not found", x["page"]); manual += 1; continue
    t = texts[f]
    seg = t[s:e]
    c = seg.count(fix["old"])
    if c != 1:
        print("MANUAL", x["page"], c, repr(fix["old"])); manual += 1; continue
    texts[f] = t[:s] + seg.replace(fix["old"], fix["new"]) + t[e:]
    applied += 1
print("applied", applied, "manual", manual)
for f in files:
    if "ega4-1-fr" in f:
        t = texts[f]
        i = t.find("\\oldpage[IV-1]{227}")
        print(t[i - 420:i + 120])
        print("count 227 markers:", t.count("\\oldpage[IV-1]{227}"))
