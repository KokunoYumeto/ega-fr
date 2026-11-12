import pathlib
import re
import sys

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex"
rel = REL.read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(rel)]
d = {}
for i, (n, s) in enumerate(cuts):
    e = cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)
    d[n] = rel[s:e]
for p in range(91, 96):
    t = (E / "run_0IV1" / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    body = t.split("\n", 1)[1]
    print(p, body == d[p], len(body), len(d[p]))
if len(sys.argv) > 1:
    for a in sys.argv[1:]:
        p, k = a.split(":")
        p = int(p)
        if k.startswith("head"):
            print(repr(d[p][: int(k[4:])]))
        else:
            print(repr(d[p][-int(k[4:]):]))
