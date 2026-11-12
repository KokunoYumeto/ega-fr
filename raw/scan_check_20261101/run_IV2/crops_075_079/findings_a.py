"""Findings for EGA IV-2 pp. 75-77 (written as Python data to keep the LaTeX escapes exact)."""

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 75 ----------------
add(75, "Paragraph after (4.6.22): 'est géométriquement réduit au point x; il en résulte'",
    "'géométriquement réduit au point x' in italics (emphasis)", "plain roman text",
    "italics", None, "high",
    r"est géométriquement réduit au point $x$; il en",
    r"est \emph{géométriquement réduit au point} $x$; il en",
    "Text outside any statement environment (ordinary roman paragraph).")
add(75, "Same paragraph: 'tel que F|U soit géométriquement réduit (4.6.11)'",
    "'géométriquement réduit' in italics", "plain roman text",
    "italics", None, "high",
    r"soit géométriquement réduit (4.6.11)",
    r"soit \emph{géométriquement réduit} (4.6.11)")
add(75, "Same paragraph, last sentence: 'le sous-préschéma Y est géométriquement ponctuellement intègre au point x.'",
    "'géométriquement ponctuellement intègre au point x' in italics", "plain roman text",
    "italics", None, "high",
    "$Y$ est géométriquement\nponctuellement intègre au point $x$.",
    "$Y$ est \\emph{géométriquement\nponctuellement intègre au point} $x$.",
    "The earlier occurrence of the same words (after 'dire que F est') is roman in the print and stays plain.")
add(75, "Heading 4.7",
    "'4.7. Multiplicités dans la décomposition primaire sur un préschéma algébrique.' (final full stop)",
    "\\subsection{... préschéma algébrique} (no full stop)",
    "punctuation", None, "high",
    "préschéma\nalgébrique}",
    "préschéma\nalgébrique.}",
    "GLOBAL_ISSUES items 43/58 (subsection titles lack the printed full stop); same page fix as other checkers.")
add(75, "(4.7.1.1)",
    "long_B(M_(B)) = long_A(M) . long_B(B/mB): the product dot is a baseline period (measured: same height as the final full stop)",
    "\\operatorname{long}_A(M)\\cdot\\operatorname{long}_B(...)", "symbol", None, "high",
    r"\operatorname{long}_A(M)\cdot\operatorname{long}_B",
    r"\operatorname{long}_A(M).\operatorname{long}_B",
    "Same treatment as the p.1 baseline periods (GLOBAL_ISSUES item 65).")
add(75, "(4.7.2.1), left side",
    "long_{B_q}(M_(B))_q : one pair of parentheses, the subscript q after it",
    "\\operatorname{long}_{B_q}((M_{(B)})_q): an extra outer pair of parentheses",
    "formula", None, "high",
    r"\operatorname{long}_{B_{\mathfrak q}}((M_{(B)})_{\mathfrak q})",
    r"\operatorname{long}_{B_{\mathfrak q}}(M_{(B)})_{\mathfrak q}",
    "Checked on a 2x crop.")
add(75, "(4.7.2.1), right side",
    "(long_{A_p}(M_p))(long_{B_q}(B_q/pB_q)). : each factor in parentheses",
    "long_{A_p}(M_p) long_{B_q}(B_q/pB_q). without the parentheses",
    "formula", None, "high",
    "=\\operatorname{long}_{A_{\\mathfrak p}}(M_{\\mathfrak p})\n \\operatorname{long}_{B_{\\mathfrak q}}\n (B_{\\mathfrak q}/\\mathfrak pB_{\\mathfrak q}).",
    "=(\\operatorname{long}_{A_{\\mathfrak p}}(M_{\\mathfrak p}))\n (\\operatorname{long}_{B_{\\mathfrak q}}\n (B_{\\mathfrak q}/\\mathfrak pB_{\\mathfrak q})).",
    "Checked on a 2x crop.")
add(75, "Proof of (4.7.2): 'A_p-module plat (0_I, 6.3.2)'",
    "(0_I, 6.3.2) with a bold 0", "$(0_{\\mathrm I},6.3.2)$, plain 0", "convention", 2, "high",
    r"$(0_{\mathrm I},6.3.2)$", r"$(\mathbf{0}_{\mathrm I},6.3.2)$")
