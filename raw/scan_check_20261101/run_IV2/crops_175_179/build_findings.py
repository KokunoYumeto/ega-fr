import json, re, sys
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_175_179.json"

def page_text(p):
    return (RUN / ("page_%03d.tex" % p)).read_text(encoding="utf-8").replace("\r\n", "\n")

F = []
def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, filepage=None, nofix=False):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if nofix else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_filepage"] = filepage if filepage is not None else page
    F.append(d)

BF = r"\boldsymbol{k}"
MOVED = "Old text is in page_178.tex until the p. 179 marker is moved (marker edit 1, page 178); apply after that move."

# ------------------------------------------------------------------ page 175
add(175, "page break 174/175: the p. 175 marker (edit 1 of 2, insert)",
    "printed p. 174 ends '... et soit C_α la fermeture'; printed p. 175 begins 'intégrale de A dans B_α. Il résulte aussitôt'",
    r"\oldpage[IV-2]{175} stands before 'II) Réduction au cas où ...', two printed lines (the last two of p. 174) too early",
    "marker", None, "high",
    "$C_\\alpha$ la fermeture\n", "$C_\\alpha$ la fermeture\n\\oldpage[IV-2]{175}\n",
    "Inserts the marker on its own line mid-sentence, no blank lines. Apply together with edit 2 (next entry), which removes the misplaced marker; both edits lie in page_175.tex.")
add(175, "page break 174/175: the p. 175 marker (edit 2 of 2, remove the misplaced marker)",
    "see the previous entry: 'II) Réduction au cas où B est une A-algèbre intègre ... et soit C_α la fermeture' is the end of p. 174",
    r"\oldpage[IV-2]{175} directly before 'II) \emph{Réduction'",
    "marker", None, "high",
    "\\oldpage[IV-2]{175}\nII) ", "II) ",
    "Apply together with, and after, edit 1. The blank line before the old marker (end of page_174.tex) remains, so 'II)' still opens a paragraph, as printed. The checker of p. 174 may report the same break.")
add(175, "proof of (6.14.4) I/II, 'Si l'on prouve que C'_α est la fermeture intégrale de A' dans B'_α il en résultera'",
    "no comma after B'_α (enlarged crop)", r"'$B'_\alpha$, il en résultera'",
    "misprint_in_print", None, "high",
    "$B'_\\alpha$, il en", "$B'_\\alpha$ il en",
    "The TeX silently corrects. The comma closing the 'Si ...' clause is expected (the parallel sentence on p. 174, '... dans B'_0, le lemme', has it).",
    corrected="$B'_\\alpha$, il en")
add(175, "'comme B est supposé réduit'", "réduit italic", "réduit upright", "italics", None, "high",
    "supposé réduit,", "supposé \\emph{réduit},",
    "The word looks heavier than the other italics on the page (possibly bold italic); \\emph proposed.")
add(175, "'il s'identifie à un sous-anneau du produit B_0'", "sous-anneau italic", "upright", "italics", None, "high",
    "un sous-anneau du produit", "un \\emph{sous-anneau} du produit")
add(175, "'C' = B' ∩ C'_0 (0_I, 6.1.3)'", "bold 0 with subscript I", r"plain 0$_{\mathrm I}$", "convention", 2, "high",
    "(0$_{\\mathrm I}$, 6.1.3)", "($\\mathbf{0}_{\\mathrm I}$, 6.1.3)")
add(175, "III): 'étant des extensions séparables de A (4.6.1)'", "séparables italic", "upright", "italics", None, "high",
    "extensions séparables de", "extensions \\emph{séparables} de")
add(175, "III): '(Bourbaki, Alg., chap. V, § 9, exerc. 2)'", "Alg. italic", "upright", "italics", None, "high",
    "(Bourbaki, Alg.,", "(Bourbaki, \\emph{Alg.},")
add(175, "III): 'a fortiori A', étant intégralement clos'", "a fortiori italic", "upright", "italics", None, "high",
    "2); a fortiori", "2); \\emph{a fortiori}")
add(175, "IV): 'et a fortiori dans B''", "a fortiori italic", "upright", "italics", None, "high",
    "a fortiori dans $B'$", "\\emph{a fortiori} dans $B'$")

# ------------------------------------------------------------------ page 176
add(176, "V): 'qui est une extension algébrique finie de K'", "finie italic", "upright", "italics", None, "high",
    "algébrique finie de $K$", "algébrique \\emph{finie} de $K$")
