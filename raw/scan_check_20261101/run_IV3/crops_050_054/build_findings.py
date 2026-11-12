import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_050_054.json"
NL = "\u00b6"  # placeholder for a line break in the raw strings below


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


CNOTE = (r"The category letter C (also C', C'_0) and the category names Pro, Sch are bold italic in the running text of "
         r"8.13 (enlarged crops); the TeX has \mathcal C (script) and \mathbf{Pro}, \mathbf{Sch} (bold upright). "
         r"\boldsymbol{C} as in the sibling IV-3 findings, \boldsymbol{\mathit{...}} for the names as for Ens in 0_III.")
SEE = "Bold italic category letter/name in the print; see the first font finding on p. 50."

# ---------------- page 50 ----------------
add(50, "(8.13.3), l. 4-5: 'une catégorie C, la catégorie Pro(C) des pro-objets de C a pour objets'",
    "C bold italic (3 times), Pro bold italic (enlarged crop)", r"\mathcal C, \mathbf{Pro}(\mathcal C)",
    "font", None, "high",
    r"une catégorie $\mathcal C$, la catégorie¶$\mathbf{Pro}(\mathcal C)$ des \emph{pro-objets} de $\mathcal C$ a",
    r"une catégorie $\boldsymbol{C}$, la catégorie¶$\boldsymbol{\mathit{Pro}}(\boldsymbol{C})$ des \emph{pro-objets} de $\boldsymbol{C}$ a",
    CNOTE)
add(50, "(8.13.3), l. 6: 'X=(X_mu) d'objets de C dont les ensembles'", "C bold italic", r"\mathcal C", "font", None,
    "high", r"d'objets de $\mathcal C$ dont", r"d'objets de $\boldsymbol{C}$ dont", SEE)
add(50, "(8.13.3), l. 9: 'les éléments de l'ensemble lim_mu' (lim_mu Hom(X_mu, X_mu')); la vérification'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"de l'ensemble¶\[¶\varprojlim_{\mu'}\left(\varinjlim_\mu¶\operatorname{Hom}(X_\mu,X'_{\mu'})\right)~;¶\]¶la vérification",
    r"de l'ensemble¶$\varprojlim_{\mu'}\left(\varinjlim_\mu¶\operatorname{Hom}(X_\mu,X'_{\mu'})\right)$~;¶la vérification",
    "Layout only (display vs inline). Apply before the next finding (misprint), whose 'old' lies inside this edit.")
add(50, "(8.13.3), l. 9: same formula, second argument of Hom",
    "Hom(X_mu, X_mu'): the second X has no prime (enlarged crop)", r"\operatorname{Hom}(X_\mu,X'_{\mu'})",
    "misprint_in_print", None, "high",
    r"\operatorname{Hom}(X_\mu,X'_{\mu'})", r"\operatorname{Hom}(X_\mu,X_{\mu'})",
    "The TeX silently corrects. The second argument is the term X'_{mu'} of the second pro-object X'. Apply after the "
    "display fix above (its 'old' is unchanged by that edit).",
    corrected=r"\operatorname{Hom}(X_\mu,X'_{\mu'})")
add(50, "(8.13.3), last line: 'le système des u''^mu_mu'' = u'^mu'_mu'' o u^mu_mu'.'",
    "u''^mu_{mu''} = u'^{mu'}_{mu''} o u^mu_{mu'} (enlarged crop)",
    r"only u_{\mu''}^{\prime\mu'}\circ u_{\mu'}^\mu: the left-hand side 'u''^mu_mu'' =' is missing", "missing", None,
    "high", r"des¶$u_{\mu''}^{\prime\mu'}\circ u_{\mu'}^\mu$.",
    r"des¶$u_{\mu''}^{\prime\prime\mu}=u_{\mu''}^{\prime\mu'}\circ u_{\mu'}^\mu$.", "")
add(50, "(8.13.4), l. 2: 'désignons par C la sous-catégorie pleine de la catégorie (Sch)_/S'",
    "C and Sch bold italic (enlarged crop)", r"\mathcal C, \mathbf{Sch}", "font", None, "high",
    r"par $\mathcal C$ la sous-catégorie pleine de la catégorie¶$(\mathbf{Sch})_{/S}$ des",
    r"par $\boldsymbol{C}$ la sous-catégorie pleine de la catégorie¶$(\boldsymbol{\mathit{Sch}})_{/S}$ des", SEE)
add(50, "(8.13.4), l. 4: 'se factorise en X -g-> X_0 -f-> S, où g : X -> X_0'",
    "the factorisation is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"se factorise en¶\[¶X\xrightarrow{g}X_0\xrightarrow{f}S,¶\]¶où $g:X\to X_0$",
    r"se factorise en¶$X\xrightarrow{g}X_0\xrightarrow{f}S$,¶où $g:X\to X_0$", "Layout only (display vs inline).")
