import json
import sys

RUN = r"user/Documents/ega_scan_check_20261101/run_0I"
OUT = RUN + "/findings_051_055.json"
NL = "\n"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []

# ---------------- page 51 ----------------
L.append(F(51,
    "(5.4.7), first paragraph: '…l'unique élément de 𝔐 isomorphe à ℒ⊗ℒ′. Avec cette loi de composition…'",
    "ℒ⊗ℒ′ (bare ⊗, no subscript)",
    r"\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}'",
    "extra", None, "high",
    r"$\mathcal{L}\otimes_{\mathcal{O}_X}\mathcal{L}'$",
    r"$\mathcal{L}\otimes\mathcal{L}'$",
    "Checked on a crop: nothing under the ⊗ here (p. 52 prints ℒ⊗_{𝒪_X}ℒ′ with the subscript, as its TeX does)."))

L.append(F(51,
    "(5.4.7), second paragraph: '…(ω_μ|U_λ∩U_μ)⁻¹. On peut faire correspondre à tout 1-cocycle de 𝔘…'",
    "no paragraph break: 'On peut faire correspondre' follows the formula on the same line",
    "blank line before 'On peut faire correspondre' (starts a new paragraph)",
    "other", None, "high",
    r"U_\mu)^{-1}$." + NL + NL + r"On peut faire",
    r"U_\mu)^{-1}$." + NL + r"On peut faire",
    "Paragraphing only: the print continues the paragraph."))

L.append(F(51,
    "(5.4.7), last lines: '…il suffit de le prouver pour les applications H¹(𝔘, 𝒪_X)→𝔐, et cela résulte alors de (3.3.2)'",
    "H¹(𝔘, 𝒪_X)→𝔐 (no star on 𝒪_X; checked on a crop)",
    r"H^1(\mathfrak{U},\mathcal{O}_X)\to\mathfrak{M} (keeps the printed reading)",
    "misprint_in_print", None, "high",
    None, None,
    "The maps φ_𝔘 are defined on H¹(𝔘, 𝒪_X^*) a few lines above; the star is missing in the print. The TeX keeps the printed reading.",
    corrected=r"$H^1(\mathfrak{U},\mathcal{O}_X^*)\to\mathfrak{M}$"))

# ---------------- page 52 ----------------
L.append(F(52,
    "(5.4.8): 'Le foncteur f*(ℒ) dans la catégorie des 𝒪_X-Modules libres définit une application … de l'ensemble 𝔐(X) dans l'ensemble 𝔐(Y)'",
    "𝒪_X-Modules libres",
    r"$\mathcal{O}_X$-Modules libres (keeps the printed reading)",
    "misprint_in_print", None, "low",
    None, None,
    "𝔐(X) is a set of invertible 𝒪_X-Modules (5.4.7), so the functor must be taken on invertible Modules; 'libres' reads as a slip for 'inversibles'. Low confidence: possibly an authorial slip rather than a typesetting error, for the coordinator to decide whether to record it.",
    corrected="inversibles"))

L.append(F(52,
    "(5.4.8): '…ces derniers correspondent au cocycle (ω♯(ε_λμ))…'",
    "ω^♯ (sharp sign: upright stems, slanted bars; checked on a crop)",
    r"\omega^\#",
    "convention", 9, "high",
    r"\omega^\#",
    r"\omega^\sharp",
    "Convention 9."))

L.append(F(52,
    "(5.4.9): the exact sequence 0→ℰ→𝒢→ℱ→0, label over the first arrow",
    "j over the arrow ℰ→𝒢 (dotted letter with a descender; checked on a crop)",
    r"\xrightarrow{i}",
    "formula", None, "high",
    r"\xrightarrow{i}",
    r"\xrightarrow{j}",
    "The second label p matches."))

L.append(F(52,
    "(5.4.10.1): f_*(ℱ)⊗_{𝒪_Y}ℒ ⥲ f_*(ℱ⊗_{𝒪_X}f*(ℒ))",
    "no full stop after the formula (the proof 'En effet, …' starts a new paragraph on p. 53)",
    r"…f^*(\mathcal{L})\bigr).",
    "punctuation", None, "high",
    r"f^*(\mathcal{L})\bigr).",
    r"f^*(\mathcal{L})\bigr)",
    "Checked on a crop."))

