import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = os.path.join(RUN, "findings_151_155.json")
NL = "\u00b6"  # newline token inside raw strings


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": s(tex),
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": s(old), "new": s(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


# ---------------- page 151 ----------------
add(151, "(20.7.14): 'l'homomorphisme (20.7.14.1) est surjectif, comme il résulte de (20.4.7)'",
    "est surjectif (italic), comme", r"est surjectif, comme il", "italics",
    r"est surjectif, comme il", r"est \emph{surjectif}, comme il")
add(151, "(20.7.14): 'on a de / de même un homomorphisme surjectif' (the first 'de' ends a printed line)",
    "on a de de même un homomorphisme surjectif", r"on a de même un", "misprint_in_print",
    r"on a de même un", r"on a de de même un",
    corrected=r"on a de même un",
    note="Doubled 'de' across a line break in the print; the TeX silently corrects it.")
add(151, "(20.7.14): unnumbered display of the transition homomorphisms",
    "φ_{(𝔐',𝔑'),(𝔐'',𝔑'')} : Ω¹_{B''/A''} → Ω¹_{B'/A'} (the single-primed pair first)",
    r"\varphi_{(\mathfrak{M}'',\mathfrak{N}''),(\mathfrak{M}',\mathfrak{N}')}", "formula",
    r"\varphi_{(\mathfrak{M}'',\mathfrak{N}''),(\mathfrak{M}',\mathfrak{N}')}",
    r"\varphi_{(\mathfrak{M}',\mathfrak{N}'),(\mathfrak{M}'',\mathfrak{N}'')}",
    note="The TeX swaps the two index pairs.")
add(151, "(20.7.14): 'est surjectif pour tout couple (𝔐',𝔑')' after (20.7.14.3)",
    "est surjectif (italic) pour tout couple", r"est surjectif pour tout couple", "italics",
    r"est surjectif pour tout couple", r"est \emph{surjectif} pour tout couple")
add(151, "(20.7.14): 'si L est un B-module topologique séparé et complet'",
    "séparé (italic) et (roman) complet (italic)", r"\emph{séparé et complet}", "italics",
    r"\emph{séparé et complet}", r"\emph{séparé} et \emph{complet}",
    note="'et' is roman in the print.")
add(151, "(20.7.14): 'Plus particulièrement, si L est un B-module discret' after the Hom. cont display",
    "new indented paragraph after the display", r"no blank line after \]", "other",
    r"\]¶Plus particulièrement", r"\]¶¶Plus particulièrement",
    note="Paragraph break after a display (GLOBAL_ISSUES 47).")
add(151, "Proposition (20.7.15): 'B une A-algèbre topologique adique (0_I, 7.1.9)'",
    "(0_I, 7.1.9) upright inside the italic statement", r"($\mathbf{0}_{\mathrm I}$, 7.1.9)", "convention",
    r"($\mathbf{0}_{\mathrm I}$, 7.1.9)", r"\textup{($\mathbf{0}_{\mathrm I}$, 7.1.9)}", conv=6)
add(151, "Proposition (20.7.15), last sentence: 'Alors Ω̂¹_{B/A} est un B-module de type fini'",
    "B-module (no hat on B)", r"$\widehat B$-module de type fini", "formula",
    r"$\widehat B$-module de type fini", r"$B$-module de type fini",
    note="Not a misprint: B is adic, hence complete (B̂ = B).")

# ---------------- page 152 ----------------
add(152, "(20.7.16): '(à l'aide de (20.4.13, (i)) et de (20.5.9) notamment'",
    "(20.4.13, (i))", r"\sref{0.20.4.13-fr}, (i) (renders '(20.4.13), (i)')", "punctuation",
    r"\sref{0.20.4.13-fr}, (i) et de", r"(\ref{0.20.4.13-fr}, (i)) et de",
    note="\\sref adds its own parentheses (\\newcommand{\\sref}[1]{(\\ref{#1})}); the print closes the parenthesis after (i).")
add(152, "(20.7.17): 'C'=C/𝔓' avec u(𝔐')⊂𝔑''",
    "no comma before 'avec'", r"$C'=C/\mathfrak{P}'$, avec", "punctuation",
    r"$C'=C/\mathfrak{P}'$, avec", r"$C'=C/\mathfrak{P}'$ avec")
add(152, "(20.7.17): 'v(N')⊂𝔓''",
    "v(N') with a roman capital N (the neighbouring 𝔑' is Fraktur)", r"v(\mathfrak{N}')", "misprint_in_print",
    r"v(\mathfrak{N}')", r"v(N')", corrected=r"v(\mathfrak{N}')",
    note="Wrong-font letter in the print; the TeX silently corrects it.")
add(152, "(20.7.17): display of the exact sequence (20.5.7.1)",
    "... Ω¹_{C/B} → 0 (no colon)", r"\Omega^1_{C/B}\to0:", "punctuation",
    r"\Omega^1_{C/B}\to0:", r"\Omega^1_{C/B}\to0")
add(152, "(20.7.17.1)", "... → Ω̂¹_{C/A} (no comma)", r"&\to\widehat{\Omega}^1_{C/A},", "punctuation",
    r"&\to\widehat{\Omega}^1_{C/A},", r"&\to\widehat{\Omega}^1_{C/A}")