add(50, "(8.13.4), l. 4: 'où g : X -> X_0 est affine et f : X_0 -> S de présentation finie;'",
    "'affine' and 'de présentation finie' in italics", "both roman", "italics", None, "high",
    r"est affine et $f:X_0\to S$ de présentation finie~;",
    r"est \emph{affine} et $f:X_0\to S$ \emph{de présentation finie}~;", "")
add(50, "(8.13.4), l. 5: 'les préschémas de C sont essentiellement affines'", "C bold italic", r"\mathcal C", "font",
    None, "high", r"les préschémas de $\mathcal C$ sont", r"les préschémas de $\boldsymbol{C}$ sont", SEE)
add(50, "(8.13.4), 2nd par., l. 1: 'la sous-catégorie pleine C'_0 de (Sch)_/S formée'",
    "C and Sch bold italic", r"\mathcal C'_0, \mathbf{Sch}", "font", None, "high",
    r"pleine $\mathcal C'_0$ de¶$(\mathbf{Sch})_{/S}$ formée",
    r"pleine $\boldsymbol{C}'_0$ de¶$(\boldsymbol{\mathit{Sch}})_{/S}$ formée", SEE)
add(50, "(8.13.4), 2nd par., l. 2: 'et la catégorie Pro(C'_0) des pro-objets de C'_0.'",
    "Pro and C bold italic (2 C)", r"\mathbf{Pro}(\mathcal C'_0), \mathcal C'_0", "font", None, "high",
    r"et la catégorie $\mathbf{Pro}(\mathcal C'_0)$ des pro-objets de¶$\mathcal C'_0$. Nous dirons",
    r"et la catégorie $\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0)$ des pro-objets de¶$\boldsymbol{C}'_0$. Nous dirons",
    SEE)
add(50, "(8.13.4), 2nd par., l. 3: 'un objet X=(X_mu) de Pro(C'_0) est essentiellement affine'",
    "Pro and C bold italic", r"\mathbf{Pro}(\mathcal C'_0)", "font", None, "high",
    r"de $\mathbf{Pro}(\mathcal C'_0)$ est¶\emph{essentiellement affine}",
    r"de $\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0)$ est¶\emph{essentiellement affine}", SEE)
add(50, "(8.13.4), 2nd par., l. 4: 'le morphisme de transition v_gamma mu : X_mu -> X_gamma soit affine (ce qui'",
    "'affine' in italics", "roman", "italics", None, "high",
    r"soit affine (ce qui", r"soit \emph{affine} (ce qui", "")
add(50, "(8.13.4), 2nd par., l. 5: 'On notera qu'un objet de Pro(C'_0) isomorphe'",
    "Pro and C bold italic", r"\mathbf{Pro}(\mathcal C'_0)", "font", None, "high",
    r"objet de $\mathbf{Pro}(\mathcal C'_0)$ \emph{isomorphe}",
    r"objet de $\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0)$ \emph{isomorphe}", SEE)
add(50, "(8.13.4): '... affine lui-même. Nous désignerons par C' ...'",
    "'Nous désignerons' starts flush left after a full line: same paragraph", "blank line: new paragraph", "other",
    None, "high", r"lui-même.¶¶Nous désignerons", r"lui-même.¶Nous désignerons",
    "Left edge of the line measured: flush with the text margin; paragraph starts on this page are indented.")
add(50, "(8.13.4): 'Nous désignerons par C' la sous-catégorie pleine de Pro(C'_0) formée des pro-objets de C'_0'",
    "C (3 times) and Pro bold italic", r"\mathcal C', \mathbf{Pro}(\mathcal C'_0), \mathcal C'_0", "font", None,
    "high",
    r"par $\mathcal C'$ la sous-catégorie pleine de¶$\mathbf{Pro}(\mathcal C'_0)$ formée des pro-objets de $\mathcal C'_0$",
    r"par $\boldsymbol{C}'$ la sous-catégorie pleine de¶$\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0)$ formée des pro-objets de $\boldsymbol{C}'_0$",
    SEE)
add(50, "(8.13.4), 'Cela étant', l. 1: 'pour tout objet X=(X_mu) de C', le S-préschéma'", "C bold italic",
    r"\mathcal C'", "font", None, "high", r"de $\mathcal C'$, le $S$-préschéma", r"de $\boldsymbol{C}'$, le $S$-préschéma",
    SEE)
