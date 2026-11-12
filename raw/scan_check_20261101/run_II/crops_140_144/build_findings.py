import json, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = RUN + r"\findings_140_144.json"

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

def bI(ref):
    return ("{I, %s}" % ref, "{\\textbf{I}, %s}" % ref)

# ---------------- page 140 ----------------
add(140, "end of (7.1.5): 'k(a) = k est le corps résiduel'", "bold italic k in k(a)", "$k(a)=k$",
    "convention", 1, "high", "$k(a)=k$", "$\\boldsymbol{k}(a)=k$",
    "Only the k of k(a) is bold; the residue field k after '=' is plain italic in the print.")
add(140, "end of (7.1.5): 'k(b) = K est le corps des fractions'", "bold italic k in k(b)", "$k(b)=K$",
    "convention", 1, "high", "$k(b)=K$", "$\\boldsymbol{k}(b)=K$")
add(140, "page start: '... est réduit à deux / points a, b : ...'",
    "p. 140 continues the sentence of p. 139, first line flush left (no paragraph break)",
    "blank lines before and after \\oldpage[II]{140} make a paragraph break",
    "other", None, "high", "\\oldpage[II]{140}\n\npoints $a$", "\\oldpage[II]{140}\npoints $a$",
    "GLOBAL_ISSUES item 20. This removes the blank line after the marker; the blank line before it is the last line of the p. 139 segment (after 'réduit à deux') and must be removed too. Apply both.")
add(140, "(7.1.6): '([1], p. 2-08 et 17-01)'", "([1], p. 2-08 et 17-01): bracket closes after the number",
    "(\\cite[p.~2-08 et 17-01]{I-1}), which prints '([1, p. 2-08 et 17-01])'",
    "punctuation", None, "high", "(\\cite[p.~2-08 et 17-01]{I-1})", "(\\cite{I-1}, p.~2-08 et 17-01)",
    "Same treatment as EGA I p. 148 and EGA II p. 113.")
add(140, "(7.1.6): the three conditions a), b), c)",
    "run-in in the paragraph ('... : a) A est normal; b) A est régulier; c) A est un anneau de valuation; en outre, ...') with italic labels a), b), c)",
    "enumerate list with upright labels \\item[\\rm{a)}] etc.",
    "other", None, "high",
    "\\begin{enumerate}\n\\item[\\rm{a)}] $A$ est normal~;\n\\item[\\rm{b)}] $A$ est régulier~;\n\\item[\\rm{c)}] $A$ est un anneau de valuation~;\n\\end{enumerate}",
    "\\textit{a)} $A$ est normal~;\n\\textit{b)} $A$ est régulier~;\n\\textit{c)} $A$ est un anneau de valuation~;",
    "Checked on a crop. One edit for both differences (run-in layout and italic labels), as for Corollaire (2.3.15) on p. 28; the env body is roman.")
add(140, "proof of (7.1.7): '([13], t. I, p. 277)'", "([13], t. I, p. 277)",
    "(\\cite[t.~I, p.~277]{I-13}), which prints '([13, t. I, p. 277])'",
    "punctuation", None, "high", "(\\cite[t.~I, p.~277]{I-13})", "(\\cite{I-13}, t.~I, p.~277)")
o, n = bI("8.1.1")
add(140, "proof of (7.1.7): 'B_p domine A (I, 8.1.1)'", "bold I", "{I, 8.1.1}",
    "convention", 2, "high", o, n)
add(140, "proof of (7.1.7): 'th. de Krull-Akizuki ([25], p. 293)'", "([25], p. 293)",
    "(\\cite[p.~293]{II-25}), which prints '([25, p. 293])'",
    "punctuation", None, "high", "(\\cite[p.~293]{II-25})", "(\\cite{II-25}, p.~293)")
add(140, "proof of (7.1.7): 'de dimension 1 ([25], p. 295)'", "([25], p. 295)",
    "(\\cite[p.~295]{II-25}), which prints '([25, p. 295])'",
    "punctuation", None, "high", "(\\cite[p.~295]{II-25})", "(\\cite{II-25}, p.~295)")
add(140, "proof of (7.1.7): 'la proposition est classique ([24], p. 106)'", "([24], p. 106)",
    "(\\cite[p.~106]{II-24}), which prints '([24, p. 106])'",
    "punctuation", None, "high", "(\\cite[p.~106]{II-24})", "(\\cite{II-24}, p.~106)")

