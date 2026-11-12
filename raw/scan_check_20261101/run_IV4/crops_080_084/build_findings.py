"""Build findings_080_084.json for EGA IV-4 pp. 80-84 and verify every fix.

Checks: (1) each "old" occurs exactly once in its page segment of the CURRENT release file when the fixes are applied
in list order, with the page segments recomputed as apply_fixes.py does (markers may move); (2) the same in the
page_NNN.tex copies (CRLF normalised), applied page by page in list order; (3) reports which fixes depend on an
earlier fix (old absent from the original page text).
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
RUN = E / "run_IV4"
SRC = E / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-17-fr.tex"
OUT = RUN / "findings_080_084.json"
NL = "\n"

F = []


def add(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention, confidence=confidence,
             fix=None if old is None else dict(old=old, new=new))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 80
add(80, "Corollaire (17.9.3): 'un morphisme étale (resp. étale et séparé). Alors'",
    "'(resp.' and the closing parenthesis upright inside the italic statement (crop p80_resp1.png)",
    "italic (whole statement in the italic environment)", "convention",
    r"un morphisme étale (resp. étale et séparé). Alors",
    r"un morphisme étale \textup{(resp.}\ étale et séparé\textup{)}. Alors", convention=6)
add(80, "Corollaire (17.9.3): 'une immersion ouverte (resp. ouverte et fermée); en outre'",
    "'(resp.' and ')' upright (crop p80_resp2.png)", "italic", "convention",
    r"immersion ouverte (resp. ouverte et fermée); en outre",
    r"immersion ouverte \textup{(resp.}\ ouverte et fermée\textup{)}; en outre", convention=6)
add(80, "Corollaire (17.9.3): 'l'application g ⇝ g(Y) est une bijection de l'ensemble Γ(X/Y)'",
    "wavy arrow (crop p80_leadsto1.png)", "\\mapsto", "symbol",
    r"l'application $g\mapsto g(Y)$ est une bijection de l'ensemble",
    r"l'application $g\leadsto g(Y)$ est une bijection de l'ensemble")
add(80, "Corollaire (17.9.3): 'des parties ouvertes Z (resp. ouvertes et fermées) de X'",
    "'(resp.' and ')' upright", "italic", "convention",
    r"parties ouvertes $Z$ (resp. ouvertes et fermées) de $X$",
    r"parties ouvertes $Z$ \textup{(resp.}\ ouvertes et fermées\textup{)} de $X$", convention=6)
add(80, "proof of (17.9.3): 'non ramifié (17.4.1, b''))'",
    "label b'') italic, its parenthesis included (crop p80_b2prime.png)",
    "$b''$) : italic b with an upright parenthesis", "italics",
    r"(17.4.1, $b''$))", r"(17.4.1, \emph{b$''$)})", note="Labels in roman text are italic in the print (GLOBAL_ISSUES 88).")
add(80, "proof of (17.9.3): 'une immersion fermée (I, 5.4.6)'",
    "bold Roman numeral I: (I, 5.4.6), i.e. EGA I (crop p80_I546.png)", "'(1, 5.4.6)': the digit 1", "number",
    r"(1, 5.4.6)", r"(\textbf{I}, 5.4.6)",
    note="Wrong character (digit 1 for the numeral I). The edit also sets the bold of convention 2 (\\textbf{I}, as the other page fixes).")
add(80, "Corollaire (17.9.4): 'l'application g ⇝ g(Y) est une bijection de Γ(X/Y)'",
    "wavy arrow (crop p80_leadsto2.png)", "\\mapsto", "symbol",
    r"l'application $g\mapsto g(Y)$ est une bijection de $\Gamma(X/Y)$",
    r"l'application $g\leadsto g(Y)$ est une bijection de $\Gamma(X/Y)$")
add(80, "Corollaire (17.9.5): 'on suppose en outre que h est plat.'",
    "'plat' roman inside the italic statement (the authors' emphasis; crop p80_plat.png)", "italic", "convention",
    r"que $h$ est plat. Pour", r"que $h$ est \textup{plat}. Pour", convention=6,
    note="Same form as the page fix of (17.8.2), p. 79.")
add(80, "Corollaire (17.9.5): 'soit une immersion ouverte (resp. un isomorphisme), il faut'",
    "'(resp.' and ')' upright", "italic", "convention",
    r"immersion ouverte (resp. un isomorphisme), il faut",
    r"immersion ouverte \textup{(resp.}\ un isomorphisme\textup{)}, il faut", convention=6)
add(80, "Corollaire (17.9.5): 'le changement de base Spec(k(s)) → S'",
    "bold italic k (crop p80_kspec.png)", "plain k", "convention",
    r"$\Spec(k(s))\to S$", r"$\Spec(\boldsymbol{k}(s))\to S$", convention=1)
add(80, "Corollaire (17.9.5), end: 'soit une immersion ouverte (resp. un isomorphisme).'",
    "'(resp.' and ')' upright", "italic", "convention",
    "soit une immersion ouverte (resp. un isomorphisme)." + NL + r"\end{corollary}",
    r"soit une immersion ouverte \textup{(resp.}\ un isomorphisme\textup{)}." + NL + r"\end{corollary}", convention=6)
add(80, "page break 80/81 inside 'il suffira donc de montrer | que g est une immersion ouverte'",
    "p. 80 ends 'il suffira donc de montrer', p. 81 begins 'que g est une immersion ouverte' in the same sentence",
    "blank line before \\oldpage[IV-4]{81} (and another after it): a paragraph break inside the sentence", "marker",
    "de montrer" + NL + NL, "de montrer" + NL,
    note="GLOBAL_ISSUES 20/99. The marker is at the right place. Part 1 of 2: the first p. 81 finding removes the blank line after \\oldpage[IV-4]{81}; apply both.")

# ---------------------------------------------------------------- page 81
add(81, "top of page_081.tex: blank line after \\oldpage[IV-4]{81}",
    "p. 81 begins mid-sentence ('que g est une immersion ouverte')", "blank line between the marker and 'que'", "marker",
    r"\oldpage[IV-4]{81}" + NL + NL + "que $g$", r"\oldpage[IV-4]{81}" + NL + "que $g$",
    note="Part 2 of 2 with the p. 80 marker finding (blank line before the marker); both blank lines must go.")
add(81, "proof of (17.9.6): 'il suffira ... de prouver que g est étale.'",
    "'étale' italic (crop p81_etale.png)", "roman", "italics",
    r"de prouver que $g$ est étale. En outre", r"de prouver que $g$ est \emph{étale}. En outre")
add(81, "proof of (17.9.6): 'l'application k(z') → k(z) déduite de g'",
    "bold italic k twice", "plain k", "convention",
    r"l'application $k(z')\to k(z)$ déduite", r"l'application $\boldsymbol{k}(z')\to\boldsymbol{k}(z)$ déduite",
    convention=1, note="Two occurrences in one formula.")
add(81, "proof of (17.9.6): 'soit bijectif (17.6.3, e''))'",
    "label e'') italic, its parenthesis included (crop p81_eprime.png)", "$e''$) : upright parenthesis", "italics",
    r"(17.6.3, $e''$))", r"(17.6.3, \emph{e$''$)})", note="GLOBAL_ISSUES 88.")
add(81, "proof of (17.9.6): 'O_{X,z'}/m_{z'}^{n+1} → O_{X,z}/m_z^{n+1} est bijectif'",
    "'bijectif' italic (crop p81_bijectif.png)", "roman", "italics",
    r"est bijectif, d'où résultera", r"est \emph{bijectif}, d'où résultera")
add(81, "proof of (17.9.6): 'tels que k(t) soit une extension de F_p'",
    "bold italic k", "plain k", "convention",
    r"tels que $k(t)$ soit", r"tels que $\boldsymbol{k}(t)$ soit", convention=1,
    note="The bold F of F_p is \\mathbb{F} in the TeX: same document-wide item as the bold Z, Q, R.")
add(81, "proof of (17.9.6): 'Désignons par J l'Idéal cohérent de O_X'",
    "'Idéal' with a capital I (crop p81_ideal.png)", "'idéal'", "word",
    r"l'idéal cohérent de", r"l'Idéal cohérent de",
    note="The script letter is the printed J (with descender): \\sh{J} is right.")
add(81, "proof of (17.9.6): 'l'homomorphisme O_{X,g(x)} → O_{X,x}/m^{n+1} se factorise en'",
    "m^{n+1} WITHOUT the subscript x (crop p81_factorise.png); the display just below has m_x^{n+1}",
    "\\mathfrak m_x^{n+1}: silent correction", "misprint_in_print",
    r"\to\sh{O}_{X,x}/\mathfrak m_x^{n+1}$ se factorise", r"\to\sh{O}_{X,x}/\mathfrak m^{n+1}$ se factorise",
    corrected=r"\to\sh{O}_{X,x}/\mathfrak m_x^{n+1}$ se factorise",
    note="Missing subscript in the print; the diplomatic text restores the printed m^{n+1}.")
add(81, "proof of (17.9.6): 'Donc (I, 4.1.9) il existe'",
    "bold I (crop p81_donc.png)", "plain I", "convention",
    r"Donc (I, ", r"Donc (\textbf{I}, ", convention=2,
    note="Independent of the two edits after it (number 4.1.9, comma).")
add(81, "proof of (17.9.6): 'Donc (I, 4.1.9) il existe'",
    "4.1.9 (crop p81_donc.png)", "'4.9': the middle number dropped", "number",
    r"4.9)", r"4.1.9)")
add(81, "proof of (17.9.6): 'Donc (I, 4.1.9) il existe un unique endomorphisme'",
    "no comma after the reference (crop p81_donc.png)", "'(I, 4.9), il existe': comma added", "punctuation",
    r"), il existe un unique", r") il existe un unique")
add(81, "proof of (17.9.6): 'on a vu que k(x) est un corps fini'",
    "bold italic k", "plain k", "convention",
    r"on a vu que $k(x)$ est un corps fini", r"on a vu que $\boldsymbol{k}(x)$ est un corps fini", convention=1)
add(81, "proof of (17.9.6): 'est un k(x)-espace vectoriel de rang fini'",
    "bold italic k", "plain k", "convention",
    r"est un $k(x)$-espace vectoriel", r"est un $\boldsymbol{k}(x)$-espace vectoriel", convention=1)
add(81, "proof of (17.9.6): 'lui aussi fini (II, 6.1.5, (v))'",
    "bold II (crop p81_II615.png)", "plain II", "convention",
    r"(II, 6.", r"(\textbf{II}, 6.", convention=2,
    note="Independent of the misprint edit of the 5 in the same reference.")
add(81, "proof of (17.9.6): '(II, 6.1.5, (v))', the digit 5",
    "the 5 is a bold 5 (wrong fount), visibly heavier than the 5 of (8.11.5) one line below in the same small type "
    "(crops p81_615_zoom.png, cmp_heavy5.png against cmp_norm5.png)",
    "normal 5 (silent correction)", "misprint_in_print",
    r"6.1.5, (v)", r"6.1.\textbf{5}, (v)", corrected=r"6.1.5, (v)", confidence="medium",
    note="Wrong-fount digit recorded as a misprint (GLOBAL_ISSUES 29/99). Not damaged type: the whole glyph (flag, stem, "
         "bowl) is heavier. Independent of the convention-2 edit of (II, 6. before it.")
add(81, "subsection title 17.10",
    "'17.10. Dimension relative d'un préschéma lisse sur un autre.' with a full stop", "no full stop", "punctuation",
    r"\subsection{Dimension relative d'un préschéma lisse sur un autre}",
    r"\subsection{Dimension relative d'un préschéma lisse sur un autre.}", note="GLOBAL_ISSUES 43/58.")
add(81, "Définition (17.10.1): 'On appelle dimension relative de f au point x∈X (ou dimension relative de X sur Y au point x)'",
    "both defined phrases italic like the rest of the definition; no change of face (crop p81_def.png)",
    "\\emph{...} twice inside the italic environment: printed upright", "italics",
    r"\emph{dimension relative de $f$ au point $x\in X$} (ou \emph{dimension relative de $X$ sur $Y$ au point $x$})",
    r"dimension relative de $f$ au point $x\in X$ (ou dimension relative de $X$ sur $Y$ au point $x$)",
    note="FIX_POLICY 2.6: drop \\emph where the print shows no change of face. The parentheses are italic in the print (crop p81_xparen.png).")
add(81, "after (17.10.1): 'Dire que f est quasi-fini au point x (Err_III, 20)'",
    "bold upright 'Err' with a light roman subscript III (crop p81_err.png)", "normal-weight Err", "font",
    r"(Err$_{\mathrm{III}}$, 20)", r"(\textbf{Err}$_{\mathrm{III}}$, 20)",
    note="Same form as the earlier page fixes; roman text, so no \\textup.")
add(81, "after (17.10.1): 'la fonction x ⇝ dim_x f est semi-continue supérieurement'",
    "wavy arrow", "\\mapsto", "symbol",
    r"la fonction $x\mapsto\dim_x f$ est semi-continue", r"la fonction $x\leadsto\dim_x f$ est semi-continue")
add(81, "after (17.10.1): 'la fonction x ⇝ dim_x f n'est pas nécessairement continue'",
    "wavy arrow", "\\mapsto", "symbol",
    r"la fonction $x\mapsto\dim_x f$ n'est pas", r"la fonction $x\leadsto\dim_x f$ n'est pas")
add(81, "example after (17.10.1): 'q=(U)+(V—W)'",
    "long dash for the subtraction V—W (crop p81_pq.png)", "minus sign", "convention",
    r"(V-W)", r"(V\setmin W)", convention=7,
    note="Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes, pending the convention-7 decision.")
add(81, "Proposition (17.10.2): 'le O_{X,x}-Module localement libre Ω^1_f'",
    "O_{X,x}-Module: subscript 'X, x' (crop p81_prop.png); Ω^1_f is a sheaf on X, so O_X is meant",
    "$\\sh{O}_X$-Module: silent correction", "misprint_in_print",
    r"le $\sh{O}_X$-Module localement libre", r"le $\sh{O}_{X,x}$-Module localement libre",
    corrected=r"le $\sh{O}_X$-Module localement libre",
    note="The diplomatic text restores the printed O_{X,x}.")
add(81, "Proposition (17.10.2): 'localement libre Ω^1_f (17.2.3)'",
    "italic Ω (sheaf of differentials)", "upright \\Omega", "font",
    r"libre $\Omega_f^1$", r"libre $\varOmega_f^1$", note="GLOBAL_ISSUES 92.")
add(81, "Proposition (17.10.2): 'Ω^1_f (17.2.3) a un rang en x'",
    "(17.2.3) upright inside the italic statement", "italic", "convention",
    r"(17.2.3) a un rang en", r"\textup{(17.2.3)} a un rang en", convention=6)
add(81, "Proposition (17.10.2): '(ce qui entraîne que x ⇝ dim_x f est une fonction continue dans X)'",
    "the whole parenthesis roman inside the italic statement, 'continue' italic; wavy arrow (crops p81_prop.png, p81_prop2.png)",
    "italic parenthesis; \\mapsto; 'continue' not distinguished", "convention",
    r"(ce qui entraîne que $x\mapsto\dim_x f$ est une fonction continue dans $X$)",
    r"\textup{(ce qui entraîne que $x\leadsto\dim_x f$ est une fonction \emph{continue} dans $X$)}", convention=6,
    note="One edit for three differences: convention 6 for the roman parenthesis, the wavy arrow (symbol) and the italic 'continue' (\\emph inside \\textup).")
add(81, "proof of (17.10.2): 'X_y=f^{-1}(y) est lisse sur k(y)'",
    "bold italic k", "plain k", "convention",
    r"est lisse sur $k(y)$, et si", r"est lisse sur $\boldsymbol{k}(y)$, et si", convention=1)
add(81, "proof of (17.10.2): 'f_y : X_y → Spec(k(y))'",
    "bold italic k", "plain k", "convention",
    r"X_y\to\Spec(k(y))$ est le morphisme", r"X_y\to\Spec(\boldsymbol{k}(y))$ est le morphisme", convention=1)
add(81, "proof of (17.10.2): 'on a Ω^1_{f_y} = Ω^1_f ⊗ ...'",
    "italic Ω twice (sheaves)", "upright \\Omega", "font",
    r"on a $\Omega_{f_y}^1=\Omega_f^1", r"on a $\varOmega_{f_y}^1=\varOmega_f^1", note="GLOBAL_ISSUES 92.")
add(81, "proof of (17.10.2): 'on a Ω^1_{f_y} = Ω^1_f ⊗_{O_{Y,y}} k(y) (16.4.5)'",
    "the tensor product is ⊗_{O_{Y,y}} k(y), with a bold italic k (crop p81_omegafy.png)",
    "'\\otimes_{\\sh{O}_X}\\sh{O}_{X_y}': a different formula", "formula",
    r"\otimes_{\sh{O}_X}\sh{O}_{X_y}$ (16.4.5)", r"\otimes_{\sh{O}_{Y,y}}\boldsymbol{k}(y)$ (16.4.5)",
    note="The TeX replaced the printed formula. The new k(y) is written bold italic as printed (convention 1). Independent of the Omega edit before it.")
add(81, "page break 81/82 inside 'autrement dit | supposer k algébriquement clos'",
    "p. 81 ends 'autrement dit', p. 82 begins 'supposer k algébriquement clos'",
    "blank line before \\oldpage[IV-4]{82} (and another after it): a paragraph break inside the sentence", "marker",
    "autrement dit" + NL + NL, "autrement dit" + NL,
    note="GLOBAL_ISSUES 20/99. The marker is at the right place. Part 1 of 2: the first p. 82 finding removes the blank line after \\oldpage[IV-4]{82}; apply both.")

# ---------------------------------------------------------------- page 82
add(82, "top of page_082.tex: blank line after \\oldpage[IV-4]{82}",
    "p. 82 begins mid-sentence ('supposer k algébriquement clos')", "blank line between the marker and 'supposer'", "marker",
    r"\oldpage[IV-4]{82}" + NL + NL + "supposer", r"\oldpage[IV-4]{82}" + NL + "supposer",
    note="Part 2 of 2 with the p. 81 marker finding; both blank lines must go.")
add(82, "proof of (17.10.2): 'supposer k algébriquement clos.'",
    "'algébriquement clos' italic (crop p82_alg.png)", "roman", "italics",
    r"supposer $k$ algébriquement clos.", r"supposer $k$ \emph{algébriquement clos}.",
    note="Independent of the marker edit before it.")
add(82, "proof of (17.10.2): 'Or (16.4.12) (Ω^1_{X/k})_x ⊗ ...'",
    "italic Ω (sheaf)", "upright \\Omega", "font",
    r"Or (16.4.12) $(\Omega^1_{X/k})", r"Or (16.4.12) $(\varOmega^1_{X/k})", note="GLOBAL_ISSUES 92.")
add(82, "proof of (17.10.2): '(Ω^1_{X/k})_x ⊗_{O_x} k(x)'",
    "subscript O_x of the tensor sign (crop p82_omegaxk.png)", "\\sh{O}_{X,x}", "formula",
    r"X/k})_x\otimes_{\sh{O}_{X,x}}", r"X/k})_x\otimes_{\sh{O}_x}",
    note="Independent of the Omega edit before it and the k(x) edit after it.")
add(82, "proof of (17.10.2): '⊗_{O_x} k(x) est alors k-isomorphe'",
    "bold italic k", "plain k", "convention",
    r"}k(x)$ est alors", r"}\boldsymbol{k}(x)$ est alors", convention=1)
add(82, "proof of (17.10.2): 'rg_k(m_x/m_x^2) = dim(O_x)'",
    "subscript k of rg (crop p82_rgk.png)", "rg_{k(x)}", "formula",
    r"\operatorname{rg}_{k(x)}(\mathfrak m_x", r"\operatorname{rg}_k(\mathfrak m_x")
add(82, "proof of (17.10.2): '(0, 17.1.1)'", "bold 0", "plain 0", "convention",
    r"(0, 17.1.1)", r"(\textbf{0}, 17.1.1)", convention=2)
add(82, "proof of (17.10.2): 'rg_{O_x}(Ω^1_{X/k})_x = dim(O_x)'",
    "italic Ω (sheaf)", "upright \\Omega", "font",
    r"\operatorname{rg}_{\sh{O}_x}(\Omega^1_{X/k})_x", r"\operatorname{rg}_{\sh{O}_x}(\varOmega^1_{X/k})_x",
    note="GLOBAL_ISSUES 92.")
add(82, "proof of (17.10.2): 'Mais puisque k(x)=k'",
    "bold italic k in k(x); the k after = is a light italic k", "plain k", "convention",
    r"Mais puisque $k(x)=k$", r"Mais puisque $\boldsymbol{k}(x)=k$", convention=1)
add(82, "proof of (17.10.3): 'les trois O_X-Modules Ω^1_{X/Y}, Ω^1_{X/Z} et f^*(Ω^1_{Y/Z})'",
    "italic Ω three times (crop p82_s2top.png)", "upright \\Omega", "font",
    r"Modules $\Omega^1_{X/Y}$, $\Omega^1_{X/Z}$ et $f^*(\Omega^1_{Y/Z})$ sont",
    r"Modules $\varOmega^1_{X/Y}$, $\varOmega^1_{X/Z}$ et $f^*(\varOmega^1_{Y/Z})$ sont", note="GLOBAL_ISSUES 92.")
add(82, "proof of (17.10.3): '(17.2.3 et 0_I, 5.4.5)'",
    "bold 0 with a light subscript I", "plain 0", "convention",
    r"(17.2.3 et $0_{\mathrm I}$, 5.4.5)", r"(17.2.3 et $\mathbf{0}_{\mathrm I}$, 5.4.5)", convention=2)
add(82, "proof of (17.10.3): 'le rang en x de f^*(Ω^1_{Y/Z}) est égal au rang en y=f(x) de Ω^1_{Y/Z}'",
    "italic Ω twice", "upright \\Omega", "font",
    r"de $f^*(\Omega^1_{Y/Z})$ est égal au rang en $y=f(x)$ de $\Omega^1_{Y/Z}$.",
    r"de $f^*(\varOmega^1_{Y/Z})$ est égal au rang en $y=f(x)$ de $\varOmega^1_{Y/Z}$.", note="GLOBAL_ISSUES 92.")
add(82, "proof of (17.10.4): 'Ω^1_{X/Y} ⊗_{O_X} O_{X'} et Ω^1_{X'/Y}'",
    "italic Ω twice (crop p82_effet2.png)", "upright \\Omega", "font",
    r"En effet, $\Omega^1_{X/Y}\otimes_{\sh{O}_X}\sh{O}_{X'}$ et $\Omega^1_{X'/Y}$ sont",
    r"En effet, $\varOmega^1_{X/Y}\otimes_{\sh{O}_X}\sh{O}_{X'}$ et $\varOmega^1_{X'/Y}$ sont", note="GLOBAL_ISSUES 92.")
add(82, "subsection title 17.11",
    "'17.11. Morphismes lisses de préschémas lisses.' with a full stop", "no full stop", "punctuation",
    r"\subsection{Morphismes lisses de préschémas lisses}", r"\subsection{Morphismes lisses de préschémas lisses.}",
    note="GLOBAL_ISSUES 43/58.")
add(82, "Théorème (17.11.1), label a)", "'a)' upright (crop p82_labels.png)", "italic label", "convention",
    r"\item[a)] $f$ est lisse au point $y$ et $g$ est lisse", r"\item[\textup{a)}] $f$ est lisse au point $y$ et $g$ est lisse",
    convention=6, note="GLOBAL_ISSUES 16/88.")
add(82, "Théorème (17.11.1), label b)", "'b)' upright", "italic label", "convention",
    r"\item[b)] $g$ et $h$ sont lisses", r"\item[\textup{b)}] $g$ et $h$ sont lisses", convention=6)
add(82, "Théorème (17.11.1) c): label c) and 'l'homomorphisme canonique (16.4.18)'",
    "'c)' and '(16.4.18)' upright", "italic", "convention",
    r"\item[c)] $h$ est lisse au point $x$, et l'homomorphisme canonique (16.4.18)",
    r"\item[\textup{c)}] $h$ est lisse au point $x$, et l'homomorphisme canonique \textup{(16.4.18)}", convention=6,
    note="One edit for the label and the reference.")
add(82, "display (17.11.1.1): '(g^*(Ω^1_{Y/S}))_x → (Ω^1_{X/S})_x'",
    "italic Ω twice (crop p82_disp1.png)", "upright \\Omega", "font",
    r"(g^*(\Omega^1_{Y/S}))_x\to(\Omega^1_{X/S})_x", r"(g^*(\varOmega^1_{Y/S}))_x\to(\varOmega^1_{X/S})_x",
    note="GLOBAL_ISSUES 92.")
add(82, "Théorème (17.11.1) c): '(autrement dit est un isomorphisme sur un facteur direct de (Ω^1_{X/S})_x)'",
    "the parenthesis roman inside the italic statement, 'facteur direct de' italic, italic Ω (crop p82_autrement.png)",
    "italic parenthesis with \\emph{facteur direct} (upright) and 'de' italic; upright \\Omega", "convention",
    r"(autrement dit est un isomorphisme sur un \emph{facteur direct} de $(\Omega^1_{X/S})_x$)",
    r"\textup{(autrement dit est un isomorphisme sur un \emph{facteur direct de} $(\varOmega^1_{X/S})_x$)}", convention=6,
    note="One edit for three differences: convention 6 for the roman parenthesis, italic 'facteur direct de' (the \\emph now "
         "inside \\textup gives italic, and takes in 'de'), and the italic Omega (font).")
add(82, "Théorème (17.11.1), label c')", "'c')' upright", "italic label", "convention",
    r"\item[c')]", r"\item[\textup{c$'$)}]", convention=6)
add(82, "display (17.11.1.2): '((Ω^1_{Y/S})_y ⊗ k(y)) ⊗_{k(y)} k(x) → (Ω^1_{X/S})_x ⊗ k(x)'",
    "italic Ω twice", "upright \\Omega", "font",
    r"((\Omega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}k(y))\otimes_{k(y)}k(x)\to(\Omega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}k(x)",
    r"((\varOmega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}k(y))\otimes_{k(y)}k(x)\to(\varOmega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}k(x)",
    note="GLOBAL_ISSUES 92. Part 1 of 2 on this formula: apply before the convention-1 edit that follows.")
add(82, "display (17.11.1.2): k(y), ⊗_{k(y)}, k(x), k(x)",
    "bold italic k three times; the subscript k of ⊗_{k(y)} bold upright (crop p82_disp2.png)", "plain k four times",
    "convention",
    r"((\varOmega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}k(y))\otimes_{k(y)}k(x)\to(\varOmega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}k(x)",
    r"((\varOmega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}\boldsymbol{k}(y))\otimes_{\mathbf{k}(y)}\boldsymbol{k}(x)\to(\varOmega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x)",
    convention=1, note="Part 2 of 2: 'old' is the text after the preceding Omega edit (apply that first). Subscript k bold upright (\\mathbf, GLOBAL_ISSUES 48).")
add(82, "Théorème (17.11.1): 'Supposons en outre que ...' after the list",
    "a new indented paragraph (page_082_s4.png)", "text right after \\end{enumerate}: set without indent", "other",
    r"\end{enumerate}" + NL + "Supposons en outre", r"\end{enumerate}" + NL + NL + "Supposons en outre",
    note="Missing paragraph break (GLOBAL_ISSUES 80/99 pattern).")
add(82, "Théorème (17.11.1): 'l'homomorphisme k(y) → k(x) soit bijectif'",
    "bold italic k twice", "plain k", "convention",
    r"l'homomorphisme $k(y)\to k(x)$ soit bijectif", r"l'homomorphisme $\boldsymbol{k}(y)\to\boldsymbol{k}(x)$ soit bijectif",
    convention=1)
add(82, "Théorème (17.11.1), label d) (printed p. 83)", "'d)' upright (crop p83_d.png)", "italic label", "convention",
    r"\item[d)] $h$ est lisse au point $x$, et l'application canonique",
    r"\item[\textup{d)}] $h$ est lisse au point $x$, et l'application canonique", convention=6,
    note="Printed on p. 83; the text is in the TeX's p. 82 segment until the marker-83 move at the end of the p. 82 findings: apply this before it.")
add(82, "Théorème (17.11.1) d): 'tangent en y à Y (16.5.12) est surjective' (printed p. 83)",
    "(16.5.12) upright", "italic", "convention",
    r"tangent en $y$ à $Y$ (16.5.12) est surjective.", r"tangent en $y$ à $Y$ \textup{(16.5.12)} est surjective.",
    convention=6, note="Printed on p. 83; apply before the marker-83 move (last p. 82 finding).")
add(82, "proof of (17.11.1): 'Le fait que a) entraîne b) résulte' (printed p. 83)",
    "labels italic, parenthesis included (crop p83_fait.png)", "upright labels", "italics",
    r"Le fait que a) entraîne b) résulte", r"Le fait que \emph{a)} entraîne \emph{b)} résulte",
    note="GLOBAL_ISSUES 88. Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): 'résulte trivialement de (17.3.3, (ii))' (printed p. 83)",
    "(17.3.3, (ii)) (crop p83_fait.png): composition of smooth morphisms", "'(17.3.3, (iii))'", "number",
    r"(17.3.3, (iii))", r"(17.3.3, (ii))", note="Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): '; b) entraîne c) par application' (printed p. 83)",
    "labels italic", "upright labels", "italics",
    r"; b) entraîne c) par application", r"; \emph{b)} entraîne \emph{c)} par application",
    note="Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): 'Pour voir que c) est équivalente à c')' (printed p. 83)",
    "labels italic", "upright labels", "italics",
    r"Pour voir que c) est équivalente à c'), notons", r"Pour voir que \emph{c)} est équivalente à \emph{c')}, notons",
    note="Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): '(17.2.3, (i)), Ω^1_{X/S} est un O_X-Module' (printed p. 83)",
    "italic Ω (crop p83_omxs.png)", "upright \\Omega", "font",
    r"(17.2.3, (i)), $\Omega^1_{X/S}$ est un", r"(17.2.3, (i)), $\varOmega^1_{X/S}$ est un",
    note="GLOBAL_ISSUES 92. Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): 'd'appliquer (0, 19.1.12)' (printed p. 83)", "bold 0", "plain 0", "convention",
    r"(0, 19.1.12) à l'anneau", r"(\textbf{0}, 19.1.12) à l'anneau", convention=2,
    note="Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): 'Lorsque k(x)=k(y)' (printed p. 83)", "bold italic k twice", "plain k", "convention",
    r"Lorsque $k(x)=k(y)$, l'application", r"Lorsque $\boldsymbol{k}(x)=\boldsymbol{k}(y)$, l'application", convention=1,
    note="Printed on p. 83; apply before the marker-83 move.")
add(82, "proof of (17.11.1): 'l'équivalence de c') et d).' (printed p. 83)", "labels italic", "upright labels", "italics",
    r"l'équivalence de c') et d).", r"l'équivalence de \emph{c')} et \emph{d)}.",
    note="Printed on p. 83; apply before the marker-83 move.")
add(82, "page break 82/83: printed p. 83 begins with item d) of Théorème (17.11.1)",
    "p. 82 ends 'Alors les conditions précédentes sont aussi équivalentes à la suivante :'; p. 83 begins 'd) h est lisse au "
    "point x, ...', then the paragraph 'Le fait que a) entraîne b) ...', then 'Il reste donc à prouver ...' (page_082_s4.png, page_083_s1.png)",
    "\\oldpage[IV-4]{83} stands before 'Il reste donc', item d) and the first proof paragraph too late", "marker",
    "aussi équivalentes à la suivante:" + NL + r"\begin{enumerate}",
    "aussi équivalentes à la suivante:" + NL + r"\oldpage[IV-4]{83}" + NL + r"\begin{enumerate}",
    note="Marker move, part 1 of 2: inserts the marker before the \\begin{enumerate} of item d) (before the \\begin, as for the "
         "other markers). Apply after all other p. 82 findings (the ten before it, marked 'printed p. 83', lie in text that this "
         "edit moves into the p. 83 segment); the first p. 83 finding removes the old marker. Net result: the p. 83 segment "
         "starts at item d), and 'Il reste donc' keeps its paragraph break.")

# ---------------------------------------------------------------- page 83
add(83, "old \\oldpage[IV-4]{83} before 'Il reste donc à prouver'",
    "'Il reste donc à prouver que c) entraîne a).' is a new indented paragraph in the middle of p. 83 (page_083_s2.png)",
    "the marker of p. 83 stands here", "marker",
    r"\oldpage[IV-4]{83}" + NL + NL + "Il reste donc", "Il reste donc",
    note="Marker move, part 2 of 2: removes the old marker (apply after the last p. 82 finding, which inserts the new one). "
         "The blank line before it stays: the print starts a new paragraph here.")
add(83, "proof of (17.11.1): 'Il reste donc à prouver que c) entraîne a).'", "labels italic", "upright labels", "italics",
    r"prouver que c) entraîne a). On peut", r"prouver que \emph{c)} entraîne \emph{a)}. On peut")
add(83, "proof of (17.11.1): '(Ω^1_{X/S})_x = Ω^1_{C_x/A_s}'",
    "the first Ω italic (stalk of the sheaf), the second upright (module) (crop p83_cx.png)", "upright \\Omega", "font",
    r"que $(\Omega^1_{X/S})_x=", r"que $(\varOmega^1_{X/S})_x=",
    note="GLOBAL_ISSUES 92/95: only the sheaf; the module stays upright.")
add(83, "proof of (17.11.1): 'Ω^1_{C_x/A_s} est un C_x-module libre'",
    "localisations written with the points as subscripts: C_x, A_s (crops p83_cx.png, p83_cxas.png)",
    "C_{\\mathfrak m}, A_{\\mathfrak s}: Fraktur subscripts", "formula",
    r"=\Omega^1_{C_{\mathfrak m}/A_{\mathfrak s}}$ est un $C_{\mathfrak m}$-module libre",
    r"=\Omega^1_{C_x/A_s}$ est un $C_x$-module libre",
    note="The TeX rewrote the printed subscripts x, s, y as Fraktur m, s, p throughout this sentence (four edits).")
add(83, "proof of (17.11.1): 'de B_y = O_{Y,y}'", "B_y (crop p83_by.png)", "B_{\\mathfrak p}", "formula",
    r"de $B_{\mathfrak p}=\sh{O}_{Y,y}$", r"de $B_y=\sh{O}_{Y,y}$")
add(83, "proof of (17.11.1): 'les différentielles d_{B_y/A_s}(t_i) engendrent le B_y-module Ω^1_{B_y/A_s}'",
    "subscripts y and s (crop p83_by.png)", "\\mathfrak p, \\mathfrak s", "formula",
    r"$d_{B_{\mathfrak p}/A_{\mathfrak s}}(t_i)$ engendrent le $B_{\mathfrak p}$-module $\Omega^1_{B_{\mathfrak p}/A_{\mathfrak s}}$",
    r"$d_{B_y/A_s}(t_i)$ engendrent le $B_y$-module $\Omega^1_{B_y/A_s}$")
add(83, "proof of (17.11.1): 'leurs images dans Ω^1_{C_x/A_s} fassent partie d'une base de ce C_x-module libre'",
    "subscripts x and s (crop p83_cxas.png)", "\\mathfrak m, \\mathfrak s", "formula",
    r"dans $\Omega^1_{C_{\mathfrak m}/A_{\mathfrak s}}$ fassent partie d'une base de ce $C_{\mathfrak m}$-module libre",
    r"dans $\Omega^1_{C_x/A_s}$ fassent partie d'une base de ce $C_x$-module libre")
add(83, "proof of (17.11.1): 'Comme Ω^1_{Y/S} (resp. Ω^1_{X/S}) est un O_Y-Module'",
    "italic Ω twice (crop p83_comme.png)", "upright \\Omega", "font",
    r"Comme $\Omega^1_{Y/S}$ (resp. $\Omega^1_{X/S}$) est un", r"Comme $\varOmega^1_{Y/S}$ (resp. $\varOmega^1_{X/S}$) est un",
    note="GLOBAL_ISSUES 92.")
add(83, "proof of (17.11.1): '(0, 20.5.2)'", "bold 0", "plain 0", "convention",
    r"(0, 20.5.2)", r"(\textbf{0}, 20.5.2)", convention=2)
add(83, "proof of (17.11.1): '(0, 20.4.13)'", "bold 0", "plain 0", "convention",
    r"(0, 20.4.13)", r"(\textbf{0}, 20.4.13)", convention=2)
add(83, "proof of (17.11.1): 'il résultera donc de (17.7.10) que u est étale au point y'",
    "'étale' italic (crop p83_etale.png)", "roman", "italics",
    r"que $u$ est étale au point $y$", r"que $u$ est \emph{étale} au point $y$")
add(83, "proof of (17.11.1): 'pour prouver que c) implique a)'", "labels italic (crop p83_cimpa.png)", "upright labels",
    "italics", r"prouver que c) implique a), on peut", r"prouver que \emph{c)} implique \emph{a)}, on peut")
add(83, "proof of (17.11.1): display 'g^*(Ω^1_{Y/S}) → Ω^1_{X/S}'", "italic Ω twice", "upright \\Omega", "font",
    r"g^*(\Omega^1_{Y/S})\to\Omega^1_{X/S}", r"g^*(\varOmega^1_{Y/S})\to\varOmega^1_{X/S}", note="GLOBAL_ISSUES 92.")
add(83, "proof of (17.11.1): 'est inversible à gauche (0, 19.1.12)'", "bold 0", "plain 0", "convention",
    r"(0, 19.1.12). Alors", r"(\textbf{0}, 19.1.12). Alors", convention=2)
add(83, "proof of (17.11.1): 'en tout point x∈X rationnel sur k'",
    "'rationnel sur k' italic (crop p83_end.png)", "roman", "italics",
    r"lisse en tout point $x\in X$ rationnel sur $k$, ou encore",
    r"lisse en tout point $x\in X$ \emph{rationnel sur $k$}, ou encore")
add(83, "page break 83/84 inside 'Or, y=g(x) est | a fortiori rationnel sur k'",
    "p. 83 ends 'Or, y=g(x) est', p. 84 begins 'a fortiori rationnel sur k'",
    "blank line before \\oldpage[IV-4]{84} (and another after it): a paragraph break inside the sentence", "marker",
    "Or, $y=g(x)$ est" + NL + NL, "Or, $y=g(x)$ est" + NL,
    note="GLOBAL_ISSUES 20/99. The marker is at the right place. Part 1 of 2: the first p. 84 finding removes the blank line after \\oldpage[IV-4]{84}; apply both.")

# ---------------------------------------------------------------- page 84
add(84, "top of page_084.tex: blank line after \\oldpage[IV-4]{84}",
    "p. 84 begins mid-sentence ('a fortiori rationnel sur k')", "blank line between the marker and '\\emph{a fortiori}'",
    "marker", r"\oldpage[IV-4]{84}" + NL + NL + r"\emph{a fortiori}", r"\oldpage[IV-4]{84}" + NL + r"\emph{a fortiori}",
    note="Part 2 of 2 with the p. 83 marker finding; both blank lines must go.")
add(84, "proof of (17.11.1): '(0, 20.5.14)'", "bold 0", "plain 0", "convention",
    r"(0, 20.5.14)", r"(\textbf{0}, 20.5.14)", convention=2)
add(84, "proof of (17.11.1): 'm_y/m_y^2 → (Ω^1_{Y/S})_y ⊗ k(y)'", "italic Ω", "upright \\Omega", "font",
    r"\mathfrak m_y^2\to(\Omega^1_{Y/S})_y", r"\mathfrak m_y^2\to(\varOmega^1_{Y/S})_y", note="GLOBAL_ISSUES 92.")
add(84, "proof of (17.11.1): '⊗_{O_{Y,y}} k(y) est bijectif'", "bold italic k", "plain k", "convention",
    r"}k(y)$ est bijectif; de même", r"}\boldsymbol{k}(y)$ est bijectif; de même", convention=1)
add(84, "proof of (17.11.1): 'm_x/m_x^2 → (Ω^1_{X/S})_x ⊗ k(x)'", "italic Ω", "upright \\Omega", "font",
    r"\mathfrak m_x^2\to(\Omega^1_{X/S})_x", r"\mathfrak m_x^2\to(\varOmega^1_{X/S})_x", note="GLOBAL_ISSUES 92.")
add(84, "proof of (17.11.1): '⊗_{O_{Y,x}} k(x) est bijectif. L'hypothèse'", "bold italic k", "plain k", "convention",
    r"}k(x)$ est bijectif. L'hypothèse", r"}\boldsymbol{k}(x)$ est bijectif. L'hypothèse", convention=1,
    note="Apply before the misprint edit that follows (same formula).")
add(84, "proof of (17.11.1): 'm_x/m_x^2 → (Ω^1_{X/S})_x ⊗_{O_{Y,x}} k(x) est bijectif'",
    "subscript O_{Y,x} of the tensor sign (crop p84_yx.png); O_{X,x} is meant", "\\sh{O}_{X,x}: silent correction",
    "misprint_in_print",
    r"_{X,x}}\boldsymbol{k}(x)$ est bijectif. L'hypothèse", r"_{Y,x}}\boldsymbol{k}(x)$ est bijectif. L'hypothèse",
    corrected=r"_{X,x}}\boldsymbol{k}(x)$ est bijectif. L'hypothèse",
    note="'old' is the text after the convention-1 edit just before (apply that first); the edit changes only X to Y.")
add(84, "proof of (17.11.1): 'L'hypothèse c'), équivalente à c), signifie'", "labels italic", "upright labels", "italics",
    r"L'hypothèse c'), équivalente à c), signifie", r"L'hypothèse \emph{c')}, équivalente à \emph{c)}, signifie")
add(84, "proof of (17.11.1), display: '(m_y/m_y^2) ⊗_{k(y)} k(x) → m_x/m_x^2'",
    "subscript k bold upright, k(x) bold italic (crop p84_disp.png)", "plain k twice", "convention",
    r"\otimes_{k(y)}k(x)\to\mathfrak m_x", r"\otimes_{\mathbf{k}(y)}\boldsymbol{k}(x)\to\mathfrak m_x", convention=1,
    note="Subscript k bold upright (\\mathbf, GLOBAL_ISSUES 48).")
add(84, "proof of (17.11.1): 'la conclusion résulte de (0, 17.3.3)'", "bold 0", "plain 0", "convention",
    r"(0, 17.3.3)", r"(\textbf{0}, 17.3.3)", convention=2)
add(84, "Corollaire (17.11.2): 'Sous les hypothèses générales de (17.11.1)'",
    "(17.11.1) upright inside the italic statement", "italic", "convention",
    r"générales de (17.11.1), les conditions", r"générales de \textup{(17.11.1)}, les conditions", convention=6)
add(84, "Corollaire (17.11.2), label a)", "'a)' upright", "italic label", "convention",
    r"\item[a)] $f$ est lisse au point $y$ et $g$ est étale", r"\item[\textup{a)}] $f$ est lisse au point $y$ et $g$ est étale",
    convention=6)
add(84, "Corollaire (17.11.2), label b)", "'b)' upright", "italic label", "convention",
    r"\item[b)] $h$ est lisse au point $x$ et $g$ est étale", r"\item[\textup{b)}] $h$ est lisse au point $x$ et $g$ est étale",
    convention=6)
add(84, "Corollaire (17.11.2), label c)", "'c)' upright", "italic label", "convention",
    r"\item[c)]", r"\item[\textup{c)}]", convention=6)
add(84, "Corollaire (17.11.2) c), display '(g^*(Ω^1_{X/S}))_x → (Ω^1_{X/S})_x'", "italic Ω twice", "upright \\Omega",
    "font", r"(g^*(\Omega^1_{Y/S}))_x\to(\Omega^1_{X/S})_x", r"(g^*(\varOmega^1_{Y/S}))_x\to(\varOmega^1_{X/S})_x",
    note="GLOBAL_ISSUES 92. Apply before the misprint edit that follows (same formula).")
add(84, "Corollaire (17.11.2) c), display: '(g^*(Ω^1_{X/S}))_x → (Ω^1_{X/S})_x'",
    "g^*(Ω^1_{X/S}) with X/S (crop p84_cdisp.png); Y/S is meant, as in (17.11.1.1)", "Ω^1_{Y/S}: silent correction",
    "misprint_in_print",
    r"(g^*(\varOmega^1_{Y/S}))_x", r"(g^*(\varOmega^1_{X/S}))_x", corrected=r"(g^*(\varOmega^1_{Y/S}))_x",
    note="'old' is the text after the Omega edit just before (apply that first); the edit changes only Y to X.")
add(84, "Corollaire (17.11.2), label c')", "'c')' upright", "italic label", "convention",
    r"\item[c')]", r"\item[\textup{c$'$)}]", convention=6)
add(84, "Corollaire (17.11.2) c'), display '((Ω^1_{Y/S})_y ⊗ k(y)) ⊗_{k(y)} k(x) → (Ω^1_{X/S})_x ⊗ k(x)'",
    "italic Ω twice (crop p84_cpdisp.png)", "upright \\Omega", "font",
    r"((\Omega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}k(y))\otimes_{k(y)}k(x)\to(\Omega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}k(x)",
    r"((\varOmega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}k(y))\otimes_{k(y)}k(x)\to(\varOmega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}k(x)",
    note="GLOBAL_ISSUES 92. Part 1 of 2 on this formula: apply before the convention-1 edit that follows.")
add(84, "Corollaire (17.11.2) c'), display: k(y), ⊗_{k(y)}, k(x), k(x)",
    "bold italic k three times; the subscript k bold upright (crop p84_cpdisp.png)", "plain k four times", "convention",
    r"((\varOmega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}k(y))\otimes_{k(y)}k(x)\to(\varOmega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}k(x)",
    r"((\varOmega^1_{Y/S})_y\otimes_{\sh{O}_{Y,y}}\boldsymbol{k}(y))\otimes_{\mathbf{k}(y)}\boldsymbol{k}(x)\to(\varOmega^1_{X/S})_x\otimes_{\sh{O}_{X,x}}\boldsymbol{k}(x)",
    convention=1, note="Part 2 of 2: 'old' is the text after the preceding Omega edit (apply that first).")
add(84, "Corollaire (17.11.2): 'Supposons en outre que ...' after the list",
    "a new indented paragraph (page_084_s2.png)", "text right after \\end{enumerate}: set without indent", "other",
    r"\end{enumerate}" + NL + "Supposons en outre", r"\end{enumerate}" + NL + NL + "Supposons en outre",
    note="Missing paragraph break (GLOBAL_ISSUES 80/99 pattern).")
add(84, "Corollaire (17.11.2): 'l'homomorphisme k(y) → k(x) soit bijectif'", "bold italic k twice", "plain k", "convention",
    r"l'homomorphisme $k(y)\to k(x)$ soit bijectif", r"l'homomorphisme $\boldsymbol{k}(y)\to\boldsymbol{k}(x)$ soit bijectif",
    convention=1)
add(84, "Corollaire (17.11.2) d): label d) and '(16.5.12)'", "'d)' and '(16.5.12)' upright (crop p84_d.png)", "italic",
    "convention",
    r"\item[d)] $h$ est lisse au point $x$, et l'application canonique $\mathrm{T}_{X/S}(x)\to\mathrm{T}_{Y/S}(y)$ (16.5.12) est bijective.",
    r"\item[\textup{d)}] $h$ est lisse au point $x$, et l'application canonique $\mathrm{T}_{X/S}(x)\to\mathrm{T}_{Y/S}(y)$ \textup{(16.5.12)} est bijective.",
    convention=6, note="One edit for the label and the reference.")
add(84, "proof of (17.11.2): 'Chacune des conditions a), b), c) de (17.11.2)'", "labels italic", "upright labels", "italics",
    r"Chacune des conditions a), b), c) de", r"Chacune des conditions \emph{a)}, \emph{b)}, \emph{c)} de")
add(84, "proof of (17.11.2): 'la condition c); d'où l'équivalence de a), b) et c). L'équivalence de c) et c')'",
    "labels italic", "upright labels", "italics",
    r"la condition c); d'où l'équivalence de a), b) et c). L'équivalence de c) et c') résulte",
    r"la condition \emph{c)}; d'où l'équivalence de \emph{a)}, \emph{b)} et \emph{c)}. L'équivalence de \emph{c)} et \emph{c')} résulte",
    note="Six labels in one edit.")
add(84, "proof of (17.11.2): 'l'équivalence de c') et d) lorsque'", "labels italic", "upright labels", "italics",
    r"l'équivalence de c') et d) lorsque", r"l'équivalence de \emph{c')} et \emph{d)} lorsque")
add(84, "proof of (17.11.2): 'lorsque k(x)=k(y)'", "bold italic k twice", "plain k", "convention",
    r"lorsque $k(x)=k(y)$ est immédiate", r"lorsque $\boldsymbol{k}(x)=\boldsymbol{k}(y)$ est immédiate", convention=1)
add(84, "Corollaire (17.11.3): 's_i (1≤i≤r) des sections'", "the parentheses around the formula upright (crop p84_1ir.png)",
    "italic parentheses", "convention",
    r"($1\leq i\leq r$) des sections", r"\textup{($1\leq i\leq r$)} des sections", convention=6,
    note="Parenthesised formula inside an italic statement (GLOBAL_ISSUES 26); same form as the p. 7 page fix.")
add(84, "Corollaire (17.11.3): '(qui sont aussi des sections de h_*(O_X) au-dessus de S)'",
    "upright parentheses around the italic words (crops p84_qui.png, p84_S.png; compare the italic one of '(où j' on p. 82, p82_ou.png)",
    "italic parentheses", "convention",
    r"(qui sont aussi des sections de $h_*(\sh{O}_X)$ au-dessus de $S$)",
    r"\textup{(}qui sont aussi des sections de $h_*(\sh{O}_X)$ au-dessus de $S$\textup{)}", convention=6,
    confidence="medium", note="GLOBAL_ISSUES 96; same form as the p. 68 page fix '\\textup{(}au sens de ...'.")
add(84, "Corollaire (17.11.3): 'défini par ces sections (II, 1.2.7)'", "bold II; reference upright (crop p84_cor3b.png)",
    "plain II, italic reference", "convention",
    r"défini par ces sections (II, 1.2.7)", r"défini par ces sections \textup{(\textbf{II}, 1.2.7)}", convention=2,
    note="One edit for convention 2 (bold II) and convention 6 (upright reference), as on p. 62.")
add(84, "Corollaire (17.11.3): 'Pour que g soit lisse (resp. étale) en un point x∈X'", "'(resp.' and ')' upright",
    "italic", "convention",
    r"soit lisse (resp. étale) en un point", r"soit lisse \textup{(resp.}\ étale\textup{)} en un point", convention=6)
add(84, "Corollaire (17.11.3): 'fassent partie d'une base (resp. constituent une base) du'", "'(resp.' and ')' upright",
    "italic", "convention",
    r"d'une base (resp. constituent une base) du", r"d'une base \textup{(resp.}\ constituent une base\textup{)} du",
    convention=6)
add(84, "Corollaire (17.11.3): 'du O_{X,x}-module (Ω^1_{X/S})_x'", "italic Ω (crop p84_omx.png)", "upright \\Omega",
    "font", "-module $(\\Omega^1_{X/S})_x$." + NL + r"\end{corollary}",
    "-module $(\\varOmega^1_{X/S})_x$." + NL + r"\end{corollary}", note="GLOBAL_ISSUES 92.")
add(84, "Corollaire (17.11.4): 'un S-morphisme étale U → S[T_1, ..., T_n]'",
    "T_n (crop p84_Tn.png); 'un entier r' is meant: T_r", "T_r: silent correction", "misprint_in_print",
    r"U\to S[T_1,\ldots,T_r]$.", r"U\to S[T_1,\ldots,T_n]$.", corrected=r"U\to S[T_1,\ldots,T_r]$.",
    note="The diplomatic text restores the printed T_n.")

# ---------------------------------------------------------------- verification
src0 = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


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
    raise SystemExit("page %d not found" % page)


ok = True
t = src0
for k, x in enumerate(F):
    if not x["fix"]:
        continue
    old, new = x["fix"]["old"], x["fix"]["new"]
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(old)
    if c != 1:
        ok = False
        print("SOURCE FAIL #%d p.%d count=%d old=%r" % (k, x["page"], c, old[:80]))
        continue
    t = t[:s] + seg.replace(old, new) + t[e:]
final_src = t

# page files: per page, in list order
pages = {p: (RUN / ("page_%03d.tex" % p)).read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(80, 85)}
orig_pages = dict(pages)
dependent = []
for k, x in enumerate(F):
    if not x["fix"]:
        continue
    old, new = x["fix"]["old"], x["fix"]["new"]
    p = x["page"]
    c = pages[p].count(old)
    if c != 1:
        ok = False
        print("PAGEFILE FAIL #%d p.%d count=%d old=%r" % (k, p, c, old[:80]))
        continue
    if orig_pages[p].count(old) != 1:
        dependent.append((k, p, old[:60]))
    pages[p] = pages[p].replace(old, new)

# also the current source segment of the ORIGINAL text (independent check)
for k, x in enumerate(F):
    if not x["fix"]:
        continue
    s, e = locate(src0, x["page"])
    c = src0[s:e].count(x["fix"]["old"])
    if c != 1 and all(k != d[0] for d in dependent):
        print("NOTE #%d p.%d occurs %d times in the original source segment" % (k, x["page"], c))

for x in F:
    if not x["fix"]:
        continue
    o, n = x["fix"]["old"], x["fix"]["new"]
    if o.count("{") - o.count("}") != n.count("{") - n.count("}"):
        print("BRACE BALANCE CHANGED", x["page"], o[:80])
        ok = False
    if (o.count("$") - n.count("$")) % 2:
        print("DOLLAR PARITY CHANGED", x["page"], o[:80])
        ok = False

print("dependent fixes (old taken from the text after an earlier fix):")
for d in dependent:
    print("   #%d p.%d %r" % d)
print("ALL OK" if ok else "FAILURES")
counts = {}
for x in F:
    p = x["page"]
    c = counts.setdefault(p, [0, 0, 0])
    if x["kind"] == "misprint_in_print":
        c[2] += 1
    elif x["kind"] == "convention":
        c[1] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", counts, "total", len(F))
(pathlib.Path(__file__).parent / "final_segment_80_85.tex").write_text(
    final_src[locate(final_src, 80)[0]:locate(final_src, 85)[0]], encoding="utf-8")
if ok and "--write" in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
