"""Build findings_120_124.json for run_IV2 (EGA IV part 2, pp. 120-124) and check every fix's old string."""
import json
import pathlib

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_120_124.json"
NL = "¶"  # placeholder for a line break inside raw strings

texts = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(120, 125)}
findings = []


def add(page, where, scan, tex, kind, old=None, new=None, conv=None, conf="high", note="", corrected=None):
    f = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if corrected is not None:
        f["corrected"] = corrected
    f["note"] = note
    findings.append(f)


SETMIN = "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
LABEL = "Item label upright in the print (GLOBAL_ISSUES 16)."

# ---------------- page 120 ----------------
add(120, "Corollaire (5.10.15), label (ii)", "item label (ii) upright roman",
    "\\item[(ii)] comes out italic in the italic statement", "convention",
    r"\item[(ii)] L'ensemble", r"\item[\textup{(ii)}] L'ensemble", 6, note=LABEL)
add(120, "Corollaire (5.10.15) (ii): 'au point x (5.7.2) est ouvert'", "reference (5.7.2) upright inside the italic statement",
    "(5.7.2) italic (statement environment)", "convention",
    r"au point $x$ (5.7.2) est", r"au point $x$ \textup{(5.7.2)} est", 6)
add(120, "Corollaire (5.10.15) (ii): 'codim(X—U, X) >= 2.'", "long dash for set difference X—U",
    "X-U", "convention", r"(X-U,X)\geq2$.", r"(X\setmin U,X)\geq2$.", 7, note=SETMIN)
add(120, "proof of (5.10.15) (i), l. 2: 'appartiennent à X—Z^(2)'", "long dash for set difference",
    "X-Z^{(2)}", "convention", r"appartiennent à $X-Z^{(2)}$", r"appartiennent à $X\setmin Z^{(2)}$", 7, note=SETMIN)
add(120, "proof of (5.10.15) (i), l. 6: 'on a x∈X—Z^(2), donc,'", "long dash for set difference",
    "X-Z^{(2)}", "convention", r"x\in X-Z^{(2)}$, donc,", r"x\in X\setmin Z^{(2)}$, donc,", 7, note=SETMIN)
add(120, "proof of (5.10.15) (i), l. 7: 'puisque F'_x = F_x on aurait'",
    "no comma after F'_x = F_x (enlarged crop)", "'$\\mathcal F'_x=\\mathcal F_x$, on aurait' (comma)", "punctuation",
    r"\mathcal F_x$, on aurait", r"\mathcal F_x$ on aurait")
add(120, "proof of (5.10.15) (ii), l. 2", "(I, 2.4.2) with a bold chapter numeral", "plain numeral", "convention",
    "(I, 2.4.2)", r"(\textbf{I}, 2.4.2)", 2)
add(120, "Proposition (5.10.16), label (i)", "item label (i) upright roman",
    "\\item[(i)] comes out italic in the italic statement", "convention",
    r"\item[(i)] Pour qu'en", r"\item[\textup{(i)}] Pour qu'en", 6, note=LABEL)
add(120, "Proposition (5.10.16) (i): '(notations de (5.10.12))'",
    "'(notations de' italic, the reference (5.10.12) upright (enlarged crop)", "(5.10.12) italic (statement environment)",
    "convention", "(notations de (5.10.12))", r"(notations de \textup{(5.10.12)})", 6)
