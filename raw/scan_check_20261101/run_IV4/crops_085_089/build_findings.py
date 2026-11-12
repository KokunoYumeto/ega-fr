import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = r'user/Documents/ega_scan_check_20261101/run_IV4'
SRC = r'user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-17-fr.tex'
OUT = RUN + '/findings_085_089.json'

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    F.append(d)


G92 = 'GLOBAL_ISSUES 92.'
C23 = 'Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.'

# ---------------- page 85 ----------------
add(85, "proof of (17.11.4), l. 2: 'S[T_1, ..., T_n] -> S est lisse (17.3.8)'",
    "T_n (crop p85_Tn.png), as in the statement of (17.11.4) on p. 84 ('un entier r', T_n)",
    "T_r: silent correction", 'misprint_in_print', None, 'high',
    r"$S[T_1,\ldots,T_r]\to S$ est lisse", r"$S[T_1,\ldots,T_n]\to S$ est lisse",
    "Same misprint as in the statement of (17.11.4) (p. 84 finding, corrected reading T_r with 'un entier r' and (17.11.3)); the diplomatic text restores the printed T_n.",
    corrected=r"$S[T_1,\ldots,T_r]\to S$ est lisse")
add(85, "proof of (17.11.4): 'tel que Omega^1_{X/S}|U soit localement libre'",
    "italic Omega (crop p85_om1z.png)", "upright \\Omega", 'font', None, 'high',
    r"que $\Omega^1_{X/S}|U$ soit", r"que $\varOmega^1_{X/S}|U$ soit", G92)
add(85, "proof of (17.11.4): 'forment une base de Omega^1_{X/S}|U'",
    "italic Omega (crop p85_om2z.png)", "upright \\Omega", 'font', None, 'high',
    r"base de $\Omega^1_{X/S}|U$;", r"base de $\varOmega^1_{X/S}|U$;", G92)
add(85, "Proposition (17.11.5): '(pour une généralisation de cette proposition, voir (18.10.5))'",
    "the whole parenthesis upright (crops p85_pour.png, p85_gen.png)", "italic (inside the italic statement)",
    'convention', 6, 'high',
    "(pour une généralisation de cette proposition, voir (18.10.5)).",
    "\\textup{(pour une généralisation de cette proposition, voir (18.10.5))}.")
add(85, "proof of (17.11.5): 'Spec(C) -> Spec(k(y)) = Spec(k)'",
    "bold italic k in k(y) (crop p85_speck.png); the k of Spec(k) is plain italic", "plain k", 'convention', 1, 'high',
    r"\Spec(k(y))=\Spec(k)", r"\Spec(\boldsymbol{k}(y))=\Spec(k)")
add(85, "proof of (17.11.5): '(I, 3.3.12)'", "bold I (crop p85_I.png)", "plain I", 'convention', 2, 'high',
    "(I, 3.3.12)", r"(\textbf{I}, 3.3.12)")
add(85, "proof of (17.11.5): 'paramètres pour B (0, 17.1.7)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 17.1.7)", r"(\textbf{0}, 17.1.7)")
add(85, "proof of (17.11.5): 'la condition (17.6.3, e''))'",
    "the label e'') in italic with its own closing parenthesis, then the upright parenthesis closing the reference: two closing parentheses (crop p85_epp.png)",
    "(17.6.3, $e''$): the label's parenthesis is missing", 'missing', None, 'high',
    "(17.6.3, $e''$)", "(17.6.3, \\emph{e$''$)})",
    "Same form as the other references to (17.6.3, e'')) in ega4-17 (italic label).")
add(85, "proof of (17.11.5): '(0, 17.1.1 et Bourbaki'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 17.1.1 et", r"(\textbf{0}, 17.1.1 et")
add(85, "heading 17.12: '... et morphismes différentiellement lisses.'",
    "final full stop (crop p85_head.png)", "no full stop (the other ega4-17 subsection titles have one)",
    'punctuation', None, 'high',
    "et morphismes différentiellement lisses}", "et morphismes différentiellement lisses.}")
add(85, "Théorème (17.12.1), label a)", "'a)' upright", "italic label", 'convention', 6, 'high',
    r"\item[a)] $h$ est lisse au point $y$", r"\item[\textup{a)}] $h$ est lisse au point $y$")
