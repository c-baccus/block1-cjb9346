# Block 2 — Meet the data

- `data/gaia_physics1.csv` — Gaia DR3 stars with a radial velocity and `random_index < 2,400,000` (16 columns).
- `block2/` — download script, exploration, column guide, numbers, plots, and the prompt log (`block2/prompts.md`).
- Run scripts from the repo root with the project venv, e.g. `.venv/bin/python block2/numbers.py`.

**Row-count note.** The handout expects 40,961 rows. The archive's own `COUNT(*)` for this query is
44,810, and a single 16-column download returns ~40,961 rows but a *different* set of stars each
run (it is truncated). `block2/get_data.py` downloads in chunks, each verified against the archive's
count, giving 44,810 rows. To be confirmed with the instructor.
