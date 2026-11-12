import difflib
import re
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
REL = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
t = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", t)]
i = [k for k, (n, s) in enumerate(cuts) if n == 149][0]
seg = t[cuts[i][1]:cuts[i + 1][1]]
body = (RUN / "page_149.tex").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n", 1)[1]
for l in difflib.unified_diff(body.split("\n"), seg.split("\n"), lineterm="", n=1):
    print(repr(l))
