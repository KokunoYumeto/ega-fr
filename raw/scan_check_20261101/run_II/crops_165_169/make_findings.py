import json

OUT = r"user\Documents\ega_scan_check_20261101\run_II\findings_165_169.json"
F = []


def add(page, where, scan, tex, kind, convention, confidence, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------- page 165 ----------------
add(165, "Proposition (8.3.5): 'Avec les notations de (8.3.1) et'",
    "the reference (8.3.1) upright inside the italic statement",
    "italic (inside the \\itshape proposition environment)",
    "convention", 6, "high",
    "(\\hyperref[II.8.3.1-fr]{8.3.1})",
    "\\textup{(\\hyperref[II.8.3.1-fr]{8.3.1})}",
    "Checked on a crop.")
add(165, "Proposition (8.3.5): 'et (8.3.4), le morphisme associé'",
    "the reference (8.3.4) upright inside the italic statement",
    "italic (inside the \\itshape proposition environment)",
    "convention", 6, "high",
    "(\\hyperref[II.8.3.4-fr]{8.3.4})",
    "\\textup{(\\hyperref[II.8.3.4-fr]{8.3.4})}",
    "Checked on a crop.")
add(165, "Proposition (8.3.5): 'le morphisme associé (3.5.1) à l'injection canonique'",
    "the reference (3.5.1) upright inside the italic statement",
    "italic (inside the \\itshape proposition environment)",
    "convention", 6, "high",
    "(\\hyperref[II.3.5.1-fr]{3.5.1})",
    "\\textup{(\\hyperref[II.3.5.1-fr]{3.5.1})}",
    "Checked on a crop.")
add(165, "Proposition (8.3.5): 'φ : 𝒮 → 𝒮̂ = 𝒮[z]'",
    "𝒮[z] with a bold upright z",
    "$\\mathcal{S}[z]$ (italic z)",
    "font", None, "high",
    "\\widehat{\\mathcal{S}}=\\mathcal{S}[z]$",
    "\\widehat{\\mathcal{S}}=\\mathcal{S}[\\mathbf{z}]$",
    "Checked on a crop. The indeterminate z of 𝒮[z] is printed bold upright here and on pp. 168-169 (see the document-wide note in the report).")
add(165, "Proposition (8.3.5): '(dit rétraction canonique)'",
    "'(dit' upright, 'rétraction canonique)' italic",
    "(dit \\emph{rétraction canonique}) inside the italic proposition: 'dit' comes out italic, 'rétraction canonique' upright",
    "convention", 6, "high",
    "(dit \\emph{rétraction canonique})",
    "\\textup{(dit} rétraction canonique)",
    "Both halves of convention 6 in one place: the roman word 'dit' is italic in the TeX and the printed italic term is set upright by \\emph. Checked on a crop; the closing parenthesis is italic in the print.")
add(165, "(8.3.5.3), whole statement 'Si Y=Spec(A) est affine, et 𝒮=S̃, on a ... (T indéterminée).'",
    "the statement is printed italic (bold number, italic text, like a proposition)",
    "the env environment sets the text upright",
    "convention", 6, "high",
    "\\label{II.8.3.5.3-fr}\nSi $Y=",
    "\\label{II.8.3.5.3-fr}\n\\itshape Si $Y=",
    "Printed italic text left upright. \\itshape inside the env group lasts to \\end{env} and covers the text on both sides of display (8.3.5.4); \\emph{...} (used for the one-sentence (TF)/(TN) on p. 39) would have to span the display.")
add(165, "end of p. 165 segment, blank line before \\oldpage[II]{166} (top of p. 166: 'à l'injection S_f^≤ → S_f (8.3.2)')",
    "p. 166 begins flush left with 'à l'injection ...', continuing the sentence 'l'immersion i, restreinte à C_f, correspondait'",
    "correspondait\\n\\n\\oldpage[II]{166}: the blank line starts a new paragraph",
    "other", None, "high",
    "restreinte à $C_f$, correspondait\n\n",
    "restreinte à $C_f$, correspondait\n",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line lies in p. 165's segment; nothing after the p. 166 marker needs to change.")

# ---------------- page 166 ----------------
add(166, "Remarque (8.3.7), after display (8.3.7.1): 'En effet, pour vérifier cette relation'",
    "new paragraph (first line indented)",
    "\\end{equation}\\nEn effet: no paragraph break",
    "other", None, "high",
    "\\end{equation}\nEn effet",
    "\\end{equation}\n\nEn effet",
    "Missing paragraph break.")
add(166, "Corollaire (8.3.8): 'la fibre p^{-1}(x) est isomorphe à Spec(k(x)[T])'",
    "bold italic k in k(x)",
    "plain k(x)",
    "convention", 1, "high",
    "\\operatorname{Spec}(k(x)[T])",
    "\\operatorname{Spec}(\\boldsymbol{k}(x)[T])",
    "")
add(166, "Corollaire (8.3.8): 'la fibre π^{-1}(x) est isomorphe à Spec(k(x)[T, T^{-1}])'",
    "bold italic k in k(x)",
    "plain k(x)",
    "convention", 1, "high",
    "\\operatorname{Spec}(k(x)[T,T^{-1}])",
    "\\operatorname{Spec}(\\boldsymbol{k}(x)[T,T^{-1}])",
    "")
add(166, "Remarque (8.3.9), first display '(x,y)→(x,x^{-1},y)→(x,x^{-1}y)→x(x^{-1}y)'",
    "three plain arrows",
    "three \\mapsto",
    "convention", 3, "high",
    "(x,y)\\mapsto(x,x^{-1},y)\\mapsto(x,x^{-1}y)\\mapsto x(x^{-1}y)",
    "(x,y)\\to(x,x^{-1},y)\\to(x,x^{-1}y)\\to x(x^{-1}y)",
    "Checked on a crop: no bar at the tails (3 arrows).")
add(166, "Remarque (8.3.9), second display '(x,y)→(x,x^{-1},y)→(x,yx^{-1})→(yx^{-1})x'",
    "three plain arrows",
    "three \\mapsto",
    "convention", 3, "high",
    "(x,y)\\mapsto(x,x^{-1},y)\\mapsto(x,yx^{-1})\\mapsto(yx^{-1})x",
    "(x,y)\\to(x,x^{-1},y)\\to(x,yx^{-1})\\to(yx^{-1})x",
    "Checked on a crop: no bar at the tails (3 arrows).")
add(166, "Remarque (8.3.9): 'doivent toutes deux se réduire à (x,y)→y'",
    "plain arrow",
    "\\mapsto",
    "convention", 3, "high",
    "$(x,y)\\mapsto y$",
    "$(x,y)\\to y$",
    "Checked on a crop.")

# ---------------- page 167 ----------------
add(167, "first line: 'Il est immédiat (I, 3.4.3)'",
    "(I, 3.4.3) with bold I",
    "plain I in the link text",
    "convention", 2, "high",
    "{I, 3.4.3}",
    "{\\textbf{I}, 3.4.3}",
    "")
add(167, "'l'ensemble des Z-sections de Z×_Y G_m (I, 3.3.14)'",
    "(I, 3.3.14) with bold I",
    "plain I in the link text",
    "convention", 2, "high",
    "{I, 3.3.14}",
    "{\\textbf{I}, 3.3.14}",
    "")
add(167, "'le même raisonnement que dans (I, 3.3.15)'",
    "(I, 3.3.15) with bold I",
    "plain I in the link text",
    "convention", 2, "high",
    "{I, 3.3.15}",
    "{\\textbf{I}, 3.3.15}",
    "")
add(167, "display of π and σ: first line 'π : 𝒪_Y[T,T^{-1}] → 𝒪_Y[T,T^{-1},T',T'^{-1}]'",
    "no punctuation after the first line (and none after the second)",
    "comma after the first line: 'T'^{-1}],\\\\'",
    "punctuation", None, "high",
    "T',T'^{-1}],\\\\",
    "T',T'^{-1}]\\\\",
    "Checked on a crop.")
add(167, "'défini par la donnée de l'homomorphisme de 𝒪_Y-Algèbres 𝒮 → 𝒮⊗_{𝒪_Y}𝒪_Y[T,T^{-1}] = 𝒮[T,T^{-1}] qui, à toute section'",
    "the formula is set inline in the running text",
    "displayed with \\[ ... \\]",
    "other", None, "high",
    "$\\mathcal{O}_Y$-Algèbres\n\\[\n  \\mathcal{S}\\to\n  \\mathcal{S}\\otimes_{\\mathcal{O}_Y}\\mathcal{O}_Y[T,T^{-1}]\n  =\\mathcal{S}[T,T^{-1}]\n\\]\nqui,",
    "$\\mathcal{O}_Y$-Algèbres\n$\\mathcal{S}\\to\\mathcal{S}\\otimes_{\\mathcal{O}_Y}\\mathcal{O}_Y[T,T^{-1}]=\\mathcal{S}[T,T^{-1}]$\nqui,",
    "Layout: the print sets this formula inline; the formula itself matches.")
add(167, "'une structure de « Y-schéma en ensembles munis de groupes d'opérateurs »'",
    "'schéma en ensembles munis de groupes d'opérateurs' all italic (only the letter Y is upright)",
    "only 'munis de groupes d'opérateurs' in \\emph; 'schéma en ensembles' roman (remark judged as roman body)",
    "italics", None, "high",
    "«~$Y$-schéma en\nensembles \\emph{munis de groupes d'opérateurs}~»",
    "«~$Y$-\\emph{schéma en\nensembles munis de groupes d'opérateurs}~»",
    "Checked on a crop.")
add(167, "'qui s'écrira donc ψ = Σ_{n∈Z} ψ_n T^n'",
    "the Z under the Σ is a roman (not bold) Z",
    "\\sum_{n\\in\\mathbf{Z}} (bold Z): silent correction",
    "misprint_in_print", None, "medium",
    "\\sum_{n\\in\\mathbf{Z}}",
    "\\sum_{n\\in\\mathrm{Z}}",
    "Wrong-font Z in the print: the integers are bold Z everywhere else (e.g. the ⊕_{n∈Z} on pp. 168-169); this one is a light roman Z (checked on a crop). The TeX silently corrects it; the fix restores the printed reading for the diplomatic edition.",
    corrected="\\sum_{n\\in\\mathbf{Z}}")
add(167, "end of p. 167 segment, blank line before \\oldpage[II]{168} (top of p. 168: 'Nous ne développerons pas davantage')",
    "p. 168 begins flush left with 'Nous ne développerons ...': same paragraph as '... sans appel à une graduation préalable.' (the paragraph indent is visible at the top of p. 167, not at the top of p. 168)",
    "préalable.\\n\\n\\oldpage[II]{168}: the blank line starts a new paragraph",
    "other", None, "high",
    "graduation préalable.\n\n",
    "graduation préalable.\n",
    "Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). The blank line lies in p. 167's segment; nothing after the p. 168 marker needs to change.")

# ---------------- page 168 ----------------
add(168, "Remarque (8.4.3): 'donc les immersions canoniques E→Ĉ et Ê→Ĉ ne sont pas projectives (5.5.3)'",
    "E→Ĉ et Ê→Ĉ (both immersions into Ĉ)",
    "$E\\to\\widehat{E}$ et $\\widehat{E}\\to\\widehat{C}$",
    "formula", None, "high",
    "$E\\to\\widehat{E}$ et",
    "$E\\to\\widehat{C}$ et",
    "Checked on a crop. The print's reading is the one the argument needs (E and Ê are open non-closed in the projective Ĉ; then (5.5.5, (v)) with Ĉ→Y).")
add(168, "Remarque (8.4.3): 'or nous avons vu que ce dernier n'est pas affine (I, 5.5.11)'",
    "(I, 5.5.11) with bold I",
    "plain I in the link text",
    "convention", 2, "high",
    "{I, 5.5.11}",
    "{\\textbf{I}, 5.5.11}",
    "")
add(168, "Remarque (8.4.3): 'où ne s'annule pas la section z au-dessus de Ê (8.3.2)'",
    "bold upright z",
    "$z$ (italic)",
    "font", None, "high",
    "la section $z$ au-dessus",
    "la section $\\mathbf{z}$ au-dessus",
    "Checked on a crop. Same bold z as in 𝒮[z] (p. 165).")
add(168, "Proposition (8.4.4): 'transformant la section nulle (resp. le lieu à l'infini) de la première'",
    "'(resp.' and ')' upright, 'le lieu à l'infini' italic",
    "all italic (inside the \\itshape proposition environment)",
    "convention", 6, "high",
    "(resp. le lieu à l'infini)",
    "\\textup{(resp.} le lieu à l'infini\\textup{)}",
    "Checked on a crop.")
add(168, "Proposition (8.4.4): 'en le lieu à l'infini (resp. la section nulle) de la seconde'",
    "'(resp.' and ')' upright, 'la section nulle' italic",
    "all italic (inside the \\itshape proposition environment)",
    "convention", 6, "high",
    "(resp. la section nulle)",
    "\\textup{(resp.} la section nulle\\textup{)}",
    "Checked on a crop.")
add(168, "proof of (8.4.4), displayed 'l'injection canonique 𝒮 → ⊕_{n∈Z} ℒ^{⊗n}'",
    "the index n in 'n∈Z' under ⊕ is bold italic (wrong font)",
    "plain n: silent correction",
    "misprint_in_print", None, "medium",
    "\\mathcal{S}\\to\\bigoplus_{n\\in\\mathbf{Z}}",
    "\\mathcal{S}\\to\\bigoplus_{\\boldsymbol{n}\\in\\mathbf{Z}}",
    "Checked on a magnified crop: this n is as heavy as the bold Z beside it, unlike the n under the other ⊕ signs on this page ((8.4.4.1), (8.4.4.3), last line). A wrong-font sort; apply only if the diplomatic edition reproduces wrong-font letters.",
    corrected="\\mathcal{S}\\to\\bigoplus_{n\\in\\mathbf{Z}}")
add(168, "end of p. 168 segment, blank line before \\oldpage[II]{169} (top of p. 169: 'et ℒ = 𝒪_Y, donc ...')",
    "p. 169 begins flush left with 'et ℒ = 𝒪_Y', continuing the sentence 'on peut supposer que Y = Spec(A) est affine'",
    "est affine\\n\\n\\oldpage[II]{169}: the blank line starts a new paragraph",
    "other", None, "high",
    "$Y=\\operatorname{Spec}(A)$ est affine\n\n",
    "$Y=\\operatorname{Spec}(A)$ est affine\n",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20), inside the proof of (8.4.4). The blank line lies in p. 168's segment; nothing after the p. 169 marker needs to change.")

# ---------------- page 169 ----------------
add(169, "first line: 'et ⊕_{n∈Z} ℒ^{⊗n} = (A[T,T^{-1}])~'",
    "the index n in 'n∈Z' under ⊕ is bold italic (wrong font)",
    "plain n: silent correction",
    "misprint_in_print", None, "medium",
    "$\\bigoplus_{n\\in\\mathbf{Z}}\\mathcal{L}^{\\otimes n}\n=",
    "$\\bigoplus_{\\boldsymbol{n}\\in\\mathbf{Z}}\\mathcal{L}^{\\otimes n}\n=",
    "Checked on a magnified crop: the n is as heavy as the bold Z, unlike the superscript n of ℒ^{⊗n}. Same wrong-font n as in the display of p. 168; apply only if wrong-font letters are reproduced.",
    corrected="$\\bigoplus_{n\\in\\mathbf{Z}}\\mathcal{L}^{\\otimes n}=")
add(169, "'Alors S(L⊕A) est produit tensoriel de A[z]'",
    "A[z] with a bold upright z",
    "$A[z]$ (italic z)",
    "font", None, "high",
    "est produit tensoriel de $A[z]$",
    "est produit tensoriel de $A[\\mathbf{z}]$",
    "Checked on a magnified crop.")
add(169, "'S(L^{-1}⊕A) produit tensoriel de A[z] et de ⊕_{n≥0} Ac'^{⊗n}'",
    "A[z] with a bold upright z",
    "$A[z]$ (italic z)",
    "font", None, "high",
    "tensoriel de $A[z]$ et de $\\bigoplus_{n\\geq0}Ac'",
    "tensoriel de $A[\\mathbf{z}]$ et de $\\bigoplus_{n\\geq0}Ac'",
    "")
add(169, "'fait correspondre à z^h⊗c'^{⊗(n-h)}'",
    "bold upright z",
    "$z^h$ (italic z)",
    "font", None, "high",
    "$z^h\\otimes c'",
    "$\\mathbf{z}^h\\otimes c'",
    "Checked on a crop.")
add(169, "'l'élément z^{n-h}⊗c^{⊗h}'",
    "bold upright z",
    "$z^{n-h}$ (italic z)",
    "font", None, "high",
    "$z^{n-h}\\otimes",
    "$\\mathbf{z}^{n-h}\\otimes",
    "Checked on a crop.")
add(169, "'le lieu à l'infini est l'ensemble des points où s'annule la section z'",
    "bold upright z",
    "$z$ (italic z)",
    "font", None, "high",
    "s'annule la section $z$ et",
    "s'annule la section $\\mathbf{z}$ et",
    "")
add(169, "(8.5.1), after display (8.5.1.1): 'On sait (1.5.6) qu'il lui correspond canoniquement un morphisme'",
    "new paragraph (first line indented)",
    "\\end{equation}\\nOn sait: no paragraph break",
    "other", None, "high",
    "\\end{equation}\nOn sait",
    "\\end{equation}\n\nOn sait",
    "Missing paragraph break. Checked on a crop.")
add(169, "end of p. 169 segment, blank line after display (8.5.1.3) before \\oldpage[II]{170} (top of p. 170: 'qui correspond au diagramme')",
    "p. 170 begins flush left with 'qui correspond au diagramme', continuing the sentence 'on a alors un diagramme commutatif (8.5.1.3)'",
    "\\end{equation}\\n\\n\\oldpage[II]{170}: the blank line starts a new paragraph",
    "other", None, "high",
    "\\tag{8.5.1.3}\n\\end{equation}\n\n",
    "\\tag{8.5.1.3}\n\\end{equation}\n",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20). The blank line lies in p. 169's segment (the p. 170 checker cannot see it); checked on the top of the p. 170 scan.")

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
