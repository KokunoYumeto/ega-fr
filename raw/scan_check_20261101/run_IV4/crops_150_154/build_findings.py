"""Build findings_150_154.json and check every fix's 'old'.

Checks: 'old' occurs exactly once in page_NNN.tex (LF), and exactly once in the
current source segment of the page at the moment it is applied (fixes of a page
applied in list order, as apply_fixes.py does). Writes nothing to any .tex file.
"""
import json
import re

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
       r"\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN + r"\findings_150_154.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 150
add(150, "Proposition (18.8.18), label '(i)'", "upright (i)", "\\item[(i)] in the italic statement (italic label)",
    "convention", 6, "high",
    r"\item[(i)] Toute limite", r"\item[\textup{(i)}] Toute limite",
    "GLOBAL_ISSUES 16. The parentheses inside (i)-(iii) ('(où les homomorphismes ...)', '(où les morphismes ...)', "
    "'(les homomorphismes ...)') are italic in the print, as in the TeX (crops p150_italparen.png, p150_ii_open.png, "
    "p150_ii_close.png, p150_iii_line2.png).")
add(150, "Proposition (18.8.18), label '(ii)'", "upright (ii)", "italic label", "convention", 6, "high",
    r"\item[(ii)] Le foncteur", r"\item[\textup{(ii)}] Le foncteur", "GLOBAL_ISSUES 16.")
add(150, "Proposition (18.8.18), label '(iii)'", "upright (iii)", "italic label", "convention", 6, "high",
    r"\item[(iii)] Tout anneau", r"\item[\textup{(iii)}] Tout anneau", "GLOBAL_ISSUES 16.")
add(150, "Théorème (18.9.1): '... géométriquement intègres (donc géométriquement connexes).'",
    "'(donc' roman with an upright parenthesis, 'géométriquement connexes' italic, closing parenthesis upright "
    "(crops p150_donc1.png, p150_donc2.png, p150_donc3.png)",
    "whole parenthesis italic (statement environment)", "convention", 6, "high",
    r"intègres (donc géométriquement connexes).",
    r"intègres \textup{(donc} géométriquement connexes\textup{)}.",
    "Same pattern as Proposition (18.5.10), p. 130. The closing parenthesis was compared with italic and roman ones "
    "on the same page: it is upright.")
add(150, "Corollaire (18.9.3): 'Sous les hypothèses de (18.9.2), le corps ...'", "reference upright (crop p150_1893.png)",
    "italic (statement environment)", "convention", 6, "high",
    r"hypothèses de (18.9.2), le corps", r"hypothèses de \textup{(18.9.2)}, le corps", "")
add(150, "Corollaire (18.9.4): '(par exemple un anneau local noethérien hensélien et excellent), et posons'",
    "'(par exemple un anneau local noethérien hensélien et' roman to the end of the line; after the line break "
    "'excellent' italic; both parentheses upright (crops p150_parex1.png - p150_parex4.png)",
    "whole parenthesis italic (statement environment)", "convention", 6, "high",
    r"normales (par exemple un anneau local noethérien hensélien et excellent), et posons",
    r"normales \textup{(par exemple un anneau local noethérien hensélien et} excellent\textup{)}, et posons",
    "Fixed by the print: the face changes back to italic after the line break, as printed; the closing parenthesis "
    "is upright (measured against the italic parenthesis of '(... locaux)' in (18.8.18)).")
add(150, "Corollaire (18.9.4): 'Alors l'application U ⇝ g^{-1}(U) est une bijection'",
    "wavy arrow (crop p150_leadsto.png)", "\\mapsto", "symbol", None, "high",
    r"$U\mapsto g^{-1}(U)$", r"$U\leadsto g^{-1}(U)$", "Wavy arrow (\\leadsto), not convention 3.")
