import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
S = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages"
     r"\IV2\native\ega4\ega4-2-fr.tex")
t = open(S, encoding="utf-8").read()
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-2\]\{(\d+)\}", t)]


def page(pos):
    p = None
    for n, s in cuts:
        if s <= pos:
            p = n
        else:
            break
    return p


c = Counter()
for m in re.finditer(r"\\overline\{[A-Za-z](?:'|_|\^)[^}]*\}", t):
    c[(page(m.start()), m.group(0))] += 1
for k, v in sorted(c.items()):
    print(k, v)
