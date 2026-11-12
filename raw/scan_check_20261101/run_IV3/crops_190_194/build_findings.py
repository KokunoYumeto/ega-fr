"""Build findings_190_194.json and check that every fix's old string occurs exactly once.

The pilcrow ¶ stands for a line break (LF) in old/new/corrected strings.
"""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = RUN + r"\findings_190_194.json"
NL = '¶'


def F(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    d = {
        'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
        'convention': conv, 'confidence': conf,
        'fix': None if old is None else {'old': old.replace(NL, '\n'), 'new': new.replace(NL, '\n')},
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected.replace(NL, '\n') if corrected is not None else None
    d['note'] = note
    return d


B = 'bold italic k'
P = 'plain k'
R6 = 'italic (statement environment)'
L = []

# ---------------- page 189 (outside this batch) ----------------
L.append(F(189,
    "end of page_189.tex, just before \\oldpage[IV-3]{190}: '... une A-algèbre de type fini, donc de la forme | B=A[T_1,...,T_n]/𝔍. Soit ...'",
    "printed p. 190 begins 'B=A[T_1, ..., T_n]/𝔍. Soit (𝔍_λ) la famille ...' flush left: the sentence of p. 189 runs on, no paragraph break",
    "blank line after 'donc de la forme', just before \\oldpage[IV-3]{190}: a paragraph break mid-sentence",
    'marker', None, 'high',
    r"donc de la forme¶¶", r"donc de la forme¶",
    "OUTSIDE pp. 190-194: 'old' lies at the end of page_189.tex (ega4-13-fr.tex, just before the p. 190 marker; no blank line follows the marker). The pp. 185-189 batch may file the same edit; apply it once. The marker position itself is right."))

# ---------------- page 190 ----------------
L.append(F(190, "Corollaire (13.1.4): 'Sous les hypothèses de (13.1.3), l'ensemble des x∈X ...'",
    "the reference (13.1.3) upright in the italic statement", R6, 'convention', 6, 'high',
    r"hypothèses de (13.1.3), l'ensemble", r"hypothèses de \textup{(13.1.3)}, l'ensemble"))
L.append(F(190, "Corollaire (13.1.5): 'Sous les hypothèses de (13.1.3), supposons en outre que f soit'",
    "the reference (13.1.3) upright in the italic statement", R6, 'convention', 6, 'high',
    r"(13.1.3), supposons", r"\textup{(13.1.3)}, supposons"))
L.append(F(190, "Corollaire (13.1.5): 'autrement dit, l'application y⇝dim(f^{-1}(y)) est semi-continue supérieurement'",
    "wavy arrow ⇝ (enlarged crop p190_wavy.png)", "\\mapsto", 'symbol', None, 'high',
    r"$y\mapsto\dim(f^{-1}(y))$", r"$y\leadsto\dim(f^{-1}(y))$",
    "GLOBAL_ISSUES 33; same fix as the wavy arrows of p. 59 (s⇝dim(f^{-1}(s)))."))
L.append(F(190, "Corollaire (13.1.6): 'Soit ξ (resp. η) le point générique de X'",
    "'(resp. η)': 'resp.' and the parentheses roman in the italic statement (enlarged crop p190_resp.png)", R6, 'convention', 6, 'high',
    r"(resp. $\eta$)", r"\textup{(resp. $\eta$)}"))
L.append(F(190, "Corollaire (13.1.6): 'de X (resp. Y) et soit e=dim(f^{-1}(η))'",
    "'(resp. Y)' roman in the italic statement (same crop)", R6, 'convention', 6, 'high',
    r"(resp. $Y$)", r"\textup{(resp. $Y$)}"))
L.append(F(190, "proof of (13.1.7): 'pour tout y∈Y, B⊗_A k(y) est une ...'", B, P, 'convention', 1, 'high',
    r"$B\otimes_Ak(y)$", r"$B\otimes_A\boldsymbol{k}(y)$"))
L.append(F(190, "proof of (13.1.7): 'est une k(y)-algèbre admettant n générateurs'", B, P, 'convention', 1, 'high',
    r"$k(y)$-algèbre", r"$\boldsymbol{k}(y)$-algèbre"))
L.append(F(190, "subsection heading 13.2",
    "'13.2. Morphismes équidimensionnels : cas des morphismes dominants de préschémas irréductibles.' (final full stop)",
    "no full stop", 'punctuation', None, 'high',
    r"de préschémas irréductibles}", r"de préschémas irréductibles.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))
L.append(F(190, "(13.2.1): 'f : X→Y un morphisme dominant localement de type fini; soit η ...'",
    "'dominant' in italics in the roman paragraph", "'dominant' upright", 'italics', None, 'high',
    r"un morphisme dominant localement de type fini~;", r"un morphisme \emph{dominant} localement de type fini~;"))

# ---------------- page 191 ----------------
L.append(F(191, "Définition (13.2.2), l. 1: 'Sous les hypothèses de (13.2.1), on dit que f est ...'",
    "the reference (13.2.1) upright in the italic statement", R6, 'convention', 6, 'high',
    r"hypothèses de (13.2.1), on dit", r"hypothèses de \textup{(13.2.1)}, on dit"))
L.append(F(191, "Définition (13.2.2), l. 1-2: 'on dit que f est équidimensionnel au point x'",
    "the defined term 'équidimensionnel au point' roman in the italic statement (enlarged crop p191_def_l12.png)", R6,
    'convention', 6, 'high',
    r"$f$ est équidimensionnel au point¶$x$ (ou", r"$f$ est \textup{équidimensionnel au point}¶$x$ (ou",
    "The parentheses, 'ou que', 'est' and 'si' are italic in the print (crops p191_paren_*.png)."))
L.append(F(191, "Définition (13.2.2), l. 2: '(ou que X est équidimensionnel sur Y au point x) si'",
    "'équidimensionnel sur Y au point' roman in the italic statement (same crop)", R6, 'convention', 6, 'high',
    r"est équidimensionnel sur $Y$ au point $x$) si", r"est \textup{équidimensionnel sur $Y$ au point} $x$) si"))
L.append(F(191, "Définition (13.2.2), second sentence: 'On dit que f est équidimensionnel (ou que'",
    "'équidimensionnel' roman in the italic statement (enlarged crop p191_def_l45.png)", R6, 'convention', 6, 'high',
    r"On dit que $f$ est équidimensionnel (ou", r"On dit que $f$ est \textup{équidimensionnel} (ou"))
L.append(F(191, "Définition (13.2.2), second sentence: '(ou que X est équidimensionnel sur Y) si f est ...'",
    "'équidimensionnel sur Y' roman in the italic statement (same crop)", R6, 'convention', 6, 'high',
    r"est équidimensionnel sur $Y$)¶si", r"est \textup{équidimensionnel sur $Y$})¶si",
    "The end of the sentence, 'si f est équidimensionnel en tout point x∈X', is italic in the print, as in the TeX."))
L.append(F(191, "Proposition (13.2.3), l. 2: 'f : X→Y un morphisme dominant localement de type fini'",
    "'dominant' roman in the italic statement (enlarged crop p191_prop1323_top.png)", R6, 'convention', 6, 'high',
    r"morphisme dominant localement", r"morphisme \textup{dominant} localement"))
L.append(F(191, "Proposition (13.2.3), display (13.2.3.1): 'dim(O_x⊗_{O_y} k(y))'", B, P, 'convention', 1, 'high',
    r"\otimes_{\mathcal O_y}k(y)", r"\otimes_{\mathcal O_y}\boldsymbol{k}(y)"))
L.append(F(191, "Proposition (13.2.3): 'si les deux membres de l'inégalité (5.6.5.2) sont égaux'",
    "the reference (5.6.5.2) upright in the italic statement (enlarged crop p191_prop1323_end.png)", R6,
    'convention', 6, 'high',
    r"l'inégalité (5.6.5.2) sont égaux", r"l'inégalité \textup{(5.6.5.2)} sont égaux"))
L.append(F(191, "(13.2.4), after the display (13.2.4.1): 'La formule (5.6.5.2) appliquée au morphisme dominant f' ...'",
    "'La formule' begins a new, indented paragraph", "no blank line after \\]: the text continues the paragraph, unindented",
    'other', None, 'high',
    r"\]¶La formule (5.6.5.2)", r"\]¶¶La formule (5.6.5.2)",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47)."))
L.append(F(191, "display (13.2.4.2): 'dim(B')≤dim(A')+dim(B'⊗_{A'} k(y))—(...)'", B, P, 'convention', 1, 'high',
    r"\label{IV.13.2.4.2-fr}¶  \dim(B')\leq\dim(A')+\dim(B'\otimes_{A'}k(y))",
    r"\label{IV.13.2.4.2-fr}¶  \dim(B')\leq\dim(A')+\dim(B'\otimes_{A'}\boldsymbol{k}(y))",
    "'old' starts at the label because the same first line recurs in (13.2.4.4)."))
L.append(F(191, "display (13.2.4.2): '...k(y))—(dim_x(f'^{-1}(y))—dim(f'^{-1}(η')))'",
    "two long dashes for the subtractions: 42 and 41 px wide against 35 px for the plus sign of the same display (measured; enlarged crop p191_13242.png)",
    "minus signs", 'convention', 7, 'high',
    r"-(\dim_x(f'^{-1}(y))-\dim", r"\setmin(\dim_x(f'^{-1}(y))\setmin\dim",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7). Two occurrences, one edit; the exponents -1 keep their minus signs."))
L.append(F(191, "end of display (13.2.4.2), before 'D'autre part, l'anneau local A' ...'",
    "no full stop after the closing parentheses '(η')))' (enlarged crop p191_13242_end.png); the display reaches the right margin",
    "'(\\eta')))' followed by a full stop: silently corrected", 'misprint_in_print', None, 'medium',
    r"(\eta')))." , r"(\eta')))",
    "The next sentence begins 'D'autre part'; the other displays of the page, (13.2.4.1) and (13.2.4.3)-(13.2.4.5), end with a full stop. The corrected edition (r20 current) has the full stop. Listed after the convention-7 edit of the same display (no overlap).",
    corrected=r"(\eta')))."))
L.append(F(191, "'D'autre part, l'anneau local A' (resp. B', B'⊗_{A'} k(y)) est un anneau quotient'", B, P, 'convention', 1, 'high',
    r"$B'\otimes_{A'}k(y)$", r"$B'\otimes_{A'}\boldsymbol{k}(y)$"))
L.append(F(191, "'anneau quotient de A (resp. B, B⊗_A k(y)), donc'", B, P, 'convention', 1, 'high',
    r"$B\otimes_Ak(y)$", r"$B\otimes_A\boldsymbol{k}(y)$"))
L.append(F(191, "display (13.2.4.3), third inequality, left side: 'dim(B'⊗_{A'} k(y))'", B, P, 'convention', 1, 'high',
    r"\quad¶  \dim(B'\otimes_{A'}k(y))", r"\quad¶  \dim(B'\otimes_{A'}\boldsymbol{k}(y))"))
L.append(F(191, "display (13.2.4.3), third inequality, right side: 'dim(B⊗_A k(y))'", B, P, 'convention', 1, 'high',
    r"\leq\dim(B\otimes_Ak(y))", r"\leq\dim(B\otimes_A\boldsymbol{k}(y))"))
L.append(F(191, "display (13.2.4.4), middle term: 'dim(B'⊗_{A'} k(y))'", B, P, 'convention', 1, 'high',
    r"\label{IV.13.2.4.4-fr}¶  \dim(B')\leq\dim(A')+\dim(B'\otimes_{A'}k(y))",
    r"\label{IV.13.2.4.4-fr}¶  \dim(B')\leq\dim(A')+\dim(B'\otimes_{A'}\boldsymbol{k}(y))",
    "'old' starts at the label because the same first line occurs in (13.2.4.2)."))
L.append(F(191, "display (13.2.4.4), right side: 'dim(A)+dim(B⊗_A k(y))'", B, P, 'convention', 1, 'high',
    r"¶  \leq\dim(A)+\dim(B\otimes_Ak(y))", r"¶  \leq\dim(A)+\dim(B\otimes_A\boldsymbol{k}(y))"))
L.append(F(191, "after the display (13.2.4.4): 'En outre, en vertu de (0, 16.3.9), on a aussi les inégalités'",
    "'En outre' begins a new, indented paragraph", "no blank line after \\]: the text continues the paragraph, unindented",
    'other', None, 'high',
    r"\]¶En outre, en vertu", r"\]¶¶En outre, en vertu",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47)."))
L.append(F(191, "display (13.2.4.5): 'dim(B')≤dim(B)≤dim(A)+dim(B⊗_A k(y))'", B, P, 'convention', 1, 'high',
    r"\dim(B)\leq\dim(A)+\dim(B\otimes_Ak(y))", r"\dim(B)\leq\dim(A)+\dim(B\otimes_A\boldsymbol{k}(y))"))

# ---------------- page 192 ----------------
L.append(F(192, "Lemme (13.2.5): 'Avec les notations de (13.2.4), les conditions suivantes'",
    "the reference (13.2.4) upright in the italic statement", R6, 'convention', 6, 'high',
    r"notations de (13.2.4), les", r"notations de \textup{(13.2.4)}, les"))
L.append(F(192, "Lemme (13.2.5) a): 'dim(B')=dim(A)+dim(B⊗_A k(y))'", B, P, 'convention', 1, 'high',
    r"$\dim(B')=\dim(A)+\dim(B\otimes_Ak(y))$", r"$\dim(B')=\dim(A)+\dim(B\otimes_A\boldsymbol{k}(y))$"))
L.append(F(192, "Lemme (13.2.5) b), item labels (i)-(iv)",
    "labels (i), (ii), (iii), (iv) upright", "enumerate label=(\\roman*) inside the italic lemma: italic labels",
    'convention', 6, 'high',
    r"[label=(\roman*)]¶    \item $\dim(A')", r"[label=\textup{(\roman*)}]¶    \item $\dim(A')",
    "One edit covers the four labels (GLOBAL_ISSUES 16)."))
L.append(F(192, "Lemme (13.2.5) b) (ii), left side: 'dim(B'⊗_{A'} k(y))'", B, P, 'convention', 1, 'high',
    r"$\dim(B'\otimes_{A'}k(y))", r"$\dim(B'\otimes_{A'}\boldsymbol{k}(y))"))
L.append(F(192, "Lemme (13.2.5) b) (ii), right side: '=dim(B⊗_A k(y)), autrement dit'", B, P, 'convention', 1, 'high',
    r"=\dim(B\otimes_Ak(y))$, autrement", r"=\dim(B\otimes_A\boldsymbol{k}(y))$, autrement"))
L.append(F(192, "Lemme (13.2.5) b) (iii): 'f' : X'→Y' est équidimensionnel (13.2.2) au point x'",
    "the reference (13.2.2) upright in the italic statement", R6, 'convention', 6, 'high',
    r"équidimensionnel (13.2.2) au point", r"équidimensionnel \textup{(13.2.2)} au point"))
L.append(F(192, "Lemme (13.2.5) b) (iv), display: 'dim(B')=dim(A')+dim(B'⊗_{A'} k(y))—(...)'", B, P, 'convention', 1, 'high',
    r"\dim(B')=\dim(A')+\dim(B'\otimes_{A'}k(y))", r"\dim(B')=\dim(A')+\dim(B'\otimes_{A'}\boldsymbol{k}(y))"))
L.append(F(192, "Lemme (13.2.5) b) (iv), display: '...k(y))—(dim_x(f'^{-1}(y))—dim(f'^{-1}(η')))'",
    "two long dashes for the subtractions: 42 and 41 px wide against 35 px (equals sign) and 34 px (plus sign) in the same display (measured)",
    "minus signs", 'convention', 7, 'high',
    r"-(\dim_x(f'^{-1}(y))-\dim", r"\setmin(\dim_x(f'^{-1}(y))\setmin\dim",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7). Two occurrences, one edit. No full stop after this display in the print or the TeX."))
L.append(F(192, "Lemme (13.2.5) b): '(relation qui est toujours vérifiée ... en vertu de (5.6.5)).'",
    "the reference (5.6.5) upright in the italic statement", R6, 'convention', 6, 'high',
    r"en vertu de (5.6.5)).", r"en vertu de \textup{(5.6.5)})."))
L.append(F(192, "Lemme (13.2.5) c), item labels (i), (ii)",
    "labels (i), (ii) upright", "enumerate label=(\\roman*) inside the italic lemma: italic labels",
    'convention', 6, 'high',
    r"[label=(\roman*)]¶    \item $\dim(B')=\dim(B)$", r"[label=\textup{(\roman*)}]¶    \item $\dim(B')=\dim(B)$",
    "One edit covers both labels."))
L.append(F(192, "Lemme (13.2.5) c) (ii): 'dim(B)=dim(A)+dim(B⊗_A k(y))'", B, P, 'convention', 1, 'high',
    r"$\dim(B)=\dim(A)+\dim(B\otimes_Ak(y))$", r"$\dim(B)=\dim(A)+\dim(B\otimes_A\boldsymbol{k}(y))$"))
L.append(F(192, "(13.2.6), after the display (13.2.6.1): 'L'équivalence des conditions b) et c) dans (13.2.5) implique ...'",
    "'L'équivalence' begins a new, indented paragraph", "no blank line after \\]: the text continues the paragraph, unindented",
    'other', None, 'high',
    r"\]¶L'équivalence", r"\]¶¶L'équivalence",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47)."))
L.append(F(192, "(13.2.6): 'L'équivalence des conditions b) et c) dans (13.2.5)'",
    "'b)' and 'c)' italic, parentheses included (enlarged crop p192_bc.png)",
    "$b)$, $c)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"$b)$ et $c)$", r"\emph{b)} et \emph{c)}",
    "As the TeX's own labels \\emph{\\alph*)} and the IV-2 p. 209 fix ($a)$ -> \\emph{a)})."))
L.append(F(192, "Proposition (13.2.7), display (13.2.7.1): '+dim(O_{X,x}⊗_{O_{Y,y}} k(y))'", B, P, 'convention', 1, 'high',
    r"+\dim(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}k(y)).",
    r"+\dim(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}\boldsymbol{k}(y))."))
L.append(F(192, "Proposition (13.2.7): 'Pour que les deux membres de (13.2.7.1) soient égaux'",
    "the reference (13.2.7.1) upright in the italic statement", R6, 'convention', 6, 'high',
    r"membres de (13.2.7.1) soient", r"membres de \textup{(13.2.7.1)} soient"))
L.append(F(192, "Proposition (13.2.7), item labels (i)-(iii) (this page) and (iv) (p. 193)",
    "labels upright", "enumerate label=(\\roman*) inside the italic proposition: italic labels",
    'convention', 6, 'high',
    r"[label=(\roman*)]¶  \item Si $Y'", r"[label=\textup{(\roman*)}]¶  \item Si $Y'",
    "One edit covers (i)-(iii) here and (iv) on p. 193 (GLOBAL_ISSUES 16)."))
L.append(F(192, "Proposition (13.2.7) (ii): 'Il revient au même de dire que dim(O_{X,x}⊗_{O_{Y,y}} k(y))=dim(O_{X',x}⊗_{O_{Y',y}} k(y)).'",
    "left side O_{X,x}⊗_{O_{Y,y}}, right side O_{X',x}⊗_{O_{Y',y}} (enlarged crop p192_iirevient.png)",
    "the two sides interchanged: dim(O_{X',x}⊗_{O_{Y',y}}k(y))=dim(O_{X,x}⊗_{O_{Y,y}}k(y))", 'formula', None, 'high',
    r"$\dim(\mathcal O_{X',x}\otimes_{\mathcal O_{Y',y}}k(y))¶  =\dim(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}k(y))$",
    r"$\dim(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}\boldsymbol{k}(y))¶  =\dim(\mathcal O_{X',x}\otimes_{\mathcal O_{Y',y}}\boldsymbol{k}(y))$",
    "The new text also gives both k(y) the bold italic k of convention 1 (the two entries below, fix null), so no edit overlaps. The corrected edition (r20 current, ega4-13-fr.tex l. 406-407) has the same interchanged sides, so the edit applies there too."))
L.append(F(192, "Proposition (13.2.7) (ii), same formula, left side: 'O_{X,x}⊗_{O_{Y,y}} k(y)'", B, P, 'convention', 1, 'high',
    None, None, "Applied by the formula edit above (its new text has \\boldsymbol{k})."))
L.append(F(192, "Proposition (13.2.7) (ii), same formula, right side: 'O_{X',x}⊗_{O_{Y',y}} k(y)'", B, P, 'convention', 1, 'high',
    None, None, "Applied by the formula edit above (its new text has \\boldsymbol{k})."))
L.append(F(192, "Proposition (13.2.7) (iii): 'contenant x ont même dimension (13.2.2)).'",
    "the reference (13.2.2) upright in the italic statement", R6, 'convention', 6, 'high',
    r"dimension (13.2.2)).", r"dimension \textup{(13.2.2)})."))

# ---------------- page 193 ----------------
L.append(F(193, "Proposition (13.2.7), item label (iv)", "'(iv)' upright", "italic label of the enumerate begun on p. 192",
    'convention', 6, 'high', None, None,
    "Covered by the p. 192 edit of the enumerate's label option ('old' in page_192.tex)."))
L.append(F(193, "Proposition (13.2.7) (iv), display: '+dim(O_{X',x}⊗_{O_{Y',y}} k(y))'", B, P, 'convention', 1, 'high',
    r"+\dim(\mathcal O_{X',x}\otimes_{\mathcal O_{Y',y}}k(y))",
    r"+\dim(\mathcal O_{X',x}\otimes_{\mathcal O_{Y',y}}\boldsymbol{k}(y))"))
L.append(F(193, "Proposition (13.2.7) (iv): '(condition toujours impliquée par (iii) lorsque O_{Y,y} est ...)'",
    "'(iii)' upright in the italic statement (enlarged crop p193_condition.png)", R6, 'convention', 6, 'high',
    r"par (iii) lorsque", r"par \textup{(iii)} lorsque"))
L.append(F(193, "Proposition (13.2.7), after the list: 'De plus, X' est alors une composante irréductible de X ...'",
    "'De plus' begins a new, indented paragraph of the statement",
    "text follows \\end{enumerate} without a blank line: set unindented", 'other', None, 'high',
    r"\end{enumerate}¶De plus", r"\end{enumerate}¶¶De plus",
    "GLOBAL_ISSUES 80."))
L.append(F(193, "Corollaire (13.2.8): 'Si les deux membres de (13.2.7.1) sont égaux'",
    "the reference (13.2.7.1) upright in the italic statement (enlarged crop p193_cor1328.png)", R6, 'convention', 6, 'high',
    r"(13.2.7.1) sont égaux, les", r"\textup{(13.2.7.1)} sont égaux, les"))
L.append(F(193, "Corollaire (13.2.8): 'vérifiant les conditions (i) à (iv) de (13.2.7) sont exactement'",
    "'(i)', '(iv)' and '(13.2.7)' upright, 'à' and 'de' italic (same crop)", R6, 'convention', 6, 'high',
    r"les conditions (i) à (iv) de (13.2.7)¶sont exactement",
    r"les conditions \textup{(i)} à \textup{(iv)} de \textup{(13.2.7)}¶sont exactement",
    "Three upright items, one edit."))
L.append(F(193, "Corollaire (13.2.9), l. 2-3: 'Supposons que O_{Y,y} soit un anneau universellement taténaire. Alors les conditions'",
    "'taténaire' with a t, first word of l. 3 (enlarged crop p193_catenaire.png)",
    "'caténaire': silently corrected", 'misprint_in_print', None, 'high',
    r"caténaire. Alors", r"taténaire. Alors",
    "Wrong letter in the print. Four lines below, l. 2 of b) begins 'celle que' for 'telle que' (next misprint entry): the two line-initial letters c and t look interchanged. No erratum for (13.2.9) in ega4-errata-addenda-list3-fr.tex; the corrected edition (r20 current) reads caténaire.",
    corrected=r"caténaire. Alors"))
L.append(F(193, "Corollaire (13.2.9) a): 'Les deux membres de (13.2.7.1) sont égaux.'",
    "the reference (13.2.7.1) upright in the italic statement", R6, 'convention', 6, 'high',
    r"\item Les deux membres de (13.2.7.1) sont égaux.", r"\item Les deux membres de \textup{(13.2.7.1)} sont égaux."))
L.append(F(193, "Corollaire (13.2.9) b), l. 1-2: '..., de dimension dim_x(f^{-1}(y)), celle que, pour tout x' dans un voisinage de x dans Z, on ait'",
    "'celle que', first word of l. 2 of b) (enlarged crop p193_celle.png); c) has 'telle que' (crop p193_telle.png)",
    "'telle que': silently corrected", 'misprint_in_print', None, 'high',
    r"telle que, pour tout", r"celle que, pour tout",
    "Wrong letter in the print (see the 'taténaire' entry). The corrected edition (r20 current) reads telle que.",
    corrected=r"telle que, pour tout"))
L.append(F(193, "Corollaire (13.2.9) b), display (13.2.9.1): '+dim(O_{X,x'}⊗_{O_{Y,y}} k(y))'", B, P, 'convention', 1, 'high',
    r"+\dim(\mathcal O_{X,x'}\otimes_{\mathcal O_{Y,y}}k(y)).",
    r"+\dim(\mathcal O_{X,x'}\otimes_{\mathcal O_{Y,y}}\boldsymbol{k}(y))."))
L.append(F(193, "proof of (13.2.9), l. 1: 'Montrons que a) entraîne b).'",
    "'a)' and 'b)' italic, parentheses included", "$a)$, $b)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"Montrons que $a)$ entraîne $b)$.", r"Montrons que \emph{a)} entraîne \emph{b)}.",
    "As the p. 192 entry for b), c)."))
L.append(F(193, "proof of (13.2.9): 'La condition b) entraîne trivialement c) en vertu de (5.1.2).'",
    "'b)' and 'c)' italic, parentheses included", "$b)$, $c)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"La condition $b)$ entraîne trivialement $c)$", r"La condition \emph{b)} entraîne trivialement \emph{c)}"))
