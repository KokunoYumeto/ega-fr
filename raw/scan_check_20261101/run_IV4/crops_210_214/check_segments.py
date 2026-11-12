"""Compare the current source segments of pp. 210-214 with the prepared page_NNN.tex files (read-only)."""
import re

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
t = open(SRC, encoding="utf-8").read()
marks = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", t)]
pos = dict(marks)
order = [n for n, _ in marks]
for p in range(209, 215):
    s = pos[p]
    e = pos[order[order.index(p) + 1]]
    seg = t[s:e]
    if p == 209:
        print("209 segment tail:", repr(seg[-90:]))
        continue
    pt = open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    body = pt.split("\n", 1)[1]
    print(p, "same" if body == seg else "DIFFERENT", len(body), len(seg))
