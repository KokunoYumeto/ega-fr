"""Write findings_025_029.json for EGA IV-3 pp. 25-29 and check that every fix's old string occurs exactly once
in its page_NNN.tex (CRLF normalised to LF). The placeholder ¶ stands for a line break in old/new/corrected."""
import json
import pathlib
from collections import Counter

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_025_029.json"
F = []


def nl(s):
    return None if s is None else s.replace("¶", "\n")


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=nl(old), new=nl(new)))
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- p. 24 (where p. 25 begins)
add(24, "end of p. 24, just before the p. 25 marker: 'et l'on a un diagramme commutatif' + the diagram (8.5.10.2) that opens p. 25",
    "the sentence runs on into the diagram (8.5.10.2) at the top of p. 25; no paragraph break",
    r"blank line between 'commutatif' and \oldpage[IV-3]{25} (ega4-8-fr.tex line 1705): a paragraph break before the display",
    "marker", None, "high",
    r"l'on a un diagramme¶commutatif¶¶", r"l'on a un diagramme¶commutatif¶",
    note="Reported by the pp. 25-29 checker (where p. 25 begins). The edit lies at the end of page 24's segment, "
         "just before \\oldpage[IV-3]{25}: mid-sentence page break with a blank line (GLOBAL_ISSUES 20).")

# ---------------------------------------------------------------- p. 25
add(25, "Proposition (8.5.11), l. 1: 'Supposons S_0 quasi-compact (resp. quasi-compact et quasi-séparé).'",
    "'(resp.' and the closing parenthesis upright inside the italic statement",
    "the whole parenthesis italic (proposition environment)", "convention", 6, "high",
    r"quasi-compact (resp. quasi-compact et quasi-séparé).",
    r"quasi-compact \textup{(resp.} quasi-compact et quasi-séparé\textup{)}.")
add(25, "Proposition (8.5.11), l. 2: 'quasi-cohérent de type fini (resp. de présentation finie) pour tout λ'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"de type fini (resp. de présentation finie)¶pour tout",
    r"de type fini \textup{(resp.} de présentation finie\textup{)}¶pour tout")
add(25, "Proposition (8.5.11), l. 3: 'alors l'application canonique (8.5.10.1) est injective'",
    "reference (8.5.10.1) upright", "italic", "convention", 6, "high",
    r"canonique (8.5.10.1) est", r"canonique \textup{(8.5.10.1)} est")
add(25, "Proposition (8.5.11), end: 'est injective (resp. bijective).'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"injective¶(resp. bijective).", r"injective¶\textup{(resp.} bijective\textup{)}.")
add(25, "heading 8.6: 'Sous-préschémas de présentation finie d'une limite projective de préschémas.'",
    "the title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"d'une limite projective de préschémas}", r"d'une limite projective de préschémas.}",
    note="Same for 8.7 and 8.8 on pp. 27-28 (GLOBAL_ISSUES 43).")
add(25, "(8.6.1), l. 2: 'des sous-préschémas de Y qui sont de présentation finie sur Y (1.6.1)'",
    "'de présentation finie' italic", "upright", "italics", None, "high",
    r"qui sont de présentation finie sur $Y$ (1.6.1)", r"qui sont \emph{de présentation finie} sur $Y$ (1.6.1)")
add(25, "(8.6.1), l. 2: 'l'ensemble ordonné (I, 4.1.10)'", "bold I", "plain I", "convention", 2, "high",
    r"ordonné (I, 4.1.10)", r"ordonné (\textbf{I}, 4.1.10)")
add(25, "(8.6.1): 'et que l'espace sous-jacent Z est rétrocompact dans Y'",
    "'rétro-compact' italic (hyphenated at the line end)", "upright", "italics", None, "high",
    r"est rétrocompact dans", r"est \emph{rétrocompact} dans")
add(25, "(8.6.1): 'l'idéal 𝒥 de 𝒪_Y qui le définit est de type fini, ce qui signifie'",
    "'de type fini' italic", "upright", "italics", None, "high",
    r"qui le définit est de type fini,", r"qui le définit est \emph{de type fini},")
