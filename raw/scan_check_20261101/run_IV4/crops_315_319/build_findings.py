"""Build findings_315_319.json and check every fix's 'old' against the page files.

Each 'old' must occur exactly once in its page_NNN.tex (CRLF normalised to LF), except
entries marked AFTER, whose 'old' is checked against the page text after the named
earlier fixes have been applied.
"""
import json

BASE = r"user\Documents\ega_scan_check_20261101\run_IV4"
OUT = BASE + r"\findings_315_319.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None, after=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_after"] = after
    F.append(d)


# ---------------------------------------------------------------- p. 315
add(315, "Corollaire (21.13.3), l. 1: 'U = X — Y'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""$U=X-Y$,
$j:U\to X$ l'injection canonique. Les""",
    r"""$U=X\setmin Y$,
$j:U\to X$ l'injection canonique. Les""")
add(315, "(21.13.3) a): 'le foncteur restriction ℰ ⇝ ℰ|(U∩V)'",
    "wavy arrow (crop p315s2_wavy1.png)", r"\mapsto",
    "symbol", None, "high",
    r"""$\mathscr E\mapsto\mathscr E|(U\cap V)$""",
    r"""$\mathscr E\leadsto\mathscr E|(U\cap V)$""")
add(315, "(21.13.3) a), last line: 'est fidèle (resp. pleinement fidèle).'",
    "'(resp.' and the closing parenthesis upright, 'pleinement fidèle' italic (crop p315s2_resp1.png)",
    "all italic (corollary environment)",
    "convention", 6, "high",
    r"""rang fini est fidèle
  (resp.\ pleinement fidèle)""",
    r"""rang fini est fidèle
  \textup{(resp.}\ pleinement fidèle\textup{)}""")
add(315, "(21.13.3) a'): 'le foncteur restriction ℒ ⇝ ℒ|(U∩V)'",
    "wavy arrow (crop p315s2_wavy2.png)", r"\mapsto",
    "symbol", None, "high",
    r"""$\mathscr L\mapsto\mathscr L|(U\cap V)$""",
    r"""$\mathscr L\leadsto\mathscr L|(U\cap V)$""")
add(315, "(21.13.3) a'), last line: 'est fidèle (resp. pleinement fidèle).'",
    "'(resp.' and the closing parenthesis upright (crop p315s2_resp2.png)",
    "all italic (corollary environment)",
    "convention", 6, "high",
    r"""rang $1$ est fidèle
  (resp.\ pleinement fidèle)""",
    r"""rang $1$ est fidèle
  \textup{(resp.}\ pleinement fidèle\textup{)}""")
add(315, "(21.13.3) b): 'est injectif (resp. bijectif) pour tout'",
    "'(resp.' and ')' upright, 'bijectif' italic (crop p315s2_b.png)",
    "all italic (corollary environment)",
    "convention", 6, "high",
    r"""est injectif (resp.\ bijectif) pour""",
    r"""est injectif \textup{(resp.}\ bijectif\textup{)} pour""")
add(315, "(21.13.3) b'): 'est injectif (resp. bijectif).'",
    "'(resp.' and ')' upright (crop p315s2_bprime.png)",
    "all italic (corollary environment)",
    "convention", 6, "high",
    r"""$\mathcal O_X\to j_*(\mathcal O_U)$ est injectif (resp.\ bijectif).""",
    r"""$\mathcal O_X\to j_*(\mathcal O_U)$ est injectif \textup{(resp.}\ bijectif\textup{)}.""")
add(315, "Lemme (21.13.4), l. 2: 'U = X — Y'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""$U=X-Y$, $j""",
    r"""$U=X\setmin Y$, $j""")
add(315, "Lemme (21.13.4), l. 3: 'soit injectif (resp. bijectif), il faut'",
    "'(resp.' and ')' upright (crop p315s3_lemma1.png)",
    "all italic (lemma environment)",
    "convention", 6, "high",
    r"""soit injectif (resp.\ bijectif), il""",
    r"""soit injectif \textup{(resp.}\ bijectif\textup{)}, il""")
add(315, "Lemme (21.13.4), ll. 3-4: '(resp. prof_Y(O_X) ≥ 2) (autrement dit, que prof(O_X,x) ≥ 1 (resp. prof(O_X,x) ≥ 2) pour tout x ∈ Y)'",
    "both parentheses wholly upright: '(resp.', 'autrement dit, que', 'pour tout' roman (crops p315s3_lemma1.png, p315s3_lemma2.png)",
    "italic (lemma environment)",
    "convention", 6, "high",
    r"""(resp.\ $\operatorname{prof}_Y(\mathcal O_X)\geq2$) (autrement dit, que
$\operatorname{prof}(\mathcal O_{X,x})\geq1$
(resp.\ $\operatorname{prof}(\mathcal O_{X,x})\geq2$) pour tout $x\in Y$).""",
    r"""\textup{(resp.\ $\operatorname{prof}_Y(\mathcal O_X)\geq2$) (autrement dit, que
$\operatorname{prof}(\mathcal O_{X,x})\geq1$
(resp.\ $\operatorname{prof}(\mathcal O_{X,x})\geq2$) pour tout $x\in Y$)}.""",
    "One edit for the two adjacent roman parentheses (the full stop stays outside).")
