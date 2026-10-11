Source: https://music21.org/music21docs/moduleReference/moduleStreamCore.html

# music21.stream.core

the Stream Core Mixin handles the core attributes of streams that
should be thought of almost as private values and not used except
by advanced programmers who need the highest speed in programming.

Nothing here promises to be stable. The music21 team can make
any changes here for efficiency reasons while being considered
backwards compatible so long as the public methods that call these
methods remain stable.

All functions here will eventually begin with .core.

## StreamCore

class music21.stream.core.StreamCore(*\*\*keywords*)[[source]](../_modules/music21/stream/core.html#StreamCore)
:   Core aspects of a Stream’s behavior. Any of these can change at any time.
    Users are encouraged only to create stream.Stream objects.

[`StreamCore`](#music21.stream.core.StreamCore "music21.stream.core.StreamCore") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`StreamCore`](#music21.stream.core.StreamCore "music21.stream.core.StreamCore") read-only properties

StreamCore.spannerBundle
:   A low-level object for Spanner management. This is a read-only property.

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`StreamCore`](#music21.stream.core.StreamCore "music21.stream.core.StreamCore") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`StreamCore`](#music21.stream.core.StreamCore "music21.stream.core.StreamCore") methods

StreamCore.asTimespans(*\**, *flatten=True*, *classList=None*)[[source]](../_modules/music21/stream/core.html#StreamCore.asTimespans)
:   Convert stream to a `TimespanTree` instance, a
    highly optimized data structure for searching through elements and
    offsets.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTimespans()
    >>> print(scoreTree)
    <TimespanTree {20} (0.0 to 8.0) <music21.stream.Score exampleScore>>
        <ElementTimespan (0.0 to 0.0) <music21.clef.BassClef>>
        <ElementTimespan (0.0 to 0.0) <music21.meter.TimeSignature 2/4>>
        <ElementTimespan (0.0 to 0.0) <music21.instrument.Instrument 'PartA: : '>>
        <ElementTimespan (0.0 to 0.0) <music21.clef.BassClef>>
        <ElementTimespan (0.0 to 0.0) <music21.meter.TimeSignature 2/4>>
        <ElementTimespan (0.0 to 0.0) <music21.instrument.Instrument 'PartB: : '>>
        <PitchedTimespan (0.0 to 1.0) <music21.note.Note C>>
        <PitchedTimespan (0.0 to 2.0) <music21.note.Note C#>>
        <PitchedTimespan (1.0 to 2.0) <music21.note.Note D>>
        <PitchedTimespan (2.0 to 3.0) <music21.note.Note E>>
        <PitchedTimespan (2.0 to 4.0) <music21.note.Note G#>>
        <PitchedTimespan (3.0 to 4.0) <music21.note.Note F>>
        <PitchedTimespan (4.0 to 5.0) <music21.note.Note G>>
        <PitchedTimespan (4.0 to 6.0) <music21.note.Note E#>>
        <PitchedTimespan (5.0 to 6.0) <music21.note.Note A>>
        <PitchedTimespan (6.0 to 7.0) <music21.note.Note B>>
        <PitchedTimespan (6.0 to 8.0) <music21.note.Note D#>>
        <PitchedTimespan (7.0 to 8.0) <music21.note.Note C>>
        <ElementTimespan (8.0 to 8.0) <music21.bar.Barline type=final>>
        <ElementTimespan (8.0 to 8.0) <music21.bar.Barline type=final>>
    ```

StreamCore.asTree(*\**, *flatten=False*, *classList=None*, *useTimespans=False*, *groupOffsets=False*)[[source]](../_modules/music21/stream/core.html#StreamCore.asTree)
:   Returns an elementTree of the score, using exact positioning.

    See tree.fromStream.asTree() for more details.

    ```python
    >>> score = tree.examples.makeExampleScore()
    >>> scoreTree = score.asTree(flatten=True)
    >>> scoreTree
    <ElementTree {20} (0.0 <0.-25...> to 8.0) <music21.stream.Score exampleScore>>
    ```

StreamCore.coreAppend(*element: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *setActiveSite=True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/core.html#StreamCore.coreAppend)
:   N.B. – a “core” method, not to be used by general users. Run .append() instead.

    Low level appending; like coreInsert does not error check,
    determine elements changed, or similar operations.

    When using this method, the caller is responsible for calling
    Stream.coreElementsChanged after all operations are completed.

StreamCore.coreCopyAsDerivation(*methodName: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\**, *recurse=True*, *deep=True*) → M21ObjType[[source]](../_modules/music21/stream/core.html#StreamCore.coreCopyAsDerivation)
:   *This is a Core method that most users will not need to use.*

    Make a copy of this stream with the proper derivation set.

    ```python
    >>> s = stream.Stream()
    >>> n = note.Note()
    >>> s.append(n)
    >>> s2 = s.coreCopyAsDerivation('exampleCopy')
    >>> s2.derivation.method
    'exampleCopy'
    >>> s2.derivation.origin is s
    True
    >>> s2[0].derivation.method
    'exampleCopy'
    ```

StreamCore.coreElementsChanged(*\**, *updateIsFlat: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *clearIsSorted: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *memo: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *keepIndex: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/core.html#StreamCore.coreElementsChanged)
:   NB – a “core” stream method that is not necessary for most users.

    This method is called automatically any time the elements in the Stream are changed.
    However, it may be called manually in case sites or other advanced features of an
    element have been modified. It was previously a private method and for most users
    should still be treated as such.

    The various arguments permit optimizing the clearing of cached data in situations
    when completely dropping all cached data is excessive.

    ```python
    >>> a = stream.Stream()
    >>> a.isFlat
    True
    ```

    Here we manipulate the private .\_elements storage (which generally shouldn’t
    be done) using coreAppend and thus need to call .coreElementsChanged directly.

    ```python
    >>> a.coreAppend(stream.Stream())
    >>> a.isFlat  # this is wrong.
    True
    ```

    ```python
    >>> a.coreElementsChanged()
    >>> a.isFlat
    False
    ```

StreamCore.coreGatherMissingSpanners(*\**, *recurse: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *requireAllPresent: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *insert: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *constrainingSpannerBundle: [SpannerBundle](moduleSpanner.html#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Spanner](moduleSpanner.html#music21.spanner.Spanner "music21.spanner.Spanner")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/core.html#StreamCore.coreGatherMissingSpanners)
:   find all spanners that are referenced by elements in the
    (recursed if recurse=True) stream and either inserts them in the Stream
    (if insert is True) or returns them if insert is False.

    If requireAllPresent is True (default) then only those spanners whose complete
    spanned elements are in the Stream are returned.

    Because spanners are stored weakly in .sites this is only guaranteed to find
    the spanners in cases where the spanner is in another stream that is still active.

    Here’s a little helper function since we’ll make the same Stream several times,
    with two slurred notes, but without the slur itself. Python’s garbage collection
    will get rid of the slur if we do not prevent it

    ```python
    >>> preventGarbageCollection = []
    >>> def getStream():
    ...    s = stream.Stream()
    ...    n = note.Note('C')
    ...    m = note.Note('D')
    ...    sl = spanner.Slur(n, m)
    ...    preventGarbageCollection.append(sl)
    ...    s.append([n, m])
    ...    return s
    ```

    Okay now we have a Stream with two slurred notes, but without the slur.
    coreGatherMissingSpanners() will put it in at the beginning.

    ```python
    >>> s = getStream()
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    >>> s.coreGatherMissingSpanners()
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {0.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    {1.0} <music21.note.Note D>
    ```

    Now, the same Stream, but insert is False, so it will return a list of
    Spanners that should be inserted, rather than inserting them.

    ```python
    >>> s = getStream()
    >>> spList = s.coreGatherMissingSpanners(insert=False)
    >>> spList
    [<music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>]
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    ```

    Now we’ll remove the second note so not all elements of the Slur
    are present. This, by default, will not insert the Slur:

    ```python
    >>> s = getStream()
    >>> s.remove(s[-1])
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    >>> s.coreGatherMissingSpanners()
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    ```

    But with requireAllPresent=False, the spanner appears!

    ```python
    >>> s.coreGatherMissingSpanners(requireAllPresent=False)
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {0.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    ```

    With recurse=False, then spanners are not gathered inside the inner
    stream:

    ```python
    >>> part = stream.Part()
    >>> s = getStream()
    >>> part.insert(0, s)
    >>> part.coreGatherMissingSpanners(recurse=False)
    >>> part.show('text')
    {0.0} <music21.stream.Stream 0x104935b00>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
    ```

    But the default acts with recursion:

    ```python
    >>> part.coreGatherMissingSpanners()
    >>> part.show('text')
    {0.0} <music21.stream.Stream 0x104935b00>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
    {0.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    ```

    Spanners already in the stream are not put there again:

    ```python
    >>> s = getStream()
    >>> sl = s.notes.first().getSpannerSites()[0]
    >>> sl
    <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    >>> s.insert(0, sl)
    >>> s.coreGatherMissingSpanners()
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {0.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    {1.0} <music21.note.Note D>
    ```

    Also does not happen with recursion.

    ```python
    >>> part = stream.Part()
    >>> s = getStream()
    >>> sl = s.notes.first().getSpannerSites()[0]
    >>> s.insert(0, sl)
    >>> part.insert(0, s)
    >>> part.coreGatherMissingSpanners()
    >>> part.show('text')
    {0.0} <music21.stream.Stream 0x104935b00>
        {0.0} <music21.note.Note C>
        {0.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
        {1.0} <music21.note.Note D>
    ```

    If constrainingSpannerBundle is set then only spanners also present in
    that spannerBundle are added. This can be useful, for instance, in restoring
    spanners from an excerpt that might already have spanners removed. In
    Jacob Tyler Walls’s brilliant phrasing, it prevents regrowing zombie spanners
    that you thought you had killed.

    Here we will constrain only to spanners also present in another Stream:

    ```python
    >>> s = getStream()
    >>> s2 = stream.Stream()
    >>> s.coreGatherMissingSpanners(constrainingSpannerBundle=s2.spannerBundle)
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {1.0} <music21.note.Note D>
    ```

    Now with the same constraint, but we will put the Slur into the other stream.

    ```python
    >>> sl = s.notes.first().getSpannerSites()[0]
    >>> s2.insert(0, sl)
    >>> s.coreGatherMissingSpanners(constrainingSpannerBundle=s2.spannerBundle)
    >>> s.show('text')
    {0.0} <music21.note.Note C>
    {0.0} <music21.spanner.Slur <music21.note.Note C><music21.note.Note D>>
    {1.0} <music21.note.Note D>
    ```

StreamCore.coreGetElementByMemoryLocation(*objId*)[[source]](../_modules/music21/stream/core.html#StreamCore.coreGetElementByMemoryLocation)
:   NB – a “core” stream method that is not necessary for most users.

    Low-level tool to get an element based only on the object id.

    This is not the same as getElementById, which refers to the id
    attribute which may be manually set and not unique.

    However, some implementations of python will reuse object locations, sometimes
    quickly, so don’t keep these around.

    Used by spanner and variant.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('g#')
    >>> s.append(n1)
    >>> s.coreGetElementByMemoryLocation(id(n1)) is n1
    True
    >>> s.coreGetElementByMemoryLocation(id(n2)) is None
    True
    >>> b = bar.Barline()
    >>> s.storeAtEnd(b)
    >>> s.coreGetElementByMemoryLocation(id(b)) is b
    True
    ```

StreamCore.coreGuardBeforeAddElement(*element*, *\**, *checkRedundancy=True*)[[source]](../_modules/music21/stream/core.html#StreamCore.coreGuardBeforeAddElement)
:   Before adding an element, this method performs
    important checks on that element.

    Used by:

    > * `insert()`
    > * `append()`
    > * `storeAtEnd()`
    > * Stream.\_\_init\_\_()

    Returns None or raises a StreamException

    ```python
    >>> s = stream.Stream()
    >>> s.coreGuardBeforeAddElement(s)
    Traceback (most recent call last):
    music21.exceptions21.StreamException: this Stream cannot be contained within itself
    ```

    ```python
    >>> s.append(s.iter())
    Traceback (most recent call last):
    music21.exceptions21.StreamException: cannot insert StreamIterator into a Stream
    Iterate over it instead (User's Guide chs. 6 and 26)
    ```

    ```python
    >>> s.insert(4, 3.14159)
    Traceback (most recent call last):
    music21.exceptions21.StreamException: The object you tried to add to
    the Stream, 3.14159, is not a Music21Object.  Use an ElementWrapper
    object if this is what you intend.
    ```

StreamCore.coreInsert(*offset: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)")*, *element: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\**, *ignoreSort=False*, *setActiveSite=True*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/stream/core.html#StreamCore.coreInsert)
:   N.B. – a “core” method, not to be used by general users. Run .insert() instead.

    A faster way of inserting elements that performs no checks,
    just insertion.

    Only be used in contexts that we know we have a proper, single Music21Object.
    Best for usage when taking objects in a known Stream and creating a new Stream

    When using this method, the caller is responsible for calling Stream.coreElementsChanged
    after all operations are completed.

    Do not mix coreInsert with coreAppend operations.

    Returns boolean if the Stream (assuming it was sorted before) is still guaranteed
    to be sorted. (False doesn’t mean that it’s not sorted, just that we can’t guarantee it.)
    If you don’t care and plan to sort the stream later, then use ignoreSort=True.

StreamCore.coreSelfActiveSite(*el*)[[source]](../_modules/music21/stream/core.html#StreamCore.coreSelfActiveSite)
:   Set the activeSite of el to be self.

    Override for SpannerStorage, VariantStorage, which should never
    become the activeSite

StreamCore.coreSetElementOffset(*element: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [OffsetSpecial](moduleCommonEnums.html#music21.common.enums.OffsetSpecial "music21.common.enums.OffsetSpecial")*, *\**, *addElement=False*, *setActiveSite=True*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/stream/core.html#StreamCore.coreSetElementOffset)
:   Sets the Offset for an element, very quickly.
    Caller is responsible for calling `coreElementsChanged()`
    afterward.

    ```python
    >>> s = stream.Stream()
    >>> s.id = 'Stream1'
    >>> n = note.Note('B-4')
    >>> s.insert(10, n)
    >>> n.offset
    10.0
    >>> s.coreSetElementOffset(n, 20.0)
    >>> n.offset
    20.0
    >>> n.getOffsetBySite(s)
    20.0
    ```

StreamCore.coreStoreAtEnd(*element*, *setActiveSite=True*)[[source]](../_modules/music21/stream/core.html#StreamCore.coreStoreAtEnd)
:   NB – this is a “core” method. General users should use .storeAtEnd() instead.

    Core method for adding end elements.
    To be called by other methods.

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`StreamCore`](#music21.stream.core.StreamCore "music21.stream.core.StreamCore") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |
