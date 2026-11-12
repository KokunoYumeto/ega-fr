"""Build findings_060_064.json and check every fix: "old" occurs exactly once in page_NNN.tex, and the fixes apply
in list order to the release file exactly as apply_fixes.py would apply them (one occurrence inside the page segment
at the time of application)."""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_II")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\BASE\native\ega2\ega2-1-fr.tex")
OUT = RUN / "findings_060_064.json"
NL = "\u23ce"  # newline placeholder in the literals below


def s(x):
    return None if x is None else x.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    item = dict(page=page, where=where, scan=scan, tex=s(tex), kind=kind, convention=conv, confidence=conf,
                fix=None if old is None else {"old": s(old), "new": s(new)})
    if kind == "misprint_in_print":
        item["corrected"] = s(corrected)
    item["note"] = note
    F.append(item)


GAMMA_NOTE = ("The print sets the Gamma of Gamma_* in bold upright (crop at 2x/3x; the Gamma of Gamma(U, O_Y) etc. is "
              "regular). ega2-1-fr.tex writes \\Gamma_* 72 times: probably a document-wide change.")
TN_NOTE = ("The print sets the whole '(TN)' in bold, parentheses included (crop: the parentheses of '(TN)' are heavier "
           "than the '(' of '(resp.'); the TeX bolds only TN. The end of ega2-1-fr.tex already writes \\textbf{(TN)}.")

# ---------------------------------------------------------------- page 60
add(60, "proof of (3.4.5), first paragraph: 'de ses sous-S-Modules gradués de type fini N_lambda'",
    "gradués in italics", r"sous-$\mathcal{S}$-Modules⏎gradués de type fini", "italics", None, "high",
    r"-Modules⏎gradués de type fini", r"-Modules⏎\emph{gradués} de type fini", "")
add(60, "proof of (3.4.5), first line: 'en prenant M=Gamma_*(F)'", "bold Gamma: M = (bold)Gamma_*(F)",
    r"$\mathcal{M}=\Gamma_*(\mathcal{F})$", "font", None, "high",
    r"$\mathcal{M}=\Gamma_*(\mathcal{F})$", r"$\mathcal{M}=\mathbf{\Gamma}_*(\mathcal{F})$", GAMMA_NOTE)
add(60, "proof of (3.4.5): 'comme X est quasi-compact ((3.4.1) et (I, 6.3.1)) et que'",
    "((3.4.1) et (I, 6.3.1)) : the second reference has its own parentheses",
    r"((\hyperref[II.3.4.1-fr]{3.4.1}) et⏎\hyperref[I.6.3.1-fr]{I, 6.3.1}) et que", "punctuation", None, "high",
    r"\hyperref[I.6.3.1-fr]{I, 6.3.1}) et que", r"(\hyperref[I.6.3.1-fr]{\textbf{I}, 6.3.1})) et que",
    "The TeX reads '((3.4.1) et I, 6.3.1)'; checked on a crop. The fix also sets the bold I (convention 2, listed "
    "next with fix null).")
add(60, "proof of (3.4.5): '(I, 6.3.1)'", "bold I", r"{I, 6.3.1}", "convention", 2, "high", None, None,
    "Applied by the fix of the preceding finding (same reference); no separate edit.")
add(60, "proof of (3.4.5): '(0, 5.2.3)'", "bold 0", r"{0, 5.2.3}", "convention", 2, "high",
    r"{0, 5.2.3}", r"{\textbf{0}, 5.2.3}", "")
add(60, "proof of (3.4.5), second paragraph: 'en raison des hypothèses sur Y (I, 9.4.9)'", "bold I", r"{I, 9.4.9}",
    "convention", 2, "high", r"{I, 9.4.9}", r"{\textbf{I}, 9.4.9}", "")
add(60, "Corollaire (3.4.6): 'Supposons vérifiées les hypothèses de (3.4.4), et en outre'",
    "(3.4.4) upright inside the italic statement", r"(\hyperref[II.3.4.4-fr]{3.4.4}), et en", "convention", 6, "high",
    r"(\hyperref[II.3.4.4-fr]{3.4.4}), et en", r"\textup{(\hyperref[II.3.4.4-fr]{3.4.4})}, et en", "")
