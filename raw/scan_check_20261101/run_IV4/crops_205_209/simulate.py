# Simulates apply_fixes.py on an in-memory copy of ega4-18-fr.tex (no .tex file of the edition is written).
# Writes the patched region and stubs into this crops folder for a test compile.
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
SRC = pathlib.Path(r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic"
                   r"\packages\IV4\native\ega4\ega4-18-fr.tex")
spec = importlib.util.spec_from_file_location("bf", HERE / "build_findings.py")
bf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bf)
F = bf.F

marker = re.compile(r"\\oldpage\[IV-4\]\{(\d+)\}")


def locate(t, page):
    cuts = [(int(m.group(1)), m.start()) for m in marker.finditer(t)]
    for i, (n, s) in enumerate(cuts):
        if n == page:
            j = i + 1
            while j < len(cuts) and cuts[j][0] == page:
                j += 1
            return s, cuts[j][1] if j < len(cuts) else len(t)
    for (a, sa), (b, sb) in zip(cuts, cuts[1:]):
        if a < page < b:
            return sa, sb
    return None, None


orig = SRC.read_text(encoding="utf-8")
# (a) each old exactly once in the CURRENT source segment of its page (before any edit)
bad = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    s, e = locate(orig, x["page"])
    c = orig[s:e].count(x["fix"]["old"])
    if c != 1:
        bad += 1
        print("SOURCE COUNT", c, i, x["page"], repr(x["fix"]["old"][:70]))
print("source check:", "ok" if not bad else f"{bad} bad")
wide = [i for i, x in enumerate(F) if x["fix"] and orig.count(x["fix"]["old"]) != 1]
print("file-wide unique:", "ok" if not wide else f"not unique: {wide}")

# (b) sequential application in list order
t = orig
fail = 0
for i, x in enumerate(F):
    if not x["fix"]:
        continue
    s, e = locate(t, x["page"])
    seg = t[s:e]
    c = seg.count(x["fix"]["old"])
    if c != 1:
        fail += 1
        print("APPLY FAIL", c, i, x["page"], repr(x["fix"]["old"][:70]))
        continue
    t = t[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + t[e:]
print("sequential apply:", "ok" if not fail else f"{fail} failed")

# also the corrected-edition variant: misprint fixes skipped
tc = orig
for x in F:
    if not x["fix"] or x["kind"] == "misprint_in_print":
        continue
    s, e = locate(tc, x["page"])
    seg = tc[s:e]
    if seg.count(x["fix"]["old"]) == 1:
        tc = tc[:s] + seg.replace(x["fix"]["old"], x["fix"]["new"]) + tc[e:]


def region(text):
    a = text.index("\\subsection{Critères de M-régularité.}")
    b = text.index("\\begin{env}[19.6.2]")
    return text[a:b]


(HERE / "test_patched.tex").write_text(region(t), encoding="utf-8", newline="\n")
(HERE / "test_orig.tex").write_text(region(orig), encoding="utf-8", newline="\n")
(HERE / "test_corrected.tex").write_text(region(tc), encoding="utf-8", newline="\n")
print("markers in patched region:", [m.group(1) for m in marker.finditer(region(t))])
