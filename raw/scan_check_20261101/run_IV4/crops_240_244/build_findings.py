"""Build findings_240_244.json and check every 'old' (page text, LF) and the current source."""
import json, pathlib, sys

RUN = pathlib.Path("user/Documents/ega_scan_check_20261101/run_IV4")
SRC = pathlib.Path("user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-20-fr.tex")
OUT = RUN / "findings_240_244.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, after=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_after"] = after  # index (in F) of the fix whose result this 'old' is taken from
    F.append(d)
    return len(F) - 1


# ---------------- p. 240 ----------------
add(240, "l. 1: 'pour λ⩽μ et Ps.hom_{S_λ}(X_λ, Y_λ) → Ps.hom_S(X, Y) sont définies'",
    "no comma after 'λ⩽μ' (crop c240_top.png)", "comma after $\\lambda\\leq\\mu$",
    "punctuation", None, "high",
    r"pour $\lambda\leq\mu$, et $\operatorname{Ps.hom}",
    r"pour $\lambda\leq\mu$ et $\operatorname{Ps.hom}",
    "Not a boundary fix: the marker and its (absent) blank lines are right; p. 240 continues the sentence after the display flush left.")

add(240, "Lemme (20.3.8.2): 'l'une des conditions (i), (ii) de (20.3.8)'",
    "(i), (ii) upright in the italic statement (crop c240_lem2.png)", "italic (lemma environment)",
    "convention", 6, "high",
    r"conditions~(i),~(ii) de \sref{IV.20.3.8} soit vérifiée",
    r"conditions~\textup{(i)},~\textup{(ii)} de \sref{IV.20.3.8} soit vérifiée",
    "GLOBAL_ISSUES 16 (roman-numeral labels upright inside italic statements).")

i_dans = add(240, "Lemme (20.3.8.2), last line: 'et dans ce cas U_μ est schématiquement dense'",
    "'dans' is BOLD italic (wrong fount), mid-line: side by side with the light 'dans' of 'dense dans X_λ' on the same line (crops c240_dans2.png, side_dans.png); ink area d 278 / a 215 / n 213 / s 122 px against 224 / 162 / 166 / 102, stroke 4.3 / 4.2 / 4.0 / 3.5 against 3.5 / 3.2 / 3.1 / 3.0 px; 'et' before it and 'ce' after it are of normal weight",
    "normal italic (silent correction)",
    "misprint_in_print", None, "high",
    r"et dans ce cas $U_\mu$",
    r"et \textbf{dans} ce cas $U_\mu$",
    "Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29/97/99; cf. 'est' p. 42, 'rentiel' p. 43). Independent of the next finding (same line, no overlap).",
    corrected=r"et dans ce cas $U_\mu$")

add(240, "Lemme (20.3.8.2), end: 'dense dans X_μ pour μ⩾1.'",
    "the print has 'μ⩾1' (old-style 1, the same sort as the 1 of '(8.8.1)' two lines above: side-by-side crop side_one.png, crop c240_mu1.png)",
    "$\\mu\\geq\\lambda$ (silent correction)",
    "misprint_in_print", None, "high",
    r"dans $X_\mu$ pour $\mu\geq\lambda$.",
    r"dans $X_\mu$ pour $\mu\geq 1$.",
    "Correct reading μ⩾λ: the indices run over the directed set of the system (8.8.1), and the lemma says that once U_λ is schematically dense in X_λ, so is U_μ for every μ⩾λ. No erratum in Liste 3.",
    corrected=r"dans $X_\mu$ pour $\mu\geq\lambda$.")

add(240, "Lemme (20.3.8.3), l. 1: 'soit M_λ (resp. M) l'ensemble'",
    "'(resp. M)' roman, parentheses upright (crop c240_lem3.png)", "italic (lemma environment)",
    "convention", 6, "high",
    r"soit $M_\lambda$ (resp. $M$) l'ensemble",
    r"soit $M_\lambda$ \textup{(resp. $M$)} l'ensemble", "")