L.append(F(193, "proof of (13.2.9): 'Enfin, si c) est vérifiée et si X'' est'",
    "'c)' italic, parenthesis included", "$c)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"si $c)$ est vérifiée", r"si \emph{c)} est vérifiée"))
L.append(F(193, "proof of (13.2.9), last line: 'donc c) implique a).'",
    "'c)' and 'a)' italic, parentheses included", "$c)$, $a)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"donc $c)$ implique $a)$.", r"donc \emph{c)} implique \emph{a)}."))
L.append(F(193, "end of page_193.tex, just before \\oldpage[IV-3]{194}: 'Soient Z_i les | composantes irréductibles de f^{-1}(y), ...'",
    "printed p. 194 begins 'composantes irréductibles de f^{-1}(y), z_i le point générique de Z_i, ...' flush left: the sentence of Proposition (13.2.10) runs on",
    "blank line before \\oldpage[IV-3]{194}: a paragraph break mid-sentence inside the proposition",
    'marker', None, 'high',
    r"Soient $Z_i$ les¶¶", r"Soient $Z_i$ les¶",
    "The marker position itself is right; no blank line follows it."))

# ---------------- page 194 ----------------
L.append(F(194, "Proposition (13.2.10) a), display (13.2.10.1): '+dim(O_{X,x}⊗_{O_{Y,y}} k(y))'", B, P, 'convention', 1, 'high',
    r"+\dim(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}k(y)).",
    r"+\dim(\mathcal O_{X,x}\otimes_{\mathcal O_{Y,y}}\boldsymbol{k}(y))."))
