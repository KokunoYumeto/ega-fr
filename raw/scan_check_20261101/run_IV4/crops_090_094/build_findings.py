"""Build findings_090_094.json; check every 'old' against page_NNN.tex and simulate apply_fixes.py on the source.
Newlines in edit strings are written as the pilcrow sign and converted below."""
import json
import pathlib
import re

RUN = pathlib.Path(r'user\Documents\ega_scan_check_20261101\run_IV4')
SRC = pathlib.Path(r'user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20'
                   r'\diplomatic\packages\IV4\native\ega4\ega4-17-fr.tex')
OUT = RUN / 'findings_090_094.json'
NL = '\u00b6'

F = []


def add(page, where, scan, tex, kind, old, new, conv=None, conf='high', note='', corrected=None, after_prev=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if old is None else dict(old=old.replace(NL, '\n'), new=new.replace(NL, '\n')))
    if kind == 'misprint_in_print':
        d['corrected'] = corrected.replace(NL, '\n')
    d['note'] = note
    d['_after_prev'] = after_prev  # old taken from the text after an earlier fix (checked sequentially)
    F.append(d)


VO = 'Italic Omega for the sheaf of differentials (GLOBAL_ISSUES 92).'
LBL6 = 'Label printed upright inside the italic statement.'
REF6 = 'Reference printed upright inside the italic statement.'
LBLR = 'Labels in roman text are italic in the print (GLOBAL_ISSUES 88).'
PAR = 'Paragraph break as printed (GLOBAL_ISSUES 80 pattern).'

# ---------------------------------------------------------------- page 90
p = 90
add(p, "(17.13.1.3)", "both Omegas italic", "upright \\Omega", 'font',
    r"\xrightarrow{\alpha}\Omega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}\to\Omega^1_{Y'/S}\to0.",
    r"\xrightarrow{\alpha}\varOmega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}\to\varOmega^1_{Y'/S}\to0.", note=VO)
add(p, "Proposition (17.13.2): 'Les notations étant celles de (17.13.1),'", "reference upright", "italic", 'convention',
    r"celles de (17.13.1),", r"celles de \textup{(17.13.1)},", conv=6, note=REF6)
add(p, "Proposition (17.13.2): 'soient x' un point de Y''", "'soient' (crop p90_s1_prop.png)", "'soit'", 'word',
    r"soit $x'$ un point", r"soient $x'$ un point")
add(p, "Proposition (17.13.2): 'au point x (17.10.1), n celle de X''", "reference upright", "italic", 'convention',
    r"au point $x$ (17.10.1),", r"au point $x$ \textup{(17.10.1)},", conv=6, note=REF6)
add(p, "Proposition (17.13.2), label a)", "'a)' upright", "italic label", 'convention',
    r"\item[a)] $Y'$ est lisse", r"\item[\textup{a)}] $Y'$ est lisse", conv=6, note=LBL6)
add(p, "Proposition (17.13.2), label b)", "'b)' upright", "italic label", 'convention',
    r"\item[b)] L'homomorphisme $\alpha", r"\item[\textup{b)}] L'homomorphisme $\alpha", conv=6, note=LBL6)
add(p, "(17.13.2) b): 'g^*(N_{Y/X})⊗_{O_Y'} k(x')'", "bold italic k", "plain k", 'convention',
    r"g^*(\sh{N}_{Y/X})\otimes_{\sh{O}_{Y'}}k(x')", r"g^*(\sh{N}_{Y/X})\otimes_{\sh{O}_{Y'}}\boldsymbol{k}(x')", conv=1)
add(p, "(17.13.2) b): '→ Ω^1_{X'/S}⊗_{O_X'} k(x')'", "italic Omega", "upright \\Omega", 'font',
    r"(x')\to\Omega^1_{X'/S}\otimes_{\sh{O}_{X'}}k(x')$ déduit", r"(x')\to\varOmega^1_{X'/S}\otimes_{\sh{O}_{X'}}k(x')$ déduit",
    note=VO + " Apply before the next finding (the k of k(x') follows in this 'old').")
add(p, "(17.13.2) b): 'Ω^1_{X'/S}⊗_{O_X'} k(x') déduit'", "bold italic k", "plain k", 'convention',
    r"_{\sh{O}_{X'}}k(x')$ déduit", r"_{\sh{O}_{X'}}\boldsymbol{k}(x')$ déduit", conv=1,
    note="Apply after the Omega fix just before (its 'old' contains this k).")
add(p, "(17.13.2) b): 'déduit de l'homomorphisme α de (17.13.1.3) est injectif'", "reference upright", "italic",
    'convention', r"$\alpha$ de (17.13.1.3) est injectif", r"$\alpha$ de \textup{(17.13.1.3)} est injectif", conv=6,
    note=REF6)
add(p, "Proposition (17.13.2): 'Soit s l'image canonique' after the list", "new indented paragraph (page_090_s2.png)",
    "text follows \\end{enumerate} directly (no indent)", 'other',
    r"\end{enumerate}¶Soit $s$", r"\end{enumerate}¶¶Soit $s$", note=PAR)
add(p, "Proposition (17.13.2): 'x' soit rationnel sur k(s)'", "bold italic k", "plain k", 'convention',
    r"rationnel sur $k(s)$. Alors", r"rationnel sur $\boldsymbol{k}(s)$. Alors", conv=1)
add(p, "Proposition (17.13.2): 'Alors les conditions a) et b) sont aussi équivalentes'", "labels upright", "italic",
    'convention', r"Alors les conditions a) et b) sont aussi", r"Alors les conditions \textup{a)} et \textup{b)} sont aussi",
    conv=6, note=LBL6)
add(p, "Proposition (17.13.2), label b')", "'b')' upright", "italic label", 'convention',
    r"\item[b')] L'homomorphisme transposé", r"\item[\textup{b$'$)}] L'homomorphisme transposé", conv=6,
    note=LBL6 + " Prime written b$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(p, "(17.13.2) b'), display: '(N_{Y/X}⊗_{O_Y} k(x))ˇ'", "k(x), no prime (crop p90_bprime_disp.png)", "k(x')",
    'formula', r"(x'))^\vee", r"(x))^\vee",
    note="The print is correct as printed (N_{Y/X} is an O_Y-Module; k(x)=k(x') here); same reading in the proof on p. 91. Independent of the convention-1 edit of the same k.")
add(p, "(17.13.2) b'), display: '(N_{Y/X}⊗_{O_Y} k(x))ˇ'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_Y}k(x", r"\otimes_{\sh{O}_Y}\boldsymbol{k}(x", conv=1)
add(p, "(17.13.2) b'): '(cf. (16.5.12)) est surjectif'", "the whole parenthesis upright", "italic", 'convention',
    r"(cf. (16.5.12)) est surjectif", r"\textup{(cf. (16.5.12))} est surjectif", conv=6)
