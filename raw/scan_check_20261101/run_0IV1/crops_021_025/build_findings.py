"""Build findings_021_025.json for EGA IV-1 chapter 0, pp. 21-25, and check it.

Strings use '⏎' for a line break (LF in the page files).
"""
import json
from pathlib import Path

RUN = Path(r"user\Documents\ega_scan_check_20261101\run_0IV1")
OUT = RUN / "findings_021_025.json"

NL = "⏎"
PRE16 = ("In the page-22 continuation: ega0-16-fr.tex, before its first page marker "
         "\\oldpage[0\\textsubscript{IV-1}]{23}.")


def nl(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": nl(old), "new": nl(new)},
         "note": note}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    F.append(d)


BOLD0 = "Bold chapter number in the print, plain in the TeX."

# ---------------------------------------------------------------- page 21
add(21, "(15.2.1), end: 'associé au préfaisceau U ⇝ gr_k(Γ(U, ℱ))'",
    "U⇝gr_k(Γ(U, ℱ)): wavy (squiggly) arrow",
    r"$U\mapsto\gr_k(\Gamma(U,\mathscr{F}))$",
    "symbol", None, "high",
    r"$U\mapsto\gr_k", r"$U\leadsto\gr_k",
    "Enlarged crop: the print's wavy arrow, neither a plain arrow nor ↦ (GLOBAL_ISSUES 33).")
add(21, "(15.2.2), definition: 'la suite (f_i)_{1⩽i⩽n} est ℱ-régulière si'",
    "ℱ-régulière italic (term being defined)",
    r"est $\mathscr{F}$-régulière si",
    "italics", None, "high",
    r"est $\mathscr{F}$-régulière si, en", r"est \emph{$\mathscr{F}$-régulière} si, en",
    "Same form as \\emph{$M$-régulière} in (15.1.7).")
add(21, "(15.2.2): 'défini par f_i est injectif pour 1⩽i⩽n'",
    "injectif italic", r"défini par $f_i$ est injectif",
    "italics", None, "high",
    r"défini par $f_i$ est injectif", r"défini par $f_i$ est \emph{injectif}", "")
add(21, "(15.2.2): 'nous dirons que la suite (f_i) est ℱ-quasi-régulière si'",
    "ℱ-quasi-régulière italic (term being defined)",
    r"$\mathscr{F}$-quasi-régulière si les homomorphismes",
    "italics", None, "high",
    r"$\mathscr{F}$-quasi-régulière si les homomorphismes",
    r"\emph{$\mathscr{F}$-quasi-régulière} si les homomorphismes", "")
add(21, "(15.2.2): 'si les homomorphismes (15.2.1.1) sont injectifs'",
    "injectifs italic", "sont injectifs.",
    "italics", None, "high",
    "sont injectifs.", r"sont \emph{injectifs}.", "")
add(21, "(15.2.2): 'la suite ((f_i)_x)_{1⩽i⩽n} soit ℱ_x-régulière (resp.'",
    "ℱ_x-régulière italic (crop)", r"soit $\mathscr{F}_x$-régulière (resp.",
    "italics", None, "high",
    r"soit $\mathscr{F}_x$-régulière (resp.", r"soit \emph{$\mathscr{F}_x$-régulière} (resp.",
    "Enlarged crop: italic here, while 'soit ℱ-régulière (resp. ℱ-quasi-régulière)' earlier in the sentence is roman.")
add(21, "(15.2.2): '(resp. ℱ_x-quasi-régulière). Toute suite'",
    "ℱ_x-quasi-régulière italic (crop)", r"$\mathscr{F}_x$-quasi-régulière). Toute",
    "italics", None, "high",
    r"$\mathscr{F}_x$-quasi-régulière). Toute", r"\emph{$\mathscr{F}_x$-quasi-régulière}). Toute", "")
add(21, "(15.2.2): 'si ℱ est un 𝒪_X-Module de type fini'",
    "de type fini italic", r"Module de type fini, si les",
    "italics", None, "high",
    "Module de type fini, si les", r"Module \emph{de type fini}, si les", "")
add(21, "(15.2.2): 'si les 𝒪_x sont des anneaux noethériens'",
    "noethériens italic", "des anneaux noethériens pour",
    "italics", None, "high",
    "des anneaux noethériens pour", r"des anneaux \emph{noethériens} pour", "")
add(21, "(15.2.2): 'les (f_i)_x appartiennent au radical de 𝒪_x'",
    "radical italic", "appartiennent au radical de",
    "italics", None, "high",
    "appartiennent au radical de", r"appartiennent au \emph{radical} de", "")
add(21, "(15.2.2), second paragraph: 'il résulte de (I, 1.3)'",
    "(𝐈, 1.3): bold I", "(I, 1.3)",
    "convention", 2, "high",
    "(I, 1.3)", r"(\textbf{I}, 1.3)", BOLD0)
