import json, sys, os
sys.stdout.reconfigure(encoding='utf-8')

RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = os.path.join(RUN, "findings_061_065.json")
NL = "\u23ce"  # placeholder for a line break inside fix strings


def L(s):
    return None if s is None else s.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    d["fix"] = None if nofix else {"old": L(old), "new": L(new)}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


P = r"\oldpage[0\textsubscript{IV-1}]"
items = []

# ---------------- page 61 ----------------
items += [
F(61, r"top of p. 61: '... tel que l'on ait w(v(b')z)=b'w(z) et | w(zv(b'))=w(z)b' quels que soient ...'",
  r"p. 61 begins flush left inside the sentence begun on p. 60",
  r"blank lines before and after \oldpage{61}: paragraph break",
  "other", None, "high",
  P + r"{61}⏎⏎$w(zv(b'))=", P + r"{61}⏎$w(zv(b'))=",
  r"Spurious paragraph break at a page break inside a sentence (GLOBAL_ISSUES item 20). Apply together with the p. 60 entry that removes the blank line before the marker; it lies in page_060.tex (outside pp. 61-65): '$w(v(b')z)=b'w(z)$ et\n\n' -> '$w(v(b')z)=b'w(z)$ et\n'. \oldpage ends with \ignorespaces, so joining the lines leaves one space."),
F(61, r"(18.3.5.1)", r"(A, B, L) ⇝ Exan_A(B, L), wavy arrow",
  r"(A,B,L)\longmapsto\operatorname{Exan}_A(B,L)", "symbol", None, "high",
  r"(A,B,L)\longmapsto\operatorname{Exan}_A(B,L)", r"(A,B,L)\leadsto\operatorname{Exan}_A(B,L)",
  r"Wavy arrow, not a maps-to arrow (GLOBAL_ISSUES 33)."),
F(61, r"after (18.3.5.1): 'de la catégorie K dans la catégorie Ab'", r"K bold italic", r"$\mathbf K$ (bold upright)",
  "font", None, "high",
  r"catégorie $\mathbf K$ dans", r"catégorie $\boldsymbol{K}$ dans",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(61, r"after (18.3.5.1): 'dans la catégorie Ab des groupes commutatifs'", r"Ab bold italic", r"$\mathbf{Ab}$ (bold upright)",
  "font", None, "high",
  r"$\mathbf{Ab}$ des groupes", r"$\boldsymbol{Ab}$ des groupes",
  r"GLOBAL_ISSUES 53 (Ab bold italic in running text)."),
F(61, r"(18.3.5), after the display (u, v, w)_*: Exan_A(B, L) → Exan_{A'}(B', L'): 'En vertu de la définition des morphismes dans K'",
  r"new paragraph (indented line)", r"no blank line after \]",
  "other", None, "high",
  r"\]⏎En vertu de la définition", r"\]⏎⏎En vertu de la définition",
  r"Paragraph break as printed (GLOBAL_ISSUES 47)."),
F(61, r"(18.3.5): 'En vertu de la définition des morphismes dans K, on peut écrire'", r"K bold italic", r"$\mathbf K$",
  "font", None, "high",
  r"morphismes dans $\mathbf K$, on peut", r"morphismes dans $\boldsymbol{K}$, on peut",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(61, r"(18.3.6): 'si w : L→L' est un homomorphisme de B-bimodules, le diagramme'", r"'bimodules' italic",
  r"$B$-bimodules (upright)", "italics", None, "high",
  r"de $B$-bimodules, le diagramme", r"de $B$-\emph{bimodules}, le diagramme",
  r"Checked on an enlarged crop."),
F(61, r"(18.3.6.3), top right entry", r"Exan_{A'}(B', L)", r"\operatorname{Exan}_A(B',L)",
  "misprint_in_print", None, "high",
  r"\operatorname{Exan}_A(B',L)\ar[d]^{w_*}", r"\operatorname{Exan}_{A'}(B',L)\ar[d]^{w_*}",
  r"Misprint: the print's diagram has A' in both right-hand entries, but v^* goes to Exan_A(B', L) by (18.3.6.2) (the ring A is unchanged in (1_A, v, 1_L)). The TeX silently corrects it; the fix restores the printed reading.",
  corrected=r"\operatorname{Exan}_A(B',L)"),
F(61, r"(18.3.6.3), bottom right entry", r"Exan_{A'}(B', L')", r"\operatorname{Exan}_A(B',L')",
  "misprint_in_print", None, "high",
  r"\operatorname{Exan}_A(B',L')", r"\operatorname{Exan}_{A'}(B',L')",
  r"Same misprint as the top right entry; the TeX silently corrects it; the fix restores the printed reading.",
  corrected=r"\operatorname{Exan}_A(B',L')"),
F(61, r"end of p. 61: '... v^* est bien un homomorphisme de groupes.' followed by \end{env}",
  r"(18.3.6) continues on p. 62 ('Enfin, l'application ...'); 18.3.6.4 is there the number of a display, not a new heading",
  r"\end{env} closes (18.3.6) here; p. 62 opens \begin{env}[18.3.6.4]",
  "other", None, "high",
  r"\emph{homomorphisme de groupes}.⏎\end{env}", r"\emph{homomorphisme de groupes}.",
  r"Part 1 of 2: apply together with the p. 62 entry that turns \begin{env}[18.3.6.4] into the display number (18.3.6.4); the existing \end{env} after 'Z-\emph{module}.' on p. 62 then closes (18.3.6)."),
]

# ---------------- page 62 ----------------
items += [
F(62, r"top of p. 62: 'Enfin, l'application (u, 1_B, 1_L)_* est l'application / (18.3.6.4) u^*: Exan_A(B, L) → Exan_{A'}(B, L)'",
  r"'Enfin' starts an indented paragraph of (18.3.6); (18.3.6.4) is the number of the display that follows, like (18.3.6.1) and (18.3.6.2)",
  r"\begin{env}[18.3.6.4] (bold heading '(18.3.6.4)' before 'Enfin', no indent) and an unnumbered \[...\] display",
  "other", None, "high",
  r"\begin{env}[18.3.6.4]⏎\label{0.18.3.6.4-fr}⏎Enfin, l'application $(u,1_B,1_L)_*$ est l'application⏎\[⏎  u^*:\operatorname{Exan}_A(B,L)\longrightarrow⏎  \operatorname{Exan}_{A'}(B,L)⏎\]",
  r"Enfin, l'application $(u,1_B,1_L)_*$ est l'application⏎\begin{equation}⏎\label{0.18.3.6.4-fr}⏎\tag{18.3.6.4}⏎  u^*:\operatorname{Exan}_A(B,L)\longrightarrow⏎  \operatorname{Exan}_{A'}(B,L)⏎\end{equation}",
  r"Part 2 of 2: apply together with the p. 61 entry that deletes \end{env} after '\emph{homomorphisme de groupes}.'. The label keeps its name and now carries the tag; the blank lines around \oldpage{62} are a real paragraph break here."),
F(62, r"(18.3.6): 'que l'on a (u∘u', v∘v', w'∘w)_* = (u', v', w')_*∘(u, v, w)_*, ce qui achève'",
  r"formula set inline in the running text", r"displayed with \[...\]",
  "other", None, "high",
  r"que l'on a⏎\[⏎  (u\circ u',v\circ v',w'\circ w)_*⏎  =(u',v',w')_*\circ(u,v,w)_*,⏎\]⏎ce qui achève",
  r"que l'on a $(u\circ u',v\circ v',w'\circ w)_*=(u',v',w')_*\circ(u,v,w)_*$,⏎ce qui achève",
  r"Layout only (display vs inline, GLOBAL_ISSUES 21); the formula itself matches."),
F(62, r"(18.3.6): 'ce qui achève de prouver que (18.3.4.1) est un foncteur'", r"(18.3.4.1)",
  r"(18.3.4.1), the printed reading", "misprint_in_print", None, "high",
  None, None,
  r"Misprint: the functor (A, B, L) ⇝ Exan_A(B, L) is (18.3.5.1) on p. 61; (18.3.4) has no subnumber .1. The TeX keeps the printed reading.",
  corrected=r"(18.3.5.1)", nofix=True),
F(62, r"(18.3.6): 'l'homothétie h_z : y ⇝ yz = zy'", r"wavy arrow", r"$h_z:y\mapsto yz=zy$",
  "symbol", None, "high",
  r"$h_z:y\mapsto yz=zy$", r"$h_z:y\leadsto yz=zy$",
  r"Wavy arrow (GLOBAL_ISSUES 33); checked on an enlarged crop."),
F(62, r"end of p. 62 / top of p. 63: '... (18.3.7.1) [diagram] | on en déduit canoniquement des homomorphismes'",
  r"p. 63 begins flush left inside the sentence", r"blank line after \end{equation}, before \oldpage{63}",
  "other", None, "high",
  r"& A\ar[u]⏎  }⏎\end{equation}⏎⏎", r"& A\ar[u]⏎  }⏎\end{equation}⏎",
  r"Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Apply together with the p. 63 entry that removes the blank line after \oldpage{63}."),
]

# ---------------- page 63 ----------------
items += [
F(63, r"top of p. 63: 'on en déduit canoniquement des homomorphismes'", r"flush left, continues the sentence of p. 62",
  r"blank line after \oldpage{63}", "other", None, "high",
  P + r"{63}⏎⏎on en déduit", P + r"{63}⏎on en déduit",
  r"Apply together with the p. 62 entry '& A\ar[u] ... \end{equation}' (blank line before the marker)."),
F(63, r"Proposition (18.3.8): 'On définit alors un isomorphisme canonique de groupes commutatifs'",
  r"'isomorphisme' roman inside the italic statement", r"italic like the rest of the statement",
  "convention", 6, "high",
  r"un isomorphisme canonique", r"un \textup{isomorphisme} canonique",
  r"Checked on an enlarged crop."),
F(63, r"Proposition (18.3.8): '(qui est a fortiori un B-homomorphisme)'",
  r"the parenthesis is roman, 'a fortiori' italic", r"italic parenthesis with an upright \emph{a fortiori}",
  "convention", 6, "high",
  r"(qui est \emph{a fortiori} un⏎$B$-homomorphisme)", r"\textup{(qui est \emph{a fortiori} un⏎$B$-homomorphisme)}",
  r"Inside \textup the \emph gives italic, as printed."),
F(63, r"proof of (18.3.8): 'Pour toute B-extension 0 → L →j E →p C → 0 de C par L'",
  r"exact sequence set inline", r"displayed with \[...\]",
  "other", None, "high",
  r"Pour toute $B$-extension⏎\[⏎  0\longrightarrow L\xrightarrow{j}E\xrightarrow{p}C\longrightarrow0⏎\]⏎de $C$ par $L$",
  r"Pour toute $B$-extension⏎$0\to L\xrightarrow{j}E\xrightarrow{p}C\to0$⏎de $C$ par $L$",
  r"Layout only (display vs inline, GLOBAL_ISSUES 21); the formula itself matches."),
F(63, r"proof of (18.3.8), first diagram (0 → J/J² → F → C → 0 over 0 → L → E → C → 0), vertical arrows",
  r"labels w and u left of their arrows; ≀ left of the 1_C arrow, 1_C right of it",
  r"\ar[d]^w and \ar[d]^u (labels right); ≀ written \ar@{}[d]|{\wr}, which centres it on the arrow line",
  "other", None, "high",
  r"\mathfrak J/\mathfrak J^2\ar[r]\ar[d]^w⏎      & F\ar[r]^g\ar[d]^u⏎      & C\ar[r]\ar[d]^{1_C}\ar@{}[d]|{\wr} & 0\\",
  r"\mathfrak J/\mathfrak J^2\ar[r]\ar[d]_w⏎      & F\ar[r]^g\ar[d]_u⏎      & C\ar[r]\ar[d]^{1_C}_{\wr} & 0\\",
  r"Label sides (cf. GLOBAL_ISSUES 30), checked on an enlarged crop. One edit because the C line also occurs in the second diagram."),
F(63, r"proof of (18.3.8), after the first diagram: 'autrement dit (u, 1_C, w) est un morphisme d'extensions'",
  r"flush left: the sentence continues after the diagram", r"blank line after \]: paragraph break",
  "other", None, "high",
  r"\]⏎⏎autrement dit", r"\]⏎autrement dit",
  r"The print has no paragraph break here."),
F(63, r"proof of (18.3.8), second diagram, L column", r"1_L left of the arrow, ≀ right of it",
  r"\ar[d]^{1_L} (label right) and ≀ centred on the arrow (\ar@{}[d]|{\wr})",
  "other", None, "high",
  r"L\ar[r]\ar[d]^{1_L}\ar@{}[d]|{\wr}", r"L\ar[r]\ar[d]_{1_L}^{\wr}",
  r"Label sides, checked on an enlarged crop."),
F(63, r"proof of (18.3.8), second diagram, bottom row 0 → L → E → C → 0", r"bottom arrows without labels",
  r"\ar[r]_j and \ar[r]_p: labels j, p added", "extra", None, "high",
  r"& E'\ar[r]\ar[d]^{u'}⏎      & C\ar[r]\ar[d]^{1_C}\ar@{}[d]|{\wr} & 0\\⏎    0\ar[r] & L\ar[r]_j & E\ar[r]_p & C\ar[r] & 0⏎  }⏎\]⏎⏎",
  r"& E'\ar[r]\ar[d]^{u'}⏎      & C\ar[r]\ar[d]^{1_C}_{\wr} & 0\\⏎    0\ar[r] & L\ar[r] & E\ar[r] & C\ar[r] & 0⏎  }⏎\]⏎",
  r"One edit for the last lines of the page (the bottom row and the C line are identical in both diagrams, so 'old' needs the u' line): it also sets ≀ left of the 1_C arrow and removes the blank line before \oldpage{64} (the next two findings)."),
F(63, r"proof of (18.3.8), second diagram, C column", r"≀ left of the 1_C arrow",
  r"≀ centred on the arrow (\ar@{}[d]|{\wr})", "other", None, "high",
  None, None, r"Fix included in the j/p edit above.", nofix=True),
F(63, r"end of p. 63 / top of p. 64: '... morphisme d'extensions [diagram] | où E' = F⊕L (18.2.8)'",
  r"p. 64 begins flush left inside the sentence", r"blank line after \], before \oldpage{64}",
  "other", None, "high",
  None, None,
  r"Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Fix included in the j/p edit above; apply that edit together with the p. 64 entry that removes the blank line after \oldpage{64}.",
  nofix=True),
]

# ---------------- page 64 ----------------
items += [
F(64, r"top of p. 64: 'où E' = F⊕_(J/J²)L (18.2.8)'", r"flush left, continues the sentence of p. 63",
  r"blank line after \oldpage{64}", "other", None, "high",
  P + r"{64}⏎⏎où $E'=", P + r"{64}⏎où $E'=",
  r"Apply together with the p. 63 j/p edit, which removes the blank line before the marker."),
F(64, r"proof of (18.3.8): 'que l'image réciproque G ... est F-triviale'", r"'triviale' italic",
  r"$F$-triviale (upright)", "italics", None, "high",
  r"est $F$-triviale", r"est $F$-\emph{triviale}", r"Checked on an enlarged crop."),
F(64, r"proof of (18.3.8), diagram, top arrow Hom_C(J/J², L) → Exan_B(C, L)",
  r"isomorphism arrow: η_L above a tilde above the arrow",
  r"\ar[r]^{\eta_L}: no tilde", "symbol", None, "high",
  r"\ar[r]^{\eta_L}\ar[d]", r"\ar[r]^{\overset{\eta_L}{\sim}}\ar[d]",
  r"Same form as an earlier page fix (\ar[r]^{\overset{\eta_V}{\sim}}). The bottom arrow \ar[r]_{\eta_{L'}}^{\sim} (tilde above, η_{L'} below) matches the print."),
F(64, r"subsection heading 18.4", r"'18.4. Extensions d'algèbres.' (final full stop)",
  r"\subsection{Extensions d'algèbres} (no full stop)", "punctuation", None, "high",
  r"\subsection{Extensions d'algèbres}", r"\subsection{Extensions d'algèbres.}",
  r"GLOBAL_ISSUES 43/57 (subsection titles without the printed full stop)."),
F(64, r"(18.4.1): 'Soit K' la sous-catégorie pleine'", r"K' bold italic", r"$\mathbf K'$",
  "font", None, "high",
  r"$\mathbf K'$ la sous-catégorie", r"$\boldsymbol{K}'$ la sous-catégorie",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(64, r"(18.4.1): 'de la catégorie K définie dans (18.3.5)'", r"K bold italic", r"$\mathbf K$",
  "font", None, "high",
  r"catégorie $\mathbf K$ définie", r"catégorie $\boldsymbol{K}$ définie",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(64, r"(18.4.1), display (A, B, L) ⇝ Exal_A(B, L)", r"wavy arrow",
  r"(A,B,L)\longmapsto\operatorname{Exal}_A(B,L)", "symbol", None, "high",
  r"(A,B,L)\longmapsto\operatorname{Exal}_A(B,L)", r"(A,B,L)\leadsto\operatorname{Exal}_A(B,L)",
  r"Wavy arrow (GLOBAL_ISSUES 33)."),
F(64, r"(18.4.1): 'est un foncteur covariant de K' dans Ab'", r"K' bold italic", r"$\mathbf K'$",
  "font", None, "high",
  r"covariant} de $\mathbf K'$", r"covariant} de $\boldsymbol{K}'$",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(64, r"(18.4.1): 'de K' dans Ab. Les résultats'", r"Ab bold italic", r"$\mathbf{Ab}$",
  "font", None, "high",
  r"dans $\mathbf{Ab}$. Les", r"dans $\boldsymbol{Ab}$. Les",
  r"GLOBAL_ISSUES 53."),
F(64, r"end of p. 64 / top of p. 65: '... et L un B-module, | les classes de A-extensions équivalentes'",
  r"p. 65 begins flush left inside the sentence", r"blank line before \oldpage{65}",
  "other", None, "high",
  r"$L$ un⏎$B$-module,⏎⏎", r"$L$ un⏎$B$-module,⏎",
  r"Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Apply together with the p. 65 entry that removes the blank line after \oldpage{65}."),
]

# ---------------- page 65 ----------------
items += [
F(65, r"top of p. 65: 'les classes de A-extensions équivalentes de B par L'", r"flush left, continues the sentence of p. 64",
  r"blank line after \oldpage{65}", "other", None, "high",
  P + r"{65}⏎⏎les classes", P + r"{65}⏎les classes",
  r"Apply together with the p. 64 entry '$L$ un\n$B$-module,\n\n'."),
F(65, r"(18.4.2): 'Si K'' est la sous-catégorie pleine'", r"K'' bold italic", r"$\mathbf K''$",
  "font", None, "high",
  r"$\mathbf K''$ est la", r"$\boldsymbol{K}''$ est la",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(65, r"(18.4.2): 'pleine de K' formée des triplets'", r"K' bold italic", r"$\mathbf K'$",
  "font", None, "high",
  r"pleine de $\mathbf K'$ formée", r"pleine de $\boldsymbol{K}'$ formée",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(65, r"(18.4.2), display (A, B, L) ⇝ Exalcom_A(B, L)", r"wavy arrow",
  r"(A,B,L)\longmapsto\operatorname{Exalcom}_A(B,L)", "symbol", None, "high",
  r"(A,B,L)\longmapsto\operatorname{Exalcom}_A(B,L)", r"(A,B,L)\leadsto\operatorname{Exalcom}_A(B,L)",
  r"Wavy arrow (GLOBAL_ISSUES 33)."),
F(65, r"(18.4.2): 'foncteur covariant de K'' dans Ab'", r"K'' bold italic", r"$\mathbf K''$",
  "font", None, "high",
  r"covariant} de $\mathbf K''$", r"covariant} de $\boldsymbol{K}''$",
  r"Category letter bold italic (GLOBAL_ISSUES 18)."),
F(65, r"(18.4.2): 'de K'' dans Ab. On peut aussi'", r"Ab bold italic", r"$\mathbf{Ab}$",
  "font", None, "high",
  r"dans $\mathbf{Ab}$. On", r"dans $\boldsymbol{Ab}$. On",
  r"GLOBAL_ISSUES 53."),
F(65, r"(18.4.3): 'la suite exacte de A-modules 0→E→L→B→0 est scindée'", r"0→E→L→B→0",
  r"$0\to L\to E\to B\to0$", "misprint_in_print", None, "high",
  r"$0\to L\to E\to B\to0$", r"$0\to E\to L\to B\to0$",
  r"Misprint: E is the extension of B by L, so the sequence is 0→L→E→B→0. Checked on an enlarged crop. The TeX silently corrects it; the fix restores the printed reading.",
  corrected=r"$0\to L\to E\to B\to0$"),
F(65, r"(18.4.3.1), end of the display", r"no punctuation after f(x, yz)",
  r"comma after f(x,yz)", "punctuation", None, "high",
  r"+f(x,yz),⏎\end{equation}", r"+f(x,yz)⏎\end{equation}",
  r"Checked on an enlarged crop."),
F(65, r"(18.4.3.2): 'f(x, y) = xg(y) — g(xy) + g(x)y'", r"long dash for the subtraction",
  r"minus sign", "convention", 7, "high",
  r"xg(y)-g(xy)", r"xg(y)\setmin g(xy)",
  r"Long dash used for a subtraction (GLOBAL_ISSUES 23); \setmin as proposed for convention 7, pending that decision (the IV1 preamble has \providecommand{\setmin}{-})."),
F(65, r"(18.4.3.2), end of the display", r"no punctuation after g(x)y",
  r"comma after g(x)y", "punctuation", None, "high",
  r"+g(x)y,⏎\end{equation}", r"+g(x)y⏎\end{equation}",
  r"Checked on an enlarged crop."),
F(65, r"(18.4.4): 'On considère un complexe P_• = (P_n)_{n⩾0} de B-modules'", r"P roman (not bold), like the B beside it",
  r"$\mathbf P_\bullet=(\mathbf P_n)_{n\geqslant0}$ (bold P)", "font", None, "medium",
  r"$\mathbf P_\bullet=(\mathbf P_n)_{n\geqslant0}$", r"$P_\bullet=(P_n)_{n\geqslant0}$",
  r"Measured on the strip: the stem of P is as wide as that of the roman B in the same line (6 px), the bold heading figures about 9 px. On p. 66 (d_n : P_n → P_{n-1}) the P is roman too; ega0-18-fr.tex has 18 \mathbf P."),
F(65, r"(18.4.4): 'où P_n = B^{⊗(n+1)} = ...'", r"P roman (not bold)", r"$\mathbf P_n$",
  "font", None, "medium",
  r"$\mathbf P_n=B^{\otimes(n+1)}", r"$P_n=B^{\otimes(n+1)}",
  r"As the previous finding."),
F(65, r"(18.4.4): 'B⊗_A B⊗ . . . ⊗_A B (n+1 fois)'", r"second ⊗ without the subscript A",
  r"B\otimes_A B\otimes_A\cdots\otimes_A B", "misprint_in_print", None, "medium",
  r"B\otimes_A B\otimes_A", r"B\otimes_A B\otimes",
  r"Misprint (omitted subscript), checked on an enlarged crop: the print has ⊗_A before and after the dots but a bare ⊗ after the second B. The TeX silently corrects it; the fix restores the printed reading. Does not overlap the dots fix (adjacent strings).",
  corrected=r"B\otimes_A B\otimes_A"),
F(65, r"(18.4.4): 'B⊗_A B⊗ . . . ⊗_A B'", r"baseline dots", r"\cdots",
  "symbol", None, "high",
  r"\cdots\otimes_A B$", r"\ldots\otimes_A B$",
  r"Baseline dots (GLOBAL_ISSUES 22/57)."),
F(65, r"end of p. 65 / top of p. 66: '... la structure de B-module étant définie | par x(y_1⊗...)'",
  r"p. 66 begins flush left inside the sentence", r"blank line before \oldpage{66}",
  "other", None, "high",
  r"étant définie⏎⏎", r"étant définie⏎",
  r"Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Apply together with the p. 66 entry (page_066.tex, outside pp. 61-65): '\oldpage[0\textsubscript{IV-1}]{66}\n\npar' -> '\oldpage[0\textsubscript{IV-1}]{66}\npar' (p. 66 begins flush left with 'par x(y_1⊗...)')."),
]

# ---------------- checks ----------------
texts = {}
for p in sorted({it['page'] for it in items}):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        texts[p] = fh.read().replace('\r\n', '\n')

ok = True
spans = {}
for i, it in enumerate(items):
    fx = it['fix']
    if fx is None:
        continue
    t = texts[it['page']]
    c = t.count(fx['old'])
    if c != 1:
        ok = False
        print('NOT UNIQUE (%d): p.%d %r' % (c, it['page'], fx['old'][:80]))
    else:
        s = t.index(fx['old'])
        spans.setdefault(it['page'], []).append((s, s + len(fx['old']), i))
for p, sp in spans.items():
    sp.sort()
    for a, b in zip(sp, sp[1:]):
        if a[1] > b[0]:
            ok = False
            print('OVERLAP on p.%d: items %d and %d' % (p, a[2], b[2]))
# sequential application check
for p in texts:
    t = texts[p]
    for it in items:
        if it['page'] != p or it['fix'] is None:
            continue
        c = t.count(it['fix']['old'])
        if c != 1:
            ok = False
            print('SEQUENTIAL FAIL p.%d %r count %d' % (p, it['fix']['old'][:60], c))
        t = t.replace(it['fix']['old'], it['fix']['new'], 1)

from collections import Counter
cnt = Counter()
for it in items:
    k = 'misprint' if it['kind'] == 'misprint_in_print' else ('convention' if it['kind'] == 'convention' else 'normal')
    cnt[(it['page'], k)] += 1
for p in sorted(texts):
    print(p, cnt[(p, 'normal')], cnt[(p, 'convention')], cnt[(p, 'misprint')])
print('ALL UNIQUE' if ok else 'PROBLEMS')
if ok:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(items, fh, ensure_ascii=False, indent=1)
    print('written', OUT, len(items))