add(85, "Théorème (17.12.1) b): label b) and '(16.4.21)'", "'b)' and '(16.4.21)' upright (crop p85_b.png)",
    "italic", 'convention', 6, 'high',
    r"\item[b)] $f$ est lisse au point $x$, et l'homomorphisme canonique (16.4.21)",
    r"\item[\textup{b)}] $f$ est lisse au point $x$, et l'homomorphisme canonique \textup{(16.4.21)}",
    "One edit for the label and the reference.")
add(85, "Théorème (17.12.1) b), display '(N_{Y/X})_y -> (j^*(Omega^1_{X/S}))_y'",
    "italic Omega (crop p85_disp.png)", "upright \\Omega", 'font', None, 'high',
    r"(j^*(\Omega^1_{X/S}))_y", r"(j^*(\varOmega^1_{X/S}))_y", G92)
add(85, "Théorème (17.12.1), label c)", "'c)' upright (crop p85_c.png)", "italic label", 'convention', 6, 'high',
    r"\item[c)] $h$ est lisse", r"\item[\textup{c)}] $h$ est lisse")
add(85, "Théorème (17.12.1) c): 'soit une immersion régulière (16.9.2)'", "'(16.9.2)' upright (crop p85_c.png)",
    "italic", 'convention', 6, 'high',
    "régulière (16.9.2).", "régulière \\textup{(16.9.2)}.")

# ---------------- page 86 ----------------
add(86, "Théorème (17.12.1), label c')", "'c')' upright (crop p86_cp.png)", "italic label", 'convention', 6, 'high',
    r"\item[c')]", r"\item[\textup{c$'$)}]")
add(86, "Théorème (17.12.1) c'): 'S•_{O_Y}(N_{Y/X})'", "bold S with a raised bullet (crop p86_Sgr.png)",
    "\\mathbf{S}_{\\sh{O}_Y}: no bullet", 'formula', None, 'high',
    r"\mathbf{S}_{\sh{O}_Y}(\sh{N}_{Y/X})", r"\mathbf{S}^{\bullet}_{\sh{O}_Y}(\sh{N}_{Y/X})",
    "Edit 1 of 4 on this formula; apply in this order: bullet, script Gr, inline, upright parenthesis.")
add(86, "Théorème (17.12.1) c'): '-> Gr•(j)'", "script Gr (the sheaf) with a raised bullet (crop p86_Sgr.png)",
    "\\operatorname{gr}^{\\bullet}(j): roman gr", 'symbol', None, 'high',
    r"\to\operatorname{gr}^{\bullet}(j)", r"\to\mathscr{G}r^{\bullet}(j)",
    "Edit 2 of 4; written \\mathscr{G}r^{\\bullet}(j) as in (16.9.8) (ega4-16).")
add(86, "Théorème (17.12.1) c'): the formula S•(N_{Y/X}) -> Gr•(j)",
    "set in the line: 'l'homomorphisme canonique S•... -> Gr•(j) est bijectif).' (crop p86_Sgr.png)", "displayed",
    'other', None, 'high',
    "canonique\n  \\[\n  \\mathbf{S}^{\\bullet}_{\\sh{O}_Y}(\\sh{N}_{Y/X})\\to\\mathscr{G}r^{\\bullet}(j)\n  \\]\n  est bijectif).",
    "canonique $\\mathbf{S}^{\\bullet}_{\\sh{O}_Y}(\\sh{N}_{Y/X})\\to\\mathscr{G}r^{\\bullet}(j)$ est bijectif).",
    "Edit 3 of 4: 'old' is the text after edits 1-2.")
add(86, "Théorème (17.12.1) c'): '(autrement dit (16.9.8), il existe ... est bijectif)'",
    "the whole parenthesis upright (crops p86_aut.png, p86_Sgr.png)", "italic (inside the italic statement)",
    'convention', 6, 'high',
    "quasi-régulière (autrement dit (16.9.8), il existe un voisinage $U$ de $y$ dans $Y$ dans lequel $\\sh{N}_{Y/X}$ est un $\\sh{O}_Y$-Module localement libre et l'homomorphisme canonique $\\mathbf{S}^{\\bullet}_{\\sh{O}_Y}(\\sh{N}_{Y/X})\\to\\mathscr{G}r^{\\bullet}(j)$ est bijectif).",
    "quasi-régulière \\textup{(autrement dit (16.9.8), il existe un voisinage $U$ de $y$ dans $Y$ dans lequel $\\sh{N}_{Y/X}$ est un $\\sh{O}_Y$-Module localement libre et l'homomorphisme canonique $\\mathbf{S}^{\\bullet}_{\\sh{O}_Y}(\\sh{N}_{Y/X})\\to\\mathscr{G}r^{\\bullet}(j)$ est bijectif)}.",
    "Edit 4 of 4: 'old' is the text after edits 1-3.")
