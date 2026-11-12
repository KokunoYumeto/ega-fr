"""Findings for pages 117-118 (EGA III part 1), written as Python data and dumped to JSON.

Kept as a helper so the final findings file can be assembled from per-page parts.
"""
import json
import sys

F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


BK = "Bold italic K' in the print (the exact subset K' of (3.1.2)); the TeX writes plain $K'$ throughout section 3.1-3.2."

# ---------------- page 117 ----------------
add(117, "1st paragraph: 'supposons par exemple que F' et F'' appartiennent à K''",
    "K' in bold italic", "$K'$", "font", None, "high",
    {"old": "appartiennent à $K'$~;", "new": "appartiennent à $\\boldsymbol{K}'$~;"}, BK)
add(117, "1st paragraph: 'du terme médian R^qf_*(F) par (0_I, 5.3.4 et 5.3.3)'",
    "(0_I, 5.3.4 et 5.3.3) with a bold 0", "(0\\textsubscript{I}, 5.3.4 et 5.3.3)", "convention", 2, "high",
    {"old": "(0\\textsubscript{I}, 5.3.4 et 5.3.3)", "new": "(\\textbf{0}\\textsubscript{I}, 5.3.4 et 5.3.3)"},
    "Bold 0 in the reference to chapter 0.")
add(117, "1st paragraph: '(resp. F et F'') sont dans K', il en est de même'",
    "K' in bold italic", "$K'$", "font", None, "high",
    {"old": "sont dans $K'$", "new": "sont dans $\\boldsymbol{K}'$"}, BK)
add(117, "1st paragraph: 'd'un O_X-Module F∈K' appartient aussi à K''",
    "F∈K' with K' in bold italic", "$\\mathcal F\\in K'$", "font", None, "high",
    {"old": "\\mathcal F\\in K'$", "new": "\\mathcal F\\in\\boldsymbol{K}'$"}, BK)
add(117, "1st paragraph: 'appartient aussi à K' : en effet'",
    "K' in bold italic", "$K'$", "font", None, "high",
    {"old": "aussi à $K'$~:", "new": "aussi à $\\boldsymbol{K}'$~:"}, BK)
add(117, "1st paragraph: 'il existe un O_X-Module cohérent F appartenant à K''",
    "'un' in italics (il existe *un* O_X-Module)", "il existe un (upright)", "italics", None, "high",
    {"old": "il existe un $\\mathcal O_X$-Module", "new": "il existe \\emph{un} $\\mathcal O_X$-Module"},
    "Enlarged crop: 'un' is italic in the print.")
add(117, "1st paragraph: 'appartenant à K', tel que F_x≠0'",
    "K' in bold italic", "$K'$", "font", None, "high",
    {"old": "$K'$, tel que", "new": "$\\boldsymbol{K}'$, tel que"}, BK)
add(117, "1st paragraph: 'f∘j est propre (II, 5.4.2)'",
    "(II, 5.4.2) with bold II", "(II, 5.4.2)", "convention", 2, "high",
    {"old": "(II, 5.4.2)", "new": "(\\textbf{II}, 5.4.2)"}, "Bold II in the reference to chapter II.")
add(117, "2nd paragraph: 'en vertu du lemme de Chow (II, 5.6.2)'",
    "(II, 5.6.2) with bold II", "(II, 5.6.2)", "convention", 2, "high",
    {"old": "(II, 5.6.2)", "new": "(\\textbf{II}, 5.6.2)"}, "Bold II in the reference to chapter II.")
add(117, "2nd paragraph: 'L ample pour g (II, 5.3.1)'",
    "(II, 5.3.1) with bold II", "(II, 5.3.1)", "convention", 2, "high",
    {"old": "(II, 5.3.1)", "new": "(\\textbf{II}, 5.3.1)"}, "Bold II in the reference to chapter II.")
add(117, "2nd paragraph: 'on a F_x≠0 (II, 3.4.7)'",
    "(II, 3.4.7) with bold II", "(II, 3.4.7)", "convention", 2, "high",
    {"old": "(II, 3.4.7)", "new": "(\\textbf{II}, 3.4.7)"}, "Bold II in the reference to chapter II.")
