"""Build findings_107_111.json for EGA III part 1, pp. 107-111 (scan check)."""
import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_III1")
OUT = RUN / "findings_107_111.json"

F = []


def add(page, where, scan, tex, kind, old, new, conf="high", conv=None, note="", corrected=None, nofix=False):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=conv, confidence=conf,
             fix=None if nofix else {"old": old, "new": new})
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


C2 = "Bold chapter number in the reference."
DISP = "The print sets this formula inline in the running text; the TeX displays it."
LBL = ("Item label printed upright; \\item[...] comes out italic inside the italic statement environment "
       "(GLOBAL_ISSUES 16).")

# ---------------- p. 107 ----------------
add(107, "Proof of (2.3.7): 'f est projectif (II, 5.5.5, (v))'", "(II, 5.5.5, (v)) with bold II", "(II, 5.5.5, (v))",
    "convention", r"(II, 5.5.5, (v))", r"(\textbf{II}, 5.5.5, (v))", conv=2, note=C2)
add(107, "Remarque (2.3.8), end: 'contenu dans Y—U'", "Y—U (long dash)", "$Y-U$",
    "convention", r"$Y-U$", r"$Y\setmin U$", conv=7, note="Set difference printed with the long dash.")
add(107, "Théorème (2.4.1), label (i)", "(i) upright", r"\item[(i)] (italic in the theorem environment)",
    "convention", r"\item[(i)] Pour tout", r"\item[\textup{(i)}] Pour tout", conv=6, note=LBL)
add(107, "Théorème (2.4.1), label (ii)", "(ii) upright", r"\item[(ii)] (italic in the theorem environment)",
    "convention", r"\item[(ii)] Soit de plus", r"\item[\textup{(ii)}] Soit de plus", conv=6,
    note=LBL + " The small mark after '(ii)' in the scan is a speck, not a full stop.")
add(107, "Théorème (2.4.1)(ii): 'l'homomorphisme canonique f*(f_*(M(n))→M(n) (0_I, 4.4.3) soit surjectif'",
    "formula inline in the text line", "displayed with \\[ \\]",
    "other",
    "canonique\n\\[\nf^*(f_*(\\mathcal M(n)))\\longrightarrow\\mathcal M(n)\n\\]",
    "canonique\n$f^*(f_*(\\mathcal M(n)))\\longrightarrow\\mathcal M(n)$",
    note=DISP + " Apply before the next finding (the misprint in the same formula).")
add(107, "Théorème (2.4.1)(ii): 'f*(f_*(M(n))→M(n)'",
    "f*(f_*(M(n))→M(n): only two closing parentheses before the arrow (enlarged crop)",
    r"f^*(f_*(\mathcal M(n)))", "misprint_in_print",
    r"f^*(f_*(\mathcal M(n)))", r"f^*(f_*(\mathcal M(n))",
    corrected=r"f^*(f_*(\mathcal M(n)))",
    note="The print omits the closing parenthesis of f*(...). The TeX silently corrects it; the fix restores the "
         "printed reading (old string still unique after the display-to-inline fix above).")
add(107, "Théorème (2.4.1)(ii): '(0_I, 4.4.3) soit surjectif'",
    "(0_I, 4.4.3) with bold 0, the whole reference upright inside the italic statement",
    r"(0\textsubscript{I}, 4.4.3) in the italic theorem environment", "convention",
    r"(0\textsubscript{I}, 4.4.3)", r"\textup{(\textbf{0}\textsubscript{I}, 4.4.3)}", conv=2,
    note="Bold 0 (convention 2); the fix also sets the reference upright (convention 6: roman inside the italic "
         "statement).")
add(107, "Proof of (2.4.1): 'X'=X×_Y Y' (II, 1.5.5)'", "(II, 1.5.5) with bold II", "(II, 1.5.5)",
    "convention", r"(II, 1.5.5)", r"(\textbf{II}, 1.5.5)", conv=2, note=C2)
add(107, "Proof of (2.4.1): 'f' est projectif (II, 5.5.5, (iii))'", "(II, 5.5.5, (iii)) with bold II",
    "(II, 5.5.5, (iii))", "convention", r"(II, 5.5.5, (iii))", r"(\textbf{II}, 5.5.5, (iii))", conv=2, note=C2)
add(107, "Proof (i): 'X-schéma affine (II, 1.4.3)'", "(II, 1.4.3) with bold II", "(II, 1.4.3)",
    "convention", r"(II, 1.4.3)", r"(\textbf{II}, 1.4.3)", conv=2, note=C2)
add(107, "Proof (i): 'Module de type fini (II, 1.4.5)'", "(II, 1.4.5) with bold II", "(II, 1.4.5)",
    "convention", r"(II, 1.4.5)", r"(\textbf{II}, 1.4.5)", conv=2, note=C2)
