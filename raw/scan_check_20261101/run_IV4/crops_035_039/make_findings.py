# Builds findings_035_039.json and checks that every fix "old" occurs exactly once
# in its page file (or, for a fix declared "after", in the text after the earlier fix).
import json, sys

BASE = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = BASE + "/findings_035_039.json"
NL = "\u23ce"  # placeholder for a line break inside "old"/"new"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, after=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    d["_after"] = after  # index (into F) of a fix that must be applied first
    F.append(d)
    return len(F) - 1


OM = "Sheaf of differentials: italic Omega (\\varOmega) in the print."
FJ = ("Wrong letter: the print's Fraktur capital has the descender of a Fraktur J (as on pp. 11-23, "
      "GLOBAL_ISSUES 91); ega4-16 writes \\mathfrak{I}.")
DOTS = "Baseline dots in the print (crop); \\cdots gives centred dots."
DASH = "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."

# ---------------- page 35 ----------------
add(35, "Théorème (16.6.2), label (iii)", "upright '(iii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]")
add(35, "Théorème (16.6.2) (iii): 'ω'_p∈Γ(U, Ω^p_{X/S}), ω''_q∈Γ(U, Ω^q_{X/S})'",
    "italic Omega twice (crop p35_s1_iii.png)", "upright \\Omega", "font", None, "high",
    r"\Gamma(U,\Omega_{X/S}^p)$,⏎$\omega''_q\in\Gamma(U,\Omega_{X/S}^q)$",
    r"\Gamma(U,\varOmega_{X/S}^p)$,⏎$\omega''_q\in\Gamma(U,\varOmega_{X/S}^q)$", OM)
add(35, "display (16.6.2.1): '+(—1)^p ω'_p∧dω''_q'", "long dash for the unary minus (crop p35_s1_disp1.png; longer than the bar of +)",
    "-", "convention", 7, "high", r"+(-1)^p", r"+(\setmin 1)^p", DASH)
add(35, "proof of (16.6.2), l. 2: 'toute section de Ω^p_{X/S} au-dessus de U'", "italic Omega (crop p35_s1_sectionOmega.png)",
    "upright \\Omega", "font", None, "high", r"de $\Omega_{X/S}^p$ au-dessus", r"de $\varOmega_{X/S}^p$ au-dessus", OM)
add(35, "proof of (16.6.2): 'de la forme g(df_1∧df_2∧...∧df_p)'", "baseline dots (crop p35_s1_dots.png)", "\\cdots",
    "symbol", None, "high", r"$g(df_1\wedge df_2\wedge\cdots", r"$g(df_1\wedge df_2\wedge\ldots", DOTS)
add(35, "proof of (16.6.2): 'où g et les f_i sont de sections de O_X'", "'sont de sections' (crop p35_s1_desections.png)",
    "'sont des sections'", "misprint_in_print", None, "high", r"sont des⏎sections", r"sont de⏎sections",
    "The print drops the s of 'des'. The TeX silently corrects it; the fix restores the printed reading.",
    corrected="sont des sections")
add(35, "proof of (16.6.2): 'au-dessus de U (0, 20.4.7)'", "bold 0, no subscript (crop p35_s1_0ref.png)", "plain 0",
    "convention", 2, "high", r"(0, 20.4.7)", r"(\textbf{0}, 20.4.7)")
add(35, "display (16.6.2.2), left side 'd(g(df_1∧df_2∧...∧df_p))'", "baseline dots (crop p35_s2_disp2.png)", "\\cdots",
    "symbol", None, "high", r"d(g(df_1\wedge df_2\wedge\cdots", r"d(g(df_1\wedge df_2\wedge\ldots", DOTS)
add(35, "display (16.6.2.2), right side 'dg∧df_1∧df_2∧...∧df_p'", "baseline dots (crop p35_s2_disp2.png)", "\\cdots",
    "symbol", None, "high", r"=dg\wedge df_1\wedge df_2\wedge\cdots", r"=dg\wedge df_1\wedge df_2\wedge\ldots", DOTS)
