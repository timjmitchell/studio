Source: https://music21.org/music21docs/moduleReference/moduleTreeTimespanTree.html

# music21.tree.timespanTree

Tools for grouping elements, timespans, and especially
pitched elements into kinds of searchable tree organized by start and stop offsets
and other positions.

## TimespanTree

class music21.tree.timespanTree.TimespanTree(*elements=None*, *source=None*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree)
:   A TimespanTree is a data structure for efficiently slicing a score for pitches, or,
    like all [`OffsetTree`](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") objects, for searching large scores
    quickly by time.

    While you can construct an TimespanTree by hand, inserting timespans one at
    a time, the common use-case is to construct the TimespanTree from an entire
    score at once:

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(bach, flatten=True,
    ...                                         classList=(note.Note, chord.Chord))
    ```

    From this representation, we can get what is happening at any given moment as a
    [`Verticality`](moduleTreeVerticality.html#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") object.

    ```python
    >>> print(scoreTree.getVerticalityAt(17.0))
    <music21.tree.verticality.Verticality 17.0 {F#3 C#4 A4}>
    ```

    The equivalent call from the stream itself is:

    > bach.asTrees(flatten=True, asTimespans=True, classList=(note.Note, chord.Chord))

    All offsets are assumed to be relative to the score’s source if flatten is True

    Example: How many moments in Bach are consonant and how many are dissonant:

    ```python
    >>> totalConsonances = 0
    >>> totalDissonances = 0
    >>> for v in scoreTree.iterateVerticalities():
    ...     if v.toChord().isConsonant():
    ...        totalConsonances += 1
    ...     else:
    ...        totalDissonances += 1
    >>> (totalConsonances, totalDissonances)
    (34, 17)
    ```

    So 1/3 of the vertical moments in Bach are dissonant! But is this an
    accurate perception? Let’s sum up the total consonant duration vs.
    dissonant duration.

    Since verticality objects do not know their end times, we can iterate pairwise
    to figure out the length. We add “padEnd=True” to include a dummy verticality
    at the end so that it includes the last object:

    ```python
    >>> totalConsonanceDuration = 0
    >>> totalDissonanceDuration = 0
    >>> iterator = scoreTree.iterateVerticalitiesNwise(n=2, padEnd=True)
    >>> for verticality1, verticality2 in iterator:
    ...     offset1 = verticality1.offset
    ...     offset2 = verticality2.offset
    ...     quarterLength = offset2 - offset1
    ...     if verticality1.toChord().isConsonant():
    ...        totalConsonanceDuration += quarterLength
    ...     else:
    ...        totalDissonanceDuration += quarterLength
    >>> (totalConsonanceDuration, totalDissonanceDuration)
    (26.5, 9.5)
    ```

    Example: Remove neighbor tones from the Bach chorale. (It’s actually quite viscous
    in its pruning.)

    Here in Alto, measure 7, there’s a neighbor tone E#.

    ```python
    >>> bach.parts['#Alto'].measure(7).show('text')
    {0.0} <music21.note.Note F#>
    {0.5} <music21.note.Note E#>
    {1.0} <music21.note.Note F#>
    {1.5} <music21.note.Note F#>
    {2.0} <music21.note.Note C#>
    ```

    We’ll get rid of it and a lot of other neighbor tones.

    ```python
    >>> for verticalities in scoreTree.iterateVerticalitiesNwise(n=3):
    ...     horizontalities = scoreTree.unwrapVerticalities(verticalities)
    ...     for unused_part, horizontality in horizontalities.items():
    ...         if horizontality.hasNeighborTone:
    ...             merged = horizontality[0].new(
    ...                endTime=horizontality[2].endTime,
    ...             )  # merged is a new PitchedTimespan
    ...             scoreTree.removeTimespan(horizontality[0])
    ...             scoreTree.removeTimespan(horizontality[1])
    ...             scoreTree.removeTimespan(horizontality[2])
    ...             scoreTree.insert(merged)
    ```

    ```python
    >>> newBach = tree.toStream.partwise(scoreTree, templateStream=bach)
    >>> newBach.parts['#Alto'].measure(7).show('text')
    {0.0} <music21.chord.Chord F#4>
    {1.5} <music21.chord.Chord F#3>
    {2.0} <music21.chord.Chord C#4>
    ```

    The second F# is an octave lower, so it wouldn’t get merged even if
    adjacent notes were fused together (which they’re not).

    Note

    TimespanTree is an implementation of an extended AVL tree. AVL
    trees are a type of binary tree, like Red-Black trees. AVL trees are
    very efficient at insertion when the objects being inserted are already
    sorted - which is usually the case with data extracted from a score.
    TimespanTree is an extended AVL tree because each node in the
    tree keeps track of not just the start offsets of PitchedTimespans
    stored at that node, but also the earliest and latest stop offset of
    all PitchedTimespans stores at both that node and all nodes which are
    children of that node. This lets us quickly located PitchedTimespans
    which overlap offsets or which are contained within ranges of offsets.
    This also means that the contents of a TimespanTree are always
    sorted.

[`TimespanTree`](#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree") bases

* [`OffsetTree`](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree")
* [`ElementTree`](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree")
* [`AVLTree`](moduleTreeCore.html#music21.tree.core.AVLTree "music21.tree.core.AVLTree")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`TimespanTree`](#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree") read-only properties

TimespanTree.offset
:   this is just for mimicking elements as streams.

    * Changed in v7: this was always meant to be a property, but was
      incorrectly a method earlier.

Read-only properties inherited from [`ElementTree`](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree"):

|  |  |  |
| --- | --- | --- |
| * [`endTime`](moduleTreeTrees.html#music21.tree.trees.ElementTree.endTime "music21.tree.trees.ElementTree.endTime") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`TimespanTree`](#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree") read/write properties

TimespanTree.element
:   defined so a TimespanTree can be used like an PitchedTimespan

    TODO: Look at subclassing or at least deriving from a common base.

Read/write properties inherited from [`ElementTree`](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree"):

|  |  |  |
| --- | --- | --- |
| * [`source`](moduleTreeTrees.html#music21.tree.trees.ElementTree.source "music21.tree.trees.ElementTree.source") |  |  |

[`TimespanTree`](#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree") methods

TimespanTree.allParts()[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.allParts)

static TimespanTree.elementEndTime(*el*, *unused\_node*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.elementEndTime)
:   Use so that both OffsetTrees, which have elements which do not have a .endTime, and
    TimespanTrees, which have element that have an .endTime but not a duration, can
    use most of the same code.

TimespanTree.findNextPitchedTimespanInSameStreamByClass(*pitchedTimespan: [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan")*, *classList=None*) → [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.findNextPitchedTimespanInSameStreamByClass)
:   Finds next element timespan in the same stream class as PitchedTimespan.

    Default classList is (stream.Part,)

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> timespan = scoreTree[0]
    >>> timespan
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
    ```

    ```python
    >>> timespan.part
    <music21.stream.Part Soprano>
    ```

    ```python
    >>> timespan = scoreTree.findNextPitchedTimespanInSameStreamByClass(timespan)
    >>> timespan
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
    ```

    ```python
    >>> timespan.part
    <music21.stream.Part Soprano>
    ```

    ```python
    >>> timespan = scoreTree.findNextPitchedTimespanInSameStreamByClass(timespan)
    >>> timespan
    <PitchedTimespan (1.0 to 2.0) <music21.note.Note A>>
    ```

    ```python
    >>> timespan.part
    <music21.stream.Part Soprano>
    ```

TimespanTree.findPreviousPitchedTimespanInSameStreamByClass(*pitchedTimespan: [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan")*, *classList=None*) → [PitchedTimespan](moduleTreeSpans.html#music21.tree.spans.PitchedTimespan "music21.tree.spans.PitchedTimespan") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.findPreviousPitchedTimespanInSameStreamByClass)
:   Finds next element timespan in the same Part/Measure, etc. (specify in classList) as
    the pitchedTimespan.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> timespan = scoreTree[-1]
    >>> timespan
    <PitchedTimespan (35.0 to 36.0) <music21.note.Note F#>>
    ```

    ```python
    >>> timespan.part
    <music21.stream.Part Bass>
    ```

    ```python
    >>> timespan = scoreTree.findPreviousPitchedTimespanInSameStreamByClass(timespan)
    >>> timespan
    <PitchedTimespan (34.0 to 35.0) <music21.note.Note B>>
    ```

    ```python
    >>> timespan.part
    <music21.stream.Part Bass>
    ```

    ```python
    >>> timespan = scoreTree.findPreviousPitchedTimespanInSameStreamByClass(timespan)
    >>> timespan
    <PitchedTimespan (33.0 to 34.0) <music21.note.Note D>>
    ```

    ```python
    >>> timespan.part
    <music21.stream.Part Bass>
    ```

TimespanTree.getVerticalityAtOrBefore(*offset*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.getVerticalityAtOrBefore)
:   Gets the [`Verticality`](moduleTreeVerticality.html#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality")
    in this TimeSpanTree which starts at offset.

    If the found Verticality has no start timespans, the function returns
    the next previous verticality with start timespans.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> scoreTree.getVerticalityAtOrBefore(0.125)
    <music21.tree.verticality.Verticality 0.0 {A3 E4 C#5}>
    ```

    ```python
    >>> scoreTree.getVerticalityAtOrBefore(0.0)
    <music21.tree.verticality.Verticality 0.0 {A3 E4 C#5}>
    ```

TimespanTree.index(*span*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.index)
:   Gets index of a TimeSpan in a TimespanTree.

    Since Timespans do not have .sites, there is only one offset to deal with

    ```python
    >>> tsList = [(0, 2), (0, 9), (1, 1), (2, 3), (3, 4),
    ...           (4, 9), (5, 6), (5, 8), (6, 8), (7, 7)]
    >>> ts = [tree.spans.Timespan(x, y) for x, y in tsList]
    >>> tsTree = tree.timespanTree.TimespanTree()
    >>> tsTree.insert(ts)
    ```

    ```python
    >>> for timespan in ts:
    ...     print(f'{timespan!r} {tsTree.index(timespan)}')
    <Timespan 0.0 2.0> 0
    <Timespan 0.0 9.0> 1
    <Timespan 1.0 1.0> 2
    <Timespan 2.0 3.0> 3
    <Timespan 3.0 4.0> 4
    <Timespan 4.0 9.0> 5
    <Timespan 5.0 6.0> 6
    <Timespan 5.0 8.0> 7
    <Timespan 6.0 8.0> 8
    <Timespan 7.0 7.0> 9
    ```

    ```python
    >>> tsTree.index(tree.spans.Timespan(-100, 100))
    Traceback (most recent call last):
    ValueError: <Timespan -100.0 100.0> not in Tree at offset -100.0.
    ```

TimespanTree.iterateConsonanceBoundedVerticalities()[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.iterateConsonanceBoundedVerticalities)
:   Iterates consonant-bounded verticality subsequences in this
    offset-tree.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> for subsequence in scoreTree.iterateConsonanceBoundedVerticalities():
    ...     print('Subsequence:')
    ...     for verticality in subsequence:
    ...         verticalityChord = verticality.toChord()
    ...         print(f'\t[{verticality.measureNumber}] '
    ...               f'{verticality}: {verticalityChord.isConsonant()}')
    Subsequence:
        [2] <music21.tree.verticality.Verticality 6.0 {E3 E4 G#4 B4}>: True
        [2] <music21.tree.verticality.Verticality 6.5 {E3 D4 G#4 B4}>: False
        [2] <music21.tree.verticality.Verticality 7.0 {A2 C#4 E4 A4}>: True
    Subsequence:
        [3] <music21.tree.verticality.Verticality 9.0 {F#3 C#4 F#4 A4}>: True
        [3] <music21.tree.verticality.Verticality 9.5 {B2 D4 G#4 B4}>: False
        [3] <music21.tree.verticality.Verticality 10.0 {C#3 C#4 E#4 G#4}>: True
    Subsequence:
        [3] <music21.tree.verticality.Verticality 10.0 {C#3 C#4 E#4 G#4}>: True
        [3] <music21.tree.verticality.Verticality 10.5 {C#3 B3 E#4 G#4}>: False
        [3] <music21.tree.verticality.Verticality 11.0 {F#2 A3 C#4 F#4}>: True
    Subsequence:
        [3] <music21.tree.verticality.Verticality 12.0 {F#3 C#4 F#4 A4}>: True
        [4] <music21.tree.verticality.Verticality 13.0 {G#3 B3 F#4 B4}>: False
        [4] <music21.tree.verticality.Verticality 13.5 {F#3 B3 F#4 B4}>: False
        [4] <music21.tree.verticality.Verticality 14.0 {G#3 B3 E4 B4}>: True
    Subsequence:
        [4] <music21.tree.verticality.Verticality 14.0 {G#3 B3 E4 B4}>: True
        [4] <music21.tree.verticality.Verticality 14.5 {A3 B3 E4 B4}>: False
        [4] <music21.tree.verticality.Verticality 15.0 {B3 D#4 F#4}>: True
    Subsequence:
        [4] <music21.tree.verticality.Verticality 15.0 {B3 D#4 F#4}>: True
        [4] <music21.tree.verticality.Verticality 15.5 {B2 A3 D#4 F#4}>: False
        [4] <music21.tree.verticality.Verticality 16.0 {C#3 G#3 C#4 E4}>: True
    Subsequence:
        [5] <music21.tree.verticality.Verticality 17.5 {F#3 D4 F#4 A4}>: True
        [5] <music21.tree.verticality.Verticality 18.0 {G#3 C#4 E4 B4}>: False
        [5] <music21.tree.verticality.Verticality 18.5 {G#3 B3 E4 B4}>: True
    Subsequence:
        [6] <music21.tree.verticality.Verticality 24.0 {F#3 C#4 F#4 A4}>: True
        [7] <music21.tree.verticality.Verticality 25.0 {B2 D4 F#4 G#4}>: False
        [7] <music21.tree.verticality.Verticality 25.5 {C#3 C#4 E#4 G#4}>: True
    Subsequence:
        [7] <music21.tree.verticality.Verticality 25.5 {C#3 C#4 E#4 G#4}>: True
        [7] <music21.tree.verticality.Verticality 26.0 {D3 C#4 F#4}>: False
        [7] <music21.tree.verticality.Verticality 26.5 {D3 F#3 B3 F#4}>: True
    Subsequence:
        [8] <music21.tree.verticality.Verticality 29.0 {A#2 F#3 C#4 F#4}>: True
        [8] <music21.tree.verticality.Verticality 29.5 {A#2 F#3 D4 F#4}>: False
        [8] <music21.tree.verticality.Verticality 30.0 {A#2 C#4 E4 F#4}>: False
        [8] <music21.tree.verticality.Verticality 31.0 {B2 C#4 E4 F#4}>: False
        [8] <music21.tree.verticality.Verticality 32.0 {C#3 B3 D4 F#4}>: False
        [8] <music21.tree.verticality.Verticality 32.5 {C#3 A#3 C#4 F#4}>: False
        [9] <music21.tree.verticality.Verticality 33.0 {D3 B3 F#4}>: True
    Subsequence:
        [9] <music21.tree.verticality.Verticality 33.0 {D3 B3 F#4}>: True
        [9] <music21.tree.verticality.Verticality 33.5 {D3 B3 C#4 F#4}>: False
        [9] <music21.tree.verticality.Verticality 34.0 {B2 B3 D4 F#4}>: True
    Subsequence:
        [9] <music21.tree.verticality.Verticality 34.0 {B2 B3 D4 F#4}>: True
        [9] <music21.tree.verticality.Verticality 34.5 {B2 B3 D4 E#4}>: False
        [9] <music21.tree.verticality.Verticality 35.0 {F#3 A#3 C#4 F#4}>: True
    ```

TimespanTree.iterateVerticalities(*reverse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → Generator['music21.tree.verticality.Verticality', [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.iterateVerticalities)
:   Iterates all vertical moments in this TimespanTree, represented as
    [`Verticality`](moduleTreeVerticality.html#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") objects.

    Note

    The TimespanTree can be mutated while its verticalities are
    iterated over. Each verticality holds a reference back to the
    TimespanTree and will ask for the start-offset after (or before) its
    own start offset in order to determine the next verticality to
    yield. If you mutate the tree by adding or deleting timespans, the
    next verticality will reflect those changes.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> iterator = scoreTree.iterateVerticalities()
    >>> for _ in range(10):
    ...     next(iterator)
    ...
    <music21.tree.verticality.Verticality 0.0 {A3 E4 C#5}>
    <music21.tree.verticality.Verticality 0.5 {G#3 B3 E4 B4}>
    <music21.tree.verticality.Verticality 1.0 {F#3 C#4 F#4 A4}>
    <music21.tree.verticality.Verticality 2.0 {G#3 B3 E4 B4}>
    <music21.tree.verticality.Verticality 3.0 {A3 E4 C#5}>
    <music21.tree.verticality.Verticality 4.0 {G#3 B3 E4 E5}>
    <music21.tree.verticality.Verticality 5.0 {A3 E4 C#5}>
    <music21.tree.verticality.Verticality 5.5 {C#3 E4 A4 C#5}>
    <music21.tree.verticality.Verticality 6.0 {E3 E4 G#4 B4}>
    <music21.tree.verticality.Verticality 6.5 {E3 D4 G#4 B4}>
    ```

    Verticalities can also be iterated in reverse:

    ```python
    >>> iterator = scoreTree.iterateVerticalities(reverse=True)
    >>> for _ in range(10):
    ...     next(iterator)
    ...
    <music21.tree.verticality.Verticality 35.0 {F#3 A#3 C#4 F#4}>
    <music21.tree.verticality.Verticality 34.5 {B2 B3 D4 E#4}>
    <music21.tree.verticality.Verticality 34.0 {B2 B3 D4 F#4}>
    <music21.tree.verticality.Verticality 33.5 {D3 B3 C#4 F#4}>
    <music21.tree.verticality.Verticality 33.0 {D3 B3 F#4}>
    <music21.tree.verticality.Verticality 32.5 {C#3 A#3 C#4 F#4}>
    <music21.tree.verticality.Verticality 32.0 {C#3 B3 D4 F#4}>
    <music21.tree.verticality.Verticality 31.0 {B2 C#4 E4 F#4}>
    <music21.tree.verticality.Verticality 30.0 {A#2 C#4 E4 F#4}>
    <music21.tree.verticality.Verticality 29.5 {A#2 F#3 D4 F#4}>
    ```

TimespanTree.iterateVerticalitiesNwise(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 3*, *\**, *reverse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *padEnd: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → Generator[[VerticalitySequence](moduleTreeVerticality.html#music21.tree.verticality.VerticalitySequence "music21.tree.verticality.VerticalitySequence"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.iterateVerticalitiesNwise)
:   Iterates [`Verticality`](moduleTreeVerticality.html#music21.tree.verticality.Verticality "music21.tree.verticality.Verticality") objects in groups of length n.

    Note

    The TimespanTree can be mutated while its verticalities are
    iterated over. Each verticality holds a reference back to the
    TimespanTree and will ask for the start-offset after (or before) its
    own start offset in order to determine the next verticality to
    yield. If you mutate the tree by adding or deleting timespans, the
    next verticality will reflect those changes.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> iterator = scoreTree.iterateVerticalitiesNwise(n=2)
    >>> for _ in range(4):
    ...     print(next(iterator))
    ...
    <music21.tree.verticality.VerticalitySequence [
        (0.0 {A3 E4 C#5}),
        (0.5 {G#3 B3 E4 B4})
        ]>
    <music21.tree.verticality.VerticalitySequence [
        (0.5 {G#3 B3 E4 B4}),
        (1.0 {F#3 C#4 F#4 A4})
        ]>
    <music21.tree.verticality.VerticalitySequence [
        (1.0 {F#3 C#4 F#4 A4}),
        (2.0 {G#3 B3 E4 B4})
        ]>
    <music21.tree.verticality.VerticalitySequence [
        (2.0 {G#3 B3 E4 B4}),
        (3.0 {A3 E4 C#5})
        ]>
    ```

    Grouped verticalities can also be iterated in reverse, but note that the
    groups within each iteration are still ordered from earliest to last.

    ```python
    >>> iterator = scoreTree.iterateVerticalitiesNwise(n=2, reverse=True)
    >>> for _ in range(4):
    ...     print(next(iterator))
    ...
    <music21.tree.verticality.VerticalitySequence [
        (34.5 {B2 B3 D4 E#4}),
        (35.0 {F#3 A#3 C#4 F#4})
        ]>
    <music21.tree.verticality.VerticalitySequence [
        (34.0 {B2 B3 D4 F#4}),
        (34.5 {B2 B3 D4 E#4})
        ]>
    <music21.tree.verticality.VerticalitySequence [
        (33.5 {D3 B3 C#4 F#4}),
        (34.0 {B2 B3 D4 F#4})
        ]>
    <music21.tree.verticality.VerticalitySequence [
        (33.0 {D3 B3 F#4}),
        (33.5 {D3 B3 C#4 F#4})
        ]>
    ```

    When iterating with n > 1 and padEnd=True will put sentinel
    Verticalities in the last VerticalitySequences that occur at the
    endTime of the tree, with no elements:

    ```python
    >>> iterator = scoreTree.iterateVerticalitiesNwise(n=3, padEnd=True)
    >>> for v in iterator:
    ...     pass
    >>> v
    <music21.tree.verticality.VerticalitySequence [
        (35.0 {F#3 A#3 C#4 F#4}),
        (36.0 {}),
        (36.0 {})
        ]>
    ```

    * Changed in v8: added padEnd. Streams with fewer than n elements
      :   also return an empty sentinel entry.

TimespanTree.maximumOverlap()[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.maximumOverlap)
:   The maximum number of timespans overlapping at any given moment in this
    timespan collection.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> scoreTree.maximumOverlap()
    4
    ```

    Returns None if there is no verticality here.

TimespanTree.removeTimespan(*elements*, *offsets=None*, *runUpdate=True*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.removeTimespan)
:   this will eventually be different from above.

TimespanTree.removeTimespanList(*elements*, *offsets=None*, *runUpdate=True*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.removeTimespanList)
:   this will eventually be different from above

TimespanTree.splitAt(*offsets*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.splitAt)
:   Splits all timespans in this TimespanTree at offsets, operating in
    place.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> scoreTree.elementsStartingAt(0.1)
    ()
    ```

    ```python
    >>> for timespan in scoreTree.elementsOverlappingOffset(0.1):
    ...     print(f'{timespan!r}, {timespan.part.id}')
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>, Soprano
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>, Tenor
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>, Bass
    <PitchedTimespan (0.0 to 1.0) <music21.note.Note E>>, Alto
    ```

    Note that the Alto is last in both of these because currently the sorting
    is done according to the endTime – potentially to be changed soon.

    ```python
    >>> scoreTree.splitAt(0.1)
    >>> for timespan in scoreTree.elementsStartingAt(0.1):
    ...     print(f'{timespan!r}, {timespan.part.id}')
    <PitchedTimespan (0.1 to 0.5) <music21.note.Note C#>>, Soprano
    <PitchedTimespan (0.1 to 0.5) <music21.note.Note A>>, Tenor
    <PitchedTimespan (0.1 to 0.5) <music21.note.Note A>>, Bass
    <PitchedTimespan (0.1 to 1.0) <music21.note.Note E>>, Alto
    ```

    ```python
    >>> scoreTree.elementsOverlappingOffset(0.1)
    ()
    ```

TimespanTree.toPartwiseTimespanTrees()[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.toPartwiseTimespanTrees)
:   Returns a dictionary of TimespanTrees where each entry
    is indexed by a Part object (TODO: Don’t use mutable objects as hash keys!)
    and each key is a TimeSpan tree containing only element timespans belonging
    to that part.

    Used by reduceChords. May disappear at any time without a deprecation
    notice.

static TimespanTree.unwrapVerticalities(*verticalities*)[[source]](../_modules/music21/tree/timespanTree.html#TimespanTree.unwrapVerticalities)
:   Unwraps a sequence of Verticality objects into a dictionary of
    Part:Horizontality key/value pairs.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans(classList=(note.Note,))
    >>> iterator = scoreTree.iterateVerticalitiesNwise()
    >>> verticalities = next(iterator)
    >>> unwrapped = scoreTree.unwrapVerticalities(verticalities)
    >>> for part in sorted(unwrapped, key=lambda x: x.partName):
    ...     print(part)
    ...     horizontality = unwrapped[part]
    ...     for timespan in horizontality:
    ...         print(f'\t{timespan!r}')
    ...
    <music21.stream.Part Alto>
        <PitchedTimespan (0.0 to 1.0) <music21.note.Note E>>
        <PitchedTimespan (1.0 to 2.0) <music21.note.Note F#>>
    <music21.stream.Part Bass>
        <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>
        <PitchedTimespan (0.5 to 1.0) <music21.note.Note G#>>
        <PitchedTimespan (1.0 to 2.0) <music21.note.Note F#>>
    <music21.stream.Part Soprano>
        <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
        <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
        <PitchedTimespan (1.0 to 2.0) <music21.note.Note A>>
    <music21.stream.Part Tenor>
        <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>
        <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
        <PitchedTimespan (1.0 to 2.0) <music21.note.Note C#>>
    ```

Methods inherited from [`OffsetTree`](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.__getitem__ "music21.tree.trees.OffsetTree.__getitem__") * [`allOffsets()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.allOffsets "music21.tree.trees.OffsetTree.allOffsets") * [`allTimePoints()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.allTimePoints "music21.tree.trees.OffsetTree.allTimePoints") * [`append()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.append "music21.tree.trees.OffsetTree.append") * [`copy()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.copy "music21.tree.trees.OffsetTree.copy") | * [`elementsOverlappingOffset()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.elementsOverlappingOffset "music21.tree.trees.OffsetTree.elementsOverlappingOffset") * [`elementsStartingAt()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.elementsStartingAt "music21.tree.trees.OffsetTree.elementsStartingAt") * [`elementsStoppingAt()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.elementsStoppingAt "music21.tree.trees.OffsetTree.elementsStoppingAt") * [`getPositionFromElementUnsafe()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.getPositionFromElementUnsafe "music21.tree.trees.OffsetTree.getPositionFromElementUnsafe") | * [`getVerticalityAt()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.getVerticalityAt "music21.tree.trees.OffsetTree.getVerticalityAt") * [`overlapTimePoints()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.overlapTimePoints "music21.tree.trees.OffsetTree.overlapTimePoints") * [`removeElements()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.removeElements "music21.tree.trees.OffsetTree.removeElements") * [`simultaneityDict()`](moduleTreeTrees.html#music21.tree.trees.OffsetTree.simultaneityDict "music21.tree.trees.OffsetTree.simultaneityDict") |

Methods inherited from [`ElementTree`](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.__eq__ "music21.tree.trees.ElementTree.__eq__") * [`getNodeByIndex()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.getNodeByIndex "music21.tree.trees.ElementTree.getNodeByIndex") * [`highestPosition()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.highestPosition "music21.tree.trees.ElementTree.highestPosition") | * [`insert()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.insert "music21.tree.trees.ElementTree.insert") * [`iterNodes()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.iterNodes "music21.tree.trees.ElementTree.iterNodes") | * [`lowestPosition()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.lowestPosition "music21.tree.trees.ElementTree.lowestPosition") * [`populateFromSortedList()`](moduleTreeTrees.html#music21.tree.trees.ElementTree.populateFromSortedList "music21.tree.trees.ElementTree.populateFromSortedList") |

Methods inherited from [`AVLTree`](moduleTreeCore.html#music21.tree.core.AVLTree "music21.tree.core.AVLTree"):

|  |  |  |
| --- | --- | --- |
| * [`createNodeAtPosition()`](moduleTreeCore.html#music21.tree.core.AVLTree.createNodeAtPosition "music21.tree.core.AVLTree.createNodeAtPosition") * [`debug()`](moduleTreeCore.html#music21.tree.core.AVLTree.debug "music21.tree.core.AVLTree.debug") * [`getNodeAfter()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeAfter "music21.tree.core.AVLTree.getNodeAfter") | * [`getNodeBefore()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeBefore "music21.tree.core.AVLTree.getNodeBefore") * [`getNodeByPosition()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeByPosition "music21.tree.core.AVLTree.getNodeByPosition") * [`getPositionAfter()`](moduleTreeCore.html#music21.tree.core.AVLTree.getPositionAfter "music21.tree.core.AVLTree.getPositionAfter") | * [`getPositionBefore()`](moduleTreeCore.html#music21.tree.core.AVLTree.getPositionBefore "music21.tree.core.AVLTree.getPositionBefore") * [`removeNode()`](moduleTreeCore.html#music21.tree.core.AVLTree.removeNode "music21.tree.core.AVLTree.removeNode") |
