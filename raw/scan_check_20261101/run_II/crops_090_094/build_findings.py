"""Build findings_090_094.json (EGA II pp. 90-94), check every fix, and dry-run the coordinator's apply logic
in memory on the current release source. Nothing but the findings JSON is written."""
import json
import pathlib
import re
import sys

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
OUT = RUN / "findings_090_094.json"
NL = "\u00b6"  # pilcrow stands for a line break inside old/new strings


def N(s):
    return None if s is None else s.replace(NL, "\n")


findings = []


def F(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=N(old), new=N(new)))
    if kind == "misprint_in_print":
        d["corrected"] = N(corrected)
    d["note"] = note
    findings.append(d)


def IT(page, where, scan, old, new, note=""):
    F(page, where, scan, "upright", "italics", None, "high", old, new, note)


def C2(page, where, old, new):
    F(page, where, "bold chapter number", "plain", "convention", 2, "high", old, new, "")


PB = "Spurious paragraph break at the page marker (GLOBAL_ISSUES item 20)."

# ---------------------------------------------------------------- page 90
F(90, "top of page: 'l'assertion résulte alors de (4.5.2, b))'",
  "the sentence of the proof of (4.6.3) continues from p. 89 ('on peut supposer Y affine et ℒ ample;'); "
  "the line is not indented",
  r"blank lines before and after \oldpage[II]{90} start a new paragraph",
  "other", None, "high",
  r"\oldpage[II]{90}¶¶l'assertion", r"\oldpage[II]{90}¶l'assertion",
  PB + r" This removes the blank line after the marker; the blank line before it (end of the p. 89 segment) "
  r"was already removed by the p. 89 entry in FIXLOG.jsonl.")
IT(90, "proof of (4.6.3): 'résulte alors de (4.5.2, b))'", "'b)' italic",
   r"{4.5.2, b)}). Il est", r"{4.5.2, \emph{b)}}). Il est")
IT(90, "proof of (4.6.3): 'Il est clair que b) entraîne b')'", "'b)' and 'b')' italic",
   r"clair que b) entraîne b')", r"clair que \emph{b)} entraîne \emph{b')}")
IT(90, "proof of (4.6.3): 'pour prouver que b') entraîne a)'", "'b')' and 'a)' italic",
   r"prouver que b') entraîne a)", r"prouver que \emph{b')} entraîne \emph{a)}")
IT(90, "proof of (4.6.3): 'le critère (4.5.2, b'))'", "'b')' italic",
   r"{4.5.2, b')}", r"{4.5.2, \emph{b')}}")
IT(90, "proof of (4.6.3): 'le critère (4.5.2, c)) montre'", "'c)' italic",
   r"{4.5.2, c)}", r"{4.5.2, \emph{c)}}")
IT(90, "after (4.6.4): 'La condition b) est en effet locale sur Y.'", "'b)' italic",
   r"La condition b) est", r"La condition \emph{b)} est")
IT(90, "proof of (4.6.6): 'des critères (4.6.3, b))'", "'b)' italic",
   r"{4.6.3, b)}", r"{4.6.3, \emph{b)}}")
IT(90, "proof of (4.6.6): 'et (4.5.2, b)), car ici'", "'b)' italic",
   r"{4.5.2, b)}), car ici", r"{4.5.2, \emph{b)}}), car ici")
IT(90, "proof of (4.6.7): 'du critère (4.5.2, a))'", "'a)' italic",
   r"{4.5.2, a)}", r"{4.5.2, \emph{a)}}")
IT(90, "proof of (4.6.8): 'Pour démontrer la condition c) lorsque'", "'c)' italic",
   r"la condition c) lorsque", r"la condition \emph{c)} lorsque")
IT(90, "proof of (4.6.8): 'un entier n_i tel que c) ait lieu'", "'c)' italic",
   r"tel que c) ait lieu", r"tel que \emph{c)} ait lieu")
IT(90, "proof of (4.6.8): 'pour obtenir c) pour Y, X et ℒ'", "'c)' italic",
   r"pour obtenir c) pour", r"pour obtenir \emph{c)} pour")
IT(90, "proof of (4.6.8): 'la condition c) découle de'", "'c)' italic",
   r"la condition c)¶découle", r"la condition \emph{c)}¶découle")