add(107, "Proof (i): '(II, 1.3.7 et I, 6.3.4, (ii))', first number", "bold II", "(II, 1.3.7",
    "convention", r"(II, 1.3.7", r"(\textbf{II}, 1.3.7", conv=2, note=C2)
add(107, "Proof (i): '(II, 1.3.7 et I, 6.3.4, (ii))', second number", "bold I", "et I, 6.3.4",
    "convention", r"et I, 6.3.4", r"et \textbf{I}, 6.3.4", conv=2, note=C2)
add(107, "Proof (i): 'X' est noethérien (I, 6.3.7)'", "(I, 6.3.7) with bold I", "(I, 6.3.7)",
    "convention", r"(I, 6.3.7)", r"(\textbf{I}, 6.3.7)", conv=2, note=C2)
add(107, "Proof (i): 'un homomorphisme de S-Modules; en effet'", "'Modules' in italics (enlarged crop)",
    "$\\mathcal S$-Modules (upright)", "italics",
    r"de $\mathcal S$-Modules~;", r"de $\mathcal S$-\emph{Modules}~;")
add(107, "Last display of the page: 'f_*(g'_*(O_X')) ⊗ R^pf_*(g'_*(M~)) → R^pf_*(g'_*(M~))'",
    "no full stop after the display; the sentence continues on p. 108 with '(0, 12.2.2), et comme'",
    "display ends with '.'", "punctuation",
    "R^pf_*(g'_*(\\widetilde{\\mathcal M})).\n\\]", "R^pf_*(g'_*(\\widetilde{\\mathcal M}))\n\\]",
    note="Enlarged crop: no full stop.")

# ---------------- p. 108 ----------------
add(108, "First line: '(0, 12.2.2), et comme'", "(0, 12.2.2) with bold 0", "(0, 12.2.2)",
    "convention", r"(0, 12.2.2)", r"(\textbf{0}, 12.2.2)", conv=2, note=C2)
add(108, "First line: '(par application de (0_I, 4.2.2.1))'", "bold 0", r"(0\textsubscript{I}, 4.2.2.1)",
    "convention", r"(0\textsubscript{I}, 4.2.2.1)", r"(\textbf{0}\textsubscript{I}, 4.2.2.1)", conv=2, note=C2)
add(108, "'de l'homomorphisme O_X'⊗M~→M~ définissant la structure'", "formula inline", "displayed",
    "other",
    "l'homomorphisme\n\\[\n\\mathcal O_{X'}\\otimes\\widetilde{\\mathcal M}\n\\longrightarrow\\widetilde{\\mathcal M}\n\\]",
    "l'homomorphisme\n$\\mathcal O_{X'}\\otimes\\widetilde{\\mathcal M}\n\\longrightarrow\\widetilde{\\mathcal M}$",
    note=DISP)
add(108, "'est commutatif (0, 12.2.6);'", "(0, 12.2.6) with bold 0", "(0, 12.2.6)",
    "convention", r"(0, 12.2.6)", r"(\textbf{0}, 12.2.6)", conv=2, note=C2)
add(108, "'l'homomorphisme canonique S→f_*(f*(S))=f_*(S')=f_*(g'_*(O_X'))=h_*(O_X'), on obtient'",
    "formula inline", "displayed", "other",
    "canonique\n\\[\n\\mathcal S\\longrightarrow f_*(f^*(\\mathcal S))=f_*(\\mathcal S')\n"
    "=f_*(g'_*(\\mathcal O_{X'}))=h_*(\\mathcal O_{X'}),\n\\]",
    "canonique\n$\\mathcal S\\longrightarrow f_*(f^*(\\mathcal S))=f_*(\\mathcal S')\n"
    "=f_*(g'_*(\\mathcal O_{X'}))=h_*(\\mathcal O_{X'})$,",
    note=DISP)
add(108, "'c'est un isomorphisme de S-Modules (en utilisant'", "'Modules' in italics (enlarged crop)",
    "upright", "italics", r"$\mathcal S$-Modules (en utilisant", r"$\mathcal S$-\emph{Modules} (en utilisant")
add(108, "'la commutativité de (0, 12.2.6.2)'", "(0, 12.2.6.2) with bold 0", "(0, 12.2.6.2)",
    "convention", r"(0, 12.2.6.2)", r"(\textbf{0}, 12.2.6.2)", conv=2, note=C2)
add(108, "'est un S-Module de type fini (II, 1.4.5)'", "'de type fini' in italics (enlarged crop)", "upright",
    "italics", "Module de type\nfini", "Module \\emph{de type\nfini}")
add(108, "'S-Module de type fini (II, 1.4.5).'", "(II, 1.4.5) with bold II", "(II, 1.4.5)",
    "convention", r"(II, 1.4.5)", r"(\textbf{II}, 1.4.5)", conv=2, note=C2)