add(35, "after (16.6.2.3): 'quels que soient f, g dans A'", "'dans A' (crop p35_s3_dansA.png)",
    "dans $A$ (keeps the print)", "misprint_in_print", None, "high", None, None,
    "f and g are sections of O_X, i.e. elements of B: the elements g.df with f, g in B generate Omega^1_{B/A}, and df=0 for f in A; "
    "the next display has g∈B. The TeX keeps the printed reading; the corrected edition should read 'dans B'. No erratum found.",
    corrected="quels que soient $f$, $g$ dans $B$")
add(35, "'comme Ω^1_{B/A}=𝔍/𝔍² (où 𝔍=𝔍_{B/A} est le noyau'", "Fraktur J four times (descender; crop p35_s3_frak.png)",
    "\\mathfrak{I}", "symbol", None, "high",
    r"=\mathfrak{I}/\mathfrak{I}^2$ (où⏎$\mathfrak{I}=\mathfrak{I}_{B/A}$",
    r"=\mathfrak{J}/\mathfrak{J}^2$ (où⏎$\mathfrak{J}=\mathfrak{J}_{B/A}$", FJ)
add(35, "'w soit nul dans l'image de B⊗_A 𝔍²'", "Fraktur J (crop p35_s4_frak2.png)", "\\mathfrak{I}", "symbol", None, "high",
    r"$B\otimes_A\mathfrak{I}^2$", r"$B\otimes_A\mathfrak{J}^2$", FJ)
add(35, "'Comme, d'autre part, 𝔍 est engendré par les éléments'", "Fraktur J (crop p35_s4_minus.png)", "\\mathfrak{I}",
    "symbol", None, "high", r"$\mathfrak{I}$ est engendré", r"$\mathfrak{J}$ est engendré", FJ)
add(35, "'les éléments 1⊗x—x⊗1 (x∈B)'", "long dash for the minus (crop p35_s4_minus.png)", "-", "convention", 7, "high",
    r"éléments $1\otimes x-x\otimes1$", r"éléments $1\otimes x\setmin x\otimes1$", DASH)
add(35, "'z=(1⊗x—x⊗1)(1⊗y—y⊗1)': first factor", "long dash for the minus", "-", "convention", 7, "high",
    r"(1\otimes x-x\otimes1)", r"(1\otimes x\setmin x\otimes1)", DASH)
add(35, "'z=(1⊗x—x⊗1)(1⊗y—y⊗1)': second factor", "long dash for the minus", "-", "convention", 7, "high",
    r"(1\otimes y-y\otimes1)", r"(1\otimes y\setmin y\otimes1)", DASH)
add(35, "'z=1⊗(xy)+(xy)⊗1—x⊗y—y⊗x': first minus", "long dash for the minus (crop p35_s4_minus.png)", "-",
    "convention", 7, "high", r"(xy)\otimes1-x", r"(xy)\otimes1\setmin x", DASH)
add(35, "'z=1⊗(xy)+(xy)⊗1—x⊗y—y⊗x': second minus", "long dash for the minus", "-", "convention", 7, "high",
    r"y-y\otimes x", r"y\setmin y\otimes x", DASH)
add(35, "last line: 'la formule (16.6.2.4) montre qu'il [suffit de voir ...]'", "(16.6.2.4) (crop p35_s4_minus.png)",
    "(16.6.2.4) (keeps the print)", "misprint_in_print", None, "medium", None, None,
    "w(g'⊗z) is computed with the defining formula (16.6.2.5) of w: w(g'⊗z)=dg'∧(d(xy)-x.dy-y.dx); (16.6.2.4) is the formula for v, "
    "which plays no part in this step. The TeX keeps the printed reading; the corrected edition should probably read (16.6.2.5). No erratum found.",
    corrected="(16.6.2.5)")

# ---------------- page 36 ----------------
add(36, "l. 1: 'd(xy)—x.dy—y.dx=0': first minus", "long dash for the minus (crop p36_s1_dashes.png)", "-",
    "convention", 7, "high", r"(xy)-x", r"(xy)\setmin x", DASH)
add(36, "l. 1: 'd(xy)—x.dy—y.dx=0': second minus", "long dash for the minus", "-", "convention", 7, "high",
    r"dy-y.dx", r"dy\setmin y.dx", DASH)
add(36, "display before C.Q.F.D.: '(d(dg))∧(df)—(dg)∧(d(df))=0'", "long dash for the minus (crop p36_s1_disp.png)", "-",
    "convention", 7, "high", r"(df)-(dg)", r"(df)\setmin(dg)", DASH)
