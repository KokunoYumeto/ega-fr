import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_155_159.json"
NL = "¶"  # newline placeholder in the strings below


def fx(old, new):
    if old is None:
        return None
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fx(old, new)}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


NSUP = "The print has n with a raised letter o (the edition's n\\textsuperscript{o}); n$^\\circ$ typesets a ring."
LABEL = "Step label in ordinary roman weight (stem 6 px at 300 dpi against 9 px for the bold I of '(I, 3.6.4)'); ega4-11-fr.tex sets its step labels I)-VI) bold (as pp. 124, 154)."
INL = "Display where the print sets the formula in the running text (GLOBAL_ISSUES 21); no connecting words lost."
C7 = "Convention 7 (\\setmin, defined in the IV-3 preamble)."
C7S = "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as for convention 7."

# ---------------------------------------------------------------- page 155
add(155, "top of page_155.tex: blank line after \\oldpage[IV-3]{155}, before 'précédemment permet' (break 154/155 mid-sentence)",
    "'... le même raisonnement que | précédemment permet de remplacer A' par B'': the page begins mid-sentence, flush left",
    "\\oldpage[IV-3]{155} followed by a blank line", "marker", None, "high", None, None,
    "Same edit as the page-155 entry of findings_150_154.json (with the end-of-page_154.tex blank line), already applied (FIXLOG.jsonl): no second edit here. The marker itself is in the right place.")
add(155, "proof of (11.6.1), l. 2: 'l'anneau local A' intégralement clos, A étant un sous-anneau local'",
    "'intégralement clos' italic", "upright", "italics", None, "high",
    "local $A'$ intégralement clos, $A$", "local $A'$ \\emph{intégralement clos}, $A$")
add(155, "l. 3: 'et par hypothèse A_1 est un anneau local;'", "'local' italic", "upright", "italics", None, "high",
    "est un anneau local~;", "est un anneau \\emph{local}~;")
add(155, "'(Bourbaki, Alg. comm., chap. V, § 2, n° 1, prop. 1)'", "n with raised o", "n$^\\circ$", "symbol", None, "high",
    "n$^\\circ$~1", "n\\textsuperscript{o}~1", NSUP)
add(155, "'Par hypothèse le morphisme Spec(k(y_1))→Spec(k(y))'", "bold italic k in k(y_1)", "plain $k$", "convention", 1, "high",
    "\\operatorname{Spec}(k(y_1))", "\\operatorname{Spec}(\\boldsymbol{k}(y_1))")
add(155, "same formula: '→Spec(k(y))'", "bold italic k in k(y)", "plain $k$", "convention", 1, "high",
    "\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))")
add(155, "'Spec(k(y_1))→Spec(k(y)) est radiciel, d'où l'on conclut'", "'radiciel' italic", "upright", "italics", None, "high",
    "est radiciel, d'où", "est \\emph{radiciel}, d'où")
add(155, "'en outre, on a vu que y_1 est le seul point de Y_1'", "'seul' italic", "upright", "italics", None, "high",
    "$y_1$ est le seul point", "$y_1$ est le \\emph{seul} point")
add(155, "'donc x_1 est le seul point de X_1 dont la projection dans X soit x'", "'seul' italic", "upright", "italics", None, "high",
    "donc $x_1$ est le seul point", "donc $x_1$ est le \\emph{seul} point")
add(155, "step label 'II) Réduction au cas où A et A' sont des anneaux locaux de Z-algèbres ...'",
    "'II)' in ordinary roman weight", "\\textbf{II)}", "font", None, "high",
    "\\noindent\\textbf{II)} \\emph{Réduction", "\\noindent II) \\emph{Réduction", LABEL)
add(155, "step II) heading: '... de Z-algèbres de type fini intégralement closes.'",
    "'intégralement closes' (feminine plural, with 'Z-algèbres')", "'intégralement clos'", "word", None, "high",
    "intégralement clos.}", "intégralement closes.}")
