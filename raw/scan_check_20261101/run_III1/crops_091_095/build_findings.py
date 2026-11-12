import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_091_095.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def c2(page, where, old, new, scan):
    add(page, where, scan, old, "convention", 2, "high", {"old": old, "new": new})


# ---------------- page 91 ----------------
c2(91, "proof of Lemme (1.4.9): 'des morphismes affines (I, 5.5.6)'",
   "(I, 5.5.6)", "(\\textbf{I}, 5.5.6)", "(I, 5.5.6) with bold I")
c2(91, "proof of Lemme (1.4.9): 'sont quasi-cohérents (II, 1.2.6)'",
   "(II, 1.2.6)", "(\\textbf{II}, 1.2.6)", "(II, 1.2.6) with bold II")
c2(91, "proof of (1.4.10): 'il résulte de (I, 5.5.10)'",
   "(I, 5.5.10)", "(\\textbf{I}, 5.5.10)", "(I, 5.5.10) with bold I")
c2(91, "proof of (1.4.10): 'En vertu de (1.4.9) et (I, 9.2.2)'",
   "(I, 9.2.2)", "(\\textbf{I}, 9.2.2)", "(I, 9.2.2) with bold I")
c2(91, "proof of (1.4.10): 'formée de O_Y-Modules quasi-cohérents (I, 4.1.1)'",
   "(I, 4.1.1)", "(\\textbf{I}, 4.1.1)", "(I, 4.1.1) with bold I")
add(91, "Lemme (1.4.9): 'défini par le recouvrement U (G, II, 5.2) est alors un'",
    "the reference (G, II, 5.2) is upright inside the italic statement (crop)",
    "(G, II, 5.2) inside the italic lemma environment: italic",
    "convention", 6, "high",
    {"old": "(G, II, 5.2) est alors", "new": "\\textup{(G, II, 5.2)} est alors"},
    "Form of the fix as on earlier pages (\\textup around the reference).")
add(91, "proof of (1.4.10), after display (1.4.10.2): 'Notons enfin qu'il résulte de la définition'",
    "'Notons enfin' begins a new, indented paragraph (the lines after the other displays are flush left)",
    "no blank line after \\end{equation}: the text continues the paragraph",
    "other", None, "high",
    {"old": "\\end{equation}\nNotons enfin", "new": "\\end{equation}\n\nNotons enfin"},
    "Missing paragraph break.")

# ---------------- page 92 ----------------
add(92, "top of the page: 'est quasi-cohérent. Il résulte en outre de (1.4.10.3), (1.4.10.2) et (1.4.10.1) que :'",
    "one paragraph: 'Il résulte en outre' follows 'est quasi-cohérent.' on the same line",
    "\\end{proof} and a blank line after 'est quasi-cohérent.': 'Il résulte en outre' starts a new paragraph",
    "other", None, "high",
    {"old": "est quasi-cohérent.\n\\end{proof}\n\nIl résulte en outre de (\\hyperref[III.1.4.10.3-fr]{1.4.10.3}),\n(\\hyperref[III.1.4.10.2-fr]{1.4.10.2}) et\n(\\hyperref[III.1.4.10.1-fr]{1.4.10.1}) que~:\n",
     "new": "est quasi-cohérent.\nIl résulte en outre de (\\hyperref[III.1.4.10.3-fr]{1.4.10.3}),\n(\\hyperref[III.1.4.10.2-fr]{1.4.10.2}) et\n(\\hyperref[III.1.4.10.1-fr]{1.4.10.1}) que~:\n\\end{proof}\n"},
    "Moves \\end{proof} after 'que~:' (the proof environment ends with \\par and adds no end mark), so the sentence stays in the proof's last paragraph as printed.")
add(92, "Corollaire (1.4.11): 'Sous les hypothèses de (1.4.10), pour tout ouvert affine'",
    "the reference (1.4.10) is upright inside the italic statement (crop)",
    "(\\hyperref[III.1.4.10-fr]{1.4.10}) inside the italic corollary: italic",
    "convention", 6, "high",
    {"old": "Sous les hypothèses de (\\hyperref[III.1.4.10-fr]{1.4.10})",
     "new": "Sous les hypothèses de \\textup{(\\hyperref[III.1.4.10-fr]{1.4.10})}"})
