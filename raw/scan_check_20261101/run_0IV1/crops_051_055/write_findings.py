import json, os, sys

RUN = r"user\Documents\ega_scan_check_20261101\run_0IV1"
OUT = os.path.join(RUN, "findings_051_055.json")


def N(s):
    """'⏎' stands for a line break in the TeX."""
    return None if s is None else s.replace("\u23ce", "\n")


F = []


def add(page, where, scan, tex, kind, conv, conf, old=None, new=None, corrected=None, note=""):
    d = {"page": page, "where": where, "scan": scan, "tex": N(tex), "kind": kind,
         "convention": conv, "confidence": conf,
         "fix": None if old is None else {"old": N(old), "new": N(new)}}
    if kind == "misprint_in_print":
        d["corrected"] = N(corrected)
    d["note"] = note
    F.append(d)


LETTER = ("Fraktur K: the kernel of g / augmentation ideal is printed 𝔎 throughout 18.1.3-18.1.7 (same glyph as the "
          "𝔎 of EGA I p. 184, transcribed \\mathfrak{K} there; the print's slip 'y∈K' with a roman K on p. 52 confirms "
          "the letter). The TeX writes \\mathfrak{R} (ℜ) at all 28 occurrences in ega0-18-fr.tex (pp. 52: 10, 53: 4, "
          "54: 9, 56: 5); apply all of them together.")

# ---------------- page 51 ----------------
add(51, "proof of Corollaire (17.3.9), lines 5-6",
    "S' est une partie multiplicative de B' et C est un anneau quotient de S'^{-1}B'",
    r"et $C$ est un anneau quotient de⏎$S'^{-1}B'$",
    "misprint_in_print", None, "medium",
    corrected=r"et $S^{-1}C$ est un anneau quotient de⏎$S'^{-1}B'$",
    note=("The TeX keeps the printed reading. C is a quotient of B', but it is S^{-1}C that is a quotient of "
          "S'^{-1}B' (localize B'→C at S'), and the sentence goes on to use exactly that ('tout revient à voir que "
          "lorsque C est régulier, il en est de même de S^{-1}C'). Not in the authors' errata (Liste 3)."))

add(51, "heading of 18.1 (ega0-18-fr.tex, before its first page marker)",
    "18.1. Images réciproques d'anneaux augmentés.",
    r"\subsection{Images réciproques d'anneaux augmentés}",
    "punctuation", None, "high",
    r"\subsection{Images réciproques d'anneaux augmentés}",
    r"\subsection{Images réciproques d'anneaux augmentés.}",
    note=("Printed final full stop. None of the 52 \\subsection titles in ega0-14-fr.tex ... ega0-23-fr.tex has it "
          "(cf. GLOBAL_ISSUES 43). This text lies in ega0-18-fr.tex before its first marker."))

add(51, "diagram (18.1.1.1) (ega0-18-fr.tex, before its first page marker)",
    "A centred below B and C; A→B (ρ, lower left) and A→C (σ, lower right) are both oblique",
    r"A placed under C, so \ar[u]_\sigma is a vertical arrow",
    "other", None, "medium",
    r"B\ar[r]^u & C\\⏎    & A\ar[lu]^\rho\ar[u]_\sigma",
    r"B\ar[rr]^u & & C\\⏎    & A\ar[lu]^\rho\ar[ru]_\sigma",
    note=("Shape of the triangle only; objects, arrows and label sides already agree. This text lies in "
          "ega0-18-fr.tex before its first marker."))

# ---------------- page 52 ----------------
add(52, "(18.1.2): structure of A-anneau on G",
    "l'homomorphisme α→(ρ(α), σ(α)) (plain arrow)", r"$\alpha\mapsto(\rho(\alpha),\sigma(\alpha))$",
    "convention", 3, "high", r"$\alpha\mapsto(", r"$\alpha\to(")

add(52, "(18.1.2), last line", "(0_III, 8.1.9) with a bold 0", r"($0_{\mathrm{III}}$, 8.1.9)",
    "convention", 2, "high", r"($0_{\mathrm{III}}$, 8.1.9)", r"($\mathbf{0}_{\mathrm{III}}$, 8.1.9)")