add(60, "Corollaire (3.4.6): 'sigma : p^*(p_*(F(n))) -> F(n) (0, 4.4.3) soit surjectif'",
    "(0, 4.4.3) with bold 0, upright inside the italic statement",
    r"(\hyperref[0.4.4.3-fr]{0, 4.4.3}) soit surjectif", "convention", 2, "high",
    r"(\hyperref[0.4.4.3-fr]{0, 4.4.3}) soit surjectif",
    r"\textup{(\hyperref[0.4.4.3-fr]{\textbf{0}, 4.4.3})} soit surjectif",
    "Bold 0; the reference is also upright inside the italic statement (convention 6, listed next), so the fix "
    "sets both.")
add(60, "Corollaire (3.4.6): '(0, 4.4.3)'", "reference upright inside the italic statement",
    r"(\hyperref[0.4.4.3-fr]{0, 4.4.3}) soit surjectif", "convention", 6, "high", None, None,
    "Applied by the fix of the preceding finding (same reference); no separate edit.")
add(60, "proof of (3.4.6): 'au-dessus de p^{-1}(U) (0, 3.7.1 et 4.4.3), donc'",
    "(0, 3.7.1 et 4.4.3): no chapter number before 4.4.3",
    r"(\hyperref[0.3.7.1-fr]{0, 3.7.1} et⏎\hyperref[0.4.4.3-fr]{0, 4.4.3})", "extra", None, "high",
    r"\hyperref[0.4.4.3-fr]{0, 4.4.3}), donc", r"\hyperref[0.4.4.3-fr]{4.4.3}), donc",
    "The TeX adds '0, ' before 4.4.3 (checked on a crop); the link target stays.")
add(60, "proof of (3.4.6): '(0, 3.7.1 et 4.4.3)'", "bold 0", r"{0, 3.7.1}", "convention", 2, "high",
    r"{0, 3.7.1}", r"{\textbf{0}, 3.7.1}", "")
add(60, "Remarques (3.4.7): 's'explicite de la façon suivante (0, 4.4.1)'", "bold 0", r"{0, 4.4.1}",
    "convention", 2, "high", r"{0, 4.4.1}", r"{\textbf{0}, 4.4.1}", "")
add(60, "Remarques (3.4.7): 'engendré par ses sections au-dessus de X (0, 5.5.1)'", "bold 0", r"{0, 5.5.1}",
    "convention", 2, "high", r"{0, 5.5.1}", r"{\textbf{0}, 5.5.1}", "")
add(60, "Remarques (3.4.7): '(en appliquant (I, 1.4.1) à p_*(F))'", "bold I", r"{I, 1.4.1}", "convention", 2,
    "high", r"{I, 1.4.1}", r"{\textbf{I}, 1.4.1}", "")

# ---------------------------------------------------------------- page 61
add(61, "page break 60/61: printed p. 60 ends with 'On en conclut que lorsque Y est un préschéma quelconque, les "
        "trois conditions'; p. 61 begins 'suivantes, pour un O_X-Module'",
    "p. 61 begins with 'suivantes,'",
    r"\oldpage[II]{61}⏎⏎On en conclut que lorsque $Y$ est un préschéma quelconque, les trois⏎conditions suivantes",
    "marker", None, "high",
    r"\oldpage[II]{61}⏎⏎On en conclut que lorsque $Y$ est un préschéma quelconque, les trois⏎conditions suivantes",
    r"On en conclut que lorsque $Y$ est un préschéma quelconque, les trois⏎conditions⏎\oldpage[II]{61}⏎suivantes",
    "The marker stood before the paragraph 'On en conclut', which starts at the foot of p. 60 (indented there). "
    "The blank line that ends the p. 60 segment keeps that paragraph break; the marker moves mid-sentence "
    "(marker line without blank lines, as elsewhere in the edition).")