add(50, "(8.13.4): 'montrons qu'on a ainsi défini un foncteur canonique'",
    "only 'foncteur' in italics; 'canonique' roman", r"\emph{foncteur canonique}", "italics", None, "high",
    r"\emph{foncteur canonique}", r"\emph{foncteur} canonique", "")
add(50, "(8.13.4.1): 'L : C' -> C'", "C' and C bold italic", r"\mathcal C', \mathcal C", "font", None, "high",
    r"L:\mathcal C'\longrightarrow\mathcal C", r"L:\boldsymbol{C}'\longrightarrow\boldsymbol{C}", SEE)
add(50, "(8.13.4.1): end of the display", "no full stop after 'L : C' -> C'", "full stop before \\tag",
    "punctuation", None, "high", r". \tag{8.13.4.1}", r" \tag{8.13.4.1}", "")
add(50, "after (8.13.4.1): 'On a en effet, pour deux objets'",
    "'On a en effet' starts flush left: the paragraph continues after the display",
    "blank line after \\end{equation}: new paragraph", "other", None, "high",
    r"\end{equation}¶¶On a en effet", r"\end{equation}¶On a en effet",
    "Left edge measured: flush with the text margin (indented paragraphs start about 110 px further right).")
add(50, "(8.13.4), 'On a en effet', l. 2: 'X'=(X'_mu') de C', une application canonique'", "C bold italic",
    r"\mathcal C'", "font", None, "high", r"de $\mathcal C'$, une application", r"de $\boldsymbol{C}'$, une application",
    SEE)
add(50, "first display after 'pour chaque mu'': 'lim_mu Hom_S(X_mu, X'_mu') -> Hom_S(lim X_mu, X'_mu')'",
    "the inner projective lim on the right has only the arrow under it, no index mu (enlarged crop)",
    r"\varprojlim_\mu X_\mu", "formula", None, "high",
    r"\longrightarrow¶\operatorname{Hom}_S(\varprojlim_\mu X_\mu",
    r"\longrightarrow¶\operatorname{Hom}_S(\varprojlim X_\mu",
    "Index the print does not have (cf. GLOBAL_ISSUES 30); the lims of the next display all carry their indices.")
add(50, "last display (bijection lim_mu' Hom_S(lim X_mu, X'_mu') ~> Hom_S(lim X_mu, lim X'_mu'))",
    "no comma after the display; p. 51 continues 'd'où une application canonique'", "comma at the end of the display",
    "punctuation", None, "high", r"X'_{\mu'}),¶\]", r"X'_{\mu'})¶\]", "")

# ---------------- page 51 ----------------
add(51, "(8.13.4.2): end of the display", "no comma after the formula", r"'), \tag{8.13.4.2}'", "punctuation", None,
    "high", r"), \tag{8.13.4.2}", r") \tag{8.13.4.2}", "Listed before the misprint of the same display; the edits do not overlap.")
add(51, "(8.13.4.2), right-hand side: '-> Hom(lim_mu X_mu, lim_mu' X'_mu')'",
    "plain Hom, without the subscript S (enlarged crop)", r"\operatorname{Hom}_S", "misprint_in_print", None, "medium",
    r"\longrightarrow¶\operatorname{Hom}_S(", r"\longrightarrow¶\operatorname{Hom}(",
    "The TeX silently corrects. The reading is certain; classed as a misprint because the same target is "
    "Hom_S(lim X_mu, lim X'_mu') in the bijection just before (p. 50) and the left-hand side has Hom_S.",
    corrected=r"\operatorname{Hom}_S(")
add(51, "Proposition (8.13.5), l. 1: 'étant celles de (8.13.4), le foncteur L'",
    "the reference (8.13.4) is upright inside the italic statement (crop)", "italic (statement environment)",
    "convention", 6, "high", r"celles de (8.13.4), le foncteur", r"celles de \textup{(8.13.4)}, le foncteur", "")
add(51, "Proposition (8.13.5), l. 2-3: '(ce qui implique déjà que S est quasi-compact et quasi-séparé (1.2.8))'",
    "the whole parenthesis is roman inside the italic statement (crop)", "italic (statement environment)",
    "convention", 6, "high",
    r"(ce qui implique¶déjà que $S$ est quasi-compact et quasi-séparé (1.2.8))",
    r"\textup{(ce qui implique¶déjà que $S$ est quasi-compact et quasi-séparé (1.2.8))}", "")
add(51, "Proposition (8.13.5), end: 'L est une équivalence de catégories.'",
    "'équivalence de catégories' italic like the rest of the statement",
    r"\emph{...} inside the italic environment: upright", "convention", 6, "high",
    r"\emph{équivalence de catégories}", r"équivalence de catégories", "FIX_POLICY 2.6: drop \\emph where the print shows no change of face.")
