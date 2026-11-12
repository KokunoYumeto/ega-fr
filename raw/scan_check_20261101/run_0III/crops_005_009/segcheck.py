"""segcheck.py: compare page_NNN.tex (pp. 5-9) with the r20 release segments of ega3-1-fr.tex."""
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
R = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex"
t = R.read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[0\\textsubscript\{III\}\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(t)]
for i, (n, s) in enumerate(cuts):
    if n > 10:
        break
    e = cuts[i + 1][1]
    seg = t[s:e]
    p = (E / "run_0III" / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    body = p.split("\n", 1)[1]
    if body == seg:
        st = "page file == segment"
    elif body.startswith(seg):
        st = "page file = segment + continuation"
    else:
        k = next((j for j in range(min(len(body), len(seg))) if body[j] != seg[j]), None)
        st = f"DIFFERENT at {k}: {body[k-40:k+40]!r} vs {seg[k-40:k+40]!r}"
    print(n, st, len(seg), len(body))
