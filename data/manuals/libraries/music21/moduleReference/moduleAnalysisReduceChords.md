Source: https://music21.org/music21docs/moduleReference/moduleAnalysisReduceChords.html

# music21.analysis.reduceChords

Automatically reduce a MeasureStack to a single chord or group of chords.

## ChordReducer

class music21.analysis.reduceChords.ChordReducer[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer)
:   A chord reducer.

[`ChordReducer`](#music21.analysis.reduceChords.ChordReducer "music21.analysis.reduceChords.ChordReducer") methods

ChordReducer.alignHockets(*scoreTree*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.alignHockets)
:   Aligns hockets between parts in tree.

ChordReducer.collapseArpeggios(*scoreTree*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.collapseArpeggios)
:   Collapses arpeggios in tree.

    ```python
    >>> m = stream.Measure([chord.Chord('C4 E4'), chord.Chord('C4 G4')])
    >>> cr = analysis.reduceChords.ChordReducer()
    >>> spans = m.asTimespans(classList=(note.NotRest,))
    >>> len(spans)
    2
    >>> cr.collapseArpeggios(spans)
    >>> len(spans)
    1
    ```

ChordReducer.computeMeasureChordWeights(*measureObject*, *weightAlgorithm=None*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.computeMeasureChordWeights)
:   Compute measure chord weights:

    ```python
    >>> s = analysis.reduceChords.testMeasureStream1().notes
    >>> cr = analysis.reduceChords.ChordReducer()
    >>> cws = cr.computeMeasureChordWeights(s)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
        (0, 4, 7)  3.0
    (0, 11, 4, 5)  1.0
    ```

    Add beatStrength:

    ```python
    >>> cws = cr.computeMeasureChordWeights(s,
    ...     weightAlgorithm=cr.quarterLengthBeatStrength)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
        (0, 4, 7)  2.2
    (0, 11, 4, 5)  0.5
    ```

    Give extra weight to the last element in a measure:

    ```python
    >>> cws = cr.computeMeasureChordWeights(s,
    ...     weightAlgorithm=cr.quarterLengthBeatStrengthMeasurePosition)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
        (0, 4, 7)  3.0
    (0, 11, 4, 5)  0.5
    ```

    Make consonance count a lot:

    ```python
    >>> cws = cr.computeMeasureChordWeights(s,
    ...     weightAlgorithm=cr.qlbsmpConsonance)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
         (0, 4, 7)  3.0
     (0, 11, 4, 5)  0.1
    ```

ChordReducer.fillBassGaps(*scoreTree*, *partwiseTrees*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.fillBassGaps)

ChordReducer.fillMeasureGaps(*scoreTree*, *partwiseTrees*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.fillMeasureGaps)
:   Fills measure gaps in tree.

ChordReducer.fuseTimespansByPart(*scoreTree*, *part*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.fuseTimespansByPart)

ChordReducer.qlbsmpConsonance(*chordObject*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.qlbsmpConsonance)
:   Everything from before plus consonance

ChordReducer.quarterLengthBeatStrength(*chordObject*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.quarterLengthBeatStrength)

ChordReducer.quarterLengthBeatStrengthMeasurePosition(*chordObject*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.quarterLengthBeatStrengthMeasurePosition)

ChordReducer.quarterLengthOnly(*chordObject*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.quarterLengthOnly)

ChordReducer.reduceMeasureToNChords(*measureObject*, *maximumNumberOfChords=1*, *weightAlgorithm=None*, *trimBelow=0.25*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.reduceMeasureToNChords)
:   Reduces measure to n chords:

    ```python
    >>> s = analysis.reduceChords.testMeasureStream1()
    >>> cr = analysis.reduceChords.ChordReducer()
    ```

    Reduce to a maximum of 3 chords; though here we will only get one
    because the other chord is below the trimBelow threshold.

    ```python
    >>> newS = cr.reduceMeasureToNChords(s, 3,
    ...     weightAlgorithm=cr.qlbsmpConsonance,
    ...     trimBelow=0.3)
    >>> newS.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.chord.Chord C4 E4 G4 C5>
    ```

    ```python
    >>> newS[-1].quarterLength
    4.0
    ```

ChordReducer.removeNonChordTones(*scoreTree*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.removeNonChordTones)
:   Removes timespans containing passing and neighbor tones from tree.

ChordReducer.removeShortTimespans(*scoreTree*, *partwiseTrees*, *duration=0.5*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.removeShortTimespans)
:   Removes timespans in tree shorter than duration.

    Special treatment is given to groups of short timespans if they take up
    an entire measure. In that case, the timespans with the most common
    sets of pitches are kept.

ChordReducer.removeVerticalDissonances(*scoreTree=None*, *allowableChords=None*, *forbiddenChords=None*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.removeVerticalDissonances)
:   Removes timespans in each dissonant verticality of tree whose pitches
    are above the lowest pitch in that verticality.

ChordReducer.removeZeroDurationTimespans(*scoreTree*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.removeZeroDurationTimespans)

ChordReducer.run(*inputScore*, *allowableChords=None*, *closedPosition=False*, *forbiddenChords=None*, *maximumNumberOfChords=3*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.run)

ChordReducer.splitByBass(*scoreTree*)[[source]](../_modules/music21/analysis/reduceChords.html#ChordReducer.splitByBass)

## Functions

music21.analysis.reduceChords.testMeasureStream1()[[source]](../_modules/music21/analysis/reduceChords.html#testMeasureStream1)
:   returns a simple measure stream for testing:

    ```python
    >>> s = analysis.reduceChords.testMeasureStream1()
    >>> s.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.chord.Chord C4 E4 G4 C5>
    {2.0} <music21.chord.Chord C4 E4 F4 B4>
    {3.0} <music21.chord.Chord C4 E4 G4 C5>
    ```
