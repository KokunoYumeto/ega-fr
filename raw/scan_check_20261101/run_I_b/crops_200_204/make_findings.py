import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
OUT = RUN / "findings_200_204.json"
NL = "\u00b6"  # placeholder for a newline inside fix strings


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv,
             confidence=conf,
             fix=None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")})
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n")
    d["note"] = note
    return d


C6 = "Printed upright inside the italic statement; italic in the TeX environment. Checked on a crop."
X = []

# ---------------- page 200 ----------------
X += [
    F(200, "Proposition (10.9.7): 'X' (resp. Y') une partie fermée de X'",
      "'(resp. Y')' roman inside the italic statement", "$X'$ (resp. $Y'$)", "convention", 6, "high",
      r"$S$,¶$X'$ (resp. $Y'$)", r"$S$,¶$X'$ \textup{(resp. $Y'$)}", C6),
    F(200, "Proposition (10.9.7): 'une partie fermée de X (resp. Y) telle que'",
      "'(resp. Y)' roman inside the italic statement", "(resp. $Y$) telle", "convention", 6, "high",
      r"(resp. $Y$) telle", r"\textup{(resp. $Y$)} telle", C6),
    F(200, "Proposition (10.9.7): 'telle que g(X')⊂S' (resp. h(Y')⊂S')'",
      "'(resp.' roman inside the italic statement", r"(resp. $h(Y')\subset S'$)", "convention", 6, "high",
      r"(resp. $h(Y')\subset S'$)", r"\textup{(resp. $h(Y')\subset S'$)}", C6),
    F(200, "Proposition (10.9.7): 'produit des S_{/S'}-préschémas formels (X_{/X'})×_{S_{/S'}}(Y_{/Y'}) les morphismes structuraux'",
      "no comma after (Y_{/Y'}): '(Y_{/Y'})  les morphismes structuraux'",
      r"(Y_{/Y'})$, les morphismes", "misprint_in_print", None, "high",
      r"(Y_{/Y'})$, les morphismes", r"(Y_{/Y'})$ les morphismes",
      "The TeX silently corrects the print by adding the comma. Checked on a crop at 2x: there is no comma between the closing parenthesis and 'les'. The absolute construction 'les morphismes structuraux s'identifiant à ...' needs the comma.",
      corrected=r"(Y_{/Y'})$, les morphismes"),
    F(200, "proof of (10.9.7): 'pour la topologie 𝔐-préadique (0, 7.7.2)'",
      "bold 0", "{0, 7.7.2}", "convention", 2, "high",
      "{0, 7.7.2}", r"{\textbf{0}, 7.7.2}", ""),
    F(200, "Corollaire (10.9.8): 'soient S' une partie fermée de S, X' (resp. Y') une partie fermée'",
      "'(resp. Y')' roman inside the italic statement", "$X'$ (resp. $Y'$)", "convention", 6, "high",
      r"$S$, $X'$ (resp. $Y'$)", r"$S$, $X'$ \textup{(resp. $Y'$)}", C6),
    F(200, "Corollaire (10.9.8): 'de X (resp. Y) dont l'image dans S'",
      "'(resp. Y)' roman inside the italic statement", "(resp. $Y$) dont", "convention", 6, "high",
      r"(resp. $Y$) dont", r"\textup{(resp. $Y$)} dont", C6),
]

