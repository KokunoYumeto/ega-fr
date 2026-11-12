import json

NL = "|NL|"


def L(s):
    return s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": (None if old is None else {"old": L(old), "new": L(new)})}
    if kind == "misprint_in_print":
        d["corrected"] = L(corrected)
    d["note"] = note
    F.append(d)


# ---------------- page 55 ----------------
add(54, "printed p. 55 begins: marker \\oldpage[IV-2]{55} (edit 1 of 2, insert; this edit lies in the p. 54 segment, page_054.tex)",
    "Printed p. 55 begins 'corps des fractions de K'⊗_kL est L(t) ; on a le diagramme commutatif d'homomorphismes canoniques', then the diagram (4.2.1.3); printed p. 54 ends '... qui en est un anneau de fractions, et le' (page_054_s4.png, last line).",
    "\\oldpage[IV-2]{55} stands after 'diagramme commutatif d'homomorphismes canoniques' (end of page_054.tex), so the first one and a half printed lines of p. 55 sit in the p. 54 segment",
    "marker", None, "high",
    r"et le corps des fractions de $K'\otimes_k L$",
    r"et le|NL|\oldpage[IV-2]{55}|NL|corps des fractions de $K'\otimes_k L$",
    "Inserts the marker where printed p. 55 begins (mid-sentence, on its own line, no blank lines). Apply before edit 2 (next finding), which removes the old marker.")
add(55, "page start: marker \\oldpage[IV-2]{55} (edit 2 of 2, remove the misplaced marker)",
    "see the previous finding",
    "\\oldpage[IV-2]{55} directly before \\begin{equation} of (4.2.1.3)",
    "marker", None, "high",
    r"\oldpage[IV-2]{55}|NL||NL|\begin{equation}",
    r"\begin{equation}",
    "Apply together with, and after, edit 1 (page 54 above). After both, 'corps des fractions ... canoniques' belongs to p. 55, matching the print.")
add(55, "after the diagram (4.2.1.3): 'Comme K est fidèlement plat sur K''",
    "the line after the display starts at the left margin (no indent): the paragraph continues",
    "blank line after \\end{equation} starts a new (indented) paragraph",
    "other", None, "high",
    r"\end{equation}|NL||NL|Comme $K$ est fidèlement plat",
    r"\end{equation}|NL|Comme $K$ est fidèlement plat",
    "Paragraph break after a display that the print does not have.")
add(55, "proof of (4.2.1): '(0_I, 6.5.2)'", "(0_I, 6.5.2) with a bold 0", "$(0_{\\mathrm I},6.5.2)$, plain 0",
    "convention", 2, "high",
    r"$(0_{\mathrm I},6.5.2)$", r"$(\mathbf{0}_{\mathrm I},6.5.2)$")
add(55, "proof of (4.2.1): '(0_I, 6.3.4 et Bourbaki, ...)'", "(0_I, 6.3.4 with a bold 0", "$(0_{\\mathrm I},6.3.4$, plain 0",
    "convention", 2, "high",
    r"$(0_{\mathrm I},6.3.4$", r"$(\mathbf{0}_{\mathrm I},6.3.4$")
add(55, "proof of (4.2.1), last lines: first 'deg.tr' in 'deg.tr_k E = deg.tr_k L(t) = Card(I) = deg.tr_k K'",
    "deg.tr with no full stop after tr (enlarged crop); same on p. 54 in (4.2.1.2)",
    "\\operatorname{deg.tr.} prints 'deg.tr.'",
    "punctuation", None, "high",
    r"$\operatorname{deg.tr.}_L E", r"$\operatorname{deg.tr}_L E",
    "ega4-2-fr.tex writes \\operatorname{deg.tr.} 47 times (deg.tr 5 times); see the final message.")
add(55, "proof of (4.2.1), last lines: second 'deg.tr'",
    "deg.tr with no full stop after tr", "\\operatorname{deg.tr.}",
    "punctuation", None, "high",
    r"E=\operatorname{deg.tr.}_L L", r"E=\operatorname{deg.tr}_L L")