add(152, "(20.7.17.2)", "... → Ω̂¹_{C/B} (no full stop)", r"\widehat{\Omega}^1_{C/B}. \tag{20.7.17.2}", "punctuation",
    r"\widehat{\Omega}^1_{C/B}. \tag{20.7.17.2}", r"\widehat{\Omega}^1_{C/B} \tag{20.7.17.2}")
add(152, "(20.7.17), last sentence: 'sont surjectifs (20.7.14)'",
    "surjectifs (italic)", r"sont surjectifs", "italics",
    r"sont surjectifs", r"sont \emph{surjectifs}")
add(152, "Proposition (20.7.18): 'On suppose B et C admissibles (0_I, 7.1.2) et métrisables'",
    "(0_I, 7.1.2) upright inside the italic statement", r"($\mathbf{0}_{\mathrm I}$, 7.1.2)", "convention",
    r"($\mathbf{0}_{\mathrm I}$, 7.1.2)", r"\textup{($\mathbf{0}_{\mathrm I}$, 7.1.2)}", conv=6)
add(152, "Proposition (20.7.18): 'Pour que l'homomorphisme canonique v̂_{C/B/A} : Ω̂¹_{B/A}⊗̂_B C → Ω̂¹_{C/A} admette...'",
    "formula in the running text (not displayed); ⊗̂_B C without hats on B and C",
    r"\[ \widehat v_{C/B/A}:\widehat{\Omega}^1_{B/A}\widehat\otimes_{\widehat B}\widehat C\to\widehat{\Omega}^1_{C/A} \] (displayed)",
    "formula",
    r"canonique¶\[¶  \widehat v_{C/B/A}:\widehat{\Omega}^1_{B/A}¶  \widehat\otimes_{\widehat B}\widehat C\to\widehat{\Omega}^1_{C/A}¶\]¶admette",
    r"canonique $\widehat v_{C/B/A}:\widehat{\Omega}^1_{B/A}\widehat\otimes_B C\to\widehat{\Omega}^1_{C/A}$¶admette",
    note="One edit for two differences: the print sets the formula inline, and has plain B, C (B, C are complete here).")
add(152, "proof of (20.7.18): 'le C-module topologique L=Ω̂¹_{B/A}⊗̂_B C est métrisable'",
    "⊗̂_B C (no hats on B, C)", r"$L=\widehat{\Omega}^1_{B/A}\widehat\otimes_{\widehat B}\widehat C$", "formula",
    r"$L=\widehat{\Omega}^1_{B/A}\widehat\otimes_{\widehat B}\widehat C$",
    r"$L=\widehat{\Omega}^1_{B/A}\widehat\otimes_B C$")

# ---------------- page 153 ----------------
add(153, "page break 152/153: printed p. 152 ends '...complet en vertu de l'hypothèse, donc E=D_C(L), muni de la topologie produit, est'; p. 153 begins 'métrisable et complet;'",
    "p. 153 begins with 'métrisable et complet; il est en outre admissible'",
    r"\oldpage{153} stands before 'complet en vertu de l'hypothèse'", "marker",
    r"\oldpage[0\textsubscript{IV-1}]{153}¶complet en vertu de l'hypothèse, donc $E=D_C(L)$, muni de la topologie produit,¶est métrisable",
    r"complet en vertu de l'hypothèse, donc $E=D_C(L)$, muni de la topologie produit,¶est¶\oldpage[0\textsubscript{IV-1}]{153}¶métrisable",
    note="The marker moves one printed line later (mid-sentence, no blank lines).")
add(153, "proof of (20.7.18): 'car si 𝔎 est un idéal de définition dans C'",
    "Fraktur K (same glyph as the 𝔎 of p. 52)", r"\mathfrak{R}", "symbol",
    r"car si $\mathfrak{R}$", r"car si $\mathfrak{K}$")
add(153, "proof of (20.7.18): '(𝔎⊕L)^n=𝔎^n⊕𝔎^{n-1}L'",
    "Fraktur K, three times", r"\mathfrak{R} (3 times)", "symbol",
    r"$(\mathfrak{R}\oplus L)^n=\mathfrak{R}^n\oplus\mathfrak{R}^{n-1}L$",
    r"$(\mathfrak{K}\oplus L)^n=\mathfrak{K}^n\oplus\mathfrak{K}^{n-1}L$")
add(153, "proof of (20.7.18): display D : B → Ω¹_{B/A} → Ω̂¹_{B/A}⊗̂_B C = L",
    "⊗̂_B C (no hats on B, C)", r"\widehat\otimes_{\widehat B}\widehat C=L", "formula",
    r"\widehat\otimes_{\widehat B}\widehat C=L", r"\widehat\otimes_B C=L")
add(153, "proof of (20.7.18): display f : x ⇝ (v(x), D(x))",
    "wavy arrow ⇝", r"\longmapsto", "symbol",
    r"f:x\longmapsto(v(x),D(x))", r"f:x\leadsto(v(x),D(x))")
add(153, "proof of (20.7.18): 'une structure de B-extension'",
    "extension (italic)", r"structure de $B$-extension", "italics",
    r"structure de $B$-extension", r"structure de $B$-\emph{extension}")
