"""List section/subsection headings of EGA IV-1 sources with the printed page they fall on (last \\oldpage before).

Usage: heading_pages.py SOURCE_DIR
Prints: file:line  page  [marker within next 3 lines?]  command  title
"""
import re
import sys

src = sys.argv[1]
files = ["ega0-14-fr.tex", "ega0-15-fr.tex", "ega0-16-fr.tex", "ega0-17-fr.tex", "ega0-18-fr.tex",
         "ega0-19-fr.tex", "ega0-19b-fr.tex", "ega0-20-fr.tex", "ega0-21-fr.tex", "ega0-22-fr.tex",
         "ega0-23-fr.tex", "ega4-1-fr.tex"]
mark = re.compile(r"\\oldpage\[([^\]]*)\]\{(\d+)\}")
head = re.compile(r"\\(chapter|section|subsection)\*?(\[[^\]]*\])?\{(.*)")
page = None
for fn in files:
    try:
        lines = open(f"{src}/{fn}", encoding="utf-8").read().split("\n")
    except FileNotFoundError:
        print("MISSING", fn)
        continue
    for i, line in enumerate(lines):
        for m in mark.finditer(line):
            page = (m.group(1), int(m.group(2)))
        h = head.search(line)
        if h and not line.lstrip().startswith("%"):
            nxt = ""
            for j in range(i + 1, min(i + 4, len(lines))):
                m2 = mark.search(lines[j])
                if m2:
                    nxt = f" [marker {m2.group(2)} at +{j - i}]"
                    break
            print(f"{fn}:{i + 1}\t{page[1] if page else None}{nxt}\t{h.group(1)}\t{h.group(3)[:90]}")
