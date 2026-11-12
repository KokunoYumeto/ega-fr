"""Dark-run widths along one row of a strip: python runs.py PAGE STRIP Y X0 X1 [THRESH]
Prints (start_x, width) of each run of pixels darker than THRESH (default 128)."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
page, strip, y, x0, x1 = (int(a) for a in sys.argv[1:6])
th = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
runs = []
start = None
for x in range(x0, x1):
    d = im.getpixel((x, y)) < th
    if d and start is None:
        start = x
    if not d and start is not None:
        runs.append((start, x - start))
        start = None
if start is not None:
    runs.append((start, x1 - start))
print(runs)
