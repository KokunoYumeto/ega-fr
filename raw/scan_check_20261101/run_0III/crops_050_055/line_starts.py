"""Print the left ink edge of each text line of a strip image (to see paragraph indents).
usage: python line_starts.py IN.png"""
import sys

from PIL import Image

im = Image.open(sys.argv[1]).convert("L")
w, h = im.size
px = im.load()
rows = []
for y in range(h):
    xs = [x for x in range(0, w, 1) if px[x, y] < 110]
    rows.append(min(xs) if xs else None)
# group consecutive inked rows into lines
y = 0
while y < h:
    if rows[y] is None:
        y += 1
        continue
    y0 = y
    while y < h and rows[y] is not None:
        y += 1
    if y - y0 >= 12:
        print(f"rows {y0:4d}-{y:4d}  left edge {min(r for r in rows[y0:y]):5d}")
