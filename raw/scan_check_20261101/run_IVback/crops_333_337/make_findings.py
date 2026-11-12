import json

OUT = r"user/Documents/ega_scan_check_20261101/run_IVback/findings_333_337.json"

F = []


def add(page, where, scan, tex, kind, fix, note="", confidence="high", convention=None, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": fix,
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 333 (bibliography)
add(333, "Bibliographie: the heading and the list",
    "one heading 'BIBLIOGRAPHIE' (with a short rule), the entries [41]-[44] directly below it on the same page",
    "\\section*{BIBLIOGRAPHIE} followed by \\begin{thebibliography}{44}; in the book class thebibliography itself issues "
    "\\chapter*{\\bibname}, so the output has a second heading 'Bibliographie' on a new page (reader PDF of r20: "
    "'BIBLIOGRAPHIE' alone on PDF p. 221, 'Bibliographie' + entries on PDF p. 222)",
    "extra",
    {"old": "\\begin{thebibliography}{44}",
     "new": "\\begingroup\\renewcommand{\\chapter}[2]{}%\n\\begin{thebibliography}{44}"},
    "Part 1 of 2: apply together with the next finding (\\endgroup after \\end{thebibliography}). The local "
    "\\chapter redefinition swallows the \\chapter*{\\bibname} of thebibliography, so the page keeps the single "
    "printed heading and the \\bibitem keys (cited as \\cite{IV-41} in ega4-20) stay. EGA I/II use thebibliography "
    "without a \\section*, so only IV-4 has the double heading.")

add(333, "Bibliographie: end of the list",
    "(see the previous finding)",
    "\\end{thebibliography}",
    "extra",
    {"old": "\\end{thebibliography}",
     "new": "\\end{thebibliography}\n\\endgroup"},
    "Part 2 of 2: closes the group opened in the previous finding; the two edits must be applied together.")

add(333, "[41] author",
    "A. GROTHENDIECK: surname in capitals and small capitals (crop crops_333_337/p333_bib.png)",
    "A.~Grothendieck (plain)",
    "font",
    {"old": "{IV-41}\nA.~Grothendieck", "new": "{IV-41}\nA.~\\textsc{Grothendieck}"},
    "Author surnames in small capitals, as in the EGA I-IV-3 bibliographies (\\textsc).")

add(333, "[41] title",
    "'Séminaire de Géométrie algébrique, 1962,' roman; italic only from 'Cohomologie locale des faisceaux cohérents, "
    "et théorèmes de Lefschetz locaux et globaux' (crop p333_bib.png)",
    "\\emph covers 'Séminaire de Géométrie algébrique, 1962, Cohomologie ... globaux'",
    "italics",
    {"old": "\\emph{Séminaire de Géométrie algébrique, 1962,\nCohomologie locale",
     "new": "Séminaire de Géométrie algébrique, 1962,\n\\emph{Cohomologie locale"},
    "The closing brace after 'globaux' stays.")

add(333, "[42] authors",
    "M. DEMAZURE et A. GROTHENDIECK: surnames in small capitals",
    "M.~Demazure et A.~Grothendieck (plain)",
    "font",
    {"old": "M.~Demazure et A.~Grothendieck", "new": "M.~\\textsc{Demazure} et A.~\\textsc{Grothendieck}"},
    "")

add(333, "[42] title",
    "'Séminaire de Géométrie algébrique, 1963-1964,' roman; only 'Schémas en groupes' italic",
    "\\emph covers 'Séminaire de Géométrie algébrique, 1963--1964, Schémas en groupes'",
    "italics",
    {"old": "\\emph{Séminaire de Géométrie algébrique,\n1963--1964, Schémas en groupes}",
     "new": "Séminaire de Géométrie algébrique,\n1963--1964, \\emph{Schémas en groupes}"},
    "Apply BEFORE the [42] dash fix (next finding), whose 'old' lies inside this one's 'old'.")

add(333, "[42] '1963-1964'",
    "hyphen between the years (same length as the hyphens of Bures-sur-Yvette)",
    "en dash 1963--1964",
    "punctuation",
    {"old": "algébrique,\n1963--1964", "new": "algébrique,\n1963-1964"},
    "Apply AFTER the [42] italics fix (its 'old' contains this text). Hyphen in ranges as in the EGA II, III, IV-1 "
    "and IV-2 bibliographies.")

add(333, "[43] authors",
    "M. ARTIN et A. GROTHENDIECK: surnames in small capitals",
    "M.~Artin et A.~Grothendieck (plain)",
    "font",
    {"old": "M.~Artin et A.~Grothendieck", "new": "M.~\\textsc{Artin} et A.~\\textsc{Grothendieck}"},
    "")

add(333, "[43] title",
    "'Séminaire de Géométrie algébrique 1963-1964,' roman (no comma after 'algébrique', as in the TeX); only "
    "'Cohomologie étale des schémas' italic",
    "\\emph covers the whole 'Séminaire ... schémas'",
    "italics",
    {"old": "\\emph{Séminaire de Géométrie algébrique\n1963--1964, Cohomologie étale des schémas}",
     "new": "Séminaire de Géométrie algébrique\n1963--1964, \\emph{Cohomologie étale des schémas}"},
    "Apply BEFORE the [43] dash fix (next finding).")

add(333, "[43] '1963-1964'",
    "hyphen between the years",
    "en dash 1963--1964",
    "punctuation",
    {"old": "algébrique\n1963--1964", "new": "algébrique\n1963-1964"},
    "Apply AFTER the [43] italics fix (its 'old' contains this text).")

add(333, "[44] author",
    "C. S. SESHADRI: surname in small capitals",
    "C.~S.~Seshadri (plain)",
    "font",
    {"old": "C.~S.~Seshadri", "new": "C.~S.~\\textsc{Seshadri}"},
    "")

add(333, "[44] article title",
    "'Quotient space by an abelian variety' roman; only the journal 'Mathematische Annalen' italic (crop p333_bib.png)",
    "\\emph{Quotient space by an abelian variety}",
    "italics",
    {"old": "\\emph{Quotient space by an abelian variety}", "new": "Quotient space by an abelian variety"},
    "Article titles roman, journal names italic, as in the other EGA bibliographies (IV-2 p. 224, IV-3 p. 249).")

add(333, "[44] 'p. 185-194'",
    "hyphen",
    "en dash 185--194",
    "punctuation",
    {"old": "p.~185--194.", "new": "p.~185-194."},
    "")

# ---------------------------------------------------------------- page 334 (Index des notations)
add(334, "entry 16.3.1, after P^inf_{X/S}",
    "'... P^inf_f, P^inf_{X/S}, Gr_n(P_f), Gr_n(P_{X/S}), Ω^1_f, Ω^1_X (f : X→S ...)' (crop p334_l1to4_left.png)",
    "the two notations Gr_n(P_f), Gr_n(P_{X/S}) are missing",
    "missing",
    {"old": "$\\mathcal{P}^{\\infty}_{X/S}$,\n",
     "new": "$\\mathcal{P}^{\\infty}_{X/S}$, $\\mathcal{G}r_n(\\mathcal{P}_f)$, $\\mathcal{G}r_n(\\mathcal{P}_{X/S})$,\n"},
    "Both notations are introduced in (16.3.1) (ega4-16, Définition 16.3.1).")

add(334, "entry 16.3.1, Ω^1_f, Ω^1_X",
    "both Omegas italic (sheaves of differentials)",
    "upright \\Omega",
    "font",
    {"old": "$\\Omega^{1}_{f}$, $\\Omega", "new": "$\\varOmega^{1}_{f}$, $\\varOmega"},
    "Listed before the misprint fix of the same notation; the two edits do not overlap.")

add(334, "entry 16.3.1, second Omega",
    "Ω^1_X: subscript X alone, no '/S' (crop p334_l1to4_left.png)",
    "\\Omega^{1}_{X/S}",
    "misprint_in_print",
    {"old": "^{1}_{X/S}$\n(", "new": "^{1}_{X}$\n("},
    "The TeX silently corrects. (16.3.1) defines only Ω^1_f and Ω^1_{X/S}; the index drops '/S'. The fix changes "
    "only the subscript and does not overlap the font fix of the previous finding.",
    corrected="$\\varOmega^{1}_{X/S}$")

add(334, "entry 16.5.1",
    "Dér_S(O_X, F): 'Dér' with the acute accent (crop p334_s2_a.png)",
    "\\operatorname{Der}",
    "word",
    {"old": "$\\operatorname{Der}_{S}", "new": "$\\operatorname{D\\acute{e}r}_{S}"},
    "Same form as the body of (16.5.4) (\\operatorname{D\\acute{e}r}).")

add(334, "entry 16.5.4",
    "script D followed by italic 'ér' (with the accent)",
    "\\mathcal{D}er (no accent)",
    "word",
    {"old": "$\\mathcal{D}er_{S}", "new": "$\\mathcal{D}\\acute{e}r_{S}"},
    "The body writes \\mathscr{D}\\!\\acute{e}r (16.5.4); the index file keeps its \\mathcal alphabet (document-wide "
    "script-letter decision).")

add(334, "entry 16.5.7",
    "Fraktur G with subscript X/S (crop p334_frakG_Di.png)",
    "\\mathcal{T}_{X/S}",
    "symbol",
    {"old": "$\\mathcal{T}_{X/S}$ : 16.5.7.", "new": "$\\mathfrak{G}_{X/S}$ : 16.5.7."},
    "Wrong letter. The body of (16.5.7) writes \\mathfrak{G}_{X/S} for the tangent sheaf.")

add(334, "entry 16.5.8, D_i",
    "roman D with italic subscript i (crop p334_frakG_Di.png)",
    "italic D",
    "font",
    {"old": "$D_i$,", "new": "$\\mathrm{D}_i$,"},
    "Derivations D_i are roman in the print (GLOBAL_ISSUES 98).")

add(334, "entry 16.5.8, ∂/∂s_i",
    "built-up fraction: ∂ over ∂s_i, at text size (crop p334_frakG_Di.png)",
    "solidus form \\partial/\\partial s_i",
    "formula",
    {"old": "$\\partial/\\partial s_i$", "new": "$\\dfrac{\\partial}{\\partial s_i}$"},
    "")

add(334, "entry 16.5.13",
    "T_{X/S}(x), T_y(g): italic lowercase y subscript and argument g (crop p334_s2_b.png)",
    "T_Y(s)",
    "formula",
    {"old": "$T_Y(s)$", "new": "$T_y(g)$"},
    "The body of (16.5.13) introduces T_y(g) (16.5.13.5), the linear tangent map of g at y.")

add(334, "entry 16.6.1",
    "Ω^p_{X/S}, Ω^•_{X/S} italic (sheaves); Ω^p_{B/A} upright (module) (crop p334_s2_b.png)",
    "all three upright \\Omega",
    "font",
    {"old": "$\\Omega^p_{X/S}$, $\\Omega^\\bullet_{X/S}$", "new": "$\\varOmega^p_{X/S}$, $\\varOmega^\\bullet_{X/S}$"},
    "Ω^p_{B/A} stays upright.")

add(334, "entry 16.7.5",
    "'d^n_{X/S,F} : 16.7.5.' only (crop p334_s2_c.png)",
    "adds ', $d^n_{X/S}$'",
    "extra",
    {"old": "$d^n_{X/S,\\mathcal{F}}$, $d^n_{X/S}$ : 16.7.5.", "new": "$d^n_{X/S,\\mathcal{F}}$ : 16.7.5."},
    "")

add(334, "entry 16.11.1, the binomial (p q)",
    "a fraction bar between the bold p and q inside the parentheses (8x crop p334_binom8.png: a separate rule on the "
    "axis, under the foot serif of p); the binomials of the body (16.11.1.3)-(16.11.1.6), p. 53, have no bar",
    "\\binom{\\mathbf p}{\\mathbf q}",
    "misprint_in_print",
    {"old": "\\binom{\\mathbf p}{\\mathbf q}", "new": "\\genfrac{(}{)}{}{}{\\mathbf p}{\\mathbf q}"},
    "The TeX silently corrects. \\genfrac with an empty thickness gives the default fraction rule: the printed "
    "binomial with a bar.",
    corrected="\\binom{\\mathbf p}{\\mathbf q}")

add(334, "entry 18.5.2",
    "'Al(X, E, J)' roman Al, then 'Al(E, J)' bold upright Al (crop p334_s3_b.png)",
    "$Al(...)$ twice: math italic A, l",
    "font",
    {"old": "$Al(X,\\mathcal E,\\mathcal J)$, $Al(\\mathcal E",
     "new": "$\\operatorname{Al}(X,\\mathcal E,\\mathcal J)$, $\\mathbf{Al}(\\mathcal E"},
    "As in the body of (18.5.2): \\operatorname{Al}(X,...) and \\mathbf{Al}(...).")

add(334, "entry 18.5.3",
    "'Of(S)' roman, 'Of(X)' bold upright, 'Id(B')' roman (crop p334_s3_b.png)",
    "$Of(S)$, $Of(X)$, $Id(...)$ in math italic",
    "font",
    {"old": "$Of(S)$, $Of(X)$, $Id(", "new": "$\\operatorname{Of}(S)$, $\\mathbf{Of}(X)$, $\\operatorname{Id}("},
    "As in the body of (18.5.3): \\operatorname{Of}, \\mathbf{Of}(X), \\operatorname{Id}.")

add(334, "entry 19.1.3",
    "codim^*_y(Y, X): superscript asterisk (crop p334_s3_c.png)",
    "\\operatorname{codim}^{t}_{y}",
    "symbol",
    {"old": "\\operatorname{codim}^{t}_{y}", "new": "\\operatorname{codim}^{*}_{y}"},
    "The body of (19.1.3) writes \\operatorname{codim}_y^*(Y,X).")

add(334, "entry 20.1.11, before M_f(F)",
    "'(u section méromorphe de F) M_f(F) : 20.1.11.': no comma after the parenthesis (crop p334_s4_c.png)",
    "'... de $\\mathcal F$), $\\mathcal M_f(\\mathcal F)$'",
    "misprint_in_print",
    {"old": "de $\\mathcal F$), $\\mathcal M_f(\\mathcal F)$", "new": "de $\\mathcal F$) $\\mathcal M_f(\\mathcal F)$"},
    "The TeX silently supplies the comma that separates the notations.",
    corrected="de $\\mathcal F$), $\\mathcal M_f(\\mathcal F)$")

# ---------------------------------------------------------------- page 335 (Index des notations, end)
add(335, "entry 20.2.2",
    "script P followed by italic 's.hom' in both notations (crop p335_s1_a.png)",
    "\\mathcal P\\!s.\\operatorname{hom}: upright 'hom'",
    "font",
    {"old": "$\\mathcal P\\!s.\\operatorname{hom}(X,Y)$,\n$\\mathcal P\\!s.\\operatorname{hom}_S(X,Y)$ : 20.2.2.",
     "new": "$\\mathcal P\\!s.\\mathit{hom}(X,Y)$,\n$\\mathcal P\\!s.\\mathit{hom}_S(X,Y)$ : 20.2.2."},
    "Italic s.hom as agreed for § 20 (GLOBAL_ISSUES 107-108: \\mathit{hom}).")

add(335, "entry 20.3.2 (second line with 20.3.2)",
    "script P with italic 's.hom'",
    "\\operatorname{hom}",
    "font",
    {"old": "$\\mathcal P\\!s.\\operatorname{hom}_S(X,Y)^f$", "new": "$\\mathcal P\\!s.\\mathit{hom}_S(X,Y)^f$"},
    "")

add(335, "entry 20.5.3",
    "script P with italic 's.hom' (crop p335_s2_a.png)",
    "\\operatorname{hom}",
    "font",
    {"old": "$\\mathcal P\\!s.\\operatorname{hom}_{X/S}(X,Y)$", "new": "$\\mathcal P\\!s.\\mathit{hom}_{X/S}(X,Y)$"},
    "")

add(335, "entry 20.6.1",
    "script T: T_{X/S}(U), T_{X/S} (crop p335_Tf.png; the 20.1.11 entry on p. 334 has script S, crop p334_Sf.png)",
    "\\mathcal S_{X/S}(U), \\mathcal S_{X/S}",
    "symbol",
    {"old": "$\\mathcal S_{X/S}(U)$, $\\mathcal S_{X/S}$,", "new": "$\\mathcal T_{X/S}(U)$, $\\mathcal T_{X/S}$,"},
    "Wrong letter; the body of (20.6.1) names the sheaf \\sh{T}_{X/S}.")

add(335, "entry 20.6.7",
    "script T: T_f(U), T_f (crop p335_s2_a.png)",
    "\\mathcal S_f(U), \\mathcal S_f",
    "symbol",
    {"old": "$\\mathcal S_f(U)$, $\\mathcal S_f$, $\\mathcal M_{X/S,f}$",
     "new": "$\\mathcal T_f(U)$, $\\mathcal T_f$, $\\mathcal M_{X/S,f}$"},
    "Wrong letter; the body of (20.6.7) has T_f(U) and \\sh{T}_f. The 'old' includes M_{X/S,f} to be unique in "
    "the source file (p. 334 has the same S_f(U), S_f in 20.1.11, correctly).")

add(335, "entry 21.2.4, Id.inv_X",
    "script I (no descender) before italic 'd.inv' (4x crop p335_IJ.png)",
    "\\sh{J}d.inv_X (script J)",
    "symbol",
    {"old": "\\sh{J}d.inv_X", "new": "\\sh{I}d.inv_X"},
    "As in the body of § 21.2 after the page checks (\\sh{I}d.inv_X; GLOBAL_ISSUES 109).")

add(335, "entry 21.2.5",
    "script I in both I_U and I_X(D) (crop p335_IJ.png)",
    "\\mathcal J_U, \\mathcal J_X(D)",
    "symbol",
    {"old": "$\\mathcal J_U$, $\\mathcal J_X(D)$", "new": "$\\mathcal I_U$, $\\mathcal I_X(D)$"},
    "The body writes \\sh{I}_U and \\sh{I}_X(D).")

add(335, "entry 21.2.6",
    "script J (with descender) in div(J) and '(J Idéal fractionnaire)' (crop p335_IJ.png)",
    "\\mathcal I twice",
    "symbol",
    {"old": "$\\operatorname{div}(\\mathcal I)$ ($\\mathcal I$ Idéal",
     "new": "$\\operatorname{div}(\\mathcal J)$ ($\\mathcal J$ Idéal"},
    "The body of (21.2.6) writes div(\\sh{J}) for a fractional Ideal J.")

add(335, "entry 21.2.12",
    "heavy sans-serif Y in Y(D) (crop p335_s3_a.png)",
    "plain $Y(D)$",
    "font",
    {"old": "$Y(D)$ ($D$ diviseur positif)", "new": "$\\boldsymbol{\\mathsf{Y}}(D)$ ($D$ diviseur positif)"},
    "GLOBAL_ISSUES 109 (\\boldsymbol{\\mathsf{Y}}).")

add(335, "entry 21.6.4",
    "the c is a bold italic c: heavy strokes and a large ball terminal; ink 126 px in a 13x17 px box, as much as the "
    "closed italic o of o_x on the 21.6.7 line (126 px, 13x16), while the italic c of the body (21.6.4.1-2, p. 272) "
    "is light (side-by-side crop p335_c_vs_o_vs_roman_c.png, 6x crop p335_c_entry.png)",
    "plain $c$",
    "misprint_in_print",
    {"old": "$c$ : 21.6.4.", "new": "$\\boldsymbol{c}$ : 21.6.4."},
    "Wrong-fount letter (GLOBAL_ISSUES 29/97: a single letter visibly bolder than its kind nearby; at the start of "
    "the line, not the line-end case of item 100). The TeX silently corrects; the fix restores the printed bold "
    "italic c.",
    confidence="medium",
    corrected="$c$")

add(335, "entry 21.6.7, second notation",
    "mult with subscript {x} under a bar: the closure of {x} (5x crop p335_mult_bar.png)",
    "\\operatorname{mult}_{\\{x\\}}(D) without the bar",
    "formula",
    {"old": "\\operatorname{mult}_{\\{x\\}}(D)", "new": "\\operatorname{mult}_{\\overline{\\{x\\}}}(D)"},
    "As in the body of (21.6.7) (\\operatorname{mult}_{\\overline{\\{x\\}}}(D)).")

add(335, "entry 21.7.1",
    "heavy sans-serif Y in Y(C) and Y'(C) (crop p335_YC.png)",
    "plain $Y(C)$, $Y'(C)$",
    "font",
    {"old": "$Y(C)$, $Y'(C)$", "new": "$\\boldsymbol{\\mathsf{Y}}(C)$, $\\boldsymbol{\\mathsf{Y}}'(C)$"},
    "As in the body of (21.7.1) (\\boldsymbol{\\mathsf{Y}}(C), \\boldsymbol{\\mathsf{Y}}'(C)). J_X(C), J(C) are "
    "script J in the print, as in the TeX.")

add(335, "entry 21.10.3, Γ_T",
    "italic Gamma (crop p335_s3_c.png)",
    "upright \\Gamma_T",
    "font",
    {"old": "$\\Gamma_T(\\mathscr Z_X^1)$", "new": "$\\varGamma_T(\\mathscr Z_X^1)$"},
    "The body of (21.10.3) writes \\varGamma_T(\\mathscr{Z}^1_X).")

# ---------------------------------------------------------------- page 336 (Index terminologique)
add(336, "macro \\EGAIVterm (every entry of pp. 336-339)",
    "the terms are set in roman, normal weight ('Algèbre étale : 17.3.2.'; crop p336_s2_top.png)",
    "\\EGAIVterm sets each term in \\textbf",
    "font",
    {"old": "\\newcommand{\\EGAIVterm}[2]{\\textbf{#1}: #2.\\par}",
     "new": "\\newcommand{\\EGAIVterm}[2]{#1: #2.\\par}"},
    "One edit for all entries of pp. 336-339 (the macro is defined in this page's segment). Same as the EGA II "
    "\\egaTerme fix and the IV-2/IV-3 term macros (#1 : #2). babel-french already spaces the colon as printed.")

# ---------------------------------------------------------------- page 337
add(337, "entry 'Espace tangent ... : 16.5.13.'",
    "'Espace tangent en un préschéma en un point' (crop p337_espace.png)",
    "'Espace tangent à un préschéma en un point'",
    "misprint_in_print",
    {"old": "Espace tangent à un préschéma", "new": "Espace tangent en un préschéma"},
    "The TeX silently corrects. The body of (16.5.13) says 'espace tangent à X au point x'.",
    corrected="Espace tangent à un préschéma")

add(337, "entry 'Idéal quasi-régulier d'un faisceau d'anneaux : 16.9.1.'",
    "the final x of 'anneaux' is a bold x, mid-line (followed by ' : 16.9.1.'): ink about 211 px against 159 px for "
    "the x of 'anneaux' two lines lower (entry 'Idéal régulier d'un faisceau d'anneaux'), while the e and a of the "
    "two words match (124 and 160 px against 128 and 161 px) (side-by-side crop p337_anneaux_x_side_by_side.png)",
    "plain 'anneaux'",
    "misprint_in_print",
    {"old": "Idéal quasi-régulier d'un faisceau d'anneaux}",
     "new": "Idéal quasi-régulier d'un faisceau d'anneau\\textbf{x}}"},
    "Wrong-fount letter (GLOBAL_ISSUES 29/97). The TeX silently corrects; the fix restores the bold x. It shows "
    "only once the \\EGAIVterm macro no longer sets the whole term bold (p. 336 finding).",
    confidence="medium",
    corrected="Idéal quasi-régulier d'un faisceau d'anneaux}")

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(F, f, ensure_ascii=False, indent=1)
    f.write("\n")
print(len(F), "findings written")
