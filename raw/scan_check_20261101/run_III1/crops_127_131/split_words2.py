import pathlib
import re

# How do the other release files write a word that the print hyphenates across a page break?
root = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native")
pat_h = re.compile(r"([A-Za-zÀ-ÿ]{2,14})-[ \t]*\n(?:[ \t]*\n)*\\oldpage\[[^\]]*\]\{\d+\}[^\n]*\n(?:[ \t]*\n)*([a-zà-ÿ]{2,14})")
pat_pct = re.compile(r"([A-Za-zÀ-ÿ]{2,14})%[ \t]*\n(?:[ \t]*\n)*\\oldpage\[[^\]]*\]\{\d+\}[^\n]*\n(?:[ \t]*\n)*([a-zà-ÿ]{2,14})")
pat_inword = re.compile(r"([a-zà-ÿ]{2,14})\\oldpage\[[^\]]*\]\{\d+\}([a-zà-ÿ]{2,14})")
for f in sorted(root.rglob("*.tex")):
    t = f.read_text(encoding="utf-8", errors="replace")
    a = [m.group(0) for m in pat_h.finditer(t)]
    b = [m.group(0) for m in pat_pct.finditer(t)]
    c = [m.group(0) for m in pat_inword.finditer(t)]
    if a or b or c:
        print(f.name, "hyphen:", len(a), "percent:", len(b), "in-word:", len(c))
        for s in (a[:3] + b[:3] + c[:3]):
            print("    ", repr(s))
