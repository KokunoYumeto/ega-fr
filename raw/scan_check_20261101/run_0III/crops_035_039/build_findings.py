"""Build findings_035_039.json for EGA 0_III pp. 35-39 and check every fix's 'old' (exactly once in its page_NNN.tex, LF)."""
import json
import pathlib
import collections

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_035_039.json"

CAT = ("Category letters of chapter 0 §11 (C, C', C'', K) are printed bold italic (checked on crops); \\mathcal gives the "
       "script shape. Same issue as GLOBAL_ISSUES item 18 (bold italic K of ega0-1); \\boldsymbol as in those page fixes.")
BOLDR = ("The print sets the R of the hypercohomology of complexes (R·T(K·), R·T(K·,K'·), R^nT(K·)) in bold upright and the R "
         "of the derived functors of objects (R^qT(K^i), R^nT(L^{ij}), R·T(A)) in plain roman; ega3-1-fr.tex has \\mathrm R "
         "for both.")
WAVY = "The print has the wavy arrow ⇝ (checked on a crop); ega3-1-fr.tex writes this arrow \\leadsto elsewhere (9 times)."

findings = []


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    findings.append(d)


# ---------------------------------------------------------------- page 34 (outside 35-39: first half of the p. 35 move)
F(34, "end of page_034.tex, in (11.4.6): 'notée R·T(K·, K'·); elle est l'aboutissement de deux suites spectrales dont les termes E_2 sont donnés par'",
  "this text opens printed p. 35 ('notée R·T(K·, K'·); elle est l'aboutissement ... sont donnés par', then (11.4.6.1))",
  "the text stands before \\oldpage[0\\textsubscript{III}]{35}, at the end of page 34's segment",
  "marker", None, "high",
  r""" notée
$\mathrm R^\bullet T(K^\bullet,K'^\bullet)$~; elle est l'aboutissement de
deux suites spectrales dont les termes $E_2$ sont donnés par
""",
  "\n",
  "OUTSIDE pages 35-39: 'old' lies in page_034.tex. First half of a two-part move (the text moves, not the marker, so each "
  "edit stays in its own page segment); the page-35 marker finding re-inserts the text after the marker. Apply both or neither.")

# ---------------------------------------------------------------- page 35
F(35, "start of page_035.tex: 'notée R·T(K·, K'·); elle est l'aboutissement de deux suites spectrales dont les termes E_2 sont donnés par'",
  "p. 35 begins with 'notée **R**·T(K·, K'·); elle est l'aboutissement de deux suites spectrales dont les termes E_2 sont donnés par' (bold R)",
  "the marker stands after 'sont donnés par' (text in page 34's segment); page_035.tex begins with the display (11.4.6.1)",
  "marker", None, "high",
  r"""\oldpage[0\textsubscript{III}]{35}
\[""",
  r"""\oldpage[0\textsubscript{III}]{35}
notée $\mathbf R^\bullet T(K^\bullet,K'^\bullet)$~; elle est l'aboutissement de
deux suites spectrales dont les termes $E_2$ sont donnés par
\[""",
  "Second half of the move begun by the page-34 finding. Apply both or neither. The re-inserted text also sets the printed "
  "bold R of this R·T (\\mathbf R), so there is no separate bold-R finding for it. " + BOLDR)

F(35, "(11.4.6): 'ou lorsque K· et K'· sont limités inférieurement'",
  "'et' between the two complexes in italics (crop)", "'et' upright",
  "italics", None, "high",
  r"""$K^\bullet$ et $K'^\bullet$ sont limités""",
  r"""$K^\bullet$ \emph{et} $K'^\bullet$ sont limités""",
  "The print sets 'K· et K'·' like one formula, with an italic 'et'.")

F(35, "(11.4.6): 'tout objet de C et tout objet de C' admettent'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""objet de
$\mathcal C$ et tout objet de $\mathcal C'$ admettent""",
  r"""objet de
$\boldsymbol{C}$ et tout objet de $\boldsymbol{C}'$ admettent""",
  CAT + " 2 occurrences.")

F(35, "(11.4.6): 'les limites inductives existent dans C et C''", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""existent dans $\mathcal C$ et $\mathcal C'$.""",
  r"""existent dans $\boldsymbol{C}$ et $\boldsymbol{C}'$.""",
  CAT + " 2 occurrences.")

F(35, "(11.4.6): 'deux autres complexes de C et C' respectivement'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""complexes de $\mathcal C$ et
$\mathcal C'$ respectivement""",
  r"""complexes de $\boldsymbol{C}$ et
$\boldsymbol{C}'$ respectivement""",
  CAT + " 2 occurrences.")

F(35, "(11.4.6): 'f, g deux morphismes homotopes de K· dans K₁·'", "'homotopes' in italics (crop)", "upright",
  "italics", None, "high",
  r"""$g$ deux morphismes homotopes""",
  r"""$g$ deux morphismes \emph{homotopes}""", "")

F(35, "(11.4.6): 'f', g' deux morphismes homotopes de K'· dans K₁'·'", "'homotopes' in italics (crop)", "upright",
  "italics", None, "high",
  r"""$g'$ deux morphismes homotopes""",
  r"""$g'$ deux morphismes \emph{homotopes}""", "")

F(35, "(11.4.6): 'les morphismes R·T(K·, K'·) → R·T(K₁·, K₁'·)', first R", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""morphismes
$\mathrm R^\bullet""",
  r"""morphismes
$\mathbf R^\bullet""",
  BOLDR)

F(35, "(11.4.6): 'les morphismes R·T(K·, K'·) → R·T(K₁·, K₁'·)', second R", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""\mathrm R^\bullet T(K_1^\bullet""",
  r"""\mathbf R^\bullet T(K_1^\bullet""",
  BOLDR)