add(51, "proof of (8.13.5), l. 2: 'quels que soient X, X' dans C', ce qui'", "C bold italic", r"\mathcal C'", "font",
    None, "high", r"dans $\mathcal C'$, ce", r"dans $\boldsymbol{C}'$, ce", SEE)
add(51, "proof of (8.13.5): 'L(X) où X in C' (0_III, 8.1.5).'", "C bold italic", r"\mathcal C'", "font", None, "high",
    r"$\mathbf X\in\mathcal C'$", r"$\mathbf X\in\boldsymbol{C}'$", SEE)
add(51, "proof of (8.13.5): '(0_III, 8.1.5). Or, il y a par hypothèse une factorisation'",
    "'Or, il y a' starts flush left after a full line: same paragraph", "blank line: new paragraph", "other", None,
    "high", r"8.1.5)$.¶¶Or, il y a", r"8.1.5)$.¶Or, il y a",
    "Left edge measured: 'Or,' at the text margin, 'Pour montrer' (paragraph start above) indented.")
add(51, "proof of (8.13.5): 'O_X0-Algèbre quasi-cohérente (II, 1.3.1)'", "bold II", "(II, 1.3.1)", "convention", 2,
    "high", r"(II, 1.3.1)", r"(\textbf{II}, 1.3.1)", "")
add(51, "proof of (8.13.5): 'de type fini (I, 9.6.6)'", "bold I", "(I, 9.6.6)", "convention", 2, "high",
    r"(I, 9.6.6)", r"(\textbf{I}, 9.6.6)", "")
add(51, "proof of (8.13.5): 'les X_lambda appartiennent à C'_0'", "C bold italic", r"\mathcal C'_0", "font", None,
    "high", r"appartiennent à $\mathcal C'_0$ et comme", r"appartiennent à $\boldsymbol{C}'_0$ et comme", SEE)
add(51, "proof of (8.13.5): 'X=(X_lambda) est un objet de C' dont la limite'", "C bold italic", r"\mathcal C'", "font",
    None, "high", r"est un objet de $\mathcal C'$ dont la", r"est un objet de $\boldsymbol{C}'$ dont la", SEE)
add(51, "Remarque (8.13.6), l. 1: 'et de (II, 1.6.2) que si X et Y'", "bold II", "(II, 1.6.2)", "convention", 2,
    "high", r"et de (II, 1.6.2) que", r"et de (\textbf{II}, 1.6.2) que", "")
add(51, "Remarque (8.13.6), l. 3: 'qu'un C-groupe n'est autre'", "C bold italic", r"\mathcal C", "font", None, "high",
    r"qu'un $\mathcal C$", r"qu'un $\boldsymbol{C}$", SEE)
add(51, "Remarque (8.13.6), l. 3: 'qu'un C-groupe n'est autre'", "'groupe' in italics (crop)",
    "roman (judged with the remark body roman)", "italics", None, "high",
    r"-groupe n'est autre", r"-\emph{groupe} n'est autre", "")
add(51, "Remarque (8.13.6), l. 3: 'qu'un (Sch)_/S-groupe qui est'", "Sch bold italic", r"\mathbf{Sch}", "font", None,
    "high", r"$(\mathbf{Sch})_{/S}$", r"$(\boldsymbol{\mathit{Sch}})_{/S}$", SEE)
add(51, "Remarque (8.13.6), l. 3: 'qu'un (Sch)_/S-groupe qui est'", "'groupe' in italics (crop)",
    "roman (judged with the remark body roman)", "italics", None, "high",
    r"-groupe qui¶est un préschéma", r"-\emph{groupe} qui¶est un préschéma", "")
add(51, "Remarque (8.13.6), l. 5: 'existent dans la catégorie C' : en effet'", "C bold italic", r"\mathcal C'", "font",
    None, "high", r"la catégorie $\mathcal C'$~:", r"la catégorie $\boldsymbol{C}'$~:", SEE)
add(51, "Remarque (8.13.6), l. 5: 'sont deux objets de C', les produits'", "C bold italic", r"\mathcal C'", "font",
    None, "high", r"objets de $\mathcal C'$, les produits", r"objets de $\boldsymbol{C}'$, les produits", SEE)
add(51, "Remarque (8.13.6), l. 7: 'pour morphismes de transition X_nu x_S Y_sigma -> X_mu x_S Y_rho les produits'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"pour morphismes de¶transition¶\[¶X_\nu\times_S Y_\sigma\longrightarrow X_\mu\times_S Y_\rho¶\]¶les produits",
    r"pour morphismes de¶transition¶$X_\nu\times_S Y_\sigma\longrightarrow X_\mu\times_S Y_\rho$¶les produits",
    "Layout only (display vs inline).")
