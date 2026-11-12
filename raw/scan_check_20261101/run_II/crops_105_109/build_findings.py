"""Build findings_105_109.json and check every fix against its page_NNN.tex.

In the strings below the character U+23CE stands for a line break (LF).
"""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUTFILE = RUN / "findings_105_109.json"
NL = "⏎"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
    }
    d["fix"] = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def conv2(page, where, ref, old=None, note=""):
    """Bold chapter numeral I or 0 in a reference."""
    num, rest = ref.split(", ", 1)
    old = old or "{" + ref + "}"
    new = old.replace("{" + ref + "}", "{\\textbf{" + num + "}, " + rest + "}")
    return F(page, where, f"({ref}) with bold {num}", f"({ref}) with plain {num} in the link text",
             "convention", 2, "high", old, new, note)


R = []

# ---------------------------------------------------------------- page 105
p = 105
R.append(F(p, "Remarques (5.5.4)(ii), end: 'une Y-immersion j de X dans un P^r_Y (5.3.3) qui est fermée par (5.4.4) et (5.5.3)'",
           "fermée in italics", "fermée upright",
           "italics", None, "high", r"qui est fermée par", r"qui est \emph{fermée} par",
           "The remarks (5.5.4) are set in the TeX as an \\textit heading plus an enumerate, so their body is roman: \\emph gives the printed italic."))
R.append(F(p, "Remarques (5.5.4)(iii), 1st line: 'Le raisonnement de (5.5.3) montre que pour tout préschéma Y'",
           "montre que pour tout (no comma)", "montre que, pour tout",
           "punctuation", None, "high", r"montre que, pour tout", r"montre que pour tout",
           "Comma added in the TeX (checked on an enlarged crop)."))
R.append(F(p, "Remarques (5.5.4)(iii): 'le morphisme structural P^r_Y→Y est surjectif'",
           "surjectif in italics", "surjectif upright",
           "italics", None, "high", r"surjectif, car si on pose", r"\emph{surjectif}, car si on pose"))
R.append(F(p, "Remarques (5.5.4)(iii): 'on a évidemment S_y = S_{k(y)}((k(y))^{r+1})', subscript of S",
           "S_{k(y)} with bold italic k in the subscript", "S_{k(y)} with plain k",
           "convention", 1, "high", r"\mathbf{S}_{k(y)}", r"\mathbf{S}_{\boldsymbol{k}(y)}",
           "Checked on an enlarged crop."))
R.append(F(p, "Remarques (5.5.4)(iii): 'on a évidemment S_y = S_{k(y)}((k(y))^{r+1})', argument",
           "((k(y))^{r+1}) with bold italic k", "((k(y))^{r+1}) with plain k",
           "convention", 1, "high", r"((k(y))^{r+1})", r"((\boldsymbol{k}(y))^{r+1})"))
R.append(conv2(p, "proof of (5.5.5): 'à cause de la restriction introduite sur Z dans (ii) (cf. (I, 3.5.1))'", "I, 3.5.1"))
R.append(conv2(p, "proof of (5.5.5): 'on se ramène au cas où S=Y (I, 3.3.11)'", "I, 3.3.11"))
R.append(F(p, "proof of (5.5.5): 'résulte alors aussitôt de (5.5.1, b)) et de (3.5.3)'",
           "(5.5.1, b)) with b) in italics", "(5.5.1, b)) with b) upright",
           "italics", None, "high", r"{5.5.1, b)}", r"{5.5.1, \emph{b)}}",
           "Letter and parenthesis italic (enlarged crop)."))
R.append(F(p, "proof of (5.5.5): 'P(p'*(E')) = P(E')×_{Y'}T; d'où'",
           "semicolon: ...×_{Y'}T; d'où", "comma: ...\\times_{Y'}T$, d'où",
           "punctuation", None, "high", r"\times_{Y'}T$, d'où", r"\times_{Y'}T$~; d'où",
           "Checked on an enlarged crop."))
