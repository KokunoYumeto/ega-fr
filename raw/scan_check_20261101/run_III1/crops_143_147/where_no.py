"""Locate 'no~' and the proof-part labels \\textit{(i)} etc. relative to the page markers of the diplomatic file."""
import pathlib
import re

t = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                 r"\packages\BASE\native\ega3\ega3-1-fr.tex").read_text(encoding="utf-8")
marks = [(m.start(), m.group(0)) for m in re.finditer(r"\\oldpage\[[^\]]*\]\{\d+\}", t)]


def page_of(pos):
    last = None
    for s, g in marks:
        if s <= pos:
            last = g
    return last


for pat in (r"no~\d", r"\\noindent\\textit\{\(?[ivxIV]+\)\}"):
    for m in re.finditer(pat, t):
        print(pat, "line", t.count("\n", 0, m.start()) + 1, "after", page_of(m.start()), repr(t[m.start():m.end() + 25]))
