import json
import os

RUN = r"user\Documents\ega_scan_check_20261101\run_0I"
OUT = os.path.join(RUN, "findings_026_030.json")
NL = "\n"


def tex(p):
    with open(os.path.join(RUN, "page_%03d.tex" % p), "rb") as f:
        return f.read().decode("utf-8").replace("\r\n", "\n")


findings = []

ESC = {"\\u00e9": "é", "\\u00e0": "à", "\\u00ea": "ê"}


def U(s):
    # raw strings keep é etc. literally; turn exactly these escapes into the characters
    if s is None:
        return None
    for a, b in ESC.items():
        s = s.replace(a, b)
    return s


def add(page, where, scan, tx, kind, conv, conf, old, new, note, corrected=None):
    tx, old, new, corrected = U(tx), U(old), U(new), U(corrected)
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tx,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    findings.append(d)


KNOTE = ("The print sets the category K in bold italic; \\mathbf{K} is bold upright. "
         "Same pattern as conventions 1 and 10 (bold italic k, P); a global "
         "\\mathbf{K} -> \\boldsymbol{K} would cover every occurrence.")


def k(page, where, old):
    add(page, where, "bold italic K", r"\mathbf{K}", "font", None, "high",
        old, old.replace(r"\mathbf{K}", r"\boldsymbol{K}"), KNOTE)


# ---------------- page 26 ----------------
add(26, "page line 3, (3.2.1): definition of F'(U)",
    "F'(U) = lim F(V), with only the arrow under lim (no index)",
    r"\varprojlim_{V\subset U}\mathcal{F}(V)",
    "formula", None, "high",
    r"\varprojlim_{V\subset U}\mathcal{F}(V)", r"\varprojlim\mathcal{F}(V)",
    "The print has no subscript V\u2282U under the lim; the range of V is given by the following words.")
add(26, "page line 4, (3.2.1): (pour \u2282, non filtrant en g\u00e9n\u00e9ral)",
    "(pour \u2282, *non filtrant* en g\u00e9n\u00e9ral): only 'non filtrant' italic",
    r"\emph{non filtrant en g\u00e9n\u00e9ral}",
    "italics", None, "high",
    r"\emph{non filtrant en" + NL + r"g\u00e9n\u00e9ral})",
    r"\emph{non filtrant} en" + NL + r"g\u00e9n\u00e9ral)",
    "'en g\u00e9n\u00e9ral' is roman in the print.")
add(26, "page line 10, (3.2.1): la transitivit\u00e9 des \u03c1'",
    "la transitivit\u00e9 des \u03c1'^{U'}_U",
    r"la transitivit\u00e9 de $\rho'_U{}^{U'}$",
    "word", None, "high",
    r"transitivit\u00e9 de $\rho'_U{}^{U'}$", r"transitivit\u00e9 des $\rho'_U{}^{U'}$",
    "Print: 'des'.")
k(26, "page line 2, (3.2.1): pr\u00e9faisceau \u00e0 valeurs dans K", r"valeurs dans $\mathbf{K}$}~:")
k(26, "footnote (1), its line 2: que K admet des limites projectives", r"que $\mathbf{K}$ admet des limites projectives")
k(26, "page line 15, (3.2.2), condition (F0): T \u2208 K", r"$T\in\mathbf{K}$")

# ---------------- page 27 ----------------
add(27, "page line 2, (3.2.2): (resp. F'(U_\u03b1))",
    "(resp. F'(U_\u03b1)) with a single prime",
    r"\mathcal{F}''(U_\alpha)",
    "formula", None, "high",
    r"$\mathcal{F}''(U_\alpha)$", r"$\mathcal{F}'(U_\alpha)$",
    "The print has F' (one prime), parallel to F'(U) before it; the TeX has two primes.")
add(27, "page line 6, end of (3.2.2): est un faisceau",
    "est *un faisceau*. ('un' italic too)",
    r"est un \emph{faisceau}.",
    "italics", None, "high",
    r"est un \emph{faisceau}.", r"est \emph{un faisceau}.",
    "")
add(27, "page line 12, (3.2.3): compatibilit\u00e9 avec les \u03c1'",
    "la v\u00e9rification des conditions de compatibilit\u00e9 avec les \u03c1'^{U'}_U d\u00e9coule",
    r"compatibilit\u00e9 avec $\rho'_U{}^{U'}$",
    "missing", None, "high",
    r"compatibilit\u00e9 avec $\rho'_U{}^{U'}$", r"compatibilit\u00e9 avec les $\rho'_U{}^{U'}$",
    "Word 'les' missing in the TeX.")
add(27, "page line 39 (last), (3.2.6): syst\u00e8me projectif (\u210c_\u03bb)",
    "Fraktur \u210c_\u03bb",
    r"\mathcal{H}_\lambda",
    "font", None, "high",
    r"projectif $(\mathcal{H}_\lambda)$ tel", r"projectif $(\mathfrak{H}_\lambda)$ tel",
    "The print uses a Fraktur H here and twice on p. 28 (same sheaves), so it is the printed notation, not a misprint.")
