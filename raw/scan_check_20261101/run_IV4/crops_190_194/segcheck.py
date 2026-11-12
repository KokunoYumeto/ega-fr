"""Compare page_NNN.tex (CRLF normalized) with the current source segments of ega4-18-fr.tex."""
import difflib
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
src = SRC.read_bytes().decode("utf-8")
print("CRLF in source:", "\r\n" in src)
marks = {int(m.group(1)): m.start() for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", src)}
for p in range(189, 195):
    seg = src[marks[p]:marks[p + 1]]
    pg = (RUN / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    body = pg.split("\n", 1)[1]
    print(p, "same" if body == seg else "DIFF", len(body), len(seg))
    if body != seg:
        for line in difflib.unified_diff(body.split("\n"), seg.split("\n"), lineterm="", n=0):
            print("   ", line[:300])
