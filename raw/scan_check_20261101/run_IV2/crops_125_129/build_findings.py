import json
import pathlib

RUN = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_IV2")
OUT = RUN / "findings_125_129.json"
NL = "\u23ce"  # placeholder for a line break inside old/new strings


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
A = L.append

# ---------------- page 125 ----------------
A(F(125, "top of page (Corollaire (5.11.5) d), continued from p. 124)",
    "the page continues the sentence of p. 124 ('pour une famille filtrante | croissante de parties fermees ...'), flush left, no new paragraph",
    "\\oldpage[IV-2]{125} stands between two blank lines: paragraph break inside item d)",
    "marker", None, "high",
    r"\oldpage[IV-2]{125}⏎⏎croissante", r"\oldpage[IV-2]{125}⏎croissante",
    "The blank line BEFORE the marker ('famille filtrante\\n\\n\\oldpage[IV-2]{125}') lies in p. 124's segment and must be removed with this edit (outside this page's segment)."))
A(F(125, "Corollaire (5.11.5) d), l. 1: 'de parties fermees T de Z, de reunion Z)'",
    "only 'croissante' is italic; 'de parties fermees T de Z, de reunion Z)' is upright roman (end of the parenthesis begun on p. 124)",
    "italic (statement environment)",
    "convention", 6, "high",
    r"de parties fermées $T$ de $Z$, de réunion $Z$),", r"\textup{de parties fermées $T$ de $Z$, de réunion $Z$)},"))
A(F(125, "Corollaire (5.11.5) d), l. 1: 'i_*(F|X-T)'",
    "X—T with the long dash", "X-T (minus sign)", "convention", 7, "high",
    r"$i_*(\mathcal F\vert X-T)$ (où", r"$i_*(\mathcal F\vert X\setmin T)$ (où"))
A(F(125, "Corollaire (5.11.5) d), l. 1: 'i : X-T -> X'",
    "X—T with the long dash", "X-T (minus sign)", "convention", 7, "high",
    r"$i:X-T\to X$", r"$i:X\setmin T\to X$"))
