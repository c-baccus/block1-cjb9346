"""First look at data/gaia_physics1.csv; writes block2/explore_output.txt.

Run from the repository root:  .venv/bin/python block2/explore.py
"""
import sys
from pathlib import Path

# block2/numbers.py (a required filename) shadows Python's built-in `numbers` module, which
# numpy imports. Drop this folder from the import path before importing numpy/pandas.
HERE = Path(__file__).resolve().parent
sys.path = [p for p in sys.path if Path(p or ".").resolve() != HERE]

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "gaia_physics1.csv"
OUT = ROOT / "block2" / "explore_output.txt"

df = pd.read_csv(DATA)

lines = [
    f"File: data/{DATA.name}",
    f"Number of stars (rows): {len(df):,}",
    f"Number of columns: {df.shape[1]}",
    "",
    "Columns:",
    *[f"  {c}" for c in df.columns],
    "",
    "Numerical columns (missing = empty entries in the file):",
    f"  {'column':<23}{'min':>22}{'median':>22}{'max':>22}{'missing':>9}",
]
for col in df.select_dtypes("number").columns:
    s = df[col]
    if col == "source_id":  # an ID: print as an integer, not in floating point
        stats = [f"{int(s.min())}", f"{int(s.median())}", f"{int(s.max())}"]
    else:
        stats = [f"{s.min():.6g}", f"{s.median():.6g}", f"{s.max():.6g}"]
    lines.append(f"  {col:<23}" + "".join(f"{v:>22}" for v in stats) + f"{s.isna().sum():>9}")

OUT.write_text("\n".join(lines) + "\n")
print("\n".join(lines))
