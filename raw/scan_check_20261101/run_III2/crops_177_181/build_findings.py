import io
import json
import sys

RUN = r"user\Documents\ega_scan_check_20261101\run_III2"
OUT = RUN + r"\findings_177_181.json"
NL = "\u00b6"  # pilcrow stands for a line break inside the raw strings below

LAYOUT = ("Layout: the print sets this formula in the running text; the TeX displays it. "
          "The formula itself matches.")
WAVY = "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33."
ABNOTE = ("Category Ab printed bold italic (enlarged crops on pp. 177, 180, 181; the same face throughout); "
          "the TeX has bold upright \\mathbf{Ab} (63 in ega3-7-fr.tex; candidate one-pass change).")
KNOTE = ("Category letter K printed bold italic, as GLOBAL_ISSUES items 38/44; "
         "the TeX has script \\mathcal K.")
C6 = "Reference printed upright inside the italic statement."

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 177
add(177, "top of the page, end of (7.2.1): 'Z-homomorphisme x→f_x de M'",
    "'homomorphisme' in italics (enlarged crop)", "$\\mathbf Z$-homomorphisme (upright)",
    "italics", None, "high",
    r"[III]{177}¶$\mathbf Z$-homomorphisme", r"[III]{177}¶$\mathbf Z$-\emph{homomorphisme}",
    "Emphasis continued from p. 176; the old string includes the end of the marker line to stay unique.")
add(177, "end of (7.2.1): 'Z-homomorphisme x→f_x'",
    "plain arrow x→f_x (enlarged crop)", "$x\\mapsto f_x$",
    "convention", 3, "high",
    r"$x\mapsto f_x$", r"$x\to f_x$", "Plain arrow printed.")
add(177, "end of (7.2.1): 'tel que f_ax(t)=f_x(ta) pour a∈A, t∈N, x∈M, les deux applications'",
    "in the running text", "displayed", "other", None, "high",
    r"tel que¶\[¶  f_{ax}(t)=f_x(ta)¶  \qquad\text{pour }a\in A,\ t\in N,\ x\in M,¶\]¶",
    r"tel que¶$f_{ax}(t)=f_x(ta)$ pour $a\in A$, $t\in N$, $x\in M$,¶",
    LAYOUT)
add(177, "(7.2.2): 'Soit T : Ab_A→Ab un foncteur covariant additif'",
    "Ab bold italic (both)", "$T:\\mathbf{Ab}_A\\to\\mathbf{Ab}$", "font", None, "high",
    r"$T:\mathbf{Ab}_A\to\mathbf{Ab}$", r"$T:\boldsymbol{Ab}_A\to\boldsymbol{Ab}$", ABNOTE)
add(177, "(7.2.2): 'un homomorphisme canonique fonctoriel en M, de Z-modules'",
    "'homomorphisme canonique fonctoriel en', 'de' and 'modules' in italics (M and Z upright)",
    "all upright", "italics", None, "high",
    r"un homomorphisme canonique¶fonctoriel en $M$, de $\mathbf Z$-modules",
    r"un \emph{homomorphisme canonique¶fonctoriel en} $M$, \emph{de} $\mathbf Z$-\emph{modules}",
    "Enlarged crop.")
add(177, "after (7.2.2.1): 'Il suffira pour cela, en vertu de (7.2.1)'",
    "new, indented paragraph", "\\]\\nIl suffira (no blank line)", "other", None, "high",
    r"\]¶Il suffira pour cela", r"\]¶¶Il suffira pour cela",
    "Missing paragraph break: the print starts a new, indented paragraph after the display.")
add(177, "(7.2.2): 'un Z-homomorphisme x⇝t'_M(x) de M'",
    "wavy arrow (enlarged crop)", "$x\\mapsto t'_M(x)$", "symbol", None, "high",
    r"$x\mapsto t'_M(x)$", r"$x\leadsto t'_M(x)$", WAVY)
