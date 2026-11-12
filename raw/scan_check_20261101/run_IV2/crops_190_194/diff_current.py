import difflib
import re

base = r"user\Documents\ega_scan_check_20261101"
cur = base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
t = open(cur, encoding="utf-8").read().replace("\r\n", "\n")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", t)]
for page in range(189, 196):
    idx = [k for k, (n, s) in enumerate(cuts) if n == page]
    if not idx:
        print("no marker", page)
        continue
    i = idx[0]
    s, e = cuts[i][1], (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
    seg = t[s:e]
    try:
        p = open(base + r"\run_IV2\page_%03d.tex" % page, encoding="utf-8").read().replace("\r\n", "\n")
    except FileNotFoundError:
        continue
    p = p.split("\n", 1)[1]  # drop the '% from' line
    if p == seg:
        print(page, "identical")
    else:
        print(page, "DIFFERS")
        for line in difflib.unified_diff(p.split("\n"), seg.split("\n"), "page_file", "current_r20", lineterm="", n=1):
            print("   ", line)
