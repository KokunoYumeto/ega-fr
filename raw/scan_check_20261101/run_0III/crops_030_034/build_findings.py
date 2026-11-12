# Builds findings_030_034.json for the scan check of EGA 0_III pp. 30-34.
# "¶" in old/new/corrected strings stands for a line break (LF).
import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_030_034.json")
NL = "¶"


def F(page, where, scan, tex, kind, conf, old=None, new=None, conv=None, corrected=None, note=""):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected.replace(NL, "\n") if corrected else corrected
    d["note"] = note
    return d


CATNOTE = ("Category letter printed bold italic (checked on zoomed crops, pp. 30-34); "
           "ega3-1-fr.tex writes \\mathcal C (calligraphic). Same fix as for C in 0_III §8 (pp. 5-14).")
DOTS = "Baseline dots in the print (checked on a crop); the TeX has centred \\cdots."
BOLDR = ("The hypercohomology R is printed bold upright (R^•T, R^nT, R^iT of a complex); "
         "the derived functors R^pT, R^qT, R^{n-i_0}T are printed in ordinary roman.")

L = []

# ---------------- page 30 ----------------
L.append(F(30, "(11.3.2), first paragraph: 'ces filtrations sont exhaustives et séparées'",
           "'exhaustives' and 'séparées' italic", "both upright", "italics", "high",
           r"""sont exhaustives et¶séparées.""", r"""sont \emph{exhaustives} et¶\emph{séparées}."""))
L.append(F(30, "(11.3.2.2), first formula",
           "'E_2^{pq}(K••) = H_I^p(H_II^p(K••)): the inner H_II carries the exponent p "
           "(same glyph as the p of E_2^{pq}; checked on a 4x crop)",
           r"\mathrm H_{\mathrm I}^p(\mathrm H_{\mathrm{II}}^q(K^{\bullet\bullet}))",
           "misprint_in_print", "high",
           r"""=\mathrm H_{\mathrm I}^p(\mathrm H_{\mathrm{II}}^q(K^{\bullet\bullet})),""",
           r"""=\mathrm H_{\mathrm I}^p(\mathrm H_{\mathrm{II}}^p(K^{\bullet\bullet})),""",
           corrected=r"""'E_2^{pq}(K^{\bullet\bullet})=\mathrm H_{\mathrm I}^p(\mathrm H_{\mathrm{II}}^q(K^{\bullet\bullet}))""",
           note="Inner exponent p printed for q. The TeX silently corrects it; the diplomatic text keeps the "
                "printed p. Correct reading as in Cartan-Eilenberg XV, 6 and as required by (11.4.3.1) "
                "'E_2^{pq}=H^p(R^qT(K•)) on p. 33."))
L.append(F(30, "(11.3.2.2), second formula",
           "''E_2^{pq}(K••) = H_II^p(H_I^p(K••)): both exponents p (checked on a 4x crop)",
           r"\mathrm H_{\mathrm{II}}^q(\mathrm H_{\mathrm I}^p(K^{\bullet\bullet}))",
           "misprint_in_print", "high",
           r"""=\mathrm H_{\mathrm{II}}^q(\mathrm H_{\mathrm I}^p(K^{\bullet\bullet})).""",
           r"""=\mathrm H_{\mathrm{II}}^p(\mathrm H_{\mathrm I}^p(K^{\bullet\bullet})).""",
           corrected=r"""''E_2^{pq}(K^{\bullet\bullet})=\mathrm H_{\mathrm{II}}^p(\mathrm H_{\mathrm I}^q(K^{\bullet\bullet}))""",
           note="Inner exponent p printed for q (the outer p is right). The TeX's H_II^q(H_I^p) is neither the "
                "printed nor the correct reading: for F_II the filtration degree is the second index "
                "(E_0^{pq}=K^{q,p}), so ''E_2^{pq}=H_II^p(H_I^q); this is what gives (11.4.3.2) "
                "''E_2^{pq}=R^pT(H^q(K•)) on p. 33. The corrected edition needs H_II^p(H_I^q), not the "
                "current TeX reading. Same pattern on p. 31 (homological version)."))
L.append(F(30, "Prop. (11.3.3), first sentence: 'catégorie abélienne C.'", "bold italic C",
           r"$\mathcal C$", "font", "high",
           r"""abélienne¶$\mathcal C$.""", r"""abélienne¶$\boldsymbol{C}$.""", note=CATNOTE))
L.append(F(30, "Prop. (11.3.3), label (i)", "label (i) upright", "label italic inside the italic proposition",
           "convention", "high", r"""\item[(i)]""", r"""\item[\textup{(i)}]""", conv=6))