add(240, "Lemme (20.3.8.3), l. 2: 'des points maximaux de S_λ (resp. S).'",
    "'(resp. S)' roman, parentheses upright (crop c240_lem3.png)", "italic (lemma environment)",
    "convention", 6, "high",
    r"de $S_\lambda$ (resp. $S$).",
    r"de $S_\lambda$ \textup{(resp. $S$)}.", "")

add(240, "proof of (20.3.8.3): 'si s' est une générisation de s'",
    "'générisation' (crop c240_s3_generis.png)", "'généralisation'",
    "word", None, "high",
    r"si $s'$ est une généralisation de $s$",
    r"si $s'$ est une générisation de $s$",
    "The TeX rewords EGA's term (générisation, as in ega4-18).")

add(240, "proof of (20.3.8.3): 'est une générisation de l'image s_λ de s'",
    "'générisation' (crop c240_s3_generis.png)", "'généralisation'",
    "word", None, "high",
    r"est une généralisation de l'image",
    r"est une générisation de l'image", "")

add(240, "proof of (20.3.8.3): 'qui sont des générisations de s_λ'",
    "'générisations' (crop c240_s3_generis2.png)", "'généralisations'",
    "word", None, "high",
    r"qui sont des généralisations de $s_\lambda$",
    r"qui sont des générisations de $s_\lambda$", "")

add(240, "Lemme (20.3.8.4), l. 1-2: 'soit V_α un ensemble ouvert de S_α, et soient V_λ et V ses images réciproques ... Si U_α est dense dans S_α, U_λ est dense ...'",
    "the hypothesis names the open set V_α (images V_λ, V), the conclusions and the proof use U_α, U_λ, U (page_240_s4.png)",
    "V_α, V_λ, V as printed (the TeX keeps the printed reading)",
    "misprint_in_print", None, "medium",
    None, None,
    "The authors' slip: the open set of the hypothesis is the U of the conclusions, of the proof ('l'hypothèse que U_α est dense dans S_α entraîne que M_α⊂U_α ...') and of the use in (20.3.8.5). Correct reading: U for V in the hypothesis. No erratum in Liste 3.",
    corrected=r"soit $U_\alpha$ un ensemble ouvert de $S_\alpha$, et soient $U_\lambda$ et $U$ ses images réciproques")

# ---------------- p. 241 ----------------
add(241, "heading '(20.3.8.5) Fin de la démonstration de (20.3.8.2). —'",
    "bold number in parentheses, italic title, upright reference, then '. —' before 'Supposons' (crop c241_h5.png)",
    "\\emph{20.3.8.5. Fin de la démonstration de (20.3.8.2).}: number italic, without parentheses, followed by a period; no dash",
    "other", None, "high",
    r"\emph{20.3.8.5. Fin de la démonstration de \sref{IV.20.3.8.2}.}",
    r"\textbf{(20.3.8.5)} \emph{Fin de la démonstration de \sref{IV.20.3.8.2}.} ---",
    "Hand-made heading: restores the parentheses, the dash and the bold number (the form the env environment prints, \\textbf{(#1)}; GLOBAL_ISSUES 61 covers the number font). \\sref stays upright inside \\emph (\\normalfont).")

add(241, "heading '(20.3.8.6) Fin de la démonstration de (20.3.8). —'",
    "bold number in parentheses, italic title, upright reference, then '. —' (crop c241_h6.png)",
    "\\emph{20.3.8.6. Fin de la démonstration de (20.3.8).}: number italic, without parentheses, followed by a period; no dash",
    "other", None, "high",
    r"\emph{20.3.8.6. Fin de la démonstration de \sref{IV.20.3.8}.}",
    r"\textbf{(20.3.8.6)} \emph{Fin de la démonstration de \sref{IV.20.3.8}.} ---",
    "Same form as (20.3.8.5).")

