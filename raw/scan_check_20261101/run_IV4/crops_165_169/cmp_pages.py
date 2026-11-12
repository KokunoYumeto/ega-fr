"""Compare the prepared page_NNN.tex files (165-169) with the current source segments."""
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    seg[n] = t[s:e]
for p in range(165, 170):
    pt = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pt.split("\n", 1)[1]  # drop the '% from' line
    s = seg[p]
    print(p, "page file len", len(body), "segment len", len(s), "equal:", body.rstrip("\n") == s.rstrip("\n"))
    if body.rstrip("\n") != s.rstrip("\n"):
        import difflib
        for l in difflib.unified_diff(s.splitlines(), body.splitlines(), lineterm="", n=0):
            print("   ", l[:300])
