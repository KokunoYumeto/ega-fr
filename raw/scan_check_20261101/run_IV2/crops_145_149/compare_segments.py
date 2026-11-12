"""Compare page_NNN.tex (pages 145-149) with the current segments of the release file."""
import re
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
REL = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
t = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", t)]
for page in range(145, 150):
    i = [k for k, (n, s) in enumerate(cuts) if n == page][0]
    seg = t[cuts[i][1]:cuts[i + 1][1]]
    pf = (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pf.split("\n", 1)[1]
    print(page, "identical" if body == seg else "DIFFERENT", len(body), len(seg), repr(pf[-30:]))
