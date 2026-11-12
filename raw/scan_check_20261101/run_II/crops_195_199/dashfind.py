import sys
from PIL import Image
# find isolated horizontal bars (dash candidates): run length >= minlen, thickness <= 4 rows, clear above/below
page, strip = sys.argv[1], sys.argv[2]
minlen = int(sys.argv[3]) if len(sys.argv) > 3 else 15
im = Image.open(r"user\Documents\ega_scan_check_20261101\run_II\page_%s_s%s.png" % (page, strip)).convert('L')
W, H = im.size
px = im.load()
dark = lambda x, y: 0 <= x < W and 0 <= y < H and px[x, y] < 110
seen = set()
out = []
for y in range(H):
    x = 0
    while x < W:
        if dark(x, y):
            s = x
            while x < W and dark(x, y): x += 1
            L = x - s
            if L >= minlen:
                # thickness: rows above/below with mostly dark over the same span
                top = y
                while top - 1 >= 0 and sum(dark(i, top - 1) for i in range(s, x)) > 0.6 * L: top -= 1
                bot = y
                while bot + 1 < H and sum(dark(i, bot + 1) for i in range(s, x)) > 0.6 * L: bot += 1
                th = bot - top + 1
                if th <= 4:
                    clear = all(sum(dark(i, yy) for i in range(s, x)) <= 0.15 * L for yy in list(range(top - 6, top - 2)) + list(range(bot + 3, bot + 7)))
                    key = (s // 4, top // 3)
                    if clear and key not in seen:
                        seen.add(key)
                        out.append((top, s, L, th))
        else:
            x += 1
for t in out: print('y=%d x=%d len=%d th=%d' % t)
