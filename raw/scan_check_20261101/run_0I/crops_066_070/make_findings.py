"""Build findings_066_070.json and check that every fix's 'old' occurs exactly once in its page file."""
import json
import pathlib

RUN = pathlib.Path(r"user/Documents/ega_scan_check_20261101/run_0I")
NL = "\u23ce"  # placeholder for a line break inside 'old'/'new'


def s(x):
    return None if x is None else x.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None, misprint=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": s(old), "new": s(new)}}
    if misprint:
        d["corrected"] = s(corrected)
    d["note"] = note
    return d


BAR = ("Checked on an enlarged crop. Analogue of convention 8 for an overline; here it also changes the "
       "statement: the print speaks of the powers of the closure (bar over the Fraktur J only).")
HAT = "Checked on an enlarged crop. Same meaning; the analogue of convention 8 for a hat and a prime (as reported for p. 196)."
INLINE = "Layout only (display vs inline); the formula itself matches."
C6REF = "Checked on a crop: the parentheses and old-style figures are roman inside the italic statement."

f = []
# ---------------- p. 66
f.append(F(66, "Exemple (7.2.12): 'J̄^n est l'adhérence de l'image canonique de J^n'",
           "bar over the Fraktur J only, exponent n outside the bar", r"$\overline{\mathfrak J^n}$ (bar over J^n)",
           "formula", None, "high",
           r"$\overline{\mathfrak J^n}$ est l'adhérence", r"$\overline{\mathfrak J}^n$ est l'adhérence",
           BAR + " With the bar over J^n the sentence becomes a tautology."))
f.append(F(66, "Exemple (7.2.12): 'A/J̄^n s'identifie à B/J^n'",
           "A/J̄^n, bar over J only", r"$A/\overline{\mathfrak J^n}$", "formula", None, "high",
           r"$A/\overline{\mathfrak J^n}$", r"$A/\overline{\mathfrak J}^n$", BAR))
f.append(F(66, "Exemple (7.2.12): 'J̄/J̄^2 est isomorphe à J/J^2'",
           "J̄/J̄^2, bar over J only, exponent 2 outside", r"$\overline{\mathfrak J}/\overline{\mathfrak J^2}$",
           "formula", None, "high",
           r"\overline{\mathfrak J}/\overline{\mathfrak J^2}", r"\overline{\mathfrak J}/\overline{\mathfrak J}^2", BAR))
f.append(F(66, "Exemple (7.2.12), 2nd sentence: 'J̄^nM s'identifie à l'adhérence de l'image canonique de J^nN'",
           "J̄^nM, bar over J only", r"$\overline{\mathfrak J^n}M$", "formula", None, "high",
           r"$\overline{\mathfrak J^n}M$ s'identifie", r"$\overline{\mathfrak J}^nM$ s'identifie", BAR))
f.append(F(66, "Exemple (7.2.12), end: 'et M/J̄^nM à N/J^nN'",
           "M/J̄^nM, bar over J only", r"$M/\overline{\mathfrak J^n}M$", "formula", None, "high",
           r"$M/\overline{\mathfrak J^n}M$", r"$M/\overline{\mathfrak J}^nM$", BAR))
f.append(F(66, "(7.3.1), 1st sentence: '(resp. M̂ = lim M/J^nM)'",
           "index u under the second lim (a turned n); the lim of Â on the same line has n",
           r"\varprojlim_u (keeps the printed u)", "misprint_in_print", None, "high", None, None,
           "Checked on an enlarged crop. The TeX keeps the printed reading. The limit is taken over n, the exponent "
           "of J^n, as for Â = lim_n A/J^n just before.",
           corrected=r"\widehat M=\varprojlim_n M/\mathfrak J^nM", misprint=True))
f.append(F(66, "(7.3.1): 'Soit M' →u M →v M'' → 0 une suite exacte de A-modules'",
           "the exact sequence is in the running text", r"displayed with \[ ... \]", "other", None, "high",
           r"\[⏎  M'\xrightarrow{u}M\xrightarrow{v}M''\to0⏎\]", r"$M'\xrightarrow{u}M\xrightarrow{v}M''\to0$",
           INLINE))
