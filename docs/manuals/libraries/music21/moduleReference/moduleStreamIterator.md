Source: https://music21.org/music21docs/moduleReference/moduleStreamIterator.html

# music21.stream.iterator

this class contains iterators and filters for walking through streams

StreamIterators are explicitly allowed to access private methods on streams.

## StreamIterator

class music21.stream.iterator.StreamIterator(*srcStream: StreamType*, *\**, *filterList: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [StreamFilter](moduleStreamFilters.html#music21.stream.filters.StreamFilter "music21.stream.filters.StreamFilter")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *restoreActiveSites: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *activeInformation: [ActiveInformation](#music21.stream.iterator.ActiveInformation "music21.stream.iterator.ActiveInformation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *ignoreSorting: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/stream/iterator.html#StreamIterator)
:   An Iterator object used to handle getting items from Streams.
    The `__iter__()` method
    returns this object, passing a reference to self.

    Note that this iterator automatically sets the active site of
    returned elements to the source Stream.

    There is one property to know about: .overrideDerivation which overrides the set
    derivation of the class when .stream() is called

    Sets:

    * StreamIterator.srcStream – the Stream iterated over
    * StreamIterator.elementIndex – current index item
    * StreamIterator.streamLength – length of elements.
    * StreamIterator.srcStreamElements – srcStream.\_elements
    * StreamIterator.activeInformation – a dict that contains information
      about where we are in the parse. Especially useful for recursive
      streams:

      > + stream = the stream that is currently active,
      > + elementIndex = where in .elements we are,
      > + iterSection is \_elements or \_endElements,
      > + sectionIndex is where we are in the iterSection, or -1 if
      >   we have not started.
      > + lastYielded the element that was last returned by the iterator.
      >   (for OffsetIterators, contains the first element last returned)
      > + (This dict is shared among all sub iterators.)

    Constructor keyword-only arguments:

    * filterList is a list of stream.filters.Filter objects to apply
    * if restoreActiveSites is True (default), then on iterating, the activeSite is set
      to the Stream being iterated over.
    * if ignoreSorting is True (default is False) then the Stream is not sorted before
      iterating. If the Stream is already sorted, then this value does not matter, and
      no time will be saved by setting to False.
    * For activeInformation see above.
    * Changed in v5.2: all arguments except srcStream are keyword only.
    * Changed in v8:
      - filterList must be a list or None, not a single filter.
      - StreamIterator inherits from typing.Sequence, hence index
      was moved to elementIndex.
    * Changed in v9: cleanupOnStop is deprecated. Was not working properly before: noone noticed.
    * Changed in v10: remove cleanupOnStop.

[`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator") read-only properties

StreamIterator.activeElementList
:   Returns the element list (\_elements or \_endElements)
    for the current activeInformation.

StreamIterator.notes
:   Returns all [`NotRest`](moduleNote.html#music21.note.NotRest "music21.note.NotRest") objects

    (will sometime become simply Note and Chord objects.)

    ```python
    >>> s = stream.Stream()
    >>> s.append(note.Note('C'))
    >>> s.append(note.Rest())
    >>> s.append(note.Note('D'))
    >>> for el in s.iter().notes:
    ...     print(el)
    <music21.note.Note C>
    <music21.note.Note D>
    ```

StreamIterator.notesAndRests
:   Returns all [`GeneralNote`](moduleNote.html#music21.note.GeneralNote "music21.note.GeneralNote") objects, including
    Rests and Unpitched elements.

    ```python
    >>> s = stream.Stream()
    >>> s.append(meter.TimeSignature('4/4'))
    >>> s.append(note.Note('C'))
    >>> s.append(note.Rest())
    >>> s.append(note.Note('D'))
    >>> for el in s.iter().notesAndRests:
    ...     print(el)
    <music21.note.Note C>
    <music21.note.Rest quarter>
    <music21.note.Note D>
    ```

    Chained filters (this makes no sense since notes is a subset of notesAndRests):

    ```python
    >>> for el in s.iter().notesAndRests.notes:
    ...     print(el)
    <music21.note.Note C>
    <music21.note.Note D>
    ```

StreamIterator.parts
:   Adds a ClassFilter for Part objects

StreamIterator.spanners
:   Adds a ClassFilter for Spanner objects

StreamIterator.voices
:   Adds a ClassFilter for Voice objects

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator") methods

StreamIterator.\_\_getitem\_\_(*k: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → M21ObjType[[source]](../_modules/music21/stream/iterator.html#StreamIterator.__getitem__)

StreamIterator.\_\_getitem\_\_(*k: [slice](https://docs.python.org/3/library/functions.html#slice "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[M21ObjType]

StreamIterator.\_\_getitem\_\_(*k: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → M21ObjType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
:   Iterators can request other items by index or slice.

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, note.Note('F#'))
    >>> s.repeatAppend(note.Note('C'), 2)
    >>> sI = s.iter()
    >>> sI
    <music21.stream.iterator.StreamIterator for Stream:0x104743be0 @:0>
    ```

    ```python
    >>> sI.srcStream is s
    True
    ```

    ```python
    >>> for n in sI:
    ...    printer = (repr(n), repr(sI[0]))
    ...    print(printer)
    ('<music21.note.Note F#>', '<music21.note.Note F#>')
    ('<music21.note.Note C>', '<music21.note.Note F#>')
    ('<music21.note.Note C>', '<music21.note.Note F#>')
    >>> sI.srcStream is s
    True
    ```

    To request an element by id, put a ‘#’ sign in front of the id,
    like in HTML DOM queries:

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> soprano = bach.recurse()['#Soprano']
    >>> soprano
    <music21.stream.Part Soprano>
    ```

    This behavior is often used to get an element from the Parts iterator:

    ```python
    >>> bach.parts['#soprano']  # notice: case-insensitive retrieval
    <music21.stream.Part Soprano>
    ```

    Slices work:

    ```python
    >>> nSlice = sI[1:]
    >>> for n in nSlice:
    ...     print(n)
    <music21.note.Note C>
    <music21.note.Note C>
    ```

    Filters, such as “notes” apply.

    ```python
    >>> s.insert(0, clef.TrebleClef())
    >>> s[0]
    <music21.clef.TrebleClef>
    >>> s.iter().notes[0]
    <music21.note.Note F#>
    ```

    * Changed in v8: for strings: prepend a ‘#’ sign to get elements by id.
      The old behavior still works until v9.
      This is an attempt to unify \_\_getitem\_\_ behavior in
      StreamIterators and Streams.

StreamIterator.addFilter(*newFilter*, *\**, *returnClone=True*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.addFilter)
:   Return a new StreamIterator with an additional filter.
    Also resets caches – so do not add filters any other way.

    If returnClone is False then adds without creating a new StreamIterator

    * Changed in v6: Encourage creating new StreamIterators: change
      default to return a new StreamIterator.

StreamIterator.cleanup() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.cleanup)
:   stop iteration; and cleanup if need be. Can be subclassed. does nothing.

StreamIterator.clone() → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.clone)
:   Returns a new copy of the same iterator.
    (a shallow copy of some things except activeInformation)

StreamIterator.first() → M21ObjType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.first)
:   Efficiently return the first matching element, or None if no
    elements match.

    Does not require creating the whole list of matching elements.

    ```python
    >>> s = converter.parse('tinyNotation: 3/4 D4 E2 F4 r2 G2 r4')
    >>> s.recurse().notes.first()
    <music21.note.Note D>
    >>> s[note.Rest].first()
    <music21.note.Rest half>
    ```

    If no elements match, returns None:

    ```python
    >>> print(s[chord.Chord].first())
    None
    ```

    * New in v7.

StreamIterator.getElementById(*elementId: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → M21ObjType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.getElementById)
:   Returns a single element (or None) that matches elementId.

    If chaining filters, this should be the last one, as it returns an element

    ```python
    >>> s = stream.Stream(id='s1')
    >>> s.append(note.Note('C'))
    >>> r = note.Rest()
    >>> r.id = 'restId'
    >>> s.append(r)
    >>> r2 = s.recurse().getElementById('restId')
    >>> r2 is r
    True
    >>> r2.id
    'restId'
    ```

StreamIterator.getElementsByClass(*classFilterList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [StreamIterator](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[M21ObjType][[source]](../_modules/music21/stream/iterator.html#StreamIterator.getElementsByClass)

StreamIterator.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [StreamIterator](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[M21ObjType]

StreamIterator.getElementsByClass(*classFilterList: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[ChangedM21ObjType]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [StreamIterator](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[ChangedM21ObjType]

StreamIterator.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [StreamIterator](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")[M21ObjType]
:   Add a filter to the Iterator to remove all elements
    except those that match one
    or more classes in the classFilterList. A single class
    can also be used for the classFilterList parameter instead of a List.

    ```python
    >>> s = stream.Stream(id='s1')
    >>> s.append(note.Note('C'))
    >>> r = note.Rest()
    >>> s.append(r)
    >>> s.append(note.Note('D'))
    >>> for el in s.iter().getElementsByClass(note.Rest):
    ...     print(el)
    <music21.note.Rest quarter>
    ```

    ActiveSite is restored.

    ```python
    >>> s2 = stream.Stream(id='s2')
    >>> s2.insert(0, r)
    >>> r.activeSite.id
    's2'
    ```

    ```python
    >>> for el in s.iter().getElementsByClass(note.Rest):
    ...     print(el.activeSite.id)
    s1
    ```

    Strings work in addition to classes, but your IDE will not know that
    el is a [`Rest`](moduleNote.html#music21.note.Rest "music21.note.Rest") object.

    ```python
    >>> for el in s.iter().getElementsByClass('Rest'):
    ...     print(el)
    <music21.note.Rest quarter>
    ```

StreamIterator.getElementsByGroup(*groupFilterList*, *\**, *returnClone=True*)[[source]](../_modules/music21/stream/iterator.html#StreamIterator.getElementsByGroup)
:   ```python
    >>> n1 = note.Note('C')
    >>> n1.groups.append('trombone')
    >>> n2 = note.Note('D')
    >>> n2.groups.append('trombone')
    >>> n2.groups.append('tuba')
    >>> n3 = note.Note('E')
    >>> n3.groups.append('tuba')
    >>> s1 = stream.Stream()
    >>> s1.append(n1)
    >>> s1.append(n2)
    >>> s1.append(n3)
    ```

    ```python
    >>> tboneSubStream = s1.iter().getElementsByGroup('trombone')
    >>> for thisNote in tboneSubStream:
    ...     print(thisNote.name)
    C
    D
    >>> tubaSubStream = s1.iter().getElementsByGroup('tuba')
    >>> for thisNote in tubaSubStream:
    ...     print(thisNote.name)
    D
    E
    ```

StreamIterator.getElementsByOffset(*offsetStart*, *offsetEnd=None*, *\**, *includeEndBoundary=True*, *mustFinishInSpan=False*, *mustBeginInSpan=True*, *includeElementsThatEndAtStart=True*, *stopAfterEnd=True*, *returnClone=True*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.getElementsByOffset)
:   Adds a filter keeping only Music21Objects that
    are found at a certain offset or within a certain
    offset time range (given the start and optional stop values).

    There are several attributes that govern how this range is
    determined:

    If mustFinishInSpan is True then an event that begins
    between offsetStart and offsetEnd but which ends after offsetEnd
    will not be included. The default is False.

    For instance, a half note at offset 2.0 will be found in
    getElementsByOffset(1.5, 2.5) or getElementsByOffset(1.5, 2.5,
    mustFinishInSpan = False) but not by getElementsByOffset(1.5, 2.5,
    mustFinishInSpan = True).

    The includeEndBoundary option determines if an element
    begun just at the offsetEnd should be included. For instance,
    the half note at offset 2.0 above would be found by
    getElementsByOffset(0, 2.0) or by getElementsByOffset(0, 2.0,
    includeEndBoundary = True) but not by getElementsByOffset(0, 2.0,
    includeEndBoundary = False).

    Setting includeEndBoundary to False at the same time as
    mustFinishInSpan is set to True is probably NOT what you want to do
    unless you want to find things like clefs at the end of the region
    to display as courtesy clefs.

    The mustBeginInSpan option determines whether notes or other
    objects that do not begin in the region but are still sounding
    at the beginning of the region are excluded. The default is
    True – that is, these notes will not be included.
    For instance the half note at offset 2.0 from above would not be found by
    getElementsByOffset(3.0, 3.5) or getElementsByOffset(3.0, 3.5,
    mustBeginInSpan = True) but it would be found by
    getElementsByOffset(3.0, 3.5, mustBeginInSpan = False)

    Setting includeElementsThatEndAtStart to False is useful for zeroLength
    searches that set mustBeginInSpan == False to not catch notes that were
    playing before the search but that end just before the end of the search type.
    See the code for allPlayingWhileSounding for a demonstration.

    This chart, like the examples below, demonstrates the various
    features of getElementsByOffset. It is one of the most complex
    methods of music21 but also one of the most powerful, so it
    is worth learning at least the basics.

    > [![../_images/getElementsByOffset.png](../_images/getElementsByOffset.png)](../_images/getElementsByOffset.png)

    ```python
    >>> st1 = stream.Stream()
    >>> n0 = note.Note('C')
    >>> n0.duration.type = 'half'
    >>> n0.offset = 0
    >>> st1.insert(n0)
    >>> n2 = note.Note('D')
    >>> n2.duration.type = 'half'
    >>> n2.offset = 2
    >>> st1.insert(n2)
    >>> out1 = list(st1.iter().getElementsByOffset(2))
    >>> len(out1)
    1
    >>> out1[0].step
    'D'
    >>> out2 = list(st1.iter().getElementsByOffset(1, 3))
    >>> len(out2)
    1
    >>> out2[0].step
    'D'
    >>> out3 = list(st1.iter().getElementsByOffset(1, 3, mustFinishInSpan=True))
    >>> len(out3)
    0
    >>> out4 = list(st1.iter().getElementsByOffset(1, 2))
    >>> len(out4)
    1
    >>> out4[0].step
    'D'
    >>> out5 = list(st1.iter().getElementsByOffset(1, 2, includeEndBoundary=False))
    >>> len(out5)
    0
    >>> out6 = list(st1.iter().getElementsByOffset(1, 2, includeEndBoundary=False,
    ...                                          mustBeginInSpan=False))
    >>> len(out6)
    1
    >>> out6[0].step
    'C'
    >>> out7 = list(st1.iter().getElementsByOffset(1, 3, mustBeginInSpan=False))
    >>> len(out7)
    2
    >>> [el.step for el in out7]
    ['C', 'D']
    ```

    Note, that elements that end at the start offset are included if mustBeginInSpan is False

    ```python
    >>> out8 = list(st1.iter().getElementsByOffset(2, 4, mustBeginInSpan=False))
    >>> len(out8)
    2
    >>> [el.step for el in out8]
    ['C', 'D']
    ```

    To change this behavior set includeElementsThatEndAtStart=False

    ```python
    >>> out9 = list(st1.iter().getElementsByOffset(2, 4, mustBeginInSpan=False,
    ...                                          includeElementsThatEndAtStart=False))
    >>> len(out9)
    1
    >>> [el.step for el in out9]
    ['D']
    ```

    ```python
    >>> a = stream.Stream(id='a')
    >>> n = note.Note('G')
    >>> n.quarterLength = 0.5
    >>> a.repeatInsert(n, list(range(8)))
    >>> b = stream.Stream(id='b')
    >>> b.repeatInsert(a, [0, 3, 6])
    >>> c = list(b.iter().getElementsByOffset(2, 6.9))
    >>> len(c)
    2
    >>> c = list(b.flatten().iter().getElementsByOffset(2, 6.9))
    >>> len(c)
    10
    ```

    Testing multiple zero-length elements with mustBeginInSpan:

    ```python
    >>> c = clef.TrebleClef()
    >>> ts = meter.TimeSignature('4/4')
    >>> ks = key.KeySignature(2)
    >>> s = stream.Stream()
    >>> s.insert(0.0, c)
    >>> s.insert(0.0, ts)
    >>> s.insert(0.0, ks)
    >>> len(list(s.iter().getElementsByOffset(0.0, mustBeginInSpan=True)))
    3
    >>> len(list(s.iter().getElementsByOffset(0.0, mustBeginInSpan=False)))
    3
    ```

    On a [`RecursiveIterator`](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator"),
    .getElementsByOffset(0.0), will get everything
    at the start of the piece, which is useful:

    ```python
    >>> bwv66 = corpus.parse('bwv66.6')
    >>> list(bwv66.recurse().getElementsByOffset(0.0))
    [<music21.metadata.Metadata object at 0x10a32f490>,
     <music21.stream.Part Soprano>,
     <music21.instrument.Instrument 'P1: Soprano: Instrument 1'>,
     <music21.stream.Measure 0 offset=0.0>,
     <music21.clef.TrebleClef>,
     <music21.tempo.MetronomeMark Quarter=96 (playback only)>,
     <music21.key.Key of f# minor>,
     <music21.meter.TimeSignature 4/4>,
     <music21.note.Note C#>,
     <music21.stream.Part Alto>,
     ...
     <music21.note.Note E>,
     <music21.stream.Part Tenor>,
     ...]
    ```

    However, any other offset passed to getElementsByOffset on a
    RecursiveIterator without additional arguments, is unlikely to be useful,
    because the iterator ends as soon as it encounters an element
    with an offset beyond the offsetEnd point. For instance,
    calling .getElementsByOffset(1.0).notes on a `Part`,
    in bwv66.6 only gets the note that appears at offset 1.0 of a measure that begins
    or includes offset 1.0.
    (Fortunately, this piece begins with a one-beat pickup, so there is such a note):

    ```python
    >>> soprano = bwv66.parts['#Soprano']  # = getElementById('Soprano')
    >>> for el in soprano.recurse().getElementsByOffset(1.0):
    ...     print(el, el.offset, el.getOffsetInHierarchy(bwv66), el.activeSite)
    <music21.stream.Measure 1 offset=1.0> 1.0 1.0 <music21.stream.Part Soprano>
    <music21.note.Note B> 1.0 2.0 <music21.stream.Measure 1 offset=1.0>
    ```

    RecursiveIterators will probably want to use
    [`getElementsByOffsetInHierarchy()`](#music21.stream.iterator.RecursiveIterator.getElementsByOffsetInHierarchy "music21.stream.iterator.RecursiveIterator.getElementsByOffsetInHierarchy")
    instead. Or to get all elements with a particular local offset, such as everything
    on the third quarter note of a measure, use the stopAfterEnd=False keyword,
    which lets the iteration continue to search for elements even after encountering
    some within Streams whose offsets are greater than the end element.

    ```python
    >>> len(soprano.recurse().getElementsByOffset(2.0, stopAfterEnd=False))
    9
    ```

    * Changed in v5.5: all arguments changing behavior are keyword only.
    * New in v6.5: stopAfterEnd keyword.

StreamIterator.getElementsByQuerySelector(*querySelector: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *returnClone=True*)[[source]](../_modules/music21/stream/iterator.html#StreamIterator.getElementsByQuerySelector)
:   First implementation of a query selector, similar to CSS QuerySelectors used in
    HTML DOM:

    * A leading # indicates the id of an element, so ‘#hello’ will find elements
      with el.id==’hello’ (should only be one)
    * A leading . indicates the group of an element, so ‘.high’ will find elements
      with ‘high’ in el.groups.
    * Any other string is considered to be the type/class of the element. So Note
      will find all Note elements. Can be fully qualified like music21.note.Note
      or partially qualified like note.Note.

    Eventually, more complex query selectors will be implemented. This is just a start.

    Setting up an example:

    ```python
    >>> s = converter.parse('tinyNotation: 4/4 GG4 AA4 BB4 r4 C4 D4 E4 F4 r1')
    >>> s[note.Note].last().id = 'last'
    >>> for n in s[note.Note]:
    ...     if n.octave == 3:
    ...         n.groups.append('tenor')
    ```

    ```python
    >>> list(s.recurse().getElementsByQuerySelector('.tenor'))
    [<music21.note.Note C>,
     <music21.note.Note D>,
     <music21.note.Note E>,
     <music21.note.Note F>]
    ```

    ```python
    >>> list(s.recurse().getElementsByQuerySelector('Rest'))
    [<music21.note.Rest quarter>,
     <music21.note.Rest whole>]
    ```

    Note that unlike with stream slices, the querySelector does not do anything special
    for id searches. .first() will need to be called to find the element (if any)

    ```python
    >>> s.recurse().getElementsByQuerySelector('#last').first()
    <music21.note.Note F>
    ```

    * New in v7.

StreamIterator.getElementsNotOfClass(*classFilterList*, *\**, *returnClone=True*)[[source]](../_modules/music21/stream/iterator.html#StreamIterator.getElementsNotOfClass)
:   Adds a filter, removing all Elements that do not
    match the one or more classes in the classFilterList.

    In lieu of a list, a single class can be used as the classFilterList parameter.

    ```python
    >>> a = stream.Stream()
    >>> a.repeatInsert(note.Rest(), range(10))
    >>> for x in range(4):
    ...     n = note.Note('G#')
    ...     n.offset = x * 3
    ...     a.insert(n)
    >>> found = a.iter().getElementsNotOfClass(note.Note)
    >>> len(found)
    10
    >>> found = a.iter().getElementsNotOfClass('Rest')
    >>> len(found)
    4
    >>> found = a.iter().getElementsNotOfClass(['Note', 'Rest'])
    >>> len(found)
    0
    ```

    ```python
    >>> b = stream.Stream()
    >>> b.repeatInsert(note.Rest(), range(15))
    >>> a.insert(b)
    ```

    ```python
    >>> found = a.recurse().getElementsNotOfClass([note.Rest, 'Stream'])
    >>> len(found)
    4
    >>> found = a.recurse().getElementsNotOfClass([note.Note, 'Stream'])
    >>> len(found)
    25
    ```

StreamIterator.last() → M21ObjType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.last)
:   Returns the last matching element, or None if no elements match.

    Currently is not efficient (does not iterate backwards, for instance),
    but easier than checking for an IndexError. Might be refactored later
    to iterate the stream backwards instead if it gets a lot of use.

    ```python
    >>> s = converter.parse('tinyNotation: 3/4 D4 E2 F4 r2 G2 r4')
    >>> s.recurse().notes.last()
    <music21.note.Note G>
    >>> s[note.Rest].last()
    <music21.note.Rest quarter>
    ```

    * New in v7.

StreamIterator.matchesFilters(*e: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.matchesFilters)
:   returns False if any filter returns False, True otherwise.

StreamIterator.matchingElements(*\**, *restoreActiveSites: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[M21ObjType][[source]](../_modules/music21/stream/iterator.html#StreamIterator.matchingElements)
:   Returns a list of elements that match the filter.

    This sort of defeats the point of using a generator, so only used if
    it’s requested by \_\_len\_\_ or \_\_getitem\_\_ etc.

    Subclasses should override to cache anything they need saved (index,
    recursion objects, etc.)

    activeSite will not be set.

    Cached for speed.

    ```python
    >>> s = converter.parse('tinynotation: 3/4 c4 d e f g a', makeNotation=False)
    >>> s.id = 'tn3/4'
    >>> sI = s.iter()
    >>> sI
    <music21.stream.iterator.StreamIterator for Part:tn3/4 @:0>
    ```

    ```python
    >>> sI.matchingElements()
    [<music21.meter.TimeSignature 3/4>, <music21.note.Note C>, <music21.note.Note D>,
     <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>,
     <music21.note.Note A>]
    ```

    ```python
    >>> sI_notes = sI.notes
    >>> sI_notes
    <music21.stream.iterator.StreamIterator for Part:tn3/4 @:0>
    ```

    Adding a filter to the Stream iterator returns a new Stream iterator; it
    does not change the original.

    ```python
    >>> sI_notes is sI
    False
    ```

    ```python
    >>> sI.filters
    []
    ```

    ```python
    >>> sI_notes.filters
    [<music21.stream.filters.ClassFilter <class 'music21.note.NotRest'>>]
    ```

    ```python
    >>> sI_notes.matchingElements()
    [<music21.note.Note C>, <music21.note.Note D>,
     <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>,
     <music21.note.Note A>]
    ```

    If restoreActiveSites is False then the elements will not have
    their activeSites changed (callers should use it when they do not plan to actually
    expose the elements to users, such as in \_\_len\_\_). By default, it is None
    which means to take from the iterator’s restoreActiveSites attribute.

    A demonstration of restoreActiveSites = False. First we create a second stream
    from the first, so that all elements are in two streams, then we’ll check the
    id of iterating through the second stream normally, and then the first stream
    with restoreActiveSites=False, and then the first stream without the restoreActiveSites:

    ```python
    >>> s2 = stream.Part()
    >>> s2.id = 'second'
    >>> s2.elements = s
    >>> {e.activeSite.id for e in s2.iter().notes.matchingElements()}
    {'second'}
    >>> {e.activeSite.id for e in sI_notes.matchingElements(restoreActiveSites=False)}
    {'second'}
    >>> {e.activeSite.id for e in sI_notes.matchingElements()}
    {'tn3/4'}
    ```

    * New in v7: restoreActiveSites
    * Changed in v9.3: restoreActiveSites allows None which takes from the iterator’s
      restoreActiveSites attribute.

StreamIterator.removeFilter(*oldFilter*, *\**, *returnClone=True*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.removeFilter)
:   Return a new StreamIterator where oldFilter is removed.

StreamIterator.reset() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.reset)
:   reset prior to iteration

StreamIterator.resetCaches() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.resetCaches)
:   reset any cached data. – do not use this at
    the start of iteration since we might as well
    save this information. But do call it if
    the filter changes.

StreamIterator.stream(*returnStreamSubClass: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]*) → streamModule.Stream[[source]](../_modules/music21/stream/iterator.html#StreamIterator.stream)

StreamIterator.stream(*returnStreamSubClass: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True] = True*) → StreamType
:   return a new stream from this iterator.

    Does nothing except copy if there are no filters, but a drop in
    replacement for the old .getElementsByClass() etc. if it does.

    In other words:

    s.getElementsByClass() == s.iter().getElementsByClass().stream()

    ```python
    >>> s = stream.Part()
    >>> s.insert(0, note.Note('C'))
    >>> s.append(note.Rest())
    >>> s.append(note.Note('D'))
    >>> b = bar.Barline()
    >>> s.storeAtEnd(b)
    ```

    ```python
    >>> s2 = s.iter().getElementsByClass(note.Note).stream()
    >>> s2.show('t')
    {0.0} <music21.note.Note C>
    {2.0} <music21.note.Note D>
    >>> s2.derivation.method
    'getElementsByClass'
    >>> s2
    <music21.stream.Part ...>
    ```

    ```python
    >>> s3 = s.iter().stream()
    >>> s3.show('t')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Rest quarter>
    {2.0} <music21.note.Note D>
    {3.0} <music21.bar.Barline type=regular>
    ```

    ```python
    >>> s3.elementOffset(b, returnSpecial=True)
    <OffsetSpecial.AT_END>
    ```

    ```python
    >>> s4 = s.iter().getElementsByClass(bar.Barline).stream()
    >>> s4.show('t')
    {0.0} <music21.bar.Barline type=regular>
    ```

    Note that this routine can create Streams that have elements that the original
    stream did not, in the case of recursion:

    ```python
    >>> bach = corpus.parse('bwv66.6')
    >>> bn = bach.flatten()[34]
    >>> bn
    <music21.note.Note E>
    ```

    ```python
    >>> bn in bach
    False
    >>> bfn = bach.recurse().notes.stream()
    >>> bn in bfn
    True
    >>> bn.getOffsetBySite(bfn)
    2.0
    >>> bn.getOffsetInHierarchy(bach)
    2.0
    ```

StreamIterator.updateActiveInformation() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#StreamIterator.updateActiveInformation)
:   Updates the (shared) activeInformation dictionary
    with information about where we are.

    Call before any element return.

## RecursiveIterator

class music21.stream.iterator.RecursiveIterator(*srcStream*, *\**, *filterList=None*, *restoreActiveSites=True*, *activeInformation=None*, *streamsOnly=False*, *includeSelf=False*, *ignoreSorting=False*)[[source]](../_modules/music21/stream/iterator.html#RecursiveIterator)
:   One of the most powerful iterators in music21. Generally not called
    directly, but created by being invoked on a stream with Stream.recurse()

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> ri = stream.iterator.RecursiveIterator(b, streamsOnly=True)
    >>> for x in ri:
    ...     print(x)
    <music21.stream.Part Soprano>
    <music21.stream.Measure 0 offset=0.0>
    <music21.stream.Measure 1 offset=1.0>
    <music21.stream.Measure 2 offset=5.0>
    ...
    <music21.stream.Part Alto>
    <music21.stream.Measure 0 offset=0.0>
    ...
    <music21.stream.Part Tenor>
    ...
    <music21.stream.Part Bass>
    ...
    ```

    But this is how you’ll actually use it:

    ```python
    >>> for x in b.recurse(streamsOnly=True, includeSelf=True):
    ...     print(x)
    <music21.stream.Score bach/bwv66.6.mxl>
    <music21.stream.Part Soprano>
    <music21.stream.Measure 0 offset=0.0>
    <music21.stream.Measure 1 offset=1.0>
    <music21.stream.Measure 2 offset=5.0>
    ...
    <music21.stream.Part Alto>
    <music21.stream.Measure 0 offset=0.0>
    ...
    <music21.stream.Part Tenor>
    ...
    <music21.stream.Part Bass>
    ...
    ```

    ```python
    >>> hasExpressions = lambda el, i: True if (hasattr(el, 'expressions')
    ...       and el.expressions) else False
    >>> expressive = b.recurse().addFilter(hasExpressions)
    >>> expressive
    <music21.stream.iterator.RecursiveIterator for Score:bach/bwv66.6.mxl @:0>
    ```

    ```python
    >>> for el in expressive:
    ...     print(el, el.expressions)
    <music21.note.Note C#> [<music21.expressions.Fermata>]
    <music21.note.Note A> [<music21.expressions.Fermata>]
    <music21.note.Note F#> [<music21.expressions.Fermata>]
    <music21.note.Note C#> [<music21.expressions.Fermata>]
    <music21.note.Note G#> [<music21.expressions.Fermata>]
    <music21.note.Note F#> [<music21.expressions.Fermata>]
    ```

    ```python
    >>> len(expressive)
    6
    >>> expressive[-1].measureNumber
    9
    >>> bool(expressive)
    True
    ```

[`RecursiveIterator`](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator") bases

* [`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RecursiveIterator`](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator") read-only properties

Read-only properties inherited from [`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator"):

|  |  |  |
| --- | --- | --- |
| * [`activeElementList`](#music21.stream.iterator.StreamIterator.activeElementList "music21.stream.iterator.StreamIterator.activeElementList") * [`notes`](#music21.stream.iterator.StreamIterator.notes "music21.stream.iterator.StreamIterator.notes") | * [`notesAndRests`](#music21.stream.iterator.StreamIterator.notesAndRests "music21.stream.iterator.StreamIterator.notesAndRests") * [`parts`](#music21.stream.iterator.StreamIterator.parts "music21.stream.iterator.StreamIterator.parts") | * [`spanners`](#music21.stream.iterator.StreamIterator.spanners "music21.stream.iterator.StreamIterator.spanners") * [`voices`](#music21.stream.iterator.StreamIterator.voices "music21.stream.iterator.StreamIterator.voices") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RecursiveIterator`](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator") methods

RecursiveIterator.currentHierarchyOffset()[[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.currentHierarchyOffset)
:   Called on the current iterator, returns the current offset in the hierarchy.
    Or None if we are not currently iterating.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> bRecurse = b.recurse().notes
    >>> print(bRecurse.currentHierarchyOffset())
    None
    >>> for n in bRecurse:
    ...     print(n.measureNumber, bRecurse.currentHierarchyOffset(), n)
    0 0.0 <music21.note.Note C#>
    0 0.5 <music21.note.Note B>
    1 1.0 <music21.note.Note A>
    1 2.0 <music21.note.Note B>
    1 3.0 <music21.note.Note C#>
    1 4.0 <music21.note.Note E>
    2 5.0 <music21.note.Note C#>
    ...
    9 34.5 <music21.note.Note E#>
    9 35.0 <music21.note.Note F#>
    0 0.0 <music21.note.Note E>
    1 1.0 <music21.note.Note F#>
    ...
    ```

    After iteration completes, the figure is reset to None:

    ```python
    >>> print(bRecurse.currentHierarchyOffset())
    None
    ```

    The offsets are with respect to the position inside the stream
    being iterated, so, for instance, this will not change the output from above:

    ```python
    >>> o = stream.Opus()
    >>> o.insert(20.0, b)
    >>> bRecurse = b.recurse().notes
    >>> for n in bRecurse:
    ...     print(n.measureNumber, bRecurse.currentHierarchyOffset(), n)
    0 0.0 <music21.note.Note C#>
    ...
    ```

    But of course, this will add 20.0 to all numbers:

    ```python
    >>> oRecurse = o.recurse().notes
    >>> for n in oRecurse:
    ...     print(n.measureNumber, oRecurse.currentHierarchyOffset(), n)
    0 20.0 <music21.note.Note C#>
    ...
    ```

    * New in v4.

RecursiveIterator.getElementsByClass(*classFilterList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [RecursiveIterator](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType][[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.getElementsByClass)

RecursiveIterator.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [RecursiveIterator](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType]

RecursiveIterator.getElementsByClass(*classFilterList: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[ChangedM21ObjType]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [RecursiveIterator](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[ChangedM21ObjType]

RecursiveIterator.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [RecursiveIterator](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")[M21ObjType]
:   Add a filter to the Iterator to remove all elements
    except those that match one
    or more classes in the classFilterList. A single class
    can also be used for the classFilterList parameter instead of a List.

    ```python
    >>> s = stream.Stream(id='s1')
    >>> s.append(note.Note('C'))
    >>> r = note.Rest()
    >>> s.append(r)
    >>> s.append(note.Note('D'))
    >>> for el in s.iter().getElementsByClass(note.Rest):
    ...     print(el)
    <music21.note.Rest quarter>
    ```

    ActiveSite is restored.

    ```python
    >>> s2 = stream.Stream(id='s2')
    >>> s2.insert(0, r)
    >>> r.activeSite.id
    's2'
    ```

    ```python
    >>> for el in s.iter().getElementsByClass(note.Rest):
    ...     print(el.activeSite.id)
    s1
    ```

    Strings work in addition to classes, but your IDE will not know that
    el is a [`Rest`](moduleNote.html#music21.note.Rest "music21.note.Rest") object.

    ```python
    >>> for el in s.iter().getElementsByClass('Rest'):
    ...     print(el)
    <music21.note.Rest quarter>
    ```

RecursiveIterator.getElementsByOffsetInHierarchy(*offsetStart*, *offsetEnd=None*, *\**, *includeEndBoundary=True*, *mustFinishInSpan=False*, *mustBeginInSpan=True*, *includeElementsThatEndAtStart=True*) → [Self](https://docs.python.org/3/library/typing.html#typing.Self "(in Python v3.14)")[[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.getElementsByOffsetInHierarchy)
:   Adds a filter keeping only Music21Objects that
    are found at a certain offset or within a certain
    offset time range (given the offsetStart and optional offsetEnd values) from
    the beginning of the hierarchy.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> for n in b.recurse().getElementsByOffsetInHierarchy(8, 9.5).notes:
    ...     print(n,
    ...           n.getOffsetInHierarchy(b),
    ...           n.measureNumber,
    ...           n.getContextByClass(stream.Part).id)
    <music21.note.Note C#> 8.0 2 Soprano
    <music21.note.Note A> 9.0 3 Soprano
    <music21.note.Note B> 9.5 3 Soprano
    <music21.note.Note G#> 8.0 2 Alto
    <music21.note.Note F#> 9.0 3 Alto
    <music21.note.Note G#> 9.5 3 Alto
    <music21.note.Note C#> 8.0 2 Tenor
    <music21.note.Note C#> 9.0 3 Tenor
    <music21.note.Note D> 9.5 3 Tenor
    <music21.note.Note E#> 8.0 2 Bass
    <music21.note.Note F#> 9.0 3 Bass
    <music21.note.Note B> 9.5 3 Bass
    ```

    * Changed in v5.5: all behavior-changing options are keyword only.

RecursiveIterator.iteratorStack() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[RecursiveIterator](#music21.stream.iterator.RecursiveIterator "music21.stream.iterator.RecursiveIterator")][[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.iteratorStack)
:   Returns a stack of RecursiveIterators at this point in the iteration. Last is most recent.

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> bRecurse = b.recurse()
    >>> i = 0
    >>> for _ in bRecurse:
    ...     i += 1
    ...     if i > 13:
    ...         break
    >>> bRecurse.iteratorStack()
    [<music21.stream.iterator.RecursiveIterator for Score:bach/bwv66.6.mxl @:2>,
     <music21.stream.iterator.RecursiveIterator for Part:Soprano @:3>,
     <music21.stream.iterator.RecursiveIterator for Measure:m.1 @:3>]
    ```

RecursiveIterator.matchingElements(*\**, *restoreActiveSites=True*)[[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.matchingElements)
:   Returns a list of elements that match the filter.

    This sort of defeats the point of using a generator, so only used if
    it’s requested by \_\_len\_\_ or \_\_getitem\_\_ etc.

    Subclasses should override to cache anything they need saved (index,
    recursion objects, etc.)

    activeSite will not be set.

    Cached for speed.

    ```python
    >>> s = converter.parse('tinynotation: 3/4 c4 d e f g a', makeNotation=False)
    >>> s.id = 'tn3/4'
    >>> sI = s.iter()
    >>> sI
    <music21.stream.iterator.StreamIterator for Part:tn3/4 @:0>
    ```

    ```python
    >>> sI.matchingElements()
    [<music21.meter.TimeSignature 3/4>, <music21.note.Note C>, <music21.note.Note D>,
     <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>,
     <music21.note.Note A>]
    ```

    ```python
    >>> sI_notes = sI.notes
    >>> sI_notes
    <music21.stream.iterator.StreamIterator for Part:tn3/4 @:0>
    ```

    Adding a filter to the Stream iterator returns a new Stream iterator; it
    does not change the original.

    ```python
    >>> sI_notes is sI
    False
    ```

    ```python
    >>> sI.filters
    []
    ```

    ```python
    >>> sI_notes.filters
    [<music21.stream.filters.ClassFilter <class 'music21.note.NotRest'>>]
    ```

    ```python
    >>> sI_notes.matchingElements()
    [<music21.note.Note C>, <music21.note.Note D>,
     <music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>,
     <music21.note.Note A>]
    ```

    If restoreActiveSites is False then the elements will not have
    their activeSites changed (callers should use it when they do not plan to actually
    expose the elements to users, such as in \_\_len\_\_). By default, it is None
    which means to take from the iterator’s restoreActiveSites attribute.

    A demonstration of restoreActiveSites = False. First we create a second stream
    from the first, so that all elements are in two streams, then we’ll check the
    id of iterating through the second stream normally, and then the first stream
    with restoreActiveSites=False, and then the first stream without the restoreActiveSites:

    ```python
    >>> s2 = stream.Part()
    >>> s2.id = 'second'
    >>> s2.elements = s
    >>> {e.activeSite.id for e in s2.iter().notes.matchingElements()}
    {'second'}
    >>> {e.activeSite.id for e in sI_notes.matchingElements(restoreActiveSites=False)}
    {'second'}
    >>> {e.activeSite.id for e in sI_notes.matchingElements()}
    {'tn3/4'}
    ```

    * New in v7: restoreActiveSites
    * Changed in v9.3: restoreActiveSites allows None which takes from the iterator’s
      restoreActiveSites attribute.

RecursiveIterator.reset()[[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.reset)
:   reset prior to iteration

RecursiveIterator.streamStack()[[source]](../_modules/music21/stream/iterator.html#RecursiveIterator.streamStack)
:   Returns a stack of Streams at this point. Last is most recent.

    However, the current element may be the same as the last element in the stack

    ```python
    >>> b = corpus.parse('bwv66.6')
    >>> bRecurse = b.recurse()
    >>> i = 0
    >>> for x in bRecurse:
    ...     i += 1
    ...     if i > 12:
    ...         break
    >>> bRecurse.streamStack()
    [<music21.stream.Score bach/bwv66.6.mxl>,
     <music21.stream.Part Soprano>,
     <music21.stream.Measure 1 offset=1.0>]
    ```

Methods inherited from [`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.stream.iterator.StreamIterator.__getitem__ "music21.stream.iterator.StreamIterator.__getitem__") * [`addFilter()`](#music21.stream.iterator.StreamIterator.addFilter "music21.stream.iterator.StreamIterator.addFilter") * [`cleanup()`](#music21.stream.iterator.StreamIterator.cleanup "music21.stream.iterator.StreamIterator.cleanup") * [`clone()`](#music21.stream.iterator.StreamIterator.clone "music21.stream.iterator.StreamIterator.clone") * [`first()`](#music21.stream.iterator.StreamIterator.first "music21.stream.iterator.StreamIterator.first") * [`getElementById()`](#music21.stream.iterator.StreamIterator.getElementById "music21.stream.iterator.StreamIterator.getElementById") | * [`getElementsByGroup()`](#music21.stream.iterator.StreamIterator.getElementsByGroup "music21.stream.iterator.StreamIterator.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.iterator.StreamIterator.getElementsByOffset "music21.stream.iterator.StreamIterator.getElementsByOffset") * [`getElementsByQuerySelector()`](#music21.stream.iterator.StreamIterator.getElementsByQuerySelector "music21.stream.iterator.StreamIterator.getElementsByQuerySelector") * [`getElementsNotOfClass()`](#music21.stream.iterator.StreamIterator.getElementsNotOfClass "music21.stream.iterator.StreamIterator.getElementsNotOfClass") * [`last()`](#music21.stream.iterator.StreamIterator.last "music21.stream.iterator.StreamIterator.last") | * [`matchesFilters()`](#music21.stream.iterator.StreamIterator.matchesFilters "music21.stream.iterator.StreamIterator.matchesFilters") * [`removeFilter()`](#music21.stream.iterator.StreamIterator.removeFilter "music21.stream.iterator.StreamIterator.removeFilter") * [`resetCaches()`](#music21.stream.iterator.StreamIterator.resetCaches "music21.stream.iterator.StreamIterator.resetCaches") * [`stream()`](#music21.stream.iterator.StreamIterator.stream "music21.stream.iterator.StreamIterator.stream") * [`updateActiveInformation()`](#music21.stream.iterator.StreamIterator.updateActiveInformation "music21.stream.iterator.StreamIterator.updateActiveInformation") |

## OffsetIterator

class music21.stream.iterator.OffsetIterator(*srcStream*, *\**, *filterList=None*, *restoreActiveSites=True*, *activeInformation=None*, *ignoreSorting=False*)[[source]](../_modules/music21/stream/iterator.html#OffsetIterator)
:   An iterator that with each iteration returns a list of elements
    that are at the same offset (or all at end)

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0, note.Note('C'))
    >>> s.insert(0, note.Note('D'))
    >>> s.insert(1, note.Note('E'))
    >>> s.insert(2, note.Note('F'))
    >>> s.insert(2, note.Note('G'))
    >>> s.storeAtEnd(bar.Repeat('end'))
    >>> s.storeAtEnd(clef.TrebleClef())
    ```

    ```python
    >>> oIter = stream.iterator.OffsetIterator(s)
    >>> for groupedElements in oIter:
    ...     print(groupedElements)
    [<music21.note.Note C>, <music21.note.Note D>]
    [<music21.note.Note E>]
    [<music21.note.Note F>, <music21.note.Note G>]
    [<music21.bar.Repeat direction=end>, <music21.clef.TrebleClef>]
    ```

    Does it work again?

    ```python
    >>> for groupedElements2 in oIter:
    ...     print(groupedElements2)
    [<music21.note.Note C>, <music21.note.Note D>]
    [<music21.note.Note E>]
    [<music21.note.Note F>, <music21.note.Note G>]
    [<music21.bar.Repeat direction=end>, <music21.clef.TrebleClef>]
    ```

    ```python
    >>> for groupedElements in oIter.notes:
    ...     print(groupedElements)
    [<music21.note.Note C>, <music21.note.Note D>]
    [<music21.note.Note E>]
    [<music21.note.Note F>, <music21.note.Note G>]
    ```

    ```python
    >>> for groupedElements in stream.iterator.OffsetIterator(s).getElementsByClass(clef.Clef):
    ...     print(groupedElements)
    [<music21.clef.TrebleClef>]
    ```

[`OffsetIterator`](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator") bases

* [`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`OffsetIterator`](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator") read-only properties

Read-only properties inherited from [`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator"):

|  |  |  |
| --- | --- | --- |
| * [`activeElementList`](#music21.stream.iterator.StreamIterator.activeElementList "music21.stream.iterator.StreamIterator.activeElementList") * [`notes`](#music21.stream.iterator.StreamIterator.notes "music21.stream.iterator.StreamIterator.notes") | * [`notesAndRests`](#music21.stream.iterator.StreamIterator.notesAndRests "music21.stream.iterator.StreamIterator.notesAndRests") * [`parts`](#music21.stream.iterator.StreamIterator.parts "music21.stream.iterator.StreamIterator.parts") | * [`spanners`](#music21.stream.iterator.StreamIterator.spanners "music21.stream.iterator.StreamIterator.spanners") * [`voices`](#music21.stream.iterator.StreamIterator.voices "music21.stream.iterator.StreamIterator.voices") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`OffsetIterator`](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator") methods

OffsetIterator.getElementsByClass(*classFilterList: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [OffsetIterator](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator")[M21ObjType][[source]](../_modules/music21/stream/iterator.html#OffsetIterator.getElementsByClass)

OffsetIterator.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [OffsetIterator](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator")[M21ObjType]

OffsetIterator.getElementsByClass(*classFilterList: [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")[ChangedM21ObjType]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [OffsetIterator](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator")[ChangedM21ObjType]

OffsetIterator.getElementsByClass(*classFilterList: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type")]*, *\**, *returnClone: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [OffsetIterator](#music21.stream.iterator.OffsetIterator "music21.stream.iterator.OffsetIterator")[M21ObjType]
:   Identical to the same method in StreamIterator, but needs to be duplicated
    for now.

OffsetIterator.reset()[[source]](../_modules/music21/stream/iterator.html#OffsetIterator.reset)
:   runs before iteration

Methods inherited from [`StreamIterator`](#music21.stream.iterator.StreamIterator "music21.stream.iterator.StreamIterator"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.stream.iterator.StreamIterator.__getitem__ "music21.stream.iterator.StreamIterator.__getitem__") * [`addFilter()`](#music21.stream.iterator.StreamIterator.addFilter "music21.stream.iterator.StreamIterator.addFilter") * [`cleanup()`](#music21.stream.iterator.StreamIterator.cleanup "music21.stream.iterator.StreamIterator.cleanup") * [`clone()`](#music21.stream.iterator.StreamIterator.clone "music21.stream.iterator.StreamIterator.clone") * [`first()`](#music21.stream.iterator.StreamIterator.first "music21.stream.iterator.StreamIterator.first") * [`getElementById()`](#music21.stream.iterator.StreamIterator.getElementById "music21.stream.iterator.StreamIterator.getElementById") | * [`getElementsByGroup()`](#music21.stream.iterator.StreamIterator.getElementsByGroup "music21.stream.iterator.StreamIterator.getElementsByGroup") * [`getElementsByOffset()`](#music21.stream.iterator.StreamIterator.getElementsByOffset "music21.stream.iterator.StreamIterator.getElementsByOffset") * [`getElementsByQuerySelector()`](#music21.stream.iterator.StreamIterator.getElementsByQuerySelector "music21.stream.iterator.StreamIterator.getElementsByQuerySelector") * [`getElementsNotOfClass()`](#music21.stream.iterator.StreamIterator.getElementsNotOfClass "music21.stream.iterator.StreamIterator.getElementsNotOfClass") * [`last()`](#music21.stream.iterator.StreamIterator.last "music21.stream.iterator.StreamIterator.last") * [`matchesFilters()`](#music21.stream.iterator.StreamIterator.matchesFilters "music21.stream.iterator.StreamIterator.matchesFilters") | * [`matchingElements()`](#music21.stream.iterator.StreamIterator.matchingElements "music21.stream.iterator.StreamIterator.matchingElements") * [`removeFilter()`](#music21.stream.iterator.StreamIterator.removeFilter "music21.stream.iterator.StreamIterator.removeFilter") * [`resetCaches()`](#music21.stream.iterator.StreamIterator.resetCaches "music21.stream.iterator.StreamIterator.resetCaches") * [`stream()`](#music21.stream.iterator.StreamIterator.stream "music21.stream.iterator.StreamIterator.stream") * [`updateActiveInformation()`](#music21.stream.iterator.StreamIterator.updateActiveInformation "music21.stream.iterator.StreamIterator.updateActiveInformation") |

## ActiveInformation

class music21.stream.iterator.ActiveInformation[[source]](../_modules/music21/stream/iterator.html#ActiveInformation)
