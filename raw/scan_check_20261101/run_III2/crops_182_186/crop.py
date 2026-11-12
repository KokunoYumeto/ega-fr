"""crop.py PAGE STRIP X0 Y0 X1 Y1 [SCALE] -> crops_182_186/p<PAGE>_s<STRIP>_<X0>_<Y0>.png (coords in original pixels)"""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
run = here.parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(run / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = here / f"p{page}_s{strip}_{x0}_{y0}.png"
c.save(out)
print(out)
