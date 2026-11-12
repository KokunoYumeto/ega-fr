"""Read-only: replay the fixes of findings_180_184.json on in-memory copies of the source page segments
(same page location rule as apply_fixes.py) and report which ones would go to the manual list."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv["I"]["files"]}


def locate(page):
    for f, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None, None


L = json.load(open(E / "run_I_b" / "findings_180_184.json", encoding="utf-8"))
for i, x in enumerate(L):
    fx = x.get("fix")
    if not fx:
        continue
    f, s, e = locate(int(x["page"]))
    t = texts[f]
    seg = t[s:e]
    c = seg.count(fx["old"])
    if c != 1:
        print("MANUAL", i, x["page"], pathlib.Path(f).name, "count", c, "|", x["where"][:70])
        continue
    texts[f] = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("done")
