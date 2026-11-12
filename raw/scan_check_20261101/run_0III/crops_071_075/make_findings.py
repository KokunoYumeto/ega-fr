"""Build findings_071_075.json for pages 71-75 of EGA III ch. 0 (ega3-1-fr.tex).

Strings use <NL> for a line break; it is replaced by "\n" before writing.
"""
import json
import os
import sys

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_071_075.json')

C_NOTE = ("Category letter C printed bold italic (edition point for this file; GLOBAL_ISSUES item 33); "
          "the TeX has a plain italic C. \\boldsymbol as in the earlier ega3-1 page fixes.")
W_NOTE = ("The statement environment is \\itshape, so the \\emph wrapper around the statement text sets it UPRIGHT; "
          "the print has it italic. ")


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind,
         "convention": conv, "confidence": conf}
    if old is None:
        d["fix"] = None
    else:
        d["fix"] = {"old": old.replace('<NL>', '\n'), "new": new.replace('<NL>', '\n')}
    if corrected is not None:
        d["corrected"] = corrected.replace('<NL>', '\n')
    d["note"] = note
    return d


def Cfix(page, where, old, new, prime=False):
    return F(page, where, "bold italic C'" if prime else "bold italic C",
             "plain $C'$" if prime else "plain $C$", "font", None, "high", old, new, C_NOTE)


L = []

# ---------------------------------------------------------------- page 71
L.append(Cfix(71, "(13.4.4): 'Supposons que dans C la limite projective'",
              r"dans $C$ la limite", r"dans $\boldsymbol{C}$ la limite"))
L.append(F(71, "(13.4.4): 'la limite projective A = lim A_k existe'",
           "lim with the arrow below and no index: A = lim← A_k",
           r"$A=\varprojlim_k A_k$ (index k under lim)", "formula", None, "high",
           r"$A=\varprojlim_k A_k$ existe", r"$A=\varprojlim A_k$ existe",
           "Enlarged crop: no k under the arrow (the lim in Corollaire (13.4.5) two lines later does carry k)."))
L.append(F(71, "Corollaire (13.4.5): start of the statement '\\emph{Supposons que C soit ...'",
           "statement italic", "whole statement wrapped in \\emph{...} inside the italic corollary environment (comes out upright)",
           "convention", 6, "high",
           r"\label{0.13.4.5-fr}<NL>\emph{Supposons", r"\label{0.13.4.5-fr}<NL>Supposons",
           W_NOTE + "Opening half: apply together with the closing edit 'isomorphisme<NL>canonique}' below."))
L.append(Cfix(71, "Corollaire (13.4.5): 'Supposons que C soit la catégorie des groupes abéliens'",
              r"que $C$ soit la", r"que $\boldsymbol{C}$ soit la"))
L.append(F(71, "Corollaire (13.4.5): 'Si le système projectif A vérifie (ML) et si'",
           "(ML) upright inside the italic statement", "(ML) inside the \\emph wrapper (italic once the wrapper goes)",
           "convention", 6, "high",
           r"vérifie (ML) et si", r"vérifie \textup{(ML)} et si",
           "Enlarged crop: (ML) is roman. Harmless before the wrapper is removed, needed after."))
L.append(F(71, "Corollaire (13.4.5): end of the statement '... un isomorphisme canonique}'",
           "statement italic", "closing brace of the \\emph wrapper",
           "convention", 6, "high",
           r"isomorphisme<NL>canonique}", r"isomorphisme<NL>canonique",
           W_NOTE + "Closing half: apply together with the opening edit '\\label{0.13.4.5-fr}<NL>\\emph{Supposons'."))
L.append(Cfix(71, "(13.5.1): 'Soient C une catégorie abélienne'",
              r"Soient $C$ une", r"Soient $\boldsymbol{C}$ une"))
L.append(Cfix(71, "(13.5.1): 'un complexe d'objets de C muni d'une filtration'",
              r"de<NL>$C$ muni", r"de<NL>$\boldsymbol{C}$ muni"))
L.append(Cfix(71, "(13.5.1): 'système projectif de complexes filtrés d'objets de C'",
              r"d'objets de $C$}", r"d'objets de $\boldsymbol{C}$}"))
L.append(Cfix(71, "(13.5.2): 'de complexes d'objets de C, limité inférieurement'",
              r"$C$, \emph{limité", r"$\boldsymbol{C}$, \emph{limité"))
L.append(Cfix(71, "(13.5.2): 'la catégorie abélienne des complexes de C limités inférieurement'",
              r"complexes de $C$ limités", r"complexes de $\boldsymbol{C}$ limités"))
L.append(F(71, "Lemme (13.5.3): 'Supposons que le système projectif ... soit obtenu comme dans (13.5.2). Alors :'",
           "statement italic; the reference (13.5.2) roman",
           "whole sentence wrapped in \\emph{...} inside the italic lemma environment (comes out upright)",
           "convention", 6, "high",
           r"\emph{Supposons que le système projectif<NL>$\mathbf X^\bullet=(X_k^\bullet)_{k\in\mathbb Z}$ de complexes filtrés soit<NL>obtenu comme dans (\hyperref[0.13.5.2-fr]{13.5.2}). Alors :}",
           r"Supposons que le système projectif<NL>$\mathbf X^\bullet=(X_k^\bullet)_{k\in\mathbb Z}$ de complexes filtrés soit<NL>obtenu comme dans \textup{(\hyperref[0.13.5.2-fr]{13.5.2})}. Alors :",
           W_NOTE + "Self-contained edit: drops the wrapper and keeps the roman reference (enlarged crop) upright."))
