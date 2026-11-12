"""List reference and arrow patterns in page_275..279.tex that need a check against the print."""
import pathlib
import re

R = pathlib.Path(__file__).resolve().parent.parent
pats = [
    ("paren-sref", r"\(\\sref"),
    ("sref-0", r"\\sref\[0\]\{[^}]*\}"),
    ("sref-label-after", r"\\sref(\[[^]]*\])?\{[^}]*\},~? ?\([ivx]+\)"),
    ("mapsto", r"\\mapsto"),
    ("Y(", r"Y'?\("),
    ("sh-J", r"\\sh\{J\}"),
    ("minus-set", r"[A-Z]_?\w*-[\\({A-Z]"),
    ("cdot", r"\\cdot"),
    ("cdots", r"\\cdots"),
    ("mathfrak", r"\\mathfrak\{[A-Za-z]+\}"),
]
for p in range(275, 280):
    t = (R / f"page_{p}.tex").read_text(encoding="utf-8")
    for name, pat in pats:
        for m in re.finditer(pat, t):
            line = t.count("\n", 0, m.start()) + 1
            ctx = t[max(0, m.start() - 30):m.end() + 30].replace("\n", " | ")
            print(p, line, name, ":", ctx)
