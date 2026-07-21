---
name: kb
description: Search studio's knowledge base — every gear manual (pedals, plugins, Boss/Roland, monitors, controllers, DAWs) plus rig plans, setup notes, and song/lyric docs. Routes via a thin local index, then opens only the documents needed to answer.
---

# kb — studio knowledge base query

Answer questions from studio's local corpora using the shared retrieval engine in
[kb/](../../../kb/README.md): a thin file-based index the skill reads **first**,
opening individual documents only when detail is needed — no database, no
embeddings, no MCP. Same engine as the sibling `backoffice-pr`'s `/kb`.

**Stores** (see [kb/stores.yaml](../../../kb/stores.yaml)):

- `manuals` — every owned-gear manual: pedals, plugins, Boss/Roland, DAW/video,
  monitors, guitar-gear, loopers, controllers-interfaces.
- `docs` — rig plans, setup notes, song/lyric docs, music-format notes.

For a Logic-Pro-specific question, prefer the `logichelp` skill (it narrows to
the Logic guides and reads sections). Use `kb` for everything else or a repo-wide
search.

## Step 1 — Diagnostics (no query, or "status"/"index")

Show coverage and freshness:

```bash
uv run kb/index.py --status
```

If a store shows `(not built)` or looks stale, rebuild:

```bash
uv run kb/index.py
```

Report the table and stop.

## Step 2 — Query

```bash
uv run kb/query.py "<the question or key terms>" --limit 10 --json
```

Scope with `--store manuals` or `--store docs` when the intent is clear. Results
score against title / section **headings** / tags / path / snippet, so a term
routes into a large guide by its section headings — enough to pick documents
without opening them. If an obvious term returns nothing, the index may be stale:
run `uv run kb/index.py` once and retry.

## Step 3 — Answer

Open the top matching documents (Read tool, or `grep -n` for a heading then Read
that range for large files) only as needed. Cite each source as a clickable path.
Prefer snippets for routing; read full files for detail. If nothing matches the
question, say so plainly rather than guessing — the corpora are the source of
truth.

## Adding a store

Append a `name / kind / root / globs / exclude` block to
[kb/stores.yaml](../../../kb/stores.yaml) and rebuild. `root` may be relative to
the repo or absolute (e.g. pointing at the sibling `backoffice-pr` corpora).
