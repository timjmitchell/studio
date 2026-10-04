Source: https://music21.org/music21docs/moduleReference/moduleFiguredBassChecker.html

# music21.figuredBass.checker

## Functions

music21.figuredBass.checker.extractHarmonies(*music21Stream*)[[source]](../_modules/music21/figuredBass/checker.html#extractHarmonies)
:   Takes in a `Stream` and returns a dictionary whose values
    are the voice leading moments of the `Stream` and whose
    keys are (offset, endTime) pairs delimiting their duration. The voice leading
    moments are spelled out from the first or highest `Part`
    to the lowest one.

    ```python
    >>> score = corpus.parse('corelli/opus3no1/1grave').measures(1, 3)
    >>> score.show()
    ```

    [![../_images/corelli_grave.png](../_images/corelli_grave.png)](../_images/corelli_grave.png)

    ```python
    >>> from music21.figuredBass import checker
    >>> allHarmonies = checker.extractHarmonies(score)
    >>> for (offsets, notes) in sorted(allHarmonies.items()):
    ...     print(f'{offsets!s:15}[{notes[0]!s:23}{notes[1]!s:23}{notes[2]!s:22}]')
    (0.0, 1.5)     [<music21.note.Note C>  <music21.note.Note A>  <music21.note.Note F> ]
    (1.5, 2.0)     [<music21.note.Note C>  <music21.note.Note A>  <music21.note.Note F> ]
    (2.0, 3.0)     [<music21.note.Note B-> <music21.note.Note G>  <music21.note.Note G> ]
    (3.0, 3.5)     [<music21.note.Note A>  <music21.note.Note F>  <music21.note.Note A> ]
    (3.5, 4.0)     [<music21.note.Note A>  <music21.note.Note F>  <music21.note.Note B->]
    (4.0, 6.0)     [<music21.note.Note G>  <music21.note.Note E>  <music21.note.Note C> ]
    (6.0, 6.5)     [<music21.note.Note A>  <music21.note.Note F>  <music21.note.Note A> ]
    (6.5, 7.0)     [<music21.note.Note B-> <music21.note.Note F>  <music21.note.Note A> ]
    (7.0, 7.5)     [<music21.note.Note C>  <music21.note.Note F>  <music21.note.Note A> ]
    (7.5, 8.0)     [<music21.note.Note C>  <music21.note.Note E>  <music21.note.Note A> ]
    (8.0, 8.5)     [<music21.note.Note C>  <music21.note.Note D>  <music21.note.Note B->]
    (8.5, 9.0)     [<music21.note.Note F>  <music21.note.Note D>  <music21.note.Note B->]
    (9.0, 9.5)     [<music21.note.Note B-> <music21.note.Note D>  <music21.note.Note B->]
    (9.5, 10.0)    [<music21.note.Note B-> <music21.note.Note G>  <music21.note.Note B->]
    (10.0, 10.5)   [<music21.note.Note B-> <music21.note.Note E>  <music21.note.Note C> ]
    (10.5, 11.0)   [<music21.note.Note B-> <music21.note.Note C>  <music21.note.Note C> ]
    (11.0, 11.5)   [<music21.note.Note A>  <music21.note.Note F>  <music21.note.Note D> ]
    (11.5, 12.0)   [<music21.note.Note A>  <music21.note.Note F>  <music21.note.Note A> ]
    ```

music21.figuredBass.checker.getVoiceLeadingMoments(*music21Stream*)[[source]](../_modules/music21/figuredBass/checker.html#getVoiceLeadingMoments)
:   Takes in a `Stream` and returns a `Score`
    of the `Stream` broken up into its voice leading moments.

    ```python
    >>> score = corpus.parse('corelli/opus3no1/1grave').measures(1, 3)
    >>> score.show()
    ```

    [![../_images/corelli_grave.png](../_images/corelli_grave.png)](../_images/corelli_grave.png)

    ```python
    >>> from music21.figuredBass import checker
    >>> vlMoments = checker.getVoiceLeadingMoments(score)
    >>> vlMoments.show()
    ```

    [![../_images/corelli_vlm.png](../_images/corelli_vlm.png)](../_images/corelli_vlm.png)

music21.figuredBass.checker.checkConsecutivePossibilities(*music21Stream*, *functionToApply*, *color='#FF0000'*, *debug=False*)[[source]](../_modules/music21/figuredBass/checker.html#checkConsecutivePossibilities)
:   Takes in a `Score` and a functionToApply which takes in two consecutive
    possibility instances, each a tuple with pitches or rests comprising a vertical sonority.
    Changes the color of notes in the `Score` which comprise rule violations
    as determined by functionToApply.

    Note

    Colored notes are NOT supported in Finale.

    ```python
    >>> music21Stream = corpus.parse('theoryExercises/checker_demo.xml')
    >>> music21Stream.show()
    ```

    [![../_images/checker_demo.png](../_images/checker_demo.png)](../_images/checker_demo.png)

    ```python
    >>> from music21.figuredBass import checker
    >>> functionToApply = checker.parallelOctaves
    >>> checker.checkConsecutivePossibilities(music21Stream, functionToApply, debug=True)
    Function To Apply: parallelOctaves
    (Offset A, End Time A):  (Offset B, End Time B):  Part Numbers:
    (1.0, 2.0)               (2.0, 3.0)               (2, 4)
    (2.0, 3.0)               (3.0, 5.0)               (2, 4)
    (8.0, 9.0)               (9.0, 11.0)              (1, 3)
    ```

    Parallel octaves can be found in the first measure, between the first two measures,
    and between the third and the fourth measure. The notes in question are highlighted
    in the music21Stream, as shown below.

    ```python
    >>> music21Stream.show()
    ```

    [![../_images/checker_parallelOctaves.png](../_images/checker_parallelOctaves.png)](../_images/checker_parallelOctaves.png)

music21.figuredBass.checker.checkSinglePossibilities(*music21Stream*, *functionToApply*, *color='#FF0000'*, *debug=False*)[[source]](../_modules/music21/figuredBass/checker.html#checkSinglePossibilities)
:   Takes in a `Score` and a functionToApply which takes in a possibility
    instance, a tuple with pitches or rests comprising a vertical sonority. Changes the color of
    notes in the `Score` which comprise rule violations as determined by
    functionToApply.

    Note

    Colored notes are NOT supported in Finale.

    ```python
    >>> music21Stream = corpus.parse('corelli/opus3no1/1grave').measures(1, 6)
    >>> music21Stream.show()
    ```

    [![../_images/corelli_grave2.png](../_images/corelli_grave2.png)](../_images/corelli_grave2.png)

    ```python
    >>> from music21.figuredBass import checker
    >>> functionToApply = checker.voiceCrossing
    >>> checker.checkSinglePossibilities(music21Stream, functionToApply, debug=True)
    Function To Apply: voiceCrossing
    (Offset, End Time):      Part Numbers:
    (16.0, 16.5)             (1, 2)
    (16.5, 17.0)             (1, 2)
    ```

    Voice Crossing is present in the fifth measure between the first and second voices,
    and the notes in question are highlighted in the music21Stream.

    ```python
    >>> music21Stream.show()
    ```

    [![../_images/corelli_voiceCrossing.png](../_images/corelli_voiceCrossing.png)](../_images/corelli_voiceCrossing.png)

music21.figuredBass.checker.correlateHarmonies(*currentMapping*, *music21Part*)[[source]](../_modules/music21/figuredBass/checker.html#correlateHarmonies)
:   Adds a new `Part` to an existing offset mapping.

    ```python
    >>> from music21.figuredBass import checker
    >>> score = corpus.parse('corelli/opus3no1/1grave').measures(1, 3)
    >>> v0 = score[0]
    >>> offsetMapping = checker.createOffsetMapping(v0)
    >>> v1 = score[1]
    >>> newMapping = checker.correlateHarmonies(offsetMapping, v1)
    >>> for (offsets, notes) in sorted(newMapping.items()):
    ...     print(f'{offsets!s:15}[{notes[0]!s:23}{notes[1]!s:21}]')
    (0.0, 1.5)     [<music21.note.Note C>  <music21.note.Note A>]
    (1.5, 2.0)     [<music21.note.Note C>  <music21.note.Note A>]
    (2.0, 3.0)     [<music21.note.Note B-> <music21.note.Note G>]
    (3.0, 4.0)     [<music21.note.Note A>  <music21.note.Note F>]
    (4.0, 6.0)     [<music21.note.Note G>  <music21.note.Note E>]
    (6.0, 6.5)     [<music21.note.Note A>  <music21.note.Note F>]
    (6.5, 7.0)     [<music21.note.Note B-> <music21.note.Note F>]
    (7.0, 7.5)     [<music21.note.Note C>  <music21.note.Note F>]
    (7.5, 8.0)     [<music21.note.Note C>  <music21.note.Note E>]
    (8.0, 8.5)     [<music21.note.Note C>  <music21.note.Note D>]
    (8.5, 9.0)     [<music21.note.Note F>  <music21.note.Note D>]
    (9.0, 9.5)     [<music21.note.Note B-> <music21.note.Note D>]
    (9.5, 10.0)    [<music21.note.Note B-> <music21.note.Note G>]
    (10.0, 10.5)   [<music21.note.Note B-> <music21.note.Note E>]
    (10.5, 11.0)   [<music21.note.Note B-> <music21.note.Note C>]
    (11.0, 12.0)   [<music21.note.Note A>  <music21.note.Note F>]
    ```

music21.figuredBass.checker.createOffsetMapping(*music21Part*)[[source]](../_modules/music21/figuredBass/checker.html#createOffsetMapping)
:   Creates an initial offset mapping of a `Part`.

    ```python
    >>> from music21.figuredBass import checker
    >>> score = corpus.parse('corelli/opus3no1/1grave').measures(1, 3)
    >>> v0 = score[0]
    >>> offsetMapping = checker.createOffsetMapping(v0)
    >>> for (offsets, notes) in sorted(offsetMapping.items()):
    ...     print(f'{offsets!s:15}[{notes[0]!s:22}]')
    (0.0, 1.5)     [<music21.note.Note C> ]
    (1.5, 2.0)     [<music21.note.Note C> ]
    (2.0, 3.0)     [<music21.note.Note B->]
    (3.0, 4.0)     [<music21.note.Note A> ]
    (4.0, 6.0)     [<music21.note.Note G> ]
    (6.0, 6.5)     [<music21.note.Note A> ]
    (6.5, 7.0)     [<music21.note.Note B->]
    (7.0, 8.0)     [<music21.note.Note C> ]
    (8.0, 8.5)     [<music21.note.Note C> ]
    (8.5, 9.0)     [<music21.note.Note F> ]
    (9.0, 11.0)    [<music21.note.Note B->]
    (11.0, 12.0)   [<music21.note.Note A> ]
    ```

music21.figuredBass.checker.generalNoteToPitch(*music21GeneralNote*)[[source]](../_modules/music21/figuredBass/checker.html#generalNoteToPitch)
:   Takes a [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote"). If it is a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note"),
    returns its pitch. Otherwise, returns the string “RT”, a rest placeholder.

    ```python
    >>> n1 = note.Note('G5')
    >>> c1 = chord.Chord(['C3', 'E3', 'G3'])
    ```

    ```python
    >>> figuredBass.checker.generalNoteToPitch(n1)
    <music21.pitch.Pitch G5>
    >>> figuredBass.checker.generalNoteToPitch(c1)
    'RT'
    ```

music21.figuredBass.checker.hiddenFifth(*possibA*, *possibB*)[[source]](../_modules/music21/figuredBass/checker.html#hiddenFifth)
:   Returns a list with a (highestPart, lowestPart) pair which represents
    a hidden fifth between shared outer parts of possibA and possibB. The
    outer parts here are the first and last elements of each possibility.

    If sopranoPitchA and bassPitchA in possibA move to a sopranoPitchB
    and bassPitchB in possibB in similar motion, and the simple interval
    between sopranoPitchB and bassPitchB is that of a perfect fifth,
    then this constitutes a hidden octave between the two possibilities.

    ```python
    >>> from music21.figuredBass import checker
    >>> C3 = pitch.Pitch('C3')
    >>> D3 = pitch.Pitch('D3')
    >>> E3 = pitch.Pitch('E3')
    >>> F3 = pitch.Pitch('F3')
    >>> E5 = pitch.Pitch('E5')
    >>> A5 = pitch.Pitch('A5')
    ```

    Here, the bass part moves up from C3 to D3 and the soprano part moves
    up from E5 to A5. The simple interval between D3 and A5 is a perfect
    fifth. Therefore, there is a hidden fifth between the two possibilities.

    ```python
    >>> possibA1 = (E5, E3, C3)
    >>> possibB1 = (A5, F3, D3)
    >>> checker.hiddenFifth(possibA1, possibB1)
    [(1, 3)]
    ```

    Here, the soprano and bass parts also move in similar motion, but the
    simple interval between D3 and Ab5 is a diminished fifth. Consequently,
    there is no hidden fifth.

    ```python
    >>> Ab5 = pitch.Pitch('A-5')
    >>> possibA2 = (E5, E3, C3)
    >>> possibB2 = (Ab5, F3, D3)
    >>> checker.hiddenFifth(possibA2, possibB2)
    []
    ```

    Now, we have the soprano and bass parts again moving to A5 and D3, whose
    simple interval is a perfect fifth. However, the bass moves up while the
    soprano moves down. Therefore, there is no hidden fifth.

    ```python
    >>> E6 = pitch.Pitch('E6')
    >>> possibA3 = (E6, E3, C3)
    >>> possibB3 = (A5, F3, D3)
    >>> checker.hiddenFifth(possibA3, possibB3)
    []
    ```

music21.figuredBass.checker.hiddenOctave(*possibA*, *possibB*)[[source]](../_modules/music21/figuredBass/checker.html#hiddenOctave)
:   Returns a list with a (highestPart, lowestPart) pair which represents
    a hidden octave between shared outer parts of possibA and possibB. The
    outer parts here are the first and last elements of each possibility.

    If sopranoPitchA and bassPitchA in possibA move to a sopranoPitchB
    and bassPitchB in possibB in similar motion, and the simple interval
    between sopranoPitchB and bassPitchB is that of a perfect octave,
    then this constitutes a hidden octave between the two possibilities.

    ```python
    >>> from music21.figuredBass import checker
    >>> C3 = pitch.Pitch('C3')
    >>> D3 = pitch.Pitch('D3')
    >>> E3 = pitch.Pitch('E3')
    >>> F3 = pitch.Pitch('F3')
    >>> A5 = pitch.Pitch('A5')
    >>> D6 = pitch.Pitch('D6')
    ```

    Here, the bass part moves up from C3 to D3 and the soprano part moves
    up from A5 to D6. The simple interval between D3 and D6 is a perfect
    octave. Therefore, there is a hidden octave between the two possibilities.

    ```python
    >>> possibA1 = (A5, E3, C3)
    >>> possibB1 = (D6, F3, D3)  # Perfect octave between soprano and bass.
    >>> checker.hiddenOctave(possibA1, possibB1)
    [(1, 3)]
    ```

    Here, the bass part moves up from C3 to D3 but the soprano part moves
    down from A6 to D6. There is no hidden octave since the parts move in
    contrary motion.

    ```python
    >>> A6 = pitch.Pitch('A6')
    >>> possibA2 = (A6, E3, C3)
    >>> possibB2 = (D6, F3, D3)
    >>> checker.hiddenOctave(possibA2, possibB2)
    []
    ```

music21.figuredBass.checker.parallelFifths(*possibA*, *possibB*)[[source]](../_modules/music21/figuredBass/checker.html#parallelFifths)
:   Returns a list of (partNumberA, partNumberB) pairs, each representing
    two voices which form parallel fifths.

    If pitchA1 and pitchA2 in possibA are separated by
    a simple interval of a perfect fifth, and they move
    to a pitchB1 and pitchB2 in possibB also separated
    by the simple interval of a perfect fifth, then this
    constitutes parallel fifths between these two parts.

    ```python
    >>> from music21.figuredBass import checker
    >>> C3 = pitch.Pitch('C3')
    >>> D3 = pitch.Pitch('D3')
    >>> G3 = pitch.Pitch('G3')
    >>> A3 = pitch.Pitch('A3')
    >>> A4 = pitch.Pitch('A4')
    >>> B4 = pitch.Pitch('B4')
    ```

    Here, the bass moves from C3 to D3 and the tenor moves
    from G3 to A3. The interval between C3 and G3, as well
    as between D3 and A3, is a perfect fifth. These two
    parts, and therefore the two possibilities, have
    parallel fifths.

    ```python
    >>> possibA1 = (B4, G3, C3)
    >>> possibB1 = (A4, A3, D3)
    >>> checker.parallelFifths(possibA1, possibB1)
    [(2, 3)]
    ```

    Now, the tenor moves instead to F3. The interval between
    D3 and F3 is a minor third. The bass and tenor parts
    don’t form parallel fifths. The soprano part forms parallel
    fifths with neither the bass nor tenor parts. The
    two possibilities, therefore, have no parallel fifths.

    ```python
    >>> F3 = pitch.Pitch('F3')
    >>> possibA2 = (B4, G3, C3)
    >>> possibB2 = (A4, F3, D3)
    >>> checker.parallelFifths(possibA2, possibB2)
    []
    ```

music21.figuredBass.checker.parallelOctaves(*possibA*, *possibB*)[[source]](../_modules/music21/figuredBass/checker.html#parallelOctaves)
:   Returns a list of (partNumberA, partNumberB) pairs, each representing
    two voices which form parallel octaves.

    If pitchA1 and pitchA2 in possibA are separated by
    a simple interval of a perfect octave, and they move
    to a pitchB1 and pitchB2 in possibB also separated
    by the simple interval of a perfect octave, then this
    constitutes parallel octaves between these two parts.

    ```python
    >>> from music21.figuredBass import checker
    >>> C3 = pitch.Pitch('C3')
    >>> D3 = pitch.Pitch('D3')
    >>> G3 = pitch.Pitch('G3')
    >>> A3 = pitch.Pitch('A3')
    >>> C4 = pitch.Pitch('C4')
    >>> D4 = pitch.Pitch('D4')
    ```

    Here, the soprano moves from C4 to D4 and the bass moves
    from C3 to D3. The interval between C3 and C4, as well as
    between D3 and D4, is a parallel octave. The two parts,
    and therefore the two possibilities, have parallel octaves.

    ```python
    >>> possibA1 = (C4, G3, C3)
    >>> possibB1 = (D4, A3, D3)
    >>> checker.parallelOctaves(possibA1, possibB1)
    [(1, 3)]
    ```

    Now, the soprano moves down to B3. The interval between
    D3 and B3 is a major sixth. The soprano and bass parts
    no longer have parallel octaves. The tenor part forms
    a parallel octave with neither the bass nor soprano,
    so the two possibilities do not have parallel octaves.
    (Notice, however, the parallel fifth between the bass
    and tenor!)

    ```python
    >>> B3 = pitch.Pitch('B3')
    >>> possibA2 = (C4, G3, C3)
    >>> possibB2 = (B3, A3, D3)
    >>> checker.parallelOctaves(possibA2, possibB2)
    []
    ```

music21.figuredBass.checker.voiceCrossing(*possibA*)[[source]](../_modules/music21/figuredBass/checker.html#voiceCrossing)
:   Returns a list of (partNumberA, partNumberB) pairs, each representing
    two voices which form a voice crossing. The parts from the lowest part to
    the highest part (right to left) must correspond to increasingly higher
    pitches in order for there to be no voice crossing. Comparisons between
    pitches are done using pitch comparison methods, which are based on pitch
    space values (see [`Pitch`](modulePitch.html#music21.pitch.Pitch "music21.pitch.Pitch")).

    ```python
    >>> from music21.figuredBass import checker
    >>> C4 = pitch.Pitch('C4')
    >>> E4 = pitch.Pitch('E4')
    >>> C5 = pitch.Pitch('C5')
    >>> G5 = pitch.Pitch('G5')
    >>> possibA1 = (C5, G5, E4)
    >>> checker.voiceCrossing(possibA1)  # G5 > C5
    [(1, 2)]
    >>> possibA2 = (C5, E4, C4)
    >>> checker.voiceCrossing(possibA2)
    []
    ```
