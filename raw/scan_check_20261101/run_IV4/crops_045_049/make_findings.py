"""Build findings_045_049.json and check every fix against the page files.

Each page's fixes are applied in list order to an LF copy of page_NNN.tex;
every 'old' must occur exactly once at the moment it is applied.  The script
also reports whether 'old' occurs exactly once in the untouched page text.
"""
import json
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUT = RUN / "findings_045_049.json"


def L(*lines):
    return "\n".join(lines)


F = []


def add(page, where, scan, tex, kind, conv, conf, old, new, note="", corrected=None):
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


JNOTE = ("Wrong letter: the print's script capital has the descender of a script J "
         "(cf. GLOBAL_ISSUES 91/95); ega4-16 writes \\mathscr{I}.")
FJNOTE = ("Wrong letter: the print's Fraktur capital has the descender of a Fraktur J "
          "(GLOBAL_ISSUES 91); ega4-16 writes \\mathfrak{I}.")
C7NOTE = "Long dash for the minus sign (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision."
C26NOTE = "Bold 0 (convention 2) and roman reference inside an italic statement (convention 6), one edit."

# ---------------------------------------------------------------- page 45
add(45, "l. 1: '(B⊗_A B)/𝔍^{n+1} comme B-module à gauche'",
    "Fraktur J (descender; crop p45_s1_frak.png)", "\\mathfrak{I}", "symbol", None, "high",
    r"$(B\otimes_A B)/\mathfrak{I}^{n+1}$ comme",
    r"$(B\otimes_A B)/\mathfrak{J}^{n+1}$ comme", FJNOTE)
add(45, "display φ_0 : B⊗_A B → ((B⊗_A B)/𝔍^{n'+1})⊗_B((B⊗_A B)/𝔍^{n+1})",
    "Fraktur J twice (crop p45_s1_disp1.png)", "\\mathfrak{I} twice", "symbol", None, "high",
    L(r"((B\otimes_A B)/\mathfrak{I}^{n'+1})",
      r"  \otimes_B((B\otimes_A B)/\mathfrak{I}^{n+1})"),
    L(r"((B\otimes_A B)/\mathfrak{J}^{n'+1})",
      r"  \otimes_B((B\otimes_A B)/\mathfrak{J}^{n+1})"), FJNOTE)
add(45, "'qu'il s'annule dans 𝔍^{n+n'+1}'",
    "Fraktur J (crop p45_s1_frak3.png)", "\\mathfrak{I}", "symbol", None, "high",
    r"$\mathfrak{I}^{n+n'+1}$", r"$\mathfrak{J}^{n+n'+1}$", FJNOTE)
add(45, "display after 'Or, on peut écrire': φ_0(b⊗1—1⊗b)=π_{n'}(b⊗1—1⊗b)⊗π_n(1⊗1)+π_{n'}(1⊗b)⊗π_n(1⊗1)—π_{n'}(1⊗1)⊗π_n(1⊗b) (3 occurrences)",
    "long dash for the three minus signs (crop p45_s1_minus.png; longer than the bar of +)",
    "-", "convention", 7, "high",
    L(r"  \varphi_0(b\otimes1-1\otimes b)",
      r"  ={}&\pi_{n'}(b\otimes1-1\otimes b)\otimes\pi_n(1\otimes1)\\",
      r"  &+\pi_{n'}(1\otimes b)\otimes\pi_n(1\otimes1)",
      r"  -\pi_{n'}(1\otimes1)\otimes\pi_n(1\otimes b)"),
    L(r"  \varphi_0(b\otimes1\setmin 1\otimes b)",
      r"  ={}&\pi_{n'}(b\otimes1\setmin 1\otimes b)\otimes\pi_n(1\otimes1)\\",
      r"  &+\pi_{n'}(1\otimes b)\otimes\pi_n(1\otimes1)",
      r"  \setmin\pi_{n'}(1\otimes1)\otimes\pi_n(1\otimes b)"),
    C7NOTE + " Three occurrences, one edit.")
add(45, "display (16.8.9.4): φ_0(b⊗1—1⊗b)=π_{n'}(b⊗1—1⊗b)⊗π_n(1⊗1)+π_{n'}(1⊗1)⊗π_n(b⊗1—1⊗b) (3 occurrences)",
    "long dash for the three minus signs", "-", "convention", 7, "high",
    L(r"  \varphi_0(b\otimes1-1\otimes b)",
      r"  ={}&\pi_{n'}(b\otimes1-1\otimes b)\otimes\pi_n(1\otimes1)\\",
      r"  &+\pi_{n'}(1\otimes1)\otimes\pi_n(b\otimes1-1\otimes b)."),
    L(r"  \varphi_0(b\otimes1\setmin 1\otimes b)",
      r"  ={}&\pi_{n'}(b\otimes1\setmin 1\otimes b)\otimes\pi_n(1\otimes1)\\",
      r"  &+\pi_{n'}(1\otimes1)\otimes\pi_n(b\otimes1\setmin 1\otimes b)."),
    C7NOTE + " Three occurrences, one edit.")
add(45, "'n+1 termes de la forme π_n(b⊗1—1⊗b)'",
    "long dash for the minus", "-", "convention", 7, "high",
    r"forme $\pi_n(b\otimes1-1\otimes b)$", r"forme $\pi_n(b\otimes1\setmin 1\otimes b)$", C7NOTE)
add(45, "'n'+1 termes de la forme π_{n'}(b⊗1—1⊗b)'",
    "long dash for the minus", "-", "convention", 7, "high",
    r"forme $\pi_{n'}(b\otimes1-1\otimes b)$", r"forme $\pi_{n'}(b\otimes1\setmin 1\otimes b)$", C7NOTE)
add(45, "end of the proof of (16.8.9.1): 'La conclusion résulte donc de (0, 20.4.4)'",
    "bold 0, no subscript", "plain 0", "convention", 2, "high",
    "(0, 20.4.4)", r"(\textbf{0}, 20.4.4)")
add(45, "Remarques (16.8.11) (i): 'comme le foncteur F ⇝ Γ(U, F) commute'",
    "wavy arrow (crop p45_s3_leadsto.png)", "\\mapsto", "symbol", None, "high",
    r"$\mathscr{F}\mapsto\Gamma(U,\mathscr{F})$", r"$\mathscr{F}\leadsto\Gamma(U,\mathscr{F})$")
