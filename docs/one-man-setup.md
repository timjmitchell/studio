# Live Performance Rig — Design Summary

## Philosophy
Solo singer-guitarist performing original songs. Technology should be invisible — the aesthetic is "guy with a guitar." Loops and backing elements support the songs rather than define them. Maximum setup and debugging at home; arrive at the gig and be ready in 10 minutes.

---

## Signal Chain Overview

### Electric Guitar
- Guitar → **GK-5 divided pickup** (Serial GK cable) → **Boss VG-800**
- Guitar → standard instrument cable → VG-800 regular input (for blending when needed)
- VG-800 handles: amp sim, FX, synth sounds, string splits, alternate tunings
- VG-800 MIDI out → interface → Ableton (pitch-to-MIDI from hex pickup)
- VG-800 audio out → interface → Ableton + PA

### Acoustic Guitar
- Guitar → **NUX Optima Air** (acoustic IR + preamp) → interface → Ableton + PA
- Completely independent chain — VG-800 never sees the acoustic signal
- Guitar swap on stage = switching between chains; Ableton scene handles the context

### Vocals
- Mic → **Boss VE-500** (compression, reverb, delay, occasional harmony)
- Harmony key programmed per song via Ableton MIDI program changes
- VE-500 audio out → interface → Ableton + PA

---

## Hardware

| Device | Role |
|--------|------|
| Boss GK-5 | Divided pickup on electric guitar |
| Boss VG-800 | Guitar modeling, synth, FX, pitch-to-MIDI |
| NUX Optima Air | Acoustic IR and preamp |
| Boss VE-500 | Vocal processing and harmony |
| MOTU M4 | Audio interface — 4 in, 4 out, MIDI in/out, USB-C |
| Foot controller | Ableton transport backup — stop, start, panic |
| Akai Launchkey Mini | Direct Ableton control at station |
| iPad + AbleSet | Song navigation and setlist management |

---

## Audio Routing

### Interface Outputs
- **Outputs 1/2** → PA (audience mix)
- **Outputs 3/4** → IEM mix (private monitor)

### Interface Input Allocation (fully utilized)

| Input | Source |
|-------|--------|
| 1 | VG-800 L (electric guitar chain) |
| 2 | VG-800 R (electric guitar chain) |
| 3 | NUX Optima Air (acoustic guitar) |
| 4 | Boss VE-500 (vocals) |

⚠️ All 4 inputs are allocated — no headroom for additional sources without mixing down upstream or upgrading interface.

### IEM Notes
- MOTU M4 front panel headphone output serves as outputs 3/4 — convenient direct IEM feed without a separate headphone amp
- Wired IEM connects directly to MOTU M4 headphone jack
- If wireless IEM needed later, feed from outputs 3/4 to IEM transmitter

### IEM Mix Contains
- Different blend than PA
- Click track
- Voice cues (spoken or tonal) — pre-recorded
- First-note cues where needed

Cue tracks in Ableton are routed exclusively to outputs 3/4 — they never touch outputs 1/2 and are completely inaudible to the audience.

---

## MIDI Architecture

### Ableton → Pedals (automated, per song/section)
- **Program changes** to VG-800 and VE-500 at scene/song transitions
- **CC messages** to VG-800 for within-song automation:
  - Mute/unmute regular guitar input
  - Mute/unmute synth layer
  - Switch amp model or effect state
- MIDI clips on dedicated tracks handle all outgoing messages — no manual intervention required during performance

### Controllers → Ableton
- **Foot controller** → transport backup (stop, start at beginning, panic/all-notes-off)
- **Launchkey Mini** → direct clip triggering, extras, manual override
- **iPad/AbleSet** → song navigation, setlist view

### Backup
- VG-800 footswitches available for manual patch changes if Ableton MIDI fails
- VE-500 footswitches available for manual preset changes
- Foot controller panic scene resets all CC values and sends all-notes-off

---

## Ableton Architecture

### Approach
Arrangement View as primary mode — each song has a real timeline. The full set lives in one Arrangement file; songs play in sequence with gaps for stage banter.

### Per-Song Structure
- Pre-recorded loops as audio clips — recorded at home with the same signal chain, triggered at the right bar
- "Extras" — optional one-shot clips that can be fired or ignored in the moment
- MIDI clips on dedicated tracks fire program changes and CC messages automatically at defined bars
- Arrangement Looper (Performance Pack) available to extend sections if a song is going well

### Song Navigation
- AbleSet on iPad provides clean song-by-song view
- Foot controller steps through songs
- Scene launch quantization set to bar-level so transitions never happen mid-beat

### Ableton Track Layout (sketch)
| Track | Content |
|-------|---------|
| Loop | Pre-recorded loop audio per song |
| Pad / Texture | Optional ambient layer |
| Extras | One-shot optional clips |
| MIDI Out — VG-800 | Program changes + CC automation |
| MIDI Out — VE-500 | Program changes (key, preset) |
| Click | Routed to outputs 3/4 only |
| Cues | Voice/note cues, routed to outputs 3/4 only |

### Laptop Stability
- Dedicated Ableton template, nothing else open
- Airplane mode, Do Not Disturb locked
- One file, loaded before soundcheck, not touched again

---

## Within-Song Switching (Electric)
The VG-800 supports multiple configurations within a song via Ableton-driven MIDI:

- **Clean electric section** → CC mutes synth layer, regular guitar input active, amp sim patch
- **Synth section** → CC unmutes synth, mutes or blends regular input
- **Transitions** written into Arrangement timeline — happen automatically at the right bar
- **Foot controller** available as manual override if automation fails

---

## Open Questions / Next Steps
1. Verify VG-800 CC implementation in detail (which CC numbers map to which functions)
2. Confirm AbleSet compatibility with current Ableton Live 12 version
3. Choose specific foot controller (4-button minimum: next song, previous, stop, panic)
4. Evaluate wired vs wireless IEM — depends on how much you move on stage
5. Acoustic guitar — confirm NUX Optima Air output level is line-level compatible with interface input
6. Build and test one complete song in Ableton before designing the full set template
