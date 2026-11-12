"""Build findings_040_044.json for EGA IV-3 pp. 40-44 and check every fix's old string."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV3")
OUT = RUN / "findings_040_044.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if corrected is not None:
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def bold(page, where, numeral, old, new, note=""):
    add(page, where, f"bold {numeral}", old, "convention", 2, "high", old, new, note)


COMBINED = "One edit for this finding and the next (convention 6): bold numeral and the upright reference together."
COVERED = "Covered by the edit of the preceding finding (convention 2), which adds the \\textup."


def covered(page, where, ref):
    add(page, where, "the reference is upright inside the italic statement", ref + " set in the italic environment",
        "convention", 6, "high", None, None, COVERED)


# ---------------- page 40 ----------------
for n, letter in (("1", "p"), ("2", "g"), ("3", "j")):
    add(40, f"Proposition (8.10.5.1) (italic statement): '{n}° {letter} soit ...'",
        f"{n}° upright (old-style figure) inside the italic statement (enlarged crop)",
        f"{n}\\textsuperscript{{o}} in the italic proposition environment: italic", "convention", 6, "medium",
        f"{n}\\textsuperscript{{o}} ${letter}$", f"\\textup{{{n}\\textsuperscript{{o}}}} ${letter}$")
bold(40, "proof of (8.10.5.1): 'Le lemme de Chow (II, 5.6.1)'", "II", "(II, 5.6.1)", "(\\textbf{II}, 5.6.1)")
bold(40, "proof of (8.10.5.1): 'par changement de base (II, 5.5.5, (iii) et I, 3.5.2 et 4.3.2)'", "II",
     "(II, 5.5.5,", "(\\textbf{II}, 5.5.5,")
bold(40, "same reference: '... (iii) et I, 3.5.2 et 4.3.2)'", "I", "et I, 3.5.2", "et \\textbf{I}, 3.5.2")
add(40, "between the end of the proof of (8.10.5.1) and 'Cas (xii) : Appliquons ...'",
    "no heading: the proof of (8.10.5) simply continues with the paragraph 'Cas (xii) : ...'",
    "\\begin{proof}[Suite de la démonstration de (8.10.5)]; the IV-3 proof environment takes no optional "
    "argument, so the bracketed text is typeset after 'Démonstration. ---'", "extra", None, "high",
    "\\begin{proof}[Suite de la démonstration de (8.10.5)]", "\\begin{proof}",
    "Same fix as ega0-16 p. 34, ega0-19 p. 85 and ega0-22 p. 210; the remaining 'Démonstration. ---' is the "
    "document-wide proof-heading item.")
add(40, "'Cas (xii) : Appliquons au morphisme f_0'", "only 'Cas' italic; '(xii)' upright (enlarged crop)",
    "\\emph{Cas (xii)}", "italics", None, "high", "\\emph{Cas (xii)}", "\\emph{Cas} (xii)")
bold(40, "'Comme g est propre (II, 5.5.3), il en est de même'", "II", "(II, 5.5.3), il", "(\\textbf{II}, 5.5.3), il")
bold(40, "'p∘j = f∘g (II, 5.4.2)'", "II", "f\\circ g$ (II, 5.4.2)", "f\\circ g$ (\\textbf{II}, 5.4.2)")
add(40, "'j est propre, donc une immersion fermée; appliquant le cas (iv)'",
    "'immersion fermée' italic (enlarged crop)", "immersion fermée (roman)", "italics", None, "high",
    "donc une immersion fermée~;", "donc une \\emph{immersion fermée}~;")
bold(40, "'donc soit propre (II, 5.4.2). Mais alors'", "II", "(II, 5.4.2). Mais", "(\\textbf{II}, 5.4.2). Mais")
add(40, "'Mais alors f_λ∘g_λ = j_λ∘p_λ est propre'", "f_λ∘g_λ = j_λ∘p_λ",
    "$f_\\lambda\\circ g_\\lambda=j_\\lambda\\circ p_\\lambda$ (keeps the printed reading)",
    "misprint_in_print", None, "high", None, None,
    "j_λ: X'_λ→P_λ and p_λ: P_λ→S_λ, so only p_λ∘j_λ is defined (cf. p∘j = f∘g a few lines above). "
    "The TeX keeps the printed reading.",
    corrected="$f_\\lambda\\circ g_\\lambda=p_\\lambda\\circ j_\\lambda$")
bold(40, "'est propre (II, 5.5.3 et 5.4.2)'", "II", "(II, 5.5.3 et", "(\\textbf{II}, 5.5.3 et")
bold(40, "'il résulte de (II, 5.4.3) que f_λ est propre'", "II", "(II, 5.4.3)", "(\\textbf{II}, 5.4.3)")
add(40, "'Cas (xiii) et (xiv) : En vertu de (xii)'",
    "'Cas' and 'et' italic; '(xiii)' and '(xiv)' upright (enlarged crop)", "\\emph{Cas (xiii) et (xiv)}",
    "italics", None, "high", "\\emph{Cas (xiii) et (xiv)}", "\\emph{Cas} (xiii) \\emph{et} (xiv)")
bold(40, "'et de (II, 5.5.3) (qui est applicable'", "II", "(II, 5.5.3) (qui", "(\\textbf{II}, 5.5.3) (qui")

# ---------------- page 41 ----------------
add(41, "'en outre, en vertu de (8.5.5), on peut supposer'", "comma after (8.5.5)", "no comma", "punctuation",
    None, "high", "(8.5.5) on peut", "(8.5.5), on peut")
add(41, "'on peut supposer L_λ inversible. Le théorème'", "'inversible' italic (enlarged crop)", "roman",
    "italics", None, "high", "inversible. Le théorème", "\\emph{inversible}. Le théorème")
add(41, "'conséquence du lemme plus précis suivant :'", "ends with ' :'", "ends with a full stop", "punctuation",
    None, "high", "lemme plus précis suivant.", "lemme plus précis suivant~:")
add(41, "Lemme (8.10.5.2): 'ample pour f (resp. très ample pour f), il faut'",
    "'(resp.' and the closing parenthesis upright inside the italic statement", "set in the italic lemma environment",
    "convention", 6, "high", "(resp. très ample pour $f$)", "\\textup{(resp.} très ample pour $f$\\textup{)}")
add(41, "Lemme (8.10.5.2): 'soit ample pour f_μ (resp. très ample pour f_μ).'",
    "'(resp.' and the closing parenthesis upright inside the italic statement", "set in the italic lemma environment",
    "convention", 6, "high", "(resp. très ample pour $f_\\mu$)",
    "\\textup{(resp.} très ample pour $f_\\mu$\\textup{)}")
bold(41, "'évidemment suffisante (II, 4.4.10 et 4.6.13)'", "II", "(II, 4.4.10", "(\\textbf{II}, 4.4.10")
bold(41, "'très ample (II, 4.6.11)'", "II", "(II, 4.6.11)", "(\\textbf{II}, 4.6.11)")
bold(41, "'(vu (II, 4.4.5) et le fait que L est filtrant)'", "II", "(II, 4.4.5)", "(\\textbf{II}, 4.4.5)")
add(41, "'(et par suite S) est affine. Alors'", "'affine' italic (enlarged crop)", "roman", "italics", None, "high",
    "est affine. Alors", "est \\emph{affine}. Alors")
bold(41, "'en vertu de (II, 4.4.1, (ii) et II, 4.1.2)'", "II (first)", "(II, 4.4.1,", "(\\textbf{II}, 4.4.1,")
bold(41, "same reference: '... et II, 4.1.2)'", "II (second)", "et\nII, 4.1.2)", "et\n\\textbf{II}, 4.1.2)")
bold(41, "'de (ii) et de (II, 4.1.3)'", "II", "(II, 4.1.3)", "(\\textbf{II}, 4.1.3)")
bold(41, "'utilisant ensuite (II, 4.1.3.2) et (8.5.2.5)'", "II", "(II, 4.1.3.2)", "(\\textbf{II}, 4.1.3.2)")
bold(41, "'très ample pour f_ν (II, 4.4.2)'", "II", "$f_\\nu$ (II, 4.4.2)", "$f_\\nu$ (\\textbf{II}, 4.4.2)")
add(41, "heading 8.11: 'Application aux morphismes quasi-finis.'", "title ends with a full stop", "no full stop",
    "punctuation", None, "high", "\\subsection{Application aux morphismes quasi-finis}",
    "\\subsection{Application aux morphismes quasi-finis.}")
bold(41, "Remarque (8.11.3): 'théorème de Chevalley (III, 4.4.2)'", "III", "(III, 4.4.2)", "(\\textbf{III}, 4.4.2)")
add(41, "(8.11.4): 'toutes locales sur Y (1.6.1, 1.2.6, (II, 5.1.1), ...'",
    "(1.6.1, 1.2.6, : light old-style figures 1 (not a bold I), each followed by a full stop (enlarged crop)",
    "(I, 6.1, I, 2.6,", "number", None, "high", "(I, 6.1, I, 2.6,", "(1.6.1, 1.2.6,",
    "The TeX read the old-style 1 as the numeral I and the first full stop as a comma; the print refers to "
    "(1.6.1) and (1.2.6) of chapter IV.")
bold(41, "same list: '(II, 5.1.1)'", "II", "(II, 5.1.1)", "(\\textbf{II}, 5.1.1)")
bold(41, "same list: '(II, 5.4.1)'", "II", "(II, 5.4.1)", "(\\textbf{II}, 5.4.1)")
bold(41, "same list: '(II, 6.2.2)'", "II", "(II, 6.2.2)", "(\\textbf{II}, 6.2.2)")
add(41, "(8.11.4): 'un morphisme de type fini f_0 : X_0→Spec(A_0) tels que X s'identifie'",
    "'tels que' (plural: A_0 and f_0)", "'tel que'", "word", None, "high", "tel que $X$", "tels que $X$")
add(41, "(8.11.4): 'utilisant la méthode de (8.1.2, c))'", "'c)' italic", "roman c)", "italics", None, "high",
    "(8.1.2, c))", "(8.1.2, \\emph{c)})")
add(41, "(8.11.4): 'utilisant maintenant la méthode de (8.1.2, a))'", "'a)' italic", "roman a)", "italics", None,
    "high", "(8.1.2, a))", "(8.1.2, \\emph{a)})")

# ---------------- page 42 ----------------
add(42, "(8.11.4): 'fidèlement plat et quasi-compact (0_I, 7.3.5)'", "bold 0 with a roman subscript I",
    "(0\\textsubscript{I}, 7.3.5)", "convention", 2, "high", "(0\\textsubscript{I}, 7.3.5)",
    "(\\textbf{0}\\textsubscript{I}, 7.3.5)")
add(42, "(8.11.4): '(0_I, 7.3.5); appliquant (2.7.1, (i), (vii), (xiv), (xv) et (xvi))'",
    "'appliquant' (hyphenated appli-|quant at the line end)", "'quant à'", "word", None, "high",
    "quant à (2.7.1", "appliquant (2.7.1", "The TeX kept only the second half of the hyphenated word and added 'à'.")
bold(42, "(8.11.4): 'Il résulte alors de (II, 6.2.6)'", "II", "(II, 6.2.6)", "(\\textbf{II}, 6.2.6)")
bold(42, "'est propre sur Y (II, 5.4.10)'", "II", "(II, 5.4.10)", "(\\textbf{II}, 5.4.10)")
add(42, "'Plaçons-nous maintenant dans les hypothèses de (8.11.2) et, en nous bornant (comme ...'",
    "'en nous bornant'", "'en nous ramenant encore'", "word", None, "high", "en nous ramenant\nencore (comme",
    "en nous bornant\n(comme")
for where, old, new in (
        ("'donc dim(Y—{y}) < dim(Y)'", "\\dim(Y-\\{y\\})", "\\dim(Y\\setmin\\{y\\})"),
        ("'f(X'') ⊂ Y—{y}'", "\\subset Y-\\{y\\}", "\\subset Y\\setmin\\{y\\}"),
        ("'appliquant à Y—{y} et à X''", "à $Y-\\{y\\}$ et", "à $Y\\setmin\\{y\\}$ et"),
        ("'X'' est quasi-affine sur Y—{y};'", "sur\n$Y-\\{y\\}$~;", "sur\n$Y\\setmin\\{y\\}$~;"),
):
    add(42, where, "long dash Y—{y}", "minus sign Y-\\{y\\}", "convention", 7, "high", old, new)
add(42, "'mais l'ouvert Y—{y} étant quasi-affine sur Y'", "'mais l'ouvert Y—{y}'", "'mais $Y-\\{y\\}$' ('l'ouvert' missing)",
    "missing", None, "high", "mais $Y", "mais l'ouvert $Y",
    "Independent of the convention-7 edit of the same Y—{y} (that edit's old string starts at the minus sign).")
add(42, "same: 'Y—{y} étant quasi-affine sur Y'", "long dash Y—{y}", "minus sign Y-\\{y\\}", "convention", 7, "high",
    "-\\{y\\}$ étant", "\\setmin\\{y\\}$ étant")
bold(42, "'aussi quasi-affine sur Y (II, 5.1.10, (ii))'", "II", "(II, 5.1.10,", "(\\textbf{II}, 5.1.10,")
bold(42, "'X est quasi-affine sur Y (II, 4.6.17 et 5.1.2, c'))'", "II", "(II, 4.6.17", "(\\textbf{II}, 4.6.17")
add(42, "same reference: '5.1.2, c'))'", "'c')' italic, with its parenthesis (enlarged crop)", "roman c')",
    "italics", None, "high", "c'))", "\\emph{c')})")
add(42, "Proposition (8.11.5): 'Les propriétés suivantes sont équivalentes :'", "'Les propriétés suivantes'",
    "'Les conditions suivantes'", "word", None, "high", "Les conditions suivantes", "Les propriétés suivantes")
add(42, "(8.11.5) c): 'géométriquement réduit sur k(y)'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "réduit sur $k(y)$", "réduit sur $\\boldsymbol{k}(y)$")
add(42, "(8.11.5) c): '(c'est-à-dire vide ou k(y)-isomorphe à'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "$k(y)$-isomorphe", "$\\boldsymbol{k}(y)$-isomorphe")
add(42, "(8.11.5) c): '-isomorphe à Spec(k(y)))'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "\\operatorname{Spec}(k(y))$)", "\\operatorname{Spec}(\\boldsymbol{k}(y))$)")
bold(42, "proof of (8.11.5): 'notons (I, 3.3.12) que'", "I", "(I, 3.3.12)", "(\\textbf{I}, 3.3.12)")
add(42, "proof of (8.11.5): 'le morphisme f^{-1}(y)→Spec(k(y)) déduit de f'", "bold italic k", "$k(y)$", "convention",
    1, "high", "\\operatorname{Spec}(k(y))$ déduit", "\\operatorname{Spec}(\\boldsymbol{k}(y))$ déduit")
bold(42, "'A⊗_k A→A est bijectif (I, 5.3.8)'", "I", "(I, 5.3.8)", "(\\textbf{I}, 5.3.8)")
add(42, "'et les images de a⊗1 et de 1⊗a dans A'", "'et de 1⊗a'", "'et $1\\otimes a$' ('de' missing)", "missing", None,
    "high", "$a\\otimes1$ et $1\\otimes a$", "$a\\otimes1$ et de $1\\otimes a$")
bold(42, "'est surjectif (II, 1.4.10)'", "II", "(II, 1.4.10)", "(\\textbf{II}, 1.4.10)")

# ---------------- page 43 ----------------
bold(43, "'Spec(A_y/m_y A_y) (II, 1.5.5) est tel que'", "II", "(II, 1.5.5)", "(\\textbf{II}, 1.5.5)")
add(43, "'k(y) = O_y/m_y → A_y/m_y A_y soit bijectif'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "$k(y)=\\mathcal O_y", "$\\boldsymbol{k}(y)=\\mathcal O_y")
add(43, "Remarque (8.11.5.1): 'est vide ou k(y)-isomorphe'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "$k(y)$-isomorphe", "$\\boldsymbol{k}(y)$-isomorphe")
add(43, "Remarque (8.11.5.1): 'à Spec(k(y))'", "bold italic k", "$k(y)$", "convention", 1, "high",
    "\\operatorname{Spec}(k(y))", "\\operatorname{Spec}(\\boldsymbol{k}(y))")
add(43, "Proposition (8.11.6): '(la réciproque étant vraie d'après (2.4.5, (i)))'",
    "the whole parenthesis roman inside the italic statement (enlarged crop)", "set in the italic proposition environment",
    "convention", 6, "high", "(la réciproque étant vraie\nd'après (2.4.5, (i)))",
    "\\textup{(la réciproque étant vraie\nd'après (2.4.5, (i)))}")
bold(43, "proof of (8.11.6): 'est propre par définition (II, 5.4.1)'", "II", "(II, 5.4.1)", "(\\textbf{II}, 5.4.1)")
bold(43, "proof of (8.11.6): 'évidemment quasi-fini (II, 6.2.3)'", "II", "(II, 6.2.3)", "(\\textbf{II}, 6.2.3)")
add(43, "heading 8.12: '... du « Main Theorem » de Zariski.'", "title ends with a full stop", "no full stop",
    "punctuation", None, "high", "de Zariski}", "de Zariski.}")
add(43, "Lemme (8.12.1): 'de O_Y-Algèbres (II, 1.2.7). Supposons'", "bold II; the reference upright inside the italic statement",
    "(II, 1.2.7) in the italic lemma environment", "convention", 2, "high", "(II, 1.2.7)",
    "\\textup{(\\textbf{II}, 1.2.7)}", COMBINED)
covered(43, "Lemme (8.12.1): same reference '(II, 1.2.7)'", "(II, 1.2.7)")
add(43, "Lemme (8.12.1): 'de X par g (I, 9.5.3) soit égale à Z'", "bold I; the reference upright inside the italic statement",
    "(I, 9.5.3) in the italic lemma environment", "convention", 2, "high", "(I, 9.5.3)",
    "\\textup{(\\textbf{I}, 9.5.3)}", COMBINED)
covered(43, "Lemme (8.12.1): same reference '(I, 9.5.3)'", "(I, 9.5.3)")
bold(43, "proof of (8.12.1): 'est égale à Z signifie (I, 9.5.2)'", "I", "(I, 9.5.2)", "(\\textbf{I}, 9.5.2)")
bold(43, "'par définition de Z (II, 1.3.1)'", "II", "(II, 1.3.1)", "(\\textbf{II}, 1.3.1)")
bold(43, "'est injectif (I, 1.3.9)'", "I", "(I, 1.3.9)", "(\\textbf{I}, 1.3.9)")
bold(43, "'résulte de (I, 9.5.10) et de l'hypothèse'", "I", "(I, 9.5.10)", "(\\textbf{I}, 9.5.10)")
add(43, "Lemme (8.12.2): '(dont C est la réunion ((I, 9.6.6) et (1.7.9)))'",
    "bold I; the reference and its parentheses upright inside the italic statement ('et' italic)",
    "((I, 9.6.6) in the italic lemma environment", "convention", 2, "high", "((I, 9.6.6)",
    "\\textup{((\\textbf{I}, 9.6.6)}", COMBINED)
covered(43, "Lemme (8.12.2): same reference '((I, 9.6.6)'", "((I, 9.6.6)")
add(43, "Lemme (8.12.2): '... et (1.7.9))); posons'", "(1.7.9) and the closing parentheses upright inside the italic statement",
    "set in the italic lemma environment", "convention", 6, "high", "(1.7.9)))", "\\textup{(1.7.9)))}")

# ---------------- page 44 ----------------
add(44, "top of the page: 'De plus, lorsque g_λ est une immersion ...' (end of Lemme (8.12.2))",
    "new indented paragraph after item b)",
    "follows \\end{enumerate} (end of page 43) without a blank line, so it is set unindented as a continuation",
    "other", None, "medium", "\\oldpage[IV-3]{44}\nDe plus", "\\oldpage[IV-3]{44}\n\nDe plus",
    "Paragraph break as in the print; the marker stays where page 44 begins.")
add(44, "'Il suffit d'appliquer (II, 3.8.4) ... et tenant compte de (II, 3.1.7).' (proof of (8.12.2))",
    "roman, after the italic statement", "inside the lemma environment (before \\end{lemma}), so set italic",
    "italics", None, "high", "pour $\\mu\\geq\\lambda$.\n\nIl suffit",
    "pour $\\mu\\geq\\lambda$.\n\\end{lemma}\n\nIl suffit",
    "Apply together with the next edit, which removes the old \\end{lemma}.")
add(44, "end of the proof of (8.12.2), before Proposition (8.12.3)", "the proof is not part of the statement",
    "\\end{lemma} after the proof", "other", None, "high", "\\end{lemma}\n\n\\begin{proposition}[8.12.3]",
    "\\begin{proposition}[8.12.3]",
    "Apply together with the preceding edit; on its own it leaves the lemma environment unclosed.")
bold(44, "'Il suffit d'appliquer (II, 3.8.4)'", "II", "(II, 3.8.4)", "(\\textbf{II}, 3.8.4)")
add(44, "'S par C[T], et tenant compte de (II, 3.1.7)'", "'et tenant compte'", "'et en tenant compte' ('en' added)",
    "extra", None, "high", "et en tenant", "et tenant")
bold(44, "'compte de (II, 3.1.7).'", "II", "(II, 3.1.7)", "(\\textbf{II}, 3.1.7)")
add(44, "Proposition (8.12.3): 'Soit B = f_*(O_X), qui est une O_Y-Algèbre quasi-cohérente (I, 9.2.2);'",
    "bold I; the reference upright inside the italic statement", "(I, 9.2.2) in the italic proposition environment",
    "convention", 2, "high", "(I, 9.2.2)", "\\textup{(\\textbf{I}, 9.2.2)}", COMBINED)
covered(44, "Proposition (8.12.3): same reference '(I, 9.2.2)'", "(I, 9.2.2)")
add(44, "Proposition (8.12.3): 'fermeture intégrale ... quasi-cohérente (II, 6.3.4);'",
    "bold II; the reference upright inside the italic statement", "(II, 6.3.4) in the italic proposition environment",
    "convention", 2, "high", "(II, 6.3.4)", "\\textup{(\\textbf{II}, 6.3.4)}", COMBINED)
covered(44, "Proposition (8.12.3): same reference '(II, 6.3.4)'", "(II, 6.3.4)")
add(44, "Proposition (8.12.3): 'l'injection canonique φ : C→B = f_*(O_X) (II, 1.2.7). Soit'",
    "bold II; the reference upright inside the italic statement", "(II, 1.2.7) in the italic proposition environment",
    "convention", 2, "high", "(II, 1.2.7)", "\\textup{(\\textbf{II}, 1.2.7)}", COMBINED)
covered(44, "Proposition (8.12.3): same reference '(II, 1.2.7)'", "(II, 1.2.7)")
add(44, "Proposition (8.12.3): '(dont C est la réunion ((I, 9.6.6) et (1.7.9)))'",
    "bold I; the reference and its parentheses upright inside the italic statement ('et' italic)",
    "((I, 9.6.6) in the italic proposition environment", "convention", 2, "high", "((I, 9.6.6)",
    "\\textup{((\\textbf{I}, 9.6.6)}", COMBINED)
covered(44, "Proposition (8.12.3): same reference '((I, 9.6.6)'", "((I, 9.6.6)")
add(44, "Proposition (8.12.3): '... et (1.7.9))), et, pour tout λ'",
    "(1.7.9) and the closing parentheses upright inside the italic statement", "set in the italic proposition environment",
    "convention", 6, "high", "(1.7.9)))", "\\textup{(1.7.9)))}")
add(44, "Proposition (8.12.3): 'et, pour tout λ, soit g_λ : X→Z_λ = Spec(C_λ) le Y-morphisme correspondant'",
    "'soit g_λ : X→Z_λ = Spec(C_λ) le Y-morphisme'",
    "'posons $Z_\\lambda=\\operatorname{Spec}(\\mathcal C_\\lambda)$, et soit $g_\\lambda:X\\to Z_\\lambda$ le' (reworded)",
    "word", None, "high",
    "posons $Z_\\lambda=\\operatorname{Spec}(\\mathcal C_\\lambda)$, et\nsoit $g_\\lambda:X\\to Z_\\lambda$ le",
    "soit $g_\\lambda:X\\to Z_\\lambda=\\operatorname{Spec}(\\mathcal C_\\lambda)$ le")
add(44, "Proposition (8.12.3): '... C_λ→B = f_*(O_X). Alors les conditions suivantes sont équivalentes :'",
    "full stop, then 'Alors les conditions'", "'~; les conditions' ('Alors' missing, semicolon for the full stop)",
    "missing", None, "high", "f_*(\\mathcal O_X)$~; les conditions", "f_*(\\mathcal O_X)$. Alors les conditions")
add(44, "(8.12.3) a): display 'X →f' Y' →u Y'", "no punctuation after the display (enlarged crop)", "comma after Y",
    "punctuation", None, "high", "\\xrightarrow{u}Y,\n\\]", "\\xrightarrow{u}Y\n\\]")
add(44, "(8.12.3): 'De plus, lorsqu'il en est ainsi, g est une immersion ouverte'",
    "new indented paragraph after item c)", "directly after \\end{enumerate}: set unindented as a continuation",
    "other", None, "medium", "\\end{enumerate}\nDe plus, lorsqu'il", "\\end{enumerate}\n\nDe plus, lorsqu'il")
add(44, "'g(X) est dense dans Z, et de même pour g_λ'", "'et de même pour'", "'et il en est de même pour'", "extra",
    None, "high", "et il en est de même pour", "et de même pour")
add(44, "'résulte aussi de (8.12.1), appliqué en y remplaçant Z par Y''", "'appliqué en y remplaçant'",
    "'appliqué en remplaçant' ('y' missing)", "missing", None, "high", "appliqué en remplaçant",
    "appliqué en y remplaçant")
bold(44, "'et f'' est une immersion (I, 4.1.10)'", "I", "(I, 4.1.10)", "(\\textbf{I}, 4.1.10)")
bold(44, "'fini au-dessus de Y (II, 6.3.4 et 6.1.2)'", "II", "(II, 6.3.4 et", "(\\textbf{II}, 6.3.4 et")
add(44, "'elle s'identifie par définition de B à une des sous-O_Y-Algèbres C_λ'", "script B (enlarged crop)",
    "$\\mathcal B$ (keeps the printed reading)", "misprint_in_print", None, "medium", None, None,
    "The step needs the definition of C (integral closure of O_Y in B; the C_λ are its sub-O_Y-Algebras of finite "
    "type): the finite O_Y-Algebra B' ⊂ B is integral, hence lies in C, and is of finite type, hence is one of the "
    "C_λ. 'par définition de B' supplies nothing, so B is most likely a misprint for C. Not in the authors' errata "
    "(IV, liste 3). The TeX keeps the printed reading.",
    corrected="$\\mathcal C$")

# ---------------- checks ----------------
texts = {n: (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n") for n in range(40, 45)}
bad = 0
for f in F:
    if f["fix"] is None:
        continue
    c = texts[f["page"]].count(f["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", c, f["page"], repr(f["fix"]["old"]))
# overlapping old strings on one page
for n in range(40, 45):
    spans = []
    for f in F:
        if f["page"] == n and f["fix"] is not None:
            i = texts[n].find(f["fix"]["old"])
            spans.append((i, i + len(f["fix"]["old"]), f["fix"]["old"]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if a[1] > b[0]:
            bad += 1
            print("OVERLAP", n, repr(a[2]), repr(b[2]))
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt[(f["page"], k)] += 1
for n in range(40, 45):
    print(n, cnt[(n, "normal")], cnt[(n, "convention")], cnt[(n, "misprint")])
print("findings", len(F), "problems", bad)
