"""Build findings_096_100.json for EGA III part 1, pp. 96-100, and check every fix's "old"."""
import json
import pathlib
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_096_100.json"


def L(*lines):
    return "\n".join(lines)


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 96 ----------------
add(96, "line 2: 'il résulte de (I, 9.3.1) qu'en posant comme d'ordinaire'",
    "(I, 9.3.1) with bold I", r"(I, 9.3.1)", "convention", 2, "high",
    r"(I, 9.3.1)", r"(\textbf{I}, 9.3.1)")
add(96, "first display: 'Γ(U_{i_0i_1...i_p}, F(*)) = H^0(...) = M_{f_{i_0}f_{i_1}...f_{i_p}}.'",
    "M_{f_{i_0}f_{i_1} . . . f_{i_p}}, dots on the baseline", r"M_{f_{i_0}f_{i_1}\cdots f_{i_p}}",
    "symbol", None, "high",
    r"f_{i_1}\cdots f_{i_p}}.", r"f_{i_1}\ldots f_{i_p}}.", "Checked on a crop.")
add(96, "'On peut encore, ..., identifier M_{f_{i_0}f_{i_1}...f_{i_p}} à lim M^{(n)}'",
    "M_{f_{i_0}f_{i_1} . . . f_{i_p}}, dots on the baseline", r"M_{f_{i_0}f_{i_1}\cdots f_{i_p}}",
    "symbol", None, "high",
    r"\cdots f_{i_p}}$ à", r"\ldots f_{i_p}}$ à", "Checked on a crop.")
add(96, "'Cette identification est un isomorphisme de S-modules gradués, si l'on définit'",
    "'gradués' in italics", "gradués upright", "italics", None, "high",
    r"de $S$-modules gradués, si", r"de $S$-modules \emph{gradués}, si")
add(96, "'on prend alors pour degré de z le nombre m-n(d_{i_0}+d_{i_1}+...+d_{i_p})'",
    "d_{i_1} + . . . + d_{i_p}, dots on the baseline", r"d_{i_1}+\cdots+d_{i_p}", "symbol", None, "high",
    r"d_{i_1}+\cdots+d_{i_p}", r"d_{i_1}+\ldots+d_{i_p}", "Checked on a crop.")
add(96, "'Tenant compte de la définition des homomorphismes φ_{kh} : M^{(h)}_{i_0i_1...i_p} → M^{(k)}_{i_0i_1...i_p} (1.2.2)'",
    "φ_{kh} : M^{(h)}_{i_0i_1...i_p} → M^{(k)}_{i_0i_1...i_p}",
    r"\varphi_{kn}:M_{i_0i_1\ldots i_p}^{(n)}\to M_{i_0i_1\ldots i_p}^{(k)}", "formula", None, "high",
    r"\varphi_{kn}:M_{i_0i_1\ldots i_p}^{(n)}\to", r"\varphi_{kh}:M_{i_0i_1\ldots i_p}^{(h)}\to",
    "Checked on a 2x crop: index h (not n) in both places. Not a misprint: h, k are free indices, as φ_{nm} in (1.2.2).")
add(96, "'une structure de S-module gradué sur lim C^p_n(M)'",
    "'gradué' in italics", "gradué upright", "italics", None, "high",
    r"de $S$-module gradué sur", r"de $S$-module \emph{gradué} sur")
add(96, "after (2.1.2.3): 'l'isomorphisme conservant les degrés : le degré d'un élément'",
    "'conservant les degrés' in italics", "upright", "italics", None, "high",
    r"l'isomorphisme conservant les degrés~:", r"l'isomorphisme \emph{conservant les degrés}~:")
add(96, "'dont les valeurs g(i_0, ..., i_p) sont dans une même composante homogène M_m de M'",
    "'même' in italics", "même upright", "italics", None, "high",
    r"dans une même composante", r"dans une \emph{même} composante")
add(96, "'est m-n(d_{i_0}+...+d_{i_p}), et il est indépendant'",
    "d_{i_0} + . . . + d_{i_p}, dots on the baseline", r"d_{i_0}+\cdots+d_{i_p}", "symbol", None, "high",
    r"d_{i_0}+\cdots+d_{i_p}", r"d_{i_0}+\ldots+d_{i_p}", "Checked on a crop.")

# ---------------- page 97 ----------------
add(97, "(2.1.4.1), end: 'pour p ⩾ 1'",
    "no punctuation after 'pour p⩾1'", r"\text{pour }p\geq1,", "punctuation", None, "high",
    L(r"p\geq1,", r"\end{equation}", r"et une suite exacte fonctorielle en $\mathcal F$"),
    L(r"p\geq1", r"\end{equation}", r"et une suite exacte fonctorielle en $\mathcal F$"),
    "Checked on a crop: no comma.")