# ---------------- p. 242 ----------------
add(242, "l. 2: 'la conclusion résulte alors de (11.10.1, c))'",
    "italic label 'c)' with no opening parenthesis (crop c242_c.png)",
    "\\sref{IV.11.10.1}[(c)] prints '(11.10.1, (c))' with an upright (c)",
    "other", None, "high",
    r"résulte alors de \sref{IV.11.10.1}[(c)]",
    r"résulte alors de \sref{IV.11.10.1}[\emph{c)}]",
    "As on pp. 232-233 (\\sref sets its third argument in \\normalfont, so \\emph gives the italic label).")

add(242, "Remarques (20.3.8.7) (i), end: 'qui montre que pour μ⩾λ assez grand, Z est schématiquement dense dans X, d'où la conclusion.'",
    "'Z' and 'X' without subscripts (crop c242_Z.png)",
    "Z_μ, X_μ (silent correction)",
    "misprint_in_print", None, "high",
    r"$Z_\mu$ est schématiquement dense dans $X_\mu$, d'où",
    r"$Z$ est schématiquement dense dans $X$, d'où",
    "Correct reading Z_μ, X_μ: (20.3.8.2) applied to the open sets underlying Z_μ and Z gives Z_μ schematically dense in X_μ for μ large ('pour μ⩾λ assez grand' refers to μ). No erratum in Liste 3.",
    corrected=r"$Z_\mu$ est schématiquement dense dans $X_\mu$, d'où")

add(242, "Corollaire (20.3.9), l. 1: 'l'une ou l'autre hypothèse a), b) de (20.3.6)'",
    "labels a), b) upright in the italic statement (crops c242_cor.png, c242_ab.png)", "italic (corollary environment)",
    "convention", 6, "high",
    r"hypothèse~a),~b) de \sref{IV.20.3.6} sur $X$",
    r"hypothèse~\textup{a)},~\textup{b)} de \sref{IV.20.3.6} sur $X$",
    "GLOBAL_ISSUES 88.")

add(242, "Corollaire (20.3.9), end: '(autrement dit, soit un S-morphisme de Spec(O_X,x) dans Y)'",
    "the parenthesis roman with upright parentheses, only 'morphisme' italic (crop c242_cor.png)", "all italic (corollary environment)",
    "convention", 6, "high",
    r"(autrement dit, soit un $S$-morphisme de $\Spec(\sh{O}_{X,x})$ dans $Y$)",
    r"\textup{(autrement dit, soit un $S$-\emph{morphisme} de $\Spec(\sh{O}_{X,x})$ dans $Y$)}",
    "\\emph inside \\textup gives the italic 'morphisme'.")

add(242, "Corollaire (20.3.9), l. 3: 'pseudo-S-morphisme ω de X dans Y soit défini au point x'",
    "'dans' heavier than 'de' before it, 'soit défini' after it and the 'dans' of 'X'' dans X'' in (20.3.10): ink area d 278 / a 209 / n 207 / s 128 px against 242 / 178 / 177 / 103, stroke 4.45 / 4.10 / 3.94 / 3.82 against 3.69 / 3.46 / 3.31 / 3.07 px; the same weight as the bold 'dans' of p. 240 (crops c242_dans.png, c242_line3.png, side_dans.png)",
    "normal italic (silent correction)",
    "misprint_in_print", None, "medium",
    r"$\omega$ de $X$ dans $Y$ soit défini",
    r"$\omega$ de $X$ \textbf{dans} $Y$ soit défini",
    "Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29/99), medium: the Y right after it is also somewhat heavier (344 px against 289-310 px for the other Y's of the strip, shape unchanged; side_Y.png), so local heavy impression of 'dans Y' cannot be excluded. Y not recorded.",
    corrected=r"$\omega$ de $X$ dans $Y$ soit défini")

add(242, "Lemme (20.3.10), l. 4: 'alors, si g∘(f|U) se prolonge'",
    "'(f|U)', no prime (crop c242_fU1.png)", "(f|U') (silent correction)",
    "misprint_in_print", None, "high",
    r"si $g\circ(f|U')$ se prolonge",
    r"si $g\circ(f|U)$ se prolonge",
    "Correct reading f|U' (the restriction U'→U of f, so that g∘(f|U') is defined on U' = f^{-1}(U)); the print has f|U both here and in the proof. No erratum in Liste 3.",
    corrected=r"si $g\circ(f|U')$ se prolonge")

