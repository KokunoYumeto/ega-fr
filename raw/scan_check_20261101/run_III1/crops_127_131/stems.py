import sys
from PIL import Image

# usage: stems.py src x0 y0 x1 y1 label
# For a box around one capital I, print the dark-pixel count and the median run width of dark pixels per row
# (stem thickness), and save a 6x preview next to this script.
src, x0, y0, x1, y1, label = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = 0
widths = []
for y in range(h):
    row = [px[x, y] < 128 for x in range(w)]
    dark += sum(row)
    best = run = 0
    for v in row:
        run = run + 1 if v else 0
        best = max(best, run)
    if best:
        widths.append(best)
widths.sort()
med = widths[len(widths) // 2] if widths else 0
im.resize((w * 6, h * 6), Image.NEAREST).save(
    rf"user\Documents\ega_scan_check_20261101\run_III1\crops_127_131\stem_{label}.png")
print(label, "dark", dark, "median longest run per row", med, "rows", len(widths))
