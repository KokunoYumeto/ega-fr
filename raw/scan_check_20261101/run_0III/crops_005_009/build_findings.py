"""Build findings_005_009.json for EGA III part 1, chapter 0 (0_III), pp. 5-9, and verify every fix.

The pilcrow sign stands for a line break (LF) in the "old"/"new" strings below.
Checks: every "old" occurs exactly once in its page_NNN.tex (CRLF normalised); the fixes, applied in list order
the way apply_fixes.py does (page segment of the r20 release file, re-located for every finding), all apply.
"""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_0III"
OUT = RUN / "findings_005_009.json"
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega3\ega3-1-fr.tex"

BC = r"\boldsymbol{C}"
ENS = r"\boldsymbol{\mathit{Ens}}"
HOM = r"\boldsymbol{\mathit{Hom}}"

NOTE_CAT = ("The category letter C (also C', C'', C_1, C_2), Ens and the functor categories Hom(C^0, Ens), "
            "Hom(C, Ens) are printed bold italic throughout section 8 (enlarged crops); the TeX has plain $C$, "
            "\\mathrm{Ens}, \\operatorname{Hom}. \\boldsymbol as for K and P in 0_I.")
NOTE_SUB = ("Subscript-size bold C (Hom_C, Hom_C', 1_C1) is printed bold UPRIGHT in this fount (enlarged crops), "
            "hence \\mathbf there and \\boldsymbol at text size.")
NOTE_SHORT = "Bold italic category letter(s) in the print; see the first font finding on p. 5."

F = []


def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=old.replace("¶", "\n"), new=new.replace("¶", "\n")), note=note)
    if corrected is not None:
        d["corrected"] = corrected
    F.append(d)


# ---------------------------------------------------------------- page 5
add(5, "chapter heading", "CHAPITRE O (suite) (1), 'suite' italic", "CHAPITRE 0 (suite), upright", "italics",
    r"CHAPITRE 0 (suite)", r"CHAPITRE 0 (\textit{suite})", "Enlarged crop. The 'O' is the print's figure 0.")
add(5, "footnote (1)", "par le signe 0_I with a bold 0 (subscript roman I)", "$0_{\\mathrm I}$, plain 0",
    "convention", r"signe $0_{\mathrm I}$", r"signe $\mathbf{0}_{\mathrm I}$",
    "Bold 0 of the chapter-0 sign (as in references (0_I, ...)); enlarged crop.", conv=2)
add(5, "(8.1.1), l. 1", "par Ens la catégorie (Ens bold italic)", "$\\mathrm{Ens}$", "font",
    r"par $\mathrm{Ens}$ la catégorie", r"par $" + ENS + r"$ la catégorie", NOTE_CAT)
add(5, "(8.1.1), l. 1", "Soit C une catégorie (C bold italic)", "$C$", "font",
    r"Soit $C$ une", r"Soit $" + BC + r"$ une", NOTE_SHORT)
add(5, "(8.1.1), l. 2", "deux objets X, Y de C, nous poserons", "$C$", "font",
    r"de $C$, nous poserons", r"de $" + BC + r"$, nous poserons", NOTE_SHORT)
add(5, "(8.1.1), l. 3", "u : Y -> Y' dans C, nous désignerons", "$C$", "font",
    r"dans $C$,¶nous désignerons", r"dans $" + BC + r"$,¶nous désignerons", NOTE_SHORT)
add(5, "(8.1.1), l. 5", "h_X : C -> Ens (C, Ens bold italic)", "$h_X:C\\to\\mathrm{Ens}$", "font",
    r"$h_X:C\to\mathrm{Ens}$", r"$h_X:" + BC + r"\to" + ENS + r"$", NOTE_SHORT)
add(5, "(8.1.1), l. 6", "notée Hom(C^0, Ens) (Hom, C, Ens bold italic)", "$\\operatorname{Hom}(C^0,\\mathrm{Ens})$",
    "font", r"notée¶$\operatorname{Hom}(C^0,\mathrm{Ens})$",
    r"notée¶$" + HOM + "(" + BC + "^0," + ENS + ")$",
    NOTE_SHORT + " The parentheses and comma of Hom(C^0, Ens) also look bold; not included in the fix.")
add(5, "(8.1.1), l. 7", "catégorie C^0, duale de la catégorie C, dans la catégorie Ens", "$C^0$, $C$, $\\mathrm{Ens}$",
    "font", r"catégorie $C^0$, duale de la catégorie $C$, dans la catégorie¶$\mathrm{Ens}$",
    r"catégorie $" + BC + r"^0$, duale de la catégorie $" + BC + r"$, dans la catégorie¶$" + ENS + "$", NOTE_SHORT)
add(5, "(8.1.1), last line", "(T, 1.7, d) with italic d", "(T, 1.7, d) upright", "italics",
    r"(T, 1.7, d) et [29])", r"(T, 1.7, \textit{d}) et [29])",
    "Enlarged crop; same style as \\textit{b}) in ega1-1-fr.tex.")
