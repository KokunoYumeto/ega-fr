import json
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_IV3")
OUT = RUN / "findings_245_249.json"

L = []


def add(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence}
    d["fix"] = None if old is None else {"old": old, "new": new}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    L.append(d)


ROMAN_REMARK = "Judged as if the remark body were roman (document-wide remark font)."

# ---------------- page 245 ----------------
add(245, "proof of (15.7.6), l. 3-4: 'Pour voir que c) entraîne b)'",
    "labels c) and b) italic, parenthesis included (crop p245_labels_a.png)",
    "plain upright 'c)', 'b)'", "italics",
    r"Pour voir que c) entraîne b)", r"Pour voir que \emph{c)} entraîne \emph{b)}",
    "Condition labels in roman text are printed italic (letter and parenthesis).")
add(245, "proof of (15.7.6), l. 4: 'en vertu de c), un voisinage'",
    "label c) italic (crop p245_labels_a.png)", "plain upright 'c)'", "italics",
    r"en vertu de c),", r"en vertu de \emph{c)},")
add(245, "proof of (15.7.6), l. 10: 'la factorisation de l'énoncé de b);'",
    "label b) italic", "plain upright 'b)'", "italics",
    r"l'énoncé de b);", r"l'énoncé de \emph{b)};")
add(245, "proof of (15.7.6), l. 12: 'Il est clair que c) implique d) en vertu de (15.7.5)'",
    "labels c) and d) italic (crop p245_labels_c.png)", "plain upright 'c)', 'd)'", "italics",
    r"que c) implique d)", r"que \emph{c)} implique \emph{d)}")
add(245, "proof of (15.7.6), l. 14: 'Prouvons enfin que d) entraîne c);'",
    "labels d) and c) italic (crop p245_labels_c.png)", "plain upright 'd)', 'c)'", "italics",
    r"que d) entraîne c);", r"que \emph{d)} entraîne \emph{c)};")
add(245, "proof of (15.7.6), l. 15: 'il résulte de d), compte tenu de'",
    "label d) italic (crop p245_labels_c.png)", "plain upright 'd)'", "italics",
    r"il résulte de d),", r"il résulte de \emph{d)},")
add(245, "proof of (15.7.6), last line: 'le critère (15.7.5, c))'",
    "label c) italic inside the upright reference (crop p245_labels_c.png)", "plain upright 'c)'", "italics",
    r"le critère (15.7.5, c))", r"le critère (15.7.5, \emph{c)})",
    "Same form as the earlier IV-3 page fixes '(8.1.2, \\emph{a)})'.")
add(245, "Remarques (15.7.7) (i), l. 1: 'Dans (15.7.4, c)), (15.7.5, c)) et (15.7.6, d))'",
    "the three labels c), c), d) italic; the reference parentheses upright",
    "plain 'c)', 'c)', 'd)' (italic only through the italic remarks environment)", "italics",
    r"Dans (15.7.4, c)), (15.7.5, c)) et (15.7.6, d))",
    r"Dans (15.7.4, \emph{c)}), (15.7.5, \emph{c)}) et (15.7.6, \emph{d)})",
    ROMAN_REMARK)
add(245, "Remarques (15.7.7) (i), l. 5: 'l'hypothèse c) est alors vérifiée'",
    "label c) italic", "plain 'c)'", "italics",
    r"l'hypothèse c) est alors", r"l'hypothèse \emph{c)} est alors",
    ROMAN_REMARK)
add(245, "Remarques (15.7.7) (i), last line: 'vérifient aussi l'hypothèse c) (II, 7.3.8)'",
    "label c) italic", "plain 'c)'", "italics",
    r"aussi l'hypothèse c)", r"aussi l'hypothèse \emph{c)}",
    ROMAN_REMARK)
add(245, "Remarques (15.7.7) (ii): 'la condition c) de (15.7.5)'",
    "label c) italic", "plain 'c)'", "italics",
    r"la condition c) de", r"la condition \emph{c)} de",
    ROMAN_REMARK)
