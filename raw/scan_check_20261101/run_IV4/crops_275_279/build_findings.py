"""Build findings_275_279.json. In old/new strings, the character U+23CE marks a line break (LF)."""
import json
import pathlib

R = pathlib.Path(__file__).resolve().parent.parent
NL = "⏎"
B = r"\boldsymbol{\mathsf{Y}}"
SANS = ("The print sets the Y of Y(C)/Y(D) as a heavy sans-serif capital (even strokes, no serifs; "
        "crops c277_2171a.png, c277_2171b.png, c277_2172.png, c278_cor3.png, c279_top.png, c279_OYD.png), "
        "while a bare Y (sous-préschéma fermé Y de X) is the ordinary roman Y. Written "
        r"\boldsymbol{\mathsf{Y}} as decided by the coordinator for pp. 260-267.")


def F(page, where, scan, tex, kind, fix, note="", conv=None, conf="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf}
    if fix is None:
        d["fix"] = None
    else:
        old, new = fix
        d["fix"] = {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


L = []
# ---------------------------------------------------------------- page 275 (page_275.tex)
L.append(F(275, "l. 2: 'un anneau de valuation discrète (II, 7.1.6), donc'",
           "one pair of parentheses around 'II, 7.1.6' (bold II)",
           r"(\sref[II]{II.7.1.6}): \sref prints its own parentheses, so the output is '((II, 7.1.6))'",
           "punctuation",
           (r"discrète (\sref[II]{II.7.1.6}), donc", r"discrète \sref[II]{II.7.1.6}, donc"),
           "GLOBAL_ISSUES 107 (ega4-21b line 223)."))
L.append(F(275, "proof of Corollaire (21.6.10), l. 1-2: 'par l'homomorphisme cyc : D(X) → 𝔜¹(X)'",
           "the print has D(X), not Div(X) (crop c275_cyc.png)",
           r"\operatorname{Div}(X): silent correction",
           "misprint_in_print",
           (r"l'homomorphisme $\operatorname{cyc}:\operatorname{Div}(X)\to\mathfrak{Z}^1(X)$ est $",
            r"l'homomorphisme $\operatorname{cyc}:D(X)\to\mathfrak{Z}^1(X)$ est $"),
           "The map cyc is defined on Div(X) (21.6.7, 21.6.9; the same proof writes Div(X)/Div.princ(X) "
           "one line below). The TeX silently corrects; the fix restores the printed reading.",
           corrected=r"\operatorname{cyc}:\operatorname{Div}(X)\to"))
L.append(F(275, "proof of (21.6.10), l. 3: '𝔜¹(X)/𝔜¹_princ(X) = Cl(X) déduit de cyc'",
           "roman 'Cl' (crop c275_Cl.png), where (21.6.10.1) on this page and (21.6.12.1) have the Fraktur ℭl",
           r"\mathfrak{Cl}(X): silent correction",
           "misprint_in_print",
           (r"=\mathfrak{Cl}(X)$ déduit de", r"=\mathrm{Cl}(X)$ déduit de"),
           "Wrong fount: the class group is ℭl(X) (Fraktur) everywhere else in 21.6. The fix restores the "
           "printed roman letters.",
           corrected=r"=\mathfrak{Cl}(X)"))
L.append(F(275, "end of the proof of (21.6.10): 'est bijectif (21.3.4, (ii)).'",
           "'(21.3.4, (ii))': the label inside the reference's parentheses",
           r"\sref{IV.21.3.4}, (ii) prints '(21.3.4), (ii)'",
           "punctuation",
           (r"\sref{IV.21.3.4}, (ii).", r"\sref{IV.21.3.4}[(ii)]."),
           "\\sref's third argument prints '(21.3.4, (ii))' (GLOBAL_ISSUES 68)."))
L.append(F(275, "Corollaire (21.6.10), l. 1: 'Soit X un préschéma localement noethérien normal.'",
           "'normal.' is roman inside the italic statement (crop c275_cor10.png)",
           "'normal' italic like the rest of the corollary",
           "convention",
           ("localement noethérien normal.", r"localement noethérien \textup{normal}."),
           "", conv=6))
L.append(F(275, "Corollaire (21.6.10): item labels (i), (ii)",
           "labels upright (crop c275_i.png; (ii) in page_275_s2.png)",
           "enumerate labels italic inside the italic corollary",
           "convention",
           (r"\begin{enumerate}[label=(\roman*)]" + NL + r"  \item Il existe",
            r"\begin{enumerate}[label=\textup{(\roman*)}]" + NL + r"  \item Il existe"),
           "GLOBAL_ISSUES 16; one edit covers both labels.", conv=6))
L.append(F(275, "proof of Corollaire (21.6.11): 'Tenant compte de (21.6.9, (ii)), la première assertion'",
           "'(21.6.9, (ii))'", r"\sref{IV.21.6.9}, (ii) prints '(21.6.9), (ii)'", "punctuation",
           (r"Tenant compte de \sref{IV.21.6.9}, (ii),", r"Tenant compte de \sref{IV.21.6.9}[(ii)],"),
           "GLOBAL_ISSUES 68."))
L.append(F(275, "Proposition (21.6.12), l. 2: 'Soit (U_λ)_{λ∈L} une famille filtrante décroissante'",
           "new indented paragraph after 'Soit X un préschéma noethérien réduit.' (crop c275_prop12.png)",
           "same paragraph (single line break)", "other",
           ("noethérien réduit." + NL + r"Soit $(U_\lambda)", "noethérien réduit." + NL + NL + r"Soit $(U_\lambda)"),
           "Inside the proposition environment, so the blank line gives the printed indent."))
L.append(F(275, "Proposition (21.6.12), condition 1°: 'Si Y_λ = X—U_λ'", "long dash for set difference",
           "minus sign", "convention",
           (r"$Y_\lambda=X-U_\lambda$", r"$Y_\lambda=X\setmin U_\lambda$"), "", conv=7))
L.append(F(275, "proof of (21.6.12), PRINTED ON P. 276 (in the p. 275 segment until marker 276 moves): "
                "'déterminée par sa rejtriction à chaque U_λ'",
           "'rejtriction' with a dotted j (crops c276_rejtr.png, c276_rejtr2.png)",
           "'restriction': silent correction", "misprint_in_print",
           ("par sa restriction à chaque", "par sa rejtriction à chaque"),
           "The fix restores the printed reading. The misprint is on printed p. 276; its text lies in the "
           "p. 275 segment of ega4-21b-fr.tex until the marker move below, so apply it before that move.",
           corrected="restriction"))
L.append(F(275, "page break 275/276: before 'Alors il existe des isomorphismes canoniques' (Proposition (21.6.12))",
           "printed p. 275 ends with condition 2° ('... l'anneau O_X,x est factoriel.'); p. 276 begins "
           "'Alors il existe des isomorphismes canoniques', indented as a new paragraph (page_275_s4.png, "
           "page_276_s1.png)",
           "\\oldpage[IV-4]{276} stands before 'Montrons d'abord ...', about 22 printed lines too late; "
           "'Alors' follows \\end{enumerate} without a blank line (no indent)",
           "marker",
           (r"\end{enumerate}" + NL + "Alors il existe des isomorphismes canoniques",
            r"\end{enumerate}" + NL + NL + r"\oldpage[IV-4]{276}" + NL + "Alors il existe des isomorphismes canoniques"),
           "MARKER 276 MOVES EARLIER. Part 1 of 2: inserts the marker at the printed page start, with the blank "
           "line before it that the printed paragraph indent needs (GLOBAL_ISSUES 80 pattern). Apply AFTER all "
           "other p. 275 edits (it ends the p. 275 segment here, and the 'rejtriction' edit lies after it); "
           "part 2 is the last p. 276 finding (removes the old marker). Until part 2 is applied the file has two "
           "\\oldpage[IV-4]{276} (apply_fixes.py then treats the span from the new one to marker 277 as page 276)."))
# ---------------------------------------------------------------- page 276 (page_276.tex)
L.append(F(276, "proof of (21.6.12): 'pour tout ouvert V⊃T, X—V est un sous-espace fermé'",
           "long dash for set difference", "minus sign", "convention",
           (r"$X-V$ est un sous-espace", r"$X\setmin V$ est un sous-espace"), "", conv=7))
L.append(F(276, "proof of (21.6.12): 'les ensembles (X—V)∩(X—U_λ)'", "two long dashes for set difference",
           "minus signs", "convention",
           (r"$(X-V)\cap(X-U_\lambda)$", r"$(X\setmin V)\cap(X\setmin U_\lambda)$"),
           "One edit for both dashes.", conv=7))
L.append(F(276, "proof of (21.6.12): 'sont fermés dans X—V, forment'", "long dash for set difference",
           "minus sign", "convention",
           (r"fermés dans $X-V$, forment", r"fermés dans $X\setmin V$, forment"), "", conv=7))
L.append(F(276, "proof of (21.6.12): 'ont pour réunion X—V, notre assertion'", "long dash for set difference",
           "minus sign", "convention",
           (r"réunion $X-V$, notre", r"réunion $X\setmin V$, notre"), "", conv=7))
L.append(F(276, "proof of (21.6.12): 'notre assertion résulte de (0_III, 9.2.4)'",
           "bold 0 with a light subscript III (crop c276_0III.png)",
           r"\sref[0]{0.9.2.4} prints '(0, 9.2.4)' without the subscript", "symbol",
           (r"résulte de \sref[0]{0.9.2.4}.", r"résulte de \sref[$\mathbf{0}_{\mathrm{III}}$]{0.9.2.4}."),
           "GLOBAL_ISSUES 108 form (as \\sref[$\\mathbf{0}_{\\mathrm I}$]). Independent of the dash edit "
           "before it (no overlap)."))
L.append(F(276, "proof of (21.6.12): 'on est donc ramené au cas où X = Spec(O_X,x); mais par hypothèse'",
           "no 'avec x∈T' here (crop c276_ramene.png); the words occur only in the parallel sentence on p. 277",
           "'... $X=\\Spec(\\sh{O}_{X,x})$ avec $x\\in T$;': words added", "extra",
           (r"$X=\Spec(\sh{O}_{X,x})$ avec $x\in T$;" + NL + "mais par hypothèse",
            r"$X=\Spec(\sh{O}_{X,x})$;" + NL + "mais par hypothèse"),
           "The TeX copied 'avec x∈T' from the p. 277 sentence (GLOBAL_ISSUES 46/102)."))
L.append(F(276, "proof of (21.6.12): 'donc la conclusion résulte de (21.6.9, (i)).'",
           "'(21.6.9, (i))' (crop c276_ramene.png)", r"\sref{IV.21.6.9}, (i) prints '(21.6.9), (i)'",
           "punctuation",
           (r"\sref{IV.21.6.9}, (i).", r"\sref{IV.21.6.9}[(i)]."), "GLOBAL_ISSUES 68."))
L.append(F(276, "old position of \\oldpage[IV-4]{276} (before 'Montrons d'abord', in the middle of printed p. 276)",
           "no page break there: 'Montrons d'abord' is a new paragraph in the middle of p. 276 (page_276_s3.png)",
           "\\oldpage[IV-4]{276}", "marker",
           (r"\oldpage[IV-4]{276}" + NL + "Montrons d'abord", "Montrons d'abord"),
           "Part 2 of 2 of the marker-276 move: apply after the last p. 275 finding (which inserts the new "
           "marker). The blank line before it stays (new paragraph in the print)."))
# ---------------------------------------------------------------- page 277 (page_277.tex)
L.append(F(277, "proof of (21.6.12), end: 'au cas où X = Spec(O_X,x) avec x∈T; mais comme O_X,x est factoriel'",
           "semicolon after 'x∈T' (crop c277_avec.png)", "comma", "punctuation",
           (r"avec $x\in T$, mais comme", r"avec $x\in T$; mais comme"), ""))
L.append(F(277, "proof of (21.6.12), last line: 'et il suffit d'appliquer (21.6.9, (ii)).'",
           "'(21.6.9, (ii))' (crop c277_avec.png)", r"\sref{IV.21.6.9}, (ii) prints '(21.6.9), (ii)'",
           "punctuation",
           (r"\sref{IV.21.6.9}, (ii).", r"\sref{IV.21.6.9}[(ii)]."), "GLOBAL_ISSUES 68. Independent of the "
           "semicolon edit on the same line (no overlap)."))
L.append(F(277, "Corollaire (21.6.13): 'U = X—{a}'", "long dash for set difference", "minus sign",
           "convention", (r"$U=X-\{a\}$." + NL + "Pour que", r"$U=X\setmin\{a\}$." + NL + "Pour que"), "", conv=7))
L.append(F(277, "Corollaire (21.6.14): 'U = X—{a}'", "long dash for set difference (crop c277_cor14.png)",
           "minus sign", "convention",
           (r"$U=X-\{a\}$." + NL + "Les conditions", r"$U=X\setmin\{a\}$." + NL + "Les conditions"), "", conv=7))
L.append(F(277, "Corollaire (21.6.14) b): '(conditions que nous exprimerons plus loin (21.13) en disant que "
                "l'anneau A est parafactoriel)'",
           "the parenthesis is roman with upright parentheses; only 'parafactoriel' is italic (crop c277_cor14.png)",
           "the parenthesis italic, 'parafactoriel' upright (\\emph inside the italic corollary)", "convention",
           ("(conditions que nous exprimerons plus loin \\sref{IV.21.13} en disant que l'anneau $A$ est "
            r"\emph{parafactoriel})",
            r"\textup{(conditions que nous exprimerons plus loin \sref{IV.21.13} en disant que l'anneau $A$ est "
            r"\emph{parafactoriel})}"),
           "Inside \\textup the \\emph gives the printed italic 'parafactoriel'.", conv=6))
L.append(F(277, "proof of (21.6.14), l. 1-2: 'puisque dim(A) ⩾ 2 (0, 16.5.1) et (21.6.13) montre que'",
           "no comma after (0, 16.5.1) (crop c277_proof14.png)", "comma before 'et'", "punctuation",
           (r"\sref[0]{0.16.5.1}, et \sref{IV.21.6.13}", r"\sref[0]{0.16.5.1} et \sref{IV.21.6.13}"), ""))
L.append(F(277, "heading of 21.7: '21.7. Interprétation des cycles positifs 1-codimensionnels en termes de "
                "sous-préschémas.'",
           "the title ends with a full stop (crop c277_head.png)", "no full stop in the \\subsection title",
           "punctuation",
           ("en termes de sous-préschémas}", "en termes de sous-préschémas.}"),
           "Same form as the 21.1 and 21.2 titles (findings_255_259.json; GLOBAL_ISSUES 43/58)."))
L.append(F(277, "(21.7.1), l. 1: 'C = Σ n_x.{x}-bar'",
           "baseline period between n_x and the barred {x} (measured: its bottom on the baseline of the x)",
           r"\cdot (centred dot)", "symbol",
           (r"$C=\sum_{x\in X^{(1)}}n_x\cdot\overline{\{x\}}$", r"$C=\sum_{x\in X^{(1)}}n_x.\overline{\{x\}}$"),
           "Same treatment as the p.1 baseline periods (GLOBAL_ISSUES 65; IV-2 p. 75)."))
L.append(F(277, "(21.7.1), l. 2: 'un cycle 1-codimensionnel positif (de sorte que'",
           "'cycle 1-codimensionnel positif' italic (crop c277_2171a.png)", "upright", "italics",
           (r"un cycle $1$-codimensionnel positif (de sorte", r"un \emph{cycle $1$-codimensionnel positif} (de sorte"),
           "Independent of the preceding edit (no overlap)."))
L.append(F(277, "(21.7.1): 'Désignons par Y(C)'", "sans-serif Y", "$Y(C)$", "font",
           ("Désignons par $Y(C)$", "Désignons par $" + B + "(C)$"), SANS))
L.append(F(277, "(21.7.1): 'image fermée (I, 9.5.3 et 9.5.1) du préschéma somme'",
           "one pair of parentheses, bold I, and both numbers are EGA I's (crop c277_2171b.png)",
           r"(\sref[I]{I.9.5.3} et \sref{IV.9.5.1}) prints '((I, 9.5.3) et (9.5.1))', and links 9.5.1 to EGA IV",
           "punctuation",
           (r"(\sref[I]{I.9.5.3} et \sref{IV.9.5.1})",
            r"(\textbf{I}, \EGAUnavailableHyperref{I.9.5.3}{9.5.3} et \EGAUnavailableHyperref{I.9.5.1}{9.5.1})"),
           "GLOBAL_ISSUES 107 (ega4-21b line 358). The 9.5.1 is EGA I's: the proof of (21.7.2) cites the same "
           "definition as '(I, 9.5.1)'. Form as ega4-20 line 737 '(\\textbf{I}, \\EGAUnavailableHyperref{I.5.2.1}"
           "{5.2.1} et ...)'."))
L.append(F(277, "(21.7.1): 'du préschéma somme Y'(C) = ∐ Spec(...)'", "sans-serif Y", "$Y'(C)$", "font",
           (r"$Y'(C)=\coprod", "$" + B + r"'(C)=\coprod"), SANS))
L.append(F(277, "(21.7.1), end: 'l'Idéal de O_X définissant Y(C).'", "sans-serif Y", "$Y(C)$", "font",
           ("définissant $Y(C)$.", "définissant $" + B + "(C)$."),
           SANS + " The script letter of J_X(C), J(C) on this line is the script J (descender), as in the TeX."))
L.append(F(277, "Proposition (21.7.2), l. 2: 'soit de la forme Y(C), où C est'", "sans-serif Y (crop c277_2172.png)",
           "$Y(C)$", "font",
           ("soit de la forme $Y(C)$, où", "soit de la forme $" + B + "(C)$, où"), SANS))
L.append(F(277, "Proposition (21.7.2): item labels (i) (p. 277) and (ii) (p. 278)",
           "labels upright (crops c277_2172.png, c278_top.png)",
           "enumerate labels italic inside the italic proposition", "convention",
           (r"\begin{enumerate}[label=(\roman*)]" + NL + r"  \item $Y$ est purement",
            r"\begin{enumerate}[label=\textup{(\roman*)}]" + NL + r"  \item $Y$ est purement"),
           "GLOBAL_ISSUES 16; one edit covers both labels.", conv=6))
L.append(F(277, "page break 276/277 inside 'il y a un voisinage W(x) | de x dans X et un diviseur D^(x)'",
           "printed p. 276 ends with 'il y a un voisinage W(x)'; p. 277 begins 'de x dans X et un diviseur D(x) "
           "sur W(x)' at the left margin (page_276_s4.png, page_277_s1.png)",
           "\\oldpage[IV-4]{277} stands before 'Pour prouver que l'homomorphisme', two printed lines too early",
           "marker",
           (r"il y a un voisinage $W(x)$ de $x$ dans $X$ et un diviseur",
            r"il y a un voisinage $W(x)$" + NL + r"\oldpage[IV-4]{277}" + NL + r"de $x$ dans $X$ et un diviseur"),
           "MARKER 277 MOVES LATER. Part 1 of 2: inserts the marker at the printed break (mid-sentence: no blank "
           "lines). Part 2 (next finding) removes the old marker; apply this one first. Until part 2 is applied "
           "the file has two \\oldpage[IV-4]{277}."))
L.append(F(277, "old position of \\oldpage[IV-4]{277} (before 'Pour prouver que l'homomorphisme', printed on p. 276)",
           "no page break there: 'Pour prouver' is a new paragraph two lines above the foot of p. 276",
           "\\oldpage[IV-4]{277}", "marker",
           (r"\oldpage[IV-4]{277}" + NL + "Pour prouver", "Pour prouver"),
           "Part 2 of 2 of the marker-277 move: apply after the preceding finding (and after all other p. 277 "
           "edits). The blank line before it stays (new paragraph in the print)."))
# ---------------------------------------------------------------- page 278 (page_278.tex)
L.append(F(278, "Proposition (21.7.2), after the items: 'On a alors'",
           "new indented paragraph (crop c278_top.png)", "follows \\end{enumerate} without a blank line (no indent)",
           "other",
           (r"\end{enumerate}" + NL + "On a alors", r"\end{enumerate}" + NL + NL + "On a alors"),
           "GLOBAL_ISSUES 80 pattern."))
L.append(F(278, "Proposition (21.7.2), after (21.7.2.1): 'L'application C ⇝ Y(C) est une bijection'",
           "wavy arrow (crop c278_top.png)", r"\mapsto", "symbol",
           (r"$C\mapsto Y(C)$", r"$C\leadsto" + B + "(C)$"),
           "GLOBAL_ISSUES 33/107. One edit for this finding and the next (sans-serif Y)."))
L.append(F(278, "same formula: 'C ⇝ Y(C)'", "sans-serif Y", "$Y(C)$", "font", None,
           "Covered by the edit of the preceding entry. " + SANS))
L.append(F(278, "Proposition (21.7.2), end: 'vérifiant les conditions (i) et (ii).'",
           "(i) and (ii) upright with upright parentheses; 'et' italic (crop c278_top.png)",
           "all italic", "convention",
           ("vérifiant les conditions (i) et (ii)." + NL + r"\end{proposition}",
            r"vérifiant les conditions \textup{(i)} et \textup{(ii)}." + NL + r"\end{proposition}"),
           "", conv=6))
L.append(F(278, "proof of (21.7.2), l. 3: 'on a alors Y(C) = Spec(A/𝔍)'", "sans-serif Y (crop c278_nec.png)",
           "$Y(C)$", "font",
           ("on a alors $Y(C)=", "on a alors $" + B + "(C)="), SANS))
L.append(F(278, "proof of (21.7.2), l. 3: 'par définition (I, 9.5.1) le noyau'",
           "no comma after the reference (crop c278_nec.png)", "comma", "punctuation",
           (r"\sref[I]{I.9.5.1}, le noyau", r"\sref[I]{I.9.5.1} le noyau"), ""))
L.append(F(278, "proof of (21.7.2), l. 4: 'A → ⊕_i A_{p_i}/p_i^{ni} A_{p_i}'",
           "exponent printed 'ni' on one level: the i is not lowered (6x crop c278_pini2.png), while the "
           "A_{p_i} beside it has a lowered second-order i",
           r"\mathfrak{p}_i^{n_i}: silent correction", "misprint_in_print",
           (r"/\mathfrak{p}_i^{n_i}A", r"/\mathfrak{p}_i^{ni}A"),
           "Flat second-order index, recorded as a misprint as in run_I_b p. 142 and run_IV3 p. 158. The same "
           "setting recurs twice below (two more entries).", conf="medium", corrected=r"\mathfrak{p}_i^{n_i}"))
L.append(F(278, "proof of (21.7.2), l. 5: 'aux points x∈X^(1) pour lesquels n_x ⩾ 0'",
           "'n_x ⩾ 0' (crop c278_nx.png), the same sign as 'n_x ⩾ 0' in (21.7.1)",
           "'n_x>0': silent correction", "misprint_in_print",
           (r"pour lesquels $n_x>0$", r"pour lesquels $n_x\geq0$"),
           "Misprint: the p_i must be the primes with n_x > 0 (for n_x = 0 the preimage of p^0A_p is A, not "
           "p-primary, and the p_i are said to be the minimal primes of A/𝔍). The TeX silently corrects; the fix "
           "restores the printed reading.", corrected=r"pour lesquels $n_x>0$"))
L.append(F(278, "proof of (21.7.2), l. 6: 'L'image réciproque q_i de p_i^{ni} A_{p_i}'",
           "exponent printed 'ni' on one level (crop c278_pini3.png)",
           r"\mathfrak{p}_i^{n_i}: silent correction", "misprint_in_print",
           (r"de $\mathfrak{p}_i^{n_i}A", r"de $\mathfrak{p}_i^{ni}A"),
           "As the first 'ni' above.", conf="medium", corrected=r"\mathfrak{p}_i^{n_i}"))
L.append(F(278, "proof of (21.7.2), second paragraph: 'Les conditions sont suffisantes; désignant par 𝒥'",
           "semicolon and lower-case 'désignant' (crop c278_Jdesig.png)",
           "full stop and 'Désignant' (a new sentence)", "punctuation",
           ("Les conditions sont suffisantes." + NL + "Désignant par",
            "Les conditions sont suffisantes;" + NL + "désignant par"),
           "The script letters 𝒥 of this paragraph are script J (descender), as in the TeX."))
L.append(F(278, "proof of (21.7.2): 'par suite les idéaux primaires ≠ 0 de cet anneau'",
           "'≠0' (crop c278_ne0.png)", "'non nuls' (reworded)", "word",
           ("les idéaux primaires non nuls de cet anneau", r"les idéaux primaires $\neq0$ de cet anneau"),
           "GLOBAL_ISSUES 46/102 (rewording)."))
L.append(F(278, "proof of (21.7.2): 'on en conclut que 𝒥 = 𝔍~, où 𝔍 = ⋂_i q_i'",
           "the second 𝔍 has no tilde (crop c278_Jtilde.png)", r"où $\widetilde{\mathfrak{J}}=\bigcap_i\mathfrak{q}_i$",
           "formula",
           (r"où $\widetilde{\mathfrak{J}}=\bigcap_i", r"où $\mathfrak{J}=\bigcap_i"),
           "The print defines the ideal 𝔍 of A; the TeX's tilde makes the sheaf equal to an intersection of ideals."))
L.append(F(278, "proof of (21.7.2): 'les images réciproques dans A d'idéaux p_i^{ni} A_{p_i}'",
           "exponent printed 'ni' on one level (crop c278_pini4.png)",
           r"\mathfrak{p}_i^{n_i}: silent correction", "misprint_in_print",
           (r"d'idéaux $\mathfrak{p}_i^{n_i}A", r"d'idéaux $\mathfrak{p}_i^{ni}A"),
           "As the first 'ni' above.", conf="medium", corrected=r"\mathfrak{p}_i^{n_i}"))
L.append(F(278, "proof of (21.7.2), last line: 'Y est de la forme Y(C).'",
           "sans-serif Y in Y(C); the bare Y before it is roman (crop c278_formeY.png)", "$Y(C)$", "font",
           ("de la forme $Y(C)$." + NL + r"\end{proof}", "de la forme $" + B + "(C)$." + NL + r"\end{proof}"), SANS))
L.append(F(278, "Corollaire (21.7.3), l. 2-3: 'du sous-préschéma fermé Y(D) (21.2.12), Y(D) majore le "
                "sous-préschéma fermé Y(cyc(D))'",
           "three sans-serif Y (crop c278_cor3.png)", "$Y(D)$, $Y(D)$, $Y(\\operatorname{cyc}(D))$", "font",
           (r"fermé $Y(D)$ \sref{IV.21.2.12}, $Y(D)$ majore le sous-préschéma fermé $Y(\operatorname{cyc}(D))$",
            "fermé $" + B + r"(D)$ \sref{IV.21.2.12}, $" + B + r"(D)$ majore le sous-préschéma fermé $" + B
            + r"(\operatorname{cyc}(D))$"),
           SANS + " One edit for three occurrences. Apply before the misprint entry that follows (same line, no "
           "overlap)."))
L.append(F(278, "Corollaire (21.7.3), l. 3: 'Y(cyc(D)) (21.7.1). et a même espace sous-jacent'",
           "a full stop after (21.7.1), then lower-case 'et' (5x crop c278_period.png; compare the comma after "
           "(21.2.12) one line above, c278_comma_ref.png)",
           "', et': silent correction", "misprint_in_print",
           (r"\sref{IV.21.7.1}, et a même", r"\sref{IV.21.7.1}. et a même"),
           "Misprint (full stop for a comma). The TeX silently corrects; the fix restores the printed reading. "
           "Listed after the Y(D) edit of the same line.", corrected=r"\sref{IV.21.7.1}, et a même"))
L.append(F(278, "Corollaire (21.7.3), l. 4: 'il suffit que Y(D) vérifie la condition (S_1)'", "sans-serif Y",
           "$Y(D)$", "font", ("il suffit que $Y(D)$ vérifie", "il suffit que $" + B + "(D)$ vérifie"), SANS))
L.append(F(278, "Corollaire (21.7.3), l. 5: 'pour tout z∈Y(D) distinct d'un point maximal de Y(D)'",
           "two sans-serif Y", "$Y(D)$ twice", "font",
           (r"pour tout $z\in Y(D)$ distinct d'un point maximal de $Y(D)$",
            r"pour tout $z\in" + B + "(D)$ distinct d'un point maximal de $" + B + "(D)$"),
           SANS + " One edit for two occurrences."))
L.append(F(278, "Corollaire (21.7.3), end: '(condition toujours vérifiée lorsque X est normal).'",
           "the parenthesis is roman with upright parentheses; only 'normal' is italic (crop c278_cor3.png)",
           "the parenthesis italic, 'normal' upright (\\emph inside the italic corollary)", "convention",
           (r"(condition toujours vérifiée lorsque $X$ est \emph{normal})",
            r"\textup{(condition toujours vérifiée lorsque $X$ est \emph{normal})}"), "", conv=6))
L.append(F(278, "proof of (21.7.3), l. 1: 'on peut toujours supposer que ℐ_X(D) = tO_X'",
           "script I: the letter sits on the base line, no descender (4x crop c278_JXD1.png; compare the script J "
           "of 𝒥_X(cyc(D)) two lines below, c278_JXD2.png)",
           r"\sh{J}_X(D)", "symbol",
           (r"supposer que $\sh{J}_X(D)=t\sh{O}_X$", r"supposer que $\sh{I}_X(D)=t\sh{O}_X$"),
           "Script I of the Idéal I_X(D) of a divisor (21.2), as on pp. 260-262; the script J is kept for J_X(C) "
           "of a cycle (21.7.1)."))
L.append(F(278, "proof of (21.7.3), l. 2: 'en tout point maximal x de Y(D)'", "sans-serif Y (crop c278_proof3.png)",
           "$Y(D)$", "font",
           ("point maximal $x$ de $Y(D)$", "point maximal $x$ de $" + B + "(D)$"), SANS))
L.append(F(278, "proof of (21.7.3), l. 4: 't_x O_X,x = 𝔪_x^{n_x}, où n_x = mult_x(D)'",
           "comma before 'où' (crop c278_proof3.png)", "no comma", "punctuation",
           (r"=\mathfrak{m}_x^{n_x}$ où $n_x", r"=\mathfrak{m}_x^{n_x}$, où $n_x"), ""))
L.append(F(278, "proof of (21.7.3), l. 5: 'si 𝒥_X(cyc(D)) = 𝔍~, ℐ_X(D) = 𝔍~', il résulte de ce qui précède et de "
                "(21.7.1) que 𝔍 et 𝔍' ont'",
           "two formulas, the second with the script I (no descender) and a tilde over 𝔍 only, the prime after it; "
           "then 'que 𝔍 et 𝔍' ont' (crops c278_proof3.png, c278_JXD2.png)",
           "the formula 'ℐ_X(D) = 𝔍~'' is missing, and the TeX writes '$\\mathfrak{J}=tA$ et "
           "$\\widetilde{\\mathfrak{J}}$' for the print's '𝔍 et 𝔍''", "word",
           (r"=\widetilde{\mathfrak{J}}$, il résulte de ce qui précède et de \sref{IV.21.7.1} que $\mathfrak{J}=tA$ "
            r"et $\widetilde{\mathfrak{J}}$ ont",
            r"=\widetilde{\mathfrak{J}}$, $\sh{I}_X(D)=\widetilde{\mathfrak{J}}'$, il résulte de ce qui précède et "
            r"de \sref{IV.21.7.1} que $\mathfrak{J}$ et $\mathfrak{J}'$ ont"),
           "Rewording (GLOBAL_ISSUES 46/102): the TeX renamed the print's 𝔍', 𝔍 as 𝔍 = tA and \\widetilde{𝔍}. "
           "Part 1 of 3 edits of this sentence (the next two follow; no overlaps). The 𝒥 of 𝒥_X(cyc(D)) is "
           "a script J in the print and stays \\sh{J}."))
L.append(F(278, "proof of (21.7.3), l. 6: 'ont mêmes idéaux primaires non immergés'",
           "'mêmes' italic too (crop c278_memes.png)", "\\emph starts after 'mêmes'", "italics",
           (r"mêmes \emph{idéaux primaires non immergés}", r"\emph{mêmes idéaux primaires non immergés}"),
           "Part 2 of 3 edits of this sentence."))
L.append(F(278, "proof of (21.7.3), l. 6: 'donc 𝔍' ⊂ 𝔍, puisque 𝔍 est l'intersection'",
           "'𝔍' ⊂ 𝔍' and '𝔍 est l'intersection' (crop c278_proof3.png)",
           "'$\\widetilde{\\mathfrak{J}}\\subset\\mathfrak{J}$, puisque $\\widetilde{\\mathfrak{J}}$ est': with "
           "the renamed letters this states the inclusion the wrong way round (\\widetilde{𝔍} ⊂ tA)", "word",
           (r"donc $\widetilde{\mathfrak{J}}\subset\mathfrak{J}$, puisque $\widetilde{\mathfrak{J}}$ est l'intersection",
            r"donc $\mathfrak{J}'\subset\mathfrak{J}$, puisque $\mathfrak{J}$ est l'intersection"),
           "Part 3 of 3 edits of this sentence (rewording, GLOBAL_ISSUES 46/102)."))
# ---------------------------------------------------------------- page 279 (page_279.tex)
L.append(F(279, "l. 1: 'Cela prouve que Y(D) majore Y(cyc(D))'", "two sans-serif Y (crop c279_top.png)",
           "$Y(D)$, $Y(\\operatorname{cyc}(D))$", "font",
           (r"Cela prouve que $Y(D)$ majore $Y(\operatorname{cyc}(D))$",
            "Cela prouve que $" + B + "(D)$ majore $" + B + r"(\operatorname{cyc}(D))$"),
           SANS + " One edit for two occurrences."))
L.append(F(279, "l. 2: 'si et seulement si Y(D) n'a pas de cycle premier'", "sans-serif Y", "$Y(D)$", "font",
           ("si et seulement si $Y(D)$", "si et seulement si $" + B + "(D)$"), SANS))
L.append(F(279, "l. 3: 'Comme pour tout x∈Y(D)'", "sans-serif Y", "$Y(D)$", "font",
           (r"Comme pour tout $x\in Y(D)$", r"Comme pour tout $x\in" + B + "(D)$"), SANS))
L.append(F(279, "l. 5: 'O_{Y(D)}|(U∩Y(D)) soit restriction à Y(D)∩U'",
           "three sans-serif Y, including the subscript of O_Y(D) (crop c279_OYD.png)", "$Y(D)$ three times",
           "font",
           (r"$\sh{O}_{Y(D)}|(U\cap Y(D))$ soit restriction à $Y(D)\cap U$",
            r"$\sh{O}_{" + B + r"(D)}|(U\cap" + B + "(D))$ soit restriction à $" + B + r"(D)\cap U$"),
           SANS + " One edit for three occurrences."))
L.append(F(279, "l. 5: 'dire que Y(D) vérifie (S_1)'", "sans-serif Y", "$Y(D)$", "font",
           ("dire que $Y(D)$ vérifie", "dire que $" + B + "(D)$ vérifie"), SANS))
L.append(F(279, "l. 6: 'en tout point z∈Y(D) non maximal'", "sans-serif Y", "$Y(D)$", "font",
           (r"en tout point $z\in Y(D)$ non maximal", r"en tout point $z\in" + B + "(D)$ non maximal"), SANS))
L.append(F(279, "l. 8: 'aux points non maximaux z de Y(D) on a'", "sans-serif Y", "$Y(D)$", "font",
           ("non maximaux $z$ de $Y(D)$", "non maximaux $z$ de $" + B + "(D)$"), SANS))
L.append(F(279, "Proposition (21.7.4) b): 'cyc : Div(X) → 𝔜¹(X) est bijectif'",
           "the Fraktur Z carries a bar beneath it, printed as dark as the type and exactly the letter's width "
           "(crop c279_Zbar.png, ink map); no other 𝔜 on pp. 275-279 has it, e.g. the same formula on the last "
           "lines of the page (c279_Z2.png)",
           r"\mathfrak{Z}^1(X): silent correction", "misprint_in_print",
           (r"$X$ est normal et l'homomorphisme $\operatorname{cyc}:\operatorname{Div}(X)\to\mathfrak{Z}^1(X)$ est bijectif.",
            r"$X$ est normal et l'homomorphisme $\operatorname{cyc}:\operatorname{Div}(X)\to\underline{\mathfrak{Z}}^1(X)$ est bijectif."),
           "A wrong or damaged sort (an underlined 𝔜) in the small type of (21.7.4); no mathematical meaning. "
           "If the coordinator judges the bar a stray mark (physical defect) rather than a printed sort, drop "
           "this entry.", conf="low", corrected=r"\to\mathfrak{Z}^1(X)$ est bijectif."))
L.append(F(279, "proof of (21.7.4), second paragraph, l. 1: 'et montrons d'abord que X est normal.'",
           "'normal' italic (crop c279_normal.png)", "upright", "italics",
           ("montrons d'abord que $X$ est normal.", r"montrons d'abord que $X$ est \emph{normal}."), ""))
L.append(F(279, "proof of (21.7.4): 'au moins un diviseur ≠ 0, autrement dit'",
           "'≠0' (page_279_s3.png, line 9)", "'non nul' (reworded)", "word",
           ("au moins un diviseur non nul,", r"au moins un diviseur $\neq0$,"), "GLOBAL_ISSUES 46/102 (rewording)."))
L.append(F(279, "proof of (21.7.4): 'que X est réduit (5.8.5)'", "'réduit' italic (crop c279_reduit.png)",
           "upright", "italics",
           (r"que $X$ est réduit \sref{IV.5.8.5}", r"que $X$ est \emph{réduit} \sref{IV.5.8.5}"), ""))
L.append(F(279, "proof of (21.7.4): 'l'ouvert U = X_1—{x}'", "long dash for set difference (crop c279_X1x.png)",
           "minus sign", "convention", (r"$U=X_1-\{x\}$", r"$U=X_1\setmin\{x\}$"), "", conv=7))

out = R / "findings_275_279.json"
out.write_text(json.dumps(L, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", out, len(L))
