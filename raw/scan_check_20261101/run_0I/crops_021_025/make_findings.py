import json
import os

RUN = r"user\Documents\ega_scan_check_20261101\run_0I"
OUT = os.path.join(RUN, "findings_021_025.json")
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega1\ega0-1-fr.tex"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
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
    F.append(d)


# ---------------- page 21 ----------------
add(21, "(2.1.3), 2nd paragraph: 'il n'en admet qu'un seul puisqu'un ouvert'",
    "qu'un seul with only 'un seul' italic ('qu'' roman)",
    r"\emph{qu'un seul}",
    "italics", None, "high",
    r"\emph{qu'un seul}", r"qu'\emph{un seul}",
    "Checked on an enlarged crop: q, u and the apostrophe are upright.")

add(21, "(2.1.3), 3rd paragraph: 'd'ensembles fermés non vides a une intersection non vide)'",
    "une inter-section non vide (hyphen in the middle of the line, not at a line break)",
    "une intersection non vide",
    "misprint_in_print", None, "medium",
    "une intersection non vide", "une inter-section non vide",
    "Stray word-division hyphen left mid-line in the print (enlarged crop); the TeX silently corrects it. "
    "The printed reading is certain; medium only because it is a typographical rather than a textual misprint.",
    corrected="une intersection non vide")

# ---------------- page 22 ----------------
add(22, "(2.1.7), last sentence: 'alors les adhérences Ȳ_i dans X'",
    "bar over Y only, subscript i outside the bar",
    r"$\overline{Y_i}$ (bar over Y_i)",
    "formula", None, "medium",
    r"$\overline{Y_i}$", r"$\overline{Y}_i$",
    "Enlarged crop. Same kind of bar-extent difference as \\overline{X'} -> \\overline{X}' reported for p. 119 "
    "(analogue of convention 8 for an overline).")

add(22, "(2.1.8), last sentence: 'l'ensemble des composantes irréductibles Z∩f^{-1}(Y) de f^{-1}(y)'",
    "Z∩f^{-1}(Y) with an upright capital Y",
    r"$Z\cap f^{-1}(y)$",
    "misprint_in_print", None, "high",
    r"$Z\cap f^{-1}(y)$ de $f^{-1}(y)$", r"$Z\cap f^{-1}(Y)$ de $f^{-1}(y)$",
    "The TeX silently corrects the print. f^{-1}(Y) is all of X; the components meant are those of the fibre "
    "f^{-1}(y), as in the rest of (2.1.8). Checked on an enlarged crop.",
    corrected=r"$Z\cap f^{-1}(y)$")

# ---------------- page 23 ----------------
P_NOTE = ("Property letter P printed bold italic (enlarged crop); the TeX has a plain italic P, so a global "
          "\\mathbf{P}->\\boldsymbol{P} pass would not catch it. \\boldsymbol as in FIX_POLICY (bold italic k, P).")
p23_P = [
    ("(2.2.2), 1st sentence: 'et soit P une propriété'", r"$P$ une propriété", r"$\boldsymbol{P}$ une propriété"),
    ("(2.2.2), 1st sentence: 'pour tout x<a, P(x) soit vraie'", r"$P(x)$ soit vraie", r"$\boldsymbol{P}(x)$ soit vraie"),
    ("(2.2.2), 1st sentence: 'alors P(a) est vraie'", r"alors $P(a)$ est", r"alors $\boldsymbol{P}(a)$ est"),
    ("(2.2.2), 2nd sentence: 'P(x) est vraie pour tout x∈E'", r"\emph{$P(x)$ est vraie", r"\emph{$\boldsymbol{P}(x)$ est vraie"),
    ("(2.2.2), proof: 'pour lesquels P(x) est fausse'", r"$P(x)$ est fausse", r"$\boldsymbol{P}(x)$ est fausse"),
    ("(2.2.2), proof: 'comme alors P(x) est vraie pour tout x<a'", r"comme alors $P(x)$ est vraie",
     r"comme alors $\boldsymbol{P}(x)$ est vraie"),
    ("(2.2.2), proof: 'P(a) serait aussi vraie'", r"$P(a)$" + NL + "serait", r"$\boldsymbol{P}(a)$" + NL + "serait"),
]
for where, old, new in p23_P:
    add(23, where, "bold italic P", "plain $P$", "font", None, "high", old, new, P_NOTE)

