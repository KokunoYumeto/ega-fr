import pathlib
import re

BASE = pathlib.Path(r"user/Documents/ega_scan_check_20261101")
for ed in ("diplomatic", "current"):
    src = (BASE / "ega-fr/editions/2026-10-24-r20" / ed / "packages/IV3/native/ega4/ega4-15-terminal-fr.tex").read_text(encoding="utf-8")
    m = list(re.finditer(r"\\oldpage\[IV-3\]\{(\d+)\}", src))
    seg = {}
    for i, x in enumerate(m):
        end = m[i + 1].start() if i + 1 < len(m) else len(src)
        seg[int(x.group(1))] = src[x.start():end]
    for n in range(245, 250):
        p = (BASE / f"run_IV3/page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        body = p.split("\n", 1)[1]
        print(ed, n, body == seg.get(n), len(body), len(seg.get(n, "")))