add(5, "(8.1.2), l. 1", "morphisme dans C; pour tout Y in C et", "$C$ twice", "font",
    r"morphisme dans $C$~; pour tout $Y\in C$ et",
    r"morphisme dans $" + BC + r"$~; pour tout $Y\in" + BC + r"$ et", NOTE_SHORT)
add(5, "(8.1.2), l. 5", "u : Y -> Y' dans C, le diagramme", "$C$", "font",
    r"$u:Y\to Y'$ dans $C$, le diagramme", r"$u:Y\to Y'$ dans $" + BC + r"$, le diagramme", NOTE_SHORT)
add(5, "(8.1.2), after the diagram", "la catégorie Hom(C^0, Ens) (T, 1.7, d))", "$\\operatorname{Hom}(C^0,\\mathrm{Ens})$",
    "font", r"catégorie¶$\operatorname{Hom}(C^0,\mathrm{Ens})$",
    r"catégorie¶$" + HOM + "(" + BC + "^0," + ENS + ")$", NOTE_SHORT)
add(5, "(8.1.2), after the diagram", "(T, 1.7, d)) with italic d", "(T, 1.7, d)) upright", "italics",
    r"(T, 1.7, d)). Les", r"(T, 1.7, \textit{d})). Les", "Enlarged crop.")
add(5, "(8.1.2.1)", "h : C -> Hom(C^0, Ens) (C, Hom, C, Ens bold italic)",
    "h:C\\to\\operatorname{Hom}(C^0,\\mathrm{Ens})", "font",
    r"h:C\to\operatorname{Hom}(C^0,\mathrm{Ens})", "h:" + BC + r"\to" + HOM + "(" + BC + "^0," + ENS + ")",
    NOTE_SHORT)
add(5, "(8.1.2.1)", "h : C -> Hom(C^0, Ens). (nothing after it)", "adds ',\\qquad X\\mapsto h_X'", "extra",
    r",\qquad X\mapsto h_X.", r".",
    "The printed display (8.1.2.1) ends with 'Ens).'; the TeX adds 'X |-> h_X'. Enlarged crop. Independent of the "
    "font finding just before (adjacent, not overlapping).")
add(5, "(8.1.3), l. 1-2", "un objet de C, F un foncteur contravariant de C dans Ens", "$C$, $C$, $\\mathrm{Ens}$",
    "font", r"un objet de $C$, $F$ un foncteur contravariant de $C$ dans¶$\mathrm{Ens}$",
    r"un objet de $" + BC + r"$, $F$ un foncteur contravariant de $" + BC + r"$ dans¶$" + ENS + "$", NOTE_SHORT)
add(5, "(8.1.3), l. 2", "(objet de Hom(C^0, Ens))", "$\\operatorname{Hom}(C^0,\\mathrm{Ens})$", "font",
    r"(objet de $\operatorname{Hom}(C^0,\mathrm{Ens})$)", r"(objet de $" + HOM + "(" + BC + "^0," + ENS + ")$)",
    NOTE_SHORT)
add(5, "(8.1.3), last line", "pour tout Y in C,", "$Y\\in C$", "font",
    r"fonctoriel}~: pour tout $Y\in C$,", r"fonctoriel}~: pour tout $Y\in" + BC + "$,", NOTE_SHORT)

# ---------------------------------------------------------------- page 6
add(6, "(8.1.3), l. 2", "u : Y -> Y' dans C, le diagramme", "$C$", "font",
    r"$u:Y\to Y'$ dans $C$, le diagramme", r"$u:Y\to Y'$ dans $" + BC + r"$, le diagramme", NOTE_CAT)
add(6, "(8.1.3), 'Inversement'", "v : Y -> X dans C, F(v)", "$C$", "font",
    r"$v:Y\to X$ dans $C$, $F(v)$", r"$v:Y\to X$ dans $" + BC + r"$, $F(v)$", NOTE_SHORT)
add(6, "(8.1.3), after (8.1.3.5)", "u : Y -> Y' dans C, (F(vu))(xi)", "$C$", "font",
    r"dans $C$,¶$(F(vu))", r"dans $" + BC + r"$,¶$(F(vu))", NOTE_SHORT)
add(6, "proof of (8.1.4), l. 1", "pour tout Y in C, (beta(xi))(Y)", "$Y\\in C$", "font",
    r"$\xi\in F(X)$~; pour tout $Y\in C$,", r"$\xi\in F(X)$~; pour tout $Y\in" + BC + "$,", NOTE_SHORT)
add(6, "proof of (8.1.4), 'Calculons maintenant'", "g in Hom(h_X, F); pour tout Y in C,", "$Y\\in C$", "font",
    r"$g\in\operatorname{Hom}(h_X,F)$~; pour tout $Y\in C$,",
    r"$g\in\operatorname{Hom}(h_X,F)$~; pour tout $Y\in" + BC + "$,", NOTE_SHORT)