add(75, "Proof of (4.7.2): 'fidèlement plat (0_I, 6.6.2)'",
    "(0_I, 6.6.2) with a bold 0", "$(0_{\\mathrm I},6.6.2)$, plain 0", "convention", 2, "high",
    r"$(0_{\mathrm I},6.6.2)$", r"$(\mathbf{0}_{\mathrm I},6.6.2)$")
add(75, "Proposition (4.7.3) (i)",
    "label (i) printed upright", "\\item[(i)] inside the italic statement (label typeset italic)",
    "convention", 6, "high",
    r"\item[(i)] On suppose", r"\item[\textup{(i)}] On suppose")
add(75, "Proposition (4.7.3) (i): '(ce qui a lieu si X est localement de type fini sur k, ou si k' est une extension de type fini de k)'",
    "parenthesis roman; only 'localement de type fini sur k' and 'de type fini' italic",
    "whole parenthesis italic (no change of face)", "convention", 6, "high",
    "(ce qui a lieu si\n$X$ est localement de type fini sur $k$, ou si $k'$ est une extension de type\nfini de $k$)",
    "\\textup{(ce qui a lieu si\n$X$ est \\emph{localement de type fini sur} $k$, ou si $k'$ est une extension \\emph{de type\nfini} de $k$)}")
add(75, "(4.7.3.1)",
    "long(O_{x''_b}) = long(O_{x'_a}) . long(O_{Z'',x''_b}): baseline period between the two factors (measured)",
    "no sign between the two factors", "symbol", None, "high",
    "(\\mathcal O_{x'_\\alpha})\n \\operatorname{long}(\\mathcal O_{Z'',x''_\\beta})",
    "(\\mathcal O_{x'_\\alpha})\n .\\operatorname{long}(\\mathcal O_{Z'',x''_\\beta})",
    "Same baseline period as in (4.7.1.1).")
add(75, "Proposition (4.7.3) (i): 'si k'' est une extension séparable de k''",
    "'séparable' set roman inside the italic statement", "plain 'séparable' (typeset italic)",
    "convention", 6, "high",
    r"extension séparable de $k'$", r"extension \emph{séparable} de $k'$")
add(75, "Proposition (4.7.3) (i), last formula: 'on a long(O_{x''_b}) = long(O_{x'_a}).'",
    "formula in the running text (same line as 'soit localement noethérien, on a')",
    "displayed with \\[ ... \\]", "other", None, "high",
    "\\[\n\\operatorname{long}(\\mathcal O_{x''_\\beta})\n=\\operatorname{long}(\\mathcal O_{x'_\\alpha}).\n\\]",
    "$\\operatorname{long}(\\mathcal O_{x''_\\beta})\n=\\operatorname{long}(\\mathcal O_{x'_\\alpha})$.")

# ---------------- page 76 ----------------
add(76, "Proposition (4.7.3) (ii)",
    "label (ii) printed upright", "\\item[(ii)] inside the italic statement (label typeset italic)",
    "convention", 6, "high",
    r"\item[(ii)] Si $X$", r"\item[\textup{(ii)}] Si $X$")
add(76, "Proposition (4.7.3) (iii)",
    "label (iii) printed upright", "\\item[(iii)] inside the italic statement (label typeset italic)",
    "convention", 6, "high",
    r"\item[(iii)] On suppose", r"\item[\textup{(iii)}] On suppose")
add(76, "Proposition (4.7.3) (iii): '(et non de l'extension parfaite particulière k' de k considérée)'",
    "the whole parenthesis roman", "typeset italic (no change of face)", "convention", 6, "high",
    "(et non de l'extension parfaite particulière $k'$\nde $k$ considérée)",
    "\\textup{(et non de l'extension parfaite particulière $k'$\nde $k$ considérée)}")
add(76, "Proposition (4.7.3) (iii), last formula: 'on ait long(O_{x'_a}) = long(O_{x_1}) pour tout a.'",
    "formula in the running text (starts the last line of the statement, flush left), followed by italic 'pour tout a.'",
    "displayed with \\[ ... \\quad\\text{pour tout }\\alpha. \\]", "other", None, "high",
    "\\[\n\\operatorname{long}(\\mathcal O_{x'_\\alpha})\n=\\operatorname{long}(\\mathcal O_{x_1})\n\\quad\\text{pour tout }\\alpha.\n\\]",
    "$\\operatorname{long}(\\mathcal O_{x'_\\alpha})\n=\\operatorname{long}(\\mathcal O_{x_1})$ pour tout $\\alpha$.")
