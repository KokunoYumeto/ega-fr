import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex"
OUT = RUN + r"\findings_115_119.json"

SUBSEC = ("\\subsection{Structure locale des morphismes non ramifiés et des morphismes étales.}\n"
          "\\EGAReaderTarget{ega4.c04.subsec.18-4}{subsection:IV.18.4}\n")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

PRE = "Spelling: the print writes 'préadique' without a hyphen; the TeX elsewhere (ega4-16, ega4-17, rest of ega4-18) already has 'préadique'. All 8 'pré-adique' of ega4-18 are on pp. 115-117."
BOLDI = "Genuine reference to EGA I (bold I, '10.11.x'), not one of EGA IV's own (1.x.y): keep the chapter numeral."

# ---------------- p. 115 ----------------
add(115, "top of p. 115: page break 114/115 inside '... (1.4.6). Dire | que B est une A-algèbre non ramifiée'",
    "p. 115 begins mid-sentence with 'que B est une A-algèbre' at the left margin; p. 114 ends with 'Dire' (checked on page_114_s4)",
    "blank line after \\oldpage[IV-4]{115} (and one before it): a paragraph break inside the sentence",
    "marker", None, "high",
    "\\oldpage[IV-4]{115}\n\nque $B$", "\\oldpage[IV-4]{115}\nque $B$",
    "BOUNDARY FIX (page break with p. 114). The marker is at the right place; both blank lines around it must go (\\oldpage ends with \\ignorespaces, which does not skip a \\par). This removes the one after the marker; the one before it ('(1.4.6). Dire' + blank line) lies at the end of the p. 114 segment (batch 110-114).")

add(115, "Proposition (18.3.2), l. 2: 'pour la topologie J-préadique, A soit séparé et complet;'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, $A$ soit séparé et complet;", "$\\mathfrak J$-préadique, $A$ soit séparé et complet;", PRE)