add(36, "Définition (16.6.3): 'définie dans (16.6.2)'", "reference upright (crop p36_s2_aussi_zoom.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"définie dans (16.6.2)", r"définie dans \textup{(16.6.2)}")
add(36, "Définition (16.6.3): 'appelée différentielle extérieure sur X (relativement à S)'",
    "only 'différentielle extérieure' is roman; 'sur' is italic like the rest of the statement (crop p36_s2_def.png)",
    "\\emph{différentielle extérieure sur $X$}: 'sur' comes out upright", "italics", None, "high",
    r"\emph{différentielle extérieure sur $X$}", r"\emph{différentielle extérieure} sur $X$")
add(36, "Proposition (16.6.4), display (16.6.4.1)", "italic Omega twice", "upright \\Omega", "font", None, "high",
    r"\Omega_{X/S}^{\bullet}\otimes_S S'⏎  \longrightarrow\Omega_{X'/S'}^{\bullet}",
    r"\varOmega_{X/S}^{\bullet}\otimes_S S'⏎  \longrightarrow\varOmega_{X'/S'}^{\bullet}", OM)
add(36, "Proposition (16.6.4): 'déduit de l'isomorphisme (16.5.9.1)'", "reference upright (crop p36_s2_prop.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"l'isomorphisme (16.5.9.1)", r"l'isomorphisme \textup{(16.5.9.1)}")
add(36, "Proposition (16.6.4): 'déduit de l'isomorphisme (16.5.9.1)'", "(16.5.9.1)", "(16.5.9.1) (keeps the print)",
    "misprint_in_print", None, "high", None, None,
    "(16.5.9.1) is the bracket [D_1, D_2]; the isomorphism Ω^1_{X/S}⊗_S S' ⥲ Ω^1_{X'/S'} is (16.5.10.1) (p. 29). "
    "The TeX keeps the printed reading; in the corrected edition change the number inside the \\textup of the convention-6 fix above.",
    corrected="(16.5.10.1)")
add(36, "Proposition (16.6.4): 'si s est une section de Ω^•_{X/S} au-dessus'", "italic Omega", "upright \\Omega", "font", None,
    "high", r"section de $\Omega_{X/S}^{\bullet}$", r"section de $\varOmega_{X/S}^{\bullet}$", OM)
add(36, "Proposition (16.6.4): 'section de Ω^•_{X'/S'}, au-dessus de l'image réciproque U''", "italic Omega", "upright \\Omega",
    "font", None, "high", r"section de $\Omega_{X'/S'}^{\bullet}$", r"section de $\varOmega_{X'/S'}^{\bullet}$", OM)
i_om = add(36, "(16.6.5), l. 1: 'Supposons que Ω^1_{X/S} soit un O_X-Module'", "italic Omega (sheaf of differentials)",
           "upright \\Omega", "font", None, "high",
           r"Supposons que $\Omega_{X/S}^1$ soit", r"Supposons que $\varOmega_{X/S}^1$ soit", OM)
add(36, "(16.6.5), l. 1: 'Supposons que Ω^1_{X/S} soit'", "this Omega is BOLD italic (wrong fount; side-by-side crop g_side_by_side.png "
    "against the two light italic Omegas of (16.6.4.1); the neighbouring 'que', '1', 'X/S' are of normal weight)",
    "normal weight (silent correction)", "misprint_in_print", None, "high",
    r"Supposons que $\varOmega_{X/S}^1$ soit", r"Supposons que $\boldsymbol{\varOmega}_{X/S}^1$ soit",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29; cf. IV-4 pp. 7, 27). Apply after the preceding font fix: "
    "'old' is the text after that fix.", corrected=r"$\varOmega_{X/S}^1$", after=i_om)
add(36, "(16.6.5), l. 1: 'localement libre de rang n en un point x'", "'localement libre de rang n' italic, 'en' roman (crop p36_s2_locallibre.png)",
    "roman", "italics", None, "high", r"localement libre⏎de rang $n$ en", r"\emph{localement libre⏎de rang $n$} en")
add(36, "(16.6.5): 'base du Γ(U, O_X)-module Γ(U, Ω^1_{X/S}) (16.5.8)'", "italic Omega (crop p36_s3_basis.png)", "upright \\Omega",
    "font", None, "high", r"$\Gamma(U,\Omega_{X/S}^1)$ (16.5.8)", r"$\Gamma(U,\varOmega_{X/S}^1)$ (16.5.8)", OM)
add(36, "(16.6.5): 'les p-différentielles ds_{i_1}∧ds_{i_2}∧...∧ds_{i_p}'", "baseline dots (crop p36_s3_basis.png)", "\\cdots",
    "symbol", None, "high", r"ds_{i_2}\wedge\cdots\wedge ds_{i_p}$ (pour", r"ds_{i_2}\wedge\ldots\wedge ds_{i_p}$ (pour", DOTS)
add(36, "(16.6.5): '(pour i_1<i_2<...<i_p'", "baseline dots", "\\cdots", "symbol", None, "high",
    r"$i_1<i_2<\cdots<i_p$", r"$i_1<i_2<\ldots<i_p$", DOTS)
add(36, "(16.6.5): 'une base de (n p) éléments de Γ(U, Ω^p_{X/S})'", "italic Omega", "upright \\Omega", "font", None, "high",
    r"$\Gamma(U,\Omega_{X/S}^p)$ sur", r"$\Gamma(U,\varOmega_{X/S}^p)$ sur", OM)
add(36, "display (16.6.5.1), left side 'd(g.ds_{i_1}∧ds_{i_2}∧...∧ds_{i_p})'", "baseline dots (crop p36_s3_disp.png)", "\\cdots",
    "symbol", None, "high", r"d(g.ds_{i_1}\wedge ds_{i_2}\wedge\cdots", r"d(g.ds_{i_1}\wedge ds_{i_2}\wedge\ldots", DOTS)
add(36, "display (16.6.5.1): 'Σ_k (—1)^r'", "long dash for the unary minus (crop p36_s3_disp.png)", "-", "convention", 7, "high",
    r"\sum_k(-1)^r", r"\sum_k(\setmin 1)^r", DASH)
add(36, "display (16.6.5.1): 'ds_{i_1}∧...∧ds_{i_r}'", "baseline dots", "\\cdots", "symbol", None, "high",
    r"ds_{i_1}\wedge\cdots\wedge ds_{i_r}", r"ds_{i_1}\wedge\ldots\wedge ds_{i_r}", DOTS)
add(36, "display (16.6.5.1): 'ds_{i_{r+1}}∧...∧ds_{i_p}'", "baseline dots", "\\cdots", "symbol", None, "high",
    r"ds_{i_{r+1}}\wedge\cdots", r"ds_{i_{r+1}}\wedge\ldots", DOTS)
add(36, "after (16.6.5.1): 'l'ensemble des n—p indices'", "long dash for the minus (crop p36_s3_disp.png)", "-", "convention", 7,
    "high", r"$n-p$ indices", r"$n\setmin p$ indices", DASH)
add(36, "(16.7.1), last line: 'le n-ème voisinage infinitésimal de X pour le morphisme diagonal'",
    "'n-ème voisinage infinitésimal' italic, 'de X' roman (crop p36_s4_voisinage.png)", "'de $X$' inside the \\emph",
    "italics", None, "high", r"infinitésimal de $X$} pour", r"infinitésimal} de $X$ pour")

# ---------------- page 37 ----------------
add(37, "(16.7.1), display of p_1^(n), p_2^(n)", "space between the two maps", "',qquad': the backslash is missing, so 'qquad' is typeset as letters",
    "extra", None, "high", r"\xrightarrow{p_1}X,qquad", r"\xrightarrow{p_1}X,\qquad",
    "Same defect at ega4-16 source lines 2789 and 2867 (next findings) and at ega4-17-fr.tex line 30.")
add(37, "(16.7.2): 'sur les espaces annelés (0_I, 4.3.1)'", "(0_I, 4.3.1): bold 0 with subscript I (crop p37_s2_0I.png)",
    "(0, 4.3.1): no subscript I", "missing", None, "high", r"(0, 4.3.1)", r"($\mathbf{0}_{\mathrm I}$, 4.3.1)",
    "The same edit sets the bold 0 (convention 2). Images réciproques of Modules on ringed spaces are in EGA 0_I §4.3.")
add(37, "(16.7.2): 'définie par l'homomorphisme de faisceaux d'anneaux d^n_{X/S}'", "'l'homomorphisme de faisceaux d'anneaux' italic (crop p37_s2_homfaisc.png)",
    "roman", "italics", None, "high", r"définie par l'homomorphisme de faisceaux d'anneaux",
    r"définie par \emph{l'homomorphisme de faisceaux d'anneaux}")
add(37, "(16.7.2), end: 'muni d'une structure de P^n_{X/S}-Module.'", "'Module' italic (crop p37_s3_Module.png)", "roman",
    "italics", None, "high", r"$\mathscr{P}_{X/S}^n$-Module.", r"$\mathscr{P}_{X/S}^n$-\emph{Module}.")
add(37, "Proposition (16.7.3), label (i)", "upright '(i)'", "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]")
add(37, "Proposition (16.7.3) (i): 'Le foncteur F ⇝ P^n_{X/S}(F)'", "wavy arrow (crop p37_s3_prop.png)", "\\mapsto", "symbol", None,
    "high", r"Le foncteur⏎$\mathscr{F}\mapsto", r"Le foncteur⏎$\mathscr{F}\leadsto")
add(37, "Proposition (16.7.3), label (ii)", "upright '(ii)'", "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(ii)]", r"\item[\textup{(ii)}]")
add(37, "Proposition (16.7.3) (ii): 'quasi-cohérent (resp. de type fini, resp. de présentation finie),'",
    "'(resp.', 'resp.' and ')' upright, the conditions italic (crop p37_s3_resp.png)", "all italic", "convention", 6, "high",
    r"(resp. de type fini, resp. de présentation finie),",
    r"\textup{(resp.}\ de type fini, \textup{resp.}\ de présentation finie\textup{)},")
add(37, "Proposition (16.7.3) (ii), end: '-Module quasi-cohérent (resp. de type fini, resp. de présentation finie).'",
    "'(resp.', 'resp.' and ')' upright, the conditions italic (crop p37_s3_resp.png)", "all italic", "convention", 6, "high",
    r"(resp. de type fini, resp. de présentation finie).",
    r"\textup{(resp.}\ de type fini, \textup{resp.}\ de présentation finie\textup{)}.")
add(37, "proof of (16.7.3): 'l'exactitude à droite du foncteur F ⇝ P^n_{X/S}(F)'", "wavy arrow (crop p37_s3_leadsto2.png)",
    "\\mapsto", "symbol", None, "high", r"du foncteur⏎$\mathscr{F}\mapsto", r"du foncteur⏎$\mathscr{F}\leadsto")
add(37, "(16.7.4): 'donc une structure de O_X-Bimodule.'", "'Bimodule' italic (crop p37_s3_bimod.png)", "roman", "italics", None,
    "high", r"$\mathcal{O}_X$-Bimodule.", r"$\mathcal{O}_X$-\emph{Bimodule}.")
add(37, "display (16.7.4.1)", "space between the two formulas", "',qquad': the backslash is missing, so 'qquad' is typeset as letters",
    "extra", None, "high", r"t,qquad", r"t,\qquad")
add(37, "last line: 'la structure de O_X-Module à gauche.'", "'à gauche' italic (crop p37_s4_gauche.png)", "roman", "italics", None,
    "high", r"$\mathcal{O}_X$-Module à⏎gauche.", r"$\mathcal{O}_X$-Module \emph{à⏎gauche}.")

# ---------------- page 38 ----------------
add(38, "(16.7.5), after (16.7.5.4): 'pour la structure de O_X-Module à droite sur P^n_{X/S}(F)'", "'à droite' italic (crop p38_s2_droite.png)",
    "roman", "italics", None, "high", r"-Module à droite sur", r"-Module \emph{à droite} sur")
add(38, "(16.7.5), end: 'pour la structure de O_X-Module à gauche.'", "'à gauche' italic (crop p38_s2_droite.png)", "roman", "italics",
    None, "high", r"-Module à gauche.", r"-Module \emph{à gauche}.")
add(38, "(16.7.7), display 'P^m_{X/S}(F) → P^n_{X/S}(F)   (n≤m)'", "space before (n≤m)",
    "'qquad' without backslash, typeset as letters", "extra", None, "high",
    r"(\mathscr{F})qquad(n\leq m)", r"(\mathscr{F})\qquad(n\leq m)")
add(38, "(16.7.7): 'un système projectif de O_X-Bimodules (P^n_{X/S}(F))'", "the exponent n is BOLD italic (wrong fount; side-by-side crop "
    "g_n_side_by_side.png against the light n of (16.7.7.1) on the next line; the P, X/S, F around it are of normal weight)",
    "normal n (silent correction)", "misprint_in_print", None, "high",
    r"$(\mathscr{P}_{X/S}^n(\mathscr{F}))$", r"$(\mathscr{P}_{X/S}^{\boldsymbol{n}}(\mathscr{F}))$",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29; cf. IV-4 pp. 7, 27).",
    corrected=r"$(\mathscr{P}_{X/S}^n(\mathscr{F}))$")

