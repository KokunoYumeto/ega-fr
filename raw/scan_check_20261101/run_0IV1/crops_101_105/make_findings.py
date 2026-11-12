import json

OUT = r"user\Documents\ega_scan_check_20261101\run_0IV1\findings_101_105.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


LBL = ("Label printed upright; \\item[...] comes out italic inside the italic statement environment "
       "(same form as the label fixes on pp. 20, 36-38).")

# ---------------- page 101 ----------------
add(101, "proof of (19.6.1), start of part II: 'II. — Cas général. —'",
    "II. — Cas général. — (numeral and first dash upright; only 'Cas général.' italic)",
    r"\emph{II. --- Cas général.} ---", "italics", None, "high",
    r"\emph{II. --- Cas général.}", r"II. --- \emph{Cas général.}",
    "Checked on an enlarged crop.")
for lab in ("a)", "b)", "c)"):
    add(101, "Corollaire (19.6.3), label " + lab, lab + " (upright)", r"\item[" + lab + "]", "convention", 6, "high",
        r"\item[" + lab + "]", r"\item[\textup{" + lab + "}]", LBL)

# ---------------- page 102 ----------------
add(102, "proof of (19.6.3): 'A contient un sous-corps premier k_0'",
    "sous-corps *premier* k_0 (premier italic)", r"sous-corps premier $k_0$,", "italics", None, "high",
    r"sous-corps premier $k_0$,", r"sous-corps \emph{premier} $k_0$,", "Checked on an enlarged crop.")
add(102, "proof of (19.6.3): 'dont k est par suite extension séparable.'",
    "extension *séparable*. (séparable italic)", r"extension séparable. Appliquant", "italics", None, "high",
    r"extension séparable. Appliquant", r"extension \emph{séparable}. Appliquant", "Checked on an enlarged crop.")
add(102, "proof of (19.6.3): 'u(T_i)=x_i pour tout i et cet homomorphisme est surjectif'",
    "pour tout i et cet homomorphisme (no comma)", r"pour tout $i$, et cet", "punctuation", None, "high",
    r"pour tout $i$, et cet", r"pour tout $i$ et cet", "Comma added in the TeX; checked on an enlarged crop.")
add(102, "Théorème (19.6.4): 'On suppose que K soit une extension séparable de k.'",
    "séparable printed upright (emphasis by roman type in the italic statement)",
    r"séparable de $k$. Alors (italic in the environment)", "convention", 6, "high",
    r"séparable de $k$. Alors", r"\textup{séparable} de $k$. Alors",
    r"\emph{séparable} gives the same output.")
for lab in ("a)", "b)", "b')", "c)"):
    add(102, "Théorème (19.6.4), label " + lab, lab + " (upright)", r"\item[" + lab + "]", "convention", 6, "high",
        r"\item[" + lab + "]", r"\item[\textup{" + lab + "}]", LBL)
add(102, "Théorème (19.6.4) b): '(dont la structure de k-algèbre est définie par l'homomorphisme composé'",
    "the whole parenthetical of b), from '(dont' to 'de K)', is printed upright",
    "inside the theorem environment (italic)", "convention", 6, "high",
    "(dont la structure de $k$-algèbre est\n  définie par l'homomorphisme composé",
    "\\textup{(dont la structure de $k$-algèbre est\n  définie par l'homomorphisme composé}",
    "First half, before the display (the display itself is math and needs no change); the second half is the next finding.")
add(102, "Théorème (19.6.4) b), after the display: 'où ψ est l'injection canonique et φ l'homomorphisme définissant la structure d'extension de K).'",
    "printed upright (end of the parenthetical of b))", "inside the theorem environment (italic)",
    "convention", 6, "high",
    "où $\\psi$ est l'injection canonique et $\\varphi$ l'homomorphisme définissant\n  la structure d'extension de $K$).",
    "\\textup{où $\\psi$ est l'injection canonique et $\\varphi$ l'homomorphisme définissant\n  la structure d'extension de $K$)}.",
    "")
add(102, "Corollaire (19.6.5): '(cf. IV, 6.7.6)'", "(cf. IV, 6.7.6) upright, IV bold",
    r"(cf.~$\mathbf{IV}$, 6.7.6)", "convention", 6, "high",
    r"(cf.~$\mathbf{IV}$, 6.7.6)", r"\textup{(cf.~$\mathbf{IV}$, 6.7.6)}", "")
