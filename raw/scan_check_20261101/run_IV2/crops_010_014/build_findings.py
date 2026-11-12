"""Build findings_010_014.json for EGA IV-2 pp. 10-14 and check every fix.

Newlines in old/new strings are written as the character U+23CE and replaced by LF.
"""
import json
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUT = RUN / "findings_010_014.json"
NL = "⏎"


def n(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else {"old": n(old), "new": n(new)})
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


WAVY = "Wavy arrow (GLOBAL_ISSUES 33), written \\leadsto as in the earlier page fixes; not convention 3."
REF6 = "Reference printed upright inside the italic statement."
LAB6 = "Item label printed upright inside the italic statement (GLOBAL_ISSUES 16)."
RESP6 = "'(resp.' printed roman inside the italic statement."

# ---------------- page 10 ----------------
add(10, "Proposition (2.2.2), item c), l. 1", "𝒢 ⇝ ℱ⊗_Y 𝒢 (wavy arrow)", r"\mathscr G\mapsto\mathscr F\otimes_Y\mathscr G",
    "symbol", None, "high", r"Le foncteur⏎$\mathscr G\mapsto", r"Le foncteur⏎$\mathscr G\leadsto", WAVY)
add(10, "proof of (2.2.2), 'fidèlement plat (0_I, 6.4.5)'", "(0_I, 6.4.5) with a bold 0", r"$(0_{\mathrm I},6.4.5)$",
    "convention", 2, "high", r"$(0_{\mathrm I},6.4.5)$", r"$(\mathbf{0}_{\mathrm I},6.4.5)$")
add(10, "proof of (2.2.2), 'La relation (ℱ⊗_Y𝒢)⊗_{𝒪_Y}𝒪_y = 0'",
    "(ℱ⊗_Y 𝒢)⊗_{𝒪_Y} 𝒪_y = 0: the second tensor sign is indexed by 𝒪_Y (enlarged crop)",
    r"(\mathscr F\otimes_Y\mathscr G)\otimes_Y\mathcal O_y=0", "formula", None, "high",
    r")\otimes_Y\mathcal O_y=0$", r")\otimes_{\mathcal O_Y}\mathcal O_y=0$")
add(10, "proof of (2.2.2), after 'pour un point fermé y de Y implique'",
    "in the running text: 'implique (ℱ⊗_{𝒪_Y} 𝒪_y)⊗_{𝒪_y} 𝒢_y = 0, donc'; first tensor sign indexed by 𝒪_Y (enlarged crop)",
    r"displayed \[(\mathscr F\otimes_Y\mathcal O_y)\otimes_{\mathcal O_y}\mathscr G_y=0,\]", "formula", None, "high",
    r"\[⏎(\mathscr F\otimes_Y\mathcal O_y)\otimes_{\mathcal O_y}\mathscr G_y=0,⏎\]",
    r"$(\mathscr F\otimes_{\mathcal O_Y}\mathcal O_y)\otimes_{\mathcal O_y}\mathscr G_y=0$,",
    "Two differences in one edit: the print sets the formula inline, and its first tensor sign is ⊗_{𝒪_Y} (TeX ⊗_Y).")
add(10, "proof of (2.2.2), 'autrement dit le foncteur 𝒢⇝ℱ⊗_Y𝒢 est fidèle'", "𝒢 ⇝ ℱ⊗_Y 𝒢 (wavy arrow)",
    r"\mathscr G\mapsto\mathscr F\otimes_Y\mathscr G", "symbol", None, "high",
    r"le foncteur $\mathscr G\mapsto", r"le foncteur $\mathscr G\leadsto", WAVY)
add(10, "proof of (2.2.2), 'la projection g' : X'→X (II, 1.5.5)'", "(II, 1.5.5) with a bold II", "(II, 1.5.5)",
    "convention", 2, "high", "(II, 1.5.5)", r"(\textbf{II}, 1.5.5)")
