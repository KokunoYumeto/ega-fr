import json

RUN = r"user\Documents\ega_scan_check_20261101\run_IV1"
OUTFILE = RUN + r"\findings_247_251.json"

F = []


def add(page, where, scan, tex, kind, convention, confidence, fix, note="", corrected=None):
    item = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": fix,
    }
    if corrected is not None:
        item["corrected"] = corrected
    item["note"] = note
    F.append(item)


def fx(old, new):
    return {"old": old, "new": new}


# ---------------- page 247 ----------------
add(247, "proof of (1.9.14), lines 2-3: 'traduisent respectivement (1.9.5), (vi), (vii) et (viii)'",
    "(1.9.5), (vi), (vii) et (viii): the parenthesis closes after 1.9.5 (crop)",
    "traduisent respectivement (1.9.5), (vi), (vii) et (viii) (printed reading kept)",
    "misprint_in_print", None, "medium", None,
    "(iii), (iv) and (v) translate (1.9.5, (vi)), (1.9.5, (vii)) and (1.9.5, (viii)) respectively; the edition's reference "
    "form is (1.9.5, (vi)). Punctuation only; the TeX keeps the printed reading.",
    corrected="(1.9.5, (vi), (vii) et (viii))")

labels_247 = [
    ("Proposition (1.9.14), label (i)", "\\item[(i)] La topologie", "\\item[\\textup{(i)}] La topologie"),
    ("Proposition (1.9.14), label (ii)", "\\item[(ii)] Les parties", "\\item[\\textup{(ii)}] Les parties"),
    ("Proposition (1.9.14), label (iii)", "\\item[(iii)] Pour tout morphisme", "\\item[\\textup{(iii)}] Pour tout morphisme"),
    ("Proposition (1.9.14), label (iv)", "\\item[(iv)] Si le morphisme", "\\item[\\textup{(iv)}] Si le morphisme"),
    ("Proposition (1.9.14), label (v)", "\\item[(v)] Si un morphisme", "\\item[\\textup{(v)}] Si un morphisme"),
    ("Proposition (1.9.14), label (vi)", "\\item[(vi)] Pour tout ouvert", "\\item[\\textup{(vi)}] Pour tout ouvert"),
    ("Proposition (1.9.15), label (i)", "\\item[(i)] Pour que", "\\item[\\textup{(i)}] Pour que"),
    ("Proposition (1.9.15), label (ii)", "\\item[(ii)] Pour que", "\\item[\\textup{(ii)}] Pour que"),
    ("Proposition (1.9.15), label (iii)", "\\item[(iii)] Pour que", "\\item[\\textup{(iii)}] Pour que"),
    ("Proposition (1.9.15), label (iv)", "\\item[(iv)] Tout point", "\\item[\\textup{(iv)}] Tout point"),
    ("Proposition (1.9.15), label (v)", "\\item[(v)] Pour qu'un", "\\item[\\textup{(v)}] Pour qu'un"),
]
for where, old, new in labels_247:
    add(247, where, "label upright (crop)", "\\item[...] comes out italic inside the italic proposition",
        "convention", 6, "high", fx(old, new), "GLOBAL_ISSUES 16.")

# ---------------- page 248 ----------------
add(248, "line 1: 'voisinage ouvert affine U de X ne contenant pas y'",
    "capital X: 'U de X ne contenant pas y' (crop)",
    "voisinage ouvert affine $U$ de $X$ ne contenant pas $y$ (printed reading kept)",
    "misprint_in_print", None, "high", None,
    "Proof of (1.9.15, (ii)): x, y distinct with x not in the closure of {y}; the affine open U must be a neighbourhood of "
    "the point x (U and X-U then separate x and y in X^cons). A neighbourhood of X is meaningless here.",
    corrected="voisinage ouvert affine $U$ de $x$ ne contenant pas $y$")
add(248, "line 2: 'donc U et X\u2014U sont localement constructibles'",
    "long dash X\u2014U (set difference)", "$X-U$",
    "convention", 7, "high", fx("$X-U$", "$X\\setmin U$"),
    "\\setmin as in the earlier convention-7 fixes (IV-1 preamble must define it before the pass).")
add(248, "proof of (1.9.15, (v)), line 2: 'que f^cons est une application fermée.'",
    "'fermée' italic (crop)", "application fermée. (upright)",
    "italics", None, "high", fx("application fermée.", "application \\emph{fermée}."), "")
