# Build findings_070_074.json for EGA IV-2 pp. 70-74, check every fix's "old" occurs exactly once
# in its page_NNN.tex (LF-normalized) and that the fixes of a page apply in sequence.
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_070_074.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def resp(page, where, old, new, note=""):
    add(page, where, "'(resp.' upright roman inside the italic statement", "'(resp.' italic (statement environment)",
        "convention", 6, "high", old, new, note)


def label(page, where, lab, old, new):
    add(page, where, f"item label {lab} upright roman", f"\\item[{lab}] comes out italic in the italic statement",
        "convention", 6, "high", old, new)


def ref(page, where, r, old, new):
    add(page, where, f"reference {r} upright inside the italic statement",
        f"{r} italic (statement environment)", "convention", 6, "high", old, new)


def bold_ref(page, where, r, old, new):
    add(page, where, f"{r} with a bold chapter numeral", "plain numeral", "convention", 2, "high", old, new)


# ---------------------------------------------------------------- page 70
add(70, "top of page", "the page continues the sentence of p. 69 ('En vertu | de (I, 5.1.8), ...'), flush left, no new paragraph",
    "blank line after \\oldpage[IV-2]{70}: paragraph break inside the sentence", "other", None, "high",
    "\\oldpage[IV-2]{70}\n\nde ", "\\oldpage[IV-2]{70}\nde ",
    "Apply together with the p. 69 entry for the blank line after 'En vertu' before the marker (GLOBAL_ISSUES 20).")
bold_ref(70, "l. 1", "(I, 5.1.8)", "(I, 5.1.8)", "(\\textbf{I}, 5.1.8)")
resp(70, "Définition (4.6.9), l. 2", "(resp.\n\\emph{géométriquement ponctuellement intègre})",
     "\\textup{(resp.}\n\\emph{géométriquement ponctuellement intègre})")
resp(70, "Définition (4.6.9), l. 4: 'X' est réduit (resp. intègre) en x''", "réduit (resp. intègre) en $x'$",
     "réduit \\textup{(resp.} intègre) en $x'$")
add(70, "Définition (4.6.9), l. 4: '(i.e.,'", "'(i.e.,' upright roman inside the italic definition",
    "(i.e., italic (definition environment)", "convention", 6, "high",
    "(i.e., $\\mathcal O", "\\textup{(i.e.,} $\\mathcal O")
resp(70, "Définition (4.6.9), l. 4: 'est réduit (resp. intègre))'", "réduit (resp. intègre)). On dit",
     "réduit \\textup{(resp.} intègre)). On dit")
add(70, "Définition (4.6.9), last line", "'(auquel cas on dit aussi que X(x)_k k' est' and the closing parenthesis upright roman; only 'ponctuellement intègre' italic",
    "the whole parenthesis italic (definition environment)", "convention", 6, "high",
    "(auquel cas on dit aussi que $X\\otimes_k k'$ est ponctuellement intègre).",
    "\\textup{(auquel cas on dit aussi que $X\\otimes_k k'$ est} ponctuellement intègre\\textup{)}.")
resp(70, "Proposition (4.6.10), l. 3", "(resp. géométriquement ponctuellement intègre) en $x$",
     "\\textup{(resp.} géométriquement ponctuellement intègre) en $x$")
bold_ref(70, "proof of (4.6.10)", "(I, 3.4.7)", "(I, 3.4.7)", "(\\textbf{I}, 3.4.7)")
bold_ref(70, "proof of (4.6.10)", "(I, 3.4.9)", "(I, 3.4.9)", "(\\textbf{I}, 3.4.9)")
add(70, "proof of (4.6.10): 'posons K = k(s)'", "bold italic k in k(s)", "plain $k(s)$", "convention", 1, "high",
    "$K=k(s)$", "$K=\\boldsymbol{k}(s)$")
bold_ref(70, "end of the proof of (4.6.10)", "(0_I, 6.5.1)", "$(0_{\\mathrm I},6.5.1)$", "$(\\mathbf{0}_{\\mathrm I},6.5.1)$")
resp(70, "Corollaire (4.6.11), l. 1: '(resp. algébriquement clos)'", "parfait (resp. algébriquement clos)",
     "parfait \\textup{(resp.} algébriquement clos)")
