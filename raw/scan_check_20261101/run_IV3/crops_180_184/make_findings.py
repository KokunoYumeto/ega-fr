import json

BASE = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = BASE + r"\findings_180_184.json"

F = []


def add(page, where, scan, tex, kind, fix, note=None, convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


LAB_P179 = ("Covered by the label-option edit of the (12.2.1) enumerate on p. 179 "
            "(findings_175_179: 'ouvertes~:\\n\\begin{enumerate}[label=(\\roman*)]' -> label=\\textup{(\\roman*)}).")

# ---------------------------------------------------------------- page 180
for lab in ["v", "vi", "vii", "viii", "ix", "x", "xi"]:
    add(180, "Théorème (12.2.1), label (%s)" % lab, "label (%s) upright" % lab,
        "label=(\\roman*) inside the italic theorem: italic label", "convention", None,
        LAB_P179, convention=6)
add(180, "Théorème (12.2.1) (xi): 'des multiplicités totales (4.7.12) de F_y'",
    "the reference (4.7.12) upright inside the italic statement (crop p180_xi_ref.png)",
    "(4.7.12) inside the italic theorem: italic", "convention",
    fx("(4.7.12)", "\\textup{(4.7.12)}"), convention=6)
add(180, "proof of (12.2.1), first word: 'A l'exception de (ii), (iii), ...'",
    "capital A without accent (crop p180_A.png)", "À l'exception", "word",
    fx("À l'exception", "A l'exception"),
    "As the earlier unaccented-capital fixes (IV-3 p. 116).")
add(180, "proof of (12.2.1): 'les propriétés P(y) considérées'",
    "bold italic P (property letter; crop p180_P.png)", "$P$ (plain italic)", "font",
    fx("les propriétés $P(y)$", "les propriétés $\\boldsymbol{P}(y)$"),
    "Property letter; plain $P$, not \\mathbf{P}, so not convention 10 (form of the earlier \\boldsymbol{P} page fixes).")
add(180, "proof of (12.2.1): '« pour tout x∈X_y, F_y a la propriété Q(x) »'",
    "bold italic Q (property letter; crop p180_QU.png)", "$Q$ (plain italic)", "font",
    fx("la propriété $Q(x)$~»", "la propriété $\\boldsymbol{Q}(x)$~»"))
add(180, "proof of (12.2.1): 'où Q(x) est l'une des propriétés (i) à (viii)'",
    "bold italic Q", "$Q$ (plain italic)", "font",
    fx("où $Q(x)$ est", "où $\\boldsymbol{Q}(x)$ est"))
add(180, "proof of (12.2.1): 'des x∈X tels que Q(x) soit vraie'",
    "bold italic Q", "$Q$ (plain italic)", "font",
    fx("$Q(x)$ soit vraie", "$\\boldsymbol{Q}(x)$ soit vraie"))
add(180, "proof of (12.2.1): 'des y∈Y tels que P(y) soit vraie'",
    "bold italic P", "$P$ (plain italic)", "font",
    fx("tels que $P(y)$", "tels que $\\boldsymbol{P}(y)$"))
add(180, "proof of (12.2.1): 'n'est autre que l'ensemble Y—f(X—U)'",
    "long dashes for the set difference, 2 times (crop p180_setmin.png)", "minus signs", "convention",
    fx("$Y-f(X-U)$", "$Y\\setmin f(X\\setmin U)$"),
    "One edit for both dashes; \\setmin pending the convention-7 decision.", convention=7)
add(180, "(12.2.1.1): 'Soit Y_1 un spectre d'anneau de valuation discrète tels que, si y_1 et y'_1 ...'",
    "'tels que' (crop p180_tels.png)", "'tel que': the TeX silently corrects", "misprint_in_print",
    fx("discrète tel que, si", "discrète tels que, si"),
    "Agreement error in the print ('tel' refers to 'un spectre'); the diplomatic text takes the printed 'tels'.",
    corrected="discrète tel que, si")
add(180, "(12.2.1.1): 'Utilisant (Err_III, 30)'",
    "bold 'Err' with a light (normal-weight) roman subscript III (crop p180_err.png)",
    "\\textbf{Err}\\textsubscript{\\textbf{III}}: bold subscript", "font",
    fx("\\textsubscript{\\textbf{III}}", "\\textsubscript{III}"),
    "ega4-10 writes the same reference as $\\mathbf{Err}_{\\mathrm{II}}$ (light subscript).")
add(180, "page break 180/181 (edit 1 of 2, insert): before (12.2.1.3)",
    "printed p. 180 ends with (12.2.1.2) '... des cas (i) et (ii).'; printed p. 181 begins '(12.2.1.3) Cas (xi) :' (page_181_s1.png)",
    "\\oldpage[IV-3]{181} after \\begin{env}[12.2.1.3]\\label{...}: the heading (12.2.1.3) falls in the p. 180 segment",
    "marker", fx("\\begin{env}[12.2.1.3]", "\\oldpage[IV-3]{181}\n\\begin{env}[12.2.1.3]"),
    "Marker move (markers-after-\\begin pattern, GLOBAL_ISSUES 37): apply together with the p. 181 entry that removes the old marker (edit 2 of 2).")

# ---------------------------------------------------------------- page 181
add(181, "page break 180/181 (edit 2 of 2, remove the old marker): '(12.2.1.3) Cas (xi)'",
    "p. 181 opens with the heading (12.2.1.3)", "\\oldpage[IV-3]{181} after \\label{IV.12.2.1.3-fr}",
    "marker", fx("\\oldpage[IV-3]{181}\nCas (xi)", "Cas (xi)"),
    "Apply together with the p. 180 insert (edit 1 of 2).")
add(181, "(12.2.1.3): 'qui prouve que la fonction z⇝l(z) est constructible'",
    "wavy arrow ⇝ (crop p181_wavy_z.png)", "\\mapsto", "symbol",
    fx("$z\\mapsto l(z)$", "$z\\leadsto l(z)$"), "GLOBAL_ISSUES 33; \\leadsto as in the earlier page fixes.")
add(181, "Lemme (12.2.1.4): 'z_i (resp. z'_j) les points maximaux'",
    "'(resp. z'_j)' upright: roman 'resp.' and upright parentheses (crop p181_resp.png)",
    "(resp. $z'_j$) inside the italic lemma: italic", "convention",
    fx("(resp. $z'_j$)", "\\textup{(resp. $z'_j$)}"), convention=6)
add(181, "Lemme (12.2.1.4): '(resp. Supp(F_{y'}))'",
    "'(resp. Supp(F_{y'}))' upright", "inside the italic lemma: italic", "convention",
    fx("(resp.\n$\\operatorname{Supp}(\\mathcal F_{y'})$)", "\\textup{(resp.\n$\\operatorname{Supp}(\\mathcal F_{y'})$)}"),
    convention=6)
add(181, "proof of (12.2.1.4), second display: 'Σ long((F_y)_{z_i}) ⩾ ΣΣ_k long((F_{y'})_{z'_{ik}})'",
    "the first Σ and the first Σ of the double sum carry no index (only k under the second; crop p181_sums.png)",
    "\\sum_i ... \\geq\\sum_i\\sum_k", "formula",
    fx("\\sum_i\\operatorname{long}((\\mathcal F_y)_{z_i})\n  \\geq\\sum_i\\sum_k",
       "\\sum\\operatorname{long}((\\mathcal F_y)_{z_i})\n  \\geq\\sum\\sum_k"),
    "Indices i added by the TeX. The heavier-looking z of z_i and k of the first display were measured (ink.py: mean stroke run 5.4 against 5.4 and 5.3 against 4.8-5.4 for the other subscript letters): ordinary sorts, not reported.")
add(181, "end of the second display of the proof of (12.2.1.4)",
    "no full stop after the display (crop p181_sum2_right.png)", "full stop after the display", "punctuation",
    fx("_{z'_{ik}}).", "_{z'_{ik}})"))
add(181, "after the second display: 'Le lemme sera donc prouvé si ...'",
    "'Le lemme sera donc prouvé' starts flush left: the paragraph continues after the display",
    "blank line after \\]: new indented paragraph", "other",
    fx("\\]\n\nLe lemme", "\\]\nLe lemme"))
add(181, "Corollaire (12.2.2): 'Sous les hypothèses de (12.2.1) :'",
    "the reference (12.2.1) upright inside the italic statement", "italic (corollary environment)", "convention",
    fx("Sous les hypothèses de (12.2.1)~:", "Sous les hypothèses de \\textup{(12.2.1)}~:"), convention=6)
add(181, "Corollaire (12.2.2), label (i)", "labels (i)-(iv) upright (crop p181_cor_a.png)",
    "label=(\\roman*) inside the italic corollary: italic labels", "convention",
    fx("\\begin{enumerate}[label=(\\roman*)]", "\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
    "One edit of the label option covers (i)-(iv) (next entries; (iv) is filed under p. 182). GLOBAL_ISSUES 16.",
    convention=6)
add(181, "Corollaire (12.2.2), label (ii)", "label (ii) upright", "italic (same enumerate)", "convention", None,
    "Covered by the previous edit (label=\\textup{(\\roman*)}).", convention=6)
add(181, "Corollaire (12.2.2), label (iii)", "label (iii) upright", "italic (same enumerate)", "convention", None,
    "Covered by the previous edit (label=\\textup{(\\roman*)}).", convention=6)
add(181, "Corollaire (12.2.2) (i): 'La fonction y⇝dim(Supp(F_y))'",
    "wavy arrow ⇝ (crop p181_cor_a.png)", "\\mapsto", "symbol",
    fx("$y\\mapsto\\dim(\\operatorname{Supp}(\\mathcal F_y))$", "$y\\leadsto\\dim(\\operatorname{Supp}(\\mathcal F_y))$"))
add(181, "Corollaire (12.2.2) (ii): 'La fonction y⇝coprof(F_y)'", "wavy arrow ⇝", "\\mapsto", "symbol",
    fx("$y\\mapsto\\operatorname{coprof}", "$y\\leadsto\\operatorname{coprof}"))
add(181, "Corollaire (12.2.2) (ii): 'coprof(F_y) (5.7.1) est semi-continue'",
    "the reference (5.7.1) upright inside the italic statement", "italic (corollary environment)", "convention",
    fx("(5.7.1)", "\\textup{(5.7.1)}"), convention=6)
add(181, "Corollaire (12.2.2) (iii): 'La fonction y⇝l(y)'", "wavy arrow ⇝", "\\mapsto", "symbol",
    fx("$y\\mapsto l(y)$", "$y\\leadsto l(y)$"))
add(181, "Corollaire (12.2.2) (iii): 'l(y) (12.2.1, (xi)) est semi-continue'",
    "the reference (12.2.1, (xi)) upright inside the italic statement", "italic (corollary environment)", "convention",
    fx("(12.2.1, (xi))", "\\textup{(12.2.1, (xi))}"), convention=6)

# ---------------------------------------------------------------- page 182
ITEM_IV = "Apply before the marker move below (after it this text belongs to the p. 181 segment)."
add(182, "Corollaire (12.2.2) (iv) (printed at the foot of p. 181; TeX in the p. 182 segment): 'La fonction y⇝prof*(F_y)'",
    "wavy arrow ⇝ (crop p181_cor_b.png); the star is an asterisk (crop p181_profstar.png)", "\\mapsto", "symbol",
    fx("$y\\mapsto\\operatorname{prof}", "$y\\leadsto\\operatorname{prof}"), ITEM_IV)
add(182, "Corollaire (12.2.2) (iv) (printed p. 181): 'prof*(F_y) (10.8.1) est semi-continue'",
    "the reference (10.8.1) upright inside the italic statement", "italic (corollary environment)", "convention",
    fx("(10.8.1)", "\\textup{(10.8.1)}"), ITEM_IV, convention=6)
add(182, "Corollaire (12.2.2), label (iv) (printed p. 181)", "label (iv) upright", "italic (same enumerate)",
    "convention", None, "Covered by the p. 181 label-option edit (label=\\textup{(\\roman*)}).", convention=6)
add(182, "page break 181/182 (edit 1 of 2, remove the old marker): before item (iv) of (12.2.2)",
    "item (iv) of Corollaire (12.2.2) is the last line of printed p. 181 (page_181_s4.png); printed p. 182 begins with the proof, '(i) Il résulte de (12.2.1, (i))' (page_182_s1.png)",
    "\\oldpage[IV-3]{182} before the last \\item of the corollary: one item (one printed line) too early",
    "marker", fx("\\oldpage[IV-3]{182}\n  \\item La fonction", "\\item La fonction"),
    "Apply together with edit 2 of 2 (next entry), after the two item-(iv) entries above. Leaves '  \\item La fonction' (the marker line's indentation).")
add(182, "page break 181/182 (edit 2 of 2, insert): before the proof of (12.2.2)",
    "printed p. 182 begins with the proof of (12.2.2)", "no marker before \\begin{proof}", "marker",
    fx("\\end{corollary}\n\n\\begin{proof}", "\\end{corollary}\n\n\\oldpage[IV-3]{182}\n\\begin{proof}"),
    "Apply together with edit 1 of 2 (previous entry).")
add(182, "proof of (12.2.2) (i): 'que z⇝dim(Supp(F_z)) est semi-continue'",
    "wavy arrow ⇝ (crop p182_wavy.png)", "\\mapsto", "symbol",
    fx("$z\\mapsto\\dim", "$z\\leadsto\\dim"))
add(182, "proof of (12.2.2): 'l'ensemble des x∈X tels que prof*_x(F_{f(x)}) ⩽ k est ouvert'",
    "prof*_x: subscript x (crop p182_profx.png)", "\\operatorname{prof}^{*}_{f(x)}: subscript f(x)", "formula",
    fx("\\operatorname{prof}^{*}_{f(x)}", "\\operatorname{prof}^{*}_x"))
add(182, "Remarques (12.2.3) (ii): 'soit X_0 le sous-schéma fermé « réunion de la droite X_1 ...'",
    "'sous-schéma' (crop p182_sousschema.png)", "sous-préschéma", "word",
    fx("sous-préschéma fermé «", "sous-schéma fermé «"))
add(182, "Remarques (12.2.3) (ii): 'du plan X_2 défini par t_2—t_3=0'",
    "long dash for the subtraction (bar 36 px; '=' bars 26 px)", "minus sign", "convention",
    fx("$t_2-t_3=0$", "$t_2\\setmin t_3=0$"),
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.", convention=7)
add(182, "Remarques (12.2.3) (ii): 'c=C(t_2—t_3)'",
    "long dash for the subtraction (bar 36 px; '=' bars 26 px)", "minus sign", "convention",
    fx("$\\mathfrak c=C(t_2-t_3)$", "$\\mathfrak c=C(t_2\\setmin t_3)$"), convention=7)
add(182, "Remarques (12.2.3) (ii): 'l'homomorphisme d'algèbres graduées k[t_0,t_2]→k[t_0,t_1,t_2,t_3]/a obtenu par passage au quotient'",
    "in the running text (crop p182_frak2.png)", "displayed with \\[ ... \\]", "other",
    fx("graduées\n  \\[\n    k[t_0,t_2]\\longrightarrow k[t_0,t_1,t_2,t_3]/\\mathfrak a\n  \\]\n  obtenu",
       "graduées\n  $k[t_0,t_2]\\longrightarrow k[t_0,t_1,t_2,t_3]/\\mathfrak a$\n  obtenu"),
    "Layout only (display vs inline); the formula itself matches.")
add(182, "Remarques (12.2.3) (ii): 'et l'anneau C'=k[t_1,t_2,t_3]/(t_2—t_3)((t_1)+(t_3)) un k[t_2]-module sans torsion'",
    "in the running text", "displayed with \\[ ... \\]", "other",
    fx("l'anneau\n  \\[\n    C'=k[t_1,t_2,t_3]/(t_2-t_3)((t_1)+(t_3))\n  \\]\n  un",
       "l'anneau\n  $C'=k[t_1,t_2,t_3]/(t_2\\setmin t_3)((t_1)+(t_3))$\n  un"),
    "The same edit writes the printed long dash as \\setmin (convention 7, next entry).")
add(182, "Remarques (12.2.3) (ii): '(t_2—t_3)' in C'", "long dash for the subtraction (bar 35 px; '+' 25 px)",
    "minus sign", "convention", None, "Included in the previous (inline) edit.", convention=7)
add(182, "Remarques (12.2.3) (iii): 'm est idéal premier associé immergé de A/At^4'",
    "'immergé' italic (crop p182_immerge.png)", "upright", "italics",
    fx("associé immergé de $A/At^4$", "associé \\emph{immergé} de $A/At^4$"),
    "Remark body judged as roman.")
add(182, "Remarques (12.2.3) (iii): '... associé immergé de A/At^4'",
    "A/At^4 (crop p182_immerge.png)", "$A/At^4$: the TeX keeps the printed reading", "misprint_in_print", None,
    "m is the maximal ideal of B = k[t^4,t^3u,tu^3,u^4], so it can only be associated to a B-module: the fibre ring "
    "B/t^4B of f over y=(t) (A=k[t], t -> t^4). Check: t^6u^2 is not in t^4B, and m t^6u^2 lies in t^4B. "
    "A/At^4 is an A-module whose only associated prime is tA.",
    confidence="medium", corrected="$B/Bt^4$")
add(182, "Remarques (12.2.3) (iii): 'étant le spectre d'une k(y')-algèbre intègre'",
    "bold italic k", "plain k", "convention",
    fx("$k(y')$-algèbre", "$\\boldsymbol{k}(y')$-algèbre"), convention=1)

# ---------------------------------------------------------------- page 183
add(183, "Remarques (12.2.3) (vi), 2nd paragraph: 'On prendra en effet ici P comme dans la Remarque (ii), puis dans P'",
    "'puis dans P' (crop p183_puis.png)", "'et dans $P$'", "word",
    fx("(ii), et dans", "(ii), puis dans"))
add(183, "same sentence: 'puis dans P le sous-schéma fermé X_0'",
    "the e of 'le' is a bold roman e (wrong font; 10x crops p183_le_e.png against p183_comme_e.png)",
    "'le' (roman): the TeX silently normalizes it", "misprint_in_print",
    fx("$P$ le", "$P$ l\\textbf{e}"),
    "Wrong-font sort (GLOBAL_ISSUES 29). ink.py: 153 dark px, mean stroke run 6.95 px, against 106-108 px and 4.7-5.1 px for the ordinary e's of the line; the l beside it is ordinary (103 px, 4.29). Apply only if wrong-font sorts are reproduced; independent of the two word fixes beside it (no overlap).",
    confidence="medium", corrected="$P$ le")
add(183, "same sentence: 'le sous-schéma fermé X_0 réunion des trois droites'",
    "'sous-schéma'", "sous-préschéma", "word",
    fx("sous-préschéma", "sous-schéma"))
add(183, "same paragraph: 't_1—t_0=t_3=0'",
    "long dash for the subtraction (bar 35 px; '=' bars 26 px)", "minus sign", "convention",
    fx("$t_1-t_0=t_3=0$", "$t_1\\setmin t_0=t_3=0$"), convention=7)
add(183, "Théorème (12.2.4), label (i)", "labels (i)-(ix) upright",
    "label=(\\roman*) inside the italic theorem: italic labels", "convention",
    fx("\\begin{enumerate}[label=(\\roman*)]", "\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
    "One edit of the label option covers (i)-(ix) (next entries). GLOBAL_ISSUES 16.", convention=6)
for lab in ["ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]:
    add(183, "Théorème (12.2.4), label (%s)" % lab, "label (%s) upright" % lab, "italic (same enumerate)",
        "convention", None, "Covered by the previous edit (label=\\textup{(\\roman*)}).", convention=6)
add(183, "Théorème (12.2.4) (iii): 'géométriquement régulier (i.e. lisse sur k(y))'",
    "'(i.e.' and the closing parenthesis upright, 'lisse sur' italic (crop p183_ie.png)",
    "(i.e. lisse sur $k(y)$) all italic", "convention",
    fx("(i.e. lisse sur $k(y)$).", "\\textup{(i.e.} lisse sur $\\boldsymbol{k}(y)$\\textup{)}."),
    "The same edit sets the bold italic k (convention 1, next entry).", convention=6)
add(183, "Théorème (12.2.4) (iii): 'lisse sur k(y)'", "bold italic k", "plain k", "convention", None,
    "Included in the previous edit.", convention=1)
add(183, "Théorème (12.2.4) (vii): 'ponctuellement intègre (4.6.9)'",
    "the reference (4.6.9) upright inside the italic statement (crop p183_469.png)", "italic (theorem environment)",
    "convention", fx("intègre (4.6.9)", "intègre \\textup{(4.6.9)}"), convention=6)
add(183, "Théorème (12.2.4) (ix): 'la multiplicité totale (4.7.4) de X_y'",
    "the reference (4.7.4) upright inside the italic statement (crop p183_474.png)", "italic (theorem environment)",
    "convention", fx("(4.7.4)", "\\textup{(4.7.4)}"), convention=6)
add(183, "Théorème (12.2.4) (ix): 'de X_y sur k(y) soit ⩽ k'", "bold italic k", "plain k", "convention",
    fx("sur $k(y)$\n  soit", "sur $\\boldsymbol{k}(y)$\n  soit"), convention=1)
add(183, "proof of (12.2.4): 'soit isomorphe à (k(z))^m'", "bold italic k", "plain k", "convention",
    fx("$(k(z))^m$", "$(\\boldsymbol{k}(z))^m$"), convention=1)
add(183, "subsection heading 12.3", "'... et localement de présentation finie.' (final full stop)",
    "\\subsection{... localement de présentation finie} (no full stop)", "punctuation",
    fx("localement de présentation finie}", "localement de présentation finie.}"),
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(183, "Lemme (12.3.1) c): 'M⊗_A k(y) est un'", "bold italic k (crop p183_lemma_c2.png)", "plain k", "convention",
    fx("$M\\otimes_Ak(y)$ est un", "$M\\otimes_A\\boldsymbol{k}(y)$ est un"), convention=1)
add(183, "Lemme (12.3.1) c): '(B⊗_A k(y))-module projectif'", "bold italic k", "plain k", "convention",
    fx("$(B\\otimes_Ak(y))$-module", "$(B\\otimes_A\\boldsymbol{k}(y))$-module"), convention=1)
add(183, "page break 183/184 (edit 1 of 2, insert): before the proof of (12.3.1)",
    "printed p. 183 ends with item c) of Lemme (12.3.1); printed p. 184 begins with its proof 'L'équivalence de a) et b) ...' (page_184_s1.png)",
    "\\begin{proof} stands before \\oldpage[IV-3]{184}, in the p. 183 segment", "marker",
    fx("\\end{lemma}\n\n\\begin{proof}", "\\end{lemma}\n\n\\oldpage[IV-3]{184}\n\\begin{proof}"),
    "Marker move (markers-after-\\begin pattern): apply together with the p. 184 entry that removes the old marker (edit 2 of 2).")

# ---------------------------------------------------------------- page 184
add(184, "page break 183/184 (edit 2 of 2, remove the old marker): 'L'équivalence de a) et b)'",
    "p. 184 opens with the proof of (12.3.1)", "\\oldpage[IV-3]{184} after \\begin{proof}", "marker",
    fx("\\oldpage[IV-3]{184}\nL'équivalence", "L'équivalence"),
    "Apply together with the p. 183 insert (edit 1 of 2).")
add(184, "proof of (12.3.1): 'L'équivalence de a) et b) résulte de Bourbaki'",
    "a), b) italic, letters and parentheses (crop p184_ab.png)", "$a)$, $b)$: italic letter, upright parenthesis",
    "italics", fx("de $a)$ et $b)$ résulte", "de \\emph{a)} et \\emph{b)} résulte"),
    "Same form as the IV-2 p. 209 fix.")
add(184, "proof of (12.3.1): 'Comme a) implique c) trivialement, il reste à prouver que c) implique b),'",
    "a), c), c), b) italic, letters and parentheses (crop p184_ac.png)", "$a)$, $c)$, $c)$, $b)$: upright parentheses",
    "italics",
    fx("Comme $a)$ implique $c)$\ntrivialement, il reste à prouver que $c)$ implique $b)$,",
       "Comme \\emph{a)} implique \\emph{c)}\ntrivialement, il reste à prouver que \\emph{c)} implique \\emph{b)},"))
add(184, "Proposition (12.3.2), label (i)", "labels (i), (ii) upright",
    "label=(\\roman*) inside the italic proposition: italic labels", "convention",
    fx("Alors~:\n\\begin{enumerate}[label=(\\roman*)]", "Alors~:\n\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
    "One edit of the label option covers (i) and (ii) (next entry). GLOBAL_ISSUES 16.", convention=6)
add(184, "Proposition (12.3.2), label (ii)", "label (ii) upright", "italic (same enumerate)", "convention", None,
    "Covered by the previous edit (label=\\textup{(\\roman*)}).", convention=6)
add(184, "(12.3.2.1): 'dim.proj_{B⊗_A k(y)}(M⊗_A k(y))'",
    "subscript k bold upright, the k of M⊗_A k(y) bold italic (crop p184_disp.png)", "plain k, 2 times", "convention",
    fx("\\operatorname{dim.proj}_{B\\otimes_Ak(y)}(M\\otimes_Ak(y))\n    =\\operatorname{Tor.dim}",
       "\\operatorname{dim.proj}_{B\\otimes_A\\mathbf{k}(y)}(M\\otimes_A\\boldsymbol{k}(y))\n    =\\operatorname{Tor.dim}"),
    "Two occurrences; \\mathbf for the subscript k (GLOBAL_ISSUES 48).", convention=1)
add(184, "Proposition (12.3.2) (ii): 'Tor.dim_B(M) est le plus petit entier i tel que'",
    "'plus petit entier' italic like the rest of the statement, no change of face (crop p184_ppe.png)",
    "\\emph{plus petit entier} inside the italic proposition: upright", "convention",
    fx("\\emph{plus petit entier}", "plus petit entier"), convention=6)
add(184, "proof of (12.3.2) (ii): 'on a dim.proj_{B⊗_A k(y)}(M⊗_A k(y)) ⩽ dim.proj_B(M). Pour prouver'",
    "in the running text (crop p184_inline.png)", "displayed with \\[ ... \\]", "other",
    fx("on a\n  \\[\n    \\operatorname{dim.proj}_{B\\otimes_Ak(y)}(M\\otimes_Ak(y))\n    \\leq\\operatorname{dim.proj}_B(M).\n  \\]\n  Pour prouver",
       "on a\n  $\\operatorname{dim.proj}_{B\\otimes_A\\mathbf{k}(y)}(M\\otimes_A\\boldsymbol{k}(y))\\leq\\operatorname{dim.proj}_B(M)$.\n  Pour prouver"),
    "The same edit sets the two k's (convention 1, next entry).")
add(184, "same formula: subscript k (bold upright) and k of M⊗_A k(y) (bold italic)", "bold k, 2 times", "plain k",
    "convention", None, "Included in the previous (inline) edit.", convention=1)
add(184, "proof of (12.3.2) (ii): '(resp. dim.proj_{B⊗_A k(y)}(M⊗_A k(y)) ⩽ n pour tout y∈Spec(A))'",
    "subscript k bold upright, the k of M⊗_A k(y) bold italic (crop p184_resp.png)", "plain k, 2 times", "convention",
    fx("(resp.\n  $\\operatorname{dim.proj}_{B\\otimes_Ak(y)}(M\\otimes_Ak(y))",
       "(resp.\n  $\\operatorname{dim.proj}_{B\\otimes_A\\mathbf{k}(y)}(M\\otimes_A\\boldsymbol{k}(y))"),
    "Two occurrences.", convention=1)
add(184, "proof of (12.3.2) (ii): 'R ... est un B-module de type fini qui est aussi un A-module plat'",
    "'qui est aussi' (crop p184_quiest.png)", "'et aussi'", "word",
    fx("de type fini et aussi un", "de type fini qui est aussi un"))
add(184, "proof of (12.3.2) (ii): 'L'hypothèse dim.proj_{B⊗_A k(y)}(M⊗_A k(y)) ⩽ n pour tout y∈Spec(A)'",
    "subscript k bold upright, the other k bold italic", "plain k, 2 times", "convention",
    fx("L'hypothèse\n  $\\operatorname{dim.proj}_{B\\otimes_Ak(y)}(M\\otimes_Ak(y))",
       "L'hypothèse\n  $\\operatorname{dim.proj}_{B\\otimes_A\\mathbf{k}(y)}(M\\otimes_A\\boldsymbol{k}(y))"),
    "Two occurrences.", convention=1)
add(184, "proof of (12.3.2) (ii): 'par tensorisation avec k(y)'", "bold italic k", "plain k", "convention",
    fx("avec\n  $k(y)$, que", "avec\n  $\\boldsymbol{k}(y)$, que"), convention=1)
add(184, "proof of (12.3.2) (ii), display: '0→R⊗_A k(y)→L_{n-1}⊗_A k(y)→'",
    "bold italic k, 2 times (crop p184_seq.png)", "plain k", "convention",
    fx("0\\to R\\otimes_Ak(y)\\to L_{n-1}\\otimes_Ak(y)",
       "0\\to R\\otimes_A\\boldsymbol{k}(y)\\to L_{n-1}\\otimes_A\\boldsymbol{k}(y)"),
    "Two occurrences.", convention=1)
add(184, "same display: '→. . .→'", "baseline dots (crop p184_dots.png)", "\\cdots", "symbol",
    fx("\\cdots", "\\ldots"))
add(184, "same display: '→L_0⊗_A k(y)→M⊗_A k(y)→0'", "bold italic k, 2 times", "plain k", "convention",
    fx("L_0\\otimes_Ak(y)\\to M\\otimes_Ak(y)", "L_0\\otimes_A\\boldsymbol{k}(y)\\to M\\otimes_A\\boldsymbol{k}(y)"),
    "Two occurrences.", convention=1)
add(184, "after the display: 'R⊗_A k(y) est un'", "bold italic k", "plain k", "convention",
    fx("$R\\otimes_Ak(y)$ est un", "$R\\otimes_A\\boldsymbol{k}(y)$ est un"), convention=1)
add(184, "after the display: '(B⊗_A k(y))-module projectif'", "bold italic k", "plain k", "convention",
    fx("$(B\\otimes_Ak(y))$-module", "$(B\\otimes_A\\boldsymbol{k}(y))$-module"), convention=1)
add(184, "Proposition (12.3.3): 'le complexe L_•⊗_{O_S} k(s)'", "bold italic k (crop p184_ks_zoom2.png)", "plain k",
    "convention", fx("\\otimes_{\\mathcal O_S}k(s)", "\\otimes_{\\mathcal O_S}\\boldsymbol{k}(s)"), convention=1)

# ---------------------------------------------------------------- checks
problems = []
texts = {}
for p in (179, 180, 181, 182, 183, 184):
    with open(BASE + r"\page_%03d.tex" % p, encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")
for i, d in enumerate(F):
    f = d["fix"]
    if f is None:
        continue
    n = texts[d["page"]].count(f["old"])
    if n != 1:
        problems.append((i, d["page"], n, f["old"]))
    if f["old"] == f["new"]:
        problems.append((i, d["page"], "same", f["old"]))

# overlap check per page (spans in the original text)
for p in (180, 181, 182, 183, 184):
    spans = []
    for i, d in enumerate(F):
        if d["page"] == p and d["fix"]:
            s = texts[p].find(d["fix"]["old"])
            spans.append((s, s + len(d["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            problems.append(("overlap", p, a[2], b[2]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "misprint_in_print":
        c[2] += 1
    elif d["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("entries:", len(F))
print("counts (normal/convention/misprint):", counts)
print("problems:", problems)
