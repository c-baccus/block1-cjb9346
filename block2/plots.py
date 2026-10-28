"""Part 6 plots: parallax histogram and Galactic sky map, saved as PNGs in block2/.

Run from the repository root:  .venv/bin/python block2/plots.py
"""
import sys
from pathlib import Path

# block2/numbers.py (a required filename) shadows Python's built-in `numbers` module, which
# numpy imports. Drop this folder from the import path before importing numpy/pandas.
HERE = Path(__file__).resolve().parent
sys.path = [p for p in sys.path if Path(p or ".").resolve() != HERE]

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
df = pd.read_csv(ROOT / "data" / "gaia_physics1.csv")
plx = df["parallax"].dropna()
n_neg = (plx < 0).sum()

# 1. Parallax histogram: full range + zoom on -5..5 mas so negatives are clearly visible
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
ax1.hist(plx, bins=400, range=(plx.min(), plx.max()), color="tab:blue")
ax1.set_yscale("log")
ax1.set_title(f"All {len(plx):,} stars with a parallax (full range)")
ax2.hist(plx, bins=200, range=(-5, 5), color="tab:blue")
ax2.set_yscale("log")  # log scale so the few hundred negative parallaxes are not hidden
ax2.set_title(f"Zoom: -5 to 5 mas ({n_neg:,} stars have parallax < 0)")
for ax in (ax1, ax2):
    ax.axvline(0, color="red", lw=1, ls="--", label="parallax = 0")
    ax.set_xlabel("parallax [mas]")
    ax.set_ylabel("number of stars")
    ax.legend()
fig.suptitle(f"Gaia DR3 parallaxes, data/gaia_physics1.csv ({len(df):,} stars; {df['parallax'].isna().sum()} have no parallax)")
fig.tight_layout()
fig.savefig(ROOT / "block2" / "parallax_histogram.png", dpi=150)

# 2. Sky map in Galactic coordinates
fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(df["l"], df["b"], s=0.5, alpha=0.4, color="k", linewidths=0)
ax.set_xlim(0, 360)
ax.set_ylim(-90, 90)
ax.set_xticks(range(0, 361, 60))
ax.set_yticks(range(-90, 91, 30))
ax.set_xlabel("Galactic longitude l [deg]")
ax.set_ylabel("Galactic latitude b [deg]")
ax.set_title(f"Sky positions of all {len(df):,} stars in Galactic coordinates (l = 0: Galactic centre direction)")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(ROOT / "block2" / "sky_map_galactic.png", dpi=150)
print("saved block2/parallax_histogram.png and block2/sky_map_galactic.png")
