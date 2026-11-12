"""Build findings_095_099.json for the EGA II scan check (pp. 95-99) and verify
that every fix's "old" occurs exactly once in its page_NNN.tex (CRLF -> LF).

In the strings below, the pilcrow character stands for a line break (LF).
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
OUT = os.path.join(RUN, "findings_095_099.json")
NL = "\u00b6"


def nl(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    rec = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": nl(old), "new": nl(new)},
    }
    if kind == "misprint_in_print":
        rec["corrected"] = corrected
    rec["note"] = note
    F.append(rec)


# ---------------------------------------------------------------- page 95
add(95, "proof of (5.1.2): 'Il est clair que b) entraîne a), et a) entraîne c) en vertu du critère b) de (4.4.4)'",
    "the criterion letters b), a), a), c), b) italic", "upright b) a) a) c) b)", "italics", None, "high",
    r"Il est clair que b) entraîne a), et a) entraîne c) en vertu du critère b) de",
    r"Il est clair que \emph{b)} entraîne \emph{a)}, et \emph{a)} entraîne \emph{c)} en vertu du critère \emph{b)} de")
add(95, "proof of (5.1.2): 'd'autre part c) entraîne c') (4.5.10, (i))'",
    "c) and c') italic; '(i)' roman", "upright c) c')", "italics", None, "high",
    r"d'autre part c) entraîne c')",
    r"d'autre part \emph{c)} entraîne \emph{c')}",
    "Checked on a crop.")
add(95, "proof of (5.1.2): 'et c'), b) et b') sont équivalents'",
    "c'), b), b') italic", "upright", "italics", None, "high",
    r"et c'), b) et b') sont",
    r"et \emph{c')}, \emph{b)} et \emph{b')} sont")
add(95, "proof of (5.1.2): '(4.5.2, critères b) et b'))'",
    "b) and b') italic", "upright in the link text", "italics", None, "high",
    r"{4.5.2, critères b) et b')}",
    r"{4.5.2, critères \emph{b)} et \emph{b')}}")
add(95, "proof of (5.1.2): 'Enfin c') équivaut à chacun des critères'",
    "c') italic", "upright", "italics", None, "high",
    r"Enfin c') équivaut",
    r"Enfin \emph{c')} équivaut")
add(95, "proof of (5.1.2): 'chacun des critères d), d'), e), e') en vertu de'",
    "d), d'), e), e') italic", "upright", "italics", None, "high",
    r"critères d), d'), e), e') en vertu",
    r"critères \emph{d)}, \emph{d')}, \emph{e)}, \emph{e')} en vertu")
add(95, "proof of (5.1.2): '(4.5.2, critères a), a'), c))'",
    "a), a'), c) italic", "upright in the link text", "italics", None, "high",
    r"{4.5.2, critères a), a'), c)}",
    r"{4.5.2, critères \emph{a)}, \emph{a')}, \emph{c)}}")
add(95, "proof of (5.1.2): '(4.5.5, critère d''))'",
    "d'') italic", "upright in the link text", "italics", None, "high",
    r"{4.5.5, critère d'')}",
    r"{4.5.5, critère \emph{d'')}}")
add(95, "proof of (5.1.3): 'X_{f_α}=ψ^{-1}(D(g_α)) (I, 2.2.4.1)'",
    "(I, 2.2.4.1) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 2.2.4.1}",
    r"{\textbf{I}, 2.2.4.1}")
add(95, "proof of (5.1.3): 'et le critère d) de (5.1.2) est vérifié'",
    "d) italic", "upright", "italics", None, "high",
    r"le critère d) de",
    r"le critère \emph{d)} de")
add(95, "Corollaire (5.1.4): 'Si X est un schéma quasi-affine, tout 𝒪_X-Module inversible'",
    "'tout' roman inside the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"schéma quasi-affine, tout",
    r"schéma quasi-affine, \textup{tout}",
    "Checked on a crop: 'tout' is upright, the words around it italic.")
add(95, "Corollaire (5.1.4): 'et a fortiori ample'",
    "'a fortiori' roman inside the italic statement", "italic (corollary environment)", "convention", 6, "high",
    r"et a fortiori ample",
    r"et \textup{a fortiori} ample",
    "Checked on a crop.")
add(95, "proof of (5.1.4): 'En effet un tel Module ℒ est engendré'",
    "'En effet un tel Module' (no comma)", "'En effet, un tel Module'", "punctuation", None, "high",
    r"En effet, un tel Module",
    r"En effet un tel Module",
    "Checked on a crop.")
add(95, "proof of (5.1.4): '(5.1.2, e))'",
    "e) italic", "upright in the link text", "italics", None, "high",
    r"{5.1.2, e)}",
    r"{5.1.2, \emph{e)}}")
add(95, "Proposition (5.1.6), b): '𝒜(X)→𝒜(X) (1.2.7) est une immersion ouverte'",
    "(1.2.7) upright inside the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"(\hyperref[II.1.2.7-fr]{1.2.7})",
    r"\textup{(\hyperref[II.1.2.7-fr]{1.2.7})}",
    "Checked on a crop.")
add(95, "Proposition (5.1.6), d): 'Le morphisme f est séparé, et pour tout 𝒪_X-Module'",
    "'séparé, et pour tout'", "'séparé et, pour tout'", "punctuation", None, "high",
    r"est séparé et, pour tout",
    r"est séparé, et pour tout",
    "Checked on a crop.")
add(95, "Proposition (5.1.6), d): 'σ : f^*(f_*(ℱ))→ℱ (0, 4.4.3) est surjectif'",
    "(0, 4.4.3) upright inside the italic statement, with bold 0", "italic, plain 0", "convention", 6, "high",
    r"(\hyperref[0.4.4.3-fr]{0, 4.4.3})",
    r"\textup{(\hyperref[0.4.4.3-fr]{\textbf{0}, 4.4.3})}",
    "Checked on a crop. The edit also sets the bold 0 (convention 2) of this reference, since the two changes overlap; there is no separate convention-2 finding for it.")
add(95, "after (5.1.6): 'L'équivalence de a) et c') résulte'",
    "a) and c') italic", "upright", "italics", None, "high",
    r"L'équivalence de a) et c')",
    r"L'équivalence de \emph{a)} et \emph{c')}")
add(95, "after (5.1.6): 'et du critère (5.1.2, c'))'",
    "c') italic", "upright in the link text", "italics", None, "high",
    r"{5.1.2, c')}",
    r"{5.1.2, \emph{c')}}")
add(95, "end of the page: '... Les autres propriétés sont locales sur Y' / p. 96 'et résultent donc ...'",
    "the sentence continues on p. 96; the first line of p. 96 is not indented (no new paragraph)",
    "blank line after '$Y$' before \\oldpage[II]{96} (and another after the marker): a paragraph break",
    "other", None, "high",
    r"locales sur¶$Y$¶¶",
    r"locales sur¶$Y$¶",
    "Spurious paragraph break at the page boundary; apply together with the p. 96 finding that removes the blank line after \\oldpage[II]{96} (both blank lines must go).")

# ---------------------------------------------------------------- page 96
add(96, "top of the page: 'et résultent donc aussitôt de (5.1.2) et (5.1.4)'",
    "continues the sentence of p. 95; first line not indented", "blank line after \\oldpage[II]{96}: a new paragraph",
    "other", None, "high",
    r"\oldpage[II]{96}¶¶et résultent",
    r"\oldpage[II]{96}¶et résultent",
    "Spurious paragraph break; apply together with the p. 95 finding that removes the blank line before the marker.")
add(96, "first paragraph: 'lorsque f est séparé (I, 9.2.2, a))'",
    "(I, 9.2.2, a)) with bold I", "plain I in the link text", "convention", 2, "high",
    r"\hyperref[I.9.2.2-fr]{I, 9.2.2",
    r"\hyperref[I.9.2.2-fr]{\textbf{I}, 9.2.2",
    "Independent of the italic 'a)' finding at the same reference (either order works).")
add(96, "first paragraph: 'lorsque f est séparé (I, 9.2.2, a))'",
    "a) italic", "upright in the link text", "italics", None, "high",
    r"9.2.2, a)}",
    r"9.2.2, \emph{a)}}",
    "Checked on a crop. Independent of the bold-I finding at the same reference (either order works).")
add(96, "Corollaire (5.1.9): 'f : X→Y un morphisme de type fini. Si f est quasi-affine'",
    "'de type fini' roman inside the italic statement", "italic", "convention", 6, "high",
    r"un morphisme de type fini. Si",
    r"un morphisme \textup{de type fini}. Si",
    "Checked on a crop.")
add(96, "Corollaire (5.1.9): '𝒜(X)=f_*(𝒪_X), de type fini (I, 9.6.2), telle que'",
    "'de type fini (I, 9.6.2)' roman inside the italic statement, bold I", "italic, plain I", "convention", 6, "high",
    r"de type fini¶(\hyperref[I.9.6.2-fr]{I, 9.6.2})",
    r"\textup{de type fini¶(\hyperref[I.9.6.2-fr]{\textbf{I}, 9.6.2})}",
    "Checked on a crop. The edit also sets the bold I (convention 2) of this reference, since the two changes overlap; there is no separate convention-2 finding for it. The later 'de type fini ℬ′' of the statement is italic in the print, as in the TeX.")
add(96, "Corollaire (5.1.9): 'ℬ→𝒜(X) (1.2.7) soit une immersion'",
    "(1.2.7) upright inside the italic statement", "italic", "convention", 6, "high",
    r"(\hyperref[II.1.2.7-fr]{1.2.7})",
    r"\textup{(\hyperref[II.1.2.7-fr]{1.2.7})}",
    "Checked on a crop.")
add(96, "proof of (5.1.9): 'quasi-cohérentes de type fini (I, 9.6.5)'",
    "(I, 9.6.5) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 9.6.5}",
    r"{\textbf{I}, 9.6.5}")
add(96, "proof of (5.1.10): 'Compte tenu du critère (5.1.6, c'))'",
    "c') italic", "upright in the link text", "italics", None, "high",
    r"{5.1.6, c')}",
    r"{5.1.6, \emph{c')}}",
    "Checked on a crop.")
add(96, "proof of (5.1.10): '(4.6.13, (i bis), (iii), (iv), (v) et (vi))'",
    "'bis' italic", "upright", "italics", None, "high",
    r"(i bis)",
    r"(i \emph{bis})",
    "Checked on a crop.")
add(96, "Remarque (5.1.11): 'étant quasi-compacte (I, 6.3.5)'",
    "(I, 6.3.5) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 6.3.5}",
    r"{\textbf{I}, 6.3.5}")
add(96, "Remarque (5.1.11): 'et (I, 5.5.12) montre que'",
    "(I, 5.5.12) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 5.5.12}",
    r"{\textbf{I}, 5.5.12}")
add(96, "proof of (5.1.12): 'un entier n tel que [display] soit ample pour f∘g'",
    "displayed formula g^*(ℒ^{⊗n}) = (g^*(ℒ))^{⊗n}, then 'soit ample pour f∘g' (not indented)",
    "inline $g^*(\\mathcal{L})^{\\otimes n}$ only", "formula", None, "high",
    r"entier $n$ tel que $g^*(\mathcal{L})^{\otimes n}$ soit ample pour",
    r"entier $n$ tel que¶\[¶  g^*(\mathcal{L}^{\otimes n})=(g^*(\mathcal{L}))^{\otimes n}¶\]¶soit ample pour",
    "Checked on a crop. The print's display has no final punctuation; the line after it continues the sentence.")

# ---------------------------------------------------------------- page 97
add(97, "Théorème (5.2.1), title",
    "'Théorème (5.2.1) (critère de Serre). — Soit': lowercase 'critère', no period inside the parentheses, roman",
    "\\emph{(Critère de Serre.)} at the start of the body", "word", None, "high",
    r"\emph{(Critère de Serre.)}",
    r"\emph{(critère de Serre).}",
    "Checked on a crop. The title's position between the number and '. —' is the document-wide titles-in-parentheses item; this edit only matches the title's letters and the place of the period.")
add(97, "Théorème (5.2.1), c): 'dans la catégorie des 𝒪_X-Modules quasi-cohérents, autrement dit, si'",
    "comma after 'quasi-cohérents'", "'quasi-cohérents~; autrement dit'", "punctuation", None, "high",
    r"quasi-cohérents~; autrement dit, si",
    r"quasi-cohérents, autrement dit, si",
    "Checked on a crop.")
add(97, "Théorème (5.2.1), c'): 'La propriété c) a lieu pour toute suite exacte (*) de'",
    "'c)' and the parentheses of '(*)' upright inside the italic statement", "italic", "convention", 6, "high",
    r"La propriété c) a lieu pour toute suite exacte (*) de",
    r"La propriété \textup{c)} a lieu pour toute suite exacte \textup{(*)} de",
    "Checked on 1x and 3x crops.")
add(97, "proof of (5.2.1): 'Il est évident que a) implique b); b) implique d'autre part'",
    "a), b), b) italic", "upright", "italics", None, "high",
    r"Il est évident que a) implique b)~; b) implique",
    r"Il est évident que \emph{a)} implique \emph{b)}~; \emph{b)} implique")
add(97, "proof of (5.2.1): 'On sait que a) implique c) (I, 1.3.11)'",
    "a) and c) italic", "upright", "italics", None, "high",
    r"On sait que a) implique c) (",
    r"On sait que \emph{a)} implique \emph{c)} (")
add(97, "proof of (5.2.1): '(I, 1.3.11), et c) entraîne'",
    "(I, 1.3.11) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 1.3.11}",
    r"{\textbf{I}, 1.3.11}",
    "Independent of the comma finding at the same reference (either order works).")
add(97, "proof of (5.2.1): '(I, 1.3.11), et c) entraîne trivialement c')'",
    "comma after the reference: '(I, 1.3.11), et c)'", "'(I, 1.3.11}) et c)': no comma", "punctuation", None, "high",
    r"1.3.11}) et",
    r"1.3.11}), et",
    "Checked on a crop. Independent of the bold-I and italic edits nearby (either order works).")
add(97, "proof of (5.2.1): 'et c) entraîne trivialement c'). Prouvons que c') implique b). Tout d'abord, c')'",
    "c), c'), c'), b), c') italic", "upright", "italics", None, "high",
    r"et c)¶entraîne trivialement c'). Prouvons que c') implique b). Tout d'abord, c')",
    r"et \emph{c)}¶entraîne trivialement \emph{c')}. Prouvons que \emph{c')} implique \emph{b)}. Tout d'abord, \emph{c')}")
add(97, "proof of (5.2.1): 'pour tout point fermé x∈X'",
    "'fermé' italic", "upright", "italics", None, "high",
    r"pour tout point fermé $x\in X$",
    r"pour tout point \emph{fermé} $x\in X$",
    "Checked on a crop.")
add(97, "proof of (5.2.1): 'x∈X_f⊂X—U'",
    "long dash for the set difference", "minus sign", "convention", 7, "high",
    r"X_f\subset X-U$",
    r"X_f\subset X\setmin U$",
    "\\setmin is not yet the long dash (global change pending).")
add(97, "proof of (5.2.1): 'ayant pour espace sous-jacent X—U'",
    "long dash for the set difference", "minus sign", "convention", 7, "high",
    r"espace sous-jacent $X-U$",
    r"espace sous-jacent $X\setmin U$",
    "As above.")
add(97, "proof of (5.2.1): '(resp. (X—U)∪{x})'",
    "long dash for the set difference", "minus sign", "convention", 7, "high",
    r"$(X-U)\cup\{x\}$",
    r"$(X\setmin U)\cup\{x\}$",
    "As above.")
add(97, "proof of (5.2.1): '(resp. (X—U)∪{x}) (I, 5.2.1)'",
    "(I, 5.2.1) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 5.2.1}",
    r"{\textbf{I}, 5.2.1}")
add(97, "proof of (5.2.1): 'et tel que 𝒥''_x=k(x)'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"\mathcal{J}''_x=k(x)$",
    r"\mathcal{J}''_x=\boldsymbol{k}(x)$")
add(97, "proof of (5.2.1): 'L'hypothèse c') appliquée à la suite exacte'",
    "c') italic", "upright", "italics", None, "high",
    r"L'hypothèse c') appliquée",
    r"L'hypothèse \emph{c')} appliquée")
add(97, "proof of (5.2.1): 'f(y)=0 dans X—U'",
    "long dash for the set difference", "minus sign", "convention", 7, "high",
    r"dans $X-U$",
    r"dans $X\setmin U$",
    "As above.")
add(97, "proof of (5.2.1): 'il en est de même de X_f (I, 1.3.6)'",
    "(I, 1.3.6) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 1.3.6}",
    r"{\textbf{I}, 1.3.6}")
add(97, "proof of (5.2.1): 'donc la réunion des X^f qui sont affines (f∈A)'",
    "X^f (f as a superscript)", "$X_f$", "misprint_in_print", None, "high",
    r"la réunion des $X_f$",
    r"la réunion des $X^f$",
    "The TeX silently corrects the print. Checked on 2x crops: the f is raised, unlike the subscript f of X_f earlier on the same line; the sets meant are the X_f (f∈A) just constructed.",
    corrected=r"X_f")
add(97, "proof of (5.2.1): 'contenant tous les points fermés de X'",
    "'tous les points fermés' italic", "upright", "italics", None, "high",
    r"contenant tous les points fermés de",
    r"contenant \emph{tous les points fermés} de")
add(97, "proof of (5.2.1): 'on a nécessairement Z=X (0, 2.1.3)'",
    "(0, 2.1.3) with bold 0", "plain 0 in the link text", "convention", 2, "high",
    r"{0, 2.1.3}",
    r"{\textbf{0}, 2.1.3}")
add(97, "proof of (5.2.1): 'il y a un nombre fini d'éléments f_i∈A'",
    "'fini' italic", "upright", "italics", None, "high",
    r"un nombre fini d'éléments",
    r"un nombre \emph{fini} d'éléments")
add(97, "proof of (5.2.1): 'défini par les sections f_i (0, 5.1.1)'",
    "(0, 5.1.1) with bold 0", "plain 0 in the link text", "convention", 2, "high",
    r"{0, 5.1.1}",
    r"{\textbf{0}, 5.1.1}")
add(97, "proof of (5.2.1): 'cet homomorphisme est surjectif'",
    "'surjectif' italic", "upright", "italics", None, "high",
    r"cet homomorphisme est¶surjectif",
    r"cet homomorphisme est¶\emph{surjectif}")
add(97, "proof of (5.2.1), last line: 'où ℛ est un sous-𝒪_X-Module quasi-cohérent de 𝒪_X.'",
    "𝒪_X (no exponent n)", "$\\mathcal{O}_X^n$", "misprint_in_print", None, "high",
    r"quasi-cohérent de $\mathcal{O}_X^n$.",
    r"quasi-cohérent de $\mathcal{O}_X$.",
    "The TeX silently corrects the print. Checked on a crop. ℛ is the kernel of 𝒪_X^n→𝒪_X in the exact sequence just written, a sub-Module of 𝒪_X^n.",
    corrected=r"\mathcal{O}_X^n")
add(97, "end of the page: '... Il résulte alors' / p. 98 'de c') que l'homomorphisme ...'",
    "the sentence continues on p. 98; the first line of p. 98 is not indented",
    "blank line after 'résulte alors' before \\oldpage[II]{98} (and another after the marker): a paragraph break",
    "other", None, "high",
    r"Il¶résulte alors¶¶",
    r"Il¶résulte alors¶",
    "Spurious paragraph break at the page boundary; apply together with the p. 98 finding that removes the blank line after \\oldpage[II]{98}.")

# ---------------------------------------------------------------- page 98
add(98, "top of the page: 'de c') que l'homomorphisme correspondant'",
    "continues the sentence of p. 97; first line not indented", "blank line after \\oldpage[II]{98}: a new paragraph",
    "other", None, "high",
    r"\oldpage[II]{98}¶¶de ",
    r"\oldpage[II]{98}¶de ",
    "Spurious paragraph break; apply together with the p. 97 finding that removes the blank line before the marker. Independent of the italic c') edit on the same line.")
add(98, "first line: 'de c') que l'homomorphisme correspondant'",
    "c') italic", "upright", "italics", None, "high",
    r"de c') que l'homomorphisme",
    r"de \emph{c')} que l'homomorphisme",
    "Checked on a crop.")
add(98, "first paragraph: 'ce qui démontre b).'",
    "b) italic", "upright", "italics", None, "high",
    r"démontre b).",
    r"démontre \emph{b)}.")
add(98, "'Enfin, a) implique d) (I, 5.1.9.2)'",
    "a) and d) italic", "upright", "italics", None, "high",
    r"Enfin, a) implique d) (",
    r"Enfin, \emph{a)} implique \emph{d)} (")
add(98, "'Enfin, a) implique d) (I, 5.1.9.2)'",
    "(I, 5.1.9.2) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 5.1.9.2}",
    r"{\textbf{I}, 5.1.9.2}")
add(98, "'et d) implique trivialement d'). Reste à montrer que d') entraîne c').'",
    "d), d'), d'), c') italic", "upright", "italics", None, "high",
    r"et d) implique¶trivialement d'). Reste à montrer que d') entraîne c').",
    r"et \emph{d)} implique¶trivialement \emph{d')}. Reste à montrer que \emph{d')} entraîne \emph{c')}.")
add(98, "'la filtration 0⊂𝒪_X⊂𝒪_X^2⊂...⊂𝒪_X^n'",
    "baseline dots", "\\cdots", "symbol", None, "high",
    r"\subset\cdots\subset",
    r"\subset\ldots\subset",
    "Checked on a crop.")
add(98, "'une filtration formée des ℱ'_k=ℱ∩𝒪_X^k (0⩽k⩽n)'",
    "ℱ'_k = ℱ∩𝒪_X^k: second ℱ without prime, ℱ written before 𝒪_X^k",
    "\\mathcal{F}'_k=\\mathcal{O}_X^k\\cap\\mathcal{F}' (prime added, factors in the other order)",
    "misprint_in_print", None, "high",
    r"\mathcal{F}'_k=\mathcal{O}_X^k\cap\mathcal{F}'$",
    r"\mathcal{F}'_k=\mathcal{F}\cap\mathcal{O}_X^k$",
    "The TeX silently corrects the print (missing prime) and also reverses the order of the intersection, which is a transcription difference for both editions. Checked on a 2.5x crop: the first ℱ carries a prime, the second none. The filtration is of the sub-Module ℱ' of 𝒪_X^n. Corrected edition: \\mathcal{F}'_k=\\mathcal{F}'\\cap\\mathcal{O}_X^k.",
    corrected=r"\mathcal{F}'_k=\mathcal{F}'\cap\mathcal{O}_X^k")
add(98, "'qui sont des 𝒪_X-Modules quasi-cohérents (I, 4.1.1)'",
    "(I, 4.1.1) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 4.1.1}",
    r"{\textbf{I}, 4.1.1}")
add(98, "'L'hypothèse d') entraîne donc H^1(X, ℱ'_{k+1}/ℱ'_k)=0'",
    "d') italic", "upright", "italics", None, "high",
    r"L'hypothèse d')",
    r"L'hypothèse \emph{d')}")
add(98, "Remarque (5.2.1.1): 'Lorsque X est un préschéma noethérien'",
    "'noethérien' italic in the roman remark", "no \\emph", "italics", None, "high",
    r"un préschéma noethérien, on peut dans",
    r"un préschéma \emph{noethérien}, on peut dans",
    "Checked on a crop; judged with the remark body roman.")
add(98, "Remarque (5.2.1.1): 'dans l'énoncé de c') et de d')'",
    "c') and d') italic", "no \\emph", "italics", None, "high",
    r"l'énoncé de c') et de¶d'),",
    r"l'énoncé de \emph{c')} et de¶\emph{d')},")
add(98, "Remarque (5.2.1.1): 'du fait que c') entraîne b)'",
    "c') and b) italic", "no \\emph", "italics", None, "high",
    r"du fait que c') entraîne b),",
    r"du fait que \emph{c')} entraîne \emph{b)},")
add(98, "Remarque (5.2.1.1): 'sont alors des faisceaux cohérents d'idéaux'",
    "'cohérents' italic", "no \\emph", "italics", None, "high",
    r"des faisceaux cohérents d'idéaux",
    r"des faisceaux \emph{cohérents} d'idéaux",
    "Checked on a crop.")
add(98, "Remarque (5.2.1.1): 'est cohérent (I, 6.1.1)'",
    "(I, 6.1.1) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 6.1.1}",
    r"{\textbf{I}, 6.1.1}")
add(98, "proof of (5.2.2): 'la propriété b) n'est autre que (I, 1.6.4)'",
    "b) italic", "upright", "italics", None, "high",
    r"la propriété b) n'est autre que",
    r"la propriété \emph{b)} n'est autre que")
add(98, "proof of (5.2.2): 'n'est autre que (I, 1.6.4)'",
    "(I, 1.6.4) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 1.6.4}",
    r"{\textbf{I}, 1.6.4}")
add(98, "proof of (5.2.2): 'montrons que b) implique a) :'",
    "b) and a) italic", "upright", "italics", None, "high",
    r"montrons que b) implique¶a)~:",
    r"montrons que \emph{b)} implique¶\emph{a)}~:")
add(98, "proof of (5.2.2): 'f_*(ℱ) est un 𝒪_Y-Module quasi-cohérent (I, 9.2.2, a))'",
    "(I, 9.2.2, a)) with bold I", "plain I in the link text", "convention", 2, "high",
    r"Module quasi-cohérent¶(\hyperref[I.9.2.2-fr]{I, 9.2.2",
    r"Module quasi-cohérent¶(\hyperref[I.9.2.2-fr]{\textbf{I}, 9.2.2",
    "First of two (I, 9.2.2, a)) on the page. Independent of the italic 'a)' finding at the same reference (either order works).")
add(98, "proof of (5.2.2): 'f_*(ℱ) est un 𝒪_Y-Module quasi-cohérent (I, 9.2.2, a))'",
    "a) italic", "upright in the link text", "italics", None, "high",
    r"9.2.2, a)}). Par",
    r"9.2.2, \emph{a)}}). Par",
    "Independent of the bold-I finding at the same reference (either order works).")
add(98, "proof of (5.2.2): 'puisque Y est affine (I, 1.3.11)'",
    "(I, 1.3.11) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 1.3.11}",
    r"{\textbf{I}, 1.3.11}")
add(98, "proof of (5.2.2): 'en vertu de (5.2.1, c))'",
    "c) italic", "upright in the link text", "italics", None, "high",
    r"{5.2.1, c)}",
    r"{5.2.1, \emph{c)}}")
add(98, "proof of (5.2.2): 'H^1(f^{-1}(U), ℱ)=0 (5.2.1, d))'",
    "d) italic", "upright in the link text", "italics", None, "high",
    r"{5.2.1, d)}",
    r"{5.2.1, \emph{d)}}")
add(98, "proof of (5.2.2): 'Supposons enfin vérifiée la condition c');'",
    "c') italic", "upright", "italics", None, "high",
    r"la condition¶c')~;",
    r"la condition¶\emph{c')}~;")
add(98, "proof of (5.2.2): paragraph after the display, 'Comme Y est affine et f_*(𝒥) quasi-cohérent'",
    "'Comme' is indented: a new paragraph after the display", "no blank line after \\]: the text continues the paragraph unindented",
    "other", None, "high",
    "\\]\u00b6Comme $Y$",
    "\\]\u00b6\u00b6Comme $Y$",
    "Checked on a crop: 'Comme' starts at the paragraph indent, the next lines at the margin. The p. 99 and p. 96 displays are followed by unindented continuations and need no change.")
add(98, "proof of (5.2.2): 'f_*(𝒥) quasi-cohérent (I, 9.2.2, a))'",
    "(I, 9.2.2, a)) with bold I", "plain I in the link text", "convention", 2, "high",
    r"\mathcal{J})$ quasi-cohérent¶(\hyperref[I.9.2.2-fr]{I, 9.2.2",
    r"\mathcal{J})$ quasi-cohérent¶(\hyperref[I.9.2.2-fr]{\textbf{I}, 9.2.2",
    "Second (I, 9.2.2, a)) on the page. Independent of the italic 'a)' finding at the same reference (either order works).")
add(98, "proof of (5.2.2): 'f_*(𝒥) quasi-cohérent (I, 9.2.2, a)), on a'",
    "a) italic", "upright in the link text", "italics", None, "high",
    r"9.2.2, a)}), on a",
    r"9.2.2, \emph{a)}}), on a",
    "Independent of the bold-I finding at the same reference (either order works).")
add(98, "proof of (5.2.2): 'l'hypothèse c') entraîne donc H^1(X, 𝒥)=0'",
    "c') italic", "upright", "italics", None, "high",
    r"l'hypothèse c') entraîne donc",
    r"l'hypothèse \emph{c')} entraîne donc")

# ---------------------------------------------------------------- page 99
add(99, "Définition (5.3.1): 'est quasi-projectif, ou que X'",
    "the defined term is italic like the rest of the definition", "\\emph inside the italic environment (comes out upright)",
    "convention", 6, "high",
    r"est \emph{quasi-projectif}, ou que",
    r"est quasi-projectif, ou que",
    "Checked on a crop: no change of face in the definition; drop the \\emph.")
add(99, "Définition (5.3.1): 'est quasi-projectif sur Y'",
    "italic like the rest of the definition", "\\emph (upright)", "convention", 6, "high",
    r"\emph{quasi-projectif¶sur $Y$}",
    r"quasi-projectif¶sur $Y$",
    "As above.")
add(99, "Définition (5.3.1): 'ou que X est un Y-schéma quasi-projectif'",
    "italic like the rest of the definition", "\\emph (upright)", "convention", 6, "high",
    r"\emph{$Y$-schéma quasi-projectif}",
    r"$Y$-schéma quasi-projectif",
    "As above.")
add(99, "after (5.3.1): 'On notera que cette notion n'est pas locale sur Y'",
    "'n'est pas locale sur' italic", "upright", "italics", None, "high",
    r"cette notion n'est pas locale sur $Y$",
    r"cette notion \emph{n'est pas locale sur} $Y$",
    "Checked on a crop.")
add(99, "after (5.3.1): 'est nécessairement séparé (4.6.1)'",
    "'séparé' italic", "upright", "italics", None, "high",
    r"nécessairement séparé",
    r"nécessairement \emph{séparé}",
    "Checked on a crop.")
add(99, "after (5.3.1): 'un 𝒪_X-Module très ample relativement à f'",
    "'très ample' italic", "upright", "italics", None, "high",
    r"Module très ample relativement",
    r"Module \emph{très ample} relativement",
    "Checked on a crop.")
add(99, "Proposition (5.3.2), c): 'soit de type fini et engendre 𝒮, et que X soit'",
    "comma after 𝒮", "no comma", "punctuation", None, "high",
    r"engendre $\mathcal{S}$ et que",
    r"engendre $\mathcal{S}$, et que",
    "Checked on a crop.")
add(99, "after (5.3.2): 'lorsque Y est un préschéma noethérien, on peut'",
    "'noethérien' italic", "upright", "italics", None, "high",
    r"un préschéma noethérien, on peut,",
    r"un préschéma \emph{noethérien}, on peut,",
    "Checked on a crop.")
add(99, "after (5.3.2): 'dans les conditions b) et c) de (5.3.2)'",
    "b) and c) italic", "upright", "italics", None, "high",
    r"conditions b) et c) de",
    r"conditions \emph{b)} et \emph{c)} de")
add(99, "after (5.3.2): 'automatiquement vérifiée (I, 6.3.5)'",
    "(I, 6.3.5) with bold I", "plain I in the link text", "convention", 2, "high",
    r"{I, 6.3.5}",
    r"{\textbf{I}, 6.3.5}")
add(99, "Corollaire (5.3.3): 'un 𝒪_Y-Module ample ℒ (4.5.3). Pour qu'un'",
    "(4.5.3) upright inside the italic statement", "italic", "convention", 6, "high",
    r"(\hyperref[II.4.5.3-fr]{4.5.3})",
    r"\textup{(\hyperref[II.4.5.3-fr]{4.5.3})}",
    "Checked on a crop.")


def main():
    texts = {}
    bad = 0
    for rec in F:
        p = rec["page"]
        if p not in texts:
            with open(os.path.join(RUN, "page_%03d.tex" % p), "rb") as fh:
                texts[p] = fh.read().decode("utf-8").replace("\r\n", "\n")
        fx = rec["fix"]
        if fx is None:
            continue
        n = texts[p].count(fx["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE (%d) p.%d: %r" % (n, p, fx["old"]))
        if fx["old"] == fx["new"]:
            bad += 1
            print("NO-OP p.%d: %r" % (p, fx["old"]))
    counts = {}
    for rec in F:
        c = counts.setdefault(rec["page"], [0, 0, 0])
        if rec["kind"] == "convention":
            c[1] += 1
        elif rec["kind"] == "misprint_in_print":
            c[2] += 1
        else:
            c[0] += 1
    for p in sorted(counts):
        print("p.%d: %d/%d/%d" % ((p,) + tuple(counts[p])))
    print("total", len(F), "bad", bad)
    if bad and "--force" not in sys.argv:
        sys.exit(1)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
