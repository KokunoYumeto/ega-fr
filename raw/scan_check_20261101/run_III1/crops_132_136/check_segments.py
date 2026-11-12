"""Compare page_NNN.tex copies with the release segments (from \\oldpage[III]{N} to the next marker)."""
import re
import pathlib

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
rel = (E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/BASE/native/ega3/ega3-1-fr.tex").read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[III\]\{(\d+)\}")
cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(rel)]
for N in range(131, 138):
    idx = [i for i, (n, s) in enumerate(cuts) if n == N]
    if not idx:
        print(N, "no marker")
        continue
    i = idx[0]
    s = cuts[i][1]
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)
    seg = rel[s:e]
    p = E / f"run_III1/page_{N:03d}.tex"
    if p.exists():
        t = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        t = t.split("\n", 1)[1]
        print(N, "equal" if t == seg else f"DIFF len {len(t)} vs {len(seg)}", "CR in release" if "\r" in seg else "", len(idx))