add(176, "V): 'si l'on pose C'_0 = C ⊗_A A''", "C'_0 = C⊗_A A' (no subscript 0 on the right-hand C; enlarged crop)",
    r"$C'_0=C_0\otimes_A A'$", "misprint_in_print", None, "high",
    "$C'_0=C_0\\otimes_A A'$", "$C'_0=C\\otimes_A A'$",
    "The TeX silently corrects. C'_0 is C_0 ⊗_A A' (as on p. 175); with C the statement C' = B' ∩ C'_0 would be empty.",
    corrected="$C'_0=C_0\\otimes_A A'$")
add(176, "V): 'C' = B' ∩ C'_0 par platitude (0_I, 6.1.3)'", "bold 0 with subscript I", r"plain 0$_{\mathrm I}$", "convention", 2, "high",
    "(0$_{\\mathrm I}$, 6.1.3)", "($\\mathbf{0}_{\\mathrm I}$, 6.1.3)")
add(176, "proof of (6.14.5): 'et posons B'_λ = B'_λ ⊗_A A''", "B'_λ = B'_λ⊗_A A' (prime on the right-hand B_λ; enlarged crop)",
    r"$B'_\lambda=B_\lambda\otimes_A A'$", "misprint_in_print", None, "high",
    "$B'_\\lambda=B_\\lambda\\otimes_A A'$", "$B'_\\lambda=B'_\\lambda\\otimes_A A'$",
    "The TeX silently corrects; B'_λ is defined as B_λ ⊗_A A'.",
    corrected="$B'_\\lambda=B_\\lambda\\otimes_A A'$")
add(176, "after (6.14.5): 'lorsque A est un anneau local excellent'", "local excellent italic (anneau roman)", "upright", "italics", None, "high",
    "anneau local\nexcellent", "anneau \\emph{local\nexcellent}")
add(176, "heading 6.15", "'6.15. Préschémas géométriquement unibranches.' with a final full stop", "no full stop",
    "punctuation", None, "high",
    "\\subsection{Préschémas géométriquement unibranches}", "\\subsection{Préschémas géométriquement unibranches.}",
    "GLOBAL_ISSUES 43/58 (subsection titles lack the printed full stop); same fix as IV-2 pp. 5, 150, 153.")
add(176, "(6.15.1): 'ou que le point x est unibranche (resp. géométriquement unibranche) dans X'",
    "unibranche and géométriquement unibranche italic", "upright", "italics", None, "high",
    "est unibranche (resp. géométriquement unibranche) dans $X$",
    "est \\emph{unibranche} (resp. \\emph{géométriquement unibranche}) dans $X$")
add(176, "(6.15.1): 'si l'anneau local O_{X,x} est unibranche (resp. géométriquement unibranche)'",
    "unibranche and géométriquement unibranche italic", "upright", "italics", None, "high",
    "$\\mathcal O_{X,x}$ est unibranche (resp. géométriquement\nunibranche)",
    "$\\mathcal O_{X,x}$ est \\emph{unibranche} (resp. \\emph{géométriquement\nunibranche})")
add(176, "(6.15.1): '(0, 23.2.1)'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 23.2.1)", "(\\textbf{0}, 23.2.1)")
add(176, "(6.15.1): 'nous dirons que X est unibranche (resp. géométriquement unibranche) s'il l'est'",
    "unibranche and géométriquement unibranche italic", "upright", "italics", None, "high",
    "que $X$ est unibranche (resp.\ngéométriquement unibranche) s'il",
    "que $X$ est \\emph{unibranche} (resp.\n\\emph{géométriquement unibranche}) s'il",
    "The following sentence 'Il suit de cette définition que, pour que X soit unibranche (resp. géométriquement unibranche)' is roman, as in the TeX.")
add(176, "(6.15.2): 'un anneau local A peut être unibranche'", "anneau local italic", "upright", "italics", None, "high",
    "un anneau local\n$A$", "un \\emph{anneau local}\n$A$")
add(176, "(6.15.2): 'sans que Spec(A) le soit'", "sans que and le soit italic", "upright", "italics", None, "high",
    "sans que\n$\\operatorname{Spec}(A)$ le soit", "\\emph{sans que}\n$\\operatorname{Spec}(A)$ \\emph{le soit}")