add(86, "proof of (17.12.1): 'l'équivalence de a) et b)'", "labels italic (crop p86_ab.png)", "upright labels",
    'italics', None, 'high',
    "l'équivalence de a) et b), on peut", "l'équivalence de \\emph{a)} et \\emph{b)}, on peut")
add(86, "proof of (17.12.1): 'le critère jacobien (0, 22.6.1)'", "bold 0 (crop p86_om.png)", "plain 0", 'convention', 2, 'high',
    "(0, 22.6.1)", r"(\textbf{0}, 22.6.1)")
add(86, "proof of (17.12.1): 'ainsi que (0, 19.1.14)'", "bold 0 (crop p86_om.png)", "plain 0", 'convention', 2, 'high',
    "(0, 19.1.14)", r"(\textbf{0}, 19.1.14)")
add(86, "proof of (17.12.1): 'compte tenu de ce que Omega^1_{X/S} est un O_X-Module'", "italic Omega (crop p86_om.png)",
    "upright \\Omega", 'font', None, 'high',
    r"ce que $\Omega^1_{X/S}$ est un", r"ce que $\varOmega^1_{X/S}$ est un", G92)
add(86, "proof of (17.12.1): 'prouvons que a) entraîne c')'", "labels italic", "upright labels", 'italics', None, 'high',
    "prouvons que a) entraîne c').", "prouvons que \\emph{a)} entraîne \\emph{c')}.")
add(86, "proof of (17.12.1): 'd'après (0, 19.3.8)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 19.3.8)", r"(\textbf{0}, 19.3.8)")
add(86, "proof of (17.12.1): 'Par suite (0, 19.5.4)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 19.5.4)", r"(\textbf{0}, 19.5.4)")
add(86, "proof of (17.12.1): 'S•_{B'/J'}(J'/J'^2)'", "bold S with a raised bullet (crop p86_S2.png)",
    "\\mathbf{S}_{B'/\\mathfrak J'}: no bullet", 'formula', None, 'high',
    r"\mathbf{S}_{B'/\mathfrak J'}", r"\mathbf{S}^{\bullet}_{B'/\mathfrak J'}",
    "Edit 1 of 2 on this formula (then the inline edit).")
add(86, "proof of (17.12.1): the formula S•_{B'/J'}(J'/J'^2) -> gr•_{J'}(B')",
    "set in the line: 'l'homomorphisme canonique S•... -> gr•(B') est bijectif.' (crop p86_S2.png)", "displayed",
    'other', None, 'high',
    "canonique\n\\[\n\\mathbf{S}^{\\bullet}_{B'/\\mathfrak J'}(\\mathfrak J'/\\mathfrak J'^2)\\to\\operatorname{gr}_{\\mathfrak J'}^{\\bullet}(B')\n\\]\nest bijectif.",
    "canonique $\\mathbf{S}^{\\bullet}_{B'/\\mathfrak J'}(\\mathfrak J'/\\mathfrak J'^2)\\to\\operatorname{gr}_{\\mathfrak J'}^{\\bullet}(B')$ est bijectif.",
    "Edit 2 of 2: 'old' is the text after the bullet edit.")
add(86, "proof of (17.12.1): 'en remplaçant F par J~''", "the tilde over the Fraktur J only, the prime outside (crop p86_Jt.png)",
    "\\widetilde{\\mathfrak J'}: tilde over J'", 'convention', 8, 'high',
    r"\widetilde{\mathfrak J'}", r"\widetilde{\mathfrak J}'")
add(86, "proof of (17.12.1): 'que les conditions c') et c) sont équivalentes'", "labels italic", "upright labels",
    'italics', None, 'high',
    "que les conditions c') et c) sont", "que les conditions \\emph{c')} et \\emph{c)} sont")