add(155, "step II): 'tels que X=X_αλ×_{Y_αλ}Y, f=f_αλ×1_Y, F=F_αλ⊗_{Y_αλ}Y; si x_αλ est'",
    "the three formulas in the running text, separated by commas", "\\[ ... \\qquad ... \\] display", "other", None, "high",
    "tels que¶\\[¶X=X_{\\alpha\\lambda}\\times_{Y_{\\alpha\\lambda}}Y,¶\\qquad f=f_{\\alpha\\lambda}\\times1_Y,¶\\qquad \\mathcal F=\\mathcal F_{\\alpha\\lambda}\\otimes_{Y_{\\alpha\\lambda}}Y~;¶\\]¶si",
    "tels que¶$X=X_{\\alpha\\lambda}\\times_{Y_{\\alpha\\lambda}}Y$,¶$f=f_{\\alpha\\lambda}\\times1_Y$,¶$\\mathcal F=\\mathcal F_{\\alpha\\lambda}\\otimes_{Y_{\\alpha\\lambda}}Y$~;¶si",
    INL)
add(155, "'X' est limite projective des X_αλ×_{Y_αλ}Y'_μ=X'_αμ, et on a aussi'",
    "X'_{αμ} (double index, as F'_{αμ} in the same line; enlarged crop)", "X'_{\\mu}", "formula", None, "high",
    "Y'_{\\mu}=X'_{\\mu}$", "Y'_{\\mu}=X'_{\\alpha\\mu}$",
    "The print writes X'_μ further on ('projection de x' dans X'_μ'), which the TeX has as printed; only this definition has the double index.")
add(155, "step label 'III) Réduction au cas où le corps résiduel k' de A' est ...'",
    "'III)' in ordinary roman weight", "\\textbf{III)}", "font", None, "high",
    "\\noindent\\textbf{III)} \\emph{Réduction", "\\noindent III) \\emph{Réduction", LABEL)
