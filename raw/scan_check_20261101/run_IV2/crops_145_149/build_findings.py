"""Build findings_145_149.json and verify every edit.

Checks: (1) each fix's "old" occurs exactly once in its page_NNN.tex (original text);
(2) applied in list order to each page file, each "old" occurs exactly once when it is applied;
(3) the same list applied to an in-memory copy of the release file with the applier's page-location
    logic (apply_fixes.py) succeeds for every edit. Nothing is written to any .tex file.
Strings use <NL> for a line break.
"""
import json
import re
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
REL = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
OUT = RUN / "findings_145_149.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace("<NL>", "\n"), "new": new.replace("<NL>", "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


DASH = ("The print has a hyphen (same length as in 'O_X-Module'); '--' typesets an en dash. "
        "ega4-2-fr.tex has Cohen-Macaulay on 62 lines and Cohen--Macaulay on 37.")
BOLDP = "Bold italic property letter, as in earlier page fixes (GLOBAL_ISSUES 13)."
BOLDQ = "Bold italic Q, like the property letter P."
BOLDT = "The indeterminate t is bold UPRIGHT in the print (enlarged crop); \\boldsymbol t gives bold italic."
REMARK = "Remark body judged as roman (document-wide remark environment); the print sets these words italic."

# ---------------------------------------------------------------- page 145
p = 145
add(p, "heading 6.6", "'6.6. Propriétés de transitivité.' (final full stop)",
    "\\subsection{Propriétés de transitivité} (no full stop)", "punctuation", None, "high",
    r"\subsection{Propriétés de transitivité}", r"\subsection{Propriétés de transitivité.}",
    "GLOBAL_ISSUES 43 pattern.")
add(p, "Proposition (6.6.1), l. 1: 'désignons par P(Z)'", "bold italic P", "$P(Z)$ (light italic P)",
    "font", None, "high", r"$P(Z)$", r"$\boldsymbol{P}(Z)$", BOLDP)
for L in "abcdef":
    add(p, f"Proposition (6.6.1), label {L})", f"upright label '{L})' with no opening parenthesis",
        f"\\item[({L})] (prints an italic '({L})' in the proposition)", "punctuation", None, "high",
        f"\\item[({L})]", f"\\item[\\textup{{{L})}}]",
        "Same pattern as run_I_b p. 175." if L == "a" else "")
add(p, "Proposition (6.6.1) a): 'préschéma de Cohen-Macaulay'", "hyphen", "Cohen--Macaulay (en dash)",
    "punctuation", None, "high", r"Cohen--Macaulay", r"Cohen-Macaulay", DASH)
add(p, "Proposition (6.6.1), sentence before (i)",
    "'f : X→Y, g : Y→Z deux morphismes.' (h=g∘f is introduced only in (i): 'Alors h=g∘f est plat')",
    "'deux morphismes, et posons $h=g\\circ f$.'", "extra", None, "high",
    r"deux morphismes, et posons $h=g\circ f$.", r"deux morphismes.",
    "Goes with the 'Alors h=g∘f est plat' entry below.")
add(p, "Proposition (6.6.1), label (i)", "label (i) upright", "\\item[(i)] in the italic statement (italic label)",
    "convention", 6, "high", r"\item[(i)] Supposons que", r"\item[\textup{(i)}] Supposons que")
add(p, "Proposition (6.6.1) (i), l. 1: 'et que pour tout y∈f(X)'", "no comma after 'que'", "'et que, pour tout'",
    "punctuation", None, "high", r"et que, pour tout", r"et que pour tout")
add(p, "Proposition (6.6.1) (i): '(resp. tout z∈g(Y))'", "'(resp.' upright", "italic in the statement",
    "convention", 6, "high", r"(resp. tout $z\in g(Y)$)", r"\textup{(resp.} tout $z\in g(Y)$)")
add(p, "Proposition (6.6.1) (i): '(resp. g^{-1}(z))'", "'(resp.' upright", "italic in the statement",
    "convention", 6, "high", r"(resp. $g^{-1}(z)$)", r"\textup{(resp.} $g^{-1}(z)$)")
add(p, "Proposition (6.6.1) (i): 'vérifie P. Alors'", "bold italic P", "$P$", "font", None, "high",
    r"vérifie $P$. Alors $h", r"vérifie $\boldsymbol{P}$. Alors $h", BOLDP)
add(p, "Proposition (6.6.1) (i): 'Alors h=g∘f est plat'", "'Alors h=g∘f est plat'", "'Alors $h$ est plat'",
    "missing", None, "high", r"Alors $h$ est plat", r"Alors $h=g\circ f$ est plat")
add(p, "Proposition (6.6.1) (i): 'est plat et pour tout z∈h(X)'", "no comma after 'et'", "'et, pour tout'",
    "punctuation", None, "high", r"est plat et, pour tout<NL>$z\in h(X)$", r"est plat et pour tout<NL>$z\in h(X)$")
add(p, "Proposition (6.6.1) (i), end: 'h^{-1}(z) vérifie P.'", "bold italic P", "$P$", "font", None, "high",
    r"$z\in h(X)$, $h^{-1}(z)$ vérifie $P$.", r"$z\in h(X)$, $h^{-1}(z)$ vérifie $\boldsymbol{P}$.", BOLDP)