add(248, "display Z=f^{-1}(y)=X×_Y Spec(k(y))",
    "bold italic k in k(y)", "\\operatorname{Spec}(k(y))",
    "convention", 1, "high",
    fx("\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))"), "")

# ---------------- page 249 ----------------
add(249, "section heading '1.10. Application aux morphismes ouverts.'",
    "full stop after the title", "\\subsection{Application aux morphismes ouverts} (no full stop)",
    "punctuation", None, "high",
    fx("\\subsection{Application aux morphismes ouverts}", "\\subsection{Application aux morphismes ouverts.}"),
    "Same form as the earlier subsection page fixes (GLOBAL_ISSUES 43).")
add(249, "Théorème (1.10.1), line 1: 'une partie ind-constructible de X (1.9.4),'",
    "reference (1.9.4) upright inside the italic theorem (crop)", "(1.9.4) italic inside the theorem environment",
    "convention", 6, "high", fx("(1.9.4)", "\\textup{(1.9.4)}"), "")
add(249, "Théorème (1.10.1), line 2: 'toute générisation (0_I, 2.1.2) x''",
    "bold 0 (crop)", "$0_{\\mathrm I}$",
    "convention", 2, "high",
    fx("($0_{\\mathrm I}$, 2.1.2)", "\\textup{($\\mathbf{0}_{\\mathrm I}$, 2.1.2)}"),
    "One edit for this finding and the next (convention 6): bold 0 and the upright reference together.")