add(153, "proof of (20.7.18): 'g est de la forme y ⇝ (y, D'(y))'",
    "wavy arrow ⇝", r"$y\mapsto(y,D'(y))$", "symbol",
    r"$y\mapsto(y,D'(y))$", r"$y\leadsto(y,D'(y))$")
add(153, "end of the proof of (20.7.18): 'donne bien h∘v̂_{C/B/A}=1_L. C.Q.F.D.'",
    "C.Q.F.D. after 1_L.", r"$h\circ\widehat v_{C/B/A}=1_L$.", "missing",
    r"$h\circ\widehat v_{C/B/A}=1_L$.", r"$h\circ\widehat v_{C/B/A}=1_L$. C.Q.F.D.",
    note="The proof environment adds no C.Q.F.D.; the sources write it literally elsewhere.")
add(153, "Corollaire (20.7.19): 'Sous les hypothèses de (20.7.18)'",
    "(20.7.18) upright inside the italic statement", r"\sref{0.20.7.18-fr}", "convention",
    r"\sref{0.20.7.18-fr}, si", r"\textup{\sref{0.20.7.18-fr}}, si", conv=6)
add(153, "proof of (20.7.19): 'les topologies de Ω̂¹_{B/A}⊗̂_B C et de Ω̂¹_{C/A}'",
    "⊗̂_B C (no hats on B, C)", r"\widehat\otimes_{\widehat B}\widehat C", "formula",
    r"$\widehat{\Omega}^1_{B/A}\widehat\otimes_{\widehat B}\widehat C$ et de",
    r"$\widehat{\Omega}^1_{B/A}\widehat\otimes_B C$ et de")
add(153, "proof of (20.7.19): 'est nécessairement continu.'",
    "continu (italic)", r"nécessairement continu.", "italics",
    r"nécessairement continu.", r"nécessairement \emph{continu}.")
add(153, "(20.7.20): 'B une A-algèbre topologique métrisable et complète'",
    "métrisable (italic) et (roman) complète (italic)", r"\emph{métrisable et complète}", "italics",
    r"\emph{métrisable et complète}", r"\emph{métrisable} et \emph{complète}")
add(153, "(20.7.20): '𝔎 un idéal fermé de B'", "Fraktur K", r"\mathfrak{R}", "symbol",
    r"$\mathfrak{R}$ un idéal", r"$\mathfrak{K}$ un idéal")
add(153, "(20.7.20): 'C=B/𝔎 l'anneau topologique quotient'", "Fraktur K", r"\mathfrak{R}", "symbol",
    r"$C=B/\mathfrak{R}$", r"$C=B/\mathfrak{K}$")
add(153, "(20.7.20): '𝔎_k=(𝔎+𝔐_k)/𝔐_k'", "Fraktur K, twice", r"\mathfrak{R} (twice)", "symbol",
    r"$\mathfrak{R}_k=(\mathfrak{R}+\mathfrak{M}_k)/\mathfrak{M}_k$",
    r"$\mathfrak{K}_k=(\mathfrak{K}+\mathfrak{M}_k)/\mathfrak{M}_k$")
add(153, "(20.7.20): 'C_k=B_k/𝔎_k'", "Fraktur K", r"\mathfrak{R}", "symbol",
    r"$C_k=B_k/\mathfrak{R}_k$", r"$C_k=B_k/\mathfrak{K}_k$")
add(153, "(20.7.20): 'On a un système projectif d'homomorphismes δ_{C_k/B_k/A} : 𝔎_k/𝔎_k² → Ω¹_{B_k/A}⊗_{B_k}C_k (20.5.11.3), d'où'",
    "formula in the running text (not displayed), with Fraktur K",
    r"\[ \delta_{C_k/B_k/A}:\mathfrak{R}_k/\mathfrak{R}_k^2\to\Omega^1_{B_k/A}\otimes_{B_k}C_k \] (displayed)",
    "formula",
    r"d'homomorphismes¶\[¶  \delta_{C_k/B_k/A}:\mathfrak{R}_k/\mathfrak{R}_k^2\to¶  \Omega^1_{B_k/A}\otimes_{B_k}C_k¶\]¶\sref{0.20.5.11.3-fr}",
    r"d'homomorphismes¶$\delta_{C_k/B_k/A}:\mathfrak{K}_k/\mathfrak{K}_k^2\to\Omega^1_{B_k/A}\otimes_{B_k}C_k$¶\sref{0.20.5.11.3-fr}",
    note="One edit for two differences: inline formula, and the two Fraktur K (written \\mathfrak{R}).")
add(153, "(20.7.20): display δ̂_{C/B/A} : 𝔎/𝔎² → Ω̂¹_{B/A}⊗̂_B C", "Fraktur K, twice", r"\mathfrak{R}/\mathfrak{R}^2", "symbol",
    r"\widehat\delta_{C/B/A}:\mathfrak{R}/\mathfrak{R}^2", r"\widehat\delta_{C/B/A}:\mathfrak{K}/\mathfrak{K}^2")
