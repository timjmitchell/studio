Source: https://music21.org/music21docs/moduleReference/moduleTreeFromStream.html

# music21.tree.fromStream

Tools for creating timespans (fast, manipulable objects) from Streams

## Functions

music21.tree.fromStream.asTimespans(*inputStream*, *\**, *flatten: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *classList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [TimespanTree](moduleTreeTimespanTree.html#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree")[[source]](../_modules/music21/tree/fromStream.html#asTimespans)
:   Recurses through a score and constructs a
    `TimespanTree`. Use Stream.asTimespans() generally
    since that caches the TimespanTree.

    ```python
    >>> score = corpus.parse('bwv66.6')
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=True,
    ...                                         classList=(note.Note, chord.Chord))
    >>> scoreTree
    <TimespanTree {165} (0.0 to 36.0) <music21.stream.Score ...>>
    >>> for x in scoreTree[:5]:
    ...     x
    ...
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note C#>>
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>
    <PitchedTimespan (0.0 to 0.5) <music21.note.Note A>>
    <PitchedTimespan (0.0 to 1.0) <music21.note.Note E>>
    <PitchedTimespan (0.5 to 1.0) <music21.note.Note B>>
    ```

    ```python
    >>> scoreTree = tree.fromStream.asTimespans(score, flatten=False, classList=())
    ```

    Each of these has 11 elements – mainly the Measures

    ```python
    >>> for x in scoreTree:
    ...     x
    ...
    <ElementTimespan (0.0 to 0.0) <music21.metadata.Metadata object at 0x...>>
    <ElementTimespan (0.0 to 0.0) <music21.layout.StaffGroup ...>>
    <TimespanTree {11} (0.0 to 36.0) <music21.stream.Part Soprano>>
    <TimespanTree {11} (0.0 to 36.0) <music21.stream.Part Alto>>
    <TimespanTree {11} (0.0 to 36.0) <music21.stream.Part Tenor>>
    <TimespanTree {11} (0.0 to 36.0) <music21.stream.Part Bass>>
    ```

    ```python
    >>> tenorElements = scoreTree[4]
    >>> tenorElements
    <TimespanTree {11} (0.0 to 36.0) <music21.stream.Part Tenor>>
    ```

    ```python
    >>> tenorElements.source
    <music21.stream.Part Tenor>
    ```

    ```python
    >>> tenorElements.source is score[3]
    True
    ```

music21.tree.fromStream.asTree(*inputStream: StreamType*, *\**, *flatten: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['semiFlat'] | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *classList: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *useTimespans: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *groupOffsets: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [OffsetTree](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") | [ElementTree](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree") | [TimespanTree](moduleTreeTimespanTree.html#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree")[[source]](../_modules/music21/tree/fromStream.html#asTree)
:   Converts a Stream and constructs an [`ElementTree`](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree") based on this.

    Use Stream.asTree() generally since that caches the ElementTree.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> elementTree = tree.fromStream.asTree(score)
    >>> elementTree
    <ElementTree {2} (0.0 <0.-20...> to 8.0) <music21.stream.Score exampleScore>>
    >>> for x in elementTree.iterNodes():
    ...     x
    <ElementNode: Start:0.0 <0.-20...> Indices:(l:0 *0* r:1) Payload:<music21.stream.Part ...>>
    <ElementNode: Start:0.0 <0.-20...> Indices:(l:0 *1* r:2) Payload:<music21.stream.Part ...>>
    ```

    ```python
    >>> etFlat = tree.fromStream.asTree(score, flatten=True)
    >>> etFlat
    <ElementTree {20} (0.0 <0.-25...> to 8.0) <music21.stream.Score exampleScore>>
    ```

    The elementTree’s classSortOrder has changed to -25 to match the lowest positioned element
    in the score, which is an Instrument object (classSortOrder=-25)

    ```python
    >>> for x in etFlat.iterNodes():
    ...     x
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:0 *0* r:2)
        Payload:<music21.instrument.Instrument 'PartA: : '>>
    <ElementNode: Start:0.0 <0.-25...> Indices:(l:1 *1* r:2)
        Payload:<music21.instrument.Instrument 'PartB: : '>>
    <ElementNode: Start:0.0 <0.0...> Indices:(l:0 *2* r:4) Payload:<music21.clef.BassClef>>
    <ElementNode: Start:0.0 <0.0...> Indices:(l:3 *3* r:4) Payload:<music21.clef.BassClef>>
    ...
    <ElementNode: Start:0.0 <0.20...> Indices:(l:5 *6* r:8) Payload:<music21.note.Note C>>
    <ElementNode: Start:0.0 <0.20...> Indices:(l:7 *7* r:8) Payload:<music21.note.Note C#>>
    <ElementNode: Start:1.0 <0.20...> Indices:(l:0 *8* r:20) Payload:<music21.note.Note D>>
    ...
    <ElementNode: Start:7.0 <0.20...> Indices:(l:15 *17* r:20) Payload:<music21.note.Note C>>
    <ElementNode: Start:End <0.-5...> Indices:(l:18 *18* r:20)
        Payload:<music21.bar.Barline type=final>>
    <ElementNode: Start:End <0.-5...> Indices:(l:19 *19* r:20)
        Payload:<music21.bar.Barline type=final>>
    ```

    ```python
    >>> etFlat.getPositionAfter(0.5)
    SortTuple(atEnd=0, offset=1.0, priority=0, classSortOrder=20, isNotGrace=1, insertIndex=...)
    ```

    ```python
    >>> etFlatNotes = tree.fromStream.asTree(score, flatten=True, classList=(note.Note,))
    >>> etFlatNotes
    <ElementTree {12} (0.0 <0.20...> to 8.0) <music21.stream.Score exampleScore>>
    ```

music21.tree.fromStream.listOfTreesByClass(*inputStream: StreamType*, *\**, *classLists: Sequence[Sequence[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[M21ObjType]]] = ()*, *currentParentage: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[stream.Stream, ...] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *initialOffset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.0*, *flatten: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = False*, *useTimespans: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[trees.OffsetTree](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") | [timespanTree.TimespanTree](moduleTreeTimespanTree.html#music21.tree.timespanTree.TimespanTree "music21.tree.timespanTree.TimespanTree")][[source]](../_modules/music21/tree/fromStream.html#listOfTreesByClass)
:   To be DEPRECATED in v8: this is no faster than calling streamToTimespanTree
    multiple times with different classLists.

    Recurses through inputStream, and constructs TimespanTrees for each
    encountered substream and PitchedTimespan for each encountered non-stream
    element.

    classLists should be a sequence of elements contained in classSet. One
    TimespanTree will be constructed for each element in classLists, in
    a single optimized pass through the inputStream.

    This is used internally by streamToTimespanTree.

    ```python
    >>> score = tree.examples.makeExampleScore()
    ```

    Get everything in the score

    ```python
    >>> treeList = tree.fromStream.listOfTreesByClass(score, useTimespans=True)
    >>> treeList
    [<TimespanTree {2} (-inf to inf) <music21.stream.Score ...>>]
    >>> tl0 = treeList[0]
    >>> for t in tl0:
    ...     print(t)
    <TimespanTree {4} (-inf to inf) <music21.stream.Part ...>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 1 offset=0.0>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 2 offset=2.0>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 3 offset=4.0>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 4 offset=6.0>>
    <TimespanTree {4} (-inf to inf) <music21.stream.Part ...>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 1 offset=0.0>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 2 offset=2.0>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 3 offset=4.0>>
        <TimespanTree {0} (-inf to inf) <music21.stream.Measure 4 offset=6.0>>
    ```

    Now filter the Notes and the Clefs & TimeSignatures of the score
    (flattened) into a list of two TimespanTrees

    ```python
    >>> classLists = ((note.Note,), (clef.Clef, meter.TimeSignature))
    >>> treeList = tree.fromStream.listOfTreesByClass(score, useTimespans=True,
    ...                                               classLists=classLists, flatten=True)
    >>> treeList
    [<TimespanTree {12} (0.0 to 8.0) <music21.stream.Score ...>>,
     <TimespanTree {4} (0.0 to 0.0) <music21.stream.Score ...>>]
    ```

    * Changed in v8: it is now a stickler that classLists must be sequences of sequences,
      :   such as tuples of tuples.

music21.tree.fromStream.makeFastShallowTreeFromSortedStream(*inputStream: stream.Stream*, *\**, *outputTree: [trees.OffsetTree](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") | [trees.ElementTree](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree")*, *classList: Sequence[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [trees.OffsetTree](moduleTreeTrees.html#music21.tree.trees.OffsetTree "music21.tree.trees.OffsetTree") | [trees.ElementTree](moduleTreeTrees.html#music21.tree.trees.ElementTree "music21.tree.trees.ElementTree")[[source]](../_modules/music21/tree/fromStream.html#makeFastShallowTreeFromSortedStream)
:   Use populateFromSortedList to quickly make a tree from a stream.

    This only works if the stream is flat (or we are not flattening) and
    sorts have already been run, and we are not making an OffsetTree.

    Returns the same outputTree that was put in, only with elements in it.
