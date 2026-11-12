"""Build findings_070_074.json for EGA IV-3 pp. 70-74 and check every fix.

<NL> in the strings below stands for a line break (LF).
"""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_070_074.json"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


SETMIN = "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."
SUB = "Long dash used for a subtraction (GLOBAL_ISSUES 23); " + SETMIN
GI20 = "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20)."

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 69 (end of page; needed by the p. 70 top fix) ----------------
add(69, "end of p. 69: 'remplaçant f par f_red, qui est de type fini (1.5.4, (vii)), on peut' | p. 70 'supposer A intègre'",
    "the sentence runs on over the page break; p. 70 begins 'supposer A intègre ...' flush left",
    "blank line before \\oldpage[IV-3]{70} (last line of the p. 69 segment)",
    "other", None, "high",
    r"type fini (1.5.4, (vii)), on peut<NL><NL>", r"type fini (1.5.4, (vii)), on peut<NL>",
    GI20 + " Outside pages 70-74 (end of page_069.tex); listed because the p. 70 top fix needs it. Apply together "
    "with the p. 70 top entry; drop it if the pp. 65-69 batch already has the same edit.")

# ---------------- page 70 ----------------
add(70, "top of page: 'supposer A intègre et X réduit' continues the sentence '... on peut' of p. 69",
    "first line continues the sentence of p. 69, flush left (no new paragraph)",
    "\\oldpage[IV-3]{70} followed by a blank line (and preceded by one at the end of p. 69)",
    "other", None, "high",
    r"\oldpage[IV-3]{70}<NL><NL>supposer $A$", r"\oldpage[IV-3]{70}<NL>supposer $A$",
    GI20 + " Apply together with the p. 69 entry (blank line before the marker).")
add(70, "l. 2: 'un k(η)-morphisme fini et surjectif'",
    "'fini' and 'surjectif' italic, 'et' roman (crop p70_s1_fini_et.png)",
    "\\emph{fini et surjectif} ('et' italic too)",
    "italics", None, "high",
    r"\emph{fini et surjectif}", r"\emph{fini} et \emph{surjectif}")
add(70, "l. 2: 'un k(η)-morphisme'", "bold italic k", "$k(\\eta)$", "convention", 1, "high",
    r"$k(\eta)$-morphisme", r"$\boldsymbol{k}(\eta)$-morphisme")
add(70, "l. 3: 'h : W→V((k(η))^n)'", "bold italic k", "(k(\\eta))^n", "convention", 1, "high",
    r"\mathbf V((k(\eta))^n)", r"\mathbf V((\boldsymbol{k}(\eta))^n)")
add(70, "l. 3: 'B'=k(η)[T_1, ..., T_n]'", "bold italic k", "B'=k(\\eta)", "convention", 1, "high",
    r"$B'=k(\eta)[T_1", r"$B'=\boldsymbol{k}(\eta)[T_1")
add(70, "'C_η=C⊗_A k(η) est donc un module'", "bold italic k (crop p70_s2_sinS.png shows the same k in C⊗_A k(s))",
    "C\\otimes_A k(\\eta)", "convention", 1, "high",
    r"$C_\eta=C\otimes_A k(\eta)$", r"$C_\eta=C\otimes_A \boldsymbol{k}(\eta)$")
add(70, "'B_η=B'=B⊗_A k(η)=k(η)[T_1, ..., T_n]'", "bold italic k, 2 times", "k(\\eta) twice", "convention", 1, "high",
    r"B\otimes_A k(\eta)=k(\eta)[T_1", r"B\otimes_A \boldsymbol{k}(\eta)=\boldsymbol{k}(\eta)[T_1")
add(70, "'dont les dénominateurs sont dans A—{0}⊂B—{0}'", "long dash for the set difference, 2 times",
    "minus signs", "convention", 7, "high",
    r"$A-\{0\}\subset B-\{0\}$", r"$A\setmin\{0\}\subset B\setmin\{0\}$", SETMIN)
