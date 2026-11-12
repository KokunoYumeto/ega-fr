import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 2), dpi=150)
for fs, y in (("stix", 0.7), ("dejavuserif", 0.25)):
    plt.rcParams["mathtext.fontset"] = fs
    fig.text(0.02, y, r"%s: $\mathfrak{J}\ \mathfrak{K}\ \mathfrak{L}\ \mathfrak{R}\ \mathfrak{S}$" % fs, fontsize=28)
fig.savefig(r"user\Documents\ega_scan_check_20261101\run_0IV1\crops_086_090\frak_ref.png")
