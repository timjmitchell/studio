Source: https://music21.org/music21docs/moduleReference/moduleChordTools.html

# music21.chord.tools

Chord utilities too obscure to go on the Chord object, yet still helpful
enough to go in the music21 core library.

## Functions

music21.chord.tools.allChordSteps(*c: [chord.Chord](moduleChord.html#music21.chord.Chord "music21.chord.Chord")*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [pitch.Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")][[source]](../_modules/music21/chord/tools.html#allChordSteps)
:   Return a dictionary of all chordSteps in the chord.
    If more than one pitch shares the same chordStep such as the third
    in (C, E-, E, G), then only the first will appear in the dictionary.

    The dictionary will be ordered by the order of pitches in the Chord.

    More efficient than calling [getChordStep(x) for x in range(1, 8)]
    which would be O(n^2) on number of pitches.

    Requires root() to be defined.

    ```python
    >>> ch = chord.Chord('C4 E4 G4 B4 C5 D5')
    >>> chord.tools.allChordSteps(ch)
    {1: <music21.pitch.Pitch C4>,
     3: <music21.pitch.Pitch E4>,
     5: <music21.pitch.Pitch G4>,
     7: <music21.pitch.Pitch B4>,
     2: <music21.pitch.Pitch D5>}
    ```
