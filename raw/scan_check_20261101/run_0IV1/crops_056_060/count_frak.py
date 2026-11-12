import os
B = r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4'
R = chr(92) + 'mathfrak{R}'
K = chr(92) + 'mathfrak{K}'
for f in ['ega0-18-fr.tex', 'ega0-20-fr.tex']:
    s = open(os.path.join(B, f), encoding='utf-8').read()
    print(f, 'R:', s.count(R), 'K:', s.count(K))
s = open(os.path.join(B, 'ega0-18-fr.tex'), encoding='utf-8').read()
m = chr(92) + 'oldpage[0' + chr(92) + 'textsubscript{IV-1}]{%d}'
i = s.find(m % 56); j = s.find(m % 57)
print('p56 segment R:', s[i:j].count(R), '| after p57 marker R:', s[j:].count(R), '| before p56 marker R:', s[:i].count(R))
# where are the R after p57?
import re
pos = [mm.start() for mm in re.finditer(re.escape(R), s)]
marks = [(mm.start(), mm.group(1)) for mm in re.finditer(re.escape(chr(92) + 'oldpage[0' + chr(92) + 'textsubscript{IV-1}]{') + r'(\d+)\}', s)]
def page_of(p):
    pg = None
    for a, n in marks:
        if a <= p:
            pg = n
    return pg
from collections import Counter
print(Counter(page_of(p) for p in pos))
