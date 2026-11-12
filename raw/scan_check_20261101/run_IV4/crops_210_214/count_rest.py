"""Count \\mathfrak R, gr^* and env-wrapped numbered displays in ega4-18 after marker 215 (read-only)."""
import re

SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
t = open(SRC, encoding="utf-8").read()
s = t.index("\\oldpage[IV-4]{215}")
rest = t[s:]
marks = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", rest)]
print("pages after 215 in ega4-18:", marks[0][0], "...", marks[-1][0])
print("mathfrak R:", rest.count("\\mathfrak R"))
print("gr^* (operatorname{gr}_..^*):", len(re.findall(r"\\operatorname\{gr\}_\{[^}]*\}\^\*", rest)), "| all ^*:", rest.count("^*"))
print("env-wrapped displays:", re.findall(r"\\begin\{env\}\[([0-9.]+)\]\n\\label\{[^}]*\}\n\\\[", rest))