add(153, "(20.7.20): display δ̂_{C/B/A} : 𝔎/𝔎² → Ω̂¹_{B/A}⊗̂_B C",
    "⊗̂_B C (no hats on B, C)", r"\widehat\otimes_{\widehat B}\widehat C", "formula",
    r"\widehat\otimes_{\widehat B}\widehat C¶\]", r"\widehat\otimes_B C¶\]")
add(153, "(20.7.20), last sentence: 'û_{C/B/A} : Ω̂¹_{B/A}⊗̂_B C → Ω̂¹_{C/A} est surjectif'",
    "⊗̂_B C (no hats on B, C)", r"\widehat\otimes_{\widehat B}\widehat C", "formula",
    r"\widehat\otimes_{\widehat B}\widehat C\to\widehat{\Omega}^1_{C/A}$ est",
    r"\widehat\otimes_B C\to\widehat{\Omega}^1_{C/A}$ est")
add(153, "(20.7.20), last sentence: 'l'homomorphisme canonique û_{C/B/A} : Ω̂¹_{B/A}⊗̂_B C → Ω̂¹_{C/A} est surjectif'",
    "û_{C/B/A}", r"\widehat u_{C/B/A}:\widehat{\Omega}^1_{B/A}", "misprint_in_print",
    None, None, conf="medium", corrected=r"\widehat v_{C/B/A}",
    note="The TeX keeps the printed reading. By (20.7.17.1) the map Ω̂¹_{B/A}⊗̂C → Ω̂¹_{C/A} is v̂_{C/B/A}; û_{C/B/A} goes to Ω̂¹_{C/B}.")
add(153, "(20.7.20), last sentence: 'Im(δ̂_{C/B/A}) est dense dans Ker(û_{C/B/A})'",
    "Ker(û_{C/B/A})", r"\operatorname{Ker}(\widehat u_{C/B/A})", "misprint_in_print",
    None, None, conf="medium", corrected=r"\operatorname{Ker}(\widehat v_{C/B/A})",
    note="The TeX keeps the printed reading; same slip as the previous entry (should be v̂).")

# ---------------- page 154 ----------------
add(154, "heading 21.1: 'Systèmes de p-générateurs et p-bases.'",
    "p bold upright, in the heading's type (as in the § 21 title on p. 153, where the TeX has a plain p)",
    r"$p$ (math italic, not bold)", "font",
    r"\subsection{Systèmes de $p$-générateurs et $p$-bases}",
    r"\subsection{Systèmes de p-générateurs et p-bases}", conf="medium",
    note="Heading typography; the subsection title's final full stop is the known document-wide item.")
add(154, "(21.1.1): 'un anneau A est de caractéristique p s'il existe'",
    "de caractéristique p (italic)", r"est de caractéristique $p$ s'il existe", "italics",
    r"est de caractéristique $p$ s'il existe", r"est \emph{de caractéristique $p$} s'il existe")
add(154, "(21.1.1): 'où P est le corps premier de caractéristique p'",
    "corps premier (italic)", r"le corps premier de", "italics",
    r"le corps premier de", r"le \emph{corps premier} de")
add(154, "(21.1.1): 'que A contient un corps de caractéristique p, l'image'",
    "contient un corps de caractéristique p (italic)", r"contient un corps de caractéristique $p$", "italics",
    r"$A$ contient un corps de¶caractéristique $p$, l'image",
    r"$A$ \emph{contient un corps de¶caractéristique $p$}, l'image")
add(154, "(21.1.2): 'on a p.1=0'", "p.1 with a baseline full stop", r"$p\cdot1=0$", "symbol",
    r"$p\cdot1=0$", r"$p.1=0$")
add(154, "(21.1.2): 'pour tout entier n≠0, n.1 est inversible'", "n.1 with a baseline full stop", r"$n\cdot1$", "symbol",
    r"que pour tout entier $n\neq0$, $n\cdot1$", r"que pour tout entier $n\neq0$, $n.1$")
add(154, "(21.1.2): 'n.1 est inversible dans A'", "inversible (italic)", r"est inversible dans $A$", "italics",
    r"est inversible dans $A$. Si", r"est \emph{inversible} dans $A$. Si")
add(154, "(21.1.2): 'cela résulte de ce qui précède et de l'identité de Bezout'",
    "cela résulte de ce qui précède et de l'identité", r"cela résulte de l'identité", "missing",
    r"cela résulte de¶l'identité", r"cela résulte de ce qui précède et de¶l'identité")
add(154, "(21.1.2): 'l'identité de Bezout'", "Bezout (no accent)", r"Bézout", "word",
    r"Bézout", r"Bezout")
add(154, "(21.1.2): 'Par contre l'anneau réduit à 0'", "no comma after 'Par contre'", r"Par contre, l'anneau", "punctuation",
    r"Par contre, l'anneau", r"Par contre l'anneau")
add(154, "(21.1.2): 'pour tout p.'", "tout (italic)", r"pour tout $p$.", "italics",
    r"pour tout $p$.", r"pour \emph{tout} $p$.")
add(154, "(21.1.3): 'il en est de même de toute algèbre sur A'", "algèbre (italic)", r"toute algèbre sur", "italics",
    r"toute algèbre sur", r"toute \emph{algèbre} sur")
