# Physics 1 AI project — standing instructions

## Prompt log (Block 2)
- Every prompt the user types is appended **verbatim** to `block2/prompts.md` automatically by the
  `UserPromptSubmit` hook in `.claude/settings.json` (script: `.claude/log_prompt.py`).
- At the end of every response, replace the `_(pending — agent fills this in)_` placeholder of the
  newest entry with a 1–2 line summary of what you did or answered, **and list the files created or changed**.
- Never edit, paraphrase, or delete the verbatim prompt text. Never skip an entry.
- If a prompt starts with `CHECK:`, the summary must state the result of the check (passed / found a mistake, and what was fixed).

## Layout
- `data/` — shared data (`data/gaia_physics1.csv`)
- `block2/` — this block's scripts, outputs, plots, and log
- Python: use the project venv, `.venv/bin/python`. Do not commit `.venv/`.
