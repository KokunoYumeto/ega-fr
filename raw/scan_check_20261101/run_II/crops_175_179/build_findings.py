import json
import sys

BASE = r"user/Documents/ega_scan_check_20261101/run_II"
OUT = BASE + "/findings_175_179.json"
NL = "<NL>"


def s(x):
    """raw string with <NL> standing for a line break"""
    return None if x is None else x.replace(NL, "\n")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": None if old is None else {"old": s(old), "new": s(new)},
    }
    if kind == "misprint_in_print":
        d["corrected"] = s(corrected)
    d["note"] = note
    return d


BREAK_NOTE = ("Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES item 20): "
              "the blank line is the last line of this page's segment, just before {marker}; "
              "the source has no blank line after that marker, so this edit alone removes the break.")

L = []

# ---------------- page 175 ----------------
L.append(F(175, "heading of (8.7.4)",
           "Remarques (8.7.4). \u2014 (i) La fin du raisonnement ... (plural 'Remarques')",
           r"\begin{remark}[8.7.4] (the remark environment prints 'Remarque (8.7.4). ---')",
           "word", None, "high",
           r"\begin{remark}[8.7.4]", r"\begin{remarks}[8.7.4]",
           "The print has the plural heading; EGA_FR.tex has a 'remarks' environment that prints 'Remarques (#1). ---'. "
           "Apply together with the p. 176 edit \\end{remark} -> \\end{remarks} (otherwise LaTeX error)."))
L.append(F(175, "'... et si on pose S|U = S~, S|U' = S~', le diagramme'",
           "S\u0303' : the tilde covers only S (same width as in S\u0303 just before); the prime stands outside it",
           r"\widetilde{S'}",
           "convention", 8, "high",
           r"\widetilde{S'}", r"\widetilde{S}'",
           "Checked on a 3x crop."))
L.append(F(175, "page break 175/176: '... soit partout d\u00e9fini; on a d'autre part | un Y-morphisme v : C -> C''' (p. 176)",
           "the sentence runs on across the page break; p. 176 begins flush left with 'un Y-morphisme' (no indent)",
           r"blank line after 'd'autre part' before \oldpage[II]{176} makes a paragraph break",
           "other", None, "high",
           "d'autre part<NL><NL>", "d'autre part<NL>",
           BREAK_NOTE.format(marker=r"\oldpage[II]{176}")))

# ---------------- page 176 ----------------
L.append(F(176, "end of Remarques (8.7.4)",
           "heading 'Remarques (8.7.4)' (p. 175)",
           r"\end{remark}",
           "word", None, "high",
           r"\end{remark}", r"\end{remarks}",
           "Second half of the p. 175 edit \\begin{remark}[8.7.4] -> \\begin{remarks}[8.7.4]; apply both together."))
L.append(F(176, "(8.7.4)(i), text before (8.7.4.2): 'd'o\u00f9 (1.5.6) un morphisme w : C_X'' -> C_X'",
           "w : C_{X''} -> C_X  (the TeX keeps this printed reading)",
           r"$w:C_{X''}\to C_X$",
           "misprint_in_print", None, "medium",
           None, None,
           "The u-morphism S_{X''} -> S_X (u : X -> X'') gives by (1.5.6) Spec(u): Spec(S_X) -> Spec(S_{X''}), i.e. w : C_X -> C_{X''}; "
           "the printed arrow is reversed. The TeX keeps the printed reading (correct for the diplomatic edition). "
           "Goes with the misprint in diagram (8.7.4.2) (next item).",
           corrected=r"$w:C_X\to C_{X''}$"))
