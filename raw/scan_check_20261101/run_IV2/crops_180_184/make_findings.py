"""Build findings_180_184.json for run_IV2 and check every fix's old string (exactly once in its page_NNN.tex).

'¶' stands for a line break (LF) in old/new strings.
"""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_180_184.json"


def F(page, where, scan, tex, kind, conv, conf, old=None, new=None, note=None):
    fix = None if old is None else {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}
    return {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
            "confidence": conf, "fix": fix, "note": note}


L = []
# ---------------- page 180 ----------------
L += [
    F(180, "l. 1: 'où X = Spec(A) (avec A = O_{X,x}) est un schéma local.'", "'local' italic", "upright",
      "italics", None, "high", r"est un schéma local.", r"est un schéma \emph{local}."),
    F(180, "l. 5: 'que A est un anneau local intègre (puisque A, étant réduit'", "'intègre' italic", "upright",
      "italics", None, "high", r"anneau local intègre (puisque", r"anneau local \emph{intègre} (puisque"),
    F(180, "commutative diagram, top arrow Y <- Y' (label h)", "h above the arrow (enlarged crop)",
      "Y' \\ar[l]^h: for a leftward arrow '^' puts the label below", "formula", None, "high",
      r"\ar[l]^h", r"\ar[l]_h", "GLOBAL_ISSUES 30 (labels of leftward arrows). The labels g, g' (left of their arrows) are right."),
    F(180, "commutative diagram, bottom arrow X <- X' (label f)", "f below the arrow (enlarged crop)",
      "X' \\ar[l]_f: for a leftward arrow '_' puts the label above", "formula", None, "high",
      r"X' \ar[l]_f", r"X' \ar[l]^f", "GLOBAL_ISSUES 30."),
    F(180, "after the diagram: 'Notons que f est un morphisme plat; donc (6.15.4.1)'",
      "new indented paragraph after the diagram", "no blank line after \\]: the text runs on in the same paragraph",
      "missing", None, "high", r"\]¶Notons que $f$", r"\]¶¶Notons que $f$",
      "Paragraph break after a display (GLOBAL_ISSUES 47)."),
    F(180, "Lemme (6.15.8): '(autrement dit, tel que la clôture algébrique de k soit radicielle sur k)'",
      "the parenthesis is roman; only 'radicielle' italic (enlarged crop)",
      "whole parenthesis italic (lemma environment)", "convention", 6, "high",
      r"(autrement dit, tel que la clôture¶algébrique de $k$ soit radicielle sur $k$)",
      r"\textup{(autrement dit, tel que la clôture¶algébrique de $k$ soit \emph{radicielle} sur $k$)}",
      "Inside \\textup the \\emph sets 'radicielle' italic, as printed."),
    F(180, "Lemme (6.15.8): 'x un point fermé de X'", "'fermé' roman (emphasis inside the italic statement; enlarged crop)",
      "italic like the rest of the statement", "convention", 6, "high",
      r"un point fermé de $X$", r"un point \emph{fermé} de $X$",
      "\\emph inside the italic statement typesets 'fermé' upright, as printed."),
    F(180, "proof of (6.15.8): 'on sait (I, 6.4.2)'", "bold I", "plain I", "convention", 2, "high",
      r"(I, 6.4.2)", r"(\textbf{I}, 6.4.2)"),
    F(180, "proof of (6.15.8): 'que k(x) est une extension algébrique de k'", "bold italic k", "k(x)",
      "convention", 1, "high", r"que $k(x)$ est", r"que $\boldsymbol{k}(x)$ est"),
    F(180, "proof of (6.15.8): 'une extension algébrique de k; comme le corps résiduel'",
      "'algébrique' italic (enlarged crop)", "upright", "italics", None, "high",
      r"extension algébrique de¶$k$;", r"extension \emph{algébrique} de¶$k$;",
      "The second 'extension algébrique de k(x)' two lines below is roman in the print and stays as it is."),
    F(180, "proof of (6.15.8): 'la clôture intégrale de (O_x)_red'",
      "(𝒪_x)_red: the subscript is x alone (4x crop)", "(\\mathcal O_{X,x})_{\\mathrm{red}}", "formula", None, "high",
      r"$(\mathcal O_{X,x})_{\mathrm{red}}$", r"$(\mathcal O_x)_{\mathrm{red}}$",
      "Not a misprint: O_x is the print's usual short form of O_{X,x}."),
    F(180, "proof of (6.15.8): 'est une extension algébrique de k(x), c'est'", "bold italic k", "k(x)",
      "convention", 1, "high", r"algébrique de $k(x)$, c'est", r"algébrique de $\boldsymbol{k}(x)$, c'est"),
    F(180, "proof of (6.15.8): 'c'est une extension radicielle de k par hypothèse'", "'radicielle' italic",
      "upright", "italics", None, "high", r"une extension radicielle de $k$", r"une extension \emph{radicielle} de $k$"),
    F(180, "proof of (6.15.8), end: 'donc aussi de k(x).'", "bold italic k", "k(x)", "convention", 1, "high",
      r"donc aussi de $k(x)$", r"donc aussi de $\boldsymbol{k}(x)$"),
    F(180, "Corollaire (6.15.9): '(autrement dit, telle que la clôture algébrique de k' soit radicielle sur k')'",
      "the whole parenthesis roman, 'radicielle' included (enlarged crop)", "italic (corollary environment)",
      "convention", 6, "high",
      r"(autrement dit, telle que la¶clôture algébrique de $k'$ soit radicielle sur $k'$)",
      r"\textup{(autrement dit, telle que la¶clôture algébrique de $k'$ soit radicielle sur $k'$)}"),
]
# ---------------- page 181 ----------------
L += [
    F(181, "Proposition (6.15.10), l. 2: 'un morphisme normal (6.8.1)'", "(6.8.1) upright", "italic (statement environment)",
      "convention", 6, "high", r"normal (6.8.1),", r"normal \textup{(6.8.1)},"),
    F(181, "Proposition (6.15.10), l. 3-4: 'si X est réduit (resp. géométriquement unibranche, resp. intègre et géométriquement unibranche) au point x = p(x')'",
      "'(resp.', 'resp.' and the closing parenthesis upright; the adjectives italic (enlarged crop)",
      "all italic", "convention", 6, "high",
      r"(resp. géométriquement unibranche,¶resp. intègre et géométriquement unibranche) au point $x=p(x')$",
      r"\textup{(resp.} géométriquement unibranche,¶\textup{resp.} intègre et géométriquement unibranche\textup{)} au point $x=p(x')$"),
    F(181, "Proposition (6.15.10), l. 4-5: 'X' est réduit (resp. géométriquement unibranche, resp. intègre et géométriquement unibranche) au point x''",
      "'(resp.', 'resp.' and the closing parenthesis upright (enlarged crop)", "all italic", "convention", 6, "high",
      r"(resp. géométriquement unibranche, resp. intègre et¶géométriquement unibranche) au point $x'$",
      r"\textup{(resp.} géométriquement unibranche, \textup{resp.} intègre et¶géométriquement unibranche\textup{)} au point $x'$"),
    F(181, "proof of (6.15.10), l. 1: 'En vertu de (I, 3.6.5)'", "bold I", "plain I", "convention", 2, "high",
      r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)"),
    F(181, "proof of (6.15.10): 'est normal (6.8.2), et a fortiori réduit'", "'a fortiori' italic (enlarged crop)",
      "upright", "italics", None, "high", r"et a fortiori réduit", r"et \emph{a fortiori} réduit"),
    F(181, "proof of (6.15.10), second paragraph: 'compte tenu de (I, 5.1.8)'", "bold I", "plain I", "convention", 2,
      "high", r"(I,¶5.1.8)", r"(\textbf{I},¶5.1.8)"),
    F(181, "proof of (6.15.10): 'supposer B réduit, donc intègre.'", "'intègre' italic", "upright", "italics", None,
      "high", r"donc intègre. Soit", r"donc \emph{intègre}. Soit"),
    F(181, "proof of (6.15.10): 'qui est par hypothèse un anneau local; posons'", "'local' italic", "upright",
      "italics", None, "high", r"un anneau local;", r"un anneau \emph{local};"),
    F(181, "commutative diagram, left vertical arrow Z -> X", "label f (4x and 6x crops; same glyph as the label f of the p. 180 diagram); the text names this morphism f ('Comme f est entier et birationnel')",
      "label l", "formula", None, "high", r"Z \ar[d]_l &", r"Z \ar[d]_f &",
      "The label stands left of the arrow in the print, as \\ar[d]_ gives."),
    F(181, "commutative diagram, right vertical arrow Z' -> X'", "label f' (enlarged crop; 'il en est de même de f'' in the text), set to the RIGHT of the arrow",
      "label l', placed left of the arrow (\\ar[d]_{l'})", "formula", None, "high", r"\ar[d]_{l'}", r"\ar[d]^{f'}",
      "One edit for the letter and the side (next entry)."),
    F(181, "commutative diagram, right vertical arrow: side of the label", "f' right of the arrow",
      "\\ar[d]_{...} puts the label left of a downward arrow", "formula", None, "high", None, None,
      "Covered by the edit of the preceding finding (\\ar[d]^{f'})."),
    F(181, "commutative diagram, bottom arrow X <- X' (label p)", "p below the arrow",
      "X' \\ar[l]_p: for a leftward arrow '_' puts the label above", "formula", None, "high",
      r"X' \ar[l]_p", r"X' \ar[l]^p", "GLOBAL_ISSUES 30. The top arrow Z <- Z' has no label in the print either."),
    F(181, "after the diagram: 'En vertu de la première partie du raisonnement'", "new indented paragraph after the diagram",
      "no blank line after \\]: the text runs on in the same paragraph", "missing", None, "high",
      r"\]¶En vertu de la première", r"\]¶¶En vertu de la première", "GLOBAL_ISSUES 47."),
    F(181, "after the diagram: 'X' est réduit; d'autre part'", "'réduit' italic", "upright", "italics", None, "high",
      r"est réduit; d'autre", r"est \emph{réduit}; d'autre"),
    F(181, "after the diagram: 'il résulte de (6.14.1) que Z' est normal'", "'normal' italic", "upright", "italics",
      None, "high", r"que $Z'$ est normal", r"que $Z'$ est \emph{normal}"),
    F(181, "after the diagram: '(et a fortiori géométriquement unibranche)'", "'a fortiori' italic", "upright",
      "italics", None, "high", r"(et a fortiori", r"(et \emph{a fortiori}"),
    F(181, "Remarques (6.15.11) (ii): 'le corps résiduel k(x) est algébriquement clos'", "bold italic k", "k(x)",
      "convention", 1, "high", r"$k(x)$ est algébriquement", r"$\boldsymbol{k}(x)$ est algébriquement"),
]
# ---------------- page 182 ----------------
L += [
    F(182, "Remarques (6.15.11), end of (ii): 'l'anneau local intègre complet R[[U, V]]/(U²+V²); si u, v sont'",
      "the formula is in the running text, followed by '; si u, v' on the same line", "set as a display \\[ ... \\]",
      "other", None, "high", r"complet¶\[¶\mathbb R[[U,V]]/(U^2+V^2);¶\]¶si",
      r"complet¶$\mathbb R[[U,V]]/(U^2+V^2)$; si", "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost or added."),
    F(182, "'où t = u/v vérifie la relation t² = —1'", "long dash for the minus (bar 41 px against 35 px for the = bars on the same line)",
      "minus sign", "convention", 7, "high", r"$t^2=-1$", r"$t^2=\setmin 1$",
      "Unary minus printed as the long dash (GLOBAL_ISSUES 23, 49)."),
    F(182, "last sentence of the remark: 'étant isomorphe à C[[U, V]]/(U—iV)(U+iV).'",
      "the formula is in the running text, on the line of 'étant isomorphe à'", "set as a display \\[ ... \\]",
      "other", None, "high", r"isomorphe à¶\[¶\mathbb C[[U,V]]/(U-iV)(U+iV).¶\]",
      r"isomorphe à $\mathbb C[[U,V]]/(U-iV)(U+iV)$.",
      "GLOBAL_ISSUES 21. Apply before the convention-7 edit of (U-iV) (next entry)."),
    F(182, "same formula: '(U—iV)'", "long dash for the minus (bar 41-42 px against 35 px for the + bar of (U+iV))",
      "minus sign", "convention", 7, "high", r"(U-iV)", r"(U\setmin iV)",
      "Apply after the display edit above; '(U-iV)' occurs once before and after it."),
    F(182, "§ 7 introduction, 2nd paragraph: 'même dans le cas des localisées d'algèbres de type fini'",
      "'localisées' (enlarged crop)", "'localisés'", "word", None, "high", r"localisés d'algèbres", r"localisées d'algèbres",
      "The printed feminine plural agrees with 'algèbres'; the TeX changed the word. Not treated as a misprint."),
    F(182, "§ 7 introduction, 2nd paragraph, end: 'du critère de régularité (0, 22.3.4)'", "bold 0", "plain 0",
      "convention", 2, "high", r"(0, 22.3.4)", r"(\textbf{0}, 22.3.4)"),
    F(182, "heading 7.1 (printed at the top of p. 183)", "'7.1. Équidimensionalité formelle et anneaux formellement caténaires.' (final full stop)",
      "\\subsection{...caténaires} (no full stop)", "punctuation", None, "high",
      r"anneaux formellement caténaires}", r"anneaux formellement caténaires.}",
      "GLOBAL_ISSUES 43/58. The heading text lies in this file before \\oldpage[IV-2]{183}; see the marker edits."),
    F(182, "page break 182/183: marker position (edit 1 of 2, insert)",
      "printed p. 182 ends with '... et même dans les chapitres ultérieurs.' (page_182_s4.png); printed p. 183 begins with the heading '7.1. Équidimensionalité formelle et anneaux formellement caténaires.' (page_183_s1.png)",
      "\\oldpage[IV-2]{183} stands after the \\subsection and its \\label, so the heading falls on p. 182", "marker", None, "high",
      r"ultérieurs.¶¶\subsection{", r"ultérieurs.¶¶\oldpage[IV-2]{183}¶\subsection{",
      "Apply together with the p. 183 edit that removes the old marker."),
]
# ---------------- page 183 ----------------
L += [
    F(183, "page start: marker position (edit 2 of 2, remove)", "the heading 7.1 is the first line of printed p. 183",
      "\\oldpage[IV-2]{183} after the heading", "marker", None, "high", r"\oldpage[IV-2]{183}¶¶", r"",
      "Apply together with the p. 182 edit that inserts the marker before \\subsection; the blank line before \\begin{definition}[7.1.1] remains."),
    F(183, "Définition (7.1.1): 'A est formellement équidimensionnel si son complété'",
      "'formellement équidimensionnel' italic like the rest of the definition (enlarged crop)",
      "\\emph{formellement équidimensionnel} inside the italic definition environment (typeset upright)",
      "convention", 6, "high", r"\emph{formellement¶équidimensionnel}", r"formellement¶équidimensionnel"),
    F(183, "Définition (7.1.1), end: '(0, 16.1.4)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0,¶16.1.4)", r"\textup{(\textbf{0},¶16.1.4)}",
      "One edit for this finding and the next (convention 6): bold numeral and the upright reference together."),
    F(183, "Définition (7.1.1), same reference '(0, 16.1.4)'", "the reference is upright inside the italic statement",
      "italic (statement environment)", "convention", 6, "high", None, None,
      "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."),
    F(183, "Proposition (7.1.2), l. 1: 'p_i (1 ≤ i ≤ n) ses idéaux premiers minimaux'",
      "both parentheses upright (2.5x crop)", "parentheses outside math, italic in the proposition environment",
      "convention", 6, "medium", r"($1\leqslant i\leqslant¶n$)", r"\textup{(}$1\leqslant i\leqslant¶n$\textup{)}"),
    F(183, "Proposition (7.1.2), end: '(autrement dit que les A/p_i aient même dimension)'",
      "the whole parenthesis roman", "italic (statement environment)", "convention", 6, "high",
      r"(autrement dit que les $A/\mathfrak p_i$ aient¶même dimension)",
      r"\textup{(autrement dit que les $A/\mathfrak p_i$ aient¶même dimension)}"),
    F(183, "proof of (7.1.2): '(0_I, 7.3.3)'", "bold 0 in 0_I", "plain 0", "convention", 2, "high",
      r"(0$_{\mathrm I}$,", r"(\textbf{0}$_{\mathrm I}$,"),
    F(183, "Proposition (7.1.3), label (i)", "label (i) upright", "\\item[(i)] inside the italic statement (typeset italic)",
      "convention", 6, "high", r"\item[(i)] $A$ est", r"\item[\textup{(i)}] $A$ est", "GLOBAL_ISSUES 16."),
    F(183, "Proposition (7.1.3), label (ii)", "label (ii) upright", "\\item[(ii)] inside the italic statement (typeset italic)",
      "convention", 6, "high", r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons", "GLOBAL_ISSUES 16."),
    F(183, "proof of (7.1.3): 'pour tout i (2.3.4). D'autre part y'_i est point maximal'",
      "no comma after 'D'autre part' (enlarged crop)", "comma after 'D'autre part'", "punctuation", None, "high",
      r"D'autre part, $y'_i$", r"D'autre part $y'_i$"),
    F(183, "proof of (7.1.3): 'de la fibre f^{-1}(y) (0_I, 2.1.8)'", "bold 0 in 0_I", "plain 0", "convention", 2, "high",
      r"(0$_{\mathrm¶I}$, 2.1.8)", r"(\textbf{0}$_{\mathrm¶I}$, 2.1.8)"),
    F(183, "proof of (7.1.3): 'O_{X',y'_i} ⊗_{O_{X,y}} k(y) = ...'", "bold italic k", "k(y)", "convention", 1, "high",
      r"\otimes_{\mathscr O_{X,y}}k(y)", r"\otimes_{\mathscr O_{X,y}}\boldsymbol{k}(y)"),
    F(183, "display (7.1.3.3): 'dim(O_{X',y'_i}) = dim(O_{X,y})'", "no punctuation after the formula (enlarged crop)",
      "comma at the end of the display", "punctuation", None, "high",
      r"\dim(\mathscr O_{X,y}),¶\tag{7.1.3.3}", r"\dim(\mathscr O_{X,y})¶\tag{7.1.3.3}",
      "Comma after a display that the print lacks (GLOBAL_ISSUES 73)."),
    F(183, "after display (7.1.3.2): 'Soient y le point générique de Y'", "new indented paragraph after the display",
      "no blank line after \\end{equation}: the text runs on in the same paragraph", "missing", None, "high",
      r"\end{equation}¶Soient $y$", r"\end{equation}¶¶Soient $y$", "GLOBAL_ISSUES 47."),
    F(183, "proof of (7.1.3): 'on a, en vertu de (0, 14.3.5)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 14.3.5)", r"(\textbf{0}, 14.3.5)"),
    F(183, "page break 183/184: after display (7.1.3.5)",
      "printed p. 184 begins 'pour tout i; en vertu de ...' flush left, continuing the sentence of (7.1.3.5)",
      "blank line between \\end{equation} and \\oldpage[IV-2]{184} makes a paragraph break", "extra", None, "high",
      r"\label{IV.2.eq.7.1.3.5-fr}¶\end{equation}¶¶", r"\label{IV.2.eq.7.1.3.5-fr}¶\end{equation}¶",
      "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20); one edit at the end of this page's segment."),
]
# ---------------- page 184 ----------------
L += [
    F(184, "proof of (7.1.3): 'sont égaux d'après (0, 14.2.2.2)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 14.2.2.2)", r"(\textbf{0}, 14.2.2.2)"),
    F(184, "proof of (7.1.3), 'Prouvons enfin (i)': 'équidimensionnel et caténaire (0, 16.1.4)'", "bold 0", "plain 0",
      "convention", 2, "high", r"(0, 16.1.4)", r"(\textbf{0}, 16.1.4)"),
    F(184, "proof of (7.1.3): 'codim(Y, X) = dim X — dim Y'", "long dash for the subtraction (bar 42 px against 34 px for the = bars on the same line)",
      "minus sign", "convention", 7, "high", r"\dim X-\dim Y", r"\dim X\setmin\dim Y", "GLOBAL_ISSUES 23."),
    F(184, "proof of (7.1.3), end: 'en vertu de (0, 14.3.3)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0, 14.3.3)", r"(\textbf{0}, 14.3.3)"),
    F(184, "Corollaire (7.1.4), label (i)", "label (i) upright", "\\item[(i)] inside the italic statement (typeset italic)",
      "convention", 6, "high", r"\item[(i)] $A$ est", r"\item[\textup{(i)}] $A$ est", "GLOBAL_ISSUES 16."),
    F(184, "Corollaire (7.1.4) (i): '(autrement dit, biéquidimensionnel)'",
      "'(autrement dit,' and the closing parenthesis roman, 'biéquidimensionnel' italic (enlarged crop)",
      "all italic", "convention", 6, "high", r"(autrement dit,¶biéquidimensionnel)",
      r"\textup{(autrement dit,}¶biéquidimensionnel\textup{)}"),
    F(184, "Corollaire (7.1.4), label (ii)", "label (ii) upright", "\\item[(ii)] inside the italic statement (typeset italic)",
      "convention", 6, "high", r"\item[(ii)] Soit", r"\item[\textup{(ii)}] Soit", "GLOBAL_ISSUES 16."),
    F(184, "Corollaire (7.1.5), l. 2: 'un A-module de Cohen-Macaulay et pour lequel'",
      "hyphen in Cohen-Macaulay (12 px at 300 dpi)", "Cohen--Macaulay (en dash)", "punctuation", None, "medium",
      r"de Cohen--Macaulay et pour", r"de Cohen-Macaulay et pour",
      "The print has the hyphen; ega4-2-fr.tex writes Cohen--Macaulay on pp. 145-206 (43 times) and Cohen-Macaulay elsewhere."),
    F(184, "Corollaire (7.1.5): '(ce qui aura lieu par exemple si A est un anneau de Cohen-Macaulay)'",
      "the whole parenthesis roman (enlarged crop)", "italic (corollary environment)", "convention", 6, "high",
      r"(ce qui aura lieu par¶exemple si $A$ est un anneau de Cohen--Macaulay)",
      r"\textup{(ce qui aura lieu par¶exemple si $A$ est un anneau de Cohen-Macaulay)}",
      "The edit also replaces the en dash of this Cohen--Macaulay by the printed hyphen (next entry)."),
    F(184, "same parenthesis: 'anneau de Cohen-Macaulay'", "hyphen (12 px, measured on this occurrence)", "Cohen--Macaulay (en dash)",
      "punctuation", None, "medium", None, None, "Covered by the edit of the preceding finding."),
    F(184, "Corollaire (7.1.5): 'donc (7.1.4) pour qu'un anneau quotient B'", "(7.1.4) upright", "italic (statement environment)",
      "convention", 6, "high", r"donc (7.1.4) pour", r"donc \textup{(7.1.4)} pour"),
]

bad = 0
for x in L:
    if x["fix"] is None:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(x["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/MISSING", x["page"], n, repr(x["fix"]["old"]))
# apply all edits of a page in list order on a copy, to check that each old still occurs once at its turn
for p in range(180, 185):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    for x in L:
        if x["page"] != p or x["fix"] is None:
            continue
        n = t.count(x["fix"]["old"])
        if n != 1:
            bad += 1
            print("SEQUENTIAL PROBLEM", p, n, repr(x["fix"]["old"]))
        t = t.replace(x["fix"]["old"], x["fix"]["new"], 1)
    (RUN / "crops_180_184" / f"_applied_{p}.tex").write_text(t, encoding="utf-8")
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter()
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in range(180, 185):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("entries", len(L), "problems", bad)
