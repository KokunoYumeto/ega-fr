import json
import os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, "findings_196_200.json")
NL = "\n"

F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note=None, corrected=None):
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
    F.append(d)


# ---------------- page 196 ----------------
add(196, "top of p. 196: page break inside the sentence '... les colonnes extrêmes du diagramme (22.4.4.6) sont donc formées ...'",
    "the display (22.4.4.6) heads the page and 'sont donc formées' follows flush left: the sentence of p. 195 runs on, no paragraph break",
    "blank line after \\oldpage{196} (and one before it at the end of p. 195's segment): paragraph break before the display",
    "other", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{196}" + NL + NL + r"\begin{equation}",
    r"\oldpage[0\textsubscript{IV-1}]{196}" + NL + r"\begin{equation}",
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20). Apply together with the removal of the blank line BEFORE the marker, which lies in page_195.tex (outside pp. 196-200): 'les colonnes extrêmes du diagramme\\n\\n' -> 'les colonnes extrêmes du diagramme\\n'.")

add(196, "diagram (22.4.4.6), second row '0 → V_0⊗_K K' → V'_0 → 0': its two zeros",
    "vertical arrows descend from both zeros: 0 → N (left column) and 0 → Ω^1_{A'/A}⊗_{A'}K' (right column) (crops)",
    "the two zeros of the second row have no \\ar[d]",
    "missing", None, "high",
    r"& 0 \ar[r] & V_0\otimes_KK' \ar[r] \ar[d] & V_0' \ar[r] \ar[d] & 0 & \\",
    r"& 0 \ar[r] \ar[d] & V_0\otimes_KK' \ar[r] \ar[d] & V_0' \ar[r] \ar[d] & 0 \ar[d] & \\",
    "The outer columns begin with 0 (kernels/cokernels of the middle horizontal arrows, as the following sentence says).")

add(196, "diagram (22.4.4.6), bottom: below Υ_{K'/K} and Ω^1_{K'/K}",
    "no arrows below Υ_{K'/K} and Ω^1_{K'/K}; the last row has only two zeros, under Ω^1_K⊗_K K' and Ω^1_{K'} (crop)",
    "\\ar[d] from \\Upsilon_{K'/K} and from \\Omega^1_{K'/K} to two extra zeros; last row '& 0 & 0 & 0 & 0 &'",
    "extra", None, "high",
    r"\Upsilon_{K'/K} \ar[r] \ar[d] &" + NL
    + r"      \Omega^1_K\otimes_KK' \ar[r] \ar[d] & \Omega^1_{K'} \ar[r] \ar[d] &" + NL
    + r"      \Omega^1_{K'/K} \ar[r] \ar[d] & 0 \\" + NL
    + r"    & 0 & 0 & 0 & 0 &",
    r"\Upsilon_{K'/K} \ar[r] &" + NL
    + r"      \Omega^1_K\otimes_KK' \ar[r] \ar[d] & \Omega^1_{K'} \ar[r] \ar[d] &" + NL
    + r"      \Omega^1_{K'/K} \ar[r] & 0 \\" + NL
    + r"    && 0 & 0 &&",
    "One edit for the two arrows and the two zeros (the middle line is unchanged).")

add(196, "after (22.4.4.6): 'des noyaux et des conoyaux des flèches horizontales'",
    "'noyaux' and 'conoyaux' italic (crop)",
    "des noyaux et des conoyaux (upright, proof text)",
    "italics", None, "high",
    "des noyaux et des conoyaux",
    r"des \emph{noyaux} et des \emph{conoyaux}",
    "Two words, one edit.")

add(196, "'ce qui achève de prouver que le diagramme est commutatif. En outre :'",
    "'commutatif' italic (crop)",
    "commutatif (upright)",
    "italics", None, "high",
    "commutatif. En outre",
    r"\emph{commutatif}. En outre",
    None)

add(196, "Lemme (22.4.4.7): 'du diagramme (22.4.4.6) sont bijectifs.'",
    "the reference (22.4.4.6) is roman inside the italic statement",
    "(22.4.4.6) italic inside the lemma environment",
    "convention", 6, "high",
    "du diagramme (22.4.4.6) sont bijectifs.",
    r"du diagramme \textup{(22.4.4.6)} sont bijectifs.",
    None)