add(117, "2nd paragraph: 'dont le terme E_2 est donné par E_2^{pq}=R^pf_*(R^qg_*(O_{X'}(n));'",
    "E_2^{pq}=R^pf_*(R^qg_*(O_{X'}(n)); : three opening parentheses, only two closing ones",
    "E_2^{pq}=R^pf_*(R^qg_*(\\mathcal O_{X'}(n)))~; (silently corrected)", "misprint_in_print", None, "high",
    {"old": "R^qg_*(\\mathcal O_{X'}(n)))~;", "new": "R^qg_*(\\mathcal O_{X'}(n))~;"},
    "Enlarged crop (2x): the print closes only two of the three parentheses. The TeX silently adds the third; the fix restores the printed reading.",
    corrected="E_2^{pq}=R^pf_*(R^qg_*(\\mathcal O_{X'}(n)))")
add(117, "2nd paragraph: 'et on sait alors (0, 11.1.6) que'",
    "(0, 11.1.6) with a bold 0", "(0, 11.1.6)", "convention", 2, "high",
    {"old": "(0, 11.1.6)", "new": "(\\textbf{0}, 11.1.6)"}, "Bold 0 in the reference to chapter 0.")
add(117, "2nd paragraph, end: 'est isomorphe à R^p(f∘g)_*(O_{X'}(n))), ce qui achève la démonstration'",
    "R^p(f∘g)_*(O_{X'}(n))) : one closing parenthesis too many",
    "R^p(f\\circ g)_*(\\mathcal O_{X'}(n)) (silently corrected)", "misprint_in_print", None, "high",
    {"old": "(\\mathcal O_{X'}(n))$, ce qui", "new": "(\\mathcal O_{X'}(n)))$, ce qui"},
    "Enlarged crop (2x): three closing parentheses after n where two are needed. The TeX silently drops the extra one; the fix restores the printed reading.",
    corrected="R^p(f\\circ g)_*(\\mathcal O_{X'}(n))")
add(117, "Corollaire (3.2.4): 'dont le support est propre sur Y (II, 5.4.10)'",
    "(II, 5.4.10) with bold II", "(II, 5.4.10)", "convention", 2, "high",
    {"old": "(II, 5.4.10)", "new": "(\\textbf{II}, 5.4.10)"}, "Bold II in the reference to chapter II.")

# ---------------- page 118 ----------------
add(118, "Proof of (3.2.4): 'et il en est donc de même de X (I, 6.3.7)'",
    "(I, 6.3.7) with bold I", "(I, 6.3.7)", "convention", 2, "high",
    {"old": "(I, 6.3.7)", "new": "(\\textbf{I}, 6.3.7)"}, "Bold I in the reference to chapter I.")
add(118, "Proof of (3.2.4): 'autrement dit, si j : Y→X est l'injection canonique, f∘j : Z→Y est propre'",
    "j : Y→X (Y where the closed subprescheme Z is meant)", "$j:Z\\to X$ (silently corrected)",
    "misprint_in_print", None, "high",
    {"old": "si $j:Z\\to X$", "new": "si $j:Y\\to X$"},
    "Enlarged crop: the print has Y→X; the injection of the closed subprescheme Z is meant (the next formula is f∘j : Z→Y). The TeX silently corrects it; the fix restores the printed reading.",
    corrected="j:Z\\to X")
add(118, "Proof of (3.2.4): 'est un O_Z-Module cohérent (I, 9.3.5)'",
    "(I, 9.3.5) with bold I", "(I, 9.3.5)", "convention", 2, "high",
    {"old": "(I, 9.3.5)", "new": "(\\textbf{I}, 9.3.5)"}, "Bold I in the reference to chapter I.")
add(118, "Proof of (3.3.1): 'f' est propre (II, 5.4.2, (iii))'",
    "(II, 5.4.2, (iii)) with bold II", "(II, 5.4.2, (iii))", "convention", 2, "high",
    {"old": "(II, 5.4.2, (iii))", "new": "(\\textbf{II}, 5.4.2, (iii))"}, "Bold II in the reference to chapter II.")
