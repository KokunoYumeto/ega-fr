import json

OUT = r"user\Documents\ega_scan_check_20261101\run_II\findings_115_119.json"
NL = "\n"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv,
             confidence=conf, fix=None if old is None else {"old": old, "new": new})
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def bold_ref(page, where, ref, old, new, note=""):
    add(page, where, ref + " with bold " + ("0" if ref.startswith("(0") else "I"),
        ref + " with plain " + ("0" if ref.startswith("(0") else "I") + " in the link text",
        "convention", 2, "high", old, new, note)


def bold_k(page, where, scan, tex, old, new, note="Bold italic k in the print, plain k in the TeX."):
    add(page, where, scan, tex, "convention", 1, "high", old, new, note)


def label_up(page, where, lab, old, new):
    add(page, where, "label " + lab + " upright (roman)",
        r"\item[" + lab + "] inside the italic statement environment (comes out italic)",
        "convention", 6, "high", old, new,
        "Checked on a crop. Roman label inside an italic statement (GLOBAL_ISSUES item 16).")


# ---------------------------------------------------------------- page 115
label_up(115, "Proposition (6.2.1), item a)", "a)", r"\item[a)] Le point", r"\item[\textup{a)}] Le point")
label_up(115, "Proposition (6.2.1), item b)", "b)", r"\item[b)] L'anneau", r"\item[\textup{b)}] L'anneau")
add(115, "Proposition (6.2.1) b), end: 'quasi-fini (0, 7.4.1).'",
    "the reference (0, 7.4.1) upright", "italic (inside the italic proposition environment)",
    "convention", 6, "high",
    r"quasi-fini (\hyperref[0.7.4.1-fr]", r"quasi-fini \upshape(\hyperref[0.7.4.1-fr]",
    r"Checked on a crop. The reference ends the statement, so the \upshape switch (closed by \end{enumerate}) "
    r"covers exactly the reference and the final period. Independent of the bold-0 edit inside the braces.")
bold_ref(115, "Proposition (6.2.1) b)", "(0, 7.4.1)", "{0, 7.4.1}", r"{\textbf{0}, 7.4.1}")
bold_ref(115, "proof of (6.2.1): 'A étant une B-algèbre de type fini (I, 6.3.3)'", "(I, 6.3.3)",
         "{I, 6.3.3}", r"{\textbf{I}, 6.3.3}")
bold_ref(115, "proof of (6.2.1): 'ni l'anneau local O_x (I, 3.6.5)'", "(I, 3.6.5)",
         "{I, 3.6.5}", r"{\textbf{I}, 3.6.5}")
bold_k(115, "proof of (6.2.1): 'de type fini sur k(f(x))=B/n'", "𝒌(f(x))=B/𝔫", "$k(f(x))=B/\\mathfrak{n}$",
       r"$k(f(x))=B/\mathfrak{n}$", r"$\boldsymbol{k}(f(x))=B/\mathfrak{n}$")
bold_ref(115, "proof of (6.2.1): 'B/n (I, 6.4.11). Cela étant'", "(I, 6.4.11)",
         "{I, 6.4.11}). Cela", r"{\textbf{I}, 6.4.11}). Cela")
add(115, "proof of (6.2.1): 'Cela étant, si a) est vérifiée'", "a) italic", "a) upright",
    "italics", None, "high", "si a) est vérifiée", r"si \emph{a)} est vérifiée", "Checked on the strip.")
bold_ref(115, "proof of (6.2.1): 'de rang fini sur B/n (I, 6.4.4), autrement dit'", "(I, 6.4.4)",
         "{I, 6.4.4}), autrement", r"{\textbf{I}, 6.4.4}), autrement")
bold_ref(115, "proof of (6.2.1): 'donc discret (I, 6.4.4); par suite'", "(I, 6.4.4)",
         "{I, 6.4.4})~; par suite", r"{\textbf{I}, 6.4.4})~; par suite")
