import sys
from PIL import Image

RUN = r"user\Documents\ega_scan_check_20261101\run_IV1"
OUT = RUN + r"\crops_247_251"

# name: (strip file, (x0, y0, x1, y1) in original pixels, scale)
CROPS = {
    "p247_s3_resp": ("page_247_s3.png", (300, 100, 2100, 300), 1),
    "p247_s2_labels": ("page_247_s2.png", (440, 160, 1100, 800), 1),
    "p247_s3_labels": ("page_247_s3.png", (440, 400, 1100, 740), 1),
    "p248_s2_fermee": ("page_248_s2.png", (380, 600, 1100, 680), 2),
    "p249_s1_thm": ("page_249_s1.png", (340, 250, 2080, 400), 1),
    "p249_s3_list": ("page_249_s3.png", (440, 30, 1300, 260), 1),
    "p249_s3_proof": ("page_249_s3.png", (340, 500, 2100, 570), 1),
    "p249_s4_proof": ("page_249_s4.png", (340, 10, 1300, 240), 1),
    "p250_s1_impl": ("page_250_s1.png", (370, 440, 1300, 720), 1),
    "p250_s2_list": ("page_250_s2.png", (370, 50, 1300, 160), 1),
    "p250_s2_proof": ("page_250_s2.png", (370, 395, 2120, 575), 1),
    "p251_s2_head": ("page_251_s2.png", (880, 20, 1480, 100), 2),
    "p251_s2_entries": ("page_251_s2.png", (290, 230, 2040, 420), 1),
}


def main(names):
    for name in names:
        fn, box, scale = CROPS[name]
        im = Image.open(RUN + "\\" + fn).crop(box)
        if scale != 1:
            im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
        im.save(OUT + "\\" + name + ".png")
        print(name, im.size)


if __name__ == "__main__":
    main(sys.argv[1:] or list(CROPS))
