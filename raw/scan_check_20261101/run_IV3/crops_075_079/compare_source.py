import difflib, re

RUN = r"user\Documents\ega_scan_check_20261101\run_IV3"
SRC = (r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\current"
       r"\packages\IV3\native\ega4\ega4-9-fr.tex")
DIP = SRC.replace(r"\current\packages", r"\diplomatic\packages")

for path in (SRC, DIP):
    src = open(path, encoding="utf-8").read()
    print("=====", path.split("2026-10-24-r20\\")[1])
    for p in range(75, 80):
        a = src.find("\\oldpage[IV-3]{%d}" % p)
        b = src.find("\\oldpage[IV-3]{%d}" % (p + 1))
        seg = src[a:b]
        with open(rf"{RUN}\page_{p:03d}.tex", encoding="utf-8", newline="") as f:
            pg = f.read().replace("\r\n", "\n")
        pg = pg.split("\n", 1)[1]  # drop '% from ...' line
        if seg == pg:
            print(p, "identical")
        else:
            print(p, "DIFFERS")
            for line in difflib.unified_diff(pg.splitlines(), seg.splitlines(), "page_file", "source", n=1, lineterm=""):
                print("   ", line)
