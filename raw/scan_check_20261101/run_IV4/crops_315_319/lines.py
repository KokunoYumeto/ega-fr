"""Crop horizontal bands of a strip, split into left and right halves, enlarged.

usage: python lines.py PAGE STRIP PREFIX x0 x1 scale y0:y1 [y0:y1 ...]
Writes PREFIX_<n>a.png (left half) and PREFIX_<n>b.png (right half).
"""
import sys
from PIL import Image

page, strip, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
x0, x1 = int(sys.argv[4]), int(sys.argv[5])
scale = float(sys.argv[6])
bands = [tuple(map(int, b.split(":"))) for b in sys.argv[7:]]
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
im = Image.open(rf"{base}\page_{page}_s{strip}.png")
xm = (x0 + x1) // 2
for n, (y0, y1) in enumerate(bands, 1):
    for tag, (a, b) in (("a", (x0, xm + 40)), ("b", (xm - 40, x1))):
        c = im.crop((a, y0, b, y1))
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        c.save(rf"{base}\crops_315_319\{prefix}_{n}{tag}.png")
print("ok", len(bands))
