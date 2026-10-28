"""Some numbers about the stars in data/gaia_physics1.csv; writes block2/numbers_output.txt.

Units in the file: parallax in mas (milliarcseconds), proper motions in mas/yr,
radial_velocity in km/s.

Run from the repository root:  .venv/bin/python block2/numbers.py
"""
import sys
from pathlib import Path

# This file is named numbers.py (required by the assignment), which shadows Python's built-in
# `numbers` module that numpy imports. Drop this folder from the import path before importing numpy.
HERE = Path(__file__).resolve().parent
sys.path = [p for p in sys.path if Path(p or ".").resolve() != HERE]

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gaia_physics1.csv"
OUT = ROOT / "block2" / "numbers_output.txt"

LY_PER_PC = 3.26156  # light-years in one parsec
K = 4.74047          # km/s per (1 arcsec/yr at 1 pc) = 1 AU/yr in km/s


def distance_pc(parallax_mas):
    """d [pc] = 1 / p [arcsec] = 1000 / p [mas]."""
    return 1000.0 / parallax_mas


df = pd.read_csv(DATA)
lines = [f"Numbers for data/{DATA.name} ({len(df):,} stars)", ""]

# 1. Nearest star = largest parallax
near = df.loc[df["parallax"].idxmax()]
d = distance_pc(near["parallax"])
lines += [
    "1. Nearest star in the file (largest parallax)",
    f"   source_id      = {int(near['source_id'])}",
    f"   parallax       = {near['parallax']:.4f} +/- {near['parallax_error']:.4f} mas",
    f"   distance       = {d:.3f} pc = {d * LY_PER_PC:.2f} light-years",
    "",
]

# 2. Typical star = median parallax (stars with a parallax measured)
med = df["parallax"].median()
d = distance_pc(med)
lines += [
    "2. A typical star (median parallax)",
    f"   median parallax = {med:.4f} mas",
    f"   distance        = {d:.0f} pc = {d * LY_PER_PC:.0f} light-years (about {d / 1000:.2f} kpc)",
    "",
]

# 3. Speed across the sky for one star with a good parallax:
#    the most precise parallax (largest parallax / parallax_error) among stars with a good fit (ruwe < 1.4)
good = df[df["ruwe"] < 1.4]
star = good.loc[(good["parallax"] / good["parallax_error"]).idxmax()]
mu = np.hypot(star["pmra"], star["pmdec"])   # total proper motion, mas/yr
d = distance_pc(star["parallax"])
v_t = K * (mu / 1000.0) * d                  # mu in arcsec/yr times d in pc -> km/s
v = np.hypot(v_t, star["radial_velocity"])
lines += [
    "3. Speed across the sky (star with the most precise parallax, ruwe < 1.4)",
    f"   source_id        = {int(star['source_id'])}",
    f"   parallax         = {star['parallax']:.4f} +/- {star['parallax_error']:.4f} mas"
    f"  (parallax/error = {star['parallax'] / star['parallax_error']:.0f})",
    f"   distance         = {d:.2f} pc",
    f"   pmra, pmdec      = {star['pmra']:.3f}, {star['pmdec']:.3f} mas/yr",
    f"   total proper motion mu = sqrt(pmra^2 + pmdec^2) = {mu:.3f} mas/yr",
    f"   speed across the sky v_t = 4.74 * mu[arcsec/yr] * d[pc] = {v_t:.2f} km/s",
    f"   radial_velocity (along line of sight) = {star['radial_velocity']:.2f}"
    f" +/- {star['radial_velocity_error']:.2f} km/s",
    f"   total 3-D speed relative to the Sun = sqrt(v_t^2 + v_r^2) = {v:.2f} km/s",
    "",
]

# 4. The trouble with parallax
neg = (df["parallax"] < 0).sum()
missing = df["parallax"].isna().sum()
small = (df["parallax"] < df["parallax_error"]).sum()  # includes the negative ones
lines += [
    "4. The trouble with parallax",
    f"   stars with a negative parallax:                    {neg:,}",
    f"   stars with no parallax at all (empty):             {missing:,}",
    f"   stars with parallax smaller than parallax_error:   {small:,}"
    f"  (this includes all {neg:,} negative ones)",
    "",
]

lines += [
    "Why you can't just take distance = 1 / parallax for every star",
    "   A parallax is a measurement with an error, not an exact value. When the error is",
    "   comparable to the parallax itself, 1/parallax is very unreliable: noise can push a tiny",
    "   true parallax up (giving a distance that is far too small) or down to zero or below",
    "   (giving an infinite or negative 'distance', which is meaningless). Because 1/p is a",
    "   non-linear function, even unbiased errors in p give biased distances. Stars with no",
    "   parallax at all (Gaia only measured their position) have no distance from this method.",
    "   So 1/parallax is only trustworthy when parallax/parallax_error is large (roughly > 5-10);",
    "   for the rest you need a statistical approach that uses the uncertainty (e.g. a prior on",
    "   distance), or you leave those stars out.",
]

OUT.write_text("\n".join(lines) + "\n")
print("\n".join(lines))
