"""Build findings_260_264.json and check every fix's "old" string.

Each "old" must occur exactly once in its page_NNN.tex (CRLF normalised to LF)
and exactly once in the current source file ega4-21a-fr.tex.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SRC = (RUN.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-21a-fr.tex")
OUT = RUN / "findings_260_264.json"

I_NOTE = ("The print has the script I here (the letter sits on the baseline, no descender; crops "
          "p260s1_left.png, p260s1_right.png, p260s2_midright.png, p260s3_ital.png, p262s3_2112.png): it is "
          "the letter of the map I_X and of the sheaf Id.inv_X. The print keeps the script J (descender below "
          "the baseline) for a general invertible fractional Ideal (e.g. 'inversible J sur X', J_1, J_2 on "
          "p. 260, all of p. 261), where the TeX's \\sh{J} is right. ega4-21a writes both letters as \\sh{J}.")


def f(page, where, scan, tex, kind, fix, note="", convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": convention, "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


def fx(old, new):
    return {"old": old, "new": new}


F = []

# ---------------------------------------------------------------- p. 260
F.append(f(260, "(21.2.5), first sentence: 'On en conclut que I_X(D), pour tout diviseur'",
           "script I: I_X(D)", "\\sh{J}_X(D) (script J)", "symbol",
           fx("On en conclut que $\\sh{J}_X(D)$", "On en conclut que $\\sh{I}_X(D)$"),
           I_NOTE + " Not a boundary fix: the marker and its blank lines at the top of p. 260 are right "
           "(the page begins a new indented paragraph)."))
F.append(f(260, "(21.2.5), first sentence: 'est l'idéal fractionnaire inversible défini'",
           "lowercase 'l'idéal fractionnaire inversible défini' (crop p260_idéal.png)",
           "l'Idéal fractionnaire inversible défini", "misprint_in_print",
           fx("l'Idéal fractionnaire inversible défini", "l'idéal fractionnaire inversible défini"),
           "The print has a lowercase i here and 'l'Idéal fractionnaire inversible' two lines later; EGA "
           "capitalises Idéal for sheaves of ideals. The TeX silently corrects; the diplomatic text takes the "
           "printed lowercase back.",
           confidence="medium", corrected="l'Idéal fractionnaire inversible défini"))
F.append(f(260, "(21.2.5): 'I_X(D)|U est l'Idéal fractionnaire inversible O_U.f'",
           "script I", "\\sh{J}_X(D)|U", "symbol",
           fx("$\\sh{J}_X(D)|U$ est l'Idéal", "$\\sh{I}_X(D)|U$ est l'Idéal"), I_NOTE))
F.append(f(260, "display (21.2.5.4): 'f∈Γ(X, I_X(D))'",
           "script I", "\\sh{J}_X(D)", "symbol",
           fx("f\\in\\Gamma(X,\\sh{J}_X(D))", "f\\in\\Gamma(X,\\sh{I}_X(D))"), I_NOTE))
F.append(f(260, "Proposition (21.2.6): 'I : Div_X → Id.inv_X'",
           "script I in Id.inv_X", "\\sh{J}d.inv_X", "symbol",
           fx("$I:\\sh{D}iv_X\\to\\sh{J}d.inv_X$", "$I:\\sh{D}iv_X\\to\\sh{I}d.inv_X$"), I_NOTE))
F.append(f(260, "proof of (21.2.6): 'que les homomorphismes I_X et I'_X sont réciproques'",
           "script I", "\\sh{J}_X", "symbol",
           fx("les homomorphismes $\\sh{J}_X$", "les homomorphismes $\\sh{I}_X$"), I_NOTE))
F.append(f(260, "proof of (21.2.6): 'l'isomorphisme I' : Id.inv_X → Div_X'",
           "script I in Id.inv_X", "\\sh{J}d.inv_X", "symbol",
           fx("$I':\\sh{J}d.inv_X", "$I':\\sh{I}d.inv_X"), I_NOTE + " Independent of the next entry."))
F.append(f(260, "proof of (21.2.6): 'I' : Id.inv_X → Div_X, réciproque de I'",
           "comma after Div_X: '→ Div_X,  réciproque de I' (crop p260s2_iso.png)",
           "no comma: '\\sh{D}iv_X$ réciproque'", "punctuation",
           fx("\\sh{D}iv_X$ réciproque de $I$", "\\sh{D}iv_X$, réciproque de $I$")))
F.append(f(260, "(21.2.7): 'les faisceaux Div_X et Id.inv_X'",
           "script I in Id.inv_X", "\\sh{J}d.inv_X", "symbol",
           fx("et $\\sh{J}d.inv_X$ (resp. les groupes", "et $\\sh{I}d.inv_X$ (resp. les groupes"), I_NOTE))
F.append(f(260, "(21.2.7): '(resp. I_X et I'_X) précédents'",
           "script I", "\\sh{J}_X", "symbol",
           fx("(resp. $\\sh{J}_X$ et $I_X'$)", "(resp. $\\sh{I}_X$ et $I_X'$)"), I_NOTE))
F.append(f(260, "display (21.2.7.1): 'D ≥ 0 ⇔ I_X(D) ⊂ O_X'",
           "script I", "\\sh{J}_X(D)", "symbol",
           fx("\\iff \\sh{J}_X(D)\\subset\\sh{O}_X", "\\iff \\sh{I}_X(D)\\subset\\sh{O}_X"), I_NOTE))
F.append(f(260, "after (21.2.7.1): 'l'image I_X(Div^+(X))'",
           "script I", "\\sh{J}_X", "symbol",
           fx("l'image $\\sh{J}_X(\\operatorname{Div}^+(X))$", "l'image $\\sh{I}_X(\\operatorname{Div}^+(X))$"),
           I_NOTE))
F.append(f(260, "after (21.2.7.1): 'l'ensemble des Idéaux de O_X'",
           "'Idéaux de O_X' italic, 'de' included (crop p260s3_ital.png)",
           "\\emph{Idéaux} de: 'de' roman", "italics",
           fx("\\emph{Idéaux} de $\\sh{O}_X$", "\\emph{Idéaux de} $\\sh{O}_X$")))
F.append(f(260, "after (21.2.7.1): '(dits aussi parfois Idéaux entiers)'",
           "'Idéaux' roman, only 'entiers' italic", "\\emph{Idéaux entiers}", "italics",
           fx("parfois \\emph{Idéaux entiers})", "parfois Idéaux \\emph{entiers})")))
F.append(f(260, "after (21.2.7.1): 'qui sont des O_X-Modules inversibles :'",
           "'inversibles' italic", "roman", "italics",
           fx("$\\sh{O}_X$-Modules inversibles :", "$\\sh{O}_X$-Modules \\emph{inversibles} :")))
F.append(f(260, "after (21.2.7.1): 'où f est un élément régulier de Γ(U, O_X)'",
           "'régulier' italic", "roman", "italics",
           fx("où $f$ est un élément régulier de", "où $f$ est un élément \\emph{régulier} de")))
F.append(f(260, "after (21.2.7.1): 'L'ensemble I_X(Div^+(X)) de ces Idéaux'",
           "script I", "\\sh{J}_X", "symbol",
           fx("L'ensemble $\\sh{J}_X(\\operatorname{Div}^+(X))$", "L'ensemble $\\sh{I}_X(\\operatorname{Div}^+(X))$"),
           I_NOTE))
F.append(f(260, "display (21.2.8.1): 'O_X(D) = (I_X(D))^{-1}'",
           "script I (crop p260s4_top.png)", "\\sh{J}_X(D)", "symbol",
           fx("(\\sh{J}_X(D))^{-1}", "(\\sh{I}_X(D))^{-1}"), I_NOTE))

# ---------------------------------------------------------------- p. 261
F.append(f(261, "display (21.2.8.2): 'div(f) ≥ —D'",
           "long dash before D (crop p261s1_disp.png)", "-D", "convention",
           fx("\\geq-D.", "\\geq\\setmin D."),
           "Long dash used for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.",
           convention=7))
F.append(f(261, "(21.2.9): 'L'injection canonique J → M_X'",
           "plain arrow, no hook (crop p261s2_arrow.png)", "\\hookrightarrow", "symbol",
           fx("$\\sh{J}\\hookrightarrow\\sh{M}_X$", "$\\sh{J}\\to\\sh{M}_X$")))
F.append(f(261, "(21.2.9), after (21.2.9.3): 'D'autre part, on déduit aussitôt des isomorphismes canoniques'",
           "new indented paragraph (crop p261s3_dautre.png)",
           "follows \\] without a blank line, so it continues the paragraph unindented", "other",
           fx("\\]\nD'autre part, on déduit aussitôt", "\\]\n\nD'autre part, on déduit aussitôt")))
F.append(f(261, "(21.2.10): 'on peut parler de l'ensemble D(X) des classes d'équivalence des couples'",
           "'l'ensemble' and 'des classes d'équivalence' italic (crop p261s4_ital.png)", "roman", "italics",
           fx("on peut parler de l'ensemble $D(X)$ des classes d'équivalence des couples",
              "on peut parler de \\emph{l'ensemble} $D(X)$ \\emph{des classes d'équivalence} des couples")))

# ---------------------------------------------------------------- p. 262
F.append(f(262, "(21.2.10), after (21.2.10.1): 'c'est une loi de groupe commutatif,'",
           "'groupe commutatif' italic (crop p262s2_grp.png)", "roman", "italics",
           fx("c'est une loi de groupe commutatif,", "c'est une loi de \\emph{groupe commutatif},")))
F.append(f(262, "display (21.2.11.1), first map: 'D ⇝ cl(O_X(D), s_D)'",
           "wavy arrow (crop p262s2_wavy.png)", "\\mapsto", "symbol",
           fx("D\\mapsto\\operatorname{cl}(\\sh{O}_X(D),s_D)", "D\\leadsto\\operatorname{cl}(\\sh{O}_X(D),s_D)"),
           "Independent of the next entry."))
F.append(f(262, "display (21.2.11.1), second map: 'cl(L, s) ⇝ div(s)'",
           "wavy arrow", "\\mapsto", "symbol",
           fx("\\operatorname{cl}(\\sh{L},s)\\mapsto\\operatorname{div}(s)",
              "\\operatorname{cl}(\\sh{L},s)\\leadsto\\operatorname{div}(s)")))
F.append(f(262, "proof of (21.2.11): 'un isomorphisme de L|U sur O_U, transformant s|U'",
           "comma after O_U (crop p262s2_comma.png)", "no comma", "punctuation",
           fx("sur $\\sh{O}_U$ transformant", "sur $\\sh{O}_U$, transformant")))
F.append(f(262, "end of the proof of (21.2.11): 'tel que v̄(s) = s_D. C.Q.F.D.'",
           "'C.Q.F.D.' after 's_D.'", "missing", "missing",
           fx("tel que $\\overline{v}(s)=s_D$.", "tel que $\\overline{v}(s)=s_D$. C.Q.F.D.")))
F.append(f(262, "after the proof of (21.2.11): 'On peut transporter par le premier des isomorphismes'",
           "'transporter' italic", "roman", "italics",
           fx("On peut transporter par", "On peut \\emph{transporter} par")))
F.append(f(262, "(21.2.12): 'l'Idéal fractionnaire I_X(D)'",
           "script I (crop p262s3_2112.png)", "\\sh{J}_X(D)", "symbol",
           fx("l'Idéal fractionnaire $\\sh{J}_X(D)$ est donc", "l'Idéal fractionnaire $\\sh{I}_X(D)$ est donc"),
           I_NOTE))
F.append(f(262, "(21.2.12): 'est donc un Idéal de O_X, qui est'",
           "'Idéal de' italic", "roman", "italics",
           fx("un Idéal de $\\sh{O}_X$, qui est", "un \\emph{Idéal de} $\\sh{O}_X$, qui est")))
F.append(f(262, "(21.2.12): 'qui est un O_X-Module inversible;'",
           "'inversible' italic", "roman", "italics",
           fx("$\\sh{O}_X$-Module inversible;", "$\\sh{O}_X$-Module \\emph{inversible};")))
Y_NOTE = ("In (21.2.12) every Y of 'Y(D)' is a sans-serif capital (even strokes, no serifs; crops "
          "p262s3_YD.png, p262s3_Ys.png, p262s4_Ys.png), seven times on this page, while the bare Y of "
          "'si Y est un sous-préschéma', 'Y(D)=Y', 'x∈Y', 'Y∩U' is the ordinary roman Y. ega4-21b/21c write "
          "Y(D) about 20 more times: check each against the print.")
F.append(f(262, "(21.2.12): 'soit Y(D) le sous-préschéma fermé'",
           "sans-serif Y", "$Y(D)$ (roman/italic Y)", "font",
           fx("soit $Y(D)$ le sous-préschéma", "soit $\\mathsf{Y}(D)$ le sous-préschéma"), Y_NOTE))
F.append(f(262, "(21.2.12): 'Pour tout x∈Y(D), il y a par hypothèse'",
           "sans-serif Y", "$x\\in Y(D)$", "font",
           fx("Pour tout $x\\in Y(D)$", "Pour tout $x\\in\\mathsf{Y}(D)$"), Y_NOTE))
F.append(f(262, "(21.2.12): 'et une section régulière t∈Γ(U, O_X)'",
           "'régulière' italic", "roman", "italics",
           fx("une section régulière $t\\in", "une section \\emph{régulière} $t\\in")))
F.append(f(262, "(21.2.12): 'telle que I_X(D)|U = O_U.t (21.2.7)'",
           "script I", "\\sh{J}_X(D)|U", "symbol",
           fx("telle que $\\sh{J}_X(D)|U", "telle que $\\sh{I}_X(D)|U"), I_NOTE))
F.append(f(262, "(21.2.12): 'l'immersion canonique Y(D) → X'",
           "sans-serif Y", "$Y(D)\\to X$", "font",
           fx("l'immersion canonique $Y(D)\\to X$", "l'immersion canonique $\\mathsf{Y}(D)\\to X$"), Y_NOTE))
F.append(f(262, "(21.2.12): 'est régulière et de codimension 1 (19.1.4) en tout point de Y(D).'",
           "the reference (19.1.4) stands right after 'codimension 1', before 'en tout point de Y(D)' "
           "(crop p262s3_2112.png)",
           "the reference at the end of the sentence, after 'en tout point de $Y(D)$'", "word",
           fx("codimension $1$} en tout point de $Y(D)$ \\sref{IV.19.1.4}.",
              "codimension $1$} \\sref{IV.19.1.4} en tout point de $\\mathsf{Y}(D)$."),
           "One edit for this finding and the next (sans-serif Y of this 'Y(D)')."))
F.append(f(262, "(21.2.12): 'en tout point de Y(D).'",
           "sans-serif Y", "$Y(D)$", "font", None,
           "Covered by the edit of the preceding entry. " + Y_NOTE))
F.append(f(262, "(21.2.12): 'il existe un diviseur positif et un seul D'",
           "'un diviseur positif et un seul' italic (crop p262s4_mid.png)", "roman", "italics",
           fx("il existe un diviseur positif et un seul $D$", "il existe \\emph{un diviseur positif et un seul} $D$")))
F.append(f(262, "(21.2.12): 'tel que Y(D) = Y'",
           "sans-serif Y on the left, roman Y on the right", "$Y(D)=Y$", "font",
           fx("tel que $Y(D)=Y$", "tel que $\\mathsf{Y}(D)=Y$"), Y_NOTE))
F.append(f(262, "(21.2.12): 'où t est régulier dans Γ(U, O_X)'",
           "'régulier' italic", "roman", "italics",
           fx("où $t$ est régulier dans", "où $t$ est \\emph{régulier} dans")))
F.append(f(262, "(21.2.12): 'On notera que l'on a alors Supp(D) = Y(D)'",
           "new indented paragraph", "continues the paragraph (no blank line)", "other",
           fx("$\\Gamma(U,\\sh{O}_X)$.\nOn notera que l'on a alors", "$\\Gamma(U,\\sh{O}_X)$.\n\nOn notera que l'on a alors"),
           "Inside the env, so the blank line gives the printed indent."))
F.append(f(262, "(21.2.12): 'Supp(D) = Y(D)'",
           "sans-serif Y", "$\\operatorname{Supp}(D)=Y(D)$", "font",
           fx("\\operatorname{Supp}(D)=Y(D)", "\\operatorname{Supp}(D)=\\mathsf{Y}(D)"), Y_NOTE))
F.append(f(262, "(21.2.12), last line: 'c'est-à-dire que x∈Y(D).'",
           "sans-serif Y", "$x\\in Y(D)$", "font",
           fx("c'est-à-dire que $x\\in Y(D)$", "c'est-à-dire que $x\\in\\mathsf{Y}(D)$"), Y_NOTE))

# ---------------------------------------------------------------- p. 263
F.append(f(263, "heading 21.3: 'Équivalence linéaire des diviseurs.'",
           "final full stop", "no full stop", "punctuation",
           fx("\\subsection{Équivalence linéaire des diviseurs}", "\\subsection{Équivalence linéaire des diviseurs.}")))
F.append(f(263, "(21.3.1): 'si D—D' est un diviseur principal'",
           "long dash", "$D-D'$", "convention",
           fx("si $D-D'$ est un diviseur principal", "si $D\\setmin D'$ est un diviseur principal"),
           "Subtraction printed with the long dash (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.",
           convention=7))
F.append(f(263, "(21.3.1), end: 'les diviseurs linéairement équivalents à 0.'",
           "'linéairement équivalents à' italic, '0' roman", "roman", "italics",
           fx("les diviseurs linéairement équivalents à $0$.", "les diviseurs \\emph{linéairement équivalents à} $0$.")))
F.append(f(263, "(21.3.2): 'l'ensemble des classes d'équivalences des O_X-Modules inversibles'",
           "'d'équivalences' (plural; crop p263s2_equiv.png)", "d'équivalence", "misprint_in_print",
           fx("classes d'équivalence des $\\sh{O}_X$-Modules inversibles",
              "classes d'équivalences des $\\sh{O}_X$-Modules inversibles"),
           "The print's plural against 'la classe d'équivalence des O_X-Modules' two lines later and 'des classes "
           "d'équivalence des couples' on p. 261. The TeX silently corrects; the diplomatic text takes the printed "
           "reading back.",
           confidence="medium", corrected="classes d'équivalence des $\\sh{O}_X$-Modules inversibles"))
F.append(f(263, "display (21.3.2.1): 'r : cl(L, s) ⇝ cl(L)'",
           "wavy arrow (crop p263s2_r.png)", "\\mapsto", "symbol",
           fx("r:\\operatorname{cl}(\\sh{L},s)\\mapsto\\operatorname{cl}(\\sh{L})",
              "r:\\operatorname{cl}(\\sh{L},s)\\leadsto\\operatorname{cl}(\\sh{L})")))
F.append(f(263, "(21.3.2), after (21.3.2.1): 'est un homomorphisme du groupe D(X)'",
           "'homomorphisme' italic (crop p263s2_homo.png)", "roman", "italics",
           fx("est un homomorphisme du groupe $D(X)$", "est un \\emph{homomorphisme} du groupe $D(X)$")))
F.append(f(263, "(21.3.2): 'quelconques L_1, L_2 on a u*(L_1⊗L_2)'",
           "no comma after L_2 (crop p263s3_notons.png)", "comma after $\\sh{L}_2$", "punctuation",
           fx("quelconques $\\sh{L}_1$, $\\sh{L}_2$, on a", "quelconques $\\sh{L}_1$, $\\sh{L}_2$ on a")))
F.append(f(263, "Proposition (21.3.3): item labels (i), (ii)",
           "upright labels (i), (ii)", "label=(\\roman*) inside the italic proposition: italic labels",
           "convention",
           fx("\\label{IV.21.3.3}\n\\begin{enumerate}[label=(\\roman*)]",
              "\\label{IV.21.3.3}\n\\begin{enumerate}[label=\\textup{(\\roman*)}]"),
           "Roman-numeral labels in italic statements are upright (GLOBAL_ISSUES 16); one edit covers both labels.",
           convention=6))
F.append(f(263, "Proposition (21.3.3) (i): 'On a donc un homomorphisme injectif canonique'",
           "'injectif' roman inside the italic statement (crop p263s3_inj.png)", "italic", "convention",
           fx("un homomorphisme injectif canonique", "un homomorphisme \\textup{injectif} canonique"),
           convention=6))

# ---------------------------------------------------------------- p. 264
F.append(f(264, "Proposition (21.3.4): 'Alors l'homomorphisme canonique l' after the list a), b)",
           "new indented paragraph (crop p264s1_prop.png)",
           "text follows \\end{enumerate} without a blank line (no indent)", "other",
           fx("\\end{enumerate}\nAlors l'homomorphisme canonique", "\\end{enumerate}\n\nAlors l'homomorphisme canonique"),
           "GLOBAL_ISSUES 80 pattern."))
F.append(f(264, "proof of (21.3.4): 'grâce à (20.2.11, (ii))'",
           "'(20.2.11, (ii))' (crop p264s2_top.png)", "\\sref{IV.20.2.11},~(ii) prints '(20.2.11), (ii)'",
           "punctuation",
           fx("\\sref{IV.20.2.11},~(ii)", "\\sref{IV.20.2.11}[(ii)]")))
F.append(f(264, "proof of (21.3.4): 'au-dessus d'un ouvert schématiquement dense U de X'",
           "'schématiquement dense' italic", "roman", "italics",
           fx("ouvert schématiquement dense $U$ de $X$", "ouvert \\emph{schématiquement dense} $U$ de $X$")))
F.append(f(264, "proof of (21.3.4): 'ou encore dans le cas a), d'un ouvert U'",
           "italic 'a)' (crop p264s2_casa.png)", "upright 'a)'", "italics",
           fx("dans le cas a), d'un ouvert", "dans le cas \\emph{a)}, d'un ouvert"),
           "GLOBAL_ISSUES 88: the whole label italic in roman text."))
F.append(f(264, "proof of (21.3.4): 'contenant Ass(O_X) (20.2.13, (iv))'",
           "'(20.2.13, (iv))'", "\\sref{IV.20.2.13},~(iv) prints '(20.2.13), (iv)'", "punctuation",
           fx("\\operatorname{Ass}(\\sh{O}_X)$ \\sref{IV.20.2.13},~(iv)",
              "\\operatorname{Ass}(\\sh{O}_X)$ \\sref{IV.20.2.13}[(iv)]")))
F.append(f(264, "proof of (21.3.4): 'Cela étant, dans le cas b), on prend'",
           "italic 'b)' (crop p264s3_b.png)", "upright 'b)'", "italics",
           fx("dans le cas b), on prend", "dans le cas \\emph{b)}, on prend")))
F.append(f(264, "proof of (21.3.4), case b): 'distincte de {x_λ}‾ et telle que L|U_λ soit isomorphe'",
           "'et telle que' (crop p264s3_telle.png)", "'et tel que'", "misprint_in_print",
           fx("et tel que $\\sh{L}|U_\\lambda$", "et telle que $\\sh{L}|U_\\lambda$"),
           "The adjective refers to 'un ouvert U_λ' (masculine): 'tel'. The TeX silently corrects; the diplomatic "
           "text takes the printed 'telle' back.",
           corrected="et tel que $\\sh{L}|U_\\lambda$"))
F.append(f(264, "proof of (21.3.4): 'Dans le cas a), on peut prendre pour U'",
           "italic 'a)' (crop p264s3_casa2.png)", "upright 'a)'", "italics",
           fx("Dans le cas a), on peut", "Dans le cas \\emph{a)}, on peut")))
F.append(f(264, "proof of (21.3.4): 'S^{-1}A est un anneau semi-local'",
           "'semi-local' italic (crop p264s3_semi.png)", "roman", "italics",
           fx("un anneau semi-local dont", "un anneau \\emph{semi-local} dont")))
F.append(f(264, "proof of (21.3.4): 'donc ici libre de rang 1'",
           "'libre' italic", "roman", "italics",
           fx("donc ici libre de rang", "donc ici \\emph{libre} de rang")))
F.append(f(264, "Corollaire (21.3.5): 'inversible ample (II, 4.5.3)'",
           "the reference upright, bold II (crop p264s4_ample.png)", "set italic by the corollary environment",
           "convention",
           fx("ample (\\textbf{II}, 4.5.3)", "ample \\textup{(\\textbf{II}, 4.5.3)}"),
           convention=6))
F.append(f(264, "Corollaire (21.3.5): '(par exemple un préschéma quasi-projectif sur un spectre d'anneau noethérien "
                "(II, 5.3.1 et 4.6.6))'",
           "the whole parenthesis roman inside the italic corollary, with 'quasi-projectif' italic "
           "(crop p264s4_cor.png)",
           "all italic (corollary environment)", "convention",
           fx("(par exemple un préschéma quasi-projectif sur un spectre d'anneau noethérien (\\textbf{II}, 5.3.1 et 4.6.6))",
              "\\textup{(par exemple un préschéma \\emph{quasi-projectif} sur un spectre d'anneau noethérien "
              "(\\textbf{II}, 5.3.1 et 4.6.6))}"),
           "One edit for this finding and the next (italic 'quasi-projectif' inside the roman parenthesis).",
           convention=6))
F.append(f(264, "Corollaire (21.3.5): 'quasi-projectif'",
           "italic inside the roman parenthesis", "italic only because the whole corollary is italic",
           "italics", None,
           "Covered by the edit of the preceding entry (\\emph inside the \\textup)."))


def norm(t):
    return t.replace("\r\n", "\n")


src = norm(SRC.read_text(encoding="utf-8"))
pages = {p: norm((RUN / f"page_{p}.tex").read_text(encoding="utf-8")) for p in range(260, 265)}
bad = 0
for e in F:
    if not e["fix"]:
        continue
    old = e["fix"]["old"]
    n_page = pages[e["page"]].count(old)
    n_src = src.count(old)
    if n_page != 1 or n_src != 1:
        bad += 1
        print(f"PROBLEM p.{e['page']} page={n_page} src={n_src}: {old!r}")
    if e["fix"]["new"] == old:
        bad += 1
        print("NO-OP", old)

# overlap check between fixes on the same page (in the source file)
spans = []
for i, e in enumerate(F):
    if e["fix"]:
        k = src.find(e["fix"]["old"])
        spans.append((k, k + len(e["fix"]["old"]), i))
spans.sort()
for a, b in zip(spans, spans[1:]):
    if b[0] < a[1]:
        bad += 1
        print("OVERLAP", F[a[2]]["fix"]["old"], "||", F[b[2]]["fix"]["old"])

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
c = Counter()
for e in F:
    k = "misprint" if e["kind"] == "misprint_in_print" else ("convention" if e["kind"] == "convention" else "normal")
    c[(e["page"], k)] += 1
for p in range(260, 265):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("entries", len(F), "problems", bad)
