"""Build findings_205_209.json and check that every fix's old string occurs once in its page file."""
import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_205_209.json"

F = []


def add(page, where, scan, tex, kind, convention, confidence, fix, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": fix,
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 205
add(204,
    "page break 204/205 (edit 1 of 3): end of Remarques (14.3.3.1), (ii) '... tels que f' ne soit pas ouvert au point x'. | Or, si y'=f'(x') ...'",
    "p. 204 ends with the full line '... tels que f' ne soit pas ouvert au point x'.' (page_204_s4.png); p. 205 begins flush left 'Or, si y'=f'(x'), ...': remark (ii) continues on p. 205 and ends with '... qui est un voisinage de x dans f^{-1}(y).', just before Proposition (14.3.4)",
    "\\end{enumerate}, \\end{remarks} and a blank line close the remark at the end of the p. 204 segment, before \\oldpage[IV-3]{205}",
    "other", None, "high",
    {"old": r"""que $f'$ ne soit pas ouvert au point $x'$.
\end{enumerate}
\end{remarks}

""",
     "new": r"""que $f'$ ne soit pas ouvert au point $x'$.
"""},
    "OUTSIDE pp. 205-209: 'old' is the end of page_204.tex (ega4-14-fr.tex, lines 392-395). Apply together with the next two entries (edits 2 and 3 of 3), which keep the marker inside item (ii) and close the remark after 'Or, si ... f^{-1}(y).'. The pp. 200-204 checker may report part of this; apply once.")

add(205,
    "page break 204/205 (edit 2 of 3): top of p. 205, 'Or, si y'=f'(x'), la projection ...'",
    "'Or, si' flush left at the top of p. 205 (the indented lines on the page start further right, e.g. 'Proposition (14.3.4)'): no paragraph break",
    "blank line after \\oldpage[IV-3]{205}: 'Or, si' opens a new paragraph",
    "marker", None, "high",
    {"old": "\\oldpage[IV-3]{205}\n\nOr, si",
     "new": "\\oldpage[IV-3]{205}\nOr, si"},
    "Apply together with edits 1 and 3 of 3. The marker position itself is right.")

add(205,
    "page break 204/205 (edit 3 of 3): end of remark (14.3.3.1), (ii): '... qui est un voisinage de x dans f^{-1}(y).'",
    "the remark ends here; Proposition (14.3.4) follows",
    "'Or, si ... f^{-1}(y).' stands outside the remarks environment (closed at the end of p. 204)",
    "other", None, "high",
    {"old": r"""qui est un voisinage de $x$ dans
$f^{-1}(y)$.

\begin{proposition}[14.3.4]""",
     "new": r"""qui est un voisinage de $x$ dans
$f^{-1}(y)$.
\end{enumerate}
\end{remarks}

\begin{proposition}[14.3.4]"""},
    "Apply together with edits 1 and 2 of 3: the remark environment of (14.3.3.1) then ends after its last printed sentence.")

add(205,
    "Proposition (14.3.4): item labels (i)-(iv)",
    "labels (i), (ii), (iii), (iv) upright",
    "enumerate label=(\\roman*) inside the italic proposition: italic labels",
    "convention", 6, "high",
    {"old": "\\label{IV.14.3.4-fr}\n\\begin{enumerate}[label=(\\roman*)]",
     "new": "\\label{IV.14.3.4-fr}\n\\begin{enumerate}[label=\\textup{(\\roman*)}]"},
    "One edit for the four labels (GLOBAL_ISSUES 16).")

add(205,
    "Proposition (14.3.4) (iv): '(on rappelle (I, 3.6.5) que X_1 est canoniquement identifié à un sous-espace de X).'",
    "the whole parenthesis roman inside the italic statement",
    "set in the italic proposition environment",
    "convention", 6, "high",
    {"old": r"""(on rappelle (I, 3.6.5) que
  $X_1$ est canoniquement identifié à un sous-espace de $X$)""",
     "new": r"""\textup{(on rappelle (\textbf{I}, 3.6.5) que
  $X_1$ est canoniquement identifié à un sous-espace de $X$)}"""},
    "One edit for this finding and the next (convention 2, bold I).")

add(205,
    "Proposition (14.3.4) (iv): reference '(I, 3.6.5)'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    None,
    "Covered by the edit of the preceding finding (convention 6), which adds \\textbf{I}.")

add(205,
    "proof of (14.3.4): 'il suffit d'appliquer le critère (1.10.3, b)). Soient'",
    "'(1.10.3, b))': italic b followed by its own parenthesis, then the closing parenthesis of the reference (enlarged crop p205_s3_top.png)",
    "'(1.10.3, $b$).': the parenthesis of the label b) is missing",
    "punctuation", None, "high",
    {"old": "(1.10.3, $b$).",
     "new": "(1.10.3, \\emph{b)})."},
    "Same form as (8.1.2, \\emph{a)}) in the earlier IV-3 fixes.")

add(205,
    "proof of (14.3.4): 'X'_1=X'×_{Y'}Y'_1, f'_1=f'_{(Y'_1)}.'",
    "f'_1 = f'_{(Y'_1)}: the f on the right carries a prime (enlarged crop p205_s3_f1.png)",
    "$f'_1=f_{(Y'_1)}$",
    "formula", None, "high",
    {"old": "$f'_1=f_{(Y'_1)}$",
     "new": "$f'_1=f'_{(Y'_1)}$"},
    "")

add(205,
    "proof of (14.3.4): 'le morphisme composé Y'_1 → Y' -g-> Y se factorise en Y'_1 → Y_1 → Y'",
    "the second arrow carries the label g (enlarged crop p205_s3_top.png)",
    "$Y'_1\\to Y'\\to Y$ (no label)",
    "formula", None, "high",
    {"old": "$Y'_1\\to Y'\\to Y$",
     "new": "$Y'_1\\to Y'\\xrightarrow{g}Y$"},
    "")

add(205,
    "proof of (14.3.4): '(I, 2.4.4), donc X'_1 = ...'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    {"old": "(I, 2.4.4)",
     "new": "(\\textbf{I}, 2.4.4)"},
    "")