add(242, "proof of (20.3.10): 'qui prolonge g∘(f|U), et posons'",
    "'(f|U)', no prime (crop c242_fU2.png)", "(f|U') (silent correction)",
    "misprint_in_print", None, "high",
    r"qui prolonge $g\circ(f|U')$, et posons",
    r"qui prolonge $g\circ(f|U)$, et posons",
    "Same slip as in the statement.",
    corrected=r"qui prolonge $g\circ(f|U')$, et posons")

add(242, "proof of (20.3.10): 'on a g''_1 = g''_2 (11.10.1, d))'",
    "italic label 'd)' with no opening parenthesis (crop c242_d.png)",
    "\\sref{IV.11.10.1}[(d)] prints '(11.10.1, (d))'",
    "other", None, "high",
    r"on a $g''_1=g''_2$ \sref{IV.11.10.1}[(d)]",
    r"on a $g''_1=g''_2$ \sref{IV.11.10.1}[\emph{d)}]",
    "As on pp. 232-233.")

add(242, "Proposition (20.3.11), l. 2: 'Supposons que f soit plat, et que l'une des conditions suivantes'",
    "'plat' and 'l'une' roman (emphasised) in the italic statement (crops c242_prop.png, c242_plat.png)", "italic",
    "convention", 6, "high",
    r"Supposons que $f$ soit plat, et que l'une des conditions suivantes",
    r"Supposons que $f$ soit \emph{plat}, et que \emph{l'une} des conditions suivantes",
    "Roman (emphasised) words in the italic statement; \\emph gives upright there.")

# ---------------- p. 243 ----------------
add(243, "Proposition (20.3.11) (iii): 'X vérifie l'une des conditions a), b) de (20.3.6)'",
    "labels a), b) upright in the italic statement (crop c243_iii.png)", "italic",
    "convention", 6, "high",
    r"vérifie l'une des conditions~a),~b) de \sref{IV.20.3.6}.",
    r"vérifie l'une des conditions~\textup{a)},~\textup{b)} de \sref{IV.20.3.6}.",
    "GLOBAL_ISSUES 88.")

add(243, "Proposition (20.3.11): 'Alors, f^{-1}(dom_S(ω)) est schématiquement dense' after the list",
    "new paragraph, indented like the item labels (page_243_s1.png)",
    "follows \\end{enumerate} without a blank line: no indent",
    "other", None, "high",
    "\\end{enumerate}" + NL + r"Alors, $f^{-1}",
    "\\end{enumerate}" + NL + NL + r"Alors, $f^{-1}",
    "GLOBAL_ISSUES 80 pattern.")

add(243, "proof of (20.3.11), l. 3: 'en vertu de (11.10.5, (ii), a))'",
    "italic label 'a)' with no opening parenthesis (crop c243_a.png)",
    "\\sref{IV.11.10.5}[(ii), (a)] prints '(11.10.5, (ii), (a))'",
    "other", None, "high",
    r"en vertu de \sref{IV.11.10.5}[(ii), (a)] que",
    r"en vertu de \sref{IV.11.10.5}[(ii), \emph{a)}] que",
    "As on pp. 232-233.")

add(243, "proof of (20.3.11): 'un ensemble ouvert U rétrocompact et schématiquement dense dans X'",
    "'rétrocompact' italic (crop c243_a.png)", "roman",
    "italics", None, "high",
    r"ouvert $U$ rétrocompact et schématiquement",
    r"ouvert $U$ \emph{rétrocompact} et schématiquement", "")