f.append(F(66, "(7.3.1): 'il existe z' = (z'_n) ∈ M̂' tel que'",
           "hat over M only, prime after it (M̂′)", r"\widehat{M'}", "formula", None, "high",
           r"\in\widehat{M'}$", r"\in\widehat{M}'$", HAT))
f.append(F(66, "(7.3.1): 'l'image par û de M̂' est dense'",
           "hat over M only, prime after it (M̂′)", r"\widehat{M'}", "formula", None, "high",
           r"de $\widehat{M'}$ est", r"de $\widehat{M}'$ est", HAT))
f.append(F(66, "Théorème de Krull (7.3.2): 'Soient A un anneau noethérien'",
           "'noethérien' roman inside the italic statement", "noethérien italic (namedtheorem body)",
           "convention", 6, "high",
           r"Soient $A$ un anneau noethérien,", r"Soient $A$ un anneau \textup{noethérien},",
           "Checked on an enlarged crop."))
f.append(F(66, "Théorème de Krull (7.3.2): 'M un A-module de type fini'",
           "'de type fini' roman inside the italic statement", "de type fini italic", "convention", 6, "high",
           r"$A$-module de type fini, $M'$", r"$A$-module \textup{de type fini}, $M'$",
           "Checked on an enlarged crop."))
f.append(F(66, "Lemme d'Artin-Rees (7.3.2.1): 'Sous les hypothèses de (7.3.2)'",
           "reference (7.3.2) roman inside the italic statement", "(7.3.2) italic", "convention", 6, "high",
           r"hypothèses de (7.3.2), il existe", r"hypothèses de \textup{(7.3.2)}, il existe", C6REF))
f.append(F(66, "Lemme d'Artin-Rees (7.3.2.1), display 'M'∩J^nM = J^{n-p}(M'∩J^pM)'",
           "no punctuation after the display", r"(M'\cap\mathfrak J^pM).", "punctuation", None, "high",
           r"(M'\cap\mathfrak J^pM).", r"(M'\cap\mathfrak J^pM)", "Checked on a crop. Minor."))
f.append(F(66, "after (7.3.2.1): 'Pour la démonstration, voir ([1], p. 2-04)'",
           "[1]: old-style figure 1 (the same glyph as the old-style 1 elsewhere on the page)",
           "[I] (capital letter I)", "number", None, "high",
           r"([I], p.~2-04)", r"([1], p.~2-04)",
           "Checked on a crop. bib-fr.tex numbers the bibliography 1-22 (\\bibitem{I-1} = H. Cartan et C. "
           "Chevalley, Séminaire de l'ENS 1955-56); the TeX read the old-style 1 as the letter I."))
# ---------------- p. 67
f.append(F(67, "Corollaire (7.3.3): 'Sous les hypothèses de (7.3.2)'",
           "reference (7.3.2) roman inside the italic statement", "(7.3.2) italic", "convention", 6, "high",
           r"hypothèses de (7.3.2), l'application", r"hypothèses de \textup{(7.3.2)}, l'application", C6REF))
f.append(F(67, "Corollaire (7.3.3), end: 'est un A-module plat (6.1.1)'",
           "reference (6.1.1) roman inside the italic statement", "(6.1.1) italic", "convention", 6, "high",
           r"plat (6.1.1).", r"plat \textup{(6.1.1)}.", C6REF))
f.append(F(67, "proof of (7.3.3): 'Soit en effet 0→M'→M→M''→0 une suite exacte'",
           "the exact sequence is in the running text", r"displayed with \[ ... \]", "other", None, "high",
           r"\[⏎  0\to M'\xrightarrow{u}M\xrightarrow{v}M''\to0⏎\]",
           r"$0\to M'\xrightarrow{u}M\xrightarrow{v}M''\to0$", INLINE))
f.append(F(67, "proof of (7.3.3): 'on sait déjà que v̂ : M̂ → M̂'' est surjectif'",
           "hat over M only, primes after it (M̂″)", r"\widehat{M''}", "formula", None, "high",
           r"\to\widehat{M''}$", r"\to\widehat{M}''$", HAT))
