import re
import os
d = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4"
BS = chr(92)
pat = re.compile(re.escape(BS + "oldpage[IV-3]{") + r"(\d+)\}")
for fn in ['ega4-11-fr.tex', 'ega4-12-fr.tex', 'ega4-13-fr.tex']:
    t = open(os.path.join(d, fn), encoding='utf-8').read()
    parts = pat.split(t)
    out = []
    for i in range(1, len(parts), 2):
        p = parts[i]
        body = parts[i + 1]
        out.append(f"{p}:{body.count(BS + 'emph{')}")
    print(fn, ' '.join(out))
