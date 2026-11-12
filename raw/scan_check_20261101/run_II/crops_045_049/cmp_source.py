"""Compare run_II/page_NNN.tex (pages 45-49) with the same segments of the current release source (read-only)."""
import difflib
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega2/ega2-1-fr.tex").read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in marker.finditer(src)]
for i, (n, s) in enumerate(cuts):
    if 44 <= n <= 50:
        seg = src[s:cuts[i + 1][1]]
        pg = (E / f"run_II/page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        body = pg.split("\n", 1)[1]
        body = body.split("% (continued in")[0]
        print(n, "identical" if body == seg else "DIFFERS", len(body), len(seg))
        if body != seg:
            for line in difflib.unified_diff(body.splitlines(), seg.splitlines(), lineterm="", n=0):
                print("   ", line[:170])