add(p, "Proposition (17.13.2): 'De plus, lorsque ...' after the list", "new indented paragraph (page_090_s2.png)",
    "text follows \\end{enumerate} directly (no indent)", 'other',
    r"\end{enumerate}¶De plus, lorsque", r"\end{enumerate}¶¶De plus, lorsque", note=PAR)
add(p, "Proposition (17.13.2): 'lorsque les conditions a) et b) sont vérifiées en x''", "labels upright", "italic",
    'convention', r"lorsque les conditions a) et b) sont vérifiées en",
    r"lorsque les conditions \textup{a)} et \textup{b)} sont vérifiées en", conv=6, note=LBL6)
add(p, "(17.13.2.1)", "both Omegas italic", "upright \\Omega", 'font',
    r"0\to g^*(\sh{N}_{Y/X})\xrightarrow{\alpha}\Omega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}\to\Omega^1_{Y'/S}\to0",
    r"0\to g^*(\sh{N}_{Y/X})\xrightarrow{\alpha}\varOmega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}\to\varOmega^1_{Y'/S}\to0",
    note=VO)
add(p, "Proposition (17.13.2): 'obtenue en ajoutant un 0 à (17.13.1.3), est exacte'", "reference upright", "italic",
    'convention', r"un $0$ à (17.13.1.3), est exacte", r"un $0$ à \textup{(17.13.1.3)}, est exacte", conv=6, note=REF6)
add(p, "proof of (17.13.2): 'les conditions équivalentes a) et b) sont vérifiées au point x''",
    "a) and b) italic (crop p90_s3_xprime.png)", "upright", 'italics',
    r"équivalentes a) et b) sont vérifiées au point", r"équivalentes \emph{a)} et \emph{b)} sont vérifiées au point",
    note=LBLR)
add(p, "proof of (17.13.2), display 'δ⊗1 : N_{Y'/X'}⊗_{O_Y'} k(x') → Ω^1_{X'/S}⊗_{O_X'} k(x')'", "italic Omega",
    "upright \\Omega", 'font', r"(x')\to\Omega^1_{X'/S}\otimes_{\sh{O}_{X'}}k(x')¶\]",
    r"(x')\to\varOmega^1_{X'/S}\otimes_{\sh{O}_{X'}}k(x')¶\]",
    note=VO + " Apply before the second k fix of this display (its 'old' contains that k).")
add(p, "proof of (17.13.2), display δ⊗1: 'N_{Y'/X'}⊗_{O_Y'} k(x')'", "bold italic k", "plain k", 'convention',
    r"\sh{N}_{Y'/X'}\otimes_{\sh{O}_{Y'}}k(x')", r"\sh{N}_{Y'/X'}\otimes_{\sh{O}_{Y'}}\boldsymbol{k}(x')", conv=1)
add(p, "proof of (17.13.2), display δ⊗1: 'Ω^1_{X'/S}⊗_{O_X'} k(x')'", "bold italic k", "plain k", 'convention',
    r"_{\sh{O}_{X'}}k(x')¶\]", r"_{\sh{O}_{X'}}\boldsymbol{k}(x')¶\]", conv=1,
    note="Apply after the Omega fix of this display (listed before).")
add(p, "proof of (17.13.2): '(0, 19.1.12)'", "bold 0", "plain 0", 'convention',
    r"(0, 19.1.12)", r"(\textbf{0}, 19.1.12)", conv=2)
add(p, "proof of (17.13.2): 'de ce que Ω^1_{X'/S} est un O_X'-Module'", "italic Omega", "upright \\Omega", 'font',
    r"de ce que $\Omega^1_{X'/S}$ est un", r"de ce que $\varOmega^1_{X'/S}$ est un", note=VO)
add(p, "proof of (17.13.2): 'comme alors Ω^1_{Y'/S} est aussi'", "italic Omega", "upright \\Omega", 'font',
    r"comme alors $\Omega^1_{Y'/S}$", r"comme alors $\varOmega^1_{Y'/S}$", note=VO)
add(p, "(17.13.2.2)", "both Omegas italic", "upright \\Omega", 'font',
    r"0\to\sh{N}_{Y'/X'}\to\Omega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}\to\Omega^1_{Y'/S}\to0",
    r"0\to\sh{N}_{Y'/X'}\to\varOmega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}\to\varOmega^1_{Y'/S}\to0", note=VO)
add(p, "page break 90/91 inside 'les conditions précédentes équivalent à dire que cet homomorphisme est | bijectif'",
    "p. 90 ends 'cet homomorphisme est', p. 91 begins 'bijectif au point x'' (page_090_s4.png, page_091_s1.png)",
    "blank line before \\oldpage[IV-4]{91} (and another after it): a paragraph break inside the sentence", 'marker',
    r"cet homomorphisme est¶¶", r"cet homomorphisme est¶",
    note="The marker is at the right place. Part 1 of 2: the first p. 91 finding removes the blank line after \\oldpage[IV-4]{91}; apply both.")

# ---------------------------------------------------------------- page 91
p = 91
add(p, "top of page_091.tex: blank line after \\oldpage[IV-4]{91}", "p. 91 begins mid-sentence ('bijectif au point x'')",
    "blank line between the marker and 'bijectif'", 'marker',
    r"\oldpage[IV-4]{91}¶¶", r"\oldpage[IV-4]{91}¶",
    note="Part 2 of 2 with the last p. 90 finding; both blank lines must go.")
add(p, "first word: 'bijectif au point x''", "'bijectif' italic (crop p91_top_lines.png)", "upright", 'italics',
    r"bijectif au point $x'$ (Bourbaki", r"\emph{bijectif} au point $x'$ (Bourbaki")
add(p, "'(0_I, 5.2.7)'", "bold 0 with subscript I", "plain 0", 'convention',
    r"(0$_{\mathrm I}$, 5.2.7)", r"($\mathbf{0}_{\mathrm I}$, 5.2.7)", conv=2)
add(p, "'cela entraîne évidemment b)'", "b) italic", "upright", 'italics',
    r"évidemment b), ainsi", r"évidemment \emph{b)}, ainsi", note=LBLR)
add(p, "display (factorisation of α⊗1): 'Ω^1_{X'/S}⊗k(x')'", "italic Omega", "upright \\Omega", 'font',
    r"\xrightarrow{\delta\otimes1}\Omega^1_{X'/S}", r"\xrightarrow{\delta\otimes1}\varOmega^1_{X'/S}", note=VO)
add(p, "display (factorisation of α⊗1): 'g^*(N_{Y/X})⊗k(x')'", "bold italic k", "plain k", 'convention',
    r"g^*(\sh{N}_{Y/X})\otimes k(x')", r"g^*(\sh{N}_{Y/X})\otimes\boldsymbol{k}(x')", conv=1)
