import sys, difflib
sys.stdout.reconfigure(encoding="utf-8")
sys.argv=[sys.argv[0]]+sys.argv[1:]
exec(open("ocr_diff2.py",encoding="utf-8").read().split("for n in range")[0])
for n in range(160,165):
    txt=""
    for s in range(1,5):
        txt+=open(out+r"\ocr_%03d_s%d.txt"%(n,s),encoding="utf-8").read()+"\n"
    ow=words_from_text(txt)
    tw=tex_words(open(base+r"\page_%03d.tex"%n,encoding="utf-8").read())
    sm=difflib.SequenceMatcher(None,tw,ow,autojunk=False)
    for op,a1,a2,b1,b2 in sm.get_opcodes():
        if op=="delete":
            print(n,"TEX ctx:"," ".join(tw[max(0,a1-6):a2+6]),"| OCR ctx:"," ".join(ow[max(0,b1-6):b1+6]))
