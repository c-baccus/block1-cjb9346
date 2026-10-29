# Block 2 prompt log

Prompts are recorded word for word. From the point the logging hook was set up
(`.claude/settings.json` → `.claude/log_prompt.py`), each prompt is appended automatically when
it is submitted; the agent then fills in the summary (standing instruction in `CLAUDE.md`).
The two prompts below were typed before the hook existed, so the agent copied them in by hand, verbatim.

## Prompt 1

**Prompt (verbatim):**

```text
cd claude projects/physics 1ai project
```

**Summary:** Agent located `~/Downloads/Claude Projects/Physics 1 AI project` (which holds the Block 2 handout as PDF and .md) and changed into it. Files: none.

## Prompt 2

**Prompt (verbatim):**

```text
read the 2 files in the folder. then do everything they ask. some of the steps are for people who have never coded pbefore so ignore the stuff about setting up antigravity and envirnments and stuff. then push to my github c-baccus, tell me when you need me to authenticate to sign you in
```

**Summary:** Agent read the handout (PDF + .md), chose the Block 1 repo `physics1-ai-project` (remote `c-baccus/physics1-ai-project`; SSH auth already works, no sign-in needed), and set up the prompt log (Part 0): a `UserPromptSubmit` hook that appends each prompt verbatim + standing instruction in `CLAUDE.md`. Made a venv (Python 3.13.5) with numpy, pandas, matplotlib, astroquery, requests and wrote `setup_output.txt`. For Part 2: the first astroquery async job failed (HTTP 500). A one-shot 16-column query returned 40,961 rows (the handout number), but the archive's own `COUNT(*)` gave 44,810. Agent investigated: two identical 16-column downloads gave **different** star sets (40,833 in common), all contained in the 44,810 set, and a 1-column query returned all 44,810 → the one-shot result is silently truncated. Rewrote `get_data.py` to download in 12 `random_index` chunks, each verified against the archive COUNT → 44,810 rows × 16 columns. Paused to ask the user which file to commit. Files: `CLAUDE.md`, `.claude/settings.json`, `.claude/log_prompt.py`, `.gitignore`, `block2/prompts.md`, `block2/setup_output.txt`, `block2/get_data.py`, `block2/explore.py`, `data/gaia_physics1.csv`.

## Prompt 3

**Prompt (verbatim):**

```text
hand on why are there 2 different numbers of stars? is this an error on the instructors part? explain the trunation
```

**Summary:** Agent explained the evidence: archive COUNT = 44,810; 1-column download = 44,810; one-shot 16-column download = 40,961 with different stars on each run, all a subset of the 44,810; chunked 16-column download verified against COUNT = 44,810. The dropped stars are ordinary, so this is a size-dependent server-side cutoff, not a selection. Most likely the handout's 40,961 came from the same truncated one-shot query, but that can't be proven without the instructor; suggested asking them and turning it into a CHECK: prompt. Files: none.

## Prompt 4

**Prompt (verbatim):**

```text
ok use the 44810 for now, ill ask. tell me what else youve done
```

**Summary:** Agent kept the verified 44,810-star file. Reran `explore.py` (44,810 rows; 226 stars lack parallax/proper motion/ruwe, 122 lack bp_rp, 3 lack G), and recounted rows and empty fields with plain Python `csv` (no pandas), which matched exactly. Wrote `columns.md`: units and official descriptions from the archive's `TAP_SCHEMA`, links to the official DR3 `gaia_source` data-model page (the docs site returned HTTP 503, so the links are not yet click-checked), and a lecture-connection table for parallax, pmra, pmdec and radial_velocity. Wrote `numbers.py`: nearest star 13.233 pc = 43.16 ly; median parallax 0.6849 mas → 1460 pc; best-parallax star μ = 313.24 mas/yr, v_t = 19.65 km/s vs v_r = 11.17 km/s; 466 negative, 226 missing, 966 with parallax < error; plus an explanation of why d = 1/parallax fails. Re-derived v_t in SI units (agrees: 19.65 km/s); the SIMBAD outside-source check failed because the service was unreachable. Found and fixed a bug: the required name `numbers.py` shadows Python's built-in `numbers` module and broke numpy imports, so an import-path guard was added to every block2 script. Made both plots; looked at them and changed the zoom panel to log scale because the negative parallaxes were invisible on a linear axis. Committed and pushed to GitHub, then confirmed every file is on the remote. Files: `block2/explore.py`, `block2/explore_output.txt`, `block2/columns.md`, `block2/numbers.py`, `block2/numbers_output.txt`, `block2/plots.py`, `block2/parallax_histogram.png`, `block2/sky_map_galactic.png`, `block2/get_data.py`, `block2/README.md`, `block2/prompts.md`.

## Prompt 5

**Prompt (verbatim):**

```text
count the stars matching the Gaia query directly on the archive with COUNT(*) and compare it to the number of rows in data/gaia_physics1.csv
```