add(205,
    "Proposition (14.3.6), last sentence: '(autrement dit, il existe une composante irréductible de X' contenant x' et dominant Y').'",
    "'(autrement dit,' and the closing parenthesis roman; 'il existe ... dominant' italic",
    "the whole parenthesis italic (proposition environment)",
    "convention", 6, "high",
    {"old": r"""(autrement dit, il existe une composante irréductible de $X'$ contenant $x'$ et
dominant $Y'$).""",
     "new": r"""\textup{(autrement dit,} il existe une composante irréductible de $X'$ contenant $x'$ et
dominant $Y'$\textup{)}."""},
    "")

# ---------------------------------------------------------------- page 206
add(206,
    "Proposition (14.3.6), end: 'et où x' est rationnel sur k(y').'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "sur\n$k(y')$.",
     "new": "sur\n$\\boldsymbol{k}(y')$."},
    "")

add(206,
    "proof of (14.3.6), l. 3: 'considérons un morphisme de type fini g : Y''→U, et soient X''=X×_Y Y''' ",
    "g : Y''→U (enlarged crop p206_s1_U.png)",
    "$g:Y''\\to U$ (the printed reading)",
    "misprint_in_print", None, "low",
    None,
    "The TeX keeps the printed reading. No U is introduced in (14.3.6) or its proof, and the next lines use Y'' as a Y-scheme (X'' = X ×_Y Y'', 'Puisque Y'' est localement noethérien'); the base changes needed for (14.3.3.1, (i)) via (8.10.2) are Y-schemes of finite type, so Y is probably meant. Low confidence: U may stand for an affine open neighbourhood of y, as in the proof of (8.10.2); not in the authors' errata. The corrected edition (r20 current) also reads U. Coordinator's decision.",
    corrected="g:Y''\\to Y")

add(206,
    "proof of (14.3.6): 'une clôture algébrique de k(x'')'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "$k(x'')$",
     "new": "$\\boldsymbol{k}(x'')$"},
    "")