add(154, "(21.1.3): 'le corps résiduel de A en 𝔭'", "corps résiduel (italic)", r"le corps résiduel de $A$ en $\mathfrak p$", "italics",
    r"le corps¶résiduel de $A$ en $\mathfrak p$", r"le \emph{corps¶résiduel} de $A$ en $\mathfrak p$")
add(154, "(21.1.3): 'si p=0 et si pour tout idéal maximal 𝔪'", "no comma after 'et si'", r"et si, pour", "punctuation",
    r"et si, pour", r"et si pour")
add(154, "(21.1.3): 'pour tout idéal maximal 𝔪 de A'", "maximal (italic)", r"idéal maximal", "italics",
    r"idéal maximal", r"idéal \emph{maximal}")
add(154, "(21.1.3): 'n≠0, n.1 est alors inversible'", "n.1 with a baseline full stop", r"$n\cdot1$", "symbol",
    r"$n\cdot1$ est alors", r"$n.1$ est alors")
add(154, "(21.1.3): 'l'exemple de l'anneau premier (intègre) Z_{pZ}'", "anneau premier (italic)", r"l'anneau premier", "italics",
    r"l'anneau¶premier", r"l'\emph{anneau¶premier}")
add(154, "(21.1.3): 'l'anneau premier (intègre) Z_{pZ} (19.8.3)'", "(intègre) before Z_{pZ}", r"(missing)", "missing",
    r"$\mathbf Z_{p\mathbf Z}$ (19.8.3)", r"(intègre) $\mathbf Z_{p\mathbf Z}$ (19.8.3)")
add(154, "(21.1.3), 2nd paragraph: 'Notons enfin que pour un anneau (même réduit)'", "no comma after 'que'",
    r"Notons enfin que, pour", "punctuation",
    r"Notons enfin que, pour", r"Notons enfin que pour")
add(154, "(21.1.4): 'nous supposons fixés un nombre premier p'",
    "fixés", r"fixé", "misprint_in_print",
    r"supposons fixé", r"supposons fixés", conf="medium", corrected=r"supposons fixé",
    note="Agreement slip in the print (the object is 'un nombre premier p'); the TeX silently corrects it.")
add(154, "(21.1.4): 'un nombre premier p et tous les anneaux'", "nombre premier p (italic)", r"un nombre premier $p$", "italics",
    r"un nombre premier¶$p$ et tous", r"un \emph{nombre premier¶$p$} et tous")
add(154, "(21.1.4): 'seront supposés de caractéristique p, sauf'", "de caractéristique p (italic)",
    r"supposés de caractéristique $p$", "italics",
    r"seront supposés de caractéristique $p$, sauf", r"seront supposés \emph{de caractéristique $p$}, sauf")
add(154, "(21.1.4): 'l'application x ⇝ x^p'", "wavy arrow ⇝", r"$x\mapsto x^p$", "symbol",
    r"l'application $x\mapsto x^p$", r"l'application $x\leadsto x^p$")
add(154, "(21.1.4): 'est un endomorphisme de A'", "endomorphisme (italic)", r"est un endomorphisme de $A$", "italics",
    r"est un endomorphisme de $A$", r"est un \emph{endomorphisme} de $A$")
add(154, "(21.1.4): 'si A est réduit'", "réduit (italic)", r"$A$ est réduit,", "italics",
    r"$A$ est réduit,", r"$A$ est \emph{réduit},")
add(154, "(21.1.4): 'F_A est injectif'", "injectif (italic)", r"est injectif. On pose", "italics",
    r"est injectif. On pose", r"est \emph{injectif}. On pose")
add(154, "(21.1.4): '(sous-anneau de A formé des x^p, pour x∈A)'", "pour x∈A", r"$x^p$, $x\in A$", "missing",
    r"$x^p$,¶$x\in A$)", r"$x^p$,¶pour $x\in A$)")
add(154, "(21.1.4), 2nd paragraph: 'comme une A-algèbre au moyen de l'homomorphisme F_A'",
    "algèbre au moyen de l'homomorphisme (italic)", r"$A$-algèbre au moyen de l'homomorphisme", "italics",
    r"$A$-algèbre au moyen de¶l'homomorphisme", r"$A$-\emph{algèbre au moyen de¶l'homomorphisme}")
add(154, "(21.1.4), 2nd paragraph: 'F_A : x ⇝ x^p de A dans A'", "wavy arrow ⇝", r"$F_A:x\mapsto x^p$", "symbol",
    r"$F_A:x\mapsto x^p$", r"$F_A:x\leadsto x^p$")
add(154, "(21.1.4), 2nd paragraph: 'il s'agit de la A-algèbre A_{[F_A]}, pour laquelle'",
    "de la A-algèbre A_{[F_A]}, pour laquelle", r"de l'algèbre $A^{(p)}$ pour laquelle", "word",
    r"s'agit de l'algèbre $A^{(p)}$ pour laquelle", r"s'agit de la $A$-algèbre $A_{[F_A]}$, pour laquelle",
    note="The print introduces A^{(p)} only in the next sentence (see the next entries).")
add(154, "(21.1.4), 2nd paragraph: 'le produit λ.x de x∈A'", "λ.x with a baseline full stop", r"$\lambda\cdot x$", "symbol",
    r"$\lambda\cdot x$", r"$\lambda.x$")
