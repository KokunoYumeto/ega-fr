"""Show how quotation marks are written in the chapter 0 (IV-1) release files (read-only)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                 r"\diplomatic\packages\IV1\native\ega4")
pat = re.compile(r"\\og\b|\\fg\b|«|»|``|''")
for fn in ["ega0-15-fr.tex", "ega0-16-fr.tex", "ega0-17-fr.tex"]:
    t = (D / fn).read_text(encoding="utf-8")
    n = 0
    for m in pat.finditer(t):
        if n < 6:
            print(fn, repr(t[max(0, m.start() - 25):m.end() + 35]))
        n += 1
    print(fn, "total", n)
