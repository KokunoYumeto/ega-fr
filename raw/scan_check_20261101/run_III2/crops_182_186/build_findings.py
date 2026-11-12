"""Build findings_182_186.json for EGA III part 2, printed pp. 182-186 (ega3-7-fr.tex).
In the edit strings below the pilcrow stands for a line break (LF)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
OUT = RUN / "findings_182_186.json"


def N(s):
    return s.replace("\u00b6", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": N(old), "new": N(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


INL = "Display set inline, as printed (GLOBAL_ISSUES items 21/36)."
INC = "Edit included in the fix of the finding '{}' (same page); no separate fix."
WAVY = "Wavy arrow in the print (\\leadsto), not convention 3; GLOBAL_ISSUES item 33."
KAPPA = ("ega3-7-fr.tex writes the residue field as \\kappa(x) (77 times in the file), not k; the print has bold italic k, "
         "bold upright k in subscripts (GLOBAL_ISSUES item 48).")
ABF = ("Category Ab printed bold italic (enlarged crops); the TeX has bold upright \\mathbf{Ab}. Fix in the form already applied "
       "on pp. 177-181 (\\boldsymbol{Ab}).")
ABS = (" Bold italic inside the italic statement too (asymmetric italic A, leaning b; compared on enlarged crops with the "
       "running-text Ab of p. 184), unlike the bold upright Ab that the pp. 187-191 checker reports inside (7.5.2) and (7.5.4).")
REF = "Reference printed upright inside the italic statement (enlarged crop); same form as the pp. 177-181 fixes."

# ---------------------------------------------------------------- p. 182
W1 = "(7.3.4): 'Alors la fonction x⇝rang_{k(x)}(T_p(k(x))) est localement constante'"
add(182, W1, "formula in the running text; wavy arrow; bold upright k in the subscript of rang, bold italic k in T_p(k(x))",
    "displayed \\[ x\\mapsto\\operatorname{rang}_{\\kappa(x)}(T_p(\\kappa(x))) \\]", "other", None, "high",
    r"la fonction¶\[¶  x\mapsto\operatorname{rang}_{\kappa(x)}(T_p(\kappa(x)))¶\]¶est localement",
    r"la fonction¶$x\leadsto\operatorname{rang}_{\mathbf{k}(x)}(T_p(\boldsymbol{k}(x)))$¶est localement",
    INL + " The fix also carries the three edits reported separately below (wavy arrow, two residue-field k's).")
add(182, "(7.3.4): 'x⇝rang_{k(x)}(…)', arrow", "wavy arrow ⇝", "\\mapsto", "symbol", None, "high", None, None,
    WAVY + " " + INC.format(W1))
add(182, "(7.3.4): 'rang_{k(x)}', subscript", "bold upright k in the subscript k(x) (enlarged crop)", "\\kappa(x)",
    "convention", 1, "high", None, None, KAPPA + " Correct form: \\mathbf{k}(x). " + INC.format(W1))
add(182, "(7.3.4): 'T_p(k(x))'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " Correct form: \\boldsymbol{k}(x). " + INC.format(W1))

W2 = "proof of (7.3.4): 'on a en outre T_p(k(x))=T_p(A)⊗_A k(x) (7.3.3, e))'"
add(182, W2, "formula in the running text; bold italic k twice", "displayed, with \\kappa(x) twice", "other", None, "high",
    r"on a en outre¶\[¶  T_p(\kappa(x))=T_p(A)\otimes_A\kappa(x)¶\]¶(7.3.3",
    r"on a en outre¶$T_p(\boldsymbol{k}(x))=T_p(A)\otimes_A\boldsymbol{k}(x)$¶(7.3.3",
    INL + " The fix also carries the two residue-field k's reported separately below.")
add(182, "proof of (7.3.4): 'T_p(k(x))'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " " + INC.format(W2))
add(182, "proof of (7.3.4): 'T_p(A)⊗_A k(x)'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " " + INC.format(W2))
add(182, "proof of (7.3.4): 'est localement constant (loc. cit.), d'où'", "'(loc. cit.)' italic, parentheses included (enlarged crop)",
    "parentheses upright", "italics", None, "medium",
    r"(\emph{loc. cit.})", r"\emph{(loc. cit.)}", "Same form as the run_III2 fix on p. 138.")

add(182, "(7.3.5) h): '(ou, ce qui revient au même (Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 5) un A-module libre)'",
    "the parenthesis '(ou, ce qui revient au même (Bourbaki, … prop. 5) un A-module' is roman, with 'Alg. comm.' italic; 'libre)' italic",
    "all italic (italic proposition), 'Alg. comm.' upright through \\emph", "convention", 6, "high",
    r"plat (ou, ce qui revient au même (Bourbaki,¶    \emph{Alg. comm.}, chap. II, \S 3, n\textsuperscript{o} 2, cor. 2 de la¶    prop. 5) un $A$-module libre)",
    r"plat \textup{(ou, ce qui revient au même (Bourbaki,¶    \emph{Alg. comm.}, chap. II, \S 3, n\textsuperscript{o} 2, cor. 2 de la¶    prop. 5) un $A$-module} libre)",
    "Inside \\textup the \\emph makes 'Alg. comm.' italic, as printed; 'libre' stays italic.")
add(182, "(7.3.5): 'Alors les conditions de (7.3.3) sont encore équivalentes'", "reference (7.3.3) upright",
    "italic (italic proposition)", "convention", 6, "high",
    r"les conditions de (7.3.3) sont", r"les conditions de \textup{(7.3.3)} sont", REF)

add(182, "(7.3.5) g): 'L'homomorphisme canonique T_i(ε) : T_i(A_s)→T_i(k) est un épimorphisme'",
    "formula in the running text", "displayed", "other", None, "high",
    r"canonique¶    \[¶      T_i(\varepsilon):T_i(A_s)\longrightarrow T_i(k)¶    \]¶    est un",
    r"canonique¶    $T_i(\varepsilon):T_i(A_s)\longrightarrow T_i(k)$¶    est un", INL)

KF = "Category letter printed bold italic (GLOBAL_ISSUES items 18, 38, 44); the TeX has calligraphic \\mathcal K."
add(182, "(7.3.5.3): 'Soient K, K' deux catégories abéliennes'", "bold italic K, K'", "\\mathcal K, \\mathcal K'", "font", None, "high",
    r"Soient $\mathcal K$, $\mathcal K'$ deux", r"Soient $\boldsymbol{K}$, $\boldsymbol{K}'$ deux", KF + " Two occurrences, one edit.")
add(182, "(7.3.5.3): 'F : K→K' un foncteur'", "bold italic K, K'", "\\mathcal K, \\mathcal K'", "font", None, "high",
    r"$F:\mathcal K\to\mathcal K'$", r"$F:\boldsymbol{K}\to\boldsymbol{K}'$", KF + " Two occurrences, one edit.")
add(182, "(7.3.5.3): 'pour tout objet simple S de K'", "bold italic K", "\\mathcal K", "font", None, "high",
    r"simple $S$ de $\mathcal K$", r"simple $S$ de $\boldsymbol{K}$", KF)
add(182, "(7.3.5.3): 'un objet de longueur finie dans K'. Alors'", "bold italic K'", "\\mathcal K'", "font", None, "high",
    r"$\mathcal K'$. Alors", r"$\boldsymbol{K}'$. Alors", KF)
add(182, "(7.3.5.3): 'pour tout objet E de longueur finie dans K, F(E) est'", "bold italic K", "\\mathcal K", "font", None, "high",
    r"dans $\mathcal K$,¶$F(E)$", r"dans $\boldsymbol{K}$,¶$F(E)$", KF)
add(182, "(7.3.5.3): 'F(E) est de longueur finie dans K'. Pour toute'", "bold italic K'", "\\mathcal K'", "font", None, "high",
    r"$\mathcal K'$. Pour toute", r"$\boldsymbol{K}'$. Pour toute", KF)
add(182, "(7.3.5.3): 'Pour toute suite exacte 0→E'→E→E''→0 d'objets'", "formula in the running text (u, v over the arrows)",
    "displayed", "other", None, "high",
    r"suite exacte¶\[¶  0\longrightarrow E'\xrightarrow{u}E\xrightarrow{v}E''\longrightarrow0¶\]¶d'objets",
    r"suite exacte¶$0\longrightarrow E'\xrightarrow{u}E\xrightarrow{v}E''\longrightarrow0$¶d'objets", INL)
add(182, "(7.3.5.3): 'd'objets de longueur finie dans K, on a'", "bold italic K", "\\mathcal K", "font", None, "high",
    r"dans $\mathcal K$, on a", r"dans $\boldsymbol{K}$, on a", KF)
add(182, "(7.3.5.3): 'et pour que les deux membres de (7.3.5.4) soient égaux'", "reference (7.3.5.4) upright",
    "italic (italic lemma)", "convention", 6, "high",
    r"membres de (7.3.5.4) soient", r"membres de \textup{(7.3.5.4)} soient", REF)
add(182, "proof of (7.3.5.3): 'En effet, la suite F(E')→F(E)→F(E'') est exacte'", "formula in the running text",
    "displayed", "other", None, "high",
    r"la suite¶\[¶  F(E')\xrightarrow{F(u)}F(E)\xrightarrow{F(v)}F(E'')¶\]¶est exacte",
    r"la suite¶$F(E')\xrightarrow{F(u)}F(E)\xrightarrow{F(v)}F(E'')$¶est exacte", INL)
add(182, "end of p. 182, after (7.3.5.5) / top of p. 183: 'Par récurrence sur la longueur de E'",
    "p. 183 begins a new indented paragraph 'Par récurrence …'",
    "no blank line between the display (7.3.5.5) and \\oldpage[III]{183}: the text runs on without indent", "other", None, "high",
    r"\label{III.7.3.5.5.fr}¶\]¶", r"\label{III.7.3.5.5.fr}¶\]¶¶",
    "The difference shows at the top of p. 183; the edit is the last line of p. 182's segment (blank line before the p. 183 marker, as at other page starts).")

# ---------------------------------------------------------------- p. 183
add(183, "proof of (7.3.5.3): 'ne peuvent être égaux que si long Im(F(u))=long F(E') (ce qui'",
    "formula in the running text", "displayed", "other", None, "high",
    r"égaux que si¶\[¶  \operatorname{long}\operatorname{Im}(F(u))=\operatorname{long}F(E')¶\]¶(ce qui",
    r"égaux que si¶$\operatorname{long}\operatorname{Im}(F(u))=\operatorname{long}F(E')$¶(ce qui", INL)
add(183, "proof of (7.3.5.3): 'et long Im(F(v))=long F(E'') (ce qui'", "formula in the running text", "displayed", "other", None,
    "high",
    r"=0$) et¶\[¶  \operatorname{long}\operatorname{Im}(F(v))=\operatorname{long}F(E'')¶\]¶(ce qui",
    r"=0$) et¶$\operatorname{long}\operatorname{Im}(F(v))=\operatorname{long}F(E'')$¶(ce qui", INL)
add(183, "after (7.3.5.6): 'En outre, il résulte de (7.3.5.3)'", "new indented paragraph",
    "no blank line after the display: runs on without indent", "other", None, "high",
    r"\label{III.7.3.5.6.fr}¶\]¶En outre", r"\label{III.7.3.5.6.fr}¶\]¶¶En outre", "Paragraph break as printed.")
add(183, "(7.3.5.7): 'La relation long T_p(A)=d.long A entraîne'", "formula in the running text", "displayed", "other", None,
    "high",
    r"La relation¶\[¶  \operatorname{long}T_p(A)=d\mathbin{.}\operatorname{long}A¶\]¶entraîne",
    r"La relation¶$\operatorname{long}T_p(A)=d\mathbin{.}\operatorname{long}A$¶entraîne", INL)
add(183, "proof of (7.3.5.7): 'partant de la suite exacte 0→m→A→k→0, il résulte'", "formula in the running text",
    "displayed (comma inside the display)", "other", None, "high",
    r"suite exacte¶\[¶  0\longrightarrow\mathfrak m\longrightarrow A\longrightarrow k¶  \longrightarrow0,¶\]¶il résulte",
    r"suite exacte¶$0\longrightarrow\mathfrak m\longrightarrow A\longrightarrow k\longrightarrow0$,¶il résulte", INL)
add(183, "proof of (7.3.5.7): 'T_p est isomorphe à un foncteur M⇝N⊗_A M'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$M\mapsto N\otimes_A M$", r"$M\leadsto N\otimes_A M$", WAVY)
add(183, "proof of (7.3.5.7): '(0, 10.1.3)'", "bold 0", "plain 0", "convention", 2, "high",
    r"plat (0, 10.1.3)", r"plat (\textbf{0}, 10.1.3)", "Bold chapter number in the reference.")
add(183, "(7.3.6): 'covariant de Ab_A dans Ab'", "bold italic Ab (twice)", "\\mathbf{Ab}_A, \\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$, commutant aux sommes directes. Supposons",
    r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$, commutant aux sommes directes. Supposons",
    ABF + " Two occurrences, one edit." + ABS)
add(183, "(7.3.7): 'covariant de Ab_A dans Ab'", "bold italic Ab (twice)", "\\mathbf{Ab}_A, \\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$, commutant aux sommes directes. On suppose",
    r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$, commutant aux sommes directes. On suppose",
    ABF + " Two occurrences, one edit." + ABS)
add(183, "(7.3.7) a): 'T_q est exact pour q⩽p;'", "semicolon after a)", "full stop", "punctuation", None, "high",
    r"$T_q$ est exact pour $q\leq p$.", r"$T_q$ est exact pour $q\leq p$;", "Item b) ends with a full stop in the print.")
add(183, "(7.3.7) c): 'l'homomorphisme canonique T_q(A_s)⊗_A M→T_q(M) est surjectif'", "formula in the running text",
    "displayed", "other", None, "high",
    r"canonique¶    \[¶      T_q(A_s)\otimes_A M\longrightarrow T_q(M)¶    \]¶    est surjectif",
    r"canonique¶    $T_q(A_s)\otimes_A M\longrightarrow T_q(M)$¶    est surjectif", INL)

# ---------------------------------------------------------------- p. 184
add(184, "(7.3.8): 'covariant de Ab_A dans Ab, il résulte'", "bold italic Ab (twice)", "\\mathbf{Ab}_A, \\mathbf{Ab}", "font",
    None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$, il résulte",
    r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$, il résulte", ABF + " Two occurrences, one edit.")
add(184, "(7.3.8): 'le foncteur de Ab_B dans Ab obtenu'", "bold italic Ab (twice)", "\\mathbf{Ab}_B, \\mathbf{Ab}", "font",
    None, "high",
    r"$\mathbf{Ab}_B$ dans $\mathbf{Ab}$ obtenu",
    r"$\boldsymbol{Ab}_B$ dans $\boldsymbol{Ab}$ obtenu", ABF + " Two occurrences, one edit.")
add(184, "(7.3.8): 'et que nous noterons T_•^{(B)}=(T_i^{(B)}), est encore'", "formula in the running text",
    "displayed (comma inside the display)", "other", None, "high",
    r"noterons¶\[¶  T_\bullet^{(B)}=(T_i^{(B)}),¶\]¶est encore",
    r"noterons¶$T_\bullet^{(B)}=(T_i^{(B)})$,¶est encore", INL)
add(184, "(7.3.8): 'est encore un foncteur homologique.'", "'homologique' italic", "upright", "italics", None, "high",
    r"un foncteur homologique.¶\end{env}", r"un foncteur \emph{homologique}.¶\end{env}", "")
add(184, "(7.3.9): 'vérifie les conditions générales de (7.3.7) et commute'", "reference (7.3.7) upright",
    "italic (italic corollary)", "convention", 6, "high",
    r"de (7.3.7) et¶commute aux limites inductives, et", r"de \textup{(7.3.7)} et¶commute aux limites inductives, et", REF)
add(184, "(7.3.9): 'il existe un f∈A—{0}'", "long dash", "minus sign", "convention", 7, "high",
    r"un $f\in A-\{0\}$", r"un $f\in A\setmin\{0\}$", "Set difference.")
W3 = "(7.3.9): 'tel que le foncteur T_p^{(A_f)}: Ab_{A_f}→Ab soit exact'"
add(184, W3, "formula in the running text; Ab bold italic", "displayed, \\mathbf{Ab}", "other", None, "high",
    r"le foncteur¶\[¶  T_p^{(A_f)}:\mathbf{Ab}_{A_f}\longrightarrow\mathbf{Ab}¶\]¶soit exact",
    r"le foncteur¶$T_p^{(A_f)}:\boldsymbol{Ab}_{A_f}\longrightarrow\boldsymbol{Ab}$¶soit exact",
    INL + " The fix also carries the Ab font finding reported below.")
add(184, "(7.3.9): 'Ab_{A_f}→Ab'", "bold italic Ab (twice)", "\\mathbf{Ab}", "font", None, "high", None, None,
    ABF + ABS + " " + INC.format(W3))
add(184, "proof of (7.3.9): 'de prendre f tel que T_p^{(A_f)}(A_f)=T_p(A_f) soit un'", "formula in the running text",
    "displayed", "other", None, "high",
    r"tel que¶\[¶  T_p^{(A_f)}(A_f)=T_p(A_f)¶\]¶soit un", r"tel que¶$T_p^{(A_f)}(A_f)=T_p(A_f)$¶soit un", INL)
add(184, "proof of (7.3.9): 'soit un A_f-module libre pour'", "'libre' italic", "upright", "italics", None, "high",
    r"$A_f$-module libre pour", r"$A_f$-module \emph{libre} pour", "")
add(184, "proof of (7.3.9): 'qu'un nombre fini d'indices'", "'fini' italic", "upright", "italics", None, "high",
    r"nombre fini d'indices", r"nombre \emph{fini} d'indices", "")
add(184, "proof of (7.3.9): 'il existe f∈A—{0} tel que tous'", "long dash", "minus sign", "convention", 7, "high",
    r"existe $f\in A-\{0\}$", r"existe $f\in A\setmin\{0\}$", "Set difference.")
add(184, "proof of (7.3.9): 'tel que tous les T_p^{(A_f)} soient exacts'", "'tous' italic", "upright", "italics", None, "high",
    r"tel que tous les", r"tel que \emph{tous} les", "")
add(184, "(7.3.10): 'vérifie les conditions générales de (7.3.7) et commute'", "reference (7.3.7) upright",
    "italic (italic corollary)", "convention", 6, "high",
    r"de (7.3.7) et¶commute aux limites inductives, que", r"de \textup{(7.3.7)} et¶commute aux limites inductives, que", REF)
W4 = "(7.3.10): 'la fonction x⇝rang_{k(x)}(T_p(k(x))) soit constante dans U'"
add(184, W4, "formula in the running text; wavy arrow; bold upright k in the subscript, bold italic k in T_p(k(x))",
    "displayed \\[ x\\mapsto\\operatorname{rang}_{\\kappa(x)}(T_p(\\kappa(x))) \\]", "other", None, "high",
    r"la fonction¶\[¶  x\mapsto\operatorname{rang}_{\kappa(x)}(T_p(\kappa(x)))¶\]¶soit constante",
    r"la fonction¶$x\leadsto\operatorname{rang}_{\mathbf{k}(x)}(T_p(\boldsymbol{k}(x)))$¶soit constante",
    INL + " The fix also carries the three edits reported separately below.")
add(184, "(7.3.10): 'x⇝rang', arrow", "wavy arrow ⇝", "\\mapsto", "symbol", None, "high", None, None, WAVY + " " + INC.format(W4))
add(184, "(7.3.10): 'rang_{k(x)}', subscript", "bold upright k (enlarged crop)", "\\kappa(x)", "convention", 1, "high", None,
    None, KAPPA + " Correct form: \\mathbf{k}(x). " + INC.format(W4))
add(184, "(7.3.10): 'T_p(k(x))'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " Correct form: \\boldsymbol{k}(x). " + INC.format(W4))
add(184, "proof of (7.3.10): 'Nous allons montrer par récurrence sur p⩽N'", "no comma after 'montrer'", "'montrer, par'",
    "punctuation", None, "high", r"allons montrer, par récurrence", r"allons montrer par récurrence", "Checked on an enlarged crop.")
add(184, "proof of (7.3.10): 'qu'il existe f_p∈B—{0}'", "long dash", "minus sign", "convention", 7, "high",
    r"$f_p\in B-\{0\}$", r"$f_p\in B\setmin\{0\}$", "Set difference.")
add(184, "proof of (7.3.10): 'T_i^{(B')} soit exact et'", "'exact' italic", "upright", "italics", None, "high",
    r"soit exact et¶les", r"soit \emph{exact} et¶les", "")
add(184, "proof of (7.3.10): 'des B'-modules de type fini pour i⩽p'", "'de type fini' italic", "upright", "italics", None, "high",
    r"$B'$-modules de type fini pour", r"$B'$-modules \emph{de type fini} pour", "")
add(184, "proof of (7.3.10): 'Comme on a T_i(A_{g_p})=(T_i(A))_{g_p}, les'", "formula in the running text",
    "displayed (comma inside the display)", "other", None, "high",
    r"Comme on a¶\[¶  T_i(A_{g_p})=(T_i(A))_{g_p},¶\]¶les", r"Comme on a¶$T_i(A_{g_p})=(T_i(A))_{g_p}$,¶les", INL)
add(184, "proof of (7.3.10): 'la suite exacte 0→p→A→A/p→0 donne'", "formula in the running text", "displayed", "other", None,
    "high",
    r"est exact; la suite exacte¶\[¶  0\longrightarrow\mathfrak p\longrightarrow A\longrightarrow A/\mathfrak p¶  \longrightarrow0¶\]¶donne",
    r"est exact; la suite exacte¶$0\longrightarrow\mathfrak p\longrightarrow A\longrightarrow A/\mathfrak p\longrightarrow0$¶donne",
    INL)
add(184, "proof of (7.3.10): 'donne alors la suite exacte T_{p+1}(A)→T_{p+1}(A/p)→∂T_p(p)→T_p(A), et comme'",
    "formula in the running text", "displayed (comma inside the display)", "other", None, "high",
    r"alors la suite exacte¶\[¶  T_{p+1}(A)\longrightarrow T_{p+1}(A/\mathfrak p)¶  \xrightarrow{\partial}T_p(\mathfrak p)\longrightarrow T_p(A),¶\]¶et comme",
    r"alors la suite exacte¶$T_{p+1}(A)\longrightarrow T_{p+1}(A/\mathfrak p)\xrightarrow{\partial}T_p(\mathfrak p)\longrightarrow T_p(A)$,¶et comme",
    INL)
add(184, "proof of (7.3.10): 'il y a un f_N∈B—{0}'", "long dash", "minus sign", "convention", 7, "high",
    r"$f_N\in B-\{0\}$", r"$f_N\in B\setmin\{0\}$", "Set difference.")

# ---------------------------------------------------------------- p. 185
add(185, "proof of (7.3.10): 'au cas où A est intègre'", "'intègre' italic", "upright", "italics", None, "high",
    r"où $A$ est intègre;", r"où $A$ est \emph{intègre};", "")
add(185, "proof of (7.3.10): 'l'existence d'un f∈A—{0}'", "long dash", "minus sign", "convention", 7, "high",
    r"d'un $f\in A-\{0\}$", r"d'un $f\in A\setmin\{0\}$", "Set difference.")
add(185, "proof of (7.3.10): 'des A_f-modules libres de type fini'", "'libres' italic", "upright", "italics", None, "high",
    r"$A_f$-modules libres de type fini", r"$A_f$-modules \emph{libres} de type fini", "")
add(185, "(7.3.11): 'covariant de Ab_A dans Ab'", "bold italic Ab (twice)", "\\mathbf{Ab}_A, \\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$,¶commutant",
    r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$,¶commutant", ABF + " Two occurrences, one edit." + ABS)
add(185, "(7.3.11): 'les conditions équivalentes a), b), c) de (7.3.7) impliquent'", "reference (7.3.7) upright",
    "italic (italic proposition)", "convention", 6, "high",
    r"(7.3.7) impliquent les deux", r"\textup{(7.3.7)} impliquent les deux", REF)
W5 = "(7.3.11) d): 'on a rang_{k(x)}T_q(k(x))=rang_k T_q(k) pour q⩽p.'"
add(185, W5, "formula in the running text; bold upright k in the subscript k(x), bold italic k in T_q(k(x)); plain k in rang_k",
    "displayed, \\kappa(x) twice", "other", None, "high",
    r"on a¶    \[¶      \operatorname{rang}_{\kappa(x)}T_q(\kappa(x))¶      =¶      \operatorname{rang}_kT_q(k)¶      \quad\text{pour }q\leq p.¶    \]¶",
    r"on a¶    $\operatorname{rang}_{\mathbf{k}(x)}T_q(\boldsymbol{k}(x))=\operatorname{rang}_kT_q(k)$¶    pour $q\leq p$.¶",
    INL + " The fix also carries the two residue-field k's reported below; 'pour' stays italic (statement text).")
add(185, "(7.3.11) d): 'rang_{k(x)}', subscript", "bold upright k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " Correct form: \\mathbf{k}(x). " + INC.format(W5))
add(185, "(7.3.11) d): 'T_q(k(x))'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " Correct form: \\boldsymbol{k}(x). " + INC.format(W5))
add(185, "(7.3.11) d'): 'rang_{k(x_j)}', subscript", "bold upright k (enlarged crop)", "\\kappa(x_j)", "convention", 1, "high",
    r"\operatorname{rang}_{\kappa(x_j)}T_q", r"\operatorname{rang}_{\mathbf{k}(x_j)}T_q", KAPPA)
add(185, "(7.3.11) d'): 'T_q(k(x_j))'", "bold italic k", "\\kappa(x_j)", "convention", 1, "high",
    r"(\kappa(x_j))¶      =", r"(\boldsymbol{k}(x_j))¶      =", KAPPA)
add(185, "proof of (7.3.11): 'T_q(A) est un A-module libre pour q⩽p'", "'libre' italic", "upright", "italics", None, "high",
    r"$A$-module libre pour $q\leq p$", r"$A$-module \emph{libre} pour $q\leq p$", "")
W6 = "proof of (7.3.11): 'la condition c) implique que T_q(k(x))=T_q(A)⊗_A k(x) pour q⩽p, donc'"
add(185, W6, "formula in the running text; bold italic k twice", "displayed, \\kappa(x) twice", "other", None, "high",
    r"implique que¶\[¶  T_q(\kappa(x))=T_q(A)\otimes_A\kappa(x)¶  \quad\text{pour }q\leq p,¶\]¶donc",
    r"implique que¶$T_q(\boldsymbol{k}(x))=T_q(A)\otimes_A\boldsymbol{k}(x)$ pour $q\leq p$,¶donc",
    INL + " The fix also carries the two residue-field k's reported below.")
add(185, "proof of (7.3.11): 'T_q(k(x))'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " " + INC.format(W6))
add(185, "proof of (7.3.11): 'T_q(A)⊗_A k(x)'", "bold italic k", "\\kappa(x)", "convention", 1, "high", None, None,
    KAPPA + " " + INC.format(W6))
add(185, "proof of (7.3.11): 'lorsque A est réduit'", "'réduit' italic", "upright", "italics", None, "high",
    r"est réduit. Raisonnons", r"est \emph{réduit}. Raisonnons", "")
add(185, "proof of (7.3.11): 'T_{q+1}(A) est un A-module libre.'", "'libre' italic", "upright", "italics", None, "high",
    r"$A$-module libre. En vertu", r"$A$-module \emph{libre}. En vertu", "")
add(185, "proof of (7.3.11): 'appliquant cette propriété à M=k(x_j)'", "bold italic k", "\\kappa(x_j)", "convention", 1, "high",
    r"$M=\kappa(x_j)$", r"$M=\boldsymbol{k}(x_j)$", KAPPA)
add(185, "proof of (7.3.11), display: 'rang_{k(x_j)}(…)', subscript", "bold upright k", "\\kappa(x_j)", "convention", 1, "high",
    r"\operatorname{rang}_{\kappa(x_j)}¶", r"\operatorname{rang}_{\mathbf{k}(x_j)}¶", KAPPA)
add(185, "proof of (7.3.11), display: 'T_{q+1}(A)⊗_A k(x_j)'", "bold italic k", "\\kappa(x_j)", "convention", 1, "high",
    r"\otimes_A\kappa(x_j)\bigr)", r"\otimes_A\boldsymbol{k}(x_j)\bigr)", KAPPA)
add(185, "after (7.3.11): 'ne faisant intervenir qu'un seul des T_p'", "'un seul' italic", "upright", "italics", None, "high",
    r"qu'un seul¶des", r"qu'\emph{un seul}¶des", "")
add(185, "heading 7.4: 'Critères d'exactitude pour les foncteurs H_•(P_•⊗_A M).'", "final full stop", "no full stop",
    "punctuation", None, "high", r"$H_\bullet(P_\bullet\otimes_A M)$}", r"$H_\bullet(P_\bullet\otimes_A M)$.}",
    "Same pattern as GLOBAL_ISSUES item 43.")
add(185, "(7.4.1): 'un complexe de A-modules à droite plats'", "'plats' italic", "upright", "italics", None, "high",
    r"à droite plats. Comme", r"à droite \emph{plats}. Comme", "")
add(185, "(7.4.1): 'Comme le foncteur M⇝P_k⊗_A M est alors exact'", "wavy arrow", "\\mapsto", "symbol", None, "high",
    r"$M\mapsto P_k\otimes_A M$", r"$M\leadsto P_k\otimes_A M$", WAVY)
add(185, "(7.4.1): 'est alors exact dans Ab_A pour tout k'", "bold italic Ab", "\\mathbf{Ab}_A", "font", None, "high",
    r"dans $\mathbf{Ab}_A$ pour tout $k$", r"dans $\boldsymbol{Ab}_A$ pour tout $k$", ABF)

# ---------------------------------------------------------------- p. 186
add(186, "(7.4.1), top of the page: 'est un foncteur homologique de Ab_A dans Ab'", "'foncteur homologique' italic", "upright",
    "italics", None, "high", r"est un foncteur homologique de", r"est un \emph{foncteur homologique} de", "")
add(186, "(7.4.1): 'de Ab_A dans Ab, évidemment'", "bold italic Ab (twice)", "\\mathbf{Ab}_A, \\mathbf{Ab}", "font", None, "high",
    r"$\mathbf{Ab}_A$ dans $\mathbf{Ab}$,¶évidemment",
    r"$\boldsymbol{Ab}_A$ dans $\boldsymbol{Ab}$,¶évidemment", ABF + " Two occurrences, one edit.")
add(186, "(7.4.1): 'comme on peut aussi écrire P_•⊗_A N_[ρ]=P_•⊗_A(B⊗_B N)_[ρ]=(P_•⊗_A B)⊗_B N, on voit'",
    "formula in the running text", "displayed (comma inside the display)", "other", None, "high",
    r"écrire¶\[¶  P_\bullet\otimes_A N_{[\rho]}¶  =P_\bullet\otimes_A(B\otimes_B N)_{[\rho]}¶  =(P_\bullet\otimes_A B)\otimes_B N,¶\]¶on voit",
    r"écrire¶$P_\bullet\otimes_A N_{[\rho]}=P_\bullet\otimes_A(B\otimes_B N)_{[\rho]}=(P_\bullet\otimes_A B)\otimes_B N$,¶on voit",
    INL)
add(186, "(7.4.1): 'le complexe P_•⊗_A B de B-modules plats'", "'plats' italic", "upright", "italics", None, "high",
    r"de $B$-modules plats", r"de $B$-modules \emph{plats}", "")
add(186, "(7.4.1): '(0_I, 6.2.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 6.2.1)", r"(\textbf{0}\textsubscript{I}, 6.2.1)", "Bold chapter number in the reference.")
add(186, "(7.4.2): 'Sous les conditions générales de (7.4.1), et pour'", "reference (7.4.1) upright",
    "italic (italic proposition)", "convention", 6, "high",
    r"générales de (7.4.1), et pour", r"générales de \textup{(7.4.1)}, et pour", REF)
add(186, "(7.4.2) a): '(ou, ce qui revient au même, T_{p+1} est exact à droite)'",
    "'(ou, ce qui revient au même,' roman inside the italic statement", "italic (italic proposition)", "convention", 6, "high",
    r"(ou, ce qui revient au même, $T_{p+1}$", r"\textup{(ou, ce qui revient au même,} $T_{p+1}$",
    "'est exact à droite' stays italic, as printed.")
add(186, "(7.4.2) b): 'Z'_p(P_•)=Coker(P_{p+1}→P_p) est un A-module à droite plat'", "formula in the running text",
    "displayed", "other", None, "high",
    r"\item[b)]¶    \[¶      Z'_p(P_\bullet)¶      =¶      \operatorname{Coker}(P_{p+1}\longrightarrow P_p)¶    \]¶    est un",
    r"\item[b)] $Z'_p(P_\bullet)=\operatorname{Coker}(P_{p+1}\longrightarrow P_p)$¶    est un", INL)
add(186, "(7.4.2) c): 'la différentielle d_{p+1} : P'_{p+1}→P'_p soit nulle'", "d_{p+1} without a prime (enlarged crop); P'_{p+1}, P'_p primed",
    "d'_{p+1}", "formula", None, "high",
    r"d'_{p+1}:P'_{p+1}\longrightarrow P'_p", r"d_{p+1}:P'_{p+1}\longrightarrow P'_p",
    "The TeX adds a prime the print does not have. Not recorded as a misprint: the printed notation is not wrong.")
add(186, "proof of (7.4.2): 'où Z'_p(P_•⊗M)=Coker(P_{p+1}⊗M→P_p⊗M)=Z'_p(P_•)⊗M en vertu'", "formula in the running text",
    "displayed", "other", None, "high",
    r"où¶\[¶  Z'_p(P_\bullet\otimes M)¶  =¶  \operatorname{Coker}(P_{p+1}\otimes M\longrightarrow P_p\otimes M)¶  =¶  Z'_p(P_\bullet)\otimes M¶\]¶en vertu",
    r"où¶$Z'_p(P_\bullet\otimes M)=\operatorname{Coker}(P_{p+1}\otimes M\longrightarrow P_p\otimes M)=Z'_p(P_\bullet)\otimes M$¶en vertu",
    INL)
add(186, "proof of (7.4.2), c) implies a): 'car si d_{p+1} : P_{p+1}→P_p est nulle'", "no primes: d_{p+1} : P_{p+1}→P_p (enlarged crop)",
    "$d'_{p+1}:P'_{p+1}\\to P'_p$", "formula", None, "high",
    r"$d'_{p+1}:P'_{p+1}\to P'_p$", r"$d_{p+1}:P_{p+1}\to P_p$",
    "The print argues for a complex P_• with d_{p+1}=0 (applied to P'_• through the isomorphism of c)); the TeX adds primes. "
    "Not recorded as a misprint; if the coordinator treats it as one, the corrected reading is the current TeX. Goes with the next finding.")
add(186, "proof of (7.4.2): display 'H_{p+1}(P_•⊗M'')→∂H_p(P_•⊗M')→H_p(P_•⊗M)'", "P_• without primes (three times; enlarged crop)",
    "P'_\\bullet three times", "formula", None, "high",
    r"H_{p+1}(P'_\bullet\otimes M'')¶  \xrightarrow{\partial}H_p(P'_\bullet\otimes M')¶  \longrightarrow H_p(P'_\bullet\otimes M)",
    r"H_{p+1}(P_\bullet\otimes M'')¶  \xrightarrow{\partial}H_p(P_\bullet\otimes M')¶  \longrightarrow H_p(P_\bullet\otimes M)",
    "Same notation as the preceding finding; the sentence continues on p. 187 ('est nul par définition').")

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for p in sorted({x["page"] for x in F}):
    pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
sim = dict(pages)
for i, x in enumerate(F):
    fx = x["fix"]
    if not fx:
        continue
    t = pages[x["page"]]
    c = t.count(fx["old"])
    if c != 1:
        ok = False
        print("NOT UNIQUE in original:", x["page"], c, repr(fx["old"][:80]))
    c2 = sim[x["page"]].count(fx["old"])
    if c2 != 1:
        ok = False
        print("NOT UNIQUE after earlier edits:", x["page"], c2, repr(fx["old"][:80]))
    else:
        sim[x["page"]] = sim[x["page"]].replace(fx["old"], fx["new"])
for x in F:
    if x["note"] == "":
        x["note"] = None
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in sorted(pages):
    print(p, "normal", cnt[(p, "normal")], "convention", cnt[(p, "convention")], "misprint", cnt[(p, "misprint")])
print("total", len(F), "all unique:", ok)
for p in sorted(pages):
    (RUN / "crops_182_186" / f"sim_{p}.txt").write_text(sim[p], encoding="utf-8")
