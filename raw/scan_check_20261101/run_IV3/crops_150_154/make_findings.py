import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_150_154.json")

NL = "<NL>"


def t(s):
    """Raw LaTeX string with <NL> for line breaks."""
    if s is None:
        return None
    return s.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": t(old), "new": t(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = t(corrected)
    d["note"] = note
    return d


G80 = "Text after the list is an indented new paragraph in the print (GLOBAL_ISSUES 80)."
HAT = "Same pattern as convention 8, with a hat (hat over A only, prime outside)."
NO = "The print has n with a raised letter o (the edition's n\\textsuperscript{o}); n$^\\circ$ typesets a ring."
LAB = "One edit of the label option covers (i) and (ii) (next entry). GLOBAL_ISSUES 16."

L = []

# ---------------- page 150 ----------------
p = 150
L.append(F(p, "proof of (11.4.12): 'il y a déjà un nombre fini de ces noyaux'",
           "'fini' italic", "upright", "italics", None, "high",
           r"nombre fini de ces noyaux", r"nombre \emph{fini} de ces noyaux"))
L.append(F(p, "proof of (11.4.12): 'au cas où la famille (A'_α) est finie.'",
           "'finie' italic", "upright", "italics", None, "high",
           r"$(A'_\alpha)$ est finie.", r"$(A'_\alpha)$ est \emph{finie}."))
L.append(F(p, "proof of (11.4.12): 'un anneau local artinien, entier sur A'",
           "'artinien' italic", "upright", "italics", None, "high",
           r"anneau local<NL>artinien,", r"anneau local<NL>\emph{artinien},"))
L.append(F(p, "proof of (11.4.12): 'artinien, entier sur A et que'",
           "'entier' italic", "upright", "italics", None, "high",
           r"entier sur $A$ et que", r"\emph{entier} sur $A$ et que"))
L.append(F(p, "proof of (11.4.12): '... soit isomorphe à k'. Par platitude, les noyaux'",
           "'Par platitude' continues the paragraph (flush left, after a full justified line; enlarged crop)",
           "blank line before 'Par platitude': a paragraph break the print does not have",
           "other", None, "high",
           r"isomorphe à $k'$.<NL><NL>Par platitude", r"isomorphe à $k'$.<NL>Par platitude",
           "Paragraph break only."))
L.append(F(p, "proof of (11.4.12): 'localisés de B'_α en ses idéaux maximaux'",
           "'maximaux' italic", "upright", "italics", None, "high",
           r"en ses idéaux maximaux~;", r"en ses idéaux \emph{maximaux}~;"))
L.append(F(p, "proof of (11.4.12): '(Bourbaki, Alg. comm., chap. II, § 3, n° 3, cor. 2 du th. 1)'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~3, cor.~2 du th.", r"n\textsuperscript{o}~3, cor.~2 du th.", NO))
L.append(F(p, "Corollaire (11.4.13): 'Soit (Y'_α) une famille de A-préschémas'",
           "'A-préschémas' (enlarged crop p150_Apresch.png)", "'$Y$-préschémas'",
           "formula", None, "high",
           r"$Y$-préschémas, et pour tout", r"$A$-préschémas, et pour tout",
           "Same meaning (Y = Spec(A)), but the print has A."))