# ---------------- page 201 ----------------
X += [
    F(201, "(10.10.1): 'nous poserons (M̃)_{/X}=M^Δ'",
      "(M̃)_{/X}=M^Δ: the subscript is a roman X, not Fraktur 𝔛",
      r"$(\widetilde M)_{/\mathfrak{X}}=M^\Delta$", "misprint_in_print", None, "high",
      r"$(\widetilde M)_{/\mathfrak{X}}=M^\Delta$", r"$(\widetilde M)_{/X}=M^\Delta$",
      "The TeX silently corrects the print. Checked on a crop at 3x against 𝓕_{/𝔛} two lines above, whose Fraktur subscript has a different shape. M^Δ is the completion of M̃ along the closed part 𝔛 of X (completion along X itself would be M̃).",
      corrected=r"$(\widetilde M)_{/\mathfrak{X}}=M^\Delta$"),
    F(201, "(10.10.1): 'un homomorphisme continu ũ_{/X'} : (M̃)_{/X'} → (Ñ)_{/X'}, que nous noterons u^Δ'",
      "ũ_{/X'} : (M̃)_{/X'} → (Ñ)_{/X'}: all three subscripts are a roman X with a prime",
      r"\widetilde u_{/\mathfrak{X}}:(\widetilde M)_{/\mathfrak{X}}\to (\widetilde N)_{/\mathfrak{X}}",
      "misprint_in_print", None, "high",
      r"\widetilde u_{/\mathfrak{X}}:(\widetilde M)_{/\mathfrak{X}}\to¶(\widetilde N)_{/\mathfrak{X}}",
      r"\widetilde u_{/X'}:(\widetilde M)_{/X'}\to¶(\widetilde N)_{/X'}",
      "The TeX silently corrects the print. Checked on a crop at 2.5x: X' (roman, primed) three times. X' is the closed subset of the general notation of 10.8; here the closed part is 𝔛.",
      corrected=r"\widetilde u_{/\mathfrak{X}}:(\widetilde M)_{/\mathfrak{X}}\to¶(\widetilde N)_{/\mathfrak{X}}"),
    F(201, "Proposition (10.10.2), display (10.10.2.3): 'Hom_A(M, N) ⥲ Hom_{𝒪_X}(M^Δ, N^Δ)'",
      "Hom_{𝒪_X}: the subscript of 𝒪 is a roman X",
      r"\operatorname{Hom}_{\mathscr{O}_{\mathfrak{X}}}", "misprint_in_print", None, "high",
      r"\operatorname{Hom}_{\mathscr{O}_{\mathfrak{X}}}", r"\operatorname{Hom}_{\mathscr{O}_X}",
      "The TeX silently corrects the print. Checked on a crop at 2.5x; (10.10.2.1) and (10.10.2.2) just above have the Fraktur 𝒪_𝔛. M^Δ and N^Δ are 𝒪_𝔛-Modules.",
      corrected=r"\operatorname{Hom}_{\mathscr{O}_{\mathfrak{X}}}"),
    F(201, "proof of (10.10.2): 'de l'exactitude des foncteurs M̃ (1.3.5) et 𝓕_{/X'} (10.8.8)'",
      "𝓕_{/X'} (roman X with a prime)", r"$\mathscr{F}_{/\mathfrak{X}}$", "formula", None, "high",
      r"$\mathscr{F}_{/\mathfrak{X}}$ (\hyperref[I.10.8.8-fr]", r"$\mathscr{F}_{/X'}$ (\hyperref[I.10.8.8-fr]",
      "Checked on a crop at 2.5x. Not a misprint: the print names the functor 𝓕_{/X'} in the general notation of (10.8.8)(i) ('Le foncteur 𝓕_{/X'} (en 𝓕) est exact'), as it names the functor M̃ of (1.3.5). The TeX replaced X' by 𝔛."),
    F(201, "proof of (10.10.2): 'Par définition, Γ(X, M^Δ) est le séparé complété du A-module Γ(X, M̃)=M'",
      "Γ(X, M^Δ): roman X", r"$\Gamma(\mathfrak{X},M^\Delta)$ est", "misprint_in_print", None, "high",
      r"$\Gamma(\mathfrak{X},M^\Delta)$ est", r"$\Gamma(X,M^\Delta)$ est",
      "The TeX silently corrects the print. Checked on a crop at 2x. M^Δ is a sheaf on 𝔛 (10.8.4: the completion is the restriction to X' of the projective limit), and (i) states Γ(𝔛, M^Δ) ⥲ M; four lines below the print has Γ(𝔛, (Hom_A(M, N))^Δ).",
      corrected=r"$\Gamma(\mathfrak{X},M^\Delta)$ est"),
    F(201, "proof of (10.10.2): 'on sait (0, 7.3.6) que M est séparé et complet'",
      "bold 0", "{0, 7.3.6}", "convention", 2, "high",
      "{0, 7.3.6}", r"{\textbf{0}, 7.3.6}", ""),
    F(201, "proof of (10.10.2): 'L'isomorphisme (10.10.2.1) (resp. (10.10.2.2)) provient de la composition'",
      "'(resp. (10.10.2.2))': the reference has its own parentheses",
      r"(resp. \hyperref[I.10.10.2.2-fr]{10.10.2.2}) provient", "punctuation", None, "high",
      r"\hyperref[I.10.10.2.2-fr]{10.10.2.2}) provient", r"(\hyperref[I.10.10.2.2-fr]{10.10.2.2})) provient",
      "Checked on a crop at 2x: two closing parentheses after 10.10.2.2. The TeX prints '(resp. 10.10.2.2)'."),
]