add(115, "proof of (6.2.1), end: 'et cela montre que b) entraîne a).'", "b) and a) italic", "upright",
    "italics", None, "high", "que b) entraîne a).", r"que \emph{b)} entraîne \emph{a)}.", "")
label_up(115, "Corollaire (6.2.2), item a)", "a)", r"\item[a)] Tout point", r"\item[\textup{a)}] Tout point")
add(115, "Corollaire (6.2.2) a): '(autrement dit le sous-espace f^{-1}(f(x)) est discret).'",
    "the parenthesis upright: '(autrement dit le sous-espace ... est' roman, 'discret' italic, ')' roman",
    "the whole parenthesis italic (inside the italic corollary environment)",
    "convention", 6, "high",
    r"(autrement dit le sous-espace $f^{-1}(f(x))$ est discret)",
    r"\textup{(autrement dit le sous-espace $f^{-1}(f(x))$ est \emph{discret})}",
    r"Checked on a crop. Inside \textup the \emph gives the printed italic 'discret'.")
label_up(115, "Corollaire (6.2.2), item b)", "b)", r"\item[b)] Pour tout", r"\item[\textup{b)}] Pour tout")
bold_k(115, "Corollaire (6.2.2) b): 'est un k(f(x))-préschéma fini'", "𝒌(f(x))-préschéma fini",
       "$k(f(x))$-préschéma fini", r"$k(f(x))$-préschéma fini", r"$\boldsymbol{k}(f(x))$-préschéma fini")
label_up(115, "Corollaire (6.2.2), item c)", "c)", r"\item[c)] Pour tout", r"\item[\textup{c)}] Pour tout")
add(115, "proof of (6.2.2): 'L'équivalence de a) et c) résulte de (6.2.1)'", "a) and c) italic", "upright",
    "italics", None, "high", "de a) et c) résulte", r"de \emph{a)} et \emph{c)} résulte", "")
bold_k(115, "proof of (6.2.2): 'est un k(f(x))-préschéma algébrique'", "𝒌(f(x))-préschéma algébrique",
       "$k(f(x))$-préschéma algébrique", r"$k(f(x))$-préschéma algébrique",
       r"$\boldsymbol{k}(f(x))$-préschéma algébrique")
bold_ref(115, "proof of (6.2.2): 'préschéma algébrique (I, 6.4.11),'", "(I, 6.4.11)",
         "{I, 6.4.11}),", r"{\textbf{I}, 6.4.11}),")
add(115, "proof of (6.2.2): 'l'équivalence de a) et b) résulte de (I, 6.4.4)'", "a) and b) italic", "upright",
    "italics", None, "high", "de a) et b) résulte", r"de \emph{a)} et \emph{b)} résulte", "")
bold_ref(115, "proof of (6.2.2), end: 'résulte de (I, 6.4.4).'", "(I, 6.4.4)",
         "{I, 6.4.4}).", r"{\textbf{I}, 6.4.4}).")
add(115, "Définition (6.2.3): 'vérifiant les conditions équivalentes de (6.2.2)'",
    "the reference (6.2.2) upright", "italic (inside the italic definition environment)",
    "convention", 6, "high", r"(\hyperref[II.6.2.2-fr]{6.2.2})", r"\textup{(\hyperref[II.6.2.2-fr]{6.2.2})}",
    "Checked on a crop.")
add(115, "Définition (6.2.3): 'on dit que f est quasi-fini'",
    "'quasi-fini' in the same italic as the rest of the definition (no change of face)",
    r"\emph{quasi-fini} inside the italic definition environment (comes out upright)",
    "convention", 6, "high", r"\emph{quasi-fini}", "quasi-fini",
    r"Checked on a crop. Printed italic word left upright by \emph inside the italic environment; drop the \emph.")
