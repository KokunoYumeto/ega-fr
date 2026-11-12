# Builds findings_220_224.json and checks every fix's "old" against its page file.
import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
OUT = os.path.join(RUN, "findings_220_224.json")
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV3\native\ega4"

def nl(s):
    return None if s is None else s.replace("<NL>", "\n")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)

LBL = "Proof-part labels are printed upright (GLOBAL_ISSUES 51/76); the edit takes the label out of \\emph."
DASH = "ega4-14-fr.tex writes '--' after its five hand-made step headings I)-V) (all on pp. 220-222); the edition elsewhere has '---' for the printed long dash."

# ---------------- page 220 ----------------
add(220, "proof of (14.5.10), step heading 'I) Réduction au cas où Y est intègre.'",
    "'I)' upright; only 'Réduction au cas où' and 'est intègre' italic",
    "\\emph{I) Réduction ...}: the label comes out italic", "italics", None, "high",
    r"\emph{I) Réduction", r"I) \emph{Réduction", LBL)
add(220, "step I), dash after the heading: 'intègre. — Si l'on'",
    "long dash —", "'--' (en dash)", "punctuation", None, "high",
    r"intègre.} -- Si l'on", r"intègre.} --- Si l'on", DASH)
add(220, "step heading 'II) Caractère local sur Y.'",
    "'II)' upright; 'Caractère local sur' italic",
    "\\emph{II) Caractère ...}: the label comes out italic", "italics", None, "high",
    r"\emph{II) Caractère", r"II) \emph{Caractère", LBL)
add(220, "step II), dash after the heading: 'sur Y. — Nous allons'",
    "long dash —", "'--' (en dash)", "punctuation", None, "high",
    r"$Y$.} -- Nous allons", r"$Y$.} --- Nous allons", DASH)
add(220, "step II): 'Considérons le normalisé Y'' de Y dans K''",
    "'normalisé' italic", "upright", "italics", None, "high",
    r"Considérons le normalisé", r"Considérons le \emph{normalisé}")
