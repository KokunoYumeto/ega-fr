# Builds findings_121_125.json and checks every fix (uniqueness, sequential application).
import json, sys, os

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RUN, 'findings_121_125.json')

def T(s):
    return s.replace('¶', '\n')

F = []
def add(page, where, scan, tex, kind, conv, conf, old=None, new=None, note='', corrected=None, nofix=False):
    d = {'page': page, 'where': where, 'scan': scan, 'tex': T(tex), 'kind': kind,
         'convention': conv, 'confidence': conf,
         'fix': None if nofix else {'old': T(old), 'new': T(new)}}
    if corrected is not None:
        d['corrected'] = T(corrected)
    d['note'] = note
    F.append(d)

KNOTE = ("Fraktur K: the print has 𝔎 (same glyph as the 𝔎 of pp. 52-54, GLOBAL_ISSUES 63; the ideals come as the "
         "pair (𝔍, 𝔎)). All 45 \\mathfrak{R} on pp. 122 and 125 are 𝔎 in the print (31 on p. 122, 14 on p. 125); "
         "none is a genuine Fraktur R, and pp. 121, 123, 124 have none. Apply all of them together.")

C7NOTE = "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin as in the earlier fixes, pending the convention-7 decision."

# ---------------- p. 121 ----------------
add(121, "(20.2.3.1), second line: the arrow before Exalcom_B(C, L)",
    "→ with ∂ above it (the label ∂ is repeated at the start of the continuation line)",
    r"&\to\operatorname{Exalcom}_B(C,L) (no label)", 'formula', None, 'high',
    r"&\to\operatorname{Exalcom}_B(C,L)", r"&\xrightarrow{\partial}\operatorname{Exalcom}_B(C,L)",
    "Same in (20.3.6.1) and (20.3.7.1) on p. 123.")
add(121, "Corollaire (20.2.4), line 1: '(resp. (20.2.3)), on a une'",
    "'(resp.' upright in the italic statement", r"(resp. inside the italic corollary environment",
    'convention', 6, 'high', r"(resp.¶\sref{0.20.2.3-fr})", r"\textup{(resp.}¶\sref{0.20.2.3-fr})")
add(121, "Corollaire (20.2.4): '(resp.' on its own line before (20.2.4.2)",
    "'(resp.' upright", r"(resp. inside the italic corollary environment",
    'convention', 6, 'high', r"(resp.¶\begin{equation}", r"\textup{(resp.}¶\begin{equation}")
add(121, "after (20.2.4.2): 'Cela résulte de la définition de Exan_{B/A}(C, L) (resp. Exalcom_{B/A}(C, L)) ((18.3.7) et (18.4.2)).'",
    "roman (the proof), continuing flush left after the display",
    r"the sentence is inside \begin{corollary}...\end{corollary}, so it is set italic", 'italics', None, 'high',
    r"\end{equation}¶Cela résulte de la définition de $\operatorname{Exan}_{B/A}(C,L)$ (resp.¶$\operatorname{Exalcom}_{B/A}(C,L)$) ((18.3.7) et (18.4.2)).¶\end{corollary}",
    r"\end{equation}¶\end{corollary}¶\noindent Cela résulte de la définition de $\operatorname{Exan}_{B/A}(C,L)$ (resp.¶$\operatorname{Exalcom}_{B/A}(C,L)$) ((18.3.7) et (18.4.2)).",
    "Moves \\end{corollary} before the proof sentence (as in the (16.4.5) fix); \\noindent because the print does not indent it. Its 'resp.' is then upright, as printed. No \\begin{proof}: the print has no heading here.")
add(121, "diagram of Remarque (20.2.5), bottom row: arrow Dér_{A'}(B', L) → Exan_{B'}(C', L)",
    "∂ below the arrow", r"\ar[r]^-\partial (label above)", 'other', None, 'high',
    r"(B',L) \ar[r]^-\partial", r"(B',L) \ar[r]_-\partial",
    "Label side (cf. GLOBAL_ISSUES 30); in the top row ∂ is above, as in the TeX.")