L.append(F(71, "Lemme (13.5.3) a): 'Pour r ⩾ p—p_0, on a B_r^pq(X_k) = B_∞^pq(X_k) pour tout k ∈ Z.'",
           "item text italic (label a) upright)",
           "item text wrapped in \\emph{...} inside the italic lemma (comes out upright)",
           "convention", 6, "high",
           r"\emph{Pour $r\geq p-p_0$, on a<NL>$\mathrm B_r^{pq}(X_k^\bullet)=\mathrm B_\infty^{pq}(X_k^\bullet)$ pour<NL>tout $k\in\mathbb Z$.}",
           r"Pour $r\geq p-p_0$, on a<NL>$\mathrm B_r^{pq}(X_k^\bullet)=\mathrm B_\infty^{pq}(X_k^\bullet)$ pour<NL>tout $k\in\mathbb Z$.",
           W_NOTE + "The label \\item[\\emph{a)}] already comes out upright, as printed; leave it."))
L.append(F(71, "Lemme (13.5.3) b): 'Pour k+1 ⩽ p+r, on a Z_r^pq(X_k) = Z_∞^pq(X_k).'",
           "item text italic", "item text wrapped in \\emph{...} (comes out upright)",
           "convention", 6, "high",
           r"\emph{Pour $k+1\leq p+r$, on a<NL>$\mathrm Z_r^{pq}(X_k^\bullet)=\mathrm Z_\infty^{pq}(X_k^\bullet)$.}",
           r"Pour $k+1\leq p+r$, on a<NL>$\mathrm Z_r^{pq}(X_k^\bullet)=\mathrm Z_\infty^{pq}(X_k^\bullet)$.",
           W_NOTE))
L.append(F(71, "Lemme (13.5.3) c): 'Pour k+1 ⩾ p+r, les morphismes ... sont des isomorphismes pour tout h ⩾ k.'",
           "item text italic", "item text wrapped in \\emph{...} (comes out upright)",
           "convention", 6, "high",
           r"\emph{Pour $k+1\geq p+r$, les morphismes<NL>$\mathrm Z_r^{pq}(X_h^\bullet)\to\mathrm Z_r^{pq}(X_k^\bullet)$ et<NL>$\mathrm B_r^{pq}(X_h^\bullet)\to\mathrm B_r^{pq}(X_k^\bullet)$ sont des<NL>isomorphismes pour tout $h\geq k$.}",
           r"Pour $k+1\geq p+r$, les morphismes<NL>$\mathrm Z_r^{pq}(X_h^\bullet)\to\mathrm Z_r^{pq}(X_k^\bullet)$ et<NL>$\mathrm B_r^{pq}(X_h^\bullet)\to\mathrm B_r^{pq}(X_k^\bullet)$ sont des<NL>isomorphismes pour tout $h\geq k$.",
           W_NOTE))

# ---------------------------------------------------------------- page 72
L.append(F(72, "(13.5.4): 'les systèmes projectifs (Z_r^pq(X_k))_{k∈Z}, (B_r^pq(X_k))_{k∈Z}, (E_r^pq(X_k))_{k∈Z} sont essentiellement constants'",
           "the three systems set inline in the running text, separated by commas",
           "set as a display \\[ ... \\] with \\quad separators", "other", None, "high",
           r"systèmes projectifs<NL>\[<NL>(\mathrm Z_r^{pq}(X_k^\bullet))_{k\in\mathbb Z},\quad<NL>(\mathrm B_r^{pq}(X_k^\bullet))_{k\in\mathbb Z},\quad<NL>(\mathrm E_r^{pq}(X_k^\bullet))_{k\in\mathbb Z}<NL>\]<NL>sont",
           r"systèmes projectifs<NL>$(\mathrm Z_r^{pq}(X_k^\bullet))_{k\in\mathbb Z}$,<NL>$(\mathrm B_r^{pq}(X_k^\bullet))_{k\in\mathbb Z}$,<NL>$(\mathrm E_r^{pq}(X_k^\bullet))_{k\in\mathbb Z}$<NL>sont",
           "Displayed formula the print sets inline (as GLOBAL_ISSUES item 21)."))
L.append(F(72, "Lemme (13.5.5): 'Sous les hypothèses de (13.5.3), on a, pour s ⩾ r > p—p_0, un monomorphisme canonique'",
           "italic statement; reference (13.5.3) roman",
           "\\emph{...} wrapper inside the italic lemma (comes out upright)",
           "convention", 6, "high",
           r"\emph{Sous les hypothèses de<NL>(\hyperref[0.13.5.3-fr]{13.5.3}), on a, pour $s\geq r>p-p_0$, un<NL>monomorphisme canonique}",
           r"Sous les hypothèses de<NL>\textup{(\hyperref[0.13.5.3-fr]{13.5.3})}, on a, pour $s\geq r>p-p_0$, un<NL>monomorphisme canonique",
           W_NOTE + "Self-contained; the reference is roman in the enlarged crop."))