add(70, "proof of (9.5.6): 'il y a un voisinage U de η dans S tel que pour s∈S, C_s=C⊗_A k(s) soit ... sans torsion'",
    "s∈S (crop p70_s2_sinS.png)", "$s\\in S$ (keeps the print)",
    "misprint_in_print", None, "medium", None, None,
    "The neighbourhood U just obtained from (9.4.8) is where C_s is torsion-free; with 's∈S' the U is never used. "
    "The TeX keeps the printed S (also in the r20 corrected edition); the corrected edition should read s∈U.",
    corrected=r"$s\in U$")
add(70, "'C_s=C⊗_A k(s) soit un module'", "bold italic k (crop p70_s2_sinS.png)", "C\\otimes_A k(s)",
    "convention", 1, "high",
    r"$C_s=C\otimes_A k(s)$", r"$C_s=C\otimes_A \boldsymbol{k}(s)$")
add(70, "'sur B_s=B⊗_A k(s)=k(s)[T_1, ..., T_n]'", "bold italic k, 2 times", "k(s) twice", "convention", 1, "high",
    r"B\otimes_A k(s)=k(s)[T_1", r"B\otimes_A \boldsymbol{k}(s)=\boldsymbol{k}(s)[T_1")
add(70, "Remarque (9.5.7): 'on a donc k(η)=K=k(T)'", "first k bold italic (residue field); k(T) plain italic",
    "$k(\\eta)=K=k(T)$", "convention", 1, "high",
    r"$k(\eta)=K=k(T)$", r"$\boldsymbol{k}(\eta)=K=k(T)$")
add(70, "Remarque (9.5.7): 'B_s=B/j_sB est composée directe de [L : K] corps'",
    "'composée directe' (crop p70_s3_composee.png)", "composé direct",
    "word", None, "high",
    r"est composé direct de", r"est composée directe de",
    "The feminine form (agreeing with an implied 'algèbre') is not an evident misprint; the TeX normalised it.")
add(70, "Remarque (9.5.7): 'tout idéal maximal de k[T] est de la forme (T—α)'", "long dash for the subtraction T—α",
    "(T-\\alpha)", "convention", 7, "high",
    r"forme $(T-\alpha)$ avec", r"forme $(T\setmin\alpha)$ avec", SUB)
add(70, "Remarque (9.5.7): 'au-dessus de l'idéal (T—α) est l'idéal principal'", "long dash for the subtraction T—α",
    "(T-\\alpha)", "convention", 7, "high",
    r"l'idéal $(T-\alpha)$ est", r"l'idéal $(T\setmin\alpha)$ est", SUB)
add(70, "Remarque (9.5.7): 'l'idéal principal (T^{1/p}—α^{1/p})'", "long dash for the subtraction",
    "(T^{1/p}-\\alpha^{1/p})", "convention", 7, "high",
    r"$(T^{1/p}-\alpha^{1/p})$", r"$(T^{1/p}\setmin\alpha^{1/p})$", SUB)
add(70, "end of page: '... (T^{1/p}—α^{1/p}) et il est immédiat' | p. 71 'que l'anneau quotient'",
    "the sentence runs on over the page break; p. 71 begins 'que l'anneau quotient ...' flush left",
    "blank line before \\oldpage[IV-3]{71} (and after it)",
    "other", None, "high",
    r"et il est immédiat<NL><NL>", r"et il est immédiat<NL>",
    GI20 + " Apply together with the p. 71 top entry.")

# ---------------- page 71 ----------------
add(71, "top of page: 'que l'anneau quotient B/(T—α)B admet ...' continues the sentence of p. 70",
    "first line continues the sentence, flush left",
    "\\oldpage[IV-3]{71} followed by a blank line",
    "other", None, "high",
    r"\oldpage[IV-3]{71}<NL><NL>que l'anneau", r"\oldpage[IV-3]{71}<NL>que l'anneau",
    GI20 + " Apply together with the p. 70 end entry ('et il est immédiat').")
add(71, "l. 1: 'l'anneau quotient B/(T—α)B'", "long dash for the subtraction T—α", "B/(T-\\alpha)B",
    "convention", 7, "high",
    r"$B/(T-\alpha)B$", r"$B/(T\setmin\alpha)B$", SUB)