add(61, "Remarques (3.4.7), after the conditions a)-c): '(0, 3.5.4.4)'", "bold 0", r"{0, 3.5.4.4}", "convention", 2,
    "high", r"{0, 3.5.4.4}", r"{\textbf{0}, 3.5.4.4}", "")
add(61, "Corollaire (3.4.8): 'Supposons vérifiées les hypothèses de (3.4.4) et supposons'",
    "(3.4.4) upright inside the italic statement", r"(\hyperref[II.3.4.4-fr]{3.4.4}) et⏎supposons", "convention",
    6, "high", r"(\hyperref[II.3.4.4-fr]{3.4.4}) et⏎supposons",
    r"\textup{(\hyperref[II.3.4.4-fr]{3.4.4})} et⏎supposons", "")
add(61, "Corollaire (3.4.8): 'il existe alors un entier n_0 tel que pour n >= n_0 F soit isomorphe'",
    "no comma after n >= n_0", r"pour $n\geq n_0$, $\mathcal{F}$ soit isomorphe", "punctuation", None, "high",
    r"pour $n\geq n_0$, $\mathcal{F}$ soit isomorphe", r"pour $n\geq n_0$ $\mathcal{F}$ soit isomorphe",
    "Checked on a crop at 2x.")
add(61, "proof of (3.4.8): 'p_*(F(n)) est quasi-cohérent (I, 9.2.2, b))'", "'b)' in italics",
    r"\hyperref[I.9.2.2-fr]{I, 9.2.2, b)}", "italics", None, "high",
    r"9.2.2, b)}", r"9.2.2, \emph{b)}}", "Checked on a crop. Independent of the convention-2 edit of the same "
                                        "reference (listed next).")
add(61, "proof of (3.4.8): '(I, 9.2.2, b))'", "bold I", r"{I, 9.2.2, b)}", "convention", 2, "high",
    r"{I, 9.2.2,", r"{\textbf{I}, 9.2.2,", "")
add(61, "proof of (3.4.8): 'en vertu de l'hypothèse sur Y (I, 9.4.9)'", "bold I", r"{I, 9.4.9}", "convention", 2,
    "high", r"{I, 9.4.9}", r"{\textbf{I}, 9.4.9}", "")
add(61, "proof of (3.4.8): 'On en déduit par (3.4.6), (0, 4.3.2) et (0, 5.2.3)'", "bold 0 in (0, 4.3.2)",
    r"{0, 4.3.2}", "convention", 2, "high", r"{0, 4.3.2}", r"{\textbf{0}, 4.3.2}", "")
add(61, "proof of (3.4.8): '(0, 5.2.3)'", "bold 0", r"{0, 5.2.3}", "convention", 2, "high",
    r"{0, 5.2.3}", r"{\textbf{0}, 5.2.3}", "")
add(61, "page break 61/62: '... et un Y-morphisme | affine Phi : G(phi) -> X''",
    "one sentence across the page break, no paragraph break", r"et un $Y$-morphisme⏎⏎[\oldpage[II]{62}]⏎⏎affine",
    "other", None, "high", r"et un $Y$-morphisme⏎⏎", r"et un $Y$-morphisme⏎",
    "The blank lines around \\oldpage[II]{62} make a paragraph break inside the sentence. Apply together with the "
    "p. 62 edit '\\oldpage[II]{62}' (blank line after the marker).")

# ---------------------------------------------------------------- page 62
add(62, "page break 61/62 (start of p. 62)", "no paragraph break before 'affine'",
    r"\oldpage[II]{62}⏎⏎affine", "other", None, "high",
    r"\oldpage[II]{62}⏎⏎", r"\oldpage[II]{62}⏎",
    "Apply together with the p. 61 edit 'et un $Y$-morphisme' (blank line before the marker).")
add(62, "(3.5.1), end: 'et un Y-morphisme affine Phi : G(phi) -> X''", "'affine' in italics",
    r"affine $\Phi:G(\varphi)\to X'$", "italics", None, "high",
    r"affine $\Phi:G(\varphi)\to X'$", r"\emph{affine} $\Phi:G(\varphi)\to X'$", "Checked on a crop at 2x.")
