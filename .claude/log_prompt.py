"""UserPromptSubmit hook: append the user's prompt, verbatim, to block2/prompts.md."""
import json
import os
import sys
from datetime import datetime

data = json.load(sys.stdin)
prompt = data.get("prompt", "")
root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
log = os.path.join(root, "block2", "prompts.md")

with open(log, "a") as f:
    f.write(f"\n## Prompt — {datetime.now():%Y-%m-%d %H:%M}\n\n")
    f.write("**Prompt (verbatim):**\n\n```text\n" + prompt + "\n```\n\n")
    f.write("**Summary:** _(pending — agent fills this in)_\n")