resp(70, "Corollaire (4.6.11), l. 2", "(resp. géométriquement ponctuellement intègre) au point\n$x$ sur",
     "\\textup{(resp.} géométriquement ponctuellement intègre) au point\n$x$ sur")
resp(70, "Corollaire (4.6.11), l. 3: 'soit réduit (resp. intègre)'", "soit réduit (resp.\nintègre).",
     "soit réduit \\textup{(resp.}\nintègre).")
add(70, "end of page", "the sentence runs on over the page break: p. 71 begins 'donc, pour tout point x' ...' flush left",
    "blank line before \\oldpage[IV-2]{71}: paragraph break inside the sentence", "other", None, "high",
    "intègre (4.4.4))~;\n\n", "intègre (4.4.4))~;\n",
    "Apply together with the p. 71 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 71
add(71, "top of page", "page begins mid-sentence: 'donc, pour tout point x' de X' = X(x)_k k' ...' (no indent, same paragraph as p. 70)",
    "\\oldpage[IV-2]{71} followed by a blank line", "other", None, "high",
    "\\oldpage[IV-2]{71}\n\ndonc,", "\\oldpage[IV-2]{71}\ndonc,",
    "Apply together with the p. 70 entry 'intègre (4.4.4))~;' (blank line before the marker).")
add(71, "Proposition (4.6.12), l. 1", "'Soient k un corps, X un k-préschéma' with a comma (enlarged crop)",
    "'corps~; $X$' (semicolon)", "punctuation", None, "high", "un corps~; $X$", "un corps, $X$")
label(71, "Proposition (4.6.12), label a)", "a)", "\\item[a)]", "\\item[\\textup{a)}]")
label(71, "Proposition (4.6.12), label b)", "b)", "\\item[b)]", "\\item[\\textup{b)}]")
label(71, "Proposition (4.6.12), label c)", "c)", "\\item[c)]", "\\item[\\textup{c)}]")
label(71, "Proposition (4.6.12), label d)", "d)", "\\item[d)]", "\\item[\\textup{d)}]")
label(71, "Proposition (4.6.12), label e)", "e)", "\\item[e)]", "\\item[\\textup{e)}]")
add(71, "Proposition (4.6.12) e)", "bold italic k in k(z)", "plain $k(z)$", "convention", 1, "high",
    "$z$, $k(z)$", "$z$, $\\boldsymbol{k}(z)$")
add(71, "Proposition (4.6.12) e), last line", "'séparable' upright roman (emphasis) in 'est une extension séparable de k' (enlarged crop)",
    "séparable italic like the rest of the statement", "convention", 6, "high",
    "séparable de $k$.", "\\emph{séparable} de $k$.")
add(71, "proof of (4.6.12), l. 1", "'d) => a) => b) => c)': the letters and parentheses italic",
    "upright d), a), b), c) in the roman proof", "italics", None, "high",
    "Les implications d) $\\Rightarrow$ a) $\\Rightarrow$ b) $\\Rightarrow$ c) sont",
    "Les implications \\emph{d)} $\\Rightarrow$ \\emph{a)} $\\Rightarrow$ \\emph{b)} $\\Rightarrow$ \\emph{c)} sont")
add(71, "proof of (4.6.12), l. 3", "'Prouvons que c) implique d).': c) and d) italic", "upright c), d)", "italics", None, "high",
    "Prouvons que c) implique d).", "Prouvons que \\emph{c)} implique \\emph{d)}.")
add(71, "proof of (4.6.12), l. 4", "'O_{X x}(x)_k k'': no comma between X and x in the subscript, a gap of a comma's width (crop at 5x)",
    "\\mathcal O_{X,x}\\otimes_k k' (comma present)", "misprint_in_print", None, "medium",
    "\\mathcal O_{X,x}\\otimes_k k'", "\\mathcal O_{X\\,x}\\otimes_k k'",
    "The TeX silently corrects. The comma may simply have failed to print in this copy (the gap is there); the corrected edition keeps O_{X,x}.",
    corrected="\\mathcal O_{X,x}\\otimes_k k'")
bold_ref(71, "proof of (4.6.12), l. 5", "(I, 3.5.8 et 3.5.7)", "(I, 3.5.8 et 3.5.7)", "(\\textbf{I}, 3.5.8 et 3.5.7)")
add(71, "proof of (4.6.12), l. 6: 'l'hypothèse c)'", "c) italic", "upright c)", "italics", None, "high",
    "l'hypothèse c).", "l'hypothèse \\emph{c)}.")
add(71, "proof of (4.6.12), l. 6: 'l'équivalence de d) et de e)'", "d) and e) italic", "upright d), e)", "italics", None, "high",
    "de d) et de e)", "de \\emph{d)} et de \\emph{e)}")
add(71, "proof of (4.6.12), l. 7: 'de b) et e) dans (4.6.1)'", "b) and e) italic", "upright b), e)", "italics", None, "high",
    "de b) et e) dans", "de \\emph{b)} et \\emph{e)} dans")
bold_ref(71, "end of the proof of (4.6.12)", "(I, 2.4.2)", "(I, 2.4.2)", "(\\textbf{I}, 2.4.2)")
ref(71, "Corollaire (4.6.13), l. 1", "(4.6.12)", "Sous les hypothèses de (4.6.12),", "Sous les hypothèses de \\textup{(4.6.12)},")
ref(71, "Corollaire (4.6.13), l. 2", "(4.6.12)", "e) de (4.6.12) équivalent", "e) de \\textup{(4.6.12)} équivalent")
label(71, "Corollaire (4.6.13), label f)", "f)", "\\item[f)]", "\\item[\\textup{f)}]")
bold_ref(71, "proof of (4.6.13)", "(I, 6.1.13)", "(I, 6.1.13)", "(\\textbf{I}, 6.1.13)")
add(71, "proof of (4.6.13): 'le critère (4.6.12, e))'", "e) italic", "upright e)", "italics", None, "high",
    "(4.6.12, e))", "(4.6.12, \\emph{e)})")
add(71, "proof of (4.6.13): 'compte tenu du critère (4.6.1, e))'", "e) italic", "upright e)", "italics", None, "high",
    "(4.6.1, e))", "(4.6.1, \\emph{e)})")
add(71, "(4.6.14), first paragraph, last line", "'est intègre en un point au-dessus de x': 'un' italic (emphasis)",
    "'un' roman, no \\emph", "italics", None, "high", "intègre en un point", "intègre en \\emph{un} point")
add(71, "(4.6.14), second paragraph", "bold italic k in k(z)", "plain $k(z)$", "convention", 1, "high",
    "$k(z)$ soit", "$\\boldsymbol{k}(z)$ soit")
add(71, "end of page", "the sentence runs on over the page break: p. 72 begins 'l'on suppose en outre ...' flush left",
    "blank line before \\oldpage[IV-2]{72}: paragraph break inside the sentence", "other", None, "high",
    "$X$, que\n\n", "$X$, que\n", "Apply together with the p. 72 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 72
add(72, "top of page", "page begins mid-sentence: 'l'on suppose en outre géométriquement irréductible; ...' (no indent, same paragraph as p. 71)",
    "\\oldpage[IV-2]{72} followed by a blank line", "other", None, "high",
    "\\oldpage[IV-2]{72}\n\nl'on", "\\oldpage[IV-2]{72}\nl'on",
    "Apply together with the p. 71 entry '$X$, que' (blank line before the marker).")
add(72, "paragraph 'Rappelons que', l. 1", "'localement noethérien' italic", "roman, no \\emph", "italics", None, "high",
    "un préschéma localement noethérien est", "un préschéma \\emph{localement noethérien} est")
add(72, "paragraph 'Rappelons que', l. 2", "'il est localement intègre (I, 6.1.13)': 'localement intègre' italic",
    "roman, no \\emph", "italics", None, "high", "il est localement intègre", "il est \\emph{localement intègre}")
bold_ref(72, "paragraph 'Rappelons que', l. 2", "(I, 6.1.13)", "(I, 6.1.13)", "(\\textbf{I}, 6.1.13)")
label(72, "Proposition (4.6.15), label (i)", "(i)", "\\item[(i)] Soient", "\\item[\\textup{(i)}] Soient")
add(72, "Proposition (4.6.15) (i), l. 1", "'Soient k un corps, X un k-préschéma de type fini' with a comma (enlarged crop)",
    "'corps~; $X$' (semicolon)", "punctuation", None, "high", "un corps~; $X$", "un corps, $X$")
label(72, "Proposition (4.6.15), label (ii)", "(ii)", "\\item[(ii)] Soit $X$", "\\item[\\textup{(ii)}] Soit $X$")
bold_ref(72, "proof of (4.6.15) (i)", "(I, 6.1.10)", "(I, 6.1.10)", "(\\textbf{I}, 6.1.10)")
add(72, "proof of (4.6.15) (ii), l. 5: 'une extension finie k' de k tel que X' = X(x)_k k' soit réduit'",
    "'tel que' (agreeing with nothing: 'une extension ... telle que' is meant)", "tel que (as printed)",
    "misprint_in_print", None, "medium", None, None,
    "The TeX keeps the printed reading. The later 'voisinage ouvert U de x tel que' on the same page is correct.",
    corrected="telle que")
bold_ref(72, "proof of (4.6.15) (ii)", "(II, 6.1.10)", "(II, 6.1.10)", "(\\textbf{II}, 6.1.10)")
label(72, "Proposition (4.6.16), label a)", "a)", "\\item[a)]", "\\item[\\textup{a)}]")
ref(72, "Proposition (4.6.16) a)", "(3.2.2)", "réduit (3.2.2).", "réduit \\textup{(3.2.2)}.")
label(72, "Proposition (4.6.16), label b)", "b)", "\\item[b)]", "\\item[\\textup{b)}]")
label(72, "Proposition (4.6.16), label c)", "c)", "\\item[c)]", "\\item[\\textup{c)}]")

# ---------------------------------------------------------------- page 73
D16_OLD = ("\\item[d)] Pour toute extension $k'$ de $k$ (ou pour une extension\n"
           "algébriquement close $k'$ de $k$), $\\mathscr F'$ est un\n$\\mathcal O_{X'}$-Module réduit.")
D16_NEW = ("\\item[\\textup{d)}] Pour toute extension $k'$ de $k$ \\textup{(ou} pour \\emph{une} extension\n"
           "algébriquement close $k'$ de $k$), $\\mathscr F'$ est un\n$\\mathcal O_{X'}$-Module réduit.")
D18_OLD = D16_OLD.replace("Module réduit.", "Module intègre.")
D18_NEW = D16_NEW.replace("Module réduit.", "Module intègre.")
add(73, "Proposition (4.6.16), label d)", "item label d) upright roman",
    "\\item[d)] comes out italic in the italic statement", "convention", 6, "high", D16_OLD, D16_NEW,
    "One edit for the label and the next entry: \\item[d)] occurs twice on the page (also in (4.6.18)), so the label is fixed with its item.")
add(73, "Proposition (4.6.16) d): '(ou pour une extension algébriquement close k' de k)'",
    "'(ou' and 'une' upright roman, 'pour' and 'extension algébriquement close k' de k' italic (enlarged crop)",
    "all italic", "convention", 6, "high", None, None,
    "Included in the edit of the previous entry (label d) of (4.6.16)): \\textup{(ou} pour \\emph{une} extension.")
add(73, "proof of (4.6.16), l. 1", "'a) entraîne b). La condition b)': a), b), b) italic", "upright a), b), b)",
    "italics", None, "high", "Il est clair que a) entraîne b). La condition b) entraîne",
    "Il est clair que \\emph{a)} entraîne \\emph{b)}. La condition \\emph{b)} entraîne")
add(73, "proof of (4.6.16), l. 3", "'Y est réduit, et il y a': 'réduit' italic", "roman, no \\emph", "italics", None, "high",
    "$Y$ est réduit, et il y a", "$Y$ est \\emph{réduit}, et il y a")
add(73, "proof of (4.6.16), l. 5", "'Or, pour toute extension': 'toute' italic", "roman, no \\emph", "italics", None, "high",
    "Or, pour toute extension", "Or, pour \\emph{toute} extension")
add(73, "proof of (4.6.16), 'lorsque X' est localement noethérien.'", "'localement noethérien' italic", "roman, no \\emph",
    "italics", None, "high", "$X'$\nest localement noethérien.", "$X'$\nest \\emph{localement noethérien}.")
add(73, "proof of (4.6.16), 'Le fait que b) entraîne c) et que c) entraîne a)'", "b), c), c), a) italic", "upright",
    "italics", None, "high", "Le fait que b) entraîne c) et que c) entraîne\na) est donc",
    "Le fait que \\emph{b)} entraîne \\emph{c)} et que \\emph{c)} entraîne\n\\emph{a)} est donc")
add(73, "proof of (4.6.16), '(4.6.1, d) et b))'", "d) and b) italic", "upright d), b)", "italics", None, "high",
    "(4.6.1, d) et b))", "(4.6.1, \\emph{d)} et \\emph{b)})")
add(73, "proof of (4.6.16), 'dans a), l'hypothèse'", "a) italic", "upright a)", "italics", None, "high",
    "dans a), l'hypothèse", "dans \\emph{a)}, l'hypothèse")
add(73, "end of the proof of (4.6.16)", "'l'équivalence de d) et des autres conditions': d) italic", "upright d)",
    "italics", None, "high", "l'équivalence de d) et des autres", "l'équivalence de \\emph{d)} et des autres")
ref(73, "Définition (4.6.17), l. 1", "(4.6.16)", "équivalentes de (4.6.16), on dit", "équivalentes de \\textup{(4.6.16)}, on dit")
add(73, "Définition (4.6.17), l. 2", "'géométriquement réduit' italic like the rest of the definition (enlarged crop)",
    "\\emph{géométriquement réduit} inside the italic definition: upright", "convention", 6, "high",
    "\\emph{géométriquement réduit} sur $k$", "géométriquement réduit sur $k$",
    "Printed italic word left upright by \\emph inside the itshape environment.")
add(73, "Définition (4.6.17), l. 2", "'séparable' italic like the rest of the definition (enlarged crop)",
    "\\emph{séparable} inside the italic definition: upright", "convention", 6, "high",
    "\\emph{séparable}\nsur", "séparable\nsur", "Printed italic word left upright by \\emph inside the itshape environment.")
add(73, "Proposition (4.6.18), l. 1", "'Soient k un corps, X un k-préschéma' with a comma (enlarged crop)",
    "'corps~; $X$' (semicolon)", "punctuation", None, "high", "un corps~; $X$", "un corps, $X$")
label(73, "Proposition (4.6.18), label a)", "a)", "\\item[a)]", "\\item[\\textup{a)}]")
ref(73, "Proposition (4.6.18) a)", "(3.2.4)", "intègre (3.2.4).", "intègre \\textup{(3.2.4)}.")
label(73, "Proposition (4.6.18), label b)", "b)", "\\item[b)]", "\\item[\\textup{b)}]")
label(73, "Proposition (4.6.18), label c)", "c)", "\\item[c)]", "\\item[\\textup{c)}]")
add(73, "Proposition (4.6.18), label d)", "item label d) upright roman",
    "\\item[d)] comes out italic in the italic statement", "convention", 6, "high", D18_OLD, D18_NEW,
    "One edit for the label and the next entry (see the same pair in (4.6.16)).")
add(73, "Proposition (4.6.18) d): '(ou pour une extension algébriquement close k' de k)'",
    "'(ou' and 'une' upright roman, 'pour' and 'extension algébriquement close k' de k' italic (enlarged crop)",
    "all italic", "convention", 6, "high", None, None,
    "Included in the edit of the previous entry (label d) of (4.6.18)).")
add(73, "proof of (4.6.18), l. 1", "'Les conditions a), b) et c)': letters italic", "upright a), b), c)", "italics", None, "high",
    "Les conditions a), b) et c) entraînent", "Les conditions \\emph{a)}, \\emph{b)} et \\emph{c)} entraînent")
add(73, "proof of (4.6.18), l. 2", "'Pour toute extension k' de k pour laquelle': 'toute' italic", "roman, no \\emph",
    "italics", None, "high", "Pour toute extension $k'$ de\n$k$ pour laquelle", "Pour \\emph{toute} extension $k'$ de\n$k$ pour laquelle")
add(73, "proof of (4.6.18), 'chacune des conditions a), b), c)'", "letters italic", "upright a), b), c)", "italics", None, "high",
    "chacune des conditions a), b), c) entraîne", "chacune des conditions \\emph{a)}, \\emph{b)}, \\emph{c)} entraîne")
add(73, "proof of (4.6.18), 'il est trivial que a) entraîne b), et b) entraîne'", "letters italic", "upright a), b), b)",
    "italics", None, "high", "il est trivial que a) entraîne b),\net b) entraîne",
    "il est trivial que \\emph{a)} entraîne \\emph{b)},\net \\emph{b)} entraîne")
add(73, "proof of (4.6.18), last line: 'donc c), puisque'", "c) italic", "upright c)", "italics", None, "high",
    "donc c), puisque", "donc \\emph{c)}, puisque")
add(73, "end of page", "the sentence runs on over the page break: p. 74 begins 'par J est alors ...' flush left",
    "blank line before \\oldpage[IV-2]{74}: paragraph break inside the sentence", "other", None, "high",
    "$Y$ défini\n\n", "$Y$ défini\n", "Apply together with the p. 74 entry that removes the blank line after the marker.")

# ---------------------------------------------------------------- page 74
add(74, "top of page", "page begins mid-sentence: 'par J est alors géométriquement réduit ...' (no indent, same paragraph as p. 73)",
    "\\oldpage[IV-2]{74} followed by a blank line", "other", None, "high",
    "\\oldpage[IV-2]{74}\n\npar", "\\oldpage[IV-2]{74}\npar",
    "Apply together with the p. 73 entry '$Y$ défini' (blank line before the marker).")
add(74, "proof of (4.6.18), l. 2", "'pour toute extension k' de k': 'toute' italic", "roman, no \\emph", "italics", None, "high",
    "pour toute extension $k'$ de $k$,", "pour \\emph{toute} extension $k'$ de $k$,")
add(74, "proof of (4.6.18), last lines", "'c) entraîne a), et que c) entraîne d)': letters italic", "upright c), a), c), d)",
    "italics", None, "high", "cela montre que c) entraîne\na), et que c) entraîne d) lorsque",
    "cela montre que \\emph{c)} entraîne\n\\emph{a)}, et que \\emph{c)} entraîne \\emph{d)} lorsque")
ref(74, "Définition (4.6.19), l. 1", "(4.6.18)", "équivalentes de (4.6.18), on dit", "équivalentes de \\textup{(4.6.18)}, on dit")
add(74, "Définition (4.6.19), l. 2", "'géométriquement intègre' italic like the rest of the definition (enlarged crop)",
    "\\emph{géométriquement intègre} inside the italic definition: upright", "convention", 6, "high",
    "\\emph{géométriquement intègre} sur $k$.", "géométriquement intègre sur $k$.",
    "Printed italic word left upright by \\emph inside the itshape environment.")
resp(74, "Proposition (4.6.20), l. 3", "(resp. géométriquement intègre) sur $k$,", "\\textup{(resp.} géométriquement intègre) sur $k$,")
resp(74, "Proposition (4.6.20), l. 3-4", "réduit (resp. géométriquement\nintègre) sur $K$.",
     "réduit \\textup{(resp.} géométriquement\nintègre) sur $K$.")
add(74, "proof of (4.6.20)", "'(X(x)_k K)(x)_K K' = X(x)_k K'' set in the running text: '... de K, (X(x)_kK)(x)_KK' = X(x)_kK' est localement noethérien'",
    "the equation is a display \\[...\\]", "other", None, "high",
    "$K$,\n\\[\n(X\\otimes_k K)\\otimes_K K'=X\\otimes_k K'\n\\]\nest localement",
    "$K$,\n$(X\\otimes_k K)\\otimes_K K'=X\\otimes_k K'$\nest localement",
    "Formula displayed where the print has it inline; no connecting word lost.")
label(74, "Proposition (4.6.21), label (i)", "(i)", "\\item[(i)] Si", "\\item[\\textup{(i)}] Si")
resp(74, "Proposition (4.6.21) (i), l. 1", "réduit (resp. géométriquement\nintègre) et", "réduit \\textup{(resp.} géométriquement\nintègre) et")
resp(74, "Proposition (4.6.21) (i), l. 1-2: 'G réduit (resp. intègre)'", "réduit (resp. intègre), alors", "réduit \\textup{(resp.} intègre), alors")
resp(74, "Proposition (4.6.21) (i), l. 2: 'est réduit (resp. intègre).'", "est réduit (resp. intègre).", "est réduit \\textup{(resp.} intègre).")
label(74, "Proposition (4.6.21), label (ii)", "(ii)", "\\item[(ii)] Si", "\\item[\\textup{(ii)}] Si")
resp(74, "Proposition (4.6.21) (ii)", "réduits (resp.\ngéométriquement intègres)", "réduits \\textup{(resp.}\ngéométriquement intègres)")
bold_ref(74, "proof of (4.6.21) (i), end", "(I, 9.1.12)", "vertu de (I,", "vertu de (\\textbf{I},")
add(74, "proof of (4.6.21) (i), end: 'entraînent, en vertu de (I, 9.1.12) que'",
    "no comma after '(I, 9.1.12)' (the line ends at the margin with the parenthesis; next line 'que')",
    "'(I, 9.1.12), que' (comma present)", "misprint_in_print", None, "high",
    "9.1.12), que", "9.1.12) que",
    "The TeX silently corrects (the incise opened by 'entraînent,' needs its closing comma). The convention-2 entry before this one edits 'vertu de (I,' and does not overlap.",
    corrected="9.1.12), que")
add(74, "'Les définitions (4.6.18) et (4.6.19) se localisent'", "'(4.6.18)' printed; (4.6.18) is a proposition, the definitions localized by (4.6.22) are (4.6.17) and (4.6.19)",
    "(4.6.18) (as printed)", "misprint_in_print", None, "medium", None, None,
    "The TeX keeps the printed reading. (4.6.22) localizes 'géométriquement réduit ou séparable' (4.6.17) and 'géométriquement (ponctuellement) intègre' (4.6.19).",
    corrected="Les définitions (4.6.17) et (4.6.19)")
add(74, "Définition (4.6.22), l. 2-3", "'(resp. géométriquement ponctuellement intègre)' all upright roman, like 'géométriquement réduit' and 'séparable' (enlarged crop)",
    "'(resp. géométriquement ponctuellement intègre)' italic", "convention", 6, "high",
    "\\emph{séparable} (resp. géométriquement\nponctuellement intègre)",
    "\\emph{séparable} \\textup{(resp. géométriquement\nponctuellement intègre)}")
resp(74, "Définition (4.6.22), l. 4: '(resp. finie)'", "radicielle (resp. finie)", "radicielle \\textup{(resp.} finie)")
resp(74, "Définition (4.6.22), l. 4: '(resp. intègre)'", "est réduit\n(resp. intègre) en chacun", "est réduit\n\\textup{(resp.} intègre) en chacun")
add(74, "Définition (4.6.22), last line", "'(cf. (3.2.2) et (3.2.4))' upright roman", "italic (definition environment)",
    "convention", 6, "high", "(cf. (3.2.2) et (3.2.4)).", "\\textup{(cf. (3.2.2) et (3.2.4))}.")

# ---------------------------------------------------------------- checks
problems = []
for n in range(70, 75):
    text = (RUN / f"page_{n:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    cur = text
    for f in F:
        if f["page"] != n or f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        c = text.count(old)
        if c != 1:
            problems.append((n, "orig", c, old))
        c2 = cur.count(old)
        if c2 != 1:
            problems.append((n, "seq", c2, old))
        else:
            cur = cur.replace(old, new)
for p in problems:
    print("PROBLEM", p)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for n in range(70, 75):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("total", len(F), "written", OUT)
