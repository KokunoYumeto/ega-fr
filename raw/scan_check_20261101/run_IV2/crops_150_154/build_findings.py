# Builds findings_150_154.json; "¶" in the strings below stands for a line break.
import json
import sys

RUN = "user/Documents/ega_scan_check_20261101/run_IV2"
OUT = RUN + "/findings_150_154.json"


def nl(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    item = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": nl(old), "new": nl(new)},
    }
    if kind == "misprint_in_print":
        item["corrected"] = nl(corrected)
    item["note"] = note
    F.append(item)


BP = r"\boldsymbol{P}"
BM = r"\boldsymbol{M}"

# ---------------------------------------------------------------- page 150
add(150, "top of the page (start of the segment)", "page begins mid-sentence: 'pour tout λ; en effet f_λ ...' (no paragraph break)",
    "blank line after \\oldpage[IV-2]{150}", "other", None, "high",
    r"\oldpage[IV-2]{150}¶¶", r"\oldpage[IV-2]{150}¶",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 149 segment edit "
    "'pour tout $\\lambda$.\\n\\n' -> 'pour tout $\\lambda$;\\n' just before the marker (print p. 149 ends 'pour tout λ;'), "
    "which lies outside pp. 150-154, and with the next entry.")
add(150, "l. 1", "en effet f_λ est bijectif", "En effet $f_\\lambda$ est bijectif", "word", None, "high",
    r"En effet $f_\lambda$", r"en effet $f_\lambda$",
    "The printed sentence runs on from p. 149 ('... pour tout λ; en effet ...'); the TeX ends p. 149 with a full stop "
    "(p. 149 segment) and capitalises here. Apply with the previous entry.")
add(150, "l. 1", "(I, 3.5.2, 3.5.7 et 3.5.8)", "(I, 3.5.2, 3.5.7 et 3.5.8)", "convention", 2, "high",
    r"(I, 3.5.2, 3.5.7 et 3.5.8)", r"(\textbf{I}, 3.5.2, 3.5.7 et 3.5.8)")
add(150, "l. 2", "(II, 6.1.10)", "(II, 6.1.10)", "convention", 2, "high",
    r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)")
add(150, "ll. 2-3", "l'hypothèse b)) with italic b)", "l'hypothèse b))", "italics", None, "high",
    r"l'hypothèse b))", r"l'hypothèse \emph{b)})", "Enlarged crop: the label b) is italic, the closing parenthesis upright.")
add(150, "l. 3", "que b) entraîne e) (b), e) italic)", "que b) entraîne e)", "italics", None, "high",
    r"que b) entraîne e) lorsque", r"que \emph{b)} entraîne \emph{e)} lorsque")
add(150, "l. 3", "P(Z, z) with bold italic P", "$P(Z,z)$", "font", None, "high",
    r"$P(Z,z)$ est la propriété $(R_n)$", r"$" + BP + r"(Z,z)$ est la propriété $(R_n)$",
    "Bold italic property letter; not convention 10 (the TeX has plain P).")
add(150, "l. 4", "Le cas où P(Z, z) (bold italic P)", "Le cas où $P(Z,z)$", "font", None, "high",
    r"Le cas où $P(Z,z)$", r"Le cas où $" + BP + r"(Z,z)$")
add(150, "l. 6", "(5.8.6), b) entraîne encore e) (b), e) italic)", "(5.8.6), b) entraîne encore e)", "italics", None, "high",
    r"(5.8.6), b) entraîne encore e)", r"(5.8.6), \emph{b)} entraîne encore \emph{e)}")
add(150, "l. 6", "lorsque P(Z, z) est la propriété d'être normal (bold italic P)", "$P(Z,z)$", "font", None, "high",
    r"$P(Z,z)$ est la propriété d'être normal", r"$" + BP + r"(Z,z)$ est la propriété d'être normal")
add(150, "Corollaire (6.7.8), l. 2", "on désigne par P(X, x) (bold italic P)", "$P(X,x)$", "font", None, "high",
    r"désigne par $P(X,x)$", r"désigne par $" + BP + r"(X,x)$")
for lab, rest in [("(i)", r" $\operatorname{coprof}"), ("(ii)", r" $\mathcal O_x$"), ("(iii)", ""), ("(iv)", ""),
                  ("(v)", ""), ("(vi)", ""), ("(vii)", "")]:
    add(150, "Corollaire (6.7.8), label " + lab, lab + " upright", "\\item[" + lab + "] in the italic statement", "convention", 6, "high",
        "\\item[" + lab + "]" + rest, "\\item[\\textup{" + lab + "}]" + rest,
        "Item labels are printed upright inside the italic statement (GLOBAL_ISSUES 16).")
add(150, "Corollaire (6.7.8) (ii)", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
    r"anneau de Cohen--Macaulay.", r"anneau de Cohen-Macaulay.",
    "Enlarged crop: the same short hyphen as in 'k-préschéma'. ega4-2-fr.tex has 42 'Cohen--Macaulay' against 57 'Cohen-Macaulay'.")
add(150, "Corollaire (6.7.8) (vii)", "(i.e. séparable) with roman 'i.e.'", "(i.e. séparable) all italic", "convention", 6, "high",
    r"(i.e. séparable)", r"(\textup{i.e.} séparable)", "Enlarged crop: 'i.e.' upright, 'séparable' italic.")
add(150, "Corollaire (6.7.8), after the list", "'Soit k' une extension de k' starts a new indented paragraph",
    "\\end{enumerate} followed directly by 'Soit' (unindented)", "other", None, "medium",
    r"\end{enumerate}¶Soit $k'$", r"\end{enumerate}¶¶Soit $k'$",
    "Paragraph after the list, indented as printed (same form as the p. 136 fix).")
add(150, "Corollaire (6.7.8), last sentence", "pour que P(X, x) ... que P(X', x') (bold italic P, twice)", "$P(X,x)$, $P(X',x')$", "font", None, "high",
    r"pour que $P(X,x)$ soit vraie, il faut¶et il suffit que $P(X',x')$ le soit",
    r"pour que $" + BP + r"(X,x)$ soit vraie, il faut¶et il suffit que $" + BP + r"(X',x')$ le soit", "Two occurrences in one edit.")