add(154, "(21.1.4), 2nd paragraph: 'dans l'anneau A; nous noterons cette A-algèbre A^{(p)}. Il est clair'",
    "; nous noterons cette A-algèbre A^{(p)}", r"l'anneau $A$. Il est clair", "missing",
    r"l'anneau $A$.", r"l'anneau $A$~; nous noterons cette $A$-algèbre $A^{(p)}$.")
add(154, "(21.1.4), 2nd paragraph: 'Il est clair que pour tout homomorphisme d'anneaux u : A→B le couple'",
    "no commas around 'pour tout homomorphisme d'anneaux u : A→B'", r"que, pour ... $u:A\to B$, le couple", "punctuation",
    r"Il est clair que, pour tout homomorphisme d'anneaux $u:A\to B$,¶le couple",
    r"Il est clair que pour tout homomorphisme d'anneaux $u:A\to B$¶le couple")
add(154, "(21.1.4), 2nd paragraph: 'est un di-homomorphisme d'algèbres'", "di-homomorphisme (italic)",
    r"est un di-homomorphisme", "italics",
    r"est un di-homomorphisme", r"est un \emph{di-homomorphisme}")
add(154, "(21.1.4), 2nd paragraph: 'on posera E^{(p)}=E⊗_A A^{(p)}'", "posera", r"on pose", "word",
    r"on pose $E^{(p)}", r"on posera $E^{(p)}")
add(154, "(21.1.4), 2nd paragraph: 'E⊗_A A^{(p)} où A^{(p)} est considéré'", "no comma before 'où'", r"A^{(p)}$, où", "punctuation",
    r"A^{(p)}$, où", r"A^{(p)}$ où")
add(154, "(21.1.4), 2nd paragraph: 'celle qu'on vient de définir, et la structure de A-module à droite'",
    "comma before 'et'", r"vient de définir et la structure", "punctuation",
    r"vient de définir et la structure", r"vient de définir, et la structure")
add(154, "(21.1.4), 2nd paragraph: 'dans A; E^{(p)} est muni de la structure de A-module provenant de la structure de A-module à droite de A^{(p)}, de sorte que pour x∈E, α, β dans A, on a'",
    "E^{(p)} est muni de la structure de A-module provenant de la structure de A-module à droite de A^{(p)}, de sorte que pour x∈E, α, β dans A, on a",
    r"ainsi, pour $x\in E$, $\alpha,\beta\in A$, on a", "missing",
    r"ainsi, pour¶$x\in E$, $\alpha,\beta\in A$, on a",
    r"$E^{(p)}$ est muni de la structure de $A$-module provenant de la structure de $A$-module à droite de $A^{(p)}$, de sorte que pour¶$x\in E$, $\alpha$, $\beta$ dans $A$, on a",
    note="The TeX paraphrases this clause.")
add(154, "(21.1.4), final display: 'α(x⊗β)=x⊗(αβ)   et   (αx)⊗β=...'",
    "connecting word 'et' between the two formulas, no comma", r"x\otimes(\alpha\beta),\qquad", "missing",
    r"x\otimes(\alpha\beta),\qquad", r"x\otimes(\alpha\beta)\qquad\text{et}\qquad")
add(154, "(21.1.4), final display: '(αx)⊗β=α^p(x⊗β)=x⊗α^pβ.'",
    "middle member α^p(x⊗β)", r"(\alpha x)\otimes\beta=x\otimes\alpha^p\beta.", "formula",
    r"(\alpha x)\otimes\beta=x\otimes\alpha^p\beta.", r"(\alpha x)\otimes\beta=\alpha^p(x\otimes\beta)=x\otimes\alpha^p\beta.")
add(154, "end of p. 154 / top of p. 155: (21.1.4) continues after the display with 'Posant x^{(p)}=x⊗1' (not indented)",
    "no paragraph break after the display; (21.1.4) ends after '...sur son sous-anneau A^p.' on p. 155",
    r"\end{env} and a blank line after the display", "other",
    r"\]¶\end{env}¶¶", r"\]¶",
    note="Apply together with the p. 155 entry that re-inserts \\end{env} after '$A^p$.'.")

# ---------------- page 155 ----------------
add(155, "top of p. 155: end of (21.1.4)", "(21.1.4) ends after 'sur son sous-anneau A^p.'",
    r"\end{env} is in the p. 154 segment", "other",
    r"$A^p$.¶¶\begin{proposition}[21.1.5]", r"$A^p$.¶\end{env}¶¶\begin{proposition}[21.1.5]",
    note="Apply together with the p. 154 entry that removes \\end{env} and the blank line after the display.")
add(155, "(21.1.4), end: 'Lorsque F_A est injectif'", "injectif (italic)", r"est injectif, on peut", "italics",
    r"est injectif, on peut", r"est \emph{injectif}, on peut")
add(155, "(21.1.4), end: 'algèbre sur son sous-anneau A^p'", "sous-anneau (italic)", r"son sous-anneau", "italics",
    r"son sous-anneau", r"son \emph{sous-anneau}")
add(155, "Proposition (21.1.5), label (i)", "(i) upright", r"\item[(i)]", "convention",
    r"\item[(i)] Toute", r"\item[\textup{(i)}] Toute", conv=6)
