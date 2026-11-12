"""Cut each strip of the given pages into a left and a right half, enlarged, for checking small letters.

usage: python halves.py PAGE [PAGE ...]
"""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent

for page in (int(p) for p in sys.argv[1:]):
    for strip in range(1, 5):
        img = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
        w, h = img.size
        # text block lies roughly between 10% and 90% of the width
        x0, x1 = int(w * 0.10), int(w * 0.90)
        mid = (x0 + x1) // 2
        for side, (a, b) in (("L", (x0, mid + 40)), ("R", (mid - 40, x1))):
            crop = img.crop((a, 0, b, h))
            scale = 2000 / crop.width
            crop = crop.resize((2000, int(h * scale)), Image.LANCZOS)
            crop.save(OUT / f"half_{page}_s{strip}{side}.png")
print("done")