add(52, "(18.1.3): 'si 𝔎 est le noyau de g, le noyau 𝔎' de p_1'", "𝔎, 𝔎' (Fraktur K)",
    r"\mathfrak{R}, \mathfrak{R}'", "symbol", None, "high",
    r"si $\mathfrak{R}$ est le noyau de⏎$g$, le noyau $\mathfrak{R}'$ de",
    r"si $\mathfrak{K}$ est le noyau de⏎$g$, le noyau $\mathfrak{K}'$ de", note=LETTER)

add(52, "(18.1.3): 'éléments (0, y) où y∈K'", "y∈K (see the misprint finding that follows)",
    r"$y\in\mathfrak{R}$", "symbol", None, "high",
    r"$y\in\mathfrak{R}$", r"$y\in\mathfrak{K}$",
    note=("Letter fix for both editions (𝔎 is the intended letter); the next finding then restores the printed "
          "roman K in the diplomatic text."))

add(52, "(18.1.3): 'éléments (0, y) où y∈K'",
    "y∈K with a roman K (wrong fount for the Fraktur 𝔎 used everywhere else in 18.1.3)",
    r"$y\in\mathfrak{R}$ (silently corrected)", "misprint_in_print", None, "high",
    r"$y\in\mathfrak{K}$", r"$y\in K$", corrected=r"$y\in\mathfrak{K}$",
    note="Apply after the previous finding (this 'old' is the text after that fix). 3x crop: plain roman K.")

add(52, "(18.1.3): 'i_2: 𝔎'→𝔎'", "𝔎', 𝔎", r"\mathfrak{R}', \mathfrak{R}", "symbol", None, "high",
    r"$i_2:\mathfrak{R}'\to\mathfrak{R}$", r"$i_2:\mathfrak{K}'\to\mathfrak{K}$", note=LETTER)

add(52, "(18.1.3): '𝔍×𝔎=𝔍'⊕𝔎''", "𝔎, 𝔎'", r"\mathfrak{R}, \mathfrak{R}'", "symbol", None, "high",
    r"$\mathfrak{J}\times\mathfrak{R}=\mathfrak{J}'\oplus\mathfrak{R}'$",
    r"$\mathfrak{J}\times\mathfrak{K}=\mathfrak{J}'\oplus\mathfrak{K}'$", note=LETTER)

add(52, "diagram (18.1.3.1), vertex 𝔍'⊕𝔎'", "𝔎'", r"\mathfrak{R}'", "symbol", None, "high",
    r"\mathfrak{J}'\oplus\mathfrak{R}'\ar[r]", r"\mathfrak{J}'\oplus\mathfrak{K}'\ar[r]", note=LETTER)

add(52, "diagram (18.1.3.1), vertex 𝔎' (top row)", "𝔎'", r"\mathfrak{R}'", "symbol", None, "high",
    r"& \mathfrak{R}'\ar[r]", r"& \mathfrak{K}'\ar[r]", note=LETTER)

add(52, "diagram (18.1.3.1), vertex 𝔎 (top right)", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"& \mathfrak{R}\ar[d]", r"& \mathfrak{K}\ar[d]", note=LETTER)

add(52, "diagram (18.1.3.1), arrow 𝔎'→𝔎",
    "isomorphism arrow: tilde above the arrow, i_2 above the tilde",
    r"\ar[r]^{i_2}_{\sim} (tilde below the arrow)", "symbol", None, "high",
    r"^{i_2}_{\sim}", r"^{\overset{i_2}{\sim}}", note="Same form as the EGA II p. 50 fix.")

add(52, "diagram (18.1.3.1), arrow 𝔎'→G", "label j left of the arrow", r"\ar[d]^j (label right)",
    "other", None, "high", r"\ar[d]^j", r"\ar[d]_j", note="Label side (cf. GLOBAL_ISSUES 30).")

