"""Build findings_165_169.json for EGA IV-2 pp. 165-169, check every "old" against its page_NNN.tex
(exactly once, LF line breaks), then dry-run all edits in order on an in-memory copy of the release source
with the same page-segment rule as apply_fixes.py (nothing is written to any .tex file)."""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
E = RUN.parent
SRC = E / r"ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex"
OUT = RUN / "findings_165_169.json"
NL = "<NL>"


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    fix = None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C = "convention"
L = []
# ---------------------------------------------------------------- page 165
p = 165
L += [
    F(p, "proof of (6.12.4.1): 'A'_1 = A_1[t'_1, ..., t'_m] est fini sur A_1'", "'fini' italic", "roman",
      C, 6, "high", r"est fini sur $A_1$", r"est \emph{fini} sur $A_1$"),
    F(p, "proof of (6.12.4.1): 'qui sont A-isomorphes (I, 6.5.5)'", "'isomorphes' italic", "roman",
      C, 6, "high", r"$A$-isomorphes", r"$A$-\emph{isomorphes}"),
    F(p, "proof of (6.12.4.1): '(I, 6.5.5)'", "bold I", "plain I",
      C, 2, "high", r"(I, 6.5.5)", r"(\textbf{I}, 6.5.5)"),
    F(p, "proof of (6.12.4.1): 'A' est une A_1-algèbre finie'", "'algèbre finie' italic", "roman",
      C, 6, "high", r"$A_1$-algèbre finie.", r"$A_1$-\emph{algèbre finie}."),
    F(p, "proof of (6.12.4.1): '(0, 17.3.7)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 17.3.7)", r"(\textbf{0}, 17.3.7)"),
    F(p, "proof of (6.12.4.1): 'A_1 est un anneau régulier, et l'on peut'", "'régulier' italic", "roman",
      C, 6, "high", r"est un anneau régulier, et", r"est un anneau \emph{régulier}, et"),
    F(p, "proof of (6.12.4.1): 'A' est une A-algèbre finie et K''", "'finie' italic", "roman",
      C, 6, "high", r"$A$-algèbre finie et $K'$", r"$A$-algèbre \emph{finie} et $K'$"),
    F(p, "proof of (6.12.4.1): 'une extension séparable et finie de K'", "'séparable et finie' italic", "roman",
      C, 6, "high", r"séparable et finie de $K$.", r"\emph{séparable et finie} de $K$."),
    F(p, "proof of (6.12.4.1): 'A' est un A-module libre de type fini'", "'libre' italic", "roman",
      C, 6, "high", r"$A$-module libre de type fini", r"$A$-module \emph{libre} de type fini"),
    F(p, "proof of (6.12.4.1): after the display 'd = det(...) ∈ A.'",
      "'Comme K' est séparable sur K' opens a new indented paragraph (enlarged crop)",
      "no blank line after \\], so the text runs on in the same paragraph", "other", None, "high",
      r"\]" + NL + r"Comme $K'$", r"\]" + NL + NL + r"Comme $K'$", "Paragraph break after a display (GLOBAL_ISSUES 47 pattern)."),
    F(p, "proof of (6.12.4.1): 'supposer d inversible dans A'", "'inversible' italic", "roman",
      C, 6, "high", r"$d$ inversible dans", r"$d$ \emph{inversible} dans"),
    F(p, "proof of (6.12.4.1): 'A'(z) = A' (x)_A k(z)'", "bold italic k", "plain k",
      C, 1, "high", r"A'\otimes_A k(z)", r"A'\otimes_A \boldsymbol{k}(z)"),
    F(p, "proof of (6.12.4.1): subscript of Tr_{A'(z)/k(z)}", "bold upright k in the subscript (enlarged crop)",
      "plain k", C, 1, "high", r"_{A'(z)/k(z)}", r"_{A'(z)/\mathbf{k}(z)}",
      "Bold upright in the subscript, as GLOBAL_ISSUES 48."),
    F(p, "proof of (6.12.4.1): 'k(z) = A_z/m_z'", "bold italic k", "plain k",
      C, 1, "high", r"$k(z)=A_z", r"$\boldsymbol{k}(z)=A_z"),
    F(p, "proof of (6.12.4.1): 'k(z) = A_z/m_z, et comme d-bar'", "comma after m_z (enlarged crop)", "no comma",
      "punctuation", None, "high", r"\mathfrak m_z$ et comme", r"\mathfrak m_z$, et comme"),
    F(p, "proof of (6.12.4.1): 'inversible (donc ≠ 0) dans k(z)'", "bold italic k", "plain k",
      C, 1, "high", r"dans $k(z)$, on sait", r"dans $\boldsymbol{k}(z)$, on sait"),
    F(p, "proof of (6.12.4.1): 'on sait (loc. cit.) que'", "'(loc. cit.)' italic", "roman",
      C, 6, "high", r"(loc. cit.)", r"\emph{(loc. cit.)}"),
    F(p, "proof of (6.12.4.1): 'une k(z)-algèbre séparable'", "bold italic k", "plain k",
      C, 1, "high", r"une $k(z)$-algèbre", r"une $\boldsymbol{k}(z)$-algèbre"),
    F(p, "proof of (6.12.4.1): 'k(z)-algèbre séparable, donc composée directe'", "'séparable' italic", "roman",
      C, 6, "high", r"séparable, donc composée", r"\emph{séparable}, donc composée"),
    F(p, "proof of (6.12.4.1): 'finies et séparables de k(z)'", "bold italic k", "plain k",
      C, 1, "high", r"de $k(z)$. Une", r"de $\boldsymbol{k}(z)$. Une"),
    F(p, "proof of (6.12.4.1): 'étant un anneau régulier, on voit'", "'régulier' italic", "roman",
      C, 6, "high", r"étant un anneau régulier,", r"étant un anneau \emph{régulier},"),
    F(p, "proof of (6.12.4.1): 'g : X' -> X est plat'", "'plat' italic", "roman",
      C, 6, "high", r"est plat et que", r"est \emph{plat} et que"),
    F(p, "proof of (6.12.4.1): 'ses fibres g^-1(z) sont régulières'", "'régulières' italic", "roman",
      C, 6, "high", r"sont régulières pour", r"sont \emph{régulières} pour"),
    F(p, "proof of (6.12.4.1): 'X' est régulier, ce qui termine'", "'régulier' italic", "roman",
      C, 6, "high", r"est régulier, ce qui termine", r"est \emph{régulier}, ce qui termine"),
    F(p, "proof of (6.12.4), part II", "'Cas général' italic", "roman",
      C, 6, "high", r"II) Cas général.", r"II) \emph{Cas général}."),
    F(p, "proof of (6.12.4) II: 'si X''_1 = Spec(A' (x)_A K_1) = X'' (x)_K K_1'",
      "X''_1 (two primes; enlarged crop)", "X'_1", "formula", None, "high",
      r"$X'_1=\operatorname{Spec}(A'\otimes_AK_1)", r"$X''_1=\operatorname{Spec}(A'\otimes_AK_1)",
      "The print writes X''_1 four times in this passage (= X'' (x)_K K_1); X'_1 is defined later as Spec(A'_1)."),
    F(p, "proof of (6.12.4) II: '(X''_1)_red soit un K_1-préschéma'", "(X''_1)_red", "(X'_1)_red",
      "formula", None, "high", r"$(X'_1)_{\mathrm{red}}$ soit", r"$(X''_1)_{\mathrm{red}}$ soit"),
    F(p, "proof of (6.12.4) II: 'géométriquement réduit de type fini'", "'géométriquement réduit' italic", "roman",
      C, 6, "high", r"géométriquement réduit de", r"\emph{géométriquement réduit} de"),
    F(p, "proof of (6.12.4) II: 'donc X''_1 est homéomorphe à X'''", "X''_1", "X'_1",
      "formula", None, "high", r"donc $X'_1$ est homéomorphe", r"donc $X''_1$ est homéomorphe"),
    F(p, "proof of (6.12.4) II: 'par suite (X''_1)_red est intègre'", "(X''_1)_red", "(X'_1)_red",
      "formula", None, "high", r"$(X'_1)_{\mathrm{red}}$ est intègre", r"$(X''_1)_{\mathrm{red}}$ est intègre"),
    F(p, "proof of (6.12.4) II: 'une extension séparable de type fini de K_1'", "'séparable' italic", "roman",
      C, 6, "high", r"extension séparable de type fini", r"extension \emph{séparable} de type fini"),
    F(p, "proof of (6.12.4) II: 'l'hypothèse c) de l'énoncé'", "'c)' italic", "roman",
      C, 6, "high", r"l'hypothèse c) de", r"l'hypothèse \emph{c)} de"),
    F(p, "proof of (6.12.4) II: 'une sous-A-algèbre finie A_1 de K_1'", "'finie' italic", "roman",
      C, 6, "high", r"algèbre finie $A_1$ de", r"algèbre \emph{finie} $A_1$ de"),
    F(p, "proof of (6.12.4) II: 'une A'-algèbre finie et dont'", "'finie' italic", "roman",
      C, 6, "high", r"$A'$-algèbre finie et dont", r"$A'$-algèbre \emph{finie} et dont"),
    F(p, "proof of (6.12.4) II: 'fini et surjectif (II, 6.1.10)'", "bold II", "plain II",
      C, 2, "high", r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)"),
]
# ---------------------------------------------------------------- page 166
p = 166
L += [
    F(p, "proof of (6.12.4) II: 'comme g est fermé (II, 6.1.10)'", "bold II", "plain II",
      C, 2, "high", r"(II, 6.1.10)", r"(\textbf{II}, 6.1.10)"),
    F(p, "proof of (6.12.4) II: 'X'_1 est régulier. En outre'", "'régulier' italic", "roman",
      C, 6, "high", r"est régulier. En outre", r"est \emph{régulier}. En outre"),
    F(p, "proof of (6.12.4) II: 'A'-module libre, et par suite'", "'libre' italic", "roman",
      C, 6, "high", r"module libre, et par suite", r"module \emph{libre}, et par suite"),
    F(p, "proof of (6.12.4) II: 'le morphisme g est plat. Mais'", "'plat' italic", "roman",
      C, 6, "high", r"est plat. Mais", r"est \emph{plat}. Mais"),
    F(p, "proof of (6.12.4) II: 'X' est régulier. C.Q.F.D.'", "'régulier' italic", "roman",
      C, 6, "high", r"est régulier. C.Q.F.D.", r"est \emph{régulier}. C.Q.F.D."),
    F(p, "Corollaire (6.12.5): '(resp. géométriquement régulier sur k)'",
      "'(resp.' and the closing parenthesis roman, the rest italic (enlarged crop)",
      "all italic (corollary environment)", C, 6, "high",
      r"(resp. géométriquement régulier sur $k$)", r"\textup{(resp.} géométriquement régulier sur $k$\textup{)}"),
    F(p, "proof of (6.12.5): 'en vertu de (6.7.7, e)); donc cet ensemble'", "semicolon after the reference (enlarged crop)",
      "comma", "punctuation", None, "high", r"e)), donc", r"e)); donc",
      "Apply before the next entry (both edits leave each other's 'old' intact in this order)."),
    F(p, "proof of (6.12.5): '(6.7.7, e))'", "'e)' italic", "roman",
      C, 6, "high", r"(6.7.7, e))", r"(6.7.7, \emph{e)})"),
    F(p, "Corollaire (6.12.6), label (i)", "label upright", "\\item[(i)] italic inside the italic statement",
      C, 6, "high", r"\item[(i)] $A$ est un anneau de Dedekind", r"\item[\textup{(i)}] $A$ est un anneau de Dedekind",
      "GLOBAL_ISSUES 16."),
    F(p, "Corollaire (6.12.6) (i): 'de caractéristique 0.'", "upright 0 (enlarged crop)",
      "text 0 set italic by the statement environment", C, 6, "medium",
      r"de caractéristique 0.", r"de caractéristique \textup{0}."),
    F(p, "Corollaire (6.12.6), label (ii)", "label upright", "\\item[(ii)] italic inside the italic statement",
      C, 6, "high", r"\item[(ii)] $A$ est un anneau semi-local", r"\item[\textup{(ii)}] $A$ est un anneau semi-local",
      "GLOBAL_ISSUES 16."),
    F(p, "proof of (6.12.6): 'Vérifions dans les deux cas la condition c)'", "'c)' italic", "roman",
      C, 6, "high", r"condition c) de (6.12.4). Dans", r"condition \emph{c)} de (6.12.4). Dans"),
    F(p, "proof of (6.12.6): 'est un corps et la condition c) de (6.12.4)'", "'c)' italic", "roman",
      C, 6, "high", r"et la condition c) de", r"et la condition \emph{c)} de"),
    F(p, "proof of (6.12.6) (i): '(0, 17.1.4)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 17.1.4)", r"(\textbf{0}, 17.1.4)"),
    F(p, "proof of (6.12.6) (i): '(0, 17.1.4), la condition c)'", "'c)' italic", "roman",
      C, 6, "high", r"), la condition c) de", r"), la condition \emph{c)} de"),
    F(p, "proof of (6.12.6) (ii): '(0, 16.1.5)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 16.1.5)", r"(\textbf{0}, 16.1.5)"),
    F(p, "proof of (6.12.6) (ii): 'ce qui prouve la condition c) de (6.12.4) dans ce cas'", "'c)' italic", "roman",
      C, 6, "high", r"condition c) de (6.12.4) dans ce cas", r"condition \emph{c)} de (6.12.4) dans ce cas"),
    F(p, "proof of (6.12.7): 'de plus A est intègre, et à prouver'", "'intègre' italic", "roman",
      C, 6, "high", r"$A$ est intègre, et", r"$A$ est \emph{intègre}, et"),
]
# ---------------------------------------------------------------- page 167
p = 167
L += [
    F(p, "proof of (6.12.7), case I)", "'Le corps des fractions K de A est de caractéristique' italic, 0 upright",
      "roman", C, 6, "high",
      r"I) Le corps des fractions $K$ de $A$ est de caractéristique 0.",
      r"I) \emph{Le corps des fractions $K$ de $A$ est de caractéristique} 0."),
    F(p, "proof of (6.12.7) I: '(0, 19.8.8)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 19.8.8)", r"(\textbf{0}, 19.8.8)"),
    F(p, "proof of (6.12.7) I: 'A soit une B-algèbre finie'", "'finie' italic", "roman",
      C, 6, "high", r"algèbre finie et que", r"algèbre \emph{finie} et que"),
    F(p, "proof of (6.12.7) I: 'C[[T_1, ..., T_r]]'", "T_r (enlarged crop)", "T_n",
      "formula", None, "high", r"T_1,\ldots,T_n]]", r"T_1,\ldots,T_r]]"),
    F(p, "proof of (6.12.7) I: '(II, 7.1.6)'", "bold II", "plain II",
      C, 2, "high", r"(II, 7.1.6)", r"(\textbf{II}, 7.1.6)"),
    F(p, "proof of (6.12.7) I: '(0, 17.3.8)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 17.3.8)", r"(\textbf{0}, 17.3.8)"),
    F(p, "proof of (6.12.7) I: 'K est une extension séparable finie de L'", "'séparable' italic", "roman",
      C, 6, "high", r"extension séparable finie", r"extension \emph{séparable} finie"),
    F(p, "proof of (6.12.7), case II)", "'Le corps des fractions K de A est de caractéristique' italic",
      "roman", C, 6, "high",
      r"II) Le corps des fractions $K$ de $A$ est de caractéristique $p>0$",
      r"II) \emph{Le corps des fractions $K$ de $A$ est de caractéristique} $p>0$"),
    F(p, "proof of (6.12.7) II: '(0, 22.7.6)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 22.7.6)", r"(\textbf{0}, 22.7.6)"),
    F(p, "proof of (6.12.8): 'Vérifions la condition c) de (6.12.4)'", "'c)' italic", "roman",
      C, 6, "high", r"Vérifions la condition c)", r"Vérifions la condition \emph{c)}"),
    F(p, "proof of (6.12.8): '(Bourbaki, Alg. comm., chap. IV'", "'Alg. comm.' italic", "roman",
      C, 6, "high", r"Alg. comm.,", r"\emph{Alg. comm.},"),
    F(p, "proof of (6.12.8): '§ 2, n° 5'", "n° with a roman superior o", "n$^o$ (math italic o)",
      "font", None, "medium", r"n$^o$ 5", r"n\textsuperscript{o} 5",
      "The edition elsewhere writes n\\textsuperscript{o} (as on p. 165)."),
    F(p, "proof of (6.12.9): 'comme la fonction x ~> codim_x(Sing(X), X)'", "wavy arrow (enlarged crop)", "\\mapsto",
      "symbol", None, "high", r"$x\mapsto\operatorname{codim}_x", r"$x\leadsto\operatorname{codim}_x",
      "GLOBAL_ISSUES 33/73 (wavy arrows)."),
    F(p, "proof of (6.12.9): 'est semi-continue inférieurement'", "'inférieurement' (enlarged crop)", "'intérieurement'",
      "word", None, "high", r"semi-continue intérieurement", r"semi-continue inférieurement",
      "The open set {codim >= n+1} needs lower semi-continuity, as printed."),
    F(p, "proof of (6.12.9): '(0, 14.2.6)'", "bold 0", "plain 0",
      C, 2, "high", r"(0, 14.2.6)", r"(\textbf{0}, 14.2.6)"),
    F(p, "Proposition (6.12.10): '(ce qui signifie que X est réduit en x)'",
      "parenthesis roman with 'réduit' italic (enlarged crop)", "all italic (proposition environment)",
      C, 6, "high", r"(ce qui" + NL + r"signifie que $X$ est réduit en $x$)",
      r"\textup{(ce qui" + NL + r"signifie que $X$ est \emph{réduit} en $x$)}"),
    F(p, "proof of (6.12.10): 'U_R0(X) est l'ensemble X — U_alpha X'_alpha'", "long dash", "minus sign",
      C, 7, "high", r"X-\bigcup_\alpha X'_\alpha", r"X\setmin\bigcup_\alpha X'_\alpha",
      "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."),
    F(p, "proof of (6.12.10): 'l'ensemble fermé Z = X — U'", "long dash", "minus sign",
      C, 7, "high", r"$Z=X-U$", r"$Z=X\setmin U$",
      "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."),
]
# ---------------------------------------------------------------- page 168 (text printed on p. 168)
p = 168
L += [
    F(p, "proof of (6.12.10): 'U_R1(X) = X — U_lambda Z_lambda'", "long dash", "minus sign",
      C, 7, "high", r"X-\bigcup_\lambda Z_\lambda", r"X\setmin\bigcup_\lambda Z_\lambda",
      "\\setmin pending the convention-7 decision (FIX_POLICY 2.7)."),
    F(p, "heading 6.13", "'... soit ouvert.' with full stop", "no full stop",
      "punctuation", None, "high", r"$\operatorname{Nor}(X)$ soit ouvert}{", r"$\operatorname{Nor}(X)$ soit ouvert.}{",
      "GLOBAL_ISSUES 43/58 pattern, as the other IV-2 heading fixes."),
    F(p, "(6.13.1): 'où X est normal; cet ensemble'", "'normal' italic", "roman",
      C, 6, "high", r"est normal; cet", r"est \emph{normal}; cet"),
    F(p, "Proposition (6.13.2): 'son normalisé (II, 6.3.8)'", "bold II, the reference upright", "plain II, italic",
      C, 2, "high", r"(II, 6.3.8)", r"\textup{(\textbf{II}, 6.3.8)}",
      "One edit for this finding and the next (convention 6): bold numeral and the upright reference together."),
    F(p, "Proposition (6.13.2): same reference '(II, 6.3.8)'", "reference upright inside the italic statement",
      "italic", C, 6, "high", None, None,
      "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."),
    F(p, "proof of (6.13.2): 'une O_X-Algèbre cohérente'", "'cohérente' italic", "roman",
      C, 6, "high", r"Algèbre cohérente", r"Algèbre \emph{cohérente}"),
    F(p, "proof of (6.13.2): '(II, 6.1.3)'", "bold II", "plain II",
      C, 2, "high", r"(II, 6.1.3)", r"(\textbf{II}, 6.1.3)"),
    F(p, "proof of (6.13.2): 'l'homomorphisme canonique O_x -> (f_*(O_X'))_x'", "O_x (lower-case x; enlarged crop)",
      "\\mathcal O_X", "formula", None, "high", r"\mathcal O_X\to(f_*", r"\mathcal O_x\to(f_*"),
    F(p, "proof of (6.13.2): '(II, 6.3.4)'", "bold II", "plain II",
      C, 2, "high", r"(II, 6.3.4)", r"(\textbf{II}, 6.3.4)"),
    F(p, "proof of (6.13.2): 'l'ensemble de ces points est ouvert'", "'ouvert' italic", "roman",
      C, 6, "high", r"est ouvert puisque", r"est \emph{ouvert} puisque"),
    F(p, "proof of (6.13.2): '(0_I, 5.2.7)'", "bold 0", "plain 0",
      C, 2, "high", r"(0$_{\rm I}$, 5.2.7)", r"(\textbf{0}$_{\rm I}$, 5.2.7)"),
    F(p, "Proposition (6.13.4): '(ce qui signifie que X est réduit au point x)'",
      "parenthesis roman with 'réduit' italic (enlarged crop)", "all italic (proposition environment)",
      C, 6, "high", r"(ce qui signifie que" + NL + r"$X$ est réduit au point $x$)",
      r"\textup{(ce qui signifie que" + NL + r"$X$ est \emph{réduit} au point $x$)}"),
    F(p, "proof of (6.13.4): 'au cas où X est réduit, i.e.'", "'réduit' italic", "roman",
      C, 6, "high", r"est réduit, i.e.", r"est \emph{réduit}, i.e."),
    F(p, "proof of (6.13.4): 'appartiennent à U_S2(X) et à U_R1(X)'", "U_{S_2} (enlarged crop)", "U_{S_1}",
      "formula", None, "high", r"$U_{S_1}(X)$ et à", r"$U_{S_2}(X)$ et à",
      "Serre's criterion (5.8.6): normal = (R_1) + (S_2)."),
    F(p, "proof of (6.13.4): 'Nor(X) = U_S2(X) ∩ U_R1(X)'", "U_{S_2} (enlarged crop)", "U_{S_1}",
      "formula", None, "high", r"=U_{S_1}(X)\cap", r"=U_{S_2}(X)\cap"),
    F(p, "proof of (6.13.5): 'et a fortiori est intérieur'", "'a fortiori' italic", "roman",
      C, 6, "high", r"a fortiori", r"\emph{a fortiori}"),
    F(p, "Proposition (6.13.6), label (i)", "label upright", "\\item[(i)] italic inside the italic statement",
      C, 6, "high", r"\item[(i)] Il existe", r"\item[\textup{(i)}] Il existe", "GLOBAL_ISSUES 16."),
    F(p, "Proposition (6.13.6) (i), end: 'soit une A_f-algèbre finie.'", "full stop (enlarged crop)", "semicolon",
      "punctuation", None, "high", r"$A_f$-algèbre finie;", r"$A_f$-algèbre finie."),
]
# ---------------------------------------------------------------- page 168 (text printed on p. 169)
L += [
    F(p, "Proposition (6.13.6), label (ii) (printed at the top of p. 169; the text still lies in the p. 168 segment)",
      "label upright", "\\item[(ii)] italic inside the italic statement", C, 6, "high", None, None,
      "Edit included in the marker move at the end of this file (\\oldpage[IV-2]{169} inserted before this \\item)."),
    F(p, "proof of (6.13.6) (printed p. 169): 'soient S_lambda = X_lambda — Nor(X_lambda)'", "long dash", "minus sign",
      C, 7, "high", r"X_\lambda-\operatorname{Nor}(X_\lambda)", r"X_\lambda\setmin\operatorname{Nor}(X_\lambda)",
      "\\setmin pending the convention-7 decision (FIX_POLICY 2.7). Text in the p. 168 segment until the marker move."),
    F(p, "proof of (6.13.6) (printed p. 169): 'S_lambda est donc fermé dans X_lambda'", "'fermé' italic", "roman",
      C, 6, "high", r"donc fermé dans", r"donc \emph{fermé} dans",
      "Text in the p. 168 segment until the marker move."),
    F(p, "proof of (6.13.6) (printed p. 169): 'T_lambda est fermé dans Y'", "'fermé' italic", "roman",
      C, 6, "high", r"$T_\lambda$ est fermé", r"$T_\lambda$ est \emph{fermé}",
      "Text in the p. 168 segment until the marker move."),
]
# ---------------------------------------------------------------- page 169 (text printed on p. 169)
p = 169
L += [
    F(p, "proof of (6.13.6): 'il existe un lambda_0 tel que'", "lambda_0 (enlarged crop)", "lambda",
      "formula", None, "high", r"il existe un $\lambda$ tel que", r"il existe un $\lambda_0$ tel que"),
    F(p, "proof of (6.13.6): 'T_{lambda_0} = ∅'", "T_{lambda_0}", "T_lambda",
      "formula", None, "high", r"$T_\lambda=\varnothing$; donc", r"$T_{\lambda_0}=\varnothing$; donc"),
    F(p, "proof of (6.13.6): 'donc B_{lambda_0} est intégralement clos'", "B_{lambda_0}", "B_lambda",
      "formula", None, "high", r"donc $B_\lambda$ est intégralement clos", r"donc $B_{\lambda_0}$ est intégralement clos"),
    F(p, "proof of (6.13.6): 'on a B_{lambda_0} = A''", "B_{lambda_0}", "B_lambda",
      "formula", None, "high", r"$B_\lambda=A'$", r"$B_{\lambda_0}=A'$"),
    F(p, "Proposition (6.13.7), label a)", "label upright (enlarged crop)", "\\item[a)] italic inside the italic statement",
      C, 6, "high", r"\item[a)]", r"\item[\textup{a)}]"),
    F(p, "Proposition (6.13.7) a), end: 'est ouvert dans X'.'", "full stop", "semicolon",
      "punctuation", None, "high", r"ouvert dans $X'$;", r"ouvert dans $X'$."),
    F(p, "Proposition (6.13.7), label b)", "label upright", "\\item[b)] italic inside the italic statement",
      C, 6, "high", r"\item[b)]", r"\item[\textup{b)}]"),
    F(p, "Proposition (6.13.7) b), end: 'est ouvert dans Spec(A').'", "full stop", "semicolon",
      "punctuation", None, "high", r"dans" + NL + r"$\operatorname{Spec}(A')$;", r"dans" + NL + r"$\operatorname{Spec}(A')$."),
    F(p, "Proposition (6.13.7), label c)", "label upright", "\\item[c)] italic inside the italic statement",
      C, 6, "high", r"\item[c)]", r"\item[\textup{c)}]"),
    F(p, "proof of (6.13.7): 'Le fait que a) implique'", "'a)' italic", "roman",
      C, 6, "high", r"que a) implique", r"que \emph{a)} implique"),
    F(p, "proof of (6.13.7): 'implique b) et'", "'b)' italic", "roman",
      C, 6, "high", r"implique b) et", r"implique \emph{b)} et"),
    F(p, "proof of (6.13.7): 'et que b) implique'", "'b)' italic", "roman",
      C, 6, "high", r"que b) implique", r"que \emph{b)} implique"),
    F(p, "proof of (6.13.7): 'implique c) se prouve'", "'c)' italic", "roman",
      C, 6, "high", r"implique c) se", r"implique \emph{c)} se"),
    F(p, "proof of (6.13.7): 'Pour montrer que c) entraîne'", "'c)' italic", "roman",
      C, 6, "high", r"que c) entraîne", r"que \emph{c)} entraîne"),
    F(p, "proof of (6.13.7): 'entraîne a), compte tenu'", "'a)' italic", "roman",
      C, 6, "high", r"entraîne a), compte", r"entraîne \emph{a)}, compte"),
    F(p, "proof of (6.13.7.1): '(Bourbaki, Alg. comm., chap. V'", "'Alg. comm.' italic", "roman",
      C, 6, "high", r"Alg. comm., chap. V", r"\emph{Alg. comm.}, chap. V"),
    F(p, "proof of (6.13.7.1): '§ 1, n° 3, cor. 2'", "n° with a roman superior o", "n$^o$ (math italic o)",
      "font", None, "medium", r"n$^o$ 3, cor. 2", r"n\textsuperscript{o} 3, cor. 2"),
    F(p, "proof of (6.13.7.1): 'A' est un A-module libre de type fini'", "'libre de type fini' italic", "roman",
      C, 6, "high", r"module libre de type fini;", r"module \emph{libre de type fini};"),
    F(p, "proof of (6.13.7.1): 'sont régulières et a fortiori normales'", "'a fortiori' italic", "roman",
      C, 6, "high", r"a fortiori", r"\emph{a fortiori}"),
    F(p, "proof of (6.13.7): 'comme dans (6.12.4; II))'", "semicolon (enlarged crop)", "comma",
      "punctuation", None, "high", r"(6.12.4, II))", r"(6.12.4; II))",
      "Printed with a semicolon; the usual form would have a comma, but the meaning is unaffected, so it is not "
      "treated as a misprint."),
    F(p, "proof of (6.13.7): 'appliquant l'hypothèse c), on voit'", "'c)' italic", "roman",
      C, 6, "high", r"l'hypothèse c),", r"l'hypothèse \emph{c)},"),
    F(p, "proof of (6.13.7): 'X'_1 est normal et g : X' -> X' plat et surjectif'",
      "g : X' -> X' (no subscript 1 on the source; enlarged crop)", "g:X'_1\\to X' (silent correction)",
      "misprint_in_print", None, "high", r"$g:X'_1\to X'$ plat", r"$g:X'\to X'$ plat",
      "Misprint of the print: g is the morphism X'_1 -> X' of (6.12.4, II). The TeX silently corrects it; the fix "
      "restores the printed reading.", corrected=r"$g:X'_1\to X'$"),
    F(p, "heading 6.14", "'Changement de base et clôture intégrale.' with full stop", "no full stop",
      "punctuation", None, "high", r"\subsection{Changement de base et clôture intégrale}",
      r"\subsection{Changement de base et clôture intégrale.}", "GLOBAL_ISSUES 43/58 pattern."),
    F(p, "Proposition (6.14.1): 'un morphisme normal (6.8.1)'", "reference upright (enlarged crop)",
      "italic (proposition environment)", C, 6, "high", r"normal (6.8.1).", r"normal \textup{(6.8.1)}."),
    F(p, "after Proposition (6.14.1): 'On notera que dans cet énoncé'", "'On notera que'", "'Notons que'",
      "word", None, "high", r"Notons que dans cet énoncé", r"On notera que dans cet énoncé"),
    F(p, "after Proposition (6.14.1): 'on ne suppose pas X localement noethérien'", "italic", "roman",
      C, 6, "high", r"on ne suppose pas $X$ localement noethérien.", r"\emph{on ne suppose pas $X$ localement noethérien}."),
]
# ---------------------------------------------------------------- page 169 (text printed on p. 170)
L += [
    F(p, "Lemme (6.14.1.1), label (i) (printed at the top of p. 170)", "label upright",
      "\\item[(i)] italic inside the italic statement", C, 6, "high",
      r"\item[(i)] Pour qu'un", r"\item[\textup{(i)}] Pour qu'un",
      "GLOBAL_ISSUES 16. Text printed on p. 170 (checked against page_170 strip 1); it lies in the p. 169 segment "
      "until the marker move."),
    F(p, "Lemme (6.14.1.1), label (ii) (printed p. 170)", "label upright",
      "\\item[(ii)] italic inside the italic statement", C, 6, "high",
      r"\item[(ii)] Soit $(A_\lambda)$", r"\item[\textup{(ii)}] Soit $(A_\lambda)$", "GLOBAL_ISSUES 16. Printed on p. 170."),
    F(p, "proof of (6.14.1.1) (i) (printed p. 170): '(Bourbaki, Alg. comm., chap. II'", "'Alg. comm.' italic", "roman",
      C, 6, "high", r"Alg. comm., chap." + NL + r"II", r"\emph{Alg. comm.}, chap." + NL + r"II", "Printed on p. 170."),
    F(p, "proof of (6.14.1.1) (i) (printed p. 170): '§ 3, n° 3, cor. 1'", "n° with a roman superior o",
      "n$^o$ (math italic o)", "font", None, "medium", r"n$^o$ 3, cor. 1", r"n\textsuperscript{o} 3, cor. 1",
      "Printed on p. 170."),
]
# ---------------------------------------------------------------- marker moves: apply last, in this order
L += [
    F(168, "page break 168/169: marker position (edit 1 of 2, insert)",
      "printed p. 168 ends with Proposition (6.13.6) (i) '... soit une A_f-algèbre finie.'; p. 169 begins with '(ii) Pour "
      "tout idéal premier'", "\\oldpage[IV-2]{169} stands 25 source lines later, before 'de X_lambda au-dessus de p' in the "
      "proof of (6.13.6)", "marker", None, "high",
      r"\item[(ii)] Pour tout idéal premier", r"\oldpage[IV-2]{169}" + NL + r"\item[\textup{(ii)}] Pour tout idéal premier",
      "Also carries the convention-6 label fix for (ii) (finding above with fix null). Apply after every other p. 168 "
      "entry and together with the next edit, which removes the old marker; afterwards (ii), the proof of (6.13.6) "
      "up to 'et par suite tous les points' belong to p. 169, as printed."),
    F(169, "page break 168/169: marker position (edit 2 of 2, remove the misplaced marker)",
      "'... et par suite tous les points de X_lambda au-dessus de p' runs on inside printed p. 169",
      "misplaced \\oldpage[IV-2]{169}", "marker", None, "high",
      r"\oldpage[IV-2]{169}" + NL + r"de $X_\lambda$", r"de $X_\lambda$",
      "Apply together with, and after, the previous edit (no blank lines are left around the old position)."),
    F(169, "page break 169/170: marker position (edit 1 of 2, insert)",
      "printed p. 169 ends with Lemme (6.14.1.1) 'Soit R un anneau composé direct d'un nombre fini de corps.'; p. 170 "
      "begins with its item (i)", "\\oldpage[IV-2]{170} stands before '(ii) Comme A ⊂ A_lambda ⊂ R' in the proof",
      "marker", None, "high",
      r"fini de corps." + NL + r"\begin{enumerate}", r"fini de corps." + NL + r"\oldpage[IV-2]{170}" + NL + r"\begin{enumerate}",
      "Marker before \\begin{enumerate} (still in the paragraph, so the \\marginpar is not put before the first \\item). "
      "Apply after every other p. 169 entry and after the two edits above, together with the next edit."),
    F(170, "page break 169/170: marker position (edit 2 of 2, remove the misplaced marker; page_170.tex)",
      "'(ii) Comme A ⊂ A_lambda ⊂ R' is in the middle of printed p. 170", "misplaced \\oldpage[IV-2]{170}",
      "marker", None, "high", r"\oldpage[IV-2]{170}" + NL + r"(ii) Comme", r"(ii) Comme",
      "Outside pp. 165-169 (page_170.tex). Apply together with, and after, the previous edit; the blank line before the "
      "old marker stays, so '(ii) Comme' still opens a paragraph, as printed. Skip both if the pp. 170-174 batch "
      "moves this marker."),
]

# ---------------------------------------------------------------- checks
ok = True
pages = {}
for n in range(165, 171):
    pages[n] = (RUN / f"page_{n}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
for i, x in enumerate(L):
    if x["fix"] is None:
        continue
    c = pages[x["page"]].count(x["fix"]["old"])
    if c != 1:
        ok = False
        print(f"#{i} page {x['page']}: old occurs {c} times: {x['fix']['old']!r}")

# dry run on the release source, with the locate() rule of apply_fixes.py
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


t = src
for i, x in enumerate(L):
    if x["fix"] is None:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print(f"DRY #{i} page {x['page']}: old occurs {c} times in the segment: {x['fix']['old']!r}")
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]

json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
(HERE / "dryrun_result.txt").write_text(t[t.index(r"\oldpage[IV-2]{165}"):t.index(r"\oldpage[IV-2]{171}")],
                                         encoding="utf-8")
cnt = {}
for x in L:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("ok" if ok else "PROBLEMS", len(L), cnt)
sys.exit(0 if ok else 1)