A(F(125, "Corollaire (5.11.5), last sentence: 'hypotheses (i), (ii) de'",
    "'(i), (ii)' upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"hypothèses (i), (ii) de", r"hypothèses \textup{(i), (ii)} de"))
A(F(125, "Corollaire (5.11.5), last sentence: '(5.11.1), a) et'",
    "'(5.11.1), a)' upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"(5.11.1), a) et", r"\textup{(5.11.1), a)} et"))
A(F(125, "Corollaire (5.11.5), last sentence: 'd) sont equivalentes'",
    "'d)' upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"d) sont⏎équivalentes", r"\textup{d)} sont⏎équivalentes"))
A(F(125, "proof of (5.11.5), l. 1: 'Ass(i_*(F|X-T))'",
    "X—T with the long dash", "X-T (minus sign)", "convention", 7, "high",
    r"\operatorname{Ass}(i_*(\mathcal F\vert X-T))", r"\operatorname{Ass}(i_*(\mathcal F\vert X\setmin T))"))
A(F(125, "proof of (5.11.5), display i_*(F|X-T) -> H^0_{X/Z}(F)",
    "X—T with the long dash", "X-T (minus sign)", "convention", 7, "high",
    r"i_*(\mathcal F\vert X-T)\longrightarrow", r"i_*(\mathcal F\vert X\setmin T)\longrightarrow"))
A(F(125, "proof of (5.11.5), after the display: 'sont injectives'",
    "'injectives' italic", "upright, no \\emph", "italics", None, "high",
    r"sont injectives;", r"sont \emph{injectives};"))
A(F(125, "proof of (5.11.5): 'le fait que a) implique d)'",
    "a) and d) italic", "upright a), d)", "italics", None, "high",
    r"le fait que a) implique d) est", r"le fait que \emph{a)} implique \emph{d)} est"))
A(F(125, "proof of (5.11.5): 'Inversement, la condition d) implique'",
    "d) italic", "upright d)", "italics", None, "high",
    r"la condition d) implique,", r"la condition \emph{d)} implique,"))
A(F(125, "proof of (5.11.5): 'en vertu de (5.11.1) que codim(T n Y_a, Y_a) >= 2'",
    "no comma after (5.11.1) (enlarged crop)", "'(5.11.1), que' (comma added)", "punctuation", None, "high",
    r"en vertu de (5.11.1), que", r"en vertu de (5.11.1) que"))
A(F(125, "Corollaire (5.11.6), label a)",
    "item label a) upright roman", "\\item[a)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]"))
A(F(125, "Corollaire (5.11.6) a): '(notation de (5.11.2))'",
    "the parenthesis is upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high", r"(notation de (5.11.2))", r"\textup{(notation de (5.11.2))}"))
A(F(125, "Corollaire (5.11.6), label b)",
    "item label b) upright roman", "\\item[b)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]"))
A(F(125, "Corollaire (5.11.6) b): 'x in Ass(F) n (X-Z)'",
    "X—Z with the long dash", "X-Z (minus sign)", "convention", 7, "high",
    r"telle que pour tout⏎$x\in\operatorname{Ass}(\mathcal F)\cap(X-Z)$",
    r"telle que pour tout⏎$x\in\operatorname{Ass}(\mathcal F)\cap(X\setmin Z)$"))
A(F(125, "Corollaire (5.11.6), label c)",
    "item label c) upright roman", "\\item[c)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]"))
A(F(125, "Corollaire (5.11.6) c): '(ou U = X-T)'",
    "X—T with the long dash", "X-T (minus sign)", "convention", 7, "high",
    r"(où $U=X-T$)", r"(où $U=X\setmin T$)"))
A(F(125, "Corollaire (5.11.6), label d)",
    "item label d) upright roman", "\\item[d)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[d)]", r"\item[\textup{d)}]"))
A(F(125, "Corollaire (5.11.6) d): 'l'anneau  cap_{p not> J} B_p  est une B-algebre finie'",
    "the intersection is in the running text, at the start of the line 'cap B_p est une B-algebre finie.'",
    "set as a display \\[ ... \\]", "formula", None, "high",
    r"l'anneau⏎\[⏎\bigcap_{\mathfrak p\not\supset\mathfrak J}B_\mathfrak p⏎\]⏎est une",
    r"l'anneau⏎$\bigcap_{\mathfrak p\not\supset\mathfrak J}B_\mathfrak p$⏎est une",
    "Formula displayed where the print has it in the running text."))
A(F(125, "Corollaire (5.11.6), display 'a) <=> b) => c) <=> d)'",
    "no full stop after d) (enlarged crop)", "'\\mathrm d).' (full stop added)", "punctuation", None, "high",
    r"\mathrm d).", r"\mathrm d)"))
A(F(125, "Corollaire (5.11.6), after the display: 'En outre, les conditions ...'",
    "'En outre' begins a new indented paragraph after the display", "no blank line after \\]: the text continues the paragraph",
    "other", None, "high",
    r"\]⏎En outre,", r"\]⏎⏎En outre,",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47 pattern)."))
A(F(125, "Corollaire (5.11.6): 'les conditions a), b), c) et'",
    "'a), b), c)' upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"conditions a), b), c) et", r"conditions \textup{a), b), c)} et"))
A(F(125, "Corollaire (5.11.6): 'et d) sont verifiees'",
    "'d)' upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"d) sont vérifiées", r"\textup{d)} sont vérifiées"))
A(F(125, "Corollaire (5.11.6), label (i)",
    "item label (i) upright roman", "\\item[(i)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]"))
A(F(125, "Corollaire (5.11.6), label (ii)",
    "item label (ii) upright roman", "\\item[(ii)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]"))
A(F(125, "proof of (5.11.6): 'Si la condition b) est verifiee'",
    "b) italic", "upright b)", "italics", None, "high",
    r"Si la condition b) est", r"Si la condition \emph{b)} est"))
A(F(125, "proof of (5.11.6): 'et a fortiori un B-module'",
    "'a fortiori' italic", "upright, no \\emph", "italics", None, "high",
    r"et a fortiori un", r"et \emph{a fortiori} un"))
A(F(125, "proof of (5.11.6): 'supposons a) verifiee'",
    "a) italic", "upright a)", "italics", None, "high",
    r"supposons a) vérifiée", r"supposons \emph{a)} vérifiée"))
A(F(125, "proof of (5.11.6): 'tel que pour tout x in Ass(F) n (X-Z)'",
    "X—Z with the long dash", "X-Z (minus sign)", "convention", 7, "high",
    r"tel que pour tout⏎$x\in\operatorname{Ass}(\mathcal F)\cap(X-Z)$",
    r"tel que pour tout⏎$x\in\operatorname{Ass}(\mathcal F)\cap(X\setmin Z)$"))
