"""Put several crops side by side at the same scale.

Usage: python side.py <out.png> <scale> <img> <x0> <y0> <x1> <y1> [<img> <x0> <y0> <x1> <y1> ...]
"""
import sys
from PIL import Image

out = sys.argv[1]
scale = float(sys.argv[2])
args = sys.argv[3:]
crops = []
for i in range(0, len(args), 5):
    src = args[i]
    box = tuple(int(float(v)) for v in args[i + 1:i + 5])
    c = Image.open(src).convert("L").crop(box)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    crops.append(c)
w = sum(c.width for c in crops) + 30 * (len(crops) - 1)
h = max(c.height for c in crops)
canvas = Image.new("L", (w, h), 255)
x = 0
for c in crops:
    canvas.paste(c, (x, 0))
    x += c.width + 30
canvas.save(out)
print(out, canvas.size)
