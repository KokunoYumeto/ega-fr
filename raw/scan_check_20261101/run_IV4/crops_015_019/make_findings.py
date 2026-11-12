import json

OUT = r"user\Documents\ega_scan_check_20261101\run_IV4\findings_015_019.json"

OMEGA_NOTE = ("The print sets the sheaf of differentials (Omega^1_{X/S}, Omega^1_f) with an italic Omega and the "
              "module Omega^1_{B/A} with an upright Omega (both on p. 15, (16.3.7)); \\Omega is upright, "
              "amsmath's \\varOmega gives the italic capital. Checked on an enlarged crop.")
FRAK_NOTE = ("The printed letter is the same glyph (with a descender) as the 𝔍_{B/A} of (0, 20.4.1), written "
             "\\mathfrak{J}_{B/A} in ega0-20, and as the 𝔍 of §17 (IV-4 p. 60, \\mathfrak{J} in ega4-17); "
             "ega4-16 writes \\mathfrak{I} throughout (132 times, no \\mathfrak{J}).")
S_NOTE = ("The symmetric algebra is printed with a bold upright S (as in EGA II, 1.7.4); ega4-16 writes "
          "\\mathscr{S} here (42 times in the file) but \\mathbf{S} for the same object at 6 later places.")

F = []
def add(page, where, scan, tex, kind, conv, conf, fix, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)

# ---------------- page 15 ----------------
add(15, "(16.3.5): 'nous conviendrons désormais, ... qu'il s'agira.'",
    "the whole convention, from 'nous conviendrons' to 's'agira', is italic (the start of the paragraph is roman)",
    "roman (env environment, no emphasis)", "italics", None, "high",
    {"old": "nous conviendrons désormais, sauf mention expresse du contraire,\nque lorsque $\\mathscr{P}_{X/S}^n$ ou $\\mathscr{P}_{X/S}^\\infty$ sera considéré\ncomme une $\\mathcal{O}_X$-Algèbre, c'est de la structure d'Algèbre définie par\n$p_1$ qu'il s'agira.",
     "new": "\\emph{nous conviendrons désormais, sauf mention expresse du contraire,\nque lorsque $\\mathscr{P}_{X/S}^n$ ou $\\mathscr{P}_{X/S}^\\infty$ sera considéré\ncomme une $\\mathcal{O}_X$-Algèbre, c'est de la structure d'Algèbre définie par\n$p_1$ qu'il s'agira}."},
    "One edit for the whole italic passage (checked on a crop).")
add(15, "Définition (16.3.6), l. 1: 'ou d^n_{X/S} (resp. d^∞_f, ou'", "'(resp.' upright inside the italic definition",
    "italic (definition environment)", "convention", 6, "high",
    {"old": "(resp. $d_f^\\infty$", "new": "\\textup{(resp.} $d_f^\\infty$"}, "")
add(15, "Définition (16.3.6), l. 2: 'ou simplement d^n (resp. d^∞),'", "'(resp.' upright",
    "italic", "convention", 6, "high",
    {"old": "(resp. $d^\\infty$)", "new": "\\textup{(resp.} $d^\\infty$)"}, "")
add(15, "Définition (16.3.6), l. 2: '(resp. O_X → P^∞_f = P^∞_{X/S})'", "'(resp.' upright",
    "italic", "convention", 6, "high",
    {"old": "(resp. $\\mathcal{O}_X\\to\\mathscr{P}_f^\\infty", "new": "\\textup{(resp.} $\\mathcal{O}_X\\to\\mathscr{P}_f^\\infty"}, "")
add(15, "Définition (16.3.6), l. 3: 'd^n t (resp. d^∞ t) est appelé'", "'(resp.' upright",
    "italic", "convention", 6, "high",
    {"old": "(resp. $d^\\infty t$)", "new": "\\textup{(resp.} $d^\\infty t$)"}, "")
add(15, "Définition (16.3.6), l. 3-4: the defined term 'la partie principale d'ordre n (resp. partie principale d'ordre infini)'",
    "the defined term, with its parenthesis, is roman inside the italic definition ('est appelé' and 'de t' italic)",
    "italic (definition environment)", "convention", 6, "high",
    {"old": "la partie\nprincipale d'ordre $n$ (resp. partie principale d'ordre infini)",
     "new": "\\textup{la partie\nprincipale d'ordre $n$ (resp. partie principale d'ordre infini)}"},
    "Checked on an enlarged crop.")
