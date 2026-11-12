"""Measure ink coverage of glyph boxes in a strip (boxes in 2000-px display coordinates)."""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent

def ink(page, strip, box, thr=128):
    im = Image.open(RUN / f"page_{page}_s{strip}.png").convert("L")
    s = im.size[0] / 2000.0
    b = tuple(int(round(v * s)) for v in box)
    c = im.crop(b)
    px = list(c.getdata())
    dark = sum(1 for p in px if p < thr)
    return dark, c.size

if __name__ == "__main__":
    page, strip = sys.argv[1], sys.argv[2]
    vals = [float(v) for v in sys.argv[3:]]
    for i in range(0, len(vals), 4):
        print(vals[i:i+4], ink(page, strip, vals[i:i+4]))