# ---------------- page 39 ----------------
add(39, "Remarque (16.7.10): 'étant définie dans (0_I, 3.7.1)'", "bold 0 with subscript I (crop p39_s3_0I.png)",
    "0\\textsubscript{I}: plain 0", "convention", 2, "high", r"(0\textsubscript{I}, 3.7.1)", r"($\mathbf{0}_{\mathrm I}$, 3.7.1)",
    "Written as the edition's other (0_I, ...) references; the math-mode form also keeps the reference upright inside the (italic) remark environment.")
add(39, "heading 16.8: 'Opérateurs différentiels (1).'", "footnote mark inside the heading, before the full stop (crop p39_s3_heading.png)",
    "\\footnote placed after \\subsection{Opérateurs différentiels.}: the mark falls outside the heading, after its full stop",
    "other", None, "high",
    r"\subsection{Opérateurs différentiels.}⏎\footnote{",
    r"\subsection{Opérateurs différentiels\texorpdfstring{\protect\footnotemark}{}.}⏎\footnotetext{",
    "Same construction as the footnoted heading 18.5 in ega4-18-fr.tex (line 503). Footnote text matches the print.")
add(39, "Définition (16.8.1): 'est un opérateur différentiel d'ordre ≤n (relativement à S)'",
    "italic like the rest of the statement, no change of face (crop p39_s3_def.png)",
    "\\emph{...} inside the italic definition: comes out upright", "italics", None, "high",
    r"\emph{opérateur différentiel d'ordre⏎$\leq n$}", r"opérateur différentiel d'ordre⏎$\leq n$")
