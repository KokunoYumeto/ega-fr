import json, pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_075_079.json"
P = "\u00b6"  # newline marker in the edit strings below


def nl(s):
    return None if s is None else s.replace(P, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=nl(old), new=nl(new)))
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


def conv2(page, where, label, numeral="I"):
    add(page, where, f"({numeral}, ...) with bold {numeral}", f"plain {numeral} in the link text", "convention",
        f"[{label}-fr]{{{numeral},", f"[{label}-fr]{{\\textbf{{{numeral}}},", conv=2, note="")


def conv1(page, where, old, new):
    add(page, where, "bold italic k in k(y)", "plain k(y)", "convention", old, new, conv=1)


# ---------------------------------------------------------------- page 75
p = 75
conv2(p, "1°, first sentence: 'schéma local (I, 2.4.8)'", "I.2.4.8")
conv1(p, "1°: Y'=Spec(k(y))", r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))")
conv1(p, "1°: ℰ^y=ℰ_y⊗_{𝒪_y}k(y)", r"\otimes_{\mathcal{O}_y}k(y)", r"\otimes_{\mathcal{O}_y}\boldsymbol{k}(y)")
conv1(p, "1°: 'considéré comme espace vectoriel sur k(y)'", r"vectoriel sur $k(y)$", r"vectoriel sur $\boldsymbol{k}(y)$")
conv1(p, "1°: 'si K est une extension de k(y),'", r"extension de¶  $k(y)$,", r"extension de¶  $\boldsymbol{k}(y)$,")
conv1(p, "1°: p^{-1}(y)⊗_{k(y)}K", r"$p^{-1}(y)\otimes_{k(y)}K$", r"$p^{-1}(y)\otimes_{\boldsymbol{k}(y)}K$")
conv1(p, "1°: P(ℰ^y⊗_{k(y)}K)", r"\mathbf{P}(\mathcal{E}^y\otimes_{k(y)}K)",
      r"\mathbf{P}(\mathcal{E}^y\otimes_{\boldsymbol{k}(y)}K)")
conv1(p, "1°: 'à valeurs dans l'extension K de k(y)'", r"l'extension $K$ de $k(y)$}", r"l'extension $K$ de $\boldsymbol{k}(y)$}")
conv2(p, "1°: '(I, 3.4.5)'", "I.3.4.5")
add(p, "1°: 'fibre géométrique rationnelle sur K de P(ℰ) au-dessus du point y'",
    "italic 'fibre géométrique rationnelle sur', roman 'de' after K, italic 'au-dessus du point'",
    "the whole phrase in one \\emph, so 'de' is italic", "italics",
    r"rationnelle sur $K$ de¶  $\mathbf{P}(\mathcal{E})$ au-dessus du point $y$}",
    r"rationnelle sur} $K$ de¶  $\mathbf{P}(\mathcal{E})$ \emph{au-dessus du point $y$}",
    note="Only 'de' (between K and P(ℰ)) is upright; in the parallel phrase two lines earlier ('l'extension K de k(y)') 'de' is italic, as in the TeX.")
conv1(p, "1°, last line: 'du K-espace vectoriel ℰ^y⊗_{k(y)}K.'", r"\otimes_{k(y)}K$.", r"\otimes_{\boldsymbol{k}(y)}K$.")
conv2(p, "2°: 'V s'identifie à A^n (I, 1.3.8)'", "I.1.3.8")
add(p, "2°: 'autrement dit le même point de P^{n-1}_A à valeurs dans A'",
    "'le même point de' and 'à valeurs dans' italic", "no \\emph", "italics",
    r"autrement dit le même point de¶  $\mathbf{P}_A^{n-1}$ à valeurs dans $A$ si",
    r"autrement dit \emph{le même point de¶  $\mathbf{P}_A^{n-1}$ à valeurs dans $A$} si")
add(p, "paragraph 'Ces propriétés justifient': 'est en fait duale de la définition classique'",
    "'duale' italic", "upright", "italics", r"est en fait duale de", r"est en fait \emph{duale} de")