add(6, "(8.1.5), l. 1", "sous-catégorie C' d'une catégorie C", "$C'$, $C$", "font",
    r"\emph{sous-catégorie} $C'$ d'une catégorie $C$ est",
    r"\emph{sous-catégorie} $" + BC + r"'$ d'une catégorie $" + BC + "$ est", NOTE_SHORT)
add(6, "(8.1.5), l. 2", "des objets de C, et que si", "$C$", "font",
    r"des objets de $C$, et que si", r"des objets de $" + BC + "$, et que si", NOTE_SHORT)
add(6, "(8.1.5), l. 2", "deux objets de C', l'ensemble", "$C'$", "font",
    r"deux objets de $C'$, l'ensemble", r"deux objets de $" + BC + "'$, l'ensemble", NOTE_SHORT)
add(6, "(8.1.5), l. 3", "Hom_C'(X', Y') (bold upright subscript C) ... dans C' (bold italic)",
    "$\\operatorname{Hom}_{C'}$, $C'$", "font",
    r"$\operatorname{Hom}_{C'}(X',Y')$ des morphismes $X'\to Y'$ \emph{dans¶$C'$}",
    r"$\operatorname{Hom}_{\mathbf{C}'}(X',Y')$ des morphismes $X'\to Y'$ \emph{dans¶$" + BC + "'$}", NOTE_SUB)
add(6, "(8.1.5), l. 4", "Hom_C(X', Y') (bold upright subscript C) ... dans C (bold italic)",
    "$\\operatorname{Hom}_C$, $C$", "font",
    r"$\operatorname{Hom}_C(X',Y')$ des¶morphismes $X'\to Y'$ \emph{dans $C$}",
    r"$\operatorname{Hom}_{\mathbf{C}}(X',Y')$ des¶morphismes $X'\to Y'$ \emph{dans $" + BC + "$}", NOTE_SUB)
add(6, "(8.1.5), display", "Hom_C'(X', Y') x Hom_C'(Y', Z') -> Hom_C'(X', Z') (bold upright subscripts)",
    "\\operatorname{Hom}_{C'} three times", "font",
    r"\operatorname{Hom}_{C'}(X',Y')\times\operatorname{Hom}_{C'}(Y',Z')¶  \to\operatorname{Hom}_{C'}(X',Z')",
    r"\operatorname{Hom}_{\mathbf{C}'}(X',Y')\times\operatorname{Hom}_{\mathbf{C}'}(Y',Z')¶  "
    r"\to\operatorname{Hom}_{\mathbf{C}'}(X',Z')", NOTE_SUB)

# ---------------------------------------------------------------- page 7
add(7, "(8.1.5), display at the top", "Hom_C(X', Y') x Hom_C(Y', Z') -> Hom_C(X', Z'). (bold upright subscripts)",
    "\\operatorname{Hom}_C three times", "font",
    r"\operatorname{Hom}_C(X',Y')\times\operatorname{Hom}_C(Y',Z')¶  \to\operatorname{Hom}_C(X',Z').",
    r"\operatorname{Hom}_{\mathbf{C}}(X',Y')\times\operatorname{Hom}_{\mathbf{C}}(Y',Z')¶  "
    r"\to\operatorname{Hom}_{\mathbf{C}}(X',Z').", NOTE_CAT + " " + NOTE_SUB)
add(7, "(8.1.5), 'On dit que'", "On dit que C' est une", "$C'$", "font",
    r"On dit que $C'$ est une", r"On dit que $" + BC + "'$ est une", NOTE_SHORT)
add(7, "(8.1.5), 'On dit que'", "sous-catégorie pleine: only 'pleine' italic", "\\emph{sous-catégorie pleine}",
    "italics", r"\emph{sous-catégorie pleine}", r"sous-catégorie \emph{pleine}", "Enlarged crop.")
add(7, "(8.1.5), 'On dit que'", "de C si Hom_C'(X', Y') = Hom_C(X', Y') pour tout couple d'objets de C'",
    "$C$, subscripts $C'$, $C$, $C'$", "font",
    r"de $C$ si¶$\operatorname{Hom}_{C'}(X',Y')=\operatorname{Hom}_C(X',Y')$ pour tout¶couple d'objets de $C'$.",
    r"de $" + BC + r"$ si¶$\operatorname{Hom}_{\mathbf{C}'}(X',Y')=\operatorname{Hom}_{\mathbf{C}}(X',Y')$ pour "
    r"tout¶couple d'objets de $" + BC + "'$.", NOTE_SUB)
add(7, "(8.1.5), 'La sous-catégorie C''", "La sous-catégorie C'' de C formée des objets de C ... de C'",
    "$C''$, $C$, $C$, $C'$", "font",
    r"La sous-catégorie $C''$ de $C$ formée des objets de¶$C$ isomorphes aux objets de $C'$ est",
    r"La sous-catégorie $" + BC + r"''$ de $" + BC + r"$ formée des objets de¶$" + BC +
    r"$ isomorphes aux objets de $" + BC + "'$ est", NOTE_SHORT)
