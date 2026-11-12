"""Build findings_076_080.json and check that every fix 'old' occurs exactly once
in its page_NNN.tex (CRLF normalised to LF). The page files are only read."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = RUN + r"\findings_076_080.json"


def N(s):
    """Placeholder ⏎ stands for a line break (LF)."""
    return s.replace("⏎", "\n")


def fx(old, new):
    return {"old": N(old), "new": N(new)}


F = []


def add(page, where, scan, tex, kind, conv, conf, fix, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf, "fix": fix}
    if corrected is not None:
        d["corrected"] = N(corrected)
    d["note"] = note
    F.append(d)


G20 = "GLOBAL_ISSUES item 20 (blank line at a page break that falls mid-sentence). \\oldpage ends with \\ignorespaces, so joining the lines leaves a single space."
G21 = "Layout: inline in the print, displayed in the TeX (GLOBAL_ISSUES 21)."
C7 = "\\setmin is \\providecommand'ed as '-' in EGA_IV1_FR.tex; the long dash appears once the convention-7 decision redefines it."
KNOTE = ("Fraktur K, not R: the same glyph as the \\mathfrak K of 𝔎_{H,μ,n} on this page and as the 𝔎 of 18.1-18.5 "
         "(findings_051_055, 056_060, 066_070); 6x crops compared. All 16 \\mathfrak R on p. 80 are the printed 𝔎 "
         "(15 entries, plus one inside the (P) display edit).")

# ---------------------------------------------------------------- page 75 (companion)
add(75, "foot of p. 75 / top of p. 76, proof of (19.1.10): '... car si u_0 est inversible / à gauche, il en est de même de u_00 ...'",
    "no paragraph break across the page break (p. 76 begins flush left in mid-sentence)",
    "blank line before \\oldpage[0\\textsubscript{IV-1}]{76} (last line of page 75's segment)",
    "other", None, "high",
    fx(r"car si $u_0$ est inversible⏎⏎", r"car si $u_0$ est inversible⏎"),
    "OUTSIDE pages 76-80: lies in page_075.tex (checked unique there); listed so the pair is complete, drop it if findings_071_075 has the same edit. Apply together with the first p. 76 entry. " + G20)

# ---------------------------------------------------------------- page 76
add(76, "top of p. 76: 'à gauche, il en est de même de u_00 ...' (continues the proof of (19.1.10) from p. 75)",
    "no paragraph break: the first line continues the sentence, flush left",
    "blank line after \\oldpage[0\\textsubscript{IV-1}]{76}",
    "other", None, "high",
    fx(r"\oldpage[0\textsubscript{IV-1}]{76}⏎⏎à gauche", r"\oldpage[0\textsubscript{IV-1}]{76}⏎à gauche"),
    "Apply together with the p. 75 entry ('car si $u_0$ est inversible', end of page 75's segment). " + G20)

add(76, "proof of (19.1.10), line 1: 'u_00 : M/𝔍_0M → N/𝔍_0M obtenu par tensorisation de u_0 avec 1_{A/𝔍_0}'",
    "u_00 : M/𝔍_0M → N/𝔍_0M (2.5x crop: the target ends in M)",
    "$u_{00}:M/\\mathfrak J_0M\\to N/\\mathfrak J_0M$ (keeps the printed reading)",
    "misprint_in_print", None, "high", None,
    "The target of u_00 = u_0 ⊗ 1_{A/𝔍_0} is (N/𝔍N)⊗_{A/𝔍}(A/𝔍_0) = N/𝔍_0N (compare the identity for M printed just after). The diplomatic TeX keeps the misprint.",
    corrected=r"$u_{00}:M/\mathfrak J_0M\to N/\mathfrak J_0N$")

add(76, "proof of (19.1.10), line 2: 'puisque l'on a M/𝔍_0M = (M/𝔍M)⊗_{A/𝔍}(A/𝔍_0). Supposons donc'",
    "formula inline in the running text", "set as a display \\[ ... \\]",
    "other", None, "high",
    fx(r"\[⏎  M/\mathfrak J_0M=(M/\mathfrak JM)\otimes_{A/\mathfrak J}(A/\mathfrak J_0).⏎\]",
       r"$M/\mathfrak J_0M=(M/\mathfrak JM)\otimes_{A/\mathfrak J}(A/\mathfrak J_0)$."),
    G21)

add(76, "proof of (19.1.10): 'il y a un A-module de type fini L et un A-homomorphisme f : L→M'",
    "'il y a un A-module de type fini L' (no 'libre'); the proof later uses 'puisqu'ici L est libre'",
    "il y a un $A$-module de type fini $L$ (keeps the printed reading)",
    "misprint_in_print", None, "low", None,
    "The argument needs L free (the remark at the start of the proof is applied to g = u∘f because 'ici L est libre'); 'libre' is missing here, or misplaced in 'M/𝔍M étant libre de type fini'. Possibly an authorial slip rather than a misprint: a decision for the corrected edition.",
    corrected=r"il y a un $A$-module libre de type fini $L$")

add(76, "proof of (19.1.10): 'on en conclut tout d'abord que f est surjectif par le lemme de Nakayama'",
    "surjectif in italics", "surjectif upright (no \\emph)",
    "italics", None, "high",
    fx(r"est surjectif par", r"est \emph{surjectif} par"))

for lab, ctx in (("a)", "a"), ("b)", "b"), ("c)", "c"), ("d)", "d")):
    add(76, f"Corollaire (19.1.12), label {lab}",
        f"{lab} upright (roman) in the italic statement",
        f"\\item[{lab}] comes out italic in the statement environment",
        "convention", 6, "high",
        fx(rf"\item[{lab}]", rf"\item[\textup{{{lab}}}]"))

add(76, "Corollaire (19.1.12) b): 'u⊗1 : M⊗_A k(𝔭) → N⊗_A k(𝔭)', first k(𝔭)",
    "bold italic k", "$M\\otimes_Ak(\\mathfrak p)$",
    "convention", 1, "high",
    fx(r"M\otimes_Ak(\mathfrak p)\to", r"M\otimes_A\boldsymbol{k}(\mathfrak p)\to"))

add(76, "Corollaire (19.1.12) b): 'u⊗1 : M⊗_A k(𝔭) → N⊗_A k(𝔭)', second k(𝔭)",
    "bold italic k", "$N\\otimes_Ak(\\mathfrak p)$",
    "convention", 1, "high",
    fx(r"N\otimes_Ak(\mathfrak p)$ est", r"N\otimes_A\boldsymbol{k}(\mathfrak p)$ est"))

add(76, "Corollaire (19.1.12) b): '(on rappelle que k(𝔭) désigne le corps résiduel de A en 𝔭)'",
    "the whole parenthesis is printed roman inside the italic statement",
    "italic (statement environment)",
    "convention", 6, "high",
    fx(r"(on rappelle que $k(\mathfrak p)$ désigne le corps résiduel de $A$⏎  en $\mathfrak p$)",
       r"\textup{(on rappelle que $\boldsymbol{k}(\mathfrak p)$ désigne le corps résiduel de $A$⏎  en $\mathfrak p$)}"),
    "The same edit writes the bold italic k of the third k(𝔭) (convention 1, next entry).")

add(76, "Corollaire (19.1.12) b): '(on rappelle que k(𝔭) désigne ...)', third k(𝔭)",
    "bold italic k", "$k(\\mathfrak p)$",
    "convention", 1, "high", None,
    "Included in the convention-6 edit of the parenthesis (previous entry).")

add(76, "Corollaire (19.1.12) c): 'det(<y_i^*, u(x_j)>) ∉ 𝔭'",
    "the pairing brackets are printed as the signs < and > (3x crop)",
    "\\det(\\langle y_i^*,u(x_j)\\rangle)",
    "symbol", None, "medium",
    fx(r"\det(\langle y_i^*,u(x_j)\rangle)", r"\det(\mathopen{<}y_i^*,u(x_j)\mathclose{>})"),
    "\\mathopen/\\mathclose keep the printed spacing (no relation spacing). The print's angle brackets may be < > throughout the edition: see final message.")

add(76, "Corollaire (19.1.12) d): 'Il existe f∈A—𝔭'",
    "long dash (set difference)", "A-\\mathfrak p",
    "convention", 7, "high",
    fx(r"$f\in A-\mathfrak p$", r"$f\in A\setmin\mathfrak p$"), C7)

add(76, "Corollaire (19.1.12): 'En outre, l'ensemble des 𝔭∈Spec(A) vérifiant ces conditions est ouvert dans Spec(A).'",
    "a new indented paragraph after d)",
    "follows \\end{enumerate} without a blank line, so it starts unindented",
    "other", None, "medium",
    fx(r"\end{enumerate}⏎En outre", r"\end{enumerate}⏎⏎En outre"),
    "Paragraph structure (cf. GLOBAL_ISSUES 47).")

add(76, "proof of (19.1.12): 'La dernière condition est conséquence triviale de d).'",
    "d) in italics", "d) upright", "italics", None, "high",
    fx(r"triviale de d).", r"triviale de \emph{d)}."))

add(76, "proof of (19.1.12): 'comme chacun des énoncés a), b), c), d) est équivalent'",
    "a), b), c), d) in italics", "upright", "italics", None, "high",
    fx(r"énoncés a), b), c), d) est", r"énoncés \emph{a)}, \emph{b)}, \emph{c)}, \emph{d)} est"))

add(76, "proof of (19.1.12): 'Il est trivial que d) entraîne a), et a) et b) sont équivalentes'",
    "d), a), a), b) in italics", "upright", "italics", None, "high",
    fx(r"trivial que d) entraîne a), et a) et b)",
       r"trivial que \emph{d)} entraîne \emph{a)}, et \emph{a)} et \emph{b)}"))

add(76, "proof of (19.1.12): 'd'ailleurs a) entraîne que M_𝔭 est libre'",
    "a) in italics", "upright", "italics", None, "high",
    fx(r"d'ailleurs a) entraîne", r"d'ailleurs \emph{a)} entraîne"))

add(76, "proof of (19.1.12): 'donc a) entraîne c), en prenant pour les x_i'",
    "a), c) in italics", "upright", "italics", None, "high",
    fx(r"donc a) entraîne c),", r"donc \emph{a)} entraîne \emph{c)},"))

add(76, "foot of p. 76 / top of p. 77, proof of (19.1.12): '... forment une base de ce / A_𝔭-module et en notant que ...'",
    "no paragraph break across the page break (p. 77 begins flush left in mid-sentence)",
    "blank line before \\oldpage[0\\textsubscript{IV-1}]{77} (last line of page 76's segment)",
    "other", None, "high",
    fx(r"forment une base de ce⏎⏎", r"forment une base de ce⏎"),
    "Apply together with the first p. 77 entry (blank line after the marker). " + G20)

# ---------------------------------------------------------------- page 77
add(77, "top of p. 77: 'A_𝔭-module et en notant que ...' (continues the proof of (19.1.12))",
    "no paragraph break: the first line continues the sentence, flush left",
    "blank line after \\oldpage[0\\textsubscript{IV-1}]{77}",
    "other", None, "high",
    fx(r"\oldpage[0\textsubscript{IV-1}]{77}⏎⏎$A_{\mathfrak p}$-module",
       r"\oldpage[0\textsubscript{IV-1}]{77}⏎$A_{\mathfrak p}$-module"),
    "Apply together with the last p. 76 entry ('forment une base de ce'). " + G20)

add(77, "proof of (19.1.12): 's'écrit u = v/f, où f∈A—𝔭'",
    "long dash (set difference)", "A-\\mathfrak p", "convention", 7, "high",
    fx(r"où $f\in A-\mathfrak p$, et où", r"où $f\in A\setmin\mathfrak p$, et où"), C7)

add(77, "proof of (19.1.12): 'Il est clair que c) entraîne b), et il reste donc à voir que a) entraîne d).'",
    "c), b), a), d) in italics", "upright", "italics", None, "high",
    fx(r"clair que c) entraîne b), et il reste donc à voir que a)⏎entraîne d).",
       r"clair que \emph{c)} entraîne \emph{b)}, et il reste donc à voir que \emph{a)}⏎entraîne \emph{d)}."))

add(77, "proof of (19.1.12): 'un homomorphisme w : N→M et un élément f∈A—𝔭'",
    "long dash (set difference)", "A-\\mathfrak p", "convention", 7, "high",
    fx(r"élément $f\in A-\mathfrak p$", r"élément $f\in A\setmin\mathfrak p$"), C7)

add(77, "proof of (19.1.12): 'tels que w = w_𝔭⊗(1/f)1_{A_𝔭}'",
    "w = w_𝔭⊗(1/f)1_{A_𝔭} (2x crop)",
    "$w=w_{\\mathfrak p}\\otimes(1/f)1_{A_{\\mathfrak p}}$ (keeps the printed reading)",
    "misprint_in_print", None, "high", None,
    "w and w_𝔭 are interchanged: w: N→M is the homomorphism obtained from the given left inverse w_𝔭 of u_𝔭, and the next sentence ((w∘u)⊗1_{A_𝔭} = f.1_{M_𝔭}) uses w_𝔭 = w⊗(1/f)1_{A_𝔭}.",
    corrected=r"$w_{\mathfrak p}=w\otimes(1/f)1_{A_{\mathfrak p}}$")

add(77, "proof of (19.1.12): 'il existe g∈A—𝔭 tel que'",
    "long dash (set difference)", "A-\\mathfrak p", "convention", 7, "high",
    fx(r"$g\in A-\mathfrak p$", r"$g\in A\setmin\mathfrak p$"), C7)

add(77, "proof of (19.1.12): 'l'endomorphisme g((w∘u)—f.1_M)'",
    "long dash used for a subtraction", "(w\\circ u)-f.1_M", "convention", 7, "high",
    fx(r"(w\circ u)-f.1_M", r"(w\circ u)\setmin f.1_M"),
    "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes, pending the convention-7 decision.")

add(77, "Proposition (19.1.13): 'Supposons vérifiées les hypothèses de (19.1.9)'",
    "(19.1.9) upright in the italic statement", "italic", "convention", 6, "high",
    fx(r"(19.1.9) et supposons", r"\textup{(19.1.9)} et supposons"))

add(77, "Proposition (19.1.13): 'Alors les conditions a) et b) de (19.1.9)'",
    "a) and b) upright in the italic statement", "italic", "convention", 6, "high",
    fx(r"conditions a) et b)", r"conditions \textup{a)} et \textup{b)}"),
    "Two occurrences in one edit.")

add(77, "Proposition (19.1.13): 'de (19.1.9) sont aussi équivalentes à'",
    "(19.1.9) upright in the italic statement", "italic", "convention", 6, "high",
    fx(r"(19.1.9) sont", r"\textup{(19.1.9)} sont"))

add(77, "Proposition (19.1.13), label c)",
    "c) upright", "\\item[c)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[c)]", r"\item[\textup{c)}]"))

add(77, "proof of (19.1.13): 'On sait déjà que c) entraîne a) (19.1.6)'",
    "c), a) in italics", "upright", "italics", None, "high",
    fx(r"déjà que c) entraîne a) (19.1.6)", r"déjà que \emph{c)} entraîne \emph{a)} (19.1.6)"))

add(77, "proof of (19.1.13): 'Inversement, si a) est vérifiée'",
    "a) in italics", "upright", "italics", None, "high",
    fx(r"si a) est vérifiée", r"si \emph{a)} est vérifiée"))

add(77, "Proposition (19.1.14), label (i)",
    "(i) upright", "\\item[(i)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[(i)]", r"\item[\textup{(i)}]"))

add(77, "Proposition (19.1.14), label (ii)",
    "(ii) upright", "\\item[(ii)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[(ii)]", r"\item[\textup{(ii)}]"))

# ---------------------------------------------------------------- page 78
add(78, "Remarque (19.1.15), display 'N/W'' →h M/V' →u' N/W''",
    "no comma after the display (2.5x crop); the sentence goes on 'où u' est déduit de u ...'",
    "comma at the end of the display",
    "punctuation", None, "high",
    fx(r"\xrightarrow{u'}N/W',", r"\xrightarrow{u'}N/W'"))

add(78, "heading 19.2: '19.2. Modules formellement projectifs.'",
    "final full stop", "\\subsection{Modules formellement projectifs}",
    "punctuation", None, "high",
    fx(r"\subsection{Modules formellement projectifs}", r"\subsection{Modules formellement projectifs.}"),
    "GLOBAL_ISSUES 43/58 (no \\subsection title in ega0-14 to ega0-23 has the printed full stop).")

add(78, "Définition (19.2.1): 'On dit qu'un A-module topologique M est formellement projectif s'il vérifie'",
    "formellement projectif in the statement's italic, no change of face (2x crop)",
    "\\emph{formellement projectif} inside the italic definition environment (comes out upright)",
    "convention", 6, "high",
    fx(r"\emph{formellement projectif} s'il", r"formellement projectif s'il"))

add(78, "(19.2.2): 'se factorise en M/V' →w P →u M/V. On notera'",
    "formula inline in the running text", "set as a display",
    "other", None, "high",
    fx(r"\[⏎  M/V'\xrightarrow{w}P\xrightarrow{u}M/V.⏎\]", r"$M/V'\xrightarrow{w}P\xrightarrow{u}M/V$."),
    G21)

# ---------------------------------------------------------------- page 79
add(79, "proof of (19.2.4): 'se factorise en M/𝔍_μM →w P →u M/𝔍_λM; mais comme'",
    "formula inline in the running text", "set as a display",
    "other", None, "high",
    fx(r"\[⏎  M/\mathfrak J_\mu M\xrightarrow{w}P\xrightarrow{u}M/\mathfrak J_\lambda M;⏎\]",
       r"$M/\mathfrak J_\mu M\xrightarrow{w}P\xrightarrow{u}M/\mathfrak J_\lambda M$~;"),
    G21)

add(79, "proof of (19.2.4): 'w se factorise en M/𝔍_μM → M/𝔍_λM →v P'",
    "M/𝔍_μM → M/𝔍_λM →v P (crop)",
    "$M/\\mathfrak J_\\lambda M\\xrightarrow{v}P$: the first object and arrow are missing",
    "formula", None, "high",
    fx(r"se factorise en $M/\mathfrak J_\lambda M\xrightarrow{v}P$",
       r"se factorise en $M/\mathfrak J_\mu M\to M/\mathfrak J_\lambda M\xrightarrow{v}P$"))

add(79, "Proposition (19.2.5), label (i)",
    "(i) upright", "\\item[(i)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[(i)] Pour que", r"\item[\textup{(i)}] Pour que"))

add(79, "Proposition (19.2.5) (i): '(resp. strictement formellement projectif)'",
    "'(resp.' and the closing parenthesis upright, the words between italic",
    "all italic", "convention", 6, "high",
    fx(r"(resp. strictement⏎  formellement projectif), il faut",
       r"\textup{(resp.} strictement⏎  formellement projectif\textup{)}, il faut"))

add(79, "Proposition (19.2.5), label (ii)",
    "(ii) upright", "\\item[(ii)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[(ii)] Soit $A'$", r"\item[\textup{(ii)}] Soit $A'$"))

add(79, "Proposition (19.2.5) (ii): 'Si M est formellement projectif (resp. strictement formellement projectif), alors'",
    "'(resp.' and the closing parenthesis upright", "all italic", "convention", 6, "high",
    fx(r"(resp. strictement formellement projectif), alors",
       r"\textup{(resp.} strictement formellement projectif\textup{)}, alors"))

add(79, "Proposition (19.2.5) (ii): '... formellement projectif (resp. strictement formellement projectif).'",
    "'(resp.' and the closing parenthesis upright", "all italic", "convention", 6, "high",
    fx(r"(resp. strictement formellement⏎  projectif).",
       r"\textup{(resp.} strictement formellement⏎  projectif\textup{)}."))

add(79, "proof of (19.2.5) (ii): 'Si l'on considère le A-homomorphisme composé v : M →j M' →v Q''",
    "the label of the second arrow is printed v, without prime (5x crop; the w' two lines below has its prime)",
    "\\xrightarrow{v'} (silently corrected)",
    "misprint_in_print", None, "high",
    fx(r"M'\xrightarrow{v'}Q'", r"M'\xrightarrow{v}Q'"),
    "The composite is v = v'∘j with v': M'→Q' the given A'-homomorphism. The fix restores the printed v in the diplomatic text.",
    corrected=r"M'\xrightarrow{v'}Q'")

add(79, "proof of (19.2.5) (ii): 'en prenant les sous-modules Im(M⊗_A𝔍'_μ) + Im(V_λ⊗_AA') = W_λμ, où λ et μ'",
    "formula inline in the running text", "set as a display",
    "other", None, "high",
    fx(r"\[⏎    \operatorname{Im}(M\otimes_A\mathfrak J'_\mu)⏎    +\operatorname{Im}(V_\lambda\otimes_A A')=W_{\lambda\mu},⏎  \]",
       r"$\operatorname{Im}(M\otimes_A\mathfrak J'_\mu)⏎    +\operatorname{Im}(V_\lambda\otimes_A A')=W_{\lambda\mu}$,"),
    G21)

add(79, "proof of (19.2.5) (ii): 'Comme (M⊗_AA')/W_λμ = (M/V_λ)⊗_{A/𝔍_λ}(A'/𝔍'_μ) et que'",
    "formula inline in the running text", "set as a display",
    "other", None, "high",
    fx(r"\[⏎    (M\otimes_A A')/W_{\lambda\mu}⏎    =(M/V_\lambda)\otimes_{A/\mathfrak J_\lambda}⏎      (A'/\mathfrak J'_\mu)⏎  \]",
       r"$(M\otimes_A A')/W_{\lambda\mu}⏎    =(M/V_\lambda)\otimes_{A/\mathfrak J_\lambda}⏎      (A'/\mathfrak J'_\mu)$"),
    G21)

add(79, "heading 19.3: '19.3. Algèbres formellement lisses.'",
    "final full stop", "\\subsection{Algèbres formellement lisses}",
    "punctuation", None, "high",
    fx(r"\subsection{Algèbres formellement lisses}", r"\subsection{Algèbres formellement lisses.}"),
    "GLOBAL_ISSUES 43/58.")

add(79, "Définition (19.3.1): 'On dit que B est une A-algèbre formellement lisse si'",
    "formellement lisse in the statement's italic, no change of face",
    "\\emph{formellement lisse} inside the italic definition environment (comes out upright)",
    "convention", 6, "high",
    fx(r"\emph{formellement lisse} si", r"formellement lisse si"))

add(79, "Définition (19.3.1), last line of p. 79: 'pour toute A-algèbre topologique discrète C'",
    "discrète printed roman (upright) inside the italic statement",
    "italic", "convention", 6, "high",
    fx(r"topologique discrète", r"topologique \textup{discrète}"))

add(79, "Définition (19.3.1), first line of p. 80: 'et tout idéal nilpotent 𝔍 de C'",
    "nilpotent printed roman (upright) inside the italic statement",
    "italic", "convention", 6, "high",
    fx(r"nilpotent $\mathfrak J$ de", r"\textup{nilpotent} $\mathfrak J$ de"),
    "Printed on p. 80; the text stands in page 79's segment because \\oldpage{80} is misplaced (marker entries at the end): apply before the marker move.")

add(79, "Définition (19.3.1), p. 80 line 2: 'se factorise en B →v C →φ C/𝔍 où v est un homomorphisme continu'",
    "formula inline, and no comma after C/𝔍",
    "set as a display, with a comma",
    "other", None, "high",
    fx(r"\[⏎  B\xrightarrow{v}C\xrightarrow{\varphi}C/\mathfrak J,⏎\]",
       r"$B\xrightarrow{v}C\xrightarrow{\varphi}C/\mathfrak J$"),
    "Layout (display vs inline) and the comma the print does not have. Printed on p. 80, in page 79's segment: apply before the marker move.")

# ---------------------------------------------------------------- page 80
add(80, "(P): 'Pour tout idéal ouvert 𝔎 de la A-algèbre B'",
    "ouvert in italics", "upright", "italics", None, "high",
    fx(r"Pour tout idéal ouvert", r"Pour tout idéal \emph{ouvert}"))

K = [
    ("(P): 'Pour tout idéal ouvert 𝔎 de la A-algèbre B'", r"$\mathfrak R$ de la $A$-algèbre", r"$\mathfrak K$ de la $A$-algèbre"),
    ("(P): 'tout A-homomorphisme u' : B/𝔎 → C/𝔍, il y a'", r"$u':B/\mathfrak R\to C/\mathfrak J$, il y a", r"$u':B/\mathfrak K\to C/\mathfrak J$, il y a"),
    ("(P): 'un idéal ouvert 𝔎'⊂𝔎 de B'", r"$\mathfrak R'\subset\mathfrak R$ de $B$", r"$\mathfrak K'\subset\mathfrak K$ de $B$"),
    ("(P): 'l'homomorphisme B → B/𝔎 →u' C/𝔍 se factorise en'", r"B/\mathfrak R\xrightarrow{u'}C/\mathfrak J$ se factorise", r"B/\mathfrak K\xrightarrow{u'}C/\mathfrak J$ se factorise"),
    ("'il a pour noyau 𝔎 un idéal ouvert de B'", r"noyau $\mathfrak R$ un", r"noyau $\mathfrak K$ un"),
    ("'donc u se factorise en B → B/𝔎 →u' C/𝔍, et si (P)'", r"B/\mathfrak R\xrightarrow{u'}C/\mathfrak J$, et si", r"B/\mathfrak K\xrightarrow{u'}C/\mathfrak J$, et si"),
    ("'la composée B → B/𝔎' →v' C pour satisfaire'", r"B/\mathfrak R'\xrightarrow{v'}C$ pour", r"B/\mathfrak K'\xrightarrow{v'}C$ pour"),
    ("'donnons-nous un idéal ouvert 𝔎 de B'", r"ouvert $\mathfrak R$ de $B$ et un", r"ouvert $\mathfrak K$ de $B$ et un"),
    ("'un A-homomorphisme u' : B/𝔎 → C/𝔍, et appliquons'", r"B/\mathfrak R\to C/\mathfrak J$, et appliquons", r"B/\mathfrak K\to C/\mathfrak J$, et appliquons"),
    ("'à u : B → B/𝔎 →u' C/𝔍; si'", r"B/\mathfrak R\xrightarrow{u'}C/\mathfrak J$~; si", r"B/\mathfrak K\xrightarrow{u'}C/\mathfrak J$~; si"),
    ("'l'idéal 𝔎' = Ker(v)∩𝔎 de B'", r"$\mathfrak R'=\operatorname{Ker}(v)\cap\mathfrak R$", r"$\mathfrak K'=\operatorname{Ker}(v)\cap\mathfrak K$"),
    ("'est ouvert et contenu dans 𝔎'", r"contenu dans $\mathfrak R$", r"contenu dans $\mathfrak K$"),
    ("'par suite v se factorise en B → B/𝔎' →v' C, et'", r"B/\mathfrak R'\xrightarrow{v'}C$, et", r"B/\mathfrak K'\xrightarrow{v'}C$, et"),
]
for i, (w, o, n) in enumerate(K):
    add(80, w, "Fraktur K (𝔎)", "\\mathfrak R", "symbol", None, "high", fx(o, n),
        KNOTE if i == 0 else "Fraktur K, not R (see the first \\mathfrak R entry on this page).")

add(80, "(P): 'se factorise en B → B/𝔎' →v' C → C/𝔍, où v' est un A-homomorphisme'",
    "formula inline in the running text", "set as a display",
    "other", None, "high",
    fx(r"\[⏎    B\to B/\mathfrak R'\xrightarrow{v'}C\to C/\mathfrak J,⏎  \]",
       r"$B\to B/\mathfrak K'\xrightarrow{v'}C\to C/\mathfrak J$,"),
    "Layout (GLOBAL_ISSUES 21); the same edit writes the printed Fraktur K for \\mathfrak R' (no separate finding).")

add(80, "after (P): 'En effet, si u : B→C/𝔍 est un A-homomorphisme continu'",
    "a new indented paragraph", "follows \\end{enumerate} without a blank line, so it starts unindented",
    "other", None, "medium",
    fx(r"\end{enumerate}⏎En effet, si", r"\end{enumerate}⏎⏎En effet, si"),
    "Paragraph structure (cf. GLOBAL_ISSUES 47).")

add(80, "Lemme (19.3.4.1), label (i)",
    "(i) upright", "\\item[(i)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[(i)] Si $f", r"\item[\textup{(i)}] Si $f"))

add(80, "Lemme (19.3.4.1), label (ii) (printed at the top of p. 81)",
    "(ii) upright (page_081_s1.png)", "\\item[(ii)] comes out italic in the statement environment",
    "convention", 6, "high",
    fx(r"\item[(ii)] Inversement", r"\item[\textup{(ii)}] Inversement"),
    "Printed on p. 81; the item stands in page 80's segment because \\oldpage{81} is misplaced: apply before the marker move. The rest of (ii) agrees with the print of p. 81.")

# ---------------------------------------------------------------- marker moves (apply last, in this order)
add(80, "top of page_080.tex: \\oldpage{80} before 'La définition (19.3.1) revient à dire'",
    "printed p. 80 begins with the end of Définition (19.3.1): 'et tout idéal nilpotent 𝔍 de C, tout A-homomorphisme continu ...'",
    "the marker stands after \\end{definition}",
    "marker", None, "high",
    fx(r"\oldpage[0\textsubscript{IV-1}]{80}⏎⏎La définition", r"La définition"),
    "Move 79/80, step 1 of 2: delete the old marker and its blank line; step 2 is the next entry (page 79). Apply both or neither, after all other fixes on pp. 79-80. The blank line after \\end{definition} (end of page 79's segment) stays, so 'La définition (19.3.1)' still starts a paragraph.")

add(79, "page break 79/80 inside Définition (19.3.1): p. 79 ends '... A-algèbre topologique discrète C', p. 80 begins 'et tout idéal nilpotent 𝔍 de C'",
    "p. 80 begins with 'et tout idéal nilpotent' (page_080_s1.png)",
    "no marker inside the definition",
    "marker", None, "high",
    fx(r"$C$ et tout idéal", r"$C$⏎\oldpage[0\textsubscript{IV-1}]{80}⏎et tout idéal"),
    "Move 79/80, step 2 of 2: insert the marker after the previous entry (page 80) has deleted the old one. No blank lines: the page break falls mid-sentence.")

add(81, "top of page_081.tex: \\oldpage{81} before \\begin{proof} (proof of Lemme (19.3.4.1))",
    "printed p. 81 begins with item (ii) of Lemme (19.3.4.1): '(ii) Inversement, soient H une partie finie de I, ...'",
    "the marker stands after \\end{lemma}",
    "marker", None, "high",
    fx(r"\oldpage[0\textsubscript{IV-1}]{81}⏎⏎\begin{proof}", r"\begin{proof}"),
    "OUTSIDE pages 76-80: lies in page_081.tex (checked unique there); drop it if findings_081_085 has the same move. Move 80/81, step 1 of 2: delete the old marker; step 2 is the next entry (page 80). Apply both or neither, after all other fixes on pp. 80-81.")

add(80, "page break 80/81 inside Lemme (19.3.4.1): p. 80 ends with (i) '... f(T_α) est nilpotent dans E pour tout α∈H.', p. 81 begins with (ii)",
    "page_081_s1.png begins with '(ii) Inversement'",
    "no marker inside the lemma",
    "marker", None, "high",
    fx(r"nilpotent dans $E$ pour tout $\alpha\in H$.", r"nilpotent dans $E$ pour tout $\alpha\in H$.⏎  \oldpage[0\textsubscript{IV-1}]{81}"),
    "Move 80/81, step 2 of 2: insert the marker at the end of item (i), before \\item[(ii)], after the previous entry (page 81) has deleted the old one.")

# ---------------------------------------------------------------- uniqueness check
texts = {}
for p in sorted({d["page"] for d in F}):
    with open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")

bad = 0
for d in F:
    fix = d["fix"]
    if fix is None:
        continue
    c = texts[d["page"]].count(fix["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE/MISSING", d["page"], c, repr(fix["old"]))
print("findings:", len(F), "bad olds:", bad)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    counts.setdefault(d["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
for p in sorted(counts):
    print(p, counts[p])