add(21, "(15.2.2), second paragraph: '(resp. ℱ-quasi-régulière) il faut et il suffit qu'elle soit'",
    "no comma after '(resp. ℱ-quasi-régulière)' (crop)",
    "quasi-régulière), il faut et il⏎suffit qu'elle".replace(NL, "\\n"),
    "punctuation", None, "high",
    "quasi-régulière), il faut et il⏎suffit qu'elle",
    "quasi-régulière) il faut et il⏎suffit qu'elle",
    "Enlarged crop: no comma here; the same phrase in the paragraph's first sentence ('...-quasi-régulière), il faut et il suffit que, pour tout x') does have the comma, and is left unchanged.")
add(21, "Remarque (15.2.3): 'quasi-régulière pour tout A-module M'",
    "tout italic in the roman remark", r"pour tout $A$-module",
    "italics", None, "high",
    r"pour tout $A$-module", r"pour \emph{tout} $A$-module",
    "Judged as if the remark body were roman (document-wide remark-environment item).")
add(21, "Remarque (15.2.3): 'dans tout ouvert U ne rencontrant pas V(𝔍)'",
    "ne rencontrant pas italic in the roman remark", r"ne rencontrant⏎pas $V(\mathfrak{J})$".replace(NL, "\\n"),
    "italics", None, "high",
    r"ne rencontrant⏎pas $V(\mathfrak{J})$", r"\emph{ne rencontrant⏎pas} $V(\mathfrak{J})$",
    "Judged as if the remark body were roman.")
add(21, "proof of (15.2.4): 'est cohérent (0_I, 5.3.4)'",
    "(𝟎_I, 5.3.4): bold 0", r"($0_{\mathrm I}$, 5.3.4) after 'est cohérent'",
    "convention", 2, "high",
    r"est cohérent⏎($0_{\mathrm I}$, 5.3.4)", r"est cohérent⏎($\mathbf{0}_{\mathrm I}$, 5.3.4)", BOLD0)
add(21, "proof of (15.2.4): 'défini par f_i (0_I, 5.3.4)'",
    "(𝟎_I, 5.3.4): bold 0", r"($0_{\mathrm I}$, 5.3.4) after 'défini par $f_i$'",
    "convention", 2, "high",
    r"défini par $f_i$⏎($0_{\mathrm I}$, 5.3.4)", r"défini par $f_i$⏎($\mathbf{0}_{\mathrm I}$, 5.3.4)", BOLD0)
add(21, "proof of (15.2.4): 'à un voisinage de x (0_I, 5.2.2)'",
    "(𝟎_I, 5.2.2): bold 0", r"($0_{\mathrm I}$, 5.2.2)",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 5.2.2)", r"($\mathbf{0}_{\mathrm I}$, 5.2.2)", BOLD0)
add(21, "end of p. 21's TeX segment: opening of Proposition (15.2.5)",
    "printed p. 21 ends with the proof of (15.2.4); 'Proposition (15.2.5). —' is the first line of p. 22",
    r"\begin{proposition}[15.2.5]\label{0.15.2.5-fr} stands before \oldpage[0\textsubscript{IV-1}]{22}",
    "marker", None, "high",
    r"\begin{proposition}[15.2.5]⏎\label{0.15.2.5-fr}⏎", "",
    "Move, part 1 of 2 (the opening moves, not the marker, so each edit stays in its own page segment): deletes the opening here; the page-22 marker finding re-inserts it after \\oldpage[0\\textsubscript{IV-1}]{22}. Apply both or neither.")

# ---------------------------------------------------------------- page 22
add(22, "top of p. 22: Proposition (15.2.5)",
    "p. 22 begins with 'Proposition (15.2.5). — Soit u = (ψ, θ)'",
    r"\oldpage[0\textsubscript{IV-1}]{22} stands after \begin{proposition}[15.2.5]\label{...}",
    "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{22}⏎Soit $u=",
    r"\oldpage[0\textsubscript{IV-1}]{22}⏎\begin{proposition}[15.2.5]⏎\label{0.15.2.5-fr}⏎Soit $u=",
    "Move, part 2 of 2: re-inserts the opening deleted by the page-21 marker finding. Apply both or neither.")
add(22, "Proposition (15.2.5): 'un morphisme plat d'espaces annelés (0_I, 6.7.1); soient'",
    "(𝟎_I, 6.7.1): bold 0", r"($0_{\mathrm I}$, 6.7.1)",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.7.1)", r"\textup{($\mathbf{0}_{\mathrm I}$, 6.7.1)}",
    "One edit for this finding and the next (convention 6): bold 0 and the upright reference together.")