A(F(125, "proof of (5.11.6): 'le resultat de a);'",
    "a) italic", "upright a)", "italics", None, "high",
    r"le résultat de a);", r"le résultat de \emph{a)};"))
A(F(125, "proof of (5.11.6), last line: 'la condition a) (compte tenu'",
    "a) italic", "upright a)", "italics", None, "high",
    r"la condition a) (compte", r"la condition \emph{a)} (compte"))
A(F(125, "end of page",
    "the sentence runs on over the page break: p. 126 begins 'et du fait que Ass(O_{Y_a}) ...' flush left",
    "blank line before \\oldpage[IV-2]{126}: paragraph break inside the sentence",
    "marker", None, "high",
    r"tenu de (5.10.2)⏎⏎", r"tenu de (5.10.2)⏎",
    "Apply together with the p. 126 entry that removes the blank line after the marker."))

# ---------------- page 126 ----------------
A(F(126, "top of page",
    "page begins mid-sentence: 'et du fait que Ass(O_{Y_a}) est reduit ...' flush left, same paragraph as p. 125",
    "\\oldpage[IV-2]{126} followed by a blank line", "marker", None, "high",
    r"\oldpage[IV-2]{126}⏎⏎et du fait", r"\oldpage[IV-2]{126}⏎et du fait",
    "Apply together with the p. 125 entry 'tenu de (5.10.2)' (blank line before the marker)."))
A(F(126, "proof of (5.11.6), l. 2: 'et b) decoule alors de (5.11.1)'",
    "b) italic", "upright b)", "italics", None, "high",
    r"et b) découle", r"et \emph{b)} découle"))
A(F(126, "proof of (5.11.6), 2nd paragraph, l. 1: 'Pour voir que c) entraine d), ... en appliquant c) au'",
    "c), d), c) italic", "upright", "italics", None, "high",
    r"Pour voir que c) entraîne d), on raisonne comme ci-dessus en appliquant c) au",
    r"Pour voir que \emph{c)} entraîne \emph{d)}, on raisonne comme ci-dessus en appliquant \emph{c)} au"))
A(F(126, "proof of (5.11.6), 2nd paragraph: 'on prouve que d) entraine c) ... l'equivalence de a) et b)'",
    "d), c), a), b) italic", "upright", "italics", None, "high",
    r"on prouve que d) entraîne c) en utilisant encore l'équivalence de⏎a) et b) dans",
    r"on prouve que \emph{d)} entraîne \emph{c)} en utilisant encore l'équivalence de⏎\emph{a)} et \emph{b)} dans"))
A(F(126, "proof of (5.11.6): 'Il est evident que c) est un cas particulier de b).'",
    "c) and b) italic", "upright", "italics", None, "high",
    r"Il est évident que c) est un cas particulier de b).",
    r"Il est évident que \emph{c)} est un cas particulier de \emph{b)}."))
A(F(126, "proof of (5.11.6): 'Enfin, le fait que a) (et par suite'",
    "a) italic", "upright a)", "italics", None, "high",
    r"Enfin, le fait que a) (et", r"Enfin, le fait que \emph{a)} (et"))
A(F(126, "Remarques (5.11.7) (i), l. 1: 'la condition d) implique a)'",
    "d) and a) italic in the roman remark", "no \\emph", "italics", None, "high",
    r"la condition d) implique a) sans", r"la condition \emph{d)} implique \emph{a)} sans",
    "Judged as if the remark body were roman (document-wide remark environment)."))
A(F(126, "Remarques (5.11.7) (i): 'lorsque X est un schema local.'",
    "'local' italic in the roman remark", "no \\emph", "italics", None, "high",
    r"un schéma local.", r"un schéma \emph{local}.",
    "Judged as if the remark body were roman."))
A(F(126, "Remarques (5.11.7) (i): 'lorsque A est un anneau local noetherien'",
    "'local' italic in the roman remark", "no \\emph", "italics", None, "high",
    r"$A$ est un anneau local noethérien", r"$A$ est un anneau \emph{local} noethérien",
    "Judged as if the remark body were roman."))
A(F(126, "Remarques (5.11.7) (i): 'les quatre proprietes a), b), c), d) de (5.11.6)'",
    "a), b), c), d) italic in the roman remark", "no \\emph", "italics", None, "high",
    r"propriétés a), b), c),⏎d) de (5.11.6)",
    r"propriétés \emph{a)}, \emph{b)}, \emph{c)},⏎\emph{d)} de (5.11.6)",
    "Judged as if the remark body were roman."))
