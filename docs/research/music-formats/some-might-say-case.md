# Case study: four files for one song ("Some Might Say", Oasis)

Tested 2026-10-12 against the files in
[music/one-man-band/some-might-say/](../../../music/one-man-band/some-might-say/) and the Logic
session `/Volumes/Samsung_X5/Oneman Band/some-might-say-oasis/`. Every claim below was run
unless it's marked otherwise (🧪 tested · 🔶 inferred · ❓ to test). See also the general
[investigation](investigation.md).

## The sources

| Source | What it really is | What's in it | Read it with | Result |
|---|---|---|---|---|
| `some might say.mid` | Standard MIDI, type 1, 480 ticks per beat, 7 tracks, 334.7 s | Rhythm gtr, lead gtr, bass, tambourine, drums, claps. 109 bpm, 4/4, **section markers** (Intro, Verse 1, Pre-Chorus, Chorus, …). No lyrics | `mido`, `music21` | 🧪 Clean |
| `Oasis - Some Might Say (ver 7 by fguzramm).gp` | Guitar Pro 7 (`VERSION` = 7.0): a zip holding `Content/score.gpif`, plain XML of about 10 MB | **13 tracks**: drums, bass, 2 leads, overdriven, clean, 2 "extras", vocal melody plus 2 harmonies, claps, tambourine. Tunings, 150 bars, 108 bpm, **10 named sections**, string/fret, techniques (bends, hammer-ons, slides), 47 chord diagrams. Chord labels are sparse. **No lyrics** | Our own XML parsing (stdlib), or alphaTab (Node) | 🧪 Clean, and the richest source |
| `some might say chords.pdf` | Ultimate Guitar page printed by jsPDF, 2 pages, **image only (no text layer)** | Lyrics with chords above them, section tags, 10 chord diagrams | Vision model (reading the page image) or macOS Vision OCR | 🧪 Vision model: accurate, keeps chord positions. OCR: words fine, chord columns lost |
| `some might say tab.pdf` | Ultimate Guitar page printed by jsPDF, 5 pages, image only. This is the "text tab", an ASCII tab by wuggle15, rendered as a picture | Guitar ASCII tab by section | Vision model reading the image | 🧪 OCR garbles it (`0|---7`, `А|`, `B1--`). A vision model reads it, but transcribing 5 pages is slow and error-prone |
| Logic session | `some-might-say-oasis.logicx`, 48k, plus the audio file and 4 stems (`_Vocals`, `_Drums`, `_Bass`, `_Guitar`, each 333.5 s) | The real recording, split into stems | `afinfo`, project `MetaData.plist`, AppleScript (UI) | 🧪 File facts read fine. ⚠️ The saved project (22:34) predates the stem split (22:41). Its saved tempo (63.07) and key (C♯m) look like auto-detection, so don't trust them |

No duplicates: the repo copies have the same MD5 hashes as the originals in `~/Downloads`.

Lengths: MIDI 334.7 s · GP ≈ 150 bars at 108 bpm · stems 333.5 s · album MP3 (RAID) 329.0 s · source
`.aif` 337.4 s. They're close but not identical, so **nothing lines up with the audio
automatically** (see "Lining up with the recording").

## What we can do (tested)

| From → To | How | Result |
|---|---|---|
| GP → ASCII tab (any track, any bars) | Parse `score.gpif`: MasterBar → Bar → Voice → Beat → Note (string/fret) + Rhythm | 🧪 Lead Guitar 1 solo bars render with bends, hammer-ons and slides, and match the UG tab's phrasing |
| GP → sections, chord labels per bar | `MasterBar/Section`, `Beat/Chord` → the track's diagram names | 🧪 Sections are complete. Chord labels exist only where the tabber added them |
| GP → MIDI (all 13 tracks) | alphaTab `MidiFileGenerator` (Node, nvm) | 🧪 168 KB MIDI written. Logic can import it (Logic can't open `.gp`) |
| Write GP / alphaTex | alphaTab `Gp7Exporter`, `AlphaTexExporter` | 🔶 The exporters exist in the library. Not run yet |
| MIDI → text dump | `scripts/midi_dump.py` | 🧪 (existing) |
| MIDI → chord names per bar | `music21` `chordify()` → `chordSymbolFromChord` | 🧪 Bars 9–24: D D Bsus2 Bsus2 G D A A … , which matches the PDF intro. Bars 1–8 (feedback intro) come out as noise |
| MIDI → MusicXML (one part) | `music21` | 🧪 Bass part written. Notation is inferred from performance timing, so expect some odd spellings and rhythms |
| MIDI → key | `music21` `analyze('key')` | 🧪 Said **G major**, which is wrong (the song centres on D). Don't trust automatic key detection on rock I–IV–V songs |
| Chord PDF → chord-over-lyric text | Vision model reads the page | 🧪 Accurate. This is the only source with lyrics |
| PDF → text with OCR | `ocrmac` (macOS Vision, via `uv`) | 🧪 Lyrics are usable. Chord columns and tab are not. Good for "what words", bad for "where" |

Tooling notes:
- No Homebrew was needed. `pypdfium2` + `pillow` render PDF pages, `ocrmac` does OCR, and
  `music21` and `mido` run via `uv run --with`. alphaTab is `npm i @coderline/alphatab` under nvm.
- PyGuitarPro can't open this file: it only handles gp3–gp5, and this one is GP7.
  `.gp3`/`.gp5` files (there are several Oasis ones in `~/Downloads`) would also work with
  PyGuitarPro.

## Mix and match: what combining the sources gives us

1. **Song doc and chart (ready to do).** Take lyrics and chords from the chords PDF (vision
   model), check the chords against `chordify` on the MIDI or GP, and take section order and
   bar counts from the GP sections. The result is `some-might-say.md`, `lyrics.md` and a
   chords file in the house style.
2. **Part extraction for the one-man band.** Write the GP bass or rhythm part to ASCII tab or
   MusicXML, and pull single parts out of the GP-derived MIDI to loop or practise against.
3. **Lyrics on the vocal melody (needs work).** The GP vocal track has the notes but no words,
   and the PDF has the words but no timing. Putting each syllable on its note is an
   LLM-assisted alignment job. The result could be written back with alphaTab's GP7 exporter
   or as MusicXML. ❓
4. **Lining up with the recording (the hard part).** The MIDI and GP have a fixed tempo
   (109 / 108), but the record drifts. Options:
   - Logic **Smart Tempo** on the drum stem, then import the MIDI to follow the project
     tempo. 🔶 This is the Logic-native route, but it means writing to the Logic project.
   - Beat tracking on the drum stem (e.g. `librosa`), then stretching the MIDI's timing to a
     tempo map. ❓
   - Once lined up, the MIDI section markers become Logic markers over the stems, and MIDI
     instruments can play along with the real recording.
5. **Transpose, capo, re-voice.** Deterministic in music21 once a part is in MusicXML or MIDI.

## Gaps and decisions

- **PDFs are the weak link.** Prefer the source the PDF was printed from (UG text, `.gp`
  downloads). Use a vision model for chord sheets and treat image tab as a last resort.
- **The saved Logic project is out of date** compared with what's open, so save before
  reading it from disk. Reading track names while Logic is running needs UI scripting. ❓
- **Worth turning into scripts** (prototype code is in the 2026-10-12 session):
  `gp_dump.py` (GP7 → sections, chords, ASCII tab per track), `gp2mid` (alphaTab), and a
  `music21` summary (sections, chords per bar) extending `midi_dump.py`.