L.append(F(72, "Lemme (13.5.5): 'et un isomorphisme canonique'",
           "italic", "\\emph{...} inside the italic lemma (comes out upright)",
           "convention", 6, "high",
           r"\emph{et un isomorphisme canonique}", r"et un isomorphisme canonique", W_NOTE))
L.append(F(72, "Lemme (13.5.5): 'tels que le diagramme'",
           "italic", "\\emph{...} inside the italic lemma (comes out upright)",
           "convention", 6, "high",
           r"\emph{tels que le diagramme}", r"tels que le diagramme", W_NOTE))
L.append(F(72, "diagram (13.5.5.3), label of the top arrow",
           "label printed 'js': the s on the baseline at the size of j, no subscript",
           "j_s", "misprint_in_print", None, "medium",
           r"\ar[r]^{j_s}", r"\ar[r]^{js}",
           "6x crop: s is not lowered or reduced (j_r in display (13.5.5.2) has a real subscript). The TeX silently corrects; the fix restores the printed reading.",
           corrected=r"\ar[r]^{j_s}"))
L.append(F(72, "diagram (13.5.5.3), bottom arrow: position of its label",
           "label below the arrow", "\\ar[r]^{j_r} (label above)", "other", None, "high",
           r"\mathrm E_r^{pq}(\mathbf X^\bullet)\ar[r]^", r"\mathrm E_r^{pq}(\mathbf X^\bullet)\ar[r]_",
           "Enlarged crop: the top label j_s is above its arrow, the bottom label below. Does not overlap the next finding (adjacent strings)."))
L.append(F(72, "diagram (13.5.5.3), label of the bottom arrow",
           "label printed 'jr': the r on the baseline at the size of j, no subscript",
           "j_r", "misprint_in_print", None, "medium",
           r"{j_r}<NL>&", r"{jr}<NL>&",
           "6x crop, as for the top label. The TeX silently corrects; the fix restores the printed reading.",
           corrected=r"{j_r}<NL>&"))
L.append(F(72, "Lemme (13.5.5): 'soit commutatif'",
           "italic", "\\emph{soit commutatif} inside the italic lemma (comes out upright)",
           "convention", 6, "high",
           r"\emph{soit commutatif}", r"soit commutatif", W_NOTE))
L.append(F(72, "Lemme (13.5.5): '(la flèche verticale de droite provenant du morphisme X_{p+s-1} → X_{p+r-1}).'",
           "parenthesis roman", "outside \\emph, so italic in the italic lemma environment",
           "convention", 6, "high",
           r"(la flèche verticale de droite provenant du<NL>morphisme $X_{p+s-1}^\bullet\to X_{p+r-1}^\bullet$)",
           r"\textup{(la flèche verticale de droite provenant du<NL>morphisme $X_{p+s-1}^\bullet\to X_{p+r-1}^\bullet$)}",
           "Enlarged crop: everything after 'soit commutatif' is roman. Visible now, independent of the wrapper edits."))
L.append(F(72, "proof of (13.5.5): 'pour r > p—p_0 (13.5.3, a));'",
           "(13.5.3, a)) with italic a) and two closing parentheses",
           "(13.5.3, a)~; (one parenthesis, roman a)", "punctuation", None, "high",
           r"{13.5.3}, a)~;", r"{13.5.3}, \emph{a)})~;",
           "Enlarged crop: italic 'a)' then the roman ')' closing the reference. The fix also sets a) italic."))
L.append(F(72, "proof of (13.5.5): 'pour k+1 ⩽ p+r (13.5.3, b)), d'où en particulier'",
           "(13.5.3, b)) with italic b) and two closing parentheses",
           "(13.5.3, b), (one parenthesis, roman b)", "punctuation", None, "high",
           r"{13.5.3}, b),", r"{13.5.3}, \emph{b)}),",
           "Enlarged crop. The fix also sets b) italic."))
L.append(F(72, "proof of (13.5.5): 'en vertu de (13.5.3, c)), d'où l'existence de j_r'",
           "italic c)", "roman c)", "italics", None, "high",
           r"{13.5.3}, c))", r"{13.5.3}, \emph{c)})",
           "Enlarged crop; the two parentheses are already there."))
L.append(F(72, "proof of (13.5.5), last line: 'd'où l'existence de j_r et la commutativité de (13.5.5.1).'",
           "(13.5.5.1)", "(13.5.5.1) (keeps the print)", "misprint_in_print", None, "medium",
           None, None,
           "The commutative diagram is (13.5.5.3); (13.5.5.1) is the monomorphism i, whose existence the proof settles in its first sentence. The TeX keeps the printed reading.",
           corrected=r"(\hyperref[0.13.5.5.3-fr]{13.5.5.3})"))