i_disp = add(243, "proof of (20.3.11): 'autrement dit que, pour tout point / x' ∈ dom_S(ω∘f), / on a x = f(x') ∈ dom_S(ω).'",
    "'x'∈dom_S(ω∘f),' is DISPLAYED on its own centred line; the text resumes flush left with 'on a' (crop c243_disp.png)",
    "set in the line",
    "formula", None, "high",
    r"pour tout point $x'\in\operatorname{dom}_S(\omega\circ f)$, on a $x=f(x')",
    "pour tout point" + NL + r"\[" + NL + r"  x'\in\operatorname{dom}_S(\omega\circ f)," + NL + r"\]" + NL + r"on a $x=f(x')",
    "Display as printed (the comma belongs to the display). Apply BEFORE the next finding (misprint x'), whose 'old' is taken from the result of this edit.")

add(243, "the display 'x'∈dom_S(ω∘f),' (first sort of the display line)",
    "the x is BOLD italic (wrong fount): side by side with the x's of 'on a x=f(x')' on the next line (side_x243.png, c243_disp_z.png), ink area 197 px against 155 / 159 px, stroke 4.0 against 3.1 / 3.4 px; its prime is heavier too (47 against 39 px), while 'dom', ω and f of the display are of normal weight",
    "normal x (silent correction)",
    "misprint_in_print", None, "medium",
    "x'\\in\\operatorname{dom}_S(\\omega\\circ f)," + NL + r"\]",
    "\\boldsymbol{x}'\\in\\operatorname{dom}_S(\\omega\\circ f)," + NL + r"\]",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99; cf. the x of p. 71, medium like p. 199). 'old' is the text AFTER the previous finding (display), which must be applied first; it does not occur in the unedited page.",
    corrected="x'\\in\\operatorname{dom}_S(\\omega\\circ f)," + NL + r"\]",
    after=i_disp)

add(243, "proof of (20.3.11): 'on peut donc supposer déjà X et X' affines, donc f quasi-compact.'",
    "'quasi-compact' italic (crop c243_ii.png)", "roman",
    "italics", None, "high",
    r"donc $f$ quasi-compact.",
    r"donc $f$ \emph{quasi-compact}.", "")

add(243, "proof of (20.3.11): 'Dans le premier cas de (i) et dans le cas (ii) f est un morphisme ouvert'",
    "no comma after '(ii)' (crop c243_ii.png)", "comma after (ii)",
    "punctuation", None, "high",
    r"dans le cas~(ii), $f$ est un morphisme ouvert",
    r"dans le cas~(ii) $f$ est un morphisme ouvert", "")

add(243, "proof of (20.3.11): 'cela sera le cas, en vertu de (11.10.5, (ii), a)) si U est pris'",
    "italic label 'a)' with no opening parenthesis (page_243_s3.png)",
    "\\sref{IV.11.10.5}[(ii), (a)] prints '(11.10.5, (ii), (a))'",
    "other", None, "high",
    r"cela sera le cas, en vertu de \sref{IV.11.10.5}[(ii), (a)] si",
    r"cela sera le cas, en vertu de \sref{IV.11.10.5}[(ii), \emph{a)}] si", "")

add(243, "proof of (20.3.11): 'si U est pris rétrocompact dans X'",
    "'rétrocompact' italic (page_243_s3.png)", "roman",
    "italics", None, "high",
    r"est pris rétrocompact dans",
    r"est pris \emph{rétrocompact} dans", "")

add(243, "proof of (20.3.11), end: 'et d'appliquer (11.10.5, (ii), b))'",
    "italic label 'b)' with no opening parenthesis (page_243_s4.png)",
    "\\sref{IV.11.10.5}[(ii), (b)] prints '(11.10.5, (ii), (b))'",
    "other", None, "high",
    r"d'appliquer \sref{IV.11.10.5}[(ii), (b)]",
    r"d'appliquer \sref{IV.11.10.5}[(ii), \emph{b)}]", "")

add(243, "proof of (20.3.11), last line: 'présentation finie et d'appliquer', the first letter (start of the line)",
    "the p of 'présentation' is a BOLD roman p (wrong fount): side by side with the p's of 'appliquer' on the same line (side_p243.png, c243_pres.png), ink area 417 px against 304 / 277, stroke 5.7 against 4.2 / 3.7 px; the rest of the word is of normal weight",
    "normal p (silent correction)",
    "misprint_in_print", None, "high",
    r"localement de présentation finie et d'appliquer",
    r"localement de \textbf{p}résentation finie et d'appliquer",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99); at the start of the line, so not the line-end heaviness of item 100. Independent of the previous finding (no overlap).",
    corrected=r"localement de présentation finie et d'appliquer")

