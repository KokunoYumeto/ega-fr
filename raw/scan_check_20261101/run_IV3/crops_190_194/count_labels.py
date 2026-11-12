"""Count math-mode letter labels such as $a)$ or $b')$ in the IV-3 source files."""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
D = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions"
     r"\2026-10-24-r20\diplomatic\packages\IV3\native\ega4" + "\\")
pat = re.compile(r"\$[a-e]'*\)\$")
for n in range(8, 16):
    s = open(D + 'ega4-%d-fr.tex' % n, encoding='utf-8').read()
    print('ega4-%d-fr.tex' % n, len(pat.findall(s)))