add(115, "after (6.2.3): 'Il est clair que tout morphisme fini est quasi-fini (6.1.8).'",
    "'fini' italic", "upright", "italics", None, "high",
    "tout morphisme fini est", r"tout morphisme \emph{fini} est", "Checked on a crop.")
label_up(115, "Proposition (6.2.4), item (i)", "(i)", r"\item[(i)] Une immersion", r"\item[\textup{(i)}] Une immersion")
label_up(115, "Proposition (6.2.4), item (ii)", "(ii)", r"\item[(ii)] Si", r"\item[\textup{(ii)}] Si")
label_up(115, "Proposition (6.2.4), item (iii)", "(iii)", r"\item[(iii)] Si", r"\item[\textup{(iii)}] Si")
label_up(115, "Proposition (6.2.4), item (iv)", "(iv)", r"\item[(iv)] Si", r"\item[\textup{(iv)}] Si")
add(115, "Proposition (6.2.4) (iv), display",
    "f×_S g : X×_S Y→X'×_S Y'",
    r"f\times_S g:X\times_S Y\to X'\times_S Y' (same as the print)",
    "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading. With f : X→Y and g : X'→Y' as stated in (iv), f×_S g goes from "
    "X×_S X' to Y×_S Y'; the printed source and target follow the lettering of (I, 3.5.1) (f : X→X', g : Y→Y'). "
    "Checked on a 2x crop. Not in the EGA III list of errata to EGA II.",
    corrected=r"f\times_S g:X\times_S X'\to Y\times_S Y'")
label_up(115, "Proposition (6.2.4), item (v)", "(v)", r"\item[(v)] Soient", r"\item[\textup{(v)}] Soient")
label_up(115, "Proposition (6.2.4), item (vi)", "(vi)", r"\item[(vi)] Si", r"\item[\textup{(vi)}] Si")
bold_ref(115, "proof of (6.2.4): '(I, 6.3.4 (i) et 6.3.5)'", "(I, 6.3.4 (i) et 6.3.5)",
         "{I, 6.3.4 (i) et", r"{\textbf{I}, 6.3.4 (i) et")
bold_ref(115, "proof of (6.2.4): 'est de type fini (I, 6.3.4 (ii))'", "(I, 6.3.4 (ii))",
         "{I, 6.3.4 (ii)}", r"{\textbf{I}, 6.3.4 (ii)}")
add(115, "end of p. 115 / top of p. 116, proof of (6.2.4): '... un voisinage ouvert de x ne rencontrant aucun | des f^{-1}(y')'",
    "one paragraph across the page break (p. 116 starts flush left with 'des f^{-1}(y')')",
    r"blank line before \oldpage[II]{116} (paragraph break)",
    "other", None, "high", "ne rencontrant aucun" + NL + NL, "ne rencontrant aucun" + NL,
    r"Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line is the last line "
    r"of page 115's segment. Apply together with the p. 116 entry that removes the blank line after the marker. "
    r"\oldpage ends with \ignorespaces, so joining the lines leaves a single space.")

# ---------------------------------------------------------------- page 116
add(116, "top of p. 116: 'des f^{-1}(y'), où y'≠y est dans g^{-1}(z)' (continues the proof of (6.2.4))",
    "continuation of the paragraph of p. 115, flush left",
    r"blank line after \oldpage[II]{116} (paragraph break)",
    "other", None, "high", r"\oldpage[II]{116}" + NL + NL + "des", r"\oldpage[II]{116}" + NL + "des",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 115 entry 'ne rencontrant aucun' "
    "(blank line before the marker).")
bold_ref(116, "proof of (6.2.4) (iii): 'au cas où Y=S (I, 3.3.11)'", "(I, 3.3.11)",
         "{I, 3.3.11}", r"{\textbf{I}, 3.3.11}")
bold_ref(116, "proof of (6.2.4) (iii): 'est de type fini (I, 6.3.4, (iii))'", "(I, 6.3.4, (iii))",
         "{I, 6.3.4, (iii)}", r"{\textbf{I}, 6.3.4, (iii)}")