add(245, "(15.7.8), last sentence: 'admet une Y-section h : Y→X'",
    "'section' italic (crop p245_ysection.png)", "'section' upright", "italics",
    r"une $Y$-section $h", r"une $Y$-\emph{section} $h",
    "Same form as the p. 222 page fix '$Y$-\\emph{section}'.")
add(245, "(15.7.8), last sentence: 'tout ensemble Z contenant h(Y)'",
    "'contenant' italic (crop p245_ysection.png)", "'contenant' upright", "italics",
    r"$Z$ contenant $h(Y)$", r"$Z$ \emph{contenant} $h(Y)$")
add(245, "(15.7.8): 'l'image réciproque Z'=p^{-1}(Z) de Z par la projection p : X×_Y Y'→Y''",
    "p : X×_Y Y'→Y' (crop p245_proj.png)", "$p:X\\times_Y Y'\\to Y'$ (keeps the print)",
    "misprint_in_print", None, None,
    "The TeX keeps the printed reading. Z is a subset of X, so p^{-1}(Z) needs the projection to X, as in the "
    "proof of (15.7.9) on p. 246 ('la projection canonique p : X×_Y Y'→X').",
    corrected=r"$p:X\times_Y Y'\to X$")
add(245, "Proposition (15.7.9) (i): 'géométriquement connexe sur k(y')'",
    "bold italic k (crop p245_item_i.png)", "\\mathbf k(y')", "convention",
    r"$\mathbf k(y')$", r"$\boldsymbol{k}(y')$", convention=1)
add(245, "Proposition (15.7.9) (i): '(4.5.2)'",
    "reference upright inside the italic statement (crop p245_item_i.png)", "italic (proposition environment)",
    "convention", r"(4.5.2)", r"\textup{(4.5.2)}", convention=6)

# ---------------- page 246 ----------------
add(246, "Proposition (15.7.9) (ii): 'Z_y est propre sur Spec(k(y))'",
    "bold italic k", "\\mathbf k(y)", "convention",
    r"$Z_y$ est propre sur $\operatorname{Spec}(\mathbf k(y))$",
    r"$Z_y$ est propre sur $\operatorname{Spec}(\boldsymbol{k}(y))$", convention=1)
add(246, "Proposition (15.7.9) (iii): 'sur f(Z) (15.7.8)'",
    "reference upright inside the italic statement", "italic (proposition environment)", "convention",
    r"$f(Z)$ (15.7.8)", r"$f(Z)$ \textup{(15.7.8)}", convention=6)
add(246, "Proposition (15.7.9): 'Alors Z est propre sur Y au point y ...' after the list",
    "indented new paragraph", "follows \\end{enumerate} without a blank line (no indent)", "other",
    "\\end{enumerate}\nAlors $Z$", "\\end{enumerate}\n\nAlors $Z$",
    "Paragraph break after the list, as printed (GLOBAL_ISSUES 80).")
add(246, "Proposition (15.7.9): '(autrement dit (15.7.1) il existe'",
    "reference upright inside the italic statement (crop p246_autrement.png)", "italic", "convention",
    r"(15.7.1)", r"\textup{(15.7.1)}",
    "'autrement dit' is italic in the print here; only the reference is upright.", convention=6)
add(246, "proof of (15.7.9), l. 1: 'Utilisant la méthode de (8.1.2, a))'",
    "label a) italic", "plain upright 'a)'", "italics",
    r"(8.1.2, a))", r"(8.1.2, \emph{a)})")
add(246, "proof of (15.7.9), l. 11: 'propre sur k(y), il résulte de (III, 5.5.2)'",
    "bold italic k", "\\mathbf k(y)", "convention",
    r"propre sur $\mathbf k(y)$, il", r"propre sur $\boldsymbol{k}(y)$, il", convention=1)
add(246, "proof of (15.7.9), l. 13: 'telles que X_0 soit propre sur Y'",
    "'propre' italic (crop p246_X0propre.png)", "'propre' upright", "italics",
    r"$X_0$ soit propre sur", r"$X_0$ soit \emph{propre} sur")