add(39, "Définition (16.8.1): 'Module à gauche (16.7.4)) tel que'", "reference upright (crop p39_s4_1674.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"à gauche (16.7.4))", r"à gauche \textup{(16.7.4)})")

# ---------------- checks ----------------
pages = {}
ok = True
applied = {}
for i, d in enumerate(F):
    p = d["page"]
    if p not in pages:
        # page files are CRLF on disk; the release files use LF: compare on LF text
        pages[p] = open(f"{BASE}/page_{p:03d}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n")
    txt = pages[p]
    if "\r" in txt:
        print("CR in page", p)
    fx = d["fix"]
    if fx is None:
        continue
    if d["_after"] is not None:
        j = d["_after"]
        base = txt.replace(F[j]["fix"]["old"], F[j]["fix"]["new"], 1)
        n = base.count(fx["old"])
        n0 = txt.count(fx["old"])
        print(f"[{i}] p{p} (after fix {j}) count after={n} count in page={n0}")
        if n != 1:
            ok = False
    else:
        n = txt.count(fx["old"])
        if n != 1:
            print(f"[{i}] p{p} COUNT {n}: {fx['old']!r}")
            ok = False
# overlap check: fixes on the same page must not overlap (except declared 'after')
for p, txt in pages.items():
    spans = []
    for i, d in enumerate(F):
        if d["page"] != p or d["fix"] is None or d["_after"] is not None:
            continue
        a = txt.find(d["fix"]["old"])
        spans.append((a, a + len(d["fix"]["old"]), i))
    spans.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(spans, spans[1:]):
        if a2 < b1:
            print(f"OVERLAP p{p}: fix {i1} and {i2}")
            ok = False
for d in F:
    del d["_after"]
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted(pages):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F), "OK" if ok else "PROBLEMS")
