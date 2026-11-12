import difflib
import pathlib
import re
import sys

# Compare each page_NNN.tex (minus its first comment line) with the release segment
# (from \oldpage[III]{N} to the next marker), as apply_fixes.py cuts it.
rel = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex")
t = rel.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
for p in map(int, sys.argv[1:]):
    seg = None
    for i, (n, s) in enumerate(cuts):
        if n == p:
            seg = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    pg = (run / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pg.split("\n", 1)[1]
    print(p, "segment found" if seg is not None else "NO SEGMENT", "| equal:", seg == body,
          "| len seg", len(seg or ""), "len page", len(body))
    if seg is not None and seg != body:
        for line in difflib.unified_diff(seg.splitlines(), body.splitlines(), "release", "page", lineterm="", n=1):
            print("   ", line)