add(102, "Corollaire (19.6.5): 'est régulier (17.3.6)'", "(17.3.6) upright", r"est régulier (17.3.6)",
    "convention", 6, "high", r"est régulier (17.3.6)", r"est régulier \textup{(17.3.6)}", "")

# ---------------- page 103 ----------------
add(103, "proof of (19.6.5.1): 'comme A' est un anneau régulier, il est réduit, donc il en est de même de K, ce qui prouve que K est une extension séparable de k'",
    "donc il en est de même de K,", r"donc il en est de même de $K$,", "misprint_in_print", None, "medium",
    None, None,
    "The TeX keeps the printed reading. The ring meant is K⊗_k k' (the subring of A' named in the preceding clause): "
    "its reducedness for every finite k' is what the cited criterion (Bourbaki, Alg. VIII, § 7, n° 3, th. 1) needs; "
    "'K' alone (a field) makes the inference empty. No entry in the errata lists of the TeX.",
    corrected=r"donc il en est de même de $K\otimes_k k'$,")
add(103, "Remarque (19.6.5.2): 'un tel anneau ne peut donc être k-isomorphe à K[[T_1, ..., T_n]]'",
    "*k-isomorphe* (italic)", r"être $k$-isomorphe", "italics", None, "high",
    r"être $k$-isomorphe", r"être \emph{$k$-isomorphe}",
    "Judged with the remark body roman (document-wide remark item).")
add(103, "Remarque (19.6.5.2): 'bien qu'il lui soit isomorphe en vertu de (19.6.5)'",
    "*isomorphe* (italic)", r"lui soit isomorphe", "italics", None, "high",
    r"lui soit isomorphe", r"lui soit \emph{isomorphe}",
    "Judged with the remark body roman (document-wide remark item).")
add(103, "Proposition (19.6.6): parenthetical '(nous exprimerons plus tard ... lorsque K est une extension de type fini de k)'",
    "the whole parenthetical is printed upright, with 'multiplicité radicielle finie' and 'extension de type fini de k' italic",
    "inside the proposition environment: italic, with the \\emph words upright", "convention", 6, "high",
    "(nous\nexprimerons plus tard cette propriété en disant que $K$ est de\n"
    "\\emph{multiplicité radicielle finie} sur $k$ ($\\mathbf{IV}$, 4.7.4) et nous\n"
    "verrons que cette condition est toujours satisfaite lorsque $K$ est une\n"
    "\\emph{extension de type fini} de $k$)",
    "\\textup{(nous\nexprimerons plus tard cette propriété en disant que $K$ est de\n"
    "\\emph{multiplicité radicielle finie} sur $k$ ($\\mathbf{IV}$, 4.7.4) et nous\n"
    "verrons que cette condition est toujours satisfaite lorsque $K$ est une\n"
    "\\emph{extension de type fini} de $k$)}",
    "Inside \\textup the existing \\emph words come out italic, as printed. Apply before the next finding (its 'old' lies inside this one).")
add(103, "Proposition (19.6.6), same parenthetical: 'lorsque K est une extension de type fini de k)'",
    "*extension de type fini de* k (the italic includes the 'de' before k)", r"\emph{extension de type fini} de $k$)",
    "italics", None, "medium",
    r"\emph{extension de type fini} de $k$)", r"\emph{extension de type fini de} $k$)",
    "Apply after the preceding convention-6 edit. Checked on an enlarged crop.")
add(103, "Proposition (19.6.6) b'): 'ait au moins un anneau local composant'",
    "'au moins un' printed upright (emphasis in the italic statement)", r"ait au moins un anneau",
    "convention", 6, "high", r"ait au moins un anneau", r"ait \textup{au moins un} anneau",
    r"\emph{au moins un} gives the same output. Checked on an enlarged crop.")
add(103, "Proposition (19.6.6) c): 'A est géométriquement régulier sur k (19.6.5).'", "(19.6.5) upright",
    r"sur $k$ (19.6.5).", "convention", 6, "high", r"sur $k$ (19.6.5).", r"sur $k$ \textup{(19.6.5)}.", "")
for lab in ("a)", "b)", "b')", "c)"):
    add(103, "Proposition (19.6.6), label " + lab, lab + " (upright)", r"\item[" + lab + "]", "convention", 6, "high",
        r"\item[" + lab + "]", r"\item[\textup{" + lab + "}]", LBL)