L.append(F(30, "Prop. (11.3.3) (i): '(resp. i>i_0 ou j>j_0)'", "'resp.' upright",
           "italic (proposition body)", "convention", "high",
           r"""(resp. $i>i_0$ ou $j>j_0$)""", r"""\textup{(resp.} $i>i_0$ ou $j>j_0$)""", conv=6))
L.append(F(30, "Prop. (11.3.3), label (ii)", "label (ii) upright", "label italic inside the italic proposition",
           "convention", "high", r"""\item[(ii)]""", r"""\item[\textup{(ii)}]""", conv=6))
L.append(F(30, "Prop. (11.3.3) (ii): '(resp. s'il existe j_0 et j_1 ...'", "'resp.' upright",
           "italic (proposition body)", "convention", "high",
           r"""$i>i_1$ (resp. s'il""", r"""$i>i_1$ \textup{(resp.} s'il""", conv=6))
L.append(F(30, "Prop. (11.3.3): 'Supposons en outre que dans C les limites inductives'", "bold italic C",
           r"$\mathcal C$", "font", "high",
           r"""dans $\mathcal C$ les limites""", r"""dans $\boldsymbol{C}$ les limites""", note=CATNOTE))
L.append(F(30, "Prop. (11.3.3), label (iii)", "label (iii) upright", "label italic inside the italic proposition",
           "convention", "high", r"""\item[(iii)]""", r"""\item[\textup{(iii)}]""", conv=6))
L.append(F(30, "Prop. (11.3.3) (iii): '(resp. s'il existe j_0 tel que K^{ij}=0 pour j<j_0)'", "'resp.' upright",
           "italic (proposition body)", "convention", "high",
           r"""$i>i_0$ (resp. s'il""", r"""$i>i_0$ \textup{(resp.} s'il""", conv=6))
L.append(F(30, "Prop. (11.3.3), label (iv)", "label (iv) upright", "label italic inside the italic proposition",
           "convention", "high", r"""\item[(iv)]""", r"""\item[\textup{(iv)}]""", conv=6))
L.append(F(30, "Prop. (11.3.3) (iv): '(resp. s'il existe j_0 tel que K^{ij}=0 pour j>j_0)'", "'resp.' upright",
           "italic (proposition body)", "convention", "high",
           r"""$i<i_0$ (resp. s'il""", r"""$i<i_0$ \textup{(resp.} s'il""", conv=6))
L.append(F(30, "proof of (11.3.3), 1°: 'la filtration F_I(K••) est discrète'", "'discrète' italic", "upright",
           "italics", "high", r"""est discrète.""", r"""est \emph{discrète}."""))
L.append(F(30, "proof of (11.3.3), 2°: 'la filtration F_I(K••) est co-discrète'", "'co-discrète' italic", "upright",
           "italics", "high", r"""est co-discrète.""", r"""est \emph{co-discrète}."""))
L.append(F(30, "proof of (11.3.3), 4°: display at the foot of p. 30",
           "no punctuation after the display; the sentence goes on at the top of p. 31 ('dès que p-r+1+j_0<n, ...')",
           "period after \\sum_{i+j=n}K^{ij}", "punctuation", "high",
           r"""=\sum_{i+j=n}K^{ij}.""", r"""=\sum_{i+j=n}K^{ij}""",
           note="Compare 3°, whose display (correctly) has no period either."))

# ---------------- page 31 ----------------
L.append(F(31, "(11.3.4), end: 'On voit donc finalement que l'edge-homomorphisme (11.3.4.1) provient, ...'",
           "only 'edge-homomorphisme' and 'provient, par passage à la cohomologie, de l'injection canonique' "
           "italic; 'l'' before edge and the reference (11.3.4.1) upright",
           "one \\emph covering l'edge-homomorphisme, the reference and the rest", "italics", "high",
           r"""\emph{l'edge-homomorphisme¶(\hyperref[0.11.3.4.1-fr]{11.3.4.1}) provient, par passage à la cohomologie,¶de l'injection canonique}""",
           r"""l'\emph{edge-homomorphisme}¶(\hyperref[0.11.3.4.1-fr]{11.3.4.1}) \emph{provient, par passage à la cohomologie,¶de l'injection canonique}"""))
L.append(F(31, "(11.3.5), first sentence: 'un bicomplexe de C dont'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""$\mathcal C$ dont""", r"""$\boldsymbol{C}$ dont""", note=CATNOTE))
L.append(F(31, "(11.3.5): 'son p^e objet d'homologie'", "p^e (superscript e)", "$p$-ème", "word", "high",
           r"""son $p$-ème objet""", r"""son $p$\textsuperscript{e} objet""",
           note="The edition writes printed ordinals as \\textsuperscript{e} elsewhere (2\\textsuperscript{e} éd.)."))
