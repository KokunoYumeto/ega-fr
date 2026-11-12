"""Build findings_110_114.json (EGA IV-4, pp. 110-114, ega4-18-fr.tex)."""
import json
import pathlib

OUT = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV4\findings_110_114.json")
N = "\n"
F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None, fix=True):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=(dict(old=old, new=new) if fix else None))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


BAR = ("The print writes these subscripts with a slash, as in Tr_{B/A}; the TeX has a vertical bar in all 16 of them "
       "(pp. 111-113, all fixed one by one here). Only the bar of B|U (restriction, p. 113) is a real bar.")
KAPPA = "The TeX has Greek \\kappa for the print's bold italic k (ega4-18 writes \\kappa 14 times; 12 are on pp. 112-114)."
LAB = "GLOBAL_ISSUES 88: condition labels in roman text are italic as a whole in the print."
ITEM = "Labels printed upright inside the italic statement (GLOBAL_ISSUES 16/88)."

# ---------------------------------------------------------------- p. 110
add(110, "top of p. 110: blank line after \\oldpage[IV-4]{110}",
    "p. 109 ends 'B_0 est donc un anneau quotient', p. 110 begins 'de B, q_0 est l'image' (no indent; page_110_s1.png)",
    "blank line between the marker and 'de $B$' (the blank line before the marker is already gone in the current source)",
    "marker", r"\oldpage[IV-4]{110}" + N + N + r"de $B$, $\mathfrak q_0$",
    r"\oldpage[IV-4]{110}" + N + r"de $B$, $\mathfrak q_0$",
    note="The marker stands at the right place. This removes the blank line after it (\\oldpage ends with \\ignorespaces, which does not skip a paragraph break).")
add(110, "Théorème (18.1.2), display 'X ⇝ X×_S S_0'", "wavy arrow (crop p110_leadsto.png)", "\\longmapsto",
    "symbol", r"X\longmapsto X\times_S S_0", r"X\leadsto X\times_S S_0", note="GLOBAL_ISSUES 33 (wavy arrow).")
add(110, "proof of (18.1.2), first sentence: 'ce foncteur est pleinement fidèle'",
    "'pleinement fidèle' italic (crop p110_pleinement.png)", "roman", "italics",
    r"ce foncteur est pleinement fidèle. Soient", r"ce foncteur est \emph{pleinement fidèle}. Soient")
add(110, "proof of (18.1.2): 'sont donc les mêmes que les parties de Z_0'", "'mêmes' italic (crop p110_memes.png)",
    "roman", "italics", r"sont donc les mêmes que", r"sont donc les \emph{mêmes} que")
add(110, "proof of (18.1.2): 'condition de recollement (0_I, 4.1.7)'", "bold 0 with subscript I (crop p110_0I417.png)",
    "plain 0", "convention", r"($0_{\mathrm I}$, 4.1.7)", r"($\mathbf{0}_{\mathrm I}$, 4.1.7)", conv=2)
add(110, "Corollaire (18.1.3): '(I, 3.4.3)'",
    "bold upright I; the reference and its parentheses upright inside the italic statement (crop p110_I343.png)",
    "plain I, italic inside the corollary", "convention", r"(I, 3.4.3)", r"\textup{(\textbf{I}, 3.4.3)}", conv=2,
    note="A genuine EGA I reference (bold I in the print, not EGA IV's own (1.3.4.3)). Convention 2 with convention 6 (upright reference in an italic statement), one edit.")
add(110, "end of page_110.tex: the heading '18.2. Revêtements étales.' (it opens printed p. 111)",
    "p. 110 ends with the proof of (18.1.3), '(ou directement de (17.9.3)).'; p. 111 begins with the heading "
    "'18.2. Revêtements étales.' (page_110_s4.png, page_111_s1.png)",
    "\\subsection{Revêtements étales.} and its \\EGAReaderTarget stand before \\oldpage[IV-4]{111}", "marker",
    r"\subsection{Revêtements étales.}" + N + r"\EGAReaderTarget{ega4.c04.subsec.18-2}{subsection:IV.18.2}" + N + N, "",
    note="Two-part move (the heading moves, not the marker, so each edit stays in its own page segment): the first p. 111 finding re-inserts these two lines after \\oldpage[IV-4]{111}. Apply both or neither. Net result in ega4-18-fr.tex: \\oldpage[IV-4]{111} stands before the 18.2 heading.")

# ---------------------------------------------------------------- p. 111
add(111, "start of page_111.tex: the 18.2 heading",
    "printed p. 111 begins with '18.2. Revêtements étales.', then '(18.2.1) Étant donnés' (page_111_s1.png)",
    "the heading stands before the marker, at the end of the p. 110 segment", "marker",
    r"\oldpage[IV-4]{111}" + N + N + r"\begin{env}[18.2.1]",
    r"\oldpage[IV-4]{111}" + N + N + r"\subsection{Revêtements étales.}" + N
    + r"\EGAReaderTarget{ega4.c04.subsec.18-2}{subsection:IV.18.2}" + N + N + r"\begin{env}[18.2.1]",
    note="Part 2 of 2: apply together with the last p. 110 finding, which removes the same two lines from the end of the p. 110 segment.")
