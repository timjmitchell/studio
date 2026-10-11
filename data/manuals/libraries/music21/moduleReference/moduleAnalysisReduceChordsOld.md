Source: https://music21.org/music21docs/moduleReference/moduleAnalysisReduceChordsOld.html

# music21.analysis.reduceChordsOld

Automatically reduce a MeasureStack to a single chord or group of chords.

## ChordReducer

class music21.analysis.reduceChordsOld.ChordReducer[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer)

[`ChordReducer`](#music21.analysis.reduceChordsOld.ChordReducer "music21.analysis.reduceChordsOld.ChordReducer") methods

ChordReducer.computeMeasureChordWeights(*measureObj*, *weightAlgorithm=None*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.computeMeasureChordWeights)
:   ```python
    >>> s = analysis.reduceChordsOld.testMeasureStream1().notes
    >>> cr = analysis.reduceChordsOld.ChordReducer()
    >>> cws = cr.computeMeasureChordWeights(s)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
         (0, 4, 7)  3.0
     (0, 11, 4, 5)  1.0
    ```

    Add beatStrength:

    ```python
    >>> cws = cr.computeMeasureChordWeights(s, weightAlgorithm=cr.quarterLengthBeatStrength)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
         (0, 4, 7)  2.2
     (0, 11, 4, 5)  0.5
    ```

    Give extra weight to the last element in a measure:

    ```python
    >>> cws = cr.computeMeasureChordWeights(s,
    ...              weightAlgorithm=cr.quarterLengthBeatStrengthMeasurePosition)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
         (0, 4, 7)  3.0
     (0, 11, 4, 5)  0.5
    ```

    Make consonance count a lot:

    ```python
    >>> cws = cr.computeMeasureChordWeights(s, weightAlgorithm=cr.qlbsmpConsonance)
    >>> for pcs in sorted(cws):
    ...     print(f'{pcs!r:18}  {cws[pcs]:2.1f}')
             (0, 4, 7)  3.0
         (0, 11, 4, 5)  0.5
    ```

ChordReducer.multiPartReduction(*inStream*, *maxChords=2*, *closedPosition=False*, *forceOctave=False*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.multiPartReduction)
:   Return a multipart reduction of a stream.

ChordReducer.qlbsmpConsonance(*c*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.qlbsmpConsonance)
:   Everything from before plus consonance

ChordReducer.quarterLengthBeatStrength(*c*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.quarterLengthBeatStrength)

ChordReducer.quarterLengthBeatStrengthMeasurePosition(*c*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.quarterLengthBeatStrengthMeasurePosition)

ChordReducer.quarterLengthOnly(*c*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.quarterLengthOnly)

ChordReducer.reduceMeasureToNChords(*measureObj*, *numChords=1*, *weightAlgorithm=None*, *trimBelow=0.25*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.reduceMeasureToNChords)
:   Takes a measure and reduces it to only one chord or numChords chords.

    ```python
    >>> s = analysis.reduceChordsOld.testMeasureStream1()
    >>> cr = analysis.reduceChordsOld.ChordReducer()
    ```

    Reduce to a maximum of 3 chords; though here we will
    only get one because the other chord is
    below the trimBelow threshold.

    ```python
    >>> newS = cr.reduceMeasureToNChords(s, 3,
    ...    weightAlgorithm=cr.qlbsmpConsonance, trimBelow = 0.3)
    >>> newS.show('text')
    {0.0} <music21.chord.Chord C4 E4 G4 C5>
    >>> newS.notes.first().quarterLength
    4.0
    ```

ChordReducer.reduceThisMeasure(*mI*, *measureIndex*, *maxChords*, *closedPosition*, *forceOctave*)[[source]](../_modules/music21/analysis/reduceChordsOld.html#ChordReducer.reduceThisMeasure)

## Functions

music21.analysis.reduceChordsOld.testMeasureStream1()[[source]](../_modules/music21/analysis/reduceChordsOld.html#testMeasureStream1)
:   returns a simple measure stream for testing:

    ```python
    >>> s = analysis.reduceChordsOld.testMeasureStream1()
    >>> s.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.chord.Chord C4 E4 G4 C5>
    {2.0} <music21.chord.Chord C4 E4 F4 B4>
    {3.0} <music21.chord.Chord C4 E4 G4 C5>
    ```
