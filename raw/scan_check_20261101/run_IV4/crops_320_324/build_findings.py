"""Build findings_320_324.json and verify every fix's "old" string.

Each "old" must occur exactly once in its page_NNN.tex (LF line ends) at the
moment it is applied; fixes of one page are applied in list order, so a fix
whose "old" comes from the text after an earlier entry is checked after that
entry. The same check is made against the current source segment of the page.
"""
import json
import re
import sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions"
       r"\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21c-fr.tex")
OUT = RUN + r"\findings_320_324.json"


def F(page, where, scan, tex, kind, fix, note="", convention=None,
      confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


C7 = "long dash for set difference (X—Y)"
LBL = "the label printed italic, letter and parenthesis"
findings = [
    # ---------------------------------------------------------------- p. 320
    F(320, "l. 1: 'à V — (V ∩ {y}‾) est inversible'", C7, "minus sign",
      "convention", fx(r"à $V-(V\cap", r"à $V\setmin(V\cap"), convention=7),
    F(320, "l. 8: 'à W — (W ∩ {y}‾) soient'", C7, "minus sign",
      "convention", fx(r"$W-(W\cap", r"$W\setmin(W\cap"), convention=7),
    F(320, "l. 9: 'soient égales. Si l'on pose alors'",
      "'égales' italic (page_320_s1.png)", "upright", "italics",
      fx("soient égales.", r"soient \emph{égales}.")),
    F(320, "l. 11: 'et de (21.13.2, b)) que j_*(L)|V_1'",
      LBL + " (grid crop crops_320_324/g320_b_paren.png: the first ')' slanted, the second upright)",
      "'$b$)': italic b, upright parenthesis", "italics",
      fx(r"(21.13.2, $b$))", r"(21.13.2, \emph{b)})"), "GLOBAL_ISSUES 88."),
    F(320, "Corollaire (21.13.11), l. 2: 'U = X — Y. Supposons'", C7, "minus sign",
      "convention", fx(r"$U=X-Y$. Supposons", r"$U=X\setmin Y$. Supposons"), convention=7),
    F(320, "Corollaire (21.13.11), l. 3: 'en d'autres termes (21.13.10), pour tout'",
      "'(21.13.10)' upright, parentheses upright (crop p320_cor11_line3.png)",
      "italic (corollary environment)", "convention",
      fx("en d'autres termes (21.13.10), pour", r"en d'autres termes \textup{(21.13.10)}, pour"),
      convention=6),
    F(320, "Corollaire (21.13.11), end: '(autrement dit, O_X,x est en fait factoriel pour tout x ∈ X).'",
      "the parenthesis roman, only 'tout' italic (crops p320_cor11_line4.png, p320_cor11_21310.png)",
      "all italic (corollary environment)", "convention",
      fx(r"(autrement dit, $\mathcal O_{X,x}$ est en fait factoriel pour tout $x\in X$).",
         r"\textup{(autrement dit, $\mathcal O_{X,x}$ est en fait factoriel pour \emph{tout} $x\in X$)}."),
      "Inside \\textup the \\emph gives the print's italic 'tout'.", convention=6),
    F(320, "proof of (21.13.11), l. 3: 'U_y = T_y — {y}'", C7, "minus sign",
      "convention", fx(r"$U_y=T_y-\{y\}$, l'hypothèse", r"$U_y=T_y\setmin\{y\}$, l'hypothèse"), convention=7),
    F(320, "proof of (21.13.12), l. 4: 'U = X — {a}'", C7, "minus sign",
      "convention", fx(r"$U=X-\{a\}$, $U'=f^{-1}(U)$", r"$U=X\setmin\{a\}$, $U'=f^{-1}(U)$"), convention=7),
    # ---------------------------------------------------------------- p. 321
    F(321, "Remarque (21.13.13), l. 6: 'la catégorie des O_X-Modules inversibles et celle des'",
      "'Modules inversibles' italic (crop p321_Modinv.png)", "upright", "italics",
      fx(r"$\mathcal O_X$-Modules inversibles et celle",
         r"$\mathcal O_X$-\emph{Modules inversibles} et celle"),
      "Remark body judged as roman (document-wide remark item)."),
    F(321, "Remarque (21.13.13): 'le foncteur L ⇝ L^* est une équivalence'",
      "wavy arrow (crop p321_leadsto1.png)", "\\mapsto", "symbol",
      fx(r"$\mathscr L\mapsto\mathscr L^*$", r"$\mathscr L\leadsto\mathscr L^*$")),
    F(321, "Remarque (21.13.13): 'est immédiate. Cela étant, considérons de façon générale'",
      "no paragraph break: 'Cela étant' follows on the same line (page_321_s2.png, l. 4)",
      "blank line: new paragraph", "extra",
      fx("est immédiate.\n\nCela étant", "est immédiate.\nCela étant")),
    F(321, "Remarque (21.13.13): 'posons U = X — Y, et soit i'", C7, "minus sign",
      "convention", fx(r"posons $U=X-Y$, et", r"posons $U=X\setmin Y$, et"), convention=7),
    F(321, "Remarque (21.13.13): 'est i-pur pour G si'",
      "only 'i-pur' italic; 'pour' roman (crop p321_ipur.png)",
      "\\emph{$i$-pur pour $\\mathscr G$}", "italics",
      fx(r"\emph{$i$-pur pour $\mathscr G$}", r"\emph{$i$-pur} pour $\mathscr G$")),
    F(321, "Remarque (21.13.13): 'le foncteur restriction P ⇝ P|(U ∩ V)'",
      "wavy arrow (crop p321_leadsto2.png)", "\\mapsto", "symbol",
      fx(r"$\mathscr P\mapsto\mathscr P|(U\cap V)$", r"$\mathscr P\leadsto\mathscr P|(U\cap V)$")),
    F(321, "Remarque (21.13.13): 'de la catégorie des faisceaux principaux homogènes'",
      "'des faisceaux' (crop p321_catdes.png)", "'de faisceaux'", "word",
      fx("de la catégorie de faisceaux", "de la catégorie des faisceaux")),
    F(321, "Remarque (21.13.13), end: 'les faisceaux de cohomologie H^i_Y(G) définis au chap. III'",
      "superscript i (crop p321_HiY.png); the next formula has H^p_Y(G) = 0 pour p ⩽ i",
      "superscript p", "formula",
      fx(r"cohomologie $\mathscr H_Y^p(\mathscr G)$", r"cohomologie $\mathscr H_Y^i(\mathscr G)$"),
      "Not a misprint (i is the generic degree of the sheaves introduced; the condition then uses p ⩽ i)."),
    F(321, "Proposition (21.13.14), l. 1: 'localement noethérien normal,'",
      "'normal' italic like the rest of the statement (crop p321_normal.png)",
      "\\emph{normal}: upright inside the italic proposition", "italics",
      fx("noethérien \\emph{normal},\n$(U_\\lambda)", "noethérien normal,\n$(U_\\lambda)")),
    F(321, "Proposition (21.13.14) a): 'soit localement principal (21.6.7), est'",
      "'(21.6.7)' upright, parentheses upright (crop p321_2167.png)",
      "italic (proposition environment)", "convention",
      fx("localement principal (21.6.7), est", r"localement principal \textup{(21.6.7)}, est"),
      convention=6),
    F(321, "end of the page: Proposition (21.13.14) continues on p. 322 with a third condition b')",
      "the print lists a), b) on p. 321 and b') at the top of p. 322, all three in the statement "
      "(upright labels, italic text, page_322_s1.png); the proof then begins 'La propriété a) peut encore'",
      "the enumerate and the proposition end after b), and \\begin{proof} opens on p. 321", "other",
      fx("  $\\mathcal O_{X,x}$ est parafactoriel.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}\n",
         "  $\\mathcal O_{X,x}$ est parafactoriel.\n"),
      "Part 1 of 3 (with the first two p. 322 entries): b') becomes the third item of the proposition. "
      "Apply the three together."),
    # ---------------------------------------------------------------- p. 322
    F(322, "top of the page: 'b') Pour toute partie fermée Y de X ...'",
      "b') is the third condition of Proposition (21.13.14): label upright, text italic (crops "
      "g322_bprime_label.png, p322_bprime.png); the print has no sentence 'La condition b) peut "
      "encore s'exprimer de la façon suivante :' (p. 321 ends with item b), p. 322 begins with b'))",
      "an added sentence 'La condition $b)$ peut encore s'exprimer de la façon suivante :' and b') "
      "set as an \\emph paragraph inside the proof", "extra",
      fx("\\oldpage[IV-4]{322}\nLa condition $b)$ peut encore s'exprimer de la façon suivante :\n\n"
         "\\emph{$b')$ Pour toute partie fermée",
         "\\oldpage[IV-4]{322}\n  \\item[\\textup{b$'$)}] Pour toute partie fermée"),
      "Part 2 of 3 (see the last p. 321 entry and the entry after next). The marker stays at the "
      "start of b'), now between the items (as at the p. 323 marker). Hand-set label upright with "
      "\\textup (GLOBAL_ISSUES 88)."),
    F(322, "b'), l. 2: 'Y ⊂ X — U_λ, le couple'", C7, "minus sign",
      "convention", fx(r"$Y\subset X-U_\lambda$", r"$Y\subset X\setmin U_\lambda$"), convention=7),
    F(322, "end of b'): 'le couple (X, Y) est parafactoriel.' followed by the proof",
      "b') ends the statement; the proof begins 'La propriété a) peut encore s'exprimer'",
      "closing brace of the \\emph paragraph", "other",
      fx("$(X,Y)$ est parafactoriel.}\n\n",
         "$(X,Y)$ est parafactoriel.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}\n"),
      "Part 3 of 3: closes the list and the proposition after b') and opens the proof "
      "(apply with the two entries above)."),
    F(322, "proof of (21.13.14), l. 1: 'La propriété a) peut encore'", LBL + " (grid crop g322_a_label.png)",
      "'$a)$'", "italics", fx("La propriété $a)$ peut", r"La propriété \emph{a)} peut"),
      "GLOBAL_ISSUES 88."),
    F(322, "l. 2: 'contenu dans l'un des X — U_λ, alors Z'", C7, "minus sign",
      "convention", fx("l'un des\n$X-U_\\lambda$, alors", "l'un des\n$X\\setmin U_\\lambda$, alors"),
      convention=7),
    F(322, "l. 6: 'La propriété a) est donc équivalente'", LBL, "'$a)$'", "italics",
      fx("La propriété $a)$ est donc", r"La propriété \emph{a)} est donc"), "GLOBAL_ISSUES 88."),
    F(322, "condition a'): 'a') S'il existe un ensemble fermé Y ...'",
      "italic label a'), the condition in ROMAN type (grid crop g322_aprime.png, p322_ZXY.png)",
      "the whole paragraph in \\emph (italic), label '$a')$'", "italics",
      fx("\\emph{$a')$ S'il existe", "\\emph{a$'$)} S'il existe"),
      "Part 1 of 2: apply together with the 'alors $Z$ est localement principal.}' entry below "
      "(removes the closing brace)."),
    F(322, "a'), l. 1: 'contenu dans un des X — U_λ, tel que'", C7, "minus sign",
      "convention", fx(r"un des $X-U_\lambda$, tel", r"un des $X\setmin U_\lambda$, tel"), convention=7),
    F(322, "a'), l. 2: 'et que Z|X — Y soit localement principal'",
      "Z|X—Y without parentheses (crop p322_ZXY.png)", "Z|(X-Y)", "formula",
      fx(r"$Z|(X-Y)$", r"$Z|X-Y$"),
      "Apply before the next entry (same spot)."),
    F(322, "a'), l. 2: 'Z|X — Y': the dash", C7, "minus sign", "convention",
      fx(r"$Z|X-Y$ soit", r"$Z|X\setmin Y$ soit"),
      "Apply after the previous entry: its 'old' is the text after that entry.", convention=7),
    F(322, "end of a'): 'alors Z est localement principal.'",
      "roman (see the a') entry above)", "closing brace of the \\emph paragraph", "italics",
      fx("alors $Z$ est localement principal.}", "alors $Z$ est localement principal."),
      "Part 2 of 2 of the a') entry above."),
    F(322, "'Notons d'autre part que b) implique b') en vertu de (21.13.10)'",
      LBL + " (crop p322_bimpl.png)", "'$b)$', '$b')$'", "italics",
      fx("que $b)$ implique $b')$ en vertu", "que \\emph{b)} implique \\emph{b$'$)} en vertu"),
      "GLOBAL_ISSUES 88."),
    F(322, "'inversement, si b') est vérifiée'", LBL, "'$b')$'", "italics",
      fx("si\n$b')$ est vérifiée", "si\n\\emph{b$'$)} est vérifiée"), "GLOBAL_ISSUES 88."),
    F(322, "'alors Y = {x}‾ est contenue dans X — U_λ'",
      "bar over {x}: the closure (crop p322_Yx.png)", "$Y=\\{x\\}$ without the bar", "formula",
      fx(r"$Y=\{x\}$ est contenue", r"$Y=\overline{\{x\}}$ est contenue")),
    F(322, "'est contenue dans X — U_λ et on a'", C7, "minus sign", "convention",
      fx(r"$X-U_\lambda$ et on a", r"$X\setmin U_\lambda$ et on a"), convention=7),
    F(322, "'ce qui prouve l'équivalence de b) et b').'", LBL, "'$b)$', '$b')$'", "italics",
      fx("$b)$ et $b')$. On est", "\\emph{b)} et \\emph{b$'$)}. On est"), "GLOBAL_ISSUES 88."),
    F(322, "'à prouver l'équivalence de a') et de b').'", LBL, "'$a')$', '$b')$'", "italics",
      fx("l'équivalence de $a')$ et de $b')$.", "l'équivalence de \\emph{a$'$)} et de \\emph{b$'$)}."),
      "GLOBAL_ISSUES 88."),
    F(322, "'si l'on pose U = X — Y, l'homomorphisme'", C7, "minus sign", "convention",
      fx(r"si l'on pose $U=X-Y$, l'homomorphisme", r"si l'on pose $U=X\setmin Y$, l'homomorphisme"),
      convention=7),
    F(322, "'comme les conditions a') et b') sont locales'", LBL, "'$a')$', '$b')$'", "italics",
      fx("$a')$ et $b')$ sont locales", "\\emph{a$'$)} et \\emph{b$'$)} sont locales"),
      "GLOBAL_ISSUES 88."),
    F(322, "'lorsque X est noethérien et normal'",
      "'noethérien' italic (crop p322_noeth.png; the letter shapes are italic, not end-of-line weight)",
      "upright", "italics",
      fx("est noethérien et normal", r"est \emph{noethérien} et normal")),
    F(322, "condition a''): 'a'') Pour tout cycle 1-codimensionnel Z sur X, ...'",
      "italic label a''), the condition in ROMAN type (crops g322_asecond.png, p322_asecond_line.png)",
      "the whole paragraph in \\emph (italic), label '$a'')$'", "italics",
      fx("\\emph{$a'')$ Pour tout cycle", "\\emph{a$''$)} Pour tout cycle"),
      "Part 1 of 2: apply together with the 'lui-même est localement principal.}' entry below."),
    F(322, "a''), l. 1: '(où U = X — Y)'", C7, "minus sign", "convention",
      fx(r"(où $U=X-Y$)", r"(où $U=X\setmin Y$)"), convention=7),
    F(322, "end of a''): 'Z lui-même est localement principal.'",
      "roman (see the a'') entry above)", "closing brace of the \\emph paragraph", "italics",
      fx("lui-même est localement\nprincipal.}", "lui-même est localement\nprincipal."),
      "Part 2 of 2 of the a'') entry above."),
    F(322, "condition b''): 'b'') L'homomorphisme canonique Pic(X) → Pic(U) est surjectif.'",
      "italic label b''), the condition in ROMAN type (page_322_s3.png, l. 1)",
      "the whole paragraph in \\emph (italic), label '$b'')$'", "italics",
      fx("\\emph{$b'')$ L'homomorphisme canonique\n$\\operatorname{Pic}(X)\\to\\operatorname{Pic}(U)$ est surjectif.}",
         "\\emph{b$''$)} L'homomorphisme canonique\n$\\operatorname{Pic}(X)\\to\\operatorname{Pic}(U)$ est surjectif.")),
    F(322, "'Prouvons d'abord que a'') entraîne b'');'", LBL, "'$a'')$', '$b'')$'", "italics",
      fx("que $a'')$ entraîne $b'')$;", "que \\emph{a$''$)} entraîne \\emph{b$''$)};"),
      "GLOBAL_ISSUES 88."),
    F(322, "'l'homomorphisme de restriction 𝔷^1(X) → 𝔷^1(U) est bijectif'",
      "Fraktur Z, the group of cycles 𝔷^1 as elsewhere in § 21 (crop p322_frakZ.png)",
      "script Z (\\mathscr Z), the sheaf letter", "symbol",
      fx(r"restriction $\mathscr Z^1(X)\to\mathscr Z^1(U)$ est bijectif",
         r"restriction $\mathfrak{Z}^1(X)\to\mathfrak{Z}^1(U)$ est bijectif"),
      "ega4-21b writes these groups \\mathfrak{Z}^1(X), \\mathfrak{Z}^1_\\mathrm{princ}(X); the script 𝒵 is the sheaf 𝒵^1_X."),
    F(322, "'il en est de même de Z en vertu de a'');'", LBL, "'$a'')$'", "italics",
      fx("en vertu de $a'')$;", "en vertu de \\emph{a$''$)};"), "GLOBAL_ISSUES 88."),
    F(322, "'Inversement, prouvons que b'') entraîne a'').'", LBL, "'$b'')$', '$a'')$'", "italics",
      fx("que $b'')$ entraîne $a'')$.", "que \\emph{b$''$)} entraîne \\emph{a$''$)}."),
      "GLOBAL_ISSUES 88."),
    F(322, "last paragraph: 'l'image de 𝔷^1_princ(X) par l'isomorphisme 𝔷^1(X) → 𝔷^1(U) est 𝔷^1_princ(U)'",
      "four Fraktur Z (crop p322_princ.png, page_322_s4.png)", "four \\mathscr Z", "symbol",
      fx("$\\mathscr Z^1_{\\mathrm{princ}}(X)$ par l'isomorphisme\n$\\mathscr Z^1(X)\\to\\mathscr Z^1(U)$ est $\\mathscr Z^1_{\\mathrm{princ}}(U)$",
         "$\\mathfrak{Z}^1_{\\mathrm{princ}}(X)$ par l'isomorphisme\n$\\mathfrak{Z}^1(X)\\to\\mathfrak{Z}^1(U)$ est $\\mathfrak{Z}^1_{\\mathrm{princ}}(U)$"),
      "As in the entry above."),
    # ---------------------------------------------------------------- p. 323
    F(323, "Corollaire (21.13.15) b): '(autrement dit, tel que {x}‾ ∩ S = ∅)'",
      "both parentheses upright (grid crops g323_open.png, g323_close.png: top and bottom ends "
      "vertically aligned; compare the slanted label parenthesis in g320_b_paren.png)",
      "italic (corollary environment)", "convention",
      fx("(autrement\n  dit, tel que $\\overline{\\{x\\}}\\cap S=\\varnothing$)",
         "\\textup{(}autrement\n  dit, tel que $\\overline{\\{x\\}}\\cap S=\\varnothing$\\textup{)}"),
      "Checked by the print (GLOBAL_ISSUES 96/101): here the parentheses are upright, the words italic.",
      convention=6),
    F(323, "proof of (21.13.15): '(les propriétés a) et b) étant locales sur X)'", LBL,
      "'$a)$', '$b)$'", "italics",
      fx("(les propriétés $a)$ et $b)$ étant", r"(les propriétés \emph{a)} et \emph{b)} étant"),
      "GLOBAL_ISSUES 88."),
    F(323, "proof of (21.13.15): 'la condition a) de (21.13.15) équivaut'", LBL, "'$a)$'", "italics",
      fx("la condition $a)$ de (21.13.15)", r"la condition \emph{a)} de (21.13.15)"), "GLOBAL_ISSUES 88."),
    F(323, "proof of (21.13.15): 'à la condition a) de (21.13.14) appliquée'", LBL, "'$a)$'", "italics",
      fx("la condition $a)$ de (21.13.14) appliquée", r"la condition \emph{a)} de (21.13.14) appliquée"),
      "GLOBAL_ISSUES 88."),
    F(323, "proof of (21.13.15): 'de l'équivalence de a) et b) dans (21.13.14)'", LBL,
      "'$a)$', '$b)$'", "italics",
      fx("l'équivalence de $a)$ et $b)$ dans", r"l'équivalence de \emph{a)} et \emph{b)} dans"),
      "GLOBAL_ISSUES 88."),
    F(323, "Remarque (21.13.16), l. 2: 'Alors la condition a) de (21.13.14)'", LBL, "'$a)$'", "italics",
      fx("Alors la condition $a)$ de (21.13.14)", r"Alors la condition \emph{a)} de (21.13.14)"),
      "GLOBAL_ISSUES 88 (remark body judged as roman)."),
    F(323, "Remarque (21.13.16), c): 'contenu dans un des ensembles X — U_λ'", C7, "minus sign",
      "convention", fx(r"un des ensembles $X-U_\lambda$ est", r"un des ensembles $X\setmin U_\lambda$ est"),
      convention=7),
    F(323, "Remarque (21.13.16): 'Il est clair que a) entraîne c), car'", LBL, "'$a)$', '$c)$'", "italics",
      fx("que $a)$ entraîne $c)$, car", r"que \emph{a)} entraîne \emph{c)}, car"), "GLOBAL_ISSUES 88."),
    F(323, "Remarque (21.13.16): 'a son support dans X — U_λ, Z|U_λ = 0'", C7, "minus sign",
      "convention", fx(r"son support dans $X-U_\lambda$,", r"son support dans $X\setmin U_\lambda$,"),
      convention=7),
    F(323, "Remarque (21.13.16): 'Inversement c) entraîne a) :'", LBL, "'$c)$', '$a)$'", "italics",
      fx("Inversement $c)$ entraîne $a)$ :", r"Inversement \emph{c)} entraîne \emph{a)} :"),
      "GLOBAL_ISSUES 88."),
    F(323, "Remarque (21.13.16): 'où D_λ est un diviseur sur U_λ (21.6.10, (i))'",
      "'(21.6.10, (i))' (crop p323_21610.png)", "'(21.6.10, (ii))'", "number",
      fx("(21.6.10, (ii))", "(21.6.10, (i))"),
      "The TeX's (ii) (Pic → Cl bijective when X is locally factorial) is neither the print nor the "
      "needed result; see the misprint entry that follows."),
    F(323, "Remarque (21.13.16): '(21.6.10, (i))' as a reference for Z|U_λ = cyc(D_λ)",
      "(21.6.10, (i))", "(21.6.10, (i)) after the entry above", "misprint_in_print", None,
      "The statement used (a locally principal cycle on the normal U_λ is cyc of a divisor) is "
      "(21.6.9, (i)): 'cyc : Div(X) → 𝔷^1(X) est injectif et son image est formée des cycles "
      "localement principaux'; (21.6.10, (i)) is the injectivity of Pic(X) → 𝔆𝔩(X). With the "
      "entry above the TeX keeps the printed reading (fix null). Medium: a cross-reference slip "
      "inferred from the content of (21.6.9) and (21.6.10); no erratum seen.",
      confidence="medium", corrected="(21.6.9, (i))"),
    F(323, "Remarque (21.13.16): 'on voit donc que Z'' = Z — Z' a son support'",
      "long dash used as the minus sign (crop p323_ZZprime.png)", "minus sign", "convention",
      fx(r"$Z''=Z-Z'$", r"$Z''=Z\setmin Z'$"), "GLOBAL_ISSUES 23 (long dash for subtraction).",
      convention=7),
    F(323, "Remarque (21.13.16): 'a son support dans X — U_μ;'", C7, "minus sign", "convention",
      fx(r"dans $X-U_\mu$;", r"dans $X\setmin U_\mu$;"), convention=7),
    F(323, "Remarque (21.13.16): 'la famille des voisinages ouverts d'un point z ∈ X'",
      "'un point' italic (crop p323_unpoint.png)", "only 'point' italic", "italics",
      fx(r"d'un \emph{point} $z\in X$", r"d'\emph{un point} $z\in X$")),
    F(323, "Remarque (21.13.16): 'tel que L_λ|U_μ soit isomorphe à O_U_λ.'",
      "𝒪 with subscript U_λ (8x crop p323_OUl_zoom.png)", "𝒪_{U_μ}: silent correction",
      "misprint_in_print",
      fx(r"isomorphe à $\mathcal O_{U_\mu}$", r"isomorphe à $\mathcal O_{U_\lambda}$"),
      "L_λ|U_μ is a sheaf on U_μ, so the print's 𝒪_{U_λ} is a slip for 𝒪_{U_μ}. The TeX silently "
      "corrects; the fix restores the printed reading.",
      corrected=r"isomorphe à $\mathcal O_{U_\mu}$"),
    F(323, "Remarque (21.13.16): 'si S = {z}, les conditions a) et b) équivalent'", LBL,
      "'$a)$', '$b)$'", "italics",
      fx("les conditions $a)$ et $b)$ équivalent", r"les conditions \emph{a)} et \emph{b)} équivalent"),
      "GLOBAL_ISSUES 88."),
    F(323, "Remarque (21.13.16): 'Si de plus Pic(X) = 0, on en conclura' after the second c)",
      "indented new paragraph, at the indent of 'La condition' and 'c)' (page_323_s3.png)",
      "follows \\end{enumerate} without a blank line: no indent", "other",
      fx("\\end{enumerate}\nSi de plus", "\\end{enumerate}\n\nSi de plus"),
      "GLOBAL_ISSUES 80 pattern."),
    F(323, "Remarque (21.13.16), end: 'dont le support ne contient pas z est principal.'",
      "'principal' italic (crop p323_principal.png)", "upright", "italics",
      fx("ne contient pas $z$ est principal.", r"ne contient pas $z$ est \emph{principal}.")),
    F(323, "heading 21.14: '21.14. Le théorème de Ramanujam-Samuel.'",
      "hyphen in 'Ramanujam-Samuel' and a final full stop (crop p323_heading.png)",
      "en dash '--', no full stop", "punctuation",
      fx(r"\subsection{Le théorème de Ramanujam--Samuel}", r"\subsection{Le théorème de Ramanujam-Samuel.}"),
      "GLOBAL_ISSUES 43/58 for the full stop; the print's name has a hyphen, as in the theorem title."),
    F(323, "Théorème (21.14.1), title: '(Ramanujam-Samuel)'",
      "hyphen (crop p323_RS_title.png)", "en dash '--'", "punctuation",
      fx(r"\textup{(Ramanujam--Samuel)}", r"\textup{(Ramanujam-Samuel)}"),
      "The heading format (title in parentheses after the number) is the document-wide item; only the dash here."),
    F(323, "Théorème (21.14.1), l. 3: 'tel que dim(B) > dim(A)'",
      "strict '>' (crop p323_dimB.png)", "\\geq", "symbol",
      fx(r"\dim(B)\geq\dim(A)", r"\dim(B)>\dim(A)"),
      "Not a misprint: with dim(B) = dim(A) the statement is trivial (𝔭 = 𝔪B is then the closed point), "
      "so the print's strict hypothesis is sound; the TeX changed it."),
    F(323, "Théorème (21.14.1), l. 4: '(pour les topologies préadiques (0, 19.3.1))'",
      "outer parentheses upright (grid crops g323_pour_open.png, g323_pour_close.png)",
      "italic (theorem environment)", "convention",
      fx("(pour les topologies préadiques\n$(\\mathbf 0, 19.3.1)$)",
         "\\textup{(}pour les topologies préadiques\n$(\\mathbf 0, 19.3.1)$\\textup{)}"),
      "Checked by the print (GLOBAL_ISSUES 96/101).", convention=6),
    F(323, "page break 323/324: printed p. 323 ends '... B/𝔪B est une k-algèbre formellement lisse (pour'",
      "page_323_s4.png ends with 'formellement lisse (pour' (page number 323 below); page_324_s1.png "
      "begins 'sa topologie préadique) (0, 19.3.5), donc régulière'",
      "\\oldpage[IV-4]{324} stands after '(pour sa topologie préadique) $(\\mathbf 0, 19.3.5)$,', "
      "half a printed line too late", "marker",
      fx("formellement lisse (pour sa topologie préadique)",
         "formellement lisse (pour\n\\oldpage[IV-4]{324}\nsa topologie préadique)"),
      "Marker move, part 2 of 2: new position (mid-sentence, no blank lines). Apply together with the "
      "first p. 324 entry, which removes the old marker. The moved words have no other differences."),
    # ---------------------------------------------------------------- p. 324
    F(324, "page break 323/324: old position of \\oldpage[IV-4]{324}",
      "p. 324 begins 'sa topologie préadique) (0, 19.3.5), donc régulière'",
      "marker before 'donc régulière'", "marker",
      fx("\\oldpage[IV-4]{324}\ndonc régulière", "donc régulière"),
      "Marker move, part 1 of 2: removes the marker here; the last p. 323 entry places it after "
      "'formellement lisse (pour'. Apply both together."),
    F(324, "l. 10: 'En outre, D = B̂ ⊗_Â C est un anneau semi-local complet'",
      "in the running text (crop p324_Ddisplay.png)", "set as a display", "formula",
      fx("En outre,\n\\[\n  D=", "En outre, $D="),
      "Part 1 of 2 of the inline setting: apply together with the 'C\\n\\]\\nest un anneau' entry below. "
      "Independent of the tensor-sign entry between them (no overlap)."),
    F(324, "same formula: the tensor sign of B̂ ⊗_Â C",
      "plain ⊗ with subscript Â; the hat stands over the subscript A, not over ⊗ (5x crop p324_otimes.png)",
      "\\widehat\\otimes (completed tensor product)", "symbol",
      fx(r"\widehat\otimes_{\widehat A}", r"\otimes_{\widehat A}"),
      "Not a misprint: C is finite free over Â, so B̂ ⊗_Â C is already complete."),
    F(324, "same formula: end of the display", "in the running text", "\\] closing the display",
      "formula", fx("C\n\\]\nest un anneau semi-local", "C$\nest un anneau semi-local"),
      "Part 2 of 2 of the inline setting (see above)."),
    F(324, "'sans quoi on aurait q = (qD_0) ∩ B ⊂ (mD_0) ∩ B = mB = p par fidèle platitude'",
      "in the running text (page_324_s2.png, l. 11)", "set as a display", "formula",
      fx("sans quoi on aurait\n\\[\n  \\mathfrak q=(\\mathfrak qD_0)\\cap B\n  \\subset(\\mathfrak mD_0)\\cap B=\\mathfrak mB=\\mathfrak p\n\\]\npar fidèle",
         "sans quoi on aurait\n$\\mathfrak q=(\\mathfrak qD_0)\\cap B\\subset(\\mathfrak mD_0)\\cap B=\\mathfrak mB=\\mathfrak p$\npar fidèle")),
    F(324, "'pas à l'idéal p' = p + BT_1 + ... + BT_{n-1} : en effet'",
      "in the running text (crop p324_pprime_zoom.png)", "set as a display", "formula",
      fx("l'idéal\n\\[\n  \\mathfrak p'=", "l'idéal $\\mathfrak p'="),
      "Part 1 of 2 of the inline setting: apply together with the '_{n-1};' entry below."),
    F(324, "same formula: 'BT_1 + . . . + BT_{n-1}'",
      "baseline dots (crop p324_pprime_zoom.png)", "\\cdots", "symbol",
      fx(r"p+BT_1+\cdots+BT", r"p+BT_1+\ldots+BT"),
      "Independent of the two inline entries around it (no overlap)."),
    F(324, "same formula: 'BT_{n-1} : en effet'",
      "colon after the formula, which stands in the line (crop p324_pprime_zoom.png)",
      "semicolon, and \\] closing the display", "punctuation",
      fx("_{n-1};\n\\]\nen effet", "_{n-1}$ :\nen effet"),
      "Part 2 of 2 of the inline setting (see the 'l'idéal' entry above)."),
    F(324, "'a pour idéal maximal mB' + B'T_1 + ... + B'T_{n-1} = m''",
      "baseline dots (crop p324_mprime.png)", "\\cdots", "symbol",
      fx(r"B'T_1+\cdots+B'T_{n-1}", r"B'T_1+\ldots+B'T_{n-1}")),
    F(324, "'tel que (σ(f))‾(0, ..., 0, T_n) ≠ 0'",
      "the bar covers '(σ(f))' with its outer parentheses (crop p324_sigmabar.png)",
      "(\\overline{\\sigma(f)}): bar over σ(f) only", "formula",
      fx(r"(\overline{\sigma(f)})(0", r"\overline{(\sigma(f))}(0")),
]


def lf(path):
    with open(path, "rb") as f:
        return f.read().decode("utf-8").replace("\r\n", "\n")


src = lf(SRC)
segments = {}
for p in (320, 321, 322, 323, 324):
    i = src.index("\\oldpage[IV-4]{%d}" % p)
    i = src.rfind("\n", 0, i) + 1  # include indentation before the marker
    j = src.index("\\oldpage[IV-4]{%d}" % (p + 1))
    j = src.rfind("\n", 0, j) + 1
    segments[p] = src[i:j]

ok = True
state_page = {p: lf(RUN + r"\page_%d.tex" % p) for p in segments}
state_seg = dict(segments)
for n, d in enumerate(findings):
    fxd = d["fix"]
    if fxd is None:
        continue
    p = d["page"]
    for label, state in (("page", state_page), ("segment", state_seg)):
        c = state[p].count(fxd["old"])
        if c != 1:
            ok = False
            print(f"#{n} p.{p} {label}: old occurs {c} times: {fxd['old']!r}")
        else:
            state[p] = state[p].replace(fxd["old"], fxd["new"], 1)

# also report file-wide counts of the original "old" strings, for information
for n, d in enumerate(findings):
    if d["fix"] is None:
        continue
    c = src.count(d["fix"]["old"])
    if c != 1:
        print(f"info #{n} p.{d['page']}: old occurs {c} times in the whole file")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(findings, f, ensure_ascii=False, indent=1)
    f.write("\n")

from collections import Counter
cnt = Counter()
for d in findings:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted(segments):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(findings), "OK" if ok else "PROBLEMS")

# write the fully patched page texts for a final look
for p in segments:
    with open(RUN + r"\crops_320_324\patched_%d.txt" % p, "w", encoding="utf-8", newline="\n") as f:
        f.write(state_page[p])
