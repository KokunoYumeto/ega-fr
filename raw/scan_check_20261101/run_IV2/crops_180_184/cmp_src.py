"""Compare run_IV2 page_180..184.tex with the matching segments of the current diplomatic ega4-2-fr.tex (read only)."""
import difflib
import pathlib
import re

base = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (base / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex").read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in mk.finditer(src)]
for i, (n, s) in enumerate(cuts):
    if 180 <= n <= 184:
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(src)
        seg = "% from ega4-2-fr.tex\n" + src[s:e]
        pg = (base / rf"run_IV2\page_{n:03d}.tex").read_text(encoding="utf-8")
        print(n, "same" if seg == pg else "DIFFERENT")
        if seg != pg:
            for line in difflib.unified_diff(pg.splitlines(), seg.splitlines(), lineterm="", n=0):
                print("   ", line)
