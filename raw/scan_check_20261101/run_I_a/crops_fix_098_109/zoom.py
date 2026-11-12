"""Zoom into a printed EGA I page from the NUMDAM PDF, using pixel coordinates of a 300-dpi strip page_NNN_sK.png
(the strips were cut by make_bands.py: margins trimmed, 4 strips, 40 px overlap).
usage: python zoom.py PAGE K X0 Y0 X1 Y1 [DPI]   (coordinates in the strip's original pixels)
       -> crops_fix_098_109/z<PAGE>_s<K>_<Y0>_<X0>.png"""
import pathlib
import sys

import fitz
from PIL import Image

PDF = r"user\Documents\Free or receipted\free\lesson-sources\numdam\PMIHES_1960__4__5_0.pdf"
OUT = pathlib.Path(__file__).resolve().parent
page, k = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
dpi = float(sys.argv[7]) if len(sys.argv) > 7 else 600
doc = fitz.open(PDF)
p = doc[page - 2]  # pdf page = printed page - 1 (1-based)
pix = p.get_pixmap(matrix=fitz.Matrix(300 / 72, 300 / 72), colorspace=fitz.csGRAY)
im = Image.frombytes("L", (pix.width, pix.height), pix.samples)
w, h = im.size
box = Image.eval(im, lambda v: 255 - v).getbbox() or (0, 0, w, h)
left, top, bottom = max(0, box[0] - 20), max(0, box[1] - 20), min(h, box[3] + 20)
step = (bottom - top) / 4
sy0 = max(top, int(top + (k - 1) * step) - (40 if k > 1 else 0))
fx0, fy0, fx1, fy1 = left + x0, sy0 + y0, left + x1, sy0 + y1
s = 72 / 300
clip = fitz.Rect(fx0 * s, fy0 * s, fx1 * s, fy1 * s)
z = p.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=clip)
name = OUT / f"z{page}_s{k}_{int(y0)}_{int(x0)}.png"
z.save(str(name))
print(name, z.width, z.height)
