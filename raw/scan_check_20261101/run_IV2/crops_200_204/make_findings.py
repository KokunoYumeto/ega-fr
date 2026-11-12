import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_200_204.json"
N = "\n"
F = []


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note="", fix_none=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if fix_none else {"old": old, "new": new},
         "note": note}
    F.append(d)


G20 = "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20)."
C7 = "\\setmin pending the convention-7 decision."

# ---------------- page 200 ----------------
add(200, "p. 200, first line: label (ii) of the proof of (7.4.4)", "(ii) upright", r"\item[\emph{(ii)}] (italic: the proof environment is roman)",
    "italics", r"\item[\emph{(ii)}] Soit $B$", r"\item[(ii)] Soit $B$",
    note="Inside the roman proof environment \\emph sets the label italic; the printed (ii) is upright (enlarged crop).")
add(200, "p. 200, (ii), l. 7: 'est fini sur k'", "est *fini* sur k", "est fini sur $k$",
    "italics", "est fini sur $k$", r"est \emph{fini} sur $k$")
add(200, "p. 200, (ii), l. 7: (I, 6.4.2)", "(**I**, 6.4.2)", "(I, 6.4.2)",
    "convention", "(I, 6.4.2)", r"(\textbf{I}, 6.4.2)", conv=2)
add(200, "p. 200, end of (ii), before Lemme (7.4.4.1)",
    "On est ainsi ramené à démontrer le / Lemme (7.4.4.1). — (the sentence runs into the lemma heading)",
    "On est ainsi ramené à démontrer le lemme suivant.",
    "extra", "démontrer le" + N + "lemme suivant.", "démontrer le",
    note="'lemme suivant.' is not printed: the printed sentence ends in 'démontrer le' followed by the heading 'Lemme (7.4.4.1). —'.")
add(200, "p. 200, proof of (7.4.4.1), l. 7: S'=C'—n'", "S'=C'—n' (long dash)", r"$S'=C'-\mathfrak n'$",
    "convention", r"$S'=C'-\mathfrak n'$", r"$S'=C'\setmin\mathfrak n'$", conv=7, note=C7)
add(200, "p. 200, proof of (7.4.4.1), end of 1st paragraph: 'par un seul élément t'", "par *un seul* élément t", r"par un \emph{seul} élément",
    "italics", r"par un \emph{seul}", r"par \emph{un seul}")
add(200, "p. 200, 3rd paragraph of the proof: critère (7.3.16, b))", "(7.3.16, *b)*)", "(7.3.16, b))",
    "italics", "(7.3.16, b))", r"(7.3.16, \emph{b)})")
add(200, "p. 200, 3rd paragraph: S=C—n", "S=C—n (long dash)", r"$S=C-\mathfrak n$",
    "convention", r"$S=C-\mathfrak n$", r"$S=C\setmin\mathfrak n$", conv=7, note=C7)
add(200, "p. 200, last line: 'si n est un idéal maximal de C' (continues on p. 201 'au-dessus de ...')",
    "no paragraph break: p. 201 continues the sentence", "blank line before \\oldpage[IV-2]{201}",
    "other", r"maximal de $C$" + N + N, r"maximal de $C$" + N,
    note=G20 + " Apply together with the p. 201 entry that removes the blank line after \\oldpage[IV-2]{201}.")

# ---------------- page 201 ----------------
add(201, "p. 201, top: blank line after the marker", "au-dessus de l'idéal maximal de A, ... (mid-sentence, no indent)",
    "blank line after \\oldpage[IV-2]{201}",
    "other", r"\oldpage[IV-2]{201}" + N + N + "au-dessus", r"\oldpage[IV-2]{201}" + N + "au-dessus",
    note="Apply together with the p. 200 entry 'maximal de $C$' (blank line before the marker).")
add(201, "p. 201, l. 5, before Lemme (7.4.4.2)", "plus général en apparence :", "plus général en apparence.",
    "punctuation", "plus général en apparence.", "plus général en apparence :")
add(201, "p. 201, 'On notera que ...': extension finie de k", "est une extension *finie* de k", "est une extension finie de $k$",
    "italics", "est une extension finie de $k$", r"est une extension \emph{finie} de $k$")