L.append(F(72, "Corollaire (13.5.6), first sentence: 'Sous les hypothèses de (13.5.3), si l'une des limites projectives ... un isomorphisme canonique'",
           "italic statement; reference (13.5.3) roman",
           "\\emph{...} wrapper inside the italic corollary (comes out upright)",
           "convention", 6, "high",
           r"\emph{Sous les hypothèses de<NL>(\hyperref[0.13.5.3-fr]{13.5.3}), si l'une des limites projectives<NL>$\varprojlim_r\mathrm E_r^{pq}(\mathbf X^\bullet)$,<NL>$\varprojlim_k\mathrm E_\infty^{pq}(X_k^\bullet)$ existe, il en est de<NL>même de l'autre, et on a un isomorphisme canonique}",
           r"Sous les hypothèses de<NL>\textup{(\hyperref[0.13.5.3-fr]{13.5.3})}, si l'une des limites projectives<NL>$\varprojlim_r\mathrm E_r^{pq}(\mathbf X^\bullet)$,<NL>$\varprojlim_k\mathrm E_\infty^{pq}(X_k^\bullet)$ existe, il en est de<NL>même de l'autre, et on a un isomorphisme canonique",
           W_NOTE + "Self-contained."))
L.append(F(72, "Corollaire (13.5.6): paragraph break before 'En outre, pour que le système projectif'",
           "'En outre' begins a new indented paragraph after display (13.5.6.1)",
           "no blank line after \\end{equation}: the text runs on unindented", "other", None, "high",
           r"(X_k^\bullet).<NL>\end{equation}<NL>", r"(X_k^\bullet).<NL>\end{equation}<NL><NL>",
           "Indent of 'En outre' matches the paragraph indent of 'Corollaire' and 'L'existence'. Adjacent to, not overlapping, the next edit."))
L.append(F(72, "Corollaire (13.5.6), second sentence: 'En outre, pour que ... soit essentiellement constant (13.4.2), il faut et il suffit ... le soit.'",
           "italic; reference (13.4.2) roman",
           "\\emph{...} wrapper inside the italic corollary (comes out upright)",
           "convention", 6, "high",
           r"\emph{En outre, pour que le système projectif<NL>$(\mathrm E_r^{pq}(\mathbf X^\bullet))_{r\in\mathbb Z}$ soit<NL>essentiellement constant<NL>(\hyperref[0.13.4.2-fr]{13.4.2}), il faut et il suffit que le système<NL>projectif $(\mathrm E_\infty^{pq}(X_k^\bullet))_{k\in\mathbb Z}$ le soit.}",
           r"En outre, pour que le système projectif<NL>$(\mathrm E_r^{pq}(\mathbf X^\bullet))_{r\in\mathbb Z}$ soit<NL>essentiellement constant<NL>\textup{(\hyperref[0.13.4.2-fr]{13.4.2})}, il faut et il suffit que le système<NL>projectif $(\mathrm E_\infty^{pq}(X_k^\bullet))_{k\in\mathbb Z}$ le soit.",
           W_NOTE + "Self-contained."))

# ---------------------------------------------------------------- page 73
L.append(Cfix(73, "(13.6.1): 'Soient C, C' deux catégories abéliennes' (first letter)",
              r"Soient $C$,", r"Soient $\boldsymbol{C}$,"))
L.append(Cfix(73, "(13.6.1): 'Soient C, C' deux catégories abéliennes' (C')",
              r"$C'$ deux catégories", r"$\boldsymbol{C}'$ deux catégories", prime=True))
L.append(Cfix(73, "(13.6.1): 'T : C → C'' (source)",
              r"T:C\to", r"T:\boldsymbol{C}\to"))
L.append(Cfix(73, "(13.6.1): 'T : C → C'' (target)",
              r"C'$ un<NL>foncteur", r"\boldsymbol{C}'$ un<NL>foncteur", prime=True))
L.append(Cfix(73, "(13.6.1): 'Supposons que tout objet de C soit isomorphe'",
              r"objet de $C$ soit isomorphe", r"objet de $\boldsymbol{C}$ soit isomorphe"))
L.append(F(73, "Lemme (13.6.2): start of the statement '\\emph{Soit A ...'",
           "statement italic", "whole statement wrapped in \\emph{...} inside the italic lemma (comes out upright)",
           "convention", 6, "high",
           r"\label{0.13.6.2-fr}<NL>\emph{Soit $A$", r"\label{0.13.6.2-fr}<NL>Soit $A$",
           W_NOTE + "Opening half: apply together with the closing edit 'injective de $\\mathrm F^i(A)$.}'."))
L.append(Cfix(73, "Lemme (13.6.2): 'Soit A un objet de C, muni d'une filtration'",
              r"un objet de $C$, muni", r"un objet de $\boldsymbol{C}$, muni"))
L.append(F(73, "Lemme (13.6.2), 1st line: 'muni d'une filtration finie (F^i(A))_{i∈Z}'",
           "'finie' roman (emphasis inside the italic statement); 'filtration' italic",
           "finie inside the \\emph wrapper (italic once the wrapper goes)", "convention", 6, "high",
           r"filtration finie<NL>$(\mathrm F^i(A))", r"filtration \textup{finie}<NL>$(\mathrm F^i(A))",
           "Enlarged crop. The second 'filtration finie' of the statement and the one in (13.6.3) are italic."))
