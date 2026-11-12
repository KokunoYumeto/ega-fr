"""Put several crops side by side at the same scale.

Usage: python side.py OUTNAME SCALE PAGE:STRIP:X0:Y0:X1:Y1 [PAGE:STRIP:X0:Y0:X1:Y1 ...]
Coordinates in the displayed-image frame (width 2000).
"""
import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\crops_165_169"

name = sys.argv[1]
scale = float(sys.argv[2])
crops = []
for spec in sys.argv[3:]:
    p, s, x0, y0, x1, y1 = spec.split(":")
    im = Image.open(rf"{RUN}\page_{int(p):03d}_s{s}.png").convert("L")
    f = im.width / 2000.0
    c = im.crop((int(float(x0) * f), int(float(y0) * f), int(float(x1) * f), int(float(y1) * f)))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    crops.append(c)
W = sum(c.width for c in crops) + 20 * (len(crops) - 1)
H = max(c.height for c in crops)
out = Image.new("L", (W, H), 255)
x = 0
for c in crops:
    out.paste(c, (x, 0))
    x += c.width + 20
out.save(rf"{OUT}\{name}.png")
print(name, out.size)
