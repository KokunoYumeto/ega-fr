# Builds findings_210_214.json; in the strings below the pilcrow stands for a line break (LF).
import json, os
from collections import Counter

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_210_214.json')
NL = '¶'


def f(page, where, scan, tex, kind, conv, conf, old=None, new=None, note='', corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": (None if old is None else {"old": old.replace(NL, '\n'), "new": new.replace(NL, '\n')})}
    if kind == 'misprint_in_print':
        d["corrected"] = corrected
    d["note"] = note
    return d


F = []

# ---------------- p. 210 ----------------
F.append(f(210, "Théorème (14.4.1), b), end: '(ce qui signifie que Z est équidimensionnelle sur Y_0 au point x (13.2.2)).'",
    "the parenthesis is set in roman, with 'équidimensionnelle' in italics (crop p210_s1_labels.png)",
    "plain text in the italic theorem environment: italic, no emphasis on 'équidimensionnelle'", "convention", 6, "high",
    r"(ce qui signifie que $Z$ est¶  équidimensionnelle sur $Y_0$ au point $x$ (13.2.2))",
    r"\textup{(ce qui signifie que $Z$ est¶  \emph{équidimensionnelle} sur $Y_0$ au point $x$ (13.2.2))}",
    "Inside \\textup, \\emph sets 'équidimensionnelle' italic as printed."))
F.append(f(210, "Théorème (14.4.1), label b')",
    "'b')' upright, like the labels b) and c) (same crop)",
    "\\item[b$'$)] inside the italic theorem environment: italic", "convention", 6, "high",
    r"\item[b$'$)]", r"\item[\textup{b$'$)}]",
    "The automatic labels a), b) (label=\\emph{\\alph*)}) come out upright as printed; the hand-set labels do not."))
F.append(f(210, "Théorème (14.4.1), after b'): 'Si de plus Y est localement noethérien, ces conditions sont aussi équivalentes à la suivante :'",
    "new, indented paragraph (same crop)",
    "the text follows \\end{enumerate} without a blank line (no paragraph indent)", "other", None, "high",
    r"\end{enumerate}¶Si de plus", r"\end{enumerate}¶¶Si de plus",
    "Missing paragraph break (GLOBAL_ISSUES 80)."))
F.append(f(210, "Théorème (14.4.1), label c)",
    "'c)' upright (same crop)", "\\item[c)] inside the italic theorem environment: italic", "convention", 6, "high",
    r"\item[c)]", r"\item[\textup{c)}]"))
F.append(f(210, "proof of (14.4.1.1): 'Spec(k(y)[T_1, ..., T_n]) est géométriquement régulier'",
    "bold italic k (crop p210_s2_ref0.png)", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(y)[T_1,\ldots,T_n])", r"\operatorname{Spec}(\boldsymbol{k}(y)[T_1,\ldots,T_n])"))
F.append(f(210, "same sentence: 'régulier sur k(y)'",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    r"régulier sur $k(y)$", r"régulier sur $\boldsymbol{k}(y)$"))
F.append(f(210, "same sentence: '(0, 17.3.7)'",
    "bold 0 without a subscript (same crop)", "($\\mathbf{0}_{\\mathrm{IV}}$, 17.3.7): subscript IV added", "extra", None, "high",
    r"($\mathbf{0}_{\mathrm{IV}}$, 17.3.7)", r"($\mathbf{0}$, 17.3.7)",
    "Same on p. 214, (0, 23.2.5)."))
F.append(f(210, "Lemme (14.4.1.2), l. 1: 'Soient A un anneau local intègre unibranche, B un anneau intègre'",
    "'unibranche' set in roman inside the italic statement (crop p210_s2_unibr.png)",
    "italic in the italic lemma environment", "convention", 6, "high",
    r"intègre unibranche,", r"intègre \textup{unibranche},"))
F.append(f(210, "proof of (14.4.1.2): 'En vertu du second théorème de Cohen-Seidenberg'",
    "hyphen (crop p210_s3_cohen.png)", "Cohen--Seidenberg (en dash)", "punctuation", None, "high",
    r"Cohen--Seidenberg", r"Cohen-Seidenberg",
    "As the Cohen--Macaulay en dashes of ega4-2 (GLOBAL_ISSUES 74)."))
F.append(f(210, "end of the page: '... au-dessus de x, le morphisme' / p. 211 'f' : X'→Y'=Y[T_1, ..., T_n], déduit de f'",
    "the sentence runs on over the page break (p. 211 starts flush left with f')",
    "blank line before \\oldpage[IV-3]{211}: paragraph break mid-sentence", "marker", None, "high",
    r"au-dessus de $x$, le¶morphisme¶¶", r"au-dessus de $x$, le¶morphisme¶",
    "Marker position itself is right. page_211.tex also has a blank line after \\oldpage[IV-3]{211} (first p. 211 entry): apply both, either alone still leaves the paragraph break."))

# ---------------- p. 211 ----------------
F.append(f(211, "top of the page: blank line after \\oldpage[IV-3]{211}",
    "'f' : X'→Y'=Y[T_1, ..., T_n], déduit de f ...' continues the sentence of p. 210, flush left",
    "blank line between \\oldpage[IV-3]{211} and '$f':X'\\to Y'...$': paragraph break mid-sentence", "marker", None, "high",
    r"\oldpage[IV-3]{211}¶¶$f':X'", r"\oldpage[IV-3]{211}¶$f':X'",
    "Apply together with the last p. 210 entry (blank line before the marker)."))
F.append(f(211, "l. 8: 'que le morphisme f se factorise en X →g Y''=Y[T_1, ..., T_m]→Y, où g est quasi-fini'",
    "the formula is set inline in the running text, followed by its comma",
    "displayed with \\[ ... \\] (comma inside the display)", "other", None, "high",
    r"factorise en¶\[¶  X\xrightarrow{g}Y''=Y[T_1,\ldots,T_m]\to Y,¶\]¶où $g$",
    r"factorise en¶$X\xrightarrow{g}Y''=Y[T_1,\ldots,T_m]\to Y$,¶où $g$",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."))
F.append(f(211, "proof of (14.4.1.3): '(tenant compte de (I, 3.6.5) et (0_I, 2.1.8)'",
    "bold I (crop p211_s2_I365.png)", "plain I", "convention", 2, "high",
    r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)"))
F.append(f(211, "same proof: 'où j est une immersion ouverte et g un morphisme fini (évidemment dominant)'",
    "'immersion ouverte' in italics, like 'fini' (crop p211_s2_immersion.png)", "'immersion ouverte' upright", "italics", None, "high",
    r"où $j$ est une immersion ouverte et", r"où $j$ est une \emph{immersion ouverte} et",
    "The later 'u une immersion ouverte (I, 9.5.3)' is roman in the print, as in the TeX."))
F.append(f(211, "same proof: 'u une immersion ouverte (I, 9.5.3)'",
    "bold I (crop p211_s3_integre.png)", "plain I", "convention", 2, "high",
    r"(I, 9.5.3)", r"(\textbf{I}, 9.5.3)"))
F.append(f(211, "same proof: 'on peut supposer que X_1 est intègre, ou encore de la forme X_1 = Spec(B)'",
    "'intègre' in italics (same crop)", "'intègre' upright", "italics", None, "high",
    r"$X_1$ est intègre, ou", r"$X_1$ est \emph{intègre}, ou"))
F.append(f(211, "Corollaire (14.4.2), a): '(ou, ce qui revient au même (14.3.3.1, (ii)), aux points maximaux de X_y).'",
    "the parenthesis is set in roman (crop p211_s3_a.png)", "italic in the italic corollary environment", "convention", 6, "high",
    r"(ou, ce qui¶  revient au même (14.3.3.1, (ii)), aux points maximaux de $X_y$)",
    r"\textup{(ou, ce qui¶  revient au même (14.3.3.1, (ii)), aux points maximaux de $X_y$)}"))
F.append(f(211, "Corollaire (14.4.2), b): 'équidimensionnelle sur Y au point x (13.2.2).'",
    "(13.2.2) upright in the italic statement (crop p211_s4_b.png)", "italic", "convention", 6, "high",
    r"au point $x$ (13.2.2).", r"au point $x$ \textup{(13.2.2)}."))
F.append(f(211, "Corollaire (14.4.2), label b')",
    "'b')' upright (same crop)", "\\item[b$'$)] inside the italic corollary environment: italic", "convention", 6, "high",
    r"\item[b$'$)]", r"\item[\textup{b$'$)}]"))
F.append(f(211, "Corollaire (14.4.2), b'): 'on a dim(U∩X_η) ⩾ dim_x(U∩X_y).'",
    "the formula is displayed (centred on its own line, full stop inside; same crop)",
    "inline after 'on a'", "other", None, "high",
    r"on a $\dim(U\cap X_\eta)\geq\dim_x(U\cap X_y)$.",
    r"on a¶  \[¶  \dim(U\cap X_\eta)\geq\dim_x(U\cap X_y).¶  \]",
    "Inline formula where the print displays it; no connecting word involved. The b'') formula is inline in the print, as in the TeX."))
F.append(f(211, "Corollaire (14.4.2), label b'')",
    "'b'')' upright (same crop)", "\\item[b$''$)] inside the italic corollary environment: italic", "convention", 6, "high",
    r"\item[b$''$)]", r"\item[\textup{b$''$)}]"))

# ---------------- p. 212 ----------------
F.append(f(212, "Corollaire (14.4.2), label c)",
    "'c)' upright (crop p212_s1_c.png)", "\\item[c)] inside the italic corollary environment: italic", "convention", 6, "high",
    r"\item[c)] $f$ est ouvert en tous", r"\item[\textup{c)}] $f$ est ouvert en tous"))
F.append(f(212, "Corollaire (14.4.2), c): '(ou, ce qui revient au même (14.3.3.1, (ii)), aux points maximaux de X_y).'",
    "the parenthesis is set in roman (same crop)", "italic in the italic corollary environment", "convention", 6, "high",
    r"(ou, ce qui revient au même¶  (14.3.3.1, (ii)), aux points maximaux de $X_y$)",
    r"\textup{(ou, ce qui revient au même¶  (14.3.3.1, (ii)), aux points maximaux de $X_y$)}"))
F.append(f(212, "Corollaire (14.4.3), b): 'et toute générisation y' de y on a'",
    "no comma after y (crop p212_s2_b.png)", "'de $y$, on a' (comma)", "punctuation", None, "high",
    r"générisation $y'$ de¶  $y$,", r"générisation $y'$ de¶  $y$"))
F.append(f(212, "Corollaire (14.4.3), b): 'on a dim(U∩X_{y'}) ⩾ dim(U∩X_y).'",
    "the formula is displayed (centred on its own line, full stop inside; same crop)",
    "inline after 'on a'", "other", None, "high",
    r"on a $\dim(U\cap X_{y'})\geq\dim(U\cap X_y)$.",
    r"on a¶  \[¶  \dim(U\cap X_{y'})\geq\dim(U\cap X_y).¶  \]",
    "Inline formula where the print displays it. Independent of the comma fix just before it."))
F.append(f(212, "Corollaire (14.4.3), after b): 'Si de plus Y est localement noethérien, ces conditions sont aussi équivalentes à la suivante :'",
    "new, indented paragraph after the display (crop p212_s3_cor.png)",
    "the text follows \\end{enumerate} without a blank line (no paragraph indent)", "other", None, "high",
    r"\end{enumerate}¶Si de plus", r"\end{enumerate}¶¶Si de plus",
    "Missing paragraph break (GLOBAL_ISSUES 80)."))
F.append(f(212, "Corollaire (14.4.3), label c)",
    "'c)' upright (same crop)", "\\item[c)] inside the italic corollary environment: italic", "convention", 6, "high",
    r"\item[c)] $f$ est ouvert.", r"\item[\textup{c)}] $f$ est ouvert."))
F.append(f(212, "Corollaire (14.4.4), labels (i) and (ii)",
    "'(i)', '(ii)' upright (same crop)",
    "automatic labels label=(\\roman*) inside the italic corollary environment: italic", "convention", 6, "high",
    r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
    "One edit for both labels (GLOBAL_ISSUES 16)."))
F.append(f(212, "Corollaire (14.4.4), (i): 'Si f est équidimensionnel en un point x∈X (13.3.2) et si'",
    "(13.3.2) upright in the italic statement (same crop)", "italic", "convention", 6, "high",
    r"un point $x\in X$ (13.3.2) et si", r"un point $x\in X$ \textup{(13.3.2)} et si"))

# ---------------- p. 213 ----------------
F.append(f(213, "Corollaire (14.4.6), a): 'f est équidimensionnel (13.3.2) en tous les points de f^{-1}(y).'",
    "(13.3.2) upright in the italic statement (crop p213_s1_a.png)", "italic", "convention", 6, "high",
    r"équidimensionnel (13.3.2) en tous", r"équidimensionnel \textup{(13.3.2)} en tous"))
F.append(f(213, "Proposition (14.4.7), a): 'f est équidimensionnel (13.3.2) au point x.'",
    "(13.3.2) upright in the italic statement (crop p213_s2_a.png)", "italic", "convention", 6, "high",
    r"équidimensionnel (13.3.2) au point", r"équidimensionnel \textup{(13.3.2)} au point"))
F.append(f(213, "Proposition (14.4.7), after c): 'En outre, lorsque ces conditions sont satisfaites, pour tout sous-préschéma fermé réduit X_i'",
    "new, indented paragraph",
    "the text follows \\end{enumerate} without a blank line (no paragraph indent)", "other", None, "high",
    r"\end{enumerate}¶En outre, lorsque", r"\end{enumerate}¶¶En outre, lorsque",
    "Missing paragraph break (GLOBAL_ISSUES 80)."))
F.append(f(213, "proof of (14.4.7): 'prouve la dernière assertion de la proposition, compte tenu de (14.3.3.1, (ii)).'",
    "(14.3.3.1, (ii)) (crop p213_s3_ii.png)", "(14.3.3.1, (iii))", "number", None, "high",
    r"(14.3.3.1, (iii))", r"(14.3.3.1, (ii))",
    "Not a misprint: the Remarques (14.3.3.1) (pp. 204-205) have only (i) and (ii); (ii), the extension of (14.1.4) to universally open morphisms, is the result used. The TeX has the same (iii) for the printed (ii) on p. 209 (Théorème (14.4.1), a); ega4-14 line 764 of the r20 diplomatic file)."))
F.append(f(213, "(14.4.7.1): 'dim(𝒪_{X_i,x}) = dim(𝒪_y) + dim(𝒪_{X_i,x} ⊗_{𝒪_y} k(y))'",
    "bold italic k (crop p213_s3_eqs.png)", "plain k", "convention", 1, "high",
    r"X_i,x}\otimes_{\mathcal O_y}k(y))¶\end{equation}", r"X_i,x}\otimes_{\mathcal O_y}\boldsymbol{k}(y))¶\end{equation}"))
F.append(f(213, "(14.4.7.2): 'dim(𝒪_{X,x}) = dim(𝒪_y) + dim(𝒪_{X,x} ⊗_{𝒪_y} k(y))'",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    r"X,x}\otimes_{\mathcal O_y}k(y))¶\end{equation}", r"X,x}\otimes_{\mathcal O_y}\boldsymbol{k}(y))¶\end{equation}"))
F.append(f(213, "proof of (14.4.7), after (14.4.7.2): 'donc (5.2.3) dim(𝒪_{X_i,x} ⊗_{𝒪_y} k(y)) = dim(𝒪_{X,x} ⊗_{𝒪_y} k(y)). On conclut donc que'",
    "the formula is set inline at the end of the line, followed by its full stop (same crop); both k bold italic",
    "displayed with \\[ ... \\]; plain k", "other", None, "high",
    r"donc (5.2.3)¶\[¶  \dim(\mathcal O_{X_i,x}\otimes_{\mathcal O_y}k(y))=¶  \dim(\mathcal O_{X,x}\otimes_{\mathcal O_y}k(y)).¶\]¶On conclut",
    r"donc (5.2.3)¶$\dim(\mathcal O_{X_i,x}\otimes_{\mathcal O_y}\boldsymbol{k}(y))=¶\dim(\mathcal O_{X,x}\otimes_{\mathcal O_y}\boldsymbol{k}(y))$.¶On conclut",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost. The edit also carries the two convention-1 bold k of this formula (next two entries, fix null)."))
F.append(f(213, "same formula: the first k(y)",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    note="Carried by the previous edit."))
F.append(f(213, "same formula: the second k(y)",
    "bold italic k (same crop)", "plain k", "convention", 1, "high",
    note="Carried by the previous edit."))
F.append(f(213, "Proposition (14.4.8), a): 'autrement dit, pour tout changement de base g : Y'→Y'",
    "'tout' set in roman inside the italic statement (crops p213_s4_a.png, p213_s4_tout.png)",
    "italic in the italic proposition environment", "convention", 6, "high",
    r"pour tout changement de base", r"pour \textup{tout} changement de base"))
F.append(f(213, "Proposition (14.4.8), a): 'on a la propriété P(Y') :'",
    "bold italic P (crop p213_s4_a.png)", "$P(Y')$ (plain italic)", "font", None, "high",
    r"la propriété $P(Y')$~:", r"la propriété $\boldsymbol{P}(Y')$~:",
    "Property letter P. The TeX has plain $P$, not \\mathbf{P}, so this is not convention 10; form of the earlier \\boldsymbol{P} page fixes (GLOBAL_ISSUES 13/44)."))

# ---------------- p. 214 ----------------
F.append(f(214, "Proposition (14.4.8), label a')",
    "'a')' upright (crop p214_s1_a.png)", "\\item[a$'$)] inside the italic proposition environment: italic", "convention", 6, "high",
    r"\item[a$'$)]", r"\item[\textup{a$'$)}]"))
F.append(f(214, "Proposition (14.4.8), a'): 'La propriété P(Y') est vraie'",
    "bold italic P (same crop)", "$P(Y')$ (plain italic)", "font", None, "high",
    r"La propriété $P(Y')$ est vraie", r"La propriété $\boldsymbol{P}(Y')$ est vraie",
    "As on p. 213."))
F.append(f(214, "Proposition (14.4.8), a'): 'pour tout morphisme fini g : Y'→Y.'",
    "'fini' set in roman inside the italic statement (same crop)", "italic", "convention", 6, "high",
    r"pour tout morphisme fini¶", r"pour tout morphisme \textup{fini}¶"))
F.append(f(214, "Proposition (14.4.8), label a'')",
    "'a'')' upright (same crop)", "\\item[a$''$)] inside the italic proposition environment: italic", "convention", 6, "high",
    r"\item[a$''$)]", r"\item[\textup{a$''$)}]"))
F.append(f(214, "Proposition (14.4.8), a''): 'La propriété P(Y'') est vraie'",
    "bold italic P (same crop)", "$P(Y'')$ (plain italic)", "font", None, "high",
    r"La propriété $P(Y'')$ est vraie", r"La propriété $\boldsymbol{P}(Y'')$ est vraie",
    "As on p. 213."))
F.append(f(214, "Proposition (14.4.8), a''): 'pour le normalisé Y'' de Y_red'",
    "'normalisé' set in roman inside the italic statement (same crop)", "italic", "convention", 6, "high",
    r"pour le normalisé $Y''$", r"pour le \textup{normalisé} $Y''$"))
F.append(f(214, "Proposition (14.4.8), a''): '(II, 6.3.8).'",
    "the reference is upright in the italic statement (same crop)", "parentheses and numbers italic", "convention", 6, "high",
    r"(\textbf{II}, 6.3.8)", r"\textup{(\textbf{II}, 6.3.8)}"))
F.append(f(214, "proof of (14.4.8): 'qui sont quasi-cohérentes et de type fini (I, 9.6.6)'",
    "bold I", "plain I", "convention", 2, "high",
    r"(I, 9.6.6)", r"(\textbf{I}, 9.6.6)"))
F.append(f(214, "same proof: 'B est limite inductive de ses sous-𝒪_Y-Algèbres B_λ'",
    "one word 'sous-𝒪_Y-Algèbres' in the middle of the line",
    "'sous-$\\mathcal O_Y$-' ends a source line, so the line end typesets a space ('sous-𝒪_Y- Algèbres')", "other", None, "high",
    r"sous-$\mathcal O_Y$-¶Algèbres", r"sous-$\mathcal O_Y$-%¶Algèbres",
    "The hyphen stays; '%' joins the compound, as the 'quasi-' fix on IV-3 p. 112."))
F.append(f(214, "same proof: 'Spec(𝒪_y)→Y est universellement bicontinu (I, 3.6.5)'",
    "bold I (crop p214_s2_I365.png)", "plain I", "convention", 2, "high",
    r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)"))
F.append(f(214, "same proof: 'on sait (0, 23.2.5) qu'il existe une factorisation'",
    "bold 0 without a subscript (crop p214_s2_ref0.png)", "($\\mathbf{0}_{\\mathrm{IV}}$, 23.2.5): subscript IV added", "extra", None, "high",
    r"($\mathbf{0}_{\mathrm{IV}}$, 23.2.5)", r"($\mathbf{0}$, 23.2.5)",
    "As (0, 17.3.7) on p. 210."))
F.append(f(214, "same proof: 'telle que v soit un morphisme fini surjectif'",
    "only 'fini' in italics, 'surjectif' roman (crop p214_s3_fini.png)", "\\emph{fini surjectif}", "italics", None, "high",
    r"\emph{fini surjectif}", r"\emph{fini} surjectif"))
F.append(f(214, "same proof: 'u un morphisme entier, radiciel et dominant, donc surjectif'",
    "'radiciel' and 'dominant' in italics, 'et' roman (same crop)", "\\emph{radiciel et dominant}", "italics", None, "high",
    r"\emph{radiciel et dominant}", r"\emph{radiciel} et \emph{dominant}"))
F.append(f(214, "same proof: 'et un point x_1 de X_1 au-dessus de x. Mais Y_1 est noethérien'",
    "full stop set close after x, then capital 'Mais' (crops p214_s3_mais.png, p214_s3_mais_zoom.png: a round baseline dot and a small speck above it, not a colon; the print's colons have a space before them, as 'au point x : en outre', p. 211)",
    "'$x$~: Mais' (colon)", "punctuation", None, "high",
    r"au-dessus de $x$~: Mais", r"au-dessus de $x$. Mais"))
F.append(f(214, "Lemme (14.4.8.1), l. 1: 'un morphisme fermé (resp. universellement fermé) et surjectif'",
    "'(resp.' and the closing parenthesis upright, 'universellement fermé' italic (crop p214_s3_lemma.png)",
    "'(resp.' and ')' italic in the italic lemma environment", "convention", 6, "high",
    r"(resp. universellement fermé)", r"\textup{(resp.} universellement fermé\textup{)}"))
F.append(f(214, "Lemme (14.4.8.1), l. 2: 'soit ouvert (resp. universellement ouvert) en un point x∈X'",
    "'(resp.' and the closing parenthesis upright (same crop)", "italic", "convention", 6, "high",
    r"(resp. universellement ouvert) en un", r"\textup{(resp.} universellement ouvert\textup{)} en un"))
F.append(f(214, "Lemme (14.4.8.1), l. 3: 'soit ouvert (resp. universellement ouvert) en tous les points de X_1'",
    "'(resp.' and the closing parenthesis upright (crop p214_s4_lemma.png)", "italic", "convention", 6, "high",
    r"(resp. universellement ouvert) en tous", r"\textup{(resp.} universellement ouvert\textup{)} en tous"))
F.append(f(214, "end of the page: '... Pour prouver la première assertion, considérons' / p. 215 'un voisinage ouvert U de x dans X'",
    "the sentence runs on over the page break (p. 215 starts flush left with 'un voisinage')",
    "blank line before \\oldpage[IV-3]{215}: paragraph break mid-sentence", "marker", None, "high",
    r"assertion, considérons¶¶", r"assertion, considérons¶",
    "Marker position itself is right. page_215.tex also has a blank line after \\oldpage[IV-3]{215} (pp. 215-219 batch): both must go."))

# ---------------- checks ----------------
ok = True
texts = {}
for p in sorted({x['page'] for x in F}):
    with open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='') as fh:
        # the run's page files are CRLF; the release files are LF
        texts[p] = fh.read().replace('\r\n', '\n')
    if '\r' in texts[p]:
        print('stray CR in page', p)
for x in F:
    if x['fix'] is None:
        continue
    n = texts[x['page']].count(x['fix']['old'])
    if n != 1:
        ok = False
        print('NOT UNIQUE/ABSENT', x['page'], n, repr(x['fix']['old'])[:120])
for p, t in texts.items():
    spans = []
    for x in F:
        if x['page'] == p and x['fix']:
            i = t.find(x['fix']['old'])
            spans.append((i, i + len(x['fix']['old']), x['where'][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print('OVERLAP', p, a, b)

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write('\n')

c = Counter()
for x in F:
    k = 'misprint' if x['kind'] == 'misprint_in_print' else ('convention' if x['kind'] == 'convention' else 'normal')
    c[(x['page'], k)] += 1
for p in sorted(texts):
    print(p, c[(p, 'normal')], c[(p, 'convention')], c[(p, 'misprint')])
print('total', len(F), 'checks ok' if ok else 'CHECK FAILURES')
