"""Compare run_IV2 page_N.tex (165-170) with the current release source segments (read-only)."""
import difflib
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
SRC = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
src = SRC.read_text(encoding="utf-8")
marks = [(int(x.group(1)), x.start()) for x in re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", src)]
seg = {}
for i, (n, s) in enumerate(marks):
    e = marks[i + 1][1] if i + 1 < len(marks) else len(src)
    seg.setdefault(n, src[s:e])
for n in range(165, 171):
    p = (E / "run_IV2" / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = p.split("\n", 1)[1]
    same = body == seg[n]
    print(n, same, len(body), len(seg[n]))
    if not same:
        for l in difflib.unified_diff(seg[n].splitlines(), body.splitlines(), lineterm="", n=0):
            print(l)
