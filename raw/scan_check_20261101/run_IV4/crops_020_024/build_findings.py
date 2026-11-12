"""Build and verify findings_020_024.json (scan check of EGA IV-4 pp. 20-24).

Writes the JSON only after every fix's "old" has been found exactly once in its
page (CRLF stripped), both in the original page text and at the moment it is
applied in list order.
"""
import json
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
OUT = RUN / "findings_020_024.json"


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


BOLD_S = ("bold upright S (symmetric algebra), as in EGA II; enlarged crops")
BOLD_S_NOTE = ("ega4-16 writes the print's bold S of the symmetric algebra as \\mathscr{S} "
               "(script S) throughout; document-wide candidate \\mathscr{S} -> \\mathbf{S}.")
OMEGA_NOTE = ("The print sets the sheaf of differentials Omega^1_{X/S} with an italic capital "
              "omega and the module Omega^1_{B/A} upright (both on p. 23, (16.4.16.2)); "
              "\\varOmega (amsmath) gives the italic shape. Document-wide decision needed.")

# ---------------------------------------------------------------- page 20
p = 20
add(p, "proof of (16.4.8): 'on prend u(s)=(—s, s)'",
    "u(s)=(—s, s): long dash for the unary minus (enlarged crop; longer than the bar of s+t)",
    "$u(s)=(-s,s)$", "convention", 7, "high",
    r"$u(s)=(-s,s)$", r"$u(s)=(\setmin s,s)$",
    "Long dash used for a minus sign (GLOBAL_ISSUES 23/49); \\setmin pending the convention-7 decision.")
add(p, "proof of (16.4.8): display X×_S X = Spec(S(E)⊗S(E)) = Spec(S(E⊕E))",
    BOLD_S + " (three S)", "\\mathscr{S} three times", "font", None, "high",
    L(r"(\mathscr{S}_{\mathcal{O}_S}(\mathscr{E})\otimes_{\mathcal{O}_S}",
      r"  \mathscr{S}_{\mathcal{O}_S}(\mathscr{E}))",
      r"  =\operatorname{Spec}(\mathscr{S}_{\mathcal{O}_S}"),
    L(r"(\mathbf{S}_{\mathcal{O}_S}(\mathscr{E})\otimes_{\mathcal{O}_S}",
      r"  \mathbf{S}_{\mathcal{O}_S}(\mathscr{E}))",
      r"  =\operatorname{Spec}(\mathbf{S}_{\mathcal{O}_S}"),
    BOLD_S_NOTE)
add(p, "proof of (16.4.8): '(II, 1.4.6 et 1.7.11)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 1.4.6 et 1.7.11)", r"(\textbf{II}, 1.4.6 et 1.7.11)")
add(p, "proof of (16.4.8): '(II, 1.2.7)'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 1.2.7)", r"(\textbf{II}, 1.2.7)")
add(p, "proof of (16.4.8): 'S(v) : S_{O_S}(E⊕E) → S_{O_S}(E)'",
    BOLD_S + " (three S)", "\\mathscr{S} three times", "font", None, "high",
    L(r"$\mathscr{S}(v):\mathscr{S}_{\mathcal{O}_S}(\mathscr{E}\oplus\mathscr{E})",
      r"\to\mathscr{S}_{\mathcal{O}_S}(\mathscr{E})$"),
    L(r"$\mathbf{S}(v):\mathbf{S}_{\mathcal{O}_S}(\mathscr{E}\oplus\mathscr{E})",
      r"\to\mathbf{S}_{\mathcal{O}_S}(\mathscr{E})$"),
    BOLD_S_NOTE)
add(p, "proof of (16.4.8): '(II, 1.7.4), de sorte que'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 1.7.4), de sorte", r"(\textbf{II}, 1.7.4), de sorte")
add(p, "proof of (16.4.8): 'si J est le noyau de cet homomorphisme'",
    "script J (𝒥, with a descender below the baseline; 4x crop p20_s2_siJ.png), not the script I (ℐ) of Lemme (16.4.8.3)",
    "\\mathscr{I}", "symbol", None, "high",
    r"$\mathscr{I}$ est le noyau", r"$\mathscr{J}$ est le noyau",
    "The print names this kernel 𝒥 in the proof of (16.4.8) and the kernel of the lemma ℐ; both letters "
    "appear in one proof on this page, so the shapes are distinct (compare p20_s4_I.png and p20_s4_Jprime.png).")
