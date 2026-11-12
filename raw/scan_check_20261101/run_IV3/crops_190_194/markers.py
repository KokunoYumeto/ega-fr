"""Print the source context around \\oldpage[IV-3]{N} markers in ega4-13-fr.tex."""
import sys

sys.stdout.reconfigure(encoding='utf-8')
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions"
       r"\2026-10-24-r20\diplomatic\packages\IV3\native\ega4\ega4-13-fr.tex")
s = open(SRC, encoding='utf-8').read()
for n in sys.argv[1:]:
    key = 'oldpage[IV-3]{%s}' % n
    i = s.index(key)
    print('=====', n)
    print(repr(s[i - 170:i + 90]))