add(111, "display (18.2.1.1): '(x, y) ⇝ Tr_{B/A}(xy)'", "wavy arrow (crop p111_leadsto.png)", "\\longmapsto",
    "symbol", r"(x,y)\longmapsto\operatorname{Tr}_{B/A}(xy)", r"(x,y)\leadsto\operatorname{Tr}_{B/A}(xy)",
    note="GLOBAL_ISSUES 33 (wavy arrow).")
add(111, "(18.2.2), l. 1-2: 'soit B une O_X-Algèbre qui, en tant que O_X-Module, est localement libre de rang fini'",
    "'Algèbre' and 'Module' italic, like 'localement libre de rang fini' after them (crop p111_algebre.png)",
    "roman", "italics", r"$\sh{O}_X$-Algèbre qui, en tant que $\sh{O}_X$-Module, est",
    r"$\sh{O}_X$-\emph{Algèbre} qui, en tant que $\sh{O}_X$-\emph{Module}, est")
add(111, "(18.2.2): 'que nous noterons aussi Tr_{B/O_X,U}'",
    "slash between B and O_X (crop p111_tr_U.png; the bar of 'B|U' two lines higher is vertical, crop p111_BbarU.png)",
    "vertical bar: \\sh{B}|\\sh{O}_X", "symbol", r"\operatorname{Tr}_{\sh{B}|\sh{O}_X,U}",
    r"\operatorname{Tr}_{\sh{B}/\sh{O}_X,U}", note=BAR)
add(111, "(18.2.2), display 'astr_{B/O_X,U} : Γ(U,B) → Γ(U,B)ˇ = Γ(U,B̌)'", "slash (crop p111_astrU_display.png)",
    "vertical bar", "symbol", r"\operatorname{astr}_{\sh{B}|\sh{O}_X,U}", r"\operatorname{astr}_{\sh{B}/\sh{O}_X,U}",
    note="Same as the previous finding.")
add(111, "after the display astr_{B/O_X,U}: 'En outre, il résulte de (18.2.1.2)'",
    "new indented paragraph (crop p111_enoutre.png)", "no blank line after \\]: the text continues the paragraph without indent",
    "other", r"\]" + N + r"En outre, il résulte de (18.2.1.2)", r"\]" + N + N + r"En outre, il résulte de (18.2.1.2)",
    note="Paragraph indent only (GLOBAL_ISSUES 47 pattern).")
add(111, "display (18.2.2.1): 'Tr_{B/O_X} : B → O_X'", "slash (crop p111_tr_sub.png)", "vertical bar", "symbol",
    r"\operatorname{Tr}_{\sh{B}|\sh{O}_X}:\sh{B}", r"\operatorname{Tr}_{\sh{B}/\sh{O}_X}:\sh{B}",
    note="Slash for the bar, as above.")
add(111, "display (18.2.2.2): 'astr_{B/O_X} : B → B̌'", "slash (crop p111_2222.png)", "vertical bar", "symbol",
    r"\operatorname{astr}_{\sh{B}|\sh{O}_X}:\sh{B}", r"\operatorname{astr}_{\sh{B}/\sh{O}_X}:\sh{B}",
    note="Slash for the bar, as above.")
add(111, "display (18.2.2.3): '(Tr_{B/O_X})_x = Tr_{B_x/O_{X,x}}'", "two slashes (crop p111_22234.png)",
    "two vertical bars", "symbol",
    r"(\operatorname{Tr}_{\sh{B}|\sh{O}_X})_x=\operatorname{Tr}_{\sh{B}_x|\sh{O}_{X,x}}",
    r"(\operatorname{Tr}_{\sh{B}/\sh{O}_X})_x=\operatorname{Tr}_{\sh{B}_x/\sh{O}_{X,x}}", note="Slash for the bar, as above.")
add(111, "display (18.2.2.4): '(astr_{B/O_X})_x = astr_{B_x/O_{X,x}}.'", "two slashes (crops p111_22234.png, p111_2224.png)",
    "two vertical bars", "symbol",
    r"(\operatorname{astr}_{\sh{B}|\sh{O}_X})_x=\operatorname{astr}_{\sh{B}_x|\sh{O}_{X,x}}",
    r"(\operatorname{astr}_{\sh{B}/\sh{O}_X})_x=\operatorname{astr}_{\sh{B}_x/\sh{O}_{X,x}}", note="Slash for the bar, as above.")