A(F(126, "Remarques (5.11.7) (ii), l. 1: 'la propriete a) de (5.11.6)'",
    "a) italic in the roman remark", "no \\emph", "italics", None, "high",
    r"la propriété a) de", r"la propriété \emph{a)} de",
    "Judged as if the remark body were roman."))
A(F(126, "Remarques (5.11.7) (ii): 'de tout anneau de fractions S^{-1}A'",
    "'anneau de fractions' italic in the roman remark", "no \\emph", "italics", None, "high",
    r"tout anneau de fractions $S^{-1}A$", r"tout \emph{anneau de fractions} $S^{-1}A$",
    "Judged as if the remark body were roman."))
A(F(126, "Remarques (5.11.7) (ii): 'de toute A-algebre finie C'",
    "'finie' italic in the roman remark", "no \\emph", "italics", None, "high",
    r"$A$-algèbre finie $C$", r"$A$-algèbre \emph{finie} $C$",
    "Judged as if the remark body were roman."))
A(F(126, "heading 5.12",
    "'5.12. Relations entre les proprietes d'un anneau local noetherien A et d'un anneau quotient A/tA.' (final full stop)",
    "no full stop in the \\subsection title", "punctuation", None, "high",
    r"d'un anneau quotient $A/tA$}{", r"d'un anneau quotient $A/tA$.}{",
    "Subsection titles lack the printed full stop (GLOBAL_ISSUES 43); same form as the 3.4 fix (p. 46)."))
A(F(126, "Proposition (5.12.1), l. 2: 'systeme de parametres (0, 16.3.6)'",
    "(0, 16.3.6): bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.6)", r"\textup{(\textbf{0}, 16.3.6)}",
    "One edit for this finding and the next (convention 6): bold numeral and the upright reference together."))
A(F(126, "Proposition (5.12.1), l. 2: same reference '(0, 16.3.6)'",
    "the reference is upright inside the italic statement", "italic (statement environment)",
    "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."))
A(F(126, "Proposition (5.12.1), l. 3: 'X_1 l'ouvert complementaire X-X_0'",
    "X—X_0 with the long dash", "X-X_0 (minus sign)", "convention", 7, "high",
    r"$X-X_0$", r"$X\setmin X_0$"))