L.append(F(176, "diagram (8.7.4.2)",
           "top row C_{X''} (iso arrow) Proj(S^\u266e); bottom row C_X (iso arrow) Proj(S^\u266e); left arrow w, right arrow Proj(\u03c8) "
           "(top right has no double prime; checked on a 3x crop). The TeX keeps this printed reading.",
           r"C_{X''}\ar[r]^{\sim}\ar[d]_{w} & \operatorname{Proj}(\mathcal{S}^{\natural})\ar[d]^{\operatorname{Proj}(\psi)}\\ C_X\ar[r]^{\sim} & \operatorname{Proj}(\mathcal{S}^{\natural})",
           "misprint_in_print", None, "medium",
           None, None,
           "As printed the right column maps Proj(S^\u266e) to Proj(S^\u266e) by Proj(\u03c8), but \u03c8 : S''^\u266e -> S^\u266e, so Proj(\u03c8) : Proj(S^\u266e) -> Proj(S''^\u266e); "
           "and C_{X''} is isomorphic to Proj(S''^\u266e), not Proj(S^\u266e) (8.7.3.1). With w : C_X -> C_{X''} (previous item) the consistent diagram has "
           "C_X ~> Proj(S^\u266e) on top and C_{X''} ~> Proj(S''^\u266e) below. That the printed right column is wrong is certain; the full correction is a reconstruction.",
           corrected=r"\xymatrix{<NL>  C_X\ar[r]^{\sim}\ar[d]_{w} & \operatorname{Proj}(\mathcal{S}^{\natural})\ar[d]^{\operatorname{Proj}(\psi)}\\<NL>  C_{X''}\ar[r]^{\sim} & \operatorname{Proj}(\mathcal{S}''^{\natural})<NL>}"))
L.append(F(176, "(8.7.4)(ii): 'Si on pose T = (+)_{n>=0} J_m, qui est une O_C^-Alg\u00e8bre gradu\u00e9e'",
           "T = \u2295_{n\u2a7e0} J_m (summation index n, summand index m; checked on a 3x crop). The TeX keeps this printed reading.",
           r"\mathcal{T}=\bigoplus_{n\geqslant 0}\mathcal{J}_m",
           "misprint_in_print", None, "high",
           None, None,
           "Index mismatch in the print: the sum runs over the index of the Ideals J_m.",
           corrected=r"\mathcal{T}=\bigoplus_{m\geqslant 0}\mathcal{J}_m"))
L.append(F(176, "end of (8.7.4)(ii): 'cet isomorphisme et (8.7.3.1) co\u00efncident au-dessus de \u00ca.'",
           "au-dessus de \u00ca (E with a hat; checked on a 2x crop)",
           r"au-dessus de $E$.",
           "misprint_in_print", None, "high",
           "au-dessus de $E$.", r"au-dessus de $\widehat{E}$.",
           "The TeX silently corrects the print. (8.7.3.1) is defined over C only, so the two isomorphisms can be compared (and glued) only over "
           "C \u2229 \u00ca = E: the correct reading is E. The fix restores the printed \u00ca.",
           corrected="au-dessus de $E$."))
L.append(F(176, "Corollaire (8.7.5), last words: 'il existe n_0>0 tel que l'on ait (8.7.5.1).'",
           "reference (8.7.5.1) upright (roman parentheses and figures) inside the italic statement",
           r"(\hyperref[II.8.7.5.1-fr]{8.7.5.1}) italic in the corollary environment",
           "convention", 6, "high",
           r"(\hyperref[II.8.7.5.1-fr]{8.7.5.1})", r"\textup{(\hyperref[II.8.7.5.1-fr]{8.7.5.1})}",
           "Checked on a crop."))
L.append(F(176, "proof of (8.7.5): 'l'image r\u00e9ciproque de \u03b5(Y) dans C_X (I, 4.4.1)'",
           "(I, 4.4.1) with bold I",
           "(I, 4.4.1) with plain I in the link text",
           "convention", 2, "high",
           "{I, 4.4.1}", r"{\textbf{I}, 4.4.1}",
           ""))
L.append(F(176, "page break 176/177: '... lorsque Y est affine noeth\u00e9rien et S de type fini. | Si Y est noeth\u00e9rien (non n\u00e9cessairement affine)' (p. 177)",
           "p. 177 begins flush left with 'Si Y est noeth\u00e9rien' (no indent): same paragraph",
           r"blank line after 'type fini.' before \oldpage[II]{177} makes a paragraph break",
           "other", None, "high",
           "type fini.<NL><NL>", "type fini.<NL>",
           BREAK_NOTE.format(marker=r"\oldpage[II]{177}")))

