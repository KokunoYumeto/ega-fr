import sys
from PIL import Image
import numpy as np
# usage: margins.py <page> <strip> ; prints, for each text line band, the leftmost and rightmost dark pixel
page, strip = sys.argv[1], sys.argv[2]
base = r"user\Documents\ega_scan_check_20261101\run_IV3"
im = np.array(Image.open(rf"{base}\page_{int(page):03d}_s{strip}.png").convert("L"))
dark = im < 128
rows = dark.sum(axis=1)
# find line bands
bands = []
inb = False
for y, c in enumerate(rows):
    if c > 3 and not inb:
        inb = True; y0 = y
    elif c <= 3 and inb:
        inb = False; bands.append((y0, y))
if inb: bands.append((y0, len(rows)))
for y0, y1 in bands:
    if y1 - y0 < 8: continue
    cols = np.where(dark[y0:y1].any(axis=0))[0]
    print(f"y {y0}-{y1}: x {cols.min()}..{cols.max()}")