add(71, "subsection heading 9.6", "'9.6. Constructibilité de certaines propriétés des morphismes.' (final full stop)",
    "\\subsection{... des morphismes} (no full stop)", "punctuation", None, "high",
    r"\subsection{Constructibilité de certaines propriétés des morphismes}",
    r"\subsection{Constructibilité de certaines propriétés des morphismes.}",
    "GLOBAL_ISSUES 43/58: subsection titles lack the printed full stop.")
add(71, "Proposition (9.6.1), labels (i)-(xii)", "the twelve labels (i) ... (xii) upright",
    "enumerate [label=(\\roman*)] inside the italic proposition: labels italic",
    "convention", 6, "high",
    r"[label=(\roman*),widest=xii]", r"[label=\textup{(\roman*)},widest=xii]",
    "GLOBAL_ISSUES 16; one edit covers all twelve labels.")
add(71, "proof of (9.6.1) (iv): 'on doit prouver que E ou S—E est un voisinage de η'", "long dash for the set difference",
    "$S-E$", "convention", 7, "high",
    r"$E$ ou $S-E$ est", r"$E$ ou $S\setmin E$ est", SETMIN)
add(71, "end of page: 'qu'en remplaçant S par un voisinage de η, on peut' | p. 72 'supposer que f est lui-même'",
    "the sentence runs on over the page break; p. 72 begins 'supposer que f ...' flush left",
    "blank line before \\oldpage[IV-3]{72} (and after it)",
    "other", None, "high",
    r"de $\eta$, on peut<NL><NL>", r"de $\eta$, on peut<NL>",
    GI20 + " Apply together with the p. 72 top entry.")

# ---------------- page 72 ----------------
add(72, "top of page: 'supposer que f est lui-même un morphisme propre' continues the sentence of p. 71",
    "first line continues the sentence, flush left",
    "\\oldpage[IV-3]{72} followed by a blank line",
    "other", None, "high",
    r"\oldpage[IV-3]{72}<NL><NL>supposer que", r"\oldpage[IV-3]{72}<NL>supposer que",
    GI20 + " Apply together with the p. 71 end entry ('de $\\eta$, on peut').")
add(72, "(iv): 'Supposons au contraire que η∈S—E, et distinguons deux cas'", "long dash for the set difference",
    "$S-E$", "convention", 7, "high",
    r"contraire que $\eta\in S-E$", r"contraire que $\eta\in S\setmin E$", SETMIN)
add(72, "(iv) 2°: 'tel que Z soit isomorphe à Y'_η et que g_η=h;'",
    "no comma after Y'_η (crop p72_s2_isomorphe2.png)", "$Y'_\\eta$, et que",
    "punctuation", None, "high",
    r"$Y'_\eta$, et que $g_\eta=h$", r"$Y'_\eta$ et que $g_\eta=h$")
add(72, "(ix): 'et à prouver que E ou S—E est un voisinage de η'", "long dash for the set difference",
    "$S-E$", "convention", 7, "high",
    r"générique $\eta$, et à prouver que $E$ ou $S-E$", r"générique $\eta$, et à prouver que $E$ ou $S\setmin E$",
    SETMIN)
add(72, "(ix): 'Supposons donc que η∈S—E et distinguons deux cas'", "long dash for the set difference",
    "$S-E$", "convention", 7, "high",
    r"Supposons donc que $\eta\in S-E$", r"Supposons donc que $\eta\in S\setmin E$", SETMIN)
add(72, "(viii): 'et à prouver que E ou S—E est un voisinage de η. Si η∈E'", "long dash for the set difference",
    "$S-E$", "convention", 7, "high",
    r"$E$ ou $S-E$ est un voisinage de $\eta$. Si $\eta\in E$, on conclut",
    r"$E$ ou $S\setmin E$ est un voisinage de $\eta$. Si $\eta\in E$, on conclut", SETMIN)
add(72, "(viii): 'Si η∈S—E, on distingue de nouveau deux cas'", "long dash for the set difference",
    "$S-E$", "convention", 7, "high",
    r"Si $\eta\in S-E$, on distingue", r"Si $\eta\in S\setmin E$, on distingue", SETMIN)