k(27, "page line 7, (3.2.3): \u00e0 valeurs dans K ; on d\u00e9finit", r"dans $\mathbf{K}$~; on d\u00e9finit")
k(27, "page line 14, (3.2.4): Si la cat\u00e9gorie K admet", r"la cat\u00e9gorie $\mathbf{K}$ admet des limites inductives")
k(27, "page line 15, (3.2.4): \u00e0 valeurs dans K, pour tout x", r"dans $\mathbf{K}$," + NL + r"pour tout")
k(27, "page line 19, (3.2.4): sur B \u00e0 valeurs dans K, u'", r"dans $\mathbf{K}$," + NL + r"$u'")
k(27, "page line 23, (3.2.5): \u00e0 valeurs dans K, F_1", r"dans $\mathbf{K}$, $\mathcal{F}_1$")
k(27, "page line 27, (3.2.5): \u00e0 valeurs dans K, et u", r"$\mathbf{K}$, et $u:")
k(27, "page line 33, (3.2.6): Supposons toujours que K", r"toujours que $\mathbf{K}$ admette")
k(27, "page line 34, (3.2.6): faisceaux sur X \u00e0 valeurs dans K", r"dans $\mathbf{K}$} admet aussi")
k(27, "page line 35, (3.2.6): \u00e0 valeurs dans K, les", r"dans $\mathbf{K}$, les")
k(27, "page line 36, (3.2.6): pr\u00e9faisceau \u00e0 valeurs dans K", r"dans $\mathbf{K}$, et la")
k(27, "page line 39, (3.2.6): Lorsque K est", r"Lorsque $\mathbf{K}$ est")

# ---------------- page 28 ----------------
add(28, "page line 1, (3.2.6) cont.: que \u210c_\u03bb soit",
    "Fraktur \u210c_\u03bb",
    r"\mathcal{H}_\lambda",
    "font", None, "high",
    r"que $\mathcal{H}_\lambda$ soit", r"que $\mathfrak{H}_\lambda$ soit",
    "Fraktur H as on p. 27.")
add(28, "page line 1, (3.2.6) cont.: lim \u210c_\u03bb",
    "lim with the arrow only, no index \u03bb under it",
    r"\varprojlim_\lambda\mathcal{H}_\lambda",
    "formula", None, "high",
    r"tout $\lambda$," + NL + r"$\varprojlim_\lambda",
    r"tout $\lambda$," + NL + r"$\varprojlim",
    "Independent of the next finding (the two 'old' strings do not overlap).")
add(28, "page line 1, (3.2.6) cont.: lim \u210c_\u03bb s'identifie",
    "Fraktur \u210c_\u03bb",
    r"\mathcal{H}_\lambda",
    "font", None, "high",
    r"\mathcal{H}_\lambda$ s'identifie", r"\mathfrak{H}_\lambda$ s'identifie",
    "Fraktur H as on p. 27.")
add(28, "page line 2, (3.2.6) cont.: sous-faisceau de lim F_\u03bb",
    "lim with the arrow only, no index \u03bb under it",
    r"\varprojlim_\lambda\mathcal{F}_\lambda",
    "formula", None, "high",
    r"de $\varprojlim_\lambda\mathcal{F}_\lambda$. Si", r"de $\varprojlim\mathcal{F}_\lambda$. Si",
    "")
add(28, "page line 3, (3.2.6) cont.: lim F_\u03bb est additif",
    "lim with the arrow only, no index \u03bb under it",
    r"\varprojlim_\lambda\mathcal{F}_\lambda",
    "formula", None, "high",
    r"$\varprojlim_\lambda\mathcal{F}_\lambda$ est", r"$\varprojlim\mathcal{F}_\lambda$ est",
    "")
add(28, "page line 3, (3.2.6) cont.: additif et exact \u00e0 gauche",
    "*additif* et *exact \u00e0 gauche* ('et' roman)",
    r"\emph{additif et exact \u00e0 gauche}",
    "italics", None, "high",
    r"\emph{additif et exact \u00e0 gauche}", r"\emph{additif} et \emph{exact \u00e0 gauche}",
    "")
add(28, "(3.3.1), its lines 6-7: (condition de recollement pour les \u03b8_\u03bb\u03bc)",
    "(*condition de recollement* pour les \u03b8_\u03bb\u03bc): 'pour les' roman",
    r"(\emph{condition de recollement pour les $\theta_{\lambda\mu}$})",
    "italics", None, "high",
    r"(\emph{condition de recollement pour les $\theta_{\lambda\mu}$})",
    r"(\emph{condition de recollement} pour les $\theta_{\lambda\mu}$)",
    "")
add(28, "(3.3.1), its line 13: la fonction \u03c4 de Hilbert",
    "bold \u03c4",
    r"$\tau$",
    "font", None, "high",
    r"fonction $\tau$ de Hilbert", r"fonction $\boldsymbol{\tau}$ de Hilbert",
    "")