add(201, "p. 201, 'On notera que ...': (I, 6.4.11 et 6.4.2)", "(**I**, 6.4.11 et 6.4.2)", "(I, 6.4.11 et 6.4.2)",
    "convention", "(I, 6.4.11 et 6.4.2)", r"(\textbf{I}, 6.4.11 et 6.4.2)", conv=2)
add(201, "p. 201, 'Si l'on pose Y=Spec(C)': Reg(Y) est ouvert dans Y", "est *ouvert* dans Y", "est ouvert dans $Y$",
    "italics", "est ouvert dans $Y$", r"est \emph{ouvert} dans $Y$")
add(201, "p. 201, same paragraph: (I, 2.4.2)", "(**I**, 2.4.2)", "(I, 2.4.2)",
    "convention", "(I, 2.4.2)", r"(\textbf{I}, 2.4.2)", conv=2)
add(201, "p. 201, same paragraph: donc U est ouvert dans X", "donc U est *ouvert* dans X", "donc $U$ est ouvert dans $X$",
    "italics", "donc $U$ est ouvert dans $X$", r"donc $U$ est \emph{ouvert} dans $X$")
add(201, "p. 201, same paragraph: S'=X'—U'", "S'=X'—U' (long dash)", "$S'=X'-U'$",
    "convention", "$S'=X'-U'$", r"$S'=X'\setmin U'$", conv=7, note=C7)
add(201, "p. 201, same paragraph: localement fermé", "est *localement fermé* dans X'", "est localement fermé dans $X'$",
    "italics", "est localement fermé dans $X'$", r"est \emph{localement fermé} dans $X'$")
add(201, "p. 201, same paragraph: cet ensemble est vide", "cet ensemble est *vide*.", "cet ensemble est vide.",
    "italics", "cet ensemble est vide.", r"cet ensemble est \emph{vide}.")
add(201, "p. 201, 'En effet, cela signifierait ...': (0, 17.1.5)", "(**0**, 17.1.5)", "(0, 17.1.5)",
    "convention", "(0," + N + "17.1.5)", r"(\textbf{0}," + N + "17.1.5)", conv=2)
add(201, "p. 201: 'n'est pas régulière au point p''", "la fibre Z de f au point p *n'est pas régulière au point* p'",
    "n'est pas régulière au point $\\mathfrak p'$ (roman)",
    "italics", "n'est pas régulière" + N + r"au point $\mathfrak p'$", r"\emph{n'est pas régulière" + N + r"au point} $\mathfrak p'$")
add(201, "p. 201: 'Montrons qu'on peut se ramener au cas où p=0'", "Montrons qu'*on peut se ramener au cas où* p=0",
    "Montrons qu'on peut se ramener au cas où (roman)",
    "italics", "Montrons qu'on peut se ramener au cas où", r"Montrons qu'\emph{on peut se ramener au cas où}")
add(201, "p. 201: l'homomorphisme B→B'/p' est injectif", "est *injectif*.", "est injectif.",
    "italics", r"$B\to B'/\mathfrak p'$ est injectif.", r"$B\to B'/\mathfrak p'$ est \emph{injectif}.")
add(201, "p. 201, case I): label", "I) upright, then 'V *est une* A-*algèbre finie*.'", r"\emph{I) $V$ est une $A$-algèbre finie.} (label italic)",
    "italics", r"\emph{I) $V$ est une", r"I) \emph{$V$ est une",
    note="The proof environment is roman; \\emph makes the label I) italic, the print has it upright (enlarged crop).")
add(201, "p. 201, case II): label", "II) upright, then 'V *n'est pas une* A-*algèbre finie*.'", r"\emph{II) $V$ n'est pas une $A$-algèbre finie.} (label italic)",
    "italics", r"\emph{II) $V$ n'est pas", r"II) \emph{$V$ n'est pas",
    note="As for I): the printed label II) is upright (enlarged crop).")
add(201, "p. 201, case II): A est complet", "l'anneau local A est *complet*", "$A$ est complet",
    "italics", "$A$ est complet, cela implique", r"$A$ est \emph{complet}, cela implique")
add(201, "p. 201, case II): quasi-finie", "une A-algèbre *quasi-finie*", "une $A$-algèbre quasi-finie",
    "italics", "$A$-algèbre" + N + "quasi-finie", "$A$-algèbre" + N + r"\emph{quasi-finie}")
