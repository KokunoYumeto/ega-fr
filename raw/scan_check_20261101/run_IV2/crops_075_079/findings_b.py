"""Findings for EGA IV-2 pp. 78-79 (Python data to keep the LaTeX escapes exact)."""

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 78 ----------------
add(78, "Proposition (4.7.6): 'Soit 0 -> F' -> F -> F'' -> 0 une suite exacte'",
    "the exact sequence in the running text (same line as 'Soit' and 'une suite exacte de O_X-Modules')",
    "displayed with \\[ ... \\]", "other", None, "high",
    "Soit\n\\[\n0\\longrightarrow\\mathscr F'\\longrightarrow\\mathscr F\n\\longrightarrow\\mathscr F''\\longrightarrow0\n\\]\nune suite",
    "Soit\n$0\\longrightarrow\\mathscr F'\\longrightarrow\\mathscr F\n\\longrightarrow\\mathscr F''\\longrightarrow0$\nune suite",
    "Apply before the misprint fix of the first arrow.")
add(78, "Proposition (4.7.6): first arrow of the exact sequence, 0 -> F'",
    "the first arrow is bold (wrong fount; measured ink 245 px against 155 for each of the other arrows, and taller)",
    "plain arrow (silently corrected)", "misprint_in_print", None, "medium",
    "0\\longrightarrow\\mathscr F'\\longrightarrow",
    "0\\boldsymbol{\\longrightarrow}\\mathscr F'\\longrightarrow",
    "Typographical only. Apply after the display-to-inline fix above (its 'old' contains this text).",
    corrected="0\\longrightarrow\\mathscr F'\\longrightarrow")
add(78, "(4.7.6.1)",
    "lambda_x(F) = lambda_x(F') + lambda_x(F'') with no final full stop",
    "final full stop after lambda_x(F'')", "punctuation", None, "high",
    "+\\lambda_x(\\mathscr F'').", "+\\lambda_x(\\mathscr F'')",
    "Checked on a 2x crop.")
add(78, "Proof of (4.7.6): 'et l'on a long(F_x) = long(F'_x) + long(F''_x).'",
    "formula in the running text (end of the line beginning 'si long(F'_x)')",
    "displayed with \\[ ... \\]", "other", None, "high",
    "\\[\n\\operatorname{long}(\\mathscr F_x)\n=\\operatorname{long}(\\mathscr F'_x)+\\operatorname{long}(\\mathscr F''_x).\n\\]",
    "$\\operatorname{long}(\\mathscr F_x)\n=\\operatorname{long}(\\mathscr F'_x)+\\operatorname{long}(\\mathscr F''_x)$.")
add(78, "(4.7.7): 'un O_x-module de longueur finie non nulle sont'",
    "'non nulle' in italics", "plain (env is roman)", "italics", None, "high",
    "finie non nulle sont", "finie \\emph{non nulle} sont")
add(78, "(4.7.7): '(en vertu de (3.1.2)) les points maximaux de Supp(F)'",
    "'les points maximaux de' in italics", "plain", "italics", None, "high",
    "(3.1.2)) les points maximaux de", "(3.1.2)) \\emph{les points maximaux de}")
add(78, "(4.7.7): 'les longueurs géométriques de F et de G en x sont égales'",
    "'égales' in italics", "plain", "italics", None, "high",
    "sont égales,", "sont \\emph{égales},")
add(78, "Proposition (4.7.8): 'Sous les hypothèses de (4.7.5), soit x'",
    "(4.7.5) upright", "typeset italic", "convention", 6, "high",
    "de (4.7.5), soit $x$", "de \\textup{(4.7.5)}, soit $x$")
add(78, "Proof of (4.7.8), the display",
    "long_{O_{x'}}(F'_{x'}) = long_{O_x}(F_x) . long_{B_q}(B_q/pB_q): the first two lengths are indexed by O_{x'} and O_x",
    "\\operatorname{long}_{B_q}(F'_{x'}) = \\operatorname{long}_{A_p}(F_x) ...", "formula", None, "high",
    "\\operatorname{long}_{B_{\\mathfrak q}}(\\mathscr F'_{x'})\n=\\operatorname{long}_{A_{\\mathfrak p}}(\\mathscr F_x)",
    "\\operatorname{long}_{\\mathcal O_{x'}}(\\mathscr F'_{x'})\n=\\operatorname{long}_{\\mathcal O_x}(\\mathscr F_x)",
    "Checked on a 2x crop; the third factor keeps B_q.")
add(78, "Proof of (4.7.8), the display: between long_{O_x}(F_x) and long_{B_q}(...)",
    "baseline period (measured: same height as the final full stop)", "no sign between the two factors",
    "symbol", None, "high",
    "(\\mathscr F_x)\n \\operatorname{long}_{B_{\\mathfrak q}}",
    "(\\mathscr F_x)\n .\\operatorname{long}_{B_{\\mathfrak q}}")