add(118, "Proof of (3.3.1), 2nd paragraph: 'pour tout k≥k_{p,i} (II, 2.1.6, (ii))'",
    "(II, 2.1.6, (ii)) with bold II (the second I is a damaged sort, but reads II)", "(II, 2.1.6, (ii))",
    "convention", 2, "high",
    {"old": "(II, 2.1.6, (ii))", "new": "(\\textbf{II}, 2.1.6, (ii))"},
    "Bold II in the reference to chapter II. Enlarged crop: the second bold I is broken at the foot; no textual difference.")
add(118, "Corollaire (3.3.2): equation tag of 'H^p(X, m^{k+r}F)=m^rH^p(X, m^kF)'",
    "tag (3.3.3.1) inside Corollaire (3.3.2)", "\\tag{3.3.3.1} (printed reading kept; label III.3.3.2.1-fr)",
    "misprint_in_print", None, "high", None,
    "Enlarged crop: the print numbers the formula (3.3.3.1) although it belongs to (3.3.2). The TeX keeps the printed tag; no reference to it found in ega3-1-fr.tex.",
    corrected="\\tag{3.3.2.1}")
add(118, "Proof of (3.3.2): 'Il suffit d'appliquer (3.3.2) avec Y=Spec(A)'",
    "(3.3.2): the corollary refers to itself", "(\\hyperref[III.3.3.2-fr]{3.3.2}) (printed reading kept)",
    "misprint_in_print", None, "high", None,
    "Enlarged crop: the print has (3.3.2); the proposition (3.3.1) is what is applied. The TeX keeps the printed reading.",
    corrected="(\\hyperref[III.3.3.1-fr]{3.3.1})")
add(118, "Proof of (3.3.2): 'avec Y=Spec(A), S=S~, M_k=m^kF'",
    "script S with a tilde on the right: 𝒮 = 𝒮̃", "$\\mathcal S=\\widetilde S$ (silently corrected)",
    "misprint_in_print", None, "high",
    {"old": "$\\mathcal S=\\widetilde S$", "new": "$\\mathcal S=\\widetilde{\\mathcal S}$"},
    "Enlarged crop (3x): the letter under the tilde is the script S, the same glyph as on the left. The ring S = ⊕ m^k of the statement is meant. The TeX silently corrects it; the fix restores the printed reading.",
    corrected="\\mathcal S=\\widetilde S")

# ---------------- page 119 ----------------
B2 = "Bold II in the reference to chapter II."
B1 = "Bold I in the reference to chapter I."
add(119, "(3.4.1), 1st paragraph: 'localement noethériens (I, 10.4.2)'",
    "(I, 10.4.2) with bold I", "(I, 10.4.2)", "convention", 2, "high",
    {"old": "(I, 10.4.2)", "new": "(\\textbf{I}, 10.4.2)"}, B1)
add(119, "(3.4.1), condition 1°: 'f est un morphisme de type fini'",
    "condition 1° set in italics (the reference (I, 10.13.3) upright)", "upright text in the env paragraph",
    "italics", None, "high",
    {"old": "\\item[$1^\\circ$] $f$ est un morphisme de type fini",
     "new": "\\item[$1^\\circ$] \\emph{$f$ est un morphisme de type fini}"},
    "Enlarged crop: the text of conditions 1° and 2° is italic in the print; the env environment is upright.")
add(119, "(3.4.1), condition 1°: '(I, 10.13.3).'",
    "(I, 10.13.3) with bold I", "(I, 10.13.3).", "convention", 2, "high",
    {"old": "(I, 10.13.3).", "new": "(\\textbf{I}, 10.13.3)."}, B1)
add(119, "(3.4.1), condition 2°: 'Si K est un Idéal de définition de S et si l'on pose'",
    "set in italics", "upright", "italics", None, "high",
    {"old": "\\item[$2^\\circ$] Si $\\mathcal K$ est un Idéal de définition de $\\mathfrak S$\net si l'on pose",
     "new": "\\item[$2^\\circ$] \\emph{Si $\\mathcal K$ est un Idéal de définition de $\\mathfrak S$\net si l'on pose}"},
    "Enlarged crop: condition 2° is italic in the print. Its last words 'est propre' are set italic by the convention-2 fix on (I, 10.5.6) of the same line.")