add(315, "Proposition (21.13.5), l. 1: 'U = X — Y'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""$U=X-Y$,
$j:U\to X$ l'injection canonique. Pour que le couple""",
    r"""$U=X\setmin Y$,
$j:U\to X$ l'injection canonique. Pour que le couple""")
add(315, "Proposition (21.13.5), last line: '(notation de (21.13.3)).'",
    "opening parenthesis and 'notation de' italic; the reference (21.13.3) and both closing parentheses upright (crops p315s3_notation_open.png, p315s3_notation_close.png)",
    "all italic (proposition environment)",
    "convention", 6, "high",
    r"""(notation de (21.13.3)).""",
    r"""(notation de \textup{(21.13.3))}.""",
    "GLOBAL_ISSUES 101: the parenthesis next to the reference is upright, the one before the italic words italic.")
add(315, "Corollaire (21.13.6): item labels (i), (ii), (iii)",
    "labels upright", "enumerate labels italic inside the italic corollary",
    "convention", 6, "high",
    r"""\begin{enumerate}[label=(\roman*)]
  \item Si le couple""",
    r"""\begin{enumerate}[label=\textup{(\roman*)}]
  \item Si le couple""",
    "GLOBAL_ISSUES 16; one edit covers the three labels.")
add(315, "Corollaire (21.13.6) (iii): 'l'ouvert U = X — Y soit rétrocompact'",
    "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""l'ouvert $U=X-Y$ soit""",
    r"""l'ouvert $U=X\setmin Y$ soit""")

# ---------------------------------------------------------------- p. 316
add(316, "proof of (21.13.6) (i), l. 2: 'tout revient à voir (en vertu de (21.13.5)) en désignant'",
    "no comma after the parenthesis (crop p316s1_envertu.png)", "'(21.13.5)), en désignant'",
    "punctuation", None, "high",
    r"""(21.13.5)), en""",
    r"""(21.13.5)) en""")
add(316, "proof of (21.13.6) (i), l. 3: 'par j_α l'injection canonique U∩W_α → W_α, que l'on a'",
    "'j_α l'injection canonique U∩W_α→W_α,' (crop p316s1_envertu.png)",
    "'j_α : U∩W_α → W_α l'injection canonique,' (map written before the words)",
    "formula", None, "high",
    r"""$j_\alpha:U\cap W_\alpha\to W_\alpha$ l'injection canonique,""",
    r"""$j_\alpha$ l'injection canonique $U\cap W_\alpha\to W_\alpha$,""",
    "Rewording of the print (GLOBAL_ISSUES 46/102). Independent of the comma entry above (no overlap).")
add(316, "proof of (21.13.6) (i), end: 'comme on a j_*(ℒ)|W_α = (j_α)_*(ℒ|(U∩W_α)), cela prouve notre assertion.'",
    "formula in the running text (page_316_s1.png)", "set as a display",
    "formula", None, "high",
    r"""comme on a
\[
  j_*(\mathscr L)|W_\alpha
  =(j_\alpha)_*(\mathscr L|(U\cap W_\alpha)),
\]
cela prouve""",
    r"""comme on a
$j_*(\mathscr L)|W_\alpha=(j_\alpha)_*(\mathscr L|(U\cap W_\alpha))$, cela prouve""")
add(316, "proof of (21.13.6) (ii), l. 1: 'Posons U' = X — Y''", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""Posons $U'=X-Y'""",
    r"""Posons $U'=X\setmin Y'""",
    "Adjacent to the next entry, no overlap.")
add(316, "proof of (21.13.6) (ii), l. 1: 'Posons U' = X — Y' et soit j' : U' → X'",
    "no comma before 'et soit' (crop p316s1_posons.png)", "'$U'=X-Y'$, et soit'",
    "punctuation", None, "high",
    r"""$, et soit $j':U'""",
    r"""$ et soit $j':U'""")
add(316, "proof of (21.13.6) (ii), after the display: 'est bijecti par hypothèse (21.13.5)'",
    "'bijecti' without its final f; the word space after it equals the other spaces of the line (27-28 px), so no letter was lost in printing (crop p316s2_bijecti.png)",
    "'bijectif': silent correction",
    "misprint_in_print", None, "high",
    r"""bijectif par hypothèse""",
    r"""bijecti par hypothèse""",
    "Compositor's misprint; the fix restores the printed reading. Independent of the comma entry below.",
    corrected=r"""bijectif par hypothèse""")
add(316, "same line: 'par hypothèse (21.13.5) et en remplaçant V par V∩U''",
    "no comma after (21.13.5) (crop p316s2_bijecti.png)", "'(21.13.5), et en remplaçant'",
    "punctuation", None, "high",
    r"""(21.13.5), et en""",
    r"""(21.13.5) et en""")
add(316, "proof of (21.13.6) (ii): 'ℒ'|U est un O_X-Module inversible, donc'",
    "O_X (crop p316s2_Lprime_zoom.png)",
    "O_U: silent correction",
    "misprint_in_print", None, "high",
    r"""$\mathscr L'|U$ est un $\mathcal O_U$-Module""",
    r"""$\mathscr L'|U$ est un $\mathcal O_X$-Module""",
    "ℒ'|U is an O_U-Module; the print's O_X is a slip (no errata list covers IV-4). The fix restores the printed reading.",
    corrected=r"""$\mathscr L'|U$ est un $\mathcal O_U$-Module""")
