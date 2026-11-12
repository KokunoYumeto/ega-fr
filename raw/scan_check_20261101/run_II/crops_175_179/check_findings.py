import json

BASE = r"user/Documents/ega_scan_check_20261101/run_II"
t = open(BASE + "/findings_175_179.json", encoding="utf-8").read()
print("literal backslash-u sequences in file text:", t.count(chr(92) + chr(92) + "u0"))
d = json.loads(t)
print(len(d), "findings")
texts = {}
for p in (175, 176, 177, 178, 179):
    with open(f"{BASE}/page_{p}.tex", encoding="utf-8", newline="") as fh:
        texts[p] = fh.read().replace("\r\n", "\n")
for x in d:
    f = x["fix"]
    n = texts[x["page"]].count(f["old"]) if f else None
    for key in ("where", "scan", "tex", "note", "corrected"):
        v = x.get(key)
        if v and (chr(92) + "u0") in v:
            print("ESCAPE LEFT", x["page"], key, v[:80])
    print(x["page"], x["kind"], x["convention"], x["confidence"], "count=", n, "|",
          json.dumps(f, ensure_ascii=True)[:160] if f else None)