add(249, "Théorème (1.10.1): same reference '(0_I, 2.1.2)'",
    "the reference is upright inside the italic theorem (crop)",
    "($0_{\\mathrm I}$, 2.1.2) inside the italic theorem: italic",
    "convention", 6, "high", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(249, "Théorème (1.10.1), line 3: 'autrement dit (I, 2.4.2) que l'on ait'",
    "bold I (crop)", "(I, 2.4.2)",
    "convention", 2, "high",
    fx("(I, 2.4.2)", "\\textup{(\\textbf{I}, 2.4.2)}"),
    "One edit for this finding and the next (convention 6): bold I and the upright reference together.")
add(249, "Théorème (1.10.1): same reference '(I, 2.4.2)'",
    "the reference is upright inside the italic theorem (crop)",
    "(I, 2.4.2) inside the italic theorem: italic",
    "convention", 6, "high", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(249, "proof of (1.10.1): 'tels que f(X')=X\u2014E'",
    "long dash X\u2014E (set difference)", "$f(X')=X-E$",
    "convention", 7, "high", fx("$f(X')=X-E$", "$f(X')=X\\setmin E$"), "")
add(249, "proof of (1.10.1): '(en vertu de (I, 3.6.5))'",
    "bold I", "(I, 3.6.5)",
    "convention", 2, "high", fx("(I, 3.6.5)", "(\\textbf{I}, 3.6.5)"), "")
add(249, "proof of (1.10.1): 'où t parcourt A\u2014\U0001D52D'",
    "long dash A\u2014\U0001D52D (set difference)", "$A-\\mathfrak p$",
    "convention", 7, "high", fx("parcourt $A-\\mathfrak p$", "parcourt $A\\setmin\\mathfrak p$"), "")
add(249, "proof of (1.10.1): '(0_I, 1.4.5)'",
    "bold 0", "$0_{\\mathrm I}$",
    "convention", 2, "high",
    fx("($0_{\\mathrm I}$, 1.4.5)", "($\\mathbf{0}_{\\mathrm I}$, 1.4.5)"), "")
add(249, "proof of (1.10.1): 'il existe un t\u2208A\u2014\U0001D52D tel que'",
    "long dash A\u2014\U0001D52D (set difference)", "$t\\in A-\\mathfrak p$",
    "convention", 7, "high", fx("$t\\in A-\\mathfrak p$", "$t\\in A\\setmin\\mathfrak p$"), "")
for lab in ["a)", "b)", "b')", "c)"]:
    add(249, "Proposition (1.10.3), label " + lab,
        "label upright (crop)", "\\item[" + lab + "] comes out italic inside the italic proposition",
        "convention", 6, "high",
        fx("\\item[" + lab + "]", "\\item[\\textup{" + lab + "}]"), "")
add(249, "proof of (1.10.3), line 2: 'donc b) et b') sont équivalentes'",
    "b) and b') italic (crop)", "upright",
    "italics", None, "high",
    fx("donc b) et b') sont", "donc \\emph{b)} et \\emph{b')} sont"), "")
add(249, "proof of (1.10.3), line 2: 'Il est immédiat que c) entraîne b)'",
    "c) and b) italic (crop)", "upright",
    "italics", None, "high",
    fx("que c) entraîne b)", "que \\emph{c)} entraîne \\emph{b)}"), "")
add(249, "proof of (1.10.3): '(0_I, 2.1.5)'",
    "bold 0", "$0_{\\mathrm I}$",
    "convention", 2, "high",
    fx("($0_{\\mathrm I}$, 2.1.5)", "($\\mathbf{0}_{\\mathrm I}$, 2.1.5)"), "")
add(249, "proof of (1.10.3): 'Inversement, b) entraîne c) :'",
    "b) and c) italic (crop)", "upright",
    "italics", None, "high",
    fx("Inversement, b) entraîne c)", "Inversement, \\emph{b)} entraîne \\emph{c)}"), "")
add(249, "proof of (1.10.3), second paragraph: 'Pour voir que a) entraîne b')'",
    "a) and b') italic (crop)", "upright",
    "italics", None, "high",
    fx("que a) entraîne b')", "que \\emph{a)} entraîne \\emph{b')}"), "")

# ---------------- page 250 ----------------
add(250, "line 1: 'où t parcourt B\u2014\U0001D52E'",
    "long dash B\u2014\U0001D52E (set difference)", "$B-\\mathfrak q$",
    "convention", 7, "high", fx("parcourt $B-\\mathfrak q$", "parcourt $B\\setmin\\mathfrak q$"), "")
add(250, "line 1: 'On a, par suite (1.9.2), f(Spec(𝒪_{X,x})) = ⋂_t f(Spec(B_t)) = ⋂_t f(D(t)), et par hypothèse'",
    "the formula is set inline in the running text (crop)", "displayed with \\[ ... \\]",
    "other", None, "high",
    fx("(1.9.2),\n\\[\n  f(\\operatorname{Spec}(\\mathcal O_{X,x}))\n  =\\bigcap_t f(\\operatorname{Spec}(B_t))=\\bigcap_t f(\\mathrm D(t)),\n\\]\net par hypothèse",
       "(1.9.2),\n$f(\\operatorname{Spec}(\\mathcal O_{X,x}))\n=\\bigcap_t f(\\operatorname{Spec}(B_t))=\\bigcap_t f(\\mathrm D(t))$,\net par hypothèse"),
    "Layout only (display vs inline); the formula itself matches; no connecting words lost.")
add(250, "line 2: 'pour tout t\u2208B\u2014\U0001D52E'",
    "long dash B\u2014\U0001D52E (set difference)", "$t\\in B-\\mathfrak q$",
    "convention", 7, "high", fx("$t\\in B-\\mathfrak q$", "$t\\in B\\setmin\\mathfrak q$"), "")
add(250, "end of the proof of (1.10.3): 'b) implique a) en vertu de (1.10.2)'",
    "b) and a) italic (crop)", "upright",
    "italics", None, "high",
    fx("b)\nimplique a)", "\\emph{b)}\nimplique \\emph{a)}"), "")
for lab in ["a)", "b)", "b')", "c)"]:
    add(250, "Corollaire (1.10.4), label " + lab,
        "label upright (crop)", "\\item[" + lab + "] comes out italic inside the italic corollary",
        "convention", 6, "high",
        fx("\\item[" + lab + "]", "\\item[\\textup{" + lab + "}]"), "")
add(250, "proof of (1.10.4), line 2: 'donc les implications a)⇒b)⇔b') résultent'",
    "a), b), b') italic (crop)", "\\mathrm{a)}, \\mathrm{b)}, \\mathrm{b')} (upright)",
    "italics", None, "high",
    fx("$\\mathrm{a)}\\Rightarrow\\mathrm{b)}\\Leftrightarrow\\mathrm{b')}$ résultent",
       "$\\textit{a)}\\Rightarrow\\textit{b)}\\Leftrightarrow\\textit{b')}$ résultent"),
    "The labels in the statement's line 'Alors on a les implications ...' are upright, as in the TeX; only the proof has them italic.")
add(250, "proof of (1.10.4), line 3: 'ainsi que l'implication b)⇒a)'",
    "b) and a) italic (crop)", "\\mathrm (upright)",
    "italics", None, "high",
    fx("$\\mathrm{b)}\\Rightarrow\\mathrm{a)}$", "$\\textit{b)}\\Rightarrow\\textit{a)}$"), "")
add(250, "proof of (1.10.4), line 3: 'L'implication c)⇒b)'",
    "c) and b) italic (crop)", "\\mathrm (upright)",
    "italics", None, "high",
    fx("$\\mathrm{c)}\\Rightarrow\\mathrm{b)}$", "$\\textit{c)}\\Rightarrow\\textit{b)}$"), "")
add(250, "proof of (1.10.4), line 4: 'prouvons enfin que b) entraîne c).'",
    "b) and c) italic (crop)", "upright",
    "italics", None, "high",
    fx("que b) entraîne c)", "que \\emph{b)} entraîne \\emph{c)}"), "")

# ---------------- page 251 ----------------
add(251, "heading 'BIBLIOGRAPHIE (suite)'",
    "'(suite)' italic including the parentheses (crop)", "(\\emph{suite}): parentheses upright",
    "italics", None, "medium",
    fx("BIBLIOGRAPHIE (\\emph{suite})", "BIBLIOGRAPHIE \\textit{(suite)}"),
    "Form as the EGA III p. 161 fix.")
add(251, "[30] 'M. Nagata'",
    "surname in caps and small caps", "plain 'Nagata'",
    "font", None, "high", fx("[30] M.~Nagata", "[30] M.~\\textsc{Nagata}"), "")
add(251, "[30] title 'Local rings'",
    "title roman (crop)", "\\emph{Local rings} (italic)",
    "italics", None, "high", fx("\\emph{Local rings}", "Local rings"),
    "Titles roman, series/journal names italic, as in the other bibliographies.")
add(251, "[31] 'M. Nagata'",
    "surname in caps and small caps", "plain 'Nagata'",
    "font", None, "high", fx("[31] M.~Nagata", "[31] M.~\\textsc{Nagata}"), "")
add(251, "[31] title 'A Jacobian criterion of simple points'",
    "title roman (crop)", "\\emph{...} (italic)",
    "italics", None, "high",
    fx("\\emph{A Jacobian criterion of simple points}", "A Jacobian criterion of simple points"), "")
add(251, "[31] 'p. 427-432'",
    "hyphen between the page numbers (crop)", "en dash (--)",
    "punctuation", None, "high", fx("p.~427--432", "p.~427-432"), "As EGA III p. 161.")
add(251, "[32] 'A. Néron'",
    "surname in caps and small caps", "plain 'Néron'",
    "font", None, "high", fx("A.~Néron", "A.~\\textsc{Néron}"), "")
add(251, "[32] title 'Modèles minimaux des variétés abéliennes sur les corps locaux et globaux'",
    "title roman (crop)", "\\emph{...} (italic)",
    "italics", None, "high",
    fx("\\emph{Modèles minimaux des variétés abéliennes sur les corps\nlocaux et globaux}",
       "Modèles minimaux des variétés abéliennes sur les corps\nlocaux et globaux"), "")


def main():
    texts = {}
    bad = 0
    for it in F:
        p = it["page"]
        if p not in texts:
            with open(RUN + "\\page_%03d.tex" % p, encoding="utf-8", newline="") as fh:
                texts[p] = fh.read().replace(chr(13) + chr(10), chr(10))
        t = texts[p]
        if "\r" in t:
            print("CR in page", p)
        if it["fix"] is not None:
            n = t.count(it["fix"]["old"])
            if n != 1:
                bad += 1
                print("BAD", p, n, repr(it["fix"]["old"]))
        if it["kind"] == "misprint_in_print":
            tex = " ".join(it["tex"].split(" (printed")[0].split())
            print("misprint tex check", p, " ".join(t.split()).count(tex), repr(tex))
    # sequential application check per page
    for p, t in texts.items():
        s = t
        for it in F:
            if it["page"] == p and it["fix"] is not None:
                if s.count(it["fix"]["old"]) != 1:
                    print("SEQ-BAD", p, repr(it["fix"]["old"]))
                s = s.replace(it["fix"]["old"], it["fix"]["new"], 1)
    with open(OUTFILE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    from collections import Counter
    c = Counter()
    for it in F:
        k = "misprint" if it["kind"] == "misprint_in_print" else ("convention" if it["kind"] == "convention" else "normal")
        c[(it["page"], k)] += 1
    for p in sorted(texts):
        print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
    print("items", len(F), "bad", bad)


if __name__ == "__main__":
    main()
