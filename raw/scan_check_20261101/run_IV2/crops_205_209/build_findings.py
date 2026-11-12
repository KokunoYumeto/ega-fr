"""Build findings_205_209.json (strings are raw; the pilcrow stands for a line break) and check every edit:
'old' must occur exactly once in the original page_NNN.tex (CRLF normalised) and exactly once at its turn when the
edits are applied in list order."""
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
run = here.parent
OUT = run / "findings_205_209.json"
NL = "¶"
F = []


def f(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}),
             note=note)
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n")
    F.append(d)


CAT = "Bold italic category letter (enlarged crop); \\mathcal gives a script C. As GLOBAL_ISSUES 35 (bold italic C, \\boldsymbol)."
HAT = "Hat over the letter only, prime outside the hat (enlarged crop). Same pattern as convention 8, with a hat (GLOBAL_ISSUES 63)."
INL = "GLOBAL_ISSUES 21 (formula printed in the running text); connecting words unchanged."
REM = "Judged with the remark body roman (document-wide remark item)."

# ---------------- page 205 ----------------
f(205, "Lemme (7.5.1.1), l. 1: 'Soit C une sous-catégorie pleine'", "bold italic C", "$\\mathcal C$", "font", None, "high",
  r"Soit $\mathcal C$ une", r"Soit $\boldsymbol{C}$ une", CAT)
f(205, "Lemme (7.5.1.1), l. 2: 'd'un anneau de C appartienne encore à C'", "bold italic C (twice)", "$\\mathcal C$ twice", "font", None, "high",
  r"$\mathcal C$ appartienne encore à $\mathcal C$", r"$\boldsymbol{C}$ appartienne encore à $\boldsymbol{C}$", "Two occurrences in one edit.")
f(205, "Lemme (7.5.1.1), l. 2: 'si C ∈ C et si t'", "second C bold italic", "$C\\in\\mathcal C$", "font", None, "high",
  r"$C\in\mathcal C$", r"$C\in\boldsymbol{C}$")
f(205, "Lemme (7.5.1.1), 2nd paragraph: 'D un anneau local appartenant à C'", "bold italic C", "$\\mathcal C$", "font", None, "high",
  r"appartenant à $\mathcal C$", r"appartenant à $\boldsymbol{C}$")
f(205, "proof of (7.5.1.1): '((0, 17.1.8) et ...'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 17.1.8)", r"(\textbf{0}, 17.1.8)")
f(205, "proof of (7.5.1.1): '... et (0, 16.3.4))'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 16.3.4)", r"(\textbf{0}, 16.3.4)")
f(205, "proof of (7.5.1.1): 'Comme (D/tD)⊗_{C/tC}k = D⊗_C k, et que'", "formula in the running text", "set as a display \\[ ... \\]", "other", None, "high",
  r"Comme¶\[¶(D/tD)\otimes_{C/tC}k=D\otimes_C k,¶\]¶et que", r"Comme $(D/tD)\otimes_{C/tC}k=D\otimes_C k$, et que", INL)
f(205, "proof of (7.5.1.1): 'et que D/tD ∈ C'", "bold italic C", "$\\mathcal C$", "font", None, "high",
  r"$D/tD\in\mathcal C$", r"$D/tD\in\boldsymbol{C}$")
f(205, "proof of (7.5.1.1): 'par platitude (0_I, 6.3.4)'", "bold 0 in 0_I", "plain 0", "convention", 2, "high",
  r"(0$_{\mathrm I}$, 6.3.4)", r"(\textbf{0}$_{\mathrm I}$, 6.3.4)")
f(205, "end of the proof of (7.5.1): 'en prenant pour C la catégorie'", "bold italic C", "$\\mathcal C$", "font", None, "high",
  r"pour $\mathcal C$ la catégorie", r"pour $\boldsymbol{C}$ la catégorie")
f(205, "Corollaire (7.5.2), after the list: 'Soit d'autre part R(C) une propriété'", "starts a new indented paragraph", "\\end{enumerate} followed directly by the text (no indent)", "other", None, "medium",
  r"\end{enumerate}¶Soit d'autre part", r"\end{enumerate}¶¶Soit d'autre part", "Paragraph after the list, indented as printed (same form as the pp. 150-152 fixes).")
f(205, "Corollaire (7.5.2): '(R_II) (7.3.10), (R_III) (7.3.18) et (R_IV) (7.5.1)'", "the three references upright, 'et' italic (enlarged crop)", "references italic inside the corollary", "convention", 6, "high",
  r"(7.3.10), $(\mathrm R_{\mathrm{III}})$¶(7.3.18) et $(\mathrm R_{\mathrm{IV}})$ (7.5.1)",
  r"\textup{(7.3.10)}, $(\mathrm R_{\mathrm{III}})$¶\textup{(7.3.18)} et $(\mathrm R_{\mathrm{IV}})$ \textup{(7.5.1)}")
f(205, "Corollaire (7.5.2): 'Enfin, soit R'(C) une propriété vérifiant la condition suivante :'", "new indented paragraph (the line before ends short after '(7.5.1).')", "same paragraph", "other", None, "high",
  r". Enfin, soit", r".¶¶Enfin, soit", "Independent of the preceding edit.")
f(205, "Corollaire (7.5.2), after (R_V): 'Supposons que le morphisme canonique'", "new indented paragraph", "\\end{quote} followed directly by the text (no indent)", "other", None, "medium",
  r"\end{quote}¶Supposons que", r"\end{quote}¶¶Supposons que")
f(205, "Corollaire (7.5.2): '... à partir de R dans (7.5.0).'", "reference upright (enlarged crop)", "italic", "convention", 6, "high",
  r"dans¶(7.5.0).", r"dans¶\textup{(7.5.0)}.")