add(92, "Corollaire (1.4.12): 'les hypothèses de (1.4.10) et supposons en outre'",
    "the reference (1.4.10) is upright inside the italic statement",
    "(\\hyperref[III.1.4.10-fr]{1.4.10}) inside the italic corollary: italic",
    "convention", 6, "high",
    {"old": "(\\hyperref[III.1.4.10-fr]{1.4.10}) et supposons en outre",
     "new": "\\textup{(\\hyperref[III.1.4.10-fr]{1.4.10})} et supposons en outre"})
add(92, "Corollaire (1.4.13): 'les hypothèses de (1.4.10) et en outre supposons'",
    "the reference (1.4.10) is upright inside the italic statement",
    "(\\hyperref[III.1.4.10-fr]{1.4.10}) inside the italic corollary: italic",
    "convention", 6, "high",
    {"old": "(\\hyperref[III.1.4.10-fr]{1.4.10}) et en outre supposons",
     "new": "\\textup{(\\hyperref[III.1.4.10-fr]{1.4.10})} et en outre supposons"})
c2(92, "proof of (1.4.13): 'un O_Y-Module quasi-cohérent (I, 1.3.7)'",
   "(I, 1.3.7)", "(\\textbf{I}, 1.3.7)", "(I, 1.3.7) with bold I")
add(92, "Proposition (1.4.14): 'R^p(g∘f)_*(F) → g_*(R^pf_*(F)) (0, 12.2.5.2) est bijectif'",
    "(0, 12.2.5.2) with bold 0", "(0, 12.2.5.2)",
    "convention", 2, "high",
    {"old": "(0, 12.2.5.2)", "new": "\\textup{(\\textbf{0}, 12.2.5.2)}"},
    "One edit for this finding and the next (convention 6): bold 0 and the upright reference together.")