K_NOTE = ("Category letter K printed bold italic (checked on enlarged crops); \\mathbf{K} gives bold upright. "
          "Same issue as convention 10 for P; \\boldsymbol as in FIX_POLICY.")
p23_K = [
    ("(3.1.1), 1st line: 'Soient K une catégorie'", r"Soient $\mathbf{K}$ une catégorie", r"Soient $\boldsymbol{K}$ une catégorie"),
    ("(3.1.1): 'deux familles d'objets de K telles que'", r"$\mathbf{K}$ telles que", r"$\boldsymbol{K}$ telles que"),
    ("(3.1.1): 'd'un objet A de K et d'une famille'", r"objet $A$ de $\mathbf{K}$", r"objet $A$ de $\boldsymbol{K}$"),
    ("(3.1.1): 'pour tout objet B de K, l'application'", r"objet $B$ de $\mathbf{K}$", r"objet $B$ de $\boldsymbol{K}$"),
    ("(3.1.2): 'à valeurs dans une catégorie K (G, I, 1.9)'", r"catégorie $\mathbf{K}$ (G, I, 1.9)",
     r"catégorie $\boldsymbol{K}$ (G, I, 1.9)"),
    ("(3.1.2): 'faisceau à valeurs dans K s'il satisfait'", r"dans $\mathbf{K}$} s'il satisfait",
     r"dans $\boldsymbol{K}$} s'il satisfait"),
]
for where, old, new in p23_K:
    add(23, where, "bold italic K", r"\mathbf{K} (bold upright)", "font", None, "high", old, new, K_NOTE)

add(23, "(3.1.2), axiom (F): 'si on désigne par ρ_α (resp. ρ_αβ) le morphisme de restriction'",
    "'(resp.' and the closing parenthesis roman inside the italic axiom",
    r"(resp. $\rho_{\alpha\beta}$) inside \emph{...}",
    "convention", 6, "high",
    r"(resp. $\rho_{\alpha\beta}$)", r"\textup{(resp. $\rho_{\alpha\beta}$)}",
    "Enlarged crop. Form of the fix as in the p. 85 precedent ('(resp.' and ')' roman).")

# ---------------- page 24 ----------------
add(24, "(3.1.2), end of axiom (F): '... et (ρ_αβ) (3.1.1) (1).'",
    "reference (3.1.1) upright inside the italic axiom",
    r"(3.1.1) inside \emph{...}",
    "convention", 6, "high",
    r"(3.1.1)}%", r"\textup{(3.1.1)}}%",
    "Enlarged crop: the parentheses and old-style figures are roman.")

add(24, "(3.1.3), 'Dans ces conditions': 'considéré comme préfaisceau d'ensembles, U→F(U)'",
    "d'ensembles with only 'ensembles' italic ('d'' roman)",
    r"préfaisceau \emph{d'ensembles}",
    "italics", None, "high",
    r"préfaisceau \emph{d'ensembles}", r"préfaisceau d'\emph{ensembles}",
    "Enlarged crop.")

add(24, "(3.1.4), 1st sentence: 'est un faisceau d'ensembles entraîne ipso facto'",
    "faisceau d'ensembles with only 'ensembles' italic",
    r"\emph{faisceau d'ensembles} entraîne",
    "italics", None, "high",
    r"\emph{faisceau d'ensembles} entraîne", r"faisceau d'\emph{ensembles} entraîne",
    "Enlarged crop: 'faisceau d'' roman.")

add(24, "(3.1.4), 1st sentence: 'que c'est un faisceau à valeurs dans K (autrement dit'",
    "'faisceau' roman, 'à valeurs dans' italic, K bold italic",
    r"\emph{faisceau à valeurs dans $\mathbf{K}$} (all italic, K bold upright)",
    "italics", None, "high",
    r"\emph{faisceau à valeurs dans $\mathbf{K}$} (autrement",
    r"faisceau \emph{à valeurs dans $\boldsymbol{K}$} (autrement",
    "Enlarged crop. This fix also makes the bold italic K change for this occurrence (no separate K finding here).")