add(86, "proof of (17.12.1): 'Montrons enfin que c) entraîne a). ... la condition b) entraîne c), ... si c) est vérifiée'",
    "labels italic", "upright labels", 'italics', None, 'high',
    "Montrons enfin que c) entraîne a). Du fait que, dans (11.3.8), la condition b) entraîne c), on voit déjà que si c) est vérifiée",
    "Montrons enfin que \\emph{c)} entraîne \\emph{a)}. Du fait que, dans (11.3.8), la condition \\emph{b)} entraîne \\emph{c)}, on voit déjà que si \\emph{c)} est vérifiée",
    "Five labels in one edit.")
add(86, "proof of (17.12.1): 'sous l'hypothèse c), f^{-1}(s)'", "label italic (crop p86_ks.png)", "upright label",
    'italics', None, 'high',
    "l'hypothèse c), $f^{-1}(s)$", "l'hypothèse \\emph{c)}, $f^{-1}(s)$")
add(86, "proof of (17.12.1): 'est lisse sur k(s) au point x'", "bold italic k (crop p86_ks2.png)", "plain k",
    'convention', 1, 'high',
    "lisse sur $k(s)$ au point", "lisse sur $\\boldsymbol{k}(s)$ au point")
add(86, "proof of (17.12.1): 'en posant s=h(x)'",
    "s = h(x) (crop p86_shx.png); h : Y -> S is not defined at the point x of X", "keeps the printed h(x)",
    'misprint_in_print', None, 'medium', None, None,
    "The TeX keeps the printed reading. Corrected edition: s=f(x) (= h(y)). No erratum in Liste 3.",
    corrected="$s=f(x)$")
add(86, "proof of (17.12.1): 'comme on a remarqué que la condition c) est stable'", "label italic", "upright label",
    'italics', None, 'high',
    "que la condition c) est stable", "que la condition \\emph{c)} est stable")
add(86, "proof of (17.12.1): 'O_{Y,y}=O_{X,x}/J_x, où J_x est un idéal'",
    "script J twice (crop p86_Jx.png), the script J of (17.12.2); the ideal of B earlier in the proof is Fraktur",
    "Fraktur \\mathfrak J_x", 'symbol', None, 'high',
    "\\sh{O}_{X,x}/\\mathfrak J_x$, où $\\mathfrak J_x$ est", "\\sh{O}_{X,x}/\\sh{J}_x$, où $\\sh{J}_x$ est")
add(86, "proof of (17.12.1): 'et O_{Y,y} est un anneau régulier;'", "'régulier' italic (crop p86_reg.png)", "roman",
    'italics', None, 'high',
    "est un anneau régulier; comme", "est un anneau \\emph{régulier}; comme")
add(86, "proof of (17.12.1): '(0, 16.4.1)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 16.4.1)", r"(\textbf{0}, 16.4.1)")
add(86, "proof of (17.12.1): 'la conclusion résulte de (0, 17.1.7)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 17.1.7)", r"(\textbf{0}, 17.1.7)")
add(86, "Corollaire (17.12.2): 'Avec les notations de (17.12.1)'", "'(17.12.1)' upright (crop p86_cor.png)", "italic",
    'convention', 6, 'high',
    "Avec les notations de (17.12.1), supposons", "Avec les notations de \\textup{(17.12.1)}, supposons")
add(86, "Corollaire (17.12.2), label a)", "'a)' upright", "italic label", 'convention', 6, 'high',
    r"\item[a)] Les $(g_i)_x$", r"\item[\textup{a)}] Les $(g_i)_x$")
add(86, "Corollaire (17.12.2), label b)", "'b)' upright", "italic label", 'convention', 6, 'high',
    r"\item[b)] Si $g_i'$", r"\item[\textup{b)}] Si $g_i'$")

# ---------------- page 87 ----------------
add(87, "Corollaire (17.12.2), label c)", "'c)' upright (crop p87_c.png)", "italic label", 'convention', 6, 'high',
    r"\item[c)] Les images", r"\item[\textup{c)}] Les images")
add(87, "Corollaire (17.12.2) c): '(Omega^1_{X/S})_x ⊗ k(x)'", "italic Omega (crop p87_cz.png)", "upright \\Omega",
    'font', None, 'high',
    r"dans $(\Omega^1_{X/S})_x", r"dans $(\varOmega^1_{X/S})_x", G92)
add(87, "Corollaire (17.12.2) c): '⊗_{O_{X,x}} k(x) ... indépendants sur k(x)'", "bold italic k twice (crop p87_cz.png)",
    "plain k", 'convention', 1, 'high',
    "}k(x)$ sont des éléments linéairement indépendants sur $k(x)$",
    "}\\boldsymbol{k}(x)$ sont des éléments linéairement indépendants sur $\\boldsymbol{k}(x)$",
    "Two occurrences in one edit.")
