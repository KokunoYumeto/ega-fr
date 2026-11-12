"""Compare the page numbers of the IV-3 table of contents (pages 253-255) with the page markers in front of each
section heading in the r20 diplomatic sources. Read-only."""
import pathlib
import re

D = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
files = ["ega4-8-fr.tex", "ega4-9-fr.tex", "ega4-10-fr.tex", "ega4-11-fr.tex", "ega4-12-fr.tex", "ega4-13-fr.tex",
         "ega4-14-fr.tex", "ega4-15-fr.tex"]
marker = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
label = re.compile(r"\\label\{(sub)?section:IV\.([\d.]+)-fr\}")
start = {}
page = None
for f in files:
    for line in (D / f).read_text(encoding="utf-8").splitlines():
        for m in marker.finditer(line):
            page = int(m.group(1))
        m = label.search(line)
        if m:
            start[("" if m.group(1) else "S") + m.group(2)] = page
toc = []
for n in (253, 254, 255):
    t = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    for m in re.finditer(r"\\EGAIVthreeContentsLine\{([^{}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}\{(\d+)\}", t):
        toc.append((n, m.group(1), m.group(2)[:50], int(m.group(3))))
for n, lab, title, p in toc:
    key = None
    if lab.startswith("\\S~"):
        key = "S" + lab[3:].rstrip(".")
    elif re.fullmatch(r"[\d.]+", lab):
        key = lab.rstrip(".")
    got = start.get(key) if key else None
    flag = "" if got == p else "   <-- differs" if got is not None else "   (no label found)"
    print(f"p{n} {lab:8s} toc {p:4d} marker {got}{flag}  {title}")
