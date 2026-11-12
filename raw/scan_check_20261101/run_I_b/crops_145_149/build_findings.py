"""Build findings_145_149.json and check every fix: "old" must occur exactly once in page_NNN.tex and in the page
segment of the source file (located as apply_fixes.py does). Read-only on all .tex files."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_I_b"
OUT = RUN / "findings_145_149.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


RESP = "'resp.' roman in the print inside the italic statement; italic in the TeX environment."
KBOLD = "Bold italic k in the print; plain k in the TeX."
LBL = "Labels a), b), c), ... are italic in the roman proof text of the print; the TeX sets them roman."
RG = ("The print sets rg in italics (checked on a crop at 3x); \\operatorname{rg} is upright. "
      "Same for all seven rg of (6.4.5) and its two displays.")
ITEM = ("The print's labels are roman 'a)'-'e)' with no opening parenthesis (checked on a crop); "
        "\\item[\\rm(a)] prints '(a)'. Same pattern as Lemme (1.3.2) in the pilot findings (p. 84).")
REF = "Reference printed upright inside the italic statement; italic in the TeX environment."

# ---------------- page 145 ----------------
add(145, "proof of (6.3.3): 'l'image canonique de b dans B_{g_i} est de la forme b'_i/g_i^{m_i}'",
    "subscript of B printed 'gi' on one level (B_{gi}): the i is not lowered as a second-order index",
    r"dans $B_{g_i}$", "misprint_in_print", None, "medium",
    r"dans $B_{g_i}$", r"dans $B_{gi}$",
    "The TeX silently corrects the print. Checked on a crop at 3x: g and i have the same size and baseline, "
    "while 'tels que B_{g_i}' a few lines earlier on the same page has the i lowered. Same typesetting slip as "
    "(𝒩_X|U_i)^{ni} on p. 142 and 𝒪_{xi}, A(Z_j)_{gj} on p. 144.",
    corrected=r"B_{g_i}")

# ---------------- page 146 ----------------
add(146, "proof of Corollaire (6.3.5): 'et A(D(g_i))=A(Y)_{g_i}=A(Y)[1/g_i] est de type fini sur A(Y)'",
    "subscript of A(Y) printed 'gi' on one level (A(Y)_{gi}): the i is not lowered as a second-order index",
    r"$A(D(g_i))=A(Y)_{g_i}=A(Y)[1/g_i]$", "misprint_in_print", None, "medium",
    r"=A(Y)_{g_i}=", r"=A(Y)_{gi}=",
    "The TeX silently corrects the print. Checked on a crop at 2.5x: g and i have the same size and baseline. "
    "Same slip as B_{gi} on p. 145 and A(Z_j)_{gj} on p. 144.",
    corrected=r"A(D(g_i))=A(Y)_{g_i}=A(Y)[1/g_i]")
add(146, "Corollaire (6.3.5): 'Si l'espace sous-jacent à Y (resp. X) est localement noethérien'",
    "'(resp. X)' roman inside the italic statement", r"(resp. $X$)", "convention", 6, "high",
    r"(resp. $X$)", r"\textup{(resp. $X$)}", RESP + " Checked on a crop.")
add(146, "Corollaire (6.3.5): '(resp. noethérien), f est de type fini'",
    "'(resp.' roman inside the italic statement; 'noethérien' italic", r"(resp. noethérien)", "convention", 6, "high",
    r"(resp. noethérien)", r"\textup{(resp.} noethérien)", RESP)
add(146, "Proposition (6.3.7): 'si Y est noethérien (resp. localement noethérien)'",
    "'(resp.' roman inside the italic statement", r"si $Y$ est noethérien (resp.", "convention", 6, "high",
    r"si $Y$ est noethérien (resp.", r"si $Y$ est noethérien \textup{(resp.}", RESP)
add(146, "Proposition (6.3.7): 'X est noethérien (resp. localement noethérien).'",
    "'(resp.' roman inside the italic statement", r"$X$ est noethérien (resp.", "convention", 6, "high",
    r"$X$ est noethérien (resp.", r"$X$ est noethérien \textup{(resp.}", RESP)
add(146, "Corollaire (6.3.8): 'telle que S' soit noethérien (resp. localement noethérien)'",
    "'(resp.' roman inside the italic statement", r"soit noethérien (resp.", "convention", 6, "high",
    r"soit noethérien (resp.", r"soit noethérien \textup{(resp.}", RESP)
add(146, "Corollaire (6.3.8): 'X_(S') est noethérien (resp. localement noethérien).'",
    "'(resp.' roman inside the italic statement", r"$X_{(S')}$ est noethérien (resp.", "convention", 6, "high",
    r"$X_{(S')}$ est noethérien (resp.", r"$X_{(S')}$ est noethérien \textup{(resp.}", RESP)

# ---------------- page 147 ----------------
add(147, "Proposition (6.3.10): 'pour tout corps algébriquement clos Ω, l'application'",
    "'algébriquement clos' set in roman inside the italic statement ('pour tout corps' and 'l'application' italic)",
    r"pour tout corps algébriquement clos $\Omega$", "convention", 6, "high",
    r"pour tout corps algébriquement clos $\Omega$", r"pour tout corps \textup{algébriquement clos} $\Omega$",
    "Checked on a crop: upright roman letters between italic words.")
add(147, "Proposition (6.3.10): 'l'application X(Ω)→Y(Ω) correspondant à f (3.4.1) soit surjective'",
    "(3.4.1) upright inside the italic statement", r"(\hyperref[I.3.4.1-fr]{3.4.1})", "convention", 6, "high",
    r"(\hyperref[I.3.4.1-fr]{3.4.1})", r"\textup{(\hyperref[I.3.4.1-fr]{3.4.1})}", REF + " Checked on a crop.")
add(147, "proof of (6.3.10): 'une extension algébriquement close Ω de k(y)'",
    "bold italic k(y)", r"$k(y)$", "convention", 1, "high",
    r"de $k(y)$, et le", r"de $\boldsymbol{k}(y)$, et le", KBOLD)
add(147, "proof of (6.3.10): '(cf. (3.5.3)). Inversement'",
    "'cf.' in roman (roman proof text)", r"(\emph{cf.} (\hyperref[I.3.5.3-fr]{3.5.3}))", "italics", None, "high",
    r"(\emph{cf.} (\hyperref[I.3.5.3-fr]{3.5.3}))", r"(cf. (\hyperref[I.3.5.3-fr]{3.5.3}))",
    "Checked on a crop at 3x: upright c and f. The TeX's \\emph sets 'cf.' in italics.")
add(147, "proof of (6.3.10): 'Inversement, supposons f surjective, et soit g : {ξ}=Spec(Ω)→Y un morphisme'",
    "supposons f surjective", r"supposons $f$ surjective", "misprint_in_print", None, "medium",
    None, None,
    "The TeX keeps the printed reading. f is a morphism (masculine): the statement reads 'Pour que f soit "
    "surjectif' and the proof continues 'Comme f est surjectif'. Gender slip in the print.",
    corrected=r"supposons $f$ surjectif")
add(147, "Définition (6.4.1): 'on appelle K-préschéma algébrique un préschéma X'",
    "'K-préschéma algébrique' in italics like the rest of the definition (no change of face)",
    r"\emph{$K$-préschéma algébrique}", "convention", 6, "high",
    r"\emph{$K$-préschéma algébrique}", r"$K$-préschéma algébrique",
    "\\emph inside the italic definition environment sets the words upright; drop the \\emph. Checked on a crop.")
add(147, "Définition (6.4.1): 'K est appelé le corps de base de X'",
    "'corps de base' in italics like the rest of the definition (no change of face)",
    r"\emph{corps de base}", "convention", 6, "high",
    r"\emph{corps de base}", r"corps de base",
    "\\emph inside the italic definition environment sets the words upright; drop the \\emph.")
add(147, "Définition (6.4.1): '(ou, ce qui revient au même (5.5.8), si X est un K-schéma)'",
    "'(ou, ce qui revient au même (5.5.8), si X est un K-' and the closing parenthesis in roman inside the italic "
    "statement; only 'schéma' italic",
    r"(ou, ce qui revient au même (\hyperref[I.5.5.8-fr]{5.5.8}), si $X$ est un $K$-schéma)",
    "convention", 6, "high",
    r"(ou, ce qui revient au même" + NL + r"(\hyperref[I.5.5.8-fr]{5.5.8}), si $X$ est un $K$-schéma)",
    r"\textup{(ou, ce qui revient au même" + NL + r"(\hyperref[I.5.5.8-fr]{5.5.8}), si $X$ est un $K$-}schéma\textup{)}",
    "Checked on a crop. The 'old' spans the line break after 'même'.")
add(147, "Définition (6.4.1): 'on dit aussi que X est un K-schéma algébrique.'",
    "'K-schéma algébrique' in italics like the rest of the definition (no change of face)",
    r"\emph{$K$-schéma algébrique}", "convention", 6, "high",
    r"\emph{$K$-schéma algébrique}", r"$K$-schéma algébrique",
    "\\emph inside the italic definition environment sets the words upright; drop the \\emph.")
add(147, "Proposition (6.4.2): 'il faut et il suffit que k(x) soit une extension algébrique de K'",
    "bold italic k(x)", r"$k(x)$", "convention", 1, "high",
    r"que $k(x)$ soit", r"que $\boldsymbol{k}(x)$ soit", KBOLD)

# ---------------- page 148 ----------------
add(148, "proof of (6.4.2): 'un corps (nécessairement égal à k(x))'",
    "bold italic k(x)", r"$k(x)$", "convention", 1, "high",
    r"égal à $k(x)$", r"égal à $\boldsymbol{k}(x)$", KBOLD)
add(148, "proof of (6.4.2): 'si x est fermé, k(x) est un corps'",
    "bold italic k(x)", r"$k(x)$", "convention", 1, "high",
    r"fermé, $k(x)$ est un corps", r"fermé, $\boldsymbol{k}(x)$ est un corps", KBOLD)
add(148, "proof of (6.4.2): 'Inversement, si k(x) est de rang fini sur K'",
    "bold italic k(x)", r"$k(x)$", "convention", 1, "high",
    r"si $k(x)$ est de rang fini", r"si $\boldsymbol{k}(x)$ est de rang fini", KBOLD)
add(148, "proof of (6.4.2): 'il en est de même de A/𝔧_x⊂k(x)'",
    "bold italic k(x)", r"$A/\mathfrak{j}_x\subset k(x)$", "convention", 1, "high",
    r"\subset k(x)", r"\subset \boldsymbol{k}(x)", KBOLD)
add(148, "proof of (6.4.2): 'on a A/𝔧_x=k(x), donc x est fermé'",
    "bold italic k(x)", r"$A/\mathfrak{j}_x=k(x)$", "convention", 1, "high",
    r"\mathfrak{j}_x=k(x)", r"\mathfrak{j}_x=\boldsymbol{k}(x)", KBOLD)
add(148, "Corollaire (6.4.3): 'les points rationnels sur K (3.4.4) et s'identifient canoniquement'",
    "(3.4.4) upright inside the italic statement", r"(\hyperref[I.3.4.4-fr]{3.4.4})", "convention", 6, "high",
    r"(\hyperref[I.3.4.4-fr]{3.4.4})", r"\textup{(\hyperref[I.3.4.4-fr]{3.4.4})}", REF + " Checked on a crop.")
for lab in ["a", "b", "c", "c'", "d", "e"]:
    add(148, f"Proposition (6.4.4), label {lab})",
        f"roman label '{lab})' without an opening parenthesis", r"\item[\rm(" + lab + ")]", "punctuation", None,
        "high", r"\item[\rm(" + lab + ")]", r"\item[\textup{" + lab + ")}]",
        ITEM if lab == "a" else None)
add(148, "proof of (6.4.4): 'que les conditions a), b), d) sont équivalentes'",
    "a), b), d) in italics", r"les conditions a), b), d) sont", "italics", None, "high",
    r"les conditions a), b), d) sont", r"les conditions \emph{a)}, \emph{b)}, \emph{d)} sont",
    LBL + " Checked on a crop.")
add(148, "proof of (6.4.4): 'et entraînent c) et c')'",
    "c) and c') in italics", r"entraînent c) et c')~;", "italics", None, "high",
    r"entraînent c) et c')~;", r"entraînent \emph{c)} et \emph{c')}~;", LBL)
add(148, "proof of (6.4.4): 'il est clair que e) entraîne a).'",
    "e) and a) in italics", r"que e) entraîne a).", "italics", None, "high",
    r"que e) entraîne a).", r"que \emph{e)} entraîne \emph{a)}.", LBL)
add(148, "proof of (6.4.4): 'Reste à voir que c) entraîne d) et e)'",
    "c), d), e) in italics", r"que c) entraîne d) et e)~;", "italics", None, "high",
    r"que c) entraîne d) et" + NL + r"e)~;", r"que \emph{c)} entraîne \emph{d)} et" + NL + r"\emph{e)}~;",
    LBL + " The 'old' spans the line break before 'e)'.")
add(148, "proof of (6.4.4): 'tout idéal premier de A(X) est donc maximal, d'où d).'",
    "d) in italics", r"d'où d).", "italics", None, "high",
    r"d'où d).", r"d'où \emph{d)}.", LBL)
add(148, "proof of (6.4.4): 'donc un anneau de Jacobson ([1], p. 3-11 et 3-12)'",
    "([1], p. 3-11 et 3-12): the bracket closes after the number, the pages follow outside it",
    r"(\cite[p.~3-11 et 3-12]{I-1})", "punctuation", None, "high",
    r"(\cite[p.~3-11 et 3-12]{I-1})", r"(\cite{I-1}, p.~3-11 et 3-12)",
    "EGA_FR.tex uses the standard \\cite, so the optional argument prints '([1, p. 3-11 et 3-12])'. "
    "This is the only \\cite with an optional argument in EGA I.")
add(148, "(6.4.5): 'on dit que X est un schéma fini sur K (cf. (II, 6.1.1))'",
    "'cf.' in roman (roman paragraph)", r"(\emph{cf.} (\hyperref[II.6.1.1-fr]{II, 6.1.1}))", "italics", None, "high",
    r"(\emph{cf.} (\hyperref[II.6.1.1-fr]", r"(cf. (\hyperref[II.6.1.1-fr]",
    "Checked on a crop at 3x: upright c and f; the env environment is roman, so \\emph sets 'cf.' in italics.")
add(148, "(6.4.5): '(cf. (II, 6.1.1))'",
    "bold II", r"{II, 6.1.1}", "convention", 2, "high",
    r"{II, 6.1.1}", r"{\textbf{II}, 6.1.1}", "Chapter numeral II printed bold (checked on a crop).")
add(148, "(6.4.5): 'de rang [A : K] que l'on note aussi rg_K(X)'",
    "italic rg", r"$\operatorname{rg}_K(X)$", "font", None, "high",
    r"$\operatorname{rg}_K(X)$~; si", r"$\mathit{rg}_K(X)$~; si", RG)
add(148, "(6.4.5.1), left side: 'rg_K(X⨿Y)'",
    "italic rg", r"\operatorname{rg}_K(X\amalg Y)", "font", None, "high",
    r"\operatorname{rg}_K(X\amalg Y)", r"\mathit{rg}_K(X\amalg Y)", None)
add(148, "(6.4.5.1), right side: '=rg_K(X)+rg_K(Y)'",
    "italic rg (twice)", r"=\operatorname{rg}_K(X)+\operatorname{rg}_K(Y)", "font", None, "high",
    r"=\operatorname{rg}_K(X)+\operatorname{rg}_K(Y)", r"=\mathit{rg}_K(X)+\mathit{rg}_K(Y)", None)
add(148, "(6.4.5.2), left side: 'rg_K(X×_K Y)'",
    "italic rg", r"\operatorname{rg}_K(X\times_K Y)", "font", None, "high",
    r"\operatorname{rg}_K(X\times_K Y)", r"\mathit{rg}_K(X\times_K Y)", None)
add(148, "(6.4.5.2), right side: '=rg_K(X)rg_K(Y)'",
    "italic rg (twice)", r"=\operatorname{rg}_K(X)\operatorname{rg}_K(Y)", "font", None, "high",
    r"=\operatorname{rg}_K(X)\operatorname{rg}_K(Y)", r"=\mathit{rg}_K(X)\mathit{rg}_K(Y)", None)
add(148, "Corollaire (6.4.7): 'on pose n=Σ_{x∈X}[k(x) : K]_s'",
    "bold italic k(x)", r"$n=\sum_{x\in X}[k(x):K]_s$", "convention", 1, "high",
    r"[k(x):K]_s", r"[\boldsymbol{k}(x):K]_s", KBOLD)

# ---------------- page 149 ----------------
add(149, "proof of (6.4.7): 'au cas où l'anneau A=A(X) est local (6.2.2)'",
    "'local' in italics", r"$A=A(X)$ est local", "italics", None, "high",
    r"$A=A(X)$ est local", r"$A=A(X)$ est \emph{local}", "Checked on a crop.")
add(149, "(6.4.8): 'ou aussi le nombre géométrique de points de X'",
    "only 'nombre géométrique de points' in italics; 'de X' roman",
    r"\emph{nombre géométrique de points de $X$}", "italics", None, "high",
    r"\emph{nombre géométrique de points de $X$}", r"\emph{nombre géométrique de points} de $X$",
    "Checked on a crop at 3x: the second 'de' is upright.")
add(149, "Proposition (6.4.9): 'l'application X(Ω)_K→Y(Ω)_K correspondant à f (3.4.1) soit surjective'",
    "(3.4.1) upright inside the italic statement", r"(\hyperref[I.3.4.1-fr]{3.4.1})", "convention", 6, "high",
    r"(\hyperref[I.3.4.1-fr]{3.4.1}) soit surjective", r"\textup{(\hyperref[I.3.4.1-fr]{3.4.1})} soit surjective",
    REF + " Checked on a crop.")
add(149, "proof of (6.4.9): 'pour tout y∈Y, k(y) est une extension de K de type fini'",
    "bold italic k(y)", r"$k(y)$", "convention", 1, "high",
    r"$k(y)$ est une extension de $K$", r"$\boldsymbol{k}(y)$ est une extension de $K$", KBOLD)
add(149, "Proposition (6.4.11): 'un préschéma algébrique sur le corps résiduel k(y)'",
    "bold italic k(y)", r"$k(y)$", "convention", 1, "high",
    r"résiduel $k(y)$", r"résiduel $\boldsymbol{k}(y)$", KBOLD)
add(149, "Proposition (6.4.11): 'pour tout x∈f^{-1}(y), k(x) est une extension'",
    "bold italic k(x)", r"$k(x)$", "convention", 1, "high",
    r"$k(x)$ est une extension", r"$\boldsymbol{k}(x)$ est une extension", KBOLD)
add(149, "Proposition (6.4.11): 'une extension de type fini de k(y).'",
    "bold italic k(y)", r"$k(y)$", "convention", 1, "high",
    r"fini de $k(y)$", r"fini de $\boldsymbol{k}(y)$", KBOLD)
add(149, "proof of (6.4.11): 'Comme f^{-1}(y)=X⊗_Y k(y) (3.6.3)'",
    "bold italic k(y)", r"$f^{-1}(y)=X\otimes_Y k(y)$", "convention", 1, "high",
    r"\otimes_Y k(y)", r"\otimes_Y \boldsymbol{k}(y)", KBOLD)
add(149, "Proposition (6.4.12): 'si la fibre f^{-1}(y) est un schéma algébrique fini sur k(y)'",
    "bold italic k(y)", r"$k(y)$", "convention", 1, "high",
    r"fini sur $k(y)$,", r"fini sur $\boldsymbol{k}(y)$,", KBOLD)
add(149, "Proposition (6.4.12): 'alors la fibre f'^{-1}(y') est un schéma algébrique fini sur k(y')'",
    "bold italic k(y')", r"$k(y')$", "convention", 1, "high",
    r"$k(y')$", r"$\boldsymbol{k}(y')$", KBOLD)

# ---------------- checks ----------------
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]["I"]["files"]
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")


def segment(page):
    for f in inv:
        t = pathlib.Path(f).read_text(encoding="utf-8")
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
        for i, (n, s) in enumerate(cuts):
            if n == page:
                return f, t[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(t)]
    return None, None


bad = 0
for x in F:
    if not x["fix"]:
        continue
    old = x["fix"]["old"]
    p = x["page"]
    pt = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    f, seg = segment(p)
    c1, c2 = pt.count(old), (seg.count(old) if seg is not None else -1)
    if c1 != 1 or c2 != 1:
        bad += 1
        print("BAD", p, repr(old), "page file:", c1, "source segment:", c2, f)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
counts = {}
for x in F:
    c = counts.setdefault(x["page"], dict(normal=0, convention=0, misprint=0))
    c["convention" if x["kind"] == "convention" else "misprint" if x["kind"] == "misprint_in_print" else "normal"] += 1
print("written", OUT, len(F), "findings;", "bad fixes:", bad)
for p in sorted(counts):
    print(p, counts[p])