add(87, "Corollaire (17.12.2), label d)", "'d)' upright (crop p87_d.png)", "italic label", 'convention', 6, 'high',
    r"\item[d)] Il existe", r"\item[\textup{d)}] Il existe")
add(87, "Corollaire (17.12.2) d): 'des sections g_j (r+1≤j≤n) de O_X'", "upright parentheses (crop p87_dz.png)",
    "italic parentheses", 'convention', 6, 'high',
    "($r+1\\leq j\\leq n$) de $\\sh{O}_X$", "\\textup{($r+1\\leq j\\leq n$)} de $\\sh{O}_X$",
    "Parenthesised formula inside an italic statement (GLOBAL_ISSUES 26), as on p. 84.")
add(87, "Corollaire (17.12.2) d): 'les sections g_i|U (1≤i≤r)'", "upright parentheses (crop p87_dz2.png)",
    "italic parentheses", 'convention', 6, 'high',
    "($1\\leq i\\leq r$) et $g_j$", "\\textup{($1\\leq i\\leq r$)} et $g_j$")
add(87, "Corollaire (17.12.2) d): 'et g_j (r+1≤j≤n) (II, 1.2.7)'", "upright parentheses (crop p87_dz2.png)",
    "italic parentheses", 'convention', 6, 'high',
    "et $g_j$ ($r+1\\leq j\\leq n$)", "et $g_j$ \\textup{($r+1\\leq j\\leq n$)}")
add(87, "Corollaire (17.12.2) d): '(II, 1.2.7)'", "bold II; the reference upright (crop p87_dz2.png)",
    "plain II, italic reference", 'convention', 2, 'high',
    "(II, 1.2.7)", "\\textup{(\\textbf{II}, 1.2.7)}",
    "One edit for convention 2 (bold II) and convention 6 (upright reference), as on p. 84.")
add(87, "proof of (17.12.2): 'l'équivalence de a) et b) résulte du lemme de Nakayama'", "labels italic", "upright labels",
    'italics', None, 'high',
    "l'équivalence de a) et b) résulte", "l'équivalence de \\emph{a)} et \\emph{b)} résulte")
add(87, "proof of (17.12.2): 'En vertu de (17.12.1, b))'", "label b) italic", "upright label", 'italics', None, 'high',
    "(17.12.1, b))", "(17.12.1, \\emph{b)})")
add(87, "proof of (17.12.2): '(Omega^1_{X/S})_x ⊗ (O_{X,x}/J_x)'", "italic Omega (crop p87_om6.png)", "upright \\Omega",
    'font', None, 'high',
    r"rang $n$, $(\Omega^1_{X/S})_x", r"rang $n$, $(\varOmega^1_{X/S})_x", G92)
add(87, "proof of (17.12.2): 'l'équivalence de b) et c) résulte de Bourbaki'", "labels italic", "upright labels",
    'italics', None, 'high',
    "l'équivalence de b) et c) résulte de", "l'équivalence de \\emph{b)} et \\emph{c)} résulte de")
add(87, "proof of (17.12.2): 'En outre, si a) est vérifié'", "label italic (crop p87_verif.png)", "upright label",
    'italics', None, 'high',
    "En outre, si a) est", "En outre, si \\emph{a)} est")
add(87, "proof of (17.12.2): 'si a) est vérifié, (g'_i)_x est ainsi identifié'",
    "'vérifié' without the agreement e (crop p87_verif.png); elsewhere 'si c) est vérifiée' (p. 86)",
    "'vérifiée': silent correction", 'misprint_in_print', None, 'medium',
    "est vérifiée, $(g_i')_x$", "est vérifié, $(g_i')_x$",
    "The diplomatic text restores the printed 'vérifié'.",
    corrected="est vérifiée, $(g_i')_x$")
add(87, "proof of (17.12.2): 'le O_{X,x}-module (Omega^1_{X/S})_x étant libre'", "italic Omega (crop p87_om7.png)",
    "upright \\Omega", 'font', None, 'high',
    r"-module $(\Omega^1_{X/S})_x$ étant", r"-module $(\varOmega^1_{X/S})_x$ étant", G92)