add(76, "Proof of (4.7.3) (i): 'est un anneau artinien, isomorphe à'",
    "'artinien' in italics", "plain", "italics", None, "high",
    r"un anneau artinien, isomorphe", r"un anneau \emph{artinien}, isomorphe")
add(76, "Proof of (4.7.3) (i): 'on a O_{Z'',x''_b} = (B/pB)_{q'} = B_q/pB_q, d'où (4.7.3.1)'",
    "formula in the running text (starts a line, flush left, followed by 'd'où (4.7.3.1).' on the same line)",
    "displayed with \\[ ... \\]", "other", None, "high",
    "\\[\n\\mathcal O_{Z'',x''_\\beta}\n=(B/\\mathfrak pB)_{\\mathfrak q'}\n=B_{\\mathfrak q}/\\mathfrak pB_{\\mathfrak q},\n\\]",
    "$\\mathcal O_{Z'',x''_\\beta}\n=(B/\\mathfrak pB)_{\\mathfrak q'}\n=B_{\\mathfrak q}/\\mathfrak pB_{\\mathfrak q}$,")
add(76, "Proof of (4.7.3) (ii): 'supposer que k' est une extension finie de k'",
    "'finie' in italics", "plain", "italics", None, "high",
    r"extension finie de $k$. Il y a", r"extension \emph{finie} de $k$. Il y a")
add(76, "Proof of (4.7.3) (ii): 'Mais k'' est une extension séparable d'une extension radicielle finie k_1'",
    "'séparable' in italics", "plain", "italics", None, "high",
    r"séparable d'une extension", r"\emph{séparable} d'une extension")
add(76, "Proof of (4.7.3) (ii): 'lorsque k'=k_1 est en outre radicielle.'",
    "'radicielle' in italics", "plain", "italics", None, "high",
    r"outre radicielle.", r"outre \emph{radicielle}.")
add(76, "Proof of (4.7.3) (ii), second paragraph: 'lorsque k' est algébriquement clos.'",
    "'algébriquement clos' in italics", "plain", "italics", None, "high",
    r"est algébriquement clos.", r"est \emph{algébriquement clos}.")
add(76, "Proof of (4.7.3) (ii), second paragraph: 'une extension séparable de la clôture algébrique'",
    "'séparable' in italics", "plain", "italics", None, "high",
    r"séparable de la clôture", r"\emph{séparable} de la clôture")
add(76, "End of p. 76: the page break falls inside the sentence 'une extension radicielle / finie k_1 de k'",
    "no paragraph break: p. 77 begins flush left with 'finie k_1 de k telle que'",
    "blank line before \\oldpage[IV-2]{77} (paragraph break)", "other", None, "high",
    "une extension radicielle\n\n", "une extension radicielle\n",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20); the blank line is the last line of the p. 76 segment. Apply together with the p. 77 fix that removes the blank line after the marker.")

# ---------------- page 77 ----------------
add(77, "Top of p. 77: 'finie k_1 de k telle que' continues the sentence of p. 76",
    "no indentation: p. 77 begins flush left inside the sentence",
    "blank line after \\oldpage[IV-2]{77} (paragraph break)", "other", None, "high",
    "\\oldpage[IV-2]{77}\n\nfinie", "\\oldpage[IV-2]{77}\nfinie",
    "Apply together with the p. 76 fix that removes the blank line before the marker (GLOBAL_ISSUES item 20).")
add(77, "Proof of (4.7.3) (iii): 'pour k' parfaite, ne dépend pas du choix de k''",
    "'parfaite' in italics", "plain", "italics", None, "high",
    r"$k'$ parfaite, ne dépend", r"$k'$ \emph{parfaite}, ne dépend")
add(77, "Proof of (4.7.3) (iii): 'puisque k'' est séparable sur k''",
    "'séparable' in italics", "plain", "italics", None, "high",
    r"séparable sur $k'$.", r"\emph{séparable} sur $k'$.")
add(77, "Paragraph after (4.7.4): 'ces nombres sont tous trois finis dans ce cas'",
    "'finis' in italics", "plain", "italics", None, "high",
    r"trois finis dans ce cas", r"trois \emph{finis} dans ce cas")
