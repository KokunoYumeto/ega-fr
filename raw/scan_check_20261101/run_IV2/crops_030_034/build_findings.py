"""Build findings_030_034.json for run_IV2 (EGA IV-2 pp. 30-34) and verify every edit.
The pilcrow sign stands for a line break inside "old"/"new"."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_030_034.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV2\native\ega4\ega4-2-fr.tex")
NL = "\u00b6"

F = []


def add(page, where, scan, tex, kind, old, new, conv=None, conf="high", note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    F.append(d)


def label(page, lab, where):
    add(page, where, f"label {lab} upright (proof text is roman)", r"\emph{" + lab + "} (italic)", "italics",
        r"\emph{" + lab + "}", lab, note="Proof-part label; the print sets the roman numeral upright.")


def bold(page, where, ref, old, new):
    add(page, where, f"{ref} with a bold chapter numeral", f"{ref}, plain numeral", "convention", old, new, conv=2)


# ---------------- page 30 ----------------
bold(30, "first paragraph, end", "(I, 3.3.11)", "(I, 3.3.11)", r"(\textbf{I}, 3.3.11)")
label(30, "(i)", "proof of (2.7.1), (i)")
add(30, "proof of (2.7.1), (i), l. 2: 'est fermé; comme'", "'fermé' italic (enlarged crop); the later 'est fermé, il' is upright",
    "'fermé' upright", "italics", r"X$ est fermé~;", r"X$ est \emph{fermé}~;")
bold(30, "proof of (2.7.1), (i)", "(I, 5.3.4)", "(I, 5.3.4)", r"(\textbf{I}, 5.3.4)")
label(30, "(ii)", "proof of (2.7.1), (ii)")
label(30, "(iii)", "proof of (2.7.1), '(iii) et (iv) :'")
label(30, "(iv)", "proof of (2.7.1), '(iii) et (iv) :'")
add(30, "Lemme (2.7.1.1), first '(resp. de présentation finie)'", "'(resp.' and the closing parenthesis upright inside the italic lemma (enlarged crop)",
    "italic (lemma environment)", "convention", "(resp. de présentation finie), il faut",
    r"\textup{(resp.} de présentation finie\textup{)}, il faut", conv=6)
add(30, "Lemme (2.7.1.1), second '(resp. de présentation finie)'", "'(resp.' and the closing parenthesis upright inside the italic lemma",
    "italic (lemma environment)", "convention", "(resp. de présentation finie)." + NL + r"\end{lemma}",
    r"\textup{(resp.} de présentation finie\textup{)}." + NL + r"\end{lemma}", conv=6)
add(30, "proof of (2.7.1.1), first paragraph, end: '(0_I, 6.4.1)'", "(0_I, 6.4.1) with a bold 0", "plain 0", "convention",
    r"$(0_{\mathrm I},6.4.1)$", r"$(\mathbf{0}_{\mathrm I},6.4.1)$", conv=2)
add(30, "proof of (2.7.1.1), second paragraph: 'une suite exacte 0→J→C→B→0, et par suite'",
    "the exact sequence is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"0\to\mathfrak J\to C\to B\to0," + NL + r"\]" + NL,
    r"$0\to\mathfrak J\to C\to B\to0$," + NL)
label(30, "(v)", "proof of (2.7.1), (v)")
label(30, "(vi)", "proof of (2.7.1), (vi)")
label(30, "(vii)", "proof of (2.7.1), (vii)")
bold(30, "proof of (2.7.1), (vii)", "(II, 5.4.1)", "(II, 5.4.1)", r"(\textbf{II}, 5.4.1)")
label(30, "(viii)", "proof of (2.7.1), (viii)")
add(30, "proof of (2.7.1), (viii): 'il s'agit de prouver que θ : O_Y→f_*(O_X) est un isomorphisme'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"\theta:\mathcal O_Y\longrightarrow f_*(\mathcal O_X)" + NL + r"\]" + NL,
    r"$\theta:\mathcal O_Y\to f_*(\mathcal O_X)$" + NL)

# ---------------- page 31 ----------------
label(31, "(ix)", "proof of (2.7.1), (ix)")
bold(31, "proof of (2.7.1), (ix)", "(I, 5.3.4)", "(I, 5.3.4)", r"(\textbf{I}, 5.3.4)")
bold(31, "proof of (2.7.1), (ix)", "(I, 5.3.8)", "(I, 5.3.8)", r"(\textbf{I}, 5.3.8)")
label(31, "(x)", "proof of (2.7.1), (x)")
bold(31, "proof of (2.7.1), (x)", "(I, 3.4.8)", "(I, 3.4.8)", r"(\textbf{I}, 3.4.8)")
label(31, "(xi)", "proof of (2.7.1), (xi)")
GQ = ("Notation clash in the print: g already denotes the base change Y'→Y (g^*(θ) on this page, g in the diagram of "
      "(xiii)); the print nevertheless names the factor X→Z of f = j∘g 'g' throughout (xi) (enlarged crop: the same "
      "italic g as in 'g est fidèlement plat'). The TeX renamed it q silently; the diplomatic text restores g, the "
      "corrected edition keeps q. Apply the five g/q edits of (xi) together.")
add(31, "proof of (2.7.1), (xi): 'posons f = j∘g, où j : Z→Y'", "f=j∘g", "$f=j\\circ q$", "misprint_in_print",
    r"$f=j\circ q$", r"$f=j\circ g$", corrected=r"$f=j\circ q$", note=GQ)
add(31, "proof of (2.7.1), (xi): 'on a alors f' = j'∘g''", "f'=j'∘g'", "$f'=j'\\circ q'$", "misprint_in_print",
    r"$f'=j'\circ q'$", r"$f'=j'\circ g'$", corrected=r"$f'=j'\circ q'$", note="See the first g/q item of (xi).")
add(31, "proof of (2.7.1), (xi): 'avec j' = j_(Y'), g' = g_(Y')'", "g'=g_{(Y')}", "$q'=q_{(Y')}$", "misprint_in_print",
    r"$q'=q_{(Y')}$", r"$g'=g_{(Y')}$", corrected=r"$q'=q_{(Y')}$", note="See the first g/q item of (xi).")
add(31, "proof of (2.7.1), (xi): 'signifie alors que g' est une immersion ouverte'", "g'", "$q'$", "misprint_in_print",
    r"que $q'$ est une immersion", r"que $g'$ est une immersion", corrected=r"que $q'$ est une immersion",
    note="See the first g/q item of (xi).")
bold(31, "proof of (2.7.1), (xi)", "(I, 9.5.10)", "(I, 9.5.10)", r"(\textbf{I}, 9.5.10)")
add(31, "proof of (2.7.1), (xi): 'donc il en est de même de g par (x)'", "g", "$q$", "misprint_in_print",
    r"de même de $q$ par (x)", r"de même de $g$ par (x)", corrected=r"de même de $q$ par (x)",
    note="See the first g/q item of (xi).")
label(31, "(xii)", "proof of (2.7.1), (xii)")
label(31, "(xiii)", "proof of (2.7.1), '(xiii) et (xiv)'")
label(31, "(xiv)", "proof of (2.7.1), '(xiii) et (xiv)'")
bold(31, "proof of (2.7.1), (xiii)-(xiv)", "(II, 5.1.1)", "(II, 5.1.1)", r"(\textbf{II}, 5.1.1)")
bold(31, "proof of (2.7.1), (xiii)-(xiv)", "(II, 1.5.2)", "(II, 1.5.2)", r"(\textbf{II}, 1.5.2)")
bold(31, "proof of (2.7.1), (xiii)-(xiv), before the diagram", "(II, 1.2.7)", r"$\mathcal A'$) (II, 1.2.7)",
     r"$\mathcal A'$) (\textbf{II}, 1.2.7)")
bold(31, "proof of (2.7.1), (xiii)-(xiv), after the diagram", "(II, 1.2.7)", "de (II, 1.2.7) que", r"de (\textbf{II}, 1.2.7) que")
bold(31, "proof of (2.7.1), (xiii)-(xiv)", "(II, 5.1.6)", "(II, 5.1.6)", r"(\textbf{II}, 5.1.6)")

# ---------------- page 32 ----------------
label(32, "(xv)", "proof of (2.7.1), (xv)")
label(32, "(xvi)", "proof of (2.7.1), (xvi)")
bold(32, "proof of (2.7.1), (xvi)", "(II, 6.2.2 ...", "(II, 6.2.2", r"(\textbf{II}, 6.2.2")
bold(32, "proof of (2.7.1), (xvi)", "... et I, 6.4.4)", "et I," + NL + "6.4.4)", r"et \textbf{I}," + NL + "6.4.4)")
label(32, "(xvii)", "proof of (2.7.1), (xvii)")
add(32, "proof of (2.7.1), (xvii): 'donc B'_α est un A'-module de type fini'", "'module' italic (enlarged crop)",
    "'module' upright", "italics", r"$B'_\alpha$ est un $A'$-module", r"$B'_\alpha$ est un $A'$-\emph{module}")
add(32, "Corollaire (2.7.2), l. 1: 'étant celles de (2.7.1)'", "(2.7.1) upright inside the italic statement",
    "italic (corollary environment)", "convention", "celles de (2.7.1), supposons",
    r"celles de \textup{(2.7.1)}, supposons", conv=6)
add(32, "Corollaire (2.7.2): 'L' = L ⊗_{O_Y} O_{Y'} son image réciproque'",
    "L'=L⊗_{O_Y}O_{Y'} (subscript O_Y, factor O_{Y'}; enlarged crop)", "\\mathcal L\\otimes_{\\mathcal O_X}\\mathcal O_{X'}",
    "formula", r"\otimes_{\mathcal O_X}\mathcal O_{X'}", r"\otimes_{\mathcal O_Y}\mathcal O_{Y'}",
    note="Not a misprint: X' = X×_Y Y', and L⊗_{O_Y}O_{Y'} is the usual EGA notation for the inverse image.")
add(32, "Corollaire (2.7.2): '... O_{Y'} son image réciproque'", "no comma before 'son image réciproque'",
    "comma after the formula", "punctuation", "$, son image", "$ son image")
add(32, "Corollaire (2.7.2), first '(resp. très ample)'", "'(resp.' and the closing parenthesis upright inside the italic statement",
    "italic (corollary environment)", "convention", "(resp. très ample) pour $f$, il",
    r"\textup{(resp.} très ample\textup{)} pour $f$, il", conv=6)
add(32, "Corollaire (2.7.2), second '(resp. très ample)'", "'(resp.' and the closing parenthesis upright inside the italic statement",
    "italic (corollary environment)", "convention", "(resp. très ample) pour $f'$.",
    r"\textup{(resp.} très ample\textup{)} pour $f'$.", conv=6)
bold(32, "proof of (2.7.2), l. 1", "(II, 4.4.10 et 4.6.13)", "(II, 4.4.10", r"(\textbf{II}, 4.4.10")
bold(32, "proof of (2.7.2)", "(II, 4.6.1)", "(II, 4.6.1)", r"(\textbf{II}, 4.6.1)")
add(32, "proof of (2.7.2): 'Si L' est très ample pour f'", "'très ample' italic (enlarged crop)", "upright", "italics",
    "est très" + NL + "ample", r"est \emph{très" + NL + "ample}")
add(32, "proof of (2.7.2): 'Si L' est très ample pour f, l'homomorphisme canonique σ''",
    "'pour f,' without a prime (enlarged crop)", "pour $f'$,", "misprint_in_print",
    "pour $f'$, l'homomorphisme", "pour $f$, l'homomorphisme", corrected="pour $f'$, l'homomorphisme",
    note="The hypothesis is on L' and f'; the TeX silently corrected the print's f to f'.")
add(32, "proof of (2.7.2): 'et le morphisme r' = r_{L',σ'} : X'→P(E') est une immersion'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"r'=r_{\mathcal L',\sigma'}:X'\longrightarrow\mathbf P(\mathcal E')" + NL + r"\]" + NL,
    r"$r'=r_{\mathcal L',\sigma'}:X'\to\mathbf P(\mathcal E')$" + NL,
    note="The bold P is upright in the print here (matches \\mathbf P).")
add(32, "proof of (2.7.2): 'est une immersion (II, 4.4.4, b))'", "'immersion' italic", "upright", "italics",
    "est une immersion", r"est une \emph{immersion}")
add(32, "proof of (2.7.2): '(II, 4.4.4, b)) nécessairement'", "(II, 4.4.4, b)) with a bold II", "plain II", "convention",
    "(II, 4.4.4, b)) nécessairement", r"(\textbf{II}, 4.4.4, b)) nécessairement", conv=2,
    note="Apply before the next item (italic b), whose 'old' overlaps this one.")
add(32, "proof of (2.7.2): '(II, 4.4.4, b)) nécessairement'", "italic 'b)' (letter and its parenthesis), then the roman ')' (enlarged crop)",
    "upright b)", "italics", "4.4.4, b)) nécessairement", r"4.4.4, \emph{b)}) nécessairement",
    note="'old' still occurs once after the previous item.")
bold(32, "proof of (2.7.2)", "(II, 4.1.3)", "(II, 4.1.3)", r"(\textbf{II}, 4.1.3)")
add(32, "proof of (2.7.2): 'l'homomorphisme g'^*(σ) : g'^*(f^*(f_*(L))) → g'^*(L) est identique'",
    "inline: g'^*(σ) : g'^*(f^*(f_*(L))) → g'^*(L) (enlarged crop)",
    "displayed g'^*(f^*(\\mathcal E))\\longrightarrow g'^*(\\mathcal L): the map's name g'^*(σ) is missing and f_*(L) is written E",
    "formula",
    r"\[" + NL + r"g'^*(f^*(\mathcal E))\longrightarrow g'^*(\mathcal L)" + NL + r"\]" + NL,
    r"$g'^*(\sigma):g'^*(f^*(f_*(\mathcal L)))\to g'^*(\mathcal L)$" + NL,
    note="Three differences in one formula: inline in the print, 'g'^*(σ) :' missing, f^*(E) for the printed f^*(f_*(L)).")
bold(32, "proof of (2.7.2)", "(II, 3.7.4)", "(II, 3.7.4)", r"(\textbf{II}, 3.7.4)")
bold(32, "proof of (2.7.2)", "(II, 4.2.10)", "(II, 4.2.10)", r"(\textbf{II}, 4.2.10)")
add(32, "proof of (2.7.2): 'et par suite L est très ample (II, 4.4.4, b))'", "'très ample' italic", "upright", "italics",
    r"$\mathcal L$ est très ample", r"$\mathcal L$ est \emph{très ample}")
add(32, "proof of (2.7.2): 'très ample (II, 4.4.4, b)).'", "(II, 4.4.4, b)) with a bold II", "plain II", "convention",
    "(II, 4.4.4, b)).", r"(\textbf{II}, 4.4.4, b)).", conv=2,
    note="Apply before the next item (italic b), whose 'old' overlaps this one.")
add(32, "proof of (2.7.2): 'très ample (II, 4.4.4, b)).'", "italic 'b)' then the roman ')' (enlarged crop)", "upright b)",
    "italics", "4.4.4, b)).", r"4.4.4, \emph{b)}).", note="'old' still occurs once after the previous item.")
add(32, "proof of (2.7.2), last paragraph: 'Supposons maintenant que L' soit ample pour f''", "'ample' italic", "upright",
    "italics", "soit ample pour $f'$~;", r"soit \emph{ample} pour $f'$~;")
bold(32, "proof of (2.7.2), last paragraph", "(II, 4.6.4)", "(II, 4.6.4)", r"(\textbf{II}, 4.6.4)")
bold(32, "proof of (2.7.2), last paragraph", "(II, 4.6.13)", "(II, 4.6.13)", r"(\textbf{II}, 4.6.13)")

# ---------------- page 33 ----------------
bold(33, "proof of (2.7.2), l. 2: 'critère de (II, 4.6.8, c))'", "(II, 4.6.8, c))", "(II, 4.6.8", r"(\textbf{II}, 4.6.8")
add(33, "proof of (2.7.2), l. 2: 'critère de (II, 4.6.8, c))'", "italic 'c)' then the roman ')' (enlarged crop)",
    "upright c)", "italics", ", c)).", r", \emph{c)}).")
add(33, "proof of (2.7.2): 'si σ : f^*(f_*(F⊗L^{⊗n})) → F⊗L^{⊗n} est l'homomorphisme canonique'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"\sigma:f^*(f_*(\mathcal F\otimes\mathcal L^{\otimes n}))" + NL
    + r"\longrightarrow\mathcal F\otimes\mathcal L^{\otimes n}" + NL + r"\]" + NL,
    r"$\sigma:f^*(f_*(\mathcal F\otimes\mathcal L^{\otimes n}))" + NL
    + r"\to\mathcal F\otimes\mathcal L^{\otimes n}$" + NL)
add(33, "proof of (2.7.2): 'tenant compte de (0_I, 4.3.3.1)'", "(0_I, 4.3.3.1) with a bold 0", "plain 0", "convention",
    r"$(0_{\mathrm I},4.3.3.1)$", r"$(\mathbf{0}_{\mathrm I},4.3.3.1)$", conv=2)
add(33, "proof of (2.7.2): 'désignant par u l'homomorphisme canonique g^*(f_*(F⊗L^{⊗n})) → f'_*(F'⊗L'^{⊗n}). Or,'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"g^*(f_*(\mathcal F\otimes\mathcal L^{\otimes n}))" + NL
    + r"\longrightarrow f'_*(\mathcal F'\otimes\mathcal L'^{\otimes n})." + NL + r"\]" + NL,
    r"$g^*(f_*(\mathcal F\otimes\mathcal L^{\otimes n}))" + NL
    + r"\to f'_*(\mathcal F'\otimes\mathcal L'^{\otimes n})$." + NL)
add(33, "heading of Remarques (2.7.3)", "'Remarques (2.7.3). —' (plural)", "\\begin{remark}[2.7.3] prints 'Remarque (2.7.3)'",
    "word", r"\begin{remark}[2.7.3]", r"\begin{remarks}[2.7.3]",
    note="Apply together with the \\end{remark} -> \\end{remarks} edit at the end of (2.7.3) on this page.")
add(33, "Remarques (2.7.3), (i): 'quasi-compact et quasi-fidèlement plat (2.3.3)'",
    "'quasi-fidèlement plat' italic in the roman remark", "no \\emph", "italics",
    "quasi-fidèlement plat (2.3.3)", r"\emph{quasi-fidèlement plat} (2.3.3)")
add(33, "Remarques (2.7.3), (ii): 'que f soit propre et f' projectif sans que f soit quasi-projectif.'",
    "italic from 'f soit propre' to 'quasi-projectif' (enlarged crop)", "no \\emph", "italics",
    "que $f$ soit propre et $f'$ projectif sans que $f$ soit quasi-projectif.",
    r"que \emph{$f$ soit propre et $f'$ projectif sans que $f$ soit quasi-projectif}.")
add(33, "Remarques (2.7.3), (ii): 'schémas algébriques réguliers (0_I, 4.1.4)'", "(0_I, 4.1.4) with a bold 0", "plain 0",
    "convention", r"$(0_{\mathrm I},4.1.4)$", r"$(\mathbf{0}_{\mathrm I},4.1.4)$", conv=2)
bold(33, "Remarques (2.7.3), (ii)", "(I, 5.5.10)", "(I, 5.5.10)", r"(\textbf{I}, 5.5.10)")
bold(33, "Remarques (2.7.3), (ii)", "(II, 5.5.6)", "(II, 5.5.6)", r"(\textbf{II}, 5.5.6)")
add(33, "Remarques (2.7.3), (ii): 'n'est pas de la forme g'^*(L) pour un O_X-Module inversible L, en vertu de'",
    "italic from 'n'est pas' to the second L", "no \\emph", "italics",
    "n'est pas de la forme" + NL + r"$g'^*(\mathcal L)$ pour un $\mathcal O_X$-Module inversible $\mathcal L$, en",
    r"\emph{n'est pas de la forme" + NL + r"$g'^*(\mathcal L)$ pour un $\mathcal O_X$-Module inversible $\mathcal L$}, en")
add(33, "Remarques (2.7.3), (iii): 'soit un isomorphisme local sans que'", "'isomorphisme local' italic", "no \\emph",
    "italics", "un isomorphisme local sans", r"un \emph{isomorphisme local} sans")
add(33, "end of Remarques (2.7.3)", "plural heading 'Remarques (2.7.3)'", "\\end{remark}", "word",
    r"\end{enumerate}" + NL + r"\end{remark}", r"\end{enumerate}" + NL + r"\end{remarks}",
    note="Apply together with the \\begin{remark}[2.7.3] -> \\begin{remarks}[2.7.3] edit on this page.")
add(33, "heading 2.8", "title ends with a full stop: '... de la fibre générique.'", "no full stop in the \\subsection title",
    "punctuation", "fermé de la fibre générique}", "fermé de la fibre générique.}", note="GLOBAL_ISSUES item 43 pattern.")

# ---------------- page 34 ----------------
add(34, "Proposition (2.8.1): 'l'homomorphisme composé (0_I, 4.4.3.2)'", "(0_I, 4.4.3.2) with a bold 0", "plain 0",
    "convention", r"$(0_{\mathrm I},4.4.3.2)$", r"$(\mathbf{0}_{\mathrm I},4.4.3.2)$", conv=2)
add(34, "proof of (2.8.1), l. 1: 'Comme i_* est quasi-compact et quasi-séparé'",
    "'i_*' with a subscript star (enlarged crop)", "$i$", "misprint_in_print",
    "Comme $i$ est quasi-compact", r"Comme $i_*$ est quasi-compact", corrected="Comme $i$ est quasi-compact",
    note="The morphism i is quasi-compact and quasi-separated (1.1.2, 1.2.2); the print's i_* is a misprint, silently corrected in the TeX.")
add(34, "proof of (2.8.1): 'on a (i_*(H'))|U = (i|U∩X_η)_*(H'|U∩X_η) par définition'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"(i_*(\mathcal H'))|U=(i|U\cap X_\eta)_*(\mathcal H'|U\cap X_\eta)" + NL + r"\]" + NL,
    r"$(i_*(\mathcal H'))|U=(i|U\cap X_\eta)_*(\mathcal H'|U\cap X_\eta)$" + NL)
add(34, "proof of (2.8.1): 'par définition (0_I, 3.4.1)'", "(0_I, 3.4.1) with a bold 0", "plain 0", "convention",
    r"$(0_{\mathrm I},3.4.1)$", r"$(\mathbf{0}_{\mathrm I},3.4.1)$", conv=2)
add(34, "Lemme (2.8.1.1): 'anneau noethérien régulier (0, 17.3.6)'", "(0, 17.3.6) with a bold 0", "plain 0", "convention",
    r"$(0,17.3.6)$", r"$(\mathbf{0},17.3.6)$", conv=2)
add(34, "proof of (2.8.1.1): 'sans torsion (0_I, 6.3.4)'", "(0_I, 6.3.4) with a bold 0", "plain 0", "convention",
    r"$(0_{\mathrm I},6.3.4)$", r"$(\mathbf{0}_{\mathrm I},6.3.4)$", conv=2)
add(34, "proof of (2.8.1.1): 'N→N_(K)=N⊗_A K est injectif.'", "'injectif' italic", "upright", "italics",
    "K$ est injectif.", r"K$ est \emph{injectif}.")
add(34, "proof of (2.8.1.1): the square M→N, M_(K)→N_(K)", "no full stop after N_(K) (enlarged crop)",
    "'N_{(K)}.' inside the diagram", "extra", "N_{(K)}." + NL + "}", "N_{(K)}" + NL + "}")
add(34, "Corollaire (2.8.2), l. 1: 'Sous les conditions de (2.8.1)'", "(2.8.1) upright inside the italic statement",
    "italic (corollary environment)", "convention", "de (2.8.1), pour", r"de \textup{(2.8.1)}, pour", conv=6)
add(34, "Corollaire (2.8.2): 'l'homomorphisme canonique F→i_*(F_η)=i_*(i^*(F)) soit injectif'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"\[" + NL + r"\mathcal F\longrightarrow i_*(\mathcal F_\eta)=i_*(i^*(\mathcal F))" + NL + r"\]" + NL,
    r"$\mathcal F\to i_*(\mathcal F_\eta)=i_*(i^*(\mathcal F))$" + NL)

# ---------------- verification ----------------
marker = re.compile(r"\\oldpage\[IV-2\]\{(\d+)\}")
rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(rel)]
ok = True
for p in sorted({x["page"] for x in F}):
    page_txt = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    i = [k for k, (n, s) in enumerate(cuts) if n == p]
    assert len(i) == 1, (p, i)
    seg = rel[cuts[i[0]][1]:cuts[i[0] + 1][1]]
    body = page_txt.split("\n", 1)[1]  # drop the '% from' line
    if body.rstrip() != seg.rstrip():
        print(f"p. {p}: page file differs from the release segment")
    for name, txt in (("page", page_txt), ("release", seg)):
        cur = txt
        for x in F:
            if x["page"] != p or not x["fix"]:
                continue
            o, n_ = x["fix"]["old"], x["fix"]["new"]
            c0 = txt.count(o)
            c = cur.count(o)
            if c != 1:
                ok = False
                print(f"[{name}] p. {p}: old occurs {c} times at its turn: {o!r}")
            elif c0 != 1:
                print(f"[{name}] p. {p}: (note) old occurs {c0} times in the original text: {o!r}")
            cur = cur.replace(o, n_)
    # corrected-edition replay: skip misprints, apply the rest in order to the original text
    cur = seg
    for x in F:
        if x["page"] != p or not x["fix"] or x["kind"] == "misprint_in_print":
            continue
        if cur.count(x["fix"]["old"]) != 1:
            ok = False
            print(f"[replay] p. {p}: {x['fix']['old']!r}")
        cur = cur.replace(x["fix"]["old"], x["fix"]["new"])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in sorted({x["page"] for x in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("ALL OK" if ok else "PROBLEMS", len(F))