add(15, "Définition (16.3.6): 'On pose dt = d^1t—t'", "long dash for the minus sign", "$dt=d^1t-t$",
    "convention", 7, "high", {"old": "$dt=d^1t-t$", "new": "$dt=d^1t\\setmin t$"}, "Subtraction (GLOBAL_ISSUES item 23).")
add(15, "Définition (16.3.6), last line: 'élément de Γ(U, Ω^1_{X/S})'", "italic Omega", "\\Omega (upright)",
    "font", None, "high",
    {"old": "$\\Gamma(U,\\Omega_{X/S}^1)$, aussi noté", "new": "$\\Gamma(U,\\varOmega_{X/S}^1)$, aussi noté"}, OMEGA_NOTE)
add(15, "after (16.3.6.1): 'd est une dérivation de l'anneau'", "'dérivation' italic", "'dérivation' roman",
    "italics", None, "high", {"old": "est une dérivation de", "new": "est une \\emph{dérivation} de"}, "")
add(15, "after (16.3.6.1): 'dans le Γ(U, O_X)-module Γ(U, Ω^1_{X/S})'", "italic Omega", "\\Omega (upright)",
    "font", None, "high",
    {"old": "-module $\\Gamma(U,\\Omega_{X/S}^1)$.", "new": "-module $\\Gamma(U,\\varOmega_{X/S}^1)$."}, OMEGA_NOTE)
add(15, "(16.3.7): 'de noyau 𝔍 = 𝔍_{B/A}'", "Fraktur J (twice)", "\\mathfrak{I}", "symbol", None, "high",
    {"old": "$\\mathfrak{I}=\\mathfrak{I}_{B/A}$", "new": "$\\mathfrak{J}=\\mathfrak{J}_{B/A}$"}, FRAK_NOTE)
add(15, "(16.3.7): '(0, 20.4.1)'", "bold 0", "plain 0", "convention", 2, "high",
    {"old": "(0, 20.4.1)", "new": "(\\textbf{0}, 20.4.1)"}, "")
add(15, "(16.3.7), display P^n_{B/A} = (B⊗_A B)/𝔍^{n+1}", "Fraktur J", "\\mathfrak{I}", "symbol", None, "high",
    {"old": "B)/\\mathfrak{I}^{n+1};", "new": "B)/\\mathfrak{J}^{n+1};"}, FRAK_NOTE)
add(15, "(16.3.7), display gr^•_𝔍(B⊗_A B) = ⊕(𝔍^n/𝔍^{n+1})", "Fraktur J (three times)", "\\mathfrak{I}",
    "symbol", None, "high",
    {"old": "\\operatorname{gr}_{\\mathfrak{I}}^\\bullet(B\\otimes_A B)\n  =\\bigoplus_{n\\geq 0}(\\mathfrak{I}^n/\\mathfrak{I}^{n+1});",
     "new": "\\operatorname{gr}_{\\mathfrak{J}}^\\bullet(B\\otimes_A B)\n  =\\bigoplus_{n\\geq 0}(\\mathfrak{J}^n/\\mathfrak{J}^{n+1});"},
    FRAK_NOTE)
add(15, "(16.3.7): 'en particulier Ω^1_f = Ω^1_{X/S} est le O_X-Module'", "italic Omega (twice); the Ω^1_{B/A} two lines below is upright",
    "\\Omega (upright)", "font", None, "high",
    {"old": "$\\Omega_f^1=\\Omega_{X/S}^1$", "new": "$\\varOmega_f^1=\\varOmega_{X/S}^1$"}, OMEGA_NOTE)
add(15, "(16.3.7): 'Ω^1_{B/A} (0, 20.4.3)'", "bold 0", "plain 0", "convention", 2, "high",
    {"old": "(0, 20.4.3)", "new": "(\\textbf{0}, 20.4.3)"}, "")