add(177, "(7.2.2): 'tel que l'on ait t'_M(ax)(y)=t'_M(x)(ya) pour a∈A, x∈M et y∈T(A_s).'",
    "'x∈M et y∈T(A_s)': the word 'et'; the formula in the running text",
    "'x\\in M,\\ y\\in T(A_s)' (comma) in a display", "word", None, "high",
    r"tel que l'on ait¶\[¶  t'_M(ax)(y)=t'_M(x)(ya)¶  \qquad\text{pour }a\in A,\ x\in M,\ y\in T(A_s).¶\]¶",
    r"tel que l'on ait¶$t'_M(ax)(y)=t'_M(x)(ya)$ pour $a\in A$, $x\in M$ et $y\in T(A_s)$.¶",
    "One edit for two differences: the missing word 'et' (the TeX has a comma) and display to inline "
    "('Notons pour cela que' continues the same line in the print).")
add(177, "(7.2.2): 'la loi externe étant telle que si a∈A, v∈Hom_Z(T(A_s), T(M)), (a.v)(y)=v(ya) pour y∈T(A_s).'",
    "(a.v) with a baseline period (enlarged crop); formula in the running text",
    "(a\\cdot v) in a display", "symbol", None, "high",
    r"\[¶  (a\cdot v)(y)=v(ya)¶  \qquad\text{pour }y\in T(A_s).¶\]¶",
    r"$(a.v)(y)=v(ya)$ pour $y\in T(A_s)$.¶",
    "One edit for two differences: the baseline dot (TeX \\cdot) and display to inline.")
add(177, "(7.2.2), display 'M⥲Hom_A(A_s, M) →T Hom_Z(T(A_s), T(M))'",
    "no punctuation after the display (enlarged crop)", "comma after T(M))", "punctuation", None, "high",
    r"(T(A_s),T(M)),¶\]", r"(T(A_s),T(M))¶\]", "The next line begins 'la seconde flèche'.")
add(177, "(7.2.2): 'la seconde flèche étant l'application u⇝T(u)'",
    "wavy arrow (enlarged crop)", "$u\\mapsto T(u)$", "symbol", None, "high",
    r"$u\mapsto T(u)$", r"$u\leadsto T(u)$", WAVY)
add(177, "(7.2.2): 'l'isomorphisme canonique de A-modules x⇝θ_x'",
    "wavy arrow (enlarged crop)", "$x\\mapsto\\theta_x$", "symbol", None, "high",
    r"$x\mapsto\theta_x$", r"$x\leadsto\theta_x$", WAVY)
add(177, "(7.2.2): 'donc T(θ_ax)=T(θ_x∘h_a)=T(θ_x)∘T(h_a) et par suite'",
    "in the running text", "displayed", "other", None, "high",
    r"donc¶\[¶  T(\theta_{ax})¶  =¶  T(\theta_x\circ h_a)¶  =¶  T(\theta_x)\circ T(h_a)¶\]¶",
    r"donc¶$T(\theta_{ax})=T(\theta_x\circ h_a)=T(\theta_x)\circ T(h_a)$¶",
    LAYOUT)
add(177, "(7.2.2), last paragraph: 'lorsque A est commutatif, c'est un homomorphisme de A-modules'",
    "'commutatif' and 'modules' in italics", "upright", "italics", None, "high",
    r"est¶commutatif, c'est un homomorphisme de $A$-modules",
    r"est¶\emph{commutatif}, c'est un homomorphisme de $A$-\emph{modules}", "")
add(177, "(7.2.3): 'par l'homomorphisme de A-modules N→N⊗_A M qui à tout y∈N'",
    "in the running text", "displayed", "other", None, "high",
    r"de $A$-modules¶\[¶  N\longrightarrow N\otimes_A M¶\]¶",
    r"de $A$-modules¶$N\longrightarrow N\otimes_A M$¶",
    LAYOUT)
add(177, "(7.2.3): 'cet homomorphisme est fonctoriel en M et N.'",
    "'fonctoriel en' and 'et' in italics", "upright", "italics", None, "high",
    r"est fonctoriel en $M$ et", r"est \emph{fonctoriel en} $M$ \emph{et}", "")
add(177, "end of p. 177 / top of p. 178: '... fonctoriel en M et N.' | 'En particulier, si B est'",
    "the last line of p. 177 is full; p. 178 begins flush left (same paragraph)",
    "blank line before \\oldpage[III]{178}", "other", None, "high",
    r"$N$.¶¶", r"$N$.¶",
    "Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). page_178.tex has no blank line "
    "after the marker, so this one edit suffices.")

