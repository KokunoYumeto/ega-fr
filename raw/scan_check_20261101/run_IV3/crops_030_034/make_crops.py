import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV3"
OUT = RUN + "/crops_030_034"

# name: (strip file, (x0, y0, x1, y1), scale)
CROPS = {
    "p30_s2_compte_tenu": ("page_030_s2.png", (650, 590, 1300, 665), 2),
    "p30_s3_indice": ("page_030_s3.png", (1700, 470, 2180, 530), 2),
    "p30_s3_Uimu": ("page_030_s3.png", (430, 530, 760, 590), 2),
    "p31_s2_quasisep": ("page_031_s2.png", (800, 625, 1300, 690), 2),
    "p31_s2_restriction": ("page_031_s2.png", (1400, 570, 1900, 630), 2),
    "p31_s3_lim": ("page_031_s3.png", (290, 340, 900, 410), 2),
    "p32_s4_162": ("page_032_s4.png", (1250, 120, 1480, 180), 3),
    "p33_s1_163": ("page_033_s1.png", (700, 670, 1960, 735), 2),
    "p33_s3_162": ("page_033_s3.png", (1400, 280, 1640, 330), 3),
    "p33_s4_f1f2": ("page_033_s4.png", (1580, 175, 1800, 230), 3),
    "p34_s3_161": ("page_034_s3.png", (700, 690, 1850, 745), 2),
    "p34_s4_182": ("page_034_s4.png", (1950, 20, 2200, 70), 3),
    "p34_s2_labels": ("page_034_s2.png", (540, 400, 900, 700), 2),
}

names = sys.argv[1:] or list(CROPS)
for name in names:
    fn, box, sc = CROPS[name]
    im = Image.open(RUN + "/" + fn)
    c = im.crop(box)
    c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
    c.save(OUT + "/" + name + ".png")
    print(name, c.size)
