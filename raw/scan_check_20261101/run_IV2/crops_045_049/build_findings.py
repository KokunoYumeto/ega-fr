"""Build findings_045_049.json for EGA IV-2 pp. 45-49 and verify every fix.

Checks: each "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF); applying the page's
fixes in listed order and in reverse order succeeds (each old still occurs exactly once when applied),
so the edits do not depend on each other's order."""
import json
import pathlib

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_045_049.json"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


B1 = "bold italic k"
BSUB = "bold upright k in the subscript (enlarged crop)"
G48 = "Bold upright in subscripts, bold italic on the line (GLOBAL_ISSUES 48)."
STMT = "The statement continues after its numbered display; the TeX closes the environment before the display, so the text is upright."

f = []

# ---------------- page 45 ----------------
f += [
    F(45, "Proposition (3.3.6), first line: 'Spec(k(x)⊗_{k(s)}k(y))', first k(x)", B1, "plain k", "convention", 1, "high",
      "\\operatorname{Spec}(k(x)", "\\operatorname{Spec}(\\boldsymbol{k}(x)"),
    F(45, "same formula: subscript k(s) of ⊗", BSUB, "plain k", "convention", 1, "high",
      "(x)\\otimes_{k(s)}", "(x)\\otimes_{\\mathbf{k}(s)}", G48),
    F(45, "same formula: k(y)", B1, "plain k", "convention", 1, "high",
      "k(y))$, et soit", "\\boldsymbol{k}(y))$, et soit"),
    F(45, "Proposition (3.3.6), line 2: '(I, 3.4.9)'", "bold I; the reference is upright inside the italic statement",
      "(I, 3.4.9): plain I, italic inside the proposition", "convention", 2, "high",
      "(I, 3.4.9)", "\\textup{(\\textbf{I}, 3.4.9)}", "The edit also sets the reference upright (next entry)."),
    F(45, "Proposition (3.3.6), line 2: '(I, 3.4.9)'", "parentheses and figures upright inside the italic statement",
      "italic (proposition environment)", "convention", 6, "high", None, None,
      "Included in the convention-2 edit of the previous entry."),
    F(45, "display (3.3.6.1)", "no punctuation after the display (enlarged crop; the dot far right is a speck above the baseline)",
      "display ends with a comma", "punctuation", None, "high",
      "I_{x,y}\\right),\n\\]", "I_{x,y}\\right)\n\\]", "Extra comma after the display."),
    F(45, "after (3.3.6.1): 'où pour tout s∈S, G_s = G⊗_{O_S} k(s).'", "'où pour tout' italic: end of the statement of (3.3.6) (enlarged crop)",
      "upright (outside the proposition environment)", "convention", 6, "high",
      "où pour tout $s\\in S$", "\\textit{où pour tout} $s\\in S$", STMT),
    F(45, "same line: 'G⊗_{O_S} k(s)'", B1, "plain k", "convention", 1, "high",
      "\\otimes_{\\mathcal O_S}k(s)", "\\otimes_{\\mathcal O_S}\\boldsymbol{k}(s)"),
    F(45, "commutative diagram, bottom arrow S ← Y", "label g BELOW the arrow (enlarged crop); p above the top arrow",
      "Y \\ar[l]_g: for a leftward arrow '_' puts the label above", "formula", None, "high",
      "Y \\ar[l]_g", "Y \\ar[l]^g", "GLOBAL_ISSUES 30 (labels of leftward arrows). The top arrow Z \\ar[l]_p (p above) is right."),
    F(45, "after the diagram: 'Posons G' = q^*(G)'", "new indented paragraph",
      "no blank line after \\]: the paragraph continues", "other", None, "high",
      "\\]\nPosons", "\\]\n\nPosons", "Paragraph break the print has and the TeX lacks (GLOBAL_ISSUES 47 pattern)."),
    F(45, "'avec G'_x = G'⊗_{O_X} k(x)'", B1, "plain k", "convention", 1, "high",
      "\\otimes_{\\mathcal O_X}k(x)", "\\otimes_{\\mathcal O_X}\\boldsymbol{k}(x)"),
    F(45, "'G'_x = G_s⊗_{k(s)} k(x)': subscript k(s)", BSUB, "plain k", "convention", 1, "high",
      "\\mathcal G_s\\otimes_{k(s)}", "\\mathcal G_s\\otimes_{\\mathbf{k}(s)}", G48),
    F(45, "'G'_x = G_s⊗_{k(s)} k(x), et p^{-1}(x) = ...'", "comma after k(x) before 'et' (enlarged crop)",
      "no comma: '$ et'", "punctuation", None, "high",
      "}k(x)$ et", "}\\boldsymbol{k}(x)$, et",
      "One edit also carries the convention-1 bold k of this k(x) (next entry)."),
    F(45, "'G_s⊗_{k(s)} k(x)': k(x)", B1, "plain k", "convention", 1, "high", None, None,
      "Included in the punctuation edit of the previous entry."),
    F(45, "'p^{-1}(x) = g^{-1}(s)⊗_{k(s)} k(x)': subscript k(s)", BSUB, "plain k", "convention", 1, "high",
      "g^{-1}(s)\\otimes_{k(s)}", "g^{-1}(s)\\otimes_{\\mathbf{k}(s)}", G48),
    F(45, "same formula: k(x)", B1, "plain k", "convention", 1, "high",
      "}k(x)$~; en outre", "}\\boldsymbol{k}(x)$~; en outre"),
    F(45, "'comme le corps k(x)'", B1, "plain k", "convention", 1, "high",
      "le corps $k(x)$", "le corps $\\boldsymbol{k}(x)$"),
    F(45, "'est un k(s)-module plat'", B1, "plain k", "convention", 1, "high",
      "un $k(s)$-module", "un $\\boldsymbol{k}(s)$-module"),
    F(45, "display (3.3.6.3)", "no punctuation after the display (enlarged crop)", "display ends with a comma",
      "punctuation", None, "high",
      "\\operatorname{Ass}(\\mathcal O_{T_{x,y}}),\n\\]", "\\operatorname{Ass}(\\mathcal O_{T_{x,y}})\n\\]",
      "Extra comma after the display."),
    F(45, "Corollaire (3.3.7), line 1: 'Sous les hypothèses de (3.3.6),'", "(3.3.6) upright inside the italic statement",
      "italic (corollary environment)", "convention", 6, "high",
      "hypothèses de (3.3.6), supposons", "hypothèses de \\textup{(3.3.6)}, supposons"),
    F(45, "display (3.3.7.1)", "no punctuation after the display (enlarged crop)", "display ends with a comma",
      "punctuation", None, "high",
      "\\bigcup_{(x,y)\\in C}I_{x,y},\n", "\\bigcup_{(x,y)\\in C}I_{x,y}\n", "Extra comma after the display."),
    F(45, "after (3.3.7.1): 'où C est l'ensemble des couples (x, y) tels que ... et f(x) = g(y).'",
      "italic: end of the statement of (3.3.7) (enlarged crop)", "upright (outside the corollary environment)",
      "convention", 6, "high",
      "où $C$ est l'ensemble des couples $(x,y)$ tels que\n$x\\in\\operatorname{Ass}(\\mathcal F)$, $y\\in\\operatorname{Ass}(\\mathcal G)$ et\n$f(x)=g(y)$.",
      "\\textit{où $C$ est l'ensemble des couples $(x,y)$ tels que\n$x\\in\\operatorname{Ass}(\\mathcal F)$, $y\\in\\operatorname{Ass}(\\mathcal G)$ et\n$f(x)=g(y)$.}",
      STMT),
    F(45, "proof of (3.3.7): 'équivaut à y∈Ass(G) : la conclusion résulte de (3.3.6.1).'", "colon (enlarged crop)",
      "semicolon '~;'", "punctuation", None, "high",
      "$y\\in\\operatorname{Ass}(\\mathcal G)$~; la conclusion", "$y\\in\\operatorname{Ass}(\\mathcal G)$~: la conclusion"),
    F(45, "heading of (3.3.8)", "'Remarques (3.3.8). —' (plural)", "\\begin{remark} prints 'Remarque'", "word", None, "high",
      "\\begin{remark}[3.3.8]", "\\begin{remarks}[3.3.8]",
      "Apply together with the next entry (\\end{remark}); the remarks environment exists in EGA_IV2_FR.tex (GLOBAL_ISSUES 28)."),
    F(45, "end of (3.3.8)", "see previous entry", "\\end{remark}", "word", None, "high",
      "\\end{remark}", "\\end{remarks}", "Apply together with the previous entry."),
    F(45, "Corollaire (3.3.9): 'Sous les conditions de (3.3.7), on a'", "(3.3.7) upright inside the italic statement",
      "italic (corollary environment)", "convention", 6, "high",
      "conditions de (3.3.7), on a", "conditions de \\textup{(3.3.7)}, on a"),
    F(45, "after (3.3.9.1): '(où q : X×_S Y→Y est la projection canonique).'",
      "italic, parentheses included: end of the statement of (3.3.9) (enlarged crop)", "upright (outside the corollary environment)",
      "convention", 6, "high",
      "(où $q:X\\times_S Y\\to Y$ est la projection canonique).",
      "\\textit{(où $q:X\\times_S Y\\to Y$ est la projection canonique).}", STMT),
]