# ---------------- page 104 ----------------
add(104, "proof of (19.6.6): 'des composants locaux de Â⊗_k k''=(Â⊗_k k')⊗_{k'} k'', on voit que'",
    "formula set inline in the running text", "displayed (\\[ ... \\])", "other", None, "high",
    "aussi des composants locaux de\n\\[\n  \\widehat A\\otimes_k k''\n  =(\\widehat A\\otimes_k k')\\otimes_{k'}k'',\n\\]\non voit",
    "aussi des composants locaux de\n$\\widehat A\\otimes_k k''=(\\widehat A\\otimes_k k')\\otimes_{k'}k''$,\non voit",
    "Layout only (GLOBAL_ISSUES 21); the formula itself matches.")
add(104, "proof of (19.6.6): 'composé direct d'anneaux locaux isomorphes à A'_0'",
    "*isomorphes à* (the à is italic too)", r"\emph{isomorphes} à $A'_0$", "italics", None, "high",
    r"\emph{isomorphes} à $A'_0$", r"\emph{isomorphes à} $A'_0$", "Checked on an enlarged crop (single-storey italic à).")
add(104, "proof of (19.6.6): 'donc aussi une extension séparable de k'_0'",
    "aussi (upright)", r"\emph{aussi}", "italics", None, "high",
    r"\emph{aussi} une extension", r"aussi une extension", "Checked on an enlarged crop.")
add(104, "proof of (19.6.6): 'Or, si c) est vérifié, alors,'", "vérifié", r"vérifiée", "word", None, "high",
    r"est vérifiée, alors", r"est vérifié, alors", "Checked on an enlarged crop. Masculine in the print (cf. 'si c) est vérifiée' on p. 102): not a misprint.")
add(104, "heading 19.7: 'Cas des homomorphismes locaux; théorèmes d'existence et d'unicité.'",
    "title ends with a full stop", r"...d'unicité}", "punctuation", None, "high",
    "d'existence et\nd'unicité}", "d'existence et\nd'unicité.}", "GLOBAL_ISSUES 43/58 (subsection titles without the printed full stop).")
add(104, "introduction of 19.7: 'sa topologie r-préadique, où r est son radical'",
    "r-*préadique* (préadique italic)", r"$\mathfrak r$-préadique", "italics", None, "high",
    r"$\mathfrak r$-préadique", r"$\mathfrak r$-\emph{préadique}", "Checked on an enlarged crop.")
add(104, "Théorème (19.7.1), label a)", "a) (upright)", r"\item[a)]", "convention", 6, "high",
    r"\item[a)]", r"\item[\textup{a)}]", LBL)
add(104, "Théorème (19.7.1) a): 'B est une A-algèbre formellement lisse.'",
    "formellement lisse in the italic of the statement (no change of face)",
    r"\emph{formellement lisse} (upright inside the environment)", "convention", 6, "high",
    r"$A$-algèbre \emph{formellement lisse}", r"$A$-algèbre formellement lisse",
    "Drop \\emph where the print shows no change of face (FIX_POLICY 2.6).")

# ---------------- page 105 ----------------
add(105, "Théorème (19.7.1), label b)", "b) (upright)", r"\item[b)]", "convention", 6, "high",
    r"\item[b)]", r"\item[\textup{b)}]", LBL)
add(105, "Théorème (19.7.1) b): 'B est un A-module plat et'", "plat in the italic of the statement",
    r"\emph{plat} (upright inside the environment)", "convention", 6, "high",
    r"\emph{plat} et", r"plat et", "Drop \\emph where the print shows no change of face (FIX_POLICY 2.6).")
add(105, "Théorème (19.7.1) b): 'est une k-algèbre formellement lisse.'", "formellement lisse in the italic of the statement",
    r"\emph{formellement lisse} (upright inside the environment)", "convention", 6, "high",
    r"\emph{formellement lisse}.", r"formellement lisse.", "Drop \\emph where the print shows no change of face (FIX_POLICY 2.6).")
add(105, "proof of (19.7.1.1): 'les idéaux 𝔏_m = Σ_{i=1}^n (x_i^0)^m B_0 (pour m>0) forment'",
    "(pour m>0), formula inline in the running text",
    "displayed, with \\qquad (m>0): the word 'pour' is missing", "missing", None, "high",
    "\\[\n  \\mathfrak Q_m=\\sum_{i=1}^n(x_i^0)^mB_0 \\qquad (m>0)\n\\]",
    "$\\mathfrak Q_m=\\sum_{i=1}^n(x_i^0)^mB_0$ (pour $m>0$)",
    "The same edit sets the formula inline, as printed. Apply before the next finding (Fraktur letter of the same formula).")
