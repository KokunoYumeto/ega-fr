import sys
from pathlib import Path
from PIL import Image

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "crops_100_104"

# name: (page, strip, x0, y0, x1, y1) in ORIGINAL pixel coordinates, enlargement factor
CROPS = {
    "c01_p100_cor536": (100, 2, 1375, 300, 2150, 375, 2),
    "c02_p100_def541": (100, 2, 412, 600, 2150, 712, 1),
    "c03_p100_def541b": (100, 3, 525, 12, 2150, 75, 1),
    "c04_p100_iv": (100, 4, 400, 325, 1250, 387, 2),
    "c05_p100_locales": (100, 3, 525, 262, 2150, 318, 1),
    "c06_p101_cor543": (101, 2, 339, 448, 1512, 496, 2),
    "c07_p101_resp": (101, 3, 242, 660, 1960, 823, 1),
    "c08_p101_afortiori": (101, 3, 242, 478, 1960, 532, 1),
    "c09_p102_somme": (102, 1, 387, 272, 2105, 333, 1),
    "c10_p102_u": (102, 1, 387, 393, 2105, 448, 1),
    "c11_p102_diagbot": (102, 4, 968, 181, 1452, 260, 3),
    "c11b_p102_diagtop": (102, 3, 968, 532, 1525, 605, 3),
    "c12_p102_text": (102, 4, 387, 308, 2130, 417, 1),
    "c13_p102_rem549": (102, 4, 484, 430, 2130, 532, 1),
    "c14_p103_display": (103, 2, 976, 604, 1342, 671, 3),
    "c15_p103_prop551a": (103, 3, 415, 689, 2037, 744, 1),
    "c16_p104_def552": (104, 1, 504, 258, 2128, 424, 1),
    "c17_p104_tresample": (104, 1, 504, 437, 2128, 541, 1),
    "c18_p104_PE": (104, 3, 1784, 344, 2128, 400, 3),
    "c19_p104_Pr": (104, 4, 1107, 332, 1722, 387, 2),
}

names = sys.argv[1:] or list(CROPS)
for name in names:
    page, strip, x0, y0, x1, y1, f = CROPS[name]
    im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
    c = im.crop((x0, y0, x1, y1))
    if f != 1:
        c = c.resize((c.width * f, c.height * f), Image.LANCZOS)
    c.save(OUT / f"{name}.png")
    print(name, c.size)
