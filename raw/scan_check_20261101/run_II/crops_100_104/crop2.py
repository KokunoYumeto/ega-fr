from pathlib import Path
from PIL import Image
RUN = Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "crops_100_104"
CROPS = {
    "d01_p104_P_ii": (104, 3, 1960, 330, 2128, 405, 5),
    "d02_p103_S": (103, 4, 840, 270, 1000, 335, 5),
    "d03_p104_P_rem": (104, 3, 860, 625, 1030, 695, 5),
    "d04_p104_Pr": (104, 4, 1240, 325, 1340, 395, 5),
    "d05_p103_P_a": (103, 3, 1640, 685, 1780, 750, 5),
    "d06_p104_k": (104, 2, 1720, 405, 1860, 460, 5),
}
for name,(page,strip,x0,y0,x1,y1,f) in CROPS.items():
    im = Image.open(RUN / f"page_{page:03d}_s{strip}.png")
    c = im.crop((x0,y0,x1,y1))
    c = c.resize((c.width*f, c.height*f), Image.LANCZOS)
    c.save(OUT / f"{name}.png")
    print(name, c.size)
