"""Build findings_011_015.json for EGA IV-1 chapter 0, printed pages 11-15 (scan check).
Strings are raw; the pilcrow stands for a line break (LF) in 'old'/'new'."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_011_015.json"
NL = "¶"


def fx(old, new):
    return {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}


def F(page, where, scan, tex, kind, conv, conf, fix, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------- page 11 ----------------
L.append(F(11, "end of the proof of (14.3.2): 'il résulte de b) que codim(Z_1, Z_n)=...'",
           "il résulte de b) que, with b) in italic", "il résulte de b) que (upright b))",
           "italics", None, "high", fx(r"il résulte de b) que", r"il résulte de \emph{b)} que"),
           "The letter references to the conditions are italic in the print on pp. 11-12 (checked on a crop); same style as earlier checkers' \\emph{c)}."))
for lab in "abcd":
    L.append(F(11, f"Proposition (14.3.3), label {lab})", f"roman label '{lab})' without an opening parenthesis",
               rf"\item[\rm({lab})]", "punctuation", None, "high", fx(rf"\item[\rm({lab})]", rf"\item[\textup{{{lab})}}]"),
               "Labels a)-d) are upright, with no opening parenthesis (checked on a crop); \\item[\\rm(a)] prints '(a)'. Same fix as run_I_b p. 148." if lab == "a" else None))
L.append(F(11, "proof of (14.3.3): 'une composante irréductible de X (0_I, 2.1.3); en outre'",
           "(0_I, 2.1.3) with a bold 0", r"($0_{\mathrm I}$, 2.1.3)", "convention", 2, "high",
           fx(r"de $X$ ($0_{\mathrm I}$, 2.1.3)~;", r"de $X$ ($\mathbf{0}_{\mathrm I}$, 2.1.3)~;")))
L.append(F(11, "proof of (14.3.3): 'l'équivalence de a) et b), et prouvent aussi que si a) est vérifiée'",
           "a), b), a) in italic", "upright a), b), a)", "italics", None, "high",
           fx(r"de a) et b), et prouvent aussi que si a)", r"de \emph{a)} et \emph{b)}, et prouvent aussi que si \emph{a)}")))
L.append(F(11, "proof of (14.3.3): 'on en conclut que c) entraîne b).'", "c) and b) in italic", "upright c), b)",
           "italics", None, "high", fx(r"on en conclut que c) entraîne b).", r"on en conclut que \emph{c)} entraîne \emph{b)}.")))
L.append(F(11, "proof of (14.3.3): 'un point fermé en vertu de (0_I, 2.1.3))'", "(0_I, 2.1.3) with a bold 0",
           r"($0_{\mathrm I}$,¶2.1.3)".replace(NL, " "), "convention", 2, "high",
           fx(r"en vertu de ($0_{\mathrm I}$,", r"en vertu de ($\mathbf{0}_{\mathrm I}$,")))
L.append(F(11, "end of the proof of (14.3.3): 'd) entraîne b).'", "d) and b) in italic", "upright d), b)",
           "italics", None, "high", fx(r"2.1.3)), d) entraîne b).", r"2.1.3)), \emph{d)} entraîne \emph{b)}.")))
L.append(F(11, "heading 15.1 (printed on p. 12; in page_011.tex as the continuation from ega0-15-fr.tex, before that file's first marker)",
           "'15.1. Suites M-régulières et suites M-quasi-régulières.' with a final full stop",
           r"\subsection{Suites ...-quasi-régulières} without the full stop", "punctuation", None, "high",
           fx(r"\texorpdfstring{$M$}{M}-quasi-régulières}", r"\texorpdfstring{$M$}{M}-quasi-régulières.}"),
           "Printed on p. 12, not p. 11: the lead of ega0-15-fr.tex (lines 1-11) is attached to page_011.tex only because of the duplicate p. 12 marker (see the p. 12 marker finding). It lies before ega0-15-fr.tex's first marker: apply by hand (ega0-15-fr.tex line 6). None of the 62 \\subsection titles of the EGA IV-1 files has the final full stop."))
# ---------------- page 12 ----------------
L.append(F(12, "page marker \\oldpage[0\\textsubscript{IV-1}]{12} at ega0-15-fr.tex line 12 (after the § 15 and 15.1 headings and \\begin{env}[15.1.1]\\label)",
           "printed p. 12 begins 'La dernière égalité résulte de ce que si Y_0={x}⊂...' (end of the proof of (14.3.4)); then (14.3.5), its proof, Remarque (14.3.6), the headings § 15 and 15.1 and the opening of (15.1.1) down to '... il est immédiat que cette classe'",
           "the marker occurs twice: ega0-14-fr.tex line 565 (right place, before \\begin{proof} 'La dernière égalité') and again ega0-15-fr.tex line 12",
           "marker", None, "high",
           fx(r"\oldpage[0\textsubscript{IV-1}]{12}¶Soient $A$ un anneau", r"Soient $A$ un anneau"),
           "Remove the duplicate: ega0-15-fr.tex lines 1-30 then precede that file's first marker ({13}) and continue p. 12, as printed. Because of the duplicate, prep_batch.py replaced the ega0-14 part of p. 12, so page_012.tex lacks ega0-14-fr.tex lines 565-611; I checked those lines against the scan directly (the next two findings). apply_fixes.py locates p. 12 in ega0-14-fr.tex: this edit and the (15.1.1) paragraph fix lie in ega0-15-fr.tex and must be applied by hand."))
L.append(F(12, "proof of (14.3.4) (top of p. 12): 'si Y_0={x}⊂Y_1⊂...⊂Y_m est une chaîne maximale'",
           "Y_0={x}⊂Y_1⊂. . .⊂Y_m with baseline dots (checked on a crop)", r"Y_1\subset\cdots\subset Y_m",
           "symbol", None, "high", fx(r"Y_1\subset\cdots\subset Y_m", r"Y_1\subset\ldots\subset Y_m"),
           "'old' lies in ega0-14-fr.tex lines 565-611 (that file's p. 12 segment, where it is unique), not in page_012.tex (see the marker finding)."))
L.append(F(12, "proof of (14.3.5): 'X' vérifie trivialement les conditions (14.3.3, c))'",
           "(14.3.3, c)) with c) in italic (checked on a crop)", "(14.3.3, c))", "italics", None, "high",
           fx(r"(14.3.3, c))", r"(14.3.3, \emph{c)})"),
           "'old' lies in ega0-14-fr.tex lines 565-611 (unique there), not in page_012.tex. The rest of lines 565-611 ((14.3.5), its proof, Remarque (14.3.6)) matches the print."))
L.append(F(12, "(15.1.1): '... et A[T_1, ..., T_n] par le degré total. Soient M un A-module, f_i (1⩽i⩽n) ...'",
           "'Soient M un A-module' continues the same paragraph: flush left, no indent (checked on a crop)",
           "blank line before 'Soient $M$': a new paragraph", "other", None, "high",
           fx(r"par le degré total.¶¶Soient", r"par le degré total.¶Soient"),
           "In ega0-15-fr.tex (lines 16-18): apply by hand (see the marker finding)."))
# ---------------- page 13 ----------------
L.append(F(13, "(15.1.1), last paragraph: 'si l'homothétie f_M : x⇝fx de M est injective'",
           "x ⇝ fx (wavy arrow; checked on a crop)", r"$f_M:x\mapsto fx$", "symbol", None, "high",
           fx(r"l'homothétie $f_M:x\mapsto fx$ de $M$", r"l'homothétie $f_M:x\leadsto fx$ de $M$"),
           "Wavy maps-to arrow, written \\leadsto as in run_0III p. 11; not convention 3 (the printed arrow is not plain)."))
L.append(F(13, "proof of (15.1.2): 'l'homothétie f_M : x⇝fx définit par passage aux quotients'",
           "x ⇝ fx (wavy arrow; checked on a crop)", r"$f_M:x\mapsto fx$", "symbol", None, "high",
           fx(r"$f_M:x\mapsto fx$ définit", r"$f_M:x\leadsto fx$ définit")))
L.append(F(13, "proof of (15.1.2): '(Bourbaki, Alg. comm., chap. III, § 2, nº 8, cor. 1 du th. 1)'",
           "nº 8 (raised o)", r"no~8 (prints 'no 8')", "symbol", None, "high",
           fx(r"no~8", r"n\textsuperscript{o}~8"),
           "ega0-15/16/17-fr.tex write no~N (53 times) where the other files write n\\textsuperscript{o}."))
L.append(F(13, "proof of (15.1.3): '(Bourbaki, Alg. comm., chap. II, § 3, nº 4, th. 1)'",
           "nº 4 (raised o)", r"no~4", "symbol", None, "high", fx(r"no~4", r"n\textsuperscript{o}~4")))
L.append(F(13, "proof of (15.1.3): 'il en est donc de même de φ' (0_I, 1.3.2)'", "(0_I, 1.3.2) with a bold 0",
           r"($0_{\mathrm I}$, 1.3.2)", "convention", 2, "high",
           fx(r"($0_{\mathrm I}$, 1.3.2)", r"($\mathbf{0}_{\mathrm I}$, 1.3.2)")))
L.append(F(13, "proof of (15.1.3): 'la topologie (fA)-préadique (0_I, 7.3.5)'", "(0_I, 7.3.5) with a bold 0",
           r"($0_{\mathrm I}$, 7.3.5)", "convention", 2, "high",
           fx(r"($0_{\mathrm I}$, 7.3.5)", r"($\mathbf{0}_{\mathrm I}$, 7.3.5)")))
L.append(F(13, "Définition (15.1.4): 'est M-régulier (resp. M-quasi-régulier) si'",
           "'régulier' and 'quasi-régulier' italic like the rest of the statement; 'resp.' upright (checked on a crop)",
           r"\emph{$M$-régulier} (resp. \emph{$M$-quasi-régulier}) in the \itshape definition: the two words come out upright, 'resp.' italic",
           "convention", 6, "high",
           fx(r"\emph{$M$-régulier} (resp. \emph{$M$-quasi-régulier})", r"$M$-régulier (\textup{resp.} $M$-quasi-régulier)"),
           "Both halves of convention 6 in one edit: \\emph dropped (no change of face in the print), 'resp.' set upright."))
L.append(F(13, "Définition (15.1.4): '(resp. si l'homomorphisme (15.1.2.1) est bijectif)'",
           "'resp.' upright", "'resp.' italic (\\itshape definition)", "convention", 6, "high",
           fx(r"(resp. si l'homomorphisme", r"(\textup{resp.} si l'homomorphisme")))
L.append(F(13, "end of page_013.tex: \\begin{env}[15.1.5] and its \\label (the heading (15.1.5) opens printed p. 14)",
           "p. 13 ends '... mais f est alors diviseur de zéro dans M.'; p. 14 begins '(15.1.5) Supposons maintenant'",
           "\\begin{env}[15.1.5] and \\label{0.15.1.5-fr} stand before \\oldpage[0\\textsubscript{IV-1}]{14}",
           "marker", None, "high", fx(r"\begin{env}[15.1.5]¶\label{0.15.1.5-fr}¶", r""),
           "Two-part move (the env opening moves, not the marker, so each edit stays in its own page segment): the p. 14 marker finding re-inserts these two lines after \\oldpage[0\\textsubscript{IV-1}]{14}. Apply both or neither."))
# ---------------- page 14 ----------------
L.append(F(14, "top of p. 14: '(15.1.5) Supposons maintenant M muni d'une filtration'",
           "p. 14 begins with the heading (15.1.5)", "page_014.tex begins after \\begin{env}[15.1.5]\\label (those lines are in p. 13's segment)",
           "marker", None, "high",
           fx(r"\oldpage[0\textsubscript{IV-1}]{14}¶Supposons maintenant",
              r"\oldpage[0\textsubscript{IV-1}]{14}¶\begin{env}[15.1.5]¶\label{0.15.1.5-fr}¶Supposons maintenant"),
           "Second half of the move begun by the p. 13 marker finding. Apply both or neither."))
L.append(F(14, "(15.1.5.1): 'M'_k=M_k+𝔍M_{k-1}+...+𝔍^{k-1}M_1+𝔍^kM_0'",
           "+ . . . + with baseline dots (checked on an enlarged crop)", r"+\cdots+", "symbol", None, "high",
           fx(r"\mathfrak{J}M_{k-1}+\cdots+", r"\mathfrak{J}M_{k-1}+\ldots+")))
L.append(F(14, "(15.1.5): 'Notons encore (gr_•(M)⊗_A(A/𝔍))[T_1, ..., T_n] le produit tensoriel'",
           "the formula is inline, in the running line (checked on a crop)", "displayed formula", "other", None, "high",
           fx(r"Notons encore¶\[¶  (\gr_\bullet(M)\otimes_A(A/\mathfrak{J}))[T_1,\ldots,T_n]¶\]¶le produit",
              r"Notons encore¶$(\gr_\bullet(M)\otimes_A(A/\mathfrak{J}))[T_1,\ldots,T_n]$¶le produit"),
           "Layout: inline in the print, displayed in the TeX."))
L.append(F(14, "(15.1.5): 'le produit tensoriel de A-modules gradués (II, 2.1.2)'", "(II, 2.1.2) with a bold II",
           r"($\mathrm{II}$, 2.1.2)", "convention", 2, "high",
           fx(r"($\mathrm{II}$, 2.1.2)", r"(\textbf{II}, 2.1.2)")))
L.append(F(14, "(15.1.5): '(II, 2.1.2) (gr_•(M)⊗_A(A/𝔍))⊗_A A[T_1, ..., T_n].'",
           "the formula is inline, at the end of the running line, followed by 'On définit' in the same paragraph",
           "displayed formula", "other", None, "high",
           fx(r"\[¶  (\gr_\bullet(M)\otimes_A(A/\mathfrak{J}))¶  \otimes_A A[T_1,\ldots,T_n].¶\]",
              r"$(\gr_\bullet(M)\otimes_A(A/\mathfrak{J}))\otimes_A A[T_1,\ldots,T_n]$."),
           "Layout: inline in the print, displayed in the TeX."))
L.append(F(14, "proof of (15.1.6), unnumbered display after (15.1.6.1): 'gr_i(Q_k)=(gr_i(M)⊗_A(A/fA))T^{k-1}.'",
           "T^{k-1}: exponent k minus the figure 1 (checked on an enlarged crop)", r"T^{k-i}",
           "misprint_in_print", None, "high",
           fx(r"(\gr_i(M)\otimes_A(A/fA))T^{k-i}.", r"(\gr_i(M)\otimes_A(A/fA))T^{k-1}."),
           "The TeX silently corrects the print; the diplomatic text should keep T^{k-1}. By (15.1.6.1), gr_i(Q_k) is the term j=k-i, and the print itself has T^{k-i} two lines below.",
           corrected=r"\gr_i(Q_k)=(\gr_i(M)\otimes_A(A/fA))T^{k-i}."))
L.append(F(14, "proof of (15.1.6): '(Bourbaki, Alg. comm., chap. III, § 3, nº 8, cor. 1 du th. 1)'",
           "nº 8 (raised o)", r"no~8", "symbol", None, "high", fx(r"no~8", r"n\textsuperscript{o}~8")))
L.append(F(14, "proof of (15.1.6): 'Or on a gr_i(Q_k)=((M_i/M_{i+1})⊗_A(A/fA))T^{k-i}=(M_i/(fM_i+M_{i+1}))T^{k-i}; d'autre part'",
           "inline formula with a second equality '=(M_i/(fM_i+M_{i+1}))T^{k-i}' (checked on a crop)",
           r"displayed \gr_i(Q_k)=((M_i/M_{i+1})\otimes_A(A/fA))T^{k-i}~; without the second equality",
           "missing", None, "high",
           fx(r"Or on¶a¶\[¶  \gr_i(Q_k)=((M_i/M_{i+1})\otimes_A(A/fA))T^{k-i}~;¶\]",
              r"Or on¶a $\gr_i(Q_k)=((M_i/M_{i+1})\otimes_A(A/fA))T^{k-i}=(M_i/(fM_i+M_{i+1}))T^{k-i}$~;"),
           "The edit also sets the formula inline, as printed."))
L.append(F(14, "proof of (15.1.6): '(Q'_k)_{i+1} est l'image de M_k+fM_{k-1}+...+f^{k-i-1}M_{i+1}'",
           "+ . . . + with baseline dots (checked on an enlarged crop)", r"+\cdots+", "symbol", None, "high",
           fx(r"M_k+fM_{k-1}+\cdots+f^{k-i-1}M_{i+1}", r"M_k+fM_{k-1}+\ldots+f^{k-i-1}M_{i+1}")))
# ---------------- page 15 (order matters: the p. 14 text in page_015.tex first, then the marker move) -------
L.append(F(15, "(15.1.6.2) (printed on p. 14; in page_015.tex because the p. 15 marker stands too early)",
           "+ . . . + with baseline dots (checked on an enlarged crop)", r"+\cdots+", "symbol", None, "high",
           fx(r"f^{k-i}x\in M_k+fM_{k-1}+\cdots+", r"f^{k-i}x\in M_k+fM_{k-1}+\ldots+"),
           "Apply before the marker move below; afterwards this text belongs to p. 14's segment. The rest of the p. 14 text in page_015.tex (down to 'entraîne donc (en raisonnant') matches the print."))
L.append(F(15, "page marker \\oldpage[0\\textsubscript{IV-1}]{15}, new place: proof of (15.1.6), '(en raisonnant | dans M/M_{i+1})'",
           "p. 14 ends '... La relation f^{k-i}x∈f^{k+1-i}M+M_{i+1} entraîne donc (en raisonnant'; p. 15 begins 'dans M/M_{i+1}) l'existence d'un y∈M'",
           "the marker stands 12 lines too early, before 'dans $M'_k/M'_{k+1}$. On est donc ramené' (printed p. 14)",
           "marker", None, "high",
           fx(r"entraîne donc (en raisonnant dans¶$M/M_{i+1}$)",
              r"entraîne donc (en raisonnant¶\oldpage[0\textsubscript{IV-1}]{15}¶dans $M/M_{i+1}$)"),
           "Move, part 1 of 2: insert the marker here first; the next finding removes the old one. Apply in this order (with the old marker removed first, p. 15 cannot be located)."))
L.append(F(15, "page marker \\oldpage[0\\textsubscript{IV-1}]{15}, old place: before 'dans M'_k/M'_{k+1}. On est donc ramené'",
           "this text is printed at the bottom of p. 14", "\\oldpage[0\\textsubscript{IV-1}]{15} before it",
           "marker", None, "high",
           fx(r"\oldpage[0\textsubscript{IV-1}]{15}¶dans $M'_k/M'_{k+1}$.", r"dans $M'_k/M'_{k+1}$."),
           "Move, part 2 of 2: remove the old marker after the insertion above."))
L.append(F(15, "Définition (15.1.7): 'On dit qu'elle est M-régulière si'",
           "'régulière' italic like the rest of the statement (checked on a crop)",
           r"\emph{$M$-régulière}: upright inside the \itshape definition", "convention", 6, "high",
           fx(r"\emph{$M$-régulière}", r"$M$-régulière")))
L.append(F(15, "Définition (15.1.7): 'la suite (f_i) est M-quasi-régulière si'",
           "'quasi-régulière' italic like the rest of the statement", r"\emph{$M$-quasi-régulière}: upright",
           "convention", 6, "high", fx(r"\emph{$M$-quasi-régulière}", r"$M$-quasi-régulière")))
L.append(F(15, "after Définition (15.1.7): 'Lorsque M=A, on dit simplement « suite régulière » et « suite quasi-régulière ».'",
           "a roman paragraph after the italic statement", "inside the \\itshape definition environment: italic",
           "convention", 6, "high",
           fx(r"est bijectif.¶¶Lorsque $M=A$, on dit simplement «~suite régulière~» et¶«~suite quasi-régulière~».¶\end{definition}",
              r"est bijectif.¶\end{definition}¶¶Lorsque $M=A$, on dit simplement «~suite régulière~» et¶«~suite quasi-régulière~»."),
           "Close the definition before the sentence (a new indented roman paragraph, as printed), as done for Lemme (13.7.7.2) in run_0III."))
L.append(F(15, "proof of (15.1.8): 'Posons 𝔍''=Σ_{i=1}^{n-1} f_iA, de sorte que'",
           "the formula is inline (checked on a crop)", "displayed formula", "other", None, "high",
           fx(r"Posons¶\[¶  \mathfrak{J}''=\sum_{i=1}^{n-1}f_iA,¶\]¶de sorte que",
              r"Posons¶$\mathfrak{J}''=\sum_{i=1}^{n-1}f_iA$,¶de sorte que"),
           "Layout: inline in the print (limits above and below the Σ), displayed in the TeX."))
L.append(F(15, "proof of (15.1.8): 'M''_k=M_k+𝔍''M_{k-1}+...+𝔍''^{k-1}M_1+𝔍''^kM_0;'",
           "+ . . . + with baseline dots", r"+\cdots+", "symbol", None, "high",
           fx(r"\mathfrak{J}''M_{k-1}+\cdots+", r"\mathfrak{J}''M_{k-1}+\ldots+")))
L.append(F(15, "proof of (15.1.8): 'M'_k=M''_k+f_nM''_{k-1}+...+f_n^{k-1}M''_1+f_n^kM''_0.'",
           "+ . . . + with baseline dots", r"+\cdots+", "symbol", None, "high",
           fx(r"f_nM''_{k-1}+\cdots+", r"f_nM''_{k-1}+\ldots+")))
L.append(F(15, "proof of (15.1.8): 'Notons gr''_•(M) le A-module gradué associé à la filtration (M''_k)'",
           "new indented paragraph after the display (checked on a crop)", "no blank line after \\]: same paragraph",
           "other", None, "high", fx(r"\]¶Notons $\gr''_\bullet(M)$", r"\]¶¶Notons $\gr''_\bullet(M)$")))
L.append(F(15, "proof of (15.1.8), display 'à des isomorphismes canoniques près', left side: '(gr_•(M)⊗(A/𝔍))⊗A[T_1, ..., T_n]'",
           "⊗A[T_1, ..., T_n]: tensor sign without index A (checked on a crop)", r"\otimes_A A[T_1,\ldots,T_n]",
           "formula", None, "high",
           fx(r"\otimes(A/\mathfrak{J}))\otimes_A A[T_1,\ldots,T_n]", r"\otimes(A/\mathfrak{J}))\otimes A[T_1,\ldots,T_n]")))
L.append(F(15, "same display, right side: '...[T_1, ..., T_{n-1}]⊗(A/f_nA)⊗A[T_n]'",
           "⊗A[T_n] without index A", r"\otimes_A A[T_n]", "formula", None, "high",
           fx(r"T_{n-1}]¶  \otimes(A/f_nA)\otimes_A A[T_n]", r"T_{n-1}]¶  \otimes(A/f_nA)\otimes A[T_n]")))
L.append(F(15, "(15.1.8.1): '(gr''_•(M)⊗(A/fA))[T_n] → gr'_•(M)'",
           "(A/fA): f without the index n (checked on an enlarged crop)", r"(A/f_nA)", "misprint_in_print", None, "high",
           fx(r"(\gr''_\bullet(M)\otimes(A/f_nA))[T_n]", r"(\gr''_\bullet(M)\otimes(A/fA))[T_n]"),
           "The TeX silently corrects the print; the diplomatic text should keep A/fA. The element is f_n (no f is defined in this proof; the next display has A/f_nA).",
           corrected=r"(\gr''_\bullet(M)\otimes(A/f_nA))[T_n]"))
L.append(F(15, "proof of (15.1.8), display after 'et', source: '...[T_1, ..., T_{n-1}])⊗(A/f_nA)⊗A[T_n]'",
           "⊗A[T_n] without index A (checked on a crop)", r"\otimes_A A[T_n]", "formula", None, "high",
           fx(r"T_{n-1}])¶  \otimes(A/f_nA)\otimes_A A[T_n]", r"T_{n-1}])¶  \otimes(A/f_nA)\otimes A[T_n]")))
L.append(F(15, "same display, target: 'gr''_•(M)⊗(A/f_nA)⊗A[T_n]'",
           "⊗A[T_n] without index A", r"\otimes_A A[T_n]", "formula", None, "high",
           fx(r"\gr''_\bullet(M)\otimes(A/f_nA)\otimes_A A[T_n]", r"\gr''_\bullet(M)\otimes(A/f_nA)\otimes A[T_n]")))
L.append(F(15, "proof of (15.1.8): 'Mais gr''_•(M) s'identifie à (gr_•(M)⊗(A/𝔍''))[T_1, ..., T_{n-1}];'",
           "the formula is inline (checked on a crop)", "displayed formula", "other", None, "high",
           fx(r"s'identifie à¶\[¶  (\gr_\bullet(M)\otimes(A/\mathfrak{J}''))¶  [T_1,\ldots,T_{n-1}]~;¶\]",
              r"s'identifie à¶$(\gr_\bullet(M)\otimes(A/\mathfrak{J}''))[T_1,\ldots,T_{n-1}]$~;"),
           "Layout: inline in the print, displayed in the TeX."))
L.append(F(15, "proof of (15.1.8): 'par hypothèse, l'homothétie de rapport f_n dans gr_•(M)⊗(A/𝔍'') est bijective'",
           "est bijective", "est bijective~; (the printed reading is kept)", "misprint_in_print", None, "medium",
           None,
           "The hypothesis ((f_i) gr_•(M)-régulière) gives only that this homothety is injective (f_n non diviseur de zéro), and injectivity is what the conclusion (f_n gr''_•(M)-régulier) needs; 'bijective' is too strong. The proof of (15.1.9) has the same step with 'est injective' (ega0-15-fr.tex line 335).",
           corrected=r"par hypothèse, l'homothétie de rapport $f_n$ dans $\gr_\bullet(M)\otimes(A/\mathfrak{J}'')$ est injective~;"))
L.append(F(15, "Proposition (15.1.9): 'les A-modules M, M/f_1M, ..., M/(Σ_{1⩽j⩽n-1} f_jM) sont séparés'",
           "the list is inline (checked on a crop)", "displayed formula (with \\quad)", "other", None, "high",
           fx(r"les $A$-modules¶\[¶  M,\quad M/f_1M,\quad\ldots,\quad¶  M/\left(\sum_{1\leq j\leq n-1}f_jM\right)¶\]¶sont séparés",
              r"les $A$-modules¶$M$, $M/f_1M$, \ldots, $M/\left(\sum_{1\leq j\leq n-1}f_jM\right)$¶sont séparés"),
           "Layout: inline in the print, displayed in the TeX."))
L.append(F(15, "proof of (15.1.9), last line of p. 15: 'Notons que si on pose 𝔍''=Σ_{i=1}^{n-1} f_iA,'",
           "the formula is inline, at the end of the line (checked on the strip)", "displayed formula", "other", None, "high",
           fx(r"Notons que si on pose¶\[¶  \mathfrak{J}''=\sum_{i=1}^{n-1}f_iA,¶\]",
              r"Notons que si on pose¶$\mathfrak{J}''=\sum_{i=1}^{n-1}f_iA$,"),
           "Layout: inline in the print, displayed in the TeX; the p. 16 marker follows directly."))

json.dump(L, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", OUT, len(L))
