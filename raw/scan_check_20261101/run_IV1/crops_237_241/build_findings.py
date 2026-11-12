"""Build findings_237_241.json for EGA IV-1 pp. 237-241 and check every fix.

Line breaks inside TeX strings are written as the placeholder NL (U+23CE) and
converted to LF before checking and writing.
usage: python -I build_findings.py <run folder> <outfile>
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN, OUT = sys.argv[1], sys.argv[2]
NL = "⏎"


def lf(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": lf(tex),
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": lf(old), "new": lf(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = lf(corrected)
    d["note"] = note
    F.append(d)


def c2(page, where, old, token, bold):
    """Convention 2: bold chapter number in a reference."""
    assert lf(old).count(lf(token)) == 1, (page, old, token)
    new = old.replace(token, token.replace(bold, r"\textbf{" + bold + "}", 1), 1)
    num = bold if bold != "0" else "0 (with subscript)"
    add(page, where, "bold " + num, "plain " + num, "convention", 2, "high", old, new)


def c1(page, where, old, arg):
    new = old.replace("k(" + arg + ")", r"\boldsymbol{k}(" + arg + ")", 1)
    assert new != old
    add(page, where, "bold italic k(" + arg + ")", "plain k(" + arg + ")", "convention", 1, "high", old, new)


# ---------------------------------------------------------------- page 237
P = 237
add(P, "top of page: continuation of (1.7.9) ('qui n'utilise que ...')",
    "the page begins mid-sentence, no paragraph break",
    r"\oldpage[IV-1]{237}⏎⏎qui n'utilise", "other", None, "high",
    r"\oldpage[IV-1]{237}⏎⏎qui", r"\oldpage[IV-1]{237}⏎qui",
    "Spurious paragraph break inside (1.7.9) (GLOBAL_ISSUES item 20). Apply together with removing the blank "
    "line before the marker at the end of page_236.tex ('démonstration,\\n\\n' -> 'démonstration,\\n'), "
    "which lies in the p. 236 segment.")
c2(P, "first line, (I, 9.4.7)", "que (I, 9.4.7). Dans", "(I,", "I")
c2(P, "first line, (I, 9.6.6)", "(I, 9.6.6)", "(I,", "I")
c2(P, "(1.7.10), (II, 1.7.15)", "(II, 1.7.15)", "(II,", "II")
c2(P, "(1.7.10), (I, 9.6.5)", "que (I, 9.6.5)", "(I,", "I")
c2(P, "(1.7.11), (II, 3.4.5)", "(II, 3.4.5)", "(II,", "II")
c2(P, "(1.7.11), (II, 3.4.8)", "(II, 3.4.8)", "(II,", "II")
c2(P, "(1.7.12), (II, 3.8.5)", "(II, 3.8.5)", "(II,", "II")
c2(P, "(1.7.12), (I, 9.4.7)", "séparé, cette hypothèse intervenant par (I, 9.4.7)", "(I,", "I")
c2(P, "(1.7.13), (II, 4.4.1, 4.4.6 et 4.4.7)", "(II, 4.4.1, 4.4.6 et 4.4.7)", "(II,", "II")
c2(P, "(1.7.13), (II, 4.4.7)", "(II, 4.4.7)", "(II,", "II")
c2(P, "(1.7.13), (II, 4.4.10.1)", "(II, 4.4.10.1)", "(II,", "II")
c2(P, "(1.7.14), (II, 4.5.2)", "(II, 4.5.2) et", "(II,", "II")
c2(P, "(1.7.14), (II, 4.5.5)", "(II, 4.5.5)", "(II,", "II")
c2(P, "(1.7.14), (I, 9.3.1 et 9.3.2)", "(I,⏎9.3.1 et 9.3.2)", "(I,", "I")
c2(P, "(1.7.15), (II, 4.6.8)", "(II, 4.6.8)", "(II,", "II")
c2(P, "(1.7.15), (I, 9.4.7)", "séparé}, cette hypothèse intervenant par (I, 9.4.7)", "(I,", "I")
c2(P, "(1.7.16), (II, 5.1.2)", "(II, 5.1.2)", "(II,", "II")
c2(P, "(1.7.16), (II, 4.5.2 et 4.5.5)", "(II, 4.5.2 et 4.5.5)", "(II,", "II")
c2(P, "(1.7.16), (II, 5.1.9)", "(II, 5.1.9)", "(II,", "II")
c2(P, "(1.7.16), (I, 9.6.5)", "utilise (I, 9.6.5)", "(I,", "I")
c2(P, "(1.7.17), (II, 5.2.1)", "(II, 5.2.1)", "(II,", "II")
c2(P, "(1.7.17), (II, 4.5.2)", "(II, 4.5.2))", "(II,", "II")
c2(P, "(1.7.18), (II, 5.2.2)", "(II, 5.2.2)", "(II,", "II")
add(P, "(1.7.18), 'il faut supposer f quasi-compact et X quasi-séparé'",
    "'quasi-compact' and 'quasi-séparé' italic",
    r"supposer $f$ quasi-compact et $X$ quasi-séparé~; (upright)", "italics", None, "high",
    r"supposer $f$ quasi-compact et $X$ quasi-séparé~;",
    r"supposer $f$ \emph{quasi-compact} et $X$ \emph{quasi-séparé}~;",
    "The same words later in (1.7.18) ('lorsque f est quasi-compact et X quasi-séparé') are roman, as in the TeX.")
add(P, "(1.7.18), sheaf letter F (twice)",
    "script F, the same glyph as the sheaf letter on p. 240",
    r"$\mathcal F$ on⏎a $\mathrm R^1f_*(\mathcal F)=0$", "font", None, "medium",
    r"$\mathcal F$ on⏎a $\mathrm R^1f_*(\mathcal F)=0$",
    r"$\mathscr F$ on⏎a $\mathrm R^1f_*(\mathscr F)=0$",
    "ega4-1-fr.tex writes this printed script F as \\mathscr F 20 times (e.g. (1.8.6), p. 240) and as \\mathcal F "
    "only here and once at source line 1159; \\mathcal gives the calligraphic shape. Cf. GLOBAL_ISSUES item 19.")
add(P, "(1.7.18), 'aux conditions b) et c')'",
    "the labels b) and c') italic",
    "conditions b) et c')) (upright)", "italics", None, "high",
    "conditions b) et c'))", r"conditions \emph{b)} et \emph{c')})",
    "The last parenthesis closes '(la même remarque ...' and stays roman.")
c2(P, "(1.7.18), (I, 9.4.7)", "(I, 9.4.7), modifié", "(I,", "I")
c2(P, "(1.7.19), (II, 5.3.2)", "(II, 5.3.2)", "(II,", "II")
c2(P, "(1.7.19), (II, 4.4.6 et 4.4.7)", "(II, 4.4.6 et 4.4.7)", "(II,", "II")
c2(P, "(1.7.19), (II, 5.5.3, (ii))", "(II,⏎5.5.3, (ii))", "(II,", "II")
c2(P, "(1.7.20), (III, 1.2.2, 1.2.3 et 1.2.4)", "(III, 1.2.2, 1.2.3 et 1.2.4)", "(III,", "III")
c2(P, "(1.7.20), (I, 9.3.3)", "(I, 9.3.3)", "(I,", "I")
c2(P, "(1.7.21), (III, 1.4.10 à 1.4.14)", "(III, 1.4.10 à 1.4.14)", "(III,", "III")
c2(P, "(1.7.21), (I, 9.2.2)", "(I,⏎9.2.2)", "(I,", "I")
c2(P, "(1.7.21), (III, 1.4.15)", "(III, 1.4.15)", "(III,", "III")
c2(P, "(1.7.22), (III, 2.1.3)", "(III, 2.1.3)", "(III,", "III")
c2(P, "(1.7.22), (III, 1.2.2)", "(III, 1.2.2)", "(III,", "III")
add(P, "subsection heading 1.8 (printed at the top of p. 238; in the TeX before the p. 238 marker)",
    "'1.8. Morphismes de présentation finie et ensembles constructibles.' (final full stop)",
    r"\subsection{Morphismes de présentation finie et ensembles constructibles}", "punctuation", None, "high",
    "ensembles constructibles}", "ensembles constructibles.}",
    "GLOBAL_ISSUES items 43/58: subsection titles lack the printed full stop. Independent of the marker move "
    "below (the two old strings do not overlap); if pages are re-split after the marker move, this heading "
    "falls in the p. 238 segment.")
add(P, "page break 237/238: the heading 1.8",
    "printed p. 238 begins with the heading '1.8. Morphismes de présentation finie ...'; p. 237 ends with (1.7.22)",
    r"\subsection{...}\label{subsection:IV.1.8-fr} stand before \oldpage[IV-1]{238}", "marker", None, "high",
    r"\subsection{Morphismes de présentation finie",
    r"\oldpage[IV-1]{238}⏎\subsection{Morphismes de présentation finie",
    "Must be applied together with the p. 238 entry that removes the old marker "
    "('\\oldpage[IV-1]{238}\\n\\n\\begin{env}[1.8.1]' -> '\\begin{env}[1.8.1]').")

# ---------------------------------------------------------------- page 238
P = 238
add(P, "top of page: the p. 238 marker after the 1.8 heading",
    "the heading 1.8 is the first line of printed p. 238",
    r"\oldpage[IV-1]{238} stands after \subsection{...}\label{subsection:IV.1.8-fr}", "marker", None, "high",
    r"\oldpage[IV-1]{238}⏎⏎\begin{env}[1.8.1]", r"\begin{env}[1.8.1]",
    "Removes the old marker; must be applied together with the p. 237 entry that inserts "
    "\\oldpage[IV-1]{238} before \\subsection{Morphismes de présentation finie ...}.")
c2(P, "(1.8.1), (0_III, 9.1.1)", r"(0\textsubscript{III}, 9.1.1)", "(0", "0")
c2(P, "(1.8.1), (0_III, 9.1.13)", r"(0\textsubscript{III}, 9.1.13)", "(0", "0")
c2(P, "(1.8.1), (0_III, 9.1.12)", r"(0\textsubscript{III}, 9.1.12)", "(0", "0")
c2(P, "(1.8.1), (0_III, 9.1.5)", r"(0\textsubscript{III}, 9.1.5)", "(0", "0")
add(P, "Proposition (1.8.2), first '(resp. localement constructible)'",
    "'resp.' roman inside the italic statement",
    "(resp. localement constructible) $Z$ (italic environment)", "convention", 6, "high",
    "(resp. localement constructible) $Z$", r"(\textup{resp.} localement constructible) $Z$")
add(P, "Proposition (1.8.2), second '(resp. localement constructible)'",
    "'resp.' roman inside the italic statement",
    "(resp. localement constructible) de $X$ (italic environment)", "convention", 6, "high",
    "(resp. localement constructible) de $X$", r"(\textup{resp.} localement constructible) de $X$")
c2(P, "proof of (1.8.2), (0_III, 9.1.3)", r"(0\textsubscript{III},⏎9.1.3)", "(0", "0")
add(P, "proof of (1.8.2), 'Z est ouvert et rétrocompact dans Y'",
    "'rétrocompact dans' italic",
    r"\emph{rétrocompact} dans⏎$Y$", "italics", None, "high",
    r"\emph{rétrocompact} dans⏎$Y$", r"\emph{rétrocompact dans}⏎$Y$",
    "In (1.8.1) ('rétrocompact dans X (0_III, 9.1.1)') 'dans' is roman, as in the TeX; later in this proof "
    "'rétrocompact dans X' is already \\emph{rétrocompact dans $X$}.")
c2(P, "proof of (1.8.2), (I, 4.4.1)", "(I, 4.4.1)", "(I,", "I")
c2(P, "proof of (1.8.3), (0_III, 9.1.8)", r"(0\textsubscript{III}, 9.1.8)", "(0", "0")
add(P, "proof of (1.8.3), 'on est ramené à prouver le lemme lorsque X_i est affine d'anneau A'",
    "X_i (subscript i clearly printed)",
    r"lorsque $X_i$ est \emph{affine} d'anneau $A$", "misprint_in_print", None, "low",
    None, None,
    "Probable misprint: the reduction is to the case X affine (each X_i is affine by choice), and the rest of "
    "the proof treats X itself as the affine scheme of A (X_{f_i}, 'sous-schéma fermé affine de X', "
    "'présentation finie sur X', X'=Z'x_X U). The TeX keeps the printed X_i. Low confidence: X_i can be read "
    "as 'for X_i'.",
    corrected=r"lorsque $X$ est \emph{affine} d'anneau $A$")
c2(P, "proof of (1.8.3), (0_III, 9.1.3)", r"(0\textsubscript{III}, 9.1.3)", "(0", "0")
add(P, "page break 238/239: 'Considérons le schéma affine X'=Z'x_X U / et soit f ...'",
    "the sentence runs on to p. 239 without a paragraph break",
    r"$X'=Z'\times_XU$⏎⏎ (blank line before \oldpage[IV-1]{239})", "other", None, "high",
    r"$X'=Z'\times_XU$⏎⏎", r"$X'=Z'\times_XU$⏎",
    "Spurious paragraph break (GLOBAL_ISSUES item 20); apply together with the p. 239 entry that removes the "
    "blank line after the marker.")

# ---------------------------------------------------------------- page 239
P = 239
add(P, "top of page: 'et soit f: X'->X le morphisme structural'",
    "continuation of the sentence from p. 238, no paragraph break",
    r"\oldpage[IV-1]{239}⏎⏎et soit", "other", None, "high",
    r"\oldpage[IV-1]{239}⏎⏎et soit", r"\oldpage[IV-1]{239}⏎et soit",
    "Apply together with the p. 238 entry that removes the blank line before the marker.")
c2(P, "proof of (1.8.3), end, (I, 3.4.8)", "(I, 3.4.8), ce qui", "(I,", "I")
add(P, "after the proof of (1.8.4.2): 'ses sous-Z-algèbres de type fini'",
    "'sous-Z-algèbres de type fini' all italic (Z bold)",
    r"sous-$\mathbf Z$-algèbres \emph{de type fini}", "italics", None, "high",
    r"sous-$\mathbf Z$-algèbres \emph{de type fini}", r"\emph{sous-$\mathbf Z$-algèbres de type fini}",
    "The next 'telle sous-Z-algèbre' is roman, as in the TeX.")
c2(P, "after (1.8.4.2), (I, 3.4.8)", "(I, 3.4.8) que", "(I,", "I")

# ---------------------------------------------------------------- page 240
P = 240
c2(P, "proof of (1.8.5), (0_III, 9.2.3)", r"(0\textsubscript{III}, 9.2.3)", "(0", "0")
c2(P, "proof of (1.8.5), (I, 5.2.1)", "(I, 5.2.1) et en", "(I,", "I")
add(P, "proof of (1.8.5), '(compte tenu de (1.5.4, (iii)) qu'on est ramené'",
    "three opening parentheses, two closing: the parenthesis opened before 'compte' is never closed",
    r"(compte tenu de⏎(1.5.4, (iii)) qu'on", "misprint_in_print", None, "high",
    None, None,
    "The TeX keeps the printed reading.",
    corrected=r"(compte tenu de⏎(1.5.4, (iii))) qu'on")
add(P, "proof of (1.8.5), 'si l'on suppose Y irréductible et f dominant'",
    "'irréductible' and 'dominant' italic, 'et' roman",
    r"\emph{irréductible et $f$ dominant}", "italics", None, "high",
    r"\emph{irréductible et $f$ dominant}", r"\emph{irréductible} et $f$ \emph{dominant}")
c2(P, "proof of (1.8.5), (I, 1.2.7)", "(I, 1.2.7). Il", "(I,", "I")
add(P, "proof of (1.8.5), 'tel que g notin j_y) l'idéal j_y'",
    "Fraktur j with subscript y, twice (the prime ideal of the point y, EGA notation)",
    r"$g\notin\mathfrak p_y$) l'idéal⏎$\mathfrak p_y$", "formula", None, "high",
    r"$g\notin\mathfrak p_y$) l'idéal⏎$\mathfrak p_y$",
    r"$g\notin\mathfrak j_y$) l'idéal⏎$\mathfrak j_y$",
    "Wrong letter: the print has the dotted Fraktur j, not Fraktur p (these are the only two \\mathfrak p_ "
    "in ega4-1-fr.tex).")
c1(P, "Corollaire (1.8.6), F_eta = F (x) k(eta)", r"\otimes_{\mathcal O_Y}k(\eta)", r"\eta")
c1(P, "Corollaire (1.8.6), F_y = F (x) k(y)", r"\otimes_{\mathcal O_Y}k(y)", "y")
c1(P, "proof of (1.8.6), Spec(k(y))", r"\operatorname{Spec}(k(y))", "y")
c2(P, "proof of (1.8.6), (I, 9.1.13.1)", "(I, 9.1.13.1)", "(I,", "I")
c2(P, "proof of (1.8.6), (I, 3.6.1)", "(I, 3.6.1)", "(I,", "I")
c2(P, "proof of (1.8.6), (0_I, 5.2.2)", r"(0\textsubscript{I},⏎5.2.2)", "(0", "0")
c2(P, "proof of (1.8.6), first (I, 5.2.1)", "(I, 5.2.1), et", "(I,", "I")
add(P, "proof of (1.8.6), 'autrement dit Y intègre'",
    "'intègre' italic",
    r"autrement dit $Y$ intègre. (upright)", "italics", None, "high",
    r"autrement dit $Y$ intègre.", r"autrement dit $Y$ \emph{intègre}.")
c2(P, "proof of (1.8.6), second (I, 5.2.1)", "(I, 5.2.1), on", "(I,", "I")
c2(P, "proof of (1.8.6), (I, 5.1.4)", "(I, 5.1.4)", "(I,", "I")
c2(P, "proof of (1.8.6), (I, 1.2.7)", "(I, 1.2.7)~;", "(I,", "I")

# ---------------------------------------------------------------- page 241
P = 241
c1(P, "Proposition (1.8.7), X_s = X x_S Spec(k(s))", r"X\times_S\operatorname{Spec}(k(s))", "s")
c1(P, "Proposition (1.8.7), Y_s = Y x_S Spec(k(s))", r"Y\times_S\operatorname{Spec}(k(s))", "s")
add(P, "Proposition (1.8.7), '(resp. radiciel)'",
    "'resp.' roman inside the italic statement",
    "(resp. radiciel) (italic environment)", "convention", 6, "high",
    "(resp. radiciel)", r"(\textup{resp.} radiciel)")
add(P, "proof of (1.8.7), S-E", "long dash for set difference: S—E", "$S-E$", "convention", 7, "high",
    "$S-E$", r"$S\setmin E$")
add(P, "proof of (1.8.7), first h(Y-f(X))", "long dash: h(Y—f(X))", "égal à $h(Y-f(X))$", "convention", 7,
    "high", "égal à $h(Y-f(X))$", r"égal à $h(Y\setmin f(X))$")
add(P, "proof of (1.8.7), second h(Y-f(X))", "long dash: h(Y—f(X))", "finie, $h(Y-f(X))$", "convention", 7,
    "high", "finie, $h(Y-f(X))$", r"finie, $h(Y\setmin f(X))$")
c2(P, "proof of (1.8.7.1), (I, 5.3.9)", "(I, 5.3.9)", "(I,", "I")
c2(P, "proof of (1.8.7.1), (1.3.7 et I, 3.4.2.1)", "(1.3.7 et I, 3.4.2.1)", "et I,", "I")
c2(P, "proof of (1.8.7.1), (I, 3.5.5)", "(I, 3.5.5)", "(I,", "I")
c1(P, "end of the proof of (1.8.7), Spec(k(s)) -> S", r"\operatorname{Spec}(k(s))\to S", "s")
c2(P, "end of the proof of (1.8.7), (I, 5.3.4)", "(I, 5.3.4)", "(I,", "I")
add(P, "subsection heading 1.9",
    "'1.9. Ensembles pro-constructibles et ind-constructibles.' (final full stop)",
    r"\subsection{Ensembles pro-constructibles et ind-constructibles}", "punctuation", None, "high",
    "ind-constructibles}", "ind-constructibles.}",
    "GLOBAL_ISSUES items 43/58.")
add(P, "Proposition (1.9.2), item (i): its label",
    "a new indented paragraph beginning with a roman, non-bold '(i)', then the italic text",
    r"\begin{env}[1.9.2.i] prints a bold '(1.9.2.i)'", "number", None, "high",
    r"\begin{env}[1.9.2.i]⏎\label{IV.1.9.2.i-fr}⏎\emph{Pour que",
    r"\setmanualcurrentlabel{1.9.2.i}\label{IV.1.9.2.i-fr}%⏎(i) \emph{Pour que",
    "Must be applied together with the next entry, which replaces the matching \\end{env}. The label keeps its "
    "text 1.9.2.i (nothing in the IV-1 sources references IV.1.9.2.i-fr). Item (ii), \\begin{env}[1.9.2.ii] "
    "on p. 242, has the same problem.")
add(P, "Proposition (1.9.2), item (i): end of the env",
    "(see the previous entry)",
    r"pour $\alpha\geq\gamma$.}⏎\end{env}", "number", None, "high",
    r"pour $\alpha\geq\gamma$.}⏎\end{env}", r"pour $\alpha\geq\gamma$.}\par",
    "Companion of the previous entry (the \\begin{env} it closes is removed there); apply both or neither.")

# ---------------------------------------------------------------- checks
pages = {}
for p in range(237, 242):
    with open(f"{RUN}/page_{p}.tex", encoding="utf-8") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")

bad = 0
for d in F:
    for key in ("where", "scan", "tex", "note", "corrected"):
        v = d.get(key)
        if isinstance(v, str) and any(ord(c) < 32 and c != "\n" for c in v):
            print("CONTROL CHAR", d["page"], key, repr(v)); bad += 1
    fx = d["fix"]
    if fx is None:
        continue
    for key in ("old", "new"):
        if any(ord(c) < 32 and c != "\n" for c in fx[key]) or NL in fx[key]:
            print("BAD CHAR", d["page"], key, repr(fx[key])); bad += 1
    n = pages[d["page"]].count(fx["old"])
    if n != 1:
        print("NOT UNIQUE", d["page"], n, repr(fx["old"])); bad += 1
    if fx["old"] == fx["new"]:
        print("NO-OP", d["page"], repr(fx["old"])); bad += 1

# apply the fixes of each page in list order to a copy: every old must still be found once
for p in pages:
    t = pages[p]
    for d in F:
        if d["page"] != p or d["fix"] is None:
            continue
        o, w = d["fix"]["old"], d["fix"]["new"]
        if t.count(o) != 1:
            print("SEQUENTIAL CONFLICT", p, repr(o)); bad += 1
            continue
        t = t.replace(o, w, 1)

# misprint 'tex' strings must occur in the page text
for d in F:
    if d["kind"] == "misprint_in_print" and pages[d["page"]].count(d["tex"]) != 1:
        print("MISPRINT TEX NOT FOUND", d["page"], repr(d["tex"])); bad += 1

counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts)
print("entries:", len(F), "problems:", bad)
if bad == 0:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(F, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("written", OUT)
