"""Build findings_010_014.json for the pp. 10-14 scan check (EGA IV-4, ega4-16-fr.tex).

Each finding's fix.old must occur exactly once in its page_NNN.tex; the script checks this
and that fixes on one page do not overlap (except where a note says they go together).
"""
import json
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
run = here.parent
OUT = run / "findings_010_014.json"

pages = {p: (run / f"page_{p:03d}.tex").read_text(encoding="utf-8") for p in range(10, 15)}

F = []


def add(page, where, scan, tex, kind, old, new, convention=None, confidence="high", note="", corrected=None):
    item = {
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
        item["corrected"] = corrected
    item["note"] = note
    F.append(item)


J_NOTE = ("Wrong letter: the print's script letter has the descender of a script J (the glyph that ega4-16 writes "
          "\\mathscr{J} on p. 24, proof of (16.4.18)); \\mathscr{I} renders a different letter. ega4-16 has 229 "
          "\\mathscr{I} and 16 \\mathscr{J} (pp. 24, 31-34); ega4-18 uses \\mathscr{J}.")
FJ_NOTE = ("Wrong letter: the print's Fraktur capital has the descender of a Fraktur J (as in EGA I/II, where the "
           "edition writes this glyph \\mathfrak{J}); \\mathfrak{I} renders a different letter without descender. "
           "ega4-16 has 132 \\mathfrak{I} and no \\mathfrak{J}; ega4-17/18 use \\mathfrak{J}.")

# ---------------------------------------------------------------- page 10
p = 10
add(p, "(16.2.1), l. 2: 'relatif à l'homomorphisme λ♯ : ρ*(O_Y)→O_Y''",
    "λ♯ (sharp sign)", "\\lambda^\\#", "convention",
    "\\lambda^\\#:\\rho^*(\\mathcal{O}_Y)", "\\lambda^\\sharp:\\rho^*(\\mathcal{O}_Y)", convention=9)
add(p, "(16.2.1): 'un ρ-morphisme (0_I, 3.5.1)'",
    "(𝟎_I, 3.5.1): bold 0", "(0\\textsubscript{I}, 3.5.1)", "convention",
    "(0\\textsubscript{I}, 3.5.1)", "(\\textbf{0}\\textsubscript{I}, 3.5.1)", convention=2)
add(p, "diagram (16.2.1.4), top left: ρ*(S•_{O_Y}(Gr_1(f)))",
    "bold upright S (symmetric algebra), crop at 1.5x", "\\mathscr{S} (script S)", "font",
    "\\rho^*(\\mathscr{S}_{\\mathcal{O}_Y}^{\\bullet}", "\\rho^*(\\mathbf{S}_{\\mathcal{O}_Y}^{\\bullet}",
    note="ega4-16 writes the symmetric algebra \\mathscr{S} 42 times; the print has bold upright S here and in (16.3.1.1) (p. 14).")
add(p, "diagram (16.2.1.4), label of the left vertical arrow: S(gr_1(u))",
    "bold upright S (crop at 5x)", "\\mathscr{S}(\\operatorname{gr}_1(u))", "font",
    "_-{\\mathscr{S}(\\operatorname{gr}_1(u))}", "_-{\\mathbf{S}(\\operatorname{gr}_1(u))}")
add(p, "diagram (16.2.1.4), bottom left: S•_{O_Y'}(Gr_1(f'))",
    "bold upright S", "\\mathscr{S}_{\\mathcal{O}_{Y'}}^{\\bullet}", "font",
    "\\mathscr{S}_{\\mathcal{O}_{Y'}}^{\\bullet}", "\\mathbf{S}_{\\mathcal{O}_{Y'}}^{\\bullet}")
add(p, "diagram (16.2.1.4), bottom left: S•_{O_Y'}(Gr_1(f')))",
    "three closing parentheses after f' (two opening ones): 'S•_{O_Y'}(Gr_1(f')))' (crop at 1.5x)",
    "(\\mathscr{G}r_1(f')) (balanced): silent correction", "misprint_in_print",
    "(\\mathscr{G}r_1(f'))", "(\\mathscr{G}r_1(f')))",
    corrected="(\\mathscr{G}r_1(f'))",
    note="The printed bottom-left entry repeats the three closing parentheses of the top-left entry ρ*(S(Gr_1(f))). Does not overlap the font fix of the same entry (previous finding).")
add(p, "(16.2.1), last paragraph: 'tel que θ''♯ soit surjectif'",
    "θ''♯ (sharp sign)", "\\theta''^\\#", "convention",
    "$\\theta''^\\#$", "$\\theta''^\\sharp$", convention=9)
add(p, "(16.2.1), last paragraph: 'des définitions et de (0_I, 3.5.5)'",
    "(𝟎_I, 3.5.5): bold 0", "(0\\textsubscript{I}, 3.5.5)", "convention",
    "(0\\textsubscript{I}, 3.5.5)", "(\\textbf{0}\\textsubscript{I}, 3.5.5)", convention=2)
add(p, "(16.2.1), last sentence: 'les Y^(n) et Gr•(f) dépendent fonctoriellement de f.'",
    "'dépendent fonctoriellement de f' italic (crop)", "upright (roman env)", "italics",
    "dépendent fonctoriellement de $f$.", "\\emph{dépendent fonctoriellement de $f$}.")
add(p, "Proposition (16.2.2): 'Avec les notations et hypothèses de (16.2.1)'",
    "(16.2.1) upright in the italic statement", "(16.2.1) italic (proposition environment)", "convention",
    "hypothèses de (16.2.1), supposons", "hypothèses de \\textup{(16.2.1)}, supposons", convention=6)
add(p, "Proposition (16.2.2), label (i)",
    "(i) upright", "\\item[(i)] italic in the proposition environment", "convention",
    "\\item[(i)] Les morphismes", "\\item[\\textup{(i)}] Les morphismes", convention=6)
add(p, "Proposition (16.2.2), label (ii)",
    "(ii) upright", "\\item[(ii)] italic", "convention",
    "\\item[(ii)] Si", "\\item[\\textup{(ii)}] Si", convention=6)
add(p, "Proposition (16.2.2) (ii): 'si f est une immersion ou si v est plat'",
    "'ou' roman inside the italic statement (crop at 2x)", "ou (italic)", "convention",
    "immersion ou si $v$", "immersion \\textup{ou} si $v$", convention=6)
add(p, "Proposition (16.2.2), label (iii)",
    "(iii) upright", "\\item[(iii)] italic", "convention",
    "\\item[(iii)] Si", "\\item[\\textup{(iii)}] Si", convention=6)
add(p, "Proposition (16.2.2) (iii): '(resp. si f est une immersion)'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention",
    "(resp. si $f$ est une\nimmersion)", "\\textup{(resp.} si $f$ est une\nimmersion\\textup{)}", convention=6)
add(p, "Proposition (16.2.2) (iii): 'est bijectif (resp. surjectif).'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention",
    "bijectif (resp. surjectif).", "bijectif \\textup{(resp.} surjectif\\textup{)}.", convention=6)
add(p, "proof of (16.2.2) (i): 'ρ*_{y'}(θ♯_{ψ'(y')})'",
    "θ♯ (sharp sign)", "\\theta_{\\psi'(y')}^\\#", "convention",
    "\\theta_{\\psi'(y')}^\\#", "\\theta_{\\psi'(y')}^\\sharp", convention=9)
add(p, "proof of (16.2.2) (i): 'est un homomorphisme local'",
    "'local' italic", "upright", "italics",
    "un homomorphisme local", "un homomorphisme \\emph{local}")
add(p, "proof of (16.2.2) (i): '(I, 1.6.2)'",
    "bold I", "(I, 1.6.2)", "convention",
    "(I, 1.6.2)", "(\\textbf{I}, 1.6.2)", convention=2)
add(p, "proof of (16.2.2) (i): '(I, 2.2.1)'",
    "bold I", "(I, 2.2.1)", "convention",
    "(I, 2.2.1)", "(\\textbf{I}, 2.2.1)", convention=2)

# ---------------------------------------------------------------- page 11
p = 11
add(p, "proof of (16.2.2) (ii)/(iii), l. 2: 'l'Idéal quasi-cohérent 𝒥 de O_X'",
    "script J (descender; crop at 2x)", "\\mathscr{I}", "symbol",
    "quasi-cohérent $\\mathscr{I}$ de", "quasi-cohérent $\\mathscr{J}$ de", note=J_NOTE)
add(p, "proof of (16.2.2), l. 2: 'Y^(n) par l'Idéal 𝒥^{n+1}'",
    "script J", "\\mathscr{I}^{n+1}", "symbol",
    "$\\mathscr{I}^{n+1}$; les assertions", "$\\mathscr{J}^{n+1}$; les assertions", note="As above.")
add(p, "proof of (16.2.2), l. 3: '(I, 4.4.5)'",
    "bold I", "(I, 4.4.5)", "convention",
    "(I, 4.4.5)", "(\\textbf{I}, 4.4.5)", convention=2)
add(p, "proof of (16.2.2): 'Supposons en second lieu que v soit plat ;'",
    "'plat' italic (crop)", "upright", "italics",
    "soit plat; on peut", "soit \\emph{plat}; on peut")
add(p, "proof of (16.2.2): 'si 𝔍 est le noyau de l'homomorphisme A→B'",
    "Fraktur J (descender; crops)", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}$ est le noyau", "$\\mathfrak{J}$ est le noyau", note=FJ_NOTE)
add(p, "proof of (16.2.2): 'le noyau 𝔍' de A'→B' s'identifie à 𝔍⊗_A A''",
    "Fraktur J (twice)", "\\mathfrak{I}' ... \\mathfrak{I}\\otimes_A A'", "symbol",
    "$\\mathfrak{I}'$ de $A'\\to B'$ s'identifie à $\\mathfrak{I}\\otimes_A A'$",
    "$\\mathfrak{J}'$ de $A'\\to B'$ s'identifie à $\\mathfrak{J}\\otimes_A A'$", note="As above.")
add(p, "proof of (16.2.2): 'par platitude, et 𝔍'^n/𝔍'^{n+1}=(𝔍^n/𝔍^{n+1})⊗_A A'. On en déduit'",
    "formula in the running text (line 'de A'→B' s'identifie à ... par platitude, et ...=(...)⊗_A A'. On en')",
    "set as a display \\[ ... \\] with the full stop inside", "other",
    "platitude, et\n\\[\n  \\mathfrak{I}'^n/\\mathfrak{I}'^{n+1}\n  =(\\mathfrak{I}^n/\\mathfrak{I}^{n+1})\\otimes_A A'.\n\\]\nOn en déduit",
    "platitude, et\n$\\mathfrak{J}'^n/\\mathfrak{J}'^{n+1}=(\\mathfrak{J}^n/\\mathfrak{J}^{n+1})\\otimes_A A'$. On en déduit",
    note="One edit: inline formula as printed, and the Fraktur J of the print (same letter fix as the neighbouring findings; no separate letter finding for this formula).")
add(p, "proof of (16.2.2): 'compte tenu de (0_I, 4.3.3)'",
    "bold 0", "(0\\textsubscript{I}, 4.3.3)", "convention",
    "(0\\textsubscript{I}, 4.3.3)", "(\\textbf{0}\\textsubscript{I}, 4.3.3)", convention=2)
add(p, "proof of (16.2.2): 'le O_Y'-Module 𝒥'^n/𝒥'^{n+1} est égal à'",
    "script J", "\\mathscr{I}'^n/\\mathscr{I}'^{n+1}", "symbol",
    "$\\mathscr{I}'^n/\\mathscr{I}'^{n+1}$ est égal à", "$\\mathscr{J}'^n/\\mathscr{J}'^{n+1}$ est égal à", note=J_NOTE)
add(p, "display after 'est égal à', first line: ψ'*(σ*((𝔍^n/𝔍^{n+1})~)⊗_{σ*(O_X)}O_X')",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "&\\psi'^*\\!\\left(\\sigma^*\n  \\left((\\mathfrak{I}^n/\\mathfrak{I}^{n+1})",
    "&\\psi'^*\\!\\left(\\sigma^*\n  \\left((\\mathfrak{J}^n/\\mathfrak{J}^{n+1})", note=FJ_NOTE)
add(p, "display after 'est égal à', first line",
    "ψ'*(σ*((𝔍^n/𝔍^{n+1})~)⊗_{σ*(O_X)}O_X'): the tensor product is inside ψ'*( ), one parenthesis after the tilde and one after O_X' (stitched crop)",
    "\\psi'^*(\\sigma^*(...)^{\\sim})) \\otimes_{\\sigma^*(\\mathcal{O}_X)}\\mathcal{O}_{X'}: ψ'* closed before the tensor product",
    "formula",
    "\\right)\\right)\n  \\otimes_{\\sigma^*(\\mathcal{O}_X)}\\mathcal{O}_{X'} \\\\",
    "\\right)\n  \\otimes_{\\sigma^*(\\mathcal{O}_X)}\\mathcal{O}_{X'}\\right) \\\\",
    note="The printed bracketing is ψ'*(v*(sheaf)) with v* = σ*(..)⊗_{σ*(O_X)}O_X', which the next line expands. The \\left( after ψ'^* now closes after O_X'.")
add(p, "display after 'est égal à', second line: ψ'*(σ*((𝔍^n/𝔍^{n+1})~))⊗...",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "={}&\n\\psi'^*\\!\\left(\\sigma^*\n  \\left((\\mathfrak{I}^n/\\mathfrak{I}^{n+1})",
    "={}&\n\\psi'^*\\!\\left(\\sigma^*\n  \\left((\\mathfrak{J}^n/\\mathfrak{J}^{n+1})", note=FJ_NOTE)
add(p, "display after 'est égal à', last term: ρ*(𝒥^n/𝒥^{n+1})⊗_{ρ*(ψ*(O_X))}ψ'*(O_X')",
    "script J", "\\mathscr{I}", "symbol",
    "\\rho^*(\\mathscr{I}^n/\\mathscr{I}^{n+1})\n  \\otimes_{\\rho^*(\\psi^*(\\mathcal{O}_X))}",
    "\\rho^*(\\mathscr{J}^n/\\mathscr{J}^{n+1})\n  \\otimes_{\\rho^*(\\psi^*(\\mathcal{O}_X))}", note=J_NOTE)
add(p, "end of the display after 'est égal à'",
    "no punctuation after ψ'*(O_X') (crop at 3x)", "comma before \\end{align*}", "punctuation",
    "  \\psi'^*(\\mathcal{O}_{X'}),\n\\end{align*}", "  \\psi'^*(\\mathcal{O}_{X'})\n\\end{align*}")
add(p, "display 'O_Y' = ρ*(O_Y)⊗_{ρ*(ψ*(O_X))}ψ'*(O_X')'",
    "no punctuation at the end (crop)", "comma at the end", "punctuation",
    "  \\psi'^*(\\mathcal{O}_{X'}),\n\\]", "  \\psi'^*(\\mathcal{O}_{X'})\n\\]")
add(p, "'on obtient un isomorphisme canonique de 𝒥'^n/𝒥'^{n+1} sur'",
    "script J", "\\mathscr{I}", "symbol",
    "$\\mathscr{I}'^n/\\mathscr{I}'^{n+1}$ sur", "$\\mathscr{J}'^n/\\mathscr{J}'^{n+1}$ sur", note=J_NOTE)
add(p, "display 'ρ*(𝒥^n/𝒥^{n+1})⊗_{ρ*(O_Y)}O_Y' = ...', left side",
    "script J", "\\mathscr{I}", "symbol",
    "  \\rho^*(\\mathscr{I}^n/\\mathscr{I}^{n+1})\n  \\otimes_{\\rho^*(\\mathcal{O}_Y)}",
    "  \\rho^*(\\mathscr{J}^n/\\mathscr{J}^{n+1})\n  \\otimes_{\\rho^*(\\mathcal{O}_Y)}", note=J_NOTE)
add(p, "same display, right side '(𝒥^n/𝒥^{n+1})⊗_{O_Y}O_Y''",
    "script J", "\\mathscr{I}", "symbol",
    "  =\n  (\\mathscr{I}^n/\\mathscr{I}^{n+1})", "  =\n  (\\mathscr{J}^n/\\mathscr{J}^{n+1})", note=J_NOTE)
add(p, "end of the same display, before 'ce qui prouve (iii)'",
    "no punctuation after O_Y' (crop)", "comma at the end", "punctuation",
    "\\mathcal{O}_{Y'},\n\\]\nce qui", "\\mathcal{O}_{Y'}\n\\]\nce qui")
add(p, "'est Γ(Y, 𝒥^n/𝒥^{n+1}) (resp.'",
    "script J", "\\mathscr{I}", "symbol",
    "$\\Gamma(Y,\\mathscr{I}^n/\\mathscr{I}^{n+1})$", "$\\Gamma(Y,\\mathscr{J}^n/\\mathscr{J}^{n+1})$", note=J_NOTE)
add(p, "'(resp. Γ(Y', 𝒥'^n/𝒥'^{n+1}))'",
    "script J", "\\mathscr{I}", "symbol",
    "$\\Gamma(Y',\\mathscr{I}'^n/\\mathscr{I}'^{n+1})$", "$\\Gamma(Y',\\mathscr{J}'^n/\\mathscr{J}'^{n+1})$", note=J_NOTE)
add(p, "diagram with rows 0→𝔎_n⊗A'→C_n⊗A'→C_{n-1}⊗A'→0: label r",
    "r to the LEFT of the first vertical arrow (crop)", "\\ar[d]^r (label on the right)", "other",
    "\\ar[d]^r &", "\\ar[d]_r &", note="xymatrix: ^ puts the label of a downward arrow on its right, _ on its left.")
add(p, "same diagram: label s_n",
    "s_n to the left of the arrow", "\\ar[d]^{s_n} (right)", "other",
    "\\ar[d]^{s_n}", "\\ar[d]_{s_n}")
add(p, "same diagram: label s_{n-1}",
    "s_{n-1} to the left of the arrow", "\\ar[d]^{s_{n-1}} (right)", "other",
    "\\ar[d]^{s_{n-1}}", "\\ar[d]_{s_{n-1}}")
add(p, "Corollaire (16.2.3), label (i)",
    "(i) upright", "\\item[(i)] italic", "convention",
    "\\item[(i)] Le morphisme", "\\item[\\textup{(i)}] Le morphisme", convention=6)
add(p, "Corollaire (16.2.3) (i): 'correspondant à f, f', u, v (16.2.1)'",
    "(16.2.1) upright", "italic", "convention",
    "(16.2.1) et le morphisme", "\\textup{(16.2.1)} et le morphisme", convention=6)
add(p, "Corollaire (16.2.3), label (ii)",
    "(ii) upright", "\\item[(ii)] italic", "convention",
    "\\item[(ii)] Si l'on munit", "\\item[\\textup{(ii)}] Si l'on munit", convention=6)
add(p, "Corollaire (16.2.3) (ii): '(resp. O_{Y'^{(n)}_{f'}})'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention",
    "(resp.\n$\\mathcal{O}_{Y_{f'}'^{(n)}}$)", "\\textup{(resp.}\n$\\mathcal{O}_{Y_{f'}'^{(n)}}$\\textup{)}", convention=6)
add(p, "Corollaire (16.2.3) (ii): '(resp. de la structure de O_Y'-Algèbre définie par g')'",
    "'(resp.' and the closing parenthesis roman, the words between italic", "italic", "convention",
    "(resp. de la structure de $\\mathcal{O}_{Y'}$-Algèbre définie\npar $g'$)",
    "\\textup{(resp.} de la structure de $\\mathcal{O}_{Y'}$-Algèbre définie\npar $g'$\\textup{)}", convention=6)
add(p, "Corollaire (16.2.3) (ii): '(16.1.6)'",
    "(16.1.6) upright", "italic", "convention",
    " (16.1.6), l'homomorphisme", " \\textup{(16.1.6)}, l'homomorphisme", convention=6)

# ---------------------------------------------------------------- page 12
p = 12
add(p, "Corollaire (16.2.3) (ii), continued: 'déduit de l'homomorphisme ν_n (16.2.1.2)'",
    "(16.2.1.2) upright", "italic", "convention",
    "$\\nu_n$ (16.2.1.2)", "$\\nu_n$ \\textup{(16.2.1.2)}", convention=6)
add(p, "proof of (16.2.3) (i): 'le morphisme g étant une immersion'",
    "'g' (crop at 3x)", "$g$ (keeps the printed reading)", "misprint_in_print",
    None, None, confidence="medium",
    corrected="le morphisme $f$ étant une immersion",
    note="(16.2.2, (ii)) needs f to be an immersion (or v flat); here f is a Y-section of X, hence an immersion, while g: X→Y is arbitrary.")
add(p, "proof of (16.2.3) (ii), diagram: label h_n",
    "h_n to the LEFT of the left arrow Y_f^(n)→X (crop)", "\\ar[d]^{h_n} (right)", "other",
    "Y_f^{(n)} \\ar[d]^{h_n}", "Y_f^{(n)} \\ar[d]_{h_n}")
add(p, "same diagram: label w_n of the top arrow Y'_f'^(n)→Y_f^(n)",
    "w_n ABOVE the leftward arrow (crop)", "\\ar[l]^{w_n} (below a leftward arrow)", "other",
    "\\ar[l]^{w_n}", "\\ar[l]_{w_n}", note="xymatrix: for a leftward arrow ^ puts the label below, _ above (cf. GLOBAL_ISSUES 30); the labels v and u below their arrows are right.")
add(p, "same diagram: label g of the arrow X→Y",
    "g to the LEFT of the arrow (crop)", "X \\ar[d]^g (right)", "other",
    "X \\ar[d]^g", "X \\ar[d]_g")
add(p, "proof of (16.2.3) (ii): 'donc (I, 3.3.9) il identifie'",
    "bold I", "(I, 3.3.9)", "convention",
    "(I, 3.3.9)", "(\\textbf{I}, 3.3.9)", convention=2)
add(p, "proof of (16.2.3) (ii): 'résulte de (II, 1.5.2)'",
    "bold II", "(II, 1.5.2)", "convention",
    "(II, 1.5.2)", "(\\textbf{II}, 1.5.2)", convention=2)
add(p, "proof of (16.2.3) (ii): 'l'Idéal d'augmentation 𝒥/𝒥^{n+1}'",
    "script J", "\\mathscr{I}", "symbol",
    "$\\mathscr{I}/\\mathscr{I}^{n+1}$, on voit", "$\\mathscr{J}/\\mathscr{J}^{n+1}$, on voit", note=J_NOTE)
add(p, "proof of (16.2.3) (ii): 'restreint à (𝒥/𝒥^{n+1})⊗_{O_Y}O_Y''",
    "script J", "\\mathscr{I}", "symbol",
    "$(\\mathscr{I}/\\mathscr{I}^{n+1})\\otimes", "$(\\mathscr{J}/\\mathscr{J}^{n+1})\\otimes", note=J_NOTE)
add(p, "proof of (16.2.3) (ii): 'est une bijection de ce dernier'",
    "'bijection' italic", "upright", "italics",
    "est une bijection de", "est une \\emph{bijection} de")
add(p, "proof of (16.2.3) (ii): 'sur 𝒥'/𝒥'^{n+1}'",
    "script J", "\\mathscr{I}", "symbol",
    "$\\mathscr{I}'/\\mathscr{I}'^{n+1}$. Pour", "$\\mathscr{J}'/\\mathscr{J}'^{n+1}$. Pour", note=J_NOTE)
add(p, "'les homomorphismes Gr_n(u) sont surjectifs en vertu de ce qui précède'",
    "'surjectifs' italic", "upright", "italics",
    "sont surjectifs en vertu", "sont \\emph{surjectifs} en vertu")
add(p, "Corollaire (16.2.4): 'Sous les hypothèses de (16.2.3)'",
    "(16.2.3) upright", "italic", "convention",
    "de (16.2.3), supposons", "de \\textup{(16.2.3)}, supposons", convention=6)
add(p, "Corollaire (16.2.4): '(resp. que les Gr_n(f) soient des O_Y-Modules plats pour n≤m)'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention",
    "(resp. que les $\\mathscr{G}r_n(f)$ soient des $\\mathcal{O}_Y$-Modules\nplats pour $n\\leq m$).",
    "\\textup{(resp.} que les $\\mathscr{G}r_n(f)$ soient des $\\mathcal{O}_Y$-Modules\nplats pour $n\\leq m$\\textup{)}.",
    convention=6)
add(p, "Corollaire (16.2.4), end: '(resp. pour n≤m)'",
    "'(resp.' and the closing parenthesis roman", "italic", "convention",
    "(resp. pour $n\\leq m$).", "\\textup{(resp.} pour $n\\leq m$\\textup{)}.", convention=6)
add(p, "proof of (16.2.4): 'il en est de même des 𝒥/𝒥^{n+1} pour n≤m'",
    "script J", "\\mathscr{I}", "symbol",
    "$\\mathscr{I}/\\mathscr{I}^{n+1}$ pour", "$\\mathscr{J}/\\mathscr{J}^{n+1}$ pour", note=J_NOTE)
add(p, "display 0→𝒥^n/𝒥^{n+1}→𝒥/𝒥^{n+1}→𝒥/𝒥^n→0",
    "script J (six times)", "\\mathscr{I}", "symbol",
    "0\\longrightarrow\\mathscr{I}^n/\\mathscr{I}^{n+1}\n  \\longrightarrow\\mathscr{I}/\\mathscr{I}^{n+1}\n  \\longrightarrow\\mathscr{I}/\\mathscr{I}^n",
    "0\\longrightarrow\\mathscr{J}^n/\\mathscr{J}^{n+1}\n  \\longrightarrow\\mathscr{J}/\\mathscr{J}^{n+1}\n  \\longrightarrow\\mathscr{J}/\\mathscr{J}^n",
    note=J_NOTE)

# ---------------------------------------------------------------- page 13
p = 13
add(p, "l. 1: '(0_I, 6.1.2); en outre'",
    "bold 0", "(0\\textsubscript{I}, 6.1.2)", "convention",
    "(0\\textsubscript{I}, 6.1.2); en outre", "(\\textbf{0}\\textsubscript{I}, 6.1.2); en outre", convention=2)
add(p, "diagram, top row: (𝒥^n/𝒥^{n+1})⊗..., (𝒥/𝒥^{n+1})⊗..., (𝒥/𝒥^n)⊗...",
    "script J (six times)", "\\mathscr{I}", "symbol",
    "(\\mathscr{I}^n/\\mathscr{I}^{n+1})\n      \\otimes_{\\mathcal{O}_Y}\\mathcal{O}_{Y'}\n      \\ar[r]\\ar[d] &\n    (\\mathscr{I}/\\mathscr{I}^{n+1})\n      \\otimes_{\\mathcal{O}_Y}\\mathcal{O}_{Y'}\n      \\ar[r]\\ar[d] &\n    (\\mathscr{I}/\\mathscr{I}^n)",
    "(\\mathscr{J}^n/\\mathscr{J}^{n+1})\n      \\otimes_{\\mathcal{O}_Y}\\mathcal{O}_{Y'}\n      \\ar[r]\\ar[d] &\n    (\\mathscr{J}/\\mathscr{J}^{n+1})\n      \\otimes_{\\mathcal{O}_Y}\\mathcal{O}_{Y'}\n      \\ar[r]\\ar[d] &\n    (\\mathscr{J}/\\mathscr{J}^n)",
    note=J_NOTE)
add(p, "diagram, bottom row: 𝒥'^n/𝒥'^{n+1}, 𝒥'/𝒥'^{n+1}, 𝒥'/𝒥'^n",
    "script J (six times)", "\\mathscr{I}", "symbol",
    "\\mathscr{I}'^n/\\mathscr{I}'^{n+1}\n      \\ar[r] &\n    \\mathscr{I}'/\\mathscr{I}'^{n+1}\n      \\ar[r] &\n    \\mathscr{I}'/\\mathscr{I}'^n",
    "\\mathscr{J}'^n/\\mathscr{J}'^{n+1}\n      \\ar[r] &\n    \\mathscr{J}'/\\mathscr{J}'^{n+1}\n      \\ar[r] &\n    \\mathscr{J}'/\\mathscr{J}'^n",
    note=J_NOTE)
add(p, "'(la première par platitude (0_I, 6.1.2))'",
    "bold 0", "(0\\textsubscript{I}, 6.1.2))", "convention",
    "(0\\textsubscript{I}, 6.1.2)) et", "(\\textbf{0}\\textsubscript{I}, 6.1.2)) et", convention=2)
add(p, "Remarques (16.2.5) (i): 'de morphismes d'espaces annelés en anneaux locaux'",
    "'espaces annelés en anneaux locaux' italic in the roman remark ('d'' roman; crop)",
    "no emphasis (remark body judged as roman)", "italics",
    "d'espaces annelés en anneaux locaux", "d'\\emph{espaces annelés en anneaux locaux}")
add(p, "Remarques (16.2.5) (ii): 'Par exemple (avec les notations de la démonstration de (16.2.2, (ii)), il peut se faire'",
    "the parenthesis opened before 'avec' is never closed (crop)", "same unbalanced text (keeps the printed reading)",
    "misprint_in_print", None, None, confidence="high",
    corrected="Par exemple (avec les notations de la\ndémonstration de (16.2.2, (ii))), il peut",
    note="Missing closing parenthesis in the print.")
add(p, "Remarques (16.2.5) (ii): 'il peut se faire que 𝔍=0'",
    "Fraktur J (descender; crop)", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}=0$ mais", "$\\mathfrak{J}=0$ mais", note=FJ_NOTE)
add(p, "Remarques (16.2.5) (ii): 'le noyau 𝔍' de A'→B''",
    "Fraktur J", "\\mathfrak{I}'", "symbol",
    "le noyau $\\mathfrak{I}'$ de", "le noyau $\\mathfrak{J}'$ de", note=FJ_NOTE)
add(p, "(16.2.6), l. 2-3: 'Y' un sous-préschéma, de Y, f, u et f'=f∘u'",
    "comma after 'sous-préschéma' at the line end (crop at 2.5x)", "'sous-préschéma de $Y$' without comma: silent correction",
    "misprint_in_print",
    "sous-préschéma de $Y$, $f$", "sous-préschéma, de $Y$, $f$",
    corrected="sous-préschéma de $Y$, $f$",
    note="Spurious comma between 'sous-préschéma' and its complement 'de Y'.")
add(p, "display (16.2.6.1) u*(Gr•(f)) → Gr•(f').",
    "full stop at the end (crop at 3x)", "no punctuation", "punctuation",
    "\\longrightarrow\\mathscr{G}r_\\bullet(f')\n  \\tag{16.2.6.1}", "\\longrightarrow\\mathscr{G}r_\\bullet(f').\n  \\tag{16.2.6.1}")
add(p, "(16.2.6): 'on identifie O_Y à ψ*(O_X)/𝒥_f'",
    "script J", "\\mathscr{I}_f", "symbol",
    "$\\psi^*(\\mathcal{O}_X)/\\mathscr{I}_f$", "$\\psi^*(\\mathcal{O}_X)/\\mathscr{J}_f$", note=J_NOTE)
add(p, "(16.2.6): 'O_Y' à ρ*(O_Y)/𝒥_u'",
    "script J", "\\mathscr{I}_u", "symbol",
    "$\\rho^*(\\mathcal{O}_Y)/\\mathscr{I}_u$", "$\\rho^*(\\mathcal{O}_Y)/\\mathscr{J}_u$", note=J_NOTE)
add(p, "(16.2.6): 'ρ*(O_Y)=ρ*(ψ*(O_X))/ρ*(𝒥_f)=ψ'*(O_X)/ρ*(𝒥_f)'",
    "script J (twice)", "\\mathscr{I}_f", "symbol",
    "/\\rho^*(\\mathscr{I}_f)=\n\\psi'^*(\\mathcal{O}_X)/\\rho^*(\\mathscr{I}_f)$",
    "/\\rho^*(\\mathscr{J}_f)=\n\\psi'^*(\\mathcal{O}_X)/\\rho^*(\\mathscr{J}_f)$", note=J_NOTE)
add(p, "(16.2.6): 's'identifie par ailleurs à ψ'*(O_X)/𝒥_f''",
    "script J", "\\mathscr{I}_{f'}", "symbol",
    "/\\mathscr{I}_{f'}$", "/\\mathscr{J}_{f'}$", note=J_NOTE)
add(p, "(16.2.6): 'ψ'*(O_X)/𝒥_f' on voit que l'on a'",
    "no comma before 'on voit' (crop)", "'$, on voit'", "punctuation",
    ", on voit que l'on a", " on voit que l'on a",
    note="Adjacent to the letter fix before it (no overlap).")
add(p, "(16.2.6): '𝒥_u=𝒥_f'/ρ*(𝒥_f)'",
    "script J (three times)", "\\mathscr{I}", "symbol",
    "$\\mathscr{I}_u=\\mathscr{I}_{f'}/\\rho^*(\\mathscr{I}_f)$", "$\\mathscr{J}_u=\\mathscr{J}_{f'}/\\rho^*(\\mathscr{J}_f)$", note=J_NOTE)
add(p, "(16.2.6): '𝒥^n_f'/𝒥^{n+1}_f' → 𝒥^n_u/𝒥^{n+1}_u'",
    "script J (four times)", "\\mathscr{I}", "symbol",
    "$\\mathscr{I}_{f'}^n/\\mathscr{I}_{f'}^{n+1}\\to\n\\mathscr{I}_u^n/\\mathscr{I}_u^{n+1}$",
    "$\\mathscr{J}_{f'}^n/\\mathscr{J}_{f'}^{n+1}\\to\n\\mathscr{J}_u^n/\\mathscr{J}_u^{n+1}$", note=J_NOTE)
add(p, "Proposition (16.2.7): 'des homomorphismes canoniques (16.2.6.1)'",
    "(16.2.6.1) upright ('et' after it italic)", "italic", "convention",
    "(16.2.6.1)", "\\textup{(16.2.6.1)}", convention=6)
add(p, "Proposition (16.2.7): 'et (16.2.6.2).'",
    "(16.2.6.2) upright", "italic", "convention",
    "et (16.2.6.2).", "et \\textup{(16.2.6.2)}.", convention=6)
add(p, "proof of (16.2.7): 'Y=Spec(A/𝔍)'",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "\\operatorname{Spec}(A/\\mathfrak{I})$", "\\operatorname{Spec}(A/\\mathfrak{J})$", note=FJ_NOTE)
add(p, "proof of (16.2.7): '𝔍 et 𝔎 étant deux idéaux'",
    "Fraktur J (crop at 4x)", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}$ et $\\mathfrak{K}$", "$\\mathfrak{J}$ et $\\mathfrak{K}$", note=FJ_NOTE)
add(p, "proof of (16.2.7): 'tels que 𝔍⊂𝔎'",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}\\subset\\mathfrak{K}$", "$\\mathfrak{J}\\subset\\mathfrak{K}$", note=FJ_NOTE)

# ---------------------------------------------------------------- page 14
p = 14
add(p, "l. 1: 'la suite d'homomorphismes canoniques 𝔍/𝔎𝔍 → 𝔎/𝔎² → (𝔎/𝔍)/(𝔎/𝔍)² → 0'",
    "Fraktur J (four times; crop at 4x)", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}/\\mathfrak{K}\\mathfrak{I}\\to\n\\mathfrak{K}/\\mathfrak{K}^2\\to\n(\\mathfrak{K}/\\mathfrak{I})/(\\mathfrak{K}/\\mathfrak{I})^2\\to 0$",
    "$\\mathfrak{J}/\\mathfrak{K}\\mathfrak{J}\\to\n\\mathfrak{K}/\\mathfrak{K}^2\\to\n(\\mathfrak{K}/\\mathfrak{J})/(\\mathfrak{K}/\\mathfrak{J})^2\\to 0$",
    note=FJ_NOTE)