add(62, "proof of (3.5.3): 'ainsi que leurs composants homogènes (0, 5.1.4)'", "bold 0", r"{0, 5.1.4}",
    "convention", 2, "high", r"{0, 5.1.4}", r"{\textbf{0}, 5.1.4}", "")
add(62, "proof of (3.5.3): 's'identifie à (S (x)_A A')~ (I, 1.6.5); la première assertion'", "bold I",
    r"{I, 1.6.5})~; la première", "convention", 2, "high",
    r"{I, 1.6.5})~; la première", r"{\textbf{I}, 1.6.5})~; la première", "")
add(62, "proof of (3.5.3): 'résulte alors de (2.8.10) et de (I, 3.2.6.2)'", "bold I", r"{I, 3.2.6.2}",
    "convention", 2, "high", r"{I, 3.2.6.2}", r"{\textbf{I}, 3.2.6.2}", "")
add(62, "proof of (3.5.3): 'en vertu de (2.8.10) et (I, 1.6.5); d'où la seconde assertion'",
    "'et (I, 1.6.5)' without 'de'", r"(\hyperref[II.2.8.10-fr]{2.8.10}) et de⏎(\hyperref[I.1.6.5-fr]{I, 1.6.5})~; d'où",
    "extra", None, "high", r"{2.8.10}) et de⏎(\hyperref[I.1.6.5-fr]", r"{2.8.10}) et⏎(\hyperref[I.1.6.5-fr]",
    "The TeX adds 'de' (checked on a crop). The earlier 'résulte alors de (2.8.10) et de (I, 3.2.6.2)' does have "
    "'de' in the print.")
add(62, "proof of (3.5.3): '(I, 1.6.5); d'où la seconde assertion'", "bold I", r"{I, 1.6.5})~; d'où",
    "convention", 2, "high", r"{I, 1.6.5})~; d'où", r"{\textbf{I}, 1.6.5})~; d'où", "")
add(62, "Corollaire (3.5.4): 'Avec les notations de (3.5.3), O_X'(n) s'identifie'",
    "(3.5.3) upright inside the italic statement", r"Avec les notations de (\hyperref[II.3.5.3-fr]{3.5.3}),",
    "convention", 6, "high", r"Avec les notations de (\hyperref[II.3.5.3-fr]{3.5.3}),",
    r"Avec les notations de \textup{(\hyperref[II.3.5.3-fr]{3.5.3})},", "")
add(62, "page break 62/63: '... que S est engendrée par S_1 | et que X est de type fini sur Y'",
    "one sentence across the page break, no paragraph break",
    r"engendrée par $\mathcal{S}_1$⏎⏎[\oldpage[II]{63}]⏎⏎et que", "other", None, "high",
    r"engendrée par $\mathcal{S}_1$⏎⏎", r"engendrée par $\mathcal{S}_1$⏎",
    "Apply together with the p. 63 edit '\\oldpage[II]{63}' (blank line after the marker).")

# ---------------------------------------------------------------- page 63
add(63, "page break 62/63 (start of p. 63)", "no paragraph break before 'et que X est de type fini'",
    r"\oldpage[II]{63}⏎⏎et que", "other", None, "high", r"\oldpage[II]{63}⏎⏎", r"\oldpage[II]{63}⏎",
    "Apply together with the p. 62 edit 'engendrée par $\\mathcal{S}_1$' (blank line before the marker).")
add(63, "(3.5.5): 'et que X' est de type fini sur Y' (I, 6.3.4)'", "bold I", r"{I, 6.3.4}", "convention", 2,
    "high", r"{I, 6.3.4}", r"{\textbf{I}, 6.3.4}", "")
add(63, "(3.5.5): 'il résulte alors de (3.5.4) et de (0, 4.3.3)'", "bold 0", r"{0, 4.3.3}", "convention", 2,
    "high", r"{0, 4.3.3}", r"{\textbf{0}, 4.3.3}", "")