L.append(F(73, "Lemme (13.6.2): 'la relation F^i(A)=A (resp. F^i(A)=0) entraîne'",
           "'(resp.' and the parentheses roman", "inside the \\emph wrapper (italic once the wrapper goes)",
           "convention", 6, "high",
           r"(resp. $\mathrm F^i(A)=0$)", r"\textup{(resp. $\mathrm F^i(A)=0$)}",
           "Enlarged crop."))
L.append(F(73, "Lemme (13.6.2): 'entraîne F^i(X)=X (resp. F^i(X)=0) et que'",
           "'(resp.' and the parentheses roman", "inside the \\emph wrapper (italic once the wrapper goes)",
           "convention", 6, "high",
           r"(resp. $\mathrm F^i(X^\bullet)=0$)", r"\textup{(resp. $\mathrm F^i(X^\bullet)=0$)}",
           "Enlarged crop."))
L.append(F(73, "Lemme (13.6.2): end of the statement '... résolution injective de F^i(A).}'",
           "statement italic", "closing brace of the \\emph wrapper", "convention", 6, "high",
           r"injective de $\mathrm F^i(A)$.}", r"injective de $\mathrm F^i(A)$.",
           W_NOTE + "Closing half: apply together with '\\label{0.13.6.2-fr}<NL>\\emph{Soit $A$'."))
L.append(F(73, "proof of (13.6.2): 'Soit p (resp. q>p) le plus grand indice tel que F^i(A)=A'",
           "F^i(A)=A (superscript i, the running index)", "$\\mathrm F^p(A)=A$", "formula", None, "high",
           r"tel que<NL>$\mathrm F^p(A)=A$", r"tel que<NL>$\mathrm F^i(A)=A$",
           "Enlarged crop: superscript i (p = the largest index i with F^i(A)=A). A correct printed reading, not a misprint."))
L.append(F(73, "proof of (13.6.2): '(resp. le plus petit indice pour lequel F^i(A)=0)'",
           "F^i(A)=0", "$\\mathrm F^q(A)=0$", "formula", None, "high",
           r"lequel<NL>$\mathrm F^q(A)=0$", r"lequel<NL>$\mathrm F^i(A)=0$",
           "Enlarged crop: superscript i."))
L.append(F(73, "proof of (13.6.2): 'on considère la suite exacte 0→F^{q-1}(A)→A→A/F^{q-1}(A)→0, on prend'",
           "exact sequence inline in the running text", "display \\[ ... \\]", "other", None, "high",
           r"la suite exacte<NL>\[<NL>0\to\mathrm F^{q-1}(A)\to A\to A/\mathrm F^{q-1}(A)\to0,<NL>\]<NL>on prend",
           r"la suite exacte<NL>$0\to\mathrm F^{q-1}(A)\to A\to A/\mathrm F^{q-1}(A)\to0$,<NL>on prend",
           "Displayed formula the print sets inline (GLOBAL_ISSUES item 21)."))
L.append(F(73, "proof of (13.6.2): 'une suite exacte 0→X'→X→X''→0 compatible avec la précédente'",
           "exact sequence inline in the running text", "display \\[ ... \\]", "other", None, "high",
           r"une suite exacte<NL>\[<NL>0\to {X'}^\bullet\to X^\bullet\to {X''}^\bullet\to0<NL>\]<NL>compatible",
           r"une suite exacte<NL>$0\to {X'}^\bullet\to X^\bullet\to {X''}^\bullet\to0$<NL>compatible",
           "Displayed formula the print sets inline."))
L.append(F(73, "Corollaire (13.6.3): start of the statement '\\emph{Soit B ...'",
           "statement italic", "whole statement wrapped in \\emph{...} inside the italic corollary (comes out upright)",
           "convention", 6, "high",
           r"\label{0.13.6.3-fr}<NL>\emph{Soit $B$", r"\label{0.13.6.3-fr}<NL>Soit $B$",
           W_NOTE + "Opening half: apply together with the closing edit 'sont<NL>homotopes.}'."))
L.append(Cfix(73, "Corollaire (13.6.3): 'Soit B un second objet de C, muni'",
              r"second objet de $C$, muni", r"second objet de $\boldsymbol{C}$, muni"))
L.append(F(73, "Corollaire (13.6.3): 'ayant les propriétés énoncées en (13.6.2), il existe'",
           "reference (13.6.2) roman", "inside the \\emph wrapper (italic once the wrapper goes)",
           "convention", 6, "high",
           r"en (\hyperref[0.13.6.2-fr]{13.6.2}), il existe", r"en \textup{(\hyperref[0.13.6.2-fr]{13.6.2})}, il existe",
           "Enlarged crop."))
L.append(F(73, "Corollaire (13.6.3): end of the statement 'deux tels morphismes v, v' sont homotopes.}'",
           "statement italic", "closing brace of the \\emph wrapper", "convention", 6, "high",
           r"sont<NL>homotopes.}", r"sont<NL>homotopes.",
           W_NOTE + "Closing half: apply together with '\\label{0.13.6.3-fr}<NL>\\emph{Soit $B$'."))