bold_k(116, "proof of (6.2.4) (iii): 'f^{-1}(y)⊗_{k(y)}k(y')', subscript of ⊗",
       "⊗ with subscript 𝒌(y) (bold italic k, heavier than the y beside it)", r"\otimes_{k(y)}",
       r"\otimes_{k(y)}", r"\otimes_{\boldsymbol{k}(y)}",
       "Checked on a 4x crop. Same treatment as the subscript of ⊗ on p. 17.")
bold_k(116, "proof of (6.2.4) (iii): 'f^{-1}(y)⊗_{k(y)}k(y')', second factor",
       "𝒌(y')", "k(y')", r"k(y')$ (\hyperref[I.3.6.5-fr]", r"\boldsymbol{k}(y')$ (\hyperref[I.3.6.5-fr]")
bold_ref(116, "proof of (6.2.4) (iii): 's'identifie à f^{-1}(y)⊗k(y') (I, 3.6.5)'", "(I, 3.6.5)",
         "{I, 3.6.5}", r"{\textbf{I}, 3.6.5}")
bold_k(116, "proof of (6.2.4) (iii): 'est de rang fini sur k(y) par hypothèse'", "𝒌(y)", "$k(y)$",
       r"sur $k(y)$ par", r"sur $\boldsymbol{k}(y)$ par")
bold_k(116, "proof of (6.2.4) (iii): 'est de rang fini sur k(y'), donc discret'", "𝒌(y')", "$k(y')$",
       r"sur $k(y')$, donc", r"sur $\boldsymbol{k}(y')$, donc")
bold_ref(116, "proof of (6.2.4): 'par la méthode générale (I, 5.5.12)'", "(I, 5.5.12)",
         "{I, 5.5.12}", r"{\textbf{I}, 5.5.12}")
add(116, "proof of (6.2.4): 'il l'est a fortiori dans f^{-1}(f(x))'", "'a fortiori' italic", "upright",
    "italics", None, "high", "il l'est a fortiori dans", r"il l'est \emph{a fortiori} dans", "")
bold_ref(116, "proof of (6.2.4), end: 'résulte alors de (I, 6.3.6)'", "(I, 6.3.6)",
         "{I, 6.3.6}", r"{\textbf{I}, 6.3.6}")
add(116, "Proposition (6.2.5): 'Soient A un anneau local noethérien complet'",
    "'complet' roman (emphasis) in the italic statement", "italic like the rest of the statement",
    "italics", None, "high", r"noethérien complet, $X$ un", r"noethérien \emph{complet}, $X$ un",
    "Checked on a crop.")
add(116, "Proposition (6.2.5): 'X est Y-isomorphe à la somme (I, 3.1) de X''",
    "the reference (I, 3.1) upright", "italic (plain text '(I, 3.1)' inside the italic proposition environment)",
    "convention", 6, "high", "somme (I, 3.1) de", r"somme \textup{(I, 3.1)} de",
    "Checked on a crop. Apply BEFORE the bold-I entry for the same reference (next entry): after this edit "
    "'(I, 3.1)' still occurs once; in the other order this 'old' no longer matches.")
bold_ref(116, "Proposition (6.2.5): 'à la somme (I, 3.1)'", "(I, 3.1)", "(I, 3.1)", r"(\textbf{I}, 3.1)",
         "Plain text, no \\hyperref. Apply after the \\textup entry for the same reference.")
bold_ref(116, "proof of (6.2.5): 'Comme O_x est noethérien (I, 6.3.7)'", "(I, 6.3.7)",
         "{I, 6.3.7}", r"{\textbf{I}, 6.3.7}")
add(116, "proof of (6.2.5): 'l'hypothèse que A est complet entraîne'", "'complet' italic", "upright",
    "italics", None, "high", r"que $A$ est complet entraîne", r"que $A$ est \emph{complet} entraîne",
    "Checked on a crop.")
