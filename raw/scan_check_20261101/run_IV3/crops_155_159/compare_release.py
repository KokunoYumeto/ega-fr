import json
import pathlib
import re
import sys

# Compare page_NNN.tex (prepared copy) with the current release segment of the same page.
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["IV-3"]
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
segs = {}
for f in inv["files"]:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    crlf = "\r\n" in t
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        segs[n] = (pathlib.Path(f).name, t[s:e], crlf)
for p in map(int, sys.argv[1:]):
    prep = (E / "run_IV3" / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    prep = prep.split("\n", 1)[1]  # drop the '% from' line
    name, seg, crlf = segs[p]
    seg = seg.replace("\r\n", "\n")
    print(p, name, "release CRLF" if crlf else "release LF", "identical" if prep == seg else "DIFFERENT",
          len(prep), len(seg))
    if prep != seg:
        import difflib
        for line in difflib.unified_diff(prep.splitlines(), seg.splitlines(), lineterm="", n=0):
            print("   ", line[:150])