add(p, "proof of (16.4.8), display: 'P^n_{X/S} = f^*(S_{O_S}(E⊕E)/J^{n+1})'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    r"f^*(\mathscr{S}_{\mathcal{O}_S}", r"f^*(\mathbf{S}_{\mathcal{O}_S}", BOLD_S_NOTE)
add(p, "proof of (16.4.8), same display: '/J^{n+1}'",
    "script J (𝒥) with descender (crop p20_s2_disp.png)", "\\mathscr{I}^{n+1}", "symbol", None, "high",
    r"(\mathscr{E}\oplus\mathscr{E})/\mathscr{I}^{n+1}", r"(\mathscr{E}\oplus\mathscr{E})/\mathscr{J}^{n+1}",
    "Same ideal 𝒥 as in 'si 𝒥 est le noyau'.")
add(p, "Lemme (16.4.8.3): 'Soit I l'Idéal noyau de S(v) :' followed by the displayed 'S_{O_Y}(F) → S_{O_Y}(F''),'",
    "the map S_{O_Y}(F) → S_{O_Y}(F''), is a centred display after 'S(v) :'; 'et soit' starts the next line",
    "inline: $\\mathscr{S}(v):\\mathscr{S}_{\\mathcal{O}_Y}(\\mathscr{F})\\to\\mathscr{S}_{\\mathcal{O}_Y}(\\mathscr{F}'')$, et soit",
    "other", None, "high",
    L(r"$\mathscr{S}(v):\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F})\to",
      r"\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F}'')$, et soit"),
    L(r"$\mathbf{S}(v)$:",
      r"\[",
      r"  \mathbf{S}_{\mathcal{O}_Y}(\mathscr{F})\to\mathbf{S}_{\mathcal{O}_Y}(\mathscr{F}''),",
      r"\]",
      r"et soit"),
    "Display where the TeX has the formula inline; no words differ. The edit also writes the three bold S "
    "of this formula (next entry).")
add(p, "Lemme (16.4.8.3): S(v), S_{O_Y}(F), S_{O_Y}(F'')",
    BOLD_S + " (three S)", "\\mathscr{S} three times", "font", None, "high",
    None, None, "Covered by the edit of the preceding entry (display), which writes \\mathbf{S}.")
add(p, "Lemme (16.4.8.3): 'et soit gr^•_I(S_{O_Y}(F)) la O_Y-Algèbre graduée'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    L(r"\operatorname{gr}_{\mathscr{I}}^\bullet", r"(\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F}))$ la"),
    L(r"\operatorname{gr}_{\mathscr{I}}^\bullet", r"(\mathbf{S}_{\mathcal{O}_Y}(\mathscr{F}))$ la"),
    BOLD_S_NOTE)
add(p, "Lemme (16.4.8.3): 'associée à la O_Y-Algèbre S_{O_Y}(F)'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    L(r"associée à la $\mathcal{O}_Y$-Algèbre", r"$\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F})$"),
    L(r"associée à la $\mathcal{O}_Y$-Algèbre", r"$\mathbf{S}_{\mathcal{O}_Y}(\mathscr{F})$"),
    BOLD_S_NOTE)
add(p, "Lemme (16.4.8.3): 'munie de la filtration I-préadique.'",
    "'munie de la filtra-/tion I-préadique' printed roman inside the italic lemma (crop p20_s2_lemma.png); "
    "'Alors l'homomorphisme' italic again",
    "set italic by the lemma environment", "convention", 6, "high",
    L(r"munie de la filtration", r"$\mathscr{I}$-préadique"),
    L(r"\textup{munie de la filtration", r"$\mathscr{I}$-préadique}"),
    "Roman emphasis inside the italic statement (the I-preadic filtration, not the canonical graduation of S(F)).")
add(p, "Lemme (16.4.8.3), display (16.4.8.4)",
    BOLD_S + " (three S)", "\\mathscr{S} three times", "font", None, "high",
    L(r"  \mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')",
      r"  \otimes_{\mathcal{O}_Y}",
      r"  \mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')",
      r"  \longrightarrow",
      r"  \operatorname{gr}_{\mathscr{I}}^\bullet",
      r"  (\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F}))",
      r"  \tag{16.4.8.4}"),
    L(r"  \mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')",
      r"  \otimes_{\mathcal{O}_Y}",
      r"  \mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')",
      r"  \longrightarrow",
      r"  \operatorname{gr}_{\mathscr{I}}^\bullet",
      r"  (\mathbf{S}_{\mathcal{O}_Y}(\mathscr{F}))",
      r"  \tag{16.4.8.4}"),
    BOLD_S_NOTE)
