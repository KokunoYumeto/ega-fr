import pathlib
import re

base = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
src = (base / "ega-fr/source/ega4/ega4-10-fr.tex").read_text(encoding="utf-8")
m = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
cuts = [(int(x.group(1)), x.start()) for x in m.finditer(src)]
ns = [n for n, _ in cuts]
pos = dict(cuts)
for n in range(105, 110):
    i = ns.index(n)
    seg = src[pos[n]:cuts[i + 1][1]]
    pg = (base / f"run_IV3/page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    body = pg.split("\n", 1)[1]
    print(n, "identical" if body == seg else "DIFFERENT", len(body), len(seg))