R.append(conv2(p, "proof of (5.5.5): 'en remplaçant T par Y×_S Y' et utilisant (I, 3.3.9.1)'", "I, 3.3.9.1"))
R.append(conv2(p, "proof of (5.5.5): 'sont de type fini sur T (0, 5.2.4)'", "0, 5.2.4"))
R.append(F(p, "proof of (5.5.5): 'comme P(p*(E))×_T P(p'*(E')) s'identifie à un sous-préschéma fermé'",
           "P(p*(E))×_T P(p'*(E')) is a centred display", "the same formula inline",
           "other", None, "high",
           r"comme⏎$\mathbf{P}(p^*(\mathcal{E}))\times_T\mathbf{P}(p'^*(\mathcal{E}'))$⏎s'identifie",
           r"comme⏎\[⏎\mathbf{P}(p^*(\mathcal{E}))\times_T\mathbf{P}(p'^*(\mathcal{E}'))⏎\]⏎s'identifie",
           "Inline formula that the print displays (cf. GLOBAL_ISSUES item 21)."))
R.append(conv2(p, "proof of (5.5.5): 'on peut appliquer (I, 5.5.13)'", "I, 5.5.13"))
R.append(F(p, "proof of (5.5.5): 'est un Y-schéma projectif par (5.5.1, a))'",
           "(5.5.1, a)) with a) in italics", "(5.5.1, a)) with a) upright",
           "italics", None, "high", r"{5.5.1, a)}", r"{5.5.1, \emph{a)}}",
           "Letter and parenthesis italic (enlarged crop)."))
R.append(F(p, "Proposition (5.5.7): 'Soient X un Y-schéma projectif, L un O_X-Module Y-ample'",
           "Soient", "Soit",
           "word", None, "high", r"Soit $X$ un $Y$-schéma projectif", r"Soient $X$ un $Y$-schéma projectif"))

# ---------------------------------------------------------------- page 106
p = 106
R.append(F(p, "Corollaire (5.5.8): 'Soient X un préschéma, L un O_X-Module inversible'",
           "Soient", "Soit",
           "word", None, "high", r"Soit $X$ un préschéma, $\mathcal{L}$", r"Soient $X$ un préschéma, $\mathcal{L}$"))
R.append(F(p, "Théorème (5.6.1): '(lemme de Chow)'",
           "(lemme de Chow) with lower-case l", "(Lemme de Chow)",
           "word", None, "high", r"(Lemme de Chow)", r"(lemme de Chow)",
           "The print sets the title in the heading, 'Théorème (5.6.1) (lemme de Chow). — Soient', in roman; that placement is the document-wide titles-in-parentheses item. This finding is only the capital L."))
R.append(F(p, "Théorème (5.6.1): 'Soient S un préschéma, X un S-schéma de type fini'",
           "Soient", "Soit",
           "word", None, "high", r"Soit $S$ un préschéma, $X$ un $S$-schéma", r"Soient $S$ un préschéma, $X$ un $S$-schéma"))
R.append(F(p, "Théorème (5.6.1)(i): 'un S-schéma X' quasi-projectif sur S'",
           "quasi-projectif upright inside the italic statement", "quasi-projectif in the italic theorem environment",
           "convention", 6, "high", r"quasi-projectif sur $S$ et un", r"\textup{quasi-projectif} sur $S$ et un",
           "Enlarged crop: 'quasi-projectif', 'projectif' and 'surjectif' are roman, 'sur', 'et un', 'et' italic."))
R.append(F(p, "Théorème (5.6.1)(i): 'f : X'→X, projectif et surjectif', word 'projectif'",
           "projectif upright", "projectif italic (theorem environment)",
           "convention", 6, "high", r"$f:X'\to X$, projectif et", r"$f:X'\to X$, \textup{projectif} et"))
R.append(F(p, "Théorème (5.6.1)(i): 'projectif et surjectif', word 'surjectif'",
           "surjectif upright ('et' italic)", "surjectif italic (theorem environment)",
           "convention", 6, "high", r"et surjectif.", r"et \textup{surjectif}."))
R.append(F(p, "Théorème (5.6.1)(ii): 'un isomorphisme U'⥲U'",
           "isomorphism arrow (arrow with tilde above)", "U'\\simeq U",
           "convention", 4, "high", r"$U'\simeq U$", r"$U'\xrightarrow{\sim}U$"))
