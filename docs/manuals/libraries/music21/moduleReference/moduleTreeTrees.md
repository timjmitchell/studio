Source: https://music21.org/music21docs/moduleReference/moduleTreeTrees.html

# music21.tree.trees

Tools for grouping elements, timespans, and especially
pitched elements into kinds of searchable tree organized by start and stop offsets
and other positions.

## ElementTree

class music21.tree.trees.ElementTree(*elements=None*, *source=None*)[[source]](../_modules/music21/tree/trees.html#ElementTree)
:   A data structure for efficiently storing a score: flat or recursed or normal.

    This data structure has no connection to the XML ElementTree.

    This data structure stores ElementNodes: objects which implement both a
    position and endTime property. It provides fast lookups of such
    objects.

    ```python
    >>> et = tree.trees.ElementTree()
    >>> et
    <ElementTree {0} (-inf to inf)>
    ```

    ```python
    >>> s = stream.Stream()
    >>> for i in range(100):
    ...     n = note.Note()
    ...     n.duration.quarterLength = 2.0
    ...     s.insert(i * 2, n)
    ```

    ```python
    >>> for n in s:
    ...     et.insert(n)
    >>> et
    <ElementTree {100} (0.0 <0.20...> to 200.0)>
    >>> et.rootNode
    <ElementNode: Start:126.0 <0.20...> Indices:(l:0 *63* r:100) Payload:<music21.note.Note C>>
    ```

    ```python
    >>> n2 = s[-1]
    ```

    These operations are very fast

    ```python
    >>> et.index(n2, n2.sortTuple())
    99
    ```

    Get a position after a certain position:

    ```python
    >>> st = s[40].sortTuple()
    >>> st
    SortTuple(atEnd=0, offset=80.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=...)
    >>> st2 = et.getPositionAfter(st)
    >>> st2.shortRepr()
    '82.0 <0.20...>'
    >>> st2.offset
    82.0
    ```

    ```python
    >>> st3 = et.getPositionAfter(5.0)
    >>> st3.offset
    6.0
    >>> et.getPositionAfter(4.0).offset
    6.0
    ```

[`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree") bases

* [`AVLTree`](moduleTreeCore.html#music21.tree.core.AVLTree "music21.tree.core.AVLTree")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree") read-only properties

ElementTree.endTime
:   Gets the latest stop position in this element-tree.

    This is cast as a property so that it can be used like a TimeSpan in a TimeSpanTree

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> tsTree = score.asTree()
    >>> tsTree.endTime
    36.0
    ```

    Returns infinity if no elements exist:

    ```python
    >>> et = tree.trees.ElementTree()
    >>> et.endTime
    inf
    ```

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree") read/write properties

ElementTree.source
:   the original stream. (stored as a weakref but returned unwrapped)

    ```python
    >>> example = tree.examples.makeExampleScore()
    >>> eTree = example.asTree()
    >>> eTree.source is example
    True
    ```

    ```python
    >>> s = stream.Stream()
    >>> eTree.source = s
    >>> eTree.source is s
    True
    ```

[`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree") methods

ElementTree.\_\_eq\_\_(*expr*)[[source]](../_modules/music21/tree/trees.html#ElementTree.__eq__)
:   Two ElementTrees are equal only if they are the same object.

    ```python
    >>> et1 = tree.trees.ElementTree()
    >>> et2 = tree.trees.ElementTree()
    >>> et3 = et1
    >>> et1 == et2
    False
    >>> et1 == et3
    True
    ```

    ```python
    >>> et2 != et1
    True
    ```

ElementTree.\_\_getitem\_\_(*i*)[[source]](../_modules/music21/tree/trees.html#ElementTree.__getitem__)
:   Gets elements by integer index or slice. This is pretty fast in computational time
    (O(log n)), but it’s O(log n) in Python while normal list slicing is O(1) in C, so
    don’t use trees for \_\_getitem\_\_ searching if you don’t have to.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTree(flatten=True)
    >>> scoreTree
    <ElementTree {20} (0.0 <0.-25...> to 8.0) <music21.stream.Score exampleScore>>
    ```

    ```python
    >>> scoreTree[0]
    <music21.instrument.Instrument 'PartA: : '>
    ```

    ```python
    >>> scoreTree[-1]
    <music21.bar.Barline type=final>
    ```

    ```python
    >>> scoreTree[2000] is None
    True
    ```

    Slices work

    ```python
    >>> scoreTree[2:5]
    [<music21.clef.BassClef>, <music21.clef.BassClef>, <music21.meter.TimeSignature 2/4>]
    ```

    ```python
    >>> scoreTree[-6:-3]
    [<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note D#>]
    ```

    ```python
    >>> scoreTree[-100:-200]
    []
    ```

    ```python
    >>> for x in scoreTree[:]:
    ...     x
    <music21.instrument.Instrument 'PartA: : '>
            ...
    <music21.bar.Barline type=final>
    ```

    These should all be the same as the flat version:

    ```python
    >>> scoreFlat = score.flatten()
    >>> for i in (0, -1, 10):
    ...     if scoreFlat[i] is not scoreTree[i]:
    ...          print('false!')
    ```

    ```python
    >>> for i, j in ((2, 5), (-6, -3)):
    ...     sfSlice = scoreFlat[i:j]
    ...     for n in range(i, j):
    ...         sliceOffset = n - i
    ...         if sfSlice[sliceOffset] is not scoreFlat[n]:
    ...             print('false!')
    ```

ElementTree.getNodeByIndex(*i*)[[source]](../_modules/music21/tree/trees.html#ElementTree.getNodeByIndex)
:   Get a node whose element is at a particular index (not position). Works with slices too

    See \_\_getitem\_\_ for caveats about speed.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTree(flatten=True)
    >>> scoreTree
    <ElementTree {20} (0.0 <0.-25...> to 8.0) <music21.stream.Score exampleScore>>
    ```

    ```python
    >>> scoreTree.getNodeByIndex(0)
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:0 *0* r:2)
        Payload:<music21.instrument.Instrument 'PartA: : '>>
    ```

    ```python
    >>> scoreTree.getNodeByIndex(-1)
    <ElementNode: Start:End <0.-5...> Indices:(l:19 *19* r:20)
        Payload:<music21.bar.Barline type=final>>
    ```

    ```python
    >>> scoreTree.getNodeByIndex(slice(2, 5))
    [<ElementNode: Start:0.0 <0.0...> Indices:(l:0 *2* r:4) Payload:<music21.clef.BassClef>>,
     <ElementNode: Start:0.0 <0.0...> Indices:(l:3 *3* r:4) Payload:<music21.clef.BassClef>>,
     <ElementNode: Start:0.0 <0.4...> Indices:(l:0 *4* r:8)
         Payload:<music21.meter.TimeSignature 2/4>>]
    ```

    ```python
    >>> scoreTree.getNodeByIndex(slice(-6, -3))
    [<ElementNode: Start:5.0 <0.20...> Indices:(l:9 *14* r:20) Payload:<music21.note.Note A>>,
     <ElementNode: Start:6.0 <0.20...> Indices:(l:15 *15* r:17) Payload:<music21.note.Note B>>,
     <ElementNode: Start:6.0 <0.20...> Indices:(l:16 *16* r:17) Payload:<music21.note.Note D#>>]
    ```

    ```python
    >>> scoreTree.getNodeByIndex(slice(-100, -200))
    []
    ```

ElementTree.getPositionFromElementUnsafe(*el*)[[source]](../_modules/music21/tree/trees.html#ElementTree.getPositionFromElementUnsafe)
:   A quick but dirty method for getting the likely position (or offset) of an element
    within the elementTree from the element itself. Such as calling

    el.getOffsetBySite(tree.source) or something like that.

    Pulled out for subclassing

ElementTree.highestPosition()[[source]](../_modules/music21/tree/trees.html#ElementTree.highestPosition)
:   Gets the latest position in this tree.

    Keep as a property, because a similar property exists on streams.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> tsTree = score.asTimespans(classList=(note.Note,))
    >>> tsTree.highestPosition()
    35.0
    ```

ElementTree.index(*element*, *position=None*)[[source]](../_modules/music21/tree/trees.html#ElementTree.index)
:   Gets index of element in tree. position could be none.

    If the element is in the original score, then it should be very fast (O(log n))

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreFlat = score.flatten()
    >>> n = scoreFlat.notes[-1]
    ```

    ```python
    >>> flatTree = scoreFlat.asTree()
    >>> flatTree.index(n)
    17
    ```

    If it’s not in the original stream, then it should be slower than doing
    it on a stream (O (n log n)).

    ```python
    >>> scoreTree = score.asTree(flatten=True)
    >>> n = score.flatten().notes[-1]
    >>> scoreTree.index(n)
    17
    ```

    And if it’s nowhere at all, you get a ValueError!

    ```python
    >>> scoreTree.index(note.Note('F-'))
    Traceback (most recent call last):
    ValueError: <music21.note.Note F-> not in Tree at position
        SortTuple(atEnd=0, offset=0.0, priority=0, ...).
    ```

ElementTree.insert(*positionsOrElements*, *elements=None*)[[source]](../_modules/music21/tree/trees.html#ElementTree.insert)
:   Inserts elements or Timespans into this tree.

    ```python
    >>> n = note.Note()
    >>> ot = tree.trees.OffsetTree()
    >>> ot
    <OffsetTree {0} (-inf to inf)>
    >>> ot.insert(10.0, n)
    >>> ot
    <OffsetTree {1} (10.0 to 11.0)>
    ```

    ```python
    >>> n2 = note.Note('D')
    >>> n2.offset = 20
    >>> n3 = note.Note('E')
    >>> n3.offset = 5
    >>> ot.insert([n2, n3])
    >>> ot
    <OffsetTree {3} (5.0 to 21.0)>
    ```

ElementTree.iterNodes()[[source]](../_modules/music21/tree/trees.html#ElementTree.iterNodes)
:   Identical to the iterating on a core.AVLTree – yields each node in order

    Slow: O(n log n) time so don’t make this your main thing.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTree(flatten=True)
    >>> scoreTree
    <ElementTree {20} (0.0 <0.-25...> to 8.0) <music21.stream.Score exampleScore>>
    ```

    ```python
    >>> for node in scoreTree.iterNodes():
    ...     print(node)
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:0 *0* r:2)
            Payload:<music21.instrument.Instrument 'PartA: : '>>
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:1 *1* r:2)
            Payload:<music21.instrument.Instrument 'PartB: : '>>
    <ElementNode: Start:0.0 <0.0...> Indices:(l:0 *2* r:4) Payload:<music21.clef.BassClef>>
    <ElementNode: Start:0.0 <0.0...> Indices:(l:3 *3* r:4) Payload:<music21.clef.BassClef>>
    <ElementNode: Start:0.0 <0.4...> Indices:(l:0 *4* r:8)
            Payload:<music21.meter.TimeSignature 2/4>>
    <ElementNode: Start:0.0 <0.4...> Indices:(l:5 *5* r:6)
            Payload:<music21.meter.TimeSignature 2/4>>
    <ElementNode: Start:0.0 <0.20...> Indices:(l:5 *6* r:8) Payload:<music21.note.Note C>>
    <ElementNode: Start:0.0 <0.20...> Indices:(l:7 *7* r:8) Payload:<music21.note.Note C#>>
    <ElementNode: Start:1.0 <0.20...> Indices:(l:0 *8* r:20) Payload:<music21.note.Note D>>
    <ElementNode: Start:2.0 <0.20...> Indices:(l:9 *9* r:11) Payload:<music21.note.Note E>>
        ...
    <ElementNode: Start:7.0 <0.20...> Indices:(l:15 *17* r:20)
            Payload:<music21.note.Note C>>
    <ElementNode: Start:End <0.-5...> Indices:(l:18 *18* r:20)
            Payload:<music21.bar.Barline type=final>>
    <ElementNode: Start:End <0.-5...> Indices:(l:19 *19* r:20)
            Payload:<music21.bar.Barline type=final>>
    ```

ElementTree.lowestPosition()[[source]](../_modules/music21/tree/trees.html#ElementTree.lowestPosition)
:   Gets the earliest position in this tree.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> elTree = score.asTree()
    >>> elTree.lowestPosition().shortRepr()
    '0.0 <0.-20...>'
    ```

    ```python
    >>> tsTree = score.asTimespans()
    >>> tsTree.lowestPosition()
    0.0
    ```

ElementTree.populateFromSortedList(*listOfTuples*)[[source]](../_modules/music21/tree/trees.html#ElementTree.populateFromSortedList)
:   This method assumes that the current tree is empty (or will be wiped) and
    that listOfTuples is a non-empty
    list where the first element is a unique position to insert,
    and the second is the complete payload for that node, and
    that the positions are strictly increasing in order.

    This is about an order of magnitude faster (3ms vs 21ms for 1000 items; 31 vs. 30ms for
    10,000 items) than running createNodeAtPosition() for each element in a list if it is
    already sorted. Thus, it should be used when converting a
    Stream where .isSorted is True into a tree.

    If any of the conditions is not true, expect to get a dangerously
    badly sorted tree that will be useless.

    ```python
    >>> bFlat = corpus.parse('bwv66.6').flatten()
    >>> bFlat.isSorted
    True
    ```

    ```python
    >>> listOfTuples = [(e.sortTuple(bFlat), e) for e in bFlat]
    >>> listOfTuples[14]
    (SortTuple(atEnd=0, offset=0.0, priority=0, ...),
     <music21.key.Key of f# minor>)
    ```

    ```python
    >>> et = tree.trees.ElementTree()
    >>> et.rootNode is None
    True
    >>> et.populateFromSortedList(listOfTuples)
    >>> et.rootNode
    <ElementNode: Start:14.5 <0.20...> Indices:(l:0 *99* r:199)
        Payload:<music21.note.Note A>>
    ```

    ```python
    >>> n = et.rootNode
    >>> while n is not None:
    ...    print(n)
    ...    n = n.leftChild
    <ElementNode: Start:14.5 <0.20...> Indices:(l:0 *99* r:199) Payload:<music21.note.Note A>>
    <ElementNode: Start:5.5 <0.20...>  Indices:(l:0 *49* r:99) Payload:<music21.note.Note A>>
    <ElementNode: Start:0.0 <0.20...>  Indices:(l:0 *24* r:49) Payload:<music21.note.Note A>>
    <ElementNode: Start:0.0 <0.1...>   Indices:(l:0 *12* r:24)
        Payload:<music21.tempo.MetronomeMark Quarter=96 (playback only)>>
    <ElementNode: Start:0.0 <0.0...>   Indices:(l:0 *6* r:12) Payload:<music21.clef.TrebleClef>>
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:0 *3* r:6)
        Payload:<music21.instrument.Instrument 'P3: Tenor: Instrument 3'>>
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:0 *1* r:3)
        Payload:<music21.instrument.Instrument 'P1: Soprano: Instrument 1'>>
    <ElementNode: Start:0.0 <0.-30...> Indices:(l:0 *0* r:1)
        Payload:<music21.metadata.Metadata object at 0x104adbdd8>>
    ```

    ```python
    >>> n = et.rootNode
    >>> while n is not None:
    ...    print(n)
    ...    n = n.rightChild
    <ElementNode: Start:14.5 <0.20...> Indices:(l:0 *99* r:199)
        Payload:<music21.note.Note A>>
    <ElementNode: Start:25.0 <0.20...> Indices:(l:100 *149* r:199)
        Payload:<music21.note.Note G#>>
    <ElementNode: Start:31.0 <0.20...> Indices:(l:150 *174* r:199)
        Payload:<music21.note.Note B>>
    <ElementNode: Start:34.0 <0.20...> Indices:(l:175 *187* r:199)
        Payload:<music21.note.Note D>>
    <ElementNode: Start:35.0 <0.20...> Indices:(l:188 *193* r:199)
        Payload:<music21.note.Note A#>>
    <ElementNode: Start:36.0 <0.-5...> Indices:(l:194 *196* r:199)
        Payload:<music21.bar.Barline type=final>>
    <ElementNode: Start:36.0 <0.-5...> Indices:(l:197 *198* r:199)
        Payload:<music21.bar.Barline type=final>>
    ```

Methods inherited from [`AVLTree`](moduleTreeCore.html#music21.tree.core.AVLTree "music21.tree.core.AVLTree"):

|  |  |  |
| --- | --- | --- |
| * [`createNodeAtPosition()`](moduleTreeCore.html#music21.tree.core.AVLTree.createNodeAtPosition "music21.tree.core.AVLTree.createNodeAtPosition") * [`debug()`](moduleTreeCore.html#music21.tree.core.AVLTree.debug "music21.tree.core.AVLTree.debug") * [`getNodeAfter()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeAfter "music21.tree.core.AVLTree.getNodeAfter") | * [`getNodeBefore()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeBefore "music21.tree.core.AVLTree.getNodeBefore") * [`getNodeByPosition()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeByPosition "music21.tree.core.AVLTree.getNodeByPosition") * [`getPositionAfter()`](moduleTreeCore.html#music21.tree.core.AVLTree.getPositionAfter "music21.tree.core.AVLTree.getPositionAfter") | * [`getPositionBefore()`](moduleTreeCore.html#music21.tree.core.AVLTree.getPositionBefore "music21.tree.core.AVLTree.getPositionBefore") * [`removeNode()`](moduleTreeCore.html#music21.tree.core.AVLTree.removeNode "music21.tree.core.AVLTree.removeNode") |

## OffsetTree

class music21.tree.trees.OffsetTree(*elements=None*, *source=None*)[[source]](../_modules/music21/tree/trees.html#OffsetTree)
:   A tree representation where positions are offsets in the score
    and each node has a payload which is a list of elements at
    that offset (unsorted by sort order).

[`OffsetTree`](#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") bases

* [`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree")
* [`AVLTree`](moduleTreeCore.html#music21.tree.core.AVLTree "music21.tree.core.AVLTree")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OffsetTree`](#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") read-only properties

Read-only properties inherited from [`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree"):

|  |  |  |
| --- | --- | --- |
| * [`endTime`](#music21.tree.trees.ElementTree.endTime "music21.tree.trees.ElementTree.endTime") |  |  |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OffsetTree`](#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") read/write properties

Read/write properties inherited from [`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree"):

|  |  |  |
| --- | --- | --- |
| * [`source`](#music21.tree.trees.ElementTree.source "music21.tree.trees.ElementTree.source") |  |  |

[`OffsetTree`](#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") methods

OffsetTree.\_\_getitem\_\_(*i*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.__getitem__)
:   Gets elements by integer index or slice.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTree(flatten=True, groupOffsets=True)
    ```

    ```python
    >>> scoreTree[0]
    <music21.instrument.Instrument 'PartA: : '>
    ```

    ```python
    >>> scoreTree[-1]
    <music21.bar.Barline type=final>
    ```

    ```python
    >>> scoreTree[2:5]
    [<music21.clef.BassClef>, <music21.clef.BassClef>, <music21.meter.TimeSignature 2/4>]
    ```

    ```python
    >>> scoreTree[-6:-3]
    [<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note D#>]
    ```

    ```python
    >>> scoreTree[-100:-200]
    []
    ```

OffsetTree.allOffsets()[[source]](../_modules/music21/tree/trees.html#OffsetTree.allOffsets)
:   Gets all unique offsets of all timespans in this offset-tree.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> tsTree = score.asTimespans()
    >>> for offset in tsTree.allOffsets()[:10]:
    ...     offset
    ...
    0.0
    0.5
    1.0
    2.0
    3.0
    4.0
    5.0
    5.5
    6.0
    6.5
    ```

OffsetTree.allTimePoints()[[source]](../_modules/music21/tree/trees.html#OffsetTree.allTimePoints)
:   Gets all unique offsets (both starting and stopping) of all elements/timespans
    in this offset-tree.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> for offset in scoreTree.allTimePoints()[:10]:
    ...     offset
    ...
    0.0
    0.5
    1.0
    2.0
    3.0
    4.0
    5.0
    5.5
    6.0
    6.5
    ```

OffsetTree.append(*el*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.append)
:   Add an element to the end, making certain speed savings.

OffsetTree.copy()[[source]](../_modules/music21/tree/trees.html#OffsetTree.copy)
:   Creates a new tree with the same payload as this tree.

    This is analogous to dict.copy().

    Much, much faster than creating a new tree; creating one
    with 3600 items took 500ms. Creating the tree the first time
    was 40 seconds, so about an 80x speedup.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTimespans()
    >>> newTree = scoreTree.copy()
    >>> newTree
    <TimespanTree {20} (0.0 to 8.0) <music21.stream.Score exampleScore>>
    ```

    ```python
    >>> scoreTree[16]
    <PitchedTimespan (6.0 to 8.0) <music21.note.Note D#>>
    >>> newTree[16]
    <PitchedTimespan (6.0 to 8.0) <music21.note.Note D#>>
    ```

    ```python
    >>> scoreTree[16] is newTree[16]
    True
    ```

static OffsetTree.elementEndTime(*el*, *node*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.elementEndTime)
:   Use so that both OffsetTrees, which have elements which do not have a .endTime, and
    TimespanTrees, which have element that have an .endTime but not a duration, can
    use most of the same code.

OffsetTree.elementsOverlappingOffset(*offset*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.elementsOverlappingOffset)
:   Finds elements in this ElementTree which overlap offset.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTree(flatten=True, groupOffsets=True)
    >>> for el in scoreTree.elementsOverlappingOffset(0.5):
    ...     el
    ...
    <music21.note.Note E>
    ```

    Works with Timespans in TimespanTrees as well.

    ```python
    >>> scoreTree = score.asTimespans()
    >>> for el in scoreTree.elementsOverlappingOffset(0.5):
    ...     el
    ...
    <PitchedTimespan (0.0 to 1.0) <music21.note.Note E>>
    ```

OffsetTree.elementsStartingAt(*position*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.elementsStartingAt)
:   Finds elements or timespans in this tree which start at position.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTimespans()
    >>> for timespan in scoreTree.elementsStartingAt(0.5):
    ...     timespan
    ...
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note G#>>
    ```

OffsetTree.elementsStoppingAt(*offset*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.elementsStoppingAt)
:   Finds elements in this OffsetTree which stop at offset. Elements are ordered
    according to (start) offset.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = score.asTree(flatten=True, groupOffsets=True)
    >>> for el in scoreTree.elementsStoppingAt(0.5):
    ...     el
    <music21.note.Note C#>
    <music21.note.Note A>
    <music21.note.Note A>
    ```

    Works also on timespans for TimespanTrees:

    ```python
    >>> scoreTree = score.asTimespans()
    >>> for el in scoreTree.elementsStoppingAt(0.5):
    ...     el
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>
    ```

OffsetTree.getPositionFromElementUnsafe(*el*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.getPositionFromElementUnsafe)
:   A quick but dirty method for getting the likely position (or offset) of an element
    within the elementTree from the element itself. Such as calling

    el.getOffsetBySite(tree.source) or something like that.

    Pulled out for subclassing

OffsetTree.getVerticalityAt(*offset*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.getVerticalityAt)
:   Gets the verticality in this offset-tree which starts at offset.

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> scoreTree = bach.asTimespans()
    >>> scoreTree.getVerticalityAt(2.5)
    <music21.tree.verticality.Verticality 2.5 {G#3 B3 E4 B4}>
    ```

    Verticalities outside the range still return a Verticality, but it might be empty:

    ```python
    >>> scoreTree.getVerticalityAt(2000)
    <music21.tree.verticality.Verticality 2000 {}>
    ```

    Test that it still works if the tree is empty:

    ```python
    >>> scoreTree = bach.asTimespans(classList=(instrument.Tuba,))
    >>> scoreTree
    <TimespanTree {0} (-inf to inf) <music21.stream.Score ...>>
    >>> scoreTree.getVerticalityAt(5.0)
    <music21.tree.verticality.Verticality 5.0 {}>
    ```

    Returns a verticality.Verticality object.

OffsetTree.overlapTimePoints(*includeStopPoints=False*, *returnVerticality=False*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.overlapTimePoints)
:   Gets all time-points where some element is starting
    (or if includeStopPoints is True, where some element is starting or stopping)
    while some other element is still continuing onward.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreOffsetTree = score.asTree(flatten=True, groupOffsets=True)
    >>> scoreOffsetTree.overlapTimePoints()
    [0.5, 5.5, 6.5, 10.5, 13.5, 14.5, 15.5...]
    ```

    if returnVerticality is True, then a mapping of time point to elements is returned.
    How cool is that?

    ```python
    >>> otp = scoreOffsetTree.overlapTimePoints(returnVerticality=True)
    >>> otp[0]
    {0.5: <music21.tree.verticality.Verticality 0.5 {G#3 B3 E4 B4}>}
    ```

OffsetTree.removeElements(*elements*, *offsets=None*, *runUpdate=True*)[[source]](../_modules/music21/tree/trees.html#OffsetTree.removeElements)
:   Removes elements which can be Music21Objects or Timespans
    (a single one or a list) from this Tree.

    Much safer (for non-timespans) if a list of offsets is used, but it is optional.

    If runUpdate is False then the tree will be left with incorrect indices and
    endTimes; but it can speed up operations where an element is going to be removed
    and then immediately replaced: i.e., where the position of an element has changed.

OffsetTree.simultaneityDict()[[source]](../_modules/music21/tree/trees.html#OffsetTree.simultaneityDict)
:   Creates a dictionary of offsets that have more than one element starting at that time,
    where the keys are offset times and the values are lists of elements at that moment.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTree(flatten=True, groupOffsets=True)
    >>> scoreTree
    <OffsetTree {20} (0.0 to 8.0) <music21.stream.Score exampleScore>>
    ```

    ```python
    >>> sd = scoreTree.simultaneityDict()
    >>> len(sd)
    5
    >>> list(sorted(sd.keys()))
    [0.0, 2.0, 4.0, 6.0, 8.0]
    >>> sd[0.0]
    [<music21.instrument.Instrument 'PartA: : '>,
     <music21.instrument.Instrument 'PartB: : '>,
     <music21.clef.BassClef>,
     <music21.clef.BassClef>,
     <music21.meter.TimeSignature 2/4>,
     <music21.meter.TimeSignature 2/4>,
     <music21.note.Note C>,
     <music21.note.Note C#>]
    >>> sd[2.0]
    [<music21.note.Note E>, <music21.note.Note G#>]
    ```

Methods inherited from [`ElementTree`](#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](#music21.tree.trees.ElementTree.__eq__ "music21.tree.trees.ElementTree.__eq__") * [`getNodeByIndex()`](#music21.tree.trees.ElementTree.getNodeByIndex "music21.tree.trees.ElementTree.getNodeByIndex") * [`highestPosition()`](#music21.tree.trees.ElementTree.highestPosition "music21.tree.trees.ElementTree.highestPosition") | * [`index()`](#music21.tree.trees.ElementTree.index "music21.tree.trees.ElementTree.index") * [`insert()`](#music21.tree.trees.ElementTree.insert "music21.tree.trees.ElementTree.insert") * [`iterNodes()`](#music21.tree.trees.ElementTree.iterNodes "music21.tree.trees.ElementTree.iterNodes") | * [`lowestPosition()`](#music21.tree.trees.ElementTree.lowestPosition "music21.tree.trees.ElementTree.lowestPosition") * [`populateFromSortedList()`](#music21.tree.trees.ElementTree.populateFromSortedList "music21.tree.trees.ElementTree.populateFromSortedList") |

Methods inherited from [`AVLTree`](moduleTreeCore.html#music21.tree.core.AVLTree "music21.tree.core.AVLTree"):

|  |  |  |
| --- | --- | --- |
| * [`createNodeAtPosition()`](moduleTreeCore.html#music21.tree.core.AVLTree.createNodeAtPosition "music21.tree.core.AVLTree.createNodeAtPosition") * [`debug()`](moduleTreeCore.html#music21.tree.core.AVLTree.debug "music21.tree.core.AVLTree.debug") * [`getNodeAfter()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeAfter "music21.tree.core.AVLTree.getNodeAfter") | * [`getNodeBefore()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeBefore "music21.tree.core.AVLTree.getNodeBefore") * [`getNodeByPosition()`](moduleTreeCore.html#music21.tree.core.AVLTree.getNodeByPosition "music21.tree.core.AVLTree.getNodeByPosition") * [`getPositionAfter()`](moduleTreeCore.html#music21.tree.core.AVLTree.getPositionAfter "music21.tree.core.AVLTree.getPositionAfter") | * [`getPositionBefore()`](moduleTreeCore.html#music21.tree.core.AVLTree.getPositionBefore "music21.tree.core.AVLTree.getPositionBefore") * [`removeNode()`](moduleTreeCore.html#music21.tree.core.AVLTree.removeNode "music21.tree.core.AVLTree.removeNode") |
