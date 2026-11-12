"""Build findings_185_189.json (pages 185-189 of EGA IV part 2) and check every fix.

Usage: python -I make_findings.py <run_IV2 folder>
'¶' in the raw strings below stands for a line break (LF).
"""
import json
import sys
from pathlib import Path

RUN = Path(sys.argv[1])
OUT = RUN / 'findings_185_189.json'


def N(s):
    return s.replace('¶', '\n')


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note='', corrected=None):
    item = {
        'page': page, 'where': where, 'scan': scan, 'tex': tex, 'kind': kind,
        'convention': conv, 'confidence': conf,
        'fix': None if old is None else {'old': N(old), 'new': N(new)},
    }
    if corrected is not None:
        item['corrected'] = N(corrected)
    item['note'] = note
    F.append(item)


HYPHEN_NOTE = ("The print has a hyphen (same length as the hyphen in 'Â-module', enlarged crop of p. 185). "
               "ega4-2-fr.tex writes 'Cohen--Macaulay' 43 times and 'Cohen-Macaulay' 58 times: one global replace would cover all.")
HAT_NOTE = ("Hat over B only, prime after it (enlarged crop): the analogue of convention 8 for a hat and a prime "
            "(as reported for EGA I pp. 66, 196, EGA II pp. 170-171, 0_IV pp. 91, 93, 215).")
LONGDASH = "long dash X—... (set difference)"

# ---------------------------------------------------------------- page 185
add(185, "l. 1: 'un Â-module de Cohen-Macaulay'", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)",
    'punctuation', None, 'medium', r"-module de¶Cohen--Macaulay", r"-module de¶Cohen-Macaulay", HYPHEN_NOTE)
add(185, "l. 1: '(0, 16.5.2)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.5.2)", r"(\textbf{0}, 16.5.2)")
add(185, "l. 2: 'par suite (0, 16.5.4)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.5.4)", r"(\textbf{0}, 16.5.4)")
add(185, "Remarque (7.1.6): 'des schémas de Cohen-Macaulay'", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)",
    'punctuation', None, 'medium', r"de Cohen--Macaulay; par suite", r"de Cohen-Macaulay; par suite", HYPHEN_NOTE)
add(185, "proof of (7.1.7): 'si l'on pose B = A_q, B' = A'_{q'} est un B-module plat'",
    "no second B' (enlarged crop): '..., B' = A'_{q'}  est un B-module plat'",
    "'$B'=A'_{\\mathfrak q'}$, $B'$ est un'", 'extra', None, 'high',
    r"$B'=A'_{\mathfrak q'}$, $B'$ est un", r"$B'=A'_{\mathfrak q'}$ est un",
    "The TeX adds ', B''. The printed sentence is complete as it stands (B' = A'_{q'} is the subject of "
    "'est un B-module plat'), so it is not treated as a misprint.")
add(185, "proof of (7.1.7): '(0_I, 6.3.2)'", "bold 0 with subscript I", "plain 0", 'convention', 2, 'high',
    r"(0$_{\mathrm I}$, 6.3.2)", r"(\textbf{0}$_{\mathrm I}$, 6.3.2)",
    "Same form as the p. 116-122 fixes ((\\textbf{0}$_\\mathrm I$, ...)).")
add(185, "proof of (7.1.7): 'Posons C = B̂, C' = B̂''", "B̂' (hat over B, then the prime)", "\\widehat {B'}",
    'formula', None, 'high', r"$C'=\widehat {B'}$", r"$C'=\widehat{B}'$", HAT_NOTE)
add(185, "proof of (7.1.7): 'B' = A'_{q'} (0, 16.1.4)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.1.4)", r"(\textbf{0}, 16.1.4)")
add(185, "proof of (7.1.7): 'théorème de Cohen (0, 19.8.8)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 19.8.8)", r"(\textbf{0}, 19.8.8)")
add(185, "proof of (7.1.7): 'il en est de même de B' (0, 17.3.9)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 17.3.9)", r"(\textbf{0}, 17.3.9)")
add(185, "proof of (7.1.7), last line: 'en vertu de (7.1.3, (i))'", "(7.1.3, (i)) (enlarged crop)", "(7.1.3, (ii))",
    'number', None, 'high', r"(7.1.3, (ii))", r"(7.1.3, (i))",
    "The printed (i) is the right reference: (7.1.3, (i)) gives that A is equidimensional when A' is flat over A, "
    "equidimensional and catenary, which is the step C -> C' here; (ii) is about quotients A/a. The TeX of p. 186 "
    "has (7.1.3, (i)) for the same step.")
