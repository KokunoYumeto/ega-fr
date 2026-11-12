"""Measure glyph weight in a box of a strip (original pixel coordinates).
usage: python ink.py PAGE STRIP X0 Y0 X1 Y1 [LABEL]
Prints dark-pixel count, bbox of dark pixels and the median length of horizontal dark runs (~ stroke width)."""
import pathlib
import statistics
import sys

from PIL import Image

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
label = sys.argv[7] if len(sys.argv) > 7 else ""
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
dark = [[px[i, j] < 128 for i in range(w)] for j in range(h)]
n = sum(sum(r) for r in dark)
xs = [i for j in range(h) for i in range(w) if dark[j][i]]
ys = [j for j in range(h) for i in range(w) if dark[j][i]]
runs = []
for j in range(h):
    k = 0
    while k < w:
        if dark[j][k]:
            s = k
            while k < w and dark[j][k]:
                k += 1
            runs.append(k - s)
        else:
            k += 1
vr = []
for i in range(w):
    k = 0
    while k < h:
        if dark[k][i]:
            s = k
            while k < h and dark[k][i]:
                k += 1
            vr.append(k - s)
        else:
            k += 1
print(label, "dark", n, "bbox", (min(xs), min(ys), max(xs), max(ys)) if xs else None,
      "median hrun", statistics.median(runs) if runs else None,
      "median vrun", statistics.median(vr) if vr else None)