add(316, "proof of (21.13.6) (iii), l. 1: 'Posons U' = X' — Y' = f^{-1}(U)'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""$U'=X'-Y'=f^{-1}(U)$""",
    r"""$U'=X'\setmin Y'=f^{-1}(U)$""")
add(316, "Définition (21.13.7): 'On dit qu'un anneau local A est parafactoriel si,'",
    "'parafactoriel' in the same italic as the rest of the definition (crop p316s4_def.png)",
    r"\emph{parafactoriel} inside the italic definition environment: upright",
    "convention", 6, "high",
    r"""anneau local $A$ est \emph{parafactoriel} si,""",
    r"""anneau local $A$ est parafactoriel si,""",
    "\\emph dropped where the print shows no change of face (FIX_POLICY 2.6). The mark after 'Spec(A)' on the next line is a damaged parenthesis, not a comma.")
add(316, "Proposition (21.13.8), l. 1: 'Les notations étant celles de (21.13.7), on pose'",
    "(21.13.7) upright with upright parentheses (crop p316s4_prop.png)",
    "italic (proposition environment)",
    "convention", 6, "high",
    r"""celles de (21.13.7),""",
    r"""celles de \textup{(21.13.7)},""")
add(316, "Proposition (21.13.8), l. 1: 'U = X — {a}'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""on pose $U=X-\{a\}$""",
    r"""on pose $U=X\setmin\{a\}$""")
add(316, "Proposition (21.13.8): item labels (i), (ii)",
    "labels upright", "enumerate labels italic inside the italic proposition",
    "convention", 6, "high",
    r"""\begin{enumerate}[label=(\roman*)]
  \item L'homomorphisme canonique""",
    r"""\begin{enumerate}[label=\textup{(\roman*)}]
  \item L'homomorphisme canonique""",
    "GLOBAL_ISSUES 16; one edit covers both labels.")

# ---------------------------------------------------------------- p. 317
add(317, "page break 316/317: p. 317 begins 'Si en outre A est noethérien, la condition (i) équivaut à'",
    "indented new paragraph at the top of p. 317 (page_317_s1.png); p. 316 ends with '(ii) Pic(U)=0.'",
    "the text follows \\end{enumerate} with no blank line (\\end{enumerate}, marker, text): set without indent",
    "marker", None, "high",
    r"""\oldpage[IV-4]{317}
Si en outre""",
    r"""\oldpage[IV-4]{317}

Si en outre""",
    "Boundary 316/317 (both pages in this batch). GLOBAL_ISSUES 80 pattern: the blank line after the marker gives the printed paragraph indent (\\oldpage ends with \\ignorespaces, the blank line still makes a \\par).")
add(317, "Proposition (21.13.8), continued: 'la condition (i) équivaut à'",
    "(i) upright (crop p317s1_ibis.png)", "italic (proposition environment)",
    "convention", 6, "high",
    r"""la condition (i) équivaut""",
    r"""la condition \textup{(i)} équivaut""")
add(317, "Proposition (21.13.8): label '(i bis)'",
    "'bis' italic, 'i' and the parentheses upright (crop p317s1_ibis.png)", "'(i bis)' all upright",
    "italics", None, "high",
    r"""\item[\textup{(i bis)}]""",
    r"""\item[\textup{(i \emph{bis})}]""",
    "GLOBAL_ISSUES 26 ('bis' italic in the print).")