add(176, "(6.15.2): 'n'est pas stable par générisation'", "italic", "upright", "italics", None, "high",
    "n'est pas stable par\ngénérisation", "\\emph{n'est pas stable par\ngénérisation}")

# ------------------------------------------------------------------ page 177
add(177, "example after (6.15.2): 'B l'anneau intègre K[U, V, W]/(U²(U—W)—V²(U+W)) (U, V, W indéterminées)' (edit 1 of 2)",
    "formula in the running text", "displayed with \\[ \\]", "formula", None, "high",
    "intègre\n\\[\nK[U,V,W]", "intègre $K[U,V,W]",
    "Apply together with edit 2 (next entry). The two edits leave the formula itself to the convention-7 entries below; no overlap.")
add(177, "same formula (edit 2 of 2)", "formula in the running text", "displayed", "formula", None, "high",
    "(U+W))\n\\]\n", "(U+W))$\n",
    "Apply together with edit 1. Result: 'l'anneau\\nintègre $K[U,V,W]/(U^2(U-W)-V^2(U+W))$\\n($U$, $V$, $W$ indéterminées)'.")
add(177, "same formula: 'U²(U—W)'", "long dash (bar 40 px; = bars 35 px)", "minus sign", "convention", 7, "high",
    "U^2(U-W)", "U^2(U\\setmin W)", "Long dash for subtraction (GLOBAL_ISSUES 23).")
add(177, "same formula: ')—V²('", "long dash (bar 40 px)", "minus sign", "convention", 7, "high",
    "W)-V^2", "W)\\setmin V^2")
add(177, "'montrons que C = B[t] est la clôture intégrale de B'", "clôture intégrale italic", "upright", "italics", None, "high",
    "clôture intégrale de $B$. On a", "\\emph{clôture intégrale} de $B$. On a",
    "The later 'C est la clôture intégrale de B' and 'A' = C_n0 est la clôture intégrale de A' are roman, as in the TeX.")
add(177, "'t² = u²—w²'", "long dash (bar 41 px; = bars 34 px)", "minus sign", "convention", 7, "high",
    "u^2-w^2", "u^2\\setmin w^2")
add(177, "'K[T, U, W]/(T²—U²+W²)'", "long dash (bar 40 px)", "minus sign", "convention", 7, "high",
    "T^2-U^2", "T^2\\setmin U^2")
add(177, "'(Bourbaki, Alg. comm., chap. V, § 1, nº 6, prop. 18)'", "Alg. comm. italic", "upright", "italics", None, "high",
    "(Bourbaki, Alg. comm.,", "(Bourbaki, \\emph{Alg. comm.},")
add(177, "same reference: 'nº 6'", "upright superior letter o (enlarged crop)", r"n$^o$ (math-italic o)", "font", None, "medium",
    "n$^o$ 6", "n\\textsuperscript{o} 6",
    "The edition writes n\\textsuperscript{o} (GLOBAL_ISSUES 57); ega4-2-fr.tex has n$^o$ 8 times (here and p. 179 among them).")
add(177, "'t est racine de l'équation t(t—v)—w²(2v—t) = 0': first dash", "long dash (bar 41 px; = bars 34-35 px)", "minus sign",
    "convention", 7, "high", "$t(t-v)", "$t(t\\setmin v)")
add(177, "same equation: second dash ')—w²('", "long dash (bar 40 px)", "minus sign", "convention", 7, "high",
    "v)-w^2", "v)\\setmin w^2")
add(177, "same equation: '(2v—t)'", "long dash (bar 41 px)", "minus sign", "convention", 7, "high",
    "2v-t", "2v\\setmin t")
add(177, "'K[t, v, w, 1/(t—v)] = K[...]'", "long dash (bar 41 px)", "minus sign", "convention", 7, "high",
    "1/(t-v)]=", "1/(t\\setmin v)]=")
add(177, "same line: 'K[t, tu/(u+w), w, (u+w)/tw]'", "built-up fractions tu over u+w and u+w over tw, at text size (fraction bars 102-105 px)",
    "solidus fractions tu/(u+w), (u+w)/(tw)", "formula", None, "high",
    "tu/(u+w),w,(u+w)/(tw)", "\\frac{tu}{u+w},w,\\frac{u+w}{tw}",
    "The print's fractions are full text size (\\dfrac would match exactly; the file uses \\frac only). The left side 1/(t—v) keeps the solidus.")