add(45, "Remarques (16.8.11) (i): 'à chaque F_λ est d^n_{X/S,F_λ} : F_λ → P^n_{X/S,(F_λ)}; on en conclut'",
    "the map is set in the running text, followed by ';' and 'on en conclut' on the same line (crop p45_s3_dline.png)",
    "displayed with \\[ ... \\]", "other", None, "high",
    L(r"  \[",
      r"    d_{X/S,\mathscr{F}_\lambda}^n:\mathscr{F}_\lambda",
      r"    \longrightarrow\mathscr{P}_{X/S}^n(\mathscr{F}_\lambda);",
      r"  \]"),
    r"  $d_{X/S,\mathscr{F}_\lambda}^n:\mathscr{F}_\lambda\to\mathscr{P}_{X/S}^n(\mathscr{F}_\lambda)$;",
    "Display vs inline only; no connecting word lost or added. Apply before the next entry (misprint), whose 'old' is taken from the text after this edit.")
add(45, "same formula: target 'P^n_{X/S,(F_λ)}'",
    "the argument (F_λ) is set in the subscript, after a comma: P^n_{X/S, (F_λ)} (4x crop p45_s3_dmis.png)",
    "\\mathscr{P}_{X/S}^n(\\mathscr{F}_\\lambda): silent correction", "misprint_in_print", None, "high",
    r"\to\mathscr{P}_{X/S}^n(\mathscr{F}_\lambda)$;",
    r"\to\mathscr{P}_{X/S,(\mathscr{F}_\lambda)}^n$;",
    "The target is P^n_{X/S}(F_λ) (16.7.2); the compositor dropped the argument into the subscript. 'old' is the text after the preceding display-to-inline edit; the fix restores the printed reading.",
    corrected=r"\mathscr{P}_{X/S}^n(\mathscr{F}_\lambda)")
add(45, "Remarques (16.8.11) (i): 'et par suite aussi (0_I, 3.2.6)'",
    "bold 0 with subscript I", "0\\textsubscript{I}: plain 0", "convention", 2, "high",
    r"aussi (0\textsubscript{I}, 3.2.6)", r"aussi ($\mathbf{0}_{\mathrm I}$, 3.2.6)",
    "Written as the edition's other (0_I, ...) references; the math-mode form stays upright inside the (italic) remarks environment.")
add(45, "Remarques (16.8.11) (i): 'si G = Π G_μ (0_I, 3.2.6), on a'",
    "bold 0 with subscript I", "0\\textsubscript{I}: plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 3.2.6), on a", r"($\mathbf{0}_{\mathrm I}$, 3.2.6), on a")

# ---------------------------------------------------------------- page 46
add(46, "Remarques (16.8.11) (i), l. 2: 'de ses composés u_μ : P^n_{X/S}(F) → G → G_μ. On a donc'",
    "the composite is set in the running text, followed by '. On a donc' on the same line",
    "displayed with \\[ ... \\]", "other", None, "high",
    L(r"composés",
      r"  \[",
      r"    u_\mu:\mathscr{P}_{X/S}^n(\mathscr{F})",
      r"    \longrightarrow\mathscr{G}\longrightarrow\mathscr{G}_\mu.",
      r"  \]"),
    L(r"composés",
      r"  $u_\mu:\mathscr{P}_{X/S}^n(\mathscr{F})\to\mathscr{G}\to\mathscr{G}_\mu$."),
    "Display vs inline only; no connecting word lost or added.")
add(46, "Définition (16.9.1): 'On dit qu'un Idéal 𝒥 de O_X'",
    "script J (descender; crop p46_s2_def1.png)", "\\mathscr{I}", "symbol", None, "high",
    r"qu'un Idéal $\mathscr{I}$ de", r"qu'un Idéal $\mathscr{J}$ de", JNOTE)
add(46, "Définition (16.9.1): 'est régulier'",
    "italic like the rest of the definition, no change of face (crop p46_s2_def1.png)",
    "\\emph{régulier} inside the italic definition: comes out upright", "italics", None, "high",
    r"$\mathcal{O}_X$ est \emph{régulier}", r"$\mathcal{O}_X$ est régulier")
add(46, "Définition (16.9.1): '(resp. quasi-régulier) si, pour'",
    "'(resp.' and ')' upright, 'quasi-régulier' italic like the rest (crop p46_s2_resp.png)",
    "'(resp.' and ')' italic; \\emph{quasi-régulier} upright", "convention", 6, "high",
    r"(resp. \emph{quasi-régulier}) si, pour",
    r"\textup{(resp.}\ quasi-régulier\textup{)} si, pour",
    "One edit for two differences: convention 6 for '(resp.' and ')', and the \\emph that sets 'quasi-régulier' upright inside the italic definition (italics).")
add(46, "Définition (16.9.1): 'x∈Supp(O_X/𝒥)'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"\operatorname{Supp}(\mathcal{O}_X/\mathscr{I})$, il existe",
    r"\operatorname{Supp}(\mathcal{O}_X/\mathscr{J})$, il existe", JNOTE)
add(46, "Définition (16.9.1): 'une suite régulière (0, 15.2.2) (resp.'",
    "(0, 15.2.2) and '(resp.' upright, bold 0 (crop p46_s2_suite.png)",
    "plain 0; reference and '(resp.' italic inside the definition", "convention", 2, "high",
    r"régulière (0, 15.2.2) (resp.",
    r"régulière \textup{(\textbf{0}, 15.2.2) (resp.}", C26NOTE)
add(46, "Définition (16.9.1): 'quasi-régulière (0, 15.2.2)) d'éléments'",
    "(0, 15.2.2)) upright, bold 0", "plain 0; italic", "convention", 2, "high",
    r"quasi-régulière (0, 15.2.2)) d'éléments",
    r"quasi-régulière \textup{(\textbf{0}, 15.2.2))} d'éléments",
    C26NOTE + " The last parenthesis closes '(resp.'.")
add(46, "Définition (16.9.1), end: 'qui engendre 𝒥|U.'",
    "script J (crop p46_s2_def1b.png)", "\\mathscr{I}", "symbol", None, "high",
    r"engendre $\mathscr{I}|U$.", r"engendre $\mathscr{J}|U$.", JNOTE)
add(46, "after (16.9.1): 'qui engendre 𝒥|U est un système régulier'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendre $\mathscr{I}|U$ est un", r"engendre $\mathscr{J}|U$ est un", JNOTE)
add(46, "after (16.9.1): 'de générateurs de 𝒥|U'",
    "'de générateurs de' italic, the second 'de' too (crop p46_s2_gen.png)",
    "\\emph{de générateurs} de: the second 'de' upright", "italics", None, "high",
    L(r"\emph{de générateurs}", r"de"), L(r"\emph{de générateurs", r"de}"))