add(p, "same paragraph: 'pour un 𝒪_Y-Module quasi-cohérent quelconque ℰ'",
    "'quelconque' italic", "upright", "italics", r"quasi-cohérent¶quelconque $\mathcal{E}$",
    r"quasi-cohérent¶\emph{quelconque} $\mathcal{E}$")
conv2(p, "Remarque (4.2.7): 'Z×H^1(Y, 𝒪_Y^*) (0, 5.4.7)'", "0.5.4.7", "0")
conv2(p, "Remarque (4.2.7): '(III, 2.1.14, compte tenu de ...)'", "III.2.1.14", "III")
conv2(p, "Remarque (4.2.7): 'compte tenu de (0, 5.4.10)'", "0.5.4.10", "0")
add(p, "Remarque (4.2.7): 'ψ : ℱ→ℒ'⊗_{𝒪_Y}(S_{𝒪_Y}(ℰ))_m, tel que'",
    "comma after (S_{𝒪_Y}(ℰ))_m", "no comma", "punctuation",
    r"(\mathcal{E}))_m$ tel que", r"(\mathcal{E}))_m$, tel que")
add(p, "Remarque (4.2.7), last sentence: 'localement isomorphe à GL(n, 𝒪_Y)'",
    "bold upright GL", "\\operatorname{GL} (roman)", "font",
    r"\operatorname{GL}(n,\mathcal{O}_Y)", r"\mathbf{GL}(n,\mathcal{O}_Y)",
    note="The preamble's \\GL macro is \\bb{GL} = \\mathbf{GL}; this is the only \\operatorname{GL} in ega2-1-fr.tex.")
add(p, "(4.2.9), last word of the page 'le' (the sentence continues 'Y-morphisme j∘r' on p. 76)",
    "no paragraph break at the page turn", "blank line before \\oldpage[II]{76} (and another after it, p. 76): paragraph break mid-sentence",
    "other", r"\to\mathcal{L}$, le¶¶", r"\to\mathcal{L}$, le¶",
    note="Apply together with the p. 76 fix removing the blank line after \\oldpage[II]{76}.")

# ---------------------------------------------------------------- page 76
p = 76
add(p, "top of the page: '\\oldpage[II]{76}' followed by a blank line before 'Y-morphisme' (mid-sentence)",
    "no paragraph break: 'le Y-morphisme j∘r correspond à'", "blank line after the marker", "other",
    r"\oldpage[II]{76}¶¶$Y$-morphisme", r"\oldpage[II]{76}¶$Y$-morphisme",
    note="Apply together with the p. 75 fix removing the blank line before the marker.")
add(p, "(4.2.9), first line: 'correspond à q*(ℰ) →^{q*(v)} q*(ℱ) →^{φ} ℒ; cela résulte'",
    "formula set inline in the running text", "displayed formula", "other",
    r"correspond à¶\[¶  q^*(\mathcal{E})\xrightarrow{q^*(v)}q^*(\mathcal{F})¶  \xrightarrow{\varphi}\mathcal{L}~;¶\]¶cela",
    r"correspond à¶$q^*(\mathcal{E})\xrightarrow{q^*(v)}q^*(\mathcal{F})¶\xrightarrow{\varphi}\mathcal{L}$~;¶cela")
add(p, "(4.2.10), commutative diagram: labels p and r of the two bottom (leftward) arrows",
    "p and r below the arrows (p_{(Y')}, r_{(Y')} above the top arrows, u, v right of the vertical arrows)",
    "\\ar[l]_{p}, \\ar[l]_{r}: xy-pic sets '_' labels of leftward arrows above", "other",
    r"& P \ar[l]_{p}¶    & X \ar[l]_{r}", r"& P \ar[l]^{p}¶    & X \ar[l]^{r}", conf="medium",
    note="Label position only; the top-row labels (_ on leftward arrows, above) and u, v (^ on downward arrows, right) already match.")
