import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_127_131.json"


def F(page, where, scan, tex, kind, conv, conf, old=None, new=None, note="", corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if old is not None else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


C2 = "Bold chapter numeral in the reference."
FINDINGS = [
    # ---------------- page 127 ----------------
    F(127, "first line: '(où les flèches horizontales sont la multiplication par x'",
      "continues the sentence of p. 126 ('Pour tout x∈𝔍^m, le diagramme ...') at the left margin, without indent",
      "blank lines before and after \\oldpage[III]{127}: a new paragraph", "other", None, "high",
      "\\oldpage[III]{127}\n\n(où", "\\oldpage[III]{127}\n(où",
      "The blank line before the marker is in the p. 126 segment ('\\]\\n\\n' after the sheaf diagram); remove it "
      "too, together with the misplaced \\tag{4.1.7.11} there (see the next finding)."),
    F(127, "(4.1.7.11): the diagram of cohomology groups after 'donc le diagramme correspondant'",
      "the diagram carries the equation number (4.1.7.11) at its left",
      "no \\tag on this diagram; the TeX puts \\tag{4.1.7.11}\\label{III.4.1.7.11-fr} on the diagram of sheaves on p. 126",
      "missing", None, "high",
      r"""H^n(X,\mathcal F)\ar[r]_{\mu_{x,0}}&H^n(X,\mathcal F)
}
\]""",
      r"""H^n(X,\mathcal F)\ar[r]_{\mu_{x,0}}&H^n(X,\mathcal F)
}
\tag{4.1.7.11}\label{III.4.1.7.11-fr}
\]""",
      "The diagram of sheaves at the foot of p. 126 has no number in the print (p. 126 strips checked across the seam). "
      "Apply together with the removal of '\\n\\tag{4.1.7.11}\\label{III.4.1.7.11-fr}' from that diagram (p. 126 segment, "
      "before \\oldpage[III]{127}), or the label is defined twice. The reference in (4.1.7.12), 'le diagramme (4.1.7.11) "
      "où on remplace n par n+1', is to this cohomology diagram."),
    F(127, "end of the proof of (4.1.7.9): 'R est un quotient du sous-S-module M'",
      "'quotient' in italics", "upright", "italics", None, "high",
      "est un quotient du", r"est un \emph{quotient} du"),
    F(127, "end of the proof of (4.1.7.9): 'R est un S-module de type fini, ce qui équivaut'",
      "'de type fini' in italics", "upright", "italics", None, "high",
      "un $S$-module de type fini, ce qui", r"un $S$-module \emph{de type fini}, ce qui"),
    F(127, "(4.1.7.12): 'le S-module gradué N=⊕_{k≥0}H^{n+1}(X, 𝔍^{k+1}ℱ) défini comme dans'",
      "the formula is set inline at the end of the first line of (4.1.7.12)", "displayed", "other", None, "high",
      r"""le $S$-module gradué
\[
\mathrm N=\bigoplus_{k\geq0}H^{n+1}(X,\mathfrak J^{k+1}\mathcal F)
\]
défini""",
      r"""le $S$-module gradué
$\mathrm N=\bigoplus_{k\geq0}H^{n+1}(X,\mathfrak J^{k+1}\mathcal F)$
défini""",
      "Layout: display where the print sets the formula inline (GLOBAL_ISSUES 21/36)."),
    F(127, "(4.1.7.12): 'défini comme dans (4.7.1.8)'",
      "(4.7.1.8)", "(4.7.1.8), plain text without a link", "misprint_in_print", None, "high",
      None, None,
      "Crop: the print reads 4.7.1.8 (digits transposed); the S-module structure is the one defined by the "
      "multiplications μ_{x,m} of (4.1.7.8), see (4.1.7.7). The TeX keeps the printed reading. Not in the authors' "
      "errata (ega3-7-fr.tex).",
      r"(\hyperref[III.4.1.7.8-fr]{4.1.7.8})"),
    F(127, "(4.1.7.12): 'c'est encore un S-module de type fini en vertu de (3.3.2)'",
      "'de type fini' in italics", "upright", "italics", None, "high",
      "$S$-module de type fini en", r"$S$-module \emph{de type fini} en"),
    F(127, "(4.1.7.12): 'Q est un sous-S-module gradué de N'",
      "'sous-S-module gradué' in italics (S a formula letter)", "upright", "italics", None, "high",
      "un sous-$S$-module gradué de", r"un \emph{sous-$S$-module gradué} de"),
    F(127, "(4.1.7.12): 'et par suite est de type fini.'",
      "'de type fini' in italics", "upright", "italics", None, "high",
      "par suite est de type fini.", r"par suite est \emph{de type fini}."),
    F(127, "(4.1.7.13): 'dans le S-module Q, on a'",
      "S-module with 'module' in italics (crop)", "upright", "italics", None, "high",
      "dans le $S$-module", r"dans le $S$-\emph{module}"),
    F(127, "(4.1.7.13), after the display (4.1.7.14): 'Comme Q est un S-module de type fini'",
      "new indented paragraph", "no paragraph break: the text follows \\] directly", "other", None, "high",
      "\\]\nComme $\\mathrm Q$ est", "\\]\n\nComme $\\mathrm Q$ est",
      "Paragraph break. 'de type fini' in this sentence is upright in the print."),
    F(127, "(4.1.7.13): '(II, 2.1.6, (ii))'", "bold II", "plain II", "convention", 2, "high",
      "(II, 2.1.6, (ii))", r"(\textbf{II}, 2.1.6, (ii))", C2),
    F(127, "(4.1.7.18): beginning of the display",
      "μ_{x,0} : H^{n+1}(X, 𝔍^kℱ) →(μ_{x,m}) H^{n+1}(X, 𝔍^{k+m}ℱ) →(ν_m) H^{n+1}(X, 𝔍^kℱ)",
      "the display begins with H^{n+1}(X,𝔍^kℱ); μ_{x,0} only in an added sentence after it",
      "missing", None, "high",
      "\\xymatrix@C=4.5em{\nH^{n+1}", "\\xymatrix@C=4.5em{\n\\mu_{x,0}:H^{n+1}",
      "Restores the printed 'μ_{x,0} :' before the composite; see the next finding."),
    F(127, "(4.1.7.16), after the display (4.1.7.18): 'dont le composé est μ_{x,0}.'",
      "no such sentence: after (4.1.7.18) p. 128 continues 'd'où on conclut que, ...' in the same paragraph",
      "dont le composé est $\\mu_{x,0}$. followed by \\end{env} and a blank line before \\oldpage[III]{128}",
      "extra", None, "high",
      "\\]\ndont le composé est $\\mu_{x,0}$.\n\\end{env}\n\n", "\\]\n",
      "Editorial sentence standing in for the printed 'μ_{x,0} :'. The edit also removes \\end{env} and the blank "
      "line before the page marker, because the print continues the paragraph (4.1.7.16) on p. 128 through "
      "(4.1.7.19). Apply together with the two p. 128 edits (blank line after \\oldpage[III]{128}; \\end{env} after "
      "(4.1.7.19)), or the env is left unbalanced."),
    # ---------------- page 128 ----------------
    F(128, "first line: 'd'où on conclut que, pour tout sous-A-module P de'",
      "continues the sentence of p. 127 at the left margin, without indent",
      "blank line after \\oldpage[III]{128} (and \\end{env} on p. 127): a new paragraph", "other", None, "high",
      "\\oldpage[III]{128}\n\nd'où", "\\oldpage[III]{128}\nd'où",
      "Apply together with the p. 127 edit that removes 'dont le composé est μ_{x,0}.' with its \\end{env}, and "
      "with the next finding."),
    F(128, "after the display (4.1.7.19)",
      "end of the paragraph (4.1.7.16); Lemme (4.1.7.20) follows", "(4.1.7.16) closed on p. 127",
      "other", None, "high",
      "\\tag{4.1.7.19}\\label{III.4.1.7.19-fr}\n\\]\n", "\\tag{4.1.7.19}\\label{III.4.1.7.19-fr}\n\\]\n\\end{env}\n",
      "Moves the \\end{env} of (4.1.7.16) after (4.1.7.19); apply only together with the p. 127 edit that "
      "removes it there."),
    F(128, "proof of (4.1.7.20): 'ν_m(Q_{k+m})=α_m(S_m)Q_k⊂α_r(S_r)Q_k=0.'",
      "set inline after 'en vertu de (4.1.7.19) et (4.1.7.15)'", "displayed", "other", None, "high",
      r"""(\hyperref[III.4.1.7.15-fr]{4.1.7.15})
\[
\nu_m(\mathrm Q_{k+m})=\alpha_m(S_m)\mathrm Q_k
\subset\alpha_r(S_r)\mathrm Q_k=0.
\]""",
      r"""(\hyperref[III.4.1.7.15-fr]{4.1.7.15})
$\nu_m(\mathrm Q_{k+m})=\alpha_m(S_m)\mathrm Q_k
\subset\alpha_r(S_r)\mathrm Q_k=0$.""",
      "Layout: display where the print sets the formula inline (GLOBAL_ISSUES 21/36)."),
    F(128, "(4.1.7.21), second diagram, bottom row: 'ℱ_{k+m} → 0'",
      "the k of the subscript k+m is a heavy bold k; '+m' normal weight",
      "\\mathcal F_{k+m} with an ordinary k", "misprint_in_print", None, "medium",
      "\\mathcal F_{k+m}\\ar[r]\\ar[u]&0", "\\mathcal F_{\\boldsymbol{k}+m}\\ar[r]\\ar[u]&0",
      "Wrong-font (or over-inked) sort: on same-scale crops this k has 244 dark pixels against 144 for the subscript "
      "k of ℱ_{k+m} in the first diagram of the page. The TeX silently has the normal k; the fix restores the printed "
      "reading. Apply only if wrong-font sorts are reproduced (GLOBAL_ISSUES 29).",
      "\\mathcal F_{k+m}"),
    F(128, "(4.1.7.21), third diagram: vertical arrow between the two H",
      "an ordinary upward arrow labelled 'id.' (italic) on its left", "\\ar@{=}[u]: an unlabelled double line",
      "formula", None, "high",
      "\\ar@{=}[u]", "\\ar[u]^{\\textit{id.}}",
      "Crop. For an upward arrow ^ puts the label on the left, as printed."),
    F(128, "(4.1.7.21), third diagram: vertical arrow Q_{k+m} → Q_k",
      "label ν_m to the right of the arrow", "\\ar[u]^{\\nu_m}: label on the left of an upward arrow",
      "formula", None, "high",
      "\\ar[u]^{\\nu_m}", "\\ar[u]_{\\nu_m}", "Crop."),
    F(128, "(4.1.7.21), last line: 'est surjective (I, 1.3.9)'", "bold I", "plain I", "convention", 2, "high",
      "(I, 1.3.9)", r"(\textbf{I}, 1.3.9)", C2),
    F(128, "last word: 'On peut donc appli-' (continued 'quer' on p. 129)",
      "the word 'appliquer' hyphenated across the page break",
      "'appli-' followed by a blank line before \\oldpage[III]{129}: a hyphen and a paragraph break inside the word",
      "other", None, "high",
      "appli-\n\n", "appli%\n",
      "As the EGA II p. 36 fix ('canoni-\\n\\n' -> 'canoni%\\n'). Apply together with the p. 129 edit that removes "
      "the blank line after \\oldpage[III]{129}."),
    # ---------------- page 129 ----------------
    F(129, "first word: 'quer (0, 13.3.1)' (end of 'appliquer' from p. 128)",
      "continuation of the word and sentence of p. 128", "blank line after \\oldpage[III]{129}: a new paragraph",
      "other", None, "high",
      "\\oldpage[III]{129}\n\nquer", "\\oldpage[III]{129}\nquer",
      "As the EGA II p. 37 fix. Apply together with the p. 128 edit 'appli-\\n\\n' -> 'appli%\\n'."),
    F(129, "first line: 'quer (0, 13.3.1)'", "bold 0", "plain 0", "convention", 2, "high",
      "(0, 13.3.1)", r"(\textbf{0}, 13.3.1)", C2),
    F(129, "first line: 'H^n(X̂, ℱ̂)→lim H^n(X, ℱ_k) est bijectif'", "'bijectif' in italics", "upright",
      "italics", None, "high",
      "est bijectif pour tout", r"est \emph{bijectif} pour tout"),
    F(129, "after (4.1.7.22): '(0, 13.2.2); comme ν_m(Q_{k+m})=0'", "bold 0", "plain 0", "convention", 2, "high",
      "(0, 13.2.2)", r"(\textbf{0}, 13.2.2)", C2),
    F(129, "'d'où un isomorphisme topologique lim (H/R_k) ⥲ lim H_k. Mais comme'",
      "the isomorphism is set inline at the start of a text line, followed by 'Mais comme la filtration'",
      "displayed", "other", None, "high",
      r"""d'où un isomorphisme topologique
\[
\varprojlim_k(\mathrm H/\mathrm R_k)\xrightarrow{\sim}
\varprojlim_k\mathrm H_k.
\]
Mais""",
      r"""d'où un isomorphisme topologique
$\varprojlim_k(\mathrm H/\mathrm R_k)\xrightarrow{\sim}
\varprojlim_k\mathrm H_k$.
Mais""",
      "Layout: display where the print sets the formula inline (GLOBAL_ISSUES 21/36)."),
    F(129, "(4.1.8): 'Γ(V, (R^nf_*(ℱ))^) est le séparé complété'",
      "(R^nf_*(ℱ))^: R^nf_*(ℱ) in parentheses, circumflex after the closing parenthesis",
      "\\widehat{R^nf_*(\\mathcal F)}: wide hat, no outer parentheses", "formula", None, "high",
      r"\Gamma(V,\widehat{R^nf_*(\mathcal F)})", r"\Gamma(V,(R^nf_*(\mathcal F))^{\widehat{\,}})",
      "Crop. Circumflex analogue of convention 5; same form as the EGA II p. 194 fixes (GLOBAL_ISSUES 31)."),
    F(129, "(4.1.8): 'un 𝒪_Y-Module cohérent (I, 10.8.4)'", "bold I", "plain I", "convention", 2, "high",
      "(I, 10.8.4)", r"(\textbf{I}, 10.8.4)", C2),
    F(129, "(4.1.8): 'et Γ(V, lim R^nf_*(ℱ_k)) est égal à lim Γ(V, R^nf_*(ℱ_k)) (0_I, 3.2.6)'",
      "the words 'est égal à' between the two expressions, all inline in the running text",
      "displayed equation with '=' instead of 'est égal à' (and \\bigl/\\bigr)", "word", None, "high",
      r"""et
\[
\Gamma\bigl(V,\varprojlim_kR^nf_*(\mathcal F_k)\bigr)
=\varprojlim_k\Gamma(V,R^nf_*(\mathcal F_k))
\]
""",
      r"""et $\Gamma(V,\varprojlim_kR^nf_*(\mathcal F_k))$ est égal à
$\varprojlim_k\Gamma(V,R^nf_*(\mathcal F_k))$
""",
      "The same edit sets the formulas inline as printed (next finding)."),
    F(129, "(4.1.8): the same two expressions", "inline in the running text", "displayed", "other", None, "high",
      None, None, "Layout; covered by the edit of the preceding finding."),
    F(129, "(4.1.8): '(0_I, 3.2.6); le fait que φ_n'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0\textsubscript{I}, 3.2.6)", r"(\textbf{0}\textsubscript{I}, 3.2.6)", C2),
    F(129, "(4.1.8): 'l'homomorphisme ψ_{n,V} de (4.1.3.3) est un isomorphisme, donc ψ_n'",
      "this first 'isomorphisme' in italics (the next one is upright)", "upright", "italics", None, "high",
      "est un isomorphisme, donc", r"est un \emph{isomorphisme}, donc"),
    F(129, "Corollaire (4.1.9): 'Sous les hypothèses de (4.1.4)'",
      "the reference (4.1.4) upright inside the italic statement (crop)", "italic inside the corollary environment",
      "convention", 6, "high",
      r"Sous les hypothèses de (\hyperref[III.4.1.4-fr]{4.1.4})",
      r"Sous les hypothèses de \textup{(\hyperref[III.4.1.4-fr]{4.1.4})}",
      "Upright reference (roman old-style figures) inside an italic statement."),
    F(129, "Remarque (4.1.10): heading",
      "Remarque (4.1.10). — Soit f : X→Y ... (roman body)",
      "\\begin{env}[4.1.10] with a hand-made '\\emph{Remarque.}': prints '(4.1.10) Remarque. Soit', no dash",
      "other", None, "high",
      "\\begin{env}[4.1.10]\n\\label{III.4.1.10-fr}\n\\emph{Remarque.}\n",
      "\\begin{remark}[4.1.10]\n\\label{III.4.1.10-fr}\n\\upshape\n",
      "As the 0_III p. 42 fix (env + \\emph{Remarques} -> remarks + \\upshape). Apply together with the next "
      "finding (the matching \\end)."),
    F(129, "Remarque (4.1.10): end, before §4.2", "end of the remark", "\\end{env}", "other", None, "high",
      "\\end{env}\n\n\\subsection{", "\\end{remark}\n\n\\subsection{",
      "Matching \\end for the preceding finding; apply both or neither."),
    F(129, "Remarque (4.1.10): 'un morphisme de type fini de préschémas'", "'de type fini' in italics", "upright",
      "italics", None, "high",
      "un morphisme de type fini de", r"un morphisme \emph{de type fini} de",
      "Judged with the remark body roman, as printed."),
    F(129, "Remarque (4.1.10): 'dont le support soit propre sur Y'", "'propre sur' in italics", "upright",
      "italics", None, "high",
      "soit propre sur $Y$", r"soit \emph{propre sur} $Y$"),
    F(129, "Remarque (4.1.10): '(II, 5.4.10)'", "bold II", "plain II", "convention", 2, "high",
      "(II, 5.4.10)", r"(\textbf{II}, 5.4.10)", C2),
    F(129, "Remarque (4.1.10): 'l'injection canonique (I, 9.3.5)'", "bold I", "plain I", "convention", 2, "high",
      "(I, 9.3.5)", r"(\textbf{I}, 9.3.5)", C2),
    F(129, "Remarque (4.1.10): 'Si on pose 𝒢_k=𝒢⊗_{𝒪_Y}(𝒪_Y/𝒥^{k+1}), on a'",
      "set inline in the running text", "displayed", "other", None, "high",
      r"""Si on pose
\[
\mathcal G_k=\mathcal G\otimes_{\mathcal O_Y}
(\mathcal O_Y/\mathcal J^{k+1}),
\]
on a""",
      r"""Si on pose
$\mathcal G_k=\mathcal G\otimes_{\mathcal O_Y}
(\mathcal O_Y/\mathcal J^{k+1})$,
on a""",
      "Layout: display where the print sets the formula inline (GLOBAL_ISSUES 21/36)."),
    F(129, "Remarque (4.1.10): 'compte tenu de (I, 10.9.5)'", "bold I", "plain I", "convention", 2, "high",
      "(I, 10.9.5)", r"(\textbf{I}, 10.9.5)", C2),
    F(129, "Remarque (4.1.10), display: 'R^n(f∘u)^_*(𝒢)'",
      "R^n(f∘u)^_*: circumflex after the closing parenthesis of (f∘u), asterisk below",
      "R^n\\widehat{(f\\circ u)}_*: wide hat over the parenthesis", "formula", None, "high",
      r"R^n\widehat{(f\circ u)}_*", r"R^n(f\circ u)^{\widehat{\,}}_*",
      "Crop. Circumflex analogue of convention 5 (GLOBAL_ISSUES 31). Independent of the next finding."),
    F(129, "Remarque (4.1.10), display: 'R^n f̂_*(ℱ̂) = R^n(f∘u)^_*(𝒢).'",
      "(𝒢) without a hat", "(\\widehat{\\mathcal G})", "misprint_in_print", None, "high",
      r"(\widehat{\mathcal G}).", r"(\mathcal G).",
      "Crop: the ℱ of the left side has its hat, the 𝒢 has none. The functor R^n(f∘u)^_* applies to Modules on the "
      "formal completion, so the completed 𝒢̂ is meant. The TeX silently corrects; the fix restores the printed "
      "reading.",
      r"(\widehat{\mathcal G})"),
    F(129, "Remarque (4.1.10), last sentence: 'les résultats de (4.1.5) sont valables pour ℱ et f.'",
      "'les résultats de', 'sont valables pour' and 'et' in italics; (4.1.5) upright", "upright",
      "italics", None, "high",
      r"""les résultats de (\hyperref[III.4.1.5-fr]{4.1.5}) sont valables pour
$\mathcal F$ et $f$.""",
      r"""\emph{les résultats de} (\hyperref[III.4.1.5-fr]{4.1.5}) \emph{sont valables pour}
$\mathcal F$ \emph{et} $f$."""),
    F(129, "last line: 'Alors, pour tout y∈Y et tout p, (R^pf_*(ℱ))_y est' (continued on p. 130)",
      "the statement of (4.2.1) continues mid-sentence on p. 130", "blank line before \\oldpage[III]{130}",
      "other", None, "high",
      "$(R^pf_*(\\mathcal F))_y$ est\n\n", "$(R^pf_*(\\mathcal F))_y$ est\n",
      "Paragraph break inside the sentence (GLOBAL_ISSUES 20). Apply together with the p. 130 edit after the "
      "marker."),
    # ---------------- page 130 ----------------
    F(130, "first line: 'un 𝒪_y-module de type fini, donc séparé'",
      "continues the statement of (4.2.1) from p. 129 at the left margin, without indent",
      "blank line after \\oldpage[III]{130}: a new paragraph inside the proposition", "other", None, "high",
      "\\oldpage[III]{130}\n\nun $\\mathcal O_y$", "\\oldpage[III]{130}\nun $\\mathcal O_y$",
      "Apply together with the p. 129 edit before the marker."),
    F(130, "(4.2.1.1): left-hand side '((R^pf_*(ℱ))_y)^'",
      "((R^pf_*(ℱ))_y)^: outer parentheses, circumflex after them",
      "\\widehat{(R^pf_*(\\mathcal F))_y}", "formula", None, "high",
      r"\widehat{(R^pf_*(\mathcal F))_y}", r"((R^pf_*(\mathcal F))_y)^{\widehat{\,}}",
      "Circumflex analogue of convention 5 (GLOBAL_ISSUES 31)."),
    F(130, "Proposition (4.2.1), last line: '(I, 3.6.1).'",
      "bold I (damaged sort: heavy stem, right serifs missing), reference upright",
      "plain I, italic inside the proposition environment", "convention", 2, "medium",
      "(I, 3.6.1)", r"\textup{(\textbf{I}, 3.6.1)}",
      "Bold I and upright reference in one edit (next finding). The sort is damaged; chapter numerals in references "
      "are bold elsewhere on the page ((I, 9.1.6), (I, 2.4.2))."),
    F(130, "Proposition (4.2.1): same reference '(I, 3.6.1)'", "upright inside the italic statement",
      "italic", "convention", 6, "high", None, None,
      "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."),
    F(130, "proof of (4.2.1): 'est séparée (0_I, 7.3.5)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0\textsubscript{I}, 7.3.5)", r"(\textbf{0}\textsubscript{I}, 7.3.5)", C2),
    F(130, "proof of (4.2.1): 'compte tenu de (G, II, 4 9.1)'",
      "(G, II, 4 9.1): no point between 4 and 9", "(G, II, 4.9.1)", "misprint_in_print", None, "high",
      "(G, II, 4.9.1)", "(G, II, 4 9.1)",
      "Crop (3x): a space and no point. The TeX silently corrects; the fix restores the printed reading.",
      "(G, II, 4.9.1)"),
    F(130, "proof of (4.2.1): 'posons Y_1=Spec(𝒪_y), X_1=X×_YY_1, ℱ_1=ℱ⊗_{𝒪_Y}𝒪_{Y_1}'",
      "set inline in the running text, items separated by commas", "displayed with \\qquad", "other", None, "high",
      r"""posons
\[
Y_1=\operatorname{Spec}(\mathcal O_y),\qquad
X_1=X\times_YY_1,\qquad
\mathcal F_1=\mathcal F\otimes_{\mathcal O_Y}\mathcal O_{Y_1}
\]
et soit""",
      r"""posons
$Y_1=\operatorname{Spec}(\mathcal O_y)$, $X_1=X\times_YY_1$,
$\mathcal F_1=\mathcal F\otimes_{\mathcal O_Y}\mathcal O_{Y_1}$
et soit""",
      "Layout: display where the print sets the formulas inline (GLOBAL_ISSUES 21/36)."),
    F(130, "proof of (4.2.1): 'f_1 propre (II, 5.4.2, (iii))'", "bold II", "plain II", "convention", 2, "high",
      "(II, 5.4.2, (iii))", r"(\textbf{II}, 5.4.2, (iii))", C2),
    F(130, "proof of (4.2.1): 'ℱ_1 est cohérent (0_I, 5.3.11)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0\textsubscript{I}, 5.3.11)", r"(\textbf{0}\textsubscript{I}, 5.3.11)", C2),
    F(130, "proof of (4.2.1): 'f_1^{-1}(y_1)=f^{-1}(y) (I, 3.6.5)'", "bold I (slightly damaged sort)", "plain I",
      "convention", 2, "medium",
      "(I, 3.6.5)", r"(\textbf{I}, 3.6.5)", C2 + " Damaged sort; see (I, 3.6.1)."),
    F(130, "proof of (4.2.1): 'canoniquement identifiés (I, 3.3.9)'", "bold I (badly broken sort)", "plain I",
      "convention", 2, "medium",
      "(I, 3.3.9)", r"(\textbf{I}, 3.3.9)", C2 + " Broken sort: only parts of the stem and serifs printed."),
    F(130, "proof of (4.2.1): 's'identifie à ℱ⊗_{𝒪_Y}(𝒪_y/𝔪_y^k) (I, 9.1.6)'", "bold I", "plain I", "convention",
      2, "high",
      "(I, 9.1.6)", r"(\textbf{I}, 9.1.6)", C2),
    F(130, "proof of (4.2.1), end: '(0_I, 6.7.1 et I, 2.4.2)'", "bold 0 and bold I", "plain 0 and I",
      "convention", 2, "high",
      r"(0\textsubscript{I}, 6.7.1 et I, 2.4.2)", r"(\textbf{0}\textsubscript{I}, 6.7.1 et \textbf{I}, 2.4.2)",
      "Bold chapter numerals (two in one reference)."),
    F(130, "proof of (4.2.2): 'on a alors H^p(f^{-1}(y), ℱ⊗(𝒪_y/𝔪_y^k))=0 (G, II, 4.15.2)'",
      "ℱ⊗(𝒪_y/𝔪_y^k): no subscript under ⊗; formula inline",
      "\\otimes_{\\mathcal O_Y}, in a display", "formula", None, "high",
      r"""En effet, on a alors
\[
H^p\bigl(f^{-1}(y),
\mathcal F\otimes_{\mathcal O_Y}(\mathcal O_y/\mathfrak m_y^k)\bigr)=0
\]
""",
      r"""En effet, on a alors
$H^p(f^{-1}(y),
\mathcal F\otimes(\mathcal O_y/\mathfrak m_y^k))=0$
""",
      "Crop: ⊗ without subscript here (with subscript 𝒪_Y in (4.2.1.1)). The same edit sets the formula inline "
      "(next finding)."),
    F(130, "proof of (4.2.2): the same formula", "inline in the running text", "displayed", "other", None, "high",
      None, None, "Layout; covered by the edit of the preceding finding."),
    F(130, "proof of (4.2.2): 'cohérent (0_I, 5.2.2)'", "bold 0", "plain 0", "convention", 2, "high",
      r"(0\textsubscript{I}, 5.2.2)", r"(\textbf{0}\textsubscript{I}, 5.2.2)", C2),
    F(130, "Corollaire (4.2.4): 'Sous les hypothèses de (4.2.1)'",
      "the reference upright inside the italic statement (crop)", "italic", "convention", 6, "high",
      r"hypothèses de (\hyperref[III.4.2.1-fr]{4.2.1})", r"hypothèses de \textup{(\hyperref[III.4.2.1-fr]{4.2.1})}",
      "Upright reference (roman old-style figures) inside an italic statement."),
    F(130, "Corollaire (4.2.4), display: '((f_*(ℱ))_y)^'",
      "((f_*(ℱ))_y)^: outer parentheses, circumflex after them", "\\widehat{(f_*(\\mathcal F))_y}",
      "formula", None, "high",
      r"\widehat{(f_*(\mathcal F))_y}", r"((f_*(\mathcal F))_y)^{\widehat{\,}}",
      "Circumflex analogue of convention 5 (GLOBAL_ISSUES 31)."),
    F(130, "last line: 'Alors 𝒜(X)=f_*(𝒪_X) est une 𝒪_Y-Algèbre cohérente.' (statement continued on p. 131)",
      "the statement of (4.3.1) continues on p. 131 in the same paragraph (no indent there)",
      "blank line before \\oldpage[III]{131}", "other", None, "high",
      "Algèbre cohérente.\n\n", "Algèbre cohérente.\n",
      "Paragraph break the print does not have (GLOBAL_ISSUES 20). Apply together with the p. 131 edit after the "
      "marker."),
    # ---------------- page 131 ----------------
    F(131, "first line: 'Soit Y' le Y-schéma fini au-dessus de Y'",
      "continues the statement of (4.3.1) at the left margin, without indent",
      "blank line after \\oldpage[III]{131}: a new paragraph inside the theorem", "other", None, "high",
      "\\oldpage[III]{131}\n\nSoit $Y'$", "\\oldpage[III]{131}\nSoit $Y'$",
      "Apply together with the p. 130 edit before the marker."),
    F(131, "Théorème (4.3.1): 'à un Y-isomorphisme près (II, 1.3.1 et 6.1.3)'",
      "bold II; the whole reference, 'et' included, upright (crop)", "plain II, italic inside the theorem",
      "convention", 2, "high",
      "(II, 1.3.1 et 6.1.3)", r"\textup{(\textbf{II}, 1.3.1 et 6.1.3)}",
      "Bold numeral and upright reference in one edit (next finding)."),
    F(131, "Théorème (4.3.1): same reference '(II, 1.3.1 et 6.1.3)'", "upright inside the italic statement",
      "italic", "convention", 6, "high", None, None,
      "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."),
    F(131, "Théorème (4.3.1): 'e : 𝒜(Y')→𝒜(X) (II, 1.2.7)'", "bold II, reference upright",
      "plain II, italic inside the theorem", "convention", 2, "high",
      "(II, 1.2.7)", r"\textup{(\textbf{II}, 1.2.7)}",
      "Bold numeral and upright reference in one edit (next finding)."),
    F(131, "Théorème (4.3.1): same reference '(II, 1.2.7)'", "upright inside the italic statement", "italic",
      "convention", 6, "high", None, None,
      "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."),
    F(131, "proof of (4.3.1): 'de prouver que g_*(θ) : g_*(𝒪_{Y'})→g_*(f'_*(𝒪_X))=f_*(𝒪_X) est l'identité'",
      "set inline in the running text", "displayed", "other", None, "high",
      r"""de prouver que
\[
g_*(\theta):g_*(\mathcal O_{Y'})\longrightarrow
g_*(f'_*(\mathcal O_X))=f_*(\mathcal O_X)
\]
est l'identité""",
      r"""de prouver que
$g_*(\theta):g_*(\mathcal O_{Y'})\longrightarrow
g_*(f'_*(\mathcal O_X))=f_*(\mathcal O_X)$
est l'identité""",
      "Layout: display where the print sets the formula inline (GLOBAL_ISSUES 21/36)."),
    F(131, "proof of (4.3.1): 'est l'identité (II, 1.4.2)'", "bold II (first I a damaged sort, second clearly bold)",
      "plain II", "convention", 2, "high",
      "(II, 1.4.2)", r"(\textbf{II}, 1.4.2)", C2),
    F(131, "proof of (4.3.1): 'f' est propre (II, 5.4.3, (i))'", "bold II", "plain II", "convention", 2, "high",
      "(II, 5.4.3, (i))", r"(\textbf{II}, 5.4.3, (i))", C2),
    F(131, "Corollaire (4.3.2): 'Sous les hypothèses de (4.3.1), supposons'",
      "the reference upright inside the italic statement", "italic", "convention", 6, "high",
      r"(\hyperref[III.4.3.1-fr]{4.3.1}), supposons", r"\textup{(\hyperref[III.4.3.1-fr]{4.3.1})}, supposons",
      "Upright reference (roman old-style figures) inside an italic statement."),
    F(131, "proof of (4.3.2): 'au cas où y est fermé dans Y'", "'fermé' in italics", "upright", "italics", None,
      "high",
      "est fermé dans $Y$", r"est \emph{fermé} dans $Y$"),
    F(131, "proof of (4.3.2): 'c'est donc un anneau local qui ne peut être'", "'anneau local' in italics",
      "upright", "italics", None, "high",
      "c'est donc un anneau local qui", r"c'est donc un \emph{anneau local} qui",
      "The earlier 'de l'anneau local 𝒪_y' is upright in the print."),
    F(131, "Corollaire (4.3.3): 'Sous les hypothèses de (4.3.1), pour tout y∈Y'",
      "the reference upright inside the italic statement", "italic", "convention", 6, "high",
      r"(\hyperref[III.4.3.1-fr]{4.3.1}), pour tout", r"\textup{(\hyperref[III.4.3.1-fr]{4.3.1})}, pour tout",
      "Upright reference (roman old-style figures) inside an italic statement."),
    F(131, "Corollaire (4.3.3), end: '(autrement dit, l'ensemble des idéaux maximaux de (f_*(𝒪_X))_y).'",
      "the parenthesis is roman, with 'idéaux maximaux' in italics (crop)",
      "all italic inside the corollary environment", "convention", 6, "high",
      r"""(autrement dit,
l'ensemble des idéaux maximaux de $(f_*(\mathcal O_X))_y$)""",
      r"""\textup{(autrement dit,
l'ensemble des \emph{idéaux maximaux} de $(f_*(\mathcal O_X))_y$)}""",
      "Roman words inside an italic statement; the same edit marks the italic 'idéaux maximaux'."),
    F(131, "proof of (4.3.3): 'un espace fini discret (II, 6.1.7)'", "bold II", "plain II", "convention", 2,
      "high",
      "(II, 6.1.7)", r"(\textbf{II}, 6.1.7)", C2),
    F(131, "Remarque (4.3.4): 'Soit k une extension du corps k(y)'", "bold italic k in k(y)", "plain k",
      "convention", 1, "high",
      "du corps $k(y)$", r"du corps $\boldsymbol{k}(y)$", "Residue field."),
    F(131, "Remarque (4.3.4): 'si le préschéma f^{-1}(y)⊗_{k(y)}k=X×_YSpec(k) est connexe'",
      "subscript k(y) of ⊗ with bold italic k; formula inline", "plain k, in a display", "convention", 1, "high",
      r"""si le préschéma
\[
f^{-1}(y)\otimes_{k(y)}k=X\times_Y\operatorname{Spec}(k)
\]
est connexe""",
      r"""si le préschéma
$f^{-1}(y)\otimes_{\boldsymbol{k}(y)}k=X\times_Y\operatorname{Spec}(k)$
est connexe""",
      "Residue field; the same edit sets the formula inline (next finding)."),
    F(131, "Remarque (4.3.4): the same formula", "inline in the running text", "displayed", "other", None, "high",
      None, None, "Layout; covered by the edit of the preceding finding."),
    F(131, "Remarque (4.3.4): 'un morphisme de projection (I, 3.4.7)'", "bold I", "plain I", "convention", 2,
      "high",
      "(I, 3.4.7)", r"(\textbf{I}, 3.4.7)", C2),
    F(131, "Remarque (4.3.4): 'si pour toute extension k de k(y)'", "'toute' in italics", "upright", "italics",
      None, "high",
      "pour toute extension", r"pour \emph{toute} extension", "Judged with the remark body roman, as printed."),
    F(131, "Remarque (4.3.4): 'si pour toute extension k de k(y)'", "bold italic k in k(y)", "plain k",
      "convention", 1, "high",
      "$k$ de $k(y)$", r"$k$ de $\boldsymbol{k}(y)$", "Residue field."),
    F(131, "Remarque (4.3.4), last line: 'f^{-1}(y)⊗_{k(y)}k=X×_YSpec(k)'", "bold italic k in the subscript k(y)",
      "plain k", "convention", 1, "high",
      r"$f^{-1}(y)\otimes_{k(y)}k", r"$f^{-1}(y)\otimes_{\boldsymbol{k}(y)}k", "Residue field."),
    F(131, "Remarque (4.3.4), last line: 'est connexe.'", "'connexe' in italics", "upright", "italics", None,
      "high",
      "\\operatorname{Spec}(k)$ est connexe.\n\n", "\\operatorname{Spec}(k)$ est \\emph{connexe}.\n",
      "The same edit removes the blank line before \\oldpage[III]{132} (next finding)."),
    F(131, "end of the page: the remark (4.3.4) continues on p. 132",
      "p. 132 begins 'Sous les hypothèses de (4.3.2), on peut alors ...' at the left margin, same paragraph",
      "blank lines before and after \\oldpage[III]{132}: a new paragraph", "other", None, "high",
      None, None,
      "Covered on this page by the edit of the preceding finding; the blank line after \\oldpage[III]{132} lies in "
      "the p. 132 segment and must go too."),
]


def main():
    pages = {}
    for p in sorted({f["page"] for f in FINDINGS}):
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    bad = 0
    # 1) every old occurs exactly once in the original page file
    for i, f in enumerate(FINDINGS):
        fx = f["fix"]
        if fx is None:
            continue
        n = pages[f["page"]].count(fx["old"])
        if n != 1:
            bad += 1
            print("NOT UNIQUE", i, f["page"], n, repr(fx["old"][:60]))
    # 2) sequential application in list order, as apply_fixes.py does (each old once in the current text)
    cur = dict(pages)
    for i, f in enumerate(FINDINGS):
        fx = f["fix"]
        if fx is None:
            continue
        n = cur[f["page"]].count(fx["old"])
        if n != 1:
            bad += 1
            print("SEQUENTIAL FAIL", i, f["page"], n, repr(fx["old"][:60]))
            continue
        cur[f["page"]] = cur[f["page"]].replace(fx["old"], fx["new"])
    # 3) brace balance of the edited pages compared with the originals
    for p in pages:
        def bal(t):
            t = t.replace("\\{", "").replace("\\}", "")
            return t.count("{") - t.count("}")
        print("page", p, "brace balance before/after:", bal(pages[p]), bal(cur[p]),
              "| $ parity before/after:", pages[p].count("$") % 2, cur[p].count("$") % 2,
              "| \\[ \\] before/after:", pages[p].count("\\["), pages[p].count("\\]"), cur[p].count("\\["),
              cur[p].count("\\]"),
              "| begin/end env before/after:", pages[p].count("\\begin{"), pages[p].count("\\end{"),
              cur[p].count("\\begin{"), cur[p].count("\\end{"))
    # counts
    for p in pages:
        fs = [f for f in FINDINGS if f["page"] == p]
        conv = sum(1 for f in fs if f["kind"] == "convention")
        mis = sum(1 for f in fs if f["kind"] == "misprint_in_print")
        print("page", p, "normal", len(fs) - conv - mis, "convention", conv, "misprint", mis)
    OUT.write_text(json.dumps(FINDINGS, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    (RUN / "crops_127_131" / "edited_preview.txt").write_text(
        "\n".join(f"===== page {p} =====\n{cur[p]}" for p in cur), encoding="utf-8")
    print("findings", len(FINDINGS), "problems", bad, "->", OUT)


main()
