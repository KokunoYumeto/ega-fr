"""v2runs.py PAGE STRIP x0 y0 x1 y1 [THRESH]
Print, for each row of the box (original pixel coordinates of run_IV4/page_PAGE_sSTRIP.png), the lengths of the
dark runs (< THRESH): a rough stroke-width profile of a glyph."""
import sys
import pathlib
from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
page, strip = int(sys.argv[1]), sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
for y in range(h):
    runs, run = [], 0
    line = ""
    for x in range(w):
        d = px[x, y] < th
        line += "#" if d else "."
        if d:
            run += 1
        elif run:
            runs.append(run)
            run = 0
    if run:
        runs.append(run)
    print(f"{y:3d} {line} {runs}")
