"""Build findings_330_332.json (pages 330-332 of EGA IV-4) and check every fix.

In the strings below the character '¶' stands for a line break of the TeX (LF).
The check applies the fixes of each page in list order to the LF-normalised
page_NNN.tex and requires every "old" to occur exactly once at its turn, and
also exactly once in the unmodified page text.
"""
import json
import sys

RUN = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = RUN + r"\findings_330_332.json"


def nl(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, nofix=False):
    e = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if nofix else {"old": nl(old), "new": nl(new)},
    }
    if kind == "misprint_in_print":
        e["corrected"] = nl(corrected)
    e["note"] = note
    F.append(e)


SCRIPT_I_NOTE = ("Script I, as everywhere in § 21 for I_X(D) (GLOBAL_ISSUES 109): the letter's lower loop sits on "
                 "the base line, without the descender of the script J; all seven I_X(D) on this page have the same "
                 "letter (crop p330_scriptI_all.png).")
SANS_Y_NOTE = ("The print's heavy sans-serif Y of Y(D) (even strokes, no serifs; crop p330_Y_compare.png, tiles 1, 2 "
               "and 4), written \\boldsymbol{\\mathsf{Y}} as decided in GLOBAL_ISSUES 109.")

# ---------------------------------------------------------------- page 330
add(330, "l. 2: 'le faisceau 𝒟iv_X/S est donc égal au préfaisceau U ⇝ Div(U/S)'",
    "wavy arrow (crop p330_wavy.png)", "\\mapsto",
    "symbol", None, "high",
    r"$U\mapsto\operatorname{Div}(U/S)$", r"$U\leadsto\operatorname{Div}(U/S)$",
    "GLOBAL_ISSUES 107/109: ega4-21 writes \\mapsto for the print's wavy arrows.")

add(330, "display (21.15.3.1): '𝒪^reg_X/S = 𝒪_X ∩ ℳ*_X/S'",
    "no full stop after ℳ*_X/S (crop p330_211531.png)", "full stop after \\mathscr M_{X/S}^*",
    "punctuation", None, "high",
    r"\cap\mathscr M_{X/S}^*.", r"\cap\mathscr M_{X/S}^*")

add(330, "'Pour tout ouvert U de X, Γ(U, 𝒪^reg_X/S) ...', l. 3: 'avec les notations de (20.6.1), que t ∈ T_X/S(U)'",
    "roman T (crop p330_TXS.png); the script 𝒯 comes in the next line ('le faisceau noté 𝒯_X/S')",
    "\\mathscr T_{X/S}(U)",
    "symbol", None, "high",
    r"que $t\in\mathscr T_{X/S}(U)$", r"que $t\in T_{X/S}(U)$",
    "(20.6.1) writes T_X/S(U) (roman) for the set of sections and 𝒯_X/S for the sheaf U ⇝ T_X/S(U) "
    "(ega4-20-fr.tex, (20.6.1), $T_{X/S}(U)$ and $\\sh{T}_{X/S}$); the print follows that notation here.")

add(330, "(21.15.3.3), l. 1: 'le sous-préschéma fermé Y(D)'",
    "heavy sans-serif Y (crops p330_s3_l1_2r.png, p330_Y_compare.png)", "$Y(D)$",
    "font", None, "high",
    r"fermé $Y(D)$", r"fermé $\boldsymbol{\mathsf{Y}}(D)$", SANS_Y_NOTE)