add(87, "proof of (17.12.2): 'n—r sections'", "long dash for the minus sign (crop p87_nr.png)", "minus sign",
    'convention', 7, 'high',
    "$n-r$ sections", "$n\\setmin r$ sections", C23)
add(87, "proof of (17.12.2): 'forment une base de (Omega^1_{X/S})_x'", "italic Omega (crop p87_om8.png)",
    "upright \\Omega", 'font', None, 'high',
    r"base de $(\Omega^1_{X/S})_x$;", r"base de $(\varOmega^1_{X/S})_x$;", G92)
add(87, "proof of (17.12.2): 'cela prouve que a) entraîne d)'", "labels italic", "upright labels", 'italics', None, 'high',
    "prouve que a) entraîne d).", "prouve que \\emph{a)} entraîne \\emph{d)}.")
add(87, "Proposition (17.12.4): '(autrement dit (16.10.5) Delta_f : X -> X×_S X est une immersion quasi-régulière)'",
    "the whole parenthesis upright (crop p87_p124.png)", "italic (inside the italic statement)", 'convention', 6, 'high',
    "lisse (autrement dit (16.10.5) $\\Delta_f:X\\to X\\times_SX$ est une immersion quasi-régulière).",
    "lisse \\textup{(autrement dit (16.10.5) $\\Delta_f:X\\to X\\times_SX$ est une immersion quasi-régulière)}.")
add(87, "Proposition (17.12.4): 'En particulier, les P^n_f = P^n_{X/S} ... localement libres de type fini.'",
    "italic, like the rest of the statement (crop p87_p124.png)",
    "wrapped in \\emph inside the italic environment: set upright", 'italics', None, 'high',
    "\\emph{En particulier, les $\\sh{P}_f^n=\\sh{P}_{X/S}^n$ et les $\\operatorname{gr}_n(\\sh{P}_{X/S})$ sont des $\\sh{O}_X$-Modules localement libres de type fini.}",
    "En particulier, les $\\sh{P}_f^n=\\sh{P}_{X/S}^n$ et les $\\operatorname{gr}_n(\\sh{P}_{X/S})$ sont des $\\sh{O}_X$-Modules localement libres de type fini.",
    "The TeX had the italics of (17.12.4) inverted (with the preceding finding).")
add(87, "Proposition (17.12.5), label a)", "'a)' upright", "italic label", 'convention', 6, 'high',
    r"\item[a)] $f$ est différentiellement lisse.", r"\item[\textup{a)}] $f$ est différentiellement lisse.")
add(87, "Proposition (17.12.5), label b)", "'b)' upright", "italic label", 'convention', 6, 'high',
    r"\item[b)] Pour tout morphisme", r"\item[\textup{b)}] Pour tout morphisme")
add(87, "Proposition (17.12.5), label c)", "'c)' upright", "italic label", 'convention', 6, 'high',
    r"\item[c)] La seconde projection", r"\item[\textup{c)}] La seconde projection")

# ---------------- page 88 ----------------
add(88, "proof of (17.12.5): 'La condition c) est un cas particulier de b)'", "labels italic (crop p88_cparen.png)",
    "upright labels", 'italics', None, 'high',
    "La condition c) est un cas particulier de b):", "La condition \\emph{c)} est un cas particulier de \\emph{b)}:")
add(88, "proof of (17.12.5): 'et g=f dans b), car alors'", "label italic", "upright label", 'italics', None, 'high',
    "dans b), car alors", "dans \\emph{b)}, car alors")
add(88, "proof of (17.12.5): 'En second lieu, c) entraîne a)'", "labels italic", "upright labels", 'italics', None, 'high',
    "En second lieu, c) entraîne a), car", "En second lieu, \\emph{c)} entraîne \\emph{a)}, car")
add(88, "proof of (17.12.5): 'Enfin, montrons que a) entraîne b)'", "labels italic", "upright labels", 'italics', None, 'high',
    "montrons que a) entraîne b);", "montrons que \\emph{a)} entraîne \\emph{b)};")
add(88, "proof of (17.12.5): '... de Delta_f(X) (17.12.3). Or, si g' : X' -> X'",
    "'Or, si g'...' continues the same paragraph, on the same line (page_088_s1.png)",
    "blank line: a new paragraph", 'other', None, 'high',
    "(17.12.3).\n\nOr, si", "(17.12.3).\nOr, si", "Paragraph break the print lacks.")
