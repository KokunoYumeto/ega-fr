"""Crop regions of the page strips for close inspection.

Usage: python -I crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [ZOOM]
Coordinates are in the 2000-px-wide display frame of the strip; they are
scaled to the strip's real width.  Output: crops_165_169/NAME.png
"""
import sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RUN = HERE.parent


def main(argv):
    name, page, strip = argv[0], int(argv[1]), int(argv[2])
    x0, y0, x1, y1 = (float(v) for v in argv[3:7])
    zoom = float(argv[7]) if len(argv) > 7 else 2.5
    src = RUN / f"page_{page:03d}_s{strip}.png"
    im = Image.open(src)
    f = im.width / 2000.0
    box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
    c = im.crop(box)
    c = c.resize((int(c.width * zoom), int(c.height * zoom)), Image.LANCZOS)
    out = HERE / f"{name}.png"
    c.save(out)
    print(out, box, c.size)


if __name__ == "__main__":
    main(sys.argv[1:])