add(97, "(2.1.4.2), end: '→ H^1((f), M) → 0'",
    "no punctuation after the final 0", r"\longrightarrow0,", "punctuation", None, "high",
    L(r"F(*))", r"\longrightarrow H^1((\mathbf f),M)\longrightarrow0,"),
    L(r"F(*))", r"\longrightarrow H^1((\mathbf f),M)\longrightarrow0"),
    "Checked on a crop: no comma.")
add(97, "Prop. (2.1.5): 'posons U_i = D_+(f_i), U = ∪U_i, H^·(U, M̃(*)) = ⊕_{n∈Z} H^·(U, (M(n))~). Il existe alors'",
    "formula set inline in the text line", "displayed with \\[ ... \\]", "other", None, "high",
    L(r"\[", r"H^\bullet(U,\widetilde M(*))", r"=\bigoplus_{n\in\mathbb Z}H^\bullet(U,(M(n))^\sim).", r"\]"),
    L(r"$H^\bullet(U,\widetilde M(*))", r"=\bigoplus_{n\in\mathbb Z}H^\bullet(U,(M(n))^\sim)$."),
    "Checked on a crop: 'Il existe' follows on the same line.")
add(97, "(2.1.5.1), end: 'pour p ⩾ 1'",
    "no punctuation after 'pour p⩾1'", r"\text{pour }p\geq1,", "punctuation", None, "high",
    L(r"p\geq1,", r"\end{equation}", r"et une suite exacte fonctorielle en $M$"),
    L(r"p\geq1", r"\end{equation}", r"et une suite exacte fonctorielle en $M$"),
    "Checked on a crop: no comma.")
add(97, "(2.1.5.2), end: '→ H^1((f), M) → 0'",
    "no punctuation after the final 0", r"\longrightarrow0,", "punctuation", None, "high",
    L(r"M(*))", r"\longrightarrow H^1((\mathbf f),M)\longrightarrow0,"),
    L(r"M(*))", r"\longrightarrow H^1((\mathbf f),M)\longrightarrow0"),
    "Checked on a crop: no comma.")
add(97, "proof of (2.1.5): 'En effet, on a Γ(U_{i_0i_1...i_p}, (M(n))~) = (M_{f_{i_0}...f_{i_p}})_n par définition'",
    "formula inline in the text line; (M_{f_{i_0} . . . f_{i_p}})_n with baseline dots",
    r"displayed with \[ ... \]; \cdots", "other", None, "high",
    L(r"\[", r"\Gamma(U_{i_0i_1\ldots i_p},(M(n))^\sim)", r"=(M_{f_{i_0}\cdots f_{i_p}})_n", r"\]"),
    L(r"$\Gamma(U_{i_0i_1\ldots i_p},(M(n))^\sim)", r"=(M_{f_{i_0}\ldots f_{i_p}})_n$"),
    "One edit for two differences: display to inline, and \\cdots to \\ldots (baseline dots, checked on a crop).")
add(97, "proof of (2.1.5): 'par définition (II, 2.5.2), donc'",
    "(II, 2.5.2) with bold II", r"(II, 2.5.2)", "convention", 2, "high",
    r"(II, 2.5.2)", r"(\textbf{II}, 2.5.2)")
add(97, "proof of (2.1.5): 'donc Γ(U_{i_0i_1...i_p}, M̃(*)) = M_{f_{i_0}...f_{i_p}}.'",
    "M_{f_{i_0} . . . f_{i_p}}, dots on the baseline", r"M_{f_{i_0}\cdots f_{i_p}}", "symbol", None, "high",
    r"=M_{f_{i_0}\cdots f_{i_p}}$", r"=M_{f_{i_0}\ldots f_{i_p}}$", "Checked on a crop.")
add(97, "Remarques (2.1.6) (i): 'sont exacts en M, en vertu de (0_I, 1.3.2)'",
    "(0_I, 1.3.2) with bold 0", r"(0\textsubscript{I}, 1.3.2)", "convention", 2, "high",
    r"(0\textsubscript{I}, 1.3.2)", r"(\textbf{0}\textsubscript{I}, 1.3.2)")
add(97, "diagram (2.1.6.1), top left: 'H^p(U, M̃''(*))'",
    "tilde over M only, the primes outside it: M̃''", r"\widetilde {M''}", "convention", 8, "high",
    r"\widetilde {M''}(*)", r"\widetilde{M}''(*)", "Checked on a 2x crop.")
