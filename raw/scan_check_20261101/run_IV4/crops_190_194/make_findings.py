"""Build findings_190_194.json and check every 'old' against page_NNN.tex (CRLF normalized) and the current source."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN / "findings_190_194.json"

F = []


def add(page, where, scan, tex, kind, convention, confidence, old, new, note="", corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": None if nofix else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


G88 = "GLOBAL_ISSUES 88 (condition label in running text: whole label italic)."
G16 = "GLOBAL_ISSUES 16/88 (labels upright inside italic statements)."

# ---------------------------------------------------------------- p. 190
add(190, "Définition (19.2.1), first sentence: the parenthesis after the first defined term",
    "'transversalement F-régulière relativement à S (ou relativement à u)' is roman, with only 'ou' (and the letter u) italic; the parentheses are upright",
    "\\emph{...} stops before the parenthesis, so '(ou relativement à' comes out italic",
    "convention", 6, "high",
    r"\emph{transversalement $\mathscr F$-régulière relativement à $S$} (ou relativement à $u$) si",
    r"\emph{transversalement $\mathscr F$-régulière relativement à $S$ (\emph{ou} relativement à $u$)} si",
    "Inside the italic definition the outer \\emph is upright and the inner \\emph{ou} italic, as printed.")
add(190, "Définition (19.2.1): the quotient F/(sum f_j F)",
    "set in the line: 'les O_X-Modules F/(Σ_{j⩽i} f_jF) soient S-plats pour 0⩽i⩽n'",
    "displayed with \\[ ... \\] and \\big/ \\Bigl( \\Bigr)",
    "formula", None, "high",
    "les $\\sh{O}_X$-Modules\n\\[\n  \\mathscr F\\big/\\Bigl(\\sum_{j\\leq i}f_j\\mathscr F\\Bigr)\n\\]\nsoient $S$-plats",
    "les $\\sh{O}_X$-Modules $\\mathscr F/(\\sum_{j\\leq i}f_j\\mathscr F)$ soient $S$-plats",
    "Inline as printed; no connecting word lost.")
add(190, "Définition (19.2.1), second sentence: 'transversalement régulier relativement à S (ou relativement à u) en un point x'",
    "roman from 'transversalement' to 'en un point' (only 'ou' italic; upright parentheses); 's'il existe' italic again",
    "\\emph covers only 'transversalement régulier relativement à S': the parenthesis and 'en un point' come out italic",
    "convention", 6, "high",
    r"\emph{transversalement régulier relativement à $S$} (ou relativement à $u$) en un point $x",
    r"\emph{transversalement régulier relativement à $S$ (\emph{ou} relativement à $u$) en un point} $x",
    "Crop p190_l5r.png: 'en un point' is roman.")
add(190, "end of the statement (19.2.1): the definition environment runs on over the roman paragraph 'Dans une A-algèbre B, ...'",
    "the statement ends at 'qui engendre J|U.'; 'Dans une A-algèbre B, on dit ...' is an indented roman paragraph with 'transversalement régulier' italic",
    "\\end{definition} stands after '... dans Spec(B).', so the paragraph is italic with an upright term",
    "italics", None, "high",
    "et qui engendre $\\mathscr J|U$.\n\n",
    "et qui engendre $\\mathscr J|U$.\n\\end{definition}\n\n",
    "Edit 1 of 2 (GLOBAL_ISSUES 58 pattern): apply together with the next edit, which removes the old \\end{definition}.")
add(190, "end of the paragraph 'Dans une A-algèbre B, ...'",
    "(see previous entry)", "the old \\end{definition}",
    "italics", None, "high",
    "dans $\\Spec(B)$.\n\\end{definition}\n",
    "dans $\\Spec(B)$.\n",
    "Edit 2 of 2: apply together with the previous edit.")
add(190, "'Dans une A-algèbre B, on dit qu'un idéal J est transversalement régulier relativement à A'",
    "only 'transversalement régulier' italic; 'relativement à A' roman",
    "\\emph{transversalement régulier relativement à $A$}",
    "italics", None, "high",
    r"\emph{transversalement régulier relativement à $A$}",
    r"\emph{transversalement régulier} relativement à $A$",
    "Judged with the paragraph roman (after the two \\end{definition} edits; no overlap with them).")
add(190, "'Dans une A-algèbre B ...': 'si J = J~ est transversalement régulier'",
    "si 𝒥 = 𝔍~ est transversalement régulier relativement à S = Spec(A)",
    "si $\\widetilde{\\mathfrak J}$ est (the script J and the equals sign are missing)",
    "missing", None, "high",
    r"si $\widetilde{\mathfrak J}$ est transversalement",
    r"si $\mathscr J=\widetilde{\mathfrak J}$ est transversalement",
    "")
add(190, "Définition (19.2.2): the defined term",
    "'On dit que u est une immersion transversalement régulière relativement à S en un point y∈Y': 'immersion' and 'en un point' italic, only 'transversalement régulière relativement à S' roman",
    "\\emph{immersion transversalement régulière relativement à $S$ en un point $y\\in Y$} (upright from 'immersion' to 'y∈Y')",
    "convention", 6, "high",
    r"une \emph{immersion transversalement régulière relativement à $S$ en un point $y\in Y$} s'il",
    r"une immersion \emph{transversalement régulière relativement à $S$} en un point $y\in Y$ s'il",
    "The term looks heavier at the end of the line and the start of the next, but its letters have the roman widths (measured): heavy impression, not bold.")
add(190, "Définition (19.2.2): 'défini par un Idéal de O_U'",
    "un Idéal de 𝒪_U (U is not introduced; the neighbourhood is V)",
    "$\\sh{O}_U$ (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "The subprescheme induced on u(Y)∩V is a closed subprescheme of the open set V, so an Ideal of O_V is meant. The diplomatic TeX keeps the printed reading. Not in the IV-4 errata list (which covers IV parts 1-3).",
    corrected=r"$\sh{O}_V$", nofix=True)
add(190, "end of the statement (19.2.2): the definition runs on over 'Il est clair ...' and 'Si S→T ...'",
    "the statement ends at 'au point u(y).'; the two following paragraphs are roman, with 'ouvert', 'immersion transversalement régulière relativement à' and 'plat' italic",
    "\\end{definition} after '... en ce point.': both paragraphs italic with upright \\emph words",
    "italics", None, "high",
    "au point $u(y)$.\n\nIl est clair",
    "au point $u(y)$.\n\\end{definition}\n\nIl est clair",
    "Edit 1 of 2 (GLOBAL_ISSUES 58 pattern): apply together with the next edit.")
add(190, "end of the paragraph 'Si S→T est un morphisme plat ...'",
    "(see previous entry)", "the old \\end{definition}",
    "italics", None, "high",
    "en ce point.\n\\end{definition}",
    "en ce point.",
    "Edit 2 of 2: apply together with the previous edit.")
add(190, "'il l'est aussi relativement à T (0_I, 6.2.1)'",
    "bold 0 with subscript I", "($0_{\\mathrm I}$, 6.2.1)",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.2.1)", r"($\mathbf{0}_{\mathrm I}$, 6.2.1)", "")
add(190, "proof of (19.2.3): '(0, 15.1.15)'",
    "bold 0", "($0$, 15.1.15)",
    "convention", 2, "high",
    r"définition et de ($0$, 15.1.15)", r"définition et de (\textbf{0}, 15.1.15)", "")
add(190, "Proposition (19.2.4): 'On suppose, soit que ..., soit que ...'",
    "both 'soit' roman inside the italic statement",
    "both italic",
    "convention", 6, "high",
    r"On suppose, soit que $S$ et $X$ sont localement noethériens, soit que les morphismes",
    r"On suppose, \textup{soit} que $S$ et $X$ sont localement noethériens, \textup{soit} que les morphismes",
    "")
add(190, "Proposition (19.2.4): label a)", "label a) upright", "\\item[a)] (italic inside the statement)",
    "convention", 6, "high",
    r"\item[a)] $u$ est transversalement", r"\item[\textup{a)}] $u$ est transversalement", G16)
add(190, "Proposition (19.2.4): label b)", "label b) upright", "\\item[b)] (italic inside the statement)",
    "convention", 6, "high",
    r"\item[b)] Les morphismes $g$ et $h$", r"\item[\textup{b)}] Les morphismes $g$ et $h$", G16)
add(190, "Proposition (19.2.4): label b')", "label b') upright", "\\item[b$'$)] (italic inside the statement)",
    "convention", 6, "high",
    r"\item[b$'$)] Les morphismes", r"\item[\textup{b$'$)}] Les morphismes", G16)
add(190, "Proposition (19.2.4): label c)", "label c) upright", "\\item[c)] (italic inside the statement)",
    "convention", 6, "high",
    r"\item[c)] Le morphisme $h$ est plat au voisinage du point $y$, et l'immersion $u$ est régulière",
    r"\item[\textup{c)}] Le morphisme $h$ est plat au voisinage du point $y$, et l'immersion $u$ est régulière", G16)

# ---------------------------------------------------------------- p. 191
add(191, "Proposition (19.2.4): label c') (first line of p. 191)", "label c') upright", "\\item[c$'$)] (italic inside the statement)",
    "convention", 6, "high",
    r"\item[c$'$)] Le morphisme", r"\item[\textup{c$'$)}] Le morphisme",
    G16 + " The heavier italic of this item (top of the page) has the normal letter widths: impression, not a wrong fount.")
add(191, "proof of (19.2.4), first sentence: 'que a) entraîne b')'",
    "labels a), b') wholly italic", "$a)$, $b')$ (italic letter, upright parenthesis)",
    "italics", None, "high",
    r"que $a)$ entraîne $b')$ sans", r"que \emph{a)} entraîne \emph{b$'$)} sans", G88)
add(191, "proof of (19.2.4): 'que b') entraîne b). Montrons que b) entraîne c).'",
    "labels wholly italic", "$b')$, $b)$, $b)$, $c)$",
    "italics", None, "high",
    r"trivial que $b')$ entraîne $b)$. Montrons que $b)$ entraîne $c)$.",
    r"trivial que \emph{b$'$)} entraîne \emph{b)}. Montrons que \emph{b)} entraîne \emph{c)}.", G88)
add(191, "display in the proof of (19.2.4): three k(s)",
    "bold italic k in k(s) (three times)", "\\mathbf k(s) (bold upright)",
    "convention", 1, "high",
    r"0\longrightarrow\mathscr J\otimes_{\sh{O}_s}\mathbf k(s)\longrightarrow\sh{O}_X\otimes_{\sh{O}_s}\mathbf k(s)\longrightarrow(\sh{O}_X/\mathscr J)\otimes_{\sh{O}_s}\mathbf k(s)\longrightarrow0",
    r"0\longrightarrow\mathscr J\otimes_{\sh{O}_s}\boldsymbol{k}(s)\longrightarrow\sh{O}_X\otimes_{\sh{O}_s}\boldsymbol{k}(s)\longrightarrow(\sh{O}_X/\mathscr J)\otimes_{\sh{O}_s}\boldsymbol{k}(s)\longrightarrow0",
    "One edit for the three k of the display (outside subscripts: bold italic).")
add(191, "'est exacte (0_I, 6.1.2)'", "bold 0 with subscript I", "($0_{\\mathrm I}$, 6.1.2)",
    "convention", 2, "high",
    r"est exacte ($0_{\mathrm I}$, 6.1.2)", r"est exacte ($\mathbf{0}_{\mathrm I}$, 6.1.2)", "")
add(191, "'O_{X_s} = O_X ⊗ k(s)'", "bold italic k", "\\mathbf k(s)",
    "convention", 1, "high",
    r"=\sh{O}_X\otimes_{\sh{O}_s}\mathbf k(s)$ qui", r"=\sh{O}_X\otimes_{\sh{O}_s}\boldsymbol{k}(s)$ qui", "")
add(191, "'qui s'identifie à J ⊗ k(s) = J/m_sJ'", "bold italic k", "\\mathbf k(s)",
    "convention", 1, "high",
    r"à $\mathscr J\otimes_{\sh{O}_s}\mathbf k(s)=\mathscr J/", r"à $\mathscr J\otimes_{\sh{O}_s}\boldsymbol{k}(s)=\mathscr J/", "")
add(191, "proof of (19.2.4): J_y/(m_sJ_y + J_y^2)",
    "set in the line: 'dont les images dans J_y/(m_sJ_y+J_y²) forment une base'",
    "displayed with \\[ ... \\]",
    "formula", None, "high",
    "dont les images dans\n\\[\n  \\mathscr J_y/(\\mathfrak m_s\\mathscr J_y+\\mathscr J_y^2)\n\\]\nforment une base",
    "dont les images dans $\\mathscr J_y/(\\mathfrak m_s\\mathscr J_y+\\mathscr J_y^2)$ forment une base",
    "Inline as printed; no connecting word lost.")
add(191, "'(qui est libre en vertu de l'hypothèse b))'", "label b) italic", "$b)$",
    "italics", None, "high",
    r"en vertu de l'hypothèse $b)$)", r"en vertu de l'hypothèse \emph{b)})", G88)
add(191, "'et de l'hypothèse b) que les images'", "label b) italic", "$b)$",
    "italics", None, "high",
    r"et de l'hypothèse $b)$ que les images", r"et de l'hypothèse \emph{b)} que les images", G88)
add(191, "'sections de J_s = J ⊗ k(s)'", "bold italic k", "\\mathbf k(s)",
    "convention", 1, "high",
    r"$\mathscr J_s=\mathscr J\otimes_{\sh{O}_s}\mathbf k(s)$", r"$\mathscr J_s=\mathscr J\otimes_{\sh{O}_s}\boldsymbol{k}(s)$", "")
add(191, "'engendrent J|U (0_I, 5.2.2)'", "bold 0 with subscript I", "($0_{\\mathrm I}$, 5.2.2)",
    "convention", 2, "high",
    r"engendrent $\mathscr J|U$ ($0_{\mathrm I}$, 5.2.2)", r"engendrent $\mathscr J|U$ ($\mathbf{0}_{\mathrm I}$, 5.2.2)", "")
add(191, "'Le fait que b) entraîne c)'", "labels italic", "$b)$, $c)$",
    "italics", None, "high",
    r"Le fait que $b)$ entraîne $c)$ est alors", r"Le fait que \emph{b)} entraîne \emph{c)} est alors", G88)
add(191, "'conséquence de (0, 15.1.16)'", "bold 0", "($0$, 15.1.16)",
    "convention", 2, "high",
    r"conséquence de ($0$, 15.1.16)", r"conséquence de (\textbf{0}, 15.1.16)", "")
add(191, "'l'équivalence de c) et c')'", "labels italic", "$c)$, $c')$",
    "italics", None, "high",
    r"l'équivalence de $c)$ et $c')$ (qui", r"l'équivalence de \emph{c)} et \emph{c$'$)} (qui", G88)
add(191, "'localement noethériens (0, 15.1.11))'", "bold 0", "($0$, 15.1.11)",
    "convention", 2, "high",
    r"noethériens ($0$, 15.1.11))", r"noethériens (\textbf{0}, 15.1.11))", "")
add(191, "'Enfin, si c) est vérifiée, pour prouver a)'", "labels italic", "$c)$, $a)$",
    "italics", None, "high",
    r"Enfin, si $c)$ est vérifiée, pour prouver $a)$,", r"Enfin, si \emph{c)} est vérifiée, pour prouver \emph{a)},", G88)
add(191, "'pour voir que c) entraîne a)'", "labels italic", "$c)$, $a)$",
    "italics", None, "high",
    r"pour voir que $c)$ entraîne $a)$, il suffit", r"pour voir que \emph{c)} entraîne \emph{a)}, il suffit", G88)
add(191, "'d'appliquer (0, 15.1.6)'", "bold 0", "($0$, 15.1.6)",
    "convention", 2, "high",
    r"d'appliquer ($0$, 15.1.6)", r"d'appliquer (\textbf{0}, 15.1.6)", "")
add(191, "Remarques (19.2.5) (i): 'dans la condition b)'", "label b) italic (remark body roman)", "$b)$",
    "italics", None, "high",
    r"Lorsque dans la condition $b)$, on supprime", r"Lorsque dans la condition \emph{b)}, on supprime",
    G88 + " Judged with the remark body roman (document-wide remark font).")
add(191, "Remarques (19.2.5) (i): 'n'entraîne plus a)'", "label a) italic (remark body roman)", "$a)$",
    "italics", None, "high",
    r"n'entraîne plus $a)$.", r"n'entraîne plus \emph{a)}.",
    G88 + " Judged with the remark body roman (document-wide remark font).")

# ---------------------------------------------------------------- p. 192
add(192, "Corollaire (19.2.6): 'Supposons, soit que ..., soit que ...'",
    "both 'soit' roman inside the italic statement", "both italic",
    "convention", 6, "high",
    r"Supposons, soit que $S$ et $X$ soient localement noethériens, soit que $g$",
    r"Supposons, \textup{soit} que $S$ et $X$ soient localement noethériens, \textup{soit} que $g$", "")
add(192, "Corollaire (19.2.6), last words: 'transversalement régulière au point x'",
    "au point x (no point x is introduced; the statement concerns u(y) and y)",
    "$x$ (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "The immersion Y→X is transversally regular at a point of Y (Définition (19.2.2)), here the point y of the hypotheses; x is not defined in (19.2.6). The diplomatic TeX keeps the printed reading. Probably an authors' slip (also in the proof, next entry).",
    corrected=r"au point $y$", nofix=True)
add(192, "proof of (19.2.6): 'l'immersion Y_s→X_s est régulière au point x'",
    "au point x", "$x$ (keeps the printed reading)",
    "misprint_in_print", None, "medium", None, None,
    "As in the statement: condition b) of (19.2.4) asks for regularity of Y_s→X_s at the point y. The diplomatic TeX keeps the printed reading.",
    corrected=r"au point $y$", nofix=True)
add(192, "proof of (19.2.6): '(19.2.4, b))'", "label b) italic", "$b)$",
    "italics", None, "high",
    r"d'appliquer (19.2.4, $b)$).", r"d'appliquer (19.2.4, \emph{b)}).", G88)
add(192, "Proposition (19.2.7): label (i)", "upright", "\\item[(i)] italic", "convention", 6, "high",
    r"\item[(i)] Toute $S$-immersion ouverte", r"\item[\textup{(i)}] Toute $S$-immersion ouverte", G16)
add(192, "Proposition (19.2.7): label (ii)", "upright", "\\item[(ii)] italic", "convention", 6, "high",
    r"\item[(ii)] Soient $f:Y\to X$ une $S$-immersion", r"\item[\textup{(ii)}] Soient $f:Y\to X$ une $S$-immersion", G16)
add(192, "Proposition (19.2.7): label (iii)", "upright", "\\item[(iii)] italic", "convention", 6, "high",
    r"\item[(iii)] Si $f:Y\to X$ et $g:Z\to Y$", r"\item[\textup{(iii)}] Si $f:Y\to X$ et $g:Z\to Y$", G16)
add(192, "Proposition (19.2.7): label (iv)", "upright", "\\item[(iv)] italic", "convention", 6, "high",
    r"\item[(iv)] Soient $X$ un $S$-préschéma, $f:Y\to X$", r"\item[\textup{(iv)}] Soient $X$ un $S$-préschéma, $f:Y\to X$", G16)
add(192, "Proposition (19.2.7): label (v)", "upright", "\\item[(v)] italic", "convention", 6, "high",
    r"\item[(v)] Sous les conditions", r"\item[\textup{(v)}] Sous les conditions", G16)
add(192, "Proposition (19.2.7) (v): 'Sous les conditions générales de (iv)'",
    "the reference (iv) upright", "(iv) italic inside the statement",
    "convention", 6, "high",
    r"générales de (iv), supposons", r"générales de \textup{(iv)}, supposons", "")
add(192, "proof of (19.2.7): 'déjà par (19.2.4, b))'", "label b) italic", "$b)$",
    "italics", None, "high",
    r"par (19.2.4, $b)$) que $Z$", r"par (19.2.4, \emph{b)}) que $Z$", G88)

# ---------------------------------------------------------------- p. 193
add(193, "Proposition (19.2.8): '(0⩽n<m)'", "upright parentheses around the formula", "($0\\leq n<m$) italic parentheses",
    "convention", 6, "high",
    r"$\mathscr J^n/\mathscr J^m$ ($0\leq n<m$) sont", r"$\mathscr J^n/\mathscr J^m$ \textup{(}$0\leq n<m$\textup{)} sont",
    "Parentheses around a formula; the edition's form \\textup{(}...\\textup{)}.")
add(193, "Proposition (19.2.8): Gr_n(u') = Gr_n(u) ⊗ O_{S'}",
    "set in the line: 'on a Gr_n(u') = Gr_n(u)⊗_{O_S}O_{S'} à isomorphisme près pour tout n>0'",
    "displayed with \\[ ... \\]",
    "formula", None, "high",
    "on a\n\\[\n  \\sh{G}r_n(u')=\\sh{G}r_n(u)\\otimes_{\\sh{O}_S}\\sh{O}_{S'}\n\\]\nà isomorphisme près",
    "on a $\\sh{G}r_n(u')=\\sh{G}r_n(u)\\otimes_{\\sh{O}_S}\\sh{O}_{S'}$ à isomorphisme près",
    "Inline as printed; no connecting word lost.")
add(193, "proof of (19.2.8): '(0_I, 6.1.2)'", "bold 0 with subscript I", "($0_{\\mathrm I}$, 6.1.2)",
    "convention", 2, "high",
    r"résulte alors de ($0_{\mathrm I}$, 6.1.2)", r"résulte alors de ($\mathbf{0}_{\mathrm I}$, 6.1.2)", "")
add(193, "Proposition (19.2.9): 'au point x (6.8.1)'", "reference (6.8.1) upright", "(6.8.1) italic inside the statement",
    "convention", 6, "high",
    r"au point $x$ (6.8.1). Alors", r"au point $x$ \textup{(6.8.1)}. Alors", "")
add(193, "Proposition (19.2.9): label (i)", "upright", "\\item[(i)] italic", "convention", 6, "high",
    r"\item[(i)] L'injection canonique", r"\item[\textup{(i)}] L'injection canonique", G16)
add(193, "Proposition (19.2.9): label (ii)", "upright", "\\item[(ii)] italic", "convention", 6, "high",
    r"\item[(ii)] Le morphisme $g=f\circ j", r"\item[\textup{(ii)}] Le morphisme $g=f\circ j", G16)
add(193, "Proposition (19.2.9) (ii): the parenthesis '(ce qui équivaut à dire, ... de Cohen-Macaulay)'",
    "the whole parenthesis is roman", "italic (inside the statement)",
    "convention", 6, "high",
    r"(ce qui équivaut à dire, compte tenu de (i), que toutes les fibres $g^{-1}(g(y))$ de $g$ sont des préschémas de Cohen-Macaulay)",
    r"\textup{(ce qui équivaut à dire, compte tenu de (i), que toutes les fibres $g^{-1}(g(y))$ de $g$ sont des préschémas de Cohen-Macaulay)}",
    "")
add(193, "Proposition (19.2.9): label (iii)", "upright", "\\item[(iii)] italic", "convention", 6, "high",
    r"\item[(iii)] Le point $x$", r"\item[\textup{(iii)}] Le point $x$", G16)
add(193, "proof of (19.2.9): 'suite régulière (0, 16.5.7)'", "bold 0", "($0$, 16.5.7)",
    "convention", 2, "high",
    r"suite régulière ($0$, 16.5.7)", r"suite régulière (\textbf{0}, 16.5.7)", "")
add(193, "proof of (19.2.9): 'l'équivalence de c) et a) dans (11.3.8)'", "labels italic", "$c)$, $a)$",
    "italics", None, "high",
    r"l'équivalence de $c)$ et $a)$ dans (11.3.8)", r"l'équivalence de \emph{c)} et \emph{a)} dans (11.3.8)", G88)
add(193, "proof of (19.2.9): 'est un morphisme plat'", "'plat' italic", "roman",
    "italics", None, "high",
    r"est un morphisme plat. Comme", r"est un morphisme \emph{plat}. Comme", "")
add(193, "proof of (19.2.9): 'par construction (0, 16.3.6)'", "bold 0", "($0$, 16.3.6)",
    "convention", 2, "high",
    r"par construction ($0$, 16.3.6)", r"par construction (\textbf{0}, 16.3.6)", "")
add(193, "proof of (19.2.9): 'Enfin, l'anneau O_{Y_s,x}, étant artinien,'",
    "comma after O_{Y_s,x} (the participial phrase between two commas)", "no comma before 'étant'",
    "punctuation", None, "high",
    r"l'anneau $\sh{O}_{Y_s,x}$ étant artinien", r"l'anneau $\sh{O}_{Y_s,x}$, étant artinien",
    "Crop p193_comma.png.")
add(193, "proof of (19.2.9): 'Cohen-Macaulay (0, 16.5.1)'", "bold 0", "($0$, 16.5.1)",
    "convention", 2, "high",
    r"Cohen-Macaulay ($0$, 16.5.1)", r"Cohen-Macaulay (\textbf{0}, 16.5.1)", "")
add(193, "end of the p. 193 segment: heading 19.3",
    "printed p. 193 ends with '... définie dans (17.16.3, (i)).'; the heading '19.3. Intersections complètes relatives (cas plat).' opens p. 194",
    "\\subsection{Intersections complètes relatives (cas plat).} and its \\EGAReaderTarget stand before \\oldpage[IV-4]{194}",
    "marker", None, "high",
    "\\subsection{Intersections complètes relatives (cas plat).}\n\\EGAReaderTarget{ega4.c04.subsec.19-3}{subsection:IV.19.3}\n\n",
    "",
    "Two-part move (the heading moves, not the marker, so each edit stays in its own page segment): part 1 of 2 removes the heading here; the first p. 194 finding re-inserts it after \\oldpage[IV-4]{194}. Apply both or neither.")

# ---------------------------------------------------------------- p. 194
add(194, "top of p. 194: heading 19.3", "p. 194 begins with '19.3. Intersections complètes relatives (cas plat).'",
    "the heading is in the p. 193 segment", "marker", None, "high",
    "\\oldpage[IV-4]{194}\n\n\\begin{definition}[19.3.1]",
    "\\oldpage[IV-4]{194}\n\n\\subsection{Intersections complètes relatives (cas plat).}\n\\EGAReaderTarget{ega4.c04.subsec.19-3}{subsection:IV.19.3}\n\n\\begin{definition}[19.3.1]",
    "Part 2 of 2 with the last p. 193 finding (which removes the heading before the marker). Net result: \\oldpage[IV-4]{194} moves before \\subsection{Intersections complètes relatives (cas plat).}.")
add(194, "Définition (19.3.1): '(ou encore, anneau d'intersection complète absolue, s'il y a danger de confusion)'",
    "only 'absolue' roman; 'anneau d'intersection complète' italic (italic parentheses)",
    "\\emph{anneau d'intersection complète absolue} (all upright)",
    "convention", 6, "high",
    r"(ou encore, \emph{anneau d'intersection complète absolue}, s'il",
    r"(ou encore, anneau d'intersection complète \emph{absolue}, s'il", "")
add(194, "Définition (19.3.1): 'complet régulier B par un idéal régulier (i.e. (16.9.7) un idéal engendré ... de B)'",
    "both 'régulier', 'i.e.', the reference (16.9.7) and both parentheses upright; 'un idéal engendré par une suite régulière d'éléments de' italic",
    "all italic", "convention", 6, "high",
    r"complet régulier $B$ par un idéal régulier (i.e. (16.9.7) un idéal engendré par une suite régulière d'éléments de $B$)",
    r"complet \textup{régulier} $B$ par un idéal \textup{régulier (i.e. (16.9.7)} un idéal engendré par une suite régulière d'éléments de $B$\textup{)}",
    "")
add(194, "end of the statement (19.3.1): the definition runs on over 'Tout anneau local régulier ...' and 'On dit qu'un préschéma ...'",
    "the statement ends at '... d'éléments de B).'; the two following paragraphs are roman, with 'intersection complète' and 'au point' italic and '(absolue)' roman",
    "\\end{definition} after '... d'intersection complète.' (both paragraphs italic, the \\emph words upright)",
    "italics", None, "high",
    "\n\nTout anneau local régulier",
    "\n\\end{definition}\n\nTout anneau local régulier",
    "Edit 1 of 2 (GLOBAL_ISSUES 58 pattern): apply together with the next edit. Does not overlap the previous entry (which ends at '$B$\\textup{)}').")
add(194, "end of the paragraph 'On dit qu'un préschéma localement noethérien ...'", "(see previous entry)", "the old \\end{definition}",
    "italics", None, "high",
    "complète.\n\\end{definition}",
    "complète.",
    "Edit 2 of 2: apply together with the previous edit.")
add(194, "Proposition (19.3.2): '(i.e. (16.9.7) engendré par une suite régulière d'éléments de B)'",
    "'i.e.', (16.9.7) and both parentheses upright; 'engendré ... de' italic", "all italic",
    "convention", 6, "high",
    r"soit régulier (i.e. (16.9.7) engendré par une suite régulière d'éléments de $B$).",
    r"soit régulier \textup{(i.e. (16.9.7)} engendré par une suite régulière d'éléments de $B$\textup{)}.", "")
add(194, "proof of (19.3.2): '(en vertu de (0, 17.1.5))'", "bold 0", "($0$, 17.1.5)",
    "convention", 2, "high",
    r"(en vertu de ($0$, 17.1.5))", r"(en vertu de (\textbf{0}, 17.1.5))", "")
add(194, "proof of (19.3.2): 'A et B sont complets'", "'complets' italic", "roman",
    "italics", None, "high",
    r"sont complets. Par hypothèse", r"sont \emph{complets}. Par hypothèse", "")
add(194, "proof of (19.3.2): 'noethérien complet régulier B''", "'régulier' italic", "roman",
    "italics", None, "high",
    r"complet régulier $B'$ tel que", r"complet \emph{régulier} $B'$ tel que", "")
add(194, "proof of (19.3.2): 'un idéal régulier de B''", "'régulier' italic", "roman",
    "italics", None, "high",
    r"est un idéal régulier de $B'$", r"est un idéal \emph{régulier} de $B'$", "")
add(194, "proof of (19.3.2): 'B'→A (0, 18.1.2)'", "bold 0", "($0$, 18.1.2)",
    "convention", 2, "high",
    r"$B'\to A$ ($0$, 18.1.2); nous", r"$B'\to A$ (\textbf{0}, 18.1.2); nous", "")
add(194, "Lemme (19.3.2.1): 'et posons G = E×_A F (0, 18.1.2)'",
    "bold 0; the reference and its parentheses upright inside the italic statement", "($0$, 18.1.2) light 0 and italic",
    "convention", 2, "high",
    r"posons $G=E\times_A F$ ($0$, 18.1.2).", r"posons $G=E\times_A F$ \textup{(\textbf{0}, 18.1.2)}.",
    "One edit for the bold 0 (convention 2) and the upright reference (convention 6).")
add(194, "Lemme (19.3.2.1): label (i)", "upright", "\\item[(i)] italic", "convention", 6, "high",
    r"\item[(i)] Si $f$ est surjectif", r"\item[\textup{(i)}] Si $f$ est surjectif", G16)
add(194, "Lemme (19.3.2.1): label (ii)", "upright", "\\item[(ii)] italic", "convention", 6, "high",
    r"\item[(ii)] Si $A$, $E$ et $F$", r"\item[\textup{(ii)}] Si $A$, $E$ et $F$", G16)
add(194, "Lemme (19.3.2.1): label (iii) and 'Si les conditions de (i) et (ii) sont vérifiées'",
    "the label (iii) and the references (i), (ii) upright", "\\item[(iii)] and (i), (ii) italic inside the statement",
    "convention", 6, "high",
    r"\item[(iii)] Si les conditions de (i) et (ii) sont vérifiées",
    r"\item[\textup{(iii)}] Si les conditions de \textup{(i)} et \textup{(ii)} sont vérifiées",
    "One edit for the label and the two references. " + G16)
add(194, "proof of (19.3.2.1) (i): 'Compte tenu de (0, 18.1.3 et 18.1.5)'", "bold 0", "($0$, 18.1.3 et 18.1.5)",
    "convention", 2, "high",
    r"($0$, 18.1.3 et 18.1.5)", r"(\textbf{0}, 18.1.3 et 18.1.5)", "")
add(194, "end of the p. 194 segment: 'on en | conclut' (break with p. 195)",
    "printed p. 194 ends mid-sentence '... on a aussi y∉s; on en' and p. 195 begins 'conclut que x et y sont inversibles'",
    "a blank line before \\oldpage[IV-4]{195} (and another after it) makes a paragraph break inside item (ii)",
    "marker", None, "high",
    "on a aussi $y\\notin\\mathfrak s$; on en\n\n",
    "on a aussi $y\\notin\\mathfrak s$; on en\n",
    "BOUNDARY FIX (page break with p. 195). The marker is at the right place; this edit removes the blank line before it. The blank line after \\oldpage[IV-4]{195} ('\\oldpage[IV-4]{195}\\n\\nconclut' -> '\\oldpage[IV-4]{195}\\nconclut', p. 195 segment) must go too (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")

# ---------------------------------------------------------------- checks
src = SRC.read_bytes().decode("utf-8")
marks = {int(m.group(1)): m.start() for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", src)}
bad = 0
for f in F:
    if f["fix"] is None:
        continue
    old = f["fix"]["old"]
    p = f["page"]
    pg = (RUN / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    n_page = pg.count(old)
    n_src = src.count(old)
    seg = src[marks[p]:marks[p + 1]]
    n_seg = seg.count(old)
    if n_page != 1 or n_src != 1 or n_seg != 1:
        bad += 1
        print("CHECK", p, repr(old[:80]), "page", n_page, "src", n_src, "seg", n_seg)
# overlaps within a page
for p in range(190, 195):
    pg = (RUN / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    spans = []
    for f in F:
        if f["page"] == p and f["fix"]:
            i = pg.find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP", p, a, b)
print("findings:", len(F), "problems:", bad)
from collections import Counter
c = Counter((f["page"], "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")) for f in F)
for p in range(190, 195):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT)