**Summary:** Check on the data download (Part 2). **Passed.** Archive `SELECT COUNT(*) ... WHERE radial_velocity IS NOT NULL AND random_index < 2400000` = 44,810; the file has 44,810 rows (by `wc -l` minus the header, and by pandas), all `source_id`s unique, no empty `radial_velocity`. Because a matching count alone doesn't prove the stars are the same, the agent also downloaded a separate 1-column `source_id` list from the archive: all 44,810 IDs match the file exactly (0 extra, 0 missing). The `random_index` cut can't be checked from the file itself because that column isn't included. (This prompt was typed without the `CHECK:` prefix.) Files: `block2/prompts.md`.

## Prompt 6

**Prompt (verbatim):**

```text
 count the missing values in each column a different way, without pandas, and compare to explore_output.txt
```

**Summary:** Check on Part 3 (explore output). **Passed.** Recounted empty entries in all 16 columns two independent ways, without pandas: Python's built-in `csv` module and `awk` on the raw text. Both match `explore_output.txt` exactly (0 for source_id, ra, dec, l, b, radial_velocity, radial_velocity_error; 226 for parallax, parallax_error, pmra, pmra_error, pmdec, pmdec_error, ruwe; 3 for phot_g_mean_mag; 122 for bp_rp), and the `csv` row count is 44,810. Sanity check: the 226 stars missing parallax/proper motion/ruwe are the *same* 226 stars in all 7 columns, as expected for stars where Gaia only measured a position. (Typed without the `CHECK:` prefix.) Files: `block2/prompts.md`.

## Prompt 7

**Prompt (verbatim):**

```text
open the Gaia DR3 gaia_source documentation and confirm every link, unit and the ruwe and bp_rp descriptions in columns.md
```

**Summary:** Check on Part 4 (`columns.md`). **Partly passed; the link could not be confirmed.** The official documentation page still returns HTTP 503 (the whole `/archive/documentation/GDR3/` section is down; the archive itself and ESA's Gaia site are up), so the agent checked against other official sources instead. **Units:** all 16 match the archive's own column metadata (compared line by line). **bp_rp:** recomputed `phot_bp_mean_mag − phot_rp_mean_mag` from the archive for 3,746 of our stars, which agrees with `bp_rp` to 1.2e-6 mag, and it is empty exactly when BP or RP is missing. **ruwe:** confirmed against Lindegren et al. 2021 (Gaia EDR3 astrometric solution, Sections 5.1 and 5.3): RUWE ≈ 1.0 for well-behaved sources, it measures deviations from the single-star model (e.g. binaries), and it is not given for 2-parameter solutions (which explains our 226 missing values); our median of 1.019 matches the paper's Table 4. Correction: the paper does not contain the 1.4 cut (that comes from the DR2 technical note, which returned 403), so the ruwe description was reworded to say what the paper supports. Also confirmed: pmra = μα cos δ and the 2016.0 epoch. **Link:** a real ESA URL inside the official data-model section, but not opened live; recheck later. Not verified: G-band wavelength range, Vega system, RV sign convention. Added a Verification section to `columns.md`. (Typed without the `CHECK:` prefix.) Files: `block2/columns.md`, `block2/prompts.md`.

## Prompt 8

**Prompt (verbatim):**

```text
 recompute the nearest star's distance and the tangential velocity by hand in SI units, and look up the nearest star in SIMBAD to compare its distance
```

**Summary:** Check on Part 5 (`numbers_output.txt`). **Passed.** Picked the nearest star again directly from the CSV (plain `csv` module): the same star, Gaia DR3 1605198298364601088. Recomputed in SI units with IAU constants: p = 75.5689 mas = 3.6637e-7 rad; d = 1 AU / tan(p) = 4.0833e17 m = 13.2330 pc = 43.160 ly; μ = 313.240 mas/yr = 4.8123e-14 rad/s; v_t = μ·d = 19,649.7 m/s = 19.650 km/s; total speed with v_r = 11.17 km/s is 22.60 km/s. All match `numbers_output.txt`. **SIMBAD was unreachable** (connection refused from both the terminal and web fetch), so as the outside source the agent used the **Hipparcos** catalogue (an independent 1990s satellite, hosted in the Gaia archive): the star is HIP 71181 (position match 0.001″), Hipparcos parallax 75.65 ± 0.42 mas → 13.22 pc = 43.11 ly. That differs from Gaia's 75.569 ± 0.015 mas by only 0.08 mas (0.2σ). Physical sense check: the absolute magnitude of about 6.8 with B−V ≈ 1.0 fits a K-type main-sequence star, a normal neighbour at 13 pc. (Typed without the `CHECK:` prefix.) Files: `block2/prompts.md`.

## Prompt 9

**Prompt (verbatim):**

```text
. CHECK: count the stars matching the Gaia query directly on the archive with COUNT(*) and compare it to the number of rows in data/gaia_physics1.csv
```

**Summary:** CHECK on Part 2 (data download), re-run fresh against the live archive. **Passed.** Archive `COUNT(*)` = 44,810 and `COUNT(DISTINCT source_id)` = 44,810 for `radial_velocity IS NOT NULL AND random_index < 2400000`. The file has 44,810 rows (by `wc -l` minus the header and by Python's `csv` module), all unique. A freshly downloaded 1-column `source_id` list from the archive matches the file star for star (44,810 in both, 0 extra, 0 missing). The handout's 40,961 still disagrees with the archive; that question is open with the instructor. Files: `block2/prompts.md`.