add(185, "Théorème (7.1.8), label a)", "label upright (enlarged crop)", "\\item[a)] inside the italic statement",
    'convention', 6, 'high', r"\item[a)] Tout anneau", r"\item[\textup{a)}] Tout anneau")
add(185, "Théorème (7.1.8), label b)", "label upright (enlarged crop)", "\\item[b)] inside the italic statement",
    'convention', 6, 'high', r"\item[b)] Les anneaux", r"\item[\textup{b)}] Les anneaux")
add(185, "Théorème (7.1.8), label c)", "label upright (enlarged crop)", "\\item[c)] inside the italic statement",
    'convention', 6, 'high', r"\item[c)] Tout anneau local", r"\item[\textup{c)}] Tout anneau local")
add(185, "Théorème (7.1.8) c): 'essentiellement de type fini (1.3.8) et qui'", "(1.3.8) upright",
    "italic (statement environment)", 'convention', 6, 'high',
    r"fini (1.3.8) et qui", r"fini \textup{(1.3.8)} et qui")
add(185, "proof of (7.1.8), l. 1: 'Il est trivial que c) entraîne a) et que a) entraîne b).'",
    "c), a), a), b) italic", "upright", 'italics', None, 'high',
    r"Il est trivial que c) entraîne a) et que a) entraîne b).",
    r"Il est trivial que \emph{c)} entraîne \emph{a)} et que \emph{a)} entraîne \emph{b)}.")
add(185, "proof of (7.1.8), l. 2-3: 'b) entraîne a) en vertu de (7.1.4, (ii))'", "b), a) italic", "upright",
    'italics', None, 'high', r"b) entraîne a) en vertu de (7.1.4, (ii))",
    r"\emph{b)} entraîne \emph{a)} en vertu de (7.1.4, (ii))")
add(185, "proof of (7.1.8), l. 3: 'Il reste à voir que a) implique c).'", "a), c) italic", "upright",
    'italics', None, 'high', r"voir que a) implique¶c).", r"voir que \emph{a)} implique¶\emph{c)}.")
add(185, "proof of (7.1.8), 2nd paragraph: 'il résulte de a) et de (7.1.7)'", "a) italic", "upright",
    'italics', None, 'high', r"résulte de a) et de (7.1.7)", r"résulte de \emph{a)} et de (7.1.7)")
add(185, "proof of (7.1.8), 2nd paragraph: 'en vertu de a), tout anneau quotient intègre de A/r'", "a) italic",
    "upright", 'italics', None, 'high', r"vertu de a), tout anneau", r"vertu de \emph{a)}, tout anneau")
add(185, "end of the p. 185 segment: 'on voit qu'on peut aussi supposer' / p. 186 'que A est intègre'",
    "the sentence runs on over the page break", "blank line before \\oldpage[IV-2]{186} (paragraph break)",
    'marker', None, 'high', r"aussi supposer¶¶", r"aussi supposer¶",
    "The marker is in the right place and has no blank line after it, so this edit alone joins the paragraph.")

# ---------------------------------------------------------------- page 186
add(186, "2nd paragraph: 'On sait alors que B̂' est un B̂-module plat'", "B̂' (hat over B, then the prime)",
    "\\widehat {B'}", 'formula', None, 'high',
    r"que $\widehat {B'}$ est un $\widehat B$-module", r"que $\widehat{B}'$ est un $\widehat B$-module", HAT_NOTE)
add(186, "2nd paragraph: 'comme B̂' est caténaire (5.6.4)'", "B̂'", "\\widehat {B'}", 'formula', None, 'high',
    r"$\widehat {B'}$ est caténaire", r"$\widehat{B}'$ est caténaire", HAT_NOTE)
add(186, "2nd paragraph: 'il suffira de prouver que B̂' est équidimensionnel'", "B̂'", "\\widehat {B'}",
    'formula', None, 'high', r"$\widehat {B'}$ est \emph{équidimensionnel}",
    r"$\widehat{B}'$ est \emph{équidimensionnel}", HAT_NOTE)
add(186, "3rd paragraph: 'théorème de Cohen (0, 19.8.8)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0,¶19.8.8)", r"(\textbf{0},¶19.8.8)")
add(186, "3rd paragraph: 'il en est de même de B' (0, 17.3.9)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 17.3.9)", r"(\textbf{0}, 17.3.9)")
add(186, "3rd paragraph: 'il suffit de prouver que B' est équidimensionnel; et'", "'équidimensionnel' italic (enlarged crop)",
    "upright", 'italics', None, 'high', r"prouver que $B'$ est équidimensionnel;",
    r"prouver que $B'$ est \emph{équidimensionnel};")
add(186, "Définition (7.1.9): 'de (7.1.8) sont vérifiées'", "(7.1.8) upright", "italic (statement environment)",
    'convention', 6, 'high', r"équivalentes de (7.1.8) sont", r"équivalentes de \textup{(7.1.8)} sont")
