"""Build findings_212_217.json for the EGA III part 2 scan check (pp. 212-217) and verify that every fix's "old"
occurs exactly once in its page_NNN.tex."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
OUT = RUN / "findings_212_217.json"
NL = "\n"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 212 (ega3-7, end of 7.9)
add(212, "proof of (7.9.14), 'On en conclut (...) que F est Y-plat'",
    "On en conclut (1.4.14.5) que", "On en conclut (I, 4.14.5) que",
    "misprint_in_print", None, "high",
    r"(I, 4.14.5)", r"(1.4.14.5)",
    "Checked on a 2x crop: the print has (1.4.14.5) in old-style figures; the first character is the digit 1 "
    "(x-height, the same glyph as in 14) followed by a full stop, not a bold I and a comma. The printed number is a "
    "misprint: EGA III has no (1.4.14.5) ((1.4.14) has no sub-items) and EGA I has no 4.14. The fact used (M_(g) a flat "
    "A-module, so the sheaf it defines on X_g is Y-flat) is Lemme (1.4.15.5) (ega3-1-fr.tex, label III.1.4.15.5-fr). "
    "The TeX's (I, 4.14.5) is neither the printed nor the correct reading; the diplomatic text takes the printed one.",
    corrected=r"(1.4.15.5)")
add(212, "proof of (7.9.14), 'Soit S l'anneau gradué ...'",
    "Soit S l'anneau gradué ⊕_{n⩾0} Γ(X, L^{⊗n}); on sait ... (inline in the running text, no 'S =')",
    "displayed formula \\[ S=\\bigoplus_{n\\geq0}\\Gamma(X,\\mathscr L^{\\otimes n}) ; \\]",
    "extra", None, "high",
    r"l'anneau gradué" + NL + r"\[" + NL + r"  S=\bigoplus_{n\geq0}\Gamma(X,\mathscr L^{\otimes n}) ;" + NL + r"\]",
    r"l'anneau gradué $\bigoplus_{n\geq0}\Gamma(X,\mathscr L^{\otimes n})$ ;",
    "The print has no 'S=' and sets the sum inline (index under the sum sign, as usual in the print). "
    "GLOBAL_ISSUES item 21 (displays for inline formulas).")
add(212, "proof of (7.9.14), 'Soit M = ...'",
    "Soit M = ⊕_{n⩾n_0} Γ(X, F(n)); remplaçant ... (inline in the running text)",
    "displayed formula \\[ M=\\bigoplus_{n\\geq n_0}\\Gamma(X,\\mathscr F(n)) ; \\]",
    "other", None, "high",
    r"Soit" + NL + r"\[" + NL + r"  M=\bigoplus_{n\geq n_0}\Gamma(X,\mathscr F(n)) ;" + NL + r"\]",
    r"Soit" + NL + r"$M=\bigoplus_{n\geq n_0}\Gamma(X,\mathscr F(n))$ ;",
    "Display where the print sets the formula inline (GLOBAL_ISSUES item 21).")
add(212, "proof of (7.9.14), reference (II, 4.5.2, (b) et 5.4.4)",
    "(b) in italic, parentheses included", "(b) upright",
    "italics", None, "high",
    r", (b) et 5.4.4)", r", \emph{(b)} et 5.4.4)",
    "Checked on a 1.5x crop. Disjoint from the convention-2 edit of '(II,' in the same reference.")
add(212, "proof of (7.9.14), reference (II, 4.5.2, (b) et 5.4.4)",
    "bold II", "plain II",
    "convention", 2, "high",
    r"(II," + NL + r"4.5.2", r"(\textbf{II}," + NL + r"4.5.2",
    "Bold chapter numeral in the reference.")
add(212, "proof of (7.9.14), reference (II, 2.7.5 et 2.7.2)",
    "bold II", "plain II",
    "convention", 2, "high",
    r"(II, 2.7.5", r"(\textbf{II}, 2.7.5",
    "Bold chapter numeral in the reference.")
add(212, "proof of (7.9.14), reference (0_I, 6.3.2)",
    "bold 0", "plain 0",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.3.2)", r"($\mathbf{0}_{\mathrm I}$, 6.3.2)",
    "Bold 0 (GLOBAL_ISSUES item 35 form).")
add(212, "proof of (7.9.14), reference (0_I, 6.1.2)",
    "bold 0", "plain 0",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.1.2)", r"($\mathbf{0}_{\mathrm I}$, 6.1.2)",
    "Bold 0 (GLOBAL_ISSUES item 35 form).")

# ---------------------------------------------------------------- page 213 (index des notations)
HYP = ("The print uses two Tor glyphs on this page: the curly heavy hypertor glyph (script T of another design, bold "
       "italic 'or') in the entries 6.4.1/6.5.1, 6.5.15, 6.6.8/6.7.1/6.7.3 and 6.7.11, and the thin script Tor "
       "(light 'or') in the entries 6.5.1 (Tor(F, G)) and 6.6.2 (U^(1), U^(2); ...), which \\mathscr{T}\\!or matches. "
       "Checked on 1.4-1.6x crops. Fix in the form of the applied p. 146 page fixes; if the GLOBAL_ISSUES item-52 "
       "mapping chooses \\mathfrak{Tor} (as ega3-6 has for the global hypertor, p. 162 fix), use that instead, the "
       "same for all six occurrences on this page.")
add(213, "entry '... : 6.4.1 et 6.5.1', first symbol (Tor_n^{O_S})",
    "curly heavy hypertor glyph", r"\mathscr{T}\!or", "font", None, "high",
    r"$\mathscr{T}\!or_n^{\mathscr O_S}", r"$\boldsymbol{\mathscr{T}\!or}_n^{\mathscr O_S}", HYP)
add(213, "entry '... : 6.4.1 et 6.5.1', second symbol (Tor_n^S(P., Q.))",
    "curly heavy hypertor glyph", r"\mathscr{T}\!or", "font", None, "high",
    r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$",
    r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$", HYP)
add(213, "entry '... : 6.5.15' (Tor_q^S)",
    "curly heavy hypertor glyph", r"\mathscr{T}\!or", "font", None, "high",
    r"$\mathscr{T}\!or_q^S", r"$\boldsymbol{\mathscr{T}\!or}_q^S", HYP)
add(213, "entry '...: 6.6.8, 6.7.1 et 6.7.3' (Tor_n^S(f_1, f_2; ...))",
    "curly heavy hypertor glyph", r"\mathscr{T}\!or", "font", None, "high",
    r"$\mathscr{T}\!or_n^S(f_1,f_2;", r"$\boldsymbol{\mathscr{T}\!or}_n^S(f_1,f_2;", HYP)
add(213, "entry '... : 6.7.11', first symbol (Tor_n^S((f_i)_{i in I}; ...))",
    "curly heavy hypertor glyph", r"\mathscr{T}\!or", "font", None, "high",
    r"$\mathscr{T}\!or_n^S((f_i)", r"$\boldsymbol{\mathscr{T}\!or}_n^S((f_i)", HYP)
add(213, "entry '... : 6.7.11', second symbol (Tor_n^S(f_1, ..., f_m; ...))",
    "curly heavy hypertor glyph", r"\mathscr{T}\!or", "font", None, "high",
    r"$\mathscr{T}\!or_n^S(f_1,\ldots", r"$\boldsymbol{\mathscr{T}\!or}_n^S(f_1,\ldots", HYP)
AB = ("The category Ab is bold italic in the print (here and in the body, e.g. 7.1.2 on p. 175); the TeX has bold "
      "upright \\mathbf{Ab} (41 times in ega3-7-fr.tex).")
add(213, "entry 'Ab, Ab_A : 7.1.1', first Ab",
    "bold italic Ab", r"\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}$, ", r"$\boldsymbol{Ab}$, ", AB)
add(213, "entry 'Ab, Ab_A : 7.1.1', Ab_A",
    "bold italic Ab", r"\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ : 7.1.1", r"$\boldsymbol{Ab}_A$ : 7.1.1", AB)
add(213, "entry 'T_(B), ... (T foncteur de Ab_A dans Ab) : 7.1.3', Ab_A",
    "bold italic Ab", r"\mathbf{Ab}", "font", None, "high",
    r"de $\mathbf{Ab}_A$ dans", r"de $\boldsymbol{Ab}_A$ dans", AB)
add(213, "entry 'T_(B), ... (T foncteur de Ab_A dans Ab) : 7.1.3', Ab",
    "bold italic Ab", r"\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}$)", r"$\boldsymbol{Ab}$)", AB)

# ---------------------------------------------------------------- page 214 (index terminologique): no findings

# ---------------------------------------------------------------- page 215 (table des matières) and blank p. 216
add(215, "contents table, column head above the page numbers",
    "Pages (small capitals) with a short rule under it, right-hand column", "absent",
    "missing", None, "high",
    r"\begin{flushleft}" + NL + r"\textsc{Chapitre III.}",
    r"\begin{flushleft}" + NL + r"\hfill\textsc{Pages}" + NL + NL + r"\textsc{Chapitre III.}",
    "Same form as the EGA III part 1 contents fix (findings_164_167, p. 165); GLOBAL_ISSUES item 45. The rule under "
    "'Pages' is layout.")
add(215, "contents entry 'Chapitre III. -- Étude cohomologique des faisceaux cohérents (suite) ... 5'",
    "(suite) in italic, not bold", "(suite) inside \\textbf",
    "italics", None, "high",
    r"faisceaux cohérents" + NL + r"(suite)}", r"faisceaux cohérents}" + NL + r"\textit{(suite)}",
    "Checked on a crop. Same as the EGA III part 1 contents entry 'Préliminaires (suite)'.")
add(215, "contents entry 7.4",
    "Critères d'exactitude pour les foncteurs H_•(P_•⊗_A M)", r"$\mathrm H_i(P\otimes_A M)$",
    "formula", None, "high",
    r"$\mathrm H_i(P\otimes_A M)$", r"$\mathrm H_\bullet(P_\bullet\otimes_A M)$",
    "Checked on a 1.3x crop: bullet subscripts on H and on P, as in the section title (ega3-7 \\subsection 7.4).")
add(215, "end of page_215.tex: the blank printed page 216",
    "printed p. 216 (pdf p. 83 of PMIHES_1963__17__5_0.pdf) is blank: no text, no page number (rendered and "
    "measured: no ink apart from specks)",
    "blank page (\\clearpage \\thispagestyle{empty} \\null \\clearpage, with the comment '% La page imprimée 216 est "
    "blanche.') but no \\oldpage[III]{216} marker",
    "marker", None, "high",
    r"\clearpage" + NL + r"\thispagestyle{empty}",
    r"\clearpage" + NL + r"\oldpage[III]{216}" + NL + r"\thispagestyle{empty}",
    "Concerns printed p. 216, which has no page file; the edit lies in the segment of p. 215. No printed text of "
    "p. 216 is missing. Marker form as for the EGA II blank pages 212 and 216 (GLOBAL_ISSUES item 32: markers for every "
    "printed page, blank ones included).")

# ---------------------------------------------------------------- page 217 (errata et addenda, liste 2)
HEAD = ("The print sets the whole heading bold (bold 0, light subscript I, bold number and parentheses); the TeX puts "
        "it in math mode inside \\textbf, which typesets it in normal weight (math ignores \\textbf). Checked on a "
        "1.5x crop.")
for num in ["3.2.1", "3.2.6", "3.4.5", "4.2.1", "5.1.3", "5.3.9", "7.6.9"]:
    add(217, f"errata heading (0_I, {num})",
        f"bold heading (0_I, {num})", f"\\textbf{{$(0_{{\\mathrm I}},\\,{num})$}} (prints non-bold)",
        "font", None, "high",
        r"\textbf{$(0_{\mathrm I},\," + num + r")$}",
        r"\textbf{($\mathbf{0}_{\mathrm I}$, " + num + r")}",
        HEAD)
add(217, "(0_I, 3.2.6), the symbol to be replaced",
    "Fraktur H_λ (ℌ_λ) par script H_λ", r"$\mathfrak S_\lambda$ par $\mathscr H_\lambda$",
    "symbol", None, "high",
    r"$\mathfrak S_\lambda$", r"$\mathfrak H_\lambda$",
    "Checked on a 3x crop: Fraktur H (right-hand part descending below the baseline), not Fraktur S. EGA 0_I (3.2.6) "
    "on pp. 27-28 has the Fraktur H three times ((\\mathfrak{H}_\\lambda) in ega0-1-fr.tex), which this erratum "
    "replaces by the script H.")
add(217, "(0_I, 7.6.9) Ligne 3 du bas de la p. 73",
    "remplacer J_λ par 𝔍_λ (roman J, then Fraktur J)", r"remplacer $I_\lambda$ par $J_\lambda$",
    "symbol", None, "high",
    r"$I_\lambda$ par $J_\lambda$", r"$J_\lambda$ par $\mathfrak J_\lambda$",
    "Checked on a 1.5x crop. EGA 0_I (7.6.9), line 3 from the bottom of p. 73, reads 'où a ⊃ J_λ' with a roman J "
    "where the rest of (7.6.9) has the Fraktur J; the erratum replaces it by the Fraktur J.")
add(217, "(I, 2.3.1)",
    "Ligne 3 de la p. 101", "Ligne 3 du bas de la p. 101",
    "extra", None, "high",
    r"Ligne 3 du bas de la p. 101", r"Ligne 3 de la p. 101",
    "Checked on a crop. The print has no 'du bas' (EGA I (2.3.1) and its reference (0, 4.1.6) stand at the top of "
    "p. 101).")
add(217, "(I, 4.2.2), the new label of the left vertical arrow",
    "remplacer α_ψ(y) par ρ_ψ(y)", r"remplacer $\alpha_{\psi(y)}$ par $\varphi_{\psi(y)}$",
    "symbol", None, "high",
    r"$\varphi_{\psi(y)}$", r"$\rho_{\psi(y)}$",
    "Checked on a 3x crop: Greek rho, no stroke through it.")
add(217, "(I, 4.4.3)",
    "remplacer isomorphee par isomorphes (no accent: the erratum quotes the misprinted word)",
    "remplacer isomorphée par isomorphes",
    "word", None, "high",
    r"isomorphée", r"isomorphee",
    "Checked on a 3x crop. EGA I p. 126 has 'isomorphee' (ega1-4-fr.tex, (4.4.3)), which the print quotes exactly.")
add(217, "(I, 2.3.1), first reference",
    "(0, 4.1.6) with bold 0", "(0, 4.1.6)",
    "convention", 2, "high",
    r"(0, 4.1.6)", r"(\textbf{0}, 4.1.6)", "Bold 0.")
add(217, "(I, 2.3.1), second reference",
    "(0, 4.1.7) with bold 0", "(0, 4.1.7)",
    "convention", 2, "high",
    r"(0, 4.1.7)", r"(\textbf{0}, 4.1.7)", "Bold 0.")
add(217, "(I, 9.6.5), first reference",
    "(0, 4.1.4) with bold 0", r"$(0,\,4.1.4)$",
    "convention", 2, "high",
    r"$(0,\,4.1.4)$", r"(\textbf{0}, 4.1.4)", "Bold 0; the reference set as text like the other references of the page.")
add(217, "(I, 9.6.5), second reference",
    "(0, 4.1.3) with bold 0", r"$(0,\,4.1.3)$",
    "convention", 2, "high",
    r"$(0,\,4.1.3)$", r"(\textbf{0}, 4.1.3)", "Bold 0; the reference set as text like the other references of the page.")

# ---------------------------------------------------------------- checks
bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/MISSING", d["page"], n, repr(fx["old"]))
# fixes on the same page must not overlap each other
for p in sorted({d["page"] for d in F}):
    t = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP on page", p, a, b)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    c[1 if d["kind"] == "convention" else 2 if d["kind"] == "misprint_in_print" else 0] += 1
print("written", OUT, len(F), "findings; problems:", bad)
for p in [212, 213, 214, 215, 217]:
    print(p, "normal/convention/misprint =", "/".join(map(str, counts.get(p, [0, 0, 0]))))