add(116, "proof of (6.2.5): 'que O_x est un A-module de type fini (0, 7.4.3)'", "'de type fini' italic", "upright",
    "italics", None, "high", r"$A$-module de type fini" + NL + r"(\hyperref[0.7.4.3-fr]",
    r"$A$-module \emph{de type fini}" + NL + r"(\hyperref[0.7.4.3-fr]",
    "Checked on a crop. Independent of the bold-0 edit of the same reference (adjacent, non-overlapping strings).")
bold_ref(116, "proof of (6.2.5): 'de type fini (0, 7.4.3)'", "(0, 7.4.3)", "{0, 7.4.3}", r"{\textbf{0}, 7.4.3}")
bold_ref(116, "proof of (6.2.5): 'le schéma local de X au point x (I, 2.4.1)'", "(I, 2.4.1)",
         "{I, 2.4.1}", r"{\textbf{I}, 2.4.1}")
add(116, "proof of (6.2.5): 'donc g(X') est fermé dans X (6.1.10)'", "'fermé' italic", "upright",
    "italics", None, "high", r"est fermé dans $X$", r"est \emph{fermé} dans $X$", "")
bold_ref(116, "proof of (6.2.5): 'en vertu de la définition de g et de (I, 6.5.4)'", "(I, 6.5.4)",
         "{I, 6.5.4}", r"{\textbf{I}, 6.5.4}")
add(116, "proof of (6.2.5), end: 'donc g(X') est aussi ouvert dans X'", "'ouvert' italic", "upright",
    "italics", None, "high", "est aussi ouvert dans", r"est aussi \emph{ouvert} dans", "")
add(116, "Corollaire (6.2.6): 'Soient A un anneau local noethérien complet, Y=Spec(A)'",
    "'complet' roman (emphasis) in the italic statement", "italic like the rest of the statement",
    "italics", None, "high", r"noethérien complet, $Y=", r"noethérien \emph{complet}, $Y=",
    "Checked on a crop.")
add(116, "Remarque (6.2.7): 'Au chapitre V, nous verrons'",
    "Au chapitre V", "Au chapitre V (same as the print)",
    "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading. EGA III, Errata et addenda: '(II, 6.2.7) Ligne 9 du bas de la p. 116, "
    "remplacer chap. V par chap. IV' (line 9 from the foot of p. 116 is this line).",
    corrected="Au chapitre IV")
add(116, "Remarque (6.2.7): 'si Y est localement noethérien'", "'localement noethérien' italic in the roman remark",
    "no emphasis", "italics", None, "high",
    r"est localement noethérien, un", r"est \emph{localement noethérien}, un",
    r"Judged with the remark body roman (document-wide remark item); the \emph comes out italic once the remark "
    r"environment is roman.")
add(116, "Remarque (6.2.7), end: 'est nécessairement quasi-affine.'", "'quasi-affine' italic in the roman remark",
    "no emphasis", "italics", None, "high",
    "nécessairement quasi-affine.", r"nécessairement \emph{quasi-affine}.",
    "As for 'localement noethérien'.")
label_up(116, "Proposition (6.3.1), item a)", "a)", r"\item[a)] Le sous-", r"\item[\textup{a)}] Le sous-")
add(116, "Proposition (6.3.1) a): 'pour n≥0 (0, 5.1.1) est de type fini'",
    "the reference (0, 5.1.1) upright", "italic (inside the italic proposition environment)",
    "convention", 6, "high",
    r"$n\geq 0$ (\hyperref[0.5.1.1-fr]{0, 5.1.1}) est",
    r"$n\geq 0$ \textup{(\hyperref[0.5.1.1-fr]{0, 5.1.1})} est",
    "Checked on a crop. Apply BEFORE the bold-0 entry for the same reference (next entry): after this edit "
    "'{0, 5.1.1}' still occurs once; in the other order this 'old' no longer matches.")
