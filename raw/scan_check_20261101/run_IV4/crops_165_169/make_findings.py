"""Build findings_165_169.json and verify every edit against the current source (simulating apply_fixes.py)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
CUR = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\current\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN / "findings_165_169.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


N = "\n"
JUDGED_REMARK = ""

# ---------------------------------------------------------------- page 165
add(165, "top of page: page break 164/165 inside 'par passage à la limite, | on en déduit'",
    "p. 165 begins mid-sentence with 'on en déduit que X′ est réduit (8.7.1)'; p. 164 ends 'par passage à la limite,'",
    "blank line after \\oldpage[IV-4]{165} (and another before it)", "marker", None, "high",
    r"\oldpage[IV-4]{165}" + N + N + "on en déduit", r"\oldpage[IV-4]{165}" + N + "on en déduit",
    "BOUNDARY FIX (page break with p. 164). The marker is at the right place. Part 2 of 2: the blank line BEFORE the "
    "marker must go too ('par passage à la limite,' + blank line, end of the p. 164 segment; edit old "
    "'par passage à la limite,\\n\\n' -> 'par passage à la limite,\\n', for the 160-164 checker or the coordinator). "
    "\\oldpage ends with \\ignorespaces, which does not skip a \\par.")
add(165, "l. 2: 'séparables sur k(η); les corps'", "bold italic k", "plain k", "convention", 1, "high",
    r"séparables sur $k(\eta)$; les corps", r"séparables sur $\boldsymbol{k}(\eta)$; les corps")
add(165, "l. 3: 'séparables sur k(η′) (4.6.1)'", "bold italic k", "plain k", "convention", 1, "high",
    r"séparables sur $k(\eta')$ (4.6.1)", r"séparables sur $\boldsymbol{k}(\eta')$ (4.6.1)")
add(165, "heading 'D) Fin de la démonstration. —'",
    "'D)' upright, 'Fin de la démonstration.' italic (crop p165_D.png)",
    "\\emph{D) Fin de la démonstration.}: the label D) italic too", "italics", None, "high",
    r"\emph{D) Fin de la démonstration.}", r"D) \emph{Fin de la démonstration.}",
    "Hand-made proof-part heading (GLOBAL_ISSUES 76 pattern); A), B), C) on pp. 162-164 have the same form.")
add(165, "D), l. 2: 'X est somme des sous-préschémas ouverts Spec(O_X,x_j) = X_j'", "'somme' italic",
    "roman (no \\emph)", "italics", None, "high",
    r"est somme des sous-préschémas ouverts $\Spec(", r"est \emph{somme} des sous-préschémas ouverts $\Spec(")
add(165, "D): 'Mais puisque k(y) est séparablement clos et que les k(x_j) sont algébriques sur k(y)'",
    "bold italic k (three times)", "plain k", "convention", 1, "high",
    r"Mais puisque $k(y)$ est séparablement clos et que les $k(x_j)$ sont algébriques sur $k(y)$",
    r"Mais puisque $\boldsymbol{k}(y)$ est séparablement clos et que les $\boldsymbol{k}(x_j)$ sont algébriques sur $\boldsymbol{k}(y)$")
add(165, "D): 'des extensions radicielles de k(y)'", "'radicielles' italic", "roman (no \\emph)", "italics", None,
    "high", r"des extensions radicielles de", r"des extensions \emph{radicielles} de")
add(165, "D): 'de k(y), donc m = n(y)'", "bold italic k", "plain k", "convention", 1, "high",
    r"de $k(y)$, donc $m=n(y)$", r"de $\boldsymbol{k}(y)$, donc $m=n(y)$",
    "Shares the word 'de' with the 'radicielles' edit; the two apply in either order.")
add(165, "D): 'que chacun des X_j est irréductible;'", "'irréductible' italic", "roman (no \\emph)", "italics", None,
    "high", r"chacun des $X_j$ est irréductible;", r"chacun des $X_j$ est \emph{irréductible};")
add(165, "D): 'comme les X_j sont réduits, ils sont intègres;'", "'réduits' and 'intègres' italic",
    "roman (no \\emph)", "italics", None, "high",
    r"sont réduits, ils sont intègres;", r"sont \emph{réduits}, ils sont \emph{intègres};")
add(165, "D): 'k(ξ_j) est une extension séparable de k(η) de degré 1, donc isomorphe à k(η)'",
    "bold italic k (three times)", "plain k", "convention", 1, "high",
    r"$k(\xi_j)$ est une extension séparable de $k(\eta)$ de degré 1, donc isomorphe à $k(\eta)$;",
    r"$\boldsymbol{k}(\xi_j)$ est une extension séparable de $\boldsymbol{k}(\eta)$ de degré 1, donc isomorphe à $\boldsymbol{k}(\eta)$;")
add(165, "D): 'est un morphisme fini et birationnel;'", "'fini et birationnel' italic", "roman (no \\emph)",
    "italics", None, "high", r"un morphisme fini et birationnel;", r"un morphisme \emph{fini et birationnel};")
add(165, "D): 'X_j est intègre et par hypothèse Y est normal;'", "'intègre' and 'normal' italic",
    "roman (no \\emph)", "italics", None, "high",
    r"$X_j$ est intègre et par hypothèse $Y$ est normal;",
    r"$X_j$ est \emph{intègre} et par hypothèse $Y$ est \emph{normal};")
add(165, "D): 'f|X_j est un isomorphisme, ce qui prouve que f est étale'", "'isomorphisme' and 'étale' italic",
    "roman (no \\emph)", "italics", None, "high",
    r"est un isomorphisme, ce qui prouve que $f$ est étale, et termine",
    r"est un \emph{isomorphisme}, ce qui prouve que $f$ est \emph{étale}, et termine")
add(165, "(18.10.17.1): the statement 'Soient f : X → Y ... on a n(y) ≤ n(y′).'",
    "the whole statement italic after the bold number (scan strip 3)",
    "roman: the env environment has an upright body", "italics", None, "high",
    r"Soient $f:X\to Y$ un morphisme séparé et quasi-fini, $y$ un point de $Y$ tel que $f$ soit universellement ouvert aux points de $f^{-1}(y)$. Alors, pour toute générisation $y'$ de $y$, on a $n(y)\leq n(y')$.",
    r"\emph{Soient $f:X\to Y$ un morphisme séparé et quasi-fini, $y$ un point de $Y$ tel que $f$ soit universellement ouvert aux points de $f^{-1}(y)$. Alors, pour toute générisation $y'$ de $y$, on a $n(y)\leq n(y')$.}",
    "Same form as the italic passages of the env statements (16.2.1), (16.3.5).")
add(165, "proof of (18.10.17.1): 'la restriction à X d'un morphisme fini g : X′ → Y'", "'fini' italic",
    "roman (no \\emph)", "italics", None, "high", r"d'un morphisme fini $g:X'\to Y$",
    r"d'un morphisme \emph{fini} $g:X'\to Y$")
add(165, "proof of (18.10.17.1): 'point générique de Y (I, 3.6.5)'", "bold I followed by a comma",
    "plain I", "convention", 2, "high", r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)",
    "Genuine EGA I reference (bold I), not EGA IV's own (1.3.6.5).")
add(165, "proof of (18.10.17.1): 'i^{-1}(X̄) = (i^{-1}(X))‾ autrement dit f^{-1}(y′) est dense'",
    "no comma before 'autrement dit' (crop p165_autrement.png)",
    "'\\overline{i^{-1}(X)}$, autrement dit': comma (silent correction)", "misprint_in_print", None, "medium",
    r"\overline{i^{-1}(X)}$, autrement dit", r"\overline{i^{-1}(X)}$ autrement dit",
    "Missing comma before 'autrement dit' (the print sets it everywhere else, e.g. '(4.6.1), autrement dit' on the "
    "same page). The fix removes only the comma.", corrected=r"\overline{i^{-1}(X)}$, autrement dit")
add(165, "last paragraph: 'la somme des nombres [k(x) : k(y)]_s'", "bold italic k (twice)", "plain k",
    "convention", 1, "high", r"$[k(x):k(y)]_s$", r"$[\boldsymbol{k}(x):\boldsymbol{k}(y)]_s$")
add(165, "end of p. 165: page break 165/166 inside 'est au plus égale | au nombre n(y′)'",
    "p. 166 begins mid-sentence with 'au nombre n(y′)'", "blank lines before and after \\oldpage[IV-4]{166}",
    "marker", None, "high", "est au plus égale" + N + N, "est au plus égale" + N,
    "The marker is at the right place. Part 1 of 2: the first p. 166 finding removes the blank line after "
    "\\oldpage[IV-4]{166}; apply both.")

# ---------------------------------------------------------------- page 166
add(166, "top of page: page break 165/166", "mid-sentence continuation 'au nombre n(y′) (pour le morphisme g)'",
    "blank line after \\oldpage[IV-4]{166}", "marker", None, "high",
    r"\oldpage[IV-4]{166}" + N + N + "au nombre", r"\oldpage[IV-4]{166}" + N + "au nombre",
    "Part 2 of 2 with the last p. 165 finding; both blank lines must go.")
add(166, "l. 3: 'on montre, comme dans (18.10.16, C)) que l'on peut se ramener'",
    "no comma after 'C))' (crop p166_C.png), although the incise opens with a comma after 'montre'",
    "'C)), que': the TeX adds the closing comma (silent correction)", "misprint_in_print", None, "medium",
    r"(18.10.16, C)), que", r"(18.10.16, C)) que",
    "Missing closing comma of the incise (same case as p. 126). The fix removes only the comma.",
    corrected=r"(18.10.16, C)), que")
add(166, "l. 3-4: 'avec O_Y,y strictement local.'", "'strictement local' italic", "roman (no \\emph)",
    "italics", None, "high", r"avec $\sh{O}_{Y,y}$ strictement local. Alors",
    r"avec $\sh{O}_{Y,y}$ \emph{strictement local}. Alors")
add(166, "l. 6: 'l'hypothèse que g est ouvert en un de ces points'", "'ouvert' italic (crop p166_1103.png)",
    "roman (no \\emph)", "italics", None, "high", r"que $g$ est ouvert en un de ces points",
    r"que $g$ est \emph{ouvert} en un de ces points")
add(166, "l. 7: 'X_j correspondant domine Y (1.10.3)'",
    "(1.10.3): light old-style 1 and full stops, no bold I, no comma (crop p166_1103.png)", "(I, 10.3)",
    "number", None, "high", r"correspondant domine $Y$ (I, 10.3)", r"correspondant domine $Y$ (1.10.3)",
    "EGA IV's own (1.10.3) misread as an EGA I reference (GLOBAL_ISSUES 78).")
add(166, "'On tire ensuite de (18.10.17.1) que les conclusions de (15.5.1) sont encore valables ...'",
    "'On tire ensuite de (18.10.17.1) que' roman; 'les conclusions de' italic; '(15.5.1)' upright; the rest italic "
    "to 'présentation finie.' (crop p166_ontire.png)",
    "the whole sentence in one \\emph", "italics", None, "high",
    r"\emph{On tire ensuite de (18.10.17.1) que les conclusions de (15.5.1) sont encore valables",
    r"On tire ensuite de (18.10.17.1) que \emph{les conclusions de} (15.5.1) \emph{sont encore valables",
    "The existing closing brace after 'présentation finie.' now closes the second \\emph.")
add(166, "proof of (i): 'l'ensemble E des points z ∈ Y tels que n(z) ≥ n(y)'",
    "z ∈ Y, n(z) (crop p166_zEY.png)", "y′ ∈ Y, n(y′): the TeX renames the variable", "formula", None, "high",
    r"des points $y'\in Y$ tels que $n(y')\geq n(y)$", r"des points $z\in Y$ tels que $n(z)\geq n(y)$")
add(166, "proof of (i): 'il suffit, en vertu de (1.10.1),'", "(1.10.1): old-style 1, full stops, no bold, no comma",
    "(I, 10.1)", "number", None, "high", r"en vertu de (I, 10.1)", r"en vertu de (1.10.1)",
    "EGA IV's own (1.10.1) misread as an EGA I reference (GLOBAL_ISSUES 78).")
add(166, "proof of (ii): 'suivant la méthode de (8.1.2, a))'",
    "label a) wholly italic, then the upright closing parenthesis (crop p166_a.png)", "a) upright",
    "italics", None, "high", r"la méthode de (8.1.2, a))", r"la méthode de (8.1.2, \emph{a)})",
    "GLOBAL_ISSUES 88 form.")
add(166, "proof of (ii): 'supposer que l'anneau O_Y,y est strictement local.'", "'strictement local' italic",
    "roman (no \\emph)", "italics", None, "high", r"est strictement local. Appliquant",
    r"est \emph{strictement local}. Appliquant")
add(166, "proof of (ii): 'Appliquant (18.5.11, c))'", "label c) wholly italic (crop p166_c.png)", "c) upright",
    "italics", None, "high", r"Appliquant (18.5.11, c))", r"Appliquant (18.5.11, \emph{c)})",
    "GLOBAL_ISSUES 88 form.")
add(166, "proof of (ii): 'X est somme de n sous-préschémas ouverts'", "'somme' italic", "roman (no \\emph)",
    "italics", None, "high", r"$X$ est somme de $n$ sous-préschémas", r"$X$ est \emph{somme} de $n$ sous-préschémas")
add(166, "proof of (ii): 'qui sont finis sur Y'", "'finis' italic", "roman (no \\emph)", "italics", None, "high",
    r"qui sont finis sur $Y$", r"qui sont \emph{finis} sur $Y$")
add(166, "proof of (ii): 'les corps k(x_j) étant des extensions algébriques de k(y)'", "bold italic k (twice)",
    "plain k", "convention", 1, "high", r"les corps $k(x_j)$ étant des extensions algébriques de $k(y)$",
    r"les corps $\boldsymbol{k}(x_j)$ étant des extensions algébriques de $\boldsymbol{k}(y)$")
add(166, "proof of (ii): 'sont radicielles, et par suite n(y) = n'", "'radicielles' italic", "roman (no \\emph)",
    "italics", None, "high", r"sont radicielles, et par suite", r"sont \emph{radicielles}, et par suite")
add(166, "proof of (ii): 'X_j domine Y (1.10.3), donc'", "(1.10.3): old-style 1, full stops, no bold, no comma "
    "(crop p166_1103b.png)", "(I, 10.3)", "number", None, "high", r"$X_j$ domine $Y$ (I, 10.3), donc",
    r"$X_j$ domine $Y$ (1.10.3), donc", "GLOBAL_ISSUES 78.")
add(166, "proof of (ii): 'étant un morphisme fini, est surjectif (II, 6.1.10)'",
    "'fini' and 'surjectif' italic (crop p166_surj.png)", "roman (no \\emph)", "italics", None, "high",
    r"étant un morphisme fini, est surjective", r"étant un morphisme \emph{fini}, est \emph{surjective}",
    "Same spot as the next finding (misprint): apply this one first; the misprint edit's 'old' ('surjective') "
    "occurs once before and after it.")
add(166, "proof of (ii): 'donc la restriction de f à X_j, ..., est surjectif'",
    "'surjectif' (masculine) although the subject is 'la restriction' (crop p166_surj.png)",
    "'surjective' (silent correction)", "misprint_in_print", None, "high", r"surjective", r"surjectif",
    "Agreement slip (with 'morphisme'). Apply after the italics edit above; the fix changes only the word ending.",
    corrected=r"est \emph{surjective}")
add(166, "proof of (ii): '(II, 6.1.10)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 6.1.10). L", r"(\textbf{II}, 6.1.10). L")
add(166, "proof of (ii): 'L'hypothèse que z ⇝ n(z) est constant dans Y'", "wavy arrow (crop p166_surj.png)",
    "\\mapsto", "symbol", None, "high", r"$z\mapsto n(z)$", r"$z\leadsto n(z)$")
add(166, "proof of (ii): 'que X″ ∩ f^{-1}(z) = ∅ pour tout z ∈ Y'", "z twice (crop p166_surj.png)",
    "y′ twice: the TeX renames the variable", "formula", None, "high",
    r"$X''\cap f^{-1}(y')=\varnothing$ pour tout $y'\in Y$", r"$X''\cap f^{-1}(z)=\varnothing$ pour tout $z\in Y$")
add(166, "footnote (1) to Lemme (18.10.18): 'mais où on ne suppose pas X et Y réduits'",
    "'où on ne suppose' (crop p166_fn.png)", "'où l'on ne suppose'", "word", None, "high",
    r"mais où l'on ne suppose pas", r"mais où on ne suppose pas")
add(166, "proof of (18.10.18): 'X et Y affines, donc f séparé,'", "'donc' before 'f séparé' (crop p166_sep.png)",
    "'affines, $f$ séparé': 'donc' missing", "missing", None, "high", r"$Y$ affines, $f$", r"$Y$ affines, donc $f$",
    "Independent of the next finding ('séparé' italic).")
add(166, "proof of (18.10.18): 'donc f séparé, et on est ramené'", "'séparé' italic (crop p166_sep.png)",
    "roman (no \\emph)", "italics", None, "high", r"séparé, et on est ramené", r"\emph{séparé}, et on est ramené")
add(166, "proof of (18.10.18): 'il s'agit de prouver que f est radiciel.'", "'radiciel' italic (crop p166_sep.png)",
    "roman (no \\emph)", "italics", None, "high", r"il s'agit de prouver que $f$ est radiciel.",
    r"il s'agit de prouver que $f$ est \emph{radiciel}.")
add(166, "proof of (18.10.18): 'que f^{-1}(y) est radiciel sur k(y).'", "bold italic k", "plain k", "convention", 1,
    "high", r"est radiciel sur $k(y)$.", r"est radiciel sur $\boldsymbol{k}(y)$.")
add(166, "end of p. 166: page break 166/167 inside 'qui est un anneau local et un A-module | fidèlement plat'",
    "p. 166 ends '... avec A = O_Y,y. Soit alors A′ = ^{hs}A, qui est un anneau local et un A-module' in one "
    "paragraph; p. 167 begins 'fidèlement plat (18.8.8)'",
    "\\oldpage[IV-4]{167} stands before 'Soit alors ...', with blank lines before and after it (paragraph break)",
    "marker", None, "high", r"avec $A=\sh{O}_{Y,y}$." + N + N, r"avec $A=\sh{O}_{Y,y}$." + N,
    "Marker 167 stands one sentence too early. Part 1 of 2: removes the blank line before the marker (the print has "
    "no paragraph break before 'Soit alors'); the first p. 167 finding moves the marker after 'un $A$-module'. "
    "Apply both.")

# ---------------------------------------------------------------- page 167
add(167, "top of page: printed p. 167 begins with 'fidèlement plat (18.8.8)'",
    "'Soit alors A′ = ^{hs}A, qui est un anneau local et un A-module' is the last line of p. 166 (page_166_s4.png)",
    "\\oldpage[IV-4]{167} before 'Soit alors', followed by a blank line", "marker", None, "high",
    r"\oldpage[IV-4]{167}" + N + N + r"Soit alors $A'={}^{hs}\!A$, qui est un anneau local et un $A$-module fidèlement plat",
    r"Soit alors $A'={}^{hs}\!A$, qui est un anneau local et un $A$-module" + N + r"\oldpage[IV-4]{167}" + N + "fidèlement plat",
    "Part 2 of 2 with the last p. 166 finding: the marker moves after 'un $A$-module' (mid-sentence: no blank lines). "
    "After this edit 'Soit alors ... $A$-module' belongs to the p. 166 segment.")
add(167, "l. 2: 'Posons Y′ = Spec(A′), X′ = X_(Y′), f′ = f_(Y′) : X′ → Y′'", "X′ = X_(Y′) (crop p167_Xp.png)",
    "X' = X ×_Y Y': the TeX rewrites the notation", "formula", None, "high",
    r"Posons $Y'=\Spec(A')$, $X'=X\times_Y Y'$", r"Posons $Y'=\Spec(A')$, $X'=X_{(Y')}$")
add(167, "l. 5: 'est radiciel sur k(y′);'", "bold italic k", "plain k", "convention", 1, "high",
    r"est radiciel sur $k(y')$;", r"est radiciel sur $\boldsymbol{k}(y')$;")
add(167, "l. 6: 'contient au plus un point (17.6.1, c′))'",
    "'au plus un point' italic; label c′) wholly italic, then an upright parenthesis (crop p167_c.png)",
    "roman, c') upright", "italics", None, "high", r"contient au plus un point (17.6.1, c'))",
    r"contient \emph{au plus un point} (17.6.1, \emph{c$'$)})",
    "Label written as elsewhere in ega4-18 ('(17.6.2, \\emph{c$'$)})').")
add(167, "second paragraph: 'f séparé, étale et birationnel et montrons que'",
    "no comma after 'birationnel' (crop p167_bira.png)", "'birationnel, et montrons': comma added", "punctuation",
    None, "high", r"étale et birationnel, et montrons", r"étale et birationnel et montrons")
add(167, "second paragraph, end: 'l'hypothèse que f est birationnel.'", "'birationnel' italic", "roman (no \\emph)",
    "italics", None, "high", r"contredit l'hypothèse que $f$ est birationnel.",
    r"contredit l'hypothèse que $f$ est \emph{birationnel}.")
add(167, "Proposition (18.10.19): '(i.e. une Y-application rationnelle de Y dans X)'",
    "'(i.e.' and the closing parenthesis roman, the rest italic (crop p167_ie.png)",
    "'(c'est-à-dire une ...)', all italic in the environment", "word", None, "high",
    r"(c'est-à-dire une $Y$-application rationnelle de $Y$ dans $X$)",
    r"\textup{(i.e.} une $Y$-application rationnelle de $Y$ dans $X$\textup{)}",
    "One edit for the wording (the TeX writes 'c'est-à-dire' for the print's 'i.e.') and the upright 'i.e.' and "
    "parentheses inside the italic statement (convention 6, next entry).")
add(167, "Proposition (18.10.19): '(i.e.' and ')'", "roman inside the italic statement", "italic",
    "convention", 6, "high", None, None, "Covered by the edit of the preceding finding.")
add(167, "Proposition (18.10.19): 'le domaine de définition de g (I, 7.2.1)'",
    "bold I followed by a comma; the reference upright inside the italic statement (crop p167_ie.png)",
    "plain I, set italic by the environment", "convention", 2, "high",
    r"de définition de $g$ (I, 7.2.1)", r"de définition de $g$ \textup{(\textbf{I}, 7.2.1)}",
    "One edit for the bold I (convention 2) and the upright reference (convention 6, next entry). Genuine EGA I "
    "reference.")
add(167, "Proposition (18.10.19): '(I, 7.2.1)' upright", "upright reference in the italic statement",
    "italic", "convention", 6, "high", None, None, "Covered by the edit of the preceding finding.")
add(167, "Proposition (18.10.19): 'pour tout point y ∈ Y—U'", "long dash (crop p167_prop.png)", "minus sign",
    "convention", 7, "high", r"$y\in Y-U$", r"$y\in Y\setmin U$")
add(167, "Proposition (18.10.19): 'Si, pour toute partie fermée irréductible T de X'",
    "'irréductible' roman inside the italic statement (crop p167_prop.png)", "italic", "convention", 6, "high",
    r"partie fermée irréductible $T$ de $X$", r"partie fermée \emph{irréductible} $T$ de $X$",
    "Roman (emphasised) word in the italic statement; \\emph gives upright there.")
add(167, "proof of (18.10.19): 'il résulte de (I, 7.2.2)'", "bold I followed by a comma", "plain I",
    "convention", 2, "high", r"(I, 7.2.2)", r"(\textbf{I}, 7.2.2)", "Genuine EGA I reference.")
add(167, "proof of (18.10.19): 'g(U) = u(U), étant réduit, est induit aussi par Z'", "g(U) = u(U) (crop p167_gU.png)",
    "Z|_U = u(U): the TeX rewrites the formula", "formula", None, "high", r"$Z|_U=u(U)$", r"$g(U)=u(U)$")
add(167, "proof of (18.10.19): 'la restriction f′ = f|Z de f'", "f|Z, Z on the line (crop p167_gU.png)",
    "f|_Z (Z as a subscript)", "formula", None, "high", r"$f'=f|_Z$", r"$f'=f|Z$")
add(167, "proof of (18.10.19): 'un morphisme birationnel de Z dans Y'", "'birationnel' italic (crop p167_gU.png)",
    "roman (no \\emph)", "italics", None, "high", r"est un morphisme birationnel de $Z$ dans $Y$",
    r"est un morphisme \emph{birationnel} de $Z$ dans $Y$")
add(167, "proof of (18.10.19): 'au cas où Y est intègre; alors u(U)'", "'intègre' italic", "roman (no \\emph)",
    "italics", None, "high", r"au cas où $Y$ est intègre; alors", r"au cas où $Y$ est \emph{intègre}; alors",
    "The second 'intègre' ('Z est aussi intègre') is roman in the print, as in the TeX.")
add(167, "proof of (18.10.19): 'Alors (I, 8.2.7) puisque f′ est dominant'", "bold I followed by a comma "
    "(crop p167_alors.png)", "plain I", "convention", 2, "high", r"(I, 8.2.7)", r"(\textbf{I}, 8.2.7)",
    "Genuine EGA I reference. Independent of the next finding (comma).")
add(167, "proof of (18.10.19): 'Alors (I, 8.2.7) puisque'", "no comma after the reference (crop p167_alors.png)",
    "'8.2.7), puisque': comma added", "punctuation", None, "high", r"8.2.7), puisque", r"8.2.7) puisque")
add(167, "proof of (18.10.19): 'l'homomorphisme O_Y,y → O_Z,x est injectif'", "O_{Y,y} (crop p167_alors.png)",
    "O_{Y,f(x)}: the TeX rewrites the subscript", "formula", None, "high",
    r"\sh{O}_{Y,f(x)}\to\sh{O}_{Z,x}", r"\sh{O}_{Y,y}\to\sh{O}_{Z,x}")
add(167, "proof of (18.10.19): 'que f′ est un morphisme étale;'", "'étale' italic", "roman (no \\emph)", "italics",
    None, "high", r"est un morphisme étale; étant", r"est un morphisme \emph{étale}; étant")
add(167, "proof of (18.10.19), end: 'donc égal à Y, i.e. on a Z_y ≠ ∅ pour tout y ∈ Y'",
    "'i.e. on a' (crop p167_ie2.png)", "'c'est-à-dire': the TeX rewords and drops 'on a'", "word", None, "high",
    r"c'est-à-dire $Z_y\ne\varnothing$", r"i.e. on a $Z_y\ne\varnothing$")
add(167, "Remarque (18.10.20), l. 2: 'est essentiellement propre s'il est localement de type fini et si,'",
    "'essentiellement propre' and 'localement de type fini' italic (crop p167_rem.png)", "no italics of their own",
    "italics", None, "high", r"est essentiellement propre s'il est localement de type fini et si,",
    r"est \emph{essentiellement propre} s'il est \emph{localement de type fini} et si,",
    "Judged as roman remark text (remark font is document-wide).")
add(167, "Remarque (18.10.20), printed p. 168 l. 2: 'l'application canonique (II, 7.3.2.2)'", "bold II",
    "plain II", "convention", 2, "high", r"(II, 7.3.2.2)", r"(\textbf{II}, 7.3.2.2)",
    "Printed p. 168; the text is in the p. 167 segment until the marker move below: apply before it.")
add(167, "Remarque (18.10.20), printed p. 168 l. 2: 'relative au Y′-préschéma X ×_Y Y′, est bijective.'",
    "a comma between 'X ×_Y Y′' and 'est bijective' (crop p168_top.png)",
    "no comma (silent correction)", "misprint_in_print", None, "medium",
    r"$X\times_Y Y'$ est bijective", r"$X\times_Y Y'$, est bijective",
    "Spurious comma between subject and verb (no comma opens an incise before 'relative'). Printed p. 168; p. 167 "
    "segment: apply before the marker move below. The fix adds only the comma.",
    corrected=r"$X\times_Y Y'$ est bijective")
add(167, "end of p. 167: page break 167/168 inside 'et si, | pour tout Y-schéma'",
    "p. 167 ends 'et si,'; p. 168 begins 'pour tout Y-schéma de la forme Y′ = Spec(A)'; 'est bijective. Le "
    "raisonnement de (II, 7.3.8)' runs on in one paragraph (no indent, crops p168_top.png, p168_margin.png)",
    "\\oldpage[IV-4]{168} stands after 'est bijective.', between blank lines (paragraph break)", "marker", None,
    "high", "est bijective." + N + N, "est bijective." + N,
    "Marker 168 stands two lines too late. Part 1 of 3 (apply in this order): this removes the blank line before "
    "the old marker; part 2 (next finding) inserts the marker after 'et si,'; part 3 (first p. 168 finding) removes "
    "the old marker and the blank line after it. Apply after the two edits above on the same printed lines.")
add(167, "end of p. 167: insert \\oldpage[IV-4]{168} after 'et si,'",
    "p. 168 begins 'pour tout Y-schéma'", "marker two lines too late", "marker", None, "high",
    r"et si, pour tout $Y$-schéma", "et si," + N + r"\oldpage[IV-4]{168}" + N + r"pour tout $Y$-schéma",
    "Part 2 of 3 of the marker move (mid-sentence, no blank lines). The 'old' shares 'et si,' with the italics edit "
    "of Remarque (18.10.20) above; they apply in either order. Until part 3 is applied the file has two "
    "\\oldpage[IV-4]{168} (apply_fixes.py treats the span as page 168).")

# ---------------------------------------------------------------- page 168
add(168, "top of page_168.tex: the old \\oldpage[IV-4]{168} before 'Le raisonnement'",
    "printed p. 168 begins two lines earlier ('pour tout Y-schéma ...'); 'Le raisonnement' continues the paragraph",
    "\\oldpage[IV-4]{168} followed by a blank line", "marker", None, "high",
    r"\oldpage[IV-4]{168}" + N + N + "Le raisonnement", "Le raisonnement",
    "Part 3 of 3 of the marker move: apply after the two p. 167 marker edits (the new marker is then in place).")
add(168, "l. 3: 'Le raisonnement de (II, 7.3.8)'", "bold II", "plain II", "convention", 2, "high",
    r"de (II, 7.3.8) prouve", r"de (\textbf{II}, 7.3.8) prouve")
add(168, "l. 4: 'est séparé et que pour tout changement de base'", "'séparé' italic (crop p168_top.png)",
    "roman (no \\emph)", "italics", None, "high", r"est séparé et que", r"est \emph{séparé} et que",
    "Judged as roman remark text. Independent of the next finding.")
add(168, "l. 4: 'et que pour tout changement de base'", "no comma after 'que' (crop p168_top.png)",
    "'et que, pour tout': comma added", "punctuation", None, "high", r"et que, pour tout changement",
    r"et que pour tout changement")
add(168, "l. 5: 'où Y″ est localement noethérien, l'image par'", "'localement noethérien' italic",
    "roman (no \\emph)", "italics", None, "high", r"où $Y''$ est localement noethérien, l'image",
    r"où $Y''$ est \emph{localement noethérien}, l'image", "Judged as roman remark text.")
add(168, "l. 5-6: 'de toute partie fermée irréductible de X″ est fermée.'", "'irréductible' and 'fermée' italic",
    "roman (no \\emph)", "italics", None, "high", r"partie fermée irréductible de $X''$ est fermée.",
    r"partie fermée \emph{irréductible} de $X''$ est \emph{fermée}.", "Judged as roman remark text.")
add(168, "l. 6: 'Dire que f est propre (pour Y localement noethérien)'", "'propre' italic", "roman (no \\emph)",
    "italics", None, "high", r"Dire que $f$ est propre (pour", r"Dire que $f$ est \emph{propre} (pour",
    "Judged as roman remark text.")
add(168, "l. 7: 'que f est essentiellement propre et de type fini (II, 7.3.8)'",
    "'essentiellement propre et de type fini' italic", "roman (no \\emph)", "italics", None, "high",
    r"est essentiellement propre et de type fini", r"est \emph{essentiellement propre et de type fini}",
    "Judged as roman remark text. Independent of the next finding.")
add(168, "l. 7: '(II, 7.3.8);'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 7.3.8);", r"(\textbf{II}, 7.3.8);")
add(168, "end of Remarque (18.10.20): 'si Y est localement noethérien, réduit et géométriquement unibranche, et si "
    "le morphisme f : X → Y est essentiellement propre et non ramifié, alors toute Y-section rationnelle de f est "
    "partout définie.'",
    "the three phrases italic ('Y' upright before '-section')", "roman (no \\emph)", "italics", None, "high",
    r"si $Y$ est localement noethérien, réduit et géométriquement unibranche, et si le morphisme $f:X\to Y$ est essentiellement propre et non ramifié, alors toute $Y$-section rationnelle de $f$ est partout définie.",
    r"si $Y$ est \emph{localement noethérien, réduit et géométriquement unibranche}, et si le morphisme $f:X\to Y$ est \emph{essentiellement propre et non ramifié}, alors \emph{toute $Y$-section rationnelle de $f$ est partout définie}.",
    "Judged as roman remark text.")
add(168, "before Proposition (18.10.21): 'La proposition suivante généralise le critère (17.15.5) de lissité d'un "
    "morphisme X → Y lorsque Y n'est pas le spectre d'un corps :'",
    "an indented roman paragraph between the remark and the proposition (page_168_s2.png)",
    "missing", "missing", None, "high",
    r"\end{remark}" + N + N + r"\begin{proposition}[18.10.21]",
    r"\end{remark}" + N + N + r"La proposition suivante généralise le critère (17.15.5) de lissité d'un morphisme $X\to Y$ lorsque $Y$ n'est pas le spectre d'un corps:" + N + N + r"\begin{proposition}[18.10.21]",
    "Sentence restored after \\end{remark} (colon written as elsewhere in the file, '(15.5.2):').")
add(168, "Proposition (18.10.21): 'supposons l'anneau O_Y,y intègre et géométriquement unibranche.'",
    "'intègre' and 'géométriquement unibranche' roman inside the italic statement, 'et' italic (crop p168_prop.png)",
    "italic (environment)", "convention", 6, "high",
    r"$\sh{O}_{Y,y}$ intègre et géométriquement unibranche. Soit",
    r"$\sh{O}_{Y,y}$ \emph{intègre} et \emph{géométriquement unibranche}. Soit",
    "Roman (emphasised) words in the italic statement; \\emph gives upright there.")
add(168, "Proposition (18.10.21): 'du O_X,x-module (Ω¹_X/Y)_x'", "italic Ω (sheaf of differentials; crop "
    "p168_prop.png)", "upright \\Omega", "font", None, "high", r"-module $(\Omega^1_{X/Y})_x$",
    r"-module $(\varOmega^1_{X/Y})_x$", "Sheaf of differentials: italic Omega (\\varOmega) in the print.")
add(168, "Proposition (18.10.21): '(égal au rang du k(x)-espace vectoriel (Ω¹_X/Y)_x ⊗_O_X,x k(x))'",
    "the parenthesis roman inside the italic statement, 'rang' italic; bold italic k twice; italic Ω "
    "(crop p168_prop.png)", "all italic (environment), plain k, upright \\Omega", "convention", 6, "high",
    r"(égal au rang du $k(x)$-espace vectoriel $(\Omega^1_{X/Y})_x\otimes_{\sh{O}_{X,x}}k(x))$",
    r"\textup{(égal au \emph{rang} du $\boldsymbol{k}(x)$-espace vectoriel $(\varOmega^1_{X/Y})_x\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x))$}",
    "One edit for the roman parenthesis with the italic 'rang' (\\emph inside \\textup), the two bold k "
    "(convention 1) and the italic Omega (next two entries).")
add(168, "Proposition (18.10.21): 'k(x)-espace vectoriel', '⊗ k(x)'", "bold italic k (twice)", "plain k",
    "convention", 1, "high", None, None, "Covered by the edit of the preceding finding.")
add(168, "Proposition (18.10.21): '(Ω¹_X/Y)_x ⊗ ...' in the parenthesis", "italic Ω", "upright \\Omega", "font",
    None, "high", None, None, "Covered by the edit of the preceding-but-one finding.")
add(168, "proof of (18.10.21), second paragraph: '((16.4.22) et (0_I, 5.2.2))'", "bold 0 with subscript I "
    "(crop p168_si.png)", "plain 0", "convention", 2, "high", r"et ($0_{\mathrm I}$, 5.2.2))",
    r"et ($\mathbf{0}_{\mathrm I}$, 5.2.2))")
add(168, "proof of (18.10.21): 'il existe r sections s_i (1 ≤ i ≤ r) de O_X'", "s_i (crop p168_si.png)",
    "t_i: the TeX renames the sections", "formula", None, "high", r"$r$ sections $t_i$", r"$r$ sections $s_i$")
add(168, "proof of (18.10.21): 'telles que les sections d_X/Y(s_i) engendrent'", "d_{X/Y}(s_i), with parentheses",
    "d_{X/Y}t_i", "formula", None, "high", r"$d_{X/Y}t_i$", r"$d_{X/Y}(s_i)$")
add(168, "proof of (18.10.21): 'engendrent Ω¹_X/Y. Soit'", "italic Ω", "upright \\Omega", "font", None, "high",
    r"engendrent $\Omega^1_{X/Y}$. Soit", r"engendrent $\varOmega^1_{X/Y}$. Soit")
add(168, "proof of (18.10.21): 'défini par les s_i (considérées comme sections ...)'", "s_i", "t_i", "formula",
    None, "high", r"défini par les $t_i$", r"défini par les $s_i$")
add(168, "proof of (18.10.21): '(II, 1.2.7)'", "bold II", "plain II", "convention", 2, "high",
    r"au-dessus de $Y$) (II, 1.2.7)", r"au-dessus de $Y$) (\textbf{II}, 1.2.7)")
add(168, "display (exact sequence (16.4.19)): 'g*(Ω¹_Z/Y) → Ω¹_X/Y → Ω¹_X/Z → 0.'", "italic Ω (three times)",
    "upright \\Omega", "font", None, "high",
    r"g^*(\Omega^1_{Z/Y})\longrightarrow\Omega^1_{X/Y}\longrightarrow\Omega^1_{X/Z}\longrightarrow0.",
    r"g^*(\varOmega^1_{Z/Y})\longrightarrow\varOmega^1_{X/Y}\longrightarrow\varOmega^1_{X/Z}\longrightarrow0.")
add(168, "after the display: 'Comme les dT_i (1 ≤ i ≤ r) engendrent Ω¹_Z/Y,'", "italic Ω (crop p168_omega.png)",
    "upright \\Omega", "font", None, "high", r"engendrent $\Omega^1_{Z/Y}$, il résulte",
    r"engendrent $\varOmega^1_{Z/Y}$, il résulte")
add(168, "after the display: 'l'homomorphisme g*(Ω¹_Z/Y) → Ω¹_X/Y est surjectif'", "italic Ω (twice)",
    "upright \\Omega", "font", None, "high", r"$g^*(\Omega^1_{Z/Y})\to\Omega^1_{X/Y}$",
    r"$g^*(\varOmega^1_{Z/Y})\to\varOmega^1_{X/Y}$")
add(168, "after the display: 'donc Ω¹_X/Z = 0,'", "italic Ω", "upright \\Omega", "font", None, "high",
    r"donc $\Omega^1_{X/Z}=0$", r"donc $\varOmega^1_{X/Z}=0$", "Independent of the next finding.")
add(168, "after the display: 'donc Ω¹_X/Z = 0, et g est par suite'", "comma after '= 0' (crop p168_omega.png)",
    "no comma", "punctuation", None, "high", r"=0$ et $g$ est par suite", r"=0$, et $g$ est par suite")
add(168, "'g est par suite non ramifié (17.4.1)'", "'non ramifié' italic (crop p168_omega.png)",
    "roman (no \\emph)", "italics", None, "high", r"par suite non ramifié (17.4.1)",
    r"par suite \emph{non ramifié} (17.4.1)", "Independent of the preceding finding.")
add(168, "'Nous allons voir que g est étale au point x'", "'étale' italic", "roman (no \\emph)", "italics", None,
    "high", r"que $g$ est étale au point $x$, et compte tenu", r"que $g$ est \emph{étale} au point $x$, et compte tenu")
add(168, "end of p. 168: page break 168/169 inside 'intègre et géométriquement | unibranche'",
    "p. 169 begins mid-sentence with 'unibranche, il en est de même'",
    "blank lines before and after \\oldpage[IV-4]{169}", "marker", None, "high",
    "est supposé intègre et géométriquement" + N + N, "est supposé intègre et géométriquement" + N,
    "The marker is at the right place. Part 1 of 2: the first p. 169 finding removes the blank line after "
    "\\oldpage[IV-4]{169}; apply both.")

# ---------------------------------------------------------------- page 169
add(169, "top of page: page break 168/169", "mid-sentence continuation 'unibranche, il en est de même'",
    "blank line after \\oldpage[IV-4]{169}", "marker", None, "high",
    r"\oldpage[IV-4]{169}" + N + N + "unibranche", r"\oldpage[IV-4]{169}" + N + "unibranche",
    "Part 2 of 2 with the last p. 168 finding; both blank lines must go.")
add(169, "l. 1: 'il en est de même de O_Z,z (17.5.7) où z = g(x)'", "reference (17.5.7) after O_Z,z "
    "(crop p169_top.png)", "no reference", "missing", None, "high",
    r"même de $\sh{O}_{Z,z}$ où $z=g(x)$", r"même de $\sh{O}_{Z,z}$ (17.5.7) où $z=g(x)$")
add(169, "l. 4: 'correspondant est dominant,'", "'dominant' italic (crop p169_Tn.png)", "roman (no \\emph)",
    "italics", None, "high", r"correspondant est dominant, puisque", r"correspondant est \emph{dominant}, puisque")
add(169, "l. 4: 'est intègre (I, 1.2.7).'", "bold I followed by a comma", "plain I", "convention", 2, "high",
    r"intègre (I, 1.2.7).", r"intègre (\textbf{I}, 1.2.7).", "Genuine EGA I reference. Independent of the next finding.")
add(169, "l. 5: 'Soit y′ le point générique de Y = ...'",
    "'Soit' at the left margin without indent: the paragraph continues (crops p169_Tn.png, p169_margin.png)",
    "blank line before 'Soit $y'$' (new paragraph)", "other", None, "high",
    "1.2.7)." + N + N + r"Soit $y'$", "1.2.7)." + N + r"Soit $y'$")
add(169, "l. 6: 'Z = Spec(O_Y,y[T_1, ..., T_n])'", "T_n (crop p169_Tn.png)", "T_r (silent correction)",
    "misprint_in_print", None, "high", r"[T_1,\ldots,T_r])$ qui est intègre", r"[T_1,\ldots,T_n])$ qui est intègre",
    "Z = Y[T_1, ..., T_r] has r indeterminates (display on p. 168 and h^{-1}(y′) = Spec(k(y′)[T_1, ..., T_r]) two "
    "lines below). The fix restores the printed n only.", corrected=r"[T_1,\ldots,T_r])$ qui est intègre")
add(169, "l. 9: 'h^{-1}(y′) = Spec(k(y′)[T_1, ..., T_r])'", "bold italic k", "plain k", "convention", 1, "high",
    r"\Spec(k(y')[T_1", r"\Spec(\boldsymbol{k}(y')[T_1")
add(169, "'à toute composante irréductible de dimension ≥ r de f^{-1}(y′)'", "'de dimension' italic",
    "roman (no \\emph)", "italics", None, "high", r"irréductible de dimension $\geq r$",
    r"irréductible \emph{de dimension} $\geq r$")
add(169, "'une telle composante contenant une générisation de x; a fortiori'", "'une générisation de x' "
    "(no x′; crop p169_gen.png)", "'une générisation $x'$ de $x$': x′ added", "extra", None, "high",
    r"une générisation $x'$ de $x$; \emph{a fortiori}", r"une générisation de $x$; \emph{a fortiori}")
add(169, "'Le lemme suivant généralise (0, 21.9.1)'", "bare bold 0 (crop p169_lemma.png)", "plain 0",
    "convention", 2, "high", r"généralise (0, 21.9.1)", r"généralise (\textbf{0}, 21.9.1)")
add(169, "'et (0, 21.9.2) :'", "bare bold 0", "plain 0", "convention", 2, "high",
    r"et (0, 21.9.2):", r"et (\textbf{0}, 21.9.2):")
add(169, "Lemme (18.11.1), l. 1: 'Soient k un corps, A un anneau local'", "comma after 'corps' (crop p169_lemma.png)",
    "semicolon", "punctuation", None, "high", r"Soient $k$ un corps; $A$", r"Soient $k$ un corps, $A$")
add(169, "Lemme (18.11.1), item (i)", "label upright (crop p169_items.png)",
    "\\item[(i)] (italic in the statement)", "convention", 6, "high", r"\item[(i)] Si le",
    r"\item[\textup{(i)}] Si le", "GLOBAL_ISSUES 16.")
add(169, "Lemme (18.11.1), item (ii)", "label upright (crop p169_items.png)",
    "\\item[(ii)] (italic in the statement)", "convention", 6, "high", r"\item[(ii)] Si de plus",
    r"\item[\textup{(ii)}] Si de plus", "GLOBAL_ISSUES 16.")
add(169, "Lemme (18.11.1) (ii), display 'dim(A) + rg_K(Ω¹_K/k) — rg_K(Υ_K/k).'",
    "long dash for the minus (crop p169_disp1.png)", "minus sign", "convention", 7, "high",
    r"(\Omega^1_{K/k})-\operatorname{rg}_K(\Upsilon_{K/k}).",
    r"(\Omega^1_{K/k})\setmin\operatorname{rg}_K(\Upsilon_{K/k}).",
    "Subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier IV-4 fixes.")
add(169, "Lemme (18.11.1): 'En outre, pour tout sous-corps k_0 de k ...' after the list",
    "indented as a new paragraph (crop p169_enoutre.png)",
    "text right after \\end{enumerate} (set without the indent)", "other", None, "high",
    r"\end{enumerate}" + N + "En outre, pour tout sous-corps",
    r"\end{enumerate}" + N + N + "En outre, pour tout sous-corps",
    "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern).")
add(169, "Lemme (18.11.1), last display: 'dim(A) + rg_K(Ω¹_K/k) — rg_K(Υ_K/k) + rg_k(Ω¹_k/k_0).'",
    "Ω¹_{K/k} and Υ_{K/k} (no k_0) in the second and third terms; long dash for the minus (crop p169_disp2.png)",
    "Ω¹_{K/k_0} and Υ_{K/k_0}", "formula", None, "high",
    r"\operatorname{rg}_K(\Omega^1_{K/k_0})-\operatorname{rg}_K(\Upsilon_{K/k_0})",
    r"\operatorname{rg}_K(\Omega^1_{K/k})\setmin\operatorname{rg}_K(\Upsilon_{K/k})",
    "The print is right: from 0 → Ω_{k/k_0}⊗A → Ω̂_{A/k_0} → Ω̂_{A/k} → 0 (A formally smooth over k) the rank is "
    "rank Ω̂_{A/k} + rg_k(Ω_{k/k_0}), i.e. the (ii) value plus rg_k(Ω_{k/k_0}); the TeX's K/k_0 terms would add "
    "rg_k(Ω_{k/k_0}) − rg_k(Υ_{k/k_0}) again. The edit also writes the long-dash minus (convention 7, next entry).")
add(169, "same display: the minus before rg_K(Υ_K/k)", "long dash", "minus sign", "convention", 7, "high",
    None, None, "Covered by the edit of the preceding finding.")
add(169, "proof of (18.11.1): 'ayant été prouvée dans (0, 20.7.15)'", "bare bold 0", "plain 0", "convention", 2,
    "high", r"prouvée dans (0, 20.7.15)", r"prouvée dans (\textbf{0}, 20.7.15)")
add(169, "proof of (18.11.1): 'par la démonstration de (0, 21.9.2)'", "bare bold 0", "plain 0", "convention", 2,
    "high", r"démonstration de (0, 21.9.2)", r"démonstration de (\textbf{0}, 21.9.2)")
add(169, "proof of (18.11.1): 'l'énoncé de (0, 21.9.2) faisant'", "bare bold 0", "plain 0", "convention", 2,
    "high", r"l'énoncé de (0, 21.9.2)", r"l'énoncé de (\textbf{0}, 21.9.2)")
add(169, "proof of (18.11.1): 'l'égalité de Cartier (0, 21.7.1)'", "bare bold 0", "plain 0", "convention", 2,
    "high", r"Cartier (0, 21.7.1))", r"Cartier (\textbf{0}, 21.7.1))")
add(169, "Lemme (18.11.2), display (18.11.2.1): 'rg_L(Ω¹_L/k) — rg_L(Υ_L/k) ≥ n.'", "long dash for the minus",
    "minus sign", "convention", 7, "high",
    r"(\Omega^1_{L/k})-\operatorname{rg}_L(\Upsilon_{L/k})\geq n",
    r"(\Omega^1_{L/k})\setmin\operatorname{rg}_L(\Upsilon_{L/k})\geq n", "Subtraction (GLOBAL_ISSUES 23).")

# ---------------------------------------------------------------- verification
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


def simulate(t, skip_misprints):
    problems = []
    for k, x in enumerate(F):
        fx = x["fix"]
        if not fx or (skip_misprints and x["kind"] == "misprint_in_print"):
            continue
        s, e = locate(t, x["page"])
        seg = t[s:e]
        c = seg.count(fx["old"])
        if c != 1:
            problems.append((k, x["page"], c, fx["old"][:70]))
            continue
        t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    return t, problems


src = SRC.read_text(encoding="utf-8")
final, probs = simulate(src, False)
print("diplomatic simulation problems:", probs)
cur = CUR.read_text(encoding="utf-8")
cur_final, cprobs = simulate(cur, True)
print("current-edition replay (misprints skipped) problems:", cprobs)

pages = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(164, 171)}
for k, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    o = fx["old"]
    pc = pages[x["page"]].count(o)
    fc = src.count(o)
    bal = (fx["new"].count("{") - fx["new"].count("}")) - (o.count("{") - o.count("}"))
    flag = "" if pc == 1 else "  <-- page count %d" % pc
    if fc != 1:
        flag += "  (file count %d)" % fc
    if bal:
        flag += "  BRACE IMBALANCE %d" % bal
    if flag:
        print(k, x["page"], repr(o[:60]), flag)

# resulting text of the pages, for a read-through
s0 = final.find(r"\oldpage[IV-4]{165}")
s1 = final.find(r"\oldpage[IV-4]{170}")
(RUN / "crops_165_169" / "result_165_169.txt").write_text(final[s0:s1], encoding="utf-8")

counts = {}
for x in F:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts per page (normal/convention/misprint):", counts, "total", len(F))
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