L.append(F(194, "Proposition (13.2.10) c): '(autrement dit, telle que le sous-préschéma fermé réduit X_i de X soit ...)'",
    "'(autrement dit, telle que' roman, opening parenthesis included; from 'le sous-préschéma' to the closing parenthesis italic (enlarged crops p194_autrement.png, p194_zi_paren.png)",
    R6, 'convention', 6, 'high',
    r"(autrement dit, telle que le", r"\textup{(autrement dit, telle que} le"))
L.append(F(194, "Proposition (13.2.10) c): 'le sous-préschéma fermé réduit X_i de X'",
    "'sous-préschéma fermé réduit' italic like the words around it (same crop)",
    "\\emph inside the italic proposition: upright", 'convention', 6, 'high',
    r"\emph{sous-préschéma fermé réduit}", r"sous-préschéma fermé réduit",
    "FIX_POLICY 2.6: drop \\emph where the print shows no change of face. Independent of the previous edit (no overlap)."))
L.append(F(194, "Proposition (13.2.10), after the list: 'Alors a) entraîne b) et b) entraîne c); ...'",
    "'Alors' begins a new, indented paragraph of the statement",
    "text follows \\end{enumerate} without a blank line: set unindented", 'other', None, 'high',
    r"\end{enumerate}¶Alors", r"\end{enumerate}¶¶Alors",
    "GLOBAL_ISSUES 80."))