add(121, "Remarque (20.2.5): 'Alors on a un diagramme commutatif'",
    "new indented paragraph after the first diagram", r"no blank line after \]: the paragraph continues",
    'other', None, 'high', r"\]¶Alors on a", r"\]¶¶Alors on a")
add(121, "heading of 20.3",
    "20.3. Dérivations continues dans les anneaux topologiques.", r"\subsection{Dérivations continues dans les anneaux topologiques}",
    'punctuation', None, 'high',
    r"\subsection{Dérivations continues dans les anneaux topologiques}",
    r"\subsection{Dérivations continues dans les anneaux topologiques.}",
    "Printed final full stop (GLOBAL_ISSUES 43/58; page fix as for 18.1 and 18.2).")
add(121, "(20.3.1): 'la catégorie des A-anneaux topologiques se définit'",
    "A-*anneaux topologiques* (italic)", "upright", 'italics', None, 'high',
    r"des $A$-anneaux topologiques se définit", r"des $A$-\emph{anneaux topologiques} se définit")
add(121, "end of the page-121 text, mid-sentence ('; si B / et C sont deux A-anneaux topologiques'); affects the first line of p. 122",
    "p. 122 begins 'et C sont deux ...' at the left margin: the sentence continues",
    r"blank line between 'si $B$' and the page-122 marker (paragraph break)", 'other', None, 'high',
    r"continu » ; si $B$¶¶", r"continu » ; si $B$¶",
    "Removes the blank line before \\oldpage[0\\textsubscript{IV-1}]{122} (GLOBAL_ISSUES 20); the edit lies in the page-121 segment.")

# ---------------- p. 122 ----------------
K122 = [
    ("proof of (20.3.3), line 1: 'si 𝔎 est un idéal bilatère ouvert'", r"si $\mathfrak{R}$ est un idéal"),
    ("proof of (20.3.3): 'D(𝔎²)⊂𝔎.D(𝔎)+D(𝔎).𝔎=0'", r"$D(\mathfrak{R}^2)\subset\mathfrak{R}.D(\mathfrak{R})+¶D(\mathfrak{R}).\mathfrak{R}=0$"),
    ("(20.3.5.1): 'Dér_{A/𝔍}(B/𝔎, L)'", r"(B/\mathfrak{R},L)\xrightarrow{\sim}"),
    ("(20.3.5): 'des couples (𝔍, 𝔎)'", r"$(\mathfrak{J},\mathfrak{R})$"),
    ("(20.3.5): 'tels que 𝔎.L=L.𝔎=0, 𝔍.B⊂𝔎, B.𝔍⊂𝔎'", r"tels que $\mathfrak{R}.L=L.\mathfrak{R}=0$,¶$\mathfrak{J}.B\subset\mathfrak{R}$,¶$B.\mathfrak{J}\subset\mathfrak{R}$."),
    ("proof of (20.3.5), line 1: 'Comme A/𝔍 et B/𝔎 sont discrets'", r"et $B/\mathfrak{R}$ sont discrets"),
    ("proof of (20.3.5), line 2: 'w_{𝔍,𝔎} : Dér_{A/𝔍}(B/𝔎, L)'", r"$w_{\mathfrak{J},\mathfrak{R}}:¶\operatorname{D\acute{e}r}_{A/\mathfrak{J}}(B/\mathfrak{R},L)"),
    ("proof of (20.3.5): 'B/𝔎'→B/𝔎'", r"$B/\mathfrak{R}'\to B/\mathfrak{R}$"),
    ("proof of (20.3.5): 'pour 𝔎⊃𝔎''", r"$\mathfrak{R}\supset\mathfrak{R}'$"),
    ("proof of (20.3.5): 'Dér_{A/𝔍}(B/𝔎, L)→Dér_{A/𝔍}(B/𝔎', L)'", r"(B/\mathfrak{R},L)\to¶\operatorname{D\acute{e}r}_{A/\mathfrak{J}}(B/\mathfrak{R}',L)$"),
    ("proof of (20.3.5): '(avec 𝔎.L=L.𝔎=0, 𝔍.B⊂𝔎', B.𝔍⊂𝔎')'", r"(avec¶$\mathfrak{R}.L=L.\mathfrak{R}=0$,¶$\mathfrak{J}.B\subset\mathfrak{R}'$,¶$B.\mathfrak{J}\subset\mathfrak{R}'$)"),
    ("proof of (20.3.5): 'Dér_{A/𝔍}(B/𝔎, L)→Dér_{A/𝔍'}(B/𝔎, L)'", r"(B/\mathfrak{R},L)\to¶\operatorname{D\acute{e}r}_{A/\mathfrak{J}'}(B/\mathfrak{R},L)$"),
    ("proof of (20.3.5): 'un idéal bilatère ouvert 𝔎_0 de B'", r"$\mathfrak{R}_0$ de $B$"),
    ("proof of (20.3.5): '𝔍_0B⊂𝔎_0 et B𝔍_0⊂𝔎_0'", r"$\mathfrak{J}_0B\subset\mathfrak{R}_0$ et¶$B\mathfrak{J}_0\subset\mathfrak{R}_0$"),
    ("proof of (20.3.5), last line: 'de B/𝔎_0 dans L'", r"$B/\mathfrak{R}_0$ dans"),
]
for where, old in K122:
    add(122, where, "𝔎 (Fraktur K)", r"\mathfrak{R}", 'symbol', None, 'high',
        old, old.replace(r'\mathfrak{R}', r'\mathfrak{K}'), KNOTE)