# ---------------- page 202 ----------------
X += [
    F(202, "first paragraph: 'la propriété d'exactitude de M^Δ, appliqué à la suite exacte'",
      "appliqué (masculine)", "appliqué", "misprint_in_print", None, "low",
      None, None,
      "The TeX keeps the printed reading. The subject of 'montre' is 'la propriété', so 'appliquée' is expected; 'appliqué' can only be read as agreeing with M^Δ (the functor), which the comma makes unlikely. Possibly not a misprint.",
      corrected="appliquée"),
    F(202, "Proposition (10.10.3): 'Sous les hypothèses de (10.10.1), 𝒪_𝔛 est un faisceau cohérent'",
      "(10.10.1) upright inside the italic statement", r"(\hyperref[I.10.10.1-fr]{10.10.1})", "convention", 6, "high",
      r"(\hyperref[I.10.10.1-fr]{10.10.1}),¶$\mathscr{O}_{\mathfrak{X}}$ est",
      r"\textup{(\hyperref[I.10.10.1-fr]{10.10.1})},¶$\mathscr{O}_{\mathfrak{X}}$ est", C6),
    F(202, "proof of (10.10.3): 'A_{{f}} est un anneau adique noethérien (0, 7.6.11)'",
      "bold 0", "{0, 7.6.11}", "convention", 2, "high",
      "{0, 7.6.11}", r"{\textbf{0}, 7.6.11}", ""),
    F(202, "Proposition (10.10.5): 'Sous les hypothèses de (10.10.1), soit 𝓕 un 𝒪_𝔛-Module'",
      "(10.10.1) upright inside the italic statement", r"(\hyperref[I.10.10.1-fr]{10.10.1}), soit", "convention", 6, "high",
      r"(\hyperref[I.10.10.1-fr]{10.10.1}), soit", r"\textup{(\hyperref[I.10.10.1-fr]{10.10.1})}, soit", C6),
    F(202, "Proposition (10.10.5): label 'a)'",
      "label a) roman inside the italic statement", r"\item[a)]", "convention", 6, "high",
      r"\item[a)]", r"\item[\textup{a)}]", "Labels a), b), c) of (10.10.5) are roman in the print (checked on a crop); \\item[a)] takes the italic of the proposition environment."),
    F(202, "Proposition (10.10.5): label 'b)'",
      "label b) roman inside the italic statement", r"\item[b)]", "convention", 6, "high",
      r"\item[b)]", r"\item[\textup{b)}]", ""),
    F(202, "Proposition (10.10.5) b): 'isomorphe à la limite projective (10.6.6) d'une suite'",
      "(10.6.6) upright inside the italic statement", r"(\hyperref[I.10.6.6-fr]{10.6.6})", "convention", 6, "high",
      r"(\hyperref[I.10.6.6-fr]{10.6.6})", r"\textup{(\hyperref[I.10.6.6-fr]{10.6.6})}", C6),
    F(202, "Proposition (10.10.5) b): 'tels que u*_{nm}(𝓕_n)=𝓕_m'",
      "u*_{nm}: subscript nm", r"$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$", "misprint_in_print", None, "high",
      r"$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$", r"$u_{nm}^*(\mathscr{F}_n)=\mathscr{F}_m$",
      "The TeX silently corrects the print. Checked on a crop at 3x. (10.10.4) defines u_{mn} : X_m→X_n (m≤n), so the inverse image of 𝓕_n under u_{mn} is 𝓕_m; the proof writes u_m=u_n∘u_{mn}. The same slip recurs on p. 204 ('On peut donc dire ...').",
      corrected=r"$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$"),
    F(202, "Proposition (10.10.5): label 'c)'",
      "label c) roman inside the italic statement", r"\item[c)]", "convention", 6, "high",
      r"\item[c)]", r"\item[\textup{c)}]", ""),
    F(202, "Proposition (10.10.5) c): 'déterminé à un isomorphisme canonique près par (10.10.2, (i))'",
      "(10.10.2, (i)) upright inside the italic statement", r"(\hyperref[I.10.10.2-fr]{10.10.2, (i)})", "convention", 6, "high",
      r"(\hyperref[I.10.10.2-fr]{10.10.2, (i)})", r"\textup{(\hyperref[I.10.10.2-fr]{10.10.2, (i)})}",
      "The reference is upright; the enclosing parentheses of '(déterminé ... (i)))' are italic. Checked on a crop."),
    F(202, "proof of (10.10.5): 'Montrons d'abord que b) implique c).'",
      "'b)' in italics", "que b) implique", "italics", None, "high",
      "que b) implique", r"que \emph{b)} implique",
      "The print sets the condition labels in the roman proof text in italics (b), c) here; also on this page and on p. 203). Checked on a crop."),
    F(202, "proof of (10.10.5): 'Montrons d'abord que b) implique c).'",
      "'c)' in italics", "implique c). On a", "italics", None, "high",
      "implique c). On a", r"implique \emph{c)}. On a", "Checked on a crop."),
    F(202, "proof of (10.10.5): 'On a 𝓕_n=M̃_n, où M_n est un A_n-module'",
      "tilde over M only, subscript n outside", r"\widetilde{M_n}", "convention", 8, "high",
      r"\widetilde{M_n}", r"\widetilde{M}_n", "Checked on a crop."),
    F(202, "proof of (10.10.5): 'vérifie les conditions de (0, 7.2.9)'",
      "bold 0", "{0, 7.2.9}", "convention", 2, "high",
      "{0, 7.2.9}", r"{\textbf{0}, 7.2.9}", ""),
    F(202, "proof of (10.10.5): 'Inversement, c) entraîne b) ; en effet'",
      "'c)' in italics", "Inversement, c) entraîne", "italics", None, "high",
      "Inversement, c) entraîne", r"Inversement, \emph{c)} entraîne", "Checked on a crop at 2x."),
    F(202, "proof of (10.10.5): 'Inversement, c) entraîne b) ; en effet'",
      "'b)' in italics", "entraîne b)~;", "italics", None, "high",
      "entraîne b)~;", r"entraîne \emph{b)}~;", "Checked on a crop at 2x."),
    F(202, "proof of (10.10.5): 'vérifient les conditions de b), d'où notre assertion'",
      "'b)' in italics", "conditions de b),", "italics", None, "high",
      "conditions de b),", r"conditions de \emph{b)},", "Checked on a crop."),
    F(202, "proof of (10.10.5): 'Montrons maintenant que c) implique a) :'",
      "'c)' in italics", "que c) implique", "italics", None, "high",
      "que c) implique", r"que \emph{c)} implique", "Checked on a crop."),
    F(202, "proof of (10.10.5): 'Montrons maintenant que c) implique a) :'",
      "'a)' in italics", "implique a)~:", "italics", None, "high",
      "implique a)~:", r"implique \emph{a)}~:", "Checked on a crop."),
    F(202, "proof of (10.10.5): 'M étant conoyau d'un homomorphisme A^m→A^n'",
      "the M at the start of the line is set in bold", r"$M$ étant conoyau", "misprint_in_print", None, "medium",
      r"$M$ étant conoyau", r"$\mathbf{M}$ étant conoyau",
      "The TeX silently corrects the print (wrong font). Checked on crops at 4x: this M has the heavy stems and serifs of the bold face, unlike the M of M^Δ at the end of the same line.",
      corrected=r"$M$ étant conoyau"),
    F(202, "proof of (10.10.5): 'il en est de même de M^Δ (0, 5.3.4)'",
      "bold 0", "{0, 5.3.4}", "convention", 2, "high",
      "{0, 5.3.4}", r"{\textbf{0}, 5.3.4}", ""),
]

