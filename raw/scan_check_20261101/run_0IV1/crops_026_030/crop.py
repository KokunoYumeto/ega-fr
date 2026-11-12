"""Enlarged crop of one strip: python crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE] [NAME]
Coordinates in the strip's original pixels. Writes into this folder."""
import pathlib
import sys

from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
page, strip, x0, y0, x1, y1 = (int(a) for a in sys.argv[1:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
name = sys.argv[8] if len(sys.argv) > 8 else f"p{page:03d}_s{strip}_{x0}_{y0}"
im = Image.open(RUN / f"page_{page:03d}_s{strip}.png").crop((x0, y0, x1, y1))
im = im.resize((int(im.width * scale), int(im.height * scale)), Image.LANCZOS)
out = HERE / f"{name}.png"
im.save(out)
print(out)
