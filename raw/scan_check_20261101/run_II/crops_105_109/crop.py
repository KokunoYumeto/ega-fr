import sys
from pathlib import Path
from PIL import Image

RUN = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent

# name, strip file, (x0, y0, x1, y1) in original pixels, upscale
JOBS = [
    ("p105_s1_P_S_k", "page_105_s1.png", (1000, 318, 2040, 475), 2),
    ("p105_s2_b", "page_105_s2.png", (1690, 560, 2030, 620), 3),
    ("p105_s3_a", "page_105_s3.png", (1690, 620, 2030, 685), 3),
    ("p106_s3_i", "page_106_s3.png", (452, 190, 2070, 295), 2),
    ("p106_s3_iii", "page_106_s3.png", (452, 416, 2070, 525), 2),
    ("p106_s4_compl", "page_106_s4.png", (333, 340, 680, 445), 3),
    ("p107_s1_534", "page_107_s1.png", (347, 580, 2080, 745), 2),
    ("p107_s2_prod", "page_107_s2.png", (920, 250, 1530, 315), 3),
    ("p108_s4_Xk", "page_108_s4.png", (404, 120, 2120, 235), 2),
    ("p109_s2_ab", "page_109_s2.png", (415, 20, 2020, 75), 2),
    ("p109_s2_resp", "page_109_s2.png", (300, 245, 2020, 360), 2),
    ("p109_s3_dtf", "page_109_s3.png", (300, 45, 2020, 105), 2),
    ("p109_s3_diag", "page_109_s3.png", (1040, 460, 1310, 705), 2),
]

only = set(sys.argv[1:])
for name, strip, box, up in JOBS:
    if only and name not in only:
        continue
    im = Image.open(RUN / strip)
    c = im.crop(box)
    c = c.resize((c.width * up, c.height * up), Image.LANCZOS)
    c.save(OUT / f"{name}.png")
    print(name, c.size)
