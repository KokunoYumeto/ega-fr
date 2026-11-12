import sys
from PIL import Image

# usage: ink.py src x0 y0 x1 y1 out_png   (original pixels); prints the count of dark pixels (< 128)
src, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
im = Image.open(src).convert("L").crop((x0, y0, x1, y1))
dark = sum(1 for v in im.getdata() if v < 128)
im.resize((im.width * 6, im.height * 6), Image.NEAREST).save(out)
print(out, "box", (x0, y0, x1, y1), "dark px", dark)
