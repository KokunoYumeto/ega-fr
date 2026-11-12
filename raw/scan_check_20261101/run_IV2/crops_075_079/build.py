"""Write findings_075_079.json from findings_a.py (+ findings_b.py if present) and check every fix's 'old'.

Check: per page, the fixes are applied in listed order to the page text (CRLF -> LF); each 'old' must occur
exactly once in the text at the moment it is applied. Also reports whether each 'old' occurs exactly once in
the original page text (fixes whose 'old' comes from the text after an earlier fix are listed separately)."""
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
OUT = RUN / "findings_075_079.json"

findings = []
for name in ("findings_a.py", "findings_b.py"):
    p = HERE / name
    if p.exists():
        spec = importlib.util.spec_from_file_location(name[:-3], p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        findings += mod.F

ok = True
pages = sorted({f["page"] for f in findings})
for pg in pages:
    orig = (RUN / f"page_{pg:03d}.tex").read_text(encoding="utf-8").replace("\r\n", "\n")
    cur = orig
    for i, f in enumerate(x for x in findings if x["page"] == pg):
        fx = f["fix"]
        if fx is None:
            continue
        old, new = fx["old"], fx["new"]
        n_cur = cur.count(old)
        n_orig = orig.count(old)
        if n_cur != 1:
            ok = False
            print(f"p.{pg} #{i}: 'old' occurs {n_cur} times at application: {old[:70]!r}")
        elif n_orig != 1:
            print(f"p.{pg} #{i}: 'old' taken from the text after earlier fixes (original count {n_orig}): {old[:70]!r}")
        cur = cur.replace(old, new, 1)

OUT.write_text(json.dumps(findings, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
cnt = {}
for f in findings:
    k = "misprint" if f["kind"] == "misprint_in_print" else ("convention" if f["kind"] == "convention" else "normal")
    cnt.setdefault(f["page"], {"normal": 0, "convention": 0, "misprint": 0})[k] += 1
print("written", OUT, len(findings), "findings; all 'old' unique at application:" , ok)
for pg in pages:
    print(pg, cnt[pg])
sys.exit(0 if ok else 1)