add(201, "p. 201, case II): (0_I, 7.4.1 et 7.4.2)", "(**0**_I, 7.4.1 et 7.4.2)", r"(0$_{\mathrm I}$, 7.4.1 et 7.4.2)",
    "convention", r"(0$_{\mathrm I}$, 7.4.1 et 7.4.2)", r"($\mathbf{0}_{\mathrm I}$, 7.4.1 et 7.4.2)", conv=2)
add(201, "p. 201, last line: extension finie du corps résiduel", "est extension *finie* du corps résiduel k de A,", "est extension finie du corps résiduel",
    "italics", "est extension finie du corps résiduel", r"est extension \emph{finie} du corps résiduel")
add(201, "p. 201, last line: 'du corps résiduel k de A,' (continues on p. 202 'donc (0_I, 7.4.4) ...')",
    "no paragraph break: p. 202 continues the sentence", "blank line before \\oldpage[IV-2]{202}",
    "other", "résiduel $k$ de $A$," + N + N, "résiduel $k$ de $A$," + N,
    note=G20 + " Apply together with the p. 202 entry that removes the blank line after \\oldpage[IV-2]{202}.")

# ---------------- page 202 ----------------
add(202, "p. 202, top: blank line after the marker", "donc (0_I, 7.4.4) l'idéal mV ... (mid-sentence, no indent)",
    "blank line after \\oldpage[IV-2]{202}",
    "other", r"\oldpage[IV-2]{202}" + N + N + "donc", r"\oldpage[IV-2]{202}" + N + "donc",
    note="Apply together with the p. 201 entry 'résiduel $k$ de $A$,' (blank line before the marker).")
add(202, "p. 202, l. 1: (0_I, 7.4.4)", "(**0**_I, 7.4.4)", r"(0$_{\mathrm I}$, 7.4.4)",
    "convention", r"(0$_{\mathrm I}$, 7.4.4)", r"($\mathbf{0}_{\mathrm I}$, 7.4.4)", conv=2)
add(202, "p. 202, l. 1: 'n'est pas un idéal de définition de V'", "l'idéal mV *n'est pas un idéal de définition de* V",
    "n'est pas un idéal de définition de $V$ (roman)",
    "italics", "n'est pas un idéal de" + N + "définition de $V$", r"\emph{n'est pas un idéal de" + N + "définition de} $V$")
add(202, "p. 202, l. 4: A=k est un corps", "A=k est un *corps*.", "$A=k$ est un corps.",
    "italics", "$A=k$ est un corps.", r"$A=k$ est un \emph{corps}.")
add(202, "p. 202, l. 4: dim(C)≤1 (0, 16.1.5)", "(**0**, 16.1.5)", "(0, 16.1.5)",
    "convention", "(0, 16.1.5); mais", r"(\textbf{0}, 16.1.5); mais", conv=2)
add(202, "p. 202, l. 5: les relations dim(V)≤dim(B')=dim(B)≤dim(C) montrent que",
    "formula in the running text", "displayed formula (\\[...\\])",
    "formula", r"\[" + N + r"\dim(V)\leqslant\dim(B')=\dim(B)\leqslant\dim(C)" + N + r"\]",
    r"$\dim(V)\leqslant\dim(B')=\dim(B)\leqslant\dim(C)$",
    note="Displayed in the TeX, inline in the print; no connecting words lost or added.")
add(202, "p. 202, l. 7: idéal premier minimal", "un *idéal premier minimal* de B'", "un idéal premier minimal de $B'$",
    "italics", "un idéal premier minimal de $B'$", r"un \emph{idéal premier minimal} de $B'$")
add(202, "p. 202, l. 8: B'_{p'} est un corps", "est un *corps*, ou encore", "est un corps, ou encore",
    "italics", "est un corps, ou encore", r"est un \emph{corps}, ou encore")
add(202, "p. 202, l. 9: C-algèbre finie (Bourbaki", "une C-algèbre *finie* (Bourbaki", "une $C$-algèbre finie (Bourbaki",
    "italics", "$C$-algèbre finie (Bourbaki", r"$C$-algèbre \emph{finie} (Bourbaki")
add(202, "p. 202: S=C—n", "S=C—n (long dash)", r"$S=C-\mathfrak n$",
    "convention", r"$S=C-\mathfrak n$", r"$S=C\setmin\mathfrak n$", conv=7, note=C7)
add(202, "p. 202: B_1 est une B-algèbre finie", "une B-algèbre *finie*, et par suite", "une $B$-algèbre finie, et par suite",
    "italics", "$B$-algèbre finie, et par suite", r"$B$-algèbre \emph{finie}, et par suite")