bold_ref(116, "Proposition (6.3.1) a)", "(0, 5.1.1)", "{0, 5.1.1}", r"{\textbf{0}, 5.1.1}",
         "Apply after the \\textup entry for the same reference.")
label_up(116, "Proposition (6.3.1), item b)", "b)", r"\item[b)] Il existe", r"\item[\textup{b)}] Il existe")
label_up(116, "Proposition (6.3.1), item c)", "c)", r"\item[c)] Pour tout", r"\item[\textup{c)}] Pour tout")

# ---------------------------------------------------------------- page 117
add(117, "proof of (6.3.1): 'il est clair que a) entraîne b).'", "a) and b) italic", "upright",
    "italics", None, "high", "il est clair que a) entraîne b).", r"il est clair que \emph{a)} entraîne \emph{b)}.", "")
add(117, "proof of (6.3.1): 'D'autre part, b) implique'", "b) italic", "upright",
    "italics", None, "high", "D'autre part, b)" + NL + "implique", r"D'autre part, \emph{b)}" + NL + "implique", "")
add(117, "proof of (6.3.1): 'tout élément de l'algèbre C_x, et en particulier f_x, est entier'",
    "comma after 𝒞_x", "no comma ('l'algèbre $\\mathcal{C}_x$ et en particulier')",
    "punctuation", None, "high", r"l'algèbre $\mathcal{C}_x$ et", r"l'algèbre $\mathcal{C}_x$, et",
    "Checked on a crop.")
add(117, "proof of (6.3.1): 'la section f^n|U+a_1.f^{n-1}|U+...+a_n'",
    "a_1.f^{n-1}: product dot on the baseline (like a full stop)", r"a_1\cdot f^{n-1} (centred dot)",
    "symbol", None, "high", r"a_1\cdot f^{n-1}", r"a_1.f^{n-1}",
    "Measured on the strip: the dot occupies the rows of the baseline of a_1 (rows 771-776), well below the "
    "bar of the + signs (rows 764-766). Same treatment as the baseline dots of p. 30.")
add(117, "proof of (6.3.1), end: 'on en conclut que c) entraîne a).'", "c) and a) italic", "upright",
    "italics", None, "high", "on en conclut que c) entraîne a).", r"on en conclut que \emph{c)} entraîne \emph{a)}.", "")
add(117, "Corollaire (6.3.2): 'Sous les hypothèses de (6.3.1)'",
    "the reference (6.3.1) upright", "italic (inside the italic corollary environment)",
    "convention", 6, "high",
    r"Sous les hypothèses de (\hyperref[II.6.3.1-fr]{6.3.1})",
    r"Sous les hypothèses de \textup{(\hyperref[II.6.3.1-fr]{6.3.1})}",
    "Checked on a crop.")
bold_ref(117, "(6.3.3): 'un g-morphisme (0, 4.4.1)'", "(0, 4.4.1)", "{0, 4.4.1}", r"{\textbf{0}, 4.4.1}")
add(117, "(6.3.3), display 'v=u^♯∘g^*(j) : g^*(B')→C''",
    "target 𝒞' (with a prime, like the ℬ' of the same display)", r"\to\mathcal{C} (no prime)",
    "misprint_in_print", None, "high",
    r"(j):g^*(\mathcal{B}')\to\mathcal{C}", r"(j):g^*(\mathcal{B}')\to\mathcal{C}'",
    "Checked on a 2.5x crop: a clear prime after the script C. 𝒞' is not defined in (6.3.3): u^♯ goes from "
    "g^*(𝒟) to 𝒞, so v=u^♯∘g^*(j) goes from g^*(ℬ') to 𝒞. The TeX silently corrects the misprint; the fix "
    "restores the printed reading. Not in the EGA III list of errata to EGA II.",
    corrected=r"v=u^\sharp\circ g^*(j):g^*(\mathcal{B}')\to\mathcal{C}")