add(7, "(8.1.5), 'La sous-catégorie C''", "pleine de C, équivalente (T, 1.2) à C'", "$C$, $C'$", "font",
    r"pleine¶de $C$, \emph{équivalente} (T, 1.2) à $C'$ comme",
    r"pleine¶de $" + BC + r"$, \emph{équivalente} (T, 1.2) à $" + BC + "'$ comme", NOTE_SHORT)
add(7, "(8.1.5), 'Un foncteur covariant'", "F : C_1 -> C_2", "$F:C_1\\to C_2$", "font",
    r"$F:C_1\to C_2$", r"$F:" + BC + r"_1\to" + BC + "_2$", NOTE_SHORT)
add(7, "(8.1.5), 'Un foncteur covariant'", "X_1, Y_1 de C_1, l'application", "$C_1$", "font",
    r"$Y_1$ de $C_1$, l'application", r"$Y_1$ de $" + BC + "_1$, l'application", NOTE_SHORT)
add(7, "(8.1.5), 'Un foncteur covariant'", "la sous-catégorie F(C_1) de C_2 est pleine", "$F(C_1)$, $C_2$", "font",
    r"la sous-catégorie $F(C_1)$ de $C_2$ est", r"la sous-catégorie $F(" + BC + r"_1)$ de $" + BC + "_2$ est",
    NOTE_SHORT)
add(7, "(8.1.5), 'Pour tout objet X_2'", "objet X_2 de F(C_1),", "$F(C_1)$", "font",
    r"objet $X_2$ de $F(C_1)$,", r"objet $X_2$ de $F(" + BC + "_1)$,", NOTE_SHORT)
add(7, "(8.1.5), 'Pour tout objet X_2'", "un des objets X_1 de C_1 tel que", "$C_1$", "font",
    r"des objets $X_1$ de $C_1$ tel que", r"des objets $X_1$ de $" + BC + "_1$ tel que", NOTE_SHORT)
add(7, "(8.1.5), 'pour tout morphisme v'", "v : X_2 -> Y_2 dans F(C_1), G(v)", "$F(C_1)$", "font",
    r"dans $F(C_1)$, $G(v)$", r"dans $F(" + BC + r"_1)$, $G(v)$", NOTE_SHORT)
add(7, "(8.1.5), 'G est alors un foncteur'", "de F(C_1) dans C_1; FG ... dans F(C_1)", "$F(C_1)$, $C_1$, $F(C_1)$",
    "font", r"$F(C_1)$ dans $C_1$~; $FG$ est le foncteur identique dans $F(C_1)$, et ce",
    r"$F(" + BC + r"_1)$ dans $" + BC + r"_1$~; $FG$ est le foncteur identique dans $F(" + BC + "_1)$, et ce",
    NOTE_SHORT)
add(7, "(8.1.5), isomorphism phi", "phi : 1_C1 -> GF: bold italic 1 (identity functor), bold upright subscript C_1",
    "$\\varphi:1_{C_1}\\to GF$", "font",
    r"$\varphi:1_{C_1}\to GF$", r"$\varphi:\boldsymbol{\mathit{1}}_{\mathbf{C}_1}\to GF$",
    "Enlarged crop: the identity functor 1 is a bold italic lining 1 (the identity morphism 1_X2 just before is "
    "the ordinary old-style 1). " + NOTE_SUB)
add(7, "(8.1.5), l'identité", "1_F(C_1) -> FG: bold italic 1, subscript F(C_1) with bold upright C",
    "$1_{F(C_1)}\\to FG$", "font",
    r"$1_{F(C_1)}\to FG$", r"$\boldsymbol{\mathit{1}}_{F(\mathbf{C}_1)}\to FG$", "Enlarged crop. " + NOTE_SUB)
add(7, "(8.1.5), last lines", "de la catégorie C_1 et de la sous-catégorie pleine F(C_1) de C_2 (T, 1.2).",
    "$C_1$, $F(C_1)$, $C_2$", "font",
    r"la catégorie $C_1$¶et de la sous-catégorie pleine $F(C_1)$ de $C_2$ (T, 1.2).",
    r"la catégorie $" + BC + r"_1$¶et de la sous-catégorie pleine $F(" + BC + r"_1)$ de $" + BC + "_2$ (T, 1.2).",
    NOTE_SHORT)
add(7, "(8.1.6), l. 2", "objet quelconque de C;", "$C$", "font",
    r"objet quelconque de $C$~;", r"objet quelconque de $" + BC + "$~;", NOTE_SHORT)
add(7, "Proposition (8.1.7)", "h : C -> Hom(C^0, Ens) est pleinement fidèle", "$h:C\\to\\operatorname{Hom}(C^0,\\mathrm{Ens})$",
    "font", r"$h:C\to\operatorname{Hom}(C^0,\mathrm{Ens})$ est pleinement",
    r"$h:" + BC + r"\to" + HOM + "(" + BC + "^0," + ENS + ")$ est pleinement", NOTE_SHORT)
