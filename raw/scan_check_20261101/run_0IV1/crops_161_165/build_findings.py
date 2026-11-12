# -*- coding: utf-8 -*-
"""Build findings_161_165.json for run_0IV1 (EGA 0_IV-1 pp. 161-165) and validate every fix against page_NNN.tex.
The pilcrow character stands for a line break (LF) in old/new strings."""
import json
import pathlib

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_161_165.json"
P = "¶"
F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace(P, "\n"), "new": new.replace(P, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 161
add(161, "first line",
    "de sorte que l'on a la suite exacte (lower-case d: the sentence runs on from the display (21.3.2.4) on p. 160)",
    "De sorte que l'on a la suite exacte", "word", None, "high",
    r"De sorte que l'on a", r"de sorte que l'on a",
    "Capital D where the print continues the sentence.")
add(161, "parenthesis after (21.3.2.5)",
    "puisque Θ_{B/A} et π_{B/A} dépendent non seulement de A et de B",
    r"puisque $\Theta_{B/A}$ et $\Xi_{B/A}$ dépendent", "formula", None, "high",
    r"et $\Xi_{B/A}$ dépendent", r"et $\pi_{B/A}$ dépendent",
    "Wrong letter: the print names π_{B/A}, not Ξ_{B/A}.")
add(161, "(21.3.3), first line", "(21.3.3) Comme en vertu de (21.3.1.2), on a F_B = i∘j",
    r"Comme, en vertu de (21.3.1.2)", "punctuation", None, "high",
    r"Comme, en vertu", r"Comme en vertu", "No comma after 'Comme' in the print.")
add(161, "display (21.3.3.1)", "M^(p) = M⊗_B B^(p) = (M⊗_B A_[j])⊗_A B_[i] (no punctuation after the display)",
    r"\otimes_A B_{[i]}, (comma)", "punctuation", None, "high",
    r"\otimes_A B_{[i]},¶\end{equation}¶d'où", r"\otimes_A B_{[i]}¶\end{equation}¶d'où",
    "Extra comma after the display.")
add(161, "display (21.3.3.2)", "(Ω^1_{B/A})^(p) = Θ_{B/A}⊗_A B_[i] (no punctuation after the display)",
    r"=\Theta_{B/A}\otimes_A B_{[i]}, (comma)", "punctuation", None, "high",
    r"=\Theta_{B/A}\otimes_A B_{[i]},", r"=\Theta_{B/A}\otimes_A B_{[i]}",
    "Extra comma after the display.")
add(161, "after (21.3.3.2)", "et on déduit donc de (21.3.2.2)", "et l'on déduit donc de (21.3.2.2)",
    "word", None, "high", r"et l'on déduit donc", r"et on déduit donc", "The print has 'et on'.")
add(161, "after (21.3.3.2)", "un homomorphisme canonique de B-modules: 'homomorphisme canonique de' and '-modules' italic",
    r"un homomorphisme canonique de $B$-modules (upright)", "italics", None, "high",
    r"un homomorphisme canonique de $B$-modules", r"un \emph{homomorphisme canonique de $B$-modules}",
    "Printed italic.")
add(161, "after display (21.3.3.3)", "'Compte tenu de (20.5.4.2), ...' begins a new indented paragraph",
    r"\end{equation} followed directly by 'Compte tenu de' (no paragraph break)", "other", None, "high",
    r"\end{equation}¶Compte tenu de (20.5.4.2)", r"\end{equation}¶¶Compte tenu de (20.5.4.2)",
    "Missing paragraph break after a display (cf. GLOBAL_ISSUES 47).")
add(161, "after (21.3.3.3)", "est le B-module engendré par les éléments d_A(j(b))⊗1: 'engendré par les éléments' italic",
    "engendré par les éléments (upright)", "italics", None, "high",
    r"engendré par les éléments $d_A(j(b))", r"\emph{engendré par les éléments} $d_A(j(b))",
    "Printed italic.")
add(161, "before (21.3.3.4)", "cette image est nulle: 'nulle' italic", "cette image est nulle (upright)", "italics",
    None, "high", r"cette image est nulle", r"cette image est \emph{nulle}", "Printed italic.")
add(161, "after (21.3.3.4)", "le composé de deux homomorphismes consécutifs est nul.: 'nul' italic", "est nul. (upright)",
    "italics", None, "high", r"consécutifs est nul.", r"consécutifs est \emph{nul}.", "Printed italic.")
add(161, "after the proof of (21.3.4)",
    "'La proposition (21.3.4) s'applique ...' begins a new indented paragraph after 'Cela résulte de la définition de la platitude.'",
    "same paragraph", "other", None, "high", r"la platitude. La", r"la platitude.¶¶La", "Missing paragraph break.")
add(161, "after the proof of (21.3.4)", "La proposition (21.3.4) s'applique en particulier",
    "La proposition s'applique en particulier", "missing", None, "high",
    r"proposition s'applique en", r"proposition (21.3.4) s'applique en", "Reference '(21.3.4)' missing.")
add(161, "after the proof of (21.3.4)", "lorsque l'on a B^p⊂A⊂B, i et j étant respectivement",
    r"lorsque $B^p\subset A\subset B$", "missing", None, "high",
    r"lorsque $B^p\subset A\subset B$", r"lorsque l'on a $B^p\subset A\subset B$", "Words 'l'on a' missing.")
add(161, "after the proof of (21.3.4)", "et que B admet une p-base sur A: 'p-base' italic",
    r"admet une $p$-base sur $A$ (upright)", "italics", None, "high",
    r"admet une $p$-base sur $A$", r"admet une \emph{$p$-base} sur $A$", "Printed italic.")

# ---------------------------------------------------------------- page 162
add(162, "top of page_162.tex (marker {162})",
    "printed p. 161 ends '... d'autre part, l'image de d_A(y_μ) par i_{B/A}'; p. 162 begins 'est d_B(y_μ), et comme les y_μ et les x_λ ...'",
    r"\oldpage[0\textsubscript{IV-1}]{162} stands before 'Comme $B$ est réduit', the opening of the proof of (21.3.5), whose first eight printed lines are on p. 161",
    "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{162}¶Comme", r"Comme",
    "Move, part 1 of 2: removes the marker here; the marker finding at the printed page break (same page file) re-inserts it after 'par $i_{B/A}$'. Apply both or neither. The text findings for that opening passage are filed under p. 162 because the passage is in page_162.tex.")
add(162, "proof of (21.3.5), first line (printed p. 161)", "x⇝x^p (wavy arrow)", r"$x\mapsto x^p$", "symbol", None,
    "high", r"$x\mapsto x^p$", r"$x\rightsquigarrow x^p$",
    "Wavy maps-to arrow (earlier page fixes write \\leadsto; ega0-21-fr.tex already writes \\rightsquigarrow at its line 466). Not convention 3: the printed arrow is not plain.")
add(162, "proof of (21.3.5) (printed p. 161)",
    "est un isomorphisme de B sur B^p, et par transport de structure ('isomorphisme' italic)",
    r"est un isomorphisme de structure de $B$ sur $B^p$~; par transport de structure", "word", None, "high",
    r"est un isomorphisme de structure de¶$B$ sur $B^p$~; par transport",
    r"est un \emph{isomorphisme} de¶$B$ sur $B^p$, et par transport",
    "The TeX adds 'de structure', sets 'isomorphisme' upright and has '~;' where the print has ', et'.")
add(162, "proof of (21.3.5) (printed p. 161)",
    "on voit que (x_λ^p)_{λ∈L} est une p-base de B^p sur A^p; on en conclut que les x_λ^p et les y_μ forment une p-base de A sur A^p (21.1.10); par suite (21.1.5, (ii) et 21.2.5) les d_A(x_λ^p) ... (italic: 'p-base'; 'p-base de', 'sur')",
    r"on voit que $(x_\lambda^p)_{\lambda\in L}$ et les $y_\mu$ forment une $p$-base de $B^p$ sur $A^p$ (21.1.10)~; on en conclut par (21.1.5), (ii), et (21.2.5) que les ...",
    "word", None, "high",
    r"on voit que $(x_\lambda^p)_{\lambda\in L}$ et les $y_\mu$ forment une $p$-base¶de $B^p$ sur $A^p$ (21.1.10)~; on en conclut par (21.1.5), (ii), et (21.2.5)¶que les",
    r"on voit que $(x_\lambda^p)_{\lambda\in L}$ est une \emph{$p$-base}¶de $B^p$ sur $A^p$~; on en conclut que les $x_\lambda^p$ et les $y_\mu$ forment¶une \emph{$p$-base de} $A$ \emph{sur} $A^p$ (21.1.10)~; par suite (21.1.5, (ii) et¶21.2.5) les",
    "Paraphrase: the TeX merges two printed statements into 'les x_λ^p et les y_μ forment une p-base de B^p sur A^p' (the y_μ need not lie in B^p) and rewrites the citation. Restores the printed sentence and its italics.")
add(162, "proof of (21.3.5) (printed p. 161)",
    "forment une base du A-module Ω^1_A; donc les d_A(x_λ^p)⊗1 et les d_A(y_μ)⊗1 forment une base du B-module Ω^1_A⊗_A B. Or, l'image ('base' italic the first time)",
    r"forment une base du $A$-module $\Omega^1_A$. Or l'image", "missing", None, "high",
    r"forment une base du¶$A$-module $\Omega^1_A$. Or l'image",
    r"forment une \emph{base} du¶$A$-module $\Omega^1_A$~; donc les $d_A(x_\lambda^p)\otimes1$ et les $d_A(y_\mu)\otimes1$¶forment une base du $B$-module $\Omega^1_A\otimes_A B$. Or, l'image",
    "Clause 'donc les ... forment une base du B-module Ω^1_A⊗_A B' missing; also italic 'base', ';' for the full stop, comma after 'Or'.")
add(162, "proof of (21.3.5): printed page break 161/162",
    "p. 161 ends '... l'image de d_A(y_μ) par i_{B/A}'; p. 162 begins 'est d_B(y_μ)'", "no marker here", "marker",
    None, "high",
    r"par $i_{B/A}$ est $d_B", r"par $i_{B/A}$¶\oldpage[0\textsubscript{IV-1}]{162}¶est $d_B",
    "Move, part 2 of 2: inserts the marker where p. 162 begins (mid-sentence: no blank lines); the finding at the top of page_162.tex removes the old marker. Apply both or neither.")
add(162, "top of printed p. 162", "est d_B(y_μ), et comme", r"est $d_B(i(y_\mu))$, et comme", "formula", None, "high",
    r"(i(y_\mu))$, et comme", r"(y_\mu)$, et comme", "The print has d_B(y_μ), without i.")
add(162, "proof of (21.3.5), p. 162 lines 1-3",
    "les d_B(y_μ) sont linéairement indépendants (sur B) dans Ω^1_B (21.2.5); on en déduit aussitôt que le noyau de i_{B/A} a une base formée des d_A(x_λ^p)⊗1; ('linéairement indépendants' italic)",
    r"les $d_B(y_\mu)$ sont une partie d'une base de $\Omega^1_B$ (21.2.5), donc sont linéairement indépendants sur $B$. On en déduit que le noyau de $i_{B/A}$ a pour base les $d_A(x_\lambda^p)\otimes1$~;",
    "word", None, "high",
    r"les $d_B(y_\mu)$ sont une¶partie d'une base de $\Omega^1_B$ (21.2.5), donc sont linéairement indépendants¶sur $B$. On en déduit que le noyau de $i_{B/A}$ a pour base les¶$d_A(x_\lambda^p)\otimes1$~;",
    r"les $d_B(y_\mu)$ sont¶\emph{linéairement indépendants} (sur $B$) dans $\Omega^1_B$ (21.2.5)~; on en déduit aussitôt¶que le noyau de $i_{B/A}$ a une base formée des¶$d_A(x_\lambda^p)\otimes1$~;",
    "Paraphrase; restores the printed wording and italics.")
add(162, "proof of (21.3.5), p. 162 lines 3-5",
    "comme ce sont les images par (21.3.5.1) des éléments d_{B/A}(x_λ)⊗1 dans Ω^1_{B/A}⊗_B B^(p), et que ces derniers forment une base du B-module Ω^1_{B/A}⊗_B B^(p) (21.2.5)",
    r"des éléments correspondants de $(\Omega^1_{B/A})^{(p)}$, et que ces derniers forment une base du $B$-module $(\Omega^1_{B/A})^{(p)}$ (21.2.5)",
    "formula", None, "high",
    r"éléments correspondants de $(\Omega^1_{B/A})^{(p)}$, et que ces derniers¶forment une base du $B$-module $(\Omega^1_{B/A})^{(p)}$ (21.2.5),",
    r"éléments $d_{B/A}(x_\lambda)\otimes1$ dans $\Omega^1_{B/A}\otimes_B B^{(p)}$, et que ces derniers¶forment une base du $B$-module $\Omega^1_{B/A}\otimes_B B^{(p)}$ (21.2.5),",
    "Paraphrase; restores the printed elements and modules.")
add(162, "Remarques (21.3.6) (i)", "et supposons que l'on ait deux homomorphismes i' : A'→B', j' : B'→A'",
    "supposons donnés deux homomorphismes", "word", None, "high",
    r"supposons donnés deux homomorphismes", r"supposons que l'on ait deux homomorphismes",
    "Reworded in the TeX.")
add(162, "Remarques (21.3.6) (i)", "(21.3.1.2), et des homomorphismes d'anneaux f : A→A', g : B→B'",
    "(21.3.1.2), ainsi que des homomorphismes d'anneaux", "word", None, "high",
    r"ainsi que des homomorphismes d'anneaux", r"et des homomorphismes d'anneaux", "Reworded in the TeX.")
add(162, "Remarques (21.3.6) (i), first diagram", "bottom row A → B → A: the labels i and j stand below the arrows",
    r"A\ar[u]^f\ar[r]^i&B\ar[u]^g\ar[r]^j&A (labels above)", "formula", None, "high",
    r"\ar[r]^i&B\ar[u]^g\ar[r]^j&A", r"\ar[r]_i&B\ar[u]^g\ar[r]_j&A",
    "Label side only; f, g (left of the vertical arrows) and i', j' (above) match.")
add(162, "Remarques (21.3.6) (i), after the first diagram",
    "'Alors l'homomorphisme canonique ...' begins a new indented paragraph", r"no blank line after \]", "other",
    None, "high", r"  \]¶  Alors l'homomorphisme canonique", r"  \]¶¶  Alors l'homomorphisme canonique",
    "Missing paragraph break after a display (cf. GLOBAL_ISSUES 47).")
add(162, "Remarques (21.3.6) (i), second diagram",
    "bottom row: the label π_{B'/A'} stands below the arrow Θ_{B'/A'} → Ω^1_{A'}",
    r"\ar[r]^{\pi_{B'/A'}} (label above)", "formula", None, "high",
    r"\ar[r]^{\pi_{B'/A'}}", r"\ar[r]_{\pi_{B'/A'}}",
    "Label side only (π_{B/A} in the top row is above, as in the TeX).")
add(162, "Remarques (21.3.6) (ii)", "Soit A' une A-algèbre quelconque, et posons", "quelconque et posons",
    "punctuation", None, "high", r"quelconque et posons", r"quelconque, et posons", "Comma missing.")
add(162, "Remarques (21.3.6) (ii)",
    "et l'on a / [centred unnumbered display] Ω^1_{B'/A'} = Ω^1_{B/A}⊗_A A' = Ω^1_{B/A}⊗_B B' / (20.5.5); on en déduit (at the margin)",
    "the formula is set in the running text", "formula", None, "high",
    r"et l'on a¶  $\Omega^1_{B'/A'}=\Omega^1_{B/A}\otimes_A A'=\Omega^1_{B/A}\otimes_B B'$¶  (20.5.5)",
    r"et l'on a¶  \[¶  \Omega^1_{B'/A'}=\Omega^1_{B/A}\otimes_A A'=\Omega^1_{B/A}\otimes_B B'¶  \]¶  (20.5.5)",
    "The print displays this formula.")
add(162, "Remarques (21.3.6) (ii)", "on en déduit un A'-isomorphisme canonique ('isomorphisme canonique' italic)",
    r"un $A'$-isomorphisme canonique (upright)", "italics", None, "high",
    r"un $A'$-isomorphisme canonique", r"un $A'$-\emph{isomorphisme canonique}",
    "Printed italic in the roman remark (judged as if the remark body were roman).")
add(162, "Remarques (21.3.6) (ii)", "et aussi un B'-homomorphisme canonique ('homomorphisme canonique' italic)",
    r"un $B'$-homomorphisme canonique (upright)", "italics", None, "high",
    r"un $B'$-homomorphisme canonique", r"un $B'$-\emph{homomorphisme canonique}",
    "Printed italic in the roman remark.")
add(162, "heading 21.4", "21.4. Cas des extensions de corps.", r"\subsection{Cas des extensions de corps}",
    "punctuation", None, "high",
    r"\subsection{Cas des extensions de corps}", r"\subsection{Cas des extensions de corps.}",
    "Printed final full stop (GLOBAL_ISSUES 43/58; page-fixed like the other 0_IV subsection titles).")
add(162, "proof of Lemme (21.4.1) (printed p. 163)",
    "printed p. 162 ends with the statement of Lemme (21.4.1); p. 163 begins with its proof 'En effet, x est racine du polynôme ...'",
    "the p. 163 marker stands before Corollaire (21.4.4): the proof of (21.4.1), Théorème (21.4.2) and Corollaire (21.4.3) with their proofs lie in the page-162 segment",
    "marker", None, "high",
    r"\begin{proof}¶En effet, $x$ est racine", r"\oldpage[0\textsubscript{IV-1}]{163}¶\begin{proof}¶En effet, $x$ est racine",
    "Move, part 1 of 2: inserts the p. 163 marker before the proof of (21.4.1); the page-163 marker finding removes the old marker. Apply both or neither. The next four findings (printed p. 163) are filed under p. 162 because their text is in page_162.tex.")
add(162, "proof of Lemme (21.4.1) (printed p. 163)", "X^p — x^p (long dash)", r"$X^p-x^p$", "convention", 7, "high",
    r"$X^p-x^p$", r"$X^p\setmin x^p$",
    "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier page fixes, pending the convention-7 decision (\\setmin is not yet defined in the IV1 preamble).")
add(162, "proof of Lemme (21.4.1) (printed p. 163)", "chap. V, § 8, nº 1, prop. 1 (raised letter o)", r"n$^\circ$~1",
    "symbol", None, "medium", r"n$^\circ$~1", r"n\textsuperscript{o}~1",
    "The print has a raised letter o (the edition's n\\textsuperscript{o}); n$^\\circ$ typesets a ring.")
add(162, "proof of Théorème (21.4.2) (printed p. 163)", "p-libre sur k et maximale parmi les parties de S ('maximale' italic)",
    "et maximale parmi (upright)", "italics", None, "high", r"et maximale parmi", r"et \emph{maximale} parmi",
    "Printed italic.")
add(162, "end of the proof of Théorème (21.4.2) (printed p. 163)", "s'obtient en prenant L = ø, S = K. C.Q.F.D.",
    r"$L=\varnothing$, $S=K$. (no C.Q.F.D.)", "missing", None, "high",
    r"$L=\varnothing$, $S=K$.", r"$L=\varnothing$, $S=K$. C.Q.F.D.", "'C.Q.F.D.' missing.")

# ---------------------------------------------------------------- page 163
add(163, "top of page_163.tex (marker {163})",
    "p. 163 begins with the proof of (21.4.1); Corollaire (21.4.4) stands in the middle of the page",
    r"\oldpage[0\textsubscript{IV-1}]{163} before \begin{corollary}[21.4.4]", "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{163}¶\begin{corollary}[21.4.4]", r"\begin{corollary}[21.4.4]",
    "Removes the old marker; apply only together with the page-162 marker finding that re-inserts it before the proof of (21.4.1).")
add(163, "proof of Corollaire (21.4.4)", "les d_{K/k}(x_α) forment une base du K-espace vectoriel Ω^1_{K/k} (21.2.5)",
    "forment une base de l'espace vectoriel", "word", None, "high",
    r"forment une base de l'espace vectoriel $\Omega^1_{K/k}$", r"forment une base du $K$-espace vectoriel $\Omega^1_{K/k}$",
    "Reworded in the TeX.")
for old, new, w in [(r"(resp. une famille de", r"(\textup{resp.} une famille de", "first"),
                    (r"resp. une $p$-base", r"\textup{resp.} une $p$-base", "second"),
                    (r"(resp. un système de", r"(\textup{resp.} un système de", "third"),
                    (r"resp. une base)", r"\textup{resp.} une base)", "fourth")]:
    add(163, f"Théorème (21.4.5), {w} 'resp.'", "'resp.' printed upright in the italic statement",
        "resp. inside the theorem environment (italic)", "convention", 6, "high", old, new,
        "Roman word inside an italic statement.")
add(163, "Théorème (21.4.5), end", "dans le K-espace vectoriel Ω^1_{K/k}", "dans l'espace vectoriel", "word", None, "high",
    r"dans l'espace vectoriel $\Omega^1_{K/k}$.", r"dans le $K$-espace vectoriel $\Omega^1_{K/k}$.",
    "Reworded in the TeX.")
add(163, "proof of Théorème (21.4.5) (bottom of p. 163)",
    "Soit K' le sous-corps (égal au sous-anneau) de K engendré par k(K^p) et les x_α; compte tenu de (20.4.7), on voit que les d_{K'/k}(x_α) engendrent Ω^1_{K'/k(K^p)} = Ω^1_{K'/k}. Si les d_{K/k}(x_α) engendrent Ω^1_{K/k} = Ω^1_{K/k(K^p)}, la flèche de gauche dans la suite exacte (20.5.7.1) [display] Ω^1_{K'/k(K^p)}⊗_{K'}K → Ω^1_{K/k(K^p)} → Ω^1_{K/K'} → 0 est surjective, donc Ω^1_{K/K'} = 0, ce qui implique K' = K par (21.4.4). [new paragraph] Si maintenant (x_α) est une famille p-libre, elle est une sous-famille d'une p-base de K sur k (21.4.2), donc les d_{K/k}(x_α) font partie d'une base du K-espace vectoriel Ω^1_{K/k} (21.2.5), et sont par suite linéairement indépendants sur K. Prouvons réciproquement que si les d_{K/k}(x_α) sont linéairement indépendants sur K, la famille (x_α) est p-libre sur k.",
    r"the page-163 segment ends with \begin{proof}; this text is missing (the TeX's proof, in the page-164 segment, has only the opening 'Soit K' ... et les x_α;' joined to p. 164's 'compte tenu de (21.4.3)', and a reworded 'Si maintenant ...' paragraph at its end)",
    "missing", None, "high",
    r"\end{theorem}¶¶\begin{proof}",
    r"\end{theorem}¶¶\begin{proof}¶Soit $K'$ le sous-corps (égal au sous-anneau) de $K$ engendré par¶$k(K^p)$ et les $x_\alpha$~; compte tenu de (20.4.7), on voit que les¶$d_{K'/k}(x_\alpha)$ engendrent $\Omega^1_{K'/k(K^p)}=\Omega^1_{K'/k}$. Si les¶$d_{K/k}(x_\alpha)$ engendrent $\Omega^1_{K/k}=\Omega^1_{K/k(K^p)}$, la flèche de¶gauche dans la suite exacte (20.5.7.1)¶\[¶\Omega^1_{K'/k(K^p)}\otimes_{K'}K\to\Omega^1_{K/k(K^p)}\to\Omega^1_{K/K'}\to0¶\]¶est surjective, donc $\Omega^1_{K/K'}=0$, ce qui implique $K'=K$ par (21.4.4).¶¶Si maintenant $(x_\alpha)$ est une famille $p$-libre, elle est une sous-famille¶d'une $p$-base de $K$ sur $k$ (21.4.2), donc les $d_{K/k}(x_\alpha)$ font partie¶d'une base du $K$-espace vectoriel $\Omega^1_{K/k}$ (21.2.5), et sont par suite¶linéairement indépendants sur $K$. Prouvons réciproquement que si les¶$d_{K/k}(x_\alpha)$ sont linéairement indépendants sur $K$, la famille¶$(x_\alpha)$ est $p$-libre sur $k$.",
    "Text move with restoration, part 1 of 3: apply together with the page-164 marker finding (deletes the TeX's opening 'Soit K' ... ; compte tenu de (21.4.3)' -> 'Compte tenu de (21.4.3)') and the page-164 'extra' finding (deletes the TeX's 'Si maintenant ...' paragraph). The p. 164 marker then stands before 'Compte tenu de (21.4.3)', where the printed page begins mid-paragraph.")

# ---------------------------------------------------------------- page 164
add(164, "top of page_164.tex (marker {164})",
    "p. 164 begins 'Compte tenu de (21.4.3), il suffit de voir que, ...' at the margin (the paragraph runs on from p. 163)",
    r"marker followed by 'Soit $K'$ le sous-corps ... et les $x_\alpha$~; compte tenu de (21.4.3)'", "marker", None, "high",
    r"Soit $K'$ le sous-corps (égal au sous-anneau) de $K$ engendré par¶$k(K^p)$ et les $x_\alpha$~; compte tenu de (21.4.3)",
    r"Compte tenu de (21.4.3)",
    "Text move, part 2 of 3: 'Soit K' ... et les x_α;' is printed on p. 163, where it continues 'compte tenu de (20.4.7), on voit que ...'; the page-163 'missing' finding restores it there. Apply together with that finding and the 'extra' finding at the end of this proof.")
add(164, "display in the proof of (21.4.5)", "Ω^1_{K_α/k(K^p)}⊗_{K_α}K → Ω^1_{K/k(K^p)} → Ω^1_{K/K_α} → 0 (no punctuation)",
    r"\longrightarrow0, (comma)", "punctuation", None, "high",
    r"\Omega^1_{K/K_\alpha}\longrightarrow0,", r"\Omega^1_{K/K_\alpha}\longrightarrow0",
    "Extra comma after the display.")
add(164, "proof of (21.4.5), after the display",
    "ne contenant pas d_{K/k}(x_α), et comme ce sous-espace vectoriel est le noyau de la flèche de droite",
    r"ne contenant pas $d_{K/k}(x_\alpha)$~; comme ce sous-espace est le noyau", "word", None, "high",
    r"$d_{K/k}(x_\alpha)$~; comme¶ce sous-espace est le noyau",
    r"$d_{K/k}(x_\alpha)$, et comme¶ce sous-espace vectoriel est le noyau",
    "'~; comme' for ', et comme'; 'vectoriel' missing.")
add(164, "end of the proof of (21.4.5)",
    "the proof ends '... on voit que d_{K/K_α}(x_α) ≠ 0, donc x_α∉K_α.'; the paragraph 'Si maintenant (x_α) est une famille p-libre, ...' is printed on p. 163, before 'Compte tenu de (21.4.3)'",
    "after 'x_α∉K_α.' a paragraph 'Si maintenant ... Réciproquement, si les d_{K/k}(x_α) sont linéairement indépendants sur K, les deux paragraphes précédents montrent que (x_α) est p-libre sur k.'",
    "extra", None, "high",
    r"donc $x_\alpha\notin K_\alpha$.¶¶Si maintenant $(x_\alpha)$ est une famille $p$-libre, elle est une sous-famille¶d'une $p$-base de $K$ sur $k$ (21.4.2)~; les $d_{K/k}(x_\alpha)$ font donc¶partie d'une base de l'espace vectoriel $\Omega^1_{K/k}$ (21.2.5), et sont¶par suite linéairement indépendants sur $K$. Réciproquement, si les¶$d_{K/k}(x_\alpha)$ sont linéairement indépendants sur $K$, les deux¶paragraphes précédents montrent que $(x_\alpha)$ est $p$-libre sur $k$.¶\end{proof}",
    r"donc $x_\alpha\notin K_\alpha$.¶\end{proof}",
    "Text move, part 3 of 3: deletes the TeX's reworded, displaced copy (its last sentence has no counterpart in the print); the printed paragraph, ending 'Prouvons réciproquement que si ..., la famille (x_α) est p-libre sur k.', is restored on p. 163 by the page-163 'missing' finding. Apply together.")
for lab, rest in [("a", r" $x\notin k(K^p)$."), ("b", r" $d_{K/k}(x)\neq0$."), ("c", r" L'élément")]:
    add(164, f"Corollaire (21.4.6), label {lab})", f"label {lab}) printed upright",
        f"\\item[{lab})] (italic in the corollary environment)", "convention", 6, "high",
        f"\\item[{lab})]" + rest, f"\\item[\\textup{{{lab})}}]" + rest,
        "Roman label inside an italic statement (cf. GLOBAL_ISSUES 16).")
add(164, "Proposition (21.4.7)", "Alors la suite de L-espaces vectoriels", r"Alors la suite d'espaces vectoriels sur $L$",
    "word", None, "high", r"la suite d'espaces vectoriels sur $L$", r"la suite de $L$-espaces vectoriels",
    "Reworded in the TeX.")
add(164, "Proposition (21.4.8)", "les éléments d_K(x_λ^p)⊗1 forment une base du L-espace vectoriel Υ_{L/K}",
    "forment une base de l'espace vectoriel", "word", None, "high",
    r"forment une base de l'espace vectoriel $\Upsilon_{L/K}$", r"forment une base du $L$-espace vectoriel $\Upsilon_{L/K}$",
    "Reworded in the TeX.")
add(164, "heading 21.5", "21.5. Application : critères de séparabilité.",
    r"\subsection{Application~: critères de séparabilité}", "punctuation", None, "high",
    r"\subsection{Application~: critères de séparabilité}", r"\subsection{Application~: critères de séparabilité.}",
    "Printed final full stop (GLOBAL_ISSUES 43/58).")
add(164, "introduction of 21.5", "Dans ce numéro et les deux suivants, on ne suppose plus que ('on ne suppose plus' italic)",
    "on ne suppose plus (upright)", "italics", None, "high",
    r"on ne suppose plus que", r"\emph{on ne suppose plus} que", "Printed italic.")
add(164, "(21.5.1)", "chap. V, § 8, nº 2, prop. 3 (raised letter o)", r"n$^\circ$~2", "symbol", None, "medium",
    r"n$^\circ$~2", r"n\textsuperscript{o}~2", "As on p. 163: raised letter o, the edition's n\\textsuperscript{o}.")
add(164, "(21.5.1)", "prop. 3) que dans une clôture algébrique de K", r"prop.~3) que, dans une", "punctuation", None,
    "high", r"que, dans une", r"que dans une", "No comma after 'que' in the print.")
add(164, "(21.5.1), last line", "par l'isomorphisme x⇝x^p (wavy arrow)", r"$x\mapsto x^p$", "symbol", None, "high",
    r"$x\mapsto x^p$", r"$x\rightsquigarrow x^p$", "Wavy arrow as in the proof of (21.3.5); not convention 3.")

# ---------------------------------------------------------------- page 165
add(165, "Proposition (21.5.2) b)", "et que w_0 = w⊗1 soit égal à σ", r"$w_0=w\otimes1:L\to L'$ soit égal à $\sigma$",
    "extra", None, "high", r"$w_0=w\otimes1:L\to L'$", r"$w_0=w\otimes1$",
    "The print has no ': L→L'' in b) (b') has ': L→L').")
add(165, "Proposition (21.5.2), after the list", "'Alors on a les implications ...' is an indented paragraph after item c')",
    r"\end{enumerate} followed by ' Alors' without a blank line (no indent)", "other", None, "medium",
    r"\end{enumerate}¶ Alors on a", r"\end{enumerate}¶¶ Alors on a",
    "Paragraph after the list, indented as printed.")
add(165, "Proposition (21.5.2)", "Alors on a les implications c)⇔c')⇔a)⇒b)⇒b'): the labels are upright in the italic statement",
    r"$c)\Leftrightarrow c')\Leftrightarrow a)\Rightarrow b)\Rightarrow b')$ (math-italic letters)", "convention", 6,
    "high",
    r"$c)\Leftrightarrow c')\Leftrightarrow a)\Rightarrow b)¶ \Rightarrow b')$",
    r"$\mathrm{c})\Leftrightarrow\mathrm{c}')\Leftrightarrow\mathrm{a})\Rightarrow\mathrm{b})¶ \Rightarrow\mathrm{b}')$",
    "Roman labels inside an italic statement (in the roman proof the print sets them italic, as the TeX does).")
add(165, "Proposition (21.5.2), last sentence",
    "'Si de plus A est un anneau de Cohen, les cinq conditions précédentes sont équivalentes.' is a separate indented paragraph",
    "same paragraph as 'Alors on a les implications ...'", "other", None, "high",
    r". Si de plus $A$", r".¶¶Si de plus $A$", "Missing paragraph break.")
add(165, "proof of (21.5.2), a) ⇒ b)", "B est un A-module plat (0_I, 6.3.4) ('plat' italic)", "plat (upright)", "italics",
    None, "high", r"un $A$-module plat", r"un $A$-module \emph{plat}", "Printed italic.")
add(165, "proof of (21.5.2), a) ⇒ b)", "(0_I, 6.3.4) with a bold 0", r"(0$_{\rm I}$, 6.3.4)", "convention", 2, "high",
    r"(0$_{\rm I}$, 6.3.4)", r"($\mathbf{0}_{\mathrm I}$, 6.3.4)", "Bold 0, written as in the earlier page fixes.")
add(165, "proof of (21.5.2), a) ⇒ b)", "donc une A-algèbre de Cohen (19.8.1) ('algèbre de Cohen' italic)",
    r"$A$-algèbre de Cohen (upright)", "italics", None, "high",
    r"$A$-algèbre de Cohen (19.8.1)", r"$A$-\emph{algèbre de Cohen} (19.8.1)", "Printed italic.")
add(165, "proof of (21.5.2), a) ⇒ b)", "conséquence de (19.8.2, (i)) appliqué à C = B'", "appliquée à", "word", None,
    "high", r"appliquée à", r"appliqué à", "Printed 'appliqué'.")
add(165, "proof of (21.5.2), a) ⇒ b)", "appliqué à C = B', 𝔍 = n'", r"$G=B'$", "formula", None, "high",
    r"$G=B'$", r"$C=B'$",
    "Wrong letter: the print has C, the C of (19.8.2, (i)) (which the TeX of (19.8.2) also writes C).")
add(165, "proof of (21.5.2), a) ⇒ c)", "en prenant cette fois C = B/n^2", r"$G=B/\mathfrak n^2$", "formula", None, "high",
    r"$G=B/\mathfrak n^2$", r"$C=B/\mathfrak n^2$", "Wrong letter: C.")
add(165, "proof of (21.5.2), a) ⇒ c)", "C étant considéré comme A-algèbre pour u'_1", r"$G$ étant considéré", "formula",
    None, "high", r"$G$ étant considéré", r"$C$ étant considéré", "Wrong letter: C.")
add(165, "proof of (21.5.2), a) ⇒ b)", "étant le composé B→B/n →σ B'/n' (σ over the second arrow)",
    r"$B\to B/\mathfrak n\to B'/\mathfrak n'$", "formula", None, "high",
    r"$B\to B/\mathfrak n\to B'/\mathfrak n'$", r"$B\to B/\mathfrak n\xrightarrow{\sigma}B'/\mathfrak n'$",
    "Arrow label σ missing.")
add(165, "proof of (21.5.2), c') ⇒ a)", "'Prouvons en second lieu que c') implique a).' begins a new indented paragraph",
    "same paragraph", "other", None, "high",
    r"pour $u'_1$.¶Prouvons en second lieu", r"pour $u'_1$.¶¶Prouvons en second lieu", "Missing paragraph break.")
add(165, "proof of (21.5.2), c') ⇒ a)", "w_1 est donc de la forme z⇝z + D'(z)", r"$x\mapsto x+D'(x)$", "formula", None,
    "high", r"$x\mapsto x+D'(x)$", r"$z\rightsquigarrow z+D'(z)$",
    "Letter z, not x, and the wavy arrow (not convention 3).")
add(165, "proof of (21.5.2), c') ⇒ a)", "une dérivation de L dans L ('de' and 'dans' italic)",
    r"une dérivation de $L$ dans $L$ (upright)", "italics", None, "high",
    r"une dérivation de $L$ dans $L$", r"une dérivation \emph{de} $L$ \emph{dans} $L$", "Printed italic.")
add(165, "proof of (21.5.2), c') ⇒ a)", "signifie que D' prolonge D ('prolonge' italic)", "prolonge (upright)", "italics",
    None, "high", r"que $D'$ prolonge $D$", r"que $D'$ \emph{prolonge} $D$", "Printed italic.")
add(165, "proof of (21.5.2), c') ⇒ a)", "Notons d'autre part que toute dérivation D de K dans L ('toute' italic)",
    "toute (upright)", "italics", None, "high",
    r"que toute dérivation $D$", r"que \emph{toute} dérivation $D$", "Printed italic.")
add(165, "proof of (21.5.2), b') ⇒ c')", "'Prouvons enfin que, lorsque A est un anneau de Cohen, ...' begins a new indented paragraph",
    "same paragraph", "other", None, "high",
    r"séparable sur $K$.¶Prouvons enfin", r"séparable sur $K$.¶¶Prouvons enfin", "Missing paragraph break.")
add(165, "proof of (21.5.2), b') ⇒ c')", "qui vérifie les hypothèses de b') et, par passage aux quotients, donne u'_1",
    "et qui, par passage aux quotients", "extra", None, "high",
    r"et qui, par passage", r"et, par passage", "Extra 'qui'.")

# ---------------------------------------------------------------- validate
pages = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8") for n in range(161, 166)}
bad = 0
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    c = pages[f["page"]].count(f["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", i, f["page"], c, repr(f["fix"]["old"][:80]))
# sequential application per page: every old must still occur exactly once when its turn comes
applied = dict(pages)
for i, f in enumerate(F):
    if f["fix"] is None:
        continue
    t = applied[f["page"]]
    c = t.count(f["fix"]["old"])
    if c != 1:
        bad += 1
        print("SEQUENTIAL PROBLEM", i, f["page"], c, repr(f["fix"]["old"][:80]))
    applied[f["page"]] = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(pathlib.Path(__file__).resolve().parent / "simulated_after_fixes.txt").write_text(
    "".join(applied[n].split("\n", 1)[1] for n in range(161, 166)), encoding="utf-8")
counts = {}
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("findings:", len(F), "problems:", bad)
for n in sorted(counts):
    print(n, counts[n])