add(117, "end of p. 117 / top of p. 118, proof of (6.3.4): '... A étant une | B-algèbre ; soit B''",
    "one sentence across the page break (p. 118 starts flush left with 'B-algèbre')",
    r"blank line before \oldpage[II]{118} (paragraph break)",
    "other", None, "high", "$A$ étant une" + NL + NL, "$A$ étant une" + NL,
    r"Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line is the last line "
    r"of page 117's segment. Apply together with the p. 118 entry that removes the blank line after the marker. "
    r"\oldpage ends with \ignorespaces, so joining the lines leaves a single space.")

# ---------------------------------------------------------------- page 118
add(118, "top of p. 118: 'B-algèbre ; soit B' la fermeture intégrale' (continues the proof of (6.3.4))",
    "continuation of the sentence of p. 117, flush left",
    r"blank line after \oldpage[II]{118} (paragraph break)",
    "other", None, "high", r"\oldpage[II]{118}" + NL + NL + "$B$-algèbre", r"\oldpage[II]{118}" + NL + "$B$-algèbre",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 117 entry '$A$ étant une' "
    "(blank line before the marker).")
add(118, "proof of (6.3.4): 'commutent ([13], t. I, p. 261 et 257).'",
    "([13], t. I, p. 261 et 257): the bracket closes after the number, the volume and pages follow outside it",
    r"\cite[t.~I, p.~261 et 257]{I-13}, which prints [13, t. I, p. 261 et 257]",
    "punctuation", None, "high",
    r"(\cite[t.~I, p.~261 et 257]{I-13})", r"(\cite{I-13}, t.~I, p.~261 et 257)",
    "Same form of fix as EGA I p. 148. \\bibitem{I-13} is the 13th item of bib-fr.tex, so \\cite{I-13} prints [13].")
add(118, "(6.3.6): 'relativement à une R(X)-Algèbre A quasi-cohérente'",
    "'Algèbre' (after ℛ(X)-) italic", "upright",
    "italics", None, "high",
    r"$\mathcal{R}(X)$-Algèbre $\mathcal{A}$ quasi-cohérente",
    r"$\mathcal{R}(X)$-\emph{Algèbre} $\mathcal{A}$ quasi-cohérente",
    "Checked on a crop; the second 'R(X)-Algèbre' of the sentence is roman, as in the TeX.")
bold_ref(118, "(6.3.6): 'On sait (I, 7.3.5) que A est composée directe'", "(I, 7.3.5)",
         "{I, 7.3.5}", r"{\textbf{I}, 7.3.5}")
bold_k(118, "(6.3.6), second paragraph: 'une algèbre sur le corps k(ξ_i)'", "𝒌(ξ_i)", "$k(\\xi_i)$",
       r"\emph{corps} $k(\xi_i)$", r"\emph{corps} $\boldsymbol{k}(\xi_i)$", "Checked on a crop.")

# ---------------------------------------------------------------- page 119
bold_k(119, "Proposition (6.3.7): 'la fermeture algébrique K'_ij de k(ξ_i) dans K_ij'", "𝒌(ξ_i)", "$k(\\xi_i)$",
       r"de $k(\xi_i)$ dans", r"de $\boldsymbol{k}(\xi_i)$ dans")
add(119, "proof of (6.3.7): 'l'anneau intègre B_U=Γ(Y, O_X) (6.3.4)'",
    "B_U=Γ(Y, 𝒪_X)", r"B_U=\Gamma(U,\mathcal{O}_X)",
    "misprint_in_print", None, "high",
    r"$B_U=\Gamma(U,\mathcal{O}_X)$", r"$B_U=\Gamma(Y,\mathcal{O}_X)$",
    "Checked on a 2.5x crop: a clear Y. No Y occurs in (6.3.6)-(6.3.7); U is the affine open of X of the same "
    "sentence and B_U its ring of sections. The TeX silently corrects the misprint; the fix restores the printed "
    "reading. Not in the EGA III list of errata to EGA II.",
    corrected=r"B_U=\Gamma(U,\mathcal{O}_X)")