add(119, "(3.4.1), condition 2°: 'le morphisme f_0 : X_0→Y_0 déduit de f'",
    "'le morphisme' and 'déduit de' in italics", "upright", "italics", None, "high",
    {"old": "le morphisme\n$f_0:X_0\\to Y_0$ déduit de",
     "new": "\\emph{le morphisme}\n$f_0:X_0\\to Y_0$ \\emph{déduit de}"},
    "Enlarged crop: italic in the print (condition 2°).")
add(119, "(3.4.1), condition 2°: 'le morphisme f_0 : X_0→Y_0 déduit de f'",
    "f_0 : X_0→Y_0 (Y_0 where S_0 is meant)", "$f_0:X_0\\to Y_0$ (printed reading kept)",
    "misprint_in_print", None, "high", None,
    "Enlarged crop: the print has Y_0; the morphism goes to S_0=(S, O_S/K) defined just before. The TeX keeps the printed reading.",
    corrected="f_0:X_0\\to S_0")
add(119, "(3.4.1), condition 2°: 'déduit de f (I, 10.5.6) est propre.'",
    "(I, 10.5.6) with bold I; 'est propre' italic", "(I, 10.5.6) est propre.", "convention", 2, "high",
    {"old": "(I, 10.5.6) est propre.", "new": "(\\textbf{I}, 10.5.6) \\emph{est propre}."},
    "Bold I in the reference to chapter I. The fix also sets the following 'est propre' in italics (end of the italic condition 2°), so that no two fixes on this line overlap.")
add(119, "(3.4.1), 2nd paragraph: 'en vertu de (II, 5.4.5)'",
    "(II, 5.4.5) with bold II", "(II, 5.4.5)", "convention", 2, "high",
    {"old": "vertu de (II, 5.4.5)", "new": "vertu de (\\textbf{II}, 5.4.5)"}, B2)
add(119, "(3.4.1), 3rd paragraph: 'le morphisme f_n : X_n→Y_n déduit de f'",
    "f_n : X_n→Y_n (Y_n where S_n is meant)", "$f_n:X_n\\to Y_n$ (printed reading kept)",
    "misprint_in_print", None, "high", None,
    "Enlarged crop: the print has Y_n; the morphism goes to S_n=(S, O_S/K^{n+1}) defined just before. The TeX keeps the printed reading.",
    corrected="f_n:X_n\\to S_n")
add(119, "(3.4.1), 3rd paragraph: 'déduit de f (I, 10.5.6) est propre pour tout n'",
    "(I, 10.5.6) with bold I", "(I, 10.5.6)", "convention", 2, "high",
    {"old": "(I, 10.5.6) est propre pour", "new": "(\\textbf{I}, 10.5.6) est propre pour"}, B1)
add(119, "(3.4.1), 3rd paragraph: 'dès qu'il l'est pour n=0 (II, 5.4.6)'",
    "(II, 5.4.6) with bold II", "(II, 5.4.6)", "convention", 2, "high",
    {"old": "(II, 5.4.6)", "new": "(\\textbf{II}, 5.4.6)"}, B2)
add(119, "(3.4.1), 4th paragraph: 'de g aux complétés (I, 10.9.1)'",
    "(I, 10.9.1) with bold I", "(I, 10.9.1)", "convention", 2, "high",
    {"old": "(I, 10.9.1)", "new": "(\\textbf{I}, 10.9.1)"}, B1)
add(119, "(3.4.1), 4th paragraph: 'comme il résulte de la définition et de (II, 5.4.5)'",
    "(II, 5.4.5) with bold II", "(II, 5.4.5)", "convention", 2, "high",
    {"old": "et\nde (II, 5.4.5)", "new": "et\nde (\\textbf{II}, 5.4.5)"}, B2)
add(119, "(3.4.1), last paragraph: 'un morphisme de type fini (I, 10.13.3); les notations'",
    "(I, 10.13.3) with bold I", "(I, 10.13.3)~;", "convention", 2, "high",
    {"old": "(I, 10.13.3)~;", "new": "(\\textbf{I}, 10.13.3)~;"}, B1)
add(119, "(3.4.1), last paragraph: 'est propre sur S (ou propre pour f)'",
    "only 'propre' in italics; 'sur' upright", "\\emph{propre sur}", "italics", None, "high",
    {"old": "\\emph{propre sur}", "new": "\\emph{propre} sur"},
    "Enlarged crop: 'sur' is roman here (unlike the later 'propre sur S_0', where both words are italic).")
