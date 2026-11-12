"""Build findings_081_085.json and check every fix: "old" once in its page_NNN.tex (LF), and a dry
simulation of apply_fixes.py (same page-segment logic) on an in-memory copy of ega0-19-fr.tex."""
import json
import pathlib
import re

E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_0IV1"
OUT = RUN / "findings_081_085.json"
SRC = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4\ega0-19-fr.tex"
MK = r"\oldpage[0\textsubscript{IV-1}]"


def s(x):
    """'¶' stands for a line break."""
    return None if x is None else x.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else {"old": s(old), "new": s(new)})
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


K_NOTE = ("Fraktur K (𝔎) misread as R: the printed glyph is the 𝔎 of 𝔎_{H,μ,n} (p. 80, TeX \\mathfrak K) and of "
          "(18.1.7.1), clearly different from the Fraktur R of 0_I p. 12 (radical ℜ(A)).")
L_NOTE = ("Fraktur L (𝔏) misread as Q: same glyph as the 𝔏 of E/𝔏 on p. 81 (TeX \\mathfrak L).")

# ---------------------------------------------------------------- p. 81 (marker move: text in p. 80's segment)
add(80, "top of p. 81: Lemme (19.3.4.1)(ii), item label (the line stands in p. 80's segment)",
    "label (ii) upright in the italic lemma",
    r"\item[(ii)] inside the italic lemma environment: label italic",
    "convention", r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement",
    "OUTSIDE MY PAGE SEGMENT (page_080.tex): (ii) of the lemma is printed at the top of p. 81. Apply before the "
    "marker insertion below, while the line is still in p. 80's segment.", conv=6)
add(80, r"page marker \oldpage[0\textsubscript{IV-1}]{81}, new place: before Lemme (19.3.4.1)(ii) 'Inversement, soient H une partie finie de I'",
    "p. 80 ends with (i) '... f(T_α) est nilpotent dans E pour tout α∈H.'; p. 81 begins '(ii) Inversement, soient H une partie finie de I, (z_α)_{α∈H} ...'",
    "the p. 81 marker stands after \\end{lemma}, before the proof '(i) résulte aussitôt'",
    "marker", r"$\alpha\in H$.¶  \item", r"$\alpha\in H$.¶" + MK + r"{81}¶  \item",
    "OUTSIDE MY PAGE SEGMENT (page_080.tex). Move, part 1 of 2: insert here; the next finding removes the old marker. "
    "The p. 76-80 checker may report the same move: apply one insertion only. I checked the lemma's (ii) "
    "(page_080.tex lines 89-93) against the p. 81 scan: only the label differs (previous finding).")
add(81, r"page marker \oldpage[0\textsubscript{IV-1}]{81}, old place: before the proof of (19.3.4.1)",
    "the proof '(i) résulte aussitôt' follows the lemma's (ii) on p. 81",
    r"\oldpage[0\textsubscript{IV-1}]{81} between \end{lemma} and \begin{proof}",
    "marker", MK + r"{81}¶¶\begin{proof}¶(i) résulte", r"\begin{proof}¶(i) résulte",
    "Move, part 2 of 2: removes the old marker (either order with the insertion).")
add(81, "proof of (19.3.4.1)(ii): 'sa continuité résulte de l'hypothèse que les f(T_α) pour α∈H sont nilpotents, car si (f(T_α))^n=0 pour tout α∈H'",
    "f(T_α) and (f(T_α))^n (checked on the strip)",
    r"keeps the print: les $f(T_\alpha)$ ... $(f(T_\alpha))^n=0$",
    "misprint_in_print", None, None,
    "The TeX keeps the printed reading. In (ii) the hypothesis is that the z_α = g(T_α) are nilpotent; f is the map "
    "of part (i). Correct reading g(T_α) (or z_α) in both places.", conf="medium",
    corrected=r"les $g(T_\alpha)$ pour $\alpha\in H$ sont nilpotents, car si $(g(T_\alpha))^n=0$")
add(81, "before 'Ce lemme étant établi, et les notations C et 𝔍 ayant le même sens que dans (19.3.1)'",
    "a new paragraph without any heading",
    r"\begin{proof}[Démonstration de la proposition~{\rm(19.3.4)}]: the proof environment takes no optional argument, so the bracket text is typeset",
    "extra", r"\begin{proof}[Démonstration de la proposition~{\rm(19.3.4)}]", r"\begin{proof}",
    "As on p. 34 (GLOBAL_ISSUES 58). The 'Démonstration. —' that the environment still prints is the document-wide item.")
for lab, old in (("i", r"\item[(i)] $A$ est une"), ("ii", r"\item[(ii)] Si $B$"), ("iii", r"\item[(iii)] Soient $B$"),
                 ("iv", r"\item[(iv)] Soient $B$"), ("v", r"\item[(v)] Soient")):
    add(81, f"Proposition (19.3.5)({lab}), item label", f"label ({lab}) upright (enlarged crop)",
        rf"\item[({lab})] inside the italic proposition: label italic",
        "convention", old, old.replace(f"[({lab})]", r"[\textup{(" + lab + ")}]"), "GLOBAL_ISSUES 16.", conv=6)
add(81, "Proposition (19.3.5)(iii): 'B⊗_A A' (0_I, 7.7.5 et 7.7.6) est formellement lisse'",
    "the reference, 'et' included, upright in the italic statement (enlarged crop)", "italic (statement environment)",
    "convention", r"($\mathbf 0_{\rm I}$, 7.7.5 et 7.7.6)", r"\textup{($\mathbf 0_{\rm I}$, 7.7.5 et 7.7.6)}", "", conv=6)
