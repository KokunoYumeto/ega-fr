import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["mathtext.fontset"] = "stix"
fig = plt.figure(figsize=(8, 1.6), dpi=150)
fig.text(0.02, 0.25, r"$\mathfrak{J}\;\mathfrak{K}\;\mathfrak{L}\;\mathfrak{R}\;\mathfrak{K}_\alpha\subset\mathfrak{R}_\alpha$", fontsize=60)
fig.savefig(r"user\Documents\ega_scan_check_20261101\run_0IV1\crops_086_090\frak_ref2.png")
