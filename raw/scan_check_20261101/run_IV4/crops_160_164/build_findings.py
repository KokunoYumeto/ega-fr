import json, sys
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101"
OUT = base + r"\run_IV4\findings_160_164.json"
NL = "\u23ce"  # placeholder for a line break in old/new strings


def R(s):
    return s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": R(old), "new": R(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


LD = "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."
G16 = "GLOBAL_ISSUES 16."
REM = "Judged with the remark body as roman (document-wide remark item)."

# ---------------- page 160 ----------------
add(160, "Remarque (18.10.3.1), l. 1-2", "dominant et quasi-compact in italics", "roman",
    "italics", None, "high", r"dominant et quasi-compact", r"\emph{dominant et quasi-compact}", REM)
add(160, "Remarque (18.10.3.1), l. 2", "(1.1.5) (no bold I, no comma)", "(I, 1.1.5)",
    "number", None, "high", r"(I, 1.1.5)", r"(1.1.5)",
    "EGA IV's own (1.1.5) misread as an EGA I reference (GLOBAL_ISSUES 78; crop p160_115.png).")
add(160, "Remarque (18.10.3.1), l. 3", "f peut être non ramifié et dominant sans que f soit étale, in italics", "roman",
    "italics", None, "high", r"$f$ peut être non ramifié et dominant sans que $f$ soit étale",
    r"\emph{$f$ peut être non ramifié et dominant sans que $f$ soit étale}", REM)
add(160, "Remarque (18.10.3.1): 'au point —1 et X_{2j+1}'", "—1 (long dash)", "$-1$",
    "convention", 7, "high", r"au point $-1$", r"au point $\setmin 1$",
    LD + " Measured: this dash is 40 px wide, the plus sign 35 px, the heading's em dash 46 px.")
add(160, "Remarque (18.10.3.1): 'le point —1 en (2j—1, 2j)'", "two long dashes", "$-1$, $(2j-1,2j)$",
    "convention", 7, "high", r"le point $-1$ en $(2j-1,2j)$", r"le point $\setmin 1$ en $(2j\setmin 1,2j)$",
    LD + " Two occurrences in one edit.")
add(160, "Remarque (18.10.3.1): 'sur X_{2j+1}, f_j est l'immersion fermée'", "f_j", "$f_j$ (as printed)",
    "misprint_in_print", None, "low", None, None,
    "Probably a slip for f (the clause for X_{2j} reads 'f ... égal sur X_{2j} à'); f_j is defined nowhere. "
    "Low confidence: it may be meant as the restriction of f; check before the corrected edition changes it. "
    "The TeX keeps the printed reading.",
    corrected=r"$f$")
add(160, "Remarque (18.10.3.1): 'transformant le point —1 en (2j+1, 2j)'", "—1 (long dash)", "$-1$",
    "convention", 7, "high", r"le point $-1$ en $(2j+1,2j)$", r"le point $\setmin 1$ en $(2j+1,2j)$", LD)
add(160, "Remarque (18.10.3.1): 'et le point —1 en (2j+1, 2j+2)'", "—1 (long dash)", "$-1$",
    "convention", 7, "high", r"et le point $-1$ en $(2j+1,2j+2)$", r"et le point $\setmin 1$ en $(2j+1,2j+2)$",
    LD + " Same spot as the next finding (a misprint the TeX keeps): the corrected edition reads +1 here "
    "instead of the \\setmin 1 this edit writes.")
add(160, "Remarque (18.10.3.1): 'et le point —1 en (2j+1, 2j+2)'", "—1 (second time in the sentence)",
    "$-1$ (as printed)", "misprint_in_print", None, "high", None, None,
    "The point -1 of X_{2j+1} already goes to (2j+1, 2j); the other point, +1, goes to (2j+1, 2j+2), where "
    "X_{2j+1} meets the image of X_{2j+2} (whose point -1 goes to (2j+1, 2j+2)). The TeX keeps the printed "
    "reading; after the convention-7 edit of the previous finding the diplomatic text has $\\setmin 1$ there, "
    "which the corrected edition replaces by $+1$.",
    corrected=r"$+1$")
add(160, "Corollaire (18.10.4), l. 3", "'plat' roman inside the italic statement", "italic (environment)",
    "convention", 6, "high", r"est plat au point $x$ et", r"est \textup{plat} au point $x$ et", "")