add(25, "(8.6.2): 'il est induit sur un ouvert (resp. il est fermé) si Y_λ l'est (I, 4.3.2)'",
    "bold I", "plain I", "convention", 2, "high",
    r"l'est (I, 4.3.2)", r"l'est (\textbf{I}, 4.3.2)")
add(25, "(8.6.2): '(𝔖𝔭𝔯𝔣(S_λ), u_λμ^{-1})) est un système inductif et les applications'",
    "'système inductif' italic (the later 'forment un système inductif d'applications' is roman)",
    "upright", "italics", None, "high",
    r"est un système inductif et¶les applications", r"est un \emph{système inductif} et¶les applications")

# ---------------------------------------------------------------- p. 26
add(26, "l. 1: 'Rappelons (I, 4.1.10) que 𝔖𝔭𝔯(X)'", "bold I", "plain I", "convention", 2, "high",
    r"Rappelons (I, 4.1.10)", r"Rappelons (\textbf{I}, 4.1.10)")
add(26, "Proposition (8.6.3), l. 1: 'Supposons S_0 quasi-compact (resp. quasi-compact et quasi-séparé).'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"quasi-compact (resp. quasi-compact et quasi-séparé). Alors",
    r"quasi-compact \textup{(resp.} quasi-compact et quasi-séparé\textup{)}. Alors")
add(26, "Proposition (8.6.3), l. 2: 'Alors les applications (8.6.2.1), (8.6.2.2), (8.6.2.3) sont injectives'",
    "the three references upright", "italic", "convention", 6, "high",
    r"applications (8.6.2.1), (8.6.2.2), (8.6.2.3) sont",
    r"applications \textup{(8.6.2.1), (8.6.2.2), (8.6.2.3)} sont")