L.append(F(31, "(11.3.5): 'son q^e objet d'homologie'", "q^e (superscript e)", "$q$-ème", "word", "high",
           r"""son $q$-ème objet""", r"""son $q$\textsuperscript{e} objet"""))
L.append(F(31, "(11.3.5): 'le n^e objet d'homologie'", "n^e (superscript e)", "$n$-ème", "word", "high",
           r"""le $n$-ème objet""", r"""le $n$\textsuperscript{e} objet"""))
L.append(F(31, "(11.3.5), second display (E^2 terms), second formula",
           "''E^2_{pq}(K..) = H^II_p(H^I_p(K..)): both subscripts p (checked on a 4x crop)",
           r"\mathrm H_q^{\mathrm{II}}(\mathrm H_p^{\mathrm I}(K_{\bullet\bullet}))",
           "misprint_in_print", "high",
           r"""=\mathrm H_q^{\mathrm{II}}(\mathrm H_p^{\mathrm I}(K_{\bullet\bullet})).""",
           r"""=\mathrm H_p^{\mathrm{II}}(\mathrm H_p^{\mathrm I}(K_{\bullet\bullet})).""",
           corrected=r"""''E_{pq}^2(K_{\bullet\bullet})=\mathrm H_p^{\mathrm{II}}(\mathrm H_q^{\mathrm I}(K_{\bullet\bullet}))""",
           note="Inner subscript p printed for q. From ''E^2_{pq}(K..)=''E_2^{-p,-q}(K'••) and the correct (11.3.2.2) "
                "one gets H^II_p(H^I_q(K..)), parallel to the first formula 'E^2_{pq}=H^I_p(H^II_q(K..)), which the "
                "print has right. The TeX's H^II_q(H^I_p) is neither the printed nor the correct reading "
                "(same pattern as (11.3.2.2), p. 30)."))
L.append(F(31, "(11.3.6), first item label", "'a)' italic, no opening parenthesis (list run into the text)",
           "\\item[(a)] (upright, with parentheses)", "punctuation", "high",
           r"""\item[(a)]""", r"""\item[\textit{a)}]""",
           note="(11.3.6) is an env (roman body); the printed labels a), b), c) are italic."))

# ---------------- page 32 ----------------
L.append(F(32, "(11.3.6) a), end: '... ou pour j<j_0); b)'", "semicolon after the parenthesis", "period",
           "punctuation", "high", r"""$j<j_0$).""", r"""$j<j_0$)~;"""))
L.append(F(32, "(11.3.6), second item label", "'b)' italic, no opening parenthesis", "\\item[(b)]",
           "punctuation", "high", r"""\item[(b)]""", r"""\item[\textit{b)}]"""))
L.append(F(32, "(11.3.6) b), end: '... pour i<i_0 et i>i_1; c)'", "semicolon", "period",
           "punctuation", "high", r"""$i>i_1$.""", r"""$i>i_1$~;"""))
L.append(F(32, "(11.3.6), third item label", "'c)' italic, no opening parenthesis", "\\item[(c)]",
           "punctuation", "high", r"""\item[(c)]""", r"""\item[\textit{c)}]"""))
L.append(F(32, "(11.3.6): 'La suite 'E(K..) est régulière s'il existe'", "'régulière' italic", "upright",
           "italics", "high", r"""La suite $'E(K_{\bullet\bullet})$ est régulière""",
           r"""La suite $'E(K_{\bullet\bullet})$ est \emph{régulière}"""))
L.append(F(32, "(11.3.6): 'La suite ''E(K..) est régulière s'il existe'", "'régulière' italic", "upright",
           "italics", "high", r"""La suite $''E(K_{\bullet\bullet})$ est régulière""",
           r"""La suite $''E(K_{\bullet\bullet})$ est \emph{régulière}"""))
L.append(F(32, "(11.4.1), first sentence: 'Soit C une catégorie abélienne'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""Soit $\mathcal C$ une catégorie""", r"""Soit $\boldsymbol{C}$ une catégorie""",
           note=CATNOTE))
L.append(F(32, "(11.4.1): 'd'un objet A de C un complexe d'objets de C, dont'", "bold italic C (twice)",
           r"$\mathcal C$ (twice)", "font", "high",
           r"""$\mathcal C$ un complexe d'objets de $\mathcal C$, dont""",
           r"""$\boldsymbol{C}$ un complexe d'objets de $\boldsymbol{C}$, dont"""))
L.append(F(32, "(11.4.1), first display", "0→L^0→L^1→L^2... (no arrow after L^2; baseline dots)",
           "0→L^0→L^1→L^2→\\cdots", "extra", "high",
           r"""\longrightarrow L^2¶  \longrightarrow\cdots""", r"""\longrightarrow L^2¶  \ldots""",
           note="Checked on a crop: the dots follow L^2 directly."))
