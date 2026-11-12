import difflib
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
t = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
for i, (n, s) in enumerate(cuts):
    if 125 <= n <= 129:
        e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
        seg = t[s:e]
        p = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        p = p.split("\n", 1)[1]  # drop the '% from' line
        if seg == p:
            print(n, "identical")
        else:
            print(n, "DIFFERENT")
            for line in difflib.unified_diff(p.split("\n"), seg.split("\n"), "page_tex", "release", lineterm="", n=1):
                print("   ", line)
