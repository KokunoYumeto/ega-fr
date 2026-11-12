"""Build findings_135_139.json and check that every fix's old string occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_135_139.json"
NL = "⏎"  # placeholder for a line break inside raw strings


def t(s):
    return None if s is None else s.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": t(scan), "tex": t(tex), "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if nofix else {"old": t(old), "new": t(new)}}
    if corrected is not None:
        d["corrected"] = t(corrected)
    d["note"] = note
    return d


L = []

# ---------------------------------------------------------------- page 134 (outside the batch)
L.append(F(134, "end of the p. 134 segment, just before \\oldpage[IV-2]{135} ('pour trouver des | critères')",
           "p. 135 begins mid-sentence ('... pour trouver des critères permettant ...'): no paragraph break",
           r"pour trouver⏎des⏎⏎\oldpage[IV-2]{135}", "other", None, "high",
           r"pour trouver⏎des⏎⏎", r"pour trouver⏎des⏎",
           "OUTSIDE pages 135-139: 'old' lies in the p. 134 segment (checked unique in run_IV2/page_134.tex). "
           "Apply together with the p. 135 entry that removes the blank line after \\oldpage[IV-2]{135} "
           "(GLOBAL_ISSUES 20). The p. 130-134 checker may report the same edit."))

# ---------------------------------------------------------------- page 135
L.append(F(135, "top of page, after \\oldpage[IV-2]{135}",
           "'critères permettant ...' continues the sentence of p. 134; no paragraph break",
           r"\oldpage[IV-2]{135}, blank line, critères", "other", None, "high",
           r"\oldpage[IV-2]{135}⏎⏎critères", r"\oldpage[IV-2]{135}⏎critères",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the "
           "page-134 entry (blank line before the marker, in the p. 134 segment)."))
L.append(F(135, "heading 6.1", "6.1. Platitude et dimension.", r"\subsection{Platitude et dimension}",
           "punctuation", None, "high",
           r"\subsection{Platitude et dimension}", r"\subsection{Platitude et dimension.}",
           "Printed final full stop (GLOBAL_ISSUES 43/58); same fix as heading 2.1 on p. 5."))
L.append(F(135, "Proposition (6.1.1), the parenthesis '(autrement dit, ... dans Spec(B))'",
           "the whole parenthesis is roman inside the italic statement; 'Alors on a' is italic again",
           "inside the italic proposition environment (comes out italic)", "convention", 6, "high",
           r"(autrement dit, qu'aucune composante irréductible de⏎"
           r"$\operatorname{Spec}(B/\mathfrak pB)$ ne soit contenue dans l'image réciproque⏎"
           r"du point fermé $\mathfrak m$ de $\operatorname{Spec}(A)$ dans⏎"
           r"$\operatorname{Spec}(B)$).",
           r"\textup{(autrement dit, qu'aucune composante irréductible de⏎"
           r"$\operatorname{Spec}(B/\mathfrak pB)$ ne soit contenue dans l'image réciproque⏎"
           r"du point fermé $\mathfrak m$ de $\operatorname{Spec}(A)$ dans⏎"
           r"$\operatorname{Spec}(B)$)}.",
           "One edit, so that the \\textup group stays balanced."))
L.append(F(135, "proof of (6.1.1), 'on a (0, 16.3.4)'", "(0, 16.3.4) with bold 0", "(0, 16.3.4)",
           "convention", 2, "high", "(0, 16.3.4)", r"(\textbf{0}, 16.3.4)"))
L.append(F(135, "proof of (6.1.1), display dim(A') = dim(A) — 1",
           "dim(A') = dim(A) — 1 (long dash: bar 41 px at 300 dpi, the = bars 34-35 px)", r"\dim(A)-1",
           "convention", 7, "high", r"\dim(A)-1", r"\dim(A)\setmin 1",
           "Subtraction set with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision "
           "(not defined in EGA_IV2_FR.tex)."))
L.append(F(135, "proof of (6.1.1), same display, dim(B') = dim(B) — 1",
           "dim(B') = dim(B) — 1 (long dash, bar 41 px)", r"\dim(B)-1",
           "convention", 7, "high", r"\dim(B)-1", r"\dim(B)\setmin 1", "As the previous entry."))
L.append(F(135, "Corollaire (6.1.2), 'Si N est un A-module plat (resp. si B est un A-module plat)'",
           "'(resp.' roman inside the italic statement (enlarged crop)", "(resp. si $B$ ... (italic environment)",
           "convention", 6, "high", r"(resp. si $B$", r"\textup{(resp.} si $B$"))
L.append(F(135, "Corollaire (6.1.2), line after (6.1.2.1): '(resp. (6.1.1.1)).'",
           "'(resp. (6.1.1.1))' all roman (enlarged crop)", "(resp. (6.1.1.1)). inside the italic environment",
           "convention", 6, "high", r"(resp. (6.1.1.1)).", r"\textup{(resp. (6.1.1.1))}."))
L.append(F(135, "end of page, '... premier p≠m de A,' before \\oldpage[IV-2]{136}",
           "p. 136 continues the sentence ('de A, | toute composante irréductible ...'); no paragraph break",
           r"de $A$, followed by a blank line before the p. 136 marker", "other", None, "high",
           r"\mathfrak m$ de $A$,⏎⏎", r"\mathfrak m$ de $A$,⏎",
           "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the "
           "p. 136 entry that removes the blank line after \\oldpage[IV-2]{136}."))

# ---------------------------------------------------------------- page 136
L.append(F(136, "top of page, after \\oldpage[IV-2]{136}",
           "'toute composante irréductible ...' continues the sentence of p. 135, flush left",
           r"\oldpage[IV-2]{136}, blank line, toute", "other", None, "high",
           r"\oldpage[IV-2]{136}⏎⏎toute", r"\oldpage[IV-2]{136}⏎toute",
           "Apply together with the p. 135 entry that removes the blank line before the marker."))
L.append(F(136, "line 1, 'f^{-1}(V(p)) domine V(p)'", "'domine' italic (enlarged crop)", "domine upright",
           "italics", None, "high", r"domine⏎$V(\mathfrak p)$", r"\emph{domine}⏎$V(\mathfrak p)$"))
L.append(F(136, "Corollaire (6.1.3), '(c'est-à-dire (0, 16.2.1) que mB soit un idéal de définition de B)'",
           "'(c'est-à-dire (0, 16.2.1) que mB soit un' and 'de B)' roman, 'idéal de définition' italic "
           "(enlarged crop); bold 0",
           "the whole parenthesis italic (environment); plain 0", "convention", 6, "high",
           r"(c'est-à-dire (0, 16.2.1) que⏎$\mathfrak mB$ soit un idéal de définition de $B$).",
           r"\textup{(c'est-à-dire (\textbf{0}, 16.2.1) que⏎$\mathfrak mB$ soit un} idéal de définition "
           r"\textup{de $B$)}.",
           "One edit; it also sets the bold 0 of the next finding (convention 2)."))
L.append(F(136, "Corollaire (6.1.3), (0, 16.2.1)", "bold 0", "(0, 16.2.1)", "convention", 2, "high",
           None, None, "Covered by the edit of the preceding finding (convention 6), which also bolds the 0.",
           nofix=True))
L.append(F(136, "Corollaire (6.1.3), '(ce qui a lieu en particulier si B est un A-module plat)'",
           "'(ce qui a lieu en particulier si B est un A-module' roman, 'plat' italic (enlarged crop)",
           "all italic (environment)", "convention", 6, "high",
           r"(ce qui a lieu en particulier si $B$ est un $A$-module plat)",
           r"\textup{(ce qui a lieu en particulier si $B$ est un $A$-module} plat)"))
L.append(F(136, "Corollaire (6.1.4), display (6.1.4.1)",
           "codim(f^{-1}(Z), X) ⩽ codim(Z, Y) with no full stop (enlarged crop; a speck far to the right is not a stop)",
           r"\operatorname{codim}(Z,Y).", "punctuation", None, "high",
           r"\leq\operatorname{codim}(Z,Y).", r"\leq\operatorname{codim}(Z,Y)",
           "Full stop after a display that the print lacks (cf. GLOBAL_ISSUES 73)."))
L.append(F(136, "Corollaire (6.1.4), after (6.1.4.1)",
           "'En outre, si f est quasi-plat ...' begins a new indented paragraph",
           r"\end{equation} followed directly by 'En outre' (no paragraph break)", "other", None, "high",
           r"\end{equation}⏎En outre, si $f$", r"\end{equation}⏎⏎En outre, si $f$",
           "Paragraph break of the print (as GLOBAL_ISSUES 47)."))
L.append(F(136, "Corollaire (6.1.4), 'si f est quasi-plat (2.3.3)'", "(2.3.3) upright inside the italic statement",
           "(2.3.3) italic (environment)", "convention", 6, "high",
           r"quasi-plat (2.3.3) les", r"quasi-plat \textup{(2.3.3)} les",
           "Reference printed upright inside the italic statement."))
L.append(F(136, "Corollaire (6.1.4), 'les deux membres de (6.1.4.1)'", "(6.1.4.1) upright inside the italic statement",
           "(6.1.4.1) italic (environment)", "convention", 6, "high",
           r"membres de (6.1.4.1) sont", r"membres de \textup{(6.1.4.1)} sont",
           "Reference printed upright inside the italic statement."))
L.append(F(136, "proof of (6.1.4), 'points maximaux de Z (0_I, 2.1.8)'", "bold 0 in (0_I, 2.1.8)",
           r"$(0_{\mathrm I}, 2.1.8)$", "convention", 2, "high",
           r"$(0_{\mathrm I}, 2.1.8)$", r"$(\mathbf{0}_{\mathrm I}, 2.1.8)$"))
L.append(F(136, "proof of (6.1.4), 'dim(O_x ⊗_{O_y} k(x)) = 0'", "bold italic k in k(x) (enlarged crop)",
           "k(x)", "convention", 1, "high", r"k(x))=0", r"\boldsymbol{k}(x))=0"))
L.append(F(136, "proof of (6.1.4), 'en chacun de ces points maximaux x on a dim(O_x ⊗_{O_y} k(x)) = 0'",
           "k(x)", "k(x) (the printed reading is kept)", "misprint_in_print", None, "high",
           None, None,
           "The local ring of x in its fibre f^{-1}(y) is O_x ⊗_{O_y} k(y), of dimension 0 since x is a maximal point "
           "of the fibre; (6.1.1) is then applied with A = O_y, whose residue field is k(y). With k(x) the claim can "
           "fail (k(x)⊗_{k(y)}k(x) need not have dimension 0). Not in the Err_IV list. The TeX keeps k(x): no "
           "diplomatic edit. Corrected reading, after the convention-1 edit of the previous finding: "
           "\\boldsymbol{k}(y).",
           corrected=r"\boldsymbol{k}(y)", nofix=True))
L.append(F(136, "Proposition (6.1.5), label 1°", "1° upright (old-style 1, superior o)",
           r"\item[1\textsuperscript{o}] (italic in the environment)", "convention", 6, "high",
           r"\item[1\textsuperscript{o}]", r"\item[\textup{1\textsuperscript{o}}]",
           "Label printed upright inside the italic statement (as EGA I p. 175)."))
L.append(F(136, "Proposition (6.1.5), label 2°", "2° upright", r"\item[2\textsuperscript{o}]", "convention", 6,
           "high", r"\item[2\textsuperscript{o}]", r"\item[\textup{2\textsuperscript{o}}]", "As label 1°."))
L.append(F(136, "Proposition (6.1.5), label 3°", "3° upright", r"\item[3\textsuperscript{o}]", "convention", 6,
           "high", r"\item[3\textsuperscript{o}]", r"\item[\textup{3\textsuperscript{o}}]", "As label 1°."))
L.append(F(136, "Proposition (6.1.5), 'Alors M est un A-module plat.'",
           "'Alors M ...' begins an indented line after the conditions",
           r"\end{enumerate} followed directly by 'Alors' (comes out flush left)", "other", None, "high",
           r"\end{enumerate}⏎Alors $M$", r"\end{enumerate}⏎⏎Alors $M$",
           "Paragraph after the list, indented as printed (same form as earlier \\end{enumerate} fixes)."))
L.append(F(136, "proof of (6.1.5), 'puisqu'il est régulier (0, 17.1.4)'", "bold 0", "(0, 17.1.4)",
           "convention", 2, "high", "(0, 17.1.4)", r"(\textbf{0}, 17.1.4)"))
L.append(F(136, "proof of (6.1.5), 'on sait alors (0, 17.1.8)'", "bold 0", "(0, 17.1.8)",
           "convention", 2, "high", "(0, 17.1.8)", r"(\textbf{0}, 17.1.8)"))
L.append(F(136, "proof of (6.1.5), 'dim(A') = dim(A) — 1'",
           "long dash (bar 42 px at 300 dpi, the = bars 34-35 px)", r"\dim(A)-1", "convention", 7, "high",
           r"\dim(A)-1$", r"\dim(A)\setmin 1$", "Subtraction set with the long dash (GLOBAL_ISSUES 23)."))
L.append(F(136, "proof of (6.1.5), line 2 from the bottom: 'et en vertu de (5.5.1.2) on a'", "(5.5.1.2)",
           "(5.5.1.2) (the printed reading is kept)", "misprint_in_print", None, "high", None, None,
           "Authors' erratum, EGA IV part 4, liste 3, item (IV, 6.1.5): 'Ligne 2 du bas de la p. 136, remplacer "
           "(5.5.1.2) par (0, 16.3.9.2)' (ega4-errata-addenda-list3-fr.tex). The TeX keeps the printed reference: "
           "no diplomatic edit.",
           corrected=r"(\textbf{0}, 16.3.9.2)", nofix=True))
L.append(F(136, "last display, last factor", "dim_{B'⊗_{A'}k}(M'⊗_A k): subscript A without prime (enlarged crop)",
           r"(M'\otimes_{A'}k)", "formula", None, "high", r"(M'\otimes_{A'}k);", r"(M'\otimes_Ak);",
           "Not a misprint: M'⊗_A k = M'⊗_{A'} k; the TeX normalised the subscript."))
L.append(F(136, "end of page, after the last display",
           "p. 137 begins 'on conclut donc ...' flush left, continuing the sentence after the display",
           r"\] followed by a blank line before the p. 137 marker", "other", None, "high",
           r"\]⏎⏎", r"\]⏎",
           "'old' is the final \\] and blank line of the p. 136 segment (unique on the page; it does not overlap "
           "the formula edit above). Apply together with the p. 137 entry that removes the blank line after "
           "\\oldpage[IV-2]{137}."))

# ---------------------------------------------------------------- page 137
L.append(F(137, "top of page, after \\oldpage[IV-2]{137}",
           "'on conclut donc de (0, 16.3.4) que l'on a' flush left (continues the sentence of p. 136)",
           r"\oldpage[IV-2]{137}, blank line, on conclut", "other", None, "high",
           r"\oldpage[IV-2]{137}⏎⏎on conclut", r"\oldpage[IV-2]{137}⏎on conclut",
           "Apply together with the p. 136 entry that removes the blank line before the marker."))
L.append(F(137, "line 1, 'on conclut donc de (0, 16.3.4)'", "bold 0", "(0, 16.3.4)", "convention", 2, "high",
           "(0, 16.3.4)", r"(\textbf{0}, 16.3.4)"))
L.append(F(137, "'(i) dim_{B'}(M') = dim_B(M) — 1'", "long dash (bar 41 px, the = bars 34 px)", r"\dim_B(M)-1",
           "convention", 7, "high", r"\dim_B(M)-1$", r"\dim_B(M)\setmin 1$",
           "Subtraction set with the long dash (GLOBAL_ISSUES 23)."))
L.append(F(137, "'cela signifie que x est M-régulier (0, 16.1.9 et 16.5.5)'", "'régulier' italic (enlarged crop)",
           "M-régulier upright", "italics", None, "high",
           r"$x$ est⏎$M$-régulier", r"$x$ est⏎$M$-\emph{régulier}",
           "Only this occurrence; 'M-régulier par (i)' at the end of the proof is upright, as in the TeX."))
L.append(F(137, "'M-régulier (0, 16.1.9 et 16.5.5); (ii)'", "bold 0", "(0, 16.1.9 et 16.5.5)", "convention", 2,
           "high", "(0, 16.1.9 et 16.5.5); (ii)", r"(\textbf{0}, 16.1.9 et 16.5.5); (ii)"))
L.append(F(137, "'en vertu de (i) et de (0, 16.1.9 et 16.5.5) et que A' est régulier'", "bold 0",
           "(0, 16.1.9 et 16.5.5)", "convention", 2, "high",
           "de (0, 16.1.9 et 16.5.5) et que", r"de (\textbf{0}, 16.1.9 et 16.5.5) et que"))
L.append(F(137, "'on déduit alors de (0_III, 10.2.7)'", "bold 0 in (0_III, 10.2.7)",
           r"$(0_{\mathrm{III}}, 10.2.7)$", "convention", 2, "high",
           r"$(0_{\mathrm{III}}, 10.2.7)$", r"$(\mathbf{0}_{\mathrm{III}}, 10.2.7)$"))
L.append(F(137, "heading 6.2", "6.2. Platitude et dimension projective.",
           r"\subsection{Platitude et dimension projective}", "punctuation", None, "high",
           r"\subsection{Platitude et dimension projective}", r"\subsection{Platitude et dimension projective.}",
           "Printed final full stop (GLOBAL_ISSUES 43/58)."))
L.append(F(137, "Proposition (6.2.1), label (i)", "(i) upright", r"\item[(i)] (italic in the environment)",
           "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]",
           "Item label printed upright inside the italic statement (GLOBAL_ISSUES 16)."))
L.append(F(137, "Proposition (6.2.1), label (ii)", "(ii) upright", r"\item[(ii)] (italic in the environment)",
           "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]",
           "Item label printed upright inside the italic statement (GLOBAL_ISSUES 16)."))
L.append(F(137, "proof of (6.2.1)(i), display 0→P_n→P_{n-1}→ . . . →P_0→M→0",
           "baseline dots (dot bottoms on the baseline of P, M)", r"\cdots", "symbol", None, "high",
           r"P_{n-1}\to\cdots", r"P_{n-1}\to\ldots", "Baseline dots in the print; the TeX has centred \\cdots."))
L.append(F(137, "proof of (6.2.1)(i), display 0→P_n⊗_A B→ ... →0", "baseline dots", r"\cdots", "symbol", None,
           "high", r"P_{n-1}\otimes_AB\to\cdots", r"P_{n-1}\otimes_AB\to\ldots", "As above."))
L.append(F(137, "proof of (6.2.1)(ii), display 0→R→P_{m-1}→P_{m-2}→ . . . →P_0→M→0", "baseline dots", r"\cdots",
           "symbol", None, "high", r"P_{m-2}\to\cdots", r"P_{m-2}\to\ldots", "As above."))
L.append(F(137, "proof of (6.2.1)(ii), 'où les P_i (0 ⩽ i ⩽ m — 1)'", "long dash (bar 40 px; the = bars on this page 34 px)",
           r"m-1", "convention", 7, "high", r"i\leq m-1)$", r"i\leq m\setmin 1)$",
           "Subtraction set with the long dash (GLOBAL_ISSUES 23). The subscript minus signs (P_{m-1} etc.) are "
           "ordinary (21-22 px) and are not reported."))
L.append(F(137, "proof of (6.2.1)(ii), display 0→R⊗_A B→P_{m-1}⊗_A B→ ... →0", "baseline dots", r"\cdots",
           "symbol", None, "high", r"P_{m-1}\otimes_AB\to\cdots", r"P_{m-1}\otimes_AB\to\ldots", "As above."))
L.append(F(137, "'est un B-module projectif (0, 17.2.1)'", "bold 0", "(0, 17.2.1)", "convention", 2, "high",
           "(0, 17.2.1)", r"(\textbf{0}, 17.2.1)"))
L.append(F(137, "Corollaire (6.2.2), 'dim.proj(ℰ) ⩽ n (0, 17.2.14), on a'",
           "(0, 17.2.14) upright with bold 0 inside the italic statement", "(0, 17.2.14) italic (environment)",
           "convention", 6, "high", "(0, 17.2.14)", r"\textup{(\textbf{0}, 17.2.14)}",
           "One edit; it also sets the bold 0 of the next finding (convention 2)."))
L.append(F(137, "Corollaire (6.2.2), (0, 17.2.14)", "bold 0", "(0, 17.2.14)", "convention", 2, "high",
           None, None, "Covered by the edit of the preceding finding (convention 6), which also bolds the 0.",
           nofix=True))

# ---------------------------------------------------------------- page 138
L.append(F(138, "proof of (6.2.3), display . . . →L_i→L_{i-1}→ . . . →L_0→N→0 (first dots)", "baseline dots",
           r"\cdots", "symbol", None, "high", r"\cdots\to L_i", r"\ldots\to L_i",
           "Baseline dots in the print; the TeX has centred \\cdots."))
L.append(F(138, "same display, second dots", "baseline dots", r"\cdots", "symbol", None, "high",
           r"L_{i-1}\to\cdots", r"L_{i-1}\to\ldots", "As above."))
L.append(F(138, "same display, end", "...→L_0→N→0 with no full stop", r"L_0\to N\to0.", "punctuation", None, "high",
           r"L_0\to N\to0.", r"L_0\to N\to0",
           "Full stop after a display that the print lacks; 'Comme les L_i ...' continues flush left."))
L.append(F(138, "'Comme les L_i et N sont des A-modules plats (B étant ...'", "'plats' italic", "plats upright",
           "italics", None, "high", r"$A$-modules plats ($B$ étant", r"$A$-modules \emph{plats} ($B$ étant"))
L.append(F(138, "'que les Z_i(L_•) sont des A-modules plats, que L_•⊗_A k ...'", "'plats' italic (enlarged crop)",
           "plats upright", "italics", None, "high", r"$A$-modules⏎plats, que", r"$A$-modules⏎\emph{plats}, que",
           "The later 'des A-modules plats, il résulte' is upright, as in the TeX."))
L.append(F(138, "'qu'il est libre ou encore projectif'", "'libre' and 'projectif' italic (enlarged crop)",
           "both upright", "italics", None, "high", r"est libre ou encore projectif",
           r"est \emph{libre} ou encore \emph{projectif}"))
L.append(F(138, "'(0_III, 10.1.3)'", "bold 0", r"$(0_{\mathrm{III}}, 10.1.3)$", "convention", 2, "high",
           r"$(0_{\mathrm{III}}, 10.1.3)$", r"$(\mathbf{0}_{\mathrm{III}}, 10.1.3)$"))
L.append(F(138, "'il résulte d'autre part de (0_III, 10.2.5)'", "bold 0", r"$(0_{\mathrm{III}}, 10.2.5)$",
           "convention", 2, "high", r"$(0_{\mathrm{III}}, 10.2.5)$", r"$(\mathbf{0}_{\mathrm{III}}, 10.2.5)$"))
L.append(F(138, "'il faut et il suffit que Z_i(L_•⊗_A k) = Z_i(L)⊗_A k soit un (B⊗_A k)-module plat'",
           "Z_i(L_•⊗_A k) = Z_i(L)⊗_A k (enlarged crop)", r"$Z_i(L_\bullet)\otimes_Ak$ only", "missing", None, "high",
           r"suffit que $Z_i(", r"suffit que $Z_i(L_\bullet\otimes_Ak)=Z_i(",
           "The TeX drops 'Z_i(L_•⊗_A k) ='. Independent of the misprint edit that follows (no overlapping "
           "characters; either order)."))
L.append(F(138, "same formula, right-hand side", "Z_i(L)⊗_A k: L without the bullet (enlarged crop)",
           r"Z_i(L_\bullet)\otimes_Ak (silently corrected)", "misprint_in_print", None, "high",
           r"L_\bullet)\otimes_Ak$ soit un", r"L)\otimes_Ak$ soit un",
           "Misprint: the bullet of L_• is missing (cf. 'Z_i(L_•⊗_A k) = Z_i(L_•)⊗_A k pour tout i' a few lines "
           "earlier). The TeX silently corrected it; the edit restores the printed reading. 'old' occurs once "
           "before and after the 'missing' edit above.",
           corrected=r"Z_i(L_\bullet)\otimes_Ak"))
L.append(F(138, "'ce qui démontre la proposition (0, 17.2.1)'", "bold 0", "(0, 17.2.1)", "convention", 2, "high",
           "(0, 17.2.1)", r"(\textbf{0}, 17.2.1)"))
L.append(F(138, "heading 6.3", "6.3. Platitude et profondeur.", r"\subsection{Platitude et profondeur}",
           "punctuation", None, "high", r"\subsection{Platitude et profondeur}",
           r"\subsection{Platitude et profondeur.}", "Printed final full stop (GLOBAL_ISSUES 43/58)."))
L.append(F(138, "proof of (6.3.1), 'de (0, 16.4.6.2)'", "bold 0", "(0, 16.4.6.2)", "convention", 2, "high",
           "(0, 16.4.6.2)", r"(\textbf{0}, 16.4.6.2)"))
L.append(F(138, "proof of (6.3.1), 'associé à N⊗_A k (0, 16.4.6, (i)). On'", "bold 0", "(0, 16.4.6, (i))",
           "convention", 2, "high", "(0, 16.4.6, (i)). On", r"(\textbf{0}, 16.4.6, (i)). On"))
L.append(F(138, "proof of (6.3.1), 'donc (0, 16.4.6, (i)) que'", "bold 0", "(0, 16.4.6, (i))", "convention", 2,
           "high", "(0, 16.4.6, (i)) que", r"(\textbf{0}, 16.4.6, (i)) que"))
L.append(F(138, "end of page, after the display M'⊗_{A'}N' = (M⊗_A N)/x(M⊗_A N);",
           "p. 139 begins 'en outre, comme N ...' flush left, continuing the sentence after the display",
           r"\] followed by a blank line before the p. 139 marker", "other", None, "high",
           r"x(M\otimes_AN);⏎\]⏎⏎", r"x(M\otimes_AN);⏎\]⏎",
           "Apply together with the p. 139 entry that removes the blank line after \\oldpage[IV-2]{139}."))

# ---------------------------------------------------------------- page 139
L.append(F(139, "top of page, after \\oldpage[IV-2]{139}", "'en outre, comme N est un A-module plat, ...' flush left",
           r"\oldpage[IV-2]{139}, blank line, en outre", "other", None, "high",
           r"\oldpage[IV-2]{139}⏎⏎en outre", r"\oldpage[IV-2]{139}⏎en outre",
           "Apply together with the p. 138 entry that removes the blank line before the marker."))
L.append(F(139, "'(M⊗_A N)-régulier (0_I, 6.1.1)'", "bold 0", r"$(0_{\mathrm I}, 6.1.1)$", "convention", 2, "high",
           r"$(0_{\mathrm I}, 6.1.1)$", r"$(\mathbf{0}_{\mathrm I}, 6.1.1)$"))
L.append(F(139, "'On a par suite (0, 16.4.6, (ii) et 16.4.8)'", "bold 0", "(0, 16.4.6, (ii) et 16.4.8)",
           "convention", 2, "high", "(0, 16.4.6, (ii) et 16.4.8)", r"(\textbf{0}, 16.4.6, (ii) et 16.4.8)"))
L.append(F(139, "first display, prof_{A'}(M') = prof_A(M) — 1", "long dash (bar 41 px, the = bars 35-36 px)",
           r"\operatorname{prof}_A(M)-1", "convention", 7, "high",
           r"\operatorname{prof}_A(M)-1,", r"\operatorname{prof}_A(M)\setmin 1,",
           "Subtraction set with the long dash (GLOBAL_ISSUES 23)."))
L.append(F(139, "first display, prof_{B'}(M'⊗_{A'}N') = prof_B(M⊗_A N) — 1", "long dash (bar 41 px)",
           r"(M\otimes_AN)-1", "convention", 7, "high", r"(M\otimes_AN)-1⏎", r"(M\otimes_AN)\setmin 1⏎",
           "As above."))
L.append(F(139, "'N' = N⊗_A A' est un A'-module plat (0_I, 6.2.1)'", "bold 0", r"$(0_{\mathrm I}, 6.2.1)$",
           "convention", 2, "high", r"$(0_{\mathrm I}, 6.2.1)$", r"$(\mathbf{0}_{\mathrm I}, 6.2.1)$"))
L.append(F(139, "case b), line 9: 'Considérons un élément y∈m qui soit (N⊗_A k)-régulier'",
           "y ∈ 𝔪 (Fraktur m, three arches; enlarged crop)", r"$y\in\mathfrak m$ (the printed reading is kept)",
           "misprint_in_print", None, "high", None, None,
           "Authors' erratum, EGA IV part 4, liste 3, item (IV, 6.3.1): 'Ligne 9 de la p. 139, remplacer y∈𝔪 par "
           "y∈𝔫' (y must lie in the maximal ideal 𝔫 of B; an element of 𝔪 kills N⊗_A k). The TeX keeps the printed "
           "reading: no diplomatic edit.",
           corrected=r"$y\in\mathfrak n$", nofix=True))
L.append(F(139, "'il résulte de (0_III, 10.2.4)'", "bold 0", r"$(0_{\mathrm{III}}, 10.2.4)$", "convention", 2,
           "high", r"$(0_{\mathrm{III}}, 10.2.4)$", r"$(\mathbf{0}_{\mathrm{III}}, 10.2.4)$"))
L.append(F(139, "'est un A-module plat, puisque N est supposé être un A-module plat'",
           "first 'plat' italic (enlarged crop)", "plat upright", "italics", None, "high",
           r"est un $A$-module plat, puisque", r"est un $A$-module \emph{plat}, puisque"))
L.append(F(139, "'Appliquant (0_I, 6.1.2)'", "bold 0", r"$(0_{\mathrm I}, 6.1.2)$", "convention", 2, "high",
           r"$(0_{\mathrm I}, 6.1.2)$", r"$(\mathbf{0}_{\mathrm I}, 6.1.2)$"))
L.append(F(139, "display prof_{B⊗_A k}(N'⊗_A k) = prof_{B⊗_A k}(N⊗_A k) — 1", "long dash (bar 40 px, the = bars 35 px)",
           r"(N\otimes_Ak)-1", "convention", 7, "high", r"(N\otimes_Ak)-1⏎", r"(N\otimes_Ak)\setmin 1⏎",
           "Subtraction set with the long dash (GLOBAL_ISSUES 23)."))
L.append(F(139, "display prof_B(M⊗_A N') = prof_B(M⊗_A N) — 1;", "long dash (bar 45 px, the = bars 35 px)",
           r"(M\otimes_AN)-1;", "convention", 7, "high", r"(M\otimes_AN)-1;", r"(M\otimes_AN)\setmin 1;",
           "As above."))
L.append(F(139, "Corollaire (6.3.2), 'Sous les hypothèses de (6.3.1)'", "(6.3.1) upright inside the italic statement",
           "(6.3.1) italic (environment)", "convention", 6, "high",
           r"(6.3.1), supposons en outre $M\neq0$ et $N\neq0$;⏎alors",
           r"\textup{(6.3.1)}, supposons en outre $M\neq0$ et $N\neq0$;⏎alors",
           "Reference printed upright inside the italic statement."))
L.append(F(139, "proof of (6.3.2), 'coprofondeur (0, 16.4.9)'", "bold 0", "(0, 16.4.9)", "convention", 2, "high",
           "(0, 16.4.9)", r"(\textbf{0}, 16.4.9)"))
L.append(F(139, "Corollaire (6.3.3), 'Sous les hypothèses de (6.3.1)'", "(6.3.1) upright inside the italic statement",
           "(6.3.1) italic (environment)", "convention", 6, "high",
           r"(6.3.1), supposons en outre $M\neq0$ et $N\neq0$; pour",
           r"\textup{(6.3.1)}, supposons en outre $M\neq0$ et $N\neq0$; pour",
           "Reference printed upright inside the italic statement."))
L.append(F(139, "proof of (6.3.3), 'coprofondeur est nulle (0, 16.5.1)'", "bold 0", "(0, 16.5.1)", "convention", 2,
           "high", "(0, 16.5.1)", r"(\textbf{0}, 16.5.1)"))
L.append(F(139, "Corollaire (6.3.4), 'Sous les hypothèses de (6.3.1)'", "(6.3.1) upright inside the italic statement",
           "(6.3.1) italic (environment)", "convention", 6, "high",
           r"(6.3.1), supposons en outre que", r"\textup{(6.3.1)}, supposons en outre que",
           "Reference printed upright inside the italic statement."))

# ---------------------------------------------------------------- checks
pages = {}
for n in sorted({d["page"] for d in L}):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    c = pages[d["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", c, d["page"], repr(fx["old"]))
# overlap check within each page (spans of olds in the original text)
for n in pages:
    spans = []
    for d in L:
        if d["page"] == n and d["fix"]:
            s = pages[n].find(d["fix"]["old"])
            spans.append((s, s + len(d["fix"]["old"]), d["fix"]["old"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP p.", n, repr(a[2]), "|", repr(b[2]))
# replay: apply all fixes of each page in order and check each old is still found exactly once at its turn
for n in pages:
    txt = pages[n]
    for d in L:
        if d["page"] == n and d["fix"]:
            c = txt.count(d["fix"]["old"])
            if c != 1:
                print("REPLAY FAIL p.", n, c, repr(d["fix"]["old"]))
            txt = txt.replace(d["fix"]["old"], d["fix"]["new"], 1)
OUT.write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter

cnt = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for n in sorted(pages):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("entries", len(L), "bad", bad)