add(186, "Définition (7.1.9): 'un anneau formellement caténaire'",
    "'formellement caténaire' in the same italic as the rest of the definition (enlarged crop)",
    "\\emph{...} inside the italic definition (comes out upright)", 'convention', 6, 'high',
    r"\emph{formellement caténaire}", r"formellement caténaire")
add(186, "Proposition (7.1.10): 'anneau local de Cohen-Macaulay'", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)",
    'punctuation', None, 'medium', r"local de Cohen--Macaulay est", r"local de Cohen-Macaulay est", HYPHEN_NOTE)
add(186, "Proposition (7.1.11), label (i)", "label upright", "\\item[(i)] inside the italic statement",
    'convention', 6, 'high', r"\item[(i)] Un anneau", r"\item[\textup{(i)}] Un anneau")
add(186, "Proposition (7.1.11), label (ii)", "label upright", "\\item[(ii)] inside the italic statement",
    'convention', 6, 'high', r"\item[(ii)] Si $A$", r"\item[\textup{(ii)}] Si $A$")
add(186, "proof of (7.1.11): 'de la condition c) de (7.1.8)'", "c) italic", "upright", 'italics', None, 'high',
    r"la condition c) de (7.1.8)", r"la condition \emph{c)} de (7.1.8)")
add(186, "proof of (7.1.11): 'en vertu de la condition b) de (7.1.8)'", "b) italic", "upright", 'italics', None,
    'high', r"la condition b) de (7.1.8)", r"la condition \emph{b)} de (7.1.8)")

# ---------------------------------------------------------------- page 187
add(187, "Remarques (7.1.12) (ii): 'A de dimension 1 est nécessairement'", "'de dimension' italic, the figure 1 roman (enlarged crop)",
    "\\emph{de dimension 1} (figure italic)", 'italics', None, 'medium',
    r"\emph{de dimension 1} est", r"\emph{de dimension} 1 est",
    "Remark body judged as roman (document-wide item).")
add(187, "Corollaire (7.1.13), l. 1-2: 'irréductible de dimension 1, X un préschéma'",
    "figure 1 roman inside the italic statement (enlarged crop)", "italic (statement environment)",
    'convention', 6, 'medium', r"irréductible de dimension 1,", r"irréductible de dimension \textup{1},",
    "Same treatment as EGA I p. 156 ('de dimension \\textup{0}').")
add(187, "Corollaire (7.1.13), end: subscript k(η) of deg.tr", "bold upright k at subscript size (enlarged crop)",
    "plain k", 'convention', 1, 'high', r"à¶$\deg.\operatorname{tr}_{k(\eta)}",
    r"à¶$\deg.\operatorname{tr}_{\mathbf{k}(\eta)}", "\\mathbf{k}: bold upright in subscripts (GLOBAL_ISSUES 48).")
add(187, "Corollaire (7.1.13), end: 'k(ξ).'", "bold italic k (enlarged crop)", "plain k", 'convention', 1, 'high',
    r"k(\xi)$.¶\end{corollary}", r"\boldsymbol{k}(\xi)$.¶\end{corollary}")
add(187, "proof of (7.1.13), l. 2: subscript k(η) of deg.tr", "bold upright k at subscript size (enlarged crop)",
    "plain k", 'convention', 1, 'high', r"de dimension $\deg.\operatorname{tr}_{k(\eta)}",
    r"de dimension $\deg.\operatorname{tr}_{\mathbf{k}(\eta)}", "\\mathbf{k}: bold upright in subscripts (GLOBAL_ISSUES 48).")
add(187, "proof of (7.1.13), l. 2: 'k(ξ) (5.2.1)'", "bold italic k (enlarged crop)", "plain k", 'convention', 1,
    'high', r"k(\xi)$ (5.2.1)", r"\boldsymbol{k}(\xi)$ (5.2.1)")
add(187, "proof of (7.1.13), display: 'dim(Z) = 1 + dim(f^{-1}(η)) — dim(O_{X,z})'", "long dash for the subtraction (enlarged crop)",
    "-", 'convention', 7, 'high', r"(\eta))-\dim", r"(\eta))\setmin\dim", "Subtraction (GLOBAL_ISSUES 23).")
add(187, "proof of (7.1.13): 'dim(O_{X,z}) ⩽ dim(O_y) (0, 16.3.9)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0,¶16.3.9)", r"(\textbf{0},¶16.3.9)")
add(187, "heading 7.2: 'Anneaux strictement formellement caténaires.'", "final full stop", "no full stop",
    'punctuation', None, 'high', r"\subsection{Anneaux strictement formellement caténaires}",
    r"\subsection{Anneaux strictement formellement caténaires.}", "As the p. 92 heading fix (GLOBAL_ISSUES 43).")
