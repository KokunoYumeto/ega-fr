"""Build findings_190_194.json. TeX strings are raw strings; <NL> stands for a line break (LF)."""
import json

OUT = r"user\Documents\ega_scan_check_20261101\run_IV2\findings_190_194.json"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=""):
    F.append({
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": nl(old), "new": nl(new)},
        "note": note,
    })


# ---------------------------------------------------------------- page 189 (outside) / 190: page break
add(189, r"end of the p. 189 segment, before \oldpage[IV-2]{190} (proof of (7.2.4))",
    r"printed p. 189 ends '... donc on conclut de (5.10.10) que l'on a, dans Y',' (page_189_s4.png, last line); p. 190 continues the same sentence flush left: 'codim({y'}∩{x'}, {x'}) ⩾ 2.'",
    r"blank line between 'dans $Y'$,' and \oldpage[IV-2]{190}: paragraph break inside the sentence",
    "marker", None, "high",
    r"que l'on a, dans $Y'$,<NL><NL>", r"que l'on a, dans $Y'$,<NL>",
    r"OUTSIDE pages 190-194: 'old' lies in page_189.tex (checked unique there). Apply together with the next entry (blank line after the marker). The pp. 185-189 checker may report the same edit; a second application finds nothing.")
add(190, r"top of the page: \oldpage[IV-2]{190}",
    r"p. 190 begins mid-sentence, flush left: 'codim({y'}∩{x'}, {x'}) ⩾ 2. Comme y' est arbitraire ...', continuing '... que l'on a, dans Y',' of p. 189",
    r"\oldpage[IV-2]{190} followed by a blank line (and preceded by one): paragraph break the print does not have",
    "marker", None, "high",
    r"\oldpage[IV-2]{190}<NL><NL>$", r"\oldpage[IV-2]{190}<NL>$",
    r"The marker itself stands where p. 190 begins. Apply together with the p. 189 entry above (blank line before the marker, outside this segment).")

# ---------------------------------------------------------------- page 190: Théorème (7.2.5)
add(190, "Théorème (7.2.5), label a)", "label a) upright roman",
    r"\item[a)] comes out italic in the italic theorem", "convention", 6, "high",
    r"\item[a)]", r"\item[\textup{a)}]")
add(190, "Théorème (7.2.5) a): 'strictement équidimensionnel (7.2.1).'",
    "reference (7.2.1) upright inside the italic statement", "italic inside the theorem environment",
    "convention", 6, "high",
    r"équidimensionnel (7.2.1).", r"équidimensionnel \textup{(7.2.1)}.")
add(190, "Théorème (7.2.5), label b)", "label b) upright roman",
    r"\item[b)] comes out italic in the italic theorem", "convention", 6, "high",
    r"\item[b)]", r"\item[\textup{b)}]")
add(190, "Théorème (7.2.5) b): 'formellement caténaire (7.1.9)'",
    "reference (7.1.9) upright inside the italic statement", "italic inside the theorem environment",
    "convention", 6, "high",
    r"caténaire (7.1.9) et les fibres", r"caténaire \textup{(7.1.9)} et les fibres")
add(190, "Théorème (7.2.5) b): '(autrement dit, n'ont pas de cycle premier associé immergé).'",
    "'(autrement dit,' and the closing parenthesis roman; 'n'ont pas ... immergé' italic (enlarged crop)",
    "all italic inside the theorem environment", "convention", 6, "high",
    r"(autrement dit, n'ont pas de cycle premier associé<NL>immergé).",
    r"\textup{(autrement dit,} n'ont pas de cycle premier associé<NL>immergé\textup{)}.")
add(190, "Théorème (7.2.5), label c)", "label c) upright roman",
    r"\item[c)] comes out italic in the italic theorem", "convention", 6, "high",
    r"\item[c)]", r"\item[\textup{c)}]")