IT(90, "proof of (4.6.8): 'découle de (4.5.5, d))'", "'d)' italic",
   r"{4.5.5, d)}", r"{4.5.5, \emph{d)}}")
IT(90, "proof of (4.6.8): 'Il est trivial que c) entraîne c')'", "'c)' and 'c')' italic",
   r"trivial que c) entraîne c')", r"trivial que \emph{c)} entraîne \emph{c')}")
IT(90, "proof of (4.6.8): 'pour prouver que c') implique'", "'c')' italic",
   r"prouver que c') implique", r"prouver que \emph{c')} implique")
IT(90, "proof of (4.6.8), last line: 'et l'hypothèse c') entraîne que'", "'c')' italic",
   r"l'hypothèse c')", r"l'hypothèse \emph{c')}")
C2(90, "proof of (4.6.8): '(I, 9.4.7)'", r"{I, 9.4.7}", r"{\textbf{I}, 9.4.7}")
F(90, "proof of (4.6.8), last two lines: 'est la restriction d'un faisceau cohérent d'idéaux de type fini de 𝒪_X "
      "(I, 9.4.7)'",
  "faisceau cohérent d'idéaux de type fini", "keeps the printed reading",
  "misprint_in_print", None, "medium", None, None,
  "The TeX keeps the printed reading. (I, 9.4.7) extends a quasi-coherent sub-Module of finite type to a "
  "quasi-coherent sub-Module of finite type of 𝒪_X, not to a coherent one, and c') is stated for quasi-coherent "
  "ideals of finite type; 'cohérent ... de type fini' is also redundant. Not in the errata of EGA II "
  "(ega2-errata-addenda-fr.tex) or EGA III (ega3-7-fr.tex).",
  corrected="faisceau quasi-cohérent d'idéaux de type fini")
F(90, "end of page: '... et l'hypothèse c') entraîne que' (the sentence continues on p. 91)",
  "no paragraph break: p. 91 begins mid-sentence, not indented",
  r"blank line before \oldpage[II]{91}",
  "other", None, "high",
  r"entraîne que¶¶", r"entraîne que¶",
  PB + r" Goes with the p. 91 entry that removes the blank line after \oldpage[II]{91}; either alone leaves "
  r"the break.")

# ---------------------------------------------------------------- page 91
F(91, "top of page: '𝒥_i⊗(ℒ^{⊗n}|f^{-1}(U_i)) est engendré'",
  "continues the sentence from p. 90; the line is not indented",
  r"blank line after \oldpage[II]{91} starts a new paragraph",
  "other", None, "high",
  r"\oldpage[II]{91}¶¶$\mathcal{J}_i", r"\oldpage[II]{91}¶$\mathcal{J}_i",
  PB + " Goes with the p. 90 entry that removes the blank line before the marker.")
C2(91, "proof of (4.6.8): '(compte tenu de (I, 9.2.2)'", r"{I, 9.2.2}", r"{\textbf{I}, 9.2.2}")
IT(91, "proof of (4.6.8): 'il suffit donc d'appliquer le critère (4.5.5, d''))'", "'d'')' italic",
   r"{4.5.5, d'')}", r"{4.5.5, \emph{d'')}}")
IT(91, "proof of (4.6.11): 'il y a un recouvrement fini (U_i) de Y'", "'fini' italic",
   r"recouvrement fini¶$(U_i)$", r"recouvrement \emph{fini}¶$(U_i)$", "Checked on a crop.")
IT(91, "proof of (4.6.11): 'Inversement, d') entraîne déjà'", "'d')' italic",
   r"Inversement, d') entraîne", r"Inversement, \emph{d')} entraîne")
F(91, "Proposition (4.6.13), item label '(i bis)'",
  "'(i' and ')' upright, 'bis' italic", r"\rm{(i bis)}: all upright",
  "italics", None, "high",
  r"\item[\rm{(i bis)}]", r"\item[\rm{(i \textit{bis})}]",
  "Checked on a crop. The references to (i bis) on pp. 92 and 94 print the same italic bis.")

# ---------------------------------------------------------------- page 92 (marker entry A comes after the others)
IT(92, "proof of (4.6.13): 'se dérivent de (i), (i bis) et (iv)'", "'bis' italic",
   r"(i bis) et (iv)", r"(i \emph{bis}) et (iv)", "Checked on a crop.")
