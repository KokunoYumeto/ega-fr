"""Build findings_112_116.json, check that every fix's old occurs exactly once in its page file
(CRLF normalised to LF), and simulate applying the fixes of each page in order to catch overlaps."""
import json
import pathlib

RUN = pathlib.Path(__file__).resolve().parent.parent
OUT = RUN / "findings_112_116.json"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf, "fix": None if old is None else {"old": old, "new": new}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def conv2(page, where, old, new, numeral="II"):
    add(page, where, f"bold {numeral} in the reference", "plain " + numeral, "convention", 2, "high", old, new,
        f"Bold chapter numeral {numeral} in the print.")


def conv7(page, where, old, new):
    add(page, where, "long dash for set difference", "minus sign", "convention", 7, "high", old, new,
        "Long dash in the print; \\setmin as in the convention-7 pass.")


def boldK(page, where, old, new):
    add(page, where, "bold italic K / K'", "plain $K$ / $K'$", "font", None, "high", old, new,
        "Category letter K (and the exact subset K') bold italic in the print; plain italic in the TeX.")


def conv1(page, where, old, new):
    add(page, where, "bold italic k in k(y)", "plain $k(y)$", "convention", 1, "high", old, new,
        "Bold italic k in the print.")


# ---------------- p. 111/112 boundary (text in page 111's segment) ----------------
add(111, "Boundary p. 111/112: blank line before \\oldpage[III]{112} ('la suite exacte de cohomologie | prouve donc que')",
    "p. 112 begins mid-sentence, first line flush left (no paragraph break)",
    "blank line before the marker (paragraph break)", "other", None, "high",
    "exacte de cohomologie\n\n", "exacte de cohomologie\n",
    "Spurious paragraph break mid-sentence (GLOBAL_ISSUES item 20). The edit lies in p. 111's segment, before p. 112's marker.")

# ---------------- page 112 ----------------
P = 112
add(P, "1st line: 'l'homomorphisme Γ(X, J⊗L^{⊗n})→Γ(X, J''⊗L^{⊗n}) est surjectif'",
    "formula set inline in the running text", "displayed with \\[ \\]", "other", None, "high",
    "\\[\n\\Gamma(X,\\mathcal J\\otimes\\mathcal L^{\\otimes n})\n\\longrightarrow\n\\Gamma(X,\\mathcal J''\\otimes\\mathcal L^{\\otimes n})\n\\]",
    "$\\Gamma(X,\\mathcal J\\otimes\\mathcal L^{\\otimes n})\n\\to\n\\Gamma(X,\\mathcal J''\\otimes\\mathcal L^{\\otimes n})$",
    "The print sets this homomorphism inline (GLOBAL_ISSUES item 21).")
add(P, "1st line: 'est surjectif.'", "'surjectif' italic", "upright", "italics", None, "high",
    "est surjectif. Une", "est \\emph{surjectif}. Une", "Proof text is roman; 'surjectif' italic in the print.")
conv2(P, "'(car en vertu de (0_I, 5.4.1), ...'", "(0\\textsubscript{I}, 5.4.1)", "(\\textbf{0}\\textsubscript{I}, 5.4.1)", "0")
conv2(P, "Prop. (2.6.2): 'propre sur Y (II, 5.4.10) telle que'", "(II, 5.4.10) telle", "(\\textbf{II}, 5.4.10) telle")
conv7(P, "Prop. (2.6.2): 'pour tout x∈X—Z'", "$x\\in X-Z$", "$x\\in X\\setmin Z$")
conv2(P, "(2.6.2.1): 'la condition est nécessaire (II, 5.1.12)'", "nécessaire (II, 5.1.12)", "nécessaire (\\textbf{II}, 5.1.12)")
conv2(P, "(2.6.2.1): 'supposer Y affine (II, 4.6.4)'", "(II, 4.6.4)", "(\\textbf{II}, 4.6.4)")
add(P, "(2.6.2.1): 'se borner au cas où X est réduit'", "'réduit' italic", "upright", "italics", None, "high",
    "$X$ est réduit. En", "$X$ est \\emph{réduit}. En", "")
add(P, "After the diagram (2.6.2.2): 'Le morphisme f∘j est alors de type fini'",
    "'Le morphisme' begins an indented new paragraph", "continues the paragraph after \\]", "other", None, "high",
    "\\]\nLe morphisme", "\\]\n\nLe morphisme", "Paragraph break after the display in the print.")
conv2(P, "'de type fini (I, 6.3.4)'", "(I, 6.3.4)", "(\\textbf{I}, 6.3.4)", "I")
conv2(P, "'g_1 est un morphisme fini (II, 6.1.5, (iii))'", "(II, 6.1.5, (iii))", "(\\textbf{II}, 6.1.5, (iii))")
add(P, "'une immersion fermée (II, 5.1.12 et I, 4.3.2)'", "bold II and bold I", "plain II, I", "convention", 2,
    "high", "(II, 5.1.12 et I, 4.3.2)", "(\\textbf{II}, 5.1.12 et \\textbf{I}, 4.3.2)",
    "Two bold chapter numerals in one reference.")