add(7, "(8.1.8), l. 1", "foncteur contravariant de C dans Ens;", "$C$, $\\mathrm{Ens}$", "font",
    r"Soit $F$ un foncteur contravariant de $C$ dans $\mathrm{Ens}$~;",
    r"Soit $F$ un foncteur contravariant de $" + BC + "$ dans $" + ENS + "$~;", NOTE_SHORT)
add(7, "(8.1.8), l. 2", "un objet X in C tel que F soit", "$X\\in C$", "font",
    r"un objet $X\in C$ tel que $F$ soit", r"un objet $X\in" + BC + "$ tel que $F$ soit", NOTE_SHORT)
add(7, "(8.1.8), l. 3", "la donnée d'un X in C et d'un", "$X\\in C$", "font",
    r"d'un $X\in C$ et d'un", r"d'un $X\in" + BC + "$ et d'un", NOTE_SHORT)
add(7, "(8.1.8), l. 5", "équivalence de C et de la sous-catégorie pleine de Hom(C^0, Ens)",
    "$C$, $\\operatorname{Hom}(C^0,\\mathrm{Ens})$", "font",
    r"\emph{équivalence} de $C$ et de la sous-catégorie pleine de¶$\operatorname{Hom}(C^0,\mathrm{Ens})$ formée",
    r"\emph{équivalence} de $" + BC + r"$ et de la sous-catégorie pleine de¶$" + HOM + "(" + BC + "^0," + ENS +
    ")$ formée", NOTE_SHORT)
add(7, "(8.1.8), italic condition", "pour tout objet Y de C l'application", "$C$", "font",
    r"objet $Y$ de $C$ l'application", r"objet $Y$ de $" + BC + "$ l'application", NOTE_SHORT)
add(7, "(8.1.8), 'Par abus de langage'", "l'objet X in C représente F", "$X\\in C$", "font",
    r"l'objet $X\in C$ représente", r"l'objet $X\in" + BC + "$ représente", NOTE_SHORT)
add(7, "(8.1.8), 'Soient F, F''", "représentables de C dans Ens,", "$C$, $\\mathrm{Ens}$", "font",
    r"représentables de $C$ dans¶$\mathrm{Ens}$, $h_X\to F$",
    r"représentables de $" + BC + r"$ dans¶$" + ENS + r"$, $h_X\to F$", NOTE_SHORT)

# ---------------------------------------------------------------- page 8
add(8, "(8.1.9), l. 3", "dans une catégorie C, on définit", "$C$", "font",
    r"dans une catégorie $C$, on définit", r"dans une catégorie $" + BC + "$, on définit", NOTE_CAT)
add(8, "(8.1.9), l. 4", "d'objets de C, et,", "$C$", "font",
    r"d'objets de $C$, et, pour tout", r"d'objets de $" + BC + "$, et, pour tout", NOTE_SHORT)
add(8, "(8.1.9), l. 6", "ce système dans C ... un objet B de C (noté", "$C$ twice", "font",
    r"système dans $C$ est constituée par un objet $B$ de $C$ (noté",
    r"système dans $" + BC + r"$ est constituée par un objet $B$ de $" + BC + "$ (noté", NOTE_SHORT)
add(8, "(8.1.9), 2°", "Pour tout objet X de C et toute famille", "$C$", "font",
    r"Pour tout objet $X$ de $C$ et toute famille", r"Pour tout objet $X$ de $" + BC + "$ et toute famille",
    NOTE_SHORT)
add(8, "(8.1.9), 'il est clair que'", "X ~> lim<- Hom(X, A_alpha) with no index under lim",
    "\\varprojlim_\\alpha", "formula",
    r"$X\mapsto\varprojlim_\alpha\operatorname{Hom}(X,A_\alpha)$ est un",
    r"$X\mapsto\varprojlim\operatorname{Hom}(X,A_\alpha)$ est un",
    "Enlarged crop: only the first lim of the sentence ('l'ensemble lim_alpha Hom(X, A_alpha)') has the alpha "
    "under the arrow; this one, the display (8.1.9.1) and the last line of (8.1.9) have none (cf. GLOBAL_ISSUES 30).")
add(8, "(8.1.9), 'foncteur contravariant'", "de C dans Ens, et l'existence", "$C$, $\\mathrm{Ens}$", "font",
    r"de $C$ dans $\mathrm{Ens}$, et l'existence", r"de $" + BC + "$ dans $" + ENS + "$, et l'existence",
    NOTE_SHORT)
add(8, "(8.1.9.1)", "lim<- Hom(X, A_alpha) ~-> Hom(X, B), no index under lim", "\\varprojlim_\\alpha", "formula",
    r"\varprojlim_\alpha\operatorname{Hom}(X,A_\alpha)¶  \xrightarrow{\sim}",
    r"\varprojlim\operatorname{Hom}(X,A_\alpha)¶  \xrightarrow{\sim}", "Enlarged crop.")