add(63, "(3.5.5): 'On définit en outre un Psi-homomorphisme canonique theta_n : q_*(F(n)) -> q'_*(F'(n))'",
    "capital Psi: 'Ψ-homomorphisme' (same glyph as in Ψ^*(F); crop at 2x)", r"$\psi$-homomorphisme canonique",
    "misprint_in_print", None, "high", r"$\psi$-homomorphisme canonique", r"$\Psi$-homomorphisme canonique",
    "The TeX silently corrects the print. theta_n goes from a sheaf on Y to a sheaf on Y' and is defined as a map "
    "q_*(F(n)) -> psi_*(q'_*(...)) in the next sentence, so it is a psi-homomorphism (psi : Y' -> Y); "
    "Psi : X' -> X does not fit.",
    corrected=r"$\psi$-homomorphisme canonique")
add(63, "(3.5.5): 'rho_n est l'homomorphisme canonique F(n) -> Psi_*(Psi^*(F(n))) (0, 4.4.3)'", "bold 0",
    r"{0, 4.4.3}", "convention", 2, "high", r"{0, 4.4.3}", r"{\textbf{0}, 4.4.3}", "")
add(63, "(3.5.5): 'l'homomorphisme canonique (0, 3.7.2)'", "bold 0", r"{0, 3.7.2}", "convention", 2, "high",
    r"{0, 3.7.2}", r"{\textbf{0}, 3.7.2}", "")
add(63, "(3.5.5): '... -> Gamma(q'^{-1}(U'), F'(n)). La commutativité de (2.8.13.2) montre'",
    "'La commutativité' continues the paragraph (flush left, not indented)",
    r"\Gamma(q'^{-1}(U'),\mathcal{F}'(n))$.⏎⏎La commutativité", "other", None, "high",
    r"\mathcal{F}'(n))$.⏎⏎La commutativité", r"\mathcal{F}'(n))$.⏎La commutativité",
    "The TeX starts a new paragraph that the print does not have (the next paragraph, 'De même, la commutativité', "
    "is indented in the print and correctly separate).")
add(63, "(3.5.5), first diagram, bottom left: '(Gamma_*(F))~'", "bold Gamma", r"(\Gamma_*(\mathcal{F}))^{\sim}",
    "font", None, "high", r"(\Gamma_*(\mathcal{F}))", r"(\mathbf{\Gamma}_*(\mathcal{F}))", GAMMA_NOTE)
add(63, "(3.5.5), first diagram, bottom right: '(Gamma_*(F'))~'", "bold Gamma",
    r"(\Gamma_*(\mathcal{F}'))^{\sim}", "font", None, "high",
    r"(\Gamma_*(\mathcal{F}'))", r"(\mathbf{\Gamma}_*(\mathcal{F}'))", "Same as the bold Gamma above.")
add(63, "(3.5.5), second diagram, top left: 'Gamma_*(M~)'", "bold Gamma", r"\Gamma_*(\widetilde{\mathcal{M}})\ar[r]",
    "font", None, "high", r"\Gamma_*(\widetilde{\mathcal{M}})\ar[r]", r"\mathbf{\Gamma}_*(\widetilde{\mathcal{M}})\ar[r]",
    "Same as the bold Gamma above.")
add(63, "(3.5.5), second diagram, top right: 'Gamma_*(M'~)'", "bold Gamma", r"\Gamma_*(\widetilde{\mathcal{M}'})",
    "font", None, "high", r"\Gamma_*(\widetilde{\mathcal{M}'})", r"\mathbf{\Gamma}_*(\widetilde{\mathcal{M}'})",
    "Same as the bold Gamma above.")