add(108, "(ii): 'on a g'_*(M~⊗L'^{⊗n})=g'_*(M~)⊗L^{⊗n}=M(n) (0_I, 5.4.10)'", "formula inline", "displayed",
    "other",
    "\\[\ng'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n})\n"
    "=g'_*(\\widetilde{\\mathcal M})\\otimes\\mathcal L^{\\otimes n}\n=\\mathcal M(n)\n\\]",
    "$g'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n})\n"
    "=g'_*(\\widetilde{\\mathcal M})\\otimes\\mathcal L^{\\otimes n}\n=\\mathcal M(n)$",
    note=DISP)
add(108, "(ii): '(0_I, 5.4.10) à un isomorphisme près'", "bold 0", r"(0\textsubscript{I}, 5.4.10)",
    "convention", r"(0\textsubscript{I}, 5.4.10)", r"(\textbf{0}\textsubscript{I}, 5.4.10)", conv=2, note=C2)
add(108, "(ii): 'qui prouve que R^pf_*(g'_*(...)) est isomorphe à g_*(R^pf'_*(...)).'",
    "formulas inline, 'est isomorphe à' in the text", "one display with \\hbox{est isomorphe à}", "other",
    "\\[\nR^pf_*(g'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}))\n"
    "\\quad\\hbox{est isomorphe à}\\quad\n"
    "g_*(R^pf'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n})).\n\\]",
    "$R^pf_*(g'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}))$\nest isomorphe à\n"
    "$g_*(R^pf'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}))$.",
    note=DISP)
add(108, "(ii): 'ample pour f' (II, 4.6.13, (iii))'", "bold II", "(II, 4.6.13, (iii))",
    "convention", r"(II, 4.6.13, (iii))", r"(\textbf{II}, 4.6.13, (iii))", conv=2, note=C2)
add(108, "(ii): 'un entier N tel que R^pf'_*(M~⊗L'^{⊗n})=0 pour tout p'", "formula inline", "displayed",
    "other",
    "\\[\nR^pf'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n})=0\n\\]",
    "$R^pf'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n})=0$",
    note=DISP)
add(108, "(ii): 'l'homomorphisme canonique f'*(f'_*(M~⊗L'^{⊗n}))→M~⊗L'^{⊗n} soit surjectif'",
    "formula inline", "displayed", "other",
    "\\[\nf'^*(f'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}))\n"
    "\\longrightarrow\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}\n\\]",
    "$f'^*(f'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}))\n"
    "\\longrightarrow\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n}$",
    note=DISP)
add(108, "(ii): 'un foncteur exact (II, 1.4.4)'", "bold II", "(II, 1.4.4)",
    "convention", r"(II, 1.4.4)", r"(\textbf{II}, 1.4.4)", conv=2, note=C2)
add(108, "(ii): 'Or, on a g'_*(f'*(f'_*(...)))=f*(g_*(f'_*(...)) (II, 1.5.2)'", "formula inline", "displayed",
    "other",
    "\\[\ng'_*(f'^*(f'_*(\\widetilde{\\mathcal M}\\otimes\n\\mathcal L'^{\\otimes n})))\n"
    "=f^*(g_*(f'_*(\\widetilde{\\mathcal M}\\otimes\n\\mathcal L'^{\\otimes n})))\n\\]",
    "$g'_*(f'^*(f'_*(\\widetilde{\\mathcal M}\\otimes\n\\mathcal L'^{\\otimes n})))\n"
    "=f^*(g_*(f'_*(\\widetilde{\\mathcal M}\\otimes\n\\mathcal L'^{\\otimes n})))$",
    note=DISP + " Apply before the next finding (the misprint in the same formula).")
add(108, "(ii): right-hand side 'f*(g_*(f'_*(M~⊗L'^{⊗n}))'",
    "f*(g_*(f'_*(M~⊗L'^{⊗n})): three opening, two closing parentheses (enlarged crop)",
    "=f^*(g_*(f'_*(...)))", "misprint_in_print",
    "=f^*(g_*(f'_*(\\widetilde{\\mathcal M}\\otimes\n\\mathcal L'^{\\otimes n})))",
    "=f^*(g_*(f'_*(\\widetilde{\\mathcal M}\\otimes\n\\mathcal L'^{\\otimes n}))",
    corrected="=f^*(g_*(f'_*(\\widetilde{\\mathcal M}\\otimes\\mathcal L'^{\\otimes n})))",
    note="The print omits one closing parenthesis. The TeX silently corrects it; the fix restores the printed "
         "reading (old string still unique after the display-to-inline fix above).")
add(108, "(ii): '...)) (II, 1.5.2) et comme'", "bold II", "(II, 1.5.2)",
    "convention", r"(II, 1.5.2)", r"(\textbf{II}, 1.5.2)", conv=2, note=C2)
