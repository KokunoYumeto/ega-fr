import difflib
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
segs = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    segs[n] = t[s:e]
for p in range(144, 151):
    page = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    page = page.split("\n", 1)[1]  # drop the '% from' line
    rel = segs.get(p)
    if rel is None:
        print(p, "no segment in ega4-11")
        continue
    if rel == page:
        print(p, "identical")
    else:
        print(p, "DIFFERS")
        for line in difflib.unified_diff(page.splitlines(), rel.splitlines(), "page_copy", "release", lineterm="", n=0):
            print("   ", line)