add(155, "end of page_155.tex: '... du fait que Z est un anneau de | Jacobson; on se réduit ainsi' (break 155/156 mid-sentence)",
    "p. 156 begins mid-sentence with 'Jacobson;', flush left", "blank line after '% IV3_B23_P155_END' before \\oldpage[IV-3]{156}",
    "marker", None, "high",
    "un anneau¶de¶% IV3_B23_P155_END¶¶", "un anneau¶de¶% IV3_B23_P155_END¶",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 156 marker itself is in the right place. APPLY TOGETHER with the p. 156 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- page 156
add(156, "top of page_156.tex: blank line after \\oldpage[IV-3]{156}, before 'Jacobson;'",
    "'Jacobson;' continues the sentence of p. 155", "blank line after the marker", "marker", None, "high",
    "\\oldpage[IV-3]{156}¶¶Jacobson", "\\oldpage[IV-3]{156}¶Jacobson",
    "Apply together with the p. 155 entry (blank line before the marker).")
add(156, "'dont le corps des fractions K_1=K[T]/(R) est une extension séparable de K'", "'séparable' italic", "upright",
    "italics", None, "high", "extension séparable de $K$", "extension \\emph{séparable} de $K$")
add(156, "'on déduit de là que d=det(Tr_{A_1/A}(t^{i+j})) est un élément de A'",
    "formula in the running text, ordinary parentheses", "\\[ d=\\det\\bigl(...\\bigr) \\] display", "other", None, "high",
    "que¶\\[¶d=\\det\\bigl(\\operatorname{Tr}_{A_1/A}(t^{i+j})\\bigr)¶\\]¶est un élément",
    "que¶$d=\\det(\\operatorname{Tr}_{A_1/A}(t^{i+j}))$¶est un élément", INL)
add(156, "'(Bourbaki, Alg. comm., chap. IV, § 2, n° 5, cor. 3 de la prop. 9)'", "n with raised o", "n$^\\circ$", "symbol", None, "high",
    "n$^\\circ$~5", "n\\textsuperscript{o}~5", NSUP)
add(156, "'contiennent mA'_1. Mais A'_1/mA'_1=(A'/mA')⊗_k k_1, et comme k_1'",
    "formula in the running text", "\\[ ... \\] display", "other", None, "high",
    "Mais¶\\[¶A'_1/\\mathfrak m A'_1=(A'/\\mathfrak m A')\\otimes_k k_1,¶\\]¶et comme",
    "Mais¶$A'_1/\\mathfrak m A'_1=(A'/\\mathfrak m A')\\otimes_k k_1$,¶et comme", INL)
add(156, "'(Bourbaki, Alg., chap. VIII, § 7, n° 2, cor. 2 de la prop. 3)'", "n with raised o", "n$^\\circ$", "symbol", None, "high",
    "n$^\\circ$~2", "n\\textsuperscript{o}~2", NSUP)
add(156, "'l'homomorphisme canonique A'_1→∏_{i=1}^r (A'_1)_{n_i} étant lui aussi injectif'",
    "formula in the running text", "\\[ ... \\] display", "other", None, "high",
    "canonique¶\\[¶A'_1\\longrightarrow\\prod_{i=1}^{r}(A'_1)_{\\mathfrak n_i}¶\\]¶étant",
    "canonique¶$A'_1\\longrightarrow\\prod_{i=1}^{r}(A'_1)_{\\mathfrak n_i}$¶étant", INL)
add(156, "'(Bourbaki, Alg. comm., chap. II, § 3, n° 3, th. 1)'", "n with raised o", "n$^\\circ$", "symbol", None, "high",
    "n$^\\circ$~3", "n\\textsuperscript{o}~3", NSUP)
add(156, "'il en est de même du composé A_1→∏_{i=1}^r (A'_1)_{n_i}. Mais A_1 est intègre'",
    "'du composé A_1→∏_{i=1}^r (A'_1)_{n_i}.' (formula)", "'du composé de $A_1$ dans ce produit.' (paraphrase)", "word", None, "high",
    "du composé de $A_1$ dans ce produit.", "du composé $A_1\\to\\prod_{i=1}^{r}(A'_1)_{\\mathfrak n_i}$.",
    "The TeX paraphrases the printed formula.")
add(156, "'F'_1=F'⊗_{Y'}Y'_1 est Y'_1-plat en tous les points de X'_1 au-dessus de x''", "'tous' italic", "upright",
    "italics", None, "high", "plat en tous les points de $X'_1$", "plat en \\emph{tous} les points de $X'_1$")
add(156, "end of page_156.tex / top of p. 157: '... est un O_y-module plat (0_I, 6.2.1). | Mais (F_1)_x1 = ...'",
    "p. 157 begins with 'Mais' flush left: the paragraph continues across the page break", "blank line after '% IV3_B23_P156_END' before \\oldpage[IV-3]{157}",
    "marker", None, "high",
    "6.2.1)$.¶% IV3_B23_P156_END¶¶", "6.2.1)$.¶% IV3_B23_P156_END¶",
    "Spurious paragraph break at the page break (the sentence ends, the paragraph does not); the p. 157 marker is in the right place. APPLY TOGETHER with the p. 157 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- page 157
add(157, "top of page_157.tex: blank line after \\oldpage[IV-3]{157}, before 'Mais (F_1)_x1'",
    "'Mais' flush left (no paragraph indent)", "blank line after the marker", "marker", None, "high",
    "\\oldpage[IV-3]{157}¶¶Mais", "\\oldpage[IV-3]{157}¶Mais",
    "Apply together with the p. 156 entry (blank line before the marker).")
add(157, "step label 'IV) Fin de la démonstration. — On est finalement réduit'",
    "'IV)' in ordinary roman weight (stem 5-6 px)", "\\textbf{IV)}", "font", None, "high",
    "\\noindent\\textbf{IV)} \\emph{Fin", "\\noindent IV) \\emph{Fin", LABEL)
add(157, "after the list (i)-(iii): 'On sait alors ((7.8.3) et (2.3.8)) que sous les conditions (i) et (ii)'",
    "'On sait alors' begins an indented new paragraph", "text directly after \\end{enumerate}: no paragraph, no indent", "other", None, "medium",
    "\\end{enumerate}¶On sait alors", "\\end{enumerate}¶¶On sait alors")
add(157, "'la topologie m-adique sur A est induite par la topologie m'-adique de A''", "'induite' italic", "upright",
    "italics", None, "high", "est induite par la", "est \\emph{induite} par la")
add(157, "'Le complété û : Â→Â' est donc un homomorphisme injectif.'", "hat over A only, prime outside: Â' (enlarged crop)",
    "\\widehat{A'}", "formula", None, "high", "\\to\\widehat{A'}$", "\\to\\widehat{A}'$",
    "Same pattern as convention 8, with a hat (GLOBAL_ISSUES 63; as IV-3 p. 151).")
add(157, "same sentence: 'est donc un homomorphisme injectif.'", "'injectif' italic", "upright", "italics", None, "high",
    "homomorphisme injectif.", "homomorphisme \\emph{injectif}.")
add(157, "'et il n'y a donc qu'un seul point x' de X''", "'un seul' italic", "upright", "italics", None, "high",
    "qu'un seul point $x'$", "qu'\\emph{un seul} point $x'$")
add(157, "Corollaire (11.6.2): 'on suppose que F' est f'-plat en tous les points x' de X''",
    "'tous' roman inside the italic statement", "italic (environment font)", "convention", 6, "high",
    "plat en tous les points $x'$", "plat en \\textup{tous} les points $x'$",
    "As in (11.6.1), pp. 150-151 (findings_150_154.json).")
add(157, "proof of (11.6.2): 'si F_1 est f_1-plat en tous les points x_1 de X_1'", "'tous' italic", "upright", "italics", None, "high",
    "$f_1$-plat en tous¶les points", "$f_1$-plat en \\emph{tous}¶les points")
add(157, "proof of (11.6.2): 'ramené au cas où A est intégralement clos, donc géométriquement unibranche'",
    "'intégralement clos' italic", "upright", "italics", None, "high",
    "est intégralement clos, donc", "est \\emph{intégralement clos}, donc")
add(157, "heading '11.7. Contre-exemples.'", "full stop after the title", "\\subsection{Contre-exemples} (no full stop)",
    "punctuation", None, "high", "\\subsection{Contre-exemples}", "\\subsection{Contre-exemples.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(157, "(11.7.1): 'Soit J le sous-k'-espace vectoriel de m''",
    "k' of 'sous-k'-espace' in BOLD italic (stems 5-6 px against 3-4 px for the k' of 'γ∈k'' on the next line; enlarged crop): a wrong-fount letter",
    "plain $k'$ (the correct reading)", "misprint_in_print", None, "medium",
    "le sous-$k'$-espace", "le sous-$\\boldsymbol{k}'$-espace",
    "The TeX silently corrects the wrong-fount k; the fix restores the printed reading (GLOBAL_ISSUES 29: wrong-fount letters are reproduced). The k' is the Galois extension, light italic everywhere else in (11.7.1).",
    corrected="$k'$")
add(157, "(11.7.1): '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5)'", "n with raised o", "n$^\\circ$",
    "symbol", None, "high", "n$^\\circ$~2", "n\\textsuperscript{o}~2", NSUP)
add(157, "end of page_157.tex: '... l'homomorphisme canonique A'→B=A'/J serait lui | aussi bijectif' (break 157/158 mid-sentence)",
    "p. 158 begins mid-sentence ('aussi bijectif'), flush left", "blank line after '% IV3_B23_P157_END' before \\oldpage[IV-3]{158}",
    "marker", None, "high",
    "serait lui¶% IV3_B23_P157_END¶¶", "serait lui¶% IV3_B23_P157_END¶",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 158 marker is in the right place. APPLY TOGETHER with the p. 158 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- page 158
add(158, "top of page_158.tex: blank line after \\oldpage[IV-3]{158}, before 'aussi bijectif'",
    "'aussi bijectif' continues the sentence of p. 157", "blank line after the marker", "marker", None, "high",
    "\\oldpage[IV-3]{158}¶¶aussi bijectif", "\\oldpage[IV-3]{158}¶aussi bijectif",
    "Apply together with the p. 157 entry (blank line before the marker).")
add(158, "(11.7.1): '(loc. cit., n° 2, cor. de la prop. 6) ce qui est absurde'", "n with raised o", "n$^\\circ$", "symbol", None, "high",
    "n$^\\circ$~2, cor. de la prop.~6) ce", "n\\textsuperscript{o}~2, cor. de la prop.~6) ce", NSUP)
add(158, "'l'homomorphisme canonique A→A_1, qui est local et injectif puisque J∩A=0'", "'local' italic", "upright",
    "italics", None, "high", "qui est local et", "qui est \\emph{local} et")
add(158, "same sentence: 'et injectif puisque'", "'injectif' italic", "upright", "italics", None, "high",
    "et injectif puisque", "et \\emph{injectif} puisque")
add(158, "'nous allons voir qu'il y a un point de X_1=X×_Y Y_1=Spec(B_1)'", "'un' italic", "upright", "italics", None, "high",
    "qu'il y a un point de", "qu'il y a \\emph{un} point de")
add(158, "'où O_X1 est Y_1-plat. Pour cela'", "'plat' italic", "upright", "italics", None, "high",
    "$Y_1$-plat. Pour cela", "$Y_1$-\\emph{plat}. Pour cela")
add(158, "'remarquons que l'on a B⊗_A B=(A'⊗_A A')/(Im(J⊗_A A')+Im(A'⊗_A J)). Or la structure'",
    "formula in the running text, quotient written with a slash", "\\[ B\\otimes_A B=\\frac{...}{...}. \\] display", "other", None, "high",
    "l'on a¶\\[¶B\\otimes_A B¶=\\frac{A'\\otimes_A A'}¶{\\operatorname{Im}(\\mathfrak J\\otimes_A A')¶+\\operatorname{Im}(A'\\otimes_A\\mathfrak J)}.¶\\]¶Or",
    "l'on a¶$B\\otimes_A B=(A'\\otimes_A A')/(\\operatorname{Im}(\\mathfrak J\\otimes_A A')+\\operatorname{Im}(A'\\otimes_A\\mathfrak J))$.¶Or",
    "Display where the print sets the formula in the running text (GLOBAL_ISSUES 21); the print also writes the quotient with a slash, not as a fraction.")
add(158, "'puisque C' et C sont des A-modules libres (Bourbaki,'", "'libres' italic", "upright", "italics", None, "high",
    "des $A$-modules libres (Bourbaki,", "des $A$-modules \\emph{libres} (Bourbaki,")
add(158, "'(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. de la prop. 6). De ce qui précède'", "n with raised o", "n$^\\circ$",
    "symbol", None, "high", "n$^\\circ$~2, cor. de la prop.~6). De", "n\\textsuperscript{o}~2, cor. de la prop.~6). De", NSUP)
add(158, "'donc est un A_1-module plat, mais comme γ∉k'", "'plat' italic", "upright", "italics", None, "high",
    "$A_1$-module plat, mais", "$A_1$-module \\emph{plat}, mais")
add(158, "(11.7.2): 'lorsqu'on ne suppose plus g propre).'", "second 'propre' italic", "upright", "italics", None, "high",
    "plus $g$¶propre)", "plus $g$¶\\emph{propre})")
add(158, "(11.7.2): 'dans le plan affine V_k^2=Spec(A_0)'", "bold upright V", "plain italic $V$", "font", None, "high",
    "$V_k^2=\\operatorname{Spec}(A_0)$", "$\\mathbf V_k^2=\\operatorname{Spec}(A_0)$",
    "The edition writes the affine space as \\mathbf V (e.g. \\mathbf V_Y^n, IV-2 p. 21).")
add(158, "'Z=Spec(B) n'est autre que le normalisé du préschéma Y'", "'normalisé' italic", "upright", "italics", None, "high",
    "le normalisé du", "le \\emph{normalisé} du")
add(158, "'(II, 6.3.8), somme des deux schémas Z_1=Spec(B_1), Z_2=Spec(B_2)'", "'somme' italic", "upright", "italics", None, "high",
    "6.3.8), somme des", "6.3.8), \\emph{somme} des")
add(158, "'l'homomorphisme A→A'=B_1⊕(B_2)_S est injectif, mais le morphisme'", "'injectif' italic", "upright", "italics", None, "high",
    "est injectif, mais le morphisme", "est \\emph{injectif}, mais le morphisme")
add(158, "'(car f(Z_2—{z_2}) n'est pas fermé dans Y'", "long dash Z_2—{z_2}", "minus sign", "convention", 7, "high",
    "f(Z_2-\\{z_2\\})", "f(Z_2\\setmin\\{z_2\\})", C7)
add(158, "'bien que Z_2—{z_2} soit fermé dans X'", "long dash Z_2—{z_2}", "minus sign", "convention", 7, "high",
    "$Z_2-\\{z_2\\}$ soit", "$Z_2\\setmin\\{z_2\\}$ soit", C7)
add(158, "'Nous allons voir maintenant que f n'est pas plat au point z_1'", "'n'est pas plat' italic", "upright", "italics", None, "high",
    "que $f$ n'est pas plat au point", "que $f$ \\emph{n'est pas plat} au point")
add(158, "'l'homomorphisme canonique O_y→O_z1 n'est pas injectif; mais cela est immédiat'", "'n'est pas injectif' italic", "upright",
    "italics", None, "high", "n'est pas injectif~;", "\\emph{n'est pas injectif}~;")
add(158, "'la première projection p : X×_Y X→X est un isomorphisme : en effet'", "'isomorphisme' italic", "upright", "italics", None, "high",
    "est un isomorphisme~: en effet", "est un \\emph{isomorphisme}~: en effet")
add(158, "'en effet, on a B_1⊗_A B_1=(A/p_1)⊗_A(A/p_1)=A/p_1, (B_2)_S⊗_A(B_2)_S=...'",
    "formula in the running text", "\\[ ... \\] display", "other", None, "high",
    "on a¶\\[¶B_1\\otimes_A B_1=(A/\\mathfrak p_1)\\otimes_A(A/\\mathfrak p_1)=A/\\mathfrak p_1,¶\\]¶$(B_2)_S",
    "on a¶$B_1\\otimes_A B_1=(A/\\mathfrak p_1)\\otimes_A(A/\\mathfrak p_1)=A/\\mathfrak p_1$,¶$(B_2)_S", INL)
add(158, "(11.7.3): 'et sa normalisée Z, de sorte que'", "'normalisée' italic", "upright", "italics", None, "high",
    "sa normalisée $Z$", "sa \\emph{normalisée} $Z$")
add(158, "(11.7.3): 'la restriction de g à Z—g^{-1}(y) est un isomorphisme'", "long dash", "minus sign", "convention", 7, "high",
    "$Z-g^{-1}(y)$", "$Z\\setmin g^{-1}(y)$", C7)
add(158, "(11.7.3): 'est un isomorphisme sur Y—{y}'", "long dash", "minus sign", "convention", 7, "high",
    "$Y-\\{y\\}$", "$Y\\setmin\\{y\\}$", C7)
add(158, "(11.7.3): 'somme des deux préschémas Spec(k(z_1)), Spec(k(z_2))'", "bold italic k", "plain $k$", "convention", 1, "high",
    "\\operatorname{Spec}(k(z_1))", "\\operatorname{Spec}(\\boldsymbol{k}(z_1))")
add(158, "(11.7.3): 'Spec(k(z_2))'", "bold italic k", "plain $k$", "convention", 1, "high",
    "\\operatorname{Spec}(k(z_2))", "\\operatorname{Spec}(\\boldsymbol{k}(z_2))")
add(158, "(11.7.3): 'canoniquement isomorphes à Spec(k(y))'", "bold italic k", "plain $k$", "convention", 1, "high",
    "\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))")
add(158, "(11.7.3): 'induit sur l'ouvert Z—{z_2}'", "long dash", "minus sign", "convention", 7, "high",
    "$Z-\\{z_2\\}$", "$Z\\setmin\\{z_2\\}$", C7)
add(158, "(11.7.3): 'Le morphisme f est radiciel, car pour tout y'∈Y'", "'radiciel' italic", "upright", "italics", None, "high",
    "est radiciel, car", "est \\emph{radiciel}, car")
add(158, "(11.7.3): 'k(y')→k(x') étant un isomorphisme' (first k)", "bold italic k", "plain $k$", "convention", 1, "high",
    "$k(y')\\to", "$\\boldsymbol{k}(y')\\to")
add(158, "(11.7.3): 'k(y')→k(x')' (second k)", "bold italic k", "plain $k$", "convention", 1, "high",
    "\\to k(x')$", "\\to\\boldsymbol{k}(x')$")
add(158, "(11.7.3): 'le morphisme diagonal Δ_f : X→X×_Y X est bijectif (1.7.7.1)'", "'bijectif' italic", "upright", "italics", None, "high",
    "est bijectif (1.7.7.1)", "est \\emph{bijectif} (1.7.7.1)")
add(158, "(11.7.3): 'comme f est non ramifié (17.4.2, d'))'",
    "'(17.4.2, d'))': italic label d') with its own parenthesis, then the reference's roman ')' (enlarged crop)",
    "'(17.4.2, d$'$)': upright d, one parenthesis", "punctuation", None, "high",
    "(17.4.2, d$'$)", "(17.4.2, \\emph{d$'$)})",
    "The fix also sets the label italic, as printed (form of the 0_IV-1 fixes such as (22.5.8, \\emph{b')})).")
add(158, "(11.7.3): 'Δ_f est une immersion ouverte (17.4.2, b))'", "'immersion ouverte' italic", "upright", "italics", None, "high",
    "est une immersion ouverte", "est une \\emph{immersion ouverte}")
add(158, "(11.7.3): 'immersion ouverte (17.4.2, b)); par suite'",
    "'(17.4.2, b))': italic label b) WITHOUT prime, then the reference's ')' (8x crop)",
    "'(17.4.2, b$'$)': label b' with a prime, one parenthesis", "symbol", None, "high",
    "(17.4.2, b$'$)", "(17.4.2, \\emph{b)})",
    "The printed b) is right: in (17.4.2) (ega4-17-fr.tex) b) is 'Le morphisme diagonal Δ_f est une immersion ouverte', while b') concerns Y'-sections. The TeX's prime is a transcription error, not a correction.")
add(158, "(11.7.3): 'par suite Δ_f est un isomorphisme, et la première projection'", "'isomorphisme' italic", "upright", "italics", None, "high",
    "est un isomorphisme, et la première", "est un \\emph{isomorphisme}, et la première")
add(158, "(11.7.3): 'Cependant f n'est pas plat au point z_1; sinon'", "'n'est pas plat' italic", "upright", "italics", None, "high",
    "Cependant $f$ n'est¶pas plat au point", "Cependant $f$ \\emph{n'est¶pas plat} au point")
add(158, "(11.7.3): 'mais cela est absurde, car O_z1 n'a que deux idéaux premiers distincts'",
    "subscript printed 'z1' with the 1 at the size and baseline of z (not a second-order index; pixel check)",
    "\\mathcal O_{z_1}", "misprint_in_print", None, "medium",
    "car $\\mathcal O_{z_1}$ n'a", "car $\\mathcal O_{z1}$ n'a",
    "The TeX silently corrects; the fix restores the printed reading (as \\mathscr{O}_{xi}, EGA I p. 144). Two lines above, 'il existerait dans O_z deux idéaux' shows O_z with a blank where the 1 belongs (spacing as for O_z1 elsewhere on the line): taken as a sort that did not print, not reported.",
    corrected="$\\mathcal O_{z_1}$")
add(158, "(11.7.4): 'Y=Spec(k[S, T]/(S(S²+T²)—(S²—T²)))' (first dash)", "long dash", "minus sign", "convention", 7, "high",
    "+T^2)-(", "+T^2)\\setmin(", C7S)
add(158, "same formula: '(S²—T²)' (second dash)", "long dash", "minus sign", "convention", 7, "high",
    "S^2-T^2", "S^2\\setmin T^2", C7S)
add(158, "end of page_158.tex: '... s'identifient alors à des sous-anneaux du corps | des fractions de A' (break 158/159 mid-sentence)",
    "p. 159 begins mid-sentence ('des fractions de A'), flush left", "blank line after '% IV3_B23_P158_END' before \\oldpage[IV-3]{159}",
    "marker", None, "high",
    "corps¶% IV3_B23_P158_END¶¶", "corps¶% IV3_B23_P158_END¶",
    "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 159 marker is in the right place. APPLY TOGETHER with the p. 159 entry removing the blank line after the marker.")

# ---------------------------------------------------------------- page 159
add(159, "top of page_159.tex: blank line after \\oldpage[IV-3]{159}, before 'des fractions de A'",
    "'des fractions de A' continues the sentence of p. 158", "blank line after the marker", "marker", None, "high",
    "\\oldpage[IV-3]{159}¶¶des fractions", "\\oldpage[IV-3]{159}¶des fractions",
    "Apply together with the p. 158 entry (blank line before the marker).")
add(159, "(11.7.4): 'l'homomorphisme û : Ô_y→Ô_z1 n'est pas injectif, car'", "'n'est pas injectif' italic", "upright",
    "italics", None, "high", "n'est pas injectif, car", "\\emph{n'est pas injectif}, car")
add(159, "(11.7.4): 'la première projection p : X×_Y X→X est un isomorphisme, bien que'", "'isomorphisme' italic", "upright",
    "italics", None, "high", "est un isomorphisme, bien que", "est un \\emph{isomorphisme}, bien que")
add(159, "(11.7.5): 'en supposant seulement A unibranche.'", "'unibranche' italic", "upright", "italics", None, "high",
    "seulement $A$ unibranche.", "seulement $A$ \\emph{unibranche}.")
add(159, "(11.7.5): 'avec t=v/u, tel que t²=—1'", "long dash as the minus sign", "minus sign", "convention", 7, "high",
    "$t^2=-1$", "$t^2=\\setmin 1$", "Unary minus printed as the long dash (GLOBAL_ISSUES 23/49); \\setmin as for convention 7.")
add(159, "(11.7.5): 'X=Spec(Ā) (normalisé de Y (II, 6.3.8))'", "'normalisé' italic", "upright", "italics", None, "high",
    "(normalisé de $Y$", "(\\emph{normalisé} de $Y$")
add(159, "(11.7.5): 'O_X' est Y'-plat en un point de X''", "'un' italic", "upright", "italics", None, "high",
    "plat en un point de $X'$", "plat en \\emph{un} point de $X'$")
add(159, "(11.7.5): 'mais n'est pas Y'-plat en tous les points ayant ces projections'", "'tous' italic", "upright",
    "italics", None, "high", "plat en tous les points ayant", "plat en \\emph{tous} les points ayant")
add(159, "(11.7.5): 'isomorphe à C[[U, V]]/(U+iV)(U—iV)'", "long dash", "minus sign", "convention", 7, "high",
    "(U-iV)$", "(U\\setmin iV)$", C7S)
add(159, "(11.7.5): 'engendrés respectivement par u+iv et u—iv'", "long dash", "minus sign", "convention", 7, "high",
    "et $u-iv$,", "et $u\\setmin iv$,", C7S)
add(159, "(11.7.5): 'e''=(1⊗1—t⊗i)/2'", "long dash", "minus sign", "convention", 7, "high",
    "(1\\otimes1-t\\otimes i)", "(1\\otimes1\\setmin t\\otimes i)", C7S)
add(159, "(11.7.5): 'et les images de u+iv et de u—iv par cette injection'", "long dash", "minus sign", "convention", 7, "high",
    "de $u-iv$ par", "de $u\\setmin iv$ par", C7S)
add(159, "(11.7.5): '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5)'", "n with raised o", "n$^\\circ$",
    "symbol", None, "high", "n$^\\circ$~2", "n\\textsuperscript{o}~2", NSUP)
add(159, "heading '11.8. Un critère valuatif de platitude.'", "full stop after the title",
    "\\subsection{Un critère valuatif de platitude} (no full stop)", "punctuation", None, "high",
    "\\subsection{Un critère valuatif de platitude}", "\\subsection{Un critère valuatif de platitude.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(159, "Théorème (11.8.1): 'l'anneau local O_y intègre (resp. réduit et noethérien)'",
    "'(resp.' and the parentheses roman, 'réduit et noethérien' italic", "all italic (environment font)", "convention", 6, "high",
    "(resp. réduit et¶noethérien)", "\\textup{(resp. \\emph{réduit et¶noethérien})}",
    "Form of the pp. 140-142 fixes (\\textup{(resp. \\emph{...})}).")
add(159, "Théorème (11.8.1): 'pour tout anneau de valuation (resp. tout anneau de valuation discrète) A''",
    "'(resp.' and the parentheses roman, the rest italic", "all italic (environment font)", "convention", 6, "high",
    "(resp. tout anneau de valuation¶discrète)", "\\textup{(resp. \\emph{tout anneau de valuation¶discrète})}")
add(159, "proof of (11.8.1): 'se borner au cas où Y=Spec(A) est le spectre d'un anneau local A'", "'local' italic", "upright",
    "italics", None, "high", "d'un anneau local $A$", "d'un anneau \\emph{local} $A$")
add(159, "proof of (11.8.1): label '(i) Cas où A est intègre. — Soient K'", "'(i)' in ordinary roman weight",
    "\\textbf{(i)}", "font", None, "high",
    "\\noindent\\textbf{(i)} \\emph{Cas", "\\noindent(i) \\emph{Cas",
    "As the step labels I)-IV) and label (ii) on p. 160 (findings_160_164.json; GLOBAL_ISSUES 51: proof-part labels are printed upright).")
add(159, "end of page_159.tex: '... Il existe alors au moins un | point x'∈X'' (break 159/160 mid-sentence)",
    "the sentence continues on p. 160", "blank line after '% IV3_B23_P159_END' before \\oldpage[IV-3]{160}", "marker", None, "high",
    None, None,
    "Mid-sentence page break (GLOBAL_ISSUES 20). Both blank lines around \\oldpage[IV-3]{160} were already removed from findings_160_164.json (FIXLOG.jsonl): no second edit here.")

# ---------------------------------------------------------------- write and verify
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
bad = 0
for d in F:
    f = d["fix"]
    if not f:
        continue
    t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(f["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(f["old"][:80]))
    for s in (f["old"], f["new"]):
        if any(ord(c) < 32 and c != "\n" for c in s):
            bad += 1
            print("CONTROL CHAR", d["page"], repr(s[:80]))
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, {k: c[(p, k)] for k in ("normal", "convention", "misprint")})
print("findings", len(F), "problems", bad)
