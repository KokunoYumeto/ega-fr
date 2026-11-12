import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_105_109.json"


def F(page, where, scan, tex, kind, convention, confidence, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


SETMIN = "Convention 7 (\\setmin, global pass; \\setmin is not yet defined in EGA_IV3_FR.tex)."
SUBTR = "Subtraction printed with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."

findings = [
    # ---------------- page 104 (end of its segment; found from the start of p. 105) ----------------
    F(104, "end of page_104.tex, before \\oldpage[IV-3]{105}: 'La condition f) implique que Spec(B) est reunion de l'ensemble | fini de ses points fermes'",
      "p. 105 begins 'fini de ses points fermés et de son point générique' flush left: the sentence of p. 104 continues; no paragraph break",
      "blank line after 'réunion de l'ensemble' (ega4-10-fr.tex line 749), before the p. 105 marker: a paragraph break mid-sentence",
      "marker", None, "high", fx("réunion de l'ensemble\n\n", "réunion de l'ensemble\n"),
      "OUTSIDE pp. 105-109: the blank line is the last line of page_104.tex (ega4-10-fr.tex line 749); the p. 105 marker itself stands in the right place. The pp. 100-104 checker may report the same edit; apply once."),

    # ---------------- page 105 ----------------
    F(105, "Proposition (10.5.5), label (i)",
      "label '(i)' upright before the italic statement",
      "\\begin{enumerate}[label=(\\roman*)] inside the italic proposition environment: italic label",
      "convention", 6, "high",
      fx("\\begin{enumerate}[label=(\\roman*)]", "\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
      "One edit of the label option covers (i) and (ii) (next entry). GLOBAL_ISSUES 16."),
    F(105, "Proposition (10.5.5), label (ii)",
      "label '(ii)' upright", "italic (same enumerate)",
      "convention", 6, "high", None,
      "Covered by the previous edit (label=\\textup{(\\roman*)})."),
    F(105, "proof of (10.5.5)(ii): 'affines U_i qui sont des spectres d'anneau semi-locaux intègres de dimension 1'",
      "'des spectres d'anneau semi-locaux' (singular 'anneau'; enlarged crop)",
      "'des spectres d'anneaux semi-locaux': the TeX silently corrects the printed reading",
      "misprint_in_print", None, "high",
      fx("spectres d'anneaux semi-locaux", "spectres d'anneau semi-locaux"),
      "Misprint 'd'anneau' for 'd'anneaux' (plural agreement with 'des spectres ... semi-locaux'). The diplomatic TeX must keep the printed 'd'anneau'; the corrected edition keeps 'd'anneaux'.",
      corrected="spectres d'anneaux semi-locaux"),

    # ---------------- page 106 ----------------
    F(106, "Proposition (10.5.7): 'le préschéma induit sur l'ouvert X—Y'",
      "long dash for set difference", "$X-Y$",
      "convention", 7, "high", fx("l'ouvert $X-Y$ est", "l'ouvert $X\\setmin Y$ est"), SETMIN),
    F(106, "proof of (10.5.7): 'un sous-préschéma Z de X—Y qui soit spectre'",
      "long dash for set difference", "$X-Y$",
      "convention", 7, "high", fx("de $X-Y$ qui soit", "de $X\\setmin Y$ qui soit"), SETMIN),
    F(106, "proof of (10.5.7): 'L'existence de la chaîne {x}‾ ⊂ {y}‾ ⊂ {z}‾'",
      "all three terms barred: \\overline{\\{x\\}} ⊂ \\overline{\\{y\\}} ⊂ \\overline{\\{z\\}} (enlarged crop)",
      "$\\{x\\}\\subset\\overline{\\{y\\}}\\subset\\overline{\\{z\\}}$: the bar over {x} is missing",
      "formula", None, "high",
      fx("$\\{x\\}\\subset\\overline{\\{y\\}}", "$\\overline{\\{x\\}}\\subset\\overline{\\{y\\}}"),
      None),
    F(106, "Corollaire (10.5.8): 'l'ouvert Spec(A)—V(ℜ)'",
      "long dash for set difference", "\\operatorname{Spec}(A)-V(\\mathfrak R)",
      "convention", 7, "high",
      fx("\\operatorname{Spec}(A)-V(\\mathfrak R)", "\\operatorname{Spec}(A)\\setmin V(\\mathfrak R)"),
      SETMIN + " The Fraktur letter is a genuine Fraktur R (radical; enlarged crop), \\mathfrak R is right here."),
    F(106, "Corollaire (10.5.9): 'Y = X—{m}'",
      "long dash for set difference", "$Y=X-\\{\\mathfrak m\\}$",
      "convention", 7, "high", fx("$Y=X-\\{\\mathfrak m\\}$", "$Y=X\\setmin\\{\\mathfrak m\\}$"), SETMIN),
    F(106, "end of page_106.tex / top of p. 107: 'la clôture intégrale A' de A est un anneau local complet intègre et | intégralement clos'",
      "p. 107 begins 'intégralement clos et de dimension 1' flush left: the sentence continues; no paragraph break",
      "blank line after 'complet intègre et', before \\oldpage[IV-3]{107}: paragraph break mid-sentence",
      "marker", None, "high", fx("complet intègre et\n\n", "complet intègre et\n"),
      "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 107 marker itself is in the right place."),

    # ---------------- page 107 ----------------
    F(107, "proof of (10.5.10): 'et posons Y = X—{x}'",
      "long dash for set difference", "$Y=X-\\{x\\}$",
      "convention", 7, "high", fx("$Y=X-\\{x\\}$", "$Y=X\\setmin\\{x\\}$"), SETMIN),
    F(107, "heading 10.6",
      "'10.6. Dimension dans les préschémas de Jacobson.' with a final full stop",
      "\\subsection{Dimension dans les préschémas de Jacobson} (no full stop)",
      "punctuation", None, "high",
      fx("\\subsection{Dimension dans les préschémas de Jacobson}", "\\subsection{Dimension dans les préschémas de Jacobson.}"),
      "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."),
    F(107, "Proposition (10.6.1), condition 2°: 'universellement caténaire (5.6.2)'",
      "the reference (5.6.2) is upright inside the italic statement (enlarged crop)",
      "(5.6.2) inside the italic proposition environment: italic",
      "convention", 6, "high", fx("caténaire (5.6.2)", "caténaire \\textup{(5.6.2)}"), None),
    F(107, "Proposition (10.6.1), condition 3°: '(autrement dit, pour tout point fermé s de S' et tout sous-préschéma de S ayant S' pour espace sous-jacent, on a dim(S') = dim(O_{S',s}))'",
      "the whole parenthesis is printed roman inside the italic statement (enlarged crop); 'On a alors les propriétés suivantes :' is italic again",
      "set in the italic proposition environment",
      "convention", 6, "high",
      fx("(autrement dit, pour\ntout point fermé $s$ de $S'$ et tout sous-préschéma de $S$ ayant $S'$ pour espace\nsous-jacent, on a $\\dim(S')=\\dim(\\mathcal O_{S',s})$)",
         "\\textup{(autrement dit, pour\ntout point fermé $s$ de $S'$ et tout sous-préschéma de $S$ ayant $S'$ pour espace\nsous-jacent, on a $\\dim(S')=\\dim(\\mathcal O_{S',s})$)}"),
      None),
    F(107, "Proposition (10.6.1), label (i)",
      "label '(i)' upright", "\\begin{enumerate}[label=(\\roman*)] inside the italic proposition environment: italic label",
      "convention", 6, "high",
      fx("\\begin{enumerate}[label=(\\roman*)]", "\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
      "One edit of the label option covers (i), (ii), (iii) (next two entries). GLOBAL_ISSUES 16."),
    F(107, "Proposition (10.6.1), label (ii)", "label '(ii)' upright", "italic (same enumerate)",
      "convention", 6, "high", None, "Covered by the label-option edit above."),
    F(107, "Proposition (10.6.1), label (iii)", "label '(iii)' upright", "italic (same enumerate)",
      "convention", 6, "high", None, "Covered by the label-option edit above."),
    F(107, "Proposition (10.6.1)(i): '(par exemple si X est irréductible)'",
      "'(par exemple si X est' and ')' roman, only 'irréductible' italic (enlarged crop)",
      "set in the italic proposition environment",
      "convention", 6, "high",
      fx("(par exemple si $X$ est irréductible)", "\\textup{(par exemple si $X$ est \\emph{irréductible})}"),
      "Inside \\textup, \\emph gives the printed italic 'irréductible'."),
    F(107, "Proposition (10.6.1)(i): '(autrement dit, X est caténaire et pour tout point fermé x de X, on a dim(O_{X,x}) = dim(X) (0, 14.3.3))'",
      "the whole parenthesis printed roman inside the italic statement (enlarged crop)",
      "set in the italic proposition environment",
      "convention", 6, "high",
      fx("(autrement dit, $X$ est caténaire et pour tout point fermé\n  $x$ de $X$, on a $\\dim(\\mathcal O_{X,x})=\\dim(X)$ ($\\mathbf 0$, 14.3.3))",
         "\\textup{(autrement dit, $X$ est caténaire et pour tout point fermé\n  $x$ de $X$, on a $\\dim(\\mathcal O_{X,x})=\\dim(X)$ ($\\mathbf 0$, 14.3.3))}"),
      None),
    F(107, "Proposition (10.6.1)(ii): 'Si ξ (resp. η) est le point générique'",
      "'(resp. η)' roman: upright 'resp.' and parentheses (enlarged crop)",
      "(resp. $\\eta$) in the italic proposition environment",
      "convention", 6, "high", fx("(resp. $\\eta$)", "\\textup{(resp. $\\eta$)}"), None),
    F(107, "Proposition (10.6.1)(ii): 'de X (resp. Y) et'",
      "'(resp. Y)' roman (enlarged crop); 'et' italic",
      "(resp. $Y$) in the italic proposition environment",
      "convention", 6, "high", fx("(resp. $Y$)", "\\textup{(resp. $Y$)}"), None),
    F(107, "Proposition (10.6.1)(ii): 'deg.tr_{k(η)} k(ξ)', subscript",
      "the k of the subscript k(η) is bold upright (enlarged crop)",
      "\\operatorname{tr}_{k(\\eta)}",
      "convention", 1, "high",
      fx("\\operatorname{tr}_{k(\\eta)}", "\\operatorname{tr}_{\\mathbf{k}(\\eta)}"),
      "Bold upright k in subscripts (GLOBAL_ISSUES 48)."),
    F(107, "Proposition (10.6.1)(ii): 'deg.tr_{k(η)} k(ξ)', residue field k(ξ)",
      "bold italic k (enlarged crop)", "k(\\xi)",
      "convention", 1, "high", fx("k(\\xi)$, on a", "\\boldsymbol{k}(\\xi)$, on a"),
      "Independent of the subscript edit (no overlap)."),
    F(107, "Proposition (10.6.1)(iii): '(resp. dim(f^{-1}(y)) ≤ n)'",
      "'(resp.' and the parentheses upright (enlarged crop)",
      "(resp. $\\dim(f^{-1}(y))\\leq n$) in the italic proposition environment",
      "convention", 6, "high",
      fx("(resp. $\\dim(f^{-1}(y))\\leq n$)", "\\textup{(resp. $\\dim(f^{-1}(y))\\leq n$)}"), None),
    F(107, "Proposition (10.6.1)(iii): '(resp.' before (10.6.1.3)",
      "'(resp.' roman (enlarged crop)", "(resp. in the italic proposition environment",
      "convention", 6, "high", fx("(resp.\n  \\begin{equation}", "\\textup{(resp.}\n  \\begin{equation}"),
      "The closing parenthesis is inside the display (10.6.1.3)."),
    F(107, "end of page_107.tex / top of p. 108: 'et l'homomorphisme O_{S,g(x)} → O_{X,x} | est local'",
      "p. 108 begins 'est local; donc (5.6.3, (iv))' flush left: the sentence continues; no paragraph break",
      "blank line after '$\\mathcal O_{S,g(x)}\\to\\mathcal O_{X,x}$', before \\oldpage[IV-3]{108}: paragraph break mid-sentence",
      "marker", None, "high", fx("\\to\\mathcal O_{X,x}$\n\n", "\\to\\mathcal O_{X,x}$\n"),
      "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 108 marker itself is in the right place."),

    # ---------------- page 108 ----------------
    F(108, "proof of (10.6.1)(i), case a), display: 'dim(O_{S',x}) — dim(O_{S',ξ})'",
      "long dash for the subtraction (bar 41 px at 300 dpi; the = bars 34-35 px)",
      "minus sign", "convention", 7, "high",
      fx("\\dim(\\mathcal O_{S',x})-\\dim", "\\dim(\\mathcal O_{S',x})\\setmin\\dim"), SUBTR),
    F(108, "proof of (10.6.1)(i), case a), same display: 'dim(S') — dim(O_{S',ξ})'",
      "subtraction printed as a long dash in two pieces ('--', 19 + 19 px with a 2 px gap, 42 px overall, the width of the first dash; enlarged crop)",
      "minus sign", "convention", 7, "high",
      fx("=\\dim(S')-\\dim", "=\\dim(S')\\setmin\\dim"),
      SUBTR + " The two-piece dash reads as the same minus; not reported as a misprint."),
    F(108, "proof of (10.6.1)(ii): 'localement de type fini (1.3.4)'",
      "'(1.3.4)': a reference to EGA IV itself, no chapter numeral (enlarged crop)",
      "(\\textbf{I}, 1.3.4)", "extra", None, "high",
      fx("(\\textbf{I}, 1.3.4)", "(1.3.4)"),
      "The TeX adds 'I,'. IV (1.3.4) is the right reference (morphisms locally of finite type); the hyperlink target, if any, must be IV 1.3.4."),
    F(108, "proof of (10.6.1)(iii): 'et a fortiori dim(X) ≥ dim(Y') + n'",
      "'a fortiori' italic (enlarged crop)", "a fortiori upright",
      "italics", None, "high", fx("et a fortiori", "et \\emph{a fortiori}"), None),
    F(108, "Corollaire (10.6.2): 'conditions 1°, 2° et 3° de (10.6.1). Alors'",
      "the reference (10.6.1) is upright inside the italic statement (enlarged crop)",
      "(10.6.1) inside the italic corollary environment: italic",
      "convention", 6, "high", fx("(10.6.1). Alors", "\\textup{(10.6.1)}. Alors"), None),

    # ---------------- page 109 ----------------
    F(109, "Proposition (10.6.3): 'conditions 1°, 2° et 3° de (10.6.1), et soit Y'",
      "the reference (10.6.1) is upright inside the italic statement (enlarged crop)",
      "(10.6.1) inside the italic proposition environment: italic",
      "convention", 6, "high", fx("(10.6.1), et soit", "\\textup{(10.6.1)}, et soit"), None),
    F(109, "display (10.6.3.1): '= dim {x}‾ + codim({x}‾, Y)'",
      "'dim' followed directly by the barred {x}, without parentheses (enlarged crop)",
      "\\dim(\\overline{\\{x\\}})", "formula", None, "high",
      fx("\\dim(U\\cap Y)=\\dim(\\overline{\\{x\\}})", "\\dim(U\\cap Y)=\\dim\\overline{\\{x\\}}"),
      "Elsewhere on the page the print writes dim({x}‾) with parentheses; here it has none."),
    F(109, "Proposition (10.6.3): 'où Y_i (1 ≤ i ≤ m) sont'",
      "both parentheses upright inside the italic statement (enlarged crop)",
      "parentheses outside math, italic in the proposition environment",
      "convention", 6, "medium",
      fx("($1\\leq i\\leq m$)", "\\textup{(}$1\\leq i\\leq m$\\textup{)}"),
      "Same treatment as IV-2 pp. 183, 212."),
    F(109, "proof of (10.6.3): 'on a (compte tenu de (10.6.1, (i))), dim(U∩X_i) = dim(X_i)'",
      "comma after the parenthesis '(compte tenu de (10.6.1, (i)))' (enlarged crop)",
      "no comma: '(10.6.1, (i))) $\\dim(U\\cap X_i)...'", "punctuation", None, "high",
      fx("(i))) $\\dim(U\\cap X_i)", "(i))), $\\dim(U\\cap X_i)"), None),
    F(109, "proof of (10.6.3): 'Ceci montre que dim(U) est indépendante du voisinage'",
      "'indépendante' italic (enlarged crop)", "upright",
      "italics", None, "high", fx("est indépendante du", "est \\emph{indépendante} du"), None),
    F(109, "Corollaire (10.6.4): 'Sous les hypothèses de (10.6.3), soient'",
      "the reference (10.6.3) is upright inside the italic statement (enlarged crop)",
      "(10.6.3) inside the italic corollary environment: italic",
      "convention", 6, "high", fx("hypothèses de (10.6.3)", "hypothèses de \\textup{(10.6.3)}"), None),
    F(109, "heading 10.7",
      "'10.7. Exemples et contre-exemples.' with a final full stop",
      "\\subsection{Exemples et contre-exemples} (no full stop)",
      "punctuation", None, "high",
      fx("\\subsection{Exemples et contre-exemples}", "\\subsection{Exemples et contre-exemples.}"),
      "GLOBAL_ISSUES 43/58."),
    F(109, "(10.7.1), l. 1: 'localement noethérien de dimension ≤ 1'",
      "'de dimension' italic (small print, enlarged crop)", "upright (env body is roman)",
      "italics", None, "high",
      fx("noethérien de dimension $\\leq1$", "noethérien \\emph{de dimension} $\\leq1$"), None),
    F(109, "(10.7.1), l. 2: 'lorsque S est noethérien'",
      "'noethérien' italic (enlarged crop)", "upright",
      "italics", None, "high", fx("lorsque $S$ est noethérien", "lorsque $S$ est \\emph{noethérien}"), None),
    F(109, "(10.7.1), l. 3: 'sont infinies'",
      "'infinies' italic (enlarged crop)", "upright",
      "italics", None, "high", fx("sont infinies", "sont \\emph{infinies}"), None),
    F(109, "(10.7.1), l. 4: 'Alors S vérifie aussi les conditions 2° et 3° de (10.6.1) :'",
      "'vérifie aussi les conditions 2° et 3° de' italic, (10.6.1) upright (enlarged crop)", "upright",
      "italics", None, "high",
      fx("Alors $S$ vérifie aussi les conditions\n$2^\\circ$ et $3^\\circ$ de",
         "Alors $S$ \\emph{vérifie aussi les conditions\n$2^\\circ$ et $3^\\circ$ de}"),
      "The print's 2 and 3 here are italic figures; the math $2^\\circ$, $3^\\circ$ stay upright (minor)."),
    F(109, "end of page_109.tex / top of p. 110: 'une composante irréductible S' de S est, soit réduite | à un point'",
      "p. 110 begins 'à un point, soit de dimension 1' flush left (page_110_s1.png): the sentence continues; no paragraph break",
      "blank line after 'soit réduite', before \\oldpage[IV-3]{110}: paragraph break mid-sentence",
      "marker", None, "high", fx("soit réduite\n\n", "soit réduite\n"),
      "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 110 marker itself is in the right place. The p. 110 checker may report the same edit; apply once."),
]

# uniqueness check of every 'old' in its page file (CRLF normalised to LF)
ok = True
for f in findings:
    if not f["fix"]:
        continue
    t = (RUN / f"page_{f['page']:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    c = t.count(f["fix"]["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE", f["page"], c, repr(f["fix"]["old"]))
# overlap check: no two fixes on the same page may share characters
for p in sorted({f["page"] for f in findings}):
    t = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    spans = []
    for f in findings:
        if f["page"] == p and f["fix"]:
            i = t.find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
counts = {}
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("all unique, no overlaps" if ok else "PROBLEMS")
print(counts)
