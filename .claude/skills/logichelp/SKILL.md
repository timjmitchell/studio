---
name: logichelp
description: Answer Logic Pro questions using the converted manuals in docs/manuals/daw-video/. Routes with the kb index first, then reads only the relevant sections so the ~5MB guides stay out of main context.
---

# logichelp

Answer the user's Logic Pro question from the manuals at `docs/manuals/daw-video/`:

- `logic-pro-mac-user-guide.md` — main app (mixing, arranging, automation, etc.)
- `logic-pro-mac-instruments-user-guide.md` — software instruments (Sculpture, ES2, Drum Kit Designer, etc.)
- `logic-pro-mac-effects-user-guide.md` — effect plug-ins (Space Designer, ChromaVerb, amps, etc.)

The full guides are too large to load into main context. **Route with the kb
index first, then read only the sections you need.** This skill is the
Logic-scoped entry to the shared retrieval engine in [kb/](../../../kb/README.md);
for non-Logic gear or a repo-wide search, use the `kb` skill instead.

## What to do

1. **Get the question.** If the user passed args after `/logichelp`, that's the
   question. Otherwise ask what they want to know.

2. **Route with the index.** Run the query against the manuals store:

   ```bash
   uv run kb/query.py "<the user's question or key terms>" --store manuals --limit 8 --json
   ```

   Because the index scores against section **headings**, a term like
   "sidechain" or "Space Designer" routes straight to the guide that documents
   it. If the index is missing/stale (empty results for an obvious term, or a
   "No indexes" error), rebuild once with `uv run kb/index.py` and retry.

3. **Narrow to the Logic guide(s).** From the ranked hits, pick the
   `daw-video/logic-pro-mac-*.md` file(s) the question belongs to — effects vs
   instruments vs main guide. (Non-Logic hits like a Boss pedal or a plugin are
   the `kb` skill's territory; ignore them here unless the user's question
   genuinely spans them.)

4. **Read only the relevant sections.** For the chosen guide(s), locate the
   section — `grep -n` for the heading, then Read that line range — or, if the
   question spans several sections or files, spawn one Explore subagent per file
   with a self-contained prompt that:
   - Names the specific `docs/manuals/daw-video/logic-pro-mac-*.md` file to search
   - States the user's question verbatim
   - Asks for relevant **verbatim excerpts** (with `file:line` citations), the
     heading each excerpt sits under, and a one-line note on what it covers
   - Caps the response ("under 400 words, excerpts only — do not paraphrase")

5. **Synthesize the answer** from the excerpts, citing sections by heading or
   `file:line`. If the excerpts don't cover the question, say so plainly rather
   than guessing — the manuals are the source of truth here.

## Notes

- Don't preload manual content "just in case" — route with the index, then fetch
  only what the current question needs.
- Multi-manual questions (e.g. "route the ES2 through Space Designer") → one
  Explore subagent per guide, in parallel.
- The per-manual `INDEX.md` TOCs include original PDF page numbers — useful for
  cross-referencing the source PDF, but the `.md` files are primary.