# ---------------- page 177 ----------------
L.append(F(177, "(8.7.6), example: 'K \u00e9tant un corps, S = S~ avec S = K[y]'",
           "S = \U0001d4ae\u0303 : roman S on the left, tilde over script S on the right (checked on a 2x crop)",
           r"$\mathcal{S}=\widetilde{S}$",
           "misprint_in_print", None, "high",
           r"$\mathcal{S}=\widetilde{S}$", r"$S=\widetilde{\mathcal{S}}$",
           "The TeX silently corrects the print (the quasi-coherent algebra is S~ for S = K[y]). The fix restores the printed reading.",
           corrected=r"$\mathcal{S}=\widetilde{S}$"))
L.append(F(177, "(8.7.6): 'o\u00f9 y est une ind\u00e9termin\u00e9e de degr\u00e9 2;'",
           "only 'de degr\u00e9' italic; the figure 2 is upright (same glyph as the 2 of (2.3.14); checked on a 6x crop)",
           "\\emph{de degr\u00e9\\n2} (the 2 inside the emphasis)",
           "italics", None, "high",
           "\\emph{de degr\u00e9<NL>2}", "\\emph{de degr\u00e9}<NL>2",
           ""))
L.append(F(177, "(8.7.6): 'S_+^\u266e n'est pas la racine dans S_+^\u266e de l'id\u00e9al engendr\u00e9 par la r\u00e9union des R_n'",
           "racine dans S^\u266e_+ (with subscript +; checked on a crop)",
           r"racine dans $S^{\natural}$ (no +)",
           "formula", None, "high",
           "racine dans<NL>$S^{\\natural}$ de", "racine dans<NL>$S_+^{\\natural}$ de",
           "Not a misprint: the example negates (8.2.10, (iv)), which reads 'S_+^\u266e est la racine dans S_+^\u266e de l'id\u00e9al de S_+^\u266e engendr\u00e9 par ...'."))
L.append(F(177, "Corollaire (8.7.7): 'Alors le morphisme canonique (8.7.6.2) est partout d\u00e9fini'",
           "reference (8.7.6.2) upright inside the italic statement",
           r"(\hyperref[II.8.7.6.2-fr]{8.7.6.2}) italic in the corollary environment",
           "convention", 6, "high",
           r"(\hyperref[II.8.7.6.2-fr]{8.7.6.2})", r"\textup{(\hyperref[II.8.7.6.2-fr]{8.7.6.2})}",
           "Checked on a crop."))
L.append(F(177, "Corollaire (8.7.7), last words: 'il existe n_0 tel que l'on ait (8.7.7.1).'",
           "reference (8.7.7.1) upright inside the italic statement",
           r"(\hyperref[II.8.7.7.1-fr]{8.7.7.1}) italic in the corollary environment",
           "convention", 6, "high",
           "l'on ait<NL>(\\hyperref[II.8.7.7.1-fr]{8.7.7.1})", "l'on ait<NL>\\textup{(\\hyperref[II.8.7.7.1-fr]{8.7.7.1})}",
           "Checked on a crop. The two (8.7.7.1) of Remarque (8.7.8) are in roman text and need nothing."))
L.append(F(177, "(8.8.1): 'f : X -> Y un morphisme s\u00e9par\u00e9 et quasi-compact'",
           "'s\u00e9par\u00e9' and 'quasi-compact' italic, 'et' roman (checked on a 2.5x crop)",
           "\\emph{s\u00e9par\u00e9 et quasi-compact} ('et' italic)",
           "italics", None, "high",
           "\\emph{s\u00e9par\u00e9 et<NL>quasi-compact}", "\\emph{s\u00e9par\u00e9} et<NL>\\emph{quasi-compact}",
           ""))
