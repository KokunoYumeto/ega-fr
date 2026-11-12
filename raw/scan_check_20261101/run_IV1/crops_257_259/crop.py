"""Enlarged crops of strip images for pages 257-259. Usage: crop.py RUN_DIR OUT_DIR"""
import sys
from PIL import Image

run, out = sys.argv[1], sys.argv[2]
# name, strip file, (x0, y0, x1, y1) in original pixels, scale
jobs = [
    ("p257_chap0", "page_257_s2.png", (300, 40, 1180, 135), 2),
    ("p257_M_reg", "page_257_s2.png", (600, 405, 1480, 475), 2),
    ("p257_M_quasi", "page_257_s2.png", (600, 470, 1580, 535), 2),
    ("p257_A_ext", "page_257_s3.png", (600, 705, 1400, 770), 2),
    ("p258_Omega", "page_258_s2.png", (1380, 515, 1660, 590), 4),
    ("p259_chapIV", "page_259_s2.png", (300, 20, 1880, 95), 2),
    ("p259_biblio", "page_259_s3.png", (300, 70, 800, 140), 3),
    ("p259_index", "page_259_s3.png", (300, 150, 820, 310), 2),
    ("p259_recu", "page_259_s3.png", (1450, 430, 1960, 510), 2),
]
for name, src, box, s in jobs:
    im = Image.open(f"{run}/{src}")
    c = im.crop(box)
    c = c.resize((c.width * s, c.height * s), Image.LANCZOS)
    c.save(f"{out}/{name}.png")
    print(name, im.size, box, c.size)
