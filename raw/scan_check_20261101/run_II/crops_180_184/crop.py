"""crop.py STRIP x0 y0 x1 y1 SCALE OUTNAME  -- coordinates in original strip pixels."""
import sys, pathlib
from PIL import Image
src, x0, y0, x1, y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), float(sys.argv[6]), sys.argv[7]
im = Image.open(src)
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(pathlib.Path(__file__).parent / out)
print(out, c.size)