add(206,
    "proof of (14.3.6): 'et qui soit rationnel sur k(y') (I, 3.4.9)'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "rationnel sur $k(y')$",
     "new": "rationnel sur $\\boldsymbol{k}(y')$"},
    "")

add(206,
    "proof of (14.3.6): '(I, 3.4.9). L'hypothèse entraîne'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    {"old": "(I, 3.4.9)",
     "new": "(\\textbf{I}, 3.4.9)"},
    "")

add(206,
    "proof of (14.3.6): 'z'' est une générisation de x'' et sa projection dans Y'' est t''; on conclut donc'",
    "t'' (t with two primes; enlarged crop p206_s2_t.png)",
    "$t$ (silent correction)",
    "misprint_in_print", None, "high",
    {"old": "dans $Y''$ est $t$~;",
     "new": "dans $Y''$ est $t''$~;"},
    "The TeX silently corrects; the fix restores the printed reading. No t'' exists: t is the generization of y'' in Y'' chosen above, and since z' lies over s with g(s) = t, the projection of z'' in Y'' is t.",
    corrected="t")

add(206,
    "Corollaire (14.3.7): 'Les notations étant celles de (14.3.6) :'",
    "(14.3.6) upright in the italic statement (enlarged crop p206_s2_cor.png)",
    "italic (corollary environment)",
    "convention", 6, "high",
    {"old": "celles de (14.3.6)~:",
     "new": "celles de \\textup{(14.3.6)}~:"},
    "")

add(206,
    "Corollaire (14.3.7): item labels (i), (ii)",
    "labels (i), (ii) upright",
    "enumerate label=(\\roman*) inside the italic corollary: italic labels",
    "convention", 6, "high",
    {"old": "\\begin{enumerate}[label=(\\roman*)]",
     "new": "\\begin{enumerate}[label=\\textup{(\\roman*)}]"},
    "One edit for both labels (GLOBAL_ISSUES 16).")

add(206,
    "Proposition (14.3.8) b): 'f est universellement ouvert dans un voisinage de (f^{-1}y).'",
    "(f^{-1}y), parenthesis misplaced (enlarged crop p206_s3_b.png)",
    "$f^{-1}(y)$ (silent correction)",
    "misprint_in_print", None, "high",
    {"old": "universellement ouvert dans un voisinage de $f^{-1}(y)$.",
     "new": "universellement ouvert dans un voisinage de $(f^{-1}y)$."},
    "The TeX silently applies the authors' erratum (Err_IV, list in EGA IV part 4, p. 347: 'Ligne 10 du bas de la p. 206, remplacer (f^{-1}y) par f^{-1}(y)'; GLOBAL_ISSUES 72). The fix restores the printed reading.",
    corrected="f^{-1}(y)")

add(206,
    "proof of (14.3.8), l. 1-2: 'a) entraîne que f_red est plat dans un voisinage de f^{-1}(y) (11.1.1)'",
    "'voisinage' in italics (page_206_s4.png, first line)",
    "'voisinage' upright",
    "italics", None, "high",
    {"old": "plat dans un voisinage de",
     "new": "plat dans un \\emph{voisinage} de"},
    "")

# ---------------------------------------------------------------- page 207
add(207,
    "page break 206/207: '... X=Spec(B) affines; si X_i (1≤i≤n) sont les sous-préschémas fermés (intègres) de X ayant pour | espaces sous-jacents ...'",
    "printed p. 206 ends with the line 'affines; si X_i (1≤i≤n) sont les sous-préschémas fermés (intègres) de X ayant pour' (page_206_s4.png); p. 207 begins 'espaces sous-jacents les composantes irréductibles de X'",
    "\\oldpage[IV-3]{207} stands before 'affines~;' (one printed line too early)",
    "marker", None, "high",
    {"old": r"""\oldpage[IV-3]{207}
affines~; si $X_i$ ($1\leq i\leq n$) sont les sous-préschémas fermés (intègres)
de $X$ ayant pour espaces""",
     "new": r"""affines~; si $X_i$ ($1\leq i\leq n$) sont les sous-préschémas fermés (intègres)
de $X$ ayant pour
\oldpage[IV-3]{207}
espaces"""},
    "One atomic edit inside page_207.tex: the marker moves down one printed line, mid-sentence, on its own line without blank lines. The moved line agrees with the print of p. 206.")