add(108, "(ii): 'on voit finalement que l'on a' (before the last display)",
    "the final 'a' is a bold roman a (wrong font)", "plain a", "misprint_in_print",
    "finalement que l'on a", "finalement que l'on \\textbf{a}", conf="medium",
    corrected="finalement que l'on a",
    note="Enlarged crop and ink measurement: this 'a' carries about 30-50% more ink than the other a's of the "
         "page (bold face). Wrong-font letter (GLOBAL_ISSUES 29: reproduced in the diplomatic text).")
add(108, "(2.4.2): 'une O_Y-Algèbre graduée à degrés positifs'", "'graduée' in italics", "upright",
    "italics", "Algèbre graduée à degrés", "Algèbre \\emph{graduée} à degrés")
add(108, "(2.4.2): 'M=⊕_{k∈Z} M_k'",
    "both k (the index under ⊕ and the subscript of M_k) in bold italic (wrong font)", "plain k",
    "misprint_in_print",
    r"\bigoplus_{k\in\mathbb Z}\mathcal M_k$", r"\bigoplus_{\boldsymbol{k}\in\mathbb Z}\mathcal M_{\boldsymbol{k}}$",
    conf="medium", corrected=r"\bigoplus_{k\in\mathbb Z}\mathcal M_k$",
    note="Enlarged crop and ink measurement: both k are bold italic (about 70% more ink than the plain k of the "
         "same formula on p. 109). Wrong-font letters (GLOBAL_ISSUES 29).")
add(108, "(2.4.2): 'un S'-Module gradué. Alors'", "'gradué' in italics", "upright",
    "italics", "Module gradué. Alors", "Module \\emph{gradué}. Alors")

# ---------------- p. 109 ----------------
add(109, "(2.4.2): 'on conclut de (2.4.1) que ⊕_{k∈Z} R^pf_*(M_k) est un'", "formula inline", "displayed",
    "other",
    "\\[\n\\bigoplus_{k\\in\\mathbb Z}R^pf_*(\\mathcal M_k)\n\\]",
    "$\\bigoplus_{k\\in\\mathbb Z}R^pf_*(\\mathcal M_k)$",
    note=DISP)
add(109, "(2.4.2): 'un S-Module de type fini pour tout p'", "'de type fini' in italics", "upright",
    "italics", "de type fini pour tout $p$", "\\emph{de type fini} pour tout $p$")
add(109, "(2.4.2): '(sous les hypothèses supplémentaires de (2.4.1, (ii)) qu'il existe'",
    "(2.4.1, (ii)) — one reference; the parenthesis opened by '(sous les' is never closed",
    "(2.4.1), (ii))", "misprint_in_print",
    r"(\hyperref[III.2.4.1-fr]{2.4.1}), (ii))", r"(\hyperref[III.2.4.1-fr]{2.4.1}, (ii))",
    corrected=r"(\hyperref[III.2.4.1-fr]{2.4.1}, (ii)))",
    note="Enlarged crop. The print lacks one closing parenthesis; the TeX silently rebalanced it as "
         "'(2.4.1), (ii))'. The fix restores the printed reading.")
add(109, "(2.4.2): 'pour tout p>0 et tout k∈Z, et'", "'tout' in italics", "upright",
    "italics", "et tout $k\\in\\mathbb Z$, et", "et \\emph{tout} $k\\in\\mathbb Z$, et")
add(109, "(2.4.2): 'f*(f_*(M_k(n)))→M_k(n)', the k of the second M_k(n)",
    "k after the arrow in bold italic (the k of the first M_k(n) is plain)", "plain k", "misprint_in_print",
    r"\to\mathcal M_k(n)$", r"\to\mathcal M_{\boldsymbol{k}}(n)$", conf="medium",
    corrected=r"\to\mathcal M_k(n)$",
    note="Enlarged side-by-side crop: this k matches the bold italic k of p. 108 (about 30% more ink than the "
         "first k). Wrong-font letter (GLOBAL_ISSUES 29).")
add(109, "(2.4.2): 'soit surjectif pour tout k∈Z.'", "'tout' in italics", "upright",
    "italics", "surjectif pour tout\n$k\\in\\mathbb Z$.", "surjectif pour \\emph{tout}\n$k\\in\\mathbb Z$.")
add(109, "(2.5.1): 'Soient A un anneau artinien'", "'artinien' in italics", "upright",
    "italics", "un anneau artinien, $X$", "un anneau \\emph{artinien}, $X$")
add(109, "(2.5.1): 'X un A-schéma projectif sur Y=Spec(A)'", "'projectif' in italics", "upright",
    "italics", "$A$-schéma projectif sur", "$A$-schéma \\emph{projectif} sur")
add(109, "(2.5.1): 'donc ici de longueur finie'", "'de longueur finie' in italics", "upright",
    "italics", "donc ici de longueur finie", "donc ici \\emph{de longueur finie}")
add(109, "(2.5.1): 'Lorsque A est un anneau local artinien'", "'anneau local artinien' in italics", "upright",
    "italics", "un anneau local artinien, on dit", "un \\emph{anneau local artinien}, on dit")
