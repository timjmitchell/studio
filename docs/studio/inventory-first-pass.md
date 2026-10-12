# Inventory: first pass (2026-10-11)

> **Working notes and evidence** from the first inventory pass: findings, the live UA
> snapshot, the vendor glossary, Tim's monitoring practice, the parking lot and open
> questions. The **rules** for deriving the inventory are in
> [studio-inventory.md](inventory.md). The **structured data** is in
> [inventory/](../../data/inventory/README.md), and the **one-page summary** in
> [studio-overview.md](overview.md). Content here moves into `inventory/` as it's
> structured.

## How to read this

**Sources.** Every fact is tagged with where it came from:

| Tag | Source | Repeatable? |
|---|---|---|
| 🏷 | **Probe**: read off this Mac on 2026-10-11 (`system_profiler`, CoreMIDI, plugin folders, app `Info.plist`, `df`) | Yes, by script |
| 📘 | **Manual**: `data/manuals/` and [`sources.toml`](../../data/manuals/sources.toml) | Yes |
| 📄 | **Repo note**: field notes, rig plan, song docs | Yes |
| 🔎 | **Lookup**: vendor site or web | Mostly |
| 👤 | **Tim**: only you know (wiring, location, status, unconnected gear) | No |
| ❓ | Open: needs an answer (numbered **[I#]**, collected at the end) | |

**Depth levels.** How far each entity is filled in:

| Level | Means | Typical source |
|---|---|---|
| **L0** exists | we know it's there | 🏷 📘 👤 |
| **L1** identity | vendor, model, version or firmware | 🏷 📘 |
| **L2** connected | ports, what it's wired to, where it sits | 📘 for ports; 👤 for wiring |
| **L3** state | parameters, presets, current settings | 📘 for parameters; 🏷 / 👤 for state |
| **L4** emulation | what it models (company, device, revision, year) | names + 🔎 |

---

## 1. Findings from this pass

These came out of comparing the probe, the manuals and the repo notes.

1. **UA rig: Apollo x8 + Apollo Twin X + UAD-2 Satellite, in series over Thunderbolt.**
   *Resolved 2026-10-11.* 👤 One Console system: all inputs, outputs and DSP from all three
   units are available together. The Twin X acts as the **monitor controller** (main monitor
   level, switching between speakers and headphones).
   - The UA driver names all three units 🏷 (`ioreg`): **Apollo x8 – HEXA**, **Apollo Twin X –
     QUAD**, **UAD-2 Satellite TB3 – QUAD**.
   - `system_profiler` lists the x8 only as "Thunderbolt 3 Option Card" (its Thunderbolt
     module). **Lesson:** the generic probe can misname devices; the vendor driver is more
     reliable.
   - The [MIDI Guitar 3 field notes](../../data/manuals/plugins/MIDI-Guitar-3/MIDI-Guitar-3-Field-Notes.md)
     ("Apollo x8, input 4") were right.
2. **The MIDI Guitar 3 notes are out of date.** They say 3.0.55 is installed (observed
   2026-10-03). 🏷 3.0.74 is installed now, which matches the docs. The "version drift" section
   of the notes no longer applies.
3. **The LUNA manual is behind.** 📘 The manual is 2.0.1; 🏷 LUNA 3.0.0 is installed.
4. **The live rig plan names gear that appears nowhere else.** The VG-800, GK-5, NUX Optima
   Air, MOTU M4 and AbleSet have no manual and don't show up in the probe. They're probably
   `planned`. The GM-800 has manuals but isn't connected. **[I2]**
5. **UAD plugins come in two implementations.** 🏷 There are 224 `UAD …` AU plugins (DSP: run
   on the Apollo/Satellite chips) and about 68 `uaudio_…` plugins (UAD Native: run on the
   Mac's CPU). Several are the *same emulation* in both forms (1176 Rev A, LA-2A, Pultec, Neve
   1073…). This is the Studio Ontology's **implementation** layer, which the model skipped. →
   model change: an emulation can have several implementations, each with its own host.
6. **Sample rates differ.** 🏷 The Apollo runs at 48 kHz and the VE-500's USB audio at
   44.1 kHz. That matters only if they're combined in an aggregate device or used together in
   one session.
7. **The system drive is 86% full.** 🏷 65 GB free on the 460 GB internal SSD. Sessions live
   on Samsung_X5, so this is mostly a housekeeping note.
8. **Many software products have no manual.** Arturia (41 instruments), Kontakt, iZotope,
   Auto-Tune, FabFilter, AmpliTube, TONEX software. That's fine: for software, the probe
   plus a vendor lookup is usually enough. Manuals matter most for hardware. Everything
   without a manual is listed in the [Parking lot](#parking-lot-no-manual-yet).

---

## 2. Computer, storage and hubs

| Unit | Identity (L1) | Connected via (L2) | Source | Notes |
|---|---|---|---|---|
| **Mac Studio** | Mac13,1 (MJMV3LL/A), Apple M1 Max, 10-core, 32 GB, macOS 14.5 (23F79) | — | 🏷 | No manual in repo. Internal SSD 460 GB, 86% used |
| **OWC ThunderBay 4** | firmware 28.2 | Mac Thunderbolt bus 3 | 🏷 📘 | Volume `RAID`, 5.5 TB, 59% used. Managed by SoftRAID 8.6.1 🏷. Holds rehearsal recordings 📄 |
| **Anker PowerExpand Elite 12-in-1 TB4 Dock** | firmware 33.1 | daisy-chained from the ThunderBay | 🏷 📘 | Hosts the X5, a USB hub (Launchkey, generic USB audio/storage), and Ethernet |
| **Samsung Portable SSD X5** | firmware 35.1 | Thunderbolt via the Anker dock | 🏷 | Volume `Samsung_X5`, 1.8 TB, 35% used. **All Logic projects** 📄. No manual |
| **iLok** | USB key | Apple USB2 hub | 🏷 | iLok License Manager installed |
| Samsung **LC34G55T** display | DisplayPort; also a 2-ch audio output | | 🏷 | |
| LG display? | LG Calibration Studio + OnScreen Control installed | | 🏷 ❓ | **[I3]** |
| Cable Matters device | USB "billboard" (a USB-C alt-mode adapter) | | 🏷 ❓ | Probably a USB-C → DisplayPort adapter |
| Generic "USB Audio" (0x4ef0) and "USB Storage" | on the Anker hub | | 🏷 ❓ | Unknown devices **[I4]** |
| **Google Drive** | Drive for Desktop | | 📄 | Bounces folder used by [`sync_bounces.py`](../../scripts/sync_bounces.py) |
| **iCloud Drive** | | | 📄 | Mix copies (song docs), manual sources |
| OneDrive | installed | | 🏷 | Used for music? **[I5]** |

**Thunderbolt chain** 🏷:

```text
Mac Studio ─ bus 0 ─► Apollo x8 HEXA (TB module fw 29.3) ─► UAD-2 Satellite TB3 QUAD (fw 43.5) ─► Apollo Twin X QUAD (fw 18.6)
Mac Studio ─ bus 3 ─► OWC ThunderBay 4 (fw 28.2) ─► Anker TB4 Dock (fw 33.1) ─► Samsung X5 (fw 35.1)
Mac Studio ─ USB  ─► Apple hub ─► Roland UM-ONE, iLok
Anker dock ─ USB  ─► Launchkey Mini MK4 25, generic USB audio, generic USB storage, Ethernet
(unknown hub)     ─► BOSS VE-500
```

**Depth reached:** L1–L2, almost entirely automatic. The probe gives the full Thunderbolt and
USB topology and firmware.

---

## 3. Audio interfaces and Core Audio devices

| Unit / device | Identity | Channels / rate | Source | Notes |
|---|---|---|---|---|
| **Apollo x8** | Universal Audio, **HEXA** DSP; Thunderbolt module fw 29.3 | via Console | 🏷 (driver) 👤 | First in the chain from the Mac. Main interface: the guitar is on input 4 📄. No manual in repo **[I6]** |
| **UAD-2 Satellite TB3** | Universal Audio, **QUAD** DSP, fw 43.5 | DSP only | 🏷 👤 | Extra DSP for `UAD …` plugins |
| **Apollo Twin X** | Universal Audio, **QUAD** DSP, fw 18.6 | via Console | 🏷 👤 | **Monitor controller**: main monitor level, speakers ↔ headphones switching 👤. No manual in repo **[I6]** |
| *UA system total* | 3 units, one Console system | **14 SHARC DSP chips** (6 + 4 + 4) 🔶 | 🏷 | DSP budget for `UAD …` plugins and Unison preamps |
| Core Audio **"Universal Audio Thunderbolt"** | | **44 in / 42 out**, 48 kHz; system default in and out | 🏷 | Console's combined virtual I/O across all three units |
| Core Audio **"VE-500"** | BOSS, USB | 2 in / 2 out, 44.1 kHz | 🏷 📘 | VE-500 USB audio (field notes §1: USB bus skips OUTPUT EQ/MODE) |
| Core Audio **"Multi-Output Device"** | Apple aggregate | | 🏷 | What's in it? **[I7]** |
| Mac Studio Speakers | built-in | 2 out, 44.1 kHz | 🏷 | |
| IK **iRig HD X** | | | 📘 | Not connected. Still used? **[I2]** |

UA software 🏷: UAD Console 1.3.1 · UA Connect 1.11.0 · UA Midi Control 5.11.1 · UAD Meter &
Control Panel.

### 3.1 UA Console I/O: live snapshot (2026-10-11)

Read-only from the **UA Mixer Engine** (local port 4710, `get /devices/...`) 🏷. Console
**channel names are your own labels for what's plugged in**, so they work as a declared wiring
map that the agent can read.

**Monitoring path**

| Item | Value | Source |
|---|---|---|
| Studio monitors | **Mackie HR824** pair ← **Apollo x8 MONITOR L/R** | 👤 |
| Monitor controller | **Apollo Twin X**, `RemoteMonitorController: true` | 👤 + 🏷 ✓ |
| Speaker correction profile | "Mackie left mix – 2023-06-14" (stored on the x8; correction currently **off**) | 🏷 |
| Headphones | **Sony MDR-7506** ← **Twin X HP** output; headphone-correction profile "Sony MDR-7506 Wired Average" (off) | 👤 + 🏷 |
| Alt monitors | up to 2 supported; selection = 0 (main) | 🏷 |
| Dim | 17 dB; front-panel function switch = none | 🏷 |
| x8 MONITOR output right now | muted | 🏷 (state at time of read) |
| Twin X outputs | HP, LINE 3/4 (feed monitor mixes), MONITOR (muted) | 🏷 |
| Cue buses | 3 active per unit (CUE 1–3) | 🏷 |

**Inputs: current names**

| Unit | Input | Type | Live name | Meaning 🔶 |
|---|---|---|---|---|
| x8 | 1 | Mic | **A1 Mic Dyn** | dynamic mic (SM7 in many sessions) |
| x8 | 2 | Mic | **A2 Mic** | |
| x8 | 3 | Mic | **A3 Mic Cond.** | condenser (KX67 / Rode in some sessions) |
| x8 | 4 | Mic | **A4 Mic** | (fader down) |
| x8 | 5 | Line | **A5 OX 1** | OX Amp Top Box out 1 |
| x8 | 6 | Line | **A6 OX2** | OX Amp Top Box out 2 (pad on) |
| x8 | 7–8 | Line | A7, A8 | |
| Twin X | 1 | Line | **B1 PdlBrd** | pedalboard output |
| Twin X | 2 | Mic/Hi-Z | **B2 Guit Dir** | guitar direct (DI) |
| both | ADAT 1–8, S/PDIF | | unnamed | mostly muted / unused; Twin X optical set to S/PDIF |
| both | VIRTUAL 1–8 | | | software returns (V1, V3 active on the x8) |

**Naming history** (from 33 saved `.uadmix` sessions, 2023–2025 🏷). The physical inputs have
moved around. Recurring patterns:
- **x8 1–2:** SM7 / Vox, Pedalboard "O2", Bass, Tonex, Mod5.
- **x8 3–4:** Condenser / KX67 / Rode, plus "PB Dir" (pedalboard direct).
- **x8 5–6:** OX 1 / OX 2, every time.
- **Twin X 1–2:** SM7, line inputs, bass DI, drums.

The most-used Unison preamps were **Neve Preamp** (18) and **Manley VOXBOX** (10). The most-used
inserts were **Pure Plate** (15), **1176 Rev A** (11) and **RealVerb-Pro** (6).

> **Recommendation:** keep Console input names in a fixed `A#`/`B#` + source form (e.g.
> `A5 OX 1`, `B2 Guit Dir`). That makes them a reliable wiring declaration the agent can read
> live.

**Channel counts: three levels** (read from the engine 2026-10-11 22:05 🧪, 13 confirmed by Tim
in the Console UI). "How many channels" means a different thing at each layer:

| Layer | Count now | What it is | Engine source |
|---|---|---|---|
| **Driver routes** (I/O Matrix) | **44 in / 42 out** (36 / 34 active) | Core Audio channels Logic sees. Mode Default, no I/O preset loaded | `/` `TotalDriverInputRoutes` / `TotalDriverOutputRoutes`; `/inputroutes/N`, `/outputroutes/N` |
| **Mixer input slots** | **50** (x8 28, Twin X 22) | Every input the Console mixer could show, including talkback and `N/A` placeholders | `/devices/N/inputs/M` |
| **Visible channel strips** | **13** (x8 10, Twin X 3) | What Console shows | input slots where `Active` and not `ChannelHidden`, minus talkback |

- The 44 driver inputs are split as follows. x8 has 34: 8 analog, 8 ADAT, 2 S/PDIF, 8 virtual (5–8 inactive), MON L/R, AUX 1–2 L/R and talkback 1–2 (inactive). Twin X has 10: 2 analog, 4 virtual (3–4 inactive), 2 S/PDIF and talkback 1–2. MON, AUX and talkback appear only as driver inputs (for recording the mix), not as strips.
- The 42 driver outputs are split as follows. x8 has 36: MON L/R, LINE 1–8, 8 ADAT, 2 S/PDIF, 8 virtual (5–8 inactive) and CUE 1–4 L/R (CUE 4 inactive). Twin X has 6: MON L/R and 4 virtual (3–4 inactive).
- **A stereo pair is one strip.** The right side reports `Active = false` (e.g. VIRTUAL 2, VIRTUAL 4, S/PDIF R).
- **Hidden is not off.** x8 ADAT 1–8 and both units' S/PDIF L are `Active` but `ChannelHidden`, so they are hidden with Show/Hide Inputs. Hiding removes the strip and its meter-bridge meter ✅ ([Meter Bridge](../../data/manuals/controllers-interfaces/UAD-Console/03-meter-bridge.md)). 🔶 It probably doesn't stop audio, so a hidden input could still feed a mix. ❓ to test.
- **Talkback isn't a strip.** The Twin X TALKBACK slot is `Active` and not hidden, but Console doesn't show it as a channel.
- **What gets saved where** (from the files 🏷):
  - A **Console session** (`Sessions/*.uadmix`) saves each input's `kPropChannelHidden` and `kPropEnabledByUser` (the "selected" part), plus its name, fader, sends, plugins and cue mirrors.
  - Two root flags, `kPropHiddenChannelsInSession` and `kPropChannelNamesInSession` (both on in `Tracking.uadmix`), 🔶 decide whether hidden state and names load with the session or stay global.
  - An **I/O preset** (`IOPresets/*.uadio`) saves only the driver map: which hardware channel sits in each of the 44/42 driver slots, and their names (e.g. "UAD OX1").
  - Neither file holds the cue bus count or sample rate. Those are hardware settings.
- The virtual channel count is set per unit: x8 V1–4 (2 stereo strips: V1, V3), Twin X V1–2 (1 strip). Twin X VIRTUAL 5–8 also have `EnabledByUser = false`.

### 3.2 How the UA system is used (from Tim, 2026-10-11)

**What Console is.** UAD Console is a control surface for the UA devices. It closely emulates
the console of a traditional recording studio: preamps and inputs going *to tape*, and
monitoring of the signal coming *off tape*. Monitoring through Console bypasses the DAW, so
latency is very low. DAW outputs can be routed back into Console, which then acts as the
**monitor mix**, like the dedicated monitor-fader section on old consoles.

Two Console features matter most for routing:

- **Virtual channels.** Both the x8 and the Twin X have virtual inputs: stereo returns from
  the computer, each with its own Console fader.
- **Cue outputs.** These set up separate monitor mixes (UA: cues). For each one you choose how
  many there are, which device and outputs carry it, and whether it's the same audio as the
  main L/R monitor mix or its own mix.

**Virtual channel assignments**

| Console channel | Fed by | Purpose | Live check 🏷 |
|---|---|---|---|
| **Twin X VIRTUAL 1/2** | **Logic main output** | The DAW's mix gets its own fader, balanced against live inputs. Use the same pattern for **any DAW** (Ableton too). LUNA is a special case, to document later | Twin X VIRTUAL 1 active, fader −10.2 dB ✓ |
| **x8 VIRTUAL 1/2** | **macOS default output**, set in Audio MIDI Setup | System audio (YouTube in a browser, etc.) on its own fader | x8 VIRTUAL 1 active, −17.7 dB ✓ |
| **x8 VIRTUAL 3/4** | a DAW submix, on demand (e.g. drums) | A submix on its own Console fader, so monitor mixes can balance it separately (pattern C, §3.3) | x8 VIRTUAL 3 active, −14.1 dB ✓ |

**Physical I/O on the x8**

| x8 port | Connected to | Used for |
|---|---|---|
| **Inputs 1–4** (mic) | XLR tails of a **Gator Cableworks Backline 6-channel snake** | The main mic inputs. Mics plug in at the snake box on the floor, not behind the desk |
| **MONITOR L/R** | **Mackie HR824** pair | Main monitors (Twin X is the remote monitor controller) |
| **Output 3** | **Turbosound** powered floor monitor (~1000 W) | A wedge, fed by a **Console cue**: for rehearsing, or singing vocal ideas to a monitor instead of headphones |
| **Outputs 7/8** | **Shure PSM300** transmitter → wireless in-ears | IEMs, fed by a **Console cue**: for recording or rehearsing on in-ears |

**On the Twin X**

| Twin X port | Connected to |
|---|---|
| **HP** | Sony MDR-7506 |

### 3.3 Monitor mixes on the UA system

Terms: **monitor mix**, **main mix**, **submix**, **virtual channel** and the rest are
reference concepts defined in [model §4.7](model.md#47-starting-concepts-mixing-and-monitoring).
UA calls monitor mixes **cues**. Below are the UA-specific terms, rules, Tim's practice, and
the live configuration.

**How UA's cue system works** ✅
([Console manual: Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md)):

1. **Cue mix buses:** 2–4 stereo buses (the Twin X always has 2, labelled HP and LINE 3/4).
2. **Cue sends:** per channel level, pan and mute into each cue. They are **pre-fader and
   pre-mute**.
3. **Cue Outputs:** a matrix routing each cue to hardware outputs. The **MIX** switch makes an
   output carry the main mix instead of the cue bus (`MixInSource: mon` vs `cue`).
4. **Cue monitoring:** the main monitors can be switched to listen to any cue.

**Glossary: solution-layer terms** (exact, manual-grounded; mapped to the reference layer
per [model §4.1a](model.md#41a-two-layers-reference-and-solution-architecture)):

| Term | Product | Meaning there | Maps to (relation) | Source |
|---|---|---|---|---|
| **MONITOR** | UAD Console | Control-room outputs and their level / mute / dim | main mix (same) | [Monitor Column](../../data/manuals/controllers-interfaces/UAD-Console/22-monitor-column.md) |
| **Cue** (CUE 1–4) | UAD Console | A cue mix bus plus its output assignment; 2–4 per system | monitor mix (close: with MIX on, the output carries the main mix) | [Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md) |
| **HP**, **LINE 3/4** (cue names) | UAD Console, Apollo Twin | The Twin's two fixed cue buses | monitor mix (close) | [Hardware Settings](../../data/manuals/controllers-interfaces/UAD-Console/33-hardware-settings-panel.md) |
| **Cue Outputs** | UAD Console | Matrix routing cues to hardware outputs | monitor mix → output (implements) | [Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md) |
| **MIX** (switch) | UAD Console | Per cue output: main monitor mix (lit) or the cue bus (dim) | chooses main mix vs monitor mix | [Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md) |
| **MONO** (switch) | UAD Console | Per cue output: sums the cue to mono | mono sum (same, cue outputs only) | [Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md) |
| **Cue Mirror to** | UAD Console, rack models | Copies a cue to a line pair; that output is no longer available to the DAW | monitor mix delivery (implements) | [Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md) |
| **Digital Mirror** | Apollo / Console | Copies the monitor outputs to S/PDIF (AES on x16) | main mix (related) | [LUNA manual](../../data/manuals/plugins/LUNA-2.0.1-Manual.md#L10055) |
| **Virtual** (VIRTUAL 1–8) | UAD Console | Input strips fed from the computer's software outputs | virtual channel (same) | [Input Channel Strips](../../data/manuals/controllers-interfaces/UAD-Console/06-input-channel-strips.md) |
| **Aux** (AUX 1/2) | UAD Console | Two stereo aux buses; returns host plug-in inserts | submix (related: an effects return) | [Aux Returns](../../data/manuals/controllers-interfaces/UAD-Console/21-aux-returns.md) |
| **Flex Routing** | UAD Console, rack models | Input channel → any hardware output; not a mix bus | direct out (related) | [Output Flex Routing](../../data/manuals/controllers-interfaces/UAD-Console/19-output-flex-routing.md) |
| **ALT** (ALT 1/2) | UAD Console | Alt monitor outputs fixed to Line 1-2 / 3-4 | alt monitors (same) | [Hardware Settings](../../data/manuals/controllers-interfaces/UAD-Console/33-hardware-settings-panel.md) |
| **Summing Stack** | Logic Pro | Subtracks routed to a bus whose aux "functions as an audio subgroup" | submix (narrower) | [UG L6115](../../data/manuals/daw-video/logic-pro-mac-user-guide.md#L6115) |
| **Groups** | Logic Pro | Channel strips whose chosen parameters are "controlled for the entire group at once" | VCA group (close) | [UG L19865](../../data/manuals/daw-video/logic-pro-mac-user-guide.md#L19865) |
| **Group Track** | Ableton Live | "Serves as a submixer for the selected tracks" | submix (same) | [Live 12 L1567](../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L1567) |
| **Patch** | Boss VE-500 (and other Boss units) | A saved set of effect settings, selected by number | preset (same) | [VE-500 Owner's Manual: Patch Structure](../../data/manuals/boss-roland/Boss-VE-500-Owners-Manual.md) |

**Rules from the Console manual that matter here** ✅:
- **The MIX switch** sends the main monitor mix to an output; clearing it sends the
  independent monitor mix. **Either way, it's summed with any DAW outputs routed to the same
  output** ([Cues](../../data/manuals/controllers-interfaces/UAD-Console/18-cues.md)).
- **The MONO switch** affects only the cue's outputs. To hear a cue in mono on the main
  monitors, use the Monitor Mono switch instead.
- **"Cue Mirror to"** (Apollo rack models) copies a cue to a line pair. **A mirror overrides
  DAW outputs on the same hardware outputs.** While CUE 3 mirrors to x8 Line 3-4, the DAW
  can't use outputs 3-4. Flex Routing has the same rule
  ([Output Flex Routing](../../data/manuals/controllers-interfaces/UAD-Console/19-output-flex-routing.md)).
- **Cue Bus Count** is 2–4 on the x8 (set in Settings > Hardware). The Twin X always has 2
  (HP, LINE 3/4). Cues 3–4 are unavailable at 176.4 and 192 kHz
  ([Hardware Settings](../../data/manuals/controllers-interfaces/UAD-Console/33-hardware-settings-panel.md)).
- **ALT Count** of 1 takes Line 1-2, and 2 takes Line 1-4, overriding other assignments.
- **The cue / virtual channel trade-off** that Tim described: the manual frames it as driver
  I/O channel count. The I/O Matrix "Custom" modes allow "up to 4 CUE mixes, or … up to 8
  Virtual I/O channels" within the driver's channel budget
  ([I/O Matrix](../../data/manuals/controllers-interfaces/UAD-Console/34-i-o-matrix-settings-panel.md)).
  🔶 So the limit is driver I/O channels, not DSP.

> Don't confuse **Digital Mirror** with the cue mirror. Digital Mirror copies the *main
> monitor* outputs to S/PDIF ✅ ([LUNA manual](../../data/manuals/plugins/LUNA-2.0.1-Manual.md#L10055)).

**How Console does it** (from Tim):
- You choose **how many** monitor mixes you want. Monitor mixes and virtual channels **trade
  off** against each other. The manual frames this as the driver's I/O channel budget, not
  DSP (see the rules below). It isn't a constraint here, but unused outputs clutter Console,
  so **3 are active**.
- For each one you choose:
  - which device outputs it, and on which channels;
  - whether it follows the main mix or is independent;
  - stereo or mono.
- By default, monitor mixes go to the **front headphone jacks**, with an option to **mirror** to
  a rear line pair.
- Tim's wiring is all on the back, so he uses **mirrors to the rear outputs** rather than the
  x8's front headphone jacks. The front jacks are still handy for plugging in another pair of
  headphones with a different mix.

**How DAW playback gets into monitor mixes** (Tim). The DAW is usually involved, because it's
playing back the song while live inputs are monitored through Console at low latency. There
are three ways to combine them:

| Pattern | How | Good for |
|---|---|---|
| **A. Blend in Console** | The DAW sends its main mix (and optionally stems) to **virtual channels**. Each virtual channel has its own monitor sends in Console, so every performer mix balances "the track" against live inputs | Simple. Live inputs and playback balanced in one place. Tim's default: Logic main → Twin X VIRTUAL 1/2 |
| **B. Blend in the DAW** | DAW **aux sends / buses** build separate playback mixes. Each bus's output goes to a virtual channel or straight to a hardware output pair | Detailed per-performer playback mixes using the DAW's mixer, sends and automation |
| **C. Both** | The DAW sends a few **submixes** (e.g. drums, everything else) to their own virtual channels. Console's monitor sends then blend those with the live inputs | "More me / more drums" control per performer without rebuilding the DAW mix. This is what x8 VIRTUAL 3/4 is for (e.g. a drum submix on its own fader for headphone tracking) |

**Preferred realization per scenario.** These patterns are examples; the gear can realize a
monitor mix many other ways (DAW output assignment, Flex Routing, either Apollo's outputs…).
Possible realizations are derived, and only the preferred ones are recorded (model §2,
*intent vs realization*):

| Scenario | Listener / transducer | Preferred realization | Status |
|---|---|---|---|
| Tracking or mixing at the desk | Tim / MDR-7506 | Twin X HP ← CUE 1 (carries the main mix); Logic → Twin X VIRTUAL 1/2 | ✅ live |
| Rehearsing, or singing vocal ideas | Tim / Turbosound wedge | x8 out 3 ← CUE 3 (own mix, mono, mirrored to Line 3-4) | ✅ live |
| Recording or rehearsing on in-ears | Tim / PSM300 IEMs | x8 out 7/8 ← a monitor mix mirrored to Line 7-8 | ❓ not routed now **[I24]** |
| A second person on headphones | guest / front HP jack | x8 HP 2 ← CUE 2 (own mix) | 🔶 inferred |
| Headphone tracking with more of one element (e.g. drums) | Tim / MDR-7506 | drum submix → x8 VIRTUAL 3/4, blended in the monitor mix | ✅ described |

Constraints that apply to all of them ✅:
- The number of virtual channels is limited (up to 8, from the driver I/O budget).
- An output used by a monitor-mix mirror can't also be a DAW output.
- A DAW output routed to the same hardware output as a monitor mix is **summed** with it.

**Current configuration** (live 🏷 2026-10-11). The cue buses are shared across both units. On
the Twin X, cue 1 is labelled "HP" and cue 2 "LINE 3/4".

| Mix | Carries (Mix toggle) | Format | Mirror (rear) | Outputs | Wiring → listener |
|---|---|---|---|---|---|
| **Main** | — | stereo | — | x8 MONITOR L/R (level −26 dB, muted at time of read; Twin X knob in control) | **Mackie HR824s** |
| **CUE 1** | **main mix** (Mix on) | stereo | none | Twin X **HP**; x8 HP 1 (front) | **MDR-7506** on Twin X HP: hears the main mix |
| **CUE 2** | own monitor mix | stereo | none | x8 HP 2 (front); Twin X **LINE 3/4** | front jack for a guest; Twin X LINE 3/4 → ? **[I19]** |
| **CUE 3** | own monitor mix | **mono** | **x8 Line 3-4** | x8 outputs 3 and 4 | **Turbosound wedge** on x8 output 3 |
| CUE 4 | — | | | inactive | |

⚠ **The in-ears aren't routed right now.** The PSM300 is on x8 outputs 7/8, but no cue is
mirrored to Line 7-8. Each cue has one mirror destination, so using the IEMs means pointing a
cue's mirror at Line 7-8, for example CUE 2. **[I24]**

⚠ **Possible Alt-monitor conflict.** On the x8, Alt 1 is fixed to line outputs 1-2 and **Alt
2 to line outputs 3-4** ✅ ([Hardware Settings](../../data/manuals/controllers-interfaces/UAD-Console/33-hardware-settings-panel.md)). The
wedge is on output 3 via the CUE 3 mirror. Setting the Alt count to 2 would clash with it.
Alt count is 0 now (AltMonSelection 0, MaxAltMons 2) 🏷.

**What this means for the agent.** "Why can't I hear myself in the in-ears?" is answerable
from the live engine: check which mix mirrors to Line 7-8, whether that mix follows main, and
the channel's send level to that mix.

**Depth reached:** L1 and channel counts automatically. **What isn't discoverable:** what is
physically plugged into each Apollo input and output. That's 👤, and it's the main gap for
troubleshooting.

---

## 4. MIDI

CoreMIDI endpoints right now 🏷:

| Endpoint | In | Out | What it is | Notes |
|---|---|---|---|---|
| **UM-ONE** | ✓ | ✓ | Roland USB ↔ 5-pin DIN MIDI cable | What's on the DIN end? **[I8]** |
| **Launchkey Mini MK4 25** MIDI / DAW | ✓ | ✓ | Novation controller, USB | 📘 manual. DAW port = control-surface mode |
| **VE-500** / **VE-500 CTRL** | ✓ | ✓ | BOSS VE-500 over USB | 📘 MIDI Implementation |
| **IAC Driver Bus 1** | ✓ | ✓ | macOS virtual bus | Used for? **[I9]** |
| **IAC Driver StreamDeck UAD** | ✓ | ✓ | virtual bus: Stream Deck → UAD Console | 🔶 UA Midi Control + Stream Deck 6.8.1 🏷 |
| **Network DAW Control Session** | ✓ | ✓ | macOS network MIDI session | 📄 [uad-midi-ai research](../research/uad-midi-ai.md) / DAW-voice-agent? **[I9]** |

Not enumerated now (disconnected, or behind the UM-ONE): GM-800, TD-17, MPK249, ES-8, FP-30X.

**Depth reached:** L0–L1 for endpoints automatically. **What isn't discoverable:** DIN-side
wiring and MIDI channel assignments (👤). Program-change and CC maps are L3 and come from the
MIDI Implementation manuals 📘.

---

## 5. Controllers

| Unit | Status | Source | Notes |
|---|---|---|---|
| **Novation Launchkey Mini MK4 25** | connected | 🏷 📘 | Via the Anker hub |
| **Akai MPK249** | not seen | 📘 | Owned? Where? **[I2]** |
| **Elgato Stream Deck** | app 6.8.1, IAC bus | 🏷 | The device isn't on USB now **[I10]** |
| **BOSS ES-8** switcher | not seen | 📘 + ES-8 Editor 1.01 🏷 | Pedalboard brain; see §7 |
| Foot controller (live rig) | planned | 📄 rig plan | Model not chosen 📄 |

---

## 6. Hardware instruments and guitar gear

| Unit | Status | Source | Notes |
|---|---|---|---|
| **BOSS GM-800** guitar synth | not seen | 📘 Reference, Parameter Guide, Sound List | Needs a GK pickup. Which one? **[I11]** |
| **BOSS SY-1** synth pedal | | 📘 | |
| **Roland TD-17** e-drums | not seen | 📘 + TD-17 Driver 1.0.2 🏷 | USB audio/MIDI when connected |
| **Roland FP-30X** piano | not seen | 📘 | Emulation: SuperNATURAL piano modelling 🔎 |
| **EMG JMaster** set / pickguard system | | 📘 | Which guitar? **[I12]** |
| **Certano T-Bender** | | 📘 | Which guitar? **[I12]** |
| **UA OX Amp Top Box** | | 📘 + OX app 1.2.0 🏷 | Load box + speaker/mic/room emulation (L4) |
| Guitars, basses, amps, mics, headphones, studio monitors | | 👤 | **No record anywhere.** SoundID Reference 5.13.5 🏷 implies calibrated studio monitors **[I13]** |

---

## 7. Pedals, effects and loopers

All from manuals 📘. None of these have USB/MIDI that appears in the probe, so status, board
position and wiring are all 👤 **[I14]**.

| Unit | Kind (model §4.6) | Has MIDI / app? | Notes |
|---|---|---|---|
| **BOSS VE-500** | harmonizer, vocal multi-FX | USB MIDI + audio 🏷, Editor 1.00 🏷 | [Field notes](../../data/manuals/boss-roland/Boss-VE-500-Field-Notes.md): L2–L3 partly done |
| **BOSS ES-8** | switcher (`route`, `control`) | MIDI, Editor 🏷 | Defines the board's loops |
| **BOSS DD-200** | digital-delay | MIDI | |
| **BOSS CE-2W** | chorus | — | Emulates the CE-1 / CE-2 (L4) |
| **BOSS RC-1** | looper | — | |
| **HeadRush Looperboard** | looper | MIDI | |
| **Strymon Flint v2** | tremolo + reverb | MIDI | Emulates '60s amp trem and spring/plate/hall (L4) |
| **Chase Bliss MOOD** | reverb/loop/micro-looper | MIDI | |
| **Meteore** reverb | reverb | | |
| **Source Audio Vertigo** | tremolo | Neuro Desktop 🏷 | |
| **Catalinbread Naga Viper** | boost (treble booster) | — | Emulates a Rangemaster-style treble booster 🔎 (L4) |
| **Vertex Boost MKII** | boost | — | |
| **Dunlop Cry Baby 535Q** | wah | — | |
| **IK TONEX pedal** | amp-simulation (captures) | TONEX app 1.12.1, Editor, Modeler 🏷 | Captures = emulations of specific units at specific settings (L4) |
| **Pinwheel** (Rev B) + expression | ? | | **[I15]** |
| **KHE ACS** audio controller | routing/switching | | |
| **Radial EXTC-Stereo** | effects interface (line ↔ pedal level) | — | |
| TonePrint 4.2.0 app | 🏷 | | Implies a TC Electronic pedal. Which? **[I15]** |
| MOD5 1.0.2 app | 🏷 | | Which device? **[I15]** |

---

## 8. Monitoring

| Unit | Source | Notes |
|---|---|---|
| **Mackie HR824** (pair) | 👤 | Studio monitors ← Apollo x8 MONITOR L/R. UA speaker-correction profile "Mackie left mix – 2023-06-14" 🏷. Original or mk2? **[I13]** |
| **Sony MDR-7506** | 👤 🏷 | Headphones ← **Apollo Twin X HP** output. UA headphone-correction profile "Sony MDR-7506 Wired Average" (off) |
| **Turbosound** powered floor monitor (~1000 W; TFM-AN series 📘) | 👤 📘 | ← x8 output 3 via a Console cue. Used in the studio for rehearsal and vocal ideas; also a live wedge. Exact model? How many? **[I13]** |
| **Shure PSM300** wireless IEM system | 👤 | Transmitter ← x8 outputs 7/8 via a Console cue. Bodypack and earphone models? **[I13]** |

---

## 9. Software

### 9.1 DAWs and video

| Product | Installed 🏷 | Manual 📘 | Drift |
|---|---|---|---|
| **Logic Pro** | 11.2.2 | Apple guides (version not recorded) | Record the guide version **[I16]** |
| **Ableton Live 12 Standard** | 12.2.2 | Live 12 | — |
| Ableton Live 12 Intro | 12.2 | | Remove? |
| **LUNA** | 3.0.0 | 2.0.1 | ⚠ manual behind |
| GarageBand | 10.4.12 | — | |
| DaVinci Resolve 18 **and** 19 | | Resolve manual | Two versions |
| Final Cut Pro | 10.8.1 | — | |

### 9.2 Notation, authoring and audio → MIDI

| Product | Installed 🏷 | Manual 📘 | Notes |
|---|---|---|---|
| **Guitar Pro 8** | 8.1.5 | GP8 guide | GP7 also installed |
| **Scaler 3** | 3.3.1 | 3.3.1 ✓ | Scaler 2 also installed (AU) |
| **MIDI Guitar 3** | 3.0.74 | jam.live mirror (3.0.74) ✓ | Field notes say 3.0.55: stale (finding 2) |
| MIDI Guitar 2 | 2.2.1 | legacy guide | |
| **Melodyne 5** | 5.4.2 | studio manuals | |
| Moises, Jamzone 3.7.5, Stage Traxx 3 3.8.40 | | — | Practice / backing tools |

### 9.3 Plugins

Counts 🏷: **380 AU**, 144 VST3, 58 VST2, 6 AAX, all in `/Library/Audio/Plug-Ins/` (none in
the user folder).

| Family | Count / examples 🏷 | Version 🏷 | Manual 📘 | Emulation (L4) |
|---|---|---|---|---|
| **UAD DSP** (`UAD …`) | 224 | 11.8.0 (1176 Rev A) | UAD Plug-Ins Manual | Rich: names state the reference device and often the revision (UA 1176 Rev A / LN Rev E / AE, Teletronix LA-2A Gray / Silver, Fairchild 660 / 670, Pultec EQP-1A, Neve 1073 / 1081 / 33609, SSL G Bus, API 2500, dbx 160, EMT 140 / 250, Lexicon 224 / 480L, Studer A800, Ampex ATR-102, Marshall, Fender, Friedman, Diezel, ENGL amps…) |
| **UAD Native** (`uaudio_…`) | ~68 | | same | Same emulations as DSP, running on the CPU (finding 5) |
| **Arturia V Collection** | 41 instruments | | — | Each one is an emulation: Mini V4 → Minimoog, Jup-8 V4 → Jupiter-8, DX7 V, CS-80 V4, Prophet-5 V, Mellotron V, B-3 V2… |
| **Soundtoys** 5.5 | EchoBoy, Decapitator, PrimalTap, Little Plate, … | 5.5.3 | Soundtoys guide | Some: EchoBoy's echo styles, PrimalTap |
| **Toontrack** | Superior Drummer 3, EZdrummer, EZbass, EZkeys 2 | SD3 3.4.4 | SD3 manual | Sample-based (real kits) |
| **Native Instruments** | Kontakt 8 | 8.13.1 | — | Libraries: sample-based |
| **IK Multimedia** | AmpliTube 5, TONEX, MODO BASS 2 | 5.10.9 / 1.12.1 / 2.0.4 | — | Amp models, captures, physically-modelled bass |
| **Antares** | Auto-Tune Pro / Artist / Access / EFX+ / Slice / Vocodist, AVOX, Harmony Engine | | — | |
| **iZotope** | Ozone 12 (+ Elements), Neutron 5 Elements, Nectar 4 Elements, Audiolens | | — | |
| **Celemony** | Melodyne | 5.4.2 | ✓ | |
| FabFilter | Pro-Q 3 | 3.22 | — | |
| oeksound | soothe2 | | ✓ | |
| Klanghelm | VUMT deluxe | 2.6.0 | ✓ | VU meter |
| Youlean | Loudness Meter 2 | 2.4.4 | ✓ | |
| Sonarworks | SoundID Reference | 5.13.5 | — | Room/speaker calibration |
| Orchestral Tools | SINE Player | 1.3.1 | — | |
| Sonnox | Oxford Limiter (as a UAD plugin) | | ✓ | |
| Akai | VIP 3.0 | not found 🏷 | ✓ | Still used? **[I16]** |

**Depth lesson:** a hand-written plugin list would go stale in weeks. The full list, versions
and formats should be **generated by the probe**. This doc should keep only families and the
emulation links that need judgment.

### 9.4 Editors, drivers and utilities

| Product | Version 🏷 | Controls / for |
|---|---|---|
| VE-500 Editor / VE-500 Driver | 1.00 / 1.0.3 | BOSS VE-500 |
| ES-8 Editor | 1.01 | BOSS ES-8 |
| TD-17 Driver, UM-ONE Driver | 1.0.2 / — | Roland TD-17, UM-ONE |
| TONEX / Editor / Modeler | 1.12.1 | TONEX pedal and software |
| Neuro Desktop | | Source Audio pedals |
| OX app | 1.2.0 | UA OX Amp Top Box |
| TonePrint | 4.2.0 | TC Electronic pedal(s) |
| UA Midi Control | 5.11.1 | MIDI control of UAD Console |
| Elgato Stream Deck | 6.8.1 | Stream Deck → UAD (IAC) |
| SoftRAID | 8.6.1 | ThunderBay RAID |
| License managers | | iLok, Native Access 3.26.0, UA Connect, IK Product Manager, Arturia Software Center, Toontrack Product Manager, iZotope Product Portal, Antares Central |

---

## 10. Connections and signals (known so far)

Very little of the wiring is known. Everything below is either probed or from repo notes.

| From | To | How | Source |
|---|---|---|---|
| VE-500 USB | Mac | USB audio 2×2 + MIDI | 🏷 |
| Launchkey Mini MK4 | Mac | USB via Anker hub | 🏷 |
| UM-ONE | Mac ↔ ? (DIN) | USB ↔ 5-pin DIN | 🏷 + **[I8]** |
| Apollo x8 → Satellite → Twin X | Mac | Thunderbolt, in series | 🏷 👤 |
| Apollo x8 MONITOR L/R | Mackie HR824 L/R | analog, balanced | 👤 |
| Twin X (monitor controller) | x8 monitor section (level, speakers ↔ headphones) | Console remote monitor control | 👤 + 🏷 `RemoteMonitorController` |
| Apollo Twin X HP | Sony MDR-7506 | headphone, stereo | 👤 |
| Gator Backline snake (ch 1–4, floor box) | Apollo x8 mic inputs 1–4 | XLR, mic level, via snake tails | 👤 |
| Apollo x8 output 3 | Turbosound powered floor monitor | line, mono; Console cue | 👤 |
| Apollo x8 outputs 7/8 | Shure PSM300 transmitter → bodypack → in-ears | line → RF wireless; Console cue | 👤 |
| Logic main out | Twin X VIRTUAL 1/2 | virtual (Core Audio) | 👤 + 🏷 |
| macOS default output | x8 VIRTUAL 1/2 | virtual (Audio MIDI Setup) | 👤 + 🏷 |
| DAW (on demand) | x8 VIRTUAL 3/4 | virtual | 👤 + 🏷 |
| Pedalboard out | Twin X input 1 ("B1 PdlBrd") | analog line | 🏷 live name |
| Guitar direct | Twin X input 2 ("B2 Guit Dir") | Hi-Z | 🏷 live name |
| OX Amp Top Box out 1 / 2 | x8 inputs 5 / 6 ("A5 OX 1", "A6 OX2") | analog line | 🏷 live name |
| Dynamic mic | x8 input 1 ("A1 Mic Dyn") | mic | 🏷 live name |
| Condenser mic | x8 input 3 ("A3 Mic Cond.") | mic | 🏷 live name |
| Clean guitar (MG3 setup) | Apollo x8 input 4 → Console → Logic and MIDI Guitar 3 | analog | 📄 MG3 notes. ⚠ The live name for x8 input 4 is "A4 Mic", and the guitar DI is now on Twin X input 2. The notes may be out of date **[I20]** |
| MIDI Guitar 3 | Apollo ("Universal Audio Thunderbolt") | audio out | 📄 MG3 notes |

Everything else (mic → VE-500 → ?, pedalboard order, ES-8 loops, monitor outputs, headphone
feeds) is 👤 **[I17]**.

---

## 11. Places

Nothing is recorded yet. 👤 **[I18]**

---

## Parking lot: no manual yet

Gear and software that is owned or in use but has **no manual in `data/manuals/`**. When one
is added, register it in [`sources.toml`](../../data/manuals/sources.toml), run
`scripts/convert_manuals.py`, and remove the row here.

**Priority** reflects what a manual would unlock:
- **High**: hardware with ports, routing or MIDI the agent needs to reason about.
- **Med**: hardware or software that's used often.
- **Low**: software where the probe plus a vendor lookup is usually enough.

### Hardware

| Item | Status | Priority | Why a manual helps | Source |
|---|---|---|---|---|
| **Apollo x8** (HEXA) hardware manual | owned, main interface | **High** | Rear-panel I/O, levels, ADAT/S/PDIF, front-panel controls. Console software is now covered (below) | 🔎 UA support (probably also Zendesk: the same fetch approach should work) |
| **Apollo Twin X** (QUAD) hardware manual | owned, monitor controller | **High** | Front-panel monitor/HP controls, LINE 3/4 outputs | 🔎 UA support |
| **UAD-2 Satellite TB3** (QUAD) | owned | Low | DSP only; few controls | 🔎 UA support |
| **Mackie HR824** | owned, studio monitors | Med | Rear-panel EQ / acoustic-space switches (state worth recording) | 🔎 Mackie (mk1 or mk2? [I13]) |
| **Sony MDR-7506** | owned, on Twin X HP | Low | Little to configure | — |
| **Shure PSM300** (transmitter + bodypack) | owned, IEMs ← x8 7/8 | Med | Channel/frequency, stereo vs mix mode, levels | 🔎 Shure |
| **Gator Cableworks Backline** 6-ch snake | owned, → x8 mic 1–4 | Low | Passive; only the channel map matters | — |
| **Roland UM-ONE** | owned, USB ↔ DIN MIDI | Med | Driver modes; what's on the DIN end [I8] | 🔎 Roland |
| **Elgato Stream Deck** | owned? [I10] | Med | Drives UAD via IAC; useful for automation | 🔎 Elgato |
| **Mac Studio** (M1 Max) | owned | Low | Ports and Thunderbolt bus layout | 🔎 Apple |
| **Samsung Portable SSD X5** | owned, Logic projects | Low | | 🔎 Samsung |
| **Mics**: dynamic ("A1 Mic Dyn", SM7 in sessions), condenser ("A3 Mic Cond.", KX67 / Rode in sessions), SM57 | owned? [I13] | Med | Polar pattern, pad and filter switches (mic state for recall) | 👤 then 🔎 |
| **Guitars and basses** | owned | Med | Which pickups / GK / T-Bender each has [I11][I12] | 👤 |
| **"MOD5"** device (MOD5 app 1.0.2; "Mod5" / "Mod5 IR" in Console sessions) | owned? | Med | Unknown device [I15] | 👤 |
| **TC Electronic pedal** (TonePrint app) | owned? | Low | Which pedal? [I15] | 👤 |
| **"O2"** (Console session names "A2 Pedalboard O2", "PB O2") | ? | Med | What is O2? [I15] | 👤 |
| Samsung LC34G55T / LG display | owned | Low | | — |

*Resolved:* **UAD Console for Apollo manual**: mirrored on 2026-10-11 to
[`manuals/controllers-interfaces/UAD-Console/`](../../data/manuals/controllers-interfaces/UAD-Console/INDEX.md)
(39 articles) by `scripts/fetch_uad_console_docs.py`, from UA's help center via the Zendesk
API. Re-run the script to pick up UA's edits.

### Software

| Item | Version 🏷 | Priority | Notes |
|---|---|---|---|
| **Arturia V Collection** (41 instruments) | | Low | Each instrument's emulation target is in its name |
| **Native Instruments Kontakt 8** | 8.13.1 | Low | Libraries matter more than the player |
| **IK AmpliTube 5 / TONEX (software) / MODO BASS 2** | 5.10.9 / 1.12.1 / 2.0.4 | Med | TONEX pedal manual exists; the software/Modeler doesn't |
| **Antares Auto-Tune** suite, AVOX, Harmony Engine | | Low | |
| **iZotope** Ozone 12, Neutron 5, Nectar 4 | | Low | |
| **FabFilter Pro-Q 3** | 3.22 | Low | |
| **Toontrack EZdrummer / EZbass / EZkeys 2** | | Low | SD3 manual exists |
| **Sonarworks SoundID Reference** | 5.13.5 | Med | Calibration of the HR824s / MDR-7506 |
| **Orchestral Tools SINE Player** | 1.3.1 | Low | |
| **UA Midi Control** | 5.11.1 | Med | MIDI → Console control (Stream Deck path) |
| **Guitar Pro 7** | | Low | GP8 manual covers it |
| **Moises, Jamzone, Stage Traxx 3** | | Low | Practice / backing tools |

### Planned (from the live rig plan): no manual, not owned yet?

| Item | Notes |
|---|---|
| Boss **VG-800**, **GK-5** | Status unclear [I2]. GK-5 may already be owned for the GM-800 [I11] |
| **NUX Optima Air** | Acoustic IR / preamp |
| **MOTU M4** | Live interface; the x8 / Twin X may make it unnecessary |
| **AbleSet** | Setlist software for Ableton |
| Foot controller | Model not chosen |

## 13. Questions for you

- ~~**[I1]** Apollo units~~ *Answered:* x8 + Twin X + Satellite in series; Twin X is the
  monitor controller.
- **[I2]** Status of gear seen only in manuals or the rig plan:
  - manuals only: GM-800, MPK249, iRig HD X, TD-17, FP-30X;
  - rig plan only: VG-800, GK-5, NUX Optima Air, MOTU M4, AbleSet.

  For each: owned, planned, or gone?
- **[I3]** Is there an LG display in use?
- ~~**[I4]** Generic USB devices on the Anker hub~~ *Resolved (inferred):* the dock's own SD card slot (Genesys reader) and its audio in/out jack, per the dock manual.
- **[I5]** Is OneDrive used for anything music-related?
- **[I6]** Add the Apollo x8, Apollo Twin X and UAD Console manuals to `data/manuals/`? (The
  models are now known: x8 HEXA, Twin X QUAD.)
- **[I7]** What's in the Multi-Output Device, and what is it for?
- **[I8]** What's plugged into the UM-ONE's DIN end?
- **[I9]** IAC Bus 1: what's it for? (*Partly answered:* Console's prefs configure the
  "Network DAW Control Session" as a bidirectional **MCU control surface** 🏷. Is that the
  DAW-voice-agent work?)
- **[I10]** Stream Deck: which model, and is it in use?
- **[I11]** Which GK pickup is on which guitar?
- **[I12]** Guitars: which ones have the EMG JMaster and the T-Bender?
- **[I13]** Studio monitors, headphones, IEMs, and how many Turbosound wedges?
- **[I14]** Pedalboard: which pedals are on it, in what order, and how is the ES-8 looped?
- **[I15]** What are the Pinwheel, TonePrint and MOD5 devices?
- **[I16]** Logic manual version; is Akai VIP still used?
- **[I17]** Main signal paths: mic → ?, guitar → ?, outputs → monitors and headphones.
- **[I18]** Places: room layout, desk, racks, pedalboard(s).
- **[I19]** *Partly answered:* HR824s ← x8 MONITOR L/R; the Twin X is the remote monitor
  controller (confirmed live); MDR-7506s ← Twin X HP. Still open: what are the Twin X LINE
  3/4 outputs feeding? Is anything on the x8's HP 1/2 or the alt monitor outputs?
- ~~**[I21]** x8 VIRTUAL 3/4~~ *Answered:* a DAW submix (e.g. drums) on its own
  Console fader, so it can be balanced separately in a monitor mix (pattern C, §3.3).
- ~~**[I22]** Monitor-mix map~~ *Answered from the live engine* (§3.3): CUE 1 follows main →
  Twin X HP; CUE 2 independent → x8 HP 2 + Twin X LINE 3/4; CUE 3 mono → mirror to x8 Line
  3-4 (wedge).
- **[I24]** In-ears: which cue do you usually mirror to Line 7-8 for the PSM300, and
  is it the same one the wedge or headphones use? Is the PSM300 set to stereo or mono
  (mixed) mode?
- **[I23]** Snake: what are channels 5–6 for, and does it have returns?
- ~~**[I20]**~~ *Resolved:* yes, the clean guitar is on x8 input 4, via ES-8 TUNER → Peterson → JHS Clover → snake 4. Console's name 'A4 Mic' was misleading. Was: Is the MG3 setup still "guitar on x8 input 4", or is it now the Twin X "B2 Guit
  Dir"?