add(p, "display (factorisation of α⊗1): 'N_{Y'/X'}⊗k(x')'", "bold italic k", "plain k", 'convention',
    r"\sh{N}_{Y'/X'}\otimes k(x')", r"\sh{N}_{Y'/X'}\otimes\boldsymbol{k}(x')", conv=1)
add(p, "display (factorisation of α⊗1): 'Ω^1_{X'/S}⊗k(x')'", "bold italic k", "plain k", 'convention',
    r"_{X'/S}\otimes k(x')", r"_{X'/S}\otimes\boldsymbol{k}(x')", conv=1)
add(p, "'ce qui achève de prouver l'équivalence de a) et b), en vertu de (17.10.2)'", "a) and b) italic", "upright",
    'italics', r"l'équivalence de a) et b), en vertu", r"l'équivalence de \emph{a)} et \emph{b)}, en vertu", note=LBLR)
add(p, "'Ω^1_{Y'/S} est de rang n—c en ce point'", "italic Omega", "upright \\Omega", 'font',
    r"$\Omega^1_{Y'/S}$ est de rang", r"$\varOmega^1_{Y'/S}$ est de rang", note=VO)
add(p, "'Reste à montrer l'équivalence de b) et b')'", "b) and b') italic", "upright", 'italics',
    r"l'équivalence de b) et b') lorsque", r"l'équivalence de \emph{b)} et \emph{b')} lorsque", note=LBLR)
add(p, "'lorsque x' est rationnel sur k(s) (ce qui implique'", "bold italic k", "plain k", 'convention',
    r"rationnel sur $k(s)$ (ce qui", r"rationnel sur $\boldsymbol{k}(s)$ (ce qui", conv=1)
add(p, "'alors g^*(N_{Y/X})⊗_{O_Y'} k(x') s'identifie'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_{Y'}}k(x')$ s'identifie", r"\otimes_{\sh{O}_{Y'}}\boldsymbol{k}(x')$ s'identifie", conv=1)
add(p, "'s'identifie à N_{Y/X}⊗_{O_Y} k(x), et puisque'", "k(x), no prime (crop p91_kx_identifie.png)", "k(x')",
    'formula', r"(x')$, et puisque", r"(x)$, et puisque",
    note="The print is correct (N_{Y/X} is an O_Y-Module; x' and x are rational over k(s)). Independent of the convention-1 edit of the same k.")
add(p, "'s'identifie à N_{Y/X}⊗_{O_Y} k(x)'", "bold italic k", "plain k", 'convention',
    r"à $\sh{N}_{Y/X}\otimes_{\sh{O}_Y}k(x", r"à $\sh{N}_{Y/X}\otimes_{\sh{O}_Y}\boldsymbol{k}(x", conv=1)
add(p, "display '0 → N_{Y/X} → Ω^1_{X/S}⊗_{O_X} O_Y → Ω^1_{Y/S} → 0'", "both Omegas italic", "upright \\Omega", 'font',
    r"0\to\sh{N}_{Y/X}\to\Omega^1_{X/S}\otimes_{\sh{O}_X}\sh{O}_Y\to\Omega^1_{Y/S}\to0",
    r"0\to\sh{N}_{Y/X}\to\varOmega^1_{X/S}\otimes_{\sh{O}_X}\sh{O}_Y\to\varOmega^1_{Y/S}\to0", note=VO)
add(p, "'le dual de N_{Y/X}⊗_{O_Y} k(x)'", "bold italic k", "plain k", 'convention',
    r"dual de $\sh{N}_{Y/X}\otimes_{\sh{O}_Y}k(x)$", r"dual de $\sh{N}_{Y/X}\otimes_{\sh{O}_Y}\boldsymbol{k}(x)$", conv=1)
add(p, "'d'où l'équivalence de b) et b').'", "b) and b') italic", "upright", 'italics',
    r"d'où l'équivalence de b) et b').", r"d'où l'équivalence de \emph{b)} et \emph{b')}.", note=LBLR)
add(p, "Définition (17.13.3): 'Avec les notations de (17.13.1),'", "reference upright", "italic", 'convention',
    r"Avec les notations de (17.13.1), on dit", r"Avec les notations de \textup{(17.13.1)}, on dit", conv=6, note=REF6)
add(p, "Définition (17.13.3): 'f est transversal à Y'", "'transversal' italic like the rest of the statement",
    "\\emph{transversal}: upright inside the italic statement", 'convention',
    r"\emph{transversal} à $Y$", r"transversal à $Y$", conv=6)
add(p, "Définition (17.13.3): 'les conditions équivalentes a), b) de (17.3.2)'", "labels and reference upright",
    "italic", 'convention', r"équivalentes a), b) de (17.13.2) sont", r"équivalentes \textup{a), b)} de \textup{(17.13.2)} sont",
    conv=6, note="Apply before the misprint finding that follows (same reference).")
add(p, "Définition (17.13.3): reference '(17.3.2)'",
    "the print has (17.3.2) (crop p91_def_line3.png); the conditions a), b) are those of Proposition (17.13.2)",
    "(17.13.2): silent correction", 'misprint_in_print',
    r"\textup{(17.13.2)} sont", r"\textup{(17.3.2)} sont", corrected=r"\textup{(17.13.2)} sont",
    note="Not in the errata (Liste 3). 'old' is the text after the convention-6 edit just before (apply that first); this edit changes only the number.",
    after_prev=True)
add(p, "Remarques (17.13.4) (i): 'relativement à k(s).'", "bold italic k", "plain k", 'convention',
    r"relativement à $k(s)$.", r"relativement à $\boldsymbol{k}(s)$.", conv=1)
add(p, "Remarques (17.13.4) (ii): 'transversal à Y en tous les points de Y'_s'", "'tous' italic (page_091_s3.png)",
    "upright", 'italics', r"à $Y$ en tous les points", r"à $Y$ en \emph{tous} les points",
    note="Judged with the remark body roman (document-wide decision).")
add(p, "Remarques (17.13.4) (ii): 'Lorsque X, Y et X' sont plats ...'",
    "no paragraph break: 'Lorsque' starts a full line at the left margin, without indent (crop p91_s3_lorsque.png)",
    "blank line before 'Lorsque': new indented paragraph", 'other',
    r"\emph{ouvert} dans $S$.¶¶Lorsque $X$", r"\emph{ouvert} dans $S$.¶Lorsque $X$")
add(p, "Remarques (17.13.4) (ii): 'relativement à k(s), est ouvert dans Y''", "bold italic k", "plain k", 'convention',
    r"relativement à $k(s)$, est", r"relativement à $\boldsymbol{k}(s)$, est", conv=1)
add(p, "Remarques (17.13.4) (ii): '(relativement à k(s))'", "bold italic k", "plain k", 'convention',
    r"(relativement à $k(s)$)", r"(relativement à $\boldsymbol{k}(s)$)", conv=1)

