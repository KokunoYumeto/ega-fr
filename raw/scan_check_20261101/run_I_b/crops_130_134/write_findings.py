import json

RUN = r"user\Documents\ega_scan_check_20261101\run_I_b"
SRC = r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega1\ega1-5-fr.tex"
OUTFILE = RUN + r"\findings_130_134.json"
NL = "\r\n"  # the page files and the source use CRLF line endings

F = []

def add(page, where, scan, tex, kind, convention, confidence, fix, note, corrected=None, fix_in_source=False):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": fix,
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_fix_in_source"] = fix_in_source
    F.append(d)

# ---------------- page 130 ----------------
add(130,
    "proof of Prop. 5.1.9, 'donc on a J ~ K~ et K_x = J_x'",
    "𝒥 ≅ 𝔎̃ (tilde over a DOUBLE bar, i.e. \\cong)",
    r"\mathscr{J}\simeq\widetilde{\mathfrak{K}}",
    "symbol", None, "high",
    {"old": r"\mathscr{J}\simeq\widetilde{\mathfrak{K}}",
     "new": r"\mathscr{J}\cong\widetilde{\mathfrak{K}}"},
    "Zoomed scan shows a tilde above two parallel bars (≅), not ≃. Not an isomorphism arrow, so not convention 4.")

add(130,
    "proof of Prop. 5.1.9, between '(1.4.1).' and 'Cela étant'",
    "'... pour tout x∈X_0 (1.4.1). Cela étant, soit X'=Spec(A) ...' in one paragraph ('Cela étant' starts flush left, not indented; the previous line is full)",
    "blank line before 'Cela étant' (new paragraph)",
    "other", None, "medium",
    {"old": "{1.4.1})." + NL + NL + "Cela étant",
     "new": "{1.4.1})." + NL + "Cela étant"},
    "Spurious paragraph break: printed paragraphs are indented, 'Cela étant' is not.")

add(130,
    "page start: Prop. 5.1.9 heading",
    "page 130 begins with the heading 'Proposition (5.1.9). — Soient X un préschéma ...'",
    r"\begin{proposition}[5.1.9]\label{I.5.1.9-fr} precede \oldpage[I]{130}, so the heading falls on page 129",
    "marker", None, "low",
    {"old": r"\begin{proposition}[5.1.9]" + "\n" + r"\label{I.5.1.9-fr}" + "\n" + r"\oldpage[I]{130}",
     "new": r"\oldpage[I]{130}" + "\n" + r"\begin{proposition}[5.1.9]" + "\n" + r"\label{I.5.1.9-fr}"},
    "The 'old' text is in ega1-5-fr.tex lines 192-194 (LF line endings there; page_130.tex starts at the marker, so the heading lines are not in it). "
    "The same file puts \\oldpage[I]{136} before \\begin{corollary}[5.4.5]; ega1 uses both placements, hence low confidence.",
    fix_in_source=True)

# ---------------- page 131 ----------------
add(131,
    "proof of Lemma 5.1.9.2, 'on en conclut que G est un O_Y-Module quasi-cohérent.'",
    "'quasi-cohérent' in italics",
    "quasi-cohérent (roman)",
    "italics", None, "high",
    {"old": "Module quasi-cohérent. Si",
     "new": r"Module \emph{quasi-cohérent}. Si"},
    "")

add(131,
    "proof of Lemma 5.1.9.2, reference (0, 5.4.9)",
    "(𝟎, 5.4.9) with bold 0",
    r"\hyperref[0.5.4.9-fr]{0, 5.4.9}",
    "convention", 2, "high",
    {"old": "{0, 5.4.9}",
     "new": r"{\textbf{0}, 5.4.9}"},
    "")

add(131,
    "proof of Lemma 5.1.9.2, 'G|V soit isomorphe à F|Y ⊕ O_Y|V'",
    "ℱ|Y ⊕ 𝒪_Y|V",
    r"\mathscr{F}|Y\oplus\mathscr{O}_Y|V",
    "misprint_in_print", None, "high",
    None,
    "TeX keeps the printed reading. The local splitting on V needs ℱ|V, not ℱ|Y.",
    corrected=r"\mathscr{F}|V\oplus\mathscr{O}_Y|V")

# ---------------- page 132 ----------------
for old, label in [(r"(resp. $Y'$)", "first"), (r"(resp. $Y$)", "second"),
                   (r"(resp. $\mathscr{K}$)", "third"), (r"(resp. $\mathscr{O}_Y$)", "fourth")]:
    inner = old[len("(resp. "):-1]
    add(132,
        "statement of Cor. 5.2.4, %s '(resp. ...)'" % label,
        "'(resp. ...)' set upright inside the italic statement",
        old + " inside the italic corollary environment",
        "convention", 6, "high",
        {"old": old, "new": r"(\textup{resp.} " + inner + ")"},
        "")