add(190, "Théorème (7.2.5) c): 'universellement caténaire (5.6.2)'",
    "reference (5.6.2) upright inside the italic statement", "italic inside the theorem environment",
    "convention", 6, "high",
    r"caténaire (5.6.2) et pour", r"caténaire \textup{(5.6.2)} et pour")
add(190, "Théorème (7.2.5) c): '(cf. (7.2.4)).'",
    "'(cf. (7.2.4))' upright inside the italic statement (enlarged crop)", "italic inside the theorem environment",
    "convention", 6, "high",
    r"(cf. (7.2.4)).", r"\textup{(cf. (7.2.4))}.")
add(190, "Théorème (7.2.5), label d)", "label d) upright roman",
    r"\item[d)] comes out italic in the italic theorem", "convention", 6, "high",
    r"\item[d)]", r"\item[\textup{d)}]")
add(190, "Théorème (7.2.5), label e)", "label e) upright roman",
    r"\item[e)] comes out italic in the italic theorem", "convention", 6, "high",
    r"\item[e)]", r"\item[\textup{e)}]")
add(190, "Théorème (7.2.5), last paragraph 'De plus, lorsque ces conditions sont remplies'",
    "new indented paragraph after item e)",
    r"'De plus' follows \end{enumerate} without a blank line (set without indentation)",
    "other", None, "medium",
    r"\end{enumerate}<NL>De plus,", r"\end{enumerate}<NL><NL>De plus,",
    r"Paragraph after the list, indented as printed (same form as the earlier \end{enumerate} fixes, e.g. p. 136).")

# ---------------------------------------------------------------- page 190: proof of (7.2.5)
add(190, "proof of (7.2.5), l. 1: 'L'équivalence de c), d) et e)'",
    "c), d), e) italic", "roman", "italics", None, "high",
    r"L'équivalence de c), d) et e) a été", r"L'équivalence de \emph{c)}, \emph{d)} et \emph{e)} a été")
add(190, "proof of (7.2.5), l. 1-2: 'Pour montrer que a) et b) sont équivalentes'",
    "a), b) italic", "roman", "italics", None, "high",
    r"que a) et b) sont équivalentes", r"que \emph{a)} et \emph{b)} sont équivalentes")
add(190, "proof of (7.2.5): 'où B = A/j_x'",
    "lower-case Fraktur j with subscript x (the prime ideal 𝔧_x of the point x; enlarged crop)",
    r"$B=A/\mathfrak J_x$ (capital Fraktur J)", "symbol", None, "high",
    r"$B=A/\mathfrak J_x$", r"$B=A/\mathfrak j_x$",
    r"Elsewhere ega4-2 writes this ideal \mathfrak j_x. The only other \mathfrak J_x of the file is on p. 197 ('Si l'on pose \mathfrak p=\mathfrak J_x'), for that checker.")
add(190, "proof of (7.2.5): 'ceci prouve l'équivalence de a) et b).'",
    "a), b) italic", "roman", "italics", None, "high",
    r"l'équivalence de a) et b). Le", r"l'équivalence de \emph{a)} et \emph{b)}. Le")
add(190, "proof of (7.2.5): 'Le même raisonnement montre que si a) est vérifiée'",
    "a) italic", "roman", "italics", None, "high",
    r"que si a) est vérifiée", r"que si \emph{a)} est vérifiée")
add(190, "proof of (7.2.5), second paragraph: 'Montrons maintenant que a) implique c). La condition a) implique'",
    "a), c), a) italic", "roman", "italics", None, "high",
    r"que a) implique c). La condition a) implique", r"que \emph{a)} implique \emph{c)}. La condition \emph{a)} implique")
add(190, "proof of (7.2.5): 'donc inf(codim(g^{-1}(T)∩{x'}, {x'})) lorsque x' parcourt'",
    "no comma between 'inf(...))' and 'lorsque' (enlarged crop); the comma after 'Ass(O_X')' is printed",
    "'...}))$, lorsque $x'$ parcourt': comma before 'lorsque'", "punctuation", None, "high",
    r"\overline{\{x'\}}))$, lorsque", r"\overline{\{x'\}}))$ lorsque")

