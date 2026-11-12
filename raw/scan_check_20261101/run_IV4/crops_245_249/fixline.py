p = r"user\Documents\ega_scan_check_20261101\run_IV4\crops_245_249\build_findings.py"
s = open(p, "rb").read()
bad = b'.read().replace("\r\n", "\r\n")'
good = b'.read().replace("\\r\\n", "\\n")'
assert s.count(bad) == 1
s = s.replace(bad, good)
s = s.replace(b"\r\n", b"\n")
open(p, "wb").write(s)
print("ok")
