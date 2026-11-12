"""Enlarged crops of printed p. 5 (EGA IV-1) for the scan check.

Usage: python -I crop.py <run_folder>
Writes the crops next to this script.
"""
import os
import sys

from PIL import Image

run = sys.argv[1]
out = os.path.dirname(os.path.abspath(__file__))

# (name, strip, (x0, y0, x1, y1) in original pixels, scale)
JOBS = [
    ("heading", "page_005_s1.png", (880, 570, 1560, 690), 2),
    ("fn1_symbole", "page_005_s4.png", (780, 130, 1260, 195), 3),
    ("fn1_chapitre_o", "page_005_s4.png", (1480, 130, 2090, 195), 3),
    ("fn1_line2", "page_005_s4.png", (350, 170, 720, 215), 3),
    ("fn2_end", "page_005_s4.png", (350, 245, 2090, 320), 1),
    ("sommaire_15", "page_005_s2.png", (340, 420, 1340, 480), 2),
]

for name, strip, box, scale in JOBS:
    im = Image.open(os.path.join(run, strip)).convert("L")
    c = im.crop(box)
    if scale != 1:
        c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    path = os.path.join(out, f"{name}.png")
    c.save(path)
    print(path, c.size)
