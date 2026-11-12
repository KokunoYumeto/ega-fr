"""Build findings_265_269.json (pages 265-269, ega4-21a-fr.tex)."""
import json
from pathlib import Path

OUT = Path(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_265_269.json")
F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------------------------------------------------------- page 265
add(265, "proof of (21.3.5): 'l'ensemble fini Ass(O_X)'",
    "'fini' italic (page_265_s1.png)", "roman 'fini'", "italics",
    fx(r"l'ensemble fini $\operatorname{Ass}", r"l'ensemble \emph{fini} $\operatorname{Ass}"))

add(265, "Remarque (21.3.6): 'Montrons que l'homomorphisme composé', after (21.3.6.1)",
    "a new indented paragraph (page_265_s2.png)",
    "no blank line after the display: the sentence continues the paragraph without indent", "other",
    fx("\\tag{21.3.6.1}\n\\]\nMontrons", "\\tag{21.3.6.1}\n\\]\n\nMontrons"),
    "GLOBAL_ISSUES 47 pattern (no blank line after \\] where the print starts an indented paragraph).")

add(265, "Remarque (21.3.6), display 'Div(X) -> H^1(X, O_X^*) -> Pic(X)', second arrow",
    "isomorphism arrow (tilde over the arrow) with pi above the tilde (crop p265_pi.png)",
    r"\xrightarrow{\pi} (no tilde)", "symbol",
    fx(r"\xrightarrow{\pi}\operatorname{Pic}(X)", r"\xrightarrow{\overset{\pi}{\sim}}\operatorname{Pic}(X)"),
    r"Same encoding as the earlier labelled isomorphism arrows (\xrightarrow{\overset{\omega}{\sim}}, IV-4 p. 146).")

add(265, "heading 21.4: 'Images réciproques de diviseurs.'",
    "final full stop (page_265_s2.png)", "no full stop", "punctuation",
    fx(r"\subsection{Images réciproques de diviseurs}", r"\subsection{Images réciproques de diviseurs.}"),
    "GLOBAL_ISSUES 43/58; same form as the earlier IV-4 subsection-title page fixes.")

add(265, "Définition (21.4.2): 'on dit que l'image réciproque par f d'un diviseur D sur X existe'",
    "italic like the rest of the definition (crop p265_def2.png)",
    r"\emph{image réciproque par $f$} inside the italic definition: upright", "convention",
    fx(r"l'\emph{image réciproque par $f$} d'un", r"l'image réciproque par $f$ d'un"), convention=6)

add(265, "Définition (21.4.2): 's_{-D} in Gamma(X, M_f(O_X(—D)))'",
    "long dash before the D of O_X(—D) (crop p265_sminusD.png); the small dash in the subscript of s_{-D} is an ordinary minus",
    "minus sign", "convention",
    fx(r"\sh{O}_X(-D)))$", r"\sh{O}_X(\setmin D)))$"),
    r"Long dash for the minus sign (GLOBAL_ISSUES 23/49); \setmin pending the convention-7 decision. The subscript of s_{-D} is left as it is.",
    convention=7)

add(265, "Définition (21.4.2): '(cf. (20.1.11))'",
    "'(cf.' and the parentheses upright inside the italic definition (crop p265_def2.png)",
    "italic (definition environment)", "convention",
    fx(r"(cf. \sref{IV.20.1.11})", r"\textup{(cf. \sref{IV.20.1.11})}"), convention=6)

add(265, "Définition (21.4.2): 'On appelle alors image réciproque de D par f'",
    "italic like the rest of the definition (crop p265_def2.png)",
    r"\emph{image réciproque} inside the italic definition: upright", "convention",
    fx(r"On appelle alors \emph{image réciproque} de", r"On appelle alors image réciproque de"), convention=6)

add(265, "Définition (21.4.2), last line: '(f^*(O_X(D)), s_D o f)'",
    "the D of O_X(D) is a BOLD upright D (wrong fount): 507 ink pixels against 322 for the D of 'f^*(D)' one line "
    "above, median stroke 7 px against 5 px; the f, parentheses and comma beside it are of normal weight, mid-line "
    "(crops p265_lastline.png, p265_fD.png)",
    "normal D (silent correction)", "misprint_in_print",
    fx(r"(f^*(\sh{O}_X(D)),s_D\circ f)", r"(f^*(\sh{O}_X(\mathbf{D})),s_D\circ f)"),
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). The fix restores the printed reading.",
    corrected=r"(f^*(\sh{O}_X(D)),s_D\circ f)")