L.append(F(194, "Proposition (13.2.10): 'Alors a) entraîne b) et b) entraîne c);'",
    "the labels a), b), b), c) upright in the italic statement (enlarged crop p194_alors.png)",
    "$a)$ etc.: italic letters", 'convention', 6, 'high',
    r"$a)$ entraîne $b)$ et $b)$ entraîne $c)$~;",
    r"\textup{a)} entraîne \textup{b)} et \textup{b)} entraîne \textup{c)}~;",
    "Four labels, one edit; does not overlap the paragraph edit above."))
L.append(F(194, "Proposition (13.2.10): 'les trois conditions a), b), c) sont équivalentes.'",
    "the labels a), b), c) and their commas upright (same crop)", "$a)$, $b)$, $c)$: italic letters", 'convention', 6, 'high',
    r"les trois conditions $a)$,¶$b)$, $c)$ sont", r"les trois conditions \textup{a),¶b), c)} sont",
    "Three labels, one edit."))
L.append(F(194, "proof of (13.2.10): 'L'anneau O_{X,z_i}⊗_{O_{Y,y}} k(y) étant de dimension 0'", B, P, 'convention', 1, 'high',
    r"\mathcal O_{X,z_i}\otimes_{\mathcal O_{Y,y}}k(y)$", r"\mathcal O_{X,z_i}\otimes_{\mathcal O_{Y,y}}\boldsymbol{k}(y)$"))