p24_K = [
    ("(3.1.2), after (F): 'pour tout objet T de K, la famille'", r"objet $T$ de $\mathbf{K}$", r"objet $T$ de $\boldsymbol{K}$"),
    ("(3.1.3), 1st sentence: 'Supposons que K soit la catégorie'", r"Supposons que $\mathbf{K}$ soit",
     r"Supposons que $\boldsymbol{K}$ soit"),
    ("(3.1.3), 1st sentence: 'les objets de K étant donc'", r"les objets de $\mathbf{K}$ étant",
     r"les objets de $\boldsymbol{K}$ étant"),
    ("(3.1.3), 2nd sentence: 'la catégorie K vérifie en outre'", r"la catégorie $\mathbf{K}$ vérifie",
     r"la catégorie $\boldsymbol{K}$ vérifie"),
    ("(3.1.3), condition (E): 'dans la catégorie K pour des familles'", r"\emph{dans la catégorie $\mathbf{K}$}",
     r"\emph{dans la catégorie $\boldsymbol{K}$}"),
    ("footnote (2): 'le foncteur canonique K→(Ens)'", r"$\mathbf{K}\to(\mathrm{Ens})$", r"$\boldsymbol{K}\to(\mathrm{Ens})$"),
    ("(3.1.3), 'En outre': 'soit un morphisme de K, il faut et il suffit'", r"$\mathbf{K}$, il faut et il suffit",
     r"$\boldsymbol{K}$, il faut et il suffit"),
    ("(3.1.3), 'Réciproquement': 'sur X, à valeurs dans K, soit un faisceau d'ensembles'", r"$\mathbf{K}$, soit un",
     r"$\boldsymbol{K}$, soit un"),
    ("(3.1.3), end: 'donc est un faisceau à valeurs dans K.'",
     r"donc est un" + NL + r"\emph{faisceau à valeurs dans $\mathbf{K}$}",
     r"donc est un" + NL + r"\emph{faisceau à valeurs dans $\boldsymbol{K}$}"),
    ("(3.1.4), 1st sentence: 'le préfaisceau U→F(U) à valeurs dans K est un'",
     r"$U\to\mathcal{F}(U)$ à valeurs dans $\mathbf{K}$ est un",
     r"$U\to\mathcal{F}(U)$ à valeurs dans $\boldsymbol{K}$ est un"),
    ("footnote (3): 'dans la catégorie K, tout morphisme'", r"la catégorie $\mathbf{K}$, tout",
     r"la catégorie $\boldsymbol{K}$, tout"),
    ("footnote (3): 'lorsque K est la catégorie des espaces topologiques'", r"plus vrai lorsque $\mathbf{K}$ est la",
     r"plus vrai lorsque $\boldsymbol{K}$ est la"),
    ("(3.1.4): 'lorsque par exemple K est la catégorie des anneaux topologiques'", r"par exemple $\mathbf{K}$ est la",
     r"par exemple $\boldsymbol{K}$ est la"),
    ("(3.1.4): 'un faisceau à valeurs dans K est un faisceau d'anneaux'", r"dans $\mathbf{K}$ est un faisceau d'anneaux",
     r"dans $\boldsymbol{K}$ est un faisceau d'anneaux"),
]
for where, old, new in p24_K:
    add(24, where, "bold italic K", r"\mathbf{K} (bold upright)", "font", None, "high", old, new, K_NOTE)