add(317, "heading of (21.13.9): 'Exemples (21.13.9). — (i) Un anneau local ...'",
    "examples heading 'Exemples (21.13.9). —' with (i) on the same line (page_317_s1.png)",
    "\\begin{env}[21.13.9] with a hand-made '\\emph{Exemples}. ---' and a blank line: prints '(21.13.9) Exemples. —' and starts (i) on a new paragraph",
    "other", None, "high",
    r"""\begin{env}[21.13.9]
\label{IV.21.13.9}
\emph{Exemples}. ---

(i) Un anneau""",
    r"""\begin{examples}[21.13.9]
\label{IV.21.13.9}
(i) Un anneau""",
    "Part 1 of 2: the preamble's examples environment, as the print shows. Apply together with the '\\end{examples}' entry on p. 319 (same environment; it ends on p. 319).")
add(317, "Exemples (21.13.9) (iii): '(1+z)(1—z) = 1'", "long dash for the minus sign (crop p317s2_1mz.png)", "minus sign",
    "convention", 7, "high",
    r"""$(1+z)(1-z)=1$""",
    r"""$(1+z)(1\setmin z)=1$""",
    "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(317, "Exemples (21.13.9) (iii): 'Par la suite exacte de cohomologie, on en déduit une suite exacte'",
    "indented new paragraph after the display (page_317_s4.png)",
    "follows \\] with no blank line: no indent",
    "other", None, "high",
    r"""\longrightarrow\mathcal O_{U_0}^*\longrightarrow1.
\]
Par la suite""",
    r"""\longrightarrow\mathcal O_{U_0}^*\longrightarrow1.
\]

Par la suite""",
    "GLOBAL_ISSUES 47 pattern.")
add(317, "display (21.13.9.1): '... →^{u_1} H^1(U, O^*_{U_0}).'",
    "full stop after the display (crop p317s4_disp.png)", "no full stop",
    "punctuation", None, "high",
    r"""\mathrm H^1(U,\mathcal O_{U_0}^*)
  \tag{21.13.9.1}""",
    r"""\mathrm H^1(U,\mathcal O_{U_0}^*).
  \tag{21.13.9.1}""")

# ---------------------------------------------------------------- p. 318
add(318, "Exemples (21.13.9) (iv): 'k[U, V, W]/(W^2 — UV)'", "long dash for the minus sign (crop p318s1_W2UV.png)", "minus sign",
    "convention", 7, "high",
    r"""(W^2-UV)""",
    r"""(W^2\setmin UV)""",
    "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(318, "Exemples (21.13.9) (v): '(cf. [41, XI, 3.13 (i))]).'",
    "an extra closing parenthesis after '(i)' inside the bracket (crop p318s2_cf_zoom.png)",
    "'(cf. [41, XI, 3.13 (i)]).': silent correction",
    "misprint_in_print", None, "high",
    r"""3.13 (i)]).""",
    r"""3.13 (i))]).""",
    "The fix restores the printed reading. (The XI is not bold: stems 5-6 px like the III of [41, III, ...] on p. 317.)",
    corrected=r"""3.13 (i)]).""")
add(318, "(vi) 1°: 'A est un anneau de Cohen-Macaulay'",
    "hyphen (crop p318s2_cm.png)", "en dash 'Cohen--Macaulay'",
    "punctuation", None, "high",
    r"""Cohen--Macaulay""",
    r"""Cohen-Macaulay""",
    "GLOBAL_ISSUES 74 pattern.")
add(318, "(vi), after 3°: 'On peut montrer en outre que ces conditions entraînent la propriété suivante :'",
    "indented new paragraph (crop p318s2_5a.png)",
    "follows \\end{enumerate} with no blank line: no indent",
    "other", None, "high",
    r"""\end{enumerate}
On peut montrer en outre""",
    r"""\end{enumerate}

On peut montrer en outre""",
    "GLOBAL_ISSUES 80 pattern.")
add(318, "(vi), 'Si l'on pose ...': 'un isomorphisme de X' — Y' sur X — Y'",
    "long dashes for set difference", "minus signs",
    "convention", 7, "high",
    r"""de $X'-Y'$ sur $X-Y$""",
    r"""de $X'\setmin Y'$ sur $X\setmin Y$""",
    "One edit for both dashes.")
add(318, "(vi): '(et en particulier A' est un anneau local noethérien)'",
    "'local' italic (crop p318s3_local.png)", "upright",
    "italics", None, "high",
    r"""est un anneau local noethérien);""",
    r"""est un anneau \emph{local} noethérien);""")
