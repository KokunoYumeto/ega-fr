import json
import pathlib
import re

# Check every fix of findings_155_159.json against the CURRENT release segment of its page (LF), as apply_fixes.py does,
# and simulate applying all edits in order to make sure none breaks another.
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["IV-3"]
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv["files"]}


def segment(texts, page):
    for f, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None, None


F = json.load(open(E / "run_IV3" / "findings_155_159.json", encoding="utf-8"))
ok = bad = 0
for x in F:
    fx = x.get("fix")
    if not fx:
        continue
    f, s, e = segment(texts, x["page"])
    seg = texts[f][s:e]
    n = seg.count(fx["old"])
    if n != 1:
        bad += 1
        print("FAIL", x["page"], n, repr(fx["old"][:70]))
        continue
    texts[f] = texts[f][:s] + seg.replace(fx["old"], fx["new"]) + texts[f][e:]
    ok += 1
print("applied in simulation", ok, "failed", bad)
