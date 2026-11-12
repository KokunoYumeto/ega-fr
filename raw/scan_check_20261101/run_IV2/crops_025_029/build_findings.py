# Build findings_025_029.json for EGA IV-2 pp. 25-29 and check every "old".
# "<NL>" in the strings below stands for a line break (LF).
import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV2"
OUT = os.path.join(RUN, "findings_025_029.json")


def R(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": R(old), "new": R(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = R(corrected)
    d["note"] = note
    F.append(d)


LBL = "GLOBAL_ISSUES 16: roman-numeral item label printed upright inside the italic statement."
DISP = "Layout: the print sets this formula inline in the running text; the TeX displays it (GLOBAL_ISSUES 21/51)."

# ---------------------------------------------------------------- page 25
add(25, "Proposition (2.5.8), l. 2: 'qui est un A-module fidèlement plat; on pose'",
    "'fidèlement plat' printed roman inside the italic statement (enlarged crop)",
    "fidèlement plat inside the italic proposition (typeset italic)",
    "convention", 6, "high",
    r"$A$-module fidèlement plat~;", r"$A$-module \textup{fidèlement plat}~;")
add(25, "Proposition (2.5.8), l. 2-3: 'on pose B'=B⊗_A A', V'=V⊗_A A', W'=W⊗_A A', de sorte que'",
    "the three formulas stand inline in the running text of the statement, separated by commas",
    "displayed: \\[ B'=B\\otimes_A A',\\qquad V'=...,\\qquad W'=..., \\]",
    "other", None, "high",
    r"on pose<NL>\[<NL>B'=B\otimes_A A',\qquad V'=V\otimes_A A',\qquad W'=W\otimes_A A',<NL>\]<NL>de sorte que",
    r"on pose $B'=B\otimes_A A'$, $V'=V\otimes_A A'$, $W'=W\otimes_A A'$, de sorte que",
    DISP)
add(25, "after (2.5.8.1), case (ii): 'V est facteur direct d'un B-module libre B^n_s'",
    "B^n_s (superscript n, subscript s; enlarged crop)",
    "$B_s$ (no exponent n)",
    "formula", None, "high",
    r"libre $B_s$, donc", r"libre $B_s^n$, donc")
add(25, "same sentence: 'facteur direct de Hom_B(B^n_s, W) = W^n'",
    "Hom_B(B^n_s, W) = W^n (enlarged crop)",
    "\\operatorname{Hom}_B(B_s,W)=W^s",
    "formula", None, "high",
    r"(B_s,W)=W^s$", r"(B_s^n,W)=W^n$",
    "Exponent n missing on B_s, and W^s for the printed W^n.")
add(25, "'Posons C = End_B(V), M = Hom_B(V, W)'",
    "'Posons' begins a new, indented paragraph (the line before is full)",
    "'Posons' continues the paragraph ending '... il en est de même de Hom_B(V,W).'",
    "other", None, "high",
    r"$\operatorname{Hom}_B(V,W)$. Posons", r"$\operatorname{Hom}_B(V,W)$.<NL><NL>Posons",
    "Missing paragraph break.")
add(25, "after (2.5.8.2): 'est bijectif (Bourbaki, Alg. comm., chap. II, § 2, no 10, prop. 11)'",
    "'bijectif' italic (enlarged crop)",
    "bijectif upright",
    "italics", None, "high",
    r"est bijectif (Bourbaki", r"est \emph{bijectif} (Bourbaki")
add(25, "before (2.5.8.3): 'on a donc u'((b⊗1)(x⊗1)) = u'(bx⊗1) = u(bx)⊗a' = bu(x)⊗a' = (b⊗1)(u(x)⊗a'), d'où notre assertion'",
    "the formula stands inline in the running text",
    "displayed \\[ ... \\] over two lines",
    "other", None, "high",
    r"on a donc<NL>\[<NL>u'((b\otimes1)(x\otimes1))=u'(bx\otimes1)=u(bx)\otimes a'<NL>=bu(x)\otimes a'=(b\otimes1)(u(x)\otimes a'),<NL>\]<NL>d'où",
    r"on a donc $u'((b\otimes1)(x\otimes1))=u'(bx\otimes1)=u(bx)\otimes a'=bu(x)\otimes a'=(b\otimes1)(u(x)\otimes a')$, d'où",
    DISP)
add(25, "(2.5.8.1): 'Sous l'une des hypothèses (i), (ii), Hom_B(V, W) est un A-module de type fini.'",
    "statement printed italic after the bold number, with '(i), (ii)' upright (enlarged crop)",
    "env body upright (the IV-2 env environment is roman)",
    "convention", 6, "high",
    r"\label{IV.2.5.8.1-fr}<NL>Sous l'une des hypothèses (i), (ii),",
    r"\label{IV.2.5.8.1-fr}<NL>\itshape Sous l'une des hypothèses \textup{(i), (ii)},",
    "Printed italic text left upright; \\itshape lasts to \\end{env} (same form as the EGA II p. 165 fix).")
add(25, "(2.5.8.3): 'Sous l'une des hypothèses (i), (ii), l'homomorphisme'",
    "statement printed italic, '(i), (ii)' upright (enlarged crop)",
    "env body upright",
    "convention", 6, "high",
    r"\label{IV.2.5.8.3-fr}<NL>Sous l'une des hypothèses (i), (ii),",
    r"\label{IV.2.5.8.3-fr}<NL>\itshape Sous l'une des hypothèses \textup{(i), (ii)},",
    "Printed italic text left upright.")
add(25, "(2.5.8.4): 'est bijectif.' after the display (end of the statement begun in (2.5.8.3))",
    "'est bijectif.' italic",
    "upright (env body)",
    "convention", 6, "high",
    r"\]<NL>est bijectif.<NL>\end{env}", r"\]<NL>\itshape est bijectif.<NL>\end{env}",
    "Printed italic text left upright.")
add(25, "'l'homothétie x ⇝ bx dans V (resp. W)'",
    "wavy arrow x ⇝ bx (enlarged crop)",
    "$x\\mapsto bx$",
    "symbol", None, "high",
    r"$x\mapsto bx$", r"$x\leadsto bx$",
    "Wavy maps-to arrow (GLOBAL_ISSUES 33); not convention 3.")
add(25, "display 'u ⇝ (h'(b_α)∘u — u∘h(b_α))_{α∈I}'",
    "wavy arrow after u (enlarged crop)",
    "u\\longmapsto(",
    "symbol", None, "high",
    r"u\longmapsto(h'(b_\alpha)", r"u\leadsto(h'(b_\alpha)",
    "Wavy maps-to arrow (GLOBAL_ISSUES 33).")
add(25, "same display: 'h'(b_α)∘u — u∘h(b_α)'",
    "long dash for the subtraction (bar 35 px against 25 px for '=' on this page)",
    "\\circ u-u\\circ h(b_\\alpha)",
    "convention", 7, "high",
    r"\circ u-u\circ h(b_\alpha)", r"\circ u\setmin u\circ h(b_\alpha)",
    "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(25, "'et par définition, son noyau n'est autre que Hom_B(V, W)'",
    "'noyau' italic (enlarged crop)",
    "noyau upright",
    "italics", None, "high",
    r"son noyau n'est", r"son \emph{noyau} n'est")
add(25, "'Le même raisonnement s'applique en remplaçant A, B, V, W par A', B', V', W''",
    "new, indented paragraph after the display of the exact sequence",
    "no blank line after \\]: the text continues the paragraph",
    "other", None, "high",
    r"(\operatorname{Hom}_A(V,W))^I.<NL>\]<NL>Le même", r"(\operatorname{Hom}_A(V,W))^I.<NL>\]<NL><NL>Le même",
    "Missing paragraph break.")
add(25, "diagram (2.5.8.5), vertical arrow r",
    "label r to the left of the arrow (enlarged crop)",
    "\\ar[d]^{r} (label right)",
    "other", None, "high",
    r"\ar[d]^{r}", r"\ar[d]_{r}",
    "Label side (cf. GLOBAL_ISSUES 30).")
add(25, "diagram (2.5.8.5), vertical arrow s",
    "label s to the left of the arrow (enlarged crop)",
    "\\ar[d]^{s} (label right)",
    "other", None, "high",
    r"\ar[d]^{s}", r"\ar[d]_{s}",
    "Label side (cf. GLOBAL_ISSUES 30).")
add(25, "diagram (2.5.8.5), vertical arrow t",
    "label t to the left of the arrow (enlarged crop)",
    "\\ar[d]^{t} (label right)",
    "other", None, "high",
    r"\ar[d]^{t}", r"\ar[d]_{t}",
    "Label side (cf. GLOBAL_ISSUES 30).")
add(25, "Proposition (2.5.8), label (i)",
    "label (i) upright (enlarged crop)",
    "\\item[(i)] inside the italic statement (typeset italic)",
    "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]", LBL)
add(25, "Proposition (2.5.8), label (ii)",
    "label (ii) upright (enlarged crop)",
    "\\item[(ii)] inside the italic statement (typeset italic)",
    "convention", 6, "high",
    r"\item[(ii)]", r"\item[\textup{(ii)}]", LBL)

# ---------------------------------------------------------------- page 26
add(26, "l. 1: 'dans le cas (ii), on peut prendre I fini, et on sait alors'",
    "'fini' italic (enlarged crop)",
    "fini upright",
    "italics", None, "high",
    r"prendre $I$ fini, et", r"prendre $I$ \emph{fini}, et")
add(26, "l. 3-4: 'donc on peut encore prendre I fini. Ainsi'",
    "'fini' italic (enlarged crop)",
    "fini upright",
    "italics", None, "high",
    r"encore prendre $I$ fini.", r"encore prendre $I$ \emph{fini}.")
add(26, "(2.5.8.6), last line: 'un di-isomorphisme de C'-modules à droite.'",
    "'modules' set italic in this roman sentence (enlarged crop)",
    "$C'$-modules upright (silently corrected)",
    "misprint_in_print", None, "medium",
    r"$C'$-modules à droite.\par}", r"$C'$-\emph{modules} à droite.\par}",
    "Wrong-font word: nothing in the sentence calls for emphasis on 'modules' alone; the TeX's roman reading is the corrected one. If the coordinator prefers an ordinary italics difference, the same edit applies to both editions.",
    corrected=r"$C'$-modules à droite.\par}")
add(26, "(2.5.8.7), l. 2: 'sont des C'-modules à droite isomorphes (2.5.6)'",
    "'isomorphes' italic (enlarged crop)",
    "isomorphes upright (env body)",
    "italics", None, "high",
    r"droite isomorphes (2.5.6)", r"droite \emph{isomorphes} (2.5.6)")
add(26, "(2.5.8.7), l. 3: 'trouver un élément u∈M qui soit un générateur de M'",
    "'générateur' italic",
    "générateur upright",
    "italics", None, "high",
    r"qui soit un générateur", r"qui soit un \emph{générateur}")
add(26, "(2.5.8.7): 'cela entraîne que u est bijectif (0_I, 6.4.1)'",
    "(0_I, 6.4.1) with a bold 0 (enlarged crop)",
    "$(0_{\\mathrm I},6.4.1)$, plain 0",
    "convention", 2, "high",
    r"$(0_{\mathrm I},6.4.1)$", r"$(\mathbf{0}_{\mathrm I},6.4.1)$",
    "Bold 0 as in GLOBAL_ISSUES 35.")
add(26, "(2.5.8.7), end: 'il suffit de prouver l'existence d'un générateur du B-module W'",
    "'générateur' italic (enlarged crop)",
    "générateur upright",
    "italics", None, "high",
    r"l'existence d'un générateur du", r"l'existence d'un \emph{générateur} du")
add(26, "(2.5.8.7), last sentence: 'On notera qu'alors B est un A-module de type fini.'",
    "'de type fini' italic (enlarged crop)",
    "de type fini upright",
    "italics", None, "high",
    r"qu'alors $B$ est un $A$-module de type fini.", r"qu'alors $B$ est un $A$-module \emph{de type fini}.")
add(26, "(2.5.8.8): 'l'homomorphisme surjectif considéré est f⊗1 : B_s⊗_A(A/r) → W⊗_A(A/r). Comme W'",
    "the formula stands inline in the running text",
    "displayed \\[ f\\otimes1:...\\longrightarrow W\\otimes_A(A/\\mathfrak r). \\]",
    "other", None, "high",
    r"surjectif considéré est<NL>\[<NL>f\otimes1:B_s\otimes_A(A/\mathfrak r)\longrightarrow<NL>W\otimes_A(A/\mathfrak r).<NL>\]<NL>Comme",
    r"surjectif considéré est $f\otimes1:B_s\otimes_A(A/\mathfrak r)\longrightarrow W\otimes_A(A/\mathfrak r)$. Comme",
    DISP)
add(26, "(2.5.8.8): 'Si l'on pose A_1=A/r, A'_1=A'⊗_A A_1=A'/rA', B_1=B/rB=B⊗_A A_1, W_1=W/rW=W⊗_A A_1, les hypothèses'",
    "the four formulas stand inline in the running text, separated by commas",
    "displayed, joined by \\quad",
    "other", None, "high",
    r"Si l'on pose<NL>\[<NL>A_1=A/\mathfrak r,\quad A'_1=A'\otimes_A A_1=A'/\mathfrak rA',\quad<NL>B_1=B/\mathfrak rB=B\otimes_A A_1,\quad<NL>W_1=W/\mathfrak rW=W\otimes_A A_1,<NL>\]<NL>les hypothèses",
    r"Si l'on pose $A_1=A/\mathfrak r$, $A'_1=A'\otimes_A A_1=A'/\mathfrak rA'$, $B_1=B/\mathfrak rB=B\otimes_A A_1$, $W_1=W/\mathfrak rW=W\otimes_A A_1$, les hypothèses",
    DISP)
add(26, "(2.5.8.8): 'c'est un anneau artinien; soit ℜ son radical'",
    "'artinien' italic (enlarged crop); the radical letter is a Fraktur R (compared with the R of 0_I p. 12 and the N of 0_IV p. 92)",
    "artinien upright",
    "italics", None, "high",
    r"anneau artinien~;", r"anneau \emph{artinien}~;")
add(26, "(2.5.8.8): 'et l'on a B'/ℜB' = (B⊗_A A')⊗_B(B/ℜ) = (B/ℜ)⊗_A A' et de même W'/ℜW' = (W⊗_A A')⊗_B(B/ℜ) = (W/ℜW)⊗_A A'. On peut donc'",
    "both formulas stand inline in the running text",
    "two displays",
    "other", None, "high",
    r"et l'on a<NL>\[<NL>B'/\mathfrak RB'=(B\otimes_A A')\otimes_B(B/\mathfrak R)<NL>=(B/\mathfrak R)\otimes_A A'<NL>\]<NL>et de même<NL>\[<NL>W'/\mathfrak RW'=(W\otimes_A A')\otimes_B(B/\mathfrak R)<NL>=(W/\mathfrak RW)\otimes_A A'.<NL>\]<NL>On peut donc",
    r"et l'on a $B'/\mathfrak RB'=(B\otimes_A A')\otimes_B(B/\mathfrak R)=(B/\mathfrak R)\otimes_A A'$ et de même $W'/\mathfrak RW'=(W\otimes_A A')\otimes_B(B/\mathfrak R)=(W/\mathfrak RW)\otimes_A A'$. On peut donc",
    DISP)
add(26, "(2.5.8.8): 'c'est-à-dire que B est une A-algèbre semi-simple.'",
    "'semi-simple' italic (enlarged crop)",
    "semi-simple upright",
    "italics", None, "high",
    r"$A$-algèbre semi-simple.", r"$A$-algèbre \emph{semi-simple}.")
add(26, "'chacune des A'_i étant annulée par les k_j d'indice j ≠ 1'",
    "j ≠ 1: old-style figure one (serifed small-capital I at x-height, no dot), the same glyph as the 1 of (1≤i≤n) on the line above (7x crop)",
    "$j\\ne i$ (silently corrected)",
    "misprint_in_print", None, "high",
    r"$j\ne i$~; l'hypothèse", r"$j\ne1$~; l'hypothèse",
    "The index must differ from i (as in 'j ≠ i' twice further down the page). The diplomatic text restores the printed 1.",
    corrected=r"$j\ne i$~; l'hypothèse")
add(26, "'autrement dit, supposer que A est le centre de B, B étant semi-simple'",
    "'centre' italic (enlarged crop)",
    "centre upright",
    "italics", None, "high",
    r"le centre de $B$, $B$ étant", r"le \emph{centre} de $B$, $B$ étant")

# ---------------------------------------------------------------- page 27
add(27, "l. 2: 'dans le cas où A et A' sont des corps'",
    "'corps' italic (enlarged crop)",
    "corps upright (env body)",
    "italics", None, "high",
    r"sont des<NL>corps, $B$", r"sont des<NL>\emph{corps}, $B$")
add(27, "l. 2: 'B une algèbre simple de centre A'",
    "'simple' italic (enlarged crop)",
    "simple upright",
    "italics", None, "high",
    r"algèbre simple", r"algèbre \emph{simple}")
add(27, "l. 2: 'de centre A'",
    "'centre' italic (enlarged crop)",
    "centre upright",
    "italics", None, "high",
    r"centre $A$.", r"\emph{centre} $A$.")
add(27, "(2.5.8.9): 'si et seulement s'ils ont même rang sur A'",
    "'même rang' italic (enlarged crop)",
    "même rang upright",
    "italics", None, "high",
    r"même rang sur", r"\emph{même rang} sur")
add(27, "heading 2.6",
    "'2.6. Permanence de propriétés ensemblistes et topologiques de morphismes par descente fidèlement plate.' (final full stop)",
    "no full stop",
    "punctuation", None, "high",
    r"par descente fidèlement plate}", r"par descente fidèlement plate.}",
    "No \\subsection title in ega4-2-fr.tex has the printed full stop (see final message).")
add(27, "Proposition (2.6.1), l. 2: 'X'→X_(S'), Y'=Y_(S'), f'=f_(S') : X'→Y''",
    "X' → X_(S') with an arrow (enlarged crop)",
    "$X'=X_{(S')}$ (silently corrected)",
    "misprint_in_print", None, "high",
    r"$X'=X_{(S')}$", r"$X'\to X_{(S')}$",
    "Recorded in the EGA IV errata ((IV, 2.6.1): 'Ligne 10 de la p. 27, remplacer X'→X_(S') par X'=X_(S')', ega4-errata-addenda-list3-fr.tex). The diplomatic text restores the printed arrow.",
    corrected=r"$X'=X_{(S')}$")
add(27, "Proposition (2.6.1), label (i)",
    "label (i) upright", "\\item[(i)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(i)] surjectif", r"\item[\textup{(i)}] surjectif", LBL)
add(27, "Proposition (2.6.1), label (ii)",
    "label (ii) upright", "\\item[(ii)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(ii)] injectif", r"\item[\textup{(ii)}] injectif", LBL)
add(27, "Proposition (2.6.1), label (iii)",
    "label (iii) upright", "\\item[(iii)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(iii)] à fibres", r"\item[\textup{(iii)}] à fibres", LBL)
add(27, "Proposition (2.6.1), label (iv)",
    "label (iv) upright", "\\item[(iv)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(iv)] bijectif", r"\item[\textup{(iv)}] bijectif", LBL)
add(27, "Proposition (2.6.1), label (v)",
    "label (v) upright", "\\item[(v)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(v)]", r"\item[\textup{(v)}]", LBL)
add(27, "Proposition (2.6.1) (iii): 'à fibres finies (en tant qu'ensembles);'",
    "'(en tant qu'' roman, only 'ensembles' italic, closing parenthesis roman (enlarged crop)",
    "whole parenthesis italic inside the italic proposition",
    "convention", 6, "high",
    r"(en tant qu'ensembles)", r"\textup{(en tant qu'\emph{ensembles})}",
    "Inside \\textup the \\emph sets 'ensembles' italic, as printed.")
add(27, "Proposition (2.6.1), last sentence: 'si P désigne ... la propriété P' (two occurrences)",
    "property letter P bold italic, twice (enlarged crop)",
    "plain $P$ twice",
    "font", None, "high",
    r"radiciel.<NL>\end{enumerate}<NL>Alors, si $P$ désigne une des propriétés précédentes et si $f'$ possède la<NL>propriété $P$",
    r"radiciel.<NL>\end{enumerate}<NL>Alors, si $\boldsymbol{P}$ désigne une des propriétés précédentes et si $f'$ possède la<NL>propriété $\boldsymbol{P}$",
    "One edit for both P's: the sentence is repeated word for word in (2.6.2) on this page, so 'old' starts at the last item to be unique. Not convention 10 (the TeX has plain P, not \\mathbf{P}); same treatment as GLOBAL_ISSUES 44.")
add(27, "proof of (2.6.1), l. 3: 'le préschéma fibre f^{-1}(y) (resp. f'^{-1}(y))'",
    "f'^{-1}(y) without a prime on y (6x crop)",
    "$f'^{-1}(y')$ (silently corrected)",
    "misprint_in_print", None, "high",
    r"$f'^{-1}(y')$", r"$f'^{-1}(y)$",
    "X'_{y'} is the fibre of f' at y'; the print drops the prime. The diplomatic text restores the printed y.",
    corrected=r"$f'^{-1}(y')$")
add(27, "proof of (2.6.1), l. 1: 'lui aussi surjectif (I, 3.5.2)'",
    "(I, 3.5.2) with a bold I", "plain I",
    "convention", 2, "high", r"aussi surjectif (I, 3.5.2)", r"aussi surjectif (\textbf{I}, 3.5.2)")
add(27, "proof of (2.6.1), l. 2: 'en vertu de (I, 3.3.11)'",
    "(I, 3.3.11) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.3.11)", r"(\textbf{I}, 3.3.11)")
add(27, "proof of (2.6.1), l. 3: '(I, 3.6.2)'",
    "(I, 3.6.2) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.6.2)", r"(\textbf{I}, 3.6.2)")
add(27, "proof of (2.6.1), l. 4: 'on a un isomorphisme canonique X'_{y'} ⥲ X_y⊗_{k(y)}k(y') (I, 3.6.4); comme le morphisme'",
    "the formula and (I, 3.6.4) stand inline in the running text",
    "displayed \\[ X'_{y'}\\xrightarrow{\\sim}...\\quad\\text{(I, 3.6.4)}~; \\]",
    "other", None, "high",
    r"canonique<NL>\[<NL>X'_{y'}\xrightarrow{\sim}X_y\otimes_{k(y)}k(y')\quad\text{(I, 3.6.4)}~;<NL>\]<NL>comme",
    r"canonique $X'_{y'}\xrightarrow{\sim}X_y\otimes_{k(y)}k(y')$ (I, 3.6.4)~;<NL>comme",
    DISP + " Apply before the three fixes below that touch this formula (their 'old' lies inside this one).")
add(27, "same formula: subscript k(y) of ⊗",
    "bold upright k in the subscript k(y) (enlarged crop)", "plain k",
    "convention", 1, "high", r"\otimes_{k(y)}", r"\otimes_{\mathbf{k}(y)}",
    "Bold upright in a subscript (GLOBAL_ISSUES 48). Apply after the display fix above.")
add(27, "same formula: k(y')",
    "bold italic k (enlarged crop)", "plain k",
    "convention", 1, "high", r"}k(y')", r"}\boldsymbol{k}(y')",
    "Apply after the display fix above.")
add(27, "same formula: '(I, 3.6.4)'",
    "(I, 3.6.4) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)",
    "Apply after the display fix above.")
add(27, "proof of (2.6.1), l. 5: 'Spec(k(y'))'",
    "bold italic k", "plain k",
    "convention", 1, "high", r"\operatorname{Spec}(k(y'))", r"\operatorname{Spec}(\boldsymbol{k}(y'))")
add(27, "proof of (2.6.1), l. 5: 'Spec(k(y))'",
    "bold italic k", "plain k",
    "convention", 1, "high", r"\operatorname{Spec}(k(y))", r"\operatorname{Spec}(\boldsymbol{k}(y))")
add(27, "proof of (2.6.1), l. 6: 'la projection X'_{y'}→X_y (I, 3.5.2);'",
    "(I, 3.5.2) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.5.2)~; donc", r"(\textbf{I}, 3.5.2)~; donc")
add(27, "proof of (2.6.1), l. 9: 'universellement injectif (I, 3.5.11)'",
    "(I, 3.5.11) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.5.11)", r"(\textbf{I}, 3.5.11)")
add(27, "proof of (2.6.1): 'D'autre part, posons Y'_1=Y_1×_Y Y', X'_1=X'×_{Y'}Y'_1=X_1×_{Y_1}Y'_1, f'_1=f'_{(Y'_1)}=(f_1)_{(Y'_1)} : X'_1→Y'_1; comme'",
    "the formulas stand inline in the running text",
    "displayed, joined by \\quad",
    "other", None, "high",
    r"posons<NL>\[<NL>Y'_1=Y_1\times_Y Y',\quad X'_1=X'\times_{Y'}Y'_1=X_1\times_{Y_1}Y'_1,<NL>\quad f'_1=f'_{(Y'_1)}=(f_1)_{(Y'_1)}:X'_1\to Y'_1~;<NL>\]<NL>",
    r"posons $Y'_1=Y_1\times_Y Y'$, $X'_1=X'\times_{Y'}Y'_1=X_1\times_{Y_1}Y'_1$, $f'_1=f'_{(Y'_1)}=(f_1)_{(Y'_1)}:X'_1\to Y'_1$~;<NL>",
    DISP)
add(27, "proof of (2.6.1), end: 'comme g'=g_(Y_1) : Y'_1→Y' est surjectif'",
    "target Y' (prime, no subscript 1; 4x crop)",
    "$g'=g_{(Y_1)}:Y'_1\\to Y_1$ (silently corrected)",
    "misprint_in_print", None, "high",
    r"g'=g_{(Y_1)}:Y'_1\to Y_1$", r"g'=g_{(Y_1)}:Y'_1\to Y'$",
    "g_(Y_1) maps Y'_1=Y_1×_Y Y' onto Y_1, and the argument needs Y'_1→Y_1 surjective. The diplomatic text restores the printed Y'.",
    corrected=r"g'=g_{(Y_1)}:Y'_1\to Y_1$")
add(27, "proof of (2.6.1), end: 'est surjectif (I, 3.5.2) et que f''",
    "(I, 3.5.2) with a bold I", "plain I",
    "convention", 2, "high", r"surjectif (I, 3.5.2) et que", r"surjectif (\textbf{I}, 3.5.2) et que")
add(27, "Proposition (2.6.2): 'Les notations étant celles de (2.6.1),'",
    "reference set roman: upright parentheses and figures (enlarged crop)",
    "(2.6.1) inside the italic proposition (typeset italic)",
    "convention", 6, "high", r"celles de (2.6.1),", r"celles de \textup{(2.6.1)},")
add(27, "Proposition (2.6.2), label (i)",
    "label (i) upright", "\\item[(i)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(i)] ouvert", r"\item[\textup{(i)}] ouvert", LBL)
add(27, "Proposition (2.6.2), label (ii)",
    "label (ii) upright", "\\item[(ii)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(ii)] fermé", r"\item[\textup{(ii)}] fermé", LBL)
add(27, "Proposition (2.6.2), label (iii)",
    "label (iii) upright", "\\item[(iii)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(iii)] quasi-compact", r"\item[\textup{(iii)}] quasi-compact", LBL)
add(27, "Proposition (2.6.2), label (iv)",
    "label (iv) upright", "\\item[(iv)] inside the italic statement (typeset italic)",
    "convention", 6, "high", r"\item[(iv)] un", r"\item[\textup{(iv)}] un", LBL)
add(27, "Proposition (2.6.2), last sentence: 'si P désigne ... la propriété P' (two occurrences)",
    "property letter P bold italic, twice",
    "plain $P$ twice",
    "font", None, "high",
    r"homéomorphisme.<NL>\end{enumerate}<NL>Alors, si $P$ désigne une des propriétés précédentes et si $f'$ possède la<NL>propriété $P$",
    r"homéomorphisme.<NL>\end{enumerate}<NL>Alors, si $\boldsymbol{P}$ désigne une des propriétés précédentes et si $f'$ possède la<NL>propriété $\boldsymbol{P}$",
    "One edit for both P's (the sentence repeats that of (2.6.1)).")

# ---------------------------------------------------------------- page 28
add(28, "proof of (2.6.2), l. 2: 'en vertu de (I, 3.3.11)'",
    "(I, 3.3.11) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.3.11)", r"(\textbf{I}, 3.3.11)")
add(28, "proof of (2.6.2), l. 3-4: 'pour toute partie M de X, g^{-1}(f(M)) = f'(g'^{-1}(M)) (I, 3.4.8). Si f''",
    "the formula and (I, 3.4.8) stand inline in the running text",
    "displayed \\[ ...\\quad\\text{(I, 3.4.8).} \\]",
    "other", None, "high",
    r"partie $M$ de $X$,<NL>\[<NL>g^{-1}(f(M))=f'(g'^{-1}(M))\quad\text{(I, 3.4.8).}<NL>\]<NL>Si $f'$",
    r"partie $M$ de $X$, $g^{-1}(f(M))=f'(g'^{-1}(M))$ (I, 3.4.8). Si $f'$",
    DISP + " Apply before the (I, 3.4.8) fix below.")
add(28, "same place: '(I, 3.4.8)'",
    "(I, 3.4.8) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.4.8)", r"(\textbf{I}, 3.4.8)",
    "Apply after the display fix above.")
add(28, "proof of (2.6.2): 'est une application quasi-compacte et ouverte.'",
    "'ouverte' italic (enlarged crop)",
    "ouverte upright",
    "italics", None, "high",
    r"quasi-compacte et ouverte.", r"quasi-compacte et \emph{ouverte}.")
add(28, "proof of (2.6.2): 'Comme f' est quasi-compacte, il en est de même de f (1.1.4)'",
    "'quasi-compacte' (feminine, as for 'application' just before; enlarged crop)",
    "quasi-compact",
    "word", None, "high",
    r"Comme $f'$ est quasi-compact, il", r"Comme $f'$ est quasi-compacte, il",
    "The feminine agrees with 'application' in the preceding sentence; not treated as a misprint.")
add(28, "proof of (2.6.2): 'pour toute partie fermée Z de X, on a Z=f^{-1}(f(Z))‾; comme g''",
    "the formula stands inline in the running text",
    "displayed \\[ Z=f^{-1}(\\overline{f(Z)})~; \\]",
    "other", None, "high",
    r"on a<NL>\[<NL>Z=f^{-1}(\overline{f(Z)})~;<NL>\]<NL>comme",
    r"on a $Z=f^{-1}(\overline{f(Z)})$~; comme",
    DISP + " Apply before the overline fix below.")
add(28, "same formula: the bar in f^{-1}((f(Z)))‾",
    "the bar covers the parenthesised argument (f(Z)), parentheses included (enlarged crop)",
    "f^{-1}(\\overline{f(Z)}): bar over f(Z) only",
    "formula", None, "medium",
    r"Z=f^{-1}(\overline{f(Z)})", r"Z=f^{-1}\overline{(f(Z))}",
    "Same meaning; extent of the bar (cf. the Ē_β findings of 0_III p. 15). Apply after the display fix above.")
add(28, "proof of (2.6.2): 'cette relation équivaut à g'^{-1}(Z)=g'^{-1}(f^{-1}(f(Z))‾) ou encore à g'^{-1}(Z)=f'^{-1}(g^{-1}(f(Z))‾). Or,'",
    "two equations inline in the running text, joined by 'ou encore à'",
    "one chained display g'^{-1}(Z)=g'^{-1}(...)=f'^{-1}(...): the words 'ou encore à' and the second 'g'^{-1}(Z)' are missing",
    "missing", None, "high",
    r"équivaut à<NL>\[<NL>g'^{-1}(Z)=g'^{-1}(f^{-1}(\overline{f(Z)}))<NL>=f'^{-1}(g^{-1}(\overline{f(Z)})).<NL>\]<NL>Or, comme",
    r"équivaut à $g'^{-1}(Z)=g'^{-1}(f^{-1}(\overline{f(Z)}))$ ou encore à $g'^{-1}(Z)=f'^{-1}(g^{-1}(\overline{f(Z)}))$. Or, comme",
    "Display set inline as printed, with the lost connecting words restored (GLOBAL_ISSUES 51). Apply before the two overline fixes below.")
add(28, "same place: the bar in g'^{-1}(f^{-1}((f(Z)))‾)",
    "the bar covers (f(Z)), parentheses included", "bar over f(Z) only",
    "formula", None, "medium",
    r"g'^{-1}(f^{-1}(\overline{f(Z)}))", r"g'^{-1}(f^{-1}\overline{(f(Z))})",
    "Same meaning; extent of the bar. Apply after the display fix above.")
add(28, "same place: the bar in f'^{-1}(g^{-1}((f(Z)))‾)",
    "the bar covers (f(Z)), parentheses included", "bar over f(Z) only",
    "formula", None, "medium",
    r"f'^{-1}(g^{-1}(\overline{f(Z)}))", r"f'^{-1}(g^{-1}\overline{(f(Z))})",
    "Same meaning; extent of the bar. Apply after the display fix above.")
add(28, "proof of (2.6.2): 'on obtient g^{-1}((f(Z)))‾ = g^{-1}(f(Z))‾; la formule'",
    "the formula stands inline in the running text",
    "displayed",
    "other", None, "high",
    r"on obtient<NL>\[<NL>g^{-1}(\overline{f(Z)})=\overline{g^{-1}(f(Z))}~;<NL>\]<NL>la formule",
    r"on obtient $g^{-1}(\overline{f(Z)})=\overline{g^{-1}(f(Z))}$~; la formule",
    DISP + " Apply before the overline fix below.")
add(28, "same formula: the bar in g^{-1}((f(Z)))‾ (left side)",
    "the bar covers (f(Z)), parentheses included; the right-hand bar over g^{-1}(f(Z)) matches the TeX",
    "bar over f(Z) only",
    "formula", None, "medium",
    r"g^{-1}(\overline{f(Z)})=", r"g^{-1}\overline{(f(Z))}=",
    "Same meaning; extent of the bar. Apply after the display fix above.")
add(28, "proof of (2.6.2): 'équivaut donc à la suivante : Z'=f'^{-1}((f'(Z')))‾, où l'on a posé'",
    "the formula stands inline in the running text",
    "displayed",
    "other", None, "high",
    r"la suivante~:<NL>\[<NL>Z'=f'^{-1}(\overline{f'(Z')}),<NL>\]<NL>où l'on",
    r"la suivante~: $Z'=f'^{-1}(\overline{f'(Z')})$, où l'on",
    DISP + " Apply before the overline fix below.")
add(28, "same formula: the bar in f'^{-1}((f'(Z')))‾",
    "the bar covers (f'(Z')), parentheses included", "bar over f'(Z') only",
    "formula", None, "medium",
    r"f'^{-1}(\overline{f'(Z')})", r"f'^{-1}\overline{(f'(Z'))}",
    "Same meaning; extent of the bar. Apply after the display fix above.")
add(28, "Remarque (2.6.3), l. 2: 'seulement g quasi-fidèlement plat (2.3.3)'",
    "'quasi-fidèlement plat' italic in the roman remark (enlarged crop)",
    "no \\emph (remark body)",
    "italics", None, "high",
    r"quasi-fidèlement plat (2.3.3)", r"\emph{quasi-fidèlement plat} (2.3.3)",
    "Judged with the remark body roman (document-wide remark item); under the current italic remark environment \\emph sets it upright until that change.")
add(28, "Remarque (2.6.3), l. 2: 'et quasi-compact; en effet'",
    "'quasi-compact' italic in the roman remark (enlarged crop)",
    "no \\emph (remark body)",
    "italics", None, "high",
    r"et<NL>quasi-compact~;", r"et<NL>\emph{quasi-compact}~;",
    "Judged with the remark body roman.")
add(28, "Remarque (2.6.3), l. 3: '(I, 3.5.2)'",
    "(I, 3.5.2) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 3.5.2)", r"(\textbf{I}, 3.5.2)")
add(28, "Remarque (2.6.3), l. 3: '(I, 9.1.13.1)'",
    "(I, 9.1.13.1) with a bold I", "plain I",
    "convention", 2, "high", r"(I, 9.1.13.1)", r"(\textbf{I}, 9.1.13.1)")
add(28, "Remarque (2.6.3), l. 5: 'quand on suppose seulement g quasi-fidèlement plat, pourvu que'",
    "'quasi-fidèlement plat' italic (enlarged crop)",
    "no \\emph (remark body)",
    "italics", None, "high",
    r"quasi-fidèlement<NL>plat, pourvu", r"\emph{quasi-fidèlement<NL>plat}, pourvu",
    "Judged with the remark body roman.")
add(28, "Remarque (2.6.3): 'la conclusion de (2.6.2) est valable lorsque P est la propriété'",
    "property letter P bold italic", "plain $P$",
    "font", None, "high", r"lorsque $P$ est", r"lorsque $\boldsymbol{P}$ est")
add(28, "Remarque (2.6.3), item (iii bis): 'être un homéomorphisme sur le sous-espace image;'",
    "item text italic; label '(iii' roman with 'bis' italic, as in the TeX (enlarged crop)",
    "item text without \\emph (remark body)",
    "italics", None, "high",
    r"être un homéomorphisme sur le sous-espace image", r"\emph{être un homéomorphisme sur le sous-espace image}",
    "Judged with the remark body roman.")
add(28, "Corollaire (2.6.4): 'Les notations étant celles de (2.6.1),'",
    "reference set roman: upright parentheses and figures (enlarged crop)",
    "(2.6.1) inside the italic corollary (typeset italic)",
    "convention", 6, "high", r"celles de (2.6.1),", r"celles de \textup{(2.6.1)},")
for lab in ["i", "ii", "iii", "iv", "v", "vi"]:
    add(28, "Corollaire (2.6.4), label (%s)" % lab,
        "label (%s) upright" % lab, "\\item[(%s)] inside the italic statement (typeset italic)" % lab,
        "convention", 6, "high", r"\item[(%s)]" % lab, r"\item[\textup{(%s)}]" % lab, LBL)
add(28, "Corollaire (2.6.4), last sentence: 'si P désigne une des propriétés précédentes'",
    "property letter P bold italic", "plain $P$",
    "font", None, "high", r"si $P$ désigne", r"si $\boldsymbol{P}$ désigne")
add(28, "Corollaire (2.6.4), last sentence: 'pour que f possède la propriété P, il faut'",
    "property letter P bold italic", "plain $P$",
    "font", None, "high", r"propriété $P$, il faut", r"propriété $\boldsymbol{P}$, il faut")

# ---------------------------------------------------------------- page 29
add(29, "proof of (2.6.4): 'D'autre part, posons Y'_1=Y_1×_Y Y', X'_1=X'×_{Y'}Y'_1=X_1×_{Y_1}Y'_1, f'_1=f'_{(Y'_1)}=f_{1(Y'_1)} : X'_1→Y'_1; comme'",
    "the formulas stand inline in the running text",
    "displayed, joined by \\qquad",
    "other", None, "high",
    r"posons<NL>\[<NL>Y'_1=Y_1\times_Y Y',\qquad<NL>X'_1=X'\times_{Y'}Y'_1=X_1\times_{Y_1}Y'_1,<NL>\qquad f'_1=f'_{(Y'_1)}=f_{1(Y'_1)}:X'_1\to Y'_1~;<NL>\]<NL>comme",
    r"posons $Y'_1=Y_1\times_Y Y'$, $X'_1=X'\times_{Y'}Y'_1=X_1\times_{Y_1}Y'_1$, $f'_1=f'_{(Y'_1)}=f_{1(Y'_1)}:X'_1\to Y'_1$~;<NL>comme",
    DISP)
add(29, "proof of (2.6.4): 'comme g'=g_(Y') : Y'_1→Y' est fidèlement plat et quasi-compact (2.2.13 et 1.1.2)'",
    "g'=g_(Y') : Y'_1→Y' (enlarged crop)",
    "$g'=g_{(Y')}:Y'_1\\to Y'$ (keeps the printed reading)",
    "misprint_in_print", None, "medium",
    None, None,
    "Error in the print, not in the published errata: applying (2.6.2) to f_1 : X_1→Y_1 needs the faithfully flat quasi-compact base change Y'_1=Y_1×_Y Y'→Y_1, i.e. g_(Y_1) : Y'_1→Y_1 (as in the parallel argument of (2.6.1) on p. 27); Y'_1→Y' is the base change of the arbitrary Y_1→Y. Corrected edition: replace 'g'=g_{(Y')}:Y'_1\\to Y'' by 'g'=g_{(Y_1)}:Y'_1\\to Y_1'.",
    corrected=r"g'=g_{(Y_1)}:Y'_1\to Y_1", nofix=True)
add(29, "'on peut remplacer la propriété (iii) par : (iii bis) universellement bicontinu.'",
    "item text italic (label '(iii' roman, 'bis' italic, as in the TeX)",
    "item text upright (roman running text)",
    "italics", None, "high",
    r"universellement bicontinu.", r"\emph{universellement bicontinu}.")
add(29, "heading 2.7",
    "'2.7. Permanence de diverses propriétés des morphismes par descente fidèlement plate.' (final full stop)",
    "no full stop",
    "punctuation", None, "high",
    r"fidèlement plate}", r"fidèlement plate.}",
    "As heading 2.6 (p. 27).")
for lab in ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii",
            "xiii", "xiv", "xv", "xvi", "xvii"]:
    add(29, "Proposition (2.7.1), label (%s)" % lab,
        "label (%s) upright" % lab, "\\item[(%s)] inside the italic statement (typeset italic)" % lab,
        "convention", 6, "high", r"\item[(%s)]" % lab, r"\item[\textup{(%s)}]" % lab, LBL)