add(26, "Proposition (8.6.3), end: 'sont injectives (resp. bijectives).'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"injectives (resp.¶bijectives).", r"injectives \textup{(resp.}¶bijectives\textup{)}.")
add(26, "proof of (8.6.3): 'comme S_λ est quasi-séparé, il en est de même de U_λ (1.2.7), et par suite'",
    "(1.2.7) without a chapter numeral (enlarged crop)", "(I, 1.2.7)", "extra", None, "high",
    r"$U_\lambda$ (I, 1.2.7)", r"$U_\lambda$ (1.2.7)",
    note="Not a misprint: the print refers to (IV, 1.2.7), the criteria for a prescheme to be quasi-separated, "
         "which is what the step uses.")
add(26, "Corollaire (8.6.3.1), l. 2-3: 'soit majoré par Z'' = u_λ^{-1}(Z''_λ) (I, 4.1.10), il faut'",
    "(I, 4.1.10) upright inside the italic statement, with a bold I",
    "plain I, italic (corollary environment)", "convention", 2, "high",
    r"(Z''_\lambda)$ (I, 4.1.10)", r"(Z''_\lambda)$ \textup{(\textbf{I}, 4.1.10)}",
    note="Bold I (convention 2) and the upright reference in an italic statement (convention 6), one edit as in "
         "the run_IV1/run_IV2 findings.")
add(26, "proof of (8.6.3.1), l. 2-3: 'sont localement constructibles dans S_λ par hypothèse (1.8.4), donc'",
    "(1.8.4) without a chapter numeral (enlarged crop)", "(I, 1.8.4)", "extra", None, "high",
    r"(I, 1.8.4)", r"(1.8.4)",
    note="Not a misprint: the print refers to Chevalley's theorem (IV, 1.8.4); EGA I (1960) has no 1.8.x.")
add(26, "proof of (8.6.3.1), l. 4: 'En outre, par hypothèse (1.6.1), les sous-espaces'",
    "(1.6.1) without a chapter numeral (enlarged crop)", "(I, 1.6.1)", "extra", None, "high",
    r"(I, 1.6.1)", r"(1.6.1)",
    note="Not a misprint: (IV, 1.6.1), the definition of finite presentation, cited as (1.6.1) in (8.6.1) on p. 25 too.")
add(26, "proof of (8.6.3.1), l. 5: 'il y a un voisinage ouvert quasi-compact V(x) dans S_λ tels que'",
    "'tels que' (enlarged crop); the only antecedent is the singular 'voisinage'",
    "tels que (keeps the printed reading)", "misprint_in_print", None, "medium",
    None, None, corrected=r"dans $S_\lambda$ tel que",
    note="Agreement slip. The diplomatic text is right as it stands; for the corrected edition replace "
         "'dans $S_\\lambda$ tels que' by 'dans $S_\\lambda$ tel que'.")
add(26, "proof of (8.6.3.1), last line: 'en outre Z' est majoré par Y (I, 4.4.1)'", "bold I", "plain I",
    "convention", 2, "high",
    r"(I, 4.4.1)", r"(\textbf{I}, 4.4.1)")

# ---------------------------------------------------------------- p. 27
add(27, "Corollaire (8.6.4), l. 2-3: 'soit un sous-préschéma induit sur un ouvert (resp. un sous-préschéma fermé) de S'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"induit sur un ouvert¶(resp. un sous-préschéma fermé) de $S$",
    r"induit sur un ouvert¶\textup{(resp.} un sous-préschéma fermé\textup{)} de $S$")
add(27, "Corollaire (8.6.4), end: 'soit induit sur un ouvert (resp. un sous-préschéma fermé) dans S_μ.'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"sur un ouvert (resp. un sous-préschéma fermé) dans $S_\mu$",
    r"sur un ouvert \textup{(resp.} un sous-préschéma fermé\textup{)} dans $S_\mu$")
add(27, "heading 8.7: 'Critères pour qu'une limite projective de préschémas soit un préschéma réduit (resp. intègre).'",
    "'(resp.' and ').' in medium-weight roman, 'réduit' and 'intègre' bold; final full stop (enlarged crop)",
    "the whole title bold, no full stop", "font", None, "high",
    r"soit un préschéma réduit (resp. intègre)}",
    r"soit un préschéma réduit \textmd{(resp.} intègre\textmd{).}}",
    note="One edit for the medium-weight '(resp. ...)' and the printed final full stop (GLOBAL_ISSUES 43).")
add(27, "Proposition (8.7.2), l. 1: 'Supposons vérifiée l'une des hypothèses suivantes :'",
    "'l'une' upright (emphasis by change of face) inside the italic statement (enlarged crop); "
    "the same in Corollaire (8.7.3), p. 28",
    "italic", "convention", 6, "high",
    r"Supposons vérifiée l'une des", r"Supposons vérifiée \textup{l'une} des")
add(27, "Proposition (8.7.2) a): '(ce qui sera par exemple vérifié lorsque S_0 est noethérien),'",
    "the parenthesis roman, only 'noethérien' italic (enlarged crop)",
    "italic (proposition environment)", "convention", 6, "high",
    r"(ce qui sera par exemple vérifié¶lorsque $S_0$ est noethérien),",
    r"\textup{(ce qui sera par exemple vérifié¶lorsque $S_0$ est \emph{noethérien})},",
    note="Inside \\textup, \\emph sets 'noethérien' italic as printed.")
add(27, "Proposition (8.7.2), after b): 'Sous ces conditions, pour que S soit réduit'",
    "new, indented paragraph after b)",
    r"the text follows \end{enumerate} without a blank line (no paragraph indent)", "other", None, "high",
    r"\end{enumerate}¶Sous ces conditions", r"\end{enumerate}¶¶Sous ces conditions",
    note="Missing paragraph break.")

# ---------------------------------------------------------------- p. 28
add(28, "Corollaire (8.7.3), l. 1: 'Supposons vérifiée l'une des hypothèses suivantes :'",
    "'l'une' upright inside the italic statement, as in (8.7.2)", "italic", "convention", 6, "high",
    r"Supposons vérifiée l'une des", r"Supposons vérifiée \textup{l'une} des")
add(28, "Corollaire (8.7.3), after b): 'Alors, pour que S soit intègre'",
    "new, indented paragraph after b)",
    r"the text follows \end{enumerate} without a blank line (no paragraph indent)", "other", None, "high",
    r"\end{enumerate}¶Alors, pour que", r"\end{enumerate}¶¶Alors, pour que",
    note="Missing paragraph break.")
add(28, "heading 8.8: 'Préschémas de présentation finie sur une limite projective de préschémas.'",
    "the title ends with a full stop", "no full stop", "punctuation", None, "high",
    r"sur une limite projective de préschémas}", r"sur une limite projective de préschémas.}")
add(28, "(8.8.1), l. 10: 'et il est clair que (Hom_{S_λ}(X_λ, Y_λ), e_λμ) est un système inductif d'ensembles'",
    "e_λμ (enlarged crop), against e_μλ in the definition two lines above",
    r"e_{\mu\lambda} (silently corrected)", "misprint_in_print", None, "high",
    r",e_{\mu\lambda})$ est un", r",e_{\lambda\mu})$ est un", corrected=r",e_{\mu\lambda})$ est un",
    note="The transition maps are e_μλ : Hom_{S_λ}(X_λ,Y_λ) → Hom_{S_μ}(X_μ,Y_μ), as defined just before. "
         "The diplomatic text restores the printed e_λμ.")
add(28, "(8.8.1): 'et (e_λ) est un système inductif d'applications'",
    "'système inductif' italic (enlarged crop)", "upright", "italics", None, "high",
    r"est un système inductif¶d'applications", r"est un \emph{système inductif}¶d'applications")
add(28, "Théorème (8.8.2), label (i)", "label (i) upright",
    r"\item[(i)] inside the italic theorem (typeset italic)", "convention", 6, "high",
    r"\item[(i)] Supposons", r"\item[\textup{(i)}] Supposons", note="GLOBAL_ISSUES 16.")
add(28, "Théorème (8.8.2) (i), l. 1: 'Supposons X_α quasi-compact (resp. quasi-compact et quasi-séparé)'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"quasi-compact (resp. quasi-compact et¶quasi-séparé),",
    r"quasi-compact \textup{(resp.} quasi-compact et¶quasi-séparé\textup{)},")
add(28, "Théorème (8.8.2) (i), l. 2: 'Y_α localement de type fini (resp. localement de présentation finie) sur S_α'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"localement de type fini (resp. localement de¶présentation finie) sur",
    r"localement de type fini \textup{(resp.} localement de¶présentation finie\textup{)} sur")
add(28, "Théorème (8.8.2) (i), l. 3: 'Alors l'application (8.8.1.1) est injective'",
    "reference upright", "italic", "convention", 6, "high",
    r"l'application (8.8.1.1) est", r"l'application \textup{(8.8.1.1)} est")
add(28, "Théorème (8.8.2) (i), end: 'est injective (resp. bijective).'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"injective (resp. bijective).", r"injective \textup{(resp.} bijective\textup{)}.")
add(28, "Théorème (8.8.2), label (ii)", "label (ii) upright",
    r"\item[(ii)] inside the italic theorem (typeset italic)", "convention", 6, "high",
    r"\item[(ii)] Supposons", r"\item[\textup{(ii)}] Supposons", note="GLOBAL_ISSUES 16.")
add(28, "end of p. 28 / top of p. 29: the proof of (8.8.2) ('(i) Considérons d'abord ...') begins on p. 29",
    "p. 28 ends with statement (ii) of (8.8.2); p. 29 opens with the proof",
    r"\begin{proof} stands before \oldpage[IV-3]{29}, in p. 28's segment", "marker", None, "medium",
    r"\end{theorem}¶¶\begin{proof}¶", r"\end{theorem}¶¶\oldpage[IV-3]{29}¶\begin{proof}¶",
    note="Apply together with the p. 29 marker finding (removes the old marker); either order works with "
         "apply_fixes.py. Same pattern as the 0_IV p. 163 fix.")

# ---------------------------------------------------------------- p. 29
add(29, r"top of p. 29: the marker after \begin{proof}", "p. 29 opens with the proof of (8.8.2)",
    r"\oldpage[IV-3]{29} after \begin{proof}", "marker", None, "medium",
    r"\oldpage[IV-3]{29}¶(i) Considérons", r"(i) Considérons",
    note="Second half of the marker move (p. 28 marker finding inserts the marker before \\begin{proof}); "
         "apply both or neither.")
add(29, "Lemme (8.8.2.1), l. 2-3: 'C_α une A_α-algèbre de type fini (resp. de présentation finie). Alors'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"de type fini (resp. de¶présentation finie). Alors",
    r"de type fini \textup{(resp.} de¶présentation finie\textup{)}. Alors")
add(29, "Lemme (8.8.2.1), display (8.8.2.2): subscripts 'A_λ-alg.' and 'A-alg.'",
    "'alg.' upright in both subscripts (enlarged crop)",
    r"\text{-alg.} inside the italic lemma: typeset italic", "convention", 6, "high",
    r"\operatorname{Hom}_{A_\lambda\text{-alg.}}¶  (C_\alpha\otimes_{A_\alpha}A_\lambda,¶   B_\alpha\otimes_{A_\alpha}A_\lambda)¶\longrightarrow¶\operatorname{Hom}_{A\text{-alg.}}",
    r"\operatorname{Hom}_{A_\lambda\textup{-alg.}}¶  (C_\alpha\otimes_{A_\alpha}A_\lambda,¶   B_\alpha\otimes_{A_\alpha}A_\lambda)¶\longrightarrow¶\operatorname{Hom}_{A\textup{-alg.}}",
    note="\\text takes the italic shape of the statement; the displays in the proofs (roman context) are right.")
add(29, "Lemme (8.8.2.1), after the display: 'est injectif (resp. bijectif).'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"\end{equation}¶est injectif (resp. bijectif).",
    r"\end{equation}¶est injectif \textup{(resp.} bijectif\textup{)}.")
add(29, "Lemme (8.8.2.3), l. 1-2: 'G une E-algèbre de type fini (resp. de présentation finie), (F_λ)'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"de type fini (resp. de présentation¶finie), $(F_\lambda)$",
    r"de type fini \textup{(resp.} de présentation¶finie\textup{)}, $(F_\lambda)$")
add(29, "Lemme (8.8.2.3), display: subscripts 'E-alg.' (twice)",
    "'alg.' upright (enlarged crop)", r"\text{-alg.} inside the italic lemma: typeset italic",
    "convention", 6, "high",
    r"\varinjlim\operatorname{Hom}_{E\text{-alg.}}(G,F_\lambda)¶\longrightarrow¶\operatorname{Hom}_{E\text{-alg.}}(G,\varinjlim F_\lambda)",
    r"\varinjlim\operatorname{Hom}_{E\textup{-alg.}}(G,F_\lambda)¶\longrightarrow¶\operatorname{Hom}_{E\textup{-alg.}}(G,\varinjlim F_\lambda)")
add(29, "Lemme (8.8.2.3), end: 'fait correspondre sa limite inductive, est injectif (resp. bijectif).'",
    "'(resp.' and ')' upright", "italic", "convention", 6, "high",
    r"inductive, est injectif (resp. bijectif).", r"inductive, est injectif \textup{(resp.} bijectif\textup{)}.")

# ---------------------------------------------------------------- checks
bad = 0
texts = {}
for x in F:
    p = x["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    fx = x["fix"]
    if fx is None:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        bad += 1
        print("OLD COUNT", n, "p.", p, repr(fx["old"][:80]))
# misprint 'corrected' spans: the uncorrected span must exist once on its page
for x in F:
    if x["kind"] == "misprint_in_print" and x["fix"] is None:
        span = x["corrected"].replace(" tel que", " tels que")
        print("misprint kept, span count", texts[x["page"]].count(span), repr(span))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
c = Counter()
for x in F:
    c[(x["page"], "misprint" if x["kind"] == "misprint_in_print" else "convention" if x["kind"] == "convention" else "normal")] += 1
for p in sorted({x["page"] for x in F}):
    print(f"p. {p}: {c[(p, 'normal')]}/{c[(p, 'convention')]}/{c[(p, 'misprint')]}")
print("findings", len(F), "bad olds", bad, "->", OUT)
