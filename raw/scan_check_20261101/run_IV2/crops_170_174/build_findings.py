"""Build findings_170_174.json for EGA IV-2 pp. 170-174 and check every fix.

Newlines inside strings are written as the placeholder NL and converted to LF.
Checks: every "old" occurs exactly once in its page_NNN.tex (CRLF normalised to LF);
then the fixes are applied in list order to an in-memory copy of the release file with
the page-segment logic of apply_fixes.py, and the resulting page starts are printed.
No .tex file is written."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
OUT = RUN / "findings_170_174.json"
NL = "\u23ce"


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=s(old), new=s(new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- printed p. 170, text in the p. 169 segment
OUT169 = ("OUTSIDE pp. 170-174: printed on p. 170, but the text lies in the p. 169 segment (page_169.tex, "
          "checked unique there) because \\oldpage[IV-2]{170} stands too late. Apply before the p. 170 marker "
          "insertion below. findings_165_169.json has the same edit (as a p. 169 entry): apply it once; a second "
          "copy fails harmlessly ('old' no longer found).")
add(169, "printed p. 170, line 1: Lemme (6.14.1.1), label (i)",
    "(i) upright before the italic statement 'Pour qu'un sous-anneau A de R ...'",
    r"\item[(i)] inside the italic lemma environment (label comes out italic)",
    "convention", 6, "high",
    r"\item[(i)] Pour qu'un", r"\item[\textup{(i)}] Pour qu'un", OUT169)
add(169, "printed p. 170, line 3: Lemme (6.14.1.1), label (ii)",
    "(ii) upright before the italic 'Soit (A_lambda) une famille ...'",
    r"\item[(ii)] inside the italic lemma environment",
    "convention", 6, "high",
    r"\item[(ii)] Soit $(A_\lambda)$", r"\item[\textup{(ii)}] Soit $(A_\lambda)$", OUT169)
add(169, "printed p. 170, proof of (6.14.1.1)(i), end: '(Bourbaki, Alg. comm., chap. II, § 3, n° 3, cor. 1 du th. 1)'",
    "Alg. comm. in italics", "Alg. comm. upright",
    "italics", None, "high",
    "(Bourbaki, Alg. comm., chap." + NL + "II,", r"(Bourbaki, \emph{Alg. comm.}, chap." + NL + "II,",
    OUT169)
NO_NOTE = ("The edition writes n\\textsuperscript{o} (103 times in ega4-2-fr.tex); n$^o$ (8 times, 4 on pp. 170-172) "
           "sets a math-italic o.")
add(169, "printed p. 170, same reference: 'chap. II, § 3, n° 3, cor. 1 du th. 1'",
    "n° with an upright superscript o", "n$^o$ (math italic o)", "font", None, "medium",
    "§ 3, n$^o$ 3, cor. 1 du th. 1", r"§ 3, n\textsuperscript{o} 3, cor. 1 du th. 1", OUT169 + " " + NO_NOTE)
add(169, "page break 169/170: the p. 170 marker (edit 1 of 2, insert)",
    "printed p. 169 ends with 'Lemme (6.14.1.1). — Soit R un anneau composé direct d'un nombre fini de corps.' "
    "(page_169_s4.png); printed p. 170 begins with '(i) Pour qu'un sous-anneau A de R ...'",
    r"\oldpage[IV-2]{170} stands before '(ii) Comme A\subset A_\lambda\subset R' (the second part of the proof), "
    "so the lemma's items (i), (ii) and the proof of (i) (about 19 printed lines of p. 170) sit in the p. 169 segment",
    "marker", None, "high",
    "d'un nombre fini de corps." + NL + r"\begin{enumerate}",
    "d'un nombre fini de corps." + NL + r"\oldpage[IV-2]{170}" + NL + r"\begin{enumerate}",
    "OUTSIDE pp. 170-174: 'old' lies in page_169.tex (checked unique there). Marker on its own line directly before "
    r"\begin{enumerate}, as at \oldpage[IV-2]{152}. Apply after the three p. 169 entries above and together with "
    "the next entry, which removes the old marker. findings_165_169.json makes the same move (its last two "
    "entries, insert 'fini de corps.\\n\\oldpage[IV-2]{170}\\n\\begin{enumerate}' and the same removal): apply one "
    "pair only; the result is identical.")
add(170, "page break 169/170: the p. 170 marker (edit 2 of 2, remove the misplaced marker)",
    "see the previous entry; '(ii) Comme A⊂A_λ⊂R' is an indented new paragraph in the middle of p. 170",
    r"\oldpage[IV-2]{170} directly before '(ii) Comme'",
    "marker", None, "high",
    r"\oldpage[IV-2]{170}" + NL + "(ii) Comme", "(ii) Comme",
    "Apply together with the previous entry (either order works). The blank line after 'dans $R$.' remains, so "
    "'(ii) Comme' still opens a paragraph, as printed. Identical to the p. 170 removal in findings_165_169.json.")

# ---------------------------------------------------------------- p. 170 segment
add(170, "proof of (6.14.1.1)(ii): 'résulte de Bourbaki, Alg. comm., chap. V, § 1, n° 3, prop. 12'",
    "Alg. comm. in italics", "Alg. comm. upright", "italics", None, "high",
    "résulte de Bourbaki, Alg. comm.,", r"résulte de Bourbaki, \emph{Alg. comm.},", None)
add(170, "proof of (6.14.1.1)(ii): 'chap. V, § 1, n° 3, prop. 12'",
    "n° with an upright superscript o", "n$^o$ (math italic o)", "font", None, "medium",
    "n$^o$" + NL + "3, prop. 12", r"n\textsuperscript{o}" + NL + "3, prop. 12", NO_NOTE)
add(170, "'... procède en plusieurs étapes.' / 'I) Réduction au cas où ...'",
    "'I) Réduction au cas où ...' begins a new indented paragraph after 'étapes.'",
    "no blank line between 'étapes.' and 'I) \\emph{Réduction': one paragraph in the TeX",
    "other", None, "high",
    "étapes." + NL + r"I) \emph{Réduction", "étapes." + NL + NL + r"I) \emph{Réduction",
    "Paragraph break the print has.")
add(170, "step I): 'B'=B⊗_A A' (I, 3.6.5)'",
    "bold I in the reference", "(I, 3.6.5)", "convention", 2, "high",
    "(I, 3.6.5), et il s'agit", r"(\textbf{I}, 3.6.5), et il s'agit", None)
add(170, "step I): 'il s'agit donc de prouver que B' est un anneau normal'",
    "normal in italics", "normal upright", "italics", None, "high",
    "anneau normal. Notons", r"anneau \emph{normal}. Notons", None)
add(170, "step I): 'par définition (6.8.1 et I, 3.6.5)'",
    "bold I in the reference", "(6.8.1 et I, 3.6.5)", "convention", 2, "high",
    "(6.8.1 et I, 3.6.5)", r"(6.8.1 et \textbf{I}, 3.6.5)", None)
add(170, "step I): 'X le spectre d'un anneau local intègre et intégralement clos B'",
    "'intègre et intégralement clos' in italics ('local' upright)", "upright", "italics", None, "high",
    "local intègre et" + NL + "intégralement clos $B$", r"local \emph{intègre et" + NL + r"intégralement clos} $B$", None)
add(170, "step I): 'la famille des clôtures intégrales des sous-A-algèbres'",
    "'clôtures intégrales' in italics", "upright", "italics", None, "high",
    "des clôtures" + NL + "intégrales des", r"des \emph{clôtures" + NL + r"intégrales} des", None)
add(170, "step I): 'des sous-A-algèbres de type fini de B'",
    "'de type fini' in italics", "upright", "italics", None, "high",
    "de type fini de $B$; il est clair", r"\emph{de type fini} de $B$; il est clair", None)
add(170, "step I): 'les anneaux B'_α sont normaux'",
    "normaux in italics", "upright", "italics", None, "high",
    "normaux et que, pour", r"\emph{normaux} et que, pour", None)
add(170, "step I): 'toute composante irréductible de Spec(B'_β) domine une composante'",
    "domine in italics", "upright", "italics", None, "high",
    "domine une composante", r"\emph{domine} une composante", None)
add(170, "printed p. 171, line 4: 'donc supposer que A est intègre et que B est la clôture intégrale de A'",
    "'clôture intégrale de' in italics", "upright", "italics", None, "high",
    "clôture intégrale de $A$. Enfin", r"\emph{clôture intégrale de} $A$. Enfin",
    "Printed on p. 171, but the text lies in the p. 170 segment (page_170.tex) until the p. 171 marker moves: apply "
    "before the p. 171 marker insertion below.")
add(170, "printed p. 171, line 5: 'se borner au cas où A est local (tenant compte ...'",
    "local in italics", "upright", "italics", None, "high",
    "est local (tenant", r"est \emph{local} (tenant",
    "Printed on p. 171, text in the p. 170 segment: apply before the p. 171 marker insertion below.")
add(170, "page break 170/171: the p. 171 marker (edit 1 of 2, insert)",
    "printed p. 170 ends 'On peut donc se borner à démontrer que B'=B⊗_A A' est normal lorsque B est'; printed "
    "p. 171 begins 'la clôture intégrale d'une A-algèbre intègre de type fini C; ...'",
    r"\oldpage[IV-2]{171} stands before 'II) \emph{Réduction', so the first six printed lines of p. 171 sit in the "
    "p. 170 segment",
    "marker", None, "high",
    "lorsque" + NL + "$B$ est la clôture intégrale d'une",
    "lorsque" + NL + "$B$ est" + NL + r"\oldpage[IV-2]{171}" + NL + "la clôture intégrale d'une",
    "Inserts the marker mid-sentence on its own line (no blank lines). Apply after every other p. 170 entry and "
    "together with the next entry, which removes the old marker.")
add(171, "page break 170/171: the p. 171 marker (edit 2 of 2, remove the misplaced marker)",
    "see the previous entry; 'II) Réduction au cas où A est un anneau local intègre ...' is an indented paragraph "
    "on p. 171, line 7",
    r"\oldpage[IV-2]{171} directly before 'II) \emph{Réduction'",
    "marker", None, "high",
    r"\oldpage[IV-2]{171}" + NL + r"II) \emph{Réduction", r"II) \emph{Réduction",
    "Apply together with, and after, the previous entry. The blank line after 'de $A$).' remains, so 'II)' still "
    "opens a paragraph, as printed.")

# ---------------------------------------------------------------- p. 171 segment
add(171, "step II): 'On sait (0, 23.2.7) que B est intersection'",
    "bold 0 in the reference", "(0, 23.2.7)", "convention", 2, "high",
    "On sait (0, 23.2.7) que", r"On sait (\textbf{0}, 23.2.7) que", None)
add(171, "step II): 'Posons K'=K⊗_A A', V'_λ=V_λ⊗_A A'; par platitude ...' after the display ⊕_λ(K/V_λ)",
    "'Posons' begins a new indented paragraph after the display",
    "no blank line after \\]: the TeX continues the paragraph",
    "other", None, "high",
    "\\]" + NL + "Posons", "\\]" + NL + NL + "Posons",
    "Paragraph break the print has (the text after the second display, 'et par suite', is not indented and stays "
    "in the paragraph).")
add(171, "step II), second display: 0→B'→K'→⊕(K'_λ/V'_λ)",
    "0→B'→K'→⊕(K'_λ/V'_λ): no index under ⊕, and K' carries the index λ",
    r"0\longrightarrow B'\longrightarrow K'\longrightarrow \bigoplus_\lambda(K'/V'_\lambda)",
    "misprint_in_print", None, "high",
    r"\bigoplus_\lambda(K'/V'_\lambda)", r"\bigoplus(K'_\lambda/V'_\lambda)",
    "The TeX silently corrects the print. The index λ has slipped from ⊕ to K': K'_λ is not defined (K' = K⊗_A A'), "
    "and tensoring the first display 0→B→K→⊕_λ(K/V_λ) with A' gives ⊕_λ(K'/V'_λ). The diplomatic text takes the "
    "printed reading.",
    corrected=r"\bigoplus_\lambda(K'/V'_\lambda)")
add(171, "step II): 'donc K' est un anneau noethérien normal'",
    "normal in italics", "upright", "italics", None, "high",
    "noethérien normal, et par", r"noethérien \emph{normal}, et par", None)
add(171, "step II): 'si l'on prouve que chacun des V'_λ est un anneau normal'",
    "normal in italics", "upright", "italics", None, "high",
    "est un anneau normal, il en sera", r"est un anneau \emph{normal}, il en sera", None)
add(171, "step II): 'On sait d'autre part (0, 23.2.7)'",
    "bold 0 in the reference", "(0, 23.2.7)", "convention", 2, "high",
    "d'autre part (0, 23.2.7)", r"d'autre part (\textbf{0}, 23.2.7)", None)
add(171, "step II): 'donc supposer que A est local, intègre et de dimension 1'",
    "'de dimension' in italics", "upright", "italics", None, "high",
    "et de dimension 1, $B$ sa", r"et \emph{de dimension} 1, $B$ sa", None)
add(171, "step II): 'Il y a une sous-A-algèbre finie A_1 de B'",
    "finie in italics", "upright", "italics", None, "high",
    "algèbre finie $A_1$", r"algèbre \emph{finie} $A_1$", None)
add(171, "step II): 'soit radiciel (0, 23.2.5)'",
    "bold 0 in the reference", "(0, 23.2.5)", "convention", 2, "high",
    "(0, 23.2.5)", r"(\textbf{0}, 23.2.5)", None)
add(171, "step II): 'ont même corps résiduel (loc. cit.).'",
    "'(loc. cit.)' in italics, parentheses included", "(loc. cit.) upright", "italics", None, "high",
    "résiduel (loc. cit.).", r"résiduel \emph{(loc. cit.)}.",
    "The parentheses are italic too (elsewhere the release writes (\\emph{loc. cit.})).")
add(171, "step II): 'A' est lui aussi un anneau local et que'",
    "local in italics", "upright", "italics", None, "high",
    "anneau local et que", r"anneau \emph{local} et que", None)
add(171, "step II): 'l'homomorphisme A→A' est local.'",
    "local in italics", "upright", "italics", None, "high",
    "A'$ est local.", r"A'$ est \emph{local}.", None)
P172 = ("Printed on p. 172, but the text lies in the p. 171 segment (page_171.tex) until the p. 172 marker moves: "
        "apply before the p. 172 marker insertion below.")
add(171, "printed p. 172, line 1: Lemme (6.14.1.2), label (i)",
    "(i) upright", r"\item[(i)] inside the italic lemma environment", "convention", 6, "high",
    r"\item[(i)] Si $\mathfrak q'_j$", r"\item[\textup{(i)}] Si $\mathfrak q'_j$", P172)
add(171, "printed p. 172, line 3: Lemme (6.14.1.2)(i), 'le corps des fractions L'_j de A'/q'_j (1⩽j⩽r), de sorte que'",
    "'(1⩽j⩽r)' printed after A'/q'_j (third time in (i))",
    "'des fractions $L'_j$ de $A'/\\mathfrak q'_j$, de sorte que': the parenthesis is missing",
    "missing", None, "high",
    r"de $A'/\mathfrak q'_j$, de sorte", r"de $A'/\mathfrak q'_j$ $(1\leqslant j\leqslant r)$, de sorte", P172)
add(171, "printed p. 172, line 5: Lemme (6.14.1.2), label (ii)",
    "(ii) upright", r"\item[(ii)] inside the italic lemma environment", "convention", 6, "high",
    r"\item[(ii)] L'idéal", r"\item[\textup{(ii)}] L'idéal", P172)
add(171, "printed p. 172, line 7: Lemme (6.14.1.2), label (iii)",
    "(iii) upright", r"\item[(iii)] inside the italic lemma environment", "convention", 6, "high",
    r"\item[(iii)] Si", r"\item[\textup{(iii)}] Si", P172)
add(171, "printed p. 172, line 7: Lemme (6.14.1.2)(iii), 'Si Ā'_p' désigne le sous-anneau de L''",
    "bar over the A only: Ā'_{p'}", r"\overline{A'_{\mathfrak p'}} (bar over A'_{p'})", "formula", None, "high",
    r"$\overline{A'_{\mathfrak p'}}$ désigne", r"$\overline{A}'_{\mathfrak p'}$ désigne", P172)
add(171, "printed p. 172, display (6.14.1.3): A'=K'∩Ā'_p'.",
    "bar over the A only", r"\overline{A'_{\mathfrak p'}}", "formula", None, "high",
    r"A'=K'\cap\overline{A'_{\mathfrak p'}}.", r"A'=K'\cap\overline{A}'_{\mathfrak p'}.", P172)
add(171, "page break 171/172: the p. 172 marker (edit 1 of 2, insert)",
    "printed p. 171 ends with the opening of Lemme (6.14.1.2), '... k=A/m son corps résiduel.' (page_171_s4.png); "
    "printed p. 172 begins with '(i) Si q'_j (1⩽j⩽r) sont les idéaux minimaux de A' ...'",
    r"\oldpage[IV-2]{172} stands after \begin{proof}, before 'L'assertion (i)', so the lemma's items (i)-(iii) and "
    "(6.14.1.3) sit in the p. 171 segment",
    "marker", None, "high",
    "son corps résiduel." + NL + r"\begin{enumerate}",
    "son corps résiduel." + NL + r"\oldpage[IV-2]{172}" + NL + r"\begin{enumerate}",
    "Marker on its own line before \\begin{enumerate}. Apply after every other p. 171 entry (the six entries above "
    "edit text that moves into the p. 172 segment) and together with the next entry, which removes the old marker.")
add(172, "page break 171/172: the p. 172 marker (edit 2 of 2, remove the misplaced marker)",
    "see the previous entry", r"\oldpage[IV-2]{172} directly before 'L'assertion (i)'",
    "marker", None, "high",
    r"\oldpage[IV-2]{172}" + NL + "L'assertion (i)", "L'assertion (i)",
    "Apply together with the previous entry (either order works). Afterwards \\begin{proof} is directly followed "
    "by 'L'assertion (i)'.")

# ---------------------------------------------------------------- p. 172 segment
add(172, "proof of (6.14.1.2): 'A'⊗_A k=A'/mA' est un anneau normal local et noethérien'",
    "local in italics ('normal' upright)", "upright", "italics", None, "high",
    "anneau normal local et", r"anneau normal \emph{local} et", None)
add(172, "proof of (6.14.1.2): 'donc intègre, ce qui montre déjà'",
    "intègre in italics", "upright", "italics", None, "high",
    "donc intègre, ce qui", r"donc \emph{intègre}, ce qui", None)
add(172, "proof of (6.14.1.3): 'On a évidemment A'⊂K'∩Ā'_p''",
    "bar over the A only", r"\overline{A'_{\mathfrak p'}}", "formula", None, "high",
    r"K'\cap\overline{A'_{\mathfrak p'}}$. Inversement", r"K'\cap\overline{A}'_{\mathfrak p'}$. Inversement", None)
add(172, "proof of (6.14.1.3): 'p' est le seul idéal premier associé à A'/a'^nA''",
    "seul in italics", "upright", "italics", None, "high",
    "seul idéal premier associé à" + NL + "$A'/", r"\emph{seul} idéal premier associé à" + NL + "$A'/", None)
add(172, "proof of (6.14.1.3): 'comme par hypothèse y'∈Ā'_p''",
    "bar over the A only", r"\overline{A'_{\mathfrak p'}}", "formula", None, "high",
    r"$y'\in\overline{A'_{\mathfrak p'}}$", r"$y'\in\overline{A}'_{\mathfrak p'}$", None)
add(172, "'B' est radiciel sur A''",
    "radiciel in italics", "upright", "italics", None, "high",
    "est radiciel sur", r"est \emph{radiciel} sur", None)
add(172, "'radiciel sur A' (I, 3.5.7)'",
    "bold I in the reference", "(I, 3.5.7)", "convention", 2, "high",
    "(I, 3.5.7)", r"(\textbf{I}, 3.5.7)", None)
add(172, "'et par suite est aussi un anneau local; en outre'",
    "local in italics", "upright", "italics", None, "high",
    "local; en outre $B'$", r"\emph{local}; en outre $B'$", None)
add(172, "'(Bourbaki, Alg. comm., chap. V, § 2, n° 1, prop. 1)'",
    "Alg. comm. in italics", "upright", "italics", None, "high",
    "Alg. comm., chap. V, § 2", r"\emph{Alg. comm.}, chap. V, § 2", None)
add(172, "same reference: 'chap. V, § 2, n° 1, prop. 1'",
    "n° with an upright superscript o", "n$^o$ (math italic o)", "font", None, "medium",
    "n$^o$ 1, prop.", r"n\textsuperscript{o} 1, prop.", NO_NOTE)
add(172, "'B'_p' est un anneau noethérien et normal.'",
    "noethérien and normal in italics ('et' upright)", "upright", "italics", None, "high",
    "anneau noethérien et normal. Or", r"anneau \emph{noethérien} et \emph{normal}. Or", None)
add(172, "'comme tout élément de A'—p' est régulier dans L_1'",
    "long dash for the set difference A'—p'", "$A'-\\mathfrak p'$", "convention", 7, "high",
    r"$A'-\mathfrak p'$", r"$A'\setmin\mathfrak p'$", None)
add(172, "'contient l'anneau local intègre de dimension 1, A'_p'/q'_jA'_p''",
    "'intègre de dimension' in italics", "upright", "italics", None, "high",
    "local intègre de dimension 1,", r"local \emph{intègre de dimension} 1,", None)
add(172, "'Krull-Akizuki (Bourbaki, Alg. comm., chap. VII, § 2, n° 5, prop. 5)'",
    "Alg. comm. in italics", "upright", "italics", None, "high",
    "Alg. comm., chap. VII", r"\emph{Alg. comm.}, chap. VII", None)
add(172, "same reference: 'chap. VII, § 2, n° 5, prop. 5'",
    "n° with an upright superscript o", "n$^o$ (math italic o)", "font", None, "medium",
    "n$^o$ 5,", r"n\textsuperscript{o} 5,", NO_NOTE)

# ---------------------------------------------------------------- p. 173 segment
add(173, "proof of Lemme (6.14.1.4): 'on a donc a∩b⊂a∩c⊂c'",
    "𝔞∩𝔟⊂𝔞∩𝔠⊂𝔠 (Fraktur a first)", r"\mathfrak c\cap\mathfrak b\subset\mathfrak a\cap\mathfrak c\subset\mathfrak c",
    "formula", None, "high",
    r"\mathfrak c\cap\mathfrak b\subset", r"\mathfrak a\cap\mathfrak b\subset",
    "Wrong letter in the TeX (Fraktur c for the printed Fraktur a); the printed chain is also the correct one.")
add(173, "'sont respectivement isomorphes aux fibres du morphisme'",
    "isomorphes in italics", "upright", "italics", None, "high",
    "isomorphes aux fibres", r"\emph{isomorphes} aux fibres", None)
add(173, "'au point générique de Spec(A) (I, 3.6.4)'",
    "bold I in the reference", "(I, 3.6.4)", "convention", 2, "high",
    "(I, 3.6.4)", r"(\textbf{I}, 3.6.4)", None)
add(173, "'donc sont géométriquement normales par hypothèse'",
    "'géométriquement normales' in italics", "upright", "italics", None, "high",
    "géométriquement normales par", r"\emph{géométriquement normales} par", None)
add(173, "'on en conclut qu'il est normal (6.8.1)'",
    "normal in italics", "upright", "italics", None, "high",
    "qu'il est normal (6.8.1)", r"qu'il est \emph{normal} (6.8.1)", None)
add(173, "'on déduit de (6.5.4) que B'_p' est normal.'",
    "normal in italics", "upright", "italics", None, "high",
    r"(6.5.4) que $B'_{\mathfrak p'}$ est normal.", r"(6.5.4) que $B'_{\mathfrak p'}$ est \emph{normal}.", None)
add(173, "'et l'anneau B̄'_q'=L''×B'_q''",
    "bar over the B only", r"\overline{B'_{\mathfrak q'}}", "formula", None, "high",
    r"$\overline{B'_{\mathfrak q'}}=L''", r"$\overline{B}'_{\mathfrak q'}=L''", None)
add(173, "'des anneaux L''×(A'_α)_p'_α=(Ā'_α)_p'_α.'",
    "bar over the A only", r"(\overline{A'_\alpha})", "formula", None, "high",
    r"=" + NL + r"(\overline{A'_\alpha})", r"=" + NL + r"(\overline{A}'_\alpha)", None)
add(173, "display after 'l'on a': A'_α=K'∩(Ā'_α)_p'_x",
    "bar over the A only", r"(\overline{A'_\alpha})", "formula", None, "high",
    r"K'\cap(\overline{A'_\alpha})", r"K'\cap(\overline{A}'_\alpha)", "Apply before the next entry (same display).")
add(173, "display after 'l'on a': subscript of p'",
    "A'_α=K'∩(Ā'_α)_{p'_x}: the inner index under p' is an italic x (not α), unlike every other p'_α on the page",
    r"_{\mathfrak p'_\alpha} at the end of the display", "misprint_in_print", None, "medium",
    r"_{\mathfrak p'_\alpha}" + NL + "\\]", r"_{\mathfrak p'_x}" + NL + "\\]",
    "The TeX silently corrects the print. The glyph is a clear italic x (possibly chi), distinct from the α of A'_α in "
    "the same display; the correct index is α. Listed after the bar fix of the same display; its 'old' does not "
    "overlap it.",
    corrected=r"_{\mathfrak p'_\alpha}")
add(173, "display: B'=K'∩B̄'_q'.",
    "bar over the B only", r"\overline{B'_{\mathfrak q'}}", "formula", None, "high",
    r"B'=K'\cap\overline{B'_{\mathfrak q'}}.", r"B'=K'\cap\overline{B}'_{\mathfrak q'}.", None)
add(173, "'Mais B̄'_q', composé direct des anneaux normaux' after the display B'=K'∩B̄'_q'.",
    "'Mais' begins a new indented paragraph after the display",
    "no blank line after \\]", "other", None, "high",
    "\\]" + NL + "Mais", "\\]" + NL + NL + "Mais", "Paragraph break the print has.")
add(173, "'Mais B̄'_q', composé direct'",
    "bar over the B only", r"\overline{B'_{\mathfrak q'}}", "formula", None, "high",
    r"$\overline{B'_{\mathfrak q'}}$, composé", r"$\overline{B}'_{\mathfrak q'}$, composé", None)
add(173, "Corollaire (6.14.2): '(non nécessairement localement noethérien)'",
    "the parenthesis is upright inside the italic statement", "italic (corollary environment)",
    "convention", 6, "high",
    "(non nécessairement" + NL + "localement noethérien)",
    r"\textup{(non nécessairement" + NL + r"localement noethérien)}", None)
add(173, "Corollaire (6.14.3): 'Soient k un corps, X, Y deux k-préschémas'",
    "comma after 'corps'", "semicolon: 'Soient $k$ un corps; $X$, $Y$'", "punctuation", None, "high",
    "un corps; $X$, $Y$", "un corps, $X$, $Y$", None)

# ---------------------------------------------------------------- p. 174 segment
add(174, "proof of Lemme (6.14.4.1): 'x^n+a_1x^{n-1}+ . . . +a_n∈n'",
    "baseline dots", r"\cdots", "symbol", None, "high",
    r"+\cdots+a_n", r"+\ldots+a_n", None)
add(174, "proof of Lemme (6.14.4.1): 'avec a_i∈A'",
    "a_i (index i)", "$a_k\\in A$", "formula", None, "high",
    r"avec $a_k\in A$", r"avec $a_i\in A$", None)
add(175, "page break 174/175: the p. 175 marker (edit 1 of 2, insert)",
    "printed p. 174 ends '... sous-A-algèbres de type fini de B, et soit C_α la fermeture' (page_174_s4.png); "
    "printed p. 175 begins 'intégrale de A dans B_α. Il résulte aussitôt ...' (page_175_s1.png)",
    r"\oldpage[IV-2]{175} stands before 'II) \emph{Réduction au cas où $B$ est une $A$-algèbre', two printed "
    "lines too early, so the end of p. 174 sits in the p. 175 segment",
    "marker", None, "high",
    r"et soit $C_\alpha$ la fermeture" + NL + r"intégrale de $A$ dans $B_\alpha$.",
    r"et soit $C_\alpha$ la fermeture" + NL + r"\oldpage[IV-2]{175}" + NL + r"intégrale de $A$ dans $B_\alpha$.",
    "OUTSIDE pp. 170-174: 'old' lies in page_175.tex (checked unique there). Marker mid-sentence on its own line. "
    "Apply together with the next entry. The moved two lines ('II) Réduction au cas où B est une A-algèbre intègre "
    "de type fini contenant A. — Soit (B_α) ... et soit C_α la fermeture') match the print of p. 174. The pp. "
    "175-179 batch may report the same move: apply it once.")
add(175, "page break 174/175: the p. 175 marker (edit 2 of 2, remove the misplaced marker)",
    "see the previous entry; 'II) Réduction ...' is an indented paragraph on p. 174",
    r"\oldpage[IV-2]{175} directly before 'II) \emph{Réduction'",
    "marker", None, "high",
    r"\oldpage[IV-2]{175}" + NL + r"II) \emph{Réduction", r"II) \emph{Réduction",
    "OUTSIDE pp. 170-174 (page_175.tex, checked unique there). Apply together with the previous entry (either order "
    "works). The blank line after 'dans $B'$.' remains, so 'II)' still opens a paragraph, as printed.")

# ---------------------------------------------------------------- checks
pages = {}
for p in range(168, 177):
    f = RUN / f"page_{p:03d}.tex"
    if f.exists():
        pages[p] = f.read_text(encoding="utf-8").replace("\r\n", "\n")
ok = True
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    old = d["fix"]["old"]
    n = pages[d["page"]].count(old)
    if n != 1:
        ok = False
        print(f"#{i} page {d['page']}: old occurs {n} times: {old!r}")
print("uniqueness in page files:", "OK" if ok else "FAILED")

# simulate apply_fixes.py on an in-memory copy of the release file
text = REL.read_text(encoding="utf-8")
part = "IV-2"
marker = re.compile(r"\\oldpage\[" + re.escape(part) + r"\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, st) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return st, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


applied = 0
for i, d in enumerate(F):
    if d["fix"] is None:
        continue
    st, en = locate(text, d["page"])
    seg = text[st:en]
    c = seg.count(d["fix"]["old"])
    if c != 1:
        print(f"SIM #{i} page {d['page']}: old occurs {c} times in the live segment: {d['fix']['old']!r}")
        continue
    text = text[:st] + seg.replace(d["fix"]["old"], d["fix"]["new"]) + text[en:]
    applied += 1
print("simulated applied:", applied, "of", sum(1 for d in F if d["fix"]))
for p in range(170, 176):
    st, en = locate(text, p)
    seg = text[st:en]
    print(f"--- p.{p} starts:", repr(seg[:110]))
    print(f"    p.{p} ends:  ", repr(seg[-110:]))
dups = [m.group(1) for m in marker.finditer(text)]
print("markers 168-177 after simulation:", [x for x in dups if 168 <= int(x) <= 177])
(RUN / "crops_170_174" / "sim_169_175.txt").write_text(text[locate(text, 169)[0]:locate(text, 176)[0]], encoding="utf-8")
if "--write" in sys.argv:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT, len(F), "findings")