add(8, "(8.1.9), last line", "le foncteur X ~> lim<- Hom (X, A_alpha), no index under lim", "\\varprojlim_\\alpha",
    "formula", r"\varprojlim_\alpha\operatorname{Hom}(X,A_\alpha)$ est¶\emph{représentable}",
    r"\varprojlim\operatorname{Hom}(X,A_\alpha)$ est¶\emph{représentable}", "Enlarged crop.")
add(8, "(8.1.10), l. 1", "Soient C une catégorie", "$C$", "font",
    r"Soient $C$ une catégorie", r"Soient $" + BC + "$ une catégorie", NOTE_SHORT)
add(8, "(8.1.10), l. 2-3", "F : C -> Ens qui, à tout objet X de C", "$C$, $\\mathrm{Ens}$, $C$", "font",
    r"$F:C\to\mathrm{Ens}$ qui, à tout objet $X$ de $C$ fait",
    r"$F:" + BC + r"\to" + ENS + r"$ qui, à tout objet $X$ de $" + BC + "$ fait", NOTE_SHORT)
add(8, "(8.1.10), l. 3", "X -> X' dans C l'unique", "$C$", "font",
    r"$X\to X'$ dans $C$ l'unique", r"$X\to X'$ dans $" + BC + "$ l'unique", NOTE_SHORT)
add(8, "(8.1.10), objet final", "un objet e in C ... Y in C, Hom(Y, e) = h_e(Y): e bold italic, subscript e bold upright",
    "$e\\in C$, $Y\\in C$, $\\operatorname{Hom}(Y,e)=h_e(Y)$", "font",
    r"un objet $e\in C$ tel que pour tout $Y\in C$,¶$\operatorname{Hom}(Y,e)=h_e(Y)$",
    r"un objet $\boldsymbol{e}\in" + BC + r"$ tel que pour tout $Y\in" + BC +
    r"$,¶$\operatorname{Hom}(Y,\boldsymbol{e})=h_{\mathbf{e}}(Y)$",
    "Enlarged crops: the final object e is printed bold italic at text size and bold upright as a subscript; "
    "C bold italic as everywhere in section 8.")
add(8, "(8.1.10), objet final", "on dit que e est un objet final de C, ... deux objets finaux de C",
    "$e$, $C$, $C$", "font",
    r"que $e$ est un \emph{objet final} de $C$, et il est clair que deux objets¶finaux de $C$ sont",
    r"que $\boldsymbol{e}$ est un \emph{objet final} de $" + BC + r"$, et il est clair que deux objets¶finaux de $" +
    BC + "$ sont", NOTE_SHORT + " Bold italic e as in the previous finding.")
add(8, "(8.1.10), l'axiome de choix", "un objet final, 'un' italic", "un (upright)", "italics",
    r"choix, un objet", r"choix, \emph{un} objet", "Enlarged crop.")
add(8, "(8.1.10), e_C", "un objet final de C qu'on note alors e_C (e bold italic, subscript C bold upright)",
    "$C$, $e_C$", "font",
    r"final de $C$ qu'on note alors $e_C$",
    r"final de $" + BC + r"$ qu'on note alors $\boldsymbol{e}_{\mathbf{C}}$", "Enlarged crop. " + NOTE_SUB)
add(8, "(8.1.10), Par exemple", "dans la catégorie Ens, les objets finaux", "$\\mathrm{Ens}$", "font",
    r"dans la catégorie $\mathrm{Ens}$, les objets finaux", r"dans la catégorie $" + ENS + "$, les objets finaux",
    NOTE_SHORT)
add(8, "(8.1.10), last line", "(I, 2.5.1) with bold I", "(I, 2.5.1)", "convention",
    r"(I, 2.5.1)", r"(\textbf{I}, 2.5.1)", "Bold chapter numeral (GLOBAL_ISSUES 4); enlarged crop.", conv=2)
add(8, "(8.1.11), l. 1", "d'une catégorie C, posons", "$C$", "font",
    r"d'une catégorie $C$, posons", r"d'une catégorie $" + BC + "$, posons", NOTE_SHORT)
add(8, "(8.1.11), l. 2", "soit h_X(u) l'application v ~> uv (no prime on h)", "$h'_X(u)$", "misprint_in_print",
    r"soit¶$h'_X(u)$", r"soit¶$h_X(u)$",
    "The print drops the prime: the map v |-> uv from Hom(X, Y) to Hom(X, Y') is h'_X(u) (h'_X(Y) = Hom(X, Y) is "
    "defined in the same sentence; h_X(u) of (8.1.1) goes the other way). Checked on a 4x crop; h'_X(Y) on the line "
    "above has its prime. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$h'_X(u)$")
