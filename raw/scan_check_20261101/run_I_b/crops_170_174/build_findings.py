# Builds findings_170_174.json and checks every "old" against its page_NNN.tex (exactly one occurrence,
# after CRLF -> LF normalisation, as apply_fixes.py does). Reads the page files only; writes only OUTFILE.
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_170_174.json"
N = "\n"

RESP = "'resp.' roman in the print inside the italic statement; italic in the TeX environment."
REF6 = "Reference printed upright inside the italic statement; italic in the TeX environment."
LAB6 = ("The print sets the item labels of italic statements upright (checked on a crop for (9.2.2)); "
        "\\item[...] takes the \\itshape of the statement environment.")
LABREF = ("Labels are italic in the roman proof text of the print (checked on a crop: italic letter and slanted "
          "parenthesis); the TeX sets them roman.")
EMPH6 = ("Emphasis printed roman inside the italic statement. The TeX marks such emphasis with \\emph (e.g. "
         "\\emph{tout} in (9.4.2)), which comes out upright in the italic environment.")
BOLD0_UP = ("Bold 0 in the print; the reference is also upright inside the italic statement (convention 6), "
            "so the fix sets both.")


def f(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


F = []

# ---------------- page 170 ----------------
F += [
    f(170, "Proposition (9.1.4): 'F (resp. G) un O_X-Module'", "'(resp. 𝒢)' roman inside the italic statement",
      r"(resp. $\mathscr{G}$)", "convention", 6, "high",
      r"(resp." + N + r"$\mathscr{G}$)", r"\textup{(resp." + N + r"$\mathscr{G}$)}", RESP),
    f(170, "Proposition (9.1.4): 'un O_X-Module (resp. O_Y-Module) quasi-cohérent'",
      "'(resp.' roman inside the italic statement; 'Module' italic",
      r"(resp. $\mathscr{O}_Y$-Module)", "convention", 6, "high",
      r"(resp. $\mathscr{O}_Y$-Module)", r"\textup{(resp.} $\mathscr{O}_Y$-Module)", RESP),
    f(170, "proof of (9.1.4): '(f, g)*_S∘q*=g* (0, 3.5.5)'", "(0, 3.5.5) with the chapter number 0 in bold",
      r"{0, 3.5.5}", "convention", 2, "high", r"{0, 3.5.5}", r"{\textbf{0}, 3.5.5}"),
    f(170, "proof of (9.1.4): 'le produit tensoriel de leurs images réciproques (0, 4.3.3)'",
      "(0, 4.3.3) with the chapter number 0 in bold",
      r"{0, 4.3.3}", "convention", 2, "high", r"{0, 4.3.3}", r"{\textbf{0}, 4.3.3}"),
    f(170, "Corollaire (9.1.5): 'F' (resp. G') un O_X'-Module'", "'(resp. 𝒢′)' roman inside the italic statement",
      r"(resp. $\mathscr{G}'$)", "convention", 6, "high",
      r"(resp." + N + r"$\mathscr{G}'$)", r"\textup{(resp." + N + r"$\mathscr{G}'$)}", RESP),
    f(170, "Corollaire (9.1.5): '(resp. O_Y'-Module) quasi-cohérent'",
      "'(resp.' roman inside the italic statement; 'Module' italic",
      r"(resp. $\mathscr{O}_{Y'}$-Module)", "convention", 6, "high",
      r"(resp." + N + r"$\mathscr{O}_{Y'}$-Module)", r"\textup{(resp.}" + N + r"$\mathscr{O}_{Y'}$-Module)", RESP),
    f(170, "Corollaire (9.1.6): 'F (resp. G, H) un O_X-Module'", "'(resp. 𝒢, ℋ)' roman inside the italic statement",
      r"(resp. $\mathscr{G}$, $\mathscr{H}$)", "convention", 6, "high",
      r"(resp." + N + r"$\mathscr{G}$, $\mathscr{H}$)", r"\textup{(resp." + N + r"$\mathscr{G}$, $\mathscr{H}$)}",
      RESP),
    f(170, "Corollaire (9.1.6): '(resp. O_Y-Module, O_Z-Module) quasi-cohérent'",
      "'(resp.' roman inside the italic statement; the two 'Module' italic",
      r"(resp. $\mathscr{O}_Y$-Module, $\mathscr{O}_Z$-Module)", "convention", 6, "high",
      r"(resp." + N + r"$\mathscr{O}_Y$-Module, $\mathscr{O}_Z$-Module)",
      r"\textup{(resp.}" + N + r"$\mathscr{O}_Y$-Module, $\mathscr{O}_Z$-Module)", RESP),
    f(170, "Corollaire (9.1.7): 'par l'isomorphisme canonique de X sur X×_S S (3.3.3)'",
      "(3.3.3) upright inside the italic statement",
      r"(\hyperref[I.3.3.3-fr]{3.3.3})", "convention", 6, "high",
      r"(\hyperref[I.3.3.3-fr]{3.3.3})", r"\textup{(\hyperref[I.3.3.3-fr]{3.3.3})}", REF6),
    f(170, "Proposition (9.1.9): 'l'isomorphisme canonique (X_(φ))_(φ') ⥲ X_(φ∘φ') (3.3.9)'",
      "(3.3.9) upright inside the italic statement",
      r"(\hyperref[I.3.3.9-fr]{3.3.9})", "convention", 6, "high",
      r"X_{(\varphi\circ\varphi')}$ (\hyperref[I.3.3.9-fr]{3.3.9})",
      r"X_{(\varphi\circ\varphi')}$ \textup{(\hyperref[I.3.3.9-fr]{3.3.9})}",
      REF6 + " The proof's (3.3.9) on the same page is roman text and needs no change."),
]

# ---------------- page 171 ----------------
F += [
    f(171, "Corollaire (9.1.11): 'F (resp. G) un O_X-Module'", "'(resp. 𝒢)' roman inside the italic statement",
      r"(resp. $\mathscr{G}$)", "convention", 6, "high",
      r"(resp. $\mathscr{G}$)", r"\textup{(resp. $\mathscr{G}$)}", RESP),
    f(171, "Corollaire (9.1.11): '(resp. O_Y-Module) quasi-cohérent'",
      "'(resp.' roman inside the italic statement; 'Module' italic",
      r"(resp. $\mathscr{O}_Y$-Module)", "convention", 6, "high",
      r"(resp. $\mathscr{O}_Y$-Module)", r"\textup{(resp.} $\mathscr{O}_Y$-Module)", RESP),
    f(171, "Corollaire (9.1.11): 'L'image réciproque du faisceau (F_(S'))⊗_S'(G_(S')) par l'isomorphisme'",
      "(𝓕_(S'))⊗_{S'}(𝒢_(S')): each factor in its own parentheses",
      r"$(\mathscr{F}_{(S')}\otimes_{S'}\mathscr{G}_{(S')})$", "formula", None, "high",
      r"$(\mathscr{F}_{(S')}\otimes_{S'}\mathscr{G}_{(S')})$",
      r"$(\mathscr{F}_{(S')})\otimes_{S'}(\mathscr{G}_{(S')})$",
      "Checked on a crop at 2.2x: the print brackets each factor, like (X_(S'))×_{S'}(Y_(S')) in the same "
      "statement; the TeX brackets the whole product. The corrected edition (r20 current) has the TeX's "
      "bracketing too. A small speck after 'est égale à' on the next line is not a printed period (much smaller "
      "and thinner than the italic periods of the statement)."),
    f(171, "Corollaire (9.1.11): '(X_(S'))×_S'(Y_(S')) (3.3.10) est égale à'",
      "(3.3.10) upright inside the italic statement",
      r"(\hyperref[I.3.3.10-fr]{3.3.10})", "convention", 6, "high",
      r"(\hyperref[I.3.3.10-fr]{3.3.10})", r"\textup{(\hyperref[I.3.3.10-fr]{3.3.10})}", REF6),
    f(171, "Proposition (9.1.12): 'Avec les notations de (9.1.2) soient z un point'",
      "(9.1.2) upright inside the italic statement",
      r"(\hyperref[I.9.1.2-fr]{9.1.2})", "convention", 6, "high",
      r"(\hyperref[I.9.1.2-fr]{9.1.2})", r"\textup{(\hyperref[I.9.1.2-fr]{9.1.2})}", REF6),
    f(171, "Proposition (9.1.12), end of the statement: '= F_x⊗_{O_x}O_z⊗_{O_y}⊗G_y.'",
      "𝓕_x⊗_{𝒪_x}𝒪_z⊗_{𝒪_y}⊗𝒢_y: a second ⊗ (without subscript) stands before 𝒢_y",
      r"\mathscr{F}_x\otimes_{\mathscr{O}_x}\mathscr{O}_z \otimes_{\mathscr{O}_y}\mathscr{G}_y",
      "misprint_in_print", None, "high",
      r"\otimes_{\mathscr{O}_y}\mathscr{G}_y", r"\otimes_{\mathscr{O}_y}\otimes\mathscr{G}_y",
      "The TeX silently corrects the print. Checked on a crop at 2x: after ⊗ with subscript 𝒪_y the print "
      "repeats a ⊗ before 𝒢_y. Not in the authors' errata; the corrected edition (r20 current) has the single ⊗.",
      r"\mathscr{F}_x\otimes_{\mathscr{O}_x}\mathscr{O}_z\otimes_{\mathscr{O}_y}\mathscr{G}_y"),
    f(171, "proof of (9.1.13): 'on est ramené, par (9.1.12) et (0, 1.7.5), au cas particulier'",
      "(0, 1.7.5) with the chapter number 0 in bold",
      r"{0, 1.7.5}", "convention", 2, "high", r"{0, 1.7.5}), au cas", r"{\textbf{0}, 1.7.5}), au cas"),
    f(171, "(9.1.13.1), left side: 'Supp(p^{-1}(F))=p^{-1}(Supp(F))'",
      "Supp(p^{-1}(𝓕)) on the left side",
      r"\operatorname{Supp}(p^{-1}(\mathscr{F}))", "misprint_in_print", None, "high", None, None,
      "The TeX keeps the printed reading. The case 𝒢=𝒪_Y of (9.1.13) is Supp(𝓕⊗_S𝒪_Y)=Supp(p^*(𝓕)), and the "
      "next paragraph's check 𝒪_z/𝔪_x𝒪_z≠0 is about p^*(𝓕)_z=𝓕_x⊗_{𝒪_x}𝒪_z; for the topological inverse image "
      "the formula would be trivial. The authors' errata make this correction: '(I, 9.1.13) Ligne 15 de la "
      "p. 171, remplacer p^{-1}(𝓕) par p^*(𝓕)' (EGA III, Errata et Addenda; ega-fr source/ega3/ega3-7-fr.tex). "
      "The corrected edition (r20 current) still has p^{-1}(𝓕).",
      r"\operatorname{Supp}(p^*(\mathscr{F}))=p^{-1}(\operatorname{Supp}(\mathscr{F}))"),
    f(171, "proof of (9.1.13): 'Le même raisonnement que dans (0, 1.7.5) ramène à vérifier'",
      "(0, 1.7.5) with the chapter number 0 in bold",
      r"{0, 1.7.5}", "convention", 2, "high", r"{0, 1.7.5}) ramène", r"{\textbf{0}, 1.7.5}) ramène"),
    f(171, "Proposition (9.2.1): 'f^{-1}(Y_α) admet un recouvrement fini (X_αi)'",
      "'fini' roman (emphasis) inside the italic statement",
      "admet un recouvrement fini", "convention", 6, "high",
      "admet un recouvrement fini", r"admet un recouvrement \emph{fini}",
      EMPH6 + " Checked on a crop at 1.4x."),
    f(171, "Proposition (9.2.1): 'soit elle-même réunion finie d'ouverts affines'",
      "'finie' roman (emphasis) inside the italic statement",
      "elle-même réunion finie", "convention", 6, "high",
      "elle-même réunion finie", r"elle-même réunion \emph{finie}",
      EMPH6 + " Checked on a crop at 1.4x."),
    f(171, "proof of (9.2.1), label a) ('a) Supposons d'abord que les X_i∩X_j ...')",
      "italic label 'a)' (the proof text is roman)",
      r"\item[a)] Supposons", "italics", None, "high",
      r"\item[a)] Supposons", r"\item[\emph{a)}] Supposons",
      "\\item[a)] in the roman proof environment prints a roman label; the print's label is italic, like the "
      "label b) on p. 172 and the case labels in the proof of (9.2.2)."),
]

# ---------------- page 172 ----------------
F += [
    f(172, "proof of (9.2.1), label b) ('b) Dans le cas général, ...')",
      "italic label 'b)' (the proof text is roman)",
      r"\item[b)] Dans le cas général", "italics", None, "high",
      r"\item[b)] Dans le cas général", r"\item[\emph{b)}] Dans le cas général",
      "\\item[b)] in the roman proof environment prints a roman label; the print's label is italic."),
    f(172, "Corollaire (9.2.2): 'La conclusion de (9.2.1) est valable dans chacun des cas suivants'",
      "(9.2.1) upright inside the italic statement",
      "La conclusion de (9.2.1)", "convention", 6, "high",
      "La conclusion de (9.2.1)", r"La conclusion de \textup{(9.2.1)}", REF6),
    f(172, "Corollaire (9.2.2), label a)", "label a) upright",
      r"\item[a)] $f$ est séparé et quasi-compact.", "convention", 6, "high",
      r"\item[a)] $f$ est séparé et quasi-compact.", r"\item[\textup{a)}] $f$ est séparé et quasi-compact.",
      LAB6),
    f(172, "Corollaire (9.2.2), label b)", "label b) upright",
      r"\item[b)] $f$ est séparé et de type fini.", "convention", 6, "high",
      r"\item[b)] $f$ est séparé et de type fini.", r"\item[\textup{b)}] $f$ est séparé et de type fini.",
      LAB6),
    f(172, "Corollaire (9.2.2), label c)", "label c) upright",
      r"\item[c)] $f$ est quasi-compact", "convention", 6, "high",
      r"\item[c)] $f$ est quasi-compact", r"\item[\textup{c)}] $f$ est quasi-compact", LAB6),
    f(172, "proof of (9.2.2): 'Dans le cas a), les X_αi∩X_αj sont affines'", "a) in italics",
      "Dans le cas a), les", "italics", None, "high",
      "Dans le cas a), les", r"Dans le cas \emph{a)}, les", LABREF),
    f(172, "proof of (9.2.2): 'Le cas b) est un cas particulier de a) (6.6.3)'", "b) and a) in italics",
      "Le cas b) est un cas particulier de a)", "italics", None, "high",
      "Le cas b) est un cas particulier de a)", r"Le cas \emph{b)} est un cas particulier de \emph{a)}", LABREF),
    f(172, "proof of (9.2.2): 'Enfin, dans le cas c), on peut se ramener'", "c) in italics",
      "dans le cas c), on peut", "italics", None, "high",
      "dans le cas c), on peut", r"dans le cas \emph{c)}, on peut", LABREF),
    f(172, "Théorème (9.3.1): 'Soient L un O_X-Module inversible (0, 5.4.1)'",
      "(0, 5.4.1) with bold 0, upright inside the italic statement",
      r"(\hyperref[0.5.4.1-fr]{0, 5.4.1})", "convention", 2, "high",
      r"(\hyperref[0.5.4.1-fr]{0, 5.4.1})", r"\textup{(\hyperref[0.5.4.1-fr]{\textbf{0}, 5.4.1})}", BOLD0_UP),
    f(172, "Théorème (9.3.1): 'où f(x)≠0 (0, 5.5.1)'",
      "(0, 5.5.1) with bold 0, upright inside the italic statement",
      r"(\hyperref[0.5.5.1-fr]{0, 5.5.1})", "convention", 2, "high",
      r"(\hyperref[0.5.5.1-fr]{0, 5.5.1})", r"\textup{(\hyperref[0.5.5.1-fr]{\textbf{0}, 5.5.1})}", BOLD0_UP),
    f(172, "Théorème (9.3.1), label (i)", "label (i) upright",
      r"\item[(i)] Si $s\in", "convention", 6, "high",
      r"\item[(i)] Si $s\in", r"\item[\textup{(i)}] Si $s\in", LAB6),
    f(172, "Théorème (9.3.1), label (ii)", "label (ii) upright",
      r"\item[(ii)] Pour toute section", "convention", 6, "high",
      r"\item[(ii)] Pour toute section", r"\item[\textup{(ii)}] Pour toute section", LAB6),
]

# ---------------- page 173 ----------------
F += [
    f(173, "proof of (9.3.1) (ii), first line: 'tels que L|U_i ≅ O_X|U_i'",
      "≅ (tilde above two bars)",
      r"\mathscr{L}|U_i\simeq\mathscr{O}_X|U_i", "symbol", None, "high",
      r"\mathscr{L}|U_i\simeq\mathscr{O}_X|U_i", r"\mathscr{L}|U_i\cong\mathscr{O}_X|U_i",
      "Checked on a crop at 3x: a tilde above two parallel bars (≅), not ≃. Not an isomorphism arrow, so not "
      "convention 4; same case as the finding for p. 130."),
    f(173, "Corollaire (9.3.2): 'Les hypothèses étant celles de (9.3.1), considérons'",
      "(9.3.1) upright inside the italic statement",
      "celles de (9.3.1)", "convention", 6, "high",
      "celles de (9.3.1)", r"celles de \textup{(9.3.1)}", REF6),
    f(173, "Corollaire (9.3.2): 'M_*=Γ_*(L, F) (0, 5.4.6)'",
      "(0, 5.4.6) with bold 0, upright inside the italic statement",
      r"(\hyperref[0.5.4.6-fr]{0, 5.4.6})", "convention", 2, "high",
      r"(\hyperref[0.5.4.6-fr]{0, 5.4.6})", r"\textup{(\hyperref[0.5.4.6-fr]{\textbf{0}, 5.4.6})}", BOLD0_UP),
    f(173, "Corollaire (9.3.2): '(sous-groupe du module de fractions (M_*)_f formé des éléments de degré 0)'",
      "the whole parenthesis roman inside the italic statement",
      r"(sous-groupe du module de fractions $(M_*)_f$ formé des éléments de degré $0$)",
      "convention", 6, "high",
      r"(sous-groupe du module de fractions $(M_*)_f$ formé des éléments de degré" + N + r"$0$)",
      r"\textup{(sous-groupe du module de fractions $(M_*)_f$ formé des éléments de degré" + N + r"$0$)}",
      "Roman parenthesis in the print; italic in the TeX environment. The 'old' spans the line break before $0$."),
    f(173, "Corollaire (9.3.3): 'On suppose vérifiées les hypothèses de (9.3.1), et on suppose'",
      "(9.3.1) upright inside the italic statement",
      "hypothèses de (9.3.1)", "convention", 6, "high",
      "hypothèses de (9.3.1)", r"hypothèses de \textup{(9.3.1)}", REF6),
    f(173, "Proposition (9.3.4): 'un faisceau cohérent d'idéaux dans O_X, tels que le support'",
      "comma after 𝒪_X",
      r"dans $\mathscr{O}_X$ tels que", "punctuation", None, "high",
      r"dans $\mathscr{O}_X$ tels que", r"dans $\mathscr{O}_X$, tels que",
      "Checked on a crop at 3x."),
    f(173, "proof of (9.3.4): 'le O_X-Module correspondant J^nF=(𝔍^nM)~ (1.3.13) est nul'",
      "(𝔍^nM)~: parentheses with the tilde written after them",
      r"\widetilde{\mathfrak{J}^nM}", "convention", 5, "high",
      r"\widetilde{\mathfrak{J}^nM}", r"(\mathfrak{J}^nM)\supertilde",
      "The TeX has a wide tilde over 𝔍^nM and no parentheses; \\supertilde as in ega1-1-fr.tex "
      "((\\Gamma(v))\\supertilde)."),
    f(173, "Corollaire (9.3.5): 'Sous les hypothèses de (9.3.4), il existe'",
      "(9.3.4) upright inside the italic statement",
      "Sous les hypothèses de (9.3.4)", "convention", 6, "high",
      "Sous les hypothèses de (9.3.4)", r"Sous les hypothèses de \textup{(9.3.4)}", REF6),
]

# ---------------- page 174 ----------------
F += [
    f(174, "(9.4.1): 'l'homomorphisme canonique ρ : F→ψ_*(ψ*(F)) (0, 3.5.3)'",
      "(0, 3.5.3) with the chapter number 0 in bold",
      r"{0, 3.5.3}", "convention", 2, "high", r"{0, 3.5.3}", r"{\textbf{0}, 3.5.3}"),
    f(174, "Proposition (9.4.2), label (i)", "label (i) upright",
      r"\item[(i)] Pour tout $(", "convention", 6, "high",
      r"\item[(i)] Pour tout $(", r"\item[\textup{(i)}] Pour tout $(", LAB6),
    f(174, "Proposition (9.4.2), label (ii)", "label (ii) upright",
      r"\item[(ii)] Pour tout $\mathscr{O}_X$", "convention", 6, "high",
      r"\item[(ii)] Pour tout $\mathscr{O}_X$", r"\item[\textup{(ii)}] Pour tout $\mathscr{O}_X$", LAB6),
    f(174, "Proposition (9.4.2)(ii): 'le prolongement canonique G-bar de G (9.4.1) est un'",
      "(9.4.1) upright inside the italic statement",
      r"$\mathscr{G}$ (9.4.1)", "convention", 6, "high",
      r"$\mathscr{G}$ (9.4.1)", r"$\mathscr{G}$ \textup{(9.4.1)}", REF6),
    f(174, "proof of (9.4.2): '(i) est donc un cas particulier de (9.2.2, a))'",
      "italic a; both closing parentheses upright",
      r"{9.2.2, a)}", "italics", None, "high",
      r"{9.2.2, a)}", r"{9.2.2, \emph{a})}",
      "Checked on a crop at 3x: only the letter a is italic (roman proof text)."),
    f(174, "Corollaire (9.4.3): 'G un sous-(O_X|U)-Module quasi-cohérent de type fini de F|U'",
      "'de type fini' roman (emphasis) inside the italic statement",
      "quasi-cohérent de type fini de", "convention", 6, "high",
      "quasi-cohérent de type fini de", r"quasi-cohérent \emph{de type fini} de", EMPH6),
    f(174, "Corollaire (9.4.3): 'un sous-O_X-Module quasi-cohérent de type fini G' de F tel que'",
      "'de type fini' roman (emphasis) inside the italic statement",
      r"quasi-cohérent de type fini $\mathscr{G}'$", "convention", 6, "high",
      r"quasi-cohérent de type fini $\mathscr{G}'$", r"quasi-cohérent \emph{de type fini} $\mathscr{G}'$",
      EMPH6 + " The earlier 'de ses sous-𝒪_X-Modules quasi-cohérents de type fini' of the statement is italic "
      "in the print and needs no change."),
    f(174, "proof of (9.4.3): 'puisqu'il est de type fini (0, 5.2.3)'",
      "(0, 5.2.3) with the chapter number 0 in bold",
      r"{0, 5.2.3}", "convention", 2, "high", r"{0, 5.2.3}", r"{\textbf{0}, 5.2.3}"),
]

# ---------------- checks ----------------
pages = {n: (RUN / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(170, 175)}  # universal newlines
bad = 0
for x in F:
    fx = x["fix"]
    if fx is None:
        assert x["kind"] == "misprint_in_print", x
        continue
    c = pages[x["page"]].count(fx["old"])
    if c != 1 or fx["old"] == fx["new"]:
        bad += 1
        print("BAD", x["page"], c, repr(fx["old"]))
assert bad == 0
for x in F:
    assert x["kind"] in ("word", "formula", "symbol", "font", "italics", "missing", "extra", "number",
                         "punctuation", "misprint_in_print", "convention", "marker", "other")
    assert (x["kind"] == "convention") == (x["convention"] is not None)
    assert x["confidence"] in ("high", "medium", "low")
# fixes on the same page must not overlap (each old must still occur once after the others are applied)
for n in range(170, 175):
    t = pages[n]
    for x in [y for y in F if y["page"] == n and y["fix"]]:
        assert t.count(x["fix"]["old"]) == 1, (n, x["fix"]["old"])
        t = t.replace(x["fix"]["old"], x["fix"]["new"])
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for n in range(170, 175):
    print(n, "normal", cnt[(n, "normal")], "convention", cnt[(n, "convention")], "misprint", cnt[(n, "misprint")])
print("total", len(F), "written", OUT)