add(111, "after (18.2.2.4): 'Enfin, sous les conditions de (18.2.1)'", "new indented paragraph (page_111_s4.png)",
    "no blank line after \\end{equation}: the text continues the paragraph without indent", "other",
    r"\end{equation}" + N + r"Enfin, sous", r"\end{equation}" + N + N + r"Enfin, sous",
    note="Paragraph indent only (GLOBAL_ISSUES 47 pattern).")
add(111, "(18.2.2), last paragraph: 'la forme Tr_{B/O_X} (resp. l'homomorphisme astr_{B/O_X})'",
    "two slashes (crop p111_enfin.png)", "two vertical bars", "symbol",
    r"la forme $\operatorname{Tr}_{\sh{B}|\sh{O}_X}$ (resp. l'homomorphisme $\operatorname{astr}_{\sh{B}|\sh{O}_X}$)",
    r"la forme $\operatorname{Tr}_{\sh{B}/\sh{O}_X}$ (resp. l'homomorphisme $\operatorname{astr}_{\sh{B}/\sh{O}_X}$)",
    note="Slash for the bar, as above.")

# ---------------------------------------------------------------- p. 112
add(112, "Proposition (18.2.3), l. 1: 'un morphisme fini de préschémas'",
    "'fini' roman inside the italic statement (crop p112_prop3_head.png)", "italic", "convention",
    r"un morphisme fini de préschémas", r"un morphisme \textup{fini} de préschémas", conv=6)
add(112, "Proposition (18.2.3), label a)", "upright 'a)' (crop p112_prop3_head.png)", "\\item[a)]: italic in the proposition",
    "convention", r"\item[a)] $f$ est étale.", r"\item[\textup{a)}] $f$ est étale.", conv=6, note=ITEM)
add(112, "Proposition (18.2.3), label a')", "upright a') (crop p112_prop3_head.png)", "\\item[a$'$)]: italic",
    "convention", r"\item[a$'$)]", r"\item[\textup{a$'$)}]", conv=6, note=ITEM)
add(112, "(18.2.3) a'): 'extension finie séparable de k(y)'", "bold italic k (crop p112_prop3_items.png)", "\\kappa(y)",
    "convention", r"extension finie séparable de $\kappa(y)$.", r"extension finie séparable de $\boldsymbol{k}(y)$.",
    conv=1, note=KAPPA)
add(112, "Proposition (18.2.3), label b)", "upright 'b)' (crop p112_prop3_items.png)", "\\item[b)]: italic",
    "convention", r"\item[b)] $\sh{B}$ est un", r"\item[\textup{b)}] $\sh{B}$ est un", conv=6, note=ITEM)
add(112, "(18.2.3) b): 'B_y ⊗_{O_{Y,y}} k(y) est une k(y)-algèbre finie séparable'",
    "two bold italic k (crop p112_prop3_items.png; the k after ⊗ is on the line, not in the subscript)", "\\kappa(y) twice",
    "convention", r"\kappa(y)$ est une $\kappa(y)$-algèbre finie", r"\boldsymbol{k}(y)$ est une $\boldsymbol{k}(y)$-algèbre finie",
    conv=1, note=KAPPA)
add(112, "(18.2.3) b): '(donc le composé direct d'un nombre fini de corps, extensions finies séparables de k(y))'",
    "the whole parenthesis roman inside the italic statement; bold italic k (crop p112_prop3_items.png)",
    "italic; \\kappa(y)", "convention",
    r"séparable (donc le composé direct d'un nombre fini de corps, extensions finies séparables de $\kappa(y)$).",
    r"séparable \textup{(donc le composé direct d'un nombre fini de corps, extensions finies séparables de $\boldsymbol{k}(y)$)}.",
    conv=6, note="Convention 6, one edit that also carries the convention-1 k of the parenthesis (\\kappa -> \\boldsymbol{k}).")
add(112, "Proposition (18.2.3), label c)", "upright 'c)' (page_112_s2.png)", "\\item[c)]: italic", "convention",
    r"\item[c)] $\sh{B}$ est un $\sh{O}_Y$-Module localement libre, et", r"\item[\textup{c)}] $\sh{B}$ est un $\sh{O}_Y$-Module localement libre, et", conv=6, note=ITEM)
add(112, "(18.2.3) c): 'astr_{B/O_Y} : B → B̌'", "slash (crop p112_c_astr.png)", "vertical bar", "symbol",
    r"l'homomorphisme $\operatorname{astr}_{\sh{B}|\sh{O}_Y}", r"l'homomorphisme $\operatorname{astr}_{\sh{B}/\sh{O}_Y}", note="Slash for the bar (see p. 111).")
add(112, "(18.2.3) c): '(18.2.2) est bijectif'", "reference upright inside the italic statement (crop p112_c_astr.png)",
    "italic", "convention", r"(18.2.2) est bijectif.", r"\textup{(18.2.2)} est bijectif.", conv=6)