add(318, "(vi): 'on en déduit que l'on a m_z O_{X',z'} = m_{z'} pour z = y_i et z' = y'_i; cette relation est aussi vérifiée'",
    "the relation in the running text, written with z, z', followed by 'pour z=y_i et z'=y'_i;' (crop p318s3_mz.png)",
    "a display 'm_{y_i} O_{X',y_i'} = m_{y_i'}.' and a new sentence 'Pour z=y_i et z'=y_i', cette relation ...'",
    "formula", None, "high",
    r"""que l'on a
\[
  \mathfrak m_{y_i}\mathcal O_{X',y_i'}=\mathfrak m_{y_i'}.
\]
Pour $z=y_i$ et $z'=y_i'$, cette relation""",
    r"""que l'on a $\mathfrak m_z\mathcal O_{X',z'}=\mathfrak m_{z'}$
pour $z=y_i$ et $z'=y_i'$; cette relation""",
    "Rewording of the print (GLOBAL_ISSUES 46/102/104): renamed variables, a display for an inline formula, the sentence cut in two. The fix restores the printed sentence.")
add(318, "(vi): 'donc pour tout z ∈ U = X — {x}'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""$z\in U=X-\{x\}$""",
    r"""$z\in U=X\setmin\{x\}$""")
add(318, "(vi): 'de caractéristique 0 (0, 21.1.1) on voit que'",
    "bold 0 without subscript (crop p318s3_zero.png)", "plain 0",
    "convention", 2, "high",
    r"""(0, 21.1.1)""",
    r"""$(\mathbf 0, 21.1.1)$""",
    "Written as the other chapter-0 reference of this file, $(\\mathbf 0, 18.2.3)$ on p. 317.")
add(318, "(vi): '(mais non étale en général)'",
    "'non' italic (crop p318s3_non.png)", "upright",
    "italics", None, "high",
    r"""(mais non étale""",
    r"""(mais \emph{non} étale""")
add(318, "(vi): 'Or, en vertu de la condition 1° et de (21.13.8), il suffit de montrer que Pic(U) = 0.'",
    "'de montrer que' (crop p318s3_nous.png)", "'de démontrer que'",
    "word", None, "high",
    r"""il suffit
de démontrer que""",
    r"""il suffit
de montrer que""")
add(318, "(vi): 'Puisque A' est factoriel en vertu de 2°, on a Pic(U') = 0'",
    "indented new paragraph (crop p318s3_nous.png)", "same paragraph as 'Nous nous bornerons ...'",
    "other", None, "high",
    r"""=0$. Puisque $A'$ est factoriel""",
    r"""=0$.

Puisque $A'$ est factoriel""",
    "Independent of the previous entry (no overlap).")
add(318, "(vi), display after (21.8.5, (ii)): leading '1 →'",
    "the 1 is BOLD (wrong fount): stem 5 px and serifs 4 rows thick against 3.5-4 px stems and 2-3-row serifs of the display 1s on p. 317 and the small-type 1 of 's_i=1'; the final 0 of the display is light (crops p318s3_one.png, p317s3_one_cmp.png)",
    "plain 1",
    "misprint_in_print", None, "medium",
    r"""\[
  1\longrightarrow""",
    r"""\[
  \mathbf{1}\longrightarrow""",
    "Wrong-fount figure recorded as a misprint (GLOBAL_ISSUES 29/99); isolated at the start of the display, not line-end heavy impression (item 100). Independent of the next entry.",
    corrected=r"""\[
  1\longrightarrow""")
add(318, "same display: '(∏_{s∈S} O'^*_{U,s}/O^*_{U,s})/Im Γ(U', O^*_{U'})'",
    "product over s ∈ S of O'^*_{U,s}/O^*_{U,s} (crop p318s3_disp.png)",
    "product over i = 1..r of O^*_{U',y_i'}/O^*_{U,y_i}",
    "formula", None, "high",
    r"""\left(\prod_{i=1}^r
  \mathcal O_{U',y_i'}^*/\mathcal O_{U,y_i}^*\right)""",
    r"""\left(\prod_{s\in S}
  \mathcal O'^*_{U,s}/\mathcal O^*_{U,s}\right)""",
    "Rewritten notation (GLOBAL_ISSUES 102/104); the print's S is the set named in the next sentence ('en prenant pour S l'ensemble des y_i').")
add(318, "after the display: 'en notant qu'ici O'_X = f_*(O_{X'}) est la O_X-Algèbre Ã''",
    "'O'_X = f_*(O_X')' (crop p318s4_1a.png)", "'O'_X =' missing",
    "missing", None, "high",
    r"""qu'ici $f_*(\mathcal O_{X'})$""",
    r"""qu'ici $\mathcal O'_X=f_*(\mathcal O_{X'})$""",
    "The O' of the display is defined here.")