f(205, "Corollaire (7.5.2): 'et supposons que la propriété P(Spec(B^⊗_A^ k), k) soit vraie'", "formula in the running text", "display", "other", None, "high",
  r"\[¶\boldsymbol P(\operatorname{Spec}(\widehat B¶\otimes_{\widehat A}k),k)¶\]",
  r"$\boldsymbol P(\operatorname{Spec}(\widehat B¶\otimes_{\widehat A}k),k)$", INL)
f(205, "Corollaire (7.5.2): 'la propriété P(f^{-1}(x), k(x)) est vraie'", "bold italic k in k(x)", "k(x)", "convention", 1, "high",
  r"k(x))$ est vraie", r"\boldsymbol{k}(x))$ est vraie")
f(205, "Corollaire (7.5.2), end: '(autrement dit, f est un P-morphisme)'", "'(autrement dit,' and 'est un' upright, '-morphisme' italic (enlarged crop)", "all italic", "convention", 6, "high",
  r"(autrement dit, $f$ est un¶$\boldsymbol P$-morphisme)", r"\textup{(autrement dit,} $f$ \textup{est un}¶$\boldsymbol P$-morphisme)")
f(205, "proof of (7.5.2), part I) heading", "'I)' upright, 'Réduction ... générique.' italic (enlarged crop)", "\\emph{I) Réduction ...}: I) italic", "italics", None, "high",
  r"\emph{I) Réduction", r"I) \emph{Réduction", "Proof-part labels are printed upright (GLOBAL_ISSUES 51).")
f(205, "proof of (7.5.2) I): 'seulement un anneau semi-local intègre'", "'semi-local' italic (enlarged crop)", "upright", "italics", None, "high",
  r"anneau semi-local intègre", r"anneau \emph{semi-local} intègre")
f(205, "proof of (7.5.2) I): 'les anneaux locaux de Spec(B'_{n'}⊗_{A'_{m'}}K') possèdent'", "formula in the running text", "display", "other", None, "high",
  r"\[¶\operatorname{Spec}(B'_{\mathfrak n'}¶\otimes_{A'_{\mathfrak m'}}K')¶\]",
  r"$\operatorname{Spec}(B'_{\mathfrak n'}¶\otimes_{A'_{\mathfrak m'}}K')$", INL)
f(205, "proof of (7.5.2) I): 'la propriété P(Spec(B^'_{n'}⊗_{A^'_{m'}}k'), k') est vraie'", "formula in the running text", "display", "other", None, "high",
  r"\[¶\boldsymbol P(\operatorname{Spec}(\widehat{B'_{\mathfrak n'}}¶\otimes_{\widehat{A'_{\mathfrak m'}}}k'),k')¶\]",
  r"$\boldsymbol P(\operatorname{Spec}(\widehat{B'_{\mathfrak n'}}¶\otimes_{\widehat{A'_{\mathfrak m'}}}k'),k')$", INL + " Apply before the two hat edits that follow.")
f(205, "same formula: B^'_{n'}", "hat over B only, prime and subscript outside", "\\widehat{B'_{\\mathfrak n'}}", "formula", None, "high",
  r"\widehat{B'_{\mathfrak n'}}", r"\widehat{B}'_{\mathfrak n'}", HAT)
f(205, "same formula: subscript A^'_{m'}", "hat over A only", "\\widehat{A'_{\\mathfrak m'}}", "formula", None, "high",
  r"\widehat{A'_{\mathfrak m'}}", r"\widehat{A}'_{\mathfrak m'}", HAT)
f(205, "proof of (7.5.2) I): 'composants de A^' = A^⊗_A A''", "hat over A only, prime outside", "\\widehat{A'}", "formula", None, "high",
  r"$\widehat{A'}=\widehat A\otimes_A A'$", r"$\widehat{A}'=\widehat A\otimes_A A'$", HAT)
f(205, "proof of (7.5.2) I): 'B^' = B^⊗_B B' = B^⊗_A A' = B^⊗_A^ A^'; le raisonnement'", "formula in the running text, semicolon after it", "display with the semicolon inside", "other", None, "high",
  r"\[¶\widehat{B'}=\widehat B\otimes_B B'¶=\widehat B\otimes_A A'¶=\widehat B\otimes_{\widehat A}\widehat{A'};¶\]",
  r"$\widehat{B'}=\widehat B\otimes_B B'¶=\widehat B\otimes_A A'¶=\widehat B\otimes_{\widehat A}\widehat{A'}$;", INL + " Apply before the two hat edits that follow.")
f(205, "same formula: B^'", "hat over B only, prime outside", "\\widehat{B'}", "formula", None, "high",
  r"\widehat{B'}=", r"\widehat{B}'=", HAT)
f(205, "same formula, end: A^'", "hat over A only, prime outside", "\\widehat{A'}", "formula", None, "high",
  r"\otimes_{\widehat A}\widehat{A'}", r"\otimes_{\widehat A}\widehat{A}'", HAT)
f(205, "proof of (7.5.2): 'A est en outre supposé intègre'", "'intègre' italic", "upright", "italics", None, "high",
  r"supposé intègre", r"supposé \emph{intègre}")
f(205, "proof of (7.5.2): 'les anneaux locaux de Spec(B⊗_A K) possèdent la propriété R'", "'les anneaux locaux de' and 'possèdent la propriété' italic", "upright", "italics", None, "high",
  r"de $A$, les anneaux locaux de¶$\operatorname{Spec}(B\otimes_A K)$ possèdent la propriété",
  r"de $A$, \emph{les anneaux locaux de}¶$\operatorname{Spec}(B\otimes_A K)$ \emph{possèdent la propriété}")
