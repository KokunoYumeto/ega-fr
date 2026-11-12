"""Write findings_242_246.json and check every fix 'old' against page_NNN.tex (CRLF normalised to LF).

Also simulates applying the fixes page by page in list order: each 'old' must occur exactly once
at the moment it is applied.
"""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")

RUN = r"user\Documents\ega_scan_check_20261101\run_IV1"
OUT = RUN + r"\findings_242_246.json"
NL = "\n"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def conv1(page, where, old, new, note=""):
    add(page, where, "bold italic k in k(%s)" % ("y" if "k(y)" in old else "x"), "plain k", "convention", 1, "high", old, new, note)


def conv2(page, where, old, new, letter="0", note=""):
    add(page, where, "bold %s in the reference" % letter, "plain %s" % letter, "convention", 2, "high", old, new, note)


def conv7(page, where, scan, old, new, note="\\setmin is still '-' in the IV-1 preamble (FIX_POLICY 2.7: convention 7 waits for the global pass)."):
    add(page, where, scan + " with the long dash", "minus sign", "convention", 7, "high", old, new, note)


def label(page, where, lab, old, new):
    add(page, where, "label %s upright (enlarged crop)" % lab, "\\item label set in the italic of the statement",
        "convention", 6, "high", old, new, "GLOBAL_ISSUES 16: item label printed upright inside the italic statement.")


# ---------------------------------------------------------------- p. 242
P = 242
add(P, "(1.9.2) (ii), opening of the page: item heading",
    "'(ii) On a': item label (ii), upright and not bold, then italic 'On a' (enlarged crop)",
    "\\begin{env}[1.9.2.ii] prints the bold heading '(1.9.2.ii)' before 'On a'",
    "other", None, "high",
    r"\begin{env}[1.9.2.ii]" + NL + r"\label{IV.1.9.2.ii-fr}" + NL + r"\emph{On a}" + NL + r"\[" + NL
    + r"  u(X)=\bigcap_{\alpha\in I}u_\alpha(X_\alpha). \tag{1.9.2.1}" + NL + r"  \label{IV.1.9.2.1-fr}" + NL
    + r"\]" + NL + r"\end{env}",
    r"(ii) {\setmanualcurrentlabel{1.9.2.ii}\label{IV.1.9.2.ii-fr}}\emph{On a}" + NL + r"\[" + NL
    + r"  u(X)=\bigcap_{\alpha\in I}u_\alpha(X_\alpha). \tag{1.9.2.1}" + NL + r"  \label{IV.1.9.2.1-fr}" + NL
    + r"\]",
    "The env environment prints its whole optional argument in bold; the print labels the item '(ii)' only, as part of "
    "Proposition (1.9.2). One edit for the block: the display is unchanged, the label IV.1.9.2.ii-fr is kept (it is "
    "not referenced anywhere), and the blank line after the block still ends the paragraph. Item (i) on p. 241 "
    "(\\begin{env}[1.9.2.i], ega4-1-fr.tex l. 1606) has the same construction and needs the same change.")
conv7(P, "proof of (1.9.2), l. 3: 'soit y∈Y—u(X)'", "Y—u(X)", r"$y\in Y-u(X)$", r"$y\in Y\setmin u(X)$")
conv1(P, "proof of (1.9.2), l. 4: 'k(y)-préschéma'", r"$k(y)$-préschéma", r"$\boldsymbol{k}(y)$-préschéma")
conv1(P, "proof of (1.9.2), l. 4: 'Spec(A⊗_B k(y))'", r"\operatorname{Spec}(A\otimes_Bk(y))",
      r"\operatorname{Spec}(A\otimes_B\boldsymbol{k}(y))")
conv1(P, "proof of (1.9.2), l. 5: 'A⊗_B k(y) est limite'", r"$A\otimes_Bk(y)$ est", r"$A\otimes_B\boldsymbol{k}(y)$ est")
conv1(P, "proof of (1.9.2), l. 6: 'A_α⊗_B k(y); le lemme'", r"$A_\alpha\otimes_Bk(y)$~;",
      r"$A_\alpha\otimes_B\boldsymbol{k}(y)$~;")