add(63, "(3.5.6): 'où G(u^sharp) est un ouvert de X' = Proj(S')'",
    "'est' set in a bold font (wrong fount; crop at 2x/3x, compare 'où' and 's'identifie')",
    r"où $G(u^\sharp)$ est un ouvert", "misprint_in_print", None, "medium",
    r"où $G(u^\sharp)$ est un ouvert", r"où $G(u^\sharp)$ \textbf{est} un ouvert",
    "Typographical accident in the print (the word is clearly bold); the TeX has roman 'est', i.e. it silently "
    "corrects. Confidence medium only for whether the diplomatic text should reproduce a wrong fount.",
    corrected=r"où $G(u^\sharp)$ est un ouvert")
add(63, "page break 63/64: '... X'' = Proj(g^*(S)) s'identifie | canoniquement à X x_Y Y''",
    "one sentence across the page break, no paragraph break", r"s'identifie⏎⏎[\oldpage[II]{64}]⏎⏎canoniquement",
    "other", None, "high", r"s'identifie⏎⏎", r"s'identifie⏎",
    "Apply together with the p. 64 edit '\\oldpage[II]{64}' (blank line after the marker).")

# ---------------------------------------------------------------- page 64
add(64, "page break 63/64 (start of p. 64)", "no paragraph break before 'canoniquement'",
    r"\oldpage[II]{64}⏎⏎canoniquement", "other", None, "high", r"\oldpage[II]{64}⏎⏎", r"\oldpage[II]{64}⏎",
    "Apply together with the p. 63 edit \"s'identifie\" (blank line before the marker).")
add(64, "(3.5.6): 'En outre, pour tout O_Y-Module gradué quasi-cohérent M, on a un v-morphisme canonique'",
    "'pour tout 𝒪_Y-Module gradué quasi-cohérent' (crop at 2x)",
    r"pour tout $\mathcal{S}$-Module gradué quasi-cohérent $\mathcal{M}$,", "misprint_in_print", None, "high",
    r"pour tout $\mathcal{S}$-Module gradué quasi-cohérent $\mathcal{M}$,",
    r"pour tout $\mathcal{O}_Y$-Module gradué quasi-cohérent $\mathcal{M}$,",
    "The TeX silently corrects the print. M~ on X=Proj(S) and g^*(M) (x)_{g^*(S)} S' in (3.5.6.1) need a graded "
    "S-Module, so the correct reading is 'S-Module'.",
    corrected=r"pour tout $\mathcal{S}$-Module gradué quasi-cohérent $\mathcal{M}$,")
add(64, "(3.5.6.1): 'upsilon : M~ -> (g^*(M) (x)_{g^*(S)} S')~|G(u^sharp)'",
    "Greek upsilon υ (rounded bottom), not nu: the ν of (3.5.2)(ii) on p. 62 has a pointed bottom (crops at 3x)",
    r"\nu:\widetilde{\mathcal{M}}\longrightarrow", "symbol", None, "high",
    r"\nu:\widetilde{\mathcal{M}}\longrightarrow", r"\upsilon:\widetilde{\mathcal{M}}\longrightarrow",
    "Same letter in all four places on p. 64 (3.5.6.1, 'En effet, υ^♯', 'que υ^♯ est', 3.5.6.2); consistent "
    "notation, not a misprint.")
add(64, "(3.5.6): 'En effet, upsilon^sharp s'obtient en composant'", "υ^♯", r"En effet, $\nu^\sharp$", "symbol",
    None, "high", r"En effet, $\nu^\sharp$", r"En effet, $\upsilon^\sharp$", "See (3.5.6.1).")
add(64, "(3.5.6), display after 'En effet': 'v^*(M~) = w^*(p^*(M~)) -> ...'",
    "lowercase italic w: '= w^*(p^*(M~))' (crop at 2x)", r"=W^*(p^*(\widetilde{\mathcal{M}}))", "misprint_in_print",
    None, "high", r"=W^*(p^*(\widetilde{\mathcal{M}}))", r"=w^*(p^*(\widetilde{\mathcal{M}}))",
    "The TeX silently corrects the print. The morphism was introduced on p. 63 as W = Proj(u^sharp) (capital W); "
    "v = p o W, so v^* = W^* p^*.", corrected=r"=W^*(p^*(\widetilde{\mathcal{M}}))")
