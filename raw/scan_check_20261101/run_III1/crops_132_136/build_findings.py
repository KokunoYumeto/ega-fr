"""Build findings_132_136.json for EGA III pages 132-136 and check every fix.
Strings use the pilcrow for a line break (replaced by a newline)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_132_136.json"


def N(s):
    return None if s is None else s.replace("¶", "\n")


def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, fixnull=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf)
    d["fix"] = None if fixnull else {"old": N(old), "new": N(new)}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 131 (outside the range)
add(131, "end of p. 131 (Remarque (4.3.4)): '... est connexe.' / p. 132 'Sous les hypothèses de (4.3.2)'",
    "the paragraph runs on: the last line of p. 131 is a full line and the first line of p. 132 is not indented",
    "blank line before \\oldpage[III]{132} (paragraph break)", "other", None, "high",
    r"\operatorname{Spec}(k)$ est connexe.¶¶", r"\operatorname{Spec}(k)$ est connexe.¶",
    "OUTSIDE pages 132-136: 'old' lies in page_131.tex. Spurious paragraph break at the page break "
    "(GLOBAL_ISSUES item 20). Apply together with the p. 132 top-of-page entry.")

# ---------------------------------------------------------------- page 132
P = 132
add(P, "top of p. 132: 'Sous les hypothèses de (4.3.2), on peut alors en renforcer la conclusion' (Remarque (4.3.4) continued)",
    "first line flush left: the paragraph of p. 131 continues", "blank line after \\oldpage[III]{132}",
    "other", None, "high", r"\oldpage[III]{132}¶¶Sous les", r"\oldpage[III]{132}¶Sous les",
    "Spurious paragraph break (GLOBAL_ISSUES item 20). Apply together with the p. 131 entry (blank line before the marker). "
    "\\oldpage ends with \\ignorespaces, so joining the lines leaves one space.")
add(P, "Remarque (4.3.4): 'pour toute extension k de k(y), il existe un anneau local'",
    "k(y) with bold italic k", "$k(y)$", "convention", 1, "high",
    r"de $k(y)$, il existe", r"de $\boldsymbol{k}(y)$, il existe", "")
add(P, "Remarque (4.3.4): 'soit k(y)-isomorphe à k'", "k(y) with bold italic k", "$k(y)$-isomorphe",
    "convention", 1, "high", r"$k(y)$-isomorphe", r"$\boldsymbol{k}(y)$-isomorphe", "")
add(P, "Remarque (4.3.4): '(0, 10.3.1)'", "bold 0", "(0, 10.3.1)", "convention", 2, "high",
    r"(0, 10.3.1)", r"(\textbf{0}, 10.3.1)", "")
add(P, "Remarque (4.3.4): 'transformant l'unique point fermé y_1 de Y_1'", "point fermé", "point fermée",
    "word", None, "high", r"point fermée", r"point fermé", "Masculine 'fermé' in the print (crop).")
add(P, "Remarque (4.3.4): '(I, 2.4.1)'", "bold I", "(I, 2.4.1)", "convention", 2, "high",
    r"(I, 2.4.1)", r"(\textbf{I}, 2.4.1)", "")
add(P, "Remarque (4.3.4): '(II, 5.4.2, (iii))'", "bold II", "(II, 5.4.2, (iii))", "convention", 2, "high",
    r"(II, 5.4.2, (iii))", r"(\textbf{II}, 5.4.2, (iii))", "")
add(P, "Remarque (4.3.4): 'f_1^{-1}(y_1) est un k(y_1)-préschéma'", "k(y_1) with bold italic k", "$k(y_1)$-préschéma",
    "convention", 1, "high", r"$k(y_1)$-préschéma", r"$\boldsymbol{k}(y_1)$-préschéma", "")
add(P, "Remarque (4.3.4): 'Or g est un morphisme plat, comme il résulte de (I, 2.4.2) et de (1.4.15.5)'",
    "Or g est un morphisme plat (crop: g)", "Or $g$ est un morphisme plat", "misprint_in_print", None, "high",
    None, None,
    "The TeX keeps the printed reading. The flat morphism is h : Y_1 -> Y (A is a flat O_y-module); g is not defined "
    "under the hypotheses of (4.3.2). The corrected edition (editions/2026-10-24-r20/current) already reads $h$.",
    corrected=r"Or $h$ est un morphisme \emph{plat}", fixnull=True)
add(P, "Remarque (4.3.4): 'Or g est un morphisme plat, comme'", "'plat' in italics", "plat (upright)",
    "italics", None, "high", r"un morphisme plat,", r"un morphisme \emph{plat},",
    "Italic in the print (crop); judged as roman remark body.")
add(P, "Remarque (4.3.4): '(I, 2.4.2)'", "bold I", "(I, 2.4.2)", "convention", 2, "high",
    r"(I, 2.4.2)", r"(\textbf{I}, 2.4.2)", "")
add(P, "Remarque (4.3.4): 'on a donc f_{1*}(O_{X_1}) = h^*(f_*(O_X)) = h^*(O_Y) = O_{Y_1} en vertu de (1.4.15)'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶f_{1*}(\mathcal O_{X_1})¶=h^*(f_*(\mathcal O_X))¶=h^*(\mathcal O_Y)¶=\mathcal O_{Y_1}¶\]",
    r"$f_{1*}(\mathcal O_{X_1})¶=h^*(f_*(\mathcal O_X))¶=h^*(\mathcal O_Y)¶=\mathcal O_{Y_1}$",
    "Layout: inline in the print ('en vertu de' follows on the same line).")
add(P, "Remarque (4.3.4), 2nd paragraph: '(avec les notations de (4.3.1)) f_{1*}(O_{X_1}) = h^*(g_*(O_{Y'})), et la factorisation'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶f_{1*}(\mathcal O_{X_1})=h^*(g_*(\mathcal O_{Y'})),¶\]",
    r"$f_{1*}(\mathcal O_{X_1})=h^*(g_*(\mathcal O_{Y'}))$,",
    "Layout: inline in the print; the comma follows the formula.")
add(P, "Remarque (4.3.4), 2nd paragraph: '(II, 1.5.2)'", "bold II", "(II, 1.5.2)", "convention", 2, "high",
    r"(II, 1.5.2)", r"(\textbf{II}, 1.5.2)", "")
add(P, "Remarque (4.3.4), 2nd paragraph: '(I, 3.6.4)'", "bold I", "(I, 3.6.4)", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)", "")
add(P, "Remarque (4.3.4), 2nd paragraph: 'égal au nombre d'éléments de g_1^{-1}(y_1) = g^{-1}(y) ⊗_{k(y)} k. Si on prend'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶g_1^{-1}(y_1)=g^{-1}(y)\otimes_{k(y)}k.¶\]",
    r"$g_1^{-1}(y_1)=g^{-1}(y)\otimes_{\boldsymbol{k}(y)}k$.",
    "Layout: inline in the print. The new text also sets the bold italic k of the subscript k(y) (next finding).")
add(P, "Remarque (4.3.4), 2nd paragraph: subscript of ⊗_{k(y)}", "k(y) with bold italic k", "\\otimes_{k(y)}",
    "convention", 1, "high", None, None, "Covered by the edit of the preceding finding (display set inline).", fixnull=True)
add(P, "Remarque (4.3.4), 2nd paragraph: 'Si on prend pour k une extension algébriquement close de k(y)'",
    "'algébriquement close' in italics (first occurrence only)", "algébriquement close (upright)", "italics", None, "high",
    r"une extension algébriquement close", r"une extension \emph{algébriquement close}",
    "The second occurrence, 'l'extension algébriquement close considérée', is roman as in the TeX.")
add(P, "Remarque (4.3.4), 2nd paragraph: 'close de k(y), ce nombre'", "k(y) with bold italic k", "$k(y)$",
    "convention", 1, "high", r"$k(y)$, ce nombre", r"$\boldsymbol{k}(y)$, ce nombre", "")
add(P, "Remarque (4.3.4), 2nd paragraph: 'égal au nombre géométrique de points de g^{-1}(y)'",
    "'nombre géométrique de points de' all italic, including the last 'de'",
    "\\emph{nombre géométrique de points} de", "italics", None, "high",
    r"\emph{nombre géométrique de points} de", r"\emph{nombre géométrique de points de}",
    "Crop: the 'de' before g^{-1}(y) is italic.")
add(P, "Remarque (4.3.4), 2nd paragraph: '(I, 6.4.7)'", "bold I", "(I, 6.4.7)", "convention", 2, "high",
    r"(I, 6.4.7)", r"(\textbf{I}, 6.4.7)", "")
add(P, "Remarque (4.3.4), 2nd paragraph: 'la somme des rangs séparables [k(y'_i) : k(y)]_s où y'_i parcourt'",
    "[k(y'_i) : k(y)]_s inline, without a summation sign", "displayed \\sum_i[k(y'_i):k(y)]_s",
    "extra", None, "high",
    r"\[¶\sum_i[k(y'_i):k(y)]_s¶\]", r"$[\boldsymbol{k}(y'_i):\boldsymbol{k}(y)]_s$",
    "The TeX adds \\sum_i and displays the formula; the print has only the bracket, inline. The new text also sets the two "
    "bold italic k (next two findings).")
add(P, "Remarque (4.3.4), 2nd paragraph: '[k(y'_i) : ...'", "k(y'_i) with bold italic k", "k(y'_i)",
    "convention", 1, "high", None, None, "Covered by the edit of the preceding finding.", fixnull=True)
add(P, "Remarque (4.3.4), 2nd paragraph: '... : k(y)]_s'", "k(y) with bold italic k", "k(y)",
    "convention", 1, "high", None, None, "Covered by the edit of the finding for the summation sign.", fixnull=True)
add(P, "Remarque (4.3.4), end: 'On notera que les k(y'_i) ne sont autres que'", "k(y'_i) with bold italic k", "$k(y'_i)$",
    "convention", 1, "high", r"les $k(y'_i)$ ne sont", r"les $\boldsymbol{k}(y'_i)$ ne sont", "")
add(P, "proof of Proposition (4.3.5): 'pour tout ouvert U de Y, Γ(U, f_*(O_X)) = Γ(f^{-1}(U), O_X) est l'intersection'",
    "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\Gamma(U,f_*(\mathcal O_X))=\Gamma(f^{-1}(U),\mathcal O_X)¶\]",
    r"$\Gamma(U,f_*(\mathcal O_X))=\Gamma(f^{-1}(U),\mathcal O_X)$",
    "Layout: inline in the print ('est l'inter-' follows on the same line).")
add(P, "proof of Proposition (4.3.5): '(I, 8.2.1.1)'", "bold I", "(I, 8.2.1.1)", "convention", 2, "high",
    r"(I, 8.2.1.1)", r"(\textbf{I}, 8.2.1.1)", "")
add(P, "Définition (4.3.6): 'On dit qu'un anneau local intègre est unibranche si'",
    "'unibranche' italic like the rest of the statement (no change of face)",
    "\\emph{unibranche} inside the italic definition environment: upright", "convention", 6, "high",
    r"\emph{unibranche}", r"unibranche", "FIX_POLICY 6: drop \\emph where the print shows no change of face.")
add(P, "Définition (4.3.6): '(ce qui est en particulier le cas lorsque Y est normal au point y)'",
    "the parenthesis is roman, with 'normal' in italics", "italic (definition environment), 'normal' not marked",
    "convention", 6, "high",
    r"(ce qui¶est en particulier le cas lorsque $Y$ est normal au point $y$)",
    r"\textup{(ce qui¶est en particulier le cas lorsque $Y$ est \emph{normal} au point $y$)}",
    "Crop. \\emph{normal} inside \\textup keeps the printed italic 'normal'.")
add(P, "bottom of p. 132: 'Réciproquement, A' est limite inductive' / p. 133 'de la famille filtrante'",
    "the sentence runs on to p. 133 (no paragraph break)", "blank line before \\oldpage[III]{133}",
    "other", None, "high", r"est limite inductive¶¶", r"est limite inductive¶",
    "Spurious paragraph break at a page break inside a sentence (GLOBAL_ISSUES item 20). Apply together with the "
    "p. 133 top-of-page entry.")

# ---------------------------------------------------------------- page 133
P = 133
add(P, "top of p. 133: 'de la famille filtrante croissante des sous-A-algèbres finies'",
    "continues the sentence of p. 132", "blank line after \\oldpage[III]{133}", "other", None, "high",
    r"\oldpage[III]{133}¶¶de la famille", r"\oldpage[III]{133}¶de la famille",
    "Apply together with the p. 132 entry 'est limite inductive'. \\oldpage ends with \\ignorespaces.")
add(P, "after Définition (4.3.6): '(0, 10.3.1.3)'", "bold 0", "(0, 10.3.1.3)", "convention", 2, "high",
    r"(0, 10.3.1.3)", r"(\textbf{0}, 10.3.1.3)", "")
add(P, "'si le complété d'un anneau local noethérien A est intègre'", "'noethérien' in italics",
    "noethérien (upright)", "italics", None, "high",
    r"local noethérien $A$ est intègre", r"local \emph{noethérien} $A$ est intègre", "Crop.")
add(P, "'(ce qu'on exprime en disant que A est analytiquement intègre), A est unibranche.'",
    "'unibranche' in italics", "unibranche (upright)", "italics", None, "high",
    r"est unibranche. Soient", r"est \emph{unibranche}. Soient", "Crop.")
add(P, "'on a donc K' = K ⊗_A Â. Soit A'_F'", "formula set inline in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶K'=K\otimes_A\widehat A.¶\]", r"$K'=K\otimes_A\widehat A$.", "Layout: inline in the print.")
add(P, "line 7 of p. 133: 'on a donc K' = K ⊗_A Â'", "K' = K ⊗_A Â", "$K'=K\\otimes_A\\widehat A$",
    "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading. Authors' errata (ega3-7-fr.tex, item (III, 4.3.6)): 'Ligne 7 de la p. 133, "
    "remplacer K'=K⊗_A Â par K'⊃K⊗_A Â'.",
    corrected=r"$K'\supset K\otimes_A\widehat A$", fixnull=True)
add(P, "'c'est un Â-module de type fini, complété de A'_F pour la topologie m-adique'", "'complété' in italics",
    "complété (upright)", "italics", None, "high",
    r"complété de $A'_F$", r"\emph{complété} de $A'_F$", "Crop.")
add(P, "'(0_I, 7.3.3 et 7.3.6)'", "bold 0", "(0\\textsubscript{I}, 7.3.3 et 7.3.6)", "convention", 2, "high",
    r"(0\textsubscript{I}, 7.3.3 et 7.3.6)", r"(\textbf{0}\textsubscript{I}, 7.3.3 et 7.3.6)", "")
add(P, "Corollaire (4.3.7): 'Sous les hypothèses de (4.3.5), supposons'",
    "(4.3.5) upright inside the italic statement",
    "(\\hyperref[III.4.3.5-fr]{4.3.5}) inside the italic corollary environment: italic", "convention", 6, "high",
    r"de (\hyperref[III.4.3.5-fr]{4.3.5}), supposons", r"de \textup{(\hyperref[III.4.3.5-fr]{4.3.5})}, supposons",
    "Crop: upright parentheses and old-style figures.")
add(P, "line 16 of p. 133, Corollaire (4.3.7): 'est radicielle sur R(X), f^{-1}(y) est connexe'",
    "radicielle sur R(X)", "radicielle sur $\\mathrm R(X)$", "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading. Authors' errata (ega3-7-fr.tex, item (III, 4.3.6)): 'Ligne 16 de la p. 133, "
    "remplacer R(X) par R(Y)'.",
    corrected=r"radicielle sur $\mathrm R(Y)$", fixnull=True)
add(P, "proof of (4.3.7): 'soit O''_y la clôture intégrale de O_y; la fermeture intégrale O'_y de O_y dans R(X) est aussi "
    "celle de O''_y; mais on sait que si O''_y est un anneau local, O'_y est un anneau semi-local'",
    "O''_y = clôture intégrale of O_y, O'_y = fermeture intégrale in R(X) (as in (4.3.5))",
    "the primes are exchanged in all five places (O'_y clôture intégrale, O''_y fermeture dans R(X))",
    "formula", None, "high",
    r"soit $\mathcal O'_y$ la clôture intégrale de $\mathcal O_y$~; la¶fermeture intégrale $\mathcal O''_y$ de $\mathcal O_y$ dans $\mathrm R(X)$¶est aussi celle de $\mathcal O'_y$~; mais on sait que si $\mathcal O'_y$ est¶un anneau local, $\mathcal O''_y$ est",
    r"soit $\mathcal O''_y$ la clôture intégrale de $\mathcal O_y$~; la¶fermeture intégrale $\mathcal O'_y$ de $\mathcal O_y$ dans $\mathrm R(X)$¶est aussi celle de $\mathcal O''_y$~; mais on sait que si $\mathcal O''_y$ est¶un anneau local, $\mathcal O'_y$ est",
    "Crop. The print's notation agrees with (4.3.5), where O'_y is the integral closure of O_y in R(X); not a misprint.")
add(P, "Remarque (4.3.8): 'l'hypothèse que Y est normal au point y'", "'normal' in italics", "normal (upright)",
    "italics", None, "high", r"que $Y$ est normal au point $y$, la fibre", r"que $Y$ est \emph{normal} au point $y$, la fibre",
    "Judged as roman remark body.")
add(P, "Remarque (4.3.8): 'et que k(y') est radiciel'", "k(y') with bold italic k", "$k(y')$", "convention", 1, "high",
    r"que $k(y')$", r"que $\boldsymbol{k}(y')$", "")
add(P, "Remarque (4.3.8): 'radiciel sur k(y).'", "k(y) with bold italic k", "$k(y)$", "convention", 1, "high",
    r"radiciel sur $k(y)$", r"radiciel sur $\boldsymbol{k}(y)$", "")
add(P, "Définition (4.3.9): 'on dit qu'un morphisme de type fini f : X → Y est universellement ouvert'",
    "'de type fini' roman inside the italic statement", "italic (definition environment)", "convention", 6, "high",
    r"morphisme de¶type fini", r"morphisme \textup{de¶type fini}", "Crop: 'de type fini' is upright.")
add(P, "Définition (4.3.9): 'est universellement ouvert si'",
    "'universellement ouvert' italic like the rest of the statement (no change of face)",
    "\\emph{universellement ouvert} inside the italic environment: upright", "convention", 6, "high",
    r"\emph{universellement ouvert}", r"universellement ouvert", "FIX_POLICY 6: drop \\emph (crop).")
add(P, "after (4.3.9): 'rencontre f'^{-1}(η') (0_I, 2.1.8); cela implique'", "bold 0",
    "(0\\textsubscript{I}, 2.1.8)", "convention", 2, "high",
    r"(0\textsubscript{I}, 2.1.8)~; cela", r"(\textbf{0}\textsubscript{I}, 2.1.8)~; cela", "")
add(P, "after (4.3.9), end of the paragraph: 'restriction de f, est universellement ouvert,'",
    "the paragraph ends with a comma (enlarged crop)", "full stop", "misprint_in_print", None, "high",
    r"restriction de $f$, est universellement ouvert.", r"restriction de $f$, est universellement ouvert,",
    "The TeX silently corrects the print; the fix restores the printed comma.",
    corrected=r"restriction de $f$, est universellement ouvert.")
add(P, "Corollaire (4.3.10): 'Soient X, Y deux préschémas localement noethériens intègres. f : X → Y un morphisme'",
    "full stop after 'intègres' (enlarged crop)", "full stop (kept)", "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading; the enumeration of the hypotheses needs a comma.",
    corrected=r"localement noethériens intègres,", fixnull=True)
add(P, "proof of (4.3.10): '(II, 7.1.7)'", "bold II", "(II, 7.1.7)", "convention", 2, "high",
    r"(II, 7.1.7)", r"(\textbf{II}, 7.1.7)", "")
add(P, "proof of (4.3.10): 'un anneau local noethérien intégralement clos A'", "'noethérien intégralement clos' in italics",
    "upright", "italics", None, "high",
    r"local noethérien intégralement clos $A$", r"local \emph{noethérien intégralement clos} $A$", "")

page133 = page_text(133)
start = page133.index(r"$X'=X\times_YY'$, $f'=f\times1_{Y'}$~;")
block = page133[start:]
assert block.endswith("$k(\\xi')=k(\\xi)$.\n\n"), repr(block[-40:])
fixed = (block.replace(r"$k(\eta)=k(\eta')", r"$\boldsymbol{k}(\eta)=\boldsymbol{k}(\eta')")
         .replace(r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
         .replace(r"(0\textsubscript{I}, 2.1.8)", r"(\textbf{0}\textsubscript{I}, 2.1.8)")
         .replace(r"$k(\xi')=k(\xi)$", r"$\boldsymbol{k}(\xi')=\boldsymbol{k}(\xi)$"))
assert fixed.count("boldsymbol") == 4 and fixed.count("textbf") == 2
add(P, "end of the p. 133 segment: 'X' = X ×_Y Y', f' = f × 1_{Y'}; désignons par ... on a k(ξ') = k(ξ).'",
    "printed p. 133 ends with 'Soient'; this text is the first eleven lines of p. 134",
    "the text stands before \\oldpage[III]{134}", "marker", None, "high",
    block.replace("\n", "¶"), "",
    "Two-part move (the text moves, not the marker, so each edit stays inside its own page segment and the order does not "
    "matter): this edit deletes the text from the end of p. 133, the p. 134 marker finding re-inserts it after "
    "\\oldpage[III]{134}. Apply both or neither.")

# ---------------------------------------------------------------- page 134
P = 134
add(P, "start of p. 134: 'X' = X ×_Y Y', f' = f × 1_{Y'}; ... et on a k(ξ') = k(ξ). Posons X'' = X'_red'",
    "p. 134 begins with this text, in the same paragraph as 'Posons'", "\\oldpage[III]{134} followed by a blank line and 'Posons'",
    "marker", None, "high",
    r"\oldpage[III]{134}¶¶Posons", "\\oldpage[III]{134}¶" + fixed.rstrip("\n").replace("\n", "¶") + "¶Posons",
    "Second half of the move begun by the p. 133 marker finding. Apply both or neither. The re-inserted text also sets the "
    "conventions of the next six findings (bold italic k four times, bold I and bold 0), and joins 'k(ξ).' and 'Posons' "
    "into one paragraph as printed.")
for w, s, t, c in [("'en outre, k(η) = k(η') = R(Y)': k(η)", "k(η) with bold italic k", "$k(\\eta)$", 1),
                   ("'en outre, k(η) = k(η') = R(Y)': k(η')", "k(η') with bold italic k", "k(\\eta')", 1),
                   ("'isomorphe à f^{-1}(η) (I, 3.6.4)'", "bold I", "(I, 3.6.4)", 2),
                   ("'générique de f^{-1}(η) (0_I, 2.1.8)'", "bold 0", "(0\\textsubscript{I}, 2.1.8)", 2),
                   ("'et on a k(ξ') = k(ξ)': k(ξ')", "k(ξ') with bold italic k", "$k(\\xi')", 1),
                   ("'et on a k(ξ') = k(ξ)': k(ξ)", "k(ξ) with bold italic k", "k(\\xi)$", 1)]:
    add(P, "moved text at the top of p. 134: " + w, s, t, "convention", c, "high", None, None,
        "Covered by the p. 134 marker finding (the re-inserted text carries the correction); the text is in page_133.tex now.",
        fixnull=True)
add(P, "'f'' est propre (II, 5.4.6)'", "bold II", "(II, 5.4.6)", "convention", 2, "high",
    r"(II, 5.4.6)", r"(\textbf{II}, 5.4.6)", "")
add(P, "'R(X'') = k(ξ') = R(X)'", "k(ξ') with bold italic k", "k(\\xi')", "convention", 1, "high",
    r"\mathrm R(X'')=k(\xi')", r"\mathrm R(X'')=\boldsymbol{k}(\xi')", "")
add(P, "'une extension quelconque de k(y); il existe'", "k(y) with bold italic k", "$k(y)$", "convention", 1, "high",
    r"$k(y)$~; il existe", r"$\boldsymbol{k}(y)$~; il existe", "")
add(P, "'une extension k_1 de k(y) dont'", "k(y) with bold italic k", "$k(y)$", "convention", 1, "high",
    r"$k_1$ de $k(y)$", r"$k_1$ de $\boldsymbol{k}(y)$", "")
add(P, "'dont k(y') et k peuvent être considérés'", "k(y') with bold italic k", "$k(y')$", "convention", 1, "high",
    r"$k(y')$ et $k$ peuvent", r"$\boldsymbol{k}(y')$ et $k$ peuvent", "")
add(P, "'(I, 5.1.8)'", "bold I", "(I, 5.1.8)", "convention", 2, "high", r"(I, 5.1.8)", r"(\textbf{I}, 5.1.8)", "")
add(P, "'isomorphe à f^{-1}(y) ×_Y Spec(k_1) (I, 3.6.4), on en conclut'", "bold I", "(I, 3.6.4)", "convention", 2, "high",
    r"(I, 3.6.4), on en conclut", r"(\textbf{I}, 3.6.4), on en conclut", "")
add(P, "Remarques (4.3.11) (ii): 'pour tout morphisme Z → Y'", "'tout' in italics", "tout (upright)", "italics", None,
    "high", r"pour tout morphisme $Z\to Y$", r"pour \emph{tout} morphisme $Z\to Y$", "Crop.")
add(P, "Remarques (4.3.11) (ii): 'le morphisme f_{(Z)} : X_{(Z)} → Z est ouvert.'", "'ouvert' in italics",
    "ouvert (upright)", "italics", None, "high", r"est ouvert. On peut", r"est \emph{ouvert}. On peut", "Crop.")
add(P, "Remarques (4.3.11) (ii): 'tels que y soit une spécialisation de y''", "'spécialisation' in italics",
    "spécialisation (upright)", "italics", None, "high", r"une spécialisation de", r"une \emph{spécialisation} de", "")
add(P, "Corollaire (4.3.12): 'Sous les hypothèses de (4.3.5), supposons en outre'",
    "(4.3.5) upright inside the italic statement",
    "(\\hyperref[III.4.3.5-fr]{4.3.5}) inside the italic corollary environment: italic", "convention", 6, "high",
    r"de (\hyperref[III.4.3.5-fr]{4.3.5}), supposons", r"de \textup{(\hyperref[III.4.3.5-fr]{4.3.5})}, supposons",
    "Crop: upright parentheses and old-style figures.")
add(P, "Corollaire (4.3.12): '(et R(Y) algébriquement fermé dans R(X)) f_*(O_X) est isomorphe à O_Y'",
    "no comma after 'R(X))' (crop of the line end; the next line begins with f_*)", "$\\mathrm R(X)$), $f_*(\\mathcal O_X)$",
    "misprint_in_print", None, "medium",
    r"$\mathrm R(X)$), $f_*(\mathcal O_X)$", r"$\mathrm R(X)$) $f_*(\mathcal O_X)$",
    "The TeX silently supplies the comma that closes the conditional clause; the fix restores the printed reading. "
    "'medium' refers to calling the omission a misprint; the reading itself is certain.",
    corrected=r"$\mathrm R(X)$), $f_*(\mathcal O_X)$")
add(P, "bottom of p. 134: '... cas particulier de (4.3.8). On en' / p. 135 'déduit que si'",
    "the sentence runs on to p. 135", "blank line before \\oldpage[III]{135}", "other", None, "high",
    r"). On en¶¶", r"). On en¶",
    "Spurious paragraph break inside a sentence (GLOBAL_ISSUES item 20). Apply together with the p. 135 top-of-page entry.")

# ---------------------------------------------------------------- page 135
P = 135
add(P, "top of p. 135: 'déduit que si f : X → Y' → Y est la factorisation de Stein'", "continues the sentence of p. 134",
    "blank line after \\oldpage[III]{135}", "other", None, "high",
    r"\oldpage[III]{135}¶¶déduit", r"\oldpage[III]{135}¶déduit", "Apply together with the p. 134 entry '). On en'.")
add(P, "proof of (4.3.12): 'si f : X →^{f'} Y' →^{g} Y est la factorisation de Stein de f'", "'f :' before X",
    "$X\\xrightarrow{f'}Y'\\xrightarrow{g}Y$ (no 'f:')", "formula", None, "high",
    r"$X\xrightarrow{f'}Y'", r"$f:X\xrightarrow{f'}Y'", "Crop.")
add(P, "proof of (4.3.12): 'on a O_y ⊂ O_{y'} = (f_*(O_X))_y ⊂ R(X), et comme'", "formula set inline in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"\[¶\mathcal O_y\subset\mathcal O_{y'}=(f_*(\mathcal O_X))_y¶\subset\mathrm R(X),¶\]",
    r"$\mathcal O_y\subset\mathcal O_{y'}=(f_*(\mathcal O_X))_y¶\subset\mathrm R(X)$,", "Layout: inline in the print.")
add(P, "proof of (4.3.12): 'et comme O_{y'} est fini sur O_y, (et a fortiori sur R(Y)), il est contenu'",
    "comma after O_y before the parenthesis (crop)", "no comma", "misprint_in_print", None, "medium",
    r"fini sur $\mathcal O_y$ (et", r"fini sur $\mathcal O_y$, (et",
    "The TeX silently corrects the print; the fix restores the printed comma. 'medium' refers to calling it a misprint "
    "(a comma before an opening parenthesis); the reading itself is certain.",
    corrected=r"fini sur $\mathcal O_y$ (et")
add(P, "proof of (4.3.12): 'isomorphisme local au point y' (I, 6.5.4), ce qui achève'", "bold I", "(I, 6.5.4)",
    "convention", 2, "high", r"(I, 6.5.4), ce qui", r"(\textbf{I}, 6.5.4), ce qui", "")
add(P, "proof of Proposition (4.3.13): '(II, 8.1.4)'", "bold II", "(II, 8.1.4)", "convention", 2, "high",
    r"(II, 8.1.4)", r"(\textbf{II}, 8.1.4)", "")
add(P, "proof of Proposition (4.3.13): '(I, 3.6.1 et II, 2.8.10)': I", "bold I", "(I, 3.6.1", "convention", 2, "high",
    r"(I, 3.6.1", r"(\textbf{I}, 3.6.1", "")
add(P, "proof of Proposition (4.3.13): '(I, 3.6.1 et II, 2.8.10)': II", "bold II", "II, 2.8.10)", "convention", 2, "high",
    r"II, 2.8.10)", r"\textbf{II}, 2.8.10)", "")
add(P, "heading 4.4: '4.4. Le « main theorem » de Zariski.'", "final full stop after the title",
    "\\subsection{Le «~main theorem~» de Zariski} (no full stop)", "punctuation", None, "high",
    r"\subsection{Le «~main theorem~» de Zariski}", r"\subsection{Le «~main theorem~» de Zariski.}",
    "Same treatment as the heading fixes applied for 12.4, 13.1, 13.2 (0_III pp. 62-65).")
add(P, "Proposition (4.4.1): 'et si f = g∘f' est la factorisation de Stein de f'", "g∘f' with the composition circle",
    "$f=gf'$", "formula", None, "high", r"$f=gf'$", r"$f=g\circ f'$", "Crop.")
add(P, "Proposition (4.4.1): 'de Stein de f (4.3.3), la restriction'", "(4.3.3) upright inside the italic statement",
    "(\\hyperref[III.4.3.3-fr]{4.3.3}) inside the italic proposition environment: italic", "convention", 6, "high",
    r"(\hyperref[III.4.3.3-fr]{4.3.3}), la restriction", r"\textup{(\hyperref[III.4.3.3-fr]{4.3.3})}, la restriction", "")
add(P, "proof of (4.4.1): '(4.3.3 et II, 6.1.7)'", "bold II", "II, 6.1.7", "convention", 2, "high",
    r"et II, 6.1.7)", r"et \textbf{II}, 6.1.7)", "")
add(P, "proof of (4.4.1): 'f^{-1}(f(x)), qui est connexe (4.3.2) est nécessairement réduit au point x'",
    "no comma after (4.3.2) (crop of the line end; the next line begins with 'est')",
    "(\\hyperref[III.4.3.2-fr]{4.3.2}), est", "misprint_in_print", None, "medium",
    r"(\hyperref[III.4.3.2-fr]{4.3.2}), est", r"(\hyperref[III.4.3.2-fr]{4.3.2}) est",
    "The TeX silently supplies the comma closing the relative clause; the fix restores the printed reading. 'medium' "
    "refers to calling the omission a misprint; the reading itself is certain.",
    corrected=r"(\hyperref[III.4.3.2-fr]{4.3.2}), est")
add(P, "proof of (4.4.1): 'f(X—V) est fermé dans Y'", "long dash X—V", "$f(X-V)$", "convention", 7, "high",
    r"$f(X-V)$ est fermé", r"$f(X\setmin V)$ est fermé", "Long dash in the print; \\setmin as in the convention-7 pass.")
add(P, "proof of (4.4.1): 'le complémentaire de f(X—V) dans Y'", "long dash X—V", "$f(X-V)$", "convention", 7, "high",
    r"$f(X-V)$ dans $Y$", r"$f(X\setmin V)$ dans $Y$", "Long dash in the print; \\setmin as in the convention-7 pass.")
add(P, "proof of (4.4.1): '(0_I, 3.4.1 et 4.2.1)'", "bold 0", "(0\\textsubscript{I}, 3.4.1 et 4.2.1)", "convention", 2,
    "high", r"(0\textsubscript{I}, 3.4.1 et 4.2.1)", r"(\textbf{0}\textsubscript{I}, 3.4.1 et 4.2.1)", "")
add(P, "proof of (4.4.1): 'l'homomorphisme θ_y^♯ : O_y → O_x'", "sharp sign ♯ (crop)", "\\theta_y^\\#", "convention", 9,
    "high", r"\theta_y^\#", r"\theta_y^\sharp", "")
add(P, "proof of (4.4.1): 'est un isomorphisme. On en conclut'", "'isomorphisme' in italics", "isomorphisme (upright)",
    "italics", None, "high", r"est un isomorphisme. On en conclut", r"est un \emph{isomorphisme}. On en conclut", "")
add(P, "proof of (4.4.1): 'de V sur U (I, 6.5.4); en outre'", "bold I", "(I, 6.5.4)", "convention", 2, "high",
    r"(I, 6.5.4)~; en outre", r"(\textbf{I}, 6.5.4)~; en outre", "")
add(P, "bottom of p. 135: 'd'après ce qu'on vient de voir,' / p. 136 'on peut supposer que'", "the sentence runs on to p. 136",
    "blank line before \\oldpage[III]{136}", "other", None, "high", r"vient de voir,¶¶", r"vient de voir,¶",
    "Spurious paragraph break inside a sentence (GLOBAL_ISSUES item 20). Apply together with the p. 136 top-of-page entry.")

# ---------------------------------------------------------------- page 136
P = 136
add(P, "top of p. 136: 'on peut supposer que f^{-1}(U) = V'", "continues the sentence of p. 135",
    "blank line after \\oldpage[III]{136}", "other", None, "high",
    r"\oldpage[III]{136}¶¶on peut", r"\oldpage[III]{136}¶on peut", "Apply together with the p. 135 entry 'vient de voir,'.")
for lab in ["a", "b", "c"]:
    add(P, f"Proposition (4.4.2): label '{lab})'", f"'{lab})' upright (crop)",
        f"\\item[{lab})] inside the italic proposition environment: italic", "convention", 6, "high",
        "\\item[" + lab + ")]", "\\item[\\textup{" + lab + ")}]", "Lettered labels are upright in this statement.")
add(P, "proof of (4.4.2): 'On sait que a) entraîne b)'", "'a)' and 'b)' in italics (crop)", "a), b) upright",
    "italics", None, "high", r"que a) entraîne b)", r"que \emph{a)} entraîne \emph{b)}", "")
add(P, "proof of (4.4.2): '(II, 6.1.2 et 6.1.11)'", "bold II", "(II, 6.1.2 et 6.1.11)", "convention", 2, "high",
    r"(II, 6.1.2 et 6.1.11)", r"(\textbf{II}, 6.1.2 et 6.1.11)", "")
add(P, "proof of (4.4.2): 'f^{-1}(y) → Spec(k(y))'", "k(y) with bold italic k", "\\operatorname{Spec}(k(y))",
    "convention", 1, "high", r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))", "")
add(P, "proof of (4.4.2): '(II, 1.6.2, (iii) et 5.4.2, (iii))'", "bold II", "(II, 1.6.2, (iii) et 5.4.2, (iii))",
    "convention", 2, "high", r"(II, 1.6.2, (iii) et 5.4.2, (iii))", r"(\textbf{II}, 1.6.2, (iii) et 5.4.2, (iii))", "")
add(P, "proof of (4.4.2): 'où A est une k(y)-algèbre finie'", "k(y) with bold italic k", "$k(y)$-algèbre",
    "convention", 1, "high", r"$k(y)$-algèbre", r"$\boldsymbol{k}(y)$-algèbre", "")
add(P, "proof of (4.4.2): 'une k(y)-algèbre finie; donc'", "'finie' in italics (crop)", "finie (upright)", "italics", None,
    "high", r"finie~; donc", r"\emph{finie}~; donc", "")
add(P, "proof of (4.4.2): 'ensemble fini (II, 6.1.7)'", "bold II", "(II, 6.1.7)", "convention", 2, "high",
    r"(II, 6.1.7)", r"(\textbf{II}, 6.1.7)", "")
add(P, "proof of (4.4.2): 'et on voit que b) entraîne c)'", "'b)' and 'c)' in italics (crop)", "b), c) upright",
    "italics", None, "high", r"que b) entraîne c)", r"que \emph{b)} entraîne \emph{c)}", "")
add(P, "proof of (4.4.2): 'préschéma algébrique sur k(y)'", "k(y) with bold italic k", "$k(y)$", "convention", 1, "high",
    r"sur $k(y)$, l'hypothèse", r"sur $\boldsymbol{k}(y)$, l'hypothèse", "")
add(P, "proof of (4.4.2): 'est discret (I, 6.4.4)'", "bold I", "(I, 6.4.4)", "convention", 2, "high",
    r"(I, 6.4.4)", r"(\textbf{I}, 6.4.4)", "")
add(P, "proof of (4.4.2): 'on voit que c) entraîne a).'", "'c)' and 'a)' in italics", "c), a) upright", "italics", None,
    "high", r"que c) entraîne a)", r"que \emph{c)} entraîne \emph{a)}", "")
add(P, "proof of (4.4.3): '(II, 5.3.2 et 5.5.1)'", "bold II", "(II, 5.3.2 et 5.5.1)", "convention", 2, "high",
    r"(II, 5.3.2 et 5.5.1)", r"(\textbf{II}, 5.3.2 et 5.5.1)", "")
add(P, "proof of (4.4.3): 'donc propre (II, 5.5.3)'", "bold II", "(II, 5.5.3)", "convention", 2, "high",
    r"(II, 5.5.3)", r"(\textbf{II}, 5.5.3)", "")
add(P, "Remarque (4.4.4): 'par le sous-préschéma adhérence X̄' de X' dans Y''", "'adhérence' in italics", "adhérence (upright)",
    "italics", None, "high", r"sous-préschéma adhérence", r"sous-préschéma \emph{adhérence}", "Judged as roman remark body.")
add(P, "Remarque (4.4.4): '(I, 9.5.11 et II, 6.1.5, (i) et (ii))': I", "bold I", "(I, 9.5.11", "convention", 2, "high",
    r"(I, 9.5.11", r"(\textbf{I}, 9.5.11", "")
add(P, "Remarque (4.4.4): '(I, 9.5.11 et II, 6.1.5, (i) et (ii))': II", "bold II", "II, 6.1.5, (i) et (ii))", "convention",
    2, "high", r"II, 6.1.5, (i) et (ii))", r"\textbf{II}, 6.1.5, (i) et (ii))", "")
add(P, "Remarque (4.4.4): 'il en est de même de X̄' (I, 9.5.9, (i))' (second of the three X̄')",
    "the bar covers X only and stops before the prime (8x crop); in the first and third X̄' it extends over the prime",
    "$\\overline{X'}$", "misprint_in_print", None, "medium",
    r"même¶de $\overline{X'}$", r"même¶de $\overline{X}'$",
    "The TeX silently gives the bar its intended extent; the fix restores the printed short bar. The closure of X' is "
    "meant, as in the two other occurrences.",
    corrected=r"\overline{X'}")
add(P, "Remarque (4.4.4): '(I, 9.5.9, (i))'", "bold I", "(I, 9.5.9, (i))", "convention", 2, "high",
    r"(I, 9.5.9, (i))", r"(\textbf{I}, 9.5.9, (i))", "")
add(P, "proof of (4.4.5): 'l'injection U → Y est affine (II, 1.6.3)'", "bold II", "(II, 1.6.3)", "convention", 2, "high",
    r"(II, 1.6.3)", r"(\textbf{II}, 1.6.3)", "")
add(P, "proof of (4.4.5): 'morphisme affine V → Y (II, 1.6.2, (ii))'", "bold II", "(II, 1.6.2, (ii))", "convention", 2,
    "high", r"(II, 1.6.2, (ii))", r"(\textbf{II}, 1.6.2, (ii))", "")
add(P, "proof of (4.4.5): '(I, 6.3.5 et II, 5.3.4, (i))': I", "bold I", "(I, 6.3.5", "convention", 2, "high",
    r"(I, 6.3.5", r"(\textbf{I}, 6.3.5", "")
add(P, "proof of (4.4.5): '(I, 6.3.5 et II, 5.3.4, (i))': II", "bold II", "II, 5.3.4, (i))", "convention", 2, "high",
    r"II, 5.3.4, (i))", r"\textbf{II}, 5.3.4, (i))", "")

# ---------------------------------------------------------------- checks
texts = {p: page_text(p) for p in range(131, 137)}
ok = True
spans = {}
for x in F:
    fx = x["fix"]
    if not fx:
        continue
    t = texts[x["page"]]
    c = t.count(fx["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", x["page"], c, repr(fx["old"])[:80])
        continue
    s = t.index(fx["old"])
    spans.setdefault(x["page"], []).append((s, s + len(fx["old"]), fx["old"][:40]))
for p, L in spans.items():
    L.sort()
    for a, b in zip(L, L[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
# apply in any order on copies and compare with reverse order
for p in texts:
    fx = [x["fix"] for x in F if x["page"] == p and x["fix"]]
    for order in (fx, list(reversed(fx))):
        t = texts[p]
        for f in order:
            assert t.count(f["old"]) == 1, (p, f["old"][:60])
            t = t.replace(f["old"], f["new"])
        if order is fx:
            first = t
        else:
            assert t == first, p
    (RUN / "crops_132_136" / f"patched_{p}.tex").write_text(first, encoding="utf-8")
print("all fixes unique, disjoint, order-free" if ok else "PROBLEMS")
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(131, 137):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print(len(F), "findings written to", OUT)