conv2(P, "'Z_1 est propre sur Y (II, 5.4.10); d'autre part'", "(II, 5.4.10)~;", "(\\textbf{II}, 5.4.10)~;")
conv2(P, "'il résulte aussitôt de (II, 1.5.2)'", "(II, 1.5.2)", "(\\textbf{II}, 1.5.2)")
conv2(P, "'comme X est noethérien (I, 6.3.7)'", "(I, 6.3.7)", "(\\textbf{I}, 6.3.7)", "I")
conv2(P, "'ℒ est ample (II, 4.5.14)'", "(II, 4.5.14)", "(\\textbf{II}, 4.5.14)")
add(P, "'Nous supposons donc désormais Y affine et X réduit.'", "'affine' and 'réduit' italic", "upright",
    "italics", None, "high",
    "désormais $Y$ affine et $X$\nréduit.", "désormais $Y$ \\emph{affine} et $X$\n\\emph{réduit}.", "")
conv2(P, "'Les hypothèses de (II, 6.6.11)'", "(II, 6.6.11)", "(\\textbf{II}, 6.6.11)")
add(P, "'il existe un Y-préschéma réduit X_2, et un Y-morphisme'", "comma after X_2", "no comma",
    "punctuation", None, "high", "réduit $X_2$ et un", "réduit $X_2$, et un", "Enlarged crop: comma after X_2.")
add(P, "'h : X_2→X fini et birationnel'", "'fini' and 'birationnel' italic", "upright", "italics", None, "high",
    "fini et\nbirationnel tel", "\\emph{fini} et\n\\emph{birationnel} tel", "Enlarged crop.")
conv7(P, "'la restriction de h à h^{-1}(X—Z)'", "h^{-1}(X-Z)", "h^{-1}(X\\setmin Z)")
add(P, "'soit un isomorphisme sur X—Z'", "'isomorphisme' italic", "upright", "italics", None, "high",
    "soit un\nisomorphisme sur", "soit un\n\\emph{isomorphisme} sur", "Enlarged crop.")
conv7(P, "'un isomorphisme sur X—Z et que h^*(ℒ)'", "sur $X-Z$ et que", "sur $X\\setmin Z$ et que")
add(P, "'en supposant en outre que g possède les propriétés qui viennent d'être énumérées pour h.'",
    "'g possède ... pour h' italic ('que' roman)", "upright", "italics", None, "high",
    "que $g$ possède les propriétés qui viennent d'être\nénumérées pour $h$.",
    "que \\emph{$g$ possède les propriétés qui viennent d'être\nénumérées pour $h$}.", "Enlarged crop.")
conv2(P, "'qui est propre sur Y (II, 5.4.10).' before (2.6.2.3)", "(II, 5.4.10).", "(\\textbf{II}, 5.4.10).")
add(P, "(2.6.2.3): 'Soient maintenant X_1 un sous-préschéma fermé de X'", "'sous-préschéma fermé' italic",
    "upright", "italics", None, "high", "un sous-préschéma fermé de $X$,", "un \\emph{sous-préschéma fermé} de $X$,", "")
conv2(P, "(2.6.2.3): 'ample pour f∘g∘j' (II, 5.1.12)'", "j'$ (II, 5.1.12)", "j'$ (\\textbf{II}, 5.1.12)")
conv2(P, "(2.6.2.3): 'propre sur Y (II, 5.4.2, (ii))'", "(II, 5.4.2, (ii))", "(\\textbf{II}, 5.4.2, (ii))")
add(P, "(2.6.2.3): 'En d'autres termes, les hypothèses de (2.6.2) sont vérifiées pour X_1, ...'",
    "'les hypothèses de' and 'sont vérifiées pour' italic; '(2.6.2)' upright", "upright", "italics", None, "high",
    "les hypothèses de\n(\\hyperref[III.2.6.2-fr]{2.6.2}) sont vérifiées pour $X_1$",
    "\\emph{les hypothèses de}\n(\\hyperref[III.2.6.2-fr]{2.6.2}) \\emph{sont vérifiées pour} $X_1$", "Enlarged crop.")

# ---------------- page 113 ----------------
P = 113
add(P, "1st paragraph: 'par récurrence noethérienne (0_I, 2.2.2)'", "'récurrence noethérienne' italic",
    "upright", "italics", None, "high", "par récurrence noethérienne", "par \\emph{récurrence noethérienne}", "")
conv2(P, "1st paragraph: '(0_I, 2.2.2)'", "(0\\textsubscript{I}, 2.2.2)", "(\\textbf{0}\\textsubscript{I}, 2.2.2)", "0")
conv7(P, "1st paragraph: 'la restriction de g à g^{-1}(X—Z)'", "$g^{-1}(X-Z)$", "$g^{-1}(X\\setmin Z)$")
add(P, "1st paragraph: 'est un isomorphisme sur X—Z'", "'isomorphisme' italic", "upright", "italics", None,
    "high", "est un isomorphisme sur", "est un \\emph{isomorphisme} sur", "")
conv7(P, "1st paragraph: 'isomorphisme sur X—Z (ce qui est suffisant'", "sur $X-Z$ (ce", "sur $X\\setmin Z$ (ce")
add(P, "1st paragraph: 'comme on l'a vu en (2.6.2.2))'", "(2.6.2.2)", "(2.6.2.1), linked to III.2.6.2.1-fr",
    "number", None, "high",
    "(\\hyperref[III.2.6.2.1-fr]{2.6.2.1}))", "(\\hyperref[III.2.6.2.2-fr]{2.6.2.2}))",
    "Enlarged crop: the print reads (2.6.2.2). Not a misprint: the reduction to g an isomorphism over X—Z is made "
    "in the text following the display (2.6.2.2) (the paragraph 'Les hypothèses de (II, 6.6.11) ...'). The TeX "
    "changed the number.")
