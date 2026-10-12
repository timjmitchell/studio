# One-Man-Band Rig — Ableton, AbleSet & MIDI/OSC Control

> **Status: research notes for the planned [live rig](one-man-band-live-rig.md).** What's
> installed, what each layer of Ableton/AbleSet scripting needs, and how AbleSet can drive
> the pedals. Checked against vendor docs on 2026-10-11.

## What's installed

| App | Version | Notes |
|---|---|---|
| Ableton Live 12 **Standard** | 12.2.2 | Main install. No prefs folder for 12.2.2 yet (latest is 12.2.1), so it may not have been launched since updating |
| Ableton Live 12 **Intro** | 12.2 | Leftover; redundant with Standard |
| Max (standalone) | — | Not installed |
| AbleSet | — | Not installed |
| AbletonOSC | — | Not installed; no `Remote Scripts` folder in the User Library yet |

The current Live release is 12.4.x (12.4 added Link Audio). The local Live manual already
covers Link Audio, so it's ahead of the installed version.

---

## Scripting layers: what each needs

| Layer | Needs | Status |
|---|---|---|
| **Python control scripts** ("MIDI Remote Scripts") | Any Live edition | ✅ Live bundles its own Python; create `~/Music/Ableton/User Library/Remote Scripts/` |
| **AbletonOSC**: a free control script that exposes Live over OSC | Any Live edition | ❌ Easiest way for outside scripts, agents or AbleSet to drive Live |
| **Max for Live**: custom devices inside Live, using Live's internal API | Live Suite, or the Max add-on for Standard | ❌ Not needed for this rig (see below) |
| **AbleSet** | All editions of Live 10–12; Live 11+ for section clips and lyrics tracks | ❌ Works with Standard; its Max for Live controller is optional and "isn't needed anymore" |
| **AbleSet scripting / OSC Tracks** | AbleSet **Pro** | ❌ |

### What Max for Live would add
- Devices saved with the set that process audio or MIDI, with a UI.
- Access to Live's internals from inside a device: tracks, clips, locators, tempo,
  parameters. Not sample-accurate.
- Suite's Max for Live devices: LFO, Envelope Follower, Shaper, Expression Control,
  Connection Kit (OSC), CV Tools, plus maxforlive.com.