R.append(F(p, "Théorème (5.6.1)(iii): 'Si X est réduit (resp. irréductible, intègre)'",
           "'(resp.' roman inside the italic statement", "(resp. in the italic theorem environment",
           "convention", 6, "high", r"est réduit (resp.", r"est réduit \textup{(resp.}",
           "Enlarged crop."))
R.append(F(p, "Théorème (5.6.1)(iii): 'on peut supposer X' réduit (resp. irréductible, intègre)'",
           "'(resp.' roman inside the italic statement", "(resp. in the italic theorem environment",
           "convention", 6, "high", r"$X'$ réduit (resp.", r"$X'$ réduit \textup{(resp.}"))
R.append(F(p, "proof of (5.6.1), A): 'se ramener au cas où X est irréductible'",
           "irréductible in italics", "irréductible upright",
           "italics", None, "high", r"$X$ est irréductible. En effet", r"$X$ est \emph{irréductible}. En effet"))
R.append(F(p, "proof of (5.6.1), A): 'dans l'hypothèse a), X est noethérien'",
           "a) in italics", "a) upright",
           "italics", None, "high", r"l'hypothèse a), $X$", r"l'hypothèse \emph{a)}, $X$"))
R.append(F(p, "proof of (5.6.1), A): 'le préschéma X' somme des X'_i'",
           "somme in italics", "somme upright",
           "italics", None, "high", r"$X'$ somme des", r"$X'$ \emph{somme} des"))
R.append(F(p, "proof of (5.6.1), A): '(j_i injection canonique X_i→X), répondront à la question'",
           "répondront", "répondent",
           "word", None, "high", r"répondent à la question", r"répondront à la question",
           "Future tense in the print."))
R.append(F(p, "proof of (5.6.1), A): 'la réunion des ensembles U_i ∩ ∁(⋃_{j≠i} X_j)'",
           "complement sign before the parenthesis: U_i∩∁(⋃_{j≠i}X_j)", "U_i\\cap(\\bigcup_{j\\neq i}X_j)^{\\complement}",
           "formula", None, "high", r"U_i\cap(\bigcup_{j\neq i}X_j)^{\complement}", r"U_i\cap\complement(\bigcup_{j\neq i}X_j)",
           "Enlarged crop."))

# ---------------------------------------------------------------- page 107
p = 107
R.append(F(p, "proof of (5.6.1), B): 'Supposons maintenant X irréductible'",
           "irréductible in italics", "irréductible upright",
           "italics", None, "high", r"maintenant $X$ irréductible.", r"maintenant $X$ \emph{irréductible}."))
R.append(F(p, "proof of (5.6.1), B): 'comme dans chacune des hypothèses a), b), l'immersion'",
           "a), b) in italics", "a), b) upright",
           "italics", None, "high", r"hypothèses a),⏎b), l'immersion", r"hypothèses \emph{a)},⏎\emph{b)}, l'immersion"))
R.append(F(p, "proof of (5.6.1), B): 'c'est un morphisme quasi-projectif (5.3.4, (i))'",
           "(5.3.4, (i))", "(5.3.4, (ii))",
           "number", None, "high", r"{5.3.4, (ii)}), donc la restriction", r"{5.3.4, (i)}), donc la restriction",
           "Enlarged crop. The print is right: (5.3.4, (i)) makes the quasi-compact immersion S_i→S quasi-projective, (5.3.4, (ii)) the composite T_ij→S_i→S; the TeX's (ii)/(iii) are a transcription error, not a correction."))
R.append(F(p, "proof of (5.6.1), B): 'la restriction de r à T_ij est un morphisme quasi-projectif (5.3.4, (ii))'",
           "(5.3.4, (ii))", "(5.3.4, (iii))",
           "number", None, "high", r"{5.3.4, (iii)}", r"{5.3.4, (ii)}",
           "See the previous finding; (5.3.4, (iii)) is base change."))