# ---------------------------------------------------------------- page 92
p = 92
add(p, "Remarques (17.13.4) (iv): 'La condition b) de (17.13.2)'", "b) italic", "plain b) (italic only through the remark environment)",
    'italics', r"La condition b) de", r"La condition \emph{b)} de",
    note="Judged with the remark body roman (document-wide decision); GLOBAL_ISSUES 88.")
add(p, "Remarques (17.13.4) (iv): 'α : g^*(N_{Y/X}) → Ω^1_{X'/S}⊗ O_Y''", "italic Omega", "upright \\Omega", 'font',
    r"\to\Omega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}$ est", r"\to\varOmega^1_{X'/S}\otimes_{\sh{O}_{X'}}\sh{O}_{Y'}$ est",
    note=VO)
add(p, "Remarques (17.13.4) (iv): 'relativement à Y' (11.9.18)'",
    "(11.9.18), light figures, no comma (crop p92_iv_ref.png): Remarque (11.9.18) of EGA IV on universally injective homomorphisms",
    "(II, 9.18)", 'number', r"(II, 9.18)", r"(11.9.18)")
add(p, "(17.13.5): 'on sait alors (I, 5.3.5)'", "bold I", "plain I", 'convention',
    r"(I, 5.3.5)", r"(\textbf{I}, 5.3.5)", conv=2)
add(p, "diagram (17.13.5.1), top right corner", "'Y×_X Z = T'", "'T=Y\\times_X Z'", 'formula',
    r"T=Y\times_X Z \ar[l]", r"Y\times_X Z=T \ar[l]")
add(p, "diagram (17.13.5.1): label Δ of the left vertical arrow", "Δ to the LEFT of the arrow (page_092_s1.png)",
    "\\ar[d]^{\\Delta}: label to the right", 'other', r"X \ar[d]^{\Delta}", r"X \ar[d]_{\Delta}",
    note="j (right of its arrow) and u (below its arrow, \\ar[l]^{u}) are as printed.")
add(p, "(17.13.5): 'Comme Δ est une S-immersion (I, 5.3.9)'", "bold I", "plain I", 'convention',
    r"(I, 5.3.9)", r"(\textbf{I}, 5.3.9)", conv=2)
add(p, "(17.13.5): 'ce qui correspond à Ω^1_{X'/S} dans (17.13.1)'", "italic Omega", "upright \\Omega", 'font',
    r"correspond à $\Omega^1_{X'/S}$ dans", r"correspond à $\varOmega^1_{X'/S}$ dans", note=VO)
add(p, "(17.13.5): '(Ω^1_{Y/S}⊗ O_{Y×_SZ})⊕(Ω^1_{Z/S}⊗ O_{Y×_SZ})'", "both Omegas italic", "upright \\Omega", 'font',
    r"$(\Omega^1_{Y/S}\otimes_{\sh{O}_Y}\sh{O}_{Y\times_SZ})\oplus(\Omega^1_{Z/S}",
    r"$(\varOmega^1_{Y/S}\otimes_{\sh{O}_Y}\sh{O}_{Y\times_SZ})\oplus(\varOmega^1_{Z/S}", note=VO)
add(p, "(17.13.5): 'est ici par définition Ω^1_{X/S} (16.3.1)'", "italic Omega", "upright \\Omega", 'font',
    r"par définition $\Omega^1_{X/S}$", r"par définition $\varOmega^1_{X/S}$", note=VO)
add(p, "(17.13.5.2)", "all four Omegas italic", "upright \\Omega", 'font',
    r"\Omega^1_{X/S}\otimes_{\sh{O}_X}\sh{O}_T\xrightarrow{\rho}¶(\Omega^1_{Y/S}\otimes_{\sh{O}_Y}\sh{O}_T)\oplus¶(\Omega^1_{Z/S}\otimes_{\sh{O}_Z}\sh{O}_T)¶\xrightarrow{\sigma}\Omega^1_{T/S}\to0",
    r"\varOmega^1_{X/S}\otimes_{\sh{O}_X}\sh{O}_T\xrightarrow{\rho}¶(\varOmega^1_{Y/S}\otimes_{\sh{O}_Y}\sh{O}_T)\oplus¶(\varOmega^1_{Z/S}\otimes_{\sh{O}_Z}\sh{O}_T)¶\xrightarrow{\sigma}\varOmega^1_{T/S}\to0",
    note=VO)
add(p, "(17.13.5): 'Tenant compte d'abord de (16.4.23) et de (0, 20.5.2)'", "bold 0", "plain 0", 'convention',
    r"(0, 20.5.2)", r"(\textbf{0}, 20.5.2)", conv=2)
add(p, "after (17.13.5.3): 'D'autre part, pour évaluer ρ'", "new indented paragraph (page_092_s3.png)",
    "follows \\] without a blank line (no indent)", 'other',
    r"\]¶D'autre part, pour évaluer", r"\]¶¶D'autre part, pour évaluer", note="Paragraph break after a display (GLOBAL_ISSUES 47 pattern).")
add(p, "display 'ρ' : Ω^1_{X/S} → Ω^1_{(X×_SX)/S}⊗ O_X'", "both Omegas italic", "upright \\Omega", 'font',
    r"\rho':\Omega^1_{X/S}\to\Omega^1_{(X\times_SX)/S}", r"\rho':\varOmega^1_{X/S}\to\varOmega^1_{(X\times_SX)/S}", note=VO)
add(p, "(17.13.5): 'l'homomorphisme δ de (0, 20.5.11.2)'", "bold 0", "plain 0", 'convention',
    r"(0, 20.5.11.2)", r"(\textbf{0}, 20.5.11.2)", conv=2)
add(p, "(17.13.5): 'et C par B = B⊗_A B)/J_{B/A}'",
    "the opening parenthesis is missing: 'B=B⊗_A B)/𝔍_{B/A}' (crops p92_s3_affine.png, p92_frakJ.png)",
    "B=(B⊗_AB)/J: silent correction", 'misprint_in_print',
    r"$B=(B\otimes_AB)/", r"$B=B\otimes_AB)/", corrected=r"$B=(B\otimes_AB)/",
    note="Not in the errata (Liste 3). The edit removes only the parenthesis.")
add(p, "(17.13.5): 'la classe de x⊗1 − 1⊗x mod. J^2_{B/A}'", "'mod.' with a full stop, no parentheses (crop p92_frakJ.png)",
    "\\pmod{...}: '(mod J^2)' in parentheses, no full stop", 'formula',
    r"x\pmod{\mathfrak J_{B/A}^2}$", r"x$ mod. $\mathfrak J_{B/A}^2$",
    note="Written as the other 'mod.' of ega4-17 (line 438: 'mod. $\\mathfrak m^2$').")
