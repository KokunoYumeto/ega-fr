"""List page markers \\oldpage[PART]{N} that occur more than once in an edition (within a file or across files).
usage: python -I find_duplicate_markers.py [diplomatic|current]"""
import collections
import pathlib
import re
import sys

ed = sys.argv[1] if len(sys.argv) > 1 else "diplomatic"
R = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20") / ed / "packages"
where = collections.defaultdict(list)
for f in sorted(R.rglob("*.tex")):
    if "direct" in f.parts or f.name.startswith("EGA_"):
        continue
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        for m in re.finditer(r"\\oldpage\[([^\]]*)\]\{(\d+)\}", line):
            where[(m.group(1), int(m.group(2)))].append(f"{f.name}:{i}")
dups = {k: v for k, v in where.items() if len(v) > 1}
for (part, n), v in sorted(dups.items()):
    print(part, n, " ".join(v))
print(len(dups), "duplicated markers;", len(where), "markers in all")
