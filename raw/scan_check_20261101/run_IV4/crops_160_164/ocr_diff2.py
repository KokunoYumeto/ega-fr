import subprocess, re, sys, unicodedata, difflib, os
sys.stdout.reconfigure(encoding="utf-8")
base = r"user\Documents\ega_scan_check_20261101\run_IV4"
out = base + r"\crops_160_164"
tess = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def words_from_text(t):
    t = strip_acc(t).lower()
    t = t.replace("\u2019", "'")
    ws = re.findall(r"[a-z]+", t)
    return [w for w in ws if len(w) >= 2]

def tex_words(tex):
    t = tex
    t = re.sub(r"^%.*$", "", t, flags=re.M)
    t = re.sub(r"\\\[.*?\\\]", " ", t, flags=re.S)
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\(label|EGAReaderTarget|oldpage|begin|end)(\[[^\]]*\])?(\{[^}]*\})*", " ", t)
    t = re.sub(r"\\item\[[^\]]*\]", " ", t)
    t = re.sub(r"\\textsuperscript\{o\}", "o", t)
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    return words_from_text(t)

for n in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    txt = ""
    for s in range(1, 5):
        img = base + r"\page_%03d_s%d.png" % (n, s)
        ob = out + r"\ocr_%03d_s%d" % (n, s)
        if not os.path.exists(ob + ".txt"):
            subprocess.run([tess, img, ob, "-l", "eng", "--psm", "6"], capture_output=True)
        txt += open(ob + ".txt", encoding="utf-8").read() + "\n"
    ow = words_from_text(txt)
    tw = tex_words(open(base + r"\page_%03d.tex" % n, encoding="utf-8").read())
    sm = difflib.SequenceMatcher(None, tw, ow, autojunk=False)
    print("===== page", n, "tex words", len(tw), "ocr words", len(ow))
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == "equal":
            continue
        print("%-8s TEX: %-45s OCR: %s" % (op, " ".join(tw[a1:a2])[:45], " ".join(ow[b1:b2])[:80]))
