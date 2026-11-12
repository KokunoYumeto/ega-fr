"""Count text lines that follow \\end{enumerate} without a blank line in the IV-3 diplomatic sources."""
import glob
import os

ROOT = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4"
total = 0
for f in sorted(glob.glob(os.path.join(ROOT, "ega4-*-fr.tex"))):
    lines = open(f, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    n = 0
    for i, line in enumerate(lines):
        if line.strip() != r"\end{enumerate}":
            continue
        j = i + 1
        while j < len(lines) and lines[j].startswith(r"\oldpage"):
            j += 1
        nxt = lines[j].strip() if j < len(lines) else ""
        if nxt and not nxt.startswith((r"\end{", r"\begin{", r"\[", "%")):
            n += 1
    total += n
    print(os.path.basename(f), n)
print("total", total)