# ---------------- page 53 ----------------
L.append(F(53,
    "proof of (5.4.10): display f_*(ℱ)⊗ℒ →(1⊗ρ) f_*(ℱ)⊗f_*(f*(ℒ)) →(α) f_*(ℱ⊗_{𝒪_X}f*(ℒ))",
    "no comma after the display; the sentence continues 'ρ étant l'homomorphisme (4.4.3.2)…'",
    r"…f^*(\mathcal{L})\bigr),",
    "punctuation", None, "high",
    r"\bigr),",
    r"\bigr)",
    "Checked on a crop."))

L.append(F(53,
    "(5.5.1): 'Nous désignerons alors par 𝔪_x l'idéal maximal de 𝒪_x, par k(x) le corps résiduel…'",
    "par 𝔪_x l'idéal maximal (no comma after 𝔪_x)",
    r"par $\mathfrak{m}_x$, l'\emph{idéal maximal}",
    "punctuation", None, "high",
    r"$\mathfrak{m}_x$, l'\emph{idéal maximal}",
    r"$\mathfrak{m}_x$ l'\emph{idéal maximal}",
    "Checked on a crop."))

L.append(F(53,
    "(5.5.1): '…par k(x) le corps résiduel 𝒪_x/𝔪_x…'",
    "bold italic k in k(x)",
    r"$k(x)$",
    "convention", 1, "high",
    r"par $k(x)$ le",
    r"par $\boldsymbol{k}(x)$ le",
    "Convention 1."))

L.append(F(53,
    "(5.5.1): '…nous désignerons par f(x) la classe du germe f_x∈ℱ_x mod. 𝔪_xℱ_x, et nous dirons…'",
    "f_x∈ℱ_x mod. 𝔪_xℱ_x (no parentheses; 'mod.' with a full stop; checked on a crop)",
    r"f_x\in\mathcal{F}_x\pmod{\mathfrak{m}_x\mathcal{F}_x} (typesets '(mod 𝔪_xℱ_x)')",
    "formula", None, "high",
    r"$f_x\in\mathcal{F}_x\pmod{\mathfrak{m}_x\mathcal{F}_x}$",
    r"$f_x\in\mathcal{F}_x$ mod.~$\mathfrak{m}_x\mathcal{F}_x$",
    r"\pmod adds parentheses and drops the print's full stop after 'mod'."))

for lab in "abc":
    L.append(F(53,
        "(5.5.2): label of item " + lab + ") of the list of equivalent properties",
        "upright roman " + lab + ") (checked on a crop)",
        r"\item[$" + lab + r")$] (math italic " + lab + ")",
        "italics", None, "high",
        r"\item[$" + lab + r")$]",
        r"\item[" + lab + r")]",
        "The list labels of (5.5.2) are upright in the print; the references a), b), c) in the proof below are italic, as in the TeX. "
        "Contrast (6.1.1) on p. 55, where the labels are italic (TeX matches); see the final report."))

L.append(F(53,
    "(5.5.2) c): '…l'image canonique de f⊗g dans Γ(V, 𝒪_X) (5.4.3) soit la section unité.'",
    "(5.4.3) upright inside the italic text (checked on a crop)",
    r"(5.4.3) inside \emph{…}, so italic",
    "convention", 6, "high",
    r"(5.4.3) soit la section unité}",
    r"\textup{(5.4.3)} soit la section unité}",
    "Convention 6 (roman reference inside italic text)."))

L.append(F(53,
    "(5.5.3): display X_f∩X_g=X_{f⊗g}",
    "no full stop after the formula",
    r"X_f\cap X_g=X_{f\otimes g}.",
    "punctuation", None, "high",
    r"X_{f\otimes g}.",
    r"X_{f\otimes g}",
    "Checked on a crop."))