add(97, "diagram (2.1.6.1), top right: 'H^{p+1}(U, M̃'(*))'",
    "tilde over M only, the prime outside it: M̃'", r"\widetilde {M'}", "convention", 8, "high",
    r"\widetilde {M'}(*)", r"\widetilde{M}'(*)", "Checked on a 2x crop.")
add(97, "diagram (2.1.6.1), bottom arrow H^{p+1}((f), M'') → H^{p+2}((f), M')",
    "∂ set below the bottom arrow (above the top arrow)", r"\ar[r]^-\partial (label above) on both rows",
    "symbol", None, "high",
    r"M'')\ar[r]^-\partial", r"M'')\ar[r]_-\partial", "Checked on a crop.")
add(97, "diagram (2.1.6.1), end of the bottom row: 'H^{p+2}((f), M')'",
    "no full stop after the diagram", r"H^{p+2}((\mathbf f),M').", "punctuation", None, "high",
    r"H^{p+2}((\mathbf f),M').", r"H^{p+2}((\mathbf f),M')", "Checked on a crop.")

# ---------------- page 98 ----------------
add(98, "line 1: 'lorsqu'il en est ainsi, tout O_X-Module quasi-cohérent est de la forme M̃'",
    "'tout' in italics", "tout upright", "italics", None, "high",
    r"ainsi, tout $\mathcal O_X$-Module", r"ainsi, \emph{tout} $\mathcal O_X$-Module", "Checked on a crop.")
add(98, "line 1: 'est de la forme M̃ (II, 2.7.7).'",
    "(II, 2.7.7) with bold II", r"(II, 2.7.7)", "convention", 2, "high",
    r"(II, 2.7.7)", r"(\textbf{II}, 2.7.7)")
add(98, "Lemme (2.1.8), first line: 'on a, avec T = (T_i)_{0⩽i⩽r}' before (2.1.8.1)",
    "no comma after (T_i)_{0⩽i⩽r}", r"$\mathbf T=(T_i)_{0\leq i\leq r}$,", "punctuation", None, "high",
    L(r"$\mathbf T=(T_i)_{0\leq i\leq r}$,", r"\begin{align}"),
    L(r"$\mathbf T=(T_i)_{0\leq i\leq r}$", r"\begin{align}"),
    "Checked on a crop.")
add(98, "(2.1.8.1), end: 'si i ≠ r+1'",
    "no punctuation after r+1", r"\text{si }i\neq r+1,", "punctuation", None, "high",
    r"H^i(\mathbf T^n,S)&=0 &&\text{si }i\neq r+1,\\", r"H^i(\mathbf T^n,S)&=0 &&\text{si }i\neq r+1\\",
    "Checked on a crop.")
add(98, "Lemme (2.1.8), last sentence: 'des monômes T_p = T_0^{p_0} ... T_r^{p_r} avec p = (p_0, ..., p_r), 0 ⩽ p_i < n pour tout i.'",
    "inline: bold T_p (T bold like the family T, p bold) = T_0^{p_0} . . . T_r^{p_r} (baseline dots), then the word 'avec', then p = (p_0, ..., p_r), 0⩽p_i<n pour tout i.",
    r"displayed; T_{\mathbf p} with plain T; \cdots; ',\qquad' where the print has 'avec'", "missing", None, "high",
    L(r"des monômes", r"\[", r"T_{\mathbf p}=T_0^{p_0}\cdots T_r^{p_r},",
      r"\qquad \mathbf p=(p_0,\ldots,p_r),\quad 0\leq p_i<n", r"\quad\text{pour tout }i.", r"\]"),
    L(r"des monômes", r"$\mathbf T_{\mathbf p}=T_0^{p_0}\ldots T_r^{p_r}$ avec",
      r"$\mathbf p=(p_0,\ldots,p_r)$, $0\leq p_i<n$ pour tout $i$."),
    "One edit for four differences in the same span: missing word 'avec', display to inline, bold T in T_p, \\cdots to \\ldots. Checked on a crop.")
add(98, "(2.1.9): 'l'homomorphisme φ_{nm} : S/(T^n) → S/(T^m) pour 0 ⩽ n ⩽ m étant la multiplication'",
    "inline, and 'pour 0⩽n⩽m' (word 'pour', no parentheses)",
    r"displayed, with '\qquad(0\leq n\leq m)'", "missing", None, "high",
    L(r"l'homomorphisme", r"\[", r"\varphi_{nm}:S/(\mathbf T^n)\longrightarrow S/(\mathbf T^m)",
      r"\qquad(0\leq n\leq m)", r"\]"),
    L(r"l'homomorphisme", r"$\varphi_{nm}:S/(\mathbf T^n)\longrightarrow S/(\mathbf T^m)$", r"pour $0\leq n\leq m$"),
    "One edit: missing word 'pour' (TeX has parentheses instead) and display to inline. Checked on a crop.")