add(132,
    "(5.3.1), 'les projections de X×_S X (déf. (3.2.1)).'",
    "(déf. (3.2.1)) — the reference has its own parentheses inside",
    r"(déf. \hyperref[I.3.2.1-fr]{3.2.1})",
    "punctuation", None, "high",
    {"old": r"(déf. \hyperref[I.3.2.1-fr]{3.2.1})",
     "new": r"(déf. (\hyperref[I.3.2.1-fr]{3.2.1}))"},
    "Inner pair of parentheses missing in the TeX.")

add(132,
    "(5.3.1), last sentence 'pourvu que ... dans cette catégorie'",
    "italics only on 'pourvu que les produits qui y figurent existent'; 'dans cette catégorie.' is roman",
    r"\emph{pourvu que les produits qui y figurent existent dans cette catégorie}",
    "italics", None, "high",
    {"old": "existent dans cette catégorie}.",
     "new": "existent} dans cette catégorie."},
    "")

add(132,
    "statement of Prop. 5.3.5, 'Soient f : X→S, Y→S les morphismes structuraux'",
    "f : X→S, Y→S (no 'g :' before the second morphism)",
    r"$f:X\to S$, $Y\to S$",
    "misprint_in_print", None, "high",
    None,
    "TeX keeps the printed reading. g is used immediately afterwards (π = f∘p = g∘q, f×_T g), so the print omits 'g :'.",
    corrected=r"$f:X\to S$, $g:Y\to S$")

# ---------------- page 134 ----------------
add(134,
    "first paragraph, 'est appelé le graphe du morphisme f'",
    "'le graphe' in italics (both words)",
    r"le \emph{graphe}",
    "italics", None, "high",
    {"old": r"le \emph{graphe}",
     "new": r"\emph{le graphe}"},
    "")

add(134,
    "second paragraph, 'qui ne sont autres que les S-sections de Y (2.5.5)'",
    "S-sections with 'sections' in italics",
    "$S$-sections (roman)",
    "italics", None, "high",
    {"old": r"les $S$-sections de $Y$ (\hyperref[I.2.5.5-fr]",
     "new": r"les $S$-\emph{sections} de $Y$ (\hyperref[I.2.5.5-fr]"},
    "The later 'graphes de S-sections' is roman in the print too and is correct in the TeX.")

add(134,
    "statement of Cor. 5.3.13, '(resp. une immersion locale)'",
    "'resp.' upright inside the italic statement",
    "(resp. une immersion locale) inside the italic corollary environment",
    "convention", 6, "high",
    {"old": r"(resp. une immersion locale), il en est de même de $f$",
     "new": r"(\textup{resp.} une immersion locale), il en est de même de $f$"},
    "")

add(134,
    "statement of Cor. 5.3.14, '(resp. une immersion locale)'",
    "'resp.' upright inside the italic statement",
    "(resp. une immersion locale) inside the italic corollary environment",
    "convention", 6, "high",
    {"old": r"(resp. une immersion locale), il en est de même de $(j,g)_S$",
     "new": r"(\textup{resp.} une immersion locale), il en est de même de $(j,g)_S$"},
    "")

add(134,
    "statement of Prop. 5.3.15, after the diagram",
    "'est commutatif' italic, then '(en d'autres termes Δ_X est un morphisme fonctoriel dans la catégorie des préschémas)' upright",
    "the parenthesis inside the italic proposition environment",
    "convention", 6, "high",
    {"old": "(en d'autres termes $\\Delta_X$ est un morphisme fonctoriel" + NL + "dans la catégorie des préschémas)",
     "new": "\\textup{(en d'autres termes $\\Delta_X$ est un morphisme fonctoriel" + NL + "dans la catégorie des préschémas)}"},
    "")

add(134,
    "proof of Cor. 5.3.13, 'f se factorise en X → X×_Z Y → Y.'",
    "factorisation set inline in the running text: '... se factorise en X →(Γ_f) X×_Z Y →(p_2) Y. D'autre part, ...'",
    "factorisation set as a displayed formula \\[ ... \\]",
    "other", None, "low",
    {"old": "se factorise en" + NL + "\\[" + NL + "  X\\xrightarrow{\\Gamma_f}X\\times_Z Y\\xrightarrow{p_2}Y." + NL + "\\]" + NL + "D'autre part",
     "new": "se factorise en $X\\xrightarrow{\\Gamma_f}X\\times_Z Y\\xrightarrow{p_2}Y$. D'autre part"},
    "Layout only (display vs inline); the formula itself matches.")

# ---------------- verify and write ----------------
problems = 0
for d in F:
    fx = d["fix"]
    if fx is None:
        continue
    path = SRC if d["_fix_in_source"] else RUN + "\\page_%03d.tex" % d["page"]
    with open(path, "rb") as fh:
        text = fh.read().decode("utf-8")
    n = text.count(fx["old"])
    if n != 1:
        problems += 1
        print("NOT UNIQUE/NOT FOUND (%d):" % n, d["page"], repr(fx["old"]))
for d in F:
    del d["_fix_in_source"]

with open(OUTFILE, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", len(F), "findings; problems:", problems)
