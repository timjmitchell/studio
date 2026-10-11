# Studio Inventory: rules

> **How the studio inventory is derived, and what it does.** Every rule comes with the real
> example from the first pass (2026-10-11) that taught it.
>
> | Doc | Role |
> |---|---|
> | **This doc** | Rules: sources, derivation, conventions, what goes where, queries, execution |
> | [inventory/](../../data/inventory/README.md) | The structured data (TOML): units, ports, connections, scenarios |
> | [studio-overview.md](overview.md) | One-page human summary |
> | [inventory-first-pass.md](inventory-first-pass.md) | Evidence and working notes: findings, live UA snapshot, vendor glossary, parking lot, open questions |
> | [studio-model.md](model.md) | Theory: concepts, principles, entities, the cascade |

## 1. What the inventory is for

The inventory is the **query surface** for studio agents. It is the part of the
[cascade](model.md#the-core-idea-cascading-semantic-input-into-execution) that turns
an intent ("route the in-ears") into a realization on *this* studio. It answers:

- **What's here?** Units, their status, what they are and do.
- **How do they connect?** Ports, cables, wireless links, standing virtual routes.
- **How does Tim like to use them?** Scenarios: an intent plus the preferred realization.
- **How can an agent read or act on them?** Execution surfaces.

It doesn't store what the machine can report live, such as fader levels or which mix feeds an
output. It records **how to read** those things.

## 2. What goes where

| Kind of fact | Home | Example |
|---|---|---|
| Units and their ports | `inventory/<area>.toml` | `apollo-x8` with `line-out-{n}` 1–8, `monitor-L/R` |
| Fixed connections (cables, RF links, standing virtual routes) | `inventory/connections.<rig>.toml` | `apollo-x8:monitor-L → hr824-pair:in-L` |
| Intents and preferred realizations | `inventory/scenarios.toml` | `wedge-vocal-ideas`: CUE 3, mono, mirrored to Line 3-4 |
| **Per-session patches** | scenario or session state, *not* connections | which mic is plugged into which snake channel |
| **Mixer-internal routing** (sends, monitor mixes, mirrors, faders) | **live state**, read from the device on demand | x8 CUE 3 `OutputDestination = Line 3-4` |
| Vendor terms (solution vocabulary) | glossary, with a manual citation | UA *Cue*, *Cue Mirror to* ([first pass §3.3](inventory-first-pass.md#33-monitor-mixes-on-the-ua-system)) |
| Generic terms (reference vocabulary) | [model §4](model.md) | monitor mix, main mix, submix |
| Gear with no manual | Parking lot | Apollo x8 hardware manual (high priority) |
| Human summary | [studio-overview.md](overview.md) | "UAD Console is the hub…" |

## 3. Sources and confidence

Every fact carries its source:

| Tag | Source | Repeatable? |
|---|---|---|
| 🏷 | **Probe**: read off the machine (`system_profiler`, `ioreg`, CoreMIDI, plugin folders, `Info.plist`, `df`, the UA engine, Console files) | Yes, by script |
| 📘 | **Manual**: `data/manuals/` | Yes |
| 📄 | **Repo note**: field notes, rig plan, song docs | Yes |
| 🔎 | **Lookup**: vendor site or web | Mostly |
| 👤 | **Tim**: only he knows | No |
| ❓ | Open: needs an answer | |

Connections in TOML use `confidence`:
- `observed`: read from the machine;
- `declared`: Tim said so;
- `console-label`: from an input name Tim set in Console;
- `inferred`.

## 4. Depth: go only as deep as a workflow needs

| Level | Means | Example |
|---|---|---|
| **L0** exists | we know it's there | Akai MPK249 (manual only, not connected) |
| **L1** identity | vendor, model, version | Apollo x8 **HEXA**, fw 29.3 |
| **L2** connected | ports, wiring, place | x8 MONITOR L/R → HR824s |
| **L3** state | parameters, presets, live settings | CUE 3: own mix, mono, mirrored to Line 3-4 |
| **L4** emulation | what it models | UAD 1176 Rev A → UA 1176 "blue stripe" |

**Rule:** don't fill a level until a workflow needs it. L3 has been captured for only three
devices (VE-500, MIDI Guitar 3, UA Console), because those had real questions behind them.

## 5. Derivation rules

**R1. Probe first; generate, don't hand-write.** Anything the machine reports should come
from a script, not a hand-kept list.
> *Example:* 380 AU, 144 VST3 and 58 VST2 plugins, with versions, came from the plugin
> folders. A hand-written list would be stale within weeks.

**R2. Prefer the vendor's own source over generic probes.**
> *Example:* `system_profiler` listed the x8 only as "Thunderbolt 3 Option Card". The UA
> driver (`ioreg`) and the UA Mixer Engine named all three units exactly: Apollo x8 HEXA,
> Twin X QUAD, Satellite QUAD.

**R3. Live state beats saved state, and saved state beats notes.** Notes are dated
observations, never the source of truth for current settings.
> *Example:* the MIDI Guitar 3 field notes said version 3.0.55 was installed, but the app is
> now 3.0.74. They also said "guitar on x8 input 4", but the live Console names that input
> "A4 Mic" and has the guitar DI on Twin X input 2.

**R4. Manuals are the catalogue of owned hardware, and they define vendor terms.** Most gear
isn't on USB, so a manual in `data/manuals/` is the strongest sign it's owned. Its terms
enter the glossary with a citation.
> *Example:* the GM-800, TD-17 and the pedals are known only from their manuals. UA's *Cue*,
> *MIX* and *Cue Mirror to* are defined by the Console manual's Cues article.

**R5. Tim's labels are declarations.** Names Tim sets in software (Console input names, track
names) count as declared wiring. Keep them in a fixed form.
> *Example:* the Console inputs "A5 OX 1", "B1 PdlBrd" and "B2 Guit Dir" became connections
> with `confidence = "console-label"`. Convention: `A#` / `B#` plus the source.

**R5a. Labels can go stale, so check what the system says when you can.** A track or channel
name is only as current as the last time Tim renamed it. Before relying on a label, compare
it with what the system reports: live signal on the input meter, the current routing, a
snapshot. A mismatch is **drift**: record it, and suggest renaming.
> *Example:* Twin X input 2 was still labelled "B2 Guit Dir", but Tim had moved the clean
> guitar to x8 input 4 (labelled "A4 Mic"). Both labels were wrong. The fix is to rename them
> to "A4 Guit DI" (and clear B2). The snapshot plus inventory can catch this automatically
> (roadmap: drift check).

**R6. Only Tim knows physical wiring, places, status and gear with no electronics.** Ask in
batches, and record the answers as `declared`.
> *Example:* "HR824s on x8 MONITOR L/R", "headphones in the Twin X HP", "PSM300 on x8 7/8",
> "snake tails into x8 1–4".

**R7. Cross-check sources. A conflict becomes a finding, not an overwrite.**
> *Examples:* the probe saw a Twin X while the notes said x8, and both were right. The live
> rig plan names a VG-800 and MOTU M4 that appear in no manual and no probe, so their status
> is open.

**R8. Fixed, per-session or live: put each fact at the right layer.**
- Cables, RF links and standing virtual routes are **connections**.
- What changes every session (which mic is in snake channel 1) is **scenario state**.
- What a mixer does internally is **live state**.
> *Example:* `trace psm300-pack` follows the cables back to x8 outputs 7/8, then stops with
> "mixed inside apollo-x8: check its live routing state". Cables can't say which monitor mix
> feeds the in-ears; the UA engine can.

**R9. Port labels are the vendor's exact names; ids are slugs.**
> *Example:* label `MONITOR L`, id `monitor-L`, referenced as `apollo-x8:monitor-L`. Labels
> come from the UA engine, the I/O presets or the manual.

**R10. Unknowns are explicit, never guessed.** Use `"?"` (or a value ending in `?`).
`check` lists them.
> *Example:* the overview's first draft placed the x8, drives and monitors "behind the desk".
> Nobody had said that, so it was corrected to "not documented yet", and `hr824-pair.place`
> became `"?"`.

**R11. Vocabulary follows the two layers.**
- Vendor terms are exact and need a manual citation.
- Reference terms are chosen with Tim; industry usage is evidence, not the rule.
> *Example:* UA's *Cue* stays as the vendor term. The reference term is **monitor mix**,
> because that's Tim's word. "Playback submix" was rejected because nobody says it.

**R12. Record intents and preferred realizations, not every possible route.** The gear can
realize a monitor mix many ways. The agent derives the options and records only Tim's
preferred one per scenario.
> *Example:* five scenarios in `scenarios.toml`. The in-ears scenario is marked
> `not-routed`, because no monitor mix mirrors to Line 7-8 right now.

**R13. No manual → parking lot, with a priority.** Mirror the manual when it's online.
*Exempt:* guitar amps and simple passive gear Tim marks as needing none, e.g. the SM58
(Tim, 2026-10-11). Record their wiring and status, not documentation. In TOML, write
`manual = "none-needed"`.
> *Example:* the UAD Console manual came off the parking lot when
> `scripts/fetch_uad_console_docs.py` mirrored all 39 help-center articles through the
> Zendesk API. The Apollo x8 and Twin X *hardware* manuals are still high priority.

**R14. Read-only by default.** Probing never changes anything. Writes go through the
execution safety rails (§8).
> *Example:* the Console databases were copied to the scratchpad before inspection, and the
> UA engine was only sent `get` commands.

**R15. Be gentle with live surfaces.** Use one connection, throttle the queries, and never
send bursts. Live services can be fragile in ways a file isn't.
> *Example:* the first `ua_snapshot.py` run opened a new connection for every query
> (hundreds in seconds). The UA Mixer Engine crashed in its connection handler
> (2026-10-11 14:42), taking Console down until Tim relaunched it. The script now reuses one
> connection, and runs only with Tim's go-ahead.

## 6. Fill methods: what each source can and can't tell us

| Detail | Best method | Automatic? | Depth |
|---|---|---|---|
| Computer, OS, RAM | `system_profiler SPHardwareDataType` | ✅ | complete |
| Thunderbolt / USB devices, firmware, topology | `system_profiler SPThunderboltDataType SPUSBDataType` | ✅ | L1 + the chain to the Mac |
| Exact model of vendor hardware | vendor driver names in `ioreg` | ✅ | L1 (see R2) |
| Audio devices, channels, sample rates | `system_profiler SPAudioDataType` | ✅ | L1; not what's plugged in |
| **UA live state**: device roles, input names, outputs, monitor mixes, mirrors, monitor section, correction profiles | **UA Mixer Engine**, TCP 127.0.0.1:4710, `get /devices/...` → JSON | ✅ | L2 (via labels) + L3. The best single source for studio I/O |
| UA session history: names, Unison preamps, inserts, sends | `~/Documents/Universal Audio/Sessions/*.uadmix` (XML) | ✅ | L2–L3 per saved session |
| UA port lists per device model | `~/Documents/Universal Audio/IOPresets/*.uadio` (XML) | ✅ | L2 |
| MIDI endpoints | CoreMIDI (`mido`) | ✅ | names only; not DIN wiring |
| Volumes, capacity | `df` | ✅ | complete |
| Apps and plugins, with versions | `/Applications`, plugin folders, `Info.plist` | ✅ | complete |
| Emulation targets | plugin names (UAD, Arturia name the device) + UAD manual + 🔎 | partly | L4; revisions and years need lookup |
| Ports, parameters, MIDI maps | manuals 📘 | by search | L2 ports, L3 parameters |
| Device settings | editor apps, preset files, app prefs, Logic via AppleScript | partly | L3; one reader per vendor |
| Unconnected hardware, ownership | manuals (strong hint) + 👤 | ❌ | L0 |
| Physical wiring, places, cables | 👤 (photos would help) | ❌ | L2 physical |
| Guitars, mics, speakers, headphones | 👤, plus clues (UA correction profiles named the HR824 and MDR-7506) | ❌ | L0–L1 |

## 7. Capture workflow: adding or changing gear

1. **Probe** (R1, R2): is it visible to the machine? Take the model, firmware and port names
   from the vendor's driver or software.
2. **Manual** (R4, R13): is it in `data/manuals/`? If not, add it to the parking lot, or
   mirror the manual.
3. **Unit**: add it to the right `inventory/<area>.toml`, with ports using the vendor's
   labels and ranges (R9). Mark unknowns `"?"` (R10).
4. **Connections**: add fixed links to `connections.<rig>.toml`, with `medium` (`physical`,
   `virtual`, `rf`), any `via` (passive gear such as a snake), and `confidence` (R5, R6).
5. **Scenarios**: if it changes how Tim works, add or update the intent and preferred
   realization (R12).
6. **Validate**: `uv run scripts/inventory.py check`. Fix errors; open values are allowed.
7. **Summary**: if it changes the big picture, update [studio-overview.md](overview.md).

## 8. What the inventory does

### Queries

```bash
uv run scripts/inventory.py check              # validate refs and port use; list open values
uv run scripts/inventory.py units [--kind K]   # what's here
uv run scripts/inventory.py ports apollo-x8    # a unit's ports and what's on each
uv run scripts/inventory.py trace psm300-pack  # follow signal up and downstream; stops at mixers
uv run scripts/inventory.py find "OX"          # search ids, names, labels, notes
uv run scripts/inventory.py scenarios          # intents and preferred realizations
```

`check` enforces:
- every endpoint exists;
- a connection runs from an output to an input;
- one physical source per input, and one cable per output (**ports have one owner**).

### Execution surfaces

The ways an agent can *act on* the studio: the bottom stage of the cascade.

| Surface | Reaches | Read | Write | Notes |
|---|---|---|---|---|
| **UA Mixer Engine**, TCP 127.0.0.1:4710, null-terminated `get <path>` → JSON | Console: devices, inputs, sends, monitor mixes, mirrors, monitor section | ✅ 2026-10-11 | ❓ `set` not tried | Paths: `/devices/N`, `/devices/N/inputs/M`, `/devices/N/outputs/M` |
| **Console files**: `Sessions/*.uadmix`, `IOPresets/*.uadio` (XML) | Saved Console configurations | ✅ | as files, then load in Console | 33 saved sessions |
| **Logic via AppleScript UI** | Control bar, transport, click, track list, project path | ✅ | ✅ click toggle (2026-10-06) | [Session notes](../../music/hot-fog/arbitrary-overlord/session-notes.md), [Logic Field Notes §4](../../data/manuals/daw-video/Logic-Pro-Field-Notes.md) |
| **MCU** over the Network DAW Control Session | DAW faders, track names, transport | ❓ | ❓ | Console has it set as an MCU surface; see [uad-midi-ai](../research/uad-midi-ai.md) |
| **MIDI PC / CC / SysEx** (VE-500, UM-ONE, Launchkey) | VE-500 patches and parameters; DIN gear | ❓ | ❓ | [VE-500 MIDI Implementation](../../data/manuals/boss-roland/Boss-VE-500-MIDI-Implementation.md) |
| **Files** | Repo records, format conversions | ✅ | ✅ | `scripts/` |

**Safety rails for any write:** confirm, dry run, read back, keep the prior State for
undo, and log an Event.

## 9. Roadmap

1. **Tim's answers** to the open questions ([first pass §13](inventory-first-pass.md#13-questions-for-you)),
   then L2 wiring for the rest of the studio: pedalboard, MIDI, controllers.
2. **Migrate the first-pass notes into `inventory/`**: remaining units, the vendor glossary
   (a solution-term TOML with sources), and the parking lot.
3. **Probe script** (`scripts/probe_studio.py`): generate the 🏷 data: devices, apps,
   plugins, and a UA engine snapshot.
4. **Live-state reader for the UA engine**, so `trace` can continue past the mixer into
   monitor mixes and mirrors. `scripts/ua_snapshot.py` exists, throttled; its first run is
   waiting for Tim's go-ahead.
4a. **Drift check:** compare each snapshot's Console input names (and signal present on the
   meters) with the inventory's connections, and list mismatches: stale labels, unlabelled
   inputs with signal, labelled inputs that are silent.
5. **Fix the stale notes**: the MIDI Guitar 3 version and input in its field notes.
6. **Make `sources.toml` the Product registry**: add mirrored HTML manuals and owned gear
   without manuals.
7. **Safe write test on the UA engine**, with Tim watching Console: `set` one harmless value,
   then restore it.
8. **First end-to-end cascade**: "route the in-ears". Resolve → preferred realization →
   dry run → set → read back → log.
9. **Music layer**: Projects, Works, Versions and Recordings from `music/hot-fog/` and
   `music/one-man-band/` (now one folder per song).