# ---------------- page 25 ----------------
p25_K = [
    ("(3.1.5), 1st sentence: 'pour toute catégorie K, si F est un préfaisceau'", r"toute catégorie $\mathbf{K}$, si",
     r"toute catégorie $\boldsymbol{K}$, si"),
    ("(3.1.5): 'sur X à valeurs dans K et U un ouvert'", r"dans $\mathbf{K}$ et $U$ un", r"dans $\boldsymbol{K}$ et $U$ un"),
    ("(3.1.5): 'à valeurs dans K, que l'on appelle'", r"dans $\mathbf{K}$, que l'on", r"dans $\boldsymbol{K}$, que l'on"),
    ("(3.1.5), 2nd paragraph: 'à valeurs dans K, on désignera'", r"dans $\mathbf{K}$, on désignera",
     r"dans $\boldsymbol{K}$, on désignera"),
    ("(3.1.6), 1st sentence: 'la catégorie K admette des limites inductives'", r"la catégorie $\mathbf{K}$ admette",
     r"la catégorie $\boldsymbol{K}$ admette"),
    ("(3.1.6): 'à valeurs dans K et tout x∈X'", r"dans $\mathbf{K}$ et tout $x\in X$", r"dans $\boldsymbol{K}$ et tout $x\in X$"),
    ("(3.1.6): 'comme l'objet de K limite inductive'", r"l'objet de $\mathbf{K}$", r"l'objet de $\boldsymbol{K}$"),
    ("(3.1.6): 'de préfaisceaux à valeurs dans K, on définit'", r"$\mathbf{K}$, on définit pour tout",
     r"$\boldsymbol{K}$, on définit pour tout"),
    ("(3.1.6): 'foncteur covariant en F, à valeurs dans K, pour tout x∈X'", r"dans $\mathbf{K}$, pour tout $x\in X$.",
     r"dans $\boldsymbol{K}$, pour tout $x\in X$."),
    ("(3.1.6), 2nd paragraph: 'Lorsque K est en outre définie'", r"Lorsque $\mathbf{K}$ est en outre",
     r"Lorsque $\boldsymbol{K}$ est en outre"),
    ("(3.1.6), 2nd paragraph: 'à valeurs dans K les éléments de F(U)'", r"dans $\mathbf{K}$ les éléments",
     r"dans $\boldsymbol{K}$ les éléments"),
    ("(3.1.6), 3rd paragraph: 'morphisme de faisceaux à valeurs dans K, on écrira'", r"dans $\mathbf{K}$, on écrira",
     r"dans $\boldsymbol{K}$, on écrira"),
    ("(3.1.6), last paragraph: 'Lorsque K est définie par une espèce de structure'", r"Lorsque $\mathbf{K}$ est définie",
     r"Lorsque $\boldsymbol{K}$ est définie"),
    ("(3.1.6), last paragraph: 'les faisceaux à valeurs dans K ; autrement dit'", r"$\mathbf{K}$~; autrement dit",
     r"$\boldsymbol{K}$~; autrement dit"),
    ("(3.2.1), 1st sentence: 'à des catégories K admettant'", r"à des catégories $\mathbf{K}$",
     r"à des catégories $\boldsymbol{K}$"),
    ("(3.2.1): 'préfaisceau sur B, à valeurs dans K, une famille'", r"dans $\mathbf{K}$}, une famille",
     r"dans $\boldsymbol{K}$}, une famille"),
    ("(3.2.1): 'une famille d'objets F(U)∈K, attachés'", r"\in\mathbf{K}$, attachés", r"\in\boldsymbol{K}$, attachés"),
]
for where, old, new in p25_K:
    add(25, where, "bold italic K", r"\mathbf{K} (bold upright)", "font", None, "high", old, new, K_NOTE)

# ---------------- checks ----------------
pages = {}
for p in (21, 22, 23, 24, 25):
    with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8", newline="") as fh:
        pages[p] = fh.read().replace("\r\n", "\n")  # page files are CRLF; release files are LF
with open(SRC, encoding="utf-8", newline="") as fh:
    raw = fh.read()
    print("source has CR:", "\r" in raw)
    src = raw.replace("\r\n", "\n")

bad = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    t = pages[d["page"]]
    n = t.count(fx["old"])
    s = src.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT on page", d["page"], n, repr(fx["old"]))
    if s < 1:
        print("not in source:", d["page"], repr(fx["old"]))
    if "\r" in fx["old"]:
        print("CR in old", d["page"])

# overlapping fixes on the same page
for p in pages:
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = pages[p].find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            print("OVERLAP on page", p, repr(a[2]), repr(b[2]))

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in (21, 22, 23, 24, 25):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "bad", bad)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("wrote", OUT)