# ---------------- page 141 ----------------
add(141, "diagram (7.1.9.1): top vertex k(x)", "bold italic k", "& k(x) \\arrow[dl,...]",
    "convention", 1, "high", "& k(x)", "& \\boldsymbol{k}(x)")
add(141, "diagram (7.1.9.1): bottom left vertex k(b)", "bold italic k", "k(b) & ...",
    "convention", 1, "high", "k(b)", "\\boldsymbol{k}(b)")
add(141, "diagram (7.1.9.1): bottom right vertex k(y)", "bold italic k", "& k(y) \\arrow[u,...]",
    "convention", 1, "high", "& k(y)", "& \\boldsymbol{k}(y)")
add(141, "diagram (7.1.9.1): vertical arrow k(y) -> k(x), label pi",
    "pi to the right of the upward arrow", "\\arrow[u,\"\\pi\"]: tikz-cd sets the label to the left of an upward arrow",
    "formula", None, "high", "\\arrow[u,\"\\pi\"]", "\\arrow[u,\"\\pi\"']",
    "Checked by compiling the diagram (gamma, upper left, is already right).")
add(141, "diagram (7.1.9.1): horizontal arrow k(y) -> k(b), label phi",
    "phi below the leftward arrow", "\\arrow[l,\"\\varphi\"']: with the swap, tikz-cd sets the label above a leftward arrow",
    "formula", None, "high", "\\arrow[l,\"\\varphi\"']", "\\arrow[l,\"\\varphi\"]",
    "Checked by compiling the diagram.")
o, n = bI("6.3.4, (iv)")
add(141, "proof of (7.1.9): '(compte tenu de (I, 6.3.4, (iv)))'", "bold I", "{I, 6.3.4, (iv)}",
    "convention", 2, "high", o, n)
add(141, "proof of (7.1.9): 'que k(x) est une extension de type fini'", "bold italic k", "$k(x)$",
    "convention", 1, "high", "$k(x)$ est une extension", "$\\boldsymbol{k}(x)$ est une extension")
add(141, "proof of (7.1.9): 'de type fini de k(y)'", "bold italic k", "$k(y)$",
    "convention", 1, "high", "de $k(y)$", "de $\\boldsymbol{k}(y)$")
o, n = bI("6.4.11")
add(141, "proof of (7.1.9): '(I, 6.4.11)'", "bold I", "{I, 6.4.11}", "convention", 2, "high", o, n)
add(141, "proof of (7.1.9): 'et dont k(x) est le corps des fractions'", "bold italic k", "$k(x)$",
    "convention", 1, "high", "dont $k(x)$", "dont $\\boldsymbol{k}(x)$")
o, n = bI("6.6.2")
add(141, "proof of (7.1.9): 'localement noethériens (I, 6.6.2)'", "bold I", "{I, 6.6.2}", "convention", 2, "high", o, n)
o, n = bI("7.1.15")
add(141, "proof of (7.1.9): 'l'isomorphisme gamma (I, 7.1.15)'", "bold I", "{I, 7.1.15}", "convention", 2, "high", o, n)
add(141, "Proposition (7.2.1) b), end: 'telle que f(x') = x'", "f(x')=x (checked on a crop)", "$f(x')=x$",
    "misprint_in_print", None, "high", None, None,
    "The TeX keeps the printed reading. x' is a point of X and f(x') a point of Y; condition b) says that every specialization y' of f(x) is the image of a specialization of x (the proof: f(closure of {x}) = closure of {y}).",
    corrected="$f(x')=y'$")
add(141, "proof of (7.2.1): 'La condition b) exprime'", "label b) in italics", "upright b)",
    "italics", None, "high", "La condition b)", "La condition \\emph{b)}")
add(141, "proof of (7.2.1): 'conséquence de a).'", "a) in italics", "upright a)",
    "italics", None, "high", "conséquence de a).", "conséquence de \\emph{a)}.")
add(141, "proof of (7.2.1): 'Pour montrer que b) entraîne a),'", "b) and a) in italics", "upright b), a)",
    "italics", None, "high", "que b) entraîne a),", "que \\emph{b)} entraîne \\emph{a)},")