add(55, "proof of (4.2.1), last lines: third 'deg.tr'",
    "deg.tr with no full stop after tr", "\\operatorname{deg.tr.}",
    "punctuation", None, "high",
    r"=\operatorname{deg.tr.}_k K", r"=\operatorname{deg.tr}_k K")
add(55, "proof of (4.2.1), last lines: 'donc deg.tr_k E = deg.tr_k L(t) = Card(I) = deg.tr_k K'",
    "deg.tr_k E = deg.tr_k L(t): both subscripts are an italic k (enlarged crop)",
    "deg.tr_L E = deg.tr_L L(t) (silently corrected)",
    "misprint_in_print", None, "high",
    r"\operatorname{deg.tr}_L E=\operatorname{deg.tr}_L L(\mathbf t)",
    r"\operatorname{deg.tr}_k E=\operatorname{deg.tr}_k L(\mathbf t)",
    "E is algebraic over L(t), so deg.tr_L E = deg.tr_L L(t) = Card(I) (the relation deg.tr_L E = deg.tr_k K of (4.2.1.1)); deg.tr_k L(t) = Card(I) is false unless L is algebraic over k. The TeX has the correct L; the fix restores the printed k. Its 'old' is the text after the three punctuation fixes above (apply them first); it changes only the two subscripts.",
    corrected=r"\operatorname{deg.tr}_L E=\operatorname{deg.tr}_L L(\mathbf t)")
add(55, "Corollaire (4.2.2): 'Sous les hypothèses de (3.3.6),'", "reference (3.3.6) upright inside the italic statement",
    "(3.3.6) italic in the corollary environment", "convention", 6, "high",
    r"de (3.3.6), si les préschémas", r"de \textup{(3.3.6)}, si les préschémas")
add(55, "Corollaire (4.2.3): '(3.3.6) (resp. (3.3.7)),'", "references, 'resp.' and all parentheses upright (crop)",
    "set italic in the corollary environment", "convention", 6, "high",
    r"de (3.3.6) (resp. (3.3.7)), si", r"de \textup{(3.3.6) (resp. (3.3.7))}, si")
add(55, "Corollaire (4.2.3): '(pour s∈S)'", "both parentheses upright, 'pour' italic (enlarged crop)",
    "parentheses italic in the corollary environment", "convention", 6, "medium",
    r"(pour $s\in S$)", r"\textup{(}pour $s\in S$\textup{)}")
add(55, "Corollaire (4.2.3): '(resp. 𝓕 et 𝓖)'", "'(resp.' and the closing parenthesis upright, 'et' italic (enlarged crop)",
    "all italic in the corollary environment", "convention", 6, "high",
    r"(resp. $\mathcal F$ et $\mathcal G$) sont", r"\textup{(resp.} $\mathcal F$ et $\mathcal G$\textup{)} sont")
add(55, "after (4.2.3): 'comme tout préschéma sur un corps k est plat sur k'", "only 'plat' italic; 'sur' roman (enlarged crop)",
    "\\emph{plat sur $k$} ('sur' italic)", "italics", None, "high",
    r"\emph{plat sur $k$}", r"\emph{plat} sur $k$")