add(81, "Proposition (19.3.5)(iv): 'S (resp. T) une partie multiplicative'", "'(resp. T)' upright (enlarged crop)",
    "italic (statement environment)", "convention", r"$S$ (resp. $T$)", r"$S$ \textup{(resp. $T$)}", "", conv=6)
add(81, "Proposition (19.3.5)(iv): 'une partie multiplicative de A (resp. B)'", "'(resp. B)' upright (enlarged crop)",
    "italic (statement environment)", "convention", r"de $A$ (resp. $B$)", r"de $A$ \textup{(resp. $B$)}", "", conv=6)
add(81, "Proposition (19.3.5)(v): 'Soient B_i (1≤i≤n) des A-algèbres topologiques'",
    "parentheses of (1≤i≤n) upright (enlarged crop)", "italic text parentheses", "convention",
    r"$B_i$ ($1\leq i\leq n$)", r"$B_i$ \textup{($1\leq i\leq n$)}", "As on pp. 7, 10, 17, 18.", conv=6)

# ---------------------------------------------------------------- p. 82
add(82, r"page marker \oldpage[0\textsubscript{IV-1}]{82}, new place: proof of (19.3.5)(ii), 'pour lesquelles E/𝔏 est | encore l'algèbre quotient (discrète)'",
    "p. 81 ends '... des structures de B-algèbre topologique, pour lesquelles E/𝔏 est'; p. 82 begins 'encore l'algèbre quotient (discrète) de la B-algèbre E.'",
    "the p. 82 marker stands before the proof of (19.3.5), whose (i) and the start of (ii) are printed on p. 81",
    "marker", r"$E/\mathfrak L$ est encore", r"$E/\mathfrak L$ est¶" + MK + r"{82}¶encore",
    "Move, part 1 of 2: insert first, then remove the old marker (next finding); with the old marker removed first, "
    "p. 82 cannot be located. I checked page_082.tex lines 4-26 (printed on p. 81) against the p. 81 scan: no other difference.")
add(82, r"page marker \oldpage[0\textsubscript{IV-1}]{82}, old place: before \begin{proof} of (19.3.5)",
    "this proof begins on p. 81", "marker before \\begin{proof}", "marker",
    MK + r"{82}¶¶\begin{proof}¶\begin{enumerate}", r"\begin{proof}¶\begin{enumerate}",
    "Move, part 2 of 2: after the insertion above.")
add(82, "proof of (19.3.5)(iii): 'où v est un A-homomorphisme continu (pour la structure de A-algèbre topologique sur C définie par le composé A → A' →^w C des homomorphismes canoniques). L'égalité'",
    "the parenthesis '(pour la structure de A-algèbre topologique sur C définie par le composé A → A' →^w C des homomorphismes canoniques)' after 'continu'",
    "'continu. L'égalité des composés': the parenthesis is missing", "missing",
    r"continu. L'égalité des composés",
    r"continu (pour la structure de $A$-algèbre¶  topologique sur $C$ définie par le composé $A\to A'\xrightarrow{w}C$ des¶  homomorphismes canoniques). L'égalité des composés")
add(82, "proof of (19.3.5)(iv): 'formé des S^{-1}𝔍 (resp. T^{-1}𝔎), où 𝔍 (resp. 𝔎) parcourt'",
    "Fraktur K (𝔎) twice (enlarged crop)", r"$T^{-1}\mathfrak R$, $\mathfrak R$", "symbol",
    r"(resp. $T^{-1}\mathfrak R$), où¶  $\mathfrak J$ (resp. $\mathfrak R$) parcourt",
    r"(resp. $T^{-1}\mathfrak K$), où¶  $\mathfrak J$ (resp. $\mathfrak K$) parcourt", K_NOTE)
add(82, "proof of (19.3.5)(iv): 'déduit de α (et dont l'existence résulte de ce que α(S)⊂T par hypothèse) est continu (0_I, 7.6.6). Soient alors'",
    "the parenthesis '(et dont l'existence résulte de ce que α(S)⊂T par hypothèse)' and the reference '(0_I, 7.6.6)' (bold 0)",
    "'déduit de $\\alpha$ est continu. Soient alors': both missing", "missing",
    r"$\alpha$ est continu. Soient alors",
    r"$\alpha$ (et dont l'existence résulte de ce que $\alpha(S)\subset T$ par¶  hypothèse) est continu ($\mathbf 0_{\rm I}$, 7.6.6). Soient alors")
add(82, "proof of (19.3.5)(iv): 'alors le composé B →^ψ T^{-1}B →^u C/𝔍 est un A-homomorphisme'",
    "ψ over the first arrow (enlarged crop)", r"$B\to T^{-1}B\xrightarrow{u}C/\mathfrak J$: no ψ", "formula",
    r"le composé $B\to T^{-1}B\xrightarrow{u}C/\mathfrak J$", r"le composé $B\xrightarrow{\psi}T^{-1}B\xrightarrow{u}C/\mathfrak J$")
add(82, "proof of (19.3.5)(iv): 'et par suite v se factorise en B →^ψ T^{-1}B →^w C'",
    "ψ over the first arrow (enlarged crop)", r"$B\to T^{-1}B\xrightarrow{w}C$: no ψ", "formula",
    r"$B\to T^{-1}B\xrightarrow{w}C$~;", r"$B\xrightarrow{\psi}T^{-1}B\xrightarrow{w}C$~;")