add(122, "proof of (20.3.3): '... .𝔎=0 (20.1.1.1) donc D est continue.'",
    "no comma after (20.1.1.1)", r"\sref{0.20.1.1.1-fr}, donc", 'punctuation', None, 'high',
    r"\sref{0.20.1.1.1-fr}, donc", r"\sref{0.20.1.1.1-fr} donc", "2.5x crop.")
add(122, "proof of (20.3.5): 'est surjectif pour 𝔎⊃𝔎' il résulte aussitôt'",
    "no comma after 𝔎⊃𝔎'", r"$\mathfrak{R}\supset\mathfrak{R}'$, il résulte", 'punctuation', None, 'high',
    r", il résulte aussitôt", r" il résulte aussitôt", "2.5x crop.")
add(122, "Proposition (20.3.5): 'des couples (𝔍, 𝔎) d'idéaux bilatères tels que'",
    "d'idéaux bilatères (without 'ouverts')", r"d'idéaux bilatères (keeps the printed reading)",
    'misprint_in_print', None, 'low', nofix=True,
    corrected=r"d'idéaux bilatères ouverts",
    note=("The TeX keeps the printed reading. The pairs must consist of open ideals: the proof begins 'Comme A/𝔍 et B/𝔎 sont "
          "discrets', and with all ideals the pair (0, 0) would make the limit Dér_A(B, L). Authors' omission, not in the "
          "authors' errata (Err_IV); for the corrected edition only, if accepted."))

# ---------------- p. 123 ----------------
add(123, "(20.3.6.1), second line: the arrow before Exantop_B(C, L)",
    "→ with ∂ above it (label repeated at the start of the continuation line)",
    r"&\to\operatorname{Exantop}_B(C,L) (no label)", 'formula', None, 'high',
    r"&\to\operatorname{Exantop}_B(C,L)", r"&\xrightarrow{\partial}\operatorname{Exantop}_B(C,L)")
add(123, "(20.3.7.1), second line: the arrow before Exalcotop_B(C, L)",
    "→ with ∂ above it (label repeated at the start of the continuation line)",
    r"&\to\operatorname{Exalcotop}_B(C,L) (no label)", 'formula', None, 'high',
    r"&\to\operatorname{Exalcotop}_B(C,L)", r"&\xrightarrow{\partial}\operatorname{Exalcotop}_B(C,L)")
