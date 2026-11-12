"""Compare page_145..149.tex with the current source segments of ega4-18-fr.tex (read-only)."""
import difflib
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-18-fr.tex")
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]
for n in range(145, 150):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    first, rest = t.split("\n", 1)
    same = rest.rstrip("\n") == seg[n].rstrip("\n")
    print(f"page {n}: {first!r} identical to current segment: {same}")
    if not same:
        for line in difflib.unified_diff(seg[n].splitlines(), rest.splitlines(), lineterm="", n=0):
            print("   ", line[:300])