add(82, "proof of (19.3.5)(iv): 'car le composé A →^α B →^ψ T^{-1}B →^w C est égal à'",
    "α and ψ over the first two arrows (enlarged crop)", r"$A\to B\to T^{-1}B\xrightarrow{w}C$: no labels", "formula",
    r"$A\to B\to T^{-1}B\xrightarrow{w}C$", r"$A\xrightarrow{\alpha}B\xrightarrow{\psi}T^{-1}B\xrightarrow{w}C$")
add(82, "proof of (19.3.5)(iv), display 'A →^φ S^{-1}A →^{α'} T^{-1}B →^w C,'",
    "φ over the first arrow (enlarged crop)", r"A\to S^{-1}A: no φ", "formula",
    r"A\to S^{-1}A\xrightarrow{\alpha'}", r"A\xrightarrow{\varphi}S^{-1}A\xrightarrow{\alpha'}")
add(82, "proof of (19.3.5)(iv): 'les homomorphismes composés B →^ψ T^{-1}B →^w C → C/𝔍 et'",
    "ψ over the first arrow (enlarged crop)", "no ψ", "formula",
    r"$B\to T^{-1}B\xrightarrow{w}C\to C/\mathfrak J$", r"$B\xrightarrow{\psi}T^{-1}B\xrightarrow{w}C\to C/\mathfrak J$")
add(82, "proof of (19.3.5)(iv): 'et B →^ψ T^{-1}B →^u C/𝔍 étant égaux'",
    "ψ over the first arrow (enlarged crop)", "no ψ", "formula",
    r"$B\to T^{-1}B\xrightarrow{u}C/\mathfrak J$ étant", r"$B\xrightarrow{\psi}T^{-1}B\xrightarrow{u}C/\mathfrak J$ étant")
add(82, "proof of (19.3.5), last paragraph: 'Enfin, (v) est immédiat'",
    "the paragraph begins 'Enfin, (v) est immédiat', without a label",
    r"\item[(v)] Enfin, (v) est immédiat: an extra label (v)", "extra",
    r"\item[(v)] Enfin,", r"\item[] Enfin,", "An empty label keeps the list.")
add(82, r"page marker \oldpage[0\textsubscript{IV-1}]{83}, new place: proof of (19.3.5)(v), '... continus B_i→C | (resp. B_i→C/𝔍) et tout'",
    "p. 82 ends '... de n A-homomorphismes continus B_i→C'; p. 83 begins '(resp. B_i→C/𝔍) et tout A-homomorphisme continu'",
    "the p. 83 marker stands after \\end{proof}; the end of (v) is printed on p. 83",
    "marker", r"continus $B_i\to C$¶  (resp. $B_i\to C/\mathfrak J$)",
    r"continus $B_i\to C$¶" + MK + r"{83}¶  (resp. $B_i\to C/\mathfrak J$)",
    "Insertion of the p. 83 marker (in p. 82's segment); part 1 of 2, the first p. 83 finding removes the old marker. "
    "I checked page_082.tex lines 91-94 (printed on p. 83) against the p. 83 scan: no other difference.")

# ---------------------------------------------------------------- p. 83
add(83, r"page marker \oldpage[0\textsubscript{IV-1}]{83}, old place: before Proposition (19.3.6)",
    "p. 83 begins with the end of (19.3.5)(v)", r"marker before \begin{proposition}[19.3.6]", "marker",
    MK + r"{83}¶¶\begin{proposition}[19.3.6]", r"\begin{proposition}[19.3.6]",
    "Part 2 of 2 of the p. 83 marker move (either order with the insertion).")
for lab in ("a", "b", "c"):
    add(83, f"Proposition (19.3.6), item label {lab})", f"label {lab}) upright (enlarged crop)",
        rf"\item[{lab})] inside the italic proposition: label italic", "convention",
        rf"\item[{lab})]", r"\item[\textup{" + lab + ")}]", "", conv=6)
add(83, "Corollaire (19.3.7): 'Sous les hypothèses de (19.3.5, (iv)), la A{S^{-1}}-algèbre'",
    "'(19.3.5, (iv))', upright in the italic statement (enlarged crop)", "'(19.3.5), (iv),' (italic)",
    "punctuation", r"(19.3.5), (iv), la", r"\textup{(19.3.5, (iv))}, la",
    "One edit: the printed bracketing and the upright reference (convention 6) in the same parenthesis.")
add(83, "after (19.3.7): 'et de (19.3.5, (iv)) et (19.3.6)'", "'(19.3.5, (iv))'", "'(19.3.5), (iv)'",
    "punctuation", r"(19.3.5), (iv) et", r"(19.3.5, (iv)) et")
add(83, "Proposition (19.3.8): 'pour tout idéal ouvert 𝔎 de B, 𝔎² soit aussi ouvert'", "Fraktur K twice (enlarged crop)",
    r"\mathfrak R", "symbol", r"ouvert $\mathfrak R$ de $B$, $\mathfrak R^2$ soit",
    r"ouvert $\mathfrak K$ de $B$, $\mathfrak K^2$ soit", K_NOTE)
add(83, "proof of (19.3.8.1): 'En effet, 𝔎 = u^{-1}(𝔍)'", "Fraktur K (enlarged crop)", r"\mathfrak R", "symbol",
    r"$\mathfrak R=u^{-1}(\mathfrak J)$", r"$\mathfrak K=u^{-1}(\mathfrak J)$", K_NOTE)
