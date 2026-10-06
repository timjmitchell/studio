# MIDI-to-Tab Inference System

## Problem Statement

Converting polyphonic MIDI from guitar to accurate tablature requires solving string/fret disambiguation. A pitch like G3 could be:
- Open G string (string 3, fret 0)
- 5th fret on D string (string 4, fret 5)
- 10th fret on A string (string 5, fret 10)

Hardware solutions (hex pickups) solve this at the signal level by isolating each string. This document explores solving it at the inference level instead—using constraints, patterns, and probabilistic reasoning.

---

## Core Insight: Guitar Playing is Highly Constrained

Human hands have physical limitations that dramatically reduce the solution space:

- **Hand span**: Typically 4 frets max, occasionally 5-6
- **Finger count**: 4 fretting fingers available
- **Position continuity**: Hands don't teleport—sequential notes tend to cluster
- **Ergonomic preferences**: Guitarists minimize effort (open strings when available, avoid awkward stretches)
- **Idiomatic patterns**: Chord shapes, scale boxes, and interval patterns are finite and well-documented

---

## The Matrix Model

Treat the fretboard as 6 parallel "keyboards" (one per string):

```
        Fret: 0   1   2   3   4   5   6   7   8   9   10  11  12
String 1 (e): E4  F4  F#4 G4  G#4 A4  A#4 B4  C5  C#5 D5  D#5 E5
String 2 (B): B3  C4  C#4 D4  D#4 E4  F4  F#4 G4  G#4 A4  A#4 B4
String 3 (G): G3  G#3 A3  A#3 B3  C4  C#4 D4  D#4 E4  F4  F#4 G4
String 4 (D): D3  D#3 E3  F3  F#3 G3  G#3 A3  A#3 B3  C4  C#4 D4
String 5 (A): A2  A#2 B2  C3  C#3 D3  D#3 E3  F3  F#3 G3  G#3 A2
String 6 (E): E2  F2  F#2 G2  G#2 A2  A#2 B2  C3  C#3 D3  D#3 E3
```

Each cell is a unique (string, fret) coordinate. Pitches in overlapping ranges exist in multiple cells—this is where ambiguity lives.

### Shapes as Matrix Masks

A chord or scale shape is a boolean mask over this matrix. An open G chord is always the same mask pattern. Slide it up the neck and the pattern holds, just offset.

Given simultaneous MIDI pitches, the question becomes: **"Which known mask, at which fret offset, produces these pitches?"**

This is set intersection / pattern matching, not complex pathfinding.

---

## Constraint Architecture

### Hard Constraints (Boolean — Reject Violations)

These are physical impossibilities:

| Constraint | Rule |
|------------|------|
| Fret span | Max 4-5 frets in a single hand position |
| Finger count | Max 4 notes fretted simultaneously (excluding barres) |
| String exclusivity | One note per string at a time |
| Open string reality | Fret 0 = specific fixed pitches only |
| Physical reach | Simultaneous notes must be reachable by one hand |

### Soft Constraints (Scored Tendencies)

These represent likelihood, not impossibility:

| Pattern | Likelihood Score |
|---------|------------------|
| 3-fret stretch | Very common (1.0) |
| 4-fret stretch | Common (0.7) |
| 5-fret stretch | Uncommon (0.3) |
| 6-fret stretch | Rare but happens (0.4) |
| 7+ fret stretch | Almost never (0.05) |
| Position shift | Penalize by fret distance |
| Open strings | Genre-dependent bias |
| Adjacent string intervals | Fifths/fourths favor same-fret, adjacent string |

### Interval Patterns

Common interval shapes that strongly predict fingering:

| Interval | Typical Shape |
|----------|---------------|
| Perfect 5th | Same fret, adjacent string (power chord) |
| Octave | +2 frets, skip one string; or +0 frets, skip two strings |
| Perfect 4th | Same fret, adjacent string (inverse of 5th depending on string pair) |
| Minor 3rd | Same string +3 frets, or adjacent string patterns |

---

## The Role of the LLM

The LLM acts as a **translator between fuzzy human intent and structured parameters**.

### Example: User Prompt → Typed Constraints

**Input**: "Jazz voicings, Wes Montgomery style"

**Output Parameters**:
```json
{
  "position_bias": "frets 5-12",
  "voicing_preference": ["drop_2", "drop_3"],
  "root_in_bass": false,
  "thumb_octaves": true,
  "stretch_tolerance": "wider",
  "open_strings": "rare"
}
```

**Input**: "Campfire strumming, beginner"