add(123, "Corollaire (20.3.8), line 1: '(resp. (20.3.6)) on a une suite'",
    "'(resp.' upright in the italic statement", r"(resp. inside the italic corollary environment",
    'convention', 6, 'high', r"(resp.¶\sref", r"\textup{(resp.}¶\sref")
add(123, "Corollaire (20.3.8), line 1: 'Sous les hypothèses de (20.3.5) (resp. (20.3.6))'",
    "(20.3.5) (resp. (20.3.6))",
    r"\sref{0.20.3.5-fr} \textup{(resp.}¶\sref{0.20.3.6-fr}) (keeps the printed reading)",
    'misprint_in_print', None, 'high', nofix=True,
    corrected=r"\sref{0.20.3.6-fr} \textup{(resp.}¶\sref{0.20.3.7-fr})",
    note=("The TeX keeps the printed reading. Wrong references, off by one: (20.3.5) concerns lim Dér_{A/𝔍}(B/𝔎, L) and has "
          "no C, u, v; the sequences (20.3.8.1) (Exantop) and (20.3.8.2) (Exalcotop) need the hypotheses of (20.3.6) (resp. "
          "(20.3.7)), exactly as (20.2.4) cites (20.2.2) (resp. (20.2.3)). Not in the authors' errata. 'tex' is the text "
          "after the convention-6 fix just above; apply that first."))
add(123, "Corollaire (20.3.8): '(resp.' on its own line before (20.3.8.2)",
    "'(resp.' upright", r"(resp. inside the italic corollary environment",
    'convention', 6, 'high', r"(resp.¶\begin{equation}", r"\textup{(resp.}¶\begin{equation}")
add(123, "heading of 20.4",
    "20.4. Parties principales et différentielles.", r"\subsection{Parties principales et différentielles}",
    'punctuation', None, 'high',
    r"\subsection{Parties principales et différentielles}",
    r"\subsection{Parties principales et différentielles.}",
    "Printed final full stop (GLOBAL_ISSUES 43/58).")
add(123, "opening sentence of 20.4: 'Dans toute la suite de ce paragraphe ... tous les anneaux sont supposés commutatifs.'",
    "the whole sentence italic (including 'commutatifs')", r"roman sentence with \emph{commutatifs}",
    'italics', None, 'high',
    r"Dans toute la suite de ce paragraphe et dans les trois suivants, tous les¶anneaux sont supposés \emph{commutatifs}.",
    r"\textit{Dans toute la suite de ce paragraphe et dans les trois suivants, tous les¶anneaux sont supposés commutatifs.}",
    "1.2x crop.")

# ---------------- p. 124 ----------------
add(124, "Définition (20.4.2): 'B-algèbre augmentée des parties principales d'ordre 1 de B par rapport à A'",
    "italic like the rest of the statement (no change of face)",
    r"\emph{...} inside the italic definition environment (comes out upright)", 'convention', 6, 'high',
    r"\emph{$B$-algèbre augmentée des parties principales d'ordre $1$ de¶$B$ par rapport à $A$}",
    r"$B$-algèbre augmentée des parties principales d'ordre $1$ de¶$B$ par rapport à $A$")
add(124, "after Définition (20.4.2): 'Comme p(b⊗1)=b par définition, il est clair que ε est bien une augmentation de B-algèbre.'",
    "new indented paragraph in roman (outside the statement)",
    r"inside \begin{definition}...\end{definition}, so it is set italic", 'italics', None, 'high',
    r"par passage au quotient.¶¶Comme $p(b\otimes1)=b$ par définition, il est clair que $\varepsilon$ est¶bien une augmentation de $B$-algèbre.¶\end{definition}",
    r"par passage au quotient.¶\end{definition}¶¶Comme $p(b\otimes1)=b$ par définition, il est clair que $\varepsilon$ est¶bien une augmentation de $B$-algèbre.",
    "The definition environment runs on over the roman sentence (GLOBAL_ISSUES 58). Apply before the misprint fix that follows (its 'old' lies inside this one).")