add(88, "proof of (17.12.5): 'v=(g', g')_Y : X' -> X×_Y X'",
    "v = (g', g')_Y (crop p88_vz.png); with it p_2∘v = g', not h∘f' = g'∘s'∘f', so the displayed square does not commute",
    "keeps the printed (g',g')_Y", 'misprint_in_print', None, 'medium', None, None,
    "The TeX keeps the printed reading. Corrected edition: v=(g', h∘f')_Y (= (g', g'∘s'∘f')_Y), which makes the square commute and cartesian. Probably the authors' slip; no erratum in Liste 3: verify before the corrected edition changes it.",
    corrected="$v=(g',h\\circ f')_Y$")
add(88, "proof of (17.12.5): '(I, 3.3.9)'", "bold I", "plain I", 'convention', 2, 'high',
    "(I, 3.3.9)", r"(\textbf{I}, 3.3.9)")
add(88, "Corollaire (17.12.6): 'Les notations étant celles de (8.8.1)'", "'(8.8.1)' upright (crop p88_cor.png)", "italic",
    'convention', 6, 'high',
    "celles de (8.8.1), on", "celles de \\textup{(8.8.1)}, on")
add(88, "Corollaire (17.12.6): '(auquel cas f_mu : X_mu -> S_mu est différentiellement lisse pour mu≥lambda)'",
    "words italic, both parentheses upright (crops p88_po2.png, p88_paren_close.png; compare the slanted italic parenthesis of 'c)', p88_cparen.png)",
    "italic parentheses", 'convention', 6, 'medium',
    "(auquel cas $f_\\mu:X_\\mu\\to S_\\mu$ est différentiellement lisse pour $\\mu\\geq\\lambda$)",
    "\\textup{(}auquel cas $f_\\mu:X_\\mu\\to S_\\mu$ est différentiellement lisse pour $\\mu\\geq\\lambda$\\textup{)}",
    "GLOBAL_ISSUES 96; same form as the p. 84 fix '\\textup{(}qui sont aussi ...\\textup{)}'.")
add(88, "page break 88/89 inside 'm∘(s×1_G) : ... -> G est un | S-isomorphisme'",
    "p. 88 ends 'est un', p. 89 begins 'S-isomorphisme du préschéma G' (no indent)",
    "blank line before \\oldpage[IV-4]{89} (and another after it): a paragraph break inside the sentence",
    'marker', None, 'high',
    "G\\times_SG\\to G$ est un\n\n", "G\\times_SG\\to G$ est un\n",
    "The marker is at the right place. Part 1 of 2: the first p. 89 finding removes the blank line after \\oldpage[IV-4]{89}; apply both.")

# ---------------- page 89 ----------------
add(89, "top of page_089.tex: blank line after \\oldpage[IV-4]{89}", "p. 89 begins mid-sentence ('S-isomorphisme du préschéma G')",
    "blank line between the marker and '$S$-isomorphisme'", 'marker', None, 'high',
    "\\oldpage[IV-4]{89}\n\n$S$-isomorphisme", "\\oldpage[IV-4]{89}\n$S$-isomorphisme",
    "Part 2 of 2 with the last p. 88 finding; both blank lines must go.")
add(89, "Remarque (17.12.8): 'en prenant delta(e')=... et delta(e'')=....'",
    "both formulas in the running text, joined by 'et' (crop p89_delta.png)",
    "displayed, joined by ',\\qquad': the connecting word 'et' lost", 'missing', None, 'high',
    "en prenant\n\\[\n\\delta(e')=e'\\otimes e'+e''\\otimes e'',\\qquad\n\\delta(e'')=e'\\otimes e''+e''\\otimes e'.\n\\]\nLa section unité",
    "en prenant $\\delta(e')=e'\\otimes e'+e''\\otimes e''$ et $\\delta(e'')=e'\\otimes e''+e''\\otimes e'$.\nLa section unité",
    "Display set inline, 'et' restored, comma removed.")
add(89, "Remarque (17.12.8): 'G est différentiellement lisse sur S (17.12.6)'",
    "(17.12.6), the corollary on passage to the limit; the argument (G smooth over S along the unit section) is the example (17.12.7)",
    "keeps the printed (17.12.6)", 'misprint_in_print', None, 'medium', None, None,
    "The TeX keeps the printed reading. Corrected edition: (17.12.7). No erratum in Liste 3.",
    corrected="(17.12.7)")
