"""Apply findings_200_205.json in memory (apply_fixes.py page-segment logic) and write the resulting page segments
200-205 to crops_200_205/simulated_200_205.txt for reading. Release files are not modified."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
E = RUN.parent
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def locate(page):
    for f in inv:
        t = texts[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for j, (n, st) in enumerate(cuts):
            if n == page:
                return f, st, cuts[j + 1][1] if j + 1 < len(cuts) else len(t)
    return None, None, None


for x in json.load(open(RUN / "findings_200_205.json", encoding="utf-8")):
    if not x.get("fix"):
        continue
    f, st, en = locate(int(x["page"]))
    seg = texts[f][st:en]
    assert seg.count(x["fix"]["old"]) == 1, x
    texts[f] = texts[f][:st] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + texts[f][en:]

out = []
for p in (200, 201, 202, 203, 205):
    f, st, en = locate(p)
    out.append(f"===== page {p} ({pathlib.Path(f).name})\n" + texts[f][st:en])
(RUN / "crops_200_205" / "simulated_200_205.txt").write_text("\n".join(out), encoding="utf-8")
print("ok")
