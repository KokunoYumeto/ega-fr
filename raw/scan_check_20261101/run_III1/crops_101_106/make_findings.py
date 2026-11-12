"""Build findings_101_106.json for EGA III pp. 101-106 and simulate apply_fixes.py on the page files.
Strings use the pilcrow as the line-break marker (LaTeX contains \\n sequences such as \\neq)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_101_106.json"
NL = "\u00b6"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=s(old), new=s(new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def c2(page, where, ref, old=None, new=None):
    old = old or ref
    new = new or old.replace("(II,", r"(\textbf{II},").replace("(I,", r"(\textbf{I},").replace(
        r"(0\textsubscript{I},", r"(\textbf{0}\textsubscript{I},")
    add(page, where, ref + " with the chapter number in bold", ref + " (plain)", "convention", 2, "high", old, new,
        "Bold chapter number in the reference.")


# ---------------------------------------------------------------- page 101 (and the missing marker of page 102)
add(101, "Corollaire (2.2.4), statement: end of printed p. 101 / start of p. 102",
    "p. 101 ends '... une suite exacte de O_X-Modules cohérents,'; p. 102 begins 'telle que les supports de F et de H soient propres sur Y'",
    r"no \oldpage[III]{102}; the text of p. 102 runs on inside page_101.tex (up to \oldpage[III]{103})",
    "marker", None, "high",
    r"$\mathcal O_X$-Modules cohérents, telle que",
    r"$\mathcal O_X$-Modules cohérents,¶\oldpage[III]{102}¶telle que",
    "Inserts the missing page-102 marker. Apply this first: the findings with page 102 below are located in the segment it creates (their 'old' strings lie in the p. 102 part of page_101.tex).")
add(101, "First line of p. 101 (proof of (2.2.2))",
    "p. 100 ends '... Comme X est recouvert par les ouverts'; p. 101 begins 'affines D_+(T_i) en nombre r+1'",
    r"\oldpage[III]{101} stands before 'Comme $X$ est recouvert par les ouverts affines'",
    "marker", None, "high",
    r"\oldpage[III]{101}¶Comme $X$ est recouvert par les ouverts affines",
    r"Comme $X$ est recouvert par les ouverts¶\oldpage[III]{101}¶affines",
    r"Moves the marker after 'ouverts'. The moved words then follow the blank line after the display ending p. 100 ('\]' + blank line); the print continues the same paragraph there ('... S=A[T_0, ..., T_r]. Comme X est recouvert ...'), so that blank line, in the p. 100 segment, should also go (see final message).")
c2(101, "Proof of (2.2.2), 1st paragraph", "(II, 2.7.9)")
c2(101, "Proof of (2.2.2), 2nd paragraph", "(II, 2.7.10)")
c2(101, "Proof of (2.2.2), 2nd paragraph: 'où R est cohérent'", r"(0\textsubscript{I}, 5.3.3)")
add(101, "Proof of (2.2.2): 'Comme E(n) est somme directe des O_X(n+m_j)' after the display H^{q-1}(X, E(n)) -> ...",
    "new indented paragraph after the display", r"'\]' followed directly by 'Comme' (no paragraph break)",
    "other", None, "high",
    r"\]¶Comme $\mathcal E(n)$", r"\]¶¶Comme $\mathcal E(n)$",
    "The line 'Comme E(n) est somme directe ...' is indented in the print.")
c2(101, "Proof of (2.2.2), 3rd paragraph", "(II, 2.5.14)")
add(101, "Corollaire (2.2.3), statement: 'Sous les hypothèses de (2.2.1), soit'",
    "(2.2.1) upright inside the italic statement", "(2.2.1) inside the corollary environment (italic)",
    "convention", 6, "high",
    r"hypothèses de (\hyperref[III.2.2.1-fr]{2.2.1}), soit",
    r"hypothèses de \textup{(\hyperref[III.2.2.1-fr]{2.2.1})}, soit",
    "Reference printed roman inside the italic statement.")
c2(101, "Proof of (2.2.3)", r"(0\textsubscript{I}, 5.3.4)")
add(101, "Proof of (2.2.3), the three short exact sequences, end of the 1st line",
    "... -> f_*(G'(n)) -> 0 (no punctuation)", r"\longrightarrow0,\\ (comma)",
    "punctuation", None, "high",
    r"f_*(\mathcal G'(n))\longrightarrow0,\\", r"f_*(\mathcal G'(n))\longrightarrow0\\",
    "Enlarged crop: the three sequences carry no punctuation.")
add(101, "Proof of (2.2.3), the three short exact sequences, end of the 2nd line",
    "... -> f_*(G''(n)) -> 0 (no punctuation)", r"\longrightarrow0,\\ (comma)",
    "punctuation", None, "high",
    r"f_*(\mathcal G''(n))\longrightarrow0,\\", r"f_*(\mathcal G''(n))\longrightarrow0\\",
    "Enlarged crop: the three sequences carry no punctuation.")
add(101, "Proof of (2.2.3), long exact sequence: '-> R^1f_*(F(n)) -> ...'",
    ". . . (dots on the baseline)", r"\cdots",
    "symbol", None, "high",
    r"\longrightarrow\cdots", r"\longrightarrow\ldots",
    "Baseline dots in the print (GLOBAL_ISSUES item 22).")

# ---------------------------------------------------------------- page 102 (text inside page_101.tex)
add(102, "Corollaire (2.2.4), statement: 'propres sur Y (II, 5.4.10)'",
    "(II, 5.4.10): bold II, reference upright inside the italic statement",
    "(II, 5.4.10) plain, italic inside the corollary environment",
    "convention", 2, "high",
    r"propres sur $Y$ (II, 5.4.10)", r"propres sur $Y$ \textup{(\textbf{II}, 5.4.10)}",
    "Conventions 2 and 6 together (bold II; reference roman in the italic statement).")
add(102, "Corollaire (2.2.4), statement, last word before the proof",
    "la suite f_*(F(n)) -> f_*(G(n)) -> f_*(H(n)) est exacte.", "soit exacte.",
    "word", None, "high",
    r"soit exacte.¶\end{corollary}¶¶\begin{proof}¶Le même",
    r"est exacte.¶\end{corollary}¶¶\begin{proof}¶Le même",
    "The print has 'est exacte' in (2.2.4) ((2.2.3) has 'soit exacte', which the TeX rightly keeps). Context included because 'soit exacte.' also ends (2.2.3) in page_101.tex.")
c2(102, "Proof of (2.2.4)", "(II, 4.6.11)")
c2(102, "Proof of (2.2.4)", "(II, 4.4.7)")
add(102, "Proof of (2.2.4): 'comme Supp(G) est fermé dans X et contenu dans Supp(F) ∩ Supp(H)'",
    "Supp(F) ∩ Supp(H) (intersection sign; enlarged crop)",
    r"\operatorname{Supp}(\mathcal F)\cap\operatorname{Supp}(\mathcal H) (keeps the printed reading)",
    "misprint_in_print", None, "high", None, None,
    "In the exact sequence F -> G -> H, G_x = 0 wherever F_x = H_x = 0, so Supp(G) lies in the union Supp(F) ∪ Supp(H) (which is proper over Y, as the argument needs); it need not lie in the intersection (take H = 0, G = F). The TeX keeps the printed ∩.",
    corrected=r"\operatorname{Supp}(\mathcal F)\cup\operatorname{Supp}(\mathcal H)")
c2(102, "Proof of (2.2.4): 'sont donc fermés dans Z (II, 5.4.10)'", "(II, 5.4.10)",
   old=r"dans $Z$} (II, 5.4.10)", new=r"dans $Z$} (\textbf{II}, 5.4.10)")
add(102, "Proof of (2.2.4): 'F'(n)=i_*(F(n)) et de même pour G' et H''",
    "F'(n)=i_*(F(n))  et de même (no comma)", r"$\mathcal F'(n)=i_*(\mathcal F(n))$, et de même",
    "punctuation", None, "high",
    r"i_*(\mathcal F(n))$, et de même", r"i_*(\mathcal F(n))$ et de même",
    "Enlarged crop: no comma after the formula.")
c2(102, "Remarques (2.2.5), (i)", "(II, 5.5.5, (iii))")
c2(102, "Remarques (2.2.5), (i)", "(II, 4.6.4)")
c2(102, "Remarques (2.2.5), (ii)", "(II, 4.6.8)")
c2(102, "Remarques (2.2.5), (ii)", "(II, 5.1.10)")
c2(102, "Remarques (2.2.5), (ii)", "(II, 5.1.6)")
c2(102, "Remarques (2.2.5), (ii)", "(I, 8.2.1.1)")
add(102, "Théorème (2.3.1), statement: 'vérifiant la condition (TF)'",
    "(TF) bold upright inside the italic statement", r"\textbf{(TF)} inside the theorem environment (bold italic)",
    "convention", 6, "high",
    r"la condition \textbf{(TF)}. Alors", r"la condition \textup{\textbf{(TF)}}. Alors",
    r"Same treatment as the EGA II precedent \textup{\textbf{(TN)}}.")
add(102, "Théorème (2.3.1), statement: 'l'homomorphisme canonique (II, 8.14.5.1)'",
    "(II, 8.14.5.1): bold II, reference upright inside the italic statement",
    "(II, 8.14.5.1) plain, italic inside the theorem environment",
    "convention", 2, "high",
    "(II, 8.14.5.1)", r"\textup{(\textbf{II}, 8.14.5.1)}",
    "Conventions 2 and 6 together.")

# ---------------------------------------------------------------- page 103
add(103, "Théorème (2.3.1), end of the statement: 'est un (TN)-isomorphisme.'",
    "(TN) bold upright, '-isomorphisme' italic", r"\textbf{(TN)} inside the theorem environment (bold italic)",
    "convention", 6, "high",
    r"est un \textbf{(TN)}-isomorphisme.¶\end{theorem}", r"est un \textup{\textbf{(TN)}}-isomorphisme.¶\end{theorem}",
    "Bold (TN) printed upright in the italic statement.")
add(103, "Proof of (2.3.1), first sentence: 'On peut se borner au cas où M est un S-module de type fini'",
    "S-module (lower-case m; enlarged crop)", r"$\mathcal S$-module (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "M is a sheaf of graded S-Modules (statement of (2.3.1): 'M un S-Module gradué'); the print's lower-case 'module' breaks the Module/module convention. The TeX keeps it.",
    corrected=r"$\mathcal S$-Module")
c2(103, "Proof of (2.3.1), first sentence", "(II, 3.4.2)")
add(103, "Proof of (2.3.1): after 'de type fini (II, 3.4.2).'",
    "paragraph break: 'Comme Y est quasi-compact' begins a new indented paragraph",
    "same paragraph", "other", None, "high",
    "3.4.2). Comme $Y$ est quasi-compact", "3.4.2).¶¶Comme $Y$ est quasi-compact",
    "The first sentence of the proof stands alone as a paragraph in the print.")
c2(103, "Proof of (2.3.1), 2nd paragraph", "(II, 3.1.10)")
c2(103, "Proof of (2.3.1), 2nd paragraph", "(II, 2.1.6, (iii))")
c2(103, "Proof of (2.3.1), 2nd paragraph", "(II, 8.14.13)")
add(103, "Proof of (2.3.1): 'Compte tenu de (II, 8.14.13) (et notamment du diagramme (8.14.13.4)), on voit'",
    "(II, 8.14.13) (et notamment du diagramme (8.14.13.4)), on voit",
    "(II, 8.14.13), et notamment du diagramme (8.14.13.4), on voit",
    "punctuation", None, "high",
    "8.14.13), et¶notamment du diagramme (8.14.13.4), on", "8.14.13) (et¶notamment du diagramme (8.14.13.4)), on",
    "The print puts the remark in parentheses, not between commas.")
add(103, "Proof of (2.3.1): '... est un O_Y-Module cohérent. Comme Y est noethérien'",
    "no paragraph break: 'Comme Y est noethérien' continues the line, not indented",
    "blank line (new paragraph)", "other", None, "high",
    "-Module cohérent.¶¶Comme $Y$ est noethérien", "-Module cohérent.¶Comme $Y$ est noethérien",
    "Paragraph break the print does not have.")
add(103, "Diagram, top row, first entry",
    "L̃'_n: tilde over L only, prime and n outside", r"\widetilde {L'_n}",
    "convention", 8, "high", r"\widetilde {L'_n}", r"\widetilde{L}'_n",
    "Tilde over a letter carrying a prime and a subscript.")
add(103, "Diagram, top row, second entry",
    "L̃_n: tilde over L only", r"\widetilde {L_n}",
    "convention", 8, "high", r"\widetilde {L_n}", r"\widetilde{L}_n",
    "Tilde over a letter carrying a subscript.")
add(103, "Diagram, top row, third entry",
    "M̃_n: tilde over M only", r"\widetilde {M_n}",
    "convention", 8, "high", r"\widetilde {M_n}", r"\widetilde{M}_n",
    "Tilde over a letter carrying a subscript.")
add(103, "Diagram, middle vertical arrow",
    "label α_n to the left of the arrow", r"\ar[d]^{\alpha_n} (label to the right)",
    "formula", None, "high",
    r"\ar[d]^{\alpha_n} &¶", r"\ar[d]_{\alpha_n} &¶",
    "All three labels α_n stand left of their arrows in the print; the first arrow already has _.")
add(103, "Diagram, right vertical arrow",
    "label α_n to the left of the arrow", r"\ar[d]^{\alpha_n} (label to the right)",
    "formula", None, "high",
    r"\ar[d]^{\alpha_n} & 0", r"\ar[d]_{\alpha_n} & 0",
    "All three labels α_n stand left of their arrows in the print.")
add(103, "Diagram, end of the bottom row: '-> q_*(M̃(n)) -> 0'",
    "-> 0 (no full stop)", "& 0 . (full stop)",
    "punctuation", None, "high",
    "& 0 .¶}", "& 0¶}",
    "Enlarged crop: no full stop after the diagram.")
add(103, "Proof of (2.3.1): 'La deuxième ligne est exacte en vertu de (2.2.3)' after the diagram",
    "new indented paragraph after the diagram", r"'\]' followed directly by 'La deuxième ligne' (no paragraph break)",
    "other", None, "high",
    r"\]¶La deuxième ligne", r"\]¶¶La deuxième ligne",
    "The line 'La deuxième ligne est exacte ...' is indented in the print.")
c2(103, "Proof of (2.3.1), last paragraph", "(II, 2.9.2)")
c2(103, "Proof of (2.3.1), last paragraph", "(II, 2.8.7)")

# ---------------------------------------------------------------- page 104
add(104, "Corollaire (2.3.2), statement: 'Sous les hypothèses de (2.3.1), soit'",
    "(2.3.1) upright inside the italic statement", "(2.3.1) italic inside the corollary environment",
    "convention", 6, "high",
    r"hypothèses de (\hyperref[III.2.3.1-fr]{2.3.1}), soit", r"hypothèses de \textup{(\hyperref[III.2.3.1-fr]{2.3.1})}, soit",
    "Reference printed roman inside the italic statement.")
add(104, "Corollaire (2.3.2), statement: 'vérifie la condition (TF).'",
    "(TF) bold upright inside the italic statement", r"\textbf{(TF)} (bold italic in the environment)",
    "convention", 6, "high",
    r"la condition¶\textbf{(TF)}.", r"la condition¶\textup{\textbf{(TF)}}.",
    "Bold (TF) printed upright in the italic statement.")
c2(104, "Proof of (2.3.2): 'isomorphe à Proj(S^(d)) (II, 3.1.8)'", "(II, 3.1.8)")
add(104, "Proof of (2.3.2): 'Proj(S^(d)) (II, 3.1.8) est de type fini sur Y'",
    "(II, 3.1.8) est de type fini (no comma)", "(II, 3.1.8), est de type fini",
    "punctuation", None, "high",
    "), est de type fini sur", ") est de type fini sur",
    "Enlarged crop: no comma after the reference.")
c2(104, "Proof of (2.3.2)", "(II, 3.4.1)")
c2(104, "Proof of (2.3.2)", "(II, 8.14.9)")
add(104, "Proof of (2.3.2): 'Γ_*(F) est (TN)-isomorphe à M, et par suite vérifie (TF)'",
    "à M, et par suite (comma)", r"à $\mathcal M$ et par suite (no comma)",
    "punctuation", None, "high",
    r"isomorphe à $\mathcal M$ et par suite", r"isomorphe à $\mathcal M$, et par suite",
    "Enlarged crop: comma after M.")
kwhere = "Scholie (2.3.3)"
knote = r"Category letter K printed bold italic (cf. GLOBAL_ISSUES 18 and 33); the EGA III ch. 0 precedent uses \boldsymbol."
add(104, kwhere + ": 'Soient K_S la catégorie abélienne'", "bold italic K", "plain K", "font", None, "high",
    r"Soient $K_{\mathcal S}$", r"Soient $\boldsymbol{K}_{\mathcal S}$", knote)
add(104, kwhere + ": 'K'_S la sous-catégorie'", "bold italic K", "plain K", "font", None, "high",
    r"$K'_{\mathcal S}$ la", r"$\boldsymbol{K}'_{\mathcal S}$ la", knote)
add(104, kwhere + ": 'sous-catégorie de K_S formée'", "bold italic K", "plain K", "font", None, "high",
    r"de $K_{\mathcal S}$ formée", r"de $\boldsymbol{K}_{\mathcal S}$ formée", knote)
add(104, kwhere + ": 'soit K_X la catégorie'", "bold italic K", "plain K", "font", None, "high",
    r"soit $K_X$ la", r"soit $\boldsymbol{K}_X$ la", knote)
c2(104, kwhere + ": 'puisque S_X est périodique (II, 8.14.4 et 8.14.12)'", "(II, 8.14.4 et 8.14.12)")
add(104, kwhere + ": 'M ⇝ Proj(M) dans K_S'", "wavy arrow M ⇝ Proj(M)", r"\longmapsto",
    "symbol", None, "high", r"\mathcal M\longmapsto", r"\mathcal M\leadsto",
    "Wavy maps-to arrow in the print (\\leadsto), not convention 3.")
add(104, kwhere + ": 'dans K_S et F ⇝ Γ_*(F)'", "bold italic K", "plain K", "font", None, "high",
    r"\text{dans }K_{\mathcal S}", r"\text{dans }\boldsymbol{K}_{\mathcal S}", knote)
add(104, kwhere + ": 'Proj(M) dans K_S et F ⇝ Γ_*(F) dans K_X'",
    "'et' between the two functors, no comma", r"comma and \qquad between the two functors",
    "word", None, "high",
    r",¶\qquad¶", r"¶\quad\text{et}\quad¶",
    "The print reads 'M ⇝ Proj(M) dans K_S et F ⇝ Γ_*(F) dans K_X définissent' (inline); the display may stay.")
add(104, kwhere + ": 'F ⇝ Γ_*(F) dans K_X'", "wavy arrow F ⇝ Γ_*(F)", r"\longmapsto",
    "symbol", None, "high", r"\mathcal F\longmapsto", r"\mathcal F\leadsto",
    "Wavy maps-to arrow in the print (\\leadsto), not convention 3.")
add(104, kwhere + ": 'Γ_*(F) dans K_X définissent'", "bold italic K", "plain K", "font", None, "high",
    r"\text{dans }K_X", r"\text{dans }\boldsymbol{K}_X", knote)
c2(104, kwhere + ": 'en vertu de (II, 8.14.8 et 8.14.10)'", "(II, 8.14.8 et 8.14.10)")
add(104, kwhere + ": 'en vertu de (II, 8.14.8 et 8.14.10) et (2.3.2) une équivalence'",
    "et (2.3.2)", "et de (2.3.2)", "word", None, "high",
    r" et de¶(\hyperref[III.2.3.2-fr]", r" et¶(\hyperref[III.2.3.2-fr]",
    "Enlarged crop: no 'de' before (2.3.2).")
add(104, kwhere + ": '(2.3.2) une équivalence'", "(2.3.2) une (no comma)", "(2.3.2), une",
    "punctuation", None, "high",
    "{2.3.2}), ", "{2.3.2}) ",
    "Enlarged crop: no comma after (2.3.2).")
add(104, kwhere + ": 'une équivalence (T, I, 1.2) de la catégorie quotient'",
    "'une équivalence' and 'de la catégorie quotient' italic", "upright",
    "italics", None, "high",
    "une équivalence (T, I, 1.2) de la¶catégorie quotient",
    r"\emph{une équivalence} (T, I, 1.2) \emph{de la¶catégorie quotient}",
    "Enlarged crop: the conclusion of the scholium is italicised; the references stay upright.")
add(104, kwhere + ": 'K_S/K'_S (T, I, 1.11)'", "bold italic K twice", "plain K", "font", None, "high",
    r"$K_{\mathcal S}/K'_{\mathcal S}$", r"$\boldsymbol{K}_{\mathcal S}/\boldsymbol{K}'_{\mathcal S}$", knote)
add(104, kwhere + ": '(T, I, 1.11) avec la catégorie K_X'", "'avec la catégorie' italic", "upright",
    "italics", None, "high",
    "(T, I, 1.11) avec la¶catégorie", r"(T, I, 1.11) \emph{avec la¶catégorie}",
    "Enlarged crop: italic in the print.")
add(104, kwhere + ": 'avec la catégorie K_X.'", "bold italic K", "plain K", "font", None, "high",
    r"$K_X$. Lorsque", r"$\boldsymbol{K}_X$. Lorsque", knote)
add(104, kwhere + ": 'Lorsque S est engendré par S_1'",
    "engendré (no final e; enlarged crop)", "engendrée (silently corrected)",
    "misprint_in_print", None, "high",
    r"engendrée par $\mathcal S_1$,¶on peut", r"engendré par $\mathcal S_1$,¶on peut",
    "S is an O_Y-Algèbre, so the participle should agree (as on p. 103 and in (2.3.4)). The fix restores the printed reading.",
    corrected="engendrée")
add(104, kwhere + ": 'on peut remplacer K_X par'", "bold italic K", "plain K", "font", None, "high",
    r"remplacer $K_X$ par", r"remplacer $\boldsymbol{K}_X$ par", knote)
c2(104, kwhere + ", last line", "(II, 8.14.12)", old="cohérents (II, 8.14.12)",
   new=r"cohérents (\textbf{II}, 8.14.12)")
add(104, "Proposition (2.3.4) (i): 'à degrés positifs, quasi-cohérente de type fini.'",
    "quasi-cohérente de type fini (no 'et'; enlarged crop)", "quasi-cohérente et de type fini",
    "extra", None, "high",
    "quasi-cohérente et de type fini. Soient", "quasi-cohérente de type fini. Soient",
    "(2.3.4) (ii) and (2.3.1) have 'et'; (i) does not.")
add(104, "Proposition (2.3.4) (i): 'graduée périodique (II, 8.14.12) dont'",
    "(II, 8.14.12): bold II, upright inside the italic statement", "(II, 8.14.12) plain, italic",
    "convention", 2, "high",
    "(II, 8.14.12) dont", r"\textup{(\textbf{II}, 8.14.12)} dont",
    "Conventions 2 and 6 together.")
add(104, "Proposition (2.3.4) (i): 'est un (TN)-isomorphisme.'",
    "(TN) bold upright in the italic statement", r"\textbf{(TN)} (bold italic in the environment)",
    "convention", 6, "high",
    r"est un \textbf{(TN)}-isomorphisme.", r"est un \textup{\textbf{(TN)}}-isomorphisme.",
    "Bold (TN) printed upright in the italic statement.")
c2(104, "Proof of (2.3.4) (i): 'a été vu en (II, 8.14.14)'", "(II, 8.14.14)", old="en (II, 8.14.14)",
   new=r"en (\textbf{II}, 8.14.14)")
c2(104, "Proof of (2.3.4) (i)", "(II, 4.6.18)")
c2(104, "Proof of (2.3.4) (i): 'Module de type fini (II, 8.14.14)'", "(II, 8.14.14)", old="fini¶(II, 8.14.14)",
   new=r"fini¶(\textbf{II}, 8.14.14)")
add(104, "Proof of (2.3.4) (i): 'quasi-cohérent de type fini en vertu de (II, 2.1.6, (ii))'",
    "de type fini en vertu de (no comma)", "de type fini, en vertu de",
    "punctuation", None, "high",
    "de type fini, en vertu de", "de type fini en vertu de",
    "Enlarged crop: no comma.")
c2(104, "Proof of (2.3.4) (i)", "(II, 2.1.6, (ii))")
add(104, "Proof of (2.3.4) (i): '(II, 2.1.6, (ii)), la question étant locale; comme O_X est cohérent'",
    "(ii)), la question étant locale; comme", "(ii))~; la question étant locale, comme",
    "punctuation", None, "high",
    "~; la question étant locale, comme", ", la question étant locale~; comme",
    "Comma and semicolon are interchanged in the TeX.")
c2(104, "Proof of (2.3.4) (ii)", "(II, 4.6.11)")
c2(104, "Proof of (2.3.4) (ii)", "(II, 3.1.8 et 3.2.9)")

# ---------------------------------------------------------------- page 105
add(105, "(2.3.4.1), heading and statement",
    "'Proposition (2.3.4.1). — Soient Y ...' with the statement in italics",
    r"\begin{env}[2.3.4.1]: bold number only, statement roman",
    "other", None, "high",
    r"\begin{env}[2.3.4.1]", r"\begin{proposition}[2.3.4.1]",
    r"Must be applied together with the next finding (\end{env} -> \end{proposition}).")
add(105, "(2.3.4.1), end of the statement", "end of the italic Proposition", r"\end{env}",
    "other", None, "high",
    r"\end{env}", r"\end{proposition}",
    r"Pairs with the previous finding (\begin{env}[2.3.4.1] -> \begin{proposition}[2.3.4.1]).")
c2(105, "Proof of (2.3.4.1), 1st sentence", "(II, 5.4.4 et 4.4.7)")
add(105, "Proof of (2.3.4.1): 'où T est une O_Y-Algèbre quasi-cohérente telle que T_1 soit un O_Y-Module de type fini et engendre T, et l'on a L=r'^*(O_P'(1))'",
    "quasi-cohérente telle que T_1 soit un O_Y-Module de type fini et engendre T, et l'on a L=...",
    "quasi-cohérente, T_1 est de type fini et engendre T, et L=...",
    "word", None, "high",
    r"quasi-cohérente,¶$\mathcal T_1$ est de type fini et engendre $\mathcal T$, et¶$\mathcal L=r'^*",
    r"quasi-cohérente telle que¶$\mathcal T_1$ soit un $\mathcal O_Y$-Module de type fini et engendre $\mathcal T$, et l'on a¶$\mathcal L=r'^*",
    "The TeX paraphrases this proof (pp. 105, lines 20-58 and 99-107 of the page file); the findings below restore the printed wording piece by piece.")
add(105, "Proof of (2.3.4.1): 'On a alors S=⊕ q'_*(O_P'(n)), où q' : P'->Y est le morphisme structural, et il résulte de (2.3.1) que pour n assez grand, l'homomorphisme canonique'",
    "On a alors S=⊕_{n≥0} q'_*(O_P'(n)), où q' : P'->Y est le morphisme structural, et il résulte de (2.3.1) que pour n assez grand, l'homomorphisme canonique",
    "Si q' : P'->Y est le morphisme structural, on a S=⊕ q'_*(O_P'(n)). En vertu de (2.3.1), l'homomorphisme canonique",
    "word", None, "high",
    r"$. Si $q':P'\to Y$ est le morphisme¶structural, on a¶\[¶\mathcal S=\bigoplus_{n\geq0}q'_*(\mathcal O_{P'}(n)).¶\]¶En vertu de (\hyperref[III.2.3.1-fr]{2.3.1}), l'homomorphisme canonique¶",
    r"$. On a alors¶\[¶\mathcal S=\bigoplus_{n\geq0}q'_*(\mathcal O_{P'}(n)),¶\]¶où $q':P'\to Y$ est le morphisme¶structural, et il résulte de (\hyperref[III.2.3.1-fr]{2.3.1}) que pour $n$ assez grand, l'homomorphisme canonique¶",
    "Printed wording restored (the display may stay).")
add(105, "Proof of (2.3.4.1): 'α_n : T_n -> S_n = q_*(L^⊗n) est bijectif;'",
    "α_n : T_n -> S_n=q_*(L^{⊗n}) est bijectif; ('bijectif' italic; 'pour n assez grand' stands earlier)",
    r"$\alpha_n:\mathcal T_n\to\mathcal S_n=q'_*(\mathcal O_{P'}(n))$ est bijectif pour $n$ assez grand~;",
    "formula", None, "high",
    r"$\alpha_n:\mathcal T_n\to\mathcal S_n=q'_*(\mathcal O_{P'}(n))$ est¶bijectif pour $n$ assez grand~;",
    r"$\alpha_n:\mathcal T_n\to\mathcal S_n=q_*(\mathcal L^{\otimes n})$ est¶\emph{bijectif}~;",
    "Formula, italics and word order of the print; 'pour n assez grand' is restored by the previous finding.")
add(105, "Proof of (2.3.4.1): 'En outre, comme l'homomorphisme canonique α : T -> S'",
    "En outre, comme l'homomorphisme", "En outre, l'homomorphisme",
    "missing", None, "high",
    "En outre, l'homomorphisme canonique", "En outre, comme l'homomorphisme canonique",
    "Word 'comme' missing.")
add(105, "Proof of (2.3.4.1): 'est un (TN)-isomorphisme, Φ=Proj(α) : Proj(S)->Proj(T) est un isomorphisme'",
    "(TN)-isomorphisme, Φ=Proj(α) ...", r"\textbf{(TN)}-isomorphisme~; par suite Φ=...",
    "word", None, "high",
    r"\textbf{(TN)}-isomorphisme~; par suite¶", r"\textbf{(TN)}-isomorphisme,¶",
    r"No '; par suite' in the print. The \phantomsection\label that follows stays.")
c2(105, "Proof of (2.3.4.1): 'est un isomorphisme (II, 3.6.1)'", "(II, 3.6.1)")
add(105, "Proof of (2.3.4.1): '(II, 3.6.1) et on a Φ_*(S̃(n))=(S(n))~_[α] (II, 3.5.2)'",
    "(II, 3.6.1) et on a Φ_*(S̃(n)) = (S(n))~_[α] (II, 3.5.2)",
    "(II, 3.6.1). En outre, il résulte de (II, 3.5.2) et du fait que ...",
    "word", None, "high",
    ". En outre, il résulte de ",
    r" et on a¶$\Phi_*(\widetilde{\mathcal S}(n))=(\mathcal S(n))\supertilde_{[\alpha]}$ ",
    r"The print states the formula Φ_*(S̃(n)) = (S(n))~_[α] (tilde after the parenthesis, subscript [α]; \supertilde as in FIX_POLICY 2.5) before (II, 3.5.2).")
c2(105, "Proof of (2.3.4.1): 'Φ_*(S̃(n))=(S(n))~_[α] (II, 3.5.2)'", "(II, 3.5.2)")
add(105, "Proof of (2.3.4.1): '; mais comme les T-Modules gradués (S(n))_[α] et T(n) sont (TN)-isomorphes, on a Φ_*(O_P(n))=O_P'(n)'",
    "(II, 3.5.2); mais comme les T-Modules gradués (S(n))_[α] et T(n) sont (TN)-isomorphes, on a",
    "(II, 3.5.2) et du fait que les T-Modules gradués obtenus à partir des S(n) par restriction des scalaires sont (TN)-isomorphes aux T(n) que",
    "word", None, "high",
    r" et¶du fait que les $\mathcal T$-Modules gradués obtenus à partir des¶$\mathcal S(n)$ par restriction des scalaires sont \textbf{(TN)}-isomorphes¶aux $\mathcal T(n)$ que¶",
    r"~; mais comme¶les $\mathcal T$-Modules gradués $(\mathcal S(n))_{[\alpha]}$ et $\mathcal T(n)$ sont \textbf{(TN)}-isomorphes, on a¶",
    "Printed wording restored.")
c2(105, "Proof of (2.3.4.1): 'pour tout n (II, 3.4.2)'", "(II, 3.4.2)")
add(105, "Proof of (2.3.4.1): '(II, 3.4.2); pour achever de prouver (2.3.4.1)'",
    "(II, 3.4.2); pour achever", "(II, 3.4.2). Pour achever",
    "punctuation", None, "high",
    "). Pour achever de prouver", ")~; pour achever de prouver",
    "Semicolon and lower-case 'pour' in the print.")
add(105, "Proof of (2.3.4.1): 'sont des O_Y-Modules cohérents en vertu de (2.2.1)'",
    "'cohérents' italic", "upright", "italics", None, "high",
    r"$\mathcal O_Y$-Modules cohérents en vertu de", r"$\mathcal O_Y$-Modules \emph{cohérents} en vertu de",
    "Enlarged crop: italic in the print.")
add(105, "Proof of (2.3.4.1): '(2.2.1) et comme S_1^n=S_n pour n≥n_0'",
    "(2.2.1) et comme S_1^n=S_n pour n≥n_0,", r"(2.2.1), et si $\mathcal S_n=\mathcal S_1^n$ pour $n\geq n_0$,",
    "word", None, "high",
    r"{2.2.1}), et si¶$\mathcal S_n=\mathcal S_1^n$ pour", r"{2.2.1}) et comme¶$\mathcal S_1^n=\mathcal S_n$ pour",
    "Words, punctuation and the order of the two sides of the equation as printed.")
add(105, "Proof of (2.3.4.1): 'qui est cohérent, d'où notre assertion'",
    "qui est cohérent, d'où", "qui est cohérent~; d'où",
    "punctuation", None, "high",
    "qui est cohérent~;¶d'où", "qui est cohérent,¶d'où",
    "Comma in the print.")
c2(105, "Proof of (2.3.4.1), end", "(I, 9.6.2)")
c2(105, "End of the proof of (2.3.4): 'de type fini (II, 8.14.12)'", "(II, 8.14.12)")
c2(105, "End of the proof of (2.3.4): 'par suite (II, 8.14.8)'", "(II, 8.14.8)")
add(105, "End of the proof of (2.3.4): 'q''_*((F^(k))_n)=q_*((S'^(d,k))_n) et pour n≥0, ce dernier'",
    "... _n) et pour n≥0, ce dernier", "... _n)$, et pour $n\\geq0$ ce dernier",
    "punctuation", None, "high",
    r"_n)$, et pour¶$n\geq0$ ce dernier", r"_n)$ et pour¶$n\geq0$, ce dernier",
    "Enlarged crop: the comma stands after n≥0, not before 'et'.")
add(105, "End of the proof of (2.3.4): 'est un (TN)-isomorphisme, donc (II, 3.4.2) on a Proj(S^(d,k)) = ...'",
    "(TN)-isomorphisme, donc (II, 3.4.2) on a", r"\textbf{(TN)}-isomorphisme~; donc",
    "missing", None, "high",
    r"\textbf{(TN)}-isomorphisme~; donc¶", r"\textbf{(TN)}-isomorphisme, donc (\textbf{II}, 3.4.2) on a¶",
    "Comma for the semicolon and the missing reference '(II, 3.4.2) on a' (bold II, convention 2).")
add(105, "End of the proof of (2.3.4): 'r''^*(Proj(S^(d,k))) = S'^(d,k)'",
    "= (equality sign)", r"\simeq",
    "symbol", None, "high",
    r"\simeq\mathcal S'^{(d,k)}", r"=\mathcal S'^{(d,k)}",
    "Enlarged crop: an equality sign in the print.")
add(105, "End of the proof of (2.3.4): 'Il reste à remarquer que Proj(S^(d,k)) = s_*((Proj(S))^(d,k)) à un isomorphisme canonique près (II, 8.14.13.1)'",
    "remarquer que [formula] à un isomorphisme canonique près (II, 8.14.13.1)",
    "remarquer que, à un isomorphisme canonique près, [formula] (II, 8.14.13.1)",
    "word", None, "high",
    "remarquer que, à un isomorphisme canonique près,¶", "remarquer que¶",
    "Word order: the phrase follows the formula in the print (next finding puts it there).")
add(105, "End of the proof of (2.3.4): 's_*((Proj(S))^(d,k)) à un isomorphisme canonique près (II, 8.14.13.1)'",
    "... ^(d,k)) à un isomorphisme canonique près (II, 8.14.13.1)", r"\] (II, 8.14.13.1)",
    "word", None, "high",
    "\\]¶(", "\\]¶à un isomorphisme canonique près (",
    "Pairs with the previous finding (the phrase moves behind the formula).")
c2(105, "End of the proof of (2.3.4)", "(II, 8.14.13.1)")
add(105, "End of the proof of (2.3.4): 'et de S'. Enfin, en vertu de (2.3.2)'",
    "no paragraph break before 'Enfin'", "blank line (new paragraph)",
    "other", None, "high",
    r"et de $\mathcal S'$.¶¶Enfin", r"et de $\mathcal S'$.¶Enfin",
    "Paragraph break the print does not have.")
add(105, "End of the proof of (2.3.4): 'en outre, comme les S'_n sont cohérents, il en est de même des S_n=q_*(S'_n) par (2.2.1), et on en conclut aussitôt'",
    "en outre, comme les S'_n sont cohérents, il en est de même des S_n=q_*(S'_n) par (2.2.1), et on en conclut aussitôt",
    "en outre, les S_n=q_*(S'_n) sont cohérents en vertu de (2.2.1), puisque les S'_n sont cohérents. On en conclut aussitôt",
    "word", None, "high",
    r"en outre, les¶$\mathcal S_n=q_*(\mathcal S'_n)$ sont cohérents en vertu de¶(\hyperref[III.2.2.1-fr]{2.2.1}), puisque les $\mathcal S'_n$ sont¶cohérents. On en conclut aussitôt",
    r"en outre, comme les $\mathcal S'_n$¶sont cohérents, il en est de même des $\mathcal S_n=q_*(\mathcal S'_n)$ par¶(\hyperref[III.2.2.1-fr]{2.2.1}), et on en conclut aussitôt",
    "Printed wording restored.")
add(105, "End of the proof of (2.3.4): 'Modules de type fini. Comme on a vu dans (2.3.4.1) que S^(d) est une O_Y-Algèbre de type fini, on en conclut bien que S est aussi une O_Y-Algèbre de type fini.'",
    "... de type fini. Comme on a vu dans (2.3.4.1) que S^(d) est une O_Y-Algèbre de type fini, on en conclut bien que S est aussi une O_Y-Algèbre de type fini.",
    "... de type fini; comme (2.3.4.1) montre que S^(d) est une O_Y-Algèbre de type fini, il en est de même de S.",
    "word", None, "high",
    r"$\mathcal S^{(d)}$-Modules de type fini~; comme¶(\hyperref[III.2.3.4.1-fr]{2.3.4.1}) montre que $\mathcal S^{(d)}$ est une¶$\mathcal O_Y$-Algèbre de type fini, il en est de même de $\mathcal S$.",
    r"$\mathcal S^{(d)}$-Modules de type fini. Comme on a vu dans¶(\hyperref[III.2.3.4.1-fr]{2.3.4.1}) que $\mathcal S^{(d)}$ est une¶$\mathcal O_Y$-Algèbre de type fini, on en conclut bien que $\mathcal S$ est aussi une¶$\mathcal O_Y$-Algèbre de type fini.",
    "Printed wording restored.")

# ---------------------------------------------------------------- page 106
add(106, "Proposition (2.3.5), statement: 'f : X->Y un morphisme projectif birationnel.'",
    "'projectif birationnel' roman inside the italic statement (enlarged crop)", "italic (environment)",
    "convention", 6, "high",
    "morphisme projectif birationnel.", r"morphisme \textup{projectif birationnel}.",
    "Roman words inside the italic statement.")
add(106, "Proposition (2.3.5), statement: 'J ⊂ R(Y) (II, 8.1.2)'",
    "(II, 8.1.2): bold II, upright inside the italic statement", "(II, 8.1.2) plain, italic",
    "convention", 2, "high", "(II, 8.1.2)", r"\textup{(\textbf{II}, 8.1.2)}", "Conventions 2 and 6 together.")
add(106, "Proposition (2.3.5), statement: 'en faisant éclater J (II, 8.1.3)'",
    "(II, 8.1.3): bold II, upright inside the italic statement", "(II, 8.1.3) plain, italic",
    "convention", 2, "high", "(II, 8.1.3)", r"\textup{(\textbf{II}, 8.1.3)}", "Conventions 2 and 6 together.")
add(106, "Proposition (2.3.5), statement: 'sur U (cf. I, 6.5.5)'",
    "(cf. I, 6.5.5): bold I, upright inside the italic statement", "(cf. I, 6.5.5) plain, italic",
    "convention", 2, "high", "(cf. I, 6.5.5)", r"\textup{(cf. \textbf{I}, 6.5.5)}", "Conventions 2 and 6 together.")
c2(106, "Proof of (2.3.5)", "(II, 4.4.2 et 5.3.2)")
c2(106, "Proof of (2.3.5)", "(I, 7.4.5)")
c2(106, "Proof of (2.3.5)", "(I, 7.4.1)")
c2(106, "Proof of (2.3.5)", "(I, 7.3.6)")
add(106, "Proof of (2.3.5): 'mais si on identifie S ⊗_O_Y R(Y) à R(Y)[T]'",
    "si on identifie S⊗_{O_Y}R(Y) à R(Y)[T]", "si on identifie ce dernier faisceau à R(Y)[T]",
    "word", None, "high",
    "si on identifie ce dernier¶faisceau à", r"si on identifie $\mathcal S\otimes_{\mathcal O_Y}\mathcal R(Y)$¶à",
    "The print repeats the formula.")
add(106, "Proof of (2.3.5): 'l'image de f_*(L) s'identifie à J.T'",
    "J.T (dot between J and T; enlarged crop)", r"$\mathcal J T$",
    "formula", None, "high", r"$\mathcal J T$", r"$\mathcal J.T$", "Dot in the print.")
add(106, "Corollaire (2.3.6), statement: 'Sous les hypothèses de (2.3.5), supposons'",
    "(2.3.5) upright inside the italic statement", "(2.3.5) italic",
    "convention", 6, "high",
    r"hypothèses de (\hyperref[III.2.3.5-fr]{2.3.5}), supposons",
    r"hypothèses de \textup{(\hyperref[III.2.3.5-fr]{2.3.5})}, supposons",
    "Reference printed roman inside the italic statement.")
add(106, "Corollaire (2.3.6), statement: 'dans l'énoncé de (2.3.5), on peut supposer'",
    "(2.3.5) upright inside the italic statement", "(2.3.5) italic",
    "convention", 6, "high",
    r"l'énoncé de (\hyperref[III.2.3.5-fr]{2.3.5}), on peut",
    r"l'énoncé de \textup{(\hyperref[III.2.3.5-fr]{2.3.5})}, on peut",
    "Reference printed roman inside the italic statement.")
c2(106, "Proof of (2.3.6), first line", r"(0\textsubscript{I}, 5.4.2)")
add(106, "Proof of (2.3.6): 'du corps des fractions (R(Y))_y de O_y'",
    "(R(Y))_y (enlarged crop)", r"$\mathcal R(Y)_y$",
    "formula", None, "high", r"$\mathcal R(Y)_y$", r"$(\mathcal R(Y))_y$", "Outer parentheses in the print.")
c2(106, "Proof of (2.3.6)", "(I, 7.1.5)")
c2(106, "Proof of (2.3.6)", "(II, 3.1.8)")
add(106, "Proof of (2.3.6): 'Si L est un O_Y-module ample'",
    "O_Y-module (lower-case m; enlarged crop)", r"$\mathcal O_Y$-Module (silently corrected)",
    "misprint_in_print", None, "high",
    r"$\mathcal O_Y$-Module ample, il", r"$\mathcal O_Y$-module ample, il",
    "The statement of (2.3.6) has 'O_Y-Module ample'; the print's lower-case 'module' in the proof is a slip. The fix restores the printed reading.",
    corrected=r"$\mathcal O_Y$-Module")
c2(106, "Proof of (2.3.6), end", "(II, 4.5.5)")

# ---------------------------------------------------------------- macro outside these pages
add(96, r"Definition of \shProj (ega3-1-fr.tex, before \oldpage[III]{97}); all 16 uses are on pp. 102-105",
    "the sheaf Proj printed as script P + italic 'roj' (pp. 102-105, e.g. q_*(Proj_0(M(n))) on p. 102; enlarged crop)",
    r"\shProj = \mathcal{P}\mathrm{roj} (upright roj)",
    "font", None, "high",
    r"\providecommand{\shProj}{\mathcal{P}\mathrm{roj}}", r"\providecommand{\shProj}{\mathcal{P}\mathit{roj}}",
    r"One change covers the 16 uses (2 on p. 102, 3 on p. 103, 4 on p. 104, 7 on p. 105), same reading as the EGA II page fixes \mathcal{P}\mathit{roj} (GLOBAL_ISSUES 31). This line lies in the p. 96 segment, outside this run's pages.")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("findings written:", len(F))

# ---------------------------------------------------------------- checks
def rd(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


pages = {n: rd(n) for n in (96, 101, 103, 104, 105, 106, 107)}
bad = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    p = x["page"]
    src = pages[101] if p == 102 else pages[p]
    c = src.count(x["fix"]["old"])
    if p == 102:  # must also lie in the printed p. 102 part of page_101.tex
        part = src.split(r"telle que les supports de $\mathcal F$", 1)[1]
        if part.count(x["fix"]["old"]) != 1:
            bad += 1
            print("NOT IN p. 102 part:", i, repr(x["fix"]["old"][:60]))
    if c != 1:
        bad += 1
        print("NOT UNIQUE in page file:", i, p, c, repr(x["fix"]["old"][:60]))
print("uniqueness check in page files: problems =", bad)

# simulate apply_fixes.py in list order on the concatenated pages (markers split segments)
body = "".join(re.sub(r"^% from [^\n]*\n", "", pages[n]) for n in (96, 101, 103, 104, 105, 106, 107))
marker = re.compile(r"\\oldpage\[III\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for k, (n, st) in enumerate(cuts):
        if n == page:
            return st, cuts[k + 1][1] if k + 1 < len(cuts) else len(t)
    return None, None


fails = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    st, en = locate(body, x["page"])
    if st is None:
        print("SIM: page not found", i, x["page"]); fails += 1; continue
    seg = body[st:en]
    if seg.count(x["fix"]["old"]) != 1:
        print("SIM: old occurs", seg.count(x["fix"]["old"]), "times", i, x["page"], repr(x["fix"]["old"][:60])); fails += 1; continue
    body = body[:st] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + body[en:]
print("simulation failures:", fails)
(RUN / "crops_101_106" / "sim_result.txt").write_text(body, encoding="utf-8")