add(98, "(2.1.9): 'étant la multiplication par (T_0 ... T_r)^{m-n}'",
    "(T_0 . . . T_r), dots on the baseline", r"(T_0\cdots T_r)", "symbol", None, "high",
    r"(T_0\cdots T_r)^{m-n}", r"(T_0\ldots T_r)^{m-n}", "Checked on a crop.")
add(98, "(2.1.9): 'désignons par ξ_p^{(n)} = ξ^{(n)}_{p_0...p_r} la classe de'",
    "subscript p_0 . . . p_r without commas", r"\xi_{p_0,\ldots,p_r}^{(n)}", "formula", None, "high",
    r"\xi_{p_0,\ldots,p_r}^{(n)}", r"\xi_{p_0\ldots p_r}^{(n)}", "Checked on a crop.")
add(98, "(2.1.9): 'la classe de T_0^{n-p_0} ... T_r^{n-p_r} mod.(T^n)'",
    "T_0^{n-p_0} . . . T_r^{n-p_r}, dots on the baseline", r"T_0^{n-p_0}\cdots T_r^{n-p_r}", "symbol", None, "high",
    r"T_0^{n-p_0}\cdots T_r^{n-p_r}", r"T_0^{n-p_0}\ldots T_r^{n-p_r}", "Checked on a crop.")
add(98, "(2.1.9): 'la classe de T_0^{n-p_0} ... T_r^{n-p_r} mod.(T^n); on a alors'",
    "'mod.(T^n)': mod with a full stop, no parentheses around it",
    r"\pmod{(\mathbf T^n)} (typesets '(mod (T^n))')", "formula", None, "high",
    r"\pmod{(\mathbf T^n)}", r"\ \mathrm{mod.}(\mathbf T^n)", "Checked on a crop.")
add(98, "(2.1.9): 'même image canonique ξ_p = ξ_{p_0...p_r} dans la limite inductive'",
    "subscript p_0 . . . p_r without commas", r"\xi_{p_0,\ldots,p_r}", "formula", None, "high",
    r"\xi_{\mathbf p}=\xi_{p_0,\ldots,p_r}$", r"\xi_{\mathbf p}=\xi_{p_0\ldots p_r}$", "Checked on a crop.")
add(98, "(2.1.9): 'est donc égal à -|p| = -(p_0+p_1+...+p_r)'",
    "p_1 + . . . + p_r, dots on the baseline", r"p_1+\cdots+p_r", "symbol", None, "high",
    r"p_1+\cdots+p_r", r"p_1+\ldots+p_r", "Checked on a crop.")
add(98, "(2.1.10.1), end: 'pour i ≠ r+1'",
    "no punctuation after r+1", r"\text{pour }i\neq r+1,", "punctuation", None, "high",
    r"\text{pour }i\neq r+1,", r"\text{pour }i\neq r+1", "Checked on a crop.")
add(98, "Corollaire (2.1.10): 'une base est formée des éléments ξ_{p_0...p_r} tels que p_i>0'",
    "subscript p_0 . . . p_r without commas", r"\xi_{p_0,\ldots,p_r}", "formula", None, "high",
    r"des éléments $\xi_{p_0,\ldots,p_r}$", r"des éléments $\xi_{p_0\ldots p_r}$", "Checked on a crop.")
add(98, "(2.1.11.1), end: 'si i ≠ r+1'",
    "no punctuation after r+1", r"\text{si }i\neq r+1,", "punctuation", None, "high",
    r"H^i(\mathbf T^n,M)&=0 &&\text{si }i\neq r+1,\\", r"H^i(\mathbf T^n,M)&=0 &&\text{si }i\neq r+1\\",
    "Checked on a crop.")
add(98, "(2.1.11.2), end: '= (S/(T^n)) ⊗_A N'",
    "no punctuation after N", r"\otimes_A N,", "punctuation", None, "high",
    L(r"\otimes_A N,", r"\end{align}"), L(r"\otimes_A N", r"\end{align}"), "Checked on a crop.")
