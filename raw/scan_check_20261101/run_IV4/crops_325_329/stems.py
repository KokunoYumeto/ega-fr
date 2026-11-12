"""stems.py PAGE STRIP x0 y0 x1 y1 [THRESH]: print, for each row band, the dark-run widths (vertical stems) in a box.
Reports the median width of horizontal dark runs across the rows of the box (a rough stem-weight measure)."""
import sys
import statistics
from PIL import Image
import pathlib

here = pathlib.Path(__file__).resolve().parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(here.parent / f"page_{page:03d}_s{strip}.png").convert("L")
px = im.load()
runs = []
for y in range(y0, y1):
    r = 0
    for x in range(x0, x1 + 1):
        dark = x < x1 and px[x, y] < th
        if dark:
            r += 1
        elif r:
            runs.append(r)
            r = 0
ink = sum(1 for y in range(y0, y1) for x in range(x0, x1) if px[x, y] < th)
print(f"runs={len(runs)} median={statistics.median(runs) if runs else 0} mean={statistics.mean(runs) if runs else 0:.2f} "
      f"ink={ink} area={(x1-x0)*(y1-y0)} ink%={100*ink/((x1-x0)*(y1-y0)):.1f}")