L.append(F(53,
    "(5.5.3): 'On se ramène en effet aussitôt au cas où ℒ=ℒ′=𝒪_X…' after the display",
    "new paragraph: 'On se ramène' is indented like a paragraph start",
    r"text follows \] directly (same paragraph, no indent)",
    "other", None, "high",
    r"\]" + NL + r"On se ramène",
    r"\]" + NL + NL + r"On se ramène",
    "Paragraphing only. Independent of the full-stop fix just above."))

# ---------------- page 54 ----------------
L.append(F(54,
    "(5.5.4): '…est un espace vectoriel de dimension (n p) sur k(x), qui s'identifie canoniquement…'",
    "bold italic k in k(x)",
    r"$k(x)$",
    "convention", 1, "high",
    r"sur $k(x)$",
    r"sur $\boldsymbol{k}(x)$",
    "Convention 1."))

L.append(F(54,
    "(5.5.4): 'Soient s_1, …, s_p des sections de F au-dessus d'un ouvert U de X'",
    "F (an upright roman capital F, not the script ℱ; checked on a crop)",
    r"$F$ (keeps the printed letter)",
    "misprint_in_print", None, "high",
    None, None,
    "The sections are sections of the Module ℱ of the paragraph. Upright F in the print against italic $F$ in the TeX is GLOBAL_ISSUES item 17, not a page fix.",
    corrected=r"$\mathcal{F}$"))

for old, new, where in [
    (r"$s=s_1\wedge\cdots\wedge s_p$", r"$s=s_1\wedge\ldots\wedge s_p$",
     "(5.5.4): 'et soit s=s_1∧ … ∧s_p, qui est une section de ∧^pℱ'"),
    (r"$s(x)=s_1(x)\wedge\cdots\wedge s_p(x)$", r"$s(x)=s_1(x)\wedge\ldots\wedge s_p(x)$",
     "(5.5.4): 'on a s(x)=s_1(x)∧ … ∧s_p(x)'"),
    (r"$s=s_1\wedge\cdots\wedge s_n$", r"$s=s_1\wedge\ldots\wedge s_n$",
     "(5.5.4), second paragraph: 's=s_1∧ … ∧s_n est alors une section de 𝒪_X inversible'"),
]:
    L.append(F(54, where,
        "baseline dots between the wedges (s_1∧ . . . ∧s_p; checked on crops)",
        r"\cdots (centred dots)",
        "symbol", None, "medium",
        old, new,
        r"Typographic only: the print sets low dots (as in s_1, …, s_p, where the TeX's \ldots matches). Probably edition-wide wherever the TeX has \cdots between operators."))

L.append(F(54,
    "(5.5.4): 'On en conclut que l'ensemble des x∈X tels que … est ouvert dans X'",
    "l' upright, italics start at 'ensemble' (checked on a crop)",
    r"\emph{l'ensemble des …} (l' italic)",
    "italics", None, "medium",
    r"que \emph{l'ensemble des",
    r"que l'\emph{ensemble des",
    r"Same pattern as l'\emph{idéal maximal} on p. 53, where the TeX already has the elided article upright."))

L.append(F(54,
    "(5.5.5): 'Pour qu'il existe un voisinage u de x∈X tel que u|U soit injectif…'",
    "voisinage u (italic lower-case u; checked on a crop)",
    r"voisinage $u$ de (keeps the printed reading)",
    "misprint_in_print", None, "high",
    None, None,
    "The neighbourhood is U (u|U follows immediately; u is the homomorphism).",
    corrected=r"$U$"))

L.append(F(54,
    "(5.5.5): '…pour tout y∈X (sections canoniques de 𝒪_X^m) ; par hypothèse…'",
    "only 'sections canoniques' italic; 'de 𝒪_X^m' roman (checked on a crop)",
    r"(\emph{sections canoniques de $\mathcal{O}_X^m$})",
    "italics", None, "high",
    r"(\emph{sections canoniques de $\mathcal{O}_X^m$})",
    r"(\emph{sections canoniques} de $\mathcal{O}_X^m$)",
    ""))