F(92, "proof of (4.6.13): 'L'assertion (i) est trivialement conséquence de (4.4.10, (i) et (4.6.2).'",
  "(4.4.10, (i) et (4.6.2): no closing parenthesis after (i)",
  "silently corrects to (4.4.10, (i)) [and adds 'de', see the next entry]",
  "misprint_in_print", None, "high",
  r"{4.4.10, (i)})", r"{4.4.10, (i)}",
  "The TeX silently corrects the missing parenthesis; the fix restores the printed reading. Checked on a crop. "
  "Independent of the 'et de' entry (non-overlapping strings). Not in the errata of EGA II or EGA III.",
  corrected=r"(\hyperref[II.4.4.10-fr]{4.4.10, (i)}) et (\hyperref[II.4.6.2-fr]{4.6.2})")
F(92, "proof of (4.6.13): '(4.4.10, (i) et (4.6.2)'", "'et (4.6.2)'", "'et de (4.6.2)'",
  "extra", None, "high",
  r" et de¶(\hyperref[II.4.6.2-fr]", r" et¶(\hyperref[II.4.6.2-fr]", "Checked on a crop.")
IT(92, "proof of (4.6.13): 'Pour démontrer (i bis), (iii) et (iv)'", "'bis' italic",
   r"Pour démontrer (i bis)", r"Pour démontrer (i \emph{bis})", "Checked on a crop.")
R6 = "Checked on a crop."
F(92, "Lemme (4.6.13.1), (ii): 'ℒ (resp. ℒ') un 𝒪_Z-Module'", "'(resp. ℒ')' upright",
  r"italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp.¶  $\mathcal{L}'$)", r"\textup{(resp.¶  $\mathcal{L}'$)}", R6)
F(92, "Lemme (4.6.13.1), (ii): '(resp. un 𝒪_{Z'}-Module) inversible'",
  "'(resp.' and ')' upright, 'un' and 'Module' italic",
  r"all italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp. un¶  $\mathcal{O}_{Z'}$-Module)", r"\textup{(resp.} un¶  $\mathcal{O}_{Z'}$-Module\textup{)}", R6)
F(92, "Lemme (4.6.13.1), (ii): 't (resp. t') une section'", "'(resp. t')' upright",
  r"italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp. $t'$)", r"\textup{(resp. $t'$)}", R6)
F(92, "Lemme (4.6.13.1), (ii): 'une section de ℒ (resp. ℒ') au-dessus'", "'(resp. ℒ')' upright",
  r"italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp. $\mathcal{L}'$)", r"\textup{(resp. $\mathcal{L}'$)}", R6)
F(92, "Lemme (4.6.13.1), (ii): 'au-dessus de Z (resp. Z')'", "'(resp. Z')' upright",
  r"italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp. $Z'$)", r"\textup{(resp. $Z'$)}", R6)
F(92, "Lemme (4.6.13.1), (ii): 's (resp. s') la section'", "'(resp. s')' upright",
  r"italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp. $s'$)", r"\textup{(resp. $s'$)}", R6)
F(92, "Lemme (4.6.13.1), (ii): 'p*(ℒ) (resp. p'*(ℒ'))'", "'(resp. p'*(ℒ'))' upright",
  r"italic (inside the \itshape lemma environment)", "convention", 6, "high",
  r"(resp.¶  $p'^*(\mathcal{L}')$)", r"\textup{(resp.¶  $p'^*(\mathcal{L}')$)}", R6)
C2(92, "proof of (4.6.13.1): 'résulte alors aussitôt de (I, 1.2.2.2)'", r"{I, 1.2.2.2}", r"{\textbf{I}, 1.2.2.2}")
IT(92, "proof of (4.6.13): 'Démontrons alors (i bis).'", "'bis' italic",
   r"Démontrons alors (i bis)", r"Démontrons alors (i \emph{bis})", "Checked on a crop.")
IT(92, "proof of (4.6.13), (i bis): 'base de la topologie de X (4.5.2, a)), donc par'", "'a)' italic",
   r"{4.5.2, a)}), donc par", r"{4.5.2, \emph{a)}}), donc par")
IT(92, "proof of (4.6.13), (i bis): 'et par (4.5.2, a)) que j*(ℒ) est ample'", "'a)' italic",
   r"{4.5.2, a)}) que $j^*", r"{4.5.2, \emph{a)}}) que $j^*")
