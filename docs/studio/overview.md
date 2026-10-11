# Studio Overview

A one-page summary of the studio: where things are, what's in it, and how signal moves
through it. For detail, see the [first-pass notes](inventory-first-pass.md) (findings, settings, open
questions) and [inventory/](../../data/inventory/README.md) (structured data).

*Last updated 2026-10-11.*

## Where things are

The studio is a **basement room, about 20 × 14 ft**.

- **The desk** sits against a wall, offset from the door. It's the working position and holds
  the Mac Studio, the Mackie HR824 monitors, all the UA hardware (Apollo x8, UAD-2 Satellite,
  Apollo Twin X as the monitor controller), the Novation Launchkey Mini, the Shure PSM300
  in-ear base unit, the Samsung X5
  (the main audio drive) and the ThunderBay RAID enclosure (backup).
- **Rolling shelves on the wall to the left of the desk** hold the guitar amps (1965 Fender
  Bassman, 1973 Hiwatt DR103, Dr. Z Maz 18 Jr., Orange OR15, 1981 Fender Princeton Reverb II),
  the KHE amp/cab/FX selector, the UA OX and a Weber speaker-impedance switcher.
- **The floor beneath those shelves** has the pedalboard, built around a Boss ES-8 switcher.
- **Behind the desk seat** is the Roland FP-30X digital piano. It feeds a DI box into snake
  channel 5 (mono), but channel 5's tail isn't plugged in at the moment.
- **The snake box** is on the floor, so mics plug in there; its tails run behind the desk into
  the x8.
- *Not placed yet:* the wedge, the mics, guitars, headphones storage, the Anker dock.

## Main devices

| Role | Device |
|---|---|
| Computer | Mac Studio (M1 Max, 32 GB) |
| Audio interfaces | **Apollo x8** (main I/O) + **Apollo Twin X** (desk, monitor control) + **UAD-2 Satellite** (extra DSP), chained over Thunderbolt and run together in **UAD Console** |
| DAWs | **Logic Pro** (main), Ableton Live 12, LUNA |
| Speakers | **Mackie HR824** pair |
| Headphones | **Sony MDR-7506** |
| Wedge | **Turbosound** powered floor monitor |
| In-ears | **Shure PSM300** wireless |
| Mic inputs | **Gator** 6-channel snake → x8 mic inputs 1–4 |
| Guitar | Pedalboard, **UA OX Amp Top Box**, guitar DI |
| Vocal processor | **Boss VE-500** (connected over USB) |
| Storage | ThunderBay 4 RAID, Samsung X5 (Logic projects) |

Also owned but not part of the everyday routing: Boss GM-800, Roland TD-17 e-drums, Roland
FP-30X piano, Akai MPK249 and Novation Launchkey controllers, and a pedal collection. See
the [first-pass notes](inventory-first-pass.md).

## How signal moves

**UAD Console is the hub.** It works like the input-and-monitor section of a traditional
console. Everything you play or sing comes into the Apollos, gets monitored through Console
with almost no latency, and is recorded into the DAW. The DAW's playback comes back into
Console on its own fader, so it can be balanced against the live inputs.

```text
 mics → snake ─────────────┐
 OX Amp Top Box ───────────┤                ┌─→ Logic (recording)
 pedalboard, guitar DI ────┼─→ Apollos ─────┤
                           │   (Console)    └─← Logic playback, Mac system audio
                           │        │
                           │        ├─→ main mix ──→ HR824 speakers
                           │        ├─→ monitor mix ──→ MDR-7506 headphones (Twin X)
                           │        ├─→ monitor mix ──→ Turbosound wedge (x8 out 3)
                           │        └─→ monitor mix ──→ PSM300 in-ears (x8 outs 7/8)
```

**Inputs**
- **Mics:** plug into the snake box on the floor, which feeds x8 inputs 1–4. A Shure SM58 is
  on channel 1 (x8 input 1) and a Roswell K67x condenser, set up in a corner of the room, is
  on channel 3 (x8 input 3).
- **Guitar:** everything goes through the pedalboard's **Boss ES-8**, which has three outputs
  (chosen per patch):
  - **OUT 1** → the **KHE** amp/cab switcher → the selected amp (Princeton, Maz 18 Jr. or
    OR15) → the **OX**, always in the KHE's attenuator insert → the Princeton's speaker. The
    OX's emulated line outs feed **x8 inputs 5–6**.
  - **OUT 2** → just loop 6, the **TONEX** amp modeller.
  - **TUNER out** (before any effects) → Peterson tuner → **JHS Clover** DI → snake channel 4
    → **x8 input 4**. This is a clean direct signal, recorded as a backup for reamping or used
    for MIDI Guitar 3 and synths.
- **The computer:** Logic's main output returns to Console on Twin X virtual 1/2. Mac system
  audio (browser, YouTube) returns on x8 virtual 1/2. x8 virtual 3/4 is spare, used for a DAW
  submix (e.g. drums) when one element needs its own level in a monitor mix.

**Outputs**
- **Speakers:** the main mix goes to the HR824s from the x8 monitor outputs. The Twin X's knob
  controls the level and switches between speakers and headphones.
- **Reference correction:** the speakers and headphones are EQ'd toward flat with **SoundID**,
  integrated into Console (Apollo Monitor Correction). There's a calibrated profile for the
  HR824s and one for the MDR-7506s.
- **Monitor mixes** (UA calls them cues) are separate listening mixes:
  - **Headphones** (Twin X headphone out): normally hear the main mix.
  - **Wedge** (x8 output 3): its own mono mix, for rehearsing or singing vocal ideas.
  - **In-ears** (x8 outputs 7/8 → PSM300): its own mix when needed. *Not routed at the
    moment.*

## Planned rigs

- [One-man-band live rig](rigs/one-man-band-live-rig.md): a potential future setup for solo
  shows (Ableton, modelling guitar rig, VE-500, IEMs). Not built yet.

## Typical setups

| Doing | Listening on | Mix |
|---|---|---|
| Tracking or mixing at the desk | MDR-7506 headphones or the HR824s | Main mix |
| Rehearsing, or singing vocal ideas | Turbosound wedge | Own monitor mix (mono) |
| Recording or rehearsing on in-ears | PSM300 | Own monitor mix |
| Tracking with more of one element | Headphones | Monitor mix with a DAW submix on its own fader |
