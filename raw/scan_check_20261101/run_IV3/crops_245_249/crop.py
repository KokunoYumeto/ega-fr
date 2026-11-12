import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = RUN + r"\crops_245_249"

# name: (strip file, box (x0, y0, x1, y1) in original pixels, scale)
CROPS = {
    "p245_ysection": ("page_245_s4.png", (300, 0, 2100, 70), 1),
    "p245_proj": ("page_245_s3.png", (1100, 650, 2100, 740), 2),
    "p245_item_i": ("page_245_s4.png", (300, 230, 2100, 370), 1),
    "p245_cb": ("page_245_s1.png", (300, 400, 2100, 520), 1),
    "p246_autrement": ("page_246_s1.png", (420, 280, 2200, 410), 1),
    "p246_X0propre": ("page_246_s2.png", (420, 380, 1500, 450), 2),
    "p246_iet": ("page_246_s3.png", (1100, 145, 2200, 220), 2),
    "p247_fini": ("page_247_s1.png", (280, 480, 1300, 570), 2),
    "p247_ou": ("page_247_s2.png", (280, 235, 2100, 380), 1),
    "p247_lemma": ("page_247_s3.png", (280, 420, 2100, 600), 1),
    "p247_fY1": ("page_247_s4.png", (280, 0, 1300, 70), 2),
    "p247_fY1b": ("page_247_s3.png", (280, 740, 1300, 838), 2),
    "p248_E": ("page_248_s1.png", (420, 300, 1500, 420), 2),
}

names = sys.argv[1:] or list(CROPS)
for n in names:
    f, box, s = CROPS[n]
    im = Image.open(RUN + "\\" + f).crop(box)
    if s != 1:
        im = im.resize((im.width * s, im.height * s), Image.LANCZOS)
    im.save(OUT + "\\" + n + ".png")
    print(n, im.size)