add(207,
    "proof of (14.3.8): 'l'homomorphisme A→B_i est injectif (I, 1.2.7);'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    {"old": "(I, 1.2.7)",
     "new": "(\\textbf{I}, 1.2.7)"},
    "")

add(207,
    "Remarques (14.3.9) (ii): 'car il est immédiat qu'en tous les points de X sauf un le morphisme f est universellement ouvert'",
    "'sauf un' in italics (page_207_s2.png)",
    "'sauf un' plain",
    "italics", None, "high",
    {"old": "sauf un\n  le morphisme",
     "new": "\\emph{sauf un}\n  le morphisme"},
    "Judged as if the remark body were roman.")

add(207,
    "Lemme (14.3.10): 'soit X_0=X⊗_A k (resp. X_1=X⊗_A K) la fibre de f'",
    "'(resp.' and the closing parenthesis roman inside the italic statement (enlarged crop p207_s2_lemma3.png)",
    "italic (lemma environment)",
    "convention", 6, "high",
    {"old": "(resp. $X_1=X\\otimes_A K$)",
     "new": "\\textup{(resp.} $X_1=X\\otimes_A K$\\textup{)}"},
    "")

add(207,
    "Lemme (14.3.10): 'au point fermé (resp. au point générique) de S.'",
    "'(resp.' and the closing parenthesis roman, 'au point générique' italic (enlarged crop p207_s3_lemma4.png)",
    "italic (lemma environment)",
    "convention", 6, "high",
    {"old": "(resp. au point générique)",
     "new": "\\textup{(resp.} au point générique\\textup{)}"},
    "")

add(207,
    "proof of (14.3.10): 'un S-morphisme quasi-fini g : U→S[T_1, ..., T_n]=Z tel que le morphisme restriction'",
    "the formula is set inline in the running text",
    "displayed with \\[ ... \\]",
    "other", None, "high",
    {"old": r"""quasi-fini
\[
  g:U\to S[T_1,\ldots,T_n]=Z
\]
tel que""",
     "new": r"""quasi-fini
$g:U\to S[T_1,\ldots,T_n]=Z$
tel que"""},
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost or added.")

add(207,
    "proof of (14.3.10): 'Considérons alors dans Z l'ensemble fermé V(F)'",
    "'dans' in italics (page_207_s4.png)",
    "'dans' upright",
    "italics", None, "high",
    {"old": "Considérons alors dans $Z$",
     "new": "Considérons alors \\emph{dans} $Z$"},
    "")

add(207,
    "page break 207/208 (edit 1 of 2, insert): '... g(U)⊂V(F); en parti- | culier, on aurait g_0(U_0)⊂V(F)∩Z_0=V(F_0) ...'",
    "printed p. 207 ends with 'est dense dans U (puisqu'il contient le point générique de X), g(U)⊂V(F); en parti-' (page_207_s4.png); p. 208 begins 'culier, on aurait g_0(U_0)⊂V(F)∩Z_0=V(F_0); ... C.Q.F.D.' (page_208_s1.png)",
    "\\oldpage[IV-3]{208} stands after 'C.Q.F.D.', before Proposition (14.3.11): two printed lines too late",
    "marker", None, "high",
    {"old": r"""$g(U)\subset V(F)$~; en
particulier, on aurait""",
     "new": r"""$g(U)\subset V(F)$~; en
parti%
\oldpage[IV-3]{208}
culier, on aurait"""},
    "Marker move, part 1 of 2: inserts the marker at the printed word break parti-|culier (as appli%|cations, IV-3 p. 100). Apply together with the p. 208 entry that removes the old marker (part 2 of 2).")

# ---------------------------------------------------------------- page 208
add(208,
    "page break 207/208 (edit 2 of 2, remove the old marker): before Proposition (14.3.11)",
    "Proposition (14.3.11) begins below the first two lines of p. 208",
    "\\oldpage[IV-3]{208} and a blank line before \\begin{proposition}[14.3.11]",
    "marker", None, "high",
    {"old": "\\oldpage[IV-3]{208}\n\n\\begin{proposition}[14.3.11]",
     "new": "\\begin{proposition}[14.3.11]"},
    "Part 2 of 2: apply together with the p. 207 insert at parti%|culier. The blank line after 'C.Q.F.D.' stays, so the proposition still starts a new paragraph.")

add(208,
    "Proposition (14.3.11): 'posons X_s=X×_S Spec(k(s))'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "$X_s=X\\times_S\\operatorname{Spec}(k(s))$",
     "new": "$X_s=X\\times_S\\operatorname{Spec}(\\boldsymbol{k}(s))$"},
    "")

