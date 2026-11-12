import sys
RUN = r"user/Documents/ega_scan_check_20261101/run_IV4"
sys.stdout.reconfigure(encoding="utf-8")
for p in [200, 201, 202, 203, 204]:
    t = open(RUN + "/page_%03d.tex" % p, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    print(p, "START", repr(t[:120]))
    print(p, "END  ", repr(t[-160:]))
    print()