add(52, "diagram (18.1.3.1), arrow 𝔎→F", "label p_2 left of the arrow", r"\ar[d]^{p_2} (label right)",
    "other", None, "high", r"\ar[d]^{p_2}", r"\ar[d]_{p_2}",
    note="Label side only; for the placement of p_2 on this arrow see the misprint finding below.")

add(52, "diagram (18.1.3.1), arrow 𝔍'→𝔍", "i_1 left of the arrow, vertical tilde ≀ right of it",
    r"\ar[d]^{i_1}_{\sim}: i_1 right, horizontal ∼ left", "symbol", None, "high",
    r"\ar[d]^{i_1}_{\sim}", r"\ar[d]_{i_1}^{\wr}")

add(52, "diagram (18.1.3.1), arrow G→E", "label p_1 left of the arrow", r"\ar[d]^{p_1} (label right)",
    "other", None, "high", r"\ar[d]^{p_1}", r"\ar[d]_{p_1}", note="Label side.")

add(52, "diagram (18.1.3.1), oblique arrow G→B", "label q below left of the arrow",
    r"\ar[dr]^q (label above right)", "other", None, "high", r"\ar[dr]^q", r"\ar[dr]_q", note="Label side.")

add(52, "diagram (18.1.3.1): label p_2",
    "p_2 labels the vertical arrow 𝔎→F (an inclusion); the arrow G→F has no label",
    r"      & \mathfrak{K}\ar[d]_{p_2}\\⏎    0\ar[r] & \mathfrak{J}'\ar[r]\ar[d]_{i_1}^{\wr}⏎      & G\ar[r]\ar[d]_{p_1}\ar[dr]_q & F\ar[d]^g\\",
    "misprint_in_print", None, "high",
    corrected=r"      & \mathfrak{K}\ar[d]\\⏎    0\ar[r] & \mathfrak{J}'\ar[r]\ar[d]_{i_1}^{\wr}⏎      & G\ar[r]^{p_2}\ar[d]_{p_1}\ar[dr]_q & F\ar[d]^g\\",
    note=("The TeX keeps the printed placement. Authors' errata, Liste 3 (EGA IV part 4, p. 345): '(0_IV, 18.1.3). "
          "Dans le diagramme (18.1.3.1), p_2 doit être à côté de la flèche G→F.' 'tex' is quoted as it reads after the "
          "letter and label fixes above; the corrected edition replaces it by 'corrected'."))

add(52, "(18.1.4): 'est appelé l'idéal d'augmentation'", "l' upright, 'idéal d'augmentation' italic",
    r"\emph{l'idéal d'augmentation}", "italics", None, "high",
    r"\emph{l'idéal d'augmentation}", r"l'\emph{idéal d'augmentation}")

add(52, "(18.1.4): 's'il existe un A-homomorphisme de A-anneaux s: B→E'",
    "A-*homomorphisme de* A-*anneaux* (italic)", "upright", "italics", None, "high",
    r"un $A$-homomorphisme de $A$-anneaux $s:B\to E$",
    r"un $A$-\emph{homomorphisme de} $A$-\emph{anneaux} $s:B\to E$")

add(52, "(18.1.4), last line: 'La suite exacte de A-bimodules'", "A-*bimodules* (italic)", "upright",
    "italics", None, "high", r"La suite exacte de $A$-bimodules", r"La suite exacte de $A$-\emph{bimodules}")

# ---------------- page 53 ----------------
add(53, "(18.1.5): 'que l'on appelle l'image réciproque par g'", "l' upright, 'image réciproque' italic",
    r"\emph{l'image réciproque}", "italics", None, "high",
    r"\emph{l'image réciproque}", r"l'\emph{image réciproque}")

