"""Build findings_227_231.json, check every fix's "old" against page_NNN.tex, and simulate the edits in order."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV1")
OUT = RUN / "findings_227_231.json"


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def ref2(page, where, ref, note=None):
    """Convention 2: bold chapter numeral I in a reference (I, n.n.n)."""
    return F(page, where, "(I, %s) with a bold I" % ref, "(I, %s), plain I" % ref, "convention", 2, "high",
             "(I, %s)" % ref, "(\\textbf{I}, %s)" % ref, note)


def label(page, where, old, lab, note="GLOBAL_ISSUES 16: item label printed upright inside the italic statement."):
    new = old.replace("\\item[%s]" % lab, "\\item[\\textup{%s}]" % lab, 1)
    return F(page, where, "label %s upright" % lab, "\\item[%s] inside the italic statement (typeset italic)" % lab,
             "convention", 6, "high", old, new, note)


L = []

# ---------------- p. 227 ----------------
L.append(F(227, "text before 'donc il en est de même de i' (printed as the last line of p. 226): '... et X×_Z X (I, 5.3.5)'",
           "(I, 5.3.5) with a bold I (page_226_s4.png, last line)", "(I, 5.3.5), plain I",
           "convention", 2, "high", "(I, 5.3.5)", "(\\textbf{I}, 5.3.5)",
           "Printed on p. 226 but placed after \\oldpage[IV-1]{227} in the TeX (see the two marker edits below). "
           "Listed first so that it is applied while the text is still inside the p. 227 segment."))
L.append(F(227, "page start: marker position (edit 1 of 2, insert)",
           "Printed p. 227 begins 'donc il en est de même de i (1.1.2, (iii)) ; si de plus f ...'. The lines "
           "'(où π est le morphisme structural) est commutatif et identifie X×_Y X au produit des (Y×_Z Y)-préschémas Y "
           "et X×_Z X (I, 5.3.5). Si g est quasi-séparé, Δ_g est quasi-compact,' are the last two lines of printed p. 226 "
           "(page_226_s4.png).",
           "\\oldpage[IV-1]{227} stands before '(où $\\pi$ est le morphisme structural)', two printed lines too early",
           "marker", None, "high",
           "quasi-compact, donc il en est de même de $i$",
           "quasi-compact,\n\\oldpage[IV-1]{227}\ndonc il en est de même de $i$",
           "Inserts the marker where p. 227 begins (mid-sentence, on its own line without blank lines, as in earlier "
           "marker moves). Apply together with the next edit, which removes the old marker; this order matches "
           "apply_fixes.py (a second copy of the marker extends the page segment until the first is removed)."))
L.append(F(227, "page start: marker position (edit 2 of 2, remove the misplaced marker)",
           "see the previous finding", "\\oldpage[IV-1]{227} directly before '(où $\\pi$'", "marker", None, "high",
           "\\oldpage[IV-1]{227}\n(où $\\pi$", "(où $\\pi$",
           "Apply together with the previous edit. After both, '(où $\\pi$ ... quasi-compact,' belongs to the p. 226 "
           "segment, matching the print; nothing is missing from p. 226."))
L.append(label(227, "Corollaire (1.2.3), label (i)", "\\item[(i)]", "(i)"))
L.append(label(227, "Corollaire (1.2.3), label (ii)", "\\item[(ii)]", "(ii)"))
L.append(ref2(227, "proof of (1.2.4), l. 1", "5.3.13"))
L.append(ref2(227, "proof of (1.2.4), l. 2", "3.3.4"))
L.append(ref2(227, "proof of (1.2.4), after (1.2.4.1)", "5.3.7"))
L.append(ref2(227, "proof of (1.2.5), l. 1", "5.3.4"))
L.append(ref2(227, "proof of (1.2.5), l. 2", "3.5.2"))
L.append(ref2(227, "proof of (1.2.5), l. 3", "3.3.11"))

# ---------------- p. 228 ----------------
L.append(label(228, "Proposition (1.2.7), label a)", "\\item[a)]", "a)",
               "Label printed upright (enlarged crop) inside the italic proposition; GLOBAL_ISSUES 16/22."))
L.append(label(228, "Proposition (1.2.7), label b)", "\\item[b)]", "b)",
               "Label printed upright (enlarged crop); GLOBAL_ISSUES 16/22."))
L.append(label(228, "Proposition (1.2.7), label b')", "\\item[b')]", "b')",
               "Label printed upright (enlarged crop); GLOBAL_ISSUES 16/22."))
L.append(label(228, "Proposition (1.2.7), label c)", "\\item[c)]", "c)",
               "Label printed upright (enlarged crop); GLOBAL_ISSUES 16/22."))
L.append(F(228, "Proposition (1.2.7) b): '(autrement dit, U est rétrocompact dans X).'",
           "the parenthesis is roman, only 'rétrocompact' italic (enlarged crop)",
           "whole parenthesis italic inside the italic proposition", "convention", 6, "high",
           "(autrement dit, $U$ est rétrocompact dans $X$)",
           "\\textup{(autrement dit, $U$ est \\emph{rétrocompact} dans $X$)}",
           "Inside \\textup the \\emph sets 'rétrocompact' italic, as printed."))
L.append(ref2(228, "proof of (1.2.7), l. 4", "3.2.7"))
L.append(F(228, "Proposition (1.2.9), last sentence", "Pour que f soit quasi-séparé, il faut et il suffit que f' et f'' le soient.",
           "Pour que $f$ soit quasi-séparé il faut et il suffit (no comma)", "punctuation", None, "high",
           "quasi-séparé il faut", "quasi-séparé, il faut", "Comma after 'quasi-séparé' (enlarged crop)."))
L.append(F(228, "Définition (1.3.2): 'de type fini en x'", "no change of face: italic like the rest of the definition (enlarged crop)",
           "\\emph{de type fini en $x$} inside the italic definition (typeset upright)", "convention", 6, "high",
           "\\emph{de type fini en $x$}", "de type fini en $x$", "Printed italic words left upright by \\emph."))
L.append(F(228, "Définition (1.3.2): 'localement de type fini'", "no change of face (enlarged crop)",
           "\\emph{localement de type fini} inside the italic definition (typeset upright)", "convention", 6, "high",
           "\\emph{localement de type fini}", "localement de type fini", "Printed italic words left upright by \\emph."))

# ---------------- p. 229 ----------------
L.append(ref2(229, "after Proposition (1.3.3)", "6.3.7"))
L.append(label(229, "Proposition (1.3.4), label (i)", "\\item[(i)] Toute", "(i)"))
L.append(label(229, "Proposition (1.3.4), label (ii)", "\\item[(ii)] Si deux", "(ii)"))
L.append(label(229, "Proposition (1.3.4), label (iii)", "\\item[(iii)]", "(iii)"))
L.append(label(229, "Proposition (1.3.4), label (iv)", "\\item[(iv)]", "(iv)"))
L.append(label(229, "Proposition (1.3.4), label (v)", "\\item[(v)]", "(v)"))
L.append(label(229, "Proposition (1.3.4), label (vi)", "\\item[(vi)]", "(vi)"))
L.append(ref2(229, "after Proposition (1.3.4)", "6.6.6"))
L.append(ref2(229, "after Proposition (1.3.6), l. 1", "6.3.3"))
L.append(ref2(229, "after Proposition (1.3.6), l. 2", "6.6.3"))
L.append(F(229, "Proposition (1.3.7): reference '(I, 3.4.1)' in the italic statement",
           "reference set roman: upright parentheses and figures", "(I, 3.4.1) inside the italic proposition (typeset italic)",
           "convention", 6, "high", "correspondant à $f$ (I, 3.4.1) soit", "correspondant à $f$ \\textup{(I, 3.4.1)} soit",
           "Apply before the convention-2 fix of the same reference (its 'old' lies inside this one)."))
L.append(ref2(229, "Proposition (1.3.7)", "3.4.1", "Apply after the convention-6 fix just above (the reference then stands inside \\textup)."))
L.append(ref2(229, "after Proposition (1.3.7)", "6.3.10"))
L.append(label(229, "Proposition (1.3.9), label (i)", "\\item[(i)] Si $B$ est une", "(i)"))
L.append(label(229, "Proposition (1.3.9), label (ii)", "\\item[(ii)] Soient $B$ une", "(ii)"))

# ---------------- p. 230 ----------------
L.append(F(230, "(1.3.10), l. 4: 'S=A—p'", "long dash for the set difference A—p (enlarged crop)", "S=A-\\mathfrak p",
           "convention", 7, "high", "S=A-\\mathfrak p", "S=A\\setmin\\mathfrak p",
           "\\setmin is not yet defined for IV-1 (FIX_POLICY 2.7: convention 7 waits for the global pass)."))
L.append(F(230, "(1.3.10), l. 5-6: 'une A_p-algèbre essentiellement de type fini'",
           "italic begins at 'algèbre': 'A_p-algèbre essen-|tiellement de type fini' (enlarged crop)",
           "$A_{\\mathfrak p}$-algèbre \\emph{essentiellement de type fini} ('algèbre' upright)", "italics", None, "high",
           "-algèbre \\emph{essentiellement de type fini}", "-\\emph{algèbre essentiellement de type fini}", None))
L.append(F(230, "(1.4.1), l. 4-5: 'A'-algèbre de présentation finie. étant isomorphe'",
           "full stop after 'finie' (no comma tail; enlarged crop), next line begins with lower-case 'étant'",
           "présentation finie, étant isomorphe (silently corrected)", "misprint_in_print", None, "high",
           "présentation finie, étant", "présentation finie. étant",
           "Misprint: full stop for a comma before 'étant'. The TeX silently corrected it; the fix restores the printed reading.",
           corrected="présentation finie, étant"))
L.append(F(230, "Définition (1.4.2): 'de présentation finie en x'", "no change of face: italic like the rest of the definition (enlarged crop)",
           "\\emph{de présentation finie en $x$} inside the italic definition (typeset upright)", "convention", 6, "high",
           "\\emph{de présentation finie en $x$}", "de présentation finie en $x$", "Printed italic words left upright by \\emph."))
L.append(F(230, "Définition (1.4.2): 'localement de présentation finie'", "no change of face (enlarged crop)",
           "\\emph{localement de présentation finie} inside the italic definition (typeset upright)", "convention", 6, "high",
           "\\emph{localement de présentation finie}", "localement de présentation finie", "Printed italic words left upright by \\emph."))
L.append(label(230, "Proposition (1.4.3), label (i)", "\\item[(i)]", "(i)"))
L.append(label(230, "Proposition (1.4.3), label (ii)", "\\item[(ii)]", "(ii)"))

# ---------------- p. 231 ----------------
L.append(label(231, "Proposition (1.4.3), label (iii)", "\\item[(iii)]", "(iii)"))
L.append(label(231, "Proposition (1.4.3), label (iv)", "\\item[(iv)]", "(iv)"))
L.append(label(231, "Proposition (1.4.3), label (v)", "\\item[(v)]", "(v)"))
L.append(ref2(231, "proof of (1.4.3), l. 2", "3.3.11"))
L.append(F(231, "proof of (1.4.3) (ii), l. 9: 'd'autre part B_s=B[T]/(1—sT)'",
           "d'autre part (the r is a broken sort, printed like a dotless ı, as in 'pıojections' on l. 2; not a different letter)",
           "d'aute part (r missing)", "word", None, "high", "d'aute part", "d'autre part", None))
L.append(F(231, "proof of (1.4.3) (ii), l. 9: 'B[T]/(1—sT)'", "long dash for the subtraction 1—sT (enlarged crop)", "(1-sT)",
           "convention", 7, "high", "(1-sT)", "(1\\setmin sT)",
           "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."))
L.append(ref2(231, "proof of (1.4.3), 'On sait que (iv) résulte'", "3.5.1"))
L.append(F(231, "proof of (1.4.3) (v), after the diagram: '(I, 5.3.7, Δ_g étant le morphisme diagonal)'",
           "(I, 5.3.7, ...) with a bold I", "(I, 5.3.7, plain I", "convention", 2, "high",
           "(I, 5.3.7,", "(\\textbf{I}, 5.3.7,", None))
L.append(ref2(231, "proof of (1.4.3) (v), factorisation of f", "5.3.13"))

# ---------------- checks ----------------
pages = {}
for p in sorted({x["page"] for x in L}):
    pages[p] = (RUN / ("page_%03d.tex" % p)).read_bytes().decode("utf-8").replace("\r\n", "\n")
ok = True
for i, x in enumerate(L):
    f = x["fix"]
    if f is None:
        continue
    c = pages[x["page"]].count(f["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE in original page", x["page"], c, repr(f["old"]))
# sequential simulation per page
sim = dict(pages)
for x in L:
    f = x["fix"]
    if f is None:
        continue
    t = sim[x["page"]]
    c = t.count(f["old"])
    if c != 1:
        ok = False
        print("SEQUENTIAL FAIL", x["page"], c, repr(f["old"]))
        continue
    sim[x["page"]] = t.replace(f["old"], f["new"])
print("all checks passed" if ok else "CHECK FAILURES")
counts = {}
for x in L:
    c = counts.setdefault(x["page"], [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print(counts)
json.dump(L, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("wrote", OUT, len(L))
print("--- simulated p. 227 start ---")
print(sim[227][:700])