add(202, "p. 202: de dimension 1 (0, 16.1.5)", "(**0**, 16.1.5)", "(0, 16.1.5)",
    "convention", "(0, 16.1.5); si", r"(\textbf{0}, 16.1.5); si", conv=2)
add(202, "p. 202: (II, 7.1.6)", "(**II**, 7.1.6)", "(II, 7.1.6)",
    "convention", "(II," + N + "7.1.6)", r"(\textbf{II}," + N + "7.1.6)", conv=2)
add(202, "p. 202, Corollaire (7.4.5): 'les propriétés a) et b) sont aussi équivalentes à'",
    "a) and b) upright inside the italic statement", "a) et b) in the italic environment (italic)",
    "convention", "propriétés a) et b) sont", r"propriétés \textup{a)} et \textup{b)} sont", conv=6)
add(202, "p. 202, after (7.4.5): 'L'équivalence de a) et b)'", "L'équivalence de *a)* et *b)*", "L'équivalence de a) et b) (roman)",
    "italics", "L'équivalence de a) et b)", r"L'équivalence de \emph{a)} et \emph{b)}")
add(202, "p. 202, after (7.4.5): first reference", "résulte de (7.4.4, (i))", "résulte de (7.4.4, (ii))",
    "number", "résulte de (7.4.4, (ii))", "résulte de (7.4.4, (i))",
    note="The print has (i) here and (ii) only in the second reference; (7.4.4, (i)) is the result that gives a)<=>b).")
add(202, "p. 202, after (7.4.5): 'celle de a) et c)'", "celle de *a)* et *c)*", "celle de a) et c) (roman)",
    "italics", "celle de a) et c)", r"celle de \emph{a)} et \emph{c)}")
add(202, "p. 202: 'Lorsque la condition a) de (7.4.5)'", "la condition *a)* de (7.4.5)", "la condition a) de (7.4.5)",
    "italics", "Lorsque la condition a) de", r"Lorsque la condition \emph{a)} de")
add(202, "p. 202: 'on dit que A est un P-anneau' (definition)", "un *P-anneau*; (anneau italic)", r"un $\boldsymbol P$-anneau; (anneau roman)",
    "italics", r"$\boldsymbol P$-anneau; pour", r"$\boldsymbol P$-\emph{anneau}; pour")
add(202, "p. 202, proof of (7.4.6): (7.3.2, c'))", "(7.3.2, *c')*)", "(7.3.2, c$'$))",
    "italics", r"(7.3.2, c$'$))", r"(7.3.2, \emph{c$'$)})")
add(202, "p. 202, last display: first term", "Spec((A_m)^) (raised hat after the parenthesis)", r"\operatorname{Spec}(\widehat{A_{\mathfrak m}})",
    "formula", r"\operatorname{Spec}(\widehat{A_{\mathfrak m}})", r"\operatorname{Spec}((A_{\mathfrak m})^{\widehat{\,}})",
    note="The print has (A_m) in parentheses with the hat raised after them; same form as the raised-hat page fixes of GLOBAL_ISSUES 47 (enlarged crop).")
add(202, "p. 202, after the last display (continues on p. 203 'tels que f soit fidèlement plat')",
    "no paragraph break: p. 203 continues the sentence without indentation", "blank line after \\] and before \\oldpage[IV-2]{203}",
    "other", r"\operatorname{Spec}(A_{\mathfrak m})" + N + r"\]" + N + N, r"\operatorname{Spec}(A_{\mathfrak m})" + N + r"\]" + N,
    note=G20 + " Apply together with the p. 203 entry that removes the blank line after \\oldpage[IV-2]{203}.")

# ---------------- page 203 ----------------
add(203, "p. 203, top: blank line after the marker", "tels que f soit fidèlement plat; ... (no indent)",
    "blank line after \\oldpage[IV-2]{203}",
    "other", r"\oldpage[IV-2]{203}" + N + N + "tels que", r"\oldpage[IV-2]{203}" + N + "tels que",
    note="Apply together with the p. 202 entry for the blank line after the last display (before the marker).")
add(203, "p. 203, proof of (7.4.7): (0, 17.3.7)", "(**0**, 17.3.7)", "(0, 17.3.7)",
    "convention", "(0, 17.3.7)", r"(\textbf{0}, 17.3.7)", conv=2)