add(p, "Lemme (16.4.8.3): '(II, 1.7.4 et 2.1.2)'",
    "bold II; the whole reference upright ('et' roman) inside the italic lemma (crop p20_s3_ou.png)",
    "plain II, set italic by the lemma environment", "convention", 2, "high",
    r"(II, 1.7.4 et 2.1.2)", r"\textup{(\textbf{II}, 1.7.4 et 2.1.2)}",
    "One edit for this finding and the next (convention 6).")
add(p, "Lemme (16.4.8.3): same reference '(II, 1.7.4 et 2.1.2)'",
    "the reference is upright inside the italic lemma", "italic (lemma environment)", "convention", 6, "high",
    None, None, "Covered by the edit of the preceding entry (convention 2), which adds the \\textup.")
add(p, "Lemme (16.4.8.3), display 'F' → I = gr^1_I(S_{O_Y}(F)),'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    L(r"=\operatorname{gr}_{\mathscr{I}}^1", r"  (\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F})),"),
    L(r"=\operatorname{gr}_{\mathscr{I}}^1", r"  (\mathbf{S}_{\mathcal{O}_Y}(\mathscr{F})),"),
    BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'S^•_{O_Y}(F') → gr^•_I(S_{O_Y}(F))'",
    BOLD_S + " (two S)", "\\mathscr{S} twice", "font", None, "high",
    L(r"$\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')\to\allowbreak",
      r"\operatorname{gr}_{\mathscr{I}}^\bullet",
      r"(\mathscr{S}_{\mathcal{O}_Y}(\mathscr{F}))$, et comme"),
    L(r"$\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')\to\allowbreak",
      r"\operatorname{gr}_{\mathscr{I}}^\bullet",
      r"(\mathbf{S}_{\mathcal{O}_Y}(\mathscr{F}))$, et comme"),
    BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'une S^•_{O_Y}(F'')-Algèbre graduée'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    r"une $\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$-Algèbre",
    r"une $\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$-Algèbre", BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'par tensorisation du précédent avec S^•_{O_Y}(F'')'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    r"avec $\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$.",
    r"avec $\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$.", BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'l'Algèbre graduée S^•_{O_Y}(F) s'identifie'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    r"$\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F})$ s'identifie",
    r"$\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F})$ s'identifie", BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'produit tensoriel gradué S^•(F')⊗S^•(F'')'",
    BOLD_S + " (two S)", "\\mathscr{S} twice", "font", None, "high",
    L(r"gradué", r"$\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')", r"\otimes_{\mathcal{O}_Y}",
      r"\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$"),
    L(r"gradué", r"$\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')", r"\otimes_{\mathcal{O}_Y}",
      r"\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$"),
    BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): '(II, 1.7.4), et il est immédiat'", "bold II", "plain II", "convention", 2, "high",
    r"(II, 1.7.4), et il est", r"(\textbf{II}, 1.7.4), et il est")
add(p, "proof of (16.4.8.3): 'I est alors l'Idéal J'⊗_{O_Y} S^•(F'')'",
    "script J' (𝒥', descender; 4x crop p20_s4_Jprime.png), while the unprimed ideal of the same sentence is the script I",
    "\\mathscr{I}'", "symbol", None, "high",
    r"$\mathscr{I}'\otimes_{\mathcal{O}_Y}", r"$\mathscr{J}'\otimes_{\mathcal{O}_Y}",
    "The print writes the augmentation ideal of S^•(F') as 𝒥' at all four occurrences on this page "
    "(it is defined there: 'où 𝒥' est l'Idéal d'augmentation'); not a misprint.")
add(p, "proof of (16.4.8.3): same formula, S^•_{O_Y}(F'')",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    r"\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$, où $",
    r"\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$, où $", BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'où J' est l'Idéal d'augmentation'",
    "script J' (𝒥')", "\\mathscr{I}'", "symbol", None, "high",
    L(r"\mathscr{I}'$ est", r"l'Idéal d'augmentation"),
    L(r"\mathscr{J}'$ est", r"l'Idéal d'augmentation"), "As above.")
add(p, "proof of (16.4.8.3): 'l'Idéal d'augmentation de S^•_{O_Y}(F')'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    L(r"de", r"$\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')$, c'est-à-dire"),
    L(r"de", r"$\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}')$, c'est-à-dire"), BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'la somme (directe) des S^m_{O_Y}(F') pour m ⩾ 1'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    r"des $\mathscr{S}_{\mathcal{O}_Y}^m(\mathscr{F}')$ pour $m\geq1$",
    r"des $\mathbf{S}_{\mathcal{O}_Y}^m(\mathscr{F}')$ pour $m\geq1$", BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'On en conclut que I^n = J'^n ⊗ S^•(F'')'",
    "ℐ^n = 𝒥'^n: script I, then script J' (3x crop p20_s4_In_Jn.png)", "\\mathscr{I}^n=\\mathscr{I}'^n",
    "symbol", None, "high",
    r"\mathscr{I}^n=\mathscr{I}'^n", r"\mathscr{I}^n=\mathscr{J}'^n", "As above.")