add(318, "'un élément inversible a'_i/s_i de A'_{p_i}, avec a'_i ∈ A', s_i ∉ p_i ;'",
    "subscript p_i (no prime) in A'_{p_i} and in s_i ∉ p_i (crop p318s4_3a.png)",
    "A'_{p_i'} and s_i ∉ p_i'",
    "formula", None, "high",
    r"""$A'_{\mathfrak p_i'}$, avec $a_i'\in A'$, $s_i\notin\mathfrak p_i'$;""",
    r"""$A'_{\mathfrak p_i}$, avec $a_i'\in A'$, $s_i\notin\mathfrak p_i$;""",
    "Rewritten notation (GLOBAL_ISSUES 102). The print's reading is sound (A' localised at A − p_i, s_i ∈ A), so not a misprint.")
add(318, "'les groupes quotients A'^*_{p_i}/A^*_{p_i}, on peut supposer'",
    "A'^*_{p_i}/A^*_{p_i} (crop p318s4_3b.png)", "(A'_{p_i'})^*/(A_{p_i})^*",
    "formula", None, "high",
    r"""$(A'_{\mathfrak p_i'})^*/(A_{\mathfrak p_i})^*$, on peut""",
    r"""$A'^*_{\mathfrak p_i}/A^*_{\mathfrak p_i}$, on peut""",
    "Rewritten notation (GLOBAL_ISSUES 102); the same quotient on printed p. 319, l. 1 is a separate entry.")
add(318, "'de sorte que b'_i/1 est un élément ≠ 0 de k(y_i)'",
    "'≠ 0' (crop p318s4_4b.png)", "'non nul'",
    "word", None, "high",
    r"""un élément non nul""",
    r"""un élément $\neq0$""")
add(318, "same sentence: 'k(y_i) = O_{Y',y'_i}'",
    "bold italic k (crop p318s4_5a.png)", "plain k",
    "convention", 1, "high",
    r"""de $k(y_i""",
    r"""de $\boldsymbol{k}(y_i""",
    "Adjacent to the misprint entry below (no overlap).")
add(318, "same sentence: 'k(y_i) = O_{Y',y'_i}'",
    "k(y_i), argument without prime (crop p318s4_5a.png)",
    "k(y_i'): silent correction",
    "misprint_in_print", None, "medium",
    r"""')=\mathcal O_{Y',y_i'}$""",
    r""")=\mathcal O_{Y',y_i'}$""",
    "O_{Y',y'_i} is the residue field of y'_i (B' reduced, y'_i maximal), which differs from k(y_i) in general (R((T)) against C((T)) in the example on p. 319): the print's k(y_i) is a slip for k(y'_i). The fix restores the printed reading; independent of the convention-1 entry above.",
    corrected=r"""')=\mathcal O_{Y',y_i'}$""")
add(318, "'où b'' ∈ B' est inversible. Soit a'' un élément'",
    "'inversible' italic (crop p318s4_7b.png)", "upright",
    "italics", None, "high",
    r"""$b''\in B'$ est inversible.""",
    r"""$b''\in B'$ est \emph{inversible}.""")
add(318, "last line: 'on a u_i = a'' — a'_i t^m ∈ J, d'où t^m a'_i = a'' — u_i = a''(1 — a''^{-1}u_i); mais'",
    "both formulas in the running text, joined by 'd'où' (crops p318s4_9a.png, p318s4_9b.png)",
    "a display with the two formulas joined by \\qquad; 'd'où' missing",
    "formula", None, "high",
    r"""$i$, on a
\[
  u_i=a''-a_i't^m\in\mathfrak J,
  \qquad
  t^m a_i'=a''-u_i=a''(1-a''^{-1}u_i);
\]
mais""",
    r"""$i$, on a $u_i=a''-a_i't^m\in\mathfrak J$, d'où $t^m a_i'=a''-u_i=a''(1-a''^{-1}u_i)$;
mais""",
    "GLOBAL_ISSUES 51 pattern (display for inline formulas, connecting word lost). Apply BEFORE the three convention-7 entries that follow (their text lies inside this edit and is unchanged by it).")
add(318, "same line: 'u_i = a'' — a'_i t^m'", "long dash for the minus sign", "minus sign",
    "convention", 7, "high",
    r"""a''-a_i't^m""",
    r"""a''\setmin a_i't^m""",
    "Apply after the inline-setting entry above. Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.",
    after="inline318")
add(318, "same line: 't^m a'_i = a'' — u_i'", "long dash for the minus sign", "minus sign",
    "convention", 7, "high",
    r"""=a''-u_i=""",
    r"""=a''\setmin u_i=""",
    "Apply after the inline-setting entry above.",
    after="inline318")
add(318, "same line: 'a''(1 — a''^{-1}u_i)'", "long dash for the minus sign", "minus sign",
    "convention", 7, "high",
    r"""(1-a''^{-1}u_i)""",
    r"""(1\setmin a''^{-1}u_i)""",
    "Apply after the inline-setting entry above.",
    after="inline318")
