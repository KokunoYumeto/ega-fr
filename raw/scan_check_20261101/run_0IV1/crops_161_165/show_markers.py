# -*- coding: utf-8 -*-
"""Print the simulated text (all fixes applied) around each page marker."""
import pathlib
import re

t = (pathlib.Path(__file__).resolve().parent / "simulated_after_fixes.txt").read_text(encoding="utf-8")
for m in re.finditer(r"\\oldpage\[[^\]]*\]\{(\d+)\}", t):
    print("=== marker", m.group(1))
    print(t[max(0, m.start() - 200):m.end() + 160])
    print()