# ---------------- page 46 ----------------
f += [
    F(46, "heading 3.4", "'3.4. Propriétés des faisceaux F/tF.' (final full stop)", "no full stop", "punctuation", None, "high",
      "faisceaux $\\mathcal F/t\\mathcal F$}{", "faisceaux $\\mathcal F/t\\mathcal F$.}{",
      "Subsection titles lack the printed full stop (GLOBAL_ISSUES 43)."),
    F(46, "Proposition (3.4.1), label (i)", "label upright", "\\item[(i)] comes out italic inside the italic proposition",
      "convention", 6, "high", "\\item[(i)] Pour tout", "\\item[\\textup{(i)}] Pour tout", "GLOBAL_ISSUES 16."),
    F(46, "Proposition (3.4.1), label (ii)", "label upright", "\\item[(ii)] comes out italic inside the italic proposition",
      "convention", 6, "high", "\\item[(ii)] Si $Z$", "\\item[\\textup{(ii)}] Si $Z$", "GLOBAL_ISSUES 16."),
    F(46, "after (3.4.1.1): 'où la somme du second membre est étendue à tous les i tels que Z⊂S_i.'",
      "italic: part of (3.4.1) (ii)", "upright (outside the proposition environment)", "convention", 6, "high",
      "où la somme du second membre est étendue à tous les $i$ tels que\n$Z\\subset S_i$.",
      "\\textit{où la somme du second membre est étendue à tous les $i$ tels que\n$Z\\subset S_i$.}", STMT),
    F(46, "(3.4.1) (iii): 'Supposons que Z ne soit égal à aucun des S_i. Pour que ... satisfaites :'",
      "italic statement text; the label (iii) and the reference (3.4.1.1) upright",
      "upright (the (iii) list stands outside the proposition environment)", "convention", 6, "high",
      "Supposons que $Z$ ne soit égal à aucun des $S_i$. Pour que les\ndeux membres de (3.4.1.1) soient égaux, il faut et il suffit que les deux\nconditions suivantes soient satisfaites~:",
      "\\textit{Supposons que $Z$ ne soit égal à aucun des $S_i$. Pour que les\ndeux membres de} (3.4.1.1) \\textit{soient égaux, il faut et il suffit que les deux\nconditions suivantes soient satisfaites~:}",
      STMT + " Labels and reference stay upright, as printed."),
    F(46, "(3.4.1) (iii) α): 't_z est F_z-régulier'", "italic", "upright (outside the proposition environment)",
      "convention", 6, "high",
      "$t_z$ est $\\mathcal F_z$-régulier", "\\textit{$t_z$ est $\\mathcal F_z$-régulier}", STMT),
    F(46, "(3.4.1) (iii) α): '(0, 15.1.4)'", "bold 0", "$(0,15.1.4)$", "convention", 2, "high",
      "$(0,15.1.4)$", "$(\\mathbf{0},15.1.4)$"),
    F(46, "(3.4.1) (iii) β): 'Pour tout i tel que Z⊂S_i, l'image canonique du germe t_z dans O_{S_i,z} engendre l'idéal maximal de cet anneau'",
      "italic; the following parenthesis '(ce qui entraîne ... de cet anneau).' roman with two italic phrases",
      "upright (outside the proposition environment)", "convention", 6, "high",
      "Pour tout $i$ tel que $Z\\subset S_i$, l'image canonique du\ngerme $t_z$ dans $\\mathcal O_{S_i,z}$ engendre l'idéal maximal de cet anneau",
      "\\textit{Pour tout $i$ tel que $Z\\subset S_i$, l'image canonique du\ngerme $t_z$ dans $\\mathcal O_{S_i,z}$ engendre l'idéal maximal de cet anneau}",
      STMT),
    F(46, "(3.4.1) (iii) β), parenthesis: 'est un anneau de valuation discrète'", "'anneau de valuation discrète' italic",
      "upright", "italics", None, "high",
      "est un anneau de valuation discrète\net l'image", "est un \\emph{anneau de valuation discrète}\net l'image"),
    F(46, "(3.4.1) (iii) β), parenthesis: 'une uniformisante de cet anneau'", "'uniformisante' italic", "upright",
      "italics", None, "high",
      "une uniformisante de cet anneau)", "une \\emph{uniformisante} de cet anneau)"),
    F(46, "proof of (3.4.1) (i): 'on a F/tF = F⊗_{O_X}O_Y = j^*(F), donc'", "formula in the running text",
      "displayed (\\[...\\]) with a comma inside", "formula", None, "high",
      "on a\n\\[\n\\mathcal F/t\\mathcal F\n=\\mathcal F\\otimes_{\\mathcal O_X}\\mathcal O_Y\n=j^*(\\mathcal F),\n\\]\ndonc\n",
      "on a\n$\\mathcal F/t\\mathcal F=\\mathcal F\\otimes_{\\mathcal O_X}\\mathcal O_Y=j^*(\\mathcal F)$, donc\n",
      "Display where the print has an inline formula (GLOBAL_ISSUES 21)."),
    F(46, "proof of (3.4.1) (i): 'Supp(F/tF) = j^{-1}(S) = S∩Y (I, 9.1.13), d'où l'assertion.'",
      "formula and reference in the running text", "displayed, with \\quad\\text{(I, 9.1.13),}", "formula", None, "high",
      "\\[\n\\operatorname{Supp}(\\mathcal F/t\\mathcal F)\n=j^{-1}(S)=S\\cap Y\n\\quad\\text{(I, 9.1.13),}\n\\]\nd'où l'assertion.",
      "$\\operatorname{Supp}(\\mathcal F/t\\mathcal F)=j^{-1}(S)=S\\cap Y$ (\\textbf{I}, 9.1.13), d'où l'assertion.",
      "The edit also carries the bold I of the reference (next entry)."),
    F(46, "proof of (3.4.1) (i): '(I, 9.1.13)'", "bold I", "plain I", "convention", 2, "high", None, None,
      "Included in the display-to-inline edit of the previous entry."),
    F(46, "proof of (3.4.1): '(0_I, 1.7.4)'", "bold 0", "$(0_{\\mathrm I},1.7.4)$", "convention", 2, "high",
      "$(0_{\\mathrm I},1.7.4)$", "$(\\mathbf{0}_{\\mathrm I},1.7.4)$"),
    F(46, "proof of (3.4.1): 'M étant un A-module fidèle'", "'fidèle' italic", "upright", "italics", None, "high",
      "$A$-module fidèle", "$A$-module \\emph{fidèle}"),
    F(46, "proof of (3.4.1): '(autrement dit est un anneau local artinien)'", "'artinien' italic", "upright",
      "italics", None, "high", "anneau local artinien)", "anneau local \\emph{artinien})"),
    F(46, "after (3.4.1.3): 'en outre, pour que les deux membres de (3.4.1.3) soient égaux, ... satisfaites :'",
      "italic: part of Lemme (3.4.1.2); the reference (3.4.1.3) upright", "upright (outside the lemma environment)",
      "convention", 6, "high",
      "en outre, pour que les deux membres de (3.4.1.3) soient égaux, il faut et il\nsuffit que les conditions suivantes soient satisfaites~:",
      "\\textit{en outre, pour que les deux membres de} (3.4.1.3) \\textit{soient égaux, il faut et il\nsuffit que les conditions suivantes soient satisfaites~:}",
      STMT + " The statement goes on to α), β) on p. 47."),
]