add(p, "Proposition (6.6.1), label (ii)", "label (ii) upright", "\\item[(ii)] in the italic statement",
    "convention", 6, "high", r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons")
add(p, "Proposition (6.6.1) (ii): 'f^{-1}(y) vérifie P, et'", "bold italic P", "$P$", "font", None, "high",
    r"vérifie $P$, et", r"vérifie $\boldsymbol{P}$, et", BOLDP)
add(p, "Proposition (6.6.1) (ii): 'et pour tout z∈h(X) le préschéma'", "no commas after 'et' and after 'h(X)'",
    "'et, pour tout $z\\in h(X)$, le'", "punctuation", None, "high",
    r"et, pour tout $z\in h(X)$, le", r"et pour tout $z\in h(X)$ le")
add(p, "Proposition (6.6.1) (ii): 'h^{-1}(z) vérifie P. Alors g'", "bold italic P", "$P$", "font", None, "high",
    r"vérifie $P$. Alors $g$", r"vérifie $\boldsymbol{P}$. Alors $g$", BOLDP)
add(p, "Proposition (6.6.1) (ii): 'Alors g est plat, et pour tout z∈g(Y)'", "comma before 'et', none after",
    "'est plat et, pour tout'", "punctuation", None, "high",
    r"est plat et, pour tout<NL>$z\in g(Y)$", r"est plat, et pour tout<NL>$z\in g(Y)$")
add(p, "Proposition (6.6.1) (ii), end: 'g^{-1}(z) vérifie P.'", "bold italic P", "$P$", "font", None, "high",
    r"$g^{-1}(z)$ vérifie $P$.", r"$g^{-1}(z)$ vérifie $\boldsymbol{P}$.", BOLDP)
add(p, "proof of (6.6.1) (edit 1 of 2: close the proposition before the proof)",
    "the proof '(i) On sait déjà (2.1.6) que h est plat; ...' is set in roman",
    "the proof's enumerate is inside \\begin{proposition}...\\end{proposition}, so it is typeset italic",
    "italics", None, "high",
    r"\end{enumerate}<NL>\begin{enumerate}<NL>\item[(i)] On sait",
    r"\end{enumerate}<NL>\end{proposition}<NL><NL>\begin{enumerate}<NL>\item[(i)] On sait",
    "Apply together with the next edit. No proof heading is added: the print has none.")
add(p, "proof of (6.6.1) (edit 2 of 2: remove the old \\end{proposition})", "see the previous entry",
    "\\end{proposition} after the proof", "italics", None, "high",
    r"(2.1.13).<NL>\end{enumerate}<NL>\end{proposition}", r"(2.1.13).<NL>\end{enumerate}",
    "Apply together with the previous edit.")
add(p, "proof of (6.6.1) (i): 'f_z=f⊗1_{k(z)} : h^{-1}(z) → g^{-1}(z) est plat (2.1.4)'",
    "formula in the running text", "displayed with \\[ ... \\]", "other", None, "high",
    r"\[<NL> f_z=f\otimes 1_{k(z)}:h^{-1}(z)\longrightarrow g^{-1}(z)<NL>\]<NL>est plat",
    r"$f_z=f\otimes 1_{k(z)}:h^{-1}(z)\longrightarrow g^{-1}(z)$ est plat",
    "Display vs inline. Apply before the next entry.")
add(p, "proof of (6.6.1) (i): subscript of 1_{k(z)}", "bold upright k in the subscript (enlarged crop)", "k(z)",
    "convention", 1, "high", r"1_{k(z)}", r"1_{\mathbf{k}(z)}",
    "Bold upright in a subscript (GLOBAL_ISSUES 48). Apply after the display entry above.")
add(p, "proof of (6.6.1) (i): '(2.1.4), et pour tout y∈g^{-1}(z)'", "no comma after 'et'", "'et, pour tout'",
    "punctuation", None, "high", r"(2.1.4), et, pour tout", r"(2.1.4), et pour tout")
add(p, "proof of (6.6.1) (i): '(I, 3.6.4)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
add(p, "proof of (6.6.1) (ii), last line: '(6.5.4, (ii)) et (2.1.13)'",
    "(6.5.4, (ii)) (enlarged crop)", "(6.5.4, (ii)): the TeX keeps the printed reading",
    "misprint_in_print", None, "medium", None, None,
    "Part (ii) descends P along the faithfully flat f_z (h^{-1}(z) normal => g^{-1}(z) normal), which is (6.5.4, (i)) "
    "('Si X est normal en un point x, Y est normal au point f(x)'); (ii) of (6.5.4) is the ascending statement. "
    "The parallel references in the same list are (6.3.5, (i)), (6.5.2, (i)), (6.5.3, (i)), and the proof of (6.7.4) "
    "uses (6.5.4, (i)) for the same descent. Not in the authors' errata list 3 (only 6.7.2 there).",
    corrected="(6.5.4, (i))")
add(p, "Remarque (6.6.2), l. 1: 'supposons que pour tout z∈Z'", "no comma after 'que'", "'supposons que, pour tout'",
    "punctuation", None, "high", r"supposons que, pour tout", r"supposons que pour tout")
add(p, "Remarque (6.6.2): 'soit de coprofondeur ≤n'", "'de coprofondeur' italic", "roman", "italics", None, "high",
    r"soit de coprofondeur", r"soit \emph{de coprofondeur}", REMARK)
add(p, "Remarque (6.6.2): 'g^{-1}(z) est de coprofondeur ≤n'", "'de coprofondeur' italic", "roman", "italics", None,
    "high", r"$g^{-1}(z)$ est de coprofondeur", r"$g^{-1}(z)$ est \emph{de coprofondeur}", REMARK)
add(p, "Remarque (6.6.2), end: 'que pour tout y∈Y'", "no comma after 'que'", "'que, pour tout'", "punctuation",
    None, "high", r"que, pour tout $y\in Y$", r"que pour tout $y\in Y$")
add(p, "Remarque (6.6.2), end: 'f^{-1}(y) est de coprofondeur ≤n'", "'de coprofondeur' italic", "roman", "italics",
    None, "high", r"$f^{-1}(y)$ est de coprofondeur", r"$f^{-1}(y)$ est \emph{de coprofondeur}", REMARK)

# ---------------------------------------------------------------- page 146 (segment starts with text printed on p. 145)
p = 146
P145 = "Printed on p. 145; this text lies in the p. 146 segment until the marker move at the end of this page's list."
add(p, "heading 6.7 (printed on p. 145)", "'6.7. Application aux changements de base dans les préschémas algébriques.'",
    "no full stop in the \\subsection title", "punctuation", None, "high",
    r"\subsection{Application aux changements de base dans les préschémas algébriques}",
    r"\subsection{Application aux changements de base dans les préschémas algébriques.}", P145)
add(p, "Proposition (6.7.1), label (i) (printed on p. 145)", "label (i) upright", "\\item[(i)] in the italic statement",
    "convention", 6, "high", r"\item[(i)] On a", r"\item[\textup{(i)}] On a", P145)
add(p, "Proposition (6.7.1) (i): 'O_x-module de Cohen-Macaulay' (printed on p. 145)", "hyphen", "Cohen--Macaulay",
    "punctuation", None, "high", r"$\mathcal O_x$-module de Cohen--Macaulay", r"$\mathcal O_x$-module de Cohen-Macaulay",
    P145)
add(p, "Proposition (6.7.1) (i), end: 'O_{x'}-module de Cohen-Macaulay' (printed on p. 145)", "hyphen",
    "Cohen--Macaulay", "punctuation", None, "high", r"$\mathcal O_{x'}$-module de Cohen--Macaulay",
    r"$\mathcal O_{x'}$-module de Cohen-Macaulay", P145)
add(p, "Proposition (6.7.1), label (ii) (printed on p. 145)", "label (ii) upright", "\\item[(ii)] in the italic statement",
    "convention", 6, "high", r"\item[(ii)] Pour que", r"\item[\textup{(ii)}] Pour que", P145)
add(p, "proof of (6.7.1), l. 3: 'Spec(k(x)⊗_k k')'", "bold italic k", "k(x)", "convention", 1, "high",
    r"\operatorname{Spec}(k(x)\otimes_k k')", r"\operatorname{Spec}(\boldsymbol{k}(x)\otimes_k k')")
add(p, "proof of (6.7.1), l. 3: 'est un préschéma de Cohen-Macaulay;'", "'préschéma de Cohen-Macaulay' italic",
    "roman", "italics", None, "high", r"est un<NL>préschéma de Cohen--Macaulay; comme",
    r"est un<NL>\emph{préschéma de Cohen--Macaulay}; comme", "Apply before the next entry.")
add(p, "proof of (6.7.1), l. 3: 'préschéma de Cohen-Macaulay'", "hyphen", "Cohen--Macaulay", "punctuation", None,
    "high", r"préschéma de Cohen--Macaulay", r"préschéma de Cohen-Macaulay", DASH)
add(p, "proof of (6.7.1), l. 4: 'corps k(x), k''", "bold italic k", "k(x)", "convention", 1, "high",
    r"corps $k(x)$, $k'$", r"corps $\boldsymbol{k}(x)$, $k'$")
add(p, "proof of (6.7.1), l. 4: 'par hypothèse on est ramené'", "no comma", "'par hypothèse, on est ramené'",
    "punctuation", None, "high", r"par hypothèse, on est ramené", r"par hypothèse on est ramené")
add(p, "proof of (6.7.1), end: 'on est ramené à prouver le' + 'Lemme (6.7.1.1). —'",
    "the sentence ends with 'le' and runs into the lemma heading", "'à prouver le lemme suivant.'", "extra", None,
    "high", r"à prouver<NL>le lemme suivant.", r"à prouver<NL>le",
    "The lemma environment supplies the printed heading 'Lemme (6.7.1.1). —'.")
add(p, "Lemme (6.7.1.1), end: 'anneau de Cohen-Macaulay.'", "hyphen", "Cohen--Macaulay", "punctuation", None, "high",
    r"Cohen--Macaulay.<NL>\end{lemma}", r"Cohen-Macaulay.<NL>\end{lemma}", DASH)
add(p, "proof of (6.7.1.1), l. 2: 'de sorte que L est extension finie'", "'est'", "'soit'", "word", None, "high",
    r"de sorte que $L$ soit extension finie", r"de sorte que $L$ est extension finie")
add(p, "proof of (6.7.1.1), l. 2: 'extension pure k(t)'", "bold upright t", "\\boldsymbol t (bold italic)", "font",
    None, "high", r"pure $k(\boldsymbol t)$", r"pure $k(\mathbf t)$", BOLDT)
add(p, "proof of (6.7.1.1), l. 2: '(t étant un système'", "bold upright t", "\\boldsymbol t", "font", None, "high",
    r"($\boldsymbol t$ étant", r"($\mathbf t$ étant", BOLDT)
add(p, "proof of (6.7.1.1), l. 3: 'Si on pose'", "'Si on pose'", "'Si l'on pose'", "word", None, "high",
    r"Si l'on pose", r"Si on pose")
add(p, "proof of (6.7.1.1), l. 3: 'A=K⊗_k k(t)'", "bold upright t", "\\boldsymbol t", "font", None, "high",
    r"\otimes_k k(\boldsymbol t)$", r"\otimes_k k(\mathbf t)$", BOLDT)
add(p, "proof of (6.7.1.1), l. 3: 'A-module plat (0_I, 6.2.1)'", "'(0_I, 6.2.1)' with bold 0 and subscript I",
    "'(0.6.2.1)'", "number", None, "high", r"(0.6.2.1)", r"$(\mathbf{0}_{\mathrm I},6.2.1)$",
    "House form $(0_{\\mathrm I},...)$ with the convention-2 bold 0 included. The five '(0.' references of "
    "ega4-2-fr.tex are all on pp. 146-147.")
add(p, "proof of (6.7.1.1): 'tout préschéma artinien est de Cohen-Macaulay'", "hyphen", "Cohen--Macaulay",
    "punctuation", None, "high", r"artinien est de Cohen--Macaulay", r"artinien est de Cohen-Macaulay", DASH)
add(p, "proof of (6.7.1.1): 'que B est un anneau de Cohen-Macaulay'", "hyphen", "Cohen--Macaulay", "punctuation",
    None, "high", r"$B$ est un anneau de Cohen--Macaulay", r"$B$ est un anneau de Cohen-Macaulay", DASH)
add(p, "proof of (6.7.1.1): 'A est un anneau de Cohen-Macaulay (6.3.5)'", "hyphen", "Cohen--Macaulay",
    "punctuation", None, "high", r"$A$ est un anneau de Cohen--Macaulay (6.3.5)",
    r"$A$ est un anneau de Cohen-Macaulay (6.3.5)", DASH)
add(p, "proof of (6.7.1.1): 'l'ensemble des éléments ≠0 de k[t]'", "'≠0' (formula)", "'non nuls'", "word", None,
    "high", r"éléments non nuls de", r"éléments $\neq 0$ de")
add(p, "proof of (6.7.1.1): 'de k[t], on a'", "bold upright t", "\\boldsymbol t", "font", None, "high",
    r"de $k[\boldsymbol t]$, on a", r"de $k[\mathbf t]$, on a", BOLDT)
add(p, "proof of (6.7.1.1): 'A'=K⊗_k k[t]=K[t]' (two occurrences)", "bold upright t", "\\boldsymbol t", "font", None,
    "high", r"k[\boldsymbol t]=K[\boldsymbol t]", r"k[\mathbf t]=K[\mathbf t]", BOLDT)
add(p, "proof of (6.7.1.1): 'en vertu de (0, 16.5.13)'", "'(0, 16.5.13)' with bold 0", "'(0.16.5.13)'", "number",
    None, "high", r"(0.16.5.13)", r"(\textbf{0}, 16.5.13)", "Includes the convention-2 bold 0.")
add(p, "proof of (6.7.1.1): 'anneau de Cohen-Macaulay; mais'", "hyphen", "Cohen--Macaulay", "punctuation", None,
    "high", r"Cohen--Macaulay; mais", r"Cohen-Macaulay; mais", DASH)
add(p, "proof of (6.7.1.1), end: 'A' est régulier'", "'régulier' italic", "roman", "italics", None, "high",
    r"ce que $A'$ est régulier", r"ce que $A'$ est \emph{régulier}")
add(p, "proof of (6.7.1.1), end: '(0, 17.3.7)'", "'(0, 17.3.7)' with bold 0", "'(0.17.3.7)'", "number", None, "high",
    r"(0.17.3.7)", r"(\textbf{0}, 17.3.7)", "Includes the convention-2 bold 0.")
add(p, "Corollaire (6.7.2), l. 1: 'O_x soit un anneau de Cohen-Macaulay'", "hyphen", "Cohen--Macaulay",
    "punctuation", None, "high", r"$\mathcal O_x$ soit un anneau de Cohen--Macaulay",
    r"$\mathcal O_x$ soit un anneau de Cohen-Macaulay", DASH)
add(p, "Corollaire (6.7.2), l. 1: '(resp. pour que X'", "'(resp.' upright", "italic", "convention", 6, "high",
    r"(resp. pour<NL>que $X$", r"\textup{(resp.} pour<NL>que $X$")
add(p, "Corollaire (6.7.2), l. 2: 'vérifie (S_n) au point x)'", "'vérifie (S_n) au point x)' (no 'la propriété')",
    "'vérifie la propriété $(S_n)$ au point $x$)'", "extra", None, "high",
    r"vérifie la propriété $(S_n)$ au point $x$)", r"vérifie $(S_n)$ au point $x$)", "Apply before the next entry.")
add(p, "Corollaire (6.7.2), l. 2: '(S_n) au point x)'", "the subscript n is a bold italic n (wrong fount; enlarged crop and ink measure: arch filled, unlike the light n of (S_n) in (6.6.1) b) and (6.7.3))",
    "light italic n: the TeX silently corrects", "misprint_in_print", None, "high",
    r"$(S_n)$ au point $x$)", r"$(S_{\boldsymbol{n}})$ au point $x$)",
    "Wrong-fount letter reproduced in the diplomatic text (GLOBAL_ISSUES 29). Its old string is the same before and "
    "after the 'la propriété' entry above.", corrected="$(S_n)$ au point $x$)")
add(p, "Corollaire (6.7.2), l. 2 (line 18 of p. 146): 'il suffit que O'_{x'} soit'",
    "script O with a prime: O'_{x'} (enlarged crop)", "$\\mathcal O_{x'}$: the TeX silently applies the errata",
    "misprint_in_print", None, "high", r"$\mathcal O_{x'}$ soit un anneau", r"$\mathcal O'_{x'}$ soit un anneau",
    "Authors' errata, EGA IV liste 3, (IV, 6.7.2): 'Ligne 18 de la p. 146, remplacer O'_{x'} par O_{x'}'.",
    corrected=r"$\mathcal O_{x'}$ soit un anneau")
add(p, "Corollaire (6.7.2), l. 2: 'anneau de Cohen-Macaulay (resp. que X''", "hyphen", "Cohen--Macaulay",
    "punctuation", None, "high", r"Cohen--Macaulay (resp. que", r"Cohen-Macaulay (resp. que",
    DASH + " Apply before the next entry.")
add(p, "Corollaire (6.7.2), l. 2: '(resp. que X''", "'(resp.' upright", "italic", "convention", 6, "high",
    r"(resp. que $X'$", r"\textup{(resp.} que $X'$")
add(p, "Corollaire (6.7.2), l. 3: '(S_n) au point x')'", "bold italic n (wrong fount), as two lines above",
    "light italic n: the TeX silently corrects", "misprint_in_print", None, "high",
    r"$(S_n)$ au point $x'$)", r"$(S_{\boldsymbol{n}})$ au point $x'$)",
    "Wrong-fount letter reproduced in the diplomatic text (GLOBAL_ISSUES 29).", corrected="$(S_n)$ au point $x'$)")
add(p, "Corollaire (6.7.3): 'Soit F (resp. G)'", "'(resp.' upright", "italic", "convention", 6, "high",
    r"(resp.<NL>$\mathscr G$)", r"\textup{(resp.}<NL>$\mathscr G$)")
add(p, "Corollaire (6.7.3): '(resp. un O_Y-Module cohérent)'", "'(resp.' upright", "italic", "convention", 6,
    "high", r"(resp. un<NL>$\mathcal O_Y$", r"\textup{(resp.} un<NL>$\mathcal O_Y$")
add(p, "proof of (6.7.3), l. 2: 'q : X×_kY→Y'", "the subscript k is a bold italic k (wrong fount; enlarged crop: "
    "filled bowl, unlike the light k of the two X×_kY on the line above)",
    "light k: the TeX silently corrects", "misprint_in_print", None, "medium",
    r"$q:X\times_kY\to Y$", r"$q:X\times_{\boldsymbol k}Y\to Y$",
    "Wrong-fount letter reproduced in the diplomatic text (GLOBAL_ISSUES 29).", corrected=r"$q:X\times_kY\to Y$")
add(p, "proof of (6.7.3), l. 3: 'Supposons par exemple que'", "no commas", "'Supposons, par exemple, que'",
    "punctuation", None, "high", r"Supposons, par exemple, que", r"Supposons par exemple que")
add(p, "proof of (6.7.3): 'F⊗_kG=p^*(F)⊗_kG et puisque'", "no comma before 'et puisque'", "comma after the formula",
    "punctuation", None, "high", r"\otimes_k\mathscr G$,<NL>et puisque", r"\otimes_k\mathscr G$<NL>et puisque")
add(p, "proof of (6.7.3): 'il suffit de voir que pour tout y∈Y'", "no comma after 'que'", "'que, pour tout'",
    "punctuation", None, "high", r"voir<NL>que, pour tout $y\in Y$", r"voir<NL>que pour tout $y\in Y$")
add(p, "proof of (6.7.3): 'p^*(F)⊗_{O_Y}k(y) a la propriété'", "bold italic k", "k(y)", "convention", 1, "high",
    r"\otimes_{\mathcal O_Y}k(y)$<NL>a la propriété", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)$<NL>a la propriété")
add(p, "proof of (6.7.3): 'mais p^*(F)⊗_{O_Y}k(y)='", "bold italic k", "k(y)", "convention", 1, "high",
    r"\otimes_{\mathcal O_Y}k(y)=", r"\otimes_{\mathcal O_Y}\boldsymbol{k}(y)=")
add(p, "proof of (6.7.3): '=F⊗_k k(y)'", "bold italic k", "k(y)", "convention", 1, "high",
    r"\mathscr F\otimes_k k(y)$", r"\mathscr F\otimes_k \boldsymbol{k}(y)$")
add(p, "Proposition (6.7.4), l. 2: 'soit P(Z, z)'", "bold italic P", "$P$", "font", None, "high",
    r"soit $P(Z,z)$", r"soit $\boldsymbol{P}(Z,z)$", BOLDP)
for L in "abcd":
    add(p, f"Proposition (6.7.4), label {L})", f"upright label '{L})' with no opening parenthesis",
        f"\\item[({L})]", "punctuation", None, "high", f"\\item[({L})]", f"\\item[\\textup{{{L})}}]")
add(p, "Proposition (6.7.4): 'avec les notations de (6.7.1)'", "reference upright", "italic in the statement",
    "convention", 6, "high", r"notations de (6.7.1), si", r"notations de \textup{(6.7.1)}, si")
add(p, "Proposition (6.7.4): 'si P(X', x') est vraie'", "bold italic P", "$P$", "font", None, "high",
    r"$P(X',x')$", r"$\boldsymbol{P}(X',x')$", BOLDP)
add(p, "Proposition (6.7.4): 'de même de P(X, x)'", "bold italic P", "$P$", "font", None, "high",
    r"$P(X,x)$", r"$\boldsymbol{P}(X,x)$", BOLDP)
add(p, "proof of (6.7.4), l. 1: 'Le cas où P est'", "bold italic P", "$P$", "font", None, "high",
    r"Le cas où $P$ est", r"Le cas où $\boldsymbol{P}$ est", BOLDP)
add(p, "proof of (6.7.4), l. 1: 'la propriété d)'", "italic 'd)' without an opening parenthesis", "upright '(d)'",
    "punctuation", None, "high", r"la propriété (d) n'a", r"la propriété \emph{d)} n'a")
add(p, "proof of (6.7.4), l. 2: 'ayant déjà été traité (2.1.13 et 4.6.1)'", "no 'dans'", "'traité dans (2.1.13'",
    "extra", None, "high", r"traité dans (2.1.13", r"traité (2.1.13")
add(p, "proof of (6.7.4), l. 2: 'Le même raisonnement qu'au début de (6.7.1)'", "'qu'au début de (6.7.1)'",
    "'qu'au début de la démonstration de (6.7.1)'", "extra", None, "high",
    r"qu'au début<NL>de la démonstration de (6.7.1)", r"qu'au début<NL>de (6.7.1)")
add(p, "proof of (6.7.4), last line: 'la seconde assertion résultera de'", "'résultera'", "'résulte'", "word", None,
    "high", r"la seconde assertion résulte de", r"la seconde assertion résultera de")
add(p, "page break 146/147 (edit 1 of 2): blank line before \\oldpage[IV-2]{147}",
    "the sentence runs on: p. 146 ends '(6.5.4, (ii))', p. 147 begins 'pourvu que' flush left",
    "blank lines around \\oldpage[IV-2]{147}: paragraph break", "other", None, "high",
    r"(6.5.4, (ii)),<NL><NL>", r"(6.5.4, (ii)),<NL>",
    "GLOBAL_ISSUES 20. Apply together with the first p. 147 entry (blank line after the marker); apply before the next entry.")
add(p, "page break 146/147: '(6.5.4, (ii))' at the end of p. 146", "no comma after '(6.5.4, (ii))'",
    "'(6.5.4, (ii)),'", "punctuation", None, "high", r"et<NL>(6.5.4, (ii)),", r"et<NL>(6.5.4, (ii))")
add(p, "page start: marker position (edit 1 of 2, insert)",
    "printed p. 146 begins 'On sait que p est fidèlement plat (2.2.13)'; the heading 6.7 and the whole statement of "
    "(6.7.1) are on p. 145 (page_145_s3/s4)",
    "\\oldpage[IV-2]{146} stands before \\subsection{Application ...}", "marker", None, "high",
    r"\end{proposition}<NL><NL>\begin{proof}<NL>On sait que $p$",
    r"\end{proposition}<NL><NL>\oldpage[IV-2]{146}<NL><NL>\begin{proof}<NL>On sait que $p$",
    "Apply after every other p. 146 entry, together with the next edit.")
add(p, "page start: marker position (edit 2 of 2, remove the misplaced marker)", "see the previous entry",
    "\\oldpage[IV-2]{146} directly before \\subsection{Application", "marker", None, "high",
    r"\oldpage[IV-2]{146}<NL><NL>\subsection{Application", r"\subsection{Application",
    "Apply together with, and after, the previous edit. Afterwards heading 6.7 and (6.7.1) belong to p. 145.")

# ---------------------------------------------------------------- page 147 (segment ends with text printed on p. 148)
p = 147
P148 = "Printed on p. 148; this text lies in the p. 147 segment until the marker move at the end of this page's list."
add(p, "page break 146/147 (edit 2 of 2): blank line after \\oldpage[IV-2]{147}", "p. 147 begins 'pourvu que' flush left (same sentence)",
    "blank line after the marker", "other", None, "high",
    r"\oldpage[IV-2]{147}<NL><NL>pourvu que", r"\oldpage[IV-2]{147}<NL>pourvu que",
    "Apply together with the p. 146 entry that removes the blank line before the marker.")
add(p, "l. 1: 'est un préschéma régulier;'", "'préschéma régulier' italic", "roman", "italics", None, "high",
    r"est un préschéma régulier; autrement", r"est un \emph{préschéma régulier}; autrement")
add(p, "l. 2: 'on est ramené à prouver le' + 'Lemme (6.7.4.1). —'", "the sentence ends with 'le' and runs into the lemma heading",
    "'à prouver le lemme suivant.'", "extra", None, "high", r"à prouver le lemme suivant.", r"à prouver le",
    "The lemma environment supplies the printed heading 'Lemme (6.7.4.1). —'.")
add(p, "proof of (6.7.4.1), l. 1: 'Distinguons deux cas :'", "colon", "full stop", "punctuation", None, "high",
    r"Distinguons deux cas.", r"Distinguons deux cas:")
add(p, "proof of (6.7.4.1) A): 'extension de type fini de k'", "'de type fini' italic", "roman", "italics", None,
    "high", r"est une extension de type fini de $k$. Alors", r"est une extension \emph{de type fini} de $k$. Alors")
add(p, "proof of (6.7.4.1) A): 'extension finie séparable de k(t)'", "'finie séparable' italic", "roman", "italics",
    None, "high", r"une extension finie<NL>séparable de", r"une extension \emph{finie<NL>séparable} de")
add(p, "proof of (6.7.4.1) A): 'de k(t). Pour tout'", "bold upright t", "\\boldsymbol t", "font", None, "high",
    r"de $k(\boldsymbol t)$. Pour tout", r"de $k(\mathbf t)$. Pour tout", BOLDT)
add(p, "proof of (6.7.4.1) A): 'k(s)⊗_{k(t)} L'", "bold italic k in k(s)", "k(s)", "convention", 1, "high",
    r"$k(s)\otimes", r"$\boldsymbol{k}(s)\otimes", "The k of the subscript k(t) is light (enlarged crop).")
add(p, "proof of (6.7.4.1) A): subscript k(t) of ⊗", "bold upright t", "\\boldsymbol t", "font", None, "high",
    r"_{k(\boldsymbol t)}L", r"_{k(\mathbf t)}L", BOLDT)
add(p, "proof of (6.7.4.1) A): 'est alors composé direct'", "no 'un'", "'est alors un composé direct'", "extra",
    None, "high", r"est alors un composé direct", r"est alors composé direct")
add(p, "proof of (6.7.4.1) A): 'séparables de k(s), donc'", "bold italic k", "k(s)", "convention", 1, "high",
    r"séparables de $k(s)$, donc", r"séparables de $\boldsymbol{k}(s)$, donc")
add(p, "proof of (6.7.4.1) A): 'donc un anneau régulier;'", "'régulier' italic", "roman", "italics", None, "high",
    r"donc un anneau<NL>régulier; il résulte", r"donc un anneau<NL>\emph{régulier}; il résulte")
add(p, "proof of (6.7.4.1) A): 'l'anneau A est régulier; comme A=S^{-1}A''", "semicolon, lower-case 'comme'",
    "'régulier. Comme'", "punctuation", None, "high", r"l'anneau $A$ est régulier. Comme $A=S^{-1}A'$",
    r"l'anneau $A$ est régulier; comme $A=S^{-1}A'$")
add(p, "proof of (6.7.4.1) A): '(0, 17.3.6)'", "'(0, 17.3.6)' with bold 0", "'(0.17.3.6)'", "number", None, "high",
    r"(0.17.3.6)", r"(\textbf{0}, 17.3.6)", "Includes the convention-2 bold 0.")
add(p, "proof of (6.7.4.1) A): '(0, 17.3.6), mais on a vu'", "comma before 'mais'", "semicolon", "punctuation", None,
    "high", r"); mais on a vu", r"), mais on a vu")
add(p, "proof of (6.7.4.1) B): 'd'autre part, pour L_λ⊂L_μ'", "'pour'", "'si'", "word", None, "high",
    r"d'autre part, si<NL>$L_\lambda", r"d'autre part, pour<NL>$L_\lambda")
add(p, "proof of (6.7.4.1) B): 'C_λ-module plat (0_I, 6.2.1)'", "'(0_I, 6.2.1)' with bold 0 and subscript I",
    "'(0.6.2.1)'", "number", None, "high", r"(0.6.2.1)", r"$(\mathbf{0}_{\mathrm I},6.2.1)$",
    "House form $(0_{\\mathrm I},...)$ with the convention-2 bold 0 included.")
add(p, "Remarques (6.7.5) (i), l. 1: 'P(X, x) entraîne'", "bold italic P", "$P$", "font", None, "high",
    r"fait que $P(X,x)$ entraîne", r"fait que $\boldsymbol{P}(X,x)$ entraîne", BOLDP)
add(p, "Remarques (6.7.5) (i), l. 2: 'P(X', x'), on ne peut'", "bold italic P", "$P$", "font", None, "high",
    r"$P(X',x')$, on ne peut", r"$\boldsymbol{P}(X',x')$, on ne peut", BOLDP)
add(p, "Remarques (6.7.5) (i), l. 2: 'une extension séparable de k'", "'séparable' italic", "roman", "italics", None,
    "high", r"une<NL>extension séparable de $k$. On", r"une<NL>extension \emph{séparable} de $k$. On", REMARK)
add(p, "Remarques (6.7.5) (i), l. 3: 'lorsque P est la propriété'", "bold italic P", "$P$", "font", None, "high",
    r"lorsque $P$ est la", r"lorsque $\boldsymbol{P}$ est la", BOLDP)
add(p, "Remarques (6.7.5) (i), l. 3: 'la propriété d);'", "italic 'd)' without an opening parenthesis",
    "'(d)'", "punctuation", None, "high", r"propriété (d); mais", r"propriété \emph{d)}; mais", REMARK)
add(p, "Remarques (6.7.5) (i): 'X est géométriquement intègre (4.6.2)'", "'géométriquement intègre' italic", "roman",
    "italics", None, "high", r"est géométriquement intègre (4.6.2)", r"est \emph{géométriquement intègre} (4.6.2)", REMARK)
add(p, "Remarques (6.7.5) (i): 'X soit régulier sans que'", "'régulier' italic", "roman", "italics", None, "high",
    r"soit régulier sans que", r"soit \emph{régulier} sans que", REMARK)
add(p, "Remarques (6.7.5) (i): 'X' soit normal.'", "'normal' italic", "roman", "italics", None, "high",
    r"$X'$ soit normal.", r"$X'$ soit \emph{normal}.", REMARK)
add(p, "Remarques (6.7.5) (i), 2nd paragraph: '(II, 7.4.2)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 7.4.2)", r"(\textbf{II}, 7.4.2)")
add(p, "Remarques (6.7.5) (i): 'de dimension 1 sont des anneaux de valuation discrète'", "no ', ce'",
    "'dimension $1$, ce sont des'", "extra", None, "high", r"dimension $1$, ce sont des", r"dimension $1$ sont des")
add(p, "Remarques (6.7.5) (i): '(II, 7.1.6)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 7.1.6)", r"(\textbf{II}, 7.1.6)")
add(p, "Remarques (6.7.5) (i): '(et a fortiori vérifie (R_n)'", "'a fortiori' italic", "roman", "italics", None,
    "high", r"(et a fortiori<NL>vérifie", r"(et \emph{a fortiori}<NL>vérifie", REMARK)
add(p, "Remarques (6.7.5) (i): '(4.6.3). Or, prenons'", "'Or, prenons' continues the same paragraph (same line)",
    "blank line before 'Or, prenons': new paragraph", "other", None, "high",
    r"(4.6.3).<NL><NL>Or, prenons", r"(4.6.3).<NL>Or, prenons")
add(p, "Remarques (6.7.5) (i): 'Soit B l'anneau de polynômes k[S, T] en deux indéterminées'",
    "'Soit B l'anneau de polynômes k[S, T] en deux'", "'Soit $B=k[S,T]$ l'anneau de polynômes en deux'", "word",
    None, "high", r"Soit<NL>$B=k[S,T]$ l'anneau de polynômes en deux", r"Soit<NL>$B$ l'anneau de polynômes $k[S,T]$ en deux")
add(p, "Remarques (6.7.5) (i): 'le polynôme P(S, T)=T^2—S^p+a est irréductible'", "formula in the running text",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"polynôme<NL>\[<NL>P(S,T)=T^2-S^p+a<NL>\]<NL>est irréductible", r"polynôme $P(S,T)=T^2-S^p+a$<NL>est irréductible",
    "Display vs inline. Apply before the next entry.")
add(p, "Remarques (6.7.5) (i): 'T^2—S^p+a'", "long dash", "minus sign", "convention", 7, "high",
    r"T^2-S^p+a", r"T^2\setmin S^p+a", "Long dash used for subtraction (GLOBAL_ISSUES 23); \\setmin pending the global pass.")
add(p, "Remarques (6.7.5) (i): 'S^p—a n'est pas un carré'", "long dash", "minus sign", "convention", 7, "high",
    r"$S^p-a$ n'est pas", r"$S^p\setmin a$ n'est pas")
add(p, "Remarques (6.7.5) (i): 'un carré dans l'anneau k[S]'", "'dans l'anneau k[S]'", "'dans $k[S]$'", "missing",
    None, "high", r"un carré dans $k[S]$; donc", r"un carré dans l'anneau $k[S]$; donc")
add(p, "Remarques (6.7.5) (i): 'qu'il est normal (II, 7.4.5)'", "'normal' italic", "roman", "italics", None, "high",
    r"qu'il est normal (", r"qu'il est \emph{normal} (", REMARK)
add(p, "Remarques (6.7.5) (i): '(II, 7.4.5)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 7.4.5)", r"(\textbf{II}, 7.4.5)")
add(p, "Remarques (6.7.5) (i): 'donc séparable sur k(S)'", "'séparable' italic", "roman", "italics", None, "high",
    r"donc séparable sur $k(S)$", r"donc \emph{séparable} sur $k(S)$", REMARK)
add(p, "Remarques (6.7.5) (i): 'et a fortiori sur k'", "'a fortiori' italic", "roman", "italics", None, "high",
    r"et a fortiori<NL>sur $k$", r"et \emph{a fortiori}<NL>sur $k$", REMARK)
add(p, "Remarques (6.7.5) (i): 'ce qui montre que X est régulier.'", "'régulier' italic", "roman", "italics", None,
    "high", r"que $X$ est régulier. Par ailleurs", r"que $X$ est \emph{régulier}. Par ailleurs", REMARK)
add(p, "Remarques (6.7.5) (i): '(avec f, g dans k(S))'", "'f, g dans k(S)' in words", "'$f,g\\in k(S)$'", "word",
    None, "high", r"(avec $f,g\in k(S)$)", r"(avec $f$, $g$ dans $k(S)$)")
add(p, "Remarques (6.7.5) (i): 'f∈k et g=0, autrement dit'", "'g=0, autrement' (space after the comma)",
    "'$g=0,<NL>$autrement': the comma is inside the formula and no space is typeset before 'autrement'", "other",
    None, "high", r"$g=0,<NL>$autrement dit", r"$g=0$,<NL>autrement dit")
add(p, "Remarques (6.7.5) (i): 'k est algébriquement fermé dans K'", "'algébriquement fermé' italic", "roman",
    "italics", None, "high", r"est algébriquement fermé dans $K$, et", r"est \emph{algébriquement fermé} dans $K$, et",
    REMARK)
add(p, "Remarques (6.7.5) (i): 'et a fortiori K est une extension'", "'a fortiori' italic", "roman", "italics", None,
    "high", r"et a fortiori $K$<NL>est une", r"et \emph{a fortiori} $K$<NL>est une", REMARK)
add(p, "Remarques (6.7.5) (i), last word of p. 147: 'extension primaire'", "'primaire' italic", "roman", "italics",
    None, "high", r"extension primaire de $k$", r"extension \emph{primaire} de $k$", REMARK)
add(p, "top of p. 148: 'on peut écrire S^p—a=(S—a^{1/p})^p' (first dash)", "long dash", "minus sign", "convention",
    7, "high", r"$S^p-a=", r"$S^p\setmin a=", P148)
add(p, "top of p. 148: '(S—a^{1/p})^p' (second dash)", "long dash", "minus sign", "convention", 7, "high",
    r"(S-a^{1/p})", r"(S\setmin a^{1/p})", P148)
add(p, "top of p. 148: 'où A'=k'[S][t'], t' étant racine du polynôme'", "', t' étant racine'",
    "'et $t'$ est racine'", "word", None, "high", r"où $A'=k'[S][t']$ et $t'$ est racine du<NL>polynôme",
    r"où $A'=k'[S][t']$, $t'$ étant racine du<NL>polynôme", P148)
add(p, "top of p. 148: 'polynôme T^2—S^p.'", "long dash", "minus sign", "convention", 7, "high",
    r"polynôme $T^2-S^p$.", r"polynôme $T^2\setmin S^p$.", P148)
add(p, "top of p. 148: 'n'est pas intégralement clos, car l'élément'", "', car'", "':'", "word", None, "high",
    r"intégralement clos: l'élément", r"intégralement clos, car l'élément", P148)
add(p, "top of p. 148: 'intégrale t''^2—S^{p-2}=0'", "t''^2 without parentheses", "$(t'')^2$", "formula", None,
    "high", r"$(t'')^2-S^{p-2}=0$", r"$t''^2-S^{p-2}=0$", P148 + " Apply before the next entry.")
add(p, "top of p. 148: 't''^2—S^{p-2}=0'", "long dash before S^{p-2}", "minus sign", "convention", 7, "high",
    r"-S^{p-2}=0", r"\setmin S^{p-2}=0", P148 + " The minus inside the exponent p-2 is short.")
add(p, "top of p. 148: 'sur A' et n'appartient pas à A''", "' et'", "', mais'", "word", None, "high",
    r"sur $A'$, mais<NL>n'appartient", r"sur $A'$ et<NL>n'appartient", P148)
add(p, "top of p. 148: 'le « genre » sur k''", "'genre' italic", "roman", "italics", None, "high",
    r"le «genre» sur", r"le «\emph{genre}» sur", P148 + " " + REMARK)
add(p, "top of p. 148: 'est strictement inférieur à celui de K'", "'strictement inférieur' italic", "roman",
    "italics", None, "high", r"est strictement inférieur à", r"est \emph{strictement inférieur} à",
    P148 + " " + REMARK)
add(p, "page start p. 148: marker position (edit 1 of 2, insert)",
    "printed p. 147 ends '... K est une extension primaire'; p. 148 begins 'de k (4.3.1). Cependant, si k'=k(a^{1/p})'",
    "\\oldpage[IV-2]{148} stands before '\\item[(ii)] Comme on l'a rappelé' (nine printed lines too late)",
    "marker", None, "high", r" de $k$ (4.3.1). Cependant", r"<NL>\oldpage[IV-2]{148}<NL>de $k$ (4.3.1). Cependant",
    "Filed under p. 147 because the insertion point lies in the current p. 147 segment. Inserts the marker "
    "mid-sentence on its own line. Apply after every other p. 147 entry, together with the first p. 148 entry "
    "(removal of the old marker).")

# ---------------------------------------------------------------- page 148
p = 148
add(p, "page start p. 148: marker position (edit 2 of 2, remove the misplaced marker)",
    "see the last p. 147 entry", "\\oldpage[IV-2]{148} directly before '\\item[(ii)] Comme'", "marker", None, "high",
    r"\oldpage[IV-2]{148}<NL><NL>\item[(ii)] Comme", r"\item[(ii)] Comme",
    "Apply together with, and after, the p. 147 insertion. Afterwards 'de k (4.3.1). Cependant ... sur k.' belongs to p. 148.")
add(p, "Remarques (6.7.5) (ii), l. 1: 'Comme on l'a rappelé dans (i)'", "'dans (i)'", "'en (i)'", "word", None,
    "high", r"rappelé en (i)", r"rappelé dans (i)")
add(p, "Remarques (6.7.5) (ii), l. 1: 'il résulte de (4.6.1) que lorsque X'", "no comma after 'que'", "'que,'",
    "punctuation", None, "high", r"de (4.6.1) que,<NL>lorsque", r"de (4.6.1) que<NL>lorsque")
add(p, "Remarques (6.7.5) (ii): 'un schéma régulier sur k'", "'régulier' italic", "roman", "italics", None, "high",
    r"un schéma régulier sur $k$", r"un schéma \emph{régulier} sur $k$", REMARK)
add(p, "Remarques (6.7.5) (ii): 'tel que k soit algébriquement fermé dans le corps K'", "'algébriquement fermé' italic",
    "roman", "italics", None, "high", r"soit algébriquement fermé dans le corps",
    r"soit \emph{algébriquement fermé} dans le corps", REMARK)
add(p, "Remarques (6.7.5) (ii): 'Soient k un corps de caractéristique p>0'", "'Soient'", "'Soit'", "word", None,
    "high", r"Soit $k$ un corps de caractéristique", r"Soient $k$ un corps de caractéristique",
    "Cf. GLOBAL_ISSUES 73 ('Soit' for 'Soient' in ega4-2).")
add(p, "Remarques (6.7.5) (ii): 'P(S, T)=T^p—aS^p—b' (first dash)", "long dash", "minus sign", "convention", 7,
    "high", r"T^p-aS^p", r"T^p\setmin aS^p")
add(p, "Remarques (6.7.5) (ii): 'P(S, T)=T^p—aS^p—b' (second dash)", "long dash", "minus sign", "convention", 7,
    "high", r"aS^p-b$", r"aS^p\setmin b$")
add(p, "Remarques (6.7.5) (ii): 'n'est pas une puissance p-ème dans k(S)'", "'p-ème'", "'$p$-ième'", "word", None,
    "high", r"$p$-ième dans $k(S)$", r"$p$-ème dans $k(S)$", "Printed 'p-ème' both times on this page.")
add(p, "Remarques (6.7.5) (ii): 'courbe affine intègre sur k'", "'intègre' italic", "roman", "italics", None, "high",
    r"affine<NL>intègre sur $k$", r"affine<NL>\emph{intègre} sur $k$", REMARK)
add(p, "Remarques (6.7.5) (ii): 'montrons que k est algébriquement fermé dans K'", "'algébriquement fermé' italic",
    "roman", "italics", None, "high", r"est<NL>algébriquement fermé dans $K$. Supposons",
    r"est<NL>\emph{algébriquement fermé} dans $K$. Supposons", REMARK)
add(p, "Remarques (6.7.5) (ii): 'comme [K : k(S)]=p, on aurait K=k(S)[z], et comme K est radiciel sur k(S), on aurait z^p∈k(S)'",
    "'on aurait K=k(S)[z], et comme K est radiciel sur k(S), on aurait z^p∈k(S)'",
    "'on aurait<NL>$z^p\\in k(S)$': the clause 'K=k(S)[z], et comme K est radiciel sur k(S), on aurait' is missing",
    "missing", None, "high", r"$[K:k(S)]=p$, on aurait<NL>$z^p\in k(S)$",
    r"$[K:k(S)]=p$, on aurait $K=k(S)[z]$, et comme $K$ est radiciel sur $k(S)$, on aurait<NL>$z^p\in k(S)$")
add(p, "Remarques (6.7.5) (ii): 't^p=aS^p+b∈k^p(S^p)(c) donc a et b'", "no comma before 'donc'", "'(c)$, donc'",
    "punctuation", None, "high", r"(c)$, donc $a$", r"(c)$ donc $a$")
add(p, "Remarques (6.7.5) (ii): 'la normalisée de la courbe'", "'normalisée' italic", "roman", "italics", None, "high",
    r"la<NL>normalisée de", r"la<NL>\emph{normalisée} de", REMARK)
add(p, "Remarques (6.7.5) (ii): '(et par suite régulière)'", "'régulière' italic", "roman", "italics", None, "high",
    r"(et par suite régulière)", r"(et par suite \emph{régulière})", REMARK)
add(p, "Remarques (6.7.5) (ii): 'est une puissance p-ème dans k'(S)'", "'p-ème'", "'$p$-ième'", "word", None, "high",
    r"$p$-ième dans $k'(S)$", r"$p$-ème dans $k'(S)$")
add(p, "Remarques (6.7.5) (ii), end: 'K⊗_k k' n'est pas réduit'", "'n'est pas réduit' italic", "roman", "italics",
    None, "high", r"n'est pas réduit, ni", r"\emph{n'est pas réduit}, ni", REMARK)
add(p, "Remarques (6.7.5) (ii), end: 'ni a fortiori le schéma'", "'a fortiori' italic", "roman", "italics", None,
    "high", r"ni a fortiori le", r"ni \emph{a fortiori} le", REMARK)
add(p, "Définition (6.7.6), first sentence: the defined terms",
    "'géométriquement régulier en un point x (resp. possède la propriété (R_n) géométrique en un point x, resp. est "
    "géométriquement normal en un point x)' upright; 'que X est' and 'si, pour toute' italic",
    "all italic", "convention", 6, "high",
    r"est géométriquement régulier en un point $x$ (resp. possède la<NL>propriété $(R_n)$ géométrique en un point $x$, resp. est géométriquement<NL>normal en un point $x$) si",
    r"est \textup{géométriquement régulier en un point $x$ (resp. possède la<NL>propriété $(R_n)$ géométrique en un point $x$, resp. est géométriquement<NL>normal en un point $x$)} si")
add(p, "Définition (6.7.6): 'est régulier (resp. possède la propriété (R_n)'", "'(resp.' upright", "italic",
    "convention", 6, "high", r"est régulier (resp. possède la propriété", r"est régulier \textup{(resp.} possède la propriété")
add(p, "Définition (6.7.6): '(R_n), resp. est normal)'", "', resp.' upright", "italic", "convention", 6, "high",
    r"$(R_n)$, resp. est normal)", r"$(R_n)$\textup{, resp.} est normal)")
add(p, "Définition (6.7.6), second sentence: 'géométriquement régulier (resp. possède'", "'(resp.' upright", "italic",
    "convention", 6, "high", r"géométriquement régulier (resp. possède<NL>la propriété",
    r"géométriquement régulier \textup{(resp.} possède<NL>la propriété")
add(p, "Définition (6.7.6): '(ou encore est géométriquement régulier en codimension ≤n)'", "'(ou encore' upright",
    "italic", "convention", 6, "high", r"géométrique (ou encore est", r"géométrique \textup{(ou encore} est")
add(p, "Définition (6.7.6): '≤n), resp. est géométriquement normal)'", "', resp.' upright", "italic", "convention", 6,
    "high", r"$\leqslant n$), resp. est", r"$\leqslant n$)\textup{, resp.} est")
add(p, "Définition (6.7.6): 'si X est géométriquement régulier (resp. possède'", "'(resp.' upright", "italic",
    "convention", 6, "high", r"régulier (resp. possède la propriété $(R_n)$<NL>",
    r"régulier \textup{(resp.} possède la propriété $(R_n)$<NL>")
add(p, "Définition (6.7.6): 'géométrique, resp. est géométriquement normal) en tout point.'", "', resp.' upright",
    "italic", "convention", 6, "high", r"géométrique, resp. est géométriquement normal) en tout point",
    r"géométrique\textup{, resp.} est géométriquement normal) en tout point")
add(p, "after Définition (6.7.6) (edit 1 of 2): end the definition after 'en tout point.'",
    "the paragraphs 'On dit qu'une algèbre A ...' and 'Si X=Spec(K) ...' are roman with italic terms",
    "both paragraphs are inside the italic definition environment", "italics", None, "high",
    r"en tout point.<NL><NL>On dit qu'une algèbre", r"en tout point.<NL>\end{definition}<NL><NL>On dit qu'une algèbre",
    "Apply together with the next edit (GLOBAL_ISSUES 58 pattern).")
add(p, "after Définition (6.7.6) (edit 2 of 2): remove the old \\end{definition}", "see the previous entry",
    "\\end{definition} after the Bourbaki reference", "italics", None, "high",
    r"cor. 1 du th. 1).<NL>\end{definition}", r"cor. 1 du th. 1).", "Apply together with the previous edit.")
add(p, "paragraph after (6.7.6): 'un anneau géométriquement régulier'", "italic", "roman once the environment ends",
    "italics", None, "high", r"un anneau géométriquement régulier<NL>(resp.",
    r"un \emph{anneau géométriquement régulier}<NL>(resp.")
add(p, "paragraph after (6.7.6): '(resp. géométriquement normal,'", "'géométriquement normal' italic", "roman",
    "italics", None, "high", r"(resp. géométriquement normal, resp.", r"(resp. \emph{géométriquement normal}, resp.")
add(p, "paragraph after (6.7.6): 'resp. géométriquement réduit,'", "'géométriquement réduit' italic", "roman",
    "italics", None, "high", r"resp. géométriquement réduit, resp.<NL>", r"resp. \emph{géométriquement réduit}, resp.<NL>")
add(p, "paragraph after (6.7.6): 'resp. possédant la propriété (R_n) géométrique)'",
    "'possédant la propriété (R_n) géométrique' italic", "roman", "italics", None, "high",
    r"possédant la propriété $(R_n)$ géométrique)", r"\emph{possédant la propriété $(R_n)$ géométrique})")
add(p, "last paragraph of p. 148: 'que X est géométriquement régulier,'", "'géométriquement régulier' italic", "roman",
    "italics", None, "high", r"$X$ est géométriquement régulier, ou", r"$X$ est \emph{géométriquement régulier}, ou")
add(p, "last paragraph of p. 148: 'ou géométriquement normal,'", "'géométriquement normal' italic", "roman", "italics",
    None, "high", r"ou géométriquement<NL>normal, ou", r"ou \emph{géométriquement<NL>normal}, ou")
add(p, "last paragraph of p. 148: 'ou géométriquement réduit,'", "'géométriquement réduit' italic", "roman", "italics",
    None, "high", r"ou géométriquement réduit, ou que", r"ou \emph{géométriquement réduit}, ou que")
add(p, "last paragraph of p. 148: 'K est une extension séparable de k :'", "'séparable' italic (the second "
    "'séparable' of the paragraph is roman)", "roman", "italics", None, "high",
    r"une extension séparable<NL>de $k$: cela", r"une extension \emph{séparable}<NL>de $k$: cela")
add(p, "last paragraph of p. 148: '(Bourbaki, Alg., chap. VIII'", "'Alg.' italic", "roman", "italics", None, "high",
    r"(Bourbaki, Alg.,", r"(Bourbaki, \emph{Alg.},")
add(p, "last paragraph of p. 148: '§ 7, nº 3'", "'nº' with a raised o (enlarged crop)", "'n°' (degree sign)",
    "symbol", None, "medium", r"n°~3", r"n\textsuperscript{o}~3",
    "The release writes n\\textsuperscript{o} on 85 lines of ega4-2-fr.tex and n° on 6.")

# ---------------------------------------------------------------- page 149
p = 149
add(p, "Proposition (6.7.7), l. 2: 'désignons par Q(k')'", "bold italic Q", "$Q$", "font", None, "high",
    r"par $Q(k')$ la relation", r"par $\boldsymbol{Q}(k')$ la relation", BOLDQ)
add(p, "Proposition (6.7.7), l. 2: 'P(X_{(k')}, x') est vraie pour tout point'", "bold italic P", "$P$", "font",
    None, "high", r"$P(X_{(k')},x')$ est vraie pour", r"$\boldsymbol{P}(X_{(k')},x')$ est vraie pour", BOLDP)
add(p, "Proposition (6.7.7), l. 3: 'où P(Z, z)'", "bold italic P", "$P$", "font", None, "high",
    r"où $P(Z,z)$", r"où $\boldsymbol{P}(Z,z)$", BOLDP)
add(p, "Proposition (6.7.7), l. 3-4: 'des propriétés a), b), c)'", "'a), b), c)' upright", "italic", "convention", 6,
    "high", r"propriétés a),<NL>b), c) de", r"propriétés \textup{a),<NL>b), c)} de")
add(p, "Proposition (6.7.7), l. 4: 'de l'énoncé (6.7.4)'", "reference upright", "italic", "convention", 6, "high",
    r"l'énoncé (6.7.4)", r"l'énoncé \textup{(6.7.4)}")
for L in "abcdef":
    add(p, f"Proposition (6.7.7), label {L})", f"item label {L}) upright", f"\\item[{L})] comes out italic in the italic statement",
        "convention", 6, "high", f"\\item[{L})]", f"\\item[\\textup{{{L})}}]")
for L, old in (("a", r"$Q(k')$ est vraie pour toute extension finie $k'$"),
               ("b", r"$Q(k')$ est vraie pour toute extension finie radicielle"),
               ("c", r"$Q(k')$ est vraie pour toute extension de type fini"),
               ("d", r"$Q(k')$ est vraie pour toute extension $k'$ de $k$."),
               ("e", r"$Q(k')$ est vraie pour une"),
               ("f", r"$Q(k')$ est vraie pour toute extension $k'=k")):
    add(p, f"Proposition (6.7.7) {L}): 'Q(k') est vraie'", "bold italic Q", "$Q$", "font", None, "high",
        old, old.replace("$Q(k')$", r"$\boldsymbol{Q}(k')$"), BOLDQ + (" Apply before the 'une' entry." if L == "e" else ""))
add(p, "Proposition (6.7.7) e): 'est vraie pour une extension parfaite'", "'une' upright (emphasis)", "italic",
    "convention", 6, "high", r"une extension parfaite", r"\textup{une} extension parfaite",
    "Apply after the bold-Q entry of e).")
add(p, "proof of (6.7.7), l. 1: 'l'équivalence de a), b) et c)'", "'a)', 'b)', 'c)' italic", "roman", "italics", None,
    "high", r"l'équivalence de a), b) et c), il", r"l'équivalence de \emph{a)}, \emph{b)} et \emph{c)}, il")
add(p, "proof of (6.7.7), l. 2: 'que b) entraîne c).'", "'b)', 'c)' italic", "roman", "italics", None, "high",
    r"que b) entraîne c). Soit", r"que \emph{b)} entraîne \emph{c)}. Soit")
add(p, "proof of (6.7.7): 'K'=k(η')'", "bold italic k", "k(\\eta')", "convention", 1, "high",
    r"$K'=k(\eta')$", r"$K'=\boldsymbol{k}(\eta')$")
add(p, "proof of (6.7.7): 'Cela étant, P(X_{(k')}, x') est vraie par hypothèse'", "bold italic P", "$P$", "font",
    None, "high", r"$P(X_{(k')},x')$ est vraie par", r"$\boldsymbol{P}(X_{(k')},x')$ est vraie par", BOLDP)
add(p, "proof of (6.7.7): 'P(X_{(K')}, x'') est vraie'", "bold italic P", "$P$", "font", None, "high",
    r"$P(X_{(K')},x'')$", r"$\boldsymbol{P}(X_{(K')},x'')$", BOLDP)
add(p, "proof of (6.7.7): 'X_{(K')}=(X_{(K)})_{(K')} et pour tout x_0'", "no comma after 'et'", "'et, pour tout'",
    "punctuation", None, "high", r"(X_{(K)})_{(K')}$ et, pour tout", r"(X_{(K)})_{(K')}$ et pour tout")
add(p, "proof of (6.7.7): 'P(X_{(K)}, x_0) est vraie.'", "bold italic P", "$P$", "font", None, "high",
    r"$P(X_{(K)},x_0)$", r"$\boldsymbol{P}(X_{(K)},x_0)$", BOLDP)
add(p, "proof of (6.7.7), 2nd paragraph: 'de sorte que pour toute extension'", "no comma after 'que'",
    "'de sorte que, pour'", "punctuation", None, "high", r"de sorte que, pour", r"de sorte que pour")
add(p, "proof of (6.7.7), 2nd paragraph: 'pour toute extension K de k'", "'toute' italic", "roman", "italics", None,
    "high", r"toute extension $K$ de $k$, $X_{(K)}$", r"\emph{toute} extension $K$ de $k$, $X_{(K)}$")
add(p, "proof of (6.7.7): 'que e) implique f);'", "'e)', 'f)' italic", "roman", "italics", None, "high",
    r"que e) implique f);", r"que \emph{e)} implique \emph{f)};")
add(p, "proof of (6.7.7): 'donc f) entraîne b); d) entraîne trivialement e), et enfin e) entraîne d).'",
    "the six letters with their parentheses italic", "roman", "italics", None, "high",
    r"donc f) entraîne b); d) entraîne<NL>trivialement e), et enfin e) entraîne d).",
    r"donc \emph{f)} entraîne \emph{b)}; \emph{d)} entraîne<NL>trivialement \emph{e)}, et enfin \emph{e)} entraîne \emph{d)}.")
add(p, "proof of (6.7.7): 'si K est une extension quelconque de k'", "'quelconque' italic", "roman", "italics", None,
    "high", r"extension<NL>quelconque de $k$,", r"extension<NL>\emph{quelconque} de $k$,")
add(p, "proof of (6.7.7): 'comme K' est extension séparable de k''", "'séparable' italic", "roman", "italics", None,
    "high", r"est extension séparable de $k'$", r"est extension \emph{séparable} de $k'$")
add(p, "proof of (6.7.7): 'que Q(k') est vraie, puis que Q(K)'", "bold italic Q (twice)", "$Q$", "font", None,
    "high", r"que $Q(k')$ est vraie, puis que $Q(K)$", r"que $\boldsymbol{Q}(k')$ est vraie, puis que $\boldsymbol{Q}(K)$",
    BOLDQ)
add(p, "proof of (6.7.7): 'on déduit de (6.7.4) que Q(k') est vraie'", "Q(k') with a lower-case k' (enlarged crop)",
    "$Q(k')$: the TeX keeps the printed reading", "misprint_in_print", None, "medium", None, None,
    "Q(k') is hypothesis e) itself. What (6.7.4) gives here, k' being perfect and K' separable over k', is Q(K'); "
    "'puis que Q(K) est vraie' then descends from K' to K as in the first part of the proof.",
    corrected=r"$\boldsymbol{Q}(K')$")
add(p, "proof of (6.7.7): 'Il suffit donc de prouver que b) entraîne e).'", "'b) entraîne e)' italic, including 'entraîne'",
    "roman", "italics", None, "high", r"prouver que b) entraîne<NL>e). Nous", r"prouver que \emph{b) entraîne<NL>e)}. Nous")
add(p, "proof of (6.7.7): 'Nous prendrons k'=k^{p^{-∞}} dans e).'", "'e)' italic", "roman", "italics", None, "high",
    r"dans e).", r"dans \emph{e)}.")
add(p, "proof of (6.7.7), 3rd paragraph: 'par définition de la propriété P'", "bold italic P", "$P$", "font", None,
    "high", r"propriété $P$ dans", r"propriété $\boldsymbol{P}$ dans", BOLDP)
add(p, "proof of (6.7.7): 'B est un anneau local noethérien'", "'local' italic", "roman", "italics", None, "high",
    r"un anneau local noethérien", r"un anneau \emph{local} noethérien")
add(p, "proof of (6.7.7): 'ses sous-extensions finies k'_λ'", "'finies' italic", "roman", "italics", None, "high",
    r"sous-extensions finies $k'_\lambda$", r"sous-extensions \emph{finies} $k'_\lambda$")
add(p, "proof of (6.7.7): 'k'_λ et si l'on pose'", "no comma after 'et'", "'et, si l'on pose'", "punctuation", None,
    "high", r"$k'_\lambda$ et, si l'on pose", r"$k'_\lambda$ et si l'on pose")
add(p, "proof of (6.7.7), last line: 'est un homéomorphisme de Spec(B')'", "'homéomorphisme' italic", "roman",
    "italics", None, "high", r"un homéomorphisme de", r"un \emph{homéomorphisme} de")
add(p, "proof of (6.7.7), last line: 'de Spec(B') sur Spec(B'_λ)'", "'sur' italic", "roman", "italics", None, "high",
    r"$\operatorname{Spec}(B')$ sur<NL>", r"$\operatorname{Spec}(B')$ \emph{sur}<NL>")


# ---------------------------------------------------------------- checks
def check_pages():
    ok = True
    texts = {}
    for page in range(145, 150):
        t = (RUN / f"page_{page:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
        texts[page] = (t, t)
    for i, d in enumerate(F):
        if not d["fix"]:
            continue
        orig, cur = texts[d["page"]]
        o, n = d["fix"]["old"], d["fix"]["new"]
        c0, c1 = orig.count(o), cur.count(o)
        if c0 != 1 or c1 != 1:
            ok = False
            print(f"PAGE-FILE PROBLEM #{i} p{d['page']} orig={c0} seq={c1}: {d['where']}")
        if c1 == 1:
            cur = cur.replace(o, n)
        texts[d["page"]] = (orig, cur)
    return ok, texts


def check_release():
    """Mimic apply_fixes.py: locate the page segment in the (in-memory) release text, old must occur once."""
    t = REL.read_text(encoding="utf-8")
    marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")

    def locate(text, page):
        cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
        for k, (num, s) in enumerate(cuts):
            if num == page:
                j = k + 1
                while j < len(cuts) and cuts[j][0] == page:
                    j += 1
                return s, cuts[j][1] if j < len(cuts) else len(text)
        for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
            if a < page < b:
                return sa, sb
        return None, None

    ok = True
    applied = 0
    for i, d in enumerate(F):
        if not d["fix"]:
            continue
        s, e = locate(t, d["page"])
        seg = t[s:e]
        o, n = d["fix"]["old"], d["fix"]["new"]
        if seg.count(o) != 1:
            ok = False
            print(f"RELEASE PROBLEM #{i} p{d['page']} count={seg.count(o)}: {d['where']}")
            continue
        t = t[:s] + seg.replace(o, n) + t[e:]
        applied += 1
    return ok, applied, t


ok1, texts = check_pages()
ok2, applied, newrel = check_release()
print("page-file check:", "OK" if ok1 else "FAILED")
print("release simulation:", "OK" if ok2 else "FAILED", "applied", applied, "of", sum(1 for d in F if d["fix"]))
# markers after the simulated application
for m in re.finditer(r"\\oldpage\[IV-2\]\{(14[5-9]|150)\}", newrel):
    a = newrel.rfind("\n", 0, m.start() - 1)
    print("  marker", m.group(1), "|", newrel[a + 1:m.start()].strip()[-50:], "||", newrel[m.end():m.end() + 60].replace("\n", " / "))
for page in range(145, 150):
    (RUN / "crops_145_149" / f"after_{page:03d}.tex").write_text(texts[page][1], encoding="utf-8")
cnt = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt.setdefault(d["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(cnt, "total", len(F))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT)
