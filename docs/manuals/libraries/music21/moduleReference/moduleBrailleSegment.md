Source: https://music21.org/music21docs/moduleReference/moduleBrailleSegment.html

# music21.braille.segment

Inner classes and functions for transcribing musical segments into braille.

This module was made in consultation with the manual “Introduction to Braille
Music Transcription, Second Edition” by Mary Turner De Garmo, 2005. It is
available from the Library of Congress
[here](https://www.loc.gov/nls/services-and-resources/music-service-and-materials/),
and will henceforth be referred to as BMTM.

## Affinity

class music21.braille.segment.Affinity(*\*values*)[[source]](../_modules/music21/braille/segment.html#Affinity)

## BrailleElementGrouping

class music21.braille.segment.BrailleElementGrouping(*\*listElements*)[[source]](../_modules/music21/braille/segment.html#BrailleElementGrouping)
:   A BrailleElementGrouping mimics a list of objects which should be displayed
    without a space in braille.

    ```python
    >>> from music21.braille import segment
    >>> bg = segment.BrailleElementGrouping()
    >>> bg.append(note.Note('C4'))
    >>> bg.append(note.Note('D4'))
    >>> bg.append(note.Rest())
    >>> bg.append(note.Note('F4'))
    >>> bg
    <music21.braille.segment.BrailleElementGrouping [<music21.note.Note C>,
        <music21.note.Note D>, <music21.note.Rest quarter>, <music21.note.Note F>]>
    >>> print(bg)
    <music21.note.Note C>
    <music21.note.Note D>
    <music21.note.Rest quarter>
    <music21.note.Note F>
    ```

    These are the defaults, and they are shared across all objects.

    ```python
    >>> bg.keySignature
    <music21.key.KeySignature of no sharps or flats>
    >>> bg.timeSignature
    <music21.meter.TimeSignature 4/4>
    ```

    ```python
    >>> bg.descendingChords
    True
    ```

    ```python
    >>> bg.showClefSigns
    False
    ```

    ```python
    >>> bg.upperFirstInNoteFingering
    True
    ```

    ```python
    >>> bg.withHyphen
    False
    ```

    ```python
    >>> bg.numRepeats
    0
    ```

[`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping") methods

BrailleElementGrouping.\_\_getitem\_\_(*item*)[[source]](../_modules/music21/braille/segment.html#BrailleElementGrouping.__getitem__)

[`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping") instance variables

BrailleElementGrouping.descendingChords
:   True if a [`Chord`](moduleChord.html#music21.chord.Chord "music21.chord.Chord") should be spelled
    from highest to lowest pitch
    in braille, False if the opposite is the case.

BrailleElementGrouping.keySignature
:   The last [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature") preceding the grouping.

BrailleElementGrouping.numRepeats
:   The number of times this grouping is repeated.

BrailleElementGrouping.showClefSigns
:   If True, clef signs are shown in braille.
    Representation of music in braille is not
    dependent upon clefs and staves, so the clef signs would be displayed
    for referential or historical purposes.

BrailleElementGrouping.timeSignature
:   The last `TimeSignature` preceding the grouping.

BrailleElementGrouping.withHyphen
:   If True, this grouping will end with a music hyphen.

## BrailleGrandSegment

class music21.braille.segment.BrailleGrandSegment(*lineLength: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 40*)[[source]](../_modules/music21/braille/segment.html#BrailleGrandSegment)
:   A BrailleGrandSegment represents a pair of segments (rightSegment, leftSegment)
    representing the right and left hands of a piano staff (or other two-staff object).

    ```python
    >>> bgs = braille.segment.BrailleGrandSegment(lineLength=36)
    >>> bgs.lineLength
    36
    ```

[`BrailleGrandSegment`](#music21.braille.segment.BrailleGrandSegment "music21.braille.segment.BrailleGrandSegment") bases

* [`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment")
* [`BrailleKeyboard`](moduleBrailleText.html#music21.braille.text.BrailleKeyboard "music21.braille.text.BrailleKeyboard")
* [`BrailleText`](moduleBrailleText.html#music21.braille.text.BrailleText "music21.braille.text.BrailleText")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BrailleGrandSegment`](#music21.braille.segment.BrailleGrandSegment "music21.braille.segment.BrailleGrandSegment") read-only properties

BrailleGrandSegment.brailleText

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BrailleGrandSegment`](#music21.braille.segment.BrailleGrandSegment "music21.braille.segment.BrailleGrandSegment") read/write properties

Read/write properties inherited from [`BrailleText`](moduleBrailleText.html#music21.braille.text.BrailleText "music21.braille.text.BrailleText"):

|  |  |  |
| --- | --- | --- |
| * [`showHand`](moduleBrailleText.html#music21.braille.text.BrailleText.showHand "music21.braille.text.BrailleText.showHand") |  |  |

[`BrailleGrandSegment`](#music21.braille.segment.BrailleGrandSegment "music21.braille.segment.BrailleGrandSegment") methods

BrailleGrandSegment.extractHeading()[[source]](../_modules/music21/braille/segment.html#BrailleGrandSegment.extractHeading)
:   Finds KeySignatures, TimeSignatures, TempoText, and Metronome Marks
    within the keyPairs, and removes some from allKeyPairs.

BrailleGrandSegment.extractNoteGrouping()[[source]](../_modules/music21/braille/segment.html#BrailleGrandSegment.extractNoteGrouping)
:   Fundamentally important method that adds a noteGrouping to the braille line.

BrailleGrandSegment.transcribe()[[source]](../_modules/music21/braille/segment.html#BrailleGrandSegment.transcribe)
:   Returns the BrailleText from the combined grouping keys

BrailleGrandSegment.yieldCombinedGroupingKeys()[[source]](../_modules/music21/braille/segment.html#BrailleGrandSegment.yieldCombinedGroupingKeys)
:   yields all the keys in order as a tuple of (rightKey, leftKey) where
    two keys are grouped if they have the same segmentKey except for the hand.

    ```python
    >>> bgs = braille.segment.BrailleGrandSegment()
    >>> SegmentKey = braille.segment.SegmentKey  # namedtuple
    >>> bgs[SegmentKey(1, 1, 1, 'right')] = '1r'
    >>> bgs[SegmentKey(1, 1, 1, 'left')]  = '1l'
    >>> bgs[SegmentKey(1, 2, 3, 'right')] = '2r'
    >>> bgs[SegmentKey(1, 2, 4, 'left')] = '3l'
    >>> bgs[SegmentKey(2, 1, 9, 'left')] = '4l'
    >>> bgs[SegmentKey(2, 1, 9, 'right')] = '4r'
    >>> bgs[SegmentKey(3, 1, 9, 'right')] = '5r'
    >>> for l, r in bgs.yieldCombinedGroupingKeys():
    ...     (bgs[l], bgs[r])
    ('1r', '1l')
    ('2r', <music21.braille.segment.BrailleElementGrouping []>)
    (<music21.braille.segment.BrailleElementGrouping []>, '3l')
    ('4r', '4l')
    ('5r', <music21.braille.segment.BrailleElementGrouping []>)
    ```

    Known Bug:
    :   Because this puts None elements into the defaultDict,
        it makes the assumption that all of .keys() will be SegmentKeys
        incorrect. In fact, if you run this method twice, the second time
        it will crash.

Methods inherited from [`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.braille.segment.BrailleSegment.__getitem__ "music21.braille.segment.BrailleSegment.__getitem__") * [`addDummyRests()`](#music21.braille.segment.BrailleSegment.addDummyRests "music21.braille.segment.BrailleSegment.addDummyRests") * [`addGroupingAttributes()`](#music21.braille.segment.BrailleSegment.addGroupingAttributes "music21.braille.segment.BrailleSegment.addGroupingAttributes") * [`addRepeatSymbols()`](#music21.braille.segment.BrailleSegment.addRepeatSymbols "music21.braille.segment.BrailleSegment.addRepeatSymbols") * [`consolidate()`](#music21.braille.segment.BrailleSegment.consolidate "music21.braille.segment.BrailleSegment.consolidate") | * [`extractInaccordGrouping()`](#music21.braille.segment.BrailleSegment.extractInaccordGrouping "music21.braille.segment.BrailleSegment.extractInaccordGrouping") * [`extractLongExpressionGrouping()`](#music21.braille.segment.BrailleSegment.extractLongExpressionGrouping "music21.braille.segment.BrailleSegment.extractLongExpressionGrouping") * [`extractMeasureNumber()`](#music21.braille.segment.BrailleSegment.extractMeasureNumber "music21.braille.segment.BrailleSegment.extractMeasureNumber") * [`extractSignatureGrouping()`](#music21.braille.segment.BrailleSegment.extractSignatureGrouping "music21.braille.segment.BrailleSegment.extractSignatureGrouping") * [`extractTempoTextGrouping()`](#music21.braille.segment.BrailleSegment.extractTempoTextGrouping "music21.braille.segment.BrailleSegment.extractTempoTextGrouping") | * [`fixArticulations()`](#music21.braille.segment.BrailleSegment.fixArticulations "music21.braille.segment.BrailleSegment.fixArticulations") * [`needsSplitToFit()`](#music21.braille.segment.BrailleSegment.needsSplitToFit "music21.braille.segment.BrailleSegment.needsSplitToFit") * [`showLeadingOctaveFromNoteGrouping()`](#music21.braille.segment.BrailleSegment.showLeadingOctaveFromNoteGrouping "music21.braille.segment.BrailleSegment.showLeadingOctaveFromNoteGrouping") * [`splitNoteGroupingAndTranscribe()`](#music21.braille.segment.BrailleSegment.splitNoteGroupingAndTranscribe "music21.braille.segment.BrailleSegment.splitNoteGroupingAndTranscribe") |

Methods inherited from [`BrailleKeyboard`](moduleBrailleText.html#music21.braille.text.BrailleKeyboard "music21.braille.text.BrailleKeyboard"):

|  |  |  |
| --- | --- | --- |
| * [`addNoteGroupings()`](moduleBrailleText.html#music21.braille.text.BrailleKeyboard.addNoteGroupings "music21.braille.text.BrailleKeyboard.addNoteGroupings") | * [`makeNewLines()`](moduleBrailleText.html#music21.braille.text.BrailleKeyboard.makeNewLines "music21.braille.text.BrailleKeyboard.makeNewLines") |  |

Methods inherited from [`BrailleText`](moduleBrailleText.html#music21.braille.text.BrailleText "music21.braille.text.BrailleText"):

|  |  |  |
| --- | --- | --- |
| * [`addHeading()`](moduleBrailleText.html#music21.braille.text.BrailleText.addHeading "music21.braille.text.BrailleText.addHeading") * [`addInaccord()`](moduleBrailleText.html#music21.braille.text.BrailleText.addInaccord "music21.braille.text.BrailleText.addInaccord") * [`addLongExpression()`](moduleBrailleText.html#music21.braille.text.BrailleText.addLongExpression "music21.braille.text.BrailleText.addLongExpression") * [`addMeasureNumber()`](moduleBrailleText.html#music21.braille.text.BrailleText.addMeasureNumber "music21.braille.text.BrailleText.addMeasureNumber") | * [`addSignatures()`](moduleBrailleText.html#music21.braille.text.BrailleText.addSignatures "music21.braille.text.BrailleText.addSignatures") * [`addToNewLine()`](moduleBrailleText.html#music21.braille.text.BrailleText.addToNewLine "music21.braille.text.BrailleText.addToNewLine") * [`appendOrInsertCurrent()`](moduleBrailleText.html#music21.braille.text.BrailleText.appendOrInsertCurrent "music21.braille.text.BrailleText.appendOrInsertCurrent") | * [`makeNewLine()`](moduleBrailleText.html#music21.braille.text.BrailleText.makeNewLine "music21.braille.text.BrailleText.makeNewLine") * [`optionalAddKeyboardSymbolsAndDots()`](moduleBrailleText.html#music21.braille.text.BrailleText.optionalAddKeyboardSymbolsAndDots "music21.braille.text.BrailleText.optionalAddKeyboardSymbolsAndDots") * [`recenterHeadings()`](moduleBrailleText.html#music21.braille.text.BrailleText.recenterHeadings "music21.braille.text.BrailleText.recenterHeadings") |

[`BrailleGrandSegment`](#music21.braille.segment.BrailleGrandSegment "music21.braille.segment.BrailleGrandSegment") instance variables

Instance variables inherited from [`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment"):

|  |  |  |
| --- | --- | --- |
| * [`beginsMidMeasure`](#music21.braille.segment.BrailleSegment.beginsMidMeasure "music21.braille.segment.BrailleSegment.beginsMidMeasure") * [`cancelOutgoingKeySig`](#music21.braille.segment.BrailleSegment.cancelOutgoingKeySig "music21.braille.segment.BrailleSegment.cancelOutgoingKeySig") * [`dummyRestLength`](#music21.braille.segment.BrailleSegment.dummyRestLength "music21.braille.segment.BrailleSegment.dummyRestLength") | * [`endHyphen`](#music21.braille.segment.BrailleSegment.endHyphen "music21.braille.segment.BrailleSegment.endHyphen") * [`lineLength`](#music21.braille.segment.BrailleSegment.lineLength "music21.braille.segment.BrailleSegment.lineLength") * [`showFirstMeasureNumber`](#music21.braille.segment.BrailleSegment.showFirstMeasureNumber "music21.braille.segment.BrailleSegment.showFirstMeasureNumber") | * [`showHand`](#music21.braille.segment.BrailleSegment.showHand "music21.braille.segment.BrailleSegment.showHand") * [`showHeading`](#music21.braille.segment.BrailleSegment.showHeading "music21.braille.segment.BrailleSegment.showHeading") * [`suppressOctaveMarks`](#music21.braille.segment.BrailleSegment.suppressOctaveMarks "music21.braille.segment.BrailleSegment.suppressOctaveMarks") |

## BrailleSegment

class music21.braille.segment.BrailleSegment(*lineLength: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 40*)[[source]](../_modules/music21/braille/segment.html#BrailleSegment)

[`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") bases

* [`BrailleText`](moduleBrailleText.html#music21.braille.text.BrailleText "music21.braille.text.BrailleText")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") read-only properties

BrailleSegment.brailleText
:   Returns the string from the BrailleText object

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") read/write properties

Read/write properties inherited from [`BrailleText`](moduleBrailleText.html#music21.braille.text.BrailleText "music21.braille.text.BrailleText"):

|  |  |  |
| --- | --- | --- |
| * [`showHand`](moduleBrailleText.html#music21.braille.text.BrailleText.showHand "music21.braille.text.BrailleText.showHand") |  |  |

[`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") methods

BrailleSegment.\_\_getitem\_\_(*item*)[[source]](../_modules/music21/braille/segment.html#BrailleSegment.__getitem__)

BrailleSegment.addDummyRests()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.addDummyRests)
:   Adds as many dummy rests as self.dummyRestLength to the signatures of
    brailleText

    ```python
    >>> seg = braille.segment.BrailleSegment()
    >>> seg.dummyRestLength = 4
    ```

    ```python
    >>> print(braille.lookup.rests['dummy'])
    ⠄
    >>> seg.addDummyRests()
    >>> print(seg.brailleText)
    ⠄⠄⠄⠄
    ```

BrailleSegment.addGroupingAttributes()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.addGroupingAttributes)
:   Modifies the attributes of all [`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping")
    instances in a list of [`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") instances. The
    necessary information is retrieved from the segment and from the found clef, if any.

BrailleSegment.addRepeatSymbols(*repeatTimes*)[[source]](../_modules/music21/braille/segment.html#BrailleSegment.addRepeatSymbols)
:   Adds the appropriate number of repeat symbols, following DeGarmo chapter 17.

    ```python
    >>> seg = braille.segment.BrailleSegment()
    >>> seg.addRepeatSymbols(0)
    >>> print(seg.brailleText)
    >>> seg.addRepeatSymbols(1)
    >>> print(seg.brailleText)
    ⠶
    ```

    ```python
    >>> seg = braille.segment.BrailleSegment()
    >>> seg.addRepeatSymbols(2)
    >>> print(seg.brailleText)
    ⠶⠀⠶
    ```

    ```python
    >>> seg = braille.segment.BrailleSegment()
    >>> seg.addRepeatSymbols(3)
    >>> print(seg.brailleText)
    ⠶⠼⠉
    ```

    Does not yet handle situations beginning with Example 17-6 (repeats at
    different octaves), and further

BrailleSegment.consolidate()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.consolidate)
:   Puts together certain types of elements according to the last digit of their key
    (if it is the same as Affinity.NOTEGROUP or not.

    ```python
    >>> SK = braille.segment.SegmentKey
    >>> BS1 = braille.segment.BrailleSegment()
    >>> BS1[SK(ordinal=0, affinity=2)] = ['hi', 'hello', 'there']
    >>> BS1[SK(ordinal=1, affinity=9)] = ['these', 'get']
    >>> BS1[SK(ordinal=2, affinity=9)] = ['put', 'together']
    >>> BS1[SK(ordinal=3, affinity=4)] = ['in', 'new', 'group']
    >>> BS1[SK(ordinal=4, affinity=9)] = ['with', 'the', 'previous']
    >>> BS2 = BS1.consolidate()
    >>> for (groupingKey, groupingList) in sorted(BS2.items()):
    ...     print(groupingKey, groupingList)
    SegmentKey(measure=0, ordinal=0, affinity=2, hand=None) ['hi', 'hello', 'there']
    SegmentKey(measure=0, ordinal=1, affinity=9, hand=None) these
    get
    put
    together
    SegmentKey(measure=0, ordinal=3, affinity=4, hand=None) ['in', 'new', 'group']
    SegmentKey(measure=0, ordinal=4, affinity=9, hand=None) with
    the
    previous
    ```

BrailleSegment.extractHeading()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractHeading)
:   Extract a [`KeySignature`](moduleKey.html#music21.key.KeySignature "music21.key.KeySignature"), `TempoText` and [`MetronomeMark`](moduleTempo.html#music21.tempo.MetronomeMark "music21.tempo.MetronomeMark") and
    add an appropriate braille heading to the brailleText object inputted.

BrailleSegment.extractInaccordGrouping() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractInaccordGrouping)

BrailleSegment.extractLongExpressionGrouping()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractLongExpressionGrouping)
:   Extract the Long Expression that is in the ElementGrouping in cgk
    and add it to brailleText.

BrailleSegment.extractMeasureNumber()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractMeasureNumber)
:   Adds a measure number from the segmentKey needing processing

    ```python
    >>> segKey = braille.segment.SegmentKey(measure=4, ordinal=1, affinity=9)
    >>> seg = braille.segment.BrailleSegment()
    ```

    Initialize a new Key

    ```python
    >>> type(seg[segKey])
    <class 'music21.braille.segment.BrailleElementGrouping'>
    >>> seg.extractMeasureNumber()
    >>> print(seg.brailleText)
    ⠼⠙
    ```

    Add a dot to the measure number if the segment begins mid-measure

    ```python
    >>> seg = braille.segment.BrailleSegment()
    >>> seg[segKey]
    <music21.braille.segment.BrailleElementGrouping []>
    ```

    ```python
    >>> seg.beginsMidMeasure = True
    >>> seg.extractMeasureNumber()
    >>> print(seg.brailleText)
    ⠼⠙⠄
    ```

BrailleSegment.extractNoteGrouping() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractNoteGrouping)
:   Fundamentally important method that adds a noteGrouping to the braille line.

BrailleSegment.extractSignatureGrouping()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractSignatureGrouping)
:   Extracts a key signature, time signature, and possibly an outgoing key signature
    from the currentGroupingKey and adds it to the BrailleText object.

BrailleSegment.extractTempoTextGrouping()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.extractTempoTextGrouping)
:   Extracts a tempo text and processes it.

BrailleSegment.fixArticulations()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.fixArticulations)
:   Goes through each [`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") and modifies the
    list of [`articulations`](moduleNote.html#music21.note.GeneralNote.articulations "music21.note.GeneralNote.articulations") of a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note")
    if appropriate. In particular, two rules are applied:

    * Doubling rule => If four or more of the same [`Articulation`](moduleArticulations.html#music21.articulations.Articulation "music21.articulations.Articulation")
      are found in a row, the first instance of the articulation is doubled and the rest are
      omitted.

      It is permissible (not mandatory) to observe this doubling with bowings. (BMTM, 114)
      For this reason, any [`TechnicalIndication`](moduleArticulations.html#music21.articulations.TechnicalIndication "music21.articulations.TechnicalIndication") but for bowings
      (e.g. fingering, harmonic) is skipped, because it does not braille as an articulation.
    * Staccato, Tenuto rule => “If two repeated notes appear to be tied, but either is marked
      staccato or tenuto, they are treated as slurred instead of tied.” (BMTM, 112)

BrailleSegment.needsSplitToFit(*brailleNoteGrouping*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/braille/segment.html#BrailleSegment.needsSplitToFit)
:   Returns boolean on whether a note grouping needs to be split in order to fit.

    Generally a noteGrouping will need to be split if the amount of space left
    is more than 1/4 of the line length and the brailleNoteGrouping cannot fit.

    ```python
    >>> n1 = note.Note('C1')
    >>> n2 = note.Note('D1')
    >>> n3 = note.Note('E1')
    ```

    ```python
    >>> beg1 = braille.segment.BrailleElementGrouping([n1, n2, n3])
    >>> seg = braille.segment.BrailleSegment()
    >>> seg.needsSplitToFit(beg1)
    False
    >>> seg.lineLength = 10
    >>> seg.needsSplitToFit(beg1)
    True
    ```

BrailleSegment.showLeadingOctaveFromNoteGrouping(*noteGrouping: [BrailleElementGrouping](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping")*)[[source]](../_modules/music21/braille/segment.html#BrailleSegment.showLeadingOctaveFromNoteGrouping)
:   Given a noteGrouping, should we show the octave symbol?

    ```python
    >>> n1 = note.Note('C1')
    >>> n2 = note.Note('D1')
    >>> n3 = note.Note('E1')
    ```

    ```python
    >>> beg1 = braille.segment.BrailleElementGrouping([n1, n2, n3])
    >>> bs1 = braille.segment.BrailleSegment()
    ```

    This is True because last note is None

    ```python
    >>> bs1.lastNote is None
    True
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg1)
    True
    ```

    But if we run it again, now we have a note within a fourth, so we do not
    need to show the octave:

    ```python
    >>> bs1.lastNote
    <music21.note.Note E>
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg1)
    False
    ```

    And that is true no matter how many times we call it on the same
    BrailleElementGrouping:

    ```python
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg1)
    False
    ```

    But if we give a new, much higher BrailleElementGrouping, we
    will see octave marks again.

    ```python
    >>> nHigh1 = note.Note('C6')
    >>> nHigh2 = note.Note('D6')
    >>> beg2 = braille.segment.BrailleElementGrouping([nHigh1, nHigh2])
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg2)
    True
    ```

    But if we set self.suppressOctaveMarks to True, we won’t see any
    when we switch back to beg1:

    ```python
    >>> bs1.suppressOctaveMarks = True
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg2)
    False
    ```

    We also show octaves if for some reason two noteGroups in the same measure have
    different BrailleElementGroupings keyed to consecutive ordinals. The code simulates
    that situation.

    ```python
    >>> bs1.suppressOctaveMarks = False
    >>> bs1.previousGroupingKey = braille.segment.SegmentKey(measure=3, ordinal=1,
    ...                                          affinity=braille.segment.Affinity.NOTEGROUP)
    >>> bs1.currentGroupingKey = braille.segment.SegmentKey(measure=3, ordinal=2,
    ...                                          affinity=braille.segment.Affinity.NOTEGROUP)
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg2)
    True
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg1)
    True
    >>> bs1.showLeadingOctaveFromNoteGrouping(beg1)
    True
    ```

BrailleSegment.splitNoteGroupingAndTranscribe(*noteGrouping*, *showLeadingOctaveOnFirst=False*, *addSpaceToFirst=False*)[[source]](../_modules/music21/braille/segment.html#BrailleSegment.splitNoteGroupingAndTranscribe)
:   Take a noteGrouping and split it at a logical place,
    returning braille transcriptions of each section.

BrailleSegment.transcribe()[[source]](../_modules/music21/braille/segment.html#BrailleSegment.transcribe)
:   Transcribes all noteGroupings in this dict by:

    * First transcribes the Heading (if applicable)
    * then the Measure Number
    * then adds appropriate numbers of dummyRests
    * then adds the Rest of the Note Groupings

    Returns brailleText

Methods inherited from [`BrailleText`](moduleBrailleText.html#music21.braille.text.BrailleText "music21.braille.text.BrailleText"):

|  |  |  |
| --- | --- | --- |
| * [`addHeading()`](moduleBrailleText.html#music21.braille.text.BrailleText.addHeading "music21.braille.text.BrailleText.addHeading") * [`addInaccord()`](moduleBrailleText.html#music21.braille.text.BrailleText.addInaccord "music21.braille.text.BrailleText.addInaccord") * [`addLongExpression()`](moduleBrailleText.html#music21.braille.text.BrailleText.addLongExpression "music21.braille.text.BrailleText.addLongExpression") * [`addMeasureNumber()`](moduleBrailleText.html#music21.braille.text.BrailleText.addMeasureNumber "music21.braille.text.BrailleText.addMeasureNumber") | * [`addSignatures()`](moduleBrailleText.html#music21.braille.text.BrailleText.addSignatures "music21.braille.text.BrailleText.addSignatures") * [`addToNewLine()`](moduleBrailleText.html#music21.braille.text.BrailleText.addToNewLine "music21.braille.text.BrailleText.addToNewLine") * [`appendOrInsertCurrent()`](moduleBrailleText.html#music21.braille.text.BrailleText.appendOrInsertCurrent "music21.braille.text.BrailleText.appendOrInsertCurrent") | * [`makeNewLine()`](moduleBrailleText.html#music21.braille.text.BrailleText.makeNewLine "music21.braille.text.BrailleText.makeNewLine") * [`optionalAddKeyboardSymbolsAndDots()`](moduleBrailleText.html#music21.braille.text.BrailleText.optionalAddKeyboardSymbolsAndDots "music21.braille.text.BrailleText.optionalAddKeyboardSymbolsAndDots") * [`recenterHeadings()`](moduleBrailleText.html#music21.braille.text.BrailleText.recenterHeadings "music21.braille.text.BrailleText.recenterHeadings") |

[`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment") instance variables

BrailleSegment.beginsMidMeasure
:   If True, then the initial measure number of this
    segment should be followed by a dot. This segment
    is starting in the middle of a measure.

BrailleSegment.cancelOutgoingKeySig
:   If True, the previous key signature should be
    cancelled immediately before a new key signature is encountered.

BrailleSegment.dummyRestLength
:   For a given positive integer n, adds n “dummy rests”
    near the beginning of a segment. Designed for test purposes, as they
    are used to demonstrate measure division at the end of braille lines.

BrailleSegment.endHyphen
:   If True, then the last
    [`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping") of this
    segment will be followed by a music hyphen.
    The last grouping is incomplete, because a segment
    break occurred in the middle of a measure.

BrailleSegment.lineLength
:   The maximum amount of braille characters that should be
    present in a line. The standard is 40 characters.

BrailleSegment.showFirstMeasureNumber
:   If True, then a measure number is shown
    following the heading (if applicable) and preceding the music.

BrailleSegment.showHand
:   If set to “right” or “left”, shows the corresponding
    hand sign at the beginning of the first line.

BrailleSegment.showHeading
:   If True, then a braille heading is displayed.
    See [`transcribeHeading()`](moduleBrailleBasic.html#music21.braille.basic.transcribeHeading "music21.braille.basic.transcribeHeading")
    for more details on headings.

BrailleSegment.suppressOctaveMarks
:   If True, then all octave marks are suppressed.
    Designed for test purposes, as octave marks were not presented
    until Chapter 7 of BMTM.

## GroupingGlobals

class music21.braille.segment.GroupingGlobals[[source]](../_modules/music21/braille/segment.html#GroupingGlobals)

## SegmentKey

class music21.braille.segment.SegmentKey(*measure*, *ordinal*, *affinity*, *hand*)[[source]](../_modules/music21/braille/segment.html#SegmentKey)

## Functions

music21.braille.segment.areGroupingsIdentical(*noteGroupingA*, *noteGroupingB*)[[source]](../_modules/music21/braille/segment.html#areGroupingsIdentical)
:   Takes in two note groupings, noteGroupingA and noteGroupingB. Returns True
    if both groupings have identical contents. False otherwise.

    Helper for numRepeats.

    Needs two identical length groupings.

    ```python
    >>> a = [note.Note('C4'), note.Note('D4')]
    >>> b = [note.Note('C4'), note.Note('D4')]
    >>> braille.segment.areGroupingsIdentical(a, b)
    True
    ```

    ```python
    >>> d = b.pop()
    >>> braille.segment.areGroupingsIdentical(a, b)
    False
    >>> c = [note.Rest(), note.Note('D4')]
    >>> braille.segment.areGroupingsIdentical(a, c)
    False
    ```

music21.braille.segment.extractBrailleElements(*music21MeasureOrVoice: [Measure](moduleStreamBase.html#music21.stream.base.Measure "music21.stream.base.Measure") | [Voice](moduleStreamBase.html#music21.stream.base.Voice "music21.stream.base.Voice")*) → [BrailleElementGrouping](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping")[[source]](../_modules/music21/braille/segment.html#extractBrailleElements)
:   Takes in a `Measure` or `Voice`
    and returns a [`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping") of correctly ordered
    [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") instances which can be directly transcribed to
    braille.

    ```python
    >>> from music21.braille import segment
    >>> tn = converter.parse('tinynotation: 2/4 c16 c c c d d d d', makeNotation=False)
    >>> tn = tn.makeNotation(cautionaryNotImmediateRepeat=False)
    >>> measure = tn[0]
    >>> measure.append(spanner.Slur(measure.notes[0],measure.notes[-1]))
    >>> measure.show('text')
    {0.0} <music21.clef.TrebleClef>
    {0.0} <music21.meter.TimeSignature 2/4>
    {0.0} <music21.note.Note C>
    {0.25} <music21.note.Note C>
    {0.5} <music21.note.Note C>
    {0.75} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    {1.25} <music21.note.Note D>
    {1.5} <music21.note.Note D>
    {1.75} <music21.note.Note D>
    {2.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    {2.0} <music21.bar.Barline type=final>
    ```

    Spanners are dealt with in [`prepareSlurredNotes()`](#music21.braille.segment.prepareSlurredNotes "music21.braille.segment.prepareSlurredNotes"),
    so they are not returned by this function, as seen below.

    ```python
    >>> print(segment.extractBrailleElements(measure))
    <music21.meter.TimeSignature 2/4>
    <music21.clef.TrebleClef>
    <music21.note.Note C>
    <music21.note.Note C>
    <music21.note.Note C>
    <music21.note.Note C>
    <music21.note.Note D>
    <music21.note.Note D>
    <music21.note.Note D>
    <music21.note.Note D>
    <music21.bar.Barline type=final>
    ```

music21.braille.segment.findSegments(*music21Part*, *\**, *setHand=None*, *cancelOutgoingKeySig=True*, *descendingChords=None*, *dummyRestLength=None*, *maxLineLength=40*, *segmentBreaks=None*, *showClefSigns=False*, *showFirstMeasureNumber=True*, *showHand=None*, *showHeading=True*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *showShortSlursAndTiesTogether=False*, *slurLongPhraseWithBrackets=True*, *suppressOctaveMarks=False*, *upperFirstInNoteFingering=True*)[[source]](../_modules/music21/braille/segment.html#findSegments)
:   Takes in a `Part`.

    Returns a list of `BrailleSegment` instances.

    Five functions or methods get called in the generation of segments:

    * [`prepareSlurredNotes()`](#music21.braille.segment.prepareSlurredNotes "music21.braille.segment.prepareSlurredNotes")
    * [`getRawSegments()`](#music21.braille.segment.getRawSegments "music21.braille.segment.getRawSegments")
    * [`addGroupingAttributes()`](#music21.braille.segment.BrailleSegment.addGroupingAttributes "music21.braille.segment.BrailleSegment.addGroupingAttributes")
    * `addSegmentAttributes()`
    * [`fixArticulations()`](#music21.braille.segment.BrailleSegment.fixArticulations "music21.braille.segment.BrailleSegment.fixArticulations")

    ```python
    >>> from music21.braille import test
    >>> example = test.example11_2()
    >>> allSegments = braille.segment.findSegments(example)
    ```

    ```python
    >>> print(str(allSegments[0]))
    ---begin segment---
    <music21.braille.segment BrailleSegment>
    Measure 0, Signature Grouping 1:
    <music21.key.KeySignature of 3 flats>
    <music21.meter.TimeSignature 4/4>
    ===
    Measure 0, Note Grouping 1:
    <music21.clef.TrebleClef>
    <music21.note.Note B->
    ===
    Measure 1, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note E->
    <music21.note.Note D>
    <music21.note.Note E->
    ===
    Measure 2, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note F>
    <music21.note.Note E->
    ===
    Measure 3, Note Grouping 1:
    <music21.note.Note A->
    <music21.note.Note G>
    <music21.note.Note C>
    <music21.note.Note C>
    ===
    Measure 4, Note Grouping 1:
    <music21.note.Note B->
    <music21.note.Note B->
    ===
    Measure 5, Note Grouping 1:
    <music21.note.Note E->
    <music21.note.Note B->
    <music21.note.Note A->
    <music21.note.Note G>
    ===
    Measure 6, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note F>
    <music21.note.Note C>
    ===
    Measure 7, Note Grouping 1:
    <music21.note.Note C>
    <music21.note.Note F>
    <music21.note.Note A->
    <music21.note.Note D>
    ===
    Measure 8, Note Grouping 1:
    <music21.note.Note E->
    music hyphen ⠐
    ===
    ---end segment---
    ```

    Second segment

    ```python
    >>> print(str(allSegments[1]))
    ---begin segment---
    <music21.braille.segment BrailleSegment>
    Measure 8, Note Grouping 2:
    <music21.note.Note G>
    ===
    Measure 9, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note F>
    <music21.note.Note F>
    <music21.note.Note F>
    ===
    Measure 10, Note Grouping 1:
    <music21.note.Note A->
    <music21.note.Note G>
    <music21.note.Note B->
    ===
    Measure 11, Note Grouping 1:
    <music21.note.Note B->
    <music21.note.Note A>
    <music21.note.Note A>
    <music21.note.Note C>
    ===
    Measure 12, Note Grouping 1:
    <music21.note.Note B->
    <music21.note.Note B->
    ===
    Measure 13, Note Grouping 1:
    <music21.note.Note E->
    <music21.note.Note B->
    <music21.note.Note A->
    <music21.note.Note G>
    ===
    Measure 14, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note F>
    <music21.note.Note C>
    ===
    Measure 15, Note Grouping 1:
    <music21.note.Note C>
    <music21.note.Rest quarter>
    <music21.note.Note F>
    <music21.note.Rest quarter>
    ===
    Measure 16, Note Grouping 1:
    <music21.note.Note A->
    <music21.note.Note D>
    ===
    Measure 17, Note Grouping 1:
    <music21.note.Note E->
    <music21.bar.Barline type=final>
    ===
    ---end segment---
    ```

music21.braille.segment.getRawSegments(*music21Part*, *\**, *setHand=None*, *maxLineLength: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 40*)[[source]](../_modules/music21/braille/segment.html#getRawSegments)
:   Takes in a `Part`, divides it up into segments (i.e. instances of
    [`BrailleSegment`](#music21.braille.segment.BrailleSegment "music21.braille.segment.BrailleSegment")). This function assumes
    that the Part is already divided up into measures
    (see `Measure`). An acceptable input is shown below.

    This will automatically find appropriate segment breaks at
    [`BrailleSegmentDivision`](moduleBrailleObjects.html#music21.braille.objects.BrailleSegmentDivision "music21.braille.objects.BrailleSegmentDivision")
    or [`BrailleOptionalSegmentDivision`](moduleBrailleObjects.html#music21.braille.objects.BrailleOptionalSegmentDivision "music21.braille.objects.BrailleOptionalSegmentDivision")
    or after 48 elements if a double bar or repeat sign is encountered.

    Two functions are called for each measure during the creation of segments:

    * [`prepareBeamedNotes()`](#music21.braille.segment.prepareBeamedNotes "music21.braille.segment.prepareBeamedNotes")
    * [`extractBrailleElements()`](#music21.braille.segment.extractBrailleElements "music21.braille.segment.extractBrailleElements")

    ```python
    >>> tn = converter.parse("tinynotation: 3/4 c4 c c e e e g g g c'2.")
    >>> tn = tn.makeNotation(cautionaryNotImmediateRepeat=False)
    >>> tn.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note C>
        {2.0} <music21.note.Note C>
    {3.0} <music21.stream.Measure 2 offset=3.0>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note E>
    {6.0} <music21.stream.Measure 3 offset=6.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note G>
        {2.0} <music21.note.Note G>
    {9.0} <music21.stream.Measure 4 offset=9.0>
        {0.0} <music21.note.Note C>
        {3.0} <music21.bar.Barline type=final>
    ```

    By default, there is no break anywhere within the Part,
    and a segmentList of size 1 is returned.

    ```python
    >>> import copy
    >>> from music21.braille import segment
    >>> tnA = copy.deepcopy(tn)
    >>> rawSegments = segment.getRawSegments(tnA)
    >>> len(rawSegments)
    1
    >>> rawSegments[0]
    <music21.braille.segment.BrailleSegment 1 line, 0 headings, 40 cols>
    ```

    ```python
    >>> print(rawSegments[0])
    ---begin segment---
    <music21.braille.segment BrailleSegment>
    Measure 1, Signature Grouping 1:
    <music21.meter.TimeSignature 3/4>
    ===
    Measure 1, Note Grouping 1:
    <music21.clef.TrebleClef>
    <music21.note.Note C>
    <music21.note.Note C>
    <music21.note.Note C>
    ===
    Measure 2, Note Grouping 1:
    <music21.note.Note E>
    <music21.note.Note E>
    <music21.note.Note E>
    ===
    Measure 3, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note G>
    <music21.note.Note G>
    ===
    Measure 4, Note Grouping 1:
    <music21.note.Note C>
    <music21.bar.Barline type=final>
    ===
    ---end segment---
    ```

    Now, a segment break occurs at measure 2, offset 1.0 within that measure.
    The two segments are shown below.

    ```python
    >>> tnB = copy.deepcopy(tn)
    >>> tnB.measure(2).insert(1.0, braille.objects.BrailleSegmentDivision())
    >>> allSegments = segment.getRawSegments(tnB)
    >>> len(allSegments)
    2
    ```

    ```python
    >>> allSegments[0]
    <music21.braille.segment.BrailleSegment 1 line, 0 headings, 40 cols>
    ```

    ```python
    >>> print(allSegments[0])
    ---begin segment---
    <music21.braille.segment BrailleSegment>
    Measure 1, Signature Grouping 1:
    <music21.meter.TimeSignature 3/4>
    ===
    Measure 1, Note Grouping 1:
    <music21.clef.TrebleClef>
    <music21.note.Note C>
    <music21.note.Note C>
    <music21.note.Note C>
    ===
    Measure 2, Note Grouping 1:
    <music21.note.Note E>
    ===
    ---end segment---
    ```

    ```python
    >>> allSegments[1]
    <music21.braille.segment.BrailleSegment 1 line, 0 headings, 40 cols>
    ```

    ```python
    >>> print(allSegments[1])
    ---begin segment---
    <music21.braille.segment BrailleSegment>
    Measure 2, Note Grouping 2:
    <music21.note.Note E>
    <music21.note.Note E>
    ===
    Measure 3, Note Grouping 1:
    <music21.note.Note G>
    <music21.note.Note G>
    <music21.note.Note G>
    ===
    Measure 4, Note Grouping 1:
    <music21.note.Note C>
    <music21.bar.Barline type=final>
    ===
    ---end segment---
    ```

    If we insert an optional division, the division
    only appears if there are 48 elements in the current segment:

    ```python
    >>> tnC = copy.deepcopy(tn)
    >>> tnC.measure(1).insert(1.0, braille.objects.BrailleOptionalSegmentDivision())
    >>> allSegments = segment.getRawSegments(tnC)
    >>> len(allSegments)
    1
    ```

    If by happenstance a segment division object is encountered where a division
    has just been created (or the very beginning),
    no unnecessary empty segment will be created:

    ```python
    >>> tnD = copy.deepcopy(tn)
    >>> tnD.measure(1).insert(0, braille.objects.BrailleSegmentDivision())
    >>> allSegments = segment.getRawSegments(tnD)
    >>> len(allSegments)
    1
    ```

music21.braille.segment.prepareBeamedNotes(*music21Measure*)[[source]](../_modules/music21/braille/segment.html#prepareBeamedNotes)
:   Takes in a `Measure` and labels beamed notes
    of smaller value than an 8th with beamStart and beamContinue keywords
    in accordance with beaming rules in braille music.

    A more in-depth explanation of beaming in braille can be found in
    Chapter 15 of Introduction to Braille Music Transcription, Second
    Edition, by Mary Turner De Garmo.

    ```python
    >>> from music21.braille import segment
    >>> tn = converter.parse('tinynotation: 2/4 c16 c c c d d d d')
    >>> tn = tn.makeNotation(cautionaryNotImmediateRepeat=False)
    >>> tn.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 2/4>
        {0.0} <music21.note.Note C>
        {0.25} <music21.note.Note C>
        {0.5} <music21.note.Note C>
        {0.75} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {1.25} <music21.note.Note D>
        {1.5} <music21.note.Note D>
        {1.75} <music21.note.Note D>
        {2.0} <music21.bar.Barline type=final>
    >>> measure = tn[0]
    >>> segment.prepareBeamedNotes(measure)
    >>> measure.notes[0].beamStart
    True
    >>> measure.notes[1].beamContinue
    True
    >>> measure.notes[2].beamContinue
    True
    >>> measure.notes[3].beamContinue
    True
    ```

music21.braille.segment.prepareSlurredNotes(*music21Part*, *\**, *slurLongPhraseWithBrackets=True*, *showShortSlursAndTiesTogether=False*, *showLongSlursAndTiesTogether: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/braille/segment.html#prepareSlurredNotes)
:   Takes in a `Part` and three keywords:

    * slurLongPhraseWithBrackets
    * showShortSlursAndTiesTogether
    * showLongSlursAndTiesTogether

    For any slurs present in the Part, the appropriate notes are labeled
    with attributes indicating where to put the symbols that represent
    slurring in braille. For purposes of slurring in braille, there is
    a distinction between short and long phrases. In a short phrase, a
    slur covers up to four notes. A short slur symbol should follow each
    note except the last.

    ```python
    >>> import copy
    >>> from music21.braille import segment
    >>> short = converter.parse('tinynotation: 3/4 c4 d e')
    >>> s1 = spanner.Slur(short.recurse().notes.first(), short.recurse().notes.last())
    >>> short.append(s1)
    >>> short.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.bar.Barline type=final>
    {3.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note E>>
    >>> shortA = copy.deepcopy(short)
    >>> segment.prepareSlurredNotes(shortA)
    >>> shortA.recurse().notes[0].shortSlur
    True
    >>> shortA.recurse().notes[1].shortSlur
    True
    ```

    In a long phrase, a slur covers more than four notes. There are two
    options for slurring long phrases. The first is by using the bracket
    slur. By default, slurLongPhraseWithBrackets is True. The opening
    bracket sign is put before the first note, and the closing bracket
    sign is put before the last note.

    ```python
    >>> long = converter.parse('tinynotation: 3/4 c8 d e f g a')
    >>> s2 = spanner.Slur(long[note.Note].first(), long[note.Note].last())
    >>> long.append(s2)
    >>> long.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 3/4>
        {0.0} <music21.note.Note C>
        {0.5} <music21.note.Note D>
        {1.0} <music21.note.Note E>
        {1.5} <music21.note.Note F>
        {2.0} <music21.note.Note G>
        {2.5} <music21.note.Note A>
        {3.0} <music21.bar.Barline type=final>
    {3.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note A>>
    >>> longA = copy.deepcopy(long)
    >>> segment.prepareSlurredNotes(longA)
    >>> longA[note.Note].first().beginLongBracketSlur
    True
    >>> longA[note.Note].last().endLongBracketSlur
    True
    ```

    The other way is by using the double slur, setting slurLongPhraseWithBrackets
    to False. The opening sign of the double slur is put after the first note
    (i.e. before the second note) and the closing sign is put before the last
    note (i.e. before the second to last note).

    If a value is not supplied for showLongSlursAndTiesTogether, it will take the
    value set for slurLongPhraseWithBrackets, which defaults True.

    ```python
    >>> longB = copy.deepcopy(long)
    >>> segment.prepareSlurredNotes(longB, slurLongPhraseWithBrackets=False)
    >>> longB.recurse().notes[1].beginLongDoubleSlur
    True
    >>> longB.recurse().notes[-2].endLongDoubleSlur
    True
    ```

    In the event that slurs and ties are shown together in print, the slur is
    redundant. Examples are shown for slurring a short phrase; the process is
    identical for slurring a long phrase.

    Below, a tie has been added between the first two notes of the short phrase
    defined above. If showShortSlursAndTiesTogether is set to its default value of
    False, then the slur on either side of the phrase is reduced by the amount that
    ties are present, as shown below.

    ```python
    >>> short.recurse().notes[0].tie = tie.Tie('start')
    >>> shortB = copy.deepcopy(short)
    >>> segment.prepareSlurredNotes(shortB)
    >>> shortB.recurse().notes[0].shortSlur
    Traceback (most recent call last):
    AttributeError: 'Note' object has no attribute 'shortSlur'
    >>> shortB.recurse().notes[0].tie
    <music21.tie.Tie start>
    >>> shortB.recurse().notes[1].shortSlur
    True
    ```

    If showShortSlursAndTiesTogether is set to True, then the slurs and ties are
    shown together (i.e. the note has both a shortSlur and a tie).

    ```python
    >>> shortC = copy.deepcopy(short)
    >>> segment.prepareSlurredNotes(shortC, showShortSlursAndTiesTogether=True)
    >>> shortC.recurse().notes[0].shortSlur
    True
    >>> shortC.recurse().notes[0].tie
    <music21.tie.Tie start>
    ```

    TODO: This should not add attributes to Note objects but instead return a collection
    of sets of notes that have each element applied to it.

music21.braille.segment.setAffinityCode(*music21Object: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/braille/segment.html#setAffinityCode)
:   Takes in a [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"), and does two things:

    * Modifies the [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") attribute of the
      object to fit the slightly modified ordering of objects in braille music.
    * Adds an affinity code to the Editorial for the object.
      This code indicates which surrounding objects the object should be grouped with.

    A BrailleSegmentException is raised if an affinity code cannot be assigned to
    the object.

    As seen in the following example, the affinity code of a [`Note`](moduleNote.html#music21.note.Note "music21.note.Note")
    and a [`TrebleClef`](moduleClef.html#music21.clef.TrebleClef "music21.clef.TrebleClef") are the same, because they should be grouped
    together. However, the classSortOrder indicates that the TrebleClef should come first
    in the braille.

    ```python
    >>> n1 = note.Note('D5')
    >>> braille.segment.setAffinityCode(n1)
    >>> n1.editorial.affinityCode
    <Affinity.NOTEGROUP: 9>
    >>> n1.classSortOrder
    10
    >>> c1 = clef.TrebleClef()
    >>> braille.segment.setAffinityCode(c1)
    >>> c1.editorial.affinityCode
    <Affinity.NOTEGROUP: 9>
    >>> c1.classSortOrder
    7
    ```

music21.braille.segment.setGroupingGlobals()[[source]](../_modules/music21/braille/segment.html#setGroupingGlobals)
:   sets defaults for grouping globals. Called first time anything
    in Braille is run, but saves creating two expensive objects if never run

music21.braille.segment.splitMeasure(*music21Measure*, *beatDivisionOffset=0*, *useTimeSignature=None*)[[source]](../_modules/music21/braille/segment.html#splitMeasure)
:   Takes a `Measure`, divides it in two parts, and returns a
    two-tuple of (leftMeasure, rightMeasure). The parameters are as
    follows:

    * beatDivisionOffset => Adjusts the end offset of the first partition by a certain amount
      of beats to the left.
    * useTimeSignature => In the event that the Measure comes from the middle of a Part
      and thus does not define an explicit `TimeSignature`. If not
      provided, a TimeSignature is retrieved by
      using `bestTimeSignature()`.

    ```python
    >>> m = stream.Measure()
    >>> m.append(note.Note('C4'))
    >>> m.append(note.Note('D4'))
    >>> left, right = braille.segment.splitMeasure(m)
    >>> left.show('text')
    {0.0} <music21.note.Note C>
    >>> right.show('text')
    {1.0} <music21.note.Note D>
    ```

music21.braille.segment.splitNoteGrouping(*noteGrouping*, *beatDivisionOffset=0*)[[source]](../_modules/music21/braille/segment.html#splitNoteGrouping)
:   Almost identical to [`splitMeasure()`](#music21.braille.segment.splitMeasure "music21.braille.segment.splitMeasure"), but
    functions on a [`BrailleElementGrouping`](#music21.braille.segment.BrailleElementGrouping "music21.braille.segment.BrailleElementGrouping")
    instead.

    ```python
    >>> from music21.braille import segment
    >>> bg = segment.BrailleElementGrouping()
    >>> bg.timeSignature = meter.TimeSignature('2/2')
    >>> s = converter.parse('tinyNotation: 2/2 c4 d r e')
    >>> for n in s.recurse().notesAndRests:
    ...     bg.append(n)
    >>> left, right = segment.splitNoteGrouping(bg)
    >>> left
    <music21.braille.segment.BrailleElementGrouping
        [<music21.note.Note C>, <music21.note.Note D>]>
    ```

    ```python
    >>> print(left)
    <music21.note.Note C>
    <music21.note.Note D>
    ```

    ```python
    >>> right
    <music21.braille.segment.BrailleElementGrouping
        [<music21.note.Rest quarter>, <music21.note.Note E>]>
    ```

    Now split one beat division earlier than it should be. For 2/2 that means
    one half of a beat, or one quarter note earlier:

    ```python
    >>> left, right = segment.splitNoteGrouping(bg, beatDivisionOffset=1)
    >>> left
    <music21.braille.segment.BrailleElementGrouping
        [<music21.note.Note C>]>
    >>> right
    <music21.braille.segment.BrailleElementGrouping
        [<music21.note.Note D>, <music21.note.Rest quarter>, <music21.note.Note E>]>
    ```