add(246, "proof of (15.7.9), l. 22: 'aux deux seules conditions (i) et (iii)'",
    "'et' italic between the upright (i) and (iii) (crop p246_iet.png)", "'et' upright", "italics",
    r"conditions} (i) et (iii)", r"conditions} (i) \emph{et} (iii)")
add(246, "proof of (15.7.9), second line from the end: 'propre sur Spec(k(y)) puisque X est propre'",
    "bold italic k", "\\mathbf k(y)", "convention",
    r"$\operatorname{Spec}(\mathbf k(y))$ puisque", r"$\operatorname{Spec}(\boldsymbol{k}(y))$ puisque",
    convention=1)

# ---------------- page 247 ----------------
add(247, "Corollaire (15.7.10), l. 2: 'universellement submersif (15.7.8)'",
    "reference upright inside the italic statement", "italic (corollary environment)", "convention",
    r"submersif (15.7.8) et tel", r"submersif \textup{(15.7.8)} et tel", convention=6)
add(247, "Corollaire (15.7.10), l. 3: 'X_y soit propre sur k(y), f est propre au point y'",
    "bold italic k", "\\mathbf k(y)", "convention",
    r"sur $\mathbf k(y)$, $f$ est propre", r"sur $\boldsymbol{k}(y)$, $f$ est propre", convention=1)
add(247, "Corollaire (15.7.11), l. 3: 'qui soit en outre propre ou plat'",
    "'ou' upright between italic 'propre' and 'plat' (crop p247_ou.png)", "italic 'ou'", "convention",
    r"propre ou plat,", r"propre \textup{ou} plat,", convention=6)
add(247, "Corollaire (15.7.11), l. 4: 'Y-morphisme Y'→X (I, 3.3.14))'",
    "reference upright inside the italic statement (crop p247_ou.png)", "italic (corollary environment)",
    "convention", r"(\textbf{I}, 3.3.14)", r"\textup{(\textbf{I}, 3.3.14)}", convention=6)
add(247, "Corollaire (15.7.11), l. 4: 'Supposons enfin que les fibres X_y=f^{-1}(y)'",
    "the subscript y of X_y is a heavy (bold italic) y: largest stroke radius 3.6 px against 2.2-2.8 px, ink "
    "193 px (left edge clipped) against 135-167 px for the subscript y of X_y on the next line, of Spec(O_y) and "
    "of the X_y of (15.7.10) (crops p247_Xy_bold.png, p247_Xy_normal.png, y_compare.png)",
    "$X_y$ (plain y)", "misprint_in_print",
    r"enfin que les fibres $X_y=", r"enfin que les fibres $X_{\boldsymbol{y}}=",
    "Wrong-fount letter if confirmed (GLOBAL_ISSUES 29; same case as IV-2 p. 164): the TeX silently corrects, "
    "the fix restores the printed bold y. Low confidence: subscript weights vary on this page (O_y is "
    "heavier than the light y of the next line); skip if doubtful founts are not reproduced.",
    confidence="low", corrected=r"$X_y=f^{-1}(y)$")
add(247, "Corollaire (15.7.11), l. 5: 'tels que X_y soit propre sur k(y) est ouvert dans Y'",
    "bold italic k", "\\mathbf k(y)", "convention",
    r"$\mathbf k(y)$ est ouvert", r"$\boldsymbol{k}(y)$ est ouvert", convention=1)
add(247, "proof of (15.7.11), l. 11: 'f^{-1}(y) est propre sur k(y) ou que'",
    "bold italic k", "\\mathbf k(y)", "convention",
    r"$\mathbf k(y)$ ou que", r"$\boldsymbol{k}(y)$ ou que", convention=1)
add(247, "proof of (15.7.11), l. 11: 'f_0^{-1}(y_0) est propre sur k(y_0)'",
    "bold italic k", "\\mathbf k(y_0)", "convention",
    r"$\mathbf k(y_0)$", r"$\boldsymbol{k}(y_0)$", convention=1)
