"""Build findings_148_152.json and check every fix's old string (helper for pp. 148-152)."""
import json, sys
sys.stdout.reconfigure(encoding='utf-8')

RUN = r'user\Documents\ega_scan_check_20261101\run_III1'
OUT = RUN + r'\findings_148_152.json'
NL = '¶'   # newline placeholder in the strings below


def s(x):
    return None if x is None else x.replace(NL, '\n')


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if kind == 'misprint_in_print':
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


def c2(page, where, numeral, old, new, inside_italic=False):
    note = "Bold %s in the reference to chapter %s." % (numeral, numeral)
    if inside_italic:
        note = "One edit for this finding and the next (convention 6): bold numeral and the upright reference together."
    add(page, where, "(%s, ...): bold %s" % (numeral, numeral), old.replace(NL, ' '), 'convention', 2, 'high',
        old, new, note)


# ---------------------------------------------------------------- page 148
add(148, "Top of page: 'définit donc un | Y_n-préschéma fini' (the sentence runs on from p. 147)",
    "no paragraph break at the page boundary", "blank lines before and after \\oldpage[III]{148} (paragraph break)",
    'marker', None, 'high',
    r"\oldpage[III]{148}¶¶$Y_n$-préschéma", r"\oldpage[III]{148}¶$Y_n$-préschéma",
    "GLOBAL_ISSUES item 20. Apply together with the removal of the blank line before the marker, which lies in "
    "p. 147's segment: 'définit donc un\\n\\n\\oldpage[III]{148}' -> 'définit donc un\\n\\oldpage[III]{148}'.")
