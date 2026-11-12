import json
import sys

RUN = 'user/Documents/ega_scan_check_20261101/run_IV4/'
OUT = RUN + 'findings_225_229.json'


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        'page': page,
        'where': where,
        'scan': scan,
        'tex': tex,
        'kind': kind,
        'convention': conv,
        'confidence': conf,
        'fix': None if old is None else {'old': old, 'new': new},
    }
    if kind == 'misprint_in_print':
        d['corrected'] = corrected
    d['note'] = note
    return d


findings = []
A = findings.append

# ---------------------------------------------------------------- p. 225
A(F(225, "top of page_225.tex: blank line after \\oldpage[IV-4]{225} (page break 224/225 inside 'un B_0-module de type fini M_0 qui est | un A_0-module plat')",
    "p. 224 ends 'un B_0-module de type fini M_0 qui est', p. 225 begins 'un A_0-module plat et un A_0-module N_0' in the same sentence (page_224_s4.png, page_225_s1.png)",
    "blank lines before and after the marker: a paragraph break inside the sentence",
    'marker', None, 'high',
    r"""\oldpage[IV-4]{225}

un $A_0$-module plat""",
    r"""\oldpage[IV-4]{225}
un $A_0$-module plat""",
    "BOUNDARY FIX (page break 224/225). The marker stands at the right place; both blank lines must go (GLOBAL_ISSUES 20/99; \\oldpage ends with \\ignorespaces, which does not skip a \\par). Part 2 of 2: part 1 is the last p. 224 finding of findings_220_224.json ('de type fini $M_0$ qui est\\n\\n' -> 'de type fini $M_0$ qui est\\n', end of the p. 224 segment of ega4-18-fr.tex). Apply both."))

A(F(225, "proof of (19.9.8): 'posons B_λ=... , Z_λ=V(𝔍_λ); si p_λ'",
    "set in the running text: 'posons B_λ=B_0⊗_{A_0}A_λ, 𝔍_λ=𝔍_0B_λ, M_λ=M_0⊗_{A_0}A_λ=M_0⊗_{B_0}B_λ, N_λ=N_0⊗_{A_0}A_λ et S_λ=Spec(A_λ), X_λ=Spec(B_λ), Z_λ=V(𝔍_λ); si p_λ : X→X_λ' (crops p225_s1_a.png, p225_s1_b.png)",
    "gathered display, and no 'et' before S_λ",
    'formula', None, 'high',
    r"""posons
\[
\begin{gathered}
  B_\lambda=B_0\otimes_{A_0}A_\lambda,\qquad
  \mathfrak J_\lambda=\mathfrak J_0B_\lambda,\qquad
  M_\lambda=M_0\otimes_{A_0}A_\lambda=M_0\otimes_{B_0}B_\lambda,\\
  N_\lambda=N_0\otimes_{A_0}A_\lambda,\qquad
  S_\lambda=\Spec(A_\lambda),\quad
  X_\lambda=\Spec(B_\lambda),\quad
  Z_\lambda=V(\mathfrak J_\lambda);
\end{gathered}
\]
si $p_\lambda""",
    r"""posons $B_\lambda=B_0\otimes_{A_0}A_\lambda$, $\mathfrak J_\lambda=\mathfrak J_0B_\lambda$, $M_\lambda=M_0\otimes_{A_0}A_\lambda=M_0\otimes_{B_0}B_\lambda$, $N_\lambda=N_0\otimes_{A_0}A_\lambda$ et $S_\lambda=\Spec(A_\lambda)$, $X_\lambda=\Spec(B_\lambda)$, $Z_\lambda=V(\mathfrak J_\lambda)$; si $p_\lambda""",
    "Formulas displayed where the print has them in the running text (GLOBAL_ISSUES 21/51), and the print's connecting word 'et' before S_λ is lost. One edit for both."))

A(F(225, "proof of (19.9.8): 'X—Z=p_λ^{-1}(X_λ—Z_λ)'",
    "long dash in X—Z and X_λ—Z_λ", "$X-Z=p_\\lambda^{-1}(X_\\lambda-Z_\\lambda)$",
    'convention', 7, 'high',
    r"""$X-Z=p_\lambda^{-1}(X_\lambda-Z_\lambda)$""",
    r"""$X\setmin Z=p_\lambda^{-1}(X_\lambda\setmin Z_\lambda)$""",
    "Two occurrences in one formula."))