f.append(F(67, "proof of (7.3.3): 'sur les applications M⊗_AÂ → M⊗_A(A/J^n) = M/J^nM. Il est clair'",
           "the formula is in the running text", r"displayed with \[ ... \]", "other", None, "high",
           r"\[⏎  M\otimes_A\widehat A\to⏎  M\otimes_A(A/\mathfrak J^n)=M/\mathfrak J^nM.⏎\]",
           r"$M\otimes_A\widehat A\to M\otimes_A(A/\mathfrak J^n)=M/\mathfrak J^nM$.", INLINE))
f.append(F(67, "proof of (7.3.3), diagram, top row 'A^p⊗Â → A^q⊗Â → M⊗Â → 0'",
           "plain ⊗ without the subscript A, three times", r"\otimes_A three times", "formula", None, "high",
           r"A^p\otimes_A\widehat A \arrow[r] \arrow[d] &⏎  A^q\otimes_A\widehat A \arrow[r] \arrow[d] &⏎"
           r"  M\otimes_A\widehat A \arrow[r] \arrow[d] &",
           r"A^p\otimes\widehat A \arrow[r] \arrow[d] &⏎  A^q\otimes\widehat A \arrow[r] \arrow[d] &⏎"
           r"  M\otimes\widehat A \arrow[r] \arrow[d] &",
           "Checked on an enlarged crop: none of the three ⊗ of the diagram has a subscript (the running text has ⊗_A)."))
f.append(F(67, "Corollaire (7.3.4), display, second isomorphism '(Hom_A(M, N))^ ⥲ Hom_Â(M̂, N̂)'",
           "outer parentheses of ordinary size, like the inner ones", r"\bigl( ... \bigr)", "formula", None,
           "medium", r"\bigl(\operatorname{Hom}_A(M,N)\bigr)^\wedge", r"(\operatorname{Hom}_A(M,N))^\wedge",
           "Checked on a crop. Minor (parenthesis size only)."))
f.append(F(67, "Corollaire (7.3.4), end of the display",
           "no punctuation after Hom_Â(M̂, N̂)", r"(\widehat M,\widehat N).", "punctuation", None, "high",
           r"(\widehat M,\widehat N).", r"(\widehat M,\widehat N)", "Checked on a crop. Minor."))
f.append(F(67, "Corollaire (7.3.5) b): 'Â est un A-module fidèlement plat (6.4.1)'",
           "reference (6.4.1) roman inside the italic statement", "(6.4.1) italic", "convention", 6, "high",
           r"plat (6.4.1).", r"plat \textup{(6.4.1)}.", C6REF))
f.append(F(67, "proof of (7.3.5): 'donc m = ⋂_{p⩾0}(m+J^p), et comme'",
           "the formula ends the line of running text", r"displayed with \[ ... \]", "other", None, "high",
           r"donc⏎\[⏎  \mathfrak m=\bigcap_{p\geq0}(\mathfrak m+\mathfrak J^p),⏎\]⏎et comme",
           r"donc $\mathfrak m=\bigcap_{p\geq0}(\mathfrak m+\mathfrak J^p)$,⏎et comme",
           INLINE + " The print sets p⩾0 under ⋂ even in the line (index position, ignored)."))
# ---------------- p. 68
f.append(F(68, "Corollaire (7.3.7): 'Sous les hypothèses de (7.3.2)'",
           "reference (7.3.2) roman inside the italic statement", "(7.3.2) italic", "convention", 6, "high",
           r"hypothèses de (7.3.2), le noyau", r"hypothèses de \textup{(7.3.2)}, le noyau", C6REF))
f.append(F(68, "after Définition (7.4.1): 'Lorsque A est noethérien, le séparé complété'",
           "'noethérien' in italics", "noethérien upright (no \\emph)", "italics", None, "high",
           r"Lorsque $A$ est noethérien,", r"Lorsque $A$ est \emph{noethérien},", "Checked on a crop."))
f.append(F(68, "proof of (7.4.2): 'en vertu de (1.7.4) et (1.7.2)'",
           "(1.7.4) with the old-style figure 1: chapter 0, §1.7", "(I.7.4) (capital letter I)", "number", None,
           "high", r"(I.7.4)", r"(1.7.4)",
           "Checked on an enlarged crop. The references are to (0, 1.7.4) and (0, 1.7.2) (support of a module); "
           "the TeX read the old-style 1 as the letter I."))