F(35, "(11.4.6): 'les morphismes R·T(K·, K'·) → R·T(K₁·, K₁'·)', second argument of the source",
  "the bullet of K' is printed low, as a subscript: K'_• (enlarged crop)", "K'^\\bullet (silently corrected)",
  "misprint_in_print", None, "high",
  r"""K'^\bullet)\to""",
  r"""K'_\bullet)\to""",
  "The TeX silently corrects; the fix restores the printed reading. Correct reading: superscript bullet, as everywhere else.",
  corrected=r"""K'^\bullet)\to""")

F(35, "Proposition (11.4.7): 'pour tout objet injectif I de C'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""injectif $I$ de $\mathcal C$""",
  r"""injectif $I$ de $\boldsymbol{C}$""",
  CAT)

F(35, "(11.4.7): '(resp. I' de C')'", "'(resp.' upright inside the italic statement", "italic (proposition environment)",
  "convention", 6, "high",
  r"""(resp. $I'$ de""",
  r"""\textup{(resp.} $I'$ de""", "")

F(35, "(11.4.7): '(resp. I' de C')', the C'", "C' bold italic", "\\mathcal C'",
  "font", None, "high",
  r"""$\mathcal C'$), $A'""",
  r"""$\boldsymbol{C}'$), $A'""",
  CAT)

F(35, "(11.4.7): 'A'⇝T(I, A')'", "wavy arrow ⇝", "\\mapsto",
  "symbol", None, "high",
  r"""\mapsto T(I,A')""",
  r"""\leadsto T(I,A')""",
  WAVY)

F(35, "(11.4.7): '(resp. A⇝T(A, I'))'", "'(resp.' upright inside the italic statement", "italic (proposition environment)",
  "convention", 6, "high",
  r"""(resp. $A""",
  r"""\textup{(resp.} $A""", "")

F(35, "(11.4.7): '(resp. A⇝T(A, I'))', the arrow", "wavy arrow ⇝", "\\mapsto",
  "symbol", None, "high",
  r"""\mapsto T(A,I')""",
  r"""\leadsto T(A,I')""",
  WAVY)

F(35, "(11.4.7): 'avec les notations de (11.4.6)'", "reference (11.4.6) upright", "italic (proposition environment)",
  "convention", 6, "high",
  r"""(\hyperref[0.11.4.6-fr]{11.4.6})""",
  r"""\textup{(\hyperref[0.11.4.6-fr]{11.4.6})}""", "")