add(119, "(3.4.1), last paragraph: 'Z est propre sur S_0 (II, 5.4.10)'",
    "(II, 5.4.10) with bold II", "(II, 5.4.10)", "convention", 2, "high",
    {"old": "(II, 5.4.10). Toutes", "new": "(\\textbf{II}, 5.4.10). Toutes"}, B2)
add(119, "(3.4.1), last paragraph: 'énoncées dans (II, 5.4.10)'",
    "(II, 5.4.10) with bold II", "(II, 5.4.10)", "convention", 2, "high",
    {"old": "dans (II, 5.4.10)", "new": "dans (\\textbf{II}, 5.4.10)"}, B2)

# ---------------- page 120 ----------------
add(120, "Page start: 'F = lim F_k (I, 10.11.3). D'autre part'",
    "no word 'par' before (I, 10.11.3)", "\\]\npar (I, 10.11.3)", "extra", None, "high",
    {"old": "\\]\npar ", "new": "\\]\n"},
    "Enlarged crop: the print reads 'tel que F = lim F_k (I, 10.11.3).' with the formula inline; 'par' is not in the print.")
add(120, "Page start: 'F = lim F_k (I, 10.11.3)'",
    "(I, 10.11.3) with bold I", "(I, 10.11.3)", "convention", 2, "high",
    {"old": "(I, 10.11.3). D'autre", "new": "(\\textbf{I}, 10.11.3). D'autre"}, B1)
add(120, "1st paragraph: 'structure de O_Y-Module topologique (I, 10.11.6)'",
    "(I, 10.11.6) with bold I", "(I, 10.11.6)", "convention", 2, "high",
    {"old": "topologique (I, 10.11.6)", "new": "topologique (\\textbf{I}, 10.11.6)"}, B1)
add(120, "1st paragraph: 'topologique précédentes (I, 10.11.6)'",
    "(I, 10.11.6) with bold I", "(I, 10.11.6)", "convention", 2, "high",
    {"old": "précédentes (I, 10.11.6)", "new": "précédentes (\\textbf{I}, 10.11.6)"}, B1)
add(120, "Corollaire (3.4.3): 'satisfait à la condition (ML)'",
    "(ML) upright in the italic statement", "condition (ML) (italic in the corollary environment)",
    "convention", 6, "high",
    {"old": "condition (ML) (", "new": "condition \\textup{(ML)} ("},
    "Enlarged crop: (ML) is roman in the print.")
add(120, "Corollaire (3.4.3): 'la condition (ML) (0, 13.1.1)'",
    "(0, 13.1.1) with a bold 0", "(0, 13.1.1)", "convention", 2, "high",
    {"old": "0, 13.1.1)", "new": "\\textbf{0}, 13.1.1)"}, "Bold 0 in the reference to chapter 0.")
add(120, "Before Corollaire (3.4.4): 'lorsque Y est un schéma affine formel noethérien'",
    "roman Y (the formal prescheme of (3.4.2) is the Fraktur Y)", "$Y$ (printed reading kept)",
    "misprint_in_print", None, "medium", None,
    "Enlarged crop: the print has a roman Y, not the Fraktur Y of (3.4.2)-(3.4.4) (Y = Spf(A) in (3.4.4)). The TeX keeps the printed letter.",
    corrected="lorsque $\\mathfrak Y$ est")
add(120, "Before Corollaire (3.4.4): 'formel noethérien (I, 10.4.1) :'",
    "(I, 10.4.1) with bold I", "(I, 10.4.1)", "convention", 2, "high",
    {"old": "(I, 10.4.1)", "new": "(\\textbf{I}, 10.4.1)"}, B1)
add(120, "Corollaire (3.4.4): 'satisfait à la condition (ML) pour tout n'",
    "(ML) upright in the italic statement", "condition (ML) (italic in the corollary environment)",
    "convention", 6, "high",
    {"old": "condition (ML) pour", "new": "condition \\textup{(ML)} pour"},
    "(ML) is roman in the print.")
add(120, "Corollaire (3.4.4): 'les N_{k,n} définissent sur H^n(X, F) une filtration'",
    "N_{k,n} (indices in the order k, n; the definition (3.4.4.1) has N_{n,k})", "$N_{k,n}$ (printed reading kept)",
    "misprint_in_print", None, "high", None,
    "Enlarged crop (2.5x): the print has N_{k,n}. The TeX keeps the printed reading.",
    corrected="N_{n,k}")
