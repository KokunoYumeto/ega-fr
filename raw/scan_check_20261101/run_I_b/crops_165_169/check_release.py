"""Read-only: count each fix.old (CRLF->LF) in the release page segment that apply_fixes.py would use,
and, for p. 169, in the ega1-9 continuation before \\oldpage[I]{170}."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
files = inv["I"]["files"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def locate(page):
    for f in files:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return pathlib.Path(f), t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    return None, None


cont = None
for f in files:
    if pathlib.Path(f).name == "ega1-9-fr.tex":
        t = pathlib.Path(f).read_text(encoding="utf-8")
        m = marker.search(t)
        cont = (f, t[:m.start()])
print("files with ega1-8/9:", [f for f in files if "ega1-8" in f or "ega1-9" in f])
F = json.load(open(E / "run_I_b" / "findings_165_169.json", encoding="utf-8"))
auto = manual = 0
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    old = fx["old"].replace("\r\n", "\n")
    path, seg = locate(x["page"])
    n = seg.count(old) if seg is not None else -1
    c = cont[1].count(old) if (cont and x["page"] == 169) else 0
    status = "auto" if n == 1 else "manual"
    auto += status == "auto"
    manual += status == "manual"
    print(x["page"], status, "seg", n, "cont", c, "|", old[:60].replace("\n", "\\n"))
print("auto", auto, "manual", manual)
