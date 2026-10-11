# studio

This repo runs on Tim's studio Mac Studio. It's the working home for his music (projects,
songs, lyrics, charts, sessions) and the **agentic context** for the studio. Agents use it to
understand the gear, how it's wired, and how to act on it (Logic, UAD Console, MIDI gear),
and to help with workflows, automation and research. Tim works directly in these folders,
so keep the layout human-friendly.

## Where things live

| Path | What | Notes |
|---|---|---|
| `music/<project>/<song>/` | **Songs**: one folder per song, per project (`hot-fog`, `one-man-band`) | `<song>.md` is the song doc (frontmatter) and the **source of truth** for that song. See `music/README.md` |
| `docs/studio/` | **Studio docs**: [overview](docs/studio/overview.md) (one page: devices and routing), [model](docs/studio/model.md) (theory: concepts, vocabulary, entities, the cascade), [inventory](docs/studio/inventory.md) (rules for deriving the inventory), [first-pass notes](docs/studio/inventory-first-pass.md) (evidence, UA live snapshot, vendor glossary, open questions) | Start with the overview |
| `data/inventory/` | **Structured inventory** (TOML): units, ports, connections, scenarios | Query with `uv run scripts/inventory.py check / ports / trace / find / scenarios` |
| `data/manuals/` | **Manuals** for owned gear and software, converted to Markdown, plus hand-written `*-Field-Notes.md` | Registry: `data/manuals/sources.toml`. Mirrors: UAD Console, MIDI Guitar 3, music21 |
| `docs/research/` | Research notes, music-format investigation, named techniques, papers | |
| `kb/` | Retrieval index over `data/manuals`, `docs` and `music` | Rebuild: `uv run kb/index.py` |
| `scripts/` | Converters, fetchers, `sync_bounces.py`, `inventory.py`, `midi_dump.py` | Each has usage in its docstring |

**Outside the repo:** Logic projects live on `/Volumes/Samsung_X5/Hot Fog/` (check it's
mounted). Rehearsal recordings are on `/Volumes/RAID/`. Bounces are in Google Drive (`My
Drive/Hot Fog/New- 3rd Album/Bounces`).

## How to answer and act

- **Look things up, don't guess.** Use the `kb` skill for gear, manuals and songs, and
  `logichelp` for Logic Pro. Cite files as links. If the docs don't cover something, say so.
- **Studio questions** (what's connected, why there's no sound, what can do X): read
  `docs/studio/overview.md`, then query `data/inventory/`, then read **live state** (below).
  Live state beats saved state, and saved state beats notes.
- **Vocabulary:** store precisely, talk naturally. Use the reference terms in
  `docs/studio/model.md` §4 (e.g. *monitor mix*, *main mix*, *submix*) and keep vendor terms
  exact (UA *Cue*, Boss *Patch*). Tim says "monitor mix" for what UA calls a cue. Bare
  "monitor" means the main mix.
- **Unknowns stay unknown.** Mark them `?` and ask. Never fill in wiring, locations or models
  by guessing.

## Live studio surfaces

- **UA Mixer Engine** (UAD Console state): TCP `127.0.0.1:4710`, send `get <path>\0` and get
  JSON back. Paths: `/devices/N`, `/devices/N/inputs/M`, `/devices/N/outputs/M`. Device 0 is
  the Apollo x8, device 1 the Twin X.
- **Console files:** `~/Documents/Universal Audio/Sessions/*.uadmix` and `IOPresets/*.uadio`
  (XML).
- **Logic Pro:** AppleScript via System Events (the `applescript` MCP server); snippets are in
  the Logic Field Notes and the Arbitrary Overlord session notes.
- **Machine probes:** `system_profiler`, `ioreg` (vendor device names), CoreMIDI, plugin
  folders.

**Read-only by default.** Before any write (UA engine `set`, AppleScript that changes
Logic, MIDI to gear, moving files on the external drives): confirm with Tim, show a dry run,
read back the result, and keep the prior state so it can be undone.

## Conventions

- **Slugs** for folders and ids: lowercase-with-hyphens (`the-killing-moon`, `apollo-x8`).
- **Bounces:** `<song-folder>_<YYYY-MM-DD>_<tag>.mp3` in the Drive Bounces folder, then
  `uv run scripts/sync_bounces.py`.
- **Claim confidence** in notes: ✅ documented · 🔶 inferred · 🧪 tested (with date) · ❓ to
  test.
- **New manuals:** add the PDF and a `sources.toml` entry, then
  `uv run scripts/convert_manuals.py` and `uv run kb/index.py`. Online-only manuals get a
  fetch script (see `scripts/fetch_*`).
- **Adding gear:** follow the capture workflow in `docs/studio/inventory.md` §7, then run
  `uv run scripts/inventory.py check`.

## Toolchain preferences

- **Node.js**: managed via `nvm`. Don't install Node from Homebrew, the macOS installer, or `n`. If `node`/`npx` isn't on PATH, ensure nvm is sourced (`source ~/.nvm/nvm.sh`) before running.
- **Python**: managed via `uv`. Use `uv run`, `uv add`, `uv sync` — not `pip`, `pyenv`, or `poetry`.
- **Config files**: prefer TOML over JSON/YAML when authoring new config (e.g. `pyproject.toml` for Python projects).