add(51, "Remarque (8.13.6), l. 9: 'produit de X et de Y dans Pro(C'_0);'", "Pro and C bold italic",
    r"\mathbf{Pro}(\mathcal C'_0)", "font", None, "high", r"$\mathbf{Pro}(\mathcal C'_0)$~;",
    r"$\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0)$~;", SEE)
add(51, "Remarque (8.13.6), l. 9: 'en outre (II, 1.6.2) les morphismes'", "bold II", "(II, 1.6.2)", "convention", 2,
    "high", r"en outre (II, 1.6.2)", r"en outre (\textbf{II}, 1.6.2)", "")
add(51, "Remarque (8.13.6), l. 10: 'appartient bien à C'. On conclut'", "C bold italic", r"\mathcal C'", "font", None,
    "high", r"bien à¶$\mathcal C'$. On conclut", r"bien à¶$\boldsymbol{C}'$. On conclut", SEE)
add(51, "Remarque (8.13.6), l. 11: 'comme plus haut qu'un C'-groupe est un'", "C bold italic", r"\mathcal C'", "font",
    None, "high", r"haut qu'un $\mathcal C'$", r"haut qu'un $\boldsymbol{C}'$", SEE)
add(51, "Remarque (8.13.6), l. 11: 'qu'un C'-groupe est un'", "'groupe' in italics (crop)",
    "roman (judged with the remark body roman)", "italics", None, "high",
    r"-groupe est¶un", r"-\emph{groupe} est¶un", "")
add(51, "Remarque (8.13.6), l. 11: 'un Pro(C'_0)-groupe qui est essentiellement affine'", "Pro and C bold italic",
    r"\mathbf{Pro}(\mathcal C'_0)", "font", None, "high", r"$\mathbf{Pro}(\mathcal C'_0)$-",
    r"$\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0)$-", SEE)
add(51, "Remarque (8.13.6), l. 11: 'un Pro(C'_0)-groupe qui est essentiellement affine'", "'groupe' in italics (crop)",
    "roman (judged with the remark body roman)", "italics", None, "high",
    r"groupe qui est essentiellement affine. On", r"\emph{groupe} qui est essentiellement affine. On", "")
add(51, "Remarque (8.13.6), l. 12: 'les catégories des C'-groupes et des C-groupes'", "C bold italic (2 times)",
    r"\mathcal C', \mathcal C", "font", None, "high",
    r"catégories des $\mathcal C'$-groupes et des¶$\mathcal C$-groupes",
    r"catégories des $\boldsymbol{C}'$-groupes et des¶$\boldsymbol{C}$-groupes", "'groupes' roman here, as in the TeX. " + SEE)
add(51, "Remarque (8.13.6), l. 14: 'la catégorie des C-groupes soit équivalente'", "C bold italic", r"\mathcal C",
    "font", None, "high", r"la catégorie des $\mathcal C$-groupes soit", r"la catégorie des $\boldsymbol{C}$-groupes soit",
    "'groupes' roman here, as in the TeX. " + SEE)
add(51, "Remarque (8.13.6), l. 14: 'à celle des K-groupes, où K est'", "'groupes' in italics (bold italic K)",
    "roman (judged with the remark body roman)", "italics", None, "high",
    r"$\boldsymbol K$-groupes, où", r"$\boldsymbol K$-\emph{groupes}, où", "")

# ---------------- page 52 ----------------
add(52, "Remarque (8.13.6), p. 52 l. 1: 'par C'_0-gr la catégorie des C'_0-groupes'", "C bold italic (2 times)",
    r"\mathcal C'_0", "font", None, "high",
    r"par $\mathcal C'_0$-$\boldsymbol{gr}$ la catégorie des¶$\mathcal C'_0$-groupes",
    r"par $\boldsymbol{C}'_0$-$\boldsymbol{gr}$ la catégorie des¶$\boldsymbol{C}'_0$-groupes", SEE)
add(52, "Remarque (8.13.6), p. 52 l. 1: 'la catégorie des C'-groupes est équivalente'", "C bold italic",
    r"\mathcal C'", "font", None, "high", r"$\mathcal C'$-groupes est équivalente",
    r"$\boldsymbol{C}'$-groupes est équivalente", SEE)
add(52, "Remarque (8.13.6), p. 52 l. 2: 'sous-catégorie pleine de Pro(C'_0-gr)'", "Pro and C bold italic",
    r"\mathbf{Pro}(\mathcal C'_0\text{-}\boldsymbol{gr})", "font", None, "high",
    r"$\mathbf{Pro}(\mathcal C'_0\text{-}\boldsymbol{gr})$", r"$\boldsymbol{\mathit{Pro}}(\boldsymbol{C}'_0\text{-}\boldsymbol{gr})$",
    SEE)
