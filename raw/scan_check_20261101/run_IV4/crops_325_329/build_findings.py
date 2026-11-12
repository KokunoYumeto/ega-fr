"""Build findings_325_329.json, check every 'old' against page_NNN.tex and simulate the application order
(apply_fixes.py logic) on an in-memory copy of the current ega4-21c-fr.tex. No .tex file is written.
In the strings below, the pilcrow sign stands for a line break."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
E = RUN.parent
SRC = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21c-fr.tex"
OUT = RUN / "findings_325_329.json"
NL = "\u00b6"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=s(old), new=s(new)))
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 325 (segment runs to 'l'injection canonique.')
add(325, "l. 4, first word: 'r∈A[T] tels que'",
    "bold italic r (wrong fount) in r∈A[T]; the r of '+r' and of 'r∈q∩A[T]' on the same line are light",
    "$r\\in A[T]$ (light r)", "misprint_in_print",
    r"$r\in A[T]$ tels", r"$\boldsymbol{r}\in A[T]$ tels",
    "Wrong-fount letter (GLOBAL_ISSUES 29, rule of items 99/100): first letter of the line, not at a line end; stem and arm "
    "visibly heavier than the two other r of the line (side-by-side crops p325_r1/r2/r3.png; ink 181 against 130 and 127 px). "
    "The TeX has the normal r. Diplomatic: bold r; corrected edition: normal r.",
    conf="medium", corrected=r"$r\in A[T]$ tels")
add(325, "ll. 8-9: 'dans A[T]. En outre, on a nécessairement'",
    "no paragraph break: 'En outre' continues the paragraph flush left; the line before is justified to the margin",
    "blank line before 'En outre' (new indented paragraph)", "other",
    r"dans $A[T]$.¶¶En outre", r"dans $A[T]$.¶En outre",
    "Crop p325_enoutre.png.")
add(325, "l. 13: 'de la forme h.K[T], où'", "h.K[T] (baseline period after h)", "$hK[T]$", "symbol",
    r"$hK[T]$", r"$h.K[T]$", "Independent of the next entry (adjacent, no overlap).")
add(325, "ll. 13-14: 'où h(T)=T^m+a_1T^{m-1}+...+a_m avec m≥1 et les a_i∈K'",
    "formula in the line, baseline dots, no comma; connecting words 'avec m≥1 et les a_i∈K'",
    "displayed formula with \\cdots, a comma and '\\qquad m\\geq1,'; then 'avec les $a_i\\in K$'", "formula",
    r"où¶\[¶  h(T)=T^m+a_1T^{m-1}+\cdots+a_m,¶  \qquad m\geq1,¶\]¶avec les $a_i\in K$",
    r"où $h(T)=T^m+a_1T^{m-1}+\ldots+a_m$ avec $m\geq1$¶et les $a_i\in K$",
    "Set inline as printed; restores 'avec m≥1 et les' and the print's baseline dots (crop p325_dots.png).")
add(325, "l. 16: 'par suite h divise F_0 dans K[T]'", "'dans' italic", "dans (roman)", "italics",
    r"divise $F_0$ dans $K[T]$", r"divise $F_0$ \emph{dans} $K[T]$")
add(325, "l. 19: 'Autrement dit, on a h∈A[T]∩q_1K[T]=q_1 (Bourbaki,'", "formula in the line", "displayed formula", "formula",
    r"on a¶\[¶  h\in A[T]\cap\mathfrak q_1K[T]=\mathfrak q_1¶\]¶(Bourbaki",
    r"on a $h\in A[T]\cap\mathfrak q_1K[T]=\mathfrak q_1$¶(Bourbaki",
    "The T of A[T] is a broken sort in the print (not reported).")
add(325, "ll. 20-21: 'divisible par h dans K[T]'", "'dans' italic (first word of l. 21)", "dans (roman)", "italics",
    r"par $h$ dans $K[T]$", r"par $h$ \emph{dans} $K[T]$")
add(325, "l. 22: 'q_1=h.A[T]. C.Q.F.D.'", "h.A[T] (baseline period after h)", "$\\mathfrak q_1=hA[T]$", "symbol",
    r"=hA[T]$", r"=h.A[T]$")
add(325, "Corollaire (21.14.2), l. 1: 'Sous les hypothèses de (21.14.1) sur'", "(21.14.1) upright",
    "plain text inside the italic corollary (italic)", "convention",
    r"Sous les hypothèses de (21.14.1) sur", r"Sous les hypothèses de \textup{(21.14.1)} sur", conv=6)
add(325, "(21.14.2), l. 3: '(i. e. dim B>dim A'",
    "upright opening parenthesis; 'i. e.' italic like the statement (crop p325_ie_zoom.png)",
    "(\\emph{i.e.}: italic parenthesis, upright 'i.e.' (\\emph inside the italic statement)", "convention",
    r"(\emph{i.e.} $\dim B", r"\textup{(}i.e.\ $\dim B",
    "GLOBAL_ISSUES 101: the parenthesis encloses formulas and references and is upright.", conv=6)
add(325, "(21.14.2), l. 3: '((0, 19.7.1) et (6.1.1)))'", "(6.1.1) without 0 (EGA IV's own (6.1.1))",
    "$(\\mathbf 0, 6.1.1)$", "extra",
    r"et $(\mathbf 0, 6.1.1)))$", r"et $(6.1.1)))$",
    "The TeX adds 'bold 0,'. The print's (6.1.1) is EGA IV (6.1.1) (dim B = dim A + dim(B⊗k) for a flat local homomorphism), "
    "the result used here.")
add(325, "Proposition (21.14.3): labels (i), (ii)", "upright (i), (ii)",
    "enumerate label=(\\roman*) inside the italic proposition (italic labels)", "convention",
    r"\begin{enumerate}[label=(\roman*)]¶  \item Si $S$", r"\begin{enumerate}[label=\textup{(\roman*)}]¶  \item Si $S$",
    "GLOBAL_ISSUES 16; one edit covers both labels.", conv=6)
add(325, "(21.14.3) (i), l. 1: '(donc aussi X)'", "upright parentheses (crop p325_parens.png)",
    "text parentheses inside the italic statement (italic)", "convention",
    r"(donc aussi $X$)", r"\textup{(}donc aussi $X$\textup{)}",
    "GLOBAL_ISSUES 26/101: fixed by the print; the phrase contains the formula X.", conv=6)
add(325, "(21.14.3) (ii), l. 2: 'et telle que pour tout point maximal'", "no comma after 'que'", "'et telle que, pour tout'",
    "punctuation", r"et telle que, pour tout point maximal", r"et telle que pour tout point maximal")
add(325, "proof of (21.14.3), l. 2: 'telle que, pour tout s∈S'", "'tout' italic", "tout (roman)", "italics",
    r"pour tout $s\in S$, $Y_s=Y\cap X_s$", r"pour \emph{tout} $s\in S$, $Y_s=Y\cap X_s$")
add(325, "printed p. 326, l. 7: 'Y∩X_η est bien de codimension ≥2 dans X. Comme le couple'",
    "dans X (no subscript η)", "dans $X_\\eta$ (silent correction)", "misprint_in_print",
    r"dans $X_\eta$. Comme le", r"dans $X$. Comme le",
    "Printed on p. 326; the text lies in the p. 325 segment until the marker move (listed before it). The argument ('et comme "
    "O_{X,z}=O_{X_η,z}') concludes the codimension in X_η required by (ii); the print drops the η, the TeX silently corrects.",
    corrected=r"dans $X_\eta$. Comme le")
add(325, "printed p. 326, l. 15: 'la condition b) de (21.13.15)'", "b) italic, letter and parenthesis",
    "$b)$ (italic b, upright parenthesis)", "italics",
    r"la condition $b)$ de", r"la condition \emph{b)} de",
    "Printed on p. 326 (p. 325 segment until the marker move).")
add(325, "printed p. 326, l. 17: 'Posons U=X—Y'", "long dash", "$U=X-Y$", "convention",
    r"Posons $U=X-Y$ et soit", r"Posons $U=X\setmin Y$ et soit",
    "Printed on p. 326 (p. 325 segment until the marker move).", conv=7)
add(325, "end of printed p. 325: '... si l'on | pose Y={x}‾, il existe'",
    "p. 325 ends with 'sous les hypothèses de (i), si l'on'; p. 326 begins 'pose Y={x}‾, il existe un voisinage ouvert'",
    "\\oldpage[IV-4]{326} stands 26 lines later, before 'Comme les hypothèses' ('pose Y=... l'injection canonique.' is printed on p. 326)",
    "marker",
    r"si l'on pose¶$Y=\overline{\{x\}}$", r"si l'on¶\oldpage[IV-4]{326}¶pose $Y=\overline{\{x\}}$",
    "MARKER 326 MOVES EARLIER. Part 1 of 2: mid-sentence break, no blank lines. Listed last for p. 325: apply after all other "
    "p. 325 entries (the three entries marked 'printed p. 326' lie in the moved text). Part 2 is the first p. 326 entry, which "
    "removes the old marker; until then the file has two \\oldpage[IV-4]{326}.")

# ---------------------------------------------------------------- page 326
add(326, "start of page_326.tex: '\\oldpage[IV-4]{326}' between 'canonique.' and 'Comme les hypothèses'",
    "'l'injection canonique.' ends a paragraph in mid-page 326; 'Comme les hypothèses' begins a new indented paragraph",
    "old marker directly between 'canonique.' and 'Comme', no blank line: the two paragraphs run together", "marker",
    r"\oldpage[IV-4]{326}¶Comme les hypothèses", r"¶Comme les hypothèses",
    "Part 2 of 2 of the marker-326 move: apply after the last p. 325 entry (which inserts the marker before 'pose'). Replaces "
    "the old marker line by an empty line, which gives 'canonique.' + blank line + 'Comme les hypothèses' (the printed paragraph "
    "break).")
add(326, "l. 22: 'on a prof(O_{X_{f(x)},x})=dim(O_{X_{f(x)},x})≥1; il résulte'", "formula in the line", "displayed formula",
    "formula",
    r"on a¶\[¶  \operatorname{prof}(\mathcal O_{X_{f(x)},x})¶  =\dim(\mathcal O_{X_{f(x)},x})\geq1;¶\]¶il résulte",
    r"on a $\operatorname{prof}(\mathcal O_{X_{f(x)},x})=\dim(\mathcal O_{X_{f(x)},x})\geq1$;¶il résulte",
    "The periods of '(19.9.8)' (twice on this page) are faintly printed: not reported.")
add(326, "l. 26: 'l'ouvert U=X—Y'", "long dash", "$U=X-Y$", "convention",
    r"l'ouvert $U=X-Y$ est", r"l'ouvert $U=X\setmin Y$ est", conv=7)
add(326, "l. 34: 'U_ν=X_ν—Y_ν'", "long dash", "$U_\\nu=X_\\nu-Y_\\nu$", "convention",
    r"$U_\nu=X_\nu-Y_\nu$", r"$U_\nu=X_\nu\setmin Y_\nu$", conv=7)
add(326, "l. 35: '(8.1.2, a))'", "a) italic (letter and first closing parenthesis); the last parenthesis upright",
    "(8.1.2, $a$)) (upright parenthesis after a)", "italics",
    r"(8.1.2, $a$))", r"(8.1.2, \emph{a)})", "Crop p326_a_label.png.")
add(326, "l. 36: 'U_0=X_0—Y_0'", "long dash", "$U_0=X_0-Y_0$", "convention",
    r"$U_0=X_0-Y_0$", r"$U_0=X_0\setmin Y_0$", conv=7)
add(326, "l. 38: 'on a (j_0)_*(O_{U_0})=p_ν^*((j_ν)_*(O_{U_ν})) (II, 1.5.2) et l'homomorphisme'",
    "formula and reference in the line", "displayed formula with the reference after \\qquad", "formula",
    r"on a¶\[¶  (j_0)_*(\mathcal O_{U_0})¶  =p_\nu^*((j_\nu)_*(\mathcal O_{U_\nu}))¶  \qquad(\mathbf{II}, 1.5.2)¶\]¶et l'homomorphisme",
    r"on a $(j_0)_*(\mathcal O_{U_0})=p_\nu^*((j_\nu)_*(\mathcal O_{U_\nu}))$¶$(\mathbf{II}, 1.5.2)$ et l'homomorphisme")
add(326, "l. 39: 'où ρ_ν : O_{X_ν} → (j)_*(O_{U_ν}) est l'homomorphisme'", "(j)_* without the subscript ν (crop p326_j.png)",
    "(j_\\nu)_* (silent correction)", "misprint_in_print",
    r"\to(j_\nu)_*(\mathcal O_{U_\nu})$ est", r"\to(j)_*(\mathcal O_{U_\nu})$ est",
    "The print drops the subscript ν of j; the TeX silently corrects. Correct reading (j_ν)_*, as in the formula just before.",
    corrected=r"\to(j_\nu)_*(\mathcal O_{U_\nu})$ est")
add(326, "printed p. 327, l. 7: 'L'_ν|U_ν et L_ν=L|U_ν soient isomorphes'", "'L_ν=L|U_ν'",
    "'$\\mathscr L|U_\\nu$' (L_ν= dropped)", "missing",
    r"et $\mathscr L|U_\nu$ soient", r"et $\mathscr L_\nu=\mathscr L|U_\nu$ soient",
    "Printed on p. 327; the text lies in the p. 326 segment until the marker-327 move (listed before it).")
add(326, "end of printed p. 326: '... pour ν assez | grand (8.5.7). Soit d'autre part'",
    "p. 326 ends with 'il en est de même de ρ_ν pour ν assez'; p. 327 begins 'grand (8.5.7). Soit d'autre part L_0'",
    "\\oldpage[IV-4]{327} stands 12 lines later, before 'On est ainsi ramené au cas où'", "marker",
    r"pour $\nu$ assez grand (8.5.7).", r"pour $\nu$ assez¶\oldpage[IV-4]{327}¶grand (8.5.7).",
    "MARKER 327 MOVES EARLIER. Part 1 of 2: mid-sentence break, no blank lines. Listed last for p. 326: apply after all other "
    "p. 326 entries (the L_ν entry lies in the moved text). Part 2 is the first p. 327 entry.")

# ---------------------------------------------------------------- page 327
add(327, "start of page_327.tex: '\\oldpage[IV-4]{327}' before 'On est ainsi ramené'",
    "'On est ainsi ramené au cas où' is in mid-page 327 (new indented paragraph)", "page marker here", "marker",
    r"\oldpage[IV-4]{327}¶On est ainsi ramené", r"On est ainsi ramené",
    "Part 2 of 2 of the marker-327 move: apply after the last p. 326 entry (which inserts the marker before 'grand (8.5.7)'). "
    "The blank line before it stays (new paragraph in the print).")
add(327, "ll. 9-10: 'donc A est intègre et intégralement clos'", "'intègre' and 'intégralement clos' italic, 'et' roman",
    "\\emph{intègre et intégralement clos} ('et' italic)", "italics",
    r"\emph{intègre et¶intégralement clos}", r"\emph{intègre} et¶\emph{intégralement clos}")
add(327, "l. 12: 'aussi une Z-algèbre de type fini (7.8.3,'", "'de type fini' italic", "de type fini (roman)", "italics",
    r"$\mathbb Z$-algèbre de type fini (7.8.3", r"$\mathbb Z$-algèbre \emph{de type fini} (7.8.3")
add(327, "l. 14: 'B_λ tels que B=B_λ⊗_{A_λ}A à un A-isomorphisme près'", "formula in the line", "displayed formula", "formula",
    r"tels que¶\[¶  B=B_\lambda\otimes_{A_\lambda}A¶\]¶à un", r"tels que $B=B_\lambda\otimes_{A_\lambda}A$¶à un")
add(327, "l. 21: 'et on a codim((Y_λ)_{η_λ}, (X_λ)_{η_λ})=codim(Y_η, X_η)≥2 en vertu de'", "formula in the line",
    "displayed formula", "formula",
    r"et on a¶\[¶  \operatorname{codim}((Y_\lambda)_{\eta_\lambda},¶  (X_\lambda)_{\eta_\lambda})¶  =\operatorname{codim}(Y_\eta,X_\eta)\geq2¶\]¶en vertu",
    r"et on a¶$\operatorname{codim}((Y_\lambda)_{\eta_\lambda},(X_\lambda)_{\eta_\lambda})=\operatorname{codim}(Y_\eta,X_\eta)\geq2$¶en vertu")
add(327, "l. 24: 'parafactoriel pour tout μ≥λ'", "μ≥λ (slanted ≥)", "$\\mu\\gg\\lambda$", "symbol",
    r"pour tout $\mu\gg\lambda$", r"pour tout $\mu\geq\lambda$", "Crop p327_s3_l3.png.")
add(327, "l. 25: 'U_λ=X_λ—Y_λ, j : U→X, j_λ : U_λ→X_λ les injections'", "index λ",
    "index μ ($U_\\mu=X_\\mu-Y_\\mu$, $j_\\mu:U_\\mu\\to X_\\mu$)", "formula",
    r"$U_\mu=X_\mu-Y_\mu$, $j:U\to X$,¶$j_\mu:U_\mu\to X_\mu$ les injections",
    r"$U_\lambda=X_\lambda-Y_\lambda$, $j:U\to X$,¶$j_\lambda:U_\lambda\to X_\lambda$ les injections",
    "The TeX rewrites the print's λ as μ in this argument (GLOBAL_ISSUES 102/104 pattern); this entry and the two after the "
    "convention entries restore it (crops p327_s3_l4-l7.png). The print is consistent (the hypothesis covers μ=λ). Apply before "
    "the convention-7 entry for U_λ=X_λ—Y_λ.")
add(327, "l. 25: 'soient U=X—Y'", "long dash", "$U=X-Y$", "convention",
    r"soient $U=X-Y$,", r"soient $U=X\setmin Y$,", conv=7)
add(327, "l. 25: 'U_λ=X_λ—Y_λ'", "long dash", "$U_\\lambda=X_\\lambda-Y_\\lambda$ (after the previous λ entry)", "convention",
    r"$U_\lambda=X_\lambda-Y_\lambda$", r"$U_\lambda=X_\lambda\setmin Y_\lambda$",
    "'old' is the text after the λ entry above; apply after it.", conv=7)
add(327, "ll. 26-27: 'la projection p_λ : X→X_λ ... on a j_*(O_U)=p_λ^*((j_λ)_*(O_{U_λ})) (II, 1.5.2), et par suite'",
    "index λ; formula and reference in the line", "index μ; displayed formula with the reference after \\qquad", "formula",
    r"$p_\mu:X\to X_\mu$ étant un morphisme affine, on a¶\[¶  j_*(\mathcal O_U)=p_\mu^*((j_\mu)_*(\mathcal O_{U_\mu}))¶  \qquad(\mathbf{II}, 1.5.2),¶\]¶et par suite",
    r"$p_\lambda:X\to X_\lambda$ étant un morphisme affine, on a¶$j_*(\mathcal O_U)=p_\lambda^*((j_\lambda)_*(\mathcal O_{U_\lambda}))$ $(\mathbf{II}, 1.5.2)$,¶et par suite",
    "λ for μ as in the entry for l. 25, and the display set in the line as printed.")
add(327, "l. 28: 'n'est autre que p_λ^*(ρ_λ), où ρ_λ : O_{X_λ} → (j_λ)_*(O_{U_λ})'", "index λ", "index μ", "formula",
    r"n'est autre que $p_\mu^*(\rho_\mu)$, où¶$\rho_\mu:\mathcal O_{X_\mu}\to(j_\mu)_*(\mathcal O_{U_\mu})$ est",
    r"n'est autre que $p_\lambda^*(\rho_\lambda)$, où¶$\rho_\lambda:\mathcal O_{X_\lambda}\to(j_\lambda)_*(\mathcal O_{U_\lambda})$ est",
    "As the entry for l. 25.")
add(327, "l. 30: 'il existe un μ≥λ et un O_{U_μ}-Module'", "μ≥λ (slanted ≥)", "$\\mu\\gg\\lambda$", "symbol",
    r"$\mu\gg\lambda$ et un", r"$\mu\geq\lambda$ et un", "Crop p327_s3_l9.png.")
add(327, "l. 33: 'L'=p_μ^*(L_μ) est alors un O_X-Module'", "p_μ^*(L_μ): no prime on L_μ (crop p327_Lprime.png)",
    "p_\\mu^*(\\mathscr L'_\\mu) (silent correction)", "misprint_in_print",
    r"(\mathscr L'_\mu)$ est alors", r"(\mathscr L_\mu)$ est alors",
    "The print drops the prime; the TeX silently corrects. L' is the inverse image of the O_{X_μ}-Module L'_μ.",
    corrected=r"(\mathscr L'_\mu)$ est alors")

# ---------------------------------------------------------------- page 328
add(328, "l. 2: 'puisque Y_s ne contient aucune composante irréductible de X_s'", "Y_s", "$Y$", "formula",
    r"(17.5.3); puisque $Y$ ne", r"(17.5.3); puisque $Y_s$ ne",
    "The second 'puisque Y ne contient' (l. 5) has a plain Y in the print, as in the TeX.")
add(328, "l. 3: 'on a dim(O_{X,x})>dim(O_{S,s}) (17.5.8)'", "O_{X,x} (crop p328_x1.png)", "\\mathcal O_{X,y}", "formula",
    r"$\dim(\mathcal O_{X,y})>\dim(\mathcal O_{S,s})$", r"$\dim(\mathcal O_{X,x})>\dim(\mathcal O_{S,s})$",
    "The TeX rewrites x as y here and in the next entry; the print is right: (21.14.2) needs dim(B_q)≥2 for B_q=O_{X,x}.")
add(328, "l. 4: 'donc dans tous les cas dim(O_{X,x})≥2'", "O_{X,x} (crop p328_x2.png)", "\\mathcal O_{X,y}", "formula",
    r"donc dans tous les cas¶$\dim(\mathcal O_{X,y})\geq2$", r"donc dans tous les cas¶$\dim(\mathcal O_{X,x})\geq2$")
add(328, "l. 5: 'n'est pas contenu dans m_sO_{X,y} puisque Y'", "no comma after O_{X,y}", "comma before 'puisque'",
    "punctuation", r"$\mathfrak m_s\mathcal O_{X,y}$, puisque", r"$\mathfrak m_s\mathcal O_{X,y}$ puisque")
add(328, "l. 7: 'k(y) est extension finie'", "bold italic k", "$k(y)$", "convention",
    r"$k(y)$ est extension", r"$\boldsymbol{k}(y)$ est extension", conv=1)
add(328, "l. 7: 'finie de k(s) (I, 6.4.2)'", "bold italic k", "$k(s)$", "convention",
    r"finie de $k(s)$", r"finie de $\boldsymbol{k}(s)$", conv=1)
add(328, "l. 9: 'Remarques (21.14.4). — (i) Il se peut'", "(i) follows the heading on the same line",
    "blank line after '\\emph{Remarques}. ---': (i) starts a new paragraph", "other",
    r"\emph{Remarques}. ---¶¶(i) Il se peut", r"\emph{Remarques}. ---¶(i) Il se peut",
    "The heading itself, '(21.14.4) Remarques. —' from the env environment against the print's 'Remarques (21.14.4). —', is the "
    "GLOBAL_ISSUES 40 pattern (hand-made \\emph{Remarques} in env; the env closes on p. 329 after the footnote): left to that pass.")
add(328, "(iii), l. 1: 'on prouve que si f : X→S un morphisme lisse,'", "no 'est' (crop p328_iii_r.png)",
    "'si $f:X\\to S$ est un morphisme lisse' (silent correction)", "misprint_in_print",
    r"$f:X\to S$ est un", r"$f:X\to S$ un",
    "The print omits 'est'; the TeX silently supplies it.", corrected=r"$f:X\to S$ est un")
add(328, "(iii), l. 7: 'de sorte que X=V^2_S'", "bold upright V (crop p328_VS.png)", "$\\mathbb V_S^2$ (blackboard V)", "font",
    r"$X=\mathbb V_S^2$", r"$X=\mathbf V_S^2$",
    "The edition writes this V as \\mathbf V elsewhere (266 times); the two \\mathbb V of ega4-21c are both on this page.")
add(328, "(iii), l. 8: 'on a X_s=V^2_k'", "bold upright V (crop p328_Vk.png)", "$\\mathbb V_k^2$", "font",
    r"$X_s=\mathbb V_k^2$", r"$X_s=\mathbf V_k^2$",
    "The heavier subscript k is small-type weight (not reported).")

# ---------------------------------------------------------------- page 329
add(329, "(iv), l. 4: 'Seshadri [44, p. 188-189]'", "hyphen (crop p329_188.png)", "188--189 (en dash)", "punctuation",
    r"p.~188--189", r"p.~188-189", "As IV-1 p. 251 and IV-2 p. 224.")
add(329, "(iv), l. 5: 'Elle donne en outre (loc. cit.) des résultats'", "parentheses italic, like 'loc. cit.' (crop p329_loccit.png)",
    "(\\emph{loc. cit.}) with upright parentheses", "italics",
    r"(\emph{loc. cit.})", r"\emph{(loc. cit.)}",
    "On p. 325 '(loc. cit., prop. 6)' has upright parentheses in the print, as in the TeX.")
add(329, "after 3°: 'Alors Z est localement principal.'", "new indented paragraph", "text right after \\end{enumerate}: no indent",
    "other", r"\end{enumerate}¶Alors $Z$", r"\end{enumerate}¶¶Alors $Z$", "GLOBAL_ISSUES 80 pattern.")
add(329, "(iv): 'en vertu de (21.12.15) (1).'", "footnote mark before the full stop",
    "full stop, then \\footnote (mark after the full stop)", "punctuation",
    r"(21.12.15).¶\footnote{", r"(21.12.15)\footnote{",
    "Part 1 of 2: apply together with the next entry, which puts the full stop after the footnote.")
add(329, "end of the footnote: 'de notre Traité.' + '\\end{env}'", "full stop of the sentence after the mark (1)",
    "no full stop after the footnote", "punctuation",
    r"notre Traité.}¶\end{env}", r"notre Traité.}.¶\end{env}",
    "Part 2 of 2: apply together with the previous entry.")
add(329, "footnote, l. 5: 'est locale sur S et sur T'", "'et sur' italic (crop p329_etsur.png)", "et sur (roman)", "italics",
    r"sur $S$ et sur $T$, ce qui", r"sur $S$ \emph{et sur} $T$, ce qui")
add(329, "heading '21.15. Diviseurs relatifs.'", "final full stop", "no full stop", "punctuation",
    r"\subsection{Diviseurs relatifs}", r"\subsection{Diviseurs relatifs.}",
    "As the other ega4-21 titles (p. 313 'Couples parafactoriels. Anneaux locaux parafactoriels.').")
add(329, "Définition (21.15.2), l. 1: 'faisceau des diviseurs sur X relativement à S'",
    "italic like the whole definition (no contrast; crop p329_def1.png)",
    "\\emph{...} inside the italic definition (upright)", "convention",
    r"On appelle \emph{faisceau des diviseurs sur $X$ relativement à $S$}, ou",
    r"On appelle faisceau des diviseurs sur $X$ relativement à $S$, ou", conv=6)
add(329, "(21.15.2), l. 2: 'faisceau des diviseurs sur X transversaux à f'", "italic like the definition",
    "\\emph{...} (upright)", "convention",
    r"\emph{faisceau des diviseurs sur $X$ transversaux à $f$}, et on note",
    r"faisceau des diviseurs sur $X$ transversaux à $f$, et on note", conv=6)
add(329, "(21.15.2), l. 3: 'se nomment diviseurs sur X relatifs à S'", "italic like the definition",
    "\\emph{...} (upright)", "convention",
    r"nomment \emph{diviseurs sur $X$ relatifs à $S$}, ou", r"nomment diviseurs sur $X$ relatifs à $S$, ou", conv=6)
add(329, "(21.15.2), l. 4: 'ou diviseurs sur X transversaux à f;'", "italic like the definition",
    "\\emph{...} (upright)", "convention",
    r"\emph{diviseurs sur $X$¶transversaux à $f$}; ils", r"diviseurs sur $X$¶transversaux à $f$; ils", conv=6)


# ---------------------------------------------------------------- checks
def page_text(p):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    return t


ok = True
for x in F:
    if x["fix"] is None:
        continue
    n = page_text(x["page"]).count(x["fix"]["old"])
    if n != 1:
        ok = False
        print("PAGE-FILE COUNT", n, x["page"], repr(x["fix"]["old"])[:90])

src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, st) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return st, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
for x in F:
    if x["fix"] is None:
        continue
    st, en = locate(t, x["page"])
    seg = t[st:en]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print("SIM COUNT", c, x["page"], repr(x["fix"]["old"])[:90])
        continue
    t = t[:st] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[en:]

st, _ = locate(t, 325)
_, en = locate(t, 329)
(HERE / "simulated_325_329.tex").write_text(t[st:en], encoding="utf-8")
print("markers after simulation:", [m.group(0) for m in marker.finditer(t) if 324 <= int(m.group(1)) <= 330])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(325, 330):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("entries", len(F), "ALL OK" if ok else "PROBLEMS")
