# kb/ — Knowledge Base index & query

The **retrieval layer** for studio's docs. Thin, file-based indexes over the
local Markdown corpora that the `kb` and `logichelp` skills read first, opening
individual documents only when they need detail. **No database, no embeddings,
no MCP** — just JSON.

```text
kb/stores.yaml   →   kb/index.py   →   kb/indexes/<store>.json   →   kb/query.py   →   skills
 (what to index)     (build)           (gitignored artifact)         (rank matches)   (logichelp, kb)
```

This is the same engine as [`backoffice-pr/kb/`](../../backoffice-pr/kb) — the
sibling checkout — so the two repos share one retrieval mechanism. studio adds
**heading indexing** (`index.py: collect_headings`) because its manuals include a
few very large concatenated guides (the ~5 MB Logic manuals); their section
headings are the routing surface, not a 280-char opening snippet.

## Stores

`kb/stores.yaml` declares each corpus — `name`, `kind`, `root`, `globs`,
`exclude`. Current stores:

| Store | Root | What |
| ----- | ---- | ---- |
| `manuals` | `docs/manuals/` | Every owned-gear manual (pedals, plugins, boss-roland, daw-video, monitors, guitar-gear, loopers, controllers) |
| `docs` | `docs/` (minus `manuals/`) | Rig plans, setup notes, song/lyric docs, music-format notes |

Add a store by appending to `stores.yaml` and rebuilding — no code change needed.
`root` may be relative to the repo, or absolute (e.g. to point at the sibling
`backoffice-pr` corpora — see the commented block in `stores.yaml`).

## Usage

```bash
uv run kb/index.py                    # build all indexes
uv run kb/index.py --store manuals    # build one store
uv run kb/index.py --list             # list configured stores
uv run kb/index.py --status           # index coverage / freshness

uv run kb/query.py "space designer reverb"           # search all stores
uv run kb/query.py "tap tempo delay" --store manuals  # one store
uv run kb/query.py "IEM routing" --limit 5 --json     # machine-readable
```

`query.py` ranks by keyword overlap against title / headings / tags / path /
snippet (weights favour title, then headings). It reads only the index JSON —
never the source files — so it's fast and safe to run anywhere.

## Rebuild when the corpus changes

`kb/indexes/*.json` is **gitignored and rebuildable** — run `kb/index.py` after
adding or converting a manual (e.g. via `scripts/convert_manuals.py`), adding a
song/doc, or editing `stores.yaml`. If a skill reports a matched file as
moved/missing, the index is stale — rebuild and retry.