add(150, "proof of (6.7.8), l. 3", "critères a) et c), ... de c) et d) (italic labels)", "a) et c) ... c) et d)", "italics", None, "high",
    r"critères a) et c), et de l'équivalence de c) et d) lorsque",
    r"critères \emph{a)} et \emph{c)}, et de l'équivalence de \emph{c)} et \emph{d)} lorsque")
add(150, "proof of (6.7.8), l. 6", "qu'un seul point (un seul italic)", "qu'un seul point", "italics", None, "high",
    r"qu'un seul point", r"qu'\emph{un seul} point")
add(150, "proof of (6.7.8), l. 7", "(I, 3.5.7 et 3.5.8)", "(I, 3.5.7 et 3.5.8)", "convention", 2, "high",
    r"(I, 3.5.7 et 3.5.8)", r"(\textbf{I}, 3.5.7 et 3.5.8)")
add(150, "proof of (6.7.8), l. 8", "P(X', x'), P(X_0, x_0) (bold italic P)", "$P(X',x')$, $P(X_0,x_0)$", "font", None, "high",
    r"si $P(X',x')$ est vraie, il en est de même de $P(X_0,x_0)$",
    r"si $" + BP + r"(X',x')$ est vraie, il en est de même de $" + BP + r"(X_0,x_0)$", "Two occurrences in one edit.")
add(150, "proof of (6.7.8), l. 9", "(6.7.7, c) et d)) (c), d) italic)", "(6.7.7, c) et d))", "italics", None, "high",
    r"(6.7.7, c) et d))", r"(6.7.7, \emph{c)} et \emph{d)})")
add(150, "proof of (6.7.8), l. 11", "Q(k'') with bold italic Q", "$Q(k'')$", "font", None, "high",
    r"$Q(k'')$", r"$\boldsymbol{Q}(k'')$")
add(150, "proof of (6.7.8), last line", "donc P(X, x) (bold italic P)", "$P(X,x)$", "font", None, "high",
    r"donc $P(X,x)$ est vraie", r"donc $" + BP + r"(X,x)$ est vraie")
add(150, "proof of (6.7.8), last line", "(6.7.7, b)) (b) italic)", "(6.7.7, b))", "italics", None, "high",
    r"(6.7.7, b))", r"(6.7.7, \emph{b)})")
add(150, "heading 6.8", "6.8. Morphismes réguliers, normaux, réduits, lisses.", "title without the full stop", "punctuation", None, "high",
    r"\subsection{Morphismes réguliers, normaux, réduits, lisses}", r"\subsection{Morphismes réguliers, normaux, réduits, lisses.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(150, "Définition (6.8.1), label (i)", "(i) upright", "\\item[(i)] in the italic statement", "convention", 6, "high",
    r"\item[(i)] de coprofondeur", r"\item[\textup{(i)}] de coprofondeur", "GLOBAL_ISSUES 16.")
add(150, "Définition (6.8.1), label (ii)", "(ii) upright", "\\item[(ii)] in the italic statement", "convention", 6, "high",
    r"\item[(ii)] de Cohen", r"\item[\textup{(ii)}] de Cohen", "GLOBAL_ISSUES 16. Independent of the next entry (the shared word is unchanged).")
add(150, "Définition (6.8.1) (ii)", "de Cohen-Macaulay (hyphen)", "Cohen--Macaulay", "punctuation", None, "high",
    r"Cohen--Macaulay au point $x$;", r"Cohen-Macaulay au point $x$;")

# ---------------------------------------------------------------- page 151
for lab, rest in [("(iii)", r" $(S_n)$"), ("(iv)", ""), ("(v)", ""), ("(vi)", ""), ("(vii)", "")]:
    add(151, "Définition (6.8.1), label " + lab, lab + " upright", "\\item[" + lab + "] in the italic statement", "convention", 6, "high",
        "\\item[" + lab + "]" + rest, "\\item[\\textup{" + lab + "}]" + rest, "GLOBAL_ISSUES 16.")
add(151, "Définition (6.8.1), after the list", "P(f^{-1}(f(x)), x) with bold italic P", "$P(f^{-1}(f(x)),x)$", "font", None, "high",
    r"$P(f^{-1}(f(x)),x)$", r"$" + BP + r"(f^{-1}(f(x)),x)$")
add(151, "Définition (6.8.1), after the list", "(notation de (6.7.8)) with upright reference", "(notation de (6.7.8)) all italic", "convention", 6, "high",
    r"(notation de (6.7.8))", r"(notation de \textup{(6.7.8)})", "Enlarged crop: 'notation de' italic, '(6.7.8)' upright.")
add(151, "Définition (6.8.1), last sentence", "de Cohen-Macaulay (hyphen)", "Cohen--Macaulay", "punctuation", None, "high",
    r"de¶Cohen--Macaulay", r"de¶Cohen-Macaulay")