add(208,
    "Proposition (14.3.11): '(Y_λ)_s=Y_λ×_S Spec(k(s))'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "Y_\\lambda\\times_S\\operatorname{Spec}(k(s))",
     "new": "Y_\\lambda\\times_S\\operatorname{Spec}(\\boldsymbol{k}(s))"},
    "")

add(208,
    "proof of (14.3.11): 'le morphisme projection p : X_s⊗_{k(s)}k(a)→X_s', subscript k(s)",
    "bold upright k in the subscript (enlarged crop p208_s2_kk.png)",
    "plain k",
    "convention", 1, "high",
    {"old": "$p:X_s\\otimes_{k(s)}",
     "new": "$p:X_s\\otimes_{\\mathbf{k}(s)}"},
    "Bold upright in a subscript, as GLOBAL_ISSUES 48.")

add(208,
    "same formula: the factor k(a)",
    "bold italic k (same crop)",
    "plain k",
    "convention", 1, "high",
    {"old": "k(a)\\to X_s$",
     "new": "\\boldsymbol{k}(a)\\to X_s$"},
    "")

add(208,
    "proof of (14.3.11): 'un espace quotient de X_s⊗_{k(s)}k(a) par une relation', subscript k(s)",
    "bold upright k in the subscript (same crop)",
    "plain k",
    "convention", 1, "high",
    {"old": "quotient de $X_s\\otimes_{k(s)}",
     "new": "quotient de $X_s\\otimes_{\\mathbf{k}(s)}"},
    "Bold upright in a subscript, as GLOBAL_ISSUES 48.")

add(208,
    "same formula: the factor k(a)",
    "bold italic k (same crop)",
    "plain k",
    "convention", 1, "high",
    {"old": "k(a)$ par une",
     "new": "\\boldsymbol{k}(a)$ par une"},
    "")

add(208,
    "proof of (14.3.11): 'par une relation d'équivalence ouverte;'",
    "'ouverte' in italics (page_208_s2.png)",
    "'ouverte' upright",
    "italics", None, "high",
    {"old": "d'équivalence\nouverte~;",
     "new": "d'équivalence\n\\emph{ouverte}~;"},
    "")

add(208,
    "proof of (14.3.11): 'et compte tenu de (I, 3.4.8), de (4.2.7)'",
    "bold I",
    "plain I",
    "convention", 2, "high",
    {"old": "(I, 3.4.8)",
     "new": "(\\textbf{I}, 3.4.8)"},
    "")

add(208,
    "proof of (14.3.11): 'si Z désigne l'adhérence dans X de Z(s')'",
    "'dans' in italics (page_208_s2.png)",
    "'dans' upright",
    "italics", None, "high",
    {"old": "l'adhérence dans $X$ de $Z(s')$",
     "new": "l'adhérence \\emph{dans} $X$ de $Z(s')$"},
    "")

add(208,
    "Remarque (14.3.12): 'autrement dit le cas où (u_λ) est une famille de S-sections de X'",
    "'sections' in italics, 'S-' roman (page_208_s3.png)",
    "'$S$-sections' without emphasis",
    "italics", None, "high",
    {"old": "$S$-sections de $X$",
     "new": "$S$-\\emph{sections} de $X$"},
    "Judged as if the remark body were roman.")

