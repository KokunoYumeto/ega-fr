"""Count how page markers sit relative to environment openings in a TeX file.
usage: python marker_pattern.py FILE.tex"""
import re
import sys

t = open(sys.argv[1], encoding="utf-8").read()
before = re.findall(r"\\oldpage\[[^\]]*\]\{\d+\}\n\\begin\{(\w+)\}", t)
after = re.findall(r"\\begin\{(\w+)\}(?:\[[^\]]*\])?\n\\label\{[^}]*\}\n\\oldpage\[[^\]]*\]\{(\d+)\}", t)
print("marker directly before \\begin:", len(before))
print("marker directly after \\begin+\\label:", len(after), after[:20])