L.append(F(32, "(11.4.1), diagram (both rows end with dots)", "baseline dots '...' in both rows",
           "\\cdots (twice)", "symbol", "high",
           r"""& \cdots\\¶  0\ar[r] & L^0\ar[r] & L^1\ar[r] & L^2\ar[r] & \cdots""",
           r"""& \ldots\\¶  0\ar[r] & L^0\ar[r] & L^1\ar[r] & L^2\ar[r] & \ldots""", note=DOTS))
L.append(F(32, "(11.4.1), display 0→A→L^0→L^1→...", "baseline dots", "\\cdots", "symbol", "high",
           r"""\longrightarrow L^1¶  \longrightarrow\cdots""", r"""\longrightarrow L^1¶  \longrightarrow\ldots""",
           note=DOTS))
L.append(F(32, "(11.4.1): 'soit exacte; de même une résolution gauche'", "'exacte' italic", "upright",
           "italics", "high", r"""soit exacte~;""", r"""soit \emph{exacte}~;"""))
L.append(F(32, "(11.4.1): inline complex 0←L_0←L_1←...", "baseline dots", "\\cdots", "symbol", "high",
           r"""L_1\leftarrow\cdots$""", r"""L_1\leftarrow\ldots$""", note=DOTS))
L.append(F(32, "(11.4.1): 'd'objets de C dont l'opérateur de dérivation est de degré -1'", "bold italic C",
           r"$\mathcal C$", "font", "high",
           r"""d'objets de $\mathcal C$¶dont""", r"""d'objets de $\boldsymbol{C}$¶dont"""))
L.append(F(32, "(11.4.1), display 0←A←L_0←L_1←...", "baseline dots", "\\cdots", "symbol", "high",
           r"""L_1¶  \longleftarrow\cdots""", r"""L_1¶  \longleftarrow\ldots""", note=DOTS))
L.append(F(32, "(11.4.1): 'de sorte que la suite ... soit exacte.'", "'exacte' italic", "upright",
           "italics", "high", r"""soit exacte.""", r"""soit \emph{exacte}."""))
L.append(F(32, "(11.4.1), second paragraph: 'cette résolution est de longueur ≤n'",
           "'de longueur' italic (the 'de' too)", "'de' upright, \\emph starts at 'longueur'", "italics", "high",
           r"""est de¶\emph{longueur""", r"""est \emph{de¶longueur"""))
L.append(F(32, "(11.4.1), third paragraph: 'si les objets de C autres que A'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""les objets de $\mathcal C$ autres""", r"""les objets de $\boldsymbol{C}$ autres"""))
L.append(F(32, "(11.4.1), third paragraph: 'Lorsque C est la catégorie des modules'", "bold italic C",
           r"$\mathcal C$", "font", "high", r"""Lorsque $\mathcal C$ est la""", r"""Lorsque $\boldsymbol{C}$ est la"""))
L.append(F(32, "(11.4.2), first sentence: 'un complexe d'objets de C, dont'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""d'objets de $\mathcal C$,¶dont""", r"""d'objets de $\boldsymbol{C}$,¶dont"""))

# ---------------- page 33 ----------------
L.append(F(33, "(11.4.2) (i), first display line 0→K^i→L^{i0}→L^{i1}→...", "baseline dots", "\\cdots",
           "symbol", "high", r"""L^{i1}\longrightarrow\cdots""", r"""L^{i1}\longrightarrow\ldots""", note=DOTS))
L.append(F(33, "(11.4.2) (i), display line for B", "baseline dots", "\\cdots", "symbol", "high",
           r"""\mathrm B_{\mathrm I}^i(L^{\bullet,1})¶        \longrightarrow\cdots""",
           r"""\mathrm B_{\mathrm I}^i(L^{\bullet,1})¶        \longrightarrow\ldots""", note=DOTS))
L.append(F(33, "(11.4.2) (i), display line for Z", "baseline dots", "\\cdots", "symbol", "high",
           r"""\mathrm Z_{\mathrm I}^i(L^{\bullet,1})¶        \longrightarrow\cdots""",
           r"""\mathrm Z_{\mathrm I}^i(L^{\bullet,1})¶        \longrightarrow\ldots""", note=DOTS))
L.append(F(33, "(11.4.2) (i), display line for H", "baseline dots", "\\cdots", "symbol", "high",
           r"""\mathrm H_{\mathrm I}^i(L^{\bullet,1})¶        \longrightarrow\cdots""",
           r"""\mathrm H_{\mathrm I}^i(L^{\bullet,1})¶        \longrightarrow\ldots""", note=DOTS))