add(177, "'on prouve aisément que C = K[t, u, v, w] = ... ∩ K[t, v, w, 1/(t—v)], ce qui achève' (edit 1 of 2)",
    "formula in the running text", "displayed with \\[ \\]", "formula", None, "high",
    "aisément\nque\n\\[\nC=", "aisément\nque $C=",
    "Apply together with edit 2 (next entry).")
add(177, "same formula (edit 2 of 2)", "formula in the running text, comma after it", "displayed", "formula", None, "high",
    "],\n\\]\nce qui", "]$,\nce qui",
    "Apply together with edit 1. The convention-7 entry for this formula's dash uses '\\cap K[t,v,w,1/(t-v' and does not overlap.")
add(177, "same formula: '∩ K[t, v, w, 1/(t—v)]'", "long dash (bar 40 px; = bars 34-35 px)", "minus sign", "convention", 7, "high",
    "\\cap K[t,v,w,1/(t-v", "\\cap K[t,v,w,1/(t\\setmin v")
add(177, "'engendré par u, v, w (« sommet du cône ») il existe un seul idéal maximal'",
    "no comma after the closing parenthesis (enlarged crop)", "'(« sommet du cône »), il existe'",
    "misprint_in_print", None, "high",
    "»), il existe", "») il existe",
    "The TeX silently corrects. The comma closing the 'si m_0 est ...' clause is expected.",
    corrected="»), il existe")
add(177, "'le morphisme canonique X' → X soit fini'", "fini italic", "upright", "italics", None, "high",
    "soit fini (ce qui", "soit \\emph{fini} (ce qui")
add(177, "'les anneaux de ses ouverts affines soient universellement japonais'", "italic", "upright", "italics", None, "high",
    "universellement japonais", "\\emph{universellement japonais}")
add(177, "'universellement japonais (0, 23.1.1)'", "bold 0", "plain 0", "convention", 2, "high",
    "(0, 23.1.1)", "(\\textbf{0}, 23.1.1)")
add(177, "'est localement constructible.'", "localement constructible italic", "upright", "italics", None, "high",
    "est localement constructible.", "est \\emph{localement constructible}.")
add(177, "(6.15.3): 'et si k(x) est une extension radicielle'", "bold italic k", "plain k", "convention", 1, "high",
    "si $k(x)$ est une", "si $" + BF + "(x)$ est une")
add(177, "(6.15.3): 'extension radicielle de k(y).'", "bold italic k", "plain k", "convention", 1, "high",
    "radicielle de $k(y)$. Il", "radicielle de $" + BF + "(y)$. Il")
add(177, "(6.15.3): 'que f est radiciel (I, 3.5.8)'", "bold I", "plain I", "convention", 2, "high",
    "(I, 3.5.8)", "(\\textbf{I}, 3.5.8)")
add(177, "(6.15.3): 'g : f^{-1}(y) → Spec(k(y))'", "bold italic k", "plain k", "convention", 1, "high",
    "Spec}(k(y))$ est le", "Spec}(" + BF + "(y))$ est le")
add(177, "(6.15.3): 'changement de base Spec(k(y)) → Y'", "bold italic k", "plain k", "convention", 1, "high",
    "Spec}(k(y))\\to Y$", "Spec}(" + BF + "(y))\\to Y$")
add(177, "(6.15.3): 'ou que g est radiciel.'", "radiciel italic", "upright", "italics", None, "high",
    "ou que $g$ est radiciel.", "ou que $g$ est \\emph{radiciel}.")
add(177, "Lemme (6.15.3.1), label (i)", "(i) upright", "\\item[(i)] (italic in the statement)", "convention", 6, "high",
    "\\item[(i)] Soient", "\\item[\\textup{(i)}] Soient", "GLOBAL_ISSUES 16.")
add(177, "Lemme (6.15.3.1), label (ii)", "(ii) upright", "\\item[(ii)] (italic)", "convention", 6, "high",
    "\\item[(ii)] Soient", "\\item[\\textup{(ii)}] Soient", "GLOBAL_ISSUES 16.")