L.append(F(194, "proof of (13.2.10): 'a) entraîne évidemment b); b) entraîne c) en vertu de (13.2.7)'",
    "the labels italic, parentheses included", "$a)$ etc.: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"$a)$ entraîne évidemment $b)$~; $b)$ entraîne $c)$ en vertu",
    r"\emph{a)} entraîne évidemment \emph{b)}~; \emph{b)} entraîne \emph{c)} en vertu",
    "As the p. 192 entry for b), c)."))
L.append(F(194, "proof of (13.2.10): 'comme la condition c) implique que f(X_i) est dense'",
    "'c)' italic, parenthesis included", "$c)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"la condition $c)$¶implique", r"la condition \emph{c)}¶implique"))
L.append(F(194, "proof of (13.2.10): 'il résulte de c) que les conditions (i) à (iv)'",
    "'c)' italic, parenthesis included", "$c)$: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"il résulte de $c)$ que", r"il résulte de \emph{c)} que"))
L.append(F(194, "proof of (13.2.10): 'donc c) implique b); enfin b) implique a) en vertu de (13.2.9)'",
    "the labels italic, parentheses included", "$c)$ etc.: italic letter, upright parenthesis", 'italics', None, 'medium',
    r"donc $c)$ implique $b)$~; enfin $b)$ implique $a)$",
    r"donc \emph{c)} implique \emph{b)}~; enfin \emph{b)} implique \emph{a)}"))
