"""Build findings_235_239.json and check every fix's 'old' (unique per page, no overlaps)."""
import json
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUT = RUN / "findings_235_239.json"

F = []


def add(page, where, scan, tex, kind, convention, confidence, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def fx(old, new):
    return {"old": old, "new": new}


WAVY = "GLOBAL_ISSUES 33; not convention 3."
SETMIN = "\\setmin is defined in the IV-3 preamble."
REF6 = "Reference printed upright inside the italic statement."
K1 = "The TeX has bold upright \\mathbf{k}; on the line the print's k is bold italic (subscript k stays \\mathbf{k}, GLOBAL_ISSUES 48)."

# ---------------- page 235 ----------------
add(235, "proof of (15.5.6), l. 3: 'implique que f est plat aux points de f^{-1}(a)'",
    "'plat' italic (crop p235_plat.png)", "'plat' upright", "italics", None, "high",
    fx("est plat aux points", "est \\emph{plat} aux points"))
add(235, "proof of (15.5.6), l. 8: 'donc Spec(O_x)—{x} est réduit à un point'",
    "long dash for the set difference", "\\operatorname{Spec}(\\mathcal O_x)-\\{x\\}", "convention", 7, "high",
    fx("(\\mathcal O_x)-\\{x\\}$ est réduit", "(\\mathcal O_x)\\setmin\\{x\\}$ est réduit"), SETMIN)
add(235, "proof of (15.5.6), l. 9: 'et a fortiori est connexe'",
    "'a fortiori' italic (crop p235_fortiori.png)", "'a fortiori' upright", "italics", None, "high",
    fx("et a fortiori est", "et \\emph{a fortiori} est"))
add(235, "proof of (15.5.6), last line: 'que Spec(O_x)—{x} est connexe'",
    "long dash for the set difference", "\\operatorname{Spec}(\\mathcal O_x)-\\{x\\}", "convention", 7, "high",
    fx("(\\mathcal O_x)-\\{x\\}$ est connexe", "(\\mathcal O_x)\\setmin\\{x\\}$ est connexe"), SETMIN)
add(235, "Proposition (15.5.7), l. 4: 'géométriquement réduit sur k(y)'",
    "bold italic k (crop p235_kz.png)", "\\mathbf{k}(y)", "convention", 1, "high",
    fx("sur $\\mathbf{k}(y)$", "sur $\\boldsymbol{k}(y)$"), K1)
add(235, "Proposition (15.5.7), l. 4: 'réduit sur k(y) (4.6.2). Alors'",
    "'(4.6.2)' upright (crop p235_kz.png)", "italic (proposition environment)", "convention", 6, "high",
    fx("(4.6.2)", "\\textup{(4.6.2)}"), REF6)
add(235, "Proposition (15.5.7), l. 4: 'la fonction z⇝n(z) est constante'",
    "wavy arrow (crop p235_kz.png)", "\\mapsto", "symbol", None, "high",
    fx("$z\\mapsto n(z)$ est constante", "$z\\leadsto n(z)$ est constante"), WAVY)
add(235, "proof of (15.5.7), l. 1: 'de l'énoncé, z⇝n(z) est semi-continue'",
    "wavy arrow (crop p235_arrow2.png)", "\\mapsto", "symbol", None, "high",
    fx("$z\\mapsto n(z)$ est semi-continue", "$z\\leadsto n(z)$ est semi-continue"), WAVY)
add(235, "proof of (15.5.7), 2nd paragraph, l. 10: 'on a aussi f^{-1}(y)≠0 (II, 7.2.1)'",
    "'f^{-1}(y)≠o' with an old-style zero, where the two neighbouring uses (and X≠∅ on the next line) have the empty-set sign ∅ (crop p235_neq.png)",
    "f^{-1}(y)\\ne\\varnothing", "misprint_in_print", None, "high",
    fx("$f^{-1}(y)\\ne\\varnothing$ (\\textbf{II}", "$f^{-1}(y)\\ne 0$ (\\textbf{II}"),
    "The TeX silently corrects the printed 0 to the empty set.",
    corrected="f^{-1}(y)\\ne\\varnothing")
add(235, "proof of (15.5.7), 2nd paragraph, l. 13: 'le préschéma f^{-1}(y) est réduit (4.6.1)'",
    "'réduit' italic (crop p235_reduit.png)", "'réduit' upright", "italics", None, "high",
    fx("est réduit (4.6.1)", "est \\emph{réduit} (4.6.1)"))
add(235, "Remarque (15.5.8), l. 4: 'la restriction de f à X—{x'}'",
    "long dash for the set difference", "X-\\{x'\\}", "convention", 7, "high",
    fx("$X-\\{x'\\}$", "$X\\setmin\\{x'\\}$"), SETMIN)

# ---------------- page 236 ----------------
add(236, "Proposition (15.5.9), (i), l. 1: 'la fonction y⇝n(y)'",
    "wavy arrow (crop p236_egale.png)", "\\mapsto", "symbol", None, "high",
    fx("quasi-fini, la fonction $y\\mapsto n(y)$", "quasi-fini, la fonction $y\\leadsto n(y)$"), WAVY)
add(236, "Proposition (15.5.9), (i), l. 1-2: '(égale alors au nombre géométrique des points de f^{-1}(y))'",
    "the whole parenthesis roman inside the italic statement (crop p236_egale.png)",
    "italic (proposition environment)", "convention", 6, "high",
    fx("(égale alors au nombre géométrique des points de $f^{-1}(y)$)",
       "\\textup{(égale alors au nombre géométrique des points de $f^{-1}(y)$)}"))
add(236, "Proposition (15.5.9), (ii), l. 1: 'la fonction y⇝n(y)'",
    "wavy arrow (crop p236_ii.png)", "\\mapsto", "symbol", None, "high",
    fx("propre, la fonction $y\\mapsto n(y)$", "propre, la fonction $y\\leadsto n(y)$"), WAVY)
add(236, "Proposition (15.5.9), (ii), l. 2: 'géométriquement réduit sur k(y_0)'",
    "bold italic k (crop p236_ii.png)", "\\mathbf{k}(y_0)", "convention", 1, "high",
    fx("$\\mathbf{k}(y_0)$", "$\\boldsymbol{k}(y_0)$"), K1)
add(236, "heading 15.6: 'Composantes connexes des fibres le long d'une section.'",
    "final full stop", "no full stop", "punctuation", None, "high",
    fx("le long d'une section}", "le long d'une section.}"),
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(236, "Proposition (15.6.1), l. 2: 'une Y-section de X (I, 2.5.5)'",
    "'(I, 2.5.5)' upright, bold upright I (crop p236_I255.png)",
    "italic (proposition environment); \\textbf{I} comes out bold italic", "convention", 6, "high",
    fx("(\\textbf{I}, 2.5.5)", "\\textup{(\\textbf{I}, 2.5.5)}"), REF6)
add(236, "Proposition (15.6.1), l. 4: 'Soient y un point de Y, v' une générisation de y dans Y'",
    "'v'' : an italic v with prime, no trace of a descender; the y of 'de y dans' on the same line has the long tail (crops p236_vprime_big.png, p236_y_dans_big.png)",
    "$y'$", "misprint_in_print", None, "high",
    fx("$y'$ une générisation", "$v'$ une générisation"),
    "The TeX silently corrects the print's v' to y' (y' is the point used in (i), (ii) and the proof).",
    corrected="$y'$ une générisation")
add(236, "Proposition (15.6.1), (i), l. 2: '(ce qui sera le cas si X^0_{y'} est irréductible)'",
    "the parenthesis roman, with only 'irréductible' italic (crop p236_cequi.png)",
    "all italic (proposition environment)", "convention", 6, "high",
    fx("(ce qui sera le cas si $X_{y'}^0$ est irréductible)",
       "\\textup{(ce qui sera le cas si $X_{y'}^0$ est \\emph{irréductible})}"),
    "Roman words in the italic statement; 'irréductible' is emphasized by italics inside them (\\emph inside \\textup).")
add(236, "Proposition (15.6.1), (ii): 'les deux membres de (15.6.1.1) sont égaux'",
    "'(15.6.1.1)' upright (crop p236_ref15611.png)", "italic (proposition environment)", "convention", 6, "high",
    fx("membres de (15.6.1.1) sont égaux, alors", "membres de \\textup{(15.6.1.1)} sont égaux, alors"), REF6)
add(236, "proof of (15.6.1), (i), l. 4-5: 'que l'on a dim_{g(y)}(Z̄∩f^{-1}(y))≥dim(Z); mais les composantes'",
    "the formula is set in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    fx("\\[\n  \\dim_{g(y)}(\\overline Z\\cap f^{-1}(y))\\geqslant\\dim(Z)~;\n\\]",
       "$\\dim_{g(y)}(\\overline Z\\cap f^{-1}(y))\\geqslant\\dim(Z)$~;"),
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost.")
add(236, "proof of (15.6.1), (ii), l. 2: 'on a nécessairement dim_{g(y)}(Z̄∩f^{-1}(y))=dim_{g(y)}(X^0_y); si X^0_y'",
    "the formula is set in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    fx("\\[\n  \\dim_{g(y)}(\\overline Z\\cap f^{-1}(y))=\\dim_{g(y)}(X_y^0)~;\n\\]",
       "$\\dim_{g(y)}(\\overline Z\\cap f^{-1}(y))=\\dim_{g(y)}(X_y^0)$~;"),
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost.")

# ---------------- page 237 ----------------
add(237, "Corollaire (15.6.2), l. 1: 'Avec les notations de (15.6.1)'",
    "'(15.6.1)' upright", "italic (corollary environment)", "convention", 6, "high",
    fx("notations de (15.6.1), supposons en outre", "notations de \\textup{(15.6.1)}, supposons en outre"), REF6)
add(237, "Corollaire (15.6.2), l. 2: 'la fonction z⇝dim(X^0_z) est semi-continue supérieurement'",
    "wavy arrow (crop p237_cor.png)", "\\mapsto", "symbol", None, "high",
    fx("$z\\mapsto\\dim(X_z^0)$ est semi-continue", "$z\\leadsto\\dim(X_z^0)$ est semi-continue"), WAVY)
add(237, "proof of (15.6.2), l. 5: 'la fonction z⇝dim(X^0_z) est localement constructible'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    fx("$z\\mapsto\\dim(X_z^0)$ est localement", "$z\\leadsto\\dim(X_z^0)$ est localement"), WAVY)
add(237, "Proposition (15.6.3), l. 1: 'Avec les notations de (15.6.1)'",
    "'(15.6.1)' upright", "italic (proposition environment)", "convention", 6, "high",
    fx("notations de (15.6.1), supposons que", "notations de \\textup{(15.6.1)}, supposons que"), REF6)
add(237, "Proposition (15.6.3), l. 2: 'géométriquement irréductible (4.5.2)'",
    "'(4.5.2)' upright", "italic (proposition environment)", "convention", 6, "high",
    fx("(4.5.2)", "\\textup{(4.5.2)}"), REF6)
add(237, "Proposition (15.6.3), l. 2: 'la fonction z⇝dim(X^0_z) soit constante'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    fx("$z\\mapsto\\dim(X_z^0)$ soit constante", "$z\\leadsto\\dim(X_z^0)$ soit constante"), WAVY)
add(237, "proof of (15.6.3), l. 5: 'l'hypothèse faite sur les X^0_z implique que'",
    "subscript z (crop p237_Xz.png)", "$X_y^0$", "formula", None, "high",
    fx("sur les $X_y^0$ implique", "sur les $X_z^0$ implique"),
    "The print's index z is a free index, not a misprint.")
add(237, "proof of (15.6.3), l. 6: 'X'^0_t=X^0_y⊗_{k(y)}k(t) et X'^0_{t'}=X^0_{y'}⊗_{k(y')}k(t'), et que'",
    "both formulas set in the running text, joined by 'et' (crop p237_ktensor.png)",
    "one display \\[ ... \\quad\\text{et}\\quad ... \\]", "other", None, "high",
    fx("\\[\n  X_t^{\\prime 0}=X_y^0\\otimes_{\\mathbf{k}(y)}\\mathbf{k}(t)\n  \\quad\\text{et}\\quad\n  X_{t'}^{\\prime 0}=X_{y'}^0\\otimes_{\\mathbf{k}(y')}\\mathbf{k}(t'),\n\\]",
       "$X_t^{\\prime 0}=X_y^0\\otimes_{\\mathbf{k}(y)}\\boldsymbol{k}(t)$ et\n$X_{t'}^{\\prime 0}=X_{y'}^0\\otimes_{\\mathbf{k}(y')}\\boldsymbol{k}(t')$,"),
    "Formulas displayed where the print has them inline (GLOBAL_ISSUES 21). One edit, which also writes the two line-level k bold italic (the two convention-1 entries below); the subscript k(y), k(y') are bold upright in the print and stay \\mathbf{k}.")
add(237, "proof of (15.6.3), l. 6: '... ⊗_{k(y)} k(t)'",
    "bold italic k (crop p237_ktensor.png)", "\\mathbf{k}(t)", "convention", 1, "high", None,
    "Included in the display edit above (written \\boldsymbol{k}(t) there).")
add(237, "proof of (15.6.3), l. 6: '... ⊗_{k(y')} k(t')'",
    "bold italic k (crop p237_ktensor.png)", "\\mathbf{k}(t')", "convention", 1, "high", None,
    "Included in the display edit above (written \\boldsymbol{k}(t') there).")
add(237, "Proposition (15.6.4), l. 1: 'Sous les hypothèses générales de (15.6.1)'",
    "'(15.6.1)' upright", "italic (proposition environment)", "convention", 6, "high",
    fx("générales de (15.6.1)", "générales de \\textup{(15.6.1)}"), REF6)
add(237, "Proposition (15.6.4), l. 2: 'soit géométriquement réduit sur k(y)'",
    "bold italic k (crop p237_1564.png)", "\\mathbf{k}(y)", "convention", 1, "high",
    fx("soit géométriquement réduit sur $\\mathbf{k}(y)$", "soit géométriquement réduit sur $\\boldsymbol{k}(y)$"), K1)
add(237, "Proposition (15.6.4), l. 2: 'réduit sur k(y) (4.6.2)'",
    "'(4.6.2)' upright (crop p237_1564.png)", "italic (proposition environment)", "convention", 6, "high",
    fx("(4.6.2)", "\\textup{(4.6.2)}"), REF6)
add(237, "Proposition (15.6.4), l. 4: 'X^0_y est géométriquement réduit sur k(y)'",
    "bold italic k (crop p237_1564.png)", "\\mathbf{k}(y)", "convention", 1, "high",
    fx("est géométriquement réduit sur $\\mathbf{k}(y)$", "est géométriquement réduit sur $\\boldsymbol{k}(y)$"), K1)
add(237, "proof of (15.6.4), l. 4: 'pour 0≤i≤n—1'",
    "long dash for the minus sign, much longer than the minus of the subscripts Z_{i-1} (crop p237_nminus1.png)",
    "n-1", "convention", 7, "medium",
    fx("i\\leqslant n-1$", "i\\leqslant n\\setmin 1$"),
    "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin as for convention 7. The subscript minus signs (Z_{i-1}, U_{i-1}) are ordinary.")
add(237, "proof of (15.6.4), l. 11: 'si X'=W∩g^{-1}(V), la restriction de f à X' est de type fini'",
    "'g^{-1}(V)' (crop p237_gV.png)", "f^{-1}(V)", "misprint_in_print", None, "high",
    fx("$X'=W\\cap f^{-1}(V)$", "$X'=W\\cap g^{-1}(V)$"),
    "The TeX silently corrects the print. V is an open set of Y, so g^{-1}(V) (g : Y→X) makes no sense; X' must be the open set W∩f^{-1}(V) of X.",
    corrected="$X'=W\\cap f^{-1}(V)$")
add(237, "last line of the page / first line of p. 238: '... et U_{i-1}∩Z_{i-1} | se rencontrent pour 2≤i≤n'",
    "the sentence runs on across the page break", "blank line before \\oldpage[IV-3]{238} (paragraph break)", "marker", None, "high",
    fx("U_{i-1}\\cap Z_{i-1}$\n\n", "U_{i-1}\\cap Z_{i-1}$\n"),
    "Marker position itself is right (GLOBAL_ISSUES 20); no blank line after the marker.")

# ---------------- page 238 ----------------
add(238, "proof of (15.6.4), p. 238 l. 13-14: 'p_y(v(y))=x, p_{y'}(v(y'))=x', de sorte que v(y') est une générisation de v(y), ... que v(y') appartient à p_{y'}^{-1}(X^0_{y'})'",
    "v(y), v(y') (five times)", "same (v(y), v(y'))", "misprint_in_print", None, "medium",
    None,
    "The TeX keeps the printed reading. v is a Y'-section of X' and y, y' are points of Y, not of Y'=Spec(A); the points meant are the closed point z and the generic point z' of Y' (p_y(v(z))=x, p_{y'}(v(z'))=x'). Possibly an authors' slip rather than a compositor's; check the errata before correcting.",
    corrected="p_y(v(z))=x, p_{y'}(v(z'))=x', de sorte que v(z') est une générisation de v(z), ... prouver que v(z') appartient à p_{y'}^{-1}(X_{y'}^0)")
add(238, "proof of (15.6.4), p. 238 l. 15: 'géométriquement réduit sur k(z)'",
    "bold italic k", "\\mathbf{k}(z)", "convention", 1, "high",
    fx("$\\mathbf{k}(z)$", "$\\boldsymbol{k}(z)$"), K1)
add(238, "proof of (15.6.4), last paragraph, l. 2: 'Comme f^{-1}(y)—X^0_y est alors fermé'",
    "long dash for the set difference (crop p238_dans.png)", "f^{-1}(y)-X_y^0", "convention", 7, "high",
    fx("Comme $f^{-1}(y)-X_y^0$", "Comme $f^{-1}(y)\\setmin X_y^0$"), SETMIN)
add(238, "proof of (15.6.4), last paragraph, l. 2-3: 'est alors fermé dans X'",
    "'dans' italic, 'fermé' roman (crop p238_dans.png)", "'dans' upright", "italics", None, "high",
    fx("fermé dans $X$", "fermé \\emph{dans} $X$"))
add(238, "proof of (15.6.4), last paragraph, l. 3: 'l'ouvert X—(f^{-1}(y)—X^0_y)', first dash",
    "long dash for the set difference (crop p238_dans.png)", "X-(f^{-1}(y)-X_y^0)", "convention", 7, "high",
    fx("$X-(f^{-1}", "$X\\setmin(f^{-1}"), SETMIN + " Disjoint from the next entry.")
add(238, "proof of (15.6.4), last paragraph, l. 3: 'l'ouvert X—(f^{-1}(y)—X^0_y)', second dash",
    "long dash for the set difference (crop p238_dans.png)", "X-(f^{-1}(y)-X_y^0)", "convention", 7, "high",
    fx("(y)-X_y^0)$", "(y)\\setmin X_y^0)$"), SETMIN)
add(238, "proof of (15.6.4), last paragraph, l. 6: 'on peut supposer X connexe.'",
    "'connexe' italic (crop p238_ital.png)", "'connexe' upright", "italics", None, "high",
    fx("supposer $X$ connexe.", "supposer $X$ \\emph{connexe}."))
add(238, "proof of (15.6.4), last paragraph, l. 8: 'et a fortiori réduit'",
    "'a fortiori réduit' italic, both words (crop p238_ital.png)", "\\emph{a fortiori} réduit", "italics", None, "high",
    fx("\\emph{a fortiori} réduit", "\\emph{a fortiori réduit}"))
add(238, "proof of (15.6.4), last paragraph, l. 7: 'géométriquement réduit sur k(y')'",
    "bold italic k (crop p238_ital.png)", "\\mathbf{k}(y')", "convention", 1, "high",
    fx("$\\mathbf{k}(y')$", "$\\boldsymbol{k}(y')$"), K1)
add(238, "proof of (15.6.4), last paragraph, l. 8: 'comme en outre f est ouvert aux points de f^{-1}(y)'",
    "'ouvert' italic (crop p238_ital.png)", "'ouvert' upright", "italics", None, "high",
    fx("$f$ est ouvert aux", "$f$ est \\emph{ouvert} aux"))
add(238, "Corollaire (15.6.5), l. 4: 'géométriquement réduit sur k(y), X^0 est un voisinage'",
    "bold italic k", "\\mathbf{k}(y)", "convention", 1, "high",
    fx("$\\mathbf{k}(y)$, $X^0$", "$\\boldsymbol{k}(y)$, $X^0$"), K1)
add(238, "Corollaire (15.6.5), l. 4: 'si f est réduit (6.8.1)'",
    "'(6.8.1)' upright (crop p238_681.png)", "italic (corollary environment)", "convention", 6, "high",
    fx("réduit (6.8.1)", "réduit \\textup{(6.8.1)}"), REF6)
add(238, "proof of (15.6.5), l. 3: 'f=(f_0)_{(Y)} ((8.9.1) et (11.2.7))'",
    "'((8.9.1) et (11.2.7))', each number in its own parentheses (crop p238_refs.png)", "(8.9.1 et 11.2.7)",
    "punctuation", None, "high",
    fx("(8.9.1 et 11.2.7)", "((8.9.1) et (11.2.7))"))
add(238, "proof of (15.6.5), l. 7: 'X^0_y est géométriquement réduit sur k(y) entraîne'",
    "bold italic k", "\\mathbf{k}(y)", "convention", 1, "high",
    fx("$\\mathbf{k}(y)$ entraîne", "$\\boldsymbol{k}(y)$ entraîne"), K1)
add(238, "proof of (15.6.5), l. 8: 'géométriquement réduit sur k(y_0) (4.6.10)'",
    "bold italic k", "\\mathbf{k}(y_0)", "convention", 1, "high",
    fx("$\\mathbf{k}(y_0)$", "$\\boldsymbol{k}(y_0)$"), K1)
add(238, "last line of the page / first line of p. 239: '... au cas où on suppose | en outre Y noethérien'",
    "the sentence runs on across the page break", "blank line before \\oldpage[IV-3]{239} (paragraph break)", "marker", None, "high",
    fx("on suppose\n\n", "on suppose\n"),
    "Marker position itself is right (GLOBAL_ISSUES 20); no blank line after the marker.")

# ---------------- page 239 ----------------
add(239, "proof of (15.6.5), l. 1: 'en outre Y noethérien'",
    "'noethérien' italic", "'noethérien' upright", "italics", None, "high",
    fx("$Y$ noethérien~; comme", "$Y$ \\emph{noethérien}~; comme"))
add(239, "Proposition (15.6.6), l. 2: 'et f localement de type fini, ou que f soit'",
    "'ou' roman inside the italic statement (crop p239_ou.png)", "italic (proposition environment)", "convention", 6, "high",
    fx("fini, ou que", "fini, \\textup{ou} que"))
add(239, "Proposition (15.6.6), (i): 'La fonction y⇝dim(X^0_y)'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    fx("La fonction $y\\mapsto", "La fonction $y\\leadsto"), WAVY)
add(239, "Proposition (15.6.6), (ii), l. 1: 'Si la fonction y⇝dim(X^0_y)'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    fx("Si la fonction $y\\mapsto", "Si la fonction $y\\leadsto"), WAVY)
add(239, "Proposition (15.6.6), (ii), l. 3: 'géométriquement réduit sur k(y_0) au point x_0, f est plat'",
    "bold italic k (crop p239_k_ii.png)", "\\mathbf{k}(y_0)", "convention", 1, "high",
    fx("$\\mathbf{k}(y_0)$ au point $x_0$, $f$", "$\\boldsymbol{k}(y_0)$ au point $x_0$, $f$"), K1)
add(239, "Proposition (15.6.6), (iii), l. 2: 'en outre que l'une des conditions suivantes'",
    "'l'une' roman inside the italic statement (crop p239_lune.png)", "italic (proposition environment)", "convention", 6, "high",
    fx("que l'une des", "que \\textup{l'une} des"))
add(239, "Proposition (15.6.6), (iii) α): 'géométriquement réduite sur k(y_0) au point g(y_0)'",
    "bold italic k (crop p239_k_alpha.png)", "\\mathbf{k}(y_0)", "convention", 1, "high",
    fx("réduite sur $\\mathbf{k}(y_0)$", "réduite sur $\\boldsymbol{k}(y_0)$"), K1)
add(239, "Proposition (15.6.6), (iii), last line: 'Alors la fonction y⇝dim(X^0_y)'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    fx("Alors la fonction $y\\mapsto", "Alors la fonction $y\\leadsto"), WAVY)
add(239, "Proposition (15.6.6), (iv), l. 1: 'tels que la fonction y⇝dim(X^0_y)'",
    "wavy arrow", "\\mapsto", "symbol", None, "high",
    fx("tels que la fonction $y\\mapsto", "tels que la fonction $y\\leadsto"), WAVY)
add(239, "Proposition (15.6.6), (iv), l. 2: 'géométriquement réduit sur k(f(x))'",
    "bold italic k (crop p239_k_iv.png)", "\\mathbf{k}(f(x))", "convention", 1, "high",
    fx("$\\mathbf{k}(f(x))$", "$\\boldsymbol{k}(f(x))$"), K1)
add(239, "proof of (15.6.6), last line: 'géométriquement réduit sur k(y_0) au point x_0 (Y étant'",
    "bold italic k (crop p239_k_proof.png)", "\\mathbf{k}(y_0)", "convention", 1, "high",
    fx("$\\mathbf{k}(y_0)$ au point $x_0$ ($Y$", "$\\boldsymbol{k}(y_0)$ au point $x_0$ ($Y$"), K1)
add(239, "last line of the page / first line of p. 240: '(Y étant toujours supposé | noethérien), comme'",
    "the sentence runs on across the page break", "blank line before \\oldpage[IV-3]{240} (paragraph break)", "marker", None, "high",
    fx("toujours supposé\n\n", "toujours supposé\n"),
    "Marker position itself is right (GLOBAL_ISSUES 20); no blank line after the marker (ega4-15-fr.tex line 878). The pp. 240-244 checker may report the same blank line: apply once.")


def main():
    ok = True
    pages = {}
    for p in sorted({f["page"] for f in F}):
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    spans = {}
    for i, f in enumerate(F):
        fix = f["fix"]
        if fix is None:
            continue
        t = pages[f["page"]]
        n = t.count(fix["old"])
        if n != 1:
            ok = False
            print("NOT UNIQUE", n, f["page"], repr(fix["old"]))
            continue
        a = t.index(fix["old"])
        spans.setdefault(f["page"], []).append((a, a + len(fix["old"]), i))
    for p, s in spans.items():
        s.sort()
        for (a1, b1, i1), (a2, b2, i2) in zip(s, s[1:]):
            if a2 < b1:
                ok = False
                print("OVERLAP p.", p, repr(F[i1]["fix"]["old"]), repr(F[i2]["fix"]["old"]))
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    from collections import Counter
    c = Counter()
    for f in F:
        k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
        c[(f["page"], k)] += 1
    for p in sorted(pages):
        print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
    print("entries", len(F), "OK" if ok else "PROBLEMS")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
