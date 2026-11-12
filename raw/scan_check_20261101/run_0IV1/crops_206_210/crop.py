"""crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]
Coordinates are in ORIGINAL pixels of page_PAGE_sSTRIP.png. Writes NAME.png into this folder."""
import sys, os
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
run = os.path.dirname(here)
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
im = Image.open(os.path.join(run, f'page_{int(page):03d}_s{strip}.png'))
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = os.path.join(here, name + '.png')
c.save(out)
print(out, c.size, im.size)
