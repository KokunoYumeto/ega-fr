"""Compare the current release segments of pp. 275-279 (ega4-21b-fr.tex) with the page_NNN.tex copies."""
import difflib
import pathlib
import re
import sys

D = pathlib.Path(__file__).resolve().parent
R = D.parent
SRC = (R.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages" / "IV4" / "native"
       / "ega4" / "ega4-21b-fr.tex")
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
out = sys.stdout.buffer
for p in range(275, 280):
    page = (R / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n", 1)[1]
    cur = seg[p]
    out.write(f"page {p}: identical={page == cur}\n".encode("utf-8"))
    if page != cur:
        for l in difflib.unified_diff(page.split("\n"), cur.split("\n"), "page_file", "current", lineterm="", n=1):
            out.write((l + "\n").encode("utf-8"))