add(p, "(4.2.10): 'D'après (4.1.3.2), on a' after the diagram",
    "new paragraph (indented)", "continues the paragraph (no blank line after the diagram)", "other",
    r"\]¶D'après", r"\]¶¶D'après", conf="medium")
add(p, "(4.2.10), display (r_{(Y')})*(𝒪_{P'}(1)) = ... = v*(ℒ) = ℒ⊗_Y𝒪_{Y'}",
    "no punctuation after the display; the next line begins 'd'autre part, u*(α_1^♯) ...'",
    "'~;' at the end of the display", "misprint_in_print",
    r"\otimes_Y\mathcal{O}_{Y'}~;", r"\otimes_Y\mathcal{O}_{Y'}",
    corrected=r"\otimes_Y\mathcal{O}_{Y'}~;",
    note="The print omits the semicolon the sentence needs; the TeX silently supplies it. Diplomatic: remove it; corrected edition keeps '~;'.")
conv2(p, "(4.3.1): 'deux 𝒪_Q-Modules inversibles (0, 5.4.4)'", "0.5.4.4", "0")
add(p, "(4.3.1): 'le 𝒪_Q-Module ℒ=𝒪_{P_1}(1)⊗_Y𝒪_{P_2}(1)=q_1*(𝒪_{P_1}(1))⊗_{𝒪_Q}q_2*(𝒪_{P_2}(1)) est inversible'",
    "formula set inline in the running text; the second sign is '='",
    "displayed formula; the second sign is ':='", "formula",
    r"-Module¶\[¶  \mathcal{L}=\mathcal{O}_{P_1}(1)\otimes_Y\mathcal{O}_{P_2}(1)¶  :=q_1^*(\mathcal{O}_{P_1}(1))\otimes_{\mathcal{O}_Q}¶  q_2^*(\mathcal{O}_{P_2}(1))¶\]¶est inversible",
    r"-Module¶$\mathcal{L}=\mathcal{O}_{P_1}(1)\otimes_Y\mathcal{O}_{P_2}(1)¶=q_1^*(\mathcal{O}_{P_1}(1))\otimes_{\mathcal{O}_Q}¶q_2^*(\mathcal{O}_{P_2}(1))$¶est inversible",
    note="Two differences in one edit: ':=' -> '=' and display -> inline.")
add(p, "(4.3.1): 'on a r*(ℰ⊗_{𝒪_Y}ℱ)=q_1*(p_1*(ℰ))⊗_{𝒪_Q}q_2*(p_2*(ℱ)) (0, 4.3.3);'",
    "formula set inline in the running text", "displayed formula", "other",
    r"on a¶\[¶  r^*(\mathcal{E}\otimes_{\mathcal{O}_Y}\mathcal{F})¶  =q_1^*(p_1^*(\mathcal{E}))\otimes_{\mathcal{O}_Q}¶  q_2^*(p_2^*(\mathcal{F}))¶\]¶",
    r"on a¶$r^*(\mathcal{E}\otimes_{\mathcal{O}_Y}\mathcal{F})¶=q_1^*(p_1^*(\mathcal{E}))\otimes_{\mathcal{O}_Q}¶q_2^*(p_2^*(\mathcal{F}))$¶")
conv2(p, "(4.3.1): '(0, 4.3.3); les homomorphismes canoniques surjectifs'", "0.4.3.3", "0")
add(p, "(4.3.1): 'les homomorphismes canoniques surjectifs (4.1.5.1) : p_1*(ℰ)→𝒪_{P_1}(1), ...'",
    "colon after (4.1.5.1)", "no colon", "punctuation",
    r"{4.1.5.1})¶$p_1^*", r"{4.1.5.1})~:¶$p_1^*")
add(p, "'Explicitons le morphisme ς ...' after (4.3.1.2)",
    "new paragraph (indented)", "continues the paragraph (no blank line after the display)", "other",
    r"\]¶Explicitons", r"\]¶¶Explicitons", conf="medium")
add(p, "'Explicitons le morphisme ς lorsque Y=Spec(A) est affine'",
    "no comma after ς", "'$\\varsigma$, lorsque'", "punctuation",
    r"$\varsigma$, lorsque", r"$\varsigma$ lorsque")
