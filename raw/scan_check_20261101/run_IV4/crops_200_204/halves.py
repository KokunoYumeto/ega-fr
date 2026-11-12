"""Cut each strip of a page into left and right halves at native resolution."""
import sys
from PIL import Image

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = RUN + "/crops_200_204"
page = int(sys.argv[1])
for s in (1, 2, 3, 4):
    im = Image.open(RUN + "/page_%03d_s%d.png" % (page, s))
    w, h = im.size
    mid = w // 2
    im.crop((250, 0, mid + 60, h)).save(OUT + "/h%03d_s%dL.png" % (page, s))
    im.crop((mid - 60, 0, w - 150, h)).save(OUT + "/h%03d_s%dR.png" % (page, s))
print("ok")
