"""Compare page_NNN.tex (prepared 1 Nov) with the CURRENT source segments for pages 325-329."""
import pathlib
import re
import difflib

R = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
SRC = R / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21c-fr.tex"
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
for page in range(325, 330):
    for i, (n, s) in enumerate(cuts):
        if n == page:
            e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
            seg = t[s:e]
    p = (R / "run_IV4" / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = p.split("\n")
    body = "\n".join(lines[1:])
    if seg == body:
        print(page, "identical")
    else:
        print(page, "DIFFERENT")
        for l in difflib.unified_diff(body.split("\n"), seg.split("\n"), "page", "current", lineterm="", n=1):
            print("   ", l)
