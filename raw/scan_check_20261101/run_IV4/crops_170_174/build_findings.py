"""Build findings_170_174.json and check every edit against page_NNN.tex and the current source segments.
usage: python -I build_findings.py"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-18-fr.tex")
OUT = RUN / "findings_170_174.json"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def c2(page, where, old, new, note=""):
    add(page, where, "bold 0" + (" with subscript" if "mathrm" in old else ""), "plain 0", "convention", 2, "high", old, new, note)


G83 = "GLOBAL_ISSUES 83 (italics lost in 18.10 and later)."
# ---------------------------------------------------------------- p. 170
add(170, "display (18.11.2.2): 'rg_L(Ω^1_{L/k})—rg_L(Υ_{L/k})=n'", "long dash for the minus sign (wider than the equals sign; crop p170_18112_2.png)", "-",
    "convention", 7, "high",
    r"(\Omega^1_{L/k})-\operatorname{rg}_L(\Upsilon_{L/k})=n", r"(\Omega^1_{L/k})\setmin\operatorname{rg}_L(\Upsilon_{L/k})=n",
    "Long dash for subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(170, "Lemme (18.11.2), last sentence: 'donc (18.11.1) est un C-module de type fini'", "(18.11.1) upright inside the italic statement (crop p170_enoutre.png)",
    "italic (environment)", "convention", 6, "high", "donc (18.11.1) est un", r"donc \textup{(18.11.1)} est un",
    "The statement began on p. 169; this edit lies in the p. 170 segment.")
c2(170, "proof of (18.11.2), l. 1: '(0, 19.8.9)'", "(0, 19.8.9)", r"(\textbf{0}, 19.8.9)")
add(170, "proof of (18.11.2), l. 3: 'L est une extension finie du corps des fractions'", "'finie' italic (crop p170_finie.png)", "roman", "italics", None, "high",
    "une extension finie du corps des fractions", r"une extension \emph{finie} du corps des fractions", G83)
c2(170, "proof of (18.11.2): 'en appliquant (0, 20.6.17.1)'", "(0, 20.6.17.1)", r"(\textbf{0}, 20.6.17.1)")
c2(170, "proof of (18.11.2): '(0, 20.6.21, (i))'", "(0, 20.6.21, (i))", r"(\textbf{0}, 20.6.21, (i))")
c2(170, "proof of (18.11.2): 'égalité de Cartier (0, 21.7.1)'", "(0, 21.7.1)", r"(\textbf{0}, 21.7.1)")
c2(170, "proof of (18.11.2): first 'L_0 est séparable sur k (0, 21.9.6.4)'", r"). Comme $L_0$ est séparable sur $k$ (0, 21.9.6.4)",
   r"). Comme $L_0$ est séparable sur $k$ (\textbf{0}, 21.9.6.4)",
   "The 'old' begins with the closing parenthesis of (0, 21.7.1); either edit can be applied first.")
c2(170, "proof of (18.11.2): first 'Υ_{L_0/k}=0 (0, 20.6.3); on déduit'", "(0, 20.6.3); on déduit", r"(\textbf{0}, 20.6.3); on déduit")
c2(170, "proof of (18.11.2): '(0_III, 11.10.2)'", r"($0_{\mathrm{III}}$, 11.10.2)", r"($\mathbf{0}_{\mathrm{III}}$, 11.10.2)")
add(170, "display after (0_III, 11.10.2), left side: 'rg_L(Ω^1_{L/k})—rg_L(Υ_{L/k})'", "long dash for the minus sign (crop p170_disp2.png)", "-",
    "convention", 7, "high",
    "(\\Omega^1_{L/k})-\\operatorname{rg}_L(\\Upsilon_{L/k})\n  =", "(\\Omega^1_{L/k})\\setmin\\operatorname{rg}_L(\\Upsilon_{L/k})\n  =",
    "Long dash for subtraction (GLOBAL_ISSUES 23).")
add(170, "same display, right side: 'rg_{L_0}(Ω^1_{L_0/k})—rg_{L_0}(Υ_{L_0/k})'", "long dash for the minus sign (crop p170_disp2.png)", "-",
    "convention", 7, "high",
    r"(\Omega^1_{L_0/k})-\operatorname{rg}_{L_0}", r"(\Omega^1_{L_0/k})\setmin\operatorname{rg}_{L_0}",
    "Long dash for subtraction (GLOBAL_ISSUES 23).")
c2(170, "proof of (18.11.2): second 'L_0 est séparable sur k (0, 21.9.6.4)'", r"et $L_0$. Comme $L_0$ est séparable sur $k$ (0, 21.9.6.4)",
   r"et $L_0$. Comme $L_0$ est séparable sur $k$ (\textbf{0}, 21.9.6.4)")
c2(170, "proof of (18.11.2): second 'Υ_{L_0/k}=0 (0, 20.6.3); d'autre part'", "(0, 20.6.3); d'autre part", r"(\textbf{0}, 20.6.3); d'autre part")
c2(170, "proof of (18.11.2): '(0, 20.5.9)'", "(0, 20.5.9)", r"(\textbf{0}, 20.5.9)")
c2(170, "proof of (18.11.2): 'On sait (0, 21.9.4)'", "(0, 21.9.4)", r"(\textbf{0}, 21.9.4)")
c2(170, "proof of (18.11.2): '(0, 21.1.5)'", "(0, 21.1.5)", r"(\textbf{0}, 21.1.5)")
add(170, "proof of (18.11.2): 'on a k[C_0^p] ⊂ C_1, avec égalité lorsque [k : k^p]<+∞. Or'", "'égalité lorsque' italic (crop p170_egalite.png)", "roman",
    "italics", None, "high", r"avec égalité lorsque $[k:k^p]<+\infty$. Or", r"avec \emph{égalité lorsque} $[k:k^p]<+\infty$. Or",
    "Only this first 'avec égalité lorsque' is italic; the second one ('...; ceci prouve déjà') is roman in the print, as in the TeX. " + G83)
c2(170, "proof of (18.11.2): '(0, 20.5.7)'", "(0, 20.5.7)", r"(\textbf{0}, 20.5.7)")
c2(170, "proof of (18.11.2): '(0, 21.9.3)'", "(0, 21.9.3)", r"(\textbf{0}, 21.9.3)")
c2(170, "proof of (18.11.2), last paragraph: '(0_I, 7.3.3)'", r"($0_{\mathrm I}$, 7.3.3)", r"($\mathbf{0}_{\mathrm I}$, 7.3.3)")
c2(170, "proof of (18.11.2), last paragraph: '(0, 20.4.7)'", "(0, 20.4.7)", r"(\textbf{0}, 20.4.7)")
add(170, "Lemme (18.11.3), l. 2: 'locale noethérienne complète, dont'", "'complète' roman inside the italic statement (crop p170_lemma3b.png)", "italic (environment)",
    "convention", 6, "high", "noethérienne complète, dont", r"noethérienne \textup{complète}, dont")
add(170, "Lemme (18.11.3), l. 3: 'une extension finie de k'", "'finie' roman inside the italic statement (crop p170_lemma3.png)", "italic (environment)",
    "convention", 6, "high", r"extension finie de $k$. Soit", r"extension \textup{finie} de $k$. Soit")
add(170, "Lemme (18.11.3), l. 3: 'soit géométriquement régulier sur k'", "'géométriquement régulier' roman inside the italic statement", "italic (environment)",
    "convention", 6, "high", "géométriquement régulier", r"\textup{géométriquement régulier}")
add(170, "Lemme (18.11.3), l. 4: '(6.7.6)'", "reference upright", "italic (environment)", "convention", 6, "high", "(6.7.6)", r"\textup{(6.7.6)}")
add(170, "end of p. 170: page break 170/171 inside '... donc ne contient | qu'un seul idéal minimal'",
    "p. 171 begins mid-sentence with 'qu'un seul idéal minimal q de A' at the left margin",
    "blank lines before and after \\oldpage[IV-4]{171}", "marker", None, "high",
    "donc ne contient\n\n", "donc ne contient\n",
    "The marker is at the right place. Part 1 of 2: the first p. 171 finding removes the blank line after \\oldpage[IV-4]{171}; apply both (\\oldpage ends with \\ignorespaces, which does not skip a \\par).")
# ---------------------------------------------------------------- p. 171
add(171, "top of p. 171: page break 170/171", "mid-sentence continuation 'qu'un seul idéal minimal'", "blank line after \\oldpage[IV-4]{171}",
    "marker", None, "high", "\\oldpage[IV-4]{171}\n\nqu'un seul", "\\oldpage[IV-4]{171}\nqu'un seul",
    "Part 2 of 2 with the last p. 170 finding; both blank lines must go.")
c2(171, "proof of (18.11.3), l. 2: 'la suite (0, 20.7.20)'", "la suite (0, 20.7.20)", r"la suite (\textbf{0}, 20.7.20)")
add(171, "proof of (18.11.3), l. 4: 'est exacte; en effet'", "'exacte' italic (crop p171_exacte.png)", "roman", "italics", None, "high",
    "est exacte; en effet", r"est \emph{exacte}; en effet", G83)
add(171, "proof of (18.11.3), l. 5: 'Ω̂^1_{A/k}/q.Ω̂^1_{A/k}'", "baseline period between q and Ω̂ (crop p171_qdot.png)", "no period: /\\mathfrak q\\hat{\\Omega}",
    "symbol", None, "high", r"/\mathfrak q\hat{\Omega}^1_{A/k}", r"/\mathfrak q.\hat{\Omega}^1_{A/k}",
    "The print's product period, written '.' as in the earlier page fixes (GLOBAL_ISSUES 65).")
c2(171, "proof of (18.11.3): '(0_I, 7.3.5)'", r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)")
c2(171, "proof of (18.11.3): 'compte tenu de (0, 20.4.5)'", "compte tenu de (0, 20.4.5)", r"compte tenu de (\textbf{0}, 20.4.5)")
c2(171, "proof of (18.11.3): 'Ω̂^1_{B/k} (0, 20.7.20), elle est'", "(0, 20.7.20), elle", r"(\textbf{0}, 20.7.20), elle")
add(171, "proof of (18.11.3): 'est bijectif. On voit ainsi'", "'bijectif' italic", "roman", "italics", None, "high",
    "est bijectif. On voit", r"est \emph{bijectif}. On voit", G83)
add(171, "proof of (18.11.3): 'au cas où A est intègre. Distinguons'", "'intègre' italic (crop p171_integre.png)", "roman", "italics", None, "high",
    "$A$ est intègre. Distinguons", r"$A$ est \emph{intègre}. Distinguons", G83)
add(171, "case heading 'I) p>1.'", "'I)' and the full stop upright, p italic (crop p171_I.png)", "\\emph{I) $p>1$.}: the label comes out italic",
    "italics", None, "high", r"\emph{I) $p>1$.}", r"I) $p>1$.",
    "Proof-part labels are printed upright (GLOBAL_ISSUES 51/76).")
add(171, "display (18.11.3.1): 'rg_K(Ω^1_{K/k})—rg_K(Υ_{K/k})=dim(A/p)'", "long dash for the minus sign", "-", "convention", 7, "high",
    r"(\Omega^1_{K/k})-\operatorname{rg}_K(\Upsilon_{K/k})=\dim", r"(\Omega^1_{K/k})\setmin\operatorname{rg}_K(\Upsilon_{K/k})=\dim",
    "Long dash for subtraction (GLOBAL_ISSUES 23).")
c2(171, "case I): 'Notons maintenant (0, 19.6.6)'", "(0, 19.6.6)", r"(\textbf{0}, 19.6.6)")
add(171, "case I), l. 1: 'A_p est une k-algèbre formellement lisse pour sa topologie pA_p-préadique'", "'formellement lisse' italic", "roman",
    "italics", None, "high", "formellement lisse pour sa", r"\emph{formellement lisse} pour sa",
    "The second 'formellement lisse' of the page ('A' est encore une k-algèbre formellement lisse (0, 19.3.6)') is roman in the print, as in the TeX. " + G83)
c2(171, "case I): 'formellement projectif (0, 20.4.9)'", "(0, 20.4.9)", r"(\textbf{0}, 20.4.9)")
c2(171, "case I): 'p-préadique (0, 20.4.5); d'autre part'", "(0, 20.4.5); d'autre part", r"(\textbf{0}, 20.4.5); d'autre part")
c2(171, "case I): '(0, 20.5.9)'", "(0, 20.5.9)", r"(\textbf{0}, 20.5.9)")
c2(171, "case I): '(0, 19.2.4)'", "(0, 19.2.4)", r"(\textbf{0}, 19.2.4)")
c2(171, "case I): '(0_III, 10.2.1 et 10.1.3)'", r"($0_{\mathrm{III}}$, 10.2.1", r"($\mathbf{0}_{\mathrm{III}}$, 10.2.1")
add(171, "case I): 'on conclut donc de (0_III, 10.2.1 et 10.1.3) que Ω^1_{A_p/k} est un A_p-module libre'",
    "Ω^1_{A_p/k} without a hat (crop p171_omhat.png)", "\\hat{\\Omega}^1_{A_{\\mathfrak p}/k}", "symbol", None, "high",
    r"que $\hat{\Omega}^1_{A_{\mathfrak p}/k}$ est un", r"que $\Omega^1_{A_{\mathfrak p}/k}$ est un",
    "No hat in the print (the hatted Ω̂^1_{A_p/k} first appears in the next sentence); the statement concerns the finite A_p-module Ω^1_{A_p/k} of the preceding sentences, so the printed reading is not a misprint.")
add(171, "case I): 'est un A_p-module libre de rang m. Soit'", "'module libre de rang m' italic (crops p171_omhat.png, p171_libre1.png)", "roman",
    "italics", None, "high", r"$A_{\mathfrak p}$-module libre de rang $m$. Soit", r"$A_{\mathfrak p}$-\emph{module libre de rang $m$}. Soit", G83)
add(171, "case I): 'A' = (A_p)^ l'algèbre complétée'", "raised circumflex accent after the closing parenthesis (crop p171_Aphat.png)", "^\\wedge (logical-and sign)",
    "symbol", None, "high", r"(A_{\mathfrak p})^\wedge", r"(A_{\mathfrak p})^{\widehat{\,}}",
    "As the earlier page fixes of the raised circumflex (EGA II p. 194, IV-2 p. 217); \\superhat pending (GLOBAL_ISSUES 31/47).")
add(171, "case I): 'l'algèbre complétée de A_p'", "'complétée' italic", "roman", "italics", None, "high",
    "l'algèbre complétée de", r"l'algèbre \emph{complétée} de", G83)
c2(171, "case I): '(0, 19.3.6)'", "(0, 19.3.6)", r"(\textbf{0}, 19.3.6)")
c2(171, "case I): '(0, 20.7.14)'", "(0, 20.7.14)", r"(\textbf{0}, 20.7.14)")
c2(171, "case I): 'et de (0, 20.4.5) que'", "et de (0, 20.4.5) que", r"et de (\textbf{0}, 20.4.5) que")
add(171, "case I): 'est un A'-module libre de rang m. Mais'", "'libre de rang m' italic, 'module' roman (crop p171_libre2.png)", "roman",
    "italics", None, "high", r"$A'$-module libre de rang $m$. Mais", r"$A'$-module \emph{libre de rang $m$}. Mais", G83)
c2(171, "case I): '(0, 16.2.4)'", "(0, 16.2.4)", r"(\textbf{0}, 16.2.4)")
add(171, "display (18.11.3.2): 'm=dim(A_p)+(rg_K(Ω^1_{K/k})—rg_K(Υ_{K/k}))'", "long dash for the minus sign (crop p171_18113_2.png)", "-",
    "convention", 7, "high", r"\bigl(\operatorname{rg}_K(\Omega^1_{K/k})-", r"\bigl(\operatorname{rg}_K(\Omega^1_{K/k})\setmin",
    "Long dash for subtraction (GLOBAL_ISSUES 23).")
add(171, "display (18.11.3.2), end", "no punctuation after the display (crop p171_18113_2.png); 'd'où, en vertu de' follows",
    "comma after \\bigr)", "punctuation", None, "high", r"(\Upsilon_{K/k})\bigr),", r"(\Upsilon_{K/k})\bigr)", "")
c2(171, "case I), last lines: '(0, 19.8.8)'", "(0, 19.8.8)", r"(\textbf{0}, 19.8.8)")
c2(171, "case I), last lines: '(0, 16.5.12)'", "(0, 16.5.12)", r"(\textbf{0}, 16.5.12)")
add(171, "case heading 'II) p=1.'", "'II)' and the full stop upright, p italic (crop p171_II.png)", "\\emph{II) $p=1$.}: the label comes out italic",
    "italics", None, "high", r"\emph{II) $p=1$.}", r"II) $p=1$.",
    "Proof-part labels are printed upright (GLOBAL_ISSUES 51/76).")
add(171, "end of p. 171: page break 171/172 inside Lemme (18.11.3.3) ('... d'un système de paramètres de A | et que, pour tout i')",
    "p. 172 begins mid-sentence with 'et que, pour tout i' at the left margin", "blank lines before and after \\oldpage[IV-4]{172}",
    "marker", None, "high", "de paramètres de $A$\n\n", "de paramètres de $A$\n",
    "The marker is at the right place. Part 1 of 2: the first p. 172 finding removes the blank line after \\oldpage[IV-4]{172}; apply both. Inside the lemma the blank lines would start a new paragraph.")
# ---------------------------------------------------------------- p. 172
add(172, "top of p. 172: page break 171/172", "mid-sentence continuation of Lemme (18.11.3.3)", "blank line after \\oldpage[IV-4]{172}",
    "marker", None, "high", "\\oldpage[IV-4]{172}\n\net que, pour tout", "\\oldpage[IV-4]{172}\net que, pour tout",
    "Part 2 of 2 with the last p. 171 finding; both blank lines must go.")
add(172, "Lemme (18.11.3.3): 'modulo l'idéal t_1A_p+...+t_{i-1}A_p'", "baseline dots (crop p172_dots.png)", "\\cdots", "symbol", None, "high",
    r"+\cdots+", r"+\ldots+",
    "The subscript minus of t_{i-1} is the ordinary short minus (about 22 px), as the TeX has: not convention 7.")
add(172, "Lemme (18.11.3.3): 'forment un système régulier de paramètres'", "'régulier' roman inside the italic statement (crop p172_regulier.png)",
    "italic (environment)", "convention", 6, "high", "forment un système régulier de paramètres", r"forment un système \textup{régulier} de paramètres",
    "The first 'régulier' of the sentence ('si A_p est régulier') is italic in the print, as in the TeX.")
c2(172, "proof of (18.11.3.3): 'idéaux premiers minimaux de A_p (0, 16.5.5), donc'", "(0, 16.5.5), donc", r"(\textbf{0}, 16.5.5), donc")
add(172, "proof of (18.11.3.3): 'donc aucun x'_i ∈ A tel que x'_1/1 = t_1'", "x'_i (subscript i, with its dot; crop p172_xi.png)",
    "x'_1 (silently corrected)", "misprint_in_print", None, "high", r"aucun $x'_1\in A$", r"aucun $x'_i\in A$",
    "The element is the x'_1 of the condition x'_1/1 = t_1 that follows (i is not bound here). The TeX silently corrected the print; this edit restores the printed reading.",
    corrected=r"aucun $x'_1\in A$")
add(172, "proof of (18.11.3.3): 'que x'_1 n'appartienne à aucun idéal premier minimal de A'", "'aucun' italic (crop p172_aucun.png)", "roman",
    "italics", None, "high", "n'appartienne à aucun idéal", r"n'appartienne à \emph{aucun} idéal", G83)
c2(172, "proof of (18.11.3.3): '(0, 16.3.4 et 16.3.7)'", "(0, 16.3.4 et 16.3.7)", r"(\textbf{0}, 16.3.4 et 16.3.7)")
c2(172, "proof of (18.11.3.3): 'anneau de Cohen-Macaulay (0, 16.5.5), et les images'", "(0, 16.5.5), et les", r"(\textbf{0}, 16.5.5), et les")
c2(172, "proof of (18.11.3.3): '(0, 17.1.1)'", "(0, 17.1.1)", r"(\textbf{0}, 17.1.1)")
c2(172, "return to (18.11.3), p=1: '(0_I, 7.4.4 et 7.4.3)'", r"($0_{\mathrm I}$, 7.4.4 et 7.4.3)", r"($\mathbf{0}_{\mathrm I}$, 7.4.4 et 7.4.3)")
add(172, "return to (18.11.3), p=1: 'u fait de A une A_0-algèbre finie.'", "'finie' italic (crop p172_finie.png)", "roman", "italics", None, "high",
    "$A_0$-algèbre finie.", r"$A_0$-algèbre \emph{finie}.", G83)
add(172, "end of p. 172: page break 172/173 inside '... de sorte que u_{p_0} : B_0 → B fait | de B une B_0-algèbre finie'",
    "p. 173 begins mid-sentence with 'de B une B_0-algèbre finie'", "blank lines before and after \\oldpage[IV-4]{173}",
    "marker", None, "high", "B_0\\to B$ fait\n\n", "B_0\\to B$ fait\n",
    "The marker is at the right place. Part 1 of 2: the first p. 173 finding removes the blank line after \\oldpage[IV-4]{173}; apply both.")
# ---------------------------------------------------------------- p. 173
add(173, "top of p. 173: page break 172/173", "mid-sentence continuation 'de B une B_0-algèbre finie'", "blank line after \\oldpage[IV-4]{173}",
    "marker", None, "high", "\\oldpage[IV-4]{173}\n\nde $B$ une", "\\oldpage[IV-4]{173}\nde $B$ une",
    "Part 2 of 2 with the last p. 172 finding; both blank lines must go.")
add(173, "l. 3: 'le morphisme Spec(B) → Spec(B_0) est non ramifié au point p''", "'non ramifié' italic", "roman", "italics", None, "high",
    "est non ramifié au point", r"est \emph{non ramifié} au point",
    "The second 'non ramifié' of the page ('Spec(B) est non ramifié sur Spec(B_0)') is roman in the print, as in the TeX. " + G83)
add(173, "l. 4: 'de ce que k(p') est une extension finie'", "bold italic k", "plain k", "convention", 1, "high",
    r"ce que $k(\mathfrak p')$ est une", r"ce que $\boldsymbol{k}(\mathfrak p')$ est une")
add(173, "l. 4: 'du corps k(p_0) de caractéristique 0'", "bold italic k", "plain k", "convention", 1, "high",
    r"du corps $k(\mathfrak p_0)$", r"du corps $\boldsymbol{k}(\mathfrak p_0)$")
add(173, "l. 5: 'donc est nécessairement séparable'", "'nécessairement séparable' italic", "roman", "italics", None, "high",
    "donc est nécessairement séparable,", r"donc est \emph{nécessairement séparable},", G83)
add(173, "l. 5: 'B_{p'}/p_0B_{p'} = k(p')'", "bold italic k", "plain k", "convention", 1, "high",
    r"=k(\mathfrak p')$ en vertu", r"=\boldsymbol{k}(\mathfrak p')$ en vertu")
add(173, "l. 5-6: 'en vertu du choix des x pour 1≤j≤s (17.4.1)'", "'des x' with no subscript, last character of the line (crops p173_xj.png, p173_xj2.png)",
    "$x_j$ (silently corrected)", "misprint_in_print", None, "high", r"choix des $x_j$ pour", r"choix des $x$ pour",
    "The x ends 5 px short of the right margin of the full lines (2049 against 2053-2058), so no subscript sort was lost: the print omits the j. Correct reading x_j (the x_j, 1≤j≤s, chosen in the proof on p. 172). The TeX silently corrected the print; this edit restores the printed reading.",
    corrected=r"$x_j$")
add(173, "display (18.11.3.6): 'Ω̂^1_{R/k} ⊗̂_R S'", "completed tensor product (⊗ with a hat; crop p173_18113_6.png)", "\\otimes_R", "symbol", None, "high",
    r"\hat{\Omega}^1_{R/k}\otimes_R S", r"\hat{\Omega}^1_{R/k}\widehat{\otimes}_R S",
    "Same sequence as (0, 20.7.17.3); the proof of (18.11.3) uses it as Ω̂^1_{A_0/k}⊗̂_{A_0}A.")
add(173, "Lemme (18.11.3.5), after (18.11.3.6): '(cf. (0, 20.7.17.3)) est exacte.'",
    "'(cf. (0, 20.7.17.3))' upright with a bold 0, 'est exacte' italic (crop p173_cf.png)", "all italic (environment), plain 0",
    "convention", 2, "high", "(cf. (0, 20.7.17.3)) est exacte", r"\textup{(cf. (\textbf{0}, 20.7.17.3))} est exacte",
    "One edit for convention 2 (bold 0) and convention 6 (upright reference in the italic statement); count it under both.")
c2(173, "proof of (18.11.3.5): '(0, 20.4.7)'", "(0, 20.4.7)", r"(\textbf{0}, 20.4.7)")
c2(173, "proof of (18.11.3.5): '(0_I, 7.3.6)'", r"($0_{\mathrm I}$, 7.3.6)", r"($\mathbf{0}_{\mathrm I}$, 7.3.6)")
c2(173, "proof of (18.11.3.5): 'on sait (0, 20.7.17.3)'", "on sait (0, 20.7.17.3)", r"on sait (\textbf{0}, 20.7.17.3)")
c2(173, "proof of (18.11.3.5): '(0_I, 7.3.5)'", r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)")
c2(173, "'Appliquons ce lemme': '(0, 21.9.3)'", "(0, 21.9.3)", r"(\textbf{0}, 21.9.3)")
add(173, "'on obtient donc un homomorphisme surjectif'", "'surjectif' italic", "roman", "italics", None, "high",
    "un homomorphisme surjectif", r"un homomorphisme \emph{surjectif}", G83)
add(173, "display after 'homomorphisme surjectif'", "'v_p : (Ω̂^1_{A_0/k}⊗_{A_0}A)_p → (Ω̂^1_{A/k})_p' (crop p173_vp.png)", "the map name 'v_p :' is missing",
    "missing", None, "high", r"(\hat{\Omega}^1_{A_0/k}\otimes_{A_0}A)_{\mathfrak p}\longrightarrow",
    r"v_{\mathfrak p}:(\hat{\Omega}^1_{A_0/k}\otimes_{A_0}A)_{\mathfrak p}\longrightarrow",
    "The localisation at p of the map v of (18.11.3.6).")
add(173, "same display, end", "no punctuation after the display (crop p173_vp.png); 'd'où l'on conclut' follows", "comma after the display",
    "punctuation", None, "high", "(\\hat{\\Omega}^1_{A/k})_{\\mathfrak p},\n\\]", "(\\hat{\\Omega}^1_{A/k})_{\\mathfrak p}\n\\]", "")
add(173, "'le A-module Ω̂^1_{A/k} est de rang n, en vertu de'", "'rang n' italic (crop p173_rang.png)", "roman", "italics", None, "high",
    r"est de rang $n$, en vertu", r"est de \emph{rang $n$}, en vertu", G83)
c2(173, "'en vertu de (0, 21.9.5)'", "(0, 21.9.5)", r"(\textbf{0}, 21.9.5)")
c2(173, "'théorème de Cohen (0, 19.8.8, (ii))'", "(0, 19.8.8, (ii))", r"(\textbf{0}, 19.8.8, (ii))")
add(173, "'ce quotient est nécessairement libre;'", "'libre' italic", "roman", "italics", None, "high",
    "nécessairement libre;", r"nécessairement \emph{libre};", G83)
add(173, "'forment un système libre, d'où la conclusion'", "'libre' italic", "roman", "italics", None, "high",
    "un système libre, d'où", r"un système \emph{libre}, d'où", G83)
add(173, "Lemme (18.11.4), label (i)", "label (i) upright", "italic (environment)", "convention", 6, "high",
    r"\item[(i)] $A'$ est", r"\item[\textup{(i)}] $A'$ est", "GLOBAL_ISSUES 16.")
add(173, "Lemme (18.11.4) (i): 'A'_i (1≤i≤r) qui sont'", "parentheses upright (crop p173_paren.png)", "italic parentheses (environment)",
    "convention", 6, "high", r"$A'_i$ ($1\leq i\leq r$) qui", r"$A'_i$ \textup{($1\leq i\leq r$)} qui", "GLOBAL_ISSUES 26.")
add(173, "Lemme (18.11.4), label (ii)", "label (ii) upright (crop p173_ii.png)", "italic (environment)", "convention", 6, "high",
    r"\item[(ii)] Pour tout", r"\item[\textup{(ii)}] Pour tout", "GLOBAL_ISSUES 16.")
add(173, "Lemme (18.11.4) (ii): 'Ω̂^1_{A'_i/k} est canoniquement isomorphe'", "subscript A'_i/k, no prime on k (crops p173_ii.png, p173_ii_k.png)",
    "A'_i/k' (silently corrected)", "misprint_in_print", None, "high",
    r"\hat{\Omega}^1_{A'_i/k'}$ est canoniquement", r"\hat{\Omega}^1_{A'_i/k}$ est canoniquement",
    "The proof (p. 174) identifies Ω̂^1_{A'/k'}, hence the Ω̂^1_{A'_i/k'}, with Ω̂^1_{A/k}⊗_A A'_i; with k the statement is false in general (Ω^1_{k'/k} contributes). The TeX silently corrected the print; this edit restores the printed reading.",
    corrected=r"\hat{\Omega}^1_{A'_i/k'}")
# ---------------------------------------------------------------- p. 174
c2(174, "proof of (18.11.4) (i): '(0_I, 6.6.2)'", r"($0_{\mathrm I}$, 6.6.2)", r"($\mathbf{0}_{\mathrm I}$, 6.6.2)")
add(174, "proof of (18.11.4) (i): 'car si K est le corps résiduel de A, K⊗_A k' est une k'-algèbre finie'", "K⊗_A k' (subscript A; crop p174_KA.png)",
    "K\\otimes_k k' (silently corrected)", "misprint_in_print", None, "high", r"$K\otimes_k k'$ est une", r"$K\otimes_A k'$ est une",
    "k' is not an A-module; the same sentence two lines further has K⊗_k k' (7.5.5). The TeX silently corrected the print; this edit restores the printed reading.",
    corrected=r"$K\otimes_k k'$")
c2(174, "proof of (18.11.4) (ii): '(0_I, 7.7.4)'", r"($0_{\mathrm I}$, 7.7.4)", r"($\mathbf{0}_{\mathrm I}$, 7.7.4)")
c2(174, "proof of (18.11.4) (ii): '(0, 20.5.5)'", "(0, 20.5.5)", r"(\textbf{0}, 20.5.5)")
c2(174, "proof of (18.11.4) (ii): '(0, 20.7.4)'", "(0, 20.7.4)", r"(\textbf{0}, 20.7.4)")
add(174, "proof of (18.11.4) (ii), display after 'un isomorphisme canonique'", "Ω̂^1_{A'/k'} ⥲ Ω̂^1_{A/k}⊗_A A'. (crop p174_disp.png)",
    "Ω̂^1_{A/k}⊗̂_k k' ⥲ Ω̂^1_{A'/k'}. (other source and target)", "formula", None, "high",
    r"\hat{\Omega}^1_{A/k}\widehat{\otimes}_k k'\xrightarrow{\sim}\hat{\Omega}^1_{A'/k'}.",
    r"\hat{\Omega}^1_{A'/k'}\xrightarrow{\sim}\hat{\Omega}^1_{A/k}\otimes_A A'.",
    "The TeX rewrote the printed display; the print's isomorphism is correct as printed (Ω̂^1_{A/k}⊗_A A' was identified with Ω̂^1_{A/k}⊗̂_k k' two lines earlier), so this is not a misprint.")
c2(174, "proof of (18.11.4) (ii): '(0, 20.4.13)'", "(0, 20.4.13)", r"(\textbf{0}, 20.4.13)")
add(174, "proof of (18.11.4) (ii): 'au produit des topologies m'_i-préadiques sur les Ω^1_{A'/k'} (où m'_i'",
    "Ω^1_{A'/k'}: no subscript i under the prime (crop p174_surles.png)", "Ω^1_{A'_i/k'} (silently corrected)", "misprint_in_print", None, "high",
    r"sur les $\Omega^1_{A'_i/k'}$ (où", r"sur les $\Omega^1_{A'/k'}$ (où",
    "Plural 'les' and the topologies m'_i-préadiques need the factors Ω^1_{A'_i/k'} (as in 'somme directe des Ω^1_{A'_i/k'}' just before). The TeX silently corrected the print; this edit restores the printed reading.",
    corrected=r"$\Omega^1_{A'_i/k'}$")
c2(174, "proof of (18.11.4) (ii), end: '(0, 20.4.5)'", "(0, 20.4.5)", r"(\textbf{0}, 20.4.5)")
add(174, "Proposition (18.11.5), l. 3-4: '(ce qui aura lieu en particulier lorsque A est équidimensionnel)'",
    "parenthetical roman with upright parentheses, only 'équidimensionnel' italic (crops p174_cequi1.png, p174_cequi2.png, p174_equi_paren.png)",
    "all italic (environment)", "convention", 6, "high",
    r"(ce qui aura lieu en particulier lorsque $A$ est équidimensionnel)",
    r"\textup{(ce qui aura lieu en particulier lorsque $A$ est \emph{équidimensionnel})}",
    "The closing parenthesis is upright too (measured: its two ends stand at the same x, like the parentheses of dim(A)); inside \\textup the \\emph gives italic.")
add(174, "Proposition (18.11.5), label a)", "label 'a)' upright (crop p174_ab.png)", "\\item[$a)$]: italic a", "convention", 6, "high",
    r"\item[$a)$] Le", r"\item[\textup{a)}] Le", "GLOBAL_ISSUES 88.")
add(174, "Proposition (18.11.5), label b)", "label 'b)' upright (crop p174_ab.png)", "\\item[$b)$]: italic b", "convention", 6, "high",
    r"\item[$b)$] Il existe", r"\item[\textup{b)}] Il existe", "GLOBAL_ISSUES 88.")
add(174, "proof of (18.11.5): 'Pour prouver que b) entraîne a),'", "labels b), a) wholly italic, parentheses included (crop p174_ba.png)",
    "$b)$, $a)$: italic letters, upright parentheses", "italics", None, "high",
    r"Pour prouver que $b)$ entraîne $a)$,", r"Pour prouver que \emph{b)} entraîne \emph{a)},", "GLOBAL_ISSUES 88.")
c2(174, "proof of (18.11.5): '(0, 21.9.3)'", "(0, 21.9.3)", r"(\textbf{0}, 21.9.3)")
add(174, "'Pour prouver que a) implique b),'", "labels a), b) wholly italic (crop p174_ab2.png)", "$a)$, $b)$: italic letters, upright parentheses",
    "italics", None, "high", r"Pour prouver que $a)$ implique $b)$,", r"Pour prouver que \emph{a)} implique \emph{b)},", "GLOBAL_ISSUES 88.")

# ---------------------------------------------------------------- checks
marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")
src = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    if 170 <= n <= 174:
        seg[n] = src[s:cuts[i + 1][1]]
ok = True
for x in F:
    if x["fix"] is None:
        continue
    page = x["page"]
    pt = (RUN / f"page_{page}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    o = x["fix"]["old"]
    if pt.count(o) != 1 or seg[page].count(o) != 1:
        ok = False
        print("NOT UNIQUE", page, pt.count(o), seg[page].count(o), repr(o))
# sequential application, forward and backward
for order in ("forward", "backward"):
    s2 = dict(seg)
    items = [x for x in F if x["fix"]]
    if order == "backward":
        items = items[::-1]
    for x in items:
        p, o, nw = x["page"], x["fix"]["old"], x["fix"]["new"]
        c = s2[p].count(o)
        if c != 1:
            ok = False
            print(order, "apply fails", p, c, repr(o))
        else:
            s2[p] = s2[p].replace(o, nw)
    if order == "forward":
        final = s2
print("all checks passed" if ok else "CHECK FAILURES")
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
cnt = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
for p in sorted(cnt):
    print(p, cnt[p])
print(len(F), "findings written to", OUT)
for p in sorted(final):
    (RUN / "crops_170_174" / f"after_{p}_tex.txt").write_text(final[p], encoding="utf-8", newline="")
