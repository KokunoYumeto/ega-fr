"""zoomorig.py PAGE STRIP X0 Y0 X1 Y1 ZOOM NAME -- ORIGINAL pixel coords, nearest-neighbour zoom."""
import sys, pathlib
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
page, strip = int(sys.argv[1]), int(sys.argv[2])
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7]); z = int(sys.argv[7]); name = sys.argv[8]
im = Image.open(here.parent / f"page_{page:03d}_s{strip}.png")
c = im.crop((x0, y0, x1, y1)); c = c.resize((c.size[0] * z, c.size[1] * z), Image.NEAREST)
c.save(here / f"{name}.png"); print(name, c.size)