add(109, "(2.5.1): 'la caractéristique d'Euler-Poincaré de F (par rapport à l'anneau A)'",
    "'caractéristique d'Euler-Poincaré de' and '(par rapport à l'anneau' in italics (italic opening "
    "parenthesis); 'A)' upright", "upright", "italics",
    "la caractéristique d'Euler-Poincaré de $\\mathcal F$ (par rapport à\nl'anneau $A$)",
    "la \\emph{caractéristique d'Euler-Poincaré de} $\\mathcal F$ \\emph{(par rapport à\nl'anneau} $A$)",
    note="Enlarged crop: the opening parenthesis is italic, the closing one upright.")
add(109, "(2.5.1): 'le genre arithmétique de X'", "'genre arithmétique de' in italics", "upright",
    "italics", "le genre arithmétique de $X$", "le \\emph{genre arithmétique de} $X$")
add(109, "Proposition (2.5.2): 'Soit 0→F'→F→F''→0 une suite exacte'", "formula inline", "displayed",
    "other",
    "\\[\n0\\longrightarrow\\mathcal F'\\longrightarrow\\mathcal F\n\\longrightarrow\\mathcal F''\\longrightarrow0\n\\]",
    "$0\\longrightarrow\\mathcal F'\\longrightarrow\\mathcal F\n\\longrightarrow\\mathcal F''\\longrightarrow0$",
    note=DISP)
add(109, "Proof of (2.5.2), first line of the exact sequence: '→H^1(X, F')→ . . .'", "baseline dots", "\\cdots",
    "symbol", "H^1(X,\\mathcal F')\\to\\cdots", "H^1(X,\\mathcal F')\\to\\ldots",
    note="Baseline dots in the print (GLOBAL_ISSUES 22).")
add(109, "Proof of (2.5.2), second line: '. . . →H^r(X, F')'", "baseline dots", "\\cdots",
    "symbol", "\\cdots\\to H^r(X,\\mathcal F')", "\\ldots\\to H^r(X,\\mathcal F')",
    note="Baseline dots in the print (GLOBAL_ISSUES 22).")
add(109, "Proof of (2.5.2): 'est nulle (0, 11.10.1)'", "(0, 11.10.1) with bold 0", "(0, 11.10.1)",
    "convention", r"(0, 11.10.1)", r"(\textbf{0}, 11.10.1)", conv=2, note=C2)
add(109, "After (2.5.2): 'les A-modules H^i(X, F) sont de type fini pour tout'", "'de type fini' in italics",
    "upright", "italics", "sont de type fini pour tout", "sont \\emph{de type fini} pour tout")
add(109, "Théorème (2.5.3), label (i)", "(i) upright", r"\item[(i)] (italic in the theorem environment)",
    "convention", r"\item[(i)] Il existe", r"\item[\textup{(i)}] Il existe", conv=6, note=LBL)
add(109, "Théorème (2.5.3)(i): '(on dit que P est le polynôme de Hilbert de F par rapport à A)'",
    "the parenthetical sentence roman, with 'polynôme de Hilbert' in italics",
    "all italic (theorem environment), no emphasis", "convention",
    "(on dit que $P$\nest le polynôme de Hilbert de $\\mathcal F$ par rapport à $A$)",
    "\\textup{(on dit que $P$\nest le \\emph{polynôme de Hilbert} de $\\mathcal F$ par rapport à $A$)}",
    conv=6, note="Enlarged crop: roman words inside the italic statement; the defined term is italic.")
add(109, "Théorème (2.5.3), label (ii)", "(ii) upright", r"\item[(ii)] (italic in the theorem environment)",
    "convention", r"\item[(ii)] Pour $n$", r"\item[\textup{(ii)}] Pour $n$", conv=6, note=LBL)
add(109, "Théorème (2.5.3), label (iii)", "(iii) upright", r"\item[(iii)] (italic in the theorem environment)",
    "convention", r"\item[(iii)] Le terme", r"\item[\textup{(iii)}] Le terme", conv=6, note=LBL)
add(109, "After (2.5.3): 'nous démontrerons en outre que le degré de χ_A(F(n)) est égal à la dimension du "
         "support de F'", "'le degré de ... est égal à la dimension du support de' in italics", "upright",
    "italics",
    "que le degré de\n$\\chi_A(\\mathcal F(n))$ est égal à la dimension du support de",
    "que \\emph{le degré de\n$\\chi_A(\\mathcal F(n))$ est égal à la dimension du support de}")

# ---------------- p. 110 ----------------
add(110, "First line: 'on a χ_A(F(n))=long H^0(X, F(n))=long Γ(X, F(n)) pour n assez grand'",
    "formula inline", "displayed", "other",
    "\\[\n\\chi_A(\\mathcal F(n))=\\operatorname{long}H^0(X,\\mathcal F(n))\n"
    "=\\operatorname{long}\\Gamma(X,\\mathcal F(n))\n\\]",
    "$\\chi_A(\\mathcal F(n))=\\operatorname{long}H^0(X,\\mathcal F(n))\n"
    "=\\operatorname{long}\\Gamma(X,\\mathcal F(n))$",
    note=DISP)