add(160, "Corollaire (18.10.4), l. 3", "'normal' roman inside the italic statement", "italic (environment)",
    "convention", 6, "high", r"$g^{-1}(s)$ normal au point $y$", r"$g^{-1}(s)$ \textup{normal} au point $y$", "")
add(160, "proof of (18.10.4)", "(0_I, 7.4.4) with bold 0", "$0_{\\mathrm I}$",
    "convention", 2, "high", r"($0_{\mathrm I}$, 7.4.4)", r"($\mathbf{0}_{\mathrm I}$, 7.4.4)", "")
add(160, "proof of (18.10.4)", "(0, 16.3.10) with a bare bold 0", "$0$",
    "convention", 2, "high", r"($0$, 16.3.10)", r"($\mathbf{0}$, 16.3.10)", "No subscript in the print.")
add(160, "Corollaire (18.10.5), l. 1", "(18.10.4) upright", "italic (environment)",
    "convention", 6, "high", r"Avec les notations de (18.10.4),", r"Avec les notations de \textup{(18.10.4)},", "")
add(160, "Corollaire (18.10.5), l. 2", "(ce qui sera par exemple le cas si g est lisse): roman clause, italic 'lisse', upright parentheses",
    "all italic", "convention", 6, "high", r"(ce qui sera par exemple le cas si $g$ est lisse)",
    r"\textup{(ce qui sera par exemple le cas si $g$ est \emph{lisse})}",
    "Both parentheses upright (crops p160_ce_paren.png, p160_lisse_paren.png); inside \\textup the \\emph gives italic.")
add(160, "Lemme (18.10.6), l. 1-2", "(Err_III, 20) with bold Err, upright parentheses and 20",
    "$\\mathrm{Err}$, parentheses and 20 italic (environment)", "font", None, "high",
    r"($\mathrm{Err}_{\mathrm{III}}$, 20)", r"\textup{($\mathbf{Err}_{\mathrm{III}}$, 20)}",
    "One edit for the bold Err (the edition writes \\mathbf{Err}) and the upright reference in the italic lemma "
    "(convention 6); same form as the p. 65 page fix.")
add(160, "Lemme (18.10.6) (i)", "label (i) upright", "italic", "convention", 6, "high",
    r"\item[(i)] L'ensemble", r"\item[\textup{(i)}] L'ensemble", G16)
add(160, "Lemme (18.10.6) (ii)", "label (ii) upright", "italic", "convention", 6, "high",
    r"\item[(ii)] Si $Y$ est irréductible", r"\item[\textup{(ii)}] Si $Y$ est irréductible", G16)

# ---------------- page 161 ----------------
add(161, "Lemme (18.10.6) (iii)", "label (iii) upright", "italic", "convention", 6, "high",
    r"\item[(iii)] Si l'ensemble", r"\item[\textup{(iii)}] Si l'ensemble",
    G16 + " The page begins with this item, as the marker has it (no boundary fix).")
add(161, "proof of (18.10.6), l. 1", "(0_I, 2.1.6) with bold 0", "$0_{\\mathrm I}$", "convention", 2, "high",
    r"(2.3.4) et ($0_{\mathrm I}$, 2.1.6)", r"(2.3.4) et ($\mathbf{0}_{\mathrm I}$, 2.1.6)", "")
add(161, "proof of (18.10.6), l. 4", "(0_I, 2.1.6) with bold 0", "$0_{\\mathrm I}$", "convention", 2, "high",
    r"irréductible ($0_{\mathrm I}$, 2.1.6)", r"irréductible ($\mathbf{0}_{\mathrm I}$, 2.1.6)", "")
add(161, "proof of (18.10.6), l. 5", "(II, 6.2.2) with bold II", "plain II", "convention", 2, "high",
    r"(II, 6.2.2)", r"(\textbf{II}, 6.2.2)", "")
add(161, "Proposition (18.10.7), l. 1-2", "(resp. intègre): 'resp.' and parentheses upright, 'intègre' italic",
    "all italic", "convention", 6, "high", r"irréductible (resp. intègre),",
    r"irréductible \textup{(resp.} intègre\textup{)},", "Closing parenthesis checked on an enlarged crop: upright.")
add(161, "Proposition (18.10.7), l. 3", "(resp. intègres): 'resp.' and parentheses upright", "all italic",
    "convention", 6, "high", r"irréductibles (resp. intègres) $X_\lambda$",
    r"irréductibles \textup{(resp.} intègres\textup{)} $X_\lambda$", "")