add(P, "(2.6.2.4): 'Soient alors A=O_X, B=g_*(O_X)'", "B = g_*(O_X) (no prime on X)", "g_*(\\mathcal O_{X'})",
    "misprint_in_print", None, "high", "\\mathcal B=g_*(\\mathcal O_{X'})", "\\mathcal B=g_*(\\mathcal O_X)",
    "Enlarged crop: the print has O_X. Since g : X'→X, B must be g_*(O_{X'}). The TeX silently corrects; the fix "
    "restores the printed reading.", corrected="\\mathcal B=g_*(\\mathcal O_{X'})")
conv7(P, "(2.6.2.4): 'la restriction B|(X—Z)'", "$\\mathcal B|(X-Z)$", "$\\mathcal B|(X\\setmin Z)$")
conv7(P, "(2.6.2.4): 'est égale à A|(X—Z)'", "$\\mathcal A|(X-Z)$", "$\\mathcal A|(X\\setmin Z)$")
add(P, "(2.6.2.4): 'Soit K le conducteur de B sur A'", "'conducteur' italic", "upright", "italics", None, "high",
    "le conducteur de", "le \\emph{conducteur} de", "")
add(P, "(2.6.2.4): 'tel que B.K ⊂ A'", "B.K with a dot", "\\mathcal B\\mathcal K (no dot)", "formula", None, "high",
    "$\\mathcal B\\mathcal K\\subset\\mathcal A$", "$\\mathcal B.\\mathcal K\\subset\\mathcal A$", "Enlarged crop.")
add(P, "(2.6.2.4): 'ou encore l'annulateur du A-Module'", "'annulateur' italic", "upright", "italics", None, "high",
    "l'annulateur du", "l'\\emph{annulateur} du", "")
conv2(P, "(2.6.2.4): 'B/A (0_I, 5.3.7)'", "(0\\textsubscript{I}, 5.3.7)", "(\\textbf{0}\\textsubscript{I}, 5.3.7)", "0")
add(P, "(2.6.2.4): 'ce qui entraîne B.K = K'", "B.K with a dot", "\\mathcal B\\mathcal K (no dot)", "formula", None,
    "high", "$\\mathcal B\\mathcal K=\\mathcal K$", "$\\mathcal B.\\mathcal K=\\mathcal K$", "Enlarged crop.")
conv7(P, "(2.6.2.4): 'en tous les points de X—Z'", "points de $X-Z$", "points de $X\\setmin Z$")
add(P, "(2.6.2.4): 'il est encore propre sur Y'", "'propre' italic", "upright", "italics", None, "high",
    "il est encore propre sur", "il est encore \\emph{propre} sur", "")
conv2(P, "(2.6.2.4): 'fermé dans Z (II, 5.4.10)'", "fermé dans $Z$ (II, 5.4.10)", "fermé dans $Z$ (\\textbf{II}, 5.4.10)")
conv7(P, "(2.6.2.4): 'B|(X—Z_1)'", "\\mathcal B|(X-Z_1)", "\\mathcal B|(X\\setmin Z_1)")
conv7(P, "(2.6.2.4): 'A|(X—Z_1)'", "\\mathcal A|(X-Z_1)", "\\mathcal A|(X\\setmin Z_1)")
conv7(P, "(2.6.2.4): 'comme on a vu que X—Z_1 est un ouvert'", "$X-Z_1$ est", "$X\\setmin Z_1$ est")
add(P, "(2.6.2.4): 'l'espace Z est distinct de X'", "'distinct' italic", "upright", "italics", None, "high",
    "est distinct de $X$", "est \\emph{distinct} de $X$", "")
conv2(P, "(2.6.2.5): 'g_*(K')=K (II, 1.4.1)'", "(II, 1.4.1)", "(\\textbf{II}, 1.4.1)")
conv2(P, "(2.6.2.5): 'Spec(B/K) (II, 1.4.10)'", "(II, 1.4.10)", "(\\textbf{II}, 1.4.10)")
conv2(P, "(2.6.2.5): 'morphisme fini (II, 6.1.5, (iii))'", "(II, 6.1.5, (iii))", "(\\textbf{II}, 6.1.5, (iii))")
add(P, "(2.6.2.5): 'Z' est propre sur Y'", "'propre' italic", "upright", "italics", None, "high",
    "$Z'$ est propre\nsur", "$Z'$ est \\emph{propre}\nsur", "")
conv2(P, "(2.6.2.5): '(II, 6.1.11 et 5.4.2, (ii))'", "(II, 6.1.11 et 5.4.2, (ii))", "(\\textbf{II}, 6.1.11 et 5.4.2, (ii))")
conv2(P, "'x∈X_s⊂U (II, 4.5.2); nous distinguerons'", "(II, 4.5.2)~;", "(\\textbf{II}, 4.5.2)~;")
conv7(P, "1°: 'On a x∈X—Z'", "$x\\in X-Z$~;", "$x\\in X\\setmin Z$~;")
conv7(P, "1°: 'aussi U⊂X—Z'", "$U\\subset X-Z$", "$U\\subset X\\setmin Z$")
conv2(P, "1°: '⊂g^{-1}(U) (II, 4.5.2). En outre'", "(II, 4.5.2). En", "(\\textbf{II}, 4.5.2). En")
conv2(P, "1°: 'au-dessus de X' (II, 4.5.5)'", "(II, 4.5.5)", "(\\textbf{II}, 4.5.5)")
conv2(P, "1°: 'il résulte de (0_I, 5.4.10)'", "(0\\textsubscript{I}, 5.4.10)", "(\\textbf{0}\\textsubscript{I}, 5.4.10)", "0")
add(P, "1°, after the display: 'La section s de K⊗L^{⊗n} qui correspond à s''", "'La section' begins an indented new paragraph",
    "continues the paragraph after \\]", "other", None, "high", "\\]\nLa section", "\\]\n\nLa section",
    "Paragraph break after the display in the print.")
