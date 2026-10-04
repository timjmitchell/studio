Source: https://music21.org/music21docs/moduleReference/moduleSpanner.html

# music21.spanner

A spanner is a music21 object that represents a connection usually between
two or more music21 objects that might live in different streams but need
some sort of connection between them. A slur is one type of spanner – it might
connect notes in different Measure objects or even between different parts.

This package defines some of the most common spanners. Other spanners
can be found in modules such as [music21.dynamics](moduleDynamics.html#moduledynamics) (for things such as crescendos).

## Spanner

class music21.spanner.Spanner(*\*spannedElements: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")]*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#Spanner)
:   Spanner objects live on Streams in the same manner as other Music21Objects,
    but represent and store connections between one or more other Music21Objects.

    Commonly used Spanner subclasses include the [`Slur`](#music21.spanner.Slur "music21.spanner.Slur"),
    [`RepeatBracket`](#music21.spanner.RepeatBracket "music21.spanner.RepeatBracket"), `Crescendo`,
    and `Diminuendo`
    objects.

    In some cases you will want to subclass Spanner
    for specific purposes.

    In the first demo, we create
    a spanner to represent a written-out accelerando, such
    as Elliott Carter uses in his second string quartet (he marks them
    with an arrow).

    ```python
    >>> class CarterAccelerandoSign(spanner.Spanner):
    ...    pass
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> n3 = note.Note('E4')
    >>> sp1 = CarterAccelerandoSign(n1, n2, n3)  # or as a list: [n1, n2, n3]
    >>> sp1.getSpannedElements()
    [<music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>]
    ```

    We can iterate over a spanner to get the contexts:

    ```python
    >>> print(' '.join([repr(n) for n in sp1]))
    <music21.note.Note C> <music21.note.Note D> <music21.note.Note E>
    ```

    Now we put the notes and the spanner into a Stream object. Note that
    the convention is to put the spanner at the beginning of the innermost
    Stream that contains all the Spanners:

    ```python
    >>> s = stream.Stream()
    >>> s.append([n1, n2, n3])
    >>> s.insert(0, sp1)
    ```

    Now we can get at the spanner in one of three ways.

    1. it is just a normal element in the stream:

    ```python
    >>> for e in s:
    ...    print(e)
    <music21.note.Note C>
    <...CarterAccelerandoSign <music21.note.Note C><music21.note.Note D><music21.note.Note E>>
    <music21.note.Note D>
    <music21.note.Note E>
    ```

    2. we can get a stream of spanners (equiv. to getElementsByClass(spanner.Spanner))
       by calling the .spanner property on the stream.

    ```python
    >>> spannerCollection = s.spanners  # a stream object
    >>> for thisSpanner in spannerCollection:
    ...     print(thisSpanner)
    <...CarterAccelerandoSign <music21.note.Note C><music21.note.Note D><music21.note.Note E>>
    ```

    (3) we can get the spanner by looking at the list getSpannerSites() on
    any object that has a spanner:

    ```python
    >>> n2.getSpannerSites()
    [<music21...CarterAccelerandoSign
            <music21.note.Note C><music21.note.Note D><music21.note.Note E>>]
    ```

    In this example we will slur a few notes and then iterate over the stream to
    see which are slurred:

    ```python
    >>> n1 = note.Note('C4')
    >>> n2 = note.Note('D4')
    >>> n3 = note.Note('E4')
    >>> n4 = note.Note('F4')
    >>> n5 = note.Note('G4')
    >>> n6 = note.Note('A4')
    ```

    Create a slur over the second and third notes at instantiation:

    ```python
    >>> slur1 = spanner.Slur([n2, n3])
    ```

    Slur the fifth and the sixth notes by adding them to an existing slur:

    ```python
    >>> slur2 = spanner.Slur()
    >>> slur2.addSpannedElements([n5, n6])
    ```

    Now add them all to a stream:

    ```python
    >>> part1 = stream.Part()
    >>> part1.append([n1, n2, n3, n4, n5, n6])
    >>> part1.insert(0, slur1)
    >>> part1.insert(0, slur2)
    ```

    Say we wanted to know which notes in a piece started a
    slur, here’s how we could do it:

    ```python
    >>> for n in part1.notes:
    ...    ss = n.getSpannerSites()
    ...    for thisSpanner in ss:
    ...       if 'Slur' in thisSpanner.classes:
    ...            if thisSpanner.isFirst(n):
    ...                print(n.nameWithOctave)
    D4
    G4
    ```

    Alternatively, you could iterate over the spanners
    of part1 and get their first elements:

    ```python
    >>> for thisSpanner in part1.spanners:
    ...     firstNote = thisSpanner.getSpannedElements()[0]
    ...     print(firstNote.nameWithOctave)
    D4
    G4
    ```

    The second method is shorter, but the first is likely to
    be useful in cases where you are doing other things to
    each note object along the way.

    Oh, and of course, slurs do print properly in musicxml:

    ```python
    >>> part1.show()
    ```

    [![../_images/slur1_example.png](../_images/slur1_example.png)](../_images/slur1_example.png)

    (the Carter example would not print an arrow since that
    element has no corresponding musicxml representation).

    *Implementation notes:*

    The elements that are included in a spanner are stored in a
    Stream subclass called `SpannerStorage`
    found as the .spannerStorage attribute. That Stream has an
    attribute called client which links to the original spanner.
    Thus, spannerStorage is smart enough to know where it’s stored, but
    it makes deleting/garbage-collecting a spanner a tricky operation:

    Ex. Prove that the spannedElement Stream is linked to container via
    client:

    ```python
    >>> sp1.spannerStorage.client is sp1
    True
    ```

    Spanners have a .completeStatus attribute which can be used to find out if
    all spanned elements have been added yet. It’s up to the processing agent to
    set this, but it could be useful in deciding where to append a spanner.

    ```python
    >>> sp1.completeStatus
    False
    ```

    When we’re done adding elements:

    ```python
    >>> sp1.completeStatus = True
    ```

[`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner") methods

Spanner.\_\_getitem\_\_(*key*)[[source]](../_modules/music21/spanner.html#Spanner.__getitem__)
:   ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> c1 = clef.BassClef()
    >>> sl = spanner.Spanner(n1, n2, c1)
    >>> sl[0] == n1
    True
    >>> sl[-1] == c1
    True
    >>> sl[clef.BassClef][0] == c1
    True
    ```

Spanner.addSpannedElements(*spannedElements: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")] | [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *\*otherElements: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*)[[source]](../_modules/music21/spanner.html#Spanner.addSpannedElements)
:   Associate one or more elements with this Spanner.

    The order in which elements are added is retained and
    may or may not be significant to the spanner.

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> n3 = note.Note('e')
    >>> n4 = note.Note('d-')
    >>> n5 = note.Note('c')
    ```

    ```python
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements(n1)
    >>> sl.addSpannedElements(n2, n3)
    >>> sl.addSpannedElements([n4, n5])
    >>> sl.getSpannedElementIds() == [id(n) for n in [n1, n2, n3, n4, n5]]
    True
    ```

Spanner.fill(*searchStream=None*, *\**, *includeEndBoundary: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *mustFinishInSpan: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *mustBeginInSpan: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *includeElementsThatEndAtStart: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/music21/spanner.html#Spanner.fill)
:   Fills in the intermediate elements of a spanner, that are found in searchStream between
    the first element’s offset and the last element’s offset+duration. If searchStream
    is None, the first element’s activeSite is used. If the first element’s activeSite
    is None, a SpannerException is raised.

    Ottava is an example of a Spanner that can be filled. The Ottava does not need
    to be inserted into the stream in order to be filled.

    ```python
    >>> m = stream.Measure([note.Note('A'), note.Note('B'), note.Note('C')])
    >>> ott1 = spanner.Ottava(m.notes[0], m.notes[2])
    >>> ott1.fill(m)
    >>> ott1
    <music21.spanner.Ottava 8va transposing<...Note A><...Note B><...Note C>>
    ```

    If the searchStream is not passed in, fill still happens in this case, because
    the first note’s activeSite is used instead.

    ```python
    >>> ott2 = spanner.Ottava(m.notes[0], m.notes[2])
    >>> ott2.fill()
    >>> ott2
    <music21.spanner.Ottava 8va transposing<...Note A><...Note B><...Note C>>
    ```

    If the searchStream is not passed, and the spanner’s first element doesn’t have
    an activeSite, a SpannerException is raised.

    ```python
    >>> ott3 = spanner.Ottava(note.Note('D'), note.Note('E'))
    >>> ott3.fill()
    Traceback (most recent call last):
    music21.spanner.SpannerException: Spanner.fill() requires a searchStream
        or getFirst().activeSite
    ```

Spanner.getFirst()[[source]](../_modules/music21/spanner.html#Spanner.getFirst)
:   Get the object of the first spannedElement (or None if it’s an empty spanner)

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> n3 = note.Note('e')
    >>> n4 = note.Note('c')
    >>> n5 = note.Note('d-')
    ```

    ```python
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements(n1, n2, n3, n4, n5)
    >>> sl.getFirst() is n1
    True
    ```

    ```python
    >>> spanner.Slur().getFirst() is None
    True
    ```

Spanner.getLast()[[source]](../_modules/music21/spanner.html#Spanner.getLast)
:   Get the object of the last spannedElement (or None if it’s an empty spanner)

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> n3 = note.Note('e')
    >>> n4 = note.Note('c')
    >>> n5 = note.Note('d-')
    ```

    ```python
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements(n1, n2, n3, n4, n5)
    >>> sl.getLast() is n5
    True
    ```

    ```python
    >>> spanner.Slur().getLast() is None
    True
    ```

Spanner.getSpannedElementIds()[[source]](../_modules/music21/spanner.html#Spanner.getSpannedElementIds)
:   Return all id() for all stored objects.
    Was performance critical, until most uses removed in v7.

    Used only as a testing tool now.
    Spanner.\_\_contains\_\_() was optimized in 839c7e5.

Spanner.getSpannedElements()[[source]](../_modules/music21/spanner.html#Spanner.getSpannedElements)
:   Return all the elements of .spannerStorage for this Spanner
    as a list of Music21Objects.

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements(n1)
    >>> sl.getSpannedElements() == [n1]
    True
    >>> sl.addSpannedElements(n2)
    >>> sl.getSpannedElements() == [n1, n2]
    True
    >>> sl.getSpannedElementIds() == [id(n1), id(n2)]
    True
    >>> c1 = clef.TrebleClef()
    >>> sl.addSpannedElements(c1)
    >>> sl.getSpannedElements() == [n1, n2, c1]  # make sure that not sorting
    True
    ```

Spanner.getSpannedElementsByClass(*classFilterList*)[[source]](../_modules/music21/spanner.html#Spanner.getSpannedElementsByClass)
:   ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> c1 = clef.AltoClef()
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements([n1, n2, c1])
    >>> sl.getSpannedElementsByClass('Note') == [n1, n2]
    True
    >>> sl.getSpannedElementsByClass(clef.Clef) == [c1]
    True
    ```

Spanner.hasSpannedElement(*spannedElement: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/music21/spanner.html#Spanner.hasSpannedElement)
:   Return True if this Spanner has the spannedElement.

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> span = spanner.Spanner()
    >>> span.addSpannedElements(n1)
    >>> span.hasSpannedElement(n1)
    True
    >>> span.hasSpannedElement(n2)
    False
    ```

    Note that a simple in does the same thing:

    ```python
    >>> n1 in span
    True
    >>> n2 in span
    False
    ```

Spanner.insertFirstSpannedElement(*firstEl: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/spanner.html#Spanner.insertFirstSpannedElement)
:   Add a single element as the first in the spanner.

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> n3 = note.Note('e')
    >>> n4 = note.Note('d-')
    >>> n5 = note.Note('c')
    ```

    ```python
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements(n2, n3)
    >>> sl.addSpannedElements([n4, n5])
    >>> sl.insertFirstSpannedElement(n1)
    >>> sl.getSpannedElementIds() == [id(n) for n in [n1, n2, n3, n4, n5]]
    True
    ```

    If the element is already in the spanner, it will not be added again, nor moved.
    (to move it to the front, remove it before running)

    ```python
    >>> sl.insertFirstSpannedElement(n4)
    >>> sl.getSpannedElementIds() == [id(n) for n in [n1, n2, n3, n4, n5]]
    True
    ```

Spanner.isFirst(*spannedElement*)[[source]](../_modules/music21/spanner.html#Spanner.isFirst)
:   Given a spannedElement, is it first?

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> n3 = note.Note('e')
    >>> n4 = note.Note('c')
    >>> n5 = note.Note('d-')
    ```

    ```python
    >>> sl = spanner.Spanner()
    >>> sl.addSpannedElements(n1, n2, n3, n4, n5)
    >>> sl.isFirst(n2)
    False
    >>> sl.isFirst(n1)
    True
    >>> sl.isLast(n1)
    False
    >>> sl.isLast(n5)
    True
    ```

Spanner.isLast(*spannedElement*)[[source]](../_modules/music21/spanner.html#Spanner.isLast)
:   Given a spannedElement, is it last? Returns True or False

Spanner.purgeLocations(*rescanIsDead=False*)[[source]](../_modules/music21/spanner.html#Spanner.purgeLocations)
:   Remove references to all locations in objects that no longer exist.

Spanner.purgeOrphans(*excludeStorageStreams=True*)[[source]](../_modules/music21/spanner.html#Spanner.purgeOrphans)
:   A Music21Object may, due to deep copying or other reasons,
    have a site (with an offset) which
    no longer contains the Music21Object. These lingering sites
    are called orphans. This method gets rid of them.

    The excludeStorageStreams are SpannerStorage and VariantStorage.

Spanner.replaceSpannedElement(*old*, *new*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/music21/spanner.html#Spanner.replaceSpannedElement)
:   When copying a Spanner, we need to update the
    spanner with new references for copied (if the Notes of a
    Slur have been copied, that Slur’s Note references need
    references to the new Notes). Given the old spanned element,
    this method will replace the old with the new.

    The old parameter can be either an object or object id.

    ```python
    >>> n1 = note.Note('g')
    >>> n2 = note.Note('f#')
    >>> c1 = clef.AltoClef()
    >>> c2 = clef.BassClef()
    >>> sl = spanner.Spanner(n1, n2, c1)
    >>> sl.replaceSpannedElement(c1, c2)
    >>> sl[-1] == c2
    True
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Glissando

class music21.spanner.Glissando(*\*spannedElements*, *lineType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'wavy'*, *label: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#Glissando)
:   A between two Notes specifying a glissando or similar alteration.
    Different line types can be specified.

    Glissandos can have a label and a lineType. Label is a string or None.
    lineType defaults to ‘wavy’

    ```python
    >>> gl = spanner.Glissando()
    >>> gl.lineType
    'wavy'
    >>> print(gl.label)
    None
    ```

    ```python
    >>> gl.label = 'gliss.'
    ```

    Note – not a Line subclass for now, but that might change.

[`Glissando`](#music21.spanner.Glissando "music21.spanner.Glissando") bases

* [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Glissando`](#music21.spanner.Glissando "music21.spanner.Glissando") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Glissando`](#music21.spanner.Glissando "music21.spanner.Glissando") read/write properties

Glissando.lineType
:   Get or set the lineType property. See Line for valid line types.

Glissando.slideType
:   Get or set the slideType which determines how
    the glissando or slide is to be played. Values
    are ‘chromatic’ (default), ‘continuous’ (like a slide or smear),
    ‘diatonic’ (like a harp gliss), ‘white’ (meaning a white-key gliss
    as on a marimba), or ‘black’ (black-key gliss).

    ‘continuous’ slides export to MusicXML as a <slide> object.
    All others export as <glissando>.

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Glissando`](#music21.spanner.Glissando "music21.spanner.Glissando") methods

Methods inherited from [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Glissando`](#music21.spanner.Glissando "music21.spanner.Glissando") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Line

class music21.spanner.Line(*\*spannedElements*, *lineType: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'solid'*, *tick: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'down'*, *startTick: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'down'*, *endTick: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'down'*, *startHeight: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *endHeight: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#Line)
:   A line or bracket represented as a spanner above two Notes.

    Brackets can take many line types.

    ```python
    >>> b = spanner.Line()
    >>> b.lineType = 'dotted'
    >>> b.lineType
    'dotted'
    >>> b = spanner.Line(endHeight=20)
    >>> b.endHeight
    20
    ```

[`Line`](#music21.spanner.Line "music21.spanner.Line") bases

* [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Line`](#music21.spanner.Line "music21.spanner.Line") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Line`](#music21.spanner.Line "music21.spanner.Line") read/write properties

Line.endHeight
:   Get or set the endHeight property.

    ```python
    >>> b = spanner.Line()
    >>> b.endHeight = -20
    Traceback (most recent call last):
    music21.spanner.SpannerException: not a valid value: -20
    ```

Line.endTick
:   Get or set the endTick property.

Line.lineType
:   Get or set the lineType property. Valid line types are listed in .validLineTypes.

    ```python
    >>> b = spanner.Line()
    >>> b.lineType = 'dotted'
    >>> b.lineType = 'navyblue'
    Traceback (most recent call last):
    music21.spanner.SpannerException: not a valid value: navyblue
    ```

    ```python
    >>> b.validLineTypes
    ('solid', 'dashed', 'dotted', 'wavy')
    ```

Line.startHeight
:   Get or set the startHeight property.

    ```python
    >>> b = spanner.Line()
    >>> b.startHeight = None
    Traceback (most recent call last):
    music21.spanner.SpannerException: not a valid value: None
    ```

Line.startTick
:   Get or set the startTick property.

Line.tick
:   Set the start and end tick to the same value

    ```python
    >>> b = spanner.Line()
    >>> b.tick = 'arrow'
    >>> b.startTick
    'arrow'
    >>> b.endTick
    'arrow'
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Line`](#music21.spanner.Line "music21.spanner.Line") methods

Methods inherited from [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Line`](#music21.spanner.Line "music21.spanner.Line") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## MultiMeasureRest

class music21.spanner.MultiMeasureRest(*\*spannedElements*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#MultiMeasureRest)
:   A grouping symbol that indicates that a collection of rests lasts
    multiple measures.

[`MultiMeasureRest`](#music21.spanner.MultiMeasureRest "music21.spanner.MultiMeasureRest") bases

* [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`MultiMeasureRest`](#music21.spanner.MultiMeasureRest "music21.spanner.MultiMeasureRest") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`MultiMeasureRest`](#music21.spanner.MultiMeasureRest "music21.spanner.MultiMeasureRest") read/write properties

MultiMeasureRest.numRests
:   Returns the number of measures involved in the
    multi-measure rest.

    Calculated automatically from the number of rests in
    the spanner. Or can be set manually to override the number.

    ```python
    >>> mmr = spanner.MultiMeasureRest()
    >>> for i in range(6):
    ...     mmr.addSpannedElements([note.Rest(type='whole')])
    >>> mmr.numRests
    6
    >>> mmr.numRests = 10
    >>> mmr.numRests
    10
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`MultiMeasureRest`](#music21.spanner.MultiMeasureRest "music21.spanner.MultiMeasureRest") methods

Methods inherited from [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`MultiMeasureRest`](#music21.spanner.MultiMeasureRest "music21.spanner.MultiMeasureRest") instance variables

MultiMeasureRest.maxSymbols
:   An int, specifying the maximum number of rests
    to display as symbols. Default is 11.
    If useSymbols is False then this setting
    does nothing.

    Change defaults.multiMeasureRestMaxSymbols to
    change globally.

MultiMeasureRest.useSymbols
:   Boolean to indicate whether rest symbols
    (breve, longa, etc.) should be used when
    displaying the rest. Your music21 inventor
    is a medievalist, so this defaults to True.

    Change defaults.multiMeasureRestUseSymbols to
    change globally.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Ottava

class music21.spanner.Ottava(*\*spannedElements*, *type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = '8va'*, *transposing: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *placement: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['above', 'below'] = 'above'*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#Ottava)
:   An octave shift line:

    ```python
    >>> ottava = spanner.Ottava(type='8va')
    >>> ottava.type
    '8va'
    >>> ottava.type = 15
    >>> ottava.type
    '15ma'
    >>> ottava.type = (8, 'down')
    >>> ottava.type
    '8vb'
    >>> print(ottava)
    <music21.spanner.Ottava 8vb transposing>
    ```

    An Ottava spanner can either be transposing or non-transposing.
    In a transposing Ottava spanner, the notes in the stream should be
    in their written octave (as if the spanner were not there) and all the
    notes in the spanner will be transposed on Stream.toSoundingPitch().

    A non-transposing spanner has notes that are at the pitch that
    they would sound (therefore the Ottava spanner is a decorative
    line).

    ```python
    >>> ottava.transposing
    True
    >>> n1 = note.Note('D4')
    >>> n2 = note.Note('E4')
    >>> n2.offset = 2.0
    >>> ottava.addSpannedElements([n1, n2])
    ```

    ```python
    >>> s = stream.Stream([ottava, n1, n2])
    >>> s.atSoundingPitch = False
    >>> s2 = s.toSoundingPitch()
    >>> s2.show('text')
    {0.0} <music21.spanner.Ottava 8vb non-transposing<music21.note.Note D><music21.note.Note E>>
    {0.0} <music21.note.Note D>
    {2.0} <music21.note.Note E>
    ```

    ```python
    >>> for n in s2.notes:
    ...     print(n.nameWithOctave)
    D3
    E3
    ```

    All valid types are given below:

    ```python
    >>> ottava.validOttavaTypes
    ('8va', '8vb', '15ma', '15mb', '22da', '22db')
    ```

[`Ottava`](#music21.spanner.Ottava "music21.spanner.Ottava") bases

* [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Ottava`](#music21.spanner.Ottava "music21.spanner.Ottava") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Ottava`](#music21.spanner.Ottava "music21.spanner.Ottava") read/write properties

Ottava.type
:   Get or set Ottava type. This can be set by as complete string
    (such as 8va or 15mb) or with a pair specifying size and direction.

    ```python
    >>> os = spanner.Ottava()
    >>> os.type = '8vb'
    >>> os.type
    '8vb'
    >>> os.type = 15, 'down'
    >>> os.type
    '15mb'
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Ottava`](#music21.spanner.Ottava "music21.spanner.Ottava") methods

Ottava.interval(*reverse=False*)[[source]](../_modules/music21/spanner.html#Ottava.interval)
:   return an interval.Interval() object representing this ottava

    ```python
    >>> ottava = spanner.Ottava(type='15mb')
    >>> i = ottava.interval()
    >>> i
    <music21.interval.Interval P-15>
    ```

Ottava.performTransposition()[[source]](../_modules/music21/spanner.html#Ottava.performTransposition)
:   On a transposing spanner, switch to non-transposing,
    and transpose all notes and chords in the spanner.
    The note/chords will all be transposed to their sounding
    pitch (at least as far as the ottava is concerned;
    transposing instruments are handled separately).

    ```python
    >>> ottava = spanner.Ottava(type='8va')
    >>> n1 = note.Note('D#4')
    >>> n2 = note.Note('E#4')
    >>> ottava.addSpannedElements([n1, n2])
    >>> ottava.transposing
    True
    ```

    ```python
    >>> ottava.performTransposition()
    ```

    ```python
    >>> ottava.transposing
    False
    >>> n1.nameWithOctave
    'D#5'
    ```

Ottava.shiftDirection(*reverse=False*)[[source]](../_modules/music21/spanner.html#Ottava.shiftDirection)
:   Returns up or down depending on the type of shift:

Ottava.shiftMagnitude()[[source]](../_modules/music21/spanner.html#Ottava.shiftMagnitude)
:   Get basic parameters of shift.

    Returns either 8, 15, or 22 depending on the amount of shift

Ottava.undoTransposition()[[source]](../_modules/music21/spanner.html#Ottava.undoTransposition)
:   Change a non-transposing spanner to a transposing spanner,
    and transpose back all the notes and chords in the spanner.
    The notes/chords will all be transposed to their written
    pitch (at least as far as the ottava is concerned;
    transposing instruments are handled separately).

    ```python
    >>> ottava = spanner.Ottava(type='8va')
    >>> n1 = note.Note('D#4')
    >>> n2 = note.Note('E#4')
    >>> ottava.addSpannedElements([n1, n2])
    >>> ottava.transposing = False
    ```

    ```python
    >>> ottava.undoTransposition()
    ```

    ```python
    >>> ottava.transposing
    True
    >>> n1.nameWithOctave
    'D#3'
    ```

Methods inherited from [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Ottava`](#music21.spanner.Ottava "music21.spanner.Ottava") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## PendingAssignmentRef

class music21.spanner.PendingAssignmentRef(*spanner: [Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")*, *className: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offsetInScore: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/spanner.html#PendingAssignmentRef)
:   A dataclass containing information about a pending first spanned element assignment.
    See [`SpannerBundle.setPendingSpannedElementAssignment()`](#music21.spanner.SpannerBundle.setPendingSpannedElementAssignment "music21.spanner.SpannerBundle.setPendingSpannedElementAssignment") for documentation
    and tests.

[`PendingAssignmentRef`](#music21.spanner.PendingAssignmentRef "music21.spanner.PendingAssignmentRef") methods

PendingAssignmentRef.\_\_eq\_\_(*other*)
:   Return self==value.

## RepeatBracket

class music21.spanner.RepeatBracket(*\*spannedElements*, *number: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = 0*, *overrideDisplay: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#RepeatBracket)
:   A grouping of one or more measures, presumably in sequence, that mark an alternate repeat.

    These gather what are sometimes called first-time bars and second-time bars.

    It is assumed that numbering starts from 1. Numberings above 2 are permitted.
    The number keyword argument can be used to pass in the desired number.

    overrideDisplay if set will display something other than the number. For instance
    ouvert and clos for medieval music. However, if you use it for something like ‘1-3’
    be sure to set number properly too.

    ```python
    >>> m = stream.Measure()
    >>> sp = spanner.RepeatBracket(m, number=1)
    >>> sp  # can be one or more measures
    <music21.spanner.RepeatBracket 1 <music21.stream.Measure 0 offset=0.0>>
    ```

    ```python
    >>> sp.number = 3
    >>> sp
    <music21.spanner.RepeatBracket 3 <music21.stream.Measure 0 offset=0.0>>
    >>> sp.numberRange  # the list of repeat numbers
    [3]
    >>> sp.number
    '3'
    ```

    Range of repeats as string:

    ```python
    >>> sp.number = '1-3'
    >>> sp.numberRange
    [1, 2, 3]
    >>> sp.number
    '1-3'
    ```

    Range of repeats as list:

    ```python
    >>> sp.number = [2, 3]
    >>> sp.numberRange
    [2, 3]
    >>> sp.number
    '2, 3'
    ```

    Comma separated numbers:

    ```python
    >>> sp.number = '1, 2, 3'
    >>> sp.numberRange
    [1, 2, 3]
    >>> sp.number
    '1-3'
    ```

    Disjunct numbers:

    ```python
    >>> sp.number = '1, 2, 3, 7'
    >>> sp.numberRange
    [1, 2, 3, 7]
    >>> sp.number
    '1, 2, 3, 7'
    ```

    Override the display.

    ```python
    >>> sp.overrideDisplay = '1-3, 7'
    >>> sp
    <music21.spanner.RepeatBracket 1-3, 7
         <music21.stream.Measure 0 offset=0.0>>
    ```

    number is not affected by display overrides:

    ```python
    >>> sp.number
    '1, 2, 3, 7'
    ```

[`RepeatBracket`](#music21.spanner.RepeatBracket "music21.spanner.RepeatBracket") bases

* [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`RepeatBracket`](#music21.spanner.RepeatBracket "music21.spanner.RepeatBracket") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`RepeatBracket`](#music21.spanner.RepeatBracket "music21.spanner.RepeatBracket") read/write properties

RepeatBracket.number
:   Get or set the number – returning a string always.

    ```python
    >>> rb = spanner.RepeatBracket()
    >>> rb.number
    ''
    >>> rb.number = '5-7'
    >>> rb.number
    '5-7'
    >>> rb.numberRange
    [5, 6, 7]
    >>> rb.number = 1
    ```

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`RepeatBracket`](#music21.spanner.RepeatBracket "music21.spanner.RepeatBracket") methods

Methods inherited from [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`RepeatBracket`](#music21.spanner.RepeatBracket "music21.spanner.RepeatBracket") instance variables

RepeatBracket.numberRange
:   Get a contiguous list of repeat numbers that are applicable for this instance.

    Will always have at least one element, but [0] means undefined

    ```python
    >>> rb = spanner.RepeatBracket()
    >>> rb.numberRange
    [0]
    ```

    ```python
    >>> rb.number = '1,2'
    >>> rb.numberRange
    [1, 2]
    ```

RepeatBracket.overrideDisplay
:   Override the string representation of this bracket, or use
    None to not override.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## Slur

class music21.spanner.Slur(*\*spannedElements*, *\*\*keywords*)[[source]](../_modules/music21/spanner.html#Slur)
:   A slur represented as a spanner between two Notes.

    Slurs have .placement options (‘above’ or ‘below’) and .lineType (‘dashed’ or None)

[`Slur`](#music21.spanner.Slur "music21.spanner.Slur") bases

* [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner")
* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`Slur`](#music21.spanner.Slur "music21.spanner.Slur") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`Slur`](#music21.spanner.Slur "music21.spanner.Slur") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`Slur`](#music21.spanner.Slur "music21.spanner.Slur") methods

Methods inherited from [`Spanner`](#music21.spanner.Spanner "music21.spanner.Spanner"):

|  |  |  |
| --- | --- | --- |
| * [`__getitem__()`](#music21.spanner.Spanner.__getitem__ "music21.spanner.Spanner.__getitem__") * [`addSpannedElements()`](#music21.spanner.Spanner.addSpannedElements "music21.spanner.Spanner.addSpannedElements") * [`fill()`](#music21.spanner.Spanner.fill "music21.spanner.Spanner.fill") * [`getFirst()`](#music21.spanner.Spanner.getFirst "music21.spanner.Spanner.getFirst") * [`getLast()`](#music21.spanner.Spanner.getLast "music21.spanner.Spanner.getLast") | * [`getSpannedElementIds()`](#music21.spanner.Spanner.getSpannedElementIds "music21.spanner.Spanner.getSpannedElementIds") * [`getSpannedElements()`](#music21.spanner.Spanner.getSpannedElements "music21.spanner.Spanner.getSpannedElements") * [`getSpannedElementsByClass()`](#music21.spanner.Spanner.getSpannedElementsByClass "music21.spanner.Spanner.getSpannedElementsByClass") * [`hasSpannedElement()`](#music21.spanner.Spanner.hasSpannedElement "music21.spanner.Spanner.hasSpannedElement") * [`insertFirstSpannedElement()`](#music21.spanner.Spanner.insertFirstSpannedElement "music21.spanner.Spanner.insertFirstSpannedElement") | * [`isFirst()`](#music21.spanner.Spanner.isFirst "music21.spanner.Spanner.isFirst") * [`isLast()`](#music21.spanner.Spanner.isLast "music21.spanner.Spanner.isLast") * [`purgeLocations()`](#music21.spanner.Spanner.purgeLocations "music21.spanner.Spanner.purgeLocations") * [`purgeOrphans()`](#music21.spanner.Spanner.purgeOrphans "music21.spanner.Spanner.purgeOrphans") * [`replaceSpannedElement()`](#music21.spanner.Spanner.replaceSpannedElement "music21.spanner.Spanner.replaceSpannedElement") |

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") | * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") | * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`Slur`](#music21.spanner.Slur "music21.spanner.Slur") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SpannerAnchor

class music21.spanner.SpannerAnchor(*\*\*keywords*)[[source]](../_modules/music21/spanner.html#SpannerAnchor)
:   A simple Music21Object that can be used to define the beginning or end
    of a Spanner, in the place of a GeneralNote.

    This is useful for (e.g.) a Crescendo that ends partway through a
    note (e.g. in a violin part). Exporters (like MusicXML) are configured
    to remove the SpannerAnchor itself on output, exporting only the Spanner
    start and stop locations.

    Here’s an example of a whole note that has a Crescendo for the first
    half of the note, and a Diminuendo for the second half of the note.

    ```python
    >>> n = note.Note('C4', quarterLength=4)
    >>> measure = stream.Measure([n], number=1)
    >>> part = stream.Part([measure], id='violin')
    >>> score = stream.Score([part])
    ```

    Add a crescendo from the note’s start to the first anchor, place in the
    middle of the note, and then a diminuendo from that first anchor to the
    second, placed at the end of the note.

    ```python
    >>> anchor1 = spanner.SpannerAnchor()
    >>> anchor2 = spanner.SpannerAnchor()
    >>> measure.insert(2.0, anchor1)
    >>> measure.insert(4.0, anchor2)
    >>> cresc = dynamics.Crescendo(n, anchor1)
    >>> dim = dynamics.Diminuendo(anchor1, anchor2)
    >>> score.append((cresc, dim))
    >>> score.show('text')
    {0.0} <music21.stream.Part violin>
        {0.0} <music21.stream.Measure 1 offset=0.0>
            {0.0} <music21.note.Note C>
            {2.0} <music21.spanner.SpannerAnchor at 2.0>
            {4.0} <music21.spanner.SpannerAnchor at 4.0>
    {4.0} <music21.dynamics.Crescendo <music21.note.Note C><...SpannerAnchor at 2.0>>
    {4.0} <music21.dynamics.Diminuendo <...SpannerAnchor at 2.0><...SpannerAnchor at 4.0>>
    ```

[`SpannerAnchor`](#music21.spanner.SpannerAnchor "music21.spanner.SpannerAnchor") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpannerAnchor`](#music21.spanner.SpannerAnchor "music21.spanner.SpannerAnchor") read-only properties

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SpannerAnchor`](#music21.spanner.SpannerAnchor "music21.spanner.SpannerAnchor") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`SpannerAnchor`](#music21.spanner.SpannerAnchor "music21.spanner.SpannerAnchor") methods

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`SpannerAnchor`](#music21.spanner.SpannerAnchor "music21.spanner.SpannerAnchor") instance variables

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## SpannerBundle

class music21.spanner.SpannerBundle(*spanners: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/spanner.html#SpannerBundle)
:   An advanced utility object for collecting and processing
    collections of Spanner objects. This is necessary because
    often processing routines that happen at many
    levels still need access to the same collection of spanners.

    Because SpannerBundles are so commonly used with
    `Stream` objects, the Stream has a
    `spannerBundle` property that stores
    and caches a SpannerBundle of the Stream.

    If a Stream or Stream subclass is provided as an argument,
    all Spanners on this Stream will be accumulated herein.

    Not to be confused with SpannerStorage (which is a Stream class inside
    a spanner that stores Elements that are spanned)

    * Changed in v7: only argument must be a List of spanners.
      Creators of SpannerBundles are required to check that this constraint is True

[`SpannerBundle`](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle") bases

* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`SpannerBundle`](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle") read-only properties

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`SpannerBundle`](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle") methods

SpannerBundle.\_\_getitem\_\_(*key*) → [Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")[[source]](../_modules/music21/spanner.html#SpannerBundle.__getitem__)

SpannerBundle.append(*other: [Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")*)[[source]](../_modules/music21/spanner.html#SpannerBundle.append)
:   adds a Spanner to the bundle. Will be done automatically when adding a Spanner
    to a Stream.

SpannerBundle.freePendingSpannedElementAssignment(*spannedElementCandidate*, *offsetInScore: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/music21/spanner.html#SpannerBundle.freePendingSpannedElementAssignment)
:   Assigns and frees up a pendingSpannedElementAssignment if one
    is active and the candidate matches the class (and offsetInScore,
    if specified). See setPendingSpannedElementAssignment for
    documentation and tests.

    It is set up via a first-in, first-out priority.

SpannerBundle.getByClass(*searchClass: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[type](moduleBar.html#music21.bar.Barline.type "music21.bar.Barline.type"), ...]*) → [SpannerBundle](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")[[source]](../_modules/music21/spanner.html#SpannerBundle.getByClass)
:   Given a spanner class, return a new SpannerBundle of all Spanners of the desired class.

    ```python
    >>> su1 = spanner.Slur()
    >>> su2 = layout.StaffGroup()
    >>> su3 = layout.StaffGroup()
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> sb.append(su3)
    ```

    searchClass should be a Class.

    ```python
    >>> slurs = sb.getByClass(spanner.Slur)
    >>> slurs
    <music21.spanner.SpannerBundle of size 1>
    >>> list(slurs) == [su1]
    True
    >>> list(sb.getByClass(spanner.Slur)) == [su1]
    True
    >>> list(sb.getByClass(layout.StaffGroup)) == [su2, su3]
    True
    ```

    A tuple of classes can also be given:

    ```python
    >>> len(sb.getByClass((spanner.Slur, layout.StaffGroup)))
    3
    ```

    Note that the ability to search via a string will be removed in
    version 10.

SpannerBundle.getByClassIdLocalComplete(*className*, *idLocal*, *completeStatus*)[[source]](../_modules/music21/spanner.html#SpannerBundle.getByClassIdLocalComplete)
:   Get all spanners of a specified class className, an id idLocal, and a completeStatus.
    This is a convenience routine for multiple filtering when searching for relevant Spanners
    to pair with.

    ```python
    >>> su1 = spanner.Slur()
    >>> su2 = layout.StaffGroup()
    >>> su2.idLocal = 3
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> list(sb.getByClassIdLocalComplete(layout.StaffGroup, 3, False)) == [su2]
    True
    >>> su2.completeStatus = True
    >>> list(sb.getByClassIdLocalComplete(layout.StaffGroup, 3, False)) == []
    True
    ```

SpannerBundle.getByCompleteStatus(*completeStatus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [SpannerBundle](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")[[source]](../_modules/music21/spanner.html#SpannerBundle.getByCompleteStatus)
:   Get spanners by matching status of completeStatus to the same attribute

    ```python
    >>> su1 = spanner.Slur()
    >>> su1.idLocal = 1
    >>> su1.completeStatus = True
    >>> su2 = spanner.Slur()
    >>> su2.idLocal = 2
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> sb2 = sb.getByCompleteStatus(True)
    >>> len(sb2)
    1
    >>> sb2 = sb.getByIdLocal(1).getByCompleteStatus(True)
    >>> sb2[0] == su1
    True
    ```

SpannerBundle.getByIdLocal(*idLocal: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [SpannerBundle](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")[[source]](../_modules/music21/spanner.html#SpannerBundle.getByIdLocal)
:   Get spanners by idLocal.

    Returns a new SpannerBundle object

    ```python
    >>> su = spanner.Slur()
    >>> su.idLocal = 1
    >>> rb = spanner.RepeatBracket()
    >>> rb.idLocal = 2
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su)
    >>> sb.append(rb)
    >>> len(sb)
    2
    ```

    ```python
    >>> sb.getByIdLocal(2)
    <music21.spanner.SpannerBundle of size 1>
    >>> sb.getByIdLocal(2)[0]
    <music21.spanner.RepeatBracket >
    ```

    ```python
    >>> len(sb.getByIdLocal(1))
    1
    ```

    ```python
    >>> sb.getByIdLocal(3)
    <music21.spanner.SpannerBundle of size 0>
    ```

SpannerBundle.getBySpannedElement(*spannedElement: [Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")*) → [SpannerBundle](#music21.spanner.SpannerBundle "music21.spanner.SpannerBundle")[[source]](../_modules/music21/spanner.html#SpannerBundle.getBySpannedElement)
:   Given a spanner spannedElement (an object),
    return a new SpannerBundle of all Spanner objects that
    have this object as a spannedElement.

    ```python
    >>> n1 = note.Note()
    >>> n2 = note.Note()
    >>> n3 = note.Note()
    >>> su1 = spanner.Slur(n1, n2)
    >>> su2 = spanner.Slur(n2, n3)
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> list(sb.getBySpannedElement(n1)) == [su1]
    True
    >>> list(sb.getBySpannedElement(n2)) == [su1, su2]
    True
    >>> list(sb.getBySpannedElement(n3)) == [su2]
    True
    ```

SpannerBundle.getSpannerStorageIds() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/music21/spanner.html#SpannerBundle.getSpannerStorageIds)
:   Return all SpannerStorage ids from all contained Spanners

SpannerBundle.popPendingSpannedElementAssignments() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PendingAssignmentRef](#music21.spanner.PendingAssignmentRef "music21.spanner.PendingAssignmentRef")][[source]](../_modules/music21/spanner.html#SpannerBundle.popPendingSpannedElementAssignments)
:   Removes and returns all pendingSpannedElementAssignments.
    This can be called when there will be no more calls to
    freePendingSpannedElementAssignment, and SpannerAnchors
    need to be created for each remaining pending assignment.
    The SpannerAnchors should be created at the appropriate
    offset, dictated by the assignment’s offsetInScore.

    ```python
    >>> sb = spanner.SpannerBundle()
    >>> sl = spanner.Slur()
    >>> sb.append(sl)
    >>> sb.setPendingSpannedElementAssignment(sl, 'Note', 0.0)
    PendingAssignmentRef(spanner=<music21.spanner.Slur>,
                         className='Note', offsetInScore=0.0)
    ```

    popPendingSpannedElementAssignments returns the full list and leaves
    an empty list behind:

    ```python
    >>> expectedPending = list(sb._pendingSpannedElementAssignment)
    >>> pending = sb.popPendingSpannedElementAssignments()
    >>> pending == expectedPending
    True
    >>> sb._pendingSpannedElementAssignment
    []
    ```

SpannerBundle.remove(*item: [Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")*)[[source]](../_modules/music21/spanner.html#SpannerBundle.remove)
:   Remove a stored Spanner from the bundle with an instance.
    Each reference must have a matching id() value.

    ```python
    >>> su1 = spanner.Slur()
    >>> su1.idLocal = 1
    >>> su2 = spanner.Slur()
    >>> su2.idLocal = 2
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> len(sb)
    2
    >>> sb
    <music21.spanner.SpannerBundle of size 2>
    ```

    ```python
    >>> sb.remove(su2)
    >>> len(sb)
    1
    ```

SpannerBundle.replaceSpannedElement(*old: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*, *new: [Music21Object](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")][[source]](../_modules/music21/spanner.html#SpannerBundle.replaceSpannedElement)
:   Given a spanner spannedElement (an object), replace all old spannedElements
    with new spannedElements
    for all Spanner objects contained in this bundle.

    The old parameter must be an object, not an object id.

    If no replacements are found, no errors are raised.

    Returns a list of spanners that had elements replaced.

    ```python
    >>> n1 = note.Note('C')
    >>> n2 = note.Note('D')
    >>> su1 = spanner.Line(n1, n2)
    >>> su2 = spanner.Glissando(n2, n1)
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    ```

    ```python
    >>> su1
    <music21.spanner.Line <music21.note.Note C><music21.note.Note D>>
    >>> su2
    <music21.spanner.Glissando <music21.note.Note D><music21.note.Note C>>
    ```

    ```python
    >>> n3 = note.Note('E')
    >>> replacedSpanners = sb.replaceSpannedElement(n2, n3)
    >>> replacedSpanners == [su1, su2]
    True
    ```

    ```python
    >>> su1
    <music21.spanner.Line <music21.note.Note C><music21.note.Note E>>
    >>> su2
    <music21.spanner.Glissando <music21.note.Note E><music21.note.Note C>>
    ```

    * Changed in v7: id() is no longer allowed for old.

    ```python
    >>> sb.replaceSpannedElement(id(n1), n2)
    Traceback (most recent call last):
    TypeError: send elements to replaceSpannedElement(), not ids.
    ```

SpannerBundle.setIdLocalByClass(*className*, *maxId=6*)[[source]](../_modules/music21/spanner.html#SpannerBundle.setIdLocalByClass)
:   (See [`setIdLocals()`](#music21.spanner.SpannerBundle.setIdLocals "music21.spanner.SpannerBundle.setIdLocals") for an explanation of what an idLocal is.)

    Automatically set idLocal values for all members of the provided class.
    This is necessary in cases where spanners are newly created in
    potentially overlapping boundaries and need to be tagged for MusicXML
    or other output. Note that, if some Spanners already have idLocals,
    they will be overwritten.

    The maxId parameter sets the largest number that is available for this
    class. In MusicXML it is 6.

    Currently, this method just iterates over the spanners of this class
    and counts the number from 1-6 and then recycles numbers. It does
    not check whether more than 6 overlapping spanners of the same type
    exist, nor does it reset the count to 1 after all spanners of that
    class have been closed. The example below demonstrates that the
    position of the contents of the spanner have no bearing on
    its idLocal (since we don’t even put anything into the spanners).

    ```python
    >>> su1 = spanner.Slur()
    >>> su2 = layout.StaffGroup()
    >>> su3 = spanner.Slur()
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> sb.append(su3)
    >>> [sp.idLocal for sp in sb.getByClass(spanner.Slur)]
    [None, None]
    >>> sb.setIdLocalByClass('Slur')
    >>> [sp.idLocal for sp in sb.getByClass(spanner.Slur)]
    [1, 2]
    ```

SpannerBundle.setIdLocals()[[source]](../_modules/music21/spanner.html#SpannerBundle.setIdLocals)
:   Utility method for outputting MusicXML (and potentially
    other formats) for spanners.

    Each Spanner type (slur, line, glissando, etc.) in MusicXML
    has a number assigned to it.
    We call this number, idLocal. idLocal is a number from 1 to 6.
    This does not mean that your piece can only have six slurs total!
    But it does mean that within a single
    part, only up to 6 slurs can happen simultaneously.
    But as soon as a slur stops, its idLocal can be reused.

    This method sets all idLocals for all classes in this SpannerBundle.
    This will assure that each class has a unique idLocal number.

    Calling this method is destructive: existing idLocal values will be lost.

    ```python
    >>> su1 = spanner.Slur()
    >>> su2 = layout.StaffGroup()
    >>> su3 = spanner.Slur()
    >>> sb = spanner.SpannerBundle()
    >>> sb.append(su1)
    >>> sb.append(su2)
    >>> sb.append(su3)
    >>> [sp.idLocal for sp in sb.getByClass('Slur')]
    [None, None]
    >>> sb.setIdLocals()
    >>> [(sp, sp.idLocal) for sp in sb]
    [(<music21.spanner.Slur>, 1),
     (<music21.layout.StaffGroup>, 1),
     (<music21.spanner.Slur>, 2)]
    ```

    [`DynamicWedge`](moduleDynamics.html#music21.dynamics.DynamicWedge "music21.dynamics.DynamicWedge") objects are commingled. That is,
    [`Crescendo`](moduleDynamics.html#music21.dynamics.Crescendo "music21.dynamics.Crescendo") and
    [`Diminuendo`](moduleDynamics.html#music21.dynamics.Diminuendo "music21.dynamics.Diminuendo")
    are not numbered separately:

    ```python
    >>> sb2 = spanner.SpannerBundle()
    >>> c = dynamics.Crescendo()
    >>> d = dynamics.Diminuendo()
    >>> sb2.append(c)
    >>> sb2.append(d)
    >>> sb2.setIdLocals()
    >>> [(sp, sp.idLocal) for sp in sb2]
    [(<music21.dynamics.Crescendo>, 1),
     (<music21.dynamics.Diminuendo>, 2)]
    ```

SpannerBundle.setPendingSpannedElementAssignment(*sp: [Spanner](#music21.spanner.Spanner "music21.spanner.Spanner")*, *className: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *offsetInScore: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PendingAssignmentRef](#music21.spanner.PendingAssignmentRef "music21.spanner.PendingAssignmentRef")[[source]](../_modules/music21/spanner.html#SpannerBundle.setPendingSpannedElementAssignment)
:   A SpannerBundle can be set up so that a particular spanner (sp) is looking
    for an element of class (className) to be set as first element. Any future
    element that matches the className (and offsetInScore, if specified)
    which is passed to the SpannerBundle via freePendingSpannedElementAssignment()
    will get it.

    Call popPendingSpannedElementAssignments after parsing to
    recover pending spanners that never matched their expected elements
    — e.g., a MusicXML <direction> whose
    <offset> lands between notes, needing a SpannerAnchor instead.

    First, let’s see the usage without an explicit offset:

    Create some notes and a rest.

    ```python
    >>> n1 = note.Note('C')
    >>> r1 = note.Rest()
    >>> n2 = note.Note('D')
    ```

    Notes start without any associated spanners.

    ```python
    >>> n1.getSpannerSites()
    []
    ```

    Create an empty Slur and a SpannerBundle to hold it.

    ```python
    >>> su1 = spanner.Slur()
    >>> sb1 = spanner.SpannerBundle()
    >>> sb1.append(su1)
    >>> su1.getSpannedElements()
    []
    ```

    Now call this method to register su1 as awaiting the next note element.
    The method returns a PendingAssignmentRef (frozen dataclass) with information
    about what is registered as pending assignment.

    ```python
    >>> sb1.setPendingSpannedElementAssignment(su1, 'Note')
    PendingAssignmentRef(spanner=<music21.spanner.Slur>,
                         className='Note', offsetInScore=None)
    ```

    Elements are then potentially added to spanners by calling
    freePendingSpannedElementAssignment on the SpannerBundle.

    That method will not attach a rest like r1 because it is not a ‘Note’:

    ```python
    >>> sb1.freePendingSpannedElementAssignment(r1)
    >>> r1 in su1
    False
    ```

    But the next Note will be attached:

    ```python
    >>> sb1.freePendingSpannedElementAssignment(n1)
    >>> su1
    <music21.spanner.Slur <music21.note.Note C>>
    >>> n1 in su1
    True
    >>> n1.getSpannerSites()
    [<music21.spanner.Slur <music21.note.Note C>>]
    ```

    Once the pending assignment has been satisfied, the registration is cleared
    from the SpannerBundle, so no future notes that would have satisfied the assignment
    get assigned:

    ```python
    >>> sb1.freePendingSpannedElementAssignment(n2)
    >>> n2 in su1
    False
    >>> n2.getSpannerSites()
    []
    ```

    And we can see that the SpannerBundle sb1 has no spanners still awaiting (pending)
    elements to assign:

    ```python
    >>> sb1.popPendingSpannedElementAssignments()
    []
    ```

    Now a similar example using offsetInScore. When offsetInScore is
    specified at registration, only candidates passed with a matching
    offset to freePendingSpannedElementAssignment will be attached.

    Create two notes and a rest.

    ```python
    >>> n3 = note.Note('C#')
    >>> wrongOffsetNote = note.Note('B')
    >>> r2 = note.Rest()
    ```

    Create a slur with n3 already in it.

    ```python
    >>> sb2 = spanner.SpannerBundle()
    >>> su2 = spanner.Slur([n3])
    >>> sb2.append(su2)
    >>> su2.getSpannedElements()
    [<music21.note.Note C#>]
    ```

    Register su2 as pending and looking for the next Note at offset 4.0:

    ```python
    >>> ref = sb2.setPendingSpannedElementAssignment(su2, 'Note', 4.0)
    >>> ref
    PendingAssignmentRef(spanner=<music21.spanner.Slur <music21.note.Note C#>>,
                         className='Note', offsetInScore=4.0)
    ```

    Call freePendingSpannedElementAssignment to attach an element of the right class
    and offset. Note that the offset must be passed to the method; it is not
    necessarily the offset of the object itself (most often it is the offsetInHierarchy
    of the Part object).

    A note offered at the wrong offset is not attached:

    ```python
    >>> sb2.freePendingSpannedElementAssignment(wrongOffsetNote, 5.0)
    >>> wrongOffsetNote in su2
    False
    ```

    (Passing an offset here is important since, when parsing MusicXML,
    if a <direction> has <offset> specified, the next note might not be the one
    at the start of the spanner)

    The freePending method will not get a rest even at the correct offsetInScore
    because it is not the class being searched for.

    ```python
    >>> sb2.freePendingSpannedElementAssignment(r2, 4.0)
    >>> r2 in su2
    False
    ```

    We are all out of possible notes, we can see which PendingAssignmentRef elements
    are still awaiting elements to attach to. In this case, there is one, our
    Slur:

    ```python
    >>> unmatched_pendingAssignmentRefs = sb2.popPendingSpannedElementAssignments()
    >>> len(unmatched_pendingAssignmentRefs)
    1
    >>> unmatched_pendingAssignmentRefs[0]
    PendingAssignmentRef(spanner=<music21.spanner.Slur <music21.note.Note C#>>,
                         className='Note', offsetInScore=4.0)
    >>> unmatched_pendingAssignmentRefs[0].spanner is su2
    True
    ```

    Parsers can use the information from the unmatched PendingAssignmentRef to
    add additional elements to the score at places where a match was expected.
    Given this ref, the most logical choice would be to create a SpannerAnchor
    object and put it at score offset 4.0 and insert it as the spanner’s first element
    with insertFirstSpannedElement.

    (If a parser needs more information about where the Spanner and SpannerAnchor
    should go, such as a staff number, etc. it can keep a dictionary mapping
    id(PendingAssignmentRef) to a staffKey, etc.)

    And now the happy path: a pending assignment that finds a matching note
    with the right offset. (We’ll demonstrate also that you need to pass
    in your own fractions.)

    ```python
    >>> frac = common.numberTools.opFrac
    >>> n4 = note.Note('G')
    >>> n5 = note.Note('A')
    >>> su3 = spanner.Slur([n4])
    >>> sb3 = spanner.SpannerBundle()
    >>> sb3.append(su3)
    >>> _ = sb3.setPendingSpannedElementAssignment(su3, 'Note', frac(77.33333))
    >>> sb3.freePendingSpannedElementAssignment(n5, frac(77.33333))
    >>> su3
    <music21.spanner.Slur <music21.note.Note A><music21.note.Note G>>
    >>> n5 in su3
    True
    ```

    An important detail demonstrated above is that a freed element is always inserted as the
    first element of the spanner, even when the spanner already has
    other elements. (Note A is before note G in the slur).
    The insert-at-front behavior is important for MusicXML parsing, since
    a <direction> specified is often encountered before
    the note that should *start* the spanner (because of voices, other classes, etc.),
    so when the starting note arrives it needs to go to the start.