add(22, "Proposition (15.2.5): same reference '(0_I, 6.7.1)'",
    "the reference is upright inside the italic statement",
    r"($0_{\mathrm I}$, 6.7.1) inside the italic proposition: italic",
    "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(22, "Proposition (15.2.5): 'fidèlement plat (0_I, 6.7.8)'",
    "(𝟎_I, 6.7.8): bold 0 (crop)", r"($0_{\mathrm I}$, 6.7.8)",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 6.7.8)", r"\textup{($\mathbf{0}_{\mathrm I}$, 6.7.8)}",
    "One edit for this finding and the next (convention 6): bold 0 and the upright reference together.")
add(22, "Proposition (15.2.5): same reference '(0_I, 6.7.8)'",
    "the reference is upright inside the italic statement (crop)",
    r"($0_{\mathrm I}$, 6.7.8) inside the italic proposition: italic",
    "convention", 6, "high", None, None,
    "Covered by the edit of the preceding finding (convention 2), which adds the \\textup.")
add(22, "proof of (15.2.5), display: '(g_i)_x = θ_x^♯(ψ_x^*((f_i)_y))'",
    "θ_x^♯: sharp sign (crop)", r"(g_i)_x=\theta_x^\#",
    "convention", 9, "high",
    r"(g_i)_x=\theta_x^\#", r"(g_i)_x=\theta_x^\sharp", "")
add(22, "proof of (15.2.5): 'comme par hypothèse θ_x^♯ : ψ_x^*(𝒪_y) → 𝒪_x'",
    "θ_x^♯: sharp sign (crop)", r"$\theta_x^\#:\psi_x^*",
    "convention", 9, "high",
    r"$\theta_x^\#:\psi_x^*", r"$\theta_x^\sharp:\psi_x^*", "")
add(22, "proof of (15.2.5): 'et que θ_x^♯ fait de 𝒪_x un ... fidèlement plat'",
    "θ_x^♯: sharp sign", r"que $\theta_x^\#$ fait",
    "convention", 9, "high",
    r"que $\theta_x^\#$ fait", r"que $\theta_x^\sharp$ fait", "")
add(22, "heading '16.1. Dimension d'un anneau.'",
    "title ends with a full stop", r"\subsection{Dimension d'un anneau}",
    "punctuation", None, "high",
    r"\subsection{Dimension d'un anneau}", r"\subsection{Dimension d'un anneau.}",
    PRE16 + " GLOBAL_ISSUES 43 (subsection titles lack the printed full stop) holds for ega0-16 too.")
add(22, "(16.1.1): 'On appelle dimension (ou dimension de Krull)'",
    "dimension and dimension de Krull italic", "On appelle dimension (ou dimension de Krull)",
    "italics", None, "high",
    "On appelle dimension (ou dimension de Krull)",
    r"On appelle \emph{dimension} (ou \emph{dimension de Krull})", PRE16)
add(22, "(16.1.1): '(Bourbaki, Alg. comm., chap. II, § 4, n° 3, cor. 1 de la prop. 14)'",
    "n° 3: n with raised o (crop)", "no~3",
    "symbol", None, "high",
    r"\S~4, no~3, cor.~1", r"\S~4, n\textsuperscript{o}~3, cor.~1",
    PRE16 + " Same form as elsewhere in the edition ('old' lengthened to be unique in the whole file).")
add(22, "(16.1.1): 'dim(A) est la borne supérieure des longueurs des chaînes (14.1.1)'",
    "la borne supérieure des longueurs des chaînes italic",
    "la borne supérieure des longueurs des chaînes",
    "italics", None, "high",
    "la borne supérieure des longueurs des chaînes",
    r"\emph{la borne supérieure des longueurs des chaînes}",
    PRE16 + " The italic phrase continues after the display ('d'idéaux premiers', next findings but one).")
add(22, "(16.1.1), display 𝔭_0 ⊂ 𝔭_1 ⊂ ... ⊂ 𝔭_n",
    "baseline dots '. . .' (crop)", r"\subset\cdots\subset\mathfrak{p}_n",
    "symbol", None, "high",
    r"\subset\cdots\subset\mathfrak{p}_n⏎\]", r"\subset\ldots\subset\mathfrak{p}_n⏎\]",
    PRE16 + " GLOBAL_ISSUES 22 (\\cdots for baseline dots) holds for ega0-16 too.")
add(22, "(16.1.1), after the display: 'd'idéaux premiers de A.'",
    "d'idéaux premiers italic (end of the italic phrase)", r"d'idéaux premiers de $A$. Si",
    "italics", None, "high",
    r"d'idéaux premiers de $A$. Si", r"\emph{d'idéaux premiers} de $A$. Si", PRE16)
add(22, "(16.1.1): '(Bourbaki, Alg. comm., chap. IV, § 2, n° 5, prop. 7)'",
    "n° 5: n with raised o", "no~5",
    "symbol", None, "high",
    r"\S~2, no~5, prop.~7)~; un", r"\S~2, n\textsuperscript{o}~5, prop.~7)~; un", PRE16)