add(203, "p. 203, Remarque (7.4.8): label A)", "A) upright", r"\item[\emph{A)}]",
    "italics", r"\item[\emph{A)}]", r"\item[A)]",
    note="Judged with the remark body roman (document-wide remark item): \\emph would set the label italic; the printed A) is upright.")
add(203, "p. 203, Remarque (7.4.8): label B)", "B) upright", r"\item[\emph{B)}]",
    "italics", r"\item[\emph{B)}]", r"\item[B)]",
    note="As for A) (enlarged crop).")
add(203, "p. 203, (7.4.8) B): 'tendent vers 0'", "*tendent vers* 0 (the 0 upright)", r"\emph{tendent vers 0}",
    "italics", r"\emph{tendent" + N + "vers 0}", r"\emph{tendent" + N + "vers} 0", conf="medium",
    note="Enlarged crop: the old-style zero after 'vers' is upright.")
add(203, "p. 203, Remarque (7.4.8): label C)", "C) upright", r"\item[\emph{C)}]",
    "italics", r"\item[\emph{C)}]", r"\item[C)]",
    note="As for A).")
add(203, "p. 203, (7.4.8) C): (0_I, 7.6.1)", "(**0**_I, 7.6.1)", r"(0$_{\mathrm I}$, 7.6.1)",
    "convention", r"(0$_{\mathrm I}$, 7.6.1)", r"($\mathbf{0}_{\mathrm I}$, 7.6.1)", conv=2)
add(203, "p. 203, (7.4.8) C): (0_I, 7.6.15)", "(**0**_I, 7.6.15)", r"(0$_{\mathrm I}$, 7.6.15)",
    "convention", r"(0$_{\mathrm I}$, 7.6.15)", r"($\mathbf{0}_{\mathrm I}$, 7.6.15)", conv=2)
add(203, "p. 203, heading 7.5", "7.5. Un critère pour les P-morphismes.", "Un critère pour les $\\boldsymbol P$-morphismes (no full stop)",
    "punctuation", r"$\boldsymbol P$-morphismes}{Un critère", r"$\boldsymbol P$-morphismes.}{Un critère",
    note="Subsection title lacks the printed full stop (GLOBAL_ISSUES 43/58); same form as the earlier IV-2 page fixes.")
add(203, "p. 203, (7.5.0): 'pour toute extension finie k' de k'", "extension *finie* k' de k", "extension finie $k'$ de $k$",
    "italics", "extension finie $k'$ de $k$", r"extension \emph{finie} $k'$ de $k$")
add(203, "p. 203, Théorème (7.5.1), l. 1: 'noethériens complets'", "complets in roman inside the italic statement", "complets (italic)",
    "convention", r"noethériens complets, $\mathfrak m$", r"noethériens \textup{complets}, $\mathfrak m$", conv=6,
    note="Enlarged crop: 'complets' is upright between the italic 'noethériens' and 'l'idéal maximal'.")

# ---------------- page 204 ----------------
add(204, "p. 204, end of Théorème (7.5.1): P(f^{-1}(x), k(x))", "**k**(x) bold italic", "k(x)",
    "convention", r"$\boldsymbol P(f^{-1}(x),k(x))$", r"$\boldsymbol P(f^{-1}(x),\boldsymbol{k}(x))$", conv=1)
add(204, "p. 204, proof of (7.5.1), l. 1: 'la fibre du point fermé'", "pour *la fibre du point fermé* de Spec(A)", "pour la fibre du point fermé de (roman)",
    "italics", "pour la fibre du point fermé de", r"pour \emph{la fibre du point fermé} de")
add(204, "p. 204, proof l. 2: 'toutes les fibres'", "pour *toutes les fibres* du morphisme f", "toutes les fibres (roman)",
    "italics", "pour toutes les" + N + "fibres du morphisme", r"pour \emph{toutes les" + N + "fibres} du morphisme")
add(204, "p. 204, proof l. 2: 'f est un P-morphisme (7.3.1)'", "un *P-morphisme* (morphisme italic)", r"$\boldsymbol P$-morphisme (morphisme roman)",
    "italics", r"$\boldsymbol P$-morphisme (7.3.1))", r"$\boldsymbol P$-\emph{morphisme} (7.3.1))")
