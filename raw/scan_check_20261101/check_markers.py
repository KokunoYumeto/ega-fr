"""Check that every page marker \\oldpage[PART]{N}, FIRST <= N <= LAST, occurs exactly once in both editions.
PART is given without backslashes as in the queue keys: 0_IV-1 means 0\\textsubscript{IV-1}; III, IV-2 are literal.
usage: python -I check_markers.py PART FIRST LAST"""
import collections
import pathlib
import re
import sys

part, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
if part.startswith("0_"):
    part = "0\\textsubscript{" + part[2:] + "}"
R = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20")
pat = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")
for ed in ("diplomatic", "current"):
    c = collections.Counter()
    for f in sorted((R / ed / "packages").rglob("*.tex")):
        if "direct" in f.parts or f.name.startswith("EGA_") or f.name.startswith("stub"):
            continue
        for m in pat.finditer(f.read_text(encoding="utf-8")):
            c[int(m.group(1))] += 1
    bad = [(n, c[n]) for n in range(first, last + 1) if c[n] != 1]
    print(ed, f"{part} pages {first}-{last} not exactly once:", bad or "none")