add(120, "Corollaire (3.4.4): 'une filtration J-bonne (0, 13.7.7)'",
    "(0, 13.7.7) with a bold 0", "(0, 13.7.7)", "convention", 2, "high",
    {"old": "(0, 13.7.7)", "new": "(\\textbf{0}, 13.7.7)"}, "Bold 0 in the reference to chapter 0.")
add(120, "After (3.4.4.3): 'est un Idéal de définition de Y (I, 10.3.1)'",
    "(I, 10.3.1) with bold I", "(I, 10.3.1)", "convention", 2, "high",
    {"old": "(I, 10.3.1)", "new": "(\\textbf{I}, 10.3.1)"}, B1)
add(120, "After (3.4.4.3): 'sont des O_{X_0}-Modules cohérents (I, 10.11.3)'",
    "(I, 10.11.3) with bold I", "(I, 10.11.3)", "convention", 2, "high",
    {"old": "(I, 10.11.3). Considérons", "new": "(\\textbf{I}, 10.11.3). Considérons"}, B1)

# ---------------- page 121 ----------------
add(121, "1st paragraph: 'N est un B-module de type fini (I, 10.10.5)'",
    "(I, 10.10.5) with bold I", "(I, 10.10.5)", "convention", 2, "high",
    {"old": "(I, 10.10.5)", "new": "(\\textbf{I}, 10.10.5)"}, B1)
add(121, "1st paragraph: 'sont respectivement égaux à S~' et M~''",
    "tilde over S only, prime outside (S̃′)", "\\widetilde{S'}", "convention", 8, "high",
    {"old": "\\widetilde{S'}", "new": "\\widetilde{S}'"},
    "Enlarged crop (2x): the tilde covers S; the prime stands after it.")
add(121, "1st paragraph: 'sont respectivement égaux à S~' et M~''",
    "tilde over M only, prime outside (M̃′)", "\\widetilde{M'}", "convention", 8, "high",
    {"old": "\\widetilde{M'}", "new": "\\widetilde{M}'"},
    "Enlarged crop (2x): the tilde covers M; the prime stands after it.")
add(121, "1st paragraph: 'S' = ⊕((J^k/J^{k+1})⊗_{A_0}B_0) et M' = ⊕(...)'",
    "'... ⊗_{A_0}B_0) et M' = ...' (the word 'et', no comma)", "B_0),\\qquad M' (no 'et', a comma)",
    "missing", None, "high",
    {"old": "B_0),\\qquad", "new": "B_0)\\quad\\text{et}\\quad"},
    "Enlarged crop: the two sums are joined by 'et' with no comma after the first (the print sets them inline; the TeX displays them).")
add(121, "1st paragraph: 'd'où notre assertion (I, 1.3.13)'",
    "(I, 1.3.13) with bold I", "(I, 1.3.13)", "convention", 2, "high",
    {"old": "(I, 1.3.13)", "new": "(\\textbf{I}, 1.3.13)"}, B1)
add(121, "2nd paragraph: 'on peut appliquer (3.3.2) à S, M et au morphisme f_0'",
    "(3.3.2): the graded statement applied to S, M and f_0 is the proposition (3.3.1)",
    "(\\hyperref[III.3.3.2-fr]{3.3.2}) (printed reading kept)", "misprint_in_print", None, "medium", None,
    "The corollary (3.3.2) concerns H^p(X, m^kF) and does not apply to the graded S-Module M; (3.3.1) with (1.4.11) gives the conclusion. Same slip as p. 118, where the proof of (3.3.2) 'applies (3.3.2)' and its formula is tagged (3.3.3.1): consistent with a draft numbering proposition = 3.3.2, corollary = 3.3.3. The TeX keeps the printed reading.",
    corrected="(\\hyperref[III.3.3.1-fr]{3.3.1})")
add(121, "2nd paragraph: 'la condition (F_n) de (0, 13.7.7)'",
    "(0, 13.7.7) with a bold 0", "(0, 13.7.7)", "convention", 2, "high",
    {"old": "de (0, 13.7.7)", "new": "de (\\textbf{0}, 13.7.7)"}, "Bold 0 in the reference to chapter 0.")