# ------------------------------------------------------------------ page 178
k1 = [
    ("proof of (6.15.3.1) (i): 'en outre k(x) est extension radicielle'", "outre $k(x)$", "outre $" + BF + "(x)$"),
    ("same: 'extension radicielle de k(y)'", "radicielle de $k(y)$ et", "radicielle de $" + BF + "(y)$ et"),
    ("same: 'et k(y) extension radicielle'", "et $k(y)$ extension", "et $" + BF + "(y)$ extension"),
    ("same: 'radicielle de k(z), donc'", "radicielle de $k(z)$, donc", "radicielle de $" + BF + "(z)$, donc"),
    ("same: 'donc k(x) est extension radicielle'", "donc $k(x)$ est extension", "donc $" + BF + "(x)$ est extension"),
    ("same: 'extension radicielle de k(z).'", "de $k(z)$.\nInversement", "de $" + BF + "(z)$.\nInversement"),
    ("same: 'k(z) ⊂ k(y) ⊂ k(x)', first k", "on a $k(z)\\subset", "on a $" + BF + "(z)\\subset"),
    ("same: 'k(z) ⊂ k(y) ⊂ k(x)', second k", "\\subset k(y)\\subset", "\\subset " + BF + "(y)\\subset"),
    ("same: 'k(z) ⊂ k(y) ⊂ k(x)', third k", "\\subset k(x)$, et", "\\subset " + BF + "(x)$, et"),
    ("same: 'et k(x) est radiciel sur k(z)', first k", "et $k(x)$ est radiciel sur", "et $" + BF + "(x)$ est radiciel sur"),
    ("same: 'radiciel sur k(z), donc'", "sur\n$k(z)$, donc", "sur\n$" + BF + "(z)$, donc"),
    ("same: 'donc k(y) est radiciel'", "donc $k(y)$ est radiciel", "donc $" + BF + "(y)$ est radiciel"),
    ("same: 'radiciel sur k(z) et'", "sur $k(z)$ et", "sur $" + BF + "(z)$ et"),
    ("same: 'et k(x) radiciel sur k(y)', first k", "et $k(x)$ radiciel", "et $" + BF + "(x)$ radiciel"),
    ("same: 'radiciel sur k(y).'", "radiciel sur $k(y)$.", "radiciel sur $" + BF + "(y)$."),
    ("proof (ii): 'g : f^{-1}(y) → Spec(k(y))'", "Spec}(k(y))$,\n", "Spec}(" + BF + "(y))$,\n"),
    ("proof (ii): 'g' : f'^{-1}(y') → Spec(k(y'))'", "Spec}(k(y'))$ les", "Spec}(" + BF + "(y'))$ les"),
]
for where, old, new in k1:
    add(178, where, "bold italic k", "plain k", "convention", 1, "high", old, new)
add(178, "proof (ii): 'f'^{-1}(y') = f^{-1}(y) ⊗_{k(y)} k(y')', subscript", "bold k at subscript size (upright, enlarged crop)",
    "plain k", "convention", 1, "high", "\\otimes_{k(y)}", "\\otimes_{\\mathbf{k}(y)}",
    "Bold upright k in subscripts (GLOBAL_ISSUES 48).")
add(178, "same formula: 'k(y')' after the tensor sign", "bold italic k", "plain k", "convention", 1, "high",
    "}k(y')$", "}" + BF + "(y')$")
add(178, "proof (ii): '(I, 3.6.4)'", "bold I", "plain I", "convention", 2, "high",
    "(I, 3.6.4)", "(\\textbf{I}, 3.6.4)")
add(178, "'Soit alors X un préschéma réduit'", "réduit italic", "upright", "italics", None, "high",
    "préschéma réduit n'ayant", "préschéma \\emph{réduit} n'ayant")
add(178, "'n'ayant qu'un nombre fini de composantes irréductibles'", "fini italic", "upright", "italics", None, "high",
    "nombre fini de\ncomposantes", "nombre \\emph{fini} de\ncomposantes")
add(178, "'et soit X' son normalisé'", "normalisé italic", "upright", "italics", None, "high",
    "son normalisé", "son \\emph{normalisé}")
add(178, "'son normalisé (II, 6.3.8)'", "bold II", "plain II", "convention", 2, "high",
    "(II, 6.3.8)", "(\\textbf{II}, 6.3.8)")
add(178, "'on sait (loc. cit.) que'", "(loc. cit.) italic, parentheses included", "upright", "italics", None, "high",
    "(loc. cit.)", "\\emph{(loc. cit.)}")