add(10, "proof of (2.2.2), 'le foncteur ℋ'⇝g'_*(ℋ')'", "ℋ' ⇝ g'_*(ℋ') (wavy arrow)", r"\mathscr H'\mapsto g'_*(\mathscr H')",
    "symbol", None, "high", r"$\mathscr H'\mapsto", r"$\mathscr H'\leadsto", WAVY)
add(10, "proof of (2.2.2), 'quasi-cohérents (I, 1.6.4)'", "(I, 1.6.4) with a bold I", "(I, 1.6.4)",
    "convention", 2, "high", "(I, 1.6.4)", r"(\textbf{I}, 1.6.4)")
add(10, "proof of (2.2.2), 'pour voir que 𝒢'⇝ℱ⊗_Y𝒢' est exact et fidèle'", "𝒢' ⇝ ℱ⊗_Y 𝒢' (wavy arrow)",
    r"\mathscr G'\mapsto\mathscr F\otimes_Y\mathscr G'", "symbol", None, "high",
    r"$\mathscr G'\mapsto\mathscr F", r"$\mathscr G'\leadsto\mathscr F", WAVY)
add(10, "proof of (2.2.2), 'il suffit par suite de voir que le foncteur 𝒢'⇝g'_*(ℱ⊗_Y𝒢') l'est'",
    "in the running text: 'le foncteur 𝒢' ⇝ g'_*(ℱ⊗_Y 𝒢') l'est' (wavy arrow)",
    r"displayed \[\mathscr G'\mapsto g'_*(\mathscr F\otimes_Y\mathscr G')\]", "formula", None, "high",
    r"\[⏎\mathscr G'\mapsto g'_*(\mathscr F\otimes_Y\mathscr G')⏎\]",
    r"$\mathscr G'\leadsto g'_*(\mathscr F\otimes_Y\mathscr G')$",
    "Two differences in one edit: the print sets the formula inline, and the arrow is the wavy arrow (GLOBAL_ISSUES 33).")
add(10, "proof of (2.2.2), 'on a g'_*(ℱ⊗_Y𝒢') = g'_*(g'^*(ℱ)⊗_{𝒪_X'} f'^*(𝒢'))'",
    "g'^*(ℱ)⊗_{𝒪_{X'}} f'^*(𝒢') (enlarged crop)", r"g'^*(\mathscr F)\otimes_{X'}f'^*(\mathscr G')",
    "formula", None, "high", r"\otimes_{X'}f'^*", r"\otimes_{\mathcal O_{X'}}f'^*")
add(10, "proof of (2.2.2), 'En effet, on sait (II, 1.5.2)'", "(II, 1.5.2) with a bold II", "(II, 1.5.2)",
    "convention", 2, "high", "(II, 1.5.2)", r"(\textbf{II}, 1.5.2)")
add(10, "proof of (2.2.2), 'ℱ→g'_*(g'^*(ℱ)) (0_I, 4.4.3.2)'", "(0_I, 4.4.3.2) with a bold 0", r"$(0_{\mathrm I},4.4.3.2)$",
    "convention", 2, "high", r"$(0_{\mathrm I},4.4.3.2)$", r"$(\mathbf{0}_{\mathrm I},4.4.3.2)$")
add(10, "proof of (2.2.2), 'l'homomorphisme canonique (0_I, 4.2.2.1)'", "(0_I, 4.2.2.1) with a bold 0", r"$(0_{\mathrm I},4.2.2.1)$",
    "convention", 2, "high", r"$(0_{\mathrm I},4.2.2.1)$", r"$(\mathbf{0}_{\mathrm I},4.2.2.1)$")
add(10, "proof of (2.2.2), 'Cela étant, le foncteur 𝒢'⇝g_*(𝒢')'", "𝒢' ⇝ g_*(𝒢') (wavy arrow)", r"\mathscr G'\mapsto g_*(\mathscr G')",
    "symbol", None, "high", r"$\mathscr G'\mapsto g_*", r"$\mathscr G'\leadsto g_*", WAVY)