IT(92, "proof of (4.6.13), (iii): 'les X_s recouvrent X (4.5.2, a')), donc'", "'a')' italic",
   r"{4.5.2, a')})~; donc", r"{4.5.2, \emph{a')}})~; donc")
IT(92, "proof of (4.6.13), (iii): 'et de (4.5.2, a')) que ℒ' est ample'", "'a')' italic",
   r"{4.5.2, a')}) que $\mathcal{L}'$", r"{4.5.2, \emph{a')}}) que $\mathcal{L}'$")
C2(92, "proof of (4.6.13), (iii): 'étant quasi-compact (I, 6.6.4, (iii))'",
   r"{I, 6.6.4, (iii)}", r"{\textbf{I}, 6.6.4, (iii)}")
C2(92, "proof of (4.6.13), (iv): 'est quasi-compact (I, 6.6.4, (iv))'",
   r"{I, 6.6.4, (iv)}", r"{\textbf{I}, 6.6.4, (iv)}")
C2(92, "proof of (4.6.13), (iv): '((4.6.4) et (I, 3.2.7))'", r"{I, 3.2.7}", r"{\textbf{I}, 3.2.7}")
IT(92, "proof of (4.6.13), (iv): 'soit affine (4.5.2, a')). D'ailleurs'", "'a')' italic",
   r"{4.5.2, a')}). D'ailleurs", r"{4.5.2, \emph{a')}}). D'ailleurs")
IT(92, "proof of (4.6.13), (iv): 'et de (4.5.2, a')) que ℒ_1⊗_S ℒ_2'", "'a')' italic",
   r"{4.5.2, a')}) que¶$\mathcal{L}_1", r"{4.5.2, \emph{a')}}) que¶$\mathcal{L}_1")
F(92, "end of page: '... il existe un nombre fini de sections s_i∈Γ(Y, 𝒦^{⊗k_i}) telles que les Y_{s_i}' "
      "(continues on p. 93)",
  "no paragraph break: p. 93 begins mid-sentence ('soient affines'), not indented",
  r"blank line before \oldpage[II]{93}",
  "other", None, "high",
  r"telles que les $Y_{s_i}$¶¶", r"telles que les $Y_{s_i}$¶",
  PB + r" Goes with the p. 93 entry that removes the blank line after \oldpage[II]{93}.")

# ---------------------------------------------------------------- marker 92: A (page 92) then B (page 91)
F(92, "top of page: printed p. 92 begins inside (4.6.13, (v)) with '𝒪_X-Module ℒ est ample relativement à g∘f'",
  "p. 91 ends '(v) Soient f : X→Y, g : Y→Z deux morphismes tels que g∘f soit quasi-compact. Si un'; p. 92 begins "
  "'𝒪_X-Module ℒ est ample relativement à g∘f, et si g est séparé ...', then (vi)",
  r"\oldpage[II]{92} stands after the whole of (v), before (vi)",
  "marker", None, "high",
  r"\oldpage[II]{92}¶¶  \item[\rm{(vi)}]", r"\item[\rm{(vi)}]",
  "Removes the misplaced marker; the next entry (page 91) inserts it after 'Si un'. Apply the two together, this "
  "one first: while both markers exist, the page-92 segment ends at the old marker and the page-92 edits fail. "
  "All other page-92 entries precede this one in the file.")
F(91, "Proposition (4.6.13), (v): 'Si un 𝒪_X-Module ℒ est ample relativement à g∘f'",
  "printed page 92 begins at '𝒪_X-Module' (p. 91 ends with 'Si un')",
  r"no marker here; \oldpage[II]{92} stands before (vi)",
  "marker", None, "high",
  r"quasi-compact. Si un $\mathcal{O}_X$-Module", r"quasi-compact. Si un¶  \oldpage[II]{92}¶  $\mathcal{O}_X$-Module",
  "Inserts the page-92 marker where the printed page begins. Apply after the previous entry (page 92), which "
  "removes the old marker; once that marker is gone this string is unique in the page-91 segment.")

# ---------------------------------------------------------------- page 93
F(93, "top of page: 'soient affines et recouvrent Y'",
  "continues the sentence from p. 92; the line is not indented",
  r"blank line after \oldpage[II]{93} starts a new paragraph",
  "other", None, "high",
  r"\oldpage[II]{93}¶¶soient", r"\oldpage[II]{93}¶soient",
  PB + " Goes with the p. 92 entry that removes the blank line before the marker.")