add(72, "page break 72/73 (edit 1 of 2, insert): (viii), item 1° 'f_η(X_η) n'est pas une partie localement fermée de Y_η'",
    "printed p. 72 ends '... on distingue de nouveau deux cas :'; printed p. 73 begins with item 1° "
    "'f_η(X_η) n'est pas une partie localement fermée de Y_η. Comme f(X) ...' (page_073_s1.png)",
    "\\oldpage[IV-3]{73} stands at item 2° ('\\item\\oldpage[IV-3]{73} $f_\\eta(X_\\eta)$ est localement fermé'), "
    "one item (three printed lines) too late",
    "marker", None, "high",
    r"\item $f_\eta(X_\eta)$ n'est pas une partie localement fermée de $Y_\eta$.",
    r"\item\oldpage[IV-3]{73} $f_\eta(X_\eta)$ n'est pas une partie localement fermée de $Y_\eta$.",
    "Marker move: apply together with the p. 73 entry that removes the old marker (edit 2 of 2). Same "
    "\\item\\oldpage form as the old placement. The item-1° text needs no other fix.")

# ---------------- page 73 ----------------
add(73, "page break 72/73 (edit 2 of 2, remove the old marker): item 2° 'f_η(X_η) est localement fermé dans Y_η'",
    "item 2° stands on printed p. 73 below item 1°", "\\item\\oldpage[IV-3]{73} at item 2°",
    "marker", None, "high",
    r"\oldpage[IV-3]{73} $f_\eta(X_\eta)$ est localement fermé", r" $f_\eta(X_\eta)$ est localement fermé",
    "Apply together with the p. 72 insert (edit 1 of 2); leaves '\\item $f_\\eta(X_\\eta)$ est localement fermé'.")
add(73, "(x): 'et où η∈S—E. Distinguons trois cas'", "long dash for the set difference", "$S-E$",
    "convention", 7, "high",
    r"$\eta\in S-E$. Distinguons", r"$\eta\in S\setmin E$. Distinguons", SETMIN)
add(73, "(x) 2°: 'f_η(X_η) est ouvert dans Y_η mais f_η n'est pas une immersion'",
    "no comma before 'mais' (crop p73_s2_mais2.png)", "$Y_\\eta$, mais",
    "punctuation", None, "high",
    r"ouvert dans $Y_\eta$, mais $f_\eta$", r"ouvert dans $Y_\eta$ mais $f_\eta$")
add(73, "(x) 3°: 'supposer que f est une immersion fermée, et par suite'",
    "'immersion fermée' both italic (crop p73_s3_immfermee.png)", "immersion \\emph{fermée} ('immersion' upright)",
    "italics", None, "high",
    r"est une immersion<NL>  \emph{fermée}, et par suite", r"est une \emph{immersion<NL>  fermée}, et par suite")
add(73, "Proposition (9.6.2) I), labels (i)-(iv)", "labels (i) ... (iv) upright",
    "enumerate [label=(\\roman*)] inside the italic proposition: labels italic",
    "convention", 6, "high",
    r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]",
    "GLOBAL_ISSUES 16; one edit covers the four labels.")

# ---------------- page 74 ----------------
add(74, "Proposition (9.6.2) II): 'ample (resp. très ample) relativement à f_s'",
    "'(resp.' and ')' roman inside the italic statement, 'très ample' italic (crop p74_s1_II.png)",
    "all italic (proposition environment)", "convention", 6, "high",
    r"ample (resp. très ample) relativement à $f_s$, est",
    r"ample \textup{(resp.} très ample\textup{)} relativement à $f_s$, est")
add(74, "'On peut améliorer (9.6.2, II)) sous certaines conditions'",
    "two closing parentheses: 'II))' (crop p74_s2_ameliorer.png)", "(9.6.2, II) (one parenthesis)",
    "punctuation", None, "high",
    r"(9.6.2, II) sous", r"(9.6.2, II)) sous",
    "The label 'II)' keeps its own parenthesis inside the reference.")
