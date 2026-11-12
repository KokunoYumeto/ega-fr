import json, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_215_219.json")

NOTE7 = "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
NOTE7S = "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
REMARK = "Inside the remark environment (italic in the TeX); judged as a roman body, as the print sets remarks."


def F(page, where, scan, tex, kind, conv, fix, note="", conf="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 214 (outside the batch) ----------------
L.append(F(214,
    "end of page_214.tex, just before \\oldpage[IV-3]{215} (proof of Lemme (14.4.8.1)): '... Pour prouver la première assertion, considérons | un voisinage ouvert U de x dans X'",
    "the sentence runs on from p. 214 to p. 215 ('considérons un voisinage ouvert U de x dans X'); no paragraph break",
    "blank line before (and after) \\oldpage[IV-3]{215}: paragraph break in mid-sentence",
    "marker", None,
    {"old": "considérons\n\n", "new": "considérons\n"},
    "OUTSIDE pp. 215-219: 'old' is the end of page_214.tex (ega4-14-fr.tex line 1136, just before the p. 215 marker); filed under page 214 so that it is found there; the pp. 210-214 checker may report the same. Goes with the p. 215 entry for the blank line after the marker (GLOBAL_ISSUES 20). The marker itself is in the right place."))

# ---------------- page 215 ----------------
L.append(F(215,
    "top of p. 215: blank line after \\oldpage[IV-3]{215} before 'un voisinage ouvert U de x dans X'",
    "p. 215 begins mid-sentence: 'un voisinage ouvert U de x dans X; comme v est fermé ...'",
    "blank line after the marker (paragraph break)",
    "marker", None,
    {"old": "\\oldpage[IV-3]{215}\n\nun voisinage", "new": "\\oldpage[IV-3]{215}\nun voisinage"},
    "The marker position is right; only the blank line goes (GLOBAL_ISSUES 20). The blank line before the marker is the page-214 entry."))
L.append(F(215,
    "proof of Lemme (14.4.8.1), l. 3: 'on a v^{-1}(f(U)) = f_1(p^{-1}(U)) (I, 3.4.8), et'",
    "bold I followed by a comma (enlarged crop p215_s1_I348.png)",
    "(I, 3.4.8) with a plain I",
    "convention", 2,
    {"old": "(I, 3.4.8), et", "new": "(\\textbf{I}, 3.4.8), et"},
    "A genuine EGA I reference (bold I and comma in the print), not a misread (1.x.y) (GLOBAL_ISSUES 78)."))
L.append(F(215,
    "same proof, l. 4: 'est un voisinage de f_1(p^{-1}(x)) = v^{-1}(y) (I, 3.4.8).'",
    "bold I (same crop)",
    "plain I",
    "convention", 2,
    {"old": "(I, 3.4.8).", "new": "(\\textbf{I}, 3.4.8)."}))
L.append(F(215,
    "Corollaire (14.4.9) a), l. 1: 'autrement dit, pour tout changement de base Y'→Y'",
    "'tout' in roman inside the italic statement (enlarged crop p215_s1_a.png)",
    "italic (corollary environment)",
    "convention", 6,
    {"old": "pour tout changement de", "new": "pour \\textup{tout} changement de"}))
L.append(F(215,
    "Corollaire (14.4.9), label a')",
    "label a') upright, like a) and b) (same crop)",
    "\\item[a$'$)] inside the italic corollary environment: the label comes out italic (the automatic labels \\emph{\\alph*)} are upright)",
    "convention", 6,
    {"old": "\\item[a$'$)]", "new": "\\item[\\textup{a$'$)}]"},
    "Item label upright in the print (GLOBAL_ISSUES 16 pattern)."))
L.append(F(215,
    "Corollaire (14.4.9) a'): 'Pour tout morphisme fini Y_1→Y, f_(Y_1) est ouvert.'",
    "'fini' in roman inside the italic statement (same crop)",
    "italic",
    "convention", 6,
    {"old": "morphisme fini $Y_1\\to Y$", "new": "morphisme \\textup{fini} $Y_1\\to Y$"}))
L.append(F(215,
    "Corollaire (14.4.9), label a'')",
    "label a'') upright (enlarged crop p215_s2_b.png)",
    "\\item[a$''$)] in the italic environment: italic label",
    "convention", 6,
    {"old": "\\item[a$''$)]", "new": "\\item[\\textup{a$''$)}]"},
    "As label a')."))
L.append(F(215,
    "Corollaire (14.4.9) a''): 'Si Y'' est le normalisé de Y_red, f_(Y'') est ouvert.'",
    "'normalisé' in roman inside the italic statement (same crop)",
    "italic",
    "convention", 6,
    {"old": "est le normalisé de", "new": "est le \\textup{normalisé} de"}))
L.append(F(215,
    "Corollaire (14.4.9) b), end: '... au point x'' (cf. (14.4.10, (ii))).'",
    "the whole parenthesis '(cf. (14.4.10, (ii)))' upright (same crop)",
    "italic",
    "convention", 6,
    {"old": "(cf. (14.4.10, (ii)))", "new": "\\textup{(cf. (14.4.10, (ii)))}"}))
L.append(F(215,
    "Remarques (14.4.10), (i), l. 4: 'b) entraîne que f'' est universellement ouvert aux points de X'' au-dessus de X (resp. en tout point de X'')'",
    "au-dessus de X: an upright capital X, the same glyph as the X'' just before (enlarged crop p215_s2_audessus.png)",
    "au-dessus de $x$ (silent correction)",
    "misprint_in_print", None,
    {"old": "au-dessus de $x$ (resp.", "new": "au-dessus de $X$ (resp."},
    "In (14.4.8) x is the given point of X and condition b) concerns the points x'' of X'' above x; 'points of X'' above X' would be all of X''. The TeX silently corrects; the fix restores the printed reading. The corrected edition (r20 current) already reads $x$.",
    corrected="$x$"))
L.append(F(215,
    "Remarques (14.4.10), (ii), l. 6: 'la restriction de f_1 à f_1^{-1}(Y—{y})'",
    "long dash Y—{y} (enlarged crop p215_s3_iso.png)",
    "minus sign",
    "convention", 7,
    {"old": "$f_1^{-1}(Y-\\{y\\})$", "new": "$f_1^{-1}(Y\\setmin\\{y\\})$"},
    NOTE7))
L.append(F(215,
    "same sentence: 'est un isomorphisme sur Y—{y} (loc. cit.)'",
    "long dash (same crop)",
    "minus sign",
    "convention", 7,
    {"old": "$Y-\\{y\\}$ (\\emph{loc.", "new": "$Y\\setmin\\{y\\}$ (\\emph{loc."},
    NOTE7))
L.append(F(215,
    "Remarques (14.4.10), (ii), l. 7: 'c'est-à-dire ici à P^1_{k(y)}'",
    "bold upright k in the subscript; the P is bold upright, as \\mathbf P gives (enlarged crops p215_s3_P1ky.png, p215_s3_P1ky_zoom.png)",
    "plain k",
    "convention", 1,
    {"old": "ici à $\\mathbf P^1_{k(y)}$", "new": "ici à $\\mathbf P^1_{\\mathbf{k}(y)}$"},
    "Bold upright in a subscript, as GLOBAL_ISSUES 48. No convention-10 item: the projective P here and in P^1_Y (l. 9) is bold upright."))
L.append(F(215,
    "same line: 'c'est-à-dire ici à P^1_{k(y)} : il résulte de (14.4.1) que f_1 n'est pas ouvert ...'",
    "a colon after P^1_{k(y)} (enlarged crop p215_s3_P1ky_zoom.png)",
    "a semicolon (~;)",
    "punctuation", None,
    {"old": "~; il résulte de\n  (14.4.1)", "new": "~: il résulte de\n  (14.4.1)"},
    "Does not overlap the convention-1 entry for the same P^1_{k(y)}."))
L.append(F(215,
    "Remarques (14.4.10), (ii), l. 10: 'en outre (II, 3.5.3), f_2^{-1}(y) est isomorphe à P^1_{k(y)};'",
    "bold upright k in the subscript (enlarged crop p215_s3_P1ky2.png)",
    "plain k",
    "convention", 1,
    {"old": "$\\mathbf P^1_{k(y)}$~; il suffit", "new": "$\\mathbf P^1_{\\mathbf{k}(y)}$~; il suffit"},
    "Bold upright in a subscript, as GLOBAL_ISSUES 48."))
L.append(F(215,
    "Remarques (14.4.10), (iii), l. 2: 'f est fini et plat (et même étale (17.6.3))'",
    "'fini' and 'plat' in italics (enlarged crop p215_s4_iii.png)",
    "upright (remark body judged as roman)",
    "italics", None,
    {"old": "est fini et plat", "new": "est \\emph{fini} et \\emph{plat}"},
    REMARK))
L.append(F(215,
    "same sentence: 'mais la restriction de f à une composante irréductible de X'",
    "'restriction' in italics (same crop)",
    "upright (remark body judged as roman)",
    "italics", None,
    {"old": "mais la restriction de $f$", "new": "mais la \\emph{restriction} de $f$"},
    REMARK))
L.append(F(215,
    "end of p. 215 / top of p. 216, Remarques (14.4.10), (iv): 'l'énoncé plus général | ainsi obtenu s'appliquera ...'",
    "the sentence runs on to p. 216; no paragraph break",
    "blank line before \\oldpage[IV-3]{216} (end of page_215.tex)",
    "marker", None,
    {"old": "plus\n  général\n\n", "new": "plus\n  général\n"},
    "Mid-sentence page break (GLOBAL_ISSUES 20); goes with the p. 216 entry for the blank line after the marker. The marker itself is in the right place."))

# ---------------- page 216 ----------------
L.append(F(216,
    "top of p. 216: blank line after \\oldpage[IV-3]{216} before 'ainsi obtenu s'appliquera'",
    "p. 216 begins mid-sentence: 'ainsi obtenu s'appliquera en particulier à des morphismes plats'",
    "blank line after the marker (paragraph break)",
    "marker", None,
    {"old": "\\oldpage[IV-3]{216}\n\n  ainsi obtenu", "new": "\\oldpage[IV-3]{216}\n  ainsi obtenu"},
    "See the end-of-page entry of p. 215; both blank lines must go for item (iv) to run on."))
L.append(F(216,
    "heading 14.5: 'Morphismes universellement ouverts et quasi-sections.'",
    "full stop after the title",
    "no full stop",
    "punctuation", None,
    {"old": "\\subsection{Morphismes universellement ouverts et quasi-sections}",
     "new": "\\subsection{Morphismes universellement ouverts et quasi-sections.}"},
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))
L.append(F(216,
    "Lemme (14.5.1), l. 2: 'tel que f soit équidimensionnel (13.3.2) au point x'",
    "(13.3.2) upright in the italic statement (enlarged crop p216_s1_lemma.png)",
    "italic (lemma environment)",
    "convention", 6,
    {"old": "équidimensionnel (13.3.2) au point", "new": "équidimensionnel \\textup{(13.3.2)} au point"}))
L.append(F(216,
    "Lemme (14.5.1), l. 4: 'codim(X', X) ⩽ n et dim_x(X'∩f^{-1}(y)) ⩽ e—n'",
    "long dash e—n (page_216_s2.png)",
    "minus sign",
    "convention", 7,
    {"old": "\\leq e-n$. Alors", "new": "\\leq e\\setmin n$. Alors"},
    NOTE7S))
L.append(F(216,
    "Lemme (14.5.1), l. 5: 'dim_x(X'∩f^{-1}(y)) = e—n'",
    "long dash",
    "minus sign",
    "convention", 7,
    {"old": "=e-n$, et la restriction", "new": "=e\\setmin n$, et la restriction"},
    NOTE7S))
L.append(F(216,
    "Lemme (14.5.1), last line: '(et a fortiori dominant)'",
    "'a fortiori' in roman inside the italic statement (enlarged crop p216_s2_fortiori.png)",
    "italic",
    "convention", 6,
    {"old": "(et a fortiori dominant)", "new": "(et \\textup{a fortiori} dominant)"}))
L.append(F(216,
    "proof of (14.5.1), l. 3: 'sont de dimension e (13.3.1, a''))'",
    "'(13.3.1, a''))': the label a'') keeps its own parenthesis, then the reference closes (enlarged crop p216_s2_a2.png)",
    "'(13.3.1, $a''$).': one closing parenthesis only",
    "punctuation", None,
    {"old": "(13.3.1, $a''$).", "new": "(13.3.1, $a''$))."}))
L.append(F(216,
    "display (14.5.1.1): 'codim(X', Z) ⩽ n'",
    "no full stop after the formula; the sentence goes on 'et si les deux membres ...' (enlarged crop p216_s2_disp.png)",
    "'\\leq n.' (full stop)",
    "punctuation", None,
    {"old": "\\leq n.\n  \\tag{14.5.1.1}", "new": "\\leq n\n  \\tag{14.5.1.1}"}))
L.append(F(216,
    "line after (14.5.1.1): 'et si les deux membres sont égaux, on a nécessairement ...'",
    "lower-case 'et' (same crop)",
    "'Et si'",
    "word", None,
    {"old": "Et si les deux membres", "new": "et si les deux membres"}))
L.append(F(216,
    "display (14.5.1.3): 'e' = dim(X'∩f^{-1}(y')) = e—codim(X', Z)'",
    "long dash (enlarged crop p216_s3_1513.png)",
    "minus sign",
    "convention", 7,
    {"old": "=e-\\operatorname{codim}", "new": "=e\\setmin\\operatorname{codim}"},
    NOTE7S))
L.append(F(216,
    "display (14.5.1.3), end: '⩾ e—n'",
    "long dash (same crop)",
    "minus sign",
    "convention", 7,
    {"old": "Z)\\geq e-n", "new": "Z)\\geq e\\setmin n"},
    NOTE7S))
L.append(F(216,
    "display (14.5.1.3): punctuation at the end of the formula",
    "no comma after '⩾ e—n' (same crop)",
    "'\\geq e-n,' (comma)",
    "punctuation", None,
    {"old": ",\n  \\tag{14.5.1.3}", "new": "\n  \\tag{14.5.1.3}"},
    "Independent of the convention-7 entry for the same e-n (the 'old' strings do not overlap)."))
L.append(F(216,
    "proof of (14.5.1): '... et si f(X') est dense dans Y. | Enfin, (13.1.1), on a dim_x(X'∩f^{-1}(y)) ⩾ e''",
    "'Enfin' begins a new indented paragraph (enlarged crop p216_s3_enfin.png)",
    "runs on in the same paragraph",
    "other", None,
    {"old": "dans $Y$. Enfin,", "new": "dans $Y$.\n\nEnfin,"},
    "Missing paragraph break."))
L.append(F(216,
    "display (14.5.1.4): 'dim_x(X'∩f^{-1}(y)) ⩾ e' ⩾ e—n.'",
    "long dash (page_216_s3.png)",
    "minus sign",
    "convention", 7,
    {"old": "e'\\geq e-n.", "new": "e'\\geq e\\setmin n."},
    NOTE7S))
L.append(F(216,
    "proof of (14.5.1), last sentence: 'Or, par hypothèse, on a aussi dim_x(X'∩f^{-1}(y)) ⩽ e—n'",
    "long dash",
    "minus sign",
    "convention", 7,
    {"old": "\\leq e-n$, d'où les", "new": "\\leq e\\setmin n$, d'où les"},
    NOTE7S))
L.append(F(216,
    "Corollaire (14.5.2), l. 1: 'Les hypothèses sur f, X, Y, x étant celles de (14.5.1), supposons'",
    "(14.5.1) upright in the italic statement (page_216_s4.png)",
    "italic (corollary environment)",
    "convention", 6,
    {"old": "celles de (14.5.1), supposons", "new": "celles de \\textup{(14.5.1)}, supposons"}))
L.append(F(216,
    "display (14.5.2.1): 'dim_x(X'∩f^{-1}(y)) = e—1'",
    "long dash (page_216_s4.png)",
    "minus sign",
    "convention", 7,
    {"old": "=e-1 \\qquad", "new": "=e\\setmin 1 \\qquad"},
    NOTE7S))

# ---------------- page 217 ----------------
L.append(F(217,
    "proof of (14.5.2), l. 10: 'on a (0, 14.2.2.2) dim_x(X'∩f^{-1}(y)) ⩽ e—1'",
    "long dash (page_217_s1.png)",
    "minus sign",
    "convention", 7,
    {"old": "\\leq e-1$. Il suffit", "new": "\\leq e\\setmin 1$. Il suffit"},
    NOTE7S))
L.append(F(217,
    "Proposition (14.5.3), l. 4-5: '(où X' est le sous-préschéma réduit de X ayant X' pour espace sous-jacent)'",
    "the whole parenthesis in roman inside the italic statement (enlarged crop p217_s2_ou.png)",
    "italic (proposition environment)",
    "convention", 6,
    {"old": "(où $X'$ est le sous-préschéma\nréduit de $X$ ayant $X'$ pour espace sous-jacent)",
     "new": "\\textup{(où $X'$ est le sous-préschéma\nréduit de $X$ ayant $X'$ pour espace sous-jacent)}"}))
L.append(F(217,
    "proof of (14.5.3), l. 2: 'tant que e—1 ⩾ 1'",
    "long dash (page_217_s2.png)",
    "minus sign",
    "convention", 7,
    {"old": "$e-1\\geq 1$", "new": "$e\\setmin 1\\geq 1$"},
    NOTE7S))
L.append(F(217,
    "Corollaire (14.5.4), l. 1: 'Sous les hypothèses de (14.5.3), supposons en outre'",
    "(14.5.3) upright in the italic statement (enlarged crop p217_s2_cor.png)",
    "italic (corollary environment)",
    "convention", 6,
    {"old": "hypothèses de (14.5.3),", "new": "hypothèses de \\textup{(14.5.3)},"}))
L.append(F(217,
    "Corollaire (14.5.4), l. 2: 'où A est un anneau local noethérien intègre et complet'",
    "'complet' in roman inside the italic statement (same crop)",
    "italic",
    "convention", 6,
    {"old": "intègre et complet, et que", "new": "intègre et \\textup{complet}, et que"}))

# ---------------- page 218 ----------------
L.append(F(218,
    "Remarque (14.5.7), l. 2: 'où A est un anneau de valuation discrète complet'",
    "'complet' in italics (page_218_s2.png)",
    "upright (remark body judged as roman)",
    "italics", None,
    {"old": "discrète complet, et que", "new": "discrète \\emph{complet}, et que"},
    REMARK))
L.append(F(218,
    "Remarque (14.5.7), l. 4: 'qui est une A-algèbre finie, comme le montre'",
    "'finie' in italics (same strip)",
    "upright (remark body judged as roman)",
    "italics", None,
    {"old": "algèbre finie, comme", "new": "algèbre \\emph{finie}, comme"},
    REMARK))
L.append(F(218,
    "Remarque (14.5.7), l. 1 (line 16 of p. 218): 'Si, dans l'énoncé de (14.5.5), on suppose que Y = Spec(A)'",
    "(14.5.5)",
    "keeps the printed (14.5.5)",
    "misprint_in_print", None,
    None,
    "Wrong reference, corrected by the authors' errata (EGA IV part 4, entry (IV, 14.5.7): 'Ligne 16 de la p. 218, remplacer (14.5.5) par (14.5.6)'; IV4 ega4-errata-addenda-list3-fr.tex lines 235-236): the remark concerns the X' of (14.5.6) e) (Y regular of dimension 1). The TeX keeps the printed reading; the corrected edition (r20 current) still reads (14.5.5) and should apply the erratum (GLOBAL_ISSUES 72).",
    corrected="(14.5.6)"))
L.append(F(218,
    "Proposition (14.5.8), condition, l. 3: 'tout élément u_0 ∈ X(Spec(k(y'))) tel que u_0(y') = x'",
    "bold italic k (enlarged crop p218_s3_u0.png)",
    "plain k",
    "convention", 1,
    {"old": "X(\\operatorname{Spec}(k(y')))", "new": "X(\\operatorname{Spec}(\\boldsymbol{k}(y')))"}))
L.append(F(218,
    "diagram of (14.5.8), top left: 'Spec(k(z'))'",
    "bold italic k (enlarged crop p218_s3_diag.png)",
    "plain k",
    "convention", 1,
    {"old": "\\operatorname{Spec}(k(z')) \\ar[r]", "new": "\\operatorname{Spec}(\\boldsymbol{k}(z')) \\ar[r]"}))
L.append(F(218,
    "diagram of (14.5.8), bottom left: 'Spec(k(y'))'",
    "bold italic k (page_218_s4.png)",
    "plain k",
    "convention", 1,
    {"old": "\\operatorname{Spec}(k(y')) \\ar[r]_{u_0}", "new": "\\operatorname{Spec}(\\boldsymbol{k}(y')) \\ar[r]_{u_0}"}))
L.append(F(218,
    "diagram of (14.5.8): label of the left vertical arrow Spec(k(z')) → Spec(k(y'))",
    "the vertical isomorphism sign ≀ to the right of the arrow (enlarged crop p218_s3_diag.png)",
    "\\ar[d]^{\\ell} (a script l)",
    "symbol", None,
    {"old": "\\ar[d]^{\\ell}", "new": "\\ar[d]^{\\wr}"},
    "≀ beside the arrow, as the print sets it (GLOBAL_ISSUES 64); ^ puts the label to the right of a downward arrow, where the print has it (as u on the other arrow)."))

# ---------------- page 219 ----------------
L.append(F(219,
    "page break 218/219: the printed p. 219 begins 'quement clos, et puisque u(z') = x' (the word algébri-|quement is split by the page break); the TeX marker stands before 'Notons que si A et B vérifient', the last paragraph of p. 218",
    "p. 218 ends '... de corps résiduel isomorphe à celui de A, donc algébri-' (page_218_s4.png); p. 219 begins 'quement clos' (page_219_s1.png)",
    "\\oldpage[IV-3]{219} before 'Notons'",
    "marker", None,
    {"old": "\\oldpage[IV-3]{219}\n\nNotons", "new": "Notons"},
    "Marker move, part 1 of 2: apply together with the next entry, which inserts the marker at the printed word break (as la fonc%|tion, IV-3 p. 93). One blank line stays after \\end{proposition}: the print starts the paragraph 'Notons' there."))
L.append(F(219,
    "same page break: insert the marker inside 'algébri-|quement'",
    "p. 219 begins 'quement clos, et puisque u(z') = x'",
    "no marker there",
    "marker", None,
    {"old": "donc\nalgébriquement clos", "new": "donc\nalgébri%\n\\oldpage[IV-3]{219}\nquement clos"},
    "Marker move, part 2 of 2 (apply together with part 1)."))
L.append(F(219,
    "proof of (14.5.8), l. 2 of p. 219: 'et qui est rationnel sur k(z')'",
    "bold italic k (page_219_s1.png)",
    "plain k",
    "convention", 1,
    {"old": "sur $k(z')$", "new": "sur $\\boldsymbol{k}(z')$"}))
L.append(F(219,
    "proof of (14.5.8), l. 7: 'au-dessus de x et de y' et rationnel sur k(y') (I, 3.3.14)'",
    "bold italic k (enlarged crop p219_s1_ky.png)",
    "plain k",
    "convention", 1,
    {"old": "sur $k(y')$", "new": "sur $\\boldsymbol{k}(y')$"}))
L.append(F(219,
    "proof of (14.5.8), l. 9-10: 'la restriction T'→Y' de f' est équidimensionnelle au point x.'",
    "'au point x.' without a prime (enlarged crop p219_s1_pointx.png)",
    "keeps the printed $x$",
    "misprint_in_print", None,
    None,
    "T'→Y' has source T' ⊂ X' = X ×_Y Y'; the point meant is x' ∈ T' (chosen two sentences before, above x and y'), not x ∈ X. The TeX keeps the printed reading; the corrected edition (r20 current) already reads $x'$, and the mathematical notes record it ('Le point considéré en 14.5.8 est x'').",
    corrected="$x'$"))
L.append(F(219,
    "proof of (14.5.8), l. 13: 'par le morphisme composé Z' →(v) X'' → X' soit x''",
    "the label v over the first arrow (enlarged crop p219_s2_v.png)",
    "$Z'\\to X''\\to X'$ (no label)",
    "formula", None,
    {"old": "$Z'\\to X''\\to X'$", "new": "$Z'\\xrightarrow{v}X''\\to X'$"},
    "Written as Y'\\xrightarrow{h}X'\\to X in (14.5.4)."))
L.append(F(219,
    "proof of (14.5.8), l. 14: 'le morphisme composé u : Z' →(v) X'' → X répond donc à la question'",
    "the label v over the first arrow (enlarged crop p219_s2_u.png)",
    "$u:Z'\\to X''\\to X$ (no label)",
    "formula", None,
    {"old": "$u:Z'\\to X''\\to X$", "new": "$u:Z'\\xrightarrow{v}X''\\to X$"}))
L.append(F(219,
    "Proposition (14.5.9), l. 2: 'y un point géométriquement unibranche de Y'",
    "'géométriquement unibranche' in roman inside the italic statement (page_219_s2.png)",
    "italic (proposition environment)",
    "convention", 6,
    {"old": "un point géométriquement unibranche de $Y$", "new": "un point \\textup{géométriquement unibranche} de $Y$"}))
L.append(F(219,
    "proof of (14.5.9), l. 7: 'et a fortiori f est ouvert au point x'",
    "'a fortiori' in italics (enlarged crop p219_s3_fort.png)",
    "upright",
    "italics", None,
    {"old": "et a fortiori $f$", "new": "et \\emph{a fortiori} $f$"}))
L.append(F(219,
    "proof of (14.5.9), l. 8: 'f est donc ouvert en tous les points fermés de X_y = f^{-1}(y)'",
    "'fermés' in italics (same crop)",
    "upright",
    "italics", None,
    {"old": "points fermés de $X_y=f", "new": "points \\emph{fermés} de $X_y=f"}))
L.append(F(219,
    "proof of (14.5.9), l. 9: 'Mais X_y est un k(y)-préschéma localement de type fini'",
    "bold italic k (enlarged crop p219_s3_ky.png)",
    "plain k",
    "convention", 1,
    {"old": "un $k(y)$-préschéma", "new": "un $\\boldsymbol{k}(y)$-préschéma"}))


# ---------------- checks ----------------
def page_text(p):
    with open(os.path.join(RUN, "page_%03d.tex" % p), "rb") as fh:
        return fh.read().decode("utf-8").replace("\r\n", "\n")

ok = True
for d in L:
    fx = d["fix"]
    if fx is None:
        continue
    t = page_text(d["page"])
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, "page", d["page"], repr(fx["old"]))

# pairwise overlap check within each page (fixes must be independent)
by_page = {}
for i, d in enumerate(L):
    if d["fix"]:
        by_page.setdefault(d["page"], []).append(i)
for p, idx in by_page.items():
    t = page_text(p)
    spans = []
    for i in idx:
        o = L[i]["fix"]["old"]
        s = t.find(o)
        spans.append((s, s + len(o), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP page", p, repr(L[a[2]]["fix"]["old"]), repr(L[b[2]]["fix"]["old"]))

counts = {}
for d in L:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts", counts)
print("all unique" if ok else "PROBLEMS")

if ok and "--write" in sys.argv:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("wrote", OUT, len(L))
