"""rankA.py: rank the A glyphs of findA_out.txt by stroke run within each size class (h<29 small, else large)."""
import re
rows = []
for line in open("findA_out.txt"):
    m = re.match(r"p(\d+) s(\d) x=\s*(\d+) y=\s*(\d+) w=\s*(\d+) h=\s*(\d+) ink=\s*(\d+) run=([\d.]+) score=([\d.]+)", line)
    if m:
        p, s, x, y, w, h, ink = (int(v) for v in m.groups()[:7])
        rows.append((p, s, x, y, w, h, ink, float(m.group(8)), float(m.group(9))))
for name, cls in (("small", [r for r in rows if r[5] < 29]), ("large", [r for r in rows if r[5] >= 29])):
    runs = sorted(r[7] for r in cls)
    inks = sorted(r[6] for r in cls)
    if not cls:
        continue
    print(name, "n=%d median run=%.2f median ink=%d" % (len(cls), runs[len(runs) // 2], inks[len(inks) // 2]))
    for r in sorted(cls, key=lambda r: -r[7])[:10]:
        print("  p%d s%d x=%d y=%d w=%d h=%d ink=%d run=%.2f score=%.2f" % r)
