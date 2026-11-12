import re
import pathlib
import sys

p = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-9-fr.tex")
t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
mk = re.compile(r"\n\n(\\oldpage\[IV-3\]\{(\d+)\})\n\n")
allm = len(re.findall(r"\\oldpage\[IV-3\]", t))
tot = 0
hits = []
for m in mk.finditer(t):
    tot += 1
    before = t[:m.start()].rstrip()
    if not re.search(r"([.:]|\\end\{[a-z*]+\}|\\\]|C\.Q\.F\.D\.)\s*$", before):
        hits.append((m.group(2), before[-45:].replace("\n", " ")))
sys.stdout.reconfigure(encoding="utf-8")
print("markers", allm, "| blank lines on both sides", tot, "| of which after no sentence end", len(hits))
for h in hits:
    print(h)
