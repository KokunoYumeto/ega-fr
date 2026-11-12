"""Build findings_200_204.json and check every 'old' string.

Newlines inside LaTeX strings are written as the pilcrow character and converted to \n.
'after' names the index (within the same page) of a finding that must be applied first.
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
SRC = (r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/"
       r"diplomatic/packages/IV4/native/ega4/ega4-18-fr.tex")
OUT = RUN + "/findings_200_204.json"


def L(s):
    return s.replace("\u00b6", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, after=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": L(old), "new": L(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_after"] = after
    F.append(d)
    return len(F) - 1


GR = "gr with a raised bullet (gr\u2022)"
G60 = "GLOBAL_ISSUES 60/83: the print's gr\u2022 is gr^\\bullet, not ^*."

# ---------------------------------------------------------------- p. 200
add(200, "top of p. 200: page break 199/200 inside '(II, 2.3.6), un | voisinage ouvert affine'",
    "p. 200 begins mid-sentence: 'voisinage ouvert affine' starts at the left margin like the lines below (x 416 px); "
    "p. 199 ends '(II, 2.3.6), un' at the right margin",
    "blank lines before and after \\oldpage[IV-4]{200}",
    "marker", None, "high",
    r"\oldpage[IV-4]{200}¶¶voisinage ouvert", r"\oldpage[IV-4]{200}¶voisinage ouvert",
    "BOUNDARY FIX (page break with p. 199). The marker is at the right place. This removes the blank line after it; "
    "the blank line BEFORE it, at the end of the p. 199 segment, must go too: 'un\\n\\n\\oldpage[IV-4]{200}' -> "
    "'un\\n\\oldpage[IV-4]{200}' (\\oldpage ends with \\ignorespaces, which does not skip a \\par). Apply both.")

add(200, "proof of (19.4.6) (ii), l. 4: 'que gr\u2022_{\U0001D50D_0}(B_0) soit un A_0-module plat'",
    GR, "\\operatorname{gr}_{\\mathfrak J_0}^*", "symbol", None, "high",
    r"\operatorname{gr}_{\mathfrak J_0}^*(B_0)$ soit un", r"\operatorname{gr}_{\mathfrak J_0}^\bullet(B_0)$ soit un",
    G60)

add(200, "proof of (19.4.6) (ii), l. 5: 'gr\u2022_\U0001D50D(B)=gr\u2022_{\U0001D50D_0}(B_0)\u2297_{A_0}A'",
    GR + ", twice", "^* twice", "symbol", None, "high",
    r"\operatorname{gr}_{\mathfrak J}^*(B)=\operatorname{gr}_{\mathfrak J_0}^*(B_0)",
    r"\operatorname{gr}_{\mathfrak J}^\bullet(B)=\operatorname{gr}_{\mathfrak J_0}^\bullet(B_0)",
    "Two occurrences in one edit. " + G60)

add(200, "proof of (19.4.6) (ii), l. 9: 'le morphisme Proj(\u2295_{n\u22650}\U0001D50D^n) \u2192 Spec(B_0)'",
    "Proj(\u2295\U0001D50D^n) with no subscript 0 on the Fraktur J (crop c200_proj.png)",
    "\\mathfrak J_0^n (silent correction)",
    "misprint_in_print", None, "high",
    r"\mathfrak J_0^n)\to\Spec(B_0)", r"\mathfrak J^n)\to\Spec(B_0)",
    "The morphism over Spec(B_0) whose base change is X'\u2192X is Proj of the Rees algebra of \U0001D50D_0, so the "
    "correct reading is \U0001D50D_0^n; the print drops the subscript (clean blank where it would stand, not a broken "
    "sort). The TeX silently corrected; the fix restores the printed reading and changes only the subscript.",
    corrected=r"\operatorname{Proj}(\bigoplus_{n\geq0}\mathfrak J_0^n)\to\Spec(B_0)")

add(200, "proof of (19.4.6) (ii): 'est de type fini (II, 2.7.1)'",
    "bold II", "plain II", "convention", 2, "high",
    r"de type fini (II, 2.7.1)", r"de type fini (\textbf{II}, 2.7.1)",
    "A real EGA II reference (bold II in the print).")

add(200, "proof of (19.4.6) (ii), last lines: 'le fait que gr\u2022_\U0001D4A5(\U0001D4AA_X) est une'",
    GR, "^*", "symbol", None, "high",
    r"le fait que $\operatorname{gr}_{\mathscr J}^*(\sh{O}_X)$", r"le fait que $\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X)$",
    G60)

add(200, "Corollaire (19.4.7): 'normalement plat le long de Y (11.3.4).'",
    "reference upright inside the italic statement", "italic (environment)", "convention", 6, "high",
    r"normalement plat le long de $Y$ (11.3.4).", r"normalement plat le long de $Y$ \textup{(11.3.4)}.",
    "")

add(200, "Corollaire (19.4.7): 'Alors (avec les notations de (19.4.1)), le morphisme'",
    "'(avec les notations de (19.4.1))' roman inside the italic statement (crop c200_alors.png)",
    "italic (environment)", "convention", 6, "high",
    r"Alors (avec les notations de (19.4.1)), le morphisme",
    r"Alors \textup{(avec les notations de (19.4.1))}, le morphisme",
    "")

add(200, "Corollaire (19.4.7): 'des points de X (resp. X') o\u00f9 X (resp. X') est S-plat est un voisinage de Y (resp. Y').'",
    "'(resp. X')' twice and '(resp. Y')' roman (crops c200_resp.png, c200_respY.png)", "italic (environment)",
    "convention", 6, "high",
    r"(resp. $X'$) où $X$ (resp. $X'$) est $S$-plat est un voisinage de $Y$ (resp. $Y'$).",
    r"\textup{(resp. $X'$)} où $X$ \textup{(resp. $X'$)} est $S$-plat est un voisinage de $Y$ \textup{(resp. $Y'$)}.",
    "Three occurrences in one edit (the shorter strings also occur in (19.4.6) on p. 199).")

add(200, "proof of (19.4.7), l. 1: 'par hypoth\u00e8se gr\u2022_\U0001D4A5(\U0001D4AA_X) est un'",
    GR, "^*", "symbol", None, "high",
    r"par hypothèse $\operatorname{gr}_{\mathscr J}^*(\sh{O}_X)$", r"par hypothèse $\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X)$",
    G60)

add(200, "proof of (19.4.7): 'Y-isomorphe \u00e0 Proj(gr\u2022_\U0001D4A5(\U0001D4AA_X))'",
    GR, "^*", "symbol", None, "high",
    r"isomorphe à $\operatorname{Proj}(\operatorname{gr}_{\mathscr J}^*(\sh{O}_X))$ (19.4.2)",
    r"isomorphe à $\operatorname{Proj}(\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X))$ (19.4.2)",
    G60)

add(200, "proof of (19.4.7), last words: 'montre que Y' est Y-plat.'",
    "'plat' italic (crop c200_plat.png)", "roman", "italics", None, "high",
    r"montre que $Y'$ est $Y$-plat.", r"montre que $Y'$ est $Y$-\emph{plat}.",
    "GLOBAL_ISSUES 83 (italics lost in 18.10 and later).")

add(200, "Proposition (19.4.8), l. 1: 'les hypoth\u00e8ses de (19.4.7)'",
    "reference upright (crop c200_1948.png)", "italic (environment)", "convention", 6, "high",
    r"les hypothèses de (19.4.7) et en outre", r"les hypothèses de \textup{(19.4.7)} et en outre",
    "")

add(200, "last line of p. 200: '(17.5.1) et (17.7.1), | il suffit de consid\u00e9rer' (page break 200/201)",
    "p. 201 begins mid-sentence: 'il suffit de consid\u00e9rer' at the left margin (x 340 px like the lines below)",
    "blank lines before and after \\oldpage[IV-4]{201}",
    "marker", None, "high",
    r"(17.5.1) et (17.7.1),¶¶", r"(17.5.1) et (17.7.1),¶",
    "The marker is at the right place. Part 1 of 2: the first p. 201 finding removes the blank line after "
    "\\oldpage[IV-4]{201}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------------------------------------------------------- p. 201
add(201, "top of p. 201: '\\oldpage[IV-4]{201}' + blank line before 'il suffit'",
    "mid-sentence page break (see the last p. 200 finding)", "blank line after the marker",
    "marker", None, "high",
    r"\oldpage[IV-4]{201}¶¶il suffit", r"\oldpage[IV-4]{201}¶il suffit",
    "Part 2 of 2 with the last p. 200 finding; both blank lines must go.")

add(201, "paragraph 'Lorsque X\u2192S...': 'et que gr\u2022_\U0001D4A5(\U0001D4AA_X) est isomorphe'",
    GR, "^*", "symbol", None, "high",
    r"et que $\operatorname{gr}_{\mathscr J}^*(\sh{O}_X)$ est isomorphe",
    r"et que $\operatorname{gr}_{\mathscr J}^\bullet(\sh{O}_X)$ est isomorphe",
    G60)

add(201, "same sentence: 'isomorphe \u00e0 S\u2022_{\U0001D4AA_Y}(\U0001D4A9_{Y/X})'",
    "bold S with a raised bullet (crop c201_S.png)", "\\mathbf S_{\\sh{O}_Y}^*", "symbol", None, "high",
    r"\mathbf S_{\sh{O}_Y}^*(\sh{N}_{Y/X})$, donc est", r"\mathbf S_{\sh{O}_Y}^\bullet(\sh{N}_{Y/X})$, donc est",
    "Same form as the earlier IV-4 page fixes (\\mathbf{S}_{...}^{\\bullet}).")

add(201, "Corollaire (19.4.9), l. 1: 'Sous les hypoth\u00e8ses g\u00e9n\u00e9rales de (19.4.8),'",
    "reference upright inside the italic statement", "italic (environment)", "convention", 6, "high",
    r"Sous les hypothèses générales de (19.4.8),", r"Sous les hypothèses générales de \textup{(19.4.8)},",
    "")

add(201, "Corollaire (19.4.9), last line: 'aux points de U\u2014Y.'",
    "long dash", "minus sign", "convention", 7, "high",
    r"lisse sur $S$ aux points de $U-Y$.", r"lisse sur $S$ aux points de $U\setmin Y$.",
    "\\setmin as in the earlier IV-4 fixes.")

add(201, "Proposition (19.4.11), l. 2: 'l'Id\u00e9al quasi-coh\u00e9rent de \U0001D4AA_X image de u'",
    "the subscript X of this \U0001D4AA_X is visibly bolder than the subscript X of '\U0001D4AA_X-Modules' earlier on the "
    "same line (side-by-side crops c201_OX1.png, c201_OX2.png); mid-line, not at the line end",
    "\\sh{O}_X (silent correction)",
    "misprint_in_print", None, "medium",
    r"de $\sh{O}_X$ image de $u$", r"de $\sh{O}_{\mathbf X}$ image de $u$",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99). The fix restores the printed reading.",
    corrected=r"de $\sh{O}_X$ image de $u$")

add(201, "Proposition (19.4.11): 'le fibr\u00e9 projectif sur X d\u00e9fini par \u2130 (II, 4.1.1)'",
    "bold II, reference upright", "plain II, italic (environment)", "convention", 2, "high",
    r"défini par $\mathscr E$ (II, 4.1.1),", r"défini par $\mathscr E$ \textup{(\textbf{II}, 4.1.1)},",
    "One edit for convention 2 (bold II) and convention 6 (upright reference inside the italic statement). "
    "The P of P(\u2130) is bold UPRIGHT here (crop c201_PP.png): \\mathbf P is right, no convention-10 change.")

add(201, "Proposition (19.4.11): '\u03b1_1^\u266f : p^*(\u2130) \u2192 \U0001D4AA_P(1)'",
    "sharp sign \u266f (crop c201_PP.png)", "^{\\#}", "convention", 9, "high",
    r"$\alpha_1^{\#}:p^*(\mathscr E)", r"$\alpha_1^{\sharp}:p^*(\mathscr E)",
    "")

add(201, "Proposition (19.4.11): 'l'homomorphisme canonique (II, 4.1.5.1) et \u210b son noyau'",
    "bold II, reference upright", "plain II, italic (environment)", "convention", 2, "high",
    r"l'homomorphisme canonique (II, 4.1.5.1) et", r"l'homomorphisme canonique \textup{(\textbf{II}, 4.1.5.1)} et",
    "One edit for convention 2 (bold II) and convention 6 (upright reference inside the italic statement).")

add(201, "Proposition (19.4.11), display: arrow label \u03b1_1^\u266f",
    "sharp sign \u266f (crop c201_disp.png)", "^{\\#}", "convention", 9, "high",
    r"\xrightarrow{\alpha_1^{\#}}\sh{O}_P(1)", r"\xrightarrow{\alpha_1^{\sharp}}\sh{O}_P(1)",
    "")

# ---------------------------------------------------------------- p. 202
add(202, "Proposition (19.4.11) (i): item label",
    "'(i)' upright", "\\item[(i)] italic inside the statement", "convention", 6, "high",
    r"\item[(i)] L'image de $X'$", r"\item[\textup{(i)}] L'image de $X'$",
    "Roman-numeral labels in italic statements are upright (GLOBAL_ISSUES 16).")

add(202, "Proposition (19.4.11) (ii): item label",
    "'(ii)' upright", "\\item[(ii)] italic", "convention", 6, "high",
    r"\item[(ii)] Si $\mathscr E$ est un", r"\item[\textup{(ii)}] Si $\mathscr E$ est un",
    "GLOBAL_ISSUES 16.")

add(202, "Proposition (19.4.11) (iii): item label",
    "'(iii)' upright", "\\item[(iii)] italic", "convention", 6, "high",
    r"\item[(iii)] On suppose que $X$", r"\item[\textup{(iii)}] On suppose que $X$",
    "GLOBAL_ISSUES 16.")

add(202, "(19.4.11) (i), l. 2: '\u2295_{n\u22650}\U0001D4A5^n (II, 3.6.2) est un sous-pr\u00e9sch\u00e9ma'",
    "bold II, reference upright (crop c202_i.png)", "plain II, italic (environment)", "convention", 2, "high",
    r"\mathscr J^n$ (II, 3.6.2) est un sous-préschéma", r"\mathscr J^n$ \textup{(\textbf{II}, 3.6.2)} est un sous-préschéma",
    "One edit for convention 2 (bold II) and convention 6 (upright reference inside the italic statement). "
    "The P of P(\u2130) in (i) is bold upright (crop c202_i.png): no convention-10 change.")

add(202, "(19.4.11) (ii): 'localement libre de rang m\u20141.'",
    "long dash", "minus sign", "convention", 7, "high",
    r"localement libre de rang $m-1$.", r"localement libre de rang $m\setmin 1$.",
    "Long dash for subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")

add(202, "(19.4.11) (iii), l. 3: 'de codimension \u00e9gale \u00e0 rg_{\U0001D4AA_x}(\u2130_x)'",
    "rg_{\U0001D4AA_x}: the subscript of \U0001D4AA is a single italic x (crop c202_rg1.png)",
    "\\operatorname{rg}_{\\sh{O}_{X,x}}", "formula", None, "high",
    r"\operatorname{rg}_{\sh{O}_{X,x}}(\mathscr E_x)", r"\operatorname{rg}_{\sh{O}_x}(\mathscr E_x)",
    "The TeX rewrote the print's notation (GLOBAL_ISSUES 102); \U0001D4AA_x is EGA's usual name for the local ring at x, not a misprint.")

add(202, "(19.4.11) (iii): '(ce que nous exprimerons en disant que l'homomorphisme u est r\u00e9gulier au point x (cf. chap. V))'",
    "the parenthesis is roman with 'r\u00e9gulier' italic (crop c202_iii.png)",
    "all italic (environment), 'r\u00e9gulier' upright through \\emph", "convention", 6, "high",
    r"(ce que nous exprimerons en disant que l'homomorphisme $u$ est \emph{régulier} au point $x$ (cf. chap. V))",
    r"\textup{(ce que nous exprimerons en disant que l'homomorphisme $u$ est \emph{régulier} au point $x$ (cf. chap. V))}",
    "Inside \\textup the existing \\emph{r\u00e9gulier} comes out italic, as printed.")

add(202, "(19.4.11) (iii): 'en tous les points de X'\u2014Y''",
    "long dash", "minus sign", "convention", 7, "high",
    r"; en tous les points de $X'-Y'$", r"; en tous les points de $X'\setmin Y'$",
    "")

add(202, "(19.4.11) (iii): '(Y' image r\u00e9ciproque de Y dans X')'",
    "both parentheses upright, next to the upright letters Y', X' (crops c202_par1.png, c202_par2.png; compare the "
    "italic parentheses of '(donc S-plat)', p. 200, crop c200_donc.png)",
    "italic parentheses (environment)", "convention", 6, "medium",
    r"($Y'$ image réciproque de $Y$ dans $X'$)", r"\textup{(}$Y'$ image réciproque de $Y$ dans $X'$\textup{)}",
    "GLOBAL_ISSUES 26/101: parentheses are upright next to formulas; the words inside stay italic.")

add(202, "(19.4.11) (iii), l. 7: 'de codimension rg_{\U0001D4AA_P}(\u210b_z) o\u00f9 z=j(x')'",
    "rg_{\U0001D4AA_P}: the subscript of \U0001D4AA is P alone (crop c202_rg2.png)",
    "\\operatorname{rg}_{\\sh{O}_{P,z}}", "formula", None, "high",
    r"\operatorname{rg}_{\sh{O}_{P,z}}(\mathscr H_z)", r"\operatorname{rg}_{\sh{O}_P}(\mathscr H_z)",
    "The TeX rewrote the print's subscript (GLOBAL_ISSUES 102). Possibly the authors meant \U0001D4AA_z (as \U0001D4AA_x in "
    "rg_{\U0001D4AA_x}(\u2130_x) above), but rg_{\U0001D4AA_P}(\u210b_z) is intelligible; not recorded as a misprint.")

add(202, "(19.4.11) (iii), end: '(autrement dit l'homomorphisme v : \u210b\u2192\U0001D4AA_P est r\u00e9gulier en z).'",
    "roman parenthesis with 'r\u00e9gulier' italic (crop c202_iii2.png)", "all italic (environment)",
    "convention", 6, "high",
    r"(autrement dit l'homomorphisme $v:\mathscr H\to\sh{O}_P$ est régulier en $z$)",
    r"\textup{(autrement dit l'homomorphisme $v:\mathscr H\to\sh{O}_P$ est \emph{régulier} en $z$)}",
    "One edit: the roman parenthesis (convention 6) and the italic 'r\u00e9gulier' inside it.")

add(202, "proof of (19.4.11), l. 3: 't\u2208E=S^1_A(E) (II, 2.3.14)'",
    "bold II", "plain II", "convention", 2, "high",
    r"(II, 2.3.14)", r"(\textbf{II}, 2.3.14)", "")

add(202, "proof, l. 4: '\u0393(D_+(t), \U0001D4AA_P)=S_{(t)} (II, 2.4.1)'",
    "bold II", "plain II", "convention", 2, "high",
    r"(II, 2.4.1)", r"(\textbf{II}, 2.4.1)", "")

add(202, "proof, l. 5: 'la d\u00e9finition de \u03b1_1^\u266f'",
    "sharp sign \u266f", "^{\\#}", "convention", 9, "high",
    r"la définition de $\alpha_1^{\#}$", r"la définition de $\alpha_1^{\sharp}$", "")

add(202, "proof, l. 6: '(II, 2.6.2.2), on voit'",
    "bold II", "plain II", "convention", 2, "high",
    r"(II, 2.6.2.2)", r"(\textbf{II}, 2.6.2.2)", "")

add(202, "proof, l. 6: 'on voit qu'\u00e0 tout \u00e9l\u00e9ment a=\u03a3_i x^{(i)}\u2297((x_1^{(i)}x_2^{(i)}...x_n^{(i)})/t^n) de E\u2297_A S_{(t)}'",
    "set in the line, with a slash, double parentheses and baseline dots (crop c202_a2.png)",
    "displayed, with \\frac and \\cdots", "formula", None, "high",
    r"on voit qu'à tout élément¶\[¶  a=\sum_i x^{(i)}\otimes\frac{x_1^{(i)}x_2^{(i)}\cdots x_n^{(i)}}{t^n}¶\]¶de $E\otimes_A S_{(t)}$",
    r"on voit qu'à tout élément $a=\sum_i x^{(i)}\otimes((x_1^{(i)}x_2^{(i)}\ldots x_n^{(i)})/t^n)$ de $E\otimes_A S_{(t)}$",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); the TeX also rewrote the slash as \\frac and "
    "the baseline dots as \\cdots.")

add(202, "proof, l. 7: '\u03b1_1^\u266f fait correspondre'",
    "sharp sign \u266f", "^{\\#}", "convention", 9, "high",
    r"$\alpha_1^{\#}$ fait correspondre", r"$\alpha_1^{\sharp}$ fait correspondre", "")

add(202, "proof, l. 7-8: 'l'\u00e9l\u00e9ment \u03a3_i(x^{(i)}x_1^{(i)}...x_n^{(i)})/t^n de (S(1))_{(t)}'",
    "set in the line, with parentheses, a slash and baseline dots (crop c202_a3.png)",
    "displayed, with \\frac and \\cdots", "formula", None, "high",
    r"l'élément¶\[¶  \sum_i\frac{x^{(i)}x_1^{(i)}\cdots x_n^{(i)}}{t^n}¶\]¶de $(S(1))_{(t)}$.",
    r"l'élément $\sum_i(x^{(i)}x_1^{(i)}\ldots x_n^{(i)})/t^n$ de $(S(1))_{(t)}$.",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21).")

add(202, "proof, l. 9: 'alors il en est de m\u00eame l'image de a''",
    "'il en est de m\u00eame l'image de' without 'de' before 'l'image' (crop c202_s3a.png)",
    "'il en est de m\u00eame de l'image de' (silent correction)",
    "misprint_in_print", None, "high",
    r"de même de l'image", r"de même l'image",
    "The construction needs 'de' ('il en est de m\u00eame de l'image'); the print drops it. The fix changes only the word; "
    "independent of the next finding (adjacent text, no overlap).",
    corrected=r"de même de l'image")

i_ap = add(202, "proof, l. 9: 'a'=v(a)=\u03a3_i u(x^{(i)})(x_1^{(i)}..x_n^{(i)})/t^n par l'homomorphisme canonique'",
    "set in the line, with a slash (crops c202_s3a.png, c202_dots.png)",
    "displayed, with \\frac", "formula", None, "high",
    r" de¶\[¶  a'=v(a)=\sum_i u(x^{(i)})\frac{x_1^{(i)}\cdots x_n^{(i)}}{t^n}¶\]¶par l'homomorphisme canonique",
    r" de $a'=v(a)=\sum_i u(x^{(i)})(x_1^{(i)}\ldots x_n^{(i)})/t^n$ par l'homomorphisme canonique",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21). This edit writes the regular three dots; the "
    "print's two dots are restored by the next finding (a misprint), which must be applied after this one.")

add(202, "same formula: 'x_1^{(i)}..x_n^{(i)}' with two dots",
    "two baseline dots between x_1^{(i)} and x_n^{(i)}, evenly spaced, no room for a third (crop c202_dots2.png)",
    "\\cdots (three dots, silent correction)",
    "misprint_in_print", None, "medium",
    r"(x_1^{(i)}\ldots x_n^{(i)})/t^n$ par", r"(x_1^{(i)}\mathinner{\ldotp\ldotp}x_n^{(i)})/t^n$ par",
    "'old' is the text AFTER the previous finding (apply that first). \\mathinner{\\ldotp\\ldotp} is the two-dot form of "
    "\\ldots (same spacing). Every other product on the page has three dots.",
    corrected=r"(x_1^{(i)}\ldots x_n^{(i)})/t^n", after=i_ap)

add(202, "proof, l. 10: 'l'homomorphisme canonique S_{(t)} \u2192 (u(E))^n_{(t)} (II, 3.6.2)'",
    "(u(E))^n_{(t)}: superscript n and subscript (t) on (u(E)); no \u2295 (crop c202_s3a.png)",
    "(\\bigoplus_{n\\geq0}(u(E))^n)_{(u(t))}", "formula", None, "high",
    r"$S_{(t)}\to(\bigoplus_{n\geq0}(u(E))^n)_{(u(t))}$", r"$S_{(t)}\to(u(E))^n_{(t)}$",
    "The TeX replaced the print's abbreviated notation by an explicit form (GLOBAL_ISSUES 46/102). The print's "
    "(u(E))^n_{(t)} stands for the degree-0 part of the Rees algebra \u2295(u(E))^n localised at u(t); kept as printed "
    "(an abbreviation, not recorded as a misprint).")

add(202, "proof, l. 10: '(II, 3.6.2). Or, cette image'",
    "bold II", "plain II", "convention", 2, "high",
    r"(II, 3.6.2). Or, cette image", r"(\textbf{II}, 3.6.2). Or, cette image", "")

add(202, "proof, l. 11: 'n'est autre que \u03a3_i u(x^{(i)})u(x_1^{(i)})...u(x_n^{(i)})/(u(t))^n dans l'anneau A_{u(t)}'",
    "set in the line, with a slash and baseline dots (crop c202_s3b.png)",
    "displayed, with \\frac and \\cdots", "formula", None, "high",
    r"n'est autre que¶\[¶  \sum_i\frac{u(x^{(i)})u(x_1^{(i)})\cdots u(x_n^{(i)})}{(u(t))^n}¶\]¶dans l'anneau",
    r"n'est autre que $\sum_i u(x^{(i)})u(x_1^{(i)})\ldots u(x_n^{(i)})/(u(t))^n$ dans l'anneau",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21).")

add(202, "proof, l. 13: 'l'image canonique de \u03a3_i(x^{(i)}x_1^{(i)}...x_n^{(i)})/t^{n+1}'",
    "parentheses around the product; baseline dots (crop c202_s3b.png)",
    "no parentheses; \\cdots", "formula", None, "high",
    r"$\sum_i x^{(i)}x_1^{(i)}\cdots x_n^{(i)}/t^{n+1}$", r"$\sum_i(x^{(i)}x_1^{(i)}\ldots x_n^{(i)})/t^{n+1}$",
    "")

add(202, "proof of (ii): 'puisque \u03b1_1^\u266f : E\u2297_A S_{(t)} \u2192 (S(1))_{(t)}'",
    "sharp sign \u266f", "^{\\#}", "convention", 9, "high",
    r"puisque $\alpha_1^{\#}:E\otimes_A", r"puisque $\alpha_1^{\sharp}:E\otimes_A", "")

add(202, "proof of (ii), display: arrow label \u03b1_1^\u266f",
    "sharp sign \u266f", "^{\\#}", "convention", 9, "high",
    r"\xrightarrow{\alpha_1^{\#}}(S(1))_{(t)}", r"\xrightarrow{\alpha_1^{\sharp}}(S(1))_{(t)}", "")

add(202, "proof of (ii), end: 'projectif de rang m\u20141, d'o\u00f9 (ii)'",
    "long dash", "minus sign", "convention", 7, "high",
    r"projectif de rang $m-1$, d'où (ii)", r"projectif de rang $m\setmin 1$, d'où (ii)",
    "Long dash for subtraction (GLOBAL_ISSUES 23).")

add(202, "proof of (iii), l. 1: 'au-dessus d'un point x\u2208X\u2014Y.'",
    "long dash", "minus sign", "convention", 7, "high",
    r"au-dessus d'un point $x\in X-Y$.", r"au-dessus d'un point $x\in X\setmin Y$.", "")

add(202, "proof of (iii), l. 2: 'restreint \u00e0 un voisinage de x, est surjectif,'",
    "'surjectif' italic", "roman", "italics", None, "high",
    r"restreint à un voisinage de $x$, est surjectif,", r"restreint à un voisinage de $x$, est \emph{surjectif},",
    "GLOBAL_ISSUES 83.")

add(202, "last line of p. 202: '(les valeurs de t\u2208E | qui v\u00e9rifient' (page break 202/203)",
    "p. 203 begins mid-sentence: 'qui v\u00e9rifient' at the left margin (x 322 px like the lines below)",
    "blank lines before and after \\oldpage[IV-4]{203}",
    "marker", None, "high",
    r"(les valeurs de $t\in E$¶¶", r"(les valeurs de $t\in E$¶",
    "The marker is at the right place. Part 1 of 2: the first p. 203 finding removes the blank line after "
    "\\oldpage[IV-4]{203}; apply both.")

# ---------------------------------------------------------------- p. 203
add(203, "top of p. 203: '\\oldpage[IV-4]{203}' + blank line before 'qui v\u00e9rifient'",
    "mid-sentence page break (see the last p. 202 finding)", "blank line after the marker",
    "marker", None, "high",
    r"\oldpage[IV-4]{203}¶¶qui vérifient", r"\oldpage[IV-4]{203}¶qui vérifient",
    "Part 2 of 2 with the last p. 202 finding; both blank lines must go.")

add(203, "l. 2: 'u(T_i)=0 pour 1\u2264i\u2264m\u20141'",
    "long dash", "minus sign", "convention", 7, "high",
    r"pour $1\leq i\leq m-1$, de sorte", r"pour $1\leq i\leq m\setmin 1$, de sorte",
    "Long dash for subtraction (GLOBAL_ISSUES 23).")

add(203, "l. 4: 'les \u00e9l\u00e9ments de la forme \u03a3_\u03b1 L_\u03b1(T)\u2297T^\u03b1 de E\u2297_A A[T_1, ..., T_{m-1}]'",
    "set in the line", "displayed", "other", None, "high",
    r"de la forme¶\[¶  \sum_\alpha L_\alpha(\mathbf T)\otimes\mathbf T^\alpha¶\]¶de $E\otimes_A",
    r"de la forme $\sum_\alpha L_\alpha(\mathbf T)\otimes\mathbf T^\alpha$ de $E\otimes_A",
    "Layout only (display vs inline, GLOBAL_ISSUES 21).")

add(203, "l. 5: 'L_\u03b1(T)=\u03bb_{\u03b10}+\u03bb_{\u03b11}T_1+...+\u03bb_{\u03b1,m-1}T_{m-1}'",
    "baseline dots (crop c203_L.png)", "\\cdots", "symbol", None, "high",
    r"\lambda_{\alpha1}T_1+\cdots+\lambda_{\alpha,m-1}", r"\lambda_{\alpha1}T_1+\ldots+\lambda_{\alpha,m-1}",
    "\\cdots where the print has baseline dots.")

add(203, "l. 6: 'lorsque la condition \u03bb_{00}=0 est remplie'",
    "\u03bb_{00}: two zeros of the same weight, no comma (crop c203_lam00.png)",
    "\\lambda_{\\mathbf0,0} (bold zero and a comma)", "formula", None, "high",
    r"$\lambda_{\mathbf0,0}=0$", r"$\lambda_{00}=0$",
    "Both subscript zeros print alike (small-type weight); the TeX added the comma and set the first zero bold.")

add(203, "l. 7: 'pour |\u03b1|\u22651'",
    "bold alpha at full size (crop c203_alpha.png)", "light \\alpha", "font", None, "high",
    r"pour $|\alpha|\geq1$", r"pour $|\boldsymbol{\alpha}|\geq1$",
    "The multi-index \u03b1 between the bars is bold; the subscript and exponent \u03b1 elsewhere are small type and are "
    "left as they are.")

add(203, "l. 9: 'Les \u00e9l\u00e9ments de l'id\u00e9al \U0001D50E correspondants'",
    "Fraktur K (crop c203_frak.png)", "\\mathscr K (script K)", "symbol", None, "high",
    r"l'idéal $\mathscr K$ correspondants", r"l'idéal $\mathfrak K$ correspondants",
    "The print has the Fraktur letter (the ideal of S_{(t)} defined by \U0001D4A6), not the script \U0001D4A6 of the statement; "
    "its shape is the Fraktur K that GLOBAL_ISSUES 63 says is often misread as R.")

add(203, "l. 13: 'en tous les points de X'\u2014Y' et que j(X')=Z'",
    "long dash", "minus sign", "convention", 7, "high",
    r"en tous les points de $X'-Y'$ et que", r"en tous les points de $X'\setmin Y'$ et que", "")

add(203, "l. 16: '(en vertu de (19.1.1) et de (0, 17.1.7))'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"et de ($0$, 17.1.7)) à dire", r"et de (\textbf{0}, 17.1.7)) à dire",
    "Bare bold 0 in the print (no subscript).")

i_ux = add(203, "l. 17: 'et que l'homomorphisme u_X\u22971 : \u2130_X\u2297_{\U0001D4AA_{X,x}}k(x) \u2192 \U0001D52A_x/\U0001D52A_x^2 est injectif'",
    "set in the line; k(x) bold italic (crop c203_ux.png)",
    "displayed; \\mathbf k(x) bold upright", "other", None, "high",
    r"et que l'homomorphisme¶\[¶  u_x\otimes1:\mathscr E_x\otimes_{\sh{O}_{X,x}}\mathbf k(x)\longrightarrow\mathfrak m_x/\mathfrak m_x^2¶\]¶est \emph{injectif}. Cela",
    r"et que l'homomorphisme $u_x\otimes1:\mathscr E_x\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x)\to\mathfrak m_x/\mathfrak m_x^2$ est \emph{injectif}. Cela",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21). One edit, which also writes the k bold italic "
    "(convention 1; not in a subscript). The print's u_X, \u2130_X are restored by the next finding (a misprint), "
    "which must be applied after this one.")

add(203, "same formula: 'u_X\u22971 : \u2130_X\u2297...'",
    "roman capital X as the subscript of u and of \u2130 (crop c203_ux.png), the same letter as the X of \U0001D4AA_{X,x}",
    "u_x, \\mathscr E_x (silent correction)",
    "misprint_in_print", None, "high",
    r"u_x\otimes1:\mathscr E_x", r"u_X\otimes1:\mathscr E_X",
    "The stalks at the point x are meant (u_x : \u2130_x \u2192 \U0001D4AA_{X,x}, as \u2130_x in the displays below). Apply AFTER "
    "the previous finding (its 'old' contains this text). The fix changes only the two subscripts.",
    corrected=r"u_x\otimes1:\mathscr E_x", after=i_ux)

add(203, "l. 18: 'pour tout z\u2208P au-dessus de x, P est r\u00e9gulier au point z (17.5.8)'",
    "'r\u00e9gulier' italic", "roman", "italics", None, "high",
    r"$P$ est régulier au point $z$", r"$P$ est \emph{régulier} au point $z$",
    "GLOBAL_ISSUES 83.")

add(203, "l. 19: 'en outre (0, 17.3.3) l'homomorphisme canonique'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"en outre ($0$, 17.3.3) l'homomorphisme", r"en outre (\textbf{0}, 17.3.3) l'homomorphisme", "")

add(203, "(19.4.11.1): '(\U0001D52A_x/\U0001D52A_x^2)\u2297_{k(x)}k(z) \u2192 \U0001D52A_z/\U0001D52A_z^2'",
    "k(z) bold italic; the subscript k(x) bold upright (crop c203_eq.png)", "\\mathbf k(z)",
    "convention", 1, "high",
    r"\mathbf k(z)\longrightarrow\mathfrak m_z/\mathfrak m_z^2¶  \tag{19.4.11.1}",
    r"\boldsymbol{k}(z)\longrightarrow\mathfrak m_z/\mathfrak m_z^2¶  \tag{19.4.11.1}",
    "The TeX has bold upright \\mathbf k; outside subscripts the print sets the residue-field k bold italic. The "
    "subscript \\mathbf k(x) stays.")

add(203, "display after (19.4.11.1): '(\u2130_x\u2297\U0001D4AA_{P,z})\u2297_{\U0001D4AA_{P,z}}k(z) \u2192 \U0001D52A_z/\U0001D52A_z^2'",
    "k(z) bold italic (crop c203_d1.png)", "\\mathbf k(z)", "convention", 1, "high",
    r"\otimes_{\sh{O}_{P,z}}\mathbf k(z)\longrightarrow", r"\otimes_{\sh{O}_{P,z}}\boldsymbol{k}(z)\longrightarrow",
    "")

add(203, "display 'le compos\u00e9': '(\u2130_x\u2297k(x))\u2297_{k(x)}k(z) \u2192 (\U0001D52A_x/\U0001D52A_x^2)\u2297_{k(x)}k(z) \u2192 ...'",
    "k(x) and the two k(z) bold italic; the two subscripts k(x) bold upright (crop c203_d2.png)",
    "\\mathbf k throughout", "convention", 1, "high",
    r"\mathbf k(x))\otimes_{\mathbf k(x)}\mathbf k(z)\longrightarrow(\mathfrak m_x/\mathfrak m_x^2)\otimes_{\mathbf k(x)}\mathbf k(z)",
    r"\boldsymbol{k}(x))\otimes_{\mathbf k(x)}\boldsymbol{k}(z)\longrightarrow(\mathfrak m_x/\mathfrak m_x^2)\otimes_{\mathbf k(x)}\boldsymbol{k}(z)",
    "Three occurrences in one edit; the subscripts stay \\mathbf k (GLOBAL_ISSUES 48).")

add(203, "'l'homomorphisme v_z\u22971 : \u210b_z\u2297_{\U0001D4AA_{P,z}}k(z) \u2192 \U0001D52A_z/\U0001D52A_z^2'",
    "k(z) bold italic", "\\mathbf k(z)", "convention", 1, "high",
    r"\otimes_{\sh{O}_{P,z}}\mathbf k(z)\to\mathfrak m_z", r"\otimes_{\sh{O}_{P,z}}\boldsymbol{k}(z)\to\mathfrak m_z",
    "")

add(203, "last line of p. 203: 'il suffit donc de montrer que les dimen-| sions' (page break 203/204)",
    "p. 204 begins with 'sions' at the left margin (x 414 px like the lines below)",
    "blank lines before and after \\oldpage[IV-4]{204}",
    "marker", None, "high",
    r"il suffit donc de montrer que les¶¶", r"il suffit donc de montrer que les¶",
    "The marker stands before the whole word 'dimensions' (the print breaks inside the word); that place is right. "
    "Part 1 of 2: the first p. 204 finding removes the blank line after \\oldpage[IV-4]{204}; apply both.")

# ---------------------------------------------------------------- p. 204
add(204, "top of p. 204: '\\oldpage[IV-4]{204}' + blank line before 'dimensions'",
    "mid-word page break (see the last p. 203 finding)", "blank line after the marker",
    "marker", None, "high",
    r"\oldpage[IV-4]{204}¶¶dimensions", r"\oldpage[IV-4]{204}¶dimensions",
    "Part 2 of 2 with the last p. 203 finding; both blank lines must go.")

add(204, "l. 1: 'sont \u00e9gales (0, 17.1.9)'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"sont égales ($0$, 17.1.9)", r"sont égales (\textbf{0}, 17.1.9)", "")

add(204, "l. 1: 'Mais en vertu de (0, 17.3.3),'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"Mais en vertu de ($0$, 17.3.3)", r"Mais en vertu de (\textbf{0}, 17.3.3)", "")

add(204, "l. 2: '\U0001D4AA_{Z,z}\u2297_{\U0001D4AA_{X,x}}k(x)'",
    "k(x) bold italic", "\\mathbf k(x)", "convention", 1, "high",
    r"\sh{O}_{Z,z}\otimes_{\sh{O}_{X,x}}\mathbf k(x)$", r"\sh{O}_{Z,z}\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x)$", "")

add(204, "l. 3: '\U0001D4AA_{X',x'}\u2297_{\U0001D4AA_{X,x}}k(x)'",
    "k(x) bold italic", "\\mathbf k(x)", "convention", 1, "high",
    r"\sh{O}_{X',x'}\otimes_{\sh{O}_{X,x}}\mathbf k(x)$", r"\sh{O}_{X',x'}\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x)$", "")

add(204, "l. 7: 'un syst\u00e8me r\u00e9gulier de param\u00e8tres (t_j)_{1\u2264j\u2264n} de B'",
    "index j (crop c204_tj.png)", "(t_i)_{1\\leq i\\leq n}", "formula", None, "high",
    r"$(t_i)_{1\leq i\leq n}$ de $B$", r"$(t_j)_{1\leq j\leq n}$ de $B$",
    "The TeX renamed the print's index (GLOBAL_ISSUES 102).")

add(204, "l. 8: 'pour 1\u2264i\u2264m (0, 17.1.7);'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"($0$, 17.1.7); soit", r"(\textbf{0}, 17.1.7); soit", "")

add(204, "l. 9: '\U0001D50D^n\u2297_B(B/\U0001D52A)=\U0001D50D^n/\U0001D52A\U0001D50D^n'",
    "parentheses around B/\U0001D52A (crop c204_Jn.png)", "\\otimes_B B/\\mathfrak m without parentheses",
    "formula", None, "high",
    r"$\mathfrak J^n\otimes_B B/\mathfrak m=", r"$\mathfrak J^n\otimes_B(B/\mathfrak m)=", "")

add(204, "l. 9-10: '(\u2295\U0001D50D^n)\u2297_B k(x) s'identifie \u00e0 k(x)[T_1, ..., T_m]'",
    "both k bold italic", "\\mathbf k twice", "convention", 1, "high",
    r"\otimes_B\mathbf k(x)$ s'identifie à $\mathbf k(x)[T_1", r"\otimes_B\boldsymbol{k}(x)$ s'identifie à $\boldsymbol{k}(x)[T_1",
    "Two occurrences in one edit.")

add(204, "19.5, introduction: 'd\u00e9j\u00e0 \u00e9tudi\u00e9s dans (0, 15.1).'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"dans ($0$, 15.1).", r"dans (\textbf{0}, 15.1).", "")

add(204, "19.5, introduction, l. 3 (first word of the line): 'étudiés'",
    "the first é of 'étudiés' is bold: heavy bowl and accent, unlike the second é of the same word "
    "and the rest of the line (crops c204_etudies.png, c204_e1.png)",
    "étudiés (silent correction)", "misprint_in_print", None, "medium",
    r"déjà étudiés", r"déjà \textbf{é}tudiés",
    "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99): a single letter at the start of the line, so not "
    "the line-end heaviness of item 100. The fix restores the printed reading; it does not touch the convention-2 edit "
    "of '(0, 15.1)' on the same line.",
    corrected=r"déjà étudiés")

add(204, "Th\u00e9or\u00e8me (19.5.1): label a)",
    "'a)' upright (crop c204_items.png)", "\\item[a)] italic inside the statement", "convention", 6, "high",
    r"\item[a)] La suite $\mathbf f$ est M-régulière.", r"\item[\textup{a)}] La suite $\mathbf f$ est M-régulière.",
    "GLOBAL_ISSUES 88: labels are upright inside italic statements.")

add(204, "Th\u00e9or\u00e8me (19.5.1): label b)",
    "'b)' upright", "\\item[b)] italic", "convention", 6, "high",
    r"\item[b)] On a $\operatorname{H}_i(\mathbf f,M)=0$", r"\item[\textup{b)}] On a $\operatorname{H}_i(\mathbf f,M)=0$",
    "GLOBAL_ISSUES 88.")

add(204, "Th\u00e9or\u00e8me (19.5.1): label b')",
    "\"b')\" upright", "\\item[b$'$)] italic", "convention", 6, "high",
    r"\item[b$'$)] On a $\operatorname{H}_1(\mathbf f,M)=0$.", r"\item[\textup{b$'$)}] On a $\operatorname{H}_1(\mathbf f,M)=0$.",
    "GLOBAL_ISSUES 88 (hand-set \\item[b$'$)] labels need \\textup).")

add(204, "Th\u00e9or\u00e8me (19.5.1): label c)",
    "'c)' upright (crop c204_items2.png)", "\\item[c)] italic", "convention", 6, "high",
    r"\item[c)] La suite $\mathbf f$ est M-quasi-régulière.", r"\item[\textup{c)}] La suite $\mathbf f$ est M-quasi-régulière.",
    "GLOBAL_ISSUES 88.")

add(204, "Th\u00e9or\u00e8me (19.5.1) b): 'pour tout i>0 (III, 1.1.3).'",
    "bold III, reference upright", "plain III, italic (environment)", "convention", 2, "high",
    r"pour tout $i>0$ (III, 1.1.3).", r"pour tout $i>0$ \textup{(\textbf{III}, 1.1.3)}.",
    "One edit for convention 2 (bold III) and convention 6 (upright reference inside the italic statement).")

add(204, "Th\u00e9or\u00e8me (19.5.1): 'Alors on a les implications' after the list",
    "indented new paragraph (first line at x 532 px, the paragraph indent; left margin 419 px)",
    "follows \\end{enumerate} without a blank line (no indent)", "other", None, "high",
    r"\end{enumerate}¶Alors on a les implications¶\[¶", r"\end{enumerate}¶¶Alors on a les implications¶\[¶",
    "GLOBAL_ISSUES 80 pattern (text after \\end{enumerate} loses the print's indent).")

add(204, "Th\u00e9or\u00e8me (19.5.1), display: 'a)\u21d2b)\u21d2b') et a)\u21d2c).'",
    "the labels are wholly italic, parentheses included (crop c204_par_c.png)",
    "math labels: italic letters, upright parentheses", "italics", None, "high",
    r"  a)\Rightarrow b)\Rightarrow b')\qquad\text{et}\qquad a)\Rightarrow c).",
    r"  \textit{a)}\Rightarrow\textit{b)}\Rightarrow\textit{b$'$)}\qquad\text{et}\qquad\textit{a)}\Rightarrow\textit{c)}.",
    "In this display, part of the italic statement, the print sets the labels italic (unlike the upright labels of the list "
    "and of the last sentence of the statement).")

add(204, "Th\u00e9or\u00e8me (19.5.1): 'Posons \U0001D50D=\u03a3 f_iA.' after the display",
    "indented new paragraph (x 532 px)", "follows \\] without a blank line (no indent)", "other", None, "high",
    r"\]¶Posons $\mathfrak J", r"\]¶¶Posons $\mathfrak J",
    "Item 47 pattern (no blank line after \\] where the print starts a new indented paragraph).")

add(204, "Th\u00e9or\u00e8me (19.5.1): '\U0001D50D-pr\u00e9adique (resp. si tout module quotient'",
    "'(resp.' upright; the closing parenthesis after the second 'pr\u00e9adique' is italic (crops c204_resp1.png, c204_par_a.png)",
    "italic (environment)", "convention", 6, "medium",
    r"préadique (resp. si tout module", r"préadique \textup{(resp.} si tout module",
    "Same form as the earlier page fixes of '(resp. ...)' in italic statements; the closing parenthesis stays italic "
    "(it follows the italic 'pr\u00e9adique' and slants like it).")

add(204, "Th\u00e9or\u00e8me (19.5.1), last line: 'l'implication c)\u21d2a) (resp. b')\u21d2a)).'",
    "two closing parentheses after the last a) (one closes '(resp.'); labels and '(resp.' upright (crops c204_resp.png, c204_par_b.png)",
    "'(resp. $b')\\Rightarrow a)$.': one closing parenthesis; labels with italic letters",
    "missing", None, "high",
    r"l'implication $c)\Rightarrow a)$ (resp. $b')\Rightarrow a)$.",
    r"l'implication \textup{c)}$\Rightarrow$\textup{a)} \textup{(resp. b$'$)}$\Rightarrow$\textup{a))}.",
    "One edit: the parenthesis that closes '(resp.' is missing in the TeX; the same edit sets the labels upright "
    "(GLOBAL_ISSUES 88) and '(resp.' roman (convention 6). The heavier 'a)).' at the line end is line-end impression "
    "(item 100), not reported.")

add(204, "proof of (19.5.1), l. 1: 'Les implications a)\u21d2c), et c)\u21d2a) lorsque'",
    "labels wholly italic in roman text", "$a)\\Rightarrow c)$: italic letters, upright parentheses", "italics", None, "high",
    r"Les implications $a)\Rightarrow c)$, et $c)\Rightarrow a)$ lorsque",
    r"Les implications \emph{a)}$\Rightarrow$\emph{c)}, et \emph{c)}$\Rightarrow$\emph{a)} lorsque",
    "GLOBAL_ISSUES 88.")

add(204, "proof of (19.5.1), l. 2: 'ont d\u00e9j\u00e0 \u00e9t\u00e9 prouv\u00e9es (0, 15.1.9)'",
    "bold 0", "plain $0$", "convention", 2, "high",
    r"prouvées ($0$, 15.1.9)", r"prouvées (\textbf{0}, 15.1.9)", "")

add(204, "proof of (19.5.1), l. 3: 'On a aussi montr\u00e9 (III, 1.1.4 et 1.1.3.3)'",
    "bold III", "plain III", "convention", 2, "high",
    r"(III, 1.1.4 et 1.1.3.3)", r"(\textbf{III}, 1.1.4 et 1.1.3.3)", "")

add(204, "proof of (19.5.1), l. 3-4: 'que a) entra\u00eene b), et b) implique trivialement b').'",
    "labels wholly italic", "$a)$ etc.: italic letters, upright parentheses", "italics", None, "high",
    r"que $a)$ entraîne $b)$, et $b)$ implique trivialement $b')$.",
    r"que \emph{a)} entraîne \emph{b)}, et \emph{b)} implique trivialement \emph{b$'$)}.",
    "GLOBAL_ISSUES 88.")

add(204, "proof of (19.5.1), l. 5: 'pr\u00e9adique, b') entra\u00eene a).'",
    "labels wholly italic", "$b')$, $a)$", "italics", None, "high",
    r"préadique, $b')$ entraîne $a)$.", r"préadique, \emph{b$'$)} entraîne \emph{a)}.",
    "GLOBAL_ISSUES 88.")

add(204, "proof of (19.5.1): 'le noyau de l'homoth\u00e9tie z\u21ddf_1z dans M'",
    "wavy arrow (crop c204_wavy.png)", "\\mapsto", "symbol", None, "high",
    r"$z\mapsto f_1z$", r"$z\leadsto f_1z$", "")

add(204, "proof of (19.5.1): '(III, 1.1.1 et 1.1.2)'",
    "bold III", "plain III", "convention", 2, "high",
    r"(III, 1.1.1 et 1.1.2)", r"(\textbf{III}, 1.1.1 et 1.1.2)", "")

add(204, "proof of (19.5.1): 'avec les notations de (III, 1.1.2),'",
    "bold III", "plain III", "convention", 2, "high",
    r"notations de (III, 1.1.2),", r"notations de (\textbf{III}, 1.1.2),", "")

add(204, "proof of (19.5.1): 'On a donc (III, 1.1.4.1) la suite exacte'",
    "bold III", "plain III", "convention", 2, "high",
    r"On a donc (III, 1.1.4.1)", r"On a donc (\textbf{III}, 1.1.4.1)", "")

add(204, "end of p. 204: display (19.5.1.1) | 'La relation H_1(f, M)=0 implique donc' (page break 204/205)",
    "p. 205 begins 'La relation' at the left margin (x 349 px like the lines below): the sentence after the display "
    "continues without a paragraph break",
    "blank lines before and after \\oldpage[IV-4]{205}",
    "marker", None, "high",
    r"\tag{19.5.1.1}\label{IV.19.5.1.1}¶\end{equation}¶¶", r"\tag{19.5.1.1}\label{IV.19.5.1.1}¶\end{equation}¶",
    "BOUNDARY FIX (page break with p. 205). The marker is at the right place. Part 1 of 2: the blank line AFTER "
    "\\oldpage[IV-4]{205} lies in the p. 205 segment (outside these pages) and must go too: "
    "'\\oldpage[IV-4]{205}\\n\\nLa relation' -> '\\oldpage[IV-4]{205}\\nLa relation'.")


# ---------------------------------------------------------------- checks
def page_text(p):
    t = open(RUN + "/page_%03d.tex" % p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    return t


src = open(SRC, encoding="utf-8", newline="").read()
assert "\r" not in src

ok = True
# simulate sequential application per page (in list order) and per source file
texts = {p: page_text(p) for p in [200, 201, 202, 203, 204]}
srcsim = src
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    o, n = d["fix"]["old"], d["fix"]["new"]
    p = d["page"]
    c_orig_page = page_text(p).count(o)
    c_page = texts[p].count(o)
    c_src = srcsim.count(o)
    c_src_orig = src.count(o)
    flag = ""
    if c_page != 1 or c_src != 1:
        flag = "  <-- PROBLEM"
        ok = False
    if d["_after"] is None and c_orig_page != 1:
        flag += "  <-- not in original page"
    print("%3d p%d page_now=%d page_orig=%d src_now=%d src_orig=%d %s%s" % (
        i, p, c_page, c_orig_page, c_src, c_src_orig, d["kind"], flag))
    texts[p] = texts[p].replace(o, n, 1)
    srcsim = srcsim.replace(o, n, 1)

# overlap check: an old string must not overlap another finding's old string in the original page
for p in texts:
    t = page_text(p)
    spans = []
    for i, d in enumerate(F):
        if d["page"] != p or d["fix"] is None or d["_after"] is not None:
            continue
        o = d["fix"]["old"]
        k = t.find(o)
        if k >= 0:
            spans.append((k, k + len(o), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP p%d: findings %d and %d" % (p, a[2], b[2]))
            ok = False

print("ALL OK" if ok else "PROBLEMS")
out = []
for d in F:
    e = dict(d)
    e.pop("_after")
    out.append(e)
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for d in out:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in [200, 201, 202, 203, 204]:
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print(len(out), "findings written")