L.append(F(194, "Corollaire (13.2.11), l. 1: 'Les notations étant celles de (13.2.10), supposons'",
    "the reference (13.2.10) upright in the italic statement (enlarged crop p194_cor13211_l1.png)", R6, 'convention', 6, 'high',
    r"celles de (13.2.10), supposons", r"celles de \textup{(13.2.10)}, supposons"))
L.append(F(194, "Corollaire (13.2.11): 'si les conditions équivalentes a), b), c) de (13.2.10) sont vérifiées'",
    "the labels a), b), c) and their commas upright (enlarged crop p194_cor13211_l4.png)",
    "$a)$, $b)$, $c)$: italic letters", 'convention', 6, 'high',
    r"équivalentes¶$a)$, $b)$, $c)$ de", r"équivalentes¶\textup{a), b), c)} de",
    "Three labels, one edit."))
L.append(F(194, "Corollaire (13.2.11): '... de (13.2.10) sont vérifiées, on a E(y)⊂E(η)'",
    "the reference (13.2.10) upright in the italic statement (same crop)", R6, 'convention', 6, 'high',
    r"(13.2.10) sont vérifiées", r"\textup{(13.2.10)} sont vérifiées",
    "Does not overlap the label edit before it."))
L.append(F(194, "Remarques (13.2.12) (ii): 'si les conditions équivalentes a), b), c) de (13.2.10) sont satisfaites'",
    "the labels italic, parentheses included (roman remark body)", "$a)$ etc.: italic letter, upright parenthesis",
    'italics', None, 'medium',
    r"équivalentes $a)$, $b)$, $c)$ de", r"équivalentes \emph{a)}, \emph{b)}, \emph{c)} de",
    "Judged with the remark body as roman (document-wide remark item)."))
