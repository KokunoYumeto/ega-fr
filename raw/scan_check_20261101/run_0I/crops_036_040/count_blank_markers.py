import json, pathlib, re
E = pathlib.Path(r"user\Documents\ega_scan_check_20261101")
inv = json.load(open(E / "page_inventory_r20.json", encoding="utf-8"))["parts"]
pat = re.compile(r"\\oldpage\[[^\]]*\]\{\d+\}")
tot_m = tot_b = tot_low = 0
seen = set()
for part, d in inv.items():
    for f in d["files"]:
        if f in seen:
            continue
        seen.add(f)
        t = pathlib.Path(f).read_text(encoding="utf-8")
        m_n = b_n = low_n = 0
        for m in pat.finditer(t):
            m_n += 1
            if t[:m.start()].endswith("\n\n"):
                b_n += 1
                nxt = t[m.end():].lstrip("\n").lstrip(" ")
                if nxt[:1].islower():
                    low_n += 1
        tot_m += m_n; tot_b += b_n; tot_low += low_n
        if pathlib.Path(f).name == "ega0-1-fr.tex":
            print("ega0-1-fr.tex markers", m_n, "blank before", b_n, "next line lowercase", low_n)
print("all files", len(seen), "markers", tot_m, "blank before", tot_b, "next line lowercase", tot_low)
