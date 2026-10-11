Source: https://music21.org/music21docs/moduleReference/moduleTreeSpans.html

# music21.tree.spans

Tools for grouping notes and chords into a searchable tree
organized by start and stop offsets.

## ElementTimespan

class music21.tree.spans.ElementTimespan(*element: [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parentOffset: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parentEndTime: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *parentage: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[stream.Stream, ...] = ()*, *offset: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *endTime: OffsetQLIn | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/tree/spans.html#ElementTimespan)
:   A span of time anchored to an element in a score. The span of time may
    be the same length as the element in the score. It may be shorter (a
    “slice” of an element) or it may be longer (in the case of a timespan
    that is anchored to a single element but extends over rests or other
    notes following a note)

    PitchedTimespans give information about an element (such as a Note). It knows
    its absolute position with respect to the element passed into TimespanTree.
    It contains information about what measure it’s in, what part it’s in, etc.

    Example, getting a passing tone from a known location from a Bach chorale.

    First we create an Offset tree:

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> scoreTree
    <TimespanTree {199} (0.0 to 36.0) <music21.stream.Score ...>>
    ```

    Then get the verticality from offset 6.5, which is beat two-and-a-half of
    measure 2 (the piece is in 4/4 with a quarter-note pickup)

    ```python
    >>> verticality = scoreTree.getVerticalityAt(6.5)
    >>> verticality
    <music21.tree.verticality.Verticality 6.5 {E3 D4 G#4 B4}>
    ```

    There are four PitchedTimespans in the verticality – each representing
    a note. The notes are arranged from lowest to highest.

    We can find all the PitchedTimespans that start exactly at 6.5. There’s
    one.

    ```python
    >>> verticality.startTimespans
    (<PitchedTimespan (6.5 to 7.0) <music21.note.Note D>>,)
    ```

    ```python
    >>> pitchedTimespan = verticality.startTimespans[0]
    >>> pitchedTimespan
    <PitchedTimespan (6.5 to 7.0) <music21.note.Note D>>
    ```

    What can we do with a PitchedTimespan? We can get its Part object and from there the
    Part object name

    ```python
    >>> pitchedTimespan.part
    <music21.stream.Part Tenor>
    >>> pitchedTimespan.part.partName
    'Tenor'
    ```

    Find out what measure it’s in:

    ```python
    >>> pitchedTimespan.measureNumber
    2
    >>> pitchedTimespan.parentOffset
    5.0
    ```

    The position in the measure is given by subtracting that from the
    .offset:

    ```python
    >>> pitchedTimespan.offset - pitchedTimespan.parentOffset
    1.5
    ```

    ```python
    >>> pitchedTimespan.element
    <music21.note.Note D>
    ```

    These are not dynamic, so changing the Score object does not change the
    measureNumber, etc.

[`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan") bases

* [`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan")

[`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan") read-only properties

ElementTimespan.measureNumber
:   The measure number of the measure containing the element.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> pitchedTimespan = verticality.startTimespans[0]
    >>> pitchedTimespan.measureNumber
    1
    ```

ElementTimespan.part
:   find the object in the parentage that is a Part object:

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> pitchedTimespan = verticality.startTimespans[2]
    >>> pitchedTimespan
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note C#>>
    >>> pitchedTimespan.part
    <music21.stream.Part Tenor>
    ```

ElementTimespan.quarterLength
:   The quarterLength of the Timespan, which, due to manipulation, may be different
    from that of the element.

    ```python
    >>> n = note.Note('D-')
    >>> n.offset = 1.0
    >>> n.duration.quarterLength = 2.0
    ```

    ```python
    >>> pts = tree.spans.PitchedTimespan(n, offset=n.offset, endTime=3.0)
    >>> pts
    <PitchedTimespan (1.0 to 3.0) <music21.note.Note D->>
    >>> pts.quarterLength
    2.0
    >>> n.duration.quarterLength
    2.0
    ```

    ```python
    >>> pts2 = pts.new(offset=0.0)
    >>> pts2
    <PitchedTimespan (0.0 to 3.0) <music21.note.Note D->>
    >>> pts2.quarterLength
    3.0
    >>> pts2.element.duration.quarterLength
    2.0
    ```

Read-only properties inherited from [`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan"):

|  |  |  |
| --- | --- | --- |
| * [`endTime`](#music21.tree.spans.Timespan.endTime "music21.tree.spans.Timespan.endTime") | * [`offset`](#music21.tree.spans.Timespan.offset "music21.tree.spans.Timespan.offset") |  |

[`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan") methods

ElementTimespan.\_\_eq\_\_(*other*)[[source]](../_modules/music21/tree/spans.html#ElementTimespan.__eq__)
:   Return self==value.

ElementTimespan.getParentageByClass(*classList*)[[source]](../_modules/music21/tree/spans.html#ElementTimespan.getParentageByClass)
:   returns that is the first parentage that has this classList.
    default stream.Part

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> score.id = 'bach'
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> pitchedTimespan = verticality.startTimespans[2]
    >>> pitchedTimespan
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note C#>>
    >>> pitchedTimespan.getParentageByClass(classList=(stream.Part,))
    <music21.stream.Part Tenor>
    >>> pitchedTimespan.getParentageByClass(classList=(stream.Measure,))
    <music21.stream.Measure 1 offset=1.0>
    >>> pitchedTimespan.getParentageByClass(classList=(stream.Score,))
    <music21.stream.Score bach>
    ```

    The closest parent is returned in case of a multiple list:

    ```python
    >>> searchTuple = (stream.Voice, stream.Measure, stream.Part)
    >>> pitchedTimespan.getParentageByClass(classList=searchTuple)
    <music21.stream.Measure 1 offset=1.0>
    ```

    TODO: this should take a normal class list.

ElementTimespan.makeElement(*makeCopy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [base.Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/tree/spans.html#ElementTimespan.makeElement)
:   Return a copy of the element (or the same one if makeCopy is False)
    with the quarterLength set to the length of the timespan

ElementTimespan.new(*element=None*, *parentOffset=None*, *parentEndTime=None*, *offset=None*, *endTime=None*)[[source]](../_modules/music21/tree/spans.html#ElementTimespan.new)
:   Create a new object that is identical to the calling object
    but with some parameters overridden.

    ```python
    >>> n = note.Note('C#')
    >>> pts = tree.spans.PitchedTimespan(n, offset=11.0, endTime=12.0)
    >>> pts
    <PitchedTimespan (11.0 to 12.0) <music21.note.Note C#>>
    >>> pts2 = pts.new(endTime=13.0)
    >>> pts2
    <PitchedTimespan (11.0 to 13.0) <music21.note.Note C#>>
    >>> pts.element is pts2.element
    True
    ```

Methods inherited from [`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan"):

|  |  |  |
| --- | --- | --- |
| * [`canMerge()`](#music21.tree.spans.Timespan.canMerge "music21.tree.spans.Timespan.canMerge") | * [`mergeWith()`](#music21.tree.spans.Timespan.mergeWith "music21.tree.spans.Timespan.mergeWith") | * [`splitAt()`](#music21.tree.spans.Timespan.splitAt "music21.tree.spans.Timespan.splitAt") |

[`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan") instance variables

ElementTimespan.parentage
:   The Stream hierarchy above the element in a ElementTimespan.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> pitchedTimespan = verticality.startTimespans[0]
    >>> pitchedTimespan
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note A>>
    >>> for streamSite in pitchedTimespan.parentage:
    ...     streamSite
    <music21.stream.Measure 1 offset=1.0>
    <music21.stream.Part Soprano>
    <music21.stream.Score ...>
    ```

## PitchedTimespan

class music21.tree.spans.PitchedTimespan(*element=None*, *parentOffset=None*, *parentEndTime=None*, *parentage=None*, *offset=None*, *endTime=None*)[[source]](../_modules/music21/tree/spans.html#PitchedTimespan)

[`PitchedTimespan`](#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan") bases

* [`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan")
* [`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan")

[`PitchedTimespan`](#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan") read-only properties

PitchedTimespan.pitches
:   Gets the pitches of the element wrapped by this PitchedTimespan.

    ```python
    >>> c = chord.Chord('C4 E4 G4')
    >>> pts = tree.spans.PitchedTimespan(c, offset=0.0, endTime=1.0)
    >>> pts.pitches
    (<music21.pitch.Pitch C4>, <music21.pitch.Pitch E4>, <music21.pitch.Pitch G4>)
    >>> pts.pitches == c.pitches
    True
    >>> pts.pitches is c.pitches
    False
    ```

Read-only properties inherited from [`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan"):

|  |  |  |
| --- | --- | --- |
| * [`measureNumber`](#music21.tree.spans.ElementTimespan.measureNumber "music21.tree.spans.ElementTimespan.measureNumber") | * [`part`](#music21.tree.spans.ElementTimespan.part "music21.tree.spans.ElementTimespan.part") | * [`quarterLength`](#music21.tree.spans.ElementTimespan.quarterLength "music21.tree.spans.ElementTimespan.quarterLength") |

Read-only properties inherited from [`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan"):

|  |  |  |
| --- | --- | --- |
| * [`endTime`](#music21.tree.spans.Timespan.endTime "music21.tree.spans.Timespan.endTime") | * [`offset`](#music21.tree.spans.Timespan.offset "music21.tree.spans.Timespan.offset") |  |

[`PitchedTimespan`](#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan") methods

PitchedTimespan.canMerge(*other*)[[source]](../_modules/music21/tree/spans.html#PitchedTimespan.canMerge)
:   sub-method of base canMerge that checks to see if the pitches are the same.

    For quick score reductions, we can merge two consecutive
    like-pitched element timespans, keeping
    score-relevant information from the first of the two, such as its
    Music21 Element.

    This is useful when using timespans to perform score reduction.

    Let’s demonstrate merging some contiguous E’s in the alto part of a Bach
    chorale:

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> timespan_one = scoreTree[12]
    >>> print(timespan_one)
    <PitchedTimespan (2.0 to 3.0) <music21.note.Note E>>
    ```

    ```python
    >>> print(timespan_one.part)
    <music21.stream.Part Alto>
    ```

    ```python
    >>> timespan_two = scoreTree.findNextPitchedTimespanInSameStreamByClass(timespan_one)
    >>> print(timespan_two)
    <PitchedTimespan (3.0 to 4.0) <music21.note.Note E>>
    ```

    ```python
    >>> timespan_one.canMerge(timespan_two)
    (True, '')
    ```

    ```python
    >>> merged = timespan_one.mergeWith(timespan_two)
    >>> print(merged)
    <PitchedTimespan (2.0 to 4.0) <music21.note.Note E>>
    ```

    ```python
    >>> merged.part is timespan_one.part
    True
    ```

    Attempting to merge timespans which are not contiguous, or which do not
    have identical pitches will result in error:

    ```python
    >>> scoreTree[0].canMerge(scoreTree[50])
    (False, 'Cannot merge <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
         with <PitchedTimespan (9.5 to 10.0) <music21.note.Note B>>: not contiguous')
    ```

    ```python
    >>> scoreTree[0].mergeWith(scoreTree[50])
    Traceback (most recent call last):
    music21.tree.spans.TimespanException: Cannot merge
            <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
            with <PitchedTimespan (9.5 to 10.0) <music21.note.Note B>>: not contiguous
    ```

    This is probably not what you want to do: get the next element timespan in
    the same score:

    ```python
    >>> timespan_twoWrong = scoreTree.findNextPitchedTimespanInSameStreamByClass(
    ...     timespan_one, classList=(stream.Score,))
    >>> print(timespan_twoWrong)
    <PitchedTimespan (3.0 to 4.0) <music21.note.Note C#>>
    >>> print(timespan_twoWrong.part)
    <music21.stream.Part Soprano>
    ```

Methods inherited from [`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.tree.spans.ElementTimespan.__eq__ "music21.tree.spans.ElementTimespan.__eq__") * [`getParentageByClass()`](#music21.tree.spans.ElementTimespan.getParentageByClass "music21.tree.spans.ElementTimespan.getParentageByClass") | * [`makeElement()`](#music21.tree.spans.ElementTimespan.makeElement "music21.tree.spans.ElementTimespan.makeElement") | * [`new()`](#music21.tree.spans.ElementTimespan.new "music21.tree.spans.ElementTimespan.new") |

Methods inherited from [`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan"):

|  |  |  |
| --- | --- | --- |
| * [`mergeWith()`](#music21.tree.spans.Timespan.mergeWith "music21.tree.spans.Timespan.mergeWith") | * [`splitAt()`](#music21.tree.spans.Timespan.splitAt "music21.tree.spans.Timespan.splitAt") |  |

[`PitchedTimespan`](#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan") instance variables

Instance variables inherited from [`ElementTimespan`](#music21.tree.spans.ElementTimespan "music21.tree.spans.ElementTimespan"):

|  |  |  |
| --- | --- | --- |
| * [`parentage`](#music21.tree.spans.ElementTimespan.parentage "music21.tree.spans.ElementTimespan.parentage") |  |  |

## Timespan

class music21.tree.spans.Timespan(*offset=-inf*, *endTime=inf*)[[source]](../_modules/music21/tree/spans.html#Timespan)
:   A span of time, with a start offset and stop offset.

    Useful for demonstrating various properties of the timespan-collection class
    family.

    ```python
    >>> timespan = tree.spans.Timespan(-1.5, 3.25)
    >>> print(timespan)
    <Timespan -1.5 3.25>
    ```

    A timespan has two attributes, its offset and its endTime. They are immutable.

    ```python
    >>> timespan.offset
    -1.5
    >>> timespan.endTime
    3.25
    ```

    To create a changed timespan, call the .new() method on the timespan.

    ```python
    >>> ts2 = timespan.new(offset=0.0)
    >>> ts2
    <Timespan 0.0 3.25>
    ```

    ```python
    >>> ts3 = timespan.new(endTime=5.0)
    >>> ts3
    <Timespan -1.5 5.0>
    ```

    Two timespans are equal if they have the same offset and endTime

    ```python
    >>> ts4 = tree.spans.Timespan(-1.5, 5.0)
    >>> ts3 == ts4
    True
    >>> ts4 == ts2
    False
    ```

[`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan") read-only properties

Timespan.endTime
:   The stop offset of the Timespan, relative to its
    containing score.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> timespan = verticality.startTimespans[0]
    >>> timespan.endTime
    2.0
    ```

Timespan.offset
:   The start offset of the Timespan, relative to its
    containing score.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> verticality = scoreTree.getVerticalityAt(1.0)
    >>> timespan = verticality.startTimespans[0]
    >>> timespan.offset
    1.0
    ```

[`Timespan`](#music21.tree.spans.Timespan "music21.tree.spans.Timespan") methods

Timespan.\_\_eq\_\_(*expr*)[[source]](../_modules/music21/tree/spans.html#Timespan.__eq__)
:   Return self==value.

Timespan.canMerge(*other*)[[source]](../_modules/music21/tree/spans.html#Timespan.canMerge)
:   returns a tuple of (True or False) if these timespans can be merged
    with the second element being a message or None.

    ```python
    >>> ts1 = tree.spans.Timespan(0, 5)
    >>> ts2 = tree.spans.Timespan(5, 7)
    >>> ts1.canMerge(ts2)
    (True, '')
    >>> ts3 = tree.spans.Timespan(6, 10)
    >>> ts1.canMerge(ts3)
    (False, 'Cannot merge <Timespan 0.0 5.0> with <Timespan 6.0 10.0>: not contiguous')
    ```

    Overlapping Timespans cannot be merged, just contiguous ones.

    ```python
    >>> ts4 = tree.spans.Timespan(3, 4)
    >>> ts1.canMerge(ts4)
    (False, 'Cannot merge <Timespan 0.0 5.0> with <Timespan 3.0 4.0>: not contiguous')
    ```

Timespan.mergeWith(*other*)[[source]](../_modules/music21/tree/spans.html#Timespan.mergeWith)
:   Merges two consecutive/contiguous timespans, keeping the
    information from the former of the two.

    ```python
    >>> ts1 = tree.spans.Timespan(0, 5)
    >>> ts2 = tree.spans.Timespan(5, 7)
    >>> ts3 = ts1.mergeWith(ts2)
    >>> ts3
    <Timespan 0.0 7.0>
    ```

    Note that (for now), overlapping timespans cannot be merged:

    ```python
    >>> ts4 = tree.spans.Timespan(6, 10)
    >>> ts3.mergeWith(ts4)
    Traceback (most recent call last):
    music21.tree.spans.TimespanException: Cannot merge <Timespan 0.0 7.0> with
        <Timespan 6.0 10.0>: not contiguous
    ```

Timespan.new(*offset=None*, *endTime=None*)[[source]](../_modules/music21/tree/spans.html#Timespan.new)
:   return a new object with the given offset and endTime

Timespan.splitAt(*offset*)[[source]](../_modules/music21/tree/spans.html#Timespan.splitAt)
:   Split Timespan at offset.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> verticality = scoreTree.getVerticalityAt(0)
    >>> verticality
    <music21.tree.verticality.Verticality 0 {A3 E4 C#5}>
    ```

    ```python
    >>> timespan = verticality.startTimespans[0]
    >>> timespan
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
    ```

    ```python
    >>> for shard in timespan.splitAt(0.25):
    ...     shard
    ...
    <PitchedTimespan (0.0 to 0.25) <music21.note.Note C#>>
    <PitchedTimespan (0.25 to 0.5) <music21.note.Note C#>>
    ```

    ```python
    >>> timespan.splitAt(1000)
    (<PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>,)
    ```
