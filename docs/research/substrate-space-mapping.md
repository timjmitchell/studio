# Mapping the studio onto the SemOps substrate space

> **Status:** exercise, 2026-10-11 (issue #9). We're testing whether SemOps'
> [substrate space](https://github.com/semops-ai/semops-core/blob/main/docs/SUBSTRATE_SPACE.md)
> fits the [studio model](../studio/model.md). It may not fit fully, and that's fine. Nothing here
> changes the model yet.

## 1. The space in brief

SemOps lays out a company's data as a space with three axes:
- **X (across):** functions side by side.
- **Y (up and down):** a hierarchy, general to detailed.
- **Z (through):** the layers stacked at one place: **reference** (the framework's options),
  **solution** (what the company chose and runs), **data** (what its systems record).

Reference and solution, plus the edges between places, form the **control plane**: what we
think, and why. The data is the **data plane**: what is actually happening. Binding the data to
the solutions tests the assumptions.

A **projection** is a parallel copy of the space in a future state. It holds only its changes
and is read at the same addresses as the present.

## 2. Where it fits

| SemOps | Studio | Example (2026-10-11) |
|---|---|---|
| Z: reference → solution → data | §4 reference concepts → gear we own plus declared realizations (inventory, scenarios) → snapshots and probes | monitor mix → CUE 3 mirrored to Line 3-4 → wedge → snapshot: no mirror |
| Control plane vs data plane | the model's *declared vs observed* principle | |
| Y: hierarchy | SKOS broader / narrower | monitoring → monitor mix → wedge monitor mix |
| X: functions | the console sections in §4 below, or §7 Functions | input → insert → tape → return → monitor |
| A solution bound at many places, each with a role | one Product, many capabilities | the x8 at input, monitor mix and main mix |
| Edges between places | **wiring**: connections are edges in the graph (control plane) | `jhs-clover:xlr-out → snake 4 → x8 in-4` |
| Choice without data | declared, not observed | the `wedge-vocal-ideas` scenario |
| Data without a choice | observed, nothing declared | A7/A8 active; x8 VIRTUAL 3 → CUE 2; the Twin X LINE 3/4 mix |
| Assumed value | declared, and the data can't reach it | A6 "pad on" (line inputs don't report a pad) |
| "Never true, or true then changed?" | needs history: dated snapshots | was the wedge mirror ever set? |
| Projection | a planned rig; a dry run before a `set` | [one-man-band live rig](../studio/rigs/one-man-band-live-rig.md); "in-ears routed" |
| Standing projection (finding out what we have) | the open-questions list | issue #9 gaps, ❓ items, first-pass §13 |
| Realization depth: *solution named, nothing held* | gear known only from a manual | GM-800, TD-17 |
| Data with no reference address → the reference is missing an address | how our reference grows (§4) | |

## 3. Where the studio differs

**Wiring is an edge, tested by traversal.** A cable can't be read. A connection is a
control-plane edge, and it is tested by data at its ends:
- **Thunderbolt and USB edges** have their own data (`system_profiler`, `ioreg`).
- **Virtual routes** show in the engine and in `.uadmix` files.
- **Analog and RF edges** are tested only by signal: a meter moving at the far end.

A path is a chain of edges. Signal at the end confirms every edge on it, and silence points to
the first edge where the signal stops. The connection `confidence` field becomes how far an edge
has been tested: declared only → endpoints observed → signal traversed (🧪 with a date).

So meters aren't a gap in the data plane: they are how analog edges get tested.

The wedge shows the difference. The cable `x8 line-out-3 → wedge` may be fine. What's missing is
the binding upstream of it (no cue mirrored to Line 3-4). That's a different finding from "the
cable is wrong."

**The solution is a stack, not one layer.** SemOps' solution layer is thin: a named system object
bound at a place, emitting a table. Ours has levels, each with its own cost to change:

| Level | Example | Stored in | Changes |
|---|---|---|---|
| Product (a bundle of capabilities) | Apollo x8: 8 analog, 8 ADAT, 8 virtual, 2–4 cues | manual, factory port lists | never (firmware aside) |
| Unit | this x8, its serial number, firmware, Thunderbolt chain | the machine | rarely |
| Configuration | 3 cues, V1–4, I/O Matrix 44 in / 42 out, 48 kHz | the driver; I/O preset (`.uadio`) | rarely; disruptive (quit the DAW first) |
| Session | 13 visible strips, names, sends, mirrors, plugins | Console session (`.uadmix`) | per task |
| Live | unsaved tweaks, mutes, meters | the engine only | constantly |
| Code (the execution surface) | engine API, AppleScript, `scripts/*` | this repo | as we build |

The code level also has a SemOps role. **`ua_snapshot.py` is a materialization pipeline**: the
solution object that emits the data plane. Each script that reads a device is one.

Configuration, session and live are three records of one thing at different change costs, like
Edge's three records of the same clean. Where they disagree is useful: saved session vs engine
means unsaved changes.

**Owning a Product makes all of its capabilities available.** The solution binds only the subset
we use, so the agent searches across the whole set (and across other owned products) at a place,
not only what is bound or observed. That's how it can suggest things outside the snapshot. Each
suggestion says which level it changes, so cost is visible.

**We write back.** SemOps reads a company; the studio cascade acts on it. In these terms, a `set`
turns a projection into the present, and the read-back is the data that confirms it.

**The machinery is lighter.** SemOps is SQL over one database; we use TOML and scripts. The
concepts carry over; the machinery doesn't need to.

## 4. Deriving the reference from the solution

SemOps scaffolds its reference from frameworks (APQC, Porter, Greiner). We have no framework
driving the reference, so we **work backwards**: derive it from the solutions we have in hand, and
add an address when the gear shows a capability with no reference place. Anchoring on one
archetype keeps that consistent.

**The archetype for the audio path: an analog console plus a tape machine.** UA Console and the
DAWs both copy it, so it's the natural coordinate system.

| Console-and-tape section | UA Console | Logic (and Ableton) |
|---|---|---|
| **Input section** (mic pre, channel) | preamp + Unison, input strips | track input |
| **Insert points + outboard** | inserts (1176, VOXBOX) | plugin slots |
| **Patchbay** | I/O Matrix, Flex Routing | I/O assignments |
| **Tape send** (to the multitrack) | the driver inputs the DAW records | record-enabled track |
| **Multitrack machine** | (none) | the DAW |
| **Tape return / monitor path** | **virtual channels** | track outputs → the interface |
| **Aux / foldback sends** | cue sends, cue mirrors | sends, buses |
| **Subgroups** | (none) | summing stacks, buses |
| **Mixdown console** | (none) | the DAW mixer |
| **Control room / monitor section** | MONITOR, Twin X as controller, dim, alt | main out |
| **2-track master recorder** | (none) | bounce |

What this already shows:
- **"Virtual channel" gets a reference term: tape return.** §4.7 of the model said it had "no
  older generic term." Derived from the solution, it's the monitor return from the multitrack.
- **Patchbay** is the reference concept behind the I/O Matrix and Flex Routing, and probably
  behind the KHE amp switcher and the ES-8 loops (patchbays for amps and pedals).
- **Channel visibility has no counterpart in the archetype.** Hiding a strip is a view choice,
  which supports *hidden ≠ off*.

**Where the archetype runs out:** MIDI, instruments, the guitar rig, and Ableton's
live-performance side. These need other anchors ("the backline", "the stage"?), also derived from
gear we own.

### 4.1 Overlapping solutions: one section, several candidates

Two solutions often cover the same place. A DAW is built to be the input and monitor sections too
(Logic and Ableton *software monitoring*). Most setups are just an interface, its driver and the
DAW, with no separate routing UI.

In SemOps terms, several solutions can be bound at one place, and the **role** says which one
performs there. Here the role is a choice we make, and it's recorded:

| Section | Candidates | Role in this studio |
|---|---|---|
| Input + inserts (tracking) | UA Console (DSP, near-zero latency) · DAW | **UA Console** |
| Monitor mixes, control room | UA Console · DAW software monitoring | **UA Console** |
| Multitrack machine | DAW | **DAW** |
| Mixdown console, subgroups | DAW · UA Console | **DAW** |
| 2-track master | DAW bounce | **DAW** |

So in this studio **the DAW is the tape machine plus the mixing console**, and **UA Console is
the input and monitor sections**.

Why this matters to an agent:
- **Overlap is a hazard, not just a choice.** If both solutions perform at the same place, the
  signal is handled twice. For example, Logic software monitoring on while Console also monitors
  the input gives a doubled, delayed (phasey) signal. A check: at each place, at most one
  candidate *performs*. ❓ Read Logic's software-monitoring setting as data (preferences or
  AppleScript) so the check can run.
- **Suggestions can still use a non-performing candidate**, flagged as a change of role. For
  example, "use Logic's software monitoring for this overdub" would fit a setup that tracks
  through an amp-sim plugin only Logic can run.
- **The role is per scenario.** A future live rig (Ableton as the input and monitor console)
  would bind the roles differently. That's a projection.

### 4.2 Software instruments: the physical model, moved inside the DAW

The reference for a software instrument is **any instrument**. It makes sound, the sound goes
into an input channel (and its preamp), and it is recorded and monitored as if it were plugged
in with a cable or played into a mic. A plugin instrument on a channel is that same physical
model with its **location** moved inside the DAW. It isn't a different kind of thing.

The archetype separates three parts that a hardware box may combine:

| Part | Reference role | Outside the DAW | Inside the DAW |
|---|---|---|---|
| **Controller** | the player's interface; sends performance (MIDI) | keyboard, pads, a guitar through MIDI Guitar 3 | (on-screen keys, rarely) |
| **Sound source** | makes the audio | a synth, sampler or sound module | a software instrument plugin |
| **Sequencer** | records and replays performance data | a hardware sequencer playing a sampler | a MIDI track |

So:
- **A controller on USB/MIDI playing a plugin** keeps the controller outside the DAW and puts
  the sound source inside it. The MIDI cable or USB is an edge from controller to instrument.
  The instrument-to-channel audio edge becomes internal (virtual).
- **A MIDI track playing an instrument** is a sequencer playing a sampler, located in the DAW.
- **A software instrument channel** is an input section whose source is the instrument rather
  than a jack. Inserts, sends and monitoring work the same as for a mic channel.

Location becomes a property of the **binding** (inside or outside the DAW), not a separate
reference place. The questions an agent asks are the same either way: what makes the sound,
what's playing it, where does its audio enter a channel, and who monitors it (§4.1).

**Two things can be recorded.** In the physical archetype you record the audio. With a
sequencer you can also record the performance itself (the MIDI), and print the audio later.
That lines up with the model's Performance vs Recording split (§5), and it's where reamping
fits too: the clean DI is to the guitar what the MIDI is to a synth.

### 4.3 Patterns are compositions of console primitives

Modern DAWs and plugins have huge routing capabilities. Almost all of them could be done on an
old-school mixer with aux sends, extra channels and a lot of patching. The convenience is new;
the pattern is old.

**Example: side-chain compression.** Today it's a menu in the compressor, often with a key
filter or even a transient shaper on the trigger. On a console it's a composition:
- an aux send from the trigger source (kick) into the compressor's **key input**;
- for a filtered trigger, route that send through an EQ before the key input;
- the compressor sits on the **insert** of the channel being ducked (bass).

It's a giant pain to patch, but it's fully doable.

So the reference has two levels:

| Level | What | Examples |
|---|---|---|
| **Primitive** | a console-and-tape part (§4) | channel, insert, aux send, bus, key input, patchbay, tape send / return |
| **Pattern** | a named composition of primitives, with a purpose | side-chain compression, parallel compression, submix, monitor mix, reamping, a click only to the drummer |

A product capability **maps to a pattern** when it packages one (the side-chain menu, Logic's
summing stack). Otherwise the pattern can still be **composed** from the primitives a product
does have.

Why it matters to an agent:
- **More things are possible than the feature list shows.** If no owned product packages a
  pattern, the agent can build it from primitives: any channel, aux and insert that exists is a
  building block. That's another way to suggest solutions outside the snapshot.
- **Cost ranks the options.** A packaged capability is cheap: one setting, at session scope. A
  composition uses more resources (channels, sends, buses, DSP, ports that have to be free) and
  is harder to undo. Show both, packaged first.
- **The pattern is the stable address.** "Side-chain the bass to the kick" names the same place
  whether it's realized as a plugin menu in Logic or as a send-to-key-input patch through
  Console and outboard gear. This is the reference coordinate, and the products bind to it.
- **Decomposing explains behaviour.** Breaking a packaged feature back into primitives
  explains latency, gain staging and why something is silent (no signal reaching the key input
  is a missing edge).

## 5. Open questions

- **X axis:** are the console-and-tape sections, §7 Functions, or both the "across" axis?
- **Model wording:** v0.4 used "layer" for configuration / session / live, which clashes with
  reference / solution / data. Proposed: call those **scope** and keep "layer" for SemOps' sense.
- **Coverage report:** for a drift check, report bindings as confirmed / contradicted /
  hypothesis / unbound (assumed). Unbound is the dangerous case: wrong but hidden.
- **Meters:** add meter reads to the snapshot so analog edges can be tested by signal.