add(124, "same sentence: 'de B-algèbre.'",
    "B-*algèbre.* with 'algèbre' italic in the roman sentence (wrong fount)",
    r"$B$-algèbre. (no change of face; silently corrected once the sentence is roman)", 'misprint_in_print', None, 'medium',
    r"une augmentation de $B$-algèbre.", r"une augmentation de $B$-\emph{algèbre}.",
    corrected=r"une augmentation de $B$-algèbre.",
    note="2x crop: 'de B-' roman, 'algèbre.' italic. Wrong-fount word (GLOBAL_ISSUES 29), reproduced in the diplomatic text. Apply after the previous finding.")
add(124, "Définition (20.4.3): 'le B-module des 1-différentielles (ou simplement des différentielles) de B'",
    "'1-différentielles' and 'différentielles' italic like the statement; '(ou simplement des' upright",
    r"\emph{$1$-différentielles} and \emph{différentielles} come out upright; '(ou simplement des' italic",
    'convention', 6, 'high',
    r"\emph{$1$-différentielles} (ou simplement des \emph{différentielles}) de $B$",
    r"$1$-différentielles \textup{(ou simplement des} différentielles) de $B$",
    "Both halves of convention 6 in one edit (1.1x crop).")
C7_124 = [
    ("Lemme (20.4.4): '1⊗s—s⊗1'", r"1\otimes s-s\otimes1"),
    ("proof of (20.4.4), line 1: 'x⊗1—1⊗x∈𝔍'", r"x\otimes1-1\otimes x\in"),
    ("proof of (20.4.4), line 2: '(1⊗y—y⊗1)'", r"(1\otimes y-y\otimes1)"),
    ("(20.4.4.1): '(1⊗y_i—y_i⊗1)'", r"(1\otimes y_i-y_i\otimes1)"),
    ("proof of (20.4.4): 'engendré par les éléments 1⊗x—x⊗1'", r"1\otimes x-x\otimes1"),
    ("(20.4.4.2): 'x⊗1—1⊗x=' (left-hand side)", r"x\otimes1-1\otimes x="),
    ("(20.4.4.2): '(t⊗1—1⊗t)'", r"(t\otimes1-1\otimes t)"),
    ("(20.4.4.2): '(s⊗1—1⊗s)'", r"(s\otimes1-1\otimes s)"),
]
for where, old in C7_124:
    add(124, where, "long dash for the minus sign", "-", 'convention', 7, 'high',
        old, old.replace('-', r'\setmin ', 1), C7NOTE)
add(124, "end of the page-124 text, mid-sentence ('la topologie induite sur 𝔍=𝔍_{B/A} / par celle de B⊗_A B'); affects the first line of p. 125",
    "p. 125 begins 'par celle de B⊗_A B est moins fine ...' at the left margin: the sentence continues",
    r"blank line between '$\mathfrak{J}=\mathfrak{J}_{B/A}$' and the page-125 marker (paragraph break)", 'other', None, 'high',
    r"$\mathfrak{J}=\mathfrak{J}_{B/A}$¶¶", r"$\mathfrak{J}=\mathfrak{J}_{B/A}$¶",
    "Removes the blank line before \\oldpage[0\\textsubscript{IV-1}]{125} (GLOBAL_ISSUES 20); the edit lies in the page-124 segment.")

# ---------------- p. 125 ----------------
C7_125 = [
    ("display before 'dans le B-module': '(xy)⊗z—x⊗(yz)'", r"z-x\otimes(yz)", r"z\setmin x\otimes(yz)"),
    ("same display: '(1⊗z)(y⊗1—1⊗y)'", r"(y\otimes1-1\otimes y)\\", r"(y\otimes1\setmin 1\otimes y)\\"),
    ("same display: 'xz.(y⊗1—1⊗y)'", r"xz.(y\otimes1-1\otimes y)", r"xz.(y\otimes1\setmin 1\otimes y)"),
    ("same display: '—x.(z⊗1 ...'", r"-x.(", r"\setmin x.("),
    ("same display: '(z⊗1—1⊗z)'", r"(z\otimes1-1\otimes z)", r"(z\otimes1\setmin 1\otimes z)"),
    ("same display, last factor: '(y⊗1—1⊗y)'", r"(y\otimes1-1\otimes y)¶\end{aligned}", r"(y\otimes1\setmin 1\otimes y)¶\end{aligned}"),
    ("(20.4.6.1): 'd_{B/A}=p_1—p_2'", r"p_1-p_2", r"p_1\setmin p_2"),
    ("proof of (20.4.7): 'x⊗1—1⊗x dans Ω^1_{B/A}'", r"x\otimes1-1\otimes x$ dans", r"x\otimes1\setmin 1\otimes x$ dans"),
]
for where, old, new in C7_125:
    add(125, where, "long dash for the minus sign", "-", 'convention', 7, 'high', old, new, C7NOTE)

