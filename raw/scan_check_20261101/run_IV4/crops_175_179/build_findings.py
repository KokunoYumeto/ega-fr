"""Build findings_175_179.json, check every 'old' and simulate the edits.

Run: python -I build_findings.py   (from anywhere)
'<NL>' in the strings below stands for a line break (LF).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SRC = (RUN.parent / "ega-fr" / "editions" / "2026-10-24-r20" / "diplomatic" / "packages"
       / "IV4" / "native" / "ega4" / "ega4-18-fr.tex")
OUT = RUN / "findings_175_179.json"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if corrected is not None:
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 175
add(175, "l. 2: 'qui est égal à rg_{k(p)}((Ω̂¹_{A/k})_p ⊗_{A_p} k(p))'",
    "subscript k of rg bold upright, the k of k(p) on the line bold italic (crop c175_rg.png)",
    "plain k twice", "convention", 1, "high",
    r"\operatorname{rg}_{k(\mathfrak p)}((\hat{\Omega}^1_{A/k})_{\mathfrak p}\otimes_{A_{\mathfrak p}}k(\mathfrak p))",
    r"\operatorname{rg}_{\mathbf{k}(\mathfrak p)}((\hat{\Omega}^1_{A/k})_{\mathfrak p}\otimes_{A_{\mathfrak p}}\boldsymbol{k}(\mathfrak p))",
    "One edit for both k: bold upright in the subscript, bold italic on the line (GLOBAL_ISSUES 48).")
add(175, "l. 4: 'est au plus égal à m. Il suffit'",
    "'au plus égal' italic, 'à' upright (crop c175_auplus1.png)", "upright", "italics", None, "high",
    r"est au plus égal à $m$. Il suffit", r"est \emph{au plus égal} à $m$. Il suffit")
add(175, "l. 6: 'au cas où k est algébriquement clos.'",
    "'algébriquement clos' italic (crop c175_isomorphes.png)", "upright", "italics", None, "high",
    r"au cas où $k$ est algébriquement clos. En effet", r"au cas où $k$ est \emph{algébriquement clos}. En effet")
add(175, "l. 8: 'dont les corps résiduels sont isomorphes à k''",
    "'isomorphes à k'' italic, 'à' included (crop c175_isom2.png)", "upright", "italics", None, "high",
    r"sont isomorphes à $k'$, et qui", r"sont \emph{isomorphes à $k'$}, et qui")
add(175, "l. 10: 'tel que n' = dim(A'/q'_i) ≥ dim(A/q) = n'",
    "dim(A'/q'_i): A' without the subscript i (crop c175_dimA.png)",
    "\\dim(A'_i/\\mathfrak q'_i) (silently corrected)", "misprint_in_print", None, "medium",
    r"$n'=\dim(A'_i/\mathfrak q'_i)", r"$n'=\dim(A'/\mathfrak q'_i)",
    "q'_i is a minimal prime of the factor A'_i ('dans un A'_i donné'), so the quotient meant is A'_i/q'_i, as in "
    "(Ω̂¹_{A'_i/k'})_{q'_i} two lines below. The TeX silently corrected the print; this edit restores the printed "
    "reading (same pattern as Ω¹_{A'/k'} on p. 174). Medium: read as the prime of A' = ∏A'_j over q'_i, the printed "
    "A'/q'_i has the same dimension, so the corrected edition could also keep the print.",
    corrected=r"$n'=\dim(A'_i/\mathfrak q'_i)")
add(175, "l. 12: 'est au plus égal à m; d'où notre assertion'",
    "'au plus égal à m' italic, 'à' included (crop c175_auplus2.png)", "upright", "italics", None, "high",
    r"est au plus égal à $m$; d'où notre assertion", r"est \emph{au plus égal à $m$}; d'où notre assertion")
add(175, "l. 14: '(0, 20.4.12)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.4.12)", r"(\textbf{0}, 20.4.12)")
add(175, "l. 15: 'homomorphisme surjectif (Ω̂¹_{A/k}) ⊗_A (A/q) → Ω̂¹_{(A/q)/k}'",
    "parentheses around Ω̂¹_{A/k} (crop c175_surj.png)", "no parentheses", "formula", None, "high",
    r"surjectif $\hat{\Omega}^1_{A/k}\otimes_A(A/\mathfrak q)", r"surjectif $(\hat{\Omega}^1_{A/k})\otimes_A(A/\mathfrak q)")
add(175, "l. 16: 'du K-module (Ω̂¹_{(A/q)/k}) ⊗_{A/q} K'",
    "parentheses around Ω̂¹_{(A/q)/k} (crop c175_surj.png)", "no parentheses", "formula", None, "high",
    r"$K$-module $\hat{\Omega}^1_{(A/\mathfrak q)/k}\otimes_{A/\mathfrak q}K$",
    r"$K$-module $(\hat{\Omega}^1_{(A/\mathfrak q)/k})\otimes_{A/\mathfrak q}K$")
add(175, "Lemme (18.11.5.2): 'éléments inversibles u_i (1≤i≤m) de A'",
    "parentheses upright inside the italic statement (crop c175_lemparen.png)",
    "text parentheses, italic in the lemma environment", "convention", 6, "high",
    r"$u_i$ ($1\leq i\leq m$) de $A$", r"$u_i$ \textup{(}$1\leq i\leq m$\textup{)} de $A$",
    "Parentheses around a formula; the edition's form \\textup{(}...\\textup{)}.")
add(175, "proof of (18.11.5.2), l. 2: '(Ω̂¹_{A/k})_p ⊗_{A_p} k(p) = Ω̂¹_{A/k} ⊗_A k(p)'",
    "bold italic k twice", "plain k", "convention", 1, "high",
    r"\otimes_{A_{\mathfrak p}}k(\mathfrak p)=\hat{\Omega}^1_{A/k}\otimes_A k(\mathfrak p)$",
    r"\otimes_{A_{\mathfrak p}}\boldsymbol{k}(\mathfrak p)=\hat{\Omega}^1_{A/k}\otimes_A\boldsymbol{k}(\mathfrak p)$",
    "Two occurrences in one edit.")
add(175, "proof of (18.11.5.2): 'comme ce k(p)-espace vectoriel'", "bold italic k", "plain k", "convention", 1, "high",
    r"comme ce $k(\mathfrak p)$-espace", r"comme ce $\boldsymbol{k}(\mathfrak p)$-espace")
add(175, "proof of (18.11.5.2): 'linéairement indépendants sur k(p)'", "bold italic k", "plain k", "convention", 1, "high",
    r"indépendants sur $k(\mathfrak p)$", r"indépendants sur $\boldsymbol{k}(\mathfrak p)$")
add(175, "proof of (18.11.5.2): 'l'image canonique de x_{r+1} dans k(p)'", "bold italic k", "plain k", "convention", 1, "high",
    r"dans $k(\mathfrak p)$ est $\neq0$", r"dans $\boldsymbol{k}(\mathfrak p)$ est $\neq0$")
add(175, "end of p. 175 / \\oldpage[IV-4]{176}",
    "p. 175 ends 'Or, il résulte de (0, 20.7.15) et de (0_I, 7.2.9) que les δ(x) engendrent le k(p)-espace vectoriel "
    "(Ω̂¹_{A/k})_p ⊗_{A_p} k(p);', in the same paragraph as '... pour 1≤i≤r.'; p. 176 begins 'comme par hypothèse r<m' "
    "(crop c175_or.png, page_176_s1.png)",
    "\\oldpage[IV-4]{176} stands before 'Or, il résulte', one sentence too early, with blank lines before and after it "
    "(a paragraph break the print lacks)", "marker", None, "high",
    r"tel que $\delta(u)$ ne soit pas combinaison linéaire des $\delta(u_ix_i)$ pour $1\leq i\leq r$.<NL><NL>",
    r"tel que $\delta(u)$ ne soit pas combinaison linéaire des $\delta(u_ix_i)$ pour $1\leq i\leq r$.<NL>",
    "Part 1 of 3 (apply all three together): this removes the blank line at the end of the p. 175 segment; the first two "
    "p. 176 findings delete the marker and its blank line before 'Or, il résulte' and re-insert \\oldpage[IV-4]{176} "
    "before 'comme par hypothèse'. Afterwards the sentence 'Or, il résulte ... k(p);' ends the p. 175 segment.")

# ---------------------------------------------------------------- p. 176
add(176, "start of page_176.tex: \\oldpage[IV-4]{176} before 'Or, il résulte'",
    "printed p. 176 begins 'comme par hypothèse r<m' (page_176_s1.png); 'Or, il résulte ... k(p);' is the last line of p. 175",
    "marker and a blank line before 'Or, il résulte'", "marker", None, "high",
    r"\oldpage[IV-4]{176}<NL><NL>Or, il", r"Or, il",
    "Part 2 of 3 with the last p. 175 finding and the next one; apply all three together.")
add(176, "first line of printed p. 176: '...k(p); | comme par hypothèse r<m'",
    "page break after 'k(p);', mid-sentence (page_175_s4.png, page_176_s1.png)", "no marker here", "marker", None, "high",
    r"$; comme par hypothèse $r<m$", r"$;<NL>\oldpage[IV-4]{176}<NL>comme par hypothèse $r<m$",
    "Part 3 of 3: re-inserts the marker at the printed page break, without blank lines (mid-sentence). The 'old' begins "
    "with the closing $ of the formula changed by the formula finding below; the two edits do not overlap.")
add(176, "printed p. 175, last line but one (TeX: p. 176 segment): '(0, 20.7.15)'", "bold 0", "plain 0",
    "convention", 2, "high", r"(0, 20.7.15)", r"(\textbf{0}, 20.7.15)",
    "Printed on p. 175; the text moves to the p. 175 segment with the marker findings.")
add(176, "printed p. 175, last line (TeX: p. 176 segment): '(0_I, 7.2.9)'", "bold 0 with subscript I", "plain 0",
    "convention", 2, "high", r"($0_{\mathrm I}$, 7.2.9)", r"($\mathbf{0}_{\mathrm I}$, 7.2.9)",
    "Printed on p. 175.")
add(176, "printed p. 175, last line (TeX: p. 176 segment): 'engendrent le k(p)-espace vectoriel'", "bold italic k",
    "plain k", "convention", 1, "high",
    r"engendrent le $k(\mathfrak p)$-espace", r"engendrent le $\boldsymbol{k}(\mathfrak p)$-espace", "Printed on p. 175.")
add(176, "printed p. 175, last line (TeX: p. 176 segment): 'le k(p)-espace vectoriel (Ω̂¹_{A/k})_p ⊗_{A_p} k(p);'",
    "(Ω̂¹_{A/k})_p ⊗_{A_p} k(p) (crop c175_or2.png)", "Ω̂¹_{A/k} ⊗_A k(p) (rewritten)", "formula", None, "high",
    r"vectoriel $\hat{\Omega}^1_{A/k}\otimes_A k(\mathfrak p)",
    r"vectoriel $(\hat{\Omega}^1_{A/k})_{\mathfrak p}\otimes_{A_{\mathfrak p}}\boldsymbol{k}(\mathfrak p)",
    "Printed on p. 175. The edit also writes this k(p) bold italic (convention 1).")
add(176, "l. 5: 'la démonstration de l'implication a) ⇒ b) dans (18.11.5)'",
    "labels a), b) wholly italic (crop c176_aimpb.png)", "$a)\\Rightarrow b)$: italic letters, upright parentheses",
    "italics", None, "high",
    r"l'implication $a)\Rightarrow b)$ dans", r"l'implication \emph{a)} $\Rightarrow$ \emph{b)} dans",
    "GLOBAL_ISSUES 88.")
add(176, "l. 11: 'L'hypothèse a) et la relation dim(A/q)=n'", "label a) wholly italic", "$a)$", "italics", None, "high",
    r"L'hypothèse $a)$ et la relation", r"L'hypothèse \emph{a)} et la relation", "GLOBAL_ISSUES 88.")
add(176, "l. 16-17: '... forment un système de paramètres. | Considérons alors le k-homomorphisme local'",
    "'Considérons' starts flush left, no paragraph indent: same paragraph (crop c176_consid.png)",
    "blank line before 'Considérons alors' (new paragraph)", "other", None, "high",
    r"forment un système de paramètres.<NL><NL>Considérons alors",
    r"forment un système de paramètres.<NL>Considérons alors")
add(176, "l. 19: '(0_I, 7.4.4 et 7.4.3)'", "bold 0 with subscript I", "plain 0", "convention", 2, "high",
    r"($0_{\mathrm I}$, 7.4.4 et 7.4.3)", r"($\mathbf{0}_{\mathrm I}$, 7.4.4 et 7.4.3)")
add(176, "l. 19: 'que u fait de A une B-algèbre finie.'", "'finie' italic", "upright", "italics", None, "high",
    r"une $B$-algèbre finie. On a donc", r"une $B$-algèbre \emph{finie}. On a donc")
add(176, "display after 'la suite exacte'",
    "(Ω̂¹_{B/k}) ⊗_B A →^v Ω̂¹_{A/k} →^w Ω¹_{A/B} → 0, no full stop (crop c176_disp.png)",
    "no parentheses around Ω̂¹_{B/k}, second arrow unlabelled, final full stop", "formula", None, "high",
    r"\hat{\Omega}^1_{B/k}\otimes_B A\xrightarrow{v}\hat{\Omega}^1_{A/k}\longrightarrow\Omega^1_{A/B}\longrightarrow0.",
    r"(\hat{\Omega}^1_{B/k})\otimes_B A\xrightarrow{v}\hat{\Omega}^1_{A/k}\xrightarrow{w}\Omega^1_{A/B}\longrightarrow0",
    "Three differences in one display: the parentheses, the label w over the second arrow, and the full stop the print lacks.")
add(176, "after the display: '(0, 20.5.2.6)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.5.2.6)", r"(\textbf{0}, 20.5.2.6)")
add(176, "after the display: 'on voit donc que v_p : (Ω̂¹_{B/k}) ⊗_B A_p → (Ω̂¹_{A/k})_p'",
    "(Ω̂¹_{B/k}) ⊗_B A_p: parentheses around Ω̂¹_{B/k} only, subscript p on A (crop c176_vp.png)",
    "(Ω̂¹_{B/k} ⊗_B A)_p", "formula", None, "high",
    r"$v_{\mathfrak p}:(\hat{\Omega}^1_{B/k}\otimes_B A)_{\mathfrak p}\to",
    r"$v_{\mathfrak p}:(\hat{\Omega}^1_{B/k})\otimes_B A_{\mathfrak p}\to")
add(176, "'est surjectif, et par suite on a 0=(Ω¹_{A/B})_p'", "'surjectif' italic (crop c176_surj.png)", "upright",
    "italics", None, "high",
    r"est surjectif, et par suite on a $0=", r"est \emph{surjectif}, et par suite on a $0=")
add(176, "'(où r est l'image réciproque de p dans A, cf. (16.4.15))'",
    "'dans A' (crop c176_surj.png)", "'dans $A$' (keeps the print)", "misprint_in_print", None, "medium",
    None, None,
    "r is the inverse image of p under u: B → A, a prime of B (p. 177: 'posons r = u^{-1}(p)'; Ω¹_{A_p/B_r}), so 'dans B' "
    "is meant. The diplomatic TeX keeps the printed reading. Not in the errata list of IV-4 (checked by search).",
    corrected=r"l'image réciproque de $\mathfrak p$ dans $B$")
add(176, "'cela entraîne la propriété b) de (18.11.5)'", "label b) wholly italic", "$b)$", "italics", None, "high",
    r"la propriété $b)$ de (18.11.5). C.Q.F.D.", r"la propriété \emph{b)} de (18.11.5). C.Q.F.D.", "GLOBAL_ISSUES 88.")

# ---------------------------------------------------------------- p. 177
add(177, "Corollaire (18.11.8), l. 2: 'complète intègre, dont le corps'",
    "'intègre' roman (upright) inside the italic statement (crop c177_integre.png)", "italic (environment)",
    "convention", 6, "high",
    r"complète intègre, dont le corps", r"complète \textup{intègre}, dont le corps",
    "The heavier 'complète' at the end of the line above is italic (heavy impression, not reported).")
add(177, "Corollaire (18.11.8): 'on a rg_K((Ω̂¹_{A/k}) ⊗_A K) ≥ dim(A).'",
    "set in the line (starts at the left margin of the statement's last line; crop c177_integre.png)",
    "displayed, with \\bigl( \\bigr)", "formula", None, "high",
    r"\[<NL>  \operatorname{rg}_K\bigl((\hat{\Omega}^1_{A/k})\otimes_A K\bigr)\geq\dim(A).<NL>\]",
    r"$\operatorname{rg}_K((\hat{\Omega}^1_{A/k})\otimes_A K)\geq\dim(A)$.",
    "Inline as printed (GLOBAL_ISSUES 21 pattern).")
add(177, "Corollaire (18.11.9), label (i)", "label (i) upright", "\\item[(i)] italic in the corollary environment",
    "convention", 6, "high",
    r"\item[(i)] Le $A_{\mathfrak p}$-module", r"\item[\textup{(i)}] Le $A_{\mathfrak p}$-module", "GLOBAL_ISSUES 16.")
add(177, "Corollaire (18.11.9), label (ii)", "label (ii) upright", "\\item[(ii)] italic in the corollary environment",
    "convention", 6, "high",
    r"\item[(ii)] Il existe un $k$-homomorphisme local", r"\item[\textup{(ii)}] Il existe un $k$-homomorphisme local",
    "GLOBAL_ISSUES 16.")
add(177, "Corollaire (18.11.9), label (iii)", "label (iii) upright", "\\item[(iii)] italic in the corollary environment",
    "convention", 6, "high",
    r"\item[(iii)] La $k$-algèbre", r"\item[\textup{(iii)}] La $k$-algèbre", "GLOBAL_ISSUES 16.")
add(177, "proof of (18.11.9): 'il existe un homomorphisme local u : B=k[[T_1, ..., T_n]] → A faisant de A'",
    "set in the line (beginning of the second line of the paragraph, page_177_s2.png)", "displayed", "formula", None,
    "high",
    r"\[<NL>  u:B=k[[T_1,\ldots,T_n]]\longrightarrow A<NL>\]",
    r"$u:B=k[[T_1,\ldots,T_n]]\to A$", "Inline as printed.")
add(177, "proof of (18.11.9): 'faisant de A une B-algèbre finie, et tel que'", "'finie' italic", "upright",
    "italics", None, "high",
    r"une $B$-algèbre finie, et tel que le morphisme correspondant $\Spec(A)\to\Spec(B)$ soit non ramifié au point $\mathfrak p$; posons",
    r"une $B$-algèbre \emph{finie}, et tel que le morphisme correspondant $\Spec(A)\to\Spec(B)$ soit non ramifié au point $\mathfrak p$; posons")
add(177, "'quotient d'anneau régulier (0, 19.8.8)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 19.8.8)", r"(\textbf{0}, 19.8.8)")
add(177, "'dim(A_p) = n—dim(A/p)'", "long dash (crop c177_dash.png)", "minus sign", "convention", 7, "high",
    r"=n-\dim(A/\mathfrak p)$", r"=n\setmin\dim(A/\mathfrak p)$", "GLOBAL_ISSUES 23 (long dash used for subtraction).")
add(177, "'(0, 16.5.12)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.5.12)", r"(\textbf{0}, 16.5.12)")
add(177, "'dim(B_r) = n—dim(B/r)'", "long dash (crop c177_dash.png)", "minus sign", "convention", 7, "high",
    r"=n-\dim(B/\mathfrak r)$", r"=n\setmin\dim(B/\mathfrak r)$", "GLOBAL_ISSUES 23.")
add(177, "'donc (0, 16.3.9) on a'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.3.9)", r"(\textbf{0}, 16.3.9)")
add(177, "'(0, 19.3.4 et 19.3.5)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 19.3.4 et 19.3.5)", r"(\textbf{0}, 19.3.4 et 19.3.5)")
add(177, "'géométriquement régulier sur k (0, 22.5.8)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 22.5.8)", r"(\textbf{0}, 22.5.8)")
add(177, "last line: 'est un A_p-module libre de type fini (2.5.2);'",
    "'libre' italic (crop c177_libre.png)", "upright", "italics", None, "high",
    r"on voit que $(\hat{\Omega}^1_{A/k})_{\mathfrak p}$ est un $A_{\mathfrak p}$-module libre de type fini",
    r"on voit que $(\hat{\Omega}^1_{A/k})_{\mathfrak p}$ est un $A_{\mathfrak p}$-module \emph{libre} de type fini")
add(177, "page break 177/178 inside '... de type fini (2.5.2); | d'ailleurs, en vertu de (18.11.5.1)'",
    "p. 178 begins mid-sentence with 'd'ailleurs' at the left margin (page_178_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{178}", "marker", None, "high",
    r" (2.5.2);<NL><NL>", r" (2.5.2);<NL>",
    "The marker is at the right place. Part 1 of 2: the first p. 178 finding removes the blank line after "
    "\\oldpage[IV-4]{178}; apply both.")

# ---------------------------------------------------------------- p. 178
add(178, "top of p. 178: page break 177/178", "mid-sentence continuation 'd'ailleurs, en vertu ...'",
    "blank line after \\oldpage[IV-4]{178}", "marker", None, "high",
    r"\oldpage[IV-4]{178}<NL><NL>d'ailleurs", r"\oldpage[IV-4]{178}<NL>d'ailleurs",
    "Part 2 of 2 with the last p. 177 finding; both blank lines must go.")
add(178, "l. 2: 'est un A_p-module libre de rang n. C.Q.F.D.'",
    "'de rang n' italic, 'libre' upright (crop c178_derang.png)", "upright", "italics", None, "high",
    r"module libre de rang $n$. C.Q.F.D.", r"module libre \emph{de rang $n$}. C.Q.F.D.")
add(178, "Théorème (18.11.10), label a)", "label a) upright (crop c178_label_a.png)", "\\item[$a)$]: italic a",
    "convention", 6, "high",
    r"\item[$a)$] Pour toute extension", r"\item[\textup{a)}] Pour toute extension", "GLOBAL_ISSUES 88.")
add(178, "Théorème (18.11.10), label a')", "label a') upright", "\\item[$a')$]: italic a", "convention", 6, "high",
    r"\item[$a')$] Il existe une", r"\item[\textup{a$'$)}] Il existe une", "GLOBAL_ISSUES 88.")
add(178, "Théorème (18.11.10) a'): 'Il existe une extension parfaite k''",
    "'parfaite' roman (upright) inside the italic statement (crop c178_parfaite.png)", "italic (environment)",
    "convention", 6, "high",
    r"extension parfaite $k'$", r"extension \textup{parfaite} $k'$")
add(178, "Théorème (18.11.10), label b)", "label b) upright", "\\item[$b)$]: italic b", "convention", 6, "high",
    r"\item[$b)$] Soit $n$ la plus grande", r"\item[\textup{b)}] Soit $n$ la plus grande", "GLOBAL_ISSUES 88.")
add(178, "Théorème (18.11.10): 'Supposons en outre que n=dim(A)' after the list",
    "indented new paragraph (page_178_s2.png)", "text right after \\end{enumerate}: no indent", "other", None, "high",
    r"\end{enumerate}<NL>Supposons en outre", r"\end{enumerate}<NL><NL>Supposons en outre",
    "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern).")
add(178, "Théorème (18.11.10): '(ce qui sera le cas si A est équidimensionnel)'",
    "parenthetical roman with upright parentheses, only 'équidimensionnel' italic (crop c178_cequi.png)",
    "all italic (environment)", "convention", 6, "high",
    r"(ce qui sera le cas si $A$ est équidimensionnel)",
    r"\textup{(ce qui sera le cas si $A$ est \emph{équidimensionnel})}",
    "Same form as the page fix of Proposition (18.11.5) on p. 174.")
add(178, "Théorème (18.11.10), label c)", "label c) upright", "\\item[$c)$]: italic c", "convention", 6, "high",
    r"\item[$c)$] Il existe un $k$-homomorphisme", r"\item[\textup{c)}] Il existe un $k$-homomorphisme",
    "GLOBAL_ISSUES 88.")
add(178, "Théorème (18.11.10): 'Chacune des conditions ...' after the list",
    "indented new paragraph (crop c178_chacune.png)", "text right after \\end{enumerate}: no indent", "other", None,
    "high",
    r"\end{enumerate}<NL>Chacune", r"\end{enumerate}<NL><NL>Chacune",
    "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern).")
add(178, "Théorème (18.11.10): 'Chacune des conditions a), a'), b) entraîne la suivante'",
    "labels and the commas between them upright inside the italic statement (crop c178_chacune.png)",
    "$a)$, $a')$, $b)$: italic letters", "convention", 6, "high",
    r"des conditions $a)$, $a')$, $b)$ entraîne la suivante", r"des conditions \textup{a), a$'$), b)} entraîne la suivante",
    "GLOBAL_ISSUES 88.")
add(178, "Théorème (18.11.10), label d)", "label d) upright (crop c178_chacune.png)", "\\item[$d)$]: italic d",
    "convention", 6, "high",
    r"\item[$d)$] L'anneau", r"\item[\textup{d)}] L'anneau", "GLOBAL_ISSUES 88.")
add(178, "Théorème (18.11.10): 'Si de plus [k:k^p]<+∞, ...' after the list",
    "indented new paragraph (crop c178_chacune.png)", "text right after \\end{enumerate}: no indent", "other", None,
    "high",
    r"\end{enumerate}<NL>Si de plus", r"\end{enumerate}<NL><NL>Si de plus",
    "Paragraph after the list, indented as printed (GLOBAL_ISSUES 80 pattern).")
add(178, "Théorème (18.11.10): 'la condition d) est équivalente à a), a') et b).'",
    "labels upright, 'et' italic (page_178_s2.png)", "$d)$, $a)$, $a')$, $b)$: italic letters", "convention", 6, "high",
    r"la condition $d)$ est équivalente à $a)$, $a')$ et $b)$.",
    r"la condition \textup{d)} est équivalente à \textup{a), a$'$)} et \textup{b)}.", "GLOBAL_ISSUES 88.")
add(178, "proof: 'Le fait que d) entraîne b) lorsque [k:k^p]<+∞'", "labels wholly italic", "$d)$, $b)$",
    "italics", None, "high",
    r"Le fait que $d)$ entraîne $b)$ lorsque", r"Le fait que \emph{d)} entraîne \emph{b)} lorsque", "GLOBAL_ISSUES 88.")
add(178, "proof: 'Il est clair que a) entraîne trivialement a'); montrons que c) entraîne a)'",
    "labels wholly italic", "$a)$, $a')$, $c)$, $a)$", "italics", None, "high",
    r"Il est clair que $a)$ entraîne trivialement $a')$; montrons que $c)$ entraîne $a)$ lorsque",
    r"Il est clair que \emph{a)} entraîne trivialement \emph{a$'$)}; montrons que \emph{c)} entraîne \emph{a)} lorsque",
    "GLOBAL_ISSUES 88.")
add(178, "proof: 'Avec les notations de a), on a alors'", "label wholly italic", "$a)$", "italics", None, "high",
    r"Avec les notations de $a)$, on a alors", r"Avec les notations de \emph{a)}, on a alors", "GLOBAL_ISSUES 88.")
add(178, "proof: 'on a alors A'=A⊗_B B', où B'=B⊗̂_k k'=k'[[T_1, ..., T_n]] (7.5.7.1)'",
    "two formulas set in the line, joined by 'où' (page_178_s2.png)",
    "one display joining them with \\qquad; 'où' missing", "missing", None, "high",
    r"\[<NL>  A'=A\otimes_B B',\qquad B'=B\widehat{\otimes}_k k'=k'[[T_1,\ldots,T_n]]<NL>\]",
    r"$A'=A\otimes_B B'$, où $B'=B\widehat{\otimes}_k k'=k'[[T_1,\ldots,T_n]]$",
    "Inline as printed, with the lost connecting word (GLOBAL_ISSUES 51 pattern).")
add(178, "proof: 'Le fait que b) entraîne c) lorsque dim(A)=n'", "labels wholly italic (crop c178_lorsque.png)",
    "$b)$, $c)$", "italics", None, "high",
    r"Le fait que $b)$ entraîne $c)$ lorsque", r"Le fait que \emph{b)} entraîne \emph{c)} lorsque", "GLOBAL_ISSUES 88.")
add(178, "proof: 'Montrons que a') entraîne b) lorsque dim(A)=n.'",
    "labels wholly italic, and 'lorsque' after b) italic too (crop c178_lorsque.png)", "$a')$, $b)$, 'lorsque' upright",
    "italics", None, "high",
    r"Montrons que $a')$ entraîne $b)$ lorsque $\dim(A)=n$.",
    r"Montrons que \emph{a$'$)} entraîne \emph{b) lorsque} $\dim(A)=n$.",
    "The print sets this 'lorsque' italic, unlike the 'lorsque' of the sentence before; possibly italic carried on from "
    "the label, but reproduced as printed.")
add(178, "proof: 'il résulte de (18.11.4) que (Ω̂¹_{A'/k'})_{p'} = (Ω̂¹_{A/k})_p ⊗_{A_p} A'_{p'}; comme k' est'",
    "formula set in the line (crop c178_geom.png)", "displayed", "formula", None, "high",
    r"\[<NL>  (\hat{\Omega}^1_{A'/k'})_{\mathfrak p'}=(\hat{\Omega}^1_{A/k})_{\mathfrak p}\otimes_{A_{\mathfrak p}}A'_{\mathfrak p'};<NL>\]",
    r"$(\hat{\Omega}^1_{A'/k'})_{\mathfrak p'}=(\hat{\Omega}^1_{A/k})_{\mathfrak p}\otimes_{A_{\mathfrak p}}A'_{\mathfrak p'}$;",
    "Inline as printed.")
add(178, "proof: 'qu'il est géométriquement régulier sur k' (6.7.7)'", "'géométriquement régulier' italic (crop c178_geom.png)",
    "upright", "italics", None, "high",
    r"qu'il est géométriquement régulier sur $k'$", r"qu'il est \emph{géométriquement régulier} sur $k'$")
add(178, "proof: 'le fait que d) entraîne b), donc'", "labels wholly italic", "$d)$, $b)$", "italics", None, "high",
    r"le fait que $d)$ entraîne $b)$, donc", r"le fait que \emph{d)} entraîne \emph{b)}, donc", "GLOBAL_ISSUES 88.")
add(178, "proof: 'Ceci montre l'équivalence de a), a'), b) et c)'", "labels wholly italic", "$a)$, $a')$, $b)$, $c)$",
    "italics", None, "high",
    r"l'équivalence de $a)$, $a')$, $b)$ et $c)$ lorsque",
    r"l'équivalence de \emph{a)}, \emph{a$'$)}, \emph{b)} et \emph{c)} lorsque", "GLOBAL_ISSUES 88.")
add(178, "proof: 'Il reste à prouver que a), a') et b) sont encore équivalentes'", "labels wholly italic",
    "$a)$, $a')$, $b)$", "italics", None, "high",
    r"à prouver que $a)$, $a')$ et $b)$ sont encore", r"à prouver que \emph{a)}, \emph{a$'$)} et \emph{b)} sont encore",
    "GLOBAL_ISSUES 88.")
add(178, "proof: 'l'homomorphisme canonique A_p→(A_1)_{p_1} est bijectif;'", "'bijectif' italic (crop c178_bij.png)",
    "upright", "italics", None, "high",
    r"est bijectif; on en conclut", r"est \emph{bijectif}; on en conclut")
add(178, "proof: 'on en conclut (I, 6.5.4)'", "bold I: a reference to EGA I (crop c178_bij.png)", "plain I",
    "convention", 2, "high",
    r"(I, 6.5.4)", r"(\textbf{I}, 6.5.4)", "Real EGA I reference (bold I in the print), not EGA IV (1.6.5.4).")
add(178, "proof: 'est un isomorphisme local au point p_1, et l'on a J_p=0'",
    "'isomorphisme local' italic (crop c178_bij.png)", "upright", "italics", None, "high",
    r"est un isomorphisme local au point $\mathfrak p_1$, et l'on a",
    r"est un \emph{isomorphisme local} au point $\mathfrak p_1$, et l'on a")
add(178, "last display: 'J/J² → (Ω̂¹_{A/k}) ⊗_A A_1 → Ω̂¹_{A_1/k} → 0'",
    "parentheses around Ω̂¹_{A/k} (crop c178_disp.png)", "no parentheses", "formula", None, "high",
    r"\longrightarrow\hat{\Omega}^1_{A/k}\otimes_A A_1\longrightarrow",
    r"\longrightarrow(\hat{\Omega}^1_{A/k})\otimes_A A_1\longrightarrow")
add(178, "end of p. 178: the last display and the page break 178/179 ('→ 0 | et en localisant en p')",
    "no full stop after the display (crop c178_disp.png); p. 179 continues the sentence with a lower-case "
    "'et en localisant' at the left margin (page_179_s1.png)",
    "full stop after the display; blank lines before and after \\oldpage[IV-4]{179}", "marker", None, "high",
    r"\hat{\Omega}^1_{A_1/k}\longrightarrow0.<NL>\]<NL><NL>",
    r"\hat{\Omega}^1_{A_1/k}\longrightarrow0<NL>\]<NL>",
    "One edit for the full stop the print lacks (the sentence goes on) and the blank line before the marker. "
    "Part 1 of 2: the first p. 179 finding removes the blank line after \\oldpage[IV-4]{179}; apply both.")

# ---------------------------------------------------------------- p. 179
add(179, "top of p. 179: page break 178/179", "mid-sentence continuation 'et en localisant en p'",
    "blank line after \\oldpage[IV-4]{179}", "marker", None, "high",
    r"\oldpage[IV-4]{179}<NL><NL>", r"\oldpage[IV-4]{179}<NL>",
    "Part 2 of 2 with the last p. 178 finding; both blank lines must go.")
add(179, "l. 1: 'et en localisant en p'", "lower-case 'et' (crop c179_top.png)", "'Et'", "word", None, "high",
    r"Et en localisant en", r"et en localisant en",
    "The sentence continues from the display at the end of p. 178.")
add(179, "l. 1: 'il vient un isomorphisme (Ω̂¹_{A/k})_p ⥲ (Ω̂¹_{A_1/k})_{p_1}. Ceci montre'",
    "formula set in the line (crop c179_top.png)", "displayed", "formula", None, "high",
    r"\[<NL>  (\hat{\Omega}^1_{A/k})_{\mathfrak p}\xrightarrow{\sim}(\hat{\Omega}^1_{A_1/k})_{\mathfrak p_1}.<NL>\]",
    r"$(\hat{\Omega}^1_{A/k})_{\mathfrak p}\xrightarrow{\sim}(\hat{\Omega}^1_{A_1/k})_{\mathfrak p_1}$.",
    "Inline as printed.")
add(179, "l. 1-2: 'la condition b) pour l'anneau A et l'idéal p est équivalente à la condition b)'",
    "labels and 'équivalente' italic", "upright 'équivalente'; $b)$", "italics", None, "high",
    r"Ceci montre que la condition $b)$ pour l'anneau $A$ et l'idéal $\mathfrak p$ est équivalente à la condition $b)$ pour",
    r"Ceci montre que la condition \emph{b)} pour l'anneau $A$ et l'idéal $\mathfrak p$ est \emph{équivalente} à la condition \emph{b)} pour")
add(179, "l. 3: 'avec les notations de a), on a A'_1'", "label wholly italic", "$a)$", "italics", None, "high",
    r"avec les notations de $a)$, on a $A'_1", r"avec les notations de \emph{a)}, on a $A'_1")
add(179, "l. 6: 'annule un élément de A'—p''", "long dash for the set difference (crop c179_dash.png)", "minus sign",
    "convention", 7, "high",
    r"$A'-\mathfrak p'$", r"$A'\setmin\mathfrak p'$")
add(179, "l. 7-8: 'ceci montre donc que la condition a) (resp. a')) pour l'anneau A'", "labels wholly italic",
    "$a)$, $a')$", "italics", None, "high",
    r"ceci montre donc que la condition $a)$ (resp. $a')$) pour",
    r"ceci montre donc que la condition \emph{a)} (resp. \emph{a$'$)}) pour")
add(179, "l. 8: 'est équivalente à la condition a) (resp. a')) pour l'anneau A_1'",
    "'équivalente' and the labels italic", "upright 'équivalente'; $a)$, $a')$", "italics", None, "high",
    r"est équivalente à la condition $a)$ (resp. $a')$) pour l'anneau $A_1$",
    r"est \emph{équivalente} à la condition \emph{a)} (resp. \emph{a$'$)}) pour l'anneau $A_1$")
add(179, "Remarques (18.11.11) (i): 'L'équivalence des conditions d) et b) dans (18.11.10)'", "labels wholly italic",
    "$d)$, $b)$", "italics", None, "high",
    r"des conditions $d)$ et $b)$ dans (18.11.10)", r"des conditions \emph{d)} et \emph{b)} dans (18.11.10)",
    "Remark body judged as roman (document-wide remark font item).")
add(179, "Remarques (18.11.11) (i): '(0, 22.7.7, (ii))'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 22.7.7, (ii))", r"(\textbf{0}, 22.7.7, (ii))")
add(179, "Remarques (18.11.11) (i): 'et on sait que j n'est pas injectif'", "'j n'est pas injectif' italic",
    "upright words", "italics", None, "high",
    r"on sait que $j$ n'est pas injectif", r"on sait que \emph{$j$ n'est pas injectif}")
add(179, "Remarques (18.11.11) (i): 'la condition d) n'entraîne pas b).'", "labels wholly italic", "$d)$, $b)$",
    "italics", None, "high",
    r"la condition $d)$ n'entraîne pas $b)$.", r"la condition \emph{d)} n'entraîne pas \emph{b)}.")
add(179, "Remarques (18.11.11) (ii): 'soit étale au point p, il faut et il suffit'", "'étale' italic", "upright",
    "italics", None, "high",
    r"soit étale au point $\mathfrak p$, il faut et il suffit", r"soit \emph{étale} au point $\mathfrak p$, il faut et il suffit")
add(179, "Remarques (18.11.11) (ii): 'forment un système de générateurs de cet A_p-module'",
    "'système de générateurs' italic", "upright", "italics", None, "high",
    r"forment un système de générateurs de cet", r"forment un \emph{système de générateurs} de cet")
add(179, "Remarques (18.11.11) (ii): 'qui engendrent (Ω̂¹_{B/k}) ⊗_B A, sont les d_A x_i'",
    "(Ω̂¹_{B/k}) ⊗_B A, no subscript p (crop c179_engendrent.png)", "(Ω̂¹_{B/k} ⊗_B A)_p", "formula", None, "high",
    r"qui engendrent $(\hat{\Omega}^1_{B/k}\otimes_B A)_{\mathfrak p}$", r"qui engendrent $(\hat{\Omega}^1_{B/k})\otimes_B A$",
    "The print's '(Ω̂¹_{B/k}⊗_B A)_p → (Ω̂¹_{A/k})_p' in the line above is as in the TeX.")
add(179, "Remarques (18.11.11) (ii): 'd'où la nécessité de la condition'", "'nécessité' italic (crop c179_engendrent.png)",
    "upright", "italics", None, "high",
    r"d'où la nécessité de la condition", r"d'où la \emph{nécessité} de la condition")
add(179, "Remarques (18.11.11) (ii), end: 'que ce morphisme est étale en p.'", "'étale' italic", "upright", "italics",
    None, "high",
    r"que ce morphisme est étale en $\mathfrak p$.", r"que ce morphisme est \emph{étale} en $\mathfrak p$.")
add(179, "Corollaire (18.11.12): 'les conditions équivalentes a), a'), b), c) et d) de (18.11.10).'",
    "labels, their commas and the reference upright; 'et', 'de' italic (crop c179_conds.png)",
    "$a)$ ... $d)$ italic letters; (18.11.10) italic (environment)", "convention", 6, "high",
    r"équivalentes $a)$, $a')$, $b)$, $c)$ et $d)$ de (18.11.10).",
    r"équivalentes \textup{a), a$'$), b), c)} et \textup{d)} de \textup{(18.11.10)}.",
    "GLOBAL_ISSUES 88; reference upright as in the page fix 'de \\textup{(18.5.4)}' (p. 128).")
add(179, "end of p. 179: page break 179/180 inside Corollaire (18.11.12) ('si n=dim(A)=dim(A'), | il existe un "
         "k'-homomorphisme local')",
    "p. 180 begins mid-sentence with 'il existe' at the left margin (page_180_s1.png)",
    "blank lines before and after \\oldpage[IV-4]{180}", "marker", None, "high",
    r"si $n=\dim(A)=\dim(A')$,<NL><NL>", r"si $n=\dim(A)=\dim(A')$,<NL>",
    "The marker is at the right place. Part 1 of 2: the p. 180 checker should remove the blank line after "
    "\\oldpage[IV-4]{180} ('\\oldpage[IV-4]{180}\\n\\nil existe'); apply both.")


# ---------------------------------------------------------------- checks
def load(p):
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


pages = {n: load(RUN / f"page_{n:03d}.tex") for n in range(175, 180)}
src = load(SRC)
ok = True
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    old = f["fix"]["old"]
    c_page = pages[f["page"]].count(old)
    c_src = src.count(old)
    if c_page != 1 or c_src != 1:
        ok = False
        print(f"#{i} p{f['page']}: page count {c_page}, source count {c_src}: {old[:80]!r}")

# simulate on the source, in list order
sim = src
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    c = sim.count(old)
    if c != 1:
        ok = False
        print(f"SIM #{i} p{f['page']}: count {c} at application time: {old[:80]!r}")
        continue
    sim = sim.replace(old, new)

a = sim.index(r"\oldpage[IV-4]{175}")
b = sim.index(r"\oldpage[IV-4]{181}")
(HERE / "after_175_179_tex.txt").write_text(sim[a:b], encoding="utf-8")

kinds = {}
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    kinds.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("counts:", kinds)
print("total:", len(F), "all ok" if ok else "PROBLEMS")
if ok or "--force" in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("written", OUT)
