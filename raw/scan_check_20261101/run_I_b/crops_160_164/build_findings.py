"""Build and validate findings_160_164.json (EGA I, pp. 160-164).

Each fix "old" must occur exactly once in page_NNN.tex (CRLF) and, after CRLF -> LF, exactly once in the
release region that apply_fixes.py / apply_manual.py would search.
"""
import json
import pathlib
import re

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_I_b")
REL = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20"
                   r"\diplomatic\packages\BASE\native\ega1")
OUT = RUN / "findings_160_164.json"
CRLF = "\r\n"

CONT164 = ("In the page-164 continuation (ega1-8-fr.tex, before its first page marker \\oldpage[I]{165}: "
           "apply_manual.py region 'before_first_marker'); apply_fixes.py searches only ega1-7-fr.tex for p. 164, "
           "so this edit lands in the manual list.")
REF6 = "Reference printed upright inside the italic statement; italic in the TeX environment. Checked on a crop."
LAB = ("Labels a), b), c) are italic in the roman proof text of the print; the TeX sets them roman. "
       "Checked on a crop.")


def F(page, where, scan, tex, kind, convention, confidence, old, new, note=None, corrected=None, region="page"):
    d = dict(page=page, where=where, scan=scan, tex=tex, kind=kind, convention=convention, confidence=confidence,
             fix=None if old is None else dict(old=old, new=new))
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    d["_region"] = region
    return d