f.append(F(68, "proof of (7.4.2): 'en vertu de (1.7.4) et (1.7.2)'",
           "(1.7.2) with the old-style figure 1", "(I.7.2)", "number", None, "high",
           r"(I.7.2)", r"(1.7.2)", "Checked on an enlarged crop; as for (1.7.4)."))
f.append(F(68, "proof of (7.4.2): 'l'annulateur du B-module M (1.7.5)'",
           "(1.7.5) with the old-style figure 1", "(I.7.5)", "number", None, "high",
           r"(I.7.5)", r"(1.7.5)", "Checked on an enlarged crop; as for (1.7.4)."))
f.append(F(68, "proof of (7.4.2), last line: 'on en conclut ([11], p. 127, cor. 4)'",
           "[11]: two old-style figures 1 (the same glyph as the 1 of 127)", "[III] (three letters I)", "number",
           None, "high", r"([III], p.~127", r"([11], p.~127",
           "Checked on an enlarged crop. Bibliography item 11 (\\bibitem{I-11}) is P. Samuel, Commutative algebra "
           "(Notes by D. Herzig)."))
# ---------------- p. 69
f.append(F(69, "proof of (7.4.2), display 'n^{hk}M ⊂ (mB+b)^hM = m^hM ⊂ n^hM'",
           "no punctuation after the display", r"\subset\mathfrak n^hM,", "punctuation", None, "high",
           r"\subset\mathfrak n^hM,", r"\subset\mathfrak n^hM", "Checked on a crop. Minor."))
f.append(F(69, "Corollaire (7.4.3): 'Sous les hypothèses de (7.4.2)'",
           "reference (7.4.2) roman inside the italic statement", "(7.4.2) italic", "convention", 6, "high",
           r"(7.4.2), si en outre", r"\textup{(7.4.2)}, si en outre", C6REF))
f.append(F(69, "Corollaire (7.4.5): 'Sous les hypothèses de (7.4.2)'",
           "reference (7.4.2) roman inside the italic statement", "(7.4.2) italic", "convention", 6, "high",
           r"(7.4.2), si $\mathfrak b$", r"\textup{(7.4.2)}, si $\mathfrak b$", C6REF))
f.append(F(69, "(7.5.1), last lines: 'telles que lim c_α = 0'",
           "lim without any index", r"\lim_\alpha c_\alpha=0", "formula", None, "high",
           r"$\lim_\alpha c_\alpha=0$", r"$\lim c_\alpha=0$", "Checked on an enlarged crop: nothing under lim."))
# ---------------- p. 70
f.append(F(70, "(7.5.1): 'pour J_μ ⊂ J_λ et α ∉ H_λ et par passage à la limite'",
           "no comma after α∉H_λ (end of a line)", r"$\alpha\notin H_\lambda$, et", "punctuation", None, "high",
           r"$\alpha\notin H_\lambda$, et", r"$\alpha\notin H_\lambda$ et", "Checked on an enlarged crop."))
f.append(F(70, "(7.5.1): 'on a φ_{λ,α}(y_μ) ∈ J_λ pour J_μ ⊂ J_λ et α ∉ H_λ'",
           "φ_{λ,α}(y_μ)", r"\varphi_{\lambda,\alpha}(y_\mu) (keeps the print)", "misprint_in_print", None,
           "medium", None, None,
           "The TeX keeps the printed reading. φ_{λ,α} is defined on B_λ; the coefficient of T^α in y_μ ∈ B_μ is "
           "φ_{μ,α}(y_μ), and the passage to the limit giving φ_α(y) ∈ J_λ needs φ_{μ,α}(y_μ) ∈ J_λ (mod J_μ) for "
           "J_μ ⊂ J_λ and α ∉ H_λ; read through B_μ → B_λ, φ_{λ,α}(y_μ) is the coefficient of y_λ, which is 0 by the "
           "definition of H_λ. Not in the errata lists 1-3.",
           corrected=r"\varphi_{\mu,\alpha}(y_\mu)\in\mathfrak J_\lambda", misprint=True))