# ---------------------------------------------------------------- page 178
add(178, "(7.2.3): 'est un homomorphisme de B-modules.'",
    "'modules' in italics", "upright", "italics", None, "high",
    r"de $B$-modules.", r"de $B$-\emph{modules}.", "")
add(178, "(7.2.3): 'c'est l'homomorphisme T(A)⊗_A M→T_(B)(B_s)⊗_B(B⊗_A M)=T_(B)(B_s)⊗_A M où'",
    "in the running text", "displayed", "other", None, "high",
    r"c'est l'homomorphisme¶\[¶  T(A)\otimes_A M¶  \longrightarrow¶  T_{(B)}(B_s)\otimes_B(B\otimes_A M)¶  =¶  T_{(B)}(B_s)\otimes_A M¶\]¶",
    r"c'est l'homomorphisme¶$T(A)\otimes_A M\longrightarrow T_{(B)}(B_s)\otimes_B(B\otimes_A M)=T_{(B)}(B_s)\otimes_A M$¶",
    LAYOUT)
add(178, "(7.2.3): 'où T(A)→T_(B)(B_s)=T(B) est T(ρ)'",
    "in the running text", "displayed", "other", None, "high",
    r"où¶\[¶  T(A)\longrightarrow T_{(B)}(B_s)=T(B)¶\]¶",
    r"où¶$T(A)\longrightarrow T_{(B)}(B_s)=T(B)$¶",
    LAYOUT)
add(178, "Lemme (7.2.4): 'de Ab_A dans Ab, commutant avec'",
    "Ab bold italic (both)", "\\mathbf{Ab}", "font", None, "high",
    r"de $\mathbf{Ab}_A$ dans¶$\mathbf{Ab}$, commutant avec",
    r"de $\boldsymbol{Ab}_A$ dans¶$\boldsymbol{Ab}$, commutant avec", ABNOTE)
add(178, "Lemme (7.2.4): 'l'homomorphisme canonique t_L (7.2.2.1) est'",
    "(7.2.2.1) upright inside the italic statement (enlarged crop)", "italic (lemma environment)",
    "convention", 6, "high",
    r"$t_L$ (7.2.2.1)", r"$t_L$ \textup{(7.2.2.1)}", C6)
add(178, "proof of (7.2.4): 'En effet, on a L=⊕_{α∈I} L_α où'",
    "in the running text", "displayed", "other", None, "high",
    r"on a¶\[¶  L=\bigoplus_{\alpha\in I}L_\alpha¶\]¶",
    r"on a¶$L=\bigoplus_{\alpha\in I}L_\alpha$¶",
    LAYOUT)
add(178, "proof of (7.2.4): 'montre que t_L=⊕_{α∈I} t_{L_α}, puisque'",
    "in the running text", "displayed", "other", None, "high",
    r"montre que¶\[¶  t_L=\bigoplus_{\alpha\in I}t_{L_\alpha},¶\]¶",
    r"montre que¶$t_L=\bigoplus_{\alpha\in I}t_{L_\alpha}$,¶",
    LAYOUT)
add(178, "proof of (7.2.4): 'applications Z-linéaires T_α : Hom_A(A_s, L_α)→Hom_Z(T(A_s), T(L_α)) en vertu'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶  T_\alpha:¶  \operatorname{Hom}_A(A_s,L_\alpha)¶  \longrightarrow¶  \operatorname{Hom}_{\mathbf Z}(T(A_s),T(L_\alpha))¶\]¶",
    r"$T_\alpha:\operatorname{Hom}_A(A_s,L_\alpha)\longrightarrow\operatorname{Hom}_{\mathbf Z}(T(A_s),T(L_\alpha))$¶",
    LAYOUT)
add(178, "proof of (7.2.4): 'l'isomorphisme canonique T(A_s)⊗_A A_s⥲T(A_s) valable'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶  T(A_s)\otimes_A A_s\xrightarrow{\sim}T(A_s)¶\]¶",
    r"$T(A_s)\otimes_A A_s\xrightarrow{\sim}T(A_s)$¶",
    LAYOUT)
add(178, "Proposition (7.2.5): 'de Ab_A dans Ab, commutant aux'",
    "Ab bold italic (both)", "\\mathbf{Ab}", "font", None, "high",
    r"de $\mathbf{Ab}_A$ dans¶$\mathbf{Ab}$, commutant aux",
    r"de $\boldsymbol{Ab}_A$ dans¶$\boldsymbol{Ab}$, commutant aux", ABNOTE)
