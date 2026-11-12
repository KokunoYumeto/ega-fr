import re
import sys
sys.stdout.reconfigure(encoding="utf-8")
SRC = (r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
       r"diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex")
src = open(SRC, encoding="utf-8", newline="").read()
start = src.index(r"\oldpage[IV-4]{200}")
end = src.index(r"\oldpage[IV-4]{205}")


def report(name, pat):
    ms = list(re.finditer(pat, src))
    inside = [m for m in ms if start <= m.start() < end]
    after = [m for m in ms if m.start() >= end]
    before = [m for m in ms if m.start() < start]
    print("%-14s total %3d  before p200 %3d  on pp200-204 %3d  after p204 %3d" % (
        name, len(ms), len(before), len(inside), len(after)))


report("gr^*", r"\\operatorname\{gr\}(_\{[^}]*\})?\^\*")
report("S^*", r"\\mathbf\s*\{?S\}?_\{[^{}]*(\{[^{}]*\}[^{}]*)*\}\^\*")
report("^{\\#}", r"\^\{\\#\}")
report("\\mathbf k", r"\\mathbf\s*\{?k\}?")
report("\\mapsto", r"\\mapsto")
report("$0$, ref", r"\(\$0\$, ")
report("(I, ", r"\(I, ")
report("(II, ", r"\(II, ")
report("(III, ", r"\(III, ")