add(74, "Proposition (9.6.3): 'f : X→Y un S-morphisme propre'",
    "'propre' roman inside the italic statement (crop p74_s2_963.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"$S$-morphisme propre, $\mathcal L$", r"$S$-morphisme \textup{propre}, $\mathcal L$")
add(74, "Proposition (9.6.3): 'l'ensemble E (resp. E') des s∈S'",
    "'(resp.' and ')' roman inside the italic statement (crop p74_s2_963.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"l'ensemble $E$ (resp. $E'$) des", r"l'ensemble $E$ \textup{(resp.} $E'$\textup{)} des")
add(74, "Proposition (9.6.3): 'ample (resp. très ample) relativement à f_s : X_s→Y_s'",
    "'(resp.' and ')' roman, 'très ample' italic (crop p74_s2_963.png)", "all italic (proposition environment)",
    "convention", 6, "high",
    r"ample (resp. très ample) relativement à<NL>$f_s:X_s",
    r"ample \textup{(resp.} très ample\textup{)} relativement à<NL>$f_s:X_s")
add(74, "proof of (9.6.3): 'si P(Z, T, M, g, k) désigne la relation'", "bold italic P", "\\mathbf P (bold upright)",
    "convention", 10, "high",
    r"si $\mathbf P(Z,T,\mathcal M,g,k)$ désigne", r"si $\boldsymbol{P}(Z,T,\mathcal M,g,k)$ désigne")
add(74, "proof of (9.6.3): 'que P(Z, T, M, g, k) vérifie la condition'", "bold italic P", "\\mathbf P (bold upright)",
    "convention", 10, "high",
    r"$\mathbf P(Z,T,\mathcal M,g,k)$ vérifie", r"$\boldsymbol{P}(Z,T,\mathcal M,g,k)$ vérifie")
add(74, "proof of (9.6.3): 'si η∈S—E (resp. η∈S—E'), alors S—E (resp. S—E')'",
    "long dash for the set difference, 4 times", "minus signs", "convention", 7, "high",
    r"$\eta\in S-E$ (resp. $\eta\in S-E'$), alors $S-E$ (resp. $S-E'$)",
    r"$\eta\in S\setmin E$ (resp. $\eta\in S\setmin E'$), alors $S\setmin E$ (resp. $S\setmin E'$)", SETMIN)
add(74, "proof of (9.6.3) I): 'les R^q f_*(L) sont tous des O_Y-Modules cohérents (III, 3.2.1)'",
    "'cohérents' italic (crop p74_s3_coherents.png)", "upright",
    "italics", None, "high",
    r"$\mathcal O_Y$-Modules cohérents", r"$\mathcal O_Y$-Modules \emph{cohérents}")
add(74, "proof of (9.6.3) I): 'L et les R^q f_*(L) sont tous S-plats'",
    "'tous' italic and 'plats' italic in S-plats (crop p74_s4_plats.png)", "upright",
    "italics", None, "high",
    r"sont tous $S$-plats", r"sont \emph{tous} $S$-\emph{plats}")
add(74, "display (9.6.3.1): 'f_*(L)⊗_{O_S} k(s) → (f_s)_*(L_s)'", "bold italic k", "k(s)",
    "convention", 1, "high",
    r"\otimes_{\mathcal O_S} k(s)", r"\otimes_{\mathcal O_S} \boldsymbol{k}(s)")

# ---------------- checks ----------------
ok = True
spans = {}
for i, d in enumerate(F):
    fx = d["fix"]
    if fx is None:
        continue
    t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(fx["old"])
    if n != 1:
        ok = False
        print("COUNT", n, d["page"], repr(fx["old"]))
        continue
    a = t.index(fx["old"])
    spans.setdefault(d["page"], []).append((a, a + len(fx["old"]), i))
    if fx["old"] == fx["new"]:
        ok = False
        print("NOCHANGE", d["page"], fx["old"])
for p, lst in spans.items():
    lst.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(lst, lst[1:]):
        if a2 < b1:
            ok = False
            print("OVERLAP page", p, F[i1]["fix"]["old"], "|", F[i2]["fix"]["old"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F), "checks ok" if ok else "CHECK FAILURES")