add(p, "proof of (16.4.8.3): same formula, S^•_{O_Y}(F'')",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    L(r"\otimes_{\mathcal{O}_Y}", r"\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$, où cette fois"),
    L(r"\otimes_{\mathcal{O}_Y}", r"\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$, où cette fois"),
    BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'où cette fois J'^n est la somme (directe)'",
    "script J' (𝒥'^n)", "\\mathscr{I}'^n", "symbol", None, "high",
    r"$\mathscr{I}'^n$ est la somme", r"$\mathscr{J}'^n$ est la somme", "As above.")
add(p, "proof of (16.4.8.3): 'des S^m_{O_Y}(F') pour m ⩾ n'",
    BOLD_S, "\\mathscr{S}", "font", None, "high",
    L(r"des", r"$\mathscr{S}_{\mathcal{O}_Y}^m(\mathscr{F}')$ pour $m\geq n$"),
    L(r"des", r"$\mathbf{S}_{\mathcal{O}_Y}^m(\mathscr{F}')$ pour $m\geq n$"), BOLD_S_NOTE)
add(p, "proof of (16.4.8.3): 'I^n/I^{n+1} = S^n(F')⊗S^•(F'')'",
    BOLD_S + " (two S)", "\\mathscr{S} twice", "font", None, "high",
    L(r"\mathscr{S}_{\mathcal{O}_Y}^n(\mathscr{F}')\otimes_{\mathcal{O}_Y}",
      r"\mathscr{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$, ce qui"),
    L(r"\mathbf{S}_{\mathcal{O}_Y}^n(\mathscr{F}')\otimes_{\mathcal{O}_Y}",
      r"\mathbf{S}_{\mathcal{O}_Y}^{\bullet}(\mathscr{F}'')$, ce qui"),
    BOLD_S_NOTE)

# ---------------------------------------------------------------- page 21
p = 21
add(p, "Corollaire (16.4.9): 'Sous les conditions de (16.4.7),'",
    "reference (16.4.7) upright inside the italic corollary (crop p21_s1_cond.png)",
    "italic (corollary environment)", "convention", 6, "high",
    r"Sous les conditions de (16.4.7), on a", r"Sous les conditions de \textup{(16.4.7)}, on a")
add(p, "(16.4.9.1): 'gr_1(δ) : f^*(E) ⥲ Ω^1_{X/S}.'",
    "italic capital omega for the sheaf Ω^1_{X/S} (3x crop p21_s1_omega.png)", "upright \\Omega",
    "font", None, "high",
    r"\xrightarrow{\sim}\Omega_{X/S}^1.", r"\xrightarrow{\sim}\varOmega_{X/S}^1.", OMEGA_NOTE)
add(p, "Corollaire (16.4.10): 'algèbre quotient A[T_1, ..., T_m, U_1, ..., U_m]/K^{n+1}, où les U_i'",
    "the quotient is set in the running text, at the start of the line, followed by ', où les U_i'",
    "displayed with \\[ ... \\]", "other", None, "high",
    L(r"quotient", r"\[", r"  A[T_1,\ldots,T_m,U_1,\ldots,U_m]/\mathfrak{K}^{n+1},", r"\]", r"où les"),
    L(r"quotient", r"$A[T_1,\ldots,T_m,U_1,\ldots,U_m]/\mathfrak{K}^{n+1}$, où les"),
    "Layout only (display vs inline); the formula matches (Fraktur K checked on a 6x crop).")
add(p, "Corollaire (16.4.10): 'où les U_i (1⩽i⩽m) sont'",
    "both parentheses of (1⩽i⩽m) upright (5x crop p21_s2_paren_full.png; the '(' of '(pour la structure' on the same page is slanted)",
    "text parentheses, italic in the corollary environment", "convention", 6, "high",
    r"($1\leq i\leq m$)", r"\textup{(}$1\leq i\leq m$\textup{)}",
    "Same treatment as IV-2 pp. 183, 212 and IV-3 p. 109.")
add(p, "after (16.4.10): 'la structure de Ω^1_{X/S} dans ce cas'",
    "italic capital omega (3x crop p21_s2_omega.png)", "upright \\Omega", "font", None, "high",
    r"structure de $\Omega_{X/S}^1$ dans", r"structure de $\varOmega_{X/S}^1$ dans", OMEGA_NOTE)
