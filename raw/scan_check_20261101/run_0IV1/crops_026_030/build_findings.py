"""Build findings_026_030.json for EGA 0_IV-1 pp. 26-30, check every fix and simulate the sequential application.
Read-only for every .tex file. "<NL>" in old/new stands for a line break (LF)."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_026_030.json"
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\IV1\native\ega4\ega0-16-fr.tex")

F = []


def add(page, where, scan, tex, kind, old, new, note="", conv=None, conf="high", corrected=None, fix=True):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old.replace("<NL>", "\n"), new=new.replace("<NL>", "\n")) if fix else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


NO = "n° printed as n with a raised o"
NOTEX = "the TeX writes 'no', which prints 'no'"
DOTS = "baseline dots '. . .' (checked on an enlarged crop)"
DASH = "long dash for the subtraction sign (bar about 40-43 px long at 300 dpi; the + and = bars on the same pages are 33-35 px)"
DASHNOTE = "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the fixes of pp. 24-25, pending the convention-7 decision."

# ---------------- page 26 ----------------
add(26, "after (16.2.2.1): 'par suite le degré de P_q(M, n) ne dépend pas ...'", "'degré' italic (crop)", "upright",
    "italics", r"par suite le degré de", r"par suite le \emph{degré} de")
add(26, "after (16.2.2.1): '... ne dépend pas de l'idéal de définition q considéré'",
    "'ne dépend pas de l'idéal de définition' italic, 'considéré' roman (crop)", "upright", "italics",
    r"ne dépend pas de l'idéal de définition", r"\emph{ne dépend pas de l'idéal de définition}")
add(26, "Lemme (16.2.2.1): '(Bourbaki, Alg. comm., chap. III, § 3, n° 1)'",
    "the reference is roman inside the italic statement, only 'Alg. comm.' italic",
    "inside the itshape lemma: the reference comes out italic and \\emph{Alg. comm.} upright", "convention",
    r"(Bourbaki,<NL>\emph{Alg.~comm.}, chap.~III, \S~3, no~1)~; alors",
    r"\textup{(Bourbaki,<NL>\emph{Alg.~comm.}, chap.~III, \S~3, no~1)}~; alors",
    "Apply before the n° fix 'no~1)' below (its 'old' is inside this one).", conv=6)
add(26, "Lemme (16.2.2.1): 'n° 1)'", NO, NOTEX, "symbol", r"no~1)", r"n\textsuperscript{o}~1)",
    "Apply after the convention-6 fix of the same reference.")
add(26, "Lemme (16.2.2.2): 'Alors le polynôme P_q(M, n) — P_q(M', n) — P_q(M'', n) a un degré'",
    "the formula is set inline in the running text", "displayed with \\[ ... \\]", "other",
    r"Alors le polynôme<NL>\[<NL>  P_{\mathfrak{q}}(M,n)-P_{\mathfrak{q}}(M',n)<NL>  -P_{\mathfrak{q}}(M'',n)<NL>\]<NL>a un degré",
    r"Alors le polynôme<NL>$P_{\mathfrak{q}}(M,n)-P_{\mathfrak{q}}(M',n)-P_{\mathfrak{q}}(M'',n)$<NL>a un degré",
    "Layout (display vs inline). Apply before the two convention-7 fixes of this formula.")
add(26, "Lemme (16.2.2.2): 'P_q(M, n) — P_q(M', n)'", DASH, "-", "convention",
    r"(M,n)-P_{\mathfrak{q}}(M',n)", r"(M,n)\setmin P_{\mathfrak{q}}(M',n)", DASHNOTE, conv=7)
add(26, "Lemme (16.2.2.2): '— P_q(M'', n)'", DASH, "-", "convention",
    r"-P_{\mathfrak{q}}(M'',n)", r"\setmin P_{\mathfrak{q}}(M'',n)",
    DASHNOTE + " Apply after the display-to-inline fix of this formula.", conv=7)
add(26, "Lemme (16.2.2.2): 'd(M') — 1'", DASH, "-", "convention", r"d(M')-1", r"d(M')\setmin 1", DASHNOTE, conv=7)
add(26, "Lemme (16.2.2.2): '≤ d(M) — 1.'", DASH, "-", "convention",
    r"d(M)-1$.<NL>\end{lemma}", r"d(M)\setmin 1$.<NL>\end{lemma}", DASHNOTE, conv=7)
add(26, "proof of (16.2.2.2): 'la filtration des M'_n = M'∩q^nM' est q-bonne'",
    "M'_n = M'∩q^nM' (prime on the last M; crop)", "M'_n=M'\\cap\\mathfrak{q}^nM' (keeps the printed reading)",
    "misprint_in_print", "", "",
    "The induced filtration M'∩q^nM is meant (Artin-Rees, the cited prop. 1; needed for "
    "long(M/q^nM) = long(M''/q^nM'') + long(M'/M'_n)). The authors' errata in EGA IV part 4 "
    "(ega4-errata-addenda-list3-fr.tex: '(0_IV, 16.2.2.2). Ligne 13 de la p. 26, remplacer M'∩q^nM' par M'∩q^nM') "
    "confirm it. The diplomatic TeX keeps the print.", corrected=r"$M'_n=M'\cap\mathfrak{q}^nM$", fix=False)
add(26, "proof of (16.2.2.2): '(Bourbaki, Alg. comm., chap. III, § 3, n° 1, prop. 1)'", NO, NOTEX, "symbol",
    r"no~1, prop.~1", r"n\textsuperscript{o}~1, prop.~1")
add(26, "proof of (16.2.2.2): 'comme long(M/q^nM) = long(M''/q^nM'') + long(M'/M'_n) le lemme résulte'",
    "formula inline in the running text, no comma after long(M'/M'_n) (crop)",
    "displayed formula ending with a comma", "punctuation",
    r"comme<NL>\[<NL>  \operatorname{long}(M/\mathfrak{q}^nM)<NL>  =\operatorname{long}(M''/\mathfrak{q}^nM'')<NL>  +\operatorname{long}(M'/M'_n),<NL>\]<NL>le lemme",
    r"comme<NL>$\operatorname{long}(M/\mathfrak{q}^nM)=\operatorname{long}(M''/\mathfrak{q}^nM'')+\operatorname{long}(M'/M'_n)$<NL>le lemme",
    "Removes the comma the print does not have and sets the formula inline as printed.")
add(26, "Théorème (16.2.3): 'M/(x_1M + . . . + x_nM)'", DOTS, "\\cdots", "symbol",
    r"x_1M+\cdots+x_nM", r"x_1M+\ldots+x_nM")
add(26, "Lemme (16.2.3.1) (ii): 'dim(M/xM) ≤ dim(M) — 1'", DASH, "-", "convention",
    r"\dim(M/xM)\leq\dim(M)-1", r"\dim(M/xM)\leq\dim(M)\setmin 1", DASHNOTE, conv=7)
add(26, "Lemme (16.2.3.1) (iii): 'P_q(_xM, n) — P_q(M/xM, n)'", DASH, "-", "convention",
    r"({}_xM,n)-P", r"({}_xM,n)\setmin P", DASHNOTE, conv=7)
add(26, "Lemme (16.2.3.1) (iii): 'est de degré ≤ d(M) — 1'", DASH, "-", "convention",
    r"degré $\leq d(M)-1$", r"degré $\leq d(M)\setmin 1$", DASHNOTE, conv=7)
add(26, "proof of (16.2.3.1) (i): 'N/(x_1N + . . . + x_mN)'", DOTS, "\\cdots", "symbol",
    r"x_1N+\cdots+x_mN", r"x_1N+\ldots+x_mN")
add(26, "proof of (16.2.3.1) (i): 'M/(xM + x_1M + . . . + x_mM)'", DOTS, "\\cdots", "symbol",
    r"x_1M+\cdots+x_mM", r"x_1M+\ldots+x_mM")
add(26, "proof of (16.2.3.1) (ii): '(0_I, 1.7.5)'", "bold 0", "$0_{\\mathrm I}$, plain 0", "convention",
    r"($0_{\mathrm I}$, 1.7.5)", r"($\mathbf{0}_{\mathrm I}$, 1.7.5)", conv=2)
add(26, "proof of (16.2.3.1) (ii): 'une longueur ≤ dim(M) — 1'", DASH, "-", "convention",
    r"longueur $\leq\dim(M)-1$", r"longueur $\leq\dim(M)\setmin 1$", DASHNOTE, conv=7)

# ---------------- page 27 ----------------
add(27, "proof of (16.2.3.1) (iii): '0 → xM → M → M/xM → 0' (end of the display)",
    "no comma after the second exact sequence (crop)", "'M/xM\\to0,' with a comma", "punctuation",
    r"M/xM\to0,<NL>\]", r"M/xM\to0<NL>\]")
add(27, "(16.2.3.2): 'On a dim(M) ≤ d(M).'", "'On a' italic (statement printed italic; crop)",
    "roman (env body is upright)", "italics", r"On a $\dim(M)\leq d(M)$.", r"\emph{On a} $\dim(M)\leq d(M)$.")
add(27, "proof of (16.2.3.2): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 4, th. 2)'", NO, NOTEX, "symbol",
    r"no~4, th.~2) et", r"n\textsuperscript{o}~4, th.~2) et")
add(27, "proof of (16.2.3.2): '(loc. cit., § 1, n° 1)'", NO, NOTEX, "symbol",
    r"no~1)~; comme", r"n\textsuperscript{o}~1)~; comme")
add(27, "proof of (16.2.3.2): 'p_0 ⊂ p_1 ⊂ . . . ⊂ p_n'", DOTS, "\\cdots", "symbol",
    r"\subset\cdots\subset", r"\subset\ldots\subset")
add(27, "proof of (16.2.3.2): 'n — 1 ≤ dim (N/xN) (16.1.7)'", DASH, "-", "convention",
    r"$n-1\leq\dim(N/xN)$", r"$n\setmin 1\leq\dim(N/xN)$", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.2): 'd(N/xN) ≤ d(N) — 1 par (16.2.3.1, (iii))'", DASH, "-", "convention",
    r"\leq d(N)-1$ par", r"\leq d(N)\setmin 1$ par", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.2): 'dim(N/xN) ≥ n — 1, donc'", DASH, "-", "convention",
    r"\geq n-1$, donc", r"\geq n\setmin 1$, donc", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.2): 'donc n — 1 ≤ d(N) — 1.' (first dash)", DASH, "-", "convention",
    r"donc $n-1\leq", r"donc $n\setmin 1\leq", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.2): 'donc n — 1 ≤ d(N) — 1.' (second dash)",
    "long dash (right end faintly printed; full extent about 40 px)", "-", "convention",
    r"d(N)-1$.", r"d(N)\setmin 1$.", DASHNOTE, conv=7)
add(27, "(16.2.3.3): 'On a d(M) ≤ s(M).'", "'On a' italic (statement printed italic)", "roman", "italics",
    r"On a $d(M)\leq s(M)$.", r"\emph{On a} $d(M)\leq s(M)$.")
add(27, "proof of (16.2.3.3): 'a = x_1A + . . . + x_nA'", DOTS, "\\cdots", "symbol",
    r"x_1A+\cdots+x_nA", r"x_1A+\ldots+x_nA")
add(27, "proof of (16.2.3.3): '(Bourbaki, Alg. comm., chap. IV, § 2, n° 5, prop. 7)'", NO, NOTEX, "symbol",
    r"no~5, prop.~7", r"n\textsuperscript{o}~5, prop.~7")
add(27, "proof of (16.2.3.3): 'x_1^{ν_1}x_2^{ν_2} . . . x_n^{ν_n}z_j'", DOTS, "\\cdots", "symbol",
    r"x_2^{\nu_2}\cdots x_n^{\nu_n}", r"x_2^{\nu_2}\ldots x_n^{\nu_n}")
add(27, "proof of (16.2.3.3): first binomial, upper entry 'm + n — 1'", DASH, "-", "convention",
    r"$r\binom{m+n-1}", r"$r\binom{m+n\setmin 1}", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.3): first binomial, lower entry 'n — 1'", DASH, "-", "convention",
    r"}{n-1}$ éléments", r"}{n\setmin 1}$ éléments", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.3): second binomial '≤ ar(m + n — 1 ...)', upper entry", DASH, "-", "convention",
    r"ar\binom{m+n-1}", r"ar\binom{m+n\setmin 1}", DASHNOTE, conv=7)
add(27, "proof of (16.2.3.3): second binomial, lower entry 'n — 1'", DASH, "-", "convention",
    r"}{n-1}$, où", r"}{n\setmin 1}$, où", DASHNOTE, conv=7)
add(27, "(16.2.3.4): 'On a s(M) ≤ dim(M).'", "'On a' italic (statement printed italic)", "roman", "italics",
    r"On a $s(M)\leq\dim(M)$.", r"\emph{On a} $s(M)\leq\dim(M)$.")
add(27, "proof of (16.2.3.4): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 4, th. 2)'", NO, NOTEX, "symbol",
    r"no~4, th.~2). Comme", r"n\textsuperscript{o}~4, th.~2). Comme")
add(27, "proof of (16.2.3.4): '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'", NO, NOTEX, "symbol",
    r"no~1, prop.~2", r"n\textsuperscript{o}~1, prop.~2")
add(27, "Corollaire (16.2.4): 'Sous les hypothèses de (16.2.3), on a'",
    "reference (16.2.3) upright inside the italic statement (crop)", "italic inside the corollary environment",
    "convention", r"Sous les hypothèses de (16.2.3), on a", r"Sous les hypothèses de \textup{(16.2.3)}, on a",
    conv=6)

# ---------------- page 28 ----------------
add(28, "proof of (16.2.4): 'M/r^nM et M̂/r̂^nM̂ sont isomorphes'", "r̂^n: the r carries a hat (crop)",
    "\\mathfrak{r}^n without hat", "formula",
    r"\widehat{M}/\mathfrak{r}^n\widehat{M}", r"\widehat{M}/\widehat{\mathfrak{r}}^n\widehat{M}")
add(28, "proof of (16.2.6): '(Bourbaki, Alg. comm., chap. II, § 3, n° 2, cor. 2 de la prop. 4)'", NO, NOTEX,
    "symbol", r"no~2, cor.~2", r"n\textsuperscript{o}~2, cor.~2")
add(28, "Proposition (16.2.7): 'B_0 = k; soient E un B-module gradué de type fini'",
    "'soient E un B-module gradué' (crop)", "soit $E$ un $B$-module gradué (silently corrected)",
    "misprint_in_print", r"soit $E$ un $B$-module gradué", r"soient $E$ un $B$-module gradué",
    "Grammatical slip of the print (plural verb, one subject E); the TeX had corrected it silently: back to the printed "
    "reading in the diplomatic text.", corrected=r"soit $E$ un $B$-module gradué")
add(28, "Proposition (16.2.7): 'de sorte (III, 2.5.4) que'",
    "reference upright inside the italic statement (crop)", "italic inside the proposition environment",
    "convention", r"de sorte (III, 2.5.4) que", r"de sorte \textup{(III, 2.5.4)} que",
    "Apply before the convention-2 fix of the same reference (its 'old' is inside this one).", conv=6)
add(28, "Proposition (16.2.7): '(III, 2.5.4)'", "bold III", "plain III", "convention",
    r"(III, 2.5.4)", r"(\textbf{III}, 2.5.4)", "Apply after the convention-6 fix of the same reference.", conv=2)
add(28, "Proposition (16.2.7): 'Φ(n) — Φ(n — 1)' (first dash)", DASH + " (small type: 34-36 px against 28 px for =)",
    "-", "convention", r"\Phi(n)-\Phi", r"\Phi(n)\setmin\Phi", DASHNOTE, conv=7)
add(28, "Proposition (16.2.7): 'Φ(n — 1)'", DASH + " (small type)", "-", "convention",
    r"\Phi(n-1)", r"\Phi(n\setmin 1)", DASHNOTE, conv=7)
BOLDN = ("Wrong-font letter of the print (GLOBAL_ISSUES 29), reproduced in the diplomatic text. Measured at 300 dpi: "
         "this n has about 140-150 dark px and a mean stroke run of 5.1-5.3 px; the ordinary subscript n's of the same "
         "paragraph ((E/E'_n)_q, E/E'_n;, (E'_n) sur E, B_n, n≥1) have 100-111 px and 3.1-3.7 px.")
add(28, "proof of (16.2.7): 'pour tout n, soit E'_n le sous-B-module'",
    "subscript n of E'_n in bold italic (enlarged crop and stroke measurement)", "$E'_n$ (ordinary italic n)",
    "misprint_in_print", r"soit $E'_n$ le sous-$B$-module", r"soit $E'_{\boldsymbol{n}}$ le sous-$B$-module",
    BOLDN + " Two further subscripts look heavier but measure in between (E/E'_n in 'artinien E/E'_n,': 126 px, "
    "4.3 px; the n of h≥n+1 under the second direct sum: 133 px, 4.6 px) and the n of Φ(n—1) in the statement is "
    "slightly heavy (156 px against 133-137 px): left unchanged, check by eye if wanted.",
    conf="medium", corrected=r"soit $E'_n$ le sous-$B$-module")
add(28, "proof of (16.2.7): 'Tout élément de B—q'", "long dash for the set difference B—q", "$B-\\mathfrak{q}$",
    "convention", r"$B-\mathfrak{q}$", r"$B\setmin\mathfrak{q}$", conv=7)
add(28, "proof of (16.2.7): '(Bourbaki, Alg., chap. VIII, § 2, n° 2, lemme 3)'", NO, NOTEX, "symbol",
    r"no~2, lemme~3", r"n\textsuperscript{o}~2, lemme~3")
add(28, "proof of (16.2.7): '(Bourbaki, Alg. comm., chap. III, § 1, n° 3, lemme 1)'", NO, NOTEX, "symbol",
    r"no~3, lemme~1", r"n\textsuperscript{o}~3, lemme~1")
add(28, "proof of (16.2.7): 'donc la filtration ((E'_n)_q) sur E_q est qB_q-bonne'",
    "subscript n of E'_n in bold italic (enlarged crop and stroke measurement: 137 px, mean run 5.1 px)",
    "$((E'_n)_{\\mathfrak{q}})$ (ordinary italic n)", "misprint_in_print",
    r"$((E'_n)_{\mathfrak{q}})$", r"$((E'_{\boldsymbol{n}})_{\mathfrak{q}})$",
    BOLDN, conf="medium", corrected=r"$((E'_n)_{\mathfrak{q}})$")
add(28, "proof of (16.2.7): '(Bourbaki, Alg. comm., chap. IV, § 3, n° 1, prop. 1)'", NO, NOTEX, "symbol",
    r"no~1, prop.~1", r"n\textsuperscript{o}~1, prop.~1")
add(28, "proof of (16.2.7): '(Bourbaki, Alg. comm., chap. III, § 1, n° 4, prop. 8)'", NO, NOTEX, "symbol",
    r"no~4,<NL>prop.~8", r"n\textsuperscript{o}~4,<NL>prop.~8")
add(28, "proof of (16.2.7): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 2, prop. 5)'", NO, NOTEX, "symbol",
    r"no~2, prop.~5", r"n\textsuperscript{o}~2, prop.~5")
add(28, "proof of (16.2.7): 'dim(E_q/t_1E_q) = d — 1'", DASH + " (small type: 35 px against 28 px for =)", "-",
    "convention", r"=d-1$", r"=d\setmin 1$", DASHNOTE, conv=7)
add(28, "heading 16.3", "'16.3. Systèmes de paramètres dans un anneau local noethérien.' ends with a full stop",
    "no full stop", "punctuation",
    r"\subsection{Systèmes de paramètres dans un anneau local noethérien}",
    r"\subsection{Systèmes de paramètres dans un anneau local noethérien.}")
add(28, "Proposition (16.3.1), label a)", "'a)' upright (crop)", "$a)$: italic a", "font",
    r"\item[$a)$]", r"\item[{\upshape a)}]", "As the label fixes on 0_I pp. 63-64.")
add(28, "Proposition (16.3.1), label b)", "'b)' upright (crop)", "$b)$: italic b", "font",
    r"\item[$b)$]", r"\item[{\upshape b)}]")
add(28, "Proposition (16.3.1) b): '(autrement dit V(p) est une composante irréductible de V(a))'",
    "'(autrement dit' roman inside the italic statement (crop)", "italic", "convention",
    r"(autrement dit", r"\textup{(autrement dit}", conv=6)
add(28, "proof of (16.3.1): 'un idéal de définition b de A_p engendré par n éléments'",
    "no comma after A_p (crop)", "'de $A_{\\mathfrak{p}}$, engendré'", "punctuation",
    r"de $A_{\mathfrak{p}}$, engendré", r"de $A_{\mathfrak{p}}$ engendré")
add(28, "proof of (16.3.1): 'avec s ∈ A—p'", "long dash for the set difference A—p", "$s\\in A-\\mathfrak{p}$",
    "convention", r"$s\in A-\mathfrak{p}$", r"$s\in A\setmin\mathfrak{p}$", conv=7)

# ---------------- page 29 ----------------
add(29, "Corollaire (16.3.2): '(« Hauptidealsatz »)'", "French guillemets « »", "``Hauptidealsatz'' (English quotes)",
    "punctuation", r"(``Hauptidealsatz'')", r"(«~Hauptidealsatz~»)",
    "Guillemets written «~...~» as elsewhere in ega0-15/ega0-17.")
add(29, "Corollaire (16.3.3), label a)", "'a)' upright (crop)", "$a)$: italic a", "font",
    r"\item[$a)$]", r"\item[{\upshape a)}]")
add(29, "Corollaire (16.3.3), label b)", "'b)' upright (crop)", "$b)$: italic b", "font",
    r"\item[$b)$]", r"\item[{\upshape b)}]")
add(29, "proof of (16.3.3): '(Bourbaki, Alg. comm., chap. II, § 1, n° 1, prop. 2)'", NO, NOTEX, "symbol",
    r"no~1, prop.~2", r"n\textsuperscript{o}~1, prop.~2")
add(29, "proof of (16.3.3): 'il résulte du « Hauptidealsatz » (16.3.2)'", "French guillemets « »",
    "``Hauptidealsatz''", "punctuation", r"du ``Hauptidealsatz''", r"du «~Hauptidealsatz~»")
add(29, "Proposition (16.3.4), display (16.3.4.1): 'dim(M/xM) ≥ dim(M) — 1'", DASH, "-", "convention",
    r"\geq\dim(M)-1.", r"\geq\dim(M)\setmin 1.", DASHNOTE, conv=7)
add(29, "Proposition (16.3.4): 'pour que les deux membres de (16.3.4.1) soient égaux'",
    "reference upright inside the italic statement (crop)", "italic", "convention",
    r"de (16.3.4.1) soient égaux, il", r"de \textup{(16.3.4.1)} soient égaux, il", conv=6)
add(29, "proof of (16.3.4): '(Bourbaki, Alg. comm., chap. IV, § 1, n° 4, th. 2)'", NO, NOTEX, "symbol",
    r"no~4, th.~2", r"n\textsuperscript{o}~4, th.~2")
add(29, "proof of (16.3.4): '(0_I, 1.7.5)'", "bold 0", "$0_{\\mathrm I}$, plain 0", "convention",
    r"($0_{\mathrm I}$, 1.7.5)", r"($\mathbf{0}_{\mathrm I}$, 1.7.5)", conv=2)
add(29, "proof of (16.3.4): 'N/(x_1N + . . . + x_nN)'", DOTS, "\\cdots", "symbol",
    r"x_1N+\cdots+x_nN", r"x_1N+\ldots+x_nN")
add(29, "proof of (16.3.4): 'M/(xM + x_1M + . . . + x_nM)'", DOTS, "\\cdots", "symbol",
    r"x_1M+\cdots+x_nM", r"x_1M+\ldots+x_nM")

# ---------------- page 30 ----------------
add(30, "proof of (16.3.4), top of p. 30: 'dim(M/xM) = dim(M) — 1, aucun'", DASH, "-", "convention",
    r"\dim(M)-1$, aucun", r"\dim(M)\setmin 1$, aucun", DASHNOTE, conv=7)
add(30, "Corollaire (16.3.5): 'Avec les notations de (16.3.4), pour tout idéal'",
    "reference upright inside the italic statement (crop)", "italic", "convention",
    r"Avec les notations de (16.3.4),", r"Avec les notations de \textup{(16.3.4)},", conv=6)
add(30, "Corollaire (16.3.5): 'la relation dim(M/xM) = dim(M) — 1 entraîne'", DASH, "-", "convention",
    r"\dim(M)-1$ entraîne", r"\dim(M)\setmin 1$ entraîne", DASHNOTE, conv=7)
add(30, "Corollaire (16.3.5): 'dim(N/xN) = dim(N) — 1.'", DASH, "-", "convention",
    r"\dim(N)-1$.", r"\dim(N)\setmin 1$.", DASHNOTE, conv=7)
add(30, "proof of (16.3.5): 'dim(N/xN) = dim(N) — 1 en vertu de (16.3.4)'", DASH, "-", "convention",
    r"\dim(N)-1$ en vertu", r"\dim(N)\setmin 1$ en vertu", DASHNOTE, conv=7)
add(30, "Définition (16.3.6): 'On appelle système de paramètres pour M tout système'",
    "the whole statement italic, no change of face at 'système de paramètres pour M' (crop)",
    "\\emph{...} inside the italic definition prints these words upright", "convention",
    r"\emph{système de<NL>paramètres pour $M$}", r"système de<NL>paramètres pour $M$",
    "FIX_POLICY 2.6: drop \\emph where the print shows no change of face.", conv=6)
add(30, "Définition (16.3.6): 'M/(x_1M + . . . + x_nM)'", DOTS, "\\cdots", "symbol",
    r"tel que $M/(x_1M+\cdots+x_nM)$", r"tel que $M/(x_1M+\ldots+x_nM)$")
add(30, "Proposition (16.3.7): '... M un A-module de type fini.' / 'On a alors'",
    "'On a alors' begins a new indented paragraph (crop; indent measured)", "same paragraph", "other",
    r"fini. On a alors", r"fini.<NL><NL>On a alors", "Paragraph break of the print.")
add(30, "Proposition (16.3.7), display (16.3.7.1): 'dim(M/(x_1M + . . . + x_kM))'", DOTS, "\\cdots", "symbol",
    r"\dim(M/(x_1M+\cdots+x_kM))", r"\dim(M/(x_1M+\ldots+x_kM))")
add(30, "Proposition (16.3.7), display (16.3.7.1): '≥ dim(M) — k'", DASH, "-", "convention",
    r"\dim(M)-k", r"\dim(M)\setmin k", DASHNOTE, conv=7)
add(30, "Proposition (16.3.7): 'En outre, pour que les deux membres de (16.3.7.1) ...' after the display",
    "'En outre' is indented: a new paragraph after (16.3.7.1) (indent measured: 510 px against the 398 px margin; "
    "on p. 29 the same phrase after (16.3.4.1) is not indented)", "continues the paragraph after \\end{equation}",
    "other", r"\end{equation}<NL>En outre, pour", r"\end{equation}<NL><NL>En outre, pour", "Paragraph break of the print.")
add(30, "Proposition (16.3.7): 'pour que les deux membres de (16.3.7.1) soient égaux'",
    "reference upright inside the italic statement (crop)", "italic", "convention",
    r"de (16.3.7.1) soient égaux, il", r"de \textup{(16.3.7.1)} soient égaux, il", conv=6)
add(30, "proof of (16.3.7): 'système de paramètres pour M/(x_1M + . . . + x_kM)'", DOTS, "\\cdots", "symbol",
    r"pour $M/(x_1M+\cdots+x_kM)$", r"pour $M/(x_1M+\ldots+x_kM)$")
add(30, "proof of (16.3.7): 'M/(x_1M + . . . + x_kM + x_{k+1}M + . . . + x_nM)' (first dots)", DOTS, "\\cdots",
    "symbol", r"x_1M+\cdots+x_kM+x_{k+1}M", r"x_1M+\ldots+x_kM+x_{k+1}M")
add(30, "proof of (16.3.7): 'M/(x_1M + . . . + x_kM + x_{k+1}M + . . . + x_nM)' (second dots)", DOTS, "\\cdots",
    "symbol", r"x_{k+1}M+\cdots+x_nM", r"x_{k+1}M+\ldots+x_nM")
add(30, "proof of (16.3.7): 'N = M/(x_1M + . . . + x_kM)'", DOTS, "\\cdots", "symbol",
    r"$N=M/(x_1M+\cdots+x_kM)$", r"$N=M/(x_1M+\ldots+x_kM)$")
add(30, "proof of (16.3.7): 'N/(x_{k+1}N + . . . + x_nN)'", DOTS, "\\cdots", "symbol",
    r"x_{k+1}N+\cdots+x_nN", r"x_{k+1}N+\ldots+x_nN")
add(30, "proof of (16.3.7): 'dim(N) ≤ n — k'", DASH, "-", "convention", r"n-k$", r"n\setmin k$", DASHNOTE, conv=7)

# ---------------- checks ----------------
ok = True
pages = {}
for n in range(26, 31):
    pages[n] = (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
for x in F:
    if x["fix"]:
        c = pages[x["page"]].count(x["fix"]["old"])
        if c != 1:
            ok = False
            print("PAGE-FILE COUNT", c, x["page"], repr(x["fix"]["old"]))

# simulate the coordinator's sequential application on the current release segments
rel = REL.read_text(encoding="utf-8")
marker = re.compile(r"\\oldpage\[0\\textsubscript\{IV-1\}\]\{(\d+)\}")


def seg(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            return s, (cuts[i + 1][1] if i + 1 < len(cuts) else len(t))
    raise KeyError(page)


sim = rel
for x in F:
    if not x["fix"]:
        continue
    s, e = seg(sim, x["page"])
    sg = sim[s:e]
    c = sg.count(x["fix"]["old"])
    if c != 1:
        ok = False
        print("RELEASE SEQ COUNT", c, x["page"], repr(x["fix"]["old"]))
        continue
    sim = sim[:s] + sg.replace(x["fix"]["old"], x["fix"]["new"]) + sim[e:]

# the release segment (before any of these fixes) should equal the page file apart from the first comment line
for n in range(26, 31):
    s, e = seg(rel, n)
    a = rel[s:e].rstrip("\n")
    b = pages[n].split("\n", 1)[1].rstrip("\n")
    if a != b:
        print("segment differs from page file:", n, len(a), len(b))
        import difflib
        for ln in list(difflib.unified_diff(b.split("\n"), a.split("\n"), lineterm="", n=0))[:12]:
            print("   ", ln)

cnt = {}
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt.setdefault(x["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(cnt, "total", len(F), "ok" if ok else "PROBLEMS")
if ok:
    OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