R.append(F(p, "proof of (5.6.1), B), display: 'φ : U→P = P_1×_S P_2× ... ×_S P_n'",
           "P_2× with no subscript S on the second product sign", "P_2\\times_S",
           "misprint_in_print", None, "medium", r"P_2\times_S", r"P_2\times",
           "The TeX silently supplies the subscript S that the print omits after P_2 (enlarged crop); diplomatic reading restored by the fix.",
           corrected=r"P_2\times_S"))
R.append(F(p, "proof of (5.6.1), B), display: 'φ : U→P = P_1×_S P_2× . . . ×_S P_n'",
           "baseline dots . . .", "\\cdots",
           "symbol", None, "high", r"\cdots\times_SP_n", r"\ldots\times_SP_n",
           "Enlarged crop (cf. GLOBAL_ISSUES item 22)."))
R.append(F(p, "proof of (5.6.1), B): 'le morphisme ψ=(j, φ)_S : U→X×_S P est une immersion (I, 5.3.14)'",
           "immersion in italics", "immersion upright",
           "italics", None, "high", r"est une immersion⏎(\hyperref[I.5.3.14-fr]", r"est une \emph{immersion}⏎(\hyperref[I.5.3.14-fr]"))
R.append(conv2(p, "proof of (5.6.1), B): 'est une immersion (I, 5.3.14)'", "I, 5.3.14"))
R.append(F(p, "proof of (5.6.1), B): 'Dans l'hypothèse a), X×_S P est localement noethérien'",
           "a) in italics", "a) upright",
           "italics", None, "high", r"Dans l'hypothèse a), $X\times_SP$", r"Dans l'hypothèse \emph{a)}, $X\times_SP$"))
R.append(F(p, "proof of (5.6.1), B): 'localement noethérien ((3.4.1) et (I, 6.3.7 et 6.3.8))', opening",
           "((3.4.1) et (I, 6.3.7 et 6.3.8)): each reference in its own parentheses inside an outer pair",
           "(3.4.1 et I, 6.3.7 et 6.3.8): one pair of parentheses",
           "punctuation", None, "high",
           r"(\hyperref[II.3.4.1-fr]{3.4.1} et⏎\hyperref[I.6.3.7-fr]",
           r"((\hyperref[II.3.4.1-fr]{3.4.1}) et⏎(\hyperref[I.6.3.7-fr]",
           "Apply together with the next finding (closing parenthesis)."))
R.append(F(p, "proof of (5.6.1), B): 'localement noethérien ((3.4.1) et (I, 6.3.7 et 6.3.8))', closing",
           "...6.3.8)); dans", "...6.3.8})~; dans",
           "punctuation", None, "high", r"6.3.8})~;", r"6.3.8}))~;",
           "Apply together with the previous finding (opening parentheses)."))
R.append(conv2(p, "proof of (5.6.1), B): '(I, 6.3.7 et 6.3.8)'", "I, 6.3.7 et 6.3.8"))
R.append(F(p, "proof of (5.6.1), B): 'dans l'hypothèse b), X×_S P est un schéma quasi-compact'",
           "b) in italics", "b) upright",
           "italics", None, "high", r"dans l'hypothèse b),", r"dans l'hypothèse \emph{b)},"))
R.append(conv2(p, "proof of (5.6.1), B): 'schéma quasi-compact (I, 5.5.1 et 6.6.4)'", "I, 5.5.1 et 6.6.4"))
R.append(F(p, "proof of (5.6.1), B): 'dans les deux cas l'adhérence X' dans X×_S P'",
           "adhérence in italics", "adhérence upright",
           "italics", None, "high", r"cas l'adhérence", r"cas l'\emph{adhérence}"))
R.append(F(p, "proof of (5.6.1), B): 'où ψ' est une immersion ouverte'",
           "immersion ouverte in italics", "immersion ouverte upright",
           "italics", None, "high", r"est une immersion ouverte", r"est une \emph{immersion ouverte}"))
R.append(F(p, "proof of (5.6.1), B): 'et h une immersion fermée (I, 9.5.10)'",
           "immersion fermée in italics", "immersion fermée upright",
           "italics", None, "high", r"$h$ une immersion fermée", r"$h$ une \emph{immersion fermée}"))