add(155, "Proposition (21.1.5), label (ii)", "(ii) upright", r"\item[(ii)]", "convention",
    r"\item[(ii)] Pour toute", r"\item[\textup{(ii)}] Pour toute", conv=6)
add(155, "Proposition (21.1.5), label (iii)", "(iii) upright", r"\item[(iii)]", "convention",
    r"\item[(iii)] Supposons", r"\item[\textup{(iii)}] Supposons", conv=6)
add(155, "proof of (21.1.5)(i): 'D : B→L, que l'on a D(x^k)=...'", "que l'on a", r"que $D(x^n)", "missing",
    r"L$, que $D", r"L$, que l'on a $D")
add(155, "proof of (21.1.5)(i): 'D(x^k)=kx^{k-1}D(x)'", "exponent letter k", r"D(x^n)=nx^{n-1}D(x)", "formula",
    r"(x^n)=nx^{n-1}", r"(x^k)=kx^{k-1}")
add(155, "proof of (21.1.5)(ii): 'cette dernière s'écrivant Dér_A(B, L)=Dér_{A[B^p]}(B, L)'",
    "Dér_A(B, L) = Dér_{A[B^p]}(B, L) (accent; Dér_A on the left)",
    r"$\operatorname{Der}_{A[B^p]}(B,L)=\operatorname{Der}_A(B,L)$", "formula",
    r"$\operatorname{Der}_{A[B^p]}(B,L)=\operatorname{Der}_A(B,L)$",
    r"$\operatorname{D\acute{e}r}_A(B,L)=\operatorname{D\acute{e}r}_{A[B^p]}(B,L)$",
    note="Two differences in one formula: 'Dér' with the accent (as Dér. cont on p. 151) and the two sides swapped.")
add(155, "proof of (21.1.5)(iii): '(x⊗1—1⊗x)^{p^s}'", "long dash", r"(x\otimes1-1\otimes x)", "convention",
    r"(x\otimes1-1\otimes x)", r"(x\otimes1\setmin1\otimes x)", conv=7,
    note="Subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes.")
add(155, "proof of (21.1.5)(iii): '=x^{p^s}⊗1—1⊗x^{p^s}'", "long dash", r"x^{p^s}\otimes1-1\otimes x^{p^s}", "convention",
    r"x^{p^s}\otimes1-1\otimes x^{p^s}", r"x^{p^s}\otimes1\setmin1\otimes x^{p^s}", conv=7,
    note="Subtraction (GLOBAL_ISSUES 23).")
add(155, "proof of (21.1.5)(iii): '... =x^{p^s}(1⊗1—1⊗1)=0, puisque'", "member x^{p^s}(1⊗1—1⊗1) before '=0'",
    r"...=0$, (missing member)", "formula",
    r"=0$,¶puisque", r"=x^{p^s}(1\otimes1\setmin1\otimes1)=0$,¶puisque",
    note="The restored member's long dash is written \\setmin like the convention-7 fixes.")
add(155, "proof of (21.1.5)(iii): 'les éléments 1⊗x—x⊗1 engendrent'", "long dash", r"$1\otimes x-x\otimes1$", "convention",
    r"$1\otimes x-x\otimes1$", r"$1\otimes x\setmin x\otimes1$", conv=7,
    note="Subtraction (GLOBAL_ISSUES 23).")
add(155, "after the proof of (21.1.5): 'Il résulte aussitôt de (21.1.5) que l'on a, pour tout couple d'homomorphismes d'anneaux A→B→C,'",
    "que l'on a, pour tout couple ... A→B→C,", r"que, pour tout couple ... $A\to B\to C$, on a", "word",
    r"que, pour tout couple d'homomorphismes¶d'anneaux $A\to B\to C$, on a",
    r"que l'on a, pour tout couple d'homomorphismes¶d'anneaux $A\to B\to C$,",
    note="Word order of the print restored.")
add(155, "before (21.1.5.2): 'D'autre part, (21.1.5) montre aussi que l'on a en particulier pour les modules de différentielles « absolues »'",
    "montre aussi que l'on a en particulier pour les modules de différentielles « absolues » (no comma)",
    r"montre en particulier que, pour les modules de différentielles «absolues»,", "word",
    r"montre en particulier que, pour les modules de¶différentielles «absolues»,",
    r"montre aussi que l'on a en particulier pour les modules de¶différentielles «absolues»")
add(155, "(21.1.5.2)", "Ω¹_A = Ω¹_{A/A^p} (no full stop)", r"\Omega^1_A=\Omega^1_{A/A^p}.", "punctuation",
    r"\Omega^1_A=\Omega^1_{A/A^p}.", r"\Omega^1_A=\Omega^1_{A/A^p}")
add(155, "Corollaire (21.1.6): 'Si l'on a Ω¹_{B/A}=0, u est surjectif'", "Si l'on a", r"Si $\Omega^1_{B/A}=0$,", "missing",
    r"Si $\Omega^1_{B/A}=0$,", r"Si l'on a $\Omega^1_{B/A}=0$,")

