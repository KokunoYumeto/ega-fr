"""Crop a region of a page strip and enlarge it.

Usage: python crop.py PAGE STRIP X0 Y0 X1 Y1 SCALE OUTNAME
Coordinates are in the strip's original pixels.
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent


def main() -> None:
    page, strip = int(sys.argv[1]), int(sys.argv[2])
    x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
    scale = float(sys.argv[7])
    name = sys.argv[8]
    src = RUN / f"page_{page:03d}_s{strip}.png"
    img = Image.open(src)
    box = img.crop((x0, y0, x1, y1))
    if scale != 1:
        box = box.resize((int(box.width * scale), int(box.height * scale)), Image.LANCZOS)
    box.save(OUT / name)
    print(OUT / name, box.size)


if __name__ == "__main__":
    main()