add(161, "proof of (18.10.7), l. 4", "(0_I, 2.1.6) with bold 0", "$0_{\\mathrm I}$", "convention", 2, "high",
    r"donc ($0_{\mathrm I}$, 2.1.6)", r"donc ($\mathbf{0}_{\mathrm I}$, 2.1.6)", "")
add(161, "Proposition (18.10.8), l. 2", "K = k(η) with bold italic k", "plain k", "convention", 1, "high",
    r"$K=k(\eta)$", r"$K=\boldsymbol{k}(\eta)$", "")
add(161, "Proposition (18.10.8), l. 4", "(1≤i≤n) with upright parentheses", "italic parentheses (environment)",
    "convention", 6, "high", r"corps $K_i$ ($1\leq i\leq n$)", r"corps $K_i$ \textup{($1\leq i\leq n$)}",
    "GLOBAL_ISSUES 26/96: parentheses around a formula inside an italic statement (enlarged crop).")
add(161, "Proposition (18.10.8), l. 4", "(17.6.2) upright", "italic (environment)", "convention", 6, "high",
    r"de $K$ (17.6.2).", r"de $K$ \textup{(17.6.2)}.", "")
add(161, "Proposition (18.10.8), l. 6", "(II, 6.3.6): bold II, upright reference", "plain II, italic reference",
    "convention", 2, "high", r"dans les $K_i$ (II, 6.3.6).", r"dans les $K_i$ \textup{(\textbf{II}, 6.3.6)}.",
    "One edit for convention 2 (bold II) and convention 6 (upright reference in the italic statement); count it under both.")
add(161, "proof of (18.10.8)", "(II, 6.3.9) with bold II", "plain II", "convention", 2, "high",
    r"(II, 6.3.9)", r"(\textbf{II}, 6.3.9)", "")
add(161, "Corollaire (18.10.9), l. 1", "(18.10.8) upright", "italic (environment)", "convention", 6, "high",
    r"Sous les hypothèses de (18.10.8),", r"Sous les hypothèses de \textup{(18.10.8)},", "")
add(161, "Corollaire (18.10.9), l. 2", "(autrement dit, pour que X soit un revêtement étale de Y): roman, italic 'revêtement étale', upright parentheses",
    "all italic", "convention", 6, "high", r"(autrement dit, pour que $X$ soit un revêtement étale de $Y$)",
    r"\textup{(autrement dit, pour que $X$ soit un \emph{revêtement étale} de $Y$)}",
    "Inside \\textup the \\emph gives italic, as printed.")
add(161, "proof of (18.10.9)", "(II, 6.1.5, (v)) with bold II", "plain II", "convention", 2, "high",
    r"(II, 6.1.5, (v))", r"(\textbf{II}, 6.1.5, (v))", "")
add(161, "proof of (18.10.9)", "(II, 6.1.10) with bold II", "plain II", "convention", 2, "high",
    r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)", "")
add(161, "(18.10.10), l. 2", "'non ramifiée sur' in italics", "roman", "italics", None, "high",
    r"est non ramifiée sur $Y$ si:", r"est \emph{non ramifiée sur} $Y$ si:", "")
add(161, "(18.10.10), last line", "'non ramifiée sur' in italics", "roman", "italics", None, "high",
    r"est non ramifiée sur $Y$ (ce qui", r"est \emph{non ramifiée sur} $Y$ (ce qui",
    "Adjacent to (not overlapping) the next finding.")