add(52, "heading 8.14: '... en termes du foncteur qu'il représente.'", "the title ends with a full stop",
    "no full stop", "punctuation", None, "high", r"qu'il représente}", r"qu'il représente.}",
    "As the other subsection-title fixes (GLOBAL_ISSUES 43).")
add(52, "Proposition (8.14.2) b): 'essentiellement affine (8.13.4) et formé'",
    "the reference is upright inside the italic statement (crop)", "italic (statement environment)", "convention", 6,
    "high", r"essentiellement affine (8.13.4) et", r"essentiellement affine \textup{(8.13.4)} et", "")
add(52, "Proposition (8.14.2) b): 'l'application canonique (8.13.1.1)'",
    "the reference is upright inside the italic statement (crop)", "italic (statement environment)", "convention", 6,
    "high", r"l'application canonique (8.13.1.1)", r"l'application canonique \textup{(8.13.1.1)}", "")
add(52, "(8.14.2.1): 'lim h_X(Z_lambda) -> h_X(lim Z_lambda)'",
    "neither lim has an index: only the arrows under 'lim' (enlarged crop)",
    r"\varinjlim_\lambda, \varprojlim_\lambda", "formula", None, "high",
    r"\varinjlim_\lambda h_X(Z_\lambda)¶\longrightarrow h_X(\varprojlim_\lambda Z_\lambda)",
    r"\varinjlim h_X(Z_\lambda)¶\longrightarrow h_X(\varprojlim Z_\lambda)", "Cf. GLOBAL_ISSUES 30.")
add(52, "Proposition (8.14.2) c): 'l'application (8.14.2.1) est bijective'",
    "the reference is upright inside the italic statement (crop)", "italic (statement environment)", "convention", 6,
    "high", r"affines,¶  l'application (8.14.2.1)", r"affines,¶  l'application \textup{(8.14.2.1)}", "")
add(52, "Proposition (8.14.2) c'): 'l'application (8.14.2.1) est bijective'",
    "the reference is upright inside the italic statement (crop)", "italic (statement environment)", "convention", 6,
    "high", r"affines, l'application (8.14.2.1)", r"affines, l'application \textup{(8.14.2.1)}", "")

# ---------------- page 53 ----------------
add(53, "(8.14.2.3): 'lim Hom_A-alg.(B, C_lambda) -> Hom_A-alg.(B, lim C_lambda)'",
    "neither lim has an index: only the arrows (enlarged crop)", r"\varinjlim_\lambda (2 times)", "formula", None,
    "high",
    r"\varinjlim_\lambda\operatorname{Hom}_{A\text{-}\mathrm{alg.}}(B,C_\lambda)¶\longrightarrow¶\operatorname{Hom}_{A\text{-}\mathrm{alg.}}¶(B,\varinjlim_\lambda C_\lambda)",
    r"\varinjlim\operatorname{Hom}_{A\text{-}\mathrm{alg.}}(B,C_\lambda)¶\longrightarrow¶\operatorname{Hom}_{A\text{-}\mathrm{alg.}}¶(B,\varinjlim C_\lambda)",
    "Cf. GLOBAL_ISSUES 30.")
add(53, "proof of (8.14.2.2), l. 2: 'de sorte que lim C_lambda = B'", "lim with the arrow only, no index (crop)",
    r"\varinjlim_\lambda", "formula", None, "high", r"$\varinjlim_\lambda C_\lambda=B$", r"$\varinjlim C_\lambda=B$",
    "Cf. GLOBAL_ISSUES 30.")
add(53, "proof of (8.14.2.2): 'tels que le composé B -u-> C_lambda -p_lambda-> B (où p_lambda ...)'",
    "the composite is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"le composé¶\[¶B\xrightarrow{u}C_\lambda\xrightarrow{p_\lambda}B¶\]¶(où",
    r"le composé¶$B\xrightarrow{u}C_\lambda\xrightarrow{p_\lambda}B$¶(où", "Layout only (display vs inline).")
add(53, "proof of (8.14.2.2): 'autrement dit u(t_i) - q_lambda(T_i) in J/J_lambda. Il existe'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"autrement dit¶\[¶u(t_i)-q_\lambda(T_i)\in\mathfrak J/\mathfrak J_\lambda.¶\]¶Il existe",
    r"autrement dit¶$u(t_i)-q_\lambda(T_i)\in\mathfrak J/\mathfrak J_\lambda$.¶Il existe",
    "Layout only (display vs inline). Apply before the next finding (convention 7), whose 'old' lies inside this edit.")
add(53, "proof of (8.14.2.2): same formula 'u(t_i) — q_lambda(T_i)'", "long dash for the subtraction (crop)",
    "minus sign", "convention", 7, "high", r"u(t_i)-q_\lambda(T_i)\in", r"u(t_i)\setmin q_\lambda(T_i)\in",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7). Apply after the "
    "display fix above (its 'old' is unchanged by that edit).")
