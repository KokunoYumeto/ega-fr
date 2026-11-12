"""Build findings_091_095.json (checker for 0_IV-1 pp. 91-95), check every "old" and simulate apply_fixes.py.
TeX strings are raw; the pilcrow stands for a line break (LF)."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_0IV1"
OUT = RUN / "findings_091_095.json"
REL = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex"
PART = r"0\textsubscript{IV-1}"


def L(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note=None, corrected=None):
    x = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=L(old), new=L(new)))
    if kind == "misprint_in_print":
        x["corrected"] = L(corrected)
    x["note"] = note
    F.append(x)


M91 = r"\oldpage[0\textsubscript{IV-1}]{91}"
M92 = r"\oldpage[0\textsubscript{IV-1}]{92}"
M93 = r"\oldpage[0\textsubscript{IV-1}]{93}"
M94 = r"\oldpage[0\textsubscript{IV-1}]{94}"
M95 = r"\oldpage[0\textsubscript{IV-1}]{95}"

# ---------------- page 91 ----------------
add(91, "first line: 'appliquée à la A-algèbre topologique E = gr•_{𝔍/𝔍^n}(B/𝔍^n)'",
    "A-algèbre (enlarged crop)", "$C$-algèbre (silently corrected)", "misprint_in_print",
    r"à la $C$-algèbre", r"à la $A$-algèbre",
    corrected=r"à la $C$-algèbre",
    note="The universal property (19.5.1) of S•_C is stated for C-algebras ('pour les catégories des C-modules topologiques et des C-algèbres topologiques'), so E must be taken as a C-algebra; the TeX already has the corrected reading.")
add(91, "first line: E = gr•_{𝔍/𝔍^n}(B/𝔍^n)", "gr with a raised bullet (enlarged crop)",
    r"\gr_{\mathfrak J/\mathfrak J^n} (no superscript)", "formula",
    r"E=\gr_{\mathfrak J/\mathfrak J^n}", r"E=\gr^\bullet_{\mathfrak J/\mathfrak J^n}")
add(91, "first line: '... (B/𝔍^n) muni de la topologie produit'", "muni (enlarged crop)",
    "munie (silently corrected)", "misprint_in_print",
    r"(B/\mathfrak J^n)$ munie", r"(B/\mathfrak J^n)$ muni",
    conf="medium", corrected=r"(B/\mathfrak J^n)$ munie",
    note="The participle refers to 'la A-algèbre topologique E' (feminine); 'munie' is the expected agreement.")
add(91, "Théorème (19.5.3), first sentence: 'On suppose que la A-algèbre C est formellement lisse.'",
    "no 'discrète' (enlarged crop)", "la $A$-algèbre discrète $C$ est formellement lisse", "extra",
    r"$A$-algèbre discrète $C$ est", r"$A$-algèbre $C$ est",
    note="Only Corollaire (19.5.4) has 'discrète'. The proof (19.5.6.1) and Lemme (19.5.6.3) use C formally smooth for its quotient topology ('Comme g est continu ...'), as printed.")
add(91, "Théorème (19.5.3) (i): 'formellement projectif (19.2.1).'", "the reference (19.2.1) is upright",
    "plain text inside the italic theorem environment", "convention",
    r"projectif (19.2.1)", r"projectif \textup{(19.2.1)}", conv=6)
add(91, "Théorème (19.5.3) (ii): 'préadmissible (0_I, 7.1.2), les'", "reference upright, bold 0 (crop)",
    r"($\mathbf 0_{\rm I}$, 7.1.2) inside the italic environment", "convention",
    r"($\mathbf 0_{\rm I}$, 7.1.2)", r"\textup{($\mathbf 0_{\rm I}$, 7.1.2)}", conv=6)
add(91, "Théorème (19.5.3) (ii): 'φ_n (19.5.2) sont des bimorphismes'", "reference upright (crop)",
    "plain text inside the italic theorem environment", "convention",
    r"(19.5.2) sont des", r"\textup{(19.5.2)} sont des", conv=6)
add(91, "Théorème (19.5.3) (ii): 'bimorphismes formels (19.1.2).'", "reference upright (crop)",
    "plain text inside the italic theorem environment", "convention",
    r"formels (19.1.2)", r"formels \textup{(19.1.2)}", conv=6)
add(91, "heading of Corollaire (19.5.4)", "'Corollaire (19.5.4.). —' with a stray full stop after the 4 (enlarged crop)",
    r"\begin{corollary}[19.5.4] prints (19.5.4)", "misprint_in_print",
    r"\begin{corollary}[19.5.4]", r"\begin{corollary}[19.5.4.]",
    corrected=r"\begin{corollary}[19.5.4]",
    note=r"Same treatment as run_I_b p. 185 ((10.4.1.)). The argument also feeds \setmanualcurrentlabel; no \ref to 0.19.5.4-fr exists in the IV1 files.")
add(91, "Corollaire (19.5.4), item label a)", "label 'a)' upright (enlarged crop); b), c) likewise",
    r"\item[a)] inside the italic corollary environment (italic label)", "convention",
    r"\item[a)]", r"\item[\textup{a)}]", conv=6)
add(91, "Corollaire (19.5.4), item label b)", "label 'b)' upright", r"\item[b)] (italic label)", "convention",
    r"\item[b)]", r"\item[\textup{b)}]", conv=6)
add(91, "Corollaire (19.5.4), item label c)", "label 'c)' upright", r"\item[c)] (italic label)", "convention",
    r"\item[c)]", r"\item[\textup{c)}]", conv=6)
add(91, "Corollaire (19.5.4) b), display: 'φ : S•_C(𝔍/𝔍²) → gr•_𝔍(B)' (S)", "S with a raised bullet",
    r"\mathbf S_C^*", "symbol",
    r"\varphi:\mathbf S_C^*(\mathfrak J/\mathfrak J^2)", r"\varphi:\mathbf S_C^\bullet(\mathfrak J/\mathfrak J^2)",
    note="GLOBAL_ISSUES 60: confirmed for §19.")
add(91, "Corollaire (19.5.4) b), display (gr)", "gr with a raised bullet", r"\gr_{\mathfrak J}^*", "symbol",
    r"\longrightarrow\gr_{\mathfrak J}^*(B)", r"\longrightarrow\gr_{\mathfrak J}^\bullet(B)")
add(91, "Corollaire (19.5.4) c): 'de la forme B̂′'", "hat over B only, prime outside the hat (enlarged crop)",
    r"\widehat{B'} (hat over B')", "formula",
    r"forme $\widehat{B'}$", r"forme $\widehat{B}'$",
    note="Same pattern as convention 8, with a hat.")
add(91, "Corollaire (19.5.4) c): 'B′ = S•_C(V)'", "S with a raised bullet", r"\mathbf S_C^*", "symbol",
    r"B'=\mathbf S_C^*(V)", r"B'=\mathbf S_C^\bullet(V)")
add(91, "page break between pp. 91 and 92: '... et que B est une A-algèbre | formellement lisse, f se factorise'",
    "p. 91 ends '... et que B est une A-algèbre'; p. 92 begins 'formellement lisse, f se factorise en B→E′→E′/𝔏, où g est un A-homomorphisme continu.' and continues 'Le diagramme' in the same paragraph (no indent)",
    r"\oldpage[...]{92} stands after 'continu.' with blank lines around it (paragraph break before 'Le diagramme')",
    "marker",
    r"$A$-algèbre formellement¶lisse, $f$ se factorise en $B\xrightarrow{g}E'\to E'/\mathfrak L$, où $g$ est¶un $A$-homomorphisme continu.¶¶",
    r"$A$-algèbre¶" + M92 + r"¶formellement¶lisse, $f$ se factorise en $B\xrightarrow{g}E'\to E'/\mathfrak L$, où $g$ est¶un $A$-homomorphisme continu.¶",
    note=r"Marker move, part 1 of 2 (inserts the marker and drops the blank line at the end of the p. 91 segment); part 2 is the last p. 92 finding (removes the old marker and its blank line, so 'Le diagramme' joins the paragraph). Apply both or neither; part 1 must be applied before part 2, as listed.")

# ---------------- page 92 ----------------
add(92, "first diagram (proof of (19.5.4.1)): left vertical arrow B → E′", "no label on the arrow (enlarged crop)",
    r"\ar[u]^{g}", "extra",
    r"B \ar[u]^{g} \ar[r]_{\theta}", r"B \ar[u] \ar[r]_{\theta}")
add(92, "(19.5.4.2): 'quotient de S•_C(𝔍/𝔍²) par la puissance'", "S with a raised bullet", r"\mathbf S_C^*", "symbol",
    r"quotient de¶$\mathbf S_C^*", r"quotient de¶$\mathbf S_C^\bullet")
add(92, "(19.5.4.2): 'par la puissance (n+1)^e de son idéal d'augmentation'", "(n+1) with a raised e (crop)",
    r"$(n+1)$-ième", "word",
    r"$(n+1)$-ième de¶son", r"$(n+1)$\textsuperscript{e} de¶son",
    note=r"The edition writes ordinals with \textsuperscript{e} elsewhere ($n$\textsuperscript{e}).")
add(92, "(19.5.4.2): 'un homomorphisme de C-algèbres S•_C(𝔍/𝔍²) → E_n'", "S with a raised bullet", r"\mathbf S_C^*",
    "symbol", r"$C$-algèbres¶$\mathbf S_C^*", r"$C$-algèbres¶$\mathbf S_C^\bullet")
add(92, "(19.5.4.2): 'S•_C(𝔍/𝔍²) → E_n qui d'ailleurs (par définition de g)'", "no comma after E_n (crop)",
    "E_n$, qui d'ailleurs", "punctuation",
    r"\to E_n$, qui d'ailleurs", r"\to E_n$ qui d'ailleurs")
add(92, "(19.5.4.2): 's'annule sur la puissance (n+1)^e de l'idéal d'augmentation'", "(n+1) with a raised e (crop)",
    r"$(n+1)$-ième", "word",
    r"$(n+1)$-ième de l'idéal", r"$(n+1)$\textsuperscript{e} de l'idéal")
add(92, "(19.5.4.2): 'de l'idéal d'augmentation de S•_C(𝔍/𝔍²), d'où'", "S with a raised bullet", r"\mathbf S_C^*",
    "symbol", r"d'augmentation de $\mathbf S_C^*", r"d'augmentation de $\mathbf S_C^\bullet")
add(92, "(19.5.4.2): 'le noyau 𝔑 de v est un idéal nilpotent'", "Fraktur N 𝔑 (6x crop; not 𝔎, not ℜ)",
    r"\mathfrak R", "symbol", r"le noyau $\mathfrak R$", r"le noyau $\mathfrak N$")
add(92, "(19.5.4.2): 'E_n s'identifie à F_n/𝔑'", "Fraktur N", r"\mathfrak R", "symbol",
    r"$F_n/\mathfrak R$", r"$F_n/\mathfrak N$")
add(92, "(19.5.4.2): 'w se factorise en B →^{p_n} B/𝔍^n = E_n →^{w′} F_n'",
    "B/𝔍^n (exponent n, crop), although E_n = B/𝔍^{n+1}", r"B/\mathfrak J^n=E_n (printed reading kept)",
    "misprint_in_print", None, None,
    corrected=r"$B\xrightarrow{p_n}B/\mathfrak J^{n+1}=E_n\xrightarrow{w'}F_n$",
    note="E_n is defined as B/𝔍^{n+1} at the start of (19.5.4.2), and w(𝔍^{n+1})=0 is what was just shown.")
add(92, "(19.5.4.2): 'Comme gr•(E_n) est engendré par gr¹(E_n)'", "gr with a raised bullet", r"\gr^*", "symbol",
    r"$\gr^*(E_n)$", r"$\gr^\bullet(E_n)$")
add(92, "end of p. 92's TeX segment: opening of (19.5.4.3)",
    "p. 92 ends '... ce qui achève de montrer que a) entraîne b).'; '(19.5.4.3) Prouvons ensuite' is the first line of p. 93",
    r"\begin{env}[19.5.4.3]\label{0.19.5.4.3-fr} stands before \oldpage[...]{93}", "marker",
    r"\begin{env}[19.5.4.3]¶\label{0.19.5.4.3-fr}¶", "",
    note="Move, part 1 of 2 (the opening moves, not the marker): deletes the opening here; the first p. 93 finding re-inserts it after the p. 93 marker. Apply both or neither.")
add(92, "top of p. 92 (old place of the marker)", "see the last p. 91 finding",
    r"\oldpage[...]{92} with a blank line before 'Le diagramme'", "marker",
    M92 + r"¶¶Le diagramme", r"Le diagramme",
    note="Marker move, part 2 of 2: removes the old marker; apply only together with, and after, the last p. 91 finding (listed last on this page so that the other p. 92 edits still find the page if part 1 fails).")

# ---------------- page 93 ----------------
add(93, "top of p. 93: (19.5.4.3)", "p. 93 begins '(19.5.4.3) Prouvons ensuite que b) entraîne a).'",
    r"\oldpage[...]{93} stands after \begin{env}[19.5.4.3]\label{...} (they lie in the p. 92 segment)", "marker",
    M93 + r"¶Prouvons ensuite", M93 + r"¶\begin{env}[19.5.4.3]¶\label{0.19.5.4.3-fr}¶Prouvons ensuite",
    note="Move, part 2 of 2: re-inserts the opening deleted by the p. 92 finding. Apply both or neither.")
add(93, "(19.5.4.3): 'Soient maintenant G ..., 𝔑 un idéal de carré nul dans G'", "Fraktur N 𝔑 (6x crop; compared with the 𝔎 of p. 56)",
    r"\mathfrak R", "symbol", r"$\mathfrak R$ un¶idéal", r"$\mathfrak N$ un¶idéal",
    note="Fraktur N throughout (19.5.4.2)-(19.5.4.3) (14 occurrences, each a separate finding).")
add(93, "(19.5.4.3): 'f : B → G/𝔑'", "Fraktur N", r"\mathfrak R", "symbol",
    r"$f:B\to G/\mathfrak R$", r"$f:B\to G/\mathfrak N$")
add(93, "(19.5.4.3): 'B → E_n →^{f_n} G/𝔑, où l'on prend n = 2m'", "Fraktur N", r"\mathfrak R", "symbol",
    r"G/\mathfrak R$, où l'on prend", r"G/\mathfrak N$, où l'on prend")
add(93, "(19.5.4.3): 'r : C → F_n ⥲ E_n →^{f_n} G/𝔑' (arrow v)", "isomorphism arrow: v above a tilde above the arrow (crop)",
    r"\xrightarrow{v}", "formula",
    r"$r:C\to F_n\xrightarrow{v}", r"$r:C\to F_n\xrightarrow{\overset{v}{\sim}}")
add(93, "(19.5.4.3): 'r : C → ... → G/𝔑, et comme C'", "Fraktur N", r"\mathfrak R", "symbol",
    r"G/\mathfrak R$, et comme", r"G/\mathfrak N$, et comme")
add(93, "(19.5.4.3): 'r se factorise en C →^{r′} G →^θ G/𝔑' (second arrow)", "θ over the second arrow (crop)",
    r"G\to G/\mathfrak R (no label)", "formula",
    r"$C\xrightarrow{r'}G\to G", r"$C\xrightarrow{r'}G\xrightarrow{\theta}G")
add(93, "(19.5.4.3): '... G/𝔑, de sorte que G est muni'", "Fraktur N", r"\mathfrak R", "symbol",
    r"/\mathfrak R$, de sorte que", r"/\mathfrak N$, de sorte que")
add(93, "(19.5.4.3): 'd'une structure de C-algèbre.'", "'algèbre' in italics (crop)", "upright", "italics",
    r"structure de $C$-algèbre", r"structure de $C$-\emph{algèbre}")
add(93, "(19.5.4.3): 'f′_n : F_n ⥲ E_n →^{f_n} G/𝔑' (arrow v)", "isomorphism arrow: v above a tilde above the arrow (crop)",
    r"\xrightarrow{v}", "formula",
    r"$f'_n:F_n\xrightarrow{v}", r"$f'_n:F_n\xrightarrow{\overset{v}{\sim}}")
add(93, "(19.5.4.3): 'f′_n : ... G/𝔑 est une application C-linéaire'", "Fraktur N", r"\mathfrak R", "symbol",
    r"G/\mathfrak R$ est une application", r"G/\mathfrak N$ est une application")
add(93, "(19.5.4.3): 'g : 𝔍/𝔍² → G/𝔑. Puisque'", "Fraktur N", r"\mathfrak R", "symbol",
    r"\to G/\mathfrak R$. Puisque", r"\to G/\mathfrak N$. Puisque")
add(93, "(19.5.4.3): '𝔍/𝔍² →^h G → G/𝔑, où h'", "Fraktur N", r"\mathfrak R", "symbol",
    r"G\to G/\mathfrak R$, où $h$", r"G\to G/\mathfrak N$, où $h$")
add(93, "(19.5.4.3): 'w : S•_C(𝔍/𝔍²) → G'", "S with a raised bullet", r"\mathbf S_C^*", "symbol",
    r"$w:\mathbf S_C^*", r"$w:\mathbf S_C^\bullet")
add(93, "(19.5.4.3): 'un élément de 𝔑, donc tout élément de degré n = 2m'", "Fraktur N", r"\mathfrak R", "symbol",
    r"$\mathfrak R$, donc tout", r"$\mathfrak N$, donc tout")
add(93, "(19.5.4.3): 'puisque 𝔑² = 0'", "Fraktur N", r"\mathfrak R", "symbol",
    r"$\mathfrak R^2=0$", r"$\mathfrak N^2=0$")
add(93, "(19.5.4.3): 'w se factorise en S•_C(𝔍/𝔍²) → F_n →^{w′} G'", "S with a raised bullet", r"\mathbf S_C^*",
    "symbol", r"$\mathbf S_C^*(\mathfrak J/\mathfrak J^2)\to F_n", r"$\mathbf S_C^\bullet(\mathfrak J/\mathfrak J^2)\to F_n")
add(93, "(19.5.4.3): 'le composé F_n →^{w′} G →^θ G/𝔑 coïncide'", "Fraktur N", r"\mathfrak R", "symbol",
    r"\xrightarrow{\theta}G/\mathfrak R$¶coïncide", r"\xrightarrow{\theta}G/\mathfrak N$¶coïncide")
add(93, "(19.5.4.3): 'Finalement, le composé B → E_n →^{v^{-1}} F_n →^{w′} G →^θ G/𝔑 étant égal à f'",
    "displayed formula (own centred line); θ over the last arrow; Fraktur N (crop)",
    r"inline $...$, last arrow \to without θ, \mathfrak R", "formula",
    r"le composé¶$B\to E_n\xrightarrow{v^{-1}}F_n\xrightarrow{w'}G\to G/\mathfrak R$ étant¶égal",
    r"le composé¶\[¶  B\to E_n\xrightarrow{v^{-1}}F_n\xrightarrow{w'}G\xrightarrow{\theta}G/\mathfrak N¶\]¶étant¶égal",
    note="One edit for three differences in one formula: display (inline in the TeX), missing θ, 𝔑 for \\mathfrak R. 'étant égal' continues the paragraph after the display (not indented).")
add(93, "(19.5.4.4): 'et finalement B̂′ est une Â-algèbre'", "hat over B only, prime outside (crop)",
    r"\widehat{B'}", "formula",
    r"finalement $\widehat{B'}$", r"finalement $\widehat{B}'$",
    note="Same pattern as convention 8, with a hat.")
add(93, "(19.5.4.4): 'v_n : S•_C(𝔍/𝔍²) = B′ → B/𝔍^{n+1}'", "S with a raised bullet", r"\mathbf S_C^*", "symbol",
    r"$v_n:\mathbf S_C^*", r"$v_n:\mathbf S_C^\bullet")
add(93, "end of p. 93: '... v_n est bijectif pour | tout n (Bourbaki' (page break mid-sentence)",
    "one paragraph across the page break", r"blank line after 'pour' (and after the p. 94 marker): paragraph break",
    "other", r"\emph{bijectif} pour¶¶", r"\emph{bijectif} pour¶",
    note="Part 1 of 2 (GLOBAL_ISSUES 20); the first p. 94 finding removes the blank line after the marker. Both are needed to remove the paragraph break.")

# ---------------- page 94 ----------------
add(94, "top of p. 94: 'tout n (Bourbaki, ...' continues the sentence of p. 93", "no new paragraph",
    "blank line after the marker", "other",
    M94 + r"¶¶tout $n$", M94 + r"¶tout $n$",
    note="Part 2 of 2 (see the last p. 93 finding).")
add(94, "Remarque (19.5.5): 'de sorte que C = B/𝔍 est un corps'", "'est un corps' (crop)", "soit un corps", "word",
    r"$C=B/\mathfrak J$ soit un corps", r"$C=B/\mathfrak J$ est un corps")
add(94, "Remarque (19.5.5): 'En effet, 𝔍/𝔍² étant ici un C-module libre'", "new indented paragraph after condition d)",
    r"no blank line after \end{enumerate}: continues the paragraph unindented", "other",
    r"\end{enumerate}¶En effet,", r"\end{enumerate}¶¶En effet,")
add(94, "Remarque (19.5.5): 'φ : S•_C(𝔍/𝔍²) → gr•_𝔍(B)' (S)", "S with a raised bullet", r"\mathbf S_C^*", "symbol",
    r"$\varphi:\mathbf S_C^*", r"$\varphi:\mathbf S_C^\bullet")
add(94, "Remarque (19.5.5): 'φ : ... → gr•_𝔍(B) est bijectif' (gr)", "gr with a raised bullet", r"\gr_{\mathfrak J}^*",
    "symbol", r"\gr_{\mathfrak J}^*(B)$", r"\gr_{\mathfrak J}^\bullet(B)$")
add(94, "Remarque (19.5.5): 'Or ici S•_C(𝔍/𝔍²) s'identifie'", "S with a raised bullet", r"\mathbf S_C^*", "symbol",
    r"Or ici $\mathbf S_C^*", r"Or ici $\mathbf S_C^\bullet")
add(94, "Remarque (19.5.5): 'formellement lisse entraîne comme dans (19.5.4.2) l'existence'", "no commas (crop)",
    "entraîne, comme dans (19.5.4.2), l'existence", "punctuation",
    r"entraîne, comme dans (19.5.4.2), l'existence", r"entraîne comme dans (19.5.4.2) l'existence")
add(94, "(19.5.6): 'Les C-modules ((𝔟_α∩𝔍^n)+𝔍^{n+1})/𝔍^{n+1}'", "new indented paragraph after the display",
    r"no blank line after \]", "other",
    r"\]¶Les $C$-modules", r"\]¶¶Les $C$-modules")
add(94, "heading of (19.5.6.1)", "'(19.5.6.1) Démonstration de (19.5.3, (i)). — Soient P, Q deux C_α-modules discrets' ('Démonstration de' italic; crop)",
    "the title 'Démonstration de (19.5.3, (i)). —' is missing", "missing",
    r"\label{0.19.5.6.1-fr}¶Soient $P$", r"\label{0.19.5.6.1-fr}¶\emph{Démonstration de} (19.5.3, (i)). --- Soient $P$",
    note="Written like the title of (19.5.6) in the TeX ('\\emph{Démonstration du théorème} (19.5.3). ---').")
add(94, "(19.5.6.1): 'passant au quotient, on déduit de v un C_α-homomorphisme de modules discrets'",
    "'on déduit de v un' (crop)", "on en déduit un", "word",
    r"on en déduit un $C_\alpha$", r"on déduit de $v$ un $C_\alpha$")
add(94, "(19.5.6.1): '(tel que le composé C_β →^{g′} E_α → C_α soit'", "g′ over the first arrow (crop)",
    r"C_\beta\to E_\alpha (no label)", "formula",
    r"le composé $C_\beta\to E_\alpha", r"le composé $C_\beta\xrightarrow{g'}E_\alpha")
add(94, "page break between pp. 94 and 95: '... définit canoniquement un | homomorphisme surjectif D_{C_β}(P)'",
    "p. 94 ends '... l'homomorphisme surjectif u : P→Q définit canoniquement un'; p. 95 begins 'homomorphisme surjectif D_{C_β}(P)→D_{C_β}(Q) (18.2.9)'",
    r"\oldpage[...]{95} stands after the end of (19.5.6.1), before (19.5.6.2) (the rest of (19.5.6.1), printed on p. 95, lies in the p. 94 segment; it agrees with the print)",
    "marker",
    r"définit canoniquement un homomorphisme surjectif",
    r"définit canoniquement un¶" + M95 + r"¶homomorphisme surjectif",
    note="Marker move, part 1 of 2 (insert here); the last p. 95 finding removes the old marker. Apply both or neither, in the listed order. The moved text needs no other edit.")

# ---------------- page 95 ----------------
add(95, "(19.5.6.2): 'les idéaux (b_α + 𝔍^{n+1})/𝔍^{n+1} forment'", "italic roman b_α, not the Fraktur 𝔟_α of the next display (enlarged crop)",
    r"\mathfrak b_\alpha (silently corrected)", "misprint_in_print",
    r"les idéaux $(\mathfrak b_\alpha", r"les idéaux $(b_\alpha",
    corrected=r"les idéaux $(\mathfrak b_\alpha",
    note="Wrong-font letter (cf. GLOBAL_ISSUES 29).")
add(95, "(19.5.6.2): 'De même, dans gr^n_𝔍(B) = 𝔍^n/𝔍^{n+1}' (small print)", "'gr' in bold (4x crop: much heavier than the text and than B, C)",
    r"\gr (light roman)", "font",
    r"$\gr_{\mathfrak J}^n(B)=", r"$\mathbf{gr}_{\mathfrak J}^n(B)=", conf="medium",
    note="In the small print of p. 95 'gr' is bold three times; on pp. 91-94 (normal size) it is light. Check the small print of pp. 96 ff. before deciding globally.")
add(95, "(19.5.6.2): 'l'algèbre symétrique S•_{C_α}(𝔍_α/𝔍_α²)'", "S with a raised bullet", r"\mathbf S_{C_\alpha}^*",
    "symbol", r"symétrique¶$\mathbf S_{C_\alpha}^*", r"symétrique¶$\mathbf S_{C_\alpha}^\bullet")
add(95, "(19.5.6.2): 'F_{α,n} le quotient de S•_{C_α}(𝔍_α/𝔍_α²)'", "S with a raised bullet", r"\mathbf S_{C_\alpha}^*",
    "symbol", r"le quotient de¶$\mathbf S_{C_\alpha}^*", r"le quotient de¶$\mathbf S_{C_\alpha}^\bullet")
add(95, "(19.5.6.2): 'par la puissance (n+1)^e de son idéal d'augmentation'", "(n+1) with a raised e", r"$(n+1)$-ième",
    "word", r"$(n+1)$-ième de son", r"$(n+1)$\textsuperscript{e} de son")
add(95, "Lemme (19.5.6.3) (i): 'un A-homomorphisme surjectif d'algèbres :' before the display", "colon (crop)",
    "no colon", "punctuation",
    r"surjectif d'algèbres¶  \[", r"surjectif d'algèbres~:¶  \[")
add(95, "Lemme (19.5.6.3) (i): 'tel que gr⁰(v_αβ) : C_β → C_α'", "'gr' bold (crop)", r"\gr", "font",
    r"$\gr^0(v_{\alpha\beta})", r"$\mathbf{gr}^0(v_{\alpha\beta})", conf="medium")
add(95, "Lemme (19.5.6.3) (i): 'et gr¹(v_αβ) : 𝔍_β/𝔍_β² → 𝔍_α/𝔍_α²'", "'gr' bold (crop)", r"\gr", "font",
    r"$\gr^1(v_{\alpha\beta})", r"$\mathbf{gr}^1(v_{\alpha\beta})", conf="medium")
add(95, "proof of Lemme (19.5.6.3), after the diagram (19.5.6.4)",
    "the proof begins '(i) Dans la A-algèbre topologique discrète E_{α,n}' with no number; (19.5.6.4) is only the number of the diagram",
    r"\begin{env}[19.5.6.4] prints a bold heading '(19.5.6.4)' before the proof", "extra",
    r"\begin{env}[19.5.6.4]¶\label{0.19.5.6.4-proof-fr}¶", r"\label{0.19.5.6.4-proof-fr}¶",
    note=r"Apply both or neither with the p. 96 finding below, which removes the matching end of the env, just before the page-97 marker; either alone breaks compilation. The label is kept (unreferenced).")
add(95, "end of p. 95: '... → E_{α,n}/(𝔍_α/𝔍_α^{n+1}); | comme C est une A-algèbre' (page break mid-sentence)",
    "one paragraph across the page break", "blank line before the p. 96 marker (and after it): paragraph break",
    "other", r"^{n+1})$~;¶¶", r"^{n+1})$~;¶",
    note="Part 1 of 2 (GLOBAL_ISSUES 20): the blank line after \\oldpage[...]{96} lies in the p. 96 segment (for the p. 96 checker).")
add(95, "old place of the p. 95 marker, before (19.5.6.2)", "see the last p. 94 finding",
    r"\oldpage[...]{95} before \begin{env}[19.5.6.2]", "marker",
    M95 + r"¶¶\begin{env}[19.5.6.2]", r"\begin{env}[19.5.6.2]",
    note="Marker move, part 2 of 2: apply only together with, and after, the last p. 94 finding (listed last on this page so that the other p. 95 edits still find the page if part 1 fails).")
add(96, "end of the proof of Lemme (19.5.6.3) (printed p. 96): matching \\end{env}", "no heading, nothing printed",
    r"\end{enumerate}\end{env} closing the env opened as [19.5.6.4]", "extra",
    r"\end{enumerate}¶\end{env}", r"\end{enumerate}",
    note="OUTSIDE pages 91-95: 'old' lies in the p. 96 segment of ega0-19-fr.tex (just before the page-97 marker; checked unique there; there is no page_096.tex in this run folder). Apply only together with the p. 95 finding that removes \\begin{env}[19.5.6.4].")

# ---------------- checks ----------------
pages = {}
for p in range(91, 96):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[" + re.escape(PART) + r"\]\{(\d+)\}")


def seg_of(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    return None, None


s96, e96 = seg_of(rel, 96)
pages[96] = rel[s96:e96]
ok = True
spans = {}
for k, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    t = pages[x["page"]]
    c = t.count(fx["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", k, x["page"], c, repr(fx["old"][:80]))
    else:
        a = t.index(fx["old"])
        spans.setdefault(x["page"], []).append((a, a + len(fx["old"]), k))
for p, sp in spans.items():
    sp.sort()
    for (a1, b1, k1), (a2, b2, k2) in zip(sp, sp[1:]):
        if a2 < b1:
            ok = False
            print("OVERLAP on page", p, k1, k2)
# simulate apply_fixes.py in file order on the release file
t = rel
for k, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    s, e = seg_of(t, int(x["page"]))
    if s is None:
        ok = False
        print("SIM page not found", k, x["page"])
        continue
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        ok = False
        print("SIM count", seg.count(fx["old"]), k, x["page"], repr(fx["old"][:60]))
        continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("all checks ok" if ok else "PROBLEMS")
cnt = {}
for x in F:
    c = cnt.setdefault(x["page"], [0, 0, 0])
    c[1 if x["kind"] == "convention" else 2 if x["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/convention/misprint):", cnt)
markers = [(int(m.group(1)), t.count("\n", 0, m.start()) + 1) for m in marker.finditer(t)]
print("markers after simulation:", [m for m in markers if 89 <= m[0] <= 98])
(RUN / "crops_091_095" / "simulated_ega0-19-fr.tex").write_text(t, encoding="utf-8", newline="")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", OUT, len(F), "findings")
