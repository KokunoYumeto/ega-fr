"""Build findings_175_179.json and check every fix's 'old' occurs exactly once."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_175_179.json"

L6 = "GLOBAL_ISSUES 16."


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def labels(page, stmt, n_labels, old, new, env):
    names = ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)"][:n_labels]
    out = [F(page, f"{stmt}, label (i)", "label '(i)' upright",
             f"\\begin{{enumerate}}[label=(\\roman*)] inside the italic {env} environment: italic label",
             "convention", 6, "high", old, new,
             f"One edit of the label option covers {', '.join(names)} (next entries). " + L6)]
    for nm in names[1:]:
        out.append(F(page, f"{stmt}, label {nm}", f"label '{nm}' upright", "italic (same enumerate)",
                     "convention", 6, "high", None, None,
                     "Covered by the previous edit (label=\\textup{(\\roman*)})."))
    return out


findings = []

# ---------------- page 175 ----------------
findings += [
    F(175, "proof of (12.1.1), cases (i)-(iii): 'entraîne que t est F-régulier (0_I, 6.3.4)'",
      "'régulier' italic (enlarged crop p175_freg.png)", "upright", "italics", None, "high",
      "est $\\mathcal F$-régulier", "est $\\mathcal F$-\\emph{régulier}"),
    F(175, "(12.1.1.3): 'K = k(y')'", "bold italic k", "plain k", "convention", 1, "high",
      "$K=k(y')$", "$K=\\boldsymbol{k}(y')$"),
    F(175, "(12.1.1.3): 'ou de dire que F' est réduit (resp. intègre) aux points de X⊗_A K''",
      "'réduit' and 'intègre' italic (enlarged crop p175_reduit1.png)", "both upright", "italics", None, "high",
      "$\\mathcal F'$ est réduit (resp. intègre)", "$\\mathcal F'$ est \\emph{réduit} (resp. \\emph{intègre})"),
    F(175, "(12.1.1.3): 'on peut se borner à prouver que F_{f(x')} est réduit'",
      "F_{f(x')}: script F with the subscript f(x') (enlarged crop p175_ffx.png)", "$\\mathcal F$ without subscript",
      "formula", None, "high",
      "prouver que\n$\\mathcal F$ est", "prouver que\n$\\mathcal F_{f(x')}$ est",
      "Independent of the next entry (no overlap)."),
    F(175, "(12.1.1.3): '... est réduit (resp. intègre) en toute générisation x' de x'",
      "'réduit' and 'intègre' italic (enlarged crop p175_ffx.png)", "both upright", "italics", None, "high",
      "réduit (resp. intègre) en toute", "\\emph{réduit} (resp. \\emph{intègre}) en toute"),
    F(175, "(12.1.1.3): 'l'uniformisante t de A étant un élément M-régulier'",
      "'régulier' italic (enlarged crop p175_Mreg.png)", "upright", "italics", None, "high",
      "élément $M$-régulier", "élément $M$-\\emph{régulier}"),
]

# ---------------- page 176 ----------------
findings += [
    F(176, "Proposition (12.1.1.5): 'F un O_X-Module cohérent et f-plat; pour tout y∈Y'",
      "'plat' printed roman inside the italic statement (enlarged crop p176_stmt1.png)", "italic (proposition environment)",
      "convention", 6, "high", "$f$-plat~; pour tout", "$f$-\\textup{plat}~; pour tout"),
    F(176, "Proposition (12.1.1.5): 'posons F_y = F⊗_{O_Y} k(y)'", "bold italic k", "plain k",
      "convention", 1, "high", "\\otimes_{\\mathcal O_Y}k(y)", "\\otimes_{\\mathcal O_Y}\\boldsymbol{k}(y)"),
    F(176, "Proposition (12.1.1.5): 'Soient Z' (resp. Y') le sous-préschéma réduit'",
      "'(resp. Y')' printed roman inside the italic statement (enlarged crop p176_stmt2.png)", "italic",
      "convention", 6, "high", "(resp. $Y'$)", "\\textup{(resp. $Y'$)}"),
    F(176, "Proposition (12.1.1.5): 'réduit de X (resp. Y) ayant pour espace sous-jacent'",
      "'(resp. Y)' printed roman (enlarged crop p176_stmt2.png)", "italic",
      "convention", 6, "high", "(resp. $Y$)", "\\textup{(resp. $Y$)}"),
    F(176, "Proposition (12.1.1.5): 'dans X (resp. de {y'} dans Y).'",
      "'(resp.' and the closing parenthesis roman, 'de ... dans' italic (enlarged crop p176_stmt2.png)", "all italic",
      "convention", 6, "high", "(resp. de $\\{y'\\}$\ndans $Y$).", "\\textup{(resp.} de $\\{y'\\}$\ndans $Y$\\textup{)}."),
    F(176, "Proposition (12.1.1.5): '(ce que nous exprimerons plus tard (13.2.2) en disant que la restriction Z'→Y' de f est un morphisme équidimensionnel)'",
      "the whole parenthesis printed roman, with 'équidimensionnel' italic (enlarged crop p176_stmt3.png)",
      "italic throughout (proposition environment), no emphasis on 'équidimensionnel'",
      "convention", 6, "high",
      "(ce que nous exprimerons plus tard\n(13.2.2) en disant que la restriction $Z'\\to Y'$ de $f$ est un morphisme\néquidimensionnel)",
      "\\textup{(ce que nous exprimerons plus tard\n(13.2.2) en disant que la restriction $Z'\\to Y'$ de $f$ est un morphisme\n\\emph{équidimensionnel})}"),
    F(176, "proof, reduction to a discrete valuation ring: 'Si Z'_1 = Z'_{y'}⊗_{k(y')} k(y'_1)', subscript",
      "bold upright k in the subscript of ⊗ (enlarged crop p176_k.png)", "plain k",
      "convention", 1, "high", "\\otimes_{k(y')}", "\\otimes_{\\mathbf{k}(y')}",
      "Subscript k bold upright (GLOBAL_ISSUES 48). Independent of the next entry (no overlap)."),
    F(176, "proof, reduction to a discrete valuation ring: 'Si Z'_1 = Z'_{y'}⊗_{k(y')} k(y'_1)', second k",
      "bold italic k (enlarged crop p176_k.png)", "plain k",
      "convention", 1, "high", "k(y'_1)", "\\boldsymbol{k}(y'_1)"),
    F(176, "proof: 'Alors g_1(z_1) est spécialisation de g_1(z) = z' dans X'",
      "'g_1(z)=z'' (plain z: enlarged crop p176_g1z.png)", "$g_1(z'_1)=z'$ (silent correction)",
      "misprint_in_print", None, "high", "de $g_1(z'_1)=z'$ dans", "de $g_1(z)=z'$ dans",
      "The print's g_1(z) is wrong: z is a point of X, not of X_1, and the argument needs g_1(z'_1)=z' (established two lines above: 'g_1(z'_1)=z''); z_1 specializes z'_1. The diplomatic text takes the printed reading.",
      corrected="de $g_1(z'_1)=z'$ dans"),
    F(176, "end of (12.1.1.5) proof, case (ii): 'Or on vient de voir que tout cycle premier'",
      "'tout' italic", "upright", "italics", None, "high",
      "de voir que tout\ncycle", "de voir que \\emph{tout}\ncycle"),
    F(176, "end of (12.1.1.5) proof, case (ii): 'a même dimension que l'un des cycles premiers'",
      "'l'un' italic", "upright", "italics", None, "high",
      "que l'un des cycles", "que \\emph{l'un} des cycles"),
    F(176, "Remarques (12.1.2) (i): '(de sorte que f est plat)'",
      "'plat' italic", "no \\emph (remark body judged as roman)", "italics", None, "high",
      "$f$ est plat),", "$f$ est \\emph{plat}),"),
    F(176, "Remarques (12.1.2) (i): 'ni même un morphisme ouvert.'",
      "'ouvert' italic", "no \\emph (remark body judged as roman)", "italics", None, "high",
      "un morphisme ouvert.", "un morphisme \\emph{ouvert}."),
]

# ---------------- page 177 ----------------
findings += [
    F(177, "Corollaire (12.1.3): 'Sous les hypothèses de (12.1.1), la fonction'",
      "'(12.1.1)' printed upright inside the italic statement (enlarged crop p177_c3a.png)", "italic",
      "convention", 6, "high", "hypothèses de (12.1.1), la", "hypothèses de \\textup{(12.1.1)}, la"),
    F(177, "Corollaire (12.1.3): 'la fonction x ⇝ coprof((F_{f(x)})_x)'",
      "wavy maps-to arrow (enlarged crop p177_c3a.png)", "\\mapsto", "symbol", None, "high",
      "$x\\mapsto\\operatorname{coprof}", "$x\\leadsto\\operatorname{coprof}",
      "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."),
    F(177, "Corollaire (12.1.3): 'la fonction x ⇝ prof*_x(F_{f(x)})'",
      "wavy maps-to arrow (enlarged crop p177_c3b.png)", "\\mapsto", "symbol", None, "high",
      "$x\\mapsto\\operatorname{prof}_x^*", "$x\\leadsto\\operatorname{prof}_x^*",
      "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."),
    F(177, "Corollaire (12.1.3): 'prof*_x(F_{f(x)}) (10.8.1) est semi-continue'",
      "'(10.8.1)' printed upright inside the italic statement (enlarged crop p177_c3b.png)", "italic",
      "convention", 6, "high", "(10.8.1) est", "\\textup{(10.8.1)} est"),
    F(177, "proof of (12.1.3): 'X = Spec(B) étant affine, F = M̃, où M est un B-module'",
      "the M under the tilde is heavier than the M of 'où M' beside it: 591 against 518 dark px, hairlines 3 px against 2, stems 6 px against 5 (enlarged crop p177_Mtilde.png)",
      "\\widetilde M", "font", None, "medium",
      "$\\mathcal F=\\widetilde M$, où $M$ est", "$\\mathcal F=\\widetilde{\\mathbf M}$, où $M$ est",
      "Same as p. 133 (findings_130_134, also noted there for p. 136): probably systematic for letters under a tilde. Decide once for the tilde letters (document-wide) before applying."),
    F(177, "Remarque (12.1.4): 'la fonction x ⇝ dim_x(X_{f(x)})'",
      "wavy maps-to arrow (enlarged crop p177_rem4.png)", "\\mapsto", "symbol", None, "high",
      "$x\\mapsto\\dim_x(X_{f(x)})$", "$x\\leadsto\\dim_x(X_{f(x)})$",
      "Wavy arrow (GLOBAL_ISSUES 33); not convention 3."),
    F(177, "Remarque (12.1.4): 'que cette propriété est vraie même sans supposer f plat.'",
      "'même sans supposer f plat' italic (enlarged crop p177_rem4.png)", "no \\emph (remark body judged as roman)",
      "italics", None, "high",
      "vraie même sans\nsupposer $f$ plat.", "vraie \\emph{même sans\nsupposer $f$ plat}."),
]
findings += labels(177, "Corollaire (12.1.5)", 2,
                   "Alors~:\n\\begin{enumerate}[label=(\\roman*)]",
                   "Alors~:\n\\begin{enumerate}[label=\\textup{(\\roman*)}]", "corollary")
findings += [
    F(177, "Corollaire (12.1.5) (ii): 'ou est un préschéma excellent (7.8.5), il existe'",
      "'(7.8.5)' printed upright inside the italic statement (enlarged crop p177_c5b.png)", "italic",
      "convention", 6, "high", "excellent (7.8.5)", "excellent \\textup{(7.8.5)}"),
]

# ---------------- page 178 ----------------
findings += [
    F(178, "Théorème (12.1.6): 'Soient f : X→Y un morphisme plat et localement de présentation finie'",
      "'plat' printed roman inside the italic statement (enlarged crop p178_plat.png)", "italic",
      "convention", 6, "high", "un morphisme plat et localement", "un morphisme \\textup{plat} et localement"),
]
findings += labels(178, "Théorème (12.1.6)", 4,
                   "ouvertes~:\n\\begin{enumerate}[label=(\\roman*)]",
                   "ouvertes~:\n\\begin{enumerate}[label=\\textup{(\\roman*)}]", "theorem")
findings += [
    F(178, "Théorème (12.1.6) (iii): 'géométriquement régulier (i.e. lisse) au point x'",
      "'(i.e.' and the closing parenthesis printed roman, 'lisse' italic (enlarged crop p178_iii.png)", "all italic",
      "convention", 6, "high", "régulier (i.e. lisse) au", "régulier \\textup{(i.e.} lisse\\textup{)} au"),
    F(178, "proof of (12.1.6), (ii): 'une extension finie quelconque K' de k(y')'",
      "bold italic k (enlarged crop p178_kref.png)", "plain k", "convention", 1, "high",
      "de $k(y')$, et tenant", "de $\\boldsymbol{k}(y')$, et tenant"),
]

# ---------------- page 179 ----------------
findings += [
    F(179, "Corollaire (12.1.7): 'l'une des propriétés suivantes (6.8.1) :'",
      "'(6.8.1)' printed upright inside the italic statement (enlarged crop p179_c7.png)", "italic",
      "convention", 6, "high", "(6.8.1)~:", "\\textup{(6.8.1)}~:"),
]
findings += labels(179, "Corollaire (12.1.7)", 6,
                   "\\begin{enumerate}[label=(\\roman*)]\n  \\item vérifier",
                   "\\begin{enumerate}[label=\\textup{(\\roman*)}]\n  \\item vérifier", "corollary")
findings += [
    F(179, "Corollaire (12.1.7) (iv): 'être régulier (ou lisse, ce qui revient au même);'",
      "'(ou' and ', ce qui revient au même)' printed roman, 'lisse' italic (enlarged crop p179_c7.png)", "all italic",
      "convention", 6, "high", "(ou lisse, ce qui revient au même)",
      "\\textup{(ou} lisse\\textup{, ce qui revient au même)}"),
    F(179, "proof of (12.1.7): 'l'ensemble des x∈X où f est plat est ouvert.'",
      "'plat' italic (enlarged crop p179_plat.png)", "upright", "italics", None, "high",
      "où $f$ est plat\n", "où $f$ est \\emph{plat}\n",
      "Independent of the next entry (no overlap)."),
    F(179, "proof of (12.1.7): '... est ouvert. On peut donc se borner'",
      "'ouvert' italic (enlarged crop p179_plat.png)", "upright", "italics", None, "high",
      "ouvert. On peut", "\\emph{ouvert}. On peut"),
    F(179, "heading 12.2: 'Propriétés locales et globales des fibres d'un morphisme propre, plat et de présentation finie.'",
      "final full stop", "no full stop", "punctuation", None, "high",
      "présentation finie}", "présentation finie.}",
      "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."),
    F(179, "Théorème (12.2.1): 'Soient f : X→Y un morphisme propre de présentation finie'",
      "'propre' printed italic like the rest of the statement (enlarged crop p179_propre.png)",
      "\\emph{propre} inside the italic theorem: upright", "convention", 6, "high",
      "\\emph{propre}", "propre",
      "The TeX adds an emphasis the print does not have (FIX_POLICY 2.6: drop \\emph where the print shows no change of face)."),
]
findings += labels(179, "Théorème (12.2.1)", 4,
                   "ouvertes~:\n\\begin{enumerate}[label=(\\roman*)]",
                   "ouvertes~:\n\\begin{enumerate}[label=\\textup{(\\roman*)}]", "theorem")

# ---------------- checks ----------------
ok = True
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    text = (RUN / f"page_{f['page']}.tex").read_text(encoding="utf-8")
    n = text.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/MISSING", f["page"], n, repr(fx["old"]))
# overlap check per page
for p in (175, 176, 177, 178, 179):
    text = (RUN / f"page_{p}.tex").read_text(encoding="utf-8")
    spans = []
    for f in findings:
        if f["page"] == p and f["fix"]:
            i = text.find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["where"][:50]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            ok = False
            print("OVERLAP", p, a, b)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(findings), "entries; checks", "OK" if ok else "FAILED")
from collections import Counter
c = Counter()
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in (175, 176, 177, 178, 179):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
