"""Second set of enlarged crops (punctuation and singular/plural in contents lines). Usage: crop2.py RUN_DIR OUT_DIR"""
import sys
from PIL import Image

run, out = sys.argv[1], sys.argv[2]
jobs = [
    ("p258_197_colon", "page_258_s1.png", (1100, 515, 1500, 580), 3),
    ("p258_198_semicolon", "page_258_s1.png", (1350, 635, 1650, 700), 3),
    ("p259_17_amelioration", "page_259_s2.png", (600, 575, 1400, 645), 2),
    ("p259_110_applications", "page_259_s2.png", (600, 745, 1400, 815), 2),
    ("p259_18_line", "page_259_s2.png", (600, 630, 2050, 700), 2),
]
for name, src, box, s in jobs:
    im = Image.open(f"{run}/{src}")
    c = im.crop(box)
    c = c.resize((c.width * s, c.height * s), Image.LANCZOS)
    c.save(f"{out}/{name}.png")
    print(name, im.size, box, c.size)