add(178, "Proposition (7.2.5) b): 'L'homomorphisme canonique t_M (7.2.2.1) est'",
    "(7.2.2.1) upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"$t_M$ (7.2.2.1)", r"$t_M$ \textup{(7.2.2.1)}", C6)

# ---------------------------------------------------------------- page 179
add(179, "proof of (7.2.5): 'Posons T'(M)=T(A_s)⊗_A M pour tout'",
    "in the running text", "displayed", "other", None, "high",
    r"Posons¶\[¶  T'(M)=T(A_s)\otimes_A M¶\]¶",
    r"Posons¶$T'(M)=T(A_s)\otimes_A M$¶",
    LAYOUT)
add(179, "proof of (7.2.5): 'une suite exacte L'→L→M→0, où L et L''",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶  L'\longrightarrow L\longrightarrow M\longrightarrow0,¶\]¶",
    r"$L'\longrightarrow L\longrightarrow M\longrightarrow0$,¶",
    LAYOUT)
add(179, "proof of (7.2.5): 'deux A-modules à gauche libres;'",
    "'libres' in italics", "upright", "italics", None, "high",
    r"à gauche libres;", r"à gauche \emph{libres};", "")
add(179, "proof of (7.2.5), diagram: labels t_{L'}, t_L, t_M of the vertical arrows",
    "labels to the left of the vertical arrows", "\\ar[d]^{...}: xy-pic sets the labels on the right",
    "other", None, "high",
    r"T'(L')\ar[r]\ar[d]^{t_{L'}}¶  &¶  T'(L)\ar[r]\ar[d]^{t_L}¶  &¶  T'(M)\ar[r]\ar[d]^{t_M}",
    r"T'(L')\ar[r]\ar[d]_{t_{L'}}¶  &¶  T'(L)\ar[r]\ar[d]_{t_L}¶  &¶  T'(M)\ar[r]\ar[d]_{t_M}",
    "Label side only (cf. GLOBAL_ISSUES item 30); the diagrams of pp. 177, 180 already use _ for left labels.")
add(179, "end of the proof of (7.2.5): 'il suffit de prouver le' / 'Lemme (7.2.5.1). —'",
    "'il suffit de prouver le' runs straight into the heading 'Lemme (7.2.5.1). —'; no 'lemme suivant.'",
    "il suffit de prouver le lemme suivant.", "extra", None, "high",
    r"il suffit de prouver le lemme suivant.", r"il suffit de prouver le",
    "The TeX adds the words 'lemme suivant.'; the print's sentence ends with 'le' before the lemma heading.")
add(179, "Lemme (7.2.5.1): 'Soient K, K' deux catégories abéliennes'",
    "K, K' bold italic", "$\\mathcal K$, $\\mathcal K'$", "font", None, "high",
    r"Soient $\mathcal K$, $\mathcal K'$ deux", r"Soient $\boldsymbol{K}$, $\boldsymbol{K}'$ deux", KNOTE)
add(179, "Lemme (7.2.5.1): 'additifs de K dans K''",
    "K, K' bold italic", "$\\mathcal K$, $\\mathcal K'$", "font", None, "high",
    r"de $\mathcal K$ dans $\mathcal K'$", r"de $\boldsymbol{K}$ dans $\boldsymbol{K}'$", KNOTE)
add(179, "Lemme (7.2.5.1): 'un morphisme fonctoriel (T, I, 1.2) tel que'",
    "(T, I, 1.2) upright inside the italic statement (enlarged crop)", "italic (lemma environment)",
    "convention", 6, "high",
    r"fonctoriel (T, I, 1.2) tel que", r"fonctoriel \textup{(T, I, 1.2)} tel que", C6)
add(179, "Lemme (7.2.5.1): 'de la catégorie K, f_E'",
    "K bold italic", "$\\mathcal K$", "font", None, "high",
    r"de la catégorie $\mathcal K$,", r"de la catégorie $\boldsymbol{K}$,", KNOTE)
add(179, "Lemme (7.2.5.1): 'f_E : F(E)→G(E) soit un épimorphisme'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶  f_E:F(E)\longrightarrow G(E)¶\]¶",
    r"$f_E:F(E)\longrightarrow G(E)$¶",
    LAYOUT)
add(179, "proof of (7.2.5.1): 'épimorphisme v : E'→E dans K,'",
    "K bold italic", "$\\mathcal K$", "font", None, "high",
    r"$v:E'\to E$ dans $\mathcal K$,", r"$v:E'\to E$ dans $\boldsymbol{K}$,", KNOTE)
add(179, "proof of (7.2.5.1): 'G(v) : G(E')→G(E) est un épimorphisme'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶  G(v):G(E')\longrightarrow G(E)¶\]¶",
    r"$G(v):G(E')\longrightarrow G(E)$¶",
    LAYOUT)
add(179, "Remarque (7.2.6): 'posons T_N(M)=N⊗_A M pour tout'",
    "in the running text", "displayed", "other", None, "high",
    r"posons¶\[¶  T_N(M)=N\otimes_A M¶\]¶",
    r"posons¶$T_N(M)=N\otimes_A M$¶",
    LAYOUT)
add(179, "Remarque (7.2.6): 'foncteur covariant additif de Ab_A dans Ab, exact à droite'",
    "Ab bold italic (both)", "\\mathbf{Ab}", "font", None, "high",
    r"de $\mathbf{Ab}_A$ dans $\mathbf{Ab}$, exact à droite",
    r"de $\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$, exact à droite", ABNOTE)
add(179, "Remarque (7.2.6): 'les morphismes fonctoriels T⇝T(A_s) et N⇝T_N constituent'",
    "'T⇝T(A_s) et N⇝T_N' in the running text: the word 'et', wavy arrows (enlarged crop)",
    "displayed 'T\\longmapsto T(A_s),\\qquad N\\longmapsto T_N'", "word", None, "high",
    r"fonctoriels¶\[¶  T\longmapsto T(A_s),¶  \qquad¶  N\longmapsto T_N¶\]¶",
    r"fonctoriels¶$T\leadsto T(A_s)$ et $N\leadsto T_N$¶",
    "One edit for three differences: the missing word 'et' (the TeX has a comma and \\qquad), the wavy "
    "arrows (\\leadsto; GLOBAL_ISSUES item 33) and display to inline.")
add(179, "Remarque (7.2.6): 'constituent une équivalence (T, I, 1.2)'",
    "'équivalence' in italics", "no emphasis (remark body)", "italics", None, "high",
    r"une équivalence (T, I, 1.2)", r"une \emph{équivalence} (T, I, 1.2)",
    "Judged with the remark body roman, as printed.")
add(179, "Remarque (7.2.6): 'foncteurs covariants additifs Ab_A→Ab qui sont'",
    "Ab bold italic (both)", "\\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A\to\mathbf{Ab}$ qui sont", r"$\boldsymbol{Ab}_A\to\boldsymbol{Ab}$ qui sont", ABNOTE)
add(179, "Proposition (7.2.7): 'de Ab_A dans Ab, commutant aux'",
    "Ab bold italic (both)", "\\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$, commutant aux",
    r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$, commutant aux", ABNOTE)
add(179, "Proposition (7.2.7): 'Les conditions de (7.2.5) sont alors aussi équivalentes à'",
    "(7.2.5) upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"conditions de (7.2.5) sont", r"conditions de \textup{(7.2.5)} sont", C6)
add(179, "Proposition (7.2.7) d): 'l'homomorphisme T(ε) : T(A_s)→T(k) déduit de'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶      T(\varepsilon):T(A_s)\longrightarrow T(k)¶    \]¶",
    r"$T(\varepsilon):T(A_s)\longrightarrow T(k)$¶",
    LAYOUT)

# ---------------------------------------------------------------- page 180
add(180, "proof of (7.2.7): '... prouvons que d) entraîne b').' | 'Il existe un entier n'",
    "'Il existe' starts flush left after a full line: same paragraph", "blank line between the sentences",
    "other", None, "high",
    r"$d)$ entraîne $b')$.¶¶Il existe", r"$d)$ entraîne $b')$.¶Il existe",
    "Spurious paragraph break (left edges measured on the strip: only 'Il est clair' is indented).")
add(180, "proof of (7.2.7): 'une suite exacte 0→M'→M→(v)M''→0 de A-modules'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶  0\longrightarrow M'¶  \longrightarrow M¶  \xrightarrow{v}M''¶  \longrightarrow 0¶\]¶",
    r"$0\longrightarrow M'\longrightarrow M\xrightarrow{v}M''\longrightarrow 0$¶",
    LAYOUT)
add(180, "heading 7.3: 'Critères d'exactitude des foncteurs homologiques de modules.'",
    "final full stop", "no full stop", "punctuation", None, "high",
    r"\subsection{Critères d'exactitude des foncteurs homologiques de modules}",
    r"\subsection{Critères d'exactitude des foncteurs homologiques de modules.}",
    "Same pattern as GLOBAL_ISSUES item 43 (ega3-1) and the run_III2 page fixes for 6.1-6.3.")
add(180, "Proposition (7.3.1): 'foncteur homologique covariant (T, II, 2.1) de la catégorie'",
    "(T, II, 2.1) upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"(T, II, 2.1)", r"\textup{(T, II, 2.1)}", C6)
add(180, "Proposition (7.3.1): 'de la catégorie Ab_A dans la catégorie Ab, commutant'",
    "Ab bold italic (both; enlarged crop)", "\\mathbf{Ab}", "font", None, "high",
    r"catégorie $\mathbf{Ab}_A$ dans la¶catégorie $\mathbf{Ab}$,",
    r"catégorie $\boldsymbol{Ab}_A$ dans la¶catégorie $\boldsymbol{Ab}$,", ABNOTE)

# ---------------------------------------------------------------- page 181
add(181, "Proposition (7.3.1) c): 'l'homomorphisme fonctoriel canonique (7.2.2.1)'",
    "(7.2.2.1) upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"canonique (7.2.2.1)", r"canonique \textup{(7.2.2.1)}", C6)
add(181, "Proposition (7.3.1) d): 'l'homomorphisme (7.3.1.1) est un épimorphisme'",
    "(7.3.1.1) upright inside the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"l'homomorphisme (7.3.1.1)", r"l'homomorphisme \textup{(7.3.1.1)}", C6)
add(181, "Proposition (7.3.1) e): 'un foncteur M⇝N⊗_A M'",
    "wavy arrow (enlarged crop)", "$M\\mapsto N\\otimes_A M$", "symbol", None, "high",
    r"$M\mapsto N\otimes_A M$", r"$M\leadsto N\otimes_A M$", WAVY)
add(181, "Proposition (7.3.1), after e): 'Si en outre les conditions de (7.2.7)'",
    "new, indented paragraph", "text directly after \\end{enumerate} (not indented)",
    "other", None, "high",
    r"\end{enumerate}¶Si en outre", r"\end{enumerate}¶¶Si en outre",
    "Missing paragraph break: the line is indented in the print.")
add(181, "Proposition (7.3.1): 'Si en outre les conditions de (7.2.7) sur A et m'",
    "(7.2.7) upright inside the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"conditions de (7.2.7) sur", r"conditions de \textup{(7.2.7)} sur", C6)
add(181, "Proposition (7.3.1) f): 'L'homomorphisme canonique T_p(ε) : T_p(A_s)→T_p(k) est un épimorphisme'",
    "in the running text", "displayed", "other", None, "high",
    r"\[¶      T_p(\varepsilon):T_p(A_s)\longrightarrow T_p(k)¶    \]¶",
    r"$T_p(\varepsilon):T_p(A_s)\longrightarrow T_p(k)$¶",
    LAYOUT + " Apply before the next finding (misprint in the same formula).")
add(181, "Proposition (7.3.1) f): 'T_p(A_s)→T_p(k)', subscript of the last T",
    "the third p of the line is bold italic: heavier strokes than the two p's before it "
    "(enlarged crop; dark pixels 160 against 107 and 110 at the same size, stroke 4 px against 3 px)",
    "plain p", "misprint_in_print", None, "high",
    r"(A_s)\longrightarrow T_p(k)", r"(A_s)\longrightarrow T_{\boldsymbol{p}}(k)",
    "Wrong-fount bold p in the print; the TeX silently corrects it. The fix restores the printed reading "
    "(apply after the display-to-inline edit above; its old string survives that edit).",
    corrected=r"T_p(k)")
add(181, "proof of (7.3.1): 'pour toute suite exacte 0→M'→(u)M→(v)M''→0, on a'",
    "in the running text", "displayed", "other", None, "high",
    r"suite exacte¶\[¶  0\longrightarrow M'\xrightarrow{u}M\xrightarrow{v}M''\longrightarrow0,¶\]¶",
    r"suite exacte¶$0\longrightarrow M'\xrightarrow{u}M\xrightarrow{v}M''\longrightarrow0$,¶",
    LAYOUT)
add(181, "proof of (7.3.1): 'on a Ker(T_{i-1}(u))=Coker(T_i(v)), il est clair'",
    "in the running text", "displayed", "other", None, "high",
    r"on a¶\[¶  \operatorname{Ker}(T_{i-1}(u))¶  =¶  \operatorname{Coker}(T_i(v)),¶\]¶",
    r"on a¶$\operatorname{Ker}(T_{i-1}(u))=\operatorname{Coker}(T_i(v))$,¶",
    LAYOUT)
add(181, "Corollaire (7.3.2): 'Avec les notations de (7.3.1), supposons'",
    "(7.3.1) upright inside the italic statement (enlarged crop)", "italic (corollary environment)",
    "convention", 6, "high",
    r"notations de (7.3.1)", r"notations de \textup{(7.3.1)}", C6)
add(181, "proof of (7.3.2): 'l'homothétie x→fx de M'",
    "plain arrow (enlarged crop)", "$x\\mapsto fx$", "convention", 3, "high",
    r"$x\mapsto fx$", r"$x\to fx$", "Plain arrow printed.")
add(181, "Proposition (7.3.3): 'de Ab_A dans Ab, commutant aux sommes directes'",
    "Ab bold italic (both)", "\\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$", r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$", ABNOTE)
add(181, "Proposition (7.3.3) e'): 'les homomorphismes canoniques (7.3.3.1) sont des épimorphismes'",
    "(7.3.3.1) upright inside the italic statement (enlarged crop)", "italic (proposition environment)",
    "convention", 6, "high",
    r"canoniques¶    (7.3.3.1)", r"canoniques¶    \textup{(7.3.3.1)}", C6)
add(181, "Proposition (7.3.3) f): 'l'homomorphisme (7.3.3.1) est un isomorphisme'",
    "(7.3.3.1) upright inside the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"l'homomorphisme (7.3.3.1) est un¶    isomorphisme",
    r"l'homomorphisme \textup{(7.3.3.1)} est un¶    isomorphisme", C6)
add(181, "Proposition (7.3.3) f'): 'l'homomorphisme (7.3.3.1) est un épimorphisme'",
    "(7.3.3.1) upright inside the italic statement", "italic (proposition environment)",
    "convention", 6, "high",
    r"l'homomorphisme (7.3.3.1) est un¶    épimorphisme",
    r"l'homomorphisme \textup{(7.3.3.1)} est un¶    épimorphisme", C6)
add(181, "proof of (7.3.3): 'le foncteur M⇝T_p(A_s)⊗_A M est exact à gauche'",
    "wavy arrow (enlarged crop); formula in the running text", "displayed, with \\mapsto",
    "symbol", None, "high",
    r"le foncteur¶\[¶  M\mapsto T_p(A_s)\otimes_A M¶\]¶",
    r"le foncteur¶$M\leadsto T_p(A_s)\otimes_A M$¶",
    WAVY + " One edit for two differences: the arrow and display to inline.")


# ---------------------------------------------------------------- checks
def page_text(p):
    with io.open(RUN + r"\page_%d.tex" % p, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
texts = {p: page_text(p) for p in range(177, 182)}
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    n = texts[d["page"]].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", i, d["page"], n, repr(fx["old"][:80]))

# apply all fixes of each page in order and confirm each old string is still found once
for p in range(177, 182):
    t = texts[p]
    for i, d in enumerate(F):
        if d["page"] != p or d["fix"] is None:
            continue
        n = t.count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("SEQUENTIAL FAIL", i, p, n, repr(d["fix"]["old"][:80]))
            continue
        t = t.replace(d["fix"]["old"], d["fix"]["new"])

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(177, 182):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "ok", ok)
if ok and "--write" in sys.argv:
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