f.append(F(70, "(7.5.2), second display: '[(A{T_1,…,T_r}){T_{r+1},…,T_s} ⥲ A{T_1,…,T_s}'",
           "a stray opening bracket before the display, with no closing bracket", r"\Bigl[ kept",
           "misprint_in_print", None, "medium", None, None,
           "The TeX keeps the mark. It has the shape of a bracket but is rough-edged, like the inked spacing after "
           "'dont' in l. 7 of this page, so it may be a printing artefact rather than a character; either way the "
           "corrected edition drops it. Its height is about that of the braces, so a plain [ would match the print "
           "better than \\Bigl[.",
           corrected=r"(A\{T_1,\ldots,T_r\})\{T_{r+1},\ldots,T_s\}\xrightarrow{\sim}A\{T_1,\ldots,T_s\}",
           misprint=True))
f.append(F(70, "(7.5.3): 'il existe un homomorphisme continu et un seul ū : A{T_1,…,T_r} → B, tel que'",
           "no commas around 'et un seul' ('… continu et un seul ū : …')",
           r"\emph{un homomorphisme continu, et un seul}, (two commas)", "punctuation", None, "high",
           r"\emph{un homomorphisme continu, et un seul},", r"\emph{un homomorphisme continu et un seul}",
           "Checked on a crop."))
f.append(F(70, "(7.5.3), display: 'ū(Σc_αT^α) = Σu(c_α)b_1^{α_1} … b_r^{α_r} ;'",
           "baseline dots between b_1^{α_1} and b_r^{α_r}", r"\cdots (centred dots)", "symbol", None, "high",
           r"b_1^{\alpha_1}\cdots b_r^{\alpha_r}~;", r"b_1^{\alpha_1}\ldots b_r^{\alpha_r}~;",
           "Checked on an enlarged crop: the dots stand on the baseline."))
f.append(F(70, "(7.5.3): 'la famille (u(c_α)b_1^{α_1} … b_r^{α_r}) est sommable'",
           "baseline dots", r"\cdots (centred dots)", "symbol", None, "high",
           r"$(u(c_\alpha)b_1^{\alpha_1}\cdots b_r^{\alpha_r})$", r"$(u(c_\alpha)b_1^{\alpha_1}\ldots b_r^{\alpha_r})$",
           "Checked on an enlarged crop."))
f.append(F(70, "Proposition (7.5.4), label (i)", "label (i) upright", r"\item[(i)] in the italic proposition",
           "convention", 6, "high", r"\item[(i)] Si $A$", r"\item[\textup{(i)}] Si $A$",
           "As for the labels on pp. 150-154 (GLOBAL_ISSUES 16)."))
f.append(F(70, "Proposition (7.5.4), label (ii)", "label (ii) upright", r"\item[(ii)] in the italic proposition",
           "convention", 6, "high", r"\item[(ii)] Soient $A$", r"\item[\textup{(ii)}] Soient $A$",
           "As for the labels on pp. 150-154 (GLOBAL_ISSUES 16)."))

# ---------------- paragraph breaks (measured left edges of the printed lines)
PB = ("Spurious paragraph break at a page break that falls inside the paragraph (GLOBAL_ISSUES item 20): the first "
      "line of the new page is flush left (measured on the strip). \\oldpage ends with \\ignorespaces, so joining the "
      "lines leaves a single space. ")
f.append(F(65, "end of p. 65 / top of p. 66, Remarque (7.2.11): '… les A_i = A/J^{i+1} vérifient | les conditions de (7.2.7)'",
           "one sentence across the page break; p. 66 begins flush left", "blank line before \\oldpage[0\\textsubscript{I}]{66}",
           "other", None, "high", "vérifient⏎⏎", "vérifient⏎",
           PB + "Lies in page 65's segment (outside pp. 66-70; checked unique in page_065.tex and in the release file); "
           "findings_061_065.json has no entry for it. Apply together with the p. 66 entry that removes the blank line "
           "after the marker."))
f.append(F(66, "top of p. 66: 'les conditions de (7.2.7) ; comme A est …' (continues Remarque (7.2.11) from p. 65)",
           "no paragraph break: the first line continues the sentence, flush left",
           "blank line after \\oldpage[0\\textsubscript{I}]{66}", "other", None, "high",
           r"\oldpage[0\textsubscript{I}]{66}⏎⏎les conditions", r"\oldpage[0\textsubscript{I}]{66}⏎les conditions",
           PB + "Apply together with the p. 65 entry 'vérifient'."))