f(205, "proof of (7.5.2), part II) heading", "'II)' upright, 'Réduction ... complets.' italic (enlarged crop)", "\\emph{II) Réduction ...}: II) italic", "italics", None, "high",
  r"\emph{II) Réduction", r"II) \emph{Réduction", "GLOBAL_ISSUES 51.")
f(205, "proof of (7.5.2) II): 'que le morphisme ^aφ^ : Spec(B^) → Spec(A^) est un P-morphisme'", "formula in the running text", "display", "other", None, "high",
  r"\[¶{}^a\widehat\varphi:\operatorname{Spec}(\widehat B)¶\to\operatorname{Spec}(\widehat A)¶\]",
  r"${}^a\widehat\varphi:\operatorname{Spec}(\widehat B)¶\to\operatorname{Spec}(\widehat A)$", INL + " The \\enlargethispage before it is left as it is.")
f(205, "Exemples (7.5.3), label (i)", "(i) upright", "\\item[\\emph{(i)}]: the examples body is upright, so \\emph sets the label italic", "italics", None, "high",
  r"\item[\emph{(i)}] (aussi notée", r"\item[(i)] (aussi notée", "The examples environment has a roman body; the printed labels (i)-(viii) are upright.")
f(205, "Exemples (7.5.3), l. 1: '(C étant un anneau local noethérien) :'", "'anneau local noethérien' italic (enlarged crop)", "upright", "italics", None, "high",
  r"étant un anneau¶local noethérien)", r"étant un \emph{anneau¶local noethérien})")

# ---------------- page 206 ----------------
for lab, old in (("ii", r"\item[\emph{(ii)}] (aussi notée"), ("iii", r"\item[\emph{(iii)}] $C$")):
    f(206, "Exemples (7.5.3), label (%s)" % lab, "(%s) upright (enlarged crop)" % lab, "\\item[\\emph{(%s)}] in the roman examples body: italic" % lab, "italics", None, "high",
      old, old.replace(r"\emph{(%s)}" % lab, "(%s)" % lab), "As label (i) on p. 205.")
f(206, "Exemples (7.5.3) (iii): 'C est un anneau de Cohen-Macaulay.'", "hyphen", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
  r"anneau de Cohen--Macaulay.", r"anneau de Cohen-Macaulay.", "ega4-2-fr.tex has 42 'Cohen--Macaulay' against 57 'Cohen-Macaulay'.")
for lab, old in (("iv", r"\item[\emph{(iv)}] $C$"), ("v", r"\item[\emph{(v)}]"), ("vi", r"\item[\emph{(vi)}]"),
                 ("vii", r"\item[\emph{(vii)}]"), ("viii", r"\item[\emph{(viii)}]")):
    f(206, "Exemples (7.5.3), label (%s)" % lab, "(%s) upright" % lab, "\\item[\\emph{(%s)}] in the roman examples body: italic" % lab, "italics", None, "high",
      old, old.replace(r"\emph{(%s)}" % lab, "(%s)" % lab), "As label (i) on p. 205.")
f(206, "Exemples (7.5.3), after the list: 'Toutes ces propriétés vérifient (R_III)'", "new indented paragraph", "\\end{enumerate} followed directly by the text", "other", None, "medium",
  r"\end{enumerate}¶Toutes ces propriétés", r"\end{enumerate}¶¶Toutes ces propriétés", "Paragraph after the list, indented as printed.")
f(206, "'pour (i), cela résulte de (0, 16.4.10, (ii))'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 16.4.10, (ii))", r"(\textbf{0}, 16.4.10, (ii))")
f(206, "'c'est un cas particulier de (0, 17.1.8)'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 17.1.8)", r"(\textbf{0}, 17.1.8)")
f(206, "'d'être un anneau de Cohen-Macaulay, en vertu de (6.3.2)'", "hyphen", "Cohen--Macaulay", "punctuation", None, "high",
  r"anneau de Cohen--Macaulay, en vertu", r"anneau de Cohen-Macaulay, en vertu")
f(206, "'la propriété d'être régulier : il suffit'", "'régulier' italic (enlarged crop)", "upright", "italics", None, "high",
  r"d'être régulier :", r"d'être \emph{régulier} :")
f(206, "'en prenant pour C la catégorie de tous les anneaux locaux noethériens'", "bold italic C", "$\\mathcal C$", "font", None, "high",
  r"pour $\mathcal C$ la catégorie", r"pour $\boldsymbol{C}$ la catégorie", CAT)
f(206, "'que les fibres formelles de A sont géométriquement régulières (cf. (7.8.2))'", "'les fibres formelles de' and 'sont géométriquement régulières' italic, A roman", "upright", "italics", None, "high",
  r"que les fibres formelles de $A$ sont géométriquement¶régulières", r"que \emph{les fibres formelles de} $A$ \emph{sont géométriquement¶régulières}")
f(206, "Remarques (7.5.4), label (i)", "(i) upright in the roman remark", "\\item[\\emph{(i)}]: italic once the remark body is roman", "italics", None, "medium",
  r"\item[\emph{(i)}] Il serait", r"\item[(i)] Il serait", REM + " Applies to all 25 \\item[\\emph{..}] labels inside remark(s) environments of ega4-2.")
f(206, "Remarques (7.5.4) (i): 'une A-algèbre formellement lisse (0, 19.3.1)'", "'formellement lisse' italic", "no emphasis", "italics", None, "high",
  r"$A$-algèbre¶formellement lisse", r"$A$-algèbre¶\emph{formellement lisse}", REM)
f(206, "Remarques (7.5.4) (i): '(0, 19.3.1)'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 19.3.1)", r"(\textbf{0}, 19.3.1)")
f(206, "Remarques (7.5.4) (i): '(0, 19.7.1)'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 19.7.1)", r"(\textbf{0}, 19.7.1)")
f(206, "Remarques (7.5.4) (i): 'est une extension finie de k, d'après (7.5.1)'", "'finie' italic", "no emphasis", "italics", None, "high",
  r"une extension finie de $k$, d'après", r"une extension \emph{finie} de $k$, d'après", REM)
