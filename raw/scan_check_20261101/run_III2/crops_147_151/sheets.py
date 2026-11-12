import sys, re
from PIL import Image, ImageDraw
# read candidate list from stdin lines "p s y0 y1 a b r", make sheets of 4 cols x 12 rows
lines = [l.split() for l in sys.stdin.read().strip().splitlines() if re.match(r"^\d{3} ", l)]
cells = []
for i, (p, s, y0, y1, a, b, r) in enumerate(lines):
    y0, y1, a, b = int(y0), int(y1), int(a), int(b)
    g = Image.open(f"page_{p}_s{s}.png").convert("L")
    cr = g.crop((max(0, a - 70), max(0, y0 - 4), min(g.width, b + 70), y1 + 4))
    cr.thumbnail((330, 60))
    cell = Image.new("L", (380, 66), 255)
    cell.paste(cr, (44, 3))
    ImageDraw.Draw(cell).text((2, 25), str(i), fill=0)
    cells.append(cell)
per = 48
for k in range(0, len(cells), per):
    chunk = cells[k:k + per]
    sheet = Image.new("L", (4 * 380, 12 * 66), 255)
    for j, c in enumerate(chunk):
        sheet.paste(c, ((j % 4) * 380, (j // 4) * 66))
    sheet.save(f"crops_147_151/bold_sheet_{k // per}.png")
print(len(cells))
