# MIDI Guitar 3 — Field Notes

Practical notes on how MIDI Guitar 3 (MG3) fits together in this studio: the
Apollo, Logic, and the synths hosted inside MG3. They fill in what the official docs
leave out. MG3 is still in beta, and much of its documentation is marked "under
construction". Several pages are stubs, and a few contradict themselves.

**Sources** (same folder, mirrored from jam.live by `scripts/fetch_jamlive_docs.py`):
- [Modules](modules/modules.md): the main reference, cited as **Mod L.N**
- [Changelog](downloads/changelog.md), cited as **CL L.N**
- [Patches](modules/patches.md), [Tutorial](modules/tutorial.md), [DAW Guides](modules/daw-guides.md)
- [Legacy MG2 DAW guide](legacy/mg2-daw-guide.md), cited as **MG2 L.N**. The new site still links to it for DAW setup.
- Logic side: [Logic Pro User Guide](../../daw-video/logic-pro-mac-user-guide.md), [Instruments guide](../../daw-video/logic-pro-mac-instruments-user-guide.md)

**How much to trust each claim.** Each claim is marked with one of:
- ✅ **Docs**: stated in the jam.live docs, the changelog or the Logic manual.
- 🏷 **Your setup**: read from your MG3 settings, logs or patch files on this Mac (2026-10-03).
- 🔶 **Inferred**: worked out from the docs or patch files, but not stated directly.
- 🎸 **Tested**: confirmed working in this studio.
- 🧪 **Test**: should be checked by playing. See the [test list](#tests-to-run).

---

## 0. Which version you're running vs. what the docs describe

🏷 **Installed: MG3 3.0.55 (Oct 2024)**, AU and standalone. The logs say `MIDI Guitar 3.0.55`.
✅ **The docs and changelog describe 3.0.74 (Aug 2026).** That's nearly two years of
changes, so some documented modules and behaviour won't match what you see.

Changes after 3.0.55 that affect how you use it (✅ CL):

| Version | Change | Why it matters |
|---|---|---|
| 3.0.66 | Sustainer works on dry guitar audio | Not in 3.0.55 |
| 3.0.67 | **Experimental modules hidden by default** (Settings → Plugins) ([CL L241](downloads/changelog.md#L241)) | After upgrading, some modules may seem to vanish |
| 3.0.67 | Hosts third-party **MIDI FX plugins**; MIDI 1.0 aftertouch fix; Patchbay can filter MIDI channel / program change; fretboard and scales views | Not in 3.0.55 |
| 3.0.68 | **MIDI Machines run before instruments**, so Transposer no longer pitch-shifts a hosted synth's audio ([CL L227](downloads/changelog.md#L227)); Legato adds an 8 ms option | 🔶 A Transposer in 3.0.55 may behave oddly in front of a hosted synth |
| 3.0.73/74 | **Per-string MIDI channels flipped**: now ch 2 = high E … ch 7 = low E. Before, ch 2 was low E ([CL L112](downloads/changelog.md#L112)) | Anything that relies on string→channel (Logic split, String Filter, recorded MIDI) reverses after upgrading |
| 3.0.74 | **Data folder moves** from `~/Library/Group Containers/X6D2Q4W5A8.midiguitargroup/` to `~/Library/Application Support/JamOrigin/` ([CL L25](downloads/changelog.md#L25)) | See below |

**If you upgrade to 3.0.74** (✅ CL L25–27):
1. Run the **standalone app once** before opening the AU in Logic. That migrates your patches.
2. **Don't delete the old Group Containers folder.** Deleting it triggers license reactivation.
3. Stop using older versions afterwards.

🏷 Note that `~/Library/Application Support/JamOrigin/` already exists, but it holds
**MIDI Guitar 2** data (Patches, Plugins64, MIDIMachines from 2023–25). 🔶 Expect
MG2 and MG3 files to share that folder after the move.

🔶 The Tahoe 26.1 Logic AU fix in 3.0.74 doesn't apply to you yet: this Mac runs macOS 14.5.

---

## 1. Signal flow

✅ A patch is a set of modules wired together ([Patches](modules/patches.md)). Modules
come in three kinds: **Instruments** (synths), **Effects** (audio) and **MIDI Machines**
(MIDI→MIDI, e.g. arpeggiator, note filters). ✅ "Audio flows through a Chain from top
to bottom, and then from left to right: Chain → Mixer → Master Chain" ([Tutorial](modules/tutorial.md)).

```
 Guitar (dry, Apollo input)
   │
   ▼
 TRACKER (the "MIDI Guitar 3" module)
   Input · Gate · tuning · polyphony · bends
   │  notes + 4 per-note envelopes: Strike · Pressure · Brightness · Pitch/Glide
   │
   ├─► CHAIN A: [MIDI machines] ─► [Instrument  or  MIDI Output] ─► [audio FX] ─┐
   ├─► CHAIN B: …                                                             ├─► MIXER (gain/pan per chain) ─► MASTER CHAIN ─► audio out
   └─► CHAIN C: …                                                             ┘

 MIDI PATCHBAY (CCs from controllers, number keys 1–9) ┐
 MODULATORS (ADSR, Brightness, Wobble, Sine …)         ├── virtual cables ──► almost any knob or switch
```

- 🔶 The patch files show **three chains plus a master** feeding a Mixer with
  `chainA/B/C` gain and pan 🏷. So a patch is three parallel chains, not one long one.
- ✅ The tracker extracts a **separate set of MPE envelopes for each note** in a chord. The
  display only shows one note ([Patches](modules/patches.md)).
- ✅ **Modulators are polyphonic.** Each cable carries six control signals, one per note
  ([Mod L128](modules/modules.md#L128)). So "Brightness → filter cutoff" works per
  note, not per chord.
- 🔶 A chain carries guitar **audio** as well as MIDI. That's how audio effects, NAM
  and Guitar Mods can sit in the same chain as synths.

### Tracker controls
✅ [Mod L21–37](modules/modules.md#L21):
- **Tuning**: set it to match the guitar. The standard tracker tracks down to **C2**.
- **Input gain**: set level at the **interface preamp**. "Only use the Input knob if your
  audio interface input gain pre-amp is not giving you a sufficiently strong signal."
- **Gate**: a threshold on how many notes get tracked. Low = more responsive.

🏷 Your current tracker settings (`Preferences/midi guitar 3.txt`): input gain 5, gate 0.00,
dynamics 0.33, threading automatic. 🔶 **dynamics** and **threading** aren't documented
anywhere. Patch files also store **polyphony** (all yours are 6) and **bends** (yes/no),
which are also undocumented. 🧪 Test T5 for what `bends: no` does.

---

## 2. The two working modes

🎸 Both modes are tested in this studio (2026-10-03). They share the same starting point:

- **Clean guitar** into the **Apollo x8, input 4**, through UAD Console.
- **Console fader for input 4 down**, so you don't hear the direct guitar, only MG3's output.
- ✅ The dry input matters: "Don't use any other effects before MIDI Guitar (as MIDI
  Guitar needs a completely dry input)" ([MG2 L136](legacy/mg2-daw-guide.md#L136)).
  🔶 Keep Console inserts off input 4, or set them to monitor only, so MG3 sees a clean signal.

| | **Mode 1: Just playing** (standalone) | **Mode 2: Writing MIDI** (Logic, also LUNA) |
|---|---|---|
| MG3 runs as | Standalone app | AU on a Logic audio track |
| Synth lives in | Inside MG3 (your Arturia V, EZbass, UADx Minimoog… patches) | Logic software instrument track |
| MG3 patch | Any hosted-synth patch | `DAW` (MIDI Output only) |
| What you can record | Nothing (play only) | **MIDI notes** on the instrument track |
| Logic monitoring | Not involved | Software Monitoring + Low Latency Mode **on** |

### Mode 1: Just playing (standalone) 🎸
1. Open the **MIDI Guitar 3** standalone app.
2. Audio settings: **input device = Universal Audio Thunderbolt, input channel 4**;
   **output = Universal Audio Thunderbolt**. 🏷 These are saved in `MIDI Guitar 3.settings`
   (44.1 kHz, 128 samples).
3. Load a patch that hosts a synth, and play.

### Mode 2: Writing MIDI in Logic 🎸
**Logic monitoring.** Turn on **Software Monitoring** and **Low Latency Mode**.
- Add both as buttons in the **Control Bar** (Customize Control Bar and Display). You'll
  want them off most of the time: without MG3, UAD Console already gives very low-latency
  monitoring, and Logic's software monitoring would only add a second, later copy.

**Track 1: audio track (the tracker)**
1. Create a **mono audio track**. Input = **Apollo input 4** (the Console channel with the clean guitar).
2. Turn on **Input Monitoring** (the orange **I** button next to **R**). MG3 gets no live audio without it.
3. **Pull this track's fader down**, so you don't hear the direct guitar here either.
4. Put **MIDI Guitar 3** in the **Audio FX** slot and load the **`DAW`** patch.
   - 🏷 `DAW` has one active chain with one module: **MIDI Output** (MPE, bend range 48).
   - The MIDI Output port should default to **MIDI Guitar Virtual Output**. If it shows
     anything else, select that port.
   - ✅ Don't choose "Direct MIDI Output" with the AU ([Mod L157](modules/modules.md#L157)).

**Track 2: software instrument track (the sound and the recording)**
1. Create a **Software Instrument track** with any instrument.
2. Set the track's **MIDI input = MIDI Guitar Virtual Output**.
3. Playing the guitar now plays that instrument, and **recording on this track writes
   MIDI notes** that you can edit, quantize or reassign to another sound later.

🔶 Setting the instrument track's MIDI input to the MG3 port, not "All", stops a
keyboard controller from also playing the track while you record guitar.

🔶 For per-note bends on Logic's own synths, set that instrument to MIDI Mono Mode with a
matching bend range (see [§3](#logics-mpe-instruments)).

**LUNA:** the same setup works there too. MG3 goes on a mono audio track with input
monitoring, feeding an instrument track whose MIDI input is MIDI Guitar Virtual Output.

### Latency settings
- ✅ **44.1 kHz, 128 or 256 samples.** Higher sample rates add CPU load and latency with
  no tracking benefit ([MG2 L460](legacy/mg2-daw-guide.md#L460)). 🏷 Your Apollo setup is already
  44.1 kHz / 128. Your logs also show sessions at 48 kHz, which is fine.
- ✅ **Logic → Settings → Audio → Multithreading: Playback Tracks**, not "Playback & Live
  Tracks". Otherwise Logic uses the large buffer for the live track and adds latency
  ([DAW Guides L13](modules/daw-guides.md#L13)).
- ✅ Use Logic's **Low Latency Mode** while playing ([MG2 L128](legacy/mg2-daw-guide.md#L128)).
- ✅ Using the **standalone app** with its virtual MIDI out also works, but adds "a bit of
  latency" compared with the AU ([MG2 L147](legacy/mg2-daw-guide.md#L147)).

### Idea: use an MG3 synth sound and still record MIDI
🔶 In Mode 2 you hear a Logic instrument. To play one of your MG3-hosted synth patches
in Logic and still capture MIDI, add a **MIDI Output** module to a spare chain of that
patch, and bring the audio track's fader back up. Its output is then the MG3 synth, not
the direct guitar. The instrument track records the
notes (mute its instrument, or use it as a layer). 🧪 Untested.

### Safety net: always keep the DI
✅ MG3 will convert **dry recorded guitar** into MIDI after the fact, the same as live
input ([MG2 L464](legacy/mg2-daw-guide.md#L464)). Record the dry guitar on its own track
every time and you can re-track the MIDI later with different settings or a newer version.

---

## 3. MPE vs. MIDI 1.0 — matching the receiving synth

✅ The MIDI Output module and every hosted Instrument have three modes ([Mod L167–189](modules/modules.md#L167)):

| Mode | Channels | Use for |
|---|---|---|
| **MIDI MPE** (default) | One note per channel, ch 2+ | MPE synths. Per-note bends and expression |
| **MIDI 1.0 Legacy** | One channel you pick (1–16) | Non-MPE instruments: EZbass, most samplers, drums |
| **MIDI 1.0 Multichannel** | Per-note/per-string channels, like MPE but without the MPE setup | Hardware-style "mono mode" receivers |

Per mode you also set **pressure type** (channel pressure / aftertouch / none) and **bend
range** (0, 1, 2, 4, 8, 12, 24, 36, 48). ✅ "Be sure to match these settings to the
receiving synth's bend range!" ([Mod L165](modules/modules.md#L165)).

**Which channels, exactly?** The docs disagree:
- ✅ Modules page: MPE and Multichannel use "channels 2-9 (not 8) in a round-robin fashion" ([Mod L175](modules/modules.md#L175)).
- ✅ Changelog: "notes on midi channel 2 (high E) .. channel 7 (low E)", i.e. one channel per string ([CL L112](downloads/changelog.md#L112)).
- 🏷 Your prefs have `string channels : [7,6,5,4,3,2]`, which looks like per-string mapping (added in 3.0.55: "String-to-MIDI mapping", [CL L304](downloads/changelog.md#L304)).
- 🔶 Probably per-string channels 2–7 on your version, in the **old** order (ch 2 = low E). 🧪 Test T1.

Either way, channel 1 is left free as the MPE "common" channel, which is what Logic expects.

### Logic's MPE instruments
✅ Logic instruments become MPE receivers via **MIDI Mono Mode**
([User Guide L20899+](../../daw-video/logic-pro-mac-user-guide.md#L20899)):
- Supported in: **Alchemy, EFM1, ES2, Quick Sampler, Retro Synth, Sampler, Sculpture, Vintage Clav**.
- Set **MIDI Mono Mode = On (with common base channel 1)**.
- Set **Mono Mode Bend Range** to match MG3. ✅ Logic's default is 48, and MG3's `DAW`
  patch sends **48** 🏷, so they already match.
- ✅ The Logic manual says 24 "is the preferable setting" for MIDI guitars
  ([Instruments guide L5572](../../daw-video/logic-pro-mac-instruments-user-guide.md#L5572)).
  That's generic advice for hardware converters that default to 24. What matters is that
  both sides match.

**Rule:** whenever you change bend range on one side, change it on the other. A mismatch
makes every bend and every bit of vibrato land out of tune by the ratio between them.

### Bend ranges in your hosted patches 🏷
| Patch | Instrument | Mode | Bend range |
|---|---|---|---|
| dont change | Prophet-5 V, Jup-8 V4 | MPE | 48, 48 |
| 80s Piano Weird | DX7 V | MPE | 48 |
| Strings | Solina V2, UADx Minimoog | MPE | 48, 48 |
| bellorgan | Jup-8 V4 / Augmented BRASS | MPE | **0** / 48 |
| BrassnBass | Augmented BRASS / EZbass | MPE / Legacy | **0** / 0 |
| Auto-Bass | EZbass | Legacy | 0 |

- 🔶 **Bend range 0 means no pitch information is sent.** Bends and vibrato are dropped
  and notes play at the fretted pitch. That suits EZbass and organ-like sounds. Jup-8 V4
  in `bellorgan` may have been set to 0 on purpose; check if it sounds stiff.
- 🔶 For each Arturia/UADx synth on 48, check that the plugin's own MPE setting is on and
  its bend range is 48 too. 🧪 Test T4.

---

## 4. Note filters and articulation — what the docs get wrong

### Auto Bassist / Auto Melody: the description is reversed
✅ The docs say Auto Bassist passes only notes **above** the limit and Auto Melody only
notes **below** ([Mod L415](modules/modules.md#L415), [L432](modules/modules.md#L432)). That's the
opposite of what the names imply. The doc author's own hidden comment says Auto Bassist
"will extract the lowest notes played at any time, as a bass line" ([Mod L417](modules/modules.md#L417)).

🔶 Most likely: **Auto Bassist plays the lowest note** (below the limit), possibly with
legato between notes, and **Auto Melody plays the highest**. 🧪 Test T2.

🏷 Your limit settings (stored as MIDI note numbers, where 60 = C4):

| Patch | Limit | Note |
|---|---|---|
| DAW-autobass | 57 | **A3** (the default; 2nd fret on the G string) |
| Auto-Bass | 60 | C4 |
| BrassnBass, Strings | 50 | D3 |

### Other doc problems
- **Gain**: headed "Boost or cut input signal" but described as controlling MIDI velocity, −40 dB to +10 ([Mod L249](modules/modules.md#L249)). 🔶 Probably scales note velocity/level going into the chain, not the guitar input.
- **Dynamics**: "pressure (MIDI sustain)" is wrong terminology. Pressure is aftertouch, and sustain is CC64 ([Mod L225](modules/modules.md#L225)). Compress raises velocity, and Hold Press raises aftertouch.
- **String Filter** and **Mute Open Strings** are listed as **Hex-only** ([Overview](modules.md)), but 🏷 your Auto-Bass, BrassnBass and Strings patches use String Filter with the standard tracker. 🔶 3.0.55 allowed it on per-string-mapped standard tracking. Its reliability on a normal pickup is unknown.
- **Pitch Filter, Scale Filter, Strike Filter, Sequencer, Cabinet, Reverb**: stubs, no real documentation. 🏷 `bellorgan` has a Pitch Filter with from = 71 (B4), to = 67 (G4). 🔶 from > to may mean an inverted (notch) range. 🧪 Test T6.

### Articulation modules that are documented properly
✅ [Mod L199–245](modules/modules.md#L199):
- **Sustainer**: *Infinite* (holds the last note until the next one), *Freeze Chord* (holds
  everything and blocks new notes until released), *Piano-like* (each note rings for a set
  release, 0 ms–10 s). Put Freeze on a footswitch CC for pads.
- **Legato**: turns overlapping notes into legato transitions instead of retriggering.
  - *Steal range 1–12 semitones*: keyboard-style legato.
  - *Note extension 1–100 ms*: stretches notes so the next one is caught as legato.
  - Use with mono-legato synth patches (lead lines, brass).
- **Chromatic**: blocks or limits bends (1–4 semitones). Bent notes retrigger as new
  notes. Use for piano/EP sounds. 🔶 Overlaps with the tracker's `bends: no`.
- **Transposer**: octaves −2…+2 (default −1), semitones ±12, cents ±50. ✅ It shifts
  both MIDI and audio.
- **Whammy**: ±12 semitones, scaled to the synth's own bend range ([Mod L331](modules/modules.md#L331)).

---

## 5. MIDI control

✅ [Mod L101–114](modules/modules.md#L101):
- **MIDI Patchbay** (bottom left): pick the MIDI controller, then drag from a CC dial to
  any knob. Number keys **1–9** send 0/127 toggles in place of pedals, which is handy for testing.
- **The first two Patchbay slots step through patches** (previous/next). 🏷 Your
  `midicontrol.txt` has `prev patch : 14`, `next patch : 15`. 🔶 That means CC#14 / CC#15.
  🏷 The controller is currently set to "No MIDI Controller".
- **Program Change** loads patches in the order of the files in your user-preset folder:
  PC#000 = first patch in the top folder, and so on. 🔶 Order is probably alphabetical:
  `80s Piano Weird`, `Auto-Bass`, `Blank-record`, `BrassnBass`, `DAW`, … 🧪 Test T7.
  Adding or renaming a patch shifts every number after it.
- ✅ Hold the mouse button on a cable to disconnect it. In 3.0.73+ this also resets the knob
  to its default ([CL L119](downloads/changelog.md#L119)).

---

## Not covered here

- **MG3 Hex / hex pickups**: not part of the current setup.
- **Guitar Mods**: ✅ "highly experimental", needs Apple Silicon, not available for
  download at the moment ([Guitar Mods](products/GM.md), [Downloads](downloads.md)).
- **Lua / WebSocket API**: arrives in 3.0.80 ([Developers](developers.md)).

---

## Tests to run

For the MIDI tests: record MG3's MIDI in Logic, export the region (File → Export →
Selection as MIDI File) into `midi/`, then run `uv run scripts/midi_dump.py` to read the
channels, bends and velocities as text.

| # | What it checks | Procedure | What the result means |
|---|---|---|---|
| T1 | String → channel mapping on 3.0.55 | `DAW` patch (MPE). Play each open string low E → high E, one at a time; dump | Ch 2…7 low→high = old order (flips on upgrade). Channels that vary per note = round-robin |
| T2 | Which way Auto Bassist / Auto Melody filter | `DAW-autobass`, limit A3. Play an open-position C chord; dump. Repeat with Auto Melody | Only the lowest note → it's a bass extractor (docs wrong). Only notes above A3 → docs right |
| T3 | Bend range matching in Logic | `DAW` patch (48) → Alchemy, MIDI Mono Mode ch 1, bend range 48. Bend the G string a whole step; then set Alchemy to 24 and repeat | 48: bend lands in tune. 24: bend comes out half as wide → confirms matching matters |
| T4 | Hosted synths really receive MPE | `dont change` patch. Play a chord, bend one string | Only that note bends → MPE works. All notes bend → synth isn't in MPE mode |
| T5 | Tracker `bends: no` vs. Chromatic module | Same synth, bend slowly with each setting | Shows whether `bends: no` retriggers or just quantizes |
| T6 | Pitch Filter with from > to | `bellorgan`. Play notes below G4, between G4 and B4, above B4 | Which band is passed or blocked |
| T7 | Program Change order | Send PC#0, #1, #2 from Logic or a controller | Confirms the patch order and whether `Factory/` counts |
| T8 | Latency, AU vs. standalone | Record DI and MG3 MIDI together; compare the note start to the audio transient. Repeat with standalone + virtual MIDI | Offset in ms. Pick the faster route |

When a test is done, update the matching 🔶 marker above to ✅ (or correct the claim).