add(105, "proof of (19.7.1.1), same formula: the letter 𝔏_m", "Fraktur L (𝔏_m)", r"\mathfrak Q_m", "symbol", None, "high",
    r"\mathfrak Q_m=\sum", r"\mathfrak L_m=\sum",
    "Same glyph as the Fraktur L of 0_I p. 77 ((7.7.7), \\mathfrak L there). Apply after the preceding edit.")
add(105, "proof of (19.7.1.1): 'car 𝔏_m est évidemment contenu dans 𝔫_0^m'", "Fraktur L (𝔏_m)",
    r"$\mathfrak Q_m$ est", "symbol", None, "high", r"$\mathfrak Q_m$ est", r"$\mathfrak L_m$ est",
    "Checked on an enlarged crop.")
add(105, "proof of (19.7.1.1): 'Tout revient par suite à prouver que les B/𝔍^m sont des A-modules libres'",
    "B/𝔍^m (exponent m)", r"$B/\mathfrak J_m$ (index m)", "misprint_in_print", None, "high",
    r"$B/\mathfrak J_m$", r"$B/\mathfrak J^m$",
    "The TeX silently corrects the print; the diplomatic text should keep 𝔍^m. The quotients meant are by the ideals 𝔍_m "
    "defined three lines earlier (they form the fundamental system just established). Checked on an enlarged crop.",
    corrected=r"$B/\mathfrak J_m$")
for lab in ("(i)", "(ii)", "(iii)"):
    add(105, "Lemme (19.7.1.2), label " + lab, lab + " (upright)", r"\item[" + lab + "]", "convention", 6, "high",
        r"\item[" + lab + "]", r"\item[\textup{" + lab + "}]", LBL + " GLOBAL_ISSUES 16.")
NP = ("The print names the maximal ideal of C 𝔫, without a prime, throughout this proof "
      "(9 places on p. 105 and the formula at the top of page_106.tex); the TeX has 𝔫'.")
add(105, "proof of (19.7.1.2): 'les idéaux Im(𝔪^i⊗_A C)+Im(B⊗_A 𝔫^j)'", "𝔫^j (no prime)",
    r"\mathfrak n'{}^j", "symbol", None, "high",
    r"(B\otimes_A\mathfrak n'{}^j)", r"(B\otimes_A\mathfrak n^j)", NP)
add(105, "proof of (19.7.1.2): 'Si l'on pose 𝔯 = Im(𝔪⊗_A C)+Im(B⊗_A 𝔫), on a'",
    "formula set inline in the running text", "displayed (\\[ ... \\])", "other", None, "high",
    "pose\n\\[\n  \\mathfrak r=\\operatorname{Im}(\\mathfrak m\\otimes_A C)+\n  \\operatorname{Im}(B\\otimes_A\\mathfrak n'),\n\\]\non a",
    "pose\n$\\mathfrak r=\\operatorname{Im}(\\mathfrak m\\otimes_A C)+\n\\operatorname{Im}(B\\otimes_A\\mathfrak n')$,\non a",
    "Layout only (GLOBAL_ISSUES 21). Apply before the next finding (prime of 𝔫 in the same formula).")
add(105, "same formula: 'Im(B⊗_A 𝔫)'", "𝔫 (no prime)", r"\mathfrak n'", "symbol", None, "high",
    r"(B\otimes_A\mathfrak n')", r"(B\otimes_A\mathfrak n)", "Apply after the preceding layout edit. " + NP)
add(105, "proof of (19.7.1.2): '𝔯^{2i} ⊂ Im(𝔪^i⊗_A C)+Im(B⊗_A 𝔫^i) ⊂ 𝔯^i'", "𝔫^i (no prime)",
    r"\mathfrak n'{}^i", "symbol", None, "high",
    r"(B\otimes_A\mathfrak n'{}^i)", r"(B\otimes_A\mathfrak n^i)", NP)
add(105, "proof of (19.7.1.2): '(B⊗_A C)/𝔯 = (B/𝔪)⊗_A(C/𝔫)'", "C/𝔫 (no prime)", r"(C/\mathfrak n')",
    "symbol", None, "high", r"\otimes_A(C/\mathfrak n')$", r"\otimes_A(C/\mathfrak n)$", NP)
add(105, "proof of (19.7.1.2): 'est un (C/𝔫)-module de type fini'", "(C/𝔫) (no prime)", r"$(C/\mathfrak n')$-module",
    "symbol", None, "high", r"$(C/\mathfrak n')$-module", r"$(C/\mathfrak n)$-module", NP)