add(53, "(18.1.7), line 2: 'on a évidemment sur 𝔎'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"évidemment sur⏎$\mathfrak{R}$ une", r"évidemment sur⏎$\mathfrak{K}$ une", note=LETTER)

add(53, "(18.1.7), line 2: 'une structure de G-bimodule'", "G-*bimodule* (italic)", "upright",
    "italics", None, "high",
    r"structure de $G$-bimodule, provenant", r"structure de $G$-\emph{bimodule}, provenant")

add(53, "(18.1.7), line 3: 'on a en outre une injection'", "*injection* (italic)", "upright",
    "italics", None, "high", r"en outre une injection", r"en outre une \emph{injection}")

add(53, "(18.1.7), line 4: 'θ=j∘i_2^{-1}: 𝔎→G'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"i_2^{-1}:\mathfrak{R}\to G$", r"i_2^{-1}:\mathfrak{K}\to G$", note=LETTER)

add(53, "(18.1.7), line 4: 'qui est un homomorphisme de G-bimodules'",
    "*homomorphisme de* G-*bimodules* (italic)", "upright", "italics", None, "high",
    r"qui est un homomorphisme de⏎$G$-bimodules.",
    r"qui est un \emph{homomorphisme de}⏎$G$-\emph{bimodules}.")

add(53, "(18.1.7), second paragraph: 'notés 𝔎 et 𝔍' respectivement'", "𝔎", r"\mathfrak{R}",
    "symbol", None, "high", r"notés⏎$\mathfrak{R}$ et", r"notés⏎$\mathfrak{K}$ et", note=LETTER)

add(53, "diagram (18.1.7.1), top: 0 → 𝔎 and the arrows θ: 𝔎→G, 𝔎→F",
    "0 and 𝔎 stand above F; θ runs obliquely from 𝔎 down to G (label θ above left), the vertical arrow from 𝔎 down to F",
    r"0 and \mathfrak{R} in G's column: \ar[ld]^\theta points to 𝔍', \ar[d] to G",
    "formula", None, "high",
    r"    & & 0\ar[d] & & \\⏎    & & \mathfrak{R}\ar[ld]^\theta\ar[d] & & \\",
    r"    & & & 0\ar[d] & \\⏎    & & & \mathfrak{K}\ar[ld]_\theta\ar[d] & \\",
    note=("Wrong arrow targets in the TeX (θ: 𝔎→𝔍' and 𝔎→G). The edit moves 0 and 𝔎 one column right (above F), "
          "puts θ above left of the oblique arrow, and includes the 𝔎 letter fix for this occurrence."))

add(53, "end of the page-53 text, after diagram (18.1.7.1); affects the first line of p. 54",
    "p. 54 begins 'L'homomorphisme h définit ...' at the left margin, without indent: the paragraph of (18.1.7) continues after the display",
    r"blank line between \end{equation} and the page-54 marker (new paragraph)",
    "other", None, "high",
    r"& & & 0 &⏎  }⏎\end{equation}⏎⏎", r"& & & 0 &⏎  }⏎\end{equation}⏎",
    note="Removes the blank line before \\oldpage[0\\textsubscript{IV-1}]{54}; the edit lies in the page-53 segment.")

# ---------------- page 54 ----------------
add(54, "(18.1.7) cont., line 1: '(et en particulier sur 𝔎)'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"particulier sur⏎$\mathfrak{R}$)", r"particulier sur⏎$\mathfrak{K}$)", note=LETTER)

add(54, "(18.1.7) cont., line 2: 'une structure de G-bimodule'", "G-*bimodule* (italic)", "upright",
    "italics", None, "high",
    r"une structure de $G$-bimodule. Soit", r"une structure de $G$-\emph{bimodule}. Soit")

add(54, "(18.1.7) cont., line 2: 'Soit θ: 𝔎→G'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"$\theta:\mathfrak{R}\to G$", r"$\theta:\mathfrak{K}\to G$", note=LETTER)

add(54, "(18.1.7) cont., line 2: 'un homomorphisme de G-bimodules'", "G-*bimodules* (italic)", "upright",
    "italics", None, "high",
    r"un homomorphisme de $G$-bimodules rendant", r"un homomorphisme de $G$-\emph{bimodules} rendant")

add(54, "(18.1.7) cont., line 3: '𝔍'∩θ(𝔎)=0'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"\cap\theta(\mathfrak{R})=0", r"\cap\theta(\mathfrak{K})=0", note=LETTER)

add(54, "(18.1.7) cont., line 4: 'comme θ(𝔎) est un idéal bilatère'", "𝔎", r"\mathfrak{R}", "symbol", None,
    "high", r"$\theta(\mathfrak{R})$ est un idéal", r"$\theta(\mathfrak{K})$ est un idéal", note=LETTER)

add(54, "(18.1.7) cont., line 4: 'h(θ(𝔎))=𝔎'", "𝔎 twice", r"\mathfrak{R} twice", "symbol", None, "high",
    r"$h(\theta(\mathfrak{R}))=\mathfrak{R}$", r"$h(\theta(\mathfrak{K}))=\mathfrak{K}$", note=LETTER)

add(54, "(18.1.7) cont., line 5: 'G →q G/θ(𝔎) →f B'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"G/\theta(\mathfrak{R})\xrightarrow{f}", r"G/\theta(\mathfrak{K})\xrightarrow{f}", note=LETTER)

add(54, "(18.1.7) cont., line 6: 'E=G/θ(𝔎)'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"$E=G/\theta(\mathfrak{R})$", r"$E=G/\theta(\mathfrak{K})$", note=LETTER)

add(54, "(18.1.7) cont., line 6: '𝔍'⊕θ(𝔎)'", "𝔎", r"\mathfrak{R}", "symbol", None, "high",
    r"\oplus\theta(\mathfrak{R})$", r"\oplus\theta(\mathfrak{K})$", note=LETTER)

add(54, "heading of 18.2", "18.2. Extensions d'un anneau par un bimodule.",
    r"\subsection{Extensions d'un anneau par un bimodule}", "punctuation", None, "high",
    r"\subsection{Extensions d'un anneau par un bimodule}",
    r"\subsection{Extensions d'un anneau par un bimodule.}",
    note="Printed final full stop (see the 18.1 heading, p. 51).")

add(54, "(18.2.1), line 4: '(resp. z'(x+z)=zx)'", "z'(x+z)=zx: no prime on the z of the right-hand side",
    r"$z'(x+z)=z'x$ (silently corrected)", "misprint_in_print", None, "high",
    r"$z'(x+z)=z'x$", r"$z'(x+z)=zx$", corrected=r"$z'(x+z)=z'x$",
    note="2.5x crop. z'(x+z)=z'x+z'z=z'x since 𝔍²=0; the next line of the print has z'x. Not in the authors' errata.")

add(54, "(18.2.1), line 5: 'ne dépend pas de l'élément x∈f^{-1}(b)'", "l'élément x∈f^{-1}(b)",
    r"l'élément $x$ de $f^{-1}(b)$", "formula", None, "high",
    r"l'élément $x$ de $f^{-1}(b)$", r"l'élément $x\in f^{-1}(b)$", note="2.2x crop.")

add(54, "diagram (18.2.2.1), vertical arrow E→E'", "u left of the arrow, ≀ right of it",
    r"\ar@{}[dd]|{\wr}: ≀ centred on the arrow itself", "other", None, "medium",
    r"\ar[dd]_u\ar@{}[dd]|{\wr}", r"\ar[dd]_u^{\wr}", note="Placement of ≀ (cf. GLOBAL_ISSUES 30).")

add(54, "diagram (18.2.2.1), label u of E→E'",
    "u printed in bold italic (much heavier than the label u of (18.2.4.1) and of the diagram in (18.1.6))",
    r"ordinary $u$ (silently corrected)", "misprint_in_print", None, "medium",
    r"\ar[dd]_u^{\wr}", r"\ar[dd]_{\boldsymbol{u}}^{\wr}", corrected=r"\ar[dd]_u^{\wr}",
    note=("Wrong-fount letter (GLOBAL_ISSUES 29), side-by-side 6x crops. Apply after the previous finding (this 'old' "
          "is the text after that fix)."))

# ---------------- page 55 ----------------
add(55, "(18.2.3): 'cette extension est l'extension triviale type'",
    "l' upright, 'extension triviale type' italic", r"\emph{l'extension triviale type}", "italics", None,
    "high", r"\emph{l'extension triviale type}", r"l'\emph{extension triviale type}")

add(55, "(18.2.3): 'qui est A-triviale, l'application canonique'", "A-*triviale* (italic)", "upright",
    "italics", None, "high", r"$A$-triviale, l'application", r"$A$-\emph{triviale}, l'application")

add(55, "(18.2.3): 'est A-équivalente à D_B(L)'", "A-*équivalente* (italic)", "upright",
    "italics", None, "high", r"$A$-équivalente à $D_B(L)$", r"$A$-\emph{équivalente} à $D_B(L)$")

add(55, "(18.2.4), after the diagram: 'des A-homomorphismes d'anneaux'", "d' upright, 'anneaux' italic",
    r"\emph{d'anneaux}", "italics", None, "high", r"\emph{d'anneaux}", r"d'\emph{anneaux}")

add(55, "(18.2.5): 'soit F=E'×_{B'}B l'image réciproque par v'", "l' upright, 'image réciproque' italic",
    r"\emph{l'image réciproque}", "italics", None, "high",
    r"\emph{l'image réciproque}", r"l'\emph{image réciproque}")

add(55, "(18.2.5), diagram, arrow L_0→L'", "i and ≀ both left of the arrow ('i ≀ ↓')",
    r"\ar[d]^i\ar@{}[d]|{\wr}: i right, ≀ centred on the arrow", "symbol", None, "high",
    r"\ar[d]^i\ar@{}[d]|{\wr}", r"\ar[d]_{i\wr}")

add(55, "(18.2.5), diagram, arrow F→E'", "label p_1 left of the arrow", r"\ar[d]^{p_1} (label right)",
    "other", None, "high", r"\ar[d]^{p_1}", r"\ar[d]_{p_1}", note="Label side.")

add(55, "(18.2.5), after the diagram: 'que i est bijectif'", "*bijectif* (italic)", "upright",
    "italics", None, "high", r"que $i$ est bijectif", r"que $i$ est \emph{bijectif}")

add(55, "(18.2.5): 'que F est une A-extension de B par L''", "F *est une* A-*extension de* B *par* L' (italic)",
    "upright", "italics", None, "high",
    r"est une $A$-extension de $B$ par $L'$, que",
    r"\emph{est une} $A$-\emph{extension de} $B$ \emph{par} $L'$, que")

add(55, "(18.2.5): 'que l'on appelle image réciproque par v'", "'image réciproque' italic, 'par v' upright",
    r"\emph{image réciproque par $v$}", "italics", None, "high",
    r"\emph{image⏎réciproque par $v$}", r"\emph{image⏎réciproque} par $v$")


# ---------------- validation ----------------
def load(p):
    with open(os.path.join(RUN, "page_%03d.tex" % p), encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


ok = True
orig = {p: load(p) for p in range(51, 56)}
cur = dict(orig)
for i, d in enumerate(F):
    p = d["page"]
    fx = d["fix"]
    if fx is not None:
        c0 = orig[p].count(fx["old"])
        c1 = cur[p].count(fx["old"])
        flag = "" if c1 == 1 else "  <-- NOT UNIQUE AT APPLY TIME"
        if c1 != 1:
            ok = False
        print("#%02d p%d %-17s orig=%d at-apply=%d%s" % (i + 1, p, d["kind"], c0, c1, flag))
        if c1 == 1:
            cur[p] = cur[p].replace(fx["old"], fx["new"], 1)
    else:
        c0 = orig[p].count(d["tex"])
        c1 = cur[p].count(d["tex"])
        print("#%02d p%d %-17s fix=null tex-in-orig=%d tex-at-this-point=%d" % (i + 1, p, d["kind"], c0, c1))
        if c0 != 1 and c1 != 1:
            ok = False

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(F, fh, ensure_ascii=False, indent=1)
print("written", OUT, len(F), "findings; all olds unique at apply time:", ok)