L.append(F(177, "page break 177/178: '(8.8.1.1) S = O_Y (+) ... | qui est quasi-coh\u00e9rente (I, 9.2.2, a))' (p. 178)",
           "p. 178 begins flush left with 'qui est quasi-coh\u00e9rente' (no indent): the sentence continues after the display",
           r"blank line after \end{equation} of (8.8.1.1) before \oldpage[II]{178} makes a paragraph break",
           "other", None, "high",
           "\\tag{8.8.1.1}<NL>\\end{equation}<NL><NL>", "\\tag{8.8.1.1}<NL>\\end{equation}<NL>",
           BREAK_NOTE.format(marker=r"\oldpage[II]{178}")))

# ---------------- page 178 ----------------
L.append(F(178, "first line: 'qui est quasi-coh\u00e9rente (I, 9.2.2, a))'",
           "(I, 9.2.2, a)) with bold I",
           "plain I in the link text",
           "convention", 2, "high",
           "{I, 9.2.2", "{\\textbf{I}, 9.2.2",
           "Independent of the italic a) edit at the same reference (either order works)."))
L.append(F(178, "first line: 'qui est quasi-coh\u00e9rente (I, 9.2.2, a))'",
           "letter a and its parenthesis italic (checked on a 6x crop)",
           "a) upright in the link text",
           "italics", None, "high",
           "9.2.2, a)}", "9.2.2, \\emph{a)}}",
           "Independent of the bold-I edit at the same reference (either order works)."))
L.append(F(178, "after (8.8.1.2): 'l'homomorphisme canonique \u03c3 : ... (0, 4.4.3)'",
           "(0, 4.4.3) with bold 0",
           "plain 0 in the link text",
           "convention", 2, "high",
           "{0, 4.4.3}", "{\\textbf{0}, 4.4.3}",
           ""))
L.append(F(178, "Proposition (8.8.2): 'Soit C = Spec(S) le c\u00f4ne affine d\u00e9fini par S;'",
           "'le c\u00f4ne affine d\u00e9fini par S' in the same italic as the rest of the statement (no change of face; checked on a crop)",
           "\\emph{le c\u00f4ne affine d\u00e9fini par $\\mathcal{S}$} inside the \\itshape proposition environment (comes out upright)",
           "convention", 6, "high",
           "\\emph{le c\u00f4ne affine d\u00e9fini par<NL>$\\mathcal{S}$}", "le c\u00f4ne affine d\u00e9fini par<NL>$\\mathcal{S}$",
           "Printed italic words left upright by \\emph inside the italic environment; drop the \\emph."))
L.append(F(178, "Proposition (8.8.2): 'la restriction de g \u00e0 V(L)\u2014j(X) est une immersion ouverte'",
           "long dash V(L)\u2014j(X)",
           "minus sign",
           "convention", 7, "high",
           "\\mathbf{V}(\\mathcal{L})-j(X)$ est une", "\\mathbf{V}(\\mathcal{L})\\setmin j(X)$ est une",
           "\\setmin is not yet the long dash (global change pending)."))
L.append(F(178, "(8.8.2.3), left side: 'V(L)\u2014j(X) -> E'",
           "long dash V(L)\u2014j(X)",
           "minus sign",
           "convention", 7, "high",
           "\\mathbf{V}(\\mathcal{L})-j(X)\\longrightarrow", "\\mathbf{V}(\\mathcal{L})\\setmin j(X)\\longrightarrow",
           "As above."))
L.append(F(178, "(8.8.2.3), right side: 'E = C\u2014\u03b5(Y)'",
           "long dash C\u2014\u03b5(Y) (checked on a 2.5x crop)",
           "minus sign",
           "convention", 7, "high",
           "E=C-\\varepsilon(Y)", "E=C\\setmin\\varepsilon(Y)",
           "As above."))
L.append(F(178, "page break 178/179: 'r^*(S_P^>=) = S_{O_X}(L) | et par suite on a un P-morphisme canonique' (p. 179)",
           "p. 179 begins flush left with 'et par suite' (no indent): the sentence continues after the display",
           r"blank line after \] before \oldpage[II]{179} makes a paragraph break",
           "other", None, "high",
           "\\mathbf{S}_{\\mathcal{O}_X}(\\mathcal{L})<NL>\\]<NL><NL>", "\\mathbf{S}_{\\mathcal{O}_X}(\\mathcal{L})<NL>\\]<NL>",
           BREAK_NOTE.format(marker=r"\oldpage[II]{179}")))

