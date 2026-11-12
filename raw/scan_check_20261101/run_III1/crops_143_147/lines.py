"""Print the line numbers (in the diplomatic ega3-1-fr.tex) of the p. 143 marker edit."""
import pathlib

t = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                 r"\packages\BASE\native\ega3\ega3-1-fr.tex").read_text(encoding="utf-8")
i = t.find("si on suppose $f_z$ fini")
j = t.find(r"\oldpage[III]{143}")
k = t.find("Pour traiter le cas", j)
print("start line", t.count("\n", 0, i) + 1, "marker line", t.count("\n", 0, j) + 1, "end line", t.count("\n", 0, k) + 1)
print(repr(t[i - 40:k + 20]))
