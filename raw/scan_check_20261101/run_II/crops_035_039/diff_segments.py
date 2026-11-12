"""Compare the page_NNN.tex snapshots with the current release-file segments (read only)."""
import difflib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
t = pathlib.Path(inv[0]).read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
for i, (n, s) in enumerate(cuts):
    if 35 <= n <= 39:
        seg = t[s:cuts[i + 1][1]]
        snap = (E / "run_II" / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        snap = snap.split("\n", 1)[1]  # drop the '% from ...' line
        d = list(difflib.unified_diff(snap.splitlines(), seg.splitlines(), lineterm="", n=0))
        print(f"p.{n}: {'identical' if not d else 'DIFFERS'}")
        for line in d[:20]:
            print("   ", line)
