"""Build findings_105_109.json; '¶' in old/new stands for a line break (LF)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_105_109.json"


def L(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
    x = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": L(old), "new": L(new)}}
    if kind == "misprint_in_print":
        x["corrected"] = corrected
    x["note"] = note
    F.append(x)


C2 = "plain numeral"
# ---------------------------------------------------------------- page 105
add(105, "(ii), l. 2: 'qui sont des générisations de x'", "'générisations' italic", "générisations (roman)",
    "italics", None, "high", r"des générisations de", r"des \emph{générisations} de")
add(105, "Proposition (5.7.5), last line: '(F|U)/(Σ_{i=1}^r f_i(F|U)) soit sans cycle premier associé immergé'",
    "the formula is in the running text (begins the line, followed on the same line by 'soit sans cycle premier associé immergé'); ordinary-size slash and parentheses",
    r"set as a display \[ ... \] with \big/ \Big( \Big)", "other", None, "high",
    r"\[¶(\mathscr F|U)\big/\Big(\sum_{i=1}^r f_i(\mathscr F|U)\Big)¶\]",
    r"$(\mathscr F|U)/(\sum_{i=1}^r f_i(\mathscr F|U))$",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost.")
add(105, "proof of (5.7.5), 1st paragraph: 'en disant que pour que F vérifie (S_1), il faut et il suffit que F soit sans cycle premier associé immergé.'",
    "'pour que ... associé immergé' italic ('en disant que' roman)", "roman", "italics", None, "high",
    r"disant que pour que $\mathscr F$ vérifie $(S_1)$, il faut et il suffit que¶$\mathscr F$ soit sans cycle premier associé immergé.",
    r"disant que \emph{pour que $\mathscr F$ vérifie $(S_1)$, il faut et il suffit que¶$\mathscr F$ soit sans cycle premier associé immergé}.")
add(105, "same paragraph: 'signifie que m_x n'est pas associé à F_x (0, 16.4.6, (i))'", "'n'est pas associé à' italic",
    "roman", "italics", None, "high",
    r"n'est pas associé à $\mathscr F_x$", r"\emph{n'est pas associé à} $\mathscr F_x$")
add(105, "same sentence: '(0, 16.4.6, (i)), ou encore'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.6, (i)), ou encore", r"(\textbf{0}, 16.4.6, (i)), ou encore")
add(105, "2nd paragraph, l. 1-2: 'la condition de l'énoncé est nécessaire'", "'nécessaire' italic", "roman",
    "italics", None, "high", r"est nécessaire.", r"est \emph{nécessaire}.")
add(105, "2nd paragraph: 'et que f est une section F-régulière de O_X au-dessus de X'",
    "'-régulière' italic (enlarged crop); the later 'élément F_x-régulier' is roman", "roman", "italics", None, "high",
    r"une section $\mathscr F$-régulière", r"une section $\mathscr F$-\emph{régulière}")
add(105, "2nd paragraph: 'alors F/fF vérifie (S_{k-1}) (i.e. vérifie (5.7.2.1) ...)'",
    "the first 'vérifie' italic (enlarged crop); the second, after 'i.e.', roman", "roman", "italics", None, "high",
    r"alors $\mathscr F/f\mathscr F$ vérifie", r"alors $\mathscr F/f\mathscr F$ \emph{vérifie}")
add(105, "2nd paragraph: 'prof(F_x/f_xF_x) = prof(F_x)-1 (0, 16.4.6, (i)), et'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.6, (i)), et", r"(\textbf{0}, 16.4.6, (i)), et")
add(105, "2nd paragraph: 'dim(F_x/f_xF_x) = dim(F_x)-1 (0, 16.3.4), et notre assertion'", "bold 0", C2, "convention", 2,
    "high", r"(0, 16.3.4), et", r"(\textbf{0}, 16.3.4), et")
add(105, "3rd paragraph, l. 1: 'la condition de l'énoncé est suffisante'", "'suffisante' italic", "roman", "italics",
    None, "high", r"est suffisante.", r"est \emph{suffisante}.")
add(105, "3rd paragraph: 'compte tenu de (0, 15.2.4)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 15.2.4)", r"(\textbf{0}, 15.2.4)")
add(105, "3rd paragraph: 'L'hypothèse entraîne que G = (F|U)/(Σ_{i=1}^{k-1} f_i(F|U)) est sans cycle premier associé immergé'",
    "the formula is in the running text (same line as 'L'hypothèse entraîne que' and 'est sans cycle premier associé')",
    r"set as a display \[ ... \] with \big/ \Big( \Big)", "other", None, "high",
    r"\[¶\mathscr G=(\mathscr F|U)\big/\Big(\sum_{i=1}^{k-1}¶f_i(\mathscr F|U)\Big)¶\]",
    r"$\mathscr G=(\mathscr F|U)/(\sum_{i=1}^{k-1}¶f_i(\mathscr F|U))$",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost.")
add(105, "3rd paragraph: 'dim(G_x) = dim(F_x)-(k-1) >= 1 (0, 16.3.4), donc'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.3.4), donc", r"(\textbf{0}, 16.3.4), donc")
add(105, "3rd paragraph: 'prof(G_x) >= 1 (0, 16.4.6), et comme'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.6), et comme", r"(\textbf{0}, 16.4.6), et comme")
add(105, "3rd paragraph: '(0, 16.4.6), on a prof(F_x) >= k'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.6), on a", r"(\textbf{0}, 16.4.6), on a")

# ---------------------------------------------------------------- page 106
add(106, "Remarques (5.7.8), l. 1: 'localement noethérien de dimension 1'",
    "'de dimension' italic in the roman remark body", "roman (inside the italic remarks environment)", "italics", None,
    "high", r"noethérien de dimension 1;", r"noethérien \emph{de dimension} 1;",
    "Judged with the remark body roman (document-wide remark item).")
add(106, "Remarques (5.7.8), last sentence: 'un préschéma localement noethérien réduit de dimension 1'",
    "'réduit' italic in the roman remark body", "roman (inside the italic remarks environment)", "italics", None, "high",
    r"noethérien réduit de dimension", r"noethérien \emph{réduit} de dimension",
    "Judged with the remark body roman (document-wide remark item).")
add(106, "Proposition (5.7.9), display (5.7.9.1)", "no punctuation after dim_{B_{q_i}}(M_{q_i}) (enlarged crop)",
    "comma after the formula", "punctuation", None, "high",
    r"(M_{\mathfrak q_i}),¶\tag{5.7.9.1}", r"(M_{\mathfrak q_i})¶\tag{5.7.9.1}",
    "GLOBAL_ISSUES 73 (commas after displays the print lacks).")
add(106, "proof of (5.7.9): '(par (0, 16.1.9) et (0, 16.4.8))', first reference", "bold 0", C2, "convention", 2, "high",
    r"(par (0, 16.1.9)", r"(par (\textbf{0}, 16.1.9)")
add(106, "same place, second reference '(0, 16.4.8))'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.8)), on", r"(\textbf{0}, 16.4.8)), on")
add(106, "proof of (5.7.9): 'que B est une A-algèbre finie'", "'finie' italic", "roman", "italics", None, "high",
    r"$A$-algèbre finie.", r"$A$-algèbre \emph{finie}.")
add(106, "proof of (5.7.9): 'Posons S = A—p'", "long dash for the set difference", "minus sign", "convention", 7,
    "high", r"$S=A-\mathfrak p$", r"$S=A\setmin\mathfrak p$")
add(106, "proof of (5.7.9): 'dim_{A_p}(M_p) = dim_{B'}(M_p) (0, 16.1.9). Cela étant'", "bold 0", C2, "convention", 2,
    "high", r"(0, 16.1.9). Cela", r"(\textbf{0}, 16.1.9). Cela")
add(106, "proof of (5.7.9): 'un cas particulier de (0, 16.1.7.4)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.1.7.4)", r"(\textbf{0}, 16.1.7.4)")
add(106, "proof of (5.7.9): 'on se ramène aussitôt comme dans (0, 16.4.8)'", "bold 0", C2, "convention", 2, "high",
    r"comme dans (0, 16.4.8)", r"comme dans (\textbf{0}, 16.4.8)")
add(106, "proof of (5.7.9): 'le même raisonnement que dans (0, 16.4.8) montre'", "bold 0", C2, "convention", 2, "high",
    r"que dans (0, 16.4.8)", r"que dans (\textbf{0}, 16.4.8)")
add(106, "proof of (5.7.9): 'un sous-B'-module de longueur finie'", "'longueur finie' italic", "roman", "italics", None,
    "high", r"de longueur finie", r"de \emph{longueur finie}")
add(106, "proof of (5.7.9): 'aussi un sous-B'-module simple'", "'simple' italic", "roman", "italics", None, "high",
    r"sous-$B'$-module¶simple;", r"sous-$B'$-module¶\emph{simple};")
add(106, "end of the proof of (5.7.9): 'prof_{B_{q_i}}(M_{q_i}) = 0 (0, 16.4.6)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.6)", r"(\textbf{0}, 16.4.6)")
add(106, "Corollaire (5.7.10), l. 1: 'les hypothèses de (5.7.9), et supposons'",
    "the reference is upright inside the italic statement (enlarged crop)", "italic (statement environment)",
    "convention", 6, "high", r"de (5.7.9), et", r"de \textup{(5.7.9)}, et")
add(106, "Corollaire (5.7.11), l. 1: 'les hypothèses de (5.7.9).'",
    "the reference is upright inside the italic statement (enlarged crop)", "italic (statement environment)",
    "convention", 6, "high", r"de (5.7.9).¶\begin{enumerate}", r"de \textup{(5.7.9)}.¶\begin{enumerate}")
add(106, "Corollaire (5.7.11): item label (i)", "label (i) upright", "italic inside the corollary environment",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(106, "Corollaire (5.7.11): item label (ii)", "label (ii) upright", "italic inside the corollary environment",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")

# ---------------------------------------------------------------- page 107
add(107, "(5.7.12), l. 1-2: 'un anneau noethérien quelconque A'", "'quelconque' italic", "roman", "italics", None,
    "high", r"quelconque $A$", r"\emph{quelconque} $A$")
add(107, "(5.7.12), l. 2-3: 'comme égal à coprof(M) = sup_{x∈X}(coprof_{A_x}(M_x)), où X = Spec(A); nous verrons'",
    "in the running text: 'égal à coprof(M) = sup_{x∈X} (coprof_{A_x}(M_x)), où X = Spec(A) ;', with parentheses around coprof_{A_x}(M_x) and the word 'où' (enlarged crop)",
    r"displayed \[ coprof(M) = \sup_{x\in X} coprof_{A_x}(M_x),\qquad X = Spec(A); \]: no parentheses after sup, 'où' replaced by \qquad",
    "formula", None, "high",
    r"\[¶\operatorname{coprof}(M)=\sup_{x\in X}¶\operatorname{coprof}_{A_x}(M_x),\qquad X=\operatorname{Spec}(A);¶\]",
    r"$\operatorname{coprof}(M)=\sup_{x\in X}¶(\operatorname{coprof}_{A_x}(M_x))$, où $X=\operatorname{Spec}(A)$;",
    "Three differences in one edit: display where the print has the formula inline, the connecting word 'où' lost (GLOBAL_ISSUES 51), and the missing parentheses around coprof_{A_x}(M_x).")
add(107, "(5.7.12), l. 4: 'que cette définition coïncide avec celle de'", "'coïncide' italic", "roman", "italics", None,
    "high", r"coïncide", r"\emph{coïncide}")
add(107, "(5.7.12), l. 4: 'celle de (0, 16.4.9)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.4.9)", r"(\textbf{0}, 16.4.9)")
add(107, "(5.7.12), last line: 'un anneau noethérien local.'", "'local' italic", "roman", "italics", None, "high",
    r"noethérien local.", r"noethérien \emph{local}.")
add(107, "heading 5.8", "'5.8. Préschémas réguliers et propriété (R_k). Critère de normalité de Serre.' (final full stop)",
    "no full stop", "punctuation", None, "high",
    r"Critère de normalité de Serre}{", r"Critère de normalité de Serre.}{",
    "Subsection titles lack the printed full stop (GLOBAL_ISSUES 43).")
add(107, "(5.8.1), l. 1: 'Rappelons (0_I, 4.1.4)'", "bold 0", C2, "convention", 2, "high",
    r"$(0_{\mathrm I},4.1.4)$", r"$(\mathbf{0}_{\mathrm I},4.1.4)$")
add(107, "(5.8.1), l. 2: 'si O_x est un anneau régulier'", "'régulier' italic", "roman", "italics", None, "high",
    r"anneau régulier. Quand", r"anneau \emph{régulier}. Quand")
add(107, "(5.8.1), last line: 'que lorsque X est localement noethérien'", "'localement noethérien' italic", "roman",
    "italics", None, "high", r"est¶localement noethérien.", r"est¶\emph{localement noethérien}.")
add(107, "Définition (5.8.2), l. 1-2: 'X est régulier en codimension ≤k'",
    "'régulier en codimension' roman inside the italic definition (enlarged crop)",
    "italic (definition environment)", "convention", 6, "high",
    r"régulier en codimension¶$\leq k$,", r"\textup{régulier en codimension¶$\leq k$},")
add(107, "Définition (5.8.2), l. 2: 'ou possède la propriété (R_k) si'",
    "'possède la propriété' roman ('ou' italic) (enlarged crop)", "italic (definition environment)", "convention", 6,
    "high", r"ou possède la propriété $(R_k)$ si", r"ou \textup{possède la propriété $(R_k)$} si")
add(107, "Définition (5.8.2), l. 3: '(autrement dit (5.1.3), si, pour tout'",
    "'(autrement dit (5.1.3),' roman (enlarged crop)", "italic (definition environment)", "convention", 6, "high",
    r"(autrement dit (5.1.3),", r"\textup{(autrement dit (5.1.3),}")
add(107, "paragraph after (5.8.2): 'possède la propriété (R_k) pour tout k.'",
    "the final k is an upright roman k (wrong fount; enlarged crop), unlike the italic subscript k of (R_k)",
    "italic $k$ (silently corrected)", "misprint_in_print", None, "high",
    r"tout $k$.", r"tout $\mathrm{k}$.",
    "Wrong-fount letter, reproduced in the diplomatic text (GLOBAL_ISSUES 29); the correct reading is the italic variable k.",
    corrected=r"$k$")
add(107, "next paragraph, l. 1: 'où A est un anneau noethérien, on dira'", "'noethérien' italic", "roman", "italics",
    None, "high", r"anneau noethérien, on dira", r"anneau \emph{noethérien}, on dira")
add(107, "same paragraph, l. 2-3: 'l'anneau A est régulier (0, 17.3.6)'", "'régulier' italic", "roman", "italics", None,
    "high", r"l'anneau $A$ est régulier", r"l'anneau $A$ est \emph{régulier}")
add(107, "same paragraph: '(0, 17.3.6). Pour un préschéma'", "bold 0", C2, "convention", 2, "high",
    r"(0, 17.3.6). Pour", r"(\textbf{0}, 17.3.6). Pour")
add(107, "same paragraph: 'on dira que X possède la propriété (R_k) en un point x∈X'",
    "'possède la propriété' and 'en un point' italic", "roman", "italics", None, "high",
    r"possède la¶propriété $(R_k)$ en un point", r"\emph{possède la¶propriété $(R_k)$ en un point}")
add(107, "same paragraph: 'pour toute générisation x' de x'", "'générisation' italic", "roman", "italics", None, "high",
    r"toute générisation", r"toute \emph{générisation}")
add(107, "same paragraph: 'la propriété (R_n) pour tout n ≥ 0 au point x'", "'tout' italic (enlarged crop)", "roman",
    "italics", None, "high", r"pour tout¶$n\geq0$", r"pour \emph{tout}¶$n\geq0$")
add(107, "same paragraph, last line: 'en vertu de (0, 17.3.6).'", "bold 0", C2, "convention", 2, "high",
    r"en vertu de (0, 17.3.6)", r"en vertu de (\textbf{0}, 17.3.6)")
add(107, "proof of (5.8.3), last line: 'un anneau régulier (0, 17.3.7)'", "'régulier' italic", "roman", "italics", None,
    "high", r"est un anneau¶régulier", r"est un anneau¶\emph{régulier}")
add(107, "proof of (5.8.3): '(0, 17.3.7)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 17.3.7)", r"(\textbf{0}, 17.3.7)")
add(107, "(5.8.4), l. 2: 'l'anneau O_x est un corps (0, 17.1.4)'", "'corps' italic", "roman", "italics", None, "high",
    r"est un corps¶", r"est un \emph{corps}¶")
add(107, "(5.8.4), l. 2: '(0, 17.1.4)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 17.1.4)", r"(\textbf{0}, 17.1.4)")
add(107, "(5.8.4), l. 3: 'que X est réduit en ce point'", "'réduit' italic", "roman", "italics", None, "high",
    r"est réduit en ce point", r"est \emph{réduit} en ce point")
add(107, "(5.8.4), last line: 'où X est réduit est ouvert (le'", "'ouvert' italic ('réduit' roman here)", "roman",
    "italics", None, "high", r"réduit est ouvert", r"réduit est \emph{ouvert}")
add(107, "end of page: '... est ouvert (le' | p. 108 'nilradical de X ...'",
    "the sentence runs on to p. 108 without a paragraph break", r"blank line after '(le' before \oldpage[IV-2]{108}",
    "other", None, "high", "(le¶¶", "(le¶",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the p. 108 top entry.")

# ---------------------------------------------------------------- page 108
add(108, "top of page", "the page continues the sentence of p. 107 ('(le | nilradical de X ...'), flush left, no new paragraph",
    r"blank line after \oldpage[IV-2]{108}: paragraph break inside the sentence", "other", None, "high",
    r"\oldpage[IV-2]{108}¶¶nilradical", r"\oldpage[IV-2]{108}¶nilradical",
    "Apply together with the p. 107 end entry (GLOBAL_ISSUES 20).")
add(108, "l. 1: '(I, 6.1.1 et 0_I, 5.2.2)'", "bold I", C2, "convention", 2, "high",
    r"(I, 6.1.1", r"(\textbf{I}, 6.1.1")
add(108, "l. 1: same reference, '0_I, 5.2.2'", "bold 0", C2, "convention", 2, "high",
    r"$0_{\mathrm I}$, 5.2.2", r"$\mathbf{0}_{\mathrm I}$, 5.2.2")
add(108, "l. 2-3: 'l'ensemble U est partout dense'", "'partout dense' italic", "roman", "italics", None, "high",
    r"est partout dense.", r"est \emph{partout dense}.")
add(108, "Théorème (5.8.6): item label (i)", "label (i) upright", "italic inside the theorem environment",
    "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]", "GLOBAL_ISSUES 16.")
add(108, "Théorème (5.8.6) (i): '(c'est-à-dire est un corps ou un anneau de valuation discrète (0, 17.1.4))'",
    "'(c'est-à-dire est un', 'ou un' and '(0, 17.1.4))' upright; 'corps' and 'anneau de valuation discrète' italic (enlarged crop)",
    "all italic (theorem environment)", "convention", 6, "high",
    r"(c'est-à-dire est un corps ou un anneau de valuation discrète (0, 17.1.4))",
    r"\textup{(c'est-à-dire est un} corps \textup{ou un} anneau de valuation discrète \textup{(\textbf{0}, 17.1.4))}",
    "One edit for this finding and the next (convention 2): upright words and the bold 0 together.")
add(108, "Théorème (5.8.6) (i): same reference '(0, 17.1.4)'", "bold 0", C2, "convention", 2, "high", None, None,
    "Covered by the edit of the preceding finding (convention 6), which adds the \\textbf{0}.")
add(108, "Théorème (5.8.6): item label (ii)", "label (ii) upright", "italic inside the theorem environment",
    "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", "GLOBAL_ISSUES 16.")
add(108, "proof of (5.8.6), 1st paragraph: 'Les conditions sont nécessaires.'", "'nécessaires' italic", "roman",
    "italics", None, "high", r"sont nécessaires", r"sont \emph{nécessaires}")
add(108, "same paragraph: 'en vertu de (II, 7.1.6)'", "bold II", C2, "convention", 2, "high",
    r"(II, 7.1.6)", r"(\textbf{II}, 7.1.6)")
add(108, "same paragraph: '(Bourbaki, Alg. comm., chap. VII, § 1, nº 4, prop. 8)'",
    "superior letter o in nº (enlarged crop)", "degree sign: n°", "symbol", None, "medium",
    r"§ 1, n° 4", r"§ 1, n\textsuperscript{o} 4",
    "The rest of the edition writes n\\textsuperscript{o} (GLOBAL_ISSUES 57); ega4-2-fr.tex has the degree sign also on printed pp. 103, 148, 154.")
add(108, "2nd paragraph, l. 1: 'Les conditions sont suffisantes.'", "'suffisantes' italic", "roman", "italics", None,
    "high", r"sont suffisantes", r"sont \emph{suffisantes}")
add(108, "2nd paragraph, l. 1-2: 'il résulte d'abord de (5.8.5) que X est réduit.'", "'réduit' italic", "roman",
    "italics", None, "high", r"est réduit. La", r"est \emph{réduit}. La")
add(108, "2nd paragraph, l. 3: 'où A est un anneau noethérien réduit (I, 5.1.4)'", "'réduit' italic", "roman",
    "italics", None, "high", r"noethérien réduit¶", r"noethérien \emph{réduit}¶")
add(108, "2nd paragraph: '(I, 5.1.4)'", "bold I", C2, "convention", 2, "high",
    r"(I, 5.1.4)", r"(\textbf{I}, 5.1.4)")
add(108, "2nd paragraph: '(compte tenu de (II, 6.3.6))'", "bold II", C2, "convention", 2, "high",
    r"(II, 6.3.6)", r"(\textbf{II}, 6.3.6)")
add(108, "2nd paragraph: 'que A est intégralement fermé dans R'", "'intégralement fermé dans' italic", "roman",
    "italics", None, "high", r"intégralement fermé dans", r"\emph{intégralement fermé dans}")
add(108, "after (5.8.6.1): 'par platitude (0_I, 5.3.1)'", "bold 0", C2, "convention", 2, "high",
    r"$(0_{\mathrm I},5.3.1)$", r"$(\mathbf{0}_{\mathrm I},5.3.1)$")
add(108, "after (5.8.6.1): 'que A/gA n'a que des idéaux premiers associés non immergés p_i'",
    "'non immergés' italic (the earlier 'sont non immergés' of the first paragraph is roman)", "roman", "italics", None,
    "high", r"associés non immergés", r"associés \emph{non immergés}")
add(108, "after (5.8.6.1): '(Bourbaki, Alg. comm., chap. IV, § 2, nº 3, prop. 5)'", "superior letter o in nº",
    "degree sign: n°", "symbol", None, "medium", r"§ 2, n° 3", r"§ 2, n\textsuperscript{o} 3",
    "As the first nº on this page.")
add(108, "after (5.8.6.1): 'en vertu du Hauptidealsatz (0, 16.3.2)'", "bold 0", C2, "convention", 2, "high",
    r"(0, 16.3.2)", r"(\textbf{0}, 16.3.2)")

# ---------------------------------------------------------------- page 109
add(109, "heading 5.9", "'5.9. Modules Z-purs et Z-clos.' (final full stop)", "no full stop", "punctuation", None,
    "high", r"$Z$-clos}{", r"$Z$-clos.}{", "Subsection titles lack the printed full stop (GLOBAL_ISSUES 43).")
add(109, "(5.9.1), 2nd paragraph, l. 1: 'Posons U_α = X—Z_α'", "long dash for the set difference", "minus sign",
    "convention", 7, "high", r"$U_\alpha=X-Z_\alpha$", r"$U_\alpha=X\setmin Z_\alpha$")
add(109, "same line: 'de sorte que X—Z est intersection'", "long dash for the set difference", "minus sign",
    "convention", 7, "high", r"$X-Z$", r"$X\setmin Z$")
add(109, "(5.9.1), 2nd paragraph: 'on a donc (i_β)_*(F|U_β) = (i_α)_*((i_αβ)_*(F|U_β)); de l'homomorphisme'",
    "the formula is in the running text (ends the line that begins '(non nécessairement quasi-cohérent); on a donc')",
    r"set as a display \[ ... \]", "other", None, "high",
    r"\[¶(i_\beta)_*(\mathcal F|U_\beta)¶=(i_\alpha)_*((i_{\alpha\beta})_*(\mathcal F|U_\beta));¶\]",
    r"$(i_\beta)_*(\mathcal F|U_\beta)¶=(i_\alpha)_*((i_{\alpha\beta})_*(\mathcal F|U_\beta))$;",
    "Formula displayed where the print has it inline (GLOBAL_ISSUES 21); no connecting word lost.")
add(109, "same paragraph: 'de l'homomorphisme canonique (0_I, 4.4.3.2)'", "bold 0", C2, "convention", 2, "high",
    r"$(0_{\mathrm I},4.4.3.2)$", r"$(\mathbf{0}_{\mathrm I},4.4.3.2)$")
add(109, "after (5.9.1.1): 'Ce O_X-Module ne dépend pas ...'",
    "'Ce O_X-Module' starts flush left: the paragraph continues after the display (the next paragraph, 'Soit alors', is indented)",
    r"blank line after \end{equation}: new indented paragraph", "other", None, "high",
    r"\end{equation}¶¶Ce $\mathcal O_X$-Module", r"\end{equation}¶Ce $\mathcal O_X$-Module",
    "Spurious paragraph break after a display.")
add(109, "same paragraph, l. 2: 'soit V un ouvert noethérien de X'", "'noethérien' italic", "roman", "italics", None,
    "high", r"ouvert¶noethérien de $X$", r"ouvert¶\emph{noethérien} de $X$")
add(109, "same paragraph, l. 2: 'on sait (G, II, 3.10.1) que dans la catégorie'",
    "'(G, II, 3.10.1)': Godement's book, chapter II (roman G and II, not bold; enlarged crop)",
    r"$(0_{\mathrm{II}},3.10.1)$: a reference to a chapter 0_II, which does not exist", "word", None, "high",
    r"$(0_{\mathrm{II}},3.10.1)$", r"(G, II, 3.10.1)",
    "Wrong reference in the TeX (the only 0_II reference in the diplomatic sources); the edition writes Godement references as (G, II, ...) elsewhere. Godement II 3.10.1 is the commutation of sections over a noetherian space with inductive limits, which is what is used here. The same text is in IV2/direct/EGA_IV2_French_Standalone_Reader.tex.")
add(109, "same paragraph, l. 3: 'le foncteur G ⇝ Γ(V, G)'", "wavy arrow ⇝ (enlarged crop)", r"\mapsto", "symbol", None,
    "high", r"\mathcal G\mapsto\Gamma", r"\mathcal G\leadsto\Gamma", "GLOBAL_ISSUES 33/73 (wavy arrows).")
add(109, "last paragraph: 'V∩Z_α∩Z'_λ = V∩Z_α (0_III, 9.2.4)'", "bold 0", C2, "convention", 2, "high",
    r"$(0_{\mathrm{III}},9.2.4)$", r"$(\mathbf{0}_{\mathrm{III}},9.2.4)$")
add(109, "last paragraph: '(où U'_λ = X—Z'_λ)'", "long dash for the set difference", "minus sign", "convention", 7,
    "high", r"$U'_\lambda=X-Z'_\lambda$", r"$U'_\lambda=X\setmin Z'_\lambda$")

# ---------------------------------------------------------------- checks
ok = True
counts = {}
for p in sorted({x["page"] for x in F}):
    text = (RUN / f"page_{p}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")
    cur = text
    for x in [y for y in F if y["page"] == p]:
        k = x["kind"]
        c = counts.setdefault(p, [0, 0, 0])
        c[1 if k == "convention" else 2 if k == "misprint_in_print" else 0] += 1
        fx = x["fix"]
        if not fx:
            continue
        n0 = text.count(fx["old"])
        n1 = cur.count(fx["old"])
        if n0 != 1 or n1 != 1:
            ok = False
            print("PROBLEM", p, repr(fx["old"]), "original:", n0, "sequential:", n1)
        cur = cur.replace(fx["old"], fx["new"], 1)
    print(p, "normal/convention/misprint =", "/".join(map(str, counts[p])))
json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print("written", OUT, len(F), "findings;", "all olds unique" if ok else "SOME OLDS NOT UNIQUE")