add(22, "(16.1.2), after (16.1.2.1): 'Si en outre 𝔞 n'est contenu...'",
    "new indented paragraph after the display", r"\]\nSi en outre",
    "other", None, "high",
    r"\]⏎Si en outre", r"\]⏎⏎Si en outre",
    PRE16 + " Paragraph break as printed (indented line).")
add(22, "(16.1.2): 'Si en outre 𝔞 n'est contenu dans aucun idéal premier minimal 𝔭_α de A'",
    "n'est contenu dans aucun idéal premier minimal italic",
    "n'est contenu dans aucun idéal premier minimal",
    "italics", None, "high",
    "n'est contenu dans aucun idéal premier minimal",
    r"\emph{n'est contenu dans aucun idéal premier minimal}", PRE16)
add(22, "end of p. 22's TeX segment: opening of (16.1.3)",
    "printed p. 22 ends with (16.1.2.2); '(16.1.3) Si S est une partie multiplicative' is the first line of p. 23",
    r"\begin{env}[16.1.3]\label{0.16.1.3-fr} stands before \oldpage[0\textsubscript{IV-1}]{23}",
    "marker", None, "high",
    r"\begin{env}[16.1.3]⏎\label{0.16.1.3-fr}⏎", "",
    PRE16 + " Move, part 1 of 2: deletes the opening here; the page-23 marker finding re-inserts it after \\oldpage[0\\textsubscript{IV-1}]{23}. Apply both or neither.")

# ---------------------------------------------------------------- page 23
add(23, "top of p. 23: (16.1.3)",
    "p. 23 begins with '(16.1.3) Si S est une partie multiplicative de A'",
    r"\oldpage[0\textsubscript{IV-1}]{23} stands after \begin{env}[16.1.3]\label{...}",
    "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{23}⏎Si $S$",
    r"\oldpage[0\textsubscript{IV-1}]{23}⏎\begin{env}[16.1.3]⏎\label{0.16.1.3-fr}⏎Si $S$",
    "Move, part 2 of 2: re-inserts the opening deleted by the page-22 marker finding (which lies in ega0-16-fr.tex before its first marker). Apply both or neither.")
add(23, "(16.1.3), after (16.1.3.1): 'Pour tout idéal premier 𝔭 de A, on a, par définition'",
    "new indented paragraph after the display", r"\]\nPour tout idéal premier",
    "other", None, "high",
    r"\]⏎Pour tout idéal premier", r"\]⏎⏎Pour tout idéal premier",
    "Paragraph break as printed (indented line).")
add(23, "(16.1.3): 'Ce nombre est encore appelé hauteur de l'idéal premier 𝔭'",
    "hauteur italic", "encore appelé hauteur de",
    "italics", None, "high",
    "encore appelé hauteur de", r"encore appelé \emph{hauteur} de", "")
add(23, "(16.1.3): 'on appelle hauteur de 𝔞 le nombre'",
    "hauteur italic", "on appelle hauteur de",
    "italics", None, "high",
    "on appelle hauteur de", r"on appelle \emph{hauteur} de", "")
add(23, "(16.1.3), after (16.1.3.3): 'Si (𝔭_λ) est la famille...'",
    "new indented paragraph after the display", r"\]\nSi $(\mathfrak{p}_\lambda)$",
    "other", None, "high",
    r"\]⏎Si $(\mathfrak{p}_\lambda)$", r"\]⏎⏎Si $(\mathfrak{p}_\lambda)$",
    "Paragraph break as printed (indented line).")
add(23, "(16.1.3), after (16.1.3.4): 'On a évidemment'",
    "new indented paragraph after the display", r"\]\nOn a évidemment",
    "other", None, "high",
    r"\]⏎On a évidemment", r"\]⏎⏎On a évidemment",
    "Paragraph break as printed (indented line).")
add(23, "(16.1.4), after (16.1.4.1): 'On dit que A est caténaire...'",
    "new indented paragraph after the display", r"\]\nOn dit que",
    "other", None, "high",
    r"\]⏎On dit que", r"\]⏎⏎On dit que",
    "Paragraph break as printed (indented line).")
add(23, "(16.1.4): 'On dit que A est caténaire (resp. équidimensionnel, équicodimensionnel, biéquidimensionnel) lorsque Spec(A)'",
    "caténaire, équidimensionnel, équicodimensionnel, biéquidimensionnel italic (terms being defined)",
    r"$A$ est caténaire (resp. équidimensionnel, équicodimensionnel,\nbiéquidimensionnel)",
    "italics", None, "high",
    r"$A$ est caténaire (resp. équidimensionnel, équicodimensionnel,⏎biéquidimensionnel) lorsque",
    r"$A$ est \emph{caténaire} (resp. \emph{équidimensionnel}, \emph{équicodimensionnel},⏎\emph{biéquidimensionnel}) lorsque",
    "The repetition after 'lorsque Spec(A) est caténaire (resp. ...' is roman in the print and stays as is.")
