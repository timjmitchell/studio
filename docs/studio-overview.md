# Studio Overview

A one-page summary of the studio: where things are, what's in it, and how signal moves
through it. For detail, see the [first-pass notes](inventory-first-pass.md) (findings, settings, open
questions) and [inventory/](../inventory/README.md) (structured data).

*Last updated 2026-10-11.*

## Where things are

- **The desk** is the working position. The Apollo Twin X is used there as the monitor
  controller, with the headphones plugged into its front jack.
- **On the floor:** the snake's box, where mics plug in, so you don't have to reach behind
  the desk. The snake's tails run behind the desk into the Apollo x8.
- *Not documented yet:* the room layout, and where the x8, Satellite, drives, monitors, wedge
  and pedalboard physically sit.

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
- **Mics:** plug into the snake box on the floor, which feeds x8 inputs 1–4. Input 1 is
  usually the dynamic mic and input 3 the condenser.
- **Guitar:** the OX Amp Top Box goes to x8 inputs 5–6. The pedalboard and a guitar DI go to
  the Twin X inputs.
- **The computer:** Logic's main output returns to Console on Twin X virtual 1/2. Mac system
  audio (browser, YouTube) returns on x8 virtual 1/2. x8 virtual 3/4 is spare, used for a DAW
  submix (e.g. drums) when one element needs its own level in a monitor mix.

**Outputs**
- **Speakers:** the main mix goes to the HR824s from the x8 monitor outputs. The Twin X's knob
  controls the level and switches between speakers and headphones.
- **Monitor mixes** (UA calls them cues) are separate listening mixes:
  - **Headphones** (Twin X headphone out): normally hear the main mix.
  - **Wedge** (x8 output 3): its own mono mix, for rehearsing or singing vocal ideas.
  - **In-ears** (x8 outputs 7/8 → PSM300): its own mix when needed. *Not routed at the
    moment.*

## Typical setups

| Doing | Listening on | Mix |
|---|---|---|
| Tracking or mixing at the desk | MDR-7506 headphones or the HR824s | Main mix |
| Rehearsing, or singing vocal ideas | Turbosound wedge | Own monitor mix (mono) |
| Recording or rehearsing on in-ears | PSM300 | Own monitor mix |
| Tracking with more of one element | Headphones | Monitor mix with a DAW submix on its own fader |
