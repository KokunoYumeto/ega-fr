"""Crop regions of the strip images for close reading (checker 090-094).
Coordinates are in the 2000-px-wide display frame of each strip; they are scaled to the original."""
import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "crops_090_094"

CROPS = [
    # name, page, strip, x0, y0, x1, y1 (display coords), zoom
    ("p091_fini", 91, 2, 1000, 445, 1800, 500, 2),
    ("p091_ibis_label", 91, 3, 330, 405, 900, 460, 3),
    ("p092_ibis_prose1", 92, 1, 900, 435, 1790, 490, 2),
    ("p092_4410", 92, 1, 290, 580, 1300, 640, 2),
    ("p092_lemma_ii_a", 92, 2, 290, 205, 1800, 305, 2),
    ("p092_lemma_ii_b", 92, 2, 290, 300, 1800, 400, 2),
    ("p092_ibis_prose2", 92, 2, 390, 605, 1000, 660, 3),
    ("p093_affines", 93, 1, 280, 225, 1100, 285, 2),
    ("p093_46113", 93, 1, 280, 370, 1700, 430, 2),
    ("p093_display", 93, 2, 740, 55, 1220, 115, 3),
    ("p093_afortiori", 93, 2, 280, 350, 1000, 405, 2),
    ("p093_0371", 93, 2, 950, 398, 1700, 452, 2),
    ("p093_tout", 93, 2, 280, 635, 1000, 690, 2),
    ("p093_4411", 93, 4, 280, 195, 1700, 245, 2),
    ("p094_ibis", 94, 1, 900, 110, 1700, 165, 2),
    ("p094_452a", 94, 1, 250, 205, 1000, 260, 2),
    ("p094_443", 94, 2, 250, 28, 1700, 82, 2),
    ("p094_heading", 94, 2, 250, 220, 1700, 310, 2),
    ("p094_def_a", 94, 2, 250, 440, 1700, 540, 2),
    ("p094_def_b", 94, 2, 250, 535, 1700, 640, 2),
    ("p094_refs512", 94, 4, 340, 135, 1300, 232, 2),
]

only = set(sys.argv[1:])
for name, page, strip, x0, y0, x1, y1, zoom in CROPS:
    if only and name not in only:
        continue
    im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
    s = im.width / 2000
    box = (int(x0 * s), int(y0 * s), int(x1 * s), int(y1 * s))
    c = im.crop(box)
    c = c.resize((c.width * zoom, c.height * zoom), Image.LANCZOS)
    c.save(OUT / f"{name}.png")
    print(name, box, c.size)