add(83, "proof of (19.3.8.1): '𝔎^n est contenu dans Ker(u)'", "Fraktur K", r"\mathfrak R", "symbol",
    r"$\mathfrak R^n$ est contenu", r"$\mathfrak K^n$ est contenu", K_NOTE)
add(83, "proof of (19.3.8.1): 'que 𝔎^{2^h} est ouvert, donc aussi 𝔎^n pour tout n'", "Fraktur K twice", r"\mathfrak R",
    "symbol", r"$\mathfrak R^{2^h}$ est ouvert, donc aussi¶$\mathfrak R^n$ pour tout",
    r"$\mathfrak K^{2^h}$ est ouvert, donc aussi¶$\mathfrak K^n$ pour tout", K_NOTE)
add(83, "after (19.3.8.1): 'la topologie de B est borne supérieure des topologies'", "'borne supérieure' italic",
    "roman", "italics", r"est borne¶supérieure des", r"est \emph{borne¶supérieure} des")
add(83, "after (19.3.8.1): 'des topologies 𝔎-préadiques, où 𝔎 parcourt'", "Fraktur K twice", r"\mathfrak R",
    "symbol", r"$\mathfrak R$-préadiques, où $\mathfrak R$ parcourt",
    r"$\mathfrak K$-préadiques, où $\mathfrak K$ parcourt", K_NOTE)
add(83, "after (19.3.8.1): 'Si B est un anneau préadique (0_I, 7.1.9)'", "'préadique' italic", "roman",
    "italics", r"un anneau préadique", r"un anneau \emph{préadique}")

# ---------------------------------------------------------------- p. 84
add(84, "proof of (19.3.10): 'Soit (𝔏_n) une suite décroissante d'idéaux de C'",
    "Fraktur L (enlarged crop, same glyph as E/𝔏 on p. 81)", r"\mathfrak Q_n", "symbol",
    r"Soit $(\mathfrak Q_n)$", r"Soit $(\mathfrak L_n)$", L_NOTE)
add(84, "proof of (19.3.10): 'la A-algèbre discrète C/𝔏_n et l'idéal (𝔍+𝔏_n)/𝔏_n de cette algèbre'",
    "Fraktur L three times", r"\mathfrak Q", "symbol",
    r"discrète $C/\mathfrak Q_n$ et l'idéal¶$(\mathfrak J+\mathfrak Q_n)/\mathfrak Q_n$ de cette",
    r"discrète $C/\mathfrak L_n$ et l'idéal¶$(\mathfrak J+\mathfrak L_n)/\mathfrak L_n$ de cette", L_NOTE)
add(84, "proof of (19.3.10): 'comme il existe k tel que 𝔍^k⊂𝔏_n, (𝔍+𝔏_n)/𝔏_n est nilpotent'",
    "Fraktur L three times", r"\mathfrak Q", "symbol",
    r"$\mathfrak J^k\subset\mathfrak Q_n$,¶$(\mathfrak J+\mathfrak Q_n)/\mathfrak Q_n$ est nilpotent",
    r"$\mathfrak J^k\subset\mathfrak L_n$,¶$(\mathfrak J+\mathfrak L_n)/\mathfrak L_n$ est nilpotent", L_NOTE)
add(84, "proof of (19.3.10): 'soit u_n l'homomorphisme continu B →^u C/𝔍 → C/(𝔍+𝔏_n) = (C/𝔏_n)/((𝔍+𝔏_n)/𝔏_n); par hypothèse'",
    "set inline in the running text; Fraktur L", r"a displayed formula \[...\] with \mathfrak Q", "other",
    r"continu¶\[¶  B\xrightarrow{u}C/\mathfrak J\to C/(\mathfrak J+\mathfrak Q_n)¶  =(C/\mathfrak Q_n)/((\mathfrak J+\mathfrak Q_n)/\mathfrak Q_n)~;¶\]¶par hypothèse",
    r"continu¶$B\xrightarrow{u}C/\mathfrak J\to C/(\mathfrak J+\mathfrak L_n)¶=(C/\mathfrak L_n)/((\mathfrak J+\mathfrak L_n)/\mathfrak L_n)$~;¶par hypothèse",
    "One edit: inline as printed (GLOBAL_ISSUES 21) and the four 𝔏 for \\mathfrak Q (letter finding, see the note on (𝔏_n)).")
add(84, "proof of (19.3.10): 'par hypothèse u_n se factorise en B →^{v_n} C/𝔏_n →^{φ_n} C/(𝔍+𝔏_n), où v_n'",
    "set inline in the running text; Fraktur L", r"a displayed formula with \mathfrak Q", "other",
    r"se factorise en¶\[¶  B\xrightarrow{v_n}C/\mathfrak Q_n¶  \xrightarrow{\varphi_n}C/(\mathfrak J+\mathfrak Q_n),¶\]¶où $v_n$",
    r"se factorise en¶$B\xrightarrow{v_n}C/\mathfrak L_n¶\xrightarrow{\varphi_n}C/(\mathfrak J+\mathfrak L_n)$,¶où $v_n$",
    "One edit: inline as printed and the two 𝔏 for \\mathfrak Q.")
