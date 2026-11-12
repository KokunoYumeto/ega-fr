import re, collections, sys
base = r"user\Documents\ega_scan_check_20261101\ega-fr\source\ega3"
for f in ["ega3-6-fr.tex", "ega3-7-fr.tex"]:
    t = open(base + "\\" + f, encoding="utf-8").read()
    m = re.findall(r"\$0_\{\\mathrm I\}\$, (\d+)\.", t)
    print(f, "0_I refs:", len(m), dict(collections.Counter(m)))
    m2 = re.findall(r"\(0, (\d+)\.", t)
    print("   plain (0, n.):", dict(collections.Counter(m2)))
    m3 = re.findall(r"\\mathscr E", t)
    m4 = re.findall(r"\{\}\^\{\([a-z]'?\)\}\\mathscr E", t)
    print("   {}^{(t)}\\mathscr E:", len(m4))
    m5 = re.findall(r"\(6\.6\.7, \$t\$\)", t)
    print("   (6.6.7, $t$):", len(m5), " tag:", len(re.findall(r"tag\{6\.6\.7, \$t\$\}", t)))