conv7(P, "2°: 'ayant pour espace sous-jacent X—U'", "sous-jacent $X-U$", "sous-jacent $X\\setmin U$")
add(P, "2°, last line: 'et considérons dans B les Idéaux'", "'dans' italic", "upright", "italics", None, "high",
    "considérons dans $\\mathcal B$", "considérons \\emph{dans} $\\mathcal B$", "")
add(P, "2°, last line of the page: 'considérons dans B les Idéaux | cohérents JB et ...'",
    "'les Idéaux' (no 'deux'); 'Idéaux' is the last word of p. 113; no paragraph break at the page break",
    "'les deux', blank line, \\oldpage[III]{114}, 'Idéaux cohérents'", "extra", None, "high",
    "$\\mathcal B$ les deux\n\n", "$\\mathcal B$ les Idéaux\n",
    "The TeX adds 'deux'; the fix also moves 'Idéaux' before the p. 114 marker and removes the spurious blank line "
    "(mid-sentence page break). Apply together with the p. 114 marker fix.")

# ---------------- page 114 ----------------
P = 114
add(P, "Page start: 'cohérents JB et JK=...'", "p. 114 begins with 'cohérents' ('Idéaux' ends p. 113)",
    "marker before 'Idéaux cohérents'", "marker", None, "high",
    "\\oldpage[III]{114}\nIdéaux cohérents", "\\oldpage[III]{114}\ncohérents",
    "Apply together with the p. 113 fix ('les deux' -> 'les Idéaux').")
add(P, "Diagram (2.6.2.6) of inclusions", "plain arrows → and ↑ (no hooks)", "hook arrows \\ar@{^{(}->}",
    "symbol", None, "high",
    "\\mathcal J\\mathcal B\\ar@{^{(}->}[r] & \\mathcal B\\\\\n\\mathcal J\\ar@{^{(}->}[r]\\ar@{^{(}->}[u] &\n"
    "\\mathcal A\\ar@{^{(}->}[u]\\\\\n\\mathcal J\\mathcal K\\mathcal B=\\mathcal J\\mathcal K\n"
    "\\ar@{^{(}->}[r]\\ar@{^{(}->}[u] &\n\\mathcal K\\ar@{^{(}->}[u]",
    "\\mathcal J\\mathcal B\\ar[r] & \\mathcal B\\\\\n\\mathcal J\\ar[r]\\ar[u] &\n"
    "\\mathcal A\\ar[u]\\\\\n\\mathcal J\\mathcal K\\mathcal B=\\mathcal J\\mathcal K\n"
    "\\ar[r]\\ar[u] &\n\\mathcal K\\ar[u]",
    "Enlarged crop: all seven arrows are plain.")
add(P, "After diagram (2.6.2.6): 'Soit J' l'Idéal cohérent (JB)~'", "'Soit' begins an indented new paragraph",
    "continues the paragraph after \\]", "other", None, "high", "\\]\nSoit $\\mathcal J'$", "\\]\n\nSoit $\\mathcal J'$",
    "Paragraph break after the display in the print.")
add(P, "'(JB)~ de O_{X'} de sorte que'", "no comma after O_{X'}", "comma", "punctuation", None, "high",
    "$\\mathcal O_{X'}$, de sorte que", "$\\mathcal O_{X'}$ de sorte que", "Enlarged crop.")
add(P, "'et par suite J'/J'K' = (JB/JKB)~ (II, 1.4.4)'", "formula set inline", "displayed with \\[ \\]", "other",
    None, "high",
    "\\[\n\\mathcal J'/\\mathcal J'\\mathcal K'\n=(\\mathcal J\\mathcal B/\\mathcal J\\mathcal K\\mathcal B)^\\sim\n\\]",
    "$\\mathcal J'/\\mathcal J'\\mathcal K'\n=(\\mathcal J\\mathcal B/\\mathcal J\\mathcal K\\mathcal B)^\\sim$",
    "Inline in the print (GLOBAL_ISSUES item 21).")
conv2(P, "'(II, 1.4.4). Comme'", "(II, 1.4.4)", "(\\textbf{II}, 1.4.4)")
add(P, "'le support de J'/J'K' est contenu dans Z''", "'contenu dans' italic", "upright", "italics", None, "high",
    "est contenu dans $Z'$", "est \\emph{contenu dans} $Z'$", "")
add(P, "After the first display: 'est surjective.'", "'surjective' italic", "upright", "italics", None, "high",
    "est surjective. Mais", "est \\emph{surjective}. Mais", "")
add(P, "'Mais en vertu de (0_I, 5.4.10), on en conclut'", "'Mais' begins an indented new paragraph",
    "same paragraph as 'est surjective.'", "other", None, "high", ". Mais en vertu", ".\n\nMais en vertu",
    "Paragraph break in the print.")
conv2(P, "'Mais en vertu de (0_I, 5.4.10), on en conclut'", "(0\\textsubscript{I}, 5.4.10), on en",
      "(\\textbf{0}\\textsubscript{I}, 5.4.10), on en", "0")
add(P, "After the second display: 'est surjective.'", "'surjective' italic", "upright", "italics", None, "high",
    "est surjective.\n\nCela", "est \\emph{surjective}.\n\nCela", "")
