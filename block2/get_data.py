"""Download the Physics 1 Gaia DR3 sample and save it to data/gaia_physics1.csv.

Sample: gaiadr3.gaia_source stars that have a radial velocity and random_index < 2,400,000.
Handout says: 40,961 rows x 16 columns.

Why it downloads in chunks: asking the archive for all 16 columns in one synchronous query
silently returns only ~40,961 rows, and a *different* subset of stars on each run, while the
archive's own COUNT(*) for the same WHERE clause is 44,810 (and a 1-column query returns all
44,810). So the one-shot result is truncated. Here the sample is downloaded in random_index
chunks, and every chunk is checked against the archive's COUNT(*) before it is accepted.

Run from the repository root:  .venv/bin/python block2/get_data.py
"""
import io
import sys
from pathlib import Path

# block2/numbers.py (a required filename) shadows Python's built-in `numbers` module, which
# numpy imports. Drop this folder from the import path before importing numpy/pandas.
HERE = Path(__file__).resolve().parent
sys.path = [p for p in sys.path if Path(p or ".").resolve() != HERE]

import pandas as pd
import requests

TAP_SYNC = "https://gea.esac.esa.int/tap-server/tap/sync"  # ESA Gaia archive TAP service

COLUMNS = [
    "source_id", "ra", "dec", "l", "b",
    "parallax", "parallax_error",
    "pmra", "pmra_error", "pmdec", "pmdec_error",
    "radial_velocity", "radial_velocity_error",
    "phot_g_mean_mag", "bp_rp", "ruwe",
]

WHERE = "radial_velocity IS NOT NULL AND random_index >= {lo} AND random_index < {hi}"
QUERY = f"SELECT {', '.join(COLUMNS)} FROM gaiadr3.gaia_source WHERE {WHERE}"
COUNT = f"SELECT COUNT(*) AS n FROM gaiadr3.gaia_source WHERE {WHERE}"

RANDOM_INDEX_MAX = 2_400_000
CHUNK = 200_000  # ~3,700 stars per chunk, far below where truncation sets in

OUT = Path(__file__).resolve().parent.parent / "data" / "gaia_physics1.csv"
EXPECTED_ROWS = 40961


def run_query(adql):
    """Send an ADQL query straight to the Gaia TAP service and return a DataFrame.

    No TOP / MAXREC is set, so the result is not truncated at a row limit
    (astroquery's synchronous launch_job would cap it at 2,000 rows).
    """
    r = requests.post(
        TAP_SYNC,
        data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": adql},
        timeout=900,
    )
    r.raise_for_status()
    if r.text.lstrip().startswith("<"):  # TAP errors come back as VOTable XML
        raise RuntimeError(f"Gaia archive returned an error:\n{r.text[:2000]}")
    return pd.read_csv(io.StringIO(r.text))


def get_chunk(lo, hi, tries=3):
    expected = int(run_query(COUNT.format(lo=lo, hi=hi))["n"].iloc[0])
    for attempt in range(1, tries + 1):
        chunk = run_query(QUERY.format(lo=lo, hi=hi))
        if len(chunk) == expected and chunk["source_id"].is_unique:
            print(f"  random_index {lo:>9,}-{hi:>9,}: {len(chunk):,} rows (archive COUNT {expected:,}) OK")
            return chunk
        print(f"  random_index {lo:,}-{hi:,}: got {len(chunk):,}, expected {expected:,}; retry {attempt}")
    raise RuntimeError(f"chunk {lo}-{hi} never matched the archive count")


if __name__ == "__main__":
    print("Query per chunk:", QUERY)
    total = int(run_query(COUNT.format(lo=0, hi=RANDOM_INDEX_MAX))["n"].iloc[0])
    print(f"Archive COUNT(*) for the whole sample: {total:,}")

    chunks = [get_chunk(lo, min(lo + CHUNK, RANDOM_INDEX_MAX))
              for lo in range(0, RANDOM_INDEX_MAX, CHUNK)]
    table = pd.concat(chunks, ignore_index=True)[COLUMNS].sort_values("source_id")
    assert len(table) == total and table["source_id"].is_unique

    OUT.parent.mkdir(exist_ok=True)
    table.to_csv(OUT, index=False)

    print(f"Saved {len(table):,} rows x {table.shape[1]} columns to {OUT}")
    print(f"Unique source_id values: {table['source_id'].nunique():,}")
    if len(table) != EXPECTED_ROWS:
        print(f"NOTE: handout expects {EXPECTED_ROWS:,} rows; the archive's own count is {total:,}.")