add(15, "(16.3.7): 'défini dans (0, 20.4.6)'", "bold 0", "plain 0", "convention", 2, "high",
    {"old": "(0, 20.4.6)", "new": "(\\textbf{0}, 20.4.6)"}, "")
add(15, "(16.3.7): '(cf. Err_IV, 11)', subscript IV", "bold subscript IV (heavier than the subscripts B/A on the same line; enlarged crop)",
    "\\mathrm{IV}", "font", None, "medium",
    {"old": "$\\mathbf{Err}_{\\mathrm{IV}}$", "new": "$\\mathbf{Err}_{\\mathbf{IV}}$"},
    "ega4-20 writes the same reference as \\textbf{Err}\\textsubscript{\\textbf{IV}}.")
add(15, "(16.3.7): '(cf. Err_IV, 11)', the number 11", "bold 11", "plain 11", "font", None, "high",
    {"old": "$,\n11).", "new": "$,\n\\textbf{11})."}, "Independent of the subscript fix.")

# ---------------- page 16 ----------------
add(16, "proof of (16.3.8): 'd^n_{X/S} n'est pas surjectif (même déjà pour n = 1)'", "'n'est pas surjectif' italic",
    "roman", "italics", None, "high",
    {"old": "n'est pas\nsurjectif (même", "new": "\\emph{n'est pas\nsurjectif} (même"}, "Checked on a crop.")
add(16, "proof of (16.3.9): 'localement de présentation finie (1.4.3.1)'",
    "(1.4.3.1): old-style 1, full stops, no bold numeral (enlarged crop)", "(I, 4.3.1)", "number", None, "high",
    {"old": "finie (I, 4.3.1).", "new": "finie (1.4.3.1)."},
    "A reference to EGA IV (1.4.3.1) misread as (I, 4.3.1) (GLOBAL_ISSUES item 78 pattern).")
add(16, "title of 16.4", "'16.4. Propriétés fonctorielles des invariants différentiels.' (final full stop)", "no full stop",
    "punctuation", None, "high",
    {"old": "\\subsection{Propriétés fonctorielles des invariants différentiels}",
     "new": "\\subsection{Propriétés fonctorielles des invariants différentiels.}"}, "")
add(16, "(16.4.1): 'où v est l'homomorphisme composé (I, 5.3.5 et 5.3.15)'", "bold I", "plain I", "convention", 2, "high",
    {"old": "(I, 5.3.5 et 5.3.15)", "new": "(\\textbf{I}, 5.3.5 et 5.3.15)"}, "")
add(16, "display (16.4.1.2), end", "no full stop after X×_S X (enlarged crop)", "X\\times_S X.", "punctuation", None, "high",
    {"old": "\\xrightarrow{u\\times_S u}X\\times_S X.", "new": "\\xrightarrow{u\\times_S u}X\\times_S X"}, "")
add(16, "after (16.4.1.2): 'On déduit donc de u et v'", "new indented paragraph after the display",
    "no blank line after \\]: the text continues the paragraph without indent", "other", None, "high",
    {"old": "\\]\nOn déduit donc", "new": "\\]\n\nOn déduit donc"}, "Paragraph indent only (GLOBAL_ISSUES item 47 pattern).")
add(16, "(16.4.1), before (16.4.1.5): '(relatif à λ^♯)'", "sharp sign ♯", "$\\lambda^\\#$", "convention", 9, "high",
    {"old": "$\\lambda^\\#$", "new": "$\\lambda^\\sharp$"}, "")
add(16, "end of page_016.tex: \\begin{env}[16.4.2] and its \\label (the heading (16.4.2) opens printed p. 17)",
    "p. 16 ends with display (16.4.1.5); p. 17 begins '(16.4.2) Si l'on a un diagramme commutatif'",
    "\\begin{env}[16.4.2]\\label{IV.16.4.2} stand before \\oldpage[IV-4]{17}", "marker", None, "high",
    {"old": "\\begin{env}[16.4.2]\n\\label{IV.16.4.2}\n", "new": ""},
    "Two-part move (the env opening moves, not the marker, so each edit stays in its own page segment): the p. 17 marker finding re-inserts these two lines after \\oldpage[IV-4]{17}. Apply both or neither.")