f(206, "Remarques (7.5.4) (i): 'une extension de type fini de k'", "'de type fini' italic", "no emphasis", "italics", None, "high",
  r"une extension de type fini de¶$k$", r"une extension \emph{de type fini} de¶$k$", REM)
f(206, "Remarques (7.5.4) (i), end: 'égal à la clôture séparable de k'", "'clôture séparable' italic", "no emphasis", "italics", None, "high",
  r"clôture séparable de $k$", r"\emph{clôture séparable} de $k$", REM)
f(206, "Remarques (7.5.4), label (ii)", "(ii) upright", "\\item[\\emph{(ii)}]: italic once the remark body is roman", "italics", None, "medium",
  r"\item[\emph{(ii)}] On pourrait", r"\item[(ii)] On pourrait", REM)
f(206, "Remarques (7.5.4) (ii): 'propriétés de (M⊗_A N)_y⊗_{O_x} k(y), où y parcourt'", "formula in the running text", "display", "other", None, "high",
  r"\[¶(M\otimes_A N)_y\otimes_{\mathscr O_x}k(y),¶\]", r"$(M\otimes_A N)_y\otimes_{\mathscr O_x}k(y)$,", INL + " Apply before the convention-1 edit that follows.")
f(206, "same formula: k(y)", "bold italic k", "k(y)", "convention", 1, "high",
  r"\otimes_{\mathscr O_x}k(y)", r"\otimes_{\mathscr O_x}\boldsymbol{k}(y)")
f(206, "Remarques (7.5.4), label (iii)", "(iii) upright", "\\item[\\emph{(iii)}]: italic once the remark body is roman", "italics", None, "medium",
  r"\item[\emph{(iii)}] Lorsque", r"\item[(iii)] Lorsque", REM)
f(206, "Remarques (7.5.4) (iii): 'des propriétés R(A) et P(Spec(B^⊗ k), k) on déduit R(B)'", "formula in the running text", "display", "other", None, "high",
  r"\[¶\boldsymbol P(\operatorname{Spec}(\widehat B¶\otimes_{\widehat A}k),k)¶\]",
  r"$\boldsymbol P(\operatorname{Spec}(\widehat B¶\otimes_{\widehat A}k),k)$",
  INL + " The subscript A^ of ⊗ has not printed (a trace remains): physical defect, TeX kept.")
f(206, "Remarques (7.5.4) (iii): 'faisant de B un A-module plat.'", "'plat' italic", "no emphasis", "italics", None, "high",
  r"-module plat. Supposons", r"-module \emph{plat}. Supposons", REM + " Listed before the misprint edit on the same words.")
f(206, "Remarques (7.5.4) (iii): 'faisant de B un A-module plat', the A", "bold roman A (wrong fount): stroke run 6.35 px against 4.2-4.8 px for the other roman A of the page (median of 142 A on pp. 205-209: 4.84); counter filled; 8x crop",
  "$A$ (silent correction)", "misprint_in_print", None, "high",
  r"faisant de $B$ un $A$-module", r"faisant de $B$ un $\mathbf{A}$-module",
  "Wrong-fount letter in the print (GLOBAL_ISSUES 29); the TeX silently corrects it; the fix reproduces it in the diplomatic text. Correct reading: plain A.",
  corrected=r"faisant de $B$ un $A$-module")
f(206, "Remarques (7.5.4) (iii): 'Supposons que A soit complet, intègre et géométriquement unibranche'", "'complet', 'intègre', 'géométriquement unibranche' italic, 'et' roman", "no emphasis", "italics", None, "high",
  r"soit complet, intègre et géométriquement unibranche", r"soit \emph{complet}, \emph{intègre} et \emph{géométriquement unibranche}", REM)
f(206, "Remarques (7.5.4) (iii): '(où k est le corps résiduel de A)', the A", "bold roman A (wrong fount): stroke run 6.10 px against 4.2-4.8 px; 8x crop",
  "$A$ (silent correction)", "misprint_in_print", None, "high",
  r"corps résiduel de $A$) soit", r"corps résiduel de $\mathbf{A}$) soit",
  "Wrong-fount letter in the print (GLOBAL_ISSUES 29); the TeX silently corrects it. Correct reading: plain A.",
  corrected=r"corps résiduel de $A$) soit")
f(206, "Remarques (7.5.4) (iii): 'soit géométriquement localement intègre;'", "italic", "no emphasis", "italics", None, "high",
  r"géométriquement localement intègre;", r"\emph{géométriquement localement intègre};", REM)
f(206, "Remarques (7.5.4) (iii): 'alors est-il vrai que B soit intègre ?'", "'intègre' italic", "no emphasis", "italics", None, "high",
  r"que $B$ soit intègre ?", r"que $B$ soit \emph{intègre} ?", REM)
f(206, "Remarques (7.5.4) (iii): 'Spec(B⊗_A k) est géométriquement normale (car'", "'géométriquement normale' italic", "no emphasis", "italics", None, "high",
  r"est géométriquement normale (car", r"est \emph{géométriquement normale} (car", REM)
f(206, "Remarques (7.5.4), label (iv)", "(iv) upright", "\\item[\\emph{(iv)}]: italic once the remark body is roman", "italics", None, "medium",
  r"\item[\emph{(iv)}] Considérons", r"\item[(iv)] Considérons", REM)

# ---------------- page 207 ----------------
f(207, "l. 1: 'à l'étude des produits tensoriels complétés A⊗^_k B'", "'produits tensoriels complétés' italic", "upright", "italics", None, "high",
  r"des¶produits tensoriels complétés", r"des¶\emph{produits tensoriels complétés}")