add(121, "2nd paragraph: 'On peut donc appliquer (0, 13.7.7), qui prouve que'",
    "(0, 13.7.7) with a bold 0", "(0, 13.7.7)", "convention", 2, "high",
    {"old": "appliquer (0, 13.7.7)", "new": "appliquer (\\textbf{0}, 13.7.7)"}, "Bold 0 in the reference to chapter 0.")
HN = "Enlarged crop: the print has H'^n (prime and n in the exponent, no comma); H'^{,n} typesets a comma between them."
add(121, "Item 2°: 'Si H'^n = lim H^n(X, F_k)'",
    "H'^n (no comma)", "H'^{,n}", "symbol", None, "high",
    {"old": "$H'^{,n}=\\varprojlim_k", "new": "$H'^{n}=\\varprojlim_k"}, HN)
add(121, "Item 2°: 'H'^n est un A-module de type fini'",
    "H'^n (no comma)", "H'^{,n}", "symbol", None, "high",
    {"old": "$H'^{,n}$ est un", "new": "$H'^{n}$ est un"}, HN)
add(121, "Item 3°: 'La filtration définie sur H'^n'",
    "H'^n (no comma)", "H'^{,n}", "symbol", None, "high",
    {"old": "sur $H'^{,n}$ par", "new": "sur $H'^{n}$ par"}, HN)
add(121, "Item 3°: 'homomorphismes canoniques H'^n → H^n(X, F_k)'",
    "H'^n (no comma)", "H'^{,n}", "symbol", None, "high",
    {"old": "$H'^{,n}\\to", "new": "$H'^{n}\\to"}, HN)
add(121, "3rd paragraph: 'F_k est un O_{X_k}-Module cohérent (I, 10.11.3)'",
    "(I, 10.11.3) with bold I", "(I, 10.11.3)", "convention", 2, "high",
    {"old": "(I, 10.11.3)", "new": "(\\textbf{I}, 10.11.3)"}, B1)
add(121, "3rd paragraph: 'dans chacun des X_k (I, 5.1.9)'",
    "(I, 5.1.9) with bold I", "(I, 5.1.9)", "convention", 2, "high",
    {"old": "(I, 5.1.9)", "new": "(\\textbf{I}, 5.1.9)"}, B1)
add(121, "3rd paragraph: 'est surjectif pour h≤k (I, 1.3.9)'",
    "(I, 1.3.9) with bold I", "(I, 1.3.9)", "convention", 2, "high",
    {"old": "(I, 1.3.9)", "new": "(\\textbf{I}, 1.3.9)"}, B1)
add(121, "3rd paragraph: 'dans les conditions de (0, 13.3.2)'",
    "(0, 13.3.2) with a bold 0", "(0, 13.3.2)", "convention", 2, "high",
    {"old": "(0, 13.3.2)", "new": "(\\textbf{0}, 13.3.2)"}, "Bold 0 in the reference to chapter 0.")
add(121, "3rd paragraph: 'l'application de (0, 13.3.1) prouve que'",
    "(0, 13.3.1) with a bold 0", "(0, 13.3.1)", "convention", 2, "high",
    {"old": "(0, 13.3.1)", "new": "(\\textbf{0}, 13.3.1)"}, "Bold 0 in the reference to chapter 0.")
add(121, "3rd paragraph: 'prouve que H'^n s'identifie canoniquement à'",
    "H'^n (no comma)", "H'^{,n}", "symbol", None, "high",
    {"old": "$H'^{,n}$ s'identifie", "new": "$H'^{n}$ s'identifie"}, HN)
add(121, "(3.4.5): 'est un isomorphisme; mais on a (0_I, 3.2.6)'",
    "(0_I, 3.2.6) with a bold 0", "(0\\textsubscript{I}, 3.2.6)", "convention", 2, "high",
    {"old": "(0\\textsubscript{I}, 3.2.6)", "new": "(\\textbf{0}\\textsubscript{I}, 3.2.6)"},
    "Bold 0 in the reference to chapter 0.")

if __name__ == "__main__":
    out = sys.argv[1]
    json.dump(F, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(F), "findings ->", out)