add(p, "'d'où ℰ⊗_{𝒪_Y}ℱ=(E⊗_A F)~ (I, 1.3.12)'",
    "(E⊗_A F) followed by a tilde", "\\widetilde{E\\otimes_A F} (tilde over the expression, no parentheses)",
    "convention", r"\widetilde{E\otimes_A F}", r"(E\otimes_A F)\supertilde", conv=5)
conv2(p, "'(E⊗_A F)~ (I, 1.3.12)'", "I.1.3.12")
add(p, "end of the page: display 'D_+(f)×_Y D_+(g)=Spec(B)'; the sentence continues 'de Q, où ...' on p. 77",
    "no paragraph break at the page turn", "blank line before \\oldpage[II]{77} (and another after it, p. 77)", "other",
    r"\operatorname{Spec}(B)¶\]¶¶", r"\operatorname{Spec}(B)¶\]¶",
    note="Apply together with the p. 77 fix removing the blank line after \\oldpage[II]{77}.")

# ---------------------------------------------------------------- page 77
p = 77
add(p, "top of the page: '\\oldpage[II]{77}' followed by a blank line before 'de Q, où' (mid-sentence)",
    "'de Q, où ...' continues the sentence, flush left", "blank line after the marker", "other",
    r"\oldpage[II]{77}¶¶de $Q$", r"\oldpage[II]{77}¶de $Q$",
    note="Apply together with the p. 76 fix removing the blank line before the marker.")
add(p, "(4.3.1), display '(x⊗y)⊗b → b((x/1)⊗(y/1))'", "plain arrow →", "\\longmapsto", "convention",
    r"b\longmapsto b(", r"b\to b(", conv=3)
add(p, "(4.3.2): 'En effet, on est ramené au cas où Y est affine' after (4.3.2.2)",
    "new paragraph (indented)", "continues the paragraph (no blank line after the display)", "other",
    r"\]¶En effet, on est ramené", r"\]¶¶En effet, on est ramené", conf="medium")
add(p, "(4.3.2): 'à l'aide de (I, 3.2.7 et 3.2.3))'", "bold I", "plain I in the link text", "convention",
    r"{I, 3.2.7} et¶", r"{\textbf{I}, 3.2.7} et¶", conv=2)
add(p, "(4.3.2): 'ramène (en revenant au cas affine, à l'aide de (I, 3.2.7 et 3.2.3)) à prouver'",
    "(I, 3.2.7 et 3.2.3)) — balanced parentheses", "(I, 3.2.7 et (3.2.3)) — an extra opening parenthesis before 3.2.3",
    "punctuation", r"(\hyperref[I.3.2.3-fr]", r"\hyperref[I.3.2.3-fr]")
conv2(p, "proof of Lemme (4.3.2.4): 'il résulte de (I, 1.2.2.2)'", "I.1.2.2.2")
add(p, "proof of Lemme (4.3.2.4): 'la conclusion résulte de (I, 3.2.7) et ...'", "bold I",
    "plain I in the link text", "convention", r"{I, 3.2.7}) et", r"{\textbf{I}, 3.2.7}) et", conv=2)
conv2(p, "proof of Lemme (4.3.2.4): '(I, 1.1.9.1), puisque'", "I.1.1.9.1")
conv2(p, "proof of Proposition (4.3.3): 'Il suffit donc (I, 4.2.4)'", "I.4.2.4")
add(p, "proof of Proposition (4.3.3): 'montre que ω est surjectif'", "'surjectif' italic", "upright", "italics",
    r"$\omega$ est surjectif", r"$\omega$ est \emph{surjectif}")
add(p, "(4.3.4): 'Le morphisme de Segre est fonctoriel en ℰ et ℱ'", "'fonctoriel' italic", "upright", "italics",
    r"est fonctoriel en", r"est \emph{fonctoriel} en")