add(178, "'il faut et il suffit que f soit radiciel en ce point'", "radiciel en ce point italic", "upright", "italics", None, "high",
    "radiciel en ce\npoint", "\\emph{radiciel en ce\npoint}")
add(178, "'il faut et il suffit donc que f soit radiciel.'", "radiciel italic", "upright", "italics", None, "high",
    "donc que $f$ soit radiciel.", "donc que $f$ soit \\emph{radiciel}.")
add(178, "(6.15.4): 'Généralisant la définition donnée dans (I, 2.2.9)'", "bold I", "plain I", "convention", 2, "high",
    "dans (I, 2.2.9)", "dans (\\textbf{I}, 2.2.9)")
add(178, "(6.15.4): 'pour deux préschémas réduits X, Y'", "réduits italic", "upright", "italics", None, "high",
    "préschémas réduits", "préschémas \\emph{réduits}")
add(178, "(6.15.4): 'est une bijection de cet ensemble'", "bijection italic", "upright", "italics", None, "high",
    "une bijection de", "une \\emph{bijection} de")
add(178, "(6.15.4): 'le morphisme X ×_Y Spec(O_y) → Spec(O_y) déduit de f'",
    "Spec(𝒪_y) twice (script O, subscript y; enlarged crop)", r"\operatorname{Spec}(k(y)) twice", "formula", None, "high",
    "$X\\times_Y\\operatorname{Spec}(k(y))\\to\\operatorname{Spec}(k(y))$",
    "$X\\times_Y\\operatorname{Spec}(\\mathcal O_y)\\to\\operatorname{Spec}(\\mathcal O_y)$",
    "Not a misprint: for a maximal point y of a reduced Y, O_y is the field k(y). The TeX replaced the printed O_y.")
add(178, "(6.15.4): 'l'homomorphisme k(y) → k(x)', first k", "bold italic k", "plain k", "convention", 1, "high",
    "$k(y)\\to", "$" + BF + "(y)\\to")
add(178, "(6.15.4): 'l'homomorphisme k(y) → k(x)', second k", "bold italic k", "plain k", "convention", 1, "high",
    "\\to k(x)$ déduit", "\\to " + BF + "(x)$ déduit")
add(178, "(6.15.4): 'se réduit à celle de (I, 2.2.9)'", "bold I", "plain I", "convention", 2, "high",
    "de (I, 2.2.9)", "de (\\textbf{I}, 2.2.9)")
add(178, "(6.15.4): 'n'ont qu'un nombre fini de composantes irréductibles'", "fini italic", "upright", "italics", None, "high",
    "nombre fini de composantes\nirréductibles", "nombre \\emph{fini} de composantes\nirréductibles")
add(178, "proof of (6.15.4.1): 'tel que k(x) = k(y)', first k", "bold italic k", "plain k", "convention", 1, "high",
    "$k(x)=", "$" + BF + "(x)=")
add(178, "same: 'k(x) = k(y)', second k", "bold italic k", "plain k", "convention", 1, "high",
    "=k(y)$. Il", "=" + BF + "(y)$. Il")
add(178, "same: 'Il résulte donc de (I, 3.4.9)'", "bold I", "plain I", "convention", 2, "high",
    "(I, 3.4.9)", "(\\textbf{I}, 3.4.9)")
add(178, "same: 'et que k(x') = k(y')', first k", "bold italic k", "plain k", "convention", 1, "high",
    "$k(x')=", "$" + BF + "(x')=")
add(178, "same: 'k(x') = k(y')', second k", "bold italic k", "plain k", "convention", 1, "high",
    "=k(y')$. On", "=" + BF + "(y')$. On")
add(178, "Proposition (6.15.5): 'soit entier et birationnel (6.15.4), donc surjectif'", "(6.15.4) upright",
    "italic in the statement", "convention", 6, "high",
    "birationnel (6.15.4)", "birationnel \\textup{(6.15.4)}")
add(178, "Proposition (6.15.5), label (i)", "(i) upright", "\\item[(i)] (italic)", "convention", 6, "high",
    "\\item[(i)] Pour", "\\item[\\textup{(i)}] Pour", "GLOBAL_ISSUES 16.")