add(84, "proof of (19.3.10), display 'B →^{v_{n+1}} C/𝔏_{n+1} → C/𝔏_n'", "Fraktur L twice", r"\mathfrak Q", "symbol",
    r"C/\mathfrak Q_{n+1}\to C/\mathfrak Q_n", r"C/\mathfrak L_{n+1}\to C/\mathfrak L_n", L_NOTE)
add(84, "proof of (19.3.10), end: 'Cela résultera du lemme suivant :'", "colon", "full stop", "punctuation",
    r"du lemme suivant.", r"du lemme suivant~:")
add(84, "Lemme (19.3.10.1): '𝔎 (resp. 𝔎') un idéal nilpotent'",
    "Fraktur K twice; '(resp. 𝔎')' upright in the italic statement (enlarged crop)",
    r"$\mathfrak R$ (resp. $\mathfrak R'$), parenthesis italic", "symbol",
    r"$\mathfrak R$ (resp. $\mathfrak R'$) un idéal", r"$\mathfrak K$ \textup{(resp. $\mathfrak K'$)} un idéal",
    "One edit: the letter (" + K_NOTE + ") and the upright parenthesis (convention 6).")
add(84, "Lemme (19.3.10.1): 'un idéal nilpotent de E (resp. E')'", "'(resp. E')' upright (enlarged crop)",
    "italic (statement environment)", "convention", r"de $E$ (resp. $E'$),", r"de $E$ \textup{(resp. $E'$)},", "", conv=6)
add(84, "Lemme (19.3.10.1): 'tel que f(𝔎)⊂𝔎', f' : E/𝔎 → E'/𝔎''", "Fraktur K four times", r"\mathfrak R", "symbol",
    r"$f(\mathfrak R)\subset\mathfrak R'$, $f':E/\mathfrak R\to¶E'/\mathfrak R'$",
    r"$f(\mathfrak K)\subset\mathfrak K'$, $f':E/\mathfrak K\to¶E'/\mathfrak K'$", K_NOTE)
add(84, "Lemme (19.3.10.1): 'Soient u : B→E/𝔎 un A-homomorphisme continu'", "Fraktur K", r"\mathfrak R", "symbol",
    r"$u:B\to E/\mathfrak R$ un", r"$u:B\to E/\mathfrak K$ un", K_NOTE)
add(84, "Lemme (19.3.10.1): 'B →^u E/𝔎 →^{f'} E'/𝔎''", "Fraktur K twice", r"\mathfrak R", "symbol",
    r"E/\mathfrak R\xrightarrow{f'}E'/\mathfrak R'", r"E/\mathfrak K\xrightarrow{f'}E'/\mathfrak K'", K_NOTE)
add(84, "Lemme (19.3.10.1): 'B →^{v'} E' → E'/𝔎'. Alors'", "Fraktur K", r"\mathfrak R", "symbol",
    r"E'\to E'/\mathfrak R'$. Alors", r"E'\to E'/\mathfrak K'$. Alors", K_NOTE)
add(84, "proof of (19.3.10.1), diagram: bottom row 'E/𝔎 →_{f'} E'/𝔎''", "Fraktur K twice", r"\mathfrak R", "symbol",
    r"E/\mathfrak R \ar[r]_{f'} & E'/\mathfrak R'", r"E/\mathfrak K \ar[r]_{f'} & E'/\mathfrak K'", K_NOTE)
add(84, "proof of (19.3.10.1): 'et 𝔎' à (𝔎+𝔏)/𝔏'", "Fraktur K twice", r"\mathfrak R", "symbol",
    r"et $\mathfrak R'$ à¶$(\mathfrak R+\mathfrak L)/\mathfrak L$", r"et $\mathfrak K'$ à¶$(\mathfrak K+\mathfrak L)/\mathfrak L$", K_NOTE)
add(84, "proof of (19.3.10.1): 'Utilisons maintenant le lemme élémentaire suivant :'", "colon", "full stop",
    "punctuation", r"élémentaire suivant.", r"élémentaire suivant~:")
add(84, "Lemme (19.3.10.2): 'alors le produit fibré (F/𝔞)×_{F/(𝔞+𝔟)}(F/𝔟) s'identifie canoniquement'",
    "set inline in the statement", r"a displayed formula \[...\]", "other",
    r"le produit fibré¶\[¶  (F/\mathfrak a)\times_{F/(\mathfrak a+\mathfrak b)}(F/\mathfrak b)¶\]¶s'identifie",
    r"le produit fibré¶$(F/\mathfrak a)\times_{F/(\mathfrak a+\mathfrak b)}(F/\mathfrak b)$¶s'identifie",
    "GLOBAL_ISSUES 21.")
add(84, "proof of (19.3.10.2): '𝔎 par (𝔞+𝔟)/𝔟'", "Fraktur K, the 𝔎 of diagram (18.1.7.1) (TeX of (18.1.7): \\mathfrak{K})",
    r"\mathfrak R", "symbol", r"$\mathfrak R$ par¶$(\mathfrak a+\mathfrak b)/\mathfrak b$",
    r"$\mathfrak K$ par¶$(\mathfrak a+\mathfrak b)/\mathfrak b$", K_NOTE)
add(84, "proof of (19.3.10.2): 'le F-homomorphisme bijectif canonique (𝔞+𝔟)/𝔟 ⥲ 𝔞/(𝔞∩𝔟)'",
    "isomorphism arrow (tilde over the arrow; enlarged crop)", r"plain \to", "symbol",
    r"/\mathfrak b\to¶\mathfrak a/(", r"/\mathfrak b\xrightarrow{\sim}¶\mathfrak a/(",
    "Not convention 4 (the TeX has \\to, not \\simeq).")