findings = [
    # ---------------- page 160 ----------------
    F(160, "Corollaire (7.2.7): 'ayant g(U)‾ pour espace sous-jacent (5.2.1). Pour que g soit restriction'",
      "(5.2.1) upright inside the italic statement",
      r"(\hyperref[I.5.2.1-fr]{5.2.1}) inside the italic corollary environment (comes out italic)",
      "convention", 6, "high",
      r"(\hyperref[I.5.2.1-fr]{5.2.1}). Pour que",
      r"\textup{(\hyperref[I.5.2.1-fr]{5.2.1})}. Pour que", REF6),
    F(160, "Corollaire (7.2.7): '(autrement dit (7.2.5) pour que l'application rationnelle de Y dans X "
           "prolongeant g soit partout définie)'",
      "the whole parenthesis roman inside the italic statement ('Pour que g soit restriction d'une Y-section de' "
      "before it and 'il faut et il suffit ...' after it italic)",
      "the parenthesis inside the italic corollary environment (comes out italic)",
      "convention", 6, "high",
      CRLF.join([r"(autrement dit (\hyperref[I.7.2.5-fr]{7.2.5}) pour que",
                 r"l'application rationnelle de $Y$ dans $X$ prolongeant $g$ soit partout",
                 r"définie)"]),
      CRLF.join([r"\textup{(autrement dit (\hyperref[I.7.2.5-fr]{7.2.5}) pour que",
                 r"l'application rationnelle de $Y$ dans $X$ prolongeant $g$ soit partout",
                 r"définie)}"]),
      "Checked on a crop. The 'old' spans the two line breaks inside the parenthesis."),
    F(160, "(7.2.8), case 1°: 'X est irréductible (donc intègre), car alors'",
      "'irréductible' and 'intègre' in italics",
      "irréductible (donc intègre) roman (the env environment is roman)",
      "italics", None, "high",
      r"$X$ est irréductible (donc intègre)",
      r"$X$ est \emph{irréductible} (donc \emph{intègre})",
      "Checked on a crop."),
    F(160, "(7.2.8), case 2°: 'X est localement noethérien ; notre assertion résulte'",
      "'localement noethérien' in italics",
      "localement noethérien roman (the env environment is roman)",
      "italics", None, "high",
      r"$X$ est localement noethérien~; notre",
      r"$X$ est \emph{localement noethérien}~; notre",
      "Checked on a crop."),
    F(160, "Lemme (7.2.8.1), end of the statement: '(ce qui a lieu en particulier si U est dense dans X)'",
      "the parenthesis roman inside the italic statement, with 'dense' in italics",
      "the parenthesis inside the italic lemma environment (comes out italic, 'dense' not set off)",
      "convention", 6, "high",
      CRLF.join([r"(ce qui a lieu en particulier", r"si $U$ est dense dans $X$)"]),
      CRLF.join([r"\textup{(ce qui a lieu en particulier", r"si $U$ est \emph{dense} dans $X$)}"]),
      "Checked on a crop. \\emph inside \\textup gives the italic 'dense' of the print. "
      "The 'old' spans the line break after 'particulier'."),
    F(160, "proof of (7.2.8.1): 'des composantes irréductibles de X contenant x (0, 2.1.6)'",
      "bold 0", r"(\hyperref[0.2.1.6-fr]{0, 2.1.6})",
      "convention", 2, "high", r"{0, 2.1.6}", r"{\textbf{0}, 2.1.6}"),
    # ---------------- page 161 ----------------
    F(161, "first line of p. 161 (proof of (7.2.8.1)): 'de A contenus dans 𝔧_x (0, 1.2.6)'",
      "bold 0", r"(\hyperref[0.1.2.6-fr]{0, 1.2.6})",
      "convention", 2, "high", r"{0, 1.2.6}", r"{\textbf{0}, 1.2.6}"),
    F(161, "Proposition (7.2.9): 'induite par f (7.2.8), soit un morphisme'",
      "(7.2.8) upright inside the italic statement",
      r"(\hyperref[I.7.2.8-fr]{7.2.8}) inside the italic proposition environment (comes out italic)",
      "convention", 6, "high",
      r"(\hyperref[I.7.2.8-fr]{7.2.8}), soit",
      r"\textup{(\hyperref[I.7.2.8-fr]{7.2.8})}, soit", REF6),
    F(161, "proof of (7.2.9): 'défini dans un ouvert dense de U∪(X—Ū)'",
      "U∪(X—Ū) (long dash)", r"$U\cup(X-\overline U)$",
      "convention", 7, "high",
      r"dense de $U\cup(X-\overline U)$", r"dense de $U\cup(X\setmin\overline U)$",
      "Long dash for the set difference (checked on a crop). \\setmin is still defined as '-' in preamble-base.tex; "
      "same edit as run_I_a p. 118."),
    F(161, "proof of (7.2.9): 'dans l'intersection de X—Ū et du domaine de définition de f'",
      "X—Ū (long dash)", r"$X-\overline U$",
      "convention", 7, "high",
      r"l'intersection de $X-\overline U$", r"l'intersection de $X\setmin\overline U$",
      "Long dash for the set difference. \\setmin is still defined as '-' in preamble-base.tex."),
    F(161, "proof of (7.2.9): 'Comme U∪(X—Ū) est dense dans X'",
      "U∪(X—Ū) (long dash)", r"$U\cup(X-\overline U)$",
      "convention", 7, "high",
      r"$U\cup(X-\overline U)$ est dense", r"$U\cup(X\setmin\overline U)$ est dense",
      "Long dash for the set difference. \\setmin is still defined as '-' in preamble-base.tex."),
    # ---------------- page 162 ----------------
    F(162, "Définition (7.3.2): 'On appelle faisceau des fonctions rationnelles sur un préschéma X'",
      "'faisceau des fonctions rationnelles' in italics like the rest of the definition (no change of face)",
      r"\emph{faisceau des fonctions rationnelles} inside the italic definition environment (comes out upright)",
      "convention", 6, "high",
      r"\emph{faisceau des fonctions rationnelles}", r"faisceau des fonctions rationnelles",
      "\\emph inside the italic definition environment sets the words upright; drop the \\emph. Checked on a crop."),
    F(162, "Corollaire (7.3.4): 'les composantes irréductibles de X (5.2.1). Si h_i est l'injection canonique'",
      "(5.2.1) upright inside the italic statement",
      r"(\hyperref[I.5.2.1-fr]{5.2.1}) inside the italic corollary environment (comes out italic)",
      "convention", 6, "high",
      r"(\hyperref[I.5.2.1-fr]{5.2.1})", r"\textup{(\hyperref[I.5.2.1-fr]{5.2.1})}", REF6),
    F(162, "proof of (7.3.5): 'soit un faisceau simple (0, 3.6.2)'",
      "bold 0", r"(\hyperref[0.3.6.2-fr]{0, 3.6.2})",
      "convention", 2, "high", r"{0, 3.6.2}", r"{\textbf{0}, 3.6.2}"),
    F(162, "proof of (7.3.5): '(R(X))^(I)→(R(X))^(J) (0, 5.1.3)'",
      "bold 0", r"(\hyperref[0.5.1.3-fr]{0, 5.1.3})",
      "convention", 2, "high", r"{0, 5.1.3}", r"{\textbf{0}, 5.1.3}"),
    # ---------------- page 163 ----------------
    F(163, "(7.3.8): 'est une surjection sur l'ensemble des points génériques'",
      "'surjection' in italics", "surjection roman (the env environment is roman)",
      "italics", None, "high",
      r"surjection sur l'ensemble", r"\emph{surjection} sur l'ensemble",
      "Checked on a crop."),
    F(163, "proof of (7.3.8): '(f^*(ℛ(Y)))_x=𝒪_y⊗_{𝒪_y}𝒪_x=𝒪_x (0, 4.3.1)'",
      "bold 0", r"(\hyperref[0.4.3.1-fr]{0, 4.3.1})",
      "convention", 2, "high", r"{0, 4.3.1}", r"{\textbf{0}, 4.3.1}"),
    F(163, "(7.4.1): 'l'homomorphisme z→z⊗1 de ℱ_x dans ℱ_x⊗_{𝒪_X}R(X)'",
      "ℱ_x⊗_{𝒪_X}R(X): the subscript of 𝒪 is a capital X",
      r"$\mathscr{F}_x\otimes_{\mathscr{O}_x}R(X)$ (silently corrected)",
      "misprint_in_print", None, "high",
      r"\mathscr{F}_x\otimes_{\mathscr{O}_x}R(X)", r"\mathscr{F}_x\otimes_{\mathscr{O}_X}R(X)",
      "Checked on a crop at 3x: upright capital X, the same letter as in the 𝒪_X of the preceding line, unlike the "
      "italic x of ℱ_x. The fibre ℱ_x is an 𝒪_x-module and the fibre of ℱ⊗_{𝒪_X}ℛ(X) at x is ℱ_x⊗_{𝒪_x}R(X), "
      "so the capital X is a slip. The TeX silently corrects the print.",
      corrected=r"\mathscr{F}_x\otimes_{\mathscr{O}_x}R(X)"),
    F(163, "(7.4.1): 'appelé faisceau de torsion de ℱ ; il est quasi-cohérent'",
      "only 'faisceau de torsion' in italics; 'de ℱ' roman",
      r"\emph{faisceau de torsion de $\mathscr{F}$}",
      "italics", None, "high",
      r"\emph{faisceau de torsion de $\mathscr{F}$}", r"\emph{faisceau de torsion} de $\mathscr{F}$",
      "Checked on a crop at 2x: the second 'de' is upright."),
    F(163, "paragraph after Proposition (7.4.2): 'Le cardinal de I est appelé le rang de ℱ'",
      "only 'rang' in italics; 'de ℱ' roman",
      r"\emph{rang de $\mathscr{F}$}",
      "italics", None, "high",
      r"\emph{rang de $\mathscr{F}$}", r"\emph{rang} de $\mathscr{F}$",
      "Checked on a crop at 2x: 'de' is upright."),
    F(163, "Corollaire (7.4.4): 'f (resp. f') une section de ℒ'",
      "'(resp. f')' upright inside the italic statement",
      r"(resp. $f'$) inside the italic corollary environment (comes out italic)",
      "convention", 6, "high",
      r"(resp. $f'$)", r"\textup{(resp. $f'$)}",
      "'resp.' and its parentheses roman in the print inside the italic statement; italic in the TeX environment. "
      "Checked on a crop."),
    F(163, "Corollaire (7.4.4): 'une section de ℒ (resp. ℒ') au-dessus de X'",
      "'(resp. ℒ')' upright inside the italic statement",
      r"(resp. $\mathscr{L}'$) inside the italic corollary environment (comes out italic)",
      "convention", 6, "high",
      r"(resp. $\mathscr{L}'$)", r"\textup{(resp. $\mathscr{L}'$)}",
      "'resp.' and its parentheses roman in the print inside the italic statement; italic in the TeX environment. "
      "Checked on a crop."),
    # ---------------- page 164 ----------------
    F(164, "proof of (7.4.5): 'Comme f_* est exact à gauche (0, 4.2.1)'",
      "bold 0", r"(\hyperref[0.4.2.1-fr]{0, 4.2.1})",
      "convention", 2, "high", r"{0, 4.2.1}", r"{\textbf{0}, 4.2.1}"),
    F(164, "proof of (7.4.5): 'contient le point générique de X (0, 2.1.5)'",
      "bold 0", r"(\hyperref[0.2.1.5-fr]{0, 2.1.5})",
      "convention", 2, "high", r"{0, 2.1.5}", r"{\textbf{0}, 2.1.5}"),
    F(164, "Proposition (7.4.6): 'sont équivalentes : a) ℱ est un faisceau de torsion'",
      "label a) roman inside the italic statement",
      "a) inside the italic proposition environment (comes out italic)",
      "convention", 6, "high",
      r"équivalentes~: a)", r"équivalentes~: \textup{a)}",
      "Labels a), b), c) of this proposition are roman in the print (checked on a crop); italic in the TeX "
      "environment. (In the proof that follows they are italic, in (7.4.7) roman.)"),
    F(164, "Proposition (7.4.6): 'faisceau de torsion ; b) ℱ_x=0'",
      "label b) roman inside the italic statement",
      "b) inside the italic proposition environment (comes out italic)",
      "convention", 6, "high",
      r"torsion~; b)", r"torsion~; \textup{b)}", None),
    F(164, "Proposition (7.4.6): 'ℱ_x=0 ; c) Supp(ℱ)≠X'",
      "label c) roman inside the italic statement",
      "c) inside the italic proposition environment (comes out italic)",
      "convention", 6, "high",
      r"$\mathscr{F}_x=0$~; c)", r"$\mathscr{F}_x=0$~; \textup{c)}", None),
    F(164, "proof of (7.4.6): 'donc a) et b) sont équivalentes'",
      "a) and b) in italics", "a) et b) roman",
      "italics", None, "high",
      r"a) et b) sont équivalentes", r"\emph{a)} et \emph{b)} sont équivalentes", LAB),
    F(164, "proof of (7.4.6): 'Supp(ℱ) est fermé dans X (0, 5.2.2)'",
      "bold 0", r"(\hyperref[0.5.2.2-fr]{0, 5.2.2})",
      "convention", 2, "high", r"{0, 5.2.2}", r"{\textbf{0}, 5.2.2}"),
    F(164, "proof of (7.4.6): 'contient x, b) et c) sont équivalentes'",
      "b) and c) in italics", "b) et c) roman",
      "italics", None, "high",
      r"b) et c) sont équivalentes", r"\emph{b)} et \emph{c)} sont équivalentes", LAB),
    F(164, "Lemme (8.1.1), label (i)",
      "label (i) upright", r"\item[(i)]",
      "convention", 6, "high", r"\item[(i)]", r"\item[\textup{(i)}]",
      "The print runs (i)-(iii) into the italic statement with upright labels (checked on a crop); \\item[(i)] "
      "takes the italic of the lemma environment (GLOBAL_ISSUES item 16). " + CONT164, region="cont"),
    F(164, "Lemme (8.1.1), label (ii)",
      "label (ii) upright", r"\item[(ii)]",
      "convention", 6, "high", r"\item[(ii)]", r"\item[\textup{(ii)}]", CONT164, region="cont"),
    F(164, "Lemme (8.1.1), label (iii)",
      "label (iii) upright", r"\item[(iii)]",
      "convention", 6, "high", r"\item[(iii)]", r"\item[\textup{(iii)}]", CONT164, region="cont"),
    F(164, "proof of (8.1.1): 'enfin, si (iii) est vérifieé, 𝔪(B)∩A contient 𝔪(A)'",
      "vérifieé (accent on the last e, none on the one before)",
      "est vérifiée, (silently corrected)",
      "misprint_in_print", None, "high",
      r"est vérifiée,", r"est vérifieé,",
      "Checked on a crop at 3x. The TeX silently corrects the print. " + CONT164,
      corrected=r"est vérifiée,", region="cont"),
    F(164, "(8.1.2): 'l'application 𝔭→A_𝔭 de Spec(A) dans L(A) est bijective'",
      "plain arrow →", r"$\mathfrak p\mapsto A_\mathfrak p$",
      "convention", 3, "high",
      r"\mathfrak p\mapsto A_\mathfrak p", r"\mathfrak p\to A_\mathfrak p",
      "Checked on a crop. " + CONT164, region="cont"),
    F(164, "proof of (8.1.3): 'et comme A—𝔭⊂M, on a A_𝔭⊂M'",
      "A—𝔭 (long dash)", r"$A-\mathfrak p\subset M$",
      "convention", 7, "high",
      r"$A-\mathfrak p\subset M$", r"$A\setmin\mathfrak p\subset M$",
      "Long dash for the set difference. \\setmin is still defined as '-' in preamble-base.tex. " + CONT164,
      region="cont"),
]