add(196, "end of the proof of (22.4.4): 'dans A' on a p.1∈𝔪A'⊂𝔪''",
    "p.1 with a baseline period (crop at 2.5x)",
    "p\\cdot1 (centred dot)",
    "symbol", None, "high",
    r"p\cdot1\in\mathfrak mA'",
    r"p.1\in\mathfrak mA'",
    "GLOBAL_ISSUES 65 (ega0-22: 7 to check); same fix as pp. 111-115.")

add(196, "end of the proof of (22.4.4): 'cela prouve que les d_A f_i⊗1_K appartiennent à N'",
    "d_A f_i⊗1_K: subscript K without prime (crops at 2.5x and 5x)",
    "$d_Af_i\\otimes1_{K'}$ (silent correction)",
    "misprint_in_print", None, "high",
    r"$d_Af_i\otimes1_{K'}$ appartiennent",
    r"$d_Af_i\otimes1_K$ appartiennent",
    "Silently corrected in the TeX; the fix restores the printed reading. N is a submodule of Ω^1_A⊗_A K' (kernel of Ω^1_A⊗_A K' → Ω^1_{A'}⊗_{A'}K' in (22.4.4.6)), and the preceding clause has d_{A'}f_i⊗1_{K'}=0, so the elements are d_A f_i⊗1_{K'}. Not in the IV errata list 3.",
    r"$d_Af_i\otimes1_{K'}$ appartiennent")

add(196, "end of the proof of (22.4.4): 'qui forment une base de Υ_{K'/K} sur K''",
    "'base' italic (crop)",
    "une base de (upright)",
    "italics", None, "high",
    "une base de",
    r"une \emph{base} de",
    None)