add(46, "after (16.9.1), end: 'de 𝒥|U.'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    L(r"$\mathscr{I}|U$.", "", r"\begin{definition}"),
    L(r"$\mathscr{J}|U$.", "", r"\begin{definition}"), JNOTE)
add(46, "Définition (16.9.2): 'On dit que j est régulière'",
    "italic like the rest of the definition (crop p46_s2_def2.png)",
    "\\emph{régulière}: upright inside the italic definition", "italics", None, "high",
    r"dit que $j$ est \emph{régulière}", r"dit que $j$ est régulière")
add(46, "Définition (16.9.2): '(resp. quasi-régulière) si le sous-préschéma'",
    "'(resp.' and ')' upright, 'quasi-régulière' italic (crop p46_s3_def2b.png)",
    "'(resp.' and ')' italic; \\emph{quasi-régulière} upright", "convention", 6, "high",
    r"(resp. \emph{quasi-régulière}) si le",
    r"\textup{(resp.}\ quasi-régulière\textup{)} si le",
    "One edit for two differences: convention 6 for '(resp.' and ')', and the \\emph that sets 'quasi-régulière' upright (italics).")
add(46, "Définition (16.9.2): 'un Idéal régulier (resp. quasi-régulier) de O_U'",
    "'(resp.' and ')' upright, the rest italic (crop p46_s3_def2b.png)", "italic", "convention", 6, "high",
    r"régulier (resp. quasi-régulier) de $\mathcal{O}_U$",
    r"régulier \textup{(resp.}\ quasi-régulier\textup{)} de $\mathcal{O}_U$")
add(46, "Définition (16.9.2), end: '(condition indépendante de l'ouvert U choisi).'",
    "the parenthesis is roman (crop p46_s3_def2b.png)", "italic (inside the definition)", "convention", 6, "high",
    L(r"(condition indépendante de", r"l'ouvert $U$ choisi)"),
    L(r"\textup{(condition indépendante de", r"l'ouvert $U$ choisi)}"))
add(46, "after (16.9.2): 'et 𝒥 l'Idéal de O_X qui définit Y'",
    "script J (crop p46_s3_par.png)", "\\mathscr{I}", "symbol", None, "high",
    r"et $\mathscr{I}$ l'Idéal de", r"et $\mathscr{J}$ l'Idéal de", JNOTE)