add(23, "(16.1.4): 'donc, si A est caténaire, il en est de même de A/𝔞'",
    "si ... est caténaire, il en est de même de italic (A and A/𝔞 roman)",
    r"donc, si $A$ est caténaire, il en est de même de",
    "italics", None, "high",
    r"donc, si $A$ est caténaire, il en est de même de",
    r"donc, \emph{si $A$ est caténaire, il en est de même de}", "")
add(23, "(16.1.4): 'donc si A est caténaire, il en est de même de S^{-1}A'",
    "si ... est caténaire, il en est de même de italic",
    r"donc si $A$ est caténaire, il en est de même de",
    "italics", None, "high",
    r"donc si $A$ est caténaire, il en est de même de",
    r"donc \emph{si $A$ est caténaire, il en est de même de}", "")
add(23, "(16.1.4), after (16.1.4.2): 'Si A est biéquidimensionnel, il en est de même de A_𝔭'",
    "new indented paragraph after the display", r"\]\nSi $A$ est biéquidimensionnel",
    "other", None, "high",
    r"\]⏎Si $A$ est biéquidimensionnel", r"\]⏎⏎Si $A$ est biéquidimensionnel",
    "Paragraph break as printed (indented line).")

# ---------------------------------------------------------------- page 24
add(24, "proof of (16.1.5): 'Si 𝔭'_0 ⊂ 𝔭'_1 ⊂ ... ⊂ 𝔭'_n est une chaîne'",
    "baseline dots '. . .' (crop)", r"\subset\cdots\subset\mathfrak{p}'_n",
    "symbol", None, "high",
    r"\mathfrak{p}'_1\subset\cdots\subset\mathfrak{p}'_n", r"\mathfrak{p}'_1\subset\ldots\subset\mathfrak{p}'_n", "")
add(24, "proof of (16.1.5): '(Bourbaki, Alg. comm., chap. V, § 2, n° 1, cor. 1 de la prop. 1)'",
    "n° 1: n with raised o", "no~1, cor.~1",
    "symbol", None, "high",
    "no~1, cor.~1", r"n\textsuperscript{o}~1, cor.~1", "")
add(24, "proof of (16.1.5): 'pour toute chaîne 𝔭_0 ⊂ 𝔭_1 ⊂ ... ⊂ 𝔭_m'",
    "baseline dots", r"\subset\cdots\subset\mathfrak{p}_m",
    "symbol", None, "high",
    r"\mathfrak{p}_1\subset\cdots\subset\mathfrak{p}_m", r"\mathfrak{p}_1\subset\ldots\subset\mathfrak{p}_m", "")
add(24, "proof of (16.1.5): 'pour 0⩽i⩽m—1 (loc. cit., ...)'",
    "m—1: long dash (crop)", r"$0\leq i\leq m-1$",
    "convention", 7, "high",
    r"i\leq m-1$", r"i\leq m\setmin 1$",
    "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes, pending the convention-7 decision.")
add(24, "proof of (16.1.6): 'une chaîne d'idéaux premiers 𝔭_0 ⊂ 𝔭_1 ⊂ ... ⊂ 𝔭_k = 𝔪 de A'",
    "baseline dots", r"\subset\cdots\subset (before \mathfrak{p}_k=\mathfrak{m})",
    "symbol", None, "high",
    r"\mathfrak{p}_1\subset\cdots\subset⏎\mathfrak{p}_k=\mathfrak{m}", r"\mathfrak{p}_1\subset\ldots\subset⏎\mathfrak{p}_k=\mathfrak{m}", "")
add(24, "proof of (16.1.6): '(Bourbaki, Alg. comm., chap. V, § 2, n° 1, prop. 1)'",
    "n° 1: n with raised o", "no~1, prop.~1",
    "symbol", None, "high",
    "no~1, prop.~1", r"n\textsuperscript{o}~1, prop.~1", "")
add(24, "proof of (16.1.6): '(Bourbaki, Alg. comm., chap. V, § 2, n° 4, th. 3)'",
    "n° 4: n with raised o", "no~4, th.~3",
    "symbol", None, "high",
    "no~4, th.~3", r"n\textsuperscript{o}~4, th.~3", "")
