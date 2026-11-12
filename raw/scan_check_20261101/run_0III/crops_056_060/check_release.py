import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["0_III"]
part = "0\\textsubscript{III}"
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
F = json.load(open(E / "run_0III" / "findings_056_060.json", encoding="utf-8"))

texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv["files"]}


def locate(page):
    for f, t in texts.items():
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    return None, None, None


segs = {}
bad = 0
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    p = x["page"]
    if p not in segs:
        f, s, e = locate(p)
        segs[p] = texts[f][s:e]
    seg = segs[p]
    n = seg.count(fx["old"])
    if n != 1:
        bad += 1
        print("segment count", n, p, repr(fx["old"][:70]))
    else:
        segs[p] = seg.replace(fx["old"], fx["new"])
# compare page files with release segments
for p in sorted(segs):
    f, s, e = locate(p)
    seg = texts[f][s:e]
    pf = (E / "run_0III" / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    body = pf.split("\n", 1)[1]
    print(p, "page file == release segment:", body.rstrip("\n") == seg.rstrip("\n"))
print("bad", bad)