F(35, "(11.4.7.1): 'R·T(K·, K'·) ⥲ ...'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""\label{0.11.4.7.1-fr}
  \mathrm R^\bullet""",
  r"""\label{0.11.4.7.1-fr}
  \mathbf R^\bullet""",
  BOLDR)

F(35, "proof of (11.4.7): 'Le quadricomplexe T(L··, L'··)) peut être considéré'",
  "extra closing parenthesis: T(L··, L'··)) (enlarged crop)", "T(L^{\\bullet\\bullet},L'^{\\bullet\\bullet}) (silently corrected)",
  "misprint_in_print", None, "high",
  r"""$T(L^{\bullet\bullet},L'^{\bullet\bullet})$ peut""",
  r"""$T(L^{\bullet\bullet},L'^{\bullet\bullet}))$ peut""",
  "The TeX silently corrects; the fix restores the printed reading.",
  corrected=r"""$T(L^{\bullet\bullet},L'^{\bullet\bullet})$""")

F(35, "Lemme (11.5.1): 'un complexe de C, et pour tout entier r'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""un complexe de $\mathcal C$, et pour""",
  r"""un complexe de $\boldsymbol{C}$, et pour""",
  CAT)

# ---------------------------------------------------------------- page 36
F(36, "Lemme (11.5.1), cont.: 'de C dans C', permutant'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""de $\mathcal C$ dans $\mathcal C'$, permutant""",
  r"""de $\boldsymbol{C}$ dans $\boldsymbol{C}'$, permutant""",
  CAT + " 2 occurrences.")

F(36, "(11.5.1): 'exactes dans C et C')'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""exactes dans $\mathcal C$ et $\mathcal C'$). Alors""",
  r"""exactes dans $\boldsymbol{C}$ et $\boldsymbol{C}'$). Alors""",
  CAT + " 2 occurrences.")

F(36, "(11.5.1): 'Alors R·T(K·) est isomorphe'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""$\mathrm R^\bullet T(K^\bullet)$ est isomorphe""",
  r"""$\mathbf R^\bullet T(K^\bullet)$ est isomorphe""",
  BOLDR)

F(36, "(11.5.1): 'à la limite inductive lim R·T(K·_(r)) lorsque r tend vers −∞'",
  "in the running text; lim with only the arrow under it (no index); bold R (crop)",
  "displayed; \\varinjlim_{r\\to-\\infty} with an index the print does not have; \\mathrm R",
  "formula", None, "high",
  r"""inductive
\[
  \varinjlim_{r\to-\infty}\mathrm R^\bullet T(K_{(r)}^\bullet)
\]
lorsque""",
  r"""inductive
$\varinjlim\mathbf R^\bullet T(K_{(r)}^\bullet)$
lorsque""",
  "Removes the added index and sets the formula inline as printed; also sets this bold R (no separate finding). Cf. GLOBAL_ISSUES items 21 and 30.")

F(36, "after (11.5.1): 'en choisissant arbitrairement, pour chaque i'", "'arbitrairement' in italics (crop)", "upright",
  "italics", None, "high",
  r"""choisissant arbitrairement,""",
  r"""choisissant \emph{arbitrairement},""", "")

F(36, "'ne dépendent que des résolutions (X_B^{i,·}), (X_H^{i,·}) et (X_B^{i+1,·})'",
  "'et' in italics, like the emphasised phrase (crop)", "'et' upright",
  "italics", None, "high",
  r"""$(X_{\mathrm H}^{i,\bullet})$ et
""",
  r"""$(X_{\mathrm H}^{i,\bullet})$ \emph{et}
""", "")

F(36, "'un système inductif (L··_(r)) de bicomplexes de C'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""bicomplexes de $\mathcal C$, dont""",
  r"""bicomplexes de $\boldsymbol{C}$, dont""",
  CAT)

F(36, "'on a bien H·(T(L··)) = lim H·(T(L··_(r))) à un isomorphisme près'", "in the running text", "displayed with \\[ ... \\]",
  "other", None, "high",
  r"""on a bien
\[
  \mathrm H^\bullet(T(L^{\bullet\bullet}))=
  \varinjlim\mathrm H^\bullet(T(L_{(r)}^{\bullet\bullet}))
\]
à un""",
  r"""on a bien
$\mathrm H^\bullet(T(L^{\bullet\bullet}))=\varinjlim\mathrm H^\bullet(T(L_{(r)}^{\bullet\bullet}))$
à un""",
  "Layout only (display vs inline); the formula itself matches.")

F(36, "Proposition (11.5.2): 'Sous les hypothèses de (11.5.1)'", "reference (11.5.1) upright", "italic (proposition environment)",
  "convention", 6, "high",
  r"""Sous les hypothèses de (\hyperref[0.11.5.1-fr]{11.5.1}) concernant""",
  r"""Sous les hypothèses de \textup{(\hyperref[0.11.5.1-fr]{11.5.1})} concernant""", "")

F(36, "(11.5.2): 'concernant C, C' et T'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""$\mathcal C$, $\mathcal C'$ et $T$,""",
  r"""$\boldsymbol{C}$, $\boldsymbol{C}'$ et $T$,""",
  CAT + " 2 occurrences.")

F(36, "(11.5.2): 'R·T(K·) est un foncteur cohomologique'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""$\mathrm R^\bullet T(K^\bullet)$ est un
foncteur""",
  r"""$\mathbf R^\bullet T(K^\bullet)$ est un
foncteur""",
  BOLDR)

F(36, "(11.5.2): 'des complexes de C.'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""complexes de
$\mathcal C$.
\end{proposition}""",
  r"""complexes de
$\boldsymbol{C}$.
\end{proposition}""",
  CAT)

F(36, "proof of (11.5.2): 'se ramener au cas des complexes limités inférieurement :'",
  "'limités inférieurement' in italics (crop)", "upright",
  "italics", None, "high",
  r"""complexes limités inférieurement~:""",
  r"""complexes \emph{limités inférieurement}~:""", "")

F(36, "proof of (11.5.2): 'si on a une suite exacte 0→K'·→K·→K''·→0 de complexes'", "in the running text", "displayed with \\[ ... \\]",
  "other", None, "high",
  r"""suite exacte
\[
  0\longrightarrow K'^\bullet\longrightarrow K^\bullet
  \longrightarrow K''^\bullet\longrightarrow0
\]
de complexes""",
  r"""suite exacte
$0\longrightarrow K'^\bullet\longrightarrow K^\bullet\longrightarrow K''^\bullet\longrightarrow0$
de complexes""",
  "Layout only (display vs inline); the formula itself matches.")

F(36, "proof of (11.5.2): 'pour chaque r une suite exacte 0→K'·_(r)→K·_(r)→K''·_(r)→0, d'où'", "in the running text", "displayed with \\[ ... \\]",
  "other", None, "high",
  r"""suite exacte
\[
  0\longrightarrow K_{(r)}'^\bullet\longrightarrow K_{(r)}^\bullet
  \longrightarrow K_{(r)}''^\bullet\longrightarrow0,
\]
d'où""",
  r"""suite exacte
$0\longrightarrow K_{(r)}'^\bullet\longrightarrow K_{(r)}^\bullet\longrightarrow K_{(r)}''^\bullet\longrightarrow0$,
d'où""",
  "Layout only (display vs inline); the formula itself matches.")

F(36, "proof of (11.5.2), first exact sequence '...→R^nT(K'·_(r))→R^nT(K·_(r))→R^nT(K''·_(r))→R^{n+1}T(K'·_(r))→...'",
  "the four R bold", "\\mathrm R (4 times)",
  "font", None, "high",
  r"""\mathrm R^nT(K_{(r)}'^\bullet)
  \longrightarrow\mathrm R^nT(K_{(r)}^\bullet)
  \longrightarrow\mathrm R^nT(K_{(r)}''^\bullet)
  \xrightarrow{\partial}\mathrm R^{n+1}T(K_{(r)}'^\bullet)""",
  r"""\mathbf R^nT(K_{(r)}'^\bullet)
  \longrightarrow\mathbf R^nT(K_{(r)}^\bullet)
  \longrightarrow\mathbf R^nT(K_{(r)}''^\bullet)
  \xrightarrow{\partial}\mathbf R^{n+1}T(K_{(r)}'^\bullet)""",
  BOLDR + " 4 occurrences.")

F(36, "first exact sequence, leading dots", "baseline dots . . . (crop)", "\\cdots (centred)",
  "symbol", None, "medium",
  r"""hypothèse, une suite exacte
\[
  \cdots""",
  r"""hypothèse, une suite exacte
\[
  \ldots""",
  "Typographic only (GLOBAL_ISSUES item 22 for EGA II).")

F(36, "first exact sequence, trailing dots", "baseline dots . . . (crop)", "\\cdots (centred)",
  "symbol", None, "medium",
  r"""\longrightarrow\cdots
\]
ces suites""",
  r"""\longrightarrow\ldots
\]
ces suites""",
  "Typographic only.")

F(36, "proof of (11.5.2), second exact sequence '...→R^nT(K'·)→R^nT(K·)→R^nT(K''·)→R^{n+1}T(K'·)→...'",
  "the four R bold", "\\mathrm R (4 times)",
  "font", None, "high",
  r"""\mathrm R^nT(K'^\bullet)
  \longrightarrow\mathrm R^nT(K^\bullet)
  \longrightarrow\mathrm R^nT(K''^\bullet)
  \xrightarrow{\partial}\mathrm R^{n+1}T(K'^\bullet)""",
  r"""\mathbf R^nT(K'^\bullet)
  \longrightarrow\mathbf R^nT(K^\bullet)
  \longrightarrow\mathbf R^nT(K''^\bullet)
  \xrightarrow{\partial}\mathbf R^{n+1}T(K'^\bullet)""",
  BOLDR + " 4 occurrences.")

F(36, "second exact sequence, leading dots", "baseline dots . . .", "\\cdots (centred)",
  "symbol", None, "medium",
  r"""démontrent que l'on a une suite exacte
\[
  \cdots""",
  r"""démontrent que l'on a une suite exacte
\[
  \ldots""",
  "Typographic only.")

F(36, "second exact sequence, trailing dots", "baseline dots . . .", "\\cdots (centred)",
  "symbol", None, "medium",
  r"""\longrightarrow\cdots
\]
\end{proof}""",
  r"""\longrightarrow\ldots
\]
\end{proof}""",
  "Typographic only.")

F(36, "'ils forment évidemment une catégorie abélienne K.'",
  "'catégorie abélienne' in italics; K bold italic (crop)", "upright; \\mathcal K",
  "italics", None, "high",
  r"""une catégorie
abélienne $\mathcal K$.""",
  r"""une \emph{catégorie
abélienne} $\boldsymbol{K}$.""",
  "Also makes the bold italic K change for this occurrence (no separate K finding). " + CAT)

F(36, "Lemme (11.5.2.1): 'Dans K, soit 𝔍'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""Dans $\mathcal K$, soit""",
  r"""Dans $\boldsymbol{K}$, soit""",
  CAT)

# ---------------------------------------------------------------- page 37
F(37, "Lemme (11.5.2.1): conditions 1°, 2°",
  "run in the statement: 'propriétés suivantes : 1° Tout Q^i est un objet injectif de C; 2° Pour tout i⩾0, on a Z^i(Q·)=B^i(Q·), et Z^i(Q·) est facteur direct de Q^i. Alors :'",
  "enumerate list with \\item[$1^\\circ$], \\item[$2^\\circ$]",
  "other", None, "high",
  r"""propriétés suivantes~:
\begin{enumerate}
  \item[$1^\circ$] Tout $Q^i$ est un objet injectif de $\mathcal C$~;
  \item[$2^\circ$] Pour tout $i\geq0$, on a
    $\mathrm Z^i(Q^\bullet)=\mathrm B^i(Q^\bullet)$, et
    $\mathrm Z^i(Q^\bullet)$ est facteur direct de $Q^i$.
\end{enumerate}
Alors~:""",
  r"""propriétés suivantes~: $1^\circ$ Tout $Q^i$ est un objet injectif de $\boldsymbol{C}$~;
$2^\circ$ Pour tout $i\geq0$, on a
$\mathrm Z^i(Q^\bullet)=\mathrm B^i(Q^\bullet)$, et
$\mathrm Z^i(Q^\bullet)$ est facteur direct de $Q^i$. Alors~:""",
  "Layout: run-in conditions (as in run_II p. 28). Also sets the bold italic C of condition 1° (no separate C finding). "
  "The items (i), (ii) after 'Alors :' are printed on separate lines and stay a list.")

F(37, "(11.5.2.1): label (i)", "'(i)' upright", "\\item[(i)] italic in the lemma environment",
  "convention", 6, "high",
  r"""\item[(i)] Tout""",
  r"""\item[\textup{(i)}] Tout""",
  "GLOBAL_ISSUES item 16.")

F(37, "(11.5.2.1): label (ii)", "'(ii)' upright", "\\item[(ii)] italic in the lemma environment",
  "convention", 6, "high",
  r"""\item[(ii)] Tout""",
  r"""\item[\textup{(ii)}] Tout""",
  "GLOBAL_ISSUES item 16.")

F(37, "(11.5.2.1)(i): 'est un objet injectif de K'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""objet injectif de
    $\mathcal K$.""",
  r"""objet injectif de
    $\boldsymbol{K}$.""",
  CAT)

F(37, "(11.5.2.1)(ii): 'Tout objet de K est isomorphe'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""objet de $\mathcal K$ est isomorphe""",
  r"""objet de $\boldsymbol{K}$ est isomorphe""",
  CAT)

F(37, "proof of (11.5.2.1)(i): 'Soient A· = (A^i) un objet de K'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""un objet de $\mathcal K$,
$A'^\bullet""",
  r"""un objet de $\boldsymbol{K}$,
$A'^\bullet""",
  CAT)

F(37, "proof of (11.5.2.1)(i): 'Identifions Q à B^i(Q·)⊕B^{i+1}(Q·)'",
  "'Q' without the superscript i (enlarged crop)", "$Q^i$ (silently corrected)",
  "misprint_in_print", None, "high",
  r"""Identifions $Q^i$ à""",
  r"""Identifions $Q$ à""",
  "The TeX silently corrects; the fix restores the printed reading. It is the component Q^i that is identified with B^i(Q·)⊕B^{i+1}(Q·).",
  corrected=r"""Identifions $Q^i$ à""")

F(37, "proof of (11.5.2.1)(i): conditions 1°, 2° of the induction",
  "run in the paragraph: 'et tels en outre que : 1° g^{i−1}(Z^{i−1}(A·))⊂Z^{i−1}(Q·); 2° Si on pose ... sur C^{i−1}. Le morphisme f^i ...'",
  "enumerate list with \\item[$1^\\circ$], \\item[$2^\\circ$]",
  "other", None, "high",
  r"""et tels en outre que~:
\begin{enumerate}
  \item[$1^\circ$] $g^{i-1}(\mathrm Z^{i-1}(A^\bullet))\subset
    \mathrm Z^{i-1}(Q^\bullet)$~;
  \item[$2^\circ$] Si on pose $C^j=(d^j)^{-1}(A'^{j+1})$ pour tout $j$, alors
    $d'^{i-1}\circ g^{i-1}$ coïncide avec $f^i\circ d^{i-1}$ sur $C^{i-1}$.
\end{enumerate}
Le morphisme""",
  r"""et tels en outre que~: $1^\circ$ $g^{i-1}(\mathrm Z^{i-1}(A^\bullet))\subset
\mathrm Z^{i-1}(Q^\bullet)$~; $2^\circ$ Si on pose $C^j=(d^j)^{-1}(A'^{j+1})$ pour tout $j$, alors
$d'^{i-1}\circ g^{i-1}$ coïncide avec $f^i\circ d^{i-1}$ sur $C^{i-1}$.
Le morphisme""",
  "Layout: run-in conditions, continuing in the same paragraph.")

F(37, "proof of (11.5.2.1)(i): 'h^i coïncide avec f'_i dans B^i(A·)∩A'^i'",
  "f'_i: prime above, i as a subscript (enlarged crop)", "f'^i (silently corrected)",
  "misprint_in_print", None, "high",
  r"""$h^i$ coïncide avec $f'^i$ dans""",
  r"""$h^i$ coïncide avec $f'_i$ dans""",
  "The TeX silently corrects; the fix restores the printed reading. f'^i is the first component of f^i, as in the rest of the proof.",
  corrected=r"""$h^i$ coïncide avec $f'^i$ dans""")

F(37, "proof of (11.5.2.1)(i): 'Considérons d'autre part le morphisme f''^{i+1}∘d^i : C^i → B^{i+1}(Q·)'",
  "f''^{i+1}∘d^i (double prime; crop)", "f''^{i+1}\\circ d^i (keeps the print)",
  "misprint_in_print", None, "medium",
  None, None,
  "The TeX keeps the printed reading. f''^{i+1} maps A'^{i+1} to B^{i+2}(Q·), so f''^{i+1}∘d^i cannot have the stated target "
  "B^{i+1}(Q·). With Q^{i+1}=B^{i+1}(Q·)⊕B^{i+2}(Q·), the induction needs d'^i∘g^i=(g''^i,0) to agree on C^i with "
  "f^{i+1}∘d^i=(f'^{i+1}∘d^i, f''^{i+1}∘d^i); there f''^{i+1}∘d^i=0 because f is a morphism of complexes, so g''^i must "
  "extend f'^{i+1}∘d^i (which equals f''^i on A'^i). Same reading at the second occurrence (next finding).",
  corrected=r"""$f'^{i+1}\circ d^i:C^i\to\mathrm B^{i+1}(Q^\bullet)$""")

F(37, "proof of (11.5.2.1)(i): 'qui coïncide avec f''^{i+1}∘d^i dans C^i et avec 0 dans Z^i(A·)'",
  "f''^{i+1}∘d^i (double prime; crop)", "f''^{i+1}\\circ d^i (keeps the print)",
  "misprint_in_print", None, "medium",
  None, None,
  "The TeX keeps the printed reading; see the previous finding.",
  corrected=r"""avec $f'^{i+1}\circ d^i$ dans $C^i$""")

F(37, "proof of (11.5.2.1)(ii): 'un objet injectif Q'^i de C'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""objet injectif $Q'^i$ de
$\mathcal C$ tel""",
  r"""objet injectif $Q'^i$ de
$\boldsymbol{C}$ tel""",
  CAT)

F(37, "proof of (11.5.2.1)(ii): 'Posons alors Q^i = 0 pour i<0, Q^0 = Q'^1 et Q^i = Q'^i⊕Q'^{i+1} pour i⩾1, avec'",
  "in the running text, with the words 'pour', 'et', 'pour'",
  "displayed: 'Q^i=0 (i<0), Q^0=Q'^1, Q^i=Q'^i⊕Q'^{i+1} (i≥1),' with \\quad and parentheses instead of the words",
  "missing", None, "high",
  r"""Posons alors
\[
  Q^i=0\quad(i<0),\qquad Q^0=Q'^1,\qquad
  Q^i=Q'^i\oplus Q'^{i+1}\quad(i\geq1),
\]
avec""",
  r"""Posons alors
$Q^i=0$ pour $i<0$, $Q^0=Q'^1$ et $Q^i=Q'^i\oplus Q'^{i+1}$ pour $i\geq1$,
avec""",
  "Restores the printed words and the inline setting.")

F(37, "Corollaire (11.5.2.2): 'Tout objet K· de K'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""objet $K^\bullet$ de $\mathcal K$ admet""",
  r"""objet $K^\bullet$ de $\boldsymbol{K}$ admet""",
  CAT)

F(37, "(11.5.2.2): 'formée d'objets de K, il y a un morphisme'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""de $\mathcal K$, il y a un morphisme""",
  r"""de $\boldsymbol{K}$, il y a un morphisme""",
  CAT)

F(37, "proof of (11.5.2.2): '(M, V, 1.1 a))'", "'a)' in italics (crop)", "upright",
  "italics", None, "high",
  r"""1.1 a))""",
  r"""1.1 \emph{a)})""", "")

F(37, "proof of (11.5.2.2): 'appliqué à la catégorie abélienne K.'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""abélienne
$\mathcal K$.
\end{proof}""",
  r"""abélienne
$\boldsymbol{K}$.
\end{proof}""",
  CAT)

F(37, "(11.5.2.3): 'montrons que l'on a un isomorphisme H·(T(L'··)) ⥲ H·(T(L··)). On déduit'", "in the running text",
  "displayed with \\[ ... \\]",
  "other", None, "high",
  r"""un isomorphisme
\[
  \mathrm H^\bullet(T(L'^{\bullet\bullet}))\xrightarrow{\sim}
  \mathrm H^\bullet(T(L^{\bullet\bullet})).
\]
On déduit""",
  r"""un isomorphisme
$\mathrm H^\bullet(T(L'^{\bullet\bullet}))\xrightarrow{\sim}\mathrm H^\bullet(T(L^{\bullet\bullet}))$.
On déduit""",
  "Layout only (display vs inline); the formula itself matches.")

F(37, "(11.5.2.3): 'ces suites spectrales sont régulières'", "'régulières' in italics (crop)", "upright",
  "italics", None, "high",
  r"""sont régulières, il""",
  r"""sont \emph{régulières}, il""", "")

LNOTE = ("In (11.5.2.2) and the first sentence of (11.5.2.3), L'·· is the Cartan-Eilenberg resolution and L·· the resolution "
         "by objects of 𝔍; for L' the equality holds by definition, and the reduction concerns L (the TeX's reading). The "
         "print's L' agrees with the naming of (11.5.2.5) and of the proof of (11.5.3), where L'·· is the 𝔍-resolution: "
         "decide together with the page-38 finding on (11.5.2.5).")

F(37, "(11.5.2.3): 'ou encore que H^q_II(T(L'^{i,·})) est égal à R^qT(K^i)'",
  "L'^{i,·} with a prime (enlarged crop)", "L^{i,\\bullet} without prime (silently corrected)",
  "misprint_in_print", None, "high",
  r"""$\mathrm H_{\mathrm{II}}^q(T(L^{i,\bullet}))$""",
  r"""$\mathrm H_{\mathrm{II}}^q(T(L'^{i,\bullet}))$""",
  "The TeX silently corrects; the fix restores the printed reading. " + LNOTE,
  corrected=r"""$\mathrm H_{\mathrm{II}}^q(T(L^{i,\bullet}))$""")

F(37, "(11.5.2.3): 'comme L'^{i,·} est une résolution droite de K^i'",
  "L'^{i,·} with a prime (enlarged crop)", "L^{i,\\bullet} without prime (silently corrected)",
  "misprint_in_print", None, "high",
  r"""comme $L^{i,\bullet}$ est une résolution droite""",
  r"""comme $L'^{i,\bullet}$ est une résolution droite""",
  "The TeX silently corrects; the fix restores the printed reading. See the previous finding.",
  corrected=r"""comme $L^{i,\bullet}$ est une résolution droite""")

# ---------------------------------------------------------------- page 38
F(38, "Lemme (11.5.2.4): 'd'un objet A de C telle que'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""d'un objet $A$
de $\mathcal C$ telle""",
  r"""d'un objet $A$
de $\boldsymbol{C}$ telle""",
  CAT)

F(38, "(11.5.2.5): 'résolution injective de K· dans la catégorie abélienne K, autrement dit'",
  "'dans la catégorie abélienne' in italics; K bold italic (crop)", "upright; \\mathcal K",
  "italics", None, "high",
  r"""dans la catégorie abélienne $\mathcal K$, autrement dit,""",
  r"""\emph{dans la catégorie abélienne $\boldsymbol{K}$}, autrement dit,""",
  "Also makes the bold italic K change for this occurrence (no separate K finding).")

F(38, "(11.5.2.5): 'K·⇝H·(T(L'··))'", "wavy arrow ⇝", "\\mapsto",
  "symbol", None, "high",
  r"""K^\bullet\mapsto\mathrm H^\bullet""",
  r"""K^\bullet\leadsto\mathrm H^\bullet""",
  WAVY)

F(38, "(11.5.2.5): 'le foncteur cohomologique dérivé droit de T'", "'dérivé droit' in italics (crop)", "upright",
  "italics", None, "high",
  r"""cohomologique dérivé droit de $T$""",
  r"""cohomologique \emph{dérivé droit} de $T$""", "")

F(38, "(11.5.2.5): 'dans la catégorie K (T, 2.3)'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""dans la catégorie $\mathcal K$
(T, 2.3)""",
  r"""dans la catégorie $\boldsymbol{K}$
(T, 2.3)""",
  CAT)

F(38, "(11.5.2.5): 'car L'·· est une résolution injective de K· dans la catégorie abélienne K, autrement dit, K·⇝H·(T(L'··))'",
  "L'·· (twice)", "L'^{\\bullet\\bullet} (keeps the print)",
  "misprint_in_print", None, "medium",
  None, None,
  "The TeX keeps the printed reading. With the naming of (11.5.2.2) and of the first sentence of (11.5.2.3) (L'·· the "
  "Cartan-Eilenberg resolution, L·· made of objects of 𝔍), only L·· is an injective resolution in K: by (11.5.2.1) the "
  "objects of 𝔍 are injective in K, while the columns of a Cartan-Eilenberg resolution are not exact in general. The print "
  "uses L' for the 𝔍-resolution here, at the end of (11.5.2.3) (p. 37, silently corrected to L in the TeX) and in the proof "
  "of (11.5.3). The corrected edition should treat the end of (11.5.2.3) and (11.5.2.5) alike.",
  corrected=r"""car $L^{\bullet\bullet}$ est une résolution injective de $K^\bullet$ ... $K^\bullet\leadsto\mathrm H^\bullet(T(L^{\bullet\bullet}))$""")

F(38, "Proposition (11.5.3): 'Sous les hypothèses de (11.5.1)'", "reference (11.5.1) upright", "italic (proposition environment)",
  "convention", 6, "high",
  r"""hypothèses de (\hyperref[0.11.5.1-fr]{11.5.1}) concernant""",
  r"""hypothèses de \textup{(\hyperref[0.11.5.1-fr]{11.5.1})} concernant""", "")

F(38, "(11.5.3): 'concernant C, C' et T'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""$\mathcal C$, $\mathcal C'$ et $T$, soit""",
  r"""$\boldsymbol{C}$, $\boldsymbol{C}'$ et $T$, soit""",
  CAT + " 2 occurrences.")

F(38, "(11.5.3.1): 'R·T(K·) ⥲ H·(T(L··)))'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""\label{0.11.5.3.1-fr}
  \mathrm R^\bullet""",
  r"""\label{0.11.5.3.1-fr}
  \mathbf R^\bullet""",
  BOLDR)

F(38, "(11.5.3.1): 'H·(T(L··))).'", "three closing parentheses (enlarged crop)", "two (silently corrected)",
  "misprint_in_print", None, "high",
  r"""\mathrm H^\bullet(T(L^{\bullet\bullet})).
  \tag{11.5.3.1}""",
  r"""\mathrm H^\bullet(T(L^{\bullet\bullet}))).
  \tag{11.5.3.1}""",
  "The TeX silently corrects; the fix restores the printed reading.",
  corrected=r"""\mathrm H^\bullet(T(L^{\bullet\bullet})).""")

F(38, "Remarque (11.5.4): 'des complexes K· limités inférieurement, sans supposer que'",
  "'limités inférieurement' in italics (crop)", "no \\emph (body judged as roman)",
  "italics", None, "high",
  r"""$K^\bullet$ limités inférieurement, \emph{sans""",
  r"""$K^\bullet$ \emph{limités inférieurement}, \emph{sans""", "")

F(38, "(11.5.4): 'la catégorie K des complexes K·'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""la catégorie $\mathcal K$ des complexes""",
  r"""la catégorie $\boldsymbol{K}$ des complexes""",
  CAT)

F(38, "(11.5.4): 'la caractérisation de R·T(K·)'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""caractérisation de $\mathrm R^\bullet T(K^\bullet)$""",
  r"""caractérisation de $\mathbf R^\bullet T(K^\bullet)$""",
  BOLDR)

F(38, "(11.5.4): 'de T dans K montre'", "K bold italic", "\\mathcal K",
  "font", None, "high",
  r"""dans $\mathcal K$
montre""",
  r"""dans $\boldsymbol{K}$
montre""",
  CAT)

F(38, "(11.5.4), 2nd paragraph: 'tout objet de C admette'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""tout objet de $\mathcal C$ admette""",
  r"""tout objet de $\boldsymbol{C}$ admette""",
  CAT)

F(38, "(11.5.4): 'une résolution injective de longueur ⩽m'", "'de longueur' in italics (crop)", "no \\emph",
  "italics", None, "high",
  r"""injective de longueur
$\leq m$. En effet""",
  r"""injective \emph{de longueur}
$\leq m$. En effet""", "")

F(38, "(11.5.4): 'résolutions injectives d'objets de C qui interviennent'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""de $\mathcal C$ qui interviennent""",
  r"""de $\boldsymbol{C}$ qui interviennent""",
  CAT)

F(38, "(11.5.4): 'sont égaux à ceux de T(L··) et en nombre fini'", "'égaux à ceux de' and 'fini' in italics (crop)", "no \\emph",
  "italics", None, "high",
  r"""sont égaux à ceux de
$T(L^{\bullet\bullet})$ et en nombre fini,""",
  r"""sont \emph{égaux à ceux de}
$T(L^{\bullet\bullet})$ et en nombre \emph{fini},""",
  "2 phrases.")

F(38, "(11.5.4): 'on a donc aussi R^nT(K·_(r)) = R^nT(K·)'", "both R bold", "\\mathrm R",
  "font", None, "high",
  r"""$\mathrm R^nT(K_{(r)}^\bullet)=\mathrm R^nT(K^\bullet)$""",
  r"""$\mathbf R^nT(K_{(r)}^\bullet)=\mathbf R^nT(K^\bullet)$""",
  BOLDR + " 2 occurrences.")

F(38, "(11.5.4): 'lorsque C vérifie l'hypothèse précédente'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""lorsque $\mathcal C$ vérifie""",
  r"""lorsque $\boldsymbol{C}$ vérifie""",
  CAT)

F(38, "(11.5.5): 'où l'on suppose que dans C, C' et C''", "C, C', C'' bold italic", "\\mathcal C, \\mathcal C', \\mathcal C''",
  "font", None, "high",
  r"""dans $\mathcal C$,
$\mathcal C'$ et $\mathcal C''$""",
  r"""dans $\boldsymbol{C}$,
$\boldsymbol{C}'$ et $\boldsymbol{C}''$""",
  CAT + " 3 occurrences.")

# ---------------------------------------------------------------- page 39
F(39, "(11.5.5): 'Alors R·T(K·, K'·) est un bifoncteur'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""Alors $\mathrm R^\bullet T(K^\bullet,K'^\bullet)$ est""",
  r"""Alors $\mathbf R^\bullet T(K^\bullet,K'^\bullet)$ est""",
  BOLDR)

F(39, "(11.5.5): 'un bifoncteur cohomologique en chacun des complexes'", "'cohomologique' in italics (crop)", "upright",
  "italics", None, "high",
  r"""bifoncteur cohomologique""",
  r"""bifoncteur \emph{cohomologique}""", "")

F(39, "(11.5.6.1): 'R·T(K·, K'·) ⥲ H·(T(L··, L'··))'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""\label{0.11.5.6.1-fr}
  \mathrm R^\bullet""",
  r"""\label{0.11.5.6.1-fr}
  \mathbf R^\bullet""",
  BOLDR)

F(39, "(11.5.6.1): end of the display", "no full stop after H·(T(L··, L'··)) (crop)", "full stop",
  "punctuation", None, "high",
  r"""L'^{\bullet\bullet})).
  \tag{11.5.6.1}""",
  r"""L'^{\bullet\bullet}))
  \tag{11.5.6.1}""",
  "Minor.")

F(39, "(11.5.6): 'les foncteurs A⇝T(A, L'^{hk})'", "wavy arrow ⇝", "\\mapsto",
  "symbol", None, "high",
  r"""$A\mapsto T(A,L'^{hk})$""",
  r"""$A\leadsto T(A,L'^{hk})$""",
  WAVY)

F(39, "(11.5.6): 'et A'⇝T(L^{ij}, A')'", "wavy arrow ⇝", "\\mapsto",
  "symbol", None, "high",
  r"""$A'\mapsto T(L^{ij},A')$""",
  r"""$A'\leadsto T(L^{ij},A')$""",
  WAVY)

F(39, "(11.5.6): 'soient exacts dans C et C' respectivement'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""exacts dans $\mathcal C$ et $\mathcal C'$ respectivement""",
  r"""exacts dans $\boldsymbol{C}$ et $\boldsymbol{C}'$ respectivement""",
  CAT + " 2 occurrences.")

F(39, "(11.5.6.2): 'R·T(K·, K'·) ...'", "bold R", "\\mathrm R",
  "font", None, "high",
  r"""\label{0.11.5.6.2-fr}
  \mathrm R^\bullet""",
  r"""\label{0.11.5.6.2-fr}
  \mathbf R^\bullet""",
  BOLDR)

F(39, "(11.5.6.2): first relation 'R·T(K·, K'·) ∼ H·(T(L··, K'·))'",
  "a tilde ∼ only, without the arrow (enlarged crop); the second relation has the isomorphism arrow ⥲",
  "\\xrightarrow{\\sim} (silently corrected)",
  "misprint_in_print", None, "high",
  r"""\xrightarrow{\sim}\mathrm H^\bullet(T(L^{\bullet\bullet},K'^\bullet))""",
  r"""\sim\mathrm H^\bullet(T(L^{\bullet\bullet},K'^\bullet))""",
  "The TeX silently corrects; the fix restores the printed reading. Both relations are isomorphisms ⥲, as in (11.4.7.1).",
  corrected=r"""\xrightarrow{\sim}\mathrm H^\bullet(T(L^{\bullet\bullet},K'^\bullet))""")

F(39, "(11.5.7): 'tout objet de C (resp. C') admet'", "C, C' bold italic", "\\mathcal C, \\mathcal C'",
  "font", None, "high",
  r"""objet de $\mathcal C$ (resp. $\mathcal C'$) admet""",
  r"""objet de $\boldsymbol{C}$ (resp. $\boldsymbol{C}'$) admet""",
  CAT + " 2 occurrences.")

F(39, "(11.6.1): 'Soient C une catégorie abélienne'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""Soient $\mathcal C$ une catégorie abélienne""",
  r"""Soient $\boldsymbol{C}$ une catégorie abélienne""",
  CAT)

F(39, "(11.6.1): 'un complexe d'objets de C, dont'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""d'objets de $\mathcal C$, dont""",
  r"""d'objets de $\boldsymbol{C}$, dont""",
  CAT)

F(39, "(11.6.1): 'Si tout objet de C est quotient d'un objet projectif'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""Si tout objet de $\mathcal C$ est quotient""",
  r"""Si tout objet de $\boldsymbol{C}$ est quotient""",
  CAT)

F(39, "(11.6.1): 'tout complexe K. de C admet'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""$K_\bullet$ de $\mathcal C$ admet une""",
  r"""$K_\bullet$ de $\boldsymbol{C}$ admet une""",
  CAT)

F(39, "(11.6.1): 'Si tout objet de C admet une résolution projective'", "C bold italic", "\\mathcal C",
  "font", None, "high",
  r"""objet de $\mathcal C$ admet une résolution projective""",
  r"""objet de $\boldsymbol{C}$ admet une résolution projective""",
  CAT)

F(39, "end of page_039.tex: \\begin{env}[11.6.2]",
  "printed p. 39 ends with '... on peut supposer que L_ij=0 pour j>n.'; '(11.6.2) Supposons que T soit ...' opens p. 40",
  "\\begin{env}[11.6.2] and its \\label stand before \\oldpage[0\\textsubscript{III}]{40}",
  "marker", None, "high",
  r"""\begin{env}[11.6.2]
\label{0.11.6.2-fr}
""",
  "",
  "Two-part move like the 3.7/3.8 headings in 0_I: this edit removes the opening of (11.6.2) from the end of p. 39's segment; "
  "the page-40 finding re-inserts it after \\oldpage[0\\textsubscript{III}]{40}. Apply both or neither.")

# ---------------------------------------------------------------- page 40 (outside 35-39: second half of the p. 39 move)
F(40, "start of page_040.tex: (11.6.2)", "p. 40 begins with '(11.6.2) Supposons que T soit un foncteur covariant additif'",
  "page_040.tex begins with the marker and 'Supposons'; \\begin{env}[11.6.2] stands in page_039.tex",
  "marker", None, "high",
  r"""\oldpage[0\textsubscript{III}]{40}
Supposons que $T$""",
  r"""\oldpage[0\textsubscript{III}]{40}
\begin{env}[11.6.2]
\label{0.11.6.2-fr}
Supposons que $T$""",
  "OUTSIDE pages 35-39: 'old' lies in page_040.tex. Second half of the page-39 marker finding. Apply both or neither.")

# ---------------------------------------------------------------- checks
pages = {}
bad = []
for d in findings:
    p = d["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    fx = d["fix"]
    if fx is None:
        continue
    n = pages[p].count(fx["old"])
    if n != 1:
        bad.append((p, n, fx["old"][:80]))
# overlapping olds on the same page
for p in pages:
    spans = []
    for d in findings:
        if d["page"] == p and d["fix"]:
            i = pages[p].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad.append((p, "overlap", a[2] + " | " + b[2]))
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
cnt = collections.defaultdict(lambda: [0, 0, 0])
for d in findings:
    k = 1 if d["kind"] == "convention" else 2 if d["kind"] == "misprint_in_print" else 0
    cnt[d["page"]][k] += 1
print("written", OUT, len(findings), "findings")
print({p: "/".join(map(str, c)) for p, c in sorted(cnt.items())})
print("problems:", bad if bad else "none")