add(p, "after (16.4.10): '(0, 20.5.13)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.5.13)", r"(\textbf{0}, 20.5.13)")
add(p, "'fait alors correspondre à un polynôme F(T_1, ..., T_m), la classe mod. K^{n+1}'",
    "comma after F(T_1, ..., T_m) (end of the line; crop p21_s2_notons.png)", "no comma",
    "punctuation", None, "high",
    r"$F(T_1,\ldots,T_m)$ la classe", r"$F(T_1,\ldots,T_m)$, la classe")
add(p, "Proposition (16.4.11): 'S^{(n)} le n-ème voisinage infinitésimal de S pour l'immersion g'",
    "S^{(n)} without the subscript g (5x crop p21_s2_Sn.png); the displays (16.4.11.1)-(16.4.11.2) have O_{S_g^{(n)}}",
    "$S_g^{(n)}$", "formula", None, "high",
    r"$S_g^{(n)}$ le $n$-ème", r"$S^{(n)}$ le $n$-ème",
    "Not a misprint: Définition (16.1.2) introduces the notation 'Y_f^{(n)} ou simplement Y^{(n)}'.")
add(p, "Proposition (16.4.11): 'pour l'immersion g (16.1.2).'",
    "reference upright inside the italic proposition", "italic (proposition environment)",
    "convention", 6, "high",
    L(r"l'immersion $g$", r"(16.1.2)."), L(r"l'immersion $g$", r"\textup{(16.1.2)}."))
add(p, "Proposition (16.4.11): 'définie par f (16.1.7)),'",
    "reference (16.1.7) upright inside the italic proposition (crop p21_s3_pour.png)",
    "italic (proposition environment)", "convention", 6, "high",
    r"par $f$ (16.1.7))", r"par $f$ \textup{(16.1.7)})")
add(p, "proof of (16.4.11): 'En vertu de (I, 5.3.7)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.3.7)", r"(\textbf{I}, 5.3.7)")

# ---------------------------------------------------------------- page 22
p = 22
add(p, "proof of (16.4.11): 'formule d'associativité (I, 3.3.9.1)'", "bold I", "plain I",
    "convention", 2, "high", r"(I, 3.3.9.1)", r"(\textbf{I}, 3.3.9.1)")
add(p, "proof of (16.4.11): 'joue le rôle d'une « section universelle » pour les S-sections'",
    "guillemets « » around the italic 'section universelle' (crop p22_s2_univ.png)",
    "\\emph{section universelle} without guillemets", "punctuation", None, "high",
    r"d'une \emph{section universelle} pour", r"d'une «\emph{section universelle}» pour",
    "Guillemets written as in '«faisceau des parties principales d'ordre $n$»' on this page.")
add(p, "Corollaire (16.4.12): 'x un point de X rationnel sur k.'",
    "'rationnel' and 'sur' printed roman inside the italic corollary (crop p22_s3_cor12.png)",
    "italic (corollary environment)", "convention", 6, "high",
    L(r"rationnel sur", r"$k$. Alors"), L(r"\textup{rationnel sur}", r"$k$. Alors"),
    "Same roman 'rationnel sur' in (16.4.13).")
add(p, "Corollaire (16.4.12): '(P^n_{X/k})_x ⊗_{O_x} k(x)'", "bold italic k in k(x)", "plain k",
    "convention", 1, "high",
    r"\otimes_{\mathcal{O}_x}k(x)$", r"\otimes_{\mathcal{O}_x}\boldsymbol{k}(x)$")
add(p, "Corollaire (16.4.12): '(en tant que k(x)-algèbre augmentée)'", "bold italic k", "plain k",
    "convention", 1, "high",
    r"(en tant que $k(x)$-algèbre", r"(en tant que $\boldsymbol{k}(x)$-algèbre")
add(p, "Corollaire (16.4.13): 'X_s = X×_S Spec(k(s))'", "bold italic k", "plain k",
    "convention", 1, "high",
    r"\operatorname{Spec}(k(s))", r"\operatorname{Spec}(\boldsymbol{k}(s))")
add(p, "Corollaire (16.4.13): 'Si x∈X_s est rationnel sur k(s),'",
    "'rationnel sur' printed roman inside the italic corollary (crop p22_s3_cor13.png)",
    "italic (corollary environment)", "convention", 6, "high",
    r"est rationnel sur", r"est \textup{rationnel sur}")
