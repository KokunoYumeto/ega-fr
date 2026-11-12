"""Show the raw text around the page markers of 0_III pages 15-20 in the release file."""
import pathlib
import sys

REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\BASE\native\ega3\ega3-1-fr.tex")
t = REL.read_text(encoding="utf-8")
for n in range(15, 21):
    key = "\\oldpage[0\\textsubscript{III}]{%d}" % n
    s = t.find(key)
    print("== page", n, "count", t.count(key))
    print(repr(t[s - 150:s + 100]))
