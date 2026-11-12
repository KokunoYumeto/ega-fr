import sys
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
sys.stdout.reconfigure(encoding="utf-8")
p = int(sys.argv[1])
t = open(RUN + "/page_%03d.tex" % p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
for i, l in enumerate(t.split("\n")):
    print(i, repr(l))
