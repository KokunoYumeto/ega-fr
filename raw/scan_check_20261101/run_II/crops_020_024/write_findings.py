import json
import pathlib
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
OUT = RUN / "findings_020_024.json"


def F(page, where, scan, tex, kind, conf, old, new, note, convention=None, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- page 20 ----------------
    F(20, "(2.1.1), paragraph 'Avec les notations précédentes': definition of a free graded module",
      "en tant que module gradué (only 'gradué' italic)",
      r"en tant que \emph{module gradué}",
      "italics", "high",
      r"en tant que \emph{module gradué}",
      r"en tant que module \emph{gradué}",
      "'module' is upright in the print."),
    F(20, "(2.1.2), first paragraph: grading of M⊗_Z N ('en posant (M⊗_Z N)_q = ⊕ M_m⊗_Z N_n')",
      "formula set inline in the running text: '... en posant (M⊗_Z N)_q = ⊕_{m+n=q} M_m⊗_Z N_n (comme M et N ...'",
      r"displayed formula \[ (M\otimes_{\mathbf{Z}}N)_q =\bigoplus_{m+n=q}... \]",
      "other", "high",
      "en posant\n\\[\n  (M\\otimes_{\\mathbf{Z}}N)_q\n  =\\bigoplus_{m+n=q}M_m\\otimes_{\\mathbf{Z}}N_n\n\\]\n(comme",
      "en posant\n$(M\\otimes_{\\mathbf{Z}}N)_q=\\bigoplus_{m+n=q}M_m\\otimes_{\\mathbf{Z}}N_n$\n(comme",
      "The print sets this formula inline (index m+n=q under the ⊕, the Σ-index position to be ignored); the TeX displays it."),
    # ---------------- page 21 ----------------
    F(21, "(2.1.2), paragraph 'Soient S, S′ deux anneaux gradués'",
      "tel que φ(S_n) ⊂ S′_n pour tout n∈Z (no comma)",
      r"$\varphi(S_n)\subset S'_n$, pour tout",
      "punctuation", "high",
      r"$\varphi(S_n)\subset S'_n$, pour tout",
      r"$\varphi(S_n)\subset S'_n$ pour tout",
      "No comma after S′_n in the print."),
    F(21, "(2.1.2), last paragraph 'Si alors M est un S-module gradué'",
      "le produit tensoriel M⊗_S S′ de S-modules gradués ('gradués' italic) est muni",
      r"de $S$-modules gradués est muni",
      "italics", "high",
      r"de $S$-modules gradués est muni",
      r"de $S$-modules \emph{gradués} est muni",
      "'gradués' (first word of a printed line) is italic."),
    # ---------------- page 22 ----------------
    F(22, "proof of Lemme (2.1.6), first sentence: 'des éléments f_1^{α_1} ... f_r^{α_r} x_j tels que'",
      "f_1^{α_1} . . . f_r^{α_r} x_j (dots on the baseline)",
      r"f_1^{\alpha_1}\cdots f_r^{\alpha_r}x_j (centred dots)",
      "symbol", "high",
      r"$f_1^{\alpha_1}\cdots f_r^{\alpha_r}x_j$ tels",
      r"$f_1^{\alpha_1}\ldots f_r^{\alpha_r}x_j$ tels",
      r"Baseline dots in the print (same correction as earlier \cdots -> \ldots fixes)."),
    F(22, "proof of Lemme (2.1.6): 'les éléments de M de la forme f_1^{α_1} ... f_r^{α_r} x_j avec 0⩽α_i<h/h_i'",
      "f_1^{α_1} . . . f_r^{α_r} x_j (dots on the baseline)",
      r"f_1^{\alpha_1}\cdots f_r^{\alpha_r}x_j (centred dots)",
      "symbol", "high",
      r"$f_1^{\alpha_1}\cdots f_r^{\alpha_r}x_j$ avec",
      r"$f_1^{\alpha_1}\ldots f_r^{\alpha_r}x_j$ avec",
      "Baseline dots in the print."),
    F(22, "proof of Lemme (2.1.6): 'd'éléments de la forme g^d f_1^{α_1} ... f_r^{α_r} x_j avec 0⩽α_i<d'",
      "g^d f_1^{α_1} . . . f_r^{α_r} x_j (dots on the baseline)",
      r"g^df_1^{\alpha_1}\cdots f_r^{\alpha_r}x_j (centred dots)",
      "symbol", "high",
      r"$g^df_1^{\alpha_1}\cdots f_r^{\alpha_r}x_j$",
      r"$g^df_1^{\alpha_1}\ldots f_r^{\alpha_r}x_j$",
      "Baseline dots in the print."),
    F(22, "(2.1.8), first sentence: 'Soit 𝔭 un idéal premier gradué de l'anneau gradué S'",
      "un idéal premier gradué ('gradué' italic) de l'anneau gradué S",
      r"un idéal premier gradué de l'anneau gradué $S$",
      "italics", "high",
      r"un idéal premier gradué de l'anneau gradué $S$",
      r"un idéal premier \emph{gradué} de l'anneau gradué $S$",
      "The first 'gradué' is italic, the second ('l'anneau gradué') upright."),
    F(22, "(2.1.8): 'Supposons que 𝔭 ne contienne pas S_+'",
      "Supposons que 𝔭 ne contienne pas (italic) S_+",
      "Supposons que $\\mathfrak{p}$ ne\ncontienne pas $S_+$",
      "italics", "high",
      "ne\ncontienne pas $S_+$",
      "\\emph{ne\ncontienne pas} $S_+$",
      "'ne contienne pas' is italic in the print."),
    F(22, "Proposition (2.1.9), first sentence",
      "Soit n_0 un entier >0; pour tout n⩾n_0, soit 𝔭_n un sous-groupe de S_n (comma after n_0)",
      r"pour tout $n\geq n_0$ soit $\mathfrak{p}_n$",
      "punctuation", "high",
      r"pour tout $n\geq n_0$ soit",
      r"pour tout $n\geq n_0$, soit",
      "The print has a comma after n⩾n_0."),
    F(22, "proof of Proposition (2.1.9), last sentence on the page: 'p_m est aussi défini comme l'ensemble des x∈S_m tels que f^r x∈𝔭_{m+rd} sauf pour un nombre fini'",
      "tels que f^r x∈𝔭_{m+rd} sauf pour un nombre fini de valeurs de r (no comma)",
      r"$f^rx\in\mathfrak{p}_{m+rd}$, sauf",
      "punctuation", "high",
      "défini comme l'ensemble des $x\\in S_m$ tels que\n$f^rx\\in\\mathfrak{p}_{m+rd}$, sauf",
      "défini comme l'ensemble des $x\\in S_m$ tels que\n$f^rx\\in\\mathfrak{p}_{m+rd}$ sauf",
      "No comma here in the print; the similar phrase six lines earlier ('... f^r x∈𝔭_{m+rd}, sauf pour un') does have the comma and the TeX matches it there."),
    # ---------------- page 23 ----------------
    F(23, "(2.1.10), first sentence",
      "et que 𝔍 est un idéal premier gradué de S_+ s'il est l'intersection de S_+",
      r"\emph{idéal premier gradué de $S_+$} si elle est l'intersection",
      "word", "high",
      r"si elle est l'intersection",
      r"s'il est l'intersection",
      "The print has 's'il est', not 'si elle est'."),
    F(23, "(2.1.10): 'autrement dit c'est l'ensemble 𝔯_+(𝔍) = 𝔯(𝔍)∩S_+'",
      "𝔯_+(𝔍) = 𝔯(𝔍)∩S_+ (Fraktur r)",
      r"$r_+(\mathfrak{J})=r(\mathfrak{J})\cap S_+$",
      "font", "high",
      r"$r_+(\mathfrak{J})=r(\mathfrak{J})\cap S_+$",
      r"$\mathfrak{r}_+(\mathfrak{J})=\mathfrak{r}(\mathfrak{J})\cap S_+$",
      r"The radical is the Fraktur 𝔯 in the print (ega0/ega1 sources write \mathfrak{r}(\mathfrak{a})). ega2-1-fr.tex has plain r also at its lines 1865 and 2016 (later pages)."),
    F(23, "(2.1.10): 'sa racine 𝔯_+(𝔍) est un idéal gradué'",
      "sa racine 𝔯_+(𝔍) (Fraktur r)",
      r"sa racine $r_+(\mathfrak{J})$",
      "font", "high",
      "sa racine\n$r_+(\\mathfrak{J})$",
      "sa racine\n$\\mathfrak{r}_+(\\mathfrak{J})$",
      "Fraktur r, as above."),
    F(23, "(2.1.10): 'sa racine 𝔯_+(𝔍) est un idéal gradué : en passant à l'anneau quotient'",
      "est un idéal gradué ('gradué' italic) : en passant",
      r"est un idéal gradué~: en passant",
      "italics", "high",
      r"est un idéal gradué~: en passant",
      r"est un idéal \emph{gradué}~: en passant",
      "Second 'gradué' of the sentence is italic in the print (the first, 'idéal \\emph{gradué} de S_+', is already in the TeX)."),
    F(23, "(2.1.10): 'tout revient à voir que si x = x_h + x_{h+1} + ... + x_k est nilpotent'",
      "x = x_h + x_{h+1} + . . . + x_k (dots on the baseline)",
      r"x=x_h+x_{h+1}+\cdots+x_k (centred dots)",
      "symbol", "high",
      r"x_{h+1}+\cdots+x_k",
      r"x_{h+1}+\ldots+x_k",
      "Baseline dots in the print."),
    # ---------------- page 24 ----------------
    F(24, "(2.2.1), proof that the monomials (f/1)^h are free: 'cette relation équivaut par définition à l'existence d'un k ... tel que Σ f^{h+k} x_h = 0'",
      "l'existence d'un k > −a (printed k>—a)",
      r"l'existence d'un $k\geq a$",
      "misprint_in_print", "high",
      r"d'un $k\geq a$ tel que",
      r"d'un $k>-a$ tel que",
      "The TeX silently corrects the print. The printed k > −a does not make the exponents h+k (h ⩾ −a) of the following sum nonnegative; clearing the denominator f^{m+a} gives such a k with k ⩾ a. Diplomatic text: k>-a; corrected edition: k\\geq a.",
      corrected=r"$k\geq a$"),
    F(24, "proof of Lemme (2.2.2): reference '(0, 1.4.6)'",
      "(0, 1.4.6) with old-style figure 1",
      r"\hyperref[0.1.4.6-fr]{0, I.4.6} (capital letter I)",
      "number", "high",
      r"I.4.6}",
      r"1.4.6}",
      "The TeX has the letter I instead of the digit 1 (the label 0.1.4.6-fr confirms 1.4.6). Independent of the convention-2 fix for the same reference (non-overlapping strings)."),
    F(24, "proof of Lemme (2.2.2): reference '(0, 1.4.6)'",
      "bold 0",
      "plain 0",
      "convention", "high",
      r"0.1.4.6-fr]{0,",
      r"0.1.4.6-fr]{\textbf{0},",
      "Convention 2.",
      convention=2),
    F(24, "(2.2.3), first sentence: 'l'homomorphisme canonique S_f→S_{fg} (0, 1.4.1)'",
      "(0, 1.4.1) with old-style figures 1",
      r"\hyperref[0.1.4.1-fr]{0, I.4.1} (capital letter I)",
      "number", "high",
      r"I.4.1}",
      r"1.4.1}",
      "The TeX has the letter I instead of the digit 1 (label 0.1.4.1-fr). Independent of the convention-2 fix for the same reference."),
    F(24, "(2.2.3), first sentence: reference '(0, 1.4.1)'",
      "bold 0",
      "plain 0",
      "convention", "high",
      r"0.1.4.1-fr]{0,",
      r"0.1.4.1-fr]{\textbf{0},",
      "Convention 2.",
      convention=2),
    F(24, "proof of Proposition (2.2.5): 'on a la congruence f^h x ≡ x (mod. (f−1)S^{(d)})'",
      "f^h x ≡ x (mod. (f−1)S^{(d)}) — 'mod.' with a period",
      r"$f^h x\equiv x\pmod{(f-1)S^{(d)}}$ (typesets 'mod' without the period)",
      "punctuation", "high",
      r"$f^h x\equiv x\pmod{(f-1)S^{(d)}}$",
      r"$f^h x\equiv x$ (mod.~$(f-1)S^{(d)}$)",
      "\\pmod prints '(mod (f−1)S^(d))'; the print has 'mod.', which the file writes as text elsewhere ('(mod. $d$)', 'classe de $x$ mod. $(f-1)S^{(d)}$')."),
]

# verify: every fix's old occurs exactly once in its page file
ok = True
for f in findings:
    if f["fix"] is None:
        continue
    text = (RUN / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    n = text.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/MISSING", f["page"], n, repr(f["fix"]["old"]))
    if f["fix"]["old"] == f["fix"]["new"]:
        ok = False
        print("NO-OP", f["page"], repr(f["fix"]["old"]))

# verify that fixes on the same page do not overlap
from collections import defaultdict
spans = defaultdict(list)
for f in findings:
    if f["fix"] is None:
        continue
    text = (RUN / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    i = text.find(f["fix"]["old"])
    spans[f["page"]].append((i, i + len(f["fix"]["old"]), f["where"][:40]))
for p, lst in spans.items():
    lst.sort()
    for a, b in zip(lst, lst[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP on page", p, a, b)

if not ok:
    sys.exit(1)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter()
for f in findings:
    k = "convention" if f["kind"] == "convention" else ("misprint" if f["kind"] == "misprint_in_print" else "normal")
    c[(f["page"], k)] += 1
for p in range(20, 25):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("written", OUT, len(findings))