L.append(F(54,
    "(5.5.5): 'Il existe alors (5.5.4) un voisinage U⊂V de x tel que les s_i(y) (1⩽i⩽n) forment une base de ℱ_y/𝔪_yℱ_y pour tout y∈V'",
    "pour tout y∈V (checked on a crop)",
    r"pour tout $y\in V$ (keeps the printed reading)",
    "misprint_in_print", None, "medium",
    None, None,
    "U⊂V is the neighbourhood that (5.5.4) provides on which the s_i(y) form a basis, and the isomorphism that follows is over U; 'y∈V' should read 'y∈U'.",
    corrected=r"pour tout $y\in U$"))

L.append(F(54,
    "(6.0): '…Nous supposons tous les anneaux commutatifs (¹).'",
    "footnote mark before the full stop: 'commutatifs (¹).'",
    r"commutatifs.\footnote{…} (full stop before the mark)",
    "punctuation", None, "high",
    r"commutatifs.\footnote{Voir l'exposé cité de" + NL
    + r"N.~Bourbaki pour la généralisation de la plupart des résultats au cas non" + NL
    + r"commutatif.}",
    r"commutatifs\footnote{Voir l'exposé cité de" + NL
    + r"N.~Bourbaki pour la généralisation de la plupart des résultats au cas non" + NL
    + r"commutatif.}.",
    "One edit: moves the full stop after the footnote mark, as on pp. 51-52."))

# ---------------- page 55 ----------------
L.append(F(55,
    "(6.1.1), last paragraph: '…pour tout idéal 𝔍 de A, de type fini, l'application canonique…'",
    "'de' roman, only 'type fini' italic (checked on a crop)",
    r"\emph{de type fini}",
    "italics", None, "high",
    r"\emph{de type fini}",
    r"de \emph{type fini}",
    ""))

L.append(F(55,
    "(6.1.3): first line of the display Im(M⊗(N′+N″))=Im(M⊗N′)+Im(M⊗N″)",
    "no comma at the end of the first line",
    r"…+\operatorname{Im}(M\otimes N''),",
    "punctuation", None, "high",
    r"+\operatorname{Im}(M\otimes N''),",
    r"+\operatorname{Im}(M\otimes N'')",
    "Checked on a crop. The two lines are one two-line display in the print (layout, not reported)."))

for old, new, where, scan in [
    (r"\emph{$A$-module plat}", r"$A$-\emph{module plat}",
     "(6.1.1): '…on dit que M est un A-module plat.'", "A- roman (upright hyphen), only 'module plat' italic"),
    (r"\emph{$A$-plat}", r"$A$-\emph{plat}",
     "6.2, opening paragraph: '…que M est A-plat, B-plat, …'", "A- roman (upright hyphen), only 'plat' italic"),
    (r"\emph{$B$-plat}", r"$B$-\emph{plat}",
     "6.2, opening paragraph: '…que M est A-plat, B-plat, …'", "B- roman (upright hyphen), only 'plat' italic"),
]:
    L.append(F(55, where, scan + " (checked on a crop)",
        old + " (hyphen italic)",
        "italics", None, "low",
        old, new,
        "Only the face of the hyphen differs visibly (the letter is in math mode either way)."))

# ---------------- checks ----------------
ok = True
cache = {}
for i, d in enumerate(L):
    p = d["page"]
    if p not in cache:
        # the page extracts are CRLF; the release files are LF: compare on LF
        with open(f"{RUN}/page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
            cache[p] = fh.read().replace("\r\n", "\n")
    fx = d["fix"]
    if fx is not None:
        n = cache[p].count(fx["old"])
        if n != 1:
            ok = False
            print(f"#{i} page {p}: old occurs {n} times: {fx['old']!r}")
    if d["kind"] == "misprint_in_print" and not d.get("corrected"):
        ok = False
        print(f"#{i}: misprint without corrected")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted({d["page"] for d in L}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(L), "all olds unique" if ok else "PROBLEMS")
sys.exit(0 if ok else 1)
