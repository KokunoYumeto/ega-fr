"""List places in the release TeX where a \\section / \\subsection heading stands directly before a page marker
(only blank lines, \\label or \\setcounter lines in between), i.e. the heading is counted on the previous page.
usage: python -I heading_marker_scan.py NATIVE_DIR"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
root = pathlib.Path(sys.argv[1])
head = re.compile(r"^\\(?:sub)*section\*?\{")
skip = re.compile(r"^(\\label\{[^}]*\}|\\setcounter\{[^}]*\}\{[^}]*\}|\s*)$")
mark = re.compile(r"^\\oldpage\[([^\]]*)\]\{(\d+)\}")
total = 0
for f in sorted(root.rglob("*.tex")):
    if f.name.startswith("stub_") or f.name == "EGA_FR.tex":
        continue
    lines = f.read_text(encoding="utf-8").split("\n")
    hits = []
    for i, line in enumerate(lines):
        if not head.match(line):
            continue
        j = i + 1
        while j < len(lines) and skip.match(lines[j]) and not mark.match(lines[j]):
            j += 1
        if j < len(lines):
            m = mark.match(lines[j])
            if m:
                hits.append(f"{m.group(2)}(l.{i + 1})")
    if hits:
        total += len(hits)
        print(f.relative_to(root), len(hits), " ".join(hits))
print("total", total)