K125 = [
    ("proof of (20.4.5): 'que, si 𝔎 est un idéal de B'", r"si $\mathfrak{R}$ est un idéal de"),
    ("proof of (20.4.5), display: '((𝔎²⊗B)+(B⊗𝔎²))∩𝔍⊂(𝔎⊗𝔎)∩𝔍+𝔎𝔍+𝔍²'",
     r"((\mathfrak{R}^2\otimes B)+(B\otimes\mathfrak{R}^2))\cap\mathfrak{J}¶  \subset(\mathfrak{R}\otimes\mathfrak{R})\cap\mathfrak{J}¶  +\mathfrak{R}\mathfrak{J}+\mathfrak{J}^2"),
    ("proof of (20.4.5): 'des éléments de 𝔎 tels que'", r"éléments de $\mathfrak{R}$ tels"),
    ("proof of (20.4.5): 'Σ(x_i⊗y_i)∈𝔎𝔍'", r"\in\mathfrak{R}\mathfrak{J}$, si bien"),
    ("(20.4.5.1)", r"(\mathfrak{R}^2\otimes B+B\otimes\mathfrak{R}^2)\cap\mathfrak{J}¶  \subset\mathfrak{R}\mathfrak{J}+\mathfrak{J}^2."),
    ("proof of (20.4.5): 'les ensembles (𝔎⊗B+B⊗𝔎)∩𝔍'", r"$(\mathfrak{R}\otimes B+B\otimes\mathfrak{R})\cap\mathfrak{J}$"),
    ("proof of (20.4.5): 'où 𝔎 parcourt'", r"$\mathfrak{R}$ parcourt"),
]
for where, old in K125:
    add(125, where, "𝔎 (Fraktur K)", r"\mathfrak{R}", 'symbol', None, 'high',
        old, old.replace(r'\mathfrak{R}', r'\mathfrak{K}'), KNOTE)

add(125, "Définition (20.4.6): 'ε∘p_1=ε∘p_2=1_B'",
    "1_B: the old-style figure one (as in x⊗1)", r"\mathrm{I}_B (capital I)", 'symbol', None, 'high',
    r"=\mathrm{I}_B$", r"=1_B$",
    "Identity map 1_B; the glyph is the print's old-style 1, smaller than the capitals (2.5x crop). ega0-20-fr.tex writes \\mathrm{I}_X for the identity 12 times.")
add(125, "(20.4.6.1): 'd_{B/A}=p_1—p_2'",
    "d_{B/A}=p_1—p_2", r"d_{B/A}=p_1\setmin p_2 (keeps the printed reading)", 'misprint_in_print', None, 'high',
    nofix=True, corrected=r"d_{B/A}=p_2\setmin p_1",
    note=("Authors' errata Err_IV 12 (IV part 4, p. 347). The errata line reads 'remplacer p_2—p_1 par p_1—p_2', the "
          "reverse of the print, which has p_1—p_2; its second half (p. 125: 1⊗x—x⊗1) and Err_IV 13 (p. 126: p_1=p_2—d_{B/A}) "
          "both give d_{B/A}=p_2—p_1, so that is the corrected reading. 'tex' is the text after the convention-7 fix of "
          "this formula; apply that first."))