add(53, "proof of (8.14.2.2): 'les n éléments u(t_i) — q_lambda(T_i) appartiennent'",
    "long dash for the subtraction", "minus sign", "convention", 7, "high",
    r"$u(t_i)-q_\lambda(T_i)$ appartiennent", r"$u(t_i)\setmin q_\lambda(T_i)$ appartiennent",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(53, "proof of (8.14.2.2): 'on a par suite p_mu lambda(u(t_i)) = p_mu lambda(q_lambda(T_i)) = q_mu(T_i). Remplaçant'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"on a par¶suite¶\[¶p_{\mu\lambda}(u(t_i))¶=p_{\mu\lambda}(q_\lambda(T_i))=q_\mu(T_i).¶\]¶Remplaçant",
    r"on a par¶suite¶$p_{\mu\lambda}(u(t_i))¶=p_{\mu\lambda}(q_\lambda(T_i))=q_\mu(T_i)$.¶Remplaçant",
    "Layout only (display vs inline).")
add(53, "(8.14.2.4): 'lim Hom_S(Z_lambda, V) -> Hom_S(lim Z_lambda, V)'",
    "neither lim has an index: only the arrows (enlarged crop)", r"\varinjlim_\lambda, \varprojlim_\lambda", "formula",
    None, "high",
    r"\varinjlim_\lambda\operatorname{Hom}_S(Z_\lambda,V)¶\longrightarrow¶\operatorname{Hom}_S(\varprojlim_\lambda Z_\lambda,V)",
    r"\varinjlim\operatorname{Hom}_S(Z_\lambda,V)¶\longrightarrow¶\operatorname{Hom}_S(\varprojlim Z_\lambda,V)",
    "Cf. GLOBAL_ISSUES 30.")
add(53, "last display, second chain: 'Z -u_lambda-> Z_lambda -v_lambda-> V -j-> X'",
    "the label of the second arrow is v_lambda without the prime; only a 2-pixel speck where a prime's tip would be "
    "(600-dpi scan; the prime of v'_lambda in the display above is a full wedge)",
    r"v'_\lambda", "misprint_in_print", None, "medium",
    r"\xrightarrow{v'_\lambda}V¶\xrightarrow{j}X", r"\xrightarrow{v_\lambda}V¶\xrightarrow{j}X",
    "The TeX silently corrects. The argument compares j o v_lambda o u_lambda with j o v'_lambda o u_lambda, so the "
    "correct reading is v'_lambda. Medium: a prime lost entirely in printing cannot be excluded.",
    corrected=r"\xrightarrow{v'_\lambda}V¶\xrightarrow{j}X")

# ---------------- page 54 ----------------
add(54, "proof of (8.14.2), surjectivity, l. 3: 'se factorise en Z -u_lambda-> Z_lambda -w_lambda-> X, et tout revient'",
    "the factorisation is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"se factorise en¶\[¶Z\xrightarrow{u_\lambda}Z_\lambda\xrightarrow{w_\lambda}X,¶\]¶et tout revient",
    r"se factorise en¶$Z\xrightarrow{u_\lambda}Z_\lambda\xrightarrow{w_\lambda}X$,¶et tout revient",
    "Layout only (display vs inline).")
add(54, "same proof: 'se factorise en Z_mu -v_mu-> V -j-> X. Posons'",
    "the factorisation is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"se factorise en¶\[¶Z_\mu\xrightarrow{v_\mu}V\xrightarrow{j}X.¶\]¶Posons",
    r"se factorise en¶$Z_\mu\xrightarrow{v_\mu}V\xrightarrow{j}X$.¶Posons", "Layout only (display vs inline).")
add(54, "same proof: 'On a u_mu^-1(U_mu) = ... = v^-1(V) = Z. Comme'",
    "the formula is set inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"On a¶\[¶u_\mu^{-1}(U_\mu)=u_\lambda^{-1}(U_\lambda)¶=u_\lambda^{-1}(w_\lambda^{-1}(V))=v^{-1}(V)=Z.¶\]¶Comme",
    r"On a¶$u_\mu^{-1}(U_\mu)=u_\lambda^{-1}(U_\lambda)¶=u_\lambda^{-1}(w_\lambda^{-1}(V))=v^{-1}(V)=Z$.¶Comme",
    "Layout only (display vs inline).")
add(54, "Remarque (8.14.3): 'qui ne sont pas de type fini (I, 2.4.2)'", "bold I", "(I, 2.4.2)", "convention", 2,
    "high", r"(I, 2.4.2)", r"(\textbf{I}, 2.4.2)", "")
add(54, "§ 9 introduction, l. 4: 'tels que le k(s)-préschéma'", "bold italic k", "plain k", "convention", 1, "high",
    r"$k(s)$-préschéma", r"$\boldsymbol{k}(s)$-préschéma", "ega4-9-fr.tex, before its first page marker.")
add(54, "§ 9 introduction, l. 4: 'X_s = f^-1(s) = X x_S Spec(k(s))'", "bold italic k", "plain k", "convention", 1,
    "high", r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))",
    "ega4-9-fr.tex, before its first page marker.")