add(112, "proof of (18.2.3): 'l'équivalence de a) et a') a déjà été démontrée'",
    "labels italic as a whole (crop p112_labels1.png)", "$a)$ and $a')$: italic letter, upright parenthesis", "italics",
    r"l'équivalence de $a)$ et $a')$ a déjà", r"l'équivalence de \emph{a)} et \emph{a$'$)} a déjà", note=LAB)
add(112, "proof of (18.2.3): 'que B est un A-module de présentation finie (1.4.7)'",
    "'module de présentation finie' italic (crop p112_module_pf.png)", "roman", "italics",
    r"est un $A$-module de présentation finie (1.4.7)", r"est un $A$-\emph{module de présentation finie} (1.4.7)")
add(112, "proof of (18.2.3): 'que B est un A-module projectif'", "'projectif' italic (crop p112_module_pf.png)", "roman",
    "italics", r"est un $A$-module projectif,", r"est un $A$-module \emph{projectif},")
add(112, "proof of (18.2.3): 'le spectre de la k(y)-algèbre B(y)=B_y ⊗_{O_{Y,y}} k(y)'", "two bold italic k (page_112_s2.png)",
    "\\kappa(y) twice", "convention",
    r"spectre de la $\kappa(y)$-algèbre $\sh{B}(y)=\sh{B}_y\otimes_{\sh{O}_{Y,y}}\kappa(y)$",
    r"spectre de la $\boldsymbol{k}(y)$-algèbre $\sh{B}(y)=\sh{B}_y\otimes_{\sh{O}_{Y,y}}\boldsymbol{k}(y)$",
    conv=1, note=KAPPA)
add(112, "proof of (18.2.3): 'l'équivalence de a') et b)'", "labels italic as a whole (page_112_s2.png)",
    "$a')$, $b)$", "italics", r"l'équivalence de $a')$ et $b)$.", r"l'équivalence de \emph{a$'$)} et \emph{b)}.", note=LAB)
add(112, "proof of (18.2.3): 'Pour voir que b) est équivalente à c), notons que la seconde assertion de b)'",
    "labels italic as a whole (page_112_s2.png)", "$b)$, $c)$, $b)$", "italics",
    r"Pour voir que $b)$ est équivalente à $c)$, notons que la seconde assertion de $b)$ équivaut",
    r"Pour voir que \emph{b)} est équivalente à \emph{c)}, notons que la seconde assertion de \emph{b)} équivaut", note=LAB)
add(112, "proof of (18.2.3): 'astr_{B(y)/k(y)}'", "slash (crop p112_astr_y.png)", "vertical bar", "symbol",
    r"\operatorname{astr}_{\sh{B}(y)|", r"\operatorname{astr}_{\sh{B}(y)/", note="Slash for the bar (see p. 111).")
add(112, "proof of (18.2.3): subscript k(y) of astr_{B(y)/k(y)}", "bold upright k in the subscript (crop p112_astr_y.png)",
    "\\kappa(y)", "convention", r"\kappa(y)}:\sh{B}(y)", r"\mathbf{k}(y)}:\sh{B}(y)", conv=1,
    note=KAPPA + " In the subscript the print's k is bold upright (GLOBAL_ISSUES 48).")
add(112, "proof of (18.2.3): 'astr_{B(y)/k(y)} : B(y) → B(y)ˇ est bijectif'",
    "check accent set after the parenthesis, like an exponent: B(y)ˇ (crop p112_astr_y.png)",
    "\\check{\\sh{B}(y)}: check over the whole expression", "symbol",
    r"\to\check{\sh{B}(y)}$ est bijectif", r"\to\sh{B}(y)^\vee$ est bijectif",
    note="Check-accent analogue of convention 5; written ^\\vee as the TeX writes the same raised check at (18.2.2) (Γ(U,B)ˇ) and (18.2.7) ((∧B)ˇ).")
add(112, "proof of (18.2.3): 'comme B(y)=B_y/m_yB_y et B(y)ˇ=B̌_y/m_yB̌_y'",
    "check accent after the parenthesis: B(y)ˇ (crop p112_astr_y.png)", "\\check{\\sh{B}(y)}", "symbol",
    r"et $\check{\sh{B}(y)}=", r"et $\sh{B}(y)^\vee=", note="As the previous finding.")
add(112, "proof of (18.2.3): 'l'homomorphisme astr_{B_y/O_{Y,y}} : B_y → B̌_y est lui aussi bijectif'",
    "slash (crop p112_astr_By.png)", "vertical bar", "symbol",
    r"\operatorname{astr}_{\sh{B}_y|\sh{O}_{Y,y}}:\sh{B}_y\to\check{\sh{B}}_y$ est lui",
    r"\operatorname{astr}_{\sh{B}_y/\sh{O}_{Y,y}}:\sh{B}_y\to\check{\sh{B}}_y$ est lui", note="Slash for the bar (see p. 111).")