conv1(P, "proof of (1.9.2), l. 7: 'A_α⊗_B k(y)=0'", r"$A_\alpha\otimes_Bk(y)=0$", r"$A_\alpha\otimes_B\boldsymbol{k}(y)=0$")
label(P, "Proposition (1.9.3), label a)", "a)", r"\item[a)]", r"\item[\textup{a)}]")
label(P, "Proposition (1.9.3), label a')", "a')", r"\item[a$'$)]", r"\item[\textup{a$'$)}]")
label(P, "Proposition (1.9.3), label a'')", "a'')", r"\item[a$''$)]", r"\item[\textup{a$''$)}]")
add(P, "Proposition (1.9.3) a''), l. 1: 'un schéma affine X'_α'",
    "X'_α with one prime (enlarged crop)", "X''_α", "formula", None, "high",
    r"schéma affine $X''_\alpha$", r"schéma affine $X'_\alpha$",
    "The print states a'') with the letters of a') (X'_α, f_α), and the proof that a'') implies a) uses them (three "
    "findings below); the TeX renamed them X''_α, f'_α. The printed notation is consistent (the proof that a') implies "
    "a'') builds X''_α, f'_α as witnesses of a''), as printed), so this is not a misprint.")
add(P, "Proposition (1.9.3) a''), l. 1: 'un morphisme f_α: X'_α→X_α'",
    "f_α : X'_α→X_α (no prime on f, one on X; enlarged crop)", "f'_α:X''_α\\to X_α", "formula", None, "high",
    r"$f'_\alpha:X''_\alpha\to X_\alpha$", r"$f_\alpha:X'_\alpha\to X_\alpha$", "See the previous finding.")
add(P, "Proposition (1.9.3) a''), l. 2: 'f_α(X'_α)=E_α'",
    "f_α(X'_α)=E_α (enlarged crop)", "f'_α(X''_α)=E_α", "formula", None, "high",
    r"$f'_\alpha(X''_\alpha)=E_\alpha$", r"$f_\alpha(X'_\alpha)=E_\alpha$", "See the finding on 'schéma affine X'_α'.")
label(P, "Proposition (1.9.3), label b)", "b)", r"\item[b)]", r"\item[\textup{b)}]")
label(P, "Proposition (1.9.3), label b')", "b')", r"\item[b$'$)]", r"\item[\textup{b$'$)}]")
conv7(P, "Proposition (1.9.3) b'): 'F=X—E'", "X—E", r"$F=X-E$", r"$F=X\setmin E$")
add(P, "proof of (1.9.3), a'') implies a): 'soit X' le préschéma somme des X'_α pour α∈J'",
    "X'_α with one prime (enlarged crop)", "X''_α", "formula", None, "high",
    r"somme des $X''_\alpha$ pour", r"somme des $X'_\alpha$ pour",
    "Notation of a'') as printed; see the finding on 'schéma affine X'_α'.")
add(P, "proof of (1.9.3), a'') implies a): 'le morphisme coïncidant avec j_α∘f_α pour tout α∈J'",
    "j_α∘f_α (no prime; enlarged crop)", "j_\\alpha\\circ f'_\\alpha", "formula", None, "high",
    r"$j_\alpha\circ f'_\alpha$ pour tout", r"$j_\alpha\circ f_\alpha$ pour tout",
    "Notation of a'') as printed.")
add(P, "proof of (1.9.3), a'') implies a): 'il en est de même de j_α∘f_α (1.1.1 et 1.1.2)'",
    "j_α∘f_α (no prime; enlarged crop)", "j_\\alpha\\circ f'_\\alpha", "formula", None, "high",
    r"$j_\alpha\circ f'_\alpha$ (1.1.1", r"$j_\alpha\circ f_\alpha$ (1.1.1",
    "Notation of a'') as printed.")
conv2(P, "proof of (1.9.3), a'') implies b): '(0_III, 9.1.8, (ii))'",
      r"(0\textsubscript{III}, 9.1.8, (ii))", r"(\textbf{0}\textsubscript{III}, 9.1.8, (ii))")

# ---------------------------------------------------------------- p. 243
P = 243
add(P, "Lemme (1.9.3.1), end: 'de présentation finie (1.4.1).'",
    "reference (1.4.1) upright: upright parentheses and figures (enlarged crop)",
    "(1.4.1) set in the italic of the lemma environment", "convention", 6, "high",
    "finie (1.4.1).", r"finie \textup{(1.4.1)}.", "")
conv2(P, "after Lemme (1.9.3.1): '(0_III, 9.1.8, (i))'",
      r"(0\textsubscript{III}, 9.1.8, (i))", r"(\textbf{0}\textsubscript{III}, 9.1.8, (i))")