add(110, "Filtration 'F(n)⊃mF(n)⊃ . . . ⊃m^{s-1}F(n)⊃0'", "baseline dots", "\\cdots",
    "symbol", "\\supset\\cdots", "\\supset\\ldots", note="Baseline dots in the print (GLOBAL_ISSUES 22).")
add(110, "'très ample relativement à Spec(K) (II, 4.4.10)'", "bold II", "(II, 4.4.10)",
    "convention", r"(II, 4.4.10)", r"(\textbf{II}, 4.4.10)", conv=2, note=C2)
add(110, "'F'(n)=F'⊗L'^{⊗n} (0_I, 5.4.10)'", "bold 0", r"(0\textsubscript{I}, 5.4.10)",
    "convention", r"(0\textsubscript{I}, 5.4.10)", r"(\textbf{0}\textsubscript{I}, 5.4.10)", conv=2, note=C2)
add(110, "'ramené au cas où A est un corps.'", "'corps' in italics", "upright",
    "italics", "est un corps.", "est un \\emph{corps}.")
add(110, "'pour un r convenable (II, 5.5.4, (ii))'", "bold II", "(II, 5.5.4, (ii))",
    "convention", r"(II, 5.5.4, (ii))", r"(\textbf{II}, 5.5.4, (ii))", conv=2, note=C2)
add(110, "'S-module gradué de type fini (II, 2.7.8)'", "bold II", "(II, 2.7.8)",
    "convention", r"(II, 2.7.8)", r"(\textbf{II}, 2.7.8)", conv=2, note=C2)
add(110, "'par des S-modules gradués libres de type fini'", "'libres' in italics", "upright",
    "italics", "gradués libres de type fini", "gradués \\emph{libres} de type fini")
add(110, "Resolution '0→L_q→L_{q-1}→ . . . →L_1→M→0'", "baseline dots", "\\cdots",
    "symbol", "L_{q-1}\\to\\cdots\\to L_1", "L_{q-1}\\to\\ldots\\to L_1",
    note="Baseline dots in the print (GLOBAL_ISSUES 22).")
add(110, "'comme M~ est un foncteur exact en M'", "only M~ (no 'M ↦')", "$M\\mapsto\\widetilde M$",
    "extra", "$M\\mapsto\\widetilde M$ est un foncteur", "$\\widetilde M$ est un foncteur",
    note="Enlarged crop: the print reads 'comme M~ est un foncteur exact en M'; 'M\\mapsto' is an addition of "
         "the TeX (the printed wording is not an error).")
add(110, "'en M (II, 2.5.4)'", "bold II", "(II, 2.5.4)",
    "convention", r"(II, 2.5.4)", r"(\textbf{II}, 2.5.4)", conv=2, note=C2)
add(110, "Sequence '0→L~_q→L~_{q-1}→ . . . →L~_1→M~→0'", "baseline dots", "\\cdots",
    "symbol", "\\widetilde L_{q-1}\\to\\cdots", "\\widetilde L_{q-1}\\to\\ldots",
    note="Baseline dots in the print (GLOBAL_ISSUES 22).")
add(110, "Sequence '0→L~_q(n)→L~_{q-1}(n)→ . . . →L~_1(n)→M~(n)→0'", "baseline dots", "\\cdots",
    "symbol", "\\widetilde L_{q-1}(n)\\to\\cdots", "\\widetilde L_{q-1}(n)\\to\\ldots",
    note="Baseline dots in the print (GLOBAL_ISSUES 22).")
add(110, "'appliquant par récurrence sur q la prop. (2.5.1), il vient'", "la prop. (2.5.1)", "la prop. (2.5.1)",
    "misprint_in_print", None, None, nofix=True, corrected="la prop. (2.5.2)",
    note="The additivity of χ_A in exact sequences is Proposition (2.5.2); (2.5.1) is the definition. "
         "The TeX keeps the printed reading.")
add(110, "'ramené au cas où M est libre et gradué de type fini'", "'libre' in italics", "upright",
    "italics", "est libre et gradué", "est \\emph{libre} et gradué")
add(110, "'Comme alors M~(n)=(M(n))~=(S(n+h))~'", "script M with tilde in the first term (𝓜~(n))",
    "\\widetilde M(n) (roman M)", "misprint_in_print",
    "$\\widetilde M(n)=(M(n))^\\sim", "$\\widetilde{\\mathcal M}(n)=(M(n))^\\sim",
    corrected="$\\widetilde M(n)=(M(n))^\\sim",
    note="Enlarged crop: the print has a script M (the S-module here is M, as in the rest of the proof). "
         "The TeX silently corrects it; the fix restores the printed reading.")
