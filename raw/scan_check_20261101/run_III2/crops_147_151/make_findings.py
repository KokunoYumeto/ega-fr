"""Build findings_147_151.json for run_III2 (EGA III part 2, pp. 147-151) and check every fix.

Strings use <NL> for a line break; it is replaced by "\n" before writing and checking.
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III2")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega3\ega3-6-fr.tex")
OUT = RUN / "findings_147_151.json"


def nl(s):
    return None if s is None else s.replace("<NL>", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": nl(tex), "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = nl(corrected)
    d["note"] = note
    F.append(d)


C2 = "Bold chapter number in the reference (convention 2)."
C6 = "The reference is upright (roman figures) inside the italic statement (convention 6)."
C6R = "'(resp.' and the closing parenthesis are upright inside the italic statement (convention 6)."
HEAVY = ("Hypertor sheaf symbol: the print sets this 𝒯or in the heavy form (roundhand T, bold italic 'or'); "
         "\\mathscr{T}\\!or gives the light form, which the print keeps for the Tor of modules (on these pages: "
         "𝒯or_n^S(ℱ, 𝒢) p. 148, 𝒯or_0^S(ℱ, 𝒢), (6.5.4.1), (6.5.4.2) p. 149, (6.5.8) p. 150). Page fix \\boldsymbol "
         "as on p. 146; the T shape is a document-wide decision (GLOBAL_ISSUES items 42, 52).")
HSCAN = "heavy hypertor form (bold italic 'or', crop)"
COV = "Covered by the edit of the preceding finding."


def heavy(page, where, old, new, tex=r"\mathscr{T}\!or (light)"):
    add(page, where, HSCAN, tex, "font", None, "high", old, new, HEAVY)
PAR = "GLOBAL_ISSUES item 20: the blank line before the page marker makes a paragraph break the print does not have."

# ---------------------------------------------------------------- page 147
add(147, "(6.4.4), 'Considérons les complexes u*(𝒫.) = (P.⊗_B B^(1))~ de 𝒪_X(1)-Modules'",
    "u*(𝒫.) = (𝒫.⊗_B B^(1))~ : script 𝒫 inside the parenthesis (enlarged crop)",
    r"(P_\bullet\otimes_B B^{(1)})^{\sim}", "misprint_in_print", None, "high",
    r"(P_\bullet\otimes_B B^{(1)})^{\sim}", r"(\mathscr P_\bullet\otimes_B B^{(1)})^{\sim}",
    "The print has the sheaf letter 𝒫 where the complex of B-modules P. is meant (cf. v*(𝒬.) = (Q.⊗_C C^(1))~ "
    "just after). The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"(P_\bullet\otimes_B B^{(1)})^{\sim}")
add(147, "(6.4.4), after (6.4.4.2): 'un morphisme de bi-∂-foncteurs dans les catégories'",
    "bi-∂-foncteurs in italics", r"bi-$\partial$-foncteurs (upright)", "italics", None, "high",
    r"morphisme de bi-$\partial$-foncteurs dans", r"morphisme de \emph{bi-$\partial$-foncteurs} dans",
    "Italic in the print (enlarged crop).")
heavy(147, "(6.4.4.1), left side: 'θ : 𝒯or^S_•(𝒫., 𝒬.)'", r"\theta:\mathscr{T}\!or", r"\theta:\boldsymbol{\mathscr{T}\!or}")
heavy(147, "(6.4.4.1), right side: '𝒯or^S_•(u*(𝒫.), v*(𝒬.))'",
      r"\mathscr{T}\!or_\bullet^S<NL>  (u^*(\mathscr P_\bullet),v^*(\mathscr Q_\bullet))<NL>  \tag{6.4.4.1}",
      r"\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>  (u^*(\mathscr P_\bullet),v^*(\mathscr Q_\bullet))<NL>  \tag{6.4.4.1}")
heavy(147, "(6.4.4.2), left side: '(u ×_S v)*(𝒯or^S_•(𝒫., 𝒬.))'",
      r"(u\times_S v)^*<NL>  \bigl(\mathscr{T}\!or", r"(u\times_S v)^*<NL>  \bigl(\boldsymbol{\mathscr{T}\!or}")
heavy(147, "(6.4.4.2), right side: '𝒯or^S_•(u*(𝒫.), v*(𝒬.))'",
      r"\mathscr{T}\!or_\bullet^S<NL>  (u^*(\mathscr P_\bullet),v^*(\mathscr Q_\bullet))<NL>  \tag{6.4.4.2}",
      r"\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>  (u^*(\mathscr P_\bullet),v^*(\mathscr Q_\bullet))<NL>  \tag{6.4.4.2}")
add(147, "Lemme (6.4.5): 'Avec les notations de (6.4.4), supposons'", "(6.4.4) upright in the italic statement",
    "(6.4.4) inside the italic namedtheorem: italic", "convention", 6, "high",
    "Avec les notations de (6.4.4), supposons", r"Avec les notations de \textup{(6.4.4)}, supposons", C6)
add(147, "Lemme (6.4.5): 'alors l'homomorphisme (6.4.4.2) est bijectif'", "(6.4.4.2) upright in the italic statement",
    "(6.4.4.2) inside the italic namedtheorem: italic", "convention", 6, "high",
    "(6.4.4.2) est bijectif", r"\textup{(6.4.4.2)} est bijectif", C6)
add(147, "Proof of (6.4.5): 'en vertu des définitions (6.4.4) et de (0_I, 4.4.8)'", "(𝟎_I, 4.4.8): bold 0",
    r"($0_{\mathrm I}$, 4.4.8)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 4.4.8)", r"($\mathbf{0}_{\mathrm I}$, 4.4.8)", C2)
heavy(147, "(6.4.5.1), left side: '(u_1 ×_S v_1)*(𝒯or^S_•(u*(𝒫.), v*(𝒬.)))'",
      r"\bigl(\mathscr{T}\!or_\bullet^S<NL>    (u^*", r"\bigl(\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>    (u^*")
add(147, "(6.4.5.1), right side: '𝒯or^S_•(u'*(𝒫.), v'*(𝒬.))'",
    "u'*(𝒫.), v'*(𝒬.): prime and star directly on u, v, no parentheses around u', v' (enlarged crop)",
    r"((u')^*(\mathscr P_\bullet),(v')^*(\mathscr Q_\bullet))", "formula", None, "high",
    r"\mathscr{T}\!or_\bullet^S<NL>  ((u')^*(\mathscr P_\bullet),(v')^*(\mathscr Q_\bullet))<NL>  \tag{6.4.5.1}",
    r"\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>  (u'^*(\mathscr P_\bullet),v'^*(\mathscr Q_\bullet))<NL>  \tag{6.4.5.1}",
    "The TeX adds parentheses around u' and v' (u'^* is valid TeX: prime and star in one superscript). "
    "One edit for this finding and the next (heavy hypertor form of this 𝒯or).")
add(147, "(6.4.5.1), right side: the 𝒯or", HSCAN, r"\mathscr{T}\!or (light)", "font", None, "high", None, None,
    COV + " " + HEAVY)
heavy(147, "(6.4.5.2), left side: '(u' ×_S v')*(𝒯or^S_•(𝒫., 𝒬.))'",
      r"(u'\times_S v')^*<NL>  \bigl(\mathscr{T}\!or", r"(u'\times_S v')^*<NL>  \bigl(\boldsymbol{\mathscr{T}\!or}")
add(147, "(6.4.5.2), right side: '𝒯or^S_•(u'*(𝒫.), v'*(𝒬.))'",
    "u'*(𝒫.), v'*(𝒬.): no parentheses around u', v' (enlarged crop)",
    r"((u')^*(\mathscr P_\bullet),(v')^*(\mathscr Q_\bullet))", "formula", None, "high",
    r"\mathscr{T}\!or_\bullet^S<NL>  ((u')^*(\mathscr P_\bullet),(v')^*(\mathscr Q_\bullet))<NL>  \tag{6.4.5.2}",
    r"\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>  (u'^*(\mathscr P_\bullet),v'^*(\mathscr Q_\bullet))<NL>  \tag{6.4.5.2}",
    "Same as in (6.4.5.1). One edit for this finding and the next (heavy hypertor form of this 𝒯or).")
add(147, "(6.4.5.2), right side: the 𝒯or", HSCAN, r"\mathscr{T}\!or (light)", "font", None, "high", None, None,
    COV + " " + HEAVY)
add(147, "Proof of (6.4.5): 'u*(𝒫.) (resp. v*(𝒬.)) s'identifie alors à (P.)_f~'",
    "(P.)~ with subscript f under the tilde, on the closing parenthesis; no outer parentheses (enlarged crop)",
    r"((P_\bullet)_f)^{\sim}", "formula", None, "high",
    r"((P_\bullet)_f)^{\sim}", r"(P_\bullet)_f^{\sim}", "The TeX adds an outer pair of parentheses.")
add(147, "Proof of (6.4.5): '(resp. (Q.)_g~)'", "(Q.)~ with subscript g, no outer parentheses",
    r"((Q_\bullet)_g)^{\sim}", "formula", None, "high",
    r"((Q_\bullet)_g)^{\sim}", r"(Q_\bullet)_g^{\sim}", "The TeX adds an outer pair of parentheses.")
add(147, "Proof of (6.4.5): 'X×_S Y = Spec(B⊗_A C) (II, 4.3.2.4)'", "(𝐈𝐈, 4.3.2.4): bold II",
    "(II, 4.3.2.4)", "convention", 2, "high", "(II, 4.3.2.4)", r"(\textbf{II}, 4.3.2.4)", C2)
add(147, "End of the page: after (6.4.5.3), before \\oldpage[III]{148}",
    "the sentence runs on to p. 148 ('l'homomorphisme (6.4.5.3) déduit par fonctorialité ... est bijectif'); "
    "'déduit' is not indented",
    r"blank line after \] before the page marker: new paragraph", "other", None, "high",
    r"\label{III.6.4.5.3.fr}<NL>\]<NL><NL>", r"\label{III.6.4.5.3.fr}<NL>\]<NL>", PAR)

# ---------------------------------------------------------------- page 148
add(148, "Proof of (6.4.5): 'Or (0_I, 1.6.1), on peut écrire'", "(𝟎_I, 1.6.1): bold 0",
    r"($0_{\mathrm I}$, 1.6.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 1.6.1), on peut", r"($\mathbf{0}_{\mathrm I}$, 1.6.1), on peut", C2)
add(148, "Proof of (6.4.5): 'La conclusion résulte alors de (0_I, 1.6.1) appliqué'", "(𝟎_I, 1.6.1): bold 0",
    r"($0_{\mathrm I}$,<NL>1.6.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$,<NL>1.6.1) appliqué", r"($\mathbf{0}_{\mathrm I}$,<NL>1.6.1) appliqué", C2)
add(148, "(6.4.6.1), first line: '(u ×_S v)*('ℰ(𝒫., 𝒬.))'",
    "the v of (u ×_S v)* is bold italic in the first line, normal in the second (enlarged side-by-side crop)",
    r"(u\times_S v)^*", "misprint_in_print", None, "high",
    r"(u\times_S v)^*\bigl('\mathscr E", r"(u\times_S \boldsymbol{v})^*\bigl('\mathscr E",
    "Wrong-font letter (GLOBAL_ISSUES item 29). The TeX silently corrects; the fix reproduces the bold v.",
    corrected=r"(u\times_S v)^*\bigl('\mathscr E")
add(148, "(6.4.6.1), end of the first line", "no comma after '... v*(𝒬.))'", r"v^*(\mathscr Q_\bullet)),\\",
    "punctuation", None, "high", r"v^*(\mathscr Q_\bullet)),\\", r"v^*(\mathscr Q_\bullet))\\",
    "The print has no punctuation at the ends of the two lines (enlarged crop).")
add(148, "(6.4.6.1), end of the second line", "no full stop after '... v*(𝒬.))'", r"v^*(\mathscr Q_\bullet)).",
    "punctuation", None, "high", r"v^*(\mathscr Q_\bullet)).<NL>  \end{aligned}",
    r"v^*(\mathscr Q_\bullet))<NL>  \end{aligned}", "No full stop in the print (enlarged crop).")
add(148, "(6.4.6): 'lorsque u et v sont des immersions ouvertes, les homomorphismes'",
    "immersions ouvertes in italics", "immersions ouvertes (upright)", "italics", None, "high",
    "des<NL>immersions ouvertes, les", r"des<NL>\emph{immersions ouvertes}, les", "Italic in the print.")
add(148, "(6.4.6): 'les homomorphismes (6.4.6.1) sont bijectifs : en effet'", "bijectifs in italics",
    "bijectifs (upright)", "italics", None, "high",
    "sont bijectifs : en effet", r"sont \emph{bijectifs} : en effet", "Italic in the print.")
add(148, "(6.4.6): 'à l'aide de (0, 11.1.2)'", "(𝟎, 11.1.2): bold 0", "(0, 11.1.2)", "convention", 2, "high",
    "(0, 11.1.2)", r"(\textbf{0}, 11.1.2)", C2)
add(148, "(6.4.6): 'et (0, 11.2.4).'", "(𝟎, 11.2.4): bold 0", "(0, 11.2.4)", "convention", 2, "high",
    "(0, 11.2.4)", r"(\textbf{0}, 11.2.4)", C2)
add(148, "Heading 6.5: 'Foncteurs hypertor locaux de complexes de Modules quasi-cohérents : cas général.'",
    "the title ends with a full stop", r"\subsection{... : cas général} (no full stop)", "punctuation", None,
    "high", "quasi-cohérents : cas général}", "quasi-cohérents : cas général.}",
    "As GLOBAL_ISSUES item 43 for ega3-1; most \\subsection titles in ega3-6-fr.tex lack the printed stop too.")
add(148, "(6.5.1), 2nd paragraph: 'de degré 0, ℱ et 𝒢, (les autres étant nuls)'",
    "comma after 𝒢 before the parenthesis (enlarged crop)", r"$\mathscr F$ et $\mathscr G$ (les",
    "punctuation", None, "high", r"$\mathscr F$ et $\mathscr G$ (les", r"$\mathscr F$ et $\mathscr G$, (les",
    "The printed comma is missing in the TeX.")
heavy(148, "(6.5.1): 'nous allons définir des 𝒪_Z-Modules quasi-cohérents 𝒯or_n^S(𝒫., 𝒬.) dits hypertor locaux'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ dits",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ dits")
heavy(148, "(6.5.1), 2nd paragraph: 'au lieu de 𝒯or_n^S(𝒫., 𝒬.)' (the 𝒯or_n^S(ℱ, 𝒢) before it is light, as in the TeX)",
      r"au lieu de<NL>$\mathscr{T}\!or_n^S", r"au lieu de<NL>$\boldsymbol{\mathscr{T}\!or}_n^S")
add(148, "(6.5.2): 'Supposons d'abord S affine'", "affine in italics", "affine (upright)", "italics", None, "high",
    r"Supposons d'abord $S$ affine", r"Supposons d'abord $S$ \emph{affine}", "Italic in the print.")
add(148, "(6.5.2): 'un 𝒪_Z_λμ-Module quasi-cohérent ℱ_λμ = 𝒯or^S_n(𝒫_λ., 𝒬_μ.), et il faut montrer'",
    "the formula is inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"quasi-cohérent<NL>\[<NL>  \mathscr F_{\lambda\mu}<NL>  =\mathscr{T}\!or_n^S<NL>"
    r"   (\mathscr P_{\lambda\bullet},\mathscr Q_{\mu\bullet}),<NL>\]<NL>et il faut",
    r"quasi-cohérent<NL>$\mathscr F_{\lambda\mu}<NL>  =\boldsymbol{\mathscr{T}\!or}_n^S<NL>"
    r"   (\mathscr P_{\lambda\bullet},\mathscr Q_{\mu\bullet})$,<NL>et il faut",
    "Display of a formula the print sets inline (as GLOBAL_ISSUES item 21). One edit for this finding and the next "
    "(heavy hypertor form of this 𝒯or); without it: \\mathscr{T}\\!or in the new text.")
add(148, "(6.5.2): the 𝒯or of 'ℱ_λμ = 𝒯or^S_n(𝒫_λ., 𝒬_μ.)'", HSCAN, r"\mathscr{T}\!or (light)", "font", None, "high",
    None, None, COV + " " + HEAVY)
add(148, "(6.5.2): 'la condition de recollement (0_I, 3.3.1)'", "(𝟎_I, 3.3.1): bold 0",
    r"($0_{\mathrm I}$, 3.3.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 3.3.1)", r"($\mathbf{0}_{\mathrm I}$, 3.3.1)", C2)
add(148, "(6.5.2): 'que le 𝒪_Z-Module ainsi défini'",
    "'Module' in bold (wrong font; side-by-side crop with the normal 'Module' two lines up the page)",
    r"$\mathscr O_Z$-Module (roman)", "misprint_in_print", None, "high",
    r"$\mathscr O_Z$-Module ainsi", r"$\mathscr O_Z$-\textbf{Module} ainsi",
    "Wrong-font word (GLOBAL_ISSUES item 29). The TeX silently corrects; the fix reproduces the bold.",
    corrected=r"$\mathscr O_Z$-Module ainsi")
heavy(148, "(6.5.2): 'de ces restrictions sur 𝒯or_n^S(𝒫.|U, 𝒬.|V) (6.4.5)'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ (6.4.5)",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ (6.4.5)")
add(148, "(6.5.2), last line: 'des recouvrements ouverts (X_λ), (Y_μ) consi-'",
    "'(X_λ), (Y_μ)' between 'ouverts' and 'consi-'; the opening parenthesis of (X_λ) is bold",
    "recouvrements ouverts consi (the two families are missing)", "missing", None, "high",
    "recouvrements ouverts consi", r"recouvrements ouverts $\boldsymbol{(}X_\lambda)$, $(Y_\mu)$ consi",
    "Missing words. The insertion reproduces the printed bold '(' (wrong-font sort, recorded as a misprint in the "
    "next finding); without it the text is $(X_\\lambda)$, $(Y_\\mu)$.")
add(148, "(6.5.2), last line: '(X_λ)'",
    "bold opening parenthesis (about 1.6 times the ink of the other parentheses; X_λ as elsewhere)",
    "the text is missing in the TeX (previous finding)", "misprint_in_print", None, "medium", None, None,
    "Wrong-font sort. Its diplomatic edit is part of the preceding 'missing' finding; apply that one.",
    corrected=r"$(X_\lambda)$")

# ---------------------------------------------------------------- page 149
heavy(149, "(6.5.2): 'nous le noterons donc 𝒯or_n^S(𝒫., 𝒬.);'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$; il",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$; il")
add(149, "(6.5.2): 'il résulte enfin de (6.4.5) que pour toute partie ouverte U'", "toute in italics",
    "toute (upright)", "italics", None, "high", "que pour toute partie", r"que pour \emph{toute} partie",
    "Italic in the print.")
heavy(149, "(6.5.2): 'la restriction de 𝒯or_n^S(𝒫., 𝒬.) à U ×_S V'",
      r"restriction de $\mathscr{T}\!or", r"restriction de $\boldsymbol{\mathscr{T}\!or}")
heavy(149, "(6.5.2): 'canoniquement isomorphe à 𝒯or_n^S(𝒫.|U, 𝒬.|V).'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$.<NL>\end{env}",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$.<NL>\end{env}")
add(149, "(6.5.3), first line: 'où S est quelconque, et soit (S_α)'",
    "'et' in bold (side-by-side crop with other 'et' on the page)", "et (roman)", "misprint_in_print", None,
    "high", "est quelconque, et soit", r"est quelconque, \textbf{et} soit",
    "Wrong-font word (GLOBAL_ISSUES item 29). The TeX silently corrects; the fix reproduces the bold.",
    corrected="est quelconque, et soit")
add(149, "(6.5.3): 'l'image réciproque de S_α dans X'",
    "'de' in bold (side-by-side crop with other 'de' on the page)", "de (roman)", "misprint_in_print", None,
    "high", r"réciproque de $S_\alpha$", r"réciproque \textbf{de} $S_\alpha$",
    "Wrong-font word (GLOBAL_ISSUES item 29). The TeX silently corrects; the fix reproduces the bold.",
    corrected=r"réciproque de $S_\alpha$")
add(149, "(6.5.3): 'les faisceaux 𝒯or^{S_α}_n(𝒫.|X_α, 𝒬.|Y_α) = 𝒢_α vérifient'",
    "the formula is inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"les faisceaux<NL>\[<NL>  \mathscr{T}\!or_n^{S_\alpha}<NL>"
    r"  (\mathscr P_\bullet|X_\alpha,\mathscr Q_\bullet|Y_\alpha)<NL>  =\mathscr G_\alpha<NL>\]<NL>vérifient",
    r"les faisceaux<NL>$\boldsymbol{\mathscr{T}\!or}_n^{S_\alpha}<NL>"
    r"  (\mathscr P_\bullet|X_\alpha,\mathscr Q_\bullet|Y_\alpha)<NL>  =\mathscr G_\alpha$<NL>vérifient",
    "Display of a formula the print sets inline (as GLOBAL_ISSUES item 21). One edit for this finding and the next "
    "(heavy hypertor form of this 𝒯or); without it: \\mathscr{T}\\!or in the new text.")
add(149, "(6.5.3): the 𝒯or of '𝒯or^{S_α}_n(𝒫.|X_α, 𝒬.|Y_α) = 𝒢_α'", HSCAN, r"\mathscr{T}\!or (light)", "font", None,
    "high", None, None, COV + " " + HEAVY)
heavy(149, "(6.5.3): 'des restrictions de 𝒢_α et 𝒢_β à U ×_S V ... sur 𝒯or_n^T(𝒫.|U, 𝒬.|V); on peut'",
      r"$\mathscr{T}\!or_n^T(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$; on",
      r"$\boldsymbol{\mathscr{T}\!or}_n^T(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$; on")
heavy(149, "(6.5.3): 'mais alors 𝒯or_n^T(𝒫.|U, 𝒬.|V) est canoniquement isomorphe'",
      r"$\mathscr{T}\!or_n^T(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ est",
      r"$\boldsymbol{\mathscr{T}\!or}_n^T(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ est")
heavy(149, "(6.5.3): '𝒯or_n^{S_α}(𝒫.|U, 𝒬.|V) d'une part'",
      r"$\mathscr{T}\!or_n^{S_\alpha}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$<NL>d'une",
      r"$\boldsymbol{\mathscr{T}\!or}_n^{S_\alpha}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$<NL>d'une")
heavy(149, "(6.5.3): 'à 𝒯or_n^{S_β}(𝒫.|U, 𝒬.|V) d'autre part'",
      r"$\mathscr{T}\!or_n^{S_\beta}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$<NL>d'autre",
      r"$\boldsymbol{\mathscr{T}\!or}_n^{S_\beta}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$<NL>d'autre")
heavy(149, "(6.5.3): 'de 𝒢_α sur 𝒯or_n^{S_α}(𝒫.|U, 𝒬.|V) et'",
      r"$\mathscr{T}\!or_n^{S_\alpha}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ et",
      r"$\boldsymbol{\mathscr{T}\!or}_n^{S_\alpha}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ et")
heavy(149, "(6.5.3): 'de 𝒢_β sur 𝒯or_n^{S_β}(𝒫.|U, 𝒬.|V) (6.5.2)'",
      r"$\mathscr{T}\!or_n^{S_\beta}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$<NL>(6.5.2)",
      r"$\boldsymbol{\mathscr{T}\!or}_n^{S_\beta}(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$<NL>(6.5.2)")
heavy(149, "(6.5.3): 'cela achève de définir le 𝒪_Z-Module 𝒯or_n^S(𝒫., 𝒬.).'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$. En",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$. En")
heavy(149, "(6.5.3): '𝒯or_n^S(𝒫.|U, 𝒬.|V) est canoniquement isomorphe à la restriction'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ est",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet|U,\mathscr Q_\bullet|V)$ est")
heavy(149, "(6.5.3): 'la restriction de 𝒯or_n^S(𝒫., 𝒬.) à U ×_S V.'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ à $U",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ à $U")
add(149, "(6.5.3), 2nd paragraph: 'un bi-∂-foncteur 𝒯or^S_•(𝒫., 𝒬.) à valeurs'",
    "bi-∂-foncteur in italics (the later 'de bi-∂-foncteurs' is upright, as in the TeX)",
    r"bi-$\partial$-foncteur (upright)", "italics", None, "high",
    r"un bi-$\partial$-foncteur", r"un \emph{bi-$\partial$-foncteur}", "Italic in the print (enlarged crop).")
heavy(149, "(6.5.3), 2nd paragraph: 'un bi-∂-foncteur 𝒯or_•^S(𝒫., 𝒬.) à valeurs'",
      r"$\mathscr{T}\!or_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ à valeurs",
      r"$\boldsymbol{\mathscr{T}\!or}_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ à valeurs")
add(149, "(6.5.3): 'défini dans (I, 9.1.2)'", "(𝐈, 9.1.2): bold I", "(I, 9.1.2)", "convention", 2, "high",
    "(I, 9.1.2)", r"(\textbf{I}, 9.1.2)", C2)
add(149, "(6.5.3): 'cela résulte en effet de (I, 9.1.3)'", "(𝐈, 9.1.3): bold I", "(I, 9.1.3)", "convention", 2,
    "high", "(I, 9.1.3)", r"(\textbf{I}, 9.1.3)", C2)
heavy(149, "(6.5.4): 'que 𝒯or_•^S(𝒫., 𝒬.) est l'aboutissement'",
      r"que $\mathscr{T}\!or_\bullet^S", r"que $\boldsymbol{\mathscr{T}\!or}_\bullet^S")
add(149, "(6.5.4.1)", "'ℰ^2_pq = ℋ_p(𝒯or^S_q(𝒫., 𝒬.) — one closing parenthesis only (enlarged crop)",
    r"\mathscr H_p\bigl(\mathscr{T}\!or_q^S(\mathscr P_\bullet,\mathscr Q_\bullet)\bigr)", "misprint_in_print",
    None, "high", r"(\mathscr P_\bullet,\mathscr Q_\bullet)\bigr)<NL>  \tag{6.5.4.1}",
    r"(\mathscr P_\bullet,\mathscr Q_\bullet)<NL>  \tag{6.5.4.1}",
    "The print omits the parenthesis closing ℋ_p(. The TeX silently corrects; the fix restores the printed "
    "reading (an unmatched \\bigl( is valid TeX).",
    corrected=r"\mathscr H_p\bigl(\mathscr{T}\!or_q^S(\mathscr P_\bullet,\mathscr Q_\bullet)\bigr)")
add(149, "(6.5.4.2), end", "no full stop after the formula (enlarged crop)",
    r"\mathscr H_{q''}(\mathscr Q_\bullet)\bigr).", "punctuation", None, "high",
    r"\mathscr H_{q''}(\mathscr Q_\bullet)\bigr).<NL>  \tag{6.5.4.2}",
    r"\mathscr H_{q''}(\mathscr Q_\bullet)\bigr)<NL>  \tag{6.5.4.2}", "No full stop in the print.")
add(149, "(6.5.4), after (6.5.4.2): 'La suite spectrale (6.5.4.2) est toujours régulière'",
    "new paragraph (indented line)", r"\]<NL>La suite spectrale (no blank line: the paragraph continues)", "other",
    None, "high", r"\]<NL>La suite spectrale", r"\]<NL><NL>La suite spectrale",
    "Paragraph break as printed.")
add(149, "(6.5.4): 'si 𝒫. et 𝒬. sont limités inférieurement'", "limités inférieurement in italics",
    "limités inférieurement (upright)", "italics", None, "high",
    "sont limités<NL>inférieurement. Un autre", r"sont \emph{limités<NL>inférieurement}. Un autre",
    "Italic in the print.")
add(149, "(6.5.5), last line: 'si les 𝒜_t sont des anneaux locaux (commutatifs) noethériens,'",
    "anneaux locaux (commutatifs) noethériens in italics", "upright", "italics", None, "high",
    "des anneaux locaux<NL>(commutatifs) noethériens", r"des \emph{anneaux locaux<NL>(commutatifs) noethériens}",
    "Italic in the print. Independent of the next edit (the two strings do not overlap).")
add(149, "End of the page: 'noethériens,' before \\oldpage[III]{150}",
    "the sentence runs on to p. 150 ('noethériens, dire qu'ils sont ...'), no paragraph break",
    "blank line before the page marker: new paragraph", "other", None, "high", ",<NL><NL>", ",<NL>", PAR)

# ---------------------------------------------------------------- page 150
add(150, "(6.5.5): 'qu'ils sont réguliers et de'", "réguliers in italics", "réguliers (upright)", "italics", None,
    "high", "réguliers et", r"\emph{réguliers} et", "Italic in the print.")
add(150, "(6.5.5): 'et de dimension (de Krull) ⩽ n'", "dimension in italics ('(de Krull)' upright)",
    "dimension (upright)", "italics", None, "high", "dimension (de Krull)", r"\emph{dimension} (de Krull)",
    "Italic in the print.")
add(150, "(6.5.5): '(0_IV, 17.3.1)'", "(𝟎_IV, 17.3.1): bold 0", r"($0_{\mathrm{IV}}$, 17.3.1)", "convention", 2,
    "high", r"($0_{\mathrm{IV}}$, 17.3.1)", r"($\mathbf{0}_{\mathrm{IV}}$, 17.3.1)", C2)
add(150, "(6.5.5): 'qu'un préschéma localement noethérien T'", "préschéma localement noethérien in italics",
    "upright", "italics", None, "high", "qu'un préschéma localement noethérien $T$",
    r"qu'un \emph{préschéma localement noethérien} $T$", "Italic in the print.")
add(150, "(6.5.5): 'T est de dimension cohomologique ⩽ n, ou de dire'", "dimension cohomologique in italics ('de' upright)",
    "upright", "italics", None, "high", r"est de dimension cohomologique $\leqslant n$, ou",
    r"est de \emph{dimension cohomologique} $\leqslant n$, ou", "Italic in the print.")
add(150, "(6.5.5): 'qu'il est régulier (0_I, 4.1.4)'", "régulier in italics", "régulier (upright)", "italics", None,
    "high", "est régulier", r"est \emph{régulier}", "Italic in the print.")
add(150, "(6.5.5): '(0_I, 4.1.4)'", "(𝟎_I, 4.1.4): bold 0", r"($0_{\mathrm I}$, 4.1.4)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 4.1.4)", r"($\mathbf{0}_{\mathrm I}$, 4.1.4)", C2)
add(150, "(6.5.5): 'et de dimension ⩽ n; cela signifie'", "dimension in italics", "dimension (upright)", "italics",
    None, "high", r"dimension $\leqslant n$; cela", r"\emph{dimension} $\leqslant n$; cela", "Italic in the print.")
add(150, "(6.5.5): 'Γ(U, 𝒪_T) est de dimension cohomologique ⩽ n'",
    "de dimension cohomologique in italics ('de' included)", "upright", "italics", None, "high",
    "est de<NL>dimension cohomologique", r"est \emph{de<NL>dimension cohomologique}", "Italic in the print.")
add(150, "(6.5.5): '(0_IV, 17.2.6)'", "(𝟎_IV, 17.2.6): bold 0", r"($0_{\mathrm{IV}}$, 17.2.6)", "convention", 2,
    "high", r"($0_{\mathrm{IV}}$, 17.2.6)", r"($\mathbf{0}_{\mathrm{IV}}$, 17.2.6)", C2)
add(150, "(6.5.5): 'si S est localement noethérien et de dimension cohomologique finie, les'",
    "localement noethérien et de dimension cohomologique finie in italics", "upright", "italics", None, "high",
    "est localement<NL>noethérien et de dimension cohomologique finie, les",
    r"est \emph{localement<NL>noethérien et de dimension cohomologique finie}, les", "Italic in the print.")
add(150, "(6.5.5): 'sont birégulières.'", "birégulières in italics", "birégulières (upright)", "italics", None,
    "high", "sont birégulières.", r"sont \emph{birégulières}.", "Italic in the print.")
heavy(150, "(6.5.5), last paragraph: 'Il est clair que 𝒯or_•^S(𝒫., 𝒬.) se transforme'",
      r"$\mathscr{T}\!or_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ se",
      r"$\boldsymbol{\mathscr{T}\!or}_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ se")
heavy(150, "(6.5.5), last paragraph: 'se transforme en 𝒯or_•^S(𝒬., 𝒫.)'",
      r"$\mathscr{T}\!or_\bullet^S(\mathscr Q_\bullet,\mathscr P_\bullet)$",
      r"$\boldsymbol{\mathscr{T}\!or}_\bullet^S(\mathscr Q_\bullet,\mathscr P_\bullet)$")
add(150, "(6.5.6.1), left side: 'lim→ (𝒯or^S_•(𝒫_α., 𝒬.))'",
    "lim with the arrow and no index; the 𝒯or term is enclosed in parentheses (enlarged crop)",
    r"\varinjlim_\alpha \mathscr{T}\!or_\bullet^S(\mathscr P_{\alpha\bullet},\mathscr Q_\bullet)", "formula", None,
    "high",
    r"\varinjlim_\alpha<NL>  \mathscr{T}\!or_\bullet^S<NL>  (\mathscr P_{\alpha\bullet},\mathscr Q_\bullet)<NL>",
    r"\varinjlim<NL>  (\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>  (\mathscr P_{\alpha\bullet},\mathscr Q_\bullet))<NL>",
    "The TeX adds the index α (cf. GLOBAL_ISSUES item 30) and lacks the printed parentheses. One edit for this "
    "finding and the next (heavy hypertor form of this 𝒯or); without it: \\mathscr{T}\\!or in the new text.")
add(150, "(6.5.6.1), left side: the 𝒯or", HSCAN, r"\mathscr{T}\!or (light)", "font", None, "high", None, None,
    COV + " " + HEAVY)
heavy(150, "(6.5.6.1), right side: the 𝒯or of '𝒯or^S_•(lim→ 𝒫_α., 𝒬.)'",
      r"\xrightarrow{\sim}<NL>  \mathscr{T}\!or_\bullet^S", r"\xrightarrow{\sim}<NL>  \boldsymbol{\mathscr{T}\!or}_\bullet^S")
add(150, "(6.5.6.1), right side: the lim of '𝒯or^S_•(lim→ 𝒫_α., 𝒬.)'", "lim with the arrow and no index",
    r"\varinjlim_\alpha\mathscr P_{\alpha\bullet}", "formula", None, "high",
    r"\left(\varinjlim_\alpha\mathscr P_{\alpha\bullet}", r"\left(\varinjlim\mathscr P_{\alpha\bullet}",
    "The TeX adds the index α.")
heavy(150, "Remarques (6.5.7) (i): 'alors les 𝒯or_n^S(𝒫., 𝒬.) sont des 𝒪_S-Modules'",
      r"$\mathscr{T}\!or_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ sont",
      r"$\boldsymbol{\mathscr{T}\!or}_n^S(\mathscr P_\bullet,\mathscr Q_\bullet)$ sont")
heavy(150, "(6.5.7.1), left side: '(𝒯or_n^S(𝒫., 𝒬.))_z'",
      r"\bigl(\mathscr{T}\!or_n^S", r"\bigl(\boldsymbol{\mathscr{T}\!or}_n^S")
add(150, "Remarques (6.5.7) (ii): 'au cas de deux complexes de 𝒪_X-Modules 𝒫., 𝒬.'",
    "deux complexes de 𝒪_X-Modules in italics (remark body roman)", "no emphasis", "italics", None, "high",
    r"cas de<NL>deux complexes de $\mathscr O_X$-Modules $\mathscr P_\bullet$",
    r"cas de<NL>\emph{deux complexes de $\mathscr O_X$-Modules} $\mathscr P_\bullet$",
    "Judged with the remark body roman, as instructed (the TeX sets this remark with namedtheorem, italic).")
add(150, "Remarques (6.5.7) (ii): 'sur un même espace annelé (X, 𝒪_X)'", "espace annelé in italics",
    "no emphasis", "italics", None, "high", "même espace annelé", r"même \emph{espace annelé}",
    "Remark body judged roman.")
add(150, "Remarques (6.5.7) (ii): 'les A(U)-modules Tor_n^{A(U)}(P.(U), Q.(U)) forment alors'",
    "the formula is inline in the running text", r"displayed with \[ ... \]", "other", None, "high",
    r"les $A(U)$-modules<NL>\[<NL>  \mathbf{Tor}_n^{A(U)}(P_\bullet(U),Q_\bullet(U))<NL>\]<NL>forment",
    r"les $A(U)$-modules<NL>$\mathbf{Tor}_n^{A(U)}(P_\bullet(U),Q_\bullet(U))$<NL>forment",
    "Display of a formula the print sets inline (as GLOBAL_ISSUES item 21).")
add(150, "Remarques (6.5.7) (ii): 'forment alors un préfaisceau sur X'", "préfaisceau in italics", "no emphasis",
    "italics", None, "high", "un préfaisceau sur", r"un \emph{préfaisceau} sur", "Remark body judged roman.")
heavy(150, "Remarques (6.5.7) (ii): 'l'on désigne par 𝒯or_n^X(𝒫., 𝒬.)'",
      r"$\mathscr{T}\!or_n^X", r"$\boldsymbol{\mathscr{T}\!or}_n^X")
add(150, "Remarques (6.5.7) (ii): 'Lorsque X est un préschéma,'", "préschéma in italics", "no emphasis", "italics",
    None, "high", "est un préschéma,", r"est un \emph{préschéma},", "Remark body judged roman.")
add(150, "Proposition (6.5.8): 'ℱ (resp. 𝒢) un 𝒪_X-Module'", "'(resp.' and ')' upright in the italic statement",
    r"(resp. $\mathscr G$) italic", "convention", 6, "high",
    r"$\mathscr F$ (resp. $\mathscr G$) un", r"$\mathscr F$ \textup{(resp.} $\mathscr G$\textup{)} un", C6R)
add(150, "Proposition (6.5.8): '(resp. un 𝒪_Y-Module) quasi-cohérent'",
    "'(resp.' and ')' upright; 'un 𝒪_Y-Module' italic", r"(resp. un $\mathscr O_Y$-Module) italic", "convention",
    6, "high", r"(resp. un $\mathscr O_Y$-Module) quasi-cohérent",
    r"\textup{(resp.} un $\mathscr O_Y$-Module\textup{)} quasi-cohérent", C6R)
add(150, "Proof of (6.5.8): 'M_s est un A_s-module plat (0_I, 6.7.1)'", "(𝟎_I, 6.7.1): bold 0",
    r"($0_{\mathrm I}$, 6.7.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.7.1)", r"($\mathbf{0}_{\mathrm I}$, 6.7.1)", C2)
add(150, "Proof of (6.5.8): 'M est un A-module plat (0_I, 6.3.3)'", "(𝟎_I, 6.3.3): bold 0",
    r"($0_{\mathrm I}$, 6.3.3)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.3.3)", r"($\mathbf{0}_{\mathrm I}$, 6.3.3)", C2)
add(150, "Proof of (6.5.8): 'pour tout C-module N (0_I, 6.1.1)'", "(𝟎_I, 6.1.1): bold 0",
    r"($0_{\mathrm I}$, 6.1.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.1.1)", r"($\mathbf{0}_{\mathrm I}$, 6.1.1)", C2)
add(150, "Corollaire (6.5.9): '𝒫. (resp. 𝒬.) un complexe de'", "'(resp.' and ')' upright in the italic statement",
    r"(resp. $\mathscr Q_\bullet$) italic", "convention", 6, "high",
    r"(resp.<NL>$\mathscr Q_\bullet$) un", r"\textup{(resp.}<NL>$\mathscr Q_\bullet$\textup{)} un", C6R)
add(150, "End of the page: 'un complexe de' before \\oldpage[III]{151}",
    "the statement runs on to p. 151 ('un complexe de 𝒪_X-Modules ...'), no paragraph break",
    "blank line before the page marker: new paragraph", "other", None, "high",
    "complexe de<NL><NL>", "complexe de<NL>", PAR)

# ---------------------------------------------------------------- page 151
add(151, "Corollaire (6.5.9): '(resp. de 𝒪_Y-Modules) quasi-cohérents limité'",
    "'(resp.' and ')' upright; 'de 𝒪_Y-Modules' italic", r"(resp. de $\mathscr O_Y$-Modules) italic",
    "convention", 6, "high", r"(resp. de $\mathscr O_Y$-Modules) quasi-cohérents limité",
    r"\textup{(resp.} de $\mathscr O_Y$-Modules\textup{)} quasi-cohérents limité", C6R)
heavy(151, "(6.5.9.1), left side: '𝒯or_•^S(𝒫., 𝒬.)'",
      r"  \mathscr{T}\!or_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)<NL>  \xrightarrow",
      r"  \boldsymbol{\mathscr{T}\!or}_\bullet^S(\mathscr P_\bullet,\mathscr Q_\bullet)<NL>  \xrightarrow")
add(151, "Corollaire (6.5.10): 'X soit plat sur S (0_I, 6.7.1), que'", "(𝟎_I, 6.7.1): bold 0",
    r"($0_{\mathrm I}$, 6.7.1)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.7.1), que", r"\textup{($\mathbf{0}_{\mathrm I}$, 6.7.1)}, que",
    "One edit for this finding and the next (convention 6): bold 0 and the upright reference together.")
add(151, "Corollaire (6.5.10): same reference '(0_I, 6.7.1)'", "the reference is upright inside the italic statement",
    r"($0_{\mathrm I}$, 6.7.1) inside the italic namedtheorem: italic", "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(151, "Corollaire (6.5.10): 'Alors l'homomorphisme (6.5.9.1) est bijectif'", "(6.5.9.1) upright in the italic statement",
    "(6.5.9.1) italic", "convention", 6, "high",
    "l'homomorphisme (6.5.9.1) est", r"l'homomorphisme \textup{(6.5.9.1)} est", C6)
add(151, "Proof of (6.5.10): 'étant un module plat (0_I, 6.1.2)'", "(𝟎_I, 6.1.2): bold 0",
    r"($0_{\mathrm I}$, 6.1.2)", "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.1.2)", r"($\mathbf{0}_{\mathrm I}$, 6.1.2)", C2)
add(151, "Proposition (6.5.11): 'Soit 𝒫. (resp. 𝒬.) un complexe'", "'(resp.' and ')' upright in the italic statement",
    r"(resp. $\mathscr Q_\bullet$) italic", "convention", 6, "high",
    r"Soit $\mathscr P_\bullet$ (resp.<NL>$\mathscr Q_\bullet$) un complexe",
    r"Soit $\mathscr P_\bullet$ \textup{(resp.}<NL>$\mathscr Q_\bullet$\textup{)} un complexe", C6R)
add(151, "Proposition (6.5.11): '(resp. de 𝒪_Y-Modules) quasi-cohérents ;'",
    "'(resp.' and ')' upright; 'de 𝒪_Y-Modules' italic", r"(resp. de $\mathscr O_Y$-Modules) italic",
    "convention", 6, "high", r"-Modules (resp. de<NL>$\mathscr O_Y$-Modules) quasi-cohérents; on a",
    r"-Modules \textup{(resp.} de<NL>$\mathscr O_Y$-Modules\textup{)} quasi-cohérents; on a", C6R)
heavy(151, "(6.5.11.1), left side: '(f ×_S g)_*(𝒯or_•^S(𝒫., 𝒬.))'",
      r"(f\times_S g)_*<NL>  \bigl(\mathscr{T}\!or", r"(f\times_S g)_*<NL>  \bigl(\boldsymbol{\mathscr{T}\!or}")
heavy(151, "(6.5.11.1), right side: '𝒯or_•^S(f_*(𝒫.), g_*(𝒬.))'",
      r"\mathscr{T}\!or_\bullet^S<NL>  (f_*", r"\boldsymbol{\mathscr{T}\!or}_\bullet^S<NL>  (f_*")
add(151, "Proof of (6.5.11): 'complexes de Modules quasi-cohérents (II, 1.2.6)'", "(𝐈𝐈, 1.2.6): bold II",
    "(II, 1.2.6)", "convention", 2, "high", "(II, 1.2.6)", r"(\textbf{II}, 1.2.6)", C2)
add(151, "Proof of (6.5.11): 'de (6.4.1.1) et (I, 1.6.3)'", "(𝐈, 1.6.3): bold I", "(I, 1.6.3)", "convention", 2,
    "high", "(I, 1.6.3)", r"(\textbf{I}, 1.6.3)", C2)
add(151, "Remarque (6.5.12): 'supposons que X' soit S-plat;'", "plat in italics (remark body roman)",
    "no emphasis", "italics", None, "high", r"soit $S$-plat;", r"soit $S$-\emph{plat};",
    "Judged with the remark body roman, as instructed (the TeX sets this remark with namedtheorem, italic).")
heavy(151, "(6.5.12.1), left side: '(i ×_S 1)_*(𝒯or_•^S(𝒫., 𝒬.))'",
      r"(i\times_S 1)_*<NL>  \bigl(\mathscr{T}\!or_\bullet^S",
      r"(i\times_S 1)_*<NL>  \bigl(\boldsymbol{\mathscr{T}\!or}_\bullet^{\mathbf S}")
F[-1]["note"] = ("One edit for this finding and the next (the bold superscript S, a misprint). " + HEAVY)
add(151, "(6.5.12.1), left side: the superscript S of 𝒯or_•^S",
    "the S is bold (side-by-side crop with the S of (6.5.9.1) and (6.5.11.1))", "^S (normal weight)",
    "misprint_in_print", None, "high", None, None,
    "Wrong-font letter (GLOBAL_ISSUES item 29); the TeX silently corrects. " + COV,
    corrected=r"\boldsymbol{\mathscr{T}\!or}_\bullet^S")
add(151, "Remarque (6.5.12), 3rd paragraph: 'isomorphisme de suites spectrales (0, 11.6.5 et 11.5.3)'",
    "(𝟎, 11.6.5 et 11.5.3): bold 0", "(0, 11.6.5 et", "convention", 2, "high",
    "(0, 11.6.5 et", r"(\textbf{0}, 11.6.5 et", C2)
add(151, "End of the page: 'complexes de A-modules limités' before \\oldpage[III]{152}",
    "the sentence runs on to p. 152 ('limités inférieurement (cf. ...)'), no paragraph break",
    "blank line before the page marker: new paragraph", "other", None, "high", "limités<NL><NL>", "limités<NL>", PAR)

# ---------------------------------------------------------------- checks
def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


rel = REL.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in re.finditer(r"\\oldpage\[III\]\{(\d+)\}", rel)]


def segment(n):
    for i, (p, s) in enumerate(cuts):
        if p == n:
            return rel[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(rel)]
    return None


bad = 0
seq = {}
for x in F:
    if not x["fix"]:
        continue
    o = x["fix"]["old"]
    t = page_text(x["page"])
    seg = segment(x["page"])
    c1, c2 = t.count(o), seg.count(o)
    if c1 != 1 or c2 != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], c1, c2, repr(o)[:90])
    # apply in sequence to the release segment, to see that every edit still applies after the earlier ones
    s = seq.setdefault(x["page"], seg)
    if s.count(o) != 1:
        bad += 1
        print("SEQUENCE FAIL", x["page"], repr(o)[:90])
    else:
        seq[x["page"]] = s.replace(o, x["fix"]["new"])
print("findings", len(F), "problems", bad)
for p in range(147, 152):
    s = seq.get(p, segment(p))
    print("page", p, "plain Tor left:", s.count(r"\mathscr{T}\!or") - s.count(r"\boldsymbol{\mathscr{T}\!or}"),
          "heavy:", s.count(r"\boldsymbol{\mathscr{T}\!or}"))
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(147, 152):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT)