# ---------------- page 47 ----------------
f += [
    F(47, "Lemme (3.4.1.2) α): 't est M-régulier ;'", "italic (enlarged crop)", "upright (outside the lemma environment)",
      "convention", 6, "high", "$t$ est $M$-régulier~;", "\\textit{$t$ est $M$-régulier~;}", STMT),
    F(47, "Lemme (3.4.1.2) β): 'pour tout i tel que M_{p_i} ≠ 0, l'image de t dans A/p_i engendre l'idéal maximal de cet anneau'",
      "italic; the following '(ce qui entraîne que A/p_i est un' roman", "upright (outside the lemma environment)",
      "convention", 6, "high",
      "pour tout $i$ tel que $M_{\\mathfrak p_i}\\neq0$, l'image de $t$\ndans $A/\\mathfrak p_i$ engendre l'idéal maximal de cet anneau",
      "\\textit{pour tout $i$ tel que $M_{\\mathfrak p_i}\\neq0$, l'image de $t$\ndans $A/\\mathfrak p_i$ engendre l'idéal maximal de cet anneau}",
      STMT),
    F(47, "Lemme (3.4.1.2) β), parenthesis: 'est un anneau de valuation discrète).'", "'anneau de valuation discrète' italic",
      "upright", "italics", None, "high",
      "est un anneau de valuation discrète).", "est un \\emph{anneau de valuation discrète})."),
    F(47, "proof of (3.4.1.2), line 2: '(0, 16.3.4)'", "bold 0", "$(0,16.3.4)$", "convention", 2, "high",
      "$(0,16.3.4)$", "$(\\mathbf{0},16.3.4)$"),
    F(47, "proof of (3.4.1.2): 't est P-régulier, car'", "'régulier' italic (enlarged crop)", "upright", "italics", None, "high",
      "$t$ est $P$-régulier", "$t$ est $P$-\\emph{régulier}"),
    F(47, "proof of (3.4.1.2): 'supposer déjà que t est M-régulier.'", "'régulier' italic (enlarged crop; the M-régulier two lines above is roman)",
      "upright", "italics", None, "high",
      "déjà que $t$ est $M$-régulier", "déjà que $t$ est $M$-\\emph{régulier}"),
    F(47, "proof of (3.4.1.2): 'on a donc nécessairement Ass(M) ⊂ ∪_i{p_i}.'", "formula in the running text (flush left, not centred)",
      "displayed (\\[...\\])", "formula", None, "high",
      "nécessairement\n\\[\n\\operatorname{Ass}(M)\\subset\\bigcup_i\\{\\mathfrak p_i\\}.\n\\]",
      "nécessairement\n$\\operatorname{Ass}(M)\\subset\\bigcup_i\\{\\mathfrak p_i\\}$.",
      "Display where the print has an inline formula (GLOBAL_ISSUES 21)."),
    F(47, "proof of (3.4.1.2): 'le A-module M est fidèle'", "'fidèle' italic (enlarged crop)", "upright", "italics", None, "high",
      "$M$ est fidèle", "$M$ est \\emph{fidèle}"),
    F(47, "same line: 'fidèle : cela entraîne'", "colon (enlarged crop)", "semicolon '~;'", "punctuation", None, "high",
      "~; cela entraîne", "~: cela entraîne"),
    F(47, "proof of (3.4.1.2): 'et par suite Ass(M) = ∪_i{p_i}.'", "formula in the running text, end of the line",
      "displayed (\\[...\\])", "formula", None, "high",
      "et par suite\n\\[\n\\operatorname{Ass}(M)=\\bigcup_i\\{\\mathfrak p_i\\}.\n\\]",
      "et par suite\n$\\operatorname{Ass}(M)=\\bigcup_i\\{\\mathfrak p_i\\}$.",
      "Display where the print has an inline formula (GLOBAL_ISSUES 21)."),
]

