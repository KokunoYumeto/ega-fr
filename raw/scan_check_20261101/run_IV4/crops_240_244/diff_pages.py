"""Compare page_NNN.tex (prepared earlier) with the current source segment between markers."""
import difflib, re, pathlib
SRC = pathlib.Path("user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/ega4-20-fr.tex")
RUN = pathlib.Path("user/Documents/ega_scan_check_20261101/run_IV4")
src = SRC.read_text(encoding="utf-8")
lines = src.split("\n")
pos = {}
for i, l in enumerate(lines):
    m = re.search(r"\\oldpage\[IV-4\]\{(\d+)\}", l)
    if m:
        pos[int(m.group(1))] = i
for p in range(240, 245):
    seg = lines[pos[p]:pos[p + 1]]
    page = (RUN / f"page_{p}.tex").read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    page = page[1:]  # drop the '% from' line
    while page and page[-1] == "":
        page.pop()
    seg2 = list(seg)
    while seg2 and seg2[-1] == "":
        seg2.pop()
    d = list(difflib.unified_diff(page, seg2, "page_%d.tex" % p, "source", lineterm="", n=0))
    print(p, "IDENTICAL" if not d else "DIFFERS")
    for x in d[:40]:
        print("   ", x[:200])