add(151, "Proposition (6.8.2), l. 1", "localement noethériens f : X→Y (no comma)", "localement noethériens, $f:X\\to Y$",
    "misprint_in_print", None, "high",
    r"noethériens, $f:X\to Y$ un", r"noethériens $f:X\to Y$ un",
    "Enlarged crop: no comma after 'noethériens' (compare (6.8.6) and (6.8.7), which have it). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"noethériens, $f:X\to Y$ un")
add(151, "Proposition (6.8.2), l. 2", "Désignons par M(f, x) (bold italic M)", "$M(f,x)$", "font", None, "high",
    r"Désignons par $M(f,x)$", r"Désignons par $" + BM + r"(f,x)$", "Bold italic property letter M.")
add(151, "Proposition (6.8.2), ll. 2-3", "(i) à (vii) de la définition (6.8.1): labels and reference upright", "all italic", "convention", 6, "high",
    r"(i) à (vii) de la définition (6.8.1)", r"\textup{(i)} à \textup{(vii)} de la définition \textup{(6.8.1)}",
    "Enlarged crop: '(i)', '(vii)', '(6.8.1)' upright; 'à', 'de la définition' italic.")
add(151, "Proposition (6.8.2), last line", "la propriété M(f, x) entraîne M(f', x') (bold italic M)", "$M(f,x)$, $M(f',x')$", "font", None, "high",
    r"la propriété $M(f,x)$ entraîne $M(f',x')$", r"la propriété $" + BM + r"(f,x)$ entraîne $" + BM + r"(f',x')$", "Two occurrences in one edit.")
add(151, "proof of (6.8.2), l. 1", "(I, 3.6.4)", "(I, 3.6.4)", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
add(151, "proof of (6.8.2), ll. 1-2", "formula f'^{-1}(y')=... in the running text", "displayed with \\[ \\]", "formula", None, "high",
    r"on a¶\[¶f'^{-1}(y')=", r"on a¶$f'^{-1}(y')=",
    "Part 1 of 2 (opening of the display); apply together with part 2 (next entry). Independent of the convention-1 entries.")
add(151, "proof of (6.8.2), l. 2", "...k(y'); comme ou bien", "...k(y').\\n\\]\\nComme ou bien", "formula", None, "high",
    r"(y').¶\]¶Comme ou bien", r"(y')$; comme ou bien",
    "Part 2 of 2: closes the inline formula; the print continues the sentence with a semicolon and lower-case 'comme'.")
add(151, "proof of (6.8.2), l. 2", "⊗ with subscript k(y) in bold upright k", "\\otimes_{k(y)}", "convention", 1, "high",
    r"\otimes_{k(y)}", r"\otimes_{\mathbf{k}(y)}", "Bold upright k at subscript size (GLOBAL_ISSUES 48), as on p. 100.")
add(151, "proof of (6.8.2), l. 2", "k(y') bold italic k", "k(y')", "convention", 1, "high",
    r"}k(y')", r"}\boldsymbol{k}(y')")
add(151, "proof of (6.8.2), l. 2", "sur k(y), ou bien (bold italic k)", "$k(y)$", "convention", 1, "high",
    r"sur $k(y)$, ou bien", r"sur $\boldsymbol{k}(y)$, ou bien")
add(151, "proof of (6.8.2), l. 3", "ou bien k(y') (bold italic k)", "$k(y')$", "convention", 1, "high",
    r"$k(y')$ est de type fini", r"$\boldsymbol{k}(y')$ est de type fini")
add(151, "proof of (6.8.2), l. 3", "sur k(y) (I, 6.4.11) (bold italic k)", "$k(y)$", "convention", 1, "high",
    r"sur $k(y)$ (", r"sur $\boldsymbol{k}(y)$ (")
add(151, "proof of (6.8.2), l. 3", "(I, 6.4.11)", "(I, 6.4.11)", "convention", 2, "high",
    r"(I, 6.4.11)", r"(\textbf{I}, 6.4.11)")
add(151, "proof of (6.8.2), l. 4", "P(f^{-1}(y), x) et P(f'^{-1}(y'), x') (bold italic P)", "plain $P$ twice", "font", None, "high",
    r"$P(f^{-1}(y),x)$ et $P(f'^{-1}(y'),x')$", r"$" + BP + r"(f^{-1}(y),x)$ et $" + BP + r"(f'^{-1}(y'),x')$")
add(151, "Proposition (6.8.3), l. 1", "soit M(f) (bold italic M)", "$M(f)$", "font", None, "high",
    r"soit $M(f)$¶l'une", r"soit $" + BM + r"(f)$¶l'une")
add(151, "Proposition (6.8.3), l. 2", "être de Cohen-Macaulay (hyphen)", "Cohen--Macaulay", "punctuation", None, "high",
    r"être de Cohen--Macaulay", r"être de Cohen-Macaulay")
add(151, "Proposition (6.8.3), label (i)", "(i) upright", "\\item[(i)] in the italic statement", "convention", 6, "high",
    r"\item[(i)] Soient", r"\item[\textup{(i)}] Soient", "GLOBAL_ISSUES 16.")
add(151, "Proposition (6.8.3) (i)", "Si M(f) et M(g) sont vraies, M(g∘f) (bold italic M)", "plain $M$ three times", "font", None, "high",
    r"Si $M(f)$ et $M(g)$ sont vraies,¶$M(g\circ f)$ est vraie.",
    r"Si $" + BM + r"(f)$ et $" + BM + r"(g)$ sont vraies,¶$" + BM + r"(g\circ f)$ est vraie.")
add(151, "Proposition (6.8.3), label (ii)", "(ii) upright", "\\item[(ii)] in the italic statement", "convention", 6, "high",
    r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement", "GLOBAL_ISSUES 16.")
add(151, "Proposition (6.8.3) (ii)", "si M(f) et M(g∘f) sont vraies, alors M(g) (bold italic M)", "plain $M$ three times", "font", None, "high",
    r"si $M(f)$ et $M(g\circ f)$¶sont vraies, alors $M(g)$",
    r"si $" + BM + r"(f)$ et $" + BM + r"(g\circ f)$¶sont vraies, alors $" + BM + r"(g)$")
add(151, "Proposition (6.8.3), label (iii)", "(iii) upright", "\\item[(iii)] in the italic statement", "convention", 6, "high",
    r"\item[(iii)] Soient", r"\item[\textup{(iii)}] Soient", "GLOBAL_ISSUES 16.")
add(151, "Proposition (6.8.3) (iii)", "si M(f) est vraie, ... de même de M(f') (bold italic M)", "plain $M$ twice", "font", None, "high",
    r"si $M(f)$ est vraie, il en est de même de $M(f')$",
    r"si $" + BM + r"(f)$ est vraie, il en est de même de $" + BM + r"(f')$")
add(151, "Proposition (6.8.3), after the list", "'Les conclusions' starts a new indented paragraph", "\\end{enumerate} followed directly by the text",
    "other", None, "medium", r"\end{enumerate}¶Les conclusions", r"\end{enumerate}¶¶Les conclusions",
    "Paragraph after the list, indented as printed (same form as the p. 136 fix).")
add(151, "Proposition (6.8.3), last sentence", "de (i) et (iii): labels upright", "all italic", "convention", 6, "high",
    r"de (i) et (iii) sont", r"de \textup{(i)} et \textup{(iii)} sont")
add(151, "Proposition (6.8.3), last sentence", "lorsque M est la propriété (bold italic M)", "$M$", "font", None, "high",
    r"lorsque $M$ est la propriété¶d'être lisse", r"lorsque $" + BM + r"$ est la propriété¶d'être lisse")
add(151, "Proposition (6.8.3), last sentence", "(dans (iii)) with upright (iii)", "all italic", "convention", 6, "high",
    r"(dans (iii))", r"(dans \textup{(iii)})")

# ---------------------------------------------------------------- page 152
P151 = "printed p. 151 (TeX text before the misplaced p. 152 marker), proof of (6.8.3) (i)"
add(152, P151, "f_z=f⊗1_{k(z)}: ordinary old-style figure 1 (identity)", "\\mathbf 1 (bold 1)", "font", None, "high",
    r"=f\otimes\mathbf 1", r"=f\otimes1",
    "Enlarged crop: the 1 has the weight of the old-style figures of (2.1.6), not bold. Printed on p. 151; 'old' is in page_152.tex.")
add(152, P151, "subscript k(z) with bold upright k", "_{k(z)}", "convention", 1, "high",
    r"1_{k(z)}:u^{-1}(z)", r"1_{\mathbf{k}(z)}:u^{-1}(z)", "GLOBAL_ISSUES 48 (bold upright k at subscript size). Independent of the previous entry.")
add(152, P151, "est plat (resp. fidèlement plat si f l'est) et pour tout y∈g^{-1}(z), (no comma after 'et')", "et, pour tout",
    "punctuation", None, "high", r"l'est) et, pour tout", r"l'est) et pour tout", "Enlarged crop: no comma after 'et'.")
add(152, P151, "(I, 3.6.4)", "(I, 3.6.4)", "convention", 2, "high",
    r"$f^{-1}(y)$ (I, 3.6.4)", r"$f^{-1}(y)$ (\textbf{I}, 3.6.4)")
add(152, P151, "Si M(f) et M(g) sont vraies, M(g∘f) ... où M est (bold italic M)", "plain $M$ four times", "font", None, "high",
    r"Si $M(f)$ et $M(g)$¶sont vraies, $M(g\circ f)$ est donc vraie pour les cas où $M$ est",
    r"Si $" + BM + r"(f)$ et $" + BM + r"(g)$¶sont vraies, $" + BM + r"(g\circ f)$ est donc vraie pour les cas où $" + BM + r"$ est")
add(152, P151, "Cohen-Macaulay (hyphenated at the line end 'Cohen-/Macaulay')", "Cohen--Macaulay", "punctuation", None, "medium",
    r"d'être de Cohen--Macaulay ou", r"d'être de Cohen-Macaulay ou",
    "The line break falls at the compound's hyphen; same hyphen as the other printed 'Cohen-Macaulay'.")
add(152, P151, "extension finie de k(z) (bold italic k)", "$k(z)$", "convention", 1, "high",
    r"extension finie de $k(z)$", r"extension finie de $\boldsymbol{k}(z)$")
add(152, P151, "Y'_z=g^{-1}(z)⊗_{k(z)}k' (subscript k bold upright)", "\\otimes_{k(z)}", "convention", 1, "high",
    r"g^{-1}(z)\otimes_{k(z)}k'", r"g^{-1}(z)\otimes_{\mathbf{k}(z)}k'")
add(152, P151, "X'_z=u^{-1}(z)⊗_{k(z)}k' (subscript k bold upright)", "\\otimes_{k(z)}", "convention", 1, "high",
    r"u^{-1}(z)\otimes_{k(z)}k'", r"u^{-1}(z)\otimes_{\mathbf{k}(z)}k'")
add(152, P151, "f'_z=f_z⊗1_{k'}: ordinary old-style figure 1", "\\mathbf 1 (bold 1)", "font", None, "high",
    r"f_z\otimes\mathbf 1_{k'}", r"f_z\otimes1_{k'}", "As the identity 1 above (enlarged crop).")
add(152, P151, "X'_z→Y'_z; le morphisme f'_z", "Y'_z$. Le morphisme", "punctuation", None, "high",
    r"Y'_z$. Le", r"Y'_z$; le", "The print has a semicolon and lower-case 'le'.")
add(152, "p. 152, l. 1", "est plat (resp. fidèlement plat) et pour tout y'∈Y'_z, (no comma after 'et')", "et, pour tout",
    "punctuation", None, "high", r"fidèlement plat) et, pour tout", r"fidèlement plat) et pour tout", "Enlarged crop: no comma after 'et'.")
add(152, "p. 152, l. 2", "est isomorphe à f^{-1}(y)⊗_{k(y)}k(y') (f without subscript z)", "$f_z^{-1}(y)\\otimes_{k(y)}k(y')$", "formula", None, "high",
    r"isomorphe à $f_z^{-1}(y)", r"isomorphe à $f^{-1}(y)",
    "Enlarged crop: plain f^{-1}(y) in the print (isomorphic to f_z^{-1}(y), as just stated), so not a misprint.")
add(152, "p. 152, l. 2", "⊗ with subscript k(y) in bold upright k", "\\otimes_{k(y)}", "convention", 1, "high",
    r"\otimes_{k(y)}", r"\otimes_{\mathbf{k}(y)}", "GLOBAL_ISSUES 48.")
add(152, "p. 152, l. 2", "k(y') bold italic k", "k(y')", "convention", 1, "high",
    r"}k(y')$, en désignant", r"}\boldsymbol{k}(y')$, en désignant")
add(152, "p. 152, l. 2", "(I, 3.6.4)", "(I, 3.6.4)", "convention", 2, "high",
    r"$g^{-1}(z)$ (I, 3.6.4)", r"$g^{-1}(z)$ (\textbf{I}, 3.6.4)")
add(152, "p. 152, l. 2", "Lorsque M est (bold italic M)", "$M$", "font", None, "high",
    r"Lorsque $M$ est la propriété d'être", r"Lorsque $" + BM + r"$ est la propriété d'être")
add(152, "p. 152, l. 3", "l'hypothèse que M(f) et M(g) (bold italic M)", "plain $M$ twice", "font", None, "high",
    r"l'hypothèse que $M(f)$ et $M(g)$ sont¶vraies", r"l'hypothèse que $" + BM + r"(f)$ et $" + BM + r"(g)$ sont¶vraies")
add(152, "p. 152, l. 5", "parmi les propriétés c), d), e), f) (italic labels)", "c), d), e), f)", "italics", None, "high",
    r"propriétés c), d),¶e), f) de (6.6.1)", r"propriétés \emph{c)}, \emph{d)},¶\emph{e)}, \emph{f)} de (6.6.1)")
add(152, "p. 152, l. 6", "donc M(g∘f) est vraie (bold italic M)", "$M(g\\circ f)$", "font", None, "high",
    r"donc $M(g\circ f)$ est vraie", r"donc $" + BM + r"(g\circ f)$ est vraie")
add(152, "proof of (6.8.3) (ii)", "M(g∘f) et M(f) (bold italic M)", "plain $M$ twice", "font", None, "high",
    r"l'hypothèse que $M(g\circ f)$ et $M(f)$ sont vraies", r"l'hypothèse que $" + BM + r"(g\circ f)$ et $" + BM + r"(f)$ sont vraies")
add(152, "proof of (6.8.3) (ii)", "donc M(g) est vraie (bold italic M)", "$M(g)$", "font", None, "high",
    r"donc $M(g)$ est¶vraie", r"donc $" + BM + r"(g)$ est¶vraie")
add(152, "proof of (6.8.3) (iii)", "P(f^{-1}(y), x) et P(f'^{-1}(y'), x') (bold italic P)", "plain $P$ twice", "font", None, "high",
    r"$P(f^{-1}(y),x)$ et¶$P(f'^{-1}(y'),x')$", r"$" + BP + r"(f^{-1}(y),x)$ et¶$" + BP + r"(f'^{-1}(y'),x')$")
add(152, "proof of (6.8.3) (iii)", "on voit que M(f) et M(f') (bold italic M)", "plain $M$ twice", "font", None, "high",
    r"on voit que $M(f)$ et $M(f')$", r"on voit que $" + BM + r"(f)$ et $" + BM + r"(f')$")
add(152, "proof of (6.8.3), last paragraph", "'Enfin, la dernière assertion' starts a new indented paragraph", "\\end{enumerate} followed directly by 'Enfin'",
    "other", None, "medium", r"\end{enumerate}¶Enfin", r"\end{enumerate}¶¶Enfin",
    "Paragraph after the list, indented as printed (same form as the p. 136 fix).")
add(152, "Remarques (6.8.4) (ii)", "« régulier (resp. (R_n), resp. normal) sur k » with régulier, normal, sur italic", "no emphasis",
    "italics", None, "high",
    r"«régulier¶(resp. $(R_n)$, resp. normal) sur $k$»", r"«\emph{régulier}¶(resp. $(R_n)$, resp. \emph{normal}) \emph{sur} $k$»",
    "The remark is printed roman (judged as if its body were roman); enlarged crop.")
add(152, "Proposition (6.8.5), l. 2", "désignons par P(Z) (bold italic P)", "$P(Z)$", "font", None, "high",
    r"désignons par $P(Z)$", r"désignons par $" + BP + r"(Z)$")
add(152, "Proposition (6.8.5), l. 3", "propriétés c) à f) de (6.6.1): c), f) and the reference upright", "all italic", "convention", 6, "high",
    r"propriétés c) à f) de (6.6.1);", r"propriétés \textup{c)} à \textup{f)} de \textup{(6.6.1)};", "Enlarged crop.")
add(152, "Proposition (6.8.5), l. 3", "« P(Z) géométrique » (bold italic P)", "$P(Z)$", "font", None, "high",
    r"«$P(Z)$ géométrique»", r"«$" + BP + r"(Z)$ géométrique»")
add(152, "Proposition (6.8.5), ll. 3-4", "définie dans (6.7.6) (resp. (4.6.1)) upright", "all italic", "convention", 6, "high",
    r"définie dans (6.7.6) (resp. (4.6.1))", r"définie dans \textup{(6.7.6) (resp. (4.6.1))}", "Enlarged crop.")
add(152, "Proposition (6.8.5), l. 4", "lorsque P(Z) est (bold italic P)", "$P(Z)$", "font", None, "high",
    r"lorsque¶$P(Z)$ est", r"lorsque¶$" + BP + r"(Z)$ est")
add(152, "Proposition (6.8.5), l. 4", "propriétés c), d), e) (resp. f)) de (6.6.1): labels, resp. and reference upright", "all italic",
    "convention", 6, "high",
    r"propriétés c), d), e) (resp. f)) de (6.6.1). Alors", r"propriétés \textup{c), d), e) (resp. f))} de \textup{(6.6.1)}. Alors",
    "Enlarged crop.")
add(152, "Proposition (6.8.5), label (i)", "(i) upright", "\\item[(i)] in the italic statement", "convention", 6, "high",
    r"\item[(i)] Si $X$", r"\item[\textup{(i)}] Si $X$", "GLOBAL_ISSUES 16.")
add(152, "Proposition (6.8.5) (i)", "la propriété P, ... P géométrique, ... la propriété P (bold italic P)", "plain $P$ three times", "font", None, "high",
    r"possède la propriété $P$, et $Y$ la propriété $P$¶géométrique, $X\times_kY$ possède la propriété $P$.",
    r"possède la propriété $" + BP + r"$, et $Y$ la propriété $" + BP + r"$¶géométrique, $X\times_kY$ possède la propriété $" + BP + r"$.")
add(152, "Proposition (6.8.5), label (ii)", "(ii) upright", "\\item[(ii)] in the italic statement", "convention", 6, "high",
    r"\item[(ii)] Si $X$", r"\item[\textup{(ii)}] Si $X$", "GLOBAL_ISSUES 16.")
add(152, "Proposition (6.8.5) (ii)", "la propriété P géométrique (bold italic P)", "$P$", "font", None, "high",
    r"possèdent la propriété $P$ géométrique", r"possèdent la propriété $" + BP + r"$ géométrique")
add(152, "proof of (6.8.5), l. 2", "la propriété P géométrique (bold italic P)", "$P$", "font", None, "high",
    r"$Y$ possède la propriété $P$ géométrique entraîne", r"$Y$ possède la propriété $" + BP + r"$ géométrique entraîne")
add(152, "proof of (6.8.5), ll. 3-4", "M(f) ..., M étant ... qui correspond à P (bold italic M, M, P)", "plain $M$, $M$, $P$", "font", None, "high",
    r"$M(f)$ est vraie, $M$ étant la propriété de (6.8.3) qui correspond à $P$",
    r"$" + BM + r"(f)$ est vraie, $" + BM + r"$ étant la propriété de (6.8.3) qui correspond à $" + BP + r"$")
add(152, "proof of (6.8.5), l. 4", "M(g) est aussi vraie (bold italic M)", "$M(g)$", "font", None, "high",
    r"$M(g)$ est aussi vraie", r"$" + BM + r"(g)$ est aussi vraie")
add(152, "Théorème (6.8.6), label a)", "a) upright", "\\item[a)] in the italic statement", "convention", 6, "high",
    r"\item[a)]", r"\item[\textup{a)}]", "Enlarged crop: the lettered labels of this statement are upright.")
add(152, "Théorème (6.8.6), label b)", "b) upright", "\\item[b)] in the italic statement", "convention", 6, "high",
    r"\item[b)]", r"\item[\textup{b)}]")
add(152, "marker: printed p. 152 begins 'est plat (resp. fidèlement plat)'", "p. 151 ends '... le morphisme f'_z'",
    "\\oldpage[IV-2]{152} stands before \\begin{enumerate} of the proof of (6.8.3)", "marker", None, "high",
    r"$f'_z$ est plat¶(resp.", r"$f'_z$¶\oldpage[IV-2]{152}¶est plat¶(resp.",
    "Inserts the marker mid-sentence on its own line (no blank lines). Apply after every other page-152 entry and together with the next "
    "entry, which removes the old marker; afterwards '\\begin{enumerate} ... le morphisme $f'_z$' belongs to p. 151, whose print it matches "
    "once the page-152 entries marked 'printed p. 151' are applied.")
add(152, "marker (old position)", "-", "\\oldpage[IV-2]{152} before the proof's \\begin{enumerate}", "marker", None, "high",
    r"\oldpage[IV-2]{152}¶\begin{enumerate}", r"\begin{enumerate}",
    "Apply together with, and after, the previous entry (both or neither).")

# ---------------------------------------------------------------- page 153
add(153, "Théorème (6.8.6), label c)", "c) upright", "\\item[c)] in the italic statement", "convention", 6, "high",
    r"\item[c)]", r"\item[\textup{c)}]")
add(153, "Théorème (6.8.6) c)", "(0, 19.3.1): bold 0, reference upright", "(0, 19.3.1) italic, plain 0", "convention", 2, "high",
    r"(0, 19.3.1) pour les topologies préadiques", r"\textup{(\textbf{0}, 19.3.1)} pour les topologies préadiques",
    "One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
add(153, "Théorème (6.8.6) c)", "(0, 19.3.1) upright", "italic", "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(153, "Théorème (6.8.6), label c')", "c') upright", "\\item[c')] in the italic statement", "convention", 6, "high",
    r"\item[c')]", r"\item[\textup{c')}]")
add(153, "Théorème (6.8.6) c')", "(0, 19.3.1): bold 0, reference upright", "(0, 19.3.1) italic, plain 0", "convention", 2, "high",
    r"(0, 19.3.1) pour les topologies discrètes", r"\textup{(\textbf{0}, 19.3.1)} pour les topologies discrètes",
    "One edit for this finding and the next (convention 6).")
add(153, "Théorème (6.8.6) c')", "(0, 19.3.1) upright", "italic", "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2).")
add(153, "proof of (6.8.6), l. 1", "L'équivalence de a) et b) (italic labels)", "a) et b)", "italics", None, "high",
    r"L'équivalence de a) et b)", r"L'équivalence de \emph{a)} et \emph{b)}")
add(153, "proof of (6.8.6), l. 1", "et du fait que pour les (no comma)", "du fait que, pour les", "punctuation", None, "high",
    r"du fait que,¶pour les", r"du fait que¶pour les", "Enlarged crop: no comma after 'que'.")
add(153, "proof of (6.8.6), l. 3", "(1.4.2). | new paragraph: En second lieu, ...", "(1.4.2). En second lieu (same paragraph)", "other", None, "high",
    r"(1.4.2). En second lieu", r"(1.4.2).¶¶En second lieu", "Missing paragraph break: 'En second lieu' is indented in the print.")
add(153, "proof of (6.8.6), l. 5", "O_x⊗_{O_y}k(y) (bold italic k)", "k(y)", "convention", 1, "high",
    r"plat et que $\mathcal O_x\otimes_{\mathcal O_y}k(y)$", r"plat et que $\mathcal O_x\otimes_{\mathcal O_y}\boldsymbol{k}(y)$")
add(153, "proof of (6.8.6), l. 6", "soit une k(y)-algèbre (bold italic k)", "$k(y)$", "convention", 1, "high",
    "¶soit une $k(y)$-algèbre", r"¶soit une $\boldsymbol{k}(y)$-algèbre")
add(153, "proof of (6.8.6), l. 6", "(0, 19.7.1)", "(0, 19.7.1)", "convention", 2, "high",
    r"(0, 19.7.1)", r"(\textbf{0}, 19.7.1)")
add(153, "proof of (6.8.6), l. 7", "mais pour que O_x⊗_{O_y}k(y) (bold italic k)", "k(y)", "convention", 1, "high",
    r"mais pour que $\mathcal O_x\otimes_{\mathcal O_y}k(y)$", r"mais pour que $\mathcal O_x\otimes_{\mathcal O_y}\boldsymbol{k}(y)$")
add(153, "proof of (6.8.6), l. 7", "soit une k(y)-algèbre formellement lisse (bold italic k)", "$k(y)$", "convention", 1, "high",
    r" soit une $k(y)$-algèbre formellement", r" soit une $\boldsymbol{k}(y)$-algèbre formellement")
add(153, "proof of (6.8.6), l. 8", "qu'elle soit une k(y)-algèbre (bold italic k)", "$k(y)$", "convention", 1, "high",
    r"qu'elle soit une $k(y)$-algèbre", r"qu'elle soit une $\boldsymbol{k}(y)$-algèbre")
add(153, "proof of (6.8.6), l. 8", "(0, 19.6.6)", "(0, 19.6.6)", "convention", 2, "high",
    r"(0, 19.6.6)", r"(\textbf{0}, 19.6.6)")
add(153, "proof of (6.8.6), l. 9", "l'équivalence de b) et c) (italic labels)", "b) et c)", "italics", None, "high",
    r"l'équivalence de b) et c). Enfin", r"l'équivalence de \emph{b)} et \emph{c)}. Enfin")
add(153, "proof of (6.8.6), ll. 9-10", "l'équivalence de c) et c') (italic labels)", "c) et c')", "italics", None, "high",
    r"l'équivalence de c) et c'), on peut", r"l'équivalence de \emph{c)} et \emph{c')}, on peut")
add(153, "proof of (6.8.6), l. 13", "l'équivalence de c) et c') résulte (italic labels)", "c) et c')", "italics", None, "high",
    r"l'équivalence de c) et c') résulte", r"l'équivalence de \emph{c)} et \emph{c')} résulte")
add(153, "proof of (6.8.6), l. 13", "(0, 22.6.4)", "(0, 22.6.4)", "convention", 2, "high",
    r"(0, 22.6.4)", r"(\textbf{0}, 22.6.4)")
add(153, "Corollaire (6.8.7), l. 2", "(ou régulier) with roman 'ou'", "(ou régulier) all italic", "convention", 6, "high",
    r"(ou régulier)", r"(\textup{ou} régulier)", "Enlarged crop: 'ou' upright, 'régulier' italic.")
add(153, "proof of (6.8.7)", "(0, 22.6.5)", "(0, 22.6.5)", "convention", 2, "high",
    r"(0, 22.6.5)", r"(\textbf{0}, 22.6.5)")
add(153, "proof of (6.8.7)", "la condition c') (italic label)", "c')", "italics", None, "high",
    r"condition c') de", r"condition \emph{c')} de")
add(153, "Remarque (6.8.8), l. 1", "l'équivalence de b) et c') (italic labels)", "b) et c')", "italics", None, "high",
    r"l'équivalence de b) et c') dans", r"l'équivalence de \emph{b)} et \emph{c')} dans",
    "The remark is printed roman (judged as if its body were roman).")
add(153, "Remarque (6.8.8), end", "morphismes localement de présentation finie (italic)", "no emphasis", "italics", None, "high",
    r"morphismes localement de¶présentation finie.", r"morphismes \emph{localement de¶présentation finie}.")
add(153, "heading 6.9", "6.9. Le théorème de platitude générique.", "title without the full stop", "punctuation", None, "high",
    r"\subsection{Le théorème de platitude générique}", r"\subsection{Le théorème de platitude générique.}",
    "GLOBAL_ISSUES 43/58.")
add(153, "Théorème (6.9.1), last line", "F|u^{-1}(U) (restriction bar, then u^{-1}(U) on the line)", "\\mathcal F|_{u^{-1}(U)} (subscript)",
    "formula", None, "high", r"\mathcal F|_{u^{-1}(U)}", r"\mathcal F|u^{-1}(U)",
    "Enlarged crop. Same notation at the top of p. 155.")
add(153, "proof of (6.9.1), l. 3", "F|(X_i∩u^{-1}(U_i)) (on the line, with parentheses)", "\\mathcal F|_{X_i\\cap u^{-1}(U_i)}",
    "formula", None, "high", r"\mathcal F|_{X_i\cap u^{-1}(U_i)}", r"\mathcal F|(X_i\cap u^{-1}(U_i))", "Enlarged crop.")
add(153, "proof of (6.9.1), end", "le théorème résultera par suite du | Lemme (6.9.2). — (the sentence runs into the heading)",
    "par suite du lemme suivant.", "extra", None, "high",
    r"par suite du lemme suivant.", r"par suite du",
    "The words 'lemme suivant.' are not printed: the printed sentence ends with 'du' and continues with the heading 'Lemme (6.9.2)'.")

# ---------------------------------------------------------------- page 154
add(154, "marker: printed p. 154 begins 'sur la dimension n du support'", "p. 153 ends '... Nous raisonnerons par récurrence'",
    "\\oldpage[IV-2]{154} stands before 'Désignons par K'", "marker", None, "high",
    r"récurrence sur la", r"récurrence¶\oldpage[IV-2]{154}¶sur la",
    "Inserts the marker mid-sentence on its own line. Apply together with the next entry (both or neither); afterwards "
    "'Désignons par $K$ ... par récurrence' belongs to p. 153 and matches its print. Independent of the other p. 154 entries.")
add(154, "marker (old position)", "-", "\\oldpage[IV-2]{154} before 'Désignons'", "marker", None, "high",
    r"\oldpage[IV-2]{154}¶Désignons", r"Désignons", "Apply together with the previous entry.")
add(154, "l. 1", "la dimension n (dimension italic)", "la dimension $n$", "italics", None, "high",
    r"dimension $n$ du support", r"\emph{dimension} $n$ du support")
add(154, "l. 1", "qui est —∞ (long dash)", "$-\\infty$", "convention", 7, "high",
    r"qui est $-\infty$", r"qui est $\setmin\infty$", "Unary minus printed as the long dash (GLOBAL_ISSUES 23/49); \\setmin pending the convention-7 decision.")
add(154, "l. 2", "n = —∞ (long dash)", "$n=-\\infty$", "convention", 7, "high",
    r"$n=-\infty$", r"$n=\setmin\infty$", "As the previous entry (same form as the p. 52 fix '=\\setmin\\infty').")
add(154, "l. 5", "M_1⊃M_2⊃. . .⊃M_q (baseline dots)", "\\supset\\cdots\\supset", "symbol", None, "high",
    r"M_2\supset\cdots\supset M_q", r"M_2\supset\ldots\supset M_q", "Enlarged crop: dots on the baseline (GLOBAL_ISSUES 22).")
add(154, "l. 7", "n° 4 (superior o)", "n°~4 (degree sign)", "symbol", None, "high",
    r"n°~4", r"n\textsuperscript{o}~4", "As the p. 108 fix (GLOBAL_ISSUES 57).")
add(154, "l. 9", "f = f_1f_2. . .f_{q-1} (baseline dots)", "f_1f_2\\cdots f_{q-1}", "symbol", None, "high",
    r"f_1f_2\cdots f_{q-1}", r"f_1f_2\ldots f_{q-1}", "Enlarged crop: dots on the baseline.")
add(154, "l. 10", "1≤i≤q—1 (long dash)", "q-1", "convention", 7, "high",
    r"i\leq q-1$", r"i\leq q\setmin 1$", "Subtraction printed with the long dash; the subscript q-1 of f_{q-1} has an ordinary minus.")
add(154, "l. 10", "(0_I, 1.3.2) with bold 0", "$(0_{\\mathrm I},1.3.2)$", "convention", 2, "high",
    r"$(0_{\mathrm I},1.3.2)$ et comme", r"$(\mathbf{0}_{\mathrm I},1.3.2)$ et comme", "Form of the p. 5 fixes.")
add(154, "l. 13", "au cas où M = B et B est intègre ('et', 'est intègre' italic)", "no emphasis", "italics", None, "high",
    r"$M=B$ et $B$ est intègre.", r"$M=B$ \emph{et} $B$ \emph{est intègre}.", "Enlarged crop.")
add(154, "l. 14", "n° 1 (superior o)", "n°~1 (degree sign)", "symbol", None, "high",
    r"n°~1", r"n\textsuperscript{o}~1", "As the p. 108 fix.")
add(154, "l. 16", "B_g soit entier sur (entier italic)", "soit entier sur", "italics", None, "high",
    r"soit entier sur", r"soit \emph{entier} sur")
add(154, "l. 18", "de type fini et sans torsion (sans torsion italic)", "no emphasis", "italics", None, "high",
    r"type fini et sans torsion.", r"type fini et \emph{sans torsion}.")
add(154, "l. 22", "un C-module de torsion de type fini (de torsion italic)", "no emphasis", "italics", None, "high",
    r"module de torsion de type fini", r"module \emph{de torsion} de type fini")
add(154, "l. 23", "(I, 7.4.6)", "(I, 7.4.6)", "convention", 2, "high",
    r"(I, 7.4.6)", r"(\textbf{I}, 7.4.6)")
add(154, "l. 24", "(I, 9.1.13.1)", "(I, 9.1.13.1)", "convention", 2, "high",
    r"(I, 9.1.13.1)", r"(\textbf{I}, 9.1.13.1)")
add(154, "l. 27", "(0_I, 1.3.2) with bold 0", "$(0_{\\mathrm I},1.3.2)$", "convention", 2, "high",
    r"vertu de $(0_{\mathrm I},1.3.2)$", r"vertu de $(\mathbf{0}_{\mathrm I},1.3.2)$")
add(154, "proof of (6.9.3), l. 1", "(0_I, 2.2.2) with bold 0", "$(0_{\\mathrm I},2.2.2)$", "convention", 2, "high",
    r"$(0_{\mathrm I},2.2.2)$", r"$(\mathbf{0}_{\mathrm I},2.2.2)$")
add(154, "end of the page (end of the segment)", "page ends mid-sentence: '... un ouvert non vide U⊂T' | p. 155 'tel que ...'",
    "blank line before \\oldpage[IV-2]{155}", "other", None, "high",
    r"$U\subset T$¶¶", r"$U\subset T$¶",
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 155 entry that removes the blank line after \\oldpage[IV-2]{155} "
    "('\\oldpage[IV-2]{155}\\n\\ntel que' -> '\\oldpage[IV-2]{155}\\ntel que'), which lies outside pp. 150-154.")


# ---------------------------------------------------------------- checks
def page_text(p):
    with open(f"{RUN}/page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
texts = {p: page_text(p) for p in range(150, 155)}
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    c = texts[f["page"]].count(f["fix"]["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE/ABSENT", c, i, f["page"], repr(f["fix"]["old"]))
# sequential application, in list order
work = dict(texts)
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    t = work[f["page"]]
    c = t.count(f["fix"]["old"])
    if c != 1:
        ok = False
        print("SEQUENTIAL FAIL", c, i, f["page"], repr(f["fix"]["old"]))
        continue
    work[f["page"]] = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
# reversed order too (order independence where claimed)
work2 = dict(texts)
for i, f in reversed(list(enumerate(F))):
    if f["fix"] is None:
        continue
    t = work2[f["page"]]
    c = t.count(f["fix"]["old"])
    if c != 1:
        print("reverse-order note", c, i, f["page"], repr(f["fix"]["old"][:60]))
        continue
    work2[f["page"]] = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in range(150, 155):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "ok" if ok else "PROBLEMS")
if "--write" in sys.argv and ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
if "--dump" in sys.argv:
    for p in range(150, 155):
        with open(f"user/Documents/ega_scan_check_20261101/run_IV2/crops_150_154/applied_{p}.tex", "w", encoding="utf-8", newline="\n") as fh:
            fh.write(work[p])