c2(148, "Proof of (4.8.7), line 1: 'Spec(𝒜_n) (II, 6.1.3)'", 'II', r"(II, 6.1.3)", r"(\textbf{II}, 6.1.3)")
c2(148, "Proof of (4.8.7): 'comme on le voit aussitôt (II, 1.4.6)'", 'II', r"(II, 1.4.6)", r"(\textbf{II}, 1.4.6)")
add(148, "Proof of (4.8.7): 'Le préschéma formel 𝔛, limite inductive du système inductif (X_n)'",
    "Le préschéma formel X (roman capital X, not Fraktur)", "$\\mathfrak X$ (silently corrected)",
    'misprint_in_print', None, 'high',
    r"préschéma formel $\mathfrak X$, limite inductive", r"préschéma formel $X$, limite inductive",
    "Enlarged crops: a roman X of the same face as X_n in the same sentence, not the Fraktur 𝔛 of (4.8.7) and "
    "(4.8.8). The formal prescheme of (4.8.7) is 𝔛. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"préschéma formel $\mathfrak X$, limite inductive")
add(148, "Proof of (4.8.7): 'le morphisme structural f : 𝔛→𝔜, limite inductive du système (f_n)'",
    "f : X→Y (roman X and Y)", "$f:\\mathfrak X\\to\\mathfrak Y$ (silently corrected)",
    'misprint_in_print', None, 'high',
    r"$f:\mathfrak X\to\mathfrak Y$, limite inductive", r"$f:X\to Y$, limite inductive",
    "Enlarged crop: both letters are roman capitals; the structure morphism of the formal prescheme 𝔛 over 𝔜 is "
    "meant. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$f:\mathfrak X\to\mathfrak Y$, limite inductive")
c2(148, "Proof of (4.8.7): '(4.8.1 et II, 10.12.3.1)'", 'II', r"et II, 10.12.3.1)", r"et \textbf{II}, 10.12.3.1)")
add(148, "Proof of (4.8.7): 'que f_*(𝒪_𝔛) est limite projective des 𝒜_n'",
    "f_*(𝒪_X) (roman X in the subscript)", "$f_*(\\mathcal O_{\\mathfrak X})$ (silently corrected)",
    'misprint_in_print', None, 'high',
    r"$f_*(\mathcal O_{\mathfrak X})$ est limite", r"$f_*(\mathcal O_X)$ est limite",
    "Enlarged crop (4x): the subscript is a roman X, as in the two preceding misprints of this proof; 𝒪_𝔛 is meant. "
    "The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$f_*(\mathcal O_{\mathfrak X})$ est limite")
c2(148, "Proof of (4.8.7): 'donc égale à 𝒜 (I, 10.10.6)'", 'I', r"(I, 10.10.6)", r"(\textbf{I}, 10.10.6)")
add(148, "Proposition (4.8.8): 'Il existe une bijection canonique de Hom_𝔜(𝔛, 𝔛') sur Hom_{𝒪_𝔜}(...) (1).'",
    "the formula is set inline in the statement", "displayed with \\[ ... \\]", 'other', None, 'high',
    r"bijection canonique de¶\[¶\operatorname{Hom}_{\mathfrak Y}(\mathfrak X,\mathfrak X')¶\quad\hbox{sur}\quad¶"
    r"\operatorname{Hom}_{\mathcal O_{\mathfrak Y}}¶\bigl(f'_*(\mathcal O_{\mathfrak X'}),f_*(\mathcal O_{\mathfrak X})\bigr)¶"
    r"\footnotemark.¶\]",
    r"bijection canonique de¶$\operatorname{Hom}_{\mathfrak Y}(\mathfrak X,\mathfrak X')$¶sur¶"
    r"$\operatorname{Hom}_{\mathcal O_{\mathfrak Y}}¶\bigl(f'_*(\mathcal O_{\mathfrak X'}),f_*(\mathcal O_{\mathfrak X})\bigr)$"
    r"\footnotemark.",
    "Layout: the print sets both Hom sets inline in the italic statement, followed by the footnote mark and the full stop.")
add(148, "Footnote (1) to (4.8.8): 'l'ensemble des homomorphismes de 𝒪_𝔜-Algèbres'",
    "'Algèbres' in italics", "upright 'Algèbres'", 'italics', None, 'high',
    r"des homomorphismes de¶$\mathcal O_{\mathfrak Y}$-Algèbres",
    r"des homomorphismes de¶$\mathcal O_{\mathfrak Y}$-\emph{Algèbres}",
    "Enlarged crop: only 'Algèbres' is italic in the roman footnote.")
c2(148, "Proof of (4.8.8): 'est la même que dans (II, 1.1.2)'", 'II', r"(II, 1.1.2)", r"(\textbf{II}, 1.1.2)")
c2(148, "Proof of (4.8.8): 'homomorphismes d'algèbres (I, 10.2.2)'", 'I', r"(I, 10.2.2)", r"(\textbf{I}, 10.2.2)")
c2(148, "Proof of (4.8.8): 'A'^Δ→A^Δ (I, 10.10.2.3)'", 'I', r"(I, 10.10.2.3)", r"(\textbf{I}, 10.10.2.3)")
add(148, "Corollaire (4.8.9): 'définie dans (4.8.8), les immersions fermées'",
    "(4.8.8) upright inside the italic statement",
    "(\\hyperref[III.4.8.8-fr]{4.8.8}) inside the italic corollary environment: italic", 'convention', 6, 'high',
    r"(\hyperref[III.4.8.8-fr]{4.8.8}), les immersions",
    r"\textup{(\hyperref[III.4.8.8-fr]{4.8.8})}, les immersions",
    "Enlarged crop: roman old-style figures and upright parentheses.")
c2(148, "Proof of (4.8.9): 'préschémas formels localement noethériens (I, 10.14.2)'", 'I',
   r"(I, 10.14.2)", r"(\textbf{I}, 10.14.2)")
add(148, "Corollaire (4.8.10): 'Les notations et hypothèses étant celles de (4.8.1), pour qu'un'",
    "(4.8.1) upright inside the italic statement",
    "(\\hyperref[III.4.8.1-fr]{4.8.1}) inside the italic corollary environment: italic", 'convention', 6, 'high',
    r"(\hyperref[III.4.8.1-fr]{4.8.1}), pour qu'un",
    r"\textup{(\hyperref[III.4.8.1-fr]{4.8.1})}, pour qu'un",
    "Enlarged crop: roman old-style figures and upright parentheses.")
c2(148, "Proof of (4.8.10): 'Modules cohérents (I, 10.11.5)'", 'I', r"(I, 10.11.5)", r"(\textbf{I}, 10.11.5)")
add(148, "End of page: 'de préschémas formels localement | noethériens' ((4.8.11) runs on to p. 149)",
    "no paragraph break at the page boundary", "blank line before \\oldpage[III]{149} (with the blank line after it: paragraph break)",
    'marker', None, 'high',
    r"de préschémas formels localement¶¶", r"de préschémas formels localement¶",
    "GLOBAL_ISSUES item 20. Apply together with the p. 149 fix that removes the blank line after \\oldpage[III]{149}.")

# ---------------------------------------------------------------- page 149
add(149, "Top of page: 'localement | noethériens soit fini' (Proposition (4.8.11) runs on from p. 148)",
    "no paragraph break at the page boundary", "blank line after \\oldpage[III]{149} (paragraph break)",
    'marker', None, 'high',
    r"\oldpage[III]{149}¶¶noethériens", r"\oldpage[III]{149}¶noethériens",
    "GLOBAL_ISSUES item 20. Apply together with the p. 148 fix that removes the blank line before the marker.")
add(149, "(5.1.1): 'Soient A un anneau adique noethérien, 𝔍 un idéal'",
    "'adique noethérien' in italics", "upright", 'italics', None, 'high',
    r"anneau adique noethérien, $\mathfrak J$", r"anneau \emph{adique noethérien}, $\mathfrak J$",
    "Enlarged crop.")
add(149, "(5.1.1): 'Spf(A) s'identifie au complété Ŷ de Y'",
    "'complété' in italics", "upright", 'italics', None, 'high',
    r"s'identifie au complété $\widehat Y$", r"s'identifie au \emph{complété} $\widehat Y$",
    "Enlarged crop.")
c2(149, "(5.1.1): 'Y'=V(𝔍) (I, 10.10.1)'", 'I', r"(I, 10.10.1)", r"(\textbf{I}, 10.10.1)")
add(149, "(5.1.1): 'nous désignerons par X̂ le complété de X le long de la partie fermée'",
    "'complété' in italics", "upright", 'italics', None, 'high',
    r"le complété de $X$ le long", r"le \emph{complété} de $X$ le long",
    "The later 'son complété, ℱ_{/X'}' is roman in the print and stays as it is.")
add(149, "Proposition (5.1.2): 'étant celles de (5.1.1), soit ℱ'",
    "(5.1.1) upright inside the italic statement",
    "(\\hyperref[III.5.1.1-fr]{5.1.1}) inside the italic proposition environment: italic", 'convention', 6, 'high',
    r"(\hyperref[III.5.1.1-fr]{5.1.1}), soit", r"\textup{(\hyperref[III.5.1.1-fr]{5.1.1})}, soit",
    "Enlarged crop.")
c2(149, "Proposition (5.1.2): 'dont le support est propre sur Y (II, 5.4.10)'", 'II',
   r"(II, 5.4.10)", r"\textup{(\textbf{II}, 5.4.10)}", inside_italic=True)
add(149, "Proposition (5.1.2): '(II, 5.4.10)'", "the reference is upright inside the italic statement",
    "(II, 5.4.10) inside the italic proposition environment: italic", 'convention', 6, 'high', None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(149, "Proposition (5.1.2): 'Les homomorphismes canoniques (4.1.4)'",
    "(4.1.4) upright inside the italic statement", "(4.1.4) inside the italic proposition environment: italic",
    'convention', 6, 'high',
    r"canoniques (4.1.4)", r"canoniques \textup{(4.1.4)}", "Enlarged crop.")
add(149, "Proof of (5.1.2): 'topologie 𝔍-préadique (0_I, 7.3.6)'", "(𝟎_I, 7.3.6): bold 0",
    "($0_{\\mathrm I}$, 7.3.6)", 'convention', 2, 'high',
    r"($0_{\mathrm I}$, 7.3.6)", r"($\mathbf{0}_{\mathrm I}$, 7.3.6)", "Bold 0 in the reference to chapter 0 (GLOBAL_ISSUES item 35).")
add(149, "After (5.1.2): 'de 𝒪_X-Modules cohérents ((0, 12.1.6) et (I, 10.8.9))'", "(𝟎, 12.1.6): bold 0",
    "(($0$, 12.1.6)", 'convention', 2, 'high',
    r"(($0$, 12.1.6)", r"((\textbf{0}, 12.1.6)", "Bold 0 in the reference to chapter 0.")
c2(149, "After (5.1.2): '((0, 12.1.6) et (I, 10.8.9))'", 'I', r"(I, 10.8.9)", r"(\textbf{I}, 10.8.9)")
add(149, "Corollaire (5.1.3): 'fait correspondre son complété û : ℱ̂→𝒢̂, est un isomorphisme'",
    "û : ℱ→𝒢 (no circumflexes on ℱ and 𝒢)", "$\\widehat u:\\widehat{\\mathcal F}\\to\\widehat{\\mathcal G}$ (silently corrected)",
    'misprint_in_print', None, 'high',
    r"$\widehat u:\widehat{\mathcal F}\to\widehat{\mathcal G}$", r"$\widehat u:\mathcal F\to\mathcal G$",
    "Enlarged crop (4x): no accent over ℱ or 𝒢 after û, while û carries its circumflex. The completion of "
    "u : ℱ→𝒢 is a map ℱ̂→𝒢̂. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$\widehat u:\widehat{\mathcal F}\to\widehat{\mathcal G}$")
add(149, "Corollaire (5.1.3): 'pour que û soit injectif (resp. surjectif), il faut'",
    "'resp.' upright (roman) inside the italic statement; 'surjectif' italic",
    "(resp. surjectif) inside the italic corollary environment: all italic", 'convention', 6, 'high',
    r"injectif (resp. surjectif), il faut", r"injectif (\textup{resp.} surjectif), il faut",
    "Enlarged crop. The parentheses look upright too; left to the parenthesis convention (GLOBAL_ISSUES item 26).")
c2(149, "Proof of (5.1.3): 'notons en vertu de (I, 10.8.14)'", 'I', r"(I, 10.8.14)", r"(\textbf{I}, 10.8.14)")
add(149, "End of the proof of (5.1.3): 'La conclusion résulte donc du lemme suivant :'",
    "this sentence is the first line of p. 150, a new indented paragraph; p. 149 ends with '(resp. surjectif).'",
    "the sentence stands before \\oldpage[III]{150}, run on in the same paragraph",
    'marker', None, 'high',
    r"injectif (resp. surjectif). La conclusion¶résulte donc du lemme suivant~:",
    r"injectif (resp. surjectif).¶¶\oldpage[III]{150}¶La conclusion¶résulte donc du lemme suivant~:",
    "Misplaced page marker and missing paragraph break. Apply together with the p. 150 fix that removes the "
    "old marker before \\begin{lemma}[5.1.3.1].")

# ---------------------------------------------------------------- page 150
add(150, "Top of page: \\oldpage[III]{150} before Lemme (5.1.3.1)",
    "p. 150 begins with 'La conclusion résulte donc du lemme suivant :'",
    "marker placed after that sentence and the end of the proof", 'marker', None, 'high',
    r"\oldpage[III]{150}¶¶\begin{lemma}[5.1.3.1]", r"\begin{lemma}[5.1.3.1]",
    "Apply together with the p. 149 fix that inserts \\oldpage[III]{150} before 'La conclusion'.")
add(150, "Lemme (5.1.3.1): 'Sous les hypothèses de (5.1.1), si on suppose'",
    "(5.1.1) upright inside the italic statement",
    "(\\hyperref[III.5.1.1-fr]{5.1.1}) inside the italic lemma environment: italic", 'convention', 6, 'high',
    r"hypothèses de (\hyperref[III.5.1.1-fr]{5.1.1})", r"hypothèses de \textup{(\hyperref[III.5.1.1-fr]{5.1.1})}",
    "Enlarged crop.")
c2(150, "Proof of (5.1.3.1): 'remplacer f par f_red (I, 6.3.4)'", 'I', r"(I, 6.3.4)", r"(\textbf{I}, 6.3.4)")
c2(150, "Proof of (5.1.3.1): 'espace sous-jacent (I, 5.2.2)'", 'I', r"(I, 5.2.2)", r"(\textbf{I}, 5.2.2)")
add(150, "Proof of (5.1.3.1): 'f(X—V) est fermé dans Y'", "X—V with the long dash", "$f(X-V)$",
    'convention', 7, 'high', r"$f(X-V)$", r"$f(X\setmin V)$", "Set difference printed with the long dash.")
add(150, "Proof of (5.1.3.1): 'à moins que X—V ne soit vide'", "X—V with the long dash", "$X-V$",
    'convention', 7, 'high', r"$X-V$ ne soit vide", r"$X\setmin V$ ne soit vide", "Set difference printed with the long dash.")
c2(150, "Proof of (5.1.3.1): '(I, 1.1.15 et 0_I, 7.1.10)'", 'I', r"(I, 1.1.15", r"(\textbf{I}, 1.1.15")
add(150, "Proof of (5.1.3.1): '(I, 1.1.15 et 0_I, 7.1.10)'", "𝟎_I: bold 0", "$0_{\\mathrm I}$",
    'convention', 2, 'high', r"et $0_{\mathrm I}$,¶7.1.10)", r"et $\mathbf{0}_{\mathrm I}$,¶7.1.10)",
    "Bold 0 in the reference to chapter 0 (GLOBAL_ISSUES item 35).")
add(150, "After (5.1.3.1): 'en disant que le foncteur ℱ⇝ℱ̂ est pleinement fidèle'",
    "ℱ ⇝ ℱ̂ (wavy arrow)", "$\\mathcal F\\mapsto\\widehat{\\mathcal F}$", 'symbol', None, 'high',
    r"en disant que le foncteur¶$\mathcal F\mapsto", r"en disant que le foncteur¶$\mathcal F\leadsto",
    "Wavy maps-to arrow in the print (\\leadsto), not convention 3; enlarged crop (GLOBAL_ISSUES item 33).")
add(150, "After (5.1.3.1): 'est pleinement fidèle de la catégorie'", "'pleinement fidèle' in italics", "upright",
    'italics', None, 'high', r"est pleinement fidèle", r"est \emph{pleinement fidèle}", "Enlarged crop.")
add(150, "After (5.1.3.1): 'établit par suite une équivalence de la première'", "'équivalence' in italics", "upright",
    'italics', None, 'high', r"par suite une équivalence de", r"par suite une \emph{équivalence} de", "Enlarged crop.")
add(150, "After (5.1.3.1): 'une sous-catégorie pleine de la seconde'", "'pleine' in italics", "upright",
    'italics', None, 'high', r"sous-catégorie pleine de", r"sous-catégorie \emph{pleine} de", "Enlarged crop.")
add(150, "After (5.1.3.1): 'de la seconde (0, 8.1.6)'", "(𝟎, 8.1.6): bold 0", "($0$, 8.1.6)", 'convention', 2, 'high',
    r"($0$, 8.1.6)", r"(\textbf{0}, 8.1.6)", "Bold 0 in the reference to chapter 0.")
add(150, "After (5.1.3.1): 'la catégorie de tous les 𝒪_X̂-Modules cohérents'", "'tous' in italics", "upright",
    'italics', None, 'high', r"la catégorie de tous les", r"la catégorie de \emph{tous} les", "Enlarged crop.")
add(150, "Théorème (5.1.4): 'le foncteur ℱ⇝ℱ_{/X'}=ℱ̂'", "ℱ ⇝ ℱ_{/X'} (wavy arrow)",
    "$\\mathcal F\\mapsto\\mathcal F_{/X'}$", 'symbol', None, 'high',
    r"$\mathcal F\mapsto\mathcal F_{/X'}", r"$\mathcal F\leadsto\mathcal F_{/X'}",
    "Wavy maps-to arrow in the print (\\leadsto); enlarged crop.")
add(150, "Corollaire (5.1.6): 'Alors le foncteur ℱ⇝ℱ̂ est une équivalence'", "ℱ ⇝ ℱ̂ (wavy arrow)",
    "$\\mathcal F\\mapsto\\widehat{\\mathcal F}$", 'symbol', None, 'high',
    r"Alors le foncteur¶$\mathcal F\mapsto", r"Alors le foncteur¶$\mathcal F\leadsto",
    "Wavy maps-to arrow in the print (\\leadsto); enlarged crop.")
add(150, "(5.1.7), heading: 'Scholie (5.1.7). — Si on tient compte'",
    "Scholie (5.1.7). — (word, then number, then dash)",
    "\\begin{env}[5.1.7] + \\emph{Scholie.}: typesets '(5.1.7) Scholie.'", 'other', None, 'high',
    r"\begin{env}[5.1.7]¶\label{III.5.1.7-fr}¶\emph{Scholie.}¶", r"\begin{scholium}[5.1.7]¶\label{III.5.1.7-fr}¶",
    "The preamble's scholium environment gives 'Scholie (5.1.7). —'. Apply together with the p. 151 fix of the "
    "matching \\end{env}. Same pattern at (2.3.3) and (5.4.2) in ega3-1-fr.tex (see final message).")
c2(150, "(5.1.7): 'sur les préschémas formels (I, 10.11.3)'", 'I', r"(I, 10.11.3)", r"(\textbf{I}, 10.11.3)")
add(150, "(5.1.7): 'de support propre sur Spec(A) équivaut (en posant'", "'équivaut' in italics", "upright",
    'italics', None, 'high', r"équivaut (en posant", r"\emph{équivaut} (en posant", "Enlarged crop.")
add(150, "(5.1.7): 'ℱ_m = ℱ_n ⊗_{Y_n} 𝒪_{Y_m} (ou encore ℱ_m = ℱ_n/𝔍^{m+1}ℱ_n)'",
    "⊗ with subscript Y_n", "\\otimes_{\\mathcal O_{Y_n}}", 'formula', None, 'high',
    r"on ait¶\[¶\mathcal F_m=\mathcal F_n\otimes_{\mathcal O_{Y_n}}\mathcal O_{Y_m}¶"
    r"\quad\text{(ou encore }\mathcal F_m=\mathcal F_n/\mathfrak J^{m+1}\mathcal F_n\text{)}¶\]",
    r"on ait¶$\mathcal F_m=\mathcal F_n\otimes_{Y_n}\mathcal O_{Y_m}$¶"
    r"(ou encore $\mathcal F_m=\mathcal F_n/\mathfrak J^{m+1}\mathcal F_n$)",
    "Enlarged crop: the tensor sign carries the subscript Y_n, not 𝒪_{Y_n}. One edit for this finding and the next "
    "(the formulas are inline in the print).")
add(150, "(5.1.7): 'tel que pour m⩽n on ait ℱ_m = ... (ou encore ...) et que le support'",
    "the formulas are set inline in the running text", "displayed with \\[ ... \\]", 'other', None, 'high', None, None,
    "Covered by the edit of the preceding finding.")
c2(150, "(5.1.7): 'Au moyen de (I, 10.11.4)'", 'I', r"(I, 10.11.4)", r"(\textbf{I}, 10.11.4)")

# ---------------------------------------------------------------- page 151
add(151, "(5.1.7), end: 'A est en fait un anneau adique local noethérien'", "'local' in italics", "upright",
    'italics', None, 'high', r"adique local¶noethérien", r"adique \emph{local}¶noethérien", "Enlarged crop.")
add(151, "(5.1.7), end: 'des spectres d'anneaux artiniens locaux'", "'artiniens locaux' in italics", "upright",
    'italics', None, 'high', r"d'anneaux artiniens locaux", r"d'anneaux \emph{artiniens locaux}", "Enlarged crop.")
add(151, "(5.1.7), end of the scholium: '\\end{env}' after 'anneaux locaux artiniens.'",
    "Scholie (5.1.7). — heading (p. 150)", "env environment closed here", 'other', None, 'high',
    r"artiniens.¶\end{env}", r"artiniens.¶\end{scholium}",
    "Must be applied together with the p. 150 fix \\begin{env}[5.1.7] -> \\begin{scholium}[5.1.7].")
add(151, "Corollaire (5.1.8): 'Sous les conditions de (5.1.4), l'application'",
    "(5.1.4) upright inside the italic statement",
    "(\\hyperref[III.5.1.4-fr]{5.1.4}) inside the italic corollary environment: italic", 'convention', 6, 'high',
    r"(\hyperref[III.5.1.4-fr]{5.1.4}), l'application", r"\textup{(\hyperref[III.5.1.4-fr]{5.1.4})}, l'application",
    "Enlarged crop.")
add(151, "Corollaire (5.1.8): 'l'application Z⇝Ẑ=Z_{/(Z∩X')}'", "Z ⇝ Ẑ (wavy arrow)", "$Z\\mapsto\\widehat Z$",
    'symbol', None, 'high', r"$Z\mapsto\widehat Z", r"$Z\leadsto\widehat Z",
    "Wavy maps-to arrow in the print (\\leadsto); enlarged crop.")
add(151, "Proof of (5.1.8): 'où 𝒜 est un Idéal cohérent de 𝒪_X̂ (I, 10.14.2)'",
    "𝒪_X (no circumflex over the subscript X)", "$\\mathcal O_{\\widehat X}$ (silently corrected)",
    'misprint_in_print', None, 'high',
    r"est un Idéal¶cohérent de $\mathcal O_{\widehat X}$", r"est un Idéal¶cohérent de $\mathcal O_X$",
    "Enlarged crop: no accent over the subscript X (the preceding (𝒪_X̂/𝒜)|T has it). 𝒜 is an Ideal of 𝒪_X̂ "
    "(I, 10.14.2). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"est un Idéal¶cohérent de $\mathcal O_{\widehat X}$")
c2(151, "Proof of (5.1.8): 'Idéal cohérent de 𝒪_X̂ (I, 10.14.2)'", 'I', r"(I, 10.14.2)", r"(\textbf{I}, 10.14.2)")
c2(151, "Proof of (5.1.8): '𝒜 = 𝒩̂ (I, 10.8.8)'", 'I', r"(I, 10.8.8)", r"(\textbf{I}, 10.8.8)")
c2(151, "Proof of (5.1.8): 'd'où la conclusion (I, 10.14.7)'", 'I', r"(I, 10.14.7)", r"(\textbf{I}, 10.14.7)")
add(151, "(5.2.1): 'qu'un 𝒪_X̂-Module cohérent est algébrisable s'il est isomorphe'", "'algébrisable' in italics",
    "upright", 'italics', None, 'high', r"est algébrisable s'il", r"est \emph{algébrisable} s'il", "Enlarged crop.")
add(151, "Proof of (5.2.2): 'l'exactitude du foncteur ℱ⇝ℱ̂'", "ℱ ⇝ ℱ̂ (wavy arrow)",
    "$\\mathcal F\\mapsto\\widehat{\\mathcal F}$", 'symbol', None, 'high',
    r"$\mathcal F\mapsto\widehat{\mathcal F}$", r"$\mathcal F\leadsto\widehat{\mathcal F}$",
    "Wavy maps-to arrow in the print (\\leadsto); 8x crop: the same glyph as on p. 150, weakly inked (wave broken), "
    "not a straight arrow.")
add(151, "Proof of (5.2.2): 'Ker (v̂) est isomorphe à (Ker (v))^ et comme'",
    "(Ker (v))^ : circumflex written after the closing parenthesis", "$\\widehat{\\operatorname{Ker}(v)}$",
    'formula', None, 'high', r"$\widehat{\operatorname{Ker}(v)}$", r"$(\operatorname{Ker}(v))^{\wedge}$",
    "Enlarged crop. Analogue of convention 5 for the circumflex; ^{\\wedge} as in the EGA II p. 194 fix "
    "(GLOBAL_ISSUES item 31, \\superhat macro planned).")
add(151, "Proposition (5.2.3): 'et pour tout 𝒪_𝔛-Module ℱ, ℱ_k = ℱ⊗_{𝒪_𝔛}𝒪_{X_n} = ℱ/𝔍^{k+1}ℱ.'",
    "the formula is set inline in the statement", "displayed with \\[ ... \\]", 'other', None, 'high',
    r"$\mathcal F$,¶\[¶\mathcal F_k=\mathcal F\otimes_{\mathcal O_{\mathfrak X}}\mathcal O_{X_k}¶"
    r"=\mathcal F/\mathfrak J^{k+1}\mathcal F.¶\]",
    r"$\mathcal F$,¶$\mathcal F_k=\mathcal F\otimes_{\mathcal O_{\mathfrak X}}\mathcal O_{X_k}¶"
    r"=\mathcal F/\mathfrak J^{k+1}\mathcal F$.",
    "Layout: inline in the print. Apply this edit before the next one (misprint X_n), whose old string survives it.")
add(151, "Proposition (5.2.3): 'ℱ_k = ℱ⊗_{𝒪_𝔛}𝒪_{X_k} = ℱ/𝔍^{k+1}ℱ'",
    "𝒪_{X_n} (subscript n)", "\\mathcal O_{X_k} (silently corrected)", 'misprint_in_print', None, 'high',
    r"\mathcal O_{X_k}¶=\mathcal F/", r"\mathcal O_{X_n}¶=\mathcal F/",
    "Enlarged crop: the second subscript is n. ℱ⊗𝒪_{X_k} = ℱ/𝔍^{k+1}ℱ is meant (X_k defined just before). "
    "The TeX silently corrects; the fix restores the printed reading. Apply after the preceding inline edit.",
    corrected=r"\mathcal O_{X_k}¶=\mathcal F/")
add(151, "Proposition (5.2.3), item label '(i)'", "label (i) upright", "\\item[(i)] inside the italic proposition environment: italic",
    'convention', 6, 'high', r"\item[(i)] L'homomorphisme", r"\item[\textup{(i)}] L'homomorphisme",
    "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES item 16).")
add(151, "Proposition (5.2.3), item label '(ii)'", "label (ii) upright", "\\item[(ii)] inside the italic proposition environment: italic",
    'convention', 6, 'high', r"\item[(ii)] On a", r"\item[\textup{(ii)}] On a",
    "Roman-numeral item labels are upright in the print (GLOBAL_ISSUES item 16).")
add(151, "Proof of (5.2.3): 'les faisceaux ℳ_k = 𝔍^kℱ/𝔍^{k+1}ℱ étant annulés par 𝔍'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", 'other', None, 'high',
    r"les faisceaux¶\[¶\mathcal M_k=\mathfrak J^k\mathcal F/\mathfrak J^{k+1}\mathcal F¶\]¶étant",
    r"les faisceaux¶$\mathcal M_k=\mathfrak J^k\mathcal F/\mathfrak J^{k+1}\mathcal F$¶étant",
    "Layout: inline in the print.")
add(151, "Proof of (5.2.3): 'Modules cohérents (0_I, 5.3.10)'", "(𝟎_I, 5.3.10): bold 0", "($0_{\\mathrm I}$, 5.3.10)",
    'convention', 2, 'high', r"($0_{\mathrm I}$, 5.3.10)", r"($\mathbf{0}_{\mathrm I}$, 5.3.10)",
    "Bold 0 in the reference to chapter 0 (GLOBAL_ISSUES item 35).")
add(151, "Proof of (5.2.3): 'on voit aussitôt que ℳ_k(n) = 𝔍^kℱ(n)/𝔍^{k+1}ℱ(n). Notons que'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", 'other', None, 'high',
    r"on voit aussitôt que¶\[¶\mathcal M_k(n)=\mathfrak J^k\mathcal F(n)/¶\mathfrak J^{k+1}\mathcal F(n).¶\]",
    r"on voit aussitôt que¶$\mathcal M_k(n)=\mathfrak J^k\mathcal F(n)/¶\mathfrak J^{k+1}\mathcal F(n)$.",
    "Layout: inline in the print.")
add(151, "End of page: 'ample pour f_0 : X_0→Y_0, et | que f_0 est propre' (the sentence runs on to p. 152)",
    "no paragraph break at the page boundary", "blank line before \\oldpage[III]{152} (with the blank line after it: paragraph break)",
    'marker', None, 'high',
    r"pour $f_0:X_0\to Y_0$, et¶¶", r"pour $f_0:X_0\to Y_0$, et¶",
    "GLOBAL_ISSUES item 20. Apply together with the p. 152 fix that removes the blank line after \\oldpage[III]{152}.")

# ---------------------------------------------------------------- page 152
add(152, "Top of page: 'et | que f_0 est propre' (the sentence runs on from p. 151)",
    "no paragraph break at the page boundary", "blank line after \\oldpage[III]{152} (paragraph break)",
    'marker', None, 'high',
    r"\oldpage[III]{152}¶¶que $f_0$ est propre", r"\oldpage[III]{152}¶que $f_0$ est propre",
    "GLOBAL_ISSUES item 20. Apply together with the p. 151 fix that removes the blank line before the marker.")
add(152, "Proof of (5.2.3): 'on en conclut que f_0 est projectif (II, 5.5.4)'", "'projectif' in italics", "upright",
    'italics', None, 'high', r"$f_0$ est projectif", r"$f_0$ est \emph{projectif}", "Enlarged crop.")
c2(152, "Proof of (5.2.3): 'f_0 est projectif (II, 5.5.4)'", 'II', r"(II, 5.5.4)", r"(\textbf{II}, 5.5.4)")
add(152, "Proof of (5.2.3): 'Soit S la A-algèbre graduée ⊕_{k⩾0}𝔍^k/𝔍^{k+1} associée à la filtration'",
    "Soit S la A-algèbre graduée ⊕_{k⩾0} 𝔍^k/𝔍^{k+1} associée (inline, no equals sign)",
    "Soit \\[ S=\\bigoplus_{k\\geq0}\\mathfrak J^k/\\mathfrak J^{k+1} \\] la $A$-algèbre graduée associée",
    'formula', None, 'high',
    r"Soit¶\[¶S=\bigoplus_{k\geq0}\mathfrak J^k/\mathfrak J^{k+1}¶\]¶la $A$-algèbre graduée associée",
    r"Soit $S$ la $A$-algèbre¶graduée $\bigoplus_{k\geq0}\mathfrak J^k/\mathfrak J^{k+1}$ associée",
    "The TeX recasts the sentence as a displayed equation; the print names S first and sets the sum inline after "
    "'graduée'. Index position under ⊕ left as is.")
add(152, "Proof of (5.2.3): 'si on pose 𝒮' = f_0^*(S̃)'",
    "S̃ with a bold upright S (the S of 'Soit S' two lines above is roman)", "\\widetilde S (silently corrected)",
    'misprint_in_print', None, 'medium',
    r"f_0^*(\widetilde S)", r"f_0^*(\widetilde{\mathbf S})",
    "Enlarged crops (6x) of both letters: the S under the tilde is bold (heavier and wider than the roman S of "
    "'Soit S'). Wrong-font letter, recorded as a misprint (GLOBAL_ISSUES item 29); the roman S is meant. The TeX "
    "silently corrects; the fix restores the printed reading.",
    corrected=r"f_0^*(\widetilde S)")
add(152, "Proof of (5.2.3): '𝒮' est une 𝒪_{X_0}-Algèbre ... de type fini, et ℳ = ⊕_{k⩾0}ℳ_k un 𝒮'-Module gradué'",
    "ℳ = ⊕_{k⩾0} ℳ_k stands after 'et', as subject of 'un 𝒮'-Module gradué'; 'si on pose' introduces only 𝒮'",
    "ℳ = ⊕ℳ_k moved into 'si on pose 𝒮'=f_0^*(S̃), ℳ=⊕ℳ_k, 𝒮' est une ...', then 'et ℳ un'",
    'formula', None, 'high',
    r"$\mathcal M=\bigoplus_{k\geq0}\mathcal M_k$, $\mathcal S'$ est une¶$\mathcal O_{X_0}$-Algèbre quasi-cohérente de type fini, et $\mathcal M$ un",
    r"$\mathcal S'$ est une¶$\mathcal O_{X_0}$-Algèbre quasi-cohérente de type fini, et¶$\mathcal M=\bigoplus_{k\geq0}\mathcal M_k$ un",
    "Print: 'si on pose 𝒮'=f_0^*(S̃), 𝒮' est une 𝒪_{X_0}-Algèbre quasi-cohérente de type fini, et ℳ=⊕_{k⩾0}ℳ_k un "
    "𝒮'-Module gradué quasi-cohérent'. Independent of the S̃ edit.")
add(152, "Proof of (5.2.3): 'pour n⩾n_0 et pour tout k, on ait'", "'tout' in italics", "upright",
    'italics', None, 'high', r"et pour tout $k$, on ait", r"et pour \emph{tout} $k$, on ait", "Enlarged crop.")
add(152, "(5.2.3.1): 'H^q(X_0, ℳ_k(n)) = 0    pour tout q>0.'", "'pour tout' in italics", "\\text{pour tout } (upright)",
    'italics', None, 'high', r"\qquad\text{pour tout }q>0.", r"\qquad\text{\emph{pour tout} }q>0.",
    "Enlarged crop; in (5.2.3.3) 'pour ... et' is roman, as in the TeX.")
add(152, "Display after 'Appliquant la suite exacte de cohomologie à'",
    "0 → 𝔍^kℱ(n)/𝔍^{k+1}ℱ(n) → 𝔍^hℱ(n)/𝔍^{k+1}ℱ(n) → 𝔍^hℱ(n)/𝔍^kℱ(n) → 0 (quotients with a slash)",
    "\\frac{...}{...} (built-up fractions)", 'formula', None, 'high',
    r"\frac{\mathfrak J^k\mathcal F(n)}{\mathfrak J^{k+1}\mathcal F(n)}¶\to¶"
    r"\frac{\mathfrak J^h\mathcal F(n)}{\mathfrak J^{k+1}\mathcal F(n)}¶\to¶"
    r"\frac{\mathfrak J^h\mathcal F(n)}{\mathfrak J^k\mathcal F(n)}",
    r"\mathfrak J^k\mathcal F(n)/\mathfrak J^{k+1}\mathcal F(n)¶\to¶"
    r"\mathfrak J^h\mathcal F(n)/\mathfrak J^{k+1}\mathcal F(n)¶\to¶"
    r"\mathfrak J^h\mathcal F(n)/\mathfrak J^k\mathcal F(n)",
    "Enlarged crop. Independent of the next edit (comma).")
add(152, "Display after 'Appliquant la suite exacte de cohomologie à': end", "no punctuation after the final 0",
    "\\to0,", 'punctuation', None, 'high', r"\to0,¶\]¶on en déduit", r"\to0¶\]¶on en déduit",
    "Enlarged crop: the display ends with 0; the text continues 'on en déduit tout d'abord'.")
add(152, "Proof of (5.2.3): 'on a par récurrence sur k—h'", "par récurrence sur h—k",
    "récurrence sur $k-h$ (silently corrected)", 'misprint_in_print', None, 'high',
    r"récurrence sur $k-h$", r"récurrence sur $h-k$",
    "Enlarged crop: h first, then the long dash, then k. Since 0⩽h<k the induction is on k−h. The TeX silently "
    "corrects; the fix restores the printed reading. The long dash is the next finding.",
    corrected=r"récurrence sur $k-h$")
add(152, "Proof of (5.2.3): 'récurrence sur h—k'", "long dash used as the minus sign", "$h-k$ after the preceding fix (minus sign)",
    'convention', 7, 'medium', None, None,
    "Subtraction printed with the long dash (GLOBAL_ISSUES item 23); left to the convention-7 decision, which must "
    "cover minus signs. The preceding misprint fix touches the same formula.")
add(152, "(5.2.3.2): 'H^q(𝔛, 𝔍^hℱ(n)/𝔍^kℱ(n)) = 0'", "quotient with a slash, plain parentheses",
    "\\left( ... \\frac{...}{...}\\right)", 'formula', None, 'high',
    r"\mathrm H^q\left(\mathfrak X,¶\frac{\mathfrak J^h\mathcal F(n)}{\mathfrak J^k\mathcal F(n)}\right)=0",
    r"\mathrm H^q(\mathfrak X,¶\mathfrak J^h\mathcal F(n)/\mathfrak J^k\mathcal F(n))=0",
    "Enlarged crop.")
add(152, "(5.2.3.4): '→ H^1(𝔛, 𝔍^kℱ(n)/𝔍^{k+1}ℱ(n)) = 0'", "quotient with a slash, plain parentheses",
    "\\left( ... \\frac{...}{...}\\right)", 'formula', None, 'high',
    r"\mathrm H^1\left(\mathfrak X,¶\frac{\mathfrak J^k\mathcal F(n)}{\mathfrak J^{k+1}\mathcal F(n)}\right)=0",
    r"\mathrm H^1(\mathfrak X,¶\mathfrak J^k\mathcal F(n)/\mathfrak J^{k+1}\mathcal F(n))=0",
    "Enlarged crop.")
add(152, "After (5.2.3.5): 'est surjective. Pour tout q'", "'surjective' in italics", "upright",
    'italics', None, 'high', r"est surjective.", r"est \emph{surjective}.", "Enlarged crop.")
add(152, "After (5.2.3.5): 'Pour tout q, le système projectif'", "'tout' in italics", "upright",
    'italics', None, 'high', r"Pour tout $q$", r"Pour \emph{tout} $q$", "Enlarged crop.")
add(152, "After (5.2.3.5): 'le système projectif (H^q(𝔛, ℱ_k(n)) (k⩾0) vérifie'",
    "(k⩾0) on the line, in parentheses, after the system", "subscript _{k\\geq0}", 'formula', None, 'high',
    r"_{k\geq0}$ vérifie", r"\quad(k\geq0)$ vérifie",
    "Enlarged crop. Independent of the next edit (missing parenthesis).")
add(152, "After (5.2.3.5): '(H^q(𝔛, ℱ_k(n)) (k⩾0)'", "(H^q(𝔛, ℱ_k(n)) : three opening, two closing parentheses",
    "$(\\mathrm H^q(\\mathfrak X,\\mathcal F_k(n)))$ (silently corrected)", 'misprint_in_print', None, 'high',
    r"$(\mathrm H^q(\mathfrak X,\mathcal F_k(n)))", r"$(\mathrm H^q(\mathfrak X,\mathcal F_k(n))",
    "Enlarged crop (5x): only two closing parentheses after n. The TeX silently adds the third; the fix restores "
    "the printed reading.",
    corrected=r"$(\mathrm H^q(\mathfrak X,\mathcal F_k(n)))")
c2(152, "Proof of (5.2.3): 'ouvert affine dans chacun des X_k (I, 10.5.2)'", 'I', r"(I, 10.5.2)", r"(\textbf{I}, 10.5.2)")
add(152, "Proof of (5.2.3): 'H^q(U, ℱ_k(n)) = 0 pour tout q>0 (1.3.1), et'", "(1.3.1) without a chapter numeral",
    "(I, 1.3.1)", 'extra', None, 'high', r"(I, 1.3.1)", r"(1.3.1)",
    "Enlarged crop: no 'I,'. The print cites (III, 1.3.1), the vanishing of H^q on an affine scheme for quasi-coherent "
    "sheaves (label III.1.3.1-fr), which is what is used; the TeX's 'I, ' is not in the print.")
c2(152, "Proof of (5.2.3): 'est surjective pour h⩽k (I, 1.3.9)'", 'I', r"(I, 1.3.9)", r"(\textbf{I}, 1.3.9)")
add(152, "Proof of (5.2.3): 'Les conditions d'application de (0, 13.3.1)'", "(𝟎, 13.3.1): bold 0", "($0$, 13.3.1)",
    'convention', 2, 'high', r"($0$, 13.3.1)", r"(\textbf{0}, 13.3.1)", "Bold 0 in the reference to chapter 0.")
add(152, "1°: 'Pour tout q>0, H^q(𝔛, ℱ(n)) → lim H^q(𝔛, ℱ_k(n)) est bijectif'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", 'other', None, 'high',
    r"Pour tout $q>0$,¶\[¶\mathrm H^q(\mathfrak X,\mathcal F(n))\longrightarrow¶\varprojlim_k\mathrm H^q(\mathfrak X,\mathcal F_k(n))¶\]¶est bijectif",
    r"Pour tout $q>0$,¶$\mathrm H^q(\mathfrak X,\mathcal F(n))\longrightarrow¶\varprojlim_k\mathrm H^q(\mathfrak X,\mathcal F_k(n))$¶est bijectif",
    "Layout: inline in the print.")
add(152, "2°: 'L'homomorphisme H^0(𝔛, ℱ(n)) → lim H^0(𝔛, ℱ_k(n)) est bijectif'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", 'other', None, 'high',
    r"L'homomorphisme¶\[¶\mathrm H^0(\mathfrak X,\mathcal F(n))\longrightarrow¶\varprojlim_k\mathrm H^0(\mathfrak X,\mathcal F_k(n))¶\]¶est bijectif~;",
    r"L'homomorphisme¶$\mathrm H^0(\mathfrak X,\mathcal F(n))\longrightarrow¶\varprojlim_k\mathrm H^0(\mathfrak X,\mathcal F_k(n))$¶est bijectif~;",
    "Layout: inline in the print. The last formula of 2° is displayed in the print too.")
add(152, "2°, last display: 'lim H^0(𝔛, ℱ_k(n)) → H^0(𝔛, ℱ_h(n))'", "no punctuation after the display",
    "comma after the display", 'punctuation', None, 'high',
    r"\longrightarrow\mathrm H^0(\mathfrak X,\mathcal F_h(n)),¶\]", r"\longrightarrow\mathrm H^0(\mathfrak X,\mathcal F_h(n))¶\]",
    "Enlarged crop: the display ends with the parenthesis; 'ce qui achève la démonstration.' follows.")
add(152, "Corollaire (5.2.4): 'Les hypothèses étant celles de (5.2.3), pour tout'",
    "(5.2.3) upright inside the italic statement",
    "(\\hyperref[III.5.2.3-fr]{5.2.3}) inside the italic corollary environment: italic", 'convention', 6, 'high',
    r"(\hyperref[III.5.2.3-fr]{5.2.3}), pour tout", r"\textup{(\hyperref[III.5.2.3-fr]{5.2.3})}, pour tout",
    "Enlarged crop.")
add(152, "End of page: 'engendré par ses sections au-dessus | de 𝔛' (Corollaire (5.2.4) runs on to p. 153)",
    "no paragraph break at the page boundary", "blank line before \\oldpage[III]{153} (with the blank line after it: paragraph break)",
    'marker', None, 'high',
    r"sections au-dessus¶¶", r"sections au-dessus¶",
    "GLOBAL_ISSUES item 20. Apply together with the removal of the blank line after the marker, in p. 153's segment: "
    "'\\oldpage[III]{153}\\n\\nde $\\mathfrak X$' -> '\\oldpage[III]{153}\\nde $\\mathfrak X$'.")

# ---------------------------------------------------------------- checks
texts = {}
for p in (148, 149, 150, 151, 152):
    with open(rf'{RUN}\page_{p}.tex', encoding='utf-8', newline='') as fh:
        texts[p] = fh.read().replace('\r\n', '\n')
bad = 0
for d in F:
    fx = d['fix']
    if fx is None:
        continue
    n = texts[d['page']].count(fx['old'])
    if n != 1:
        bad += 1
        print('NOT UNIQUE/MISSING', d['page'], n, repr(fx['old'])[:120])
# overlapping olds on one page (fixes that are not independent)
for p in texts:
    spans = []
    for i, d in enumerate(F):
        if d['page'] != p or d['fix'] is None:
            continue
        a = texts[p].find(d['fix']['old'])
        spans.append((a, a + len(d['fix']['old']), i))
    spans.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(spans, spans[1:]):
        if a2 < b1:
            print('OVERLAP on page', p, i1, i2)
counts = {}
for d in F:
    c = counts.setdefault(d['page'], [0, 0, 0])
    if d['kind'] == 'convention':
        c[1] += 1
    elif d['kind'] == 'misprint_in_print':
        c[2] += 1
    else:
        c[0] += 1
print('problems:', bad)
print('counts (normal/convention/misprint):', counts)
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print('written', OUT, len(F))