add(204, "p. 204: 'Nous procéderons en plusieurs étapes :'", "new indented paragraph", "same paragraph as 'Autrement dit, ...'",
    "other", "(7.3.1)). Nous procéderons", "(7.3.1))." + N + N + "Nous procéderons",
    note="Its 'old' shares '(7.3.1))' with the previous entry; the two edits apply in either order.")
add(204, "p. 204, step I): label", "I) upright, then *Réduction ... générique.*", r"\emph{I) Réduction ...} (label italic)",
    "italics", r"\emph{I) Réduction", r"I) \emph{Réduction",
    note="The proof environment is roman; the printed label is upright (enlarged crop).")
add(204, "p. 204, step I): 'A-algèbre finie et intègre A''", "A-algèbre *finie* et *intègre* A'", "finie et intègre (roman)",
    "italics", "$A$-algèbre finie et intègre $A'$", r"$A$-algèbre \emph{finie} et \emph{intègre} $A'$")
add(204, "p. 204, step I): 'il est local'", "il est *local*;", "il est local;",
    "italics", "il est local;", r"il est \emph{local};")
add(204, "p. 204, step I): 'les anneaux locaux de Spec(B'_{n'}⊗_{A'}K') possèdent'", "formula in the running text", "displayed formula",
    "formula", r"\[" + N + r"\operatorname{Spec}(B'_{\mathfrak n'}\otimes_{A'}K')" + N + r"\]", r"$\operatorname{Spec}(B'_{\mathfrak n'}\otimes_{A'}K')$",
    note="No connecting words lost.")
add(204, "p. 204, step I): 'les anneaux locaux de Spec(B'_{n'}⊗_{A'}k'') sont aussi'", "formula in the running text", "displayed formula",
    "formula", r"\[" + N + r"\operatorname{Spec}(B'_{\mathfrak n'}\otimes_{A'}k'')" + N + r"\]", r"$\operatorname{Spec}(B'_{\mathfrak n'}\otimes_{A'}k'')$",
    note="No connecting words lost.")
add(204, "p. 204, step I): 'entraîne que P(Spec(B'_{n'}⊗_{A'}k'), k') est vraie'", "formula in the running text", "displayed formula",
    "formula", r"\[" + N + r"\boldsymbol P(\operatorname{Spec}(B'_{\mathfrak n'}\otimes_{A'}k'),k')" + N + r"\]",
    r"$\boldsymbol P(\operatorname{Spec}(B'_{\mathfrak n'}\otimes_{A'}k'),k')$",
    note="No connecting words lost.")
add(204, "p. 204: 'A est de plus supposé intègre'", "supposé *intègre*", "supposé intègre",
    "italics", "de plus supposé intègre", r"de plus supposé \emph{intègre}")
add(204, "p. 204: 'les anneaux locaux de Spec(B⊗_A K) possèdent la propriété R'",
    "*les anneaux locaux de* Spec(B⊗_A K) *possèdent la propriété* R", "roman",
    "italics", "et à prouver que les anneaux locaux de" + N + r"$\operatorname{Spec}(B\otimes_A K)$ possèdent la propriété",
    r"et à prouver que \emph{les anneaux locaux de}" + N + r"$\operatorname{Spec}(B\otimes_A K)$ \emph{possèdent la propriété}")
add(204, "p. 204, step II): label", "II) upright, then *Cas où* dim(A)=1.", r"\emph{II) Cas où $\dim(A)=1$.} (label italic)",
    "italics", r"\emph{II) Cas où", r"II) \emph{Cas où",
    note="Printed label upright (enlarged crop).")
add(204, "p. 204, step II): (0, 23.1.6)", "(**0**, 23.1.6)", "(0, 23.1.6)",
    "convention", "(0, 23.1.6)", r"(\textbf{0}, 23.1.6)", conv=2)
add(204, "p. 204, step II): 'A-algèbre finie et un anneau local complet'", "A-algèbre *finie* et un anneau *local* complet", "roman",
    "italics", "$A$-algèbre finie et un anneau local", r"$A$-algèbre \emph{finie} et un anneau \emph{local}")
add(204, "p. 204, step II): dim(A')=1 (0, 16.1.5)", "(**0**, 16.1.5)", "(0, 16.1.5)",
    "convention", "(0, 16.1.5) et que", r"(\textbf{0}, 16.1.5) et que", conv=2)
