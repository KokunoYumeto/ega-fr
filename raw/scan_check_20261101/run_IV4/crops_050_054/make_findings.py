"""Build findings_050_054.json; '¶' in old/new/corrected stands for a line break."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_050_054.json"

J91 = "Wrong letter: the print's Fraktur capital has the descender of a Fraktur J (GLOBAL_ISSUES 91); ega4-16 writes \\mathfrak{I}."
OM = "Sheaf of differentials: italic Omega (\\varOmega) in the print."
C7 = "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": old.replace("¶", "\n"), "new": new.replace("¶", "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace("¶", "\n")
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 50
add(50, "l. 2 (end of Proposition (16.9.13)): 'des homomorphismes de (16.9.13.1) forment'",
    "reference upright (crop p50_s1_ref1.png)", "italic (inside the italic statement)",
    "convention", 6, "high",
    r"homomorphismes de (16.9.13.1)", r"homomorphismes de \textup{(16.9.13.1)}")
add(50, "Lemme (16.9.13.2): 'J un idéal de A, A'=A/J'",
    "Fraktur J twice (crop p50_s1_l1.png)", r"\mathfrak{I} twice", "symbol", None, "high",
    r"Soient $A$ un anneau, $\mathfrak{I}$ un idéal de $A$,¶$A'=A/\mathfrak{I}$,",
    r"Soient $A$ un anneau, $\mathfrak{J}$ un idéal de $A$,¶$A'=A/\mathfrak{J}$,", J91)
add(50, "Lemme (16.9.13.2): 'L=J+K,'", "Fraktur J (crop p50_s1_l2.png)", r"\mathfrak{I}",
    "symbol", None, "high",
    r"$\mathfrak{L}=\mathfrak{I}+\mathfrak{K}$,", r"$\mathfrak{L}=\mathfrak{J}+\mathfrak{K}$,", J91)
add(50, "display (16.9.13.3), left side and first term: 'J∩K^n = JK^n'",
    "Fraktur J twice (crop p50_s1_eq3.png)", r"\mathfrak{I} twice", "symbol", None, "high",
    r"  \mathfrak{I}\cap\mathfrak{K}^n¶  =\mathfrak{I}\mathfrak{K}^n",
    r"  \mathfrak{J}\cap\mathfrak{K}^n¶  =\mathfrak{J}\mathfrak{K}^n", J91)
add(50, "display (16.9.13.3), last term: '+ J∩K^N.'",
    "no parentheses: 'JK^n + J∩K^N.' (crop p50_s1_eq3.png); Fraktur J",
    r"+(\mathfrak{I}\cap\mathfrak{K}^N).", "extra", None, "high",
    r"+(\mathfrak{I}\cap\mathfrak{K}^N).", r"+\mathfrak{J}\cap\mathfrak{K}^N.",
    "One edit for two differences: parentheses the print lacks, and the Fraktur J (GLOBAL_ISSUES 91).")
add(50, "proof of (16.9.13.2): 'l'hypothèse P(f_1, ..., f_r)∈J signifie que'",
    "Fraktur J", r"\mathfrak{I}", "symbol", None, "high",
    r"\in\mathfrak{I}$ signifie", r"\in\mathfrak{J}$ signifie", J91)
add(50, "proof of (16.9.13.2): 'l'homomorphisme canonique S^n_C(K'/K'^2) → K'^n/K'^{n+1} est bijectif'",
    "in the running text, followed by 'est bijectif' on the same line (crop p50_s2_S.png)",
    "displayed with \\[ ... \\]", "other", None, "high",
    r"canonique¶\[¶  \mathbf{S}_C^n(\mathfrak{K}'/\mathfrak{K}'^2)¶  \longrightarrow\mathfrak{K}'^n/\mathfrak{K}'^{n+1}¶\]¶est bijectif",
    r"canonique¶$\mathbf{S}_C^n(\mathfrak{K}'/\mathfrak{K}'^2)\to\mathfrak{K}'^n/\mathfrak{K}'^{n+1}$ est bijectif",
    "Display vs inline only; no connecting word lost or added.")
add(50, "proof of (16.9.13.2): 'est bijectif (0, 15.1.9)'", "bold 0 (crop p50_s2_S.png)", "plain 0",
    "convention", 2, "high", r"(0, 15.1.9)", r"(\textbf{0}, 15.1.9)")
add(50, "proof of (16.9.13.2): 'appartiennent à L=J+K. Il en résulte'", "Fraktur J", r"\mathfrak{I}",
    "symbol", None, "high",
    r"$\mathfrak{L}=\mathfrak{I}+\mathfrak{K}$. Il", r"$\mathfrak{L}=\mathfrak{J}+\mathfrak{K}$. Il", J91)
add(50, "proof of (16.9.13.2): 'P(f_1, ..., f_r)∈JK^n+K^{n+1}'", "Fraktur J", r"\mathfrak{I}",
    "symbol", None, "high",
    r"\in\mathfrak{I}\mathfrak{K}^n+\mathfrak{K}^{n+1}$", r"\in\mathfrak{J}\mathfrak{K}^n+\mathfrak{K}^{n+1}$", J91)
add(50, "proof of (16.9.13.2): 'et comme P(f_1, ..., f_r)∈J, on a finalement'", "Fraktur J", r"\mathfrak{I}",
    "symbol", None, "high",
    r"$P(f_1,\ldots,f_r)\in\mathfrak{I}$, on a", r"$P(f_1,\ldots,f_r)\in\mathfrak{J}$, on a", J91)
add(50, "end of the proof of (16.9.13.2): 'on a finalement P(f_1, ..., f_r)∈JK^n+J∩K^{n+1}, ce qui prouve le lemme.'",
    "in the running text, without parentheses around J∩K^{n+1}, followed by ', ce qui prouve le lemme' on the same line (crop p50_s2_fin_z.png); Fraktur J twice",
    "displayed with \\[ ... \\]; '+(\\mathfrak{I}\\cap\\mathfrak{K}^{n+1})'", "other", None, "high",
    r"finalement¶\[¶  P(f_1,\ldots,f_r)¶  \in\mathfrak{I}\mathfrak{K}^n¶    +(\mathfrak{I}\cap\mathfrak{K}^{n+1}),¶\]¶ce qui",
    r"finalement¶$P(f_1,\ldots,f_r)\in\mathfrak{J}\mathfrak{K}^n+\mathfrak{J}\cap\mathfrak{K}^{n+1}$, ce qui",
    "One edit for three differences: display vs inline (no connecting word lost or added), parentheses the print lacks, and the Fraktur J (GLOBAL_ISSUES 91).")
add(50, "'les quotients des deux membres de (16.9.13.3) par JK^n, on voit'", "Fraktur J", r"\mathfrak{I}",
    "symbol", None, "high",
    r"$\mathfrak{I}\mathfrak{K}^n$, on voit", r"$\mathfrak{J}\mathfrak{K}^n$, on voit", J91)
add(50, "display (16.9.13.4), left side: '(J∩K^n)/JK^n'", "Fraktur J twice (crop p50_s2_16914.png)",
    r"\mathfrak{I} twice", "symbol", None, "high",
    r"  (\mathfrak{I}\cap\mathfrak{K}^n)/\mathfrak{I}\mathfrak{K}^n¶  \subset",
    r"  (\mathfrak{J}\cap\mathfrak{K}^n)/\mathfrak{J}\mathfrak{K}^n¶  \subset", J91)
add(50, "display (16.9.13.4): 'K^N.(A/(JK^n))'", "baseline period after K^N (crop p50_s2_16914.png)",
    r"\cdot", "symbol", None, "high", r"\cdot(A/", r".(A/", "GLOBAL_ISSUES 65.")
add(50, "display (16.9.13.4), end: '(A/(JK^n))'",
    "no full stop after the formula (crops p50_s2_16914.png, p50_s3); Fraktur J",
    "full stop after the formula; \\mathfrak{I}", "punctuation", None, "high",
    r"(\mathfrak{I}\mathfrak{K}^n)).", r"(\mathfrak{J}\mathfrak{K}^n))",
    "One edit for two differences: the full stop the print lacks, and the Fraktur J (GLOBAL_ISSUES 91).")
add(50, "after (16.9.13.4): 'On en déduit le'", "new indented paragraph after the display (crop p50_s3_ondeduit.png)",
    "follows \\] without a blank line, so it is set without indent", "other", None, "high",
    r"\]¶On en déduit le", r"\]¶¶On en déduit le", "Paragraph break after a display (GLOBAL_ISSUES 47 pattern).")
add(50, "Corollaire (16.9.13.5): 'les hypothèses de (16.9.13.2) et supposons'", "reference upright (crop p50_s3_ref2.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"hypothèses de (16.9.13.2)", r"hypothèses de \textup{(16.9.13.2)}")
add(50, "display (16.9.13.6): 'J∩K^n = JK^n.'", "Fraktur J twice", r"\mathfrak{I} twice", "symbol", None, "high",
    r"\mathfrak{I}\cap\mathfrak{K}^n=\mathfrak{I}\mathfrak{K}^n.", r"\mathfrak{J}\cap\mathfrak{K}^n=\mathfrak{J}\mathfrak{K}^n.", J91)
add(50, "proof of (16.9.13.5): 'puisque A/JK^n est un A-module de type fini'", "Fraktur J", r"\mathfrak{I}",
    "symbol", None, "high",
    r"$A/\mathfrak{I}\mathfrak{K}^n$", r"$A/\mathfrak{J}\mathfrak{K}^n$", J91)
add(50, "'L^2=J^2+JK+K^2=JL+K^2; puisque JL⊂L^2'", "Fraktur J four times", r"\mathfrak{I} four times",
    "symbol", None, "high",
    r"$\mathfrak{L}^2=\mathfrak{I}^2+\mathfrak{I}\mathfrak{K}+\mathfrak{K}^2¶=\mathfrak{I}\mathfrak{L}+\mathfrak{K}^2$; puisque¶$\mathfrak{I}\mathfrak{L}\subset",
    r"$\mathfrak{L}^2=\mathfrak{J}^2+\mathfrak{J}\mathfrak{K}+\mathfrak{K}^2¶=\mathfrak{J}\mathfrak{L}+\mathfrak{K}^2$; puisque¶$\mathfrak{J}\mathfrak{L}\subset", J91)
add(50, "display 'J∩L^2=JL+(J∩K^2)=JL+JK^2=JL,'", "Fraktur J six times", r"\mathfrak{I} six times",
    "symbol", None, "high",
    r"  \mathfrak{I}\cap\mathfrak{L}^2¶  =\mathfrak{I}\mathfrak{L}+(\mathfrak{I}\cap\mathfrak{K}^2)¶  =\mathfrak{I}\mathfrak{L}+\mathfrak{I}\mathfrak{K}^2¶  =\mathfrak{I}\mathfrak{L},",
    r"  \mathfrak{J}\cap\mathfrak{L}^2¶  =\mathfrak{J}\mathfrak{L}+(\mathfrak{J}\cap\mathfrak{K}^2)¶  =\mathfrak{J}\mathfrak{L}+\mathfrak{J}\mathfrak{K}^2¶  =\mathfrak{J}\mathfrak{L},",
    J91 + " The parentheses around J∩K^2 are in the print.")
add(50, "display (16.9.13.7): 'J∩L^2=JL,'", "Fraktur J twice", r"\mathfrak{I} twice", "symbol", None, "high",
    r"\mathfrak{I}\cap\mathfrak{L}^2=\mathfrak{I}\mathfrak{L},", r"\mathfrak{J}\cap\mathfrak{L}^2=\mathfrak{J}\mathfrak{L},", J91)
add(50, "display 'J/JL → (J+L^2)/L^2'", "Fraktur J three times", r"\mathfrak{I} three times",
    "symbol", None, "high",
    r"  \mathfrak{I}/\mathfrak{I}\mathfrak{L}¶  \longrightarrow(\mathfrak{I}+\mathfrak{L}^2)/\mathfrak{L}^2",
    r"  \mathfrak{J}/\mathfrak{J}\mathfrak{L}¶  \longrightarrow(\mathfrak{J}+\mathfrak{L}^2)/\mathfrak{L}^2", J91)

# ---------------------------------------------------------------- page 51
add(51, "l. 2-3: 'O_{Y,x}=A'=A/J où J est un idéal'", "Fraktur J twice", r"\mathfrak{I} twice",
    "symbol", None, "high",
    r"A'=A/\mathfrak{I}$ où $\mathfrak{I}$ est", r"A'=A/\mathfrak{J}$ où $\mathfrak{J}$ est", J91)
add(51, "l. 4: 'engendré par une suite A'-régulière d'éléments de A''",
    "'régulière' italic (crop p51_s1_reguliere.png); the second 'A'-régulière' of the sentence is roman",
    "roman", "italics", None, "high",
    r"suite $A'$-régulière d'éléments de $A'$, eux", r"suite $A'$-\emph{régulière} d'éléments de $A'$, eux")
add(51, "'et L=J+K, on a O_{Y',x}=A/L'", "Fraktur J", r"\mathfrak{I}", "symbol", None, "high",
    r"$\mathfrak{L}=\mathfrak{I}+\mathfrak{K}$, on a", r"$\mathfrak{L}=\mathfrak{J}+\mathfrak{K}$, on a", J91)
add(51, "'l'homomorphisme canonique J/JL → (J+L^2)/L^2 est bijectif.'",
    "in the running text, followed by 'est bijectif.' on the same line; Fraktur J three times",
    "displayed with \\[ ... \\]; \\mathfrak{I}", "other", None, "high",
    r"canonique¶\[¶  \mathfrak{I}/\mathfrak{I}\mathfrak{L}¶  \longrightarrow(\mathfrak{I}+\mathfrak{L}^2)/\mathfrak{L}^2¶\]¶est bijectif.",
    r"canonique¶$\mathfrak{J}/\mathfrak{J}\mathfrak{L}\to(\mathfrak{J}+\mathfrak{L}^2)/\mathfrak{L}^2$ est bijectif.",
    "One edit for two differences: display vs inline (no connecting word lost or added), and the Fraktur J (GLOBAL_ISSUES 91).")
add(51, "display '0 → J/JL → L/L^2 → (L/J)/(L/J)^2 → 0'", "Fraktur J four times", r"\mathfrak{I} four times",
    "symbol", None, "high",
    r"  0\longrightarrow\mathfrak{I}/\mathfrak{I}\mathfrak{L}¶  \longrightarrow\mathfrak{L}/\mathfrak{L}^2¶  \longrightarrow(\mathfrak{L}/\mathfrak{I})/¶    (\mathfrak{L}/\mathfrak{I})^2\longrightarrow0",
    r"  0\longrightarrow\mathfrak{J}/\mathfrak{J}\mathfrak{L}¶  \longrightarrow\mathfrak{L}/\mathfrak{L}^2¶  \longrightarrow(\mathfrak{L}/\mathfrak{J})/¶    (\mathfrak{L}/\mathfrak{J})^2\longrightarrow0", J91)
add(51, "'N_{Y'/Y} est un O_{Y'}-Module localement libre (16.9.8)'",
    "'localement libre' both italic (crop p51_s2_loclibre.png)", "only 'libre' italic", "italics", None, "high",
    r"Module localement \emph{libre} (16.9.8)", r"Module \emph{localement libre} (16.9.8)")
add(51, "heading 16.10", "'16.10. Morphismes différentiellement lisses.' (final full stop; crop p51_s2_heading.png)",
    "no full stop", "punctuation", None, "high",
    r"\subsection{Morphismes différentiellement lisses}", r"\subsection{Morphismes différentiellement lisses.}",
    "GLOBAL_ISSUES 43/58.")
add(51, "Définition (16.10.1): 'est différentiellement lisse (ou que X est différentiellement lisse sur S)'",
    "italic like the rest of the definition, no change of face (crop p51_s2_def.png)",
    "\\emph{...} twice inside the italic definition: comes out upright", "italics", None, "high",
    r"\emph{différentiellement lisse} (ou que $X$ est \emph{différentiellement¶lisse sur $S$}) s'il",
    r"différentiellement lisse (ou que $X$ est différentiellement¶lisse sur $S$) s'il")
add(51, "Définition (16.10.1), label (i)", "upright '(i)' (crop p51_s2_items.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(i)]", r"\item[\textup{(i)}]")
add(51, "Définition (16.10.1) (i): 'Ω^1_{X/S} est un O_X-Module localement projectif'", "italic Omega (crop p51_s2_items.png)",
    r"upright \Omega", "font", None, "high",
    r"$\Omega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement¶  projectif",
    r"$\varOmega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement¶  projectif", OM)
add(51, "Définition (16.10.1) (i): 'Γ(U, Ω^1_{X/S}) soit un'", "italic Omega", r"upright \Omega", "font", None, "high",
    r"\Gamma(U,\Omega_{X/S}^1)$ soit un", r"\Gamma(U,\varOmega_{X/S}^1)$ soit un", OM)
add(51, "Définition (16.10.1), label (ii)", "upright '(ii)' (crop p51_s2_items.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"\item[(ii)]", r"\item[\textup{(ii)}]")
add(51, "Définition (16.10.1) (ii): 'L'homomorphisme canonique (16.3.1.1)'", "reference upright (crop p51_s2_items.png)",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"canonique (16.3.1.1)¶  \[", r"canonique \textup{(16.3.1.1)}¶  \[")
add(51, "Définition (16.10.1) (ii), display 'S^•_{O_X}(Ω^1_{X/S}) → Gr_•(P_{X/S})'", "italic Omega (crop p51_s3_disp.png)",
    r"upright \Omega", "font", None, "high",
    r"^{\bullet}(\Omega_{X/S}^1)", r"^{\bullet}(\varOmega_{X/S}^1)", OM)
add(51, "Définition (16.10.1), last sentence 'En particulier, si ...'",
    "new indented paragraph after 'est bijectif.' (crop p51_s3_enpart.png)",
    "follows \\end{enumerate} without a blank line, so it is set without indent", "other", None, "high",
    r"\end{enumerate}¶En particulier,", r"\end{enumerate}¶¶En particulier,", "Paragraph break as in GLOBAL_ISSUES 80.")
add(51, "Définition (16.10.1): 'En particulier, si Ω^1_{X/S} est localement libre'", "italic Omega (crop p51_s3_enpart.png)",
    r"upright \Omega", "font", None, "high",
    r"si $\Omega_{X/S}^1$ est localement libre de rang fini, les",
    r"si $\varOmega_{X/S}^1$ est localement libre de rang fini, les", OM)
add(51, "Définition (16.10.1), end: '(étant des extensions de tels Modules).'",
    "roman (crop p51_s3_enpart.png)", "italic (inside the definition environment)", "convention", 6, "high",
    r"(étant des extensions de tels Modules)", r"\textup{(étant des extensions de tels Modules)}")
add(51, "'puisque Ω^1_{X/S}=0 en vertu de'", "italic Omega (crop p51_s3_I538.png)", r"upright \Omega",
    "font", None, "high", r"puisque $\Omega_{X/S}^1=0$", r"puisque $\varOmega_{X/S}^1=0$", OM)
add(51, "'en vertu de (I, 5.3.8)'", "bold I (crop p51_s3_I538.png)", "plain I", "convention", 2, "high",
    r"(I, 5.3.8)", r"(\textbf{I}, 5.3.8)", "A genuine EGA I reference (monomorphism and diagonal), not a misread (1.x.y).")
add(51, "Proposition (16.10.2), first word: 'Scient A un anneau'",
    "'Scient': the second letter is an italic c, as in 'discrètes' below, not a broken o (8x crop p51_s4_scient_z8.png)",
    "'Soient': silent correction", "misprint_in_print", None, "high",
    r"Soient $A$ un anneau", r"Scient $A$ un anneau",
    "The fix restores the printed reading.", corrected=r"Soient $A$ un anneau")
add(51, "Proposition (16.10.2): 'pour les topologies discrètes (0, 19.3.1). Alors'",
    "bold 0; reference upright (crop p51_s4_prop.png)", "plain 0; italic inside the statement",
    "convention", 2, "high",
    r"discrètes (0, 19.3.1). Alors", r"discrètes \textup{(\textbf{0}, 19.3.1)}. Alors",
    "Bold 0 (convention 2) and roman reference inside an italic statement (convention 6), one edit.")
add(51, "last line: 'homomorphismes canoniques b ⇝ b⊗1, b ⇝ 1⊗b de B'", "wavy arrows, twice (crop p51_s4_leadsto.png)",
    r"\mapsto twice", "symbol", None, "high",
    r"$b\mapsto b\otimes1$, $b\mapsto1\otimes b$", r"$b\leadsto b\otimes1$, $b\leadsto1\otimes b$",
    "Wavy arrow in the print (GLOBAL_ISSUES 33 pattern).")

# ---------------------------------------------------------------- page 52
add(52, "l. 1: 'dans B⊗_A B) (0, 19.3.5, (iii))'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 19.3.5, (iii))", r"(\textbf{0}, 19.3.5, (iii))")
add(52, "l. 2: 'discrètes (0, 19.3.5, (ii))'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 19.3.5,¶(ii))", r"(\textbf{0}, 19.3.5,¶(ii))")
add(52, "l. 2: 'Posant J=J_{B/A}'", "Fraktur J twice (crop p52_s1_JBA.png)", r"\mathfrak{I} twice", "symbol", None, "high",
    r"$\mathfrak{I}=\mathfrak{I}_{B/A}$", r"$\mathfrak{J}=\mathfrak{J}_{B/A}$", J91)
add(52, "l. 3: 'pour la topologie J-préadique'", "Fraktur J (crop p52_s1_l3_5.png)", r"\mathfrak{I}", "symbol", None, "high",
    r"topologie¶$\mathfrak{I}$-préadique", r"topologie¶$\mathfrak{J}$-préadique", J91)
add(52, "l. 3: 'J-préadique (0, 19.3.8)'", "bold 0 (crop p52_s1_l3_5.png)", "plain 0", "convention", 2, "high",
    r"(0, 19.3.8)", r"(\textbf{0}, 19.3.8)")
add(52, "l. 4: 'B=(B⊗_A B)/J'", "Fraktur J", r"\mathfrak{I}", "symbol", None, "high",
    r"$B=(B\otimes_A B)/\mathfrak{I}$", r"$B=(B\otimes_A B)/\mathfrak{J}$", J91)
add(52, "l. 5: 'de l'équivalence de a) et b) dans'", "a) and b) italic (crop p52_s1_l3_5.png)", "upright",
    "italics", None, "high", r"de a) et b)", r"de \emph{a)} et \emph{b)}")
add(52, "l. 5: 'dans (0, 19.5.4).'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 19.5.4).", r"(\textbf{0}, 19.5.4).")
add(52, "Proposition (16.10.3): 'Si Ω^1_{X/S} est localement libre de rang fini'", "italic Omega (crop p52_s1_omegaSi.png)",
    r"upright \Omega", "font", None, "high",
    r"Si¶$\Omega_{X/S}^1$ est localement libre", r"Si¶$\varOmega_{X/S}^1$ est localement libre", OM)
add(52, "proof of (16.10.3): 'posons J=J_{C/B}'", "Fraktur J twice", r"\mathfrak{I} twice", "symbol", None, "high",
    r"$\mathfrak{I}=\mathfrak{I}_{C/B}$", r"$\mathfrak{J}=\mathfrak{J}_{C/B}$", J91)
add(52, "proof of (16.10.3): 'de la topologie J-préadique;'", "Fraktur J", r"\mathfrak{I}", "symbol", None, "high",
    r"topologie $\mathfrak{I}$-préadique;", r"topologie $\mathfrak{J}$-préadique;", J91)
add(52, "proof of (16.10.3): 'et à l'idéal J de C⊗_B C'", "Fraktur J (crop p52_s2_bc.png)", r"\mathfrak{I}", "symbol", None, "high",
    r"l'idéal¶$\mathfrak{I}$ de", r"l'idéal¶$\mathfrak{J}$ de", J91)
add(52, "proof of (16.10.3): 'l'équivalence de b) et c) dans'", "b) and c) italic (crop p52_s2_bc.png)", "upright",
    "italics", None, "high", r"de b) et c)", r"de \emph{b)} et \emph{c)}")
add(52, "proof of (16.10.3): 'dans (0, 19.5.4), puisque'", "bold 0 (crop p52_s2_bc.png)", "plain 0", "convention", 2, "high",
    r"(0, 19.5.4),", r"(\textbf{0}, 19.5.4),")
add(52, "proof of (16.10.3): '(C⊗_B C)/J=C'", "Fraktur J", r"\mathfrak{I}", "symbol", None, "high",
    r"$(C\otimes_B C)/\mathfrak{I}=C$", r"$(C\otimes_B C)/\mathfrak{J}=C$", J91)
add(52, "'est le rang de Ω^1_{X/S} au point x'", "italic Omega (crop p52_s2_omegarang.png)", r"upright \Omega",
    "font", None, "high",
    r"\emph{rang} de¶$\Omega_{X/S}^1$", r"\emph{rang} de¶$\varOmega_{X/S}^1$", OM)
add(52, "Proposition (16.10.4), label (i)", "upright '(i)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(i)] Si $f$", r"\item[\textup{(i)}] Si $f$")
add(52, "Proposition (16.10.4), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement")
add(52, "Proposition (16.10.4) (ii): 'et Ω^1_{X'/S'} un O_{X'}-Module'", "italic Omega (crop p52_s3_Omega1.png)",
    r"upright \Omega", "font", None, "high",
    r"et $\Omega_{X'/S'}^1$ un", r"et $\varOmega_{X'/S'}^1$ un", OM)
add(52, "Proposition (16.10.4) (ii): 'et Ω^1_{X/S} est un O_X-Module de type fini.'", "italic Omega (crop p52_s3_Omega1.png)",
    r"upright \Omega", "font", None, "high",
    r"$\Omega_{X/S}^1$ est un $\mathcal{O}_X$-Module de type fini.",
    r"$\varOmega_{X/S}^1$ est un $\mathcal{O}_X$-Module de type fini.", OM)
add(52, "proof of (16.10.4): 'l'homomorphisme Gr_n(P_{X/S})⊗_{O_X}O_{X'} → Gr_n(P_{X'/S'}) est bijectif pour tout n, et'",
    "in the running text, followed by 'est bijectif pour' on the same line", "displayed with \\[ ... \\]",
    "other", None, "high",
    r"l'homomorphisme¶\[¶  \mathscr{G}r_n(\mathscr{P}_{X/S})\otimes_{\mathcal{O}_X}\mathcal{O}_{X'}¶  \longrightarrow\mathscr{G}r_n(\mathscr{P}_{X'/S'})¶\]¶est bijectif pour tout $n$, et",
    r"l'homomorphisme¶$\mathscr{G}r_n(\mathscr{P}_{X/S})\otimes_{\mathcal{O}_X}\mathcal{O}_{X'}\to\mathscr{G}r_n(\mathscr{P}_{X'/S'})$ est bijectif pour tout $n$, et",
    "Display vs inline only; no connecting word lost or added.")
add(52, "proof of (16.10.4): 'il résulte encore de (16.4.6) que Gr_n(P_{X/S})⊗_{O_X}O_{X'} → Gr_n(P_{X'/S'}) est bijectif pour tout n.'",
    "in the running text, followed by 'est bijectif pour tout n.' on the next line of the same paragraph", "displayed with \\[ ... \\]",
    "other", None, "high",
    r"(16.4.6) que¶\[¶  \mathscr{G}r_n(\mathscr{P}_{X/S})\otimes_{\mathcal{O}_X}\mathcal{O}_{X'}¶  \longrightarrow\mathscr{G}r_n(\mathscr{P}_{X'/S'})¶\]¶est bijectif pour tout $n$. Supposons",
    r"(16.4.6) que¶$\mathscr{G}r_n(\mathscr{P}_{X/S})\otimes_{\mathcal{O}_X}\mathcal{O}_{X'}\to\mathscr{G}r_n(\mathscr{P}_{X'/S'})$ est bijectif pour tout $n$. Supposons",
    "Display vs inline only; no connecting word lost or added.")
add(52, "proof of (16.10.4): 'et Ω^1_{X'/S'} de rang fini'", "italic Omega (crop p52_s3_Omega2.png)", r"upright \Omega",
    "font", None, "high", r"$\Omega_{X'/S'}^1$ de rang fini", r"$\varOmega_{X'/S'}^1$ de rang fini", OM)
add(52, "proof of (16.10.4): 'de (2.5.2) que Ω^1_{X/S} est un O_X-Module localement libre'", "italic Omega (crop p52_s4_Omega3.png)",
    r"upright \Omega", "font", None, "high",
    r"que $\Omega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement libre",
    r"que $\varOmega_{X/S}^1$ est un $\mathcal{O}_X$-Module localement libre", OM)

# ---------------------------------------------------------------- page 53
add(53, "proof of (16.10.5): 'localement de présentation finie (1.4.3.1)'", "'(1.4.3.1)' (crop p53_s1_1431.png)",
    "'(I, 4.3.1)'", "number", None, "high", r"(I, 4.3.1)", r"(1.4.3.1)",
    "EGA IV's own reference read as (I, ...) (GLOBAL_ISSUES 78).")
add(53, "proof of (16.10.5): 'défini par un Idéal de type fini J, et'", "script J (descender; crop p53_s1_scriptJ.png)",
    r"\mathscr{I}", "symbol", None, "high",
    r"type fini $\mathscr{I}$, et", r"type fini $\mathscr{J}$, et",
    "Wrong letter: the print's script capital has the descender of a script J (cf. GLOBAL_ISSUES 91/95); ega4-16 writes \\mathscr{I}.")
add(53, "proof of (16.10.5): 'Ω^1_{X/S}=J/J^2'", "italic Omega; script J twice (crop p53_s1_scriptJ.png)",
    r"upright \Omega; \mathscr{I} twice", "symbol", None, "high",
    r"$\Omega_{X/S}^1=\mathscr{I}/\mathscr{I}^2$", r"$\varOmega_{X/S}^1=\mathscr{J}/\mathscr{J}^2$",
    "One edit for two differences: script J for the TeX's \\mathscr{I} (twice), and the italic Omega of the sheaf of differentials.")
add(53, "Remarque (16.10.6): 'le O_X-Module Ω^1_{X/S} soit localement libre'", "italic Omega (crop p53_s1_Omega2.png)",
    r"upright \Omega", "font", None, "high",
    r"$\Omega_{X/S}^1$ soit localement libre", r"$\varOmega_{X/S}^1$ soit localement libre", OM)
add(53, "Remarque (16.10.6): 'Il résulte alors de (0, 20.4.7)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.4.7)", r"(\textbf{0}, 20.4.7)")
add(53, "Remarque (16.10.6), end: 'Γ(U, Ω^1_{X/S}).'", "italic Omega (crop p53_s1_Omega3.png)", r"upright \Omega",
    "font", None, "high", r"\Gamma(U,\Omega_{X/S}^1)$.", r"\Gamma(U,\varOmega_{X/S}^1)$.", OM)
add(53, "heading 16.11: 'sur un S-préschéma'", "bold upright S, like the rest of the heading (crop p53_s2_heading_S.png)",
    "$S$: light math italic S in the bold heading", "font", None, "high",
    r"sur un $S$-préschéma", r"sur un S-préschéma",
    "Same treatment as the p-bases titles of ega0-21 (GLOBAL_ISSUES 46c). The PDF-string argument already has a plain S.")
add(53, "heading 16.11", "'... différentiellement lisse.' (final full stop; crop p53_s2_heading.png)", "no full stop",
    "punctuation", None, "high",
    r"différentiellement¶lisse}{Opérateurs", r"différentiellement¶lisse.}{Opérateurs", "GLOBAL_ISSUES 43/58.")
add(53, "(16.11.1): 'système de générateurs de Ω^1_{X/S}|U=Ω^1_{U/S}'", "italic Omega twice (crop p53_s2_omegaXU.png)",
    r"upright \Omega twice", "font", None, "high",
    r"$\Omega_{X/S}^1|U=\Omega_{U/S}^1$. Soit", r"$\varOmega_{X/S}^1|U=\varOmega_{U/S}^1$. Soit", OM)
add(53, "display (16.11.1.1): 'd^m z_λ — z_λ'", "long dash for the minus (crop p53_s2_16111.png; longer than the bars of =)",
    "-", "convention", 7, "high", r"d^m z_\lambda-z_\lambda", r"d^m z_\lambda\setmin z_\lambda", C7)
add(53, "display (16.11.1.3): 'p!/(q!(p—q)!)'", "long dash for the minus (crop p53_s3_16113.png)",
    "-", "convention", 7, "high", r"(\mathbf{p}-\mathbf{q})!)", r"(\mathbf{p}\setmin\mathbf{q})!)", C7)
add(53, "display (16.11.1.6): '(d^m z — z)^p'", "long dash for the minus (crop p53_s3_16116.png)",
    "-", "convention", 7, "high", r"d^m\mathbf{z}-\mathbf{z}", r"d^m\mathbf{z}\setmin\mathbf{z}",
    C7 + " The short minus signs in the exponents p−q of (16.11.1.5)-(16.11.1.6) are ordinary minus signs, as in the TeX.")
add(53, "display (16.11.1.6): '(—1)^{|p−q|}'", "long dash for the unary minus (crop p53_s3_16116.png)",
    "-", "convention", 7, "high", r"(-1)^{|\mathbf{p}-\mathbf{q}|}", r"(\setmin 1)^{|\mathbf{p}-\mathbf{q}|}", C7)
add(53, "display (16.11.1.6), left side: 'ζ^p'",
    "the exponent is a light italic p (5x crop p53_s3_zetap.png), not the bold upright p of ζ^p in (16.11.1.4) and in the text below (crop p53_s4_zetap_text_z.png)",
    "\\mathbf{p}: silent correction", "misprint_in_print", None, "high",
    r"\boldsymbol{\zeta}^{\mathbf{p}}¶  =(", r"\boldsymbol{\zeta}^{p}¶  =(",
    "Wrong-fount exponent (GLOBAL_ISSUES 29: wrong-font letters are reproduced in the diplomatic text). The fix restores the printed reading; it does not overlap the convention-7 edit of the same display.",
    corrected=r"\boldsymbol{\zeta}^{\mathbf{p}}")
add(53, "'Comme les dz_λ engendrent Ω^1_{X/S} et sont'", "italic Omega (crop p53_s4_omega.png)", r"upright \Omega",
    "font", None, "high", r"engendrent $\Omega_{X/S}^1$ et", r"engendrent $\varOmega_{X/S}^1$ et", OM)

# ---------------------------------------------------------------- page 54
add(54, "display (16.11.1.7), last term: '⟨ζ^p, D⟩ z^{p−q}'",
    "the exponent of ζ is a bold p (4x crop p54_s1_16117_zeta.png)", "\\boldsymbol{\\zeta}^{\\mathbf{q}}: silent correction",
    "misprint_in_print", None, "high",
    r"\langle\boldsymbol{\zeta}^{\mathbf{q}},D\rangle", r"\langle\boldsymbol{\zeta}^{\mathbf{p}},D\rangle",
    "By (16.11.1.5), d^m(z^p) = Σ_{q≤p} (p q) z^{p−q} ζ^q, so ⟨d^m(z^p), D⟩ = Σ (p q) ⟨ζ^q, D⟩ z^{p−q}; the printed ζ^p is wrong (no erratum in Liste 3). The fix restores the printed reading.",
    corrected=r"\langle\boldsymbol{\zeta}^{\mathbf{q}},D\rangle")
add(54, "Théorème (16.11.2): 'engendre Ω^1_{X/S}|U=Ω^1_{U/S}.'", "italic Omega twice (crop p54_s1_Omega_thm.png)",
    r"upright \Omega twice", "font", None, "high",
    r"$\Omega_{X/S}^1|U=\Omega_{U/S}^1$. Les", r"$\varOmega_{X/S}^1|U=\varOmega_{U/S}^1$. Les", OM)
add(54, "Théorème (16.11.2), label a)", "upright 'a)' (crop p54_s1_label_a.png)", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[a)]", r"\item[\textup{a)}]", "GLOBAL_ISSUES 88 (hand-set labels inside italic statements).")
add(54, "Théorème (16.11.2) a): 'base du O_U-Module Ω^1_{U/S}.'", "italic Omega (crop p54_s1_Omega_a.png)",
    r"upright \Omega", "font", None, "high",
    r"du $\mathcal{O}_U$-Module $\Omega_{U/S}^1$.", r"du $\mathcal{O}_U$-Module $\varOmega_{U/S}^1$.", OM)
add(54, "Théorème (16.11.2), label b)", "upright 'b)' (crop p54_s1_DpL.png)", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[b)]", r"\item[\textup{b)}]", "GLOBAL_ISSUES 88 (hand-set labels inside italic statements).")
add(54, "Théorème (16.11.2) b): 'une famille (D_p)_{p∈N}(L)'",
    "the '(L)' is set full size on the line after the subscript p∈N, not as the exponent of N (crop p54_s1_DpL.png)",
    "(D_p)_{p∈N^{(L)}}: silent correction", "misprint_in_print", None, "high",
    r"(D_{\mathbf{p}})_{\mathbf{p}\in\mathbb{N}^{(L)}}", r"(D_{\mathbf{p}})_{\mathbf{p}\in\mathbb{N}}(L)",
    "Misplaced exponent of N^(L) (cf. N^(L) in (16.11.2.1)-(16.11.2.2)). The fix restores the printed reading.",
    corrected=r"(D_{\mathbf{p}})_{\mathbf{p}\in\mathbb{N}^{(L)}}")
add(54, "Théorème (16.11.2) b): 'dans lui-même, vérifiant les conditions'", "comma after 'lui-même' (crop p54_s1_luimeme.png)",
    "no comma", "punctuation", None, "high", r"lui-même vérifiant", r"lui-même, vérifiant")
add(54, "Théorème (16.11.2), 'De plus, lorsque ces conditions sont vérifiées'",
    "new indented paragraph after (16.11.2.1) (crop p54_s2_deplus.png)",
    "follows \\end{enumerate} without a blank line, so it is set without indent", "other", None, "high",
    r"\end{enumerate}¶De plus,", r"\end{enumerate}¶¶De plus,", "Paragraph break as in GLOBAL_ISSUES 80.")
add(54, "Théorème (16.11.2): 'par les conditions (16.11.2.1) et vérifie'", "reference upright",
    "italic (inside the italic statement)", "convention", 6, "high",
    r"conditions¶(16.11.2.1) et vérifie", r"conditions¶\textup{(16.11.2.1)} et vérifie")
add(54, "Théorème (16.11.2): 'une base du O_U-Module Diff^m_{U/S}, autrement dit'",
    "script D with italic 'iff' (sheaf of differential operators; crop p54_s2_Diff.png); the group D∈Diff^m_{U/S} on p. 53 is roman",
    r"\operatorname{Diff}: roman Diff", "symbol", None, "high",
    r"$\operatorname{Diff}_{U/S}^m$, autrement dit", r"$\mathscr{D}\!iff_{U/S}^m$, autrement dit",
    "Written as the edition's other script Diff (ega4-16 (16.8.4): \\mathscr{D}\\!iff_{X/S}^n).")
add(54, "proof of (16.11.2): 'donc forment une base du O_U-Module Ω^1_{U/S}. Puis'",
    "UPRIGHT Omega (3x crop p54_s3_OmegaUS.png), unlike the italic Omega of the same sheaf in the statement (crop p54_s1_Omega_thm.png)",
    r"upright \Omega: the TeX keeps the printed reading", "misprint_in_print", None, "medium",
    None, None,
    "Wrong-fount Omega for the sheaf Ω^1_{U/S} (the print reserves the upright Omega for modules of differentials). Diplomatic text keeps \\Omega here; a global \\Omega -> \\varOmega pass must skip this occurrence.",
    corrected=r"\varOmega_{U/S}^1")
add(54, "proof of (16.11.2): 'et cela prouve que b) entraîne a).'", "b) and a) italic (crop p54_s3_ba.png)", "upright",
    "italics", None, "high", r"prouve que b) entraîne a)", r"prouve que \emph{b)} entraîne \emph{a)}")
add(54, "proof of (16.11.2): 'forment une base de P^m_{U/S} pour |p|≤m entraînant'",
    "light italic p between the bars (2.2x crop p54_s3_pitalic2.png), not the bold p of the other |p|≤m on the page",
    r"|\mathbf{p}|: silent correction", "misprint_in_print", None, "high",
    r"pour $|\mathbf{p}|\leq m$ entraînant", r"pour $|p|\leq m$ entraînant",
    "Wrong-fount letter (GLOBAL_ISSUES 29). The fix restores the printed reading.",
    corrected=r"pour $|\mathbf{p}|\leq m$ entraînant")
add(54, "proof of (16.11.2): 'Cela prouve donc que a) entraîne b),'", "a) and b) italic (crop p54_s4_ab.png)", "upright",
    "italics", None, "high", r"donc que a) entraîne b)", r"donc que \emph{a)} entraîne \emph{b)}")
add(54, "proof of (16.11.2): 'une base du dual Diff^m_{U/S} de P^m_{U/S}'",
    "script D with italic 'iff' (crop p54_s4_Diff.png)", r"\operatorname{Diff}: roman Diff", "symbol", None, "high",
    r"dual¶$\operatorname{Diff}_{U/S}^m$", r"dual¶$\mathscr{D}\!iff_{U/S}^m$",
    "Written as the edition's other script Diff (ega4-16 (16.8.4)).")


# ---------------------------------------------------------------- checks
def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
spans = {}
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    t = page_text(f["page"])
    old = f["fix"]["old"]
    n = t.count(old)
    if n != 1:
        ok = False
        print("COUNT", n, f["page"], repr(old))
        continue
    s = t.index(old)
    spans.setdefault(f["page"], []).append((s, s + len(old), i))

for p, lst in spans.items():
    lst.sort()
    for (a1, b1, i1), (a2, b2, i2) in zip(lst, lst[1:]):
        if a2 < b1:
            ok = False
            print("OVERLAP", p, F[i1]["where"], "|", F[i2]["where"])

# sequential application in list order
for p in sorted({f["page"] for f in F}):
    t = page_text(p)
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        if t.count(f["fix"]["old"]) != 1:
            ok = False
            print("SEQ", p, repr(f["fix"]["old"]))
            continue
        t = t.replace(f["fix"]["old"], f["fix"]["new"])
    (HERE / f"applied_{p:03d}.tex").write_text(t, encoding="utf-8")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
cnt = {}
for f in F:
    c = cnt.setdefault(f["page"], [0, 0, 0])
    c[2 if f["kind"] == "misprint_in_print" else 1 if f["kind"] == "convention" else 0] += 1
print("ok" if ok else "PROBLEMS", len(F), {p: "/".join(map(str, c)) for p, c in sorted(cnt.items())})