add(64, "(3.5.6), same display: '-> w^*((g^*(M))~) ->'", "lowercase italic w: 'w^*((g^*(M))~)'",
    r"\longrightarrow W^*((g^*(\mathcal{M}))^{\sim})", "misprint_in_print", None, "high",
    r"\longrightarrow W^*((g^*(\mathcal{M}))^{\sim})", r"\longrightarrow w^*((g^*(\mathcal{M}))^{\sim})",
    "The TeX silently corrects the print; see the previous finding.",
    corrected=r"\longrightarrow W^*((g^*(\mathcal{M}))^{\sim})")
add(64, "(3.5.6): 'la seconde est l'homomorphisme (3.5.2, (i))'", "(3.5.2, (i)) (crop at 2.5x)",
    r"\hyperref[II.3.5.2-fr]{3.5.2, (ii)}", "misprint_in_print", None, "high",
    r"{3.5.2, (ii)}", r"{3.5.2, (i)}",
    "The TeX silently corrects the print. The second arrow W^*((g^*(M))~) -> (g^*(M) (x)_{g^*(S)} S')~|G(u^sharp) "
    "is the homomorphism nu of (3.5.2)(ii) for phi = u^sharp : g^*(S) -> S' and M' = g^*(M); (3.5.2)(i) is the "
    "isomorphism (M_[phi])~ -> Phi_*(M~|G(phi)). The next sentence uses the last clause of (ii).",
    corrected=r"\hyperref[II.3.5.2-fr]{3.5.2, (ii)}")
add(64, "(3.5.6): 'il résulte de (3.5.2) que upsilon^sharp est un isomorphisme'", "υ^♯", r"$\nu^\sharp$ est un",
    "symbol", None, "high", r"$\nu^\sharp$ est un", r"$\upsilon^\sharp$ est un", "See (3.5.6.1).")
add(64, "(3.5.6): '... que upsilon^sharp est un isomorphisme.'", "'isomorphisme' in italics",
    r"est un isomorphisme.", "italics", None, "high", r"est un isomorphisme.", r"est un \emph{isomorphisme}.", "")
add(64, "(3.5.6.2): 'upsilon : O_X(n) -> O_X'(n)|G(u^sharp)'", "υ", r"\nu:\mathcal{O}_X(n)\longrightarrow", "symbol",
    None, "high", r"\nu:\mathcal{O}_X(n)\longrightarrow", r"\upsilon:\mathcal{O}_X(n)\longrightarrow",
    "See (3.5.6.1).")
add(64, "(3.6.1): 'On dit que phi est (TN)-surjectif'", "bold (TN), parentheses included",
    r"est (\textbf{TN})-\emph{surjectif}", "font", None, "high",
    r"est (\textbf{TN})-\emph{surjectif}", r"est \textbf{(TN)}-\emph{surjectif}", TN_NOTE)
add(64, "(3.6.1): '(resp. (TN)-injectif'", "bold (TN), parentheses included", r"(\textbf{TN})-\emph{injectif}",
    "font", None, "high", r"(\textbf{TN})-\emph{injectif}", r"\textbf{(TN)}-\emph{injectif}", "See (TN)-surjectif.")
add(64, "(3.6.1): '(TN)-bijectif) s'il existe n'", "bold (TN), parentheses included",
    r"(\textbf{TN})-\emph{bijectif}", "font", None, "high",
    r"(\textbf{TN})-\emph{bijectif}", r"\textbf{(TN)}-\emph{bijectif}", "See (TN)-surjectif.")
add(64, "(3.6.1): 'on ramène l'étude du morphisme ... au cas où phi est surjectif (resp. injectif, bijectif).'",
    "'surjectif', 'injectif', 'bijectif' in italics",
    r"au cas où $\varphi$ est surjectif (resp. injectif, bijectif).", "italics", None, "high",
    r"au cas où $\varphi$ est surjectif (resp. injectif, bijectif).",
    r"au cas où $\varphi$ est \emph{surjectif} (resp. \emph{injectif}, \emph{bijectif}).",
    "Three words; the same words two lines higher ('soit surjectif (resp. injectif, bijectif)') are upright in "
    "the print and in the TeX.")