add(78, "Proof of (4.7.8): 'Mais comme k(x) = A_p/pA_p'",
    "bold italic k in k(x)", "plain k(x)", "convention", 1, "high",
    "$k(x)=A_{\\mathfrak p}", "$\\boldsymbol{k}(x)=A_{\\mathfrak p}")
add(78, "Proof of (4.7.8): 'l'anneau total des fractions de k(x) (x)_k k''",
    "bold italic k in k(x)", "plain k(x)", "convention", 1, "high",
    "$k(x)\\otimes_k k'$", "$\\boldsymbol{k}(x)\\otimes_k k'$")
add(78, "Proof of (4.7.8): 'est par définition mu_i(k(x)|k)'",
    "bold italic k in k(x)", "plain k(x)", "convention", 1, "high",
    "$\\mu_i(k(x)\\mid k)$", "$\\mu_i(\\boldsymbol{k}(x)\\mid k)$")
add(78, "Paragraph after the proof of (4.7.8): 'est la multiplicité radicielle du cycle premier maximal {x}-bar associé à F'",
    "'multiplicité radicielle du cycle premier maximal' in italics", "plain", "italics", None, "high",
    "la multiplicité radicielle du cycle premier maximal",
    "la \\emph{multiplicité radicielle du cycle premier maximal}")
add(78, "Corollaire (4.7.9): 'Sous les hypothèses de (4.7.5), soient k''",
    "(4.7.5) upright", "typeset italic", "convention", 6, "high",
    "de (4.7.5), soient $k'$", "de \\textup{(4.7.5)}, soient $k'$")
add(78, "Corollaire (4.7.9): 'qui domine Z (4.2.7). Alors'",
    "(4.2.7) upright", "typeset italic", "convention", 6, "high",
    "(4.2.7). Alors", "\\textup{(4.2.7)}. Alors")

# ---------------- page 79 ----------------
add(79, "Proposition (4.7.10): 'géométriquement réduit au point x (4.6.22)'",
    "(4.6.22) upright", "typeset italic", "convention", 6, "high",
    "(4.6.22)", "\\textup{(4.6.22)}")
add(79, "Proposition (4.7.10): 'Pour que F soit géométriquement réduit au point x (4.6.22)'",
    "the x after 'au point' is bold italic (wrong fount; measured ink 189 px against 150-151 for the x of 'contiennent x.' and 'que x n'appartienne'; visibly heavier in a 3x side-by-side crop)",
    "plain $x$ (silently corrected)", "misprint_in_print", None, "medium",
    "soit géométriquement réduit au point $x$",
    "soit géométriquement réduit au point $\\boldsymbol{x}$",
    "Wrong-fount letter, kept in the diplomatic text (GLOBAL_ISSUES item 29). Does not overlap the (4.6.22) fix.",
    corrected="soit géométriquement réduit au point $x$")
add(79, "Proof of (4.7.10), second paragraph: 'que si, pour une extension finie k' de k'",
    "'une' in italics", "plain", "italics", None, "high",
    "pour une extension finie", "pour \\emph{une} extension finie")
add(79, "Proposition (4.7.11): 'géométriquement réduit (resp. géométriquement ponctuellement intègre) au point x'",
    "'(resp.' and the closing parenthesis upright; the words italic", "typeset italic",
    "convention", 6, "high",
    "réduit (resp. géométriquement ponctuellement intègre) au point\n$x$,",
    "réduit \\textup{(resp.} géométriquement ponctuellement intègre\\textup{)} au point\n$x$,")
add(79, "Proposition (4.7.11): 'géométriquement réduit (resp. géométriquement ponctuellement intègre) au point x''",
    "'(resp.' and the closing parenthesis upright; the words italic", "typeset italic",
    "convention", 6, "high",
    "réduit (resp.\ngéométriquement ponctuellement intègre) au point $x'$.",
    "réduit \\textup{(resp.}\ngéométriquement ponctuellement intègre\\textup{)} au point $x'$.")
add(79, "End of p. 79: the page break falls inside the sentence of Définition (4.7.12) ('On appelle multiplicité / totale de x')",
    "no paragraph break: the sentence continues at the top of p. 80",
    "blank line before \\oldpage[IV-2]{80} (paragraph break)", "other", None, "high",
    "\\emph{multiplicité}\n\n", "\\emph{multiplicité}\n",
    "GLOBAL_ISSUES item 20; the blank line is the last line of the p. 79 segment. Apply together with the p. 80 fix removing the blank line after \\oldpage[IV-2]{80}, and before the next fix on this page (whose 'old' it leaves intact).")
add(79, "Définition (4.7.12), last line of p. 79: 'On appelle multiplicité'",
    "'multiplicité' italic like the rest of the definition (no change of face; 2x crop)",
    "\\emph{multiplicité} inside the italic definition (typeset upright)", "convention", 6, "high",
    "On appelle \\emph{multiplicité}", "On appelle multiplicité",
    "Only the p. 79 word; the continuation \\emph{totale de $x$} at the top of p. 80 is for the p. 80 check. Apply after the blank-line fix above.")
