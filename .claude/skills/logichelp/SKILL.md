---
name: logichelp
description: Answer Logic Pro questions using the converted manuals in docs/manuals/. Delegates a search to an Explore subagent so the full guides (~5MB of markdown) stay out of main context.
---

# logichelp

Answer the user's Logic Pro question using the manuals at `docs/manuals/`:

- `logic-pro-mac-user-guide.md` — main app (mixing, arranging, automation, etc.)
- `logic-pro-mac-instruments-user-guide.md` — software instruments (Sculpture, ES2, Drum Kit Designer, etc.)
- `logic-pro-mac-effects-user-guide.md` — effect plug-ins (Space Designer, ChromaVerb, amps, etc.)
- `INDEX.md` — TOC for all three with page numbers from the source PDFs

The full guides are too large to load into main context. Always delegate the lookup.

## What to do

1. **Get the question.** If the user passed args after `/logichelp`, that's the question. Otherwise ask them what they want to know.

2. **Pick the likely manual(s)** from the question — effects vs instruments vs main guide. If unclear, search all three.

3. **Spawn an Explore subagent** with a self-contained prompt that:
   - Names the specific .md file(s) to search under `docs/manuals/`
   - States the user's question verbatim
   - Asks the agent to return: relevant verbatim excerpts (with `file:line` citations), section headings for context, and a one-line note on what the excerpt covers
   - Caps the response (e.g. "under 400 words, excerpts only — do not paraphrase or interpret")

4. **Synthesize the answer** from the excerpts. Cite sections by their markdown heading or `file:line`. If the excerpts don't cover the question, say so plainly rather than guessing — the manuals are the source of truth here.

## Example subagent prompt shape

> Search `docs/manuals/logic-pro-mac-effects-user-guide.md` for content about sidechain compression on the Compressor plug-in. Return verbatim excerpts (with file:line citations) plus the heading each excerpt sits under. Under 400 words. Do not paraphrase — I need the source text so I can answer the user accurately.

## Notes

- Don't preload manual content "just in case" — only fetch what the current question needs.
- If a question spans multiple manuals (e.g. "how do I route the ES2 through Space Designer?"), spawn one subagent per manual in parallel rather than one giant search.
- The INDEX.md TOC entries include PDF page numbers — useful if the user wants to cross-reference the original PDF, but the .md files are the primary source.