A(F(126, "Proposition (5.12.1), l. 4-5: '(ce qui sera le cas si A est equidimensionnel ... (0, 16.5.12))'",
    "the whole parenthesis is upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"(ce qui sera le⏎cas si $A$ est équidimensionnel et quotient d'un anneau local régulier (0,⏎16.5.12))",
    r"\textup{(ce qui sera le⏎cas si $A$ est équidimensionnel et quotient d'un anneau local régulier (\textbf{0},⏎16.5.12))}",
    "One edit for this finding and the next (convention 2): upright parenthesis and bold 0 together."))
A(F(126, "Proposition (5.12.1), l. 5: '(0, 16.5.12)'",
    "(0, 16.5.12): bold 0", "plain 0", "convention", 2, "high", None, None,
    "Covered by the edit of the preceding finding (convention 6), which adds the \\textbf{0}."))
A(F(126, "proof of (5.12.1), l. 2: 'lorsque Z est ferme :'",
    "'ferme' italic", "upright, no \\emph", "italics", None, "high",
    r"est fermé: en effet", r"est \emph{fermé}: en effet"))
A(F(126, "proof of (5.12.1), l. 4: 'on aura aussi codim(Z_0,X_0) = inf_a(codim(...)) <= inf_a(codim(Z_a,X)) = codim(Z,X).'",
    "the formula is in the running text (same line as 'aura aussi'), and each inf is followed by a parenthesis: inf_a(codim(X_0 n Z_a, X_0)) <= inf_a(codim(Z_a, X))",
    "set as a display \\[ ... \\], without the parentheses after inf_a", "formula", None, "high",
    r"on aura aussi⏎\[⏎\operatorname{codim}(Z_0,X_0)⏎=\inf_\alpha\operatorname{codim}(X_0\cap Z_\alpha,X_0)⏎\leq\inf_\alpha\operatorname{codim}(Z_\alpha,X)⏎=\operatorname{codim}(Z,X).⏎\]⏎Supposons",
    r"on aura aussi⏎$\operatorname{codim}(Z_0,X_0)⏎=\inf_\alpha(\operatorname{codim}(X_0\cap Z_\alpha,X_0))⏎\leq\inf_\alpha(\operatorname{codim}(Z_\alpha,X))⏎=\operatorname{codim}(Z,X)$.⏎Supposons",
    "Formula displayed where the print has it in the running text; one edit also restores the parentheses (next finding). 'Supposons donc' continues the paragraph flush left in the print."))
A(F(126, "proof of (5.12.1), same formula: 'inf_a(codim(X_0 n Z_a, X_0))', 'inf_a(codim(Z_a, X))'",
    "parentheses after each inf_a", "\\inf_\\alpha\\operatorname{codim}(...) without the outer parentheses",
    "formula", None, "high", None, None,
    "Covered by the edit of the preceding finding."))
A(F(126, "proof of (5.12.1), last display: 'codim(Z, X) = dim(X) - dim(Z)'",
    "long dash for the subtraction", "minus sign", "convention", 7, "high",
    r"=\dim(X)-\dim(Z)", r"=\dim(X)\setmin\dim(Z)",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
A(F(126, "end of page",
    "the sentence runs on: p. 127 begins 'en vertu de (0, 14.3.5.1).' flush left after the display",
    "blank line after \\] before \\oldpage[IV-2]{127}: new paragraph", "marker", None, "high",
    r"⏎\]⏎⏎", r"⏎\]⏎",
    "Apply together with the p. 127 entry that removes the blank line after the marker."))

# ---------------- page 127 ----------------
A(F(127, "top of page",
    "page begins mid-sentence: 'en vertu de (0, 14.3.5.1).' flush left, same paragraph as the display on p. 126",
    "\\oldpage[IV-2]{127} followed by a blank line", "marker", None, "high",
    r"\oldpage[IV-2]{127}⏎⏎en vertu", r"\oldpage[IV-2]{127}⏎en vertu",
    "Apply together with the p. 126 entry (blank line before the marker)."))
A(F(127, "l. 1: '(0, 14.3.5.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 14.3.5.1)", r"(\textbf{0}, 14.3.5.1)"))
A(F(127, "l. 2: 'de dimension dim(X) - 1'", "long dash for the subtraction", "minus sign",
    "convention", 7, "high", r"$\dim(X)-1$", r"$\dim(X)\setmin 1$", "Subtraction (GLOBAL_ISSUES 23)."))
A(F(127, "l. 2: 'en vertu de (0, 16.3.4); on a donc aussi'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.4); on a", r"(\textbf{0}, 16.3.4); on a"))
A(F(127, "display, 'dim(X_0) - dim(Z_0)'", "long dash for the subtraction", "minus sign",
    "convention", 7, "high", r"\dim(X_0)-\dim(Z_0)", r"\dim(X_0)\setmin\dim(Z_0)", "Subtraction (GLOBAL_ISSUES 23)."))
A(F(127, "display, 'dim(X) - 1 - dim(Z_0)', first dash", "long dash for the subtraction", "minus sign",
    "convention", 7, "high", r"=\dim(X)-1-\dim(Z_0)", r"=\dim(X)\setmin 1\setmin\dim(Z_0)",
    "One edit for this finding and the next (both dashes of the same term). Subtraction (GLOBAL_ISSUES 23)."))
A(F(127, "display, 'dim(X) - 1 - dim(Z_0)', second dash", "long dash for the subtraction", "minus sign",
    "convention", 7, "high", None, None, "Covered by the edit of the preceding finding."))
A(F(127, "end of the display 'codim(Z_0, X_0) = ... = dim(X) - 1 - dim(Z_0)'",
    "no full stop after the display (enlarged crop)", "'\\dim(Z_0).' (full stop added)", "punctuation", None, "high",
    r"(Z_0).⏎\]", r"(Z_0)⏎\]"))
A(F(127, "after the display: 'Mais on a dim(Z_0) >= dim(Z) - 1'",
    "'Mais on a' begins a new indented paragraph", "no blank line after \\]: the text continues the paragraph",
    "other", None, "high", r"\]⏎Mais on a", r"\]⏎⏎Mais on a",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47 pattern)."))
A(F(127, "'Mais on a dim(Z_0) >= dim(Z) - 1'", "long dash for the subtraction", "minus sign",
    "convention", 7, "high", r"\dim(Z)-1$", r"\dim(Z)\setmin 1$", "Subtraction (GLOBAL_ISSUES 23)."))
A(F(127, "'(0, 16.3.4), ce qui acheve de prouver'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.4), ce qui", r"(\textbf{0}, 16.3.4), ce qui"))
A(F(127, "proof of (5.12.2): 'donc biequidimensionnel puisque A est local'",
    "'biequidimensionnel' italic", "upright, no \\emph", "italics", None, "high",
    r"donc biéquidimensionnel puisque", r"donc \emph{biéquidimensionnel} puisque"))
A(F(127, "proof of (5.12.2): 'parametres pour M (0, 16.4.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.4.1)", r"(\textbf{0}, 16.4.1)"))
A(F(127, "end of page (Remarque (5.12.3))",
    "the sentence runs on: p. 128 begins 'est irreductible et de dimension 1' flush left",
    "blank line before \\oldpage[IV-2]{128}: paragraph break inside the sentence", "marker", None, "high",
    r"que $\operatorname{Spec}(A/tA)$⏎⏎", r"que $\operatorname{Spec}(A/tA)$⏎",
    "Apply together with the p. 128 entry that removes the blank line after the marker."))

# ---------------- page 128 ----------------
A(F(128, "top of page",
    "page begins mid-sentence: 'est irreductible et de dimension 1, ...' flush left (end of Remarque (5.12.3))",
    "\\oldpage[IV-2]{128} followed by a blank line", "marker", None, "high",
    r"\oldpage[IV-2]{128}⏎⏎est irréductible", r"\oldpage[IV-2]{128}⏎est irréductible",
    "Apply together with the p. 127 entry (blank line before the marker)."))
A(F(128, "proof of (5.12.5): 'en vertu de (0, 17.3.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0,⏎17.3.2)", r"(\textbf{0},⏎17.3.2)"))
A(F(128, "proof of (5.12.5): 'de (0, 17.1.8) que'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 17.1.8)", r"(\textbf{0}, 17.1.8)"))
A(F(128, "proof of (5.12.5), first display: 'k <= codim(Z'_0, X_0) <= codim(Z_0, X_0).'",
    "k \u2a7d codim(Z'_0, X_0): the same slanted less-or-equal sign as the second inequality (enlarged crop)",
    "k<\\operatorname{codim}(Z'_0,X_0) (strict)", "misprint_in_print", None, "high",
    r"k<\operatorname{codim}(Z'_0,X_0)", r"k\leq\operatorname{codim}(Z'_0,X_0)",
    "The TeX silently corrects the print. X_0 satisfies (R_k) means codim(Z'_0, X_0) > k (Z'_0 the non-regular locus); with \u2a7d the conclusion that X satisfies (R_k) would not follow. Not in the authors' Liste 3 of errata.",
    corrected=r"k<\operatorname{codim}(Z'_0,X_0)"))
A(F(128, "proof of (5.12.5), after the first display: 'Mais, puisque A est equidimensionnel'",
    "'Mais, puisque' begins a new indented paragraph", "no blank line after \\]: the text continues the paragraph",
    "other", None, "high", r"\]⏎Mais, puisque", r"\]⏎⏎Mais, puisque",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47 pattern)."))
A(F(128, "proof of (5.12.5): 'on a, d'apres (5.12.1)' before the second display",
    "no comma after (5.12.1) (enlarged crop)", "'(5.12.1),' (comma added)", "punctuation", None, "high",
    r"d'après (5.12.1),", r"d'après (5.12.1)"))
A(F(128, "Remarque (5.12.6): 'P(U, V) = U(U^2+V^2) + (U^2 - V^2)'", "long dash in U^2—V^2", "minus sign",
    "convention", 7, "high", r"(U^2-V^2)", r"(U^2\setmin V^2)", "Subtraction (GLOBAL_ISSUES 23)."))
A(F(128, "Remarque (5.12.6), display 'p = CW + CP(U-T, V)'", "long dash in U—T", "minus sign",
    "convention", 7, "high", r"CP(U-T,V)", r"CP(U\setmin T,V)", "Subtraction (GLOBAL_ISSUES 23)."))
A(F(128, "Remarque (5.12.6), after the display: 'Considerons alors l'anneau local A = C/pq'",
    "'Considerons alors' begins a new indented paragraph", "no blank line after \\]: the text continues the paragraph",
    "other", None, "high", r"\]⏎Considérons alors", r"\]⏎⏎Considérons alors",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47 pattern)."))
A(F(128, "Remarque (5.12.6): 'l'ideal C(U-T) + CV + CW'", "long dash in U—T", "minus sign",
    "convention", 7, "high", r"$C(U-T)+CV+CW$", r"$C(U\setmin T)+CV+CW$", "Subtraction (GLOBAL_ISSUES 23)."))

# ---------------- page 129 ----------------
A(F(129, "Proposition (5.12.8), l. 3: '(notation de (5.10.17))'",
    "the parenthesis is upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high", r"(notation de (5.10.17))", r"\textup{(notation de (5.10.17))}"))
A(F(129, "Proposition (5.12.8), l. 3-4: '(ce qui aura lieu par exemple lorsque A possede l'une des proprietes (i), (ii) de (5.11.6))'",
    "the whole parenthesis is upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"(ce qui aura⏎lieu par exemple lorsque $A$ possède l'une des propriétés (i), (ii) de⏎(5.11.6))",
    r"\textup{(ce qui aura⏎lieu par exemple lorsque $A$ possède l'une des propriétés (i), (ii) de⏎(5.11.6))}"))
A(F(129, "Proposition (5.12.8), label (i)",
    "item label (i) upright roman", "\\item[(i)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]"))
A(F(129, "Proposition (5.12.8) (i): '(necessairement de hauteur 1 en vertu du Hauptidealsatz (0, 16.3.2), mais ... a A/tA)'",
    "the whole parenthesis is upright roman inside the italic statement", "italic (statement environment)",
    "convention", 6, "high",
    r"(nécessairement de hauteur 1 en vertu du⏎Hauptidealsatz (0, 16.3.2), mais on ne suppose pas que ce soit le seul idéal⏎premier associé à $A/tA$)",
    r"\textup{(nécessairement de hauteur 1 en vertu du⏎Hauptidealsatz (\textbf{0}, 16.3.2), mais on ne suppose pas que ce soit le seul idéal⏎premier associé à $A/tA$)}",
    "One edit for this finding and the next (convention 2): upright parenthesis and bold 0 together."))
A(F(129, "Proposition (5.12.8) (i): '(0, 16.3.2)'", "bold 0", "plain 0", "convention", 2, "high", None, None,
    "Covered by the edit of the preceding finding (convention 6), which adds the \\textbf{0}."))
A(F(129, "Proposition (5.12.8), label (ii)",
    "item label (ii) upright roman", "\\item[(ii)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]"))
A(F(129, "Proposition (5.12.8), label (iii)",
    "item label (iii) upright roman", "\\item[(iii)] comes out italic in the italic statement",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]"))
A(F(129, "proof of (5.12.8), l. 2: 'dont le point generique z est tel que j_z = p'",
    "Fraktur j (descender below the baseline, enlarged crop), the usual EGA notation j_x for the ideal of a point",
    "\\mathfrak i_z (Fraktur i)", "symbol", None, "high",
    r"$\mathfrak i_z=\mathfrak p$", r"$\mathfrak j_z=\mathfrak p$",
    "ega4-2-fr.tex writes \\mathfrak j_ everywhere else (13 times); this is its only \\mathfrak i_."))
A(F(129, "proof of (5.12.8): 'A_p est un anneau de valuation discrete dont t/1'",
    "'anneau de valuation discrete' italic", "upright, no \\emph", "italics", None, "high",
    r"un anneau de⏎valuation discrète dont", r"un \emph{anneau de⏎valuation discrète} dont"))
A(F(129, "proof of (5.12.8): 'n'est contenu que dans une seule des composantes'",
    "'une seule' italic", "upright, no \\emph", "italics", None, "high",
    r"dans une seule des", r"dans \emph{une seule} des"))
A(F(129, "proof of (5.12.8): 'et l'on a par suite (5.1.8) codim(X_i n Z, X_i) = codim(X_j n Z, X_j) = 1, quel que soit j != i'",
    "the formula is in the running text (line 'codim(...) = codim(...) = 1, quel que soit j != i. Comme A est sup-')",
    "set as a display \\[ ... \\]", "formula", None, "high",
    r"par suite (5.1.8)⏎\[⏎\operatorname{codim}(X_i\cap Z,X_i)⏎=\operatorname{codim}(X_j\cap Z,X_j)=1,⏎\]⏎quel que soit",
    r"par suite (5.1.8)⏎$\operatorname{codim}(X_i\cap Z,X_i)⏎=\operatorname{codim}(X_j\cap Z,X_j)=1$,⏎quel que soit",
    "Formula displayed where the print has it in the running text."))
A(F(129, "proof of (5.12.8): 'dim(X_i) != dim(X_j) (0, 14.3.3.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 14.3.3.1)", r"(\textbf{0}, 14.3.3.1)"))
A(F(129, "proof of (5.12.8): 'qu'il n'y a qu'un seul ideal premier minimal dans A'",
    "'un seul ideal premier minimal' italic", "upright, no \\emph", "italics", None, "high",
    r"n'y a qu'un seul idéal premier minimal", r"n'y a qu'\emph{un seul idéal premier minimal}"))
A(F(129, "proof of (5.12.8): 'cela entraine qu'il est integre.'",
    "'integre' italic", "upright, no \\emph", "italics", None, "high",
    r"qu'il est intègre.", r"qu'il est \emph{intègre}."))
A(F(129, "proof of (5.12.8): 'Hauptidealsatz (0, 16.3.2); or,'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.2); or", r"(\textbf{0}, 16.3.2); or"))
A(F(129, "proof of (5.12.8): 'si l'on pose S = A - p'", "A—p with the long dash", "A-p (minus sign)",
    "convention", 7, "high", r"$S=A-\mathfrak p$", r"$S=A\setmin\mathfrak p$"))
A(F(129, "proof of (5.12.8): 'qu'il n'existe qu'un seul ideal premier p' de A''",
    "'un seul' italic", "upright, no \\emph", "italics", None, "high",
    r"qu'il n'existe qu'un⏎seul idéal", r"qu'il n'existe qu'\emph{un⏎seul} idéal"))
A(F(129, "proof of (5.12.8): 'et a fortiori un seul ideal premier p^(1)'",
    "'a fortiori' italic", "upright, no \\emph", "italics", None, "high",
    r"et a⏎fortiori un seul", r"et \emph{a⏎fortiori} un seul"))
A(F(129, "proof of (5.12.8): 'et l'on a A_p = A'_{p'} = A^(1)_{p^(1)}. Notons maintenant'",
    "the formula is in the running text (same line as 'l'on a' and 'Notons maintenant que')",
    "set as a display \\[ ... \\]", "formula", None, "high",
    r"et l'on a⏎\[⏎A_{\mathfrak p}=A'_{\mathfrak p'}⏎=A^{(1)}_{\mathfrak p^{(1)}}.⏎\]⏎Notons",
    r"et l'on a⏎$A_{\mathfrak p}=A'_{\mathfrak p'}⏎=A^{(1)}_{\mathfrak p^{(1)}}$.⏎Notons",
    "Formula displayed where the print has it in the running text."))
A(F(129, "end of page",
    "the sentence runs on: p. 130 begins 'immerges (5.7.7).' ('n'a pas d'ideaux premiers associes | immerges')",
    "blank line before \\oldpage[IV-2]{130}: paragraph break inside the sentence", "marker", None, "high",
    r"premiers associés⏎⏎", r"premiers associés⏎",
    "The blank line AFTER the marker ('\\oldpage[IV-2]{130}\\n\\nimmergés') lies in p. 130's segment and must be removed with this edit (outside this page's segment)."))

json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------------- checks ----------------
ok = True
pages = {}
for p in range(125, 130):
    t = (RUN / ("page_%d.tex" % p)).read_text(encoding="utf-8").replace("\r\n", "\n")
    # segment as apply_fixes sees it: from the marker to the end (header comment line excluded)
    seg = t[t.index("\\oldpage"):]
    pages[p] = seg
for x in L:
    fx = x["fix"]
    if fx is None:
        continue
    c = pages[x["page"]].count(fx["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", x["page"], c, repr(fx["old"][:60]))
# sequential application in listed order
for p in range(125, 130):
    s = pages[p]
    for x in L:
        if x["page"] != p or x["fix"] is None:
            continue
        o, n = x["fix"]["old"], x["fix"]["new"]
        c = s.count(o)
        if c != 1:
            ok = False
            print("SEQ FAIL", p, c, repr(o[:60]))
            continue
        s = s.replace(o, n)
    (RUN / "crops_125_129" / ("applied_%d.tex" % p)).write_text(s, encoding="utf-8", newline="\n")
from collections import Counter
cnt = Counter()
for x in L:
    k = "convention" if x["kind"] == "convention" else ("misprint" if x["kind"] == "misprint_in_print" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(125, 130):
    print(p, "normal", cnt[(p, "normal")], "convention", cnt[(p, "convention")], "misprint", cnt[(p, "misprint")])
print("total", len(L), "OK" if ok else "PROBLEMS")
