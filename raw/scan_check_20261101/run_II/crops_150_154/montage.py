"""Stack several enlarged crops vertically into one image.

Usage: python montage.py OUTNAME SCALE PAGE:STRIP:x0:y0:x1:y1 [...]
"""
import sys
from PIL import Image, ImageDraw

base = r"user\Documents\ega_scan_check_20261101\run_II"
out = sys.argv[1]
scale = float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    page, strip, x0, y0, x1, y1 = spec.split(":")
    im = Image.open(rf"{base}\page_{page}_s{strip}.png").convert("L")
    c = im.crop((int(x0), int(y0), int(x1), int(y1)))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    tiles.append(c)
w = max(t.width for t in tiles)
h = sum(t.height for t in tiles) + 6 * (len(tiles) - 1)
m = Image.new("L", (w, h), 255)
y = 0
d = ImageDraw.Draw(m)
for t in tiles:
    m.paste(t, (0, y))
    y += t.height
    if y < h:
        d.rectangle((0, y, w, y + 5), fill=0)
    y += 6
m.save(rf"{base}\crops_150_154\{out}")
print(m.size)