add(330, "(21.15.3.3), l. 2: 'défini par l'Idéal 𝓘_X(D) de 𝒪_X (21.6.5)'",
    "script I (crops p330_IXD_1.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"l'Idéal $\mathscr J_X(D)$ de", r"l'Idéal $\mathscr I_X(D)$ de", SCRIPT_I_NOTE)

add(330, "(21.15.3.3), l. 3: 'pour tout x ∈ Y(D), il y a un voisinage ouvert'",
    "heavy sans-serif Y (crops p330_Y_l3.png, p330_Y_compare.png)", "$x\\in Y(D)$",
    "font", None, "high",
    r"pour tout $x\in Y(D)$", r"pour tout $x\in\boldsymbol{\mathsf{Y}}(D)$", SANS_Y_NOTE)

add(330, "(21.15.3.3), l. 3: 'et une section t ∈ T_X/S(U) telle que'",
    "roman T (crop p330_s3_l34_right.png)", "\\mathscr T_{X/S}(U)",
    "symbol", None, "high",
    r"une section $t\in\mathscr T_{X/S}(U)$", r"une section $t\in T_{X/S}(U)$",
    "The notation T_X/S(U) of (20.6.1), as two lines above.")

add(330, "(21.15.3.3), l. 4: '𝓘_X(D)|U = 𝒪_U.t'",
    "script I (crops p330_s3_l34_left.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"$\mathscr J_X(D)|U=", r"$\mathscr I_X(D)|U=", SCRIPT_I_NOTE)

add(330, "(21.15.3.3), l. 4: '𝓘_X(D)|U = 𝒪_U.t'",
    "baseline period (measured: the dot occupies rows 253-257 of page_330_s3.png, its bottom on the base line "
    "of t and 𝒪 at row 257; crop p330_OUt.png)", "\\mathcal O_U\\cdot t",
    "symbol", None, "high",
    r"\mathcal O_U\cdot t", r"\mathcal O_U.t",
    "GLOBAL_ISSUES 65 pattern (\\cdot for the print's baseline period).")

add(330, "(21.15.3.3), l. 4: 'puisque x ∈ Y(D), l'image t_f(x) de t'",
    "roman Y with serifs, the same shape and weight as the roman Y of 'fermés Y de X' two lines lower "
    "(ASCII stem measure and crop p330_Y_compare.png, tiles 3 and 5; crop p330_Y_l4.png)",
    "$x\\in Y(D)$: keeps the printed reading",
    "misprint_in_print", None, "high",
    None, None,
    "Wrong fount: the other three Y(D) on this page have the heavy sans-serif Y of (21.2.12). The TeX keeps the "
    "printed reading (fix null; the edition writes the print's roman capitals as $Y$). Corrected edition: the "
    "sans-serif Y like the other Y(D).",
    corrected=r"puisque $x\in\boldsymbol{\mathsf{Y}}(D)$", nofix=True)

add(330, "(21.15.3.3), l. 5: 'appartient à l'idéal maximal de 𝒪_X_f(x),x, et en outre, par définition'",
    "comma after 𝒪_X_f(x),x, on the base line (crop p330_s3_l5_comma.png)", "no comma",
    "punctuation", None, "high",
    r"_{X_{f(x)},x}$ et en outre", r"_{X_{f(x)},x}$, et en outre")

add(330, "(21.15.3.3), l. 7: 'que l'immersion canonique Y(D) → X est transversalement'",
    "heavy sans-serif Y (crops p330_s3_l7_8left.png, p330_Y_compare.png)", "$Y(D)\\to X$",
    "font", None, "high",
    r"$Y(D)\to X$", r"$\boldsymbol{\mathsf{Y}}(D)\to X$", SANS_Y_NOTE)

add(330, "(21.15.3.3), l. 9: 'on voit qu'on peut identifier canoniquement les diviseurs positifs'",
    "only 'identifier' italic; 'canoniquement' roman (crop p330_s3_l9_left.png)", "\\emph{identifier canoniquement}",
    "italics", None, "high",
    r"\emph{identifier canoniquement}", r"\emph{identifier} canoniquement")

add(330, "Proposition (21.15.4), l. 1: 'Soient D un diviseur sur X, 𝓘_X(D) l'Idéal fractionnaire inversible'",
    "script I (crops p330_prop4_l1.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"$\mathscr J_X(D)$ l'Idéal", r"$\mathscr I_X(D)$ l'Idéal", SCRIPT_I_NOTE)

add(330, "Proposition (21.15.4), l. 2: 'correspondant (21.2.5). Pour que'",
    "the reference upright: upright parentheses and figures (measured: the parentheses' end points stand "
    "one above the other; crop p330_prop4_l2_4.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"correspondant (21.2.5).", r"correspondant \textup{(21.2.5)}.")

add(330, "Proposition (21.15.4), l. 3: 'on ait (𝓘_X(D) ∩ ℳ*_X/S)_x ≠ 0'",
    "script I (crops p330_prop4_ne.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"$(\mathscr J_X(D)\cap", r"$(\mathscr I_X(D)\cap", SCRIPT_I_NOTE)

add(330, "Proposition (21.15.4), l. 3: '(ou, ce qui revient au même, que l'on ait'",
    "the opening parenthesis upright, the words italic (measured on page_330_s4.png: the parenthesis' top and "
    "bottom ends at x 990-993, no slant, unlike the slanted italic parentheses of p. 255; crop p330_prop4_openparen.png)",
    "italic parenthesis (text in the proposition environment)",
    "convention", 6, "high",
    r"\ne0$ (ou,", r"\ne0$ \textup{(}ou,",
    "Item 96/101: fixed by the print; the closing parenthesis is the next entry but one.")

add(330, "Proposition (21.15.4), l. 3: 'que l'on ait 𝓘_X(D) ⊂ ℳ_X/S et'",
    "script I (crops p330_prop4_ou.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"l'on ait $\mathscr J_X(D)\subset", r"l'on ait $\mathscr I_X(D)\subset", SCRIPT_I_NOTE)

add(330, "Proposition (21.15.4), l. 4: '𝓘_X(D)^-1 ⊂ ℳ_X/S).'",
    "script I (crops p330_prop4_end.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"$\mathscr J_X(D)^{-1}", r"$\mathscr I_X(D)^{-1}", SCRIPT_I_NOTE)

add(330, "Proposition (21.15.4), l. 4: '... ⊂ ℳ_X/S).' (closing parenthesis)",
    "the closing parenthesis upright (measured on page_330_s4.png: top end x 728, bottom end x 730-732, "
    "no italic slant; crop p330_prop4_closeparen.png)", "italic parenthesis (text in the proposition environment)",
    "convention", 6, "high",
    r"\subset\mathscr M_{X/S}$).", r"\subset\mathscr M_{X/S}$\textup{)}.",
    "Pairs with the opening parenthesis two entries above.")

add(330, "proof of (21.15.4), l. 2: 'comme 𝓘_X(D)|U est l'Idéal fractionnaire inversible 𝒪_U f'",
    "script I (crops p330_proof4.png, p330_scriptI_all.png)", "\\mathscr J_X(D)",
    "symbol", None, "high",
    r"$\mathscr J_X(D)|U$ est", r"$\mathscr I_X(D)|U$ est", SCRIPT_I_NOTE)

# ---------------------------------------------------------------- page 331
add(331, "Proposition (21.15.5), l. 2: 'définis canoniquement par D (21.2.8 et 21.2.9).'",
    "the reference roman: upright parentheses and figures, roman 'et' (crop p331_prop5.png)",
    "italic (proposition environment)",
    "convention", 6, "high",
    r"(21.2.8 et 21.2.9).", r"\textup{(21.2.8 et 21.2.9)}.")

add(331, "proof of (21.15.5), l. 1: 'où f ∈ Γ(U, ℳ*_X) dire que'",
    "no comma before 'dire' (crop p331_proof5_comma1.png)", "comma after Γ(U, ℳ*_X): silent correction",
    "misprint_in_print", None, "high",
    r"$f\in\Gamma(U,\mathscr M_X^*)$, dire que", r"$f\in\Gamma(U,\mathscr M_X^*)$ dire que",
    "The 'si ...' clause is not closed before the main clause 'dire que ... signifie'. The TeX silently "
    "corrects; the fix restores the printed reading.",
    corrected=r"$f\in\Gamma(U,\mathscr M_X^*)$, dire que")

add(331, "proof of (21.15.5), l. 2: 'signifie, en vertu des définitions (20.6.2) que f^-1 ∈ ...'",
    "no comma after (20.6.2) (crop p331_proof5_comma2.png)", "comma after (20.6.2): silent correction",
    "misprint_in_print", None, "high",
    r"définitions (20.6.2), que", r"définitions (20.6.2) que",
    "The incise 'en vertu des définitions (20.6.2)' opened by a comma is not closed. The TeX silently "
    "corrects; the fix restores the printed reading.",
    corrected=r"définitions (20.6.2), que")

add(331, "proof of (21.15.5), l. 2: 'que f^-1 ∈ Γ(U, ℳ*_X/S), d'où la proposition'",
    "ℳ with the star (crop p331_proof5_comma2.png)", "\\mathscr M_{X/S} without star",
    "formula", None, "high",
    r"$f^{-1}\in\Gamma(U,\mathscr M_{X/S})$", r"$f^{-1}\in\Gamma(U,\mathscr M_{X/S}^*)$")

add(331, "Proposition (21.15.6), l. 2: 'on ait D_x ⩾ 0 (resp. D_x = 0).'",
    "'(resp.' and the parentheses upright (crop p331_prop6.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"(resp. $D_x=0$)", r"\textup{(resp. $D_x=0$)}")

add(331, "Proposition (21.15.6), l. 3: 'Alors on a D ⩾ 0 (resp. D = 0)'",
    "'(resp.' and the parentheses upright (crop p331_prop6_end.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"(resp. $D=0$)", r"\textup{(resp. $D=0$)}",
    "Apply before the next entry (misprint: the final full stop), which concerns the character after this edit.")

add(331, "Proposition (21.15.6), end of the statement: '... (resp. D = 0)'",
    "no full stop at the end of the statement (crop p331_prop6_end.png)", "full stop: silent correction",
    "misprint_in_print", None, "high",
    r".¶\end{proposition}¶¶\begin{proof}¶Comme", r"¶\end{proposition}¶¶\begin{proof}¶Comme",
    "Listed after the convention fix of '(resp. $D=0$)' (previous entry); this 'old' starts at the full stop, "
    "outside that edit, and occurs once both before and after it. The TeX silently corrects; the fix restores "
    "the printed reading.",
    corrected=r"\textup{(resp. $D=0$)}.")

add(331, "proof of (21.15.6), l. 4: 'si T = X—dom(φ) on a'",
    "long dash for set difference (crop p331_proof6_dom.png)", "minus sign",
    "convention", 7, "high",
    r"$T=X-\operatorname{dom}", r"$T=X\setmin\operatorname{dom}",
    "The next entry (misprint) is at the end of the same formula; the two edits do not overlap.")

add(331, "proof of (21.15.6), l. 4: 'Mais cette hypothèse signifie que, si T = X—dom(φ) on a prof(...) ⩾ 2'",
    "no comma after dom(φ) (crop p331_proof6_dom.png)", "comma after dom(\\varphi): silent correction",
    "misprint_in_print", None, "high",
    r"(\varphi)$, on a", r"(\varphi)$ on a",
    "The incise 'si T = X—dom(φ)' opened by the comma after 'que' is not closed. The TeX silently corrects; "
    "the fix restores the printed reading.",
    corrected=r"(\varphi)$, on a")

add(331, "(21.15.7), l. 4: 'que l'on a alors g*(D) ∈ Div(S'/S).'",
    "Div(S'/S) (crop p331_2157_Sprime.png)", "Div(X'/S): silent correction",
    "misprint_in_print", None, "high",
    r"g^*(D)\in\operatorname{Div}(X'/S)", r"g^*(D)\in\operatorname{Div}(S'/S)",
    "g*(D) is a divisor on X', so the group is Div(X'/S), as in the hypothesis D ∈ Div(X/S) and in (21.15.8). "
    "The TeX silently corrects; the fix restores the printed reading.",
    corrected=r"g^*(D)\in\operatorname{Div}(X'/S)")

add(331, "(21.15.8), l. 2: 'un S-morphisme fini et plat.'",
    "'fini' and 'plat' italic, 'et' roman (crop p331_2158a.png)", "\\emph{fini et plat}",
    "italics", None, "high",
    r"\emph{fini et plat}", r"\emph{fini} et \emph{plat}")

add(331, "(21.15.8), l. 5: 'autrement dit g est un morphisme localement libre (18.2.7)'",
    "'localement libre' italic (crop p331_2158a.png)", "roman",
    "italics", None, "high",
    r"localement libre (18.2.7)", r"\emph{localement libre} (18.2.7)")

add(331, "(21.15.8), l. 7: 'et toute section t' ∈ Γ(g^-1(U); 𝒯_X'/S), la norme'",
    "semicolon after g^-1(U) (crop p331_2158_semicolon.png)", "comma: silent correction",
    "misprint_in_print", None, "high",
    r"\Gamma(g^{-1}(U),\mathscr T_{X'/S})", r"\Gamma(g^{-1}(U);\mathscr T_{X'/S})",
    "Γ(U, F) is written with a comma everywhere else (e.g. Γ(U, 𝒯_X/S) in the next line). The TeX silently "
    "corrects; the fix restores the printed reading.",
    corrected=r"\Gamma(g^{-1}(U),\mathscr T_{X'/S})")

add(331, "(21.15.8), l. 11: 'ℒ = N_X'/X(ℒ') au-dessus de X, régulière relativement à S.'",
    "'régulière relativement à' italic (crop p331_2158c.png)", "roman",
    "italics", None, "high",
    r"au-dessus de $X$, régulière relativement à $S$.",
    r"au-dessus de $X$, \emph{régulière relativement à $S$}.")

add(331, "(21.15.8), l. 13: 'pour tout diviseur D' ∈ Div(X'/S), on a g_*(D') ∈ Div(X/S).'",
    "'on a' italic (crop p331_2158c.png)", "roman",
    "italics", None, "high",
    r"on a $g_*(D')", r"\emph{on a} $g_*(D')")

add(331, "(21.15.9), l. 1: 'Considérons enfin un morphisme quelconque S' → S'",
    "'quelconque' italic (crop p331_2159.png)", "roman",
    "italics", None, "high",
    r"morphisme quelconque $S'\to S$", r"morphisme \emph{quelconque} $S'\to S$")

add(331, "(21.15.9), l. 6: 'au-dessus de p^-1(U), régulière relativement à S (20.6.5, (iii))'",
    "'régulière relativement à' italic (crop p331_2159.png)", "roman",
    "italics", None, "high",
    r"$p^{-1}(U)$, régulière¶relativement à $S$ (20.6.5",
    r"$p^{-1}(U)$, \emph{régulière¶relativement à $S$} (20.6.5")

# ---------------------------------------------------------------- page 332
add(332, "display after 'deux foncteurs contravariants': 'Div_X/S : Sch_/S → Ab,'",
    "Sch and Ab bold italic (crop p332_functors.png)", "\\mathbf{Sch}, \\mathbf{Ab} (bold upright)",
    "font", None, "high",
    r"\mathbf{Sch}_{/S}\longrightarrow\mathbf{Ab}",
    r"\boldsymbol{\mathit{Sch}}_{/S}\longrightarrow\boldsymbol{\mathit{Ab}}",
    "As the bold italic Sch of IV-3 pp. 50-51 (\\boldsymbol{\\mathit{Sch}}) and Ab of GLOBAL_ISSUES 53.")

add(332, "same display: 'Div+_X/S : Sch_/S → Ens'",
    "Sch and Ens bold italic (crop p332_functors.png)", "\\mathbf{Sch}, \\mathbf{Ens} (bold upright)",
    "font", None, "high",
    r"\mathbf{Sch}_{/S}\longrightarrow\mathbf{Ens}",
    r"\boldsymbol{\mathit{Sch}}_{/S}\longrightarrow\boldsymbol{\mathit{Ens}}")

add(332, "'Pour tout diviseur D ∈ Div(X/S), ...', l. 2: 'n'est autre d'ailleurs que l'image réciproque p*(D)'",
    "'image réciproque' roman (crop p332_imrec.png)", "\\emph{image réciproque}",
    "italics", None, "high",
    r"l'\emph{image réciproque}", r"l'image réciproque")


# ---------------------------------------------------------------- check
def page_text(p):
    with open(rf"{RUN}\page_{p}.tex", encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
texts = {p: page_text(p) for p in (330, 331, 332)}
cur = dict(texts)
for i, e in enumerate(F):
    fx = e["fix"]
    if fx is None:
        continue
    p = e["page"]
    n0 = texts[p].count(fx["old"])
    n1 = cur[p].count(fx["old"])
    if n0 != 1 or n1 != 1:
        ok = False
        print(f"FAIL entry {i} page {p}: original count {n0}, sequential count {n1}: {fx['old']!r}")
    cur[p] = cur[p].replace(fx["old"], fx["new"], 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
cnt = Counter()
for e in F:
    k = "misprint" if e["kind"] == "misprint_in_print" else ("convention" if e["kind"] == "convention" else "normal")
    cnt[(e["page"], k)] += 1
for p in (330, 331, 332):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("entries", len(F), "all olds unique:", ok)
if len(sys.argv) > 1:
    for p in (330, 331, 332):
        with open(rf"{RUN}\crops_330_332\after_{p}.tex", "w", encoding="utf-8", newline="\n") as fh:
            fh.write(cur[p])