add(196, "end of p. 196: page break inside the sentence '... deux homomorphismes A→B→A | vérifiant les conditions de (21.3.1)'",
    "p. 197 begins flush left with 'vérifiant', continuing the sentence after the display",
    "blank line after the display, before \\oldpage{197} (and another after the marker): paragraph break",
    "other", None, "high",
    r"A\xrightarrow{i}B\xrightarrow{j}A" + NL + r"\]" + NL + NL,
    r"A\xrightarrow{i}B\xrightarrow{j}A" + NL + r"\]" + NL,
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 197 finding that removes the blank line after \\oldpage{197}.")

# ---------------- page 197 ----------------
add(197, "top of p. 197: 'vérifiant les conditions de (21.3.1)'",
    "flush left: continues the sentence of p. 196 (no paragraph break)",
    "blank line after \\oldpage{197}",
    "other", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{197}" + NL + NL + "vérifiant",
    r"\oldpage[0\textsubscript{IV-1}]{197}" + NL + "vérifiant",
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 196 finding that removes the blank line before the marker.")

add(197, "after the display j'(i'(x))=x^p ... y∈B_{(K)}: 'En posant, suivant les notations de (21.3.2)'",
    "'En posant' begins a new indented paragraph",
    "no blank line after \\]: same paragraph, no indent",
    "other", None, "high",
    r"\]" + NL + "En posant, suivant",
    r"\]" + NL + NL + "En posant, suivant",
    "Missing paragraph break after a display (cf. GLOBAL_ISSUES 47). Independent of the comma fix that follows.")

add(197, "'En posant, suivant les notations de (21.3.2)' before the display Θ_{B_{(K)}/A}",
    "no comma after (21.3.2) (crop at 2.2x)",
    "(21.3.2),",
    "punctuation", None, "high",
    "les notations de (21.3.2),",
    "les notations de (21.3.2)",
    None)

add(197, "display Θ_{B_{(K)}/A}=Ω^1_{B_{(K)}/A}⊗_{B_{(K)}}A_{[j']}=Ω^1_{B_{(K)}/K}⊗_{B_{(K)}}A_{[j']}",
    "no punctuation at the end of the display (crop at 2.2x)",
    "A_{[j']}, (final comma)",
    "punctuation", None, "high",
    "A_{[j']},",
    "A_{[j']}",
    None)

add(197, "'(tenant compte de ce que j(i(𝔪))=0) des homomorphismes'",
    "no comma after the closing parenthesis (crop at 2.2x)",
    "=0$), des homomorphismes",
    "punctuation", None, "high",
    "=0$), des homomorphismes",
    "=0$) des homomorphismes",
    None)

add(197, "commutative diagram A→B→A / K→B_{(K)}→K: label ψ of the middle vertical arrow",
    "ψ stands to the LEFT of the arrow B→B_{(K)} (both φ labels: left, right)",
    "\\ar[d]^\\psi puts ψ on the right",
    "other", None, "high",
    r"\ar[d]^\psi",
    r"\ar[d]_\psi",
    "Label placement only (cf. GLOBAL_ISSUES 30 for wrong-side labels).")

add(197, "after the diagram: 'Il est clair en outre que l'on a'",
    "new indented paragraph",
    "no blank line after \\]: same paragraph, no indent",
    "other", None, "high",
    r"\]" + NL + "Il est clair",
    r"\]" + NL + NL + "Il est clair",
    "Missing paragraph break after a display.")

add(197, "after the display j_0(i_0(s))=s^p ...: 'On définit donc de même'",
    "new indented paragraph",
    "no blank line after \\]: same paragraph, no indent",
    "other", None, "high",
    r"\]" + NL + "On définit donc",
    r"\]" + NL + NL + "On définit donc",
    "Missing paragraph break after a display.")

add(197, "display Θ_{B_{(K)}/K}=Ω^1_{B_{(K)}/K}⊗_{B_{(K)}}K_{[j_0]}=Θ_{B_{(K)}/A}⊗_A K",
    "no punctuation at the end of the display (crop at 2.2x)",
    "\\otimes_AK, (final comma)",
    "punctuation", None, "high",
    r"=\Theta_{B_{(K)}/A}\otimes_AK,",
    r"=\Theta_{B_{(K)}/A}\otimes_AK",
    None)

# ---------------- page 198 ----------------
add(198, "(22.4.6), line 2: 'que 𝔪 soit un idéal maximal de carré nul, donc K un corps'",
    "only 'maximal' italic; 'de carré nul' roman (crop at 2x)",
    "\\emph{maximal de carré nul}",
    "italics", None, "high",
    r"\emph{maximal de carré nul}",
    r"\emph{maximal} de carré nul",
    None)

add(198, "(22.4.6), after (22.4.6.1): 'On a donc par (22.4.5.3) un homomorphisme noté'",
    "new indented paragraph",
    "no blank line after \\end{equation}: same paragraph, no indent",
    "other", None, "high",
    r"\end{equation}" + NL + "On a donc par (22.4.5.3)",
    r"\end{equation}" + NL + NL + "On a donc par (22.4.5.3)",
    "Missing paragraph break after a display.")

add(198, "(22.4.6), last sentence: 'il faut et il suffit que π'_{B_{(K)}/K} soit injectif, le noyau'",
    "the second 'injectif' italic too (crop)",
    "soit injectif, (upright)",
    "italics", None, "high",
    "soit injectif, le noyau",
    r"soit \emph{injectif}, le noyau",
    None)

add(198, "(22.4.7.1): 'F_i(T_i)=T_i^p—f_i'",
    "long dash for the subtraction (crop at 2x)",
    "T_i^p-f_i",
    "convention", 7, "high",
    "T_i^p-f_i",
    r"T_i^p\setmin f_i",
    "Subtraction, not set difference (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")

add(198, "Proposition (22.4.7) (ii): '(cf. (22.4.6.2)) soit injectif.'",
    "'(cf. (22.4.6.2))' roman inside the italic statement; 'soit injectif.' italic (crop at 2.2x)",
    "(cf. (22.4.6.2)) italic inside the proposition",
    "convention", 6, "high",
    "(cf. (22.4.6.2)) soit injectif.",
    r"\textup{(cf. (22.4.6.2))} soit injectif.",
    None)

add(198, "end of p. 198: page break inside the sentence '... que la sous-famille | (a_i)_{s+1⩽i⩽r} est p-libre'",
    "p. 199 begins flush left with '(a_i)_{s+1⩽i⩽r} est p-libre': same sentence",
    "blank line before \\oldpage{199} (and another after it): paragraph break",
    "other", None, "high",
    "que la sous-famille" + NL + NL,
    "que la sous-famille" + NL,
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 199 finding that removes the blank line after \\oldpage{199}.")

# ---------------- page 199 ----------------
add(199, "top of p. 199: '(a_i)_{s+1⩽i⩽r} est p-libre sur K^p'",
    "flush left: continues the sentence of p. 198",
    "blank line after \\oldpage{199}",
    "other", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{199}" + NL + NL + "$(a_i)",
    r"\oldpage[0\textsubscript{IV-1}]{199}" + NL + "$(a_i)",
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 198 finding that removes the blank line before the marker.")

add(199, "line 1: 'et forme une p-base sur K^p'",
    "'p-base' italic, hyphen and 'base' included (crop)",
    "$p$-base (upright 'base')",
    "italics", None, "high",
    "$p$-base sur",
    r"\emph{$p$-base} sur",
    None)

add(199, "after the display a_i∈K^p(a_{s+1}, ..., a_r) pour 1⩽i⩽s: 'Désignons par A'' l'anneau quotient'",
    "new indented paragraph",
    "no blank line after \\]: same paragraph, no indent",
    "other", None, "high",
    r"\]" + NL + "Désignons par $A''$",
    r"\]" + NL + NL + "Désignons par $A''$",
    "Missing paragraph break after a display.")

add(199, "display G_i(T_i)=T_i^p+Σ_{k=1}^{p−1}(p k)g_i^{p−k}T^k—h_i (1⩽i⩽s)",
    "T^k without the subscript i (crop at 3x)",
    "T_i^k (silent correction)",
    "misprint_in_print", None, "high",
    r"g_i^{p-k}T_i^k",
    r"g_i^{p-k}T^k",
    "Silently corrected in the TeX; the fix restores the printed reading. G_i(T_i)=F_i(T_i+g_i)=(T_i+g_i)^p−f_i, so the term is (p k)g_i^{p−k}T_i^k. Does not overlap the convention-7 fix of '—h_i' (either order).",
    r"g_i^{p-k}T_i^k")

add(199, "same display: 'T^k—h_i'",
    "long dash before h_i (the superscripts p−1, p−k have the short minus) (crop at 3x)",
    "-h_i",
    "convention", 7, "high",
    "-h_i",
    r"\setmin h_i",
    "Subtraction (GLOBAL_ISSUES 23).")

add(199, "'son corps résiduel K' est isomorphe à K''' (line break after 'isomorphe')",
    "'isomorphe à' italic: the 'à' at the start of the next line is italic (crop)",
    "\\emph{isomorphe} à",
    "italics", None, "high",
    r"\emph{isomorphe} à",
    r"\emph{isomorphe à}",
    None)

add(199, "'par l'idéal engendré par les polynômes F̄_i=T_i^p—a_i'",
    "long dash for the subtraction (crop at 2.2x)",
    "T_i^p-a_i",
    "convention", 7, "high",
    "T_i^p-a_i",
    r"T_i^p\setmin a_i",
    "Subtraction (GLOBAL_ISSUES 23).")

add(199, "'la condition que π'_{B_{(K)}/K} soit injectif est donc équivalente au fait que'",
    "'équivalente' italic (crop)",
    "équivalente (upright)",
    "italics", None, "high",
    "injectif est donc équivalente au fait",
    r"injectif est donc \emph{équivalente} au fait",
    None)

add(199, "'le noyau de l'homomorphisme canonique Ω^1_A⊗_A K'→Ω^1_{A''}⊗_{A''}K' a pour base les'",
    "'base' italic (crop)",
    "base (upright)",
    "italics", None, "high",
    "a pour" + NL + "base les",
    "a pour" + NL + r"\emph{base} les",
    None)

add(199, "'sont linéairement indépendants dans Ω^1_{A''}⊗_{A''}K''",
    "'linéairement indépendants' italic; 'dans' roman (crop)",
    "linéairement indépendants (upright)",
    "italics", None, "high",
    "linéairement indépendants dans",
    r"\emph{linéairement indépendants} dans",
    None)

add(199, "same sentence: '... ⊗_{A''}K' pour 1⩽i⩽s.'",
    "'pour' italic (crop at 1.4x; italic p and slanted 'our'), while 'dans' between it and 'indépendants' is roman",
    "pour (upright, the expected reading)",
    "misprint_in_print", None, "medium",
    r"\otimes_{A''}K'$ pour",
    r"\otimes_{A''}K'$ \emph{pour}",
    "Wrong-fount word (cf. GLOBAL_ISSUES 29): the emphasis is 'linéairement indépendants'; 'dans' is roman, so the italic 'pour' looks like a compositor's slip. The TeX has the roman reading; the fix reproduces the print in the diplomatic text, the corrected edition keeps roman. If judged intended emphasis instead, apply to both editions. Independent of the previous edit.",
    r"\otimes_{A''}K'$ pour")

add(199, "'et la condition rg_{K'}(V')=rg_K(V) est donc équivalente à rg_{K'}(V'')=rg_{K'}(V')'",
    "'équivalente' italic (crop)",
    "équivalente (upright)",
    "italics", None, "high",
    "est donc équivalente à",
    r"est donc \emph{équivalente} à",
    None)

add(199, "'cette dernière relation est équivalente au fait que les classes h_i'",
    "'équivalente' italic (crop)",
    "équivalente (upright)",
    "italics", None, "high",
    "relation est équivalente au fait",
    r"relation est \emph{équivalente} au fait",
    None)

add(199, "end of p. 199: page break inside the sentence '... les classes h_i | dans V'' sont linéairement indépendantes'",
    "p. 200 begins flush left with 'dans V''': same sentence",
    "blank line before \\oldpage{200} (and another after it): paragraph break",
    "other", None, "high",
    "que les classes $h_i$" + NL + NL,
    "que les classes $h_i$" + NL,
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 200 finding that removes the blank line after \\oldpage{200}.")

# ---------------- page 200 ----------------
add(200, "top of p. 200: 'dans V'' sont linéairement indépendantes sur K''",
    "flush left: continues the sentence of p. 199",
    "blank line after \\oldpage{200}",
    "other", None, "high",
    r"\oldpage[0\textsubscript{IV-1}]{200}" + NL + NL + "dans $V''$",
    r"\oldpage[0\textsubscript{IV-1}]{200}" + NL + "dans $V''$",
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the p. 199 finding that removes the blank line before the marker.")

add(200, "end of the proof of (22.4.7): 'des h_i par l'injection V''→Ω^1_{A''}⊗_{A''}K''",
    "'injection' italic (crop)",
    "l'injection (upright)",
    "italics", None, "high",
    "par l'injection",
    r"par l'\emph{injection}",
    None)

add(200, "Remarque (22.4.8), line 3: 'p un nombre premier tel que p.1∈𝔪'",
    "p.1 with a baseline period (crop at 2x)",
    "p\\cdot1 (centred dot)",
    "symbol", None, "high",
    r"$p\cdot1\in\mathfrak m$ (autrement",
    r"$p.1\in\mathfrak m$ (autrement",
    "GLOBAL_ISSUES 65.")

add(200, "Remarque (22.4.8): '(y+y')^p—x—x'', first dash",
    "long dash (crop)",
    "(y+y')^p-x",
    "convention", 7, "high",
    "(y+y')^p-x",
    r"(y+y')^p\setmin x",
    "Subtraction (GLOBAL_ISSUES 23). Does not overlap the next edit.")

add(200, "Remarque (22.4.8): '(y+y')^p—x—x'', second dash",
    "long dash (crop)",
    "-x'",
    "convention", 7, "high",
    "-x'$ et",
    r"\setmin x'$ et",
    "Subtraction (GLOBAL_ISSUES 23).")

add(200, "Remarque (22.4.8): '(yy')^p—xx''",
    "long dash (crop)",
    "(yy')^p-xx'",
    "convention", 7, "high",
    "(yy')^p-xx'",
    r"(yy')^p\setmin xx'",
    "Subtraction (GLOBAL_ISSUES 23).")

add(200, "Remarque (22.4.8): 'pour 1⩽i⩽p—1. L'application'",
    "long dash (crop); the exponent in pt^{p−1} further down has the short minus",
    "p-1",
    "convention", 7, "high",
    r"i\leqslant p-1$",
    r"i\leqslant p\setmin 1$",
    "Subtraction (GLOBAL_ISSUES 23).")

add(200, "Remarque (22.4.8): 'il suffit (20.4.8) de définir une K-dérivation'",
    "'dérivation' italic (crop)",
    "$K$-dérivation (upright in a roman reading of the remark)",
    "italics", None, "high",
    "$K$-dérivation",
    r"$K$-\emph{dérivation}",
    None)

add(200, "Remarque (22.4.8): 'Pour cela, il suffit de définir une A-dérivation'",
    "'dérivation' italic (crop); the later 'donc D est une A-dérivation' is roman",
    "$A$-dérivation (upright)",
    "italics", None, "high",
    "définir une $A$-dérivation",
    r"définir une $A$-\emph{dérivation}",
    None)

add(200, "Remarque (22.4.8): 'ne dépend que de la classe j(y) mod. pA de x'",
    "'classe' italic (crop)",
    "la classe (upright)",
    "italics", None, "high",
    "de la classe $j(y)$",
    r"de la \emph{classe} $j(y)$",
    None)

add(200, "Remarque (22.4.8): 'puisque p.1∈𝔪. On peut donc prendre'",
    "p.1 with a baseline period (crop at 2.5x)",
    "p\\cdot1 (centred dot)",
    "symbol", None, "high",
    r"$p\cdot1\in\mathfrak m$. On peut",
    r"$p.1\in\mathfrak m$. On peut",
    "GLOBAL_ISSUES 65.")

add(200, "Remarque (22.4.8), after the display D(y)=d_A x⊗1_K: 'Le fait que D est une dérivation'",
    "new indented paragraph",
    "no blank line after \\]: same paragraph, no indent",
    "other", None, "high",
    r"\]" + NL + "Le fait que $D$",
    r"\]" + NL + NL + "Le fait que $D$",
    "Missing paragraph break after a display.")

add(200, "end of p. 200: page break inside the sentence '... si l'on a de plus t∈𝔪, on a | D(ty)=tD(y)=0 puisque ...'",
    "p. 201 begins flush left with 'D(ty)=tD(y)=0 puisque': same sentence (checked on the p. 201 strip)",
    "blank line before \\oldpage{201} (and another after it, in p. 201's segment): paragraph break",
    "other", None, "high",
    r"$t\in\mathfrak m$, on a" + NL + NL,
    r"$t\in\mathfrak m$, on a" + NL,
    "Spurious paragraph break (GLOBAL_ISSUES 20). Apply together with the removal of the blank line AFTER \\oldpage{201}, which lies in page_201.tex (outside pp. 196-200): '\\oldpage[0\\textsubscript{IV-1}]{201}\\n\\n$D(ty)' -> '\\oldpage[0\\textsubscript{IV-1}]{201}\\n$D(ty)'.")

# ---------------- validation ----------------
texts = {}
for p in range(196, 201):
    with open(os.path.join(RUN, f"page_{p}.tex"), "rb") as fh:
        texts[p] = fh.read().decode("utf-8").replace("\r\n", "\n")

bad = 0
for i, f in enumerate(F):
    fx = f["fix"]
    if fx is None:
        continue
    n = texts[f["page"]].count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", i, f["page"], n, repr(fx["old"]))
    if fx["old"] == fx["new"]:
        bad += 1
        print("NO CHANGE", i)

# sequential application check per page (in listed order)
for p in range(196, 201):
    t = texts[p]
    for f in F:
        if f["page"] != p or f["fix"] is None:
            continue
        o = f["fix"]["old"]
        if t.count(o) != 1:
            bad += 1
            print("SEQ FAIL", p, repr(o))
        t = t.replace(o, f["fix"]["new"], 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)

from collections import Counter
c = Counter()
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    c[(f["page"], k)] += 1
for p in range(196, 201):
    print(p, c[(p, "normal")], c[(p, "convention")], c[(p, "misprint")])
print("total", len(F), "problems", bad)