L.append(F(33, "(11.4.2) (i): '(B_I^i(L••))'", "L•• (no comma between the bullets)", "L^{\\bullet,\\bullet}",
           "formula", "high", r"""\mathrm B_{\mathrm I}^i(L^{\bullet,\bullet})""",
           r"""\mathrm B_{\mathrm I}^i(L^{\bullet\bullet})""",
           note="Checked on a 3x crop; (L^{i,•}) just before has its comma."))
L.append(F(33, "(11.4.2) (i): '(Z_I^i(L••))'", "L•• (no comma)", "L^{\\bullet,\\bullet}", "formula", "high",
           r"""\mathrm Z_{\mathrm I}^i(L^{\bullet,\bullet})""", r"""\mathrm Z_{\mathrm I}^i(L^{\bullet\bullet})"""))
L.append(F(33, "(11.4.2) (i): '(H_I^i(L••))'", "L•• (no comma)", "L^{\\bullet,\\bullet}", "formula", "high",
           r"""\mathrm H_{\mathrm I}^i(L^{\bullet,\bullet})""", r"""\mathrm H_{\mathrm I}^i(L^{\bullet\bullet})"""))
L.append(F(33, "(11.4.2) (ii), after (11.4.2.2): 'sont scindées.'", "'scindées' italic", "upright",
           "italics", "high", r"""sont scindées.""", r"""sont \emph{scindées}."""))
L.append(F(33, "(11.4.2): 'que si tout objet de C est sous-objet'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""objet de $\mathcal C$ est sous-objet""", r"""objet de $\boldsymbol{C}$ est sous-objet""",
           note=CATNOTE))
L.append(F(33, "(11.4.2): 'tout complexe K• de C admet'", "bold italic C", r"$\mathcal C$", "font", "high",
           r"""$K^\bullet$ de $\mathcal C$ admet""", r"""$K^\bullet$ de $\boldsymbol{C}$ admet"""))
L.append(F(33, "(11.4.2): 'f : K•→K'• de complexes de C, toute'", "bold italic C", r"$\mathcal C$", "font", "high",
           r"""complexes de¶$\mathcal C$, toute""", r"""complexes de¶$\boldsymbol{C}$, toute"""))
L.append(F(33, "(11.4.2): 'et toute résolution injective de Cartan-Eilenberg L'•• de K'•'", "'injective' italic",
           "upright", "italics", "high", r"""toute résolution injective de Cartan-Eilenberg""",
           r"""toute résolution \emph{injective} de Cartan-Eilenberg"""))
L.append(F(33, "(11.4.2), last paragraph: 'tout objet de C admette une résolution injective'", "bold italic C",
           r"$\mathcal C$", "font", "high", r"""tout objet de¶$\mathcal C$ admette""",
           r"""tout objet de¶$\boldsymbol{C}$ admette"""))
L.append(F(33, "(11.4.3), first sentence: 'additif de C dans une catégorie abélienne C''", "bold italic C and C'",
           r"$\mathcal C$, $\mathcal C'$", "font", "high",
           r"""additif} de $\mathcal C$¶dans une catégorie abélienne $\mathcal C'$""",
           r"""additif} de $\boldsymbol{C}$¶dans une catégorie abélienne $\boldsymbol{C}'$"""))
L.append(F(33, "(11.4.3): 'Étant donnés un complexe K• de C et une résolution'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""$K^\bullet$ de $\mathcal C$ et une résolution""",
           r"""$K^\bullet$ de $\boldsymbol{C}$ et une résolution"""))
L.append(F(33, "(11.4.3): 'une résolution de Cartan-Eilenberg injective L•• de K•, supposons'",
           "'injective' italic", "upright", "italics", "high",
           r"""Cartan-Eilenberg injective¶$L^{\bullet\bullet}$ de""",
           r"""Cartan-Eilenberg \emph{injective}¶$L^{\bullet\bullet}$ de""",
           note="The later 'résolution de Cartan-Eilenberg injective L•• choisie' is upright in the print, as in the TeX."))
L.append(F(33, "(11.4.3): 'sont dites suites spectrales d'hypercohomologie de T par rapport au complexe K•'",
           "only 'suites spectrales d'hypercohomologie' italic", "\\emph runs to the end of 'complexe K•'",
           "italics", "high",
           r"""\emph{suites spectrales d'hypercohomologie de $T$ par rapport au¶complexe $K^\bullet$}""",
           r"""\emph{suites spectrales d'hypercohomologie} de $T$ par rapport au¶complexe $K^\bullet$"""))
L.append(F(33, "(11.4.3): 'appelé encore l'hypercohomologie de T par rapport à K•'",
           "only 'hypercohomologie' italic", "\\emph includes 'de T par rapport à K•'", "italics", "high",
           r"""l'\emph{hypercohomologie de $T$ par rapport à $K^\bullet$}, et noté""",
           r"""l'\emph{hypercohomologie} de $T$ par rapport à $K^\bullet$, et noté"""))
