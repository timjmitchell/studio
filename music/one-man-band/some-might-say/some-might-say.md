---
type: song
title: "Some Might Say"
artist: "Oasis"                   # original artist (the Work's credit)
project: one-man-band
version: cover
status: idea                      # idea | demo | arranging | tracking | mixing | done
key: D                            # as charted; the record sounds ≈ E♭, slightly flat (see Pitch)
tuning: [E, A, D, G, B, E]        # low → high; standard, per the GP file and both UG sheets
capo:
tempo: { record: ~112, midi: 109, gp: 108 }
time_signature: 4/4
logic:
  project: /Volumes/Samsung_X5/Oneman Band/some-might-say-oasis/some-might-say-oasis.logicx
---

# Some Might Say

Cover of **Some Might Say** by Oasis (*(What's the Story) Morning Glory?*, 1995), for one-man-band.

## Pitch

- **The record sounds at about E♭, a little flat** 🧪 (2026-10-12; measured on the stems, the
  Logic source file and the album MP3). The charts and transcriptions are all in **D**,
  standard tuning, with no drop D.
- The likely cause is D shapes in standard tuning with the tape sped up a bit 🔶 (Tim: "that's
  typical"). The exact number of cents wasn't pinned down: estimates ranged from −13 to −48
  cents flat of E♭.
- **To play MIDI against the stems:** transpose the MIDI up 1 semitone, then detune the
  software instruments slightly flat by ear (File > Project Settings > Tuning > Software
  Instrument Pitch).

## Logic session

- [some-might-say-oasis.logicx](<file:///Volumes/Samsung_X5/Oneman%20Band/some-might-say-oasis/some-might-say-oasis.logicx>):
  the official recording at 48k, stemmed into Vocals, Drums, Bass and Guitar (2026-10-12).
  The source file has about 10 s of silence before the music, and is otherwise the same as
  the album MP3 (same tempo).
- The tempo map was made with Smart Tempo on the drum stem (Tim, 2026-10-12).
- **MIDI over the stems:** set Keep Project Tempo, then import
  [midi/some-might-say_no-tempo.mid](midi/some-might-say_no-tempo.mid) at
  *(the Logic bar of the band's first downbeat) − 8*. In the MIDI, the band comes in on
  **bar 9**. See the [Logic Field Notes §5](../../../data/manuals/daw-video/Logic-Pro-Field-Notes.md).

## Structure (from the MIDI markers, 4/4, bars)

| Bar | Section |
|---|---|
| 1 | Intro (feedback and lead guitar; drums enter with a pickup at 8.3, band at 9) |
| 17 | Verse 1 |
| 33 | Pre-Chorus |
| 41 | Chorus |
| 57 | Bridge |
| 61 | Solo |
| 69 | Verse 2 |
| 85 | Pre-Chorus |
| 93 | Chorus |
| 109 | Outro |
| 127 | Outro riff |

The GP file has the same sections (it calls the outro a Coda) over 150 bars.

## Files

| File | What | Notes |
|---|---|---|
| [some might say.mid](<some might say.mid>) | Full-band MIDI: rhythm and lead guitar, bass, drums, tambourine, claps | 109 bpm, section markers, no lyrics |
| [midi/some-might-say_no-tempo.mid](midi/some-might-say_no-tempo.mid) | The same with its tempo events removed, for importing onto a tempo map | [text dump](midi/some-might-say_no-tempo.txt) |
| [Oasis - Some Might Say (ver 7 by fguzramm).gp](<Oasis - Some Might Say (ver 7 by fguzramm).gp>) | Guitar Pro 7: 13 tracks incl. vocal melody and 2 harmonies | The richest source. No lyrics |
| [some might say chords.pdf](<../../_pdfs/one-man-band/some-might-say/some might say chords.pdf>) (local, untracked) | Ultimate Guitar chords and lyrics (image-only PDF) | The only source with lyrics |
| [some might say tab.pdf](<../../_pdfs/one-man-band/some-might-say/some might say tab.pdf>) (local, untracked) | Ultimate Guitar ASCII tab by wuggle15 (image-only PDF) | |

What each format can and can't do: [some-might-say-case.md](../../../docs/research/music-formats/some-might-say-case.md).

## Notes

<!-- Dated log, newest first. -->