add(P, "After the diagram of i, i': 'Soient M=i^*(L), M'=i'^*(L')'", "'Soient' begins an indented new paragraph",
    "continues the paragraph after \\]", "other", None, "high", "\\]\nSoient $\\mathcal M", "\\]\n\nSoient $\\mathcal M",
    "Paragraph break after the display in the print.")
conv2(P, "'M' est ample (II, 5.1.12)'", "(II, 5.1.12)", "(\\textbf{II}, 5.1.12)")
add(P, "'que M est ample. Par suite'", "'ample' italic", "upright", "italics", None, "high",
    "$\\mathcal M$ est ample. Par", "$\\mathcal M$ est \\emph{ample}. Par", "")
conv2(P, "'pour n assez grand (II, 4.5.5)'", "(II, 4.5.5)", "(\\textbf{II}, 4.5.5)")
conv2(P, "'on déduit encore de (0_I, 5.4.10) qu'il existe'", "(0\\textsubscript{I}, 5.4.10) qu'il",
      "(\\textbf{0}\\textsubscript{I}, 5.4.10) qu'il", "0")
add(P, "'donc s est l'image canonique d'une section t de (JB)⊗L^{⊗n}'", "'image canonique d'une section t de' italic",
    "upright", "italics", None, "high",
    "l'image\ncanonique d'une section $t$ de", "l'\\emph{image\ncanonique d'une section $t$ de}", "Enlarged crop.")
add(P, "'mod. (JKB)⊗L^{⊗n} est dans (J⊗L^{⊗n})/(JKB⊗L^{⊗n}) donc'", "formula set inline", "displayed with \\[ \\]",
    "other", None, "high",
    "\\[\n(\\mathcal J\\otimes\\mathcal L^{\\otimes n})/\n(\\mathcal J\\mathcal K\\mathcal B\\otimes\\mathcal L^{\\otimes n})\n\\]",
    "$(\\mathcal J\\otimes\\mathcal L^{\\otimes n})/\n(\\mathcal J\\mathcal K\\mathcal B\\otimes\\mathcal L^{\\otimes n})$",
    "Inline in the print (GLOBAL_ISSUES item 21).")
add(P, "'t est une section de J⊗L^{⊗n} au-dessus de X'", "'section de' italic", "upright", "italics", None, "high",
    "une section de $\\mathcal J\\otimes", "une \\emph{section de} $\\mathcal J\\otimes", "Enlarged crop.")
conv7(P, "'t(y)=0 dans X—U'", "dans $X-U$", "dans $X\\setmin U$")

# ---------------- page 115 ----------------
P = 115
add(P, "Remarque (2.6.3): heading", "'Remarque (2.6.3). —' heading, roman body",
    "\\begin{env}[2.6.3] + hand-made \\emph{Remarque.} (renders '(2.6.3) Remarque.' without the dash)",
    "other", None, "medium",
    "\\begin{env}[2.6.3]\n\\label{III.2.6.3-fr}\n\\emph{Remarque.}",
    "\\begin{remark}[2.6.3]\n\\label{III.2.6.3-fr}\n\\upshape",
    "Same treatment as the precedent for (11.7.3) (env + \\emph{Remarques} -> remarks + \\upshape). Apply together with "
    "the \\end{env} -> \\end{remark} fix below.")
add(P, "Remarque (2.6.3): end of the environment", "-", "\\end{env}", "other", None, "medium",
    "\\end{env}\n\n\\section{", "\\end{remark}\n\n\\section{",
    "Companion of the heading fix; apply both or neither.")
add(P, "Remarque (2.6.3): 'Lorsque X est propre sur Y'", "'propre' italic", "upright", "italics", None, "high",
    "est propre sur $Y$, on peut", "est \\emph{propre} sur $Y$, on peut",
    "Correct whether or not the remark heading fix is applied (env and \\upshape bodies are roman).")
conv2(P, "Remarque (2.6.3): 'le th. de Chevalley (II, 6.7.1)'", "(II, 6.7.1), à", "(\\textbf{II}, 6.7.1), à")
conv2(P, "Remarque (2.6.3): 'du lemme (II, 6.7.1.1)'", "(II, 6.7.1.1)", "(\\textbf{II}, 6.7.1.1)")
boldK(P, "Déf. (3.1.1): 'Soit K une catégorie abélienne'", "Soit $K$ une", "Soit $\\boldsymbol{K}$ une")
boldK(P, "Déf. (3.1.1): 'un sous-ensemble K' de l'ensemble'", "sous-ensemble $K'$ de\nl'ensemble",
      "sous-ensemble $\\boldsymbol{K}'$ de\nl'ensemble")
boldK(P, "Déf. (3.1.1): 'des objets de K est exact'", "objets de $K$ est", "objets de $\\boldsymbol{K}$ est")
add(P, "Déf. (3.1.1): 'est exact si'", "'exact' italic like the rest of the statement (no change of face)",
    "\\emph{exact} inside the italic definition (comes out upright)", "italics", None, "high",
    "est \\emph{exact} si", "est exact si", "Enlarged crop.")
boldK(P, "Déf. (3.1.1): 'si 0∈K''", "si $0\\in K'$", "si $0\\in\\boldsymbol{K}'$")
add(P, "Déf. (3.1.1): 'pour toute suite exacte 0→A'→A→A''→0 dans K'", "formula set inline",
    "displayed with \\[ \\]", "other", None, "high",
    "\\[\n0\\longrightarrow A'\\longrightarrow A\\longrightarrow A''\\longrightarrow0\n\\]",
    "$0\\to A'\\to A\\to A''\\to0$", "Inline in the print (GLOBAL_ISSUES item 21).")
