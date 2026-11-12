import difflib
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega3\ega3-6-fr.tex")
rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[III\]\{(\d+)\}", rel)]
for n in range(147, 152):
    t = (RUN / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = t.split("\n", 1)[1]
    seg = None
    for i, (p, s) in enumerate(cuts):
        if p == n:
            seg = rel[s:cuts[i + 1][1]]
    print(n, body == seg, len(body), len(seg))
    if body != seg:
        for line in list(difflib.unified_diff(seg.splitlines(), body.splitlines(), lineterm=""))[:20]:
            print(line)