add(p, "Corollaire (16.4.13): 'rationnel sur k(s),'", "bold italic k", "plain k",
    "convention", 1, "high",
    L(r"$k(s)$,", r"$(\mathscr{P}_{X/S}^n)_x"), L(r"$\boldsymbol{k}(s)$,", r"$(\mathscr{P}_{X/S}^n)_x"))
add(p, "Corollaire (16.4.13): '(P^n_{X/S})_x ⊗_{O_s} k(s)'", "bold italic k", "plain k",
    "convention", 1, "high",
    r"\otimes_{\mathcal{O}_s}k(s)$", r"\otimes_{\mathcal{O}_s}\boldsymbol{k}(s)$")
add(p, "Corollaire (16.4.13): '(où t est une section de O_X au-dessus d'un voisinage ouvert de x dans X)'",
    "the whole parenthesis printed roman, parentheses upright (crop p22_s3_cor13.png); 'la classe de' italic again",
    "italic (corollary environment)", "convention", 6, "high",
    L(r"(où $t$ est",
      r"une section de $\mathcal{O}_X$ au-dessus d'un voisinage ouvert de $x$ dans",
      r"$X$)"),
    L(r"\textup{(où $t$ est",
      r"une section de $\mathcal{O}_X$ au-dessus d'un voisinage ouvert de $x$ dans",
      r"$X$)}"))

# ---------------------------------------------------------------- page 23
p = 23
add(p, "Proposition (16.4.14), first line of the page: 'P^n_{B/A} → P^n_{S^{-1}B/A} (16.4.4), forment'",
    "reference (16.4.4) upright inside the italic proposition", "italic (proposition environment)",
    "convention", 6, "high",
    r"(16.4.4), forment", r"\textup{(16.4.4)}, forment")
add(p, "proof of (16.4.14): 'Il suffit de remarquer que S^{-1}((B⊗_A B)/J^{n+1}) = S^{-1}(B⊗_A B)/(S^{-1}J)^{n+1} par platitude'",
    "the equation is set in the running text ('remarquer que ... par plati-tude'); Fraktur J (𝔍) both times "
    "(5x crop p23_s1_frakJ1.png: the letter descends below the baseline)",
    "displayed with \\[ ... \\]; \\mathfrak{I} twice", "other", None, "high",
    L(r"remarquer que", r"\[", r"  S^{-1}((B\otimes_A B)/\mathfrak{I}^{n+1})",
      r"  =S^{-1}(B\otimes_A B)/(S^{-1}\mathfrak{I})^{n+1}", r"\]", r"par platitude"),
    L(r"remarquer que", r"$S^{-1}((B\otimes_A B)/\mathfrak{J}^{n+1})",
      r"=S^{-1}(B\otimes_A B)/(S^{-1}\mathfrak{J})^{n+1}$", r"par platitude"),
    "Display vs inline; the edit also writes the Fraktur J (next entry).")
add(p, "proof of (16.4.14): the ideal of the diagonal in J^{n+1} and (S^{-1}J)^{n+1}",
    "Fraktur J 𝔍 (descender), the 𝔍_{B/A} of (0, 20.4.1)", "\\mathfrak{I} twice", "symbol", None, "high",
    None, None,
    "Covered by the edit of the preceding entry. ega0-20 writes this ideal \\mathfrak{J}_{B/A}; "
    "ega4-16 has \\mathfrak{I} about 30 times (e.g. \\mathfrak{I}_{B/A}, (16.3.x)): check them against the print.")
add(p, "proof of (16.4.14): '(I, 1.3.4)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 1.3.4)", r"(\textbf{I}, 1.3.4)")
add(p, "Corollaire (16.4.15): 'Les notations étant celles de (16.4.14),'",
    "reference upright inside the italic corollary", "italic (corollary environment)",
    "convention", 6, "high",
    r"celles de (16.4.14), soit", r"celles de \textup{(16.4.14)}, soit")
add(p, "(16.4.15.2): 'P^n_{S^{-1}B/A} ⥲ P^n_{S^{-1}B/R^{-1}A}'",
    "no punctuation after the display (3x crop p23_s2_disp152.png)", "a comma after the display",
    "punctuation", None, "high",
    L(r"P_{S^{-1}B/R^{-1}A}^n,", r"  \tag{16.4.15.2}"),
    L(r"P_{S^{-1}B/R^{-1}A}^n", r"  \tag{16.4.15.2}"),
    "As (16.4.15.1), which the print also leaves without punctuation before 'formant'.")
add(p, "proof of (16.4.15): 'par passage aux quotients (0_I, 1.5.3)'", "bold 0 with subscript I",
    "plain 0 ('0$_{\\rm I}$')", "convention", 2, "high",
    r"(0$_{\rm I}$, 1.5.3)", r"(\textbf{0}$_{\rm I}$, 1.5.3)")
