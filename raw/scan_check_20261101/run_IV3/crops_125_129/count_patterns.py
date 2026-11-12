import glob
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
D = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4"
lab = re.compile(r"\\textbf\{[IVX]+\)\}")
gr = re.compile(r"\\operatorname\{gr\}(_\{(?:[^{}]|\{[^{}]*\})*\}|_\\?\w+)?\^\*")
gr2 = re.compile(r"\\operatorname\{gr\}\^\*")
for f in sorted(glob.glob(D + r"\ega4-*.tex")):
    t = open(f, encoding="utf-8").read()
    a, b, c = len(lab.findall(t)), len(gr.findall(t)), len(gr2.findall(t))
    if a or b or c:
        print(f.split("\\")[-1], "bold labels", a, "gr_..^*", b, "of which gr^*_", c)