add(29, "Proposition (2.7.1), last sentence: 'si P désigne une des propriétés précédentes'",
    "property letter P bold italic", "plain $P$",
    "font", None, "high", r"si $P$ désigne", r"si $\boldsymbol{P}$ désigne")
add(29, "Proposition (2.7.1), last sentence: 'pour que f possède la propriété P, il faut'",
    "property letter P bold italic", "plain $P$",
    "font", None, "high", r"propriété $P$, il faut", r"propriété $\boldsymbol{P}$, il faut")
add(29, "after (2.7.1): 'si f possède une des propriétés P ci-dessus'",
    "property letter P bold italic (enlarged crop)", "plain $P$",
    "font", None, "high", r"propriétés $P$ ci-dessus", r"propriétés $\boldsymbol{P}$ ci-dessus")

# ---------------------------------------------------------------- checks
ok = True
for p in sorted({d["page"] for d in F}):
    txt = open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8").read().replace("\r\n", "\n")
    cur = txt
    for d in [x for x in F if x["page"] == p]:
        fx = d["fix"]
        if fx is None:
            continue
        n0 = txt.count(fx["old"])
        n1 = cur.count(fx["old"])
        if n0 != 1 or n1 != 1:
            ok = False
            print("PROBLEM p%d count_orig=%d count_seq=%d: %r" % (p, n0, n1, fx["old"][:80]))
        else:
            cur = cur.replace(fx["old"], fx["new"], 1)
    # misprint without fix: check the tex substring exists
    for d in [x for x in F if x["page"] == p and x["fix"] is None]:
        if "g'=g_{(Y')}:Y'_1\\to Y'" not in txt:
            ok = False
            print("PROBLEM: kept-misprint text not found on p%d" % p)

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "misprint_in_print":
        c[2] += 1
    elif d["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts, "total", len(F))
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
else:
    sys.exit(1)