# ---------------- page 48 ----------------
f += [
    F(48, "page break 47/48: 'Supposons d'abord n = 1; il n'y a alors qu'un seul idéal premier minimal p de A,'",
      "this sentence opening is the last line of printed p. 47; p. 48 begins 'et dire que M_p est de longueur 1'",
      "\\oldpage[IV-2]{48} stands before 'Supposons d'abord'", "marker", None, "high",
      "\\oldpage[IV-2]{48}\n\nSupposons d'abord $n=1$~; il n'y a alors qu'un seul idéal premier minimal\n$\\mathfrak p$ de $A$, et dire que",
      "Supposons d'abord $n=1$~; il n'y a alors qu'un seul idéal premier minimal\n$\\mathfrak p$ de $A$,\n\\oldpage[IV-2]{48}\net dire que",
      "Moves the marker; the moved words match the print of p. 47. The blank line before 'Supposons' (end of the p. 47 segment) stays: new paragraph, as printed."),
    F(48, "'M est nécessairement monogène'", "'monogène' italic (enlarged crop)", "upright", "italics", None, "high",
      "nécessairement monogène", "nécessairement \\emph{monogène}"),
    F(48, "'t est M'-régulier et M''-régulier': first 'régulier'", "italic (enlarged crop)", "upright", "italics", None, "high",
      "$M'$-régulier et", "$M'$-\\emph{régulier} et"),
    F(48, "same line: second 'régulier'", "italic (enlarged crop)", "upright", "italics", None, "high",
      "$M''$-régulier. Cette", "$M''$-\\emph{régulier}. Cette"),
    F(48, "'pour tout i, on a' (before the two long(...) equations)",
      "bold italic i: stem and dot much heavier than the light italic i of 'pour tout i, on a' on p. 47 (enlarged crops compared)",
      "plain $i$ (silently corrected)", "misprint_in_print", None, "high",
      "pour tout $i$, on a", "pour tout $\\boldsymbol{i}$, on a",
      "Wrong-font letter in the print, reproduced in the diplomatic text (as GLOBAL_ISSUES 29). Some subscript i's (p. 48 M''_{p_i}, M_{p_i} in the last lines; p. 49 'Les S_i') also look heavier, but too little to call at that size: not reported.",
      corrected="pour tout $i$, on a"),
    F(48, "first line of the two-line display 'long(M/tM) = long(M'/tM') + long(M''/tM'')'",
      "no punctuation at the end of the line (enlarged crop)", "line ends with a comma", "punctuation", None, "high",
      "\\operatorname{long}(M''/tM''),\\\\", "\\operatorname{long}(M''/tM'')\\\\", "Extra comma in the display."),
    F(48, "'En outre les deux membres ne peuvent être égaux'", "no comma after 'En outre' (enlarged crop)",
      "'En outre,'", "punctuation", None, "high",
      "En outre,\nles deux membres", "En outre\nles deux membres"),
]