add(p, "(4.3.4), end of the page: 'lorsqu'on restreint les' (continues 'homomorphismes' on p. 78)",
    "no paragraph break at the page turn", "blank line before \\oldpage[II]{78} (and another after it, p. 78)", "other",
    r"lorsqu'on restreint les¶¶", r"lorsqu'on restreint les¶",
    note="Apply together with the p. 78 fix removing the blank line after \\oldpage[II]{78}.")

# ---------------------------------------------------------------- page 78
p = 78
add(p, "top of the page: '\\oldpage[II]{78}' followed by a blank line before 'homomorphismes' (mid-sentence)",
    "no paragraph break", "blank line after the marker", "other",
    r"\oldpage[II]{78}¶¶homomorphismes", r"\oldpage[II]{78}¶homomorphismes",
    note="Apply together with the p. 77 fix removing the blank line before the marker.")
add(p, "(4.3.4): 'aux homomorphismes surjectifs. Il faut en effet'", "'surjectifs' italic", "upright", "italics",
    r"homomorphismes¶surjectifs. Il faut", r"homomorphismes¶\emph{surjectifs}. Il faut")
add(p, "(4.3.4), diagram, top left: P(ℰ')×P(ℱ)", "plain × (no subscript Y)", "\\times_Y", "formula",
    r"\mathbf{P}(\mathcal{E}')\times_Y\mathbf{P}(\mathcal{F})", r"\mathbf{P}(\mathcal{E}')\times\mathbf{P}(\mathcal{F})",
    note="The print abbreviates ×_Y to × here, as in (4.3.5) 'P(ℰ')×P(ℱ')', which the TeX keeps without subscript.")
add(p, "(4.3.4), diagram, top right: P(ℰ)×P(ℱ)", "plain × (no subscript Y)", "\\times_Y", "formula",
    r"& \mathbf{P}(\mathcal{E})\times_Y\mathbf{P}(\mathcal{F})", r"& \mathbf{P}(\mathcal{E})\times\mathbf{P}(\mathcal{F})")
conv2(p, "(4.3.4): 'j×1 est une immersion fermée (I, 4.3.1)'", "I.4.3.1")
conv2(p, "(4.3.4): 'en vertu de (4.1.2.1) et de (I, 9.1.5)'", "I.9.1.5")
add(p, "(4.3.5): 'Enfin, ... =ℒ' s'identifie à ℒ⊗_Y𝒪_{Y'} en vertu de (4.1.3.2)'",
    "no comma after ℒ⊗_Y𝒪_{Y'}", "comma", "punctuation",
    r"\mathcal{O}_{Y'}$, en vertu de", r"\mathcal{O}_{Y'}$ en vertu de")
conv2(p, "(4.3.5): 'et de (I, 9.1.11)'", "I.9.1.11")
add(p, "Remarque (4.3.6): 'Le préschéma somme de P(ℰ) et P(ℱ)'", "'somme' italic (remark body roman)",
    "no \\emph", "italics", r"Le préschéma somme de", r"Le préschéma \emph{somme} de")
add(p, "Remarque (4.3.6): 'isomorphe à un sous-préschéma fermé de P(ℰ⊕ℱ)'",
    "'sous-préschéma fermé de' italic (remark body roman)", "no \\emph", "italics",
    r"isomorphe à un¶sous-préschéma fermé de", r"isomorphe à un¶\emph{sous-préschéma fermé de}")
add(p, "Remarque (4.3.6): 'mais qui contient S_+(F)'", "'contient' italic (remark body roman)", "no \\emph", "italics",
    r"mais qui contient", r"mais qui \emph{contient}")
add(p, "heading 4.4: 'Immersions dans les fibrés projectifs. Faisceaux très amples.'",
    "final period after 'amples'", "no final period (the 4.3 heading has one)", "punctuation",
    r"Faisceaux très amples}", r"Faisceaux très amples.}")
add(p, "Proposition (4.4.1), first sentence: 'q : X→Y un morphisme de type fini'",
    "'de type fini' roman inside the italic statement", "italic", "convention",
    r"un morphisme de type fini,", r"un morphisme \textup{de type fini},", conv=6)