A(F(225, "proof of (19.9.8): 'Comme X_λ—Z_λ est quasi-compact'",
    "long dash", "$X_\\lambda-Z_\\lambda$",
    'convention', 7, 'high',
    r"""Comme $X_\lambda-Z_\lambda$""",
    r"""Comme $X_\lambda\setmin Z_\lambda$""",
    ""))

A(F(225, "proof of (19.9.8): 'si l'on pose 𝓕_λ=M̃_λ'",
    "tilde over M only, subscript λ outside it (crop p225_Mtilde.png)", "\\widetilde{M_\\lambda}",
    'convention', 8, 'high',
    r"""\widetilde{M_\lambda}""",
    r"""\widetilde{M}_\lambda""",
    ""))

A(F(225, "proof of (19.9.8): 'les homomorphismes lim Γ(X_λ, ℋ_λ) → Γ(X, ℋ) et lim Γ(X_λ—Z_λ, ℋ_λ) → Γ(X—Z, ℋ) sont bijectifs'",
    "both homomorphisms set in the running text, joined by 'et' (crops p225_s1_c.png, p225_s1_d.png)",
    "displayed, joined by \\qquad\\text{et}\\qquad",
    'formula', None, 'high',
    r"""les homomorphismes
\[
  \varinjlim\Gamma(X_\lambda,\sh H_\lambda)\longrightarrow\Gamma(X,\sh H)
  \qquad\text{et}\qquad
  \varinjlim\Gamma(X_\lambda-Z_\lambda,\sh H_\lambda)\longrightarrow\Gamma(X-Z,\sh H)
\]
""",
    r"""les homomorphismes $\varinjlim\Gamma(X_\lambda,\sh H_\lambda)\to\Gamma(X,\sh H)$ et $\varinjlim\Gamma(X_\lambda-Z_\lambda,\sh H_\lambda)\to\Gamma(X-Z,\sh H)$
""",
    "Layout (display vs inline, GLOBAL_ISSUES 21). Apply BEFORE the next two convention-7 findings, whose 'old' lie inside this formula and survive this edit (not vice versa)."))

A(F(225, "proof of (19.9.8): 'lim Γ(X_λ—Z_λ, ℋ_λ)'",
    "long dash", "\\varinjlim\\Gamma(X_\\lambda-Z_\\lambda",
    'convention', 7, 'high',
    r"""\varinjlim\Gamma(X_\lambda-Z_\lambda""",
    r"""\varinjlim\Gamma(X_\lambda\setmin Z_\lambda""",
    "Apply after the display-to-inline finding just above (same formula)."))

A(F(225, "proof of (19.9.8): '→ Γ(X—Z, ℋ) sont bijectifs'",
    "long dash", "\\Gamma(X-Z,\\sh H)",
    'convention', 7, 'high',
    r"""\Gamma(X-Z,\sh H)""",
    r"""\Gamma(X\setmin Z,\sh H)""",
    "Apply after the display-to-inline finding above (same formula)."))

A(F(225, "proof of (19.9.8): 'sont bijectifs; en vertu de l'exactitude'",
    "'bijectifs' italic (crop p225_bijectifs.png)", "sont bijectifs; (roman)",
    'italics', None, 'high',
    r"""sont bijectifs;""",
    r"""sont \emph{bijectifs};""",
    "GLOBAL_ISSUES 83."))

A(F(225, "proof of (19.9.8): 'Γ(X_λ, ℋ_λ) → Γ(X_λ—Z_λ, ℋ_λ) est injectif'",
    "long dash", "\\Gamma(X_\\lambda-Z_\\lambda,\\sh H_\\lambda)$ est injectif",
    'convention', 7, 'high',
    r"""\Gamma(X_\lambda-Z_\lambda,\sh H_\lambda)$ est injectif""",
    r"""\Gamma(X_\lambda\setmin Z_\lambda,\sh H_\lambda)$ est injectif""",
    ""))

A(F(225, "proof of (19.9.8): 'on a prof((𝓕_{f(x)})_x)=prof(((𝓕_λ)_{f_λ(x_λ)})_{x_λ}) en vertu de (4.2.7)'",
    "the equality is set in the running text (crop p225_s2_a.png)",
    "displayed",
    'formula', None, 'high',
    r"""on a
\[
  \operatorname{prof}((\sh F_{f(x)})_x)
  =\operatorname{prof}(((\sh F_\lambda)_{f_\lambda(x_\lambda)})_{x_\lambda})
\]
en vertu""",
    r"""on a $\operatorname{prof}((\sh F_{f(x)})_x)=\operatorname{prof}(((\sh F_\lambda)_{f_\lambda(x_\lambda)})_{x_\lambda})$ en vertu""",
    "Layout only (display vs inline, GLOBAL_ISSUES 21); no connecting word lost or added."))