# ---------------- page 179 ----------------
L.append(F(179, "after (8.8.2.6): 'il en est donc de m\u00eame de q (I, 4.3.2)'",
           "(I, 4.3.2) with bold I",
           "plain I in the link text",
           "convention", 2, "high",
           "{I, 4.3.2}", "{\\textbf{I}, 4.3.2}",
           ""))
L.append(F(179, "'la restriction de q \u00e0 V(L)\u2014j(X) applique ce pr\u00e9sch\u00e9ma dans E_P'",
           "long dash V(L)\u2014j(X)",
           "minus sign",
           "convention", 7, "high",
           "\\mathbf{V}(\\mathcal{L})-j(X)$ applique", "\\mathbf{V}(\\mathcal{L})\\setmin j(X)$ applique",
           "\\setmin is not yet the long dash (global change pending)."))
L.append(F(179, "Remarque (8.8.3): 'On verra en outre au chapitre III (III, 2.3.5.1), que S est alors'",
           "(III, 2.3.5.1) with bold III",
           "plain III in the link text",
           "convention", 2, "high",
           "{III, 2.3.5.1}), que $\\mathcal{S}$", "{\\textbf{III}, 2.3.5.1}), que $\\mathcal{S}$",
           "The 'III' of 'au chapitre III' is plain in the print and stays."))
L.append(F(179, "Remarque (8.8.3): 'la restriction (8.8.2.3) de g est un isomorphisme V(L)\u2014j(X) ~> E'",
           "long dash V(L)\u2014j(X)",
           "minus sign",
           "convention", 7, "high",
           "\\mathbf{V}(\\mathcal{L})-j(X)\\xrightarrow{\\sim}E", "\\mathbf{V}(\\mathcal{L})\\setmin j(X)\\xrightarrow{\\sim}E",
           "As above."))
L.append(F(179, "Remarque (8.8.3), second paragraph: 'Si on suppose de plus que L est tr\u00e8s ample pour f'",
           "plain roman L (not the script L; checked on a 2x crop)",
           r"$\mathcal{L}$",
           "misprint_in_print", None, "high",
           "que $\\mathcal{L}$ est \\emph{tr\u00e8s ample}", "que $L$ est \\emph{tr\u00e8s ample}",
           "The TeX silently corrects the print; the invertible sheaf is script L throughout. The fix restores the printed roman L.",
           corrected="que $\\mathcal{L}$ est \\emph{tr\u00e8s ample}"))
L.append(F(179, "Remarque (8.8.3), second paragraph: 'on verra aussi au chapitre III (III, 2.3.5.1), qu'il existe'",
           "(III, 2.3.5.1) with bold III",
           "plain III in the link text",
           "convention", 2, "high",
           "{III, 2.3.5.1}), qu'il", "{\\textbf{III}, 2.3.5.1}), qu'il",
           ""))
L.append(F(179, "Remarque (8.8.3): 'et que la section nulle de V(L) (identifi\u00e9e \u00e0 Y) est l'image r\u00e9ciproque'",
           "(identifi\u00e9e \u00e0 Y)  (the TeX keeps this printed reading)",
           "(identifi\u00e9e \u00e0 $Y$)",
           "misprint_in_print", None, "medium",
           None, None,
           "The zero section of V(L) (a vector bundle over X) is identified with X, not Y (compare Remarque (8.7.8): 'le sommet (identifi\u00e9 \u00e0 X) de C_X'); "
           "Y is the vertex subscheme of C. The TeX keeps the printed reading.",
           corrected="(identifi\u00e9e \u00e0 $X$)"))
L.append(F(179, "Remarque (8.8.3): 'est l'image r\u00e9ciproque du sous-pr\u00e9sch\u00e9ma des sommets'",
           "\"l'\" roman, only 'image r\u00e9ciproque' italic (checked on a 2.5x crop)",
           "\\emph{l'image r\u00e9ciproque} (the article inside the emphasis)",
           "italics", None, "high",
           "\\emph{l'image r\u00e9ciproque}", "l'\\emph{image r\u00e9ciproque}",
           "Judged with the remark body as roman (document-wide remark item)."))