add(318, "same line: 'donc 1 — a''^{-1}u_i est un'", "long dash for the minus sign", "minus sign",
    "convention", 7, "high",
    r"""donc $1-a''^{-1}u_i$""",
    r"""donc $1\setmin a''^{-1}u_i$""")
add(318, "page break 318/319: printed p. 318 ends 'donc 1 — a''^{-1}u_i est un'; p. 319 begins 'élément inversible de A, et les classes ...'",
    "page_318_s4.png ends with 'est un' (page number 318 below); page_319_s1.png begins with 'élément inversible de A, ... ce qui achève la démonstration.'",
    "\\oldpage[IV-4]{319} stands before 'Pour avoir un exemple explicite', one printed line too late",
    "marker", None, "high",
    r"""est un
élément inversible de $A$""",
    r"""est un
\oldpage[IV-4]{319}
élément inversible de $A$""",
    "Marker move, part 2 of 2 (new position; mid-sentence break, no blank lines). Apply together with part 1 on p. 319, which removes the old marker. The moved line has one more difference (next entry).")
add(318, "printed p. 319, l. 1 (in the TeX before the 319 marker): 'les classes de a' et a'_i dans A'^*_{p_i}/A^*_{p_i} sont les mêmes'",
    "A'^*_{p_i}/A^*_{p_i} (crop p319s1_1b.png)", "(A'_{p_i'})^*/(A_{p_i})^*",
    "formula", None, "high",
    r"""$(A'_{\mathfrak p_i'})^*/(A_{\mathfrak p_i})^*$ sont""",
    r"""$A'^*_{\mathfrak p_i}/A^*_{\mathfrak p_i}$ sont""",
    "Text of printed p. 319 that sits in the p. 318 segment until the marker move; no overlap with the marker entries.")

# ---------------------------------------------------------------- p. 319
add(319, "page break 318/319: old marker position",
    "p. 319 begins with 'élément inversible de A, ...'; 'Pour avoir un exemple explicite' is its second line",
    "\\oldpage[IV-4]{319} before 'Pour avoir'",
    "marker", None, "high",
    r"""\oldpage[IV-4]{319}
Pour avoir""",
    r"""Pour avoir""",
    "Marker move, part 1 of 2: removes the marker; the blank line before it stays ('Pour avoir' is an indented new paragraph in the print). Apply together with part 2 on p. 318.")
add(319, "l. 3: 'considérons l'anneau E = R[[U, V]]/(U^2+V^2), dont la clôture intégrale'",
    "formula in the running text (crop p319s1_3a.png)", "set as a display",
    "formula", None, "high",
    r"""l'anneau
\[
  E=\mathbb R[[U,V]]/(U^2+V^2),
\]
dont""",
    r"""l'anneau
$E=\mathbb R[[U,V]]/(U^2+V^2)$, dont""")
add(319, "'localisé de l'anneau k[U, V, W]/(U^2 — WV^2)'", "long dash for the minus sign (crop p319s1_9a.png)", "minus sign",
    "convention", 7, "high",
    r"""(U^2-WV^2)""",
    r"""(U^2\setmin WV^2)""",
    "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(319, "end of Exemples (21.13.9): '... un anneau régulier.'",
    "see the heading entry on p. 317", "\\end{env}",
    "other", None, "high",
    r"""\emph{régulier}.
\end{env}""",
    r"""\emph{régulier}.
\end{examples}""",
    "Part 2 of 2: apply together with the '\\begin{examples}' entry on p. 317.")
add(319, "proof of (21.13.10), l. 1: 'Posons U = X — Y'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""Posons $U=X-Y$ et soit $j:U\to X$ l'injection canonique.

En vertu""",
    r"""Posons $U=X\setmin Y$ et soit $j:U\to X$ l'injection canonique.

En vertu""")
add(319, "proof of (21.13.10): 'dire que l'homomorphisme canonique O_X → j_*(O_U) soit injectif équivaut à dire'",
    "'injectif' (crop p319s2_2a.png)", "'bijectif': silent correction",
    "misprint_in_print", None, "high",
    r"""soit bijectif équivaut""",
    r"""soit injectif équivaut""",
    "By (21.13.4) the condition (i bis) prof ≥ 2 is equivalent to bijectivity (injectivity is prof ≥ 1), and the proof uses bijectivity: the print's 'injectif' is a slip. The fix restores the printed reading.",
    corrected=r"""soit bijectif équivaut""")
add(319, "same sentence: 'la condition (i bis) de (21.13.8)'",
    "'bis' italic (crop p319s2_3a.png)", "upright",
    "italics", None, "high",
    r"""condition (i bis) de""",
    r"""condition (i \emph{bis}) de""",
    "GLOBAL_ISSUES 26.")
add(319, "proof of (21.13.10): 'U_y = T_y — {y}'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""et $U_y=T_y-\{y\}$, tout""",
    r"""et $U_y=T_y\setmin\{y\}$, tout""")