add(115, "Proposition (18.3.2), displayed functor 'B ⇝ B⊗_A A_0'",
    "wavy arrow ⇝ (crop p115_s2_arrow.png)", "\\longmapsto", "symbol", None, "high",
    "B\\longmapsto B\\otimes_A A_0", "B\\leadsto B\\otimes_A A_0",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")

add(115, "Lemme (18.3.2.1), l. 2: 'pour la topologie J-préadique, A soit séparé et complet.'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, $A$ soit séparé et complet.", "$\\mathfrak J$-préadique, $A$ soit séparé et complet.", PRE)

add(115, "Lemme (18.3.2.1), label '(i)'",
    "upright (i) inside the italic statement (measured: no slant)", "\\item[(i)] (italic in the lemma)", "convention", 6, "high",
    "\\item[(i)] Tout $A$-module projectif", "\\item[\\textup{(i)}] Tout $A$-module projectif", "GLOBAL_ISSUES 16.")

add(115, "Lemme (18.3.2.1) (i): 'pour la topologie J-préadique, donc limite projective'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, donc limite", "$\\mathfrak J$-préadique, donc limite", PRE)

add(115, "Lemme (18.3.2.1), label '(ii)'",
    "upright (ii) inside the italic statement", "\\item[(ii)] (italic in the lemma)", "convention", 6, "high",
    "\\item[(ii)] Inversement", "\\item[\\textup{(ii)}] Inversement", "GLOBAL_ISSUES 16.")

add(115, "proof of (i): 'comme L est séparé pour la topologie J-préadique, il en est de même'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, il en est de même", "$\\mathfrak J$-préadique, il en est de même", PRE)

add(115, "proof of (i): 'est continu pour la topologie J-préadique, son noyau N'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, son noyau", "$\\mathfrak J$-préadique, son noyau", PRE)

add(115, "proof of (ii): 'soit u_n : L_n → M_n l'application A-linéaire telle que'",
    "'l'application A-linéaire' (plain A, no subscript; crop p115_s4_lin.png)", "l'application $A_n$-linéaire",
    "formula", None, "high",
    "l'application $A_n$-linéaire", "l'application $A$-linéaire",
    "The TeX rewords the print (A_n for A). Not a misprint: an A_n-linear map between A_n-modules is the same as an A-linear one.")

add(115, "proof of (ii): 'Par hypothèse on a une suite exacte scindée'",
    "scindée in italics (crop p115_s4_lin.png)", "scindée upright", "italics", None, "high",
    "Par hypothèse on a une suite exacte scindée", "Par hypothèse on a une suite exacte \\emph{scindée}")

add(115, "page break 115/116 after the display '0 → N_n → L_n → M_n → 0' | 'et comme L_n = ...'",
    "p. 116 continues the sentence after the display: 'et comme' at the left margin, no indent (page_116_s1)",
    "blank line before \\oldpage[IV-4]{116} (and another after it): 'et comme' starts a new indented paragraph",
    "marker", None, "high",
    "M_n\\longrightarrow 0\n\\]\n\n", "M_n\\longrightarrow 0\n\\]\n",
    "The marker is at the right place. Part 1 of 2: the first p. 116 finding removes the blank line after \\oldpage[IV-4]{116}; apply both.")

# ---------------- p. 116 ----------------
add(116, "top of p. 116: 'et comme L_n = L_{n+1}/J^{n+1}L_{n+1}'",
    "continuation line after the display, no indent", "blank line after \\oldpage[IV-4]{116}",
    "marker", None, "high",
    "\\oldpage[IV-4]{116}\n\net comme", "\\oldpage[IV-4]{116}\net comme",
    "Part 2 of 2 with the last p. 115 finding; both blank lines must go.")

add(116, "after the diagram: 'sont toutes trois surjectives.'",
    "surjectives in italics (crop p116_s1_surj.png)", "surjectives upright", "italics", None, "high",
    "sont toutes trois surjectives.", "sont toutes trois \\emph{surjectives}.")

add(116, "'on a, en vertu de (0_III, 13.2.2), la suite exacte'",
    "bold 0 with subscript III", "plain 0", "convention", 2, "high",
    "($0_{\\mathrm{III}}$, 13.2.2)", "($\\mathbf{0}_{\\mathrm{III}}$, 13.2.2)")

add(116, "'il résulte de (0, 19.1.8) que la suite exacte (18.3.2.2) est scindée'",
    "bare bold 0", "plain 0", "convention", 2, "high",
    "(0, 19.1.8)", "(\\textbf{0}, 19.1.8)")

add(116, "'B et C sont séparés et complets pour la topologie J-préadique, et l'on a'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, et l'on a", "$\\mathfrak J$-préadique, et l'on a", PRE)

add(116, "'est continu pour les topologies J-préadiques'",
    "𝔍-préadiques", "$\\mathfrak J$-pré-adiques", "word", None, "high",
    "$\\mathfrak J$-pré-adiques", "$\\mathfrak J$-préadiques", PRE)

add(116, "'Mais comme B et C sont des A-algèbres étales,'",
    "étales in italics (crop p116_s3_it.png)", "étales upright", "italics", None, "high",
    "des $A$-algèbres étales, il résulte", "des $A$-algèbres \\emph{étales}, il résulte")

add(116, "'est bijective pour n ≥ 0'",
    "bijective in italics (crop p116_s3_it.png)", "bijective upright", "italics", None, "high",
    "est bijective pour $n\\geq 0$", "est \\emph{bijective} pour $n\\geq 0$",
    "The second 'est bijective.' at the end of the sentence is roman in the print.")

add(116, "'que l'application canonique Hom_{A-alg.}(B, C) → Hom_{A_0-alg.}(B_0, C_0) est bijective.'",
    "the formula is set in the line (starts a text line and is followed by 'est bijective.' on the same line)",
    "displayed with \\[ ... \\]", "other", None, "high",
    "canonique\n\\[\n  \\Hom_{A\\text{-alg.}}(B,C)\\longrightarrow\\Hom_{A_0\\text{-alg.}}(B_0,C_0)\n\\]\nest bijective.",
    "canonique $\\Hom_{A\\text{-alg.}}(B,C)\\to\\Hom_{A_0\\text{-alg.}}(B_0,C_0)$ est bijective.",
    "Display vs inline only; no connecting word lost or added.")

add(116, "last line: 'radical de A (0_I, 7.1.10),'",
    "bold 0 with subscript I", "plain 0", "convention", 2, "high",
    "Or, puisque $\\mathfrak J$ est contenu dans le radical de $A$ ($0_{\\mathrm I}$, 7.1.10)",
    "Or, puisque $\\mathfrak J$ est contenu dans le radical de $A$ ($\\mathbf{0}_{\\mathrm I}$, 7.1.10)",
    "Same spot as the next finding (page break); apply this one first (both orders work: neither edit changes the other's 'old').")

add(116, "page break 116/117 inside 'puisque J est contenu dans le radical de A (0_I, 7.1.10), | on a J ⊂ m'",
    "p. 116 ends with a comma; p. 117 continues the sentence ('on a') at the left margin",
    "blank line before \\oldpage[IV-4]{117} (and another after it)", "marker", None, "high",
    "7.1.10),\n\n", "7.1.10),\n",
    "The marker is at the right place. Part 1 of 2: the first p. 117 finding removes the blank line after \\oldpage[IV-4]{117}; apply both. Apply after the convention-2 fix just before it (same spot).")

# ---------------- p. 117 ----------------
add(117, "top of p. 117: 'on a J ⊂ m et si m_0 = m/J'",
    "continuation of the sentence, no indent", "blank line after \\oldpage[IV-4]{117}", "marker", None, "high",
    "\\oldpage[IV-4]{117}\n\non a", "\\oldpage[IV-4]{117}\non a",
    "Part 2 of 2 with the last p. 116 finding; both blank lines must go.")

add(117, "heading of (18.3.3)",
    "'Exemple (18.3.3). — La prop. (18.3.2) ...' (italic 'Exemple', number after it; roman body)",
    "\\begin{env}[18.3.3] ... \\emph{Exemple.} --- gives '(18.3.3) Exemple. —'", "other", None, "high",
    "\\begin{env}[18.3.3]\n\\label{IV.18.3.3}\n\\emph{Exemple.} --- La prop.",
    "\\begin{example}[18.3.3]\n\\label{IV.18.3.3}\nLa prop.",
    "Use the preamble's singular example environment ('Exemple (…). —', roman body), as the print shows. Part 1 of 2 with the next finding (\\end{env} -> \\end{example}); apply both.")

add(117, "end of (18.3.3)",
    "-", "\\end{env}", "other", None, "high",
    "en vertu de (18.3.2).\n\\end{env}", "en vertu de (18.3.2).\n\\end{example}",
    "Part 2 of 2 with the previous finding (\\begin{env}[18.3.3] -> \\begin{example}[18.3.3]); apply both.")

add(117, "Théorème (18.3.4), l. 2: 'complet pour la topologie J-préadique, A_0 = A/J'",
    "𝔍-préadique", "$\\mathfrak J$-pré-adique", "word", None, "high",
    "$\\mathfrak J$-pré-adique, $A_0=A/\\mathfrak J$", "$\\mathfrak J$-préadique, $A_0=A/\\mathfrak J$", PRE)

add(117, "Théorème (18.3.4), displayed functor 'Z ⇝ Z ×_X X_0'",
    "wavy arrow ⇝", "\\longmapsto", "symbol", None, "high",
    "Z\\longmapsto Z\\times_X X_0", "Z\\leadsto Z\\times_X X_0",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")

add(117, "'Il résulte de (III, 5.4.1) que l'on a une bijection canonique'",
    "bold III", "plain III", "convention", 2, "high",
    "(III, 5.4.1)", "(\\textbf{III}, 5.4.1)")

add(117, "'le deuxième théorème de comparaison (III, 5.1.4)'",
    "bold III", "plain III", "convention", 2, "high",
    "(III, 5.1.4)", "(\\textbf{III}, 5.1.4)")

add(117, "'il résulte de (III, 5.1.3), (I, 10.11.4) et (I, 10.11.7) que' — first reference",
    "bold III", "plain III", "convention", 2, "high",
    "il résulte de (III, 5.1.3)", "il résulte de (\\textbf{III}, 5.1.3)")

add(117, "same sentence: '(I, 10.11.4) et'",
    "bold I, then '10.11.4' (crop p117_s3_refs.png)", "plain I", "convention", 2, "high",
    "(I, 10.11.4) et", "(\\textbf{I}, 10.11.4) et", BOLDI)

add(117, "same sentence: '(I, 10.11.7) que B est muni'",
    "bold I, then '10.11.7'", "plain I", "convention", 2, "high",
    "(I, 10.11.7) que", "(\\textbf{I}, 10.11.7) que", BOLDI)

add(117, "'cela résulte encore de (III, 5.1.3), (I, 10.11.4), (I, 10.11.7)' — first reference",
    "bold III", "plain III", "convention", 2, "high",
    "encore de (III, 5.1.3)", "encore de (\\textbf{III}, 5.1.3)")

add(117, "same sentence: '(I, 10.11.4),'",
    "bold I, then '10.11.4'", "plain I", "convention", 2, "high",
    "(I, 10.11.4),", "(\\textbf{I}, 10.11.4),", BOLDI)

add(117, "same sentence: '(I, 10.11.7) et du fait que'",
    "bold I, then '10.11.7'", "plain I", "convention", 2, "high",
    "(I, 10.11.7) et du fait", "(\\textbf{I}, 10.11.7) et du fait", BOLDI)

add(117, "'le foncteur G ⇝ Hom_{O_X}(F, G) est exact'",
    "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
    "\\sh{G}\\mapsto\\mathscr{H}\\!om", "\\sh{G}\\leadsto\\mathscr{H}\\!om",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")

add(117, "'pour tout point fermé x ∈ X, B_x ⊗_{O_{X,x}} k(x)'",
    "bold italic k(x) (crop p117_s4_end.png)", "\\kappa(x) (Greek kappa)", "symbol", None, "high",
    "\\otimes_{\\sh{O}_{X,x}}\\kappa(x)$", "\\otimes_{\\sh{O}_{X,x}}\\boldsymbol{k}(x)$",
    "Wrong letter: the print's residue field is a bold italic k, written \\boldsymbol{k} in ega4-16/17 (GLOBAL_ISSUES 55 pattern); not convention 1, since the TeX letter is a kappa. ega4-18 has 7 \\kappa, the other 5 on pp. 110-114.")

add(117, "'est une k(x)-algèbre séparable'",
    "bold italic k(x)", "\\kappa(x) (Greek kappa)", "symbol", None, "high",
    "une $\\kappa(x)$-algèbre séparable", "une $\\boldsymbol{k}(x)$-algèbre séparable",
    "As the previous finding.")

add(117, "'puisque J est contenu dans le radical de A (0_I, 7.1.10);'",
    "bold 0 with subscript I", "plain 0", "convention", 2, "high",
    "radical de $A$ ($0_{\\mathrm I}$, 7.1.10);", "radical de $A$ ($\\mathbf{0}_{\\mathrm I}$, 7.1.10);")

add(117, "last line: 'et de ce que B_0 est une O_{X_0}-algèbre finie et étale.'",
    "lower-case 'algèbre' for the sheaf B_0 (crop p117_s4_end.png); EGA writes O_X-Algèbre with a capital A for sheaves, as at the start of the same paragraph ('si B_0 est une O_{X_0}-Algèbre finie et étale')",
    "$\\sh{O}_{X_0}$-Algèbre (silent correction)", "misprint_in_print", None, "high",
    "$\\sh{O}_{X_0}$-Algèbre finie et étale.", "$\\sh{O}_{X_0}$-algèbre finie et étale.",
    "Restores the printed lower-case a; the fix changes only that letter. Adjacent to (not overlapping) the next finding.",
    corrected="$\\sh{O}_{X_0}$-Algèbre finie et étale.")

add(117, "page break 117/118: heading '18.4. Structure locale des morphismes non ramifiés et des morphismes étales.'",
    "p. 117 ends with '... O_{X_0}-algèbre finie et étale.'; the 18.4 heading is the first line of p. 118 (page_118_s1)",
    "\\subsection{...18.4} and its \\EGAReaderTarget stand before \\oldpage[IV-4]{118}, at the end of the p. 117 segment",
    "marker", None, "high",
    "\\subsection{Structure locale des morphismes non ramifiés et des morphismes étales.}\n\\EGAReaderTarget{ega4.c04.subsec.18-4}{subsection:IV.18.4}\n\n",
    "",
    "The marker stands too late (after the heading). Two-part move (the heading moves, not the marker, so each edit stays in its own page segment): part 1 of 2 removes the heading from the end of the p. 117 segment; the first p. 118 finding re-inserts it after \\oldpage[IV-4]{118}. Apply both or neither. Result: 'étale.' + blank line + \\oldpage[IV-4]{118} + blank line + \\subsection, as at markers 63, 72, 79 of ega4-17 (heading at the top of a page: blank lines stay).")

# ---------------- p. 118 ----------------
add(118, "top of p. 118: heading 18.4",
    "'18.4. Structure locale des morphismes non ramifiés et des morphismes étales.' at the top of p. 118",
    "heading missing after \\oldpage[IV-4]{118} (it stands at the end of the p. 117 segment)", "marker", None, "high",
    "\\oldpage[IV-4]{118}\n\n\\begin{lemma}[18.4.1]",
    "\\oldpage[IV-4]{118}\n\n" + SUBSEC + "\n\\begin{lemma}[18.4.1]",
    "Part 2 of 2 with the last p. 117 finding (which removes these two lines from the end of the p. 117 segment). Apply both or neither.")

add(118, "'On a la suite exacte (0, 20.5.12.1)'",
    "bare bold 0", "plain 0", "convention", 2, "high",
    "(0, 20.5.12.1)", "(\\textbf{0}, 20.5.12.1)")

add(118, "'où G′ parcourt un système de générateurs de l'idéal J'",
    "'où G′ parcourt' — G with a prime (crop p118_s2_G.png)", "où $G$ parcourt (silent correction)",
    "misprint_in_print", None, "high",
    "où $G$ parcourt", "où $G'$ parcourt",
    "The print has G′ where G (ranging over generators of J, whose derivatives G′(u) generate J′) is meant.",
    corrected="où $G$ parcourt")

add(118, "'de l'idéal J (0, 20.5.13); d'où aussitôt le lemme.'",
    "bare bold 0", "plain 0", "convention", 2, "high",
    "(0, 20.5.13)", "(\\textbf{0}, 20.5.13)")

add(118, "Proposition (18.4.2): 'Les notations étant celles de (18.4.1), soit q'",
    "upright (18.4.1) inside the italic statement", "italic", "convention", 6, "high",
    "celles de (18.4.1), soit", "celles de \\textup{(18.4.1)}, soit", "Printed upright inside the italic statement.")

add(118, "Proposition (18.4.2), label '(i)'",
    "upright (i)", "\\item[(i)] (italic)", "convention", 6, "high",
    "\\item[(i)] Si $\\mathfrak q$ ne contient pas", "\\item[\\textup{(i)}] Si $\\mathfrak q$ ne contient pas", "GLOBAL_ISSUES 16.")

add(118, "Proposition (18.4.2) (i): '(p étant l'image réciproque de q dans A)'",
    "upright parentheses around the italic words (measured: no slant; crops p118_s2_pparen.png, p118_pclose.png)",
    "italic parentheses", "convention", 6, "medium",
    "($\\mathfrak p$ étant l'image réciproque de $\\mathfrak q$ dans $A$)",
    "\\textup{(}$\\mathfrak p$ étant l'image réciproque de $\\mathfrak q$ dans $A$\\textup{)}",
    "Parentheses inside italic statements are upright in the print also around italic words (GLOBAL_ISSUES 26, 96).")

add(118, "Proposition (18.4.2), label '(ii)'",
    "upright (ii)", "\\item[(ii)] (italic)", "convention", 6, "high",
    "\\item[(ii)] Supposons de plus que $F$ soit unitaire et engendre $\\mathfrak J$. Alors, pour que",
    "\\item[\\textup{(ii)}] Supposons de plus que $F$ soit unitaire et engendre $\\mathfrak J$. Alors, pour que", "GLOBAL_ISSUES 16.")

add(118, "'Ω^1_{B_q/A_p} = 0 (0, 20.5.9)'",
    "bare bold 0", "plain 0", "convention", 2, "high",
    "$\\Omega^1_{B_{\\mathfrak q}/A_{\\mathfrak p}}=0$ (0, 20.5.9)", "$\\Omega^1_{B_{\\mathfrak q}/A_{\\mathfrak p}}=0$ (\\textbf{0}, 20.5.9)")

add(118, "'de l'implication c) ⇒ a) dans (17.6.1)'",
    "labels c) and a) wholly italic, parentheses included (measured slant)", "$c)\\Rightarrow a)$: italic letters, upright parentheses",
    "italics", None, "high",
    "l'implication $c)\\Rightarrow a)$ dans (17.6.1)", "l'implication $\\textit{c)}\\Rightarrow\\textit{a)}$ dans (17.6.1)",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88); written as the edition's other $\\textit{d'')}\\Rightarrow\\textit{c)}$.")

add(118, "Corollaire (18.4.3): 'Les notations étant celles de (18.4.2), supposons'",
    "upright (18.4.2) inside the italic statement", "italic", "convention", 6, "high",
    "celles de (18.4.2), supposons", "celles de \\textup{(18.4.2)}, supposons", "Printed upright inside the italic statement.")

add(118, "Corollaire (18.4.3): '(ou, ce qui revient au même, que l'idéal de A[T] engendré par F et F′ soit égal à A[T])'",
    "the whole parenthesis is roman", "italic (inside the corollary)", "convention", 6, "high",
    "(ou, ce qui revient au même, que l'idéal de $A[T]$ engendré par $F$ et $F'$ soit égal à $A[T]$)",
    "\\textup{(ou, ce qui revient au même, que l'idéal de $A[T]$ engendré par $F$ et $F'$ soit égal à $A[T]$)}")

add(118, "'Compte tenu de (18.4.2), (ii)), dire que Spec(B) est étale'",
    "'(18.4.2), (ii)),' — an extra closing parenthesis (crop p118_s3_compte.png)", "(18.4.2), (ii), (silent correction)",
    "misprint_in_print", None, "high",
    "Compte tenu de (18.4.2), (ii), dire", "Compte tenu de (18.4.2), (ii)), dire",
    "Unbalanced parentheses in the print. The intended form is EGA's usual '(18.4.2, (ii))', as printed on p. 119 ('en vertu de (18.4.2, (ii))'); the TeX's '(18.4.2), (ii)' is also a correct reading.",
    corrected="Compte tenu de (18.4.2, (ii)), dire")

add(118, "Lemme (18.4.4): 'Soient n_i (1 ≤ i ≤ r) des idéaux maximaux'",
    "upright parentheses (measured)", "italic parentheses", "convention", 6, "high",
    "($1\\leq i\\leq r$) des idéaux", "\\textup{(}$1\\leq i\\leq r$\\textup{)} des idéaux",
    "Same treatment as p. 21 (\\textup{(}$1\\leq i\\leq m$\\textup{)}).")

add(118, "Lemme (18.4.4): 'pour tout indice i (1 ≤ i ≤ r).'",
    "upright parentheses (measured)", "italic parentheses", "convention", 6, "high",
    "indice $i$ ($1\\leq i\\leq r$)", "indice $i$ \\textup{(}$1\\leq i\\leq r$\\textup{)}")

add(118, "page break 118/119 inside Lemme (18.4.4): 'si k est le corps | résiduel de A'",
    "p. 119 continues the sentence ('résiduel de A') at the left margin",
    "blank line before \\oldpage[IV-4]{119} (and another after it): a paragraph break inside the lemma's sentence",
    "marker", None, "high",
    "si $k$ est le corps\n\n", "si $k$ est le corps\n",
    "The marker is at the right place. Part 1 of 2: the first p. 119 finding removes the blank line after \\oldpage[IV-4]{119}; apply both.")

# ---------------- p. 119 ----------------
add(119, "top of p. 119: 'résiduel de A, f ∈ k[T] ...'",
    "continuation of the sentence, no indent", "blank line after \\oldpage[IV-4]{119}", "marker", None, "high",
    "\\oldpage[IV-4]{119}\n\nrésiduel", "\\oldpage[IV-4]{119}\nrésiduel",
    "Part 2 of 2 with the last p. 118 finding; both blank lines must go.")

add(119, "end of Lemme (18.4.4): 'vérifie les conditions F′(u) ∉ n^i pour 1 ≤ i ≤ r'",
    "the index i is set as a SUPERSCRIPT: 𝔫^i (crop p119_s1_ni.png)", "\\mathfrak n_i (silent correction)",
    "misprint_in_print", None, "high",
    "vérifie les conditions $F'(u)\\notin\\mathfrak n_i$", "vérifie les conditions $F'(u)\\notin\\mathfrak n^i$",
    "Superior i for the inferior i (the maximal ideals n_i).",
    corrected="vérifie les conditions $F'(u)\\notin\\mathfrak n_i$")

add(119, "'chacun des n_i (II, 6.1.10)'",
    "bold II", "plain II", "convention", 2, "high",
    "chacun des $\\mathfrak n_i$ (II, 6.1.10)", "chacun des $\\mathfrak n_i$ (\\textbf{II}, 6.1.10)")

add(119, "'en vertu de (17.6.1, c))'",
    "label c) wholly italic, then an upright closing parenthesis (measured slant)", "$c)$: italic c, upright parenthesis",
    "italics", None, "high",
    "(17.6.1, $c)$)", "(17.6.1, \\emph{c)})",
    "Labels in roman text are italic in the print (GLOBAL_ISSUES 88).")

add(119, "Proposition (18.4.5): 'B une A-algèbre finie (resp. finie et de présentation finie).'",
    "'(resp.' and ')' upright, the words italic (measured)", "all italic", "convention", 6, "high",
    "(resp. finie et de présentation finie)", "\\textup{(resp.} finie et de présentation finie\\textup{)}")

add(119, "Proposition (18.4.5): 'formellement non ramifiée (resp. étale), il faut'",
    "'(resp.' and ')' upright, 'étale' italic (measured)", "all italic", "convention", 6, "high",
    "non ramifiée (resp. étale), il faut et il suffit qu'il existe un polynôme unitaire séparable",
    "non ramifiée \\textup{(resp.} étale\\textup{)}, il faut et il suffit qu'il existe un polynôme unitaire séparable")

add(119, "Proposition (18.4.5): 'séparable F ∈ A[T] (18.4.3) tel que'",
    "upright (18.4.3)", "italic", "convention", 6, "high",
    "$F\\in A[T]$ (18.4.3) tel que", "$F\\in A[T]$ \\textup{(18.4.3)} tel que", "Printed upright inside the italic statement.")

add(119, "Proposition (18.4.5): '(resp. isomorphe à A[T]/F.A[T])'",
    "'(resp.' and ')' upright, 'isomorphe à' italic (measured)", "all italic", "convention", 6, "high",
    "(resp. isomorphe à $A[T]/F.A[T]$)", "\\textup{(resp.} isomorphe à $A[T]/F.A[T]$\\textup{)}")

add(119, "Proposition (18.4.5): '(resp. F est nécessairement de degré n)'",
    "'(resp.' and ')' upright, the words italic (measured)", "all italic", "convention", 6, "high",
    "(resp. $F$ est nécessairement de degré $n$)", "\\textup{(resp.} $F$ est nécessairement de degré $n$\\textup{)}")

add(119, "'si l'on pose f = f_1 f_2 ... f_r'",
    "baseline dots (crop p119_s3_dots.png)", "\\cdots (centred dots)", "symbol", None, "high",
    "f=f_1f_2\\cdots f_r", "f=f_1f_2\\ldots f_r", "Baseline dots in the print; \\cdots gives centred dots.")

add(119, "page break 119/120 inside 'autrement dit la A-algèbre B est | isomorphe à A[T]/F.A[T]'",
    "p. 119 ends 'B est' (no stop); p. 120 begins 'isomorphe à A[T]/F.A[T]' at the left margin (checked on page_120_s1)",
    "blank line before \\oldpage[IV-4]{120} (and another after it): a paragraph break inside the sentence",
    "marker", None, "high",
    "autrement dit la $A$-algèbre $B$ est\n\n", "autrement dit la $A$-algèbre $B$ est\n",
    "The marker is at the right place. The blank line AFTER \\oldpage[IV-4]{120} (before 'isomorphe à', in the p. 120 segment) must go too; it lies in the p. 120 batch and is not reported here.")

# ---------------- checks ----------------
ok = True
pages = {}
for p in range(115, 120):
    t = open(RUN + "\\page_%03d.tex" % p, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    pages[p] = t
for i, f in enumerate(F):
    if f['fix'] is None:
        continue
    o = f['fix']['old']
    c = pages[f['page']].count(o)
    if c != 1:
        ok = False
        print('NOT UNIQUE/ABSENT', i, f['page'], c, repr(o))
print('uniqueness ok' if ok else 'uniqueness FAILED')
_whole = open(SRC, encoding='utf-8', newline='').read()
_fw = [(i, f['page'], _whole.count(f['fix']['old'])) for i, f in enumerate(F) if f['fix'] and _whole.count(f['fix']['old']) != 1]
print('file-wide uniqueness ok' if not _fw else ('file-wide repeats: %r' % _fw))

# simulate applying all fixes, in list order, to the current source file
src = open(SRC, encoding='utf-8', newline='').read()
m1 = src.index('\\oldpage[IV-4]{115}')
m2 = src.index('\\oldpage[IV-4]{120}')
pre_seg = src[:m1]
tail = src[m2:]
segs = {}
for p in range(115, 120):
    a = src.index('\\oldpage[IV-4]{%d}' % p)
    b = src.index('\\oldpage[IV-4]{%d}' % (p + 1))
    segs[p] = src[a:b]
for p in range(115, 120):
    first, rest = pages[p].split('\n', 1)
    assert rest == segs[p], p
sim_ok = True
for i, f in enumerate(F):
    if f['fix'] is None:
        continue
    o, n = f['fix']['old'], f['fix']['new']
    s = segs[f['page']]
    if s.count(o) != 1:
        sim_ok = False
        print('SEQUENTIAL APPLY FAILED', i, f['page'], s.count(o), repr(o))
        continue
    segs[f['page']] = s.replace(o, n)
print('sequential apply ok' if sim_ok else 'sequential apply FAILED')
new_mid = ''.join(segs[p] for p in range(115, 120))
# show the boundaries after all edits
for p in range(115, 121):
    k = new_mid.find('\\oldpage[IV-4]{%d}' % p) if p < 120 else len(new_mid)
    print('--- around marker', p, ':', repr(new_mid[max(0, k - 60):k + 70]) if p < 120 else repr(new_mid[-70:]))
open(RUN + r"\crops_115_119\applied_preview.txt", 'w', encoding='utf-8', newline='\n').write(new_mid)

counts = {}
for f in F:
    c = counts.setdefault(f['page'], [0, 0, 0])
    if f['kind'] == 'convention':
        c[1] += 1
    elif f['kind'] == 'misprint_in_print':
        c[2] += 1
    else:
        c[0] += 1
print(counts, len(F))
with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print('written', OUT)
