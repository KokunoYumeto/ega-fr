"""Write findings_071_075.json. TeX strings are raw strings; the pilcrow stands for a line break (LF)."""
import json
import sys

OUT = r"user\Documents\ega_scan_check_20261101\run_0I\findings_071_075.json"
NL = "\u00b6"


def f(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": conv,
         "confidence": conf,
         "fix": None if old is None else {"old": old.replace(NL, "\n"), "new": new.replace(NL, "\n")}}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


M71 = r"\oldpage[0\textsubscript{I}]{71}"
M72 = r"\oldpage[0\textsubscript{I}]{72}"
M74 = r"\oldpage[0\textsubscript{I}]{74}"
M75 = r"\oldpage[0\textsubscript{I}]{75}"
M76 = r"\oldpage[0\textsubscript{I}]{76}"
PB = ("GLOBAL_ISSUES item 20 (blank line at a page break that falls mid-sentence). "
      "\\oldpage ends with \\ignorespaces, so joining the lines leaves a single space.")

F = [
    # ---------------- page 70 (outside pages 71-75; half of the p. 70/71 page-break fix) ----------------
    f(70, "end of p. 70, just before \\oldpage[0\\textsubscript{I}]{71}: '... tel que 𝔍/𝔍² soit de type fini' "
          "(item (ii) of Proposition (7.5.4); outside pages 71-75)",
      "the sentence runs on to the top of p. 71 ('sur A/𝔍.') with no paragraph break",
      "blank line before \\oldpage[0\\textsubscript{I}]{71}",
      "other", None, "high",
      r"soit de type fini¶¶", r"soit de type fini¶",
      "Lies in page 70's segment (checked unique in page_070.tex). Apply together with the p. 71 entry that removes "
      "the blank line after the marker; one of the two alone leaves the paragraph break. " + PB),

    # ---------------- page 71 ----------------
    f(71, "top of p. 71: 'sur A/𝔍. Si on pose 𝔍' = 𝔍A' ...' (continues the sentence of (7.5.4) (ii) from p. 70)",
      "no paragraph break: the first line continues the sentence, flush left",
      "blank line after \\oldpage[0\\textsubscript{I}]{71} (paragraph break inside item (ii))",
      "other", None, "high",
      M71 + r"¶¶  sur", M71 + r"¶  sur",
      "Apply together with the p. 70 entry (the blank line before the marker ends page 70's segment). " + PB),

    f(71, "(7.5.4), proof of (ii), page line 13: 'le noyau 𝔍'_i de u_{0i} est l'ensemble des polynômes de "
          "A_i[T_1, ..., T_r]'",
      "u_{0i} without prime",
      "$u'_{0i}$",
      "misprint_in_print", None, "high",
      r"de $u'_{0i}$ est", r"de $u_{0i}$ est",
      "Enlarged crop. The TeX silently corrects the print. 𝔍'_i is a set of polynomials in A'_i = A_i[T_1, ..., T_r], "
      "the kernel of u'_{0i}: A'_i → A'_0; u_{0i}: A_i → A_0 is the map of coefficient rings, with kernel 𝔍/𝔍^{i+1}.",
      corrected=r"$u'_{0i}$"),

    f(71, "(7.5.4), proof of (ii), page line 17: 'Montrons que le noyau de u_{ij} est 𝔍'_j^{i+1}'",
      "u_{ij} without prime",
      "$u'_{ij}$",
      "misprint_in_print", None, "high",
      r"le noyau de $u'_{ij}$ est", r"le noyau de $u_{ij}$ est",
      "Enlarged crop. The TeX silently corrects the print. 𝔍'_j^{i+1} is an ideal of A'_j, so the map is "
      "u'_{ij}: A'_j → A'_i (as in the preceding sentences); the kernel of u_{ij}: A_j → A_i is 𝔍^{i+1}/𝔍^{j+1}.",
      corrected=r"$u'_{ij}$"),

    f(71, "Proposition (7.5.5) c): '(nécessairement fermé en vertu de (7.3.6) et (7.5.4 (ii)))'",
      "reference (7.3.6) upright inside the italic statement",
      "(7.3.6) italic (proposition environment)",
      "convention", 6, "high",
      r"de (7.3.6) et", r"de \textup{(7.3.6)} et",
      "Enlarged crop: 'nécessairement fermé en vertu de' and 'et' are italic, the references roman."),

    f(71, "Proposition (7.5.5) c): '... et (7.5.4 (ii)))'",
      "reference (7.5.4 (ii)) upright inside the italic statement",
      "(7.5.4 (ii)) italic (proposition environment)",
      "convention", 6, "high",
      r"(7.5.4 (ii))", r"\textup{(7.5.4 (ii))}",
      "Enlarged crop. The final parenthesis closing '(nécessairement ...' is left outside the \\textup."),

    f(71, "proof of (7.5.5), 1st paragraph: 'donc c) implique que B est noethérien'",
      "c) italic",
      "c) upright",
      "italics", None, "high",
      r"donc c) implique", r"donc \emph{c)} implique",
      "Enlarged crop. Condition labels in running text are italic in the print (cf. the earlier fixes "
      "'que \\emph{c)} entraîne \\emph{a)}')."),

    f(71, "proof of (7.5.5), end of 1st paragraph: 'ce qui achève de prouver que c) entraîne a).'",
      "c) and a) italic",
      "c), a) upright",
      "italics", None, "high",
      r"que c) entraîne a)", r"que \emph{c)} entraîne \emph{a)}",
      "Enlarged crop."),

    f(71, "foot of p. 71 / top of p. 72: '(c_i)_{1⩽i⩽r} un système d'éléments de B/𝔍²B dont les classes / "
          "mod. 𝔍B/𝔍²B forment ...'",
      "no paragraph break across the page break (p. 72 begins flush left in mid-sentence)",
      "blank line before \\oldpage[0\\textsubscript{I}]{72}",
      "other", None, "high",
      r"classes¶¶", r"classes¶",
      "Apply together with the p. 72 entry that removes the blank line after the marker. " + PB),

    # ---------------- page 72 ----------------
    f(72, "top of p. 72: 'mod. 𝔍B/𝔍²B forment un système de générateurs ...' (continues the sentence from p. 71)",
      "no paragraph break: the first line continues the sentence, flush left",
      "blank line after \\oldpage[0\\textsubscript{I}]{72}",
      "other", None, "high",
      M72 + r"¶¶mod.", M72 + r"¶mod.",
      "Apply together with the p. 71 entry 'classes' (blank line before the marker). " + PB),

    f(72, "proof of (7.5.5), page line 3: 'donc a) implique b).'",
      "a) and b) italic",
      "a), b) upright",
      "italics", None, "high",
      r"donc a) implique b)", r"donc \emph{a)} implique \emph{b)}",
      "Enlarged crop."),

    f(72, "proof of (7.5.5), page line 4: 'Reste à prouver que b) entraîne c).'",
      "b) and c) italic",
      "b), c) upright",
      "italics", None, "high",
      r"que b) entraîne c)", r"que \emph{b)} entraîne \emph{c)}",
      "Enlarged crop."),

    f(72, "proof of (7.5.5): 'si nous prouvons que u est surjectif, c) sera établi'",
      "c) italic",
      "c) upright",
      "italics", None, "high",
      r"c) sera établi", r"\emph{c)} sera établi",
      "Enlarged crop."),

    f(72, "proof of (7.5.5): 'il suffit ([1], p. 18-07) de montrer que'",
      "[1] (old-style figure one, the same glyph as the 1 of 18-07)",
      "[I]",
      "number", None, "high",
      r"([I], p.~18-07)", r"([1], p.~18-07)",
      "Enlarged crop. Bibliography item 1 (Cartan–Chevalley, Séminaire E.N.S. 1955-56, exposé 18). "
      "Same fix as the three applied on pp. 64-65 (findings_061_065)."),

    f(72, "after Corollaire (7.6.3), last sentence: 'pour tout λ il existe n tel que f^n ∈ J_λ, donc'",
      "f^n∈J_λ with a roman capital J, not the Fraktur 𝔍 used in the same lines",
      "$f^n\\in\\mathfrak J_\\lambda$",
      "misprint_in_print", None, "high",
      r"$f^n\in\mathfrak J_\lambda$", r"$f^n\in J_\lambda$",
      "Enlarged crop. The TeX silently corrects the print; the ideals of the fundamental system are 𝔍_λ.",
      corrected=r"$f^n\in\mathfrak J_\lambda$"),

    # ---------------- page 73 ----------------
    f(73, "(7.6.9), page line 30: 'de la forme S^{-1}𝔞, où 𝔞 ⊃ J_λ.'",
      "𝔞⊃J_λ with a roman capital J",
      "$\\mathfrak a\\supset\\mathfrak J_\\lambda$",
      "misprint_in_print", None, "high",
      r"$\mathfrak a\supset\mathfrak J_\lambda$", r"$\mathfrak a\supset J_\lambda$",
      "Enlarged crop; same slip as on p. 72 (f^n ∈ J_λ). The TeX silently corrects the print.",
      corrected=r"$\mathfrak a\supset\mathfrak J_\lambda$"),

    f(73, "Proposition (7.6.10), 1st line: 'L'application 𝔭 → 𝔭{S^{-1}}'",
      "plain arrow →",
      "\\mapsto",
      "convention", 3, "high",
      r"$\mathfrak p\mapsto\mathfrak p\{S^{-1}\}$", r"$\mathfrak p\to\mathfrak p\{S^{-1}\}$",
      "Enlarged crop: no bar at the tail."),

    f(73, "Proposition (7.6.10), page line 33: 'de l'ensemble des idéaux premiers ouverts 𝔭 de A tels que'",
      "'premiers ouverts' roman inside the italic statement",
      "italic (proposition environment)",
      "convention", 6, "high",
      r"idéaux premiers ouverts $\mathfrak p$", r"idéaux \textup{premiers ouverts} $\mathfrak p$",
      "Enlarged crop."),

    f(73, "Proposition (7.6.10), last line of p. 73: 'sur l'ensemble des idéaux premiers ouverts / de A{S^{-1}}'",
      "'premiers ouverts' roman inside the italic statement; the sentence continues on p. 74 without a paragraph break",
      "italic; blank line before \\oldpage[0\\textsubscript{I}]{74}",
      "convention", 6, "high",
      r"idéaux premiers ouverts¶¶", r"idéaux \textup{premiers ouverts}¶",
      "Enlarged crop. This one edit also removes the blank line before \\oldpage{74} (" + PB + "), because both "
      "changes touch the same words; apply it together with the p. 74 entry that removes the blank line after the marker."),

    # ---------------- page 74 ----------------
    f(74, "top of p. 74: 'de A{S^{-1}} ; en outre, le corps des fractions ...' (Proposition (7.6.10) continued)",
      "no paragraph break: the first line continues the statement, flush left",
      "blank line after \\oldpage[0\\textsubscript{I}]{74}",
      "other", None, "high",
      M74 + r"¶¶de $A", M74 + r"¶de $A",
      "Apply together with the last p. 73 entry ('idéaux premiers ouverts', which removes the blank line before the "
      "marker). " + PB),

    f(74, "Corollaire (7.6.12): 'Sous les hypothèses de (7.6.11, (ii)), on a'",
      "reference (7.6.11, (ii)) upright inside the italic statement",
      "italic (corollary environment)",
      "convention", 6, "high",
      r"(7.6.11, (ii))", r"\textup{(7.6.11, (ii))}",
      "Enlarged crop."),

    f(74, "Corollaire (7.6.14): 'Sous les hypothèses de (7.6.13), soit S' ⊂ S'",
      "reference (7.6.13) upright inside the italic statement",
      "italic (corollary environment)",
      "convention", 6, "high",
      r"de (7.6.13), soit", r"de \textup{(7.6.13)}, soit",
      "Enlarged crop."),

    f(74, "foot of p. 74 / top of p. 75, (7.6.15): '... on a un homomorphisme A_{f} → A{S^{-1}} (7.6.7), et / "
          "ces homomorphismes forment ...'",
      "no paragraph break across the page break (p. 75 begins flush left in mid-sentence)",
      "blank line before \\oldpage[0\\textsubscript{I}]{75}",
      "other", None, "high",
      r"(7.6.7), et¶¶", r"(7.6.7), et¶",
      "Apply together with the p. 75 entry that removes the blank line after the marker. " + PB),

    # ---------------- page 75 ----------------
    f(75, "top of p. 75: 'ces homomorphismes forment un système inductif ...' (continues (7.6.15) from p. 74)",
      "no paragraph break: the first line continues the sentence, flush left",
      "blank line after \\oldpage[0\\textsubscript{I}]{75}",
      "other", None, "high",
      M75 + r"¶¶ces", M75 + r"¶ces",
      "Apply together with the p. 74 entry '(7.6.7), et'. " + PB),

    f(75, "Proposition (7.6.17), 1st sentence: 'et soit S = A—𝔭.'",
      "A—𝔭 (long dash, set difference)",
      "$S=A-\\mathfrak p$",
      "convention", 7, "high",
      r"$S=A-\mathfrak p$", r"$S=A\setmin\mathfrak p$",
      "Enlarged crop. Form of the fix as in findings_011_015 (p. 13)."),

    f(75, "Corollaire (7.6.18): 'Sous les hypothèses de (7.6.17), si on suppose de plus'",
      "reference (7.6.17) upright inside the italic statement",
      "italic (corollary environment)",
      "convention", 6, "high",
      r"(7.6.17)", r"\textup{(7.6.17)}",
      "Enlarged crop."),

    f(75, "(7.7.1), 1st line: 'Soient A un anneau linéairement topologisé, M, N, deux A-modules'",
      "bold M (wrong-font sort: thick stems and serifs; the N beside it and the later M's are normal weight)",
      "$M$",
      "misprint_in_print", None, "medium",
      r"$M$, $N$, deux", r"$\mathbf{M}$, $N$, deux",
      "Crop at 3x. The TeX silently corrects it. Medium only because it is a typographical (wrong-font) rather than a "
      "textual misprint; drop the edit if such slips are not to be reproduced.",
      corrected=r"$M$"),

    f(75, "(7.7.1), 2nd sentence: 'et tels que 𝔍.M ⊂ V, 𝔍.N ⊂ W, de sorte que'",
      "𝔍.M⊂V, 𝔍.N⊂W: a dot between 𝔍 and M, N",
      "$\\mathfrak JM\\subset V$, $\\mathfrak JN\\subset W$ (no dot)",
      "symbol", None, "high",
      r"$\mathfrak JM\subset V$, $\mathfrak JN\subset W$", r"$\mathfrak J.M\subset V$, $\mathfrak J.N\subset W$",
      "Enlarged crop. The file writes the same notation as '$\\mathfrak J.B\\subset\\mathfrak K$' a little further on."),

    f(75, "foot of p. 75 / top of p. 76, (7.7.1): '... forment un système projectif de modules / sur le système "
          "projectif d'anneaux A/𝔍 ...'",
      "no paragraph break across the page break (p. 76 begins flush left in mid-sentence)",
      "blank line before \\oldpage[0\\textsubscript{I}]{76}",
      "other", None, "high",
      r"projectif de modules¶¶", r"projectif de modules¶",
      "Apply together with the p. 76 entry that removes the blank line after the marker. " + PB),

    # ---------------- page 76 (outside pages 71-75; half of the p. 75/76 page-break fix) ----------------
    f(76, "top of p. 76 (outside pages 71-75): 'sur le système projectif d'anneaux A/𝔍 ; par passage à la limite'",
      "no paragraph break: the first line continues the sentence of (7.7.1), flush left",
      "blank line after \\oldpage[0\\textsubscript{I}]{76}",
      "other", None, "high",
      M76 + r"¶¶sur le", M76 + r"¶sur le",
      "Lies in page 76's segment (checked unique in page_076.tex; findings_076_078 has no entry for it). Apply together "
      "with the p. 75 entry 'projectif de modules'. " + PB),
]

json.dump(F, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
sys.stdout.reconfigure(encoding="utf-8")
print(len(F), "findings written to", OUT)