# ---------------- validation ----------------
marker = re.compile(r"\\oldpage\[I\]\{(\d+)\}")
rel7 = (REL / "ega1-7-fr.tex").read_text(encoding="utf-8")
rel8 = (REL / "ega1-8-fr.tex").read_text(encoding="utf-8")


def page_region(t, n):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (k, s) in enumerate(cuts):
        if k == n:
            return t[s:(cuts[i + 1][1] if i + 1 < len(cuts) else len(t))]
    return None


ok = True
for x in findings:
    region = x.pop("_region")
    if not x["fix"]:
        continue
    old = x["fix"]["old"]
    # page files are CRLF on disk; read the bytes so that the CRLF of multi-line olds is matched exactly
    raw = (RUN / f"page_{x['page']:03d}.tex").read_bytes().decode("utf-8")
    c_raw = raw.count(old)
    lf_old = old.replace("\r\n", "\n")
    if region == "cont":
        seg = rel8[:marker.search(rel8).start()]
    else:
        seg = page_region(rel7, x["page"])
    c_rel = seg.count(lf_old) if seg is not None else -1
    flag = "OK " if (c_raw == 1 and c_rel == 1) else "BAD"
    if flag == "BAD":
        ok = False
    print(flag, x["page"], f"raw={c_raw} rel={c_rel}", repr(old[:60]))

json.dump(findings, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", OUT, len(findings), "findings; all unique" if ok else "; SOME NOT UNIQUE")