add(178, "Proposition (6.15.5), label (ii)", "(ii) upright", "\\item[(ii)] (italic)", "convention", 6, "high",
    "\\item[(ii)] Pour", "\\item[\\textup{(ii)}] Pour", "GLOBAL_ISSUES 16.")
add(178, "proof of (6.15.5): 'se borner au cas où X et Y sont réduits'", "réduits italic", "upright", "italics", None, "high",
    "sont réduits", "sont \\emph{réduits}")
add(178, "same: 'sont réduits; le fait que f soit surjectif'", "semicolon after réduits (enlarged crop)", "comma",
    "punctuation", None, "high",
    ", le fait\nque $f$", "; le fait\nque $f$",
    "Does not overlap the italics fix on 'sont réduits'.")
add(178, "same: 'le fait que f soit surjectif résulte'", "surjectif italic", "upright", "italics", None, "high",
    "soit surjectif résulte", "soit \\emph{surjectif} résulte")
add(178, "same: 'un morphisme fermé (II, 6.1.10)'", "bold II", "plain II", "convention", 2, "high",
    "(II,\n6.1.10)", "(\\textbf{II},\n6.1.10)")
add(178, "same: 'Utilisant (I, 3.6.5)'", "bold I", "plain I", "convention", 2, "high",
    "(I, 3.6.5)", "(\\textbf{I}, 3.6.5)")
add(178, "same: 'et (II, 6.1.5)'", "bold II", "plain II", "convention", 2, "high",
    "(II, 6.1.5)", "(\\textbf{II}, 6.1.5)")
add(178, "page break 178/179: the p. 179 marker (edit 1 of 2, insert)",
    "printed p. 178 ends '... on peut supposer, pour prouver (i), que Y = Spec(O_{Y,y}),'; printed p. 179 begins 'autrement dit Y = Spec(A), où A est local.'",
    r"\oldpage[IV-2]{179} stands after the end of the proof of (6.15.5), before Proposition (6.15.6): the first eleven printed lines of p. 179 sit in the p. 178 segment",
    "marker", None, "high",
    ", autrement dit\n$Y=", ",\n\\oldpage[IV-2]{179}\nautrement dit\n$Y=",
    "The old text lies in the p. 178 segment, hence page 178. Apply after the other p. 178 entries, together with edit 2 (page 179), and before the seven p. 179 entries marked as moved text, whose old text enters the p. 179 segment with this edit.")

# ------------------------------------------------------------------ page 179
add(179, "page break 178/179: the p. 179 marker (edit 2 of 2, remove the misplaced marker)",
    "see the last page-178 entry", r"\oldpage[IV-2]{179} directly before \begin{proposition}[6.15.6]",
    "marker", None, "high",
    "\\oldpage[IV-2]{179}\n\\begin{proposition}", "\\begin{proposition}",
    "Apply together with, and after, edit 1 (page 178). The blank line after \\end{proof} remains.")
mv = [
    ("p. 179, l. 1 (text now before the p. 179 marker): 'où A est local.'", "local italic", "italics", None,
     "où $A$ est local. Comme", "où $A$ est \\emph{local}. Comme"),
    ("p. 179, l. 2 (moved text): 'il est intègre, donc'", "intègre italic", "italics", None,
     "il est intègre, donc", "il est \\emph{intègre}, donc"),
    ("p. 179, l. 5 (moved text): 'B est un anneau local,'", "local italic", "italics", None,
     "anneau local, et dire", "anneau \\emph{local}, et dire"),
    ("p. 179, l. 7 (moved text): 'donc intègre.'", "intègre italic", "italics", None,
     "donc intègre. Comme", "donc \\emph{intègre}. Comme"),
    ("p. 179, l. 8 (moved text): 'A ⊂ B (I, 1.2.7)'", "bold I", "convention", 2,
     "(I,\n1.2.7)", "(\\textbf{I},\n1.2.7)"),
    ("p. 179, l. 8 (moved text): 'donc A est aussi intègre.'", "intègre italic", "italics", None,
     "aussi intègre. Ainsi", "aussi \\emph{intègre}. Ainsi"),
    ("p. 179, l. 11 (moved text): 'même clôture intégrale C'", "clôture intégrale italic", "italics", None,
     "même clôture intégrale $C$", "même \\emph{clôture intégrale} $C$"),
]
for where, scan, kind, conv, old, new in mv:
    add(179, where, scan, "plain I" if conv == 2 else "upright", kind if conv is None else "convention", conv, "high",
        old, new, MOVED, filepage=178)