add(p, "(16.4.16.1): '(P^n_{X/S})_x ⥲ P^n_{O_x/O_s}.' followed by 'formant un système projectif.'",
    "a full stop after the display (3x crop p23_s2_disp161.png), although the sentence goes on with 'formant un système projectif'",
    "no full stop: the TeX silently corrects", "misprint_in_print", None, "high",
    L(r"P_{\mathcal{O}_x/\mathcal{O}_s}^n", r"  \tag{16.4.16.1}"),
    L(r"P_{\mathcal{O}_x/\mathcal{O}_s}^n.", r"  \tag{16.4.16.1}"),
    "Spurious full stop in the print (cf. (16.4.15.1), same sentence pattern, no punctuation). "
    "The diplomatic text restores it; the corrected reading has no stop.",
    corrected=r"P_{\mathcal{O}_x/\mathcal{O}_s}^n")
add(p, "(16.4.16.2): '(Ω^1_{X/S})_x ⥲ Ω^1_{O_x/O_s}.'",
    "first omega (the sheaf) italic, second (the module) upright (3x crop p23_s3_omega.png)",
    "upright \\Omega both times", "font", None, "high",
    r"(\Omega_{X/S}^1)_x", r"(\varOmega_{X/S}^1)_x", OMEGA_NOTE)
add(p, "Corollaire (16.4.17): 'fait correspondre d^nT_i—T_i.1'",
    "long dash for the minus (4x crop p23_s3_dT.png)", "minus sign", "convention", 7, "high",
    r"d^nT_i-T_i", r"d^nT_i\setmin T_i",
    "Long dash used for a subtraction (GLOBAL_ISSUES 23); \\setmin pending the convention-7 decision.")
add(p, "Corollaire (16.4.17): same formula, 'T_i.1'",
    "baseline full stop between T_i and 1 (4x crop p23_s3_dT.png)", "\\cdot (centred dot)",
    "symbol", None, "high",
    r"T_i\cdot1$", r"T_i.1$", "As GLOBAL_ISSUES 65 (p.1 written p\\cdot1).")
add(p, "proof of (16.4.17): 'et S=B—{0}'", "long dash for the set difference (2x crop p23_s3_Bminus.png)",
    "minus sign", "convention", 7, "high",
    r"S=B-\{0\}", r"S=B\setmin\{0\}")
add(p, "after (16.4.17): '(0, 20.5.10)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.5.10)", r"(\textbf{0}, 20.5.10)")
add(p, "Proposition (16.4.18): 'deux morphismes de préschémas, et considérons'",
    "comma (3x crop p23_s3_presch.png)", "semicolon", "punctuation", None, "high",
    r"préschémas; et considérons", r"préschémas, et considérons")
add(p, "Proposition (16.4.18): 'Algèbres augmentées (16.4.3.3)'",
    "reference upright inside the italic proposition", "italic (proposition environment)",
    "convention", 6, "high",
    L(r"augmentées", r"(16.4.3.3)"), L(r"augmentées", r"\textup{(16.4.3.3)}"))

# ---------------------------------------------------------------- page 24
p = 24
add(p, "proof of (16.4.18): 'On a un diagramme commutatif (I, 5.3.5)'", "bold I", "plain I",
    "convention", 2, "high", r"(I, 5.3.5)", r"(\textbf{I}, 5.3.5)")
add(p, "proof of (16.4.18): 'Mais on sait (loc. cit.) que'",
    "both parentheses italic, like 'loc. cit.' (3x crops p24_s2_loccit.png, p24_s2_loccit2.png)",
    "(\\emph{loc. cit.}): upright parentheses", "italics", None, "high",
    r"(\emph{loc. cit.})", r"\emph{(loc. cit.)}", "As the earlier (loc. cit.) fixes (II p. 9, III p. 182, 0_IV p. 42).")
add(p, "proof of (16.4.18): 'L est égal à (f×_Z f)^*(K).O_{X×_Z X}'",
    "baseline full stop between (K) and O (5x crop p24_s2_Kdot.png)", "\\cdot (centred dot)",
    "symbol", None, "high",
    r"(\mathscr{K})\cdot\mathcal{O}_{X\times_Z X}", r"(\mathscr{K}).\mathcal{O}_{X\times_Z X}",
    "As GLOBAL_ISSUES 65.")