add(247, "Lemme (15.7.11.1), l. 2: 'qui est en outre propre ou plat et quasi-compact'",
    "'ou' upright (crop p247_lemma.png)", "italic 'ou'", "convention",
    r"propre ou plat et", r"propre \textup{ou} plat et", convention=6)
add(247, "Lemme (15.7.11.1), l. 3: 'si f' est submersif (resp. universellement submersif)'",
    "'(resp.' and the closing parenthesis upright, 'universellement submersif' italic (crop p247_lemma.png)",
    "all italic", "convention",
    r"(resp. universellement submersif)", r"\textup{(resp.} universellement submersif\textup{)}",
    "Same form as the IV-3 p. 14 page fixes.", convention=6)
add(247, "proof of (15.7.11.1), l. 4: 'f_1'=(f')_(Y_1) : X_1'→Y_1''",
    "(f')_(Y_1): subscript Y_1 without prime (crops p247_fY1.png, p247_fY1b.png)", "(f')_{(Y_1')}",
    "formula", r"(f')_{(Y_1')}", r"(f')_{(Y_1)}",
    "Not a misprint: f' is also a Y-morphism and X'×_Y Y_1 = X'×_{Y'}Y_1', so (f')_(Y_1) is X_1'→Y_1'. "
    "The TeX changed the printed subscript.")

# ---------------- page 248 ----------------
add(248, "proof of (15.7.11.1), l. 3: 'E est fermé dans Y, ce qui prouve le lemme'",
    "the E at the start of the line is a bold roman E: about 30 % more ink than the three other E on the page "
    "(489 px against 368-382 px), arms and serifs twice as thick (crops p248_E.png, E_compare3.png)",
    "$E$", "misprint_in_print",
    r"$E$ est fermé dans $Y$", r"$\mathbf{E}$ est fermé dans $Y$",
    "Wrong-fount letter (GLOBAL_ISSUES 29): the TeX silently corrects; the fix restores the printed bold E.",
    confidence="medium", corrected=r"$E$")

# ---------------- page 249 ----------------
add(249, "heading 'BIBLIOGRAPHIE (suite)'",
    "'(suite)' italic with italic parentheses, light weight (crop p249_heading.png)",
    "(\\emph{suite}): upright parentheses", "italics",
    r"(\emph{suite})", r"\textnormal{\emph{(suite)}}",
    "Same form as the IV-2 heading (ega4-2-fr.tex, IV-2 p. 224); the weight of 'BIBLIOGRAPHIE' belongs to the "
    "document-wide heading format.", confidence="medium")
add(249, "[40]: 'Groupes proalgébriques'",
    "title roman (article title; the journal name is italic) (crop p249_refs.png)",
    "\\emph{Groupes proalgébriques}", "italics",
    r"\emph{Groupes proalgébriques}", r"Groupes proalgébriques",
    "Titles of articles roman, journal names italic, as in the other bibliographies (IV-2 p. 224); the book "
    "title 'Corps locaux' of [39] is italic, as in the TeX.")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
print("wrote", len(L), "findings to", OUT)

# ---- validation: each old occurs exactly once (LF text), and sequential application works ----
ok = True
texts = {n: (RUN / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(245, 250)}
work = dict(texts)
for i, d in enumerate(L):
    if d["fix"] is None:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    c = texts[d["page"]].count(old)
    if c != 1:
        ok = False
        print("NOT UNIQUE/ABSENT", i, d["page"], repr(old), c)
    if work[d["page"]].count(old) != 1:
        ok = False
        print("SEQUENTIAL PROBLEM", i, d["page"], repr(old))
    work[d["page"]] = work[d["page"]].replace(old, new, 1)
print("all olds unique:", ok)
cnt = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for n in range(245, 250):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
for n in range(245, 250):
    (RUN / "crops_245_249" / f"applied_{n}.tex").write_text(work[n], encoding="utf-8", newline="\n")
