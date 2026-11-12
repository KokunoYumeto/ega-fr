"""Compare run_IV2 page_140..144.tex with the current release segments (read-only)."""
import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
t = src.read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(t)]
print([c for c in cuts if 139 <= c[0] <= 146])
for i, (n, s) in enumerate(cuts):
    if 140 <= n <= 144:
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        seg = t[s:e]
        pf = (E / "run_IV2" / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        body = pf.split("\n", 1)[1]
        print(n, "same" if seg == body else "DIFF", len(seg), len(body))
        if seg != body:
            for l in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm="", n=1):
                print(l)
