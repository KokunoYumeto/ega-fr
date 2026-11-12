"""Cross-check the EGA II contents (pp. 213-215) against the page markers: for every section/subsection label in
ega2-1-fr.tex, report the printed page on which the TeX places it (last \\oldpage[II]{N} before the label)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages"
       r"\BASE\native\ega2\ega2-1-fr.tex")
t = open(SRC, encoding="utf-8").read()
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"\\oldpage\[II\]\{(\d+)\}", t)]


def page_at(pos):
    p = None
    for s, n in marks:
        if s <= pos:
            p = n
        else:
            break
    return p


for m in re.finditer(r"\\label\{((?:sub)?section:II\.[0-9.]+-fr|II\.[0-9]+\.[0-9]+-fr)\}", t):
    lab = m.group(1)
    if len(re.findall(r"[0-9]+", lab)) > 2:
        continue
    pre = t[max(0, m.start() - 400):m.start()]
    h = re.findall(r"\\(?:sub)?section\*?\{([^}]*)\}", pre)
    # position of the heading itself (not the label) for the page lookup
    hpos = m.start() - (len(pre) - pre.rfind("\\")) if h else m.start()
    print(lab, page_at(m.start()), "|", (h[-1][:60] if h else "?"))
