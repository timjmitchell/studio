Source: https://music21.org/music21docs/moduleReference/moduleSearchSerial.html

# music21.search.serial

## ContiguousSegmentOfNotes

class music21.search.serial.ContiguousSegmentOfNotes(*segment=None*, *containerStream=None*, *partNumber=0*, *\*\*keywords*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentOfNotes)
:   Class whose instantiations represent contiguous segments of notes and chords appearing
    within a `Stream`. Generally speaking, these objects are instantiated
    internally, though it is possible
    for the user to create them as well.

    ```python
    >>> s = stream.Stream()
    >>> p = stream.Part()
    >>> n1 = note.Note('c4')
    >>> n2 = note.Note('d4')
    >>> p.append(n1)
    >>> p.append(n2)
    >>> p = p.makeMeasures()
    >>> s.insert(0, p)
    >>> cdContiguousSegment = search.serial.ContiguousSegmentOfNotes([n1, n2], s, 0)
    >>> cdContiguousSegment
    <music21.search.serial.ContiguousSegmentOfNotes ['C4', 'D4']>
    ```

[`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") bases

* [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object")
* [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object")

[`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") read-only properties

ContiguousSegmentOfNotes.originalCenteredTransformationsFromMatched
:   The list of original-centered transformations taking a segment being
    searched for to a found segment, for example, in
    `findTransformedSegments()`.
    For an explanation of the
    zero-centered convention for serial transformations, see
    `music21.search.serial.ToneRow.originalCenteredTransformation()`.

ContiguousSegmentOfNotes.startMeasureNumber
:   The measure number on which the contiguous segment begins.

ContiguousSegmentOfNotes.startOffset
:   The offset of the beginning of the contiguous segment,
    with respect to the measure containing the first note.

ContiguousSegmentOfNotes.zeroCenteredTransformationsFromMatched
:   The list of zero-centered transformations taking a segment being searched
    for to a found segment, for example, in
    `findTransformedSegments()`.
    For an explanation of the zero-centered convention for serial transformations,
    see `music21.search.serial.ToneRow.zeroCenteredTransformation()`.

Read-only properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`beat`](moduleBase.html#music21.base.Music21Object.beat "music21.base.Music21Object.beat") * [`beatDuration`](moduleBase.html#music21.base.Music21Object.beatDuration "music21.base.Music21Object.beatDuration") * [`beatStr`](moduleBase.html#music21.base.Music21Object.beatStr "music21.base.Music21Object.beatStr") | * [`beatStrength`](moduleBase.html#music21.base.Music21Object.beatStrength "music21.base.Music21Object.beatStrength") * [`hasEditorialInformation`](moduleBase.html#music21.base.Music21Object.hasEditorialInformation "music21.base.Music21Object.hasEditorialInformation") | * [`hasStyleInformation`](moduleBase.html#music21.base.Music21Object.hasStyleInformation "music21.base.Music21Object.hasStyleInformation") * [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") |

Read-only properties inherited from [`ProtoM21Object`](modulePrebase.html#music21.prebase.ProtoM21Object "music21.prebase.ProtoM21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSet`](modulePrebase.html#music21.prebase.ProtoM21Object.classSet "music21.prebase.ProtoM21Object.classSet") | * [`classes`](modulePrebase.html#music21.prebase.ProtoM21Object.classes "music21.prebase.ProtoM21Object.classes") |  |

[`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") read/write properties

Read/write properties inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`activeSite`](moduleBase.html#music21.base.Music21Object.activeSite "music21.base.Music21Object.activeSite") * [`derivation`](moduleBase.html#music21.base.Music21Object.derivation "music21.base.Music21Object.derivation") * [`duration`](moduleBase.html#music21.base.Music21Object.duration "music21.base.Music21Object.duration") * [`editorial`](moduleBase.html#music21.base.Music21Object.editorial "music21.base.Music21Object.editorial") | * [`id`](moduleBase.html#music21.base.Music21Object.id "music21.base.Music21Object.id") * [`offset`](moduleBase.html#music21.base.Music21Object.offset "music21.base.Music21Object.offset") * [`priority`](moduleBase.html#music21.base.Music21Object.priority "music21.base.Music21Object.priority") | * [`quarterLength`](moduleBase.html#music21.base.Music21Object.quarterLength "music21.base.Music21Object.quarterLength") * [`seconds`](moduleBase.html#music21.base.Music21Object.seconds "music21.base.Music21Object.seconds") * [`style`](moduleBase.html#music21.base.Music21Object.style "music21.base.Music21Object.style") |

[`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") methods

ContiguousSegmentOfNotes.getActiveMatchedRows()[[source]](../_modules/music21/search/serial.html#ContiguousSegmentOfNotes.getActiveMatchedRows)
:   Returns two ToneRow objects, the activeSegment as ToneRow
    and the matchedSegment as ToneRow

ContiguousSegmentOfNotes.getDistinctPitchClasses()[[source]](../_modules/music21/search/serial.html#ContiguousSegmentOfNotes.getDistinctPitchClasses)
:   Returns a list of distinct pitch classes in the segment, in order of appearance,
    where pitches in a chord are read from bottom to top.

    Does not sort or order.

    ```python
    >>> sc = stream.Score()
    >>> n1 = note.Note('d4')
    >>> n1.quarterLength = 1
    >>> c = chord.Chord(['d4', 'e4', 'g4', 'd5'])
    >>> c.quarterLength = 1
    >>> sc.append(n1)
    >>> sc.append(c)
    >>> sc = sc.makeMeasures()
    >>> searcher = search.serial.ContiguousSegmentSearcher(sc)
    >>> segmentList = searcher.byLength(4)
    >>> csn = segmentList[0]
    >>> csn.getDistinctPitchClasses()
    [2, 4, 7]
    ```

ContiguousSegmentOfNotes.readPitchClassesFromBottom()[[source]](../_modules/music21/search/serial.html#ContiguousSegmentOfNotes.readPitchClassesFromBottom)
:   Returns the list of pitch classes in the segment, reading pitches within
    chords from bottom to top.

    ```python
    >>> sc = stream.Score()
    >>> n1 = note.Note('d4')
    >>> n1.quarterLength = 1
    >>> Cmaj = chord.Chord(['c5', 'e4', 'g4'])
    >>> Cmaj.quarterLength = 1
    >>> sc.append(n1)
    >>> sc.append(Cmaj)
    >>> sc = sc.makeMeasures()
    >>> searcher = search.serial.ContiguousSegmentSearcher(sc)
    >>> segmentList = searcher.byLength(4)
    >>> csn = segmentList[0]
    >>> csn.readPitchClassesFromBottom()
    [2, 0, 4, 7]
    ```

Methods inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`__eq__()`](moduleBase.html#music21.base.Music21Object.__eq__ "music21.base.Music21Object.__eq__") * [`clearCache()`](moduleBase.html#music21.base.Music21Object.clearCache "music21.base.Music21Object.clearCache") * [`containerHierarchy()`](moduleBase.html#music21.base.Music21Object.containerHierarchy "music21.base.Music21Object.containerHierarchy") * [`contextSites()`](moduleBase.html#music21.base.Music21Object.contextSites "music21.base.Music21Object.contextSites") * [`getAllContextsByClass()`](moduleBase.html#music21.base.Music21Object.getAllContextsByClass "music21.base.Music21Object.getAllContextsByClass") * [`getContextByClass()`](moduleBase.html#music21.base.Music21Object.getContextByClass "music21.base.Music21Object.getContextByClass") * [`getOffsetBySite()`](moduleBase.html#music21.base.Music21Object.getOffsetBySite "music21.base.Music21Object.getOffsetBySite") * [`getOffsetInHierarchy()`](moduleBase.html#music21.base.Music21Object.getOffsetInHierarchy "music21.base.Music21Object.getOffsetInHierarchy") | * [`getSpannerSites()`](moduleBase.html#music21.base.Music21Object.getSpannerSites "music21.base.Music21Object.getSpannerSites") * [`informSites()`](moduleBase.html#music21.base.Music21Object.informSites "music21.base.Music21Object.informSites") * [`mergeAttributes()`](moduleBase.html#music21.base.Music21Object.mergeAttributes "music21.base.Music21Object.mergeAttributes") * [`next()`](moduleBase.html#music21.base.Music21Object.next "music21.base.Music21Object.next") * [`previous()`](moduleBase.html#music21.base.Music21Object.previous "music21.base.Music21Object.previous") * [`purgeLocations()`](moduleBase.html#music21.base.Music21Object.purgeLocations "music21.base.Music21Object.purgeLocations") * [`purgeOrphans()`](moduleBase.html#music21.base.Music21Object.purgeOrphans "music21.base.Music21Object.purgeOrphans") | * [`setOffsetBySite()`](moduleBase.html#music21.base.Music21Object.setOffsetBySite "music21.base.Music21Object.setOffsetBySite") * [`show()`](moduleBase.html#music21.base.Music21Object.show "music21.base.Music21Object.show") * [`sortTuple()`](moduleBase.html#music21.base.Music21Object.sortTuple "music21.base.Music21Object.sortTuple") * [`splitAtDurations()`](moduleBase.html#music21.base.Music21Object.splitAtDurations "music21.base.Music21Object.splitAtDurations") * [`splitAtQuarterLength()`](moduleBase.html#music21.base.Music21Object.splitAtQuarterLength "music21.base.Music21Object.splitAtQuarterLength") * [`splitByQuarterLengths()`](moduleBase.html#music21.base.Music21Object.splitByQuarterLengths "music21.base.Music21Object.splitByQuarterLengths") * [`write()`](moduleBase.html#music21.base.Music21Object.write "music21.base.Music21Object.write") |

[`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") instance variables

ContiguousSegmentOfNotes.activeSegment
:   A list of pitch classes representing the way the contiguous
    segment of notes is being read as a sequence of single pitches. Set to None
    unless the container stream is being searched for segments or multisets
    (for example, using [`find()`](#music21.search.serial.SegmentMatcher.find "music21.search.serial.SegmentMatcher.find")), in which case
    the representation depends on the segments or multisets being searched for.
    If there are no chords in the segment, this attribute will simply give the
    pitch classes of the notes in the segment.

ContiguousSegmentOfNotes.containerStream
:   The stream containing the contiguous segment -
    all contiguous segments must have a container stream.

ContiguousSegmentOfNotes.matchedSegment
:   A list of pitch classes representing the segment to which
    the contiguous segment of notes is matched when segments or multisets are
    searched for (for example, using `findSegments()`);
    otherwise set to None. Note that the contiguous segment will only be
    matched to one of the segments or multisets being searched for.

ContiguousSegmentOfNotes.partNumber
:   The part number in which the segment appears, or None
    (if the container stream has no parts). Note that this attribute is zero-indexed,
    so the top (e.g. soprano) part is labeled 0.

ContiguousSegmentOfNotes.segment
:   The list of notes and chords in the contiguous segment.

Instance variables inherited from [`Music21Object`](moduleBase.html#music21.base.Music21Object "music21.base.Music21Object"):

|  |  |  |
| --- | --- | --- |
| * [`classSortOrder`](moduleBase.html#music21.base.Music21Object.classSortOrder "music21.base.Music21Object.classSortOrder") * [`groups`](moduleBase.html#music21.base.Music21Object.groups "music21.base.Music21Object.groups") | * [`isStream`](moduleBase.html#music21.base.Music21Object.isStream "music21.base.Music21Object.isStream") | * [`sites`](moduleBase.html#music21.base.Music21Object.sites "music21.base.Music21Object.sites") |

## ContiguousSegmentSearcher

class music21.search.serial.ContiguousSegmentSearcher(*inputStream=None*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher)
:   Class that when given a `Stream`
    and .byLength() is called, returns a
    [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") objects
    where the desired number of notes in the segment is specified.

    The inputStream is a Score or Part or Opus containing one score..
    Furthermore, all notes must be contained within measures.

    The reps argument specifies how repeated pitch classes are dealt with.
    It may be set to ‘skipConsecutive’ (default), ‘rowsOnly’, ‘includeAll’, or ‘ignoreAll’.
    These are explained in detail below.

    The includeChords argument specifies how chords are dealt with. When set to True (default),
    the pitches of all chords
    are read in order from bottom to top, and when set to False, all segments containing
    chords are ignored.

    The main subtleties of this function lie in how each reps setting works in
    conjunction with chords when
    includeChords is set to True, and how the lengths of the segments are measured.
    However, let us first examine what happens when includeChords
    is set to False, to get an idea of how the function works.

    To begin, we create a stream on which we will apply the function.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 6
    >>> s.append(n1)
    >>> n2 = note.Note('f4')
    >>> n2.quarterLength = 1
    >>> s.append(n2)
    >>> n3 = chord.Chord(['g4', 'b4'])
    >>> n3.quarterLength = 1
    >>> s.append(n3)
    >>> n4 = note.Note('g4')
    >>> n4.quarterLength = 1
    >>> s.repeatAppend(n4, 2)
    >>> n5 = note.Note('a4')
    >>> n5.quarterLength = 3
    >>> s.repeatAppend(n5, 2)
    >>> n6 = note.Note('b4')
    >>> n6.quarterLength = 1
    >>> s.append(n6)
    >>> n7 = note.Note('c5')
    >>> n7.quarterLength = 1
    >>> s.append(n7)
    ```

    We can now try to apply this function:

    ```python
    >>> searcher = search.serial.ContiguousSegmentSearcher(s, 'skipConsecutive', False)
    >>> contiguousList = searcher.byLength(3)
    >>> print(contiguousList)
    [<music21.search.serial.ContiguousSegmentOfNotes ['G4', 'A4', 'B4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['A4', 'B4', 'C5']>]
    ```

    [![../_images/serial-findTransposedSegments.png](../_images/serial-findTransposedSegments.png)](../_images/serial-findTransposedSegments.png)

    We now can apply the function, and in doing so we examine in detail each of the reps settings.

    ‘skipConsecutive’ means that whenever immediate repetitions of notes or chords occur,
    only the first instance of the note or chord is included in the segment.
    The durations of the repeated notes,
    do not have to be the same.

    ```python
    >>> searcher = search.serial.ContiguousSegmentSearcher(s, includeChords=False)
    >>> searcher.reps = 'skipConsecutive'
    ```

    ```python
    >>> skipConsecutiveList = searcher.byLength(3)
    >>> print(skipConsecutiveList)
    [<music21.search.serial.ContiguousSegmentOfNotes ['G4', 'A4', 'B4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['A4', 'B4', 'C5']>]
    ```

    ```python
    >>> [instance.segment for instance in skipConsecutiveList]
    [[<music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B>],
     [<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note C>]]
    ```

    In order to be considered repetition, the spellings of the notes
    in question must be exactly the same:
    enharmonic equivalents are not checked and notes with the
    same pitch in different octaves are considered different.
    To illustrate this, see the example below, in which all three notes,
    with pitch class 0, are considered
    separately.

    ```python
    >>> new = stream.Stream()
    >>> n1 = note.Note('c4')
    >>> n2 = note.Note('c5')
    >>> n3 = note.Note('b#5')
    >>> new.append(n1)
    >>> new.append(n2)
    >>> new.append(n3)
    >>> new = new.makeMeasures()
    ```

    ```python
    >>> searcherNew = search.serial.ContiguousSegmentSearcher(new,
    ...       reps='skipConsecutive', includeChords=False)
    >>> foundSegments = searcherNew.byLength(3)
    >>> [seg.segment for seg in foundSegments]
    [[<music21.note.Note C>, <music21.note.Note C>, <music21.note.Note B#>]]
    ```

    ‘rowsOnly’ searches only for tone rows, in which all pitch classes
    in the segment must be distinct. Below,
    we are looking for sequences three consecutive notes within the
    stream s, all of which have different pitch classes.
    There is only one such set of notes, and by calling the
    [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") we can
    determine its location (the measure number of its first note).

    We’ll return to our original searcher, but make sure that it has measures now:

    ```python
    >>> searcher = search.serial.ContiguousSegmentSearcher(s.makeMeasures(), includeChords=False)
    >>> searcher.reps = 'rowsOnly'
    >>> rowsOnlyList = searcher.byLength(3)
    >>> [(instance.segment, instance.startMeasureNumber) for instance in rowsOnlyList]
    [([<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note C>], 4)]
    ```

    ‘includeAll’ disregards all repetitions, and simply gets all
    contiguous segments of the specified length (still subject
    to the includeChords setting).

    ```python
    >>> searcher.reps = 'includeAll'
    >>> includeAllList = searcher.byLength(3)
    >>> for instance in includeAllList:
    ...     print(instance.segment, instance.startMeasureNumber, instance.startOffset)
    [<music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>] 3 0.0
    [<music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>] 3 1.0
    [<music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B>] 3 2.0
    [<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note C>] 4 1.0
    ```

    Note that there only two total As appear in these segments, despite there being three
    [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") objects with the A4 as the pitch
    in the stream s; this is because only the first note of each set
    of tied notes is considered. This convention applies to this
    function and all parsing functions below.
    Also note that so far, neither of the first two notes n1, n2
    nor the major third n3 in s have been included in any of the
    returned contiguous segments. This is because for each of these,
    any instance of three consecutive notes or chords
    contains the chord n3. This phenomenon also applies to the next example below.

    Finally, when includeChords is set to False, ‘ignoreAll’ finds all
    contiguous segments containing exactly three distinct pitch
    classes within it. It is unique in that unlike the previous three
    reps settings, the segments returned in fact
    have more than the number of notes specified (3). Rather, they
    each have 3 distinct pitch classes, and some pitch classes
    may be repeated.

    ```python
    >>> searcher.reps = 'ignoreAll'
    >>> ignoreAllList = searcher.byLength(3)
    >>> [instance.segment for instance in ignoreAllList]
    [[<music21.note.Note G>, <music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>,
      <music21.note.Note B>],
     [<music21.note.Note G>, <music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B>],
     [<music21.note.Note A>, <music21.note.Note A>, <music21.note.Note B>, <music21.note.Note C>],
     [<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note C>]]
    ```

    Let us now examine what happens in the default chord setting,
    in which includeChords is set to True.

    There are two points to remember when considering chords: the first is that all
    chords are read as sequences of single notes,
    from bottom to top. The second is that ‘length’ always applies to the total
    number of single pitches or pitch classes found
    in the segment, including within chords, and not to the number of notes or chords.
    However, as we will see, when we search
    for contiguous segments of length 4, the returned segments may not have exactly
    4 total notes (possibly existing
    as single notes or within chords), a natural point of confusion.

    Below is a new stream s0.

    ```python
    >>> s0 = stream.Stream()
    >>> n1 = note.Note('d4')
    >>> maj2nd = chord.Chord(['f4', 'g4'])
    >>> bMaj1 = chord.Chord(['b4', 'd#5', 'f#5'])
    >>> bMaj2 = chord.Chord(['b4', 'd#5', 'f#5'])
    >>> n2 = note.Note('f#4')
    >>> n3 = note.Note('e4')
    >>> n4 = note.Note('a4')
    >>> s0.append([n1, maj2nd, bMaj1, bMaj2, n2, n3, n4])
    >>> s0 = s0.makeMeasures()
    >>> s0.show()
    ```

    [![../_images/serial-getContiguousSegmentsOfLength2.png](../_images/serial-getContiguousSegmentsOfLength2.png)](../_images/serial-getContiguousSegmentsOfLength2.png)

    ```python
    >>> searcher = search.serial.ContiguousSegmentSearcher(s0, 'skipConsecutive', True)
    >>> skipConsecutiveWithChords = searcher.byLength(4)
    >>> [seg.segment for seg in skipConsecutiveWithChords]
    [[<music21.note.Note D>, <music21.chord.Chord F4 G4>, <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord F4 G4>, <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.note.Note F#>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.note.Note F#>, <music21.note.Note E>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.note.Note F#>, <music21.note.Note E>,
      <music21.note.Note A>]]
    ```

    Let us look closely at the found segments. First, because reps
    was set to ‘skipConsecutive’, the second
    B major chord (bMaj2) is never considered, as the chord right
    before it is the same. As was mentioned before,
    not all the segments found have exactly 4 notes total.
    This is because, for each segment, only a subset
    of the notes contained in the first and last elements are read. Given one of the
    found segments, it will always
    be possible to extract exactly four consecutive pitches from the notes and chords,
    reading in order, so that
    at least one pitch is taken from each of the first and last chords.

    In the first segment, there is one way to extract 4 consecutive pitches:
    we take the D in the first note, read
    the F and G (in that order) from the next chord, and finally,
    reading the last chord from bottom to top, the B
    from the B major chord. Note that no other reading of the segment
    is possible because the D from the first note
    must be used. The second segment in the returned list, on the other
    hand, can be read as a sequence of 4
    consecutive pitches in two ways, both equally valid. We can either take
    the top note of the first chord, and all three
    notes, in order, of the second chord, or both notes of the first chord
    and the bottom two notes of the second chord.

    ```python
    >>> searcher.reps = 'rowsOnly'
    >>> rowsOnlyChords = searcher.byLength(4)
    >>> rowsOnlyChords
    [<music21.search.serial.ContiguousSegmentOfNotes ['D4', 'F4 G4', 'B4 D#5 F#5']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['F4 G4', 'B4 D#5 F#5']>]
    ```

    ```python
    >>> [seg.segment for seg in rowsOnlyChords]
    [[<music21.note.Note D>, <music21.chord.Chord F4 G4>, <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord F4 G4>, <music21.chord.Chord B4 D#5 F#5>]]
    ```

    When reps is set to ‘rowsOnly’, the segments returned are those such that
    each may be read as a sequence
    of 4 pitches, in the same manner as explained above with the ‘skipConsecutive’ setting,
    such that the sequence
    of 4 pitches constitutes a four-note tone row. Above, the first segment
    corresponds to the row [2, 5, 7, 11], and the
    second may be read as either [5, 7, 11, 3] or [7, 11, 3, 6]. Note that, for example,
    we could not include both
    the B-major chord and the F# that comes right after it in the same segment,
    because there would have to be two
    consecutive instances of the pitch class 6 (corresponding to F#). Similarly,
    we could not include both instances
    of the B-major chord, as, again, we would have a pitch class repeated in
    any resulting four-note row.

    ```python
    >>> searcher.reps = 'includeAll'
    >>> includeAll = searcher.byLength(4)
    >>> [seg.segment for seg in includeAll]
    [[<music21.note.Note D>, <music21.chord.Chord F4 G4>, <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord F4 G4>, <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.note.Note F#>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.note.Note F#>, <music21.note.Note E>],
     [<music21.chord.Chord B4 D#5 F#5>, <music21.note.Note F#>,
      <music21.note.Note E>, <music21.note.Note A>]]
    ```

    Here, all segments from which sequences of four consecutive pitches can be extracted,
    again with at least
    one pitch coming from each of the first and last elements of the segments, are found.

    ```python
    >>> searcher.reps = 'ignoreAll'
    >>> ignoreAll = searcher.byLength(4)
    >>> [seg.segment for seg in ignoreAll]
    [[<music21.note.Note D>,
      <music21.chord.Chord F4 G4>,
      <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord F4 G4>,
      <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord F4 G4>,
      <music21.chord.Chord B4 D#5 F#5>,
      <music21.chord.Chord B4 D#5 F#5>],
     [<music21.chord.Chord F4 G4>,
      <music21.chord.Chord B4 D#5 F#5>,
      <music21.chord.Chord B4 D#5 F#5>,
      <music21.note.Note F#>],
     [<music21.chord.Chord B4 D#5 F#5>,
      <music21.chord.Chord B4 D#5 F#5>,
      <music21.note.Note F#>,
      <music21.note.Note E>],
     [<music21.chord.Chord B4 D#5 F#5>,
      <music21.note.Note F#>,
      <music21.note.Note E>],
     [<music21.chord.Chord B4 D#5 F#5>,
      <music21.note.Note F#>,
      <music21.note.Note E>,
      <music21.note.Note A>]]
    ```

    When reps is set to ‘ignoreAll’, the pitch classes from each segment are read by taking,
    in order, the pitch classes
    in the order in which they first appear, where chords are again read from bottom to top.
    For example, in the last segment,
    the first three pitch classes are those in the first chord, from
    bottom to top: 11, 3, and 6. Then, the next pitch class
    appearing is 6, which is disregarded because it has already appeared.
    Finally, the pitch classes 4 and 9 appear in that order.
    There are thus five pitch classes in this segment, in the order [11, 3, 6, 4, 9].

    The segment can be read has having length 4 because four consecutive
    pitch classes, [3, 6, 4, 9], can be read from this sequence
    in such a way that the first pitch class of this subsequence is part of the
    first chord in the segment, and the last pitch class
    is that of the last note of the segment. More generally, in this setting the
    found segments are those which contain at least 4
    distinct pitch classes, but the top note of the first chord (or note), the
    bottom note of the last chord (or note),
    and all pitches of all notes and chords other than the first and last
    contain at most 4 distinct pitch classes.

[`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher") methods

ContiguousSegmentSearcher.addActiveChords(*partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.addActiveChords)

ContiguousSegmentSearcher.byLength(*length*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.byLength)
:   Run the current setting for reps and includeChords to find all segments
    of length length.

ContiguousSegmentSearcher.getSearchBoundMethod()[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.getSearchBoundMethod)
:   Return a search method based on the setting of reps (how to classify repetitions),
    and the includeChord setting.

ContiguousSegmentSearcher.searchIgnoreAllExclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchIgnoreAllExclude)

ContiguousSegmentSearcher.searchIgnoreAllInclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchIgnoreAllInclude)

ContiguousSegmentSearcher.searchIncludeAllExclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchIncludeAllExclude)

ContiguousSegmentSearcher.searchIncludeAllInclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchIncludeAllInclude)
:   Returns the number added.

ContiguousSegmentSearcher.searchRowsOnlyExclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchRowsOnlyExclude)

ContiguousSegmentSearcher.searchRowsOnlyInclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchRowsOnlyInclude)

ContiguousSegmentSearcher.searchSkipConsecutiveExclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchSkipConsecutiveExclude)

ContiguousSegmentSearcher.searchSkipConsecutiveInclude(*n*, *partNumber*)[[source]](../_modules/music21/search/serial.html#ContiguousSegmentSearcher.searchSkipConsecutiveInclude)

## MultisetSegmentMatcher

class music21.search.serial.MultisetSegmentMatcher(*inputStream*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#MultisetSegmentMatcher)
:   Finds all instances of given multisets of pitch classes
    within a `Stream`. A multiset
    is a generalization of a set, in which the order of the
    elements in the multiset does not matter, but multiple instances
    of the same thing (in this case, same pitch class) are treated as distinct elements.
    Thus, two multisets of pitch classes
    are considered to be equal if and only if the number of times any given
    pitch class appears in one multiset is the same as
    the number of times the pitch class appears in the other multiset.

    The inputStream is `Stream`; as
    in [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher"),
    the inputStream can contain at most one `Score`
    its notes must be contained in measures. However, the inputStream may have
    multiple parts. The searchList is a list of multisets to
    be searched for, each multiset being given as a list of pitch classes.
    Note that the order of pitch classes given in a multiset
    does not matter. The reps and includeChords settings specify how
    repeated pitches and chords, respectively, are handled;
    the possible settings are the same as those in
    [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher")

    Returns a list of [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes")
    objects for the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment"),
    interpreted as a multiset,
    matches at least one of the elements of the searchList,
    subject to the settings specified in reps and includeChords.

    ```python
    >>> part = stream.Part()
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 4
    >>> n2 = note.Note('e4')
    >>> n2.quarterLength = 4
    >>> n3 = note.Note('f4')
    >>> n3.quarterLength = 4
    >>> n4 = note.Note('e4')
    >>> n4.quarterLength = 4
    >>> n5 = note.Note('g4')
    >>> n5.quarterLength = 4
    >>> part.append(n1)
    >>> part.append(n2)
    >>> part.append(n3)
    >>> part.append(n4)
    >>> part.append(n5)
    >>> part.makeMeasures(inPlace=True)
    >>> part.show('text')
    {0.0} <music21.stream.Measure 1 offset=0.0>
        {0.0} <music21.clef.TrebleClef>
        {0.0} <music21.meter.TimeSignature 4/4>
        {0.0} <music21.note.Note E>
    {4.0} <music21.stream.Measure 2 offset=4.0>
        {0.0} <music21.note.Note E>
    {8.0} <music21.stream.Measure 3 offset=8.0>
        {0.0} <music21.note.Note F>
    {12.0} <music21.stream.Measure 4 offset=12.0>
        {0.0} <music21.note.Note E>
    {16.0} <music21.stream.Measure 5 offset=16.0>
        {0.0} <music21.note.Note G>
        {4.0} <music21.bar.Barline type=final>
    ```

    ```python
    >>> part.show()
    ```

    [![../_images/serial-findMultisets.png](../_images/serial-findMultisets.png)](../_images/serial-findMultisets.png)

    Find all instances of the multiset [5, 4, 4] in the part

    ```python
    >>> MSS = search.serial.MultisetSegmentMatcher(part, 'includeAll', includeChords=False)
    >>> EEF = MSS.find([5, 4, 4])
    >>> EEF
    [<music21.search.serial.ContiguousSegmentOfNotes ['E4', 'E4', 'F4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['E4', 'F4', 'E4']>]
    >>> [(seg.activeSegment, seg.startMeasureNumber) for seg in EEF]
    [([4, 4, 5], 1), ([4, 5, 4], 2)]
    ```

    ```python
    >>> MSS = search.serial.MultisetSegmentMatcher(part, 'ignoreAll')
    >>> EF = MSS.find([5, 4])
    >>> EF
    [<music21.search.serial.ContiguousSegmentOfNotes ['E4', 'E4', 'F4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['E4', 'F4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['E4', 'E4', 'F4', 'E4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['E4', 'F4', 'E4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['F4', 'E4']>]
    ```

    Consider the following examples, with chords.

    ```python
    >>> sc0 = stream.Score()
    >>> part0 = stream.Part()
    >>> part0.append(note.Note('c4'))
    >>> part0.append(note.Note('d4'))
    >>> part0.append(note.Note('e4'))
    >>> part0.append(chord.Chord(['f4', 'e5']))
    >>> part0 = part0.makeMeasures()
    >>> sc0.insert(0, part0)
    ```

    ```python
    >>> MSS = search.serial.MultisetSegmentMatcher(sc0, 'ignoreAll')
    >>> CDE = MSS.find([0, 4, 2])
    ```

    ```python
    >>> [seg.segment for seg in CDE]
    [[<music21.note.Note C>, <music21.note.Note D>, <music21.note.Note E>]]
    ```

    Also:

    ```python
    >>> sc1 = stream.Score()
    >>> part1 = stream.Part()
    >>> part1.append(note.Note('c4'))
    >>> part1.append(note.Note('d4'))
    >>> part1.append(chord.Chord(['e4', 'f4']))
    >>> part1 = part1.makeMeasures()
    >>> sc1.insert(0, part1)
    >>> searcher = search.serial.ContiguousSegmentSearcher(sc1)
    >>> segmentList = searcher.byLength(3)
    >>> [seg.getDistinctPitchClasses() for seg in segmentList]
    [[0, 2, 4, 5], [2, 4, 5]]
    ```

    ```python
    >>> MSS = search.serial.MultisetSegmentMatcher(sc1)
    >>> CDF = MSS.find([0, 2, 5])
    >>> CDF
    []
    ```

[`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher") bases

* [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher")

[`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher") read/write properties

Read/write properties inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`includeChords`](#music21.search.serial.SegmentMatcher.includeChords "music21.search.serial.SegmentMatcher.includeChords") | * [`reps`](#music21.search.serial.SegmentMatcher.reps "music21.search.serial.SegmentMatcher.reps") |  |

[`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher") methods

MultisetSegmentMatcher.equalSubset(*searchSegment*, *subsetToCheck*)[[source]](../_modules/music21/search/serial.html#MultisetSegmentMatcher.equalSubset)
:   Returns True if there are the same number of each pitchClass in searchSegment
    as in subsetToCheck

Methods inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`checkSearchedAlready()`](#music21.search.serial.SegmentMatcher.checkSearchedAlready "music21.search.serial.SegmentMatcher.checkSearchedAlready") * [`find()`](#music21.search.serial.SegmentMatcher.find "music21.search.serial.SegmentMatcher.find") | * [`findOneIgnoreAll()`](#music21.search.serial.SegmentMatcher.findOneIgnoreAll "music21.search.serial.SegmentMatcher.findOneIgnoreAll") * [`findOneOtherReps()`](#music21.search.serial.SegmentMatcher.findOneOtherReps "music21.search.serial.SegmentMatcher.findOneOtherReps") | * [`getContiguousSegmentsByLength()`](#music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength "music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength") * [`normalize()`](#music21.search.serial.SegmentMatcher.normalize "music21.search.serial.SegmentMatcher.normalize") |

## SegmentMatcher

class music21.search.serial.SegmentMatcher(*inputStream*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher)
:   Matches all the ContiguousSegmentsOfNotes (found by ContiguousSegmentSearcher)
    within a `Stream`
    to one or more segments of pitch classes.

    The inputStream is a `Stream`; as
    in [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher"),
    the inputStream can contain at most one `Score` and
    its notes must be contained in measures. The searchList is a list of contiguous segments to
    be searched for, each segment being given as a list of pitch classes.
    The reps and includeChords settings specify how
    repeated pitches and chords, respectively, are handled; the
    possible settings are the same as those in
    [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher").

    Returns a list of [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes")
    objects for which the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment")
    matches at least one of the elements of the searchList,
    subject to the settings specified in reps and includeChords.

    ```python
    >>> sc = stream.Score()
    >>> part = stream.Part()
    >>> sig = meter.TimeSignature('2/4')
    >>> part.append(sig)
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 6
    >>> part.append(n1)
    >>> n2 = note.Note('f4')
    >>> n2.quarterLength = 1
    >>> part.append(n2)
    >>> n3 = chord.Chord(['g4', 'b4'])
    >>> n3.quarterLength = 1
    >>> part.append(n3)
    >>> n4 = note.Note('g4')
    >>> n4.quarterLength = 1
    >>> part.repeatAppend(n4, 2)
    >>> n5 = note.Note('a4')
    >>> n5.quarterLength = 3
    >>> part.repeatAppend(n5, 2)
    >>> n6 = note.Note('b4')
    >>> n6.quarterLength = 1
    >>> part.append(n6)
    >>> n7 = note.Note('c5')
    >>> n7.quarterLength = 1
    >>> part.append(n7)
    >>> newPart = part.makeMeasures()
    >>> newPart.makeTies(inPlace=True)
    >>> newPart.show()
    ```

    [![../_images/serial-findSegments.png](../_images/serial-findSegments.png)](../_images/serial-findSegments.png)

    ```python
    >>> sc.insert(0, newPart)
    ```

    ```python
    >>> matcher = search.serial.SegmentMatcher(sc, includeChords=False)
    ```

    ```python
    >>> GABandABC = matcher.find([[7, 9, 11], [9, 11, 0]])
    >>> print(GABandABC)
    [<music21.search.serial.ContiguousSegmentOfNotes ['G4', 'A4', 'B4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['A4', 'B4', 'C5']>]
    ```

    ```python
    >>> GABandABC[0].segment, GABandABC[1].segment
    ([<music21.note.Note G>, <music21.note.Note A>, <music21.note.Note B>],
     [<music21.note.Note A>, <music21.note.Note B>, <music21.note.Note C>])
    ```

    ```python
    >>> GABandABC[0].startMeasureNumber, GABandABC[1].startMeasureNumber
    (5, 6)
    ```

    In case it is not clear, we can use
    the `matchedSegment` property
    to determine, to which element of the original searchList the found
    contiguous segments were matched.

    ```python
    >>> GABandABC[0].matchedSegment
    [7, 9, 11]
    >>> GABandABC[1].matchedSegment
    [9, 11, 0]
    ```

    One can also search for segments of different lengths, simultaneously.
    Below, ‘B’ refers to the
    pitch class 11, which only coincidentally is the same as that of the note B.

    ```python
    >>> x = (matcher.find([[7, 9, 11], ['B', 0]]))
    >>> x
    [<music21.search.serial.ContiguousSegmentOfNotes ['G4', 'A4', 'B4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['B4', 'C5']>]
    ```

    Below, we can see what happens when we include the chords and use ignoreAll

    ```python
    >>> matcher = search.serial.SegmentMatcher(sc, reps='ignoreAll', includeChords=True)
    >>> [seg.segment for seg in matcher.find([[5, 7, 'B']])]
    [[<music21.note.Note F>, <music21.chord.Chord G4 B4>]]
    ```

    As expected, the pitch classes found segment are read
    in the order 5, 7, 11 (‘B’), as the pitches
    in the chord are read from bottom to top.

    Consider the following other example with chords, which is somewhat more complex:

    ```python
    >>> sc0 = stream.Score()
    >>> p0 = stream.Part()
    >>> c1 = chord.Chord(['c4', 'd4'])
    >>> c2 = chord.Chord(['e4', 'f4'])
    >>> p0.append(c1)
    >>> p0.append(c2)
    >>> p0 = p0.makeMeasures()
    >>> sc0.insert(0, p0)
    ```

    ```python
    >>> matcher = search.serial.SegmentMatcher(sc0)
    >>> foundSegments = matcher.find([[0, 2, 4]])
    >>> len(foundSegments)
    1
    >>> seg = foundSegments[0]
    >>> seg.segment
    [<music21.chord.Chord C4 D4>, <music21.chord.Chord E4 F4>]
    >>> seg.activeSegment
    [0, 2, 4]
    ```

    If we are just searching for a single term, the list-of-lists can be
    given just as a list:

    ```python
    >>> foundSegments = matcher.find([2, 4, 5])
    >>> len(foundSegments)
    1
    >>> seg = foundSegments[0]
    >>> seg.segment
    [<music21.chord.Chord C4 D4>, <music21.chord.Chord E4 F4>]
    >>> seg.activeSegment
    [2, 4, 5]
    ```

    In the two function calls, despite the fact that two different segments
    of pitch classes were searched for, the same
    [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") object was found for each.
    This is because the found object can be read
    in two ways as a sequence of three pitch classes: either as [0, 2, 4], by
    taking the two notes of the first chord in order
    and the bottom note of the second, or as [2, 4, 5], by taking the top
    note of the first chord and the two notes of the second
    chord in order. Both times, the chords are read from bottom to top.

    ```python
    >>> matcher = search.serial.SegmentMatcher(sc, includeChords=False)
    >>> foundSegments = matcher.find([[7, -3, 11], [9, 11, 0]])
    ```

    ```python
    >>> for a in foundSegments:
    ...    print(a.matchedSegment)
    [7, -3, 11]
    [9, 11, 0]
    ```

    ```python
    >>> len(foundSegments)
    2
    ```

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('e4')
    >>> n2 = note.Note('f4')
    >>> n3 = note.Note('g4')
    >>> c = chord.Chord(['b4', 'g5', 'a5'])
    >>> s.append(n1)
    >>> s.append(n2)
    >>> s.append(n3)
    >>> s.append(c)
    >>> s = s.makeMeasures()
    ```

    ```python
    >>> matcher = search.serial.SegmentMatcher(s, 'ignoreAll')
    >>> foundSegments = matcher.find([4, -7, 7])
    ```

    ```python
    >>> [seg.segment for seg in foundSegments]
    [[<music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>]]
    ```

    ```python
    >>> foundSegments = matcher.find([7, 'B', 9])
    >>> [seg.segment for seg in foundSegments]
    [[<music21.note.Note G>, <music21.chord.Chord B4 G5 A5>]]
    ```

[`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher") read/write properties

SegmentMatcher.includeChords
:   Returns or sets bool on whether chords should be included.

    Clears the segment cache when it is changed.

SegmentMatcher.reps

[`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher") methods

SegmentMatcher.checkSearchedAlready(*unNormalizedSearchSegment*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.checkSearchedAlready)
:   Check to see if we have searched this segment already.

    Called out to be subclassible by Transformed searchers.

    If yes, return True.

    If not, add to searchedAlready and return False

    ```python
    >>> matcher = search.serial.SegmentMatcher(None)
    >>> matcher.checkSearchedAlready([4, 5, 6])
    False
    >>> matcher.checkSearchedAlready([1, 2, 3])
    False
    >>> matcher.checkSearchedAlready([4, 5, 6])
    True
    ```

SegmentMatcher.equalSubset(*searchSegment*, *subsetToCheck*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.equalSubset)
:   Returns True if these are equal in some way.

    Here’s it is simple – are they equal? But it will be harder for other classes.

SegmentMatcher.find(*searchList*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.find)

SegmentMatcher.findOneIgnoreAll(*thisSegment*, *searchSegment*, *unNormalizedCurrentSearchSegment=None*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.findOneIgnoreAll)
:   Checks whether thisSegment is a match for the searchSegment if ‘ignoreAll’ is the search
    term.

    If so adds it to self.matchedSegments. Only matches once per segment

SegmentMatcher.findOneOtherReps(*thisSegment*, *searchSegment*, *unNormalizedCurrentSearchSegment*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.findOneOtherReps)
:   Checks whether thisSegment is a match for the searchSegment if ‘ignoreAll’ is NOT the search
    term.

    If so adds it to self.matchedSegments. Only matches once per segment

SegmentMatcher.getContiguousSegmentsByLength(*searchSegmentLength*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.getContiguousSegmentsByLength)
:   Creates a ContiguousSegmentSearcher and finds all segments in
    self.stream based on the .reps and .includeChords settings and
    the searchSegmentLength

    If we are searching on lots of segments to match, then we could
    end up running this expensive routine multiple times, so we’ll
    cache the answer for each length.

    If .reps or .includeChords is changed, then this will be obsolete,
    so cleared.

static SegmentMatcher.normalize(*segment*)[[source]](../_modules/music21/search/serial.html#SegmentMatcher.normalize)
:   Normalize an input segment for searching. This class just changes
    letters to numbers, etc.

    Staticmethod:

    ```python
    >>> search.serial.SegmentMatcher.normalize([3, 4, 5])
    [3, 4, 5]
    >>> search.serial.SegmentMatcher(None).normalize(['B', -24, '1'])
    [11, 0, 1]
    ```

## TransformedSegmentMatcher

class music21.search.serial.TransformedSegmentMatcher(*inputStream*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#TransformedSegmentMatcher)
:   Finds all instances of given contiguous segments of pitch classes,
    with serial transformations,
    within a `Stream`.

    The inputStream is `Stream`; as
    in [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher"),
    the inputStream can
    contain at most one `Score`
    and its notes must be contained in measures. The searchList is a list of contiguous segments to
    be searched for, each segment being given as a list of pitch classes.
    The reps and includeChords settings specify how
    repeated pitches and chords, respectively, are handled; the possible settings
    are the same as those in
    [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher").

    The convention for serial
    transformations must be specified to either
    ‘zero’ or ‘original’, as described in
    `zeroCenteredTransformation()` and
    `originalCenteredTransformation()` - the default setting
    is ‘original’, as to relate found segments
    directly to the given segments, without first transposing the given segment to
    begin on the pitch class 0.

    Returns a list of [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") objects
    for which some transformation of the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment") matches at
    least one of the elements of the searchList,
    subject to the settings specified in reps and includeChords.

    ```python
    >>> n1 = note.Note('c#4')
    >>> n2 = note.Note('e4')
    >>> n3 = note.Note('d#4')
    >>> n4 = note.Note('f4')
    >>> n5 = note.Note('e4')
    >>> n6 = note.Note('g4')
    >>> noteList = [n1, n2, n3, n4, n5, n6]
    >>> part = stream.Part()
    >>> part.append(noteList)
    >>> part = part.makeMeasures()
    >>> part.show()
    ```

    [![../_images/serial-findTransformedSegments.png](../_images/serial-findTransformedSegments.png)](../_images/serial-findTransformedSegments.png)

    ```python
    >>> tsMatcher = search.serial.TransformedSegmentMatcher(part, 'rowsOnly',
    ...                 includeChords=False)
    >>> rowInstances = tsMatcher.find([2, 5, 4])
    ```

    ```python
    >>> row = [2, 5, 4]
    >>> len(rowInstances)
    2
    >>> firstInstance = rowInstances[0]
    >>> firstInstance
    <music21.search.serial.ContiguousSegmentOfNotes ['C#4', 'E4', 'D#4']>
    ```

    ```python
    >>> firstInstance.activeSegment, firstInstance.startMeasureNumber
    (<music21.serial.ToneRow 143>, 1)
    >>> firstInstance.activeSegment.pitchClasses()
    [1, 4, 3]
    >>> firstInstance.originalCenteredTransformationsFromMatched
    [('T', 11)]
    ```

    We have thus found that the first instance of the row [2, 5, 4] within our
    stream appears as a transposition
    down a semitone, beginning in measure 1. We can do a similar analysis on
    the other instance of the row.

    ```python
    >>> secondInstance = rowInstances[1]
    >>> secondInstance.activeSegment.pitchClasses(), secondInstance.startMeasureNumber
    ([5, 4, 7], 1)
    >>> secondInstance.zeroCenteredTransformationsFromMatched
    [('RI', 7)]
    ```

    Let us give an example of this function used with chords included and reps set to ‘ignoreAll’.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('e4')
    >>> n2 = note.Note('f4')
    >>> n3 = note.Note('g4')
    >>> c = chord.Chord(['b4', 'g5', 'a5'])
    >>> s.append(n1)
    >>> s.append(n2)
    >>> s.append(n3)
    >>> s.append(c)
    >>> s = s.makeMeasures()
    ```

    ```python
    >>> tsMatcher = search.serial.TransformedSegmentMatcher(s, 'ignoreAll',
    ...                 includeChords=True)
    >>> found643 = tsMatcher.find([6, 4, 3])
    >>> [seg.segment for seg in found643]
    [[<music21.note.Note E>, <music21.note.Note F>, <music21.note.Note G>]]
    ```

    ```python
    >>> found684 = tsMatcher.find([6, 8, 4])
    >>> for seg in found684:
    ...    print(seg.segment)
    [<music21.note.Note G>, <music21.chord.Chord B4 G5 A5>]
    [<music21.chord.Chord B4 G5 A5>]
    ```

    ```python
    >>> [seg.activeSegment.pitchClasses() for seg in found684]
    [[7, 11, 9],
     [11, 7, 9]]
    ```

    ```python
    >>> [seg.originalCenteredTransformationsFromMatched for seg in found684]
    [[('R', 3)],
     [('RI', 3)]]
    ```

    Pitch classes are extracted from segments in order of appearance, with
    pitches in chords being read from bottom to top.
    However, only the first instance of each pitch class is considered, as seen in the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment") calls.
    As long as the first and last pitch classes in the
    active segment first appear in the first and last elements of
    the found segment, respectively, the segment will be matched to the
    segment being searched for. To make this more clear, consider the
    following example in the same stream s:

    ```python
    >>> tsMatcher = search.serial.TransformedSegmentMatcher(s, 'includeAll')
    >>> found = tsMatcher.find([4, 0, 4])
    >>> [(seg.segment, seg.activeSegment.pitchClasses()) for seg in found]
    [([<music21.note.Note G>, <music21.chord.Chord B4 G5 A5>], [7, 11, 7])]
    ```

    Above, the pitch classes of the found segment are read in the order 7, 11, 7, 9.
    Because a subsequence of this, [7, 11, 7],
    is an inversion of the search segment, [4, 0, 4], and furthermore,
    the first 7 is part of the first note of the segment (G), and
    the last 7 is part of the last chord of the segment, the found segment is
    matched to the segment being searched for.

[`TransformedSegmentMatcher`](#music21.search.serial.TransformedSegmentMatcher "music21.search.serial.TransformedSegmentMatcher") bases

* [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher")

[`TransformedSegmentMatcher`](#music21.search.serial.TransformedSegmentMatcher "music21.search.serial.TransformedSegmentMatcher") read/write properties

Read/write properties inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`includeChords`](#music21.search.serial.SegmentMatcher.includeChords "music21.search.serial.SegmentMatcher.includeChords") | * [`reps`](#music21.search.serial.SegmentMatcher.reps "music21.search.serial.SegmentMatcher.reps") |  |

[`TransformedSegmentMatcher`](#music21.search.serial.TransformedSegmentMatcher "music21.search.serial.TransformedSegmentMatcher") methods

TransformedSegmentMatcher.checkSearchedAlready(*unNormalizedSearchSegment*)[[source]](../_modules/music21/search/serial.html#TransformedSegmentMatcher.checkSearchedAlready)
:   Here a segment is returned as searchedAlready if it is a transformation
    of a previous search segment.

    ```python
    >>> transMatcher = search.serial.TransformedSegmentMatcher(None)
    >>> transMatcher.checkSearchedAlready([0, 1, 2])
    False
    >>> transMatcher.checkSearchedAlready([0, 1, 2])
    True
    >>> transMatcher.checkSearchedAlready([0, 1, 3])
    False
    >>> transMatcher.checkSearchedAlready([3, 5, 6])  # RI of 0, 1, 3
    True
    ```

TransformedSegmentMatcher.equalSubset(*searchSegment*, *subsetToCheck*)[[source]](../_modules/music21/search/serial.html#TransformedSegmentMatcher.equalSubset)
:   Returns True if these are equal in some way.

    If is case two rows are equal if they have a zeroCenteredTransformation of the other.

    ```python
    >>> TSM = search.serial.TransformedSegmentMatcher(None)
    >>> TSM.equalSubset(TSM.normalize([3, 4, 5]), TSM.normalize([4, 5, 6]))
    True
    >>> TSM.equalSubset(TSM.normalize([0, 1, 2]), TSM.normalize([0, 1, 3]))
    False
    ```

static TransformedSegmentMatcher.getTransformations(*row1*, *row2*)[[source]](../_modules/music21/search/serial.html#TransformedSegmentMatcher.getTransformations)
:   Returns a list of transformations that transform row1 into row2

    Staticmethod:

    ```python
    >>> TSM = search.serial.TransformedSegmentMatcher
    ```

    ```python
    >>> TSM.getTransformations(TSM.normalize([3, 4, 5]), TSM.normalize([4, 5, 6]))
    [('P', 3), ('RI', 5)]
    >>> TSM.getTransformations(TSM.normalize(['12', 'B', 7]), TSM.normalize([0, 1, 5]))
    [('I', 0)]
    ```

static TransformedSegmentMatcher.normalize(*segment*)[[source]](../_modules/music21/search/serial.html#TransformedSegmentMatcher.normalize)
:   Normalize an input segment for searching. For this class changes to intervals

    Staticmethod:

    ```python
    >>> search.serial.TransformedSegmentMatcher.normalize([3, 4, 5])
    <music21.serial.ToneRow 345>
    >>> search.serial.TransformedSegmentMatcher.normalize(['12', 'B', 7])
    <music21.serial.ToneRow 0B7>
    ```

Methods inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`find()`](#music21.search.serial.SegmentMatcher.find "music21.search.serial.SegmentMatcher.find") * [`findOneIgnoreAll()`](#music21.search.serial.SegmentMatcher.findOneIgnoreAll "music21.search.serial.SegmentMatcher.findOneIgnoreAll") | * [`findOneOtherReps()`](#music21.search.serial.SegmentMatcher.findOneOtherReps "music21.search.serial.SegmentMatcher.findOneOtherReps") | * [`getContiguousSegmentsByLength()`](#music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength "music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength") |

## TransposedInvertedMultisetMatcher

class music21.search.serial.TransposedInvertedMultisetMatcher(*inputStream*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#TransposedInvertedMultisetMatcher)
:   Finds all instances of given multisets of pitch classes, with
    transpositions and inversions, within a `Stream`.
    A multiset is a generalization of a set, as described in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    The inputStream is `Stream`; as
    in [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher"),
    it can contain at most one `Score`, and
    its notes must be contained in measures. The multisetList is a list of multisets to
    be searched for, each multiset being given as a list of pitch classes. Note that the
    order of pitch classes given in a multiset
    does not matter. The reps and includeChords settings specify how
    repeated pitches and chords, respectively, are handled; the possible settings
    are the same as those in
    [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher")

    Returns a list of [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes")
    objects for some transposition or inversion of the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment"),
    interpreted as a multiset,
    matches at least one of the elements of the searchList,
    subject to the settings specified in reps and includeChords.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('c4')
    >>> n2 = note.Note('e-4')
    >>> n3 = note.Note('g4')
    >>> n4 = note.Note('e4')
    >>> n5 = note.Note('c4')
    >>> for n in [n1, n2, n3, n4]:
    ...     n.quarterLength = 1
    ...     s.append(n)
    >>> n5.quarterLength = 4
    >>> s.append(n5)
    >>> s = s.makeMeasures()
    >>> s.show()
    ```

    [![../_images/serial-findTransposedAndInvertedMultisets.png](../_images/serial-findTransposedAndInvertedMultisets.png)](../_images/serial-findTransposedAndInvertedMultisets.png)

    ```python
    >>> transposedMatcher = search.serial.TransposedInvertedMultisetMatcher(s, 'ignoreAll',
    ...                                                               includeChords=False)
    >>> majOrMinTriads = transposedMatcher.find([0, 3, 7])
    >>> majOrMinTriads
    [<music21.search.serial.ContiguousSegmentOfNotes ['C4', 'E-4', 'G4']>,
     <music21.search.serial.ContiguousSegmentOfNotes ['G4', 'E4', 'C4']>]
    ```

    Note that if we search for both kinds, we should only find each once.

    ```python
    >>> bothTriads = transposedMatcher.find([[0, 4, 7], [0, 3, 7]])
    >>> [(maj.segment, maj.startOffset) for maj in bothTriads]
    [([<music21.note.Note C>, <music21.note.Note E->, <music21.note.Note G>], 0.0),
     ([<music21.note.Note G>, <music21.note.Note E>, <music21.note.Note C>], 2.0)]
    ```

    In both these cases, the [0, 4, 7] search should have matched:

    ```python
    >>> [maj.matchedSegment for maj in bothTriads]
    [[0, 4, 7], [0, 4, 7]]
    ```

    Note that when we search for both [0, 4, 7] and [0, 3, 7], which are related to each other
    by the composition of an inversion and a transposition, each
    found segment is only matched to one
    of the multisets in the searchList; thus each found segment appears
    still appears at most once in the returned list
    of contiguous segments. Accordingly, calling
    [`matchedSegment`](#music21.search.serial.ContiguousSegmentOfNotes.matchedSegment "music21.search.serial.ContiguousSegmentOfNotes.matchedSegment")
    returns only one element of the searchList for each found segment.

[`TransposedInvertedMultisetMatcher`](#music21.search.serial.TransposedInvertedMultisetMatcher "music21.search.serial.TransposedInvertedMultisetMatcher") bases

* [`TransposedMultisetMatcher`](#music21.search.serial.TransposedMultisetMatcher "music21.search.serial.TransposedMultisetMatcher")
* [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher")

[`TransposedInvertedMultisetMatcher`](#music21.search.serial.TransposedInvertedMultisetMatcher "music21.search.serial.TransposedInvertedMultisetMatcher") read/write properties

Read/write properties inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`includeChords`](#music21.search.serial.SegmentMatcher.includeChords "music21.search.serial.SegmentMatcher.includeChords") | * [`reps`](#music21.search.serial.SegmentMatcher.reps "music21.search.serial.SegmentMatcher.reps") |  |

[`TransposedInvertedMultisetMatcher`](#music21.search.serial.TransposedInvertedMultisetMatcher "music21.search.serial.TransposedInvertedMultisetMatcher") methods

TransposedInvertedMultisetMatcher.checkSearchedAlready(*multiset*)[[source]](../_modules/music21/search/serial.html#TransposedInvertedMultisetMatcher.checkSearchedAlready)
:   since the parent class adds to the list, we check inversions
    first and then return the parent class result

TransposedInvertedMultisetMatcher.equalSubset(*searchSegment*, *subsetToCheck*)[[source]](../_modules/music21/search/serial.html#TransposedInvertedMultisetMatcher.equalSubset)
:   Returns True if there are the same number of each pitchClass in searchSegment
    as in subsetToCheck

Methods inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`find()`](#music21.search.serial.SegmentMatcher.find "music21.search.serial.SegmentMatcher.find") * [`findOneIgnoreAll()`](#music21.search.serial.SegmentMatcher.findOneIgnoreAll "music21.search.serial.SegmentMatcher.findOneIgnoreAll") | * [`findOneOtherReps()`](#music21.search.serial.SegmentMatcher.findOneOtherReps "music21.search.serial.SegmentMatcher.findOneOtherReps") * [`getContiguousSegmentsByLength()`](#music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength "music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength") | * [`normalize()`](#music21.search.serial.SegmentMatcher.normalize "music21.search.serial.SegmentMatcher.normalize") |

## TransposedMultisetMatcher

class music21.search.serial.TransposedMultisetMatcher(*inputStream*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#TransposedMultisetMatcher)
:   Finds all instances of given multisets of pitch classes, with transpositions,
    within a `Stream`. A multiset
    is a generalization of a set, as described in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    The inputStream is `Stream`; as
    in [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher"),
    the inputStream can contain at most one `Score`
    and its notes must be contained in measures.
    The searchList is a list of multisets to
    be searched for, each multiset being given as a list of pitch classes.
    Note that the order of pitch classes given in a multiset
    does not matter. The reps and includeChords settings specify how
    repeated pitches and chords, respectively, are handled; the
    possible settings are the same as those in
    [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher").

    Returns a list of [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") objects
    for some transposition of the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment"),
    interpreted as a multiset,
    matches at least one of the elements of the searchList,
    subject to the settings specified in reps and includeChords.

    ```python
    >>> part = stream.Part()
    >>> n1 = note.Note('c4')
    >>> n2 = note.Note('c#4')
    >>> n3 = note.Note('d4')
    >>> n4 = note.Note('e4')
    >>> n5 = note.Note('e-4')
    >>> n6 = note.Note('e4')
    >>> n7 = note.Note('d4')
    >>> for n in [n1, n2, n3, n4, n5, n6, n7]:
    ...    n.quarterLength = 2
    ...    part.repeatAppend(n, 2)
    >>> part = part.makeMeasures()
    >>> part.show()
    ```

    [![../_images/serial-findTransposedMultisets.png](../_images/serial-findTransposedMultisets.png)](../_images/serial-findTransposedMultisets.png)

    ```python
    >>> TMM = search.serial.TransposedMultisetMatcher(part, includeChords=False)
    >>> instanceList = TMM.find([[-9, -10, -11]])
    >>> for instance in instanceList:
    ...    (instance.activeSegment, instance.startMeasureNumber, instance.matchedSegment)
    ([0, 1, 2], 1, [-9, -10, -11])
    ([2, 4, 3], 3, [-9, -10, -11])
    ([3, 4, 2], 5, [-9, -10, -11])
    ```

[`TransposedMultisetMatcher`](#music21.search.serial.TransposedMultisetMatcher "music21.search.serial.TransposedMultisetMatcher") bases

* [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher")

[`TransposedMultisetMatcher`](#music21.search.serial.TransposedMultisetMatcher "music21.search.serial.TransposedMultisetMatcher") read/write properties

Read/write properties inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`includeChords`](#music21.search.serial.SegmentMatcher.includeChords "music21.search.serial.SegmentMatcher.includeChords") | * [`reps`](#music21.search.serial.SegmentMatcher.reps "music21.search.serial.SegmentMatcher.reps") |  |

[`TransposedMultisetMatcher`](#music21.search.serial.TransposedMultisetMatcher "music21.search.serial.TransposedMultisetMatcher") methods

TransposedMultisetMatcher.checkSearchedAlready(*multiset*)[[source]](../_modules/music21/search/serial.html#TransposedMultisetMatcher.checkSearchedAlready)
:   searched already uses counters.

TransposedMultisetMatcher.equalSubset(*searchSegment*, *subsetToCheck*)[[source]](../_modules/music21/search/serial.html#TransposedMultisetMatcher.equalSubset)
:   Returns True if there are the same number of each pitchClass in searchSegment
    as in subsetToCheck

Methods inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`find()`](#music21.search.serial.SegmentMatcher.find "music21.search.serial.SegmentMatcher.find") * [`findOneIgnoreAll()`](#music21.search.serial.SegmentMatcher.findOneIgnoreAll "music21.search.serial.SegmentMatcher.findOneIgnoreAll") | * [`findOneOtherReps()`](#music21.search.serial.SegmentMatcher.findOneOtherReps "music21.search.serial.SegmentMatcher.findOneOtherReps") * [`getContiguousSegmentsByLength()`](#music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength "music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength") | * [`normalize()`](#music21.search.serial.SegmentMatcher.normalize "music21.search.serial.SegmentMatcher.normalize") |

## TransposedSegmentMatcher

class music21.search.serial.TransposedSegmentMatcher(*inputStream*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#TransposedSegmentMatcher)
:   Finds all instances of given contiguous segments of pitch classes, with transpositions,
    within a `Stream`.

    The inputStream is a `Stream`; as
    in [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher"),
    the inputStream can contain at most one `Score` and
    its notes must be contained in measures. The searchList is a list of contiguous segments to
    be searched for, each segment being given as a list of pitch classes.
    The reps and includeChords settings specify how
    repeated pitches and chords, respectively, are handled; the possible settings
    are the same as those in
    [`ContiguousSegmentSearcher`](#music21.search.serial.ContiguousSegmentSearcher "music21.search.serial.ContiguousSegmentSearcher")

    Returns a list of [`ContiguousSegmentOfNotes`](#music21.search.serial.ContiguousSegmentOfNotes "music21.search.serial.ContiguousSegmentOfNotes") objects
    for which some transposition of the
    [`activeSegment`](#music21.search.serial.ContiguousSegmentOfNotes.activeSegment "music21.search.serial.ContiguousSegmentOfNotes.activeSegment") matches at
    least one of the elements of the searchList,
    subject to the settings specified in reps and includeChords.

    ```python
    >>> part = stream.Part()
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 6
    >>> part.append(n1)
    >>> n2 = note.Note('f4')
    >>> n2.quarterLength = 1
    >>> part.append(n2)
    >>> n3 = chord.Chord(['g4', 'b4'])
    >>> n3.quarterLength = 1
    >>> part.append(n3)
    >>> n4 = note.Note('g4')
    >>> n4.quarterLength = 1
    >>> part.repeatAppend(n4, 2)
    >>> n5 = note.Note('a4')
    >>> n5.quarterLength = 3
    >>> part.repeatAppend(n5, 2)
    >>> n6 = note.Note('b4')
    >>> n6.quarterLength = 1
    >>> part.append(n6)
    >>> n7 = note.Note('c5')
    >>> n7.quarterLength = 1
    >>> part.append(n7)
    >>> newPart = part.makeMeasures()
    >>> newPart.makeTies(inPlace=True)
    >>> newPart.show()
    ```

    [![../_images/serial-findTransposedSegments.png](../_images/serial-findTransposedSegments.png)](../_images/serial-findTransposedSegments.png)

    First, note that it is impossible, using the ‘ignoreAll’ setting,
    to find segments, transposed or not,
    with repeated pitch classes.

    ```python
    >>> matcher = search.serial.TransposedSegmentMatcher(newPart, 'ignoreAll')
    >>> matcher.find([0, 0])
    []
    ```

    A somewhat more interesting example is below.

    ```python
    >>> matcher = search.serial.TransposedSegmentMatcher(newPart, 'rowsOnly',
    ...                                                            includeChords=False)
    >>> halfStepList = matcher.find([0, 1])
    >>> L = [step.segment for step in halfStepList]
    >>> print(L)
    [[<music21.note.Note E>, <music21.note.Note F>],
     [<music21.note.Note B>, <music21.note.Note C>]]
    >>> [step.startMeasureNumber for step in halfStepList]
    [1, 5]
    ```

    In addition to calling the
    [`startMeasureNumber`](#music21.search.serial.ContiguousSegmentOfNotes.startMeasureNumber "music21.search.serial.ContiguousSegmentOfNotes.startMeasureNumber")
    property
    to return the measure numbers on which the half steps start, one may also call the
    [`measureNumber`](moduleBase.html#music21.base.Music21Object.measureNumber "music21.base.Music21Object.measureNumber") property of the
    first [`Note`](moduleNote.html#music21.note.Note "music21.note.Note") of each segment.

    ```python
    >>> s = stream.Stream()
    >>> s.repeatAppend(newPart, 2)  # s has two parts, each of which is a copy of newPart.
    ```

    ```python
    >>> sMatcher = search.serial.TransposedSegmentMatcher(s, includeChords=False)
    >>> wholeStepList = sMatcher.find([12, 2])
    >>> [(step.segment, step.startMeasureNumber, step.partNumber) for step in wholeStepList]
    [([<music21.note.Note G>, <music21.note.Note A>], 3, 0),
    ([<music21.note.Note A>, <music21.note.Note B>], 3, 0),
    ([<music21.note.Note G>, <music21.note.Note A>], 3, 1),
    ([<music21.note.Note A>, <music21.note.Note B>], 3, 1)]
    ```

    Including chords works similarly as in `findSegments`.

    ```python
    >>> sMatcher = search.serial.TransposedSegmentMatcher(newPart, includeChords=True)
    >>> foundSegments = sMatcher.find([4, 6, 'A'])
    >>> [seg.segment for seg in foundSegments]
    [[<music21.note.Note F>, <music21.chord.Chord G4 B4>]]
    ```

[`TransposedSegmentMatcher`](#music21.search.serial.TransposedSegmentMatcher "music21.search.serial.TransposedSegmentMatcher") bases

* [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher")

[`TransposedSegmentMatcher`](#music21.search.serial.TransposedSegmentMatcher "music21.search.serial.TransposedSegmentMatcher") read/write properties

Read/write properties inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`includeChords`](#music21.search.serial.SegmentMatcher.includeChords "music21.search.serial.SegmentMatcher.includeChords") | * [`reps`](#music21.search.serial.SegmentMatcher.reps "music21.search.serial.SegmentMatcher.reps") |  |

[`TransposedSegmentMatcher`](#music21.search.serial.TransposedSegmentMatcher "music21.search.serial.TransposedSegmentMatcher") methods

static TransposedSegmentMatcher.normalize(*segment*)[[source]](../_modules/music21/search/serial.html#TransposedSegmentMatcher.normalize)
:   Normalize an input segment for searching. For this class changes to intervals

    Staticmethod:

    ```python
    >>> search.serial.TransposedSegmentMatcher.normalize([3, 4, 5])
    '11'
    >>> search.serial.TransposedSegmentMatcher.normalize(['12', 'B', 7])
    'E8'
    ```

Methods inherited from [`SegmentMatcher`](#music21.search.serial.SegmentMatcher "music21.search.serial.SegmentMatcher"):

|  |  |  |
| --- | --- | --- |
| * [`checkSearchedAlready()`](#music21.search.serial.SegmentMatcher.checkSearchedAlready "music21.search.serial.SegmentMatcher.checkSearchedAlready") * [`equalSubset()`](#music21.search.serial.SegmentMatcher.equalSubset "music21.search.serial.SegmentMatcher.equalSubset") | * [`find()`](#music21.search.serial.SegmentMatcher.find "music21.search.serial.SegmentMatcher.find") * [`findOneIgnoreAll()`](#music21.search.serial.SegmentMatcher.findOneIgnoreAll "music21.search.serial.SegmentMatcher.findOneIgnoreAll") | * [`findOneOtherReps()`](#music21.search.serial.SegmentMatcher.findOneOtherReps "music21.search.serial.SegmentMatcher.findOneOtherReps") * [`getContiguousSegmentsByLength()`](#music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength "music21.search.serial.SegmentMatcher.getContiguousSegmentsByLength") |

## Functions

music21.search.serial.labelMultisets(*inputStream*, *multisetDict*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#labelMultisets)
:   Labels all instances of a given collection of multisets of pitch classes in a
    `Stream`. A multiset
    is a generalization of a set, as described in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    The multisetDict is a dictionary whose keys are names of
    the multisets to be searched for, and whose
    values are the segments of pitch classes. The values will be
    turned in to a segmentList, as in [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").
    All other settings are as in [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher") as well.

    Returns a deep copy of the inputStream
    with a [`Line`](moduleSpanner.html#music21.spanner.Line "music21.spanner.Line") connecting the first and last notes
    of each found multiset, and the first note of each found multiset
    labeled with a [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric"),
    the label being the key corresponding to the segment of pitch classes. One should make sure not
    to call this function with too large of a segmentDict, as a note being contained
    in too many segments will result in some spanners not showing.

    At the present time a relatively large number of multisets are
    found using the ‘ignoreAll’ setting,
    particularly when there are many repetitions of pitch classes (immediate or otherwise).
    As a result, it is possible that at points in the stream
    there will be more than six spanners active
    simultaneously, which may result in some
    spanners not showing correctly in XML format, or not at all.

    ```python
    >>> part = stream.Part()
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 4
    >>> n2 = note.Note('e4')
    >>> n2.quarterLength = 4
    >>> n3 = note.Note('f4')
    >>> n3.quarterLength = 4
    >>> n4 = note.Note('e4')
    >>> n4.quarterLength = 4
    >>> part.append(n1)
    >>> part.append(n2)
    >>> part.append(n3)
    >>> part.append(n4)
    >>> part = part.makeMeasures()
    >>> labeledPart = search.serial.labelMultisets(part, {'EEF':[4, 5, 4]},
    ...                                     reps='includeAll', includeChords=False)
    >>> labeledPart.show()
    ```

    [![../_images/serial-labelMultisets.png](../_images/serial-labelMultisets.png)](../_images/serial-labelMultisets.png)

    Note: the spanners above were moved manually so that they can
    be more easily distinguished from one another.

music21.search.serial.labelSegments(*inputStream*, *segmentDict*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#labelSegments)
:   Labels all instances of a given collection of segments of pitch classes in a
    `Stream`.

    The segmentDict is a dictionary whose keys are names of
    the segments to be searched for, and whose values are the segments of pitch classes.
    The values will be
    turned in to a segmentList, as in `findSegments()`.
    All other settings are as in `findSegments()` as well.

    Returns a deepcopy of the inputStream with a [`Line`](moduleSpanner.html#music21.spanner.Line "music21.spanner.Line")
    connecting the first and last notes
    of each found segment, and the first note of each found segment labeled
    with a [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric"),
    the label being the key corresponding to the segment of pitch classes.
    One should make sure not
    to call this function with too large of a segmentDict, as a note being contained
    in too many segments will result in some spanners not showing.

    ```python
    >>> part = stream.Part()
    >>> sig = meter.TimeSignature('2/4')
    >>> part.append(sig)
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 6
    >>> part.append(n1)
    >>> n2 = note.Note('f4')
    >>> n2.quarterLength = 1
    >>> part.append(n2)
    >>> n3 = chord.Chord(['g4', 'b4'])
    >>> n3.quarterLength = 1
    >>> part.append(n3)
    >>> n4 = note.Note('g4')
    >>> n4.quarterLength = 1
    >>> part.repeatAppend(n4, 2)
    >>> n5 = note.Note('a4')
    >>> n5.quarterLength = 3
    >>> part.repeatAppend(n5, 2)
    >>> n6 = note.Note('b4')
    >>> n6.quarterLength = 1
    >>> part.append(n6)
    >>> n7 = note.Note('c5')
    >>> n7.quarterLength = 1
    >>> part.append(n7)
    >>> newPart = part.makeMeasures()
    >>> newPart.makeTies(inPlace=True)
    ```

    We can then label the segment of pitch classes [7, 9, 11], which corresponds to a G,
    followed by an A,
    followed by a B. Let us call this segment “GAB”.

    ```python
    >>> labelGAB = search.serial.labelSegments(newPart, {'GAB':[7, 9, 11]},
    ...    includeChords=False)
    >>> labelGAB.show()
    ```

    [![../_images/serial-labelSegments.png](../_images/serial-labelSegments.png)](../_images/serial-labelSegments.png)

    ```python
    >>> len(labelGAB.getElementsByClass(spanner.Line))
    1
    ```

music21.search.serial.labelTransformedSegments(*inputStream*, *segmentDict*, *reps='skipConsecutive'*, *includeChords=True*, *convention='original'*)[[source]](../_modules/music21/search/serial.html#labelTransformedSegments)
:   Labels all instances of a given collection of segments of pitch classes,
    with transformations, in a `Stream`.

    The segmentDict is a dictionary whose keys are names of the segments to be
    searched for, and whose values are the segments of pitch classes. The
    values will be turned in to a segmentList, as in
    `findTransposedSegments()`. The last argument specifies
    the convention (‘zero’ or ‘original’) used for naming serial
    transformations, as explained in
    `zeroCenteredTransformation()` and
    `originalCenteredTransformation()`.

    All other settings are as in `findTransposedSegments()`
    as well.

    Returns a deep copy of the inputStream with a
    [`Line`](moduleSpanner.html#music21.spanner.Line "music21.spanner.Line") connecting the first and last notes of each
    found segment, and the first note of each found segment labeled with a
    [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric"), the label being the key corresponding to the
    segment of pitch classes. One should make sure not to call this function
    with too large of a segmentDict, as a note being contained in too many
    segments will result in some spanners not showing.

    ```python
    >>> c1 = chord.Chord(['c#4', 'e4'])
    >>> c2 = chord.Chord(['d#4', 'f4'])
    >>> c3 = chord.Chord(['e4', 'g4'])
    >>> chordList = [c1, c2, c3]
    >>> part = stream.Part()
    >>> for c in chordList:
    ...    c.quarterLength = 4
    ...    part.append(c)
    >>> part = part.makeMeasures()
    >>> labeledPart = search.serial.labelTransformedSegments(part, {'row':[2, 5, 4]})
    >>> labeledPart.show()
    ```

    [![../_images/serial-labelTransformedSegments.png](../_images/serial-labelTransformedSegments.png)](../_images/serial-labelTransformedSegments.png)

    Note: the spanners above were moved manually so that they can be more easily
    distinguished from one another.

music21.search.serial.labelTransposedAndInvertedMultisets(*inputStream*, *multisetDict*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#labelTransposedAndInvertedMultisets)
:   Labels all instances of a given collection of multisets, with
    transpositions and inversions, of pitch classes in a
    `Stream`.

    A multiset is a generalization of a set, as described in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    The multisetDict is a dictionary whose keys are names of the multisets to
    be searched for, and whose values are the segments of pitch classes. The
    values will be turned in to a segmentList, as in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    All other settings are as in
    `findTransposedMultisets()` as well.

    Returns a deep copy of the inputStream with a
    [`Line`](moduleSpanner.html#music21.spanner.Line "music21.spanner.Line") connecting the first and last notes of each
    found multiset, and the first note of each found multiset labeled with a
    [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric"), the label being the key corresponding to the
    segment of pitch classes. One should make sure not to call this function
    with too large of a segmentDict, as a note being contained in too many
    segments will result in some spanners not showing.

    At the present time a relatively large number of multisets are found using
    the ‘ignoreAll’ setting, particularly when there are many repetitions of
    pitch classes (immediate or otherwise).

    As a result, it is possible that at points in the stream there will be more
    than six spanners active simultaneously, which may result in some spanners
    not showing correctly in XML format, or not at all.

    ```python
    >>> s = stream.Stream()
    >>> n1 = note.Note('c4')
    >>> n2 = note.Note('e-4')
    >>> n3 = note.Note('g4')
    >>> n4 = note.Note('e4')
    >>> n5 = note.Note('c4')
    >>> for n in [n1, n2, n3, n4]:
    ...     n.quarterLength = 1
    ...     s.append(n)
    >>> n5.quarterLength = 4
    >>> s.append(n5)
    >>> s = s.makeMeasures()
    ```

    ```python
    >>> l = search.serial.labelTransposedAndInvertedMultisets
    >>> l(s, {'triad':[0, 4, 7]}, includeChords=False).show()
    ```

    [![../_images/serial-labelTransposedAndInvertedMultisets.png](../_images/serial-labelTransposedAndInvertedMultisets.png)](../_images/serial-labelTransposedAndInvertedMultisets.png)

    Note: the spanners above were moved manually so that they can be more
    easily distinguished from one another.

music21.search.serial.labelTransposedMultisets(*inputStream*, *multisetDict*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#labelTransposedMultisets)
:   Labels all instances of a given collection of multisets, with
    transpositions, of pitch classes in a `Stream`.

    A multiset is a generalization of a set, as described in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    The multisetDict is a dictionary whose keys are names of the multisets to
    be searched for, and whose values are the segments of pitch classes. The
    values will be turned in to a segmentList, as in
    [`MultisetSegmentMatcher`](#music21.search.serial.MultisetSegmentMatcher "music21.search.serial.MultisetSegmentMatcher").

    All other settings are as in
    `findTransposedMultisets()` as well.

    Returns a deep copy of the inputStream with a
    [`Line`](moduleSpanner.html#music21.spanner.Line "music21.spanner.Line") connecting the first and last notes of each
    found multiset, and the first note of each found multiset labeled with a
    [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric"), the label being the key corresponding to the
    segment of pitch classes. One should make sure not to call this function
    with too large of a segmentDict, as a note being contained in too many
    segments will result in some spanners not showing.

    At the present time a relatively large number of multisets are found using
    the ‘ignoreAll’ setting, particularly when there are many repetitions of
    pitch classes (immediate or otherwise). As a result, it is possible that at
    points in the stream there will be more than six spanners active
    simultaneously, which may result in some spanners not showing correctly in
    XML format, or not at all.

    As a diversion, instead of using this tool on atonal music, let us do so on
    Bach.

    We can label all instances of three of the same pitch classes occurring in
    a row in one of the chorales.

    We learn the obvious - it appears that the alto section would be the most
    bored while performing this chorale.

    ```python
    >>> bach = corpus.parse('bach/bwv57.8')
    >>> bachLabeled = search.serial.labelTransposedMultisets(bach,
    ...                                               {'x3': [0, 0, 0]},
    ...                                               reps='includeAll',
    ...                                               includeChords=False)
    >>> bachLabeled.show()
    ```

    [![../_images/serial-labelTransposedMultisets.png](../_images/serial-labelTransposedMultisets.png)](../_images/serial-labelTransposedMultisets.png)

    Note: the spanners above were moved manually so that they can be more
    easily distinguished from one another.

music21.search.serial.labelTransposedSegments(*inputStream*, *segmentDict*, *reps='skipConsecutive'*, *includeChords=True*)[[source]](../_modules/music21/search/serial.html#labelTransposedSegments)
:   Labels all instances of a given collection of segments of pitch classes,
    with transpositions, in a `Stream`.

    The segmentDict is a dictionary whose keys are names of the segments to be
    searched for, and whose values are the segments of pitch classes. The
    values will be turned in to a segmentList, as in
    `findTransposedSegments()`. All other settings are as
    in `findTransposedSegments()` as well.

    Returns a deep copy of the inputStream with a
    [`Line`](moduleSpanner.html#music21.spanner.Line "music21.spanner.Line") connecting the first and last notes of each
    found segment, and the first note of each found segment labeled with a
    [`Lyric`](moduleNote.html#music21.note.Lyric "music21.note.Lyric"), the label being the key corresponding to the
    segment of pitch classes. One should make sure not to call this function
    with too large of a segmentDict, as a note being contained in too many
    segments will result in some spanners not showing.

    ```python
    >>> part = stream.Part()
    >>> n1 = note.Note('e4')
    >>> n1.quarterLength = 6
    >>> part.append(n1)
    >>> n2 = note.Note('f4')
    >>> n2.quarterLength = 1
    >>> part.append(n2)
    >>> n3 = chord.Chord(['g4', 'b4'])
    >>> n3.quarterLength = 1
    >>> part.append(n3)
    >>> n4 = note.Note('g4')
    >>> n4.quarterLength = 1
    >>> part.repeatAppend(n4, 2)
    >>> n5 = note.Note('a4')
    >>> n5.quarterLength = 3
    >>> part.repeatAppend(n5, 2)
    >>> n6 = note.Note('b4')
    >>> n6.quarterLength = 1
    >>> part.append(n6)
    >>> n7 = note.Note('c5')
    >>> n7.quarterLength = 1
    >>> part.append(n7)
    >>> newPart = part.makeMeasures()
    >>> newPart.makeTies(inPlace=True)
    ```

    We have a soprano line; let us now form a bass line.

    ```python
    >>> bass = stream.Part()
    >>> n8 = note.Note('c3')
    >>> n8.quarterLength = 4
    >>> bass.append(n8)
    >>> r1 = note.Rest()
    >>> r1.quarterLength = 4
    >>> bass.append(r1)
    >>> n9 = note.Note('b2')
    >>> n9.quarterLength = 4
    >>> bass.append(n9)
    >>> r2 = note.Rest()
    >>> r2.quarterLength = 4
    >>> bass.append(r2)
    >>> n10 = note.Note('c3')
    >>> n10.quarterLength = 4
    >>> bass.append(n10)
    >>> newBass = bass.makeMeasures()
    >>> sc = stream.Score()
    >>> import copy
    >>> sc.insert(0, copy.deepcopy(newPart))
    >>> sc.insert(0, copy.deepcopy(newBass))
    >>> labeledSC = search.serial.labelTransposedSegments(sc, {'half':[0, 1]}, 'rowsOnly')
    >>> labeledSC.show()
    ```

    [![../_images/serial-labelTransposedSegments.png](../_images/serial-labelTransposedSegments.png)](../_images/serial-labelTransposedSegments.png)
