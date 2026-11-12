import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{I\}\]\{(\d+)\}")
cite = re.compile(r"\(\[[IVX0-9]+\]")
for fn in sys.argv[1:]:
    lines = open(fn, encoding="utf-8").read().split("\n")
    page = None
    for i, l in enumerate(lines):
        m = marker.search(l)
        if m:
            page = int(m.group(1))
        if cite.search(l):
            print(fn[-50:], i + 1, "p.", page, l.strip()[:90])