add(119, "proof of (6.3.7): 'est par définition un schéma intègre et normal'",
    "'intègre' and 'normal' italic, 'et' roman", r"\emph{intègre et normal} ('et' italic too)",
    "italics", None, "high", r"\emph{intègre et normal}", r"\emph{intègre} et \emph{normal}", "Checked on a crop.")
bold_ref(119, "proof of (6.3.7): '((0, 4.1.4) et (I, 5.1.4))'", "(0, 4.1.4)", "{0, 4.1.4}", r"{\textbf{0}, 4.1.4}")
bold_ref(119, "proof of (6.3.7): '((0, 4.1.4) et (I, 5.1.4))'", "(I, 5.1.4)", "{I, 5.1.4}", r"{\textbf{I}, 5.1.4}")
add(119, "proof of (6.3.7): 'au-dessus de l'idéal premier (0) de B_U ([13], t. I, p. 259)'",
    "([13], t. I, p. 259): the bracket closes after the number", r"\cite[t.~I, p.~259]{I-13}, which prints [13, t. I, p. 259]",
    "punctuation", None, "high", r"(\cite[t.~I, p.~259]{I-13})", r"(\cite{I-13}, t.~I, p.~259)",
    "As on p. 118.")
bold_k(119, "proof of (6.3.7): 'et k(ξ') est le corps des fractions K' de B'_U'", "𝒌(ξ')", "$k(\\xi')$",
       r"et $k(\xi')$ est", r"et $\boldsymbol{k}(\xi')$ est")
bold_k(119, "proof of (6.3.7): 'la fermeture algébrique de k(ξ) dans K'", "𝒌(ξ)", "$k(\\xi)$",
       r"de $k(\xi)$ dans $K$", r"de $\boldsymbol{k}(\xi)$ dans $K$")
bold_ref(119, "proof of (6.3.7), end: 'et on conclut par (0, 2.1.4)'", "(0, 2.1.4)", "{0, 2.1.4}", r"{\textbf{0}, 2.1.4}")
bold_k(119, "Corollaire (6.3.8): 'et on a k(ξ'_i)=k(ξ_i)', left side", "𝒌(ξ'_i)", "$k(\\xi'_i)",
       r"$k(\xi'_i)", r"$\boldsymbol{k}(\xi'_i)")
bold_k(119, "Corollaire (6.3.8): 'et on a k(ξ'_i)=k(ξ_i)', right side", "𝒌(ξ_i)", "k(\\xi_i)$",
       r"=k(\xi_i)$", r"=\boldsymbol{k}(\xi_i)$",
       "Bold italic k in the print, plain k in the TeX. Either order with the left-side entry works (both keep the '=').")
add(119, "after (6.3.8): 'il faut et il suffit que X soit normal.'", "'normal' italic", "upright",
    "italics", None, "high", r"que $X$ soit normal.", r"que $X$ soit \emph{normal}.", "")
add(119, "end of p. 119 / top of p. 120, (6.3.9): '... s'identifie canoniquement à la fermeture algé-|brique L' (resp. K')'",
    "one sentence across the page break (the word algé-brique is divided between the pages)",
    r"blank line before \oldpage[II]{120} (paragraph break)",
    "other", None, "high", "la fermeture algébrique" + NL + NL, "la fermeture algébrique" + NL,
    r"Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line is the last line "
    r"of page 119's segment; apply together with the p. 120 entry that removes the blank line after "
    r"\oldpage[II]{120} (old '\oldpage[II]{120}\n\n$L'$', new '\oldpage[II]{120}\n$L'$'; outside pp. 115-119). "
    r"The divided word is kept whole before the marker (hyphenation ignored).")

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print(len(F), "findings written")