add(24, "proof of (16.1.6): 'une chaîne d'idéaux premiers 𝔭'_0 ⊂ 𝔭'_1 ⊂ ... ⊂ 𝔭'_k = 𝔫 de B'",
    "baseline dots", r"\subset\cdots\subset (before \mathfrak{p}'_k=\mathfrak{n})",
    "symbol", None, "high",
    r"\mathfrak{p}'_1\subset\cdots\subset⏎\mathfrak{p}'_k=\mathfrak{n}", r"\mathfrak{p}'_1\subset\ldots\subset⏎\mathfrak{p}'_k=\mathfrak{n}", "")
add(24, "(16.1.7): 'on appelle dimension de M et on note dim_A(M)'",
    "dimension de italic (crop)", r"on appelle dimension de $M$",
    "italics", None, "high",
    r"on appelle dimension de $M$", r"on appelle \emph{dimension de} $M$", "")
add(24, "(16.1.7): 'Si M est de type fini, les idéaux premiers de A contenant Ann(M)'",
    "de type fini italic (crop)", r"Si $M$ est de type fini, les idéaux",
    "italics", None, "high",
    r"Si $M$ est de type fini, les idéaux", r"Si $M$ est \emph{de type fini}, les idéaux",
    "The later 'et si M est de type fini, on a' (before (16.1.7.3)) is roman in the print.")
add(24, "(16.1.7): 'appartiennent à Supp(M) (0_I, 1.7.4)'",
    "(𝟎_I, 1.7.4): bold 0", r"($0_{\mathrm I}$, 1.7.4)",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 1.7.4)", r"($\mathbf{0}_{\mathrm I}$, 1.7.4)", BOLD0)
add(24, "(16.1.7), after (16.1.7.1): 'Si M, N sont deux A-modules'",
    "new indented paragraph after the display", r"\]\nSi $M$, $N$",
    "other", None, "high",
    r"\]⏎Si $M$, $N$", r"\]⏎⏎Si $M$, $N$",
    "Paragraph break as printed (indented line).")
add(24, "(16.1.7), after (16.1.7.2): 'Si S est une partie multiplicative de A et si M est de type fini'",
    "new indented paragraph after the display", r"\]\nSi $S$ est une partie",
    "other", None, "high",
    r"\]⏎Si $S$ est une partie", r"\]⏎⏎Si $S$ est une partie",
    "Paragraph break as printed (indented line).")
add(24, "(16.1.7), after (16.1.7.3): 'En effet, on a Ann(S^{-1}M) = ...'",
    "new indented paragraph after the display", r"\]\nEn effet, on a",
    "other", None, "high",
    r"\]⏎En effet, on a", r"\]⏎⏎En effet, on a",
    "Paragraph break as printed (indented line).")
add(24, "(16.1.7): '(Bourbaki, Alg. comm., chap. II, § 2, n° 4) et'",
    "n° 4: n with raised o", "no~4) et",
    "symbol", None, "high",
    "no~4) et", r"n\textsuperscript{o}~4) et", "")
add(24, "(16.1.7), last paragraph: 'On dit que M est caténaire (resp. équidimensionnel, équicodimensionnel, biéquidimensionnel)'",
    "caténaire, équidimensionnel, équicodimensionnel, biéquidimensionnel italic",
    r"$M$ est caténaire (resp. équidimensionnel, équicodimensionnel,\nbiéquidimensionnel)",
    "italics", None, "high",
    r"$M$ est caténaire (resp. équidimensionnel, équicodimensionnel,⏎biéquidimensionnel) lorsque",
    r"$M$ est \emph{caténaire} (resp. \emph{équidimensionnel}, \emph{équicodimensionnel},⏎\emph{biéquidimensionnel}) lorsque", "")
add(24, "end of p. 24's TeX segment: opening of Proposition (16.1.8)",
    "printed p. 24 ends with (16.1.7); 'Proposition (16.1.8). —' is the first line of p. 25",
    r"\begin{proposition}[16.1.8]\label{0.16.1.8-fr} stands before \oldpage[0\textsubscript{IV-1}]{25}",
    "marker", None, "high",
    r"\begin{proposition}[16.1.8]⏎\label{0.16.1.8-fr}⏎", "",
    "Move, part 1 of 2: deletes the opening here; the page-25 marker finding re-inserts it after \\oldpage[0\\textsubscript{IV-1}]{25}. Apply both or neither.")

# ---------------------------------------------------------------- page 25
add(25, "top of p. 25: Proposition (16.1.8)",
    "p. 25 begins with 'Proposition (16.1.8). — Soient A un anneau'",
    r"\oldpage[0\textsubscript{IV-1}]{25} stands after \begin{proposition}[16.1.8]\label{...}",
    "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{25}⏎Soient $A$ un anneau, $M$",
    r"\oldpage[0\textsubscript{IV-1}]{25}⏎\begin{proposition}[16.1.8]⏎\label{0.16.1.8-fr}⏎Soient $A$ un anneau, $M$",
    "Move, part 2 of 2: re-inserts the opening deleted by the page-24 marker finding. Apply both or neither.")