add(p, "(17.13.5): 'dans Ω^1_{(B⊗_AB)/A}⊗_{(B⊗_AB)} B'", "subscript of ⊗ in parentheses '(B⊗_A B)' (crop p92_s3_dans.png); this Omega is upright (module), as in the TeX",
    "\\otimes_{B\\otimes_AB}", 'formula', r"\otimes_{B\otimes_AB}B$; mais", r"\otimes_{(B\otimes_AB)}B$; mais")
add(p, "(17.13.5): 'π^(1) et π^(2) de Ω^1_{X/S} dans Ω^1_{(X×_SX)/S}⊗ O_X'", "both Omegas italic", "upright \\Omega",
    'font', r"de $\Omega^1_{X/S}$ dans $\Omega^1_{(X\times_SX)/S}", r"de $\varOmega^1_{X/S}$ dans $\varOmega^1_{(X\times_SX)/S}",
    note=VO)
add(p, "(17.13.5): 'correspondant respectivement à la première et la seconde projection'",
    "'à la première et la seconde' (crop p92_s4_seconde.png)", "'à la première et à la seconde'", 'extra',
    r"à la première et à la seconde", r"à la première et la seconde")
add(p, "printed p. 93, l. 1: 'ρ'' : Ω^1_{(X×_SX)/S}⊗ O_{(Y×_SZ)} → Ω^1_{(Y×_SZ)/S}'",
    "set in the line: 'dérer l'homomorphisme ρ'' : ... correspondant par' (crop p93_top.png)",
    "displayed formula", 'other',
    r"\[¶\rho'':\Omega^1_{(X\times_SX)/S}\otimes_{\sh{O}_{X\times_SX}}\sh{O}_{Y\times_SZ}\to\Omega^1_{(Y\times_SZ)/S}¶\]¶",
    r"$\rho'':\Omega^1_{(X\times_SX)/S}\otimes_{\sh{O}_{X\times_SX}}\sh{O}_{Y\times_SZ}\to\Omega^1_{(Y\times_SZ)/S}$ ",
    note="Text of printed p. 93 that still lies in the p. 92 segment. Apply before the three fixes inside this formula (listed next) and before the marker move (last p. 92 finding).")
add(p, "printed p. 93, l. 1, ρ'': 'O_{(Y×_SZ)}'", "subscript in parentheses (crop p93_top.png)", "\\sh{O}_{Y\\times_SZ}",
    'formula', r"\sh{O}_{Y\times_SZ}\to", r"\sh{O}_{(Y\times_SZ)}\to",
    note="Printed p. 93 (p. 92 segment); apply after the inline edit above, before the marker move.")
add(p, "printed p. 93, l. 1, ρ'': 'Ω^1_{(X×_SX)/S}'", "italic Omega", "upright \\Omega", 'font',
    r"\rho'':\Omega^1_{(X\times_SX)/S}", r"\rho'':\varOmega^1_{(X\times_SX)/S}",
    note=VO + " Printed p. 93 (p. 92 segment); apply after the inline edit above, before the marker move.")
add(p, "printed p. 93, l. 1, ρ'': 'Ω^1_{(Y×_SZ)/S}'", "italic Omega", "upright \\Omega", 'font',
    r"\to\Omega^1_{(Y\times_SZ)/S}", r"\to\varOmega^1_{(Y\times_SZ)/S}",
    note=VO + " Printed p. 93 (p. 92 segment); apply after the inline edit above, before the marker move.")
add(p, "printed p. 93: 'il résulte de ce qui précède que l'on a, avec les notations de (16.4.18)' before (17.13.5.4)",
    "no comma after (16.4.18) (crop p93_top.png)", "comma", 'punctuation',
    r"notations de (16.4.18),", r"notations de (16.4.18)",
    note="Printed p. 93 (p. 92 segment); apply before the marker move.")
add(p, "page break 92/93 inside the word 'consi-|dérer'",
    "p. 92 ends 'il faut d'abord consi-', p. 93 begins 'dérer l'homomorphisme ρ'' : ...' (page_092_s4.png, page_093_s1.png)",
    "\\oldpage[IV-4]{93} stands before 'Ceci dit', after (17.13.5.4): the end of the p. 92 segment (from 'dérer') belongs to printed p. 93",
    'marker', r"d'abord considérer", "d'abord consi%" + NL + r"\oldpage[IV-4]{93}" + NL + "dérer",
    note="Marker move, part 1 of 2: inserts the marker at the printed word break (as $Z$-mor%|phisme, p. 58). Apply after all other p. 92 findings (the five before it, marked 'printed p. 93', lie in text that this edit moves into the p. 93 segment); the first p. 93 finding removes the old marker.")

# ---------------------------------------------------------------- page 93
p = 93
add(p, "old \\oldpage[IV-4]{93} before 'Ceci dit, l'application'",
    "'Ceci dit' is an indented paragraph in the middle of printed p. 93 (page_093_s1.png)", "the p. 93 marker stands here",
    'marker', r"\oldpage[IV-4]{93}¶¶Ceci dit", r"Ceci dit",
    note="Marker move, part 2 of 2: removes the old marker (apply after the last p. 92 finding, which inserts the new one). The blank line before it (end of the p. 92 segment) stays: 'Ceci dit' opens a new paragraph.")
add(p, "(17.13.5), end: 'donne le' before 'Corollaire (17.13.6)'",
    "the sentence ends 'donne le' and runs into the heading 'Corollaire (17.13.6). —' (page_093_s1.png, page_093_s2.png)",
    "'donne le corollaire suivant.'", 'extra', r"donne le corollaire suivant.", r"donne le")
add(p, "Corollaire (17.13.6): 'X, Y, Z trois S-préschémas f : Y→X, g : Z→X deux S-morphismes'",
    "no comma after 'S-préschémas' (crop p93_s2_cor.png)", "comma", 'punctuation',
    r"trois $S$-préschémas, $f:Y\to X$", r"trois $S$-préschémas $f:Y\to X$")
add(p, "Corollaire (17.13.6): '(resp. Z)', '(resp. z)', '(resp. m+b)'", "'(resp.' and ')' upright, three times (crop p93_s2_cor.png)",
    "italic", 'convention',
    r"$Y$ (resp. $Z$) lisse sur $S$ au point $y$ (resp. $z$), de dimension relative $m+a$ (resp. $m+b$)",
    r"$Y$ \textup{(resp. $Z$)} lisse sur $S$ au point $y$ \textup{(resp. $z$)}, de dimension relative $m+a$ \textup{(resp. $m+b$)}",
    conv=6, note="One edit for the three parentheses.")
add(p, "Corollaire (17.13.6), label a)", "'a)' upright", "italic label", 'convention',
    r"\item[a)] $T$ est lisse", r"\item[\textup{a)}] $T$ est lisse", conv=6, note=LBL6)
