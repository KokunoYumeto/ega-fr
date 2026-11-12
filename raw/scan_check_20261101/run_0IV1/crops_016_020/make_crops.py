import sys, os
from PIL import Image
run = r"user/Documents/ega_scan_check_20261101/run_0IV1"
out = os.path.join(run, "crops_016_020")
# (name, page, strip, x0, y0, x1, y1) in ORIGINAL pixel coordinates
crops = [
 ("p16_fnk1",   16, 2,  400, 405, 2130, 527),
 ("p16_radical",16, 3,  400, 370, 2130, 440),
 ("p16_0I735",  16, 3,  900, 540, 1500, 610),
 ("p17_0I",     17, 2,  700, 370, 1800, 450),
 ("p18_posons", 18, 1,  350, 170, 2100, 330),
 ("p18_labels", 18, 2,  460, 100, 1340, 450),
 ("p18_proof1", 18, 2,  480, 465, 2100, 575),
 ("p18_proof2", 18, 3,  350, 50, 2100, 245),
 ("p18_proof3", 18, 3,  350, 505, 2100, 565),
 ("p18_items",  18, 4,  380, 40, 1700, 330),
 ("p19_0I612",  19, 1,  320, 290, 2050, 400),
 ("p19_labels", 19, 1,  400, 660, 1300, 790),
 ("p19_fgr",    19, 2,  680, 170, 1750, 360),
 ("p19_no8",    19, 2,  320, 435, 2050, 495),
 ("p19_items",  19, 4,  320, 105, 2050, 330),
 ("p20_finie",  20, 1,  370, 680, 1100, 745),
 ("p20_labels", 20, 2,  470, 565, 1400, 690),
 ("p20_proofab",20, 2,  470, 700, 1300, 765),
 ("p20_title",  20, 3,  370, 555, 1300, 700),
 ("p20_filtr",  20, 4,  370, 30, 2100, 330),
]
for name, page, strip, x0, y0, x1, y1 in crops:
    im = Image.open(os.path.join(run, f"page_{page:03d}_s{strip}.png"))
    c = im.crop((x0, y0, x1, y1))
    c.save(os.path.join(out, name + ".png"))
    print(name, im.size, c.size)
