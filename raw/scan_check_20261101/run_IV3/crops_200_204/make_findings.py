import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_200_204.json")


def F(page, where, scan, tex, kind, convention, confidence, old, new, note="", corrected=None, fix_null=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": None if fix_null else {"old": old, "new": new},
    }
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---- page 200
    F(200,
      "§14 introduction, l. 8-9: 'en termes de propriétés de la fibre f^{-1}(f(x)) de x'",
      "'la' roman, only 'fibre' italic (crop p200_lafibre.png)",
      "\\emph{la fibre}",
      "italics", None, "high",
      "\\emph{la fibre}", "la \\emph{fibre}"),
    # ---- page 201
    F(201,
      "Remarques (14.1.3), (ii), l. 2-3: 'alors f est ouvert au point ξ'",
      "'est' roman, 'ouvert au point' italic (crops p201_estouvert.png, p201_aupoint.png)",
      "\\emph{est ouvert au point $\\xi$}",
      "italics", None, "high",
      "\\emph{est ouvert au point", "est \\emph{ouvert au point",
      note="Judged with the remark body as roman (document-wide remark font)."),
    F(201,
      "Remarque (14.1.5), l. 6: '𝔠=(T_1)+(T_2—T_3)'",
      "long dash between T_2 and T_3: 41 px at 300 dpi, against 34 px for the bars of + and = on the same line (crop p201_T2T3.png)",
      "(T_2-T_3)",
      "convention", 7, "medium",
      "(T_2-T_3)", "(T_2\\setmin T_3)",
      note="Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision (FIX_POLICY 2.7)."),
    # ---- page 202
    F(202,
      "(14.2.1.1): 'dim(O_x ⊗_{O_y} k(y))'",
      "bold italic k (crop p202_formula.png)",
      "plain k(y)",
      "convention", 1, "high",
      "\\otimes_{\\mathcal O_y}k(y))", "\\otimes_{\\mathcal O_y}\\boldsymbol{k}(y))"),
    F(202,
      "proof of (14.2.1), l. 3: 'aucune composante irréductible X' de f^{-1}(Y') contenant x ne peut être contenue'",
      "'contenant' in italics (crop p202_contenant.png)",
      "'contenant' upright",
      "italics", None, "high",
      "contenant $x$ ne peut", "\\emph{contenant} $x$ ne peut"),
    F(202,
      "Proposition (14.2.3), last line: 'et telle que dim(Z)=dim(X'∩f^{-1}(y))=dim(X'∩f^{-1}(η)).'",
      "the formula is set in the running text, flush left on the statement's last line (crop p202_dimline.png)",
      "displayed with \\[ ... \\]",
      "other", None, "high",
      "telle que\n\\[\n  \\dim(Z)=\\dim(X'\\cap f^{-1}(y))=\\dim(X'\\cap f^{-1}(\\eta)).\n\\]",
      "telle que\n$\\dim(Z)=\\dim(X'\\cap f^{-1}(y))=\\dim(X'\\cap f^{-1}(\\eta))$.",
      note="Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost."),
    F(202,
      "Corollaire (14.2.5), l. 3: 'la fonction z⇝dim(f^{-1}(z))'",
      "wavy arrow (crop p202_arrow.png)",
      "\\mapsto",
      "symbol", None, "high",
      "$z\\mapsto\\dim(f^{-1}(z))$", "$z\\leadsto\\dim(f^{-1}(z))$",
      note="GLOBAL_ISSUES 33."),
    # ---- page 203
    F(203,
      "proof of (14.2.5), l. 3: 'on déduit de (13.1.5) que z⇝dim(f^{-1}(z)) est semi-continue'",
      "wavy arrow",
      "\\mapsto",
      "symbol", None, "high",
      "$z\\mapsto\\dim(f^{-1}(z))$ est semi-continue", "$z\\leadsto\\dim(f^{-1}(z))$ est semi-continue",
      note="GLOBAL_ISSUES 33."),
    F(203,
      "Corollaire (14.2.6), (i): '(resp. d(y)=d(y_i))'",
      "'(resp.' roman inside the italic statement (crop p203_resp.png)",
      "italic (corollary environment)",
      "convention", 6, "high",
      "(resp. $d(y)=d(y_i)$)", "\\textup{(resp. $d(y)=d(y_i)$)}"),
    F(203,
      "Corollaire (14.2.6), (i): 'la fonction E (resp. d)'",
      "'(resp.' roman inside the italic statement (crop p203_resp.png)",
      "italic (corollary environment)",
      "convention", 6, "high",
      "(resp. $d$)", "\\textup{(resp. $d$)}"),
    F(203,
      "Corollaire (14.2.6), (ii): 'la fonction z⇝dim(U∩f^{-1}(z))'",
      "wavy arrow",
      "\\mapsto",
      "symbol", None, "high",
      "$z\\mapsto\\dim(U\\cap f^{-1}(z))$", "$z\\leadsto\\dim(U\\cap f^{-1}(z))$",
      note="GLOBAL_ISSUES 33."),
    F(203,
      "proof of (14.2.6), (ii), l. 6: 'un morphisme ouvert de type fini (I, 6.3.5)'",
      "bold I (crop p203_I635.png)",
      "(I, 6.3.5)",
      "convention", 2, "high",
      "(I, 6.3.5)", "(\\textbf{I}, 6.3.5)"),
    F(203,
      "proof of (14.2.6), (ii), l. 7: 'x_{ij} est point maximal de U∩f^{-1}(y_i) et il résulte de (13.1.1)'",
      "no comma before 'et il résulte' (crop p203_comma.png)",
      "'$U\\cap f^{-1}(y_i)$, et il'",
      "punctuation", None, "high",
      "$U\\cap f^{-1}(y_i)$, et il", "$U\\cap f^{-1}(y_i)$ et il"),
    F(203,
      "proof of (14.2.6), (ii), l. 8: 'appliqué à la restriction X_{ij}→Y_i=\\overline{\\{y_i\\}} de f'",
      "X_{ij} without prime (crop p203_Xij1.png); the print defines X'_{ij}=\\overline{\\{x_{ij}\\}} two lines earlier (with prime, crop p203_Xprime.png)",
      "X'_{ij}",
      "misprint_in_print", None, "high",
      "$X'_{ij}\\to Y_i", "$X_{ij}\\to Y_i",
      corrected="X'_{ij}\\to Y_i",
      note="The print drops the prime of X'_{ij} in its last four uses (this and the next three entries); the TeX silently restores it. Fix returns to the printed reading."),
    F(203,
      "proof of (14.2.6), (ii), l. 8: '(compte tenu de (I, 5.2.2) et de (1.5.4))'",
      "bold I (crop p203_I522.png)",
      "(I, 5.2.2)",
      "convention", 2, "high",
      "(I, 5.2.2)", "(\\textbf{I}, 5.2.2)"),
    F(203,
      "proof of (14.2.6), (ii), l. 9: 'les composantes irréductibles de X_{ij}∩f^{-1}(y) ont une dimension'",
      "X_{ij} without prime (crop p203_Xij2a.png)",
      "X'_{ij}",
      "misprint_in_print", None, "high",
      "$X'_{ij}\\cap f^{-1}(y)$ ont", "$X_{ij}\\cap f^{-1}(y)$ ont",
      corrected="X'_{ij}\\cap f^{-1}(y)",
      note="Same dropped prime; TeX silently corrected."),
    F(203,
      "proof of (14.2.6), (ii), l. 9: '≥dim(X_{ij}∩f^{-1}(y_i))'",
      "X_{ij} without prime (crop p203_Xij2b.png)",
      "X'_{ij}",
      "misprint_in_print", None, "high",
      "\\dim(X'_{ij}\\cap", "\\dim(X_{ij}\\cap",
      corrected="\\dim(X'_{ij}\\cap",
      note="Same dropped prime; TeX silently corrected."),
    F(203,
      "proof of (14.2.6), (ii), l. 12: 'composantes irréductibles de X_{ij}∩f^{-1}(y) (1≤j≤m_i)'",
      "X_{ij} without prime (crop p203_Xij3.png)",
      "X'_{ij}",
      "misprint_in_print", None, "high",
      "$X'_{ij}\\cap f^{-1}(y)$ ($1", "$X_{ij}\\cap f^{-1}(y)$ ($1",
      corrected="X'_{ij}\\cap f^{-1}(y)",
      note="Same dropped prime; TeX silently corrected."),
    F(203,
      "Remarque (14.2.7), l. 3: 'remplacer la fonction z⇝dim(f^{-1}(z))'",
      "wavy arrow",
      "\\mapsto",
      "symbol", None, "high",
      "$z\\mapsto\\dim(f^{-1}(z))$ par", "$z\\leadsto\\dim(f^{-1}(z))$ par",
      note="GLOBAL_ISSUES 33."),
    F(203,
      "Remarque (14.2.7), l. 3: 'par la fonction z⇝E(z)'",
      "wavy arrow",
      "\\mapsto",
      "symbol", None, "high",
      "$z\\mapsto E(z)$", "$z\\leadsto E(z)$",
      note="GLOBAL_ISSUES 33."),
    # ---- page 204
    F(204,
      "Définition (14.3.3), l. 2: 'On dit que f est universellement ouvert au point x si'",
      "the defined term is italic like the rest of the statement, no change of face (crop p204_def.png)",
      "\\emph{universellement ouvert au point $x$} inside the italic definition environment (prints upright)",
      "convention", 6, "high",
      "\\emph{universellement ouvert au point $x$}", "universellement ouvert au point $x$",
      note="FIX_POLICY 2.6: inside an italic environment drop \\emph where the print shows no change of face."),
    F(204,
      "Remarques (14.3.3.1), end of (ii): '... tels que f' ne soit pas ouvert au point x'.' | p. 205 'Or, si y'=f'(x'), ...'",
      "the paragraph of (ii) runs on across the page break: p. 205 begins flush left with 'Or, si y'=f'(x'), ... est un voisinage de x dans f^{-1}(y).', which ends remark (ii); Proposition (14.3.4) follows",
      "\\end{enumerate}\\end{remarks} and a blank line before \\oldpage[IV-3]{205}, another blank line after it: the end of (ii) on p. 205 falls outside the remarks, as a new paragraph",
      "other", None, "high",
      "ouvert au point $x'$.\n\\end{enumerate}\n\\end{remarks}\n\n", "ouvert au point $x'$.\n",
      note="Apply together with the two page-205 entries below (blank line after the marker; \\end{enumerate}\\end{remarks} moved before Proposition (14.3.4)). 'old' ends with the blank line before the 205 marker."),
    # ---- page 205 companions (edits that must be applied with the last page-204 entry)
    F(205,
      "top of p. 205: 'Or, si y'=f'(x'), ...' continues remark (ii) of (14.3.3.1)",
      "no paragraph break: the line starts flush left",
      "blank line after \\oldpage[IV-3]{205}",
      "marker", None, "high",
      "\\oldpage[IV-3]{205}\n\nOr, si", "\\oldpage[IV-3]{205}\nOr, si",
      note="Companion of the page-204 entry on the end of Remarques (14.3.3.1); the pp. 205-209 checker may report the same blank line: apply once."),
    F(205,
      "p. 205, l. 4: '... qui est un voisinage de x dans f^{-1}(y).' ends Remarques (14.3.3.1), (ii)",
      "the remark ends here; Proposition (14.3.4) follows",
      "remarks environment closed on p. 204, before the marker",
      "other", None, "high",
      "$f^{-1}(y)$.\n\n\\begin{proposition}[14.3.4]",
      "$f^{-1}(y)$.\n\\end{enumerate}\n\\end{remarks}\n\n\\begin{proposition}[14.3.4]",
      note="Companion of the page-204 entry: the \\end{enumerate}\\end{remarks} removed there goes here."),
]

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

# verification: every fix's old occurs exactly once in its page file (CRLF normalised to LF)
ok = True
for f in findings:
    if f["fix"] is None:
        continue
    p = os.path.join(RUN, "page_%03d.tex" % f["page"])
    with open(p, encoding="utf-8") as fh:
        txt = fh.read().replace("\r\n", "\n")
    n = txt.count(f["fix"]["old"])
    if n != 1:
        ok = False
        print("COUNT", n, f["page"], repr(f["fix"]["old"]))
sys.stdout.reconfigure(encoding="utf-8")
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0, 0])
    if f["kind"] == "misprint_in_print":
        c[2] += 1
    elif f["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("all unique" if ok else "NOT ALL UNIQUE", counts)
