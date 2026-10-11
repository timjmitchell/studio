# Named techniques: seed log

> **Status:** seed log, started 2026-10-11. This may grow into its own project. The entries
> capture the basic idea only.

## Why log these

A **named technique** is a reusable recipe, usually named after a person, studio or label,
whose name has become common language (like "1176-style"). In the [Studio
Model](../studio/model.md) each one is a **Technique** (§6.14) with:

- **an origin**: people, place, era;
- **a recipe**: the idea in reference-layer terms (send, EQ, compressor, reverb, mic array,
  arrangement);
- **an intended result**: traits ("punch", "air", "solid centre image");
- **realizations**: how this studio can do it with what's owned.

So "do the Abbey Road reverb trick on the vocal" becomes: look up the recipe → find the owned
Products for each step → propose a routing in Console or Logic.

---

## 1. Abbey Road reverb trick

- **Origin:** Abbey Road Studios (EMI), 1960s.
- **Idea:** put an **EQ before the reverb** on the reverb send, and roll off the **lows and
  highs** (roughly: high-pass in the hundreds of Hz, low-pass around 10 kHz). Return it 100%
  wet.
- **Result:** reverb that doesn't muddy the low end or hiss, and sits behind the source.
- **Here:** Console AUX → EQ → **Pure Plate**; or a Logic bus → Channel EQ → ChromaVerb /
  Space Designer.

## 2. New York compression ("NYC trick")

- **Origin:** New York studios, 1980s–90s.
- **Idea:** **parallel compression**. Send drums or vocals to an aux, compress it hard (an
  1176 or SSL bus comp), often boost lows and highs on that aux, and blend it **under** the
  dry signal.
- **Result:** punch and weight, while keeping the transients.
- **Here:** Console AUX or a Logic bus + UAD 1176 / SSL G Bus + EQ.

## 3. Motown EQ / the Motown trick

- **Origin:** Hitsville U.S.A. (Motown, Detroit), 1960s; custom EQs.
- **Idea:** a parallel path with a strong **presence boost** (around 5–8 kHz) and heavy
  compression, blended back. Also cut the lows on everything except kick and bass.
- **Result:** forward, bright, clear on small radio speakers.
- **Here:** UAD **Hitsville EQ** / **Hitsville EQ Mastering** and **Hitsville Reverb
  Chambers** are installed.

## 4. Decca Tree

- **Origin:** Decca Records, 1950s, for orchestral stereo.
- **Idea:** three omni mics in a **T**: two spaced apart, one forward in the centre, high
  above and behind the conductor.
- **Result:** wide, natural stereo with a solid centre.
- **Model note:** the Studio Ontology uses the Decca Tree as its example of a
  `MicrophoneArrangement`.

## 5. Glyn Johns method

- **Origin:** Glyn Johns (The Who, Led Zeppelin, The Rolling Stones).
- **Idea:** **four-mic drums**: kick, snare, one overhead above the snare, and one side mic
  by the floor tom. The overhead and side mic sit the same distance from the snare to keep
  phase coherent.
- **Result:** a big, cohesive kit sound from few mics.
- **Here:** the 4 snake channels → x8 mic inputs 1–4 are exactly four mics (acoustic kit
  only).

## 6. Wall of Sound

- **Origin:** Phil Spector with Larry Levine, Gold Star Studios, LA, 1960s.
- **Idea:** many musicians **doubling the same parts** in one room, tracked live through an
  echo chamber, and layered.
- **Result:** a dense, roaring wash that sounds huge on the radio.
- **Model note:** an arrangement-and-tracking approach, not a signal chain. A Technique must
  allow more than signal-flow steps.

---

## Candidates to add later

- Stereo-mic arrays: Blumlein pair, ORTF, XY, mid-side
- Recorderman drum overheads
- Double tracking / ADT (Abbey Road's Automatic Double Tracking)
- Sidechain "pumping"
- The "Pultec trick" (boost and cut the same low frequency)
- "All buttons in" on an 1176. That's a named **State** of the 1176 rather than a technique,
  but it's named the same way.