add(25, "proof of (16.1.8): 'V(Ann(M/𝔭M)) = V(𝔭+𝔫) (0_I, 1.7.5)'",
    "(𝟎_I, 1.7.5): bold 0", r"($0_{\mathrm I}$, 1.7.5)",
    "convention", 2, "high",
    r"($0_{\mathrm I}$, 1.7.5)", r"($\mathbf{0}_{\mathrm I}$, 1.7.5)", BOLD0)
add(25, "proof of (16.1.9): '(Bourbaki, Alg. comm., chap. III, § 3, n° 1, lemme 2)'",
    "n° 1: n with raised o", "no~1, lemme~2",
    "symbol", None, "high",
    "no~1, lemme~2", r"n\textsuperscript{o}~1, lemme~2", "")
add(25, "(16.1.10): 'si M est un A-module de longueur finie, on sait'",
    "longueur finie italic", "de longueur finie, on",
    "italics", None, "high",
    "de longueur finie, on", r"de \emph{longueur finie}, on",
    "The final 'M est de longueur finie.' of (16.1.10) is roman in the print.")
add(25, "(16.1.10): '(Bourbaki, Alg. comm., chap. IV, § 2, n° 5, prop. 7 et cor. 1 de la prop. 7)'",
    "n° 5: n with raised o", "no~5, prop.~7",
    "symbol", None, "high",
    "no~5, prop.~7", r"n\textsuperscript{o}~5, prop.~7", "")
add(25, "heading '16.2. Dimension d'un anneau semi-local noethérien (¹).'",
    "title ends with a full stop after the footnote mark (crop)",
    r"...noethérien\protect\footnote{...en 1958.}}",
    "punctuation", None, "high",
    "Collège de France en 1958.}}", "Collège de France en 1958.}.}",
    "Adds the printed full stop after the footnote mark in the displayed title (the optional TOC title is unchanged). GLOBAL_ISSUES 43.")
add(25, "(16.2.1): 'Soient A un anneau semi-local noethérien, 𝔯 son radical'",
    "semi-local noethérien italic", r"anneau semi-local noethérien, $\mathfrak{r}$",
    "italics", None, "high",
    r"anneau semi-local noethérien, $\mathfrak{r}$", r"anneau \emph{semi-local noethérien}, $\mathfrak{r}$", "")
add(25, "(16.2.1): 'rappelons qu'un idéal de définition 𝔮 de A'",
    "idéal de définition italic", r"un idéal de définition $\mathfrak{q}$",
    "italics", None, "high",
    r"un idéal de définition $\mathfrak{q}$", r"un \emph{idéal de définition} $\mathfrak{q}$", "")
add(25, "(16.2.1): 'les seuls idéaux premiers contenant 𝔮 sont maximaux'",
    "maximaux italic", "sont maximaux, ou que",
    "italics", None, "high",
    "sont maximaux, ou que", r"sont \emph{maximaux}, ou que", "")
add(25, "(16.2.1): 'ou que A/𝔮 est un anneau artinien'",
    "artinien italic", "un anneau artinien. Soit",
    "italics", None, "high",
    "un anneau artinien. Soit", r"un anneau \emph{artinien}. Soit", "")
add(25, "(16.2.1): 'M/𝔮^nM est un A-module de longueur finie, égale à'",
    "longueur finie italic", "de longueur finie, égale à",
    "italics", None, "high",
    "de longueur finie, égale à", r"de \emph{longueur finie}, égale à", "")
add(25, "(16.2.1): 'égale à Σ_{i=0}^{n—1} long(gr_i(M))'",
    "upper index n—1 with the long dash (crop; compared with the ordinary minus of i−1 on p. 21)",
    r"\sum_{i=0}^{n-1}",
    "convention", 7, "medium",
    r"\sum_{i=0}^{n-1}", r"\sum_{i=0}^{n\setmin 1}",
    "Long dash used for a subtraction (GLOBAL_ISSUES 23), small type; \\setmin pending the convention-7 decision.")
add(25, "(16.2.1): 'On sait qu'il existe un polynôme Q(n)'",
    "polynôme italic", r"existe un polynôme $Q(n)$",
    "italics", None, "high",
    r"existe un polynôme $Q(n)$", r"existe un \emph{polynôme} $Q(n)$",
    "The second 'il existe un polynôme P_𝔮(M, n)' is roman in the print.")
add(25, "(16.2.1): 'pour n assez grand (III, 2.5.4)'",
    "(𝐈𝐈𝐈, 2.5.4): bold III", "(III, 2.5.4)",
    "convention", 2, "high",
    "(III, 2.5.4)", r"(\textbf{III}, 2.5.4)", BOLD0)
