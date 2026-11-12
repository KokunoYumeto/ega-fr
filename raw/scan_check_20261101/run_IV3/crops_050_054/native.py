import sys
import fitz

# usage: native.py <printed page> -> prints info on embedded images of that pdf page (offset -1, 0-based index = printed + offset - 1)
# usage: native.py <printed page> <fx0> <fy0> <fx1> <fy1> <out> [zoom]: render region given as fractions of page size
pdf = r"user\Documents\Free or receipted\free\lesson-sources\numdam\PMIHES_1966__28__5_0.pdf"
doc = fitz.open(pdf)
printed = int(sys.argv[1])
idx = printed - 1 - 1  # pdf page number = printed - 1; 0-based index = that - 1
page = doc[idx]
if len(sys.argv) == 2:
    print("page index", idx, "rect", page.rect)
    for img in page.get_images(full=True):
        print(img)
    sys.exit()
fx0, fy0, fx1, fy1 = map(float, sys.argv[2:6])
out = sys.argv[6]
zoom = float(sys.argv[7]) if len(sys.argv) > 7 else 8.0
r = page.rect
clip = fitz.Rect(r.x0 + fx0 * r.width, r.y0 + fy0 * r.height, r.x0 + fx1 * r.width, r.y0 + fy1 * r.height)
pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
pix.save(rf"user\Documents\ega_scan_check_20261101\run_IV3\crops_050_054\{out}.png")
print(pix.width, pix.height)
