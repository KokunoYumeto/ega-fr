import json
import pathlib

RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_IV2")
OUT = RUN / "findings_225_229.json"

F = []


def add(page, where, scan, tex, kind, fix, note, convention=None, confidence="high", corrected=None):
    d = {"page": page, "where": where, "scan": scan, "tex": tex, "kind": kind, "convention": convention,
         "confidence": confidence, "fix": fix}
    if kind == "misprint_in_print":
        d["corrected"] = corrected
    d["note"] = note
    F.append(d)


# ---- p. 225, Index des notations
add(225, "Index des notations, entry 'deg.tr_K L (L extension du corps K) : 4.1.'",
    "deg.tr_K L: no period after 'tr', the subscript K follows directly (2x crop)",
    "$\\operatorname{deg.tr.}_K L$ (period after tr)",
    "punctuation",
    {"old": "\\operatorname{deg.tr.}_K L", "new": "\\operatorname{deg.tr}_K L"},
    "The main text writes \\operatorname{deg.tr}_K L as well (definition in 4.1, source line 3947).")

# ---- p. 226, Index terminologique
add(226, "Index terminologique, entry 'P-anneau : 7.3.13.'",
    "bold italic P (3x crop), hyphen and 'anneau' roman",
    "$P$-anneau (plain italic P)",
    "font",
    {"old": "$P$-anneau", "new": "$\\boldsymbol P$-anneau"},
    "The property letter P, written \\boldsymbol P in the main text (7.3.13). The TeX has plain $P$, not \\mathbf, so this "
    "is not convention 10.")

add(226, "Index terminologique, entry 'Décomposition irredondante, décomposition irredondante réduite d'un Module : 3.2.5'",
    "the entry ends '3.2.5' with no final period (enlarged crop; no ink after the 5); every other entry ends with a period",
    "\\EGAIVtwoTerm{...}{3.2.5}: the macro adds the period (silent correction)",
    "misprint_in_print",
    {"old": "\\EGAIVtwoTerm{Décomposition irredondante, décomposition irredondante réduite\nd'un Module}{3.2.5}",
     "new": "Décomposition irredondante, décomposition irredondante réduite\nd'un Module : 3.2.5\\par"},
    "The period comes from \\EGAIVtwoTerm (#1 : #2.\\par), so the diplomatic text writes this one entry out without the "
    "macro (same output minus the period); the corrected edition keeps the macro call. Medium: a sort lost in printing "
    "cannot be excluded, but no trace of a period is visible.",
    confidence="medium",
    corrected="\\EGAIVtwoTerm{Décomposition irredondante, décomposition irredondante réduite\nd'un Module}{3.2.5}")

# ---- p. 227
add(227, "Index terminologique, entry 'P-morphisme : 7.3.1.'",
    "bold italic P (3x crop)",
    "$P$-morphisme (plain italic P)",
    "font",
    {"old": "$P$-morphisme", "new": "$\\boldsymbol P$-morphisme"},
    "Property letter P, \\boldsymbol P in the main text (7.3.1 ff.). Not convention 10 (the TeX has plain $P$).")

add(227, "Index terminologique, entry 'Préschéma connexe en codimension d—1 : 5.10.8.'",
    "long dash for the minus in d—1 (2x crop)",
    "$d-1$",
    "convention",
    {"old": "$d-1$", "new": "$d\\setmin 1$"},
    "Subtraction printed with the long dash (GLOBAL_ISSUES 23); form of the fix as for the other convention-7 findings in "
    "ega4-2.",
    convention=7)

# ---- p. 228
add(228, "Index terminologique, entry 'Propriété P du premier type (du second type) associée à une propriété R ...'",
    "bold italic P",
    "$P$ (plain italic)",
    "font",
    {"old": "Propriété $P$ du premier", "new": "Propriété $\\boldsymbol P$ du premier"},
    "Property letter P, \\boldsymbol P in the main text (7.3.10). Not convention 10 (the TeX has plain $P$).")

add(228, "same entry, '... associée à une propriété R d'anneaux locaux noethériens : 7.3.10.'",
    "bold italic R",
    "$R$ (plain italic)",
    "font",
    {"old": "propriété $R$ d'anneaux", "new": "propriété $\\boldsymbol R$ d'anneaux"},
    "The property R of local rings is \\boldsymbol R in the main text (7.3.10 ff.).")

add(228, "Index terminologique, entry 'Propriété P géométrique : 7.3.6.'",
    "bold italic P",
    "$P$ (plain italic)",
    "font",
    {"old": "Propriété $P$ géométrique", "new": "Propriété $\\boldsymbol P$ géométrique"},
    "Property letter P, as in the two entries above.")

# ---- p. 229, Table des matières
add(229, "Table des matières, top right above the page-number column (before the Chapitre IV line)",
    "column head 'Pages' in small capitals, a short rule under it",
    "(nothing)",
    "missing",
    {"old": "\\setlength{\\parskip}{1.5pt}\n", "new": "\\setlength{\\parskip}{1.5pt}\n\\hfill\\textsc{Pages}\\par\n"},
    "Contents column head, as added for the EGA II, EGA III part 1 and EGA IV part 1 contents (GLOBAL_ISSUES 45); the "
    "rule under it is layout. Placed inside the group so that it gets \\small; it does not touch the \\newcommand line.")

add(229, "\\newcommand{\\EGAIVtwoContentsLine} (labels of every contents line, pp. 229-231)",
    "the labels 'Chapitre IV.', '§ 2.', '2.1.', ..., '4.6.' are set in regular weight (enlarged crop)",
    "\\textbf{#1}: every label bold",
    "font",
    {"old": "{\\textbf{#1}\\quad #2\\dotfill #3\\par}", "new": "{#1\\quad #2\\dotfill #3\\par}"},
    "One edit for all labels of pp. 229-231 (the macro is defined in this page's segment).")

add(229, "contents line 'Chapitre IV. — Étude locale des schémas et des morphismes des schémas (suite) ... 5'",
    "'CHAPITRE' in small capitals with a full capital C, 'IV.' in capitals, regular weight (enlarged crop)",
    "{CHAPITRE IV.} (full capitals, bold through the macro)",
    "font",
    {"old": "\\EGAIVtwoContentsLine{CHAPITRE IV.}", "new": "\\EGAIVtwoContentsLine{\\textsc{Chapitre IV.}}"},
    "Independent of the macro fix and of the dash fix (no overlap).")

add(229, "same line, between 'IV.' and 'Étude'",
    "a long dash: 'CHAPITRE IV. — Étude locale ...'",
    "no dash",
    "punctuation",
    {"old": "{\\textbf{Étude locale", "new": "{--- \\textbf{Étude locale"},
    "As in the EGA IV part 1 contents (Chapitre 0 line). The new string ends the dash with a space before \\textbf.")

OUT.write_text(json.dumps(F, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# check every fix's old string occurs exactly once in its page file (CRLF normalised to LF)
ok = True
for d in F:
    if not d["fix"]:
        continue
    t = (RUN / f"page_{d['page']:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    n = t.count(d["fix"]["old"])
    if n != 1:
        ok = False
    print(d["page"], n, repr(d["fix"]["old"][:60]))
print("all unique" if ok else "PROBLEM")
counts = {}
for d in F:
    c = counts.setdefault(d["page"], [0, 0, 0])
    c[1 if d["kind"] == "convention" else 2 if d["kind"] == "misprint_in_print" else 0] += 1
print(counts)