add(p, "proof of (16.4.18): '(I, 4.4.5)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 4.4.5)", r"(\textbf{I}, 4.4.5)")
add(p, "Corollaire (16.4.19): 'Avec les notations de (16.4.18),'",
    "reference upright inside the italic corollary", "italic (corollary environment)",
    "convention", 6, "high",
    r"notations de (16.4.18), on a", r"notations de \textup{(16.4.18)}, on a")
add(p, "(16.4.19.1): 'f^*(Ω^1_{Y/Z}) → Ω^1_{X/Z} → Ω^1_{X/Y} → 0.'",
    "italic capital omega three times (2x crop p24_s3_seq.png)", "upright \\Omega three times",
    "font", None, "high",
    L(r"    f^*(\Omega_{Y/Z}^1)\ar[r]^-{f_{X/Y/Z}}&",
      r"    \Omega_{X/Z}^1\ar[r]^-{g_{X/Y/Z}}&",
      r"    \Omega_{X/Y}^1\ar[r]&0."),
    L(r"    f^*(\varOmega_{Y/Z}^1)\ar[r]^-{f_{X/Y/Z}}&",
      r"    \varOmega_{X/Z}^1\ar[r]^-{g_{X/Y/Z}}&",
      r"    \varOmega_{X/Y}^1\ar[r]&0."),
    OMEGA_NOTE)
add(p, "after (16.4.19): 'la suite exacte (0, 20.5.7.1)'", "bold 0", "plain 0", "convention", 2, "high",
    r"(0, 20.5.7.1)", r"(\textbf{0}, 20.5.7.1)")
add(p, "Proposition (16.4.20): 'engendré par j^*(O_Y.d^n_{Y/Z}(K))'",
    "baseline full stop between O_Y and d (5x crop p24_s3_Odot.png)", "\\cdot (centred dot)",
    "symbol", None, "high",
    r"\mathcal{O}_Y\cdot d_{Y/Z}^n", r"\mathcal{O}_Y.d_{Y/Z}^n", "As GLOBAL_ISSUES 65.")
add(p, "proof of (16.4.20): 'On sait (I, 5.3.8)'", "bold I", "plain I", "convention", 2, "high",
    r"(I, 5.3.8)", r"(\textbf{I}, 5.3.8)")
add(p, "proof of (16.4.20): 'son quotient par l'Idéal engendré par j^*(d^n_{Y/Z}(K)) à P^n_{Y/Z}/(ϖ_1(K)+ϖ_2(K))P^n_{Y/Z}.'",
    "the quotient is set in the running text at the end of the line, followed by '.'; 'Notons maintenant' "
    "starts the next line of the same paragraph (no indent)",
    "displayed with \\[ ... \\]", "other", None, "high",
    L(r"à", r"\[", r"  \mathscr{P}_{Y/Z}^n/",
      r"  (\varpi_1(\mathscr{K})+\varpi_2(\mathscr{K}))\mathscr{P}_{Y/Z}^n.", r"\]", r"Notons"),
    L(r"à", r"$\mathscr{P}_{Y/Z}^n/(\varpi_1(\mathscr{K})+\varpi_2(\mathscr{K}))\mathscr{P}_{Y/Z}^n$.", r"Notons"),
    "Layout only (display vs inline); the formula matches.")


# ---------------------------------------------------------------- checks
def page_text(n):
    return (RUN / f"page_{n:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")


ok = True
for n in range(20, 25):
    orig = page_text(n)
    cur = orig
    for i, f in enumerate(F):
        if f["page"] != n or not f["fix"]:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        c0 = orig.count(old)
        c1 = cur.count(old)
        if c0 != 1 or c1 != 1:
            ok = False
            print(f"p{n} entry {i}: old count original={c0} sequential={c1}: {old[:70]!r}")
        cur = cur.replace(old, new, 1)
    # reverse order application as a robustness check
    rev = orig
    for i, f in reversed(list(enumerate(F))):
        if f["page"] != n or not f["fix"]:
            continue
        old, new = f["fix"]["old"], f["fix"]["new"]
        if rev.count(old) != 1:
            ok = False
            print(f"p{n} entry {i}: reverse-order count {rev.count(old)}: {old[:70]!r}")
        rev = rev.replace(old, new, 1)
    if rev != cur:
        ok = False
        print(f"p{n}: order-dependent result")
    if n == 20:
        print("p20 remaining \\mathscr{S}:", cur.count(r"\mathscr{S}"),
              "| \\mathscr{I}' left:", cur.count(r"\mathscr{I}'"))
    (RUN / "crops_020_024" / f"applied_{n:03d}.txt").write_text(cur, encoding="utf-8")

counts = {}
for f in F:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    counts.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print(counts)
if not ok:
    print("NOT WRITTEN")
    sys.exit(1)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT, len(F))