add(92, "Proposition (1.4.14): same reference '(0, 12.2.5.2)'",
    "the reference is upright inside the italic statement",
    "(0, 12.2.5.2) inside the italic proposition: italic",
    "convention", 6, "high", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
c2(92, "proof of (1.4.14): '(0, 12.2.5) est donc bijectif'",
   "(0, 12.2.5) est", "(\\textbf{0}, 12.2.5) est", "(0, 12.2.5) with bold 0")
add(92, "Proposition (1.4.15): 'un morphisme plat de préschémas (0_I, 6.7.1); soit'",
    "(0_I, 6.7.1) with bold 0", "(0\\textsubscript{I}, 6.7.1)",
    "convention", 2, "high",
    {"old": "(0\\textsubscript{I}, 6.7.1)", "new": "\\textup{(\\textbf{0}\\textsubscript{I}, 6.7.1)}"},
    "One edit for this finding and the next (convention 6).")
add(92, "Proposition (1.4.15): same reference '(0_I, 6.7.1)'",
    "the reference is upright inside the italic statement (crop)",
    "(0\\textsubscript{I}, 6.7.1) inside the italic proposition: italic",
    "convention", 6, "high", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(92, "diagram (1.4.15.1), bottom arrow Y ← Y'",
    "label v below the leftward arrow (crop); the top arrow has v' above",
    "Y'\\ar[l]_v: for a leftward arrow _ puts the label above",
    "formula", None, "high",
    {"old": "Y'\\ar[l]_v", "new": "Y'\\ar[l]^v"},
    "The top arrow's \\ar[l]_{v'} (label above) matches the print.")
add(92, "diagram (1.4.15.1): full stop after the diagram",
    "a full stop at the right of the diagram, level with its middle row (crop); 'Alors' then starts a new sentence",
    "no full stop after the xymatrix",
    "punctuation", None, "high",
    {"old": "}\n\\end{equation}\nAlors, pour tout", "new": "}\\quad.\n\\end{equation}\nAlors, pour tout"},
    "Spacing before the full stop is a suggestion.")

# ---------------- page 93 ----------------
c2(93, "proof of (1.4.15): 'ρ : F → v'_*(v'^*(F)) (0_I, 4.4.3.2)'",
   "(0\\textsubscript{I}, 4.4.3.2)", "(\\textbf{0}\\textsubscript{I}, 4.4.3.2)", "(0_I, 4.4.3.2) with bold 0")
add(93, "proof of (1.4.15), after display (1.4.15.2): 'D'autre part, on a, en posant w=u∘v''",
    "'D'autre part' begins a new, indented paragraph",
    "no blank line after \\end{equation}: the text continues the paragraph",
    "other", None, "high",
    {"old": "\\end{equation}\nD'autre part", "new": "\\end{equation}\n\nD'autre part"},
    "Missing paragraph break.")
c2(93, "proof of (1.4.15): 'les homomorphismes canoniques (0, 12.2.5.1 et 12.2.5.2)'",
   "(0, 12.2.5.1 et 12.2.5.2)", "(\\textbf{0}, 12.2.5.1 et 12.2.5.2)", "(0, 12.2.5.1 et 12.2.5.2) with bold 0")
add(93, "proof of (1.4.15), after display (1.4.15.3): 'Composant (1.4.15.3) et (1.4.15.2)'",
    "'Composant' begins a new, indented paragraph",
    "no blank line after \\end{equation}: the text continues the paragraph",
    "other", None, "high",
    {"old": "\\end{equation}\nComposant", "new": "\\end{equation}\n\nComposant"},
    "Missing paragraph break.")
add(93, "proof of (1.4.15): '(dont la définition ne fait intervenir aucune hypothèse sur v)'",
    "only 'aucune hypothèse' is italic; 'sur' is upright (crop)",
    "\\emph{aucune hypothèse sur $v$}",
    "italics", None, "high",
    {"old": "\\emph{aucune hypothèse sur $v$}", "new": "\\emph{aucune hypothèse} sur $v$"})
add(93, "Lemme (1.4.15.5): 'soit f-plat (0_I, 6.7.1), il faut et il suffit'",
    "(0_I, 6.7.1) with bold 0", "(0\\textsubscript{I}, 6.7.1)",
    "convention", 2, "high",
    {"old": "(0\\textsubscript{I}, 6.7.1), il faut",
     "new": "\\textup{(\\textbf{0}\\textsubscript{I}, 6.7.1)}, il faut"},
    "One edit for this finding and the next (convention 6).")
add(93, "Lemme (1.4.15.5): same reference '(0_I, 6.7.1)'",
    "the reference is upright inside the italic statement",
    "(0\\textsubscript{I}, 6.7.1) inside the italic lemma: italic",
    "convention", 6, "high", None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
c2(93, "after Lemme (1.4.15.5): 'cela résulte de la définition (0_I, 6.7.1)'",
   "définition (0\\textsubscript{I}, 6.7.1)", "définition (\\textbf{0}\\textsubscript{I}, 6.7.1)",
   "(0_I, 6.7.1) with bold 0")
c2(93, "after Lemme (1.4.15.5): 'et de (0_I, 6.3.3)'",
   "(0\\textsubscript{I}, 6.3.3)", "(\\textbf{0}\\textsubscript{I}, 6.3.3)", "(0_I, 6.3.3) with bold 0")
c2(93, "after Lemme (1.4.15.5): 'compte tenu de (I, 1.3.4)'",
   "(I, 1.3.4)", "(\\textbf{I}, 1.3.4)", "(I, 1.3.4) with bold I")
c2(93, "proof of (1.4.15): 'des homomorphismes (1.4.15.3) (cf. 0, 12.2.5)'",
   "(cf. 0, 12.2.5)", "(cf. \\textbf{0}, 12.2.5)", "(cf. 0, 12.2.5) with bold 0")
c2(93, "proof of (1.4.15): 'θ_q est le φ-morphisme (0, 12.1.3.1)'",
   "(0, 12.1.3.1)", "(\\textbf{0}, 12.1.3.1)", "(0, 12.1.3.1) with bold 0")
add(93, "commutative diagram at the foot of the page, bottom arrow labelled v'^*(ρ_q)",
    "label v'^*(ρ_q) below the arrow (the top label ρ_q is above)",
    "\\ar[rr]^{v'^*(\\rho_q)}: label above",
    "formula", None, "high",
    {"old": "\\ar[rr]^{v'^*(\\rho_q)}", "new": "\\ar[rr]_{v'^*(\\rho_q)}"})

# ---------------- page 94 ----------------
c2(94, "top of the page: 'et comme par définition (0_I, 4.4.3)'",
   "(0\\textsubscript{I}, 4.4.3)", "(\\textbf{0}\\textsubscript{I}, 4.4.3)", "(0_I, 4.4.3) with bold 0")
add(94, "'ψ^♯ est par suite le B-homomorphisme associé H^q(X, F)⊗_A B → H^q(X', F'). Comme u est de type fini'",
    "the formula is set in the running text (same line as 'associé' and 'Comme u est de type fini')",
    "displayed with \\[ ... \\]",
    "other", None, "high",
    {"old": "associé\n\\[\nH^q(X,\\mathcal F)\\otimes_A B\\longrightarrow H^q(X',\\mathcal F').\n\\]\nComme $u$",
     "new": "associé\n$H^q(X,\\mathcal F)\\otimes_A B\\to H^q(X',\\mathcal F')$.\nComme $u$"})
c2(94, "proof of (1.4.15): 'il en est de même de v' (II, 1.6.2, (iii))'",
   "(II, 1.6.2,", "(\\textbf{II}, 1.6.2,", "(II, 1.6.2, (iii)) with bold II")
c2(94, "proof of (1.4.15): 'On sait alors (0, 12.1.4.2) que le diagramme'",
   "(0, 12.1.4.2)", "(\\textbf{0}, 12.1.4.2)", "(0, 12.1.4.2) with bold 0")
add(94, "diagram H^q(U,F) → H^q(U',F') over H^q(X,F) → H^q(X',F'): bottom arrow",
    "label θ_q below the bottom arrow (the top θ_q is above)",
    "H^q(X,\\mathcal F)\\ar[r]^{\\theta_q}: label above",
    "formula", None, "high",
    {"old": "H^q(X,\\mathcal F)\\ar[r]^{\\theta_q}", "new": "H^q(X,\\mathcal F)\\ar[r]_{\\theta_q}"})
add(94, "'est tel que le B-homomorphisme associé :' before the display H^q(U,F)⊗_A B → H^q(U',F')",
    "associé : (colon, crop)", "associé (no colon)",
    "punctuation", None, "high",
    {"old": "est tel que le $B$-homomorphisme associé", "new": "est tel que le $B$-homomorphisme associé~:"})
add(94, "'posons U_s = ∩_{k=0}^p U_{i_k}, U'_s = ... , M_s = Γ(U_s, F), M'_s = Γ(U'_s, F').'",
    "'posons' and the four formulas share one justified text line (∩ with its limits set above and below); 'L'application canonique' continues the paragraph",
    "'posons' followed by a centred display \\[ ... \\]",
    "other", None, "medium",
    {"old": "posons\n\\[\nU_{\\mathbf s}=\\bigcap_{k=0}^pU_{i_k},\\qquad\nU_{\\mathbf s}'=\\bigcap_{k=0}^pU_{i_k}'=v'^{-1}(U_{\\mathbf s}),\\qquad\nM_{\\mathbf s}=\\Gamma(U_{\\mathbf s},\\mathcal F),\\qquad\nM_{\\mathbf s}'=\\Gamma(U_{\\mathbf s}',\\mathcal F').\n\\]\nL'application",
     "new": "posons\n$U_{\\mathbf s}=\\bigcap\\limits_{k=0}^pU_{i_k}$,\\quad\n$U_{\\mathbf s}'=\\bigcap\\limits_{k=0}^pU_{i_k}'=v'^{-1}(U_{\\mathbf s})$,\\quad\n$M_{\\mathbf s}=\\Gamma(U_{\\mathbf s},\\mathcal F)$,\\quad\n$M_{\\mathbf s}'=\\Gamma(U_{\\mathbf s}',\\mathcal F')$.\nL'application"},
    "The formulas stand in the text line beginning with 'posons' (paragraph margin), not in a centred display. Apply before the bold-p finding below, whose 'old' is kept unchanged by this edit.")
add(94, "same line: upper limit p of the second ∩ in U'_s = ∩_{k=0}^p U'_{i_k}",
    "the second p looks bold italic (heavier strokes than the first limit p and than the p of C^p on this page; about 35% more ink at the same size, enlarged crops)",
    "plain p in both limits",
    "misprint_in_print", None, "low",
    {"old": "^pU_{i_k}'=v'^{-1}", "new": "^{\\boldsymbol{p}}U_{i_k}'=v'^{-1}"},
    "Possibly a wrong-fount sort (the bold s of U_s is set next to it); possibly only heavier inking. The TeX has a plain p (silent correction if the bold is real). Apply after the inline 'posons' edit if both are accepted.",
    corrected="p")
c2(94, "proof of (1.4.15): 'est un isomorphisme (I, 1.6.5)'",
   "(I, 1.6.5)", "(\\textbf{I}, 1.6.5)", "(I, 1.6.5) with bold I")
c2(94, "end of the proof of (1.4.15): 'est un isomorphisme (0_I, 6.1.1)'",
   "(0\\textsubscript{I}, 6.1.1)", "(\\textbf{0}\\textsubscript{I}, 6.1.1)", "(0_I, 6.1.1) with bold 0")
c2(94, "proof of (1.4.16): 'évidemment nécessaire (I, 3.2.2)'",
   "(I, 3.2.2)", "(\\textbf{I}, 3.2.2)", "(I, 3.2.2) with bold I")
add(94, "proof of (1.4.16): 'Spec(B) → Spec(A) est plat, il résulte de (1.4.1) que l'on a' (1.4.16.1)",
    "(1.4.1) (crop)", "(1.4.1) (plain text, no link)",
    "misprint_in_print", None, "high", None,
    "The TeX keeps the printed reading. The isomorphism (1.4.16.1) H^i(X⊗_A B, F⊗_A B) = H^i(X, F)⊗_A B is the flat base change of (1.4.15) (X separated over A, Spec(B) → Spec(A) flat: exactly its hypotheses); (1.4.1) is the comparison of Čech and sheaf cohomology for affine covers. The corrected edition already reads (1.4.15).",
    corrected="(\\hyperref[III.1.4.15-fr]{1.4.15})")
c2(94, "proof of (1.4.16): 'par le critère de Serre (II, 5.2.1)'",
   "(II, 5.2.1)", "(\\textbf{II}, 5.2.1)", "(II, 5.2.1) with bold II")

# ---------------- page 95 ----------------
c2(95, "proof of (1.4.17): 'les conditions d1) et d2) de (I, 1.4.1) (avec V=X)'",
   "(I, 1.4.1) (avec", "(\\textbf{I}, 1.4.1) (avec", "(I, 1.4.1) with bold I")
add(95, "proof of (1.4.17): 'vérifie les conditions d1) et d2)'",
    "italic d in d 1) and d 2) (crop); the numbers and parentheses upright",
    "d~1) et d~2): roman d",
    "italics", None, "high",
    {"old": "conditions d~1) et d~2)", "new": "conditions \\textit{d}\\,1) et \\textit{d}\\,2)"},
    "Two letters. Form as in ega1-1-fr.tex for the conditions of (I, 1.4.1): \\textit{d}\\,1).")
add(95, "proof of (1.4.17): 'La vérification de d2) est immédiate'",
    "italic d (crop)", "d~2): roman d",
    "italics", None, "high",
    {"old": "La vérification de d~2)", "new": "La vérification de \\textit{d}\\,2)"})
c2(95, "proof of (1.4.17): 'f^m v(t) = v(f^m t) = 0 (I, 1.4.1), et comme Γ'",
   "(I, 1.4.1), et comme", "(\\textbf{I}, 1.4.1), et comme", "(I, 1.4.1) with bold I")
c2(95, "proof of (1.4.17): 'd'où (I, 1.4.1) l'existence d'un entier'",
   "d'où (I, 1.4.1)", "d'où (\\textbf{I}, 1.4.1)", "(I, 1.4.1) with bold I")
add(95, "proof of (1.4.17), second paragraph: 'Vérifions maintenant d2), et soit t' ∈ Γ(D(f), G)'",
    "italic d (crop)", "d~2): roman d",
    "italics", None, "high",
    {"old": "Vérifions maintenant d~2)", "new": "Vérifions maintenant \\textit{d}\\,2)"},
    "See the misprint finding for the same place.")
add(95, "proof of (1.4.17), second paragraph: 'Vérifions maintenant d2)'",
    "d 2) (crop)", "d~2)",
    "misprint_in_print", None, "high", None,
    "The TeX keeps the printed reading. In (I, 1.4.1) d1) is the extension condition (f^n t extends to a section over V) and d2) the vanishing condition; the first paragraph has just verified d2), and this paragraph proves the extension property (f^{m+n}t' is the restriction of a section over X), i.e. d1). The corrected edition already reads d~1).",
    corrected="\\textit{d}\\,1)")
c2(95, "proof of (1.4.17): 'se prolonge en une section z ∈ Γ(X, H) (I, 1.4.1). Mais'",
   "(I, 1.4.1). Mais", "(\\textbf{I}, 1.4.1). Mais", "(I, 1.4.1) with bold I")
c2(95, "proof of (1.4.17): '(ou de (I, 5.1.9.2))'",
   "(I, 5.1.9.2)", "(\\textbf{I}, 5.1.9.2)", "(I, 5.1.9.2) with bold I")
add(95, "proof of (1.4.17): 'on voit donc que v(f^m t' — t'') = 0'",
    "long dash for the subtraction (40 px against 33 px for '=' and about 22 px for '+'; the same length as the set-difference dash of X—Y on p. 85)",
    "minus sign", "convention", 7, "medium",
    {"old": "v(f^mt'-t'')=0", "new": "v(f^mt'\\setmin t'')=0"},
    "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin as proposed for convention 7, pending that decision.")
add(95, "proof of (1.4.17): 'on a donc f^m t' — t'' = u(s')'",
    "long dash for the subtraction (measured as above)", "minus sign",
    "convention", 7, "medium",
    {"old": "f^mt'-t''=u(s')", "new": "f^mt'\\setmin t''=u(s')"},
    "Subtraction (GLOBAL_ISSUES 23).")
add(95, "proof of (1.4.17): 'comme f^{m+n} t' — f^n t'' = u(f^n s')'",
    "long dash for the subtraction (measured as above)", "minus sign",
    "convention", 7, "medium",
    {"old": "f^{m+n}t'-f^nt''", "new": "f^{m+n}t'\\setmin f^nt''"},
    "Subtraction (GLOBAL_ISSUES 23).")
add(95, "end of the proof of (1.4.17): 'la restriction à D(f) de la section f^n t + u(f^n s) ∈ Γ(X, G)'",
    "f^n t + u(f^n s) (crop)", "$f^nt+u(f^ns)\\in\\Gamma(X,\\mathcal G)$",
    "misprint_in_print", None, "high", None,
    "The TeX keeps the printed reading. s is the section of F over X that extends f^n s' (two lines above), so u(s) restricts to u(f^n s') and f^{m+n}t' = f^n t'' + u(f^n s') is the restriction of f^n t + u(s); u(f^n s) would restrict to u(f^{2n} s'). The corrected edition already reads f^nt+u(s).",
    corrected="$f^nt+u(s)\\in\\Gamma(X,\\mathcal G)$")
c2(95, "(2.1.1): 'considérons l'anneau gradué (0_I, 5.4.6)'",
   "l'anneau gradué (0\\textsubscript{I}, 5.4.6)", "l'anneau gradué (\\textbf{0}\\textsubscript{I}, 5.4.6)",
   "(0_I, 5.4.6) with bold 0")
add(95, "display (2.1.1.1): 'S = Γ_*(X, L) = ⊕_{n∈Z} Γ(X, L^{⊗n}).'",
    "Γ with a subscript asterisk, Γ_* (crop)", "\\Gamma_\\bullet (subscript bullet)",
    "symbol", None, "high",
    {"old": "S=\\Gamma_\\bullet(X,\\mathcal L)", "new": "S=\\Gamma_*(X,\\mathcal L)"},
    "ega3-1-fr.tex writes \\Gamma_* elsewhere (11 times); \\Gamma_\\bullet occurs only here, in (2.1.2.1) and once on p. 90 ('A_\\bullet=\\Gamma_\\bullet(\\mathcal L)').")
add(95, "(2.1.1), after display (2.1.1.1): 'Soit (f_i)_{1⩽i⩽r} une famille finie'",
    "'Soit' begins a new, indented paragraph",
    "no blank line after \\end{equation}: the text continues the paragraph",
    "other", None, "high",
    {"old": "\\end{equation}\nSoit $(f_i)", "new": "\\end{equation}\n\nSoit $(f_i)"},
    "Missing paragraph break.")
add(95, "display (2.1.1.2): end of the first line, H^•(U, F⊗L^{⊗n})",
    "no comma after the closing parenthesis (crop)", "),\\\\",
    "punctuation", None, "high",
    {"old": "\\mathcal L^{\\otimes n}),\\\\", "new": "\\mathcal L^{\\otimes n})\\\\"},
    "(2.1.1.3) ends with a full stop in both.")
add(95, "(2.1.1), after displays (2.1.1.2)-(2.1.1.3): 'Les groupes abéliens (2.1.1.2) et (2.1.1.3) sont bigradués'",
    "'Les groupes abéliens' begins a new, indented paragraph",
    "no blank line after \\end{align}: the text continues the paragraph",
    "other", None, "high",
    {"old": "\\end{align}\nLes groupes", "new": "\\end{align}\n\nLes groupes"},
    "Missing paragraph break.")
add(95, "(2.1.1): 'du fait que F ⇝ H^m(U, F) et ...'",
    "wavy arrow ⇝ (crop)", "\\mapsto",
    "symbol", None, "high",
    {"old": "\\mathcal F\\mapsto H^m(U,\\mathcal F)", "new": "\\mathcal F\\leadsto H^m(U,\\mathcal F)"},
    "Not convention 3 (the printed arrow is not plain); GLOBAL_ISSUES 33.")
add(95, "(2.1.1): '... et F ⇝ H^m(U, F) sont des foncteurs' (the Čech one)",
    "wavy arrow ⇝ (crop)", "\\mapsto",
    "symbol", None, "high",
    {"old": "\\mathcal F\\mapsto H^m(\\mathfrak U,\\mathcal F)", "new": "\\mathcal F\\leadsto H^m(\\mathfrak U,\\mathcal F)"},
    "As above.")
c2(95, "(2.1.2): 'Considérons maintenant le S-module gradué (0_I, 5.4.6)'",
   "$S$-module gradué (0\\textsubscript{I}, 5.4.6)", "$S$-module gradué (\\textbf{0}\\textsubscript{I}, 5.4.6)",
   "(0_I, 5.4.6) with bold 0")
add(95, "display (2.1.2.1): 'M = Γ_*(L, F) = H^0(X, F(*)) = ...'",
    "Γ with a subscript asterisk, Γ_* (crop)", "\\Gamma_\\bullet (subscript bullet)",
    "symbol", None, "high",
    {"old": "M=\\Gamma_\\bullet(\\mathcal L,\\mathcal F)", "new": "M=\\Gamma_*(\\mathcal L,\\mathcal F)"},
    "As for (2.1.1.1).")

# ---------------- checks ----------------
ok = True
texts = {}
for d in F:
    p = d["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8")
    fx = d["fix"]
    if fx is None:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/MISSING", p, n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("NO CHANGE", p, repr(fx["old"]))

# overlapping edits on the same page
for p, t in texts.items():
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = t.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP on page", p, repr(a[2]), repr(b[2]))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter()
for d in F:
    k = "convention" if d["kind"] == "convention" else ("misprint" if d["kind"] == "misprint_in_print" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted(texts):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "all unique" if ok else "PROBLEMS")
