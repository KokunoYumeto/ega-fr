"""Write findings_230_234.json and check every fix's 'old' against the page files and the source."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
SRC = RUN.parent / "ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-20-fr.tex"
OUT = RUN / "findings_230_234.json"


def F(page, where, scan, tex, kind, old, new, note="", convention=None, confidence="high", corrected=None):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": convention,
        "confidence": confidence,
        "fix": None if old is None else {"old": old, "new": new},
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    return d


findings = [
    # ---------------- p. 230 ----------------
    F(230, "l. 1: 'on déduit canoniquement de θ♯ : ψ*(O_X) → O_X′'",
      "sharp sign ♯ (crop p230_theta.png)", "^\\#",
      "convention", r"de $\theta^\#:\psi^*(\sh{O}_X)", r"de $\theta^\sharp:\psi^*(\sh{O}_X)", convention=9),
    F(230, "l. 2: 'faisceaux d'anneaux θ′♯ : ψ*(M_f) → M_X′'",
      "sharp sign ♯", "^{\\prime\\#}",
      "convention", r"$\theta^{\prime\#}:\psi^*(\sh{M}_f)", r"$\theta^{\prime\sharp}:\psi^*(\sh{M}_f)", convention=9),
    F(230, "l. 2: 'prolongeant θ♯ (Bourbaki'",
      "sharp sign ♯", "^\\#",
      "convention", r"prolongeant $\theta^\#$ (Bourbaki", r"prolongeant $\theta^\sharp$ (Bourbaki", convention=9),
    F(230, "l. 4: 'un homomorphisme canonique de O_X′-Algèbres'",
      "'-Algèbres' with a capital A (crop p230_Algebres.png)", "'-algèbres'",
      "word", r"canonique de $\sh{O}_{X'}$-algèbres", r"canonique de $\sh{O}_{X'}$-Algèbres"),
    F(230, "after (20.1.11.1): 'Γ(θ′♯)(φ) est une fonction méromorphe'",
      "sharp sign ♯", "^{\\prime\\#}",
      "convention", r"$\Gamma(\theta^{\prime\#})(\vphi)$", r"$\Gamma(\theta^{\prime\sharp})(\vphi)$", convention=9),
    F(230, "'De même, si F est un O_X-Module, on pose'",
      "'-Module' with a capital M (crop p230_Module.png)", "'-module'",
      "word", r"est un $\sh{O}_X$-module, on pose", r"est un $\sh{O}_X$-Module, on pose"),
    F(230, "'et on déduit aussitôt de θ′♯ un homomorphisme canonique'",
      "sharp sign ♯ (crop p230_theta2.png)", "^{\\prime\\#}",
      "convention", r"aussitôt de $\theta^{\prime\#}$ un", r"aussitôt de $\theta^{\prime\sharp}$ un", convention=9),
    F(230, "'(qu'on écrit aussi u ⇝ u∘f)'",
      "wavy arrow", "\\mapsto",
      "symbol", r"(qu'on écrit aussi $u\mapsto u\circ f$)", r"(qu'on écrit aussi $u\leadsto u\circ f$)"),
    F(230, "'alors, si L est un O_X-Module inversible'",
      "'-Module' with a capital M", "'-module'",
      "word", r"est un $\sh{O}_X$-module inversible, l'image", r"est un $\sh{O}_X$-Module inversible, l'image"),
    F(230, "'l'image dans M_X′(f*(L)), par Γ(θ′♯), d'une section'",
      "sharp sign ♯", "^{\\prime\\#}",
      "convention", r"par $\Gamma(\theta^{\prime\#})$, d'une", r"par $\Gamma(\theta^{\prime\sharp})$, d'une", convention=9),
    F(230, "Proposition (20.1.12): 'est plat (0_I, 6.7.1)'",
      "bold 0 with a light roman subscript I (crop p230_prop_line1.png)",
      "\\sref[0\\textsubscript{I}] sets the whole optional argument in \\textbf, so the subscript I is bold",
      "font", r"est plat \sref[0\textsubscript{I}]", r"est plat \sref[0\textsubscript{\mdseries I}]",
      note="The edition writes this reference elsewhere as $\\mathbf{0}_{\\mathrm I}$ (light I). Same in the other 4 \\sref[0\\textsubscript{I}] of ega4-20 (pp. 228-229). Does not overlap the next finding.",
      confidence="medium"),
    F(230, "Proposition (20.1.12): '(0_I, 6.7.1) on a M_f = M_X'",
      "no comma after the reference (crop p230_prop_line1.png)", "comma after the reference",
      "punctuation", r"{0.6.7.1}, on a", r"{0.6.7.1} on a"),
    F(230, "Proposition (20.1.12): 'et l'homomorphisme φ ⇝ φ∘f est défini dans M(X)'",
      "wavy arrow", "\\mapsto",
      "symbol", r"$\vphi\mapsto\vphi\circ f$ est défini", r"$\vphi\leadsto\vphi\circ f$ est défini"),
    F(230, "Proposition (20.1.12), end: 'l'homomorphisme φ ⇝ φ∘f est injectif'",
      "wavy arrow (crop p230_phi.png)", "\\mapsto",
      "symbol", r"$\vphi\mapsto\vphi\circ f$ est injectif", r"$\vphi\leadsto\vphi\circ f$ est injectif"),
    F(230, "proof of (20.1.12), l. 2: 'non diviseur de 0 dans B (0_I, 6.3.4)'",
      "bold 0 with a light roman subscript I (crop p230_0I_634.png)", "bold subscript I (\\textbf around the whole optional argument)",
      "font", r"\sref[0\textsubscript{I}]{0.6.3.4}", r"\sref[0\textsubscript{\mdseries I}]{0.6.3.4}",
      confidence="medium"),
    F(230, "proof of (20.1.12): 'il est injectif (0_I, 6.5.1 et 6.6.2)'",
      "one parenthesis: '(0_I, 6.5.1 et 6.6.2)', bold 0 with a light subscript I (crop p230_0I_651.png)",
      "two \\sref inside parentheses typeset '((0_I, 6.5.1) et (0_I, 6.6.2))' (each \\sref prints its own parentheses and 0_I)",
      "extra",
      r"(\sref[0\textsubscript{I}]{0.6.5.1} et \sref[0\textsubscript{I}]{0.6.6.2})",
      r"(\textbf{0}\textsubscript{I}, \EGAUnavailableHyperref{0.6.5.1}{6.5.1} et \EGAUnavailableHyperref{0.6.6.2}{6.6.2})",
      note="\\EGAUnavailableHyperref (IV-4 preamble) is the link \\sref itself uses for these labels (r@0.6.5.1, r@0.6.6.2 are undefined); a plain '(\\textbf{0}\\textsubscript{I}, 6.5.1 et 6.6.2)' gives the same print without links. The same doubled-parenthesis construction '(\\sref...)' stands at ega4-20 lines 13, 30, 383, 728, 729 and ega4-21b lines 81, 223, 358, 657, 917."),
    # ---------------- p. 231 ----------------
    F(231, "proof of (20.1.12): 'Le quotient ... s'identifie à un sous-O_X′-Module de M_X′/O_X′'",
      "'-Module' with a capital M", "'-module'",
      "word", r"sous-$\sh{O}_{X'}$-module de", r"sous-$\sh{O}_{X'}$-Module de"),
    F(231, "Remarque (20.1.13): 'l'homomorphisme canonique u ⇝ u∘f de M(Y) dans M(Y^an)'",
      "wavy arrow (crop p231_uf.png)", "\\mapsto",
      "symbol", r"$u\mapsto u\circ f$ de $M(Y)$", r"$u\leadsto u\circ f$ de $M(Y)$"),
    F(231, "Remarque (20.1.13): '(Err_III, 14)'",
      "bold 'Err' with a light roman subscript III (crop p231_Err2.png)", "subscript \\textbf{III} (bold)",
      "font", r"(\textbf{Err}\textsubscript{\textbf{III}},~14)", r"(\textbf{Err}\textsubscript{III},~14)",
      note="Elsewhere the edition writes $\\mathbf{Err}_{\\mathrm{III}}$ (light III)."),
    F(231, "(20.2.1), last paragraph: 'la classe d'équivalence ... d'un S-morphisme d'un ouvert'",
      "'morphisme' italic, 'S-' roman (crop p231_Smorph.png)", "roman",
      "italics", r"d'un $S$-morphisme d'un ouvert", r"d'un $S$-\emph{morphisme} d'un ouvert"),
    F(231, "end of p. 231 / top of p. 232: heading '(20.2.2)'",
      "p. 231 ends with '... (resp. des pseudo-S-morphismes) de X dans Y.'; p. 232 begins with the heading '(20.2.2) Il résulte'",
      "\\oldpage[IV-4]{232} stands after \\begin{env}[20.2.2] and its \\EGAReaderTarget, so the heading (20.2.2) falls on p. 231",
      "marker",
      "\\begin{env}[20.2.2]\n\\EGAReaderTarget{ega4.c04.statement.20-2-2}{IV.20.2.2}",
      "\\oldpage[IV-4]{232}\n\\begin{env}[20.2.2]\n\\EGAReaderTarget{ega4.c04.statement.20-2-2}{IV.20.2.2}",
      note="Part 1 of 2 (marker move): apply together with the first p. 232 finding, which removes the old marker; either order works, and each 'old' stays unique after the other is applied."),
    # ---------------- p. 232 ----------------
    F(232, "top of p. 232: old marker position",
      "p. 232 begins with the heading (20.2.2)", "\\oldpage[IV-4]{232} after \\begin{env}[20.2.2]",
      "marker", "\\oldpage[IV-4]{232}\nIl résulte", "Il résulte",
      note="Part 2 of 2 (marker move): apply together with the last p. 231 finding, which inserts the marker before \\begin{env}[20.2.2]."),
    F(232, "(20.2.2), l. 7: 'et on note ce pseudo-morphisme ω|U.'",
      "ω|U (crop p232_omegaU.png)", "ω|V (silent correction)",
      "misprint_in_print", r"on note ce pseudo-morphisme $\omega|V$.", r"on note ce pseudo-morphisme $\omega|U$.",
      corrected=r"on note ce pseudo-morphisme $\omega|V$.",
      note="The TeX silently corrects. Correct reading ω|V: the sentence names the restriction to V of ω, and the next sentence uses (ω|V)|W = ω|W. No erratum in Err_IV."),
    F(232, "(20.2.2): 'un préfaisceau d'ensembles U ⇝ Ps.hom(U, Y)'",
      "wavy arrow", "\\mapsto",
      "symbol", r"d'ensembles $U\mapsto\operatorname{Ps.hom}(U,Y)$", r"d'ensembles $U\leadsto\operatorname{Ps.hom}(U,Y)$"),
    F(232, "(20.2.2): 'le faisceau associé se note 𝒫s.hom(X, Y)'",
      "script P followed by italic 's.hom' (crop p232_Pshom.png)", "upright 'hom' (\\operatorname{hom})",
      "font", r"se note $\mathscr{P}\!s.\!\operatorname{hom}(X,Y)$", r"se note $\mathscr{P}\!s.\!\mathit{hom}(X,Y)$",
      note="Like the sheaf Proj (script P + italic 'roj', GLOBAL_ISSUES 31). ega4-20 writes \\mathscr{P}\\!s.\\!\\operatorname{hom} 14 times."),
    F(232, "(20.2.2): 'on voit de même que U ⇝ Ps.hom_S(X, Y)'",
      "wavy arrow (crop p232_Pshom.png)", "\\mapsto",
      "symbol", r"on voit de même que $U\mapsto", r"on voit de même que $U\leadsto",
      note="Does not overlap the next finding (misprint)."),
    F(232, "(20.2.2): 'U ⇝ Ps.hom_S(X, Y) est un préfaisceau d'ensembles'",
      "Ps.hom_S(X, Y) (crop p232_Pshom.png)", "Ps.hom_S(U, Y) (silent correction)",
      "misprint_in_print", r"\operatorname{Ps.hom}_S(U,Y)$ est un préfaisceau", r"\operatorname{Ps.hom}_S(X,Y)$ est un préfaisceau",
      corrected=r"\operatorname{Ps.hom}_S(U,Y)$ est un préfaisceau",
      note="The TeX silently corrects. Correct reading Ps.hom_S(U, Y): the presheaf U ⇝ Ps.hom_S(U, Y), as in U ⇝ Ps.hom(U, Y) two lines before and in Corollaire (20.2.6). No erratum in Err_IV. Apply after (or before) the arrow fix above; they do not overlap."),
    F(232, "(20.2.2): 'dont on note 𝒫s.hom_S(X, Y) le faisceau associé'",
      "script P followed by italic 's.hom' (crop p232_Pshom2.png)", "upright 'hom'",
      "font", r"dont on note $\mathscr{P}\!s.\!\operatorname{hom}_S(X,Y)$", r"dont on note $\mathscr{P}\!s.\!\mathit{hom}_S(X,Y)$"),
    F(232, "(20.2.2), last paragraph: 'donc l'application ω ⇝ ω|V est une bijection'",
      "wavy arrow", "\\mapsto",
      "symbol", r"l'application $\omega\mapsto\omega|V$", r"l'application $\omega\leadsto\omega|V$"),
    F(232, "proof of (20.2.4), end: 'notre assertion résulte de (11.10.1, d))'",
      "'(11.10.1, d))': the label is an italic 'd)' with no opening parenthesis (crop p232_11101d.png)",
      "\\sref{IV.11.10.1}[(d)] prints '(11.10.1, (d))' with an upright (d)",
      "other", r"notre assertion résulte de \sref{IV.11.10.1}[(d)]", r"notre assertion résulte de \sref{IV.11.10.1}[\emph{d)}]",
      note="\\sref sets its third argument in \\normalfont, so \\emph gives the italic label. ega4-20 has the same form at lines 537 [(a)], 638 [(c)], 669 [(d)] and 504, 693, 702, 704 [(ii), (a)/(b)]: check those labels against the print."),
    # ---------------- p. 233 ----------------
    F(233, "proof of (20.2.5), end: 'cela résulte encore de (11.10.1, d))'",
      "italic label 'd)' with no opening parenthesis", "\\sref{IV.11.10.1}[(d)] prints '(11.10.1, (d))'",
      "other", r"cela résulte encore de \sref{IV.11.10.1}[(d)]", r"cela résulte encore de \sref{IV.11.10.1}[\emph{d)}]"),
    F(233, "Corollaire (20.2.6): 'le préfaisceau U ⇝ Ps.hom_S(U, Y) est un faisceau'",
      "wavy arrow", "\\mapsto",
      "symbol", r"le préfaisceau $U\mapsto\operatorname{Ps.hom}_S(U,Y)$ est un faisceau",
      r"le préfaisceau $U\leadsto\operatorname{Ps.hom}_S(U,Y)$ est un faisceau"),
    F(233, "(20.2.8): 'Il est clair que le faisceau 𝒫s.hom_X(X, X⊗_Z Z[T]))'",
      "script P followed by italic 's.hom' (crop p233_Pshom_paren.png)", "upright 'hom'",
      "font", r"Il est clair que le faisceau $\mathscr{P}\!s.\!\operatorname{hom}_X(", r"Il est clair que le faisceau $\mathscr{P}\!s.\!\mathit{hom}_X(",
      note="Does not overlap the next finding (misprint)."),
    F(233, "(20.2.8): '𝒫s.hom_X(X, X⊗_Z Z[T])) est ici un faisceau d'anneaux'",
      "two closing parentheses after Z[T] for one opening (crop p233_Pshom_paren.png)", "one closing parenthesis (silent correction)",
      "misprint_in_print", r"\bb{Z}[T])$ est ici un", r"\bb{Z}[T]))$ est ici un",
      corrected=r"\bb{Z}[T])$ est ici un",
      note="The TeX silently corrects the unbalanced parenthesis. Correct reading 𝒫s.hom_X(X, X⊗_Z Z[T]). No erratum in Err_IV."),
    F(233, "(20.2.8), end: '(V ouvert de X) les éléments inversibles'",
      "no comma after the parenthesis (crop p233_Vouvert.png)", "comma after the parenthesis",
      "punctuation", r"($V$ ouvert de $X$), les éléments", r"($V$ ouvert de $X$) les éléments"),
    F(233, "(20.2.8), last word of p. 233: 'correspondent aux morphismes qui se'",
      "'se' italic (crop p233_se.png); the italic phrase is 'se factorisent en' across the page break", "roman 'se'",
      "italics", r"correspondent aux morphismes qui se", r"correspondent aux morphismes qui \emph{se}",
      note="See the first p. 234 finding for 'factorisent en'."),
    # ---------------- p. 234 ----------------
    F(234, "l. 1: 'factorisent en V → Spec(Z[T, T⁻¹])'",
      "'factorisent en' italic, 'en' included (crop p234_factorisent.png)", "\\emph{factorisent} en: 'en' roman",
      "italics", r"\emph{factorisent} en $V", r"\emph{factorisent en} $V"),
    F(234, "l. 3: 's'identifie canoniquement au faisceau 𝒫s.hom_X(X, X⊗_Z Z[T, T⁻¹])'",
      "script P followed by italic 's.hom'", "upright 'hom'",
      "font", r"au faisceau $\mathscr{P}\!s.\!\operatorname{hom}_X(", r"au faisceau $\mathscr{P}\!s.\!\mathit{hom}_X("),
    F(234, "Proposition (20.2.11) (i): '(et par suite aussi (20.2.10.2)) est injectif.'",
      "the parenthesis '(et par suite aussi (20.2.10.2))' roman, 'est injectif' italic (crop p234_prop1.png)",
      "parenthesis italic (statement environment); \\emph{injectif} inside the italic environment comes out upright",
      "convention", r"(et par suite aussi \emph{\sref{IV.20.2.10.2}}) est \emph{injectif}.",
      r"\textup{(et par suite aussi \emph{\sref{IV.20.2.10.2}})} est injectif.", convention=6,
      note="Two parts in one edit: \\textup for the roman parenthesis, and \\emph dropped where the print shows no change of face (FIX_POLICY 2.6)."),
    F(234, "Proposition (20.2.11) (ii), end: '(et par suite aussi (20.2.10.2)) est bijectif.'",
      "the parenthesis roman, 'est bijectif' italic (crop p234_prop2.png)",
      "parenthesis italic; \\emph{bijectif} upright inside the italic environment",
      "convention", r"(et par suite aussi \emph{\sref{IV.20.2.10.2}}) est \emph{bijectif}.",
      r"\textup{(et par suite aussi \emph{\sref{IV.20.2.10.2}})} est bijectif.", convention=6,
      note="Same two-part edit as (i)."),
    F(234, "proof of (20.2.11): 'S⁻¹A est l'anneau total des fractions de A'",
      "\"l'\" roman, 'anneau total des fractions' italic (crop p234_lanneau.png)", "\\emph{l'anneau total des fractions}: \"l'\" italic",
      "italics", r"est \emph{l'anneau total des fractions}", r"est l'\emph{anneau total des fractions}"),
]


def norm(s):
    return s.replace("\r\n", "\n")


src = norm(SRC.read_text(encoding="utf-8"))
pages = {n: norm((RUN / f"page_{n}.tex").read_text(encoding="utf-8")) for n in range(230, 235)}
bad = 0
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    old = fx["old"]
    cp = pages[f["page"]].count(old)
    cs = src.count(old)
    if cp != 1 or cs != 1:
        bad += 1
        print("NOT UNIQUE", f["page"], cp, cs, repr(old))
# simulate applying all fixes in order on the source, checking each old is unique at its turn
s = src
for f in findings:
    fx = f["fix"]
    if fx is None:
        continue
    c = s.count(fx["old"])
    if c != 1:
        bad += 1
        print("SEQUENTIAL PROBLEM", f["page"], c, repr(fx["old"]))
        continue
    s = s.replace(fx["old"], fx["new"], 1)
print("problems:", bad)
OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1), encoding="utf-8")
counts = {}
for f in findings:
    c = counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})
    if f["kind"] == "convention":
        c["convention"] += 1
    elif f["kind"] == "misprint_in_print":
        c["misprint"] += 1
    else:
        c["normal"] += 1
print(counts, len(findings))
