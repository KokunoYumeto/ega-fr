"""Build findings_140_144.json for EGA IV-2 pp. 140-144 and validate every fix.

Validation: (1) every fix's "old" occurs exactly once in the original page text;
(2) applying the fixes in list order, each "old" occurs exactly once at the moment
it is applied (the coordinator's apply_fixes.py applies them in this order).
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_140_144.json"

F = []


def add(page, where, scan, tex, kind, fix, note=None, convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention,
             confidence=confidence, fix=fix)
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


BS = "\\boldsymbol{k}"

# ---------------------------------------------------------------- page 140
p = 140
add(p, "proof of (6.3.4): 'les modules de longueur finie ≠ 0 ... (0, 16.2.3)'", "bold 0", "plain 0",
    "convention", fx("(0, 16.2.3)", "(\\textbf{0}, 16.2.3)"), convention=2)
add(p, "after (6.3.4): 'lorsque mB est un idéal de définition de l'anneau B'",
    "'idéal de définition' italic (enlarged crop)", "upright", "italics",
    fx("est un idéal\nde définition", "est un \\emph{idéal\nde définition}"))
add(p, "Corollaire (6.3.5), label (i)", "label (i) upright",
    "\\item[(i)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(i)] Si, en un point", "\\item[\\textup{(i)}] Si, en un point"), convention=6,
    note="GLOBAL_ISSUES 16.")
add(p, "Corollaire (6.3.5) (i): 'coprof(O_x ⊗_{O_y} k(y)) ≤ n'", "bold italic k in k(y)", "k(y)",
    "convention", fx("k(y))\\leq n$; en", BS + "(y))\\leq n$; en"), convention=1)
add(p, "Corollaire (6.3.5) (i), end: 'et de O_x ⊗_{O_y} k(y).'", "bold italic k in k(y)", "k(y)",
    "convention", fx("et de\n$\\mathcal O_x\\otimes_{\\mathcal O_y}k(y)$",
                     "et de\n$\\mathcal O_x\\otimes_{\\mathcal O_y}" + BS + "(y)$"), convention=1)
add(p, "Corollaire (6.3.5), label (ii)", "label (ii) upright",
    "\\item[(ii)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(ii)] Supposons inversement", "\\item[\\textup{(ii)}] Supposons inversement"),
    convention=6, note="GLOBAL_ISSUES 16.")
add(p, "Corollaire (6.3.5) (ii): 'que O_x ⊗_{O_y} k(y) soit un anneau'", "bold italic k in k(y)", "k(y)",
    "convention", fx("k(y)$ soit un anneau", BS + "(y)$ soit un anneau"), convention=1)
add(p, "Corollaire (6.3.5) (ii): 'coprof(O_y) ≤ n (resp. si O_y est'", "'(resp.' upright inside the italic statement",
    "typeset italic", "convention", fx("(resp. si", "\\textup{(resp.} si"), convention=6,
    note="Enlarged crop.")
add(p, "Corollaire (6.3.5) (ii): 'coprof(O_x) ≤ n (resp. O_x est'", "'(resp.' upright inside the italic statement",
    "typeset italic", "convention", fx("(resp. $\\mathcal O_x$", "\\textup{(resp.} $\\mathcal O_x$"),
    convention=6, note="Enlarged crop.")
add(p, "proof of (6.3.5): 'pour M = A = O_y et N = B = O_x' (end of the paragraph)",
    "no full stop after O_x (enlarged crop; no ink between O_x and the margin)",
    "full stop after $N=B=\\mathcal O_x$", "misprint_in_print",
    fx("$N=B=\\mathcal O_x$.", "$N=B=\\mathcal O_x$"), corrected="$N=B=\\mathcal O_x$.",
    note="Missing final full stop in the print; the TeX silently corrects it. The fix restores the printed reading.")
add(p, "proof of (6.3.6): 'f est plat (puisque A' est un A-module libre'", "'plat' italic (enlarged crop)",
    "upright", "italics", fx("est plat (puisque", "est \\emph{plat} (puisque"))
add(p, "proof of (6.3.6): 'pour tout y∈Y, k(y)[T_1, ..., T_n]'", "bold italic k in k(y)", "k(y)",
    "convention", fx("$k(y)[T_1", "$" + BS + "(y)[T_1"), convention=1)
add(p, "proof of (6.3.6): '(0, 17.3.7)'", "bold 0", "plain 0", "convention",
    fx("(0, 17.3.7)", "(\\textbf{0}, 17.3.7)"), convention=2)
add(p, "proof of (6.3.7): 'et de (0, 16.5.12)'", "bold 0", "plain 0", "convention",
    fx("(0, 16.5.12)", "(\\textbf{0}, 16.5.12)"), convention=2)
add(p, "proof of (6.3.8): 'B^ = B ⊗_A A^ (0_I, 7.3.3)'", "bold 0 in 0_I", "$(0_{\\mathrm I}, 7.3.3)$",
    "convention", fx("$(0_{\\mathrm I}, 7.3.3)$", "$(\\mathbf{0}_{\\mathrm I}, 7.3.3)$"), convention=2)
add(p, "proof of (6.3.8): 'on sait (0, 16.5.6 et 16.5.9)'", "bold 0", "plain 0", "convention",
    fx("(0, 16.5.6 et", "(\\textbf{0}, 16.5.6 et"), convention=2)
add(p, "proof of (6.3.8): 'telle que N = M/(Σ_{i=1}^r t_iM) soit un A-module'",
    "formula in the running text (ordinary parentheses)", "set as a display \\[ ... \\] with \\Bigl( \\Bigr)",
    "other", fx("\\[\nN=M/\\Bigl(\\sum_{i=1}^{r}t_iM\\Bigr)\n\\]", "$N=M/(\\sum_{i=1}^{r}t_iM)$"),
    note="GLOBAL_ISSUES 21; the connecting words 'telle que' / 'soit un' are kept.")
add(p, "proof of (6.3.8): 'p un idéal premier associé minimal de N'", "'minimal' italic (enlarged crop)",
    "upright", "italics", fx("associé\nminimal de", "associé\n\\emph{minimal} de"))
add(p, "last line: '... supposer que p est un' / p. 141 'idéal premier minimal de A'",
    "the sentence runs on to p. 141 without a paragraph break", "blank line before \\oldpage[IV-2]{141}",
    "other", fx("supposer que $\\mathfrak p$ est un\n\n", "supposer que $\\mathfrak p$ est un\n"),
    note="Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the "
         "p. 141 edit that removes the blank line after \\oldpage[IV-2]{141}.")

# ---------------------------------------------------------------- page 141
p = 141
add(p, "top of the page: 'idéal premier minimal de A' continues '... supposer que p est un' of p. 140",
    "no paragraph break", "blank line after \\oldpage[IV-2]{141}", "other",
    fx("\\oldpage[IV-2]{141}\n\nidéal", "\\oldpage[IV-2]{141}\nidéal"),
    note="Apply together with the p. 140 edit that removes the blank line before the marker.")
add(p, "line 1: 'idéal premier minimal de A'", "'minimal' italic", "upright", "italics",
    fx("premier minimal de $A$", "premier \\emph{minimal} de $A$"))
add(p, "line 1: 'M' = M^ = M ⊗_A A' (0_I, 7.3.3)'", "bold 0 in 0_I", "$(0_{\\mathrm I}, 7.3.3)$",
    "convention", fx("$(0_{\\mathrm I}, 7.3.3)$", "$(\\mathbf{0}_{\\mathrm I}, 7.3.3)$"), convention=2)
add(p, "line 2: 'on sait (0, 16.5.2)'", "bold 0", "plain 0", "convention",
    fx("(0, 16.5.2)", "(\\textbf{0}, 16.5.2)"), convention=2)
add(p, "line 3: 'A'_{p'}-module de Cohen-Macaulay (0, 16.5.10).'", "bold 0", "plain 0", "convention",
    fx("(0, 16.5.10). Compte", "(\\textbf{0}, 16.5.10). Compte"), convention=2)
add(p, "line 4: 'Compte tenu de (I, 3.6.5)'", "bold I", "plain I", "convention",
    fx("(I, 3.6.5)", "(\\textbf{I}, 3.6.5)"), convention=2)
add(p, "line 6: 'A''_{p''}-module de Cohen-Macaulay (0, 16.5.10);'", "bold 0", "plain 0", "convention",
    fx("(0, 16.5.10);", "(\\textbf{0}, 16.5.10);"), convention=2)
add(p, "line 8: 'A''_{p''} est un A_p-module plat puisque A' est un A-module plat'",
    "the first 'plat' italic, the second upright (enlarged crop)", "both upright", "italics",
    fx("-module plat puisque", "-module \\emph{plat} puisque"))
add(p, "line 8: '(0_I, 7.3.3 et 6.3.2)'", "bold 0 in 0_I", "$(0_{\\mathrm I}, 7.3.3\\text{ et }6.3.2)$",
    "convention", fx("$(0_{\\mathrm I}, 7.3.3\\text{ et }6.3.2)$",
                     "$(\\mathbf{0}_{\\mathrm I}, 7.3.3\\text{ et }6.3.2)$"), convention=2)
add(p, "line 11: 'à ceux de k ⊗_{A_p} A'' (I, 3.5.7)'", "bold I", "plain I", "convention",
    fx("(I, 3.5.7)", "(\\textbf{I}, 3.5.7)"), convention=2)
add(p, "line 13: 'Par suite (0, 16.5.13)'", "bold 0", "plain 0", "convention",
    fx("(0, 16.5.13)", "(\\textbf{0}, 16.5.13)"), convention=2)
add(p, "heading 6.4", "'6.4. Platitude et propriété (S_k).' with a final full stop",
    "\\subsection{\\texorpdfstring{Platitude et propriété $(S_k)$}{...}} (no full stop)", "punctuation",
    fx("\\texorpdfstring{Platitude et propriété $(S_k)$}", "\\texorpdfstring{Platitude et propriété $(S_k)$.}"),
    note="GLOBAL_ISSUES 43/58; the bookmark argument is left as it is.")
add(p, "Proposition (6.4.1), label (i)", "label (i) upright",
    "\\item[(i)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(i)] Soit $x", "\\item[\\textup{(i)}] Soit $x"), convention=6, note="GLOBAL_ISSUES 16.")
add(p, "Proposition (6.4.1), label (ii)", "label (ii) upright",
    "\\item[(ii)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(ii)] Supposons que pour tout", "\\item[\\textup{(ii)}] Supposons que pour tout"),
    convention=6, note="GLOBAL_ISSUES 16.")
add(p, "Proposition (6.4.1) (ii): 'F_y = F ⊗_{O_Y} k(y)'",
    "index of the tensor sign O_Y with a capital Y (enlarged crop; same Y as in 'O_Y-Module' above)",
    "\\otimes_{\\mathcal O_y} (small y)", "formula",
    fx("\\mathscr F_y=\\mathscr F\\otimes_{\\mathcal O_y}", "\\mathscr F_y=\\mathscr F\\otimes_{\\mathcal O_Y}"),
    note="The fibre F_y = F ⊗_{O_Y} k(y) (tensor over the structure sheaf of Y), as printed.")
add(p, "Proposition (6.4.1) (ii): 'F ⊗_{O_Y} k(y) ait la propriété (S_k)'", "bold italic k in k(y)", "k(y)",
    "convention", fx("k(y)$ ait la propriété", BS + "(y)$ ait la propriété"), convention=1)
add(p, "proof of (6.4.1) (i): 'dim(F_{x'} ⊗_{O_{y'}} k(y')) = 0'", "bold italic k in k(y')", "k(y')",
    "convention", fx("k(y'))=0", BS + "(y'))=0"), convention=1)

# ---------------------------------------------------------------- page 142
p = 142
add(p, "proof of (6.4.1) (ii), first display: 'dim(G_x) = dim(E_y) + dim(F_x ⊗_{O_y} k(y))'",
    "bold italic k in k(y)", "k(y)", "convention",
    fx("k(y))\n\\]\n\\[", BS + "(y))\n\\]\n\\["), convention=1)
add(p, "second display: 'prof(G_x) = prof(E_y) + prof(F_x ⊗_{O_y} k(y)).'", "bold italic k in k(y)", "k(y)",
    "convention", fx("k(y)).\n\\]", BS + "(y)).\n\\]"), convention=1)
add(p, "display after 'Par hypothèse, on a', second line: 'prof(F_x ⊗_{O_y} k(y)) ≥ ...', first F_x",
    "the subscript x of the first F_x is a bold italic x (wrong fount): ink 250 px, mean stroke run 8.1 px, "
    "against 163-182 px / 4.5-5.3 px for the ordinary x of F_x and G_x on this page (the second F_x of the same "
    "line: 174 px / 5.3 px); checked on a 5x crop",
    "ordinary $\\mathscr F_x$ (silent correction)", "misprint_in_print",
    fx("\\[\n\\operatorname{prof}(\\mathscr F_x", "\\[\n\\operatorname{prof}(\\mathscr F_{\\boldsymbol{x}}"),
    corrected="\\operatorname{prof}(\\mathscr F_x", confidence="medium",
    note="Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text; plain x in the corrected edition.")
add(p, "same line: 'prof(F_x ⊗_{O_y} k(y)) ≥'", "bold italic k in k(y)", "k(y)", "convention",
    fx("k(y))\n\\geq\\inf", BS + "(y))\n\\geq\\inf"), convention=1)
add(p, "same line: '≥ inf(k, dim(F_x ⊗_{O_y} k(y)))'", "bold italic k in k(y)", "k(y)", "convention",
    fx("k(y)))\n\\]", BS + "(y)))\n\\]"), convention=1)
add(p, "display 'd'où, en ajoutant membre à membre', line 1: 'prof(G_x) ≥ ...'",
    "the subscript x of G_x is a bold italic x (wrong fount): 214 px / 6.9 px against about 165 px / 5 px for "
    "the ordinary x (this line is inked about 10-15% heavier overall); 5x crop",
    "ordinary $\\mathscr G_x$ (silent correction)", "misprint_in_print",
    fx("\\operatorname{prof}(\\mathscr G_x)\n&", "\\operatorname{prof}(\\mathscr G_{\\boldsymbol{x}})\n&"),
    corrected="\\operatorname{prof}(\\mathscr G_x)", confidence="medium",
    note="Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text.")
add(p, "same display, line 1: '+ inf(k, dim(F_x ⊗_{O_y} k(y))) ≥', the x of F_x",
    "subscript x looks bold (200 px / 6.9 px; the E_y of the same line is ordinary, 225 px / 5.1 px); 4x crop",
    "ordinary $\\mathscr F_x$ (silent correction)", "misprint_in_print",
    fx("+\\inf(k,\\dim(\\mathscr F_x", "+\\inf(k,\\dim(\\mathscr F_{\\boldsymbol{x}}"),
    corrected="+\\inf(k,\\dim(\\mathscr F_x", confidence="low",
    note="Borderline: the line is inked heavier than the rest of the page; apply only with the other wrong-fount "
         "x of this display.")
add(p, "same display, line 1: 'dim(F_x ⊗_{O_y} k(y))) ≥'", "bold italic k in k(y)", "k(y)", "convention",
    fx("k(y)))\\geq{}", BS + "(y)))\\geq{}"), convention=1)
add(p, "same display, line 2: '+ dim(F_x ⊗_{O_y} k(y)))'", "bold italic k in k(y)", "k(y)", "convention",
    fx("k(y))\\bigr)", BS + "(y))\\bigr)"), convention=1)
add(p, "same display, line 2, end: '= inf(k, dim(G_x))'",
    "the subscript x of G_x is a bold italic x (wrong fount): 217 px / 7.0 px on a normally inked line "
    "(the E_y and O_y of the line are ordinary); 5x crop",
    "ordinary $\\mathscr G_x$ (silent correction)", "misprint_in_print",
    fx("=\\inf(k,\\dim(\\mathscr G_x))", "=\\inf(k,\\dim(\\mathscr G_{\\boldsymbol{x}}))"),
    corrected="=\\inf(k,\\dim(\\mathscr G_x))", confidence="medium",
    note="Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text.")
add(p, "Remarque (6.4.3): 'tels que F_x ⊗_{O_{f(x)}} k(f(x)) vérifie'", "bold italic k in k(f(x))", "k(f(x))",
    "convention", fx("k(f(x))", BS + "(f(x))"), convention=1)
add(p, "Remarque (6.4.3): 'l'ensemble U des x∈X tels que ... vérifie (S_k) est ouvert dans X'",
    "(S_k) (enlarged crop)", "$(S_k)$, as printed", "misprint_in_print", None, corrected="$(S_n)$",
    confidence="medium",
    note="The TeX keeps the printed reading. The remark is about (S_n) throughout; U contains the closed point of X "
         "'par hypothèse' only if U is defined by (S_n), the property assumed for M ⊗_A k.")
add(p, "same sentence: 'vérifie (S_k) est ouvert dans X'", "'ouvert' italic (enlarged crop)",
    "upright in the remark body", "italics", fx("est ouvert\ndans $X$", "est \\emph{ouvert}\ndans $X$"),
    note="Judged with the remark body roman; the later 'que U est ouvert quand' is upright in the print.")

# ---------------------------------------------------------------- page 143
p = 143
add(p, "heading 6.5", "'6.5. Platitude et propriété (R_k).' with a final full stop",
    "\\subsection{\\texorpdfstring{Platitude et propriété $(R_k)$}{...}} (no full stop)", "punctuation",
    fx("\\texorpdfstring{Platitude et propriété $(R_k)$}", "\\texorpdfstring{Platitude et propriété $(R_k)$.}"),
    note="GLOBAL_ISSUES 43/58.")
add(p, "Proposition (6.5.1), label (i)", "label (i) upright",
    "\\item[(i)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(i)] Si $B$ est régulier", "\\item[\\textup{(i)}] Si $B$ est régulier"), convention=6,
    note="GLOBAL_ISSUES 16.")
add(p, "Proposition (6.5.1), label (ii)", "label (ii) upright",
    "\\item[(ii)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(ii)] Si $A$ et", "\\item[\\textup{(ii)}] Si $A$ et"), convention=6, note="GLOBAL_ISSUES 16.")
add(p, "after Proposition (6.5.1): 'Cette proposition est donnée pour mémoire, ayant déjà été démontrée dans "
       "(0, 17.3.3).'",
    "a separate roman paragraph after the italic statement", "inside the proposition environment (italic)",
    "italics",
    fx("\\end{enumerate}\nCette proposition est donnée pour mémoire, ayant déjà été démontrée dans\n"
       "(0, 17.3.3).\n\\end{proposition}",
       "\\end{enumerate}\n\\end{proposition}\n\nCette proposition est donnée pour mémoire, ayant déjà été "
       "démontrée dans\n(0, 17.3.3)."),
    note="The environment closes too late. Apply before the convention-2 edit of (0, 17.3.3) that follows.")
add(p, "same sentence: '(0, 17.3.3)'", "bold 0", "plain 0", "convention",
    fx("(0, 17.3.3)", "(\\textbf{0}, 17.3.3)"), convention=2)
add(p, "Corollaire (6.5.2), l. 1: 'localement noethériens f : X → Y'",
    "no comma after 'noethériens' (enlarged crop; (6.5.3) and (6.5.4) have it)",
    "comma after 'noethériens'", "misprint_in_print",
    fx("\\label{IV.2.s6.5.2-fr}\nSoient $X$, $Y$ deux préschémas localement noethériens, $f",
       "\\label{IV.2.s6.5.2-fr}\nSoient $X$, $Y$ deux préschémas localement noethériens $f"),
    corrected="localement noethériens, $f:X\\to Y$",
    note="Missing comma in the print; the TeX silently corrects it. The fix restores the printed reading.")
add(p, "Corollaire (6.5.2), label (i)", "label (i) upright",
    "\\item[(i)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(i)] Si $X$ est régulier", "\\item[\\textup{(i)}] Si $X$ est régulier"), convention=6,
    note="GLOBAL_ISSUES 16.")
add(p, "Corollaire (6.5.2), label (ii)", "label (ii) upright",
    "\\item[(ii)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(ii)] Si pour un", "\\item[\\textup{(ii)}] Si pour un"), convention=6, note="GLOBAL_ISSUES 16.")
add(p, "Proposition (6.5.3), label (i)", "label (i) upright",
    "\\item[(i)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(i)] Si $X$ possède", "\\item[\\textup{(i)}] Si $X$ possède"), convention=6,
    note="GLOBAL_ISSUES 16.")
add(p, "Proposition (6.5.3) (i): 'en un point x (resp. si X possède la propriété (R_k))'",
    "'(resp.' upright inside the italic statement", "typeset italic", "convention",
    fx("(resp. si $X$ possède", "\\textup{(resp.} si $X$ possède"), convention=6)
add(p, "Proposition (6.5.3) (i): 'au point f(x) (resp. Y possède la propriété (R_k) en tous les points'",
    "'(resp.' upright inside the italic statement", "typeset italic", "convention",
    fx("(resp. $Y$ possède", "\\textup{(resp.} $Y$ possède"), convention=6)
add(p, "Proposition (6.5.3), label (ii)", "label (ii) upright",
    "\\item[(ii)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(ii)] Supposons que pour tout", "\\item[\\textup{(ii)}] Supposons que pour tout"),
    convention=6, note="GLOBAL_ISSUES 16.")
add(p, "proof of (6.5.3) (i): 'donc on a dim(O_{x'} ⊗_{O_{y'}} k(y')) = 0 et en vertu de'",
    "formula in the running text", "set as a display", "other",
    fx("\\[\n\\dim(\\mathcal O_{x'}\\otimes_{\\mathcal O_{y'}}k(y'))=0\n\\]",
       "$\\dim(\\mathcal O_{x'}\\otimes_{\\mathcal O_{y'}}k(y'))=0$"),
    note="GLOBAL_ISSUES 21. Apply before the convention-1 edit of this k(y') that follows.")
add(p, "same formula: 'k(y')'", "bold italic k in k(y')", "k(y')", "convention",
    fx("k(y'))=0", BS + "(y'))=0"), convention=1)
add(p, "proof of (6.5.3) (i): '= 0 et en vertu de l'hypothèse et de (6.1.2),'",
    "'et en vertu' with no comma after 'et' (enlarged crop)", "'et, en vertu'", "punctuation",
    fx("et, en vertu de l'hypothèse", "et en vertu de l'hypothèse"))
add(p, "proof of (6.5.3) (i): 'et de (6.1.2), dim(O_{x'}) = dim(O_{y'}). L'hypothèse'",
    "formula in the running text", "set as a display", "other",
    fx("\\[\n\\dim(\\mathcal O_{x'})=\\dim(\\mathcal O_{y'}).\n\\]",
       "$\\dim(\\mathcal O_{x'})=\\dim(\\mathcal O_{y'})$."), note="GLOBAL_ISSUES 21.")
add(p, "proof of (6.5.3) (i): 'soit que dim(O_{x'}) > k, auquel cas'",
    "the subscript x of O_{x'} is a bold italic x (wrong fount): 188 px / 7.5 px against 153-164 px / 4.5-4.9 px "
    "for the x' of the two preceding O_{x'} on the same lines; 4x crop",
    "ordinary $x'$ (silent correction)", "misprint_in_print",
    fx("\\dim(\\mathcal O_{x'})>k", "\\dim(\\mathcal O_{\\boldsymbol{x}'})>k"),
    corrected="\\dim(\\mathcal O_{x'})>k", confidence="medium",
    note="Wrong-fount letter (GLOBAL_ISSUES 29), reproduced in the diplomatic text.")
add(p, "proof of (6.5.3) (ii): 'Or, on a, en vertu de (6.1.2)' before the display",
    "no comma after (6.1.2) (enlarged crop)", "comma after (6.1.2)", "punctuation",
    fx("en vertu de (6.1.2),\n\\[", "en vertu de (6.1.2)\n\\["))
add(p, "proof of (6.5.3) (ii), display: 'dim(O_x) = dim(O_y) + dim(O_x ⊗_{O_y} k(y))'",
    "bold italic k in k(y)", "k(y)", "convention",
    fx("+\\dim(\\mathcal O_x\\otimes_{\\mathcal O_y}k(y))", "+\\dim(\\mathcal O_x\\otimes_{\\mathcal O_y}" + BS + "(y))"),
    convention=1)
add(p, "same display, end", "no full stop after the display (enlarged crop)", "full stop at the end of the display",
    "punctuation", fx(")).\n\\]", "))\n\\]"), note="GLOBAL_ISSUES 73 (punctuation after displays).")
add(p, "after the display: 'donc si dim(O_x) ≤ k'", "lower-case 'donc' (the sentence runs on after the display)",
    "'Donc si'", "word", fx("\\]\nDonc si", "\\]\ndonc si"))
add(p, "same sentence: 'on a a fortiori dim(O_y) ≤ k'", "'a fortiori' italic", "upright", "italics",
    fx("on a a fortiori", "on a \\emph{a fortiori}"))
add(p, "same sentence: 'dim(O_x ⊗_{O_y} k(y)) ≤ k et l'hypothèse'", "bold italic k in k(y)", "k(y)",
    "convention", fx("\\dim(\\mathcal O_x\\otimes_{\\mathcal O_y}k(y))\\leqslant k",
                     "\\dim(\\mathcal O_x\\otimes_{\\mathcal O_y}" + BS + "(y))\\leqslant k"), convention=1)
add(p, "same sentence: '≤ k et l'hypothèse entraîne'", "no comma before 'et l'hypothèse' (enlarged crop)",
    "'\\leqslant k$, et l'hypothèse'", "punctuation",
    fx("\\leqslant k$, et l'hypothèse", "\\leqslant k$ et l'hypothèse"))
add(p, "same sentence: 'que O_y et O_x ⊗_{O_y} k(y) sont des anneaux réguliers'", "bold italic k in k(y)", "k(y)",
    "convention", fx("k(y)$ sont des", BS + "(y)$ sont des"), convention=1)
add(p, "Corollaire (6.5.4), label (i)", "label (i) upright",
    "\\item[(i)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(i)] Si $X$ est normal", "\\item[\\textup{(i)}] Si $X$ est normal"), convention=6,
    note="GLOBAL_ISSUES 16.")
add(p, "Corollaire (6.5.4), label (ii)", "label (ii) upright",
    "\\item[(ii)] inside the italic statement (typeset italic)", "convention",
    fx("\\item[(ii)] Si, pour tout", "\\item[\\textup{(ii)}] Si, pour tout"), convention=6,
    note="GLOBAL_ISSUES 16.")
add(p, "proof of (6.5.4): 'appliqué pour k = 2 et (6.5.3) appliqué pour k = 1'",
    "'et (6.5.3)' (no 'de')", "'et de (6.5.3)'", "extra", fx("et de (6.5.3) appliqué", "et (6.5.3) appliqué"))

# ---------------------------------------------------------------- page 144
p = 144
add(p, "Remarques (6.5.5) (i): 'tel que B soit un A-module plat.'", "'plat' italic (enlarged crop)",
    "upright in the remarks body", "italics", fx("module\nplat. Soit", "module\n\\emph{plat}. Soit"),
    note="Judged with the remarks body roman (document-wide remark item).")
add(p, "(i): 'alors il ne s'ensuit pas nécessairement que B vérifie (R_i)'",
    "'il ne s'ensuit pas nécessairement' italic", "upright", "italics",
    fx("alors il ne\ns'ensuit pas nécessairement", "alors \\emph{il ne\ns'ensuit pas nécessairement}"))
add(p, "(i): 'où B est le complété A^ de A'", "'complété' italic", "upright", "italics",
    fx("est le complété $\\widehat A$", "est le \\emph{complété} $\\widehat A$"))
add(p, "(i): 'un exemple où A est normal (donc vérifie (R_1))'", "'normal' italic", "upright", "italics",
    fx("est normal (donc vérifie", "est \\emph{normal} (donc vérifie"))
add(p, "(ii): 'et soit A l'anneau intègre k[U, V]/(UV — (U+V)^3) (dont le spectre'",
    "'soit A l'anneau intègre k[U, V]/(...)' (no '=', no comma)", "'soit $A=k[U,V]/(UV-(U+V)^3)$, l'anneau intègre'",
    "word",
    fx("et soit $A=k[U,V]/(UV-(U+V)^3)$, l'anneau intègre (dont",
       "et soit $A$ l'anneau intègre $k[U,V]/(UV-(U+V)^3)$ (dont"),
    note="Apply before the convention-7 edit of 'UV-(U+V)' that follows.")
add(p, "(ii): 'UV — (U+V)^3'",
    "long dash for the subtraction (40 px, broken by a 5 px gap; the = bars 34 px)", "minus sign", "convention",
    fx("UV-(U+V)", "UV\\setmin(U+V)"), convention=7,
    note="GLOBAL_ISSUES 23; \\setmin pending the convention-7 decision.")
add(p, "(ii): 'avec t = (u — v)/(u + v), qui vérifie l'équation t^2 = 1 + u + v, d'où l'on tire'",
    "both formulas in the running text, joined by ', qui vérifie l'équation'",
    "one display 't=(u-v)/(u+v),\\qquad t^2=1+u+v,': the words 'qui vérifie l'équation' are missing", "missing",
    fx("avec\n\\[\nt=(u-v)/(u+v),\\qquad t^2=1+u+v,\n\\]\nd'où l'on tire",
       "avec $t=(u-v)/(u+v)$, qui vérifie l'équation $t^2=1+u+v$, d'où l'on tire"),
    note="GLOBAL_ISSUES 51. Apply before the convention-7 edit of '(u-v)' that follows.")
add(p, "(ii): 't = (u — v)/(u + v)'", "long dash for the subtraction (40 px)", "minus sign", "convention",
    fx("(u-v)", "(u\\setmin v)"), convention=7)
add(p, "(ii): 'd'où l'on tire u = ½(t^3 + t^2 — t), v = ½(—t^3 + t^2 + t) et par suite'",
    "both formulas in the running text; no comma after the v formula", "one display joined by \\qquad, "
    "with a comma after the v formula", "other",
    fx("\\[\nu=\\frac{1}{2}(t^3+t^2-t),\\qquad\nv=\\frac{1}{2}(-t^3+t^2+t),\n\\]",
       "$u=\\frac{1}{2}(t^3+t^2-t)$,\n$v=\\frac{1}{2}(-t^3+t^2+t)$"),
    note="GLOBAL_ISSUES 21/51. Apply before the two convention-7 edits that follow.")
add(p, "(ii): 'u = ½(t^3 + t^2 — t)'", "long dash for the subtraction (40 px)", "minus sign", "convention",
    fx("t^2-t)", "t^2\\setmin t)"), convention=7)
add(p, "(ii): 'v = ½(—t^3 + t^2 + t)'", "long dash for the unary minus", "minus sign", "convention",
    fx("(-t^3", "(\\setmin t^3"), convention=7)
add(p, "(ii): 'engendrés respectivement par t — 1 et t + 1'", "long dash (41 px; = bars 34 px)", "minus sign",
    "convention", fx("par $t-1$", "par $t\\setmin 1$"), convention=7)
add(p, "(ii): 'f(1) = g(—1)'", "long dash (41 px)", "minus sign", "convention",
    fx("g(-1)", "g(\\setmin 1)"), convention=7)
add(p, "(ii): 'f(—1) = g(1)'", "long dash (41 px)", "minus sign", "convention",
    fx("f(-1)", "f(\\setmin 1)"), convention=7)
add(p, "(ii): 'les homomorphismes canoniques A^_m → B^_{r_1} et A^_m → B^_{r_2} sont bijectifs'",
    "both arrows in the running text, joined by 'et'",
    "one display joined by ',\\qquad': the word 'et' is missing", "missing",
    fx("\\[\n\\widehat A_{\\mathfrak m}\\to\\widehat B_{\\mathfrak r_1},\n\\qquad\n"
       "\\widehat A_{\\mathfrak m}\\to\\widehat B_{\\mathfrak r_2}\n\\]",
       "$\\widehat A_{\\mathfrak m}\\to\\widehat B_{\\mathfrak r_1}$ et\n"
       "$\\widehat A_{\\mathfrak m}\\to\\widehat B_{\\mathfrak r_2}$"),
    note="GLOBAL_ISSUES 51.")

# ---------------------------------------------------------------- validation
ok = True
texts = {}
for n in range(140, 145):
    raw = (RUN / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    texts[n] = raw.split("\n", 1)[1]  # drop the '% from ...' line (not in the source)
orig = dict(texts)
for i, x in enumerate(F):
    fix = x["fix"]
    if not fix:
        continue
    n = x["page"]
    c0 = orig[n].count(fix["old"])
    c1 = texts[n].count(fix["old"])
    if c0 != 1 or c1 != 1:
        ok = False
        print(f"PROBLEM #{i} p{n}: original count {c0}, sequential count {c1}: {fix['old']!r}")
    else:
        texts[n] = texts[n].replace(fix["old"], fix["new"])
print("validation", "OK" if ok else "FAILED")
for n in range(140, 145):
    rows = [x for x in F if x["page"] == n]
    conv = sum(1 for x in rows if x["kind"] == "convention")
    mis = sum(1 for x in rows if x["kind"] == "misprint_in_print")
    print(n, "normal", len(rows) - conv - mis, "convention", conv, "misprint", mis)
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("written", OUT, len(F))
