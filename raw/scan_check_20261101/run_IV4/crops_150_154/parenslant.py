"""Estimate the slant of a parenthesis glyph inside a box: x of the ink centre per row."""
import sys
from PIL import Image
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
im = Image.open(RUN + rf"\page_{page:03d}_s{strip}.png").convert("L")
rows = []
for y in range(y0, y1):
    xs = [x for x in range(x0, x1) if im.getpixel((x, y)) < 110]
    if xs:
        rows.append((y, min(xs), max(xs)))
for r in rows:
    print(r[0], r[1] - x0, r[2] - x0, "#" * 0)
if rows:
    print("top", rows[0], "bottom", rows[-1], "height", rows[-1][0] - rows[0][0])