A(F(225, "proof of (19.9.8): 'dans le cas où A est noethérien, il faut prouver'",
    "'noethérien' italic (crop p225_s2_b.png)", "roman",
    'italics', None, 'high',
    r"""$A$ est noethérien, il faut""",
    r"""$A$ est \emph{noethérien}, il faut""",
    "GLOBAL_ISSUES 83. The later 'lorsque A est noethérien' (next paragraph) is roman in the print."))

A(F(225, "proof of (19.9.8): 'pour tout point x_λ∈Z_λ'",
    "'tout' italic (crop p225_s2_b.png)", "roman",
    'italics', None, 'high',
    r"""pour tout point $x_\lambda\in Z_\lambda$""",
    r"""pour \emph{tout} point $x_\lambda\in Z_\lambda$""",
    "GLOBAL_ISSUES 83."))

A(F(225, "proof of (19.9.8): 'que Z'_λ est ouvert dans Z_λ'",
    "'ouvert' italic (crop p225_s2_c.png)", "roman",
    'italics', None, 'high',
    r"""est ouvert dans $Z_\lambda$""",
    r"""est \emph{ouvert} dans $Z_\lambda$""",
    "GLOBAL_ISSUES 83."))

A(F(225, "end of the proof of (19.9.8): 'de (5.10.2) (resp. 5.10.4)).'",
    "'(resp. 5.10.4)).' with no opening parenthesis before 5.10.4 (crop p225_resp2.png)",
    "(resp. 5.10.4)) as printed",
    'misprint_in_print', None, 'high',
    None, None,
    "Unbalanced parentheses in the print; the TeX keeps the printed reading (no diplomatic fix).",
    corrected=r"""(5.10.2) (resp. (5.10.4))"""))

A(F(225, "Remarque (19.9.9): 'Sous les conditions générales de (19.9.8), supposons'",
    "(19.9.8) upright inside the italic phrase (crop p225_remark.png)", "inside \\emph",
    'convention', 6, 'high',
    r"""générales de (19.9.8), supposons""",
    r"""générales de \textup{(19.9.8)}, supposons""",
    "Reference printed upright inside the italic statement of the remark (judged as if the remark body were roman)."))

A(F(225, "Remarque (19.9.9), display 'H^i(X, ℋ) → H^i(X—Z, ℋ|(X—Z))'",
    "long dash twice (crop p225_Hi.png)", "H^i(X-Z,\\sh H|(X-Z))",
    'convention', 7, 'high',
    r"""H^i(X-Z,\sh H|(X-Z))""",
    r"""H^i(X\setmin Z,\sh H|(X\setmin Z))""",
    "Two occurrences in one formula."))