add(265, "last paragraph: 'il en est de même de —D et de D+D''",
    "long dash before D, longer than the plus sign of D+D' (crop p265_minusD.png)",
    "minus sign", "convention",
    fx(r"de même de $-D$ et de", r"de même de $\setmin D$ et de"),
    "GLOBAL_ISSUES 23/49.", convention=7)

# ---------------------------------------------------------------- page 266
add(266, "l. 1: 'des diviseurs sur X dont'",
    "the X is a BOLD upright X (wrong fount): 495 ink pixels against 356 for the X of 'Div^f(X)' on the same line; "
    "mid-line, 'dont' after it is of normal weight (crop p266_Xdont.png)",
    "normal X (silent correction)", "misprint_in_print",
    fx(r"des diviseurs sur $X$ dont", r"des diviseurs sur $\mathbf{X}$ dont"),
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). The fix restores the printed reading.",
    corrected=r"des diviseurs sur $X$ dont")

add(266, "l. 2: 'est un sous-groupe de Div(X)'",
    "'sous-groupe' italic (crop p266_l1.png)", "roman", "italics",
    fx(r"existe est un sous-groupe de", r"existe est un \emph{sous-groupe} de"))

add(266, "l. 2: 'l'application D ~> f^*(D) est'",
    "wavy arrow (crop p266_l1.png)", r"\mapsto", "symbol",
    fx(r"$D\mapsto f^*(D)$ est", r"$D\leadsto f^*(D)$ est"),
    "Adjacent to the next finding; no overlap.")

add(266, "l. 3: 'est un homomorphisme croissant du sous-groupe ordonné'",
    "'homomorphisme croissant' italic (crop p266_l1.png)", "roman", "italics",
    fx(r"homomorphisme croissant du sous-groupe", r"\emph{homomorphisme croissant} du sous-groupe"))

add(266, "diagram (21.4.2.1): label l_{X'} of the bottom arrow",
    "the label stands BELOW the arrow (crop p266_diag_bottom.png)", "label above the arrow (^)", "formula",
    fx(r"\ar[r]^{l_{X'}}", r"\ar[r]_{l_{X'}}"),
    "The other three labels are on the printed side already.")

add(266, "(21.4.3): 'noté M_f^{**}'",
    "two asterisks: M_f^{**} (crop p266_Mff.png)", r"\sh{M}_f^* (one asterisk)", "formula",
    fx(r"noté $\sh{M}_f^*$,", r"noté $\sh{M}_f^{**}$,"),
    "The print writes M_f^{**} four times in (21.4.3) (this one, psi^*(M_f^{**}) -> M_{X'}^*, D-iv^f_X = M_f^{**}/O_X^*, "
    "psi^*(M_f^{**})/psi^*(O_X^*)): a consistent notation, not a misprint. Not in the IV-4 errata list.")

add(266, "(21.4.3): 'psi^*(M_f^{**}) -> M_{X'}^*'",
    "two asterisks on M_f (crop p266_Mff.png)", "one asterisk", "formula",
    fx(r"$\psi^*(\sh{M}_f^*)\to\sh{M}_{X'}^*$", r"$\psi^*(\sh{M}_f^{**})\to\sh{M}_{X'}^*$"))

add(266, "(21.4.3): 'Posant D-iv^f_X = M_f^{**}/O_X^*, on a Div^f(X) = Gamma(X, D-iv^f_X)'",
    "script D-iv with superscript f and subscript X, twice (crop p266_divf.png)",
    r"\sh{D}iv_X' (a prime instead of the superscript f), twice", "formula",
    fx(r"Posant $\sh{D}iv_X'=\sh{M}_f^*/\sh{O}_X^*$, on a $\operatorname{Div}^f(X)=\Gamma(X,\sh{D}iv_X')$",
       r"Posant $\sh{D}iv_X^f=\sh{M}_f^{**}/\sh{O}_X^*$, on a $\operatorname{Div}^f(X)=\Gamma(X,\sh{D}iv_X^f)$"),
    "One edit for this finding and the next (the two asterisks of M_f^{**} in the same formula).")

add(266, "(21.4.3): 'D-iv^f_X = M_f^{**}/O_X^*'",
    "two asterisks on M_f (crop p266_divf.png)", "one asterisk", "formula", None,
    "Covered by the edit of the preceding entry.")

