"""Build findings_166_170.json and check that every fix's old string occurs exactly once."""
import json
import sys
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_166_170.json"


def L(*parts):
    return "\n".join(parts)


SETMIN_NOTE = ("Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes, "
               "pending the convention-7 decision.")

F = []


def add(page, where, scan, tex, kind, fix, confidence="high", convention=None, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 166
add(166, "Remarques (21.5.3) (i), first sentence: 'résoudre la question de l'unicité du corps de représentants'",
    "l'*unicité* (italic)", "unicité upright (no \\emph)", "italics",
    {"old": r"l'unicité du corps", "new": r"l'\emph{unicité} du corps"},
    note="Remark body judged as roman (document-wide remark environment).")
add(166, "Remarques (21.5.3) (i), second sentence: 'Soient en effet J l'idéal maximal de C'",
    "'Soient en effet 𝔍 l'idéal maximal de C' (crop)", "'Soient $\\mathfrak J$ l'idéal maximal' ('en effet' missing)",
    "missing",
    {"old": r"Soient $\mathfrak J$ l'idéal maximal", "new": r"Soient en effet $\mathfrak J$ l'idéal maximal"})
add(166, "Remarques (21.5.3) (i): 'alors, pour que cet homomorphisme soit unique, il faut et il suffit que Ω^1_K=0'",
    "'pour que cet homomorphisme soit unique, il faut et il suffit que' italic (crop); 'alors,' and the formula upright",
    "upright", "italics",
    {"old": L(r"alors, pour", r"  que cet homomorphisme soit unique, il faut et il suffit que"),
     "new": L(r"alors, \emph{pour", r"  que cet homomorphisme soit unique, il faut et il suffit que}")},
    note="Remark body judged as roman.")
add(166, "Remarques (21.5.3) (i): 'l'ensemble des u(x)—v(x) pour x∈K'",
    "long dash (bar 40 px at 300 dpi; the = bars on the page are 33-35 px)", "$u(x)-v(x)$", "convention",
    {"old": r"$u(x)-v(x)$", "new": r"$u(x)\setmin v(x)$"}, convention=7, note=SETMIN_NOTE)
add(166, "Remarques (21.5.3) (i): 'deux homomorphismes distincts u', v' de K dans C/J^{n+1}'",
    "u', v' (primes, crop)", "$u_1,v_1$", "formula",
    {"old": r"$u_1,v_1$ de $K$ dans", "new": r"$u'$, $v'$ de $K$ dans"},
    note="The print keeps u_1, v_1 for the maps into C/J^2 a few lines further on; here the maps into C/J^{n+1} are u', v'.")
add(166, "Remarques (21.5.3) (i): 'Rappelons ((20.6.20) et (21.4.4)) que la condition ...'",
    "new indented paragraph", "runs on in the paragraph of 'et l'on a v≠u.'", "other",
    {"old": L(r"$v\ne u$.", r"  Rappelons"), "new": L(r"$v\ne u$.", "", r"  Rappelons")})
add(166, "Remarques (21.5.3) (i): 'signifie que K est parfait s'il est de caractéristique ≠0'",
    "*parfait* (italic)", "parfait upright", "italics",
    {"old": r"est parfait s'il", "new": r"est \emph{parfait} s'il"},
    note="Remark body judged as roman.")
add(166, "Remarques (21.5.3) (ii), first sentence: 'C un anneau local noethérien complet, J un idéal ≠0 de C contenu dans l'idéal maximal'",
    "'𝔍 un idéal ≠0 de C' (crop)", "'soit $\\mathfrak J\\ne0$ un idéal de $C$' (added 'soit'; ≠0 attached to J)", "word",
    {"old": r"complet, soit $\mathfrak J\ne0$ un idéal de $C$", "new": r"complet, $\mathfrak J$ un idéal $\ne0$ de $C$"})
add(166, "Remarques (21.5.3) (ii): 'pour que la factorisation W→C→C/J dans (19.8.6, (i))'",
    "v over the first arrow: W -v-> C -> C/𝔍 (crop)", "$W\\to C\\to C/\\mathfrak J$ (no label)", "formula",
    {"old": r"$W\to C\to C/\mathfrak J$", "new": r"$W\xrightarrow{v}C\to C/\mathfrak J$"},
    note="The v is the map whose uniqueness the remark proves ('l'unicité de v').")
add(166, "Remarques (21.5.3) (ii): 'dans (19.8.6, (i)) soit unique, il faut et il suffit'",
    "*unique* (italic; the rest of the sentence upright)", "unique upright", "italics",
    {"old": r"(i)) soit unique,", "new": r"(i)) soit \emph{unique},"},
    note="Remark body judged as roman.")
add(166, "Remarques (21.5.3) (ii), last sentence: 'W est formellement non ramifiée (pour sa topologie adique) sur Z'",
    "'non ramifiée' (crop)", "'non ramifié' (silent correction)", "misprint_in_print",
    {"old": L(r"formellement non ramifié", r"  (pour"), "new": L(r"formellement non ramifiée", r"  (pour")},
    confidence="medium", corrected=r"formellement non ramifié",
    note=("The TeX silently corrects; the fix restores the printed reading. W is 'un anneau de Cohen' (masculine) and the "
          "same remark has 'K est formellement non ramifié'; the feminine fits only if W is read as a Z-algèbre, "
          "hence medium confidence that it is a misprint."))

# ---------------------------------------------------------------- page 167
add(167, "heading 21.6: 'Corps admissibles pour une extension.'",
    "final full stop", "no full stop", "punctuation",
    {"old": r"\subsection{Corps admissibles pour une extension}",
     "new": r"\subsection{Corps admissibles pour une extension.}"},
    note="GLOBAL_ISSUES 43/58 (subsection titles without the printed full stop).")
add(167, "(21.6.1), second paragraph: 'est encore bijectif, on dit que'",
    "*bijectif* (italic)", "upright", "italics",
    {"old": r"est encore bijectif,", "new": r"est encore \emph{bijectif},"})
add(167, "(21.6.1): 'on dit que k est un corps k_0-admissible pour l'extension L de K.'",
    "'corps k_0-admissible pour l'extension L de K' italic (L, K upright)", "upright", "italics",
    {"old": r"un corps $k_0$-admissible pour l'extension $L$ de $K$",
     "new": r"un \emph{corps $k_0$-admissible pour l'extension $L$ de $K$}"},
    note="Defined term.")
add(167, "(21.6.1): '(par exemple tels que [K:k] soit fini)'",
    "*fini* (italic, crop)", "upright", "italics",
    {"old": r"soit fini", "new": r"soit \emph{fini}"})
add(167, "(21.6.1): '(par exemple tels que [K:k] soit fini) est qu'ils permettent'",
    "no comma after the closing parenthesis (crop)", "'soit fini), est'", "punctuation",
    {"old": L(r"), est", r"qu'ils"), "new": L(r") est", r"qu'ils")})
add(167, "(21.6.1.2), part 1 of 2: 'On posera' and the display numbered (21.6.1.2)",
    "(21.6.1.2) is the number of the display after 'On posera' (bold, at the left margin like (21.6.1.1)); "
    "'(espace vectoriel sur L); ...' continues the paragraph of (21.6.1)",
    "\\end{env} closes (21.6.1) after 'On posera' and \\begin{env}[21.6.1.2] opens a new numbered paragraph "
    "holding an unnumbered \\[...\\] display and the rest of the text",
    "other",
    {"old": L(r"On posera", r"\end{env}", "", r"\begin{env}[21.6.1.2]", r"\label{0.21.6.1.2-fr}", r"\["),
     "new": L(r"On posera", r"\begin{equation}", r"\label{0.21.6.1.2-fr}", r"\tag{21.6.1.2}")},
    confidence="medium",
    note=("Apply together with part 2 (the closing \\] becomes \\end{equation}). The \\end{env} after "
          "'d(L/K,k/k_0).' then closes (21.6.1); the label keeps its name and carries the tag. Same pattern as "
          "(18.3.6.4), p. 62 (GLOBAL_ISSUES 64). The rendered page changes little; the difference is the role of the number."))
add(167, "(21.6.1.2), part 2 of 2: end of the display",
    "see part 1", "\\]", "other",
    {"old": L(r"\Upsilon_{L/K/k})", r"\]"), "new": L(r"\Upsilon_{L/K/k})", r"\end{equation}")},
    confidence="medium", note="Apply together with part 1.")
add(167, "(21.6.1.2): 'Coker(...) ≅ Ker(...)'",
    "≅ (tilde over a double bar, enlarged crop)", "\\simeq (tilde over a single bar)", "symbol",
    {"old": r"\simeq\operatorname{Ker}", "new": r"\cong\operatorname{Ker}"},
    note="Not an arrow, so not convention 4.")
add(167, "Proposition (21.6.2) (i) b): 'L'homomorphisme canonique u: Υ_{L/k/k_0} → Υ_{L/K/k_0} est nul.'",
    "u : Υ_{L/k/k_0} → Υ_{L/K/k_0} (crop)", "$u:\\Upsilon_{K/k/k_0}\\to\\Upsilon_{L/k/k_0}$", "formula",
    {"old": r"$u:\Upsilon_{K/k/k_0}\to\Upsilon_{L/k/k_0}$", "new": r"$u:\Upsilon_{L/k/k_0}\to\Upsilon_{L/K/k_0}$"},
    note="The print's u is the map u of (21.6.1.1); the TeX repeats the source of v.")
add(167, "Proposition (21.6.2) (ii): 'Les conditions équivalentes de (i) sont vérifiées'",
    "(i) upright (crop)", "(i) italic inside the proposition", "convention",
    {"old": r"de (i) sont vérifiées", "new": r"de \textup{(i)} sont vérifiées"}, convention=6)
add(167, "proof of (21.6.2) (ii), first clause: 'Si L est séparable sur k, on a Υ_{L/k/k_0}=0 (20.6.19)'",
    "Υ_{L/k/k_0} (lower-case k in the middle; the next clause has Υ_{L/K/k_0}; crop)", "$\\Upsilon_{L/K/k_0}=0$", "formula",
    {"old": L(r"sur $k$, on a", r"  $\Upsilon_{L/K/k_0}=0$"), "new": L(r"sur $k$, on a", r"  $\Upsilon_{L/k/k_0}=0$")})
add(167, "proof of (21.6.2) (ii): 'donc la condition b) de (i) est remplie'",
    "*b)* italic", "b) upright", "italics",
    {"old": r"la condition b) de (i)", "new": r"la condition \emph{b)} de (i)"})
add(167, "proof of (21.6.2) (ii): 'donc la condition a) de (i) est remplie'",
    "*a)* italic", "a) upright", "italics",
    {"old": r"donc la condition a) de (i) est remplie", "new": r"donc la condition \emph{a)} de (i) est remplie"})
add(167, "proof of (21.6.2) (ii), end: 'et la condition a) de (i) est vérifiée'",
    "*a)* italic", "a) upright", "italics",
    {"old": r"condition a) de (i) est vérifiée", "new": r"condition \emph{a)} de (i) est vérifiée"})

# ---------------------------------------------------------------- page 168
add(168, "(21.6.3): 'Il résulte alors de (20.6.17, (ii)) que l'on a un homomorphisme canonique' after the diagram",
    "new indented paragraph after the diagram", "no blank line after \\]", "other",
    {"old": L(r"\]", r"Il résulte alors"), "new": L(r"\]", "", r"Il résulte alors")})
add(168, "proof of (21.6.4) (i): 'comme des complexes T•_1, T•_2, T•_3 respectivement'",
    "T with a raised bullet: T•_1, T•_2, T•_3 (crop)", "$T_1,T_2,T_3$", "formula",
    {"old": r"$T_1,T_2,T_3$ respectivement", "new": r"$T^\bullet_1,T^\bullet_2,T^\bullet_3$ respectivement"})
add(168, "proof of (21.6.4) (i): 'une suite exacte de complexes 0→T•_1→T•_2→T•_3→0'",
    "raised bullets (crop)", "$0\\to T_1\\to T_2\\to T_3\\to0$", "formula",
    {"old": r"$0\to T_1\to T_2\to T_3\to0$", "new": r"$0\to T^\bullet_1\to T^\bullet_2\to T^\bullet_3\to0$"})

# ---------------------------------------------------------------- page 169
add(169, "proof of (21.6.4) (i): 'la cohomologie de T•_1 et celle de T•_2 sont nulles'",
    "raised bullets", "$T_1$, $T_2$", "formula",
    {"old": r"de $T_1$ et celle de $T_2$", "new": r"de $T^\bullet_1$ et celle de $T^\bullet_2$"})
add(169, "proof of (21.6.4) (i): 'comme T•_1 et T•_2 ont ainsi même cohomologie'",
    "raised bullets (crop)", "$T_1$, $T_2$", "formula",
    {"old": r"comme $T_1$ et $T_2$ ont", "new": r"comme $T^\bullet_1$ et $T^\bullet_2$ ont"})
add(169, "proof of (21.6.4) (i): 'celle de T•_3 est nécessairement nulle'",
    "raised bullet", "$T_3$", "formula",
    {"old": r"celle de $T_3$ est", "new": r"celle de $T^\bullet_3$ est"})
add(169, "proof of (21.6.4) (ii), diagram: vertical arrow below Δ(M/L, k/k_0)",
    "the third column has vertical arrows like the first two (Δ(M/L,k/k_0) → Υ_{M/L/k_0} → Υ_{M/L/k})",
    "no \\ar[d] in the third column", "missing",
    {"old": r"\Delta(M/L,k/k_0)\ar[r]&0", "new": r"\Delta(M/L,k/k_0)\ar[r]\ar[d]&0"})
add(169, "proof of (21.6.4) (ii), diagram: vertical arrow below Υ_{M/L/k_0}",
    "vertical arrow Υ_{M/L/k_0} → Υ_{M/L/k}", "no \\ar[d]", "missing",
    {"old": r"\Upsilon_{M/L/k_0}\ar[r]&0", "new": r"\Upsilon_{M/L/k_0}\ar[r]\ar[d]&0"})
add(169, "proof of (21.6.4) (ii): 'comme des complexes T'•_1, T'•_2 et T'•_3; la suite'",
    "T'•_1, T'•_2 et T'•_3 (raised bullets; 'et' before the third; crop)", "$T'_1,T'_2,T'_3$", "formula",
    {"old": r"$T'_1,T'_2,T'_3$~;", "new": r"$T'^\bullet_1$, $T'^\bullet_2$ et $T'^\bullet_3$~;"},
    note="Two differences in one span: the bullets and the printed word 'et'.")
add(169, "proof of (21.6.4) (ii): 'suite exacte de complexes 0→T'•_1→T'•_2→T'•_3→0'",
    "raised bullets (crop)", "$0\\to T'_1\\to T'_2\\to T'_3\\to0$", "formula",
    {"old": r"$0\to T'_1\to T'_2\to T'_3\to0$", "new": r"$0\to T'^\bullet_1\to T'^\bullet_2\to T'^\bullet_3\to0$"})
add(169, "proof of (21.6.4) (ii): 'la cohomologie de T'•_2 et celle de T'•_3'",
    "raised bullets", "$T'_2$, $T'_3$", "formula",
    {"old": r"de $T'_2$ et celle de $T'_3$", "new": r"de $T'^\bullet_2$ et celle de $T'^\bullet_3$"})
add(169, "proof of (21.6.4) (ii): 'les modules de cohomologie sont tous deux égaux à Υ_{M/L/K}'",
    "Υ_{M/L/K} (capital K, enlarged crop)", "$\\Upsilon_{M/L/k_0}$", "formula",
    {"old": r"$\Upsilon_{M/L/k_0}$~; on conclut", "new": r"$\Upsilon_{M/L/K}$~; on conclut"},
    note="Υ_{M/L/K} is the cokernel of Υ_{M/K/k_0}→Υ_{M/L/k_0} by (21.6.1.1), as the argument needs.")
add(169, "proof of (21.6.4) (ii): 'la cohomologie de T'•_1 est nulle'",
    "raised bullet", "$T'_1$", "formula",
    {"old": r"cohomologie de $T'_1$ est", "new": r"cohomologie de $T'^\bullet_1$ est"})
add(169, "Corollaire (21.6.5), label (i)",
    "(i) upright", "\\item[(i)] italic inside the corollary environment", "convention",
    {"old": r"\item[(i)] Étant donnés", "new": r"\item[\textup{(i)}] Étant donnés"}, convention=6,
    note="GLOBAL_ISSUES 16.")
add(169, "Corollaire (21.6.5), label (ii)",
    "(ii) upright", "\\item[(ii)] italic inside the corollary environment", "convention",
    {"old": r"\item[(ii)] Étant donnés", "new": r"\item[\textup{(ii)}] Étant donnés"}, convention=6,
    note="GLOBAL_ISSUES 16.")
add(169, "after Corollaire (21.6.5): 'Cela résulte aussitôt des relations (21.6.4.2) et (21.6.4.4), les valeurs de d étant ⩾0.'",
    "roman sentence in a new indented paragraph after the statement",
    "inside the italic corollary environment", "other",
    {"old": L(r"\end{enumerate}", "", r"Cela résulte aussitôt des relations (21.6.4.2) et (21.6.4.4), les valeurs de",
              r"$d$ étant $\geqslant0$.", r"\end{corollary}"),
     "new": L(r"\end{enumerate}", r"\end{corollary}", "",
              r"Cela résulte aussitôt des relations (21.6.4.2) et (21.6.4.4), les valeurs de",
              r"$d$ étant $\geqslant0$.")},
    note="One edit: moves \\end{corollary} to the end of the printed statement (as GLOBAL_ISSUES 58, (16.4.5); p. 71).")
add(169, "heading 21.7: 'L'égalité de Cartier.'",
    "final full stop", "no full stop", "punctuation",
    {"old": r"\subsection{L'égalité de Cartier}", "new": r"\subsection{L'égalité de Cartier.}"},
    note="GLOBAL_ISSUES 43/58.")

# ---------------------------------------------------------------- page 170
add(170, "proof of (21.7.1): the exact sequence from (20.6.15.1)",
    "0→Υ_{L'/K}⊗_{L'}L→Υ_{L/K}→Υ_{L/L'}→Ω^1_{L'/K}⊗_{L'}L→Ω^1_{L/K}→Ω^1_{L/L'}→0 (crop)",
    "the term Υ_{L/L'} and its arrow are missing", "missing",
    {"old": L(r"\to\Upsilon_{L/K}", r"\to\Omega^1_{L'/K}"),
     "new": L(r"\to\Upsilon_{L/K}\to\Upsilon_{L/L'}", r"\to\Omega^1_{L'/K}")})
add(170, "proof of (21.7.1): 'd'où (0_III, 11.10.2)'",
    "bold 0", "plain 0", "convention",
    {"old": r"(0$_{\rm III}$, 11.10.2)", "new": r"($\mathbf{0}_{\rm III}$, 11.10.2)"}, convention=2)
add(170, "proof of (21.7.1), rank display: first parenthesis '(rg_L Ω^1_{L/L'} — rg_L Υ_{L/L'})', first rg",
    "rg_L (subscript L without prime, crop)", "\\operatorname{rg}_{L'}", "formula",
    {"old": r"=(\operatorname{rg}_{L'}", "new": r"=(\operatorname{rg}_L"},
    note="Ω^1_{L/L'} and Υ_{L/L'} are L-vector spaces.")
add(170, "proof of (21.7.1), rank display: first parenthesis, second rg",
    "rg_L Υ_{L/L'} (crop)", "\\operatorname{rg}_{L'}\\Upsilon_{L/L'}", "formula",
    {"old": r"\operatorname{rg}_{L'}\Upsilon_{L/L'})", "new": r"\operatorname{rg}_L\Upsilon_{L/L'})"})
add(170, "proof of (21.7.1), rank display: 'rg_L Ω^1_{L/K} — rg_L Υ_{L/K}'",
    "long dash (bar 41 px at 300 dpi; = bars 33-35 px)", "-", "convention",
    {"old": r"\Omega^1_{L/K}-\operatorname{rg}_L", "new": r"\Omega^1_{L/K}\setmin\operatorname{rg}_L"},
    convention=7, note=SETMIN_NOTE)
add(170, "proof of (21.7.1), rank display: 'rg_L Ω^1_{L/L'} — rg_L Υ_{L/L'}'",
    "long dash (bar 40 px)", "-", "convention",
    {"old": r"\Omega^1_{L/L'}-", "new": r"\Omega^1_{L/L'}\setmin"}, convention=7, note=SETMIN_NOTE)
add(170, "proof of (21.7.1), rank display: 'rg_{L'} Ω^1_{L'/K} — rg_{L'} Υ_{L'/K}'",
    "long dash (bar 39 px)", "-", "convention",
    {"old": r"\Omega^1_{L'/K}-", "new": r"\Omega^1_{L'/K}\setmin"}, convention=7, note=SETMIN_NOTE)
add(170, "(21.7.1.1): 'rg Ω^1_{L/K} — rg Υ_{L/K} = deg. tr_K L'",
    "long dash (bar 41 px; = bars 33-35 px)", "-", "convention",
    {"old": L(r"-\operatorname{rg}\Upsilon_{L/K}", r"=\deg"), "new": L(r"\setmin\operatorname{rg}\Upsilon_{L/K}", r"=\deg")},
    convention=7, note=SETMIN_NOTE)
add(170, "proof of (21.7.1), case label a)",
    "*a)* italic (crop)", "\\item[\\rm a)] upright", "italics",
    {"old": r"\item[\rm a)]", "new": r"\item[\textit{a)}]"})
add(170, "proof of (21.7.1), case label b)",
    "*b)* italic (crop)", "\\item[\\rm b)] upright", "italics",
    {"old": r"\item[\rm b)]", "new": r"\item[\textit{b)}]"})
add(170, "proof of (21.7.1), case label c)",
    "*c)* italic", "\\item[\\rm c)] upright", "italics",
    {"old": r"\item[\rm c)]", "new": r"\item[\textit{c)}]"})
add(170, "proof of (21.7.1), case c): 'le raisonnement du début montre qu'on peut se borner'",
    "'montre qu'on peut' (crop)", "'montre que l'on peut'", "word",
    {"old": r"montre que l'on peut", "new": r"montre qu'on peut"})
add(170, "Corollaire (21.7.2): 'Par suite, on a l'inégalité' after (21.7.2.1)",
    "new indented paragraph after the display", "no blank line after \\end{equation}", "other",
    {"old": L(r"\end{equation}", r"Par suite"), "new": L(r"\end{equation}", "", r"Par suite")})
add(170, "(21.7.2.1): 'rg Ω^1_{L/K} — rg Υ_{L/K/k}'",
    "long dash (bar 40 px)", "-", "convention",
    {"old": L(r"-\operatorname{rg}\Upsilon_{L/K/k}", r"=\deg"), "new": L(r"\setmin\operatorname{rg}\Upsilon_{L/K/k}", r"=\deg")},
    convention=7, note=SETMIN_NOTE)
add(170, "(21.7.2.2): 'rg Ω^1_{L/K} — rg Υ_{L/K/k} ⩾ deg. tr_K L'",
    "long dash (bar 42 px)", "-", "convention",
    {"old": L(r"-\operatorname{rg}\Upsilon_{L/K/k}", r"\geqslant"),
     "new": L(r"\setmin\operatorname{rg}\Upsilon_{L/K/k}", r"\geqslant")},
    convention=7, note=SETMIN_NOTE)
add(170, "Corollaire (21.7.2): 'pour que les deux membres de (21.7.2.2) soient égaux'",
    "(21.7.2.2) upright (crop)", "italic inside the corollary environment", "convention",
    {"old": r"membres de (21.7.2.2) soient", "new": r"membres de \textup{(21.7.2.2)} soient"}, convention=6)
add(170, "proof of (21.7.2): 'rg Υ_{L/K} — rg Υ_{L/K/k} = d(L/K, k)'",
    "long dash (bar 42 px)", "-", "convention",
    {"old": r"\Upsilon_{L/K}-\operatorname{rg}\Upsilon_{L/K/k}", "new": r"\Upsilon_{L/K}\setmin\operatorname{rg}\Upsilon_{L/K/k}"},
    convention=7, note=SETMIN_NOTE + " The '=' after it has a broken upper bar (print defect), not a double sign.")
add(170, "(21.7.3.1): 'rg_L Ω^1_{L/k} — rg_K Ω^1_{K/k}'",
    "long dash (bar 40 px)", "-", "convention",
    {"old": r"\Omega^1_{L/k}-\operatorname{rg}_K", "new": r"\Omega^1_{L/k}\setmin\operatorname{rg}_K"},
    convention=7, note=SETMIN_NOTE)

# ---------------------------------------------------------------- checks
ok = True
texts = {}
for p in sorted({f["page"] for f in F}):
    texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    old = f["fix"]["old"]
    n = texts[f["page"]].count(old)
    if n != 1:
        ok = False
        print(f"#{i} page {f['page']}: old occurs {n} times: {old!r}")
    if f["fix"]["old"] == f["fix"]["new"]:
        ok = False
        print(f"#{i}: old == new")

# sequential application per page must succeed (every old still present once after earlier edits)
for p, t in texts.items():
    cur = t
    for i, f in enumerate(F):
        if f["page"] != p or f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        if cur.count(old) != 1:
            ok = False
            print(f"#{i} page {p}: after earlier edits old occurs {cur.count(old)} times")
        cur = cur.replace(old, new, 1)

# the same olds against the LF source file, inside each page's segment
SRC = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega4\ega0-21-fr.tex")
src = SRC.read_bytes().decode("utf-8")
assert "\r" not in src
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    p = f["page"]
    a = src.index("\\oldpage[0\\textsubscript{IV-1}]{%d}" % p)
    b = src.index("\\oldpage[0\\textsubscript{IV-1}]{%d}" % (p + 1))
    seg = src[a:b]
    old = f["fix"]["old"]
    if seg.count(old) != 1:
        ok = False
        print(f"#{i} page {p}: old occurs {seg.count(old)} times in the source segment")
    if src.count(old) != 1:
        print(f"#{i} page {p}: note: old occurs {src.count(old)} times in the whole source file")

if not ok:
    sys.exit(1)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in sorted(texts):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F))