R.append(conv2(p, "proof of (5.6.1), B): 'une immersion fermée (I, 9.5.10)'", "I, 9.5.10"))
R.append(F(p, "proof of (5.6.1), B): between the displays (5.6.1.3) and (5.6.1.4)",
           "the two displays follow each other with no word between them", "the word 'et' between the displays",
           "extra", None, "high", r"\]⏎et⏎\[", r"\]⏎\[",
           "'et' is not in the print."))
R.append(F(p, "proof of (5.6.1), C): 'Montrons d'abord que f est projectif et surjectif'",
           "projectif and surjectif in italics", "both upright",
           "italics", None, "high", r"que $f$ est projectif et surjectif, et", r"que $f$ est \emph{projectif} et \emph{surjectif}, et"))
R.append(F(p, "proof of (5.6.1), C): 'est un isomorphisme de U' sur U'",
           "isomorphisme in italics", "isomorphisme upright",
           "italics", None, "high", r"est un isomorphisme de $U'$ sur $U$", r"est un \emph{isomorphisme} de $U'$ sur $U$"))
R.append(F(p, "proof of (5.6.1), C): 'mais f est un morphisme fermé (5.5.3)'",
           "fermé in italics", "fermé upright",
           "italics", None, "high", r"mais $f$ est un morphisme fermé", r"mais $f$ est un morphisme \emph{fermé}"))
R.append(F(p, "proof of (5.6.1), C), last line: 'c'est par suite l'adhérence par' (continues 'rapport à' on p. 108)",
           "par in italics (start of the italic phrase 'par rapport à')", "par upright",
           "italics", None, "high", r"l'adhérence par", r"l'adhérence \emph{par}",
           "The phrase continues on p. 108 ('rapport à', also italic; separate finding there)."))

# ---------------------------------------------------------------- page 108
p = 108
R.append(F(p, "proof of (5.6.1), C), 1st line: 'rapport à U×_S P du préschéma Z'",
           "rapport à in italics (end of 'par rapport à', begun on p. 107)", "rapport à upright",
           "italics", None, "high", r"rapport à $U\times_SP$", r"\emph{rapport à} $U\times_SP$"))
R.append(conv2(p, "proof of (5.6.1), C): 'du préschéma Z (I, 9.5.8). Or l'immersion'", "I, 9.5.8",
               old=r"{I, 9.5.8}). Or l'immersion"))
R.append(F(p, "proof of (5.6.1), C): 'Or l'immersion ψ se factorise en U→U×_S P→X×_S P, et comme'",
           "the factorisation U --Γ_φ--> U×_S P --j×1--> X×_S P is inline in the text line", "a separate display",
           "other", None, "high",
           r"se factorise en⏎\[⏎U\xrightarrow{\Gamma_\varphi}U\times_SP\xrightarrow{j\times1}X\times_SP,⏎\]⏎et comme",
           r"se factorise en⏎$U\xrightarrow{\Gamma_\varphi}U\times_SP\xrightarrow{j\times1}X\times_SP$,⏎et comme",
           "Displayed formula that the print sets inline (cf. GLOBAL_ISSUES item 21)."))
R.append(conv2(p, "proof of (5.6.1), C): 'immersion fermée (I, 5.4.3), donc Z est un'", "I, 5.4.3",
               old=r"{I, 5.4.3}), donc $Z$"))
R.append(F(p, "proof of (5.6.1), C): 'donc Z est un sous-préschéma fermé de U×_S P'",
           "fermé in italics", "fermé upright",
           "italics", None, "high", r"sous-préschéma fermé de $U\times_SP$", r"sous-préschéma \emph{fermé} de $U\times_SP$"))
R.append(F(p, "proof of (5.6.1), D): 'Prouvons maintenant que g est une immersion'",
           "immersion in italics", "immersion upright",
           "italics", None, "high", r"que $g$ est une immersion, ce qui", r"que $g$ est une \emph{immersion}, ce qui"))