IT(93, "proof of (4.6.13), (ii), first line: 'soient affines et recouvrent Y'", "'affines' italic",
   r"affines et recouvrent $Y$", r"\emph{affines} et recouvrent $Y$", "Checked on a crop.")
IT(93, "proof of (4.6.13), (ii): 'recouvrent Y (4.5.2, a')); remplaçant'", "'a')' italic",
   r"{4.5.2, a')})~;¶remplaçant", r"{4.5.2, \emph{a')}})~;¶remplaçant")
F(93, "proof of (4.6.13), (ii): 'X_{s'_i}=f^{-1}(Y_{s_i}) (4.6.1.13, (i)) recouvrent X'",
  "(4.6.1.13, (i))", "keeps the printed reading (plain text, no link)",
  "misprint_in_print", None, "high", None, None,
  "The TeX keeps the printed reading. The result used is Lemme (4.6.13.1), (i) on p. 92 (Z_{s'} = u^{-1}(S_s)); "
  "there is no (4.6.1.13). Checked on a crop. Not in the errata of EGA II or EGA III.",
  corrected=r"(\hyperref[II.4.6.13.1-fr]{4.6.13.1, (i)})")
F(93, "proof of (4.6.13), (ii): 'Comme ℒ|X_{s'_i} est ample (4.6.4 et 4.6.6)'",
  "one pair of parentheses: (4.6.4 et 4.6.6)", "((4.6.4) et (4.6.6))",
  "punctuation", None, "high",
  r"((\hyperref[II.4.6.4-fr]{4.6.4}) et¶(\hyperref[II.4.6.6-fr]{4.6.6}))",
  r"(\hyperref[II.4.6.4-fr]{4.6.4} et¶\hyperref[II.4.6.6-fr]{4.6.6})",
  "Checked on a crop. Same form as the '(1.1.2 et 1.1.3)' reference of p. 9.")
IT(93, "proof of (4.6.13), (ii): 'recouvrent X_{s'_i} (4.5.2, a')); on peut d'ailleurs'", "'a')' italic",
   r"{4.5.2, a')})~; on peut", r"{4.5.2, \emph{a')}})~; on peut")
F(93, "proof of (4.6.13), (ii), display: 'u_{ij}∈Γ(X, ℒ^{⊗n}⊗_X f*(𝒦^{⊗mk}))'",
  "⊗ with subscript X", "⊗ without subscript",
  "formula", None, "high",
  r"\mathcal{L}^{\otimes n}\otimes¶  f^*", r"\mathcal{L}^{\otimes n}\otimes_X¶  f^*",
  "Checked on a 3x crop.")
C2(93, "proof of (4.6.13), (ii): 'de u_{ij} (I, 9.3.1)'", r"{I, 9.3.1}", r"{\textbf{I}, 9.3.1}")
IT(93, "proof of (4.6.13), (ii): 'on voit donc (4.5.2, a')) que'", "'a')' italic",
   r"{4.5.2, a')}) que", r"{4.5.2, \emph{a')}}) que")
IT(93, "proof of (4.6.13), (ii): 'a fortiori, f*(𝒦^{⊗h}) est engendré'", "'a fortiori' italic",
   r"~; a fortiori,", r"~; \emph{a fortiori},", "Checked on a crop.")
F(93, "proof of (4.6.13), (ii): 'par définition des images réciproques (0, 3.7.1 et 4.4.1)'",
  "one pair of parentheses: (0, 3.7.1 et 4.4.1)", "((0, 3.7.1) et (4.4.1))",
  "punctuation", None, "high",
  r"((\hyperref[0.3.7.1-fr]", r"(\hyperref[0.3.7.1-fr]",
  "Checked on a crop. Removes the outer opening parenthesis; the next entry removes the inner ones and fixes the "
  "link. Apply both. Independent of the bold-0 entry.")