add(204, "p. 204, step II): 'anneau de valuation discrète complet'", "c'est un *anneau de valuation discrète complet*.", "roman",
    "italics", "c'est un anneau de valuation discrète complet.", r"c'est un \emph{anneau de valuation discrète complet}.")
add(204, "p. 204, step II): U_R(Spec(B)) contient le point fermé", "U with a bold upright (sans-serif-looking) R subscript", r"U_{\boldsymbol R} (bold italic R)",
    "font", r"$U_{\boldsymbol R}(\operatorname{Spec}(B))$ contient", r"$U_{\mathbf R}(\operatorname{Spec}(B))$ contient",
    note="Enlarged crop: the subscript R of U_R is upright bold, unlike the bold italic R of R(B); cf. GLOBAL_ISSUES 48 (bold letters upright in subscripts).")
add(204, "p. 204, step II): Mais comme U_R(Spec(B)) est ouvert en vertu de (R_III)", "bold upright R subscript", r"U_{\boldsymbol R}",
    "font", r"$U_{\boldsymbol R}(\operatorname{Spec}(B))$ est ouvert en vertu", r"$U_{\mathbf R}(\operatorname{Spec}(B))$ est ouvert en vertu")
add(204, "p. 204, step III): label", "III) upright, then *Cas général*.", r"\emph{III) Cas général.} (label italic)",
    "italics", r"\emph{III) Cas", r"III) \emph{Cas",
    note="Printed label upright.")
add(204, "p. 204, step III): 'Si nous prouvons que f^{-1}(V')⊂U_R(Spec(B)), la proposition'", "formula in the running text", "displayed formula",
    "formula", r"\[" + N + r"f^{-1}(V')\subset U_{\boldsymbol R}(\operatorname{Spec}(B))," + N + r"\]",
    r"$f^{-1}(V')\subset U_{\boldsymbol R}(\operatorname{Spec}(B))$,",
    note="No connecting words lost. Apply before the next entry (U_R font), whose 'old' lies inside this one.")
add(204, "p. 204, step III): U_R in f^{-1}(V')⊂U_R(Spec(B))", "bold upright R subscript", r"U_{\boldsymbol R}",
    "font", r"\subset U_{\boldsymbol R}", r"\subset U_{\mathbf R}",
    note="Apply after the previous (display) entry; its 'old' is still unique afterwards.")
add(204, "p. 204, step III): complémentaire de U_R(Spec(B))", "bold upright R subscript", r"U_{\boldsymbol R}",
    "font", "complémentaire" + N + r"de $U_{\boldsymbol R}", "complémentaire" + N + r"de $U_{\mathbf R}")
add(204, "p. 204, step III): 'est vide'", "est *vide*.", "est vide.",
    "italics", "est vide. Raisonnons", r"est \emph{vide}. Raisonnons")
add(204, "p. 204, step III): U_R(Spec(B)) est ouvert dans Spec(B)", "bold upright R subscript", r"U_{\boldsymbol R}",
    "font", r"$U_{\boldsymbol R}(\operatorname{Spec}(B))$ est ouvert dans", r"$U_{\mathbf R}(\operatorname{Spec}(B))$ est ouvert dans")
add(204, "p. 204, step III): A_p soit régulier", "soit *régulier*,", "soit régulier,",
    "italics", "soit régulier, alors", r"soit \emph{régulier}, alors")
add(204, "p. 204, step III): (A/p)-algèbre quasi-finie", "(A/p)-algèbre *quasi-finie*", "quasi-finie (roman)",
    "italics", r"$(A/\mathfrak p)$-algèbre quasi-finie", r"$(A/\mathfrak p)$-algèbre \emph{quasi-finie}")
add(204, "p. 204, step III): (0_I, 7.4.4)", "(**0**_I, 7.4.4)", r"(0$_{\mathrm I}$, 7.4.4)",
    "convention", r"(0$_{\mathrm I}$, 7.4.4)", r"($\mathbf{0}_{\mathrm I}$, 7.4.4)", conv=2)
add(204, "p. 204, step III): (0_I, 7.4.1)", "(**0**_I, 7.4.1)", r"(0$_{\mathrm I}$, 7.4.1)",
    "convention", r"(0$_{\mathrm I}$, 7.4.1)", r"($\mathbf{0}_{\mathrm I}$, 7.4.1)", conv=2)