conv2(P, "proof of Lemme (1.9.3.2): '(I, 3.4.7)'", "(I, 3.4.7)", r"(\textbf{I}, 3.4.7)", letter="I")
add(P, "Définition (1.9.4), l. 1-2: 'est pro-constructible (resp.'",
    "pro-constructible in the italic of the statement, no change of face; '(resp.' upright (enlarged crops)",
    "\\emph sets pro-constructible upright inside the italic definition; '(resp.' italic",
    "convention", 6, "high",
    r"\emph{pro-constructible} (resp.", r"pro-constructible \textup{(resp.}",
    "Printed italic word left upright by \\emph, and a roman '(resp.' set italic.")
add(P, "Définition (1.9.4), l. 2: 'ind-constructible) dans X si'",
    "ind-constructible in the italic of the statement; closing parenthesis upright (enlarged crop)",
    "\\emph sets ind-constructible upright; ')' italic", "convention", 6, "high",
    r"\emph{ind-constructible}) dans", r"ind-constructible\textup{)} dans",
    "Adjacent to the previous finding, no overlap.")
add(P, "Définition (1.9.4), l. 3: 'soit intersection (resp. réunion) de parties'",
    "'(resp.' and ')' upright, 'réunion' italic (enlarged crop)", "all italic", "convention", 6, "high",
    "intersection (resp. réunion) de parties", r"intersection \textup{(resp.} réunion\textup{)} de parties", "")
conv2(P, "last paragraph: '(0_III, 9.1.8 et 9.1.12)'",
      r"(0\textsubscript{III}, 9.1.8 et 9.1.12)", r"(\textbf{0}\textsubscript{III}, 9.1.8 et 9.1.12)")

# ---------------------------------------------------------------- p. 244
P = 244
RESP_SCAN = "'(resp.' and the closing parenthesis upright, the word inside italic (enlarged crops)"
RESP_TEX = "all italic inside the proposition environment"
label(P, "Proposition (1.9.5), label (i)", "(i)", r"\item[(i)]", r"\item[\textup{(i)}]")
conv7(P, "Proposition (1.9.5) (i): 'X—E soit ind-constructible'", "X—E", r"que $X-E$ soit", r"que $X\setmin E$ soit")
label(P, "Proposition (1.9.5), label (ii)", "(ii)", r"\item[(ii)]", r"\item[\textup{(ii)}]")
label(P, "Proposition (1.9.5), label (iii)", "(iii)", r"\item[(iii)]", r"\item[\textup{(iii)}]")
add(P, "Proposition (1.9.5) (iii), l. 1: 'Toute intersection (resp. réunion)'", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "intersection (resp. réunion) de parties localement",
    r"intersection \textup{(resp.} réunion\textup{)} de parties localement", "")
add(P, "Proposition (1.9.5) (iii), l. 2: 'pro-constructible (resp. ind-constructible). Inversement'", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "(resp. ind-constructible)." + NL + "  Inversement",
    r"\textup{(resp.} ind-constructible\textup{)}." + NL + "  Inversement", "")
add(P, "Proposition (1.9.5) (iii), l. 3: 'toute partie pro-constructible (resp. ind-constructible) de X'", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "(resp. ind-constructible) de $X$ est",
    r"\textup{(resp.} ind-constructible\textup{)} de $X$ est", "")
add(P, "Proposition (1.9.5) (iii), l. 3-4: 'est intersection (resp. réunion) de parties constructibles'", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "intersection (resp." + NL + "  réunion) de parties constructibles",
    r"intersection \textup{(resp.}" + NL + r"  réunion\textup{)} de parties constructibles", "")
label(P, "Proposition (1.9.5), label (iv)", "(iv)", r"\item[(iv)]", r"\item[\textup{(iv)}]")
add(P, "Proposition (1.9.5) (iv), l. 1-2: 'soit pro-constructible (resp. ind-constructible) dans X'", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "(resp. ind-constructible) dans" + NL + "  $X$, il faut",
    r"\textup{(resp.} ind-constructible\textup{)} dans" + NL + "  $X$, il faut", "")
add(P, "Proposition (1.9.5) (iv), l. 3: '(rep. ind-constructible) dans U_α'", RESP_SCAN.replace("resp.", "rep."), RESP_TEX,
    "convention", 6, "high",
    r"(rep. ind-constructible) dans $U_\alpha$",
    r"\textup{(rep.} ind-constructible\textup{)} dans $U_\alpha$",
    "Keeps the printed 'rep.' (misprint, next finding).")
add(P, "Proposition (1.9.5) (iv), l. 3: '(rep. ind-constructible)'",
    "'(rep.' for '(resp.' (enlarged crop)", "'(rep.': printed reading kept", "misprint_in_print", None, "high",
    None, None,
    "The TeX keeps the printed reading. After the convention-6 edit above the TeX reads "
    "'\\textup{(rep.} ind-constructible\\textup{)}'; the corrected edition changes only 'rep.' to 'resp.', as in the "
    "seven other '(resp. ...)' of this proposition.",
    corrected=r"\textup{(resp.} ind-constructible\textup{)}")