# ---------------- page 203 ----------------
X += [
    F(203, "proof of (10.10.5), last part: 'Enfin, a) entraîne b).'",
      "'a)' in italics", "Enfin, a) entraîne", "italics", None, "high",
      "Enfin, a) entraîne", r"Enfin, \emph{a)} entraîne", "Checked on a crop."),
    F(203, "proof of (10.10.5), last part: 'Enfin, a) entraîne b).'",
      "'b)' in italics", "entraîne b). Considéré", "italics", None, "high",
      "entraîne b). Considéré", r"entraîne \emph{b)}. Considéré", "Checked on a crop."),
    F(203, "proof of (10.10.5): 'est un 𝒪_𝔛-Module cohérent (0, 5.3.5)'",
      "bold 0", "{0, 5.3.5}", "convention", 2, "high",
      "{0, 5.3.5}", r"{\textbf{0}, 5.3.5}", ""),
    F(203, "proof of (10.10.5): 'est un 𝒪_{X_n}-Module cohérent (0, 5.3.10)'",
      "bold 0", "{0, 5.3.10}", "convention", 2, "high",
      "{0, 5.3.10}", r"{\textbf{0}, 5.3.10}", ""),
    F(203, "proof of (10.10.5): 'puisqu'on a vu que b) entraîne a).'",
      "'b)' in italics", "vu que b)", "italics", None, "high",
      "vu que b)", r"vu que \emph{b)}", "Checked on a crop."),
    F(203, "proof of (10.10.5): 'puisqu'on a vu que b) entraîne a).'",
      "'a)' in italics", "entraîne a). Les", "italics", None, "high",
      "entraîne a). Les", r"entraîne \emph{a)}. Les", "Checked on a crop."),
    F(203, "proof of (10.10.5): 'La question étant maintenant locale, on peut se borner'",
      "'locale' in italics", "maintenant locale,", "italics", None, "high",
      "maintenant locale,", r"maintenant \emph{locale},", "Checked on a crop."),
    F(203, "proof of (10.10.5): '𝓕 est conoyau d'un homomorphisme 𝒪_𝔛^p→𝒪_𝔛^q ; ... où v est un homomorphisme A^m→A^n (10.10.2)'",
      "A^m→A^n after 𝒪_𝔛^p→𝒪_𝔛^q", r"$A^m\to A^n$", "misprint_in_print", None, "medium",
      None, None,
      "The TeX keeps the printed reading. v^Δ is the homomorphism 𝒪_𝔛^p→𝒪_𝔛^q, so v : A^p→A^q; m and n are the indices of the projective system in the same paragraph (𝓕_n, A_n). Checked on a crop at 2x.",
      corrected=r"$A^p\to A^q$"),
    F(203, "proof of (10.10.5): 'on a (M⊗_A A_n)^Δ=(M⊗_n A_n)~ (en tant que 𝒪_{X_n}-Module)'",
      "second tensor product printed ⊗_n (subscript italic n)", r"=(M\otimes_A A_n)^{\sim}", "misprint_in_print", None, "high",
      r"=(M\otimes_A A_n)^{\sim}", r"=(M\otimes_n A_n)^{\sim}",
      "The TeX silently corrects the print. Checked on a crop at 3x: the first product has the subscript A, the second an italic n.",
      corrected=r"=(M\otimes_A A_n)^{\sim}"),
    F(203, "Corollaire (10.10.6): 'Si 𝓕 vérifie la condition b) de (10.10.5)'",
      "'b)' roman inside the italic statement", "la condition b) de", "convention", 6, "high",
      "la condition b) de", r"la condition \textup{b)} de", C6),
    F(203, "Corollaire (10.10.6): 'la condition b) de (10.10.5), le système projectif'",
      "(10.10.5) upright inside the italic statement", r"(\hyperref[I.10.10.5-fr]{10.10.5})", "convention", 6, "high",
      r"(\hyperref[I.10.10.5-fr]{10.10.5})", r"\textup{(\hyperref[I.10.10.5-fr]{10.10.5})}", C6),
    F(203, "Proposition (10.10.8), display: 'f̂*(N^Δ) ⥲ (N⊗_B A)^Δ'",
      "no full stop after the display", r"(N\otimes_B A)^\Delta.", "punctuation", None, "high",
      r"(N\otimes_B A)^\Delta.", r"(N\otimes_B A)^\Delta",
      "Checked on a crop at 3x: the statement ends with the display and no full stop. The TeX adds one."),
]

