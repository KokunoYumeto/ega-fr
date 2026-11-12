"""Build findings_015_019.json for EGA II pp. 15-19 and check every fix.

Run: python -I build_findings.py
"""
import json
import os

RUN = r"user\Documents\ega_scan_check_20261101\run_II"
OUT = os.path.join(RUN, "findings_015_019.json")
NL = "\n"


def F(page, where, scan, tex, kind, conv, conf, old, new, note, corrected=None):
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
    return d


C2 = "Bold chapter number in the print, plain in the TeX."
C1 = "Bold italic k in the print, plain k in the TeX."
C3 = "Plain arrow in the print, \\mapsto in the TeX."
C4 = "Isomorphism arrow (arrow with a tilde above) in the print, \\simeq in the TeX."

findings = [
    # ---------------- page 15 ----------------
    F(15, "(1.7.1), end: 'un produit σ(x1)σ(x2) . . . σ(xn), où les xi∈E'",
      "σ(x₁)σ(x₂) . . . σ(xₙ), dots on the baseline",
      r"\sigma(x_1)\sigma(x_2)\cdots\sigma(x_n)",
      "symbol", None, "high",
      r"\sigma(x_2)\cdots\sigma(x_n)", r"\sigma(x_2)\ldots\sigma(x_n)",
      "Checked on a crop: baseline dots. Same treatment as EGA I pp. 113 and 169."),
    F(15, "(1.7.1), end: 'se note souvent x1x2 . . . xn si aucune confusion'",
      "x₁x₂ . . . xₙ, dots on the baseline",
      r"$x_1x_2\cdots x_n$",
      "symbol", None, "high",
      r"$x_1x_2\cdots x_n$", r"$x_1x_2\ldots x_n$",
      "Checked on a crop: baseline dots."),
    F(15, "(1.7.4): 'est la 𝒜-Algèbre symétrique du 𝒜-Module ℰ'",
      "'𝒜-Algèbre symétrique' italic as a whole ('Algèbre' italic; 'Module' later in the line upright)",
      r"$\mathcal{A}$-Algèbre \emph{symétrique} (only 'symétrique' italic)",
      "italics", None, "high",
      r"$\mathcal{A}$-Algèbre" + NL + r"\emph{symétrique}", r"\emph{$\mathcal{A}$-Algèbre" + NL + "symétrique}",
      "Checked on a crop. (1.7.4) is the roman env environment."),
    # ---------------- page 16 ----------------
    F(16, "(1.7.4), first paragraph of p. 16: 'S(ℰ⊕ℱ) s'identifie canoniquement à S(ℰ)⊗ S(ℱ)'",
      "S(ℰ)⊗_A S(ℱ): the subscript of ⊗ is a roman capital A, not the script 𝒜",
      r"\mathbf{S}(\mathcal{E})\otimes_{\mathcal{A}}\mathbf{S}(\mathcal{F})",
      "misprint_in_print", None, "high",
      r"\otimes_{\mathcal{A}}\mathbf{S}(\mathcal{F})", r"\otimes_A\mathbf{S}(\mathcal{F})",
      "Checked on a 3x crop: roman A, unlike the script 𝒜 of S_𝒜(𝒜) further down the page. ℰ and ℱ are "
      "𝒜-Modules and the product is over the sheaf 𝒜 (the proof of (1.7.11) quotes this as "
      "S(ℰ⊕ℱ)⥲S(ℰ)⊗_{𝒪_S}S(ℱ) (1.7.4)). The TeX silently corrects the misprint; the fix restores the "
      "printed reading.",
      corrected=r"\otimes_{\mathcal{A}}\mathbf{S}(\mathcal{F})"),
    F(16, "(1.7.4): 'le faisceau associé au préfaisceau U→S_n(Γ(U, ℰ))'",
      "U→S_n(Γ(U, ℰ)), plain arrow", r"U\mapsto\mathbf{S}_n(\Gamma(U,\mathcal{E}))",
      "convention", 3, "high",
      r"U\mapsto\mathbf{S}_n", r"U\to\mathbf{S}_n", C3),
    F(16, "(1.7.5): 'on a par définition (0, 4.3.1)'",
      "(𝟎, 4.3.1)", r"(\hyperref[0.4.3.1-fr]{0, 4.3.1})",
      "convention", 2, "high",
      "{0, 4.3.1}", r"{\textbf{0}, 4.3.1}", C2),
    F(16, "(1.7.5): 'la définition de ψ*(ℱ) (0, 3.7.1)'",
      "(𝟎, 3.7.1)", r"(\hyperref[0.3.7.1-fr]{0, 3.7.1})",
      "convention", 2, "high",
      "{0, 3.7.1}", r"{\textbf{0}, 3.7.1}", C2),
    F(16, "(1.7.5): 'tels que h coïncide avec t→h'(ψ(t)) au-dessus de V''",
      "t→h'(ψ(t)), plain arrow", r"t\mapsto h'(\psi(t))",
      "convention", 3, "high",
      r"t\mapsto h'(\psi(t))", r"t\to h'(\psi(t))", C3),
    F(16, "proof of (1.7.6): 'résulte donc des définitions (I, 1.3.4)'",
      "(𝐈, 1.3.4)", r"(\hyperref[I.1.3.4-fr]{I, 1.3.4})",
      "convention", 2, "high",
      "{I, 1.3.4}", r"{\textbf{I}, 1.3.4}", C2),
    F(16, "proof of (1.7.7): 'conséquence immédiate de (1.7.6) et de (I, 1.4.1)'",
      "(𝐈, 1.4.1)", r"(\hyperref[I.1.4.1-fr]{I, 1.4.1})",
      "convention", 2, "high",
      "{I, 1.4.1}", r"{\textbf{I}, 1.4.1}", C2),
    F(16, "proof of (1.7.7): 'on applique alors (I, 1.3.13)'",
      "(𝐈, 1.3.13)", r"(\hyperref[I.1.3.13-fr]{I, 1.3.13})",
      "convention", 2, "high",
      "{I, 1.3.13}", r"{\textbf{I}, 1.3.13}", C2),
    F(16, "Définition (1.7.8): 'On appelle fibré vectoriel sur S défini par ℰ et on note V(ℰ)'",
      "the whole statement italic; 'fibré vectoriel sur S défini par ℰ' shows no change of face",
      r"\emph{fibré vectoriel sur $S$ défini par $\mathcal{E}$} inside the \itshape definition environment (comes out upright)",
      "convention", 6, "high",
      r"\emph{fibré vectoriel sur $S$ défini par $\mathcal{E}$}",
      r"fibré vectoriel sur $S$ défini par $\mathcal{E}$",
      "Checked on a crop. Printed italic words left upright by \\emph in an italic environment; drop the \\emph."),
    F(16, "Définition (1.7.8): 'le spectre (1.3.1) de la 𝒪_S-Algèbre'",
      "reference (1.3.1) upright inside the italic statement",
      r"(\hyperref[II.1.3.1-fr]{1.3.1}) italic in the environment",
      "convention", 6, "high",
      r"(\hyperref[II.1.3.1-fr]{1.3.1})", r"\textup{(\hyperref[II.1.3.1-fr]{1.3.1})}",
      "Checked on a crop. Same form of fix as EGA I p. 135."),
    F(16, "paragraph after (1.7.8): 'et les homomorphismes de 𝒪_S-Algèbres S(ℰ)→𝒜(X)'",
      "'Algèbres' italic", r"$\mathcal{O}_S$-Algèbres (roman)",
      "italics", None, "high",
      r"$\mathcal{O}_S$-Algèbres", r"$\mathcal{O}_S$-\emph{Algèbres}",
      "Checked on a crop. Deliberate contrast with 'Modules' in the same sentence (homomorphisms of "
      "Algebras S(ℰ)→𝒜(X) against homomorphisms of Modules ℰ→𝒜(X)); (1.7.14) prints the same pair "
      "in italics and the TeX has them there."),
    F(16, "paragraph after (1.7.8): 'les homomorphismes de 𝒪_S-Modules ℰ→𝒜(X)=f_*(𝒪_X)'",
      "'Modules' italic", r"$\mathcal{O}_S$-Modules (roman)",
      "italics", None, "high",
      r"$\mathcal{O}_S$-Modules" + NL + r"$\mathcal{E}\to\mathcal{A}(X)",
      r"$\mathcal{O}_S$-\emph{Modules}" + NL + r"$\mathcal{E}\to\mathcal{A}(X)",
      "Checked on a crop; see the previous finding."),
    F(16, "(1.7.9): 'un sous-préschéma induit par S sur un ouvert U⊂S'",
      "'ouvert' italic", "sur un ouvert $U\\subset S$ (roman)",
      "italics", None, "high",
      r"sur un ouvert $U\subset S$", r"sur un \emph{ouvert} $U\subset S$",
      "Checked on a crop."),
    F(16, "(1.7.9): 'les U-sections (I, 2.5.5)'",
      "(𝐈, 2.5.5)", r"(\hyperref[I.2.5.5-fr]{I, 2.5.5})",
      "convention", 2, "high",
      "{I, 2.5.5}", r"{\textbf{I}, 2.5.5}", C2),
    # ---------------- page 17 ----------------
    F(17, "(1.7.9), first line of p. 17: 'ce qui revient au même (0, 4.4.3) aux (𝒪_S|U)-homomorphismes'",
      "(𝟎, 4.4.3)", r"(\hyperref[0.4.4.3-fr]{0, 4.4.3})",
      "convention", 2, "high",
      "{0, 4.4.3}) aux", r"{\textbf{0}, 4.4.3}) aux", C2),
    F(17, "(1.7.10): 'correspond donc à un monomorphisme k(s)→K'",
      "𝒌(s)→K", r"$k(s)\to K$",
      "convention", 1, "high",
      r"$k(s)\to K$", r"$\boldsymbol{k}(s)\to K$", C1),
    F(17, "(1.7.10): 'où s=f(ξ) (I, 2.4.6)'",
      "(𝐈, 2.4.6)", r"(\hyperref[I.2.4.6-fr]{I, 2.4.6})",
      "convention", 2, "high",
      "{I, 2.4.6}", r"{\textbf{I}, 2.4.6}", C2),
    F(17, "(1.7.10): 'à valeurs dans l'extension K de k(s)'",
      "𝒌(s)", r"$k(s)$",
      "convention", 1, "high",
      r"l'extension $K$ de $k(s)$", r"l'extension $K$ de $\boldsymbol{k}(s)$", C1),
    F(17, "(1.7.10): 'de k(s) (I, 3.4.5), points qui sont localisés'",
      "(𝐈, 3.4.5)", r"(\hyperref[I.3.4.5-fr]{I, 3.4.5})",
      "convention", 2, "high",
      "{I, 3.4.5}", r"{\textbf{I}, 3.4.5}", C2),
    F(17, "(1.7.10): 'ou, ce qui revient au même (0, 4.4.3) à l'ensemble des homomorphismes'",
      "(𝟎, 4.4.3)", r"(\hyperref[0.4.4.3-fr]{0, 4.4.3})",
      "convention", 2, "high",
      "{0, 4.4.3}) à l'ensemble", r"{\textbf{0}, 4.4.3}) à l'ensemble", C2),
    F(17, "(1.7.10): 'Mais on a par définition (0, 4.3.1)'",
      "(𝟎, 4.3.1)", r"(\hyperref[0.4.3.1-fr]{0, 4.3.1})",
      "convention", 2, "high",
      "{0, 4.3.1}", r"{\textbf{0}, 4.3.1}", C2),
    F(17, "(1.7.10): 'f*(ℰ)=ℰ_s⊗K=ℰ^s⊗_{k(s)}K, en posant'",
      "⊗ with subscript 𝒌(s)", r"\otimes_{k(s)}K",
      "convention", 1, "high",
      r"\otimes_{k(s)}K$, en posant", r"\otimes_{\boldsymbol{k}(s)}K$, en posant", C1),
    F(17, "(1.7.10): 'au dual du K-espace vectoriel ℰ^s⊗_{k(s)}K;'",
      "⊗ with subscript 𝒌(s)", r"\otimes_{k(s)}K",
      "convention", 1, "high",
      r"\otimes_{k(s)}K$}~;", r"\otimes_{\boldsymbol{k}(s)}K$}~;", C1),
    F(17, "(1.7.10): 'si ℰ^s ou K est de dimension finie sur k(s)'",
      "𝒌(s)", r"$k(s)$",
      "convention", 1, "high",
      r"finie sur $k(s)$", r"finie sur $\boldsymbol{k}(s)$", C1),
    F(17, "(1.7.10): 'ce dual s'identifie aussi à (ℰ^s)ˇ⊗_{k(s)}K'",
      "(ℰ^s) followed by a check accent ˇ (the same háček glyph as over ℰ̌ on the first lines of the page)",
      r"(\mathcal{E}^s)^\vee (a ∨ superscript)",
      "symbol", None, "medium",
      "aussi à" + NL + r"$(\mathcal{E}^s)^\vee", "aussi à" + NL + r"$(\mathcal{E}^s)\check{}",
      "Checked on a 2x crop. Same pattern as convention 5 with a check instead of a tilde; same form of fix "
      "as the EGA 0 p. 50 finding. A document-wide rendering (like \\supertilde) may be preferred."),
    F(17, "(1.7.10): '(ℰ^s)ˇ⊗_{k(s)}K, en désignant par'",
      "⊗ with subscript 𝒌(s)", r"\otimes_{k(s)}K",
      "convention", 1, "high",
      r"\otimes_{k(s)}K$, en désignant", r"\otimes_{\boldsymbol{k}(s)}K$, en désignant", C1),
    F(17, "(1.7.10): 'en désignant par (ℰ^s)ˇ le dual'",
      "(ℰ^s) followed by a check accent ˇ", r"(\mathcal{E}^s)^\vee",
      "symbol", None, "medium",
      r"$(\mathcal{E}^s)^\vee$ le dual", r"$(\mathcal{E}^s)\check{}$ le dual",
      "Checked on a 2x crop; see the previous check-accent finding."),
    F(17, "(1.7.10): 'le dual du k(s)-espace vectoriel ℰ^s'",
      "𝒌(s)", r"$k(s)$",
      "convention", 1, "high",
      r"du $k(s)$-espace", r"du $\boldsymbol{k}(s)$-espace", C1),
    F(17, "Proposition (1.7.11), (v): 'A un homomorphisme surjectif ℰ→ℱ'",
      "'A un' (capital A without the grave accent)", "À un",
      "word", None, "high",
      "À un homomorphisme surjectif", "A un homomorphisme surjectif",
      "Checked on a 2x crop: no accent on the capital (the print's usage; É keeps its accent, e.g. 'Étant' "
      "on p. 19). The section file has only one other 'À' (line 2224, a different page)."),
    F(17, "proof of (1.7.11): 'des définitions (I, 6.3.1)'",
      "(𝐈, 6.3.1)", r"(\hyperref[I.6.3.1-fr]{I, 6.3.1})",
      "convention", 2, "high",
      "{I, 6.3.1}", r"{\textbf{I}, 6.3.1}", C2),
    F(17, "proof of (1.7.11): 'l'isomorphisme canonique S(ℰ⊕ℱ)⥲S(ℰ)⊗_{𝒪_S}S(ℱ)'",
      "arrow with a tilde above", r"\simeq",
      "convention", 4, "high",
      r"\simeq\mathbf{S}(\mathcal{E})", r"\xrightarrow{\sim}\mathbf{S}(\mathcal{E})", C4),
    F(17, "proof of (1.7.11): 'l'isomorphisme canonique S(g*(ℰ))⥲g*(S(ℰ))'",
      "arrow with a tilde above", r"\simeq",
      "convention", 4, "high",
      r"\simeq g^*(\mathbf{S}(\mathcal{E}))", r"\xrightarrow{\sim} g^*(\mathbf{S}(\mathcal{E}))", C4),
    # ---------------- page 18 ----------------
    F(18, "(1.7.12): 'déjà vue dans (I, 3.3.15)'",
      "(𝐈, 3.3.15)", r"(\hyperref[I.3.3.15-fr]{I, 3.3.15})",
      "convention", 2, "high",
      "{I, 3.3.15}", r"{\textbf{I}, 3.3.15}", C2),
    F(18, "(1.7.13): 'comme un foncteur contravariant en X, de la catégorie des S-préschémas'",
      "'foncteur contravariant' italic, 'en' upright", r"\emph{foncteur contravariant en $X$}",
      "italics", None, "high",
      r"\emph{foncteur contravariant en $X$}", r"\emph{foncteur contravariant} en $X$",
      "Checked on a crop."),
    F(18, "(1.7.13), end: '(cf. chap. 0, § 8)'",
      "chap. 𝟎, § 8 (bold 0)", r"chap.~0, \textsection8",
      "convention", 2, "high",
      r"chap.~0, \textsection8", r"chap.~\textbf{0}, \textsection8",
      "Checked on a crop. A written-out chapter reference with the bold chapter number."),
    F(18, "(1.7.14), first display: '(h+h')(s1s2 . . . sn) = Π (h(si)+h'(si))'",
      "s₁s₂ . . . sₙ, dots on the baseline", r"(h+h')(s_1s_2\cdots s_n)",
      "symbol", None, "high",
      r"(h+h')(s_1s_2\cdots s_n)", r"(h+h')(s_1s_2\ldots s_n)",
      "Checked on a crop."),
    F(18, "(1.7.14), second display: '(t.h)(s1s2 . . . sn) = t^n Π h(si)'",
      "s₁s₂ . . . sₙ, dots on the baseline", r"(t.h)(s_1s_2\cdots s_n)",
      "symbol", None, "high",
      r"(t.h)(s_1s_2\cdots s_n)", r"(t.h)(s_1s_2\ldots s_n)",
      "Checked on a crop."),
    F(18, "(1.7.14): 'si z est une section de S(ℰ) au-dessus de U, h→h(z) est une application'",
      "h→h(z), plain arrow", r"h\mapsto h(z)",
      "convention", 3, "high",
      r"$h\mapsto h(z)$ est une", r"$h\to h(z)$ est une", C3),
    # ---------------- page 19 ----------------
    F(19, "(1.7.14), italic statement: 'l'application h→h(z) de Hom_{𝒪_S|U}(…)'",
      "h→h(z), plain arrow", r"h\mapsto h(z)",
      "convention", 3, "high",
      r"$h\mapsto h(z)$ de", r"$h\to h(z)$ de", C3),
    F(19, "(1.7.14): 'les homomorphismes d'anneaux h : B→B[T] (I, 1.3.13)'",
      "(𝐈, 1.3.13)", r"(\hyperref[I.1.3.13-fr]{I, 1.3.13})",
      "convention", 2, "high",
      "{I, 1.3.13}", r"{\textbf{I}, 1.3.13}", C2),
    F(19, "proof of (1.7.15): 'quasi-cohérent de type fini ℰ (I, 9.6.5)'",
      "(𝐈, 9.6.5)", r"(\hyperref[I.9.6.5-fr]{I, 9.6.5})",
      "convention", 2, "high",
      "{I, 9.6.5}", r"{\textbf{I}, 9.6.5}", C2),
    F(19, "Notations (2.1.1): 'Si M est un module gradué sur S'",
      "'module' upright, only 'gradué' italic", r"\emph{module gradué}",
      "italics", None, "high",
      r"\emph{module" + NL + "gradué}", "module" + NL + r"\emph{gradué}",
      "Checked on a crop. The notation environment's body is roman."),
]