A(F(225, "Remarque (19.9.9): 'bijectif pour i≤k—2'",
    "long dash used as minus (crop p225_estbij.png)", "$i\\leq k-2$",
    'convention', 7, 'high',
    r"""$i\leq k-2$""",
    r"""$i\leq k\setmin 2$""",
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23)."))

A(F(225, "Remarque (19.9.9): 'injectif pour i=k—1'",
    "long dash used as minus (crop p225_estbij.png)", "$i=k-1$",
    'convention', 7, 'high',
    r"""$i=k-1$""",
    r"""$i=k\setmin 1$""",
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23)."))

A(F(225, "heading '20.0. Introduction.'",
    "'20.0. Introduction.' with a final full stop", "\\subsection{Introduction}",
    'punctuation', None, 'high',
    r"""\subsection{Introduction}""",
    r"""\subsection{Introduction.}""",
    "Subsection title full stop, as on the earlier IV-4 pages (GLOBAL_ISSUES 43/58). This text lies BEFORE THE FIRST MARKER of ega4-20-fr.tex (it opens that file; page_225.tex carries it as the continuation)."))

# ---------------------------------------------------------------- p. 226
A(F(226, "20.0: 'développer au § 21 (n^os 21.1 à 21.7)'",
    "'(n^os 21.1 à 21.7)': the numbers without parentheses (crop p226_s1_a.png)",
    "\\sref prints its own parentheses: '(n^os (21.1) à (21.7))'",
    'extra', None, 'high',
    r"""(n\textsuperscript{os} \sref{IV.21.1} à \sref{IV.21.7})""",
    r"""(n\textsuperscript{os} \hyperref[IV.21.1]{21.1} à \hyperref[IV.21.7]{21.7})""",
    "Labels IV.21.1 and IV.21.7 exist (ega4-21a, ega4-21b), so plain \\hyperref keeps the links."))

A(F(226, "20.0: 'en outre factoriels (21.6 et 21.7)'",
    "'(21.6 et 21.7)' (crop p226_s1_b.png)",
    "'(\\sref{IV.21.6} et \\sref{IV.21.7})' prints '((21.6) et (21.7))'",
    'extra', None, 'high',
    r"""(\sref{IV.21.6} et \sref{IV.21.7})""",
    r"""(\hyperref[IV.21.6]{21.6} et \hyperref[IV.21.7]{21.7})""",
    "Checked against the print: one pair of parentheses here, so the doubling is not real (ega4-20 line 13). Labels exist (ega4-21b). The real double parentheses on this page ('(dans (20.6), ...)' on p. 225, '(les n^os (21.9), (21.11) et (21.12)', 'Dans les n^os (21.13) et (21.14)') match the print and need no change."))

A(F(226, "20.0: 'Les n^os 21.11 et 21.12 donnent deux théorèmes'",
    "'Les n^os 21.11 et 21.12' without parentheses (crop p226_s2_a.png)",
    "\\sref prints '(21.11) et (21.12)'",
    'extra', None, 'high',
    r"""Les n\textsuperscript{os} \sref{IV.21.11} et \sref{IV.21.12} donnent""",
    r"""Les n\textsuperscript{os} \hyperref[IV.21.11]{21.11} et \hyperref[IV.21.12]{21.12} donnent""",
    "The later '(les n^os (21.9), (21.11) et (21.12)' and 'Dans les n^os (21.13) et (21.14)' do have parentheses in the print and need no change. Labels exist (ega4-21c)."))

A(F(226, "20.0: 'dus respectivement à Auslander-Buchsbaum'",
    "hyphen (crop p226_auslander.png)", "en dash",
    'punctuation', None, 'high',
    r"""Auslander--Buchsbaum""",
    r"""Auslander-Buchsbaum""",
    "As GLOBAL_ISSUES 74 (Cohen--Macaulay)."))

A(F(226, "20.0: '(théorème de Ramanujam-Samuel)'",
    "hyphen (crop p226_ramanujam.png)", "en dash",
    'punctuation', None, 'high',
    r"""Ramanujam--Samuel""",
    r"""Ramanujam-Samuel""",
    ""))

A(F(226, "heading '20.1. Fonctions méromorphes.'",
    "final full stop", "\\subsection{Fonctions méromorphes}",
    'punctuation', None, 'high',
    r"""\subsection{Fonctions méromorphes}""",
    r"""\subsection{Fonctions méromorphes.}""",
    "Subsection title full stop (GLOBAL_ISSUES 43/58)."))

A(F(226, "(20.1.1): 'l'application U⇝Γ(U, 𝒪_X)[Γ(U, 𝒮)^{-1}]'",
    "wavy arrow (crop p226_leadsto.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$U\mapsto\Gamma(U,\sh{O}_X)""",
    r"""$U\leadsto\Gamma(U,\sh{O}_X)""",
    ""))

A(F(226, "(20.1.1): 'préfaisceau d'anneaux (0_I, 1.5.1 et 1.5.7)'",
    "'(0_I, 1.5.1 et 1.5.7)': one pair of parentheses, bold 0 with a light subscript I (crop p226_0I.png)",
    "'(\\sref[0]{0.1.5.1} et \\sref[0]{0.1.5.7})' prints '((0, 1.5.1) et (0, 1.5.7))'",
    'extra', None, 'high',
    r"""(\sref[0]{0.1.5.1} et \sref[0]{0.1.5.7})""",
    r"""($\mathbf{0}_{\mathrm I}$, \EGAUnavailableHyperref{0.1.5.1}{1.5.1} et \EGAUnavailableHyperref{0.1.5.7}{1.5.7})""",
    "Checked against the print: here the doubled parentheses are NOT real (one pair in the print). Doubled parentheses (ega4-20 line 30) and the missing subscript I in one edit; bold 0 with light I written $\\mathbf{0}_{\\mathrm I}$ as in the \\sref[$\\mathbf{0}_{\\mathrm I}$] form; r@0.1.5.1, r@0.1.5.7 are undefined, so \\EGAUnavailableHyperref is the link \\sref itself makes (same construction as the pp. 230-234 fix of (0_I, 6.5.1 et 6.6.2))."))

A(F(226, "(20.1.1): 'c'est un 𝒪_X-Module plat'",
    "'Module' with a capital M (crop p226_moduleplat.png)", "module",
    'word', None, 'high',
    r"""$\sh{O}_X$-module \emph{plat}""",
    r"""$\sh{O}_X$-Module \emph{plat}""",
    "ega4-20 writes 'O_X$-module' 12 times; the print has 'Module' in the 10 on pp. 226-229."))

A(F(226, "(20.1.1.1): '(𝒪_X[𝒮^{-1}])_x ⥲ 𝒪_x[𝒮_x^{-1}]'",
    "isomorphism arrow (tilde over the arrow) (crop p226_20111.png)", "\\isoto (= \\simeq)",
    'convention', 4, 'high',
    r"""\sh{O}_X[\sh{S}^{-1}])_x\isoto""",
    r"""\sh{O}_X[\sh{S}^{-1}])_x\simto""",
    "\\simto is \\xrightarrow{\\sim} in preamble-base.tex (GLOBAL_ISSUES 34: \\isoto is \\simeq). Does not overlap the next finding."))

A(F(226, "(20.1.1.1): right-hand side '𝒪_x[𝒮_x^{-1}]', no comma after it",
    "𝒪_x (subscript x only) and no comma after the display (crop p226_20111.png)", "\\sh{O}_{X,x}[\\sh{S}_x^{-1}],",
    'formula', None, 'high',
    r"""\sh{O}_{X,x}[\sh{S}_x^{-1}],""",
    r"""\sh{O}_x[\sh{S}_x^{-1}]""",
    "The TeX rewrites the print's 𝒪_x (EGA's own notation for the local ring, not a misprint) as 𝒪_{X,x} and adds a comma the print does not have; one edit for both."))

A(F(226, "(20.1.1): 'car le raisonnement de (0_I, 1.4.5)'",
    "(0_I, 1.4.5) with the subscript I (page_226_s4.png)", "\\sref[0]{0.1.4.5} prints '(0, 1.4.5)'",
    'number', None, 'high',
    r"""raisonnement de \sref[0]{0.1.4.5}""",
    r"""raisonnement de \sref[$\mathbf{0}_{\mathrm I}$]{0.1.4.5}""",
    "Missing subscript I; bold 0 with a light I as in the print (coordinator form \\sref[$\\mathbf{0}_{\\mathrm I}$])."))

# ---------------------------------------------------------------- p. 227
A(F(227, "(20.1.1), first line: 'on prend alors pour S la limite inductive dans A=lim A'",
    "'A=lim A': no subscript α on the second A (crop p227_lim.png)", "$A=\\varinjlim A_\\alpha$",
    'misprint_in_print', None, 'high',
    r"""$A=\varinjlim A_\alpha$""",
    r"""$A=\varinjlim A$""",
    "The print drops the subscript; the TeX silently corrects it. The fix restores the printed reading.",
    corrected=r"""$A=\varinjlim A_\alpha$"""))

A(F(227, "(20.1.2): 'Soit maintenant 𝓕 un 𝒪_X-Module.'",
    "'Module', capital M, roman (crop p227_2012.png)", "module",
    'word', None, 'high',
    r"""maintenant $\sh{F}$ un $\sh{O}_X$-module.""",
    r"""maintenant $\sh{F}$ un $\sh{O}_X$-Module.""",
    ""))

A(F(227, "(20.1.2): 'au préfaisceau de modules U⇝Γ(U, 𝓕)[Γ(U, 𝒮)^{-1}]'",
    "wavy arrow (crop p227_s1_mid.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$U\mapsto\Gamma(U,\sh{F})""",
    r"""$U\leadsto\Gamma(U,\sh{F})""",
    ""))

A(F(227, "(20.1.2.2): '(𝓕[𝒮^{-1}])_x ⥲ 𝓕_x[𝒮_x^{-1}].'",
    "isomorphism arrow (crop p227_20122.png)", "\\isoto (= \\simeq)",
    'convention', 4, 'high',
    r"""(\sh{F}[\sh{S}^{-1}])_x\isoto""",
    r"""(\sh{F}[\sh{S}^{-1}])_x\simto""",
    "GLOBAL_ISSUES 34."))

A(F(227, "(20.1.3): '(et non seulement d'un préfaisceau) la régularité d'une section'",
    "no comma after the parenthesis (crop p227_prefaisceau.png)", "'préfaisceau), la régularité'",
    'punctuation', None, 'medium',
    r"""d'un préfaisceau), la régularité""",
    r"""d'un préfaisceau) la régularité""",
    "Comma added by the TeX; the print has none (sparse punctuation, not treated as a misprint)."))

A(F(227, "(20.1.3): 'le germe de la section en x est régulier dans 𝒪_X pour tout x∈U'",
    "𝒪_X (subscript capital X only) (crop p227_regulier.png)", "$\\sh{O}_{X,x}$",
    'misprint_in_print', None, 'medium',
    r"""régulier dans $\sh{O}_{X,x}$ pour tout""",
    r"""régulier dans $\sh{O}_X$ pour tout""",
    "The germ is regular in the stalk, as the next sentence has it (𝒪_{X,x}); the print's 𝒪_X is a slip (perhaps for 𝒪_x) and the TeX silently corrects it. The fix restores the printed reading.",
    corrected=r"""$\sh{O}_{X,x}$"""))

A(F(227, "(20.1.3): '(i.e. ... pour tout x∈U) autrement dit 𝒮(𝒪_X)_x'",
    "no comma after the parenthesis (crop p227_regulier.png)", "'), autrement dit'",
    'punctuation', None, 'medium',
    r"""$x\in U$), autrement dit""",
    r"""$x\in U$) autrement dit""",
    "Comma added by the TeX; the print has none. Does not overlap the previous finding."))

A(F(227, "(20.1.3): 'Pour tout 𝒪_X-Module 𝓕,'",
    "'Module' capital M and italic (crop p227_pourtoutmodule.png)", "roman 'module'",
    'word', None, 'high',
    r"""Pour tout $\sh{O}_X$-module $\sh{F}$,
""",
    r"""Pour tout $\sh{O}_X$-\emph{Module} $\sh{F}$,
""",
    "Capital M and italics in one edit ('old' ends with the line break, so it differs from the 'Pour tout ... $\\sh{F}$, on déduit' of p. 228)."))

A(F(227, "(20.1.3): '𝓜_X(𝓕)|U ⥲ 𝓜_U(𝓕|U)'",
    "isomorphism arrow (crop p227_s3_a.png)", "\\isoto (= \\simeq)",
    'convention', 4, 'high',
    r"""\sh{M}_X(\sh{F})|U\isoto""",
    r"""\sh{M}_X(\sh{F})|U\simto""",
    "GLOBAL_ISSUES 34."))

A(F(227, "(20.1.3): 'en particulier 𝓜_X|U ⥲ 𝓜_U'",
    "isomorphism arrow (crop p227_s3_a.png)", "\\isoto (= \\simeq)",
    'convention', 4, 'high',
    r"""\sh{M}_X|U\isoto""",
    r"""\sh{M}_X|U\simto""",
    "GLOBAL_ISSUES 34. With this page's other two, these are all 4 \\isoto of ega4-20."))

A(F(227, "(20.1.4): 'l'homomorphisme t⇝t/1'",
    "wavy arrow (crop p227_tt1.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$t\mapsto t/1$""",
    r"""$t\leadsto t/1$""",
    ""))

# ---------------------------------------------------------------- p. 228
A(F(228, "(20.1.4): 'Étant donnée une fonction méromorphe φ∈M(X)'",
    "the X of M(X) is a bold X, visibly heavier and wider-stroked than the M beside it and than the X of 'U de X' on the same line and of the other M(X) on pp. 227, 229 (crops p228_MX.png, p228_deX.png, p227_MX.png, p229_MX.png)",
    "M(X), ordinary X",
    'misprint_in_print', None, 'high',
    r"""$\vphi\in M(X)$""",
    r"""$\vphi\in M(\mathbf{X})$""",
    "Wrong-fount letter mid-line (GLOBAL_ISSUES 29/97): reproduced in the diplomatic text, normal X in the corrected edition. The TeX silently corrects it. (\\vphi left alone: preamble decision.)",
    corrected=r"""$\vphi\in M(X)$"""))

A(F(228, "(20.1.5): 'Pour tout 𝒪_X-Module 𝓕, on déduit'",
    "'Module', capital M, roman (crop p228_2015.png)", "module",
    'word', None, 'high',
    r"""Pour tout $\sh{O}_X$-module $\sh{F}$, on déduit""",
    r"""Pour tout $\sh{O}_X$-Module $\sh{F}$, on déduit""",
    ""))

A(F(228, "(20.1.5): 'l'homothétie z⇝sz de Γ(U, 𝓕)'",
    "wavy arrow (crop p228_zsz.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$z\mapsto sz$ de $\Gamma(U,\sh{F})$""",
    r"""$z\leadsto sz$ de $\Gamma(U,\sh{F})$""",
    ""))

A(F(228, "Proposition (20.1.6): '𝓕 un 𝒪_X-Module quasi-cohérent'",
    "'Module' with a capital M (crop p228_prop2016.png)", "module",
    'word', None, 'high',
    r"""$\sh{O}_X$-module quasi-cohérent""",
    r"""$\sh{O}_X$-Module quasi-cohérent""",
    ""))

A(F(228, "proof of (20.1.6): 'l'homothétie z⇝sz n'est pas injective'",
    "wavy arrow (page_228_s3.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$z\mapsto sz$ n'est pas injective""",
    r"""$z\leadsto sz$ n'est pas injective""",
    ""))

A(F(228, "(20.1.7): 'dire que u est définie dans U signifie que u|V est une section de 𝓕 au-dessus de U'",
    "'u|V' (crop p228_uV.png)", "$u|U$",
    'misprint_in_print', None, 'high',
    r"""signifie que $u|U$ est une""",
    r"""signifie que $u|V$ est une""",
    "The print has u|V where u|U is meant (u defined in U; V belongs to the previous sentence); the TeX silently corrects it. The fix restores the printed reading.",
    corrected=r"""$u|U$"""))

A(F(228, "(20.1.8): 'Conformément aux notations générales (0_I, 5.4.7)'",
    "bold 0, light subscript I (crop p228_s3_b.png)", "\\sref[0\\textsubscript{I}] sets the I bold",
    'font', None, 'high',
    r"""générales \sref[0\textsubscript{I}]{0.5.4.7}""",
    r"""générales \sref[$\mathbf{0}_{\mathrm I}$]{0.5.4.7}""",
    "Bold 0 with a light I as in the print; coordinator form \\sref[$\\mathbf{0}_{\\mathrm I}$]."))

A(F(228, "(20.1.8): 'Soit 𝓛 un 𝒪_X-Module inversible (0_I, 5.4.1)'",
    "'Module inversible' italic, capital M (crop p228_moduleinv.png)", "roman 'module inversible'",
    'word', None, 'high',
    r"""Soit $\sh{L}$ un $\sh{O}_X$-module inversible""",
    r"""Soit $\sh{L}$ un $\sh{O}_X$-\emph{Module inversible}""",
    "Capital M and italics in one edit. Does not overlap the next finding."))

A(F(228, "(20.1.8): '(0_I, 5.4.1)'",
    "bold 0, light subscript I (crop p228_moduleinv.png)", "\\sref[0\\textsubscript{I}] sets the I bold",
    'font', None, 'high',
    r"""\sref[0\textsubscript{I}]{0.5.4.1}""",
    r"""\sref[$\mathbf{0}_{\mathrm I}$]{0.5.4.1}""",
    "Bold 0 with a light I as in the print; coordinator form \\sref[$\\mathbf{0}_{\\mathrm I}$]."))

# ---------------------------------------------------------------- p. 229
A(F(229, "(20.1.8), first line of p. 229: 'est un 𝓜_X-Module inversible.'",
    "'Module inversible' italic, capital M (crop p229_Minv.png)", "roman 'module inversible'",
    'word', None, 'high',
    r"""est un $\sh{M}_X$-module inversible.""",
    r"""est un $\sh{M}_X$-\emph{Module inversible}.""",
    "Capital M and italics in one edit."))

A(F(229, "(20.1.8): 'élément inversible de Γ(U, 𝓜_X) (0_I, 5.4.7)'",
    "bold 0, light subscript I (crop p229_s1_a.png)", "\\sref[0\\textsubscript{I}] sets the I bold",
    'font', None, 'high',
    r"""$\Gamma(U,\sh{M}_X)$ \sref[0\textsubscript{I}]{0.5.4.7}""",
    r"""$\Gamma(U,\sh{M}_X)$ \sref[$\mathbf{0}_{\mathrm I}$]{0.5.4.7}""",
    "Bold 0 with a light I as in the print; coordinator form \\sref[$\\mathbf{0}_{\\mathrm I}$]."))

A(F(229, "(20.1.8): 'une section méromorphe régulière de 𝓛 au-dessus de U;'",
    "'au-dessus de U' roman (crop p229_audessus.png)", "inside \\emph",
    'italics', None, 'high',
    r"""\emph{section méromorphe régulière de $\sh{L}$ au-dessus de $U$}""",
    r"""\emph{section méromorphe régulière de $\sh{L}$} au-dessus de $U$""",
    ""))

A(F(229, "(20.1.8): 'l'homothétie t⇝ts'",
    "wavy arrow (page_229_s2.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$t\mapsto ts$""",
    r"""$t\leadsto ts$""",
    ""))

A(F(229, "(20.1.9): 'régulière du 𝒪_X-Module inversible 𝓛'",
    "'Module', capital M, roman (crop p229_s2_b.png)", "module",
    'word', None, 'high',
    r"""du $\sh{O}_X$-module inversible""",
    r"""du $\sh{O}_X$-Module inversible""",
    ""))

A(F(229, "(20.1.9): 'pour tout 𝒪_X-Module 𝓕, s définit'",
    "'Module', capital M, roman (crop p229_s2_b.png)", "module",
    'word', None, 'high',
    r"""pour tout $\sh{O}_X$-module $\sh{F}$, $s$""",
    r"""pour tout $\sh{O}_X$-Module $\sh{F}$, $s$""",
    ""))

A(F(229, "(20.1.10): 'd'un 𝒪_X-Module inversible 𝓛'",
    "'Module', capital M, roman (crop p229_s2_c.png)", "module",
    'word', None, 'high',
    r"""d'un $\sh{O}_X$-module inversible""",
    r"""d'un $\sh{O}_X$-Module inversible""",
    ""))

A(F(229, "(20.1.10): 'dans 𝓜_X (0_I, 5.4.3)'",
    "bold 0, light subscript I (crop p229_s2_c.png)", "\\sref[0\\textsubscript{I}] sets the I bold",
    'font', None, 'high',
    r"""\sref[0\textsubscript{I}]{0.5.4.3}""",
    r"""\sref[$\mathbf{0}_{\mathrm I}$]{0.5.4.3}""",
    "Bold 0 with a light I as in the print; coordinator form \\sref[$\\mathbf{0}_{\\mathrm I}$]."))

A(F(229, "(20.1.10): 'si 𝓛' est un second 𝒪_X-Module inversible'",
    "'Module', capital M, roman (crop p229_s3_a.png)", "module",
    'word', None, 'high',
    r"""second $\sh{O}_X$-module inversible""",
    r"""second $\sh{O}_X$-Module inversible""",
    ""))

A(F(229, "(20.1.11), display 'Γ(θ^♯) : Γ(U, 𝒪_X) → Γ(f^{-1}(U), 𝒪_X')'",
    "sharp sign ♯ (crop p229_sharp.png)", "\\theta^\\#",
    'convention', 9, 'high',
    r"""\Gamma(\theta^\#)""",
    r"""\Gamma(\theta^\sharp)""",
    ""))

A(F(229, "(20.1.11): 'Il est immédiat que U⇝𝒮_f(U) est un sous-faisceau'",
    "wavy arrow (page_229_s4.png)", "\\mapsto",
    'symbol', None, 'high',
    r"""$U\mapsto\sh{S}_f(U)$""",
    r"""$U\leadsto\sh{S}_f(U)$""",
    ""))


# ---------------------------------------------------------------- checks
def page_text(p):
    return open(RUN + 'page_%d.tex' % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')


ok = True
texts = {p: page_text(p) for p in range(225, 230)}
orig = dict(texts)
for i, f in enumerate(findings):
    fx = f['fix']
    if fx is None:
        continue
    p = f['page']
    o, n = fx['old'], fx['new']
    c0 = orig[p].count(o)
    c1 = texts[p].count(o)
    if c0 != 1 or c1 != 1:
        ok = False
        sys.stdout.buffer.write(('PROBLEM #%d p%d orig=%d seq=%d old=%r\n' % (i, p, c0, c1, o[:80])).encode('utf-8'))
    texts[p] = texts[p].replace(o, n, 1)
    if o == n:
        ok = False
        print('NOOP', i)
print('all olds unique (original and sequential):', ok)
counts = {}
for f in findings:
    c = counts.setdefault(f['page'], {'normal': 0, 'convention': 0, 'misprint': 0})
    if f['kind'] == 'convention':
        c['convention'] += 1
    elif f['kind'] == 'misprint_in_print':
        c['misprint'] += 1
    else:
        c['normal'] += 1
print(counts, 'total', len(findings))
json.dump(findings, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
print('written', OUT)
# write the sequentially fixed texts for inspection
for p, t in texts.items():
    open(RUN + 'crops_225_229/fixed_%d.tex' % p, 'w', encoding='utf-8', newline='\n').write(t)