boldK(P, "Déf. (3.1.1): 'dans K telle que'", "dans $K$ telle que", "dans $\\boldsymbol{K}$ telle que")
add(P, "Déf. (3.1.1): 'telle que deux des objets A, A', A'' soit dans K''", "'soit' (singular)", "'soit' (kept)",
    "misprint_in_print", None, "high", None, None,
    "Enlarged crop. Agreement error in the print ('deux des objets ... soient'); the TeX keeps the printed reading.",
    corrected="soient")
boldK(P, "Déf. (3.1.1): 'soit dans K', alors'", "soit dans $K'$, alors", "soit dans $\\boldsymbol{K}'$, alors")
boldK(P, "Déf. (3.1.1): 'est aussi dans K'.'", "aussi dans $K'$.", "aussi dans $\\boldsymbol{K}'$.")
boldK(P, "Th. (3.1.2): 'on désigne par K la catégorie'", "on désigne par $K$ la", "on désigne par $\\boldsymbol{K}$ la")
boldK(P, "Th. (3.1.2): 'Soient K' un sous-ensemble exact'", "Soient $K'$ un", "Soient $\\boldsymbol{K}'$ un")
boldK(P, "Th. (3.1.2): 'exact de K, X' une partie fermée'", "de\n$K$, $X'$", "de\n$\\boldsymbol{K}$, $X'$")
boldK(P, "Th. (3.1.2): 'un O_X-Module G∈K' tel que'", "$\\mathcal G\\in K'$ tel que", "$\\mathcal G\\in\\boldsymbol{K}'$ tel que")
conv1(P, "Th. (3.1.2): 'un k(y)-espace vectoriel de dimension 1'", "$k(y)$", "$\\boldsymbol{k}(y)$")
boldK(P, "Th. (3.1.2): 'appartient à K' (et en particulier'", "appartient à $K'$ (et", "appartient à $\\boldsymbol{K}'$ (et")
boldK(P, "Th. (3.1.2): 'on a K'=K)'", "on a $K'=K$)", "on a $\\boldsymbol{K}'=\\boldsymbol{K}$)")
add(P, "Proof of (3.1.2): 'la propriété suivante P(Y)'", "bold italic P", "plain $P$", "font", None, "high",
    "suivante $P(Y)$", "suivante $\\boldsymbol{P}(Y)$",
    "Property letter P bold italic in the print; plain P in the TeX (not \\mathbf, so not convention 10).")
boldK(P, "Proof of (3.1.2): 'appartient à K'. En vertu'", "appartient à\n$K'$. En vertu", "appartient à\n$\\boldsymbol{K}'$. En vertu")
conv2(P, "Proof of (3.1.2): 'récurrence noethérienne (0_I, 2.2.2)'", "(0\\textsubscript{I},\n2.2.2)",
      "(\\textbf{0}\\textsubscript{I},\n2.2.2)", "0")
add(P, "Proof of (3.1.2): 'si Y est une partie fermée de X' tel que la propriété P(Y')'", "'tel que'",
    "'telle que'", "misprint_in_print", None, "high",
    "fermée de $X'$ telle que la propriété", "fermée de $X'$ tel que la propriété",
    "Enlarged crop: the print has 'tel' (agreement error with 'partie fermée'). The TeX silently corrects; the fix "
    "restores the printed reading.", corrected="telle que")
add(P, "Proof of (3.1.2): 'la propriété P(Y') soit vraie'", "bold italic P", "plain $P$", "font", None, "high",
    "$P(Y')$", "$\\boldsymbol{P}(Y')$", "Property letter P bold italic in the print.")
add(P, "Proof of (3.1.2): 'alors P(Y) est vraie'", "bold italic P", "plain $P$", "font", None, "high",
    "alors $P(Y)$", "alors $\\boldsymbol{P}(Y)$", "Property letter P bold italic in the print.")
boldK(P, "Proof: 'Soit donc F∈K à support contenu dans Y'", "$\\mathcal F\\in K$ à support", "$\\mathcal F\\in\\boldsymbol{K}$ à support")
boldK(P, "Proof: 'et prouvons que F∈K''", "$\\mathcal F\\in K'$. Désignons", "$\\mathcal F\\in\\boldsymbol{K}'$. Désignons")
conv2(P, "Proof: 'ayant Y pour espace sous-jacent (I, 5.2.1)'", "(I, 5.2.1)", "(\\textbf{I}, 5.2.1)", "I")
conv2(P, "Proof: 'On sait (I, 9.3.4)'", "(I, 9.3.4)", "(\\textbf{I}, 9.3.4)", "I")
conv2(P, "Proof: 'de O_X-Modules cohérents (0_I, 5.3.6 et 5.3.3)'", "(0\\textsubscript{I}, 5.3.6 et 5.3.3)",
      "(\\textbf{0}\\textsubscript{I}, 5.3.6 et 5.3.3)", "0")
boldK(P, "Proof: 'comme K' est exact'", "comme $K'$ est exact", "comme $\\boldsymbol{K}'$ est exact")
boldK(P, "Proof: 'chacun des F_k ... est dans K''", "est dans\n$K'$. On est", "est dans\n$\\boldsymbol{K}'$. On est")
boldK(P, "Proof: 'prouver que F∈K' sous l'hypothèse'", "$\\mathcal F\\in K'$ sous", "$\\mathcal F\\in\\boldsymbol{K}'$ sous")
add(P, "Proof: case label 'a) Y est réductible'", "label 'a)' italic (letter and parenthesis)", "\\item[a)] upright",
    "italics", None, "high", "\\item[a)]", "\\item[\\textit{a)}]", "Enlarged crop; cf. GLOBAL_ISSUES items 16, 22.")