add(p, "Corollaire (17.13.6), label b)", "'b)' upright", "italic label", 'convention',
    r"\item[b)] L'homomorphisme", r"\item[\textup{b)}] L'homomorphisme", conv=6, note=LBL6)
add(p, "(17.13.6) b), display: 'Ω^1_{X/S}⊗_{O_X} k(t)'", "italic Omega", "upright \\Omega", 'font',
    r"\rho\otimes1:\Omega^1_{X/S}", r"\rho\otimes1:\varOmega^1_{X/S}", note=VO)
add(p, "(17.13.6) b), display: '(Ω^1_{Y/S}⊗_{O_Y} k(t))'", "italic Omega", "upright \\Omega", 'font',
    r"\to¶  (\Omega^1_{Y/S}", r"\to¶  (\varOmega^1_{Y/S}", note=VO)
add(p, "(17.13.6) b), display: '(Ω^1_{Z/S}⊗_{O_Z} k(t))'", "italic Omega", "upright \\Omega", 'font',
    r"\oplus¶  (\Omega^1_{Z/S}", r"\oplus¶  (\varOmega^1_{Z/S}", note=VO)
add(p, "(17.13.6) b), display: '⊗_{O_X} k(t)'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_X}k(t)", r"\otimes_{\sh{O}_X}\boldsymbol{k}(t)", conv=1)
add(p, "(17.13.6) b), display: '⊗_{O_Y} k(t)'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_Y}k(t)", r"\otimes_{\sh{O}_Y}\boldsymbol{k}(t)", conv=1)
add(p, "(17.13.6) b), display: '⊗_{O_Z} k(t)'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_Z}k(t)", r"\otimes_{\sh{O}_Z}\boldsymbol{k}(t)", conv=1)
add(p, "(17.13.6) b): 'où ρ est donné par (17.13.5.4), est injectif'", "reference upright", "italic", 'convention',
    r"par (17.13.5.4), est injectif", r"par \textup{(17.13.5.4)}, est injectif", conv=6, note=REF6)
add(p, "Corollaire (17.13.6), label c)", "'c)' upright", "italic label", 'convention',
    r"\item[c)] Le morphisme", r"\item[\textup{c)}] Le morphisme", conv=6, note=LBL6)
add(p, "(17.13.6) c): 'Le morphisme T=Y×_SZ→X×_SX est transversal à la diagonale de X×_SX au point t'",
    "'T=Y×_S Z→X×_S X' (crop p93_s2_c.png)", "the TeX keeps the printed reading", 'misprint_in_print',
    None, None, conf='medium', corrected=r"Le morphisme $Y\times_SZ\to X\times_SX$",
    note="T is Y×_X Z by the statement itself; the morphism transversal to the diagonal is u=f×_Sg: Y×_SZ→X×_SX of (17.13.5.1), at the point t of T=u^{-1}(diagonal) (Definition (17.13.3) with X'=Y×_SZ, Y'=T). 'T=' is wrong. Not in the errata (Liste 3).")
add(p, "Corollaire (17.13.6): 'Si t est rationnel ...' after the list", "new indented paragraph (page_093_s3.png)",
    "text follows \\end{enumerate} directly (no indent)", 'other',
    r"\end{enumerate}¶Si $t$ est rationnel", r"\end{enumerate}¶¶Si $t$ est rationnel", note=PAR)
add(p, "Corollaire (17.13.6), label b')", "'b')' upright", "italic label", 'convention',
    r"\item[b')] L'homomorphisme", r"\item[\textup{b$'$)}] L'homomorphisme", conv=6,
    note=LBL6 + " Prime written b$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(p, "(17.13.6) b'): '(cf. (16.5.12.5)) est surjectif'", "the whole parenthesis upright (crop p93_s3_cf.png)",
    "italic", 'convention', r"(cf. (16.5.12.5)) est surjectif", r"\textup{(cf. (16.5.12.5))} est surjectif", conv=6)
add(p, "Corollaire (17.13.6): 'De plus, lorsque ...' after the list", "new indented paragraph (page_093_s3.png)",
    "text follows \\end{enumerate} directly (no indent)", 'other',
    r"\end{enumerate}¶De plus, lorsque", r"\end{enumerate}¶¶De plus, lorsque", note=PAR)
add(p, "Corollaire (17.13.6): 'lorsque les conditions a) et b) sont vérifiées en t'", "labels upright", "italic",
    'convention', r"les conditions a) et b) sont vérifiées en $t$", r"les conditions \textup{a)} et \textup{b)} sont vérifiées en $t$",
    conv=6, note=LBL6)
add(p, "(17.13.6.2)", "all four Omegas italic", "upright \\Omega", 'font',
    r"0\to\Omega^1_{X/S}\otimes_{\sh{O}_X}\sh{O}_T\xrightarrow{\rho}¶(\Omega^1_{Y/S}\otimes_{\sh{O}_Y}\sh{O}_T)\oplus¶(\Omega^1_{Z/S}\otimes_{\sh{O}_Z}\sh{O}_T)¶\xrightarrow{\sigma}\Omega^1_{T/S}\to0",
    r"0\to\varOmega^1_{X/S}\otimes_{\sh{O}_X}\sh{O}_T\xrightarrow{\rho}¶(\varOmega^1_{Y/S}\otimes_{\sh{O}_Y}\sh{O}_T)\oplus¶(\varOmega^1_{Z/S}\otimes_{\sh{O}_Z}\sh{O}_T)¶\xrightarrow{\sigma}\varOmega^1_{T/S}\to0",
    note=VO)
add(p, "Corollaire (17.13.6): '(où σ est donné par (17.13.5.3)) est exacte'",
    "both parentheses and the reference upright, the words italic (crop p93_s3_ou.png)", "italic", 'convention',
    r"(où $\sigma$ est donné par (17.13.5.3))", r"\textup{(}où $\sigma$ est donné par \textup{(17.13.5.3))}", conv=6,
    note="Parentheses upright around italic words (GLOBAL_ISSUES 96).")
add(p, "end of Corollaire (17.13.6)",
    "the statement ends with '... est exacte.'; 'Le seul point qui reste à prouver ...' and 'Lorsque les conditions équivalentes de (17.13.6) ...' are roman (page_093_s3.png, page_093_s4.png)",
    "\\end{corollary} stands after 'la mention de $S$.': the two roman paragraphs are set italic", 'other',
    r"est exacte.¶¶Le seul point", "est exacte." + NL + r"\end{corollary}" + NL + NL + "Le seul point",
    note="Part 1 of 2 (apply both): ends the corollary after its statement; the second part removes the old \\end{corollary}.")
