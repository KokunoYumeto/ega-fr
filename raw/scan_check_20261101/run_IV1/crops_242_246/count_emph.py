import re, sys
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101\ega-fr\editions\2026-10-24-r20\diplomatic\packages\IV1\native\ega4"
fn = base + "\\" + (sys.argv[1] if len(sys.argv) > 1 else "ega4-1-fr.tex")
s = open(fn, encoding="utf-8").read()
for env in ["definition", "proposition", "theorem", "corollary", "lemma"]:
    pat = re.compile(r"\\begin\{" + env + r"\}(.*?)\\end\{" + env + r"\}", re.S)
    blocks = pat.findall(s)
    n = sum(b.count("\\emph{") for b in blocks)
    nb = sum(1 for b in blocks if "\\emph{" in b)
    print(env, len(blocks), "blocks;", nb, "with \\emph;", n, "\\emph total")
    if env == "definition":
        for b in blocks:
            for m in re.finditer(r"\\emph\{([^{}]*)\}", b):
                print("   ", m.group(1)[:60])