add(P, "Case a): 'Posons F'=F⊗_{O_X}(O_X/J'), F''=F⊗_{O_X}(O_X/J'').'", "formulas set inline",
    "displayed with \\[ \\] and \\qquad", "other", None, "high",
    "\\[\n\\mathcal F'=\\mathcal F\\otimes_{\\mathcal O_X}\n(\\mathcal O_X/\\mathcal J'),\\qquad\n"
    "\\mathcal F''=\\mathcal F\\otimes_{\\mathcal O_X}\n(\\mathcal O_X/\\mathcal J'').\n\\]",
    "$\\mathcal F'=\\mathcal F\\otimes_{\\mathcal O_X}\n(\\mathcal O_X/\\mathcal J')$,\n"
    "$\\mathcal F''=\\mathcal F\\otimes_{\\mathcal O_X}\n(\\mathcal O_X/\\mathcal J'')$.",
    "Inline in the print (GLOBAL_ISSUES item 21).")
add(P, "Last line: 'car la question est locale et | l'égalité précédente' (page break mid-sentence)",
    "no paragraph break; p. 116 starts flush left", "blank line before \\oldpage[III]{116}", "other", None, "high",
    "locale et\n\n", "locale et\n", "Spurious paragraph break mid-sentence (GLOBAL_ISSUES item 20).")

# ---------------- page 116 ----------------
P = 116
conv2(P, "1st line: 'résulte de (I, 5.2.1 et 1.1.5)'", "(I, 5.2.1 et 1.1.5)", "(\\textbf{I}, 5.2.1 et 1.1.5)", "I")
boldK(P, "'qui sont dans K (0_I, 5.3.4)'", "qui sont\ndans $K$", "qui sont\ndans $\\boldsymbol{K}$")
conv2(P, "'qui sont dans K (0_I, 5.3.4)'", "(0\\textsubscript{I}, 5.3.4)", "(\\textbf{0}\\textsubscript{I}, 5.3.4)", "0")
boldK(P, "'et sont donc dans K' par hypothèse'", "sont donc dans $K'$ par", "sont donc dans $\\boldsymbol{K}'$ par")
boldK(P, "'F' et F'' sont dans K''", "sont dans $K'$, donc aussi", "sont dans $\\boldsymbol{K}'$, donc aussi")
boldK(P, "'puisque K' est exact. La conclusion'", "puisque $K'$ est exact. La", "puisque $\\boldsymbol{K}'$ est exact. La")
add(P, "First displayed sequence '0 → Im u → F'⊕F'' → Coker u → 0'", "no comma at the end", "comma after the final 0",
    "punctuation", None, "high", "\\operatorname{Coker}u\\longrightarrow0,", "\\operatorname{Coker}u\\longrightarrow0",
    "Enlarged crop: neither displayed sequence has punctuation.")
boldK(P, "'et de l'hypothèse que K' est exact.'", "hypothèse que $K'$ est exact.", "hypothèse que $\\boldsymbol{K}'$ est exact.")
add(P, "Case label 'b) Y est irréductible'", "label 'b)' italic (letter and parenthesis)", "\\item[b)] upright",
    "italics", None, "high", "\\item[b)]", "\\item[\\textit{b)}]", "Enlarged crop; cf. GLOBAL_ISSUES items 16, 22.")
conv1(P, "Case b): '(O_Y)_y = k(y)'", "$(\\mathcal O_Y)_y=k(y)$", "$(\\mathcal O_Y)_y=\\boldsymbol{k}(y)$")
conv1(P, "Case b): 'est un k(y)-espace vectoriel de dimension finie m'", "$k(y)$-espace vectoriel de dimension finie",
      "$\\boldsymbol{k}(y)$-espace vectoriel de dimension finie")
conv1(P, "Case b): 'G_y soit un k(y)-espace vectoriel de dimension 1'", "soit un $k(y)$", "soit un $\\boldsymbol{k}(y)$")
conv1(P, "Case b): 'il y a un k(y)-isomorphisme'", "un $k(y)$-isomorphisme", "un $\\boldsymbol{k}(y)$-isomorphisme")
conv2(P, "Case b): 'F|W (0_I, 5.2.7)'", "(0\\textsubscript{I}, 5.2.7)", "(\\textbf{0}\\textsubscript{I}, 5.2.7)", "0")
add(P, "Case b): 'il existe donc un sous-O_X-Module cohérent H_0'", "sous-O_X-Module (one word)",
    "line ends 'sous-$\\mathcal O_X$-' so the newline typesets a space ('sous-O_X- Module')", "other", None, "high",
    "sous-$\\mathcal O_X$-\nModule", "sous-$\\mathcal O_X$-%\nModule", "The % keeps the line structure and removes the space.")