label(P, "Proposition (1.9.5), label (v)", "(v)", r"\item[(v)]", r"\item[\textup{(v)}]")
label(P, "Proposition (1.9.5), label (vi)", "(vi)", r"\item[(vi)]", r"\item[\textup{(vi)}]")
add(P, "Proposition (1.9.5) (vi), l. 2: '(resp. ind-constructible) E de X'", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "(resp. ind-constructible) $E$ de $X$",
    r"\textup{(resp.} ind-constructible\textup{)} $E$ de $X$", "")
add(P, "Proposition (1.9.5) (vi), l. 2: '(resp. ind-constructible) dans X''", RESP_SCAN, RESP_TEX,
    "convention", 6, "high",
    "(resp. ind-constructible) dans $X'$",
    r"\textup{(resp.} ind-constructible\textup{)} dans $X'$", "")
label(P, "Proposition (1.9.5), label (vii)", "(vii)", r"\item[(vii)]", r"\item[\textup{(vii)}]")
label(P, "Proposition (1.9.5), label (viii)", "(viii)", r"\item[(viii)]", r"\item[\textup{(viii)}]")
label(P, "Proposition (1.9.5), label (ix)", "(ix)", r"\item[(ix)]", r"\item[\textup{(ix)}]")
conv2(P, "proof of (1.9.5), (iii): '(1.2.7) et (0_III, 9.1.8, (ii))'",
      r"(0\textsubscript{III}, 9.1.8, (ii))", r"(\textbf{0}\textsubscript{III}, 9.1.8, (ii))")
conv2(P, "proof of (1.9.5), (v): 'E est quasi-compact (0_III, 9.1.1)'",
      r"(0\textsubscript{III}, 9.1.1)", r"(\textbf{0}\textsubscript{III}, 9.1.1)")

# ---------------------------------------------------------------- p. 245
P = 245
add(P, "proof of (1.9.5) (vii), end: 'puisque g∘f est quasi-compact'",
    "g∘f (enlarged crop)", "$g\\circ f$: printed reading kept", "misprint_in_print", None, "high",
    None, None,
    "The TeX keeps the printed reading. g: X''→X' and f: X'→X, so the quasi-compact composite is f∘g "
    "(f(E')=f(g(X'')) in the same sentence; compositions are written in this order elsewhere, e.g. "
    "f'_α=f_α∘g_α on p. 242).",
    corrected=r"$f\circ g$")
conv2(P, "proof of (1.9.5) (v), second assertion: '(I, 5.2.1)'", "(I," + NL + "5.2.1)", r"(\textbf{I}," + NL + "5.2.1)",
      letter="I")
add(P, "Exemples (1.9.6): heading",
    "'Exemples (1.9.6). — Toute partie finie': 'Exemples' italic, the number printed once; body roman",
    "\\begin{env}[1.9.6] prints a bold '(1.9.6)', then the hand-made '\\textbf{Exemples} (1.9.6). ---': "
    "number twice, 'Exemples' bold", "other", None, "high",
    r"\begin{env}[1.9.6]" + NL + r"\label{IV.1.9.6-fr}" + NL + r"\textbf{Exemples} (1.9.6). --- Toute",
    r"\begin{examples}[1.9.6]" + NL + r"\label{IV.1.9.6-fr}" + NL + "Toute",
    "Edit 1 of 2: use the examples environment of the IV-1 preamble (italic 'Exemples (1.9.6). ---', roman body, "
    "as printed; the number font is the document-wide heading item). Apply together with edit 2 "
    "(\\end{env} -> \\end{examples}) at the end of the examples.")
conv1(P, "Exemples (1.9.6), l. 2: 'l'image de Spec(k(x))'", r"\operatorname{Spec}(k(x))$ par",
      r"\operatorname{Spec}(\boldsymbol{k}(x))$ par")
conv1(P, "Exemples (1.9.6), l. 3: 'Spec(k(x))→X'", r"\operatorname{Spec}(k(x))\to X",
      r"\operatorname{Spec}(\boldsymbol{k}(x))\to X")
conv2(P, "Exemples (1.9.6), first paragraph: '(0_III, 9.2.2)'",
      r"(0\textsubscript{III}, 9.2.2)", r"(\textbf{0}\textsubscript{III}, 9.2.2)")