add(84, "Proposition (19.3.10): 'Alors, tout A-homomorphisme continu u : B → C/𝔍 se factorise'",
    "new indented paragraph after 2°", "no blank line after \\end{enumerate}: continues unindented", "other",
    r"\end{enumerate}¶Alors, tout", r"\end{enumerate}¶¶Alors, tout", "", conf="medium")

# ---------------------------------------------------------------- p. 85
add(85, "top of p. 85: 'Appliquant ce lemme à la situation de (19.3.10.1)'", "paragraph without any heading",
    r"\begin{proof}[Suite de la démonstration du lemme~{\rm(19.3.10.1)}]: the bracket text is typeset", "extra",
    r"\begin{proof}[Suite de la démonstration du lemme~{\rm(19.3.10.1)}]", r"\begin{proof}", "GLOBAL_ISSUES 58.")
add(85, "diagram: bottom row 'E/𝔎 →_{f'} E'/𝔎''", "Fraktur K twice", r"\mathfrak R", "symbol",
    r"E/\mathfrak R \ar[r]_{f'} & E'/\mathfrak R'", r"E/\mathfrak K \ar[r]_{f'} & E'/\mathfrak K'", K_NOTE)
add(85, "'d'un homomorphisme w : B → E/(𝔎∩𝔏) tel que'", "Fraktur K", r"\mathfrak R", "symbol",
    r"$w:B\to E/(\mathfrak R\cap\mathfrak L)$ tel que", r"$w:B\to E/(\mathfrak K\cap\mathfrak L)$ tel que", K_NOTE)
add(85, "'en B →^w E/(𝔎∩𝔏) → E/𝔏 et B →^w E/(𝔎∩𝔏) → E/𝔎'", "Fraktur K three times", r"\mathfrak R", "symbol",
    r"E/(\mathfrak R\cap\mathfrak L)\to E/\mathfrak L$¶et¶$B\xrightarrow{w}E/(\mathfrak R\cap\mathfrak L)\to E/\mathfrak R$",
    r"E/(\mathfrak K\cap\mathfrak L)\to E/\mathfrak L$¶et¶$B\xrightarrow{w}E/(\mathfrak K\cap\mathfrak L)\to E/\mathfrak K$", K_NOTE)
add(85, "'il est clair que 𝔎∩𝔏 est nilpotent'", "Fraktur K", r"\mathfrak R", "symbol",
    r"que $\mathfrak R\cap\mathfrak L$ est nilpotent", r"que $\mathfrak K\cap\mathfrak L$ est nilpotent", K_NOTE)
add(85, "'donc w se factorise en B →^u E → E/(𝔎∩𝔏)'", "Fraktur K", r"\mathfrak R", "symbol",
    r"E/(\mathfrak R\cap\mathfrak L)$, où", r"E/(\mathfrak K\cap\mathfrak L)$, où",
    K_NOTE + " Listed before the two misprint edits of the same line (no overlap).")
add(85, "'donc w se factorise en B →^u E → E/(𝔎∩𝔏)': arrow label",
    "u over the arrow (enlarged crop)", r"\xrightarrow{v}: silently corrected", "misprint_in_print",
    r"\xrightarrow{v}E\to", r"\xrightarrow{u}E\to",
    "u is already the map B → E/𝔎 of the lemma; the map B → E answering the lemma is v. The TeX silently corrects "
    "the print; the fix restores the printed u.", corrected=r"\xrightarrow{v}E\to")
add(85, "'où u est un A-homomorphisme continu répondant à la question'",
    "'où u est' (enlarged crop)", r"'où $v$ est': silently corrected", "misprint_in_print",
    r"$v$ est¶un $A$-homomorphisme continu répondant", r"$u$ est¶un $A$-homomorphisme continu répondant",
    "Same misprint as the arrow label (u for v).", corrected=r"$v$ est¶un $A$-homomorphisme continu répondant")
add(85, "'Revenant à la démonstration de (19.3.10), l'existence de v_{n+1}'", "new paragraph without any heading",
    r"\begin{proof}[Suite de la démonstration de la proposition~{\rm(19.3.10)}]: the bracket text is typeset", "extra",
    r"\begin{proof}[Suite de la démonstration de la proposition~{\rm(19.3.10)}]", r"\begin{proof}",
    "GLOBAL_ISSUES 58. The printed words the bracket replaced: next finding.")
add(85, "'Revenant à la démonstration de (19.3.10), l'existence de v_{n+1} résulte du lemme'",
    "'Revenant à la démonstration de (19.3.10), l'existence'", "'L'existence': the opening words are missing",
    "missing", r"L'existence de $v_{n+1}$ résulte",
    r"Revenant à la démonstration de (19.3.10), l'existence de $v_{n+1}$ résulte")
add(85, "'en remplaçant E, E', 𝔎, 𝔎' par'", "Fraktur K twice", r"\mathfrak R", "symbol",
    r"$\mathfrak R$, $\mathfrak R'$ par", r"$\mathfrak K$, $\mathfrak K'$ par", K_NOTE)
