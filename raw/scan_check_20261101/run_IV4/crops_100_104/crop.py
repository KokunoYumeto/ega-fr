"""crop.py PAGE STRIP x0 y0 x1 y1 NAME [SCALE]: crop a region (original pixel coords) of page_PAGE_sSTRIP.png into crops_100_104/NAME.png"""
import sys
from PIL import Image
page, strip = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
name = sys.argv[7]
scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
im = Image.open(f"page_{int(page):03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1))
if scale != 1.0:
    c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(f"crops_100_104/{name}.png")
print(im.size, c.size)
