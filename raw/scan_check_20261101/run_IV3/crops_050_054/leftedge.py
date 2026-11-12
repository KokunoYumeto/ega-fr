import sys
from PIL import Image
page, strip = int(sys.argv[1]), int(sys.argv[2])
im = Image.open(rf"user\Documents\ega_scan_check_20261101\run_IV3\page_{page:03d}_s{strip}.png").convert("L")
W, H = im.size
dark = [any(im.getpixel((x, y)) < 100 for x in range(150, W - 50, 2)) for y in range(H)]
bands = []; start = None
for y, d in enumerate(dark):
    if d and start is None: start = y
    if not d and start is not None:
        bands.append((start, y - 1)); start = None
if start is not None: bands.append((start, H - 1))
for a, b in bands:
    if b - a < 8: continue
    xs = [x for x in range(150, W - 50) for y in range(a, b + 1, 2) if im.getpixel((x, y)) < 100]
    print(a, b, min(xs), max(xs))