**Output Parameters**:
```json
{
  "position_bias": "frets 0-3",
  "voicing_preference": ["open_cowboy_chords"],
  "barre_tolerance": "avoid",
  "stretch_tolerance": "minimal",
  "open_strings": "preferred"
}
```

These typed parameters can feed directly into constraint weights or library filtering.

---

## Algorithm Options

### Pattern Matching (Primary)

For chords and simultaneous notes:
1. Enumerate all physically possible (string, fret) assignments
2. Check against known chord shape masks
3. If match found, prefer that voicing
4. If no match, score by soft constraints and pick best

### Path Search (Sequential Notes)

For melodic lines:
1. Build graph: nodes = (pitch, string, fret), edges = transitions
2. Weight edges by hand movement cost + soft constraints
3. Viterbi or beam search for optimal path

### Hybrid

Real music mixes chords and melody. Segment the MIDI by timing:
- Simultaneous notes (within ~20ms) → chord/pattern matching
- Sequential notes → path search within position, shift detection between phrases

---

## Training Data Sources

Abundant labeled data exists:

- **Guitar Pro files** (.gp5, .gpx): Contain both MIDI and tab—millions available
- **Ultimate Guitar corpus**: Massive crowd-sourced tab collection
- **Synthetic generation**: Render known tabs to MIDI, train inverse mapping
- **User corrections**: Feedback loop to improve priors

---

## Prototype Approach

### Philosophy

Use an LLM agent as the algorithm initially. Focus on discovering which inputs matter before committing to code. The agent can be the constraint solver, pattern matcher, and scorer all at once—imperfect but fast to iterate.

### System Prompt Structure

```markdown
You are a guitar tablature inference system. Given MIDI input (pitch, timing, velocity), output the most likely guitar tablature.

## Hard Constraints (never violate)
- Maximum 4 fret span in one hand position (5 rare, 6 requires position shift or open string)
- Maximum 4 fingers fretting simultaneously
- One note per string at a time  
- Fret 0 available only for: E2, A2, D3, G3, B3, E4
- Simultaneous notes must be physically reachable by one hand

## Soft Constraints (prefer but don't require)
- Prefer smaller stretches (3 frets common, 4 less so, 5+ uncommon)
- Prefer minimal position shifts between sequential notes
- Prefer staying in one position for fast passages
- Penalize large jumps unless timing suggests deliberate shift

## Interval Heuristics
- Perfect 5th: almost always same fret, adjacent strings (power chord shape)
- Octave: typically +2 frets and skip one string, or same fret skip two strings
- Fast scalar runs: likely within one scale box pattern

## Shape Library
[Include common chord voicings and scale box patterns as reference]

## User Context
[User provides: genre, style hints, position preferences, specific corrections]

## Output Format
For each note or chord, output:
- Fret number per string (x = not played)
- Confidence score
- Alternative interpretations if ambiguous
```

### Iteration Loop

1. Feed agent MIDI sequence (pitch + timing + velocity)
2. Provide constraints and library as system context
3. Add user hint if available ("open position folk", "jazz comping at 7th fret")
4. Agent outputs candidate tablature
5. Human reviews, corrects errors
6. Note which constraint or library entry would have caught the error
7. Refine prompts and constraints
8. Repeat

### What You're Looking For

After several iterations, patterns emerge:
- Missing constraints ("need a 'barre chord bias' rule")
- Missing shapes ("add jazz shell voicings to library")
- Edge cases that need explicit handling
- Which soft constraint weights matter most

This informs what to eventually codify in a proper algorithm.

---

## Future Directions

### User Feedback Loop
- Show multiple candidate interpretations ranked by score
- Let user select correct one
- Use selection to tune priors for rest of piece

### Genre Presets
- Pre-built constraint profiles for common styles
- User picks "blues", "classical", "metal" etc. and gets tuned defaults

### Integration Points
- Import from Jam Origin MIDI Guitar output
- Export to Guitar Pro, MusicXML, or plain ASCII tab
- Real-time mode for practice/transcription workflow

---

## Summary

The core insight is that guitar fingering is heavily constrained by physical ergonomics and idiomatic playing patterns. Rather than solving an open-ended AI problem, we're doing constrained pattern matching with probabilistic tie-breaking.

The LLM's role is to:
1. Translate fuzzy user intent ("jazz style") into typed constraints
2. Act as a rapid-prototyping inference engine during development
3. Eventually hand off the well-defined algorithm to traditional code

Start with the agent-as-algorithm approach to discover what inputs matter, then codify the proven heuristics.