add(p, "(4.4.1)(i), end of the page: 'il faut et' (continues 'il suffit' on p. 79)",
    "no paragraph break at the page turn", "blank line before \\oldpage[II]{79} (and another after it, p. 79)", "other",
    r"il faut et¶¶", r"il faut et¶",
    note="Apply together with the p. 79 fix removing the blank line after \\oldpage[II]{79}; inside the enumerate item the blank line also ends the item's paragraph.")

# ---------------------------------------------------------------- page 79
p = 79
add(p, "top of the page: '\\oldpage[II]{79}' followed by a blank line before 'il suffit' (mid-sentence)",
    "no paragraph break", "blank line after the marker", "other",
    r"\oldpage[II]{79}¶¶  il suffit", r"\oldpage[II]{79}¶  il suffit",
    note="Apply together with the p. 78 fix removing the blank line before the marker.")
add(p, "(4.4.1)(i): 'un sous-𝒪_Y-Module quasi-cohérent de type fini ℰ de 𝒮_n'",
    "'de type fini' roman inside the italic statement", "italic", "convention",
    r"quasi-cohérent de type fini $\mathcal{E}$ de $\mathcal{S}_n$",
    r"quasi-cohérent \textup{de type fini} $\mathcal{E}$ de $\mathcal{S}_n$", conv=6)
add(p, "(4.4.1)(i): 'l'homomorphisme ψ'=ψ_n∘q*(j) : q*(ℰ)→ℒ^{⊗n}=ℒ' (j étant ...)'",
    "formula set inline in the running text", "displayed formula", "other",
    r"l'homomorphisme¶  \[¶    \psi'=\psi_n\circ q^*(j):q^*(\mathcal{E})¶      \longrightarrow\mathcal{L}^{\otimes n}=\mathcal{L}'¶  \]¶",
    r"l'homomorphisme¶  $\psi'=\psi_n\circ q^*(j):q^*(\mathcal{E})¶  \to\mathcal{L}^{\otimes n}=\mathcal{L}'$¶")
add(p, "(4.4.1)(i), last line: 'et que le morphisme r_{ℒ',φ'} : X→P(ℰ) soit une immersion'",
    "r_{ℒ',φ'} (phi prime)", "r_{\\mathcal{L}',\\psi'}", "misprint_in_print",
    r"r_{\mathcal{L}',\psi'}:X\to\mathbf{P}(\mathcal{E})", r"r_{\mathcal{L}',\varphi'}:X\to\mathbf{P}(\mathcal{E})",
    corrected=r"r_{\mathcal{L}',\psi'}:X\to\mathbf{P}(\mathcal{E})",
    note="(i) defines ψ'=ψ_n∘q*(j); φ' belongs to (ii). The TeX silently corrects the print's φ'.")
add(p, "(4.4.1)(ii): 'un sous-𝒪_Y-Module quasi-cohérent de type fini ℰ de ℱ'",
    "'de type fini' roman inside the italic statement", "italic", "convention",
    r"quasi-cohérent de type fini $\mathcal{E}$ de¶  $\mathcal{F}$",
    r"quasi-cohérent \textup{de type fini} $\mathcal{E}$ de¶  $\mathcal{F}$", conv=6)
add(p, "(4.4.1)(ii): 'l'homomorphisme φ'=φ∘q(j) : q*(ℰ)→ℒ'",
    "φ∘q(j) (no asterisk on q)", "\\varphi\\circ q^*(j)", "misprint_in_print",
    r"\varphi'=\varphi\circ q^*(j)", r"\varphi'=\varphi\circ q(j)",
    corrected=r"\varphi'=\varphi\circ q^*(j)",
    note="j : ℰ→ℱ is a map of 𝒪_Y-Modules, so the composite with φ : q*(ℱ)→ℒ needs q*(j), as in (i) (ψ_n∘q*(j)). The TeX silently corrects.")