o, n = bI("5.2.1")
add(141, "proof of (7.2.1): 'espaces sous-jacents X' et Y' (I, 5.2.1)'", "bold I", "{I, 5.2.1}", "convention", 2, "high", o, n)
o, n = bI("5.2.2")
add(141, "proof of (7.2.1): 'soit commutatif (I, 5.2.2)'", "bold I", "{I, 5.2.2}", "convention", 2, "high", o, n)

# ---------------- page 142 ----------------
add(142, "proof of (7.2.1), first line: 'condition b) implique que f(X) = Y'", "b) in italics", "upright b)",
    "italics", None, "high", "condition b) implique", "condition \\emph{b)} implique")
add(142, "proof of (7.2.1): 'en vertu de b), il suffit'", "b) in italics", "upright b)",
    "italics", None, "high", "vertu de b),", "vertu de \\emph{b)},")
o, n = bI("6.6.5")
add(142, "proof of (7.2.1), end: '(I, 6.6.5)'", "bold I", "{I, 6.6.5}", "convention", 2, "high", o, n)
add(142, "Proposition (7.2.3), first line: '(resp. un préschéma localement noethérien)'",
    "'(resp.' and the closing parenthesis upright, the words inside italic",
    "all italic in the proposition environment", "convention", 6, "high",
    "(resp. un préschéma localement noethérien)",
    "\\textup{(resp.} un préschéma localement noethérien\\textup{)}", "Checked on a crop.")
add(142, "Proposition (7.2.3): '(resp. un morphisme localement de type fini)'",
    "'(resp.' and the closing parenthesis upright", "all italic", "convention", 6, "high",
    "(resp. un morphisme localement de type fini)",
    "\\textup{(resp.} un morphisme localement de type fini\\textup{)}", "Checked on a crop.")
add(142, "Proposition (7.2.3) b): '(resp. un anneau de valuation discrète)'",
    "'(resp.' and the closing parenthesis upright", "all italic", "convention", 6, "high",
    "(resp. un anneau de valuation discrète), deux\n$Y$-morphismes",
    "\\textup{(resp.} un anneau de valuation discrète\\textup{)}, deux\n$Y$-morphismes", "Checked on a crop.")
add(142, "Proposition (7.2.3) c): '(resp. un anneau de valuation discrète)'",
    "'(resp.' and the closing parenthesis upright", "all italic", "convention", 6, "high",
    "(resp. un anneau de valuation discrète), deux\n$Y'$-sections",
    "\\textup{(resp.} un anneau de valuation discrète\\textup{)}, deux\n$Y'$-sections", "Checked on a crop.")
add(142, "proof of (7.2.3): 'L'équivalence de b) et de c)'", "b) and c) in italics", "upright",
    "italics", None, "high", "de b) et de c)", "de \\emph{b)} et de \\emph{c)}")
o, n = bI("3.3.14")
add(142, "proof of (7.2.3): '(I, 3.3.14)'", "bold I", "{I, 3.3.14}", "convention", 2, "high", o, n)
add(142, "proof of (7.2.3): 'la condition b) est vérifiée'", "b) in italics", "upright b)",
    "italics", None, "high", "la condition b)\nest vérifiée", "la condition \\emph{b)}\nest vérifiée")
o, n = bI("7.2.2.1")
add(142, "proof of (7.2.3): '(I, 7.2.2.1)'", "bold I", "{I, 7.2.2.1}", "convention", 2, "high", o, n)
add(142, "proof of (7.2.3): 'Il reste à prouver que b) entraîne'", "b) in italics", "upright b)",
    "italics", None, "high", "prouver que b) entraîne", "prouver que \\emph{b)} entraîne")
o, n = bI("5.3.1")
add(142, "proof of (7.2.3): 'ce qui signifie (I, 5.3.1)'", "bold I", "{I, 5.3.1}", "convention", 2, "high", o, n)
o, n = bI("6.6.7")
add(142, "proof of (7.2.3): 'localement noethérien (I, 6.6.7)'", "bold I", "{I, 6.6.7}", "convention", 2, "high", o, n)
o, n = bI("6.6.4, (i)")
add(142, "Remarques (7.2.4) (i): '(I, 6.6.4, (i))'", "bold I", "{I, 6.6.4, (i)}", "convention", 2, "high", o, n)
add(142, "Remarques (7.2.4) (ii): 'la condition b) ou la condition c)'", "b) and c) in italics in the roman remark",
    "plain b), c)", "italics", None, "high",
    "que la condition b)\nou la condition c)", "que la condition \\emph{b)}\nou la condition \\emph{c)}",
    "Judged with the remark body roman (document-wide remark item); \\emph gives italics once the body is roman.")

