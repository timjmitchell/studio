Source: https://music21.org/music21docs/moduleReference/moduleAnalysisTransposition.html

# music21.analysis.transposition

## TranspositionChecker

class music21.analysis.transposition.TranspositionChecker(*pitches: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Pitch](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")] = ()*)[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker)
:   Given a list of pitches, checks for the number of distinct transpositions.

    ```python
    >>> pList = [pitch.Pitch('C4'), pitch.Pitch('E4'), pitch.Pitch('G#4')]
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> tc.numDistinctTranspositions()
    4
    >>> allNormalOrderPitchTuples = tc.getPitchesOfDistinctTranspositions()
    >>> allNormalOrderPitchTuples
    [(<music21.pitch.Pitch C>, <music21.pitch.Pitch E>,
                                         <music21.pitch.Pitch G#>),
     (<music21.pitch.Pitch C#>, <music21.pitch.Pitch F>,
                                         <music21.pitch.Pitch A>),
     (<music21.pitch.Pitch D>, <music21.pitch.Pitch F#>,
                                         <music21.pitch.Pitch A#>),
     (<music21.pitch.Pitch E->, <music21.pitch.Pitch G>,
                                         <music21.pitch.Pitch B>)]
    >>> myChord = chord.Chord(['C', 'E-', 'F#', 'A'])
    >>> pList = myChord.pitches
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> allNormalOrderChords = tc.getChordsOfDistinctTranspositions()
    >>> allNormalOrderChords
    [<music21.chord.Chord C E- F# A>,
     <music21.chord.Chord C# E G A#>,
     <music21.chord.Chord D F G# B>]
    ```

[`TranspositionChecker`](#music21.analysis.transposition.TranspositionChecker "music21.analysis.transposition.TranspositionChecker") methods

TranspositionChecker.getChordsOfDistinctTranspositions()[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker.getChordsOfDistinctTranspositions)
:   Outputs chords for each distinct transposition (normal order).

    ```python
    >>> pList = [pitch.Pitch('C4'), pitch.Pitch('E4'), pitch.Pitch('G#4')]
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> tc.getChordsOfDistinctTranspositions()
    [<music21.chord.Chord C E G#>,
     <music21.chord.Chord C# F A>,
     <music21.chord.Chord D F# A#>,
     <music21.chord.Chord E- G B>]
    ```

TranspositionChecker.getPitchesOfDistinctTranspositions()[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker.getPitchesOfDistinctTranspositions)
:   Outputs pitch tuples for each distinct transposition (normal order).

    ```python
    >>> pList = [pitch.Pitch('C4'), pitch.Pitch('E4'), pitch.Pitch('G#4')]
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> tc.getPitchesOfDistinctTranspositions()
    [(<music21.pitch.Pitch C>, <music21.pitch.Pitch E>, <music21.pitch.Pitch G#>),
     (<music21.pitch.Pitch C#>, <music21.pitch.Pitch F>, <music21.pitch.Pitch A>),
     (<music21.pitch.Pitch D>, <music21.pitch.Pitch F#>, <music21.pitch.Pitch A#>),
     (<music21.pitch.Pitch E->, <music21.pitch.Pitch G>, <music21.pitch.Pitch B>)]
    ```

TranspositionChecker.getTranspositions()[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker.getTranspositions)
:   Gets all 12 transpositions (distinct or otherwise).

    ```python
    >>> p = [pitch.Pitch('D#')]
    >>> tc = analysis.transposition.TranspositionChecker(p)
    >>> tc.getTranspositions()
    [[<music21.pitch.Pitch E->],
    [<music21.pitch.Pitch E>],
    [<music21.pitch.Pitch F>],
    [<music21.pitch.Pitch F#>],
    [<music21.pitch.Pitch G>],
    [<music21.pitch.Pitch G#>],
    [<music21.pitch.Pitch A>],
    [<music21.pitch.Pitch B->],
    [<music21.pitch.Pitch B>],
    [<music21.pitch.Pitch C>],
    [<music21.pitch.Pitch C#>],
    [<music21.pitch.Pitch D>]]
    ```

TranspositionChecker.listDistinctNormalOrders()[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker.listDistinctNormalOrders)
:   List the distinct normal orders (without duplication).

    ```python
    >>> pList = [pitch.Pitch('C4'), pitch.Pitch('E4'), pitch.Pitch('G#4')]
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> tc.listDistinctNormalOrders()
    [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]
    ```

TranspositionChecker.listNormalOrders()[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker.listNormalOrders)
:   List the normal orders for all 12 transpositions

    ```python
    >>> pList = [pitch.Pitch('C4'), pitch.Pitch('E4'), pitch.Pitch('G#4')]
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> tc.listNormalOrders()
    [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11],
     [0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11],
     [0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]
    ```

TranspositionChecker.numDistinctTranspositions()[[source]](../_modules/music21/analysis/transposition.html#TranspositionChecker.numDistinctTranspositions)
:   Gives the number of distinct transpositions (normal orders).

    ```python
    >>> pList = [pitch.Pitch('C4'), pitch.Pitch('E4'), pitch.Pitch('G#4')]
    >>> tc = analysis.transposition.TranspositionChecker(pList)
    >>> tc.numDistinctTranspositions()
    4
    ```