F(93, "proof of (4.6.13), (ii): '(0, 3.7.1 et 4.4.1)'",
  "4.4.1 is part of the chapter-0 reference: (0, 4.4.1)",
  "(4.4.1) in its own parentheses, linked to II.4.4.1-fr",
  "other", None, "high",
  r"3.7.1}) et¶(\hyperref[II.4.4.1-fr]{4.4.1}))", r"3.7.1} et¶\hyperref[0.4.4.1-fr]{4.4.1})",
  "The TeX turns the second number into a reference to EGA II (4.4.1); the print means (0, 4.4.1), the inverse "
  "image of a Module (label 0.4.4.1-fr in ega0-1-fr.tex). Goes with the previous entry; independent of the "
  "bold-0 entry.")
C2(93, "proof of (4.6.13), (ii): '(0, 3.7.1 et 4.4.1)'", r"{0, 3.7.1}", r"{\textbf{0}, 3.7.1}")
F(93, "Remarque (4.6.14): 'tout 𝒪_X-Module inversible serait ample pour f'",
  "'tout' italic in the roman remark", "upright word in the (italic) remark environment",
  "italics", None, "high",
  r"identique, tout $\mathcal{O}_X$-Module", r"identique, \emph{tout} $\mathcal{O}_X$-Module",
  "Checked on a crop. Judged with the remark body as roman (document-wide remark issue).")
C2(93, "proof of (4.6.16): 'nilpotent d'idéaux (I, 6.1.6)'", r"{I, 6.1.6}", r"{\textbf{I}, 6.1.6}")
F(93, "Proposition (4.6.17): 'étant celles de (4.4.11), pour que'", "the reference (4.4.11) upright",
  r"italic (inside the \itshape proposition environment)", "convention", 6, "high",
  r"(\hyperref[II.4.4.11-fr]{4.4.11})", r"\textup{(\hyperref[II.4.4.11-fr]{4.4.11})}", "Checked on a crop.")

# ---------------------------------------------------------------- page 94
IT(94, "proof of (4.6.17): 'résulte de (4.6.13, (i bis))'", "'bis' italic",
   r"{4.6.13, (i bis)}", r"{4.6.13, (i \emph{bis})}", "Checked on a crop.")
IT(94, "proof of (4.6.17): 'résulte du critère (4.5.2, a))'", "'a)' italic",
   r"{4.5.2, a)}", r"{4.5.2, \emph{a)}}")
F(94, "proof of (4.6.18): 'la proposition résulte alors de (4.4.3) et (4.6.2)'", "'et (4.6.2)'", "'et de (4.6.2)'",
  "extra", None, "high",
  r"{4.4.3}) et de¶", r"{4.4.3}) et¶", "Checked on a crop.")
F(94, "heading of § 5: 'MORPHISMES QUASI-AFFINES; MORPHISMES QUASI-PROJECTIFS / MORPHISMES PROPRES; "
      "MORPHISMES PROJECTIFS'",
  "no punctuation between QUASI-PROJECTIFS (end of the first heading line) and MORPHISMES PROPRES",
  "silently inserts a period: 'morphismes quasi-projectifs. Morphismes propres'",
  "misprint_in_print", None, "medium",
  r"quasi-projectifs. Morphismes¶propres", r"quasi-projectifs morphismes¶propres",
  "Checked on a crop. The table of contents of the volume reads 'morphismes quasi-projectifs; morphismes propres' "
  "(ega2-indexes-and-contents-fr.tex), so the heading lost its semicolon at the line break; the TeX's period "
  "matches neither. Diplomatic: no punctuation, lower-case 'morphismes' as after the other separators; corrected "
  "edition: semicolon. Medium: the omission could be a display convention rather than a misprint.",
  corrected=r"morphismes quasi-projectifs~; morphismes propres")
D6 = (r"Checked on a crop: the defined term is in the same italic as the rest of the definition; \emph inside "
      r"the \itshape definition environment makes it upright. Drop the \emph.")
F(94, "Définition (5.1.1): 'On appelle schéma quasi-affine un schéma'", "no change of face",
  r"\emph{schéma quasi-affine} (upright)", "convention", 6, "high",
  r"\emph{schéma quasi-affine}", r"schéma quasi-affine", D6)
F(94, "Définition (5.1.1): 'est quasi-affine, ou encore que X'", "no change of face",
  r"\emph{quasi-affine} (upright)", "convention", 6, "high",
  r"\emph{quasi-affine}", r"quasi-affine", D6)
F(94, "Définition (5.1.1): 'est un Y-schéma quasi-affine, s'il existe'", "no change of face",
  r"\emph{$Y$-schéma quasi-affine} (upright)", "convention", 6, "high",
  r"\emph{$Y$-schéma quasi-affine}", r"$Y$-schéma quasi-affine", D6)