add(243, "end of p. 243 / top of p. 244: heading 'Remarque (20.3.13). —'",
    "p. 243 ends with Corollaire (20.3.12); p. 244 begins with 'Remarque (20.3.13). — Lorsque X vérifie' (page_243_s4.png, page_244_s1.png)",
    "\\oldpage[IV-4]{244} stands after \\begin{remark}[20.3.13] and its \\label, so the heading falls on p. 243",
    "marker", None, "high",
    r"\begin{remark}[20.3.13]" + NL + r"\label{IV.20.3.13}",
    r"\oldpage[IV-4]{244}" + NL + r"\begin{remark}[20.3.13]" + NL + r"\label{IV.20.3.13}",
    "Marker move, part 1 of 2: apply together with the first p. 244 finding, which removes the old marker; either order works, each 'old' stays unique after the other.")

# ---------------- p. 244 ----------------
add(244, "top of p. 244: old marker position",
    "p. 244 begins with the heading 'Remarque (20.3.13). —'",
    "\\oldpage[IV-4]{244} after \\begin{remark}[20.3.13]\\label",
    "marker", None, "high",
    r"\oldpage[IV-4]{244}" + NL + "Lorsque",
    "Lorsque",
    "Marker move, part 2 of 2: apply together with the last p. 243 finding, which inserts the marker before \\begin{remark}[20.3.13].")

add(244, "Remarque (20.3.13), l. 1: 'l'une des conditions a), b) de (20.3.6)'",
    "labels a), b) italic, parentheses included, in the roman remark (crop c244_ab.png)",
    "plain a), b) (italic now only because the remark environment is italic)",
    "italics", None, "high",
    r"conditions~a),~b) de \sref{IV.20.3.6}, alors on a vu",
    r"conditions~\emph{a)},~\emph{b)} de \sref{IV.20.3.6}, alors on a vu",
    "GLOBAL_ISSUES 88; judged with the remark body roman (document-wide remark decision): \\emph then gives the italic labels.")

add(244, "title of 20.4: 'Propriétés des domaines de définition des fonctions rationnelles.'",
    "final full stop (crop c244_title.png)", "no full stop",
    "punctuation", None, "high",
    r"\subsection{Propriétés des domaines de définition des fonctions rationnelles}",
    r"\subsection{Propriétés des domaines de définition des fonctions rationnelles.}",
    "As the page-fixed titles of ega4-18 (GLOBAL_ISSUES 43/58).")

add(244, "(20.4.1): 'l'injection j est un morphisme quasi-compact et quasi-séparé ((1.2.2) et (1.7.4))'",
    "EGA IV's own (1.2.2) and (1.7.4): light old-style 1 followed by a full stop, no bold I, no comma; the print itself has the doubled parentheses (crop c244_refs_z.png)",
    "\\sref[I]{I.2.2} and \\sref[I]{I.7.4} print '((I, 2.2) et (I, 7.4))' (bold I)",
    "number", None, "high",
    r"(\sref[I]{I.2.2} et \sref[I]{I.7.4})",
    r"(\sref{IV.1.2.2} et \sref{IV.1.7.4})",
    "The (I, x.y) misreading of EGA IV's (1.x.y) (GLOBAL_ISSUES 78/103); EGA IV (1.2.2) (i) and (1.7.4) are the cited facts (quasi-separated immersions; (I, 9.2.2) under 'quasi-compact et quasi-séparé'). Keep the outer parentheses: here the doubling is the print's (cf. p. 235).")