R.append(F(p, "proof of (5.6.1), D): 'ce qui établira que X' est quasi-projectif sur S'",
           "quasi-projectif in italics", "quasi-projectif upright",
           "italics", None, "high", r"quasi-projectif sur $S$, puisque", r"\emph{quasi-projectif} sur $S$, puisque"))
R.append(F(p, "proof of (5.6.1), D), display 'Posons': row V_k",
           "(ouvert de P_k) with no comma after it", "\\text{(ouvert de $P_k$)},",
           "punctuation", None, "high", r"(ouvert de $P_k$)},\\", r"(ouvert de $P_k$)}\\",
           "Enlarged crop: the display has no punctuation."))
R.append(F(p, "proof of (5.6.1), D), display 'Posons': row W_k",
           "(ouvert de P) with no comma after it", "\\text{(ouvert de $P$)},",
           "punctuation", None, "high", r"(ouvert de $P$)},\\", r"(ouvert de $P$)}\\"))
R.append(F(p, "proof of (5.6.1), D), display 'Posons': rows U'_k, U''_k",
           "U'_k=f^{-1}(U_k) and U''_k=g^{-1}(W_k) on two lines joined by a right brace to '(ouverts de X')', no comma, no final period",
           "both on one line separated by ',\\qquad', label followed by a period",
           "punctuation", None, "high",
           r"U'_k&=f^{-1}(U_k),\qquad U''_k=g^{-1}(W_k)⏎&&\text{(ouverts de $X'$)}.",
           r"&\left.\begin{aligned}U'_k&=f^{-1}(U_k)\\U''_k&=g^{-1}(W_k)\end{aligned}\right\}⏎&&\text{(ouverts de $X'$)}",
           "The added comma and period are the textual differences; the brace layout of the fix is approximate (amsmath aligned inside the align*)."))
R.append(conv2(p, "proof of (5.6.1), D): 'par rapport à U'_k (I, 9.5.8). Pour montrer'", "I, 9.5.8",
               old=r"{I, 9.5.8}). Pour montrer"))
R.append(conv2(p, "proof of (5.6.1), D): 'on obtient un diagramme commutatif (I, 9.5.6)'", "I, 9.5.6"))
R.append(conv2(p, "proof of (5.6.1), D): 'est une immersion dans W_k (I, 4.2.4)'", "I, 4.2.4"))
R.append(conv2(p, "proof of (5.6.1), D): 'est une immersion fermée (I, 5.4.3), donc le graphe'", "I, 5.4.3",
               old=r"{I, 5.4.3}), donc le graphe"))
R.append(F(p, "proof of (5.6.1), D): 'le sous-préschéma induit par X' sur l'ouvert X''_k de X''",
           "X''_k", "X''_k (keeps the print)",
           "misprint_in_print", None, "high", None, None,
           "TeX keeps the printed reading. The open set is U''_k = g^{-1}(W_k), defined in the display above; X''_k is never defined (enlarged crop).",
           corrected=r"U''_k"))
R.append(conv2(p, "proof of (5.6.1), D): 'de X', par (I, 9.5.8). Comme la restriction'", "I, 9.5.8",
               old=r"{I, 9.5.8}). Comme la restriction"))
R.append(F(p, "proof of (5.6.1), D): 'la restriction de g à X''_k sera une immersion dans W_k'",
           "X''_k", "X''_k (keeps the print)",
           "misprint_in_print", None, "high", None, None,
           "TeX keeps the printed reading; should be U''_k (g|U''_k, as in 'chacune des restrictions g|U''_k' above).",
           corrected=r"U''_k"))
R.append(conv2(p, "proof of (5.6.1), D): 'il suffit de prouver que q_1∘v_k=u_k∘q_2∘v_k (I, 3.2.1)'", "I, 3.2.1"))

# ---------------------------------------------------------------- page 109
p = 109
R.append(F(p, "proof of (5.6.1), E): 'le morphisme f est donc birationnel (I, 2.2.9)'",
           "birationnel in italics", "birationnel upright",
           "italics", None, "high", r"est donc⏎birationnel", r"est donc⏎\emph{birationnel}"))