add(110, "'(S(n+h))~ (II, 2.5.15)'", "bold II", "(II, 2.5.15)",
    "convention", r"(II, 2.5.15)", r"(\textbf{II}, 2.5.15)", conv=2, note=C2)

# ---------------- p. 111 ----------------
add(111, "Lemme (2.5.3.1): 'on a alors χ_A(O_X(n))=(n+r choose r) pour tout n∈Z'", "formula inline",
    "displayed", "other",
    "\\[\n\\chi_A(\\mathcal O_X(n))=\\binom{n+r}{r}\n\\]",
    "$\\chi_A(\\mathcal O_X(n))=\\binom{n+r}{r}$",
    note=DISP)
add(111, "Proof of (2.5.3.1): 'En effet, pour n>0, on a'", "n>0", "$n\\geq0$", "misprint_in_print",
    "pour $n\\geq0$, on a", "pour $n>0$, on a", corrected="pour $n\\geq0$, on a",
    note="Enlarged crop: strict '>'. With '-r≤n≤0' below, the print puts n=0 in the last case, where "
         "C(r,r)=1≠0 and H^0(X,O_X)=A≠0; the case n=0 belongs here. The TeX silently corrects it; the fix "
         "restores the printed reading.")
add(111, "Proof of (2.5.3.1): 'on a de même χ_A(O_X(n))=(-1)^r long H^r(X, O_X(n)); si n=-r-h'",
    "formula inline", "displayed", "other",
    "\\[\n\\chi_A(\\mathcal O_X(n))=(-1)^r\n\\operatorname{long}H^r(X,\\mathcal O_X(n))~;\n\\]",
    "$\\chi_A(\\mathcal O_X(n))=(-1)^r\n\\operatorname{long}H^r(X,\\mathcal O_X(n))$~;",
    note=DISP)
add(111, "Proof of (2.5.3.1): 'c'est donc le nombre C(h+r-1,r)=(-1)^r C(n+r,r).'", "formula inline",
    "displayed", "other",
    "\\[\n\\binom{h+r-1}{r}=(-1)^r\\binom{n+r}{r}.\n\\]",
    "$\\binom{h+r-1}{r}=(-1)^r\\binom{n+r}{r}$.",
    note=DISP)
add(111, "Proof of (2.5.3.1): 'Enfin, pour -r≤n≤0, on a C(n+r,r)=0'", "-r⩽n⩽0", "$-r\\leq n<0$",
    "misprint_in_print", "$-r\\leq n<0$", "$-r\\leq n\\leq0$", corrected="$-r\\leq n<0$",
    note="Enlarged crop: '≤0'. False for n=0 (C(r,r)=1, H^0(X,O_X)=A); see the n>0 finding above. The TeX "
         "silently corrects it; the fix restores the printed reading.")
add(111, "Corollaire (2.5.4): 'On a alors χ_A(M~(n))=long M_n pour n assez grand'", "formula inline",
    "displayed", "other",
    "\\[\n\\chi_A(\\widetilde M(n))=\\operatorname{long}M_n\n\\]",
    "$\\chi_A(\\widetilde M(n))=\\operatorname{long}M_n$",
    note=DISP)
add(111, "Proposition (2.6.1), label a)", "a) upright", r"\item[a)] (italic in the proposition environment)",
    "convention", r"\item[a)]", r"\item[\textup{a)}]", conv=6,
    note="Enlarged crop: the labels a), b), c) of this statement are upright.")
add(111, "Proposition (2.6.1), label b)", "b) upright", r"\item[b)]",
    "convention", r"\item[b)]", r"\item[\textup{b)}]", conv=6, note="Enlarged crop: upright label.")
add(111, "Proposition (2.6.1) b): 'on ait R^qf_*(F⊗L^{⊗n})=0 pour tout q>0.'", "formula inline", "displayed",
    "other",
    "\\[\nR^qf_*(\\mathcal F\\otimes\\mathcal L^{\\otimes n})=0\n\\]",
    "$R^qf_*(\\mathcal F\\otimes\\mathcal L^{\\otimes n})=0$",
    note=DISP)
add(111, "Proposition (2.6.1), label c)", "c) upright", r"\item[c)]",
    "convention", r"\item[c)]", r"\item[\textup{c)}]", conv=6, note="Enlarged crop: upright label.")
add(111, "Proposition (2.6.1) c): 'on ait R^1f_*(J⊗L^{⊗n})=0.'", "formula inline", "displayed",
    "other",
    "\\[\nR^1f_*(\\mathcal J\\otimes\\mathcal L^{\\otimes n})=0.\n\\]",
    "$R^1f_*(\\mathcal J\\otimes\\mathcal L^{\\otimes n})=0$.",
    note=DISP)