add(10, "proof of (2.2.2), 'il en est de même de 𝒢⇝ℱ⊗_Y𝒢 = ℱ⊗_{𝒪_X} f^*(𝒢)'", "𝒢 ⇝ ℱ⊗_Y 𝒢 (wavy arrow)",
    r"\mathscr G\mapsto\mathscr F\otimes_Y\mathscr G", "symbol", None, "high",
    r"$\mathscr G\mapsto\mathscr F\otimes_Y\mathscr G⏎=", r"$\mathscr G\leadsto\mathscr F\otimes_Y\mathscr G⏎=", WAVY)
add(10, "Corollaire (2.2.3), 'conditions équivalentes de (2.2.1) (ou (2.2.2))'",
    "(2.2.1) and (2.2.2) upright; 'ou' italic", "(2.2.1) (ou (2.2.2)) set in the italic environment",
    "convention", 6, "high", "de (2.2.1) (ou (2.2.2)),", r"de \textup{(2.2.1)} (ou \textup{(2.2.2)}),", REF6)
add(10, "proof of (2.2.3), 'le foncteur N⇝M⊗_A N'", "N ⇝ M⊗_A N (wavy arrow)", r"N\mapsto M\otimes_A N",
    "symbol", None, "high", r"$N\mapsto M", r"$N\leadsto M", WAVY)
add(10, "proof of (2.2.3), 'la conclusion résulte de (0_I, 6.4.1)'", "(0_I, 6.4.1) with a bold 0", r"$(0_{\mathrm I},6.4.1)$",
    "convention", 2, "high", r"$(0_{\mathrm I},6.4.1)$", r"$(\mathbf{0}_{\mathrm I},6.4.1)$")
add(10, "Définition (2.2.4), 'conditions équivalentes de (2.2.1) sont satisfaites'", "(2.2.1) upright",
    "(2.2.1) set in the italic environment", "convention", 6, "high",
    "équivalentes de (2.2.1) sont", r"équivalentes de \textup{(2.2.1)} sont", REF6)
add(10, "Définition (2.2.4), 'est fidèlement plat relativement à f (ou à Y)'",
    "'fidèlement plat relativement à' italic like the rest of the definition (no change of face)",
    r"\emph{fidèlement plat relativement à} inside the italic definition environment (typeset upright)",
    "convention", 6, "high", r"\emph{fidèlement plat⏎relativement à}", r"fidèlement plat⏎relativement à",
    "Printed italic words left upright: drop the \\emph inside the italic environment (FIX_POLICY 2.6).")

# ---------------- page 11 ----------------
add(11, "l. 4, '(ℱ_y)_x = ℱ_x⊗_{𝒪_y} k(y) ≠ 0'", "k(y) with a bold italic k", "k(y)",
    "convention", 1, "high", r"k(y)\neq0", r"\boldsymbol{k}(y)\neq0")
add(11, "proof of (2.2.6), 'En effet (I, 9.1.13 et 3.6.1)'", "(I, 9.1.13 et 3.6.1) with a bold I", "(I, 9.1.13 et 3.6.1)",
    "convention", 2, "high", "(I, 9.1.13 et 3.6.1)", r"(\textbf{I}, 9.1.13 et 3.6.1)")
add(11, "after the proof of (2.2.6): '... la condition du corollaire. / En particulier, le 𝒪_X-Module 𝒪_X'",
    "'En particulier' begins a new indented paragraph", "same paragraph: 'corollaire. En particulier,'",
    "other", None, "high", "corollaire. En particulier,", "corollaire.⏎⏎En particulier,",
    "Missing paragraph break.")
add(11, "'le morphisme f est fidèlement plat (0_I, 6.7.8)'", "(0_I, 6.7.8) with a bold 0", r"$(0_{\mathrm I},6.7.8)$",
    "convention", 2, "high", r"$(0_{\mathrm I},6.7.8)$", r"$(\mathbf{0}_{\mathrm I},6.7.8)$")
