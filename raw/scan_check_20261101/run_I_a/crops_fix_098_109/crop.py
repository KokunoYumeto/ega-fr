"""Render a region of a printed EGA I page from the NUMDAM PDF (pdf page = printed page - 1, 1-based).
usage: python crop.py PAGE Y0 Y1 [X0 X1] [ZOOM]   (fractions of the page height/width, 0..1)
writes crops_fix_098_109/p<PAGE>_<Y0>_<Y1>.png"""
import pathlib
import sys

import fitz

PDF = r"user\Documents\Free or receipted\free\lesson-sources\numdam\PMIHES_1960__4__5_0.pdf"
OUT = pathlib.Path(__file__).resolve().parent
page = int(sys.argv[1])
y0, y1 = float(sys.argv[2]), float(sys.argv[3])
x0, x1 = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 5 else (0.0, 1.0)
zoom = float(sys.argv[6]) if len(sys.argv) > 6 else 6.0
doc = fitz.open(PDF)
p = doc[page - 2]  # 0-based index of pdf page (printed page - 1)
r = p.rect
clip = fitz.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height, r.x0 + x1 * r.width, r.y0 + y1 * r.height)
pix = p.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
name = OUT / f"p{page}_{y0:.3f}_{y1:.3f}_{x0:.2f}_{x1:.2f}.png"
pix.save(str(name))
print(name, pix.width, pix.height)
