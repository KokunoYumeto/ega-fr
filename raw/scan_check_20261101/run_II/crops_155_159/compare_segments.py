"""Compare run_II/page_NNN.tex (154-160) with the same page's segment of the release file apply_fixes.py edits."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
E = RUN.parent
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
for f in inv:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if 154 <= n <= 160:
            e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
            seg = t[s:e]
            pf = RUN / f"page_{n:03d}.tex"
            if not pf.exists():
                print(n, "no page file"); continue
            body = pf.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n", 1)[1]
            print(n, pathlib.Path(f).name, "same" if body == seg else "DIFF", len(seg), len(body))