add(112, "after (18.2.3): 'les conditions équivalentes b) et c) de (18.2.3)'", "labels italic as a whole (page_112_s3.png)",
    "$b)$, $c)$", "italics", r"équivalentes $b)$ et $c)$ de", r"équivalentes \emph{b)} et \emph{c)} de", note=LAB)
add(112, "Corollaire (18.2.4), label a)", "upright 'a)' (page_112_s3.png)", "\\item[a)]: italic", "convention",
    r"\item[a)] Il existe un voisinage ouvert $U$ de $y$ dans $Y$", r"\item[\textup{a)}] Il existe un voisinage ouvert $U$ de $y$ dans $Y$", conv=6, note=ITEM)
add(112, "Corollaire (18.2.4), label b)", "upright 'b)' (page_112_s4.png)", "\\item[b)]: italic", "convention",
    r"\item[b)] $\sh{B}_y$ est un", r"\item[\textup{b)}] $\sh{B}_y$ est un", conv=6, note=ITEM)
add(112, "(18.2.4) b): 'B_y ⊗_{O_{Y,y}} k(y) est une k(y)-algèbre séparable'", "two bold italic k (crop p112_cor4b_k.png)",
    "\\kappa(y) twice", "convention",
    r"\kappa(y)$ est une $\kappa(y)$-algèbre séparable", r"\boldsymbol{k}(y)$ est une $\boldsymbol{k}(y)$-algèbre séparable",
    conv=1, note=KAPPA)
add(112, "proof of (18.2.4): 'Il est clair que a) entraîne b)'", "labels italic as a whole (page_112_s4.png)",
    "$a)$, $b)$", "italics", r"Il est clair que $a)$ entraîne $b)$", r"Il est clair que \emph{a)} entraîne \emph{b)}", note=LAB)
add(112, "proof of (18.2.4): 'O_U-Module localement libre (0_I, 5.2.7)'", "bold 0 with subscript I (page_112_s4.png)",
    "plain 0", "convention", r"localement libre ($0_{\mathrm I}$, 5.2.7)", r"localement libre ($\mathbf{0}_{\mathrm I}$, 5.2.7)", conv=2)
add(112, "proof of (18.2.4): 'l'homomorphisme astr_{B_y/O_{Y,y}} : B_y → B̌_y étant bijectif'",
    "slash (crop p112_astr_By2.png)", "vertical bar", "symbol",
    r"\operatorname{astr}_{\sh{B}_y|\sh{O}_{Y,y}}:\sh{B}_y\to\check{\sh{B}}_y$ étant",
    r"\operatorname{astr}_{\sh{B}_y/\sh{O}_{Y,y}}:\sh{B}_y\to\check{\sh{B}}_y$ étant", note="Slash for the bar (see p. 111).")
add(112, "proof of (18.2.4): 'il résulte aussi de (0_I, 5.2.7)'", "bold 0 with subscript I (page_112_s4.png)", "plain 0",
    "convention", r"aussi de ($0_{\mathrm I}$, 5.2.7)", r"aussi de ($\mathbf{0}_{\mathrm I}$, 5.2.7)", conv=2)
add(112, "page break 112/113 inside 'choisi de sorte que | l'homomorphisme'",
    "p. 112 ends 'choisi de sorte que' (no stop); p. 113 continues the sentence ('l'homomorphisme astr ...', no indent) (page_112_s4.png, page_113_s1.png)",
    "blank line before \\oldpage[IV-4]{113} (and another after it): a paragraph break inside the sentence", "marker",
    r"choisi de sorte que" + N + N, r"choisi de sorte que" + N,
    note="The marker is at the right place. Part 1 of 2: the first p. 113 finding removes the blank line after \\oldpage[IV-4]{113}; apply both.")

# ---------------------------------------------------------------- p. 113
add(113, "top of page_113.tex: blank line after \\oldpage[IV-4]{113}", "p. 113 begins mid-sentence ('l'homomorphisme', no indent)",
    "blank line between the marker and 'l'homomorphisme'", "marker",
    r"\oldpage[IV-4]{113}" + N + N + r"l'homomorphisme", r"\oldpage[IV-4]{113}" + N + r"l'homomorphisme",
    note="Part 2 of 2 with the last p. 112 finding; both blank lines must go.")
add(113, "proof of (18.2.4), first line of p. 113: 'l'homomorphisme astr_{B|U,O_U} soit bijectif'",
    "'astr_{B|U, O_U}': a vertical bar after B, then U, a COMMA, O_U (crop p113_astrU.png)",
    "'\\sh{B}|U/\\sh{O}_U': slash where the print has the comma (silent correction)", "misprint_in_print",
    r"\operatorname{astr}_{\sh{B}|U/\sh{O}_U}", r"\operatorname{astr}_{\sh{B}|U,\sh{O}_U}", conf="medium",
    corrected=r"\operatorname{astr}_{\sh{B}|U/\sh{O}_U}",
    note="The notation of (18.2.2.2) needs the slash (the map astr of the O_U-algebra B|U); the print's comma looks like a slip. The fix restores the printed comma and touches nothing else; the bar of B|U is right in both.")