add(85, "'par C/𝔏_{n+1}, C/𝔏_n, (𝔍+𝔏_{n+1})/𝔏_{n+1} et (𝔍+𝔏_n)/𝔏_n respectivement'", "Fraktur L six times",
    r"\mathfrak Q", "symbol",
    r"$C/\mathfrak Q_{n+1}$, $C/\mathfrak Q_n$,¶$(\mathfrak J+\mathfrak Q_{n+1})/\mathfrak Q_{n+1}$ et¶$(\mathfrak J+\mathfrak Q_n)/\mathfrak Q_n$ respectivement",
    r"$C/\mathfrak L_{n+1}$, $C/\mathfrak L_n$,¶$(\mathfrak J+\mathfrak L_{n+1})/\mathfrak L_{n+1}$ et¶$(\mathfrak J+\mathfrak L_n)/\mathfrak L_n$ respectivement", L_NOTE)
add(85, "'il est égal à lim←_n (C/𝔏_n)'", "Fraktur L", r"\mathfrak Q", "symbol",
    r"\varprojlim_n(C/\mathfrak Q_n)", r"\varprojlim_n(C/\mathfrak L_n)", L_NOTE)
add(85, "'on a 𝔍 = ∩_n(𝔍+𝔏_n)'", "Fraktur L", r"\mathfrak Q", "symbol",
    r"\bigcap_n(\mathfrak J+\mathfrak Q_n)", r"\bigcap_n(\mathfrak J+\mathfrak L_n)", L_NOTE)
add(85, "'que les (𝔍+𝔏_n)/𝔍 forment un système fondamental'", "Fraktur L", r"\mathfrak Q", "symbol",
    r"$(\mathfrak J+\mathfrak Q_n)/\mathfrak J$ forment", r"$(\mathfrak J+\mathfrak L_n)/\mathfrak J$ forment", L_NOTE)
add(85, "'on a C/𝔍 = lim←_n(C/(𝔍+𝔏_n)) et lim← φ_n est l'application canonique'",
    "inline in the running text, with parentheses around C/(𝔍+𝔏_n); Fraktur L",
    r"displayed, \varprojlim_n C/(\mathfrak J+\mathfrak Q_n) without the outer parentheses", "formula",
    r"on a¶\[¶  C/\mathfrak J=\varprojlim_n C/(\mathfrak J+\mathfrak Q_n)¶\]¶et",
    r"on a¶$C/\mathfrak J=\varprojlim_n(C/(\mathfrak J+\mathfrak L_n))$¶et",
    "One edit: printed parentheses, inline as printed (GLOBAL_ISSUES 21) and 𝔏 for \\mathfrak Q.")
add(85, "end of the proof of (19.3.10): 'Comme lim u_n = u, on a bien u = v∘φ, C.Q.F.D.'",
    "u = v∘φ", r"keeps the print: $u=v\circ\varphi$", "misprint_in_print", None, None,
    "The TeX keeps the printed reading. v : B → C and φ : C → C/𝔍, so the composite B → C/𝔍 is φ∘v; v∘φ does not compose.",
    corrected=r"$u=\varphi\circ v$")
add(85, "Proposition (19.3.12) 1°: 'idéaux ouverts 𝔏_λ de C, tels que les C_λ = C/𝔏_λ'",
    "Fraktur L twice (small type; enlarged crop)", r"\mathfrak Q_\lambda", "symbol",
    r"$\mathfrak Q_\lambda$ de $C$, tels que les¶  $C_\lambda=C/\mathfrak Q_\lambda$",
    r"$\mathfrak L_\lambda$ de $C$, tels que les¶  $C_\lambda=C/\mathfrak L_\lambda$", L_NOTE)
add(85, "Proposition (19.3.12): 'Dans ces conditions, tout A-homomorphisme continu'",
    "new indented paragraph after 3°", "no blank line after \\end{enumerate}: continues unindented", "other",
    r"\end{enumerate}¶Dans ces conditions", r"\end{enumerate}¶¶Dans ces conditions", "", conf="medium")
add(85, "proof of (19.3.12): 'Soit 𝔍_λ = (𝔍+𝔏_λ)/𝔏_λ'", "Fraktur L twice", r"\mathfrak Q", "symbol",
    r"\mathfrak J_\lambda=(\mathfrak J+\mathfrak Q_\lambda)/\mathfrak Q_\lambda",
    r"\mathfrak J_\lambda=(\mathfrak J+\mathfrak L_\lambda)/\mathfrak L_\lambda", L_NOTE)
add(85, "proof of (19.3.12): 'C_λ/𝔍_λ = C/(𝔍+𝔏_λ).'", "Fraktur L", r"\mathfrak Q", "symbol",
    r"=C/(\mathfrak J+\mathfrak Q_\lambda)$.", r"=C/(\mathfrak J+\mathfrak L_\lambda)$.", L_NOTE)
add(85, "proof of (19.3.12): 'Montrons que tout A-homomorphisme w : B → C'", "'tout' italic (enlarged crop)",
    "roman", "italics", r"Montrons que tout", r"Montrons que \emph{tout}")
add(85, "proof of (19.3.12): 'est nécessairement continu; en effet'", "'continu' italic (enlarged crop)", "roman",
    "italics", r"nécessairement continu~;", r"nécessairement \emph{continu}~;")
add(85, "proof of (19.3.12): 'un idéal ouvert 𝔎 de B tel que u(𝔎) ⊂ (𝔍+𝔏_λ)/𝔍'", "Fraktur K twice, Fraktur L",
    r"\mathfrak R, \mathfrak Q", "symbol",
    r"idéal ouvert $\mathfrak R$ de $B$¶tel que $u(\mathfrak R)\subset¶(\mathfrak J+\mathfrak Q_\lambda)/\mathfrak J$",
    r"idéal ouvert $\mathfrak K$ de $B$¶tel que $u(\mathfrak K)\subset¶(\mathfrak J+\mathfrak L_\lambda)/\mathfrak J$",
    K_NOTE + " " + L_NOTE)
