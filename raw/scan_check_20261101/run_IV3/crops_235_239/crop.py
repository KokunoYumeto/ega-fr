"""Crop helper for the pp. 235-239 check.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [ZOOM]
Coordinates are in the 2000-px-wide display frame of the strip image;
they are scaled to the original strip pixels before cropping.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent


def main():
    page, strip = sys.argv[1], sys.argv[2]
    x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
    name = sys.argv[7]
    zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
    src = RUN / f"page_{int(page):03d}_s{strip}.png"
    im = Image.open(src)
    s = im.size[0] / 2000.0
    box = tuple(int(round(v * s)) for v in (x0, y0, x1, y1))
    c = im.crop(box)
    if zoom != 1.0:
        c = c.resize((int(c.size[0] * zoom), int(c.size[1] * zoom)), Image.LANCZOS)
    dst = OUT / f"{name}.png"
    c.save(dst)
    print(dst, c.size)


if __name__ == "__main__":
    main()