# ---------------------------------------------------------------- page 191
add(191, "proof of (7.2.5), l. 1: 'Reste à prouver que c) entraîne a).'",
    "c), a) italic", "roman", "italics", None, "high",
    r"Reste à prouver que c) entraîne a).", r"Reste à prouver que \emph{c)} entraîne \emph{a)}.")
add(191, "proof of (7.2.5), l. 2-3: 'au cas où A = B est intègre.'",
    "'intègre' italic (enlarged crop)", "roman", "italics", None, "high",
    r"$A=B$ est intègre.", r"$A=B$ est \emph{intègre}.")
add(191, "case I): 'dim(C) = n—1. On a'",
    "long dash for the subtraction n—1 (clearly longer than the = bars; enlarged crop)", "minus sign n-1",
    "convention", 7, "high",
    r"$\dim(C)=n-1$. On a", r"$\dim(C)=n\setmin 1$. On a",
    r"\setmin pending the convention-7 decision (GLOBAL_ISSUES 23).")
add(191, "case I): 'par platitude (0_I, 6.3.4)'",
    "bold 0 with roman subscript I (enlarged crop)", "plain 0", "convention", 2, "high",
    r"(0$_{\mathrm I}$, 6.3.4)", r"(\textbf{0}$_{\mathrm I}$, 6.3.4)")
add(191, "display (7.2.5.1): 'dim({y'}) = dim({x'})—1.'",
    "long dash for the subtraction (enlarged crop)", "minus sign", "convention", 7, "high",
    r"\dim(\overline{\{x'\}})-1.", r"\dim(\overline{\{x'\}})\setmin 1.",
    r"\setmin pending the convention-7 decision (GLOBAL_ISSUES 23).")
add(191, "after (7.2.5.1): 'vérifie aussi l'hypothèse c) de l'énoncé'",
    "c) italic", "roman", "italics", None, "high",
    r"aussi l'hypothèse c) de", r"aussi l'hypothèse \emph{c)} de")
add(191, "after (7.2.5.1): 'on a dim({y'}) = dim(C) = n—1;'",
    "long dash for the subtraction (enlarged crop)", "minus sign", "convention", 7, "high",
    r"=\dim(C)=n-1$", r"=\dim(C)=n\setmin 1$",
    r"\setmin pending the convention-7 decision (GLOBAL_ISSUES 23).")
add(191, "case II), l. 1: 'est une A-algèbre finie,'",
    "'finie' italic (enlarged crop)", "roman", "italics", None, "high",
    r"$A$-algèbre finie, il vérifie", r"$A$-algèbre \emph{finie}, il vérifie")
add(191, "case II): 'sont tous de dimension n (5.6.10)'",
    "'de dimension' italic, both words (enlarged crop)", r"de \emph{dimension}: 'de' roman",
    "italics", None, "high",
    r"de \emph{dimension}", r"\emph{de dimension}")
add(191, "case II): 'ces anneaux vérifient l'hypothèse c) de l'énoncé'",
    "c) italic", "roman", "italics", None, "high",
    r"vérifient l'hypothèse c) de", r"vérifient l'hypothèse \emph{c)} de")
add(191, "case II): 'X'_1 = Spec((A^{(1)})^) = X'×_X X_1'",
    "Spec((A^{(1)})^): A^{(1)} in parentheses with the circumflex raised after the closing parenthesis (enlarged crop)",
    r"\operatorname{Spec}(\widehat{A^{(1)}}): hat over A^{(1)}, no inner parentheses",
    "formula", None, "high",
    r"\operatorname{Spec}(\widehat{A^{(1)}})", r"\operatorname{Spec}((A^{(1)})^{\widehat{\,}})",
    r"Hat after the parenthesis, written as in the EGA II p. 194 and EGA III p. 123 fixes (^{\widehat{\,}}; \superhat pending, GLOBAL_ISSUES 31/47).")