add(64, "(3.6.1): 'Au lieu de dire que phi est (TN)-bijectif'", "bold (TN), parentheses included",
    r"(\textbf{TN})-bijectif", "font", None, "high",
    r"(\textbf{TN})-bijectif", r"\textbf{(TN)}-bijectif", "See (TN)-surjectif.")
add(64, "(3.6.1): 'c'est alors un (TN)-isomorphisme'", "bold (TN), parentheses included",
    r"un⏎(\textbf{TN})-isomorphisme", "font", None, "high",
    r"un⏎(\textbf{TN})", r"un⏎\textbf{(TN)}", "See (TN)-surjectif. Independent of the next edit.")
add(64, "(3.6.1): 'c'est alors un (TN)-isomorphisme.'", "'isomorphisme' in italics",
    r"(\textbf{TN})-isomorphisme.", "italics", None, "high",
    r"-isomorphisme.", r"-\emph{isomorphisme}.", "")
add(64, "Proposition (3.6.2)(i): 'est un homomorphisme (TN)-surjectif de O_Y-Algèbres graduées'",
    "(TN) bold upright, parentheses included, inside the italic statement; '-surjectif' italic",
    r"homomorphisme (\textbf{TN})-surjectif", "convention", 6, "high",
    r"homomorphisme (\textbf{TN})-surjectif", r"homomorphisme \textup{\textbf{(TN)}}-surjectif",
    "In the italic proposition \\textbf{TN} comes out bold italic; the print has bold upright (TN) (crop at 3x). "
    "The fix also makes the parentheses bold (see (3.6.1)).")
add(64, "Proposition (3.6.2)(i): 'le morphisme correspondant Phi = Proj(phi) (3.5.1) est défini'",
    "(3.5.1) upright inside the italic statement", r"(\hyperref[II.3.5.1-fr]{3.5.1}) est défini", "convention", 6,
    "high", r"(\hyperref[II.3.5.1-fr]{3.5.1}) est défini", r"\textup{(\hyperref[II.3.5.1-fr]{3.5.1})} est défini", "")
add(64, "page break 64/65, inside Proposition (3.6.2)(ii): '... d'idéaux de O_X. Soit J | le faisceau gradué ...'",
    "one sentence across the page break, no paragraph break", r"Soit⏎    $\mathcal{J}$⏎⏎[\oldpage[II]{65}]⏎⏎    le faisceau",
    "other", None, "high", r"Soit⏎    $\mathcal{J}$⏎⏎", r"Soit⏎    $\mathcal{J}$⏎",
    "The p. 65 segment begins '\\oldpage[II]{65}' + blank line + '    le faisceau gradué'; that blank line "
    "(outside pages 60-64) must also go for the paragraph break to disappear.")

# ---------------------------------------------------------------- checks
pages = {}
for p in range(60, 65):
    raw = (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    pages[p] = raw
bad = 0
for x in F:
    if x["fix"]:
        c = pages[x["page"]].count(x["fix"]["old"])
        if c != 1:
            bad += 1
            print("NOT UNIQUE in page file:", x["page"], c, repr(x["fix"]["old"]))
# sequential application on the release text, as apply_fixes.py does
t = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[II\]\{(\d+)\}")


def locate(text, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(text)]
    for i, (n, st) in enumerate(cuts):
        if n == page:
            return st, cuts[i + 1][1] if i + 1 < len(cuts) else len(text)


for x in F:
    if not x["fix"]:
        continue
    st, en = locate(t, x["page"])
    seg = t[st:en]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("SEQUENTIAL FAIL:", x["page"], c, repr(x["fix"]["old"]))
        continue
    t = t[:st] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[en:]
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
(RUN / "crops_060_064" / "simulated_after_fixes.tex").write_text(t, encoding="utf-8")
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(60, 65):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("findings", len(F), "problems", bad)