add(55, "Proposition (4.2.4), label (i)", "label (i) upright", "\\item[(i)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(55, "Proposition (4.2.4), label (ii)", "label (ii) upright", "\\item[(ii)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(55, "Proposition (4.2.4) (i): '(autrement dit l'ensemble des idéaux premiers minimaux de R(X)⊗_kR(Y))'",
    "'(autrement dit' and the closing parenthesis roman; 'l'ensemble des idéaux premiers minimaux de' italic (enlarged crop)",
    "whole parenthesis italic inside the proposition", "convention", 6, "high",
    r"(autrement dit l'ensemble des|NL|idéaux premiers minimaux de $R(X)\otimes_k R(Y)$),",
    r"\textup{(autrement dit} l'ensemble des|NL|idéaux premiers minimaux de $R(X)\otimes_k R(Y)$\textup{)},")

# ---------------- page 56 ----------------
add(56, "Proposition (4.2.4), label (iii)", "label (iii) upright", "\\item[(iii)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", "GLOBAL_ISSUES 16.")
add(56, "proof of (4.2.4): '(0_I, 1.2.5)'", "(0_I, 1.2.5) with a bold 0", "$(0_{\\mathrm I},1.2.5)$, plain 0",
    "convention", 2, "high", r"$(0_{\mathrm I},1.2.5)$", r"$(\mathbf{0}_{\mathrm I},1.2.5)$")
add(56, "proof of (4.2.4): 'Enfin, si par exemple R(Y) est séparable sur k'",
    "'Enfin,' begins a new indented paragraph", "runs on in the same paragraph after '(0_I, 1.2.5).'",
    "other", None, "high",
    r"$. Enfin, si par exemple", r"$.|NL||NL|Enfin, si par exemple", "Missing paragraph break.")
add(56, "Proposition (4.2.5), l. 2: '𝓕 (resp. 𝓖) un'", "'(resp. 𝓖)' upright, parentheses included",
    "italic in the proposition environment", "convention", 6, "high",
    r"(resp. $\mathcal G$) un", r"\textup{(resp. $\mathcal G$)} un")
add(56, "Proposition (4.2.5), l. 2: '(resp. un 𝒪_Y-Module)'", "'(resp.' and the closing parenthesis upright; 'un 𝒪_Y-Module' italic (enlarged crop)",
    "all italic", "convention", 6, "high",
    r"(resp. un|NL|$\mathcal O_Y$-Module)", r"\textup{(resp.} un|NL|$\mathcal O_Y$-Module\textup{)}")
add(56, "Proposition (4.2.5), l. 2: 'Soit (Z'_λ) (resp. (Z''_μ)) la famille des cycles'", "'(resp. (Z''_μ))' upright",
    "'resp.' and the outer closing parenthesis italic", "convention", 6, "high",
    r"(resp.|NL|$(Z''_\mu)$) la famille des cycles", r"\textup{(resp.|NL|$(Z''_\mu)$)} la famille des cycles")
add(56, "Proposition (4.2.5), l. 3: 'associés à 𝓕 (resp. 𝓖), et'", "'(resp. 𝓖)' upright",
    "italic", "convention", 6, "high",
    r"(resp.|NL|$\mathcal G$), et", r"\textup{(resp.|NL|$\mathcal G$)}, et")
add(56, "Proposition (4.2.5), l. 3: 'par Z'_λ (resp. Z''_μ) le sous-préschéma'", "'(resp. Z''_μ)' upright",
    "italic", "convention", 6, "high",
    r"(resp. $Z''_\mu$) le|NL|sous-préschéma", r"\textup{(resp. $Z''_\mu$)} le|NL|sous-préschéma")
add(56, "Proposition (4.2.5), l. 4: 'réduit de X (resp. Y) ayant'", "'(resp. Y)' upright",
    "italic", "convention", 6, "high",
    r"de $X$ (resp. $Y$) ayant $Z'_\lambda$", r"de $X$ \textup{(resp. $Y$)} ayant $Z'_\lambda$")
add(56, "Proposition (4.2.5), l. 4: 'ayant Z'_λ (resp. Z''_μ) comme espace'", "'(resp. Z''_μ)' upright",
    "italic", "convention", 6, "high",
    r"(resp.|NL|$Z''_\mu$) comme espace", r"\textup{(resp.|NL|$Z''_\mu$)} comme espace")
add(56, "proof of (4.2.5): 'Spec(k(x))'", "bold italic k in k(x)", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(x))", r"\operatorname{Spec}(\boldsymbol{k}(x))")
add(56, "proof of (4.2.5): 'Spec(k(y))'", "bold italic k in k(y)", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))")
add(56, "Corollaire (4.2.6), l. 2: 'tels que X×_kY soit localement noethérien'",
    "the subscript k is a bold italic sort (enlarged crop: heavy strokes, unlike every other subscript k on the page)",
    "plain $X\\times_k Y$ (silently corrected)", "misprint_in_print", None, "high",
    r"que $X\times_k Y$ soit", r"que $X\times_{\boldsymbol{k}} Y$ soit",
    "Wrong-font sort (GLOBAL_ISSUES 29 practice: reproduced in the diplomatic text).",
    corrected=r"que $X\times_k Y$ soit")
add(56, "Corollaire (4.2.6), l. 2: 'Soit (Z'_λ) (resp. (Z''_μ)) la famille des sous-préschémas'", "'(resp. (Z''_μ))' upright",
    "'resp.' and the outer closing parenthesis italic", "convention", 6, "high",
    r"(resp.|NL|$(Z''_\mu)$) la famille des sous-préschémas", r"\textup{(resp.|NL|$(Z''_\mu)$)} la famille des sous-préschémas")
add(56, "Corollaire (4.2.6), l. 3: 'réduits de X (resp. Y) ayant'", "'(resp. Y)' upright", "italic", "convention", 6, "high",
    r"réduits de $X$ (resp. $Y$) ayant|NL|pour", r"réduits de $X$ \textup{(resp. $Y$)} ayant|NL|pour")
add(56, "Corollaire (4.2.6), l. 3: 'irréductibles de X (resp. Y).'", "'(resp. Y)' upright", "italic", "convention", 6, "high",
    r"irréductibles de $X$ (resp. $Y$).|NL|Alors", r"irréductibles de $X$ \textup{(resp. $Y$)}.|NL|Alors")
add(56, "proof of (4.2.6): '(I, 5.1.8)'", "(I, 5.1.8) with a bold I", "plain I", "convention", 2, "high",
    r"(I, 5.1.8)", r"(\textbf{I}, 5.1.8)")
add(56, "before Proposition (4.2.7): 'le spectre d'une extension K de k'", "'extension' italic", "roman",
    "italics", None, "high",
    r"d'une|NL|extension $K$ de $k$~:", r"d'une|NL|\emph{extension} $K$ de $k$~:")
add(56, "Proposition (4.2.7), label (i)", "label (i) upright", "\\item[(i)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(56, "Proposition (4.2.7), label (ii)", "label (ii) upright", "\\item[(ii)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")

# ---------------- page 57 ----------------
add(57, "Proposition (4.2.7), label (iii)", "label (iii) upright", "\\item[(iii)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", "GLOBAL_ISSUES 16.")
add(57, "Proposition (4.2.7), label (iv)", "label (iv) upright", "\\item[(iv)] comes out italic in the italic proposition",
    "convention", 6, "high", r"\item[(iv)]", r"\item[\textup{(iv)}]", "GLOBAL_ISSUES 16.")
add(57, "Proposition (4.2.9), l. 1: 'les hypothèses de (4.2.5),'", "reference upright inside the italic statement",
    "italic in the proposition environment", "convention", 6, "high",
    r"hypothèses de (4.2.5), et supposons", r"hypothèses de \textup{(4.2.5)}, et supposons")
add(57, "Proposition (4.2.9), l. 4: 'Ass(𝓕_λ⊗_k𝓖_μ) (3.2.5). Alors'", "reference upright inside the italic statement",
    "italic in the proposition environment", "convention", 6, "high",
    r"|NL|(3.2.5). Alors", r"|NL|\textup{(3.2.5)}. Alors")
add(57, "Proposition (4.2.9), l. 5: '(pour tous les triplets (λ, μ, ν))'", "both outer parentheses upright, 'pour tous les triplets' italic (enlarged crop)",
    "outer parentheses italic", "convention", 6, "medium",
    r"(pour tous les triplets|NL|$(\lambda,\mu,\nu)$)", r"\textup{(}pour tous les triplets|NL|$(\lambda,\mu,\nu)$\textup{)}")
add(57, "proof of (4.2.9): 'que l'homomorphisme canonique 𝓕⊗_k𝓖 → ⊕_{λ,μ,ν} 𝓗_{λμν} est injectif'",
    "formula in the running text (same line as 'l'homomorphisme canonique' and 'est injectif')",
    "displayed with \\[ ... \\]", "formula", None, "high",
    r"l'homomorphisme canonique|NL|\[|NL|\mathcal F\otimes_k\mathcal G|NL|\longrightarrow\bigoplus_{\lambda,\mu,\nu}\mathcal H_{\lambda\mu\nu}|NL|\]|NL|est injectif~;",
    r"l'homomorphisme canonique|NL|$\mathcal F\otimes_k\mathcal G|NL|\longrightarrow\bigoplus_{\lambda,\mu,\nu}\mathcal H_{\lambda\mu\nu}$|NL|est injectif~;",
    "Connecting words unchanged; display turned inline.")
add(57, "proof of (4.2.9): 'il est composé des homomorphismes 𝓕⊗_k𝓖 → ⊕_{λ,μ}(𝓕_λ⊗_k𝓖_μ) → ⊕_{λ,μ,ν} 𝓗_{λμν} ; le second'",
    "formula in the running text; the middle term is ⊕_{λ,μ}(𝓕_λ⊗_k𝓖_μ) (enlarged crop)",
    "displayed; middle term (⊕_λ 𝓕_λ)⊗_k(⊕_μ 𝓖_μ)", "formula", None, "high",
    r"des homomorphismes|NL|\[|NL|\mathcal F\otimes_k\mathcal G|NL|\longrightarrow|NL|\left(\bigoplus_\lambda\mathcal F_\lambda\right)\otimes_k|NL|\left(\bigoplus_\mu\mathcal G_\mu\right)|NL|\longrightarrow\bigoplus_{\lambda,\mu,\nu}\mathcal H_{\lambda\mu\nu}~;|NL|\]|NL|le second",
    r"des homomorphismes|NL|$\mathcal F\otimes_k\mathcal G|NL|\longrightarrow\bigoplus_{\lambda,\mu}(\mathcal F_\lambda\otimes_k\mathcal G_\mu)|NL|\longrightarrow\bigoplus_{\lambda,\mu,\nu}\mathcal H_{\lambda\mu\nu}$~;|NL|le second",
    "Two differences in one edit: the TeX rewrote the middle term (an equivalent but different formula) and displayed what the print sets inline.")
add(57, "proof of (4.2.9): '(on se souviendra que 𝓕 et 𝓖 sont plats sur k)'", "only 'plats' italic; 'sur' roman",
    "\\emph{plats sur $k$} ('sur' italic)", "italics", None, "high",
    r"\emph{plats sur $k$}", r"\emph{plats} sur $k$")
add(57, "proof of (4.2.9), last line: 'forment une partition de Ass(𝓕⊗𝓖)'",
    "Ass(𝓕⊗𝓖), tensor sign without the subscript k (elsewhere 𝓕⊗_k𝓖)",
    "\\operatorname{Ass}(\\mathcal F\\otimes\\mathcal G): keeps the printed reading", "misprint_in_print", None, "low",
    None, None,
    "Probably an omitted subscript; the corrected edition may also keep the printed reading.",
    corrected=r"\operatorname{Ass}(\mathcal F\otimes_k\mathcal G)")
add(57, "Corollaire (4.2.10), l. 1: 'Sous les hypothèses de (4.2.7),'", "reference upright inside the italic statement",
    "italic in the corollary environment", "convention", 6, "high",
    r"hypothèses de (4.2.7), supposons", r"hypothèses de \textup{(4.2.7)}, supposons")

# ---------------- page 58 ----------------
add(58, "heading 4.3", "'4.3. Rappels sur les produits tensoriels de corps.' (final full stop)",
    "\\subsection{Rappels sur les produits tensoriels de corps} (no full stop)", "punctuation", None, "high",
    r"\subsection{Rappels sur les produits tensoriels de corps}", r"\subsection{Rappels sur les produits tensoriels de corps.}",
    "GLOBAL_ISSUES 43/58.")
add(58, "Proposition (4.3.2): 'k(ξ) est une extension primaire de K'", "bold italic k in k(ξ)", "plain k",
    "convention", 1, "high", r"$k(\xi)$", r"$\boldsymbol{k}(\xi)$")
add(58, "Corollaire (4.3.3): '(i.e. si sa clôture algébrique est radicielle sur k)'",
    "'(i.e.' roman and the closing parenthesis upright; the rest italic (enlarged crop)",
    "all italic in the corollary", "convention", 6, "high",
    r"(i.e. si sa clôture algébrique est radicielle sur|NL|$k$),",
    r"\textup{(i.e.} si sa clôture algébrique est radicielle sur|NL|$k$\textup{)},")
add(58, "Corollaire (4.3.4): '(parfois appelée la fermeture algébrique séparable de k dans L)'",
    "'(parfois appelée la', 'de', 'dans' and the parentheses roman; only 'fermeture algébrique séparable' italic (enlarged crop)",
    "inside the italic corollary the parenthesis is italic and \\emph sets 'fermeture algébrique séparable' upright: the reverse of the print",
    "convention", 6, "high",
    r"(parfois appelée la|NL|\emph{fermeture algébrique séparable} de $k$ dans $L$)",
    r"\textup{(parfois appelée la|NL|\emph{fermeture algébrique séparable} de $k$ dans $L$)}",
    "Inside \\textup the \\emph turns italic, as printed.")
add(58, "Corollaire (4.3.7), l. 2: 'soit finie sur k ; alors les corps résiduels'", "semicolon after 'sur k' (enlarged crop)",
    "comma", "punctuation", None, "high",
    r"soit finie sur $k$, alors", r"soit finie sur $k$~; alors")

# ---------------- page 59 ----------------
add(59, "heading 4.4", "'4.4. Préschémas irréductibles et préschémas connexes sur un corps algébriquement clos.' (final full stop)",
    "\\subsection{...algébriquement clos} (no full stop)", "punctuation", None, "high",
    r"algébriquement clos}", r"algébriquement clos.}", "GLOBAL_ISSUES 43/58.")
add(59, "(4.4.1), 2nd paragraph: 'lorsque X est de type fini sur k'", "only 'de type fini' italic; 'sur' roman (enlarged crop)",
    "\\emph{de type fini sur $k$} ('sur' italic)", "italics", None, "high",
    r"\emph{de type fini sur|NL|$k$}", r"\emph{de type fini} sur|NL|$k$")
add(59, "(4.4.1): '(I, 5.1.8)'", "(I, 5.1.8) with a bold I", "plain I", "convention", 2, "high",
    r"(I, 5.1.8)", r"(\textbf{I}, 5.1.8)")
add(59, "Lemme (4.4.2), label (i)", "label (i) upright", "\\item[(i)] comes out italic in the italic lemma",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(59, "Lemme (4.4.2) (i): '(resp. telle que'", "'(resp.' roman inside the italic statement", "italic",
    "convention", 6, "high",
    r"ouverte (resp. telle que", r"ouverte \textup{(resp.} telle que",
    "Opening half of the parenthesis; the closing parenthesis is the next finding.")
add(59, "Lemme (4.4.2) (i): 'définie par f).'", "closing parenthesis upright (enlarged crop)", "italic",
    "convention", 6, "medium",
    r"définie par $f$).", r"définie par $f$\textup{)}.")
add(59, "Lemme (4.4.2) (i): 'au quotient de X par la relation d'équivalence définie par f'",
    "'au quotient de X par la relation': X without a prime (enlarged crop, compared with the X' of 'Soient X', X')",
    "$X'$ (silently corrected)", "misprint_in_print", None, "high",
    r"de $X'$ par la relation", r"de $X$ par la relation",
    "The equivalence relation defined by f: X'->X lives on X'; X is the quotient of X'.",
    corrected=r"de $X'$ par la relation")

out = r"user\Documents\ega_scan_check_20261101\run_IV2\findings_055_059.json"
with open(out, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