add(77, "Definition (4.7.5): 'ou multiplicité radicielle de x pour F le produit'",
    "only 'multiplicité radicielle' roman; 'de x pour F' italic like the statement",
    "\\emph{multiplicité radicielle de $x$ pour $\\mathscr F$}: 'de' and 'pour' typeset upright",
    "convention", 6, "high",
    r"\emph{multiplicité radicielle de $x$ pour $\mathscr F$}",
    r"\emph{multiplicité radicielle} de $x$ pour $\mathscr F$")
add(77, "Definition (4.7.5), the formula for lambda_x(F)",
    "in the running text: 'F le produit lambda_x(F) = (long_{O_x}(F_x)) mu_i(k(x)|k), où mu_i(k(x)|k) désigne ...'",
    "displayed with \\[ ... \\]", "other", None, "high",
    "\\[\n\\lambda_x(\\mathscr F)\n=\\operatorname{long}_{\\mathcal O_x}(\\mathscr F_x)\\mu_i(k(x)\\mid k),\n\\]",
    "$\\lambda_x(\\mathscr F)\n=\\operatorname{long}_{\\mathcal O_x}(\\mathscr F_x)\\mu_i(k(x)\\mid k)$,",
    "Apply first of the four (4.7.5) formula fixes (then parentheses, k(x), misprint).")
add(77, "Definition (4.7.5), the formula for lambda_x(F)",
    "(long_{O_x}(F_x)) mu_i(...): the length factor in parentheses",
    "\\operatorname{long}_{\\mathcal O_x}(\\mathscr F_x)\\mu_i(...) without the parentheses",
    "formula", None, "high",
    r"=\operatorname{long}_{\mathcal O_x}(\mathscr F_x)\mu_i",
    r"=(\operatorname{long}_{\mathcal O_x}(\mathscr F_x))\mu_i",
    "Apply after the display-to-inline fix and before the misprint fix.")
add(77, "Definition (4.7.5), the formula: mu_i(k(x)|k)",
    "bold italic k in k(x)", "plain k(x)", "convention", 1, "high",
    r")\mu_i(k(x)", r")\mu_i(\boldsymbol{k}(x)")
add(77, "Definition (4.7.5): 'où mu_i(k(x)|k) désigne'",
    "bold italic k in k(x)", "plain k(x)", "convention", 1, "high",
    r"où $\mu_i(k(x)\mid k)$", r"où $\mu_i(\boldsymbol{k}(x)\mid k)$")
add(77, "Definition (4.7.5): 'la multiplicité radicielle de k(x) sur k'",
    "bold italic k in k(x)", "plain k(x)", "convention", 1, "high",
    r"de $k(x)$ sur $k$.", r"de $\boldsymbol{k}(x)$ sur $k$.")
add(77, "Definition (4.7.5), the formula: subscript of lambda_x",
    "the subscript x of lambda_x is bold italic (wrong fount; measured ink 177 px against 108-113 for the normal subscript x of F_x, O_x in the same definition and of long(O_x)=1 below); the x inside k(x) is normal",
    "plain x (silently corrected)", "misprint_in_print", None, "medium",
    "\\lambda_x(", "\\lambda_{\\boldsymbol{x}}(",
    "Wrong-fount letters are kept in the diplomatic text (GLOBAL_ISSUES item 29). Apply after the display-to-inline fix above (its 'old' contains this text).",
    corrected="\\lambda_x(")
add(77, "Definition (4.7.5), the formula: subscripts of long_{O_x} and F_x",
    "the x under long_{O_x} and the subscript x of F_x are bold italic (wrong fount; measured ink 131 and 187 px against 108-113 for normal subscript x)",
    "plain x (silently corrected)", "misprint_in_print", None, "medium",
    "_{\\mathcal O_x}(\\mathscr F_x)", "_{\\mathcal O_{\\boldsymbol{x}}}(\\mathscr F_{\\boldsymbol{x}})",
    "Same wrong fount as the lambda_x subscript. Apply after the display-to-inline and parentheses fixes above (their 'old' contains this text).",
    corrected="_{\\mathcal O_x}(\\mathscr F_x)")
add(77, "Paragraph after (4.7.5): 'Lorsque X est intègre, et x le point générique'",
    "'intègre' in italics", "plain", "italics", None, "high",
    r"$X$ est intègre, et", r"$X$ est \emph{intègre}, et")