- **Custom MIDI logic** that plain clips can't do:
  - stateful footswitches (tap, hold, double-tap)
  - conditions ("only in the chorus")
  - MIDI sent when the playhead reaches a locator or section
  - chord detection from guitar MIDI
  - MIDI ↔ OSC
  - SysEx (the VE-500's SysEx spec isn't published, so this doesn't help with it)

None of the rig plan needs it. Standard sends program changes and CCs from MIDI clips
([Live §8.3.2](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L4257), CC clip
envelopes [§26.4](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L9941)). Many
foot controllers handle tap/hold and message bursts themselves. Suite's 30-day trial
includes Max for Live if you want to try it.

---

## AbleSet → devices over OSC and MIDI

AbleSet can **send** OSC and turn OSC into MIDI, so it can control both network gear and
the MIDI-only pedals (VG-800, VE-500, GM-800).

### OSC out (network devices: TouchOSC, mixers, lighting, video)
- **OSC Tracks:** a MIDI track whose name contains `+OSC`. Each clip's name is a command,
  sent when the playhead reaches it, e.g. `192.168.1.5:3000/scene 2`. Chain commands with
  `;` and add pauses with `//sleep 2500`. Track-name attributes set a default target or
  prefix: `External +OSC [192.168.1.25:3000]`.
- **OSC Connections:** name a target once in settings, then send `:X32/ch/1/mix/on 1`. A
  Listen Port receives values for Canvases and scripts.
- **MIDI mapping:** a footswitch can fire a custom OSC command.
- **Scripts** (Pro).

### MIDI out (the pedals)
AbleSet sends MIDI to any MIDI output on the computer:

```
/midi/send/pc   [output] [channel] [program]
/midi/send/cc   [output] [channel] [controller] [value]
/midi/send/note [output] [channel] [note] [velocity] [duration]
/midi/send/raw  [output] [data]          # e.g. "F0 … F7"
```

`/midi/outputs` lists the port names. An OSC Track clip named, for example,
`/midi/send/pc "VE-500" 1 12` changes the VE-500 patch when the playhead reaches it. In
scripts the same commands are `sendMidiPc()`, `sendMidiCc()` and so on. The pedals still
need a MIDI or USB connection to the computer.

### Controlling Live itself
AbleSet has a built-in setup for **AbletonOSC**: send to `127.0.0.1:11000`, listen on
`11001`, and add `start_listen` commands to "OSC on Create". This reaches almost anything
in the Live set.

### Other inputs
- AbleSet Standard and Pro **listen** for OSC on port **39051**, advertised over Bonjour.
- **AbleSet Connect** on the iPad can make MIDI devices plugged into the iPad available to
  AbleSet, natively or over RTP MIDI.

### Live clips vs AbleSet for program changes and CCs

| | Live MIDI clips | AbleSet (OSC Tracks / scripts) |
|---|---|---|
| Timing | Tightest, in time with playback | Fires when the playhead reaches the clip; looser, fine for patch changes |
| Jumping into the middle of a song | Earlier program changes aren't re-sent, so a pedal can be left on the wrong patch | A script can send a known state on every song or section change |
| Network (OSC) devices | ❌ | ✅ |
| Needs | Live Standard | AbleSet Pro |

**Recommended split:**
- Put per-section program changes and CCs in Live MIDI clips.
- Use an AbleSet Pro script to send a known-state burst on each song change.
- Use OSC Tracks for network gear.

### AbleSet tiers (ableset.com, 2026-10-11)

| Tier | Price | Activations | Adds |
|---|---|---|---|
| Intro | $129 | 1 | Setlist, multi-file projects, MIDI mapping, spoken cues, one lyrics track |
| Standard | $179 | 2 | Unlimited lyrics, AbleNet (redundant computers), audio-interface support, OSC control, Stream Deck |
| Pro | $269 | 3 | Mixer, Canvas, **OSC Tracks**, **scripting**, LTC Display |

Upgrades cost the price difference (Standard → Pro: $90). The trial is unlimited, but
playback stops every 15 minutes. The docs don't say which tier OSC Connections and
MIDI-mapped custom OSC need on their own, so check in the trial.

---

## Manuals

### Ableton Live 12 (local)
[Ableton-Live-12-Manual.md](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md)
(PDF alongside; online at <https://www.ableton.com/en/manual/>). Sections that matter here:

| Topic | Section |
|---|---|
| Launching the Arrangement with locators | [§6.4](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L3341) |
| Arrangement loop | [§6.6](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L3415) |
| MIDI clip bank and program change controls | [§8.3.2](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L4257) |
| External MIDI in/out | [§17.3](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L7229) |
| External Instrument device | [§30.6](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L14513) |
| MIDI controller clip envelopes | [§26.4](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L9941) |
| Max for Live | [§31](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L16749), devices [§32](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L16867) |
| MIDI remote control / control surfaces | [§33.1](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L17531) |
| Link, Tempo Follower, MIDI sync | [§36](../../../data/manuals/daw-video/Ableton-Live-12-Manual.md#L20037) |

### AbleSet (local mirror)
[AbleSet/INDEX.md](../../../data/manuals/daw-video/AbleSet/INDEX.md), 31 pages mirrored from <https://ableset.com/docs/> by
`scripts/fetch_ableset_docs.py`. Re-run with `--force` to refresh.

| Topic | Page |
|---|---|
| FAQ (compatibility, licences) | [faqs.md](../../../data/manuals/daw-video/AbleSet/faqs.md) |
| Controlling AbleSet via OSC (incl. sending MIDI) | [osc.md](../../../data/manuals/daw-video/AbleSet/osc.md) |
| OSC Connections (incl. AbletonOSC) | [osc-connections.md](../../../data/manuals/daw-video/AbleSet/osc-connections.md) |
| OSC Tracks | [osc-tracks.md](../../../data/manuals/daw-video/AbleSet/osc-tracks.md) |
| Scripting | [scripting.md](../../../data/manuals/daw-video/AbleSet/scripting.md) |
| MIDI mapping | [midi-mapping.md](../../../data/manuals/daw-video/AbleSet/midi-mapping.md) |
| Controllers (Stream Deck, etc.) | [controllers.md](../../../data/manuals/daw-video/AbleSet/controllers.md) |
| AbleSet Connect (iPad) | [connect.md](../../../data/manuals/daw-video/AbleSet/connect.md) |
| AbleNet (redundancy) | [ablenet.md](../../../data/manuals/daw-video/AbleSet/ablenet.md) |
| Sections track, lyrics, guide tracks | [sections-track.md](../../../data/manuals/daw-video/AbleSet/sections-track.md), [lyrics.md](../../../data/manuals/daw-video/AbleSet/lyrics.md), [guide-tracks.md](../../../data/manuals/daw-video/AbleSet/guide-tracks.md) |

### Not yet in the knowledge base
- AbletonOSC: <https://github.com/ideoforms/AbletonOSC>
- Live Object Model / Max for Live API reference (Cycling '74)
