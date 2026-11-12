"""Compare run_IV4/page_NNN.tex (305-309) with the current source segments of ega4-21c-fr.tex."""
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
SRC = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21c-fr.tex"
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in marker.finditer(src)]
for i, (n, s) in enumerate(cuts):
    if 305 <= n <= 309:
        e = cuts[i + 1][1]
        seg = src[s:e]
        raw = (E / f"run_IV4/page_{n}.tex").read_bytes()
        txt = raw.decode("utf-8").replace("\r\n", "\n")
        body = txt.split("\n", 1)[1]
        print(n, "CRLF" if b"\r\n" in raw else "LF", "equal" if body.rstrip() == seg.rstrip() else "DIFF",
              len(body), len(seg))