add(204, "p. 204, step III): (A/p)-algèbre finie. En outre", "(A/p)-algèbre *finie*.", "finie (roman)",
    "italics", r"$(A/\mathfrak p)$-algèbre finie. En outre", r"$(A/\mathfrak p)$-algèbre \emph{finie}. En outre")
add(204, "p. 204, step III): donc (0, 16.1.5) on a", "(**0**, 16.1.5)", "(0, 16.1.5)",
    "convention", "(0," + N + "16.1.5) on a", r"(\textbf{0}," + N + "16.1.5) on a", conv=2)
add(204, "p. 204, step III): 'on a dim(A/p)=dim(B/q)=1. On peut alors'", "formula in the running text", "displayed formula",
    "formula", r"\[" + N + r"\dim(A/\mathfrak p)=\dim(B/\mathfrak q)=1." + N + r"\]", r"$\dim(A/\mathfrak p)=\dim(B/\mathfrak q)=1$.",
    note="No connecting words lost; 'On peut alors' continues the same paragraph in the print.")
add(204, "p. 204, step III): 'en outre, on a (B/pB)⊗_{A/p}k=B⊗_A k=B/mB.'", "formula in the running text", "displayed formula",
    "formula", r"\[" + N + r"(B/\mathfrak pB)\otimes_{A/\mathfrak p}k=B\otimes_A k=B/\mathfrak mB." + N + r"\]",
    r"$(B/\mathfrak pB)\otimes_{A/\mathfrak p}k=B\otimes_A k=B/\mathfrak mB$.",
    note="No connecting words lost.")
add(204, "p. 204, step III): 'les anneaux locaux de Spec((B/pB)⊗_{A/p}k(p)) vérifient R'", "formula in the running text (with bold italic k(p))", "displayed formula",
    "formula", r"\[" + N + r"\operatorname{Spec}((B/\mathfrak pB)" + N + r"\otimes_{A/\mathfrak p}k(\mathfrak p))" + N + r"\]",
    r"$\operatorname{Spec}((B/\mathfrak pB)" + N + r"\otimes_{A/\mathfrak p}\boldsymbol{k}(\mathfrak p))$",
    note="No connecting words lost. This one edit also makes the convention-1 change of the next entry (the same formula recurs inline two lines below, so the two changes cannot be given separate unique edits).")
add(204, "p. 204, step III): k(p) in the formula of the previous entry", "**k**(p) bold italic", "k(\\mathfrak p)",
    "convention", None, None, conv=1, fix_none=True,
    note="Made by the edit of the previous entry.")
add(204, "p. 204, step III): 'un des anneaux locaux de Spec((B/pB)⊗_{A/p}k(p))'", "**k**(p) bold italic", "k(\\mathfrak p)",
    "convention", r"k(\mathfrak p))$. En outre", r"\boldsymbol{k}(\mathfrak p))$. En outre", conv=1)
add(204, "p. 204, last line: A_p est régulier", "et A_p est *régulier*.", "est régulier.",
    "italics", r"$A_{\mathfrak p}$ est régulier.", r"$A_{\mathfrak p}$ est \emph{régulier}.")
add(204, "p. 204, last line", "Or on a le lemme suivant :", "Or on a le lemme suivant.",
    "punctuation", "Or on a le lemme suivant.", "Or on a le lemme suivant :")

# ---------------- checks ----------------
ok = True
by_page = {}
for d in F:
    by_page.setdefault(d["page"], []).append(d)
for page, items in sorted(by_page.items()):
    text = (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8")
    assert "\r" not in text
    for d in items:
        if d["fix"] is None:
            continue
        c = text.count(d["fix"]["old"])
        if c != 1:
            ok = False
            print("NOT UNIQUE IN ORIGINAL", page, c, repr(d["fix"]["old"]))
    cur = text
    for d in items:
        if d["fix"] is None:
            continue
        c = cur.count(d["fix"]["old"])
        if c != 1:
            ok = False
            print("SEQUENTIAL PROBLEM", page, c, repr(d["fix"]["old"]))
            continue
        cur = cur.replace(d["fix"]["old"], d["fix"]["new"], 1)
    (RUN / "crops_200_204" / f"applied_{page:03d}.tex").write_text(cur, encoding="utf-8")
print("all unique and sequentially applicable:", ok)
from collections import Counter
cnt = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt.setdefault(d["page"], Counter())[k] += 1
for p in sorted(cnt):
    print(p, dict(cnt[p]))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(F))