add(113, "proof of (18.2.4): 'Le fait que b) implique a)'", "labels italic as a whole (page_113_s1.png)", "$b)$, $a)$",
    "italics", r"Le fait que $b)$ implique $a)$", r"Le fait que \emph{b)} implique \emph{a)}", note=LAB)
add(113, "proof of (18.2.4), last words: 'résulte alors de (18.2.3).'",
    "'de' printed ITALIC at the start of the line, in roman text (crop p113_de_italic.png against the roman 'de' of 'il résulte de', crop p113_de_roman_cmp.png)",
    "roman 'de' (silent correction)", "misprint_in_print", r"alors de (18.2.3)", r"alors \textit{de} (18.2.3)",
    corrected=r"alors de (18.2.3)", note="Wrong-fount word (GLOBAL_ISSUES 29 pattern); corrected edition roman.")
add(113, "Corollaire (18.2.5): 'B_y ⊗_{O_{Y,y}} k(y) une k(y)-algèbre séparable'", "two bold italic k (crop p113_cor5_k.png)",
    "\\kappa(y) twice", "convention",
    r"\otimes_{\sh{O}_{Y,y}}\kappa(y)$ une $\kappa(y)$-algèbre",
    r"\otimes_{\sh{O}_{Y,y}}\boldsymbol{k}(y)$ une $\boldsymbol{k}(y)$-algèbre", conv=1, note=KAPPA)
add(113, "proof of (18.2.5): '(5.1.11 et 0_I, 2.1.3)'", "bold 0 with subscript I (crop p113_cor5_0I.png)", "plain 0",
    "convention", r"et $0_{\mathrm I}$, 2.1.3)", r"et $\mathbf{0}_{\mathrm I}$, 2.1.3)", conv=2)
add(113, "Corollaire (18.2.6): 'Tr_{B/O_Y} : B → O_Y'", "slash (crop p113_cor6.png)", "vertical bar", "symbol",
    r"\operatorname{Tr}_{\sh{B}|\sh{O}_Y}", r"\operatorname{Tr}_{\sh{B}/\sh{O}_Y}", note="Slash for the bar (see p. 111).")
add(113, "Corollaire (18.2.6): '(18.2.2) (aussi noté Tr_f) est surjectif'",
    "'(18.2.2) (aussi noté Tr_f)' roman with upright parentheses inside the italic statement; 'est surjectif' italic (crop p113_cor6_paren.png)",
    "italic", "convention", r"(18.2.2) (aussi noté $\operatorname{Tr}_f$)",
    r"\textup{(18.2.2) (aussi noté $\operatorname{Tr}_f$)}", conv=6)
add(113, "Remarques (18.2.7) (i): 'revêtement étale de Y. On notera que dans ce cas'",
    "no paragraph break: 'de Y.' ends a full line and 'On notera' starts the next line at the left margin, without the indent of the print's paragraphs (compare the indented 'On dit qu'un revêtement' below) (page_113_s2.png, page_113_s3.png)",
    "blank line: 'On notera' opens a new paragraph", "other",
    r"\emph{revêtement étale} de $Y$." + N + N + r"On notera", r"\emph{revêtement étale} de $Y$. On notera", conf="medium",
    note="The blank line before 'On dit qu'un revêtement étale' stays (indented paragraph in the print).")
add(113, "Remarques (18.2.7) (i): 'de préschémas isomorphes à Y'", "'isomorphes à' italic, 'à' included (crop p113_isomorphes.png)",
    "\\emph{isomorphes} à: 'à' outside the emphasis", "italics", r"\emph{isomorphes} à $Y$", r"\emph{isomorphes à} $Y$",
    note="Judged with the remark body roman, as the print sets it.")
add(113, "Remarques (18.2.7) (ii): 'soit u=astr_{B/O_Y} : B → B̌'", "slash (crop p113_wedge_line.png)", "vertical bar", "symbol",
    r"u=\operatorname{astr}_{\sh{B}|\sh{O}_Y}", r"u=\operatorname{astr}_{\sh{B}/\sh{O}_Y}", note="Slash for the bar (see p. 111).")
add(113, "Remarques (18.2.7) (ii): 'puissance extérieure n-ème'", "'n-ème' italic, '-ème' included (crop p113_wedge_line.png)",
    "$n$-ème: '-ème' roman in a roman body", "italics", r"extérieure $n$-ème", r"extérieure \emph{$n$-ème}",
    note="Judged with the remark body roman, as the print sets it.")
