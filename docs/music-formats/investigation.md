# Headless agentic reading of music formats — investigation

Goal: let an agent read/reason over MIDI, tablature (`.gpx`, ASCII/txt tab),
notation, and other score formats to **extract, translate, and convert**.

Status: reference only (no pipeline built yet). Drop example files in
`docs/music-formats/examples/` and we can prototype against them.

## Core insight

An LLM can't reason over binary MIDI or a zipped `.gpx` directly. The pattern
that works — and that `scripts/midi_dump.py` already demonstrates — is:

> a **deterministic parser** converts the opaque format into a flat **text**
> representation, and the agent reasons over the text.

So the whole problem decomposes into: *format ↔ headless converter ↔ the text
form that's best to reason over.*

## Format landscape

| Format | What it is | Headless read | Agent-friendliness |
|---|---|---|---|
| MIDI (`.mid`) | performance events (note on/off, tempo, CC); no notation semantics | `mido` (in use), `pretty_midi`, `music21`, `symusic` (fast) | High once dumped to text; no barlines/spelling unless inferred |
| MusicXML (`.xml`/`.mxl`) | full notation — pitch, rhythm, staves, lyrics, tab | `music21`, raw XML (lxml) | **Highest** — already semantic text/XML. Logic exports these |
| Guitar Pro (`.gp`, `.gpx`, `.gp5`) | tab + notation, binary/zip | `PyGuitarPro` (gp3–gp5 only), AlphaTab (JS, incl. `.gpx`/`.gp`), TuxGuitar CLI | Medium — parse then serialize to our own text/ASCII tab |
| ASCII/txt tab | what `docs/one-man-band/songs/*` use | regex/custom parser, or ABC bridge | LLM reads directly; *lossless* parse (timing) is genuinely hard |
| ABC notation | compact text notation | `music21`, `abcjs`, `abc2midi` | High — text-native; LLM can read *and write* it |
| MEI | scholarly XML notation | `music21` (partial), `verovio` | High (XML), niche |
| Lilypond (`.ly`) | text engraving source | text + `lilypond` CLI | High to read/write; renders to PDF/PNG/MIDI |

## The library that ties it together

**`music21`** (MIT, pure-Python, `uv add music21`) is the hub: parses
MusicXML/MIDI/ABC/MEI into a queryable object model (notes, chords, keys, time
signatures, measures), does analysis (key detection, `chordify`, roman-numeral
harmony, transposition), and writes back to MusicXML / MIDI / Lilypond / text.
Natural engine for "extract, translate, convert."

Supporting cast:
- `symusic` / `pretty_midi` — fast MIDI feature extraction (piano-roll, beats)
- `PyGuitarPro` + AlphaTab — Guitar Pro on-ramp (`.gpx` needs AlphaTab or
  TuxGuitar; PyGuitarPro tops out at gp5)
- `verovio` / `lilypond` — render notation to PNG/PDF/SVG so the agent (or you)
  can *see* the score

## Candidate workflows for this repo

1. **Score → structured summary.** Agent reads a MIDI/MusicXML dump → key,
   tempo map, section markers, chord progression (`chordify`), arrangement
   notes. Good for one-man-band charts. (`arbitrary-overlord` already carries a
   rich tempo map + a "Drums" marker to test against.)
2. **Tab ⇄ notation ⇄ MIDI round-trip.** Turn a markdown ASCII tab into MIDI to
   hear it; or turn a Logic MIDI export into clean ASCII tab / chord charts.
3. **Harmonic / section analysis → lead sheet or Nashville-number chart.**
4. **Transpose / re-voice / capo math** — deterministic in `music21`,
   agent-orchestrated across a batch of songs.
5. **Guitar Pro import** — `.gp`/`.gpx` → our markdown-tab convention so
   everything lives as text in the repo.

## Honest limitations

- **MIDI has no notation semantics** — no "dotted eighth in 6/8." Quantization
  and note spelling are inference, sometimes wrong. MusicXML avoids this, which
  is why the Logic `.xml` exports are the best raw material.
- **Lossless ASCII-tab parsing is the hardest** — rhythm is only weakly encoded
  in spacing. LLM *reading* tab is easy; a *faithful* tab→MIDI parser is fiddly.
- **`.gpx` specifically** needs AlphaTab (JS) or TuxGuitar; PyGuitarPro won't
  open the newer container.

## What exists here already

- `scripts/midi_dump.py` — `mido`-based MIDI→text dumper (the pattern above)
- `docs/hot-fog/midi/` — `.mid`, dumped `.txt`, and a Logic MusicXML `.xml`
- `docs/one-man-band/songs/*` — ASCII tab / chords / lyrics in markdown

## Next step

Provide example files (a `.gpx`, a couple of tabs, a MIDI/MusicXML pair) in
`docs/music-formats/examples/`. First prototype to consider: extend
`midi_dump.py` with `music21` to emit a structured markdown summary (key, tempo,
sections, chords) — validated against `arbitrary-overlord`.
