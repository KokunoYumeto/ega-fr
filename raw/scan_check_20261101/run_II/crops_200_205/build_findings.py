"""Build findings_200_205.json for EGA II pp. 200-205, check every fix's 'old' against its page file, and simulate
the sequential application (same page-segment logic as apply_fixes.py) on in-memory copies of the release files.
Writes nothing but the findings JSON."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
E = RUN.parent
OUT = RUN / "findings_200_205.json"
NL = "\u00b6"  # stands for a line break in the strings below


def s(x):
    return x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else {"old": s(old), "new": s(new)})
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    F.append(d)


SP = "Script 𝒫roj (script P, italic roj) for the sheaf, as fixed on pp. 195-199 (global item 31): "
SPN = ("the scheme Proj(𝒮) stays roman on these pages (X = Proj(𝒮) in (8.14.8) and (8.14.14), "
       "X^(d) = Proj(𝒮^(d)) in (8.14.13)), as in the TeX.")
GN = ("Checked on a crop. Γ'_*(ℱ') = ⊕ q'_*(ℱ'_n) (8.14.6.2) is the graded 𝒮-Module on Y, printed with the bold Γ "
      "like Γ_* in (3.3.1.1); \\bbGamma as in the pp. 56-58 fixes.")

# ---------------- page 200 (entries located in the page-200 segment) ----------------
add(200, "p. 200, (8.14.7), affine case: 'alors Γ'_*(ℱ') = M̃'", "bold Γ in Γ'_*(ℱ')", "\\Gamma'_*(\\mathcal{F}')",
    "font", None, "high",
    r"$\Gamma'_*(\mathcal{F}')=\widetilde{M}$", r"$\bbGamma'_*(\mathcal{F}')=\widetilde{M}$", GN)
add(200, "p. 200, (8.14.7), affine case: 'où M = ⊕ Γ(X', ℱ'_n) est un S-module gradué'",
    "the index under ⊕ is printed 'Z∈n' (bold Z, ∈, italic n)", r"\bigoplus_{n\in\mathbf{Z}}",
    "misprint_in_print", None, "high",
    r"\bigoplus_{n\in\mathbf{Z}}\Gamma(X',\mathcal{F}'_n)", r"\bigoplus_{\mathbf{Z}\in n}\Gamma(X',\mathcal{F}'_n)",
    "Checked on a 2.5x crop: inverted index. The TeX silently corrects it; the fix restores the printed reading.",
    corrected=r"\bigoplus_{n\in\mathbf{Z}}\Gamma(X',\mathcal{F}'_n)")
add(200, "p. 200, (8.14.7): 'α_d(f) restreinte à D_+(f), est la section de 𝒪_X(d)'",
    "comma after D_+(f)", "no comma", "punctuation", None, "high",
    "restreinte à $D_+(f)$ est la", "restreinte à $D_+(f)$, est la", "Checked on a crop.")
add(200, "Proposition (8.14.8): 'l'homomorphisme β' défini dans (8.14.7) est bijectif'",
    "the reference (8.14.7) upright inside the italic statement", "italic (inside the proposition environment)",
    "convention", 6, "high",
    r"(\hyperref[II.8.14.7-fr]{8.14.7}) est bijectif", r"\textup{(\hyperref[II.8.14.7-fr]{8.14.7})} est bijectif",
    "Checked on a crop.")
add(200, "proof of (8.14.8): '(I, 9.3.1)'", "bold I", "plain I in the link text", "convention", 2, "high",
    "{I, 9.3.1}", r"{\textbf{I}, 9.3.1}", "")
add(200, "Corollaire (8.14.9): 'Sous les hypothèses de (8.14.8), tout'",
    "the reference (8.14.8) upright inside the italic statement", "italic (inside the corollary environment)",
    "convention", 6, "high",
    r"Sous les hypothèses de (\hyperref[II.8.14.8-fr]{8.14.8}), tout",
    r"Sous les hypothèses de \textup{(\hyperref[II.8.14.8-fr]{8.14.8})}, tout", "Checked on a crop.")
add(200, "Proposition (8.14.10): 'Sous les hypothèses de (8.14.7), soient'",
    "the reference (8.14.7) upright inside the italic statement", "italic (inside the proposition environment)",
    "convention", 6, "high",
    r"de (\hyperref[II.8.14.7-fr]{8.14.7}), soient", r"de \textup{(\hyperref[II.8.14.7-fr]{8.14.7})}, soient",
    "Checked on a crop.")
add(200, "Corollaire (8.14.9): 'de la forme 𝒫roj'(ℳ)'", "script 𝒫, italic 'roj'", r"\operatorname{Proj}'",
    "font", None, "high",
    r"$\operatorname{Proj}'(\mathcal{M})$, où", r"$\mathcal{P}\mathit{roj}'(\mathcal{M})$, où", SP + SPN)
add(200, "display (8.14.10.1), middle term 𝒫roj'(Γ'_*(𝒫roj'(ℳ)))", "bold Γ", r"\Gamma'_*", "font", None, "high",
    r"(\Gamma'_*(\operatorname{Proj}'(\mathcal{M})))", r"(\bbGamma'_*(\operatorname{Proj}'(\mathcal{M})))",
    GN + " Keep the order: this entry must run before the entry for the last two 𝒫roj' of (8.14.10.1), which "
         "edits the \\operatorname{Proj} inside this string.")
add(200, "display (8.14.10.1): 𝒫roj'(ℳ) on the left, the arrow label 𝒫roj'(α') and the outer 𝒫roj' of the middle term",
    "script 𝒫, italic 'roj' (three times)", r"\operatorname{Proj}'", "font", None, "high",
    "  \\operatorname{Proj}'(\\mathcal{M})" + NL + "  \\xrightarrow{\\operatorname{Proj}'(\\alpha')}" + NL
    + "  \\operatorname{Proj}'(",
    "  \\mathcal{P}\\mathit{roj}'(\\mathcal{M})" + NL + "  \\xrightarrow{\\mathcal{P}\\mathit{roj}'(\\alpha')}" + NL
    + "  \\mathcal{P}\\mathit{roj}'(",
    SP + "checked on a crop.")
add(200, "display (8.14.10.1): the inner 𝒫roj'(ℳ) of the middle term and the target 𝒫roj'(ℳ)",
    "script 𝒫, italic 'roj' (twice)", r"\operatorname{Proj}'", "font", None, "high",
    r"\operatorname{Proj}'(\mathcal{M})))" + NL + r"  \xrightarrow{\beta'}\operatorname{Proj}'(\mathcal{M})",
    r"\mathcal{P}\mathit{roj}'(\mathcal{M})))" + NL + r"  \xrightarrow{\beta'}\mathcal{P}\mathit{roj}'(\mathcal{M})",
    SP + "keep the order: after the bold-Γ entry for (8.14.10.1).")
add(200, "display (8.14.10.2): middle term Γ'_*(𝒫roj'(Γ'_*(ℱ')))", "script 𝒫, italic 'roj'", r"\operatorname{Proj}'",
    "font", None, "high",
    r"\Gamma'_*(\operatorname{Proj}'(\Gamma'_*(\mathcal{F}')))",
    r"\Gamma'_*(\mathcal{P}\mathit{roj}'(\Gamma'_*(\mathcal{F}')))",
    SP + "keep the order: this entry must run before the two bold-Γ entries for (8.14.10.2), which edit the two "
         "\\Gamma in this string.")
add(200, "display (8.14.10.2): Γ'_*(ℱ') on the left and the first Γ'_* of the middle term",
    "bold Γ (twice)", r"\Gamma'_*", "font", None, "high",
    "  \\Gamma'_*(\\mathcal{F}')" + NL + "  \\xrightarrow{\\alpha'}" + NL + "  \\Gamma'_*(",
    "  \\bbGamma'_*(\\mathcal{F}')" + NL + "  \\xrightarrow{\\alpha'}" + NL + "  \\bbGamma'_*(",
    "Checked on a crop. After the 𝒫roj entry for (8.14.10.2).")
add(200, "display (8.14.10.2): inner Γ'_*(ℱ'), the arrow label Γ'_*(β') and the target Γ'_*(ℱ')",
    "bold Γ (three times)", r"\Gamma'_*", "font", None, "high",
    r"roj}'(\Gamma'_*(\mathcal{F}')))" + NL + r"  \xrightarrow{\Gamma'_*(\beta')}\Gamma'_*(\mathcal{F}')",
    r"roj}'(\bbGamma'_*(\mathcal{F}')))" + NL + r"  \xrightarrow{\bbGamma'_*(\beta')}\bbGamma'_*(\mathcal{F}')",
    "Checked on a crop. 'roj}'(' matches both \\operatorname{Proj}'( and \\mathit{roj}'(, so this entry works with or "
    "without the 𝒫roj entries; after the 𝒫roj entry for (8.14.10.2).")
add(200, "Remarque (8.14.11): 'Au chapitre III (III, 2.3.1)'", "bold III in the reference", "plain III in the link text",
    "convention", 2, "high", "{III, 2.3.1}", r"{\textbf{III}, 2.3.1}", "The words 'Au chapitre III' are roman, as in the TeX.")

# ---------------- page 201 ----------------
add(201, "Remarque (8.14.12), end: 'et où la condition (TN) pour ℳ (3.4.2)'",
    "'TN' bold, the parentheses roman (light)", r"\textbf{(TN)} (bold parentheses)", "font", None, "high",
    r"la condition \textbf{(TN)} pour", r"la condition (\textbf{TN}) pour",
    "Checked on a 5x crop against '« mod. (TN) »' two lines above, whose parentheses are bold (TeX right there), "
    "and '(TN)-bijectif' / '(TF)' at the top of the page (bold parentheses, TeX right).")

# ---------------- page 202 ----------------
add(202, "Remarque (8.14.13), after 'lorsque A' est une A-algèbre.': 'En particulier, on a ainsi un h-isomorphisme'",
    "'En particulier' starts flush left, not indented: the same paragraph continues", "blank line: new paragraph",
    "other", None, "high",
    "$A$-algèbre." + NL + NL + "En particulier", "$A$-algèbre." + NL + "En particulier",
    "Checked on a crop of the left margin: every other new paragraph on the page ('Supposons d'abord', 'On déduit') "
    "is indented; 'En particulier' is not.")
add(202, "display (8.14.13.1): (𝒫roj(ℳ))^(d,k) ⟵~ 𝒫roj(ℳ^(d,k))", "script 𝒫, italic 'roj' (twice)",
    r"\operatorname{Proj}", "font", None, "high",
    "  (\\operatorname{Proj}(\\mathcal{M}))^{(d,k)}" + NL + "  \\xleftarrow{\\sim}\\operatorname{Proj}(\\mathcal{M}^{(d,k)}).",
    "  (\\mathcal{P}\\mathit{roj}(\\mathcal{M}))^{(d,k)}" + NL + "  \\xleftarrow{\\sim}\\mathcal{P}\\mathit{roj}(\\mathcal{M}^{(d,k)}).",
    SP + "the left-pointing iso arrow is right.")
add(202, "display (8.14.13.3): 𝒫roj_0(𝒮^(d,k)(n)) ⥲ 𝒪_X(nd+k)", "script 𝒫, italic 'roj'", r"\operatorname{Proj}_0",
    "font", None, "high",
    r"\operatorname{Proj}_0(\mathcal{S}^{(d,k)}(n))", r"\mathcal{P}\mathit{roj}_0(\mathcal{S}^{(d,k)}(n))", SP.rstrip(": ") + ".")
add(202, "display (8.14.13.4), left term Γ_*^(d)(𝒫roj(ℳ^(d,k)))", "bold Γ", r"\Gamma_*^{(d)}", "font", None, "high",
    "8.14.13.4-fr}" + NL + "  \\Gamma_*^{(d)}", "8.14.13.4-fr}" + NL + "  \\bbGamma_*^{(d)}",
    "Checked on a crop. Γ_*^(d) is the Γ_* of X^(d) → Y (graded 𝒪_Y-Module), bold like Γ_*.")
add(202, "display (8.14.13.4), right term Γ_*((𝒫roj(ℳ))^(d,k))", "bold Γ", r"\Gamma_*", "font", None, "high",
    "\\xrightarrow{\\sim}" + NL + "  \\Gamma_*((", "\\xrightarrow{\\sim}" + NL + "  \\bbGamma_*((", "Checked on a crop.")
add(202, "display (8.14.13.4), left term", "script 𝒫, italic 'roj'", r"\operatorname{Proj}", "font", None, "high",
    "(\\operatorname{Proj}(\\mathcal{M}^{(d,k)}))" + NL + "  \\xrightarrow{\\sim}",
    "(\\mathcal{P}\\mathit{roj}(\\mathcal{M}^{(d,k)}))" + NL + "  \\xrightarrow{\\sim}", SP.rstrip(": ") + ".")
add(202, "display (8.14.13.4), right term", "script 𝒫, italic 'roj'", r"\operatorname{Proj}", "font", None, "high",
    "((\\operatorname{Proj}(\\mathcal{M}))^{(d,k)})" + NL + "\\tag{8.14.13.4}",
    "((\\mathcal{P}\\mathit{roj}(\\mathcal{M}))^{(d,k)})" + NL + "\\tag{8.14.13.4}", SP.rstrip(": ") + ".")
add(202, "after (8.14.13.4): 'où Γ_*^(d) correspond au morphisme structural q^(d)'", "bold Γ", r"\Gamma_*^{(d)}",
    "font", None, "high",
    r"où $\Gamma_*^{(d)}$ correspond", r"où $\bbGamma_*^{(d)}$ correspond", "Checked on a crop.")
add(202, "diagram (8.14.13.5), bottom left Γ_*^(d)(𝒫roj(ℳ^(d,k)))", "bold Γ", r"\Gamma_*^{(d)}", "font", None, "high",
    "& \\\\" + NL + "    \\Gamma_*^{(d)}", "& \\\\" + NL + "    \\bbGamma_*^{(d)}", "Checked on a crop.")
add(202, "diagram (8.14.13.5), bottom right Γ_*((𝒫roj(ℳ))^(d,k))", "bold Γ", r"\Gamma_*", "font", None, "high",
    r"&& \Gamma_*((", r"&& \bbGamma_*((", "Checked on a crop.")
add(202, "diagram (8.14.13.5), bottom left", "script 𝒫, italic 'roj'", r"\operatorname{Proj}", "font", None, "high",
    "(\\operatorname{Proj}(\\mathcal{M}^{(d,k)}))" + NL + "      \\ar[rr]",
    "(\\mathcal{P}\\mathit{roj}(\\mathcal{M}^{(d,k)}))" + NL + "      \\ar[rr]", SP.rstrip(": ") + ".")
add(202, "diagram (8.14.13.5), bottom right", "script 𝒫, italic 'roj'", r"\operatorname{Proj}", "font", None, "high",
    "((\\operatorname{Proj}(\\mathcal{M}))^{(d,k)})" + NL + "  }",
    "((\\mathcal{P}\\mathit{roj}(\\mathcal{M}))^{(d,k)})" + NL + "  }", SP.rstrip(": ") + ".")

add(202, "Proposition (8.14.14): 'vérifiant la condition (TF); soit X = Proj(𝒮)'",
    "(TF) bold upright inside the italic statement", r"\textbf{(TF)} inside the proposition environment (bold italic)",
    "convention", 6, "high",
    r"\textbf{(TF)}~; soit", r"\textup{\textbf{(TF)}}~; soit",
    "Checked on a 5x crop. Same fix as for (TN) in italic statements on pp. 64-69.")
add(202, "Proposition (8.14.14): 'graduée périodique (8.14.12), et il existe une'",
    "the reference (8.14.12) upright inside the italic statement", "italic (inside the proposition environment)",
    "convention", 6, "high",
    r"(\hyperref[II.8.14.12-fr]{8.14.12}), et il existe une",
    r"\textup{(\hyperref[II.8.14.12-fr]{8.14.12})}, et il existe une", "Checked on a crop.")

# ---------------- page 203 ----------------
add(203, "Proposition (8.14.14), end: 'telle que les (𝒫roj(ℳ))^(d,k) (0 ≤ k ≤ d−1)'", "script 𝒫, italic 'roj'",
    r"\operatorname{Proj}", "font", None, "high",
    r"$(\operatorname{Proj}(\mathcal{M}))^{(d,k)}$", r"$(\mathcal{P}\mathit{roj}(\mathcal{M}))^{(d,k)}$",
    SP.rstrip(": ") + ".")
add(203, "proof of (8.14.14), last line: 'conséquence de (2.1.6 (iii)) et de (3.4.3)'",
    "no comma: '(2.1.6 (iii))'", "'2.1.6, (iii)' with a comma", "punctuation", None, "high",
    "{2.1.6, (iii)}", "{2.1.6 (iii)}",
    "Checked on a 2.5x crop. Contrast '(3.2.9, (ii))' on p. 202, printed with the comma (TeX right there).")

# ---------------- page 205 (ega2-bibliography-fr.tex) ----------------
BIB = ("The p. 205 entries follow the print's bibliography style, which the EGA I bibliography TeX (bib-fr.tex) "
       "already uses: author surnames in caps and small caps (\\textsc), article/book titles roman, journal or series "
       "names italic, page ranges with a hyphen.")
add(205, "[23] 'C. Chevalley'", "surname in caps and small caps", "plain 'Chevalley'", "font", None, "high",
    "C.~Chevalley,", r"C.~\textsc{Chevalley},", BIB)
add(205, "[23] title 'Introduction to the theory of algebraic functions of one variable,'",
    "title roman, followed by a comma", "title in \\emph, followed by a period", "italics", None, "high",
    r"\emph{Introduction to the theory of algebraic functions of one variable}.",
    "Introduction to the theory of algebraic functions of one variable,",
    "Two differences in one edit: the face (roman) and the comma after the title (TeX: period).")
add(205, "[23] series 'Math. Surveys, nº 6'", "'Math. Surveys' italic", "roman", "italics", None, "high",
    "Math. Surveys, n", r"\emph{Math. Surveys}, n", "")
add(205, "[24] 'P. Jaffard'", "surname in caps and small caps", "plain 'Jaffard'", "font", None, "high",
    "P.~Jaffard,", r"P.~\textsc{Jaffard},", "The title 'Les systèmes d'idéaux' is italic in the print, as in the TeX.")
add(205, "[25] 'M. Nagata'", "surname in caps and small caps", "plain 'Nagata'", "font", None, "high",
    "{II-25}" + NL + "M.~Nagata,", "{II-25}" + NL + "M.~\\textsc{Nagata},", "")
add(205, "[25] title 'On the derived normal rings of Noetherian integral domains'", "title roman", "title in \\emph",
    "italics", None, "high",
    r"\emph{On the derived normal rings of Noetherian integral domains}",
    "On the derived normal rings of Noetherian integral domains", "")
add(205, "[25] journal 'Mem. Coll. Sci. Kyoto'", "journal italic", "roman", "italics", None, "high",
    "Mem. Coll. Sci. Kyoto,", r"\emph{Mem. Coll. Sci. Kyoto},", "")
add(205, "[25] 'p. 293-303'", "hyphen between the page numbers", "en dash (--)", "punctuation", None, "high",
    "p.~293--303", "p.~293-303", "Checked on a 4x crop: the dash is shorter than a figure, a hyphen.")
add(205, "[26] 'M. Nagata'", "surname in caps and small caps", "plain 'Nagata'", "font", None, "high",
    "{II-26}" + NL + "M.~Nagata,", "{II-26}" + NL + "M.~\\textsc{Nagata},", "")
add(205, "[26] title 'Existence theorems for non projective complete algebraic varieties'", "title roman",
    "title in \\emph", "italics", None, "high",
    r"\emph{Existence theorems for non projective complete algebraic varieties}",
    "Existence theorems for non projective complete algebraic varieties", "")
add(205, "[26] journal 'Ill. J. Math.'", "journal italic", "roman", "italics", None, "high",
    "Ill. J. Math.,", r"\emph{Ill. J. Math.},", "")
add(205, "[26] 'p. 490-498'", "hyphen between the page numbers", "en dash (--)", "punctuation", None, "high",
    "p.~490--498", "p.~490-498", "Checked on a 4x crop.")

# ---------------- checks ----------------
bad = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(x["fix"]["old"])
    if n != 1:
        bad += 1
        print("PAGE-FILE CHECK FAILED", i, x["page"], n, repr(x["fix"]["old"][:70]))

inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["II"]["files"]
texts = {f: pathlib.Path(f).read_text(encoding="utf-8") for f in inv}
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def locate(page):
    for f in inv:
        t = texts[f]
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for j, (n, st) in enumerate(cuts):
            if n == page:
                return f, st, cuts[j + 1][1] if j + 1 < len(cuts) else len(t)
    return None, None, None


for i, x in enumerate(F):
    if not x["fix"]:
        continue
    f, st, en = locate(x["page"])
    if f is None:
        bad += 1; print("SIM: page not found", i, x["page"]); continue
    seg = texts[f][st:en]
    if seg.count(x["fix"]["old"]) != 1:
        bad += 1; print("SIM: old occurs", seg.count(x["fix"]["old"]), "times", i, x["page"], repr(x["fix"]["old"][:60])); continue
    texts[f] = texts[f][:st] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + texts[f][en:]

f, st, en = locate(199)
print("--- simulated end of p. 199 segment:", repr(texts[f][en - 160:en]))
f, st, en = locate(200)
print("--- simulated start of p. 200 segment:", repr(texts[f][st:st + 420]))
print("entries", len(F), "problems", bad)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
