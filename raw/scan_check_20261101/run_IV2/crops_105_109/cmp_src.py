import difflib
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex").read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(src)]
for p in range(105, 110):
    i = [k for k, (n, s) in enumerate(cuts) if n == p][0]
    seg = src[cuts[i][1]:cuts[i + 1][1]]
    pg = (E / "run_IV2" / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    body = pg.split("\n", 1)[1]
    print(p, "identical" if body == seg else "DIFF", len(body), len(seg))
    if body != seg:
        for line in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm="", n=0):
            print("   ", line[:160])
