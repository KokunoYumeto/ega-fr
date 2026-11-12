"""Put several crops of one strip side by side at the same scale, with a thin separator.

Usage: python montage.py PAGE STRIP SCALE OUTNAME x0,y0,x1,y1 [x0,y0,x1,y1 ...]
Coordinates are in the strip's original pixel frame.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0III")
OUT = RUN / "crops_015_019"

page, strip, scale, name = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
boxes = [tuple(int(v) for v in b.split(",")) for b in sys.argv[5:]]
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").convert("L")
crops = []
for b in boxes:
    c = im.crop(b)
    crops.append(c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS))
h = max(c.height for c in crops)
w = sum(c.width for c in crops) + 12 * (len(crops) - 1)
out = Image.new("L", (w, h), 255)
x = 0
for c in crops:
    out.paste(c, (x, 0))
    x += c.width
    if x < w:
        for yy in range(h):
            for xx in range(x + 4, x + 8):
                out.putpixel((xx, yy), 0)
    x += 12
out.save(OUT / name)
print(OUT / name, out.size)