L.append(Cfix(73, "(13.6.4): 'le complexe T(X) dans C', qui est'",
              r"dans $C'$, qui est", r"dans $\boldsymbol{C}'$, qui est", prime=True))
L.append(F(73, "(13.6.4), last line: 'que la filtration de l'aboutissement est finie, et que'",
           "*finie* italic", "finie roman", "italics", None, "high",
           r"est finie, et que", r"est \emph{finie}, et que", "Enlarged view."))

# ---------------------------------------------------------------- page 74
L.append(F(74, "(13.6.4), 1st line: 'sont stationnaires, donc la suite spectrale'",
           "*stationnaires* italic", "stationnaires roman", "italics", None, "high",
           r"sont<NL>stationnaires,", r"sont<NL>\emph{stationnaires},", "Enlarged crop."))
L.append(F(74, "(13.6.5): 'on a (Tv)(T(F^i(X))) ⊂ T(F^{i+s}(Y)) pour tout i ∈ Z'",
           "formula inline in the running text", "display \\[ ... \\]", "other", None, "high",
           r"on a<NL>\[<NL>(\mathrm T v)(\mathrm T(\mathrm F^i(X^\bullet)))<NL>\subset\mathrm T(\mathrm F^{i+s}(Y^\bullet))<NL>\]<NL>pour tout",
           r"on a<NL>$(\mathrm T v)(\mathrm T(\mathrm F^i(X^\bullet)))<NL>\subset\mathrm T(\mathrm F^{i+s}(Y^\bullet))$<NL>pour tout",
           "Displayed formula the print sets inline (only w_r : E_r(A) → E_r(B); is displayed)."))
L.append(F(74, "(13.6.5), second diagram, bottom right vertex 'gr^{p+s}(R^{p+q}T(B))'",
           "no full stop after the diagram", "full stop after T(B))", "punctuation", None, "high",
           r"\mathrm T(B)).<NL>}", r"\mathrm T(B))<NL>}",
           "Enlarged crop: the diagram ends without punctuation (the first diagram has none either)."))
L.append(F(74, "(13.6.6): 'un anneau S, muni d'une filtration (F^i(S))_{i∈Z}'",
           "*filtration* italic", "filtration roman", "italics", None, "high",
           r"muni d'une<NL>filtration $(\mathrm F^i(S))", r"muni d'une<NL>\emph{filtration} $(\mathrm F^i(S))",
           "Strip and enlarged crop."))
L.append(Cfix(74, "(13.6.6.1): 'h : S → Hom_C(A, A)' (subscript)",
              r"\operatorname{Hom}_C(A,A)", r"\operatorname{Hom}_{\boldsymbol{C}}(A,A)"))

# ---------------------------------------------------------------- page 75
L.append(F(75, "1st line: 'tel que pour tout t ∈ F^j(S), on ait ...'",
           "t∈F^j(S)", "$t\\in\\mathrm F^i(S)$", "formula", None, "high",
           r"$t\in\mathrm F^i(S)$", r"$t\in\mathrm F^j(S)$",
           "3x crop: F^j(S) here and h_t(F^i(A)) next; the TeX swaps i and j."))
L.append(F(75, "1st line: '... on ait h_t(F^i(A)) ⊂ F^{i+j}(A)'",
           "h_t(F^i(A))", "$h_t(\\mathrm F^j(A))", "formula", None, "high",
           r"$h_t(\mathrm F^j(A))", r"$h_t(\mathrm F^i(A))",
           "Pairs with the previous finding (the print's reading)."))
L.append(Cfix(75, "'une structure de S-C-module filtré'",
              r"\emph{$S$-$C$-module filtré}", r"\emph{$S$-$\boldsymbol{C}$-module filtré}"))
L.append(F(75, "'définit un endomorphisme gradué h̄_t de gr(A)'",
           "*gradué* italic", "gradué roman", "italics", None, "high",
           r"un endomorphisme gradué $\overline h_t$", r"un endomorphisme \emph{gradué} $\overline h_t$",
           "Enlarged crop."))
L.append(F(75, "'on définit ainsi un homomorphisme d'anneaux gradués'",
           "*anneaux gradués* italic", "roman", "italics", None, "high",
           r"d'anneaux<NL>gradués<NL>\[", r"d'\emph{anneaux<NL>gradués}<NL>\[",
           "Enlarged crop; the elided d' is roman."))
L.append(Cfix(75, "display 'h̄ : gr(S) → Hom^g_C(gr(A), gr(A))' (subscript)",
              r"\operatorname{Hom}_C^g(", r"\operatorname{Hom}_{\boldsymbol{C}}^g("))
L.append(F(75, "'où le second membre est l'anneau des endomorphismes gradués de gr(A)'",
           "*gradués* italic", "gradués roman", "italics", None, "high",
           r"endomorphismes gradués de", r"endomorphismes \emph{gradués} de", "Enlarged crop."))
L.append(Cfix(75, "'une structure de gr(S)-C-module gradué'",
              r"$C$-module gradué}", r"$\boldsymbol{C}$-module gradué}"))