# ------- print p. 155, TeX in the p. 156 segment (marker misplaced) -------
P156 = "PRINTED P. 155, TeX in the p. 156 segment (old lies in page_156.tex)."
add(156, "printed p. 155: the proof of (21.1.6), Lemme (21.1.6.1) and its proof up to '(T^{-1}S)⊗_{R_𝔪}(T^{-1}S)→T^{-1}S' are on p. 155; printed p. 156 begins 'est bijectif (0_I, 1.3.4)'",
    "p. 156 begins with 'est bijectif (0_I, 1.3.4), et comme T^{-1}S'",
    r"\oldpage{156} stands right after \begin{proof} of (21.1.6)", "marker",
    r"\oldpage[0\textsubscript{IV-1}]{156}¶D'après", r"D'après",
    note=P156 + " Removes the misplaced marker; apply together with the entry that re-inserts it before 'est bijectif (0$_I$, 1.3.4)'.")
add(156, "printed p. 155, proof of (21.1.6): 'donc il est nilpotent'", "nilpotent (italic)", r"donc il est nilpotent", "italics",
    r"donc il est nilpotent", r"donc il est \emph{nilpotent}", note=P156)
add(156, "printed p. 155, proof of (21.1.6): 'π : B⊗_A B→B est bijectif'", "bijectif (italic)", r"B\to B$ est bijectif.", "italics",
    r"B\to B$ est bijectif.", r"B\to B$ est \emph{bijectif}.", note=P156)
add(156, "printed p. 155, proof of (21.1.6): 'B est entier sur A'", "entier (italic)", r"$B$ est entier sur", "italics",
    r"$B$ est entier sur", r"$B$ est \emph{entier} sur", note=P156)
add(156, "printed p. 155, proof of (21.1.6): 'c'est une A-algèbre finie'", "finie (italic)", r"c'est une $A$-algèbre finie.", "italics",
    r"c'est une $A$-algèbre finie.", r"c'est une $A$-algèbre \emph{finie}.", note=P156)
add(156, "printed p. 155, proof of (21.1.6): '(où on ne suppose pas que'", "où on", r"(où l'on", "word",
    r"(où l'on", r"(où on", note=P156)
add(156, "printed p. 155, proof of (21.1.6): 'ne suppose pas'", "ne suppose pas (italic)", r"ne suppose pas que", "italics",
    r"ne suppose pas que", r"\emph{ne suppose pas} que", note=P156)
add(156, "printed p. 155, proof of (21.1.6.1): 'Il suffit de montrer que pour tout idéal maximal 𝔪 de R'",
    "no comma after 'que'", r"montrer que, pour tout idéal maximal", "punctuation",
    r"montrer que, pour tout idéal maximal", r"montrer que pour tout idéal maximal", note=P156)
add(156, "printed p. 155, proof of (21.1.6.1): 'si l'on pose T=R—𝔪'", "long dash (set difference)", r"$T=R-\mathfrak m$", "convention",
    r"$T=R-\mathfrak m$", r"$T=R\setmin\mathfrak m$", conv=7, note=P156)
add(156, "printed p. 155, proof of (21.1.6.1): '(Bourbaki, Alg. comm., chap. II, § 3, n° 3, th. 1)'",
    "n with a superscript letter o", r"n$^\circ$~3 (degree ring)", "symbol",
    r"n$^\circ$~3", r"n\textsuperscript{o}~3", conf="medium",
    note=P156 + " The edition's usual form is n\\textsuperscript{o}.")
add(156, "printed p. 155, last line: 'l'homomorphisme (T^{-1}S)⊗_{R_𝔪}(T^{-1}S)→T^{-1}S'",
    "(T^{-1}S)⊗_{R_𝔪}(T^{-1}S)", r"(T^{-1}S)\otimes_{R_{\mathfrak m}}(S/\mathfrak mS)", "formula",
    r"(T^{-1}S)\otimes_{R_{\mathfrak m}}(S/\mathfrak mS)", r"(T^{-1}S)\otimes_{R_{\mathfrak m}}(T^{-1}S)",
    note=P156 + " Not a misprint: the localisation of S⊗_R S→S is meant.")
add(156, "page break 155/156: printed p. 156 begins 'est bijectif (0_I, 1.3.4)'",
    "p. 155 ends with '(T^{-1}S)⊗_{R_𝔪}(T^{-1}S)→T^{-1}S'", r"(no marker here)", "marker",
    r"\to T^{-1}S$¶est bijectif", r"\to T^{-1}S$¶\oldpage[0\textsubscript{IV-1}]{156}¶est bijectif",
    note=P156 + " Re-inserts the p. 156 marker; apply together with the entry that removes it after \\begin{proof}.")

# ---------------- checks ----------------
pages = {}
for n in range(151, 157):
    with open(os.path.join(RUN, "page_%03d.tex" % n), encoding="utf-8") as fh:
        pages[n] = fh.read().replace("\r\n", "\n")

bad = 0
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    c = pages[f["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("BAD", i, f["page"], c, repr(fx["old"])[:100])

# overlap check per page
for n in pages:
    spans = []
    for i, f in enumerate(F):
        if f["page"] == n and f["fix"]:
            st = pages[n].find(f["fix"]["old"])
            spans.append((st, st + len(f["fix"]["old"]), i))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("OVERLAP page", n, a[2], b[2])
            bad += 1

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for n in range(151, 157):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("total", len(F), "bad", bad)
