"""Contact sheets of the scan lines that contain a Tor sheaf symbol, one sheet per page (for the heavy/light check)."""
from PIL import Image, ImageDraw

RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
LINES = {
    147: [(2, 150, 215), (2, 320, 390), (3, 448, 508), (3, 622, 682)],
    148: [(3, 315, 372), (3, 478, 535), (3, 715, 772), (4, 160, 218)],
    149: [(1, 280, 335), (1, 345, 400), (1, 400, 452), (1, 635, 690), (2, 60, 120), (2, 150, 230),
          (2, 290, 360), (2, 360, 420), (2, 400, 460), (2, 515, 570), (3, 75, 135), (3, 205, 262),
          (3, 405, 470), (3, 490, 560)],
    150: [(2, 40, 100), (2, 320, 395), (2, 495, 560), (3, 25, 100), (3, 380, 445), (3, 660, 725)],
    151: [(1, 405, 470), (2, 485, 552), (3, 515, 580)],
}
for page, rows in LINES.items():
    crops = []
    for s, y0, y1 in rows:
        im = Image.open(f"{RUN}\\page_{page}_s{s}.png").convert("L")
        c = im.crop((250, y0, 2250, y1))
        crops.append(c)
    W = max(c.width for c in crops) + 60
    H = sum(c.height + 6 for c in crops)
    sheet = Image.new("L", (W, H), 255)
    d = ImageDraw.Draw(sheet)
    y = 0
    for i, c in enumerate(crops):
        sheet.paste(c, (60, y))
        d.text((5, y + c.height // 2 - 5), str(i), fill=0)
        y += c.height + 6
    sheet.save(f"{RUN}\\crops_147_151\\tor_{page}.png")
    print(page, sheet.size)
