import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_095_099.json')

def page_text(p):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8') as f:
        return f.read().replace('\r\n', '\n')

F = []
def add(page, where, scan, tex, kind, fix, note='', convention=None, confidence='high', corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

def fx(old, new):
    return {"old": old, "new": new}

OM = 'Italic Omega for the sheaf of differentials (GLOBAL_ISSUES 92).'
C6 = 'Printed upright inside the italic statement.'
LBL = 'Labels in roman text are italic in the print (GLOBAL_ISSUES 88).'

# ---------------- page 95 ----------------
add(95, "(17.13.6.2), display after 'Dire que la suite (17.13.6.2)'",
    "all four Omegas italic (page_095_s1.png)", "upright \\Omega", "font",
    fx("0\\to\\Omega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T\n\\xrightarrow{\\alpha\\oplus(-\\beta)}\n(\\Omega^1_{Y/S}\\otimes_{\\sh{O}_Y}\\sh{O}_T)\\oplus\n(\\Omega^1_{Z/S}\\otimes_{\\sh{O}_Z}\\sh{O}_T)\n\\xrightarrow{\\gamma+\\delta}\\Omega^1_{T/S}\\to0",
       "0\\to\\varOmega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T\n\\xrightarrow{\\alpha\\oplus(-\\beta)}\n(\\varOmega^1_{Y/S}\\otimes_{\\sh{O}_Y}\\sh{O}_T)\\oplus\n(\\varOmega^1_{Z/S}\\otimes_{\\sh{O}_Z}\\sh{O}_T)\n\\xrightarrow{\\gamma+\\delta}\\varOmega^1_{T/S}\\to0"),
    OM)
add(95, "'Ω^1_{X/S}⊗O_T s'identifie canoniquement au produit fibré de Ω^1_{Y/S}⊗O_T et Ω^1_{Z/S}⊗O_T sur Ω^1_{T/S}'",
    "italic Omega four times", "upright \\Omega", "font",
    fx("$\\Omega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T$ s'identifie canoniquement au \\emph{produit fibré} de $\\Omega^1_{Y/S}\\otimes_{\\sh{O}_Y}\\sh{O}_T$ et $\\Omega^1_{Z/S}\\otimes_{\\sh{O}_Z}\\sh{O}_T$ sur $\\Omega^1_{T/S}$",
       "$\\varOmega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T$ s'identifie canoniquement au \\emph{produit fibré} de $\\varOmega^1_{Y/S}\\otimes_{\\sh{O}_Y}\\sh{O}_T$ et $\\varOmega^1_{Z/S}\\otimes_{\\sh{O}_Z}\\sh{O}_T$ sur $\\varOmega^1_{T/S}$"),
    OM)
add(95, "'Le même raisonnement que dans (0, 18.1.2 et 18.1.3)'", "bold 0", "plain 0", "convention",
    fx("(0, 18.1.2 et 18.1.3)", "(\\textbf{0}, 18.1.2 et 18.1.3)"), "", convention=2)
add(95, "diagram: vertical arrow N_{Y/X}⊗O_T → N_{T/Z}",
    "isomorphism sign ≀ to the right of the arrow (crop p95_wr.png)", "plain \\ar[d], no sign", "missing",
    fx("\\sh{N}_{Y/X}\\otimes\\sh{O}_T \\ar[r] \\ar[d]", "\\sh{N}_{Y/X}\\otimes\\sh{O}_T \\ar[r] \\ar[d,\"\\wr\"]"),
    "tikz-cd puts the label of a downward arrow on its right, beside the arrow as printed.")
add(95, "diagram: label β of the arrow Ω^1_{X/S}⊗O_T → Ω^1_{Z/S}⊗O_T",
    "β to the LEFT of the arrow (crop p95_labels.png)", "\\ar[d,\"\\beta\"]: label on the right", "other",
    fx("\\ar[d,\"\\beta\"]", "\\ar[d,\"\\beta\" swap]"),
    "γ (right of its arrow) and α (above) are as printed.")
add(95, "diagram: label δ of the arrow Ω^1_{Z/S}⊗O_T → Ω^1_{T/S}",
    "δ BELOW the arrow (crop p95_row3.png)", "\\ar[r,\"\\delta\"]: label above", "other",
    fx("\\ar[r,\"\\delta\"]", "\\ar[r,\"\\delta\" swap]"), "")
add(95, "diagram: label ι of the diagonal arrow from (N_{Y/X}⊗O_T)⊕(N_{Z/X}⊗O_T)",
    "ι beside the arrow, above and to its right (page_095_s2.png)", "'description': label set on the arrow, interrupting it", "other",
    fx("\\ar[dr,\"\\iota\" description]", "\\ar[dr,\"\\iota\"]"),
    "Without 'description' tikz-cd sets the label of a down-right arrow on its upper right side, as printed.",
    confidence='medium')
add(95, "diagram: label ε of the diagonal arrow Ω^1_{X/S}⊗O_T → Ω^1_{T/S}",
    "ε beside the arrow, above and to its right (crop p95_labels.png)", "'description': label set on the arrow, interrupting it", "other",
    fx("\\ar[dr,\"\\varepsilon\" description]", "\\ar[dr,\"\\varepsilon\"]"),
    "Same as the ι label.", confidence='medium')
add(95, "diagram: Ω^1_{X/S}⊗O_T (middle row)", "italic Omega (crop p95_row2.png)", "upright \\Omega", "font",
    fx("& \\Omega^1_{X/S}\\otimes\\sh{O}_T", "& \\varOmega^1_{X/S}\\otimes\\sh{O}_T"), OM)
add(95, "diagram: Ω^1_{Y/S}⊗O_T (middle row)", "italic Omega (crop p95_row2.png)", "upright \\Omega", "font",
    fx("& \\Omega^1_{Y/S}\\otimes\\sh{O}_T", "& \\varOmega^1_{Y/S}\\otimes\\sh{O}_T"), OM)
add(95, "diagram: Ω^1_{Z/S}⊗O_T (bottom row)", "italic Omega (crop p95_row3.png)", "upright \\Omega", "font",
    fx("& \\Omega^1_{Z/S}\\otimes\\sh{O}_T", "& \\varOmega^1_{Z/S}\\otimes\\sh{O}_T"), OM)
add(95, "diagram: Ω^1_{T/S} (bottom row)", "italic Omega (crop p95_row3.png)", "upright \\Omega", "font",
    fx("& \\Omega^1_{T/S} \\ar[r]", "& \\varOmega^1_{T/S} \\ar[r]"), OM)
add(95, "'résulte de (0, 20.5.2.7)'", "bold 0", "plain 0", "convention",
    fx("(0, 20.5.2.7)", "(\\textbf{0}, 20.5.2.7)"), "", convention=2)
add(95, "(17.13.9): 'tous identiques à X (I, 3.3.5)'", "bold I", "plain I", "convention",
    fx("(I, 3.3.5)", "(\\textbf{I}, 3.3.5)"), "", convention=2)
add(95, "(17.13.9): '(comme dans (I, 5.3.1))'", "bold I", "plain I", "convention",
    fx("(I, 5.3.1)", "(\\textbf{I}, 5.3.1)"), "", convention=2)
add(95, "(17.13.9): 'donc (I, 5.3.11) une immersion'", "bold I", "plain I", "convention",
    fx("(I, 5.3.11)", "(\\textbf{I}, 5.3.11)"), "", convention=2)

# ---------------- page 96 ----------------
add(96, "'le produit des S-préschémas Y_i'", "'préschémas' italic (crop p96_top.png)", "upright", "italics",
    fx("des $S$-préschémas $Y_i$", "des $S$-\\emph{préschémas} $Y_i$"), "")
add(96, "'T le produit des X-préschémas Y_i'", "'préschémas' italic (crop p96_top.png)", "upright", "italics",
    fx("des $X$-préschémas $Y_i$", "des $X$-\\emph{préschémas} $Y_i$"),
    "The later 'des X^I-préschémas X et Y' is roman in the print, as in the TeX.")
add(96, "'On prouve comme dans (I, 5.3.5)'", "bold I", "plain I", "convention",
    fx("(I, 5.3.5)", "(\\textbf{I}, 5.3.5)"), "", convention=2)
add(96, "diagram (17.13.9.1): label Δ of the arrow X → X^I", "Δ to the LEFT of the arrow (page_096_s1.png)",
    "\\ar[d]^{\\Delta}: label on the right", "other",
    fx("X \\ar[d]^{\\Delta}", "X \\ar[d]_{\\Delta}"),
    "xymatrix: ^ puts the label of a downward arrow on its right, _ on its left. j (right), v (above) and u (below) are as printed. Same fix as for (17.13.5.1) on p. 92.")
add(96, "'il résulte de (16.4.23) que Ω^1_{X^I/S} (resp. Ω^1_{Y/S}) ... des p_i^*(Ω^1_{X/S}) (resp. des q_i^*(Ω^1...'",
    "italic Omega four times (crops p96_pi.png, p96_qi.png)", "upright \\Omega", "font",
    fx("que $\\Omega^1_{X^I/S}$ (resp. $\\Omega^1_{Y/S}$) s'identifie canoniquement à la somme directe des $p_i^*(\\Omega^1_{X/S})$ (resp. des $q_i^*(\\Omega^1",
       "que $\\varOmega^1_{X^I/S}$ (resp. $\\varOmega^1_{Y/S}$) s'identifie canoniquement à la somme directe des $p_i^*(\\varOmega^1_{X/S})$ (resp. des $q_i^*(\\varOmega^1"),
    OM + " The edit stops before the subscript of the last Omega, which the misprint entry that follows changes.")
add(96, "'(resp. des q_i^*(Ω^1_{X_i/S}), si q_i : Y → Y_i sont les projections canoniques)'",
    "subscript X_i/S (crop p96_qi.png)", "Y_i/S: silent correction", "misprint_in_print",
    fx("_{Y_i/S})$, si $q_i", "_{X_i/S})$, si $q_i"),
    "Y is the product of the Y_i and q_i : Y → Y_i, so the summands of Ω^1_{Y/S} are q_i^*(Ω^1_{Y_i/S}) (16.4.23); X_i (the copies of X in X^I) is a slip. Not in Liste 3. Independent of the Omega entry before it (the two edits do not overlap).",
    corrected="$q_i^*(\\varOmega^1_{Y_i/S})$")
add(96, "display '0 → 𝒢r_1(Δ) → (Ω^1_{X/S})^I → Ω^1_{X/S} → 0'",
    "script G followed by italic r: 𝒢r_1(Δ) (crop p96_gr_big.png)", "\\operatorname{gr}_1 (roman gr)", "symbol",
    fx("0\\to\\operatorname{gr}_1(\\Delta)", "0\\to\\mathscr{G}r_1(\\Delta)"),
    "The sheaf 𝒢r_1 of (16.1.2); written \\mathscr{G}r_1 as elsewhere in ega4-17 (source lines 180-182) and ega4-16.")
add(96, "same display: (Ω^1_{X/S})^I → Ω^1_{X/S}", "italic Omega twice (crop p96_gr_big.png)", "upright \\Omega", "font",
    fx("(\\Omega^1_{X/S})^I\\to\\Omega^1_{X/S}\\to0.", "(\\varOmega^1_{X/S})^I\\to\\varOmega^1_{X/S}\\to0."), OM)
add(96, "'Posons 𝒥 = 𝒢r_1(Δ)'", "script G followed by italic r (crop p96_posons.png)", "\\operatorname{gr}_1", "symbol",
    fx("Posons $\\sh{J}=\\operatorname{gr}_1(\\Delta)$", "Posons $\\sh{J}=\\mathscr{G}r_1(\\Delta)$"), "As in the display above.")
add(96, "(17.13.9.1), the exact sequence", "italic Omega twice (crop p96_seq.png)", "upright \\Omega", "font",
    fx("(\\Omega^1_{X/S})^I\\otimes_{\\sh{O}_X}\\sh{O}_T\\xrightarrow{\\sigma}\\Omega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T\\to0",
       "(\\varOmega^1_{X/S})^I\\otimes_{\\sh{O}_X}\\sh{O}_T\\xrightarrow{\\sigma}\\varOmega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T\\to0"), OM)
add(96, "equation numbers: the diagram AND the exact sequence are both numbered (17.13.9.1)",
    "'(17.13.9.1)' printed twice (page_096_s1.png, page_096_s2.png)", "\\tag{17.13.9.1} twice: keeps the printed reading", "misprint_in_print",
    None,
    "Duplicated equation number. The later reference 'la situation de (17.13.9.1)' (end of (17.13.9)) is to the diagram, so the sequence is the one wrongly numbered; the number it should have cannot be read off (no erratum in Liste 3; nothing in ega4-16 to ega4-18 cites (17.13.9.2)). The corrected edition needs an editorial decision.",
    confidence='medium',
    corrected="sequence numbered differently from the diagram's (17.13.9.1), e.g. \\tag{17.13.9.1$'$} (editorial choice, not a printed or errata reading)")
add(96, "'à chaque famille de sections (t_i)_{i∈I} de Ω^1_{X/S}⊗O_T'", "italic Omega", "upright \\Omega", "font",
    fx("de $\\Omega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T$ au-dessus", "de $\\varOmega^1_{X/S}\\otimes_{\\sh{O}_X}\\sh{O}_T$ au-dessus"), OM)
add(96, "(17.13.9.2)", "italic Omega twice (page_096_s3.png)", "upright \\Omega", "font",
    fx("\\tau:(\\Omega^1_{X/S})^I\\otimes_{\\sh{O}_X}\\sh{O}_T\\to\\bigoplus_{i\\in I}(\\Omega^1_{Y_i/S}",
       "\\tau:(\\varOmega^1_{X/S})^I\\otimes_{\\sh{O}_X}\\sh{O}_T\\to\\bigoplus_{i\\in I}(\\varOmega^1_{Y_i/S}"), OM)
add(96, "'des sections au-dessus d'un ouvert de X de Ω^1_{X/S}'", "italic Omega", "upright \\Omega", "font",
    fx("de $X$ de $\\Omega^1_{X/S}$, associe", "de $X$ de $\\varOmega^1_{X/S}$, associe"), OM)
add(96, "Corollaire (17.13.10): 'Sous les hypothèses générales de (17.13.9),'", "reference upright (crop p96_cor_l1.png)", "italic",
    "convention", fx("générales de (17.13.9),", "générales de \\textup{(17.13.9)},"), C6, convention=6)
add(96, "Corollaire (17.13.10): 'y_i (i∈I) ses projections'", "parentheses upright (measured slant 0.00)", "italic parentheses",
    "convention", fx("($i\\in I$) ses projections", "\\textup{($i\\in I$)} ses projections"),
    "Parentheses around formulas inside italic statements are upright in the print (GLOBAL_ISSUES 26).", convention=6)
add(96, "Corollaire (17.13.10): '(c_i entier positif ou négatif)'", "both parentheses upright, the words italic (measured slant 0.00 and 0.02; crop p96_cor_l4.png)",
    "italic parentheses", "convention",
    fx("($c_i$ entier positif ou négatif)", "\\textup{(}$c_i$ entier positif ou négatif\\textup{)}"),
    "Parentheses upright around italic words (GLOBAL_ISSUES 96).", convention=6)

# ---------------- page 97 ----------------
add(97, "Corollaire (17.13.10), label a)", "'a)' upright", "italic label", "convention",
    fx("\\item[a)] $T$ est lisse", "\\item[\\textup{a)}] $T$ est lisse"), "Label printed upright inside the italic statement.", convention=6)
add(97, "Corollaire (17.13.10), label b)", "'b)' upright", "italic label", "convention",
    fx("\\item[b)] L'homomorphisme", "\\item[\\textup{b)}] L'homomorphisme"), "Label printed upright inside the italic statement.", convention=6)
add(97, "(17.13.10) b), display: '⊕(Ω^1_{Y_i/S}⊗_{O_{Y_i}} k(t))'", "italic Omega", "upright \\Omega", "font",
    fx("(t)\\to\\bigoplus_{i\\in I}(\\Omega^1_{Y_i/S}", "(t)\\to\\bigoplus_{i\\in I}(\\varOmega^1_{Y_i/S}"), OM)
add(97, "(17.13.10) b), display: '𝒥⊗_{O_X} k(t)'", "bold italic k", "plain k", "convention",
    fx("\\rho\\otimes1:\\sh{J}\\otimes_{\\sh{O}_X}k", "\\rho\\otimes1:\\sh{J}\\otimes_{\\sh{O}_X}\\boldsymbol{k}"), "", convention=1)
add(97, "(17.13.10) b), display: '⊗_{O_{Y_i}} k(t)'", "bold italic k", "plain k", "convention",
    fx("\\otimes_{\\sh{O}_{Y_i}}k(t))", "\\otimes_{\\sh{O}_{Y_i}}\\boldsymbol{k}(t))"), "", convention=1)
add(97, "Corollaire (17.13.10): 'Lorsque t est rationnel ...' after the list", "new indented paragraph (page_097_s1.png)",
    "text follows \\end{enumerate} directly (no indent)", "other",
    fx("\\end{enumerate}\nLorsque $t$", "\\end{enumerate}\n\nLorsque $t$"), "Paragraph break as printed (GLOBAL_ISSUES 80 pattern).")
add(97, "Corollaire (17.13.10): 'rationnel sur le corps k(s)'", "bold italic k", "plain k", "convention",
    fx("le corps $k(s)$", "le corps $\\boldsymbol{k}(s)$"), "", convention=1)
add(97, "Corollaire (17.13.10): '(où s est l'image de t dans S)'", "both parentheses upright (measured slant -0.01), the words italic (crop p97_ou_s.png)",
    "italic parentheses", "convention",
    fx("(où $s$ est l'image de $t$ dans $S$)", "\\textup{(}où $s$ est l'image de $t$ dans $S$\\textup{)}"),
    "Parentheses upright around italic words (GLOBAL_ISSUES 96). The parentheses of '(où δ est l'application diagonale)' in b') are italic in the print (measured slant 0.19): no change there.", convention=6)
add(97, "Corollaire (17.13.10), label b')", "'b )' upright; no prime visible, a gap where it stands (crop p97_bprime.png)", "italic label",
    "convention", fx("\\item[b')] L'homomorphisme transposé", "\\item[\\textup{b$'$)}] L'homomorphisme transposé"),
    "Label printed upright inside the italic statement; prime written b$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88). The prime did not print (no ink at all, but its space is left): treated as a physical printing defect, not reported as a misprint.", convention=6)
add(97, "end of Corollaire (17.13.10): 'Il suffit de remarquer ...' and 'Lorsque les conditions équivalentes de (17.13.10) ...'",
    "the statement ends with '... est surjectif.'; both following paragraphs are roman and indented (page_097_s2.png)",
    "\\end{corollary} stands after '... est \\emph{ouvert} dans $S$.': both paragraphs are set italic", "other",
    fx("\\end{enumerate}\nIl suffit", "\\end{enumerate}\n\\end{corollary}\n\nIl suffit"),
    "Part 1 of 2 (apply both): ends the corollary after b'); the second part removes the old \\end{corollary}. Same repair as for (17.13.6) on p. 93.")
add(97, "'X^I est lisse sur S et de dimension relative d.Card(I),'", "baseline period between d and Card (crop p97_card.png)", "\\cdot (centred dot)", "symbol",
    fx("d\\cdot\\operatorname{Card}(I)$, et", "d.\\operatorname{Card}(I)$, et"), "Baseline period as printed (GLOBAL_ISSUES 65 pattern).")
add(97, "'Y lisse sur S de dimension relative d.Card(I)+Σ c_i'", "baseline period (crop p97_card2.png)", "\\cdot", "symbol",
    fx("d\\cdot\\operatorname{Card}(I)+\\sum", "d.\\operatorname{Card}(I)+\\sum"), "Baseline period as printed (GLOBAL_ISSUES 65 pattern).")
add(97, "'famille de morphismes transversaux au point t, relativement à S'", "'relativement à' italic, 'à' included (crop p97_relativement.png)",
    "'à' outside the \\emph", "italics", fx("relativement} à $S$. On voit", "relativement à} $S$. On voit"), "")
add(97, "'La remarque (17.13.4, (ii)) montre alors'", "'(ii)' (crop p97_remarque.png)", "'(iii)'", "number",
    fx("(17.13.4, (iii))", "(17.13.4, (ii))"),
    "The print is right: (17.13.4, (ii)) is the remark on openness and properness over S that is used here; (iii) is about base change.")
add(97, "end of the roman paragraph 'Lorsque les conditions équivalentes de (17.13.10) ...': old \\end{corollary}",
    "see part 1", "\\end{corollary} after 'est \\emph{ouvert} dans $S$.'", "other",
    fx("\\emph{ouvert} dans $S$.\n\\end{corollary}", "\\emph{ouvert} dans $S$."),
    "Part 2 of 2 (apply both): removes the old \\end{corollary}; part 1 inserts it after b').")
add(97, "(17.13.11): 'La condition a) de (17.13.10)'", "'a)' italic (crop p97_s3_l3.png)", "upright", "italics",
    fx("La condition a) de (17.13.10)", "La condition \\emph{a)} de (17.13.10)"), LBL)
add(97, "(17.13.11): 'En outre, on a la propriété suivante' after (17.13.11.1)", "new indented paragraph after the display (page_097_s3.png)",
    "no blank line after \\]: continues the paragraph without indent", "other",
    fx("\\]\nEn outre, on a", "\\]\n\nEn outre, on a"), "Paragraph break as printed (GLOBAL_ISSUES 47 pattern).")
add(97, "end of p. 97 (after (17.13.12.2)) / top of p. 98 'Mais ici les O_T-Modules'",
    "p. 98 begins 'Mais ici' at the left margin, without indent: the paragraph continues after the display (page_098_s1.png)",
    "blank line before \\oldpage[IV-4]{98} (and another after it): a paragraph break the print does not have", "marker",
    fx("\\to\\sh{N}_{T/X}.\n\\]\n\n", "\\to\\sh{N}_{T/X}.\n\\]\n"),
    "The marker is at the right place. Part 1 of 2: the first p. 98 finding removes the blank line after \\oldpage[IV-4]{98}; apply both.")

# ---------------- page 98 ----------------
add(98, "top of page_098.tex: blank line after \\oldpage[IV-4]{98}", "p. 98 begins mid-paragraph ('Mais ici', no indent)",
    "blank line between the marker and 'Mais ici'", "marker",
    fx("\\oldpage[IV-4]{98}\n\nMais ici", "\\oldpage[IV-4]{98}\nMais ici"), "Part 2 of 2 with the last p. 97 finding; both blank lines must go.")
add(98, "'et de même rang Σ_i c_i'", "'de' roman, 'même rang' italic (crop p98_l2.png)", "\\emph{de même rang}", "italics",
    fx("\\emph{de même rang}", "de \\emph{même rang}"), "")
add(98, "'en vertu de (17.2.5) et de la condition a) de (17.13.10)'", "'a)' italic (crop p98_l2.png)", "upright", "italics",
    fx("de la condition a) de (17.13.10)", "de la condition \\emph{a)} de (17.13.10)"), LBL)
add(98, "Proposition (17.14.1): 'Soient f : X → Y un morphisme'", "'Soient' (crop p98_prop_l1.png)", "'Soit'", "word",
    fx("Soit $f:X\\to Y$ un morphisme localement de présentation finie, $x$ un point de $X$, $y=f(x)$. Pour que", "Soient $f:X\\to Y$ un morphisme localement de présentation finie, $x$ un point de $X$, $y=f(x)$. Pour que"), "")
add(98, "Proposition (17.14.1): 'Pour que f soit lisse (resp. non ramifié, resp. étale) au point x'",
    "'(resp.', 'resp.' and ')' upright, 'non ramifié', 'étale' italic (crop p98_prop_l1.png)", "all italic", "convention",
    fx("(resp. non ramifié, resp. étale) au point $x$, il faut et il suffit que",
       "\\textup{(resp.} non ramifié, \\textup{resp.} étale\\textup{)} au point $x$, il faut et il suffit que"), C6, convention=6)
add(98, "Proposition (17.14.1): 'Pour tout schéma local Y' = Spec(A')'", "'schéma local' roman (crop p98_prop_l3.png)", "italic", "convention",
    fx("Pour tout schéma local", "Pour tout \\textup{schéma local}"), C6, convention=6)
add(98, "Proposition (17.14.1): 'tout Y-morphisme g_0 : Y'_0 → X tel que g'_0(y') = x'",
    "g'_0(y') = x: a prime on g (crop p98_prop_l5.png)", "g_0(y')=x: silent correction", "misprint_in_print",
    fx("tel que $g_0(y')=x$", "tel que $g'_0(y')=x$"),
    "The condition is on the given morphism g_0 (Y'_0 has the underlying space of Y', so g_0(y') makes sense); g'_0 is not defined anywhere. Not in Liste 3.",
    corrected="tel que $g_0(y')=x$")
add(98, "Proposition (17.14.1): 'il existe au moins un (resp. au plus un, resp. un et un seul) Y-morphisme'",
    "'(resp.', 'resp.' and ')' upright, the rest italic (crop p98_prop_l5.png)", "all italic", "convention",
    fx("(resp. au plus un, resp. un et un seul)", "\\textup{(resp.} au plus un, \\textup{resp.} un et un seul\\textup{)}"), C6, convention=6)
add(98, "proof of (17.14.1): '(i) Cas des morphismes lisses.'", "'(i)' upright, 'Cas des morphismes lisses' italic (crop p98_i_l1.png)",
    "\\emph{(i) Cas ...}: the label italic", "italics",
    fx("\\emph{(i) Cas des morphismes lisses.} On peut", "(i) \\emph{Cas des morphismes lisses.} On peut"),
    "Proof-part labels are printed upright (GLOBAL_ISSUES 76).")
FK = "Wrong letter: the print has Fraktur K (𝔎: arch with a flag to the upper right, as in run_0IV1/crops_066_070/frak_compare.png), not Fraktur R (GLOBAL_ISSUES 63). Crops p98_frakA.png, p98_frakB.png."
add(98, "(17.14.1) (i): 'avec C = B/𝔎, où B = A[T_1, ..., T_n] ... et 𝔎 un idéal de type fini'", "Fraktur K twice", "\\mathfrak{R}", "symbol",
    fx("$C=B/\\mathfrak{R}$, où $B=A[T_1,\\ldots,T_n]$ est une $A$-algèbre de polynômes et $\\mathfrak{R}$ un idéal",
       "$C=B/\\mathfrak{K}$, où $B=A[T_1,\\ldots,T_n]$ est une $A$-algèbre de polynômes et $\\mathfrak{K}$ un idéal"), FK)
add(98, "(17.14.1) (i): 'Or on a O_{X,x} = B_𝔮/𝔎B_𝔮'", "Fraktur K", "\\mathfrak{R}", "symbol",
    fx("$\\sh{O}_{X,x}=B_{\\mathfrak q}/\\mathfrak{R}B_{\\mathfrak q}$", "$\\sh{O}_{X,x}=B_{\\mathfrak q}/\\mathfrak{K}B_{\\mathfrak q}$"), FK)
add(98, "(17.14.1) (i): 'B_𝔮/𝔎²B_𝔮 est une extension A_𝔭-triviale de B_𝔮/𝔎B_𝔮 par 𝔎B_𝔮/𝔎²B_𝔮'", "Fraktur K four times", "\\mathfrak{R}", "symbol",
    fx("voir que $B_{\\mathfrak q}/\\mathfrak{R}^2B_{\\mathfrak q}$ est une extension $A_{\\mathfrak p}$-triviale de $B_{\\mathfrak q}/\\mathfrak{R}B_{\\mathfrak q}$ par $\\mathfrak{R}B_{\\mathfrak q}/\\mathfrak{R}^2B_{\\mathfrak q}$",
       "voir que $B_{\\mathfrak q}/\\mathfrak{K}^2B_{\\mathfrak q}$ est une extension $A_{\\mathfrak p}$-triviale de $B_{\\mathfrak q}/\\mathfrak{K}B_{\\mathfrak q}$ par $\\mathfrak{K}B_{\\mathfrak q}/\\mathfrak{K}^2B_{\\mathfrak q}$"), FK)
add(98, "(17.14.1) (i): 'appliquée à A' = B_𝔮/𝔎²B_𝔮 et 𝔍' = 𝔎B_𝔮/𝔎²B_𝔮'", "Fraktur K three times", "\\mathfrak{R}", "symbol",
    fx("$A'=B_{\\mathfrak q}/\\mathfrak{R}^2B_{\\mathfrak q}$ et $\\mathfrak{J}'=\\mathfrak{R}B_{\\mathfrak q}/\\mathfrak{R}^2B_{\\mathfrak q}$",
       "$A'=B_{\\mathfrak q}/\\mathfrak{K}^2B_{\\mathfrak q}$ et $\\mathfrak{J}'=\\mathfrak{K}B_{\\mathfrak q}/\\mathfrak{K}^2B_{\\mathfrak q}$"), FK + " The Fraktur J of 𝔍' is right.")
add(98, "(17.14.1) (i): 'pour les topologies discrètes (0, 19.3.2 et 19.3.5)'", "bold 0", "plain 0", "convention",
    fx("(0, 19.3.2 et 19.3.5)", "(\\textbf{0}, 19.3.2 et 19.3.5)"), "", convention=2)
add(98, "(17.14.1) (i): 'critère jacobien (0, 22.6.1 et 20.5.12)'", "bold 0", "plain 0", "convention",
    fx("(0, 22.6.1 et 20.5.12)", "(\\textbf{0}, 22.6.1 et 20.5.12)"), "", convention=2)
add(98, "proof of (17.14.1): '(ii) Cas des morphismes non ramifiés.'", "'(ii)' upright, the title italic (crop p98_ii_l1.png)",
    "\\emph{(ii) Cas ...}: the label italic", "italics",
    fx("\\emph{(ii) Cas des morphismes non ramifiés.} Posons", "(ii) \\emph{Cas des morphismes non ramifiés.} Posons"),
    "Proof-part labels are printed upright (GLOBAL_ISSUES 76).")
add(98, "(17.14.1) (ii): 'en vertu de (17.4.1, c))'", "'c)' (italic c, no prime; crop p98_c.png)", "'c')' upright", "symbol",
    fx("(17.4.1, c'))", "(17.4.1, \\emph{c)})"),
    "Wrong label: (17.4.1) has no condition c'); its c) is '(Ω^1_{X/Y})_x = 0', the condition used here. The edit also sets the label italic as printed (GLOBAL_ISSUES 88).")
add(98, "(17.14.1) (ii): 'Ω^1_{B/A} = (Ω^1_{X/Y})_x = 0'", "the module Ω^1_{B/A} upright, the sheaf Ω^1_{X/Y} italic (crop p98_ii_l1.png)",
    "both upright", "font", fx("(\\Omega^1_{X/Y})_x=0", "(\\varOmega^1_{X/Y})_x=0"),
    OM + " The three Ω^1_{B/A} (modules) are upright in the print and stay \\Omega.")
add(98, "(17.14.1) (ii): 'avec les notations de (0, 20.4.1)'", "bold 0", "plain 0", "convention",
    fx("(0, 20.4.1)", "(\\textbf{0}, 20.4.1)"), "", convention=2)
add(98, "(17.14.1) (ii): 'l'anneau C = P^1_{B/A} = (B⊗_A B)/𝔍²'", "roman P (crop p98_P.png)", "\\sh{P} (script P)", "symbol",
    fx("\\sh{P}^1_{B/A}", "\\mathrm{P}^1_{B/A}"),
    "The ring of principal parts P^1_{B/A} is roman, as ega0-20 writes it (\\mathrm{P}^1_{B/A}, 22 times); the script letter is the sheaf 𝒫^1_{X/S}.")
add(98, "(17.14.1) (ii): 'est nulle (0, 20.4.6)'", "bold 0", "plain 0", "convention",
    fx("est nulle (0, 20.4.6)", "est nulle (\\textbf{0}, 20.4.6)"), "", convention=2)
add(98, "(17.14.1) (ii): 'par (0, 20.4.7)'", "bold 0", "plain 0", "convention",
    fx("par (0, 20.4.7)", "par (\\textbf{0}, 20.4.7)"), "", convention=2)
add(98, "Proposition (17.14.2): 'Soient Y un préschéma localement noethérien'", "'localement noethérien' roman (crop p98_142_l1.png)", "italic", "convention",
    fx("\\label{IV.17.14.2}\nSoient $Y$ un préschéma localement noethérien", "\\label{IV.17.14.2}\nSoient $Y$ un préschéma \\textup{localement noethérien}"), C6, convention=6)
add(98, "Proposition (17.14.2): 'Pour que f soit lisse (resp. non ramifié, resp. étale) au point x'",
    "'(resp.', 'resp.' and ')' upright (crop p98_142_l2.png)", "all italic", "convention",
    fx("(resp. non ramifié, resp. étale) au point $x$, il faut et il suffit qu'il",
       "\\textup{(resp.} non ramifié, \\textup{resp.} étale\\textup{)} au point $x$, il faut et il suffit qu'il"), C6, convention=6)
add(98, "Proposition (17.14.2): 'la condition de (17.14.1) où l'on suppose'", "reference upright", "italic", "convention",
    fx("la condition de (17.14.1) où", "la condition de \\textup{(17.14.1)} où"), C6, convention=6)
add(98, "Proposition (17.14.2): 'l'anneau local A' est artinien'", "'artinien' roman ('est' italic; crop p98_142_l2.png)", "italic", "convention",
    fx("$A'$ est artinien", "$A'$ est \\textup{artinien}"), C6, convention=6)
add(98, "Proposition (17.14.2): 'de A' est égal à k(x)'", "'égal à' roman ('est' italic; crop p98_142_l2.png)", "italic", "convention",
    fx("$A'$ est égal à", "$A'$ est \\textup{égal à}"), C6, convention=6)
add(98, "Proposition (17.14.2): 'est égal à k(x)'", "bold italic k", "plain k", "convention",
    fx("$k(x)$.", "$\\boldsymbol{k}(x)$."), "", convention=1)

# ---------------- page 99 ----------------
add(99, "proof of (17.14.2): '(i) Cas des morphismes lisses.'", "'(i)' upright, the title italic (page_099_s1.png)",
    "\\emph{(i) Cas ...}: the label italic", "italics",
    fx("\\emph{(i) Cas des morphismes lisses.} Si l'on pose", "(i) \\emph{Cas des morphismes lisses.} Si l'on pose"),
    "Proof-part labels are printed upright (GLOBAL_ISSUES 76).")
add(99, "'B est une A-algèbre formellement lisse pour les topologies préadiques'", "'pour les topologies préadiques' italic (crop p99_l2.png)", "upright", "italics",
    fx("que $B$ est une $A$-algèbre formellement lisse pour les topologies préadiques.", "que $B$ est une $A$-algèbre formellement lisse \\emph{pour les topologies préadiques}."), "")
add(99, "'en vertu de (0, 22.1.4)'", "bold 0", "plain 0", "convention",
    fx("(0, 22.1.4)", "(\\textbf{0}, 22.1.4)"), "", convention=2)
add(99, "'en considérant les anneaux A'/𝔪'^j𝔍''", "no comma between the prime and j (crop p99_mj.png)", "\\mathfrak m'^{,j} prints a comma", "punctuation",
    fx("A'/\\mathfrak m'^{,j}\\mathfrak{J}'", "A'/\\mathfrak m'^{j}\\mathfrak{J}'"), "GLOBAL_ISSUES 49 pattern.")
add(99, "'par récurrence sur j comme dans (0, 19.4.3)'", "bold 0", "plain 0", "convention",
    fx("(0, 19.4.3)", "(\\textbf{0}, 19.4.3)"), "", convention=2)
add(99, "proof of (17.14.2): '(ii) Cas des morphismes non ramifiés.'", "'(ii)' upright, the title italic (page_099_s1.png)",
    "\\emph{(ii) Cas ...}: the label italic", "italics",
    fx("\\emph{(ii) Cas des morphismes non ramifiés.} Reprenons", "(ii) \\emph{Cas des morphismes non ramifiés.} Reprenons"),
    "Proof-part labels are printed upright (GLOBAL_ISSUES 76).")
add(99, "'pour tout n (0_I, 7.3.5)'", "bold 0 with subscript I (crop p99_0I.png)", "plain 0", "convention",
    fx("(0$_{\\mathrm I}$, 7.3.5)", "($\\mathbf{0}_{\\mathrm I}$, 7.3.5)"), "Written as elsewhere in ega4-17 (source line 304: ($\\mathbf{0}_{\\mathrm I}$, 5.2.7)).", convention=2)
add(99, "'Avec les notations de (0, 20.4.6)'", "bold 0", "plain 0", "convention",
    fx("Avec les notations de (0, 20.4.6)", "Avec les notations de (\\textbf{0}, 20.4.6)"), "", convention=2)
add(99, "Remarque (17.14.3): 'le corps k(x) est une extension finie'", "bold italic k (crop p99_rem.png)", "plain k", "convention",
    fx("le corps $k(x)$", "le corps $\\boldsymbol{k}(x)$"), "", convention=1)
add(99, "Remarque (17.14.3): 'extension finie de k(y)'", "bold italic k", "plain k", "convention",
    fx("de $k(y)$, alors", "de $\\boldsymbol{k}(y)$, alors"), "", convention=1)
add(99, "Remarque (17.14.3): 'des k(y)-espaces vectoriels'", "bold italic k", "plain k", "convention",
    fx("des $k(y)$-espaces", "des $\\boldsymbol{k}(y)$-espaces"), "", convention=1)
add(99, "Remarque (17.14.3): 'les A'-modules 𝔪'^j/𝔪'^{j+1}'", "no commas between the primes and the exponents (crop p99_mj2.png)",
    "\\mathfrak m'^{,j}, \\mathfrak m'^{,j+1} print commas", "punctuation",
    fx("\\mathfrak m'^{,j}/\\mathfrak m'^{,j+1}", "\\mathfrak m'^{j}/\\mathfrak m'^{j+1}"), "GLOBAL_ISSUES 49 pattern.")
add(99, "Remarque (17.14.3): 'A' est une O_{Y,y}-algèbre finie.'", "'finie' italic (crop p99_rem.png)", "no \\emph", "italics",
    fx("$\\sh{O}_{Y,y}$-algèbre finie.", "$\\sh{O}_{Y,y}$-algèbre \\emph{finie}."),
    "The remark body is roman in the print (document-wide item); the other emphasised words 'finie', 'a fortiori' already have \\emph.")
add(99, "Proposition (17.15.1): '(ou seulement pour toute extension finie radicielle de k)'",
    "'(ou seulement pour toute extension', 'de' and ')' roman, 'finie radicielle' italic; parentheses measured upright (crop p99_1511.png)",
    "all italic", "convention",
    fx("(ou seulement pour toute extension finie radicielle de $k$)",
       "\\textup{(ou seulement pour toute extension} finie radicielle \\textup{de} $k$\\textup{)}"), C6, convention=6)
add(99, "Proposition (17.15.1): 'Si k(x) est une extension séparable de k'", "bold italic k", "plain k", "convention",
    fx("Si $k(x)$ est une extension", "Si $\\boldsymbol{k}(x)$ est une extension"), "", convention=1)
add(99, "Proposition (17.15.1): '(en particulier si k est parfait)'",
    "'(en particulier si', 'est' and ')' roman, 'parfait' italic; parentheses measured upright (crop p99_1511.png)", "all italic", "convention",
    fx("(en particulier si $k$ est parfait)", "\\textup{(en particulier si} $k$ \\textup{est} parfait\\textup{)}"), C6, convention=6)
add(99, "Corollaire (17.15.2): 'Sous les conditions de (17.15.1),'", "reference upright (crop p99_1512.png)", "italic", "convention",
    fx("Sous les conditions de (17.15.1),", "Sous les conditions de \\textup{(17.15.1)},"), C6, convention=6)
add(99, "Corollaire (17.15.2): 'géométriquement régulier sur k (6.7.6)'", "reference upright (crop p99_1512.png)", "italic", "convention",
    fx("sur $k$ (6.7.6), ce qui", "sur $k$ \\textup{(6.7.6)}, ce qui"), C6, convention=6)
add(99, "Proposition (17.15.3): 'transformant T_i en g_i (I, 2.2.4)'", "bold upright I, reference upright (crop p99_1531.png)", "plain I, italic reference", "convention",
    fx("(I, 2.2.4)", "\\textup{(\\textbf{I}, 2.2.4)}"),
    "One edit for convention 2 (bold I) and convention 6 (upright reference inside the italic statement), as for (II, 1.7.8) on p. 62.", convention=2)
add(99, "Proposition (17.15.3): '(et impliquent que X est lisse sur k au point x et par suite régulier au point x)'",
    "'et par suite' and 'au point' (the second one) roman; the rest, 'régulier' and both parentheses italic (parentheses measured slant 0.18; crop p99_1532.png)",
    "all italic", "convention",
    fx("et par suite régulier au point $x$)", "\\textup{et par suite} régulier \\textup{au point} $x$)"),
    C6 + " The roman/italic pattern inside this parenthesis is irregular (only these words roman), but it is what the print shows.", convention=6)
add(99, "Proposition (17.15.3), labels a) and b)", "'a)', 'b)' upright (crop p99_items.png)", "italic labels", "convention",
    fx("\\item[a)] $f$ est étale au point $x$.\n  \\item[b)] Les images", "\\item[\\textup{a)}] $f$ est étale au point $x$.\n  \\item[\\textup{b)}] Les images"),
    "Labels printed upright inside the italic statement. One edit for both labels (the a) line alone recurs at (17.15.4) on p. 100).", convention=6)
add(99, "Proposition (17.15.3), label c)", "'c)' upright", "italic label", "convention",
    fx("\\item[c)] Les images", "\\item[\\textup{c)}] Les images"), "Label printed upright inside the italic statement.", convention=6)
add(99, "(17.15.3) b): 'base du O_{X,x}-module (Ω^1_{X/k})_x'", "italic Omega (crop p99_items.png)", "upright \\Omega", "font",
    fx("forment une base du $\\sh{O}_{X,x}$-module $(\\Omega^1_{X/k})_x$", "forment une base du $\\sh{O}_{X,x}$-module $(\\varOmega^1_{X/k})_x$"), OM)
add(99, "(17.15.3) c): 'engendrent le O_{X,x}-module (Ω^1_{X/k})_x'", "italic Omega (crop p99_items.png)", "upright \\Omega", "font",
    fx("engendrent le $\\sh{O}_{X,x}$-module $(\\Omega^1_{X/k})_x$", "engendrent le $\\sh{O}_{X,x}$-module $(\\varOmega^1_{X/k})_x$"), OM)
add(99, "proof of (17.15.3): 'le fait que a) entraîne b) est donc'", "labels italic (crop p99_proof.png)", "upright", "italics",
    fx("le fait que a) entraîne b) est donc", "le fait que \\emph{a)} entraîne \\emph{b)} est donc"), LBL)
add(99, "proof of (17.15.3): 'Comme b) entraîne trivialement c), il reste à voir que c) implique a).'", "labels italic (crop p99_proof.png)", "upright", "italics",
    fx("Comme b) entraîne trivialement c), il reste à voir que c) implique a).",
       "Comme \\emph{b)} entraîne trivialement \\emph{c)}, il reste à voir que \\emph{c)} implique \\emph{a)}."), LBL)
add(99, "page break 99/100 inside 'Notons d'abord | que l'hypothèse entraîne'",
    "p. 99 ends 'Notons d'abord' (no stop); p. 100 continues the sentence", "blank line before \\oldpage[IV-4]{100} (and another after it): a paragraph break inside the sentence", "marker",
    fx("Notons d'abord\n\n", "Notons d'abord\n"),
    "The marker is at the right place. The blank line AFTER \\oldpage[IV-4]{100} (before 'que l'hypothèse', page_100.tex) must go too; it lies in the p. 100 batch and is not reported here.")

# ---------------- verification ----------------
ok = True
texts = {p: page_text(p) for p in range(95, 100)}
for i, d in enumerate(F):
    if d['fix'] is None:
        continue
    old = d['fix']['old']
    n = texts[d['page']].count(old)
    if n != 1:
        ok = False
        print('NOT UNIQUE/MISSING', i, d['page'], n, repr(old[:80]))
# overlap check: no two fixes on the same page may overlap
for p in range(95, 100):
    spans = []
    for i, d in enumerate(F):
        if d['page'] != p or d['fix'] is None:
            continue
        old = d['fix']['old']
        k = texts[p].find(old)
        if k >= 0:
            spans.append((k, k + len(old), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print('OVERLAP page', p, a, b)
ED = os.path.join(os.path.dirname(RUN), 'ega-fr', 'editions', '2026-10-24-r20')
dip = open(os.path.join(ED, 'diplomatic', 'packages', 'IV4', 'native', 'ega4', 'ega4-17-fr.tex'), encoding='utf-8').read()
cur = open(os.path.join(ED, 'current', 'packages', 'IV4', 'native', 'ega4', 'ega4-17-fr.tex'), encoding='utf-8').read()
for i, d in enumerate(F):
    if d['fix'] is None:
        continue
    old = d['fix']['old']
    nd = dip.count(old)
    nc = cur.count(old)
    if nd != 1:
        print('diplomatic file count', nd, d['page'], repr(old[:70]))
    if d['kind'] != 'misprint_in_print' and nc != 1:
        print('current-edition file count', nc, d['page'], repr(old[:70]))
print('findings:', len(F), 'ok' if ok else 'PROBLEMS')
from collections import Counter
c = Counter()
for d in F:
    c[(d['page'], 'misprint' if d['kind'] == 'misprint_in_print' else ('convention' if d['kind'] == 'convention' else 'normal'))] += 1
for p in range(95, 100):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
if ok:
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(F, f, ensure_ascii=False, indent=1)
    print('written', OUT)