add(p, "l. 2: 'l'image de 𝔍/𝔎𝔍 dans 𝔎/𝔎²'",
    "Fraktur J (twice)", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}/\\mathfrak{K}\\mathfrak{I}$ dans", "$\\mathfrak{J}/\\mathfrak{K}\\mathfrak{J}$ dans", note=FJ_NOTE)
add(p, "l. 2: 'est (𝔍+𝔎²)/𝔎² et que'",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "$(\\mathfrak{I}+\\mathfrak{K}^2)/\\mathfrak{K}^2$ et que", "$(\\mathfrak{J}+\\mathfrak{K}^2)/\\mathfrak{K}^2$ et que", note=FJ_NOTE)
add(p, "l. 3: '(𝔎/𝔍)/(𝔎/𝔍)² s'identifie à 𝔎/(𝔍+𝔎²)'",
    "Fraktur J (twice)", "\\mathfrak{I}", "symbol",
    "$(\\mathfrak{K}/\\mathfrak{I})/(\\mathfrak{K}/\\mathfrak{I})^2$ s'identifie", "$(\\mathfrak{K}/\\mathfrak{J})/(\\mathfrak{K}/\\mathfrak{J})^2$ s'identifie", note=FJ_NOTE)
add(p, "l. 3: '𝔎/(𝔍+𝔎²).'",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{K}/(\\mathfrak{I}+\\mathfrak{K}^2)$.", "$\\mathfrak{K}/(\\mathfrak{J}+\\mathfrak{K}^2)$.", note=FJ_NOTE)
add(p, "example after (16.2.7): '𝔍=AT²'",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}=AT^2$", "$\\mathfrak{J}=AT^2$", note=FJ_NOTE)
add(p, "example after (16.2.7): '(𝔍+𝔎²)/𝔎²=0'",
    "Fraktur J", "\\mathfrak{I}", "symbol",
    "$(\\mathfrak{I}+\\mathfrak{K}^2)/\\mathfrak{K}^2=0$", "$(\\mathfrak{J}+\\mathfrak{K}^2)/\\mathfrak{K}^2=0$", note=FJ_NOTE)
add(p, "example after (16.2.7): '𝔍/𝔎𝔍≠0'",
    "Fraktur J (twice)", "\\mathfrak{I}", "symbol",
    "$\\mathfrak{I}/\\mathfrak{K}\\mathfrak{I}\\neq 0$", "$\\mathfrak{J}/\\mathfrak{K}\\mathfrak{J}\\neq 0$", note=FJ_NOTE)
add(p, "heading 16.3",
    "'16.3. Invariants différentiels fondamentaux d'un morphisme de préschémas.' (final full stop)",
    "\\subsection{...} without the full stop", "punctuation",
    "de préschémas}", "de préschémas.}", note="GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop).")
add(p, "Définition (16.3.1): 'qui est une immersion (I, 5.3.9 et Err_III, 10)'",
    "bold I", "(I, 5.3.9 et", "convention",
    "(I, 5.3.9 et\n$\\mathbf{Err}_{\\mathrm{III}}$, 10)",
    "\\textup{(\\textbf{I}, 5.3.9} et\n\\textup{$\\mathbf{Err}_{\\mathrm{III}}$, 10)}", convention=2,
    note="One edit for this finding and the next (convention 6): bold I and the upright reference ('et' stays italic, as printed).")
add(p, "Définition (16.3.1): same reference '(I, 5.3.9 et Err_III, 10)'",
    "parentheses, I, 5.3.9 and Err_III, 10 upright in the italic definition; 'et' italic", "italic (definition environment)",
    "convention", None, None, convention=6,
    note="Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(p, "Définition (16.3.1): 'et l'on appelle faisceau des parties principales d'ordre n du S-préschéma X'",
    "the defined term is roman inside the italic definition (n italic)", "italic", "convention",
    "faisceau des parties principales d'ordre $n$\ndu $S$-préschéma $X$, le",
    "\\textup{faisceau des parties principales d'ordre $n$\ndu $S$-préschéma $X$}, le", convention=6)
add(p, "Définition (16.3.1): 'n-ème invariant normal de Δ_f (16.1.2)'",
    "(16.1.2) upright", "italic", "convention",
    "$\\Delta_f$ (16.1.2). On pose", "$\\Delta_f$ \\textup{(16.1.2)}. On pose", convention=6)
add(p, "Définition (16.3.1): 'Gr_n(Δ_f) (16.1.2); le O_X-Module'",
    "(16.1.2) upright", "italic", "convention",
    "(\\Delta_f)$ (16.1.2); le", "(\\Delta_f)$ \\textup{(16.1.2)}; le", convention=6)
add(p, "Définition (16.3.1): 'est aussi noté Ω¹_f ou Ω¹_X/S'",
    "italic (slanted) capital Omega (crop)", "\\Omega (upright)", "font",
    "$\\Omega_f^1$ ou $\\Omega_{X/S}^1$", "$\\varOmega_f^1$ ou $\\varOmega_{X/S}^1$",
    note="The print's Ω of the differentials is italic on all of p. 14 (here, in (16.3.1.1) and in Ω¹_{f|U}=Ω¹_f|U); \\varOmega (amsmath) gives it. ega4-16/17/18 have 138/197/219 upright \\Omega: candidate for one pass after a check of other pages.")
add(p, "Définition (16.3.1): 'le O_X-Module des 1-différentielles de f'",
    "'1-différentielles' roman inside the italic definition", "italic", "convention",
    "des 1-différentielles de", "des \\textup{1-différentielles} de", convention=6)
add(p, "display (16.3.1.1): S•_{O_X}(Ω¹_X/S) → Gr•(P_X/S)",
    "bold upright S (crop at 3x)", "\\mathscr{S} (script S)", "font",
    "\\mathscr{S}_{\\mathcal{O}_X}^{\\bullet}", "\\mathbf{S}_{\\mathcal{O}_X}^{\\bullet}",
    note="As for the S of (16.2.1.4), p. 10.")
add(p, "display (16.3.1.1): Ω¹_X/S",
    "italic capital Omega", "\\Omega", "font",
    "(\\Omega_{X/S}^1)\n  \\longrightarrow", "(\\varOmega_{X/S}^1)\n  \\longrightarrow",
    note="See the Ω finding of Définition (16.3.1).")
add(p, "after (16.3.1.1): 'Ω¹_{f|U}=Ω¹_f|U'",
    "italic capital Omega (twice)", "\\Omega", "font",
    "$\\Omega_{f|U}^1=\\Omega_f^1|U$", "$\\varOmega_{f|U}^1=\\varOmega_f^1|U$",
    note="See the Ω finding of Définition (16.3.1).")
add(p, "after (16.3.1.1): 'les notions introduites sont locales sur X)'",
    "'locales' italic (crop)", "upright", "italics",
    "locales sur $X$).", "\\emph{locales} sur $X$).")
add(p, "(16.3.2): 'à la fois pour les morphismes p_1 et p_2, chacun de ces morphismes définit'",
    "'chacun' italic (crop); 'de ces morphismes définit' roman", "upright", "italics",
    "chacun de ces morphismes", "\\emph{chacun} de ces morphismes")
add(p, "(16.3.2): 'on définit ainsi sur P^n_X/S deux structures'",
    "'deux' italic (crop)", "upright", "italics",
    "$ deux structures de", "$ \\emph{deux} structures de")
add(p, "(16.3.2): 'de O_X-Algèbres augmentées quasi-cohérentes ;'",
    "'Algèbres augmentées quasi-cohérentes' italic (crop)", "upright", "italics",
    "-Algèbres augmentées\nquasi-cohérentes;", "-\\emph{Algèbres augmentées\nquasi-cohérentes};")
add(p, "(16.3.3): 'est un automorphisme involutif de X×_S X'",
    "'automorphisme involutif' italic (crop)", "upright", "italics",
    "automorphisme\ninvolutif de", "\\emph{automorphisme\ninvolutif} de")
add(p, "(16.3.3): 'appelé la symétrie canonique, tel que'",
    "'symétrie canonique' italic", "upright", "italics",
    "la symétrie canonique, tel que", "la \\emph{symétrie canonique}, tel que")
add(p, "(16.3.3): 'Δ_f=(δ, ν), λ♯ est donc un isomorphisme'",
    "λ♯ (sharp sign)", "\\lambda^\\#", "convention",
    "$\\lambda^\\#$ est donc", "$\\lambda^\\sharp$ est donc", convention=9)
add(p, "(16.3.3): 'et δ*(λ♯) laisse invariant'",
    "λ♯", "\\lambda^\\#", "convention",
    "$\\delta^*(\\lambda^\\#)$ laisse", "$\\delta^*(\\lambda^\\sharp)$ laisse", convention=9)
add(p, "(16.3.3): 'et le noyau 𝒥 de l'homomorphisme'",
    "script J (crop)", "\\mathscr{I}", "symbol",
    "le noyau $\\mathscr{I}$ de", "le noyau $\\mathscr{J}$ de", note=J_NOTE)
add(p, "(16.3.3): 'ν♯ : δ*(O_{X×_S X})→O_X'",
    "ν♯", "\\nu^\\#", "convention",
    "$\\nu^\\#:", "$\\nu^\\sharp:", convention=9)
add(p, "Proposition (16.3.4): 'L'homomorphisme σ=δ*(λ♯)'",
    "λ♯", "\\lambda^\\#", "convention",
    "\\sigma=\\delta^*(\\lambda^\\#)", "\\sigma=\\delta^*(\\lambda^\\sharp)", convention=9)
add(p, "Proposition (16.3.4): 'déduit de s (et appelé encore symétrie canonique)'",
    "'(et appelé encore' and the closing parenthesis roman, 'symétrie canonique' italic", "italic", "convention",
    "(et appelé encore\nsymétrie canonique)", "\\textup{(et appelé encore}\nsymétrie canonique\\textup{)}", convention=6)

# ---------------------------------------------------------------- checks
errors = []
spans = {}
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    text = pages[f["page"]]
    n = text.count(fx["old"])
    if n != 1:
        errors.append(f"page {f['page']} finding {i}: old occurs {n} times: {fx['old']!r}")
        continue
    start = text.index(fx["old"])
    spans.setdefault(f["page"], []).append((start, start + len(fx["old"]), i))
for page, ss in spans.items():
    ss.sort()
    for (a0, a1, ia), (b0, b1, ib) in zip(ss, ss[1:]):
        if b0 < a1:
            errors.append(f"page {page}: findings {ia} and {ib} overlap")
# apply all fixes per page to be sure they compose
for page in pages:
    t = pages[page]
    for f in F:
        if f["page"] == page and f["fix"]:
            assert t.count(f["fix"]["old"]) == 1, (page, f["fix"]["old"])
            t = t.replace(f["fix"]["old"], f["fix"]["new"])
if errors:
    print("\n".join(errors))
    sys.exit(1)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for page in range(10, 15):
    print(page, c[(page, "normal")], c[(page, "convention")], c[(page, "misprint")])
print("total", len(F), "->", OUT)