f.append(F(67, "end of p. 67 / top of p. 68, proof of (7.3.5): '… pour p assez | grand, d'où …'",
           "one sentence across the page break; p. 68 begins flush left", "blank line before \\oldpage[0\\textsubscript{I}]{68}",
           "other", None, "high", r"pour $p$ assez⏎⏎", r"pour $p$ assez⏎",
           PB + "Apply together with the p. 68 entry that removes the blank line after the marker."))
f.append(F(68, "top of p. 68: 'grand, d'où J^p ⊂ m …' (continues the proof of (7.3.5))",
           "no paragraph break: the first line continues the sentence, flush left",
           "blank line after \\oldpage[0\\textsubscript{I}]{68}", "other", None, "high",
           r"\oldpage[0\textsubscript{I}]{68}⏎⏎grand,", r"\oldpage[0\textsubscript{I}]{68}⏎grand,",
           PB + "Apply together with the p. 67 entry 'pour $p$ assez'."))
f.append(F(68, "end of p. 68 / top of p. 69, proof of (7.4.2): '… mB+b est un idéal | de définition de B'",
           "one sentence across the page break; p. 69 begins flush left", "blank line before \\oldpage[0\\textsubscript{I}]{69}",
           "other", None, "high", r"est un idéal⏎⏎", r"est un idéal⏎",
           PB + "Apply together with the p. 69 entry that removes the blank line after the marker."))
f.append(F(69, "top of p. 69: 'de définition de B, autrement dit …' (continues the proof of (7.4.2))",
           "no paragraph break: the first line continues the sentence, flush left",
           "blank line after \\oldpage[0\\textsubscript{I}]{69}", "other", None, "high",
           r"\oldpage[0\textsubscript{I}]{69}⏎⏎de définition", r"\oldpage[0\textsubscript{I}]{69}⏎de définition",
           PB + "Apply together with the p. 68 entry 'est un idéal'."))
f.append(F(69, "end of p. 69 / top of p. 70, (7.5.1): '… à coefficients dans A. | Pour tout voisinage V de 0 dans A'",
           "no paragraph break: the last line of p. 69 is full and p. 70 begins flush left (paragraphs are indented)",
           "blank line before \\oldpage[0\\textsubscript{I}]{70}", "other", None, "high",
           r"à coefficients dans $A$.⏎⏎", r"à coefficients dans $A$.⏎",
           "Spurious paragraph break at the page break (GLOBAL_ISSUES item 20): (7.5.1) continues as one paragraph "
           "(measured left edges). Apply together with the p. 70 entry that removes the blank line after the marker."))
f.append(F(70, "top of p. 70: 'Pour tout voisinage V de 0 dans A, …' (continues (7.5.1))",
           "no paragraph break: the first line is flush left", "blank line after \\oldpage[0\\textsubscript{I}]{70}",
           "other", None, "high",
           r"\oldpage[0\textsubscript{I}]{70}⏎⏎Pour tout", r"\oldpage[0\textsubscript{I}]{70}⏎Pour tout",
           "Spurious paragraph break at the page break (GLOBAL_ISSUES item 20). Apply together with the p. 69 entry "
           "'à coefficients dans $A$.'."))
f.append(F(69, "(7.4.4), after item (ii): 'Lorsqu'il en est ainsi, tout B-module de type fini …'",
           "new paragraph: the line is indented like the other paragraphs (measured)",
           "\\end{enumerate} directly followed by 'Lorsqu'il' (LaTeX continues without indent)", "other", None, "high",
           r"\end{enumerate}⏎Lorsqu'il", r"\end{enumerate}⏎⏎Lorsqu'il", "Paragraph break only."))

# ---------------- check
bad = 0
for x in f:
    if x["fix"] is None:
        continue
    t = (RUN / f"page_{x['page']:03d}.tex").read_text(encoding="utf-8")
    n = t.count(x["fix"]["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/MISSING", x["page"], n, repr(x["fix"]["old"]))
out = RUN / "findings_066_070.json"
out.write_text(json.dumps(f, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter()
for x in f:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    c[(x["page"], k)] += 1
for p in range(65, 71):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("findings:", len(f), "bad olds:", bad, "->", out)