add(25, "(16.2.1): 'tel que long(M/𝔮^nM) = P_𝔮(M, n) pour n assez grand'",
    "formula set inline in the running text (crop)",
    r"\[ \operatorname{long}(M/\mathfrak{q}^nM)=P_{\mathfrak{q}}(M,n) \] (display)",
    "other", None, "high",
    r"tel que⏎\[⏎  \operatorname{long}(M/\mathfrak{q}^nM)=P_{\mathfrak{q}}(M,n)⏎\]⏎",
    r"tel que⏎$\operatorname{long}(M/\mathfrak{q}^nM)=P_{\mathfrak{q}}(M,n)$⏎",
    "Layout: the print sets this formula inline; the TeX displays it (GLOBAL_ISSUES 21).")
add(25, "(16.2.1): '= P_𝔮(M, n) pour n assez grand; il est clair'",
    "pour n assez grand italic (crop)", r"pour $n$ assez grand~; il est clair",
    "italics", None, "high",
    r"pour $n$ assez grand~; il est clair", r"\emph{pour $n$ assez grand}~; il est clair",
    "The earlier 'pour n assez grand (III, 2.5.4)' is roman in the print.")
add(25, "(16.2.1): 'on dit que c'est le polynôme de Hilbert-Samuel de M'",
    "polynôme de Hilbert-Samuel italic", r"le polynôme de\nHilbert-Samuel de $M$",
    "italics", None, "high",
    r"le polynôme de⏎Hilbert-Samuel de $M$", r"le \emph{polynôme de⏎Hilbert-Samuel} de $M$", "")
add(25, "end of p. 25's TeX segment: opening of Lemme (16.2.2.1)",
    "printed p. 25 ends with (16.2.1) and the footnote; 'Lemme (16.2.2.1). —' is the first line of p. 26",
    r"\begin{lemma}[16.2.2.1]\label{0.16.2.2.1-fr} stands before \oldpage[0\textsubscript{IV-1}]{26}",
    "marker", None, "high",
    r"\begin{lemma}[16.2.2.1]⏎\label{0.16.2.2.1-fr}⏎", "",
    "Move, part 1 of 2: deletes the opening here; the page-26 marker finding (next) re-inserts it after \\oldpage[0\\textsubscript{IV-1}]{26}. Apply both or neither.")

# ---------------------------------------------------------------- page 26 (outside pp. 21-25)
add(26, "top of p. 26: Lemme (16.2.2.1)",
    "p. 26 begins with 'Lemme (16.2.2.1). — Soit (M_n) une filtration 𝔮-bonne de M' (page_026_s1 checked)",
    r"\oldpage[0\textsubscript{IV-1}]{26} stands after \begin{lemma}[16.2.2.1]\label{...}",
    "marker", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{26}⏎Soit $(M_n)$",
    r"\oldpage[0\textsubscript{IV-1}]{26}⏎\begin{lemma}[16.2.2.1]⏎\label{0.16.2.2.1-fr}⏎Soit $(M_n)$",
    "OUTSIDE pages 21-25: 'old' lies in page_026.tex. Move, part 2 of 2: re-inserts the opening deleted by the page-25 marker finding. Apply both or neither.")


# ---------------------------------------------------------------- checks
def page_text(p):
    # page files are CRLF; the release sources (and the fixes) use LF
    return (RUN / f"page_{p:03d}.tex").read_bytes().decode("utf-8").replace("\r\n", "\n")


SRC = Path(r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega4")
src15 = (SRC / "ega0-15-fr.tex").read_bytes().decode("utf-8")
src16 = (SRC / "ega0-16-fr.tex").read_bytes().decode("utf-8")
assert "\r" not in src15 and "\r" not in src16
SRCALL = src15 + "\n%%FILEBREAK%%\n" + src16

ok = True
for d in F:
    if d["fix"] is None:
        continue
    t = page_text(d["page"])
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE/MISSING", d["page"], n, repr(d["fix"]["old"]))
    m = SRCALL.count(d["fix"]["old"])
    if m < 1:
        ok = False
        print("NOT IN SOURCE", d["page"], repr(d["fix"]["old"]))
    elif m > 1:
        print("note: occurs", m, "times in ega0-15/16 (unique on its page):", d["page"], repr(d["fix"]["old"]))

# sequential application, forward and reverse order, per page
for p in sorted({d["page"] for d in F}):
    fixes = [d["fix"] for d in F if d["page"] == p and d["fix"]]
    for order, seq in (("forward", fixes), ("reverse", fixes[::-1])):
        t = page_text(p)
        for fx in seq:
            if t.count(fx["old"]) != 1:
                ok = False
                print("APPLY FAIL", p, order, repr(fx["old"]))
            t = t.replace(fx["old"], fx["new"], 1)
    print("page", p, "fixes", len(fixes))

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("written", OUT, len(F), "ok" if ok else "PROBLEMS")