add(125, "Définition (20.4.6): 'la différentielle extérieure de B relative à A'",
    "italic like the statement (no change of face)", r"\emph{...} inside the italic definition (comes out upright)",
    'convention', 6, 'high',
    r"\emph{différentielle extérieure de $B$ relative à $A$}", r"différentielle extérieure de $B$ relative à $A$")
add(125, "Définition (20.4.6): 'la différentielle de x (relativement à A)'",
    "italic like the statement (no change of face)", r"\emph{différentielle de $x$} (comes out upright)",
    'convention', 6, 'high', r"\emph{différentielle de $x$}", r"différentielle de $x$")
add(125, "proof of (20.4.7): 'l'image canonique de x⊗1—1⊗x' (line 10 from the bottom)",
    "x⊗1—1⊗x", r"$x\otimes1\setmin 1\otimes x$ dans (keeps the printed reading)", 'misprint_in_print', None, 'high',
    nofix=True, corrected=r"$1\otimes x\setmin x\otimes1$ dans",
    note=("Authors' errata Err_IV 12 (IV part 4, p. 347): 'ligne 10 du bas de la p. 125, remplacer x⊗1—1⊗x par 1⊗x—x⊗1'. "
          "'tex' is the text after the convention-7 fix of this formula; apply that first."))
add(125, "Théorème (20.4.8) (ii): 'l'application u⇝u∘d_{B/A}'",
    "wavy arrow ⇝", r"\mapsto", 'symbol', None, 'high',
    r"u\mapsto u\circ d_{B/A}", r"u\leadsto u\circ d_{B/A}", "Wavy arrow (GLOBAL_ISSUES 33).")

# ---------------- checks ----------------
ok = True
pages = sorted(set(f['page'] for f in F))
for p in pages:
    src = open(os.path.join(RUN, 'page_%03d.tex' % p), encoding='utf-8', newline='').read()
    src = src.replace('\r\n', '\n')  # page files are CRLF; the release files use LF
    assert '\r' not in src
    cur = src
    SRCFILE = os.path.join(os.path.dirname(RUN), 'ega-fr', 'editions', '2026-10-24-r20', 'current', 'packages',
                           'IV1', 'native', 'ega4', 'ega0-20-fr.tex')
    full = open(SRCFILE, encoding='utf-8', newline='').read()
    for f in [x for x in F if x['page'] == p and x['fix'] is not None]:
        if f['fix']['old'] not in full:
            print('INFO: old not in ega0-20-fr.tex as is (may follow an earlier fix):', p, repr(f['fix']['old'][:60]))
    for f in [x for x in F if x['page'] == p]:
        if f['fix'] is not None:
            o = f['fix']['old']
            n0 = src.count(o)
            if n0 != 1:
                ok = False; print('NOT UNIQUE in original', p, n0, repr(o))
            n1 = cur.count(o)
            if n1 != 1:
                ok = False; print('NOT UNIQUE in sequence', p, n1, repr(o))
            cur = cur.replace(o, f['fix']['new'], 1)
        else:
            t = f['tex'].replace(' (keeps the printed reading)', '')
            if cur.count(t) != 1:
                ok = False; print('misprint tex not found once', p, repr(t))
    # all \mathfrak{R} gone after the fixes?
    print('page', p, 'mathfrak{R} before', src.count(r'\mathfrak{R}'), 'after', cur.count(r'\mathfrak{R}'))

# strip the explanatory suffix used only for the check from misprint 'tex' fields
for f in F:
    if f['fix'] is None:
        f['tex'] = f['tex'].replace(' (keeps the printed reading)', '')

cnt = {}
for f in F:
    c = cnt.setdefault(f['page'], [0, 0, 0])
    if f['kind'] == 'misprint_in_print': c[2] += 1
    elif f['kind'] == 'convention': c[1] += 1
    else: c[0] += 1
print('counts normal/convention/misprint:', cnt)
print('all checks ok' if ok else 'CHECKS FAILED')
if ok:
    json.dump(F, open(OUT, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    print('wrote', OUT, len(F))