add(46, "after (16.9.2): 'il revient au même de dire que 𝒥 est régulier'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"dire que $\mathscr{I}$ est", r"dire que $\mathscr{J}$ est", JNOTE)
add(46, "'Tout Idéal régulier est quasi-régulier (0, 15.2.2)'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"quasi-régulier (0, 15.2.2); toute", r"quasi-régulier (\textbf{0}, 15.2.2); toute")
add(46, "Proposition (16.9.3), l. 1: '𝒥 un Idéal de O_X'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"$\mathscr{I}$ un Idéal de $\mathcal{O}_X$,", r"$\mathscr{J}$ un Idéal de $\mathcal{O}_X$,", JNOTE)
add(46, "Proposition (16.9.3): '(f_i)_{1≤i≤m} une suite finie' against 'toute suite (f'_i)_{1≤i≤n} de n sections'",
    "m in the first index range, n (twice) in the last sentence (2x crop p46_s3_fim.png; p46_s4_fprime.png)",
    "the same: the TeX keeps the printed reading", "misprint_in_print", None, "medium",
    None, None,
    "The last assertion (any generating sequence with as many terms as the basis is quasi-regular; proof: a generating system of n elements of a free module with a basis of n elements is a basis) needs the same number of sections in both places; with n ≠ m it is false (repeat a generator). The authors write n elsewhere in 16.9 (16.9.4, 16.9.5); alternative correction: m in the last sentence. No erratum found.",
    corrected=r"$(f_i)_{1\leq i\leq n}$")
add(46, "Proposition (16.9.3): 'engendrant 𝒥. Pour que'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendrant $\mathscr{I}$. Pour que", r"engendrant $\mathscr{J}$. Pour que", JNOTE)
add(46, "Proposition (16.9.3): 'suite quasi-régulière (0, 15.2.2), il faut'",
    "bold 0, reference upright", "plain 0, italic", "convention", 2, "high",
    r"quasi-régulière (0, 15.2.2), il faut",
    r"quasi-régulière \textup{(\textbf{0}, 15.2.2)}, il faut", C26NOTE)
add(46, "Proposition (16.9.3), label (i)", "upright '(i)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(i)] Les images", r"\item[\textup{(i)}] Les images")
add(46, "Proposition (16.9.3) (i): '𝒥/𝒥² forment une base de cet O_X/𝒥-Module'",
    "script J three times", "\\mathscr{I} three times", "symbol", None, "high",
    L(r"$\mathscr{I}/\mathscr{I}^2$ forment une base de cet",
      r"  $\mathcal{O}_X/\mathscr{I}$-Module."),
    L(r"$\mathscr{J}/\mathscr{J}^2$ forment une base de cet",
      r"  $\mathcal{O}_X/\mathscr{J}$-Module."), JNOTE)
add(46, "Proposition (16.9.3), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)] L'", r"\item[\textup{(ii)}] L'")
add(46, "Proposition (16.9.3) (ii): 'surjectif canonique (16.1.2.2)'",
    "reference upright", "italic (inside the italic statement)", "convention", 6, "high",
    r"canonique (16.1.2.2)", r"canonique \textup{(16.1.2.2)}")
add(46, "Proposition (16.9.3) (ii), display S^•_{O_X/𝒥}(𝒥/𝒥²) → 𝒢r^•_𝒥(O_X)",
    "script J four times (crops p46_s4_disp.png, p46_s4_Ssub.png)", "\\mathscr{I} four times",
    "symbol", None, "high",
    L(r"\mathbf{S}_{\mathcal{O}_X/\mathscr{I}}^{\bullet}",
      r"    (\mathscr{I}/\mathscr{I}^2)",
      r"    \longrightarrow\mathscr{G}r_{\mathscr{I}}^{\bullet}(\mathcal{O}_X)"),
    L(r"\mathbf{S}_{\mathcal{O}_X/\mathscr{J}}^{\bullet}",
      r"    (\mathscr{J}/\mathscr{J}^2)",
      r"    \longrightarrow\mathscr{G}r_{\mathscr{J}}^{\bullet}(\mathcal{O}_X)"), JNOTE)
add(46, "Proposition (16.9.3), last paragraph 'En outre, s'il en est ainsi'",
    "new indented paragraph after 'est bijectif.' (crop p46_s4_fprime.png)",
    "follows \\end{enumerate} without a blank line, so it is set without indent", "other", None, "high",
    L(r"\end{enumerate}", r"En outre,"), L(r"\end{enumerate}", "", r"En outre,"),
    "Paragraph break as in GLOBAL_ISSUES 80.")
add(46, "Proposition (16.9.3), end: 'de n sections de 𝒥 au-dessus de X qui engendre 𝒥'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"sections de $\mathscr{I}$ au-dessus de $X$ qui engendre $\mathscr{I}$ est",
    r"sections de $\mathscr{J}$ au-dessus de $X$ qui engendre $\mathscr{J}$ est", JNOTE)

# ---------------------------------------------------------------- page 47
add(47, "proof of (16.9.3), l. 2: 'la définition donnée dans (0, 15.2.2)'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 15.2.2), compte tenu", r"(\textbf{0}, 15.2.2), compte tenu")
add(47, "proof of (16.9.3), l. 2: 'des homomorphismes canoniques (0, 15.2.1.1)'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 15.2.1.1). La", r"(\textbf{0}, 15.2.1.1). La")
add(47, "Corollaire (16.9.4): '𝒥 un Idéal de O_X. Pour que 𝒥 soit quasi-régulier'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    L(r"$\mathscr{I}$ un Idéal de", r"$\mathcal{O}_X$. Pour que $\mathscr{I}$ soit"),
    L(r"$\mathscr{J}$ un Idéal de", r"$\mathcal{O}_X$. Pour que $\mathscr{J}$ soit"), JNOTE)
add(47, "Corollaire (16.9.4), label (i)", "upright '(i)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(i)] $", r"\item[\textup{(i)}] $")
add(47, "Corollaire (16.9.4) (i): '𝒥 est de type fini.'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"\mathscr{I}$ est de type fini.", r"\mathscr{J}$ est de type fini.", JNOTE)
add(47, "Corollaire (16.9.4), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)] $", r"\item[\textup{(ii)}] $")
add(47, "Corollaire (16.9.4) (ii): '𝒥/𝒥² est un (O_X/𝒥)-Module'",
    "script J three times", "\\mathscr{I} three times", "symbol", None, "high",
    L(r"\mathscr{I}/\mathscr{I}^2$ est un", r"  $(\mathcal{O}_X/\mathscr{I})$-Module"),
    L(r"\mathscr{J}/\mathscr{J}^2$ est un", r"  $(\mathcal{O}_X/\mathscr{J})$-Module"), JNOTE)
add(47, "Corollaire (16.9.4), label (iii)", "upright '(iii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(iii)] L'homomorphisme", r"\item[\textup{(iii)}] L'homomorphisme")
add(47, "display (16.9.4.1): S^•_{O_X/𝒥}(𝒥/𝒥²) → 𝒢r^•_𝒥(O_X)",
    "script J four times (crop p47_s2_Ssub.png)", "\\mathscr{I} four times", "symbol", None, "high",
    L(r"\mathbf{S}_{\mathcal{O}_X/\mathscr{I}}^{\bullet}",
      r"    (\mathscr{I}/\mathscr{I}^2)",
      r"    \longrightarrow\mathscr{G}r_{\mathscr{I}}^{\bullet}(\mathcal{O}_X)"),
    L(r"\mathbf{S}_{\mathcal{O}_X/\mathscr{J}}^{\bullet}",
      r"    (\mathscr{J}/\mathscr{J}^2)",
      r"    \longrightarrow\mathscr{G}r_{\mathscr{J}}^{\bullet}(\mathcal{O}_X)"), JNOTE)
add(47, "proof of (16.9.4): 'en un point x∈Supp(O_X/𝒥)'",
    "script J (crop p47_s2_right.png)", "\\mathscr{I}", "symbol", None, "high",
    r"\operatorname{Supp}(\mathcal{O}_X/\mathscr{I})$, il",
    r"\operatorname{Supp}(\mathcal{O}_X/\mathscr{J})$, il", JNOTE)
add(47, "proof of (16.9.4): 'n sections f_i (1≤i≤n) de 𝒥 au-dessus de U'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"de $\mathscr{I}$ au-dessus de $U$", r"de $\mathscr{J}$ au-dessus de $U$", JNOTE)
add(47, "proof of (16.9.4): 'images canoniques dans 𝒥/𝒥² forment une base de'",
    "script J twice (crop p47_s2_left.png)", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\mathscr{I}/\mathscr{I}^2$ forment une base de",
    r"$\mathscr{J}/\mathscr{J}^2$ forment une base de", JNOTE)
add(47, "proof of (16.9.4): '(𝒥/𝒥²)|U sur'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$(\mathscr{I}/\mathscr{I}^2)|U$ sur", r"$(\mathscr{J}/\mathscr{J}^2)|U$ sur", JNOTE)
add(47, "proof of (16.9.4): '(O_X/𝒥)|U, alors'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"$(\mathcal{O}_X/\mathscr{I})|U$, alors", r"$(\mathcal{O}_X/\mathscr{J})|U$, alors", JNOTE)
add(47, "proof of (16.9.4): 'les f_i|V engendrent 𝒥|V'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendrent $\mathscr{I}|V$", r"engendrent $\mathscr{J}|V$", JNOTE)
add(47, "proof of (16.9.4): 'on a 𝒥_x≠O_x, donc 𝒥_x est contenu'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\mathscr{I}_x\neq\mathcal{O}_x$, donc $\mathscr{I}_x$ est",
    r"$\mathscr{J}_x\neq\mathcal{O}_x$, donc $\mathscr{J}_x$ est", JNOTE)
add(47, "proof of (16.9.4): 'comme 𝒥_x est un O_x-module'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"comme $\mathscr{I}_x$ est un", r"comme $\mathscr{J}_x$ est un", JNOTE)
add(47, "proof of (16.9.4): 'dans 𝒥_x/𝒥_x² engendrent cet'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\mathscr{I}_x/\mathscr{I}_x^2$ engendrent cet", r"$\mathscr{J}_x/\mathscr{J}_x^2$ engendrent cet", JNOTE)
add(47, "proof of (16.9.4): '(O_x/𝒥_x)-module, le lemme de Nakayama'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"$(\mathcal{O}_x/\mathscr{I}_x)$-module, le lemme", r"$(\mathcal{O}_x/\mathscr{J}_x)$-module, le lemme", JNOTE)
add(47, "proof of (16.9.4): 'engendrent 𝒥_x. Comme 𝒥 est de type fini'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"engendrent $\mathscr{I}_x$. Comme $\mathscr{I}$ est de type fini,",
    r"engendrent $\mathscr{J}_x$. Comme $\mathscr{J}$ est de type fini,", JNOTE)
add(47, "proof of (16.9.4), end: 'on conclut par (0_I, 5.2.2).'",
    "bold 0 with subscript I", "0\\textsubscript{I}: plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 5.2.2).", r"($\mathbf{0}_{\mathrm I}$, 5.2.2).")
add(47, "Corollaire (16.9.5): '𝒥 un Idéal quasi-régulier'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    L(r"$\mathscr{I}$ un Idéal", r"quasi-régulier"), L(r"$\mathscr{J}$ un Idéal", r"quasi-régulier"), JNOTE)
add(47, "Corollaire (16.9.5): 'une suite de sections de 𝒥 au-dessus de X'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"sections de $\mathscr{I}$ au-dessus de $X$,", r"sections de $\mathscr{J}$ au-dessus de $X$,", JNOTE)
add(47, "Corollaire (16.9.5): 'x un point de Supp(O_X/𝒥)'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"\operatorname{Supp}(\mathcal{O}_X/\mathscr{I})$. Les",
    r"\operatorname{Supp}(\mathcal{O}_X/\mathscr{J})$. Les", JNOTE)
add(47, "Corollaire (16.9.5), label a)", "upright 'a)' without an opening parenthesis",
    "\\item[(a)]: italic '(a)'", "punctuation", None, "high",
    r"\item[(a)]", r"\item[\textup{a)}]", "Same form as the earlier page fixes of lettered labels in italic statements (GLOBAL_ISSUES 88).")
add(47, "Corollaire (16.9.5) a): 'engendrant 𝒥|U.'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendrant $\mathscr{I}|U$.", r"engendrant $\mathscr{J}|U$.", JNOTE)
add(47, "Corollaire (16.9.5), label b)", "upright 'b)' without an opening parenthesis",
    "\\item[(b)]: italic '(b)'", "punctuation", None, "high", r"\item[(b)]", r"\item[\textup{b)}]")
add(47, "Corollaire (16.9.5) b): 'générateurs de 𝒥_x dont le nombre'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"$\mathscr{I}_x$ dont le nombre", r"$\mathscr{J}_x$ dont le nombre", JNOTE)
add(47, "Corollaire (16.9.5), label b')", "upright \"b')\" without an opening parenthesis",
    "\\item[(b')]: italic \"(b')\"", "punctuation", None, "high", r"\item[(b')]", r"\item[\textup{b$'$)}]")
add(47, "Corollaire (16.9.5) b'): 'système minimal de générateurs de 𝒥_x'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    L(r"minimal de générateurs de", r"  $\mathscr{I}_x$"), L(r"minimal de générateurs de", r"  $\mathscr{J}_x$"), JNOTE)
add(47, "Corollaire (16.9.5), label c)", "upright 'c)' without an opening parenthesis",
    "\\item[(c)]: italic '(c)'", "punctuation", None, "high", r"\item[(c)]", r"\item[\textup{c)}]")
add(47, "Corollaire (16.9.5) c): 'Γ(X, 𝒥/𝒥²)'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\Gamma(X,\mathscr{I}/\mathscr{I}^2)$", r"$\Gamma(X,\mathscr{J}/\mathscr{J}^2)$", JNOTE)
add(47, "Corollaire (16.9.5) c): 'une base du (O_x/𝒥_x)-module'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"du $(\mathcal{O}_x/\mathscr{I}_x)$-module", r"du $(\mathcal{O}_x/\mathscr{J}_x)$-module", JNOTE)
add(47, "Corollaire (16.9.5) c), end: '𝒥_x/𝒥_x².'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    L(r"$\mathscr{I}_x/\mathscr{I}_x^2$.", r"\end{enumerate}"),
    L(r"$\mathscr{J}_x/\mathscr{J}_x^2$.", r"\end{enumerate}"), JNOTE)
add(47, "proof of (16.9.5), l. 1: '𝒥_x un idéal de type fini'",
    "script J (crop p47_s3_beq.png)", "\\mathscr{I}", "symbol", None, "high",
    r"$\mathscr{I}_x$ un idéal", r"$\mathscr{J}_x$ un idéal", JNOTE)
add(47, "proof of (16.9.5): 'l'équivalence de b), b') et c) résulte'",
    "the labels b), b') and c) italic (crop p47_s3_labels1.png)", "upright", "italics", None, "high",
    r"de b), b') et c) résulte", r"de \emph{b)}, \emph{b')} et \emph{c)} résulte")
add(47, "proof of (16.9.5): 'Il est clair que a) entraîne c)'",
    "a) and c) italic (crop p47_s3_labels2.png)", "upright", "italics", None, "high",
    r"que a) entraîne c) en", r"que \emph{a)} entraîne \emph{c)} en")
add(47, "proof of (16.9.5): 'il résulte de (0_I, 5.2.2) que si'",
    "bold 0 with subscript I (crop p47_s4_0I522.png)", "0\\textsubscript{I}: plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 5.2.2) que si", r"($\mathbf{0}_{\mathrm I}$, 5.2.2) que si",
    "The print shows no point between 5 and 2.2 (gap at its place); taken as a point that did not print, not reported.")
add(47, "proof of (16.9.5): 'la condition c) est vérifiée (donc aussi b))'",
    "c) and b) italic, the last parenthesis roman (crop p47_s4_labels3.png)", "upright", "italics", None, "high",
    r"condition c) est vérifiée (donc aussi b))",
    r"condition \emph{c)} est vérifiée (donc aussi \emph{b)})")
add(47, "proof of (16.9.5): '(𝒥/𝒥²)|U ait un rang constant'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$(\mathscr{I}/\mathscr{I}^2)|U$ ait", r"$(\mathscr{J}/\mathscr{J}^2)|U$ ait", JNOTE)
add(47, "proof of (16.9.5): 'les f_i|U engendrent 𝒥|U; il suffit'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendrent $\mathscr{I}|U$; il suffit", r"engendrent $\mathscr{J}|U$; il suffit", JNOTE)
add(47, "Remarques (16.9.6) (i): 'une base du (O_y/𝒥_y)-module'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"$(\mathcal{O}_y/\mathscr{I}_y)$-module", r"$(\mathcal{O}_y/\mathscr{J}_y)$-module", JNOTE)
add(47, "Remarques (16.9.6) (i): '𝒥_y/𝒥_y²'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\mathscr{I}_y/\mathscr{I}_y^2$", r"$\mathscr{J}_y/\mathscr{J}_y^2$", JNOTE)
add(47, "Remarques (16.9.6) (i): 'pour tout y∈X'",
    "'tout' italic in the roman remark", "roman (judged with the remark body roman)", "italics", None, "high",
    r"pour tout $y", r"pour \emph{tout} $y")
add(47, "Remarques (16.9.6) (i): 'pour que la suite (f_i) engendre 𝒥.'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendre $\mathscr{I}$. On en a", r"engendre $\mathscr{J}$. On en a", JNOTE)

# ---------------------------------------------------------------- page 48
add(48, "Remarques (16.9.6) (i), l. 1: '𝒥 = 𝔍~, où 𝔍 est un idéal premier'",
    "script J, then Fraktur J twice (crop p48_s1_frak1.png)", "\\mathscr{I}, \\mathfrak{I} twice",
    "symbol", None, "high",
    r"$\mathscr{I}=\widetilde{\mathfrak{I}}$, où $\mathfrak{I}$ est",
    r"$\mathscr{J}=\widetilde{\mathfrak{J}}$, où $\mathfrak{J}$ est",
    "Wrong letters: script J and Fraktur J (descenders), as in the rest of 16.9 (GLOBAL_ISSUES 91).")
add(48, "Remarques (16.9.6) (i), l. 1: 'un idéal premier non principal de A'",
    "'non principal' italic (crop p48_s1_frak1.png)", "roman (judged with the remark body roman)", "italics", None, "high",
    r"premier non principal de", r"premier \emph{non principal} de")
add(48, "Remarques (16.9.6) (i): '𝒥_y/𝒥_y²=0'",
    "script J twice (crop p48_s1_l2.png)", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\mathscr{I}_y/\mathscr{I}_y^2=0$", r"$\mathscr{J}_y/\mathscr{J}_y^2=0$", JNOTE)
add(48, "Remarques (16.9.6) (i): 'correspondant à 𝔍, et 𝒥_x/𝒥_x²'",
    "Fraktur J (4x crop p48_s1_frak7.png), then script J twice", "\\mathfrak{I}, \\mathscr{I} twice",
    "symbol", None, "high",
    L(r"correspondant à $\mathfrak{I}$, et", r"  $\mathscr{I}_x/\mathscr{I}_x^2$"),
    L(r"correspondant à $\mathfrak{J}$, et", r"  $\mathscr{J}_x/\mathscr{J}_x^2$"),
    "Wrong letters: Fraktur J and script J (GLOBAL_ISSUES 91).")
add(48, "Remarques (16.9.6) (i): 'sur le corps O_x/𝒥_x; en outre 𝒥 est'",
    "script J twice", "\\mathscr{I} twice", "symbol", None, "high",
    r"$\mathcal{O}_x/\mathscr{I}_x$; en outre $\mathscr{I}$ est",
    r"$\mathcal{O}_x/\mathscr{J}_x$; en outre $\mathscr{J}$ est", JNOTE)
add(48, "Remarques (16.9.6) (ii): 'La suite (f_1, f_2) est régulière dans A'",
    "'régulière' italic (crop p48_s1_reguliere.png)", "roman", "italics", None, "high",
    r"est régulière dans $A$: en effet", r"est \emph{régulière} dans $A$: en effet")
add(48, "Remarques (16.9.6) (ii): 'la suite (f_2, f_1) n'est pas régulière dans A'",
    "'n'est pas régulière' italic (crop p48_s2_nestpas.png)", "roman", "italics", None, "high",
    r"n'est pas régulière dans $A$; d'autre", r"\emph{n'est pas régulière} dans $A$; d'autre")
add(48, "Remarques (16.9.6) (ii): 'l'idéal 𝔍=f_1A+f_2A'",
    "Fraktur J (4x crop p48_s2_frak32.png)", "\\mathfrak{I}", "symbol", None, "high",
    r"l'idéal $\mathfrak{I}=f_1A+f_2A$", r"l'idéal $\mathfrak{J}=f_1A+f_2A$", FJNOTE)
add(48, "Remarques (16.9.6) (ii): 'les conditions b), b') et c) de (16.9.5)'",
    "the labels italic (crop p48_s2_bbc.png)", "upright", "italics", None, "high",
    r"b), b') et c) de (16.9.5)", r"\emph{b)}, \emph{b')} et \emph{c)} de (16.9.5)")
add(48, "Remarques (16.9.6) (ii): 'la condition a) lorsqu'on'",
    "'a)' italic (crop p48_s2_a.png)", "upright", "italics", None, "high",
    r"la condition a) lorsqu'on", r"la condition \emph{a)} lorsqu'on")
add(48, "(16.9.7), l. 1: 'nous dirons qu'un idéal 𝔍 de A'",
    "Fraktur J (crop p48_s2_frakJ.png)", "\\mathfrak{I}", "symbol", None, "high",
    L(r"qu'un idéal", r"$\mathfrak{I}$ de $A$"), L(r"qu'un idéal", r"$\mathfrak{J}$ de $A$"), FJNOTE)
add(48, "(16.9.7): 'est régulier (resp. quasi-régulier) si l'Idéal'",
    "'régulier' and 'quasi-régulier' italic, '(resp.' roman (crop p48_s2_1697.png)", "roman", "italics", None, "high",
    r"est régulier (resp. quasi-régulier) si", r"est \emph{régulier} (resp. \emph{quasi-régulier}) si",
    "The second 'est régulier (resp. quasi-régulier)' of the sentence is roman in the print, as in the TeX.")
add(48, "(16.9.7): 'si l'Idéal 𝒥 = 𝔍~ de O_X'",
    "script J and Fraktur J", "\\mathscr{I}, \\mathfrak{I}", "symbol", None, "high",
    r"$\mathscr{I}=\widetilde{\mathfrak{I}}$ de", r"$\mathscr{J}=\widetilde{\mathfrak{J}}$ de",
    "Wrong letters: script J and Fraktur J (GLOBAL_ISSUES 91).")
add(48, "(16.9.7): 'cette notion est locale'",
    "'locale' italic", "roman", "italics", None, "high", r"est locale et", r"est \emph{locale} et")
add(48, "(16.9.7): 'l'existence d'un système de générateurs de 𝔍'",
    "'système de générateurs de' italic", "roman", "italics", None, "high",
    r"d'un système de générateurs de", r"d'un \emph{système de générateurs de}")
add(48, "(16.9.7): 'générateurs de 𝔍 formant'",
    "Fraktur J (crop p48_s2_1697.png)", "\\mathfrak{I}", "symbol", None, "high",
    r"$\mathfrak{I}$ formant", r"$\mathfrak{J}$ formant", FJNOTE)
add(48, "(16.9.7): 'lorsque A est local (16.9.5)'",
    "'local' italic", "roman", "italics", None, "high", r"est local (16.9.5)", r"est \emph{local} (16.9.5)")
add(48, "Proposition (16.9.8), label (i)", "upright '(i)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(i)] $j$ est", r"\item[\textup{(i)}] $j$ est")
add(48, "Proposition (16.9.8), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)] Le faisceau", r"\item[\textup{(ii)}] Le faisceau")
add(48, "Proposition (16.9.8) (ii): 'Le faisceau conormal 𝒢r¹(j) = N_{Y/X}'",
    "script G with italic r (3x crop p48_s3_Gr1.png), as in 𝒢r^•_𝒥 on pp. 46-47",
    "\\operatorname{Gr}: roman Gr", "symbol", None, "high",
    r"$\operatorname{Gr}^1(j)=\mathcal{N}_{Y/X}$", r"$\mathscr{G}r^1(j)=\mathcal{N}_{Y/X}$",
    "Written as the edition's other 𝒢r (\\mathscr{G}r).")
add(48, "Proposition (16.9.8) (ii): 'N_{Y/X} (16.1.2) est un O_Y-Module'",
    "reference upright (crop p48_s3_ii.png)", "italic (inside the italic statement)", "convention", 6, "high",
    L(r"(16.1.2) est un", r"  $\mathcal{O}_Y$-Module"), L(r"\textup{(16.1.2)} est un", r"  $\mathcal{O}_Y$-Module"))
add(48, "Proposition (16.9.8), label (iii)", "upright '(iii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(iii)] L'homomorphisme", r"\item[\textup{(iii)}] L'homomorphisme")
add(48, "Proposition (16.9.8) (iii), display: 'S^•_{O_Y}(...)'",
    "bold upright S, as in the displays of (16.9.3) and (16.9.4.1) (crop p48_s3_prop.png)",
    "\\operatorname{S}: light upright S", "font", None, "high",
    r"\operatorname{S}_{\mathcal{O}_Y}^{\bullet}", r"\mathbf{S}_{\mathcal{O}_Y}^{\bullet}",
    "The only \\operatorname{S} in ega4-16 (GLOBAL_ISSUES 93: bold S).")
add(48, "Proposition (16.9.8) (iii), display: '(𝒢r¹(j)) → 𝒢r^•(j)'",
    "script G with italic r, twice", "\\operatorname{Gr} twice", "symbol", None, "high",
    r"(\operatorname{Gr}^1(j))\longrightarrow\operatorname{Gr}^{\bullet}(j)",
    r"(\mathscr{G}r^1(j))\longrightarrow\mathscr{G}r^{\bullet}(j)")
add(48, "Proposition (16.9.8) (iii): '(16.1.2.2) est bijectif.'",
    "reference upright", "italic (inside the italic statement)", "convention", 6, "high",
    r"(16.1.2.2) est bijectif.", r"\textup{(16.1.2.2)} est bijectif.")
add(48, "proof of (16.9.8): 'de l'explicitation de 𝒢r¹(j) et 𝒢r^•(j)'",
    "script G with italic r, twice", "\\operatorname{Gr} twice", "symbol", None, "high",
    r"$\operatorname{Gr}^1(j)$ et $\operatorname{Gr}^{\bullet}(j)$",
    r"$\mathscr{G}r^1(j)$ et $\mathscr{G}r^{\bullet}(j)$")
add(48, "proof of (16.9.8): 'en termes de l'Idéal 𝒥 de O_X'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"l'Idéal $\mathscr{I}$ de $\mathcal{O}_X$ définissant", r"l'Idéal $\mathscr{J}$ de $\mathcal{O}_X$ définissant", JNOTE)
add(48, "Corollaire (16.9.9): 'invariant normal A^(n) de j (16.1.2) est une'",
    "reference upright (crop p48_s3_lim2.png)", "italic (inside the italic statement)", "convention", 6, "high",
    r"(16.1.2) est une", r"\textup{(16.1.2)} est une")
add(48, "Corollaire (16.9.9): 'O_Y-Algèbre augmentée (16.1.7); posons'",
    "reference upright (crop p48_s3_l3.png)", "italic (inside the italic statement)", "convention", 6, "high",
    r"augmentée (16.1.7); posons", r"augmentée \textup{(16.1.7)}; posons")
add(48, "proof of (16.9.9): 'une Algèbre quotient O_X/𝒥'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"$\mathcal{O}_X/\mathscr{I}$ et l'homomorphisme", r"$\mathcal{O}_X/\mathscr{J}$ et l'homomorphisme", JNOTE)

# ---------------------------------------------------------------- page 49
add(49, "l. 2: 'l'idéal d'augmentation 𝔍 étant de type fini'",
    "Fraktur J (crop p49_s1_top.png)", "\\mathfrak{I}", "symbol", None, "high",
    r"d'augmentation $\mathfrak{I}$ étant", r"d'augmentation $\mathfrak{J}$ étant", FJNOTE)
add(49, "l. 3: '(B/𝔍^{n+1})~'",
    "Fraktur J", "\\mathfrak{I}", "symbol", None, "high",
    r"$(B/\mathfrak{I}^{n+1})^{\sim}$", r"$(B/\mathfrak{J}^{n+1})^{\sim}$", FJNOTE)
add(49, "l. 3-4: 'l'équivalence de b) et c) dans (0, 19.5.4)'",
    "b) and c) italic (crop p49_s1_top.png)", "upright", "italics", None, "high",
    L(r"de b)", r"et c) dans"), L(r"de \emph{b)}", r"et \emph{c)} dans"))
add(49, "l. 4: 'dans (0, 19.5.4) puisque'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"dans (0, 19.5.4) puisque", r"dans (\textbf{0}, 19.5.4) puisque")
add(49, "l. 4: 'puisque B/𝔍 = A'",
    "Fraktur J", "\\mathfrak{I}", "symbol", None, "high",
    r"$B/\mathfrak{I}=A$", r"$B/\mathfrak{J}=A$", FJNOTE)
add(49, "'en vertu de (0, 19.5.4), à dire que'",
    "bold 0", "plain 0", "convention", 2, "high",
    r"de (0, 19.5.4), à dire", r"de (\textbf{0}, 19.5.4), à dire")
add(49, "'une A-algèbre formellement lisse'",
    "'formellement lisse' italic (crop p49_s1_preadique.png)", "roman", "italics", None, "high",
    r"algèbre formellement lisse pour", r"algèbre \emph{formellement lisse} pour")
add(49, "'pour la topologie 𝔍-préadique'",
    "Fraktur J (crop p49_s1_preadique.png)", "\\mathfrak{I}", "symbol", None, "high",
    L(r"topologie", r"$\mathfrak{I}$"), L(r"topologie", r"$\mathfrak{J}$"), FJNOTE)
add(49, "'pour la topologie 𝔍-préadique'",
    "'préadique', no hyphen after 'pré' (crop p49_s1_preadique.png)", "'pré-adique'", "word", None, "high",
    r"-pré-adique.", r"-préadique.")
add(49, "Proposition (16.9.10), label (i)", "upright '(i)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(i)] Pour qu'il", r"\item[\textup{(i)}] Pour qu'il")
add(49, "Proposition (16.9.10) (i): 'le noyau 𝒥_y de l'homomorphisme surjectif'",
    "script J (crop p49_s2_prop.png)", "\\mathscr{I}", "symbol", None, "high",
    r"le noyau $\mathscr{I}_y$ de l'homomorphisme", r"le noyau $\mathscr{J}_y$ de l'homomorphisme", JNOTE)
add(49, "Proposition (16.9.10), label (ii)", "upright '(ii)'", "italic (inside the italic statement)",
    "convention", 6, "high", r"\item[(ii)] Pour que", r"\item[\textup{(ii)}] Pour que")
add(49, "proof of (16.9.10) (i): 'un Idéal cohérent 𝒥 de O_X'",
    "script J (crop p49_s2_proof.png)", "\\mathscr{I}", "symbol", None, "high",
    r"\emph{cohérent} $\mathscr{I}$", r"\emph{cohérent} $\mathscr{J}$", JNOTE)
add(49, "proof of (16.9.10) (i): 'Inversement, si 𝒥_y est engendré'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"si $\mathscr{I}_y$", r"si $\mathscr{J}_y$", JNOTE)
add(49, "proof of (16.9.10) (i): 'des sections de 𝒥 au-dessus d'un voisinage'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"sections de $\mathscr{I}$ au-dessus", r"sections de $\mathscr{J}$ au-dessus", JNOTE)
add(49, "proof of (16.9.10) (i): 'les s_i engendrent 𝒥|U'",
    "script J", "\\mathscr{I}", "symbol", None, "high",
    r"engendrent $\mathscr{I}|U$", r"engendrent $\mathscr{J}|U$", JNOTE)
add(49, "proof of (16.9.10) (i): 'engendrent J|U (0_I, 5.2.2)'",
    "bold 0 with subscript I", "0\\textsubscript{I}: plain 0", "convention", 2, "high",
    r"(0\textsubscript{I}, 5.2.2) et forment", r"($\mathbf{0}_{\mathrm I}$, 5.2.2) et forment")
add(49, "proof of (16.9.10) (i): 'une suite régulière (0, 15.2.4)'",
    "bold 0", "plain 0", "convention", 2, "high", r"(0, 15.2.4)", r"(\textbf{0}, 15.2.4)")
add(49, "proof of (16.9.10) (ii): 'de l'idéal maximal (0, 15.1.11)'",
    "bold 0", "plain 0", "convention", 2, "high", r"(0, 15.1.11)", r"(\textbf{0}, 15.1.11)")
add(49, "'Lorsque (sans hypothèse noethérienne sur X) le noyau 𝒥_y'",
    "script J (crop p49_s3_OXY.png)", "\\mathscr{I}", "symbol", None, "high",
    r"noethérienne sur $X$) le noyau $\mathscr{I}_y$", r"noethérienne sur $X$) le noyau $\mathscr{J}_y$", JNOTE)
add(49, "'engendré par une suite régulière d'éléments de O_{X,Y}, on dit'",
    "O_{X,Y} with a capital roman Y (4x crop p49_s3_OXY_zoom.png); the line above, in the same sentence, has O_{X,y} → O_{Y,y} with a lower-case y",
    "\\mathcal{O}_{X,y}: silent correction", "misprint_in_print", None, "high",
    r"$\mathcal{O}_{X,y}$, on dit", r"$\mathcal{O}_{X,Y}$, on dit",
    "The local ring at the point y is meant. The fix restores the printed reading.",
    corrected=r"$\mathcal{O}_{X,y}$")
add(49, "Remarques (16.9.12) (ii): 'il résulte aussitôt de (16.9.4) et de (0, 17.1.1)'",
    "bold 0", "plain 0", "convention", 2, "high", r"(0, 17.1.1)", r"(\textbf{0}, 17.1.1)")
add(49, "Remarques (16.9.12) (ii), end: 'l'injection canonique Spec(k(x)) → X'",
    "bold italic k", "plain k", "convention", 1, "high",
    r"\operatorname{Spec}(k(x))", r"\operatorname{Spec}(\boldsymbol{k}(x))")


# ---------------------------------------------------------------- checks
def page_text(p):
    return (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
for p in range(45, 50):
    orig = page_text(p)
    cur = orig
    for i, f in enumerate([f for f in F if f["page"] == p]):
        if f["fix"] is None:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        n_now = cur.count(old)
        n_orig = orig.count(old)
        if n_now != 1:
            ok = False
            print(f"p{p} #{i}: old occurs {n_now} times at application: {old!r}")
        if n_orig != 1:
            print(f"p{p} #{i}: note: old occurs {n_orig} times in the untouched page: {old[:60]!r}")
        cur = cur.replace(old, new, 1)
    # leftovers of the letters every occurrence of which is J in the print
    left_s = cur.count(r"\mathscr{I}")
    left_f = cur.count(r"\mathfrak{I}")
    print(f"p{p}: script I before {orig.count(chr(92)+'mathscr{I}')} after {left_s}; "
          f"fraktur I before {orig.count(chr(92)+'mathfrak{I}')} after {left_f}")
    (Path(__file__).resolve().parent / f"applied_{p:03d}.tex").write_text(cur, encoding="utf-8")

kinds = {}
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    kinds.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(kinds)
if not ok:
    sys.exit(1)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("wrote", OUT, len(F))
