Source: https://music21.org/music21docs/moduleReference/moduleVariant.html

# music21.variant

Contains [`Variant`](#music21.variant.Variant "music21.variant.Variant") and its subclasses, as well as functions for merging
and showing different variant streams. These functions and the variant class should only be
used when variants of a score are the same length and contain the same measure structure at
this time.

## Variant

class music21.variant.Variant(*givenElements: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] = None*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *givenElementsBehavior: [GivenElementsBehavior](moduleStreamEnums.html#music21.stream.enums.GivenElementsBehavior "music21.stream.enums.GivenElementsBehavior") = <GivenElementsBehavior.OFFSETS>*, *\*\*music21ObjectKeywords*)[[source]](../_modules/music21/variant.html#Variant)
:   A Music21Object that stores elements like a Stream, but does not
    represent itself externally to a Stream; i.e., the contents of a Variant are not flattened.

    This is accomplished not by subclassing, but by object composition: similar to the Spanner,
    the Variant contains a Stream as a private attribute. Calls to this Stream, for the Variant,
    are automatically delegated by use of the \_\_getattr\_\_ method. Special cases are overridden
    or managed as necessary: e.g., the Duration of a Variant is generally always zero.

    To use Variants from a Stream, see the `activateVariants()` method.

    ```python
    >>> v = variant.Variant()
    >>> v.repeatAppend(note.Note(), 8)
    >>> len(v.notes)
    8
    >>> v.highestTime
    0.0
    >>> v.containedHighestTime
    8.0
    ```

    ```python
    >>> v.duration  # handled by Music21Object
    <music21.duration.Duration 0.0>
    >>> v.isStream
    False
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.append(v)
    >>> s.append(note.Note())
    >>> s.highestTime
    1.0
    >>> s.show('t')
    {0.0} <music21.variant.Variant object of length 8.0>
    {0.0} <music21.note.Note C>
    >>> s.flatten().show('t')
    {0.0} <music21.variant.Variant object of length 8.0>
    {0.0} <music21.note.Note C>
    ```

[`Variant`](#music21.variant.Variant "music21.variant.Variant") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Variant`](#music21.variant.Variant "music21.variant.Variant") read-only properties

Variant.containedHighestOffset
:   This property calls the contained Stream.highestOffset.

    ```python
    >>> v = variant.Variant()
    >>> v.append(note.Note(quarterLength=4))
    >>> v.append(note.Note())
    >>> v.containedHighestOffset
    4.0
    ```

Variant.containedHighestTime
:   This property calls the contained Stream.highestTime.

    ```python
    >>> v = variant.Variant()
    >>> v.append(note.Note(quarterLength=4))
    >>> v.containedHighestTime
    4.0
    ```

Variant.containedSite
:   Return the Stream contained in this Variant.

Variant.highestOffset
:   This property masks calls to Stream.highestOffset. Assuming exposeTime
    is False, this always returns zero, making the Variant always take zero time.

    ```python
    >>> v = variant.Variant()
    >>> v.append(note.Note(quarterLength=4))
    >>> v.highestOffset
    0.0
    ```

Variant.highestTime
:   This property masks calls to Stream.highestTime. Assuming exposeTime
    is False, this always returns zero, making the Variant always take zero time.

    ```python
    >>> v = variant.Variant()
    >>> v.append(note.Note(quarterLength=4))
    >>> v.highestTime
    0.0
    ```

Variant.lengthType
:   Returns ‘deletion’ if variant is shorter than the region it replaces, ‘elongation’
    if the variant is longer than the region it replaces, and ‘replacement’ if it is
    the same length.

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Variant`](#music21.variant.Variant "music21.variant.Variant") read/write properties

Variant.replacementDuration
:   Set or Return the quarterLength duration in the main stream which this variant
    object replaces in the variant version of the stream. If replacementDuration is
    not set, it is assumed to be the same length as the variant. If, it is set to 0,
    the variant should be interpreted as an insertion. Setting replacementDuration
    to None will return the value to the default which is the duration of the variant
    itself.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Variant`](#music21.variant.Variant "music21.variant.Variant") methods

Variant.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/variant.html#Variant.__getitem__)

Variant.getElementIds()[[source]](../_modules/music21/variant.html#Variant.getElementIds)

Variant.purgeLocations(*rescanIsDead=False*)[[source]](../_modules/music21/variant.html#Variant.purgeLocations)
:   Remove references to all locations in objects that no longer exist.

Variant.purgeOrphans(*excludeStorageStreams=True*)[[source]](../_modules/music21/variant.html#Variant.purgeOrphans)
:   A Music21Object may, due to deep copying or other reasons,
    have a site (with an offset) which
    no longer contains the Music21Object. These lingering sites
    are called orphans. This method gets rid of them.

    The excludeStorageStreams are SpannerStorage and VariantStorage.

Variant.removeReplacedElementsFromStream(*referenceStream=None*, *classList=None*)[[source]](../_modules/music21/variant.html#Variant.removeReplacedElementsFromStream)
:   remove replaced elements from a referenceStream or activeSite

    ```python
    >>> v = variant.Variant()
    >>> variantDataM1 = [('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'),
    ...                  ('a', 'quarter'),('b', 'quarter')]
    >>> variantDataM2 = [('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    >>> variantData = [variantDataM1, variantDataM2]
    >>> for d in variantData:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    v.append(m)
    >>> v.groups = ['paris']
    >>> v.replacementDuration = 4.0
    ```

    ```python
    >>> s = stream.Stream()
    >>> streamDataM1 = [('a', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('g', 'quarter')]
    >>> streamDataM2 = [('b', 'eighth'), ('c', 'quarter'), ('a', 'eighth'),
    ...                 ('a', 'quarter'), ('b', 'quarter')]
    >>> streamDataM3 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> streamDataM4 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> streamData = [streamDataM1, streamDataM2, streamDataM3, streamDataM4]
    >>> for d in streamData:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    s.append(m)
    >>> s.insert(4.0, v)
    ```

    ```python
    >>> v.removeReplacedElementsFromStream(s)
    >>> s.show('t')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note G>
    {4.0} <music21.variant.Variant object of length 8.0>
    {8.0} <music21.stream.Measure 0 offset=8.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    {12.0} <music21.stream.Measure 0 offset=12.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    ```

Variant.replaceElement(*old*, *new*)[[source]](../_modules/music21/variant.html#Variant.replaceElement)
:   When copying a Variant, we need to update the Variant with new
    references for copied elements. Given the old element,
    this method will replace the old with the new.

    The old parameter can be either an object or object id.

    This method is very similar to the replaceSpannedElement method on Spanner.

Variant.replacedElements(*contextStream=None*, *classList=None*, *keepOriginalOffsets=False*, *includeSpacers=False*)[[source]](../_modules/music21/variant.html#Variant.replacedElements)
:   Returns a Stream containing the elements which this variant replaces in a
    given context stream.
    This Stream will have length self.replacementDuration.

    In regions that are strictly replaced, only elements that share a class with
    an element in the variant
    are captured. Elsewhere, all elements are captured.

    ```python
    >>> s = converter.parse("tinynotation: 4/4 d4 e4 f4 g4   a2 b-4 a4    g4 a8 g8 f4 e4    d2 a2                  d4 e4 f4 g4    a2 b-4 a4    g4 a8 b-8 c'4 c4    f1", makeNotation=False)
    >>> s.makeMeasures(inPlace=True)
    >>> v1stream = converter.parse("tinynotation: 4/4        a2. b-8 a8", makeNotation=False)
    >>> v2stream1 = converter.parse("tinynotation: 4/4                                       d4 f4 a2", makeNotation=False)
    >>> v2stream2 = converter.parse("tinynotation: 4/4                                                  d4 f4 AA2", makeNotation=False)
    ```

    ```python
    >>> v1 = variant.Variant()
    >>> v1measure = stream.Measure()
    >>> v1.insert(0.0, v1measure)
    >>> for e in v1stream.notesAndRests:
    ...    v1measure.insert(e.offset, e)
    ```

    ```python
    >>> v2 = variant.Variant()
    >>> v2measure1 = stream.Measure()
    >>> v2measure2 = stream.Measure()
    >>> v2.insert(0.0, v2measure1)
    >>> v2.insert(4.0, v2measure2)
    >>> for e in v2stream1.notesAndRests:
    ...    v2measure1.insert(e.offset, e)
    >>> for e in v2stream2.notesAndRests:
    ...    v2measure2.insert(e.offset, e)
    ```

    ```python
    >>> v3 = variant.Variant()
    >>> v2.replacementDuration = 4.0
    >>> v3.replacementDuration = 4.0
    ```

    ```python
    >>> s.insert(4.0, v1)    # replacement variant
    >>> s.insert(12.0, v2)  # insertion variant (2 bars replace 1 bar)
    >>> s.insert(20.0, v3)  # deletion variant (0 bars replace 1 bar)
    ```

    ```python
    >>> v1.replacedElements(s).show('text')
    {0.0} <music21.stream.Measure 2 offset=0.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    ```

    ```python
    >>> v2.replacedElements(s).show('text')
    {0.0} <music21.stream.Measure 4 offset=0.0>
        {0.0} <music21.note.Note D>
        {2.0} <music21.note.Note A>
    ```

    ```python
    >>> v3.replacedElements(s).show('text')
    {0.0} <music21.stream.Measure 6 offset=0.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    ```

    ```python
    >>> v3.replacedElements(s, keepOriginalOffsets=True).show('text')
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.note.Note A>
        {2.0} <music21.note.Note B->
        {3.0} <music21.note.Note A>
    ```

    A second example:

    ```python
    >>> v = variant.Variant()
    >>> variantDataM1 = [('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'),
    ...                  ('a', 'quarter'),('b', 'quarter')]
    >>> variantDataM2 = [('c', 'quarter'), ('d', 'quarter'),
    ...                  ('e', 'quarter'), ('e', 'quarter')]
    >>> variantData = [variantDataM1, variantDataM2]
    >>> for d in variantData:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    v.append(m)
    >>> v.groups = ['paris']
    >>> v.replacementDuration = 4.0
    ```

    ```python
    >>> s = stream.Stream()
    >>> streamDataM1 = [('a', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('g', 'quarter')]
    >>> streamDataM2 = [('b', 'eighth'), ('c', 'quarter'),
    ...                 ('a', 'eighth'), ('a', 'quarter'), ('b', 'quarter')]
    >>> streamDataM3 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> streamDataM4 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> streamData = [streamDataM1, streamDataM2, streamDataM3, streamDataM4]
    >>> for d in streamData:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    s.append(m)
    >>> s.insert(4.0, v)
    ```

    ```python
    >>> v.replacedElements(s).show('t')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.note.Note B>
        {0.5} <music21.note.Note C>
        {1.5} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    ```

Variant.show(*fmt=None*, *app=None*)[[source]](../_modules/music21/variant.html#Variant.show)
:   Call show() on the Stream contained by this Variant.

    This method must be overridden, otherwise Music21Object.show() is called.

    ```python
    >>> v = variant.Variant()
    >>> v.repeatAppend(note.Note(quarterLength=0.25), 8)
    >>> v.show('t')
    {0.0} <music21.note.Note C>
    {0.25} <music21.note.Note C>
    {0.5} <music21.note.Note C>
    {0.75} <music21.note.Note C>
    {1.0} <music21.note.Note C>
    {1.25} <music21.note.Note C>
    {1.5} <music21.note.Note C>
    {1.75} <music21.note.Note C>
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Variant`](#music21.variant.Variant "music21.variant.Variant") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Functions

music21.variant.addVariant(*s: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream")*, *startOffset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *sVariant: [Stream](moduleStreamBase.html#music21.stream.base.Stream "music21.stream.base.Stream") | [Variant](#music21.variant.Variant "music21.variant.Variant")*, *variantName=None*, *variantGroups=None*, *replacementDuration=None*)[[source]](../_modules/music21/variant.html#addVariant)
:   Takes a stream, the location of the variant to be added to
    that stream (startOffset), the content of the
    variant to be added (sVariant), and the duration of the section of the stream which the variant
    replaces (replacementDuration).

    If replacementDuration is 0,
    this is an insertion. If sVariant is
    None, this is a deletion.

    ```python
    >>> data1M1 = [('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'),
    ...            ('a', 'quarter'), ('a', 'quarter')]
    >>> data1M3 = [('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    >>> data1M2 = [('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'),
    ...            ('a', 'quarter'),('b', 'quarter')]
    >>> data1 = [data1M1, data1M2, data1M3]
    >>> tempPart = stream.Part()
    >>> stream1 = stream.Stream()
    >>> for d in data1:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    stream1.append(m)
    ```

    ```python
    >>> data2M2 = [('b', 'eighth'), ('c', 'quarter'), ('a', 'eighth'),
    ...            ('a', 'quarter'), ('b', 'quarter')]
    >>> stream2 = stream.Stream()
    >>> m = stream.Measure()
    >>> for pitchName, durType in data2M2:
    ...    n = note.Note(pitchName)
    ...    n.duration.type = durType
    ...    m.append(n)
    >>> stream2.append(m)
    >>> variant.addVariant(stream1, 4.0, stream2,
    ...                    variantName='rhythmic_switch', replacementDuration=4.0)
    >>> stream1.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
        {1.5} <music21.note.Note C>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    {4.0} <music21.variant.Variant object of length 4.0>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note B>
        {0.5} <music21.note.Note C>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {8.0} <music21.stream.Measure 0 offset=8.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note E>
    ```

    ```python
    >>> stream1 = stream.Stream()
    >>> stream1.repeatAppend(note.Note('e'), 6)
    >>> variant1 = variant.Variant()
    >>> variant1.repeatAppend(note.Note('f'), 3)
    >>> startOffset = 3.0
    >>> variant.addVariant(stream1, startOffset, variant1,
    ...                    variantName='paris', replacementDuration=3.0)
    >>> stream1.show('text')
    {0.0} <music21.note.Note E>
    {1.0} <music21.note.Note E>
    {2.0} <music21.note.Note E>
    {3.0} <music21.variant.Variant object of length 6.0>
    {3.0} <music21.note.Note E>
    {4.0} <music21.note.Note E>
    {5.0} <music21.note.Note E>
    ```

music21.variant.getMeasureHashes(*s*)[[source]](../_modules/music21/variant.html#getMeasureHashes)
:   Takes in a stream containing measures and returns a list of hashes,
    one for each measure. This is currently implemented
    with search.translateStreamToString()

    ```python
    >>> s = converter.parse("tinynotation: 2/4 c4 d8. e16 FF4 a'4 b-2")
    >>> sm = s.makeMeasures()
    >>> hashes = variant.getMeasureHashes(sm)
    >>> hashes
    ['<P>K@<', ')PQP', 'FZ']
    ```

music21.variant.makeAllVariantsReplacements(*streamWithVariants*, *variantNames=None*, *inPlace=False*, *recurse=False*)[[source]](../_modules/music21/variant.html#makeAllVariantsReplacements)
:   This function takes a stream and a list of variantNames
    (default works on all variants), and changes all insertion
    (elongations with replacementDuration 0)
    and deletion variants (with containedHighestTime 0) into variants with non-zero
    replacementDuration and non-null elements
    by adding measures on the front of insertions and measures on the end
    of deletions. This is designed to make it possible to format all variants in a
    readable way as a graphical ossia (via lilypond). If inPlace is True
    it will perform this action on the stream itself; otherwise it will return a
    modified copy. If recurse is True, this
    method will work on variants within container objects within the stream (like parts).

    ```python
    >>> #                                                          *                                            *                                *
    >>> s = converter.parse("tinynotation: 4/4       d4 e4 f4 g4   a2 b-4 a4    g4 a8 g8 f4 e4    d2 a2                        d4 e4 f4 g4    a2 b-4 a4    g4 a8 b-8 c'4 c4    f1")
    >>> s2 = converter.parse("tinynotation: 4/4      d4 e4 f4 g4   a2. b-8 a8   g4 a8 g8 f4 e4    d2 a2   d4 f4 a2  d4 f4 AA2  d4 e4 f4 g4                 g4 a8 b-8 c'4 c4    f1")
    >>> #                                                          replacement                            insertion                            deletion
    >>> s.makeMeasures(inPlace=True)
    >>> s2.makeMeasures(inPlace=True)
    >>> variant.mergeVariants(s, s2, variantName='london', inPlace=True)
    ```

    ```python
    >>> newStream = stream.Score(s)
    ```

    ```python
    >>> returnStream = variant.makeAllVariantsReplacements(newStream, recurse=False)
    >>> for v in returnStream.parts[0][variant.Variant]:
    ...     (v.offset, v.lengthType, v.replacementDuration)
    (4.0, 'replacement', 4.0)
    (16.0, 'elongation', 0.0)
    (20.0, 'deletion', 4.0)
    ```

    ```python
    >>> returnStream = variant.makeAllVariantsReplacements(
    ...                            newStream, variantNames=['france'], recurse=True)
    >>> for v in returnStream.parts[0][variant.Variant]:
    ...     (v.offset, v.lengthType, v.replacementDuration)
    (4.0, 'replacement', 4.0)
    (16.0, 'elongation', 0.0)
    (20.0, 'deletion', 4.0)
    ```

    ```python
    >>> variant.makeAllVariantsReplacements(newStream, recurse=True, inPlace=True)
    >>> for v in newStream.parts[0][variant.Variant]:
    ...     (v.offset, v.lengthType, v.replacementDuration, v.containedHighestTime)
    (4.0, 'replacement', 4.0, 4.0)
    (12.0, 'elongation', 4.0, 12.0)
    (20.0, 'deletion', 8.0, 4.0)
    ```

music21.variant.makeVariantBlocks(*s*)[[source]](../_modules/music21/variant.html#makeVariantBlocks)
:   Unknown and undocumented. Used only in lily/translate – for musicdiff.

music21.variant.mergePartAsOssia(*mainPart*, *ossiaPart*, *ossiaName*, *inPlace=False*, *compareByMeasureNumber=False*, *recurseInMeasures=False*)[[source]](../_modules/music21/variant.html#mergePartAsOssia)
:   Some MusicXML files are generated with full parts that have only a few non-rest measures
    instead of ossia parts, such as those
    created by Sibelius 7. This function
    takes two streams (mainPart and ossiaPart), the second interpreted as an ossia.
    It outputs a stream with the ossia part merged into the stream as a
    group of variants.

    If compareByMeasureNumber is True, then the ossia measures will be paired with the
    measures in the mainPart that have the
    same measure.number. Otherwise, they will be paired by offset. In most cases
    these should have the same result.

    Note that this method has no way of knowing if a variant is supposed to be a
    different duration than the segment of stream which it replaces
    because that information is not contained in the format of score this method is
    designed to deal with.

    ```python
    >>> mainStream = converter.parse('tinynotation: 4/4   A4 B4 C4 D4   E1    F2 E2     E8 F8 F4 G2   G2 G4 F4   F4 F4 F4 F4   G1      ')
    >>> ossiaStream = converter.parse('tinynotation: 4/4  r1            r1    r1        E4 E4 F4 G4   r1         F2    F2      r1      ')
    >>> mainStream.makeMeasures(inPlace=True)
    >>> ossiaStream.makeMeasures(inPlace=True)
    ```

    ```python
    >>> mainPart = stream.Part()
    >>> for m in mainStream:
    ...    mainPart.insert(m.offset, m)
    >>> ossiaPart = stream.Part()
    >>> for m in ossiaStream:
    ...    ossiaPart.insert(m.offset, m)
    ```

    ```python
    >>> s = stream.Stream()
    >>> s.insert(0.0, ossiaPart)
    >>> s.insert(0.0, mainPart)
    >>> s.show()
    ```

    ```python
    >>> mainPartWithOssiaVariantsFT = variant.mergePartAsOssia(mainPart, ossiaPart,
    ...                                                            ossiaName='Parisian_Variant',
    ...                                                            inPlace=False,
    ...                                                            compareByMeasureNumber=False,
    ...                                                            recurseInMeasures=True)
    >>> mainPartWithOssiaVariantsTT = variant.mergePartAsOssia(mainPart, ossiaPart,
    ...                                                            ossiaName='Parisian_Variant',
    ...                                                            inPlace=False,
    ...                                                            compareByMeasureNumber=True,
    ...                                                            recurseInMeasures=True)
    >>> mainPartWithOssiaVariantsFF = variant.mergePartAsOssia(mainPart, ossiaPart,
    ...                                                            ossiaName='Parisian_Variant',
    ...                                                            inPlace=False,
    ...                                                            compareByMeasureNumber=False,
    ...                                                            recurseInMeasures=False)
    >>> mainPartWithOssiaVariantsTF = variant.mergePartAsOssia(mainPart, ossiaPart,
    ...                                                            ossiaName='Parisian_Variant',
    ...                                                            inPlace=False,
    ...                                                            compareByMeasureNumber=True,
    ...                                                            recurseInMeasures=False)
    ```

    ```python
    >>> mainPartWithOssiaVariantsFT.show('text') == mainPartWithOssiaVariantsTT.show('text')
    {0.0} <music21.stream.Measure ...
    True
    ```

    ```python
    >>> mainPartWithOssiaVariantsFF.show('text') == mainPartWithOssiaVariantsFT.show('text')
    {0.0} <music21.stream.Measure ...
    True
    ```

    ```python
    >>> mainPartWithOssiaVariantsFT.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
    ...
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.variant.Variant object of length 3.0>
        {0.0} <music21.note.Note E>
        {0.5} <music21.note.Note F>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note G>
    {16.0} <music21.stream.Measure 5 offset=16.0>
    ...
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.variant.Variant object of length 4.0>
        {0.0} <music21.note.Note F>
        {1.0} <music21.note.Note F>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note F>
    ...
    ```

    ```python
    >>> mainPartWithOssiaVariantsFF.activateVariants('Parisian_Variant').show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
    ...
    {12.0} <music21.variant.Variant object of length 4.0>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note E>
        {2.0} <music21.note.Note F>
        {3.0} <music21.note.Note G>
    {16.0} <music21.stream.Measure 5 offset=16.0>
    ...
    {20.0} <music21.variant.Variant object of length 4.0>
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.note.Note F>
        {2.0} <music21.note.Note F>
    ...
    ```

music21.variant.mergeVariantMeasureStreams(*streamX*, *streamY*, *variantName='variant'*, *\**, *inPlace=False*)[[source]](../_modules/music21/variant.html#mergeVariantMeasureStreams)
:   Takes two streams of measures and returns a stream (new if inPlace is False) with the second
    merged with the first as variants. This function differs from mergeVariantsEqualDuration by
    dealing with streams that are of different length. This function matches measures that are
    exactly equal and creates variant objects for regions of measures that differ at all. If more
    refined variants are sought (with variation within the bar considered and related but different
    bars associated with each other), use variant.refineVariant().

    In this example, the second bar has been deleted in the second version,
    a new bar has been inserted between the
    original third and fourth bars, and two bars have been added at the end.

    ```python
    >>> data1M1 = [('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'),
    ...            ('a', 'quarter'), ('a', 'quarter')]
    >>> data1M2 = [('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'),
    ...            ('a', 'quarter'),('b', 'quarter')]
    >>> data1M3 = [('c', 'quarter'), ('d', 'quarter'),
    ...            ('e', 'quarter'), ('e', 'quarter')]
    >>> data1M4 = [('d', 'quarter'), ('g', 'eighth'), ('g', 'eighth'),
    ...            ('a', 'quarter'), ('b', 'quarter')]
    ```

    ```python
    >>> data2M1 = [('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'),
    ...            ('a', 'quarter'), ('a', 'quarter')]
    >>> data2M2 = [('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    >>> data2M3 = [('e', 'quarter'), ('g', 'eighth'), ('g', 'eighth'),
    ...            ('a', 'quarter'), ('b', 'quarter')]
    >>> data2M4 = [('d', 'quarter'), ('g', 'eighth'), ('g', 'eighth'),
    ...            ('a', 'quarter'), ('b', 'quarter')]
    >>> data2M5 = [('f', 'eighth'), ('c', 'quarter'), ('a', 'eighth'),
    ...            ('a', 'quarter'), ('b', 'quarter')]
    >>> data2M6 = [('g', 'quarter'), ('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    ```

    ```python
    >>> data1 = [data1M1, data1M2, data1M3, data1M4]
    >>> data2 = [data2M1, data2M2, data2M3, data2M4, data2M5, data2M6]
    >>> stream1 = stream.Stream()
    >>> stream2 = stream.Stream()
    >>> mNumber = 1
    >>> for d in data1:
    ...    m = stream.Measure()
    ...    m.number = mNumber
    ...    mNumber += 1
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    stream1.append(m)
    >>> mNumber = 1
    >>> for d in data2:
    ...    m = stream.Measure()
    ...    m.number = mNumber
    ...    mNumber += 1
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    stream2.append(m)
    >>> stream1.show()
    ```

    [![../_images/variant_measuresStreamMergeStream1.png](../_images/variant_measuresStreamMergeStream1.png)](../_images/variant_measuresStreamMergeStream1.png)

    ```python
    >>> stream2.show()
    ```

    [![../_images/variant_measuresStreamMergeStream2.png](../_images/variant_measuresStreamMergeStream2.png)](../_images/variant_measuresStreamMergeStream2.png)

    ```python
    >>> mergedStream = variant.mergeVariantMeasureStreams(stream1, stream2, 'paris', inPlace=False)
    >>> mergedStream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
        {1.5} <music21.note.Note C>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    {4.0} <music21.variant.Variant object of length 0.0>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note B>
        {0.5} <music21.note.Note C>
        {1.0} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note E>
    {12.0} <music21.variant.Variant object of length 4.0>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note G>
        {1.5} <music21.note.Note G>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {16.0} <music21.variant.Variant object of length 8.0>
    ```

    ```python
    >>> mergedStream[variant.Variant][0].replacementDuration
    4.0
    >>> mergedStream[variant.Variant][1].replacementDuration
    0.0
    ```

    ```python
    >>> parisStream = mergedStream.activateVariants('paris', inPlace=False)
    >>> parisStream.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
        {1.5} <music21.note.Note C>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    {4.0} <music21.variant.Variant object of length 4.0>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note E>
    {8.0} <music21.variant.Variant object of length 0.0>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note E>
        {1.0} <music21.note.Note G>
        {1.5} <music21.note.Note G>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note D>
        {1.0} <music21.note.Note G>
        {1.5} <music21.note.Note G>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {16.0} <music21.variant.Variant object of length 0.0>
    {16.0} <music21.stream.Measure 5 offset=16.0>
        {0.0} <music21.note.Note F>
        {0.5} <music21.note.Note C>
        {1.5} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {20.0} <music21.stream.Measure 6 offset=20.0>
        {0.0} <music21.note.Note G>
        {1.0} <music21.note.Note D>
        {2.0} <music21.note.Note E>
        {3.0} <music21.note.Note E>
    ```

    ```python
    >>> parisStream[variant.Variant][0].replacementDuration
    0.0
    >>> parisStream[variant.Variant][1].replacementDuration
    4.0
    >>> parisStream[variant.Variant][2].replacementDuration
    8.0
    ```

music21.variant.mergeVariantScores(*aScore*, *vScore*, *variantName='variant'*, *\**, *inPlace=False*)[[source]](../_modules/music21/variant.html#mergeVariantScores)
:   Takes two scores and merges them with mergeVariantMeasureStreams, part-by-part.

    ```python
    >>> aScore, vScore = stream.Score(), stream.Score()
    ```

    ```python
    >>> ap1 = converter.parse('tinynotation: 4/4   a4 b c d    e2 f2   g2 f4 g4 ')
    >>> vp1 = converter.parse('tinynotation: 4/4   a4 b c e    e2 f2   g2 f4 a4 ')
    ```

    ```python
    >>> ap2 = converter.parse('tinynotation: 4/4   a4 g f e    f2 e2   d2 g4 f4 ')
    >>> vp2 = converter.parse('tinynotation: 4/4   a4 g f e    f2 g2   f2 g4 d4 ')
    ```

    ```python
    >>> aScore.insert(0.0, ap1)
    >>> aScore.insert(0.0, ap2)
    >>> vScore.insert(0.0, vp1)
    >>> vScore.insert(0.0, vp2)
    ```

    ```python
    >>> mergedScores = variant.mergeVariantScores(aScore, vScore,
    ...                                           variantName='docVariant', inPlace=False)
    >>> mergedScores.show('text')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.variant.Variant object of length 4.0>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note A>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note C>
            {3.0} <music21.note.Note D>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note E>
            {2.0} <music21.note.Note F>
        {8.0} <music21.variant.Variant object of length 4.0>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.note.Note G>
            {2.0} <music21.note.Note F>
            {3.0} <music21.note.Note G>
            {4.0} <music21.bar.Barline type=final>
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note A>
            {1.0} <music21.note.Note G>
            {2.0} <music21.note.Note F>
            {3.0} <music21.note.Note E>
        {4.0} <music21.variant.Variant object of length 8.0>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note F>
            {2.0} <music21.note.Note E>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.note.Note D>
            {2.0} <music21.note.Note G>
            {3.0} <music21.note.Note F>
            {4.0} <music21.bar.Barline type=final>
    ```

music21.variant.mergeVariants(*streamX*, *streamY*, *variantName='variant'*, *\**, *inPlace=False*)[[source]](../_modules/music21/variant.html#mergeVariants)
:   Takes two streams objects or their derivatives (Score, Part, Measure, etc.) which
    should be variant versions of the same stream,
    and merges them (determines differences and stores those differences as variant objects
    in streamX) via the appropriate merge
    function for their type. This will not know how to deal with scores meant for
    mergePartAsOssia(). If this is the intention, use
    that function instead.

    ```python
    >>> streamX = converter.parse('tinynotation: 4/4 a4 b  c d', makeNotation=False)
    >>> streamY = converter.parse('tinynotation: 4/4 a4 b- c e', makeNotation=False)
    ```

    ```python
    >>> mergedStream = variant.mergeVariants(streamX, streamY,
    ...                                      variantName='docVariant', inPlace=False)
    >>> mergedStream.show('text')
    {0.0} <music21.meter.TimeSignature 4/4>
    {0.0} <music21.note.Note A>
    {1.0} <music21.variant.Variant object of length 1.0>
    {1.0} <music21.note.Note B>
    {2.0} <music21.note.Note C>
    {3.0} <music21.variant.Variant object of length 1.0>
    {3.0} <music21.note.Note D>
    ```

    ```python
    >>> v0 = mergedStream.getElementsByClass(variant.Variant).first()
    >>> v0
    <music21.variant.Variant object of length 1.0>
    >>> v0.first()
    <music21.note.Note B->
    ```

    ```python
    >>> streamZ = converter.parse('tinynotation: 4/4 a4 b c d e f g a', makeNotation=False)
    >>> variant.mergeVariants(streamX, streamZ, variantName='docVariant', inPlace=False)
    Traceback (most recent call last):
    music21.variant.VariantException: Could not determine what merging method to use.
            Try using a more specific merging function.
    ```

    Example: Create a main score (aScore) and a variant score (vScore), each with
    two parts (ap1/vp1
    and ap2/vp2) and some small variants between ap1/vp1 and ap2/vp2, marked with \* below.

    ```python
    >>> aScore = stream.Score()
    >>> vScore = stream.Score()
    ```

    ```python
    >>> #                                                 *
    >>> ap1 = converter.parse('tinynotation: 4/4   a4 b c d    e2 f   g2 f4 g ')
    >>> vp1 = converter.parse('tinynotation: 4/4   a4 b c e    e2 f   g2 f4 a ')
    ```

    ```python
    >>> #                                                         *    *    *
    >>> ap2 = converter.parse('tinynotation: 4/4   a4 g f e    f2 e   d2 g4 f ')
    >>> vp2 = converter.parse('tinynotation: 4/4   a4 g f e    f2 g   f2 g4 d ')
    ```

    ```python
    >>> ap1.id = 'aPart1'
    >>> ap2.id = 'aPart2'
    ```

    ```python
    >>> aScore.insert(0.0, ap1)
    >>> aScore.insert(0.0, ap2)
    >>> vScore.insert(0.0, vp1)
    >>> vScore.insert(0.0, vp2)
    ```

    Create one merged score where everything different in vScore from aScore is called a variant.

    ```python
    >>> mergedScore = variant.mergeVariants(aScore, vScore, variantName='docVariant', inPlace=False)
    >>> mergedScore.show('text')
    {0.0} <music21.stream.Part aPart1>
        {0.0} <music21.variant.Variant object of length 4.0>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note A>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note C>
            {3.0} <music21.note.Note D>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note E>
            {2.0} <music21.note.Note F>
        {8.0} <music21.variant.Variant object of length 4.0>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.note.Note G>
            {2.0} <music21.note.Note F>
            {3.0} <music21.note.Note G>
            {4.0} <music21.bar.Barline type=final>
    {0.0} <music21.stream.Part aPart2>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.clef.TrebleClef>
            {0.0} <music21.meter.TimeSignature 4/4>
            {0.0} <music21.note.Note A>
            {1.0} <music21.note.Note G>
            {2.0} <music21.note.Note F>
            {3.0} <music21.note.Note E>
        {4.0} <music21.variant.Variant object of length 8.0>
        {4.0} <music21.stream.Measure 2 offset=4.0>
            {0.0} <music21.note.Note F>
            {2.0} <music21.note.Note E>
        {8.0} <music21.stream.Measure 3 offset=8.0>
            {0.0} <music21.note.Note D>
            {2.0} <music21.note.Note G>
            {3.0} <music21.note.Note F>
            {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> mergedPart = variant.mergeVariants(ap2, vp2, variantName='docVariant', inPlace=False)
    >>> mergedPart.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
    ...
    {4.0} <music21.variant.Variant object of length 8.0>
    {4.0} <music21.stream.Measure 2 offset=4.0>
    ...
        {4.0} <music21.bar.Barline type=final>
    ```

music21.variant.mergeVariantsEqualDuration(*streams*, *variantNames*, *\**, *inPlace=False*)[[source]](../_modules/music21/variant.html#mergeVariantsEqualDuration)
:   Pass this function a list of streams (they must be of the same
    length or a VariantException will be raised).
    It will return a stream which merges the differences between the
    streams into variant objects keeping the
    first stream in the list as the default. If inPlace is True, the
    first stream in the list will be modified,
    otherwise a new stream will be returned. Pass a list of names to
    associate variants with their sources, if this list
    does not contain an entry for each non-default variant,
    naming may not behave properly. Variants that have the
    same differences from the default will be saved as separate
    variant objects (i.e. more than once under different names).
    Also, note that a streams with bars of differing lengths will not behave properly.

    ```python
    >>> stream1 = stream.Stream()
    >>> stream2paris = stream.Stream()
    >>> stream3london = stream.Stream()
    >>> data1 = [('a', 'quarter'), ('b', 'eighth'),
    ...    ('c', 'eighth'), ('a', 'quarter'), ('a', 'quarter'),
    ...    ('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'), ('a', 'quarter'),
    ...    ('b', 'quarter'), ('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter')]
    >>> data2 = [('a', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('g', 'quarter'),
    ...    ('b', 'eighth'), ('c', 'quarter'), ('a', 'eighth'), ('a', 'quarter'),
    ...    ('b', 'quarter'), ('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter')]
    >>> data3 = [('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'),
    ...    ('a', 'quarter'), ('a', 'quarter'),
    ...    ('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'), ('a', 'quarter'),
    ...    ('c', 'quarter'), ('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter')]
    >>> for pitchName, durType in data1:
    ...    n = note.Note(pitchName)
    ...    n.duration.type = durType
    ...    stream1.append(n)
    >>> for pitchName, durType in data2:
    ...    n = note.Note(pitchName)
    ...    n.duration.type = durType
    ...    stream2paris.append(n)
    >>> for pitchName, durType in data3:
    ...    n = note.Note(pitchName)
    ...    n.duration.type = durType
    ...    stream3london.append(n)
    >>> mergedStreams = variant.mergeVariantsEqualDuration(
    ...       [stream1, stream2paris, stream3london], ['paris', 'london'])
    >>> mergedStreams.show('t')
    {0.0} <music21.note.Note A>
    {1.0} <music21.variant.Variant object of length 1.0>
    {1.0} <music21.note.Note B>
    {1.5} <music21.note.Note C>
    {2.0} <music21.note.Note A>
    {3.0} <music21.variant.Variant object of length 1.0>
    {3.0} <music21.note.Note A>
    {4.0} <music21.note.Note B>
    {4.5} <music21.variant.Variant object of length 1.5>
    {4.5} <music21.note.Note C>
    {5.0} <music21.note.Note A>
    {6.0} <music21.note.Note A>
    {7.0} <music21.variant.Variant object of length 1.0>
    {7.0} <music21.note.Note B>
    {8.0} <music21.note.Note C>
    {9.0} <music21.variant.Variant object of length 2.0>
    {9.0} <music21.note.Note D>
    {10.0} <music21.note.Note E>
    ```

    ```python
    >>> mergedStreams.activateVariants('london').show('t')
    {0.0} <music21.note.Note A>
    {1.0} <music21.variant.Variant object of length 1.0>
    {1.0} <music21.note.Note B>
    {1.5} <music21.note.Note C>
    {2.0} <music21.note.Note A>
    {3.0} <music21.variant.Variant object of length 1.0>
    {3.0} <music21.note.Note A>
    {4.0} <music21.note.Note B>
    {4.5} <music21.variant.Variant object of length 1.5>
    {4.5} <music21.note.Note C>
    {5.0} <music21.note.Note A>
    {6.0} <music21.note.Note A>
    {7.0} <music21.variant.Variant object of length 1.0>
    {7.0} <music21.note.Note C>
    {8.0} <music21.note.Note C>
    {9.0} <music21.variant.Variant object of length 2.0>
    {9.0} <music21.note.Note D>
    {10.0} <music21.note.Note E>
    ```

    If the streams contain parts and measures, the merge function will iterate
    through them and determine
    and store variant differences within each measure/part.

    ```python
    >>> stream1 = stream.Stream()
    >>> stream2 = stream.Stream()
    >>> data1M1 = [('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'),
    ...            ('a', 'quarter'), ('a', 'quarter')]
    >>> data1M2 = [('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'),
    ...            ('a', 'quarter'),('b', 'quarter')]
    >>> data1M3 = [('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    >>> data2M1 = [('a', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('g', 'quarter')]
    >>> data2M2 = [('b', 'eighth'), ('c', 'quarter'), ('a', 'eighth'),
    ...            ('a', 'quarter'), ('b', 'quarter')]
    >>> data2M3 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> data1 = [data1M1, data1M2, data1M3]
    >>> data2 = [data2M1, data2M2, data2M3]
    >>> tempPart = stream.Part()
    >>> for d in data1:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    tempPart.append(m)
    >>> stream1.append(tempPart)
    >>> tempPart = stream.Part()
    >>> for d in data2:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    tempPart.append(m)
    >>> stream2.append(tempPart)
    >>> mergedStreams = variant.mergeVariantsEqualDuration([stream1, stream2], ['paris'])
    >>> mergedStreams.show('t')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.note.Note A>
            {1.0} <music21.variant.Variant object of length 1.0>
            {1.0} <music21.note.Note B>
            {1.5} <music21.note.Note C>
            {2.0} <music21.note.Note A>
            {3.0} <music21.variant.Variant object of length 1.0>
            {3.0} <music21.note.Note A>
        {4.0} <music21.stream.Measure 0 offset=4.0>
            {0.0} <music21.note.Note B>
            {0.5} <music21.variant.Variant object of length 1.5>
            {0.5} <music21.note.Note C>
            {1.0} <music21.note.Note A>
            {2.0} <music21.note.Note A>
            {3.0} <music21.note.Note B>
        {8.0} <music21.stream.Measure 0 offset=8.0>
            {0.0} <music21.note.Note C>
            {1.0} <music21.variant.Variant object of length 3.0>
            {1.0} <music21.note.Note D>
            {2.0} <music21.note.Note E>
            {3.0} <music21.note.Note E>
    >>> mergedStreams.show()
    ```

    [![../_images/variant_measuresAndParts.png](../_images/variant_measuresAndParts.png)](../_images/variant_measuresAndParts.png)

    ```python
    >>> for p in mergedStreams.getElementsByClass(stream.Part):
    ...    for m in p.getElementsByClass(stream.Measure):
    ...        m.activateVariants('paris', inPlace=True)
    >>> mergedStreams.show('t')
    {0.0} <music21.stream.Part ...>
        {0.0} <music21.stream.Measure 0 offset=0.0>
            {0.0} <music21.note.Note A>
            {1.0} <music21.variant.Variant object of length 1.0>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note A>
            {3.0} <music21.variant.Variant object of length 1.0>
            {3.0} <music21.note.Note G>
        {4.0} <music21.stream.Measure 0 offset=4.0>
            {0.0} <music21.note.Note B>
            {0.5} <music21.variant.Variant object of length 1.5>
            {0.5} <music21.note.Note C>
            {1.5} <music21.note.Note A>
            {2.0} <music21.note.Note A>
            {3.0} <music21.note.Note B>
        {8.0} <music21.stream.Measure 0 offset=8.0>
            {0.0} <music21.note.Note C>
            {1.0} <music21.variant.Variant object of length 3.0>
            {1.0} <music21.note.Note B>
            {2.0} <music21.note.Note A>
            {3.0} <music21.note.Note A>
    >>> mergedStreams.show()
    ```

    [![../_images/variant_measuresAndParts2.png](../_images/variant_measuresAndParts2.png)](../_images/variant_measuresAndParts2.png)

    If barlines do not match up, an exception will be thrown. Here two streams that are identical
    are merged, except one is in 3/4, the other in 4/4. This throws an exception.

    ```python
    >>> streamDifferentMeasures = stream.Stream()
    >>> dataDiffM1 = [('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter')]
    >>> dataDiffM2 = [ ('a', 'quarter'), ('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter')]
    >>> dataDiffM3 = [('a', 'quarter'), ('b', 'quarter'), ('c', 'quarter')]
    >>> dataDiffM4 = [('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    >>> dataDiff = [dataDiffM1, dataDiffM2, dataDiffM3, dataDiffM4]
    >>> streamDifferentMeasures.insert(0.0, meter.TimeSignature('3/4'))
    >>> tempPart = stream.Part()
    >>> for d in dataDiff:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    tempPart.append(m)
    >>> streamDifferentMeasures.append(tempPart)
    >>> mergedStreams = variant.mergeVariantsEqualDuration(
    ...                 [stream1, streamDifferentMeasures], ['paris'])
    Traceback (most recent call last):
    music21.variant.VariantException: _mergeVariants cannot merge streams
        which are of different lengths
    ```

music21.variant.refineVariant(*s*, *sVariant*, *\**, *inPlace=False*)[[source]](../_modules/music21/variant.html#refineVariant)
:   Given a stream and variant contained in that stream, returns a
    stream with that variant ‘refined.’

    It is refined in the sense that, (with the best estimates) measures which have been determined
    to be related are merged within the measure.

    Suppose a four-bar phrase in a piece is a slightly
    different five-bar phrase in a variant. In the variant, every F# has been replaced by an F,
    and the last bar is repeated. Given these streams, mergeVariantMeasureStreams would return
    the first stream with a single variant object containing the entire 5 bars of the variant.
    Calling refineVariant on this stream and that variant object would result in a variant object
    in the measures for each F#/F pair, and a variant object containing the added bar at the end.
    For a more detailed explanation of how similar measures are properly associated with each other
    look at the documentation for \_getBestListAndScore

    Note that this code does not work properly yet.

    ```python
    >>> v = variant.Variant()
    >>> variantDataM1 = [('b', 'eighth'), ('c', 'eighth'), ('a', 'quarter'),
    ...                  ('a', 'quarter'),('b', 'quarter')]
    >>> variantDataM2 = [('c', 'quarter'), ('d', 'quarter'), ('e', 'quarter'), ('e', 'quarter')]
    >>> variantData = [variantDataM1, variantDataM2]
    >>> for d in variantData:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    v.append(m)
    >>> v.groups = ['paris']
    >>> v.replacementDuration = 8.0
    ```

    ```python
    >>> s = stream.Stream()
    >>> streamDataM1 = [('a', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('g', 'quarter')]
    >>> streamDataM2 = [('b', 'eighth'), ('c', 'quarter'),
    ...                 ('a', 'eighth'), ('a', 'quarter'), ('b', 'quarter')]
    >>> streamDataM3 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> streamDataM4 = [('c', 'quarter'), ('b', 'quarter'), ('a', 'quarter'), ('a', 'quarter')]
    >>> streamData = [streamDataM1, streamDataM2, streamDataM3, streamDataM4]
    >>> for d in streamData:
    ...    m = stream.Measure()
    ...    for pitchName, durType in d:
    ...        n = note.Note(pitchName)
    ...        n.duration.type = durType
    ...        m.append(n)
    ...    s.append(m)
    >>> s.insert(4.0, v)
    ```

    ```python
    >>> variant.refineVariant(s, v, inPlace=True)
    >>> s.show('text')
    {0.0} <music21.stream.Measure 0 offset=0.0>
        {0.0} <music21.note.Note A>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note G>
    {4.0} <music21.stream.Measure 0 offset=4.0>
        {0.0} <music21.note.Note B>
        {0.5} <music21.variant.Variant object of length 1.5>
        {0.5} <music21.note.Note C>
        {1.5} <music21.note.Note A>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note B>
    {8.0} <music21.stream.Measure 0 offset=8.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.variant.Variant object of length 3.0>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    {12.0} <music21.stream.Measure 0 offset=12.0>
        {0.0} <music21.note.Note C>
        {1.0} <music21.note.Note B>
        {2.0} <music21.note.Note A>
        {3.0} <music21.note.Note A>
    ```