add(11, "Proposition (2.2.7), 'soit injectif (resp. surjectif, bijectif, nul)'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    "injectif (resp. surjectif", r"injectif \textup{(resp.} surjectif", RESP6)
add(11, "Proposition (2.2.7), 'l'application 𝒢'⇝ℱ⊗_Y𝒢''", "𝒢' ⇝ ℱ⊗_Y 𝒢' (wavy arrow)",
    r"\mathscr G'\mapsto\mathscr F\otimes_Y\mathscr G'", "symbol", None, "high",
    r"$\mathscr G'\mapsto\mathscr F", r"$\mathscr G'\leadsto\mathscr F", WAVY)
add(11, "proof of (2.2.8), 'Hom_{𝒪_Y}(𝒪_Y, 𝒢) (0_I, 5.1.1)'", "(0_I, 5.1.1) with a bold 0", r"$(0_{\mathrm I},5.1.1)$",
    "convention", 2, "high", r"$(0_{\mathrm I},5.1.1)$", r"$(\mathbf{0}_{\mathrm I},5.1.1)$")
add(11, "proof of (2.2.8), '(0_I, 5.1.1) et de même'", "no comma: '(0_I, 5.1.1) et de même' (enlarged crop)",
    r"$(0_{\mathrm I},5.1.1)$, et de même", "punctuation", None, "high",
    "$, et de même", "$ et de même", "Extra comma in the TeX. Independent of the convention-2 edit just before.")
add(11, "proof of (2.2.8), 'le foncteur 𝒢⇝f^*(𝒢)'", "𝒢 ⇝ f^*(𝒢) (wavy arrow)", r"\mathscr G\mapsto f^*(\mathscr G)",
    "symbol", None, "high", r"$\mathscr G\mapsto f^*", r"$\mathscr G\leadsto f^*", WAVY)

# ---------------- page 12 ----------------
add(12, "Remarque (2.2.9), l. 1, 'et par suite le foncteur 𝒢_y⇝𝒢_y⊗_{𝒪_y}ℱ_x est fidèle'",
    "𝒢_y ⇝ 𝒢_y⊗_{𝒪_y} ℱ_x (wavy arrow)", r"\mathscr G_y\mapsto\mathscr G_y\otimes_{\mathcal O_y}\mathscr F_x",
    "symbol", None, "high", r"par suite le foncteur⏎$\mathscr G_y\mapsto", r"par suite le foncteur⏎$\mathscr G_y\leadsto", WAVY)
add(12, "Remarque (2.2.9), l. 2, 'pour tout x∈f^{-1}(y) le foncteur 𝒢_y⇝𝒢_y⊗_{𝒪_y}ℱ_x est exact'",
    "𝒢_y ⇝ 𝒢_y⊗_{𝒪_y} ℱ_x (wavy arrow)", r"\mathscr G_y\mapsto\mathscr G_y\otimes_{\mathcal O_y}\mathscr F_x",
    "symbol", None, "high", r"(y)$ le foncteur⏎$\mathscr G_y\mapsto", r"(y)$ le foncteur⏎$\mathscr G_y\leadsto", WAVY)
add(12, "Proposition (2.2.10), 'Pour que 𝒢' soit plat (resp. fidèlement plat)'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    "soit plat⏎(resp.", r"soit plat⏎\textup{(resp.}", RESP6)
add(12, "Proposition (2.2.10), 'soit un 𝒪_X'-Module plat (resp. fidèlement plat)'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    "-Module plat⏎(resp.", r"-Module plat⏎\textup{(resp.}", RESP6)
add(12, "(2.2.10.1)", "ℋ'' ⇝ ℋ''⊗_Z 𝒢' ⇝ (ℋ''⊗_Z 𝒢')⊗_Y ℱ = ... (two wavy arrows)",
    r"\mathscr H''\mapsto\mathscr H''\otimes_Z\mathscr G' \mapsto(\mathscr H''\otimes_Z\mathscr G')\otimes_Y\mathscr F",
    "symbol", None, "high", r"\mathscr H''\mapsto\mathscr H''\otimes_Z\mathscr G'⏎\mapsto(",
    r"\mathscr H''\leadsto\mathscr H''\otimes_Z\mathscr G'⏎\leadsto(", WAVY + " Both arrows of the display in one edit.")
add(12, "proof of (2.2.10), 'il en est de même de ℋ''⇝ℋ''⊗_Z𝒢''", "ℋ'' ⇝ ℋ''⊗_Z 𝒢' (wavy arrow)",
    r"\mathscr H''\mapsto\mathscr H''\otimes_Z\mathscr G'", "symbol", None, "high",
    r"$\mathscr H''\mapsto\mathscr H''\otimes_Z\mathscr G'$,", r"$\mathscr H''\leadsto\mathscr H''\otimes_Z\mathscr G'$,", WAVY)
add(12, "proof of (2.2.10), 'puisque le foncteur ℳ'⇝ℳ'⊗_Y ℱ'", "ℳ' ⇝ ℳ'⊗_Y ℱ (wavy arrow)",
    r"\mathscr M'\mapsto\mathscr M'\otimes_Y\mathscr F", "symbol", None, "high",
    r"$\mathscr M'\mapsto", r"$\mathscr M'\leadsto", WAVY)
add(12, "proof of (2.2.10), last line: '(de la catégorie des 𝒪_Y'-Modules quasi-cohérents dans celle des 𝒪_X-Modules quasi-cohérents)'",
    "𝒪_X-Modules, no prime on X (enlarged crop; the prime of 𝒪_Y' on the line above is clear)",
    r"$\mathcal O_{X'}$-Modules (silently corrected)", "misprint_in_print", None, "high",
    r"$\mathcal O_{X'}$-Modules quasi-cohérents)", r"$\mathcal O_X$-Modules quasi-cohérents)",
    "ℳ'⊗_Y ℱ is a Module on X' = X×_Y Y' (the hypothesis is (2.2.2) a) for the base change Y'→Y), so the target "
    "category is that of the 𝒪_X'-Modules. The TeX silently corrects; the fix restores the printed 𝒪_X.",
    corrected=r"\mathcal O_{X'}")
for lab in ("i", "ii", "iii", "iv"):
    add(12, f"Corollaire (2.2.11), label ({lab})", f"label ({lab}) upright", f"\\item[({lab})] inside the italic statement (typeset italic)",
        "convention", 6, "high", f"\\item[({lab})]", f"\\item[\\textup{{({lab})}}]", LAB6)
add(12, "Corollaire (2.2.11) (iii), 'Pour que 𝒢 soit plat (resp. fidèlement plat)'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    r"$\mathscr G$ soit plat (resp.", r"$\mathscr G$ soit plat \textup{(resp.}", RESP6)
add(12, "Corollaire (2.2.11) (iii), 'que f^*(𝒢) soit plat (resp. fidèlement plat)'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    r"$f^*(\mathscr G)$ soit plat (resp.", r"$f^*(\mathscr G)$ soit plat \textup{(resp.}", RESP6)
add(12, "proof of (2.2.11), 'et tenant compte de (0_I, 6.6.2)'", "(0_I, 6.6.2) with a bold 0", r"$(0_{\mathrm I},6.6.2)$",
    "convention", 2, "high", r"$(0_{\mathrm I},6.6.2)$", r"$(\mathbf{0}_{\mathrm I},6.6.2)$")

# ---------------- page 13 ----------------
add(13, "page start: marker position (edit 1 of 2, insert)",
    "Printed p. 13 begins 'l'hypothèse entraîne que g^*(ℱ) est fidèlement plat relativement à f∘g, en vertu de (2.2.11, (iii)).' "
    "The line 'pour g : X'→X le morphisme canonique; il est clair que g est fidèlement plat, et' is the last line of printed p. 12 (page_012_s4.png).",
    r"\oldpage[IV-2]{13} stands before 'pour $g:X'\to X$ le morphisme canonique', one printed line too early",
    "marker", None, "high", "fidèlement⏎plat, et l'hypothèse", r"fidèlement⏎plat, et⏎\oldpage[IV-2]{13}⏎l'hypothèse",
    "Apply together with the next edit, which removes the misplaced marker.")
add(13, "page start: marker position (edit 2 of 2, remove the misplaced marker)", "see the previous finding",
    r"\oldpage[IV-2]{13} directly before 'pour $g:X'\to X$'", "marker", None, "high",
    r"\oldpage[IV-2]{13}⏎pour $g:X'\to X$", r"pour $g:X'\to X$",
    "Apply together with the previous edit. Afterwards 'pour g : X'→X ... fidèlement plat, et' belongs to the p. 12 segment; "
    "it matches the print there (no further change).")
for lab in ("i", "ii", "iii"):
    add(13, f"Corollaire (2.2.13), label ({lab})", f"label ({lab}) upright", f"\\item[({lab})] inside the italic statement (typeset italic)",
        "convention", 6, "high", f"\\item[({lab})]", f"\\item[\\textup{{({lab})}}]", LAB6)
add(13, "Corollaire (2.2.13) (iii), 'que g soit un morphisme plat (resp. fidèlement plat),'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    "morphisme plat (resp. fidèlement plat),", r"morphisme plat \textup{(resp.} fidèlement plat),", RESP6)
add(13, "Corollaire (2.2.13) (iii), 'que g∘f soit un morphisme plat (resp. fidèlement plat).'", "'(resp.' roman",
    "(resp. set in the italic environment", "convention", 6, "high",
    "morphisme plat (resp. fidèlement⏎plat).", r"morphisme plat \textup{(resp.} fidèlement⏎plat).", RESP6)
add(13, "proof of (2.2.14), 'donc A est noethérien (0_I, 6.5.2)'", "(0_I, 6.5.2) with a bold 0", r"$(0_{\mathrm I},6.5.2)$",
    "convention", 2, "high", r"$(0_{\mathrm I},6.5.2)$", r"$(\mathbf{0}_{\mathrm I},6.5.2)$")
add(13, "Proposition (2.2.15), 'l'application Z⇝f^{-1}(Z)'", "Z ⇝ f^{-1}(Z) (wavy arrow)", r"Z\mapsto f^{-1}(Z)",
    "symbol", None, "high", r"$Z\mapsto f^{-1}(Z)$", r"$Z\leadsto f^{-1}(Z)$", WAVY)
add(13, "proof of (2.2.15), l. 1, 'pour l'ensemble sous-jacent'", "'ensemble' in italics (enlarged crop)",
    "ensemble (roman)", "italics", None, "high", "pour l'ensemble sous-jacent", r"pour l'\emph{ensemble} sous-jacent")
add(13, "proof of (2.2.15), 'f^*(𝒥)𝒪_X de 𝒪_X (I, 4.4.5)'", "(I, 4.4.5) with a bold I", "(I, 4.4.5)",
    "convention", 2, "high", "(I, 4.4.5)", r"(\textbf{I}, 4.4.5)")
add(13, "proof of (2.2.15), 'Mais l'application 𝒥⇝f^*(𝒥)'", "𝒥 ⇝ f^*(𝒥) (wavy arrow)", r"\mathscr J\mapsto f^*(\mathscr J)",
    "symbol", None, "high", r"$\mathscr J\mapsto", r"$\mathscr J\leadsto", WAVY)
add(13, "Corollaire (2.2.16), 'l'application f⇝f_{(S')}'", "f ⇝ f_{(S')} (wavy arrow)", r"f\mapsto f_{(S')}",
    "symbol", None, "high", r"$f\mapsto f_{(S')}$", r"$f\leadsto f_{(S')}$", WAVY)
add(13, "proof of (2.2.16), '= (X×_S Y)_{(S')} (I, 3.3.10)'", "(I, 3.3.10) with a bold I", "(I, 3.3.10)",
    "convention", 2, "high", "(I, 3.3.10)", r"(\textbf{I}, 3.3.10)")
add(13, "proof of (2.2.16), 'ces S-morphismes (I, 5.3.11)'", "(I, 5.3.11) with a bold I", "(I, 5.3.11)",
    "convention", 2, "high", "(I, 5.3.11)", r"(\textbf{I}, 5.3.11)")
add(13, "proof of (2.2.16), 'Z_{f_(S')} = g^{-1}(Z_f) (I, 5.3.12)'", "(I, 5.3.12) with a bold I", "(I, 5.3.12)",
    "convention", 2, "high", "(I, 5.3.12)", r"(\textbf{I}, 5.3.12)")
add(13, "Proposition (2.2.17), 'sur un facteur direct du A-module B'",
    "'facteur direct' italic like the rest of the statement (no change of face; enlarged crop)",
    r"\emph{facteur direct} inside the italic proposition environment (typeset upright)",
    "convention", 6, "high", r"\emph{facteur⏎direct}", "facteur⏎direct",
    "Printed italic words left upright: drop the \\emph inside the italic environment (FIX_POLICY 2.6).")

# ---------------- page 14 ----------------
add(14, "heading 2.3", "'2.3. Propriétés topologiques des morphismes plats.' with a final full stop",
    r"\subsection{Propriétés topologiques des morphismes plats}", "punctuation", None, "high",
    r"\subsection{Propriétés topologiques des morphismes plats}", r"\subsection{Propriétés topologiques des morphismes plats.}",
    "GLOBAL_ISSUES 43/58 (subsection titles without the printed full stop); same form as the IV-1 page fixes.")
add(14, "after Lemme (2.3.1), 'C'est un cas particulier de (III, 1.4.15)'", "(III, 1.4.15) with a bold III", "(III, 1.4.15)",
    "convention", 2, "high", "(III, 1.4.15)", r"(\textbf{III}, 1.4.15)")
add(14, "Proposition (2.3.2), 'image fermée de X par f ((I, 9.5.3) et (1.7.8))'",
    "((I, 9.5.3) upright with a bold upright I; 'et' italic (enlarged crop)", "((I, 9.5.3) set in the italic environment, plain I",
    "convention", 2, "high", "((I, 9.5.3)", r"\textup{((\textbf{I}, 9.5.3)}",
    "One edit for the bold I (convention 2) and the upright reference (convention 6), as on IV-1 p. 249.")
add(14, "Proposition (2.3.2), 'et (1.7.8)),'", "(1.7.8)) upright", "(1.7.8)) set in the italic environment",
    "convention", 6, "high", "(1.7.8))", r"\textup{(1.7.8))}", REF6)
add(14, "Proposition (2.3.2), 'où g : X→Z est un morphisme (loc. cit.).'",
    "'loc. cit.' italic like the rest of the statement (no change of face; enlarged crop)",
    r"(\emph{loc. cit.}) inside the italic proposition environment (typeset upright)",
    "convention", 6, "high", r"(\emph{loc. cit.}). Soit", "(loc. cit.). Soit",
    "Printed italic words left upright: drop the \\emph inside the italic environment (FIX_POLICY 2.6).")
add(14, "proof of (2.3.2), 'au cas où S = Y (I, 3.3.11)'", "(I, 3.3.11) with a bold I", "(I, 3.3.11)",
    "convention", 2, "high", "(I, 3.3.11)", r"(\textbf{I}, 3.3.11)")
add(14, "proof of (2.3.2), 'θ : 𝒪_S → f_*(𝒪_X) (I, 9.5.2). Comme h'", "(I, 9.5.2) with a bold I", "(I, 9.5.2)",
    "convention", 2, "high", "(I, 9.5.2). Comme", r"(\textbf{I}, 9.5.2). Comme")
add(14, "proof of (2.3.2), 'et utilisant (I, 2.2.4))'", "(I, 2.2.4) with a bold I", "(I, 2.2.4)",
    "convention", 2, "high", "(I, 2.2.4)", r"(\textbf{I}, 2.2.4)")
add(14, "proof of (2.3.2), 'résulte donc de (2.3.1) et de (I, 9.5.2), puisque'", "(I, 9.5.2) with a bold I", "(I, 9.5.2)",
    "convention", 2, "high", "de (I, 9.5.2), puisque", r"de (\textbf{I}, 9.5.2), puisque")
add(14, "(2.3.3), 'qui soit f-plat'", "'f-plat' in italics (enlarged crop)", "$f$-plat (roman 'plat')",
    "italics", None, "high", "qui soit⏎$f$-plat et dont", r"qui soit⏎\emph{$f$-plat} et dont")
add(14, "(2.3.3), 'dont le support soit égal à X'", "'égal à' in italics (enlarged crop)", "égal à (roman)",
    "italics", None, "high", "soit égal à $X$", r"soit \emph{égal à} $X$")
add(14, "(2.3.3), 's'il est quasi-plat et surjectif.'", "'quasi-plat' and 'surjectif' in italics; 'et' roman (enlarged crop)",
    "quasi-plat et surjectif (roman)", "italics", None, "high",
    "s'il est quasi-plat et surjectif.", r"s'il est \emph{quasi-plat} et \emph{surjectif}.")
add(14, "after (2.3.3), 'Il résulte aussitôt de (2.1.4) et de (I, 9.1.13)'", "(I, 9.1.13) with a bold I", "(I, 9.1.13)",
    "convention", 2, "high", "(I, 9.1.13)", r"(\textbf{I}, 9.1.13)")
add(14, "after (2.3.3), '(compte tenu de (I, 3.5.2))'", "(I, 3.5.2) with a bold I", "(I, 3.5.2)",
    "convention", 2, "high", "(I, 3.5.2)", r"(\textbf{I}, 3.5.2)")
add(14, "Proposition (2.3.4), 'un morphisme quasi-plat (2.3.3).'", "(2.3.3) upright", "(2.3.3) set in the italic environment",
    "convention", 6, "high", "quasi-plat (2.3.3). Alors", r"quasi-plat \textup{(2.3.3)}. Alors", REF6)
add(14, "Proposition (2.3.4), '(qui sont équivalentes en vertu de (1.10.4))'", "(1.10.4) upright", "(1.10.4) set in the italic environment",
    "convention", 6, "high", "(1.10.4))~:", r"\textup{(1.10.4)})~:", REF6)
for lab in ("i", "ii"):
    add(14, f"Proposition (2.3.4), label ({lab})", f"label ({lab}) upright", f"\\item[({lab})] inside the italic statement (typeset italic)",
        "convention", 6, "high", f"\\item[({lab})]", f"\\item[\\textup{{({lab})}}]", LAB6)


def main():
    pages = {}
    for p in range(10, 15):
        pages[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    bad = 0
    # each old exactly once in the original page file
    for x in F:
        if x["fix"]:
            c = pages[x["page"]].count(x["fix"]["old"])
            if c != 1:
                bad += 1
                print("NOT UNIQUE in original", x["page"], c, repr(x["fix"]["old"]))
    # sequential application in list order, as apply_fixes.py does
    sim = dict(pages)
    for x in F:
        if x["fix"]:
            t = sim[x["page"]]
            c = t.count(x["fix"]["old"])
            if c != 1:
                bad += 1
                print("NOT UNIQUE in sequence", x["page"], c, repr(x["fix"]["old"]))
            else:
                sim[x["page"]] = t.replace(x["fix"]["old"], x["fix"]["new"])
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts = {}
    for x in F:
        k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
        counts.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
    print("findings", len(F), "problems", bad)
    for p in sorted(counts):
        c = counts[p]
        print(p, f"{c['normal']}/{c['convention']}/{c['misprint']}")


if __name__ == "__main__":
    main()