add(319, "proof of (21.13.10): 'sur les ouverts V — (V∩{y}‾)'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""ouverts
$V-(V""",
    r"""ouverts
$V\setmin(V""",
    "Independent of the next entry (no overlap).")
add(319, "same sentence: 'les ouverts V — (V∩{y}‾) qui sont quasi-compacts'",
    "no comma after the formula (crop p319s3_comma.png)", "comma after the formula",
    "punctuation", None, "high",
    r"""\{y\}})$, qui sont""",
    r"""\{y\}})$ qui sont""")
add(319, "proof of (21.13.10): 'Comme les U_V = V — (V∩{y}‾) sont séparés'",
    "'U_V =' before the formula (crop p319s3_UV.png)", "'U_V =' missing",
    "missing", None, "high",
    r"""Comme les $V""",
    r"""Comme les $U_V=V""",
    "The U_V of the next lines is named here. Independent of the convention-7 entry below (no overlap).")
add(319, "same formula: 'U_V = V — (V∩{y}‾)'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""-(V\cap\overline{\{y\}})$ sont séparés""",
    r"""\setmin(V\cap\overline{\{y\}})$ sont séparés""")
add(319, "proof of (21.13.10): 'en vertu de (21.13.6, (i) et (ii)), que le couple (V, V∩{y}‾)'",
    "'(i) et (ii)' (crop p319s3_2136_zoom.png)", "'(i) et (iii)'",
    "number", None, "high",
    r"""(i) et (iii))""",
    r"""(i) et (ii))""",
    "The print is right: (21.13.6) (i) restricts to the open V, (ii) passes to the closed part V∩{y}‾ of V∩Y.")
add(319, "proof of (21.13.10), converse: 'L'ensemble des x ∈ X tels que ...'",
    "no V after 'L'ensemble' (crops p319s4_1b.png, p319s4_2a.png), although 'montrer que V = X' follows",
    "'L'ensemble $V$ des': silent correction",
    "misprint_in_print", None, "high",
    r"""L'ensemble $V$ des""",
    r"""L'ensemble des""",
    "The print never names the set it then calls V. The fix restores the printed reading.",
    corrected=r"""L'ensemble $V$ des""")
add(319, "proof of (21.13.10): 'posons Z = X — V ≠ ∅'", "long dash for set difference", "minus sign",
    "convention", 7, "high",
    r"""$Z=X-V\neq""",
    r"""$Z=X\setmin V\neq""")


# ---------------------------------------------------------------- checks
def page_text(p):
    with open(BASE + rf"\page_{p}.tex", encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


SRC = BASE + r"\..\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV4\native\ega4\ega4-21c-fr.tex"
with open(SRC, encoding="utf-8") as fh:
    src = fh.read().replace("\r\n", "\n")
ok = True
texts = {p: page_text(p) for p in (315, 316, 317, 318, 319)}
inline318 = [d for d in F if d["page"] == 318 and d["fix"] and "\\qquad" in d["fix"]["old"]][0]
after_text = {"inline318": texts[318].replace(inline318["fix"]["old"], inline318["fix"]["new"])}
for d in F:
    if not d["fix"]:
        continue
    old = d["fix"]["old"]
    n = texts[d["page"]].count(old)
    if d["_after"]:
        n2 = after_text[d["_after"]].count(old)
        status = f"orig {n}, after {n2}"
        good = n2 == 1
    else:
        status = f"{n}"
        good = n == 1
    src_now = src
    if d["_after"]:
        src_now = src.replace(inline318["fix"]["old"], inline318["fix"]["new"])
    ns = src_now.count(old)
    if ns != 1:
        good = False
        status += f", source {ns}"
    if not good:
        ok = False
    print(("OK  " if good else "BAD ") + f"p{d['page']} {status}: {old[:60]!r}")

# overlaps between olds on the same page (positions in the original text)
import itertools
for p in texts:
    spans = []
    for d in F:
        if d["page"] != p or not d["fix"] or d["_after"]:
            continue
        i = texts[p].find(d["fix"]["old"])
        spans.append((i, i + len(d["fix"]["old"]), d["fix"]["old"][:40]))
    for a, b in itertools.combinations(sorted(spans), 2):
        if a[1] > b[0]:
            print("OVERLAP", p, a, b)

for d in F:
    del d["_after"]
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", len(F), "entries; all unique:", ok)
from collections import Counter
c = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
