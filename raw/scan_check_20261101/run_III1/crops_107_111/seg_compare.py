"""Compare page_NNN.tex (pages 107-111) with the current release-file segments (read only)."""
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
rel = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega3/ega3-1-fr.tex"
t = rel.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in marker.finditer(t)]
for p in range(107, 112):
    idx = [i for i, (n, s) in enumerate(cuts) if n == p]
    i = idx[0]
    s = cuts[i][1]
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(t)
    seg = t[s:e]
    pg = (E / f"run_III1/page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = pg.split("\n", 1)[1]
    print(p, "markers:", len(idx), "identical:", seg == body, "strip-identical:", seg.strip() == body.strip(),
          len(seg), len(body))