# ---------------- page 143 ----------------
add(143, "Proposition (7.3.1): 'X un schéma intègre'", "'schéma' upright inside the italic statement",
    "italic", "convention", 6, "high", "$X$ un schéma intègre", "$X$ un \\textup{schéma} intègre", "Checked on a crop.")
add(143, "Proposition (7.3.1): 'un morphisme fermé tel que'", "'fermé' upright inside the italic statement",
    "italic", "convention", 6, "high", "morphisme fermé tel", "morphisme \\textup{fermé} tel", "Checked on a crop.")
add(143, "Proposition (7.3.1): 'k(b)->k(x)', first k", "bold italic k", "$k(b)\\to",
    "convention", 1, "high", "$k(b)\\to", "$\\boldsymbol{k}(b)\\to")
add(143, "Proposition (7.3.1): 'k(b)->k(x)', second k", "bold italic k", "k(x)$ soit bijectif",
    "convention", 1, "high", "k(x)$ soit bijectif", "\\boldsymbol{k}(x)$ soit bijectif")
o, n = bI("4.2.2")
add(143, "proof of (7.3.1): 'il suffit (I, 4.2.2)'", "bold I", "{I, 4.2.2}", "convention", 2, "high", o, n)
add(143, "proof of (7.3.1): 'il existe un seul point x''", "'un seul' in italics (both words)",
    "un \\emph{seul}", "italics", None, "high", "un \\emph{seul} point", "\\emph{un seul} point", "Checked on a crop.")
add(143, "proof of (7.3.1): 'K = k(x) = k(b)', first k", "bold italic k", "$K=k(x)",
    "convention", 1, "high", "$K=k(x)", "$K=\\boldsymbol{k}(x)")
add(143, "proof of (7.3.1): 'K = k(x) = k(b)', second k", "bold italic k", "=k(b)$ et dominant",
    "convention", 1, "high", "=k(b)$ et dominant", "=\\boldsymbol{k}(b)$ et dominant")
add(143, "proof of (7.3.1): '(0, 2.1.3)'", "bold 0", "{0, 2.1.3}", "convention", 2, "high",
    "{0, 2.1.3}", "{\\textbf{0}, 2.1.3}")
o, n = bI("8.2.2")
add(143, "proof of (7.3.1), end: '(I, 8.2.2)'", "bold I", "{I, 8.2.2}", "convention", 2, "high", o, n)
add(143, "(7.3.2): 'O_b = k(b)'", "bold italic k", "$\\mathcal{O}_b=k(b)$", "convention", 1, "high",
    "$\\mathcal{O}_b=k(b)$", "$\\mathcal{O}_b=\\boldsymbol{k}(b)$")
o, n = bI("7.1.4")
add(143, "(7.3.2): 'On sait (I, 7.1.4)'", "bold I", "{I, 7.1.4}", "convention", 2, "high", o, n)
add(143, "(7.3.2): 'les Y-sections rationnelles de X'", "'sections rationnelles' in italics",
    "only 'rationnelles' emphasized", "italics", None, "high",
    "$Y$-sections \\emph{rationnelles}", "$Y$-\\emph{sections rationnelles}", "Checked on a crop.")
o, n = bI("3.4.5")
add(143, "(7.3.2): 'par définition (I, 3.4.5)'", "bold I", "{I, 3.4.5}", "convention", 2, "high", o, n)
add(143, "(7.3.2): 'il résulte de (I, 5.4.7) que'", "bold I", "{I, 5.4.7}", "convention", 2, "high",
    "{I, 5.4.7}) que", "{\\textbf{I}, 5.4.7}) que")
o, n = bI("7.1.2")
add(143, "(7.3.2): 'Gamma(X/Y)->Gamma_rat(X/Y) (I, 7.1.2)'", "bold I", "{I, 7.1.2}", "convention", 2, "high", o, n)
add(143, "(7.3.2), end: 'encore injective (I, 5.4.7)'", "bold I", "{I, 5.4.7}", "convention", 2, "high",
    "{I, 5.4.7}).", "{\\textbf{I}, 5.4.7}).")