add(191, "Définition (7.2.6): 'les conditions équivalentes de (7.2.5)'",
    "reference (7.2.5) upright inside the italic definition (enlarged crop)", "italic inside the definition environment",
    "convention", 6, "high",
    r"(7.2.5), on dit", r"\textup{(7.2.5)}, on dit")
add(191, "Définition (7.2.6): 'on dit qu'il est strictement formellement caténaire.'",
    "italic like the rest of the definition, no change of face (enlarged crop)",
    r"\emph{...} inside the italic definition (comes out upright)", "convention", 6, "high",
    r"\emph{strictement formellement caténaire}", r"strictement formellement caténaire")

# ---------------------------------------------------------------- page 192
add(192, "Corollaire (7.2.7): 'un A-module de Cohen-Macaulay'",
    "hyphen in Cohen-Macaulay (enlarged crop)", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
    r"$A$-module de Cohen--Macaulay et", r"$A$-module de Cohen-Macaulay et",
    "Same correction as the p. 150-151 fixes (findings_150_154).")
add(192, "proof of (7.2.7): 'préschémas de Cohen-Macaulay (6.3.8)'",
    "hyphen", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
    r"préschémas de Cohen--Macaulay (6.3.8)", r"préschémas de Cohen-Macaulay (6.3.8)")
add(192, "proof of (7.2.9): 'tout anneau quotient intègre B d'un tel anneau A'",
    "'intègre' italic (enlarged crop)", "roman", "italics", None, "high",
    r"quotient intègre $B$ d'un tel", r"quotient \emph{intègre} $B$ d'un tel")
add(192, "Remarques (7.2.10) (i): 'd'un anneau local de Cohen-Macaulay'",
    "hyphen", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
    r"anneau local de Cohen--Macaulay est", r"anneau local de Cohen-Macaulay est")
add(192, "Remarques (7.2.10) (i), second paragraph: 'un anneau de Cohen-Macaulay. Rappelons'",
    "hyphen", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
    r"Cohen--Macaulay. Rappelons", r"Cohen-Macaulay. Rappelons")
add(192, "Remarques (7.2.10) (ii): 'dans les conditions équivalentes c), d), e) de (7.2.5)'",
    "c), d), e) italic in the roman remark (enlarged crop)", "roman letters (judged with the remark body roman)",
    "italics", None, "high",
    r"équivalentes c), d), e) de", r"équivalentes \emph{c)}, \emph{d)}, \emph{e)} de")
add(192, "heading 7.3",
    "'7.3. Fibres formelles des anneaux locaux noethériens.' with a final full stop",
    "no full stop in the \\subsection title", "punctuation", None, "high",
    r"\subsection{Fibres formelles des anneaux locaux noethériens}",
    r"\subsection{Fibres formelles des anneaux locaux noethériens.}",
    "GLOBAL_ISSUES 43; same form as the p. 90/92 heading fixes.")

# ---------------------------------------------------------------- page 193
add(193, "(7.3.1) continued, 2°: 'la propriété P(f^{-1}(y), k(y)) est vraie'",
    "bold italic k in k(y)", "plain k", "convention", 1, "high",
    r"\boldsymbol P(f^{-1}(y),k(y))", r"\boldsymbol P(f^{-1}(y),\boldsymbol{k}(y))")
add(193, "Lemme (7.3.2) b): 'Q(O_x ⊗_{O_y} k(y), k(y))', first k(y)",
    "bold italic k (both k(y) in this formula)", "plain k", "convention", 1, "high",
    r"\otimes_{\mathscr O_y}k(y),k(y))", r"\otimes_{\mathscr O_y}\boldsymbol{k}(y),\boldsymbol{k}(y))",
    "One edit for this entry and the next (second k(y) of the same formula).")
add(193, "Lemme (7.3.2) b): 'Q(O_x ⊗_{O_y} k(y), k(y))', second k(y)",
    "bold italic k", "plain k", "convention", 1, "high",
    None, None, "Covered by the edit of the previous entry.")