L.append(F(75, "'des endomorphismes bigradués de degrés (s, —s)'",
           "(s, —s)", "$(s,-s)$ (keeps the print)", "misprint_in_print", None, "medium",
           None, None,
           "t̄ ∈ gr^j(S) comes from h_t with t ∈ F^j(S), so (13.6.5) applies with s = j: the endomorphisms have bidegree (j, -j). s is not defined in (13.6.6). The TeX keeps the printed reading.",
           corrected=r"$(j,-j)$"))
L.append(Cfix(75, "'ces derniers sont des gr(S)-C'-modules bigradués'",
              r"$C'$-modules bigradués}", r"$\boldsymbol{C}'$-modules bigradués}", prime=True))
L.append(F(75, "'les α_r^pq définissent un isomorphisme pour ce type de structures'",
           "*isomorphisme* italic", "roman", "italics", None, "high",
           r"définissent un isomorphisme pour ce type", r"définissent un \emph{isomorphisme} pour ce type",
           "Enlarged crop."))
L.append(F(75, "'le sous-objet gradué de B_r^••(A) ...' (B)",
           "B_r^{••}(A): two bullets", "$\\mathrm B_r^\\bullet(A)$ (one bullet)", "formula", None, "high",
           r"$\mathrm B_r^\bullet(A)$", r"$\mathrm B_r^{\bullet\bullet}(A)$",
           "3.5x crop: two dots side by side in all three superscripts (bigraded objects)."))
L.append(F(75, "'(resp. Z_r^••(A), E_r^••(A))' (Z)",
           "Z_r^{••}(A)", "$\\mathrm Z_r^\\bullet(A)$", "formula", None, "high",
           r"$\mathrm Z_r^\bullet(A)$", r"$\mathrm Z_r^{\bullet\bullet}(A)$", "As the previous finding."))
L.append(F(75, "'(resp. Z_r^••(A), E_r^••(A))' (E)",
           "E_r^{••}(A)", "$\\mathrm E_r^\\bullet(A)$", "formula", None, "high",
           r"$\mathrm E_r^\bullet(A)$", r"$\mathrm E_r^{\bullet\bullet}(A)$", "As the previous finding."))
L.append(Cfix(75, "'il est immédiat que ce sont des gr(S)-C'-modules gradués'",
              r"$C'$-modules gradués}", r"$\boldsymbol{C}'$-modules gradués}", prime=True))
L.append(F(75, "'qui est ainsi muni d'une structure de gr(S)-C'-module gradué; les β^pq'",
           "*C'-module gradué* italic, C' bold italic", "roman, plain C'", "italics", None, "high",
           r"$C'$-module gradué~; les", r"\emph{$\boldsymbol{C}'$-module gradué}~; les",
           "Enlarged crop. One edit for both differences (the C' font change lies inside the italic span); counted once."))
L.append(F(75, "'les β^pq (pour p+q=n) définissent un isomorphisme de E^(n)(A)'",
           "*isomorphisme* italic", "roman", "italics", None, "high",
           r"définissent un isomorphisme de", r"définissent un \emph{isomorphisme} de", "Enlarged crop."))
L.append(F(75, "'définissent un isomorphisme de E^(n)(A) sur gr(R^nT(A))'",
           "E^{(n)}(A) with no index r", "$\\mathrm E^{(n)}(A)$ (keeps the print)", "misprint_in_print", None, "low",
           None, None,
           "The β^pq are defined on E_∞^pq(A), and E_r^(n)(A) was just defined for 1 ⩽ r ⩽ +∞, so the source should be E_∞^(n)(A). Possibly an intended abbreviation; the TeX keeps the printed reading.",
           corrected=r"$\mathrm E_\infty^{(n)}(A)$"))
L.append(Cfix(75, "'On notera que lorsque C' est la catégorie'",
              r"lorsque $C'$ est", r"lorsque $\boldsymbol{C}'$ est", prime=True))
L.append(F(75, "'la catégorie des groupes abéliens, les structures de'",
           "*groupes abéliens* italic", "roman", "italics", None, "high",
           r"des groupes abéliens, les", r"des \emph{groupes abéliens}, les", "Enlarged crop."))
L.append(Cfix(75, "'les structures de S-C'-module (resp. de'",
              r"$S$-$C'$-module (resp. de", r"$S$-$\boldsymbol{C}'$-module (resp. de", prime=True))
L.append(Cfix(75, "'(resp. de gr(S)-C'-module gradué ou bigradué)'",
              r"$C'$-module gradué ou bigradué", r"$\boldsymbol{C}'$-module gradué ou bigradué", prime=True))
L.append(F(75, "'les structures usuelles de S-module (resp. gr(S)-module gradué, bigradué)'",
           "S-*module*: 'module' italic; the following 'module gradué, bigradué' roman",
           "roman", "italics", None, "high",
           r"de $S$-module (resp.", r"de $S$-\emph{module} (resp.",
           "Enlarged crop. Possibly a wrong-font slip rather than emphasis; reproduced either way."))
