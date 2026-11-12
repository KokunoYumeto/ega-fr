"""Crop helper for the pp. 95-99 scan check (writes only into this folder).

Usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE]
Coordinates are pixels of the original strip image page_PPP_sS.png.
"""
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)


def main():
    name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    x0, y0, x1, y1 = (int(v) for v in sys.argv[4:8])
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 1.5
    src = os.path.join(RUN, "page_%03d_s%d.png" % (page, strip))
    im = Image.open(src)
    box = (max(0, x0), max(0, y0), min(im.width, x1), min(im.height, y1))
    c = im.crop(box)
    if scale != 1:
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    out = os.path.join(HERE, name + ".png")
    c.save(out)
    print(out, c.size)


if __name__ == "__main__":
    main()