add(113, "Remarques (18.2.7) (ii): '∧^n u : ∧^n B → ∧^n B̌ = (∧^n B)ˇ de O_Y-Modules inversibles'",
    "formula in the running text, at the start of a text line, followed on the same line by 'de O_Y-Modules inversibles' (crop p113_wedge_line.png)",
    "displayed with \\[ ... \\]", "other",
    r"\[" + N + r"  \bigwedge^n u:\bigwedge^n\sh{B}\longrightarrow\bigwedge^n\check{\sh{B}}=(\bigwedge^n\sh{B})^\vee" + N + r"\]" + N + r"de $\sh{O}_Y$-Modules",
    r"$\bigwedge^n u:\bigwedge^n\sh{B}\to\bigwedge^n\check{\sh{B}}=(\bigwedge^n\sh{B})^\vee$ de $\sh{O}_Y$-Modules",
    note="Display set inline, as printed (GLOBAL_ISSUES 21). No words lost or added. Independent of the 'n-ème' edit just before it (no overlap).")
add(113, "Remarques (18.2.7) (ii): 'et par suite (0_I, 5.4.2) un élément'", "bold 0 with subscript I (crop p113_wedge_line.png)",
    "plain 0", "convention", r"($0_{\mathrm I}$, 5.4.2)", r"($\mathbf{0}_{\mathrm I}$, 5.4.2)", conv=2)
add(113, "Remarques (18.2.7) (ii), last line: 'encore appelé Idéal discriminant de X sur Y'",
    "only 'Idéal discriminant' italic; 'de X sur Y' roman (page_113_s4.png)", "\\emph{Idéal discriminant de $X$ sur $Y$}",
    "italics", r"\emph{Idéal discriminant de $X$ sur $Y$}", r"\emph{Idéal discriminant} de $X$ sur $Y$",
    note="Judged with the remark body roman, as the print sets it.")

# ---------------------------------------------------------------- p. 114
add(114, "first line of p. 114: 'il faut et il suffit que ∧^n u soit bijectif'",
    "the index n over ∧ and the u after it BOLD (side-by-side crop p114_n_side.png against the light n of ∧^n u, ∧^n B on p. 113; crop p114_line1_right.png against the light u of 'l'homomorphisme u' on the same line)",
    "normal weight (silent correction)", "misprint_in_print", r"$\bigwedge^n u$ soit bijectif",
    r"$\bigwedge^{\boldsymbol{n}}\boldsymbol{u}$ soit bijectif", conf="medium", corrected=r"$\bigwedge^n u$ soit bijectif",
    note="Wrong-fount letters (GLOBAL_ISSUES 29, rule of 4 Nov), at the end of the line; heavy impression of the last sorts is the alternative reading. The fix changes only the two letters.")
add(114, "'ce qui s'écrit aussi d_{X/Y}(y)≠0 pour tout y (0_I, 5.5.2)'", "bold 0 with subscript I (crop p114_top.png)", "plain 0",
    "convention", r"($0_{\mathrm I}$, 5.5.2)", r"($\mathbf{0}_{\mathrm I}$, 5.5.2)", conv=2)
add(114, "Proposition (18.2.8): 'Alors la fonction y ⇝ n(y)'", "wavy arrow (crop p114_leadsto.png)", "\\mapsto", "symbol",
    r"$y\mapsto n(y)$", r"$y\leadsto n(y)$", note="GLOBAL_ISSUES 33 (wavy arrow).")
add(114, "Proposition (18.2.8): '(donc constante dans un voisinage de y)'",
    "the parenthesis roman inside the italic statement, except 'constante', which is italic (crop p114_prop8_l3_l4.png)",
    "all italic", "convention", r"(donc constante dans un voisinage de $y$)",
    r"\textup{(donc \emph{constante} dans un voisinage de $y$)}", conv=6,
    note="'constante' italic inside the roman parenthesis is reproduced with \\emph (emphasis, or the compositor's italic carried over; same output either way).")
add(114, "proof of (18.2.8): 'chaque fibre f^{-1}(y) est géométriquement réduite sur k(y)'", "bold italic k (crop p114_k.png)",
    "\\kappa(y)", "convention", r"réduite sur $\kappa(y)$", r"réduite sur $\boldsymbol{k}(y)$", conv=1, note=KAPPA)
add(114, "Corollaire (18.2.9): '(autrement dit, que X soit un revêtement étale de Y)'",
    "the parenthesis roman inside the italic statement, 'revêtement étale' italic in it (crop p114_cor9.png)", "all italic",
    "convention", r"(autrement dit, que $X$ soit un revêtement étale de $Y$)",
    r"\textup{(autrement dit, que $X$ soit un \emph{revêtement étale} de $Y$)}", conv=6)
