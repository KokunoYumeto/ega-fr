"""Independent check of findings_061_065.json: fields, unique olds, and sequential application per page."""
import json, pathlib
RUN = pathlib.Path(r"user\Documents\ega_scan_check_20261101\run_0III")
F = json.loads((RUN / "findings_061_065.json").read_text(encoding="utf-8"))
need = {"page", "where", "scan", "tex", "kind", "convention", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "italics", "missing", "extra", "number", "punctuation",
         "misprint_in_print", "convention", "marker", "other"}
problems = 0
texts = {}
for d in F:
    miss = need - set(d)
    if miss or d["kind"] not in kinds or (d["kind"] == "misprint_in_print" and "corrected" not in d):
        problems += 1
        print("FIELDS", d.get("page"), miss, d.get("kind"))
    if d["kind"] == "convention" and not d["convention"]:
        problems += 1
        print("CONV without number", d["page"], d["where"])
    p = d["page"]
    texts.setdefault(p, (RUN / f"page_{p:03d}.tex").read_text(encoding="utf-8"))
    if d["fix"] is not None:
        n = texts[p].count(d["fix"]["old"])
        if n != 1:
            problems += 1
            print("COUNT", p, n, d["where"])
# sequential application
for p, t in texts.items():
    cur = t
    for d in F:
        if d["page"] == p and d["fix"] is not None:
            if cur.count(d["fix"]["old"]) != 1:
                problems += 1
                print("SEQ", p, d["where"])
            cur = cur.replace(d["fix"]["old"], d["fix"]["new"], 1)
    # brace balance check after all fixes
    if cur.count("{") - cur.count("\\{") != cur.count("}") - cur.count("\\}"):
        print("BRACES differ after fixes on page", p,
              cur.count("{") - cur.count("}"), "vs original", t.count("{") - t.count("}"))
print("findings:", len(F), "problems:", problems)
