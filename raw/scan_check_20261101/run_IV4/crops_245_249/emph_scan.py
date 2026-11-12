import io
import re

SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
       r"\diplomatic\packages\IV4\native\ega4\ega4-20-fr.tex")
lines = io.open(SRC, encoding="utf-8").read().split("\n")
env = None
beg = re.compile(r"\\begin\{(proposition|corollary|theorem|lemma|definition)\}")
end = re.compile(r"\\end\{(proposition|corollary|theorem|lemma|definition)\}")
page = None
for i, l in enumerate(lines, 1):
    m = re.search(r"\\oldpage\[IV-4\]\{(\d+)\}", l)
    if m:
        page = m.group(1)
    if beg.search(l):
        env = beg.search(l).group(1)
    if end.search(l):
        env = None
    if env and l.startswith("\\emph{"):
        print(i, "p.", page, env, l[:70])
