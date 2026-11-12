"""Build findings_218_223.json and check that every fix's 'old' occurs exactly once in its page file.

Strings are raw; the character U+23CE (return symbol) stands for a newline.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
RUN = Path(r"user/Documents/ega_scan_check_20261101/run_III2")
OUT = RUN / "findings_218_223.json"
NL = "\u23ce"


def L(s):
    return None if s is None else s.replace(NL, "\n")


F = []


def add(page, where, scan, tex, kind, old, new, note, conv=None, conf="high", corrected=None, fix=True):
    d = {
        "page": page,
        "where": where,
        "scan": scan,
        "tex": tex,
        "kind": kind,
        "convention": conv,
        "confidence": conf,
        "fix": ({"old": L(old), "new": L(new)} if fix else None),
    }
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


def conv2(page, where, old, new, numeral):
    add(page, where, f"bold {numeral}", f"plain {numeral}", "convention", old, new,
        f"Bold chapter number {numeral} in the reference.", conv=2)


HEAD_NOTE = ("The print sets the label bold (bold parentheses and number, light subscript); the TeX puts it in math mode "
             "inside \\textbf, which typesets it in normal weight (math ignores \\textbf). Same fix as the p. 217 headings.")


def head_err(page, n):
    add(page, f"heading (Err_III, {n})", f"(Err_III, {n}) bold except the subscript III",
        r"\textbf{$(\mathbf{Err}_{\mathrm{III}},\," + str(n) + r")$}: parentheses and number in normal weight",
        "font", r"\textbf{$(\mathbf{Err}_{\mathrm{III}},\," + str(n) + r")$}",
        r"\textbf{($\mathbf{Err}_{\mathrm{III}}$, " + str(n) + r")}", HEAD_NOTE)


def head_0iii(page, num):
    add(page, f"heading (0_III, {num})", f"(0_III, {num}) bold except the subscript III",
        r"\textbf{$(0_{\mathrm{III}},\," + num + r")$}: whole label in normal weight",
        "font", r"\textbf{$(0_{\mathrm{III}},\," + num + r")$}",
        r"\textbf{($\mathbf{0}_{\mathrm{III}}$, " + num + r")}", HEAD_NOTE)


# ---------------------------------------------------------------- page 218
add(218, "first item: '(I), Index terminologique :'",
    "only '(I)' is bold; ', Index terminologique :' is roman",
    r"\textbf{(I), Index terminologique :} (all bold)", "font",
    r"\textbf{(I), Index terminologique :}", r"\textbf{(I)}, Index terminologique :",
    "Checked on an enlarged crop.")
conv2(218, "(I), Index terminologique: 'remplacer 0, 4.1.4'", r"remplacer 0, 4.1.4", r"remplacer \textbf{0}, 4.1.4", "0")
conv2(218, "(I), Index terminologique: 'par 0, 4.1.5'", r"par 0, 4.1.5", r"par \textbf{0}, 4.1.5", "0")
conv2(218, "(I), Index terminologique: 'remplacer I, 2.1.7'", r"remplacer I, 2.1.7", r"remplacer \textbf{I}, 2.1.7", "I")
conv2(218, "(I), Index terminologique: 'par I, 2.1.8 ;'", r"par I, 2.1.8 ;", r"par \textbf{I}, 2.1.8 ;", "I")
conv2(218, "(I), Index terminologique: 'remplacer I, 2.1.8'", r"remplacer I," + NL + "2.1.8", r"remplacer \textbf{I}," + NL + "2.1.8", "I")
conv2(218, "(I), Index terminologique: 'par I, 2.1.7.'", r"par I, 2.1.7.", r"par \textbf{I}, 2.1.7.", "I")
conv2(218, "(II, 4.2.7): '(III, 2.1.14)'", r"(III," + NL + "2.1.14)", r"(\textbf{III}," + NL + "2.1.14)", "III")
conv2(218, "(II, 4.2.7): '(III, 2.1.13)'", r"(III, 2.1.13)", r"(\textbf{III}, 2.1.13)", "III")
add(218, "(II, 5.2.1): 'remplacer X—U par U'", "X—U with the long dash", r"$X-U$ (minus sign)", "convention",
    r"$X-U$", r"$X\setmin U$", "Set difference printed with the long dash.", conv=7)
add(218, "(II, 5.2.1): 'remplacer X^f par X_f'",
    "X^f: superscript italic f (with its hook; same glyph as the subscript f of X_f), not a prime",
    r"$X'$", "symbol", r"remplacer $X'$ par", r"remplacer $X^f$ par",
    "Checked on a 5x crop. The erratum corrects EGA II p. 97, which reads 'la réunion des $X^f$ qui sont affines' "
    "(ega2-1-fr.tex, (5.2.1), under \\oldpage[II]{97}).")
conv2(218, "(II, 8.1.4): '(III, 2.3.8)'", r"(III, 2.3.8)", r"(\textbf{III}, 2.3.8)", "III")
conv2(218, "(II, 8.1.4): '(III, 2.3.7)'", r"(III, 2.3.7)", r"(\textbf{III}, 2.3.7)", "III")
head_0iii(218, "10.2.7")
add(218, "(0_III, 10.2.7): 'remplacer u-adique'", "Fraktur u (𝔲-adique)", r"italic $u$-adique", "font",
    r"$u$-adique", r"$\mathfrak u$-adique",
    "Checked on a 4x crop. The erratum quotes the turned letter of EGA 0_III p. 20, line 1 "
    "('topologie $\\mathfrak u$-adique' in ega3-1-fr.tex, proof of (10.2.7)).")
add(218, "(0_III, 10.2.7): 'par n-adique'", "Fraktur n (𝔫-adique: two legs)", r"$\mathfrak m$-adique", "symbol",
    r"$\mathfrak m$-adique", r"$\mathfrak n$-adique",
    "Checked on a 4x crop. In the proof of 0_III (10.2.7) the ideal is 'le radical $\\mathfrak n$ de $B$', so 𝔫 is "
    "also the mathematically intended reading.")
head_0iii(218, "11.1.1")
head_0iii(218, "11.8.6")
head_0iii(218, "12.3.4")
add(218, "(0_III, 12.3.4): 'remplacer ⥲ par →'", "isomorphism arrow (tilde above a right arrow), then a plain arrow",
    r"$\rightsquigarrow$ (wavy arrow) for the first symbol", "symbol",
    r"remplacer $\rightsquigarrow$ par $\to$", r"remplacer $\xrightarrow{\sim}$ par $\to$",
    "Checked on a 4x crop. The erratum concerns (12.3.4.1) on EGA 0_III p. 61, which has the isomorphism arrow "
    "(\\xrightarrow{\\sim} in ega3-1-fr.tex).")
head_0iii(218, "13.2.4")
add(218, "(III, 1.1.7): 'par ∧(A^r)'", "small wedge (about two thirds of the height of the A; the wedge of the main "
    "text, EGA III p. 85, is as tall as the capital)", r"$\bigwedge(A^r)$ (large operator)", "symbol",
    r"$\bigwedge(A^r)$", r"$\wedge(A^r)$",
    "Size of the sign only; compared side by side with p. 85 on an enlarged crop, where \\bigwedge is right.",
    conf="medium")
add(218, "(III, 2.5.3.1): 'remplacer —r≤n≤0'", "unary minus printed as the long dash", r"$-r\leq n\leq0$",
    "convention", r"$-r\leq n\leq0$", r"$\setmin r\leq n\leq0$",
    "Unary minus with the long dash (GLOBAL_ISSUES 23); \\setmin as for convention 7.", conv=7)
add(218, "(III, 2.5.3.1): 'par —r≤n<0'", "unary minus printed as the long dash", r"$-r\leq n<0$",
    "convention", r"$-r\leq n<0$", r"$\setmin r\leq n<0$",
    "Unary minus with the long dash (GLOBAL_ISSUES 23); \\setmin as for convention 7.", conv=7)
add(218, "(III, 3.1.2): 'par G∈K''", "bold italic K'", r"$\mathbf K'$ (bold upright)", "font",
    r"$\mathscr G\in\mathbf K'$", r"$\mathscr G\in\boldsymbol{K}'$",
    "Bold italic category letter, as page-fixed in EGA III section 3 (GLOBAL_ISSUES 44). Checked on a 4x crop.")
head_err(218, 1)
add(218, "(Err_III, 1): 'Dans (0_I, 5.1.3)'", "bold 0", "plain 0", "convention",
    r"$(0_{\mathrm I},\,5.1.3)$", r"($\mathbf{0}_{\mathrm I}$, 5.1.3)", "Bold 0.", conv=2)
head_err(218, 2)
add(218, "(Err_III, 2): 'Dans (0_I, 5.4.3)'", "bold 0", "plain 0", "convention",
    r"$(0_{\mathrm I},\,5.4.3)$", r"($\mathbf{0}_{\mathrm I}$, 5.4.3)", "Bold 0.", conv=2)

# ---------------------------------------------------------------- page 219
head_err(219, 3)
for n in ("7.2.4", "7.2.5", "7.2.6"):
    add(219, f"(Err_III, 3): '(0_I, {n})'", "bold 0", "plain 0", "convention",
        r"$(0_{\mathrm I},\," + n + r")$", r"($\mathbf{0}_{\mathrm I}$, " + n + ")", "Bold 0.", conv=2)
head_err(219, 4)
conv2(219, "(Err_III, 4): 'Après la proposition (I, 2.2.5)'", r"proposition" + NL + "(I, 2.2.5)",
      r"proposition" + NL + r"(\textbf{I}, 2.2.5)", "I")
conv2(219, "(Err_III, 4): 'avec les notations de (I, 2.2.5)'", r"notations de (I, 2.2.5)",
      r"notations de (\textbf{I}, 2.2.5)", "I")
add(219, "(Err_III, 4): 'on note JF'", "𝔍𝓕 with no tilde", r"$\widetilde{\mathfrak J\mathscr F}$", "symbol",
    r"on note $\widetilde{\mathfrak J\mathscr F}$", r"on note $\mathfrak J\mathscr F$",
    "Checked on a 3x crop: no tilde over the first 𝔍𝓕.")
add(219, "(Err_III, 4): 'le sous-O_X-Module J~F'", "tilde over the Fraktur J only (𝔍̃𝓕), the product of the ideal "
    "sheaf 𝔍̃ with 𝓕 as in (0, 4.3.5)", r"$\mathfrak J\widetilde{\mathscr F}$ (tilde over F)", "symbol",
    r"$\mathfrak J\widetilde{\mathscr F}$ défini", r"$\widetilde{\mathfrak J}\mathscr F$ défini",
    "Checked on a 5x crop: the tilde spans the 𝔍 and stops before the 𝓕.")
conv2(219, "(Err_III, 4): 'défini dans (0, 4.3.5)'", r"$(0,\,4.3.5)$", r"(\textbf{0}, 4.3.5)", "0")
head_err(219, 5)
conv2(219, "(Err_III, 5): 'Dans (I, 3.4.5)'", r"Dans (I, 3.4.5)", r"Dans (\textbf{I}, 3.4.5)", "I")
head_err(219, 6)
add(219, "(Err_III, 6): 'A la fin de la démonstration'", "'A' without accent", "'À'", "word",
    r"À la fin", r"A la fin", "Checked on a 4x crop: unaccented capital A.")
conv2(219, "(Err_III, 6): 'de (I, 3.6.1)'", r"(I, 3.6.1)", r"(\textbf{I}, 3.6.1)", "I")
conv2(219, "(Err_III, 6): 'par platitude (0, 1.3.2)'", r"$(0,\,1.3.2)$", r"(\textbf{0}, 1.3.2)", "0")
head_err(219, 7)
conv2(219, "(Err_III, 7): 'Dans (I, 5.1.1)'", r"Dans (I, 5.1.1)", r"Dans (\textbf{I}, 5.1.1)", "I")
add(219, "(Err_III, 7): '« O_X-Module quasi-cohérent »'", "'Module quasi-cohérent' in italics",
    "upright", "italics", r"$\mathscr O_X$-Module quasi-cohérent »",
    r"$\mathscr O_X$-\emph{Module quasi-cohérent} »", "Italic in the print, like the replacement text.")
head_err(219, 8)
conv2(219, "(Err_III, 8): 'Après (I, 5.1.10)'", r"Après (I, 5.1.10)", r"Après (\textbf{I}, 5.1.10)", "I")
add(219, "end of the page: '..., mais' / p. 220 'en supposant seulement'",
    "the sentence runs on to p. 220 (no paragraph break)", "blank line before \\oldpage[III]{220}", "other",
    r"soit un préschéma}, mais" + NL + NL, r"soit un préschéma}, mais" + NL,
    "Spurious paragraph break at a mid-sentence page break (GLOBAL_ISSUES 20); the edit lies at the end of p. 219's segment.")

# ---------------------------------------------------------------- page 220
add(220, "'(cf. (Err_II))'", "bold parentheses around Err_II (the outer closing parenthesis light)",
    r"$(\mathbf{Err}_{\mathrm{II}})$: parentheses in normal weight", "font",
    r"$(\mathbf{Err}_{\mathrm{II}})$", r"\textbf{($\mathbf{Err}_{\mathrm{II}}$)}",
    "Checked on a 6x crop: the inner parentheses are heavy, the outer ')' of '(cf. ...)' is light.", conf="medium")
head_err(220, 9)
conv2(220, "(Err_III, 9): 'Dans (I, 5.3.1)'", r"Dans (I, 5.3.1)", r"Dans (\textbf{I}, 5.3.1)", "I")
head_err(220, 10)
conv2(220, "(Err_III, 10): 'Dans (I, 5.3.9)'", r"Dans (I, 5.3.9)", r"Dans (\textbf{I}, 5.3.9)", "I")
head_err(220, 11)
conv2(220, "(Err_III, 11): 'Dans (I, 7.1.15)'", r"Dans (I, 7.1.15)", r"Dans (\textbf{I}, 7.1.15)", "I")
conv2(220, "(Err_III, 11): 'et (I, 7.1.16)'", r"(I, 7.1.16)", r"(\textbf{I}, 7.1.16)", "I")
head_err(220, 12)
conv2(220, "(Err_III, 12): 'Remplacer (I, 7.4.7)'", r"Remplacer (I, 7.4.7)", r"Remplacer (\textbf{I}, 7.4.7)", "I")
add(220, "(Err_III, 12): 'dire que F est un faisceau de torsion'",
    "roman capital F (wrong fount) where the rest of the passage has the script 𝓕",
    r"$\mathscr F$", "misprint_in_print", r"dire que $\mathscr F$ est un", r"dire que $F$ est un",
    "Silent correction in the TeX; the fix restores the printed letter (the edition's $F$ for the print's upright "
    "capital). Checked on a 3x crop, next to 'type fini 𝓕' on the line above.", corrected=r"$\mathscr F$")
head_err(220, 13)
conv2(220, "(Err_III, 13): 'Dans (I, 10.11.7)'", r"Dans (I, 10.11.7)", r"Dans (\textbf{I}, 10.11.7)", "I")
conv2(220, "(Err_III, 13): 'cohérents par (0, 5.3.5)'", r"$(0,\,5.3.5)$", r"(\textbf{0}, 5.3.5)", "0")
head_err(220, 14)
conv2(220, "(Err_III, 14): 'Dans (II, 1.7.8)'", r"Dans (II, 1.7.8)", r"Dans (\textbf{II}, 1.7.8)", "II")
head_err(220, 15)
conv2(220, "(Err_III, 15): 'Dans (II, 1.7.10)'", r"Dans (II, 1.7.10)", r"Dans (\textbf{II}, 1.7.10)", "II")
add(220, "(Err_III, 15): 'lignes 12 et 16-17'", "hyphen '16-17'", "en dash '16--17'", "punctuation",
    r"16--17", r"16-17", "Checked on a 3x crop: same length as the hyphens of the page.", conf="medium")
head_err(220, 16)
conv2(220, "(Err_III, 16): 'Dans (II, 1.7.12)'", r"Dans (II, 1.7.12)", r"Dans (\textbf{II}, 1.7.12)", "II")
head_err(220, 17)
conv2(220, "(Err_III, 17): 'Dans (II, 4.2.6)'", r"Dans (II, 4.2.6)", r"Dans (\textbf{II}, 4.2.6)", "II")
head_err(220, 18)
conv2(220, "(Err_III, 18): 'Dans (II, 4.6.13)'", r"Dans (II, 4.6.13)", r"Dans (\textbf{II}, 4.6.13)", "II")
add(220, "(Err_III, 18): 'afin d'appliquer (i bis)'", "'bis' italic", "upright", "italics",
    r"(i bis)", r"(i \emph{bis})", "GLOBAL_ISSUES 26.")
conv2(220, "(Err_III, 18): 'quasi-compact (I, 6.6.4)'", r"quasi-compact (I, 6.6.4)",
      r"quasi-compact (\textbf{I}, 6.6.4)", "I")

# ---------------------------------------------------------------- page 221
conv2(221, "top: 'immersion fermée (I, 5.4.3)'", r"(I, 5.4.3)", r"(\textbf{I}, 5.4.3)", "I")
conv2(221, "top: 'quasi-compacte (I, 6.6.4). Si au contraire'", r"(I, 6.6.4). Si", r"(\textbf{I}, 6.6.4). Si", "I")
conv2(221, "top: 'appliquer (I, 6.6.4)'", r"appliquer (I, 6.6.4)", r"appliquer (\textbf{I}, 6.6.4)", "I")
head_err(221, 19)
conv2(221, "(Err_III, 19): 'L'énoncé de (II, 5.2.2)'", r"(II," + NL + "5.2.2)", r"(\textbf{II}," + NL + "5.2.2)", "II")
conv2(221, "(Err_III, 19): '(I, 5.5.5 et 5.5.8)'", r"(I, 5.5.5 et 5.5.8)", r"(\textbf{I}, 5.5.5 et 5.5.8)", "I")
conv2(221, "(Err_III, 19): 'appliquer (I, 9.2.2)'", r"(I, 9.2.2)", r"(\textbf{I}, 9.2.2)", "I")
head_err(221, 20)
conv2(221, "(Err_III, 20): 'Dans (II, 6.2.3)'", r"Dans (II, 6.2.3)", r"Dans (\textbf{II}, 6.2.3)", "II")
add(221, "(Err_III, 20): 'p. 115 :' / 'On dit qu'un morphisme'",
    "the italic text continues the same paragraph: the line ending 'p. 115 :' is justified and 'On dit' starts flush "
    "left, not indented", "blank line: new indented paragraph", "other",
    r"p. 115 :" + NL + NL + r"\emph{On dit", r"p. 115 :" + NL + r"\emph{On dit",
    "Checked on a crop of the left margin; the replacement texts of (Err_III, 2) and (Err_III, 5), by contrast, start "
    "indented paragraphs.")
head_err(221, 21)
conv2(221, "(Err_III, 21): 'Dans (II, 6.4.3)'", r"Dans (II, 6.4.3)", r"Dans (\textbf{II}, 6.4.3)", "II")
head_err(221, 22)
add(221, "(Err_III, 22): 'Dans (0_III, 9.1.1)'", "bold 0", "plain 0", "convention",
    r"$(0_{\mathrm{III}},\,9.1.1)$", r"($\mathbf{0}_{\mathrm{III}}$, 9.1.1)", "Bold 0.", conv=2)
head_err(221, 23)
add(221, "(Err_III, 23): 'Dans (0_III, 11.7.3)'", "bold 0", "plain 0", "convention",
    r"$(0_{\mathrm{III}},\,11.7.3)$", r"($\mathbf{0}_{\mathrm{III}}$, 11.7.3)", "Bold 0.", conv=2)
add(221, "(Err_III, 23): 'après C'''", "bold italic C''", r"$\mathsf C''$ (sans serif)", "font",
    r"après $\mathsf C''$", r"après $\boldsymbol{C}''$",
    "Bold italic category letter (GLOBAL_ISSUES 33/35); the four \\mathsf of ega3-7 are all in this erratum.")
add(221, "(Err_III, 23): 'tout objet projectif P de C'", "bold italic C with no prime",
    r"$\mathsf C'$", "symbol", r"projectif $P$ de $\mathsf C'$", r"projectif $P$ de $\boldsymbol{C}$",
    "Checked on a 2x crop: no prime. Fix also sets the bold italic C. The print's reading is the coherent one: "
    "P in C and A'⇝T(P, A') exact on C', P' in C' and A⇝T(A, P') exact on C.")
add(221, "(Err_III, 23): '(resp. tout objet projectif P' de C')'", "bold italic C with one prime",
    r"$\mathsf C''$ (two primes)", "symbol", r"projectif $P'$ de $\mathsf C''$",
    r"projectif $P'$ de $\boldsymbol{C}'$", "Checked on a 2x crop: one prime. Fix also sets the bold italic C.")
add(221, "(Err_III, 23): 'soit exact dans C' (resp. C)'", "bold italic C', C", r"$\mathsf C'$, $\mathsf C$",
    "font", r"dans $\mathsf C'$ (resp. $\mathsf C$)", r"dans $\boldsymbol{C}'$ (resp. $\boldsymbol{C}$)",
    "Bold italic category letters.")
head_err(221, 24)
add(221, "(Err_III, 24): 'L'énoncé de (0_III, 13.7.7)'", "bold 0", "plain 0", "convention",
    r"$(0_{\mathrm{III}},\,13.7.7)$", r"($\mathbf{0}_{\mathrm{III}}$, 13.7.7)", "Bold 0.", conv=2)
add(221, "(Err_III, 24): 'supprimer « et (R^{n+1}T(A_k))_{k∈Z} »'", "'et' italic", "upright", "italics",
    r"supprimer « et" + NL + r"$(\mathrm R^{n+1}", r"supprimer « \emph{et}" + NL + r"$(\mathrm R^{n+1}",
    "Checked on a 2x crop.")
add(221, "(Err_III, 24): 'remplacer « R'^nT(A) est un ...'", "bold A in T(A)", "plain $A$", "font",
    r"remplacer" + NL + r"« $\mathrm R'^nT(A)$", r"remplacer" + NL + r"« $\mathrm R'^nT(\mathbf A)$",
    "The bold A of the projective system (A_k) of 0_III (13.7.7) ($\\mathbf A$ in ega3-1-fr.tex). Checked on a 2x crop.")
add(221, "(Err_III, 24): '... est un S-module de type fini »'", "'est un' and 'module de type fini' italic",
    "upright", "italics", r"est un $S$-module de type fini »", r"\emph{est un} $S$-\emph{module de type fini} »",
    "Quoted statement text, italic as in the print.")
add(221, "(Err_III, 24): 'par « R'^nT(A) et R'^{n+1}T(A) ...'", "bold A twice; 'et' italic",
    "plain $A$ twice; 'et' upright", "font",
    r"« $\mathrm R'^nT(A)$ et $\mathrm R'^{n+1}T(A)$",
    r"« $\mathrm R'^nT(\mathbf A)$ \emph{et} $\mathrm R'^{n+1}T(\mathbf A)$",
    "Bold A (as above) and the italic 'et' between the two terms, in one edit because they share the span.")
add(221, "(Err_III, 24): '... sont des S-modules de type fini »'", "'sont des' and 'modules de type fini' italic",
    "upright", "italics", r"sont des $S$-modules de type" + NL + "fini »",
    r"\emph{sont des} $S$-\emph{modules de type" + NL + "fini} »", "Quoted statement text, italic as in the print.")
add(221, "(Err_III, 24): 'lignes 12-13'", "hyphen '12-13'", "en dash '12--13'", "punctuation",
    r"12--13", r"12-13", "Checked on a 2x crop.", conf="medium")
add(221, "(Err_III, 24): 'supprimer « et p+q=n+1 »'", "'et' italic", "upright", "italics",
    r"supprimer « et $p+q=n+1$ »", r"supprimer « \emph{et} $p+q=n+1$ »",
    "Checked on a 2x crop; the later « et pour n+1 » is upright in the print, as in the TeX.")
head_err(221, 25)
conv2(221, "(Err_III, 25): 'Dans (III, 1.4.15)'", r"Dans (III, 1.4.15)", r"Dans (\textbf{III}, 1.4.15)", "III")
head_err(221, 26)
conv2(221, "(Err_III, 26): 'Dans (III, 2.2.4)'", r"Dans (III, 2.2.4)", r"Dans (\textbf{III}, 2.2.4)", "III")

# ---------------------------------------------------------------- page 222
conv2(222, "replacement text of (Err_III, 26): 'fermé dans Z (II, 5.4.10)'", r"(II, 5.4.10)", r"(\textbf{II}, 5.4.10)", "II")
conv2(222, "replacement text of (Err_III, 26): 'On sait (I, 9.4.3)'", r"(I, 9.4.3)", r"(\textbf{I}, 9.4.3)", "I")
head_err(222, 27)
conv2(222, "(Err_III, 27): 'Dans (III, 2.2.5)'", r"Dans (III, 2.2.5)", r"Dans (\textbf{III}, 2.2.5)", "III")
add(222, "(Err_III, 27) (iii): 'dont le support est propre sur Y'", "only 'propre' italic; 'sur Y' roman",
    r"\emph{propre sur $Y$}", "italics", r"\emph{propre sur $Y$}", r"\emph{propre} sur $Y$",
    "Checked on a 2x crop.")
add(222, "(Err_III, 27) (iii): 'aient leurs supports propres sur Y'", "only 'propres' italic; 'sur Y' roman",
    r"\emph{propres sur $Y$}", "italics", r"\emph{propres sur $Y$}", r"\emph{propres} sur $Y$",
    "Checked on a 2x crop.")
head_err(222, 28)
conv2(222, "(Err_III, 28): 'Dans (III, 4.4.9)'", r"Dans (III, 4.4.9)", r"Dans (\textbf{III}, 4.4.9)", "III")
add(222, "(Err_III, 28): 'localement de type fini sur k(y)'", "bold italic k", "plain $k$", "convention",
    r"sur $k(y)$", r"sur $\boldsymbol{k}(y)$", "Bold italic k in k(y).", conv=1)
head_err(222, 29)
add(222, "(Err_III, 29): 'dans (I, 9.3.4)'", "lower-case 'dans' after the label (every other item starts with a capital)",
    "'dans' (kept)", "misprint_in_print", None, None,
    "The TeX keeps the printed reading.", conf="medium", corrected="Dans", fix=False)
conv2(222, "(Err_III, 29): 'dans (I, 9.3.4)'", r"dans (I, 9.3.4)", r"dans (\textbf{I}, 9.3.4)", "I")
add(222, "page break inside 'quasi-|cohérent' (part 1 of 2)",
    "p. 222 ends with '« quasi-'; p. 223 begins 'cohérent de type fini ». Dans la démonstration, on se ramène au cas "
    "où X = Spec(A), ...' as one paragraph",
    "'cohérent de type fini ». Dans la démonstration, on se ramène au cas où' stands before \\oldpage[III]{223}, "
    "followed by a blank line (spurious paragraph break)", "marker",
    r"« \emph{quasi-cohérent de type fini} ». Dans la" + NL + "démonstration, on se ramène au cas où" + NL + NL,
    r"« \emph{quasi-}%" + NL,
    "Apply together with part 2 (p. 223). Moves the text after the page break behind the marker, splitting the "
    "word at its hyphen as in the homomor%|phismes precedent (EGA III p. 126), and removes the blank line.")

# ---------------------------------------------------------------- page 223
add(223, "page break inside 'quasi-|cohérent' (part 2 of 2)", "see part 1 (p. 222)", "see part 1 (p. 222)", "marker",
    r"\oldpage[III]{223}" + NL + r"$X=\operatorname{Spec}(A)$",
    r"\oldpage[III]{223}" + NL + r"\emph{cohérent de type fini} ». Dans la" + NL
    + "démonstration, on se ramène au cas où" + NL + r"$X=\operatorname{Spec}(A)$",
    "Apply together with part 1 (p. 222). \\oldpage ends with \\ignorespaces, so with the % of part 1 the word "
    "prints as 'quasi-cohérent' without a space.")
head_err(223, 30)
conv2(223, "(Err_III, 30): 'Dans (I, 9.3.5)'", r"Dans (I, 9.3.5)", r"Dans (\textbf{I}, 9.3.5)", "I")
add(223, "(Err_III, 30), proof: 'l'Idéal J de O_X, annulateur de F'", "only 'annulateur' italic; 'de 𝓕' roman",
    r"\emph{annulateur de $\mathscr F$}", "italics", r"\emph{annulateur de $\mathscr F$}",
    r"\emph{annulateur} de $\mathscr F$", "Checked on a 2.5x crop.")
conv2(223, "(Err_III, 30), proof: 'défini par J (I, 4.1.2)'", r"(I, 4.1.2)", r"(\textbf{I}, 4.1.2)", "I")
add(223, "(Err_III, 30), proof: 'l'homomorphisme s⇝sx_i'", "wavy arrow", r"\mapsto", "symbol",
    r"$s\mapsto sx_i$", r"$s\leadsto sx_i$", "Checked on a 4x crop. Wavy arrow (\\leadsto), not convention 3 (GLOBAL_ISSUES 33/53).")
conv2(223, "(Err_III, 30), proof: 'Idéal quasi-cohérent (I, 4.1.1)'", r"(I, 4.1.1)", r"(\textbf{I}, 4.1.1)", "I")
conv2(223, "(Err_III, 30), proof: 'Idéal quasi-cohérent (I, 1.3.10)'", r"(I," + NL + "1.3.10)", r"(\textbf{I}," + NL + "1.3.10)", "I")
add(223, "end of the page (end of the errata and of the fascicle)", "short centred closing rule below the last line",
    "nothing", "missing", r"1.3.10).", r"1.3.10)." + NL + NL + r"\begin{center}\rule{25mm}{0.4pt}\end{center}",
    "End-of-article rule; the closing rules of the other fascicles (e.g. after 'Reçu le 22 juillet 1960.', EGA II "
    "p. 215) are not reproduced either: a document-wide decision, apply only if all are added. The 'old' shares "
    "'1.3.10)' with the convention-2 edit of '(I, 1.3.10)'; neither edit changes the shared text, so either order "
    "applies.", conf="low")

# ---------------------------------------------------------------- checks
texts = {}
for p in range(218, 224):
    texts[p] = (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")

bad = 0
for i, x in enumerate(F):
    fx = x["fix"]
    if fx is None:
        continue
    c = texts[x["page"]].count(fx["old"])
    if c != 1:
        bad += 1
        print("NOT UNIQUE", c, x["page"], repr(fx["old"]))

# overlapping 'old' spans on the same page
for p in texts:
    spans = []
    for x in F:
        if x["page"] != p or x["fix"] is None:
            continue
        o = x["fix"]["old"]
        s = texts[p].find(o)
        spans.append((s, s + len(o), o))
    spans.sort()
    for a, b in zip(spans, spans[1:]):
        if b[0] < a[1]:
            print("OVERLAP", p, repr(a[2]), repr(b[2]))

# simulate applying the fixes in order, per page
for p in texts:
    t = texts[p]
    for x in F:
        if x["page"] != p or x["fix"] is None:
            continue
        o, nw = x["fix"]["old"], x["fix"]["new"]
        if t.count(o) != 1:
            print("APPLY FAIL", p, repr(o))
            continue
        t = t.replace(o, nw)

from collections import Counter
cnt = Counter()
for x in F:
    k = "misprint" if x["kind"] == "misprint_in_print" else ("convention" if x["kind"] == "convention" else "normal")
    cnt[(x["page"], k)] += 1
for p in range(218, 224):
    print(p, cnt[(p, "normal")], cnt[(p, "convention")], cnt[(p, "misprint")])
print("total", len(F), "bad", bad)
OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", OUT)
