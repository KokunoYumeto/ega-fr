# Builds findings_201_205.json and checks that every fix's "old" occurs exactly once in its page file.
# In the strings below, the pilcrow stands for a line break (LF).
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_201_205.json"
NL = "¶"


def F(page, where, scan, tex, kind, convention, confidence, old, new, note="", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


REF6 = "Reference upright in the print inside the italic statement."
LAB6 = "Label printed upright; \\item[..] comes out italic inside the italic statement environment."
REM = "Judged with the remark body as roman (document-wide remark item)."
C7 = ("Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the fixes of pp. 24-37, pending the "
      "convention-7 decision.")

findings = [
    # ---------------- p. 201 ----------------
    F(201, "top of p. 201: '... t∈m, on a | D(ty)=tD(y)=0 puisque' (the sentence continues from p. 200)",
      "no paragraph break: the line starts at the margin without indent (strip s1)",
      "blank line after \\oldpage{201}: paragraph break", "other", None, "high",
      r"\oldpage[0\textsubscript{IV-1}]{201}¶¶$D(ty)", r"\oldpage[0\textsubscript{IV-1}]{201}¶$D(ty)",
      "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). The source has no blank line "
      "before the marker (ega0-22-fr.tex: '$t\\in\\mathfrak m$, on a' directly above it), so this edit alone "
      "completes the repair; \\oldpage ends with \\ignorespaces."),
    F(201, "Remarque (22.4.8), last paragraph: 'le critère (22.4.7), où l'on remplace'",
      "(22.4.7) upright inside the italic emphasis (crop p201_emph)", "(22.4.7) inside \\emph{...}: italic",
      "convention", 6, "high", r"critère (22.4.7), où", r"critère \textup{(22.4.7)}, où",
      "Reference upright in the print inside the emphasised clause."),
    F(201, "Remarque (22.4.8), last paragraph: '(autrement dit, que p.1∈m dans A)'",
      "p.1 with a baseline period (crop p201_p1, 2.5x)", "p\\cdot1 (centred dot)",
      "symbol", None, "high", r"$p\cdot1\in\mathfrak m$ dans", r"$p.1\in\mathfrak m$ dans",
      "GLOBAL_ISSUES 65 (ega0-22 p\\cdot1 to check); same form as the fixes on pp. 111-115."),
    F(201, "Remarque (22.4.8), last paragraph: 'de la forme plus générale (22.4.4.1) : en effet'",
      "(22.4.4.1) upright after the italic clause (crop p201_emph)", "(22.4.4.1) inside \\emph{...}: italic",
      "convention", 6, "high", r"(22.4.4.1)}~:", r"\textup{(22.4.4.1)}}~:",
      "Reference upright in the print inside the emphasised clause."),
    F(201, "heading 22.5: 'Algèbres géométriquement régulières et algèbres formellement lisses.'",
      "final full stop", "no full stop", "punctuation", None, "high",
      r"\subsection{Algèbres géométriquement régulières et algèbres formellement lisses}",
      r"\subsection{Algèbres géométriquement régulières et algèbres formellement lisses.}",
      "GLOBAL_ISSUES 43/58 (no \\subsection title in ega0-14 to ega0-23 has the printed full stop)."),
    F(201, "Proposition (22.5.1): 'm (resp. m') l'idéal maximal'",
      "'(resp. m')' roman inside the italic statement (crop p201_prop)", "italic (proposition environment)",
      "convention", 6, "high", r"(resp. $\mathfrak m'$) l'idéal", r"\textup{(resp. $\mathfrak m'$)} l'idéal"),
    F(201, "Proposition (22.5.1): 'l'idéal maximal de A (resp. A'),'",
      "'(resp. A')' roman inside the italic statement (crop p201_prop)", "italic (proposition environment)",
      "convention", 6, "high", r"(resp. $A'$),", r"\textup{(resp. $A'$)},"),
    F(201, "Proposition (22.5.1): 'K=A/m (resp. K'=A'/m') son corps résiduel'",
      "'(resp. K'=A'/m')' roman inside the italic statement (crop p201_prop)", "italic (proposition environment)",
      "convention", 6, "high", r"(resp. $K'=A'/\mathfrak m'$) son", r"\textup{(resp. $K'=A'/\mathfrak m'$)} son"),
    F(201, "heading of Remarques (22.5.2)", "'Remarques (22.5.2). —' (plural)",
      "\\begin{remark}[22.5.2] prints 'Remarque (22.5.2)'", "word", None, "high",
      r"\begin{remark}[22.5.2]", r"\begin{remarks}[22.5.2]",
      "Apply together with the \\end{remark} -> \\end{remarks} fix on p. 202, where this remark ends "
      "(as EGA II pp. 175-176)."),
    F(201, "Remarques (22.5.2) (i): 'comme m²A'⊂m'², m'_1=m'/mA' est l'idéal maximal de A'_1'",
      "m'/mA': no exponent on the second m (4x crop p201_mA_4x; m²A' at the start of the same line has it)",
      "\\mathfrak m'/\\mathfrak m^2A': silent correction", "misprint_in_print", None, "high",
      r"\mathfrak m'_1=\mathfrak m'/\mathfrak m^2A'", r"\mathfrak m'_1=\mathfrak m'/\mathfrak mA'",
      "A'_1=A'/m²A' (same sentence), so its maximal ideal is m'/m²A'; the isomorphism m'_1/m'_1²≅m'/m'² "
      "then follows from m²A'⊂m'². The fix restores the printed reading.",
      corrected=r"\mathfrak m'_1=\mathfrak m'/\mathfrak m^2A'"),
    F(201, "Remarques (22.5.2) (i): 'de la structure de la A_1-algèbre A'_1'",
      "'algèbre' italic (crop p201_alg)", "upright", "italics", None, "high",
      r"$A_1$-algèbre $A'_1$", r"$A_1$-\emph{algèbre} $A'_1$", REM),
    # ---------------- p. 202 ----------------
    F(202, "Remarques (22.5.2) (iii): 'comme A' est supposé être un anneau local, il en est de même'",
      "'local' italic (crop p202_local)", "upright", "italics", None, "high",
      r"un anneau local, il en est", r"un anneau \emph{local}, il en est", REM),
    F(202, "Remarques (22.5.2) (iii): 'l'on a, sous les hypothèses de (22.4.1)' before (22.5.2.2)",
      "no comma after (22.4.1) (crop p202_comma)", "'(22.4.1),'", "punctuation", None, "high",
      r"sous les hypothèses de (22.4.1),", r"sous les hypothèses de (22.4.1)"),
    F(202, "end of Remarques (22.5.2)", "plural heading 'Remarques (22.5.2)' (p. 201)", "\\end{remark}",
      "word", None, "high", r"\end{enumerate}¶\end{remark}", r"\end{enumerate}¶\end{remarks}",
      "Apply together with the \\begin{remark}[22.5.2] -> \\begin{remarks}[22.5.2] fix on p. 201."),
    F(202, "Corollaire (22.5.3) (ii): 'les classes ξ_i mod. m² des éléments'",
      "'mod.' roman inside the italic statement (crop p202_mod)", "italic (corollary environment)",
      "convention", 6, "high", r"$\xi_i$ mod.~$\mathfrak m^2$", r"$\xi_i$ \textup{mod.}~$\mathfrak m^2$"),
    F(202, "Théorème (22.5.4), display (22.5.4.1): '... c_{ik}T_i^{p-k} — f_i'",
      "long dash before f_i: 39 px against 34 px for = and 36 px for + in the same display (crops p202_dash, "
      "p202_sum_hi)", "-f_i", "convention", 7, "high", r"T_i^{p-k}-f_i", r"T_i^{p-k}\setmin f_i",
      C7 + " The small-type minus signs of p-1, p-k here and d_i-k in (22.5.3.1) measure 21-22 px against "
      "20 px for the small = (like the ordinary minus of p. 21): ordinary minus signs, as in the TeX."),
    F(202, "Théorème (22.5.4), label a)", "upright 'a)' (crop p202_labels)", "\\item[a)] italic", "convention", 6,
      "high", r"\item[a)] $B$ est", r"\item[\textup{a)}] $B$ est", LAB6),
    F(202, "Théorème (22.5.4), label b)", "upright 'b)' (crop p202_labels)", "\\item[b)] italic", "convention", 6,
      "high", r"\item[b)] les éléments", r"\item[\textup{b)}] les éléments", LAB6),
    F(202, "Théorème (22.5.4), label c)", "upright 'c)' (crop p202_labels)", "\\item[c)] italic", "convention", 6,
      "high", r"\item[c)] si", r"\item[\textup{c)}] si", LAB6),
    F(202, "Théorème (22.5.4) c): 'Ξ_{B_(K)/K}=Ξ_{B'_(K)/K} (22.4.5), l'homomorphisme caractéristique'",
      "(22.4.5) upright (crop p202_labels)", "italic", "convention", 6, "high",
      r"(22.4.5), l'homomorphisme", r"\textup{(22.4.5)}, l'homomorphisme", REF6),
    F(202, "Théorème (22.5.4) c): '→m/m² (22.4.6.2) est injectif'",
      "(22.4.6.2) upright (crop p202_labels)", "italic", "convention", 6, "high",
      r"(22.4.6.2) est injectif", r"\textup{(22.4.6.2)} est injectif", REF6),
    # ---------------- p. 203 ----------------
    F(203, "(22.5.5), line 2: 'k' une extension radicielle finie de k'",
      "'radicielle' roman, only 'finie' italic (crop p203_radic)", "\\emph{radicielle finie}", "italics", None,
      "high", r"\emph{radicielle finie}", r"radicielle \emph{finie}"),
    F(203, "(22.5.5), display after '(21.3.2.2)': 'π_{k'/k} : Θ_{k'/k} → Ω¹_K'",
      "Ω¹ with a roman capital K subscript (4x crop p203_pi; the π and Θ subscripts are italic k)",
      "\\Omega^1_k: silent correction", "misprint_in_print", None, "high",
      r"\Theta_{k'/k}\longrightarrow\Omega^1_k", r"\Theta_{k'/k}\longrightarrow\Omega^1_K",
      "(21.3.2.2) defines π_{B/A}: Θ_{B/A} → Ω¹_{A/A^p}=Ω¹_A for the smaller ring A (B^p⊂A); here A=k, B=k', "
      "so the target is Ω¹_k, and the text below describes the image in Ω¹_k⊗_k K (printed with italic k). "
      "The fix restores the printed reading.",
      corrected=r"\pi_{k'/k}:\Theta_{k'/k}\longrightarrow\Omega^1_k"),
    F(203, "(22.5.5), display (22.5.5.2): 'Θ_{A'_(K)/K} → Ω¹_K⊗_k K'",
      "Ω¹ with a roman capital K subscript; the ⊗ subscript is italic k (4x crop p203_inj)",
      "\\Omega^1_k\\otimes_kK: silent correction", "misprint_in_print", None, "high",
      r"\longrightarrow\Omega^1_k\otimes_kK", r"\longrightarrow\Omega^1_K\otimes_kK",
      "The injection is π_{k'/k}⊗1_K: Θ_{k'/k}⊗_k K → Ω¹_k⊗_k K; the explicit description after the display "
      "sends to 'd_k(x'^p)⊗1_K de Ω¹_k⊗_k K' (crop p203_text, italic k). The fix restores the printed reading.",
      corrected=r"\Theta_{A'_{(K)}/K}\longrightarrow\Omega^1_k\otimes_kK"),
    F(203, "Lemme (22.5.6): 'Avec les notations de (22.5.5) :'", "(22.5.5) upright", "italic (lemma environment)",
      "convention", 6, "high", r"notations de (22.5.5)~:", r"notations de \textup{(22.5.5)}~:", REF6),
    F(203, "Lemme (22.5.6) (i): 'π_{A'_(K)/K} (21.3.2.2) s'identifie'", "(21.3.2.2) upright", "italic",
      "convention", 6, "high", r"(21.3.2.2) s'identifie", r"\textup{(21.3.2.2)} s'identifie", REF6),
    F(203, "Lemme (22.5.6) (i): 's'identifie par (22.5.5.2) à'", "(22.5.5.2) upright", "italic",
      "convention", 6, "high", r"par (22.5.5.2) à", r"par \textup{(22.5.5.2)} à", REF6),
    F(203, "Lemme (22.5.6) (ii): 'χ'_{A'_1/A_1} (22.4.6.2) s'identifie'", "(22.4.6.2) upright", "italic",
      "convention", 6, "high", r"(22.4.6.2) s'identifie", r"\textup{(22.4.6.2)} s'identifie", REF6),
    F(203, "Lemme (22.5.6) (ii): 'V=m/m² (20.6.24) à (Θ⊗K)∩Υ'", "(20.6.24) upright", "italic",
      "convention", 6, "high", r"\mathfrak m^2$¶  (20.6.24) à", r"\mathfrak m^2$¶  \textup{(20.6.24)} à", REF6),
    F(203, "proof of (22.5.6) (ii): 'Θ_{A'_(K)/K} s'identifie à Θ_{(A'_1)_(K)/K}, et la vérification'",
      "comma after Θ_{(A'_1)_(K)/K} (crop p203_comma)", "no comma", "punctuation", None, "high",
      r"$\Theta_{(A'_1)_{(K)}/K}$ et la vérification", r"$\Theta_{(A'_1)_{(K)}/K}$, et la vérification"),
    F(203, "Proposition (22.5.7): 'χ_{A/k} : Υ_{K/k}→V (20.6.24) à'", "(20.6.24) upright", "italic",
      "convention", 6, "high", r"V$ (20.6.24) à", r"V$ \textup{(20.6.24)} à", REF6),
    F(203, "end of p. 203 / top of p. 204: '... isomorphe au quotient de l'anneau de | polynômes k[T_1, ..., T_r]'",
      "one sentence across the page break (no indent at the top of p. 204)",
      "blank line before \\oldpage{204}: paragraph break", "other", None, "high",
      r"quotient de l'anneau de¶¶", r"quotient de l'anneau de¶",
      "Spurious paragraph break mid-sentence (GLOBAL_ISSUES 20); the blank line is the last line of the p. 203 "
      "segment. Apply together with the p. 204 entry that removes the blank line after the marker (both blank "
      "lines must go)."),
    # ---------------- p. 204 ----------------
    F(204, "top of p. 204: 'polynômes k[T_1, ..., T_r] par l'idéal ...' continues the sentence of p. 203",
      "no indent: continuation line", "blank line after \\oldpage{204}: paragraph break", "other", None, "high",
      r"\oldpage[0\textsubscript{IV-1}]{204}¶¶polynômes", r"\oldpage[0\textsubscript{IV-1}]{204}¶polynômes",
      "Spurious paragraph break (GLOBAL_ISSUES 20); apply together with the p. 203 entry that removes the blank "
      "line before the marker."),
    F(204, "proof of (22.5.7), line 1: 'F_i=T_i^p — b_i (1≤i≤r)'",
      "long dash: 41 px against 34-35 px for the = of the same formula (crop p204_dash)", "T_i^p-b_i",
      "convention", 7, "high", r"$F_i=T_i^p-b_i$", r"$F_i=T_i^p\setmin b_i$", C7),
    F(204, "Théorème (22.5.8), label a)", "upright 'a)' (crop p204_a_label)", "\\item[a)] italic", "convention", 6,
      "high", r"\item[a)] $A$ est une", r"\item[\textup{a)}] $A$ est une", LAB6),
    F(204, "Théorème (22.5.8), label b)", "upright 'b)' (crop p204_bprime_label)", "\\item[b)] italic", "convention",
      6, "high", r"\item[b)] $A$ est géométriquement", r"\item[\textup{b)}] $A$ est géométriquement", LAB6),
    F(204, "Théorème (22.5.8), label b')", "upright 'b')' (crop p204_bprime_label)", "\\item[b')] italic",
      "convention", 6, "high", r"\item[b')] Pour toute", r"\item[\textup{b')}] Pour toute", LAB6),
    F(204, "Théorème (22.5.8) b'): 'A'=A⊗_K k' est un anneau régulier'",
      "⊗ with a roman capital K subscript (3x crop p204_otimesK)", "\\otimes_k: silent correction",
      "misprint_in_print", None, "high", r"A'=A\otimes_kk'", r"A'=A\otimes_Kk'",
      "A is a k-algebra and k' an extension of k: A'=A⊗_k k', as in (22.5.5), (22.5.7) and the proof of "
      "(22.5.9) ('A⊗_k k'', italic k). The fix restores the printed reading.",
      corrected=r"A'=A\otimes_kk'"),
    F(204, "proof of (22.5.8): 'Le fait que a) implique b) n'est autre que (19.6.5), et b) entraîne trivialement b').'",
      "the four labels italic (crop p204_proof1)", "upright", "italics", None, "high",
      r"Le fait que a) implique b) n'est autre que (19.6.5), et b) entraîne¶trivialement b').",
      r"Le fait que \emph{a)} implique \emph{b)} n'est autre que (19.6.5), et \emph{b)} entraîne¶"
      r"trivialement \emph{b')}."),
    F(204, "proof of (22.5.8): 'Montrons que b') entraîne'", "'b')' italic (crop p204_proof1)", "upright",
      "italics", None, "high", r"Montrons que b') entraîne", r"Montrons que \emph{b')} entraîne"),
    F(204, "proof of (22.5.8): 'puisque b') entraîne d'abord'", "'b')' italic (crop p204_proof1)", "upright",
      "italics", None, "high", r"puisque b') entraîne", r"puisque \emph{b')} entraîne"),
    F(204, "proof of (22.5.8): 'que la condition b') entraîne que χ_{A/k} est injectif'",
      "'b')' italic (crop p204_proof2)", "upright", "italics", None, "high",
      r"la condition b') entraîne", r"la condition \emph{b')} entraîne"),
    F(204, "proof of (22.5.9): 'avec les notations de (22.5.8, b'))'", "'b')' italic (crop p204_cor)", "upright",
      "italics", None, "high", r"(22.5.8, b'))", r"(22.5.8, \emph{b')})"),
    F(204, "heading of Remarques (22.5.10)", "'Remarques (22.5.10). —' (plural; crop p204_rem)",
      "\\begin{remark}[22.5.10] prints 'Remarque (22.5.10)'", "word", None, "high",
      r"\begin{remark}[22.5.10]", r"\begin{remarks}[22.5.10]",
      "Apply together with the \\end{remark} -> \\end{remarks} fix on p. 205, where this remark ends."),
    F(204, "Remarques (22.5.10) (i): 'dans la condition b'), on se borne'", "'b')' italic (crop p204_rem)",
      "upright", "italics", None, "high", r"condition b'), on se borne", r"condition \emph{b')}, on se borne", REM),
    F(204, "Remarques (22.5.10) (i): 'pour toutes ces extensions k''", "'toutes' italic (crop p204_rem)",
      "upright", "italics", None, "high", r"pour toutes ces extensions", r"pour \emph{toutes} ces extensions", REM),
    F(204, "Remarques (22.5.10) (i): 'Υ_{K/k}∩(Θ_{k'/k}⊗_k K)=0, bien que Υ_{K/k}≠0'",
      "'bien que' italic (crop p204_rem)", "upright", "italics", None, "high",
      r"=0$, bien que", r"=0$, \emph{bien que}",
      REM + " The later 'bien que K soit une extension inséparable' is upright in the print, as in the TeX."),
    F(204, "Remarques (22.5.10) (i): 'pour h l'homomorphisme nul'", "'nul' italic (crop p204_rem2)", "upright",
      "italics", None, "high", r"l'homomorphisme nul~;", r"l'homomorphisme \emph{nul}~;", REM),
    F(204, "Remarques (22.5.10) (i), last line: 'A⊗_k k' est un anneau régulier pour toute extension monogène'",
      "'régulier' italic (crop p204_rem2)", "upright", "italics", None, "high",
      r"anneau régulier pour toute", r"anneau \emph{régulier} pour toute", REM),
    # ---------------- p. 205 ----------------
    F(205, "end of Remarques (22.5.10)", "plural heading 'Remarques (22.5.10)' (p. 204)", "\\end{remark}",
      "word", None, "high", r"\end{enumerate}¶\end{remark}", r"\end{enumerate}¶\end{remarks}",
      "Apply together with the \\begin{remark}[22.5.10] -> \\begin{remarks}[22.5.10] fix on p. 204."),
    F(205, "heading 22.6: 'Critère jacobien de Zariski.'", "final full stop", "no full stop", "punctuation", None,
      "high", r"\subsection{Critère jacobien de Zariski}", r"\subsection{Critère jacobien de Zariski.}",
      "GLOBAL_ISSUES 43/58."),
    F(205, "Théorème (22.6.1): 'faisant de B une A-algèbre formellement lisse, J un idéal'",
      "'formellement lisse' roman inside the italic statement, 'algèbre' italic (crop p205_thm)",
      "italic (theorem environment)", "convention", 6, "high",
      r"$A$-algèbre formellement lisse, $\mathfrak J$", r"$A$-algèbre \textup{formellement lisse}, $\mathfrak J$",
      "Roman words inside the italic statement."),
    F(205, "Théorème (22.6.1): 'l'homomorphisme canonique (cf. (20.5.11.2))'",
      "'(cf. (20.5.11.2))' upright (crop p205_cf)", "italic", "convention", 6, "high",
      r"canonique (cf. (20.5.11.2))", r"canonique \textup{(cf. (20.5.11.2))}", REF6),
    F(205, "Théorème (22.6.1), end: 'soit formellement inversible à gauche'",
      "italic like the rest of the statement, no change of face (crop p205_inv)",
      "\\emph{...} inside the italic theorem: upright", "convention", 6, "high",
      r"soit \emph{formellement inversible à gauche}", r"soit formellement inversible à gauche",
      "Printed italic words left upright: \\emph dropped inside the italic environment (FIX_POLICY 2.6)."),
    F(205, "Théorème (22.6.1), end: '(cf. (19.1.5)).'", "'(cf. (19.1.5))' upright (crop p205_inv)", "italic",
      "convention", 6, "high", r"(cf. (19.1.5)).", r"\textup{(cf. (19.1.5))}.", REF6),
    F(205, "proof of (22.6.1): 'Exalcotop_A(C, L)→Exalcotop_A(B, L) est injectif'",
      "'injectif' italic (crop p205_inj)", "upright", "italics", None, "high",
      r"est injectif, et le théorème", r"est \emph{injectif}, et le théorème"),
    F(205, "Corollaire (22.6.2): 'étant celles de (22.6.1), supposons'", "(22.6.1) upright (crop p205_cor)",
      "italic", "convention", 6, "high", r"celles de (22.6.1), supposons", r"celles de \textup{(22.6.1)}, supposons",
      REF6),
    F(205, "Corollaire (22.6.2): 'déduite de celle de B (19.0)'", "(19.0) upright (crop p205_cor)", "italic",
      "convention", 6, "high", r"$B$ (19.0)", r"$B$ \textup{(19.0)}", REF6),
    F(205, "Corollaire (22.6.2): '(on notera que ces deux conditions ... topologie J-préadique)'",
      "the parenthesis is roman with 'noethérien', 'préadique', 'préadique' italic; 0 of (0_I, 7.3.2) bold "
      "(crop p205_cor)", "the whole parenthesis italic, plain 0", "convention", 6, "high",
      r"(on notera que ces deux conditions sont vérifiées lorsque¶$B$ est noethérien et sa topologie préadique "
      r"($0_{\mathrm I}$, 7.3.2), ou si la¶topologie de $B$ est la topologie $\mathfrak J$-préadique)",
      r"\textup{(on notera que ces deux conditions sont vérifiées lorsque¶$B$ est \emph{noethérien} et sa "
      r"topologie \emph{préadique} ($\mathbf{0}_{\mathrm I}$, 7.3.2), ou si la¶topologie de $B$ est la topologie "
      r"$\mathfrak J$-\emph{préadique})}",
      "Both halves of convention 6 in one edit; the same edit sets the bold 0 of (0_I, 7.3.2) (convention 2), "
      "so that no second edit overlaps it."),
    F(205, "Corollaire (22.6.2) (i), label a)", "upright 'a)' (crop p205_ab)", "\\item[a)] italic", "convention", 6,
      "high", r"\item[a)] $C$ est une", r"\item[\textup{a)}] $C$ est une", LAB6),
    F(205, "Corollaire (22.6.2) (i), label b)", "upright 'b)' (crop p205_ab)", "\\item[b)] italic", "convention", 6,
      "high", r"\item[b)] Pour tout", r"\item[\textup{b)}] Pour tout", LAB6),
    F(205, "Corollaire (22.6.2) (i) b): '(autrement dit un isomorphisme sur un facteur direct de Ω¹_{B/A}⊗_B B_λ)'",
      "the parenthesis is roman (crop p205_end)", "italic", "convention", 6, "high",
      r"(autrement dit un isomorphisme sur un facteur direct de¶    $\Omega^1_{B/A}\otimes_BB_\lambda$)",
      r"\textup{(autrement dit un isomorphisme sur un facteur direct de¶    $\Omega^1_{B/A}\otimes_BB_\lambda$)}",
      "Roman words inside the italic statement."),
    F(205, "Corollaire (22.6.2) (ii): 'soit préadmissible (0_I, 7.1.2) et'",
      "upright reference with a bold 0 (crop p205_end)", "italic, plain 0", "convention", 2, "high",
      r"préadmissible ($0_{\mathrm I}$, 7.1.2)", r"préadmissible \textup{($\mathbf{0}_{\mathrm I}$, 7.1.2)}",
      "Also convention 6 (upright reference in the italic statement); one edit, as on p. 7."),
    F(205, "end of p. 205 / top of p. 206: '... soit préadmissible (0_I, 7.1.2) et | soit L un idéal de "
      "définition de C'", "one sentence across the page break", "blank line before \\oldpage{206}: paragraph break",
      "other", None, "high", r" et¶¶", r" et¶",
      "Spurious paragraph break mid-sentence (GLOBAL_ISSUES 20); the blank line is the last line of the p. 205 "
      "segment. The source also has a blank line after \\oldpage{206} (ega0-22-fr.tex, in the p. 206 segment, "
      "outside pp. 201-205): both must go, so apply together with the p. 206 fix for it."),
]

# ---- checks ----
bad = 0
texts = {}
for f in findings:
    p = f["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    fx = f["fix"]
    if fx is None:
        continue
    n = texts[p].count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", p, n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO-OP", p, repr(fx["old"]))
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        bad += 1
        print("MISSING corrected", p)
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
from collections import Counter
c = Counter()
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in sorted({f["page"] for f in findings}):
    print(p, "normal", c[(p, "normal")], "convention", c[(p, "convention")], "misprint", c[(p, "misprint")])
print("findings", len(findings), "problems", bad)
