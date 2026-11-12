# -*- coding: utf-8 -*-
import os
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.join(os.path.dirname(RUN), "ega-fr", "editions", "2026-10-24-r20", "diplomatic",
                 "packages", "IV1", "native", "ega4")
s = open(os.path.join(R, "ega0-20-fr.tex"), encoding="utf-8").read()
N = "\n"
cands = [
    r"noyau $\mathfrak{Q}$" + N + "est de carré nul",
    "vérifiant" + N + "les conditions (i)",
    "et (ii) de",
    r"(ii) de \sref{0.20.1.1-fr}",
    r"\end{proof}" + N + N + r"\subsection{Propriétés",
    r"\subsection{Propriétés fonctorielles",
    r"des dérivations}",
    r"$\mathbf{Z}$-dérivation de $B$ dans $L$ \sref{0.20.1.5-fr}",
    r"une" + N + r"$\mathbf{Z}$-dérivation de $B$",
]
for c in cands:
    print(s.count(c), repr(c))
i = s.find(r"\subsection{Propriétés")
while i >= 0:
    print("subsection at", s.count(N, 0, i) + 1, repr(s[i:i + 70]))
    i = s.find(r"\subsection{Propriétés", i + 1)