add(98, "Remarque (2.1.11): 'il est clair que M/(T_0^nM+...+T_{i-1}^nM) s'identifie au produit tensoriel (S/(T_0^nS+...+T_{i-1}^nS))⊗_A N,'",
    "inline; words 's'identifie au produit tensoriel' between the two formulas; baseline dots; ordinary parentheses",
    r"displayed; '=' instead of the words; \cdots; \bigl( \bigr)", "missing", None, "high",
    L(r"il est clair que", r"\[", r"M/(T_0^nM+\cdots+T_{i-1}^nM)",
      r"=\bigl(S/(T_0^nS+\cdots+T_{i-1}^nS)\bigr)\otimes_A N,", r"\]"),
    L(r"il est clair que", r"$M/(T_0^nM+\ldots+T_{i-1}^nM)$", r"s'identifie au produit tensoriel",
      r"$(S/(T_0^nS+\ldots+T_{i-1}^nS))\otimes_A N$,"),
    "One edit: missing words 's'identifie au produit tensoriel' (TeX '='), display to inline, \\cdots to \\ldots (twice). Checked on a crop.")
add(98, "Remarque (2.1.11): 'l'idéal T_0^nS+...+T_{i-1}^nS étant facteur direct'",
    "T_0^nS + . . . + T_{i-1}^nS, dots on the baseline", r"\cdots", "symbol", None, "high",
    r"$T_0^nS+\cdots+T_{i-1}^nS$ étant", r"$T_0^nS+\ldots+T_{i-1}^nS$ étant", "Checked on a crop.")
add(98, "Prop. (2.1.12): 'et X = P^r_A (II, 4.1.1). Alors :'",
    "(II, 4.1.1) with bold II", r"(II, 4.1.1)", "convention", 2, "high",
    r"(II, 4.1.1)", r"(\textbf{II}, 4.1.1)", "The P of P^r_A is bold upright here (matches \\mathbf P; no convention 10).")
add(98, "Prop. (2.1.12) (ii): 'α : S → H^0(X, O_X(*)) (II, 2.6.2) est bijectif'",
    "(II, 2.6.2) with bold II", r"(II, 2.6.2)", "convention", 2, "high",
    r"(II, 2.6.2)", r"(\textbf{II}, 2.6.2)")

# ---------------- page 99 ----------------
add(99, "Prop. (2.1.12) (iii): 'une base formée d'éléments ξ_{p_0...p_r}, où p_i>0'",
    "subscript p_0 . . . p_r without commas", r"\xi_{p_0,\ldots,p_r}", "formula", None, "high",
    r"d'éléments $\xi_{p_0,\ldots,p_r}$", r"d'éléments $\xi_{p_0\ldots p_r}$", "Checked on a crop.")
add(99, "Prop. (2.1.12) (iii): 'pour 0⩽i⩽r, ξ_{p_0...p_r} étant de degré'",
    "subscript p_0 . . . p_r without commas", r"\xi_{p_0,\ldots,p_r}", "formula", None, "high",
    r"$\xi_{p_0,\ldots,p_r}$ étant de degré", r"$\xi_{p_0\ldots p_r}$ étant de degré", "Checked on a crop.")
add(99, "Prop. (2.1.12) (iii): '-|p| = -(p_0+...+p_r)'",
    "p_0 + . . . + p_r, dots on the baseline", r"p_0+\cdots+p_r", "symbol", None, "high",
    r"-(p_0+\cdots+p_r)", r"-(p_0+\ldots+p_r)", "Checked on a crop.")
add(99, "Prop. (2.1.12) (iii): 'et le produit T_i ξ_{p_0...p_r} étant'",
    "subscript p_0 . . . p_r without commas", r"T_i\xi_{p_0,\ldots,p_r}", "formula", None, "high",
    r"T_i\xi_{p_0,\ldots,p_r}", r"T_i\xi_{p_0\ldots p_r}",
    "Checked on a crop. The last one, ξ_{p_0,...,p_i-1,...,p_r}, has commas in the print, as in the TeX.")
add(99, "proof of (2.1.12): 'dans la suite exacte (2.1.5.2) appliquée à M = S = A[T_0, ..., T_r], on a'",
    "M = S = A[T_0, . . ., T_r], set as a centred display", "inline $...$", "other", None, "high",
    L(r"appliquée à", r"$M=S=A[T_0,\ldots,T_r]$, on a"),
    L(r"appliquée à", r"\[", r"M=S=A[T_0,\ldots,T_r],", r"\]", r"on a"),
    "Checked on a crop: the formula stands alone on a centred line.")
add(99, "proof of (2.1.12): 'puisque X est réunion des D_+(T_i) (II, 2.3.14)'",
    "(II, 2.3.14) with bold II", r"(II, 2.3.14)", "convention", 2, "high",
    r"(II, 2.3.14)", r"(\textbf{II}, 2.3.14)")