k(28, "page line 2, (3.2.6) cont.: Si K est la cat\u00e9gorie des groupes commutatifs", r"$\mathbf{K}$ est la cat\u00e9gorie des groupes")
k(28, "(3.3.1), its line 1: la cat\u00e9gorie K admette", r"cat\u00e9gorie $\mathbf{K}$ admette")
k(28, "(3.3.1), its line 3: \u00e0 valeurs dans K ; pour tout couple", r"dans $\mathbf{K}$~; pour tout couple")
k(28, "(3.3.1), its line 7: \u00e0 valeurs dans K, et pour chaque \u03bb", r"dans $\mathbf{K}$, et pour")
k(28, "(3.3.1), last paragraph, its line 1: \u00e0 valeurs dans K peut \u00eatre", r"$\mathbf{K}$ peut \u00eatre")
k(28, "(3.3.2), its line 2: \u00e0 valeurs dans K, et soit", r"dans $\mathbf{K}$, et soit")

# ---------------- page 29 ----------------
k(29, "(3.4.1), its line 2: une cat\u00e9gorie K ; pour tout ouvert", r"cat\u00e9gorie $\mathbf{K}$~; pour tout ouvert")
k(29, "(3.4.1), its line 5: \u00e0 valeurs dans K, que l'on appelle", r"dans $\mathbf{K}$, que l'on")
k(29, "(3.4.2), its line 1: \u00e0 valeurs dans K, et soit", r"dans $\mathbf{K}$, et soit")
k(29, "(3.4.2), its line 6: \u00e0 valeurs dans K, on a", r"dans $\mathbf{K}$, on a")
k(29, "(3.4.2), its line 8: \u00e0 valeurs dans K, dans celle", r"$\mathbf{K}$, dans celle")
k(29, "(3.4.2), its line 8 (end): sur Y \u00e0 valeurs dans K.", r"$Y$ \u00e0 valeurs dans $\mathbf{K}$.")
k(29, "(3.4.3), its line 3: \u00e0 valeurs dans K ; en outre", r"$\mathbf{K}$~; en")
k(29, "(3.4.4), its line 1: la cat\u00e9gorie K admette", r"cat\u00e9gorie $\mathbf{K}$ admette")
k(29, "(3.4.4), its line 2: \u00e0 valeurs dans K ; pour tout x", r"dans $\mathbf{K}$~; pour tout")

# ---------------- page 30 ----------------
add(30, "heading of (3.4.5), page line 6 (diagram not counted)",
    "3.4.5) (no opening parenthesis)",
    r"\begin{env}[3.4.5] (prints (3.4.5))",
    "misprint_in_print", None, "high",
    None, None,
    "The print omits the opening parenthesis of the heading. The TeX silently corrects it: the env "
    "environment prints \\textbf{(#1)}, so no page-level edit can restore the printed reading; "
    "it needs an env variant without the opening parenthesis (coordinator).",
    corrected=r"\textbf{(3.4.5)}")
add(30, "(3.4.6), its line 7: et 0 sur Y\u2014X",
    "Y\u2014X (long dash)",
    r"$Y-X$",
    "convention", 7, "high",
    r"$Y-X$", r"$Y\setmin X$",
    "")
add(30, "(3.5.1), its line 5: 'Pour tout couple (U, V)'",
    "no paragraph break: 'Pour tout couple' continues the paragraph, flush left without indent",
    "blank line before 'Pour tout couple' (new paragraph)",
    "other", None, "medium",
    r"$\mathcal{F}$." + NL + NL + r"Pour tout couple", r"$\mathcal{F}$." + NL + r"Pour tout couple",
    "The line before ends at the right margin; the paragraph continuation is shown by the missing indent.")
k(30, "page line 3, (3.4.4) cont.: \u00e0 valeurs dans K, le diagramme", r"dans $\mathbf{K}$, le diagramme")
k(30, "(3.4.6), its line 1: Supposons que K soit", r"que $\mathbf{K}$ soit")
k(30, "(3.4.6), its line 2: \u00e0 valeurs dans K, de support S", r"dans $\mathbf{K}$, de")
k(30, "(3.5.1), its line 2: \u00e0 valeurs dans K, tout morphisme", r"dans $\mathbf{K}$, tout morphisme")

# ---------------- checks ----------------
texts = {p: tex(p) for p in range(26, 31)}
bad = 0
for f in findings:
    if f["fix"] is None:
        continue
    old = f["fix"]["old"]
    n = texts[f["page"]].count(old)
    if n != 1:
        bad += 1
        print("NOT UNIQUE/MISSING", f["page"], n, repr(old))
# overlapping fixes on the same page
for p in range(26, 31):
    spans = []
    t = texts[p]
    for f in findings:
        if f["page"] == p and f["fix"] is not None:
            i = t.find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP", p, repr(a[2]), repr(b[2]))
# every \mathbf{K} covered
for p in range(26, 31):
    t = texts[p]
    total = t.count(r"\mathbf{K}")
    covered = sum(1 for f in findings if f["page"] == p and f["fix"] and r"\mathbf{K}" in f["fix"]["old"])
    print("page", p, "mathbf K", total, "covered", covered)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for f in findings:
    cat = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], cat)] += 1
for p in range(26, 31):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(findings), "bad", bad)
