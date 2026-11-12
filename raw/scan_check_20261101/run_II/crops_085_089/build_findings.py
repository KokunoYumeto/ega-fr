"""Build findings_085_089.json for the EGA II scan check (pp. 85-89) and verify the fixes.

Each fix's "old" must occur exactly once in the LF-normalised page_NNN.tex.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
OUT = os.path.join(RUN, "findings_085_089.json")


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, nofix=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if nofix else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


BOLD_NOTE = "Bold chapter number in the print, plain in the TeX."
BLANK_NOTE = ("The page break falls mid-sentence; the blank lines around the \\oldpage marker make a paragraph "
              "break the print does not have.")

f = []

# ---------------------------------------------------------------- page 85
f += [
    F(85, "proof of (4.5.4): 'il existe un élément homogène f∈S_+ tel que Z⊂(Proj(S))_f⊂U (2.4.1)'",
      "Z⊂(Proj(S))_f⊂U: Z without a prime", "$Z'\\subset(\\operatorname{Proj}(S))_f\\subset U$",
      "misprint_in_print", None, "high",
      "$Z'\\subset(\\operatorname{Proj}(S))_f\\subset U$", "$Z\\subset(\\operatorname{Proj}(S))_f\\subset U$",
      "The TeX silently corrects the print. The sentence quantifies over 'toute partie finie Z′ de Proj(S)' "
      "(Z′ twice in the same sentence); Z is the finite subset of X in (4.5.4). Checked on a 2x crop: no prime.",
      corrected="$Z'\\subset(\\operatorname{Proj}(S))_f\\subset U$"),
    F(85, "proof of (4.5.4), first line: 'En vertu de (4.5.2, b))'",
      "'b)' italic (the b and its closing parenthesis); the outer ')' roman", "b) upright in the link text",
      "italics", None, "high", "{4.5.2, b)}", "{4.5.2, \\emph{b)}}", "Checked on a 2.5x crop."),
    F(85, "proof of (4.5.4): 'est de la forme V_+(𝔍), où 𝔍 est un idéal gradué de S'",
      "Fraktur 𝔍 (J form, with a descender) twice", "\\mathfrak{I} twice",
      "symbol", None, "high",
      "$V_+(\\mathfrak{I})$, où $\\mathfrak{I}$", "$V_+(\\mathfrak{J})$, où $\\mathfrak{J}$",
      "Checked on a 2x crop. ega2-1-fr.tex writes this printed glyph \\mathfrak{J} elsewhere (pp. 23-54, 112-114, "
      "185-186); same change as EGA I p. 120."),
    F(85, "proof of (4.5.4): 'idéaux premiers gradués 𝔭_i de S_+ ne contenant pas 𝔍 (2.3.1)'",
      "Fraktur 𝔍", "\\mathfrak{I}", "symbol", None, "high",
      "ne contenant pas $\\mathfrak{I}$", "ne contenant pas $\\mathfrak{J}$", "See the previous finding."),
    F(85, "proof of (4.5.4): 'Il existe donc un élément f∈𝔍'",
      "Fraktur 𝔍", "\\mathfrak{I}", "symbol", None, "high",
      "$f\\in\\mathfrak{I}$", "$f\\in\\mathfrak{J}$", "See the previous finding."),
    F(85, "Proposition (4.5.5): 'Les conditions a) à c′) de (4.5.2)'",
      "'a)' and 'c′)' upright, 'à' and 'de' italic", "all italic (inside the \\itshape proposition environment)",
      "convention", 6, "high", "Les conditions a) à c') de", "Les conditions \\textup{a)} à \\textup{c')} de",
      "Checked on a crop."),
    F(85, "Proposition (4.5.5): 'de (4.5.2) sont aussi équivalentes'",
      "the reference (4.5.2) upright", "italic (inside the \\itshape proposition environment)",
      "convention", 6, "high",
      "(\\hyperref[II.4.5.2-fr]{4.5.2}) sont aussi", "\\textup{(\\hyperref[II.4.5.2-fr]{4.5.2})} sont aussi",
      "Checked on a crop."),
    F(85, "Proposition (4.5.5), d″): 'La propriété d′) a lieu'",
      "'d′)' upright inside the italic statement", "italic", "convention", 6, "high",
      "La propriété d') a lieu", "La propriété \\textup{d')} a lieu", ""),
    F(85, "proof of (4.5.5): 'engendré par un nombre fini de ces sections'",
      "'fini' italic", "fini upright", "italics", None, "high",
      "un nombre fini de ces sections", "un nombre \\emph{fini} de ces sections", "Checked on a crop."),
    F(85, "proof of (4.5.5): '(0, 5.2.3)'", "(𝟎, 5.2.3)", "plain 0 in the link text", "convention", 2, "high",
      "{0, 5.2.3}", "{\\textbf{0}, 5.2.3}", BOLD_NOTE),
    F(85, "proof of (4.5.5): 'donc d) implique d′)'",
      "'d)' and 'd′)' italic (letters and parentheses)", "upright", "italics", None, "high",
      "donc d) implique d') et", "donc \\emph{d)} implique \\emph{d')} et", "Checked on a crop."),
    F(85, "proof of (4.5.5): 'il est clair que d′) implique d″)'",
      "'d′)' and 'd″)' italic", "upright", "italics", None, "high",
      "que\nd') implique d'').", "que\n\\emph{d')} implique \\emph{d'')}.", "Checked on a crop."),
    F(85, "proof of (4.5.5): 'sous-𝒪_X-Modules de type fini (I, 9.4.9)'", "(𝐈, 9.4.9)",
      "plain I in the link text", "convention", 2, "high", "{I, 9.4.9}", "{\\textbf{I}, 9.4.9}", BOLD_NOTE),
    F(85, "proof of (4.5.5): 'pour vérifier la condition c′) de (4.5.2)'", "'c′)' italic", "upright",
      "italics", None, "high", "la condition c')", "la condition \\emph{c')}", "Checked on a crop."),
    F(85, "proof of (4.5.5): 'et d″) entraîne donc c′)'", "'d″)' and 'c′)' italic", "upright",
      "italics", None, "high", "et d'')\nentraîne donc c').", "et \\emph{d'')}\nentraîne donc \\emph{c')}.",
      "Checked on a crop."),
    F(85, "proof of (4.5.5): 'la propriété d) est vérifiée'", "'d)' italic", "upright", "italics", None, "high",
      "la propriété\nd) est vérifiée", "la propriété\n\\emph{d)} est vérifiée", "Checked on a crop."),
    F(85, "proof of (4.5.5): 'au-dessus de X_{f_i} (I, 1.3.13)'", "(𝐈, 1.3.13)", "plain I in the link text",
      "convention", 2, "high", "{I, 1.3.13}", "{\\textbf{I}, 1.3.13}", BOLD_NOTE),
    F(85, "proof of (4.5.5): 'pour tout couple (i, j) (I, 9.3.1)'", "(𝐈, 9.3.1)", "plain I in the link text",
      "convention", 2, "high", "{I, 9.3.1}", "{\\textbf{I}, 9.3.1}", BOLD_NOTE),
    F(85, "Proposition (4.5.6), (ii), end of p. 85: 'il existe un entier n>0' / p. 86 'et une section s′'",
      "one sentence running on to p. 86, no paragraph break", "blank line before \\oldpage[II]{86}",
      "other", None, "high", "il existe un entier $n>0$\n\n", "il existe un entier $n>0$\n",
      BLANK_NOTE + " Apply together with the p. 86 fix for the blank line after the marker."),
]

# ---------------------------------------------------------------- page 86
f += [
    F(86, "start of p. 86, Proposition (4.5.6) (ii): 'et une section s′ de ℒ′^{⊗n}'",
      "continues the sentence of p. 85, no paragraph break", "blank line after \\oldpage[II]{86}",
      "other", None, "high", "\\oldpage[II]{86}\n\n  et une section", "\\oldpage[II]{86}\n  et une section",
      BLANK_NOTE + " Apply together with the p. 85 fix for the blank line before the marker."),
    F(86, "proof of (4.5.6): 'conséquence évidente du critère a) de (4.5.2)'",
      "only the letter 'a' italic; its parenthesis upright", "a) upright", "italics", None, "medium",
      "du critère a) de", "du critère \\emph{a}) de",
      "Checked on a 6x crop: the parenthesis is upright here, unlike the slanted ones of 'a)' on the same page."),
    F(86, "proof of (4.5.6): 'tel que x∈X_f⊂U (4.5.2, a));'",
      "'a)' italic (letter and its parenthesis); outer ')' roman", "a) upright", "italics", None, "high",
      "{4.5.2, a)})~; si", "{4.5.2, \\emph{a)}})~; si", "Checked on a 3x crop."),
    F(86, "proof of (4.5.6), end: 'est ample (4.5.2, a)).'",
      "'a)' italic (letter and its parenthesis); outer ')' roman", "a) upright", "italics", None, "high",
      "{4.5.2, a)}).", "{4.5.2, \\emph{a)}}).", "Checked on a 3x crop."),
    F(86, "Remarque (4.5.9): 'inversibles (0, 5.4.7)'", "(𝟎, 5.4.7)", "plain 0 in the link text",
      "convention", 2, "high", "{0, 5.4.7}", "{\\textbf{0}, 5.4.7}", BOLD_NOTE),
    F(86, "Remarque (4.5.9): 'Supposons que P^+ soit non vide.'", "'non vide' italic in the roman remark",
      "no \\emph", "italics", None, "high", "soit non vide", "soit \\emph{non vide}",
      "Judged with the remark body as roman."),
    F(86, "Remarque (4.5.9): 'l'ensemble des éléments positifs dans P'", "'positifs' italic", "no \\emph",
      "italics", None, "high", "éléments positifs", "éléments \\emph{positifs}", ""),
    F(86, "Remarque (4.5.9): 'pour une structure de préordre sur P'", "'préordre' italic", "no \\emph",
      "italics", None, "high", "structure de préordre", "structure de \\emph{préordre}", ""),
    F(86, "Remarque (4.5.9): 'et qui est même archimédienne'", "'archimédienne' italic", "no \\emph",
      "italics", None, "high", "même archimédienne", "même \\emph{archimédienne}", ""),
    F(86, "Proposition (4.5.10) (ii): 'que le morphisme q soit de type fini.'",
      "'de type fini' upright inside the italic statement", "italic", "convention", 6, "high",
      "soit de type fini.", "soit \\textup{de type fini}.", ""),
    F(86, "proof of (4.5.10): 'on voit que la condition a) de (4.5.2) est vérifiée'",
      "'a)' italic (letter and parenthesis)", "upright", "italics", None, "high",
      "la condition a) de", "la condition \\emph{a)} de", "Checked on a 5x crop."),
    F(86, "proof of (4.5.10): 'il vérifie la condition e).'", "'e)' italic", "upright", "italics", None, "high",
      "la condition e).", "la condition \\emph{e)}.", "Checked on a crop."),
    F(86, "proof of (4.5.10): 'il résulte du critère b) de (4.5.2)'", "'b)' italic", "upright", "italics", None,
      "high", "du critère b)", "du critère \\emph{b)}", "Checked on a crop."),
    F(86, "proof of (4.5.10), end of p. 86: 'qu'il existe' / p. 87 'un entier k_0>0'",
      "one sentence running on to p. 87, no paragraph break", "blank line before \\oldpage[II]{87}",
      "other", None, "high", "{4.4.1, (i)}) qu'il existe\n\n", "{4.4.1, (i)}) qu'il existe\n",
      BLANK_NOTE + " Apply together with the p. 87 fix for the blank line after the marker."),
]

# ---------------------------------------------------------------- page 87
f += [
    F(87, "start of p. 87: 'un entier k_0>0 tel que'",
      "continues the sentence of p. 86, no paragraph break", "blank line after \\oldpage[II]{87}",
      "other", None, "high", "\\oldpage[II]{87}\n\nun entier", "\\oldpage[II]{87}\nun entier",
      BLANK_NOTE + " Apply together with the p. 86 fix for the blank line before the marker."),
    F(87, "proof of (4.5.10): 'il est clair que e) entraîne e′), et e′) implique'",
      "'e)', 'e′)', 'e′)' italic (letters and parentheses)", "upright", "italics", None, "high",
      "que e) entraîne e'), et e') implique", "que \\emph{e)} entraîne \\emph{e')}, et \\emph{e')} implique",
      "Checked on a crop."),
    F(87, "(4.5.10.1): 'Démonstration du lemme (4.4.10.1). — Posons'",
      "only 'Démonstration du lemme' italic; '(4.4.10.1).' upright",
      "\\emph{} includes the reference and the period", "italics", None, "high",
      "\\emph{Démonstration du lemme (\\hyperref[II.4.4.10.1-fr]{4.4.10.1}).}",
      "\\emph{Démonstration du lemme} (\\hyperref[II.4.4.10.1-fr]{4.4.10.1}).",
      "Checked on a crop. Independent of the dash finding below (non-overlapping strings)."),
    F(87, "(4.5.10.1): 'Démonstration du lemme (4.4.10.1). — Posons'",
      "'. —' (period and long dash) before 'Posons'", "no dash", "punctuation", None, "high",
      "Posons\n$\\mathcal{E}(n)=", "--- Posons\n$\\mathcal{E}(n)=",
      "Checked on a crop. The env environment prints only the bold number, so the dash belongs in the text."),
    F(87, "(4.5.10.1): 'l'homomorphisme canonique g*(g_*(ℰ(n))→ℰ(n) est surjectif'",
      "g*(g_*(ℰ(n))→ℰ(n): three opening, two closing parentheses before the arrow",
      "$g^*(g_*(\\mathcal{E}(n)))\\to\\mathcal{E}(n)$ (balanced)", "misprint_in_print", None, "high",
      "$g^*(g_*(\\mathcal{E}(n)))\\to\\mathcal{E}(n)$", "$g^*(g_*(\\mathcal{E}(n))\\to\\mathcal{E}(n)$",
      "The TeX silently corrects the print. Checked on a 3x crop.",
      corrected="$g^*(g_*(\\mathcal{E}(n)))\\to\\mathcal{E}(n)$"),
    F(87, "(4.5.10.1), end: 'la conclusion résulte de (4.5.5, d′))'", "'d′)' italic; outer ')' roman",
      "d') upright", "italics", None, "high", "{4.5.5, d')}", "{4.5.5, \\emph{d')}}", ""),
    F(87, "Proposition (4.5.13): 'défini par un faisceau quasi-cohérent nilpotent 𝒥 d'idéaux'",
      "'nilpotent' upright inside the italic statement", "italic", "convention", 6, "high",
      "quasi-cohérent nilpotent $\\mathcal{J}$", "quasi-cohérent \\textup{nilpotent} $\\mathcal{J}$",
      "Checked on a crop."),
    F(87, "proof of (4.5.13): 'La condition est nécessaire.'", "'nécessaire' italic", "no \\emph", "italics",
      None, "high", "La condition est nécessaire.", "La condition est \\emph{nécessaire}.", ""),
    F(87, "proof of (4.5.13): 'donc le critère a) de (4.5.2) montre que ℒ′ est ample'",
      "'a)' italic (letter and parenthesis)", "upright", "italics", None, "high",
      "le\ncritère a)", "le\ncritère \\emph{a)}", "Checked on a 3x crop."),
    F(87, "proof of (4.5.13): 'Pour voir que la condition est suffisante'", "'suffisante' italic", "no \\emph",
      "italics", None, "high", "est suffisante,", "est \\emph{suffisante},", ""),
    F(87, "proof of (4.5.13): 'X_red l'est par hypothèse (4.5.3 et I, 5.5.1)'",
      "one pair of parentheses: (4.5.3 et 𝐈, 5.5.1), with bold I",
      "((4.5.3) et (I, 5.5.1)) with plain I", "punctuation", None, "high",
      "((\\hyperref[II.4.5.3-fr]{4.5.3}) et\n(\\hyperref[I.5.5.1-fr]{I, 5.5.1}))",
      "(\\hyperref[II.4.5.3-fr]{4.5.3} et\n\\hyperref[I.5.5.1-fr]{\\textbf{I}, 5.5.1})",
      "Checked on a 2x crop. The new text also sets the bold I (convention 2); there is no separate "
      "convention-2 edit for this reference."),
    F(87, "proof of (4.5.13): 'Le critère a) de (4.5.2) montre qu'il suffira de prouver le'",
      "'a)' italic (letter and parenthesis)", "upright", "italics", None, "high",
      "Le critère a)", "Le critère \\emph{a)}", "Checked on a 2x crop."),
    F(87, "Lemme (4.5.13.1): 'Sous les hypothèses de (4.5.13), supposons'",
      "the reference (4.5.13) upright", "italic (inside the \\itshape lemma environment)",
      "convention", 6, "high",
      "(\\hyperref[II.4.5.13-fr]{4.5.13}), supposons", "\\textup{(\\hyperref[II.4.5.13-fr]{4.5.13})}, supposons",
      "Checked on a crop."),
    F(87, "end of p. 87: display '0→𝒥(n)→…→0' / p. 88 'puisque ℱ(n) est un foncteur exact'",
      "p. 88 continues the sentence at the left margin, no paragraph break",
      "blank line before \\oldpage[II]{88}", "other", None, "high",
      "\\longrightarrow0\n\\]\n\n", "\\longrightarrow0\n\\]\n",
      BLANK_NOTE + " Apply together with the p. 88 fix for the blank line after the marker."),
]

# ---------------------------------------------------------------- page 88
f += [
    F(88, "start of p. 88: 'puisque ℱ(n) est un foncteur exact en ℱ'",
      "continues the sentence of p. 87 after the display, not indented", "blank line after \\oldpage[II]{88}",
      "other", None, "high", "\\oldpage[II]{88}\n\npuisque", "\\oldpage[II]{88}\npuisque",
      BLANK_NOTE + " Apply together with the p. 87 fix for the blank line before the marker."),
    F(88, "'un homomorphisme H^i(X, 𝒥(n)) →^s H^i(X, 𝒥(n+k)) de groupes de cohomologie'",
      "s written above the arrow", "plain \\to, no s", "formula", None, "high",
      "\\mathrm{H}^i(X,\\mathcal{J}(n))\\to\n", "\\mathrm{H}^i(X,\\mathcal{J}(n))\\xrightarrow{s}\n",
      "Checked on a 2x crop."),
    F(88, "'En effet, Z_g est un ouvert affine de Z'", "'ouvert affine' italic", "no \\emph", "italics", None,
      "high", "est un ouvert affine de", "est un \\emph{ouvert affine} de", ""),
    F(88, "'quand 𝒥(n) est considéré comme un 𝒪_Z-Module (I, 5.1.9.2)'", "'Module' italic",
      "Module upright", "italics", None, "high",
      "$\\mathcal{O}_Z$-Module\n(\\hyperref[I.5.1.9.2-fr]", "$\\mathcal{O}_Z$-\\emph{Module}\n(\\hyperref[I.5.1.9.2-fr]",
      "Checked on a 2x crop. Independent of the bold-I edit at the same reference."),
    F(88, "'comme un 𝒪_Z-Module (I, 5.1.9.2)'", "(𝐈, 5.1.9.2)", "plain I in the link text", "convention", 2,
      "high", "{I, 5.1.9.2}", "{\\textbf{I}, 5.1.9.2}", BOLD_NOTE),
    F(88, "'que l'on peut supposer fini et formé d'ouverts affines'", "'fini' italic", "no \\emph", "italics",
      None, "high", "supposer fini et formé", "supposer \\emph{fini} et formé", ""),
    F(88, "'telle que (g_{α|β}−g_{β|α})|(U_α∩U_β∩Z_g)=h_{α|β}−h_{β|α} en désignant par'",
      "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
      "\\[\n  (g_{\\alpha|\\beta}-g_{\\beta|\\alpha})\n  |(U_\\alpha\\cap U_\\beta\\cap Z_g)\n"
      "  =h_{\\alpha|\\beta}-h_{\\beta|\\alpha}\n\\]",
      "$(g_{\\alpha|\\beta}-g_{\\beta|\\alpha})\n|(U_\\alpha\\cap U_\\beta\\cap Z_g)\n"
      "=h_{\\alpha|\\beta}-h_{\\beta|\\alpha}$",
      "'telle que' and 'en désignant par h_{α|β}' stand on the same printed line as the formula."),
    F(88, "'pour tout α (I, 9.3.1); on a donc'", "(𝐈, 9.3.1)", "plain I in the link text", "convention", 2,
      "high", "{I, 9.3.1}", "{\\textbf{I}, 9.3.1}", BOLD_NOTE),
    F(88, "'on a donc g^{⊗m}⊗(g_{α|β}−g_{β|α})=t_{α|β}−t_{β|α} pour tout couple d'indices'",
      "formula set inline in the running text", "displayed with \\[ ... \\]", "other", None, "high",
      "\\[\n  g^{\\otimes m}\\otimes(g_{\\alpha|\\beta}-g_{\\beta|\\alpha})\n"
      "  =t_{\\alpha|\\beta}-t_{\\beta|\\alpha}\n\\]",
      "$g^{\\otimes m}\\otimes(g_{\\alpha|\\beta}-g_{\\beta|\\alpha})\n=t_{\\alpha|\\beta}-t_{\\beta|\\alpha}$",
      "'on a donc' and 'pour tout couple d'indices, ce qui' stand on the same printed line as the formula."),
    F(88, "proof of (4.5.13.3): 's_α∈Γ(U_α, 𝒪_X(p)) (resp. t_α∈Γ(U_α, 𝒪_X(q)) dont l'image'",
      "'(resp.' is never closed: 𝒪_X(q)) with two closing parentheses",
      "the same (TeX keeps the printed reading)", "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. Checked on a 2x crop.",
      corrected="(resp. $t_\\alpha\\in\\Gamma(U_\\alpha,\\mathcal{O}_X(q))$)", nofix=True),
    F(88, "proof of (4.5.13.3): 'Γ(U_α, 𝒪_Z(p)) (resp. Γ(U_α, 𝒪_Z(q)) soit s|U_α'",
      "'(resp.' is never closed: 𝒪_Z(q)) with two closing parentheses",
      "the same (TeX keeps the printed reading)", "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. Checked on a 2x crop.",
      corrected="(resp. $\\Gamma(U_\\alpha,\\mathcal{O}_Z(q))$)", nofix=True),
    F(88, "end of p. 88: display (4.5.13.4) / p. 89 'et on conclut de (4.5.13.2)'",
      "p. 89 continues the sentence at the left margin, no paragraph break",
      "blank line before \\oldpage[II]{89}", "other", None, "high",
      "\\tag{4.5.13.4}\n\\end{equation}\n\n", "\\tag{4.5.13.4}\n\\end{equation}\n",
      BLANK_NOTE + " Apply together with the p. 89 fix for the blank line after the marker."),
]

# ---------------------------------------------------------------- page 89
f += [
    F(89, "start of p. 89: 'et on conclut de (4.5.13.2) et (4.5.13.4)'",
      "continues the sentence of p. 88, not indented", "blank line after \\oldpage[II]{89}",
      "other", None, "high", "\\oldpage[II]{89}\n\net on conclut", "\\oldpage[II]{89}\net on conclut",
      BLANK_NOTE + " Apply together with the p. 88 fix for the blank line before the marker."),
    F(89, "after Corollaire (4.5.14): 'Cela résulte de (I, 6.1.6).'", "(𝐈, 6.1.6)", "plain I in the link text",
      "convention", 2, "high", "{I, 6.1.6}", "{\\textbf{I}, 6.1.6}", BOLD_NOTE),
    F(89, "Définition (4.6.1): '(ou même ample si aucune confusion n'en résulte avec la notion définie dans (4.5.3))'",
      "the whole parenthesis upright, only 'ample' italic", "all italic (inside the \\itshape definition environment)",
      "convention", 6, "high",
      "(ou\nmême ample si aucune confusion n'en résulte avec la notion définie dans\n"
      "(\\hyperref[II.4.5.3-fr]{4.5.3}))",
      "\\textup{(ou\nmême \\emph{ample} si aucune confusion n'en résulte avec la notion définie dans\n"
      "(\\hyperref[II.4.5.3-fr]{4.5.3}))}",
      "Checked on a crop. Inside \\textup the \\emph gives the italic 'ample'."),
    F(89, "'entraîne que f est nécessairement séparé'", "'séparé' italic", "no \\emph", "italics", None, "high",
      "nécessairement séparé", "nécessairement \\emph{séparé}", "Checked on a crop."),
    F(89, "'((4.5.3) et (I, 5.5.5))'", "(𝐈, 5.5.5)", "plain I in the link text", "convention", 2, "high",
      "{I, 5.5.5}", "{\\textbf{I}, 5.5.5}", BOLD_NOTE),
    F(89, "Proposition (4.6.3) b): 'σ : f*(𝒮)→⊕ℒ^{⊗n} (0, 4.4.3) est tel que'",
      "(𝟎, 4.4.3) upright with bold 0 inside the italic statement",
      "plain 0, and the reference italic in the \\itshape proposition environment", "convention", 2, "high",
      "(\\hyperref[0.4.4.3-fr]{0, 4.4.3})", "\\textup{(\\hyperref[0.4.4.3-fr]{\\textbf{0}, 4.4.3})}",
      "Checked on a crop. One edit for both conventions 2 and 6 (same form as EGA I p. 172)."),
    F(89, "Proposition (4.6.3), after (4.6.3.1): 'défini dans (3.7.9.1), est un isomorphisme'",
      "the reference (3.7.9.1) upright", "italic (inside the \\itshape proposition environment)",
      "convention", 6, "high",
      "(\\hyperref[II.3.7.9.1-fr]{3.7.9.1})", "\\textup{(\\hyperref[II.3.7.9.1-fr]{3.7.9.1})}", ""),
    F(89, "Proposition (4.6.3), after (4.6.3.2): 'défini dans (3.7.9.2), est un isomorphisme'",
      "the reference (3.7.9.2) upright", "italic (inside the \\itshape proposition environment)",
      "convention", 6, "high",
      "(\\hyperref[II.3.7.9.2-fr]{3.7.9.2})", "\\textup{(\\hyperref[II.3.7.9.2-fr]{3.7.9.2})}", ""),
    F(89, "proof of (4.6.3): 'On a remarqué que a) implique que f est séparé'", "'a)' italic", "upright",
      "italics", None, "high", "On a remarqué que a) implique", "On a remarqué que \\emph{a)} implique", ""),
    F(89, "proof of (4.6.3): 'quasi-cohérente (I, 9.2.2, a))'", "(𝐈, 9.2.2, a))", "plain I in the link text",
      "convention", 2, "high", "[I.9.2.2-fr]{I,", "[I.9.2.2-fr]{\\textbf{I},",
      BOLD_NOTE + " Independent of the italic-a) edit at the same reference."),
    F(89, "proof of (4.6.3): 'quasi-cohérente (I, 9.2.2, a))'",
      "'a)' italic (letter and parenthesis); outer ')' roman", "a) upright", "italics", None, "high",
      "9.2.2, a)})", "9.2.2, \\emph{a)}})", "Independent of the bold-I edit at the same reference."),
    F(89, "proof of (4.6.3): 'pour prouver que a) entraîne b), on peut supposer'", "'a)' and 'b)' italic",
      "upright", "italics", None, "high",
      "pour prouver que a) entraîne b),", "pour prouver que \\emph{a)} entraîne \\emph{b)},", ""),
    F(89, "end of p. 89: 'on peut supposer Y affine et ℒ ample;' / p. 90 'l'assertion résulte alors'",
      "one sentence running on to p. 90, no paragraph break", "blank line before \\oldpage[II]{90}",
      "other", None, "high", "$\\mathcal{L}$ ample~;\n\n", "$\\mathcal{L}$ ample~;\n",
      BLANK_NOTE + " The blank line after \\oldpage[II]{90} lies in the p. 90 file; remove it in the same pass."),
]


def main():
    pages = {}
    for p in (85, 86, 87, 88, 89):
        with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
            pages[p] = fh.read().replace("\r\n", "\n")
    bad = 0
    for d in f:
        if d["fix"] is None:
            continue
        old = d["fix"]["old"]
        n = pages[d["page"]].count(old)
        if n != 1:
            bad += 1
            print("COUNT %d on p. %d: %r" % (n, d["page"], old))
    # check that applying all fixes of a page in order succeeds (independence)
    for p, text in pages.items():
        t = text
        for d in f:
            if d["page"] != p or d["fix"] is None:
                continue
            old, new = d["fix"]["old"], d["fix"]["new"]
            if t.count(old) != 1:
                bad += 1
                print("SEQUENTIAL FAIL p. %d: %r" % (p, old))
                continue
            t = t.replace(old, new)
        # reverse order as well
        t = text
        for d in reversed(f):
            if d["page"] != p or d["fix"] is None:
                continue
            old, new = d["fix"]["old"], d["fix"]["new"]
            if t.count(old) != 1:
                bad += 1
                print("REVERSE FAIL p. %d: %r" % (p, old))
                continue
            t = t.replace(old, new)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(f, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    counts = {}
    for d in f:
        c = counts.setdefault(d["page"], [0, 0, 0])
        if d["kind"] == "convention":
            c[1] += 1
        elif d["kind"] == "misprint_in_print":
            c[2] += 1
        else:
            c[0] += 1
    print("problems:", bad)
    print("counts (normal/convention/misprint):", counts)
    print("written", OUT, len(f))


if __name__ == "__main__":
    main()