add(p, "proof paragraph: 'Le seul point ... concerne b')'", "b') italic", "upright (once the paragraph is roman)",
    'italics', r"concerne b'), et", r"concerne \emph{b')}, et", note=LBLR)
add(p, "proof paragraph: 't est rationnel sur k(s)'", "bold italic k", "plain k", 'convention',
    r"que $t$ est rationnel sur $k(s)$", r"que $t$ est rationnel sur $\boldsymbol{k}(s)$", conv=1)
add(p, "'forment un couple de morphismes transversaux au point t, relativement à S'",
    "'relativement à' italic, 'à' included (crop p93_s4_lines.png)", "'à' outside the \\emph", 'italics',
    r"relativement} à $S$;", r"relativement à} $S$;")
add(p, "end of Corollaire (17.13.6): old \\end{corollary}", "see part 1", "\\end{corollary} after 'la mention de $S$.'",
    'other', "la mention de $S$." + NL + r"\end{corollary}", r"la mention de $S$.",
    note="Part 2 of 2 (apply both): removes the old \\end{corollary}.")
add(p, "(17.13.7): 'Y et Z sont des sous-préschémas de X'", "'sous-préschémas de' italic, 'de' included (crop p93_s4_lines.png)",
    "'de' outside the \\emph", 'italics', r"\emph{sous-préschémas} de $X$", r"\emph{sous-préschémas de} $X$")
add(p, "page break 93/94 inside 'le sous-préschéma « intersection » | inf(Y, Z) de X'",
    "p. 93 ends '« intersection »', p. 94 begins 'inf(Y, Z) de X (I, 4.4.3)' (page_093_s4.png, page_094_s1.png)",
    "blank line before \\oldpage[IV-4]{94} (and another after it): a paragraph break inside the sentence", 'marker',
    r"« intersection »¶¶", r"« intersection »¶",
    note="The marker is at the right place. Part 1 of 2: the first p. 94 finding removes the blank line after \\oldpage[IV-4]{94}; apply both.")

# ---------------------------------------------------------------- page 94
p = 94
add(p, "top of page_094.tex: blank line after \\oldpage[IV-4]{94}", "p. 94 begins mid-sentence ('inf(Y, Z) de X')",
    "blank line between the marker and '$\\inf(Y,Z)$'", 'marker',
    r"\oldpage[IV-4]{94}¶¶$\inf", r"\oldpage[IV-4]{94}¶$\inf",
    note="Part 2 of 2 with the last p. 93 finding; both blank lines must go.")
add(p, "(17.13.7): 'inf(Y, Z) de X (I, 4.4.3)'", "bold I", "plain I", 'convention',
    r"(I, 4.4.3)", r"(\textbf{I}, 4.4.3)", conv=2)
add(p, "(17.13.7): 'on dit alors que Y et Z se coupent transversalement au point x'",
    "'et' italic as well (crop p94_s1_top.png)", "'et' upright", 'italics',
    r"$Y$ et $Z$ \emph{se coupent", r"$Y$ \emph{et} $Z$ \emph{se coupent")
add(p, "(17.13.7): 'tenant compte de (5.2.3), (5.1.9) et (0, 16.5.12)'", "bold 0", "plain 0", 'convention',
    r"(0, 16.5.12)", r"(\textbf{0}, 16.5.12)", conv=2)
add(p, "(17.13.7): 'il faut et il suffit que T soit lisse sur S au point x'", "'lisse' italic (crop p94_s1_top.png)",
    "upright", 'italics', r"$T$ soit lisse sur", r"$T$ soit \emph{lisse} sur")
add(p, "Proposition (17.13.8), label a)", "'a)' upright", "italic label", 'convention',
    r"\item[a)] L'injection", r"\item[\textup{a)}] L'injection", conv=6, note=LBL6)
add(p, "Proposition (17.13.8) a): 'relativement à S (17.13.3).'", "reference upright", "italic", 'convention',
    r"relativement à $S$ (17.13.3).", r"relativement à $S$ \textup{(17.13.3)}.", conv=6, note=REF6)
add(p, "Proposition (17.13.8), label a')", "'a')' upright", "italic label", 'convention',
    r"\item[a')] L'injection", r"\item[\textup{a$'$)}] L'injection", conv=6,
    note=LBL6 + " Prime written a$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(p, "Proposition (17.13.8), label a'')", "'a'')' upright", "italic label", 'convention',
    r"\item[a'')] $Y$ et $Z$", r"\item[\textup{a$''$)}] $Y$ et $Z$", conv=6,
    note=LBL6 + " Primes written a$''$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(p, "Proposition (17.13.8), label b)", "'b' upright (the parenthesis: next finding)", "italic label", 'convention',
    r"\item[b)] $X$, $Y$, $Z$", r"\item[\textup{b)}] $X$, $Y$, $Z$", conv=6,
    note=LBL6 + " Apply before the misprint finding that follows (same label).")
add(p, "Proposition (17.13.8), label b): its closing parenthesis",
    "upright b with an ITALIC closing parenthesis, unlike the upright parentheses of a), a'), a''), b') (crops p94_s2_b.png, p94_labels_side.png)",
    "regular label (silent correction)", 'misprint_in_print',
    r"\item[\textup{b)}] $X$", r"\item[\textup{b})] $X$", corrected=r"\item[\textup{b)}] $X$",
    note="Wrong-fount parenthesis (GLOBAL_ISSUES 29). 'old' is the text after the convention-6 edit just before (apply that first); the edit moves only the parenthesis out of \\textup, where the statement's italic sets it.",
    after_prev=True)
add(p, "Proposition (17.13.8) b): 'l'homomorphisme ρ (17.13.5.4) est tel que'", "reference upright", "italic",
    'convention', r"$\rho$ (17.13.5.4) est tel que", r"$\rho$ \textup{(17.13.5.4)} est tel que", conv=6, note=REF6)
add(p, "(17.13.8) b), display: 'Ω^1_{X/S}⊗_{O_X} k(x)'", "italic Omega", "upright \\Omega", 'font',
    r"\rho\otimes1:\Omega^1_{X/S}", r"\rho\otimes1:\varOmega^1_{X/S}", note=VO)
add(p, "(17.13.8) b), display: '(Ω^1_{Y/S}⊗_{O_Y} k(x))'", "italic Omega", "upright \\Omega", 'font',
    r"\to¶  (\Omega^1_{Y/S}", r"\to¶  (\varOmega^1_{Y/S}", note=VO)
add(p, "(17.13.8) b), display: '(Ω^1_{Z/S}⊗_{O_Z} k(x))'", "italic Omega", "upright \\Omega", 'font',
    r"\oplus¶  (\Omega^1_{Z/S}", r"\oplus¶  (\varOmega^1_{Z/S}", note=VO)
