"""Which EGA II page numbers have no \\oldpage[II] marker in the r20 diplomatic files, and where 200-212 sit."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
d = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))
files = d["parts"]["II"]["files"]
pat = re.compile(r"\\oldpage\[II\]\{(\d+)\}")
seen = {}
for f in files:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    for m in pat.finditer(t):
        seen.setdefault(int(m.group(1)), []).append(pathlib.Path(f).name)
print("missing", [n for n in range(5, 223) if n not in seen])
print({n: seen[n] for n in range(198, 212) if n in seen})
