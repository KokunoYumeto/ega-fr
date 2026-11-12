"""Build findings_120_124.json for the EGA IV-3 scan check of pp. 120-124 and verify every fix.
'¶' stands for a line break in the TeX strings below."""
import json
import pathlib
import re

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_120_124.json"
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV3\native\ega4\ega4-11-fr.tex")


def nl(s):
    return None if s is None else s.replace("¶", "\n")


F = []


def add(page, where, scan, tex, kind, old, new, note="", confidence="high", convention=None, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---------------------------------------------------------------- page 120
add(120, "first line: 'Comme les L'_i sont des A'-modules libres, on sait (M, V, 1.1)'",
    "'libres' in italics", "'libres' upright", "italics",
    r"$A'$-modules libres,", r"$A'$-modules \emph{libres},")
add(120, "top of p. 120: 'Comme les L'_i sont des A'-modules libres ...' (continuation of (11.2.1))",
    "the line starts flush left (no indent): the paragraph of (11.2.1) runs on after the display (11.2.1.4) that ends p. 119",
    "\\end{env} closes (11.2.1) at the end of the p. 119 segment and blank lines surround \\oldpage[IV-3]{120}, so 'Comme les' starts a new indented paragraph",
    "other",
    r"\oldpage[IV-3]{120}¶¶Comme les", r"\oldpage[IV-3]{120}¶\noindent Comme les",
    "Paragraph structure only. The print's (11.2.1) runs on to 'est commutatif.' just before (11.2.2), so the \\end{env} "
    "at the end of the p. 119 segment stands too early; moving it would touch p. 119, so this edit only removes the "
    "indent (\\noindent, as the (16.4.5) precedent).", confidence="medium")
add(120, "diagram after 'formant un diagramme commutatif', top row (left end and between L'_i and L'_0)",
    "'...' on the baseline (enlarged crop: the dots sit at the foot of L and M, below the arrows)",
    "\\cdots (centred dots), twice", "symbol",
    r"\cdots\ar[r]&L'_{i+1}\ar[r]^{f'_i}\ar[d]_{u_{i+1}}&¶L'_i\ar[r]\ar[d]_{u_i}&\cdots\ar[r]&",
    r"\ldots\ar[r]&L'_{i+1}\ar[r]^{f'_i}\ar[d]_{u_{i+1}}&¶L'_i\ar[r]\ar[d]_{u_i}&\ldots\ar[r]&",
    "GLOBAL_ISSUES 22 (\\cdots for baseline dots).")
add(120, "same diagram, bottom row (left end and between L''_i and L''_0)",
    "'...' on the baseline", "\\cdots, twice", "symbol",
    r"\cdots\ar[r]&L''_{i+1}\ar[r]_{f''_i}&L''_i\ar[r]&\cdots\ar[r]&",
    r"\ldots\ar[r]&L''_{i+1}\ar[r]_{f''_i}&L''_i\ar[r]&\ldots\ar[r]&")
add(120, "same diagram, end of the bottom row 'M' -> 0'",
    "no full stop after 0 (enlarged crop)", "'0.' (full stop)", "punctuation",
    r"&M'\ar[r]&0.", r"&M'\ar[r]&0")
add(120, "after the diagram: 'Si l'on compose l'homomorphisme u_• : L'_• -> L''_• de complexes ...'",
    "'Si l'on compose' begins a new, indented paragraph",
    "no blank line after \\]: the text continues the paragraph", "other",
    r"\]¶Si l'on compose", r"\]¶¶Si l'on compose", "Missing paragraph break after a display (GLOBAL_ISSUES 47).")
add(120, "(11.2.2), l. 1-2: 'considérons maintenant un système inductif filtrant de A-algèbres'",
    "'système inductif' in italics, 'filtrant' roman (enlarged crop)", "\\emph{système inductif filtrant}",
    "italics", r"\emph{système inductif filtrant}", r"\emph{système inductif} filtrant")
add(120, "(11.2.2): 'est un système inductif de A_α-modules' (across the page break 120/121)",
    "'système' (last word of p. 120) and 'inductif de' and '-modules' (first line of p. 121) in italics (enlarged crop)",
    "\\emph{système¶inductif} de $A_\\alpha$-modules: the italics stop after 'inductif'", "italics",
    r"inductif} de $A_\alpha$-modules.", r"inductif de $A_\alpha$-modules}.",
    "Listed before the marker entry below, so that its 'old' is still inside the p. 120 segment when it is applied.")
add(120, "page break 120/121 inside (11.2.2): 'est un système | inductif de A_α-modules. Posons ...'",
    "p. 120 ends with 'est un système'; p. 121 begins 'inductif de A_α-modules. Posons A' = lim A_α, ...' "
    "(page_121_s1.png); Lemme (11.2.2.2) comes after the end of (11.2.2) on p. 121",
    "\\oldpage[IV-3]{121} stands after \\end{env} of (11.2.2), before \\begin{lemma}[11.2.2.2]: the rest of (11.2.2) "
    "('inductif de ... à prouver le', 9 printed lines of p. 121) lies in the p. 120 segment", "marker",
    "est un \\emph{système¶", "est un \\emph{système¶\\oldpage[IV-3]{121}¶",
    "Marker move, part 1 of 2 (apply both or neither): inserts the marker at the break, inside the \\emph group (as at "
    "0_I p. 41), with no blank lines, so the sentence stays one paragraph. Part 2 (page 121) removes the old marker. "
    "Apply after the italics entry above.")

# ---------------------------------------------------------------- page 121
add(121, "start of page_121.tex (old position of the p. 121 marker)",
    "Lemme (11.2.2.2) is not the start of p. 121: the last lines of (11.2.2) precede it",
    "\\oldpage[IV-3]{121} before \\begin{lemma}[11.2.2.2]", "marker",
    r"\oldpage[IV-3]{121}¶¶\begin{lemma}[11.2.2.2]", r"\begin{lemma}[11.2.2.2]",
    "Marker move, part 2 of 2: apply together with the page-120 marker entry (which inserts the marker after "
    "'est un \\emph{système').")
add(121, "Lemme (11.2.2.2), l. 6: 'si h'_βα : F(M_α) -> F(M_β) (pour α ≤ β)'",
    "h'_{βα} with a prime, the same sign as in h'_α beside it (enlarged crop)", "h^0_{\\beta\\alpha}", "formula",
    r"si $h^0_{\beta\alpha}", r"si $h'_{\beta\alpha}")
add(121, "Lemme (11.2.2.2), l. 7: '(F(M_α), h'_βα) est un système inductif de A_α-modules'",
    "h'_{βα} (prime)", "h^0_{\\beta\\alpha}", "formula",
    r"(F(M_\alpha),h^0_{\beta\alpha})", r"(F(M_\alpha),h'_{\beta\alpha})")
add(121, "'Pour la démonstration, voir Bourbaki, Alg., chap. II, 3e éd.'",
    "superscript e upright (roman), enlarged crop", "3$^e$ (math italic e)", "font",
    r"3$^e$", r"3\textsuperscript{e}", "The edition's usual form is \\textsuperscript{e}.", confidence="medium")
add(121, "same sentence: '§ 6, nº 6, cor. de la prop. 10'",
    "raised letter o (enlarged crop)", "n$^\\circ$ (a ring)", "symbol",
    r"n$^\circ$~6", r"n\textsuperscript{o}~6",
    "As the 0_IV-1 pages 156-164 findings; the edition's usual form is n\\textsuperscript{o}.", confidence="medium")
add(121, "(11.2.3), l. 2-3: 'alors ψ_1 est l'homomorphisme Ker(f_0⊗1_N)/Im(f_1⊗1_N) -> Ker(f''_0⊗1_N')/Im(f''_1⊗1_N') qui se déduit'",
    "the formula is in the running text", "displayed with \\[ ... \\]", "other",
    r"\[¶\operatorname{Ker}(f_0\otimes1_N)/\operatorname{Im}(f_1\otimes1_N)¶\to¶\operatorname{Ker}(f''_0\otimes1_{N'})/¶\operatorname{Im}(f''_1\otimes1_{N'})¶\]",
    r"$\operatorname{Ker}(f_0\otimes1_N)/\operatorname{Im}(f_1\otimes1_N)¶\to¶\operatorname{Ker}(f''_0\otimes1_{N'})/¶\operatorname{Im}(f''_1\otimes1_{N'})$",
    "Display vs inline; no connecting word is lost.")
add(121, "(11.2.3), displayed formula 'u_1⊗1 : L_0⊗_A N -> L''_0⊗_A' N' = L''_0⊗_A N.'",
    "L_0, L''_0, L''_0: subscript 0 three times, with u_1 (enlarged crop)",
    "u_1\\otimes1:L_0\\otimes_AN\\to L''_0\\otimes_{A'}N'=L''_0\\otimes_AN. (keeps the printed reading)",
    "misprint_in_print", None, None,
    "f_i : L_{i+1} -> L_i ((11.2.1.3), (11.2.1.4)), so Ker(f_0⊗1_N) lies in L_1⊗_A N and the map restricted is u_1⊗1 on "
    "L_1⊗_A N (cf. g_0⊗1_N : L_1⊗_A N -> R⊗_A N on p. 122, and u_1 : L'_1 -> L''_1). The TeX keeps the printed reading.",
    corrected=r"u_1\otimes1:L_1\otimes_AN\to L''_1\otimes_{A'}N'=L''_1\otimes_AN.")
add(121, "(11.2.3.2), end: '... -> M'⊗_A' N' -> 0'",
    "no full stop after 0 (enlarged crop)", "'\\to0.' (full stop)", "punctuation",
    r"M'\otimes_{A'}N'\to0.", r"M'\otimes_{A'}N'\to0")
add(121, "'On a d'autre part un homomorphisme de A'-modules' after (11.2.3.2)",
    "'On a d'autre part' begins a new, indented paragraph",
    "no blank line after \\end{equation}: the text continues the paragraph", "other",
    r"\end{equation}¶On a d'autre part", r"\end{equation}¶¶On a d'autre part",
    "Missing paragraph break after a display (GLOBAL_ISSUES 47).")

# ---------------------------------------------------------------- page 122
add(122, "square 'L_1 -> R, L''_1 -> R''' after 'la commutativité du diagramme'",
    "no full stop after R'' (enlarged crop)", "'R''.' (full stop)", "punctuation",
    r"L''_1\ar[r]&R''.", r"L''_1\ar[r]&R''")
add(122, "'est commutatif, ce qui résulte de la commutativité du diagrammc'",
    "'diagrammc': the last letter is a c, the same glyph (ball terminal) as the c of 'commutatif' on that line "
    "(enlarged crop); not a broken e",
    "'diagramme': silently corrected", "misprint_in_print",
    r"du diagramme", r"du diagrammc",
    "Wrong letter in the print; the diplomatic text restores it.", corrected=r"du diagramme")
add(122, "Lemme (11.2.4), last line: '(cf. (11.2.1.5)) est surjectif.'",
    "'(cf. (11.2.1.5))' roman inside the italic statement", "italic (lemma environment)", "convention",
    r"(cf. (11.2.1.5)) est surjectif.", r"\textup{(cf. (11.2.1.5))} est surjectif.", convention=6)
add(122, "proof of (11.2.4): 'l'homomorphisme v est surjectif, et il en est donc de même de v⊗1'",
    "'surjectif' in italics", "'surjectif' upright", "italics",
    r"$v$ est surjectif,", r"$v$ est \emph{surjectif},")
add(122, "same proof: '(Bourbaki, Alg. comm., chap. Ier, § 1, nº 4, ...)'",
    "raised letter o", "n$^\\circ$ (a ring)", "symbol",
    r"n$^\circ$~4", r"n\textsuperscript{o}~4", "The edition's usual form is n\\textsuperscript{o}.",
    confidence="medium")
add(122, "page break 122/123 mid-sentence: 'Utilisons pour cela | l'hypothèse que M⊗_A N est un C-module plat.'",
    "one sentence across the page break", "blank lines before and after \\oldpage[IV-3]{123} (paragraph break)",
    "other", "Utilisons pour cela¶¶", "Utilisons pour cela¶",
    "GLOBAL_ISSUES 20; the marker is in the right place. Removes the blank line before the marker; the page-123 entry "
    "removes the one after it (both needed).")

# ---------------------------------------------------------------- page 123
add(123, "start of page_123.tex: 'l'hypothèse que M⊗_A N est un C-module plat' (continues 'Utilisons pour cela')",
    "continuation of the sentence begun on p. 122", "blank line after \\oldpage[IV-3]{123}", "other",
    r"\oldpage[IV-3]{123}¶¶l'hypothèse", r"\oldpage[IV-3]{123}¶l'hypothèse",
    "With the page-122 entry (blank line before the marker).")
add(123, "l. 1: 'l'hypothèse que M⊗_A N est un C-module plat.'",
    "'plat' in italics", "'plat' upright", "italics",
    r"$C$-module plat.", r"$C$-module \emph{plat}.")
add(123, "l. 3: 'des homomorphismes de C-modules;'",
    "'modules' in italics", "'modules' upright", "italics",
    r"de $C$-modules~;", r"de $C$-\emph{modules}~;")
add(123, "second display 'T⊗_C C' -> (R⊗_A N)⊗_C C' -> Q⊗_C C' -> 0'",
    "no comma after 0 (enlarged crop)", "'\\to0,' (comma)", "punctuation",
    r"Q\otimes_CC'\to0,", r"Q\otimes_CC'\to0")
add(123, "third display '... -> (M⊗_A N)⊗_C C' -> 0'",
    "no full stop after 0 (enlarged crop)", "'\\to0.' (full stop)", "punctuation",
    r"(M\otimes_AN)\otimes_CC'\to0.", r"(M\otimes_AN)\otimes_CC'\to0")
add(123, "Lemme (11.2.5), l. 3: 'Soit p' un idéal premier de B' contenant JB'.'",
    "Fraktur J without a prime: 𝔍B' (enlarged crop; the proof has 𝔍'B'_p' with a prime)",
    "\\mathfrak J'B'", "formula",
    r"contenant $\mathfrak J'B'$", r"contenant $\mathfrak JB'$",
    "The same ideal (𝔍B' = 𝔍'B'); the diplomatic text follows the print.")
add(123, "Lemme (11.2.5), item labels a), b)",
    "a) and b) in italics, like the statement; (i), (ii) upright",
    "label=\\emph{\\alph*)} inside the italic lemma gives upright a), b)", "italics",
    r"\begin{enumerate}[label=\emph{\alph*)}]", r"\begin{enumerate}[label=\textit{\alph*)}]",
    "The (i), (ii) labels (label=\\emph{(\\roman*)}, upright) match the print. GLOBAL_ISSUES 16 and 22.")
add(123, "proof of (11.2.5), l. 1: 'Notons que dans l'hypothèse b) M'_p' est un ...'",
    "'b)' in italics", "'b)' upright", "italics", r"l'hypothèse b)", r"l'hypothèse \emph{b)}")
add(123, "same proof, l. 3: 'dans l'hypothèse a), J' est nilpotent'",
    "'a)' in italics", "'a)' upright", "italics", r"l'hypothèse a)", r"l'hypothèse \emph{a)}")
add(123, "same proof, l. 4: 'suivant que a) ou b) est vérifiée'",
    "'a)' and 'b)' in italics", "upright", "italics",
    r"suivant que a) ou b)", r"suivant que \emph{a)} ou \emph{b)}")
add(123, "same proof: 'En premier lieu, on a M'_p'⊗_A'(A'/J') = (M'⊗_A'(A'/J'))_p' = ((M⊗_A(A/J))⊗_A/J(A'/J'))_p'; l'hypothèse (i) ...'",
    "the formula is in the running text, followed by '; l'hypothèse (i)' on the same line",
    "displayed with \\[ ... \\] (the '~;' inside the display)", "other",
    r"\[¶M'_{\mathfrak p'}\otimes_{A'}(A'/\mathfrak J')¶=(M'\otimes_{A'}(A'/\mathfrak J'))_{\mathfrak p'}¶=((M\otimes_A(A/\mathfrak J))\otimes_{A/\mathfrak J}¶(A'/\mathfrak J'))_{\mathfrak p'}~;¶\]",
    r"$M'_{\mathfrak p'}\otimes_{A'}(A'/\mathfrak J')¶=(M'\otimes_{A'}(A'/\mathfrak J'))_{\mathfrak p'}¶=((M\otimes_A(A/\mathfrak J))\otimes_{A/\mathfrak J}¶(A'/\mathfrak J'))_{\mathfrak p'}$~;",
    "Display vs inline; no connecting word is lost.")
add(123, "same proof: 'or ce B'_p'-module est égal à (Tor_1^A'(M', A'/J'))_p' en vertu de la platitude'",
    "no comma before 'en vertu' (enlarged crop)", "comma after the formula", "punctuation",
    r"_{\mathfrak p'}$, en vertu", r"_{\mathfrak p'}$ en vertu")

# ---------------------------------------------------------------- page 124
add(124, "Corollaire (11.2.6.1), l. 3-4: 'On pose B_λ = B_0⊗_A_0 A_λ, M_λ = ..., A = lim A_λ, B = lim B_λ = B_0⊗_A_0 A, M = lim M_λ = M_0⊗_A_0 A = M_0⊗_B_0 B.'",
    "the five equalities are in the running text, separated by commas, ending with a full stop",
    "a gathered display of three lines (\\qquad separators)", "other",
    r"On pose¶\[¶\begin{gathered}¶B_\lambda=B_0\otimes_{A_0}A_\lambda,\qquad¶M_\lambda=M_0\otimes_{A_0}A_\lambda=M_0\otimes_{B_0}B_\lambda,\\¶A=\varinjlim A_\lambda,\qquad¶B=\varinjlim B_\lambda=B_0\otimes_{A_0}A,\\¶M=\varinjlim M_\lambda=M_0\otimes_{A_0}A=M_0\otimes_{B_0}B.¶\end{gathered}¶\]",
    r"On pose¶$B_\lambda=B_0\otimes_{A_0}A_\lambda$,¶$M_\lambda=M_0\otimes_{A_0}A_\lambda=M_0\otimes_{B_0}B_\lambda$,¶$A=\varinjlim A_\lambda$, $B=\varinjlim B_\lambda=B_0\otimes_{A_0}A$,¶$M=\varinjlim M_\lambda=M_0\otimes_{A_0}A=M_0\otimes_{B_0}B$.",
    "Display vs inline; no connecting word is lost.")
add(124, "step label 'I) Réduction au cas où les A_λ sont noethériens.'",
    "'I)' in ordinary roman weight (compare the bold Z of 'Z-algèbre' on the next line; enlarged crop)",
    "\\textbf{I)}", "font",
    r"\noindent\textbf{I)} \emph{Réduction", r"\noindent I) \emph{Réduction",
    "ega4-11-fr.tex sets all its step labels I)-VI) bold (16 times); see the final report.")
add(124, "step I): 'on peut donc déjà supposer que A_0 est noethérien.'",
    "'noethérien' in italics", "'noethérien' upright", "italics",
    r"$A_0$ est noethérien.", r"$A_0$ est \emph{noethérien}.")
add(124, "step I): 'où C_λ est une sous-A_0-algèbre de type fini de A_λ'",
    "'de type fini' in italics, 'de' included (enlarged crop)", "de \\emph{type fini}: 'de' upright", "italics",
    r"algèbre de¶\emph{type fini}", r"algèbre \emph{de¶type fini}")
add(124, "step I): 'cette fois les A_ξ sont noethériens;'",
    "'noethériens' in italics", "'noethériens' upright", "italics",
    r"sont¶noethériens~;", r"sont¶\emph{noethériens}~;")
add(124, "step I): '(Bourbaki, Alg., chap. II, 3e éd., § 6, nº 4, prop. 7)'",
    "superscript e upright (roman)", "3$^e$ (math italic e)", "font",
    r"3$^e$", r"3\textsuperscript{e}", "The edition's usual form is \\textsuperscript{e}.", confidence="medium")
add(124, "same reference: 'nº 4'",
    "raised letter o", "n$^\\circ$ (a ring)", "symbol",
    r"n$^\circ$~4", r"n\textsuperscript{o}~4", "The edition's usual form is n\\textsuperscript{o}.",
    confidence="medium")
add(124, "page break 124/125 (step I)): '... soit p un idéal premier de B, tel que M_p soit un A-module plat; il existe "
    "alors ξ∈H tel que, si p_ξ est l'image | réciproque de p dans B_ξ, ...'",
    "p. 124 ends with 'tel que M_p soit un A-module plat; il existe alors ξ∈H tel que, si p_ξ est l'image' "
    "(page_124_s4.png); p. 125 begins 'réciproque de p dans B_ξ' (page_125_s1.png); one sentence",
    "the p. 124 segment stops at 'idéal premier de $B$,'; then a blank line, \\oldpage[IV-3]{125}, a blank line and "
    "'tel que $M_{\\mathfrak p}$ ...': the marker stands about one and a half printed lines too early, inside a "
    "spurious paragraph break", "marker",
    "un idéal premier de $B$,¶¶", "un idéal premier de $B$,¶",
    "Marker move, part 1 of 2: removes the blank line before the marker (GLOBAL_ISSUES 20). Part 2 (page 125, below) "
    "moves the marker to 'l'image | réciproque' and drops the blank line after it. Apply both.")

# ---------------------------------------------------------------- page 125 (outside 120-124: second half of the move)
add(125, "start of page_125.tex: 'tel que M_p soit un A-module plat; il existe alors ξ∈H tel que, si p_ξ est l'image' "
    "(printed at the foot of p. 124)",
    "p. 125 begins 'réciproque de p dans B_ξ, (M_ξ)_p_ξ soit un A_ξ-module plat.'",
    "\\oldpage[IV-3]{125} and a blank line stand before 'tel que $M_{\\mathfrak p}$'", "marker",
    r"\oldpage[IV-3]{125}¶¶tel que $M_{\mathfrak p}$ soit un $A$-module plat~; il existe alors¶$\xi\in H$ tel que, si $\mathfrak p_\xi$ est l'image réciproque de",
    r"tel que $M_{\mathfrak p}$ soit un $A$-module plat~; il existe alors¶$\xi\in H$ tel que, si $\mathfrak p_\xi$ est l'image¶\oldpage[IV-3]{125}¶réciproque de",
    "OUTSIDE pages 120-124 (page_125.tex): part 2 of the 124/125 marker move begun by the page-124 entry. The p. 125 "
    "checker may report the same move from its side; apply only one version.")

# ---------------------------------------------------------------- checks
marker_re = re.compile(r"\\oldpage\[IV-3\]\{(\d+)\}")
src = SRC.read_text(encoding="utf-8")
cuts = [(int(m.group(1)), m.start()) for m in marker_re.finditer(src)]
segs = {}
for i, (n, s) in enumerate(cuts):
    segs[n] = src[s:cuts[i + 1][1] if i + 1 < len(cuts) else len(src)]
bad = 0
for d in F:
    fx = d["fix"]
    if not fx:
        continue
    page_txt = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    c_page = page_txt.count(fx["old"])
    c_src = segs.get(d["page"], "").count(fx["old"])
    if c_page != 1 or c_src != 1:
        bad += 1
        print("BAD", d["page"], repr(fx["old"][:60]), c_page, c_src)
# overlap check within a page: each pair of olds must not overlap in the page text
for p in sorted({d["page"] for d in F}):
    txt = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    spans = []
    for d in F:
        if d["page"] == p and d["fix"]:
            i = txt.find(d["fix"]["old"])
            spans.append((i, i + len(d["fix"]["old"]), d["where"][:40]))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            bad += 1
            print("OVERLAP", p, a, b)
json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("entries", len(F), "bad", bad, "->", OUT)