add(143, "Proposition (7.3.3): 'l'application canonique (7.3.2.2) est bijective'",
    "reference (7.3.2.2) upright inside the italic statement", "italic in the proposition environment",
    "convention", 6, "high",
    "(\\hyperref[II.7.3.2.2-fr]{7.3.2.2}) est bijective",
    "\\textup{(\\hyperref[II.7.3.2.2-fr]{7.3.2.2})} est bijective", "Checked on a crop.")
add(143, "Proposition (7.3.3): '(ce qui revient à dire ... partout définies)'",
    "the parenthesis is roman, with 'surjective' and 'partout définies' in italics",
    "italic parenthesis with upright \\emph words", "convention", 6, "high",
    "(ce qui revient à dire\nqu'elle est \\emph{surjective} et entraîne que les $Y$-sections rationnelles de\n$X$ sont \\emph{partout définies})",
    "\\textup{(ce qui revient à dire\nqu'elle est \\emph{surjective} et entraîne que les $Y$-sections rationnelles de\n$X$ sont \\emph{partout définies})}",
    "Checked on a crop. Inside \\textup the two \\emph give the printed italics.")
o, n = bI("5.5.1, (iv)")
add(143, "proof of (7.3.3): '(I, 5.5.1, (iv))'", "bold I", "{I, 5.5.1, (iv)}", "convention", 2, "high", o, n)
o, n = bI("5.4.6")
add(143, "proof of (7.3.3): 'immersion fermée (I, 5.4.6)'", "bold I", "{I, 5.4.6}", "convention", 2, "high", o, n)
add(143, "proof of (7.3.3): 'l'adhérence {x}‾ de {x} dans X'", "'dans' in italics", "upright 'dans'",
    "italics", None, "high", "dans $X$. Il est clair", "\\emph{dans} $X$. Il est clair", "Checked on a crop.")

# ---------------- page 144 ----------------
add(144, "Corollaire (7.3.5): 'n'est pas régulier (0, 4.1.4)'",
    "bold 0; the reference is upright inside the italic statement", "(\\hyperref[0.4.1.4-fr]{0, 4.1.4}) italic, plain 0",
    "convention", 2, "high",
    "(\\hyperref[0.4.1.4-fr]{0, 4.1.4})~;", "\\textup{(\\hyperref[0.4.1.4-fr]{\\textbf{0}, 4.1.4})}~;",
    "The fix also sets the reference upright (convention 6), as on pp. 37 and 40; no separate convention-6 entry. Checked on a crop.")
add(144, "Corollaire (7.3.5): 'un morphisme de type fini, séparé et fermé'", "'séparé' upright inside the italic statement",
    "italic", "convention", 6, "high", "fini,\nséparé et", "fini,\n\\textup{séparé} et", "Checked on a crop ('et' between them is italic).")
add(144, "Corollaire (7.3.5): 'séparé et fermé et soit g'", "'fermé' upright inside the italic statement",
    "italic", "convention", 6, "high", "fermé et soit $g$", "\\textup{fermé} et soit $g$", "Checked on a crop.")
add(144, "Corollaire (7.3.5): '(ensemble qui est fermé (I, 7.2.1))'",
    "the parenthesis is roman with 'fermé' in italics and bold I",
    "italic parenthesis, upright \\emph{fermé}, plain I", "convention", 6, "high",
    "(ensemble qui est\n\\emph{fermé} (\\hyperref[I.7.2.1-fr]{I, 7.2.1}))",
    "\\textup{(ensemble qui est\n\\emph{fermé} (\\hyperref[I.7.2.1-fr]{\\textbf{I}, 7.2.1}))}",
    "Checked on a crop. The edit also sets the bold I (convention 2); no separate convention-2 entry.")
o, n = bI("1.1.14")
add(144, "proof of (7.3.5): '(I, 1.1.14)'", "bold I", "{I, 1.1.14}", "convention", 2, "high", o, n)
add(144, "proof of (7.3.5): 'comme U = Y—Y' est partout dense'", "long dash Y—Y'", "$U=Y-Y'$",
    "convention", 7, "high", "$U=Y-Y'$", "$U=Y\\setmin Y'$", "\\setmin is not yet the long dash (global change pending).")