add(187, "Notations (7.2.1), l. 1: 'Pour un anneau intègre noethérien A'", "'intègre noethérien' italic (enlarged crop)",
    "upright (env body is roman)", 'italics', None, 'high', r"un anneau intègre noethérien $A$",
    r"un anneau \emph{intègre noethérien} $A$")
add(187, "Notations (7.2.1), l. 3: 'de A de hauteur 1 (5.10.17)'", "'de hauteur' italic, 1 roman", "upright",
    'italics', None, 'high', r"de $A$ de hauteur 1", r"de $A$ \emph{de hauteur} 1")
add(187, "Notations (7.2.1), l. 3: 'Si A est un anneau local noethérien intègre'", "'local' italic ('noethérien intègre' roman)",
    "upright", 'italics', None, 'high', r"anneau local noethérien intègre, nous",
    r"anneau \emph{local} noethérien intègre, nous")
add(187, "Notations (7.2.1), l. 5: 'distincts de l'idéal maximal.'", "italic", "upright", 'italics', None, 'high',
    r"distincts de l'idéal maximal.", r"\emph{distincts de l'idéal maximal}.")
add(187, "Notations (7.2.1), 2nd paragraph: 'que A est équidimensionnel et sans idéaux...'", "'équidimensionnel' italic",
    "upright", 'italics', None, 'high', r"$A$ est¶équidimensionnel et \emph{sans",
    r"$A$ est¶\emph{équidimensionnel} et \emph{sans")
add(187, "Exemple (7.2.1.1), l. 1: 'de dimension 1. Alors'", "'de dimension' italic, the figure 1 roman (enlarged crop)",
    "\\emph{de dimension 1} (figure italic)", 'italics', None, 'medium',
    r"\emph{de dimension 1}. Alors", r"\emph{de dimension} 1. Alors")
add(187, "Exemple (7.2.1.1), label a)", "label italic", "\\item[a)] upright (example body is roman)", 'italics', None,
    'high', r"\item[a)] $A$ est sans", r"\item[\emph{a)}] $A$ est sans")
add(187, "Exemple (7.2.1.1), label a')", "label italic, parenthesis included", "\\item[$a'$)] (upright parenthesis)",
    'italics', None, 'high', r"\item[$a'$)]", r"\item[\emph{a$'$)}]")
add(187, "Exemple (7.2.1.1), label b)", "label italic", "\\item[b)] upright", 'italics', None, 'high',
    r"\item[b)] $A$ est strictement", r"\item[\emph{b)}] $A$ est strictement")
add(187, "Exemple (7.2.1.1), label b')", "label italic, parenthesis included", "\\item[$b'$)] (upright parenthesis)",
    'italics', None, 'high', r"\item[$b'$)]", r"\item[\emph{b$'$)}]")
add(187, "Exemple (7.2.1.1), label c)", "label italic", "\\item[c)] upright", 'italics', None, 'high',
    r"\item[c)] $A$ est un anneau", r"\item[\emph{c)}] $A$ est un anneau")
add(187, "Exemple (7.2.1.1) c): 'un anneau de Cohen-Macaulay.'", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)",
    'punctuation', None, 'medium', r"de Cohen--Macaulay.", r"de Cohen-Macaulay.", HYPHEN_NOTE)
add(187, "after Exemple (7.2.1.1): 'En effet a) signifie'", "a) italic", "upright", 'italics', None, 'high',
    r"En effet a) signifie", r"En effet \emph{a)} signifie")
add(187, "end of the p. 187 segment: 'tous distincts de m, et' / p. 188 'pour un tel idéal p'",
    "the sentence runs on over the page break", "blank line before \\oldpage[IV-2]{188} (paragraph break)",
    'marker', None, 'high', r"distincts de $\mathfrak m$, et¶¶", r"distincts de $\mathfrak m$, et¶",
    "Apply together with the p. 188 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 188
add(188, "top of the page: 'pour un tel idéal p' (continues 'tous distincts de m, et')",
    "the sentence runs on over the page break", "blank line after \\oldpage[IV-2]{188}", 'marker', None, 'high',
    r"\oldpage[IV-2]{188}¶¶pour un tel", r"\oldpage[IV-2]{188}¶pour un tel",
    "Apply together with the p. 187 entry that removes the blank line before the marker.")
add(188, "l. 1-2: 'donc a) implique b). Inversement, b) implique que'", "a), b), b) italic", "upright", 'italics',
    None, 'high', r"donc a) implique b). Inversement, b) implique que",
    r"donc \emph{a)} implique \emph{b)}. Inversement, \emph{b)} implique que")
add(188, "l. 3: 'et par suite b) implique a). On sait déjà que a) et c) sont'", "b), a), a), c) italic", "upright",
    'italics', None, 'high', r"et par suite b) implique a). On sait déjà que¶a) et c) sont",
    r"et par suite \emph{b)} implique \emph{a)}. On sait déjà que¶\emph{a)} et \emph{c)} sont")
add(188, "l. 4-5: 'A est un anneau de Cohen-Macaulay ou'", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)",
    'punctuation', None, 'medium', r"anneau de Cohen--Macaulay ou", r"anneau de Cohen-Macaulay ou", HYPHEN_NOTE)
