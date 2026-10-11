Source: https://music21.org/music21docs/moduleReference/moduleSerial.html

# music21.serial

This module defines objects for defining and manipulating structures
common to serial and/or twelve-tone music,
including [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") subclasses.

Serial searching methods that were previously here have been moved to
[`serial`](moduleSearchSerial.html#module-music21.search.serial "music21.search.serial").

## ToneRow

class music21.serial.ToneRow(*row=None*, *\*\*keywords*)[[source]](../_modules/music21/serial.html#ToneRow)
:   A Stream representation of a tone row, or an ordered sequence of pitches;
    can most importantly be used to deal with
    serial transformations.

    Unlike a normal Stream, the first argument is assumed to be a ToneRow:

    ```python
    >>> toneRow = serial.ToneRow([10, 9, 4, 5, 6, 3, 2, 8, 7, 11, 0, 1])
    ```

    The representation of a ToneRow will be the contents:

    ```python
    >>> toneRow
    <music21.serial.ToneRow A94563287B01>
    ```

    Unless (like a Stream), the id is set:

    ```python
    >>> toneRow.id = 'retrograde_jungfrau'
    >>> toneRow
    <music21.serial.ToneRow retrograde_jungfrau>
    ```

    A ToneRow does not need to have twelve pitches, like this ten-tone row
    from Ruth Crawford Seeger’s String Quartet 1931

    ```python
    >>> rcsRow = serial.ToneRow([2, 4, 5, 3, 6, 9, 8, 7, 1, 0])
    >>> rcsRow
    <music21.serial.ToneRow 2453698710>
    >>> len(rcsRow)
    10
    ```

[`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") bases

* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") read-only properties

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") methods

ToneRow.findOriginalCenteredTransformations(*otherRow*)[[source]](../_modules/music21/serial.html#ToneRow.findOriginalCenteredTransformations)
:   Gives the list of original-centered serial transformations taking one
    [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow")
    to another, the second specified in the argument. Each transformation is given as a tuple
    of the transformation type and index.

    See [`originalCenteredTransformation()`](#music21.serial.ToneRow.originalCenteredTransformation "music21.serial.ToneRow.originalCenteredTransformation") for an
    explanation of this convention.

    ```python
    >>> chromatic = serial.pcToToneRow(       [2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B',   0, 1])
    >>> reverseChromatic = serial.pcToToneRow([8, 7, 6, 5, 4, 3, 2, 1, 0,   'B', 'A', 9])
    >>> chromatic.findOriginalCenteredTransformations(reverseChromatic)
    [('I', 6), ('R', 7)]
    >>> schoenberg25 = serial.getHistoricalRowByName('SchoenbergOp25')
    >>> schoenberg26 = serial.getHistoricalRowByName('SchoenbergOp26')
    >>> schoenberg25.findOriginalCenteredTransformations(schoenberg26)
    []
    >>> schoenberg26.findOriginalCenteredTransformations(
    ...     schoenberg26.originalCenteredTransformation('RI',8))
    [('RI', 8)]
    ```

ToneRow.findZeroCenteredTransformations(*otherRow*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/music21/serial.html#ToneRow.findZeroCenteredTransformations)
:   Gives the list of zero-centered serial transformations
    taking one [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow")
    to another, the second specified in the argument. Each transformation is given as a
    tuple of the transformation type and index.

    See [`zeroCenteredTransformation()`](#music21.serial.ToneRow.zeroCenteredTransformation "music21.serial.ToneRow.zeroCenteredTransformation") for
    an explanation of this convention.

    ```python
    >>> chromatic = serial.pcToToneRow([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1])
    >>> reverseChromatic = serial.pcToToneRow([8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 10, 9])
    >>> chromatic.findZeroCenteredTransformations(reverseChromatic)
    [('I', 8), ('R', 9)]
    >>> schoenberg25 = serial.getHistoricalRowByName('SchoenbergOp25')
    >>> schoenberg26 = serial.pcToToneRow(serial.getHistoricalRowByName(
    ...                                        'SchoenbergOp26').row)
    >>> schoenberg25.findZeroCenteredTransformations(schoenberg26)
    []
    >>> schoenberg26.findZeroCenteredTransformations(
    ...     schoenberg26.zeroCenteredTransformation('RI', 8))
    [('RI', 8)]
    ```

ToneRow.getIntervalsAsString()[[source]](../_modules/music21/serial.html#ToneRow.getIntervalsAsString)
:   Returns the string of intervals between consecutive pitch classes of
    a [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow").
    ‘T’ = 10, ‘E’ = 11.

    ```python
    >>> cRow = serial.pcToToneRow([0])
    >>> cRow.getIntervalsAsString()
    ''
    >>> reverseChromatic = serial.pcToToneRow([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    >>> reverseChromatic.getIntervalsAsString()
    'EEEEEEEEEEE'
    ```

ToneRow.isSameRow(*other*)[[source]](../_modules/music21/serial.html#ToneRow.isSameRow)
:   Convenience function describing if two rows are the same.

    ```python
    >>> row1 = serial.pcToToneRow([6, 7, 8])
    >>> row2 = serial.pcToToneRow([-6, 19, 128])
    >>> row3 = serial.pcToToneRow([6, 7, -8])
    >>> row1.isSameRow(row2)
    True
    >>> row2.isSameRow(row1)
    True
    >>> row1.isSameRow(row3)
    False
    ```

ToneRow.isTwelveToneRow()[[source]](../_modules/music21/serial.html#ToneRow.isTwelveToneRow)
:   Describes whether a [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") constitutes
    a twelve-tone row. Note that a
    [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") object might not be a twelve-tone row.

    ```python
    >>> serial.ToneRow([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]).isTwelveToneRow()
    True
    >>> serial.ToneRow([0, 4, 8]).isTwelveToneRow()
    False
    >>> serial.ToneRow([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]).isTwelveToneRow()
    False
    ```

ToneRow.makeTwelveToneRow()[[source]](../_modules/music21/serial.html#ToneRow.makeTwelveToneRow)
:   Convenience function returning a [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") with the
    same pitches.
    Note that a [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") may be created without being a
    true twelve tone row.

    ```python
    >>> r1 = serial.pcToToneRow(range(11))
    >>> type(r1)
    <class 'music21.serial.ToneRow'>
    >>> n = note.Note()
    >>> n.pitch.pitchClass = 11
    >>> r1.append(n)
    >>> r2 = r1.makeTwelveToneRow()
    >>> type(r2)
    <class 'music21.serial.TwelveToneRow'>
    ```

ToneRow.noteNames()[[source]](../_modules/music21/serial.html#ToneRow.noteNames)
:   Convenience function showing the note names of a
    [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") as a list.

    ```python
    >>> chromatic = serial.TwelveToneRow(range(12))
    >>> chromatic.noteNames()
    ['C', 'C#', 'D', 'E-', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B-', 'B']
    ```

    ```python
    >>> halfStep = serial.ToneRow([0, 1])
    >>> halfStep.noteNames()
    ['C', 'C#']
    ```

ToneRow.originalCenteredTransformation(*transformationType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](../_modules/music21/serial.html#ToneRow.originalCenteredTransformation)
:   Returns a [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") giving a transformation of a tone row.
    Admissible transformations are ‘T’ (transposition), ‘I’ (inversion),
    ‘R’ (retrograde), and ‘RI’ (retrograde inversion).

    In the “original-centered” convention,
    which is less common than the “zero-centered” convention, the original row is not initially
    transposed to start on the pitch class 0. Thus, the transformation Tn transposes
    the original row up by n semitones, and the transformations In, Rn, and RIn first
    transform the row appropriately (without transposition), then transpose the resulting
    row by n semitones.

    ```python
    >>> chromatic = serial.pcToToneRow(range(12))
    >>> chromatic.pitchClasses()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    >>> chromaticP3 = chromatic.originalCenteredTransformation('T',3)
    >>> chromaticP3.pitchClasses()
    [3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
    >>> chromaticI6 = chromatic.originalCenteredTransformation('I',6)
    >>> chromaticI6.pitchClasses()
    [6, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 7]
    >>> schoenberg = serial.getHistoricalRowByName('SchoenbergOp26')
    >>> schoenberg.pitchClasses()
    [3, 7, 9, 11, 1, 0, 10, 2, 4, 6, 8, 5]
    >>> schoenbergR8 = schoenberg.originalCenteredTransformation('R',8)
    >>> schoenbergR8.pitchClasses()
    [1, 4, 2, 0, 10, 6, 8, 9, 7, 5, 3, 11]
    >>> schoenbergRI9 = schoenberg.originalCenteredTransformation('RI',9)
    >>> schoenbergRI9.noteNames()
    ['B-', 'G', 'A', 'B', 'C#', 'F', 'E-', 'D', 'E', 'F#', 'G#', 'C']
    ```

ToneRow.pitchClasses()[[source]](../_modules/music21/serial.html#ToneRow.pitchClasses)
:   Convenience function showing the pitch classes of a
    [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") as a list.

    ```python
    >>> fiveFold = [5 * i for i in range(12)]
    >>> fiveFold
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    ```

    ```python
    >>> quintupleRow = serial.pcToToneRow(fiveFold)
    >>> quintupleRow
    <music21.serial.TwelveToneRow 05A3816B4927>
    >>> quintupleRow.pitchClasses()
    [0, 5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7]
    ```

    ```python
    >>> halfStep = serial.pcToToneRow([0, 1])
    >>> halfStep.pitchClasses()
    [0, 1]
    ```

ToneRow.zeroCenteredTransformation(*transformationType*, *index*)[[source]](../_modules/music21/serial.html#ToneRow.zeroCenteredTransformation)
:   Returns a [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") giving a transformation of a tone row.
    Admissible transformationTypes are ‘P’ (prime), ‘I’ (inversion),
    ‘R’ (retrograde), and ‘RI’ (retrograde inversion).

    In the “zero-centered” convention,
    the transformations Pn and In start on the pitch class n, and the transformations
    Rn and RIn end on the pitch class n.

    ```python
    >>> chromatic = serial.pcToToneRow(range(12))
    >>> chromatic.pitchClasses()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    >>> chromaticP3 = chromatic.zeroCenteredTransformation('P',3)
    >>> chromaticP3.pitchClasses()
    [3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2]
    >>> chromaticI6 = chromatic.zeroCenteredTransformation('I',6)
    >>> chromaticI6.pitchClasses()
    [6, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 7]
    >>> schoenberg = serial.getHistoricalRowByName('SchoenbergOp26')
    >>> schoenberg.pitchClasses()
    [3, 7, 9, 11, 1, 0, 10, 2, 4, 6, 8, 5]
    >>> schoenbergR8 = schoenberg.zeroCenteredTransformation('R',8)
    >>> schoenbergR8.pitchClasses()
    [10, 1, 11, 9, 7, 3, 5, 6, 4, 2, 0, 8]
    >>> schoenbergRI9 = schoenberg.zeroCenteredTransformation('RI',9)
    >>> schoenbergRI9.noteNames()
    ['G', 'E', 'F#', 'G#', 'B-', 'D', 'C', 'B', 'C#', 'E-', 'F', 'A']
    ```

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](moduleStreamBase.html#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](moduleStreamBase.html#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") instance variables

ToneRow.row
:   A list representing the pitch class values of the row.

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TwelveToneRow

class music21.serial.TwelveToneRow(*row=None*, *\*\*keywords*)[[source]](../_modules/music21/serial.html#TwelveToneRow)
:   A Stream representation of a twelve-tone row, capable of producing a 12-tone matrix.

[`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") bases

* [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow")
* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") read-only properties

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") methods

TwelveToneRow.areCombinatorial(*transType1: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *index1: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *transType2: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *index2: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/serial.html#TwelveToneRow.areCombinatorial)
:   Describes whether two transformations of a twelve-tone row are combinatorial.

    The first and second arguments describe one transformation, while the third and fourth
    describe another.

    First, let’s take a row we know to have a combinatoriality pair:

    ```python
    >>> moses = serial.getHistoricalRowByName('SchoenbergMosesAron')
    >>> moses.pitchClasses()
    [9, 10, 4, 2, 3, 1, 7, 5, 6, 8, 11, 0]
    ```

    Combinatoriality holds here between P0 and I3

    ```python
    >>> moses.areCombinatorial('P', 0, 'I', 3)
    True
    ```

    And a combinatorial pair like this between P0 and I3 will also hold
    if you modify both rows in the same way, e.g.
    if you transpose both by the same amount

    ```python
    >>> moses.areCombinatorial('P', 1, 'I', 4)
    True
    ```

    or if you retrograde both

    ```python
    >>> moses.areCombinatorial('R', 1, 'RI', 4)
    True
    ```

    Any modification made to one row form and not the other means all bets are off

    ```python
    >>> moses.areCombinatorial('R', 6, 'RI', 4)
    False
    ```

    * Changed in v7: convention is no longer necessary and no longer used.
      Renamed to unused\_convention and defaults None; to be removed in v8.

TwelveToneRow.findHistorical()[[source]](../_modules/music21/serial.html#TwelveToneRow.findHistorical)
:   Checks if a given [`music21.serial.TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") is the same as
    any of the historical
    twelve-tone rows stored by music21: see [`music21.serial.getHistoricalRowByName()`](#music21.serial.getHistoricalRowByName "music21.serial.getHistoricalRowByName").
    Returns a list of names of historical rows to which the input row is identical.

    ```python
    >>> row = serial.pcToToneRow([2, 3, 9, 1, 11, 5, 8, 7, 4, 0, 10, 6])
    >>> row.findHistorical()
    ['SchoenbergOp32']
    >>> chromatic = serial.pcToToneRow(range(12))
    >>> chromatic.findHistorical()
    []
    ```

TwelveToneRow.findTransformedHistorical(*convention*)[[source]](../_modules/music21/serial.html#TwelveToneRow.findTransformedHistorical)
:   Checks if a given [`music21.serial.TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") is a transformation of
    any historical
    twelve-tone row stored by music21 (see [`music21.serial.getHistoricalRowByName()`](#music21.serial.getHistoricalRowByName "music21.serial.getHistoricalRowByName")).
    Returns a list
    of tuples, the tuple consisting of the name of a historical row, and a
    list of transformations relating
    the input row to the historical row.

    The convention for serial transformations must also be specified as ‘zero’ or
    ‘original’, as explained
    in [`findZeroCenteredTransformations()`](#music21.serial.ToneRow.findZeroCenteredTransformations "music21.serial.ToneRow.findZeroCenteredTransformations") and
    [`findOriginalCenteredTransformations()`](#music21.serial.ToneRow.findOriginalCenteredTransformations "music21.serial.ToneRow.findOriginalCenteredTransformations").

    ```python
    >>> row = serial.pcToToneRow([5, 9, 11, 3, 6, 7, 4, 10, 0, 8, 2, 1])
    >>> row.findTransformedHistorical('original')
    [('SchoenbergOp32', [('R', 11)])]
    ```

TwelveToneRow.getLinkClassification()[[source]](../_modules/music21/serial.html#TwelveToneRow.getLinkClassification)
:   Gives the classification number of a Link Chord
    (as given in <http://www.johnlinkmusic.com/LinkChords.pdf>),
    that is, is an all-interval twelve-tone row containing a voicing of the
    all-trichord hexachord: [0, 1, 2, 4, 7, 8].
    In addition, gives a list of sets of five contiguous intervals
    within the row representing a voicing
    of the all-trichord hexachord. Note that the interval sets may be transformed.

    Named for John Link who discovered them.

    ```python
    >>> bergLyric = serial.getHistoricalRowByName('BergLyricSuite')
    >>> bergLyric.pitchClasses()
    [5, 4, 0, 9, 7, 2, 8, 1, 3, 6, 10, 11]
    >>> bergLyric.isAllInterval()
    True
    >>> bergLyric.getLinkClassification()
    (None, [])
    >>> link = serial.pcToToneRow([0, 3, 8, 2, 10, 11, 9, 4, 1, 5, 7, 6])
    >>> link.getLinkClassification()
    (62, ['8352E'])
    >>> doubleLink = serial.pcToToneRow([0, 1, 8, 5, 7, 10, 4, 3, 11, 9, 2, 6])
    >>> doubleLink.getLinkClassification()
    (33, ['236E8', '36E8T'])
    ```

TwelveToneRow.isAllInterval() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/serial.html#TwelveToneRow.isAllInterval)
:   Describes whether a [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") is an all-interval row.

    ```python
    >>> chromatic = serial.pcToToneRow(range(12))
    >>> chromatic.pitchClasses()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    >>> chromatic.isAllInterval()
    False
    >>> bergLyric = serial.getHistoricalRowByName('BergLyricSuite')
    >>> bergLyric.pitchClasses()
    [5, 4, 0, 9, 7, 2, 8, 1, 3, 6, 10, 11]
    >>> bergLyric.isAllInterval()
    True
    ```

TwelveToneRow.isLinkChord() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/serial.html#TwelveToneRow.isLinkChord)
:   Describes whether a [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") is a Link Chord.

    ```python
    >>> bergLyric = serial.getHistoricalRowByName('BergLyricSuite')
    >>> bergLyric.pitchClasses()
    [5, 4, 0, 9, 7, 2, 8, 1, 3, 6, 10, 11]
    >>> bergLyric.isAllInterval()
    True
    >>> bergLyric.isLinkChord()
    False
    >>> link = serial.pcToToneRow([0, 3, 8, 2, 10, 11, 9, 4, 1, 5, 7, 6])
    >>> link.isLinkChord()
    True
    >>> doubleLink = serial.pcToToneRow([0, 1, 8, 5, 7, 10, 4, 3, 11, 9, 2, 6])
    >>> doubleLink.isLinkChord()
    True
    ```

TwelveToneRow.matrix()[[source]](../_modules/music21/serial.html#TwelveToneRow.matrix)
:   Returns a [`TwelveToneMatrix`](#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") object for the row.
    That object can just be printed (or displayed via .show())

    ```python
    >>> src = serial.getHistoricalRowByName('SchoenbergOp37')
    >>> [p.name for p in src]
    ['D', 'C#', 'A', 'B-', 'F', 'E-', 'E', 'C', 'G#', 'G', 'F#', 'B']
    >>> len(src)
    12
    >>> s37 = serial.getHistoricalRowByName('SchoenbergOp37').matrix()
    >>> print(s37)
      0  B  7  8  3  1  2  A  6  5  4  9
      1  0  8  9  4  2  3  B  7  6  5  A
      5  4  0  1  8  6  7  3  B  A  9  2
      4  3  B  0  7  5  6  2  A  9  8  1
    ...
    >>> [str(e.pitch) for e in s37[0]]
    ['C', 'B', 'G', 'G#', 'E-', 'C#', 'D', 'B-', 'F#', 'F', 'E', 'A']
    ```

Methods inherited from [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow"):

|  |  |  |
| --- | --- | --- |
| * [`findOriginalCenteredTransformations()`](#music21.serial.ToneRow.findOriginalCenteredTransformations "music21.serial.ToneRow.findOriginalCenteredTransformations") * [`findZeroCenteredTransformations()`](#music21.serial.ToneRow.findZeroCenteredTransformations "music21.serial.ToneRow.findZeroCenteredTransformations") * [`getIntervalsAsString()`](#music21.serial.ToneRow.getIntervalsAsString "music21.serial.ToneRow.getIntervalsAsString") * [`isSameRow()`](#music21.serial.ToneRow.isSameRow "music21.serial.ToneRow.isSameRow") | * [`isTwelveToneRow()`](#music21.serial.ToneRow.isTwelveToneRow "music21.serial.ToneRow.isTwelveToneRow") * [`makeTwelveToneRow()`](#music21.serial.ToneRow.makeTwelveToneRow "music21.serial.ToneRow.makeTwelveToneRow") * [`noteNames()`](#music21.serial.ToneRow.noteNames "music21.serial.ToneRow.noteNames") | * [`originalCenteredTransformation()`](#music21.serial.ToneRow.originalCenteredTransformation "music21.serial.ToneRow.originalCenteredTransformation") * [`pitchClasses()`](#music21.serial.ToneRow.pitchClasses "music21.serial.ToneRow.pitchClasses") * [`zeroCenteredTransformation()`](#music21.serial.ToneRow.zeroCenteredTransformation "music21.serial.ToneRow.zeroCenteredTransformation") |

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](moduleStreamBase.html#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](moduleStreamBase.html#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") instance variables

Instance variables inherited from [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow"):

|  |  |  |
| --- | --- | --- |
| * [`row`](#music21.serial.ToneRow.row "music21.serial.ToneRow.row") |  |  |

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## HistoricalTwelveToneRow

class music21.serial.HistoricalTwelveToneRow(*composer: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *opus: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *title: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = None*, *row=None*, *\*\*keywords*)[[source]](../_modules/music21/serial.html#HistoricalTwelveToneRow)
:   Subclass of [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow") storing additional attributes of a
    twelve-tone row used in the historical literature.

[`HistoricalTwelveToneRow`](#music21.serial.HistoricalTwelveToneRow "music21.serial.HistoricalTwelveToneRow") bases

* [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow")
* [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow")
* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`HistoricalTwelveToneRow`](#music21.serial.HistoricalTwelveToneRow "music21.serial.HistoricalTwelveToneRow") read-only properties

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`HistoricalTwelveToneRow`](#music21.serial.HistoricalTwelveToneRow "music21.serial.HistoricalTwelveToneRow") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`HistoricalTwelveToneRow`](#music21.serial.HistoricalTwelveToneRow "music21.serial.HistoricalTwelveToneRow") methods

HistoricalTwelveToneRow.mergeAttributes(*other*)[[source]](../_modules/music21/serial.html#HistoricalTwelveToneRow.mergeAttributes)
:   Merge relevant attributes from the Other stream into this one.

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note())
    >>> s.autoSort = False
    >>> s.id = 'hi'
    >>> s2 = stream.Stream()
    >>> s2.mergeAttributes(s)
    >>> s2.autoSort
    False
    >>> s2
    <music21.stream.Stream hi>
    >>> len(s2)
    0
    ```

Methods inherited from [`TwelveToneRow`](#music21.serial.TwelveToneRow "music21.serial.TwelveToneRow"):

|  |  |  |
| --- | --- | --- |
| * [`areCombinatorial()`](#music21.serial.TwelveToneRow.areCombinatorial "music21.serial.TwelveToneRow.areCombinatorial") * [`findHistorical()`](#music21.serial.TwelveToneRow.findHistorical "music21.serial.TwelveToneRow.findHistorical") * [`findTransformedHistorical()`](#music21.serial.TwelveToneRow.findTransformedHistorical "music21.serial.TwelveToneRow.findTransformedHistorical") | * [`getLinkClassification()`](#music21.serial.TwelveToneRow.getLinkClassification "music21.serial.TwelveToneRow.getLinkClassification") * [`isAllInterval()`](#music21.serial.TwelveToneRow.isAllInterval "music21.serial.TwelveToneRow.isAllInterval") | * [`isLinkChord()`](#music21.serial.TwelveToneRow.isLinkChord "music21.serial.TwelveToneRow.isLinkChord") * [`matrix()`](#music21.serial.TwelveToneRow.matrix "music21.serial.TwelveToneRow.matrix") |

Methods inherited from [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow"):

|  |  |  |
| --- | --- | --- |
| * [`findOriginalCenteredTransformations()`](#music21.serial.ToneRow.findOriginalCenteredTransformations "music21.serial.ToneRow.findOriginalCenteredTransformations") * [`findZeroCenteredTransformations()`](#music21.serial.ToneRow.findZeroCenteredTransformations "music21.serial.ToneRow.findZeroCenteredTransformations") * [`getIntervalsAsString()`](#music21.serial.ToneRow.getIntervalsAsString "music21.serial.ToneRow.getIntervalsAsString") * [`isSameRow()`](#music21.serial.ToneRow.isSameRow "music21.serial.ToneRow.isSameRow") | * [`isTwelveToneRow()`](#music21.serial.ToneRow.isTwelveToneRow "music21.serial.ToneRow.isTwelveToneRow") * [`makeTwelveToneRow()`](#music21.serial.ToneRow.makeTwelveToneRow "music21.serial.ToneRow.makeTwelveToneRow") * [`noteNames()`](#music21.serial.ToneRow.noteNames "music21.serial.ToneRow.noteNames") | * [`originalCenteredTransformation()`](#music21.serial.ToneRow.originalCenteredTransformation "music21.serial.ToneRow.originalCenteredTransformation") * [`pitchClasses()`](#music21.serial.ToneRow.pitchClasses "music21.serial.ToneRow.pitchClasses") * [`zeroCenteredTransformation()`](#music21.serial.ToneRow.zeroCenteredTransformation "music21.serial.ToneRow.zeroCenteredTransformation") |

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](moduleStreamBase.html#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](moduleStreamBase.html#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`HistoricalTwelveToneRow`](#music21.serial.HistoricalTwelveToneRow "music21.serial.HistoricalTwelveToneRow") instance variables

HistoricalTwelveToneRow.composer
:   The name of the composer, or None. (String)

HistoricalTwelveToneRow.opus
:   The opus of the work, or None. (String)

HistoricalTwelveToneRow.title
:   The title of the work, or None. (String)

Instance variables inherited from [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow"):

|  |  |  |
| --- | --- | --- |
| * [`row`](#music21.serial.ToneRow.row "music21.serial.ToneRow.row") |  |  |

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## TwelveToneMatrix

class music21.serial.TwelveToneMatrix(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *\**, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*keywords*)[[source]](../_modules/music21/serial.html#TwelveToneMatrix)
:   An object representation of a 2-dimensional array of 12 pitches.
    Internal representation is as a `Stream`,
    which stores 12 Streams, each Stream a horizontal row of pitches
    in the matrix.

    This object is commonly used by calling the
    `matrix()` method of
    `TwelveToneRow` (or a subclass).

    ```python
    >>> ttr = serial.TwelveToneRow([0, 2, 11, 7, 8, 3, 9, 1, 4, 10, 6, 5])
    >>> aMatrix = ttr.matrix()
    >>> print(aMatrix)
      0  2  B  7  8  3  9  1  4  A  6  5
      A  0  9  5  6  1  7  B  2  8  4  3
      1  3  0  8  9  4  A  2  5  B  7  6
      5  7  4  0  1  8  2  6  9  3  B  A
      4  6  3  B  0  7  1  5  8  2  A  9
      9  B  8  4  5  0  6  A  1  7  3  2
      3  5  2  A  B  6  0  4  7  1  9  8
      B  1  A  6  7  2  8  0  3  9  5  4
      8  A  7  3  4  B  5  9  0  6  2  1
      2  4  1  9  A  5  B  3  6  0  8  7
      6  8  5  1  2  9  3  7  A  4  0  B
      7  9  6  2  3  A  4  8  B  5  1  0
    ```

    ```python
    >>> repr(aMatrix)
    '<music21.serial.TwelveToneMatrix for [<music21.serial.TwelveToneRow row-1>]>'
    ```

    ```python
    >>> fourthQuartetMatrix = serial.getHistoricalRowByName('SchoenbergOp37').matrix()
    >>> repr(fourthQuartetMatrix)
    '<music21.serial.TwelveToneMatrix for
         [<music21.serial.HistoricalTwelveToneRow Schoenberg Op. 37 Fourth String Quartet>]>'
    ```

[`TwelveToneMatrix`](#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") bases

* [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")
* [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TwelveToneMatrix`](#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") read-only properties

Read-only properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleStreamBase.html#music21.stream.base.Stream.beat "music21.stream.base.Stream.beat") * [`beatDuration`](moduleStreamBase.html#music21.stream.base.Stream.beatDuration "music21.stream.base.Stream.beatDuration") * [`beatStr`](moduleStreamBase.html#music21.stream.base.Stream.beatStr "music21.stream.base.Stream.beatStr") * [`beatStrength`](moduleStreamBase.html#music21.stream.base.Stream.beatStrength "music21.stream.base.Stream.beatStrength") * [`highestOffset`](moduleStreamBase.html#music21.stream.base.Stream.highestOffset "music21.stream.base.Stream.highestOffset") | * [`highestTime`](moduleStreamBase.html#music21.stream.base.Stream.highestTime "music21.stream.base.Stream.highestTime") * [`isGapless`](moduleStreamBase.html#music21.stream.base.Stream.isGapless "music21.stream.base.Stream.isGapless") * [`lowestOffset`](moduleStreamBase.html#music21.stream.base.Stream.lowestOffset "music21.stream.base.Stream.lowestOffset") * [`notes`](moduleStreamBase.html#music21.stream.base.Stream.notes "music21.stream.base.Stream.notes") * [`notesAndRests`](moduleStreamBase.html#music21.stream.base.Stream.notesAndRests "music21.stream.base.Stream.notesAndRests") | * [`pitches`](moduleStreamBase.html#music21.stream.base.Stream.pitches "music21.stream.base.Stream.pitches") * [`secondsMap`](moduleStreamBase.html#music21.stream.base.Stream.secondsMap "music21.stream.base.Stream.secondsMap") * [`spanners`](moduleStreamBase.html#music21.stream.base.Stream.spanners "music21.stream.base.Stream.spanners") * [`voices`](moduleStreamBase.html#music21.stream.base.Stream.voices "music21.stream.base.Stream.voices") |

Read-only properties inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`spannerBundle`](moduleStreamCore.html#music21.stream.core.StreamCore.spannerBundle "music21.stream.core.StreamCore.spannerBundle") |  |  |

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") | * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TwelveToneMatrix`](#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") read/write properties

Read/write properties inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`atSoundingPitch`](moduleStreamBase.html#music21.stream.base.Stream.atSoundingPitch "music21.stream.base.Stream.atSoundingPitch") * [`clef`](moduleStreamBase.html#music21.stream.base.Stream.clef "music21.stream.base.Stream.clef") * [`duration`](moduleStreamBase.html#music21.stream.base.Stream.duration "music21.stream.base.Stream.duration") * [`elements`](moduleStreamBase.html#music21.stream.base.Stream.elements "music21.stream.base.Stream.elements") | * [`finalBarline`](moduleStreamBase.html#music21.stream.base.Stream.finalBarline "music21.stream.base.Stream.finalBarline") * [`keySignature`](moduleStreamBase.html#music21.stream.base.Stream.keySignature "music21.stream.base.Stream.keySignature") * [`metadata`](moduleStreamBase.html#music21.stream.base.Stream.metadata "music21.stream.base.Stream.metadata") | * [`seconds`](moduleStreamBase.html#music21.stream.base.Stream.seconds "music21.stream.base.Stream.seconds") * [`staffLines`](moduleStreamBase.html#music21.stream.base.Stream.staffLines "music21.stream.base.Stream.staffLines") * [`timeSignature`](moduleStreamBase.html#music21.stream.base.Stream.timeSignature "music21.stream.base.Stream.timeSignature") |

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`TwelveToneMatrix`](#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") methods

Methods inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleStreamBase.html#music21.stream.base.Stream.__eq__ "music21.stream.base.Stream.__eq__") * [`__getitem__()`](moduleStreamBase.html#music21.stream.base.Stream.__getitem__ "music21.stream.base.Stream.__getitem__") * [`activateVariants()`](moduleStreamBase.html#music21.stream.base.Stream.activateVariants "music21.stream.base.Stream.activateVariants") * [`addGroupForElements()`](moduleStreamBase.html#music21.stream.base.Stream.addGroupForElements "music21.stream.base.Stream.addGroupForElements") * [`allPlayingWhileSounding()`](moduleStreamBase.html#music21.stream.base.Stream.allPlayingWhileSounding "music21.stream.base.Stream.allPlayingWhileSounding") * [`analyze()`](moduleStreamBase.html#music21.stream.base.Stream.analyze "music21.stream.base.Stream.analyze") * [`append()`](moduleStreamBase.html#music21.stream.base.Stream.append "music21.stream.base.Stream.append") * [`attachIntervalsBetweenStreams()`](moduleStreamBase.html#music21.stream.base.Stream.attachIntervalsBetweenStreams "music21.stream.base.Stream.attachIntervalsBetweenStreams") * [`attachMelodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.attachMelodicIntervals "music21.stream.base.Stream.attachMelodicIntervals") * [`augmentOrDiminish()`](moduleStreamBase.html#music21.stream.base.Stream.augmentOrDiminish "music21.stream.base.Stream.augmentOrDiminish") * [`beatAndMeasureFromOffset()`](moduleStreamBase.html#music21.stream.base.Stream.beatAndMeasureFromOffset "music21.stream.base.Stream.beatAndMeasureFromOffset") * [`chordify()`](moduleStreamBase.html#music21.stream.base.Stream.chordify "music21.stream.base.Stream.chordify") * [`clear()`](moduleStreamBase.html#music21.stream.base.Stream.clear "music21.stream.base.Stream.clear") * [`cloneEmpty()`](moduleStreamBase.html#music21.stream.base.Stream.cloneEmpty "music21.stream.base.Stream.cloneEmpty") * [`containerInHierarchy()`](moduleStreamBase.html#music21.stream.base.Stream.containerInHierarchy "music21.stream.base.Stream.containerInHierarchy") * [`elementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.elementOffset "music21.stream.base.Stream.elementOffset") * [`expandRepeats()`](moduleStreamBase.html#music21.stream.base.Stream.expandRepeats "music21.stream.base.Stream.expandRepeats") * [`explode()`](moduleStreamBase.html#music21.stream.base.Stream.explode "music21.stream.base.Stream.explode") * [`extendDuration()`](moduleStreamBase.html#music21.stream.base.Stream.extendDuration "music21.stream.base.Stream.extendDuration") * [`extendTies()`](moduleStreamBase.html#music21.stream.base.Stream.extendTies "music21.stream.base.Stream.extendTies") * [`extractContext()`](moduleStreamBase.html#music21.stream.base.Stream.extractContext "music21.stream.base.Stream.extractContext") * [`findConsecutiveNotes()`](moduleStreamBase.html#music21.stream.base.Stream.findConsecutiveNotes "music21.stream.base.Stream.findConsecutiveNotes") * [`findGaps()`](moduleStreamBase.html#music21.stream.base.Stream.findGaps "music21.stream.base.Stream.findGaps") * [`first()`](moduleStreamBase.html#music21.stream.base.Stream.first "music21.stream.base.Stream.first") * [`flatten()`](moduleStreamBase.html#music21.stream.base.Stream.flatten "music21.stream.base.Stream.flatten") * [`flattenUnnecessaryVoices()`](moduleStreamBase.html#music21.stream.base.Stream.flattenUnnecessaryVoices "music21.stream.base.Stream.flattenUnnecessaryVoices") * [`getElementAfterElement()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAfterElement "music21.stream.base.Stream.getElementAfterElement") * [`getElementAtOrBefore()`](moduleStreamBase.html#music21.stream.base.Stream.getElementAtOrBefore "music21.stream.base.Stream.getElementAtOrBefore") * [`getElementBeforeOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementBeforeOffset "music21.stream.base.Stream.getElementBeforeOffset") * [`getElementById()`](moduleStreamBase.html#music21.stream.base.Stream.getElementById "music21.stream.base.Stream.getElementById") * [`getElementsByClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByClass "music21.stream.base.Stream.getElementsByClass") * [`getElementsByGroup()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByGroup "music21.stream.base.Stream.getElementsByGroup") * [`getElementsByOffset()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsByOffset "music21.stream.base.Stream.getElementsByOffset") * [`getElementsNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.getElementsNotOfClass "music21.stream.base.Stream.getElementsNotOfClass") * [`getInstrument()`](moduleStreamBase.html#music21.stream.base.Stream.getInstrument "music21.stream.base.Stream.getInstrument") * [`getInstruments()`](moduleStreamBase.html#music21.stream.base.Stream.getInstruments "music21.stream.base.Stream.getInstruments") * [`getOverlaps()`](moduleStreamBase.html#music21.stream.base.Stream.getOverlaps "music21.stream.base.Stream.getOverlaps") | * [`getTimeSignatures()`](moduleStreamBase.html#music21.stream.base.Stream.getTimeSignatures "music21.stream.base.Stream.getTimeSignatures") * [`hasElement()`](moduleStreamBase.html#music21.stream.base.Stream.hasElement "music21.stream.base.Stream.hasElement") * [`hasElementOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.hasElementOfClass "music21.stream.base.Stream.hasElementOfClass") * [`hasMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.hasMeasures "music21.stream.base.Stream.hasMeasures") * [`hasPartLikeStreams()`](moduleStreamBase.html#music21.stream.base.Stream.hasPartLikeStreams "music21.stream.base.Stream.hasPartLikeStreams") * [`hasVoices()`](moduleStreamBase.html#music21.stream.base.Stream.hasVoices "music21.stream.base.Stream.hasVoices") * [`haveAccidentalsBeenMade()`](moduleStreamBase.html#music21.stream.base.Stream.haveAccidentalsBeenMade "music21.stream.base.Stream.haveAccidentalsBeenMade") * [`index()`](moduleStreamBase.html#music21.stream.base.Stream.index "music21.stream.base.Stream.index") * [`insert()`](moduleStreamBase.html#music21.stream.base.Stream.insert "music21.stream.base.Stream.insert") * [`insertAndShift()`](moduleStreamBase.html#music21.stream.base.Stream.insertAndShift "music21.stream.base.Stream.insertAndShift") * [`insertIntoNoteOrChord()`](moduleStreamBase.html#music21.stream.base.Stream.insertIntoNoteOrChord "music21.stream.base.Stream.insertIntoNoteOrChord") * [`invertDiatonic()`](moduleStreamBase.html#music21.stream.base.Stream.invertDiatonic "music21.stream.base.Stream.invertDiatonic") * [`isSequence()`](moduleStreamBase.html#music21.stream.base.Stream.isSequence "music21.stream.base.Stream.isSequence") * [`isTwelveTone()`](moduleStreamBase.html#music21.stream.base.Stream.isTwelveTone "music21.stream.base.Stream.isTwelveTone") * [`isWellFormedNotation()`](moduleStreamBase.html#music21.stream.base.Stream.isWellFormedNotation "music21.stream.base.Stream.isWellFormedNotation") * [`iter()`](moduleStreamBase.html#music21.stream.base.Stream.iter "music21.stream.base.Stream.iter") * [`last()`](moduleStreamBase.html#music21.stream.base.Stream.last "music21.stream.base.Stream.last") * [`lyrics()`](moduleStreamBase.html#music21.stream.base.Stream.lyrics "music21.stream.base.Stream.lyrics") * [`makeAccidentals()`](moduleStreamBase.html#music21.stream.base.Stream.makeAccidentals "music21.stream.base.Stream.makeAccidentals") * [`makeBeams()`](moduleStreamBase.html#music21.stream.base.Stream.makeBeams "music21.stream.base.Stream.makeBeams") * [`makeImmutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeImmutable "music21.stream.base.Stream.makeImmutable") * [`makeMeasures()`](moduleStreamBase.html#music21.stream.base.Stream.makeMeasures "music21.stream.base.Stream.makeMeasures") * [`makeMutable()`](moduleStreamBase.html#music21.stream.base.Stream.makeMutable "music21.stream.base.Stream.makeMutable") * [`makeNotation()`](moduleStreamBase.html#music21.stream.base.Stream.makeNotation "music21.stream.base.Stream.makeNotation") * [`makeRests()`](moduleStreamBase.html#music21.stream.base.Stream.makeRests "music21.stream.base.Stream.makeRests") * [`makeTies()`](moduleStreamBase.html#music21.stream.base.Stream.makeTies "music21.stream.base.Stream.makeTies") * [`makeVoices()`](moduleStreamBase.html#music21.stream.base.Stream.makeVoices "music21.stream.base.Stream.makeVoices") * [`measure()`](moduleStreamBase.html#music21.stream.base.Stream.measure "music21.stream.base.Stream.measure") * [`measureOffsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.measureOffsetMap "music21.stream.base.Stream.measureOffsetMap") * [`measures()`](moduleStreamBase.html#music21.stream.base.Stream.measures "music21.stream.base.Stream.measures") * [`melodicIntervals()`](moduleStreamBase.html#music21.stream.base.Stream.melodicIntervals "music21.stream.base.Stream.melodicIntervals") * [`mergeAttributes()`](moduleStreamBase.html#music21.stream.base.Stream.mergeAttributes "music21.stream.base.Stream.mergeAttributes") * [`mergeElements()`](moduleStreamBase.html#music21.stream.base.Stream.mergeElements "music21.stream.base.Stream.mergeElements") * [`metronomeMarkBoundaries()`](moduleStreamBase.html#music21.stream.base.Stream.metronomeMarkBoundaries "music21.stream.base.Stream.metronomeMarkBoundaries") * [`offsetMap()`](moduleStreamBase.html#music21.stream.base.Stream.offsetMap "music21.stream.base.Stream.offsetMap") * [`playingWhenAttacked()`](moduleStreamBase.html#music21.stream.base.Stream.playingWhenAttacked "music21.stream.base.Stream.playingWhenAttacked") * [`plot()`](moduleStreamBase.html#music21.stream.base.Stream.plot "music21.stream.base.Stream.plot") | * [`pop()`](moduleStreamBase.html#music21.stream.base.Stream.pop "music21.stream.base.Stream.pop") * [`quantize()`](moduleStreamBase.html#music21.stream.base.Stream.quantize "music21.stream.base.Stream.quantize") * [`recurse()`](moduleStreamBase.html#music21.stream.base.Stream.recurse "music21.stream.base.Stream.recurse") * [`recurseRepr()`](moduleStreamBase.html#music21.stream.base.Stream.recurseRepr "music21.stream.base.Stream.recurseRepr") * [`remove()`](moduleStreamBase.html#music21.stream.base.Stream.remove "music21.stream.base.Stream.remove") * [`removeByClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByClass "music21.stream.base.Stream.removeByClass") * [`removeByNotOfClass()`](moduleStreamBase.html#music21.stream.base.Stream.removeByNotOfClass "music21.stream.base.Stream.removeByNotOfClass") * [`repeatAppend()`](moduleStreamBase.html#music21.stream.base.Stream.repeatAppend "music21.stream.base.Stream.repeatAppend") * [`repeatInsert()`](moduleStreamBase.html#music21.stream.base.Stream.repeatInsert "music21.stream.base.Stream.repeatInsert") * [`replace()`](moduleStreamBase.html#music21.stream.base.Stream.replace "music21.stream.base.Stream.replace") * [`scaleDurations()`](moduleStreamBase.html#music21.stream.base.Stream.scaleDurations "music21.stream.base.Stream.scaleDurations") * [`scaleOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.scaleOffsets "music21.stream.base.Stream.scaleOffsets") * [`setDerivationMethod()`](moduleStreamBase.html#music21.stream.base.Stream.setDerivationMethod "music21.stream.base.Stream.setDerivationMethod") * [`setElementOffset()`](moduleStreamBase.html#music21.stream.base.Stream.setElementOffset "music21.stream.base.Stream.setElementOffset") * [`shiftElements()`](moduleStreamBase.html#music21.stream.base.Stream.shiftElements "music21.stream.base.Stream.shiftElements") * [`show()`](moduleStreamBase.html#music21.stream.base.Stream.show "music21.stream.base.Stream.show") * [`showVariantAsOssialikePart()`](moduleStreamBase.html#music21.stream.base.Stream.showVariantAsOssialikePart "music21.stream.base.Stream.showVariantAsOssialikePart") * [`simultaneousAttacks()`](moduleStreamBase.html#music21.stream.base.Stream.simultaneousAttacks "music21.stream.base.Stream.simultaneousAttacks") * [`sliceAtOffsets()`](moduleStreamBase.html#music21.stream.base.Stream.sliceAtOffsets "music21.stream.base.Stream.sliceAtOffsets") * [`sliceByBeat()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByBeat "music21.stream.base.Stream.sliceByBeat") * [`sliceByGreatestDivisor()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByGreatestDivisor "music21.stream.base.Stream.sliceByGreatestDivisor") * [`sliceByQuarterLengths()`](moduleStreamBase.html#music21.stream.base.Stream.sliceByQuarterLengths "music21.stream.base.Stream.sliceByQuarterLengths") * [`sort()`](moduleStreamBase.html#music21.stream.base.Stream.sort "music21.stream.base.Stream.sort") * [`sorted()`](moduleStreamBase.html#music21.stream.base.Stream.sorted "music21.stream.base.Stream.sorted") * [`splitAtDurations()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtDurations "music21.stream.base.Stream.splitAtDurations") * [`splitAtQuarterLength()`](moduleStreamBase.html#music21.stream.base.Stream.splitAtQuarterLength "music21.stream.base.Stream.splitAtQuarterLength") * [`splitByClass()`](moduleStreamBase.html#music21.stream.base.Stream.splitByClass "music21.stream.base.Stream.splitByClass") * [`storeAtEnd()`](moduleStreamBase.html#music21.stream.base.Stream.storeAtEnd "music21.stream.base.Stream.storeAtEnd") * [`stripTies()`](moduleStreamBase.html#music21.stream.base.Stream.stripTies "music21.stream.base.Stream.stripTies") * [`template()`](moduleStreamBase.html#music21.stream.base.Stream.template "music21.stream.base.Stream.template") * [`toSoundingPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toSoundingPitch "music21.stream.base.Stream.toSoundingPitch") * [`toWrittenPitch()`](moduleStreamBase.html#music21.stream.base.Stream.toWrittenPitch "music21.stream.base.Stream.toWrittenPitch") * [`transferOffsetToElements()`](moduleStreamBase.html#music21.stream.base.Stream.transferOffsetToElements "music21.stream.base.Stream.transferOffsetToElements") * [`transpose()`](moduleStreamBase.html#music21.stream.base.Stream.transpose "music21.stream.base.Stream.transpose") * [`voicesToParts()`](moduleStreamBase.html#music21.stream.base.Stream.voicesToParts "music21.stream.base.Stream.voicesToParts") * [`write()`](moduleStreamBase.html#music21.stream.base.Stream.write "music21.stream.base.Stream.write") |

Methods inherited from [`StreamCore`](moduleStreamCore.html#music21.stream.core.StreamCore "music21.stream.core.StreamCore"):

|  |  |  |
| --- | --- | --- |
| * [`asTimespans()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTimespans "music21.stream.core.StreamCore.asTimespans") * [`asTree()`](moduleStreamCore.html#music21.stream.core.StreamCore.asTree "music21.stream.core.StreamCore.asTree") * [`coreAppend()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreAppend "music21.stream.core.StreamCore.coreAppend") * [`coreCopyAsDerivation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreCopyAsDerivation "music21.stream.core.StreamCore.coreCopyAsDerivation") | * [`coreElementsChanged()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreElementsChanged "music21.stream.core.StreamCore.coreElementsChanged") * [`coreGatherMissingSpanners()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGatherMissingSpanners "music21.stream.core.StreamCore.coreGatherMissingSpanners") * [`coreGetElementByMemoryLocation()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGetElementByMemoryLocation "music21.stream.core.StreamCore.coreGetElementByMemoryLocation") * [`coreGuardBeforeAddElement()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreGuardBeforeAddElement "music21.stream.core.StreamCore.coreGuardBeforeAddElement") | * [`coreInsert()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreInsert "music21.stream.core.StreamCore.coreInsert") * [`coreSelfActiveSite()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSelfActiveSite "music21.stream.core.StreamCore.coreSelfActiveSite") * [`coreSetElementOffset()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreSetElementOffset "music21.stream.core.StreamCore.coreSetElementOffset") * [`coreStoreAtEnd()`](moduleStreamCore.html#music21.stream.core.StreamCore.coreStoreAtEnd "music21.stream.core.StreamCore.coreStoreAtEnd") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") |

[`TwelveToneMatrix`](#music21.serial.TwelveToneMatrix "music21.serial.TwelveToneMatrix") instance variables

Instance variables inherited from [`Stream`](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream"):

|  |  |  |
| --- | --- | --- |
| * [`autoSort`](moduleStreamBase.html#music21.stream.base.Stream.autoSort "music21.stream.base.Stream.autoSort") * [`definesExplicitPageBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitPageBreaks "music21.stream.base.Stream.definesExplicitPageBreaks") | * [`definesExplicitSystemBreaks`](moduleStreamBase.html#music21.stream.base.Stream.definesExplicitSystemBreaks "music21.stream.base.Stream.definesExplicitSystemBreaks") * [`isFlat`](moduleStreamBase.html#music21.stream.base.Stream.isFlat "music21.stream.base.Stream.isFlat") | * [`isSorted`](moduleStreamBase.html#music21.stream.base.Stream.isSorted "music21.stream.base.Stream.isSorted") * [`recursionType`](moduleStreamBase.html#music21.stream.base.Stream.recursionType "music21.stream.base.Stream.recursionType") |

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.serial.pcToToneRow(*pcSet*)[[source]](../_modules/music21/serial.html#pcToToneRow)
:   A convenience function that, given a list of pitch classes represented as integers
    and turns it in to a [`ToneRow`](#music21.serial.ToneRow "music21.serial.ToneRow") object.

    ```python
    >>> chromaticRow = serial.pcToToneRow([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    >>> chromaticRow.show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note C#>
    {2.0} <music21.note.Note D>
    {3.0} <music21.note.Note E->
    {4.0} <music21.note.Note E>
    {5.0} <music21.note.Note F>
    {6.0} <music21.note.Note F#>
    {7.0} <music21.note.Note G>
    {8.0} <music21.note.Note G#>
    {9.0} <music21.note.Note A>
    {10.0} <music21.note.Note B->
    {11.0} <music21.note.Note B>
    >>> matrixObj = chromaticRow.matrix()
    >>> print(matrixObj)
      0  1  2  3  4  5  6  7  8  9  A  B
      B  0  1  2  3  4  5  6  7  8  9  A
    ...
    ```

    ```python
    >>> fancyRow = serial.pcToToneRow([4, 5, 0, 6, 7, 2, 'a', 8, 9, 1, 'b', 3])
    >>> matrixObj = fancyRow.matrix()
    >>> print(matrixObj)
      0  1  8  2  3  A  6  4  5  9  7  B
      B  0  7  1  2  9  5  3  4  8  6  A
    ...
    ```

    Note that the Row does not have to be a valid row to exist:

    ```python
    >>> multiSetRow = serial.pcToToneRow([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    >>> multiSetRow.pitchClasses()
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ```

    Or even have 12 notes:

    ```python
    >>> shortRow = serial.pcToToneRow([3, 4])
    >>> shortRow.pitchClasses()
    [3, 4]
    ```

    If the row does have twelve notes (whether unique or not) the object returned
    is a TwelveToneRow:

    ```python
    >>> multiSetRow
    <music21.serial.TwelveToneRow 111111111111>
    ```

    Otherwise, it is simply a ToneRow:

    ```python
    >>> shortRow
    <music21.serial.ToneRow 34>
    ```

music21.serial.rowToMatrix(*p: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[source]](../_modules/music21/serial.html#rowToMatrix)
:   Takes a list of numbers of converts it to a string representation of a
    12-tone matrix.

    ```python
    >>> aMatrix = serial.rowToMatrix([0, 2, 11, 7, 8, 3, 9, 1, 4, 10, 6, 5])
    >>> print(aMatrix)
      0  2 11  7  8  3  9  1  4 10  6  5
     10  0  9  5  6  1  7 11  2  8  4  3
      1  3  0  8  9  4 10  2  5 11  7  6
      5  7  4  0  1  8  2  6  9  3 11 10
      4  6  3 11  0  7  1  5  8  2 10  9
      9 11  8  4  5  0  6 10  1  7  3  2
      3  5  2 10 11  6  0  4  7  1  9  8
     11  1 10  6  7  2  8  0  3  9  5  4
      8 10  7  3  4 11  5  9  0  6  2  1
      2  4  1  9 10  5 11  3  6  0  8  7
      6  8  5  1  2  9  3  7 10  4  0 11
      7  9  6  2  3 10  4  8 11  5  1  0
    ```

    This function survives today (2020) because it’s been
    an example function for music21 since the very first demonstrations
    of predecessors from around 2000 onwards. Nowadays, better to create
    a TwelveToneRow() object and then get a matrix from that:

    ```python
    >>> ttr = serial.TwelveToneRow([0, 2, 11, 7, 8, 3, 9, 1, 4, 10, 6, 5])
    >>> matrix = ttr.matrix()
    >>> print(matrix)
      0  2  B  7  8  3  9  1  4  A  6  5
      A  0  9  5  6  1  7  B  2  8  4  3
      1  3  0  8  9  4  A  2  5  B  7  6
      5  7  4  0  1  8  2  6  9  3  B  A
      4  6  3  B  0  7  1  5  8  2  A  9
      9  B  8  4  5  0  6  A  1  7  3  2
      3  5  2  A  B  6  0  4  7  1  9  8
      B  1  A  6  7  2  8  0  3  9  5  4
      8  A  7  3  4  B  5  9  0  6  2  1
      2  4  1  9  A  5  B  3  6  0  8  7
      6  8  5  1  2  9  3  7  A  4  0  B
      7  9  6  2  3  A  4  8  B  5  1  0
    ```

music21.serial.getHistoricalRowByName(*rowName*)[[source]](../_modules/music21/serial.html#getHistoricalRowByName)
:   Given the name referring to a twelve-tone row used in the historical literature,
    returns a [`HistoricalTwelveToneRow`](#music21.serial.HistoricalTwelveToneRow "music21.serial.HistoricalTwelveToneRow") object with attributes
    describing the row.

    The names of the rows with stored attributes are below (each must be passed as a string,
    in single quotes).

    ```python
    >>> for r in sorted(list(serial.historicalDict)):
    ...     print(r)
    BergChamberConcerto
    BergDerWein
    BergLulu
    BergLuluActIIScene1
    BergLuluActIScene20
    BergLyricSuite
    BergLyricSuitePerm
    BergViolinConcerto
    BergWozzeckPassacaglia
    SchoenbergFragOrganSonata
    SchoenbergFragPiano
    SchoenbergFragPianoPhantasia
    SchoenbergIsraelExists
    SchoenbergJakobsleiter
    SchoenbergMosesAron
    SchoenbergOp23No5
    SchoenbergOp24Mvmt4
    SchoenbergOp24Mvmt5
    SchoenbergOp25
    SchoenbergOp26
    SchoenbergOp27No1
    SchoenbergOp27No2
    SchoenbergOp27No3
    SchoenbergOp27No4
    SchoenbergOp28No1
    SchoenbergOp28No3
    SchoenbergOp29
    SchoenbergOp30
    SchoenbergOp31
    SchoenbergOp32
    SchoenbergOp33A
    SchoenbergOp33B
    SchoenbergOp34
    SchoenbergOp35No1
    SchoenbergOp35No2
    SchoenbergOp35No3
    SchoenbergOp35No5
    SchoenbergOp36
    SchoenbergOp37
    SchoenbergOp41
    SchoenbergOp42
    SchoenbergOp44
    SchoenbergOp45
    SchoenbergOp46
    SchoenbergOp47
    SchoenbergOp48No1
    SchoenbergOp48No2
    SchoenbergOp48No3
    SchoenbergOp50A
    SchoenbergOp50B
    SchoenbergOp50C
    WebernOp17No2
    WebernOp17No3
    WebernOp18No1
    WebernOp18No2
    WebernOp18No3
    WebernOp19No1
    WebernOp19No2
    WebernOp20
    WebernOp21
    WebernOp22
    WebernOp23
    WebernOp24
    WebernOp25
    WebernOp26
    WebernOp27
    WebernOp28
    WebernOp29
    WebernOp30
    WebernOp31
    WebernOpNo17No1
    ```

    ```python
    >>> web = serial.getHistoricalRowByName('WebernOp29')
    >>> web.row
    [3, 11, 2, 1, 5, 4, 7, 6, 10, 9, 0, 8]
    >>> web.composer
    'Webern'
    >>> web.opus
    'Op. 29'
    >>> web.title
    'Cantata I'
    >>> web.isLinkChord()
    False
    ```

    NOTE: before v6, these rows had ‘Row’ in front of them,
    like ‘RowWebernOp29’ instead of ‘WebernOp29’. They can still be accessed
    by the old name.

    ```python
    >>> rowWeb = serial.getHistoricalRowByName('RowWebernOp29')
    >>> rowWeb.row == web.row
    True
    ```
