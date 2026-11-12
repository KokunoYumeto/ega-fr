"""For every index entry of pp. 338-339, look at the text after its link target in the IV-4 sources and report
which significant words of the term occur there (read-only heuristic to spot misprinted references)."""
import re
import sys
import unicodedata

src = r"user/Documents/ega_scan_check_20261101/ega-fr/editions/2026-10-24-r20/diplomatic/packages/IV4/native/ega4/"
base = r"user/Documents/ega_scan_check_20261101/run_IVback/"
files = ["ega4-16-fr.tex", "ega4-17-fr.tex", "ega4-18-fr.tex", "ega4-20-fr.tex",
         "ega4-21a-fr.tex", "ega4-21b-fr.tex", "ega4-21c-fr.tex"]
alltex = "".join(open(src + f, encoding="utf-8").read() for f in files)
low = alltex.lower()
stop = set("un une de des du d la le les l en et à au aux sur par ou pour relativement relative point "
           "morphisme morphismes préschéma préschémas d'un d'une n-ème".split())
pat = re.compile(r"\\EGAIVterm\{(.*?)\}\{(.*)\}\s*$")
link = re.compile(r"\\hyperlink\{([^}]*)\}\{([^}]*)\}")
WINDOW = 3500
for p in [338, 339]:
    for line in open(base + f"page_{p}.tex", encoding="utf-8").read().splitlines():
        m = pat.match(line)
        if not m:
            continue
        term, refs = m.groups()
        words = re.findall(r"[a-zà-ÿœæ'\-]+", re.sub(r"\$[^$]*\$", " ", term.lower()))
        words = [w.strip("'-") for w in words]
        words = [w for w in words if len(w) > 3 and w not in stop]
        for t, num in link.findall(refs):
            i = alltex.find("{" + t + "}")
            if i < 0:
                sys.stdout.write(f"{p} {num}: target {t} not found\n")
                continue
            win = low[max(0, i - 600):i + WINDOW]
            miss = [w for w in words if w[:-1] not in win]  # crude stem: drop last letter
            flag = "" if not miss else "  MISSING: " + ", ".join(miss)
            sys.stdout.write(f"{p} {num:9} {term[:70]}{flag}\n")