add(p, "proof of (4.4.1)(i): 'soit surjectif et que r_{ℒ,ψ'} : X→Proj(𝒮') soit partout défini'",
    "r_{ℒ,ψ'} (ℒ without prime)", "r_{\\mathcal{L}',\\psi'}", "formula",
    r"r_{\mathcal{L}',\psi'}:X\to\operatorname{Proj}", r"r_{\mathcal{L},\psi'}:X\to\operatorname{Proj}",
    note="Not a misprint: (3.8.5) b), which this step cites, writes r_{ℒ,ψ'} : X→Proj(𝒮') with ψ'=ψ∘q*(j') the restriction of ψ to 𝒮'.")
conv2(p, "proof of (4.4.1)(ii): 'de type fini ℰ_λ (I, 9.4.9)'", "I.9.4.9")
add(p, "Définition (4.4.2): 'ℒ est très ample pour q'",
    "'très ample' roman (the defined term), 'pour q' italic", "\\emph{très ample pour $q$}: 'pour' upright too",
    "convention", r"\emph{très ample pour¶$q$}", r"\emph{très ample} pour¶$q$", conv=6)
add(p, "Définition (4.4.2): '(ou très ample pour Y, ou simplement'",
    "'(ou' and ', ou simplement' roman; 'très ample pour' italic",
    "'(ou' and ', ou simplement' italic; 'très ample pour Y' upright (\\emph)", "convention",
    r"(ou \emph{très ample pour $Y$}, ou simplement",
    r"\textup{(ou} très ample pour $Y$\textup{, ou simplement}", conv=6)
add(p, "Définition (4.4.2): 'très ample si aucune confusion n'en résulte)'",
    "'très ample' italic; 'si aucune confusion n'en résulte)' roman",
    "'très ample' upright (\\emph); the rest italic", "convention",
    r"\emph{très ample} si¶aucune confusion n'en résulte)",
    r"très ample \textup{si¶aucune confusion n'en résulte)}", conv=6,
    note="With the two preceding fixes the whole parenthesis matches the print: roman comment, italic alternative terms.")
add(p, "paragraph 'Il revient au même (4.2.3)': 'un homomorphisme surjectif φ : q*(ℰ)→ℒ'",
    "'surjectif' italic", "upright", "italics",
    r"homomorphisme¶surjectif $\varphi", r"homomorphisme¶\emph{surjectif} $\varphi")
add(p, "same paragraph: 'r_{ℒ,φ} : X→P(ℰ) soit une immersion.'", "'immersion' italic", "upright", "italics",
    r"soit une immersion.¶¶On notera", r"soit une \emph{immersion}.¶¶On notera")
add(p, "paragraph 'On notera que': 'implique que q est séparé'", "'séparé' italic", "upright", "italics",
    r"implique que $q$ est séparé", r"implique que $q$ est \emph{séparé}")
conv2(p, "paragraph 'On notera que': '(I, 5.5.1, (i) et (ii))'", "I.5.5.1")
conv2(p, "proof of Proposition (4.4.4): 'si q est séparé (I, 9.2.2)'", "I.9.2.2")

# ---------------------------------------------------------------- checks
ok = True
for page in sorted({x["page"] for x in F}):
    raw = (RUN / f"page_{page:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    cur = raw
    for x in [y for y in F if y["page"] == page]:
        fx = x["fix"]
        if fx is None:
            continue
        n0 = raw.count(fx["old"])
        n1 = cur.count(fx["old"])
        if n0 != 1 or n1 != 1:
            ok = False
            print("PROBLEM", page, repr(fx["old"]), "in original:", n0, "at its turn:", n1)
        cur = cur.replace(fx["old"], fx["new"])
    body = cur.split("\n", 1)[1]
    print(page, "dollar signs:", body.count("$"), "braces:", body.count("{") - body.count("}"),
          "\\[ vs \\]:", body.count("\\["), body.count("\\]"))
from collections import Counter
c = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for page in sorted({x["page"] for x in F}):
    print(page, c[(page, "normal")], c[(page, "convention")], c[(page, "misprint")])
print("total", len(F), "all olds unique:", ok)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