R.append(conv2(p, "proof of (5.6.1), E): 'birationnel (I, 2.2.9)'", "I, 2.2.9"))
R.append(conv2(p, "proof of (5.6.1), E): 'donc X' est réduit (I, 9.5.9)'", "I, 9.5.9"))
R.append(F(p, "Corollaire (5.6.2): 'On suppose vérifiée l'une des hypothèses a), b) de (5.6.1)'",
           "a), b) roman inside the italic statement", "a), b) in the italic corollary environment",
           "convention", 6, "high", r"hypothèses a), b) de", r"hypothèses \textup{a), b)} de",
           "Enlarged crop."))
R.append(F(p, "Corollaire (5.6.2): 'soit un isomorphisme f^{-1}(U)⥲U'",
           "isomorphism arrow (arrow with tilde above)", "f^{-1}(U)\\simeq U",
           "convention", 4, "high", r"$f^{-1}(U)\simeq U$", r"$f^{-1}(U)\xrightarrow{\sim}U$"))
R.append(F(p, "Corollaire (5.6.2): 'Si en outre X est irréductible (resp. réduit)'",
           "'(resp.' roman inside the italic statement", "(resp. in the italic corollary environment",
           "convention", 6, "high", r"(resp. réduit)", r"\textup{(resp.} réduit)",
           "Enlarged crop."))
R.append(F(p, "Corollaire (5.6.3): 'Soient S un préschéma localement noethérien'",
           "Soient", "Soit",
           "word", None, "high", r"Soit $S$ un préschéma localement noethérien", r"Soient $S$ un préschéma localement noethérien"))
R.append(F(p, "Corollaire (5.6.3): 'que pour tout morphisme de type fini S'→S'",
           "de type fini roman inside the italic statement", "de type fini in the italic corollary environment",
           "convention", 6, "high", r"morphisme de type fini $S'\to S$", r"morphisme \textup{de type fini} $S'\to S$",
           "Enlarged crop; the earlier 'X un S-schéma de type fini sur S' of the same statement is italic, as in the TeX."))
R.append(F(p, "proof of (5.6.3), diagram: bottom arrow S ←r— P",
           "label r below the arrow", "P\\ar[l]_r (for a leftward arrow xy-pic sets a _ label above)",
           "formula", None, "medium", r"P\ar[l]_r", r"P\ar[l]^r",
           "The top label f is above its arrow in the print, as \\ar[l]_f gives; only r is on the wrong side."))
R.append(F(p, "proof of (5.6.3): 'la projection q_2 : X×_S P→P est un morphisme fermé'",
           "fermé in italics", "fermé upright",
           "italics", None, "high", r"est un morphisme fermé. Mais", r"est un morphisme \emph{fermé}. Mais"))


# ---------------------------------------------------------------- checks
def load(page):
    return (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
texts = {}
for d in R:
    pg = d["page"]
    texts.setdefault(pg, load(pg))
    if d["fix"] is None:
        continue
    n = texts[pg].count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE", pg, n, repr(d["fix"]["old"]))

# apply all fixes in order and in reverse order: each old must still occur exactly once
for order in ("forward", "reverse"):
    cur = {pg: t for pg, t in texts.items()}
    seq = R if order == "forward" else list(reversed(R))
    for d in seq:
        if d["fix"] is None:
            continue
        pg = d["page"]
        n = cur[pg].count(d["fix"]["old"])
        if n != 1:
            ok = False
            print("CONFLICT", order, pg, n, repr(d["fix"]["old"]))
            continue
        cur[pg] = cur[pg].replace(d["fix"]["old"], d["fix"]["new"], 1)

# misprints that the TeX keeps: the printed reading must be in the TeX
for d in R:
    if d["kind"] == "misprint_in_print" and d["fix"] is None:
        if texts[d["page"]].count("X''_k") < 1:
            ok = False
            print("MISPRINT TEXT MISSING", d["page"])

counts = {}
for d in R:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
print("total", len(R), "ok" if ok else "PROBLEMS")
OUTFILE.write_text(json.dumps(R, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
print("wrote", OUTFILE)