add(114, "Remarques (18.2.10) (i): '« droite affine avec un point dédoublé » (I, 5.5.11)'",
    "bold I (crop p114_I5511.png); a genuine EGA I reference", "plain I", "convention", r"(I, 5.5.11)",
    r"(\textbf{I}, 5.5.11)", conv=2)
add(114, "Remarques (18.2.10) (ii): 'toute fibre f^{-1}(y) est finie ((17.6.1) et (I, 6.2.2)), de la caractérisation'",
    "both references inside an outer pair of parentheses: '((17.6.1) et (I, 6.2.2))' (crop p114_I622.png)",
    "'(17.6.1) et (I, 6.2.2),': outer parentheses missing", "missing", r"est finie (17.6.1)", r"est finie ((17.6.1)",
    note="Part 1 of 2 (opening parenthesis); the closing one is two findings below. The convention-2 edit between them does not overlap either part.")
add(114, "Remarques (18.2.10) (ii): '(I, 6.2.2)'", "bold I (crop p114_I622.png); a genuine EGA I reference", "plain I",
    "convention", r"et (I, 6.2.2", r"et (\textbf{I}, 6.2.2", conv=2)
add(114, "Remarques (18.2.10) (ii): closing outer parenthesis after '(I, 6.2.2)'", "'(I, 6.2.2)),' (crop p114_I622.png)",
    "one closing parenthesis", "missing", r"), de la caractérisation", r")), de la caractérisation",
    note="Part 2 of 2 of the outer parentheses (part 1 two findings above).")
add(114, "Proposition (18.3.1), label (i)", "upright '(i)' (crop p114_prop31_i.png)", "\\item[(i)]: italic", "convention",
    r"\item[(i)] Pour que $B$ soit une $A$-algèbre non ramifiée", r"\item[\textup{(i)}] Pour que $B$ soit une $A$-algèbre non ramifiée", conv=6, note=ITEM)
add(114, "Proposition (18.3.1) (i), end of its first line: 'que B soit un A-module'",
    "the final e of 'module' BOLD italic (side-by-side crop p114_e_side.png against 'module' of (ii), line 2; the 'modul' before it is light)",
    "normal weight (silent correction)", "misprint_in_print", r"soit un $A$-module de présentation finie et que",
    r"soit un $A$-modul\textbf{e} de présentation finie et que", conf="low",
    corrected=r"soit un $A$-module de présentation finie et que",
    note="Wrong-fount letter by the 4 Nov rule (GLOBAL_ISSUES 29); it is the last letter of the line, so a sort printing heavy is the alternative reading. Changes only the letter.")
add(114, "Proposition (18.3.1), label (ii)", "upright '(ii)' (crop p114_prop31_ii.png)", "\\item[(ii)]: italic", "convention",
    r"\item[(ii)] Supposons de plus que $B$ soit une $A$-algèbre finie", r"\item[\textup{(ii)}] Supposons de plus que $B$ soit une $A$-algèbre finie", conv=6, note=ITEM)
add(114, "Proposition (18.3.1) (ii), end of its first line: 'Pour que B soit une A-algèbre étale,'",
    "'étale,' BOLD italic, the comma included (side-by-side crop p114_etale_side.png: heavier than 'algèbre' just before it)",
    "normal weight (silent correction)", "misprint_in_print", r"Pour que $B$ soit une $A$-algèbre étale, il faut et il suffit que $B$ soit un $A$-module projectif", r"Pour que $B$ soit une $A$-algèbre \textbf{étale,} il faut et il suffit que $B$ soit un $A$-module projectif",
    conf="medium", corrected=r"Pour que $B$ soit une $A$-algèbre étale, il faut et il suffit que $B$ soit un $A$-module projectif",
    note="Wrong-fount word, as the bold italic 'est' of p. 42 (GLOBAL_ISSUES 97); at the line end, so heavy impression is the alternative reading. Changes only the word.")
add(114, "after (18.3.1): 'de noyau J_{B/A} (0, 20.4.1)'", "bold 0, no subscript (crop p114_0_2041.png)", "plain 0",
    "convention", r"(0, 20.4.1)", r"(\textbf{0}, 20.4.1)", conv=2)
add(114, "page break 114/115 inside 'Dire | que B est une A-algèbre non ramifiée'",
    "p. 114 ends '(1.4.6). Dire'; p. 115 continues the sentence ('que B est une A-algèbre non ramifiée signifie alors', no indent) (page_114_s4.png, page_115_s1.png)",
    "blank line before \\oldpage[IV-4]{115} (and another after it): a paragraph break inside the sentence", "marker",
    r"(1.4.6). Dire" + N + N, r"(1.4.6). Dire" + N,
    note="The marker is at the right place. Part 1 of 2: the blank line AFTER \\oldpage[IV-4]{115} (p. 115 segment, outside this batch) must go too.")

json.dump(F, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "findings written to", OUT)
