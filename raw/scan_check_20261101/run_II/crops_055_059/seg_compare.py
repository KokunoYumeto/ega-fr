"""Compare run_II/page_NNN.tex (CRLF copies) with the current segments of the diplomatic release file.
usage: python seg_compare.py FIRST LAST"""
import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
F = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex"
first, last = int(sys.argv[1]), int(sys.argv[2])
t = F.read_text(encoding="utf-8")
ms = list(re.finditer(r"\\oldpage\[II\]\{(\d+)\}", t))
for i, m in enumerate(ms):
    p = int(m.group(1))
    if not first <= p <= last:
        continue
    seg = t[m.start(): ms[i + 1].start() if i + 1 < len(ms) else len(t)]
    pf = E / "run_II" / f"page_{p:03d}.tex"
    body = pf.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n", 1)[1]
    print(p, "same" if body == seg else "DIFF", len(body), len(seg))