add(54, "§ 9 introduction, l. 5: 'F_s = F (x)_O_X k(s)'", "bold italic k", "plain k", "convention", 1, "high",
    r"\otimes_{\mathcal O_X}k(s)", r"\otimes_{\mathcal O_X}\boldsymbol{k}(s)",
    "ega4-9-fr.tex, before its first page marker.")
add(54, "heading 9.1: 'Le principe de l'extension finie.'", "the title ends with a full stop", "no full stop",
    "punctuation", None, "high", r"\subsection{Le principe de l'extension finie}",
    r"\subsection{Le principe de l'extension finie.}",
    "ega4-9-fr.tex, before its first page marker. As the other subsection-title fixes (GLOBAL_ISSUES 43).")
add(54, "Proposition (9.1.1), l. 1: 'Soient k un corps, C un ensemble d'extensions de k'",
    "C bold italic, here and in (i)-(iii) (enlarged crops)", r"\mathcal C (script)", "font", None, "high",
    r"$\mathcal C$ un ensemble d'extensions", r"$\boldsymbol{C}$ un ensemble d'extensions",
    "ega4-9-fr.tex, before its first page marker. Bold italic like the category letter C of 8.13.")
add(54, "Proposition (9.1.1), item labels (i), (ii), (iii)",
    "labels upright (crops)", "enumerate label=(\\roman*) inside the italic statement: italic", "convention", 6, "high",
    r"label=(\roman*)]", r"label=\textup{(\roman*)}]",
    "ega4-9-fr.tex, before its first page marker. One edit for the three labels (GLOBAL_ISSUES 16).")
add(54, "Proposition (9.1.1) (i): 'Si K in C et s'il existe'", "C bold italic", r"\mathcal C", "font", None, "high",
    r"Si $K\in\mathcal C$ et s'il existe", r"Si $K\in\boldsymbol{C}$ et s'il existe",
    "ega4-9-fr.tex, before its first page marker.")
add(54, "Proposition (9.1.1) (i)-(ii): 'alors K' in C. (ii) Si K in C, il existe'", "C bold italic (2 times)",
    r"\mathcal C", "font", None, "high",
    r"$K'\in\mathcal C$.¶  \item Si $K\in\mathcal C$, il existe",
    r"$K'\in\boldsymbol{C}$.¶  \item Si $K\in\boldsymbol{C}$, il existe",
    "ega4-9-fr.tex, before its first page marker.")
add(54, "Proposition (9.1.1) (ii): 'telle que K' in C.'", "C bold italic", r"\mathcal C", "font", None, "high",
    r"telle que $K'\in\mathcal C$.", r"telle que $K'\in\boldsymbol{C}$.", "ega4-9-fr.tex, before its first page marker.")
add(54, "Proposition (9.1.1) (iii): 'Si K in C est le corps de fractions'", "C bold italic", r"\mathcal C", "font",
    None, "high", r"Si $K\in\mathcal C$ est le corps", r"Si $K\in\boldsymbol{C}$ est le corps",
    "ega4-9-fr.tex, before its first page marker.")
add(54, "Proposition (9.1.1) (iii): 'il existe f in A—{0}'", "long dash for the set difference (crop)", "minus sign",
    "convention", 7, "high", r"$f\in A-\{0\}$", r"$f\in A\setmin\{0\}$",
    "ega4-9-fr.tex, before its first page marker. \\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(54, "Proposition (9.1.1) (iii): 'on ait A_f/m in C.'", "C bold italic", r"\mathcal C", "font", None, "high",
    r"$A_f/\mathfrak m\in\mathcal C$", r"$A_f/\mathfrak m\in\boldsymbol{C}$",
    "ega4-9-fr.tex, before its first page marker.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(F), "findings written")
