"""Crop helper for the scan check of EGA II pp. 85-89.

Usage: python crop.py <strip.png> <x0> <y0> <x1> <y1> <scale> <out_name>
Coordinates are in the strip's original pixels; the crop is enlarged by <scale>.
Output goes into this script's folder.
"""
import os
import sys

from PIL import Image


def main():
    src, x0, y0, x1, y1, scale, out = sys.argv[1:8]
    x0, y0, x1, y1 = (int(v) for v in (x0, y0, x1, y1))
    scale = float(scale)
    im = Image.open(src)
    box = im.crop((x0, y0, x1, y1))
    if scale != 1:
        box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, out)
    box.save(path)
    print(path, box.size)


if __name__ == "__main__":
    main()