add(150, "proof of (18.9.4): '... par la relation d'équivalence définie par f.'",
    "'définie par f.' (italic f; crop p150_parf.png)", "'définie par $g$' (silent correction)",
    "misprint_in_print", None, "high",
    r"définie par $g$", r"définie par $f$",
    "The equivalence relation is the one defined by the projection g : X′ → X of (18.9.4); no f occurs in the "
    "corollary or its proof. The fix restores the printed f; only the letter changes.",
    corrected=r"définie par $g$")
add(150, "proof of (18.9.4): 'les fibres de g sont connexes, d'où aussitôt notre assertion'",
    "'connexes' italic (crop p150_connexes.png)", "upright", "italics", None, "high",
    r"les fibres de $g$ sont connexes,", r"les fibres de $g$ sont \emph{connexes},", "")
add(150, "end of p. 150: page break 150/151 inside '(qui est ouverte et fermée | dans X)'",
    "p. 151 begins mid-sentence with 'dans X), g^{-1}(U) est connexe'", "blank lines before and after \\oldpage[IV-4]{151}",
    "marker", None, "high",
    "(qui est ouverte et fermée" + NL + NL, "(qui est ouverte et fermée" + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 151 finding removes the blank line after "
    "\\oldpage[IV-4]{151}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------------------------------------------------------- page 151
add(151, "top of p. 151: page break 150/151", "mid-sentence continuation 'dans X), ...'",
    "blank line after \\oldpage[IV-4]{151}", "marker", None, "high",
    r"\oldpage[IV-4]{151}" + NL + NL + r"dans $X$)", r"\oldpage[IV-4]{151}" + NL + r"dans $X$)",
    "Part 2 of 2 with the last p. 150 finding; both blank lines must go.")
add(151, "Corollaire (18.9.5): 'Sous les hypothèses de (18.9.4), le foncteur'", "reference upright (crop p151_1895.png)",
    "italic (statement environment)", "convention", 6, "high",
    r"hypothèses de (18.9.4), le foncteur", r"hypothèses de \textup{(18.9.4)}, le foncteur", "")
add(151, "display (18.9.5.1): 'Z ⇝ Z ⊗_A A′'", "wavy arrow (crop p151_1895.png)", "\\longmapsto", "symbol", None, "high",
    r"Z\longmapsto Z\otimes_A A'", r"Z\leadsto Z\otimes_A A'", "Wavy arrow (\\leadsto), not convention 3.")
add(151, "proof of (18.9.5): 'le graphe Γ′ d'un X′-morphisme Z′_1 → Z′_2 qui est ouvert (17.9.3) dans Z′_1 ×_X′ Z′_2 est de la forme'",
    "no comma after 'Z′_1 → Z′_2' (crop p151_ouvert.png)", "'$Z'_1\\to Z'_2$, qui'", "punctuation", None, "high",
    r"Z'_2$, qui", r"Z'_2$ qui",
    "The TeX adds two commas around 'qui est ouvert (17.9.3) dans ...'; this is the first. Adjacent to (not "
    "overlapping) the next two findings.")
add(151, "same sentence: 'qui est ouvert (17.9.3)'", "'ouvert' italic (crop p151_ouvert.png)", "upright",
    "italics", None, "high",
    r"est ouvert (17.9.3)", r"est \emph{ouvert} (17.9.3)", "")
add(151, "same sentence: 'dans Z′_1 ×_X′ Z′_2 est de la forme Γ ⊗_A A′'", "no comma before 'est de la forme'",
    "'$Z'_1\\times_{X'}Z'_2$, est de la forme'", "punctuation", None, "high",
    r"Z'_2$, est de la forme", r"Z'_2$ est de la forme", "The second comma the TeX adds.")
add(151, "proof of (18.9.5): 'la caractérisation des graphes de morphismes (I, 5.3)'",
    "bold I followed by a comma (crop p151_I53.png)", "plain I", "convention", 2, "high",
    r"(I, 5.3)", r"(\textbf{I}, 5.3)",
    "Genuine EGA I reference (bold I followed by a comma), not EGA IV's own (1.5.3).")
add(151, "proof of (18.9.5): 'changement de base Spec(k(x)) → X'", "bold italic k (crop p151_kx.png)", "plain k",
    "convention", 1, "high",
    r"$\Spec(k(x))\to X$", r"$\Spec(\boldsymbol{k}(x))\to X$", "")
add(151, "proof of (18.9.5): 'séparé sur X (17.6.2, c′))'",
    "label c′) italic including its parenthesis; the reference's closing parenthesis upright (crop p151_c2.png)",
    "'$c'$)' (italic c′, upright parenthesis)", "italics", None, "high",
    r"(17.6.2, $c'$))", r"(17.6.2, \emph{c$'$)})", "GLOBAL_ISSUES 88; prime written c$'$ as in the edition's fixed labels.")

# ---------------------------------------------------------------- page 152
add(152, "Théorème (18.9.7), label '(i)'", "upright (i) (crop p152_thm2.png)", "italic label", "convention", 6, "high",
    r"\item[(i)] $f$ est plat", r"\item[\textup{(i)}] $f$ est plat", "GLOBAL_ISSUES 16.")
add(152, "Théorème (18.9.7) (i): 'X_y = f^{-1}(y) (y ∈ Y)'", "parentheses upright (crop p152_yinY.png)",
    "italic parentheses (text in the statement environment)", "convention", 6, "high",
    r"$X_y=f^{-1}(y)$ ($y\in Y$) sont", r"$X_y=f^{-1}(y)$ \textup{(}$y\in Y$\textup{)} sont",
    "Parentheses around a formula inside an italic statement, upright in the print (GLOBAL_ISSUES 26/96).")
add(152, "Théorème (18.9.7) (i): 'géométriquement réduites (4.6.2).'", "reference upright", "italic",
    "convention", 6, "high",
    r"réduites (4.6.2).", r"réduites \textup{(4.6.2)}.", "")
add(152, "Théorème (18.9.7), label '(ii)' and 'Ou bien'", "upright (ii); 'Ou bien' roman (crop p152_thm2.png)",
    "italic label and words", "convention", 6, "high",
    r"\item[(ii)] Ou bien l'anneau", r"\item[\textup{(ii)}] \textup{Ou bien} l'anneau",
    "Two convention-6 items in one edit: the label (GLOBAL_ISSUES 16) and the roman 'Ou bien'; 'l'anneau A' is italic.")
add(152, "Théorème (18.9.7) (ii): 'géométriquement unibranche (0, 23.2.1), ou bien l'anneau A'",
    "reference upright, 'ou bien' roman (crops p152_thm2.png, p152_0231.png)", "italic", "convention", 6, "high",
    r"unibranche (0, 23.2.1), ou bien l'anneau", r"unibranche \textup{(0, 23.2.1), ou bien} l'anneau",
    "Apply THIS one before the next finding (bold 0): its 'old' contains the next one's 'old', which this edit "
    "leaves unchanged inside \\textup.")
add(152, "Théorème (18.9.7) (ii): first '(0, 23.2.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 23.2.1), ou bien", r"(\textbf{0}, 23.2.1), ou bien",
    "Apply after the previous finding (\\textup around the same spot); this 'old' occurs exactly once before and after it.")
add(152, "Théorème (18.9.7) (ii): 'est unibranche (0, 23.2.1) et k(B)'", "reference upright with a bold 0",
    "italic reference, plain 0", "convention", 6, "high",
    r"est unibranche (0, 23.2.1) et", r"est unibranche \textup{(\textbf{0}, 23.2.1)} et",
    "One edit for two differences at the same characters: the upright reference (convention 6) and the bold 0 "
    "(convention 2; count it there too). A separate bold-0 edit cannot keep a unique 'old' once \\textup is inserted.")
add(152, "Théorème (18.9.7) (ii): 'et k(B) est une extension primaire'", "bold italic k", "plain k",
    "convention", 1, "high",
    r"$k(B)$ est une extension", r"$\boldsymbol{k}(B)$ est une extension", "")
add(152, "Théorème (18.9.7) (ii): 'extension primaire (4.3.1) de k(A)'", "reference upright", "italic",
    "convention", 6, "high",
    r"primaire (4.3.1)", r"primaire \textup{(4.3.1)}", "")
add(152, "Théorème (18.9.7) (ii): '... de k(A).'", "bold italic k", "plain k", "convention", 1, "high",
    r"$k(A)$.", r"$\boldsymbol{k}(A)$.", "")
add(152, "Théorème (18.9.7): 'Alors, si η est le point générique de Y, ...' after the list",
    "'Alors' opens an indented paragraph (crop p152_thm3.png)",
    "text follows \\end{enumerate} without a blank line, so it is set without indent", "other", None, "high",
    r"\end{enumerate}" + NL + r"Alors, si $\eta$", r"\end{enumerate}" + NL + NL + r"Alors, si $\eta$",
    "Paragraph break as in GLOBAL_ISSUES 80.")
add(152, "Théorème (18.9.7): 'telle que f(T) soit rare dans Y, X—T est connexe.'", "long dash X—T", "minus sign",
    "convention", 7, "high",
    r"dans $Y$, $X-T$ est connexe.", r"dans $Y$, $X\setmin T$ est connexe.", "\\setmin as in the earlier IV-4 fixes.")
add(152, "proof of (18.9.7): 'l'hypothèse que f(T) est rare entraîne que f(T)‾ ne contient pas η'",
    "bar over the second f(T) (closure; crop p152_proof1.png)", "'$f(T)$' without the bar", "formula", None, "high",
    r"entraîne que $f(T)$ ne contient", r"entraîne que $\overline{f(T)}$ ne contient", "")
add(152, "proof of (18.9.7): 'comme {η} est proconstructible (1.9.6)'",
    "(1.9.6): old-style 1, no comma (crop p152_proof2.png)", "(I, 9.6)", "number", None, "high",
    r"proconstructible (I, 9.6)", r"proconstructible (1.9.6)",
    "The § 18 misreading of (1.x.y) as (I, x.y) (GLOBAL_ISSUES 78).")
add(152, "proof of (18.9.7): 'il en est de même de X—T qui le contient'", "long dash", "minus sign",
    "convention", 7, "high",
    r"de même de $X-T$ qui le contient", r"de même de $X\setmin T$ qui le contient", "")
add(152, "proof of (18.9.7): 'induits sur les ouverts f^{-1}(U) de X (8.1.2, a))'",
    "label a) italic including its parenthesis (crop p152_proof3.png)", "'$a)$'", "italics", None, "high",
    r"(8.1.2, $a)$)", r"(8.1.2, \emph{a)})", "GLOBAL_ISSUES 88.")
add(152, "proof of (18.9.7): 'si l'on suppose que X—T est connexe pour toute partie fermée'", "long dash", "minus sign",
    "convention", 7, "high",
    r"que $X-T$ est connexe pour toute", r"que $X\setmin T$ est connexe pour toute", "")
add(152, "proof of (18.9.7): 'une sous-A-algèbre finie A″ de K'", "'finie' italic (crop p152_finie.png)", "upright",
    "italics", None, "high",
    r"sous-$A$-algèbre finie $A''$", r"sous-$A$-algèbre \emph{finie} $A''$", "")
add(152, "proof of (18.9.7): 'Spec(A′) → Spec(A″) soit radiciel'", "'radiciel' italic (crop p152_rad.png)", "upright",
    "italics", None, "high",
    r"soit radiciel", r"soit \emph{radiciel}", "Adjacent to (not overlapping) the next finding.")
add(152, "proof of (18.9.7): '(0, 23.2.5)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 23.2.5)", r"(\textbf{0}, 23.2.5)", "")
add(152, "proof of (18.9.7): 'que Spec(A″) est géométriquement unibranche.'", "italic (crop p152_rad.png)", "upright",
    "italics", None, "high",
    r"est géométriquement unibranche. Comme", r"est \emph{géométriquement unibranche}. Comme", "")
add(152, "proof of (18.9.7): 'B″ = B ⊗_A A″ est aussi un anneau local.'", "'local' italic", "upright",
    "italics", None, "high",
    r"est aussi un anneau local.", r"est aussi un anneau \emph{local}.", "")
add(152, "last line: 'les points de Spec(k(B) ⊗_k(A) k″)'",
    "bold italic k in k(B); bold upright k in the subscript k(A); light italic k″ (crop p152_last.png)", "plain k (both)",
    "convention", 1, "high",
    r"\Spec(k(B)\otimes_{k(A)}k'')", r"\Spec(\boldsymbol{k}(B)\otimes_{\mathbf{k}(A)}k'')",
    "One edit for both k (GLOBAL_ISSUES 48: bold upright in the subscript, bold italic on the line).")
add(152, "last line: '(I, 3.4.9)'", "bold I followed by a comma", "plain I", "convention", 2, "high",
    r"(I, 3.4.9)", r"(\textbf{I}, 3.4.9)",
    "Genuine EGA I reference, not EGA IV's own (1.3.4.9). Shares '3.4.9)' with the next finding's 'old'; either order works.")
add(152, "end of p. 152: page break 152/153 inside '... (I, 3.4.9) | puisque le point fermé'",
    "p. 153 begins mid-sentence with 'puisque'", "blank lines before and after \\oldpage[IV-4]{153}",
    "marker", None, "high",
    "3.4.9)" + NL + NL, "3.4.9)" + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 153 finding removes the blank line after "
    "\\oldpage[IV-4]{153}; apply both.")

# ---------------------------------------------------------------- page 153
add(153, "top of p. 153: page break 152/153", "mid-sentence continuation 'puisque le point fermé ...'",
    "blank line after \\oldpage[IV-4]{153}", "marker", None, "high",
    r"\oldpage[IV-4]{153}" + NL + NL + "puisque", r"\oldpage[IV-4]{153}" + NL + "puisque",
    "Part 2 of 2 with the last p. 152 finding; both blank lines must go.")
add(153, "'k″ est une extension radicielle de k(A)'", "bold italic k (crop p153_k1.png)", "plain k", "convention", 1, "high",
    r"radicielle de $k(A)$", r"radicielle de $\boldsymbol{k}(A)$", "")
add(153, "'donc Spec(k(B) ⊗_k(A) k″) est radiciel'", "bold italic k(B), bold upright subscript k(A)", "plain k (both)",
    "convention", 1, "high",
    r"\Spec(k(B)\otimes_{k(A)}k'')$ est radiciel", r"\Spec(\boldsymbol{k}(B)\otimes_{\mathbf{k}(A)}k'')$ est radiciel",
    "GLOBAL_ISSUES 48 (subscript k bold upright).")
add(153, "'radiciel sur Spec(k(B))'", "bold italic k", "plain k", "convention", 1, "high",
    r"sur $\Spec(k(B))$", r"sur $\Spec(\boldsymbol{k}(B))$", "")
add(153, "'Lorsque A est unibranche et k(B) extension primaire de k(A)'", "bold italic k (twice)", "plain k (twice)",
    "convention", 1, "high",
    r"et $k(B)$ extension primaire de $k(A)$", r"et $\boldsymbol{k}(B)$ extension primaire de $\boldsymbol{k}(A)$",
    "Two occurrences in one edit.")
add(153, "'Spec(k(B) ⊗_k(A) k″) est irréductible (4.3.2)'", "bold italic k(B), bold upright subscript k(A)",
    "plain k (both)", "convention", 1, "high",
    r"\Spec(k(B)\otimes_{k(A)}k'')$ est irréductible",
    r"\Spec(\boldsymbol{k}(B)\otimes_{\mathbf{k}(A)}k'')$ est irréductible", "GLOBAL_ISSUES 48.")
add(153, "'un espace fini et discret (I, 6.4.4)'", "bold I followed by a comma (crop p153_k2.png)", "plain I",
    "convention", 2, "high",
    r"(I, 6.4.4)", r"(\textbf{I}, 6.4.4)", "Genuine EGA I reference, not EGA IV's own (1.6.4.4).")
add(153, "'dans les deux cas envisagés B″ est local.'", "'local' italic", "upright", "italics", None, "high",
    r"$B''$ est local.", r"$B''$ est \emph{local}.", "")
add(153, "'k(η″) = k(η) = K par définition'", "bold italic k (twice) (crop p153_eta.png)", "plain k (twice)",
    "convention", 1, "high",
    r"$k(\eta'')=k(\eta)=K$", r"$\boldsymbol{k}(\eta'')=\boldsymbol{k}(\eta)=K$", "Two occurrences in one edit.")
add(153, "Remarque (18.9.7.1): 'par définition (0, 23.1.1)'", "bold 0 (crop p153_remark.png)", "plain 0",
    "convention", 2, "high",
    r"(0, 23.1.1)", r"(\textbf{0}, 23.1.1)", "")
add(153, "(18.9.7.2): 'pour prouver que X—T est connexe'", "long dash", "minus sign", "convention", 7, "high",
    r"prouver que $X-T$ est connexe", r"prouver que $X\setmin T$ est connexe", "")
add(153, "(18.9.7.2): 'Spec(O_X,x)—{x} est connexe'", "long dash (crop p153_connexe.png)", "minus sign",
    "convention", 7, "high",
    r"\Spec(\sh{O}_{X,x})-\{x\}", r"\Spec(\sh{O}_{X,x})\setmin\{x\}", "")
add(153, "(18.9.7.2): '... —{x} est connexe. Posons'", "'connexe' italic (crop p153_connexe.png)", "upright",
    "italics", None, "high",
    r"est connexe. Posons", r"est \emph{connexe}. Posons", "")
add(153, "Lemme (18.9.7.3), label '(i)'", "upright (i) (crop p153_lemma.png)", "italic label", "convention", 6, "high",
    r"\item[(i)] $f$ est plat", r"\item[\textup{(i)}] $f$ est plat", "GLOBAL_ISSUES 16.")
add(153, "Lemme (18.9.7.3) (i): 'X_y (y ∈ Y)'", "parentheses upright (crop p153_yinY.png)", "italic parentheses",
    "convention", 6, "high",
    r"$X_y$ ($y\in Y$) sont", r"$X_y$ \textup{(}$y\in Y$\textup{)} sont", "GLOBAL_ISSUES 26/96.")
add(153, "Lemme (18.9.7.3), label '(ii)'", "upright (ii)", "italic label", "convention", 6, "high",
    r"\item[(ii)] $A$ est intègre", r"\item[\textup{(ii)}] $A$ est intègre", "GLOBAL_ISSUES 16.")
add(153, "Lemme (18.9.7.3): 'Alors, si b est le point fermé de X, ...' after the list",
    "'Alors' opens an indented paragraph (crop p153_lemma.png)",
    "text follows \\end{enumerate} without a blank line, so it is set without indent", "other", None, "high",
    r"\end{enumerate}" + NL + r"Alors, si $b$", r"\end{enumerate}" + NL + NL + r"Alors, si $b$",
    "Paragraph break as in GLOBAL_ISSUES 80.")
add(153, "Lemme (18.9.7.3): 'X—{b} est connexe.'", "long dash", "minus sign", "convention", 7, "high",
    r"de $X$, $X-\{b\}$ est connexe.", r"de $X$, $X\setmin\{b\}$ est connexe.", "")
add(153, "proof of (18.9.7.3): 'théorème de Hartshorne (5.10.7), X—{b} est connexe'", "long dash", "minus sign",
    "convention", 7, "high",
    r"(5.10.7), $X-\{b\}$", r"(5.10.7), $X\setmin\{b\}$", "")
add(153, "proof of (18.9.7.3): 'un corps (0, 16.4.7)'", "bold 0 (crop p153_end.png)", "plain 0", "convention", 2, "high",
    r"(0, 16.4.7)", r"(\textbf{0}, 16.4.7)", "")
add(153, "A): 'on a prof(A) ≥ 2 (0, 16.5.1)'", "bold 0 (crop p153_end.png)", "plain 0", "convention", 2, "high",
    r"(0, 16.5.1)", r"(\textbf{0}, 16.5.1)", "")
add(153, "end of p. 153: page break 153/154 inside '... et puisque B ⊗_A k | est un corps'",
    "p. 154 begins mid-sentence with 'est un corps'", "blank lines before and after \\oldpage[IV-4]{154}",
    "marker", None, "high",
    r"et puisque $B\otimes_A k$" + NL + NL, r"et puisque $B\otimes_A k$" + NL,
    "The marker is at the right place. Part 1 of 2: the first p. 154 finding removes the blank line after "
    "\\oldpage[IV-4]{154}; apply both.")

# ---------------------------------------------------------------- page 154
add(154, "top of p. 154: page break 153/154", "mid-sentence continuation 'est un corps et que f est plat'",
    "blank line after \\oldpage[IV-4]{154}", "marker", None, "high",
    r"\oldpage[IV-4]{154}" + NL + NL + "est un corps", r"\oldpage[IV-4]{154}" + NL + "est un corps",
    "Part 2 of 2 with the last p. 153 finding; both blank lines must go.")
add(154, "first line: 'B est régulier (0, 17.3.3)'", "bold 0 (crop p154_top.png)", "plain 0", "convention", 2, "high",
    r"(0, 17.3.3)", r"(\textbf{0}, 17.3.3)", "")
add(154, "'Mais alors X—{b} est réduit à un seul point'", "long dash", "minus sign", "convention", 7, "high",
    r"Mais alors $X-\{b\}$", r"Mais alors $X\setmin\{b\}$", "")
add(154, "Lemme (18.9.7.5): 'soient S l'ensemble des points fermés de X et U = X—S.'", "long dash (crop p154_lemma.png)",
    "minus sign", "convention", 7, "high",
    r"$U=X-S$", r"$U=X\setmin S$", "")
add(154, "proof of (18.9.7.5): 'Rappelons que si p_i (1 ≤ i ≤ m) sont les idéaux minimaux de A'",
    "no article before p_i (crop p154_rappelons.png)", "'si les $\\mathfrak p_i$'", "extra", None, "high",
    r"Rappelons que si les $\mathfrak p_i$", r"Rappelons que si $\mathfrak p_i$",
    "The TeX adds 'les'; the printed sentence is grammatical without it, so this is not treated as a misprint.")
add(154, "proof of (18.9.7.5): 'Or (I, 8.2.1.1), Γ(U′, O_X′) est l'intersection'", "bold I followed by a comma (crop p154_krull.png)",
    "plain I", "convention", 2, "high",
    r"Or (I, 8.2.1.1)", r"Or (\textbf{I}, 8.2.1.1)", "Genuine EGA I reference, not EGA IV's own (1.8.2.1.1).")
add(154, "proof of (18.9.7.5): 'pour lesquels p′ est de hauteur 1'", "'de hauteur' italic (crop p154_krull.png)", "upright",
    "italics", None, "high",
    r"est de hauteur 1. Mais", r"est \emph{de hauteur} 1. Mais", "")
add(154, "proof of (18.9.7.5): 'le raisonnement de (0, 23.2.7)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 23.2.7)", r"(\textbf{0}, 23.2.7)", "")
add(154, "proof of (18.9.7.5): 'à un anneau semi-local intègre noethérien'",
    "'semi-|local' italic across the line break (crop p154_krull.png)", "upright", "italics", None, "high",
    r"à un anneau semi-local intègre", r"à un anneau \emph{semi-local} intègre", "")
add(154, "proof of (18.9.7.5): 'A′ est un anneau de Krull semi-local'",
    "'anneau de Krull' italic, 'semi-local' roman (crop p154_krull.png)", "'\\emph{anneau de Krull semi-local}'",
    "italics", None, "high",
    r"\emph{anneau de Krull semi-local}", r"\emph{anneau de Krull} semi-local", "")
add(154, "Remarque (18.9.7.6): 'On sait (0, 23.2.5)'", "bold 0 (crop p154_remark.png)", "plain 0", "convention", 2, "high",
    r"(0, 23.2.5)", r"(\textbf{0}, 23.2.5)", "")
add(154, "Remarque (18.9.7.6): 'une sous-A-algèbre finie A″'", "'finie' italic (crop p154_remark.png)", "upright",
    "italics", None, "high",
    r"sous-$A$-algèbre finie $A''$", r"sous-$A$-algèbre \emph{finie} $A''$",
    "Judged with the remark body as roman (document-wide remark item).")
add(154, "Remarque (18.9.7.6): 'donc surjectif (II, 6.1.10)'", "bold II (crop p154_remark.png)", "plain II",
    "convention", 2, "high",
    r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)", "")
add(154, "end of p. 154: page break 154/155 inside '... au-dessus de x. Cela | étant, il résulte'",
    "p. 155 begins mid-sentence with 'étant, il résulte d'abord' (crop p155_top.png)",
    "blank lines before and after \\oldpage[IV-4]{155}", "marker", None, "high",
    r"au-dessus de $x$. Cela" + NL + NL, r"au-dessus de $x$. Cela" + NL,
    "The marker is at the right place. Part 1 of 2: the blank line AFTER \\oldpage[IV-4]{155} lies in the p. 155 "
    "segment (outside these pages) and must go too: '\\oldpage[IV-4]{155}\\n\\nétant' -> '\\oldpage[IV-4]{155}\\nétant'.")


# ---------------------------------------------------------------- checks
src = open(SRC, encoding="utf-8", newline="").read()
problems = []
segs = {}
for n in range(150, 155):
    a = src.index("\\oldpage[IV-4]{%d}" % n)
    b = src.index("\\oldpage[IV-4]{%d}" % (n + 1))
    segs[n] = src[a:b]
pages = {n: open(RUN + rf"\page_{n}.tex", encoding="utf-8", newline="").read().replace("\r\n", "\n") for n in range(150, 155)}
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    n, old, new = x["page"], x["fix"]["old"], x["fix"]["new"]
    c_page = pages[n].count(old)
    c_seg = segs[n].count(old)
    c_file = src.count(old)
    if c_page != 1 or c_seg != 1:
        problems.append((i, n, old, c_page, c_seg))
    segs[n] = segs[n].replace(old, new, 1) if c_seg == 1 else segs[n]
    x["_file_count"] = c_file
report = open(RUN + r"\crops_150_154\check_report.txt", "w", encoding="utf-8")
for i, x in enumerate(F):
    if x["fix"]:
        report.write("%2d p%d file=%d %s\n" % (i, x["page"], x.pop("_file_count"), json.dumps(x["fix"]["old"], ensure_ascii=False)))
report.write("PROBLEMS: %r\n" % (problems,))
counts = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
report.write("COUNTS: %r\n" % (counts,))
report.close()
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("findings:", len(F), "problems:", len(problems))
print(counts)