add(111, "Proof of (2.6.1): 'On a vu que a) entraîne b)'", "a) and b) in italics", "upright",
    "italics", "que a) entraîne b)", "que \\emph{a)} entraîne \\emph{b)}",
    note="Enlarged crop: the letter labels are italic in the proof text.")
add(111, "Proof of (2.6.1): 'Il est trivial que b) entraîne c)'", "b) and c) in italics", "upright",
    "italics", "que b) entraîne c)", "que \\emph{b)} entraîne \\emph{c)}")
add(111, "Proof of (2.6.1): 'il reste à prouver que c) implique a)'", "c) and a) in italics", "upright",
    "italics", "que c) implique\na).", "que \\emph{c)} implique\n\\emph{a)}.")
add(111, "Proof of (2.6.1): 'Y est affine (II, 4.6.4)'", "bold II", "(II, 4.6.4)",
    "convention", r"(II, 4.6.4)", r"(\textbf{II}, 4.6.4)", conv=2, note=C2)
add(111, "Proof of (2.6.1): 'un recouvrement de X (II, 4.5.2)'", "bold II", "(II, 4.5.2)",
    "convention", r"(II, 4.5.2)", r"(\textbf{II}, 4.5.2)", conv=2, note=C2)
add(111, "Proof of (2.6.1): 'pour tout point fermé x de X'", "'fermé' in italics", "upright",
    "italics", "point\nfermé $x$", "point\n\\emph{fermé} $x$")
add(111, "Proof of (2.6.1): 'nécessairement affine (I, 1.3.6)'", "bold I", "(I, 1.3.6)",
    "convention", r"(I, 1.3.6)", r"(\textbf{I}, 1.3.6)", conv=2, note=C2)
add(111, "Proof of (2.6.1): '(I, 6.3.7 et 0_I, 2.1.3)', first number", "bold I", "(I, 6.3.7 et",
    "convention", r"(I, 6.3.7 et", r"(\textbf{I}, 6.3.7 et", conv=2, note=C2)
add(111, "Proof of (2.6.1): '(I, 6.3.7 et 0_I, 2.1.3)', second number", "bold 0", r"0\textsubscript{I}, 2.1.3)",
    "convention", r"0\textsubscript{I}, 2.1.3)", r"\textbf{0}\textsubscript{I}, 2.1.3)", conv=2, note=C2)
add(111, "Proof of (2.6.1): 'ayant pour espace sous-jacent X—U'", "X—U (long dash)", "$X-U$",
    "convention", r"$X-U$ (resp.", r"$X\setmin U$ (resp.", conv=7, note="Set difference printed with the long dash.")
add(111, "Proof of (2.6.1): '(resp. (X—U)∪{x})'", "(X—U)∪{x} (long dash)", r"$(X-U)\cup\{x\}$",
    "convention", r"$(X-U)\cup\{x\}$", r"$(X\setmin U)\cup\{x\}$", conv=7,
    note="Set difference printed with the long dash.")
add(111, "Proof of (2.6.1): '(resp. (X—U)∪{x}) (I, 5.2.1)'", "bold I", "(I, 5.2.1)",
    "convention", r"(I, 5.2.1)", r"(\textbf{I}, 5.2.1)", conv=2, note=C2)
add(111, "Proof of (2.6.1): 'sont cohérents (I, 6.1.1)'", "bold I", "(I, 6.1.1)",
    "convention", r"(I, 6.1.1)", r"(\textbf{I}, 6.1.1)", conv=2, note=C2)
add(111, "Proof of (2.6.1): 'un O_X-Module cohérent (0_I, 5.3.3)'", "bold 0", r"(0\textsubscript{I}, 5.3.3)",
    "convention", r"(0\textsubscript{I}, 5.3.3)", r"(\textbf{0}\textsubscript{I}, 5.3.3)", conv=2, note=C2)
add(111, "Proof of (2.6.1): 'tel que J''_x=k(x)'", "bold italic k in k(x)", "k(x)",
    "convention", r"\mathcal J''_x=k(x)", r"\mathcal J''_x=\boldsymbol{k}(x)", conv=1,
    note="Residue field with bold italic k.")
add(111, "Proof of (2.6.1): 'la suite 0→J'⊗L^{⊗n}→J⊗L^{⊗n}→J''⊗L^{⊗n}→0 est exacte'", "formula inline",
    "displayed", "other",
    "\\[\n0\\to\\mathcal J'\\otimes\\mathcal L^{\\otimes n}\n\\to\\mathcal J\\otimes\\mathcal L^{\\otimes n}\n"
    "\\to\\mathcal J''\\otimes\\mathcal L^{\\otimes n}\\to0\n\\]",
    "$0\\to\\mathcal J'\\otimes\\mathcal L^{\\otimes n}\n\\to\\mathcal J\\otimes\\mathcal L^{\\otimes n}\n"
    "\\to\\mathcal J''\\otimes\\mathcal L^{\\otimes n}\\to0$",
    note=DISP)

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT, len(F), "findings")
