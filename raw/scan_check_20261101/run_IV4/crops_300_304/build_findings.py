import io, json, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4/"
SRC = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
OUT = RUN + "findings_300_304.json"


def T(s):
    return s.replace('¶', '\n')


def read(p):
    with open(p, encoding='utf-8', newline='') as f:
        return f.read().replace('\r\n', '\n')


F = []


def add(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high",
        corrected=None, src="b"):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence,
         "fix": None if old is None else {"old": T(old), "new": T(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = T(corrected)
    d["note"] = note
    d["_src"] = src
    F.append(d)


OUTSIDE = ("OUTSIDE the page segments: ega4-21c-fr.tex, text before the file's first marker "
           "(\\oldpage[IV-4]{303}); printed on p. 302 and appended to page_302.tex.")

# ---------------------------------------------------------------- p. 300
add(300, "l. 2: 'déduit de ⊕_i u'_i par passage aux quotients'",
    "index i under the ⊕ (crop p300_oplus_sum.png)",
    "\\bigoplus u'_i without the index", "missing",
    r"$\bigoplus u'_i$", r"$\bigoplus_i u'_i$")
add(300, "l. 3: 'χ(M, u)+χ(M'', u'') = Σ_{i=1}^{n} χ(M'_i, u'_i), et'",
    "Σ with i=1 below and n above (crop p300_oplus_sum.png)",
    "\\sum_i (bounds =1 and n missing)", "missing",
    r"=\sum_i\chi(M'_i,u'_i)$", r"=\sum_{i=1}^n\chi(M'_i,u'_i)$")
add(300, "display (21.10.17.9): 'χ(M, u) = long A_𝔭.χ(M_0, u_0).'",
    "baseline period (measured: its bottom on the baseline, at the height of the final full stop; crop p300_longdot.png)",
    "\\cdot (centred dot)", "symbol",
    r"\operatorname{long}A_{\mathfrak{p}}\cdot\chi(M_0,u_0)", r"\operatorname{long}A_{\mathfrak{p}}.\chi(M_0,u_0)",
    "Baseline period in the print (GLOBAL_ISSUES 65), written '.' as on pp. 271-277.")
add(300, "after (21.10.17.9): 'Soit 𝔫_j (0⩽j⩽r) la « puissance symbolique j-ème »'",
    "'Soit' flush left (left edge 417 px like the full lines; the paragraph indent of 'Pour prouver la première assertion' is 529 px): the paragraph goes on after the display",
    "blank line after \\]: a new indented paragraph", "other",
    r"\tag{21.10.17.9}¶\]¶¶Soit", r"\tag{21.10.17.9}¶\]¶Soit",
    "Paragraph break the print does not have (as p. 44; reverse of the GLOBAL_ISSUES 47 pattern).")
add(300, "l. 1 after (21.10.17.9): 'la « puissance symbolique j-ème » de 𝔭'",
    "'j-ème' italic (crop p300_jeme.png)",
    "'-ème' upright", "italics",
    r"symbolique $j$-ème »", r"symbolique \emph{$j$-ème} »")
add(300, "display after 'posons': 'M_j = 𝔫_jM/𝔫_{j+1}M (0⩽j⩽r—1),'",
    "long dash (41 px, as the dash of X—{a} on p. 302; crop p300_rminus.png)",
    "minus sign", "convention",
    r"\leq r-1),", r"\leq r\setmin 1),",
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.",
    convention=7)
add(300, "'Pour prouver la première assertion', l. 3: 'Désignons par l_j le rang du A_0-module'",
    "'rang' italic (page_300_s3.png)",
    "upright", "italics",
    r"le rang du $A_0$-module", r"le \emph{rang} du $A_0$-module",
    "The 'rang' of l. 1 ('si m est le rang du A-module libre M') is roman in the print, as in the TeX.")

# ---------------------------------------------------------------- p. 301
add(301, "l. 10: 'à l'homothétie injective t : ξ → (det u)ξ de A'",
    "plain arrow (crop p301_xi_arrow.png)",
    "\\mapsto", "convention",
    r"$t:\xi\mapsto(\det u)\xi$", r"$t:\xi\to(\det u)\xi$",
    convention=3)
add(301, "display 'χ(A, t) = Σ_i long(A_{𝔭_i}).χ(A/𝔭_i, t_i).'",
    "baseline period (measured: bottom on the baseline of the line)",
    "\\cdot (centred dot)", "symbol",
    r"\operatorname{long}(A_{\mathfrak{p}_i})\cdot\chi(A/\mathfrak{p}_i,t_i)",
    r"\operatorname{long}(A_{\mathfrak{p}_i}).\chi(A/\mathfrak{p}_i,t_i)",
    "GLOBAL_ISSUES 65.")
add(301, "'IV) Cas général. Posons A' = Â'",
    "'Cas général' italic (crop p301_III_cas.png)",
    "upright", "italics",
    r"IV) Cas général.", r"IV) \emph{Cas général}.",
    "The step label IV) and the full stop are roman. The 'III)' mid-line and the 'II)' at the line end have the stroke weight of this 'IV)' (measured), not bold.")
add(301, "Proposition (21.10.18), l. 3: 'l'une des conditions (ii), (iii), (iv) de (21.10.10)'",
    "the three labels upright inside the italic statement (crop p301_conditions.png)",
    "italic (inside the italic proposition)", "convention",
    r"l'une des conditions (ii), (iii), (iv) de", r"l'une des conditions \textup{(ii), (iii), (iv)} de",
    "'de' after them is italic in the print.", convention=6)
add(301, "display (21.10.18.1): 'f_*(f^*(Z)) = n.Z'",
    "baseline period (measured: bottom on the baseline of n and Z)",
    "\\cdot (centred dot)", "symbol",
    r"f_*(f^*(Z))=n\cdot Z", r"f_*(f^*(Z))=n.Z",
    "GLOBAL_ISSUES 65.")
add(301, "Proposition (21.10.18), after (21.10.18.1): '(« formule de projection »).'",
    "roman (crop p301_projection.png)",
    "italic (inside the proposition environment)", "convention",
    r"(« formule de projection »).", r"\textup{(« formule de projection »)}.",
    "The heavier-looking 'de' of this line is ink spread (stem 5-6 px against 4-5 px nearby, same shapes), not a wrong fount: not recorded.",
    convention=6)
add(301, "proof of (21.10.18), l. 4: 'au cas où A est complet.'",
    "'complet' italic (crop p301_complet_fY.png)",
    "upright", "italics",
    r"au cas où $A$ est complet.", r"au cas où $A$ est \emph{complet}.")
add(301, "proof of (21.10.18), l. 6: 'et posons Y' = X'×_X Y = Spec(B⊗_A A') et g = f_{(Y)} : Y' → Y; le morphisme g'",
    "both formulas in the running text, joined by 'et'; the subscript of f is (Y) in parentheses (crops p301_posons.png, p301_fY.png)",
    "one display, the formulas joined by \\qquad ('et' lost); subscript \\{Y\\} in braces", "formula",
    r"et posons¶\[¶  Y'=X'\times_XY=\Spec(B\otimes_AA'),\qquad g=f_{\{Y\}}:Y'\to Y;¶\]¶le morphisme",
    r"et posons $Y'=X'\times_XY=\Spec(B\otimes_AA')$ et $g=f_{(Y)}:Y'\to Y$;¶le morphisme",
    "One edit for the inline setting (GLOBAL_ISSUES 21/51) and the subscript f_{(Y)} (base-change notation).")

# ---------------------------------------------------------------- p. 302
add(302, "l. 1: 'de la condition 𝔪_{x'}∉Ass(O_{X',x'}) (3.3.1). Le morphisme'",
    "'(3.3.1)' without 0 (crop p302_331.png)",
    "(\\mathbf{0},3.3.1) prints '(0, 3.3.1)'", "number",
    r"\operatorname{Ass}(\sh{O}_{X',x'})$ $(\mathbf{0},3.3.1)$",
    r"\operatorname{Ass}(\sh{O}_{X',x'})$ \sref{IV.3.3.1}",
    "EGA IV's own (3.3.1) (associated primes under flat base change: 'par platitude'). Written with \\sref like the other IV references of ega4-21b; the label is not in this part, so \\sref prints '(3.3.1)' through \\EGAUnavailableHyperref.")
add(302, "l. 9: 'est un A-module libre (0_III, 10.1.3)'",
    "'libre' roman (crop p302_libre_zoom.png)",
    "\\emph{libre}", "italics",
    r"\emph{libre} $(\mathbf{0}_{\mathrm{III}},10.1.3)$, de rang", r"libre $(\mathbf{0}_{\mathrm{III}},10.1.3)$, de rang",
    "The TeX adds an emphasis the print does not have.")
add(302, "l. 10: 'on a par définition (21.10.1 et 21.10.3)'",
    "one pair of parentheses around both numbers (crop p302_libre.png)",
    "\\sref{IV.21.10.1} et \\sref{IV.21.10.3} prints '(21.10.1) et (21.10.3)'", "punctuation",
    r"par définition \sref{IV.21.10.1} et \sref{IV.21.10.3}",
    r"par définition (\hyperref[IV.21.10.1]{21.10.1} et \hyperref[IV.21.10.3]{21.10.3})",
    "Form of the p. 226 fix '(\\hyperref[IV.21.6]{21.6} et \\hyperref[IV.21.7]{21.7})'; both labels exist in ega4-21b (\\label{IV.21.10.1}; \\EGAReaderTarget{...}{IV.21.10.3}). Independent of the next entry (adjacent, no overlap).")
add(302, "l. 10: 'f^*(Z) = λ_{x'}.{x'}-bar, où λ_{x'} est la longueur'",
    "the formula in the running text; baseline period (measured) (crop p302_s2_top.png)",
    "displayed, with \\cdot", "formula",
    r"\[¶  f^*(Z)=\lambda_{x'}\cdot\overline{\{x'\}},¶\]¶où $\lambda_{x'}$",
    r"$f^*(Z)=\lambda_{x'}.\overline{\{x'\}}$, où $\lambda_{x'}$",
    "Inline as printed (GLOBAL_ISSUES 21); the same edit writes the baseline period (GLOBAL_ISSUES 65).")
add(302, "l. 11: 'puis f_*(f^*(Z)) = (λ_{x'}[k(x') : k(x)]).{x}-bar; mais'",
    "the formula in the running text; baseline period (measured) (crop p302_s2_top.png)",
    "displayed, with \\cdot", "formula",
    r"puis¶\[¶  f_*(f^*(Z))=(\lambda_{x'}[\boldsymbol{k}(x'): \boldsymbol{k}(x)])\cdot\overline{\{x\}};¶\]¶mais",
    r"puis $f_*(f^*(Z))=(\lambda_{x'}[\boldsymbol{k}(x'): \boldsymbol{k}(x)]).\overline{\{x\}}$;¶mais",
    "Inline as printed; the same edit writes the baseline period.")
add(302, "Dans le cas (iii), l. 2: 'un anneau de Cohen-Macaulay (0, 16.4.6)'",
    "hyphen (crop p302_CM1.png)",
    "Cohen--Macaulay (en dash)", "punctuation",
    r"$A'$ est un anneau de Cohen--Macaulay $(\mathbf{0},16.4.6)$", r"$A'$ est un anneau de Cohen-Macaulay $(\mathbf{0},16.4.6)$",
    "GLOBAL_ISSUES 74.")
add(302, "Dans le cas (iii), l. 3: 'comme dim(A') = dim(A) = 1 que A'/𝔪_xA' est un anneau artinien'",
    "no 'et' before 'que' (crop p302_s2_mid.png)",
    "'et que' (silent correction)", "misprint_in_print",
    r"$\dim(A')=\dim(A)=1$ et que", r"$\dim(A')=\dim(A)=1$ que",
    "The print drops the 'et' joining the two conditions of 'comme ... et que ...'; the TeX silently supplies it. Restore the printed reading; the corrected edition keeps 'et que'.",
    corrected=r"$\dim(A')=\dim(A)=1$ et que")
add(302, "Dans le cas (iii), l. 4: 'que A' est un A-module plat'",
    "'plat' italic (crop p302_s2_mid.png)",
    "upright", "italics",
    r"un $A$-module plat et on est ramené", r"un $A$-module \emph{plat} et on est ramené")
add(302, "Dans le cas (iv), l. 3: 'f^*(Z) = (n/[k(x') : k(x)]).{x'}-bar, d'où'",
    "in the running text, with a slash and parentheses; baseline period (measured) (crop p302_caseiv.png)",
    "displayed \\frac with \\cdot", "formula",
    r"on a¶\[¶  f^*(Z)=\frac{n}{[\boldsymbol{k}(x'): \boldsymbol{k}(x)]}\cdot\overline{\{x'\}},¶\]¶",
    r"on a¶$f^*(Z)=(n/[\boldsymbol{k}(x'): \boldsymbol{k}(x)]).\overline{\{x'\}}$,¶",
    "One edit: inline as printed, the print's (n/[...]) for the \\frac, and the baseline period. Independent of the next two entries (no overlap).")
add(302, "Dans le cas (iv), l. 3: 'd'où f_*(f^*(Z)) = n.{x}-bar.'",
    "baseline period (measured: bottom on the baseline of n)",
    "\\cdot (centred dot)", "symbol",
    r"=n\cdot\overline{\{x\}}$", r"=n.\overline{\{x\}}$",
    "GLOBAL_ISSUES 65.")
add(302, "end of the proof of (21.10.18): '... = n.{x}-bar. C.Q.F.D.'",
    "'C.Q.F.D.' after the last formula (crop p302_caseiv.png)",
    "missing", "missing",
    r".¶\end{proof}¶¶On notera", r". C.Q.F.D.¶\end{proof}¶¶On notera",
    "Written as in ega4-21c ('... $. C.Q.F.D.'). Independent of the entry above (adjacent, no overlap).")
add(302, "display (21.10.19.1): 'f_*(cyc(f^*(D))) = n.cyc(D).'",
    "baseline period (measured: bottom on the baseline of n and c)",
    "\\cdot (centred dot)", "symbol",
    r"=n\cdot\operatorname{cyc}(D)", r"=n.\operatorname{cyc}(D)",
    "GLOBAL_ISSUES 65.")
add(302, "proof of (21.10.19): 'Cela résulte de (21.10.18) et (21.10.13).'",
    "'(21.10.13)' (page_302_s3.png)",
    "\\sref{IV.21.10.13bis} prints '(21.10.13bis)'", "number",
    r"\sref{IV.21.10.13bis}", r"(\hyperref[IV.21.10.13bis]{21.10.13})",
    "The print numbers both the lemma and the proposition of 21.10 '(21.10.13)' (TeX labels IV.21.10.13 and IV.21.10.13bis); the printed reference reads (21.10.13). The link keeps the TeX's target, the proposition.")
add(302, "heading of 21.11: '21.11. Factorialité des anneaux locaux réguliers.'",
    "the title ends with a full stop (page_302_s3.png)",
    "no full stop", "punctuation",
    r"\subsection{Factorialité des anneaux locaux réguliers}",
    r"\subsection{Factorialité des anneaux locaux réguliers.}",
    OUTSIDE + " Same form as the 21.8 and 21.9 titles (pp. 280, 284).", src="c")
add(302, "proof of (21.11.1), l. 5: 'et posons U = X—{a}.'",
    "long dash for set difference (crop p302_Xa_n1.png)",
    "minus sign", "convention",
    r"$U=X-\{a\}$. En tout point", r"$U=X\setmin\{a\}$. En tout point",
    OUTSIDE, convention=7, src="c")
add(302, "proof of (21.11.1), l. 6: 'dim(O_{X,y}) ⩽ n—1'",
    "long dash (41 px; crop p302_Xa_n1.png)",
    "minus sign", "convention",
    r"\leq n-1$, et puisque", r"\leq n\setmin 1$, et puisque",
    OUTSIDE + " Subtraction printed with the long dash (GLOBAL_ISSUES 23).", convention=7, src="c")
add(302, "proof of (21.11.1), last line of the page: 'donc de Cohen-Macaulay (0, 17.1.3).'",
    "hyphen (crop p302_CM2.png)",
    "Cohen--Macaulay (en dash)", "punctuation",
    r"Cohen--Macaulay $(\mathbf 0, 17.1.3)$", r"Cohen-Macaulay $(\mathbf 0, 17.1.3)$",
    OUTSIDE + " GLOBAL_ISSUES 74.", src="c")

# ---------------------------------------------------------------- p. 303
add(303, "display after 'une résolution gauche finie de ℱ :': '0 ← ℱ ← O_X^{n_1} ← O_X^{n_2} ← . . . ← O_X^{n_h} ← 0'",
    "baseline dots (crop p303_resF.png)",
    "\\cdots", "symbol",
    r"\mathcal O_X^{n_2}\leftarrow\cdots", r"\mathcal O_X^{n_2}\leftarrow\ldots",
    "\\cdots where the print has baseline dots. This display, (21.11.1.1), the formulas of (21.11.1.2) and the diagram of p. 304 are set in a heavier type (lining 0, bold indices); their weight is not reported.",
    src="c")
add(303, "display (21.11.1.1): '0 ← ℒ ← O_U^{n_1} → O_U^{n_2} ← . . . ← O_U^{n_h} ← 0.'",
    "the arrow between O_U^{n_1} and O_U^{n_2} points to the right (crop p303_211111.png)",
    "\\leftarrow (silent correction)", "misprint_in_print",
    r"\mathcal O_U^{n_1}¶  \leftarrow", r"\mathcal O_U^{n_1}¶  \rightarrow",
    "Every other arrow of the resolution, and all those of the resolution of ℱ just above, point left; the print reverses this one. The TeX silently corrects it; restore the printed reading. Independent of the next entry (adjacent, no overlap).",
    corrected=r"\mathcal O_U^{n_1}¶  \leftarrow", src="c")
add(303, "display (21.11.1.1): '... O_U^{n_2} ← . . . ← O_U^{n_h} ← 0.'",
    "baseline dots (crop p303_211111.png)",
    "\\cdots", "symbol",
    r"\mathcal O_U^{n_2}\leftarrow\cdots", r"\mathcal O_U^{n_2}\leftarrow\ldots", src="c")
add(303, "'Le théorème résultera alors ...', l. 4: 'en désignant par p le rang de ℰ dans ce voisinage'",
    "'rang' italic (crop p303_rang.png)",
    "upright", "italics",
    r"par $p$ le rang de $\mathscr E$", r"par $p$ le \emph{rang} de $\mathscr E$", src="c")
add(303, "Lemme (21.11.1.2), display: '0 ← ℰ_0 ←(u_0) ℰ_1 ← . . . ← ℰ_h ← 0'",
    "baseline dots (page_303_s2.png)",
    "\\cdots", "symbol",
    r"\xleftarrow{u_0}\mathscr E_1¶  \leftarrow\cdots", r"\xleftarrow{u_0}\mathscr E_1¶  \leftarrow\ldots",
    src="c")
add(303, "Lemme (21.11.1.2), l. 3: 'alors le O_X-Module inversible ⊗_{0⩽i⩽h}(Λ^max ℰ_i)^{⊗(−1)^i} est isomorphe à O_X.'",
    "the tensor product in the running text, at the start of the line (crop p303_tensorinline.png)",
    "displayed", "formula",
    r"inversible¶\[¶  \bigotimes_{0\leq i\leq h}¶  (\Lambda^{\max}\mathscr E_i)^{\otimes(-1)^i}¶\]¶est isomorphe",
    r"inversible¶$\bigotimes_{0\leq i\leq h}(\Lambda^{\max}\mathscr E_i)^{\otimes(-1)^i}$¶est isomorphe",
    "Inline as printed (GLOBAL_ISSUES 21). The minus signs of (−1)^i here and in O_U^{⊗(−1)} are ordinary minus signs of the heavier type, not the long dash.",
    src="c")
add(303, "proof of (21.11.1.2), second exact sequence: '0 ← 𝒩 ← ℰ_2 ← . . . ← ℰ_h ← 0'",
    "baseline dots (crop p303_twoseq.png)",
    "\\cdots", "symbol",
    r"\mathscr E_2¶  \leftarrow\cdots", r"\mathscr E_2¶  \leftarrow\ldots",
    "Independent of the next entry (no overlap).", src="c")
add(303, "proof of (21.11.1.2), end of the second exact sequence",
    "no full stop after '← 0' (crop p303_twoseq.png)",
    "'0.'", "punctuation",
    r"\mathscr E_h\leftarrow0.¶\]", r"\mathscr E_h\leftarrow0¶\]", src="c")
add(303, "proof of (21.11.1.2): 'un isomorphisme canonique (Λ^max𝒩)⊗(Λ^maxℰ_0) ⥲ Λ^maxℰ_1 pour achever la démonstration'",
    "in the running text, at the end of the line (page_303_s3.png)",
    "displayed", "formula",
    r"canonique¶\[¶  (\Lambda^{\max}\mathscr N)\otimes(\Lambda^{\max}\mathscr E_0)¶  \xrightarrow{\sim}\Lambda^{\max}\mathscr E_1¶\]¶pour achever",
    r"canonique¶$(\Lambda^{\max}\mathscr N)\otimes(\Lambda^{\max}\mathscr E_0)\xrightarrow{\sim}\Lambda^{\max}\mathscr E_1$¶pour achever",
    "Inline as printed (GLOBAL_ISSUES 21).", src="c")
add(303, "display 'r_α : (Λ^max𝒩|U_α)⊗(Λ^maxℳ_α) ⥲ (Λ^maxℰ_1)|U_α'",
    "no comma at the end (crop p303_ru.png)",
    "comma", "punctuation",
    r"(\Lambda^{\max}\mathscr E_1)|U_\alpha,¶\]", r"(\Lambda^{\max}\mathscr E_1)|U_\alpha¶\]",
    "The heavy script ℳ is the shape of this fount's script M (the same on p. 282 and throughout pp. 303-304), not a wrong fount.",
    src="c")
add(303, "last display of the page: 'u_α : (Λ^max𝒩|U_α)⊗(Λ^maxℰ_0|U_α) ⥲ Λ^maxℰ_1|U_α'",
    "no full stop: the sentence goes on at the top of p. 304, 'et il s'agit de montrer' (crops p303_ru.png, p304_et.png)",
    "full stop after the display", "punctuation",
    r"\Lambda^{\max}\mathscr E_1|U_\alpha.¶\]", r"\Lambda^{\max}\mathscr E_1|U_\alpha¶\]",
    "Apply together with the first p. 304 entry ('Et' -> 'et'): the TeX ends the sentence here, the print continues it.",
    src="c")

# ---------------------------------------------------------------- p. 304
add(304, "l. 1: 'et il s'agit de montrer que u_α et u_β coïncident'",
    "lowercase 'et', continuing the sentence of p. 303 (crop p304_et.png)",
    "'Et' (capital, after a full stop the print lacks)", "word",
    r"Et il s'agit de montrer", r"et il s'agit de montrer",
    "Apply together with the last p. 303 entry (the full stop after the u_α display).", src="c")
add(304, "l. 3: 'où w_{βα} : ℳ_α|(U_α∩U_β) ⥲ ℳ_β|(U_α∩U_β) est la « projection parallèle'",
    "in the running text (crop p304_wba.png)",
    "displayed", "formula",
    r"où¶\[¶  w_{\beta\alpha}:\mathscr M_\alpha|(U_\alpha\cap U_\beta)¶  \xrightarrow{\sim}\mathscr M_\beta|(U_\alpha\cap U_\beta)¶\]¶est la",
    r"où¶$w_{\beta\alpha}:\mathscr M_\alpha|(U_\alpha\cap U_\beta)\xrightarrow{\sim}\mathscr M_\beta|(U_\alpha\cap U_\beta)$¶est la",
    "Inline as printed (GLOBAL_ISSUES 21). Independent of the next entry (no overlap).", src="c")
add(304, "l. 4: 'est la « projection parallèle à N » telle que'",
    "a roman capital N, while the Module is the script 𝒩 in 't ∈ Γ(U_α∩U_β, 𝒩)' on the same line (crops p304_aN.png, p304_N_script.png)",
    "\\mathscr N (silent correction)", "misprint_in_print",
    r"parallèle à $\mathscr N$ »", r"parallèle à $N$ »",
    "Wrong letter in the print: the projection is parallel to the Module 𝒩 = Ker(u_0). The TeX silently corrects it; restore the printed reading.",
    corrected=r"parallèle à $\mathscr N$ »", src="c")
add(304, "heading of 21.12: '... pour l'ensemble de ramification d'un morphisme birationnel.'",
    "the title ends with a full stop (page_304_s1.png)",
    "no full stop", "punctuation",
    r"ramification d'un morphisme birationnel}", r"ramification d'un morphisme birationnel.}",
    "As the 21.8, 21.9 and 21.11 titles.", src="c")
add(304, "(21.12.1), after (21.12.1.1): 'Pour tout X-préschéma V affine sur X, l'application'",
    "a new indented paragraph (left edge 532 px, as 'Pour que i_U' above it; full lines start at 418 px), after the short last line 'f : U → X soit affine.' (crop p304_affine_sur.png)",
    "the same paragraph as 'Pour que i_U ... soit affine.'", "other",
    r"soit \emph{affine}. Pour tout", r"soit \emph{affine}.¶¶Pour tout",
    "Independent of the next two entries (no overlap).", src="c")
add(304, "(21.12.1): 'Pour tout X-préschéma V affine sur X'",
    "only 'affine' italic; 'sur X' roman (crop p304_affine_sur.png)",
    "\\emph{affine sur $X$}", "italics",
    r"\emph{affine sur¶$X$}", r"\emph{affine} sur¶$X$", src="c")
add(304, "(21.12.1): 'l'application u ⇝ u∘i_U est une bijection'",
    "wavy arrow (crop p304_affine_sur.png)",
    "\\mapsto", "symbol",
    r"$u\mapsto u\circ i_U$", r"$u\leadsto u\circ i_U$",
    "GLOBAL_ISSUES 33/107/109 (wavy arrows).", src="c")
add(304, "(21.12.1): 'le foncteur covariant V ⇝ Hom_X(U, V)'",
    "wavy arrow (crop p304_wavy_V.png)",
    "\\mapsto", "symbol",
    r"$V\mapsto\operatorname{Hom}_X(U,V)$", r"$V\leadsto\operatorname{Hom}_X(U,V)$", src="c")
add(304, "(21.12.1): 'que pour X fixé, U ⇝ Aff(U/X) est un foncteur covariant'",
    "wavy arrow (crop p304_wavy_U.png)",
    "\\mapsto", "symbol",
    r"$U\mapsto\operatorname{Aff}(U/X)$", r"$U\leadsto\operatorname{Aff}(U/X)$", src="c")
add(304, "diagram at the end of the page (U_1 → U_2 over U_1^0 → U_2^0)",
    "no full stop after U_2^0 (crop p304_diagram.png)",
    "'U_2^0.'", "punctuation",
    r"U_1^0 \ar[r]_{g^0} & U_2^0.", r"U_1^0 \ar[r]_{g^0} & U_2^0",
    "Labels i_{U_1} (left), i_{U_2} (right), g (above), g^0 (below) stand as in the TeX.", src="c")

# ---------------------------------------------------------------- checks
pages = {p: read(RUN + "page_%d.tex" % p) for p in range(300, 305)}
srcs = {"b": read(SRC + "ega4-21b-fr.tex"), "c": read(SRC + "ega4-21c-fr.tex")}
ok = True
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    n_page = pages[d["page"]].count(fx["old"])
    n_src = srcs[d["_src"]].count(fx["old"])
    other = srcs["c" if d["_src"] == "b" else "b"].count(fx["old"])
    if n_page != 1 or n_src != 1:
        ok = False
        print("PROBLEM", d["page"], repr(fx["old"][:70]), "page", n_page, "src", n_src)
    if other:
        print("note: also in the other file", d["page"], repr(fx["old"][:60]), other)
    if fx["old"] == fx["new"]:
        ok = False
        print("PROBLEM old == new", d["page"])
print("all olds unique:", ok, "entries:", len(F))
for d in F:
    del d["_src"]
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "misprint_in_print":
        c[2] += 1
    elif d["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print(counts)
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(F, f, ensure_ascii=False, indent=1)
    print("written", OUT)