L.append(Cfix(75, "(13.7.1): 'Soient C, C' deux catégories abéliennes' (first letter)",
              r"Soient $C$,", r"Soient $\boldsymbol{C}$,"))
L.append(Cfix(75, "(13.7.1): 'Soient C, C' deux catégories abéliennes' (C')",
              r"$C'$ deux catégories", r"$\boldsymbol{C}'$ deux catégories", prime=True))
L.append(Cfix(75, "(13.7.1): 'C étant supposée telle que'",
              r"$C$ étant supposée", r"$\boldsymbol{C}$ étant supposée"))
L.append(Cfix(75, "(13.7.1): 'tout objet de C soit sous-objet d'un objet injectif'",
              r"objet de $C$ soit sous-objet", r"objet de $\boldsymbol{C}$ soit sous-objet"))
L.append(Cfix(75, "(13.7.1): 'soit T : C → C'' (source)",
              r"T:C\to", r"T:\boldsymbol{C}\to"))
L.append(Cfix(75, "(13.7.1): 'soit T : C → C'' (target)",
              r"C'$ un foncteur", r"\boldsymbol{C}'$ un foncteur", prime=True))
L.append(F(75, "(13.7.1): 'Considérons un système projectif strict A = (A_k)_{k∈Z}'",
           "*système projectif strict* italic", "roman", "italics", None, "high",
           r"Considérons un<NL>système projectif strict $\mathbf A", r"Considérons un<NL>\emph{système projectif strict} $\mathbf A",
           "Enlarged crop."))
L.append(Cfix(75, "(13.7.1): 'dans C, limité inférieurement'",
              r"dans $C$,<NL>\emph{limité", r"dans $\boldsymbol{C}$,<NL>\emph{limité"))
L.append(F(75, "(13.7.1): 'une filtration (F^p(A_k))_{k∈Z} sur chaque A_k'",
           "index k∈Z", "$(\\mathrm F^p(A_k))_{p\\in\\mathbb Z}$ (silently corrected)", "misprint_in_print", None, "high",
           r"$(\mathrm F^p(A_k))_{p\in\mathbb Z}$", r"$(\mathrm F^p(A_k))_{k\in\mathbb Z}$",
           "2.5x crop: the print indexes the filtration of the fixed A_k by k; it runs over p. The fix restores the printed reading.",
           corrected=r"$(\mathrm F^p(A_k))_{p\in\mathbb Z}$"))
L.append(F(75, "(13.7.1): 'sur chaque A_k par les formules (13.4.1.1)'",
           "no comma after A_k", "comma after $A_k$", "punctuation", None, "high",
           r"sur chaque $A_k$, par les", r"sur chaque $A_k$ par les", "2.5x crop."))
L.append(F(75, "(13.7.1): 'comme il s'agit d'un système projectif strict, les morphismes canoniques'",
           "*strict* italic", "roman", "italics", None, "high",
           r"projectif strict, les morphismes", r"projectif \emph{strict}, les morphismes", "Enlarged crop."))
L.append(F(75, "(13.7.1): 'pour i ⩽ j ⩽ k+1 sont des isomorphismes. Rappelons'",
           "*isomorphismes* italic", "roman", "italics", None, "high",
           r"sont des isomorphismes. Rappelons", r"sont des \emph{isomorphismes}. Rappelons", "Enlarged crop."))
L.append(F(75, "(13.7.2): 'Construisons maintenant pour chaque k une résolution injective X_k = (X_k^j)'",
           "*résolution injective* italic", "roman", "italics", None, "high",
           r"une résolution injective<NL>$X_k^\bullet", r"une \emph{résolution injective}<NL>$X_k^\bullet",
           "Enlarged crop."))
L.append(F(75, "page break 75/76 in (13.7.2): printed p. 75 ends '... morphisme de complexes X_{k+1} → X_k compatibles'; p. 76 begins 'avec les filtrations, et faisant de ...'",
           "page 76 begins at 'avec les filtrations'",
           "\\oldpage[0\\textsubscript{III}]{76} stands after 'de complexes.' (first line of the next segment), one line too late",
           "marker", None, "high",
           r"compatibles avec les<NL>filtrations", r"compatibles<NL>\oldpage[0\textsubscript{III}]{76}<NL>avec les<NL>filtrations",
           "Checked on the top strip of p. 76. Apply together with deleting the old marker line: in ega3-1-fr.tex "
           "'de complexes.\\n\\oldpage[0\\textsubscript{III}]{76}\\nOn peut en outre' -> 'de complexes.\\nOn peut en outre' "
           "(outside this page's segment; the print runs on without a paragraph break)."))
L.append(F(75, "(13.7.2), printed on p. 76: 'faisant de X = (X_k)_{k∈Z} un système projectif de complexes'",
           "*système projectif* italic, 'de complexes' roman", "roman", "italics", None, "high",
           r"un système projectif<NL>de complexes.", r"un \emph{système projectif}<NL>de complexes.",
           "Seen on the top strip of p. 76; the TeX for it lies in this page's segment until the marker is moved."))

for d in L:
    if d.get('fix') is not None:
        pass

with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(L, fh, ensure_ascii=False, indent=1)
print(OUT, len(L))