# ---------------- page 49 ----------------
f += [
    F(49, "Corollaire (3.4.2), line 1: 'Sous les hypothèses générales de (3.4.1),'", "(3.4.1) upright inside the italic statement",
      "italic (corollary environment)", "convention", 6, "high",
      "générales de (3.4.1), supposons", "générales de \\textup{(3.4.1)}, supposons"),
    F(49, "Corollaire (3.4.2), line 3: 'en outre O_{S,z} est un anneau de valuation discrète'",
      "O_{S,z}: subscript S without index (enlarged crop)", "\\mathcal O_{S_i,z}", "formula", None, "high",
      "$\\mathcal O_{S_i,z}$ est un anneau", "$\\mathcal O_{S,z}$ est un anneau",
      "Not a misprint: S_i is the only component of S containing z (first assertion of the corollary), so near z the reduced S equals S_i and O_{S,z} = O_{S_i,z}. The TeX's S_i matches (3.4.1) (iii) β); the print has S."),
    F(49, "proof of (3.4.3): '(0, 16.4.6.3)'", "bold 0", "$(0,16.4.6.3)$", "convention", 2, "high",
      "$(0,16.4.6.3)$", "$(\\mathbf{0},16.4.6.3)$"),
    F(49, "proof of (3.4.4), first paragraph: 't_x est F_x-régulier (0, 15.2.4)'", "bold 0", "$(0,15.2.4)$", "convention", 2, "high",
      "régulier $(0,15.2.4)$", "régulier $(\\mathbf{0},15.2.4)$"),
    F(49, "proof of (3.4.4): 'A/tA et A_1/tA_1 sont des anneaux artiniens'", "'artiniens' italic", "upright", "italics", None, "high",
      "des anneaux artiniens", "des anneaux \\emph{artiniens}"),
    F(49, "proof of (3.4.4): 'p = 0 et A = A_1 (0, 16.1.2.2)'", "bold 0", "$(0,16.1.2.2)$", "convention", 2, "high",
      "$(0,16.1.2.2)$", "$(\\mathbf{0},16.1.2.2)$"),
    F(49, "proof of (3.4.4), second paragraph: 'on déduit encore de (0, 15.2.4)'", "bold 0", "$(0,15.2.4)$", "convention", 2, "high",
      "encore de $(0,15.2.4)$", "encore de $(\\mathbf{0},15.2.4)$"),
]


def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
for page in sorted({x["page"] for x in f}):
    text = page_text(page)
    fixes = [x["fix"] for x in f if x["page"] == page and x["fix"]]
    for fx in fixes:
        c = text.count(fx["old"])
        if c != 1:
            ok = False
            print(f"p.{page}: old occurs {c} times: {fx['old']!r}")
    for label, order in (("forward", fixes), ("reverse", list(reversed(fixes)))):
        t = text
        for fx in order:
            c = t.count(fx["old"])
            if c != 1:
                ok = False
                print(f"p.{page} {label}: old occurs {c} times at application: {fx['old']!r}")
            t = t.replace(fx["old"], fx["new"], 1)

counts = {}
for x in f:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("all checks ok" if ok else "CHECK FAILED")
print(counts)
if ok:
    OUT.write_text(json.dumps(f, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("wrote", OUT, len(f), "findings")