add(266, "(21.4.3): 'et l'application D ~> f^*(D) correspond'",
    "wavy arrow (crop p266_divf.png)", r"\mapsto", "symbol",
    fx(r"$D\mapsto f^*(D)$ correspond", r"$D\leadsto f^*(D)$ correspond"))

add(266, "(21.4.3): 'psi^*(M_f^{**})/psi^*(O_X^*) -> M_{X'}^*/O_{X'}^*'",
    "two asterisks on M_f (crop p266_divf.png)", "one asterisk", "formula",
    fx(r"$\psi^*(\sh{M}_f^*)/\psi^*(\sh{O}_X^*)", r"$\psi^*(\sh{M}_f^{**})/\psi^*(\sh{O}_X^*)"))

add(266, "Proposition (21.4.5): labels (i), (ii), (iii)",
    "upright labels inside the italic statement (crop p266_labels.png)", "italic (enumerate label in the italic environment)",
    "convention",
    fx("est définie :\n\\begin{enumerate}[label=(\\roman*)]", "est définie :\n\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
    "GLOBAL_ISSUES 16; one edit covers the three labels (as on p. 259).", convention=6)

add(266, "proof of (21.4.5): 'jointe à (20.2.13, (iv)) assure que'",
    "'(20.2.13, (iv))' with no comma after it (crop p266_iv.png)",
    r"\sref{IV.20.2.13},~(iv), prints '(20.2.13), (iv),'", "punctuation",
    fx(r"\sref{IV.20.2.13},~(iv), assure", r"\sref{IV.20.2.13}[(iv)] assure"),
    "Same form as the p. 264 fix of (20.2.13, (iv)).")

# ---------------------------------------------------------------- page 267
add(267, "Corollaire (21.4.6): labels (i), (ii)",
    "upright labels inside the italic statement (page_267_s1.png)", "italic (enumerate label in the italic environment)",
    "convention",
    fx("ayant l'une des propriétés suivantes :\n\\begin{enumerate}[label=(\\roman*)]",
       "ayant l'une des propriétés suivantes :\n\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
    "GLOBAL_ISSUES 16; one edit covers both labels.", convention=6)

add(267, "(21.4.7): 'le sous-préschéma fermé Y(f^*(D)) de X''",
    "sans-serif Y (heavy, no serifs; crop p267_Yzoom.png)", "$Y(f^*(D))$ (ordinary Y)", "font",
    fx(r"$Y(f^*(D))$ de $X'$", r"$\mathsf{Y}(f^*(D))$ de $X'$"),
    r"The Y(D) notation of (21.2.12) (sans-serif Y); same encoding as the pp. 260-264 fixes (\mathsf{Y}).")

add(267, "(21.4.7): 'l'image réciproque f^{-1}(Y(D))'",
    "sans-serif Y (crop p267_Yzoom2.png)", "$Y(D)$ (ordinary Y)", "font",
    fx(r"$f^{-1}(Y(D))$", r"$f^{-1}(\mathsf{Y}(D))$"),
    "The heavier D)); after it is the line-end heavy impression (item 100), not reported.")

add(267, "Proposition (21.4.8): 'Soient X, Y deux préschémas, f : X -> Y'",
    "comma after 'préschémas' (crop p267_prop8.png)", "semicolon", "punctuation",
    fx("deux préschémas;\n$f:X\\to Y$", "deux préschémas,\n$f:X\\to Y$"))

add(267, "Proposition (21.4.8): '(l'existence de f^*(D) résultant de (21.4.5))'",
    "the whole parenthesis roman, with upright parentheses (crop p267_prop8.png)", "italic (proposition environment)",
    "convention",
    fx(r"(l'existence de $f^*(D)$ résultant de \sref{IV.21.4.5})",
       r"\textup{(l'existence de $f^*(D)$ résultant de \sref{IV.21.4.5})}"), convention=6)

add(267, "Proposition (21.4.8): 'l'application D ~> f^*(D) de Div(Y) dans Div(X)'",
    "wavy arrow (crop p267_prop8.png)", r"\mapsto", "symbol",
    fx(r"$D\mapsto f^*(D)$ de", r"$D\leadsto f^*(D)$ de"))

add(267, "proof of (21.4.8): 'd'où uO_Y ⊂ vO_Y puisque f est surjectif'",
    "no comma after vO_Y at the end of the line (crops p267_vOY.png, p267_vOY2.png)", "comma before 'puisque'",
    "punctuation",
    fx(r"v\sh{O}_Y$, puisque", r"v\sh{O}_Y$ puisque"))

add(267, "heading 21.5: 'Images directes de diviseurs.'",
    "final full stop (page_267_s3.png)", "no full stop", "punctuation",
    fx(r"\subsection{Images directes de diviseurs}", r"\subsection{Images directes de diviseurs.}"),
    "GLOBAL_ISSUES 43/58.")

add(267, "(21.5.1): 'Soient X, X' deux préschémas,'",
    "'préschémas' italic (crop p267_2151.png); in (21.4.7) above the same words are roman",
    "roman", "italics",
    fx("deux préschémas, $f:X'\\to X$ un morphisme.\nNous allons",
       "deux \\emph{préschémas}, $f:X'\\to X$ un morphisme.\nNous allons"))

add(267, "(21.5.1): 'associer à tout diviseur D''",
    "'tout' italic (crop p267_2151.png)", "roman", "italics",
    fx(r"associer à tout diviseur", r"associer à \emph{tout} diviseur"))

add(267, "(21.5.3): 'que le morphisme f : X' -> X soit fini,'",
    "'fini' italic (crop p267_2153a.png)", "roman", "italics",
    fx(r"soit fini, et en outre", r"soit \emph{fini}, et en outre"))

add(267, "(21.5.3): 'que f vérifie l'une des deux propriétés'",
    "'l'une' italic (crop p267_2153a.png)", "roman", "italics",
    fx(r"vérifie l'une des deux", r"vérifie \emph{l'une} des deux"))

add(267, "(21.5.3) I): 'f est un morphisme fini'",
    "'est' printed ITALIC in the roman text (crop p267_fest.png, against the roman 'est' of the next line, "
    "p267_est_roman.png); 'un morphisme fini' after it is roman",
    "roman 'est' (silent correction)", "misprint_in_print",
    fx(r"\item $f$ est un morphisme fini", r"\item $f$ \textit{est} un morphisme fini"),
    "Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29 pattern, as 'de' on p. 113); corrected edition roman.",
    corrected=r"\item $f$ est un morphisme fini")

add(267, "(21.5.3) I): 'f_*(O_X') est localement libre.'",
    "'localement libre' italic (crop p267_est_roman.png)", "roman", "italics",
    fx(r"$f_*(\sh{O}_{X'})$ est localement libre.", r"$f_*(\sh{O}_{X'})$ est \emph{localement libre}."))

# ---------------------------------------------------------------- page 268
add(268, "(21.5.3) II), l. 1: 'N_{f_*(O_X')/O_X}(s') est une section de O_X'",
    "slash between f_*(O_X') and O_X in the subscript, as in N_{X'/X} (crops p268_Nsub.png, p268_top.png)",
    "vertical bar |", "formula",
    fx(r"$\mathrm{N}_{f_*(\sh{O}_{X'})|\sh{O}_X}(s')$ est une section",
       r"$\mathrm{N}_{f_*(\sh{O}_{X'})/\sh{O}_X}(s')$ est une section"),
    "The print writes the norm subscripts with a slash in all five places on pp. 268-269.")

add(268, "(21.5.3) II): 'pour tout morphisme fini f lorsque X'",
    "'tout morphisme fini f' italic (crop p268_top.png)", "roman", "italics",
    fx(r"pour tout morphisme fini $f$ lorsque", r"pour \emph{tout morphisme fini $f$} lorsque"))

add(268, "(21.5.3) II): 'localement noethérien normal (loc. cit.).)'",
    "'normal (loc. cit.)' italic, its parentheses included; the final '.)' roman (crop p268_top.png)",
    r"'normal' roman, upright parentheses around \emph{loc. cit.}", "italics",
    fx(r"noethérien normal (\emph{loc. cit.}).)", r"noethérien \emph{normal (loc. cit.)}.)"))

add(268, "'on définit la norme L = N_{X'/X}(L')'",
    "'norme' italic (crop p268_norme.png)", "roman", "italics",
    fx(r"on définit la norme $\sh{L}", r"on définit la \emph{norme} $\sh{L}"))

add(268, "'et toute section régulière s' in Gamma(f^{-1}(U), O_X')'",
    "'régulière' italic (crop p268_norme.png)", "roman", "italics",
    fx(r"toute section régulière $s'\in", r"toute section \emph{régulière} $s'\in"))

add(268, "'la norme N_{X'/X}(s') = ...'",
    "'norme' italic (crop p268_norme.png)", "roman", "italics",
    fx(r"la norme $\mathrm{N}_{X'/X}(s')", r"la \emph{norme} $\mathrm{N}_{X'/X}(s')"),
    "Adjacent to the next finding; no overlap.")

add(268, "'N_{X'/X}(s') = N_{f_*(O_X')/O_X}(s')'",
    "slash in the subscript (crop p268_Nsub2.png)", "vertical bar |", "formula",
    fx(r"=\mathrm{N}_{f_*(\sh{O}_{X'})|\sh{O}_X}(s')$", r"=\mathrm{N}_{f_*(\sh{O}_{X'})/\sh{O}_X}(s')$"))

add(268, "'est un élément régulier de Gamma(U, O_X)'",
    "'régulier' italic (crop p268_norme.png)", "roman", "italics",
    fx(r"est un élément régulier de $\Gamma(U,\sh{O}_X)$", r"est un élément \emph{régulier} de $\Gamma(U,\sh{O}_X)$"))

add(268, "'et s' est une section régulière dans Gamma(f^{-1}(U), O_X')'",
    "'régulière' italic (crop p268_reg1.png)", "roman", "italics",
    fx(r"est une section régulière dans", r"est une section \emph{régulière} dans"))

add(268, "'si u' est une section méromorphe régulière de L''",
    "'régulière' italic (crop p268_s3.png)", "roman", "italics",
    fx(r"si $u'$ est une section méromorphe régulière de", r"si $u'$ est une section méromorphe \emph{régulière} de"))

add(268, "'N(u') est une section méromorphe régulière de L au-dessus de X'",
    "'régulière' italic (crop p268_s3.png); the 'régulière' of 'N(t') est régulière si t' l'est' is roman",
    "roman", "italics",
    fx(r"$\mathrm{N}(u')$ est une section méromorphe régulière de",
       r"$\mathrm{N}(u')$ est une section méromorphe \emph{régulière} de"))

add(268, "'s'_1 (resp. s'_2) une section méromorphe de L'_1 (resp. L'_2)'",
    "'une section méromorphe de' without 'régulière' (crop p268_s3.png)",
    "'une section méromorphe régulière de' (word added)", "extra",
    fx(r"une section méromorphe régulière de $\sh{L}_1'$", r"une section méromorphe de $\sh{L}_1'$"),
    "Not a misprint: the norm of (21.5.3.1) is defined for every meromorphic section, and (21.5.3.2) holds for them.")

add(268, "(21.5.4): 'qui en outre sont équivalents au sens de (21.2.10)'",
    "'équivalents' italic (crop p268_equiv.png)", "roman", "italics",
    fx(r"sont équivalents au sens de", r"sont \emph{équivalents} au sens de"))

# ---------------------------------------------------------------- page 269
add(269, "Définition (21.5.5): 'l'une des conditions I), II) de (21.5.3)'",
    "the labels I), II) upright inside the italic definition (crop p269_def.png)", "italic (definition environment)",
    "convention",
    fx(r"conditions I), II) de", r"conditions \textup{I), II)} de"), convention=6)

add(269, "Définition (21.5.5): 'on appelle image directe (ou norme) d'un diviseur'",
    "italic like the rest of the definition, the parentheses included (crops p269_def.png, p269_ounorme.png)",
    r"\emph{image directe}, \emph{norme} inside the italic definition: upright", "convention",
    fx(r"on appelle \emph{image directe} (ou \emph{norme}) d'un", r"on appelle image directe (ou norme) d'un"),
    convention=6)

add(269, "Définition (21.5.5): '(ou N_{X'/X}(D'))'",
    "upright parentheses around 'ou N_{X'/X}(D')' ('ou' italic), unlike the italic ones of '(ou norme)' "
    "(side-by-side crop p269_paren_side.png)",
    "italic parentheses (definition environment)", "convention",
    fx(r"(ou $\mathrm{N}_{X'/X}(D')$)", r"\textup{(}ou $\mathrm{N}_{X'/X}(D')$\textup{)}"),
    "GLOBAL_ISSUES 26/101: parentheses around a formula are upright in the print.", convention=6)

add(269, "after (21.5.5.1): 'autrement dit, D' ~> f_*(D') est un'",
    "wavy arrow (crop p269_wavy.png)", r"\mapsto", "symbol",
    fx(r"$D'\mapsto f_*(D')$", r"$D'\leadsto f_*(D')$"))

add(269, "after (21.5.5.1): 'est un homomorphisme croissant du groupe ordonné Div(X')'",
    "'homomorphisme croissant' italic (crop p269_s2a.png)", "roman", "italics",
    fx(r"homomorphisme croissant du groupe ordonné", r"\emph{homomorphisme croissant} du groupe ordonné"))

add(269, "'définissent donc un homomorphisme de faisceaux de groupes ordonnés'",
    "the phrase italic (crop p269_s2a.png)", "roman", "italics",
    fx(r"un homomorphisme de faisceaux de groupes ordonnés", r"un \emph{homomorphisme de faisceaux de groupes ordonnés}"))

add(269, "'En outre, pour tout ouvert U de X', after (21.5.5.2)",
    "a new indented paragraph (page_269_s2.png)",
    "no blank line after the display: no paragraph break, no indent", "other",
    fx("\\tag{21.5.5.2}\n\\]\nEn outre", "\\tag{21.5.5.2}\n\\]\n\nEn outre"),
    "GLOBAL_ISSUES 47 pattern.")

add(269, "Proposition (21.5.7): 'l'une des hypothèses I), II) de (21.5.3)'",
    "the labels I), II) upright inside the italic statement (crop p269_prop7.png)",
    "italic (proposition environment)", "convention",
    fx(r"un morphisme fini vérifiant l'une des hypothèses I), II) de",
       r"un morphisme fini vérifiant l'une des hypothèses \textup{I), II)} de"), convention=6)

add(269, "Lemme (21.5.7.2), last line: 'dans la catégorie des O_X''-Modules inversibles'",
    "O_{X''} with two primes (crop p269_lemma.png)", r"$\sh{O}_X$", "formula",
    fx(r"des $\sh{O}_X$-Modules inversibles.", r"des $\sh{O}_{X''}$-Modules inversibles."),
    "Not treated as a misprint: the isomorphism is functorial in L'', which runs through the invertible "
    "O_X''-Modules, so the printed reading makes sense. No erratum in the IV-4 list.")

add(269, "'compte tenu des définitions de (II, 6.5.2 et 6.5.3) de prouver que'",
    "no comma after the reference (crop p269_comma.png)", "comma after the reference", "punctuation",
    fx(r"6.5.2 et 6.5.3), de prouver", r"6.5.2 et 6.5.3) de prouver"))

add(269, "display (21.5.7.4)",
    "N_{f''_*(O_X'')/O_X}(s) = N_{f_*(O_X')/O_X}(N_{f''_*(O_X'')/f_*(O_X')}(s)): slashes in the three subscripts, "
    "and the inner norm is that of f''_*(O_X'') over f_*(O_X') (crops p269_21574.png, p269_inner.png, p269_first.png)",
    "bars in the subscripts; inner norm written N_{f'_*(O_X'')|O_X'}(s)", "formula",
    fx(r"\mathrm{N}_{f_*''(\sh{O}_{X''})|\sh{O}_X}(s)=\mathrm{N}_{f_*(\sh{O}_{X'})|\sh{O}_X}(\mathrm{N}_{f_*'(\sh{O}_{X''})|\sh{O}_{X'}}(s))",
       r"\mathrm{N}_{f_*''(\sh{O}_{X''})/\sh{O}_X}(s)=\mathrm{N}_{f_*(\sh{O}_{X'})/\sh{O}_X}(\mathrm{N}_{f_*''(\sh{O}_{X''})/f_*(\sh{O}_{X'})}(s))"),
    "The TeX rewrote the inner norm (GLOBAL_ISSUES 102 pattern); the printed form, the norm of the f_*(O_X')-algebra "
    "f''_*(O_X'') = f_*(f'_*(O_X'')), is the transitivity formula as stated over X. Adjacent to the next finding; no overlap.")

add(269, "display (21.5.7.4): end",
    "no full stop after the display (crop p269_end.png); p. 270 begins a new paragraph", "full stop", "punctuation",
    fx(".\n  \\tag{21.5.7.4}", "\n  \\tag{21.5.7.4}"))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(F), "findings written to", OUT)