# ---------------- page 17 ----------------
add(17, "start of page_017.tex: (16.4.2) heading", "printed p. 17 begins with '(16.4.2) Si l'on a'",
    "the env opening of (16.4.2) stands before the marker, in the p. 16 segment", "marker", None, "high",
    {"old": "\\oldpage[IV-4]{17}\nSi l'on a", "new": "\\oldpage[IV-4]{17}\n\\begin{env}[16.4.2]\n\\label{IV.16.4.2}\nSi l'on a"},
    "Part 2 of 2: apply together with the p. 16 finding that removes \\begin{env}[16.4.2]\\label{IV.16.4.2} from the end of the p. 16 segment. Net result in ega4-16-fr.tex: \\oldpage[IV-4]{17} moves before \\begin{env}[16.4.2].")
add(17, "(16.4.2), first diagram: label f' of the middle vertical arrow", "f' to the LEFT of the arrow X' → S' (enlarged crop)",
    "\\ar[d]^-{f'} (label on the right)", "formula", None, "high",
    {"old": "\\ar[d]^-{f'} &", "new": "\\ar[d]_-{f'} &"}, "f is left and f'' right, as in the TeX.")
add(17, "(16.4.2), second diagram: label Δ_{f'} of the middle vertical arrow", "Δ_{f'} to the LEFT of the arrow (enlarged crop)",
    "\\ar[d]^-{\\Delta_{f'}} (label on the right)", "formula", None, "high",
    {"old": "\\ar[d]^-{\\Delta_{f'}}", "new": "\\ar[d]_-{\\Delta_{f'}}"}, "Δ_f is left and Δ_{f''} right, as in the TeX.")
add(17, "(16.4.2), composite display: label ρ'^*(ν_n^♯) of the first arrow", "sharp sign ♯", "\\nu_n^\\#", "convention", 9, "high",
    {"old": "\\rho'^*(\\nu_n^\\#)", "new": "\\rho'^*(\\nu_n^\\sharp)"}, "")
add(17, "(16.4.2), composite display: label ρ'^*(ν_n^♯)", "ρ'^*(ν_n^♯)",
    "\\rho'^*(\\nu_n^\\#): keeps the printed reading (sign aside)", "misprint_in_print", None, "medium", None,
    "By (16.4.1.3) ν_n is already the map ρ^*(P^n_{X/S}) → P^n_{X'/S'}, so the first arrow ρ'^*(ρ^*(P^n_{X/S})) → ρ'^*(P^n_{X'/S'}) is ρ'^*(ν_n); the second arrow of the same display is written ν'_n without a sharp. ν_n^♯ is not defined. Authors' slip; not in the errata list of this volume. For the corrected edition only, if accepted.",
    corrected="\\rho'^*(\\nu_n)")
add(17, "end of (16.4.2): 'dépendent fonctoriellement de f.'", "'dépendent fonctoriellement de f' italic",
    "roman", "italics", None, "high",
    {"old": "dépendent fonctoriellement de $f$.", "new": "\\emph{dépendent fonctoriellement de $f$}."}, "")
add(17, "diagram (16.4.3.1): top arrow λ^♯", "sharp sign ♯", "\\lambda^\\#", "convention", 9, "high",
    {"old": "\\ar[r]^{\\lambda^\\#} \\ar[d] &", "new": "\\ar[r]^{\\lambda^\\sharp} \\ar[d] &"}, "")
add(17, "diagram (16.4.3.2): top arrow λ^♯", "sharp sign ♯", "\\lambda^\\#", "convention", 9, "high",
    {"old": "\\ar[r]^{\\lambda^\\#}\n      \\ar[d]_{\\rho^*", "new": "\\ar[r]^{\\lambda^\\sharp}\n      \\ar[d]_{\\rho^*"}, "")

# ---------------- page 18 ----------------
add(18, "(16.4.3): 'un homomorphisme canonique de O_{X'}-Algèbres augmentées'", "'O_{X'}-Algèbres augmentées' italic (crop)",
    "roman", "italics", None, "high",
    {"old": "$\\mathcal{O}_{X'}$-Algèbres augmentées", "new": "\\emph{$\\mathcal{O}_{X'}$-Algèbres augmentées}"}, "")
