"""Count 'Cohen--Macaulay' per printed page in the current ega4-2-fr.tex (read-only)."""
import collections
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
t = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", t)]
c = collections.Counter()
for m in re.finditer("Cohen--Macaulay", t):
    page = max((n for n, s in cuts if s <= m.start()), default=0)
    c[page] += 1
print(sum(c.values()), dict(sorted(c.items())))