add(193, "proof of (7.3.2), l. 1: 'L'équivalence de a) et b) résulte'",
    "a), b) italic (enlarged crop)", "roman", "italics", None, "high",
    r"L'équivalence de a) et b) résulte", r"L'équivalence de \emph{a)} et \emph{b)} résulte")
add(193, "proof of (7.3.2), l. 2: 'l'équivalence de b) et c), compte tenu'",
    "b), c) italic", "roman", "italics", None, "high",
    r"l'équivalence de b) et c), compte", r"l'équivalence de \emph{b)} et \emph{c)}, compte")
add(193, "proof of (7.3.2): '(I, 2.4.2)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 2.4.2)", r"(\textbf{I}, 2.4.2)")
add(193, "proof of (7.3.2), l. 2-3: 'l'équivalence de b) et c') résulte'",
    "b), c') italic", "roman", "italics", None, "high",
    r"l'équivalence de b) et c$'$) résulte", r"l'équivalence de \emph{b)} et \emph{c$'$)} résulte")
add(193, "proof of (7.3.3): '(I, 1.6.2)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 1.6.2)", r"(\textbf{I}, 1.6.2)")
add(193, "(7.3.4), condition (P_III)",
    "'(P_III). — Pour tout corps k': full stop after the label (enlarged crop)",
    r"\item[$(\mathrm P_{\mathrm{III}})$] --- Pour: no full stop", "punctuation", None, "high",
    r"\item[$(\mathrm P_{\mathrm{III}})$] --- Pour", r"\item[$(\mathrm P_{\mathrm{III}})$.] --- Pour")
add(193, "Remarques (7.3.5), label (i)",
    "'(i)' upright, with both parentheses (enlarged crop)",
    r"\item[\emph{i)}]: no opening parenthesis, label set with \emph (italic once the remark body is roman)",
    "punctuation", None, "high",
    r"\item[\emph{i)}] Les conditions", r"\item[(i)] Les conditions",
    "Also an italics difference (same edit).")
add(193, "Remarques (7.3.5), label (ii)",
    "'(ii)' upright, with both parentheses (enlarged crop)",
    r"\item[\emph{ii)}]: no opening parenthesis, \emph label", "punctuation", None, "high",
    r"\item[\emph{ii)}] Notons", r"\item[(ii)] Notons", "Also an italics difference (same edit).")