add(8, "(8.1.11), l. 4", "foncteur covariant C -> Ens", "$C\\to\\mathrm{Ens}$", "font",
    r"$C\to\mathrm{Ens}$, d'où", "$" + BC + r"\to" + ENS + "$, d'où", NOTE_SHORT)
add(8, "(8.1.11), l. 5", "h' : C^0 -> Hom(C, Ens)", "$h':C^0\\to\\operatorname{Hom}(C,\\mathrm{Ens})$", "font",
    r"$h':C^0\to\operatorname{Hom}(C,\mathrm{Ens})$",
    r"$h':" + BC + r"^0\to" + HOM + "(" + BC + "," + ENS + ")$", NOTE_SHORT)
add(8, "(8.1.11), l. 6", "un foncteur covariant: only 'covariant' italic", "\\emph{foncteur covariant}", "italics",
    r"un \emph{foncteur¶covariant} $F$", r"un foncteur¶\emph{covariant} $F$", "Enlarged crop.")
add(8, "(8.1.11), l. 6-7", "F de C dans Ens, autrement dit un objet de Hom(C, Ens)",
    "$C$, $\\mathrm{Ens}$, $\\operatorname{Hom}(C,\\mathrm{Ens})$", "font",
    r"de $C$ dans $\mathrm{Ens}$, autrement dit un objet de¶$\operatorname{Hom}(C,\mathrm{Ens})$",
    r"de $" + BC + "$ dans $" + ENS + r"$, autrement dit un objet de¶$" + HOM + "(" + BC + "," + ENS + ")$",
    NOTE_SHORT)
add(8, "(8.1.11), l. 8", "un objet X in C (nécessairement", "$X\\in C$", "font",
    r"un objet $X\in C$ (nécessairement", r"un objet $X\in" + BC + "$ (nécessairement", NOTE_SHORT)
add(8, "end of the p. 8 segment (heading 8.2 and the opening of (8.2.1))",
    "p. 8 ends with (8.1.11) '... solution de problème universel ».'; the heading '8.2. Structures algébriques "
    "dans les catégories.' and (8.2.1) begin printed p. 9",
    "\\subsection{Structures algébriques ...} and \\begin{env}[8.2.1] stand before \\oldpage[0\\textsubscript{III}]{9}",
    "marker",
    r"\subsection{Structures algébriques dans les catégories}¶\label{subsection:0.8.2-fr}¶¶\begin{env}[8.2.1]¶"
    r"\label{0.8.2.1-fr}¶", "",
    "Two-part move (the heading moves, not the marker, so each edit stays inside its own page segment and the "
    "order does not matter): this edit deletes the 8.2 heading and the (8.2.1) env opening from the end of p. 8; "
    "the p. 9 marker finding re-inserts them after \\oldpage[0\\textsubscript{III}]{9}. Apply both or neither.")

# ---------------------------------------------------------------- page 9
add(9, "top of p. 9", "p. 9 begins with the heading '8.2. Structures algébriques dans les catégories.' and (8.2.1)",
    "the marker stands after the heading and \\begin{env}[8.2.1]", "marker",
    r"\oldpage[0\textsubscript{III}]{9}¶Étant donnés",
    r"\oldpage[0\textsubscript{III}]{9}¶\subsection{Structures algébriques dans les catégories}¶"
    r"\label{subsection:0.8.2-fr}¶¶\begin{env}[8.2.1]¶\label{0.8.2.1-fr}¶Étant donnés",
    "Second half of the move begun by the p. 8 marker finding (which deletes these lines before the marker). "
    "Apply both or neither.")
add(9, "(8.2.1), l. 1-2", "F, F' de C dans Ens, ... pour tout objet Y in C, on pose", "$C$, $\\mathrm{Ens}$, $C$",
    "font", r"$F'$ de $C$ dans¶$\mathrm{Ens}$, rappelons que pour tout objet $Y\in C$, on pose",
    r"$F'$ de $" + BC + r"$ dans¶$" + ENS + r"$, rappelons que pour tout objet $Y\in" + BC + "$, on pose",
    NOTE_CAT)
add(9, "(8.2.1), l. 3", "u : Y -> Y' dans C, on pose", "$C$", "font",
    r"dans¶$C$, on pose", r"dans¶$" + BC + "$, on pose", NOTE_SHORT)
add(9, "(8.2.1), l. 4", "(t, t') ~> (F(u)(t), F'(u)(t'))", "((F(u))(t),(F'(u))(t'))", "formula",
    r"$(t,t')\mapsto((F(u))(t),(F'(u))(t'))$", r"$(t,t')\mapsto(F(u)(t),F'(u)(t'))$",
    "The print has no parentheses around F(u) and F'(u); enlarged crop.")
add(9, "(8.2.1), l. 5", "F x F' : C -> Ens", "$F\\times F':C\\to\\mathrm{Ens}$", "font",
    r"$F\times F':C\to\mathrm{Ens}$", r"$F\times F':" + BC + r"\to" + ENS + "$", NOTE_SHORT)