add(105, "proof of (19.7.1.2): 'étant un quotient de ((𝔪/𝔪²)⊗_A C)⊕(B⊗_A(𝔫/𝔫²)), est un'",
    "formula set inline in the running text", "displayed (\\[ ... \\])", "other", None, "high",
    "quotient de\n\\[\n  ((\\mathfrak m/\\mathfrak m^2)\\otimes_A C)\n  \\oplus(B\\otimes_A(\\mathfrak n'/\\mathfrak n'{}^2)),\n\\]\nest un",
    "quotient de\n$((\\mathfrak m/\\mathfrak m^2)\\otimes_A C)\n\\oplus(B\\otimes_A(\\mathfrak n'/\\mathfrak n'{}^2))$,\nest un",
    "Layout only (GLOBAL_ISSUES 21). Apply before the next finding (primes of 𝔫 in the same formula).")
add(105, "same formula: '(𝔫/𝔫²)'", "𝔫/𝔫² (no primes)", r"(\mathfrak n'/\mathfrak n'{}^2)", "symbol", None, "high",
    r"(\mathfrak n'/\mathfrak n'{}^2)", r"(\mathfrak n/\mathfrak n^2)", "Apply after the preceding layout edit. " + NP)
add(105, "proof of (19.7.1.2): 'que E, qui est isomorphe à lim_{i,j}((B/𝔪^i)⊗_A(C/𝔫^j)), est aussi isomorphe'",
    "formula set inline in the running text", "displayed (\\[ ... \\])", "other", None, "high",
    "isomorphe à\n\\[\n  \\varprojlim_{i,j}((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j)),\n\\]\nest aussi",
    "isomorphe à\n$\\varprojlim_{i,j}((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))$,\nest aussi",
    "Layout only (GLOBAL_ISSUES 21). Apply before the next finding (prime of 𝔫 in the same formula).")
add(105, "same formula: 'C/𝔫^j'", "𝔫^j (no prime)", r"\mathfrak n'{}^j", "symbol", None, "high",
    r"\varprojlim_{i,j}((B/\mathfrak m^i)\otimes_A(C/\mathfrak n'{}^j))",
    r"\varprojlim_{i,j}((B/\mathfrak m^i)\otimes_A(C/\mathfrak n^j))", "Apply after the preceding layout edit. " + NP)
add(105, "proof of (19.7.1.2), last line of p. 105: 'à lim_i(lim_j((B/𝔪^i)⊗_A(C/𝔫^j))); mais'",
    "formula set inline, same paragraph continuing with 'mais'",
    "displayed with \\left( \\right), followed by a blank line (paragraph break) before the p. 106 marker", "other", None, "high",
    "projective, à\n\\[\n  \\varprojlim_i\\left(\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))\\right)~;\n\\]\n\n",
    "projective, à\n$\\varprojlim_i(\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j)))$~;\n",
    "Layout only: inline, normal-size parentheses, no paragraph break (the 'old' ends with the blank line before the p. 106 marker). "
    "Apply before the next finding (prime of 𝔫 in the same formula).")
add(105, "same formula: 'C/𝔫^j'", "𝔫^j (no prime)", r"\mathfrak n'{}^j", "symbol", None, "high",
    "\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))",
    "\\varprojlim_j\n  ((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n^j))", "Apply after the preceding layout edit. " + NP)
add(106, "page break 105/106 (scan evidence: p. 105 ends 'mais lim_j((B/𝔪^i)⊗_A(C/𝔫^j))', p. 106 begins 'est le séparé complété')",
    "'mais lim_j((B/𝔪^i)⊗_A(C/𝔫^j))' is the last line of p. 105 (no prime on 𝔫); p. 106 starts with 'est le'",
    r"\oldpage[0\textsubscript{IV-1}]{106} stands before 'mais $\varprojlim_j(...\mathfrak n'{}^j))$', between blank lines",
    "marker", None, "high",
    "\\oldpage[0\\textsubscript{IV-1}]{106}\n\nmais $\\varprojlim_j((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n'{}^j))$ est le",
    "mais $\\varprojlim_j((B/\\mathfrak m^i)\\otimes_A(C/\\mathfrak n^j))$\n\\oldpage[0\\textsubscript{IV-1}]{106}\nest le",
    "OUTSIDE THE PAGE-105 SEGMENT: filed under page 106 so that apply_fixes finds it (old lies in page_106.tex, ega0-19-fr.tex at the "
    "p. 106 marker). One edit: moves the marker after the formula, removes the paragraph breaks around it, and removes the prime of 𝔫 "
    "in the moved formula (" + NP + ")")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written")
