import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_I_b"
OUT = RUN + r"\crops_130_134"

# name, strip file, box in ORIGINAL pixel coordinates (x0, y0, x1, y1), scale factor
CROPS = [
    ("p130_fraktur", "page_130_s2.png", (440, 255, 900, 330), 2),
    ("p130_simeq", "page_130_s2.png", (1080, 440, 1560, 515), 2),
    ("p130_M_I", "page_130_s4.png", (600, 190, 900, 250), 3),
    ("p131_FY", "page_131_s1.png", (1100, 630, 1450, 705), 3),
    ("p132_def", "page_132_s2.png", (1100, 290, 1650, 360), 2),
    ("p132_pourvu", "page_132_s2.png", (300, 560, 2040, 680), 1),
    ("p134_graphe", "page_134_s1.png", (1600, 290, 2080, 350), 2),
    ("p134_sections", "page_134_s1.png", (340, 635, 1100, 695), 2),
]

for name, strip, box, scale in CROPS:
    im = Image.open(RUN + "\\" + strip)
    c = im.crop(box)
    if scale != 1:
        c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    c.save(OUT + "\\" + name + ".png")
    print(name, c.size)