add(18, "(16.4.3): 'On en déduit un homomorphisme de O_{X'}-Algèbres graduées'", "'O_{X'}-Algèbres graduées' italic (crop)",
    "roman", "italics", None, "high",
    {"old": "$\\mathcal{O}_{X'}$-Algèbres\ngraduées", "new": "\\emph{$\\mathcal{O}_{X'}$-Algèbres\ngraduées}"}, "")
add(18, "display (16.4.3.6): Ω^1_{X/S} ⊗ O_{X'} → Ω^1_{X'/S'}", "italic Omega (twice)", "\\Omega (upright)", "font", None, "high",
    {"old": "\\Omega_{X/S}^1\\otimes_{\\mathcal{O}_X}\\mathcal{O}_{X'}\n  \\longrightarrow\\Omega_{X'/S'}^1",
     "new": "\\varOmega_{X/S}^1\\otimes_{\\mathcal{O}_X}\\mathcal{O}_{X'}\n  \\longrightarrow\\varOmega_{X'/S'}^1"}, OMEGA_NOTE)
add(18, "diagram (16.4.3.7), bottom row", "italic Omega (twice)", "\\Omega (upright)", "font", None, "high",
    {"old": "\\Omega_{X/S}^1\\otimes_{\\mathcal{O}_X}\\mathcal{O}_{X'} \\ar[r] &\n      \\Omega_{X'/S'}^1",
     "new": "\\varOmega_{X/S}^1\\otimes_{\\mathcal{O}_X}\\mathcal{O}_{X'} \\ar[r] &\n      \\varOmega_{X'/S'}^1"}, OMEGA_NOTE)
add(18, "(16.4.4): 'l'image de 𝔍_{B/A} dans B'⊗_{A'}B''", "Fraktur J", "\\mathfrak{I}", "symbol", None, "high",
    {"old": "$\\mathfrak{I}_{B/A}$", "new": "$\\mathfrak{J}_{B/A}$"}, FRAK_NOTE)
add(18, "(16.4.4): 'est contenue dans 𝔍_{B'/A'}'", "Fraktur J", "\\mathfrak{I}", "symbol", None, "high",
    {"old": "$\\mathfrak{I}_{B'/A'}$", "new": "$\\mathfrak{J}_{B'/A'}$"}, FRAK_NOTE)
add(18, "(16.4.4): '(0, 20.5.4.1)'", "bold 0", "plain 0", "convention", 2, "high",
    {"old": "(0, 20.5.4.1)", "new": "(\\textbf{0}, 20.5.4.1)"}, "")
add(18, "(16.4.4): '(0, 20.5.4.2)'", "bold 0", "plain 0", "convention", 2, "high",
    {"old": "(0, 20.5.4.2)", "new": "(\\textbf{0}, 20.5.4.2)"}, "")

# ---------------- page 19 ----------------
add(19, "Proposition (16.4.5): 'P^n(u) (16.4.3.3) et'", "(16.4.3.3) upright inside the italic statement", "italic",
    "convention", 6, "high", {"old": "$P^n(u)$ (16.4.3.3) et", "new": "$P^n(u)$ \\textup{(16.4.3.3)} et"}, "")
add(19, "Proposition (16.4.5): 'Gr_1(u) (16.4.3.6) sont bijectifs'", "(16.4.3.6) upright", "italic",
    "convention", 6, "high",
    {"old": "$\\operatorname{Gr}_1(u)$ (16.4.3.6) sont", "new": "$\\operatorname{Gr}_1(u)$ \\textup{(16.4.3.6)} sont"}, "")
add(19, "after (16.4.5): 'Gr_•(u) (16.4.3.5) est surjectif, mais non bijectif'", "'surjectif' italic", "roman",
    "italics", None, "high", {"old": "est surjectif, mais", "new": "est \\emph{surjectif}, mais"}, "")
add(19, "Corollaire (16.4.6): 'celles de (16.4.5), supposons'", "(16.4.5) upright inside the italic statement", "italic",
    "convention", 6, "high",
    {"old": "celles de (16.4.5), supposons", "new": "celles de \\textup{(16.4.5)}, supposons"}, "")
add(19, "Corollaire (16.4.6): 'soit plat (resp. que les'", "'(resp.' upright", "italic", "convention", 6, "high",
    {"old": "(resp. que les", "new": "\\textup{(resp.} que les"}, "")