add(208,
    "Proposition (14.3.13): 'x un point maximal de la fibre X_y=X×_Y Spec(k(y)).'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "X\\times_Y\\operatorname{Spec}(k(y))",
     "new": "X\\times_Y\\operatorname{Spec}(\\boldsymbol{k}(y))"},
    "")

add(208,
    "Proposition (14.3.13): 'Considérons les conditions suivantes :'",
    "a new indented paragraph (indented like 'a)' below it)",
    "continues the paragraph of the first sentence (no blank line)",
    "other", None, "high",
    {"old": ".\nConsidérons les conditions suivantes~:",
     "new": ".\n\nConsidérons les conditions suivantes~:"},
    "Missing paragraph break.")

add(208,
    "Proposition (14.3.13) a): '(ou encore en tout point de la composante irréductible de X_y de point générique x (14.3.3.1, (ii)))'",
    "the whole parenthesis roman inside the italic statement (page_208_s3.png, page_208_s4.png)",
    "italic (proposition environment)",
    "convention", 6, "high",
    {"old": r"""(ou encore en tout point de la
  composante irréductible de $X_y$ de point générique $x$ (14.3.3.1, (ii)))""",
     "new": r"""\textup{(ou encore en tout point de la
  composante irréductible de $X_y$ de point générique $x$ (14.3.3.1, (ii)))}"""},
    "")

add(208,
    "Proposition (14.3.13) b): '(ce qui entraîne que Z est équidimensionnelle sur Y_0 au point x (13.2.2))'",
    "the parenthesis roman inside the italic statement, with 'équidimensionnelle' italic (page_208_s4.png)",
    "the whole parenthesis italic, 'équidimensionnelle' not distinguished",
    "convention", 6, "high",
    {"old": r"""(ce qui entraîne que $Z$ est équidimensionnelle sur $Y_0$ au
  point $x$ (13.2.2))""",
     "new": r"""\textup{(ce qui entraîne que $Z$ est \emph{équidimensionnelle} sur $Y_0$ au
  point $x$ (13.2.2))}"""},
    "Inside \\textup the \\emph makes 'équidimensionnelle' italic, as printed.")

# ---------------------------------------------------------------- page 209
add(209,
    "Proposition (14.3.13), label b')",
    "label b') upright, like a) and b) (enlarged crop p209_s1_labels.png)",
    "\\item[b$'$)] inside the italic proposition: italic label",
    "convention", 6, "high",
    {"old": "\\item[b$'$)]",
     "new": "\\item[\\textup{b$'$)}]"},
    "")

add(209,
    "Proposition (14.3.13): 'Alors on a les implications a)⇒b)⇔b').'",
    "a new indented paragraph after b')",
    "follows \\end{enumerate} without a blank line: no indent",
    "other", None, "high",
    {"old": "\\end{enumerate}\nAlors on a",
     "new": "\\end{enumerate}\n\nAlors on a"},
    "GLOBAL_ISSUES 80 pattern (text after \\end{enumerate} without a blank line).")

add(209,
    "same sentence: 'a)⇒b)⇔b')'",
    "the labels a), b), b') are set roman (upright) inside the italic statement (enlarged crop p209_s1_labels.png)",
    "$a)\\Rightarrow b)\\Leftrightarrow b')$: math-italic a, b",
    "convention", 6, "high",
    {"old": "$a)\\Rightarrow b)\\Leftrightarrow b')$",
     "new": "$\\mathrm{a})\\Rightarrow\\mathrm{b})\\Leftrightarrow\\mathrm{b}')$"},
    "Roman letters inside the italic statement; \\textup has no effect on math letters, hence \\mathrm.")

add(209,
    "proof of (14.3.13): 'le complémentaire de la réunion des W̄_i (adhérences dans X) qui ne contiennent pas x'",
    "'dans' in italics (page_209_s2.png)",
    "'dans' upright",
    "italics", None, "high",
    {"old": "(adhérences dans $X$)",
     "new": "(adhérences \\emph{dans} $X$)"},
    "")