add(120, "Proposition (5.10.16), label (ii)", "item label (ii) upright roman",
    "\\item[(ii)] comes out italic in the italic statement", "convention",
    r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons", 6, note=LABEL)
add(120, "Proposition (5.10.16) (ii): '(voir dans (5.11.2) des conditions suffisantes pour qu'il en soit ainsi)'",
    "the parenthesis upright roman except 'suffisantes', which is italic (enlarged crop)",
    "the whole parenthesis italic (statement environment)", "convention",
    "(voir dans" + NL + "(5.11.2) des conditions suffisantes pour qu'il en soit ainsi)",
    r"\textup{(voir dans" + NL + r"(5.11.2) des conditions} suffisantes \textup{pour qu'il en soit ainsi)}", 6,
    note="'suffisantes' is italic in the print (emphasis inside the roman parenthesis) and stays italic.")
add(120, "Proposition (5.10.16) (ii): 'codim(X—U, X) >= 2; en outre'", "long dash for set difference X—U",
    "X-U", "convention", r"(X-U,X)\geq2$;", r"(X\setmin U,X)\geq2$;", 7, note=SETMIN)
add(120, "Proposition (5.10.16), label (iii)", "item label (iii) upright roman",
    "\\item[(iii)] comes out italic in the italic statement", "convention",
    r"\item[(iii)]", r"\item[\textup{(iii)}]", 6, note=LABEL)
add(120, "Proposition (5.10.16) (iii): 'que dans (ii),'", "reference (ii) upright inside the italic statement",
    "(ii) italic (statement environment)", "convention",
    r"que dans (ii), $X'$", r"que dans \textup{(ii)}, $X'$", 6)
add(120, "Proposition (5.10.16) (iii), end: 'est tel que codim({x}-, X) = codim({x'}-, X').'",
    "the formula ends the line of running text 'le point x = g(x') est tel que codim(...) = codim(...).'",
    "set as a display \\[ ... \\]", "other",
    r"\[" + NL + r"\operatorname{codim}(\overline{\{x\}},X)" + NL + r"=\operatorname{codim}(\overline{\{x'\}},X')." + NL + r"\]",
    r"$\operatorname{codim}(\overline{\{x\}},X)" + NL + r"=\operatorname{codim}(\overline{\{x'\}},X')$.",
    note="Formula displayed where the print has it inline; no connecting word lost.")
add(120, "Proposition (5.10.16), label (iv)", "item label (iv) upright roman",
    "\\item[(iv)] comes out italic in the italic statement", "convention",
    r"\item[(iv)]", r"\item[\textup{(iv)}]", 6, note=LABEL)
add(120, "Proposition (5.10.16) (iv): 'celles de (ii),'", "reference (ii) upright inside the italic statement",
    "(ii) italic (statement environment)", "convention",
    "celles de (ii), soit", r"celles de \textup{(ii)}, soit", 6)
add(120, "proof of (5.10.16) (iii), l. 2: 'donc dim(O_{X',x'}) <= dim(X'_x) <= dim(X_x) = dim(O_{X,x}) en vertu de (5.4.1)'",
    "the inequalities are in the running text (same line as 'donc' and 'en vertu de (5.4.1)')",
    "set as a display \\[ ... \\]", "other",
    r"\[" + NL + r"\dim(\mathcal O_{X',x'})\leq\dim(X'_x)\leq\dim(X_x)" + NL + r"=\dim(\mathcal O_{X,x})" + NL + r"\]",
    r"$\dim(\mathcal O_{X',x'})\leq\dim(X'_x)\leq\dim(X_x)" + NL + r"=\dim(\mathcal O_{X,x})$",
    note="Formula displayed where the print has it inline; no connecting word lost.")
add(120, "proof of (5.10.16) (iii), l. 4: 'appliqué à O_X, on aurait prof(...)'",
    "comma after O_X (enlarged crop)", "no comma: 'appliqué à $\\mathcal O_X$ on aurait'", "punctuation",
    r"appliqué à $\mathcal O_X$ on aurait", r"appliqué à $\mathcal O_X$, on aurait")
add(120, "proof of (5.10.16) (iii), l. 5: 'On a donc x∈X—Z^(2), et par suite'", "long dash for set difference",
    "X-Z^{(2)}", "convention", r"x\in X-Z^{(2)}$, et par suite", r"x\in X\setmin Z^{(2)}$, et par suite", 7,
    note=SETMIN)
add(120, "end of page", "the sentence runs on over the page break: p. 121 begins 'premiers associés de codimension 1, ...' flush left",
    "blank line before \\oldpage[IV-2]{121}: paragraph break inside the sentence", "other",
    "pas de cycles" + NL + NL, "pas de cycles" + NL,
    note="Apply together with the p. 121 entry that removes the blank line after the marker (GLOBAL_ISSUES 20).")

# ---------------- page 121 ----------------
add(121, "top of page", "page begins mid-sentence: 'premiers associés de codimension 1, l'hypothèse ...' (no indent, same paragraph as p. 120)",
    "\\oldpage[IV-2]{121} followed by a blank line", "other",
    r"\oldpage[IV-2]{121}" + NL + NL + "premiers", r"\oldpage[IV-2]{121}" + NL + "premiers",
    note="Apply together with the p. 120 entry 'pas de cycles' (blank line before the marker).")
add(121, "Proposition (5.10.17), l. 3: 'Supposons que A^(1) soit une A-algèbre finie.'",
    "'finie' upright roman (emphasis) inside the italic statement (enlarged crop)",
    "finie italic like the rest of the statement", "convention",
    r"$A$-algèbre finie. Alors:", r"$A$-algèbre \emph{finie}. Alors:", 6)
add(121, "Proposition (5.10.17), label (i)", "item label (i) upright roman",
    "\\item[(i)] comes out italic in the italic statement", "convention",
    r"\item[(i)]", r"\item[\textup{(i)}]", 6, note=LABEL)
add(121, "Proposition (5.10.17), label (ii)", "item label (ii) upright roman",
    "\\item[(ii)] comes out italic in the italic statement", "convention",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", 6, note=LABEL)
add(121, "Proposition (5.10.17) (ii): 'codim(X—U, X) >= 2'", "long dash for set difference X—U",
    "X-U", "convention", "(X-U,X)", r"(X\setmin U,X)", 7, note=SETMIN)
add(121, "Proposition (5.10.17), label (iii)", "item label (iii) upright roman",
    "\\item[(iii)] comes out italic in the italic statement", "convention",
    r"\item[(iii)]", r"\item[\textup{(iii)}]", 6, note=LABEL)
add(121, "Proposition (5.10.17), label (iv)", "item label (iv) upright roman",
    "\\item[(iv)] comes out italic in the italic statement", "convention",
    r"\item[(iv)]", r"\item[\textup{(iv)}]", 6, note=LABEL)
add(121, "proof of (5.10.17), l. 2: 'est la Z^(2)-clôture de X = Spec(A)'",
    "'clôture' italic (enlarged crop)", "roman, no \\emph", "italics",
    r"$Z^{(2)}$-clôture de", r"$Z^{(2)}$-\emph{clôture} de")
add(121, "proof of (5.10.17) (iv): 'Montrons que G = H^0_{X/Z^(2)(X)}(f_*(O_Y)) est cohérent'",
    "the formula is in the running text (same line as 'Montrons que'; 'est' ends the line)",
    "set as a display \\[ ... \\]", "other",
    r"\[" + NL + r"\mathcal G=\mathcal H^0_{X/Z^{(2)}(X)}(f_*(\mathcal O_Y))" + NL + r"\]",
    r"$\mathcal G=\mathcal H^0_{X/Z^{(2)}(X)}(f_*(\mathcal O_Y))$",
    note="Formula displayed where the print has it inline; no connecting word lost.")
add(121, "proof of (5.10.17) (iv): 'cela prouve a fortiori que'", "'a fortiori' italic (enlarged crop)",
    "roman, no \\emph", "italics", "cela prouve a fortiori que", r"cela prouve \emph{a fortiori} que")

# ---------------- page 122 ----------------
add(122, "heading 5.11", "'5.11. Critères de cohérence pour les Modules H^0_{X/Z}(F).' (final full stop)",
    "no full stop in the \\subsection title", "punctuation",
    r"$\mathcal H^0_{X/Z}(\mathcal F)$}{Critères", r"$\mathcal H^0_{X/Z}(\mathcal F)$.}{Critères",
    note="Subsection titles lack the printed full stop (GLOBAL_ISSUES 43/58); same form as the p. 46 fix.")
add(122, "Proposition (5.11.1), l. 3: 'Ass(F) ∩ (X—Z)'", "long dash for set difference X—Z",
    "X-Z", "convention", r"\cap(X-Z)$", r"\cap(X\setmin Z)$", 7, note=SETMIN)
add(122, "Proposition (5.11.1), label a)", "item label a) upright roman",
    "\\item[a)] comes out italic in the italic statement", "convention",
    r"\item[a)]", r"\item[\textup{a)}]", 6, note="Lettered labels are upright in this statement (GLOBAL_ISSUES 22).")
add(122, "Proposition (5.11.1), label b)", "item label b) upright roman",
    "\\item[b)] comes out italic in the italic statement", "convention",
    r"\item[b)]", r"\item[\textup{b)}]", 6)
add(122, "Proposition (5.11.1), label c)", "item label c) upright roman",
    "\\item[c)] comes out italic in the italic statement", "convention",
    r"\item[c)]", r"\item[\textup{c)}]", 6)
add(122, "Proposition (5.11.1): 'les trois conditions a), b), c) sont équivalentes'",
    "'a), b), c)' upright roman inside the italic statement", "italic (statement environment)", "convention",
    "trois conditions a), b), c) sont", r"trois conditions \textup{a), b), c)} sont", 6)
add(122, "Proposition (5.11.1): 'lorsqu'en outre une des propriétés suivantes'",
    "'une' upright roman (emphasis) inside the italic statement", "une italic like the rest of the statement",
    "convention", "lorsqu'en outre une" + NL + "des", r"lorsqu'en outre \emph{une}" + NL + "des", 6)
add(122, "Proposition (5.11.1), label (i)", "item label (i) upright roman",
    "\\item[(i)] comes out italic in the italic statement", "convention",
    r"\item[(i)]", r"\item[\textup{(i)}]", 6, note=LABEL)
add(122, "Proposition (5.11.1) (i): '(auquel cas on dit aussi que X est localement immersible dans un schéma régulier).'",
    "'(auquel cas on dit aussi que X est' and the closing parenthesis upright roman; only 'localement immersible dans un schéma régulier' italic",
    "the whole parenthesis italic (statement environment)", "convention",
    "(auquel cas on dit aussi que $X$ est" + NL + "localement immersible dans un schéma régulier).",
    r"\textup{(auquel cas on dit aussi que $X$ est}" + NL + r"localement immersible dans un schéma régulier\textup{)}.", 6)
add(122, "Proposition (5.11.1), label (ii)", "item label (ii) upright roman",
    "\\item[(ii)] comes out italic in the italic statement", "convention",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", 6, note=LABEL)
add(122, "Proposition (5.11.1) (ii): 'universellement caténaire (5.6.2)'",
    "reference (5.6.2) upright inside the italic statement", "(5.6.2) italic (statement environment)", "convention",
    "caténaire" + NL + "(5.6.2) et", "caténaire" + NL + r"\textup{(5.6.2)} et", 6)
add(122, "Proposition (5.11.1) (ii): 'son normalisé (II, 6.3.8)'",
    "(II, 6.3.8) with a bold chapter numeral, the reference upright", "plain numeral, italic (statement environment)",
    "convention", "(II, 6.3.8)", r"\textup{(\textbf{II}, 6.3.8)}", 2,
    note="The edit also sets the reference upright (convention 6, next entry).")
add(122, "Proposition (5.11.1) (ii): 'son normalisé (II, 6.3.8)'",
    "reference upright inside the italic statement", "italic (statement environment)", "convention", conv=6,
    note="Included in the convention-2 edit of the previous entry.")
add(122, "proof of (5.11.1), l. 10: 'H^0_{X/Z}(G_α) est isomorphe à H^0_{Y_α/Z_α}(O_{Y_α})'",
    "no (h_α)_*: 'est isomorphe à H^0_{Y_α/Z_α}(O_{Y_α}); cela prouve' (enlarged crop)",
    "$(h_\\alpha)_*(\\mathcal H^0_{Y_\\alpha/Z_\\alpha}(\\mathcal O_{Y_\\alpha}))$", "extra",
    r"$(h_\alpha)_*(\mathcal H^0_{Y_\alpha/Z_\alpha}(\mathcal O_{Y_\alpha}))$;",
    r"$\mathcal H^0_{Y_\alpha/Z_\alpha}(\mathcal O_{Y_\alpha})$;",
    note="The print identifies the O_{Y_α}-Module with its direct image under the closed immersion h_α; the same "
         "wording recurs on p. 123, so it is not treated as a misprint. The TeX adds (h_α)_*(...).")
add(122, "proof of (5.11.1), l. 11: 'cela prouve que a) entraîne b). Pour voir que b) entraîne a),'",
    "a), b), b), a) italic", "upright", "italics",
    "que a) entraîne b). Pour voir que b) entraîne a),",
    r"que \emph{a)} entraîne \emph{b)}. Pour voir que \emph{b)} entraîne \emph{a)},")
add(122, "proof of (5.11.1), display 0 → F_{i+1} → F_i → F_i/F_{i+1}",
    "the display ends with a full stop, yet the sentence continues 'du fait que ...' in lower case (enlarged crop: round dot on the baseline, no tail)",
    "comma: silently corrected", "misprint_in_print",
    r"\mathcal F_i/\mathcal F_{i+1}," + NL + r"\]", r"\mathcal F_i/\mathcal F_{i+1}." + NL + r"\]",
    conf="medium", corrected=r"\mathcal F_i/\mathcal F_{i+1},",
    note="The TeX silently corrects; the fix restores the printed full stop. Correct reading: a comma.")
add(122, "proof of (5.11.1): 'et enfin de (0_I, 5.3.3)'", "bold 0 in (0_I, 5.3.3)", "plain 0", "convention",
    r"(0$_\mathrm I$, 5.3.3)", r"(\textbf{0}$_\mathrm I$, 5.3.3)", 2)
add(122, "proof of (5.11.1): 'et (I, 6.1.1)'", "(I, 6.1.1) with a bold chapter numeral", "plain numeral", "convention",
    "(I, 6.1.1)", r"(\textbf{I}, 6.1.1)", 2)
add(122, "proof of (5.11.1): 'lorsque F est irredondant;'", "'irredondant' italic (enlarged crop)", "roman, no \\emph",
    "italics", "est irredondant;", r"est \emph{irredondant};")
add(122, "end of page", "the sentence runs on over the page break: p. 123 begins 'il existe un entier r tel que ...' flush left",
    "blank line before \\oldpage[IV-2]{123}: paragraph break inside the sentence", "other",
    "$B$-module de type fini," + NL + NL, "$B$-module de type fini," + NL,
    note="Apply together with the p. 123 entry that removes the blank line after the marker (GLOBAL_ISSUES 20).")

# ---------------- page 123 ----------------
add(123, "top of page", "page begins mid-sentence: 'il existe un entier r tel que m^r N = 0; ...' (no indent, same paragraph as p. 122)",
    "\\oldpage[IV-2]{123} followed by a blank line", "other",
    r"\oldpage[IV-2]{123}" + NL + NL + "il existe", r"\oldpage[IV-2]{123}" + NL + "il existe",
    note="Apply together with the p. 122 entry '$B$-module de type fini,' (blank line before the marker).")
add(123, "2nd paragraph, l. 2: '(moyennant b))'", "b) italic", "upright b)", "italics",
    "(moyennant b))", r"(moyennant \emph{b)})")
P_NOTE = "The print names this sheaf with a script P (enlarged crop), not the G of p. 122; six occurrences on the page."
add(123, "2nd paragraph, l. 3: 'H^0_{X/Z}(P) est cohérent, où'", "script P", "\\mathcal G", "symbol",
    r"(\mathcal G)$ est cohérent, où", r"(\mathcal P)$ est cohérent, où", note=P_NOTE)
add(123, "2nd paragraph, l. 3: 'où P = (A/p)~'", "script P", "\\mathcal G", "symbol",
    r"$\mathcal G=(A/", r"$\mathcal P=(A/", note=P_NOTE)
add(123, "2nd paragraph, l. 4: 'le support de P est un ensemble fermé'", "script P", "\\mathcal G", "symbol",
    r"$\mathcal G$ est un ensemble", r"$\mathcal P$ est un ensemble", note=P_NOTE)
add(123, "2nd paragraph, l. 6: 'H^0_{X/Z}(P) = 0'", "script P", "\\mathcal G", "symbol",
    r"(\mathcal G)=0$", r"(\mathcal P)=0$", note=P_NOTE)
add(123, "2nd paragraph, l. 6: 'on a P = (h_α)_*(O_{Y_α})'", "script P", "\\mathcal G", "symbol",
    r"$\mathcal G=(h_\alpha)_*", r"$\mathcal P=(h_\alpha)_*", note=P_NOTE)
add(123, "2nd paragraph, l. 7: 'H^0_{X/Z}(P) est isomorphe à'", "script P", "\\mathcal G", "symbol",
    r"(\mathcal G)$ est isomorphe", r"(\mathcal P)$ est isomorphe", note=P_NOTE)
add(123, "2nd paragraph, l. 7: 'est isomorphe à H^0_{Y_α/Z_α}(O_{Y_α}), donc'",
    "no (h_α)_*: 'est isomorphe à H^0_{Y_α/Z_α}(O_{Y_α}), donc est cohérent' (enlarged crop)",
    "$(h_\\alpha)_*(\\mathcal H^0_{Y_\\alpha/Z_\\alpha}(\\mathcal O_{Y_\\alpha}))$", "extra",
    r"$(h_\alpha)_*(\mathcal H^0_{Y_\alpha/Z_\alpha}(\mathcal O_{Y_\alpha}))$,",
    r"$\mathcal H^0_{Y_\alpha/Z_\alpha}(\mathcal O_{Y_\alpha})$,",
    note="Same as p. 122: the print identifies the sheaf with its direct image; the TeX adds (h_α)_*(...).")
add(123, "2nd paragraph, end: 'l'hypothèse b).'", "b) italic", "upright b)", "italics",
    "l'hypothèse b).", r"l'hypothèse \emph{b)}.")
add(123, "3rd paragraph, l. 1: 'que a) entraîne c).'", "a) and c) italic", "upright a), c)", "italics",
    "que a) entraîne c)", r"que \emph{a)} entraîne \emph{c)}")
add(123, "3rd paragraph, l. 2: '(i), (ii), c) entraîne b).'", "c) and b) italic ((i), (ii) upright)", "upright c), b)",
    "italics", "(ii), c) entraîne b)", r"(ii), \emph{c)} entraîne \emph{b)}")
add(123, "Corollaire (5.11.2), label (i)", "item label (i) upright roman",
    "\\item[(i)] comes out italic in the italic statement", "convention",
    r"\item[(i)]", r"\item[\textup{(i)}]", 6, note=LABEL)
add(123, "Corollaire (5.11.2), label (ii)", "item label (ii) upright roman",
    "\\item[(ii)] comes out italic in the italic statement", "convention",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", 6, note=LABEL)
add(123, "proof of (5.11.2) (i), l. 2: 'est ouvert dans X moyennant'", "'ouvert' italic (enlarged crop)",
    "roman, no \\emph", "italics", "est ouvert dans $X$ moyennant", r"est \emph{ouvert} dans $X$ moyennant")
add(123, "proof of (5.11.2) (i), l. 2: 'Z = X—U'", "long dash for set difference X—U", "X-U", "convention",
    "$Z=X-U$", r"$Z=X\setmin U$", 7, note=SETMIN)
add(123, "proof of (5.11.2) (ii), l. 1: 'un anneau noethérien intègre'", "'noethérien' italic (enlarged crop)",
    "roman, no \\emph", "italics", "un anneau noethérien" + NL + "intègre", r"un anneau \emph{noethérien}" + NL + "intègre")
add(123, "proof of (5.11.2) (ii): 'S = A—p'", "long dash for set difference A—p", "A-\\mathfrak p", "convention",
    r"$S=A-\mathfrak p$", r"$S=A\setmin\mathfrak p$", 7, note=SETMIN)
add(123, "end of page", "the sentence runs on over the page break: p. 124 begins 'une A_p-algèbre finie; ...' flush left",
    "blank line before \\oldpage[IV-2]{124}: paragraph break inside the sentence", "other",
    "est par hypothèse" + NL + NL, "est par hypothèse" + NL,
    note="Apply together with the p. 124 entry that removes the blank line after the marker (GLOBAL_ISSUES 20).")

# ---------------- page 124 ----------------
add(124, "top of page", "page begins mid-sentence: 'une A_p-algèbre finie; comme S^-1 p' ...' (no indent, same paragraph as p. 123)",
    "\\oldpage[IV-2]{124} followed by a blank line", "other",
    r"\oldpage[IV-2]{124}" + NL + NL + "une", r"\oldpage[IV-2]{124}" + NL + "une",
    note="Apply together with the p. 123 entry 'est par hypothèse' (blank line before the marker).")
add(124, "Remarque (5.11.3), l. 3: 'on suppose seulement que A est caténaire.'",
    "'caténaire' italic (emphasis) in the roman remark (enlarged crop)", "no \\emph", "italics",
    "est" + NL + "caténaire. Un exemple", "est" + NL + r"\emph{caténaire}. Un exemple",
    note="Judged with the remark body roman (document-wide remark item).")
add(124, "Corollaire (5.11.4), l. 2: 'U = X—Z'", "long dash for set difference X—Z", "X-Z", "convention",
    "$U=X-Z$", r"$U=X\setmin Z$", 7, note=SETMIN)
add(124, "Corollaire (5.11.4), l. 3: 'on ait codim({x}- ∩ Z, {x}-) >= 2.'",
    "the formula ends the line of running text 'pour tout x ∈ Ass(F), on ait codim(...) >= 2.'",
    "set as a display \\[ ... \\]", "other",
    r"\[" + NL + r"\operatorname{codim}(\overline{\{x\}}\cap Z,\overline{\{x\}})\geq2." + NL + r"\]",
    r"$\operatorname{codim}(\overline{\{x\}}\cap Z,\overline{\{x\}})\geq2$.",
    note="Formula displayed where the print has it inline; no connecting word lost.")
add(124, "Corollaire (5.11.4), label (i)", "item label (i) upright roman",
    "\\item[(i)] comes out italic in the italic statement", "convention",
    r"\item[(i)]", r"\item[\textup{(i)}]", 6, note=LABEL)
add(124, "Corollaire (5.11.4), label (ii)", "item label (ii) upright roman",
    "\\item[(ii)] comes out italic in the italic statement", "convention",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", 6, note=LABEL)
add(124, "Corollaire (5.11.4) (ii): '(ce qui signifie, par définition, que tout point x∈X admet un voisinage ouvert affine dont l'anneau est'",
    "this part of the parenthesis upright roman; 'universellement japonais' after it italic",
    "italic (statement environment)", "convention",
    "(ce qui signifie, par définition, que tout point $x\\in X$ admet un" + NL
    + "voisinage ouvert affine dont l'anneau est universellement",
    r"\textup{(ce qui signifie, par définition, que tout point $x\in X$ admet un" + NL
    + r"voisinage ouvert affine dont l'anneau est} universellement", 6)
add(124, "Corollaire (5.11.4) (ii): '(0, 23.1.1)).'",
    "bold 0; the reference and the closing parenthesis upright", "plain 0, italic (statement environment)",
    "convention", "japonais (0," + NL + "23.1.1)).", r"japonais \textup{(\textbf{0}," + NL + "23.1.1))}.", 2,
    note="The edit also sets the reference and the closing parenthesis upright (convention 6, next entry).")
add(124, "Corollaire (5.11.4) (ii): '(0, 23.1.1)).'", "reference and closing parenthesis upright",
    "italic (statement environment)", "convention", conv=6,
    note="Included in the convention-2 edit of the previous entry.")
add(124, "proof of (5.11.4), l. 1: 'On sait (I, 9.4.7)'", "(I, 9.4.7) with a bold chapter numeral", "plain numeral",
    "convention", "(I, 9.4.7)", r"(\textbf{I}, 9.4.7)", 2)
add(124, "proof of (5.11.4), l. 1: 'un sous-O_X-Module cohérent G de i_*(F)'", "'cohérent' italic (enlarged crop)",
    "roman, no \\emph", "italics", "Module cohérent" + NL + r"$\mathcal G$ de", r"Module \emph{cohérent}" + NL + r"$\mathcal G$ de",
    note="The later 'au O_X-Module cohérent G, en notant' is roman in the print, as in the TeX.")
add(124, "Corollaire (5.11.5), l. 2: 'Ass(F) ⊂ X—Z'", "long dash for set difference X—Z", "X-Z", "convention",
    r"\subset X-Z$", r"\subset X\setmin Z$", 7, note=SETMIN)
add(124, "Corollaire (5.11.5), label a)", "item label a) upright roman",
    "\\item[a)] comes out italic in the italic statement", "convention",
    r"\item[a)]", r"\item[\textup{a)}]", 6, note="Lettered labels are upright in this statement (GLOBAL_ISSUES 22).")
add(124, "Corollaire (5.11.5), label d)", "item label d) upright roman",
    "\\item[d)] comes out italic in the italic statement", "convention",
    r"\item[d)]", r"\item[\textup{d)}]", 6)
add(124, "Corollaire (5.11.5) d): '(ou seulement pour une famille filtrante'",
    "'(ou seulement pour une' upright roman, 'famille filtrante' italic", "italic (statement environment)",
    "convention", "(ou seulement pour une" + NL + "famille", r"\textup{(ou seulement pour une}" + NL + "famille", 6,
    note="The parenthesis continues on p. 125 ('croissante de parties fermées T de Z, de réunion Z)'), checked there.")
add(124, "end of page", "the sentence runs on over the page break: p. 125 continues 'croissante de parties fermées ...' inside item d)",
    "blank line before \\oldpage[IV-2]{125}: paragraph break inside the sentence", "other",
    "filtrante" + NL + NL, "filtrante" + NL,
    note="Apply together with the p. 125 fix of the blank line after \\oldpage[IV-2]{125} (source: '\\oldpage[IV-2]{125}\\n\\ncroissante'), which lies outside this batch.")

# ---------------- checks ----------------
bad = []
for i, f in enumerate(findings):
    if f["fix"] is None:
        continue
    c = texts[f["page"]].count(f["fix"]["old"])
    if c != 1:
        bad.append((i, f["page"], c, f["fix"]["old"]))
# overlapping old strings on the same page
for n in texts:
    spans = []
    for i, f in enumerate(findings):
        if f["page"] == n and f["fix"]:
            s = texts[n].find(f["fix"]["old"])
            spans.append((s, s + len(f["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            bad.append(("overlap", n, a[2], b[2]))
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("findings:", len(findings), "problems:", bad)
for n in sorted(counts):
    print(n, counts[n])