add(p, "(17.13.8) b), display: '⊗_{O_X} k(x)'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_X}k(x)", r"\otimes_{\sh{O}_X}\boldsymbol{k}(x)", conv=1)
add(p, "(17.13.8) b), display: '⊗_{O_Y} k(x)'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_Y}k(x)", r"\otimes_{\sh{O}_Y}\boldsymbol{k}(x)", conv=1)
add(p, "(17.13.8) b), display: '⊗_{O_Z} k(x)'", "bold italic k", "plain k", 'convention',
    r"\otimes_{\sh{O}_Z}k(x)", r"\otimes_{\sh{O}_Z}\boldsymbol{k}(x)", conv=1)
add(p, "Proposition (17.13.8): 'Lorsque x est rationnel ...' after the list", "new indented paragraph (page_094_s2.png)",
    "text follows \\end{enumerate} directly (no indent)", 'other',
    r"\end{enumerate}¶Lorsque $x$", r"\end{enumerate}¶¶Lorsque $x$", note=PAR)
add(p, "Proposition (17.13.8): 'Lorsque x est rationnel sur k(s)'", "bold italic k", "plain k", 'convention',
    r"Lorsque $x$ est rationnel sur $k(s)$", r"Lorsque $x$ est rationnel sur $\boldsymbol{k}(s)$", conv=1)
add(p, "Proposition (17.13.8): '(s image de x dans S)'", "both parentheses upright, the words italic (crop p94_s2_lorsque.png)",
    "italic", 'convention', r"($s$ image de $x$ dans $S$)", r"\textup{(}$s$ image de $x$ dans $S$\textup{)}", conv=6,
    note="Parentheses upright around italic words (GLOBAL_ISSUES 96).")
add(p, "Proposition (17.13.8), label b')", "'b')' upright", "italic label", 'convention',
    r"\item[b')] L'homomorphisme", r"\item[\textup{b$'$)}] L'homomorphisme", conv=6,
    note=LBL6 + " Prime written b$'$ as in the edition's fixed labels (GLOBAL_ISSUES 88).")
add(p, "Proposition (17.13.8): 'En outre, lorsque ...' after the list", "new indented paragraph (page_094_s3.png)",
    "text follows \\end{enumerate} directly (no indent)", 'other',
    r"\end{enumerate}¶En outre,", r"\end{enumerate}¶¶En outre,", note=PAR)
add(p, "Proposition (17.13.8): 'les conditions équivalentes a) à b) sont vérifiées'", "labels upright", "italic",
    'convention', r"équivalentes a) à b) sont", r"équivalentes \textup{a)} à \textup{b)} sont", conv=6, note=LBL6)
add(p, "Proposition (17.13.8): 'la suite (17.13.6.2) est exacte'", "reference upright", "italic", 'convention',
    r"la suite (17.13.6.2) est exacte", r"la suite \textup{(17.13.6.2)} est exacte", conv=6, note=REF6)
add(p, "proof of (17.13.8): 'Les conditions a), a'), a'') impliquent'", "labels italic (page_094_s3.png)", "upright",
    'italics', r"Les conditions a), a'), a'') impliquent", r"Les conditions \emph{a)}, \emph{a')}, \emph{a'')} impliquent",
    note=LBLR)
add(p, "proof of (17.13.8): 'que les conditions a), a') équivalent toutes deux'", "labels italic", "upright", 'italics',
    r"que les conditions a), a') équivalent", r"que les conditions \emph{a)}, \emph{a')} équivalent", note=LBLR)
add(p, "proof of (17.13.8): 'la condition a'') est vérifiée, d'où l'équivalence de a), a') et a'')'",
    "labels italic (page_094_s4.png)", "upright", 'italics',
    r"la condition a'') est vérifiée, d'où l'équivalence de a), a') et a'').",
    r"la condition \emph{a'')} est vérifiée, d'où l'équivalence de \emph{a)}, \emph{a')} et \emph{a'')}.", note=LBLR)
add(p, "proof of (17.13.8): 'L'équivalence de a'') et de b) (ou b') lorsque'", "labels italic, '(ou' upright",
    "upright", 'italics', r"L'équivalence de a'') et de b) (ou b') lorsque",
    r"L'équivalence de \emph{a'')} et de \emph{b)} (ou \emph{b')} lorsque", note=LBLR)
add(p, "proof of (17.13.8): 'lorsque x est rationnel sur k(s))'", "bold italic k", "plain k", 'convention',
    r"rationnel sur $k(s)$) a été", r"rationnel sur $\boldsymbol{k}(s)$) a été", conv=1)

# ---------------------------------------------------------------- checks
pages = {}
for n in range(90, 95):
    t = (RUN / f'page_{n:03d}.tex').read_text(encoding='utf-8').replace('\r\n', '\n')
    pages[n] = t
orig = dict(pages)
ok = True
for i, f in enumerate(F):
    fx = f['fix']
    if not fx:
        continue
    n = f['page']
    c_now = pages[n].count(fx['old'])
    c_orig = orig[n].count(fx['old'])
    if c_now != 1 or (c_orig != 1 and not f['_after_prev']):
        ok = False
        print('PAGE-CHECK FAIL', i, n, c_orig, c_now, repr(fx['old'])[:120])
    if f['_after_prev'] and c_orig != 0:
        print('note: after_prev old also in original', i, n, c_orig)
    pages[n] = pages[n].replace(fx['old'], fx['new'])
print('page-file check', 'OK' if ok else 'FAILED')

# simulate apply_fixes.py on the current source (in memory)
src = SRC.read_text(encoding='utf-8')
marker = re.compile(r'\\oldpage\[IV-4\]\{(\d+)\}')


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


ok2 = True
t = src
for i, f in enumerate(F):
    fx = f['fix']
    if not fx:
        continue
    s, e = locate(t, f['page'])
    seg = t[s:e]
    if seg.count(fx['old']) != 1:
        ok2 = False
        print('SIM FAIL', i, f['page'], seg.count(fx['old']), repr(fx['old'])[:120])
        continue
    t = t[:s] + seg.replace(fx['old'], fx['new']) + t[e:]
print('simulation', 'OK' if ok2 else 'FAILED')
a = t.index(r'\oldpage[IV-4]{90}')
b = t.index(r'\oldpage[IV-4]{95}')
(RUN / 'crops_090_094' / 'segment_after_fixes.txt').write_text(t[a:b], encoding='utf-8')

out = []
for f in F:
    g = {k: v for k, v in f.items() if k != '_after_prev'}
    out.append(g)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
from collections import Counter
cnt = Counter()
for f in out:
    k = 'misprint' if f['kind'] == 'misprint_in_print' else ('convention' if f['kind'] == 'convention' else 'normal')
    cnt[(f['page'], k)] += 1
for n in range(90, 95):
    print(n, cnt[(n, 'normal')], cnt[(n, 'convention')], cnt[(n, 'misprint')])
print('total', len(out))