L.append(F(179, "end of Remarque (8.8.3): '... du sous-pr\u00e9sch\u00e9ma des sommets Y de C. | Une partie des r\u00e9sultats pr\u00e9c\u00e9dents peut en fait s'\u00e9tablir sans hypoth\u00e8se noeth\u00e9rienne :'",
           "'Une partie des r\u00e9sultats pr\u00e9c\u00e9dents ...' begins a new, indented paragraph (the previous line ends short)",
           "same paragraph as '... sommets $Y$ de $C$.'",
           "other", None, "high",
           "$Y$ de $C$. Une partie", "$Y$ de $C$.<NL><NL>Une partie",
           "Missing paragraph break."))
L.append(F(179, "Corollaire (8.8.4): 'Soient Y un pr\u00e9sch\u00e9ma (resp. un sch\u00e9ma quasi-compact)'",
           "'(resp.' and the closing parenthesis roman, 'un sch\u00e9ma quasi-compact' italic (checked on a crop)",
           "all italic in the corollary environment",
           "convention", 6, "high",
           "(resp. un sch\u00e9ma quasi-compact)", "\\textup{(resp.} un sch\u00e9ma quasi-compact\\textup{)}",
           ""))
L.append(F(179, "Corollaire (8.8.4): 'Alors le morphisme (8.8.2.1) est propre'",
           "reference (8.8.2.1) upright inside the italic statement",
           "italic in the corollary environment",
           "convention", 6, "high",
           "(\\hyperref[II.8.8.2.1-fr]{8.8.2.1})", "\\textup{(\\hyperref[II.8.8.2.1-fr]{8.8.2.1})}",
           ""))
L.append(F(179, "Corollaire (8.8.4): 'est propre (resp. projectif)'",
           "'(resp.' and the closing parenthesis roman, 'projectif' italic",
           "all italic in the corollary environment",
           "convention", 6, "high",
           "(resp.<NL>projectif)", "\\textup{(resp.}<NL>projectif\\textup{)}",
           ""))
L.append(F(179, "Corollaire (8.8.4): 'et sa restriction (8.8.2.3) est un isomorphisme'",
           "reference (8.8.2.3) upright inside the italic statement",
           "italic in the corollary environment",
           "convention", 6, "high",
           "sa restriction (\\hyperref[II.8.8.2.3-fr]{8.8.2.3})", "sa restriction \\textup{(\\hyperref[II.8.8.2.3-fr]{8.8.2.3})}",
           "The other two (8.8.2.3) on this page are in roman text."))
L.append(F(179, "page break 179/180: 'on peut appliquer (3.8.5) \u00e0 l'homo- | morphisme \u03c4 de (8.8.1.2)' (p. 180)",
           "the word and the sentence run on across the page break",
           r"blank line after 'l'homomorphisme' before \oldpage[II]{180} makes a paragraph break",
           "other", None, "high",
           "\u00e0 l'homomorphisme<NL><NL>", "\u00e0 l'homomorphisme<NL>",
           BREAK_NOTE.format(marker=r"\oldpage[II]{180}")
           + " The marker follows the whole word 'l'homomorphisme' (print: 'l'homo-|morphisme'); left as is."))

# ---------------- check and write ----------------
texts = {}
for p in (175, 176, 177, 178, 179):
    with open(f"{BASE}/page_{p}.tex", encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")

bad = 0
for d in L:
    f = d["fix"]
    if f is None:
        continue
    n = texts[d["page"]].count(f["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", d["page"], n, repr(f["old"]))
    if f["old"] == f["new"]:
        bad += 1
        print("NO-OP", d["page"], repr(f["old"]))

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for d in L:
    k = "misprint" if d["kind"] == "misprint_in_print" else ("convention" if d["kind"] == "convention" else "normal")
    c[(d["page"], k)] += 1
for p in (175, 176, 177, 178, 179):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("findings", len(L), "bad", bad)
sys.exit(1 if bad else 0)