add(220, "step II): 'pour tout j, A'_j=Γ(U'_j, O_{U'_j})=Γ(U_j, (g_j)_*(O_{U'_j})) s'identifie à'",
    "the formula is set in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[<NL>  A'_j=\Gamma(U'_j,\mathcal O_{U'_j})<NL>      =\Gamma(U_j,(g_j)_*(\mathcal O_{U'_j}))<NL>\]",
    r"$A'_j=\Gamma(U'_j,\mathcal O_{U'_j})<NL>=\Gamma(U_j,(g_j)_*(\mathcal O_{U'_j}))$",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting words lost.")
add(220, "step II): 'est une O_{U_j}-Algèbre cohérente, sous-Algèbre de B|U_j'",
    "'cohérente' italic", "upright", "italics", None, "high",
    r"Algèbre cohérente, sous-Algèbre", r"Algèbre \emph{cohérente}, sous-Algèbre")
add(220, "step II): 'Il existe donc un sous-O_Y-Module C'_j cohérent de B'",
    "'sous-O_Y-Module C'_j cohérent' italic", "upright", "italics", None, "high",
    r"un sous-$\mathcal O_Y$-Module $\mathcal C'_j$ cohérent de",
    r"un \emph{sous-$\mathcal O_Y$-Module $\mathcal C'_j$ cohérent} de")
add(220, "step II): 'engendrée par C' est cohérente puisque B est'",
    "'cohérente' italic", "upright", "italics", None, "high",
    r"est cohérente puisque", r"est \emph{cohérente} puisque")
add(220, "step heading 'III) Réduction au cas où Y est intègre, local et géométriquement unibranche.'",
    "'III)' upright", "\\emph{III) Réduction ...}: the label comes out italic", "italics", None, "high",
    r"\emph{III) Réduction", r"III) \emph{Réduction", LBL)
add(220, "step III), dash after the heading: 'unibranche. — Supposons'",
    "long dash —", "'--' (en dash)", "punctuation", None, "high",
    r"unibranche.} -- Supposons", r"unibranche.} --- Supposons", DASH)
add(220, "last line: '(avec s∈A—p,'",
    "long dash for the set difference A—p", "$s\\in A-\\mathfrak p$ (minus sign)", "convention", 7, "high",
    r"$s\in A-", r"$s\in A\setmin",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(220, "page break 220/221: '(avec s∈A—p, | z_i entiers sur A)'",
    "one sentence runs over the page break; p. 221 begins flush left with 'z_i entiers sur A)' (page_221_s1.png)",
    "blank lines before and after \\oldpage[IV-3]{221}: a paragraph break in mid-sentence", "marker", None, "high",
    r"\mathfrak p$,<NL><NL>", r"\mathfrak p$,<NL>",
    "Part 1 of 2 (blank line before the marker; GLOBAL_ISSUES 20); part 2 is the page-221 entry for the blank line after the marker. The marker itself is in the right place. Disjoint from the convention-7 edit on the same line.")

# ---------------- page 221 ----------------
add(221, "top of the page: '\\oldpage[IV-3]{221}' followed by a blank line",
    "'z_i entiers sur A), que l'on peut supposer' continues the sentence of p. 220, flush left",
    "blank line after the marker starts a new paragraph", "marker", None, "high",
    r"\oldpage[IV-3]{221}<NL><NL>$z_i$", r"\oldpage[IV-3]{221}<NL>$z_i$",
    "Part 2 of 2 (the page-220 entry removes the blank line before the marker); apply both.")
add(221, "step III): 'appliquant la méthode de (8.1.2, a)), on peut supposer'",
    "'a)' italic, its parenthesis included; the outer parenthesis upright (crop p221_a.png)",
    "$a)$: italic a, upright parenthesis", "italics", None, "high",
    r"(8.1.2, $a)$)", r"(8.1.2, \emph{a)})")
add(221, "step heading 'IV) Réduction au cas où X est intègre, affine, et f quasi-fini, surjectif, birationnel et universellement ouvert.'",
    "'IV)' upright", "\\emph{IV) Réduction ...}: the label comes out italic", "italics", None, "high",
    r"\emph{IV) Réduction", r"IV) \emph{Réduction", LBL)
add(221, "step IV), dash after the heading: 'ouvert. — Supposons donc'",
    "long dash —", "'--' (en dash)", "punctuation", None, "high",
    r"ouvert.} -- Supposons", r"ouvert.} --- Supposons", DASH)
add(221, "step IV): 'f_0 : X_0→Y de f soit un morphisme quasi-fini et dominant et que'",
    "'quasi-fini' and 'dominant' italic, 'et' roman", "upright", "italics", None, "high",
    r"morphisme quasi-fini et dominant et que", r"morphisme \emph{quasi-fini} et \emph{dominant} et que")
add(221, "step IV): 'supposer que X est intègre et f quasi-fini et dominant,'",
    "'quasi-fini' and 'dominant' italic, the 'et' between them roman (crop p221_qfd.png)",
    "\\emph{quasi-fini et dominant}: 'et' italic", "italics", None, "high",
    r"\emph{quasi-fini et dominant}", r"\emph{quasi-fini} et \emph{dominant}")
add(221, "step IV): 'contenant y est égal à Y, f est surjectif.'",
    "'surjectif' italic", "upright", "italics", None, "high",
    r"$f$ est surjectif.", r"$f$ est \emph{surjectif}.")
add(221, "step IV): 'k(ξ) est donc une extension finie'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"$k(\xi)$ est donc", r"$\boldsymbol{k}(\xi)$ est donc")
add(221, "step IV): 'de K=k(η)'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"$K=k(\eta)$", r"$K=\boldsymbol{k}(\eta)$")
add(221, "step IV): '(Spec(k(ξ)⊗_K K'))_red'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(\xi)\otimes_K K'))", r"\operatorname{Spec}(\boldsymbol{k}(\xi)\otimes_K K'))")
add(221, "step IV): '(Spec(k(ξ)⊗_K K'))_red soit géométriquement réduit sur K et que ses composantes'",
    "'sur K' without a prime (crop p221_surK.png)", "'sur $K$': keeps the printed reading", "misprint_in_print", None, "medium",
    None, None,
    "(4.6.8) gives (X_(k'))_red geometrically reduced over the extension k', and the next step applies (4.5.9) and (4.6.1) over K' ('extensions ... séparables de K''); over K the claim fails when K'/K is inseparable. Not in the authors' errata lists; the diplomatic TeX already keeps the print.",
    corrected=r"géométriquement réduit sur $K'$", nofix=True)
add(221, "step IV): 'les corps résiduels de Spec(k(ξ)⊗_K K') sont'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(\xi)\otimes_K K')$ sont", r"\operatorname{Spec}(\boldsymbol{k}(\xi)\otimes_K K')$ sont")
add(221, "step IV): 'f est alors un morphisme quasi-fini, surjectif et universellement ouvert;'",
    "'quasi-fini', 'surjectif' and 'universellement ouvert' italic, 'et' roman (crop p221_qse.png)",
    "one \\emph over the whole phrase: 'et' italic", "italics", None, "high",
    r"\emph{quasi-fini,<NL>surjectif et universellement ouvert}", r"\emph{quasi-fini,<NL>surjectif} et \emph{universellement ouvert}")
add(221, "page break 221/222: 'f_i(U) est donc | ouvert dans Y'",
    "one sentence runs over the page break; p. 222 begins flush left with 'ouvert dans Y' (page_222_s1.png)",
    "blank lines before and after \\oldpage[IV-3]{222}: a paragraph break in mid-sentence", "marker", None, "high",
    r"$f_i(U)$ est donc<NL><NL>", r"$f_i(U)$ est donc<NL>",
    "Part 1 of 2 (blank line before the marker; GLOBAL_ISSUES 20); part 2 is the page-222 entry. The marker itself is in the right place.")

# ---------------- page 222 ----------------
add(222, "top of the page: '\\oldpage[IV-3]{222}' followed by a blank line",
    "'ouvert dans Y et contient y' continues the sentence of p. 221, flush left",
    "blank line after the marker starts a new paragraph", "marker", None, "high",
    r"\oldpage[IV-3]{222}<NL><NL>ouvert dans", r"\oldpage[IV-3]{222}<NL>ouvert dans",
    "Part 2 of 2 (the page-221 entry removes the blank line before the marker); apply both.")
add(222, "step heading 'V) Fin de la démonstration.'",
    "'V)' upright", "\\emph{V) Fin ...}: the label comes out italic", "italics", None, "high",
    r"\emph{V) Fin", r"V) \emph{Fin", LBL)
add(222, "step V), dash after the heading: 'démonstration. — Nous supposons'",
    "long dash —", "'--' (en dash)", "punctuation", None, "high",
    r"démonstration.} -- Nous", r"démonstration.} --- Nous", DASH)
add(222, "proof of (14.5.11): 'il existe un morphisme fini surjectif h : Y_1→Y'",
    "'fini surjectif' italic (crop p222_finisurj.png)", "upright", "italics", None, "high",
    r"morphisme fini surjectif $h:Y_1\to Y$", r"morphisme \emph{fini surjectif} $h:Y_1\to Y$")
add(222, "proof of (14.5.11): 'il existe une Y-section s de Y''",
    "'section' italic (crop p222_Ysection.png)", "upright", "italics", None, "high",
    r"$Y$-section $s$ de $Y'$", r"$Y$-\emph{section} $s$ de $Y'$")

# ---------------- page 223 ----------------
add(223, "proof of Lemme (14.5.11.1): diagram at the top of the page",
    "all four horizontal arrows point to the right: X -p_1-> X×_S Y -s'-> X over S --> Y -s-> S (crop p223_diagram.png)",
    "\\ar[r] throughout: keeps the printed reading", "misprint_in_print", None, "high",
    None, None,
    "p_1 : X×_S Y→X, s' : X→X×_S Y and s : S→Y need leftward arrows, as in the diagram of (I, 3.3.11) that this one replaces. The authors' errata (ega4-errata-addenda-list3-fr.tex, item (IV, 14.5.11)) say: 'les flèches horizontales doivent toutes aller de droite à gauche'.",
    corrected=r"\xymatrix{<NL>    X \ar[d]_{f} & X\times_S Y \ar[l]_{p_1} \ar[d]^{p_2} & X \ar[l]_{s'} \ar[d]^{f} \\<NL>    S & Y \ar[l] & S \ar[l]^{s}<NL>  }",
    nofix=True)
add(223, "after the diagram: 'Appliquant ce lemme en y remplaçant S, Y par Y, Y'...'",
    "the line starts flush left (no indent): the paragraph runs on after the display",
    "\\end{proof} and a blank line: 'Appliquant' starts a new indented paragraph", "other", None, "medium",
    r"\end{proof}<NL><NL>Appliquant", r"\end{proof}<NL>\noindent Appliquant",
    "Paragraph structure only (as the IV-3 p. 120 fix).")
add(223, "Corollaire (14.5.12), l. 1: 'hypothèses générales de (14.5.11), soit L'",
    "(14.5.11) upright inside the italic statement (crop p223_cor_l12.png)", "italic (corollary environment)",
    "convention", 6, "high",
    r"générales de (14.5.11), soit", r"générales de \textup{(14.5.11)}, soit")
add(223, "Corollaire (14.5.12): 'propre sur Y (II, 5.4.10)'",
    "reference upright, bold upright II", "italic (corollary environment)", "convention", 6, "high",
    r"(\textbf{II}, 5.4.10)", r"\textup{(\textbf{II}, 5.4.10)}")
add(223, "Corollaire (14.5.12): 'sur l'ouvert X—Z soit normal'",
    "long dash for the set difference X—Z", "$X-Z$ (minus sign)", "convention", 7, "high",
    r"$X-Z$", r"$X\setmin Z$",
    "\\setmin pending the convention-7 decision (FIX_POLICY 2.7).")
add(223, "subsection heading 15.1",
    "'15.1. Multiplicités des fibres d'un morphisme universellement ouvert.' (final full stop)",
    "\\subsection{...} without the full stop", "punctuation", None, "high",
    r"\subsection{Multiplicités des fibres d'un morphisme universellement ouvert}",
    r"\subsection{Multiplicités des fibres d'un morphisme universellement ouvert.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(223, "Proposition (15.1.1): 'on pose F_y=F⊗_{O_Y}k(y)'",
    "bold italic k (crop p223_prop_l3.png)", "\\mathbf{k} (bold upright)", "convention", 1, "high",
    r"\otimes_{\mathcal O_Y}\mathbf{k}(y)", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)",
    "Outside subscripts the residue-field k is bold italic (GLOBAL_ISSUES 48).")
add(223, "Proposition (15.1.1): '(faisceau de modules sur la fibre f^{-1}(y))'",
    "the whole parenthesis roman inside the italic statement (crop p223_prop_l3.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"(faisceau de modules<NL>sur la fibre $f^{-1}(y)$)", r"\textup{(faisceau de modules<NL>sur la fibre $f^{-1}(y)$)}")
add(223, "Proposition (15.1.1): 'Si λ_x(F_y) (resp. λ_t(F_η)) désigne'",
    "'resp.' roman (crop p223_prop_resp.png)", "italic (proposition environment)", "convention", 6, "high",
    r"(resp. $\lambda_t", r"(\textup{resp.} $\lambda_t")
add(223, "Proposition (15.1.1): '(resp. celle de F_η en un point t∈f^{-1}(η))'",
    "'resp.' roman, 'celle de ... en un point' italic", "italic (proposition environment)", "convention", 6, "high",
    r"(resp. celle de", r"(\textup{resp.} celle de")
add(223, "Proposition (15.1.1): '(4.7.5), on a'",
    "reference upright inside the italic statement", "italic (proposition environment)", "convention", 6, "high",
    r"(4.7.5), on a", r"\textup{(4.7.5)}, on a")
add(223, "page break 223/224: end of Proposition (15.1.1) / proof 'Les fibres f^{-1}(y') de f ...'",
    "p. 223 ends with the display (15.1.1.2); p. 224 opens with the proof (no heading in the print)",
    "\\begin{proof} stands before \\oldpage[IV-3]{224}, in p. 223's segment", "marker", None, "medium",
    r"\end{proposition}<NL><NL>\begin{proof}<NL>", r"\end{proposition}<NL><NL>\oldpage[IV-3]{224}<NL>\begin{proof}<NL>",
    "Part 1 of 2: apply together with the page-224 entry that removes the old marker (same pattern as the IV-3 pp. 28/29 fix).")

# ---------------- page 224 ----------------
add(224, "top of the page: marker after \\begin{proof}",
    "p. 224 opens with the proof of (15.1.1)", "\\oldpage[IV-3]{224} after \\begin{proof}", "marker", None, "medium",
    r"\oldpage[IV-3]{224}<NL>Les fibres", r"Les fibres",
    "Part 2 of 2: the page-223 entry inserts the marker before \\begin{proof}; apply both or neither.")
add(224, "proof of (15.1.1): 'on posera K=k(η)'",
    "bold italic k (crop p224_Keta.png)", "\\mathbf{k} (bold upright)", "convention", 1, "high",
    r"$K=\mathbf{k}(\eta)$", r"$K=\boldsymbol{k}(\eta)$",
    "Outside subscripts the residue-field k is bold italic (GLOBAL_ISSUES 48).")
add(224, "proof of (15.1.1): 'le morphisme Spec(k(y')) → Spec(k(y))', first k",
    "bold italic k (crop p224_kspec.png)", "\\mathbf{k} (bold upright)", "convention", 1, "high",
    r"\mathbf{k}(y'))\to", r"\boldsymbol{k}(y'))\to")
add(224, "proof of (15.1.1): 'le morphisme Spec(k(y')) → Spec(k(y))', second k",
    "bold italic k (crop p224_kspec.png)", "\\mathbf{k} (bold upright)", "convention", 1, "high",
    r"\mathbf{k}(y))$ étant", r"\boldsymbol{k}(y))$ étant")
add(224, "proof of (15.1.1): 'Par construction, on a k(η')=K''",
    "bold italic k", "\\mathbf{k} (bold upright)", "convention", 1, "high",
    r"$\mathbf{k}(\eta')=K'$", r"$\boldsymbol{k}(\eta')=K'$")

# ---------------- page 225 (marker of the 224/225 break) ----------------
add(225, "page break 224/225: 'Posons S=Spec(A), ... si m est l'idéal maximal de A, on a donc par définition | P=Proj(B), où B est'",
    "p. 224 ends with 'on a donc par définition' (page_224_s4.png); p. 225 begins with 'P=Proj(B), où B est la A-algèbre graduée' (page_225_s1.png)",
    "\\oldpage[IV-3]{225} stands before 'Posons', three printed lines too early", "marker", None, "high",
    r"\oldpage[IV-3]{225}<NL>Posons", r"Posons",
    "Part 1 of 2 (removes the marker); part 2 inserts it before '$P=\\operatorname{Proj}(B)$'. Both olds lie in page_225.tex (ega4-15-fr.tex, after line 112). The three lines 'Posons ... par définition' were compared with p. 224: no other difference.")
add(225, "page break 224/225: insertion point of the marker",
    "p. 225 begins with 'P=Proj(B)'", "no marker there", "marker", None, "high",
    r"par définition<NL>$P=\operatorname{Proj}(B)$", r"par définition<NL>\oldpage[IV-3]{225}<NL>$P=\operatorname{Proj}(B)$",
    "Part 2 of 2: apply together with the previous entry.")

# ---------------- checks ----------------
def load(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")

pages = {}
ok = True
for d in F:
    if d["fix"] is None:
        continue
    p = d["page"]
    if p not in pages:
        pages[p] = load(os.path.join(RUN, "page_%03d.tex" % p))
    t = pages[p]
    old, new = d["fix"]["old"], d["fix"]["new"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("NOT UNIQUE/ABSENT", p, n, repr(old))
    if old == new:
        ok = False
        print("NO-OP", p, repr(old))

# overlap check: apply all fixes of a page sequentially, in order, then in reverse order
for p in sorted(pages):
    fx = [d["fix"] for d in F if d["page"] == p and d["fix"]]
    for order in (fx, list(reversed(fx))):
        t = pages[p]
        for f in order:
            if t.count(f["old"]) != 1:
                ok = False
                print("SEQUENCE CONFLICT", p, repr(f["old"]))
            t = t.replace(f["old"], f["new"], 1)

# the olds must also exist in the release source files
srcs = {}
for name in ("ega4-14-fr.tex", "ega4-15-fr.tex"):
    srcs[name] = load(os.path.join(SRC, name))
for d in F:
    if d["fix"] is None:
        continue
    c = sum(s.count(d["fix"]["old"]) for s in srcs.values())
    if c < 1:
        ok = False
        print("NOT IN SOURCE", d["page"], repr(d["fix"]["old"]))
    elif c > 1:
        print("note: %d copies in source files for page %d: %r" % (c, d["page"], d["fix"]["old"][:60]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "OK" if ok else "PROBLEMS")
