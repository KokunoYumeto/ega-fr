"""Build findings_080_084.json from the entries below and check every fix's "old" occurs exactly once in its page file.
Strings are raw; the pilcrow stands for a newline (the release files use LF)."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_080_084.json"
NL = "¶"

F = []


def f(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    fix = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n") if corrected is not None else None
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 80
f(80, "top of p. 80: 'On appelle multiplicité | totale de x' (Définition (4.7.12) runs over the page break)",
  "'totale de x (ou du cycle premier ...' continues the sentence of p. 79 at the left margin (no new paragraph)",
  "blank lines before and after \\oldpage[IV-2]{80} (paragraph break inside the sentence)",
  "other", None, "high",
  r"\oldpage[IV-2]{80}¶¶", r"\oldpage[IV-2]{80}¶",
  "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with removing the blank "
  "line BEFORE the marker, which lies in page 79's segment (ega4-2-fr.tex, line before \\oldpage[IV-2]{80}): "
  "'On appelle \\emph{multiplicité}\\n\\n' -> 'On appelle \\emph{multiplicité}\\n'.")
f(80, "Définition (4.7.12), first line of p. 80: 'totale de x (ou du cycle premier ...)'",
  "'totale de x' italic like the rest of the statement (no change of face; enlarged crop)",
  "\\emph{totale de $x$} inside the italic definition environment (prints upright)",
  "convention", 6, "high",
  r"\emph{totale de $x$}", r"totale de $x$",
  "No change of face in the print; \\emph inside the italic environment sets the words upright. The first half of the "
  "term, \\emph{multiplicité}, is on p. 79 (that page's check decides it).")
f(80, "Définition (4.7.12): 'par la multiplicité séparable de k(x) sur k'",
  "bold italic k in k(x)", "$k(x)$", "convention", 1, "high",
  r"séparable de $k(x)$", r"séparable de $\boldsymbol{k}(x)$", "")
f(80, "2nd paragraph, l. 2: 'le produit de la longueur long_{O_x}(F_x)'",
  "'longueur' italic", "longueur (roman)", "italics", None, "high",
  r"la longueur", r"la \emph{longueur}", "")
f(80, "2nd paragraph, l. 2: 'par la multiplicité totale de k(x)'",
  "'la' set in bold roman (wrong-font sort): 8x side-by-side crop with the 'la' of 'de la longueur' on the same line "
  "shows a much heavier bowl and stem (about 1.3 times the ink of the a, 1.2 of the l)",
  "par la multiplicité totale", "misprint_in_print", None, "medium",
  r"par la multiplicité totale", r"par \textbf{la} multiplicité totale",
  "Wrong-font slip in the print (cf. the bold 'que' recorded for 0_III p. 11); the TeX silently normalizes it. "
  "Drop this edit if wrong-font words are not reproduced.",
  corrected=r"par la multiplicité totale")
f(80, "2nd paragraph, l. 2: 'multiplicité totale de k(x) sur k (4.7.4)'",
  "bold italic k in k(x)", "$k(x)$", "convention", 1, "high",
  r"de $k(x)$ sur $k$ (4.7.4)", r"de $\boldsymbol{k}(x)$ sur $k$ (4.7.4)", "")
f(80, "2nd paragraph, l. 3: 'est égale à la somme des multiplicités totales'",
  "'somme' italic", "somme (roman)", "italics", None, "high",
  r"la somme des", r"la \emph{somme} des", "")
f(80, "2nd paragraph, l. 5: 'il existe une extension finie k' de k'",
  "'finie' italic", "finie (roman)", "italics", None, "high",
  r"extension finie $k'$", r"extension \emph{finie} $k'$", "")
f(80, "2nd paragraph, last line: 'soit égale à Σ_i long(F'_{x'_i})'",
  "'égale à' italic", "égale à (roman)", "italics", None, "high",
  r"soit égale à¶$\sum_i", r"soit \emph{égale à}¶$\sum_i", "")
f(80, "Proposition (4.7.13), l. 1: 'étant celles de (4.7.10), pour que'",
  "(4.7.10) upright inside the italic statement", "(4.7.10) (italic in the environment)",
  "convention", 6, "high",
  r"celles de (4.7.10)", r"celles de \textup{(4.7.10)}", "")
f(80, "proof of (4.7.13), l. 2: 'x' ne peut appartenir qu'à un seul cycle premier associé à F,'",
  "'associé à 𝓕,' without prime (enlarged crop)", "associé à $\\mathscr F'$,",
  "misprint_in_print", None, "high",
  r"associé à $\mathscr F'$,", r"associé à $\mathscr F$,",
  "x' is a point of X' = X⊗_k k', so the associated prime cycles meant are those of 𝓕'. The TeX silently corrects; "
  "the fix restores the printed reading.",
  corrected=r"associé à $\mathscr F'$,")
f(80, "heading 4.8", "'4.8. Corps de définition.' (final full stop)", "\\subsection{Corps de définition}",
  "punctuation", None, "high",
  r"\subsection{Corps de définition}", r"\subsection{Corps de définition.}",
  "GLOBAL_ISSUES 43/58 pattern (subsection titles lack the printed full stop); same fix as IV-2 pp. 5, 9, 33.")
f(80, "display (4.8.2.1)", "no comma after the formula", "comma after the formula", "punctuation", None, "high",
  r"\Phi(\mathscr F\otimes_kK),", r"\Phi(\mathscr F\otimes_kK)", "Enlarged crop of the five displays.")
f(80, "display (4.8.2.2)", "no comma after the formula", "comma after the formula", "punctuation", None, "high",
  r"\mathscr G\otimes_kK),", r"\mathscr G\otimes_kK)", "")
f(80, "display (4.8.2.3)", "no comma after the formula", "comma after the formula", "punctuation", None, "high",
  r"\mathfrak S(X_{(K)}),", r"\mathfrak S(X_{(K)})", "")
f(80, "display (4.8.2.4)", "no comma after the formula", "comma after the formula", "punctuation", None, "high",
  r"Y_{(K)}),", r"Y_{(K)})", "")
f(80, "display (4.8.2.5)", "no full stop after the formula", "full stop after the formula", "punctuation", None,
  "high", r"\mathfrak P(X_{(K)}).", r"\mathfrak P(X_{(K)})", "")
f(80, "after the displays: 'l'application (4.8.2.5) est M ⇝ p_X^{-1}(M)'",
  "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
  r"$M\mapsto p_X^{-1}(M)$", r"$M\leadsto p_X^{-1}(M)$",
  "Wavy maps-to arrow (\\leadsto, GLOBAL_ISSUES 33/73); enlarged crop.")
f(80, "after the displays: 'de même (4.8.2.3) est Z ⇝ p_X^{-1}(Z) = Z⊗_{K'}K'",
  "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
  r"$Z\mapsto p_X^{-1}(Z)", r"$Z\leadsto p_X^{-1}(Z)", "")
f(80, "after the displays: 'Z⊗_{K'}K (I, 4.4.1)'", "bold I", "(I, 4.4.1)", "convention", 2, "high",
  r"(I, 4.4.1)", r"(\textbf{I}, 4.4.1)", "")
f(80, "'L'application (4.8.2.1) est H ⇝ p_X^*(H) = H⊗_{O_{X_(K')}}O_{X_(K)}; (4.8.2.2) est ...'",
  "the formula is in the running text ('tion (4.8.2.1) est ...; (4.8.2.2) est u ⇝ ...' on one line), with a wavy arrow",
  "displayed with \\[ ... \\] and \\longmapsto", "other", None, "high",
  r"\[¶\mathscr H\longmapsto p_X^*(\mathscr H)¶=\mathscr H\otimes_{\mathcal O_{X_{(K')}}}\mathcal O_{X_{(K)}};¶\]",
  r"$\mathscr H\leadsto p_X^*(\mathscr H)¶=\mathscr H\otimes_{\mathcal O_{X_{(K')}}}\mathcal O_{X_{(K)}}$;",
  "Formula displayed where the print has it inline; no connecting word lost. The edit also sets the printed wavy "
  "arrow (\\leadsto for \\longmapsto): no separate arrow finding for it.")
f(80, "'(4.8.2.2) est u ⇝ p_X^*(u)'", "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
  r"$u\mapsto p_X^*(u)$", r"$u\leadsto p_X^*(u)$", "")
f(80, "'(4.8.2.4) est l'application f ⇝ f_{(K)}'", "wavy arrow ⇝", "\\mapsto", "symbol", None, "high",
  r"$f\mapsto f_{(K)}$", r"$f\leadsto f_{(K)}$", "")


# ---------------------------------------------------------------- page 81
f(81, "Proposition (4.8.3): 'Les applications canoniques (4.8.2.1) à ...'",
  "(4.8.2.1) upright inside the italic statement", "(4.8.2.1) (italic in the environment)",
  "convention", 6, "high",
  r"canoniques (4.8.2.1)", r"canoniques \textup{(4.8.2.1)}", "")
f(81, "Proposition (4.8.3): '... à (4.8.2.5) sont injectives'",
  "(4.8.2.5) upright inside the italic statement", "(4.8.2.5) (italic in the environment)",
  "convention", 6, "high",
  r"(4.8.2.5) sont injectives", r"\textup{(4.8.2.5)} sont injectives", "")
f(81, "proof of (4.8.3): 'p_X est fidèlement plat et quasi-compact'",
  "'fidèlement plat' italic", "fidèlement plat (roman)", "italics", None, "high",
  r"est fidèlement plat", r"est \emph{fidèlement plat}", "")
f(81, "proof of (4.8.3): 'et quasi-compact; le fait que'",
  "'quasi-compact' italic", "quasi-compact (roman)", "italics", None, "high",
  r"et quasi-compact;", r"et \emph{quasi-compact};", "")
f(81, "Définition (4.8.4), l. 1: 'Les notations étant celles de (4.8.2), on dit'",
  "(4.8.2) upright inside the italic statement", "(4.8.2) (italic in the environment)",
  "convention", 6, "high",
  r"celles de (4.8.2), on dit", r"celles de \textup{(4.8.2)}, on dit", "Enlarged crop of the whole definition.")
f(81, "Définition (4.8.4), l. 2: '(resp. un homomorphisme'",
  "'(resp.' upright inside the italic statement", "(resp. (italic in the environment)",
  "convention", 6, "high",
  r"(resp. un homomorphisme", r"\textup{(resp.} un homomorphisme", "")
f(81, "Définition (4.8.4), l. 2: ', resp. un sous-préschéma'",
  "'resp.' upright inside the italic statement", "resp. (italic in the environment)",
  "convention", 6, "high",
  r"resp. un sous-préschéma", r"\textup{resp.} un sous-préschéma", "")
f(81, "Définition (4.8.4), l. 3: ', resp. un K-morphisme'",
  "'resp.' upright inside the italic statement", "resp. (italic in the environment)",
  "convention", 6, "high",
  r"resp. un $K$-morphisme", r"\textup{resp.} un $K$-morphisme", "")
f(81, "Définition (4.8.4), l. 3: ', resp. un sous-ensemble de X_(K)) est'",
  "'resp.' and the closing parenthesis after X_(K) upright inside the italic statement (5x crop)",
  "resp. and ) (italic in the environment)", "convention", 6, "high",
  r"resp. un¶sous-ensemble de $X_{(K)}$)", r"\textup{resp.} un¶sous-ensemble de $X_{(K)}$\textup{)}", "")
f(81, "Définition (4.8.4), l. 4-5: 'l'application (4.8.2.1) (resp. (4.8.2.2), resp. (4.8.2.3), resp. (4.8.2.4), "
      "resp. (4.8.2.5))'",
  "the references and the 'resp.' between them upright inside the italic statement",
  "all italic in the environment", "convention", 6, "high",
  r"l'application (4.8.2.1) (resp. (4.8.2.2), resp. (4.8.2.3), resp.¶(4.8.2.4), resp. (4.8.2.5))",
  r"l'application \textup{(4.8.2.1) (resp. (4.8.2.2), resp. (4.8.2.3), resp.¶(4.8.2.4), resp. (4.8.2.5))}",
  "The defined term 'défini sur K'' is printed roman, which the TeX's \\emph already gives.")
f(81, "Définition (4.8.4), last sentence: 'On dit alors que K' est un corps de définition de l'objet considéré'",
  "'corps de définition' italic like the rest of the sentence (no change of face)",
  "\\emph{corps de définition} inside the italic definition environment (prints upright)",
  "convention", 6, "high",
  r"\emph{corps de¶définition}", r"corps de¶définition",
  "No change of face in the print; \\emph inside the italic environment sets the words upright.")
f(81, "paragraph after (4.8.4): 'des applications de (4.8.2) est défini sur K', il est aussi défini sur tout corps'",
  "the first 'défini sur' italic (the second one roman)", "défini sur (roman)", "italics", None, "high",
  r"(4.8.2) est défini sur", r"(4.8.2) est \emph{défini sur}", "Enlarged crop.")
f(81, "Proposition (4.8.5), l. 1: 'Avec les notations de (4.8.2), soit'",
  "(4.8.2) upright inside the italic statement", "(4.8.2) (italic in the environment)",
  "convention", 6, "high",
  r"notations de (4.8.2), soit", r"notations de \textup{(4.8.2)}, soit", "")
f(81, "Proposition (4.8.5), l. 2: 'H∈Φ(F⊗_kK) (resp. u∈Hom(...)'",
  "'(resp.' upright inside the italic statement", "(resp. (italic in the environment)",
  "convention", 6, "high",
  r"(resp.¶$u\in", r"\textup{(resp.}¶$u\in", "")
f(81, "Proposition (4.8.5), l. 2: ', resp. Z∈S(X_(K))'",
  "'resp.' upright inside the italic statement", "resp. (italic in the environment)",
  "convention", 6, "high",
  r", resp.¶$Z\in", r", \textup{resp.}¶$Z\in", "")
f(81, "Proposition (4.8.5), l. 3: 'resp. M∈P(X_(K))) soit défini sur K''",
  "'resp.' and the closing parenthesis of '(resp. ...)' upright inside the italic statement",
  "resp. and ) (italic in the environment)", "convention", 6, "high",
  r"resp. $M\in\mathfrak P(X_{(K)})$)", r"\textup{resp.} $M\in\mathfrak P(X_{(K)})$\textup{)}", "")
f(81, "Proposition (4.8.5), l. 3: 'H|(X_α)_(K) (resp. u|(X_α)_(K), ...'",
  "'(resp.' upright inside the italic statement", "(resp. (italic in the environment)",
  "convention", 6, "high",
  r"(resp. $u|(X_\alpha)_{(K)}$", r"\textup{(resp.} $u|(X_\alpha)_{(K)}$", "")
f(81, "Proposition (4.8.5), l. 4: 'M∩(X_α)_(K)) soit défini sur K''",
  "the closing parenthesis upright inside the italic statement", ") (italic in the environment)",
  "convention", 6, "high",
  r"$M\cap(X_\alpha)_{(K)}$)", r"$M\cap(X_\alpha)_{(K)}$\textup{)}", "")
f(81, "proof of (4.8.5): 'on aura H|(X_α∩X_β)_(K) = (H'_α|(X_α∩X_β)_(K'))⊗_{K'}K = (H'_β|(X_α∩X_β)_(K'))⊗_{K'}K, "
      "donc'",
  "the chain begins with the member 'H|(X_α∩X_β)_(K) =' (enlarged crop)",
  "the first member is missing; the display starts at (H'_α|...)⊗_{K'}K", "missing", None, "high",
  r"on aura¶\[¶\bigl(\mathscr H'_\alpha|(X_\alpha\cap X_\beta)_{(K')}\bigr)¶ \otimes_{K'}K¶"
  r"=\bigl(\mathscr H'_\beta|(X_\alpha\cap X_\beta)_{(K')}\bigr)¶ \otimes_{K'}K,¶\]¶donc",
  r"on aura¶$\mathscr H|(X_\alpha\cap X_\beta)_{(K)}¶=\bigl(\mathscr H'_\alpha|(X_\alpha\cap X_\beta)_{(K')}\bigr)¶"
  r" \otimes_{K'}K¶=\bigl(\mathscr H'_\beta|(X_\alpha\cap X_\beta)_{(K')}\bigr)¶ \otimes_{K'}K$,¶donc",
  "One edit for this finding and the next: it restores the missing member and sets the chain inline, as printed.")
f(81, "proof of (4.8.5): the same chain of equalities",
  "in the running text ('on aura ... , donc' fills one justified line)", "displayed with \\[ ... \\]",
  "other", None, "high", None, None,
  "Covered by the edit of the preceding finding (missing member), which also sets the formula inline; no "
  "connecting word lost.")
f(81, "Lemme (4.8.6), label a)", "a) upright", "\\item[a)] (italic in the lemma environment)",
  "convention", 6, "high",
  r"\item[a)]", r"\item[\textup{a)}]", "Lettered labels printed upright here (as on pp. 68, 71-73).")
f(81, "Lemme (4.8.6), label b)", "b) upright", "\\item[b)] (italic in the lemma environment)",
  "convention", 6, "high",
  r"\item[b)]", r"\item[\textup{b)}]", "")
f(81, "Lemme (4.8.6) b): 'le O_{X_(K)}-Module quasi-cohérent (N̄)~ sur X_(K)'",
  "(N̄)~: parentheses around N̄ and the tilde after the closing parenthesis",
  "$\\widetilde{\\overline N}$ (tilde over the bare N̄, parentheses dropped)", "convention", 5, "high",
  r"$\widetilde{\overline N}$", r"$(\overline N)^{\sim}$",
  "Written as ega4-2-fr.tex already writes (M⊗_A N')^{\\sim} and (\\overline v)^{\\sim}; \\supertilde is not "
  "defined in the IV-2 package preamble.")
f(81, "Lemme (4.8.6), label c)", "c) upright", "\\item[c)] (italic in the lemma environment)",
  "convention", 6, "high",
  r"\item[c)]", r"\item[\textup{c)}]", "")


# ---------------------------------------------------------------- page 82
f(82, "proof of (4.8.6), l. 1: 'L'équivalence de a) et b) résulte'",
  "a) and b) italic", "a), b) (roman)", "italics", None, "high",
  r"de a) et b) résulte", r"de \emph{a)} et \emph{b)} résulte", "Enlarged crop.")
f(82, "proof of (4.8.6), l. 1: 'résulte trivialement de (I, 1.6.5)'", "bold I", "(I, 1.6.5)",
  "convention", 2, "high",
  r"(I, 1.6.5)", r"(\textbf{I}, 1.6.5)", "")
f(82, "proof of (4.8.6), l. 2: 'que a) entraîne c)'",
  "a) and c) italic", "a), c) (roman)", "italics", None, "high",
  r"que a) entraîne c).", r"que \emph{a)} entraîne \emph{c)}.", "")
f(82, "proof of (4.8.6), l. 2: 'Inversement, si c) est vérifiée'",
  "c) italic", "c) (roman)", "italics", None, "high",
  r"si c) est vérifiée", r"si \emph{c)} est vérifiée", "")
f(82, "Corollaire (4.8.7), l. 1: 'Sous les hypothèses de (4.8.6), il existe'",
  "(4.8.6) upright inside the italic statement", "(4.8.6) (italic in the environment)",
  "convention", 6, "high",
  r"hypothèses de (4.8.6)", r"hypothèses de \textup{(4.8.6)}", "")
f(82, "Corollaire (4.8.7), l. 2: 'les conditions équivalentes de (4.8.6) soient vérifiées'",
  "(4.8.6) upright inside the italic statement", "(4.8.6) (italic in the environment)",
  "convention", 6, "high",
  r"équivalentes de (4.8.6)", r"équivalentes de \textup{(4.8.6)}", "")
f(82, "proof of (4.8.7): 'pour la condition c), où cela résulte de Bourbaki'",
  "c) italic", "c) (roman)", "italics", None, "high",
  r"condition c), où", r"condition \emph{c)}, où", "")
f(82, "proof of (4.8.7): 'Bourbaki, Alg., chap II, 3e éd.'",
  "'chap' without the abbreviation point (5x crop: no point between 'chap' and II)",
  "chap.~II", "misprint_in_print", None, "high",
  r"chap.~", r"chap~",
  "Missing point in the print; the TeX silently supplies it. Independent of the next finding (its 'old' starts "
  "after this one's).",
  corrected=r"chap.~")
f(82, "proof of (4.8.7): 'Bourbaki, Alg., chap II, 3e éd.'",
  "chap II with a BOLD II (wrong fount; Bourbaki chapter numerals are light elsewhere)", "II (light)",
  "misprint_in_print", None, "high",
  r"II, 3\textsuperscript{e}", r"\textbf{II}, 3\textsuperscript{e}",
  "Wrong-fount numeral, recorded and reproduced as on IV-2 p. 22 ('chap. II, § 5'); the TeX normalizes it.",
  corrected=r"II, 3\textsuperscript{e}")
f(82, "Lemme (4.8.8), l. 1: 'Les notations étant celles de (4.8.2) :'",
  "(4.8.2) upright inside the italic statement", "(4.8.2) (italic in the environment)",
  "convention", 6, "high",
  r"celles de (4.8.2):", r"celles de \textup{(4.8.2)}:", "")
f(82, "Lemme (4.8.8), label (i)", "(i) upright", "\\item[(i)] (italic in the lemma environment)",
  "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
f(82, "Lemme (4.8.8), label (ii)", "(ii) upright", "\\item[(ii)] (italic in the lemma environment)",
  "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
f(82, "Lemme (4.8.8), label (iii)", "(iii) upright", "\\item[(iii)] (italic in the lemma environment)",
  "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", "GLOBAL_ISSUES 16.")
f(82, "Lemme (4.8.8) (iii): 'graphe de f̄ (I, 5.3.11); pour que'", "bold I", "(I, 5.3.11)",
  "convention", 2, "high",
  r"$\overline f$ (I, 5.3.11)", r"$\overline f$ \textup{(\textbf{I}, 5.3.11)}",
  "One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
f(82, "Lemme (4.8.8) (iii): same reference '(I, 5.3.11)'",
  "the reference is upright inside the italic statement", "(I, 5.3.11) (italic in the environment)",
  "convention", 6, "high", None, None,
  "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
f(82, "proof of (4.8.8), l. 1: 'résulte aussitôt de (I, 4.4.5)'", "bold I", "(I, 4.4.5)",
  "convention", 2, "high", r"(I, 4.4.5)", r"(\textbf{I}, 4.4.5)", "")
f(82, "proof of (4.8.8), l. 2: 'supposons réciproquement que l'on ait Z̄ = Z'_(K')'",
  "Z̄ = Z'_{(K')} (subscript (K'), 6x crop)", "\\overline Z=Z'_{(K)}", "misprint_in_print", None, "high",
  r"\overline Z=Z'_{(K)}", r"\overline Z=Z'_{(K')}",
  "Z' is a sub-prescheme of (X×_kY)_{(K')} and Z̄ is its extension to K, so the subscript must be (K). "
  "The TeX silently corrects; the fix restores the printed reading.",
  corrected=r"\overline Z=Z'_{(K)}")
f(82, "proof of (4.8.8): 'mais cela signifie (I, 5.3.11) que'", "bold I", "(I, 5.3.11)",
  "convention", 2, "high", r"signifie (I, 5.3.11)", r"signifie (\textbf{I}, 5.3.11)", "")
f(82, "proof of (4.8.8), end: 'et l'on a alors f = f'_(K)'",
  "f = f'_{(K)}: no bar over the first f (6x crop)", "\\overline f=f'_{(K)}", "misprint_in_print", None, "high",
  r"$\overline f=f'_{(K)}$", r"$f=f'_{(K)}$",
  "The morphism of (iii) is f̄; the bar is missing in the print. The TeX silently corrects; the fix restores "
  "the printed reading.",
  corrected=r"$\overline f=f'_{(K)}$")
f(82, "proof of (4.8.8), end: '(I, 5.3.12)'", "bold I", "(I, 5.3.12)",
  "convention", 2, "high", r"(I, 5.3.12)", r"(\textbf{I}, 5.3.12)", "")
f(82, "proof of (4.8.8), (i): 'par fidèle platitude (0_I, 6.4.1)'", "bold 0", "$(0_{\\mathrm I},6.4.1)$",
  "convention", 2, "high", r"$(0_{\mathrm I},6.4.1)$", r"$(\mathbf{0}_{\mathrm I},6.4.1)$", "")
f(82, "proof of (4.8.8), last line: 'et l'on a évidemment v̄ = v'⊗1_{K'}'",
  "v̄ = v'⊗1_{K'} (5x crop)", "\\overline v=v'\\otimes1_{K'} (same)", "misprint_in_print", None, "medium",
  None, None,
  "The TeX keeps the printed reading. v' : M_(K') → N_(K') and v̄ : M_(K) → N_(K), so v̄ = v'⊗1_K (extension "
  "from K' to K, as with p'⊗1_K three lines earlier).",
  corrected=r"\overline v=v'\otimes1_K")
f(82, "Corollaire (4.8.10), l. 1: 'Les notations étant celles de (4.8.9), soit'",
  "(4.8.9) upright inside the italic statement", "(4.8.9) (italic in the environment)",
  "convention", 6, "high",
  r"celles de (4.8.9)", r"celles de \textup{(4.8.9)}", "")


# ---------------------------------------------------------------- page 83
f(83, "proof of (4.8.12): 'mais comme Z̄ est un sous-préschéma fermé de (X×_kY)_(K)'",
  "'fermé' italic", "fermé (roman)", "italics", None, "high",
  r"fermé de¶$(X\times_kY)_{(K)}$", r"\emph{fermé} de¶$(X\times_kY)_{(K)}$", "")
f(83, "proof of (4.8.12): '(X×_kY)_(K) (I, 5.4.3)'", "bold I", "(I, 5.4.3)",
  "convention", 2, "high", r"(I, 5.4.3)", r"(\textbf{I}, 5.4.3)", "")
f(83, "Proposition (4.8.13), l. 1-2: 'de (4.8.11) (resp. (4.8.9), (4.8.10), (4.8.12))'",
  "the references and 'resp.' upright inside the italic statement",
  "all italic in the environment", "convention", 6, "high",
  r"de (4.8.11) (resp. (4.8.9), (4.8.10), (4.8.12))",
  r"de \textup{(4.8.11) (resp. (4.8.9), (4.8.10), (4.8.12))}", "Enlarged crop of the whole statement.")
f(83, "Proposition (4.8.13), l. 2: 'soit de type fini sur k (resp. que X soit de type fini'",
  "'(resp.' upright inside the italic statement", "(resp. (italic in the environment)",
  "convention", 6, "high",
  r"sur $k$ (resp. que $X$ soit de", r"sur $k$ \textup{(resp.} que $X$ soit de", "")
f(83, "Proposition (4.8.13), l. 3: 'et F cohérent, resp. que X'",
  "'resp.' upright inside the italic statement", "resp. (italic in the environment)",
  "convention", 6, "high",
  r"cohérent, resp. que", r"cohérent, \textup{resp.} que", "")
f(83, "Proposition (4.8.13), l. 3: 'F et G cohérents, resp. que X et Y'",
  "'resp.' upright inside the italic statement", "resp. (italic in the environment)",
  "convention", 6, "high",
  r"cohérents, resp. que", r"cohérents, \textup{resp.} que", "")
f(83, "Proposition (4.8.13), l. 4: 'soient de type fini sur k). Alors'",
  "the closing parenthesis of the '(resp. ...)' clause upright (5x crop)", ") (italic in the environment)",
  "convention", 6, "medium",
  r"sur $k$). Alors", r"sur $k$\textup{)}. Alors", "")
f(83, "Proposition (4.8.13), l. 4: 'de Z̄ (resp. de H̄, de ū, de f̄)'",
  "'(resp.' upright inside the italic statement", "(resp. (italic in the environment)",
  "convention", 6, "high",
  r"$\overline Z$ (resp. de", r"$\overline Z$ \textup{(resp.} de", "")
f(83, "Proposition (4.8.13), l. 4: '... de f̄) est une extension'",
  "the closing parenthesis upright (5x crop)", ") (italic in the environment)",
  "convention", 6, "medium",
  r"de $\overline f$) est", r"de $\overline f$\textup{)} est", "")
f(83, "proof of (4.8.13): 'vérifiant les conditions a), b) ou c)'",
  "a), b), c) italic", "a), b), c) (roman)", "italics", None, "high",
  r"conditions a), b) ou c)", r"conditions \emph{a)}, \emph{b)} ou \emph{c)}", "")
f(83, "proof of (4.8.13): 'tels que n_j = Σ_i(m_i⊗1)b_ij, où b_ij∈A_(K); chaque b_ij'",
  "in the running text, with the words 'où' in the text line",
  "displayed with \\[ ... \\], 'où' inside the display as \\text", "other", None, "high",
  r"\[¶n_j=\sum_i(m_i\otimes1)b_{ij},¶\quad\text{où }b_{ij}\in A_{(K)};¶\]",
  r"$n_j=\sum_i(m_i\otimes1)b_{ij}$,¶où $b_{ij}\in A_{(K)}$;",
  "Formula displayed where the print has it inline; the connecting word 'où' returns to the text.")
f(83, "proof of (4.8.13): 's'écrit d'ailleurs b_ij = Σ_h a_ijh⊗c_ijh, où a_ijh∈A et c_ijh∈K; il est clair'",
  "in the running text, 'où' and 'et' in the text line",
  "displayed with \\[ ... \\], 'où' and 'et' inside the display as \\text", "other", None, "high",
  r"\[¶b_{ij}=\sum_h a_{ijh}\otimes c_{ijh},¶\quad\text{où }a_{ijh}\in A\text{ et }c_{ijh}\in K;¶\]",
  r"$b_{ij}=\sum_h a_{ijh}\otimes c_{ijh}$,¶où $a_{ijh}\in A$ et $c_{ijh}\in K$;",
  "Formula displayed where the print has it inline; 'où' and 'et' return to the text.")
f(83, "proof of (4.8.14): 'égal à (X_(K))_red (I, 5.1.8)'", "bold I", "(I, 5.1.8)",
  "convention", 2, "high", r"(I, 5.1.8)", r"(\textbf{I}, 5.1.8)", "")
f(83, "end of p. 83: Remarques (4.8.15) (i) 'Par exemple, soient k_0 | un corps de caractéristique p>0' "
      "(sentence runs over the page break)",
  "p. 84 continues the sentence flush left (no new paragraph)",
  "blank line after 'soient $k_0$' before \\oldpage[IV-2]{84} (paragraph break inside the sentence)",
  "other", None, "high",
  r"soient $k_0$¶¶", r"soient $k_0$¶",
  "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 84 entry "
  "that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 84
f(84, "top of p. 84: 'soient k_0 | un corps de caractéristique p>0'",
  "continues the sentence of p. 83 flush left (no new paragraph)",
  "blank line after \\oldpage[IV-2]{84} (paragraph break inside the sentence)",
  "other", None, "high",
  r"\oldpage[IV-2]{84}¶¶", r"\oldpage[IV-2]{84}¶",
  "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 83 entry ('soient $k_0$' + blank line, "
  "before the marker).")
f(84, "heading 4.9", "'4.9. Corps de définition d'une partie d'un préschéma.' (final full stop)",
  "\\subsection{Corps de définition d'une partie d'un préschéma}", "punctuation", None, "high",
  r"d'une partie d'un préschéma}", r"d'une partie d'un préschéma.}",
  "GLOBAL_ISSUES 43/58 pattern, as heading 4.8 on p. 80.")
f(84, "Proposition (4.9.1), label a)", "a) upright", "\\item[a)] (italic in the proposition environment)",
  "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", "")
f(84, "Proposition (4.9.1), label b)", "b) upright", "\\item[b)] (italic in the proposition environment)",
  "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", "")
f(84, "Proposition (4.9.1) b): 'La partie ouverte Ū = X_(K)—T̄'", "long dash for the set difference",
  "minus sign", "convention", 7, "high",
  r"X_{(K)}-\overline T", r"X_{(K)}\setmin\overline T",
  "EGA_IV2_FR.tex provides \\setmin as '-' (FIX_POLICY 2.7: the long-dash definition waits for the global pass).")
f(84, "Proposition (4.9.1), label b')", "b') upright", "\\item[b')] (italic in the proposition environment)",
  "convention", 6, "high", r"\item[b')]", r"\item[\textup{b')}]", "")
f(84, "Proposition (4.9.1), label c)", "c) upright", "\\item[c)] (italic in the proposition environment)",
  "convention", 6, "high", r"\item[c)]", r"\item[\textup{c)}]", "")
f(84, "proof of (4.9.1): 'g^{-1}(X_(K')—T')'", "long dash for the set difference", "minus sign",
  "convention", 7, "high",
  r"X_{(K')}-T')", r"X_{(K')}\setmin T')", "As above (\\setmin pending).")
f(84, "proof of (4.9.1): '= X_(K)—g^{-1}(T')'", "long dash for the set difference", "minus sign",
  "convention", 7, "high",
  r"=X_{(K)}-g^{-1}", r"=X_{(K)}\setmin g^{-1}", "As above (\\setmin pending).")
f(84, "proof of (4.9.1): 'pour toute partie T' de X_(K'), a), b) et b') sont équivalentes'",
  "a), b), b') italic", "a), b), b') (roman)", "italics", None, "high",
  r"a), b) et b') sont", r"\emph{a)}, \emph{b)} et \emph{b')} sont", "")
f(84, "proof of (4.9.1): 'on sait que T̄ = g^{-1}(T') (I, 4.4.1)'", "bold I", "(I, 4.4.1)",
  "convention", 2, "high", r"(I, 4.4.1)", r"(\textbf{I}, 4.4.1)", "")
f(84, "proof of (4.9.1): 'pour voir que a) entraîne c), il suffit'",
  "a), c) italic", "a), c) (roman)", "italics", None, "high",
  r"que a) entraîne c),", r"que \emph{a)} entraîne \emph{c)},", "")
f(84, "proof of (4.9.1): 'ayant pour espace sous-jacent T' (I, 5.2.1)'", "bold I", "(I, 5.2.1)",
  "convention", 2, "high", r"(I, 5.2.1)", r"(\textbf{I}, 5.2.1)", "")
f(84, "proof of (4.9.1), end: 'et de prendre Z̄ = Z'⊗_K K''",
  "Z̄ = Z'⊗_K K' (subscript K, then K'; 5x crop)", "\\overline Z=Z'\\otimes_{K'}K",
  "misprint_in_print", None, "high",
  r"prendre $\overline Z=Z'\otimes_{K'}K$", r"prendre $\overline Z=Z'\otimes_KK'$",
  "Z' lives over K' and Z̄ is its extension to K, as written correctly earlier in the same proof "
  "(Z̄ = Z'⊗_{K'}K). The TeX silently corrects; the fix restores the printed reading.",
  corrected=r"prendre $\overline Z=Z'\otimes_{K'}K$")
f(84, "Corollaire (4.9.2), l. 1: 'Avec les notations de (4.9.1), supposons'",
  "(4.9.1) upright inside the italic statement", "(4.9.1) (italic in the environment)",
  "convention", 6, "high",
  r"notations de (4.9.1), supposons", r"notations de \textup{(4.9.1)}, supposons", "")
f(84, "Remarque (4.9.3): 'que si elle est déjà définie sur k : en effet'",
  "colon after 'sur k' (5x crop)", "semicolon", "punctuation", None, "high",
  r"définie sur $k$;", r"définie sur $k$:", "")


# ---------------------------------------------------------------- checks and output
def main():
    bad = 0
    for d in F:
        if d["fix"] is None:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        for s in (old, new):
            if any(ord(c) < 32 and c != "\n" for c in s):
                print("CONTROL CHARACTER", d["page"], repr(s)); bad += 1
        t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
        n = t.count(old)
        if n != 1:
            print(f"p{d['page']}: old occurs {n} times: {old!r}"); bad += 1
        if old == new:
            print("NO-OP", d["page"], repr(old)); bad += 1
    # sequential application in list order: every old must still occur exactly once when its turn comes
    cur = {}
    for d in F:
        if d["fix"] is None:
            continue
        p = d["page"]
        if p not in cur:
            cur[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
        n = cur[p].count(d["fix"]["old"])
        if n != 1:
            print(f"SEQUENTIAL p{p}: old occurs {n} times: {d['fix']['old']!r}"); bad += 1
        else:
            cur[p] = cur[p].replace(d["fix"]["old"], d["fix"]["new"], 1)
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    c = Counter()
    for d in F:
        k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
        c[(d["page"], k)] += 1
    for p in sorted({d["page"] for d in F}):
        print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
    print("entries", len(F), "problems", bad)


if __name__ == "__main__":
    main()