add(161, "end of page, (18.10.10) '(ce qui, par (18.10.3), | équivaut'", "page break inside the sentence",
    "blank lines before and after \\oldpage[IV-4]{162}", "marker", None, "high",
    "par (18.10.3)," + NL + NL, "par (18.10.3)," + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 162 finding removes the blank line after "
    "\\oldpage[IV-4]{162}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------- page 162 ----------------
add(162, "top of page", "p. 162 continues the sentence of (18.10.10) (first line not indented)",
    "blank line after \\oldpage[IV-4]{162}", "marker", None, "high",
    r"\oldpage[IV-4]{162}" + NL + NL + "équivaut", r"\oldpage[IV-4]{162}" + NL + "équivaut",
    "Part 2 of 2 with the last p. 161 finding; both blank lines must go.")
add(162, "(18.10.10), l. 1", "'étale sur' in italics", "roman", "italics", None, "high",
    r"est étale sur $Y$).", r"est \emph{étale sur} $Y$).", "")
add(162, "(18.10.10), l. 4", "'non ramifiée sur' (before A) in italics", "roman", "italics", None, "high",
    r"est non ramifiée sur $A$ au lieu", r"est \emph{non ramifiée sur} $A$ au lieu",
    "The quoted « non ramifiée sur Y » is roman, as in the TeX.")
add(162, "Corollaire (18.10.12), l. 3", "'non ramifiées' roman, 'sur' italic", "all italic",
    "convention", 6, "high", r"qui sont non ramifiées sur $Y$.", r"qui sont \textup{non ramifiées} sur $Y$.",
    "Enlarged crop p162_nonram.png.")
add(162, "Proposition (18.10.13) (i)", "label (i) upright", "italic", "convention", 6, "high",
    r"\item[(i)] Le corps", r"\item[\textup{(i)}] Le corps", G16)
add(162, "Proposition (18.10.13) (ii)", "label (ii) upright", "italic", "convention", 6, "high",
    r"\item[(ii)] Soit $L$", r"\item[\textup{(ii)}] Soit $L$", G16)
add(162, "Proposition (18.10.13) (ii), end", "(« transitivité » de la non-ramification) roman, upright parentheses",
    "italic", "convention", 6, "high", r"(« transitivité » de la non-ramification)",
    r"\textup{(« transitivité » de la non-ramification)}", "")
add(162, "Proposition (18.10.13) (iii)", "label (iii) upright", "italic", "convention", 6, "high",
    r"\item[(iii)] Soient $Y'$", r"\item[\textup{(iii)}] Soient $Y'$", G16)
add(162, "Proposition (18.10.13) (iii), l. 3", "(propriété de « translation ») roman, upright parentheses",
    "italic", "convention", 6, "high", r"(propriété de « translation »)",
    r"\textup{(propriété de « translation »)}", "")
add(162, "proof of (18.10.13)", "(I, 3.4.9) with bold I and comma", "plain I", "convention", 2, "high",
    r"(I, 3.4.9)", r"(\textbf{I}, 3.4.9)",
    "Genuine EGA I reference (bold I followed by a comma; crop p162_I349.png), not EGA IV's own (1.3.4.9).")
add(162, "Corollaire (18.10.14), l. 3-4", "(Bourbaki, Alg., chap. VIII, § 8, déf. 1) de: roman with italic 'Alg.'; 'et de' italic",
    "citation italic and 'Alg.' upright (\\emph inside the italic environment)", "convention", 6, "high",
    r"composée (Bourbaki, \emph{Alg.}, chap.~VIII, \textsection~8, déf.~1) de $L$",
    r"composée \textup{(Bourbaki, \emph{Alg.}, chap.~VIII, \textsection~8, déf.~1) de} $L$",
    "The 'de' after the parenthesis is roman too (enlarged crop p162_bourbaki.png); inside \\textup the \\emph gives italic.")
add(162, "end of page, proof of (18.10.14) '..., et L_1 | est l'une'", "page break inside the sentence",
    "blank lines before and after \\oldpage[IV-4]{163}", "marker", None, "high",
    "séparables de $K'$, et $L_1$" + NL + NL, "séparables de $K'$, et $L_1$" + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 163 finding removes the blank line after "
    "\\oldpage[IV-4]{163}; apply both.")

# ---------------- page 163 ----------------
add(163, "top of page", "p. 163 continues the sentence (first line not indented)",
    "blank line after \\oldpage[IV-4]{163}", "marker", None, "high",
    r"\oldpage[IV-4]{163}" + NL + NL + "est l'une", r"\oldpage[IV-4]{163}" + NL + "est l'une",
    "Part 2 of 2 with the last p. 162 finding; both blank lines must go.")
add(163, "proof of (18.10.14), l. 1-2", "la fermeture intégrale de Y dans L est somme de préschémas dont l'un est la fermeture intégrale de Y dans L_1",
    "same (as printed)", "misprint_in_print", None, "medium", None, None,
    "The argument concerns Y' and the factors of L(x)_K K' (it applies (18.10.13, (iii))): L_1 is a factor of "
    "L(x)_K K', not of L. Probably the authors' slip (Y for Y' twice, L for L(x)_K K'); no erratum found in the "
    "IV-4 errata list; check before the corrected edition changes it. The TeX keeps the printed reading.",
    corrected=r"la fermeture intégrale de $Y'$ dans $L\otimes_K K'$ est somme de préschémas dont l'un est la fermeture intégrale de $Y'$ dans $L_1$")
add(163, "proof of (18.10.14), l. 3", "Le corollaire résulte donc aussitôt de (18.10.14).", "(18.10.14) (as printed)",
    "misprint_in_print", None, "high", None, None,
    "Self-reference inside the proof of (18.10.14); the corollary follows from (18.10.13) (its (iii)). "
    "The TeX keeps the printed reading.",
    corrected=r"(18.10.13)")
add(163, "(18.10.15), l. 3", "'projectif' in italics", "roman", "italics", None, "high",
    r"un $A$-module projectif de type fini", r"un $A$-module \emph{projectif} de type fini", "")
add(163, "(18.10.15), l. 6", "'étale' in italics", "roman", "italics", None, "high",
    r"que $C$ est étale (18.10.10)", r"que $C$ est \emph{étale} (18.10.10)", "")
add(163, "(18.10.15), l. 6-7", "'discriminant' in italics", "roman", "italics", None, "high",
    r"que le discriminant $d_{C/A}$", r"que le \emph{discriminant} $d_{C/A}$", "")
add(163, "(18.10.15), l. 7", "first 'inversible' in italics (the last one is roman)", "roman", "italics", None, "high",
    r"$\Spec(A)$ est inversible dans $A$. Dans", r"$\Spec(A)$ est \emph{inversible} dans $A$. Dans", "")
add(163, "(18.10.15), l. 8", "'libre' in italics", "roman", "italics", None, "high",
    r"un $A$-module libre et", r"un $A$-module \emph{libre} et", "")
add(163, "Théorème (18.10.16), l. 3", "K = k(η) with bold italic k", "plain k", "convention", 1, "high",
    r"sur $K=k(\eta)$", r"sur $K=\boldsymbol{k}(\eta)$", "")
add(163, "Théorème (18.10.16), 'On pose n = ... (somme des degrés séparables des L_i).'",
    "set in the line, ending the paragraph (flush left, ragged right); 'Soit y ...' then starts a new indented paragraph",
    "displayed formula, and 'Soit $y$' runs on after the display without a paragraph break", "other", None, "high",
    "On pose" + NL + r"\[" + NL + r"  n=[L:K]=\sum_i[L_i:K],\qquad n_s=\sum_i[L_i:K]_s \quad\text{(somme des degrés séparables des $L_i$)}." + NL + r"\]" + NL + "Soit $y$",
    r"On pose $n=[L:K]=\sum_i[L_i:K]$, $n_s=\sum_i[L_i:K]_s$ (somme des degrés séparables des $L_i$)." + NL + NL + "Soit $y$",
    "Display vs inline only; no connecting word lost or added (measured: the formula line starts at the left "
    "margin, 373 px, and ends at 1931 px; 'Soit y' is indented, 485 px). Apply THIS one before the next finding "
    "(\\textup on the parenthesis), whose 'old' it leaves in place.")
add(163, "Théorème (18.10.16), the same line", "(somme des degrés séparables des L_i) roman, upright parentheses",
    "italic (\\text inherits the environment's italic)", "convention", 6, "high",
    r"(somme des degrés séparables des $L_i$)", r"\textup{(somme des degrés séparables des $L_i$)}",
    "Apply after the previous finding (display made inline): this 'old' occurs exactly once before and after it.")
add(163, "Théorème (18.10.16), 'Soit y un point ...'", "'géométriquement unibranche' roman", "italic (environment)",
    "convention", 6, "high", r"point géométriquement unibranche de $Y$, et",
    r"point \textup{géométriquement unibranche} de $Y$, et", "Enlarged crop p163_soity.png.")
add(163, "Théorème (18.10.16), 'Soit y un point ...'", "k(y) with bold italic k", "plain k", "convention", 1, "high",
    r"$n(y)$ la somme des degrés séparables sur $k(y)$", r"$n(y)$ la somme des degrés séparables sur $\boldsymbol{k}(y)$",
    "Adjacent to (not overlapping) the next finding.")
add(163, "Théorème (18.10.16), 'Soit y un point ...'", "'isolés' roman", "italic (environment)",
    "convention", 6, "high", r"des points isolés de $f^{-1}(y)$", r"des points \textup{isolés} de $f^{-1}(y)$", "")
add(163, "Théorème (18.10.16) (i)", "label (i) upright", "italic", "convention", 6, "high",
    r"\item[(i)] On a", r"\item[\textup{(i)}] On a", G16)
add(163, "Théorème (18.10.16) (ii)", "label (ii) upright", "italic", "convention", 6, "high",
    r"\item[(ii)] Supposons $X$ réduit", r"\item[\textup{(ii)}] Supposons $X$ réduit", G16)
add(163, "proof, heading A)", "label A) upright, the title italic", "label italic (inside \\emph)", "italics", None, "high",
    r"\emph{A) Réduction", r"A) \emph{Réduction",
    "Hand-made heading label upright in the print (GLOBAL_ISSUES 76 pattern; enlarged crop p163_A.png).")
add(163, "proof A), l. 3", "Puisque f^{-1}(η) est fini,", "est finie,", "word", None, "high",
    r"Puisque $f^{-1}(\eta)$ est finie,", r"Puisque $f^{-1}(\eta)$ est fini,",
    "The TeX changes the printed masculine 'fini' (crop p163_fini.png); both agreements occur in the print "
    "((18.10.6) 'si f^{-1}(η) est fini', (18.10.8) 'est finie'), so this is not a misprint.")
add(163, "proof A), l. 5", "k(y) with bold italic k", "plain k", "convention", 1, "high",
    r"$n_\lambda(y)$ est la somme des degrés séparables sur $k(y)$",
    r"$n_\lambda(y)$ est la somme des degrés séparables sur $\boldsymbol{k}(y)$", "")
add(163, "proof A), last lines", "(II, 6.1.5, (v)) with bold II", "plain II", "convention", 2, "high",
    r"(II, 6.1.5, (v))", r"(\textbf{II}, 6.1.5, (v))", "")
add(163, "proof A), last lines", "(II, 6.1.10) with bold II", "plain II", "convention", 2, "high",
    r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)", "")
add(163, "proof, heading B)", "label B) upright, the title italic", "label italic (inside \\emph)", "italics", None, "high",
    r"\emph{B) Réduction", r"B) \emph{Réduction", "As A) (enlarged crop p163_B.png).")
add(163, "end of page, '... supposer donc X réduit. | D'autre part'",
    "page break inside a paragraph: the last line of p. 163 is full and the first line of p. 164 is not indented",
    "blank lines before and after \\oldpage[IV-4]{164}", "marker", None, "high",
    "supposer donc $X$ réduit." + NL + NL, "supposer donc $X$ réduit." + NL,
    "The marker is at the right place. Measured: p. 164's first line starts at 398 px like the lines after it "
    "(indented lines start near 480-517 px), p. 163's last line runs to the right margin. Part 1 of 2: the first "
    "p. 164 finding removes the blank line after \\oldpage[IV-4]{164}; apply both.")

# ---------------- page 164 ----------------
add(164, "top of page", "'D'autre part, ...' continues the paragraph (not indented)",
    "blank line after \\oldpage[IV-4]{164}", "marker", None, "high",
    r"\oldpage[IV-4]{164}" + NL + NL + "D'autre part", r"\oldpage[IV-4]{164}" + NL + "D'autre part",
    "Part 2 of 2 with the last p. 163 finding; both blank lines must go.")
add(164, "l. 3", "'fini' (où g est fini) in italics", "roman", "italics", None, "high",
    r"où $g$ est fini et $j$", r"où $g$ est \emph{fini} et $j$", "")
add(164, "l. 4", "(I, 5.2.2) with bold I and comma", "plain I", "convention", 2, "high",
    r"(I, 5.2.2)", r"(\textbf{I}, 5.2.2)",
    "Genuine EGA I reference (crop p164_I522.png), not EGA IV's own (1.5.2.2).")
add(164, "l. 8", "(0_I, 1.2.7) with bold 0", "$0_{\\mathrm I}$", "convention", 2, "high",
    r"($0_{\mathrm I}$, 1.2.7)", r"($\mathbf{0}_{\mathrm I}$, 1.2.7)", "")
add(164, "l. 10", "'fini' (lorsqu'en outre f est un morphisme fini) in italics", "roman", "italics", None, "high",
    r"lorsqu'en outre $f$ est un morphisme fini", r"lorsqu'en outre $f$ est un morphisme \emph{fini}", "")
add(164, "'On est ainsi ramené ...'", "'fini' in italics", "roman", "italics", None, "high",
    r"est en outre un morphisme fini.", r"est en outre un morphisme \emph{fini}.", "")
add(164, "'On est ainsi ramené ...', l. 5", "'intègre' in italics", "roman", "italics", None, "high",
    r"et que $Y$ est intègre, on conclut", r"et que $Y$ est \emph{intègre}, on conclut", "")
add(164, "'On est ainsi ramené ...', l. 6", "'étale aux points de' in italics", "roman", "italics", None, "high",
    r"que $f$ est étale aux points de $f^{-1}(y)$, donc", r"que $f$ est \emph{étale aux points de} $f^{-1}(y)$, donc", "")
add(164, "proof, heading C)", "label C) upright, the title italic", "label italic (inside \\emph)", "italics", None, "high",
    r"\emph{C) Réduction", r"C) \emph{Réduction", "As A) on p. 163 (enlarged crop p164_C.png).")
add(164, "C), 'Si n'(y'), n' et n'_s sont ...'", "no paragraph break: the line continues the paragraph of C) (not indented)",
    "blank line before 'Si $n'(y')$' (new paragraph)", "other", None, "high",
    "domine $Y'$ (2.3.7)." + NL + NL + "Si $n'(y')$", "domine $Y'$ (2.3.7)." + NL + "Si $n'(y')$",
    "Measured: the line starts at 406 px like the other full lines (the C) line is indented, 517 px) and the "
    "line before it runs to the right margin.")
add(164, "C), 'on a n'_s = n_s et n'(y') = n(y) (I, 6.4.8)'", "(I, 6.4.8) with bold I and comma", "plain I",
    "convention", 2, "high", r"(I, 6.4.8)", r"(\textbf{I}, 6.4.8)",
    "Genuine EGA I reference (crop p164_I648.png), not EGA IV's own (1.6.4.8).")
add(164, "C), 'de la remarque (8.1.2, a))'", "a) italic, including its parenthesis", "$a$) (italic a, upright parenthesis)",
    "italics", None, "high", r"(8.1.2, $a$))", r"(8.1.2, \emph{a)})", "GLOBAL_ISSUES 88 (crop p164_812a.png).")
add(164, "end of page, '... par passage à la limite, | on en déduit'", "page break inside the sentence",
    "blank lines before and after \\oldpage[IV-4]{165}", "marker", None, "high",
    "par passage à la limite," + NL + NL, "par passage à la limite," + NL,
    "The marker is at the right place (p. 164 ends with 'par passage à la limite,' above the footnote). Part 1 "
    "of 2: the blank line AFTER \\oldpage[IV-4]{165} lies in the p. 165 segment (outside these pages) and must go "
    "too: '\\oldpage[IV-4]{165}\\n\\non en déduit' -> '\\oldpage[IV-4]{165}\\non en déduit'.")

# ---------------- checks ----------------
src = open(base + r"\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex", encoding="utf-8").read()


def segment(n):
    a = src.index("\\oldpage[IV-4]{%d}" % n)
    b = src.index("\\oldpage[IV-4]{%d}" % (n + 1))
    return src[a:b]


ok = True
pages = {}
for n in range(160, 165):
    pages[n] = open(base + r"\run_IV4\page_%03d.tex" % n, encoding="utf-8").read().replace("\r\n", "\n")
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    o = d["fix"]["old"]
    c1 = pages[d["page"]].count(o)
    c2 = segment(d["page"]).count(o)
    if c1 != 1 or c2 != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], c1, c2, repr(o)[:120])
    if d["fix"]["old"] == d["fix"]["new"]:
        ok = False
        print("NO CHANGE", i)

# sequential application on the source segments, in list order, to make sure every edit applies
for n in range(160, 165):
    s = segment(n)
    for d in F:
        if d["page"] == n and d["fix"]:
            if s.count(d["fix"]["old"]) != 1:
                ok = False
                print("FAILS IN SEQUENCE", n, repr(d["fix"]["old"])[:100])
            s = s.replace(d["fix"]["old"], d["fix"]["new"], 1)
    open(base + r"\run_IV4\crops_160_164\applied_%d.tex" % n, "w", encoding="utf-8", newline="\n").write(s)

print("all old strings unique and applicable:" if ok else "PROBLEMS FOUND", ok)
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for n in range(160, 165):
    print(n, "normal", cnt[(n, "normal")], "convention", cnt[(n, "convention")], "misprint", cnt[(n, "misprint")])
if ok:
    json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("written", OUT, len(F))