f(207, "Lemme (7.5.5): 'A⊗^_k B (0_I, 7.7.5). Alors :'", "(0_I, 7.7.5): bold 0, reference upright", "plain 0, italic inside the lemma", "convention", 2, "high",
  r"(0$_{\mathrm I}$, 7.7.5)", r"\textup{(\textbf{0}$_{\mathrm I}$, 7.7.5)}",
  "One edit for this finding and the next (convention 6): bold numeral and the upright reference together.")
f(207, "Lemme (7.5.5): '(0_I, 7.7.5)'", "reference upright", "italic", "convention", 6, "high", None, None,
  "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
f(207, "proof of (7.5.5): 'Les propriétés (i), (iii) et la première assertion de (ii) ...' (edit 1 of 2)", "roman paragraph after the italic statement (the print has no proof heading)", "the paragraph stands inside \\begin{lemma} (italic) up to 'extensions finies de B/n.'", "italics", None, "high",
  r"\end{enumerate}¶Les propriétés (i), (iii)", r"\end{enumerate}¶\end{lemma}¶¶Les propriétés (i), (iii)",
  "The environment closes too late. Apply together with the next entry (both or neither).")
f(207, "proof of (7.5.5), end: 'extensions finies de B/n.' (edit 2 of 2)", "-", "\\end{lemma} after the proof", "italics", None, "high",
  r"extensions finies de $B/\mathfrak n$.¶\end{lemma}", r"extensions finies de $B/\mathfrak n$.",
  "Removes the old \\end{lemma}; apply together with the previous entry.")
f(207, "proof of (7.5.5): 'cas particuliers de (0, 19.7.1.2)'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 19.7.1.2)", r"(\textbf{0}, 19.7.1.2)")
f(207, "proof of (7.5.5): 'pour tout h > 0, C/m^hC = (A/m^h)⊗_k B est un B-module plat'", "formula in the running text", "display", "other", None, "high",
  r"\[¶C/\mathfrak m^hC=(A/\mathfrak m^h)\otimes_k B¶\]", r"$C/\mathfrak m^hC=(A/\mathfrak m^h)\otimes_k B$", INL)
f(207, "proof of (7.5.5): 'd'appliquer (0_III, 10.2.6)'", "bold 0 in 0_III", "plain 0", "convention", 2, "high",
  r"(0$_{\mathrm{III}}$, 10.2.6)", r"(\textbf{0}$_{\mathrm{III}}$, 10.2.6)")
f(207, "Proposition (7.5.6): '(la propriété P étant définie à partir de R par (7.5.0))'", "the whole parenthesis upright (roman), P and R bold italic", "italic inside the proposition", "convention", 6, "high",
  r"(la propriété $\boldsymbol P$ étant définie à¶partir de $\boldsymbol R$ par (7.5.0))",
  r"\textup{(la propriété $\boldsymbol P$ étant définie à¶partir de $\boldsymbol R$ par (7.5.0))}")
f(207, "Proposition (7.5.6): '(ce qui signifie que ... R(B'_i) est vraie)'", "the whole parenthesis upright (roman)", "italic inside the proposition", "convention", 6, "high",
  r"(ce qui signifie que¶pour toute extension finie $k'$ de $k$ et pour chacun des anneaux locaux¶complets $B_i$ dont le composé direct est $B\otimes_k k'$,¶$\boldsymbol R(B_i)$ est vraie)",
  r"\textup{(ce qui signifie que¶pour toute extension finie $k'$ de $k$ et pour chacun des anneaux locaux¶complets $B_i$ dont le composé direct est $B\otimes_k k'$,¶$\boldsymbol R(B_i)$ est vraie)}",
  "Apply before the two B'_i edits that follow (their 'old' lies inside this one).")
f(207, "Proposition (7.5.6): 'anneaux locaux complets B'_i dont le composé direct est B⊗_k k''", "B'_i with a prime (8x crop)", "$B_i$", "formula", None, "high",
  r"complets $B_i$ dont", r"complets $B'_i$ dont", "The components of B⊗_k k' are named B'_i in the print.")
f(207, "Proposition (7.5.6): 'R(B'_i) est vraie'", "B'_i, prime faint but present (8x crop)", "$B_i$", "formula", None, "medium",
  r"\boldsymbol R(B_i)$", r"\boldsymbol R(B'_i)$", "Same notation as the preceding finding.")
f(207, "proof of (7.5.6): 'la propriété P(Spec(C⊗_A(A/m)), A/m) est vraie'", "formula in the running text", "display", "other", None, "high",
  r"\[¶\boldsymbol P(\operatorname{Spec}(C\otimes_A(A/\mathfrak m)),A/\mathfrak m)¶\]",
  r"$\boldsymbol P(\operatorname{Spec}(C\otimes_A(A/\mathfrak m)),A/\mathfrak m)$", INL)
f(207, "proof of (7.5.6): 'car C/mC = (A/m)⊗_k B', the subscript k", "bold italic k (wrong fount; the base field is a light italic k elsewhere, e.g. B⊗_k k' on the same page): ink 139 px, stroke run 4.34 px against 117-118 px, 3.3-3.6 px; 8x crop",
  "\\otimes_k (silent correction)", "misprint_in_print", None, "medium",
  r"(A/\mathfrak m)\otimes_kB$, et l'assertion", r"(A/\mathfrak m)\otimes_{\boldsymbol{k}}B$, et l'assertion",
  "Wrong-fount letter in the print (GLOBAL_ISSUES 29); the TeX silently corrects it. Correct reading: light italic k.",
  corrected=r"(A/\mathfrak m)\otimes_kB$, et l'assertion")
f(207, "proof of (7.5.6): 'A/m est une extension finie de k'", "'finie' italic", "upright", "italics", None, "high",
  r"extension finie de $k$. Toutes", r"extension \emph{finie} de $k$. Toutes")
f(207, "proof of (7.5.6): 'sont donc des P-morphismes;'", "'morphismes' italic", "upright", "italics", None, "high",
  r"$\boldsymbol P$-morphismes;", r"$\boldsymbol P$-\emph{morphismes};")
f(207, "Corollaire (7.5.7): 'parfait (resp. algébriquement clos)'", "'(resp.' upright, 'algébriquement clos' italic", "all italic", "convention", 6, "high",
  r"(resp. algébriquement clos)", r"\textup{(resp.} algébriquement clos)")
f(207, "Corollaire (7.5.7): 'réduits (resp. intègres)'", "'(resp.' upright", "all italic", "convention", 6, "high",
  r"(resp. intègres)", r"\textup{(resp.} intègres)")
f(207, "Corollaire (7.5.7): 'est réduit (resp. intègre).'", "'(resp.' upright", "all italic", "convention", 6, "high",
  r"(resp. intègre)", r"\textup{(resp.} intègre)")
f(207, "proof of (7.5.7) I): 'ramené au cas où A et B sont intègres'", "'intègres' italic", "upright", "italics", None, "high",
  r"sont intègres. Soient alors", r"sont \emph{intègres}. Soient alors")
f(207, "proof of (7.5.7) I): 'finitude de Nagata (0, 23.1.6)'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 23.1.6)", r"(\textbf{0}, 23.1.6)")
f(207, "Lemme (7.5.7.1): 'M⊗^_k B (0_I, 7.7.1) s'identifie'", "(0_I, 7.7.1): bold 0, reference upright", "plain 0, italic inside the lemma", "convention", 2, "high",
  r"(0$_{\mathrm I}$, 7.7.1)", r"\textup{(\textbf{0}$_{\mathrm I}$, 7.7.1)}",
  "One edit for this finding and the next (convention 6).")
f(207, "Lemme (7.5.7.1): '(0_I, 7.7.1)'", "reference upright", "italic", "convention", 6, "high", None, None,
  "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
f(207, "proof of (7.5.7.1): '((7.5.5) et (0_I, 7.7.8))'", "bold 0 in 0_I", "plain 0", "convention", 2, "high",
  r"(0$_{\mathrm I}$, 7.7.8)", r"(\textbf{0}$_{\mathrm I}$, 7.7.8)")
f(207, "last display: 'φ^ : M⊗^_k B → M⊗_A(A⊗^_k B)'", "no full stop after the display (enlarged crop; p. 208 begins 'Il est immédiat')", "full stop at the end of the display", "punctuation", None, "high",
  r"M\otimes_A(A\widehat\otimes_kB).¶\]", r"M\otimes_A(A\widehat\otimes_kB)¶\]", "GLOBAL_ISSUES 73 (punctuation after displays).")

# ---------------- page 208 ----------------
f(208, "'(la première ... et de (0_III, 13.2.2))'", "bold 0 in 0_III", "plain 0", "convention", 2, "high",
  r"(0$_{\mathrm{III}}$, 13.2.2)", r"(\textbf{0}$_{\mathrm{III}}$, 13.2.2)")
f(208, "proof of (7.5.7) I), end: 'que A et B sont intégralement clos;'", "'intégralement clos' italic", "upright", "italics", None, "high",
  r"sont intégralement¶clos; comme", r"sont \emph{intégralement¶clos}; comme")
f(208, "same: 'comme en outre k est supposé parfait,'", "'parfait' italic", "upright", "italics", None, "high",
  r"supposé parfait,", r"supposé \emph{parfait},")
f(208, "same: 'Spec(A) et Spec(B) sont géométriquement normaux sur k'", "'géométriquement normaux' italic", "upright", "italics", None, "high",
  r"sont géométriquement normaux sur", r"sont \emph{géométriquement normaux} sur")
f(208, "same: 'en vertu de (6.7.7, b))'", "'b)' italic (letter and first parenthesis), outer parenthesis upright (enlarged crop)", "upright", "italics", None, "high",
  r"(6.7.7, b))", r"(6.7.7, \emph{b)})")
f(208, "proof of (7.5.7) II): 'au cas où A et B sont intégralement clos;'", "'intégralement clos' italic", "upright", "italics", None, "high",
  r"sont intégralement clos; il résulte", r"sont \emph{intégralement clos}; il résulte")
f(208, "II): 'Spec(A⊗^_k B) est normal, donc'", "'normal' italic", "upright", "italics", None, "high",
  r"est normal, donc", r"est \emph{normal}, donc")
f(208, "II): 'est un anneau local; il suffit'", "'local' italic", "upright", "italics", None, "high",
  r"anneau local; il suffit", r"anneau \emph{local}; il suffit")
f(208, "II): '(voir démonstration de (0, 19.7.1.2))'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 19.7.1.2)", r"(\textbf{0}, 19.7.1.2)")
f(208, "Remarque (7.5.8): 'Spec(A) ou Spec(B) est géométriquement intègre sur k'", "'géométriquement intègre' italic", "no emphasis", "italics", None, "high",
  r"est géométriquement¶intègre sur $k$, ou", r"est \emph{géométriquement¶intègre} sur $k$, ou", REM)
f(208, "Remarque (7.5.8): 'k[[T_1, ..., T_n]], tel que le corps des fractions K de A soit séparable'", "'tel que' (enlarged crop)", "'et que'", "word", None, "high",
  r"]]$, et que le corps", r"]]$, tel que le corps")
f(208, "Remarque (7.5.8): 'soit séparable sur le corps des fractions K_0'", "'séparable' italic", "no emphasis", "italics", None, "high",
  r"séparable sur le corps des fractions $K_0$", r"\emph{séparable} sur le corps des fractions $K_0$", REM)
f(208, "heading 7.6", "'7.6. Applications : I. Anneaux japonais locaux.' with a final full stop", "title without the full stop", "punctuation", None, "high",
  r"\subsection{Applications : I. Anneaux japonais locaux}", r"\subsection{Applications : I. Anneaux japonais locaux.}", "GLOBAL_ISSUES 43/58.")
f(208, "Proposition (7.6.1): 'et son complété A^' est isomorphe'", "hat over A only, prime outside", "\\widehat{A'}", "formula", None, "high",
  r"$\widehat{A'}$ est isomorphe", r"$\widehat{A}'$ est isomorphe", HAT)
f(208, "proof of (7.6.1): 'Les fibres formelles de A sont a fortiori géométriquement réduites'", "'a fortiori' italic", "upright", "italics", None, "high",
  r"sont a fortiori", r"sont \emph{a fortiori}")
f(208, "proof of (7.6.1): 'il résulte de (0, 23.1.7, (i))'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 23.1.7, (i))", r"(\textbf{0}, 23.1.7, (i))")
f(208, "proof of (7.6.1): 'comme A' est composée directe des B'_i'", "'composée directe' (enlarged crop)", "'composé direct'", "word", None, "high",
  r"composé direct des $B'_i$", r"composée directe des $B'_i$")
f(208, "proof of (7.6.1): '(II, 6.3.8)'", "bold II", "plain II", "convention", 2, "high",
  r"(II, 6.3.8)", r"(\textbf{II}, 6.3.8)")
f(208, "proof of (7.6.1): 'on sait que le complété A^' de A''", "hat over A only, prime outside", "\\widehat{A'}", "formula", None, "high",
  r"le complété $\widehat{A'}$ de $A'$", r"le complété $\widehat{A}'$ de $A'$", HAT)
f(208, "proof of (7.6.1): 'des complétés A^'_{m_j} des A'_{m_j}'", "hat over A only, prime and subscript outside", "\\widehat{A'_{\\mathfrak m_j}}", "formula", None, "high",
  r"$\widehat{A'_{\mathfrak m_j}}$ des", r"$\widehat{A}'_{\mathfrak m_j}$ des", HAT)
f(208, "last line: '... des A'_{m_j} (Bourbaki,' / p. 209 'Alg. comm., chap. III ...'", "the sentence runs on to p. 209 without a paragraph break", "blank line before \\oldpage[IV-2]{209}", "other", None, "high",
  r"(Bourbaki,¶¶", r"(Bourbaki,¶",
  "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 209 edit that removes the blank line after \\oldpage[IV-2]{209}.")

# ---------------- page 209 ----------------
f(209, "top of the page: 'Alg. comm., chap. III, § 2, n° 13, ...' continues '(Bourbaki,' of p. 208", "no paragraph break", "blank line after \\oldpage[IV-2]{209}", "other", None, "high",
  r"\oldpage[IV-2]{209}¶¶\emph{Alg. comm.}", r"\oldpage[IV-2]{209}¶\emph{Alg. comm.}",
  "Apply together with the p. 208 edit that removes the blank line before the marker.")
f(209, "l. 4: 'que Spec(A^'_{m_j}) est normal pour tout j'", "hat over A only, prime and subscript outside (enlarged crop)", "\\widehat{A'_{\\mathfrak m_j}}", "formula", None, "high",
  r"\operatorname{Spec}(\widehat{A'_{\mathfrak m_j}})", r"\operatorname{Spec}(\widehat{A}'_{\mathfrak m_j})", HAT)
f(209, "l. 4: 'donc aussi Spec(A^')'", "hat over A only", "\\widehat{A'}", "formula", None, "high",
  r"donc aussi $\operatorname{Spec}(\widehat{A'})$", r"donc aussi $\operatorname{Spec}(\widehat{A}')$", HAT)
f(209, "l. 6: 'A^' s'identifie à A'⊗_A A^'", "hat over A only", "\\widehat{A'}", "formula", None, "high",
  r"$\widehat{A'}$ s'identifie", r"$\widehat{A}'$ s'identifie", HAT)
f(209, "l. 8: 'A^' contient A^'", "hat over A only", "\\widehat{A'}", "formula", None, "high",
  r"$\widehat{A'}$ contient", r"$\widehat{A}'$ contient", HAT)
f(209, "l. 9: 'aussi A^-régulier (0_I, 6.3.4)'", "bold 0 in 0_I", "plain 0", "convention", 2, "high",
  r"(0$_{\mathrm I}$, 6.3.4)", r"(\textbf{0}$_{\mathrm I}$, 6.3.4)")
f(209, "l. 11: '(Bourbaki, Alg. comm., chap. II, § 2, n° 1, Remarque 7)'", "'Remarque' italic", "upright", "italics", None, "high",
  r"Remarque 7)", r"\emph{Remarque} 7)")
f(209, "l. 11: 'Comme Spec(A^') est normal'", "hat over A only", "\\widehat{A'}", "formula", None, "high",
  r"Comme¶$\operatorname{Spec}(\widehat{A'})$ est normal", r"Comme¶$\operatorname{Spec}(\widehat{A}')$ est normal", HAT)
f(209, "l. 11: 'et que A^' est un A^-module'", "hat over A only", "\\widehat{A'}", "formula", None, "high",
  r"et que $\widehat{A'}$ est un", r"et que $\widehat{A}'$ est un", HAT)
f(209, "l. 12: 'de type fini, A^' est bien la fermeture intégrale'", "hat over A only", "\\widehat{A'}", "formula", None, "high",
  r"fini, $\widehat{A'}$ est bien", r"fini, $\widehat{A}'$ est bien", HAT)
f(209, "Corollaire (7.6.2): 'Sous les hypothèses de (7.6.1), il y a'", "reference upright (enlarged crop)", "italic", "convention", 6, "high",
  r"Sous les hypothèses de (7.6.1), il y a", r"Sous les hypothèses de \textup{(7.6.1)}, il y a")
f(209, "Corollaire (7.6.2): '(autrement dit, l'ensemble des points de Spec(A') au-dessus du point fermé de A)'", "the whole parenthesis upright (roman)", "italic", "convention", 6, "high",
  r"(autrement dit,¶l'ensemble des points de $\operatorname{Spec}(A')$ au-dessus du point fermé de¶$A$)",
  r"\textup{(autrement dit,¶l'ensemble des points de $\operatorname{Spec}(A')$ au-dessus du point fermé de¶$A$)}")
f(209, "Corollaire (7.6.2): '(autrement dit, l'ensemble des points maximaux de Spec(A^))'", "the whole parenthesis upright (roman)", "italic", "convention", 6, "high",
  r"(autrement dit, l'ensemble des points maximaux de¶$\operatorname{Spec}(\widehat A)$)",
  r"\textup{(autrement dit, l'ensemble des points maximaux de¶$\operatorname{Spec}(\widehat A)$)}")
f(209, "Corollaire (7.6.2): 'le complété A^'_{m_j} de A'_{m_j}'", "hat over A only, prime and subscript outside", "\\widehat{A'_{\\mathfrak m_j}}", "formula", None, "high",
  r"$\widehat{A'_{\mathfrak m_j}}$ de", r"$\widehat{A}'_{\mathfrak m_j}$ de", HAT)
f(209, "proof of (7.6.2): 'anneaux locaux complets (0, 23.1.6)'", "bold 0", "plain 0", "convention", 2, "high",
  r"(0, 23.1.6)", r"(\textbf{0}, 23.1.6)")
f(209, "Corollaire (7.6.3): 'Sous les hypothèses de (7.6.1), pour que'", "reference upright (enlarged crop)", "italic", "convention", 6, "high",
  r"Sous les hypothèses de (7.6.1), pour que", r"Sous les hypothèses de \textup{(7.6.1)}, pour que")
f(209, "Théorème (7.6.4) title: '(Zariski-Nagata)'", "hyphen (enlarged crop)", "Zariski--Nagata (en dash)", "punctuation", None, "high",
  r"(Zariski--Nagata)", r"(Zariski-Nagata)", "The placement of the parenthesised title is the document-wide heading item; only the dash is a page fix.")
f(209, "Théorème (7.6.4) a''): '(autrement dit, pour tout anneau quotient intègre B de A, ..., la K-algèbre B^⊗_B K est séparable (4.6.2))'", "the whole parenthesis upright (roman)", "italic", "convention", 6, "high",
  r"(autrement dit, pour tout anneau quotient intègre $B$ de $A$, de corps des¶fractions $K$, la $K$-algèbre $\widehat B\otimes_BK$ est séparable (4.6.2))",
  r"\textup{(autrement dit, pour tout anneau quotient intègre $B$ de $A$, de corps des¶fractions $K$, la $K$-algèbre $\widehat B\otimes_BK$ est séparable (4.6.2))}")
f(209, "proof of (7.6.4): 'Pour montrer que a) entraîne a')'", "a) and a') italic, letters and parentheses (enlarged crop)", "$a)$, $a')$: italic letter, upright parenthesis", "italics", None, "medium",
  r"$a)$ entraîne $a')$", r"\emph{a)} entraîne \emph{a$'$)}", "Form of the labels in the TeX's \\item[\\emph{a$'$)}].")
f(209, "proof of (7.6.4): 'On a B^' = B^⊗_B B''", "hat over B only, prime outside (enlarged crop)", "\\widehat{B'}", "formula", None, "high",
  r"$\widehat{B'}=", r"$\widehat{B}'=", HAT)
f(209, "proof of (7.6.4): '((0_I, 7.3.3) et Bourbaki'", "bold 0 in 0_I", "plain 0", "convention", 2, "high",
  r"(0$_{\mathrm I}$, 7.3.3)", r"(\textbf{0}$_{\mathrm I}$, 7.3.3)")
f(209, "last line: '... n° 5, cor. 3 de' / p. 210 'la prop. 9), donc'", "the sentence runs on to p. 210", "blank line before \\oldpage[IV-2]{210}", "other", None, "high",
  r"cor. 3 de¶¶", r"cor. 3 de¶",
  "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 210 edit removing the blank line after \\oldpage[IV-2]{210} (page_210.tex, outside pp. 205-209).")

# ---------------- checks ----------------
ok = True
pages = {}
for p in sorted({x["page"] for x in F}):
    t = (run / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    t = t.split("\n", 1)[1]  # drop the '% from' line
    pages[p] = t
cur = dict(pages)
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    p, old, new = x["page"], x["fix"]["old"], x["fix"]["new"]
    n0 = pages[p].count(old)
    n1 = cur[p].count(old)
    if n0 != 1 or n1 != 1:
        ok = False
        print("PROBLEM", i, p, repr(old[:60]), "original", n0, "at its turn", n1)
    cur[p] = cur[p].replace(old, new, 1)
for p in cur:  # braces balance after all edits
    if cur[p].count("{") - cur[p].count("}") != pages[p].count("{") - pages[p].count("}"):
        ok = False
        print("BRACE BALANCE CHANGED on", p)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in sorted(pages):
    print(p, "normal %d / convention %d / misprint %d" % (cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")]))
print("total", len(F), "OK" if ok else "PROBLEMS")
