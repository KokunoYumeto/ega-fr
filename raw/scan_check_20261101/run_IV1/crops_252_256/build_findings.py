"""Build findings_252_256.json for EGA IV-1 pages 252-256 (index pages).

Convention-2 entries (bold 0 / IV in each index reference) are generated from
the page TeX; the other findings are listed by hand below. Every fix's "old"
is checked to occur exactly once in its page file, and the fixes of each page
are applied in order to check that they still apply one after another.
"""
import json
import re
import sys

RUN = sys.argv[1]
OUT = sys.argv[2]
PAGES = [252, 253, 254, 255, 256]

texts = {}
for p in PAGES:
    # the page files here have CRLF; the release files use LF
    with open(f"{RUN}/page_{p}.tex", encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")

# Hand-written findings, keyed by page; each is inserted after the convention
# entry of the same line (so that the convention fix is listed first).
manual = {
    252: [
        {
            "anchor": r"$\dim_c(X)$, $\dim(X)$",
            "where": "first entry of the Index des notations: 'dimc(X), dim(X) (X espace topologique) : 0, 14.1.2.'",
            "scan": "'dimc(X)': the c is full size on the baseline, run on to dim (not a subscript; compare dim_x(X) on the next line)",
            "tex": r"$\dim_c(X)$ (subscript c): silent correction",
            "kind": "misprint_in_print",
            "convention": None,
            "confidence": "medium",
            "fix": {"old": r"$\dim_c(X)$", "new": r"$\operatorname{dimc}(X)$"},
            "corrected": r"$\dim_c(X)$",
            "note": "The index repeats the printing of Définition (14.1.2), where the same run-on 'dimc(X)' was reported as a misprint (0_IV-1 p. 6); same fix and corrected reading here.",
        },
        {
            "anchor": r"$\mathrm H_A^2(B,L)$, $\mathrm H_A^2(B,L)^s$",
            "where": "entry 'H^i_A(B, L), H^2_A(B, L)^s : 0, 18.4.3.'",
            "scan": "first symbol H^i_A(B, L), with italic superscript i",
            "tex": r"$\mathrm H_A^2(B,L)$ (superscript 2)",
            "kind": "formula",
            "convention": None,
            "confidence": "high",
            "fix": {"old": r"\mathrm H_A^2(B,L)$, ", "new": r"\mathrm H_A^i(B,L)$, "},
            "note": "The TeX has H^2 twice. (18.4.3) introduces the Hochschild group H^2_A(B,L) and H^2_A(B,L)^s, (18.4.4) the groups H^i_A(B,L); indexing the general H^i_A(B,L) at 18.4.3 is a plausible reading, so this is treated as a transcription error, not a misprint.",
        },
    ],
    253: [
        {
            "anchor": r"$\chi_E$ ($E$ $B$-algèbre topologique)",
            "where": "entry 'χ_E (E B-algèbre topologique) : 0, 20.7.10'",
            "scan": "the entry ends with a comma: '20.7.10,'",
            "tex": "20.7.10. (period): silent correction",
            "kind": "misprint_in_print",
            "convention": None,
            "confidence": "high",
            "fix": {"old": "20.7.10.\\par", "new": "20.7.10,\\par"},
            "corrected": "20.7.10.",
            "note": "Every other index entry ends with a period.",
        },
    ],
    254: [
        {
            "anchor": r"$A$-algèbre de Cohen",
            "where": "entry 'A-algèbre de Cohen : 0, 19.8.1.'",
            "scan": "the initial A is bold (wrong fount); the hyphen and 'algèbre' are roman, and the A of the neighbouring entries 'A-algèbre essentiellement de type fini', 'A-anneau' is roman",
            "tex": "$A$ (roman): silent correction",
            "kind": "misprint_in_print",
            "convention": None,
            "confidence": "medium",
            "fix": {"old": r"$A$-algèbre de Cohen", "new": r"$\mathbf{A}$-algèbre de Cohen"},
            "corrected": r"$A$-algèbre de Cohen",
            "note": "Measured on the 300 dpi strip: this A carries about 1.3 times the ink of the other line-initial A's on pp. 254-256 (the same ratio as the bold I of 'IV' to a roman I), with a thicker hairline and a partly filled counter. Drop it if judged an inking variation.",
        },
    ],
}

# Special-cased convention "old" strings (to keep them apart from another fix
# on the same line).
special_old = {
    (253, r"$\chi_E$ ($E$ $B$-algèbre topologique)"): "$B$-algèbre topologique) : 0,",
}

ref_re = re.compile(r" : (0|IV), ")


def plain(s):
    s = s.replace("\\par", "").strip()
    return s


def unique_old(text, line_start, m_start, m_end):
    """Smallest old string, starting at ': 0,' (m_start + 1), ending at m_end
    and extended left word by word (never before the line start), that occurs
    once in the text."""
    start = m_start + 1
    while True:
        cand = text[start:m_end]
        if text.count(cand) == 1:
            return cand
        if start <= line_start:
            raise SystemExit(f"cannot make unique: {cand!r}")
        # start - 1 is the space before the current first word; move to the
        # beginning of the previous word
        j = text.rfind(" ", line_start, start - 1)
        start = line_start if j < 0 else j + 1


findings = []
for p in PAGES:
    text = texts[p]
    lines_done = []
    pos = 0
    for line in text.split("\n"):
        line_start = pos
        pos += len(line) + 1
        m = ref_re.search(line)
        if not m:
            continue
        numeral = m.group(1)
        # reference text after the numeral, up to and including the final
        # period (the period keeps 17.2.1. apart from 17.2.14.)
        rest = line[m.end():]
        assert rest.endswith(".\\par"), repr(line)
        ref = rest[: -len("\\par")]
        entry = plain(line)
        key = None
        for (pp, anchor), val in special_old.items():
            if pp == p and anchor in line:
                key = val
        if key is not None:
            old = key
        else:
            a = line_start + m.start()
            b = line_start + m.end() + len(ref)
            old = unique_old(text, line_start, a, b)
        new = old.replace(f": {numeral},", f": \\textbf{{{numeral}}},", 1)
        assert new != old, old
        findings.append({
            "page": p,
            "where": f"index entry '{entry[:90]}{'...' if len(entry) > 90 else ''}'",
            "scan": f"bold {numeral} in the reference '{numeral}, {ref.rstrip('.')}'",
            "tex": f"plain {numeral}",
            "kind": "convention",
            "convention": 2,
            "confidence": "high",
            "fix": {"old": old, "new": new},
            "note": "Bold chapter numeral in the index reference.",
        })
        for mf in manual.get(p, []):
            if mf["anchor"] in line:
                f = {k: v for k, v in mf.items() if k != "anchor"}
                f["page"] = p
                findings.append(f)

# every manual finding must have been placed
placed = {(f["page"], f["where"]) for f in findings}
for p, lst in manual.items():
    for mf in lst:
        assert (p, mf["where"]) in placed, mf["where"]

# order the keys as in the checker prompt
order = ["page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "corrected", "note"]
findings = [{k: f[k] for k in order if k in f} for f in findings]

# checks: each old occurs exactly once in its page file; sequential application
for f in findings:
    if f["fix"] is None:
        continue
    n = texts[f["page"]].count(f["fix"]["old"])
    assert n == 1, (f["page"], f["fix"]["old"], n)
for p in PAGES:
    t = texts[p]
    for f in findings:
        if f["page"] != p or f["fix"] is None:
            continue
        n = t.count(f["fix"]["old"])
        assert n == 1, ("sequential", p, f["fix"]["old"], n)
        t = t.replace(f["fix"]["old"], f["fix"]["new"], 1)

with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(findings, fh, ensure_ascii=False, indent=1)
    fh.write("\n")

from collections import Counter
c = Counter()
for f in findings:
    k = "convention" if f["kind"] == "convention" else "misprint" if f["kind"] == "misprint_in_print" else "normal"
    c[(f["page"], k)] += 1
for p in PAGES:
    print(p, "normal", c[(p, "normal")], "convention", c[(p, "convention")], "misprint", c[(p, "misprint")])
print("total", len(findings))