add(179, "proof of (6.15.6): 'au cas où l'extension k' de k est radicielle.'", "radicielle italic", "upright", "italics", None, "high",
    "est radicielle.", "est \\emph{radicielle}.")
add(179, "same: 'En outre (I, 3.6.5)'", "bold I", "plain I", "convention", 2, "high",
    "outre (I, 3.6.5)", "outre (\\textbf{I}, 3.6.5)")
add(179, "same: 'un anneau local intègre et intégralement clos'", "local intègre et intégralement clos italic (anneau roman)",
    "upright", "italics", None, "high",
    "anneau local intègre\net intégralement clos", "anneau \\emph{local intègre\net intégralement clos}")
add(179, "same: '(Bourbaki, Alg. comm., chap. V, § 2, nº 3, lemme 3)'", "Alg. comm. italic", "upright", "italics", None, "high",
    "(Bourbaki, Alg. comm.,", "(Bourbaki, \\emph{Alg. comm.},")
add(179, "same reference: 'nº 3'", "upright superior letter o", r"n$^o$ (math-italic o)", "font", None, "medium",
    "n$^o$ 3", "n\\textsuperscript{o} 3", "As on p. 177 (GLOBAL_ISSUES 57).")
add(179, "same: 'et a fortiori de celui de A'_0'", "a fortiori italic", "upright", "italics", None, "high",
    "et a fortiori de", "et \\emph{a fortiori} de")
add(179, "Proposition (6.15.7): 'X' = X ⊗_A k''", "X⊗_A k' (subscript capital A, same glyph as the ⊗_A subscripts of pp. 175-176; enlarged crop)",
    r"$X'=X\otimes_k k'$", "misprint_in_print", None, "high",
    "X\\otimes_k k'$. Soient", "X\\otimes_A k'$. Soient",
    "The TeX silently corrects. X is a k-préschéma and k' an extension of k (cf. (6.15.6), printed X⊗_k k').",
    corrected="X\\otimes_k k'$. Soient")
add(179, "proof of (6.15.7): 'en vertu de (I, 5.1.8)'", "bold I", "plain I", "convention", 2, "high",
    "(I, 5.1.8)", "(\\textbf{I}, 5.1.8)")
add(179, "same: 'et en vertu de (I, 3.6.5), au cas'", "bold I", "plain I", "convention", 2, "high",
    "de (I, 3.6.5), au cas", "de (\\textbf{I}, 3.6.5), au cas")

# ------------------------------------------------------------------ checks
texts = {p: page_text(p) for p in range(174, 181)}
problems = []
# 1. literal check per page file (moved-text entries checked against their file page)
for i, d in enumerate(F):
    if not d["fix"]:
        continue
    old = d["fix"]["old"]
    n = texts[d["_filepage"]].count(old)
    if n != 1:
        problems.append((i, d["page"], d["_filepage"], n, old))
    if d["_filepage"] != d["page"] and texts[d["page"]].count(old) != 0:
        problems.append((i, "also in page file", d["page"], old))
# 2. simulate sequential application in listed order, segment by segment
doc = texts[174][texts[174].index("\\oldpage"):]  # keep p.174 segment for context
for p in range(175, 181):
    doc += texts[p][texts[p].index("\\oldpage"):]
def segment(doc, p):
    a = doc.index("\\oldpage[IV-2]{%d}" % p)
    b = doc.find("\\oldpage[IV-2]{%d}" % (p + 1), a)
    return a, (b if b >= 0 else len(doc))
for i, d in enumerate(F):
    if not d["fix"]:
        continue
    old, new = d["fix"]["old"], d["fix"]["new"]
    a, b = segment(doc, d["page"])
    seg = doc[a:b]
    n = seg.count(old)
    if n != 1:
        problems.append(("SIM", i, d["page"], n, old))
        continue
    j = a + seg.index(old)
    doc = doc[:j] + new + doc[j + len(old):]
# 3. counts
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in range(175, 180):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F))
print("PROBLEMS:", problems if problems else "none")
if "--write" in sys.argv and not problems:
    out = [{k: v for k, v in d.items() if not k.startswith("_")} for d in F]
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (RUN / "crops_175_179" / "simulated_after_fixes.tex").write_text(doc, encoding="utf-8")
    print("written", OUT)