add(209,
    "Remarque (14.3.14): 'l'hypothèse plus faible que f est ouvert au point x.'",
    "'ouvert' in italics (page_209_s3.png)",
    "'ouvert' without emphasis",
    "italics", None, "high",
    {"old": "que $f$ est ouvert au point $x$. On",
     "new": "que $f$ est \\emph{ouvert} au point $x$. On"},
    "Judged as if the remark body were roman.")

add(209,
    "heading 14.4: 'Le critère de Chevalley pour les morphismes universellement ouverts.'",
    "the title ends with a full stop",
    "\\subsection{...} without the full stop",
    "punctuation", None, "high",
    {"old": "\\subsection{Le critère de Chevalley pour les morphismes universellement ouverts}",
     "new": "\\subsection{Le critère de Chevalley pour les morphismes universellement ouverts.}"},
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")

add(209,
    "Théorème (14.4.1): 'x un point maximal de la fibre X_y=X×_Y Spec(k(y)).'",
    "bold italic k",
    "plain k",
    "convention", 1, "high",
    {"old": "X_y=X\\times_Y\\operatorname{Spec}(k(y))",
     "new": "X_y=X\\times_Y\\operatorname{Spec}(\\boldsymbol{k}(y))"},
    "")

add(209,
    "Théorème (14.4.1): 'Supposons y géométriquement unibranche.'",
    "'géométriquement unibranche' roman inside the italic statement, 'Supposons y' italic (enlarged crop p209_s4_unibranche.png)",
    "italic (theorem environment)",
    "convention", 6, "high",
    {"old": "$y$ géométriquement unibranche.",
     "new": "$y$ \\textup{géométriquement unibranche}."},
    "")

add(209,
    "Théorème (14.4.1) a): '... de point générique x (14.3.3.1, (ii))).'",
    "(14.3.3.1, (ii)) (enlarged crop p209_s4_ref.png)",
    "(14.3.3.1, (iii))",
    "number", None, "high",
    {"old": r"""(ou encore en tout point de la
  composante irréductible de $X_y$ de point générique $x$ (14.3.3.1, (iii)))""",
     "new": r"""\textup{(ou encore en tout point de la
  composante irréductible de $X_y$ de point générique $x$ (14.3.3.1, (ii)))}"""},
    "Transcription error: the remarks (14.3.3.1) have only items (i) and (ii); (ii) (the extension of (14.1.4)) is the one meant, as in the same phrase of (14.3.13) a), p. 208. One edit for this finding and the next (convention 6). ega4-14-fr.tex line 1030 also cites '(14.3.3.1, (iii))' (later page): worth a look by that page's checker.")

add(209,
    "Théorème (14.4.1) a): the parenthesis '(ou encore en tout point ... (14.3.3.1, (ii)))'",
    "the whole parenthesis roman inside the italic statement",
    "italic (theorem environment)",
    "convention", 6, "high",
    None,
    "Covered by the edit of the preceding finding, which adds the \\textup.")


# ---------------------------------------------------------------- checks
def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")


bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    cnt = page_text(d["page"]).count(fx["old"])
    if cnt != 1:
        bad += 1
        print("COUNT", cnt, "page", d["page"], repr(fx["old"][:80]))
    if fx["old"] == fx["new"]:
        bad += 1
        print("NOOP", d["page"], repr(fx["old"][:80]))

# overlapping edits on the same page
for i, a in enumerate(F):
    for b in F[i + 1:]:
        if a["page"] != b["page"] or not a["fix"] or not b["fix"]:
            continue
        t = page_text(a["page"])
        ia, ib = t.find(a["fix"]["old"]), t.find(b["fix"]["old"])
        ra = range(ia, ia + len(a["fix"]["old"]))
        rb = range(ib, ib + len(b["fix"]["old"]))
        if ia < ib + len(b["fix"]["old"]) and ib < ia + len(a["fix"]["old"]):
            bad += 1
            print("OVERLAP", a["page"], repr(a["fix"]["old"][:50]), repr(b["fix"]["old"][:50]))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
json.loads(OUT.read_text(encoding="utf-8"))
print("written", OUT, len(F), "findings; problems:", bad)

from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