add(9, "(8.2.1), l. 7", "la catégorie Hom(C^0, Ens)). Étant donné un objet X in C,",
    "$\\operatorname{Hom}(C^0,\\mathrm{Ens})$, $X\\in C$", "font",
    r"$\operatorname{Hom}(C^0,\mathrm{Ens})$). Étant donné un objet $X\in C$, nous",
    r"$" + HOM + "(" + BC + "^0," + ENS + r")$). Étant donné un objet $X\in" + BC + "$, nous", NOTE_SHORT)
add(9, "(8.2.1), l. 7-8", "loi de composition interne (italic) sur X (roman)", "\\emph{loi de composition interne sur $X$}",
    "italics", r"\emph{loi de composition interne sur $X$}", r"\emph{loi de composition interne} sur $X$",
    "Enlarged crop: 'sur' is upright.")
add(9, "(8.2.1), l. 8", "un morphisme fonctoriel (italic)", "morphisme fonctoriel upright", "italics",
    r"un morphisme fonctoriel¶\[¶  \gamma_X", r"un \emph{morphisme fonctoriel}¶\[¶  \gamma_X", "Enlarged crop.")
add(9, "(8.2.1), 'Autrement dit'", "pour tout objet Y in C, gamma_X(Y)", "$Y\\in C$", "font",
    r"pour tout objet $Y\in C$, $\gamma_X(Y)$", r"pour tout objet $Y\in" + BC + r"$, $\gamma_X(Y)$", NOTE_SHORT)
add(9, "(8.2.1), before the diagram", "u : Y -> Y' dans C, le diagramme", "$C$", "font",
    r"$u:Y\to Y'$ dans $C$, le diagramme", r"$u:Y\to Y'$ dans $" + BC + r"$, le diagramme", NOTE_SHORT)
add(9, "(8.2.1), 'De la même façon'", "deux objets Z, X de C, on appelle", "$C$", "font",
    r"$Z$, $X$ de $C$, on appelle", r"$Z$, $X$ de $" + BC + "$, on appelle", NOTE_SHORT)
add(9, "(8.2.1), 'On voit comme ci-dessus'", "pour tout Y in C, omega_X,Z(Y)", "$Y\\in C$", "font",
    r"ci-dessus que pour tout $Y\in C$,", r"ci-dessus que pour tout $Y\in" + BC + "$,", NOTE_SHORT)
add(9, "(8.2.2), l. 1", "un second objet de C, et supposons", "$C$", "font",
    r"un second objet de $C$, et supposons", r"un second objet de $" + BC + "$, et supposons", NOTE_SHORT)
add(9, "(8.2.2), l. 2", "w : X -> X' dans C est un", "$C$", "font",
    r"$w:X\to X'$ dans $C$ est un", r"$w:X\to X'$ dans $" + BC + "$ est un", NOTE_SHORT)
add(9, "(8.2.2), l. 3", "si pour tout Y in C, h_w(Y)", "$Y\\in C$", "font",
    r"si pour tout $Y\in C$, $h_w(Y)", r"si pour tout $Y\in" + BC + r"$, $h_w(Y)", NOTE_SHORT)
add(9, "(8.2.2), l. 4", "est un homomorphisme (italic) pour les lois de composition", "homomorphisme upright",
    "italics", r"est un¶homomorphisme pour les lois", r"est un¶\emph{homomorphisme} pour les lois", "Enlarged crop.")

# ---------------------------------------------------------------- checks
pages = {p: (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(5, 10)}
bad = 0
for x in F:
    if x["fix"] is None:
        continue
    n = pages[x["page"]].count(x["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], n, repr(x["fix"]["old"]))

# simulate apply_fixes.py on the release file (segments re-located per finding)
t = REL.read_text(encoding="utf-8")
mk = re.compile(r"\\oldpage\[0\\textsubscript\{III\}\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in mk.finditer(text)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, cuts[i + 1][1] if i + 1 < len(cuts) else len(text)
    return None, None


applied = 0
for x in F:
    if x["fix"] is None:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("SIM FAIL", x["page"], c, repr(x["fix"]["old"]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
    applied += 1
# the marker of p. 9 must now stand right before the 8.2 heading
k = t.find(r"\oldpage[0\textsubscript{III}]{9}")
print("after marker 9:", repr(t[k:k + 90]))
print("end of p. 8:", repr(t[k - 60:k]))
print("findings", len(F), "simulated applied", applied, "problems", bad)
cnt = {}
for x in F:
    c = cnt.setdefault(x["page"], [0, 0, 0])
    c[2 if x["kind"] == "misprint_in_print" else 1 if x["kind"] == "convention" else 0] += 1
print("per page normal/convention/misprint:", cnt)
if bad == 0:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
    # keep the simulated result for a compile check
    (RUN / "crops_005_009" / "simulated_ega3-1-fr.tex").write_text(t, encoding="utf-8", newline="")