L.append(F(194, "Remarques (13.2.12) (iii): 'alors que E(y_0) est réduit à un seul élément'",
    "'un seul' italic, both words (enlarged crop p194_unseul.png)", "'un \\emph{seul}': 'un' not emphasized",
    'italics', None, 'high',
    r"à un \emph{seul} élément", r"à \emph{un seul} élément",
    "Judged with the remark body as roman."))
L.append(F(194, "Remarques (13.2.12) (iii): 'donc E(y) n'est pas constant dans Y.'",
    "'n'est pas constant' italic, all three words (same crop)", "\"n'est \\emph{pas constant}\": \"n'est\" not emphasized",
    'italics', None, 'high',
    r"n'est \emph{pas constant}", r"\emph{n'est pas constant}",
    "Judged with the remark body as roman."))
L.append(F(194, "subsection heading 13.3", "'13.3. Morphismes équidimensionnels : cas général.' (final full stop)",
    "no full stop", 'punctuation', None, 'high',
    r"\subsection{Morphismes équidimensionnels : cas général}", r"\subsection{Morphismes équidimensionnels : cas général.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))

# ---------------- checks ----------------
texts = {}
for n in range(189, 195):
    texts[n] = open(RUN + r"\page_%03d.tex" % n, 'rb').read().decode('utf-8').replace('\r\n', '\n')
bad = 0
for i, d in enumerate(L):
    fx = d['fix']
    if fx is None:
        continue
    c = texts[d['page']].count(fx['old'])
    if c != 1:
        bad += 1
        print('NOT UNIQUE (%d):' % c, i, d['page'], repr(fx['old']))
# overlap check: within each page, the spans of olds must not intersect
for n in texts:
    spans = []
    for i, d in enumerate(L):
        if d['page'] == n and d['fix']:
            s = texts[n].find(d['fix']['old'])
            spans.append((s, s + len(d['fix']['old']), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print('OVERLAP on page', n, a, b)
print('entries', len(L), 'problems', bad)
counts = {}
for d in L:
    k = 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal')
    counts.setdefault(d['page'], {'normal': 0, 'convention': 0, 'misprint': 0})[k] += 1
for p in sorted(counts):
    print(p, counts[p])
if bad == 0:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(L, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('written', OUT)