conv2(P, "Exemples (1.9.6), first paragraph: 'théorème d'Artin-Tate (0, 16.3.3)'",
      "(0, 16.3.3)", r"(\textbf{0}, 16.3.3)")
conv2(P, "Exemples (1.9.6), third paragraph: '(0_III, 9.1.7)'",
      r"(0\textsubscript{III}, 9.1.7)", r"(\textbf{0}\textsubscript{III}, 9.1.7)")
add(P, "Exemples (1.9.6): end of the examples",
    "the examples end before Théorème (1.9.7)", "\\end{env}", "other", None, "high",
    r"localement fermées de $X$}." + NL + r"\end{env}",
    r"localement fermées de $X$}." + NL + r"\end{examples}",
    "Edit 2 of 2: apply together with edit 1 (\\begin{env}[1.9.6] -> \\begin{examples}[1.9.6]).")
conv7(P, "proof of Théorème (1.9.7): 'F=X—E'", "F=X—E", r"$F=X-E$", r"$F=X\setmin E$")

# ---------------------------------------------------------------- p. 246
P = 246
conv2(P, "proof of (1.9.10), l. 3: 'espace sous-jacent (I, 5.2.1)'", "(I, 5.2.1)", r"(\textbf{I}, 5.2.1)", letter="I")
conv2(P, "proof of (1.9.10), l. 8: 'x∈U∩∁V⊂E∩Y (0_III, 9.1.3)'",
      r"(0\textsubscript{III}, 9.1.3)", r"(\textbf{0}\textsubscript{III}, 9.1.3)")
add(P, "proof of (1.9.10), second paragraph: 'au cas où X est noethérien'",
    "'noethérien' italic (enlarged crop)", "roman", "italics", None, "high",
    "au cas où $X$ est noethérien.", r"au cas où $X$ est \emph{noethérien}.", "")
conv7(P, "Proposition (1.9.11) c): 'E et X—E sont pro-constructibles'", "X—E",
      r"$X-E$ sont pro-constructibles", r"$X\setmin E$ sont pro-constructibles",
      "The labels a)-d) of (1.9.11) are italic in the print, as in the TeX. " +
      "\\setmin is still '-' in the IV-1 preamble (FIX_POLICY 2.7: convention 7 waits for the global pass).")
conv7(P, "Proposition (1.9.11) d): 'E et X—E sont ind-constructibles'", "X—E",
      r"$X-E$ sont ind-constructibles", r"$X\setmin E$ sont ind-constructibles")
conv7(P, "proof of (1.9.11), l. 2: 'E (resp. X—E) est réunion'", "X—E",
      r"(resp. $X-E$)", r"(resp. $X\setmin E$)")
add(P, "proof of (1.9.11), l. 3: 'une famille (E_λ) (resp. E'_μ)) de parties constructibles'",
    "'(resp. E'_μ))': no opening parenthesis before E'_μ (enlarged crop)",
    "'(resp. $(E'_\\mu)$)': silent correction", "misprint_in_print", None, "high",
    r"(resp. $(E'_\mu)$)", r"(resp. $E'_\mu$))",
    "Misprint: the family (E'_μ) lost its opening parenthesis (unbalanced in the print). The fix restores the printed "
    "reading in the diplomatic text.",
    corrected=r"(resp. $(E'_\mu)$)")
add(P, "Corollaire (1.9.12), l. 3: '(resp. pro-constructible, resp. ind-constructible)'",
    "both 'resp.' and the parentheses upright, the adjectives italic (enlarged crop)",
    "all italic inside the corollary environment", "convention", 6, "high",
    "(resp. pro-constructible, resp. ind-constructible)",
    r"\textup{(resp.} pro-constructible, \textup{resp.} ind-constructible\textup{)}", "")

# ---------------------------------------------------------------- write and check
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

ok = True
texts = {}
for p in range(242, 247):
    texts[p] = open(RUN + "\\page_%03d.tex" % p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
work = dict(texts)
for i, f in enumerate(F):
    if not f["fix"]:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    n0 = texts[f["page"]].count(old)
    n1 = work[f["page"]].count(old)
    if n0 != 1 or n1 != 1:
        ok = False
        print("PROBLEM", i, f["page"], repr(old), "original count", n0, "sequential count", n1)
    else:
        work[f["page"]] = work[f["page"]].replace(old, new, 1)
    if "\r" in old or "\r" in new:
        ok = False
        print("CR in fix", i)
from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for p in range(242, 247):
    print(p, "normal", cnt[(p, "normal")], "convention", cnt[(p, "convention")], "misprint", cnt[(p, "misprint")])
print("total findings", len(F), "all olds unique and sequentially applicable:", ok)
