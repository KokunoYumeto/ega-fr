"""Crop a region of a strip image for close reading.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 NAME [ZOOM]
Coordinates are in the 2000-px-wide display frame of the strip; ZOOM (default 2) upscales the crop.
"""
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
RUN = HERE.parent


def main() -> None:
    page, strip = sys.argv[1], sys.argv[2]
    x0, y0, x1, y1 = (float(v) for v in sys.argv[3:7])
    name = sys.argv[7]
    zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
    im = Image.open(RUN / f"page_{page}_s{strip}.png")
    s = im.size[0] / 2000.0
    box = tuple(int(round(v * s)) for v in (x0, y0, x1, y1))
    crop = im.crop(box)
    crop = crop.resize((int(crop.size[0] * zoom), int(crop.size[1] * zoom)), Image.LANCZOS)
    out = HERE / f"{name}.png"
    crop.save(out)
    print(out)


if __name__ == "__main__":
    main()