add(89, "(17.13.1): 'i : Y -> X une S-immersion'", "'immersion' italic (crop p89_imm.png); the later 'j est une S-immersion' is roman",
    "roman", 'italics', None, 'high',
    "une $S$-immersion, $f:X'\\to X$", "une $S$-\\emph{immersion}, $f:X'\\to X$")
add(89, "(17.13.1.2): label gr_1(g) of the first vertical arrow",
    "the label stands to the LEFT of the arrow (page_089_s3.png)",
    "\\ar{d}{...}: tikz-cd puts the label to the right of a downward arrow", 'other', None, 'high',
    "\\ar{d}{\\operatorname{gr}_1(g)}", "\\ar{d}[swap]{\\operatorname{gr}_1(g)}",
    "Checked by a test compilation (crops_085_089/test_tikzcd.pdf).")
add(89, "(17.13.1.2), top row: 'f^*(Omega^1_{X/S}) ⊗ O_{Y'} -> g^*(Omega^1_{Y/S})'", "italic Omega twice (crop p89_top.png)",
    "upright \\Omega", 'font', None, 'high',
    "f^*(\\Omega^1_{X/S})\\otimes_{\\sh{O}_{X'}}\\sh{O}_{Y'} \\ar{r} \\ar{d} & g^*(\\Omega^1_{Y/S})",
    "f^*(\\varOmega^1_{X/S})\\otimes_{\\sh{O}_{X'}}\\sh{O}_{Y'} \\ar{r} \\ar{d} & g^*(\\varOmega^1_{Y/S})", G92)
add(89, "(17.13.1.2), bottom row: 'Omega^1_{X'/S} ⊗ O_{Y'} -> Omega^1_{Y'/S}'", "italic Omega twice (crop p89_bot.png)",
    "upright \\Omega", 'font', None, 'high',
    "& \\Omega^1_{X'/S}\\otimes_{\\sh{O}_{X'}}\\sh{O}_{Y'} \\ar{r} & \\Omega^1_{Y'/S}",
    "& \\varOmega^1_{X'/S}\\otimes_{\\sh{O}_{X'}}\\sh{O}_{Y'} \\ar{r} & \\varOmega^1_{Y'/S}", G92)
add(89, "(17.13.1): '(0, 20.5.7.3)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 20.5.7.3)", r"(\textbf{0}, 20.5.7.3)")
add(89, "(17.13.1): '(0, 20.5.11.3)'", "bold 0", "plain 0", 'convention', 2, 'high',
    "(0, 20.5.11.3)", r"(\textbf{0}, 20.5.11.3)")

# ---------------- verification ----------------
src = open(SRC, encoding='utf-8', newline='').read()
pat = re.compile(r'\\oldpage\[IV-4\]\{(\d+)\}')
cuts = [(int(m.group(1)), m.start()) for m in pat.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    if 85 <= n <= 89:
        seg[n] = src[s:cuts[i + 1][1]]
pages = {}
for n in range(85, 90):
    t = open(RUN + '/page_%03d.tex' % n, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    pages[n] = t.split('\n', 1)[1]
ok = True
for i, x in enumerate(F):
    fx = x['fix']
    if not fx:
        continue
    p = x['page']
    for name, store in (('page', pages), ('source', seg)):
        c = store[p].count(fx['old'])
        if c != 1:
            ok = False
            print('FAIL', name, i, p, c, repr(fx['old'])[:120])
        else:
            store[p] = store[p].replace(fx['old'], fx['new'])
    if x['kind'] == 'misprint_in_print' and x.get('corrected') is None:
        print('MISSING corrected', i)
print('all unique' if ok else 'PROBLEMS', len(F), 'findings')
# Per-page counts
from collections import Counter
cnt = Counter()
for x in F:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    cnt[(x['page'], k)] += 1
for n in range(85, 90):
    print(n, cnt[(n, 'normal')], cnt[(n, 'convention')], cnt[(n, 'misprint')])
# after-state check: page text after all fixes equals source segment after all fixes (modulo the page-file header)
for n in range(85, 90):
    a = pages[n].rstrip('\n')
    b = seg[n].rstrip('\n')
    print(n, 'page==source after fixes:', a == b)
if ok and '--write' in sys.argv:
    json.dump(F, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('written', OUT)
    # write the fixed pages for a compile check
    for n in range(85, 90):
        open(RUN + '/crops_085_089/fixed_%03d.tex' % n, 'w', encoding='utf-8', newline='').write(pages[n])