L.append(F(p, "Corollaire (11.4.13), label (i)",
           "label '(i)' upright before the italic statement",
           "\\begin{enumerate}[label=(\\roman*)] inside the italic corollary environment: italic label",
           "convention", 6, "high",
           r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]", LAB))
L.append(F(p, "Corollaire (11.4.13), label (ii)",
           "label '(ii)' upright", "italic (same enumerate)", "convention", 6, "high",
           None, None, "Covered by the previous edit (label=\\textup{(\\roman*)})."))
L.append(F(p, "Corollaire (11.4.13)(ii): 'est f'_α-plat en tous les points x'_α'",
           "'tous' printed roman inside the italic statement (enlarged crop p150_tous.png)",
           "italic (corollary environment)", "convention", 6, "high",
           r"-plat en tous", r"-plat en \textup{tous}"))
L.append(F(p, "Corollaire (11.4.13): 'Alors F est f-plat au point x.' after the list",
           "indented new paragraph", "follows \\end{enumerate} without a blank line: set without indent",
           "other", None, "high",
           r"\end{enumerate}<NL>Alors", r"\end{enumerate}<NL><NL>Alors", G80))
L.append(F(p, "proof of (11.4.13): 'le schéma local Y''_{α,y'_α} = Spec(O_{y'_α})'",
           "Spec(O_{y'_α}): subscript y'_α only (enlarged crop p150_spec.png)",
           "\\operatorname{Spec}(\\mathcal O_{Y'_\\alpha,y'_\\alpha})", "formula", None, "high",
           r"\operatorname{Spec}(\mathcal O_{Y'_\alpha,y'_\alpha})", r"\operatorname{Spec}(\mathcal O_{y'_\alpha})"))
L.append(F(p, "proof of (11.4.13): 'est Y''_{α,y'_α}-plat aux points'",
           "'plat' italic (enlarged crop p150_plat.png)", "upright", "italics", None, "high",
           r"$Y''_{\alpha,y'_\alpha}$-plat aux points", r"$Y''_{\alpha,y'_\alpha}$-\emph{plat} aux points"))
L.append(F(p, "proof of (11.4.13): 'Bourbaki, Alg. comm., chap. II, § 3, n° 3, cor. 2 du th. 1.'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~3, cor.~2 du<NL>th.", r"n\textsuperscript{o}~3, cor.~2 du<NL>th.", NO))
L.append(F(p, "heading 11.5",
           "'11.5. Descente de la platitude par des morphismes quelconques : cas général.' with a final full stop",
           "no full stop", "punctuation", None, "high",
           r"\subsection{Descente de la platitude par des morphismes quelconques : cas général}",
           r"\subsection{Descente de la platitude par des morphismes quelconques : cas général.}",
           "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))

# ---------------- page 151 ----------------
p = 151
L.append(F(p, "Théorème (11.5.1): 'l'homomorphisme canonique (I, 2.4.4)'",
           "the reference (I, 2.4.4) upright inside the italic statement (enlarged crop p151_top.png)",
           "(\\textbf I, 2.4.4) inside the italic theorem environment: italic", "convention", 6, "high",
           r"(\textbf I, 2.4.4)", r"\textup{(\textbf I, 2.4.4)}"))
L.append(F(p, "Théorème (11.5.1): 'et supposons vérifiée l'une des hypothèses suivantes'",
           "'l'une' printed roman inside the italic statement (enlarged crop p151_top.png)",
           "italic", "convention", 6, "high",
           r"vérifiée l'une", r"vérifiée \textup{l'une}"))
L.append(F(p, "Théorème (11.5.1), label (i)",
           "label '(i)' upright", "\\begin{enumerate}[label=(\\roman*)] in the italic theorem: italic label",
           "convention", 6, "high",
           r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]", LAB))
L.append(F(p, "Théorème (11.5.1), label (ii)",
           "label '(ii)' upright", "italic (same enumerate)", "convention", 6, "high",
           None, None, "Covered by the previous edit (label=\\textup{(\\roman*)})."))
L.append(F(p, "Théorème (11.5.1)(i): 'est f'_α-plat en tous les points'",
           "'tous' printed roman inside the italic statement (enlarged crop p151_items.png)",
           "italic", "convention", 6, "high",
           r"-plat en tous", r"-plat en \textup{tous}"))
L.append(F(p, "Théorème (11.5.1)(ii): 'et k(x) est une extension primaire'",
           "bold italic k(x)", "plain k(x)", "convention", 1, "high",
           r"et $k(x)$ est une", r"et $\boldsymbol{k}(x)$ est une"))
L.append(F(p, "Théorème (11.5.1)(ii): 'extension primaire de k(y)'",
           "bold italic k(y)", "plain k(y)", "convention", 1, "high",
           r"primaire de $k(y)$", r"primaire de $\boldsymbol{k}(y)$"))
L.append(F(p, "Théorème (11.5.1): 'Dans ces conditions, F est f-plat au point x.' after the list",
           "indented new paragraph", "follows \\end{enumerate} without a blank line: set without indent",
           "other", None, "high",
           r"\end{enumerate}<NL>Dans ces conditions", r"\end{enumerate}<NL><NL>Dans ces conditions", G80))
L.append(F(p, "proof of (11.5.1): 'et comme F_x⊗(O_y/m_y^n) = (F_x⊗(O_y/J_λ))⊗(O_y/m_y^n), il suffira'",
           "formula in the running text: 'et comme F_x⊗_{O_y}(O_y/m^n_y)=(F_x⊗_{O_y}(O_y/J_λ))⊗_{O_y/J_λ}(O_y/m^n_y), il suffira de prouver'",
           "displayed with \\[ ... \\]", "other", None, "high",
           r"et comme<NL>\[<NL>\mathcal F_x\otimes_{\mathcal O_y}(\mathcal O_y/\mathfrak m_y^n)<NL>=\bigl(\mathcal F_x\otimes_{\mathcal O_y}(\mathcal O_y/\mathfrak J_\lambda)\bigr)<NL> \otimes_{\mathcal O_y/\mathfrak J_\lambda}(\mathcal O_y/\mathfrak m_y^n),<NL>\]<NL>il suffira",
           r"et comme<NL>$\mathcal F_x\otimes_{\mathcal O_y}(\mathcal O_y/\mathfrak m_y^n)=(\mathcal F_x\otimes_{\mathcal O_y}(\mathcal O_y/\mathfrak J_\lambda))\otimes_{\mathcal O_y/\mathfrak J_\lambda}(\mathcal O_y/\mathfrak m_y^n)$,<NL>il suffira",
           "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); the connecting words 'et comme' and ', il suffira' are kept."))
L.append(F(p, "Corollaire (11.5.2): 'l'homomorphisme û : Â→Â' soit injectif'",
           "hat over A only, prime outside the hat (enlarged crop p151_hat.png)", "\\widehat{A'} (hat over A')",
           "formula", None, "high",
           r"\to\widehat{A'}$ soit injectif", r"\to\widehat{A}'$ soit injectif", HAT))
L.append(F(p, "proof of (11.5.2): 'un sous-anneau de Â (resp. Â')'",
           "hat over A only, prime outside the hat", "\\widehat{A'}", "formula", None, "high",
           r"(resp.<NL>$\widehat{A'}$)", r"(resp.<NL>$\widehat{A}'$)", HAT))
L.append(F(p, "proof of (11.5.2): '(Bourbaki, Alg. comm., chap. III, § 3, n° 3, prop. 6)'",
           "n with a raised letter o (enlarged crop p151_no.png)", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~3,", r"n\textsuperscript{o}~3,", NO))
L.append(F(p, "proof of (11.5.2), display: 'm'^n_α Â' = m-hat'^n_α'",
           "hat over A only, prime outside the hat", "\\widehat{A'}", "formula", None, "high",
           r"\mathfrak m_\alpha'^{\,n}\widehat{A'}", r"\mathfrak m_\alpha'^{\,n}\widehat{A}'", HAT))
L.append(F(p, "proof of (11.5.2): '(Bourbaki, Alg. comm., chap. III, § 2, n° 7, prop. 8, où on peut ...)'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~7", r"n\textsuperscript{o}~7", NO))

# ---------------- page 152 ----------------
p = 152
L.append(F(p, "proof of (11.5.2), first line: 'fixé, l'intersection des m-hat'^n_α Â'_{m-hat'_α} pour n>0'",
           "'l'intersection des m̂'ⁿ_α Â'...' without the word 'idéaux' (enlarged crop p152_top.png)",
           "'l'intersection des idéaux'", "extra", None, "high",
           r"l'intersection des idéaux", r"l'intersection des"))
L.append(F(p, "proof of (11.5.2): 'des m-hat'^n_α Â'_{m-hat'_α} pour n>0'",
           "hat over A only, prime and subscript outside the hat", "\\widehat{A'}_{...}", "formula", None, "high",
           r"^{\,n}\widehat{A'}_{", r"^{\,n}\widehat{A}'_{", HAT))
L.append(F(p, "proof of (11.5.2): 'dans l'anneau local noethérien Â'_{m-hat'_α}'",
           "hat over A only", "\\widehat{A'}_{...}", "formula", None, "high",
           r"\widehat{A'}_{\widehat{\mathfrak m}'_\alpha}$. D'autre", r"\widehat{A}'_{\widehat{\mathfrak m}'_\alpha}$. D'autre", HAT))
L.append(F(p, "proof of (11.5.2): 'sont les idéaux maximaux de Â''",
           "hat over A only (enlarged crop p152_hats.png)", "\\widehat{A'}", "formula", None, "high",
           r"maximaux de $\widehat{A'}$", r"maximaux de $\widehat{A}'$", HAT))
L.append(F(p, "proof of (11.5.2): 'l'homomorphisme canonique Â'→Π_α Â'_{m-hat'_α}'",
           "hat over A only in both Â' (enlarged crop p152_hats.png)", "\\widehat{A'} twice", "formula", None, "high",
           r"$\widehat{A'}\to\prod_\alpha\widehat{A'}_{", r"$\widehat{A}'\to\prod_\alpha\widehat{A}'_{",
           HAT + " Both occurrences in one edit."))
L.append(F(p, "proof of (11.5.2): '(Bourbaki, Alg. comm., chap. II, § 3, n° 3, cor. 2 du th. 1)'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~3, cor.~2", r"n\textsuperscript{o}~3, cor.~2", NO))
L.append(F(p, "proof of (11.5.2): 'comme par hypothèse û : Â→Â' est aussi injectif'",
           "hat over A only", "\\widehat{A'}", "formula", None, "high",
           r"\to\widehat{A'}$ est aussi", r"\to\widehat{A}'$ est aussi", HAT))
L.append(F(p, "proof of (11.5.2): '(0_I, 7.3.5) et Â' = A'⊗_A Â puisque'",
           "hat over A only (enlarged crop p152_hats2.png)", "\\widehat{A'}", "formula", None, "high",
           r"$\widehat{A'}=A'\otimes_A", r"$\widehat{A}'=A'\otimes_A", HAT))
L.append(F(p, "proof of (11.5.2): '(Bourbaki, Alg. comm., chap. III, § 3, n° 4, th. 3'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~4", r"n\textsuperscript{o}~4", NO))
L.append(F(p, "proof of (11.5.2): 'et chap. IV, § 2, n° 5, cor. 3 de la prop. 9)'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~5", r"n\textsuperscript{o}~5", NO))
L.append(F(p, "Proposition (11.5.3): 'g = (ψ, θ) : Y'→Y un morphisme propre de présentation finie'",
           "'propre' printed roman inside the italic statement (enlarged crop p152_stmt.png)",
           "italic", "convention", 6, "high",
           r"un morphisme propre de", r"un morphisme \textup{propre} de"))
L.append(F(p, "Proposition (11.5.3): 'On suppose que :'",
           "'On suppose que :' (enlarged crop p152_stmt.png)", "'Supposons que~:'", "word", None, "high",
           r"Supposons que~:", r"On suppose que~:",
           "The TeX rewords the hypotheses of (11.5.3); with the next entries for (i) and (ii)."))
L.append(F(p, "Proposition (11.5.3), label (i)",
           "label '(i)' upright", "\\begin{enumerate}[label=(\\roman*)] in the italic proposition: italic label",
           "convention", 6, "high",
           r"\begin{enumerate}[label=(\roman*)]", r"\begin{enumerate}[label=\textup{(\roman*)}]", LAB))
L.append(F(p, "Proposition (11.5.3), label (ii)",
           "label '(ii)' upright", "italic (same enumerate)", "convention", 6, "high",
           None, None, "Covered by the previous edit (label=\\textup{(\\roman*)})."))
L.append(F(p, "Proposition (11.5.3)(i): 'L'homomorphisme θ_y'",
           "capital 'L'homomorphisme'", "'l'homomorphisme'", "word", None, "high",
           r"\item l'homomorphisme", r"\item L'homomorphisme"))
L.append(F(p, "Proposition (11.5.3)(i): 'θ_y : O_y→(g_*(O_{Y'}))_y'",
           "(g_*(O_{Y'}))_y: O_{Y'} in parentheses (enlarged crop p152_stmt.png)",
           "(g_*\\mathcal O_{Y'})_y", "formula", None, "high",
           r"(g_*\mathcal O_{Y'})_y", r"(g_*(\mathcal O_{Y'}))_y"))
L.append(F(p, "Proposition (11.5.3)(i): '... est injectif.'",
           "'est injectif.' (indicative, full stop)", "'soit injectif~;'", "word", None, "high",
           r"soit injectif~;", r"est injectif."))
L.append(F(p, "Proposition (11.5.3)(ii): 'Pour tout x'∈X''",
           "capital 'Pour'", "'pour'", "word", None, "high",
           r"\item pour tout", r"\item Pour tout"))
L.append(F(p, "Proposition (11.5.3)(ii): 'F' = F⊗_Y Y' est Y'-plat au point x''",
           "'est Y'-plat'", "'soit $Y'$-plat'", "word", None, "high",
           r"$ soit $Y'$-plat", r"$ est $Y'$-plat"))
L.append(F(p, "Proposition (11.5.3): 'Alors F est f-plat au point x.' after the list",
           "indented new paragraph", "follows \\end{enumerate} without a blank line: set without indent",
           "other", None, "high",
           r"\end{enumerate}<NL>Alors", r"\end{enumerate}<NL><NL>Alors", G80))
L.append(F(p, "proof of (11.5.3): 'on peut donc supposer déjà que F' est f'-plat.'",
           "'plat' italic (enlarged crop p152_a.png)", "upright", "italics", None, "high",
           r"est $f'$-plat.", r"est $f'$-\emph{plat}."))
L.append(F(p, "proof of (11.5.3): '... est f'-plat. D'autre part, tenant compte de'",
           "'D'autre part' continues the line: no paragraph break (enlarged crop p152_a.png)",
           "blank line before 'D'autre part': a paragraph break the print does not have",
           "other", None, "high",
           r"<NL><NL>D'autre part", r"<NL>D'autre part", "Paragraph break only."))
L.append(F(p, "proof of (11.5.3): 'D'autre part, tenant compte de (I, 3.6.5)'",
           "'tenant compte de' (no 'en')", "'en tenant compte de'", "extra", None, "high",
           r", en tenant compte de", r", tenant compte de"))
L.append(F(p, "proof of (11.5.3): 'où A est un anneau local.'",
           "'local' italic", "upright", "italics", None, "high",
           r"anneau<NL>local. Sous", r"anneau<NL>\emph{local}. Sous"))
L.append(F(p, "proof of (11.5.3): 'on va prouver que F est f-plat.'",
           "'plat' italic (enlarged crop p152_a.png)", "upright", "italics", None, "high",
           r"est $f$-plat. En", r"est $f$-\emph{plat}. En"))
L.append(F(p, "proof of (11.5.3): 'de sous-anneaux locaux noethériens A_λ'",
           "'locaux noethériens' italic", "upright", "italics", None, "high",
           r"sous-anneaux locaux noethériens", r"sous-anneaux \emph{locaux noethériens}"))
L.append(F(p, "proof of (11.5.3): 'soit un homomorphisme local.'",
           "'local' italic", "upright", "italics", None, "high",
           r"homomorphisme local. En vertu", r"homomorphisme \emph{local}. En vertu"))
L.append(F(p, "proof of (11.5.3): 'étant un morphisme de type fini, F_λ un O_{X_λ}-Module cohérent'",
           "comma before F_λ (enlarged crop p152_b.png)", "'et $\\mathcal F_\\lambda$ un'", "word", None, "high",
           r"de type fini et $\mathcal F_\lambda$ un", r"de type fini, $\mathcal F_\lambda$ un"))
L.append(F(p, "proof of (11.5.3): 'en outre (8.10.5, (xii)), on peut supposer que g_λ est propre.'",
           "'en outre (8.10.5, (xii)), on peut supposer que g_λ est propre.' with 'propre' italic (enlarged crop p152_b.png)",
           "'en outre, (8.10.5, (xii)) permet de supposer $g_\\lambda$ propre.' (reworded)", "word", None, "high",
           r"en outre, (8.10.5, (xii)) permet de supposer $g_\lambda$ propre.",
           r"en outre (8.10.5, (xii)), on peut supposer que $g_\lambda$ est \emph{propre}.",
           "The edit restores the printed wording and the italic 'propre' together."))
L.append(F(p, "proof of (11.5.3): 'supposer l'anneau A noethérien, les autres hypothèses'",
           "'noethérien' italic", "upright", "italics", None, "high",
           r"l'anneau $A$<NL>noethérien,", r"l'anneau $A$<NL>\emph{noethérien},"))
L.append(F(p, "proof of (11.5.3): '... étant vérifiées. Posons alors B = Â'",
           "'Posons alors' continues the line: no paragraph break",
           "blank line before 'Posons alors': a paragraph break the print does not have",
           "other", None, "high",
           r"étant vérifiées.<NL><NL>Posons alors", r"étant vérifiées.<NL>Posons alors", "Paragraph break only."))
L.append(F(p, "proof of (11.5.3): 'est Z-plat (2.1.4); de même, si l'on pose'",
           "semicolon and lower-case 'de même' (enlarged crop p152_c.png)", "'(2.1.4). De même,'",
           "punctuation", None, "high",
           r"$Z$-plat (2.1.4). De même,", r"$Z$-plat (2.1.4)~; de même,"))

# ---------------- page 153 ----------------
p = 153
L.append(F(p, "proof of (11.5.3): 'l'homomorphisme O_z→(h_*(O_{Z'}))_z'",
           "(h_*(O_{Z'}))_z: O_{Z'} in parentheses (enlarged crop p153_a.png)", "(h_*\\mathcal O_{Z'})_z",
           "formula", None, "high",
           r"(h_*\mathcal O_{Z'})_z", r"(h_*(\mathcal O_{Z'}))_z"))
L.append(F(p, "proof of (11.5.3): '... est injectif, car il résulte de (2.3.1)'",
           "'injectif' italic", "upright", "italics", None, "high",
           r"$ est injectif, car il", r"$ est \emph{injectif}, car il"))
L.append(F(p, "proof of (11.5.3): 'h_*(O_{Z'}) = g_*(O_{Y'})⊗_Y Z'",
           "O_{Z'} and O_{Y'} in parentheses (enlarged crop p153_a.png)",
           "h_*\\mathcal O_{Z'}=g_*\\mathcal O_{Y'}\\otimes_Y Z", "formula", None, "high",
           r"h_*\mathcal O_{Z'}=g_*\mathcal O_{Y'}\otimes_Y Z", r"h_*(\mathcal O_{Z'})=g_*(\mathcal O_{Y'})\otimes_Y Z"))
L.append(F(p, "proof of (11.5.3): 'l'anneau local noethérien A complet'",
           "'complet' italic", "upright", "italics", None, "high",
           r"$A$ complet~;", r"$A$ \emph{complet}~;"))
L.append(F(p, "proof of (11.5.3): '(où y' parcourt g^{-1}(y)) est réduite à 0.'",
           "'réduite à' italic (enlarged crop p153_b.png)", "upright", "italics", None, "high",
           r"est réduite à $0$. En effet", r"est \emph{réduite à} $0$. En effet"))
L.append(F(p, "proof of (11.5.3): 'les intersections finies des a_{n,y'} formeront donc un système fondamental'",
           "'; les intersections finies des 𝔞_{n,y'} formeront donc un système' (enlarged crop p153_c.png)",
           "'~; elles forment donc un système'", "word", None, "high",
           r"~; elles forment donc", r"~; les intersections finies des $\mathfrak a_{n,y'}$ formeront donc"))
L.append(F(p, "proof of (11.5.3): '(Bourbaki, Alg. comm., chap. III, § 2, n° 7, prop. 8'",
           "n with a raised letter o", "n$^\\circ$ (degree ring)", "symbol", None, "medium",
           r"n$^\circ$~7", r"n\textsuperscript{o}~7", NO))
L.append(F(p, "proof of (11.5.3): 'où on peut dans la démonstration remplacer la suite décroissante'",
           "'où on peut dans la démonstration remplacer' (enlarged crop p153_c.png)",
           "'où l'on peut remplacer'", "word", None, "high",
           r"où l'on peut remplacer", r"où on peut dans la démonstration remplacer"))
L.append(F(p, "proof of (11.5.3): 'filtrant quelconque); on pourra par suite appliquer (11.5.1)'",
           "'quelconque); on pourra' (enlarged crop p153_d.png)", "'quelconque), et l'on pourra'",
           "word", None, "high",
           r"quelconque), et l'on pourra", r"quelconque)~; on pourra"))
L.append(F(p, "proof of (11.5.3): 'Mais comme g est fermé'",
           "'fermé' italic (enlarged crop p153_e.png)", "upright", "italics", None, "high",
           r"$g$ est<NL>fermé,", r"$g$ est<NL>\emph{fermé},"))
L.append(F(p, "proof of (11.5.3): 'dans Y; or, Y est un schéma local'",
           "comma after 'or' (enlarged crop p153_e.png)", "'or $Y$ est'", "punctuation", None, "high",
           r"~; or $Y$ est", r"~; or, $Y$ est"))
L.append(F(p, "'Le cas particulier suivant de (11.5.3) nous sera utile au chap. V :'",
           "ends with ' :' (enlarged crop p153_f.png)", "ends with '.'", "punctuation", None, "high",
           r"utile au chap.~V.", r"utile au chap.~V~:"))
L.append(F(p, "Corollaire (11.5.4): 'un morphisme propre de présentation finie'",
           "'propre' printed roman inside the italic statement (enlarged crop p153_f.png)",
           "italic", "convention", 6, "high",
           r"un morphisme propre de présentation finie, et", r"un morphisme \textup{propre} de présentation finie, et"))
L.append(F(p, "Corollaire (11.5.4): 'On suppose que θ : O_Y→f_*(O_X) soit injectif.'",
           "'soit injectif' (enlarged crop p153_f.png)", "'est injectif'", "word", None, "high",
           r"$ est injectif. Alors", r"$ soit injectif. Alors"))
L.append(F(p, "Proposition (11.5.5): 'faisant de A' une algèbre entière sur A'",
           "'entière' printed roman inside the italic statement (enlarged crop p153_g.png)",
           "italic", "convention", 6, "high",
           r"une algèbre entière sur", r"une algèbre \textup{entière} sur"))
L.append(F(p, "Proposition (11.5.5): 'si F' est f'-plat en tout point de X''",
           "'tout' printed roman inside the italic statement (enlarged crop p153_g.png)",
           "italic", "convention", 6, "high",
           r"-plat en<NL>tout point", r"-plat en<NL>\textup{tout} point"))
L.append(F(p, "proof of (11.5.5): 'une A-algèbre finie et de présentation finie;'",
           "'finie' and 'de présentation finie' italic, 'et' roman (enlarged crop p153_h.png)",
           "upright", "italics", None, "high",
           r"$A$-algèbre finie et de présentation finie~;", r"$A$-algèbre \emph{finie} et \emph{de présentation finie}~;"))
L.append(F(p, "proof of (11.5.5): 'le morphisme Y'→Y est propre (II, 6.1.11)'",
           "'propre' italic", "upright", "italics", None, "high",
           r"est propre (\textbf{II}, 6.1.11)", r"est \emph{propre} (\textbf{II}, 6.1.11)"))
L.append(F(p, "proof of (11.5.5): 'de ses sous-A-algèbres finies A'_λ'",
           "'finies' italic", "upright", "italics", None, "high",
           r"sous-$A$-algèbres finies", r"sous-$A$-algèbres \emph{finies}"))
L.append(F(p, "proof of (11.5.5.1): 'qui est un A-module libre'",
           "'libre' italic (enlarged crop p153_i.png)", "upright", "italics", None, "high",
           r"$A$-module libre, et", r"$A$-module \emph{libre}, et"))
L.append(F(p, "proof of (11.5.5.1): '(et a fortiori des A-modules de type fini)'",
           "'a fortiori' italic", "upright", "italics", None, "high",
           r"(et a<NL>fortiori", r"(et \emph{a<NL>fortiori}"))
L.append(F(p, "proof of (11.5.5.1): 'des A-modules de type fini)'",
           "'modules de type fini' italic (A- upright)", "upright", "italics", None, "high",
           r"$A$-modules de type fini)", r"$A$-\emph{modules de type fini})"))
L.append(F(p, "proof of (11.5.5.1): 'B/J_λ; or, B/J_λ est par définition'",
           "comma after 'or' (enlarged crop p153_i.png)", "'or $B/\\mathfrak J_\\lambda$'", "punctuation", None, "high",
           r"~; or $B/\mathfrak J_\lambda$", r"~; or, $B/\mathfrak J_\lambda$"))

# ---------------- page 154 ----------------
p = 154
L.append(F(p, "'il en est ainsi a fortiori de A→A'_λ pour tout λ.'",
           "no comma after A'_λ (enlarged crop p154_a.png)", "'$A\\to A'_{\\lambda}$, pour tout'",
           "punctuation", None, "high",
           r"$A\to A'_{\lambda}$, pour tout", r"$A\to A'_{\lambda}$ pour tout"))
L.append(F(p, "proof of (11.5.5.2): 'Considérons le schéma T = Spec(k(x))'",
           "bold italic k (enlarged crop p154_b.png)", "plain k(x)", "convention", 1, "high",
           r"\operatorname{Spec}(k(x))", r"\operatorname{Spec}(\boldsymbol{k}(x))"))
L.append(F(p, "proof of (11.5.5.2): 'aux parties fermées quasi-compactes T'_λ—V'_λ de T'_λ'",
           "long dash for set difference (enlarged crop p154_c.png)", "minus sign", "convention", 7, "high",
           r"T'_{\lambda}-V'_{\lambda}", r"T'_{\lambda}\setmin V'_{\lambda}",
           "Convention 7 (\\setmin, defined in the IV-3 preamble)."))
L.append(F(p, "heading 11.6",
           "'11.6. Descente de la platitude par des morphismes quelconques : cas d'un préschéma de base unibranche.' with a final full stop",
           "no full stop", "punctuation", None, "high",
           r"préschéma de base unibranche}", r"préschéma de base unibranche.}",
           "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop)."))
L.append(F(p, "proof of (11.6.1): step label 'I) Réduction au cas où A et A' sont des anneaux locaux intégralement clos.'",
           "'I)' in ordinary roman weight (enlarged crop p154_d.png)", "\\textbf{I)}", "font", None, "high",
           r"\noindent\textbf{I)} \emph{Réduction", r"\noindent I) \emph{Réduction",
           "As the p. 124 finding: ega4-11-fr.tex sets its step labels I)-VI) bold."))
L.append(F(p, "proof of (11.6.1): 'on peut donc supposer d'abord que A' est intègre.'",
           "'intègre' italic (enlarged crop p154_e.png)", "upright", "italics", None, "high",
           r"est intègre. Si", r"est \emph{intègre}. Si"))
L.append(F(p, "end of page_154.tex / top of p. 155: 'le même raisonnement que | précédemment permet de remplacer A' par B''",
           "p. 155 begins 'précédemment permet de remplacer A' par B'' flush left (page_155_s1.png, crop p155_top.png): the sentence continues; no paragraph break",
           "blank line after 'le même raisonnement que' and the comment line, before \\oldpage[IV-3]{155} (and another blank line after the marker, in page_155.tex): paragraph break mid-sentence",
           "marker", None, "high",
           r"raisonnement que<NL>% IV3_B23_P154_END<NL><NL>", r"raisonnement que<NL>% IV3_B23_P154_END<NL>",
           "Mid-sentence page break (GLOBAL_ISSUES 20); the p. 155 marker itself is in the right place. APPLY TOGETHER with the next entry (blank line after the marker, page_155.tex); either alone leaves the paragraph break."))
# outside the batch: page 155 part of the same break
L.append(F(155, "top of page_155.tex: blank line after \\oldpage[IV-3]{155}, before 'précédemment permet'",
           "p. 155 begins mid-sentence, flush left (continuation of 'le même raisonnement que' on p. 154)",
           "blank line after the marker: paragraph break mid-sentence", "marker", None, "high",
           r"\oldpage[IV-3]{155}<NL><NL>précédemment", r"\oldpage[IV-3]{155}<NL>précédemment",
           "OUTSIDE pp. 150-154: lies in page_155.tex (checked unique there); the pp. 155-159 checker may report the same edit; apply once. Apply together with the previous entry."))


def load(page):
    path = os.path.join(RUN, "page_%03d.tex" % page)
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
for d in L:
    fx = d["fix"]
    if fx is None:
        continue
    txt = load(d["page"])
    n = txt.count(fx["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE (%d) p%d: %r" % (n, d["page"], fx["old"]))
    if fx["old"] == fx["new"]:
        ok = False
        print("NO-OP p%d: %r" % (d["page"], fx["old"]))

# check that fixes on one page do not overlap in the text
from collections import defaultdict
spans = defaultdict(list)
for i, d in enumerate(L):
    fx = d["fix"]
    if fx is None:
        continue
    txt = load(d["page"])
    s = txt.find(fx["old"])
    spans[d["page"]].append((s, s + len(fx["old"]), i))
for pg, ss in spans.items():
    ss.sort()
    for a, b in zip(ss, ss[1:]):
        if a[1] > b[0]:
            ok = False
            print("OVERLAP p%d: #%d %r / #%d %r" % (pg, a[2], L[a[2]]["fix"]["old"], b[2], L[b[2]]["fix"]["old"]))

# simulate applying all fixes per page (in list order) to confirm each still applies
for pg in sorted(set(d["page"] for d in L)):
    txt = load(pg)
    for d in L:
        if d["page"] != pg or d["fix"] is None:
            continue
        old, new = d["fix"]["old"], d["fix"]["new"]
        if txt.count(old) != 1:
            ok = False
            print("SEQUENTIAL FAIL p%d: %r" % (pg, old))
        else:
            txt = txt.replace(old, new, 1)

from collections import Counter
c = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for pg in sorted(set(d["page"] for d in L)):
    print(pg, c[(pg, "normal")], c[(pg, "convention")], c[(pg, "misprint")])
print("total", len(L), "ok" if ok else "PROBLEMS")

if ok and "--write" in sys.argv:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(L, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("wrote", OUT)
