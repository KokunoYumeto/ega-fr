"""ink.py PAGE STRIP X0 Y0 X1 Y1 [THRESH]: dark-pixel count and column profile of a region."""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
im = Image.open(here.parent / f"page_{int(page):03d}_s{strip}.png").convert("L")
x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
c = im.crop((x0, y0, x1, y1))
w, h = c.size
px = c.load()
cols = [sum(1 for y in range(h) if px[x, y] < th) for x in range(w)]
print("total dark", sum(cols))
# segments of non-empty columns
segs, start = [], None
for i, v in enumerate(cols + [0]):
    if v and start is None: start = i
    if not v and start is not None: segs.append((x0 + start, x0 + i - 1, sum(cols[start:i]))); start = None
print(segs)
