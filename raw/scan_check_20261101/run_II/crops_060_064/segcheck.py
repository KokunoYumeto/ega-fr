import re
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
F = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
t = F.read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(t)]
d = {n: (s, cuts[i + 1][1] if i + 1 < len(cuts) else len(t)) for i, (n, s) in enumerate(cuts)}
for p in range(60, 66):
    s, e = d[p]
    seg = t[s:e]
    if p < 65:
        raw = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8")
        crlf = raw.count("\r\n")
        pg = raw.replace("\r\n", "\n")
        body = pg.split("\n", 1)[1]
        print(p, "crlf", crlf, "same" if body == seg else "DIFF", len(body), len(seg), repr(seg[-50:]))
    else:
        print(p, repr(seg[:160]))
