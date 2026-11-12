"""Show how the current release segment for IV-1 p. 226 differs from run_IV1/page_226.tex (read only)."""
import difflib
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
S = E / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV1" / "native" / "ega4" / "ega4-1-fr.tex"
t = S.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-1\]\{(\d+)\}", t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    seg.setdefault(n, t[s:e])
for n in (222, 223, 224, 225, 226):
    old = (E / "run_IV1" / f"page_{n:03d}.tex").read_text(encoding="utf-8").split("\n", 1)[1]
    d = list(difflib.unified_diff(old.splitlines(), seg[n].splitlines(), lineterm="", n=0))
    print(f"== page {n}: {len(d)} diff lines")
    for line in d:
        print(line)
