"""Build findings_005_009.json for run_IV4 and check every fix's 'old' string.

Fixes inside a page segment must occur exactly once in page_NNN.tex (CRLF normalized to LF).
Fixes marked OUTSIDE are checked against the named release file instead.
"""
import json
import os

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4"
OUT = os.path.join(RUN, "findings_005_009.json")

F = []


def add(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high",
        corrected=None, outside=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_outside"] = outside
    F.append(d)


S9 = "Convention 9: the print has the sharp sign; ^\\# typesets #."
C2 = "Bold chapter number in the reference."
C6REF = "Reference printed upright inside the italic statement."

# ---------------------------------------------------------------- page 5
add(5, "top of p. 5: chapter heading (before the section 16 title)",
    "CHAPITRE IV (fin) ['(fin)' italic, with italic parentheses], then 'ÉTUDE LOCALE DES SCHÉMAS / ET DES MORPHISMES DE SCHÉMAS' in large bold capitals",
    "absent: ega4-16-fr.tex begins with \\section{Invariants différentiels. ...}; EGA_IV4_FR.tex has no chapter heading either",
    "missing",
    {"old": "\\section{Invariants",
     "new": "\\clearpage\n\\thispagestyle{plain}\n\\oldpage[IV-4]{5}\n\\phantomsection\n\\label{chapter:IV4-fr}\n\n\\begin{center}\n{\\large CHAPITRE IV \\textit{(fin)}\\par}\n\\vspace{1.5em}\n{\\Large\\bfseries ÉTUDE LOCALE DES SCHÉMAS\\\\\nET DES MORPHISMES DE SCHÉMAS\\par}\n\\end{center}\n\n\\section{Invariants"},
    "OUTSIDE the page segment: 'old' is line 1 of ega4-16-fr.tex, before the file's first marker (unique there). Same block as the openings of ega4-2-fr.tex (IV-2) and ega4-8-fr.tex (IV-3), with (fin) for (suite); the label chapter:IV4-fr is unused so far. The new block also carries the p. 5 marker: apply together with the next finding (which deletes the old marker), both or neither.",
    outside="ega4-16-fr.tex")

add(5, "top of p. 5: page marker",
    "printed p. 5 begins with the chapter heading, then the section 16 title, then 'Dans ce paragraphe'",
    "\\oldpage[IV-4]{5} stands after \\section{...} and \\label{section:IV.16} (ega4-16-fr.tex line 4): the section title falls before the marker",
    "marker",
    {"old": "\\oldpage[IV-4]{5}\nDans ce paragraphe", "new": "Dans ce paragraphe"},
    "Deletes the misplaced marker; apply only together with the chapter-heading finding above, whose new text puts \\oldpage[IV-4]{5} before the chapter heading and the \\section.")

add(5, "section 16 title",
    "'§ 16. INVARIANTS DIFFÉRENTIELS' / 'MORPHISMES DIFFÉRENTIELLEMENT LISSES' on two centred lines, no full stop between the two titles",
    "\\section{Invariants différentiels. Morphismes différentiellement lisses} (full stop between them)",
    "punctuation",
    {"old": "différentiels. Morphismes", "new": "différentiels\\texorpdfstring{\\\\}{.} Morphismes"},
    "OUTSIDE the page segment (ega4-16-fr.tex line 1, unique there). The print separates the two titles by the line break only (IV-3's § 11 title, by contrast, prints its full stop inside a line); the contents line in ega4-backmatter-contents-fr.tex keeps the full stop (printed contents not checked here). May be treated as heading layout in the heading pass: coordinator's decision. No overlap with the chapter-heading edit.",
    confidence="low", outside="ega4-16-fr.tex")

add(5, "introduction, l. 7: 'dans le cadre affine, dans (0, 21))'",
    "(𝟎, 21): bold 0", "(0, 21), plain 0", "convention",
    {"old": "dans (0, 21))", "new": "dans (\\textbf{0}, 21))"}, C2, convention=2)

add(5, "subsection heading 16.1",
    "'16.1. Invariants normaux d'une immersion.' (final full stop)",
    "\\subsection{Invariants normaux d'une immersion} (no full stop)", "punctuation",
    {"old": "\\subsection{Invariants normaux d'une immersion}",
     "new": "\\subsection{Invariants normaux d'une immersion.}"},
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same form as the IV-1 to IV-3 page fixes.")

add(5, "(16.1.1), l. 2: 'morphisme d'espaces annelés (0_I, 4.1.1)'",
    "(𝟎_I, 4.1.1): bold 0", "(0\\textsubscript{I}, 4.1.1), plain 0", "convention",
    {"old": "(0\\textsubscript{I}, 4.1.1)", "new": "(\\textbf{0}\\textsubscript{I}, 4.1.1)"}, C2, convention=2)

add(5, "(16.1.1), display: 'θ♯ : ψ*(O_X) → O_Y'",
    "θ♯ (sharp sign, enlarged crop)", "\\theta^\\#", "convention",
    {"old": "\\theta^\\#:\\psi^*", "new": "\\theta^\\sharp:\\psi^*"}, S9, convention=9)

add(5, "(16.1.1), after the display: 'soit surjectif, de sorte que'",
    "*surjectif* italic", "surjectif upright", "italics",
    {"old": "soit surjectif, de sorte", "new": "soit \\emph{surjectif}, de sorte"})

add(5, "Définition (16.1.2), l. 2: 'le n-ème invariant normal de f'",
    "'invariant normal' roman inside the italic statement (enlarged crop)",
    "italic (definition environment)", "convention",
    {"old": "-ème invariant normal", "new": "-ème \\textup{invariant normal}"},
    "Defined term printed roman.", convention=6)

add(5, "Définition (16.1.2), ll. 2-3: 'le n-ème voisinage infinitésimal de Y pour le morphisme f'",
    "'voisinage infinitésimal de' roman (Y in the formula); 'pour le morphisme f' italic again",
    "italic (definition environment)", "convention",
    {"old": "-ème voisinage\ninfinitésimal de", "new": "-ème \\textup{voisinage\ninfinitésimal de}"},
    "Defined term printed roman, including 'de'.", convention=6)

add(5, "Définition (16.1.2), after (16.1.2.1): 'le faisceau d'anneaux gradués associé à f'",
    "'associé à' roman; 'est appelé le faisceau d'anneaux gradués' and 'f' italic (enlarged crop)",
    "italic", "convention",
    {"old": "gradués associé à $f$", "new": "gradués \\textup{associé à} $f$"}, convention=6)

add(5, "Définition (16.1.2), last sentence: 'est appelé le faisceau conormal de f'",
    "'faisceau conormal' roman; 'le' and 'de f' italic", "italic", "convention",
    {"old": "faisceau conormal", "new": "\\textup{faisceau conormal}"}, convention=6)

add(5, "Définition (16.1.2), last sentence: '(que l'on note aussi N_{Y/X} s'il n'en résulte pas de confusion)'",
    "the whole parenthesis roman", "italic", "convention",
    {"old": "(que l'on note aussi $\\mathscr{N}_{Y/X}$ s'il n'en résulte pas de confusion)",
     "new": "\\textup{(que l'on note aussi $\\mathscr{N}_{Y/X}$ s'il n'en résulte pas de confusion)}"},
    convention=6)

# ---------------------------------------------------------------- page 6
add(6, "first lines: 'par la puissance (J_f/J_f^{n+1})^m de l'Idéal d'augmentation de O_{Y(n)}, noyau de φ_{0n} : O_{Y(n)} → O_Y'",
    "(𝒥_f/𝒥_f^{n+1})^m ... de 𝒪_{Y(n)}, noyau de φ_{0n} : 𝒪_{Y(n)} → 𝒪_Y (enlarged crop)",
    "the same: the TeX keeps the printed reading", "misprint_in_print", None,
    "Mathematical slip in the print (n and m interchanged): φ_{nm} : O_{Y(m)} = ψ*(O_X)/J^{m+1} → O_{Y(n)} = ψ*(O_X)/J^{n+1} has kernel J^{n+1}/J^{m+1} = (J/J^{m+1})^{n+1}, the (n+1)-th power of the augmentation Ideal of O_{Y(m)} (kernel of φ_{0m}); the printed (J/J^{n+1})^m is an ideal of O_{Y(n)}, not of O_{Y(m)}. The corrected edition (whose text is also the printed one) needs the correction or a mathematical note.",
    corrected="$(\\mathscr{I}_f/\\mathscr{I}_f^{m+1})^{n+1}$ de l'Idéal d'augmentation de $\\mathcal{O}_{Y^{(m)}}$, noyau de $\\varphi_{0m}:\\mathcal{O}_{Y^{(m)}}\\to\\mathcal{O}_Y$")

add(6, "l. 3: 'de l'Idéal d'augmentation de O_{Y(n)}'",
    "*Idéal d'augmentation* italic", "upright", "italics",
    {"old": "de l'Idéal d'augmentation de", "new": "de l'\\emph{Idéal d'augmentation} de"})

add(6, "l. 6: 'où θ_n♯ est le morphisme canonique'",
    "θ_n♯ (sharp sign)", "\\theta_n^\\#", "convention",
    {"old": "$\\theta_n^\\#$", "new": "$\\theta_n^\\sharp$"}, S9, convention=9)

add(6, "l. 8: 'et les Gr_k(f) des O_Y-Modules.'",
    "*Modules* italic (enlarged crop)", "upright", "italics",
    {"old": "$\\mathcal{O}_Y$-Modules.", "new": "$\\mathcal{O}_Y$-\\emph{Modules}."})

add(6, "paragraph before (16.1.2.2): 'on a un homomorphisme canonique surjectif de O_Y-Algèbres graduées'",
    "*homomorphisme canonique surjectif* italic", "upright", "italics",
    {"old": "on a un homomorphisme canonique\nsurjectif de", "new": "on a un \\emph{homomorphisme canonique\nsurjectif} de"})

add(6, "display (16.1.2.2): 'S•_{O_Y}(Gr_1(f)) → Gr_•(f)'",
    "bold upright S (symmetric algebra) with raised bullet and subscript O_Y (enlarged crop)",
    "\\mathscr{S} (script S)", "symbol",
    {"old": "\\mathscr{S}_{\\mathcal{O}_Y}^{\\bullet}", "new": "\\mathbf{S}_{\\mathcal{O}_Y}^{\\bullet}"},
    "Wrong letter. ega4-16-fr.tex writes the symmetric-algebra S as \\mathscr{S} 40 times (other IV-4 files: \\mathbf S); see the final message.")

add(6, "Exemples (16.1.3): the body",
    "heading 'Exemples (16.1.3). —' italic; the body, including the labels (i), (ii), roman",
    "the IV-4 examples environment is \\itshape for the whole body (EGA_IV4_FR.tex line 142); IV-1 and IV-2 use \\textit for the heading only",
    "italics",
    {"old": "\\noindent\\itshape Exemples (#1). ---\\ }{\\par}", "new": "\\noindent\\textit{Exemples (#1). ---}\\ }{\\par}"},
    "OUTSIDE the page: preamble EGA_IV4_FR.tex (unique there); covers both IV-4 examples environments ((16.1.3) and one in ega4-17). The \\emph fixes inside (16.1.3) below assume this roman body.",
    outside="EGA_IV4_FR.tex")

add(6, "Exemples (16.1.3) (i): 'θ♯ : O_x → O_y soit un homomorphisme surjectif'",
    "θ♯ (sharp sign)", "\\theta^\\#", "convention",
    {"old": "$\\theta^\\#:\\mathcal{O}_x", "new": "$\\theta^\\sharp:\\mathcal{O}_x"}, S9, convention=9)

add(6, "Exemples (16.1.3) (i): 'un homomorphisme surjectif d'anneaux'",
    "*surjectif* italic in the roman body", "upright word (italic only through the environment)", "italics",
    {"old": "surjectif d'anneaux", "new": "\\emph{surjectif} d'anneaux"},
    "Judged with the roman examples body (finding above).")

add(6, "Exemples (16.1.3) (ii), 2nd paragraph: 'l'homomorphisme tel que θ_0♯ soit'",
    "θ_0♯ (sharp sign)", "\\theta_0^\\#", "convention",
    {"old": "$\\theta_0^\\#$ soit", "new": "$\\theta_0^\\sharp$ soit"}, S9, convention=9)

add(6, "Exemples (16.1.3) (ii): 'l'homomorphisme tel que θ♯ = θ_0♯' (first sharp)",
    "θ♯ (sharp sign)", "\\theta^\\#", "convention",
    {"old": "$\\theta^\\#=\\theta_0", "new": "$\\theta^\\sharp=\\theta_0"}, S9 + " Order-independent of the next edit.", convention=9)

add(6, "Exemples (16.1.3) (ii): 'l'homomorphisme tel que θ♯ = θ_0♯' (second sharp)",
    "θ_0♯ (sharp sign)", "\\theta_0^\\#", "convention",
    {"old": "=\\theta_0^\\#$", "new": "=\\theta_0^\\sharp$"}, S9, convention=9)

add(6, "Exemples (16.1.3) (ii): 'Comme θ♯ est surjectif'",
    "θ♯ (sharp sign)", "\\theta^\\#", "convention",
    {"old": "Comme $\\theta^\\#$ est surjectif", "new": "Comme $\\theta^\\sharp$ est surjectif"}, S9, convention=9)

add(6, "(16.1.4), ll. 1-2: 'ne sont pas munis canoniquement d'une structure de O_Y-Module,'",
    "the whole phrase italic, through 'O_Y-Module'", "upright", "italics",
    {"old": "ne sont pas munis canoniquement d'une structure de\n$\\mathcal{O}_Y$-Module,",
     "new": "\\emph{ne sont pas munis canoniquement d'une structure de\n$\\mathcal{O}_Y$-Module},"})

add(6, "(16.1.4), l. 2: 'ni a fortiori d'une structure'",
    "*a fortiori* italic", "upright", "italics",
    {"old": "ni a fortiori", "new": "ni \\emph{a fortiori}"})

add(6, "Proposition (16.1.5), label (i)",
    "label (i) upright", "\\item[(i)] comes out italic in the italic proposition", "convention",
    {"old": "\\item[(i)] $\\mathscr{G}r_\\bullet(f)$", "new": "\\item[\\textup{(i)}] $\\mathscr{G}r_\\bullet(f)$"},
    "Roman-numeral labels in italic statements are upright (GLOBAL_ISSUES 16).", convention=6)

# ---------------------------------------------------------------- page 7
add(7, "Proposition (16.1.5), label (ii)",
    "label (ii) upright", "\\item[(ii)] italic", "convention",
    {"old": "\\item[(ii)]", "new": "\\item[\\textup{(ii)}]"}, "GLOBAL_ISSUES 16.", convention=6)

add(7, "Proposition (16.1.5) (ii), 2nd line: 'de X.'",
    "'de' set in bold italic and 'X.' in bold upright (wrong fount; enlarged crops, compared with 'sur X et sur Y' on the same page)",
    "de $X$. (ordinary weight): silent correction", "misprint_in_print",
    {"old": "sous-préschémas de $X$.", "new": "sous-préschémas \\textbf{de} $\\mathbf{X}$."},
    "Wrong-fount line in the print (GLOBAL_ISSUES 29: wrong-font letters are reproduced in the diplomatic text). Separate from the (ii) label edit.",
    corrected="sous-préschémas de $X$.")

add(7, "Proposition (16.1.5), label (iii)",
    "label (iii) upright", "\\item[(iii)] italic", "convention",
    {"old": "\\item[(iii)]", "new": "\\item[\\textup{(iii)}]"}, "GLOBAL_ISSUES 16.", convention=6)

add(7, "Proposition (16.1.5) (iii), end: 'coïncident avec celles définies dans (16.1.2).'",
    "(16.1.2) upright", "(16.1.2) italic inside the proposition", "convention",
    {"old": "dans\n(16.1.2).", "new": "dans\n\\textup{(16.1.2)}."}, C6REF, convention=6)

add(7, "proof of (16.1.5), end: 'par J^k/J^{k+1} (III, 1.4.17).'",
    "(𝐈𝐈𝐈, 1.4.17): bold III", "(III, 1.4.17), plain", "convention",
    {"old": "$\\mathscr{I}^k/\\mathscr{I}^{k+1}$ (III, 1.4.17)",
     "new": "$\\mathscr{I}^k/\\mathscr{I}^{k+1}$ (\\textbf{III}, 1.4.17)"}, C2, convention=2)

add(7, "Corollaire (16.1.6), l. 1: 'Sous les hypothèses générales de (16.1.5), si l'immersion'",
    "(16.1.5) upright", "italic inside the corollary", "convention",
    {"old": "(16.1.5), si l'immersion", "new": "\\textup{(16.1.5)}, si l'immersion"}, C6REF, convention=6)

add(7, "proof of (16.1.6): 'donc les J^n/J^{n+1} sont des O_Y-Modules de type fini'",
    "'-Modules' set in bold (wrong fount; enlarged crop, compared with '-Mo(dules)' two paragraphs above)",
    "$\\mathcal{O}_Y$-Modules (ordinary weight): silent correction", "misprint_in_print",
    {"old": "$\\mathcal{O}_Y$-Modules de type fini", "new": "$\\mathcal{O}_Y$\\textbf{-Modules} de type fini"},
    "Wrong-fount word (GLOBAL_ISSUES 29). The hyphen is bold too.",
    corrected="$\\mathcal{O}_Y$-Modules de type fini")

add(7, "Corollaire (16.1.7), l. 1: 'Sous les hypothèses générales de (16.1.5), soit g : X→Y'",
    "(16.1.5) upright", "italic inside the corollary", "convention",
    {"old": "(16.1.5), soit $g", "new": "\\textup{(16.1.5)}, soit $g"}, C6REF, convention=6)

add(7, "Corollaire (16.1.7): 'φ_{nm} : O_{Y(m)} → O_{Y(n)} (n≤m) sont des homomorphismes'",
    "parentheses of (n≤m) upright", "($n\\leq m$): italic parentheses inside the corollary", "convention",
    {"old": "($n\\leq m$) sont", "new": "\\textup{($n\\leq m$)} sont"},
    "Same treatment as the earlier page fixes of parenthesised formulas in italic statements.", convention=6)

add(7, "proof of (16.1.7), end: 'd'un nombre fini de Gr_k(f) (III, 1.4.17).'",
    "(𝐈𝐈𝐈, 1.4.17): bold III", "(III, 1.4.17), plain", "convention",
    {"old": "$\\mathscr{G}r_k(f)$ (III, 1.4.17)", "new": "$\\mathscr{G}r_k(f)$ (\\textbf{III}, 1.4.17)"}, C2, convention=2)

add(7, "proof of (16.1.8), end: 'et de (0_I, 5.3.7).'",
    "(𝟎_I, 5.3.7): bold 0", "(0\\textsubscript{I}, 5.3.7), plain 0", "convention",
    {"old": "(0\\textsubscript{I}, 5.3.7)", "new": "(\\textbf{0}\\textsubscript{I}, 5.3.7)"}, C2, convention=2)

add(7, "end of the p. 7 segment: opening of Proposition (16.1.9)",
    "printed p. 7 ends with the proof of (16.1.8) ('... et de (0_I, 5.3.7).'); 'Proposition (16.1.9). — Soient X un préschéma' is the first line of p. 8",
    "\\begin{proposition}[16.1.9] and \\label{IV.16.1.9} stand before \\oldpage[IV-4]{8}",
    "marker",
    {"old": "\\begin{proposition}[16.1.9]\n\\label{IV.16.1.9}\n", "new": ""},
    "Two-part move (the opening moves, not the marker, so each edit stays in its own page segment): this edit deletes the opening here; the p. 8 marker finding re-inserts it after \\oldpage[IV-4]{8}. Apply both or neither.")

# ---------------------------------------------------------------- page 8
add(8, "top of p. 8: Proposition (16.1.9)",
    "p. 8 begins with 'Proposition (16.1.9). — Soient X un préschéma'",
    "page_008.tex begins after \\begin{proposition}[16.1.9]\\label (those lines are in p. 7's segment)",
    "marker",
    {"old": "\\oldpage[IV-4]{8}\nSoient", "new": "\\oldpage[IV-4]{8}\n\\begin{proposition}[16.1.9]\n\\label{IV.16.1.9}\nSoient"},
    "Second half of the move begun by the p. 7 marker finding. Apply both or neither.")

for lab in ("a", "b", "c"):
    add(8, f"Proposition (16.1.9), label {lab})",
        f"'{lab})' upright, without an opening parenthesis",
        f"\\item[({lab})]: italic '({lab})'", "punctuation",
        {"old": f"\\item[({lab})]", "new": f"\\item[\\textup{{{lab})}}]"},
        "Same form as the earlier page fixes of lettered labels in italic statements.")

add(8, "Proposition (16.1.9): 'De plus, si l'entier n vérifie ...'",
    "'De plus' opens a new indented paragraph of the statement", "text follows \\end{enumerate} directly, so it is set without an indent",
    "other",
    {"old": "\\end{enumerate}\nDe plus,", "new": "\\end{enumerate}\n\nDe plus,"},
    "Paragraph break (GLOBAL_ISSUES 80 pattern).")

add(8, "Proposition (16.1.9): 'si l'entier n vérifie b) ou c)' (label b)",
    "b) upright inside the italic statement", "italic b)", "convention",
    {"old": "vérifie b) ou", "new": "vérifie \\textup{b)} ou"},
    "Order-independent of the next edit.", convention=6)

add(8, "Proposition (16.1.9): 'si l'entier n vérifie b) ou c)' (label c)",
    "c) upright inside the italic statement", "italic c)", "convention",
    {"old": "ou c), il existe", "new": "ou \\textup{c)}, il existe"}, convention=6)

add(8, "proof of (16.1.9), l. 2: 'un Idéal quasi-cohérent de type fini J de O_X'",
    "*de type fini* italic", "upright", "italics",
    {"old": "quasi-cohérent de type fini\n$\\mathscr{I}$", "new": "quasi-cohérent \\emph{de type fini}\n$\\mathscr{I}$"})

add(8, "proof of (16.1.9): 'L'équivalence de b) et c)'",
    "*b)* and *c)* italic (letter and parenthesis)", "upright", "italics",
    {"old": "L'équivalence de b) et c),", "new": "L'équivalence de \\emph{b)} et \\emph{c)},"})

add(8, "proof of (16.1.9): 'J^n|U = J^{n+1}|U (0_I, 5.2.2)'",
    "(𝟎_I, 5.2.2): bold 0", "plain 0", "convention",
    {"old": "|U$ (0\\textsubscript{I}, 5.2.2)", "new": "|U$ (\\textbf{0}\\textsubscript{I}, 5.2.2)"}, C2, convention=2)

add(8, "proof of (16.1.9): 'Pour prouver que a) entraîne b)'",
    "*a)* and *b)* italic", "upright", "italics",
    {"old": "Pour prouver que a) entraîne b),", "new": "Pour prouver que \\emph{a)} entraîne \\emph{b)},"})

add(8, "proof of (16.1.9): 'le Nilradical N de O_X (I, 5.1.2)'",
    "(𝐈, 5.1.2): bold I", "plain I", "convention",
    {"old": "(I, 5.1.2)", "new": "(\\textbf{I}, 5.1.2)"}, C2, convention=2)

add(8, "proof of (16.1.9): 'il est nilpotent, ce qui prouve b).'",
    "*b)* italic", "upright", "italics",
    {"old": "ce qui prouve b).", "new": "ce qui prouve \\emph{b)}."})

add(8, "proof of (16.1.9): 'pour prouver que b) entraîne a)'",
    "*b)* and *a)* italic", "upright", "italics",
    {"old": "prouver que b) entraîne a),", "new": "prouver que \\emph{b)} entraîne \\emph{a)},"})

add(8, "proof of (16.1.9), end: 'un ouvert U de X contenant Y (0_I, 5.2.2)'",
    "(𝟎_I, 5.2.2): bold 0", "plain 0", "convention",
    {"old": "$Y$ (0\\textsubscript{I}, 5.2.2)", "new": "$Y$ (\\textbf{0}\\textsubscript{I}, 5.2.2)"}, C2, convention=2)

add(8, "Corollaire (16.1.10): '(autrement dit pour que j soit un isomorphisme local au point y)'",
    "the parenthesis roman, with *isomorphisme local* italic inside it (enlarged crop)",
    "all italic (corollary environment)", "convention",
    {"old": "(autrement dit pour que $j$ soit un isomorphisme local au\npoint $y$)",
     "new": "\\textup{(autrement dit pour que $j$ soit un \\emph{isomorphisme local} au\npoint $y$)}"},
    "Roman clause inside the italic statement; the \\emph inside \\textup gives the printed italic of 'isomorphisme local'.", convention=6)

add(8, "Remarques (16.1.11) (i): 'la limite projective du système projectif (O_{Y(n)}, φ_nm) de faisceaux d'anneaux sur Y est appelé l'invariant normal'",
    "'est appelé' (masculine participle; the subject is 'la limite projective')",
    "est\\nappelé: the TeX keeps the printed reading", "misprint_in_print", None,
    "Agreement slip in the print; the TeX keeps it (fix null). The corrected edition may give 'appelée'.",
    confidence="medium", corrected="appelée")

add(8, "Remarques (16.1.11) (i): 'appelé l'invariant normal d'ordre infini de f'",
    "*invariant normal d'ordre infini* italic in the roman remark", "no emphasis", "italics",
    {"old": "l'invariant normal d'ordre infini de", "new": "l'\\emph{invariant normal d'ordre infini} de"},
    "Remark body judged as roman (document-wide remark item).")

add(8, "Remarques (16.1.11) (i): 'n'est autre que le complété formel de O_X'",
    "*complété formel* italic", "no emphasis", "italics",
    {"old": "le complété formel de", "new": "le \\emph{complété formel} de"})

add(8, "Remarques (16.1.11) (i): 'le long de Y (I, 10.8.4)'",
    "(𝐈, 10.8.4): bold I", "plain I", "convention",
    {"old": "(I, 10.8.4)", "new": "(\\textbf{I}, 10.8.4)"}, C2, convention=2)

add(8, "Remarques (16.1.11) (i): 'le préschéma formel complété de X'",
    "*complété* italic ('le préschéma formel' roman)", "no emphasis", "italics",
    {"old": "formel complété de", "new": "formel \\emph{complété} de"})

add(8, "Remarques (16.1.11) (i): 'le long de Y (I, 10.8.5)'",
    "(𝐈, 10.8.5): bold I", "plain I", "convention",
    {"old": "(I, 10.8.5)", "new": "(\\textbf{I}, 10.8.5)"}, C2, convention=2)

add(8, "Remarques (16.1.11) (i): 'Y^(∞) est le voisinage formel de Y dans X'",
    "*voisinage formel* italic", "no emphasis", "italics",
    {"old": "le voisinage formel de", "new": "le \\emph{voisinage formel} de"})

add(8, "Remarques (16.1.11) (ii): 'l'homomorphisme θ♯ : ψ*(O_X) → O_Y soit surjectif'",
    "θ♯ (sharp sign)", "\\theta^\\#", "convention",
    {"old": "$\\theta^\\#:\\psi^*(\\mathcal{O}_X)\\to\\mathcal{O}_Y$", "new": "$\\theta^\\sharp:\\psi^*(\\mathcal{O}_X)\\to\\mathcal{O}_Y$"},
    S9, convention=9)

# ---------------------------------------------------------------- page 9
add(9, "subsection heading 16.2",
    "'16.2. Propriétés fonctorielles des invariants normaux d'une immersion.' (final full stop)",
    "no full stop", "punctuation",
    {"old": "\\subsection{Propriétés fonctorielles des invariants normaux d'une immersion}",
     "new": "\\subsection{Propriétés fonctorielles des invariants normaux d'une immersion.}"},
    "GLOBAL_ISSUES 43/58.")

add(9, "(16.2.1), l. 2: 'les homomorphismes θ♯ et θ'♯ soient surjectifs' (θ♯)",
    "θ♯ (sharp sign)", "\\theta^\\#", "convention",
    {"old": "homomorphismes $\\theta^\\#$ et", "new": "homomorphismes $\\theta^\\sharp$ et"}, S9, convention=9)

add(9, "(16.2.1), l. 2: 'les homomorphismes θ♯ et θ'♯ soient surjectifs' (θ'♯)",
    "θ'♯ (sharp sign)", "\\theta'^\\#", "convention",
    {"old": "$\\theta'^\\#$ soient", "new": "$\\theta'^\\sharp$ soient"}, S9 + " Order-independent of the next edit.", convention=9)

add(9, "(16.2.1), l. 2: 'soient surjectifs ;'",
    "*surjectifs* italic", "upright", "italics",
    {"old": "soient surjectifs;", "new": "soient \\emph{surjectifs};"})

add(9, "after diagram (16.2.1.1): 'Posons u=(ρ, λ), v=(σ, μ).'",
    "'Posons' opens a new indented paragraph", "'Posons' follows \\] directly: no paragraph break", "other",
    {"old": "\\]\nPosons", "new": "\\]\n\nPosons"},
    "Paragraph break after a display (GLOBAL_ISSUES 47 pattern).")

for old, new, lab in (
        ("\\ar[r]^-{\\psi'^*(\\mu^\\#)}", "\\ar[r]^-{\\psi'^*(\\mu^\\sharp)}", "top arrow label ψ'*(μ♯)"),
        ("\\ar[d]_{\\rho^*(\\theta^\\#)}", "\\ar[d]_{\\rho^*(\\theta^\\sharp)}", "left arrow label ρ*(θ♯)"),
        ("\\ar[d]^{\\theta'^\\#}", "\\ar[d]^{\\theta'^\\sharp}", "right arrow label θ'♯"),
        ("\\ar[r]_-{\\lambda^\\#}", "\\ar[r]_-{\\lambda^\\sharp}", "bottom arrow label λ♯")):
    add(9, f"square diagram after 'Posons': {lab}", "sharp sign (enlarged crop)", "^\\#", "convention",
        {"old": old, "new": new}, S9, convention=9)

add(9, "after the square diagram: 'si J et J' sont les noyaux de θ♯ et θ'♯' (θ♯)",
    "θ♯ (sharp sign)", "\\theta^\\#", "convention",
    {"old": "noyaux de\n$\\theta^\\#$", "new": "noyaux de\n$\\theta^\\sharp$"}, S9, convention=9)

add(9, "after the square diagram: 'si J et J' sont les noyaux de θ♯ et θ'♯' (θ'♯)",
    "θ'♯ (sharp sign)", "\\theta'^\\#", "convention",
    {"old": "$\\theta'^\\#$, que", "new": "$\\theta'^\\sharp$, que"}, S9, convention=9)

add(9, "'que l'on a ψ'*(μ♯)(ρ*(J)) ⊂ J''",
    "μ♯ (sharp sign)", "\\mu^\\#", "convention",
    {"old": "(\\mu^\\#)(\\rho^*(\\mathscr{I}))", "new": "(\\mu^\\sharp)(\\rho^*(\\mathscr{I}))"}, S9, convention=9)

add(9, "'pour tout entier n, ψ'*(μ♯)(ρ*(J^n)) ⊂ J'^n'",
    "μ♯ (sharp sign)", "\\mu^\\#", "convention",
    {"old": "(\\mu^\\#)(\\rho^*(\\mathscr{I}^n))", "new": "(\\mu^\\sharp)(\\rho^*(\\mathscr{I}^n))"}, S9, convention=9)

add(9, "'ce qui montre que ψ'*(μ♯) définit, par passage aux quotients'",
    "μ♯ (sharp sign)", "\\mu^\\#", "convention",
    {"old": "que $\\psi'^*(\\mu^\\#)$ définit", "new": "que $\\psi'^*(\\mu^\\sharp)$ définit"}, S9, convention=9)


# ---------------------------------------------------------------- checks
def load(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


bad = 0
for d in F:
    fix = d["fix"]
    if fix is None:
        continue
    if d["_outside"]:
        text = load(os.path.join(SRC, d["_outside"]))
        where = d["_outside"]
    else:
        text = load(os.path.join(RUN, "page_%03d.tex" % d["page"]))
        where = "page_%03d.tex" % d["page"]
    n = text.count(fix["old"])
    if n != 1:
        bad += 1
        print("COUNT", n, where, repr(fix["old"]))
print("findings", len(F), "bad", bad)

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in (5, 6, 7, 8, 9):
    print(p, {k: cnt[(p, k)] for k in ("normal", "convention", "misprint")})
conv = Counter(d["convention"] for d in F if d["convention"])
print("by convention", dict(conv))

for d in F:
    d.pop("_outside")
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")
print("wrote", OUT)
