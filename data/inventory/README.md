# inventory/: structured studio data

The **query surface** for studio agents: what's here, its ports, and how it's wired. Theory is
in [docs/studio/model.md](../../docs/studio/model.md). The rules for deriving this data are in
[docs/studio/inventory.md](../../docs/studio/inventory.md); findings, the vendor glossary and open
questions are in [docs/studio/inventory-first-pass.md](../../docs/studio/inventory-first-pass.md).

| File | Holds |
|---|---|
| `ua-system.toml`, `monitoring.toml`, `sources.toml`, `software.toml` | **Units** with their **ports**, grouped by area of the studio |
| `connections.<rig>.toml` | **Connections** for one rig (`studio` for now): fixed cables, RF links, standing virtual routes |
| `scenarios.toml` | **Intents** (who listens, on what, hearing what) and Tim's **preferred realization** |

## Conventions

- **Ids:** lowercase slugs. A port is referenced as `unit:port` (`apollo-x8:line-out-3`).
- **Port labels** are the vendor's exact names (solution vocabulary), as read from the UA
  engine, I/O presets or the manual.
- **Ranges:** `{ id = "in-{n}", range = [1, 4] }` and `{ id = "monitor-{ch}", channels = ["L", "R"] }`
  expand to individual ports.
- **Unknowns:** `"?"`, or a value ending in `?`. `check` lists them.
- **`confidence`** on connections: `declared` (Tim) · `console-label` (from a Console input
  name) · `observed` (read from the machine) · `inferred`.
- **What doesn't go here:** per-session patches (which mic is in which snake channel) and
  mixer-internal routing (Console sends and mirrors). Those are live state or scenario
  state.

## Query

```bash
uv run scripts/inventory.py check              # validate; list open values
uv run scripts/inventory.py units [--kind K]
uv run scripts/inventory.py ports apollo-x8
uv run scripts/inventory.py trace psm300-pack  # follow signal; stops at mixers
uv run scripts/inventory.py find "OX"
uv run scripts/inventory.py scenarios
```