add(19, "Corollaire (16.4.6), last line: '(resp. pour n≤m)'", "'(resp.' upright, 'pour' italic", "italic",
    "convention", 6, "high",
    {"old": "(resp. pour $n\\leq m$)", "new": "\\textup{(resp.} pour $n\\leq m$)"}, "")
add(19, "(16.4.7): 'X = V(ℰ) (II, 1.7.8)'", "bold II", "plain II", "convention", 2, "high",
    {"old": "(II, 1.7.8)", "new": "(\\textbf{II}, 1.7.8)"}, "")
add(19, "(16.4.7): 'égal à Spec(S_{O_S}(ℰ))'", "bold upright S (enlarged crop)", "\\mathscr{S}", "font", None, "high",
    {"old": "\\operatorname{Spec}(\\mathscr{S}_{\\mathcal{O}_S}", "new": "\\operatorname{Spec}(\\mathbf{S}_{\\mathcal{O}_S}"}, S_NOTE)
add(19, "(16.4.7): 'une section de S_{O_S}(ℰ) au-dessus de U'", "bold upright S", "\\mathscr{S}", "font", None, "high",
    {"old": "$\\mathscr{S}_{\\mathcal{O}_S}(\\mathscr{E})$ au-dessus", "new": "$\\mathbf{S}_{\\mathcal{O}_S}(\\mathscr{E})$ au-dessus"}, S_NOTE)
add(19, "(16.4.7): '= Γ(U, S_{O_S}(ℰ)), et posons'", "bold upright S", "\\mathscr{S}", "font", None, "high",
    {"old": "\\Gamma(U,\\mathscr{S}_{\\mathcal{O}_S}", "new": "\\Gamma(U,\\mathbf{S}_{\\mathcal{O}_S}"}, S_NOTE)
add(19, "display (16.4.7.1): 'd^n_{X/S}(t')—t''", "long dash for the minus sign", "d_{X/S}^n(t')-t'",
    "convention", 7, "high", {"old": "d_{X/S}^n(t')-t'", "new": "d_{X/S}^n(t')\\setmin t'"}, "Subtraction (GLOBAL_ISSUES item 23).")
add(19, "display (16.4.7.2): f^*(S_{O_S}(ℰ))", "bold upright S", "\\mathscr{S}", "font", None, "high",
    {"old": "f^*(\\mathscr{S}_{\\mathcal{O}_S}(\\mathscr{E}))", "new": "f^*(\\mathbf{S}_{\\mathcal{O}_S}(\\mathscr{E}))"}, S_NOTE)
add(19, "(16.4.7): 'l'augmentation S_{O_S}(ℰ) → O_S'", "bold upright S", "\\mathscr{S}", "font", None, "high",
    {"old": "l'augmentation $\\mathscr{S}_{\\mathcal{O}_S}", "new": "l'augmentation $\\mathbf{S}_{\\mathcal{O}_S}"}, S_NOTE)
add(19, "display (16.4.7.3): δ_n : f^*(S_{O_S}(ℰ)/𝒦^{n+1})", "bold upright S", "\\mathscr{S}", "font", None, "high",
    {"old": "\\delta_n:f^*(\\mathscr{S}_{\\mathcal{O}_S}", "new": "\\delta_n:f^*(\\mathbf{S}_{\\mathcal{O}_S}"}, S_NOTE)
add(19, "Proposition (16.4.8): 'Sous les conditions de (16.4.7), les'", "(16.4.7) upright inside the italic statement",
    "italic", "convention", 6, "high",
    {"old": "Sous les conditions de (16.4.7), les", "new": "Sous les conditions de \\textup{(16.4.7)}, les"}, "")
add(19, "display (16.4.8.1): f^*(S^•_{O_S}(ℰ))", "bold upright S with raised bullet", "\\mathscr{S}", "font", None, "high",
    {"old": "f^*(\\mathscr{S}_{\\mathcal{O}_S}^{\\bullet}", "new": "f^*(\\mathbf{S}_{\\mathcal{O}_S}^{\\bullet}"}, S_NOTE)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print(len(F), "findings written")
