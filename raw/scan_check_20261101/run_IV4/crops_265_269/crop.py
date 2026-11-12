"""Crop regions from the page strips for close reading.

Usage: python crop.py NAME PAGE STRIP X0 Y0 X1 Y1 [SCALE] [DISP]
Coordinates are in displayed-image pixels when DISP=1 (default), using the
strip's display factor (original width / 2000); otherwise original pixels.
"""
import sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
RUN = HERE.parent


def main():
    name, page, strip = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
    scale = float(sys.argv[8]) if len(sys.argv) > 8 else 2.0
    disp = (sys.argv[9] != "0") if len(sys.argv) > 9 else True
    img = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
    f = img.width / 2000.0 if disp else 1.0
    box = tuple(int(round(v * f)) for v in (x0, y0, x1, y1))
    crop = img.crop(box)
    if scale != 1.0:
        crop = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
    out = HERE / f"{name}.png"
    crop.save(out)
    print(out, box, crop.size)


if __name__ == "__main__":
    main()