conv7(P, "Case b): 'induisant H sur W et 0 sur X—Y'", "sur $X-Y$ puisque", "sur $X\\setmin Y$ puisque")
conv2(P, "Case b): 'ont pour support Y (I, 9.4.7)'", "(I, 9.4.7)", "(\\textbf{I}, 9.4.7)", "I")
conv7(P, "Case b): 'dans W et dans X—Y, se réduisent'", "$X-Y$, se réduisent", "$X\\setmin Y$, se réduisent")
conv7(P, "Case b): 'l'ensemble fermé Y—(Y∩W)'", "$Y-(Y\\cap W)$", "$Y\\setmin(Y\\cap W)$")
boldK(P, "Case b): 'Ils appartiennent donc à K''", "donc à $K'$~;", "donc à $\\boldsymbol{K}'$~;")
boldK(P, "Case b): 'on a G^m∈K''", "$\\mathcal G^m\\in K'$", "$\\mathcal G^m\\in\\boldsymbol{K}'$")
boldK(P, "Case b): 'puisque G∈K''", "puisque $\\mathcal G\\in K'$", "puisque $\\mathcal G\\in\\boldsymbol{K}'$")
boldK(P, "Case b): 'et que K' est exact'", "et que $K'$ est\nexact", "et que $\\boldsymbol{K}'$ est\nexact")
boldK(P, "Case b): 'par l'exactitude de K''", "l'exactitude de $K'$", "l'exactitude de $\\boldsymbol{K}'$")
boldK(P, "Case b): 'que H_0∈K''", "$\\mathcal H_0\\in K'$", "$\\mathcal H_0\\in\\boldsymbol{K}'$")
boldK(P, "Case b): 'puis que F∈K'. C.Q.F.D.'", "puis que $\\mathcal F\\in K'$", "puis que $\\mathcal F\\in\\boldsymbol{K}'$")
boldK(P, "Cor. (3.1.3): 'le sous-ensemble exact K' de K ait'", "exact $K'$ de $K$ ait",
      "exact $\\boldsymbol{K}'$ de $\\boldsymbol{K}$ ait")
boldK(P, "Cor. (3.1.3): 'un O_X-Module cohérent M∈K''", "$\\mathcal M\\in K'$", "$\\mathcal M\\in\\boldsymbol{K}'$")
boldK(P, "Cor. (3.1.3): 'appartienne encore à K'.'", "encore à $K'$. Dans", "encore à $\\boldsymbol{K}'$. Dans")
conv1(P, "Cor. (3.1.3): '« G_y est un k(y)-espace vectoriel de dimension 1 »'", "«~$\\mathcal G_y$ est un $k(y)$",
      "«~$\\mathcal G_y$ est un $\\boldsymbol{k}(y)$")
add(P, "Proof of (3.1.3): 'modifié que dans le cas b);'", "'b)' italic (letter and parenthesis)", "upright",
    "italics", None, "high", "dans le cas b)~;", "dans le cas \\textit{b)}~;", "Enlarged crop.")
conv1(P, "Proof of (3.1.3): 'G_y est un k(y)-espace vectoriel de dimension q>0'", "cette fois $\\mathcal G_y$ est un $k(y)$",
      "cette fois $\\mathcal G_y$ est un $\\boldsymbol{k}(y)$")
add(P, "Proof of (3.1.3): 'un O_Y-isomorphisme (G_y)^m ⥲ (F_y)^q'", "O_Y-isomorphisme (one word)",
    "line ends 'un $\\mathcal O_Y$-' so the newline typesets a space ('O_Y- isomorphisme')", "other", None, "high",
    "un $\\mathcal O_Y$-\nisomorphisme", "un $\\mathcal O_Y$-%\nisomorphisme", "The % keeps the line structure and removes the space.")
boldK(P, "Proof of (3.1.3): 'prouve alors que F^q∈K''", "$\\mathcal F^q\\in K'$", "$\\mathcal F^q\\in\\boldsymbol{K}'$")
boldK(P, "Proof of (3.1.3): 'l'hypothèse additionnelle sur K''", "additionnelle sur $K'$", "additionnelle sur $\\boldsymbol{K}'$")
boldK(P, "Proof of (3.1.3): 'implique que F∈K'.'", "implique que\n$\\mathcal F\\in K'$.", "implique que\n$\\mathcal F\\in\\boldsymbol{K}'$.")
conv2(P, "Proof of (3.2.1): 'donc X noethérien (I, 6.3.7)'", "(I, 6.3.7)", "(\\textbf{I}, 6.3.7)", "I")
add(P, "Proof of (3.2.1): 'forment un sous-ensemble exact K''", "'exact' italic", "upright", "italics", None, "high",
    "forment un sous-ensemble exact", "forment un sous-ensemble \\emph{exact}", "Enlarged crop.")
boldK(P, "Proof of (3.2.1): 'K' de la catégorie K des O_X-Modules'", "$K'$ de la catégorie $K$ des",
      "$\\boldsymbol{K}'$ de la catégorie $\\boldsymbol{K}$ des")
add(P, "Last line: 'des O_X-Modules cohérents. | En effet, soit' (page break)",
    "no paragraph break: p. 117 begins 'En effet, soit' flush left", "blank line before \\oldpage[III]{117}", "other",
    None, "high", "Modules cohérents.\n\n", "Modules cohérents.\n",
    "Checked the top of p. 117: its first line is not indented. Spurious paragraph break (GLOBAL_ISSUES item 20).")

# ---------------- checks ----------------
texts = {}
for d in F:
    p = d["page"]
    if p not in texts:
        texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
bad = 0
for d in F:
    if d["fix"] is None:
        continue
    c = texts[d["page"]].count(d["fix"]["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE/ABSENT", d["page"], c, repr(d["fix"]["old"]))
# sequential application per page
work = dict(texts)
for d in F:
    if d["fix"] is None:
        continue
    p, o, n = d["page"], d["fix"]["old"], d["fix"]["new"]
    c = work[p].count(o)
    if c != 1:
        bad += 1
        print("CONFLICT at application", p, c, repr(o))
        continue
    work[p] = work[p].replace(o, n)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
cnt = Counter()
for d in F:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    cnt[(d["page"], k)] += 1
for p in sorted({d["page"] for d in F}):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("findings:", len(F), "problems:", bad)