add(193, "Remarques (7.3.5) (ii): 'f^{-1}(y) (I, 3.6.4)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
add(193, "Remarques (7.3.5), label (iii)",
    "'(iii)' upright, with both parentheses",
    r"\item[\emph{iii)}]: no opening parenthesis, \emph label", "punctuation", None, "high",
    r"\item[\emph{iii)}] Dans", r"\item[(iii)] Dans", "Also an italics difference (same edit).")
add(193, "Remarques (7.3.5) (iii), condition (P'_I)",
    "'(P'_I). — Si f : X→Y': full stop after the label (enlarged crop)",
    r"\item[$(\mathrm P'_{\mathrm I})$] --- Si: no full stop", "punctuation", None, "high",
    r"\item[$(\mathrm P'_{\mathrm I})$] --- Si", r"\item[$(\mathrm P'_{\mathrm I})$.] --- Si")

# ---------------------------------------------------------------- page 194
add(194, "proof of (7.3.7), l. 1: 'k(y') est une extension de type fini'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"$k(y')$ est une", r"$\boldsymbol{k}(y')$ est une")
add(194, "proof of (7.3.7), l. 2: 'de type fini de k(y)'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"fini de $k(y)$", r"fini de $\boldsymbol{k}(y)$")
add(194, "proof of (7.3.7): '(I, 6.4.11)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 6.4.11)", r"(\textbf{I}, 6.4.11)")
add(194, "proof of (7.3.7): 'f'^{-1}(y') = f^{-1}(y) ⊗_{k(y)} k(y')', subscript k(y)",
    "k of the subscript k(y) bold upright; the following k(y') bold italic (enlarged crop)", "plain k twice",
    "convention", 1, "high",
    r"\otimes_{k(y)}k(y')", r"\otimes_{\mathbf{k}(y)}\boldsymbol{k}(y')",
    "Subscript k bold upright (GLOBAL_ISSUES 48). One edit for this entry and the next.")
add(194, "proof of (7.3.7): 'f^{-1}(y) ⊗_{k(y)} k(y')', the k(y') after the tensor sign",
    "bold italic k", "plain k", "convention", 1, "high",
    None, None, "Covered by the edit of the previous entry.")
add(194, "proof of (7.3.7): '(I, 3.6.4)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 3.6.4)", r"(\textbf{I}, 3.6.4)")
add(194, "heading of (7.3.8) (edit 1 of 2)",
    "'Exemples (7.3.8). — Les propriétés P(Z, k) suivantes ...': heading word before the number, body roman",
    r"\begin{env}[7.3.8] with a hand-made '\emph{Exemples.} ---': gives '(7.3.8) Exemples. —'",
    "other", None, "high",
    r"\begin{env}[7.3.8]<NL>\label{IV.2.s7.3.8-fr}<NL>\emph{Exemples.} --- Les",
    r"\begin{examples}[7.3.8]<NL>\label{IV.2.s7.3.8-fr}<NL>Les",
    r"Uses the examples environment of EGA_IV2_FR.tex (as for (7.5.3)); cf. GLOBAL_ISSUES 40. Apply together with the next entry, which closes the environment.")
add(194, "end of (7.3.8) (edit 2 of 2)", "see the previous entry",
    r"\end{env} closing (7.3.8) after (vii')", "other", None, "high",
    r"géométriquement normal.<NL>\end{enumerate}<NL>\end{env}",
    r"géométriquement normal.<NL>\end{enumerate}<NL>\end{examples}",
    "Apply together with the previous entry.")
add(194, "Exemples (7.3.8) (ii): 'Z est un préschéma de Cohen-Macaulay.'",
    "hyphen", "Cohen--Macaulay (en dash)", "punctuation", None, "high",
    r"préschéma de Cohen--Macaulay.", r"préschéma de Cohen-Macaulay.")
add(194, "Exemples (7.3.8): paragraph 'Pour les propriétés (ii) à (vii)' after the list",
    "new indented paragraph after (vii) (enlarged crop)",
    r"'Pour les propriétés' follows \end{enumerate} without a blank line (set without indentation)",
    "other", None, "medium",
    r"\end{enumerate}<NL>Pour les propriétés", r"\end{enumerate}<NL><NL>Pour les propriétés",
    r"Same form as the earlier \end{enumerate} fixes (e.g. p. 136).")
add(194, "Exemples (7.3.8): 'les propriétés (i), (ii) et (iii) sont géométriques;'",
    "'géométriques' italic (enlarged crop)", "roman", "italics", None, "high",
    r"sont<NL>géométriques;", r"sont<NL>\emph{géométriques};")
add(194, "Remarques (7.3.9), label (i)",
    "'(i)' upright, with both parentheses",
    r"\item[\emph{i)}]: no opening parenthesis, \emph label", "punctuation", None, "high",
    r"\item[\emph{i)}] Chacune", r"\item[(i)] Chacune", "Also an italics difference (same edit).")
add(194, "Remarques (7.3.9), label (ii)",
    "'(ii)' upright, with both parentheses",
    r"\item[\emph{ii)}]: no opening parenthesis, \emph label", "punctuation", None, "high",
    r"\item[\emph{ii)}] Dans tous", r"\item[(ii)] Dans tous", "Also an italics difference (same edit).")
add(194, "Remarques (7.3.9) (ii), last line: '(0, 16.5.10 et 17.3.2)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 16.5.10 et 17.3.2)", r"(\textbf{0}, 16.5.10 et 17.3.2)")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
print(len(F), "findings written")
