import json

RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
OUT = RUN + "/findings_040_044.json"

FJ_NOTE = ("Wrong letter: the print's Fraktur capital has the descender of a Fraktur J (crops p40_s3_frakJ_a.png, "
           "p40_s3_frakJ_b.png, p44_s4_frak.png), as on pp. 11-35 (GLOBAL_ISSUES 91); ega4-16 writes \\mathfrak{I}.")
C7_NOTE = "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."
WAVY_NOTE = "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern)."


def F(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


findings = [
    # ---------------- page 40 ----------------
    F(40, "after (16.8.1): 'ne sont autres que les homomorphismes de O_X-Modules F→G'",
      "'Modules' italic (crop p40_s2_modules.png); the later 'O_X-Modules mais' is roman",
      "roman", "italics",
      fx("$\\mathcal{O}_X$-Modules\n$\\mathscr{F}\\to\\mathscr{G}$",
         "$\\mathcal{O}_X$-\\emph{Modules}\n$\\mathscr{F}\\to\\mathscr{G}$")),
    F(40, "end of (16.8.1): 'cela résulte de la structure de P^1_{B/A} (0, 20.4.8)'",
      "bold 0, no subscript (crop p40_s2_0ref.png)", "plain 0", "convention",
      fx("(0, 20.4.8)", "(\\textbf{0}, 20.4.8)"), convention=2),
    F(40, "(16.8.2): 'on a Γ(U, P^n_{X/S})=(B⊗_A B)/𝔍^{n+1}, où l'on a posé'",
      "formula in the running text, followed by ', où l'on a posé' on the same line (crop p40_s3_frak1.png); Fraktur J",
      "set as a display \\[ ... \\] with the comma inside; \\mathfrak{I}", "other",
      fx("on a\n\\[\n  \\Gamma(U,\\mathscr{P}_{X/S}^n)\n  =(B\\otimes_A B)/\\mathfrak{I}^{n+1},\n\\]\noù l'on a posé",
         "on a $\\Gamma(U,\\mathscr{P}_{X/S}^n)=(B\\otimes_A B)/\\mathfrak{J}^{n+1}$,\noù l'on a posé"),
      note="One edit: inline formula as printed (no connecting word lost or added), and the Fraktur J of the print "
           "(same letter fix as the following entries; no separate letter entry for this formula)."),
    F(40, "(16.8.2): 'où l'on a posé pour abréger 𝔍=𝔍_{B/A}'",
      "Fraktur J twice (crop p40_s3_frakJ_b.png)", "\\mathfrak{I} twice", "symbol",
      fx("$\\mathfrak{I}=\\mathfrak{I}_{B/A}$", "$\\mathfrak{J}=\\mathfrak{J}_{B/A}$"), note=FJ_NOTE),
    F(40, "(16.8.2), display 'M→((B⊗_A B)/𝔍^{n+1})⊗_B M →v N'",
      "Fraktur J", "\\mathfrak{I}", "symbol",
      fx("/\\mathfrak{I}^{n+1})\\otimes_B M\n  \\xrightarrow{v}N", "/\\mathfrak{J}^{n+1})\\otimes_B M\n  \\xrightarrow{v}N"),
      note=FJ_NOTE),
    F(40, "(16.8.2): 'la structure de B-module de ((B⊗_A B)/𝔍^{n+1})⊗_B M provenant du premier facteur'",
      "Fraktur J", "\\mathfrak{I}", "symbol",
      fx("\\mathfrak{I}^{n+1})\\otimes_B M$ provenant", "\\mathfrak{J}^{n+1})\\otimes_B M$ provenant"), note=FJ_NOTE),
    F(40, "(16.8.2): 'la structure de B-module de (B⊗_A B)/𝔍^{n+1} provient du second facteur B'",
      "Fraktur J", "\\mathfrak{I}", "symbol",
      fx("/\\mathfrak{I}^{n+1}$ provient", "/\\mathfrak{J}^{n+1}$ provient"), note=FJ_NOTE),
    F(40, "(16.8.2): 'le B-module ((B⊗_A B)/𝔍^{n+1})⊗_B M est isomorphe à'",
      "Fraktur J", "\\mathfrak{I}", "symbol",
      fx("\\mathfrak{I}^{n+1})\\otimes_B M$ est isomorphe", "\\mathfrak{J}^{n+1})\\otimes_B M$ est isomorphe"),
      note=FJ_NOTE),
    F(40, "(16.8.2): 'est isomorphe à (B⊗_A M)/𝔍^{n+1}(B⊗_A M)'",
      "Fraktur J", "\\mathfrak{I}", "symbol",
      fx("/\\mathfrak{I}^{n+1}(B\\otimes_A M)$", "/\\mathfrak{J}^{n+1}(B\\otimes_A M)$"), note=FJ_NOTE),
    F(40, "end of (16.8.2): 'doit être nul dans le B-module 𝔍^{n+1}(B⊗_A M).'",
      "Fraktur J", "\\mathfrak{I}", "symbol",
      fx("$\\mathfrak{I}^{n+1}(B\\otimes_A M)$.", "$\\mathfrak{J}^{n+1}(B\\otimes_A M)$."), note=FJ_NOTE),
    F(40, "(16.8.2): 'l'homomorphisme canonique t ⇝ 1⊗t'",
      "wavy arrow: the arrowhead with its short straight piece matches the wavy arrows of 'b ⇝ b⊗1' (same page) and "
      "'U ⇝ Diff' (p. 41), not the thin plain arrow of 'M→N'; the wavy shaft is faintly inked, only a fragment shows; "
      "no bar of a mapsto (crops p40_s3_mapsto_z.png, p40_s3_leadsto_z.png, p40_s3_MtoN.png)",
      "\\mapsto", "symbol",
      fx("t\\mapsto1\\otimes t", "t\\leadsto1\\otimes t"), confidence="medium", note=WAVY_NOTE),
    F(40, "(16.8.2): 'l'homomorphisme b ⇝ b⊗1 de B dans B⊗_A B'",
      "wavy arrow (crop p40_s3_leadsto_z.png)", "\\mapsto", "symbol",
      fx("b\\mapsto b\\otimes1", "b\\leadsto b\\otimes1"), note=WAVY_NOTE),

    # ---------------- page 41 ----------------
    F(41, "l. 1: 'donc U ⇝ Diff^n_{U/S}(F|U, G|U) est un préfaisceau'",
      "wavy arrow (crop p41_s1_leadsto1.png)", "\\mapsto", "symbol",
      fx("donc $U\\mapsto", "donc $U\\leadsto"), note=WAVY_NOTE),
    F(41, "(16.8.3): 'les homomorphismes u ⇝ u∘d^n_{U/S,F|U}'",
      "wavy arrow (crop p41_s1_leadsto2.png)", "\\mapsto", "symbol",
      fx("$u\\mapsto u\\circ", "$u\\leadsto u\\circ"), note=WAVY_NOTE),
    F(41, "display (16.8.3.1): 'Hom_{O_U}(P^n_{U/S}(F|U), G|U) ⥲ Diff^n_{U/S}(F|U, G|U)'",
      "roman 'Hom' (the group of O_U-homomorphisms over U; crop p41_s1_Hom.png); the sheaf Hom of (16.8.4.1) is script",
      "\\mathscr{H}\\!om (script sheaf Hom)", "symbol",
      fx("\\mathscr{H}\\!om_{\\mathcal{O}_U}", "\\operatorname{Hom}_{\\mathcal{O}_U}")),
    F(41, "Proposition (16.8.4): 'Les isomorphismes (16.8.3.1) définissent'",
      "reference upright (crop p41_s1_prop.png)", "italic (inside the italic statement)", "convention",
      fx("Les isomorphismes (16.8.3.1) définissent", "Les isomorphismes \\textup{(16.8.3.1)} définissent"),
      convention=6),
    F(41, "Proposition (16.8.6), end: 'pour l'une ou l'autre structure définies dans (16.8.5).'",
      "reference upright (crop p41_s3_prop.png)", "italic (inside the italic statement)", "convention",
      fx("dans (16.8.5).", "dans \\textup{(16.8.5)}."), convention=6),
    F(41, "after Proposition (16.8.6): 'et de (I, 1.3.12)'",
      "bold I (crop p41_s3_Iref.png)", "plain I", "convention",
      fx("(I, 1.3.12)", "(\\textbf{I}, 1.3.12)"), convention=2,
      note="A genuine EGA I reference (bold I printed), not a misread (1.3.12)."),
    F(41, "(16.8.7): 'on voit encore comme dans (16.8.3) que U ⇝ Diff_{U/S}(F|U, G|U) est un faisceau'",
      "wavy arrow (crop p41_s4_leadsto.png)", "\\mapsto", "symbol",
      fx("$U\\mapsto\\operatorname{Diff}_{U/S}(", "$U\\leadsto\\operatorname{Diff}_{U/S}("), note=WAVY_NOTE),

    # ---------------- page 42 ----------------
    F(42, "(16.8.7), after (16.8.7.1): 'où les flèches horizontales sont les isomorphismes (16.8.4.2)'",
      "(16.8.4.2) (crop p42_s2_1684.png)", "(16.8.4.2): keeps the printed reading", "misprint_in_print",
      None, corrected="(16.8.4.1)",
      note="There is no (16.8.4.2): Proposition (16.8.4) has the single formula (16.8.4.1), and the horizontal arrows of "
           "(16.8.7.1) are its isomorphisms for n and m. No erratum found in Liste 3."),
    F(42, "(16.8.7): 'munissons alors Γ(U, P^∞_{X/S}(F))=lim← Γ(U, P^n_{X/S}(F)) de la topologie'",
      "formula in the running text ('munissons alors ... de la')", "displayed with \\[ ... \\]", "other",
      fx("munissons alors\n\\[\n  \\Gamma(U,\\mathscr{P}_{X/S}^{\\infty}(\\mathscr{F}))\n  =\\varprojlim\\Gamma(U,\\mathscr{P}_{X/S}^n(\\mathscr{F}))\n\\]\nde la topologie",
         "munissons alors\n$\\Gamma(U,\\mathscr{P}_{X/S}^{\\infty}(\\mathscr{F}))=\\varprojlim\\Gamma(U,\\mathscr{P}_{X/S}^n(\\mathscr{F}))$\nde la topologie"),
      note="Display vs inline only; no connecting word lost or added."),
    F(42, "(16.8.7): 'groupes commutatifs topologiques (0_I, 3.2.6)'",
      "bold 0 with subscript I (crop p42_s2_refs.png)", "0\\textsubscript{I}: plain 0", "convention",
      fx("(0\\textsubscript{I}, 3.2.6)", "($\\mathbf{0}_{\\mathrm I}$, 3.2.6)"), convention=2,
      note="Written as the edition's other (0_I, ...) references."),
    F(42, "(16.8.7): 'la limite du système inductif de faisceaux de groupes commutatifs (Hom_{O_X}(P^n_{X/S}(F), G)) n'est autre que'",
      "formula in the running text ('commu-tatifs (...) n'est autre que')", "displayed with \\[ ... \\]", "other",
      fx("commutatifs\n\\[\n  (\\mathscr{H}\\!om_{\\mathcal{O}_X}\n  (\\mathscr{P}_{X/S}^n(\\mathscr{F}),\\mathscr{G}))\n\\]\nn'est autre",
         "commutatifs\n$(\\mathscr{H}\\!om_{\\mathcal{O}_X}(\\mathscr{P}_{X/S}^n(\\mathscr{F}),\\mathscr{G}))$\nn'est autre"),
      note="Display vs inline only; no connecting word lost or added."),
    F(42, "(16.8.7), last display: 'Hom.cont_{O_X}(P^∞_{X/S}(F), G) ⥲ Diff_{X/S}(F, G)'",
      "'cont' italic like 'om' (crop p42_s3_homcont.png)", "\\mathrm{cont} (upright)", "font",
      fx("\\mathscr{H}\\!om.\\mathrm{cont}_{\\mathcal{O}_X}", "\\mathscr{H}\\!om.\\mathit{cont}_{\\mathcal{O}_X}")),
    F(42, "Proposition (16.8.8), label a)",
      "'a)' upright, no opening parenthesis (crop p42_s3_labels.png)",
      "\\item[(a)]: '(a)' with an opening parenthesis, italic inside the statement", "punctuation",
      fx("\\item[(a)]", "\\item[\\textup{a)}]"),
      note="The edit also sets the label upright (GLOBAL_ISSUES 88: upright labels inside italic statements)."),
    F(42, "Proposition (16.8.8), label b)",
      "'b)' upright, no opening parenthesis", "\\item[(b)]: '(b)', italic", "punctuation",
      fx("\\item[(b)]", "\\item[\\textup{b)}]"), note="As for a)."),
    F(42, "Proposition (16.8.8), label c)",
      "'c)' upright, no opening parenthesis", "\\item[(c)]: '(c)', italic", "punctuation",
      fx("\\item[(c)]", "\\item[\\textup{c)}]"), note="As for a)."),
    F(42, "display (16.8.8.1): 'D_a(t)=D(at)—aD(t)'",
      "long dash for the minus (crop p42_s3_disp1.png)", "-", "convention",
      fx("D(at)-aD(t)", "D(at)\\setmin aD(t)"), convention=7, note=C7_NOTE),
    F(42, "Proposition (16.8.8) b), last line: 'est un opérateur différentiel d'ordre ≤n—1.'",
      "long dash for the minus (crop p42_s4_n1.png)", "-", "convention",
      fx("$\\leq n-1$", "$\\leq n\\setmin 1$"), convention=7, note=C7_NOTE),
    F(42, "Proposition (16.8.8) b), last line: 'est un opérateur différentiel d'ordre ≤n—1.'",
      "'est' is BOLD italic (wrong fount): skeleton stroke width 4.5 px against 3.3 px for the 'est' of a) and 3.4-3.8 px for "
      "'un opérateur différentiel d'ordre' on the same line (crops p42_s4_est_z.png, side_rentiel_est.png)",
      "normal italic (silent correction)", "misprint_in_print",
      fx("\\]\n  est un", "\\]\n  \\textbf{est} un"), corrected="est un",
      note="Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29; cf. IV-4 pp. 7, 36, 38). Independent of the "
           "convention-7 edit on the same line."),
    F(42, "display (16.8.8.2): '(—1)^{Card(H)}'",
      "long dash for the unary minus (crop p42_s4_disp2.png)", "-", "convention",
      fx("(-1)^{\\operatorname{Card}(H)}", "(\\setmin 1)^{\\operatorname{Card}(H)}"), convention=7, note=C7_NOTE),

    # ---------------- page 43 ----------------
    F(43, "proof of (16.8.8), l. 1: 'Prouvons d'abord l'équivalence de a) et c).'",
      "labels a) and c) italic, parenthesis included (crop p43_s1_l1.png)", "plain 'a)', 'c)' (upright)", "italics",
      fx("d'abord l'équivalence de a) et c)", "d'abord l'équivalence de \\emph{a)} et \\emph{c)}"),
      note="Labels in roman text are italic in the print (GLOBAL_ISSUES 88)."),
    F(43, "proof of (16.8.8): 'la propriété c) est valable'",
      "label c) italic (crop p43_s1_l4.png)", "upright", "italics",
      fx("la propriété c)", "la propriété \\emph{c)}")),
    F(43, "proof of (16.8.8): 'la condition a) signifie alors'",
      "label a) italic (crop p43_s1_l6.png)", "upright", "italics",
      fx("la condition a)", "la condition \\emph{a)}")),
    F(43, "proof of (16.8.8): 'D' s'annule dans 𝔍^{n+1}(B⊗_A M)'",
      "Fraktur J (crop p43_s1_l8.png)", "\\mathfrak{I}", "symbol",
      fx("$\\mathfrak{I}^{n+1}(B\\otimes_A M)$, ce qui", "$\\mathfrak{J}^{n+1}(B\\otimes_A M)$, ce qui"), note=FJ_NOTE),
    F(43, "proof of (16.8.8): 'en vertu de (0, 20.4.4)'",
      "bold 0, no subscript (crop p43_s1_l8.png)", "plain 0", "convention",
      fx("(0, 20.4.4)", "(\\textbf{0}, 20.4.4)"), convention=2),
    F(43, "proof of (16.8.8), display '(Π_{i=1}^{n+1}(a_i⊗1—1⊗a_i)).(1⊗t)'",
      "long dash for the minus (crop p43_s2_disp1.png)", "-", "convention",
      fx("(a_i\\otimes1-1\\otimes a_i)", "(a_i\\otimes1\\setmin 1\\otimes a_i)"), convention=7, note=C7_NOTE),
    F(43, "proof of (16.8.8): 'Or, cet élément s'écrit Σ_{H⊂I_{n+1}}(Π_{i∈H}a_i)⊗((Π_{i∉H}a_i)t), et la valeur de D''",
      "the sum is in the running text, followed by ', et la valeur de D'' on the same line (crop p43_s2_inlinesum.png)",
      "displayed with \\[ ... \\]", "other",
      fx("s'écrit\n\\[\n  \\sum_{H\\subset I_{n+1}}\n  \\left(\\prod_{i\\in H}a_i\\right)\\otimes\n  \\left(\\left(\\prod_{i\\notin H}a_i\\right)t\\right),\n\\]\net la valeur",
         "s'écrit\n$\\sum_{H\\subset I_{n+1}}(\\prod_{i\\in H}a_i)\\otimes((\\prod_{i\\notin H}a_i)t)$,\net la valeur"),
      note="Display vs inline only; no connecting word lost or added. The missing sign is a separate misprint entry (next)."),
    F(43, "proof of (16.8.8): 'cet élément s'écrit Σ_{H⊂I_{n+1}}(Π_{i∈H}a_i)⊗((Π_{i∉H}a_i)t)'",
      "no sign factor in the sum", "no sign factor: keeps the printed reading", "misprint_in_print", None,
      corrected="$\\sum_{H\\subset I_{n+1}}(-1)^{n+1-\\operatorname{Card}(H)}(\\prod_{i\\in H}a_i)\\otimes((\\prod_{i\\notin H}a_i)t)$",
      confidence="medium",
      note="Mathematical slip of the print, not a typographical one: expanding Π_{i=1}^{n+1}(a_i⊗1−1⊗a_i) gives the sign "
           "(−1)^{n+1−Card(H)} (n=0: a_1⊗t−1⊗a_1t, the print gives a_1⊗t+1⊗a_1t). With the sign, the value of D' is "
           "(−1)^{n+1} times the first member of (16.8.8.2), so 'n'est autre que' holds up to sign (as 'au signe près' "
           "in the next paragraph); the equivalence a)⇔c) is unaffected. No erratum found. Corrected-edition decision."),
    F(43, "proof of (16.8.8): 'ce qui prouve l'équivalence de a) et c).'",
      "labels a) and c) italic (crop p43_s2_bc.png)", "upright", "italics",
      fx("prouve l'équivalence de a) et c)", "prouve l'équivalence de \\emph{a)} et \\emph{c)}")),
    F(43, "proof of (16.8.8): 'Prouvons maintenant l'équivalence de b) et c).'",
      "labels b) and c) italic (crop p43_s2_b2.png)", "upright", "italics",
      fx("l'équivalence de b) et c)", "l'équivalence de \\emph{b)} et \\emph{c)}")),
    F(43, "proof of (16.8.8): 'au lieu de a dans la condition b), on voit'",
      "label b) italic (crop p43_s2_b2.png)", "upright", "italics",
      fx("dans la condition b),", "dans la condition \\emph{b)},")),
    F(43, "proof of (16.8.8): 'que la condition b) signifie que pour toute famille'",
      "label b) italic (crop p43_s2_b2.png)", "upright", "italics",
      fx("condition b) signifie", "condition \\emph{b)} signifie")),
    F(43, "proof of (16.8.8), display 'Σ_{H'⊂I_n}(—1)^{Card(H')}...'",
      "long dash for the unary minus (crop p43_s2_disp2.png)", "-", "convention",
      fx("(-1)^{\\operatorname{Card}(H')}", "(\\setmin 1)^{\\operatorname{Card}(H')}"), convention=7, note=C7_NOTE),
    F(43, "proof of (16.8.8), end of the display '...D_{a_{n+1}}((Π_{i∉H'}a_i)t)=0'",
      "no full stop after '=0' (crop p43_s2_eq0_wide.png)", "'=0.'", "punctuation",
      fx("t\\right)=0.", "t\\right)=0")),
    F(43, "Proposition (16.8.9), last line: 'diffé-rentiel d'ordre ≤n+n''",
      "'rentiel' (after the line break 'diffé-') is BOLD italic (wrong fount); 'diffé-' and 'd'ordre' are of normal weight "
      "(crops p43_s3_rentiel.png, p43_rentiel_z.png, side_rentiel_est.png; ink per column 10.7 against 8.5 for the 'rentiel' "
      "of 'différentiel' in (16.8.8) a))",
      "normal italic (silent correction)", "misprint_in_print",
      fx("différentiel d'ordre $\\leq n+n'$", "diffé\\textbf{rentiel} d'ordre $\\leq n+n'$"),
      corrected="différentiel d'ordre $\\leq n+n'$",
      note="Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29), like 'est' on p. 42: both are the first word of the "
           "last line of a statement."),

    # ---------------- page 44 ----------------
    F(44, "proof of (16.8.9): 'w le O_X-homomorphisme composé [display]. Reste à prouver le lemme (16.8.9.1).'",
      "'Reste' continues the paragraph after the display, flush left (crop p44_s3_reste.png)",
      "blank line after \\]: a new indented paragraph", "other",
      fx("\\]\n\nReste à prouver", "\\]\nReste à prouver"),
      note="Paragraph break the print does not have (reverse of the GLOBAL_ISSUES 47 pattern)."),
    F(44, "proof of (16.8.9.1): 'posant 𝔍=𝔍_{B/A}'",
      "Fraktur J twice (crop p44_s4_frak.png)", "\\mathfrak{I} twice", "symbol",
      fx("$\\mathfrak{I}=\\mathfrak{I}_{B/A}$", "$\\mathfrak{J}=\\mathfrak{J}_{B/A}$"), note=FJ_NOTE),
    F(44, "proof of (16.8.9.1), display 'φ : (B⊗_A B)/𝔍^{n+n'+1} → ((B⊗_A B)/𝔍^{n'+1})⊗_B((B⊗_A B)/𝔍^{n+1})'",
      "Fraktur J three times (crop p44_s4_phi.png)", "\\mathfrak{I} three times", "symbol",
      fx("/\\mathfrak{I}^{n+n'+1}\n  \\longrightarrow\n  ((B\\otimes_A B)/\\mathfrak{I}^{n'+1})\n  \\otimes_B((B\\otimes_A B)/\\mathfrak{I}^{n+1})",
         "/\\mathfrak{J}^{n+n'+1}\n  \\longrightarrow\n  ((B\\otimes_A B)/\\mathfrak{J}^{n'+1})\n  \\otimes_B((B\\otimes_A B)/\\mathfrak{J}^{n+1})"),
      note=FJ_NOTE),
    F(44, "last line: 'du second membre, (B⊗_A B)/𝔍^{n'+1} doit être considéré'",
      "Fraktur J (crop p44_s4_last.png)", "\\mathfrak{I}", "symbol",
      fx("/\\mathfrak{I}^{n'+1}$ doit", "/\\mathfrak{J}^{n'+1}$ doit"), note=FJ_NOTE),
]

# verify every old occurs exactly once in its page file
ok = True
texts = {}
for f in findings:
    p = f["page"]
    if p not in texts:
        with open(f"{RUN}/page_{p:03d}.tex", encoding="utf-8") as fh:
            texts[p] = fh.read()
    if f["fix"] is not None:
        n = texts[p].count(f["fix"]["old"])
        if n != 1:
            ok = False
            print("COUNT", n, "page", p, repr(f["fix"]["old"]))
print("all unique:", ok)

# counts per page
from collections import Counter
cnt = {}
for f in findings:
    c = cnt.setdefault(f["page"], Counter())
    if f["kind"] == "misprint_in_print":
        c["misprint"] += 1
    elif f["kind"] == "convention":
        c["convention"] += 1
    else:
        c["normal"] += 1
for p in sorted(cnt):
    print(p, dict(cnt[p]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
print("written", OUT, len(findings))