add(244, "(20.4.1): 'ayant pour espace sous-jacent ... à Γ_u (I, 5.2.1 et 5.2.2).'",
    "one parenthesis, one bold I: '(I, 5.2.1 et 5.2.2)' (page_244_s3.png)",
    "two \\sref inside parentheses print '((I, 5.2.1) et (I, 5.2.2))'",
    "extra", None, "high",
    r"(\sref[I]{I.5.2.1} et \sref[I]{I.5.2.2})",
    r"(\textbf{I}, \EGAUnavailableHyperref{I.5.2.1}{5.2.1} et \EGAUnavailableHyperref{I.5.2.2}{5.2.2})",
    "Same construction as the p. 230 fix ((0_I, 6.5.1 et 6.6.2)); \\EGAUnavailableHyperref links as \\sref does, defined label or not.")

add(244, "(20.4.1): 'Notons enfin que si Y est séparé sur S'",
    "new indented paragraph (page_244_s3.png)", "runs on in the same paragraph",
    "other", None, "high",
    NL + r"Notons enfin que si $Y$",
    NL + NL + r"Notons enfin que si $Y$",
    "Does not overlap the previous finding (its 'old' ends before the full stop).")

add(244, "(20.4.1): 'si v : X → Y est un S-morphisme, le graphe Γ_ω'",
    "'morphisme' italic, 'S-' roman (page_244_s3.png)", "roman",
    "italics", None, "high",
    r"$v:X\to Y$ est un $S$-morphisme, le graphe",
    r"$v:X\to Y$ est un $S$-\emph{morphisme}, le graphe", "")

add(244, "(20.4.2), last line: 'dom_S(ω) est le plus grand ouvert U de X'",
    "'le plus grand ouvert' italic, 'le' included (crop c244_le.png)", "\\emph{plus grand ouvert}: 'le' roman",
    "italics", None, "high",
    r"est le \emph{plus grand ouvert}",
    r"est \emph{le plus grand ouvert}", "")


# ---------------- checks ----------------
def load_page(p):
    return (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

src = SRC.read_text(encoding="utf-8")
assert "\r" not in src
pages = {p: load_page(p) for p in range(240, 245)}
ok = True
# 1) each 'old' exactly once in its page (unless taken from a previous fix's result)
for k, d in enumerate(F):
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    if d["_after"] is None:
        n = pages[d["page"]].count(old)
        if n != 1:
            ok = False
            print("PAGE COUNT", n, "for finding", k, d["page"], repr(old[:80]))
    else:
        prev = F[d["_after"]]["fix"]
        t = pages[d["page"]].replace(prev["old"], prev["new"], 1)
        n0 = pages[d["page"]].count(old)
        n = t.count(old)
        if n != 1 or n0 != 0:
            ok = False
            print("AFTER COUNT", n0, n, "for finding", k)
# 2) sequential application on the current source and on the pages: each old exactly once when applied
s = src
pg = dict(pages)
for k, d in enumerate(F):
    if d["fix"] is None:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    n = s.count(old)
    if n != 1:
        ok = False
        print("SOURCE COUNT", n, "for finding", k, d["page"], repr(old[:80]))
    s = s.replace(old, new, 1)
    m = pg[d["page"]].count(old)
    if m != 1:
        ok = False
        print("SEQ PAGE COUNT", m, "for finding", k)
    pg[d["page"]] = pg[d["page"]].replace(old, new, 1)
# 3) misprint fixes: 'corrected' present
for k, d in enumerate(F):
    if d["kind"] == "misprint_in_print" and not d.get("corrected"):
        ok = False
        print("MISSING corrected", k)
print("checks", "OK" if ok else "FAILED", len(F), "findings")
# counts
for p in range(240, 245):
    norm = sum(1 for d in F if d["page"] == p and d["kind"] not in ("convention", "misprint_in_print"))
    conv = sum(1 for d in F if d["page"] == p and d["kind"] == "convention")
    mis = sum(1 for d in F if d["page"] == p and d["kind"] == "misprint_in_print")
    print(p, "%d/%d/%d" % (norm, conv, mis))
if ok and "--write" in sys.argv:
    out = []
    for d in F:
        e = {k: v for k, v in d.items() if k != "_after"}
        out.append(e)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
