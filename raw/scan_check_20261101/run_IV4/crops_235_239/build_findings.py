"""Build findings_235_239.json and verify every fix 'old' (unique in page_NNN.tex and in the current source segment,
also after the earlier fixes of the same page are applied in order)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4")
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-20-fr.tex")
NL = "\n"


def F(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention, confidence=confidence,
             fix=(None if old is None else dict(old=old, new=new)))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C7 = dict(kind="convention", convention=7)
X = []

# ---------------- p. 235 ----------------
X.append(F(235, "l. 2: 'S^{-1}A = lim A_t' (lim with an arrow below)", "index t under the arrow of the lim",
           "\\varinjlim A_t: no index", "formula",
           r"$S^{-1}A=\varinjlim A_t$", r"$S^{-1}A=\varinjlim_t A_t$",
           "The index is missing (its position under or beside the lim is not at issue)."))
X.append(F(235, "l. 3: 'la relation « t est un diviseur de t' » (0_I, 1.4.5)'",
           "(0_I, 1.4.5): bold 0 with a light roman subscript I (crop p235_0I.png)",
           "\\sref[0]{0.1.4.5} prints '(0, 1.4.5)': bold 0 without the subscript I", "missing",
           r"\sref[0]{0.1.4.5}", r"\sref[$\mathbf{0}_{\mathrm I}$]{0.1.4.5}",
           "Keeps the link. The IV-4 \\sref sets its optional argument in \\textbf, but math ignores that, so this "
           "gives a bold 0 with a LIGHT subscript I as printed (test compile; \\sref[0\\textsubscript{I}] would bold "
           "the I), the form ($\\mathbf{0}_{\\mathrm I}$, ...) of ega4-16/17/18. The same \\sref[0] form occurs twice "
           "more in ega4-20 (p. 226) and 15 times in ega4-21b: check those against the print."))
X.append(F(235, "l. 4: 'M'(X) = lim Γ(U, O_X)' (lim with an arrow below)", "index U under the arrow of the lim",
           "\\varinjlim\\Gamma(U,\\sh{O}_X): no index", "formula",
           r"$M'(X)=\varinjlim\Gamma(U,\sh{O}_X)$", r"$M'(X)=\varinjlim_U\Gamma(U,\sh{O}_X)$",
           "The index is missing (its position is not at issue)."))
X.append(F(235, "proof, 'dire que U=X—Y (où Y=V(𝔍) est fermé dans X)'", "long dash", "minus sign",
           old=r"$U=X-Y$", new=r"$U=X\setmin Y$", note="\\setmin as in the earlier IV-4 fixes.", **C7))

# ---------------- p. 236 ----------------
X.append(F(236, "(ii), l. 4: 'il existe dans A—Q des éléments ≠0'", "long dash", "minus sign",
           old=r"dans $A-Q$ des", new=r"dans $A\setmin Q$ des", **C7))
X.append(F(236, "(iii), l. 4: 'donc Γ(X, 𝓜_X) = M(X) = A;'",
           "no primes: Γ(X, 𝓜_X) = M(X) = A (crop p236_primes1.png)",
           "\\Gamma(X,\\sh{M}'_X)=M'(X)=A: two primes added", "formula",
           r"$\Gamma(X,\sh{M}'_X)=M'(X)=A$", r"$\Gamma(X,\sh{M}_X)=M(X)=A$",
           "In (iii) only the first sentence has 𝓜'_X; the TeX also primes this formula and the next two. "
           "Not a misprint: X is noetherian, so 𝓜_X = 𝓜'_X and M(X) = M'(X) (20.2.12)."))
X.append(F(236, "(iii), l. 5: 'si 𝓜_X était quasi-cohérent'", "𝓜_X without prime (crop p236_primes2.png)",
           "\\sh{M}'_X", "formula", r"si $\sh{M}'_X$ était", r"si $\sh{M}_X$ était", "See the previous finding."))
X.append(F(236, "(iii), l. 5: '𝓜_X|U = R(U) est un faisceau simple'",
           "𝓜_X|U without prime (crops p236_primes1.png, p236_primes2.png)", "\\sh{M}'_X|U", "formula",
           r"$\sh{M}'_X|U=R(U)$", r"$\sh{M}_X|U=R(U)$", "See the previous findings."))
X.append(F(236, "(iv): 'sont ceux qui contiennent l'ensemble Ass(O_X)'",
           "'contiennent l'ensemble' italic (crop p236_ensemble.png)", "only 'contiennent' emphasised", "italics",
           r"\emph{contiennent} l'ensemble", r"\emph{contiennent l'ensemble}",
           "Remark body judged as roman (document-wide remark font)."))
X.append(F(236, "(20.2.14), l. 3-4: 'on appelle Idéal des dénominateurs de u l'annulateur'",
           "no article before the italic 'Idéal' (crop p236_appelle.png)",
           "'on appelle l'\\emph{Idéal ...}': article added", "extra",
           r"on appelle l'\emph{Idéal", r"on appelle \emph{Idéal",
           "Rewording: the print has no article here."))
X.append(F(236, "Proposition (20.2.15), l. 2 (first word of the line): 'quasi-|cohérent,'",
           "the t of 'cohérent' is BOLD italic (wrong fount), not at a line end: side by side with the t of "
           "'section' on the same line it has a 5 px median stroke (mean 5.8 px, 190 dark px) against 4 px "
           "(mean 4.0 px, 151 dark px); the n before it (170 against 173 px for the n of 'une') and the comma "
           "after it (64 against 61 px for the comma after 'morphisme') are normal (crops p236_coherent2.png, "
           "p236_t_cmp2.png, p236_n_cmp.png)",
           "normal italic t (silent correction)", "misprint_in_print",
           r"-Module quasi-cohérent,", r"-Module quasi-cohéren\textbf{t},",
           "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99; mid-line, so not item 100). The fix "
           "restores the printed reading.", confidence="medium", corrected=r"-Module quasi-cohérent,"))
X.append(F(236, "Remarque (20.2.16), l. 1: 'le préfaisceau U ⇝ Ps.hom_S(U, Y)'", "wavy arrow (crop p236_arrow.png)",
           "\\mapsto", "symbol",
           r"$U\mapsto\operatorname{Ps.hom}_S(U,Y)$", r"$U\leadsto\operatorname{Ps.hom}_S(U,Y)$",
           "ega4-20 has no \\leadsto at all (25 \\mapsto): its other \\mapsto need the same check (item 33)."))
X.append(F(236, "Remarque (20.2.16), l. 3: 'un spectre d'un anneau semi-local noethérien A'",
           "'semi-local' italic", "roman (no \\emph)", "italics",
           r"anneau semi-local noethérien", r"anneau \emph{semi-local} noethérien",
           "Remark body judged as roman (document-wide remark font)."))

# ---------------- p. 237 ----------------
X.append(F(237, "Remarque (20.2.16), l. 2: 'l'ouvert U = X—{x', x''}'", "long dash", "minus sign",
           old=r"$U=X-\{x',x''\}$", new=r"$U=X\setmin\{x',x''\}$", **C7))
X.append(F(237, "l. 2: 'Soient U' = X—{x'}'", "long dash", "minus sign",
           old=r"$U'=X-\{x'\}$", new=r"$U'=X\setmin\{x'\}$", **C7))
X.append(F(237, "l. 2: 'U'' = X—{x''}'", "long dash", "minus sign",
           old=r"$U''=X-\{x''\}$", new=r"$U''=X\setmin\{x''\}$", **C7))
X.append(F(237, "l. 6: 'au même pseudo-morphisme de U dans Y, mais qui sont tels que'",
           "'sont' (crop p237_sont.png)", "'soient'", "word",
           r"mais qui soient tels que", r"mais qui sont tels que",
           "The TeX turns the print's indicative into a subjunctive (rewording)."))
X.append(F(237, "l. 8-9: 'considérons une partie fermée irréductible Z de X'",
           "'irréductible' italic (crop p237_irred.png)", "roman", "italics",
           r"fermée irréductible $Z$", r"fermée \emph{irréductible} $Z$",
           "Remark body judged as roman (document-wide remark font)."))
X.append(F(237, "l. 10: 'le long de l'ouvert partout dense X—Z (I, 2.3.1)'", "long dash", "minus sign",
           old=r"dense $X-Z$", new=r"dense $X\setmin Z$", **C7))
X.append(F(237, "l. 10-11: 'des isomorphismes structuraux Y' ⥲ X, Y'' ⥲ X'",
           "two isomorphism arrows, a tilde over each arrow (crop p237_iso.png)",
           "$Y'\\to X$, $Y''\\to X$: plain arrows", "symbol",
           r"$Y'\to X$, $Y''\to X$", r"$Y'\xrightarrow{\sim}X$, $Y''\xrightarrow{\sim}X$",
           "Not convention 4 (the TeX has a plain arrow, not \\simeq); written as FIX_POLICY writes convention 4."))
X.append(F(237, "l. 12: 'les restrictions de u' et u'' à U—(U∩Z) sont égales'", "long dash", "minus sign",
           old=r"à $U-(U\cap Z)$ sont", new=r"à $U\setmin(U\cap Z)$ sont", **C7))
X.append(F(237, "l. 12: 'et U—(U∩Z) est un ouvert dense dans U'", "long dash", "minus sign",
           old=r"et $U-(U\cap Z)$ est", new=r"et $U\setmin(U\cap Z)$ est", **C7))
X.append(F(237, "heading 20.3: 'Composition des pseudo-morphismes.'", "full stop after the title",
           "no full stop", "punctuation",
           r"\subsection{Composition des pseudo-morphismes}", r"\subsection{Composition des pseudo-morphismes.}",
           "GLOBAL_ISSUES 43/58; same form as the earlier IV-4 subsection-title page fixes."))
X.append(F(237, "(20.3.1), l. 2: 'f: Y → Z un morphisme.'", "'morphisme' italic (crop p237_morph.png)", "roman",
           "italics", r"$f:Y\to Z$ un morphisme.", r"$f:Y\to Z$ un \emph{morphisme}.", ""))
X.append(F(237, "(20.3.1): 'le pseudo-morphisme de X dans Z composé de f et de ω'",
           "only 'composé' italic; 'de' and 'et de' roman (crop p237_compose1.png)",
           "\\emph{composé de $f$ et de $\\omega$}", "italics",
           r"\emph{composé de $f$ et de $\omega$}", r"\emph{composé} de $f$ et de $\omega$", ""))
X.append(F(237, "(20.3.2), l. 3-4: 'tel que l'ouvert V' = f^{-1}(dom_S(ω)) soit schématiquement dense dans X''",
           "'schématiquement dense dans' italic (crop p237_schem.png)", "roman", "italics",
           r"soit schématiquement dense dans $X'$ ;", r"soit \emph{schématiquement dense dans} $X'$ ;", ""))
X.append(F(237, "(20.3.2), l. 5: 'du S-morphisme u∘(f|U')'", "u∘(f|U') (crop p237_UV.png)",
           "u\\circ(f|U'): the TeX keeps the printed reading", "misprint_in_print", None, None,
           "No U' is defined in (20.3.2): u is defined on dom_S(ω) and f maps V' = f^{-1}(dom_S(ω)) into it, so the "
           "restriction meant is f|V'. Not in Err_IV (Liste 3).", corrected=r"$u\circ(f|V')$"))
X.append(F(237, "(20.3.2), l. 6: 'est le pseudo-S-morphisme composé de ω et de f'",
           "only 'composé' italic (crop p237_compose2.png)", "\\emph{composé de $\\omega$ et de $f$}", "italics",
           r"\emph{composé de $\omega$ et de $f$}", r"\emph{composé} de $\omega$ et de $f$", ""))
X.append(F(237, "display (20.3.2.1): 'f^{-1}(dom_S(ω)) ⊂ dom_S(ω∘f).'", "full stop after the formula "
           "(crop p237_disp.png)", "no full stop", "punctuation",
           r"\operatorname{dom}_S(\omega\circ f)" + NL + r"  \tag{20.3.2.1}",
           r"\operatorname{dom}_S(\omega\circ f)." + NL + r"  \tag{20.3.2.1}", ""))

# ---------------- p. 238 ----------------
X.append(F(238, "l. 2: 'un préfaisceau d'ensembles V ⇝ Ps.hom_S(V, Y)^{f^V}'", "wavy arrow (crop p238_arr1.png)",
           "\\mapsto", "symbol",
           r"$V\mapsto\operatorname{Ps.hom}_S(V,Y)^{f^V}$", r"$V\leadsto\operatorname{Ps.hom}_S(V,Y)^{f^V}$", ""))
X.append(F(238, "l. 3: 'sous-préfaisceau de V ⇝ Ps.hom_S(V, Y)'", "wavy arrow (crop p238_arr2.png)", "\\mapsto",
           "symbol", r"de $V\mapsto\operatorname{Ps.hom}_S(V,Y)$,", r"de $V\leadsto\operatorname{Ps.hom}_S(V,Y)$,", ""))
X.append(F(238, "l. 4: 'que l'on note 𝒫s.hom_S(X, Y)^f'",
           "script P followed by italic 's.hom' (the same form in (20.3.4), crop p238_psh.png)",
           "\\mathscr{P}\\!s.\\!\\operatorname{hom}: upright 'hom'", "font",
           r"que l'on note $\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y)^f$",
           r"que l'on note $\mathscr{P}\!s.\mathit{hom}_S(X,Y)^f$",
           "Only the sheaf 𝒫s.hom has the italic 'hom' (like the sheaf Proj, GLOBAL_ISSUES 31); the roman Ps.hom of "
           "the sets is right. ega4-20 writes the sheaf this way 13 times (pp. 232-234, 238-239, 250)."))
X.append(F(238, "l. 4: 'une application ω ⇝ ω∘f^V'", "wavy arrow (crop p238_arr3.png)", "\\mapsto", "symbol",
           r"$\omega\mapsto\omega\circ f^V$", r"$\omega\leadsto\omega\circ f^V$", ""))
X.append(F(238, "l. 5: 'qui définit donc un f-morphisme de faisceaux'", "'f-morphisme' italic (crop p238_fmorph.png)",
           "roman", "italics", r"un $f$-morphisme de", r"un \emph{$f$-morphisme} de", ""))
X.append(F(238, "display at the end of (20.3.2): '𝒫s.hom_S(X, Y)^f → 𝒫s.hom_S(X', Y).'", "italic 'hom' twice",
           "upright \\operatorname{hom} twice", "font",
           r"\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y)^f\to\mathscr{P}\!s.\!\operatorname{hom}_S(X',Y).",
           r"\mathscr{P}\!s.\mathit{hom}_S(X,Y)^f\to\mathscr{P}\!s.\mathit{hom}_S(X',Y).",
           "See the finding for l. 4."))
X.append(F(238, "(20.3.3), second paragraph: 'D'autre part, pour tout S-morphisme g: Y → Z'",
           "new indented paragraph", "same paragraph (no blank line before 'D'autre part')", "other",
           r"\omega\circ(f\circ f')$." + NL + r"D'autre part", r"\omega\circ(f\circ f')$." + NL + NL + r"D'autre part",
           ""))
X.append(F(238, "(20.3.4), l. 2: '𝒫s.hom_S(X, Y)^f = 𝒫s.hom_S(X, Y)'", "italic 'hom' twice (crop p238_psh.png)",
           "upright \\operatorname{hom} twice", "font",
           r"$\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y)^f=\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y)$",
           r"$\mathscr{P}\!s.\mathit{hom}_S(X,Y)^f=\mathscr{P}\!s.\mathit{hom}_S(X,Y)$",
           "See the finding for l. 4."))
X.append(F(238, "(20.3.4), l. 4: 'lorsqu'il en est ainsi, alors, pour tout ouvert U'",
           "'alors,' set in BOLD roman (wrong fount), mid-line: mean stroke run 6.05 px against 5.32 px for "
           "'ainsi' and 4.8-5.0 px for the words around it; its a 247 against 186 dark px for the a of 'ainsi'; "
           "its comma 87 against 65 px for the comma after 'ainsi' (crops p238_alors.png, p238_alors_z.png)",
           "normal weight (silent correction)", "misprint_in_print",
           r"ainsi, alors, pour", r"ainsi, \textbf{alors,} pour",
           "Wrong-fount word recorded as a misprint (GLOBAL_ISSUES 29/99; cf. p. 68). The fix restores the printed "
           "reading.", confidence="medium", corrected=r"ainsi, alors, pour"))
X.append(F(238, "(20.3.4), l. 5 (first character of the line): 'ω : U → Y'",
           "this ω is BOLD (wrong fount): 274 dark px and a mean stroke run of 5.5 px against 219 px and 4.4 px "
           "for the ω of 'ω∘f^U' later on the same line (crops p238_omega.png, p238_omega_cmp.png, p238_w1.png)",
           "\\omega (silent correction)", "misprint_in_print",
           r"pseudo-$S$-morphisme $\omega:U\to Y$", r"pseudo-$S$-morphisme $\boldsymbol{\omega}:U\to Y$",
           "Wrong-fount letter recorded as a misprint (GLOBAL_ISSUES 29/99); a single letter at the start of the "
           "line, as the é of p. 204, so not item 100. The fix restores the printed reading.",
           confidence="medium", corrected=r"pseudo-$S$-morphisme $\omega:U\to Y$"))
X.append(F(238, "proof of (20.3.5): 'L'assertion (i) résulte de (11.10.5, (ii), b))'",
           "italic 'b)' (letter and its parenthesis) with no opening parenthesis (crop p238_b.png)",
           "\\sref{IV.11.10.5}[(ii), (b)] prints '(11.10.5, (ii), (b))': an added '(' and an upright b", "italics",
           r"\sref{IV.11.10.5}[(ii), (b)]", r"\sref{IV.11.10.5}[(ii), \emph{b)}]",
           "The third \\sref argument is set inside \\normalfont, so \\emph gives the printed italic. ega4-20 has 8 "
           "such '[..., (a)]' labels; the other 5 (after p. 239) need the same check."))
X.append(F(238, "proof of (20.3.5): 'l'assertion (ii) résulte de (11.10.5, (ii), a))'",
           "italic 'a)' with no opening parenthesis (crop p238_a.png)",
           "\\sref{IV.11.10.5}[(ii), (a)] prints '(11.10.5, (ii), (a))'", "italics",
           r"\sref{IV.11.10.5}[(ii), (a)]", r"\sref{IV.11.10.5}[(ii), \emph{a)}]", ""))
X.append(F(238, "proof of (20.3.5): 'tout ouvert V dans U est rétrocompact'", "'rétrocompact' italic (crop p238_a.png)",
           "roman", "italics", r"est rétrocompact", r"est \emph{rétrocompact}", ""))
X.append(F(238, "proof of (20.3.5): 'tout ouvert V dense dans U, f^{-1}(V) est dense dans f^{-1}(U)'",
           "the first 'dense' is italic too", "only the second 'dense' emphasised", "italics",
           r"ouvert $V$ dense dans $U$", r"ouvert $V$ \emph{dense} dans $U$", ""))

# ---------------- p. 239 ----------------
X.append(F(239, "l. 1 (first line of the page): 'tout point maximal de X' appartenant à f^{-1}(V)'",
           "f^{-1}(V) (crop p239_fV.png)", "f^{-1}(U) (silent correction)", "misprint_in_print",
           r"appartenant à $f^{-1}(U)$ est un point", r"appartenant à $f^{-1}(V)$ est un point",
           "The step needs the maximal points of X' that lie in f^{-1}(U) (p. 238: 'il suffit que f^{-1}(V) "
           "contienne tous les points maximaux de X' appartenant à f^{-1}(U)'); with f^{-1}(V) it proves nothing. "
           "Not in Err_IV (Liste 3). The marker and page break are right (not a boundary fix).",
           corrected=r"appartenant à $f^{-1}(U)$ est un point"))
X.append(F(239, "(20.3.6): item labels a), b)", "roman (upright) labels (crop p239_ab.png)",
           "label=\\emph{\\alph*)}: italic in the roman env", "italics",
           r"\begin{enumerate}[label=\emph{\alph*)}]", r"\begin{enumerate}[label=\alph*)]", ""))
X.append(F(239, "(20.3.6) a): 'X est localement noethérien;'",
           "'est localement noethérien' italic (crop p239_ab.png)", "roman", "italics",
           r"\item $X$ est localement noethérien ;", r"\item $X$ \emph{est localement noethérien} ;", ""))
X.append(F(239, "(20.3.6) b): 'X est réduit et l'ensemble de ses composantes irréductibles est localement fini.'",
           "italic after X (crop p239_ab.png)", "roman", "italics",
           r"\item $X$ est réduit et l'ensemble de ses composantes irréductibles est localement fini.",
           r"\item $X$ \emph{est réduit et l'ensemble de ses composantes irréductibles est localement fini}.", ""))
X.append(F(239, "(20.3.6): 'Alors, pour tout x∈X' after the list", "new indented paragraph",
           "follows \\end{enumerate} without a blank line, so no indent", "other",
           r"\end{enumerate}" + NL + r"Alors, pour tout", r"\end{enumerate}" + NL + NL + r"Alors, pour tout",
           "Item 80 pattern."))
X.append(F(239, "(20.3.6): 'dans le cas a), la condition (iii)'", "italic 'a)' (crop p239_cas.png)", "roman 'a)'",
           "italics", r"dans le cas~a), la", r"dans le cas~\emph{a)}, la", ""))
X.append(F(239, "(20.3.6): 'dans le cas b).'", "italic 'b)' (crop p239_cas.png)", "roman 'b)'", "italics",
           r"dans le cas~b).", r"dans le cas~\emph{b)}.", ""))
X.append(F(239, "(20.3.6): 'Pour tout pseudo-S-morphisme ω de X dans Y'", "'tout' italic (crop p239_cas.png)",
           "roman", "italics", r"Pour tout pseudo-$S$-morphisme", r"Pour \emph{tout} pseudo-$S$-morphisme", ""))
X.append(F(239, "(20.3.6): 'si X vérifie la condition a) (resp. b)) de (20.3.6)'",
           "italic 'a)' and 'b)', upright '(resp.' and outer ')' (crop p239_cond.png)", "roman a), b)", "italics",
           r"la condition~a) (resp. b))", r"la condition~\emph{a)} (resp. \emph{b)})", ""))
X.append(F(239, "display (20.3.6.1): '(𝒫s.hom_S(X, Y))_x → Ps.hom_S(Spec(O_{X,x}), Y)'",
           "italic 'hom' in the sheaf 𝒫s.hom", "upright \\operatorname{hom}", "font",
           r"(\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y))_x", r"(\mathscr{P}\!s.\mathit{hom}_S(X,Y))_x",
           "As on p. 238."))
X.append(F(239, "after (20.3.6.1): 'la fibre au point x du faisceau 𝒫s.hom_S(X, Y)'", "italic 'hom'",
           "upright \\operatorname{hom}", "font",
           r"du faisceau $\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y)$", r"du faisceau $\mathscr{P}\!s.\mathit{hom}_S(X,Y)$",
           "As on p. 238."))
X.append(F(239, "proof of (20.3.7): 'Par application de la méthode de (8.1.2, a))'",
           "italic 'a)' with no opening parenthesis (crop p239_812.png)",
           "\\sref{IV.8.1.2}[(a)] prints '(8.1.2, (a))'", "italics",
           r"\sref{IV.8.1.2}[(a)]", r"\sref{IV.8.1.2}[\emph{a)}]", "As the two on p. 238."))
X.append(F(239, "Proposition (20.3.8), l. 2: '(resp. quasi-compact et quasi-séparé)'",
           "'(resp.' upright; the words and the closing parenthesis italic (crops p239_resp1.png, p239_separe.png)",
           "'(resp.' italic (statement environment)",
           old=r"(resp. quasi-compact", new=r"\textup{(resp.} quasi-compact",
           note="Item 101: upright only where 'resp.' stands next to the parenthesis.", kind="convention",
           convention=6))
X.append(F(239, "Proposition (20.3.8), l. 2: '(resp. localement de présentation finie)'",
           "'(resp.' upright; the closing parenthesis after 'finie' italic (crops p239_resp2.png, p239_finie.png)",
           "'(resp.' italic", old=r"(resp. localement de présentation", new=r"\textup{(resp.} localement de présentation",
           kind="convention", convention=6))
X.append(F(239, "Proposition (20.3.8): 'Alors, l'application canonique' after the list", "new indented line "
           "(paragraph) after (ii)", "follows \\end{enumerate} without a blank line, so no indent", "other",
           r"\end{enumerate}" + NL + r"Alors, l'application canonique",
           r"\end{enumerate}" + NL + NL + r"Alors, l'application canonique", "Item 80 pattern."))
X.append(F(239, "Proposition (20.3.8), last line: 'est injective (resp. bijective).'",
           "'(resp.' upright; 'bijective)' italic (crop p239_resp3.png)", "'(resp.' italic",
           old=r"est injective (resp. bijective)", new=r"est injective \textup{(resp.} bijective)",
           kind="convention", convention=6))

# ---------------- verify ----------------
src = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[IV-4\]\{(\d+)\}", src)]
seg = {}
for i, (n, s) in enumerate(cuts):
    seg[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]
pages = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for p in range(235, 240)}
bad = 0
cur_seg = dict(seg)
for x in X:
    fx = x["fix"]
    if not fx:
        continue
    p, old, new = x["page"], fx["old"], fx["new"]
    c_page = pages[p].count(old)
    c_seg = cur_seg[p].count(old)
    if c_page != 1 or c_seg != 1 or old == new:
        bad += 1
        print("PROBLEM", p, repr(old), c_page, c_seg)
    cur_seg[p] = cur_seg[p].replace(old, new)
counts = {}
for x in X:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("problems:", bad, "findings:", len(X))
print(counts)
out = RUN / "findings_235_239.json"
out.write_text(json.dumps(X, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", out)