L.append(F(33, "(11.4.3): 'et noté R•T(K•)'", "bold upright R", r"\mathrm R", "font", "high",
           r"""$\mathrm R^\bullet T(K^\bullet)$. On montre""", r"""$\mathbf R^\bullet T(K^\bullet)$. On montre""",
           note=BOLDR))
L.append(F(33, "(11.4.3.1): 'E_2^{pq} = H^p(R^qT(K•))", "the exponent p of H is set in bold italic (wrong font); "
           "the p, q of E_2^{pq} and the q of R^q are ordinary italic (checked on a 5x crop)",
           "ordinary $p$", "misprint_in_print", "medium",
           r"""'E_2^{pq}=\mathrm H^p(\mathrm R^qT(K^\bullet))""",
           r"""'E_2^{pq}=\mathrm H^{\boldsymbol{p}}(\mathrm R^qT(K^\bullet))""",
           corrected=r"""'E_2^{pq}=\mathrm H^p(\mathrm R^qT(K^\bullet))""",
           note="Wrong-font letter (recorded as a misprint, reproduced in the diplomatic text, as for the bold "
                "italic n in EGA II). The TeX silently normalizes it."))
L.append(F(33, "(11.4.3.2): ''E_2^{pq} = R^pT(H^q(K•))", "the exponent p of R is set in bold italic (wrong font); "
           "checked on a 5x crop", "ordinary $p$", "misprint_in_print", "medium",
           r"""''E_2^{pq}=\mathrm R^pT(\mathrm H^q(K^\bullet))""",
           r"""''E_2^{pq}=\mathrm R^{\boldsymbol{p}}T(\mathrm H^q(K^\bullet))""",
           corrected=r"""''E_2^{pq}=\mathrm R^pT(\mathrm H^q(K^\bullet))""",
           note="As (11.4.3.1): wrong-font p; the TeX silently normalizes it."))

# ---------------- page 34 ----------------
L.append(F(34, "first line: 'le p^e foncteur dérivé'", "p^e (superscript e)", "$p$-ième", "word", "high",
           r"""le $p$-ième \emph{foncteur""", r"""le $p$\textsuperscript{e} \emph{foncteur"""))
L.append(F(34, "'Sauf mention expresse du contraire, ...' (the paragraph cited as (11.4.4))",
           "no number (11.4.4) anywhere: the print numbers (11.4.3) and then Proposition (11.4.5), whose proof "
           "cites '(11.4.4)'; 'Sauf mention ...' runs on in the same paragraph",
           "no visible number; invisible anchor \\phantomsection\\label{0.11.4.4-fr}",
           "misprint_in_print", "medium", None, None,
           corrected=r"""$(\mathrm R^qT(K^i))_{i\in\mathbb Z}$.¶\end{env}¶¶\begin{env}[11.4.4]¶\label{0.11.4.4-fr}¶Sauf mention expresse du contraire""",
           note="The TeX keeps the printed reading (no number). The heading (11.4.4) is missing in the print; "
                "the block from 'Sauf mention' to '... suites spectrales de cohomologie.' is what the proof of "
                "(11.4.5) cites ('comme elle est régulière (11.4.4)'), so the corrected edition should open "
                "(11.4.4) there (the existing \\end{env} after 'cohomologie.' then closes it). See the next finding "
                "for the paragraph break."))
L.append(F(34, "'(R^qT(K^i))_{i∈Z}. Sauf mention expresse du contraire'",
           "same paragraph, same line (no break, no indent)", "blank line: new paragraph before the anchor",
           "other", "high",
           r"""$(\mathrm R^qT(K^i))_{i\in\mathbb Z}$.¶¶\phantomsection\label{0.11.4.4-fr}¶Sauf""",
           r"""$(\mathrm R^qT(K^i))_{i\in\mathbb Z}$.¶\phantomsection\label{0.11.4.4-fr}Sauf""",
           note="Keeps the anchor used by the reference (11.4.4) in the proof of (11.4.5)."))
L.append(F(34, "'tout objet de C est sous-objet d'un objet injectif de C'", "bold italic C (twice)",
           r"$\mathcal C$ (twice)", "font", "high",
           r"""de $\mathcal C$ est sous-objet d'un objet injectif de $\mathcal C$, de sorte""",
           r"""de $\boldsymbol{C}$ est sous-objet d'un objet injectif de $\boldsymbol{C}$, de sorte""", note=CATNOTE))
L.append(F(34, "'existent pour tout complexe de C. Comme'", "bold italic C", r"$\mathcal C$", "font", "high",
           r"""de $\mathcal C$. Comme""", r"""de $\boldsymbol{C}$. Comme"""))