add(85, "proof of (19.3.12): 'd'où w(𝔎) ⊂ 𝔍+𝔏_λ'", "Fraktur K, Fraktur L", r"\mathfrak R, \mathfrak Q", "symbol",
    r"$w(\mathfrak R)\subset\mathfrak J+\mathfrak Q_\lambda$", r"$w(\mathfrak K)\subset\mathfrak J+\mathfrak L_\lambda$",
    K_NOTE + " " + L_NOTE)
add(85, "proof of (19.3.12): 'une puissance 𝔎^{2^m} de 𝔎 telle que'", "Fraktur K twice", r"\mathfrak R", "symbol",
    r"puissance $\mathfrak R^{2^m}$ de $\mathfrak R$ telle", r"puissance $\mathfrak K^{2^m}$ de $\mathfrak K$ telle", K_NOTE)
add(85, "proof of (19.3.12): 'w(𝔎^{2^m}) ⊂ 𝔏_λ'", "Fraktur K, Fraktur L", r"\mathfrak R, \mathfrak Q", "symbol",
    r"$w(\mathfrak R^{2^m})\subset\mathfrak Q_\lambda$", r"$w(\mathfrak K^{2^m})\subset\mathfrak L_\lambda$",
    K_NOTE + " " + L_NOTE)
add(85, "proof of (19.3.12): 'puisque 𝔎^{2^m} est ouvert dans B'", "Fraktur K", r"\mathfrak R", "symbol",
    r"puisque $\mathfrak R^{2^m}$ est ouvert", r"puisque $\mathfrak K^{2^m}$ est ouvert", K_NOTE)
add(85, "proof of (19.3.12): 'est égal à lim← Hom(B, C_λ)'", "lim with the arrow and no index (enlarged crop)",
    r"\varprojlim_\lambda", "formula", r"\varprojlim_\lambda\operatorname{Hom}(B,C_\lambda)",
    r"\varprojlim\operatorname{Hom}(B,C_\lambda)", "As GLOBAL_ISSUES 30 (inline lims printed without index).")
add(85, "proof of (19.3.12): 'fermé dans le C-module C_λ^B'", "'C-module' (no subscript; enlarged crop)",
    r"$C_\lambda$-module", "formula", r"dans le $C_\lambda$-module", r"dans le $C$-module",
    "Not a misprint: C_λ^B is a C-module through C → C_λ.")
add(85, "last line: 'Pour tout λ, soit W_λ | l'ensemble des w_λ' (page break mid-sentence)",
    "the sentence runs on to p. 86 without a paragraph break",
    r"blank lines before and after \oldpage[0\textsubscript{IV-1}]{86}: two paragraph breaks", "other",
    r"soit $W_\lambda$¶¶", r"soit $W_\lambda$¶",
    "GLOBAL_ISSUES 20. Must go with the p. 86 half (next finding), which removes the blank line after the marker.")
add(86, r"top of p. 86: blank line after \oldpage[0\textsubscript{IV-1}]{86} before 'l'ensemble des w_λ'",
    "continuation of the sentence begun on p. 85", "paragraph break", "other",
    MK + r"{86}¶¶l'ensemble", MK + r"{86}¶l'ensemble",
    "OUTSIDE MY PAGE SEGMENT (page_086.tex); second half of the previous finding. The p. 86-90 checker may report it too.")

# ---------------------------------------------------------------- checks
pages = {}
for f in F:
    p = f["page"]
    if p not in pages:
        pages[p] = (RUN / ("page_%03d.tex" % p)).read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for i, f in enumerate(F):
    if f["fix"]:
        c = pages[f["page"]].count(f["fix"]["old"])
        if c != 1:
            bad += 1
            print("UNIQUENESS", i, f["page"], c, repr(f["fix"]["old"][:80]))
print("uniqueness problems:", bad)

# dry run of apply_fixes.py's logic on ega0-19-fr.tex
t = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[" + re.escape(r"0\textsubscript{IV-1}") + r"\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, st) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return st, cuts[j][1] if j < len(cuts) else len(text)
    return None, None


fails = 0
for i, f in enumerate(F):
    if not f["fix"]:
        continue
    st, en = locate(t, f["page"])
    seg = t[st:en]
    c = seg.count(f["fix"]["old"])
    if c != 1:
        fails += 1
        print("DRY-RUN", i, f["page"], c, repr(f["fix"]["old"][:80]))
        continue
    t = t[:st] + seg.replace(f["fix"]["old"], f["fix"]["new"]) + t[en:]
print("dry-run failures:", fails)
for p in range(80, 87):
    st, en = locate(t, p)
    seg = t[st:en]
    print(p, "markers for this page:", len(re.findall(re.escape(MK + "{%d}" % p), t)),
          "| R:", seg.count(r"\mathfrak R"), "Q:", seg.count(r"\mathfrak Q"), "| starts:", repr(seg[len(MK) + 4:len(MK) + 60]))
(RUN / "crops_081_085" / "dryrun_ega0-19.tex").write_text(t, encoding="utf-8", newline="")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
print(sorted(cnt.items()))
print("written", OUT, len(F))
