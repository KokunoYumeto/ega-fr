# -*- coding: utf-8 -*-
"""Report how often each fix's 'old' occurs in the release source files (information only)."""
import json
import os
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(os.path.dirname(RUN), "ega-fr", "editions", "2026-10-24-r20", "diplomatic",
                 "packages", "IV1", "native", "ega4")
src = {f: open(os.path.join(R, f), encoding="utf-8").read() for f in ("ega0-19b-fr.tex", "ega0-20-fr.tex")}
L = json.load(open(os.path.join(RUN, "findings_116_120.json"), encoding="utf-8"))
for d in L:
    if not d["fix"]:
        continue
    o = d["fix"]["old"]
    c = {f: s.count(o) for f, s in src.items()}
    flag = "" if sum(c.values()) == 1 else "  <-- not unique in files"
    print(d["page"], c["ega0-19b-fr.tex"], c["ega0-20-fr.tex"], repr(o)[:60], flag)