L.append(F(34, "2°: 'Tout objet de C admet une résolution injective'", "bold italic C", r"$\mathcal C$",
           "font", "high", r"""Tout objet de $\mathcal C$ admet""", r"""Tout objet de $\boldsymbol{C}$ admet"""))
L.append(F(34, "'Lorsqu'on suppose que dans C' les limites inductives'", "bold italic C'", r"$\mathcal C'$",
           "font", "high", r"""Lorsqu'on suppose que dans $\mathcal C'$""",
           r"""Lorsqu'on suppose que dans $\boldsymbol{C}'$"""))
L.append(F(34, "'l'existence dans C' des sommes directes infinies'", "bold italic C'", r"$\mathcal C'$",
           "font", "high", r"""$\mathcal C'$ des sommes""", r"""$\boldsymbol{C}'$ des sommes"""))
L.append(F(34, "'R^nT(K•) est isomorphe à R^{n-i_0}T(K^{i_0})'", "first R bold upright, second R roman",
           r"\mathrm R (both)", "font", "high",
           r"""$\mathrm R^nT(K^\bullet)$ est isomorphe""", r"""$\mathbf R^nT(K^\bullet)$ est isomorphe""",
           note=BOLDR))
L.append(F(34, "'Si K• et K'• sont deux complexes de C, f, g'", "bold italic C", r"$\mathcal C$", "font", "high",
           r"""complexes de $\mathcal C$, $f$, $g$""", r"""complexes de $\boldsymbol{C}$, $f$, $g$"""))
L.append(F(34, "'les morphismes R•T(K•)→R•T(K'•)'", "both R bold upright", r"\mathrm R (both)", "font", "high",
           r"""$\mathrm R^\bullet T(K^\bullet)\to¶\mathrm R^\bullet T(K'^\bullet)$""",
           r"""$\mathbf R^\bullet T(K^\bullet)\to¶\mathbf R^\bullet T(K'^\bullet)$""", note=BOLDR))
L.append(F(34, "Prop. (11.4.5): 'Supposons que dans C' les limites'", "bold italic C'", r"$\mathcal C'$",
           "font", "high", r"""Supposons que dans $\mathcal C'$""", r"""Supposons que dans $\boldsymbol{C}'$"""))
L.append(F(34, "(11.4.5.1): R^iT(K•) ⥲ H^i(T(K•))", "R bold upright (the R^nT(K^i) of the statement is roman)",
           r"\mathrm R", "font", "high",
           r"""\mathrm R^iT(K^\bullet)\xrightarrow{\sim}""", r"""\mathbf R^iT(K^\bullet)\xrightarrow{\sim}""",
           note=BOLDR))
L.append(F(34, "(11.4.6), first sentence: 'un bifoncteur covariant'", "only 'bifoncteur' italic",
           "\\emph{bifoncteur covariant}", "italics", "high",
           r"""\emph{bifoncteur covariant}""", r"""\emph{bifoncteur} covariant"""))
L.append(F(34, "(11.4.6): '(M, N)→T(M, N)'", "plain arrow", "\\mapsto", "convention", "high",
           r"""$(M,N)\mapsto T(M,N)$""", r"""$(M,N)\to T(M,N)$""", conv=3))
L.append(F(34, "(11.4.6): 'de C×C' dans C'', C, C', C'' étant trois catégories'", "bold italic C, C', C'' (six letters)",
           r"\mathcal C, \mathcal C', \mathcal C''", "font", "high",
           r"""$\mathcal C\times\mathcal C'$ dans $\mathcal C''$,¶$\mathcal C$, $\mathcal C'$, $\mathcal C''$ étant""",
           r"""$\boldsymbol{C}\times\boldsymbol{C}'$ dans $\boldsymbol{C}''$,¶$\boldsymbol{C}$, $\boldsymbol{C}'$, $\boldsymbol{C}''$ étant"""))
L.append(F(34, "(11.4.6): 'tout objet de C et tout objet de C' sont sous-objets'", "bold italic C, C'",
           r"\mathcal C, \mathcal C'", "font", "high",
           r"""tout objet de $\mathcal C$ et tout objet de¶$\mathcal C'$ sont""",
           r"""tout objet de $\boldsymbol{C}$ et tout objet de¶$\boldsymbol{C}'$ sont"""))
L.append(F(34, "(11.4.6): 'existent dans C'' et sont exactes'", "bold italic C''", r"$\mathcal C''$", "font", "high",
           r"""existent dans $\mathcal C''$ et sont""", r"""existent dans $\boldsymbol{C}''$ et sont"""))
