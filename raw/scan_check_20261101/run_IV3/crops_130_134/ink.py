"""Measure ink of glyph regions: dark pixel count and horizontal stem run widths.
usage: python ink.py PAGE STRIP x0 y0 x1 y1 [threshold]"""
import sys
from PIL import Image
page, strip, x0, y0, x1, y1 = sys.argv[1:7]
th = int(sys.argv[7]) if len(sys.argv) > 7 else 128
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L")
c = im.crop((int(x0), int(y0), int(x1), int(y1)))
w, h = c.size
px = c.load()
dark = sum(1 for y in range(h) for x in range(w) if px[x, y] < th)
runs = []
for y in range(h):
    r = 0; best = 0
    for x in range(w):
        if px[x, y] < th:
            r += 1; best = max(best, r)
        else:
            r = 0
    runs.append(best)
nz = [r for r in runs if r > 0]
nz.sort()
print("dark", dark, "rows", len(nz), "median run", nz[len(nz)//2] if nz else 0, "max run", max(nz) if nz else 0)