# ---------------- page 204 ----------------
X += [
    F(204, "(10.11.2): 'de sorte que 𝔛 est limite inductive de la suite (X_n)'",
      "'limite inductive' in italics", "est limite inductive de", "italics", None, "high",
      "est limite inductive de", r"est \emph{limite inductive} de", "Checked on a crop."),
    F(204, "Théorème (10.11.3): 'tel que u*_{mn}(𝓕_n)=𝓕_n pour m≤n (10.6.6)'",
      "u*_{mn}(𝓕_n)=𝓕_n: the right-hand side has the subscript n", r"$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$",
      "misprint_in_print", None, "high",
      r"tel que¶$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$", r"tel que¶$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_n$",
      "The TeX silently corrects the print. Checked on a crop at 3x: '=𝓕_n pour m≤n'. The inverse image of 𝓕_n under u_{mn} : X_m→X_n is 𝓕_m, as in (10.10.5) b).",
      corrected=r"tel que¶$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$"),
    F(204, "Théorème (10.11.3): 'pour m≤n (10.6.6). Le système projectif'",
      "(10.6.6) upright inside the italic statement", r"(\hyperref[I.10.6.6-fr]{10.6.6})", "convention", 6, "high",
      r"(\hyperref[I.10.6.6-fr]{10.6.6})", r"\textup{(\hyperref[I.10.6.6-fr]{10.6.6})}", C6),
    F(204, "after (10.11.3): 'de 𝒪_{X_n}-Modules cohérents tels que u*_{nm}(𝓕_n)=𝓕_m pour m≤n'",
      "u*_{nm}: subscript nm", r"$u_{mn}^*(\mathscr{F}_n)=\mathscr{F}_m$", "misprint_in_print", None, "high",
      r"tels que¶$u_{mn}^*(\mathscr{F}_n)", r"tels que¶$u_{nm}^*(\mathscr{F}_n)",
      "The TeX silently corrects the print. Checked on a crop at 3x. Same slip as in (10.10.5) b) on p. 202; the theorem just above has u*_{mn}.",
      corrected=r"tels que¶$u_{mn}^*(\mathscr{F}_n)"),
    F(204, "Corollaire (10.11.4): 'on peut (avec les notations de (10.11.3)) définir'",
      "'(avec les notations de (10.11.3))' roman inside the italic statement",
      r"(avec les notations de (\hyperref[I.10.11.3-fr]{10.11.3}))", "convention", 6, "high",
      r"(avec les¶notations de (\hyperref[I.10.11.3-fr]{10.11.3}))",
      r"\textup{(avec les¶notations de (\hyperref[I.10.11.3-fr]{10.11.3}))}", C6),
    F(204, "Corollaire (10.11.4), display (10.11.4.1): 'Hom_{𝒪_𝔛}(𝓕, 𝓖) ⥲ lim←_n Hom_{𝒪_{X_n}}(𝓕_n, 𝓖_n)'",
      "no full stop after the display", r"(\mathscr{F}_n,\mathscr{G}_n).", "punctuation", None, "high",
      r"(\mathscr{F}_n,\mathscr{G}_n).", r"(\mathscr{F}_n,\mathscr{G}_n)",
      "Checked on a crop at 2.5x: no full stop after (𝓕_n, 𝓖_n). The TeX adds one."),
    F(204, "after (10.11.4): 'pour les applications θ_n → u*_{mn}(θ_n) (m≤n)'",
      "plain arrow →", r"\theta_n\mapsto u_{mn}^*(\theta_n)", "convention", 3, "high",
      r"\theta_n\mapsto u_{mn}^*(\theta_n)", r"\theta_n\to u_{mn}^*(\theta_n)", "Checked on a crop at 2.2x: no bar at the tail."),
    F(204, "proof of (10.11.5): 'on a en outre alors θ_0=ũ_0'",
      "tilde over u only, subscript 0 outside", r"\widetilde{u_0}", "convention", 8, "high",
      r"\widetilde{u_0}", r"\widetilde{u}_0", "Checked on a crop at 3x."),
    F(204, "proof of (10.11.5): 'simultanément surjectifs (0, 7.1.14)'",
      "bold 0", "{0, 7.1.14}", "convention", 2, "high",
      "{0, 7.1.14}", r"{\textbf{0}, 7.1.14}", ""),
    F(204, "(10.11.6): 'comme un 𝒪_𝔛-Module topologique'",
      "'Module topologique' in italics (the word Module included)", r"-Module \emph{topologique}", "italics", None, "high",
      r"-Module \emph{topologique}", r"-\emph{Module topologique}", "Checked on a crop at 2.2x."),
    F(204, "(10.11.6): 'faisceaux de groupes pseudo-discrets 𝓕_n (0, 3.8.1)'",
      "bold 0", "{0, 3.8.1}", "convention", 2, "high",
      "{0, 3.8.1}", r"{\textbf{0}, 3.8.1}", ""),
]

# ---- check: every fix applies to its page in sequence, "old" occurring exactly once (as apply_fixes.py requires)
texts = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(200, 205)}
bad = 0
for x in X:
    fx = x["fix"]
    if not fx:
        continue
    t = texts[x["page"]]
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", x["page"], n, repr(fx["old"]))
        continue
    texts[x["page"]] = t.replace(fx["old"], fx["new"])
# the "tex" excerpts and the misprints kept by the TeX must be present in the original page text
orig = {p: (RUN / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(200, 205)}
for x in X:
    if x["fix"] is None and x["tex"] not in orig[x["page"]]:
        bad += 1
        print("KEPT READING NOT FOUND", x["page"], repr(x["tex"]))
print("problems:", bad)

json.dump(X, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
for p in range(200, 205):
    c = Counter("misprint" if x["kind"] == "misprint_in_print" else "convention" if x["kind"] == "convention" else "normal"
                for x in X if x["page"] == p)
    print(p, dict(c))
print("total", len(X))