C2(94, "after (5.1.1): 'séparé (I, 5.5.5 et 5.5.8)'", r"{I, 5.5.5}", r"{\textbf{I}, 5.5.5}")
C2(94, "after (5.1.1): 'quasi-compact (I, 6.6.1)'", r"{I, 6.6.1}", r"{\textbf{I}, 6.6.1}")
C2(94, "after (5.1.1): 'dit canonique (I, 2.2.4)'", r"{I, 2.2.4}", r"{\textbf{I}, 2.2.4}")
F(94, "Proposition (5.1.2), c): 'très ample relativement à u (4.4.2)'", "the reference (4.4.2) upright",
  r"italic (inside the \itshape proposition environment)", "convention", 6, "high",
  r"(\hyperref[II.4.4.2-fr]{4.4.2})", r"\textup{(\hyperref[II.4.4.2-fr]{4.4.2})}", "Checked on a crop.")
F(94, "Proposition (5.1.2), c'): 'est ample (4.5.1)'", "the reference (4.5.1) upright",
  r"italic (inside the \itshape proposition environment)", "convention", 6, "high",
  r"est ample¶  (\hyperref[II.4.5.1-fr]{4.5.1})", r"est ample¶  \textup{(\hyperref[II.4.5.1-fr]{4.5.1})}",
  "Checked on a crop.")

# ================================================================ checks
ok = True
pages = {}
for n in range(90, 95):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
for i, x in enumerate(findings):
    if "\t" in json.dumps(x, ensure_ascii=False).replace("\\t", ""):
        print("TAB CHARACTER in", i); ok = False
    fx = x["fix"]
    if fx:
        c = pages[x["page"]].count(fx["old"])
        if c != 1:
            ok = False
            print(f"NOT UNIQUE ({c}) p{x['page']} #{i}: {fx['old']!r}")
print("page-file uniqueness:", "all ok" if ok else "FAILURES")

# current release segments equal to the page files?
src = SRC.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def segments(t):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    return cuts


cuts = segments(src)
for k, (n, s) in enumerate(cuts):
    if 90 <= n <= 94:
        seg = src[s:cuts[k + 1][1]]
        body = pages[n].split("\n", 1)[1]
        print(f"source segment {n}:", "identical to page file" if seg == body else "DIFFERS from page file")

# dry run of apply_fixes.py logic, in file order, in memory
t = src
fails = 0
for i, x in enumerate(findings):
    fx = x["fix"]
    if not fx:
        continue
    page = x["page"]
    cs = segments(t)
    loc = None
    for k, (n, s) in enumerate(cs):
        if n == page:
            loc = (s, cs[k + 1][1] if k + 1 < len(cs) else len(t))
            break
    if loc is None:
        print("dry run: page not found", i); fails += 1; continue
    s, e = loc
    seg = t[s:e]
    if seg.count(fx["old"]) != 1:
        print(f"dry run: old occurs {seg.count(fx['old'])} times, p{page} #{i}: {fx['old']!r}"); fails += 1; continue
    t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
print("dry run on current source:", "all applied" if fails == 0 else f"{fails} FAILED")

if "--show" in sys.argv:
    for key in (r"\oldpage[II]{90}", r"\oldpage[II]{91}", r"\oldpage[II]{92}", r"\oldpage[II]{93}"):
        j = t.find(key)
        print("-----", key, "occurrences:", t.count(key))
        print(t[max(0, j - 160):j + 160])
    for key in ("par définition des images réciproques", "{4.4.10, (i)}", "(4.6.1.13", "\\otimes_X\n", "\\item[\\rm{(i \\textit"):
        j = t.find(key)
        print("-----", key); print(t[max(0, j - 80):j + 150])
    j = t.find(r"\section{Morphismes quasi-affines")
    print("-----"); print(t[j:j + 140])

# counts and output
from collections import Counter
cnt = Counter()
for x in findings:
    cat = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], cat)] += 1
print("; ".join(f"p. {p}: {cnt[(p, 'normal')]}/{cnt[(p, 'convention')]}/{cnt[(p, 'misprint')]}" for p in range(90, 95)))
if ok and fails == 0 and "--write" in sys.argv:
    OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT, len(findings), "findings")
