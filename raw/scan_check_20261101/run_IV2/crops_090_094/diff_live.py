"""Read-only: compare the live release segments of pp. 89-95 with the page_NNN.tex snapshots."""
import difflib
import pathlib
import re

run = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
src = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV2\native\ega4\ega4-2-fr.tex")
t = src.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
for p in range(89, 96):
    snap = (run / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    snap = snap.split("\n", 1)[1]  # drop the '% from' line
    live = seg.get(p, "")
    d = list(difflib.unified_diff(snap.splitlines(), live.splitlines(), lineterm="", n=0))
    print(f"=== p{p}: {len(d)} diff lines")
    for line in d[:40]:
        print(line)