add(99, "proof of (2.1.12): 'l'application S → H^0(X, O_X(*)) de la suite exacte (2.1.5.1) et l'application canonique α'",
    "(2.1.5.1)", r"(\hyperref[III.2.1.5.2-fr]{2.1.5.2}) (silently corrected)", "misprint_in_print", None, "high",
    r"(\hyperref[III.2.1.5.2-fr]{2.1.5.2}) et l'application", r"(\hyperref[III.2.1.5.1-fr]{2.1.5.1}) et l'application",
    "Checked on a crop: the print reads (2.1.5.1). The map S → H^0 belongs to the exact sequence (2.1.5.2); (2.1.5.1) is the isomorphism H^p ≅ H^{p+1} for p⩾1, not an exact sequence, and the same sentence cites (2.1.5.2) for the sequence two lines earlier. The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"(\hyperref[III.2.1.5.2-fr]{2.1.5.2})")
add(99, "Corollaire (2.1.13): 'i = 0 et n ⩾ 0, i = r et n ⩽ -(r+1).'",
    "the second 'et' (between i=r and n⩽-(r+1)) upright roman; the first 'et' italic",
    "both italic (corollary environment)", "convention", 6, "high",
    r"$i=r$ et $n\leq-(r+1)$.", r"$i=r$ \textup{et} $n\leq-(r+1)$.",
    "Checked on a crop. In (2.1.15) the corresponding 'et' is italic in the print (no change there).")
add(99, "Prop. (2.1.15): 'X = P(E) le fibré projectif défini par E, f : X → Y'",
    "roman capital E (not script) after 'défini par'", r"$\mathcal E$ (silently corrected)", "misprint_in_print", None, "high",
    L(r"défini", r"par $\mathcal E$,"), L(r"défini", r"par $E$,"),
    "Checked on a crop: script ℰ in P(ℰ) just before, roman E here; the bundle is defined by the sheaf ℰ (E is only introduced in the proof, ℰ = Ẽ). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"$\mathcal E$")
add(99, "Prop. (2.1.15): 'en outre, l'homomorphisme canonique (II, 3.3.2)'",
    "(II, 3.3.2) with bold II", r"(II, 3.3.2)", "convention", 2, "high",
    r"(II, 3.3.2)", r"(\textbf{II}, 3.3.2)")
add(99, "Prop. (2.1.15), display: 'α : S_{O_Y}(E) → Γ_*(O_X) = ...'",
    "bold S (symmetric algebra S_{O_Y}(E))", r"S_{\mathcal O_Y}(\mathcal E)", "font", None, "high",
    r"\alpha:S_{\mathcal O_Y}(\mathcal E)", r"\alpha:\mathbf S_{\mathcal O_Y}(\mathcal E)", "Checked on a crop.")
add(99, "Prop. (2.1.15), display: '→ Γ_*(O_X) = R^0f_*(O_X(*))'",
    "bold Γ in Γ_*(O_X)", r"\Gamma_*", "font", None, "high",
    r"\longrightarrow\Gamma_*(\mathcal O_X)", r"\longrightarrow\bbGamma_*(\mathcal O_X)",
    "Checked on a crop. The graded O_Y-Algebra Γ_*(O_X) of (II, 3.3.1); \\bbGamma as in the EGA II page fixes (global item 24).")
add(99, "Remarque (2.1.16): 'posons ω = f^*(∧^{r+1} E)(-r-1), qui est un O_X-Module inversible'",
    "formula set inline in the text line", "displayed with \\[ ... \\], \\left( \\right)", "other", None, "high",
    L(r"posons", r"\[", r"\boldsymbol\omega=f^*\left(\bigwedge^{r+1}\mathcal E\right)(-r-1),", r"\]"),
    L(r"posons", r"$\boldsymbol\omega=f^*(\bigwedge^{r+1}\mathcal E)(-r-1)$,"),
    "Checked on a crop: 'qui est un' follows on the same line.")
add(99, "Remarque (2.1.16) (ii): 'L'accouplement par cup-produit (0, 12.2.2)'",
    "(0, 12.2.2) with bold 0", r"(0, 12.2.2)", "convention", 2, "high",
    r"(0, 12.2.2)", r"(\textbf{0}, 12.2.2)")
add(99, "Remarque (2.1.16) (ii), last display: '(∧^{r+1} E) ⊗_{O_Y} (S_{O_Y}(E))_{-n}.'",
    "bold S", r"S_{\mathcal O_Y}(\mathcal E)", "font", None, "high",
    r"\bigl(S_{\mathcal O_Y}(\mathcal E)\bigr)_{-n}", r"\bigl(\mathbf S_{\mathcal O_Y}(\mathcal E)\bigr)_{-n}",
    "Checked on a crop.")
add(99, "end of the page segment: \\subsection{Le théorème fondamental des morphismes projectifs} + \\label",
    "the heading '2.2. Le théorème fondamental des morphismes projectifs.' is the first line of printed page 100",
    r"heading stands before \oldpage[III]{100}", "marker", None, "high",
    L(r"\subsection{Le théorème fondamental des morphismes projectifs}", r"\label{subsection:III.2.2-fr}", ""),
    "",
    "Removes the heading here; the page-100 finding 'marker' puts it back right after \\oldpage[III]{100}. Apply both edits together.")

# ---------------- page 100 ----------------
add(100, "page start: \\oldpage[III]{100}",
    "page 100 begins with the heading '2.2. Le théorème fondamental des morphismes projectifs.'",
    r"marker placed after the \subsection heading", "marker", None, "high",
    L(r"\oldpage[III]{100}", ""),
    L(r"\oldpage[III]{100}", r"\subsection{Le théorème fondamental des morphismes projectifs}",
      r"\label{subsection:III.2.2-fr}", ""),
    "Puts the heading after the marker; goes with the page-99 edit that removes it before the marker. Apply both together.")
add(100, "Théorème (2.2.1): 'posons F(n) = F ⊗_{O_X} L^{⊗n} pour tout n∈Z. Alors,'",
    "formula and 'pour tout n∈Z' inline in the text line", "displayed with \\[ ... \\]", "other", None, "high",
    L(r"posons", r"\[", r"\mathcal F(n)=\mathcal F\otimes_{\mathcal O_X}\mathcal L^{\otimes n}",
      r"\qquad\text{pour tout }n\in\mathbb Z.", r"\]"),
    L(r"posons", r"$\mathcal F(n)=\mathcal F\otimes_{\mathcal O_X}\mathcal L^{\otimes n}$", r"pour tout $n\in\mathbb Z$."),
    "Checked on a crop.")
add(100, "Théorème (2.2.1) (ii): 'on ait R^qf_*(F(n)) = 0 pour tout q>0.'",
    "inline in the item's text line", "displayed with \\[ ... \\]", "other", None, "high",
    L(r"on ait", r"\[", r"R^qf_*(\mathcal F(n))=0\qquad\text{pour tout }q>0.", r"\]"),
    L(r"on ait", r"$R^qf_*(\mathcal F(n))=0$ pour tout $q>0$."),
    "Checked on the strip.")
add(100, "Théorème (2.2.1) (iii): 'l'homomorphisme canonique f^*(f_*(F(n))) → F(n) soit surjectif.'",
    "inline in the item's text line", "displayed with \\[ ... \\]", "other", None, "high",
    L(r"l'homomorphisme canonique", r"\[", r"f^*(f_*(\mathcal F(n)))\longrightarrow\mathcal F(n)", r"\]",
      r"soit surjectif."),
    L(r"l'homomorphisme canonique", r"$f^*(f_*(\mathcal F(n)))\longrightarrow\mathcal F(n)$", r"soit surjectif."),
    "Checked on the strip.")
add(100, "proof of (2.2.1): 'on peut alors écrire F(n) = (F⊗L^{⊗r})⊗L^{⊗hd} avec un h>0'",
    "formula inline in the text line", "displayed with \\[ ... \\]", "other", None, "high",
    L(r"écrire", r"\[", r"\mathcal F(n)", r"=(\mathcal F\otimes\mathcal L^{\otimes r})",
      r"\otimes\mathcal L^{\otimes hd}", r"\]", r"avec"),
    L(r"écrire", r"$\mathcal F(n)", r"=(\mathcal F\otimes\mathcal L^{\otimes r})",
      r"\otimes\mathcal L^{\otimes hd}$", r"avec"),
    "Checked on the strip.")
add(100, "proof of (2.2.1): 'On peut donc supposer L très ample relativement à f'",
    "'très ample' in italics", "upright", "italics", None, "high",
    r"$\mathcal L$ très ample relativement", r"$\mathcal L$ \emph{très ample} relativement", "Checked on a crop.")
add(100, "proof of (2.2.1): 'relativement à f (II, 4.6.11)'",
    "(II, 4.6.11) with bold II", r"(II, 4.6.11)", "convention", 2, "high",
    r"(II, 4.6.11)", r"(\textbf{II}, 4.6.11)")
add(100, "proof of (2.2.1): 'L est isomorphe à i^*(O_P(1)) (II, 4.4.7)'",
    "(II, 4.4.7) with bold II", r"(II, 4.4.7)", "convention", 2, "high",
    r"(II, 4.4.7)", r"(\textbf{II}, 4.4.7)")
add(100, "proof of (2.2.1): 'il en est de même de i (II, 5.4.4)'",
    "(II, 5.4.4) with bold II", r"(II, 5.4.4)", "convention", 2, "high",
    r"(II, 5.4.4)", r"(\textbf{II}, 5.4.4)")
add(100, "proof of (2.2.1): 'donc i est un isomorphisme X ⥲ P'",
    "'isomorphisme' in italics", "upright", "italics", None, "high",
    r"est un isomorphisme $X\xrightarrow{\sim}P$", r"est un \emph{isomorphisme} $X\xrightarrow{\sim}P$",
    "Checked on a crop.")
add(100, "proof of (2.2.2) => (2.2.1): '(tenant compte de (1.4.11) et de (II, 3.4.7))'",
    "(II, 3.4.7) with bold II", r"(II, 3.4.7)", "convention", 2, "high",
    r"(II, 3.4.7)", r"(\textbf{II}, 3.4.7)")
add(100, "'X s'identifie à un sous-schéma fermé de P = P^r_A (II, 3.6.2)'",
    "(II, 3.6.2) with bold II", r"(II, 3.6.2)", "convention", 2, "high",
    r"(II, 3.6.2)", r"(\textbf{II}, 3.6.2)", "P^r_A is bold upright here (no convention 10).")
add(100, "'j_*(F(n)) = (j_*(F))(n) (II, 3.4.5 et 3.5.2)'",
    "(II, 3.4.5 et 3.5.2) with bold II", r"(II, 3.4.5 et 3.5.2)", "convention", 2, "high",
    r"(II, 3.4.5 et 3.5.2)", r"(\textbf{II}, 3.4.5 et 3.5.2)")
add(100, "'Compte tenu de (G, II, cor. du th. 4.9.1)'",
    "(G, II, ...) with bold II", r"(G, II, cor. du th. 4.9.1)", "convention", 2, "high",
    r"(G, II, cor.", r"(G, \textbf{II}, cor.",
    "Chapter II of Godement's book (G), printed with the same bold numeral as EGA chapter references. Checked on a crop.")
add(100, "last line: 'dans le cas particulier où X = P^r_A et S = A[T_0, ..., T_r]. Comme X est recouvert par les ouverts'",
    "inline; the paragraph continues on the same line ('Comme X est recouvert ...')",
    r"displayed with \[ ... \], followed by a blank line (paragraph break)", "other", None, "high",
    L(r"où", r"\[", r"X=\mathbf P_A^r\quad\text{et}\quad S=A[T_0,\ldots,T_r].", r"\]", "", ""),
    L(r"où", r"$X=\mathbf P_A^r$ et $S=A[T_0,\ldots,T_r]$.", ""),
    "Also removes the blank line before \\oldpage[III]{101}: the print has no paragraph break there.")
add(101, "marker \\oldpage[III]{101} (end of printed page 100)",
    "printed page 100 ends with 'Comme X est recouvert par les ouverts'; page 101 begins with 'affines D_+(T_i) en nombre r+1'",
    r"\oldpage[III]{101} stands before 'Comme $X$ est recouvert par les ouverts affines'", "marker", None, "high",
    L(r"\oldpage[III]{101}", r"Comme $X$ est recouvert par les ouverts affines"),
    L(r"Comme $X$ est recouvert par les ouverts", r"\oldpage[III]{101}", r"affines"),
    "Found while checking p. 100 (last line of the scan; top of the p. 101 scan confirms). The edit lies in page 101's segment.")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- checks: control characters, uniqueness, sequential application per page ----
bad = 0
for i, x in enumerate(F):
    for k in ("old", "new"):
        s = (x["fix"] or {}).get(k) or ""
        if any(ord(c) < 32 and c != "\n" for c in s):
            print("CONTROL CHAR in", i, k, repr(s)); bad += 1
pages = {}
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    p = x["page"]
    if p not in pages:
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    orig = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n0 = orig.count(x["fix"]["old"])
    n1 = pages[p].count(x["fix"]["old"])
    if n0 != 1 or n1 != 1:
        print(f"PROBLEM finding {i} p{p}: original count {n0}, after earlier fixes {n1}: {x['fix']['old']!r}")
        bad += 1
    else:
        pages[p] = pages[p].replace(x["fix"]["old"], x["fix"]["new"])
from collections import Counter
c = Counter()
for x in F:
    t = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], t)] += 1
for p in sorted({x["page"] for x in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("findings:", len(F), "problems:", bad)
sys.exit(1 if bad else 0)