L.append(F(34, "(11.4.6): 'On définit alors l'hypercohomologie de T par rapport à deux complexes'",
           "only 'hypercohomologie' italic", "\\emph includes 'de T par rapport à deux complexes'",
           "italics", "high",
           r"""l'\emph{hypercohomologie de $T$ par rapport à deux complexes}""",
           r"""l'\emph{hypercohomologie} de $T$ par rapport à deux complexes"""))
L.append(F(34, "(11.4.6): 'de C et C' respectivement'", "bold italic C, C'", r"\mathcal C, \mathcal C'",
           "font", "high", r"""de $\mathcal C$ et $\mathcal C'$ respectivement""",
           r"""de $\boldsymbol{C}$ et $\boldsymbol{C}'$ respectivement"""))
L.append(F(34, "(11.4.6): 'quadricomplexe de C'', que l'on considère comme bicomplexe de C''", "bold italic C'' (twice)",
           r"$\mathcal C''$ (twice)", "font", "high",
           r"""quadricomplexe de¶$\mathcal C''$, que l'on considère comme \emph{bicomplexe} de $\mathcal C''$""",
           r"""quadricomplexe de¶$\boldsymbol{C}''$, que l'on considère comme \emph{bicomplexe} de $\boldsymbol{C}''$"""))
L.append(F(34, "(11.4.6): 'L'hypercohomologie de T par rapport à K• et K'• est par définition'",
           "only 'hypercohomologie' italic", "\\emph includes 'de T par rapport à K• et K'•'", "italics", "high",
           r"""L'\emph{hypercohomologie de $T$ par rapport à $K^\bullet$ et $K'^\bullet$}""",
           r"""L'\emph{hypercohomologie} de $T$ par rapport à $K^\bullet$ et $K'^\bullet$"""))
L.append(F(34, "end of p. 34 / start of p. 35",
           "p. 34 ends with '(autrement dit, celle du complexe simple associé)'; p. 35 begins "
           "'notée R•T(K•, K'•); elle est l'aboutissement de deux suites spectrales dont les termes E_2 sont "
           "donnés par' (checked on page_035_s1.png)",
           "\\oldpage[0\\textsubscript{III}]{35} stands only before the (11.4.6.1) display, so that sentence is in "
           "the p. 34 segment", "marker", "high",
           r"""simple associé) notée¶""",
           r"""simple associé)¶\oldpage[0\textsubscript{III}]{35}¶notée¶""",
           note="Apply together with the page-35 entry below, which removes the old marker before (11.4.6.1). "
                "The page-35 checker may report the same sentence as missing at the top of p. 35."))
L.append(F(34, "'notée R•T(K•, K'•)' (printed at the top of p. 35, in the p. 34 segment of the TeX)",
           "R bold upright", r"\mathrm R", "font", "high",
           r"""$\mathrm R^\bullet T(K^\bullet,K'^\bullet)$""", r"""$\mathbf R^\bullet T(K^\bullet,K'^\bullet)$""",
           note=BOLDR + " Independent of the marker move."))
L.append(F(35, "start of page_035.tex: second half of the p. 34/35 marker move",
           "p. 35 begins with 'notée R•T(K•, K'•); ...', before (11.4.6.1)",
           "\\oldpage[0\\textsubscript{III}]{35} immediately before the (11.4.6.1) display", "marker", "high",
           r"""\oldpage[0\textsubscript{III}]{35}¶\[""", r"""\[""",
           note="Apply together with the page-34 marker finding (which inserts the marker before 'notée'). "
                "Outside pages 30-34: listed so the move is complete."))


def load(page):
    with open(os.path.join(RUN, "page_%03d.tex" % page), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
pages = {}
for d in L:
    if d["fix"] is None:
        continue
    t = pages.setdefault(d["page"], load(d["page"]))
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
        print("NOT UNIQUE (%d) p%d: %r" % (n, d["page"], d["fix"]["old"]))

# apply all fixes per page in forward and reverse order: every old must still be found exactly once
for order in ("forward", "reverse"):
    for p, t0 in pages.items():
        fx = [d["fix"] for d in L if d["page"] == p and d["fix"] is not None]
        if order == "reverse":
            fx = fx[::-1]
        t = t0
        for f in fx:
            if t.count(f["old"]) != 1:
                ok = False
                print("INTERFERENCE (%s) p%d: %r" % (order, p, f["old"]))
            t = t.replace(f["old"], f["new"], 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

counts = {}
for d in L:
    c = counts.setdefault(d["page"], [0, 0, 0])
    if d["kind"] == "convention":
        c[1] += 1
    elif d["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
sys.stdout.reconfigure(encoding="utf-8")
print("ok" if ok else "PROBLEMS", len(L), "findings")
for p in sorted(counts):
    print(p, "normal/convention/misprint = %d/%d/%d" % tuple(counts[p]))