o, n = bI("2.4.2")
add(144, "proof of (7.3.5): '(I, 2.4.2)'", "bold I", "{I, 2.4.2}", "convention", 2, "high", o, n)
o, n = bI("7.2.8")
add(144, "proof of (7.3.5): '(I, 7.2.8)'", "bold I", "{I, 7.2.8}", "convention", 2, "high", o, n)
o, n = bI("7.2.9")
add(144, "proof of (7.3.5): '(I, 7.2.9)'", "bold I", "{I, 7.2.9}", "convention", 2, "high", o, n)
o, n = bI("5.5.1, (i)")
add(144, "proof of (7.3.5): '(I, 5.5.1, (i))'", "bold I", "{I, 5.5.1, (i)}", "convention", 2, "high", o, n)
o, n = bI("7.2.2")
add(144, "proof of (7.3.5), end: '(I, 7.2.2)'", "bold I", "{I, 7.2.2}", "convention", 2, "high", o, n)
o, n = bI("7.1.2")
add(144, "proof of (7.3.6): 'On sait (I, 7.1.2)'", "bold I", "{I, 7.1.2}", "convention", 2, "high", o, n)
add(144, "Remarque (7.3.7): 'normal (0, 4.1.4)'", "bold 0", "{0, 4.1.4}", "convention", 2, "high",
    "{0, 4.1.4}), en vertu", "{\\textbf{0}, 4.1.4}), en vertu")
add(144, "Théorème (7.3.8): '(resp. un préschéma localement noethérien)'",
    "'(resp.' and the closing parenthesis upright", "all italic", "convention", 6, "high",
    "(resp. un préschéma localement noethérien)",
    "\\textup{(resp.} un préschéma localement noethérien\\textup{)}", "Checked on a crop.")
add(144, "Théorème (7.3.8): '(resp. de type fini)'", "'(resp.' and the closing parenthesis upright",
    "all italic", "convention", 6, "high", "(resp. de type fini)", "\\textup{(resp.} de type fini\\textup{)}",
    "Checked on a crop.")
add(144, "Théorème (7.3.8) a): '(resp. propre)'", "'(resp.' and the closing parenthesis upright",
    "all italic", "convention", 6, "high", "(resp. propre)", "\\textup{(resp.} propre\\textup{)}",
    "Checked on a crop.")
add(144, "Théorème (7.3.8) b): '(resp. un anneau de valuation discrète)'", "'(resp.' upright",
    "all italic", "convention", 6, "medium", "(resp. un anneau\nde valuation discrète)",
    "\\textup{(resp.} un anneau\nde valuation discrète)",
    "Checked on a 3x crop: here the closing parenthesis looks italic (unlike the other '(resp. ...)' of the theorem), so it stays italic.")
add(144, "Théorème (7.3.8) b), end: '(resp. bijective)'", "'(resp.' and the closing parenthesis upright",
    "all italic", "convention", 6, "high", "(resp.\nbijective)", "\\textup{(resp.}\nbijective\\textup{)}",
    "Checked on a crop.")

# ---------------- validation ----------------
ok = True
pages = {}
for p in sorted({f["page"] for f in F}):
    raw = open(RUN + r"\page_%03d.tex" % p, "rb").read().decode("utf-8")
    pages[p] = raw.replace("\r\n", "\n")
for p, txt in pages.items():
    spans = []
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        old = f["fix"]["old"]
        c = txt.count(old)
        if c != 1:
            ok = False
            print("COUNT", c, "page", p, repr(old))
            continue
        i = txt.index(old)
        spans.append((i, i + len(old), old))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP page", p, repr(a[2]), repr(b[2]))
    # apply all fixes in sequence to check each old survives the others
    t = txt
    for f in F:
        if f["page"] == p and f["fix"]:
            if t.count(f["fix"]["old"]) != 1:
                ok = False
                print("SEQ", p, repr(f["fix"]["old"]))
            t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

# also check against the LF source segment
src = open(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current\packages\BASE\native\ega2\ega2-1-fr.tex", encoding="utf-8").read()
for p in pages:
    a = src.index("\\oldpage[II]{%d}" % p)
    b = src.index("\\oldpage[II]{%d}" % (p + 1))
    seg = src[a:b]
    for f in F:
        if f["page"] == p and f["fix"] and seg.count(f["fix"]["old"]) != 1:
            ok = False
            print("SRC", p, seg.count(f["fix"]["old"]), repr(f["fix"]["old"]))

from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in sorted(pages):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("OK" if ok else "PROBLEMS", len(F))
if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