# ---- check every fix: 'old' exactly once in its page file; apply all fixes of a page in order ----
ok = True
by_page = {}
for f in findings:
    by_page.setdefault(f["page"], []).append(f)
for page, fs in sorted(by_page.items()):
    path = os.path.join(RUN, "page_%03d.tex" % page)
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    # the page files carry CRLF; the release files use LF, so compare with LF line breaks
    text = text.replace("\r\n", "\n")
    if "\r" in text:
        print("WARNING: stray CR in", path)
    work = text
    for f in fs:
        fx = f["fix"]
        if fx is None:
            continue
        n = text.count(fx["old"])
        if n != 1:
            ok = False
            print("p.%d: old occurs %d times: %r" % (page, n, fx["old"]))
        m = work.count(fx["old"])
        if m != 1:
            ok = False
            print("p.%d: after earlier fixes, old occurs %d times: %r" % (page, m, fx["old"]))
        work = work.replace(fx["old"], fx["new"], 1)
    # applying in reverse order must give the same result (fixes independent of order)
    work2 = text
    for f in reversed(fs):
        fx = f["fix"]
        if fx and work2.count(fx["old"]) == 1:
            work2 = work2.replace(fx["old"], fx["new"], 1)
    if work2 != work:
        ok = False
        print("p.%d: fixes depend on order" % page)

counts = {}
for f in findings:
    c = counts.setdefault(f["page"], [0, 0, 0])
    if f["kind"] == "convention":
        c[1] += 1
    elif f["kind"] == "misprint_in_print":
        c[2] += 1
    else:
        c[0] += 1
print("counts (normal/convention/misprint):", {p: tuple(v) for p, v in sorted(counts.items())})
print("total", len(findings), "all fixes ok" if ok else "FIX PROBLEMS")

if ok:
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(findings, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print("wrote", OUT)
