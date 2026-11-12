"""Stroke weight of the ink inside a box: python stroke.py PAGE STRIP X0 Y0 X1 Y1 [THRESH]
Prints the number of dark pixels, the median and mean width of horizontal dark runs (runs of 1..14 px),
and an ASCII picture of the box so the glyph can be identified."""
import pathlib
import statistics
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
px = im.load()
runs, dark = [], 0
for y in range(y0, y1):
    x = x0
    while x < x1:
        if px[x, y] < th:
            s = x
            while x < x1 and px[x, y] < th:
                x += 1
            dark += x - s
            if x - s <= 14:
                runs.append(x - s)
        x += 1
print("dark", dark, "median run", statistics.median(runs) if runs else None,
      "mean run", round(statistics.mean(runs), 2) if runs else None)
for y in range(y0, y1):
    print("".join("#" if px[x, y] < th else ("+" if px[x, y] < 200 else ".") for x in range(x0, x1)))
