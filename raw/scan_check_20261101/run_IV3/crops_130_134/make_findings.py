"""Build findings_130_134.json and check every fix against page_NNN.tex and the release file segment."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")
OUT = RUN / "findings_130_134.json"

F = []


def add(page, where, scan, tex, kind, old=None, new=None, conv=None, conf="high", note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def bullet(page, anchor, where, note="Raised bullet in the print (gr•); the TeX has ^* (GLOBAL_ISSUES 60 pattern)."):
    assert anchor.count("^*") == 1, anchor
    add(page, where, "gr• (raised bullet)", "^*", "symbol", anchor, anchor.replace("^*", "^\\bullet"), note=note)


def bullet_cov(page, where, by):
    add(page, where, "gr• (raised bullet)", "^*", "symbol", note=f"Covered by the edit of the entry '{by}' (written with ^\\bullet there).")


def frak(page, anchor, where, note=""):
    assert anchor.count("\\mathfrak R") == 1, anchor
    add(page, where, "Fraktur K (𝔎), same glyph as the 𝔎 of 0_IV p. 52 (enlarged crop)", "\\mathfrak R (ℜ)", "symbol",
        anchor, anchor.replace("\\mathfrak R", "\\mathfrak K"),
        note=note or "Wrong letter: \\mathfrak R where the print has a Fraktur K (cf. GLOBAL_ISSUES 63).")


def frak_cov(page, where, by):
    add(page, where, "Fraktur K (𝔎)", "\\mathfrak R", "symbol", note=f"Covered by the edit of the entry '{by}' (written \\mathfrak K there).")


def kbold(page, anchor, where):
    assert anchor.count("k(\\mathfrak p)") == 1, anchor
    add(page, where, "bold italic k in k(𝔭)", "k(\\mathfrak p)", "convention",
        anchor, anchor.replace("k(\\mathfrak p)", "\\boldsymbol{k}(\\mathfrak p)"), conv=1)


def kbold_cov(page, where, by):
    add(page, where, "bold italic k in k(𝔭)", "k(\\mathfrak p)", "convention", conv=1,
        note=f"Covered by the edit of the entry '{by}' (written \\boldsymbol{{k}} there).")


def ker(page, anchor, where):
    assert anchor.count("\\ker(") == 1, anchor
    add(page, where, "Ker (capital K)", "\\ker (prints 'ker')", "word", anchor,
        anchor.replace("\\ker(", "\\operatorname{Ker}("))


# ---------------------------------------------------------------- page 130
P = 130
bullet(P, "Le $C_0$-module $\\operatorname{gr}_{\\mathfrak J_0}^*(M_0)$", "first line: 'Le C_0-module gr•_{J_0}(M_0)'")
add(P, "'de sorte qu'il y a un épimorphisme de C_0-modules gradués u_0 : C_0^r → gr•_{J_0}(M_0).'",
    "the formula u_0 : C_0^r → gr•(M_0). is in the running text, at the end of the line; 'Comme' follows flush left in the same paragraph",
    "displayed \\[ u_0:C_0^r\\longrightarrow\\operatorname{gr}_{\\mathfrak J_0}^*(M_0). \\]", "other",
    "épimorphisme de $C_0$-modules gradués\n\\[\nu_0:C_0^r\\longrightarrow\\operatorname{gr}_{\\mathfrak J_0}^*(M_0).\n\\]\n",
    "épimorphisme de $C_0$-modules gradués\n$u_0:C_0^r\\longrightarrow\\operatorname{gr}_{\\mathfrak J_0}^\\bullet(M_0)$.\n",
    note="Formula displayed where the print has it in the running text. The edit also writes the bullet of gr• (next entry).")
bullet_cov(P, "u_0 : C_0^r → gr•_{J_0}(M_0)", "u_0 display")
bullet(P, "canonique\n$\\operatorname{gr}_{\\mathfrak J_0}^*(M_0)", "'l'homomorphisme canonique gr•_{J_0}(M_0)⊗_{A_0}A'")
bullet(P, "\\to\\operatorname{gr}_{\\mathfrak J}^*(M)$ est surjectif", "'→ gr•_J(M) est surjectif'")
bullet(P, "u_0\\otimes1_A}\n\\operatorname{gr}_{\\mathfrak J_0}^*(M_0)", "display u : C^r → gr•_{J_0}(M_0)⊗_{A_0}A → gr•_J(M), first gr")
bullet(P, "\\longrightarrow\\operatorname{gr}_{\\mathfrak J}^*(M),", "display u, second gr")
ker(P, "$Q=\\ker(u)$", "'le C-module gradué Q = Ker(u) est de type fini'")
frak(P, "soit $\\mathfrak R_0$ un idéal", "Lemme (11.2.9.6), l. 1: 'soit 𝔎_0 un idéal de A_0'")
add(P, "Lemme (11.2.9.6): 'posons A'_0 = A_0/𝔎_0, B'_0 = B_0⊗_{A_0}A'_0 = B_0/𝔎_0B_0, 𝔍'_0 = 𝔍_0B'_0, 𝔎 = 𝔎_0A, A' = A/𝔎, et supposons en outre'",
    "all in the running text, as one list joined by commas; no 'et' before 𝔎 = 𝔎_0A",
    "the first three equalities displayed (\\[ ... \\qquad ... \\]), then 'et $\\mathfrak R=\\mathfrak R_0A$, ...'", "other",
    "posons\n\\[\nA'_0=A_0/\\mathfrak R_0,\\qquad\nB'_0=B_0\\otimes_{A_0}A'_0=B_0/\\mathfrak R_0B_0,\\qquad\n\\mathfrak J'_0=\\mathfrak J_0B'_0,\n\\]\net $\\mathfrak R=\\mathfrak R_0A$, $A'=A/\\mathfrak R$, et supposons",
    "posons\n$A'_0=A_0/\\mathfrak K_0$, $B'_0=B_0\\otimes_{A_0}A'_0=B_0/\\mathfrak K_0B_0$,\n$\\mathfrak J'_0=\\mathfrak J_0B'_0$, $\\mathfrak K=\\mathfrak K_0A$, $A'=A/\\mathfrak K$, et supposons",
    note="Formula displayed where the print has it in the running text (GLOBAL_ISSUES 51 pattern). One edit for: display -> inline, the added 'et' (next entry), and the five Fraktur K of these formulas (entries below).")
add(P, "Lemme (11.2.9.6): '𝔍'_0 = 𝔍_0B'_0, 𝔎 = 𝔎_0A'", "no 'et' before 𝔎 = 𝔎_0A (comma)", "'et $\\mathfrak R=\\mathfrak R_0A$'", "extra",
    note="Covered by the display edit above (connecting word added when the formulas were displayed).")
for w in ("A'_0 = A_0/𝔎_0", "B_0/𝔎_0B_0", "𝔎 = 𝔎_0A (𝔎)", "𝔎 = 𝔎_0A (𝔎_0)", "A' = A/𝔎"):
    frak_cov(P, f"Lemme (11.2.9.6): {w}", "posons A'_0 = A_0/𝔎_0, ... (display -> inline)")
bullet(P, "que $\\operatorname{gr}_{\\mathfrak J'_0}^*(M_0\\otimes_{A_0}A'_0)$ soit un", "Lemme (11.2.9.6): 'que gr•_{J'_0}(M_0⊗A'_0) soit un A'_0-module plat'")
add(P, "Lemme (11.2.9.6): 'q_h (1≤h≤s) de Q'", "parentheses of (1≤h≤s) upright inside the italic statement (enlarged crop)",
    "($1\\leq h\\leq s$): text parentheses, italic in the lemma environment", "convention",
    "($1\\leq h\\leq s$) de $Q$", "\\textup{(}$1\\leq h\\leq s$\\textup{)} de $Q$", conv=6,
    note="Same treatment as (α∈J_{s,i}) on p. 84.")
frak(P, "\\mathfrak p\\supset\\mathfrak RB$ de $B$, les images", "Lemme (11.2.9.6): 'pour tout idéal premier 𝔭 ⊃ 𝔎B de B'")
frak(P, "$\\mathfrak R_0$ étant remplacé", "'𝔎_0 étant remplacé par l'idéal 𝔎_{ik}'")
frak(P, "l'idéal\n$\\mathfrak R_{ik}$ définissant", "'l'idéal 𝔎_{ik} définissant le sous-schéma fermé'")
frak(P, "$\\mathfrak R_{ik}B_{f_{ik}}$. On peut", "'contenant 𝔎_{ik}B_{f_{ik}}. On peut écrire'")
add(P, "'Puisque les S_{0i} recouvrent S_0, tout idéal premier 𝔭 de B'", "'tout' in italics", "roman 'tout'", "italics",
    "recouvrent $S_0$, tout idéal premier", "recouvrent $S_0$, \\emph{tout} idéal premier")
frak(P, "contient $\\mathfrak R_{ik}B_{f_{ik}}$", "'donc l'image 𝔭_{ik} de 𝔭 dans B_{f_{ik}} contient 𝔎_{ik}B_{f_{ik}}'")
add(P, "'(Bourbaki, Alg. comm., chap. II, § 3, n° 3, th. 1)'", "n with a superior letter o (enlarged crop)",
    "n$^\\circ$ (degree sign)", "symbol", "n$^\\circ$~3,", "n\\textsuperscript{o}~3,",
    note="The edition writes n\\textsuperscript{o} (GLOBAL_ISSUES 46c, 57); ega4-11-fr.tex has 29 n$^\\circ$.")
add(P, "'Reste à démontrer le lemme (11.2.9.6). Posons C' = C⊗_A A' = C/𝔎C, B' = B⊗_A A', 𝔍' = 𝔍B', M' = M⊗_A A'. Par hypothèse'",
    "all in the running text; 'Par hypothèse' follows on the same line",
    "displayed \\[ C'=...,\\qquad B'=...,\\qquad \\mathfrak J'=...,\\qquad M'=... . \\]", "other",
    "Posons\n\\[\nC'=C\\otimes_AA'=C/\\mathfrak RC,\\qquad\nB'=B\\otimes_AA',\\qquad \\mathfrak J'=\\mathfrak JB',\\qquad\nM'=M\\otimes_AA'.\n\\]\n",
    "Posons\n$C'=C\\otimes_AA'=C/\\mathfrak KC$, $B'=B\\otimes_AA'$, $\\mathfrak J'=\\mathfrak JB'$,\n$M'=M\\otimes_AA'$.\n",
    note="Formula displayed where the print has it in the running text. The edit also writes the Fraktur K of C/𝔎C (next entry).")
frak_cov(P, "'C' = C⊗_A A' = C/𝔎C'", "Reste à démontrer ... Posons C' = ... (display -> inline)")
bullet(P, "Par hypothèse $\\operatorname{gr}_{\\mathfrak J}^*(M)$", "'Par hypothèse gr•_J(M) est un A-module plat'")
bullet(P, "donc $\\operatorname{gr}_{\\mathfrak J'}^*(M')$ s'identifie", "'donc gr•_{J'}(M') s'identifie à'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(M)\\otimes_AA'$ (11.2.9.2)", "'gr•_J(M)⊗_A A' (11.2.9.2)'")
bullet(P, "Q\\otimes_AA'\\longrightarrow C'^{r}\n\\xrightarrow{u\\otimes1_{A'}}\\operatorname{gr}_{\\mathfrak J'}^*(M')", "(11.2.9.7)")
add(P, "after (11.2.9.7): 'Posons C'_0 = C_0⊗_{A_0}A'_0 = C_0/𝔎_0C_0 et considérons'",
    "'Posons' begins a new indented paragraph after the display",
    "no blank line after \\end{equation}: the text continues the paragraph without indent", "other",
    "\\tag{11.2.9.7}\n\\end{equation}\nPosons", "\\tag{11.2.9.7}\n\\end{equation}\n\nPosons",
    note="Paragraph break after a display (GLOBAL_ISSUES 47 pattern).")
frak(P, "C_0/\\mathfrak R_0C_0$", "'C'_0 = C_0⊗_{A_0}A'_0 = C_0/𝔎_0C_0'")
bullet(P, "\\operatorname{gr}_{\\mathfrak J_0}^*(M_0)\\otimes_{A_0}A'_0", "display u'_0, first gr")
bullet(P, "\\operatorname{gr}_{\\mathfrak J'_0}^*(M_0\\otimes_{A_0}A'_0).\n\\]", "display u'_0, second gr")
ker(P, "$Q_0=\\ker(u'_0)$", "'Soit Q_0 = Ker(u'_0)'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J'_0}^*(M_0\\otimes_{A_0}A'_0)$ est un", "'utilisant le fait que gr•_{J'_0}(M_0⊗A'_0) est un A'_0-module plat'")
add(P, "'est un A'_0-module plat, on voit'", "'plat' in italics", "roman 'plat'", "italics",
    "$A'_0$-module plat, on voit", "$A'_0$-module \\emph{plat}, on voit")
add(P, "'on voit que gr•_{J'_0}(M_0⊗_{A_0}A'_0)⊗_{A'}A' s'identifie à gr•_{J'}(M')'",
    "a formula: gr•_{J'_0}(M_0⊗_{A_0}A'_0)⊗_{A'}A'",
    "the formula is paraphrased in words: 'son produit tensoriel sur $A'_0$ par $A'$'", "word",
    "que son produit tensoriel sur $A'_0$ par $A'$",
    "que $\\operatorname{gr}_{\\mathfrak J'_0}^\\bullet(M_0\\otimes_{A_0}A'_0)\\otimes_{A'_0}A'$",
    note="Restores the printed formula with its correct subscript A'_0; the next entry (misprint) then changes A'_0 to the printed A'. Apply this edit first.")
add(P, "same formula: 'gr•_{J'_0}(M_0⊗_{A_0}A'_0)⊗_{A'}A''",
    "the outer tensor product is printed ⊗_{A'} (prime, no subscript 0; enlarged crop)",
    "the TeX paraphrase 'son produit tensoriel sur $A'_0$ par $A'$' silently gives the correct reading A'_0",
    "misprint_in_print",
    "A'_0)\\otimes_{A'_0}A'$", "A'_0)\\otimes_{A'}A'$", corrected="\\otimes_{A'_0}A'",
    note="Misprint: gr•_{J'_0}(M_0⊗_{A_0}A'_0) is an A'_0-module, not an A'-module; the base change is over A'_0 (cf. Q_0⊗_{A'_0}A' in (11.2.9.8)). 'old' is taken from the text after the previous edit (it is not in page_130.tex until that edit is applied).")
bullet(P, "s'identifie à $\\operatorname{gr}_{\\mathfrak J'}^*(M')$ (11.2.9.2) et", "'s'identifie à gr•_{J'}(M') (11.2.9.2)'")
bullet(P, "Q_0\\otimes_{A'_0}A'\\longrightarrow C'^{r}\n\\xrightarrow{u\\otimes1_{A'}}\\operatorname{gr}_{\\mathfrak J'}^*(M')", "(11.2.9.8)")
add(P, "(11.2.9.8): '0 → Q_0⊗_{A'_0}A' → C'^r → gr•_{J'}(M') → 0,'", "comma at the end of the display (the sentence continues on p. 131: 'd'où, ...')",
    "full stop", "punctuation", "\\longrightarrow0.\n\\label{IV.11.2.9.8-fr}", "\\longrightarrow0,\n\\label{IV.11.2.9.8-fr}")
add(P, "end of page_130.tex, before \\oldpage[IV-3]{131}", "p. 131 begins 'd'où, par comparaison avec (11.2.9.7)' flush left: the sentence continues after (11.2.9.8)",
    "blank line after \\end{equation} at the end of page_130.tex: paragraph break mid-sentence", "marker",
    "\\tag{11.2.9.8}\n\\end{equation}\n\n", "\\tag{11.2.9.8}\n\\end{equation}\n",
    note="Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 131 entry removing the blank line after \\oldpage[IV-3]{131}. The marker itself is in the right place.")

# ---------------------------------------------------------------- page 131
P = 131
add(P, "top of the page: 'd'où, par comparaison avec (11.2.9.7)'", "flush left: continues the sentence of p. 130",
    "\\oldpage[IV-3]{131} followed by a blank line", "marker",
    "\\oldpage[IV-3]{131}\n\nd'où", "\\oldpage[IV-3]{131}\nd'où",
    note="Apply together with the p. 130 entry removing the blank line before the marker.")
add(P, "'un isomorphisme de C'-modules gradués Q⊗_A A' ⥲ Q_0⊗_{A_0}A'.' then 'Comme C'_0 est noethérien'",
    "the isomorphism is in the running text (start of line 2); 'Comme C'_0 est noethérien' begins a new indented paragraph",
    "displayed \\[ ... \\], and 'Comme' continues the paragraph after \\] (no blank line)", "other",
    "gradués\n\\[\nQ\\otimes_AA'\\xrightarrow{\\sim}Q_0\\otimes_{A'_0}A'.\n\\]\nComme $C'_0$",
    "gradués\n$Q\\otimes_AA'\\xrightarrow{\\sim}Q_0\\otimes_{A'_0}A'$.\n\nComme $C'_0$",
    note="One edit for display -> inline and the missing paragraph break (next entry).")
add(P, "'Comme C'_0 est noethérien' (after the isomorphism)", "new indented paragraph", "no blank line", "other",
    note="Covered by the previous edit.")
add(P, "isomorphism 'Q⊗_A A' ⥲ Q_0⊗_{A_0}A''", "subscript A_0 (no prime; enlarged crop), whereas the next line has Q_0⊗_{A'_0}A'",
    "Q_0\\otimes_{A'_0}A'", "formula",
    "\\xrightarrow{\\sim}Q_0\\otimes_{A'_0}A'", "\\xrightarrow{\\sim}Q_0\\otimes_{A_0}A'", conf="high",
    note="Not treated as a misprint: Q_0 is an A'_0-module and A'_0⊗_{A_0}A' = A' (𝔎 = 𝔎_0A), so Q_0⊗_{A_0}A' = Q_0⊗_{A'_0}A'. If the coordinator prefers a misprint (consistency with (11.2.9.8)), the corrected reading is \\otimes_{A'_0}. The 'old' works before or after the previous edit.")
frak(P, "\\supset\\mathfrak RB$ de $B$~; on a", "'Considérons maintenant un idéal premier quelconque 𝔭 ⊃ 𝔎B de B'")
bullet(P, "C_\\mathfrak p=\\operatorname{gr}_{\\mathfrak J_\\mathfrak p}^*(B_\\mathfrak p)", "'C_𝔭 = gr•_{J_𝔭}(B_𝔭) par platitude'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(M)$ est un $A$-module plat entraîne", "'l'hypothèse que gr•_J(M) est un A-module plat entraîne'")
add(P, "'en vertu de (0_I, 6.1.2) que M/J^iM est un A-module plat'", "no comma after (0_I, 6.1.2) (enlarged crop)",
    "'($\\mathbf 0_{\\mathrm I}$, 6.1.2), que': comma added", "punctuation",
    "6.1.2), que $M/\\mathfrak J^iM$", "6.1.2) que $M/\\mathfrak J^iM$")
add(P, "'est un A_μ-module plat pour k≤i. On déduit'", "the i of 'k≤i.' is a bold italic i (wrong fount: stem about twice as heavy as the k beside it and as the i of 'k≤i' two lines above; enlarged crops, ink measurement)",
    "plain $i$", "misprint_in_print",
    "pour $k\\leq i$. On déduit", "pour $k\\leq\\boldsymbol{i}$. On déduit", conf="medium", corrected="$k\\leq i$",
    note="Wrong-font letter recorded as a misprint (GLOBAL_ISSUES 29 practice); the TeX silently corrects it. Heavy inking cannot be excluded entirely, hence medium confidence.")
add(P, "'Par ailleurs les images des q_h dans Q_𝔭⊗_{B_𝔭}k(𝔭) = (Q⊗_A A')_𝔭⊗_{A'}k(𝔭) engendrent ce (C_𝔭⊗_{B_𝔭}k(𝔭))-module (car C_𝔭⊗_{B_𝔭}k(𝔭) = C'_𝔭⊗_{A'}k(𝔭)); comme'",
    "both formulas in the running text; 'engendrent ce (C_𝔭⊗k(𝔭))-module (car ... );'",
    "two displays and the wording 'engendrent ce module sur $C_\\mathfrak p\\otimes_{B_\\mathfrak p}k(\\mathfrak p)$, puisque \\[ ... ~; \\]'", "other",
    "ailleurs les images des $q_h$ dans\n\\[\nQ_\\mathfrak p\\otimes_{B_\\mathfrak p}k(\\mathfrak p)\n=(Q\\otimes_AA')_\\mathfrak p\\otimes_{A'}k(\\mathfrak p)\n\\]\nengendrent ce module sur\n$C_\\mathfrak p\\otimes_{B_\\mathfrak p}k(\\mathfrak p)$, puisque\n\\[\nC_\\mathfrak p\\otimes_{B_\\mathfrak p}k(\\mathfrak p)\n=C'_\\mathfrak p\\otimes_{A'}k(\\mathfrak p)~;\n\\]\ncomme on a la suite exacte",
    "ailleurs les images des $q_h$ dans\n$Q_\\mathfrak p\\otimes_{B_\\mathfrak p}\\boldsymbol{k}(\\mathfrak p)\n=(Q\\otimes_AA')_\\mathfrak p\\otimes_{A'}\\boldsymbol{k}(\\mathfrak p)$\nengendrent ce\n$(C_\\mathfrak p\\otimes_{B_\\mathfrak p}\\boldsymbol{k}(\\mathfrak p))$-module\n(car $C_\\mathfrak p\\otimes_{B_\\mathfrak p}\\boldsymbol{k}(\\mathfrak p)\n=C'_\\mathfrak p\\otimes_{A'}\\boldsymbol{k}(\\mathfrak p)$)~;\ncomme on a la suite exacte",
    note="One edit for: the two displays the print sets inline, the reworded clause (next entry) and the five bold k of this passage (convention 1, entries below).")
add(P, "'engendrent ce (C_𝔭⊗_{B_𝔭}k(𝔭))-module (car ...)'", "'ce (C_𝔭⊗k(𝔭))-module (car C_𝔭⊗k(𝔭) = C'_𝔭⊗_{A'}k(𝔭))'",
    "'ce module sur $C_\\mathfrak p\\otimes k(\\mathfrak p)$, puisque [display]'", "word",
    note="Covered by the previous edit.")
for w in ("Q_𝔭⊗_{B_𝔭}k(𝔭)", "(Q⊗_A A')_𝔭⊗_{A'}k(𝔭)", "(C_𝔭⊗_{B_𝔭}k(𝔭))-module", "(car C_𝔭⊗_{B_𝔭}k(𝔭)", "C'_𝔭⊗_{A'}k(𝔭))"):
    kbold_cov(P, f"'Par ailleurs ...': {w}", "Par ailleurs les images des q_h ...")
kbold(P, "Q_\\mathfrak p\\otimes_{B_\\mathfrak p}k(\\mathfrak p)\n\\longrightarrow", "exact sequence, Q_𝔭⊗_{B_𝔭}k(𝔭)")
kbold(P, "C_\\mathfrak p^{r}\\otimes_{B_\\mathfrak p}k(\\mathfrak p)", "exact sequence, C^r_𝔭⊗_{B_𝔭}k(𝔭)")
bullet(P, "\\longrightarrow\n\\operatorname{gr}_{\\mathfrak J_\\mathfrak p}^*(M_\\mathfrak p)\n", "exact sequence, gr•_{J_𝔭}(M_𝔭)")
add(P, "exact sequence 'Q_𝔭⊗k(𝔭) → C^r_𝔭⊗k(𝔭) → gr•(M_𝔭)⊗k(𝔭) → 0'", "no punctuation after the final 0 (enlarged crop); 'on en conclut que' follows",
    "comma after 0", "punctuation",
    "\\otimes_{B_\\mathfrak p}k(\\mathfrak p)\\longrightarrow0,\n\\]", "\\otimes_{B_\\mathfrak p}\\boldsymbol{k}(\\mathfrak p)\\longrightarrow0\n\\]",
    note="The same edit sets the third k of the sequence bold (next entry).")
kbold_cov(P, "exact sequence, gr•(M_𝔭)⊗_{B_𝔭}k(𝔭)", "exact sequence ... no punctuation after the final 0")
bullet(P, "on en conclut que\n$\\operatorname{gr}_{\\mathfrak J_\\mathfrak p}^*(M_\\mathfrak p)", "'on en conclut que gr•_{J_𝔭}(M_𝔭)⊗k(𝔭) est un'")
kbold(P, "\\otimes_{B_\\mathfrak p}k(\\mathfrak p)$ est un", "'gr•(M_𝔭)⊗_{B_𝔭}k(𝔭) est un'")
kbold(P, "$(C_\\mathfrak p\\otimes_{B_\\mathfrak p}k(\\mathfrak p))$-module de présentation", "'(C_𝔭⊗_{B_𝔭}k(𝔭))-module de présentation finie'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\mathfrak p}^*(M_\\mathfrak p)$, on en conclut", "'C_𝔭 et gr•_{J_𝔭}(M_𝔭), on en conclut'")
add(P, "'on en conclut que Q_𝔭 est un C_𝔭-module de type fini.'", "'de type fini' in italics", "roman", "italics",
    "$C_\\mathfrak p$-module de type fini. Utilisant", "$C_\\mathfrak p$-module \\emph{de type fini}. Utilisant")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(M)$ est un $C$-module", "'le fait que gr•_J(M) est un C-module de présentation finie'")
add(P, "'VI) Fin de la démonstration. —'", "'VI)' roman, medium weight (enlarged crop)", "\\textbf{VI)} (bold)", "font",
    "\\textbf{VI)}", "VI)",
    note="ega4-11-fr.tex sets all 8 hand-made proof-part labels I)-VI) with \\textbf: check the others against the print (document-wide candidate).")
bullet(P, "$N_\\lambda=\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)$", "'N_λ = gr•_{J_λ}(M_λ)'")
bullet(P, "$N=\\operatorname{gr}_{\\mathfrak J}^*(M)$", "'N = gr•_J(M)'")
add(P, "'par exactitude du foncteur lim→, l'image de J^k_λM_λ dans M_μ'", "comma after lim→ (enlarged crop)", "'~;' (semicolon)", "punctuation",
    "$\\varinjlim$~; l'image", "$\\varinjlim$, l'image")
add(P, "'nous allons d'abord prouver que : (11.2.9.9) Pour λ assez grand, l'homomorphisme canonique v_λ : N_λ⊗_{A_λ}A → N est bijectif.'",
    "a numbered paragraph: bold (11.2.9.9) at the paragraph indent followed by the italic statement in the text line (as an env statement)",
    "an equation environment with \\tag{11.2.9.9} and \\text{\\emph{...}}: a centred display with the number in the equation-number position", "other",
    "nous allons d'abord prouver que~:\n\\begin{equation}\n\\text{\\emph{Pour $\\lambda$ assez grand, l'homomorphisme canonique\n$v_\\lambda:N_\\lambda\\otimes_{A_\\lambda}A\\to N$ est bijectif.}}\n\\label{IV.11.2.9.9-fr}\n\\tag{11.2.9.9}\n\\end{equation}\nComme les",
    "nous allons d'abord prouver que~:\n\n\\begin{env}[11.2.9.9]\n\\label{IV.11.2.9.9-fr}\n\\emph{Pour $\\lambda$ assez grand, l'homomorphisme canonique\n$v_\\lambda:N_\\lambda\\otimes_{A_\\lambda}A\\to N$ est bijectif.}\n\\end{env}\n\nComme les",
    conf="medium",
    note="Same form as the edition's (11.1.1.1) (\\begin{env} with an \\emph body). Nothing \\ref's the label. The edit also restores the paragraph break before 'Comme les C_λ' (next entry).")
add(P, "'Comme les C_λ sont noethériens' (after (11.2.9.9))", "new indented paragraph", "no blank line after \\end{equation}", "other",
    note="Covered by the previous edit.")
add(P, "end of page_131.tex, before \\oldpage[IV-3]{132}: 'v_{μλ} : N_λ⊗_{A_λ}A → N_μ⊗_{A_μ}A | pour λ≤μ'",
    "p. 132 begins 'pour λ≤μ et les homomorphismes' flush left: mid-sentence page break",
    "blank line at the end of page_131.tex: paragraph break mid-sentence", "marker",
    "\\to N_\\mu\\otimes_{A_\\mu}A$\n\n", "\\to N_\\mu\\otimes_{A_\\mu}A$\n",
    note="Mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 132 entry removing the blank line after \\oldpage[IV-3]{132}. The marker itself is in the right place.")

# ---------------------------------------------------------------- page 132
P = 132
add(P, "top of the page: 'pour λ≤μ et les homomorphismes v_λ sont surjectifs'", "flush left: continues the sentence of p. 131",
    "\\oldpage[IV-3]{132} followed by a blank line", "marker",
    "\\oldpage[IV-3]{132}\n\npour", "\\oldpage[IV-3]{132}\npour",
    note="Apply together with the p. 131 entry removing the blank line before the marker.")
ker(P, "$\\ker(v_{\\mu\\lambda})=N'_\\mu$", "'les sous-C-modules Ker(v_{μλ}) = N'_μ'")
ker(P, "de $\\ker(v_\\lambda)$, dont", "'de sous-C-modules de Ker(v_λ), dont la réunion'")
ker(P, "$\\ker(v_\\lambda)$~; mais", "'dont la réunion est Ker(v_λ); mais'")
add(P, "'(Bourbaki, Alg. comm., chap. I, § 2, n° 8, lemme 9)'", "n with a superior letter o", "n$^\\circ$ (degree sign)", "symbol",
    "n$^\\circ$~8", "n\\textsuperscript{o}~8", note="As on p. 130.")
ker(P, "lemme 9) $\\ker(v_\\lambda)$ est", "'lemme 9) Ker(v_λ) est un C-module de type fini'")
add(P, "'Ker(v_λ) est un C-module de type fini; il existe'", "'de type fini;' in italics", "roman", "italics",
    "$C$-module de type fini~; il", "$C$-module \\emph{de type fini}~; il")
ker(P, "$N'_\\mu=\\ker(v_\\lambda)$", "'tel que N'_μ = Ker(v_λ)'")
add(P, "'P_μ soit un A_μ-module plat. Or, pour μ≥λ'", "'plat' in italics", "roman", "italics",
    "$A_\\mu$-module\nplat. Or", "$A_\\mu$-module\n\\emph{plat}. Or")
add(P, "diagram before 'où il résulte des définitions'", "the label w_μ stands to the LEFT of the vertical arrow P_μ → N_μ",
    "\\ar[d]^{w_\\mu}: xy-pic puts the label to the right of a downward arrow (inside the square)", "formula",
    "\\ar[d]^{w_\\mu}", "\\ar[d]_{w_\\mu}", conf="high")
add(P, "'que P_μ est un A_μ-module plat, l'homomorphisme canonique'", "'plat' in italics", "roman", "italics",
    "est un $A_\\mu$-module plat, l'homomorphisme", "est un $A_\\mu$-module \\emph{plat}, l'homomorphisme")
add(P, "'que w_μ est aussi injectif, donc bijectif'", "'injectif' in italics", "roman", "italics",
    "est aussi injectif, donc", "est aussi \\emph{injectif}, donc")
add(P, "'N_μ est un A_μ-module plat pour μ≥λ'", "'plat' in italics", "roman", "italics",
    "$N_\\mu$ est un $A_\\mu$-module plat pour", "$N_\\mu$ est un $A_\\mu$-module \\emph{plat} pour")
add(P, "heading 11.3", "'11.3. Application à l'élimination d'hypothèses noethériennes.' (final full stop)",
    "\\subsection{...} without the full stop", "punctuation",
    "\\subsection{Application à l'élimination d'hypothèses noethériennes}",
    "\\subsection{Application à l'élimination d'hypothèses noethériennes.}",
    note="Subsection titles lack the printed full stop (GLOBAL_ISSUES 43 pattern).")
add(P, "proof of (11.3.1): 'on peut supposer que X = X_0×_{Y_0}Y, f = f_0×1, ℱ = ℱ_0⊗_{𝒪_{Y_0}}𝒪_Y, où Y_0 est noethérien'",
    "all in the running text", "displayed \\[ ... \\qquad ... \\]", "other",
    "peut supposer que\n\\[\nX=X_0\\times_{Y_0}Y,\\qquad f=f_0\\times1,\\qquad\n\\mathcal F=\\mathcal F_0\\otimes_{\\mathcal O_{Y_0}}\\mathcal O_Y,\n\\]\noù $Y_0$",
    "peut supposer que\n$X=X_0\\times_{Y_0}Y$, $f=f_0\\times1$,\n$\\mathcal F=\\mathcal F_0\\otimes_{\\mathcal O_{Y_0}}\\mathcal O_Y$,\noù $Y_0$",
    note="Formula displayed where the print has it in the running text.")

# ---------------------------------------------------------------- page 133
P = 133
add(P, "Corollaire (11.3.2): '(i.e. tels que'", "'(i.e.' upright roman inside the italic statement (enlarged crop)", "italic", "convention",
    "(i.e. tels que", "\\textup{(i.e.} tels que", conv=6)
add(P, "Corollaire (11.3.2): '... X×_Y Spec(𝒪_{Y,y}) → Z) est ouvert dans Y'", "the closing parenthesis after Z upright (enlarged crop)", "italic", "convention",
    "\\to Z$) est ouvert", "\\to Z$\\textup{)} est ouvert", conv=6)
add(P, "proof of (11.3.2): 'E = Y—f(X—V)', first dash", "long dash (set difference)", "$Y-f(...)$", "convention",
    "$E=Y-f(X-V)$", "$E=Y\\setmin f(X\\setmin V)$", conv=7, note="One edit for both dashes of this formula.")
add(P, "proof of (11.3.2): 'E = Y—f(X—V)', second dash", "long dash", "$X-V$", "convention", conv=7, note="Covered by the previous edit.")
add(P, "proof of (11.3.2): 'et par suite X—V est pro-constructible'", "long dash", "$X-V$", "convention",
    "et par suite $X-V$ est", "et par suite $X\\setmin V$ est", conv=7)
add(P, "proof of (11.3.2): 'f(X—V) est pro-constructible dans Y'", "long dash", "$f(X-V)$", "convention",
    "$f(X-V)$ est pro-constructible", "$f(X\\setmin V)$ est pro-constructible", conv=7)
bullet(P, "On suppose que $\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F)$", "Proposition (11.3.4): 'On suppose que gr•_𝒥(ℱ) est f-plat'")
bullet(P, "\\item Si $\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)$", "(11.3.4) (ii): 'Si gr•_𝒥(𝒪_X) est f-plat'")
bullet(P, "$f$-plat,\n$\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)$ est une", "(11.3.4) (ii): 'gr•_𝒥(𝒪_X) est une (𝒪_X/𝒥)-Algèbre'")
bullet(P, "finie et\n$\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F)$ est un", "(11.3.4) (ii): 'et gr•_𝒥(ℱ) est un'")
bullet(P, "$(\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X))$-Module", "(11.3.4) (ii): '(gr•_𝒥(𝒪_X))-Module'")
bullet(P, "\\item Supposons $\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)$ $f$-plat\n(ce qui", "(11.3.4) (iii): 'Supposons gr•_𝒥(𝒪_X) f-plat'")
bullet(P, "$(\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F))_y$", "(11.3.4) (iii): '(gr•_𝒥(ℱ))_y'")
bullet(P, "\\item Supposons $\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)$ $f$-plat.\nSoit", "(11.3.4) (iv): 'Supposons gr•_𝒥(𝒪_X) f-plat.'")
bullet(P, "$\\operatorname{gr}_{\\mathcal J'}^*(\\mathcal F')|W'", "(11.3.4) (iv): 'gr•_{𝒥'}(ℱ')|W''")
add(P, "(11.3.4) (iv): 'gr•_{𝒥'}(ℱ')|W' ≅ p*(gr•_𝒥(ℱ)|W)'", "≅ (tilde over two bars; enlarged crop)", "\\simeq (tilde over one bar)", "symbol",
    "\\simeq p^*", "\\cong p^*")
bullet(P, "(\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F)|W)$", "(11.3.4) (iv): 'p*(gr•_𝒥(ℱ)|W)'")
bullet(P, "$\\operatorname{gr}_{\\mathcal J'}^*(\\mathcal F')$ est un", "(11.3.4) (iv): 'et gr•_{𝒥'}(ℱ') est un (𝒪_{X'}/𝒥')-Module plat'")
add(P, "proof of (11.3.4): 'et ℱ = M̃, où M est un B-module'", "the M under the tilde is bold (heavier than the M of 'où M' beside it; enlarged crop)",
    "\\widetilde M", "font", "$\\mathcal F=\\widetilde M$, où $M$ est", "$\\mathcal F=\\widetilde{\\mathbf M}$, où $M$ est", conf="medium",
    note="Probably systematic, not a one-off: p. 136 prints both ℱ = M̃ and ℱ_λ = M̃_λ with the same bold M. A III p. 152 checker recorded a bold S̃ as a wrong-fount misprint. Decide once for the tilde letters (document-wide) before applying.")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(M)$ est un $A$-module plat~; donc", "proof of (11.3.4): 'par hypothèse gr•_J(M) est un A-module plat'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)$ soit un", "proof of (11.3.4): 'il existe un λ tel que gr•_{J_λ}(M_λ) soit un A_λ-module plat'")
add(P, "proof of (11.3.4): 'on peut donc se borner au cas où S est noethérien; mais alors'", "'noethérien' in italics", "roman", "italics",
    "$S$ est noethérien~; mais alors", "$S$ est \\emph{noethérien}~; mais alors")

# ---------------------------------------------------------------- page 134
P = 134
add(P, "top of p. 134 / foot of p. 133: 'La démonstration de (ii) se ramène de la même façon au cas où S est noethérien, | en utilisant (11.2.9)'",
    "p. 133 ends with the indented line 'La démonstration de (ii) se ramène de la même façon au cas où S est noethérien,'; p. 134 begins 'en utilisant (11.2.9); la conclusion' flush left",
    "\\oldpage[IV-3]{134} and a blank line stand before 'La démonstration de (ii)': one printed line too early", "marker",
    "\\oldpage[IV-3]{134}\n\nLa démonstration de (ii) se ramène de la même façon au cas où $S$ est\nnoethérien, en utilisant",
    "La démonstration de (ii) se ramène de la même façon au cas où $S$ est\nnoethérien,\n\\oldpage[IV-3]{134}\nen utilisant",
    note="One edit inside the p. 134 segment: the marker moves after 'noethérien,' (mid-sentence, no blank lines). The blank line before 'La démonstration' (end of the p. 133 segment) stays: that paragraph begins indented at the foot of p. 133.")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(B)$ étant", "'gr•_J(B) étant dans ce cas une (B/J)-algèbre'")
bullet(P, "type fini et\n$\\operatorname{gr}_{\\mathfrak J}^*(M)$ un", "'et gr•_J(M) un gr•_J(B)-module de type fini' (first gr)")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(B)$-module de type fini.", "'gr•_J(B)-module de type fini' (second gr)")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(B_\\lambda)$ et", "proof of (iii): 'gr•_{J_λ}(B_λ) et'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)$ sont des", "proof of (iii): 'gr•_{J_λ}(M_λ) sont des A_λ-modules plats'")
add(P, "proof of (iii): 'et que l'on a gr•_J(B) = gr•_{J_λ}(B_λ)⊗_{A_λ}A et gr•_J(M) = gr•_{J_λ}(M_λ)⊗_{A_λ}A. Par suite'",
    "both equalities in the running text, joined by 'et'", "displayed \\[ ... \\quad\\text{et}\\quad ... . \\]", "other",
    "et que l'on a\n\\[\n\\operatorname{gr}_{\\mathfrak J}^*(B)\n=\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(B_\\lambda)\\otimes_{A_\\lambda}A\n\\quad\\text{et}\\quad\n\\operatorname{gr}_{\\mathfrak J}^*(M)\n=\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)\\otimes_{A_\\lambda}A.\n\\]\n",
    "et que l'on a\n$\\operatorname{gr}_{\\mathfrak J}^\\bullet(B)\n=\\operatorname{gr}_{\\mathfrak J_\\lambda}^\\bullet(B_\\lambda)\\otimes_{A_\\lambda}A$\net\n$\\operatorname{gr}_{\\mathfrak J}^\\bullet(M)\n=\\operatorname{gr}_{\\mathfrak J_\\lambda}^\\bullet(M_\\lambda)\\otimes_{A_\\lambda}A$.\n",
    note="Formula displayed where the print has it in the running text. The edit also writes the four bullets of these formulas (entries below).")
for w in ("gr•_J(B)", "gr•_{J_λ}(B_λ)", "gr•_J(M)", "gr•_{J_λ}(M_λ)"):
    bullet_cov(P, f"proof of (iii), display: {w}", "et que l'on a gr•_J(B) = ... (display -> inline)")
bullet(P, "Par suite $\\operatorname{gr}_{\\mathfrak J}^*(B)$", "'Par suite gr•_J(B) est une (B/J)-algèbre de présentation finie'")
bullet(P, "présentation finie et\n$\\operatorname{gr}_{\\mathfrak J}^*(M)$ un", "'et gr•_J(M) un gr•_J(B)-module de présentation finie' (first gr)")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(B)$-module de présentation finie. Si", "'gr•_J(B)-module de présentation finie' (second gr)")
bullet(P, "\\operatorname{Spec}(\\operatorname{gr}_{\\mathfrak J}^*(B))", "'X = Spec(gr•_J(B))'")
bullet(P, "(\\operatorname{gr}_{\\mathfrak J}^*(M))^{\\sim}", "'ℱ = (gr•_J(M))~'")
bullet(P, "$(\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F))_y$", "definition: 'si (gr•_𝒥(ℱ))_y est un 𝒪_{Y,y}-module plat'")
add(P, "definition after the proof of (11.3.4): 'est un 𝒪_{Y,y}-module plat.'", "'plat' in italics", "roman", "italics",
    "$\\mathcal O_{Y,y}$-module plat.", "$\\mathcal O_{Y,y}$-module \\emph{plat}.")
add(P, "definition: 'On dit que F est normalement plat le long de Y'", "a roman capital F, not the script ℱ (enlarged crop)",
    "$\\mathcal F$ (script): silent correction", "misprint_in_print",
    "On dit que $\\mathcal F$ est", "On dit que $F$ est", corrected="On dit que $\\mathcal F$ est",
    note="Wrong-fount letter: the sheaf is ℱ throughout the definition. $F$ follows the edition's treatment of the print's upright capitals.")
bullet(P, "$\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)$ et", "Corollaire (11.3.5): 'on suppose que gr•_𝒥(𝒪_X) et'")
bullet(P, "$\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F)$ soient", "Corollaire (11.3.5): 'gr•_𝒥(ℱ) soient f-plats'")
add(P, "Corollaire (11.3.5): 'Sous les hypothèses générales de (11.3.4), on suppose'", "the reference (11.3.4) upright inside the italic statement (enlarged crop)",
    "italic", "convention", "générales de (11.3.4), on suppose", "générales de \\textup{(11.3.4)}, on suppose", conv=6)
add(P, "Corollaire (11.3.5): '(avec les notations de (11.3.4, (iv)))'", "'(11.3.4, (iv)))' upright inside the italic statement; '(avec les notations de' italic (enlarged crop)",
    "italic", "convention", "(11.3.4, (iv)))", "\\textup{(11.3.4, (iv)))}", conv=6)
add(P, "Proposition (11.3.6): 'Les notations étant celles de (8.5.1) et (8.8.1)', first reference", "(8.5.1) upright inside the italic statement (enlarged crop)",
    "italic", "convention", "celles de (8.5.1) et", "celles de \\textup{(8.5.1)} et", conv=6)
add(P, "Proposition (11.3.6): second reference (8.8.1)", "(8.8.1) upright inside the italic statement", "italic", "convention",
    "et (8.8.1), on suppose", "et \\textup{(8.8.1)}, on suppose", conv=6)
bullet(P, "$\\operatorname{gr}_{\\mathcal J_\\alpha}^*(\\mathcal O_{X_\\alpha})$ soit plat", "Proposition (11.3.6): 'tel que gr•_{𝒥_α}(𝒪_{X_α}) soit plat sur S_α'")
add(P, "proof of (11.3.6): 'on a gr•_𝒥(𝒪_X) = gr•_{𝒥_α}(𝒪_{X_α})⊗_{𝒪_{S_α}}𝒪_S et gr•_{𝒥_λ}(𝒪_{X_λ}) = gr•_{𝒥_α}(𝒪_{X_α})⊗_{𝒪_{S_α}}𝒪_{S_λ} pour λ≥α, et'",
    "both equalities in the running text", "two displays (the second with \\quad\\text{pour }\\lambda\\geq\\alpha)", "other",
    "on a\n\\[\n\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)\n=\\operatorname{gr}_{\\mathcal J_\\alpha}^*(\\mathcal O_{X_\\alpha})\n \\otimes_{\\mathcal O_{S_\\alpha}}\\mathcal O_S\n\\]\net\n\\[\n\\operatorname{gr}_{\\mathcal J_\\lambda}^*(\\mathcal O_{X_\\lambda})\n=\\operatorname{gr}_{\\mathcal J_\\alpha}^*(\\mathcal O_{X_\\alpha})\n \\otimes_{\\mathcal O_{S_\\alpha}}\\mathcal O_{S_\\lambda}\n\\quad\\text{pour }\\lambda\\geq\\alpha,\n\\]\n",
    "on a\n$\\operatorname{gr}_{\\mathcal J}^\\bullet(\\mathcal O_X)\n=\\operatorname{gr}_{\\mathcal J_\\alpha}^\\bullet(\\mathcal O_{X_\\alpha})\n \\otimes_{\\mathcal O_{S_\\alpha}}\\mathcal O_S$\net\n$\\operatorname{gr}_{\\mathcal J_\\lambda}^\\bullet(\\mathcal O_{X_\\lambda})\n=\\operatorname{gr}_{\\mathcal J_\\alpha}^\\bullet(\\mathcal O_{X_\\alpha})\n \\otimes_{\\mathcal O_{S_\\alpha}}\\mathcal O_{S_\\lambda}$\npour $\\lambda\\geq\\alpha$,\n",
    note="Formulas displayed where the print has them in the running text. The edit also writes the four bullets of these formulas (entries below).")
for w in ("gr•_𝒥(𝒪_X)", "gr•_{𝒥_α}(𝒪_{X_α}) (first)", "gr•_{𝒥_λ}(𝒪_{X_λ})", "gr•_{𝒥_α}(𝒪_{X_α}) (second)"):
    bullet_cov(P, f"proof of (11.3.6), displays: {w}", "on a gr•_𝒥(𝒪_X) = ... (displays -> inline)")
bullet(P, "et $\\operatorname{gr}_{\\mathcal J}^*(\\mathcal O_X)$ (resp.", "proof of (11.3.6): 'et gr•_𝒥(𝒪_X) (resp.'")
bullet(P, "$\\operatorname{gr}_{\\mathcal J_\\lambda}^*(\\mathcal O_{X_\\lambda})$) est plat", "proof of (11.3.6): 'gr•_{𝒥_λ}(𝒪_{X_λ})) est plat sur S'")
bullet(P, "$Y_\\lambda$, $\\operatorname{gr}_{\\mathcal J_\\lambda}^*\n(", "proof of (11.3.6): 'gr•_{𝒥_λ}(ℱ_λ)|Y_λ est plat sur Y_λ'")
add(P, "proof of (11.3.6): 'et comme (gr•_{𝒥_λ}(ℱ_λ))_{x_λ} = 0 pour x_λ∉Y_λ'", "the stalk at x_λ: (gr•_{𝒥_λ}(ℱ_λ))_{x_λ} = 0 (enlarged crop)",
    "gr(ℱ_λ)|x_λ = 0 (restriction bar, no outer parentheses)", "formula",
    "et comme\n$\\operatorname{gr}_{\\mathcal J_\\lambda}^*(\\mathcal F_\\lambda)|x_\\lambda=0$",
    "et comme\n$(\\operatorname{gr}_{\\mathcal J_\\lambda}^\\bullet(\\mathcal F_\\lambda))_{x_\\lambda}=0$",
    note="The edit also writes the bullet of this gr (next entry).")
bullet_cov(P, "proof of (11.3.6): '(gr•_{𝒥_λ}(ℱ_λ))_{x_λ}'", "et comme (gr•_{𝒥_λ}(ℱ_λ))_{x_λ} = 0")
bullet(P, "$\\operatorname{gr}_{\\mathcal J_\\lambda}^*(\\mathcal F_\\lambda)$ est plat sur", "proof of (11.3.6): 'gr•_{𝒥_λ}(ℱ_λ) est plat sur S_λ'")
add(P, "proof of (11.3.6): 'On en conclut (11.2.9.2) que gr•_𝒥(ℱ) = gr•_{𝒥_λ}(ℱ_λ)⊗_{𝒪_{S_λ}}𝒪_S, donc'",
    "in the running text", "displayed \\[ ... , \\]", "other",
    "que\n\\[\n\\operatorname{gr}_{\\mathcal J}^*(\\mathcal F)\n=\\operatorname{gr}_{\\mathcal J_\\lambda}^*(\\mathcal F_\\lambda)\n \\otimes_{\\mathcal O_{S_\\lambda}}\\mathcal O_S,\n\\]\n",
    "que\n$\\operatorname{gr}_{\\mathcal J}^\\bullet(\\mathcal F)\n=\\operatorname{gr}_{\\mathcal J_\\lambda}^\\bullet(\\mathcal F_\\lambda)\n \\otimes_{\\mathcal O_{S_\\lambda}}\\mathcal O_S$,\n",
    note="Formula displayed where the print has it in the running text. The edit also writes the two bullets (entries below).")
for w in ("gr•_𝒥(ℱ)", "gr•_{𝒥_λ}(ℱ_λ)"):
    bullet_cov(P, f"proof of (11.3.6), display: {w}", "On en conclut (11.2.9.2) que gr•_𝒥(ℱ) = ... (display -> inline)")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J}^*(B)$ est un $A$-module plat", "proof of (11.3.6): 'puisque gr•_J(B) est un A-module plat'")
bullet(P, "de $\\operatorname{gr}_{\\mathfrak J}^*(M)$, donc", "proof of (11.3.6): 'il en est de même de gr•_J(M), donc'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)$ soit un", "proof of (11.3.6): 'tel que gr•_{J_λ}(M_λ) soit un A_λ-module plat'")
bullet(P, "d'où\n$\\operatorname{gr}_{\\mathfrak J}^*(M)\n=", "proof of (11.3.6): 'd'où gr•_J(M) = ...' (first gr)")
bullet(P, "=\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)\\otimes_{A_\\lambda}A$.\nEn outre", "proof of (11.3.6): '= gr•_{J_λ}(M_λ)⊗_{A_λ}A' (second gr)")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(M_\\lambda)$ est un", "proof of (11.3.6): 'En outre (11.3.4, (ii)), gr•_{J_λ}(M_λ) est un'")
bullet(P, "$\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(B_\\lambda)$-module de présentation", "proof of (11.3.6): 'gr•_{J_λ}(B_λ)-module de présentation finie'")
bullet(P, "finie et $\\operatorname{gr}_{\\mathfrak J_\\lambda}^*(B_\\lambda)$ une", "proof of (11.3.6): 'et gr•_{J_λ}(B_λ) une (B_λ/J_λ)-algèbre'")


# ---------------------------------------------------------------- checks
def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-3\]\{(\d+)\}", rel)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = rel[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]

ok = True
for p in range(130, 135):
    pt = page_text(p)
    body = pt.split("\n", 1)[1]  # drop the '% from' line
    if body != seg[p]:
        print(f"p{p}: page file differs from release segment (len {len(body)} vs {len(seg[p])})")
    cur_page = pt
    cur_seg = seg[p]
    for x in F:
        if x["page"] != p or not x["fix"]:
            continue
        o, nw = x["fix"]["old"], x["fix"]["new"]
        c0 = pt.count(o)
        c1 = cur_page.count(o)
        c2 = cur_seg.count(o)
        tag = "" if c0 == 1 else f"  [orig count {c0}]"
        if c1 != 1 or c2 != 1:
            ok = False
            print(f"FAIL p{p}: count now page={c1} seg={c2}: {o[:70]!r}")
        else:
            cur_page = cur_page.replace(o, nw)
            cur_seg = cur_seg.replace(o, nw)
        if tag:
            print(f"p{p}: {x['kind']} old not unique/absent in original page file{tag}: {o[:60]!r}")
    left = cur_page.count("}^*")
    print(f"p{p}: after all fixes, remaining '}}^*' = {left}, '\\mathfrak R' = {cur_page.count(chr(92)+'mathfrak R')}, '\\ker' = {cur_page.count(chr(92)+'ker')}, 'k(\\mathfrak p)' unbold = {cur_page.count(' k(' + chr(92) + 'mathfrak p)') + cur_page.count('}k(' + chr(92) + 'mathfrak p)')}")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(130, 135):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("OK" if ok else "ERRORS", len(F), "entries ->", OUT)
