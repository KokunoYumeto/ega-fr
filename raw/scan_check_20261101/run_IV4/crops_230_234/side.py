"""Put several crops side by side at the same scale.

Usage: python side.py NAME SCALE PAGE:STRIP:X0:Y0:X1:Y1 [PAGE:STRIP:X0:Y0:X1:Y1 ...]
"""
import sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RUN = HERE.parent

name = sys.argv[1]
scale = float(sys.argv[2])
tiles = []
for spec in sys.argv[3:]:
    page, strip, x0, y0, x1, y1 = spec.split(":")
    img = Image.open(RUN / f"page_{page}_s{strip}.png").convert("L")
    box = img.crop((int(x0), int(y0), int(x1), int(y1)))
    box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
    tiles.append(box)
gap = 20
w = sum(t.width for t in tiles) + gap * (len(tiles) - 1)
h = max(t.height for t in tiles)
out = Image.new("L", (w, h), 255)
x = 0
for t in tiles:
    out.paste(t, (x, 0))
    x += t.width + gap
path = HERE / f"{name}.png"
out.save(path)
print(path)