add(188, "l. 5: 'que Â est un anneau de Cohen-Macaulay'", "Cohen-Macaulay (hyphen)", "Cohen--Macaulay (en dash)",
    'punctuation', None, 'medium', r"$\widehat A$ est un anneau de Cohen--Macaulay",
    r"$\widehat A$ est un anneau de Cohen-Macaulay", HYPHEN_NOTE)
add(188, "l. 5: '(0, 16.5.2)'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"(0, 16.5.2)", r"(\textbf{0}, 16.5.2)")
add(188, "l. 6: 'on voit enfin que a') et b') sont équivalentes à c).'", "a'), b'), c) italic (parentheses included)",
    "$a'$), $b'$) with upright parentheses; c) upright", 'italics', None, 'high',
    r"$a'$) et $b'$) sont équivalentes à¶c).", r"\emph{a$'$)} et \emph{b$'$)} sont équivalentes à¶\emph{c)}.")
add(188, "Proposition (7.2.2): 'j : X—{a} → X l'injection canonique'", LONGDASH, "-", 'convention', 7, 'high',
    r"$j:X-\{a\}\to X$", r"$j:X\setmin\{a\}\to X$")
add(188, "Proposition (7.2.2), label a)", "label upright (enlarged crop)", "\\item[a)] inside the italic statement",
    'convention', 6, 'high', r"\item[a)] Le $\mathscr O_X$", r"\item[\textup{a)}] Le $\mathscr O_X$")
add(188, "Proposition (7.2.2) a): 'j_*(F|X—{a})'", "restriction F|X—{a} on the line (enlarged crop)",
    "subscript |_{X-\\{a\\}}", 'formula', None, 'high', r"Module¶$j_*(\mathscr F|_{X-\{a\}})$",
    r"Module¶$j_*(\mathscr F|X\setmin\{a\})$", "One edit for this finding and the next (long dash).")
add(188, "Proposition (7.2.2) a): 'X—{a}' in j_*(F|X—{a})", LONGDASH, "-", 'convention', 7, 'high', None, None,
    "Covered by the edit of the finding just before (one edit for the whole expression).")
add(188, "Proposition (7.2.2), label b)", "label upright (enlarged crop)", "\\item[b)] inside the italic statement",
    'convention', 6, 'high', r"\item[b)] Pour tout $x'\in", r"\item[\textup{b)}] Pour tout $x'\in")
add(188, "proof of (7.2.2), l. 2: 'j' : X'—{a'} → X''", LONGDASH, "-", 'convention', 7, 'high',
    r"$j':X'-\{a'\}\to X'$", r"$j':X'\setmin\{a'\}\to X'$")
add(188, "proof of (7.2.2), l. 3: 'de dire que j_*(F|X—{a}) est cohérent'", "restriction on the line",
    "subscript |_{X-\\{a\\}}", 'formula', None, 'high', r"dire que $j_*(\mathscr F|_{X-\{a\}})$",
    r"dire que $j_*(\mathscr F|X\setmin\{a\})$", "One edit for this finding and the next (long dash).")
add(188, "proof of (7.2.2), l. 3: 'X—{a}'", LONGDASH, "-", 'convention', 7, 'high', None, None,
    "Covered by the edit of the finding just before (one edit for the whole expression).")
add(188, "proof of (7.2.2), l. 4: 'ou que j'_*(F'|X'—{a'}) est cohérent (5.9.5)'", "restriction on the line",
    "subscript |_{X'-\\{a'\\}}", 'formula', None, 'high', r"ou que¶$j'_*(\mathscr F'|_{X'-\{a'\}})$",
    r"ou que¶$j'_*(\mathscr F'|X'\setmin\{a'\})$", "One edit for this finding and the next (long dash).")
add(188, "proof of (7.2.2), l. 4: 'X'—{a'}'", LONGDASH, "-", 'convention', 7, 'high', None, None,
    "Covered by the edit of the finding just before (one edit for the whole expression).")
add(188, "proof of (7.2.2): 'théorème de Cohen (0, 19.8.8), il résulte'", "bold 0", "plain 0", 'convention', 2,
    'high', r"(0, 19.8.8), il", r"(\textbf{0}, 19.8.8), il")
add(188, "proof of (7.2.2): 'la condition b) de l'énoncé'", "b) italic", "upright", 'italics', None, 'high',
    r"la condition b) de l'énoncé", r"la condition \emph{b)} de l'énoncé")
add(188, "proof of (7.2.2): 'au fait que j'_*(F'|X'—{a'}) est cohérent'", "restriction on the line",
    "subscript |_{X'-\\{a'\\}}", 'formula', None, 'high', r"au fait que $j'_*(\mathscr F'|_{X'-\{a'\}})$",
    r"au fait que $j'_*(\mathscr F'|X'\setmin\{a'\})$", "One edit for this finding and the next (long dash).")
add(188, "proof of (7.2.2): 'X'—{a'}' (second j'_*)", LONGDASH, "-", 'convention', 7, 'high', None, None,
    "Covered by the edit of the finding just before (one edit for the whole expression).")
add(188, "Proposition (7.2.3), l. 1-2: 'celles de (7.2.2),'", "(7.2.2) upright", "italic (statement environment)",
    'convention', 6, 'high', r"celles de¶(7.2.2), les", r"celles de¶\textup{(7.2.2)}, les")
add(188, "Proposition (7.2.3), label a)", "label upright", "\\item[a)] inside the italic statement",
    'convention', 6, 'high', r"\item[a)] $A^{(1)}$", r"\item[\textup{a)}] $A^{(1)}$")
add(188, "Proposition (7.2.3), label b)", "label upright", "\\item[b)] inside the italic statement",
    'convention', 6, 'high', r"\item[b)] Pour toute partie", r"\item[\textup{b)}] Pour toute partie")
add(188, "Proposition (7.2.3) b): 'i : X—T → X'", LONGDASH + " (the subscript of O_{X-T} has a short minus, as the TeX)",
    "-", 'convention', 7, 'high', r"$i:X-T\to X$", r"$i:X\setmin T\to X$")
add(188, "Proposition (7.2.3), label c)", "label upright", "\\item[c)] inside the italic statement",
    'convention', 6, 'high', r"\item[c)] Pour tout $x'", r"\item[\textup{c)}] Pour tout $x'")
add(188, "proof of (7.2.3), l. 2: 'les conditions a) et b) équivalent'", "a), b) italic", "upright", 'italics', None,
    'high', r"les conditions a) et b) équivalent", r"les conditions \emph{a)} et \emph{b)} équivalent")
PARA_SCAN = ("one paragraph: 'propriétés suivantes : a_1) ... cohérent; b_1) ... ⩾2. Compte tenu de (5.9.5), ... "
             "respectivement à : a'_1) ... cohérent; b'_1) posant ... ⩾2. Or, tout point ...' (continuation lines flush left)")
PARA_NOTE = "One of six edits (independent of each other) that remove the paragraph breaks the print does not have in the proof of (7.2.3)."
add(188, "proof of (7.2.3): break before 'a_1)'", PARA_SCAN, "blank line: new paragraph", 'other', None, 'high',
    r"suivantes:¶¶$a_1)$", r"suivantes:¶$a_1)$", PARA_NOTE)
add(188, "proof of (7.2.3): break before 'b_1)'", PARA_SCAN, "blank line: new paragraph", 'other', None, 'high',
    r"cohérent;¶¶$b_1)$", r"cohérent;¶$b_1)$", PARA_NOTE)
add(188, "proof of (7.2.3): break before 'Compte tenu de (5.9.5)'", PARA_SCAN, "blank line: new paragraph", 'other',
    None, 'high', r"$\geqslant2$.¶¶Compte tenu", r"$\geqslant2$.¶Compte tenu", PARA_NOTE)
add(188, "proof of (7.2.3): break before 'a'_1)'", PARA_SCAN, "blank line: new paragraph", 'other', None, 'high',
    r"respectivement à:¶¶$a'_1)$", r"respectivement à:¶$a'_1)$", PARA_NOTE)
add(188, "proof of (7.2.3): break before 'b'_1)'", PARA_SCAN, "blank line: new paragraph", 'other', None, 'high',
    r"cohérent;¶¶$b'_1)$", r"cohérent;¶$b'_1)$", PARA_NOTE)
add(188, "proof of (7.2.3): break before 'Or, tout point de Ass(O_X')'", PARA_SCAN, "blank line: new paragraph",
    'other', None, 'high', r"$\geqslant2$.¶¶Or, tout point", r"$\geqslant2$.¶Or, tout point", PARA_NOTE)
add(188, "last line: 'théorème de Cohen (0, 19.8.8) (ou encore'", "bold 0", "plain 0", 'convention', 2, 'high',
    r"Cohen¶(0, 19.8.8)", r"Cohen¶(\textbf{0}, 19.8.8)")
add(188, "end of the p. 188 segment: '(ou encore' / p. 189 'parce que A' est universellement japonais'",
    "the sentence runs on over the page break", "blank line before \\oldpage[IV-2]{189} (paragraph break)",
    'marker', None, 'high', r"(ou encore¶¶", r"(ou encore¶",
    "Apply together with the p. 189 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 189
add(189, "top of the page: 'parce que A' est universellement japonais (7.6.5))' (continues '(ou encore')",
    "the sentence runs on over the page break", "blank line after \\oldpage[IV-2]{189}", 'marker', None, 'high',
    r"\oldpage[IV-2]{189}¶¶parce que", r"\oldpage[IV-2]{189}¶parce que",
    "Apply together with the p. 188 entry that removes the blank line before the marker.")
add(189, "l. 2: 'les conditions b'_1) et c) sont aussi équivalentes'", "c) italic", "upright", 'italics', None,
    'high', r"$b'_1)$ et c) sont", r"$b'_1)$ et \emph{c)} sont")
for lab in 'abcdef':
    add(189, f"Proposition (7.2.4), label {lab})", "label upright", f"\\item[{lab})] inside the italic statement",
        'convention', 6, 'high', rf"\item[{lab})]", rf"\item[\textup{{{lab})}}]")
add(189, "Proposition (7.2.4) b): 'x ∈ Ass(F) ∩ (X—Z)'", LONGDASH, "-", 'convention', 7, 'high',
    r"\cap(X-Z)$", r"\cap(X\setmin Z)$")
add(189, "Proposition (7.2.4) c): '(où U = X—T)'", LONGDASH, "-", 'convention', 7, 'high',
    r"(où $U=X-T$)", r"(où $U=X\setmin T$)")
add(189, "Proposition (7.2.4) e): '(ou, ce qui revient au même, si Y = Spec(C) ...'",
    "'(ou, ce qui revient au même,' roman; 'si', 'et si U est le complémentaire ...' italic (enlarged crop)",
    "italic (statement environment)", 'convention', 6, 'high', r"finie (ou,¶ce qui revient au même, si",
    r"finie \textup{(ou,¶ce qui revient au même,} si",
    "The closing parenthesis after 'cohérent' is upright too (parenthesis slant, GLOBAL_ISSUES 26; no edit).")
add(189, "proof of (7.2.4), l. 1: 'que a) et b) sont équivalentes, ainsi que c) et d),'", "a), b), c), d) italic",
    "upright", 'italics', None, 'high', r"que a) et b) sont équivalentes, ainsi que c) et d),",
    r"que \emph{a)} et \emph{b)} sont équivalentes, ainsi que \emph{c)} et \emph{d)},")
add(189, "proof of (7.2.4), l. 1-2: 'et que a) entraîne d). L'équivalence de a) et d)'", "a), d), a), d) italic",
    "upright", 'italics', None, 'high', r"et que a) entraîne d). L'équivalence de a) et d) dans",
    r"et que \emph{a)} entraîne \emph{d)}. L'équivalence de \emph{a)} et \emph{d)} dans")
add(189, "proof of (7.2.4), l. 3: 'la condition d) étant une formulation équivalente'", "d) italic", "upright",
    'italics', None, 'high', r"la condition¶d) étant", r"la condition¶\emph{d)} étant")
add(189, "proof of (7.2.4), l. 4: '(7.2.3, b))'", "b) italic", "upright", 'italics', None, 'high',
    r"(7.2.3, b)) en vertu", r"(7.2.3, \emph{b)}) en vertu")
add(189, "proof of (7.2.4), l. 4: 'L'équivalence de e) et f)'", "e), f) italic", "upright", 'italics', None, 'high',
    r"L'équivalence de e) et f) est", r"L'équivalence de \emph{e)} et \emph{f)} est")
add(189, "proof of (7.2.4): 'que si A vérifie a), il en est de même'", "a) italic", "upright", 'italics', None,
    'high', r"vérifie a), il en est", r"vérifie \emph{a)}, il en est")
add(189, "proof of (7.2.4): 'La condition a) pour A entraîne donc (avec les notations de e))'", "a), e) italic",
    "upright", 'italics', None, 'high', r"La condition¶a) pour $A$ entraîne donc (avec les notations de e)) que",
    r"La condition¶\emph{a)} pour $A$ entraîne donc (avec les notations de \emph{e)}) que")
add(189, "proof of (7.2.4): 'que l'anneau C vérifie a), donc aussi c);'", "a), c) italic", "upright", 'italics',
    None, 'high', r"vérifie a), donc aussi c);", r"vérifie \emph{a)}, donc aussi \emph{c)};")
add(189, "proof of (7.2.4): 'appliquer à C la condition c) en prenant'", "c) italic", "upright", 'italics', None,
    'high', r"la condition c) en prenant", r"la condition \emph{c)} en prenant")
add(189, "proof of (7.2.4): 'cela prouve que a) entraîne e). Reste à prouver que e) entraîne a);'",
    "a), e), e), a) italic", "upright", 'italics', None, 'high',
    r"cela prouve que a) entraîne e). Reste¶à prouver que e) entraîne a);",
    r"cela prouve que \emph{a)} entraîne \emph{e)}. Reste¶à prouver que \emph{e)} entraîne \emph{a)};")
add(189, "proof of (7.2.4): 'la condition e) entraîne la condition (7.2.3, c)). Avec les notations de (7.2.3, c)),'",
    "e), c), c) italic", "upright", 'italics', None, 'high',
    r"la condition e)¶entraîne la condition (7.2.3, c)). Avec les notations de (7.2.3, c)),",
    r"la condition \emph{e)}¶entraîne la condition (7.2.3, \emph{c)}). Avec les notations de (7.2.3, \emph{c)}),")
add(189, "proof of (7.2.4): 'et par suite (avec les notations de e)),'", "e) italic", "upright", 'italics', None,
    'high', r"(avec les notations de e)),", r"(avec les notations de \emph{e)}),")
add(189, "proof of (7.2.4): 's'identifie à f^{-1}(Y) (I, 3.6.5)'", "bold I", "plain I", 'convention', 2, 'high',
    r"(I, 3.6.5)", r"(\textbf{I}, 3.6.5)")
add(189, "end of the p. 189 segment: 'que l'on a, dans Y',' / p. 190 'codim(...) ⩾ 2. Comme y' ...'",
    "the sentence runs on over the page break; p. 190 begins with the formula in the running text, flush left (checked on the p. 190 scan)",
    "blank lines before and after \\oldpage[IV-2]{190} (paragraph break)", 'marker', None, 'high',
    r"que l'on a, dans $Y'$,¶¶", r"que l'on a, dans $Y'$,¶",
    "Apply together with the page-190 entry below, which removes the blank line after the marker (outside this page's segment).")
add(190, "top of p. 190: blank line after \\oldpage[IV-2]{190} before 'codim(...) ⩾ 2.'",
    "the formula continues the sentence 'que l'on a, dans Y',' of p. 189 (same paragraph, inline)",
    "blank line after the marker (paragraph break)", 'marker', None, 'high',
    r"\oldpage[IV-2]{190}¶¶$\operatorname{codim}", r"\oldpage[IV-2]{190}¶$\operatorname{codim}",
    "OUTSIDE pages 185-189: 'old' lies in page_190.tex (checked unique there). Second half of the p. 189 end-of-page "
    "entry; apply together. Skip if the pp. 190-194 batch already removes this blank line.")

# ---------------------------------------------------------------- checks
def load(page):
    return (RUN / f'page_{page:03d}.tex').read_text(encoding='utf-8').replace('\r\n', '\n')


ok = True
texts = {}
for item in F:
    fx = item['fix']
    if fx is None:
        continue
    p = item['page']
    texts.setdefault(p, load(p))
    c = texts[p].count(fx['old'])
    if c != 1:
        ok = False
        print('NOT UNIQUE', p, c, repr(fx['old']))
# apply all edits per page in order: each old must still occur exactly once
for p in sorted(texts):
    t = load(p)
    for item in F:
        if item['page'] != p or item['fix'] is None:
            continue
        fx = item['fix']
        c = t.count(fx['old'])
        if c != 1:
            ok = False
            print('SEQUENTIAL PROBLEM', p, c, repr(fx['old']))
            continue
        t = t.replace(fx['old'], fx['new'])
print('all fixes unique and applicable:', ok)

from collections import Counter
cnt = Counter()
for item in F:
    if item['kind'] == 'convention':
        cnt[(item['page'], 'convention')] += 1
    elif item['kind'] == 'misprint_in_print':
        cnt[(item['page'], 'misprint')] += 1
    else:
        cnt[(item['page'], 'normal')] += 1
for p in sorted({i['page'] for i in F}):
    print(p, 'normal', cnt[(p, 'normal')], 'convention', cnt[(p, 'convention')], 'misprint', cnt[(p, 'misprint')])

if ok or '--force' in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding='utf-8')
    print('written', OUT, len(F))
else:
    print('NOT written: fix the problems above')
