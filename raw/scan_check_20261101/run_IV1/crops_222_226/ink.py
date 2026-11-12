"""Ink fraction of the dark glyph inside a box: dark pixels / bounding-box area of the dark pixels.

Usage: python ink.py <strip.png> <x0> <y0> <x1> <y1> [threshold]
"""
import sys
from PIL import Image

src = sys.argv[1]
x0, y0, x1, y1 = map(int, sys.argv[2:6])
thr = int(sys.argv[6]) if len(sys.argv) > 6 else 128
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
w, h = im.size
px = im.load()
dark = [(x, y) for y in range(h) for x in range(w) if px[x, y] < thr]
if not dark:
    print("no ink")
    sys.exit()
xs = [p[0] for p in dark]
ys = [p[1] for p in dark]
bw, bh = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
print(f"ink={len(dark)} bbox={bw}x{bh} fraction={len(dark) / (bw * bh):.3f} ink/height^2={len(dark) / (bh * bh):.3f}")
